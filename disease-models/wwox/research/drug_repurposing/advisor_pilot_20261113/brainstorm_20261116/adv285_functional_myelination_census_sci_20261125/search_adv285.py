#!/usr/bin/env python3
"""ADV-285 step 0 searches: PubMed (esearch) and Europe PMC REST (search), strings frozen in PREREG_ADV285_SCI_20261125.md.
Usage (python3 -I -P -E): search_adv285.py <outdir>. Public GET only; no e-mail or identity is sent; a non-200, challenge page or timeout is recorded as a route result."""
import json, sys, time, urllib.parse, urllib.request, os, csv, hashlib
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
FN = '"conduction velocity" OR "compound action potential" OR "evoked potential" OR "evoked potentials" OR "visual evoked" OR "auditory brainstem"'
S = {
 "S1": '(WWOX OR Wwox) AND ("conduction velocity" OR "compound action potential" OR "evoked potential" OR "evoked potentials" OR "visual evoked" OR "auditory brainstem" OR latency)',
 "S2": '(WWOX OR Wwox) AND (myelin* OR oligodendrocyte* OR "white matter" OR hypomyelinat* OR leukodystroph*)',
 "S3": '(WWOX OR SCAR12 OR WOREE) AND ("evoked potential" OR "evoked potentials" OR VEP OR ABR OR "nerve conduction" OR "brainstem auditory" OR "visual evoked")',
 "S4": '(hypomyelinat* OR dysmyelinat* OR leukodystroph* OR "Pelizaeus-Merzbacher" OR shiverer OR "vanishing white matter" OR "Charcot-Marie-Tooth") AND (' + FN + ')',
 "S5": '(clemastine OR miconazole OR benztropine OR clobetasol OR quetiapine OR guanabenz OR sephin1 OR ISRIB OR ibudilast OR "thyroid hormone" OR lactate OR "ketogenic") AND (myelin* OR oligodendrocyte*) AND ("compound action potential" OR "conduction velocity" OR "evoked potential" OR "evoked potentials" OR "visual evoked" OR latency)',
}
def get(url):
    r = urllib.request.Request(url, headers={"User-Agent": "legend-census/1.0"})
    try:
        with urllib.request.urlopen(r, timeout=60) as h:
            return h.status, h.read().decode("utf-8", "replace")
    except Exception as e:
        return getattr(e, "code", "ERR"), str(e)
res = {}; log = []
for k, q in S.items():
    st, b = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=3000&term=" + urllib.parse.quote(q))
    pm = []
    if st == 200:
        j = json.loads(b)["esearchresult"]; pm = j["idlist"]; cnt = j["count"]
    else:
        cnt = "NA"
    log.append([k, "PubMed", st, cnt, len(pm)])
    time.sleep(0.5)
    eq = "TITLE_ABS:(" + q + ")"
    em = []; ec = "NA"; st2 = None; cur = "*"
    while True:
        st2, b = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&pageSize=1000&resultType=idlist&cursorMark=" + urllib.parse.quote(cur) + "&query=" + urllib.parse.quote(eq))
        if st2 != 200: break
        j = json.loads(b); ec = j["hitCount"]
        em += [r["pmid"] for r in j["resultList"]["result"] if r.get("pmid")]
        nxt = j.get("nextCursorMark")
        if not nxt or nxt == cur or len(j["resultList"]["result"]) == 0: break
        cur = nxt
    log.append([k, "EuropePMC", st2, ec, len(em)])
    res[k] = (pm, em)
    time.sleep(0.5)
with open(f"{out}/route_counts_adv285.tsv", "w", newline="") as h:
    w = csv.writer(h, delimiter="\t"); w.writerow(["string", "route", "http_status", "reported_count", "pmids_collected"]); w.writerows(log)
rows = []
for k, (pm, em) in res.items():
    a, b = set(pm), set(em)
    rows.append([k, len(a), len(b), len(a & b), len(a - b), len(b - a), len(a | b)])
with open(f"{out}/overlap_adv285.tsv", "w", newline="") as h:
    w = csv.writer(h, delimiter="\t"); w.writerow(["string", "pubmed", "europepmc", "both", "pubmed_only", "europepmc_only", "union"]); w.writerows(rows)
allp = {}
for k, (pm, em) in res.items():
    for p in set(pm) | set(em):
        allp.setdefault(p, []).append(k + ("P" if p in pm else "") + ("E" if p in em else ""))
with open(f"{out}/union_pmids_adv285.tsv", "w", newline="") as h:
    w = csv.writer(h, delimiter="\t"); w.writerow(["pmid", "strings_and_routes"])
    for p in sorted(allp, key=int): w.writerow([p, ";".join(allp[p])])
for r in log: print(r)
for r in rows: print(r)
print("union", len(allp))
