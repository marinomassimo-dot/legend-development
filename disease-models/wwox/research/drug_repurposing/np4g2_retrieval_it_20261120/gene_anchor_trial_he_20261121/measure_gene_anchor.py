"""HE trial of the scout's opt-in gene-anchor on the NP4G2 reopen row, against IT's recall set K_core (29 records).
Arms: B = the query the scout built before (TITLE_ABS:opc AND TITLE_ABS:drg); G = the same with TITLE_ABS:WWOX first (what --gene-anchor builds).
Each arm run with and without the scout's two-year window. Europe PMC public search, generic client name, no contact parameter, no key.
Usage: python3 measure_gene_anchor.py <out.json>   Reference-genotype class only; retrieval counts, not a reading."""
import json, sys, time, urllib.parse, urllib.request, pathlib, csv

UA = "legend-research-client"
HERE = pathlib.Path(__file__).resolve().parent
K = [r for r in csv.DictReader(open(HERE.parent / "K_core_record_ids.tsv"), delimiter="\t")]
SINCE, UNTIL = "2024-11-20", "2026-11-20"
ARMS = {"B": "TITLE_ABS:opc AND TITLE_ABS:drg", "G": "TITLE_ABS:WWOX AND TITLE_ABS:opc AND TITLE_ABS:drg"}


def search(q):
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=lite&pageSize=1000&query=" + urllib.parse.quote(q)
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                d = json.loads(r.read().decode())
            return d.get("hitCount"), {x.get("pmid") for x in d["resultList"]["result"] if x.get("pmid")}
        except Exception as e:  # noqa: BLE001
            time.sleep(2 + 3 * k)
    return None, None   # recorded as an error, never as zero hits


def pubmed(term, window):
    """Second route (Europe PMC answered 500 on 2026-11-21): the same two arms as PubMed title/abstract queries. All 28 PMIDs of K_core are PubMed records; the preprint is not."""
    p = {"db": "pubmed", "retmode": "json", "retmax": "1000", "term": term}
    if window:
        p.update(datetype="pdat", mindate=SINCE.replace("-", "/"), maxdate=UNTIL.replace("-", "/"))
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(p)
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                d = json.loads(r.read().decode())["esearchresult"]
            return d["count"], set(d["idlist"])
        except Exception:  # noqa: BLE001
            time.sleep(2 + 3 * k)
    return None, None


PM_ARMS = {"B": "opc[tiab] AND drg[tiab]", "G": "wwox[tiab] AND opc[tiab] AND drg[tiab]",
           "G1": "wwox[tiab] AND opc[tiab]",   # gene + the first object only (what the epmc builder keeps if the gene takes one of its two slots)
           "G1b": "wwox[tiab] AND drg[tiab]", "GA": "wwox[tiab] AND (opc[tiab] OR drg[tiab])",
           # the no-object branch's kind of query (subject words, as for NP4G1/NP4G3), without and with the gene
           "S": "oligodendrocyte[tiab] AND differentiation[tiab]", "SG": "wwox[tiab] AND oligodendrocyte[tiab]",
           # what a revised flag can build from the row text: gene + the row's top subject word (key_terms with the form words skipped)
           "GD": "wwox[tiab] AND differentiation[tiab]", "D": "differentiation[tiab]"}
out = {}
for arm, q in PM_ARMS.items():
    for win in ("all years", "scout window"):
        hits, pm = pubmed(q, win == "scout window")
        key = f"PubMed {arm} / {win}"
        if pm is None:
            out[key] = {"query": q, "error": "PubMed did not answer (3 tries)"}; continue
        found = [r["paper"] for r in K if r["pmid"] and r["pmid"] in pm]
        out[key] = {"query": q, "hitCount": hits, "K_core_found": found, "n_found": len(found), "of": sum(1 for r in K if r["pmid"]),
                    "K_core_in_window": sum(1 for r in K if r["pmid"] and SINCE[:4] <= r["year"] <= UNTIL[:4])}
        time.sleep(0.5)
        json.dump(out, open(sys.argv[1], "w"), indent=1)
for arm, q in ({} if "--no-epmc" in sys.argv else ARMS).items():
    for win in ("all years", "scout window"):
        full = q if win == "all years" else f"({q}) AND FIRST_PDATE:[{SINCE} TO {UNTIL}]"
        hits, pm = search(full)
        if pm is None:
            out[f"{arm} / {win}"] = {"query": full, "error": "Europe PMC did not answer (3 tries)"}
            json.dump(out, open(sys.argv[1], "w"), indent=1)
            continue
        found = [r["paper"] for r in K if r["pmid"] and r["pmid"] in pm]
        out[f"{arm} / {win}"] = {"query": full, "hitCount": hits, "K_core_found": found, "n_found": len(found), "of": sum(1 for r in K if r["pmid"]),
                                 "K_core_in_window": sum(1 for r in K if r["pmid"] and SINCE[:4] <= r["year"] <= UNTIL[:4])}
        json.dump(out, open(sys.argv[1], "w"), indent=1)
        time.sleep(0.5)
json.dump(out, open(sys.argv[1], "w"), indent=1)
for k, v in out.items():
    if "error" in v:
        print(k, "| ERROR", v["error"]); continue
    print(k, "| hitCount", v["hitCount"], "| K_core found", v["n_found"], "of", v["of"], v["K_core_found"])
