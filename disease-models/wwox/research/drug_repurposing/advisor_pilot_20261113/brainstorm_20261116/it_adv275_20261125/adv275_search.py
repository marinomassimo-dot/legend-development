"""ADV-275 step 1: dated existence queries on GEO (E-utilities) and BioStudies/ArrayExpress.

Usage: adv275_search.py <work_dir>
Writes search_log.tsv rows next to this script and raw JSON into <work_dir>.
No e-mail, API key or browser identity is sent.
"""
import datetime
import json
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
BIOSTUDIES = "https://www.ebi.ac.uk/biostudies/api/v1/arrayexpress/search"

COMPOUNDS = {
    "valproate": ['"valproic acid"', "valproate", "VPA"],
    "vorinostat": ["vorinostat", "SAHA", '"suberoylanilide hydroxamic acid"'],
    "trichostatin": ['"trichostatin A"', "trichostatin", "TSA"],
    "entinostat": ["entinostat", "MS-275"],
    "panobinostat": ["panobinostat", "LBH589"],
    "belinostat": ["belinostat", "PXD101"],
    "romidepsin": ["romidepsin", "FK228", "depsipeptide"],
    "butyrate": ['"sodium butyrate"', "butyrate", "phenylbutyrate"],
    "other_named": ["givinostat", "mocetinostat", "RGFP966", "tubastatin", "tacedinaline", "CI-994",
                    "apicidin", "scriptaid", "quisinostat", "domatinostat"],
    "hdac_generic": ['"HDAC inhibitor"', '"histone deacetylase inhibitor"', '"HDAC inhibitors"',
                     '"histone deacetylase inhibitors"', "HDACi"],
}
NEURAL = ["neural", "neuron", "neurons", "neuronal", "neuroprogenitor", "neurosphere", "neurodevelopmental",
          "brain", "cortex", "cortical", "hippocampus", "hippocampal", "cerebellum", "cerebellar",
          "striatum", "striatal", '"spinal cord"', "astrocyte", "astrocytes", "oligodendrocyte",
          "microglia", "glia", "glial", "neuroblastoma", "glioma", "glioblastoma", "medulloblastoma",
          "cerebral", "forebrain", "amygdala", "hypothalamus"]
ORG = '("Homo sapiens"[Organism] OR "Mus musculus"[Organism])'


def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "research-query-client"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i + 1 < tries:
                time.sleep(5 * (i + 1))
                continue
            return e.code, b""
        except Exception as e:  # network error: recorded as a route result
            if i + 1 < tries:
                time.sleep(3)
                continue
            return 0, str(e).encode()


def geo_term(words, organism=ORG):
    compound = " OR ".join(f"{w}[All Fields]" for w in words)
    neural = " OR ".join(f"{w}[All Fields]" for w in NEURAL)
    term = f"({compound}) AND ({neural}) AND gse[ETYP]"
    return term + (f" AND {organism}" if organism else "")


def esearch(term):
    q = urllib.parse.urlencode({"db": "gds", "term": term, "retmax": 5000, "retmode": "json"})
    status, body = get(EUTILS + "esearch.fcgi?" + q)
    time.sleep(0.5)
    if status != 200:
        return status, None, [], {}
    d = json.loads(body)["esearchresult"]
    return status, int(d["count"]), d["idlist"], {"translation": d.get("querytranslation"),
                                                  "warnings": d.get("warninglist"), "errors": d.get("errorlist")}


