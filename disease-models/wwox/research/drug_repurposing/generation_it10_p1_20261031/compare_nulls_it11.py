#!/usr/bin/env python3
"""IT11 P1.2: does the choice of the null's matching covariate change the seed-specific candidates? Compares, per seed set, the z (Z_ind_robust) under the three IT10 nulls
(total degree, in-degree, v3 admissible in-degree) with the reach-matched null (null genes matched on the number of nodes with an F5-admissible walk to them).
Reports: rows seed-specific under the 3 nulls, rows seed-specific when the reach null replaces/joins them, rank agreement, and the effect size (Q_net_ind) of the rows that
change status, so that effect size and threshold sensitivity are read apart.  Writes results/null_sensitivity.tsv.
  compare_nulls_it11.py [--v4 DIR] [--reach DIR]
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, csv, gzip, collections, statistics
from pathlib import Path
HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--v4", default=str(HERE / "results_v4")); ap.add_argument("--reach", default=str(HERE / "results_v4_reach")); a = ap.parse_args()
rd = lambda p: {r["family_id"]: r for r in csv.DictReader(gzip.open(p, "rt"), delimiter="\t")}
def spearman(x, y):
    import numpy as np
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1])
rows = []
for sn in ("Q2_expression_tiersAB", "Q4_expression_tiersAB", "Q5_expression_tiersAB", "Q6_expression_tiersAB", "Q6_protein_tiersAB"):
    T = rd(Path(a.v4) / f"proposals_p1_{sn}.tsv.gz"); I = rd(Path(a.v4) / f"proposals_p1_{sn}_indeg.tsv.gz"); A = rd(Path(a.v4) / f"proposals_p1_{sn}_adm.tsv.gz")
    R = rd(Path(a.reach) / f"proposals_p1_{sn}_reach.tsv.gz")
    def spec(zs, sign):
        return all(z is not None and z * sign > 3 for z in zs)
    old, new, both3 = set(), set(), set()
    for f, t in T.items():
        z1 = float(t["Z_ind_robust"])
        if abs(z1) <= 3: continue
        sg = 1 if z1 > 0 else -1
        z2 = float(I[f]["Z_ind_robust"]) if f in I else None; z3 = float(A[f]["Z_ind_robust"]) if f in A else None; zr = float(R[f]["Z_ind_robust"]) if f in R else None
        if spec((z1, z2, z3), sg): old.add(f)
        if spec((z1, z2, z3, zr), sg): both3.add(f)
        if spec((z1, z2, zr), sg) : new.add(f)
    common = [f for f in T if f in R and abs(float(T[f]["Z_ind_robust"])) > 0 and abs(float(R[f]["Z_ind_robust"])) > 0]
    rho = spearman([float(T[f]["Z_ind_robust"]) for f in common], [float(R[f]["Z_ind_robust"]) for f in common]) if len(common) > 3 else float("nan")
    lost = old - both3
    lost_q = [abs(float(T[f]["Q_net_ind"])) for f in lost]; kept_q = [abs(float(T[f]["Q_net_ind"])) for f in both3]
    near = sum(1 for f in lost if f in R and abs(float(R[f]["Z_ind_robust"])) > 2.5)
    rows.append([sn, len(old), len(both3), len(lost), near, f"{rho:.3f}", f"{statistics.median(lost_q):.5f}" if lost_q else "", f"{statistics.median(kept_q):.5f}" if kept_q else ""])
with open(HERE / "results" / "null_sensitivity.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["seed_set", "specific_under_3_nulls", "specific_under_3_nulls_and_reach", "lost_by_adding_reach", "of_which_reach_z_between_2.5_and_3", "spearman_z_total_vs_reach", "median_abs_Q_lost", "median_abs_Q_kept"]); w.writerows(rows)
for r in rows: print(r)
