#!/usr/bin/env python3
"""Size check of SIZE_CHECK_PREREGISTRATION.md. Writes size_check.tsv and size_check_required_share.tsv."""
import csv, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PH50 = {"TASK-1": [6.6, 7.3, 7.4], "TASK-3": [6.3, 6.5], "TREK-1": [7.5]}
if len(sys.argv) > 1:  # optional override: channel=v1,v2;channel=v1
    PH50 = {kv.split("=")[0]: [float(x) for x in kv.split("=")[1].split(",")] for kv in sys.argv[1].split(";")}
PH0 = [7.2, 7.4]; D = [0.05, 0.1, 0.2, 0.3, 0.5]; N = [1, 2]; S = [0.05, 0.1, 0.23, 0.5]
TARGET = 0.28

def o(ph, ph50, n):
    return 1.0 / (1.0 + 10 ** (n * (ph50 - ph)))

def f_close(ph0, d, ph50, n):
    return 1.0 - o(ph0 - d, ph50, n) / o(ph0, ph50, n)

rows = []
for ch, vals in PH50.items():
    for p50 in vals:
        for ph0 in PH0:
            for n in N:
                for d in D:
                    f = f_close(ph0, d, p50, n)
                    row = [ch, p50, ph0, n, d, round(f, 4)]
                    row += [round(s * f, 4) for s in S]
                    row.append(round(TARGET / f, 2) if f > 0 else "inf")
                    rows.append(row)
hdr = ["channel", "pH50", "pH0", "hill_n", "delta_pH", "closure_f"] + [f"L_at_s{s}" for s in S] + ["required_share_s_star"]
with open(HERE / "size_check.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t"); w.writerow(hdr); w.writerows(rows)
# predictions
def cells(ch, cond):
    return [r for r in rows if r[0] == ch and cond(r)]
L = lambda r, s: r[5] * s
p = {}
p["S1"] = all(L(r, 0.5) < 0.01 for r in cells("TASK-3", lambda r: r[4] <= 0.2)) if "TASK-3" in PH50 else None
p["S1_max_L_at_s0.5"] = max((L(r, 0.5) for r in cells("TASK-3", lambda r: r[4] <= 0.2)), default=None)
t = [r for ch in ("TASK-1", "TREK-1") if ch in PH50 for r in cells(ch, lambda r: r[4] <= 0.2)]
p["S2"] = not any(L(r, 0.23) >= TARGET for r in t)
p["S3"] = all(r[-1] > 0.5 for r in t if r[3] == 1)
p["S3_min_s_star_n1_d<=0.2"] = min(r[-1] for r in t if r[3] == 1)
t5 = [r for ch in PH50 for r in cells(ch, lambda r: r[4] == 0.5 and r[3] == 2)]
p["S4_f_gt_0.8_only_when_d0.5_n2"] = (any(r[5] > 0.8 for r in t5) and not any(r[5] > 0.8 for r in rows if not (r[4] == 0.5 and r[3] == 2)))
p["any_cell_reaches_0.28_s<=0.5_d<=0.3"] = any(r[5] * 0.5 >= TARGET for r in rows if r[4] <= 0.3)
p["max_f_d<=0.2"] = max(r[5] for r in rows if r[4] <= 0.2)
p["max_f_d<=0.3"] = max(r[5] for r in rows if r[4] <= 0.3)
with open(HERE / "size_check_predictions.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t"); w.writerow(["item", "value"])
    for k, v in p.items(): w.writerow([k, v])
for k, v in p.items(): print(k, v)
