#!/usr/bin/env python3
"""Window statistics for Fig 7b (ethosuximide, raster) and Fig 7d (lithium, vector) of PMID 32000863, from the extracted tables.

Inputs: the outputs of extract_fig7d_vector.py (fig7d_vector_points.tsv) and of extract_fig7_raster.py run on the two raster
sources of Fig 7b (b_pdf.tsv from the article PDF image, b_png.tsv from the publisher PNG).
Fig 7b is the mean of the two raster readings where both exist (the two readings agree to a mean absolute difference of
about 0.01 to 0.03 stage; see validation.tsv), else the one that exists.

For each genotype and time window the script gives, with the sample sizes printed in the figure legends:
  D            mean over minutes of (PTZ mean - treated-arm mean), in Racine stage units, and D as a share of the PTZ mean;
  SD_curve     standard deviation of the PTZ mean curve across the minutes of the window (the figure's own scatter);
  SEM_P, SEM_T mean per-minute SEM of each arm (the upward error bar; bars shorter than the marker half height are not
               visible in the raster and are set to 0.11 for the upper bound, 0.055 for the other);
  SE_ind       standard error of D if the minutes of a window were independent:  sqrt(mean(se_t^2) / T)
  SE_corr      standard error of D if the minutes were perfectly correlated within animal:  mean(se_t). This is an upper
               limit: the SD of an average of correlated series cannot exceed the average of their SDs;
  t_ind, t_corr  D divided by each; the 0.05 two-sided critical t for the stated Ns is printed beside them;
  z_minutes    minutes with |D_t| > 1.96 * se_t, of the minutes with both arms measured.
Stage scores are integers, so the mean of N animals lies on the lattice k/N; the vector data of 7d satisfy that exactly
(validation.tsv), and the 7b raster values are reported raw (the lattice distance is in the extraction output).
It does NOT reanalyse animals: no per-animal value is in the figure. Everything here is a function of means and SEMs.
Run:  python3 -I analyse_fig7.py <fig7d_vector_points.tsv> <b_pdf.tsv> <b_png.tsv> <out_dir>      (--help prints this text)
"""
import csv
import math
import os
import sys

T05 = {10: 2.228, 11: 2.201, 18: 2.101, 22: 2.074, 28: 2.048, 34: 2.032}
NB = {"+/+": (20, 16), "+/-": (18, 12), "-/-": (6, 6)}  # PTZ, PTZ+ETS (legend of Fig 7b)
ND = {"+/+": (12, 8), "+/-": (12, 12), "-/-": (6, 7)}  # PTZ, PTZ+LiCl (legend of Fig 7d)
WINDOWS = [(1, 10), (10, 30), (30, 60), (40, 60), (1, 60)]
HIDDEN_LO, HIDDEN_HI = 0.055, 0.11


def read(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def tcrit(df):
    keys = sorted(T05)
    return T05[max([k for k in keys if k <= df] or [keys[0]])]


def window_row(series_p, series_t, n_p, n_t, lo, hi, floor_zero_bars):
    ts = [t for t in sorted(series_p) if lo <= t <= hi and t in series_t and t >= 1]
    if not ts:
        return None
    P = [series_p[t][0] for t in ts]
    Tm = [series_t[t][0] for t in ts]
    sp = [series_p[t][1] for t in ts]
    st = [series_t[t][1] for t in ts]
    d = [a - b for a, b in zip(P, Tm)]
    D = sum(d) / len(d)
    mp = sum(P) / len(P)
    if floor_zero_bars:
        lo_t = [math.hypot(max(a, HIDDEN_LO), max(b, HIDDEN_LO)) for a, b in zip(sp, st)]
        hi_t = [math.hypot(max(a, HIDDEN_HI), max(b, HIDDEN_HI)) for a, b in zip(sp, st)]
    else:
        lo_t = [math.hypot(a, b) for a, b in zip(sp, st)]
        hi_t = lo_t
    se_ind = math.sqrt(sum(x * x for x in lo_t) / len(lo_t) / len(lo_t))
    se_corr = sum(hi_t) / len(hi_t)
    sd_curve = math.sqrt(sum((x - mp) ** 2 for x in P) / (len(P) - 1)) if len(P) > 1 else float("nan")
    zmin = sum(1 for dd, s in zip(d, lo_t) if s > 0 and abs(dd) > 1.96 * s)
    pos = sum(1 for dd in d if dd > 0)
    df = n_p + n_t - 2
    return dict(minutes=len(ts), mean_P=mp, mean_T=sum(Tm) / len(Tm), D=D, share=D / mp if mp else float("nan"), SD_curve=sd_curve,
                SEM_P=sum(sp) / len(sp), SEM_T=sum(st) / len(st), SE_ind=se_ind, SE_corr=se_corr, t_ind=D / se_ind, t_corr=D / se_corr,
                t_crit=tcrit(df), z_minutes=f"{zmin}/{len(ts)}", positive_minutes=f"{pos}/{len(ts)}")


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 5:
        print(__doc__)
        return 0
    vec, bp, bn, out = sys.argv[1:5]
    os.makedirs(out, exist_ok=True)
    # --- 7d: exact vector values on the half-minute grid
    d7 = {}
    for r in read(vec):
        d7.setdefault((r["genotype"], r["arm"]), {})[round(float(r["minute"]) * 2) / 2] = (float(r["mean_stage"]), float(r["bar_up_stage"]))
    # --- 7b: consensus of the two raster readings
    raw = {}
    for src in (bp, bn):
        for r in read(src):
            if r["mean_stage_raw"] != "":
                raw.setdefault((r["genotype"], r["arm"], float(r["minute"])), []).append((float(r["mean_stage_raw"]), float(r["sem_up_stage"])))
    d7b = {}
    for (g, arm, m), v in raw.items():
        d7b.setdefault((g, arm), {})[m] = (sum(x[0] for x in v) / len(v), sum(x[1] for x in v) / len(v))
    cols = ["figure", "genotype", "window_min", "minutes", "mean_PTZ", "mean_treated", "D_stage", "D_share_of_PTZ", "SD_PTZ_curve", "SEM_PTZ", "SEM_treated",
            "SE_ind", "SE_corr", "t_ind", "t_corr", "t_crit_05", "minutes_z_gt_1.96", "minutes_PTZ_gt_treated"]
    rows = []
    for fig, data, ns, arm_t, floor in (("7b_ethosuximide", d7b, NB, "PTZ+ETS", True), ("7d_lithium", d7, ND, "PTZ+LiCl", False)):
        for g in ("+/+", "+/-", "-/-"):
            for lo, hi in WINDOWS:
                w = window_row(data[(g, "PTZ")], data[(g, arm_t)], ns[g][0], ns[g][1], lo, hi, floor)
                if w:
                    rows.append([fig, g, f"{lo}-{hi}", w["minutes"]] + [f"{w[k]:.3f}" for k in ("mean_P", "mean_T", "D", "share", "SD_curve", "SEM_P", "SEM_T", "SE_ind", "SE_corr", "t_ind", "t_corr")]
                                + [w["t_crit"], w["z_minutes"], w["positive_minutes"]])
    with open(os.path.join(out, "window_statistics.tsv"), "w", encoding="utf-8") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(map(str, r)) + "\n")
    for r in rows:
        print("\t".join(map(str, r)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
