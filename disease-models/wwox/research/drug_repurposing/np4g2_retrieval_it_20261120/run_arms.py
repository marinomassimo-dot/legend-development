"""NP4G2 retrieval comparison, arms B / S / M (written and frozen before any query; see ADV124_RESIDUAL_ROWS_IT_20261120.md section 6).
Plain public clients, generic user agent, no contact parameter, no key, no spend. Usage: python3 run_arms.py <outdir>
Reference-genotype class only; abstract-level retrieval, not a reading."""
import json, sys, time, urllib.parse, urllib.request, pathlib, re

UA = "legend-research-client"
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
EUT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SINCE = "2024-11-20"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for k in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            err = str(e)
            time.sleep(2 + 3 * k)
    return {"_error": err}


def epmc(query, n):
    d = get(f"{EPMC}?format=json&resultType=lite&pageSize={n}&query=" + urllib.parse.quote(query))
    rows = []
    for r in (d.get("resultList") or {}).get("result", []):
        rows.append({"key": ("PMID:" + r["pmid"]) if r.get("pmid") else f"{r.get('source')}:{r.get('id')}", "pmid": r.get("pmid", ""),
                     "doi": (r.get("doi") or "").lower(), "date": r.get("firstPublicationDate", ""), "title": (r.get("title") or "").strip(), "src": r.get("source", "")})
    return rows, d.get("hitCount"), d.get("_error")


def pubmed(term, n):
    d = get(f"{EUT}/esearch.fcgi?db=pubmed&retmode=json&retmax={n}&term=" + urllib.parse.quote(term))
    ids = (d.get("esearchresult") or {}).get("idlist", [])
    cnt = (d.get("esearchresult") or {}).get("count")
    time.sleep(0.4)
    rows = []
    if ids:
        s = get(f"{EUT}/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids))
        for i in ids:
            r = (s.get("result") or {}).get(i, {})
            rows.append({"key": "PMID:" + i, "pmid": i, "doi": "", "date": r.get("pubdate", ""), "title": (r.get("title") or "").strip(), "src": "MED"})
    time.sleep(0.4)
    return rows, cnt, d.get("_error")


def neutral(groups):
    """groups: list of OR-groups of phrases -> (pubmed syntax, epmc syntax)"""
    pm = " AND ".join("(" + " OR ".join(f'"{w}"[tiab]' if " " in w else (f"{w}[tiab]") for w in g) + ")" for g in groups)
    ep = " AND ".join("(" + " OR ".join(f'TITLE_ABS:"{w}"' if " " in w else f"TITLE_ABS:{w}" for w in g) + ")" for g in groups)
    return pm, ep


G = ["Wwox", "WWOX", "Wox1", "WOX1", "WW domain-containing oxidoreductase", "FRA16D"]
C = ["oligodendrocyte", "oligodendrocyte precursor", "OPC", "NG2", "Olig2", "myelin*", "hypomyelination", "myelin basic protein"]
M_QUERIES = [
    [G, C],
    [G, ["oligodendrocyte precursor", "OPC", "NG2"]],
    [G, ["oligodendrocyte differentiation", "oligodendrocyte maturation"]],
    [G, ["myelination", "hypomyelination", "demyelination", "remyelination"]],
    [G, ["coculture", "co-culture", "DRG", "dorsal root ganglion"], C],
    [G, ["conditional knockout", "Cre", "null mice", "knockout mice"], C],
    [G, ["organoid*", "iPSC", "stem cell"], C],
    [G, ["white matter", "leukodystrophy", "corpus callosum"]],
    [["WOREE", "WWOX-related epileptic encephalopathy", "WWOX related"], C],
    [["lde/lde", "Wwox-null", "Wwox null"], ["myelin*", "oligodendro*"]],
    [G, ["glia", "astrocyte", "microglia"], ["myelin*", "oligodendrocyte"]],
    [G, ["lipid", "sphingolipid", "ceramide", "cholesterol"], ["myelin*", "oligodendrocyte"]],
]

arms = {}
log = []
# B: the engine's own Europe PMC string for the reopened row (derived with scout_daily's functions; see B_query.txt)
bq = open(OUT.parent / "B_query.txt").read().strip()
rows, hits, err = epmc(bq, 25)
arms["B"] = rows; log.append({"arm": "B", "source": "epmc", "query": bq, "hits": hits, "returned": len(rows), "error": err})
# S: one field-tagged PubMed query
sq = "Wwox[tiab] AND (oligodendrocyte[tiab] OR myelin*[tiab])"
rows, hits, err = pubmed(sq, 50)
arms["S"] = rows; log.append({"arm": "S", "source": "pubmed", "query": sq, "hits": hits, "returned": len(rows), "error": err})
# M: concept set, both sources
m_rows = {}
for i, g in enumerate(M_QUERIES, 1):
    pm, ep = neutral(g)
    for src, q, fn in (("pubmed", pm, pubmed), ("epmc", ep, epmc)):
        rows, hits, err = fn(q, 50)
        log.append({"arm": "M", "q": i, "source": src, "query": q, "hits": hits, "returned": len(rows), "error": err})
        for r in rows:
            e = m_rows.setdefault(r["key"], dict(r, found_by=[], sources=set()))
            e["found_by"].append(i); e["sources"].add(src)
            if not e["title"] and r["title"]: e["title"] = r["title"]
            if not e["date"] and r["date"]: e["date"] = r["date"]
        time.sleep(0.5)
arms["M"] = [dict(v, sources=sorted(v["sources"])) for v in m_rows.values()]
for name, rows in arms.items():
    with open(OUT / f"arm_{name}.tsv", "w", encoding="utf-8") as f:
        f.write("key\tpmid\tdoi\tdate\tsrc\ttitle\tfound_by\n")
        for r in rows:
            f.write("\t".join([r["key"], r["pmid"], r["doi"], r["date"], r["src"], r["title"].replace("\t", " "), ",".join(map(str, r.get("found_by", [])))]) + "\n")
json.dump(log, open(OUT / "query_log.json", "w"), indent=1)
print({k: len(v) for k, v in arms.items()})
errs = [l for l in log if l.get("error")]
print("errors", len(errs))
