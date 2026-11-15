#!/usr/bin/env python3
"""Animals per arm for NX1 (drug-by-genotype test, same-day control), ethosuximide, from the Fig 7b extraction of PMID 32000863.

Inputs: the two raster tables of Fig 7b written by fig7_quant_ethosuximide_lithium_sci_20261115/extract_fig7_raster.py
(fig7b_raster_pdf.tsv, fig7b_raster_png.tsv). Offline, stdlib only.

What is read from the extraction (DATO): per-minute mean stage and upward SEM per arm, minutes 30 to 60, and the group sizes of the
Fig 7b legend (PTZ v PTZ+ETS: -/- 6 v 6, +/- 18 v 12, +/+ 20 v 16). What is assumed (INFERENZA): the summary is the per-animal window
average of the stage over minutes 30 to 60; between-animal SD of that average lies between two bounds:
  s_ind   minutes independent within animal:      sqrt(mean(sd_min^2) / T)       (lower; implausible for a persistent score)
  s_corr  minutes perfectly correlated in animal:  mean(sd_min)                   (upper; an SD of an average cannot exceed the average of SDs)
with sd_min = SEM_up * sqrt(N). Bars shorter than the marker half height are hidden in the raster: they take 0.055 (lower) and 0.11 (upper).
Size: two-sample, equal n per arm, unequal variances, two-sided alpha 0.05, normal quantiles plus the Guenther small-sample term
n = (za+zb)^2 (v1+v2)/d^2 + za^2/4; a result below 3 per arm is reported as '<3' (the approximation is not valid there).
Run:  python3 -I size_nx1.py <fig7b_raster_pdf.tsv> <fig7b_raster_png.tsv> <out_dir>      (--help prints this text)
"""
import csv
import math
import os
import sys
from statistics import NormalDist

N = {"+/+": (20, 16), "+/-": (18, 12), "-/-": (6, 6)}
LO_FLOOR, HI_FLOOR = 0.055, 0.11
WIN = (30, 60)
Z = NormalDist().inv_cdf


def read(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def series(paths):
    acc = {}
    for p in paths:
        for r in read(p):
            if r["mean_stage_raw"] != "" and r["sem_up_stage"] != "":
                acc.setdefault((r["genotype"], r["arm"], float(r["minute"])), []).append((float(r["mean_stage_raw"]), float(r["sem_up_stage"])))
    out = {}
    for (g, a, m), v in acc.items():
        out.setdefault((g, a), {})[m] = (sum(x[0] for x in v) / len(v), sum(x[1] for x in v) / len(v))
    return out


def arm_stats(s, g, arm, n):
    ms = [m for m in sorted(s[(g, arm)]) if WIN[0] <= m <= WIN[1]]
    mean = sum(s[(g, arm)][m][0] for m in ms) / len(ms)
    sd_lo = [max(s[(g, arm)][m][1], LO_FLOOR) * math.sqrt(n) for m in ms]
    sd_hi = [max(s[(g, arm)][m][1], HI_FLOOR) * math.sqrt(n) for m in ms]
    s_ind = math.sqrt(sum(x * x for x in sd_lo) / len(sd_lo) / len(sd_lo))
    s_corr = sum(sd_hi) / len(sd_hi)
    return dict(minutes=len(ms), mean=mean, s_ind=s_ind, s_corr=s_corr)


def n_per_arm(v1, v2, d, power, alpha=0.05):
    za, zb = Z(1 - alpha / 2), Z(power)
    n = (za + zb) ** 2 * (v1 + v2) / d ** 2 + za ** 2 / 4
    return math.ceil(n)


def fmt(n):
    return "<3" if n < 3 else str(n)


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 4:
        print(__doc__)
        return 0
    s = series(sys.argv[1:3])
    out = sys.argv[3]
    os.makedirs(out, exist_ok=True)
    st = {}
    for g in N:
        st[g] = (arm_stats(s, g, "PTZ", N[g][0]), arm_stats(s, g, "PTZ+ETS", N[g][1]))
    rows = [["genotype", "arm", "N_legend", "minutes", "mean_stage_30_60", "sd_window_low(s_ind)", "sd_window_high(s_corr)"]]
    for g in N:
        for i, arm in enumerate(("PTZ", "PTZ+ETS")):
            a = st[g][i]
            rows.append([g, arm, N[g][i], a["minutes"], f"{a['mean']:.3f}", f"{a['s_ind']:.3f}", f"{a['s_corr']:.3f}"])
    with open(os.path.join(out, "arm_summaries.tsv"), "w", encoding="utf-8") as fh:
        fh.write("\n".join("\t".join(map(str, r)) for r in rows) + "\n")
    # effect scenarios on the window-average stage
    gap_null = st["-/-"][0]["mean"] - st["-/-"][1]["mean"]
    share = gap_null / st["-/-"][0]["mean"]
    scen = []
    for lab, delta, g, why in (
        ("T1 null simple effect, observed gap", gap_null, "-/-", "A or B v C: is there any effect in the nulls"),
        ("T1 null simple effect, half the observed gap", gap_null / 2, "-/-", "same, allowing for an over-read single experiment"),
        ("T2 wt simple effect under B, from +/+ PTZ level", share * st["+/+"][0]["mean"], "+/+", "B v A: proportional effect in wild type, +/+ level"),
        ("T2 wt simple effect under B, from +/- PTZ level", share * st["+/-"][0]["mean"], "+/-", "B v A: proportional effect in wild type, +/- level"),
    ):
        p, t = st[g]
        for power in (0.8, 0.9):
            nlo = n_per_arm(p["s_ind"] ** 2, t["s_ind"] ** 2, delta, power)
            nhi = n_per_arm(p["s_corr"] ** 2, t["s_corr"] ** 2, delta, power)
            scen.append([lab, g, f"{delta:.3f}", power, fmt(nlo), fmt(nhi), f"{nhi / max(nlo, 1):.0f}", why])
    cols = ["test", "genotype", "gap_to_detect_stage", "power", "n_per_arm_if_minutes_independent", "n_per_arm_if_minutes_correlated", "ratio_high_over_low", "meaning"]
    with open(os.path.join(out, "sizing.tsv"), "w", encoding="utf-8") as fh:
        fh.write("\t".join(cols) + "\n" + "\n".join("\t".join(map(str, r)) for r in scen) + "\n")
    print("observed null gap %.3f (%.0f%% of PTZ)" % (gap_null, 100 * share))
    for r in rows:
        print("\t".join(map(str, r)))
    print("\t".join(cols))
    for r in scen:
        print("\t".join(map(str, r)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