def main():
    work = pathlib.Path(sys.argv[1])
    log = HERE / "search_log.tsv"
    rows = []
    today = datetime.date.today().isoformat()
    union, by_compound, meta = set(), {}, {}
    for name, words in COMPOUNDS.items():
        term = geo_term(words)
        status, count, ids, extra = esearch(term)
        by_compound[name] = ids
        meta[name] = extra
        union.update(ids)
        rows.append([today, "GEO esearch db=gds", name, term, f"HTTP {status}; count {count}; ids {len(ids)}"])
    allwords = [w for ws in COMPOUNDS.values() for w in ws]
    term = geo_term(allwords)
    status, count, ids, extra = esearch(term)
    rows.append([today, "GEO esearch db=gds (route 2: one combined query)", "all compounds", term,
                 f"HTTP {status}; count {count}; ids {len(ids)}; union of per-compound ids {len(union)}; "
                 f"only in combined {len(set(ids) - union)}; only in union {len(union - set(ids))}"])
    term_any = geo_term(allwords, organism=None)
    status, count_any, ids_any, _ = esearch(term_any)
    rows.append([today, "GEO esearch db=gds (no organism limit)", "all compounds", term_any,
                 f"HTTP {status}; count {count_any}; not human or mouse (counted, not read) {len(set(ids_any) - set(ids))}"])
    # summaries for every id
    summaries = {}
    idlist = sorted(set(ids) | union)
    for i in range(0, len(idlist), 200):
        q = urllib.parse.urlencode({"db": "gds", "id": ",".join(idlist[i:i + 200]), "retmode": "json"})
        status, body = get(EUTILS + "esummary.fcgi?" + q)
        time.sleep(0.5)
        if status == 200:
            res = json.loads(body)["result"]
            for u in res.get("uids", []):
                summaries[u] = res[u]
        else:
            rows.append([today, "GEO esummary", "batch", str(i), f"HTTP {status}"])
    rows.append([today, "GEO esummary", "all ids", f"{len(idlist)} ids", f"{len(summaries)} summaries"])
    (work / "geo_summaries.json").write_text(json.dumps(summaries))
    (work / "geo_by_compound.json").write_text(json.dumps(by_compound))
    (work / "geo_query_meta.json").write_text(json.dumps(meta))

    # ArrayExpress via BioStudies
    ae = {}
    queries = ["valproic acid", "valproate", "vorinostat", "SAHA", "trichostatin", "entinostat", "MS-275",
               "panobinostat", "belinostat", "romidepsin", "sodium butyrate", "givinostat",
               "histone deacetylase inhibitor", "HDAC inhibitor"]
    neural_block = "(neural OR neuron OR neuronal OR brain OR cortex OR hippocampus OR astrocyte OR neuroblastoma OR glioma OR glioblastoma OR organoid OR cerebellum)"
    for c in queries:
        query = f'"{c}" AND {neural_block}'
        hits, total, page, status = [], None, 1, 200
        while True:
            url = BIOSTUDIES + "?" + urllib.parse.urlencode({"query": query, "pageSize": 100, "page": page})
            status, body = get(url)
            time.sleep(0.5)
            if status != 200:
                break
            d = json.loads(body)
            total = d.get("totalHits")
            batch = d.get("hits", [])
            hits.extend(batch)
            if not batch or len(hits) >= total or page >= 20:
                break
            page += 1
        for h in hits:
            ae.setdefault(h["accession"], {"title": h.get("title"), "queries": []})["queries"].append(c)
        rows.append([today, "BioStudies arrayexpress search", c, query,
                     f"HTTP {status}; totalHits {total}; records enumerated {len({h['accession'] for h in hits})}"])
    (work / "ae_hits.json").write_text(json.dumps(ae))
    rows.append([today, "BioStudies arrayexpress search", "union", "all queries above",
                 f"{len(ae)} accessions; E-GEOD (GEO mirrors) {sum(a.startswith('E-GEOD') for a in ae)}"])

    new = not log.exists()
    with log.open("a") as f:
        if new:
            f.write("date\troute\tobject\tquery_or_scope\tresult\n")
        for r in rows:
            f.write("\t".join(str(x).replace("\t", " ") for x in r) + "\n")
    for r in rows:
        print(r[1], "|", r[2], "|", r[4])


if __name__ == "__main__":
    main()
