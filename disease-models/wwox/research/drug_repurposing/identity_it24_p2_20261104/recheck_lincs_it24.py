#!/usr/bin/env python3
"""IT24 P2: overlap of the stored IT23 top-20 lists (nine scenarios) with every LEGEND Q2/Q4/Q8 row that now has a structure (routes R0 to R3), by InChIKey skeleton.
Writes lincs_top20_recheck.json. Usage: recheck_lincs_it24.py"""
import sys
if len(sys.argv) > 1:
    print(__doc__); raise SystemExit(0)
import csv, collections, json
from pathlib import Path
H = Path(__file__).resolve().parent
R = list(csv.DictReader(open(H / "q248/identity_routes.tsv"), delimiter="\t"))
S = list(csv.DictReader(open(H.parent / "signature_it23_20261103/scenarios.tsv"), delimiter="\t"))
sk = collections.defaultdict(list)
for r in R:
    if r["inchikey"]:
        sk[r["inchikey"].split("-")[0]].append(r)
hits = [dict(scenario=s["scenario"], rank=s["rank"], pert_name=s["pert_name"], inchikey=s["inchikey"], legend=[(h["proposal_id"], h["route"]) for h in sk[s["inchikey"].split("-")[0]]])
        for s in S if s["inchikey"] and s["inchikey"].split("-")[0] in sk]
out = dict(top_rows=len(S), tops_with_unresolved_identity=sum(1 for s in S if not s["inchikey"]), legend_rows=len(R), legend_rows_with_structure=sum(1 for r in R if r["inchikey"]),
           legend_distinct_full_keys=len({r["inchikey"] for r in R if r["inchikey"]}), legend_distinct_skeletons=len(sk), top20_hits=hits)
json.dump(out, open(H / "lincs_top20_recheck.json", "w"), indent=1, sort_keys=True)
print(json.dumps({k: v for k, v in out.items() if k != "top20_hits"}), "hits:", len(hits))
