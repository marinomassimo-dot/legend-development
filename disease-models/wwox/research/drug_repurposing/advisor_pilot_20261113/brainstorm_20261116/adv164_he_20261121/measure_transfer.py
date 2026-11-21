"""ADV-164 (HE, 2026-11-21): transfer check of `scout_daily.py --gene-anchor` on two reopen rows that did not inform its design.
Reads the FROZEN spec (FROZEN_SPEC_ADV164_HE_20261121.json, committed before this script was run), runs each arm on each route
at a matched budget (the scout's page of 25 records, relevance order) and writes the raw answers. Retrieval counts only: no reading, no claim.
Public Europe PMC and PubMed routes, generic client name, no contact parameter, no key.
Usage: python3 -I measure_transfer.py <spec.json> <out.json>"""
import json, sys, time, urllib.parse, urllib.request

UA = "legend-research-client"
CAP = 25
spec = json.load(open(sys.argv[1]))


def get(url):
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001
            err = repr(e)[:160]
            time.sleep(2 + 3 * k)
    return {"_error": err}


def epmc(q):
    d = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=lite&pageSize=1000&query=" + urllib.parse.quote(q))
    if "_error" in d:
        return {"error": d["_error"]}
    res = d["resultList"]["result"]
    return {"hitCount": d.get("hitCount"), "ids": [x.get("pmid") or ("EPMC:" + str(x.get("id"))) for x in res],
            "titles": {(x.get("pmid") or ("EPMC:" + str(x.get("id")))): (x.get("title") or "")[:160] + " (" + str(x.get("pubYear")) + ")" for x in res[:CAP]}}


def pubmed(q):
    d = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "retmode": "json", "retmax": "1000", "sort": "relevance", "term": q}))
    if "_error" in d:
        return {"error": d["_error"]}
    r = d["esearchresult"]
    ids = r["idlist"]
    titles = {}
    if ids[:CAP]:
        s = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(
            {"db": "pubmed", "retmode": "json", "id": ",".join(ids[:CAP])}))
        if "result" in s:
            titles = {i: (s["result"][i].get("title") or "")[:160] + " (" + (s["result"][i].get("pubdate") or "")[:4] + ")" for i in ids[:CAP] if i in s["result"]}
    return {"hitCount": r["count"], "ids": ids, "titles": titles}


out = {"cap": CAP, "rows": {}}
for row in spec["rows"]:
    pos = {p["pmid"] for p in row["positives"]}
    o = out["rows"][row["id"]] = {"positives_n": len(pos), "arms": {}}
    for arm, qs in row["arms"].items():
        for route, fn in (("epmc", epmc), ("pubmed", pubmed)):
            res = fn(qs[route])
            time.sleep(0.5)
            if "error" in res:
                o["arms"][f"{arm}/{route}"] = {"query": qs[route], "error": res["error"]}
                continue
            top = res["ids"][:CAP]
            o["arms"][f"{arm}/{route}"] = {
                "query": qs[route], "hitCount": res["hitCount"], "returned_all": len(res["ids"]),
                "positives_in_all": sorted(pos & set(res["ids"])), "positives_in_top": sorted(pos & set(top)),
                "top_ids": top, "top_titles": res["titles"],
                "hurt_in_all": sorted(set(row.get("hurt", [])) & set(res["ids"]))}
    json.dump(out, open(sys.argv[2], "w"), indent=1)
json.dump(out, open(sys.argv[2], "w"), indent=1)
for r, o in out["rows"].items():
    for a, v in o["arms"].items():
        print(r, a, "| ERROR " + v["error"] if "error" in v else f"| hits {v['hitCount']} | pos(all) {len(v['positives_in_all'])}/{o['positives_n']} | pos(top{CAP}) {len(v['positives_in_top'])} | {v['query']}")
