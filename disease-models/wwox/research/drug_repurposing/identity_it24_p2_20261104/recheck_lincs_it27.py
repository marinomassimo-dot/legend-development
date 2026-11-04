#!/usr/bin/env python3
"""IT27 P10: the IT24 top-20 recheck (recheck_lincs_it24.py) with the verified R4 identities added as one more route.
Same frozen lists (signature_it23_20261103/scenarios.tsv, nine scenarios, 180 rows), no new query. R4 = G-SRS name -> UNII -> structure, confirmed by a second actor
(identity_gsrs_it26_a1_20261104/identity_r4_it26.tsv, verify_rows.tsv); the InChIKey first block is the independently seen one. Writes lincs_top20_recheck_it27.json. Usage: recheck_lincs_it27.py"""
import sys
if len(sys.argv) > 1:
    print(__doc__); raise SystemExit(0)
import csv, collections, json
from pathlib import Path
H = Path(__file__).resolve().parent
D = H.parent
R = list(csv.DictReader(open(H / "q248/identity_routes.tsv"), delimiter="\t"))
S = list(csv.DictReader(open(D / "signature_it23_20261103/scenarios.tsv"), delimiter="\t"))
r4 = {r["family_id"]: r for r in csv.DictReader(open(D / "identity_gsrs_it26_a1_20261104/identity_r4_it26.tsv"), delimiter="\t")}
ver = {r["compound"].lower(): r for r in csv.DictReader(open(D / "identity_gsrs_it26_a1_20261104/verify_rows.tsv"), delimiter="\t") if r["verdict"] == "CONFIRMED"}
sk = collections.defaultdict(list)
for r in R:
    if r["inchikey"]:
        sk[r["inchikey"].split("-")[0]].append((r["proposal_id"], r["route"]))
new, amb = 0, []
for r in R:
    if r["family_id"] in r4 and not r["inchikey"]:
        v = ver.get(r["compound"].lower())
        k = v and v["independent_inchikey14"]
        if k:
            sk[k].append((r["proposal_id"], "R4_gsrs_unii_structure")); new += 1
            if v["catalogue_inchikey14"] and v["catalogue_inchikey14"] != k:
                amb.append(r["compound"])
before = {}
for r in R:
    if r["inchikey"]:
        before.setdefault(r["inchikey"].split("-")[0], 0)
hits = [dict(scenario=s["scenario"], rank=s["rank"], pert_name=s["pert_name"], inchikey=s["inchikey"], legend=sk[s["inchikey"].split("-")[0]])
        for s in S if s["inchikey"] and s["inchikey"].split("-")[0] in sk]
out = dict(top_rows=len(S), tops_with_unresolved_identity=sum(1 for s in S if not s["inchikey"]), legend_rows=len(R),
           legend_rows_with_structure_before=sum(1 for r in R if r["inchikey"]), r4_rows_added=new, legend_rows_with_structure_after=sum(1 for r in R if r["inchikey"]) + new,
           r4_catalogue_vs_independent_key_disagreements=amb, distinct_skeletons_before=len(before), distinct_skeletons_after=len(sk),
           top20_hits_with_r4=[h for h in hits if any(x[1].startswith("R4") for x in h["legend"])], top20_hits_all=hits)
json.dump(out, open(H / "lincs_top20_recheck_it27.json", "w"), indent=1, sort_keys=True)
print(json.dumps({k: v for k, v in out.items() if not k.startswith("top20")}), "hits:", len(hits), "R4 hits:", len(out["top20_hits_with_r4"]))
