"""Dated addendum 2026-11-11 (after the Q1 verifier V6): TREK-1 has a reported residual current at acid pH.
Bagriantsev 2011 (21765396), Supplementary Table S1 (mouse TREK-1, oocytes, 22.5 C, n 30): pK1/2 7.51 +/- 0.06, Imin 0.25; the Hill coefficient is not tabulated.
Model: o(pH) = Imin + (1 - Imin) / (1 + 10^(n (pH50 - pH))). Closure f = 1 - o(pH0 - d)/o(pH0); loss = pool * f; pool 0.53 (Labbaf Rin knock-out, INFERENZA).
TASK-1 and TASK-3 Imin are not available in the verified tables, so they stay at 0 (an overestimate of closure).
Writes size_check_imin.tsv."""
import csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent
def o(ph, p50, n, imin): return imin + (1 - imin) / (1 + 10 ** (n * (p50 - ph)))
rows = []
for imin in (0.0, 0.25):
    for n in (0.7, 1, 2):
        for ph0 in (7.2, 7.4):
            for d in (0.1, 0.2, 0.3, 0.5):
                f = 1 - o(ph0 - d, 7.51, n, imin) / o(ph0, 7.51, n, imin)
                rows.append([imin, n, ph0, d, round(f, 3), round(0.53 * f, 3), "yes" if 0.53 * f >= 0.28 else "no"])
with open(HERE / "size_check_imin.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["Imin", "hill_n", "pH0", "delta_pH", "closure_f", "loss_L_pool0.53", "reaches_0.28"]); w.writerows(rows)
print("cells reaching 0.28 with Imin 0.25 up to 0.3 unit:", [r for r in rows if r[0] == 0.25 and r[3] <= 0.3 and r[6] == "yes"])
print("with Imin 0 up to 0.3 unit:", sorted({(r[1], r[2], r[3]) for r in rows if r[0] == 0.0 and r[3] <= 0.3 and r[6] == "yes"}))
print("Imin 0.25, 0.5 unit:", [(r[1], r[2], r[5]) for r in rows if r[0] == 0.25 and r[3] == 0.5])
