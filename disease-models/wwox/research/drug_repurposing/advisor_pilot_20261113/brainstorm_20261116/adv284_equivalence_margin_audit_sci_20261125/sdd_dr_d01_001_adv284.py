#!/usr/bin/env python3
"""ADV-284: smallest detectable difference for DR-D01-001 (Steinberg 2026, PMID 42397075, Supplementary Fig 7F, SOX2+MYC+ panel).
Formula frozen in PREREG_ADV284 section 2: SDD = (t(.975,df)+t(.80,df)) * sp * sqrt(1/n1+1/n2), df = n1+n2-2.
Inputs are read by eye / pixel from the held figure (File010.pdf page 12, rendered at 500 dpi, y axis calibrated 0..150) and are labelled so.
Run: python3 -I -P -E sdd_dr_d01_001_adv284.py"""
import math
# Student t quantiles (two-sided alpha .05 and power .80), tabulated for the dfs used
T = {13: (2.160, 0.870), 32: (2.037, 0.853)}
# by-eye arm means (percent of cells), Supp Fig 7F SOX2+MYC+ count: WT NT 48, WT DMSO 45, KO-1B 72, KO-1B A51 50 (+-3 reading error)
wt_mean, ko_mean, a51_mean = 46.5, 72.0, 50.0   # WT = mean of the two WT arms
effect = ko_mean - wt_mean                       # disease effect, knockout minus wild type
print(f"disease effect (KO - WT) = {effect:.1f} percentage points; A51 minus WT = {a51_mean - wt_mean:+.1f}")
cases = {
 "organoid unit, n = 8 WT (4 NT + 4 DMSO) v 7 A51 (legend n)": (8, 7, 13),
 "plotted-point unit, about 19 WT points (6 + 13) v 15 A51 points": (19, 15, 32),
}
print("sp (pooled SD, percentage points, read by eye from the plotted spread: 8-20)  SDD  SDD/effect  at-least-half-effect")
for name, (n1, n2, df) in cases.items():
    t1, t2 = T[df]
    print(name)
    for sp in (8, 10, 12, 15, 18, 20):
        sdd = (t1 + t2) * sp * math.sqrt(1 / n1 + 1 / n2)
        print(f"  sp {sp:>2}  SDD {sdd:5.1f}  ratio {sdd / effect:4.2f}  {'YES' if sdd >= effect / 2 else 'no'}")
