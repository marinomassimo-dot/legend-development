#!/usr/bin/env python3
"""v3 vs v4 (F5 member junction) on the seed-specific candidates: per seed set, the families seed-specific in all three nulls and not flagged in v3, how many remain,
which are lost, which are gained, and the main-target chain they rested on.  Writes v3_vs_v4_counts.tsv and v3_specific_lost_in_v4.tsv.
  compare_v3_v4.py [--v3 DIR] [--v4 DIR] [--out DIR]
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, csv, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = HERE.parent
ap = argparse.ArgumentParser()
ap.add_argument("--v3", default=str(DR / "generation_it9_p2_20261030" / "v3" / "results")); ap.add_argument("--v4", default=str(HERE / "results_v4")); ap.add_argument("--out", default=str(HERE / "results"))
a = ap.parse_args()
rd = lambda p: list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
def spec(path):
    d = {}
    for r in rd(path):
        if r["arm"] in ("opposes", "mimics") and r["seed_specific_all_three_nulls"] == "1" and "UNCERTAIN_ACTIVE_MOIETY" not in r["family_flags"]:
            d[(r["seed_set"], r["arm"], r["family_id"])] = r
    return d
s3, s4 = spec(Path(a.v3) / "v3_seed_specific_all_nulls.tsv"), spec(Path(a.v4) / "v3_seed_specific_all_nulls.tsv")
cnt = collections.defaultdict(lambda: collections.Counter())
lost = []
for k, r in s3.items():
    cnt[k[0]][("v3", k[1])] += 1
    if k in s4: cnt[k[0]][("kept", k[1])] += 1
    else:
        cnt[k[0]][("lost", k[1])] += 1; lost.append([k[0], k[1], r["family_id"], r["name"], r["Z_ind_robust_total_null"], r["edge_chain_main_target_to_seed_1"][:160]])
for k, r in s4.items():
    cnt[k[0]][("v4", k[1])] += 1
    if k not in s3: cnt[k[0]][("gained", k[1])] += 1
with open(Path(a.out) / "v3_vs_v4_counts.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["seed_set", "arm", "v3_specific", "kept_in_v4", "lost_in_v4", "gained_in_v4", "v4_specific"])
    for sn in sorted(cnt):
        for arm in ("opposes", "mimics"):
            c = cnt[sn]; w.writerow([sn, arm, c[("v3", arm)], c[("kept", arm)], c[("lost", arm)], c[("gained", arm)], c[("v4", arm)]])
with open(Path(a.out) / "v3_specific_lost_in_v4.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["seed_set", "arm", "family_id", "name", "z_total_null_v3", "v3_chain"]); w.writerows(sorted(lost))
for sn in sorted(cnt):
    c = cnt[sn]; print(sn, {a_: (c[("v3", a_)], c[("kept", a_)], c[("lost", a_)], c[("gained", a_)]) for a_ in ("opposes", "mimics")})
