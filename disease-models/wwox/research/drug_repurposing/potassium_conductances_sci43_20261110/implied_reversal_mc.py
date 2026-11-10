"""SCI43 S7: uncertainty of the implied reversal (see S7_PREREGISTRATION.md, fixed and committed before this ran).
  python3 implied_reversal_mc.py -> output/implied_reversal_mc.tsv"""
import csv
import numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent
N, SEED = 200_000, 43
# case, Rin_old (mean, se), Rin_new, V_old, V_new
CASES = [
 ("Wwox WT->KO", (102.88, 11.74), (143.03, 8.88), (-79.25, 1.99), (-73.62, 1.36), "34634460 Table 1 (+/- read as SEM)"),
 ("Wwox WT->HT", (102.88, 11.74), (143.26, 15.49), (-79.25, 1.99), (-75.51, 1.81), "34634460 Table 1 (+/- read as SEM)"),
 ("Fmr1 WT->KO (calibration)", (172.7, 34.7 / 1.96), (124.5, 33.2 / 1.96), (-78.3, 0.0), (-82.0, 1.85), "preprint Fig 1; Rin 95% CI/1.96; rest SE from p 0.0457"),
 ("Kcnq2 cKO (calibration)", (239.0, 17.0), (299.0, 18.0), (-67.3, 0.8), (-65.7, 1.1), "28100740 Fig 2 legend, SEM"),
 ("Development L3 P7->P14", (405.85, 50.54), (213.42, 21.95), (-61.63, 1.39), (-69.96, 0.98), "30911152 Table 2, SEM"),
 ("Development L3 P14->P28", (213.42, 21.95), (110.28, 11.54), (-69.96, 0.98), (-73.02, 1.09), "30911152 Table 2, SEM"),
]
OFF = [0, 8, 13, 16]
def main():
    rng = np.random.default_rng(SEED)
    rows = []
    for name, r0, r1, v0, v1, src in CASES:
        R0 = rng.normal(*r0, N); R1 = rng.normal(*r1, N); V0 = rng.normal(*v0, N); V1 = rng.normal(*v1, N)
        ok = (R0 > 1) & (R1 > 1); R0, R1, V0, V1 = R0[ok], R1[ok], V0[ok], V1[ok]
        g0, g1 = 1000 / R0, 1000 / R1
        dG = g1 - g0
        ex = V0 + (V1 - V0) * g1 / dG
        ex = ex[np.isfinite(ex)]
        q = np.percentile(ex, [2.5, 50, 97.5])
        row = [name, src, f"{q[1]:.1f}", f"{q[0]:.1f}", f"{q[2]:.1f}", f"{q[2]-q[0]:.0f}", f"{np.mean(ex <= -85):.3f}", f"{np.mean(ex >= -80):.3f}", f"{ok.mean():.3f}"]
        row.append("; ".join(f"d{d}:{'yes' if q[0] <= -97.5 + d <= q[2] else 'no'}" for d in OFF))
        rows.append(row)
    with open(HERE / "output/implied_reversal_mc.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["case", "inputs", "median_E_x_mV", "p2.5", "p97.5", "width_95", "P_Ex_le_-85", "P_Ex_ge_-80", "fraction_draws_kept", "interval_contains_E_K_recorded_by_offset(-97.5+delta)"])
        w.writerows(rows)
    for r in rows: print(r[0], "| median", r[2], "95%", r[3], "to", r[4], "width", r[5], "| P<=-85", r[6], "P>=-80", r[7], "|", r[9])
main()
