"""ADV-272 step 1b: Europe PMC REST open-access flags for the top N ranked keys. One request at a time, 2 s apart, declared generic client, no e-mail.
Usage: oa_flags_adv272.py RANKING_TSV N OUT_TSV"""
import sys, csv, json, time, urllib.request, urllib.parse
if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
rk, n, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
keys = [r["study_key"] for r in csv.DictReader(open(rk), delimiter="\t")][:n]
rows = []
for k in keys:
    q = ("EXT_ID:%s AND SRC:MED" % k) if k.isdigit() else ("DOI:%s" % k)
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({"query": q, "format": "json", "resultType": "core"})
    req = urllib.request.Request(url, headers={"User-Agent": "legend-research-client/1.0 (plain request; no browser identity)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
        res = d.get("resultList", {}).get("result", [])
        if not res:
            rows.append((k, "not_indexed", "", "", "", "", "")); status = "no record"
        else:
            x = res[0]
            rows.append((k, "ok", x.get("isOpenAccess", ""), x.get("hasSuppl", ""), x.get("pmcid", ""), x.get("inPMC", ""), (x.get("title", "") or "")[:140]))
    except Exception as e:
        rows.append((k, "route_result:%s" % str(e)[:60], "", "", "", "", ""))
    time.sleep(2)
with open(out, "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("study_key status isOpenAccess hasSuppl pmcid inPMC title".split())
    w.writerows(rows)
for r in rows: print("\t".join(r))
