#!/usr/bin/env python3
"""IT24 P10: what the existing attribution screen (attribution_screen_it21.attribution) would say for DGIdb-only rows whose GtoPdb ligand id is in the record's own concept ids (IT24 P2 route R3),
which family_ligands() does not use. Read-only; nothing in the generator is changed. Usage: r3_attribution_it24_p10.py OUT.tsv (LEGEND_CATALOG_CACHE must be set)"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, re, collections
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(DR / "generation_it21_p2_20261103"))
import attribution_screen_it21 as A
lig_, aff, kinds = A.load_gtopdb_affinities()
P = {x["proposal_id"]: x for x in csv.DictReader(open(DR / "generation_it22_p1_20261103/results_p4/proposals_it21.tsv"), delimiter="\t")}
H = {r["proposal_id"] for r in csv.DictReader(open(DR / "generation_it22_p1_20261103/results_p4/handoff_it21.tsv"), delimiter="\t")}
out, c = [], collections.Counter()
for r in csv.DictReader(open(DR / "identity_it24_p2_20261104/all/identity_routes.tsv"), delimiter="\t"):
    if not r["route"].startswith("R3"):
        continue
    p = P[r["proposal_id"]]; lid = re.search(r"ligand (\d+)", r["via"]).group(1)
    res = A.attribution({lid}, p["main_target"], aff, kinds)
    st = res.get("state") if isinstance(res, dict) else str(res)
    c[st] += 1
    out.append(dict(proposal_id=p["proposal_id"], compound=p["compound"], question=p["question"], hypothesis=p["hypothesis"], main_target=p["main_target"], ligand=lid, state_now=p["attribution_state"],
                    state_if_ligand_used=st, fold=(res.get("fold") if isinstance(res, dict) else ""), earlier_decision=p["earlier_decision"][:30], blocker=p["handoff_blocker"], handed_over="yes" if p["proposal_id"] in H else ""))
with open(sys.argv[1], "w", newline="") as fh:
    w = csv.DictWriter(fh, list(out[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
print(dict(c))
