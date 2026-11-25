#!/usr/bin/env python3
"""ADV-288: n per arm and smallest detectable difference for a two-sample t test on a log scale.
Exact power from the noncentral t (numerical integration over the chi variable; no scipy).
Inputs are the frozen PREREG ones (CV used as SD on the log scale). Output: adv288_power_output.tsv
Run: python3 -P -E adv288_power.py"""
import math
from math import erf, exp, lgamma, log, sqrt

def Phi(x): return 0.5 * (1 + erf(x / sqrt(2)))

def chi_pdf_over_nu(s, nu):
    """density of s = sqrt(chi2_nu / nu)"""
    return 2 * (nu / 2) ** (nu / 2) / exp(lgamma(nu / 2)) * s ** (nu - 1) * exp(-nu * s * s / 2)

def tail_two_sided(tc, delta, nu, steps=2000):
    """P(|T| > tc) for T noncentral t(nu, delta): integrate over s."""
    lo, hi = 1e-6, 1 + 12 / sqrt(nu) + 1.0
    h = (hi - lo) / steps
    tot = 0.0
    for i in range(steps + 1):
        s = lo + i * h
        w = 1 if i in (0, steps) else (4 if i % 2 else 2)
        # |Z + delta| > tc * s
        p = (1 - Phi(tc * s - delta)) + Phi(-tc * s - delta)
        tot += w * p * chi_pdf_over_nu(s, nu)
    return tot * h / 3

def tcrit(alpha, nu):
    lo, hi = 0.5, 20.0
    for _ in range(50):
        mid = (lo + hi) / 2
        if tail_two_sided(mid, 0.0, nu, 800) > alpha: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def power(n, d_log, sd_log, alpha, cells=2):
    """cells=2: two-group contrast, var 2 s^2/n, df 2n-2. cells=4: four-cell contrast, var 4 s^2/n, df 4n-4."""
    nu = 2 * n - 2 if cells == 2 else 4 * n - 4
    se = sd_log * sqrt(cells / n)
    return tail_two_sided(tcrit(alpha, nu), abs(d_log) / se, nu)

def n_needed(d_log, sd_log, alpha, cells=2, target=0.80):
    for n in range(3, 400):
        if power(n, d_log, sd_log, alpha, cells) >= target: return n
    return None

def sdd(n, sd_log, alpha, cells=2):
    lo, hi = 0.0, 3.0
    for _ in range(30):
        mid = (lo + hi) / 2
        if power(n, mid, sd_log, alpha, cells) >= 0.8: hi = mid
        else: lo = mid
    return hi

A_UN, A_ADJ = 0.05, 0.05 / 3
rows = [("kind", "contrast", "CV_as_SD_log", "alpha_label", "delta_log", "delta_ratio", "n_per_arm_or_cell", "extra")]
CVS = (0.12, 0.16, 0.21, 0.30)
contrasts = [
    ("WT drug-only slowing (clemastine-sized, Palma I4 ratio 0.84)", log(0.84), 2),
    ("KO restoration by half the genotype gap (ratio 1.14 vs KO vehicle)", log(1.14), 2),
    ("genotype gap, Repudi I3 latency ratio 1.28 (graph read)", log(1.28), 2),
    ("genotype gap, Cheng I1 latency ratio 1.76 (2.44/1.39)", log(2.44 / 1.39), 2),
    ("interaction (KO restoration 1.14 minus WT slowing 0.84, log scale 0.305)", log(1.14) - log(0.84), 4),
]
for name, d, cells in contrasts:
    for cv in CVS:
        for lab, a in (("unadjusted two-sided 0.05", A_UN), ("adjusted for three contrasts, alpha 0.0167", A_ADJ)):
            n = n_needed(d, cv, a, cells)
            rows.append(("n_for_80pct_power", name, cv, lab, round(d, 4), round(exp(d), 3), n, "four-cell contrast" if cells == 4 else "two-group"))
for n in (4, 8, 12, 16, 24):
    for cv in CVS:
        for lab, a in (("unadjusted two-sided 0.05", A_UN), ("adjusted for three contrasts, alpha 0.0167", A_ADJ)):
            s2 = sdd(n, cv, a, 2); s4 = sdd(n, cv, a, 4)
            rows.append(("SDD_80pct_power", "two-group difference, ratio scale", cv, lab, round(s2, 4), round(exp(s2), 3), n, f"downward ratio {round(exp(-s2),3)}"))
            rows.append(("SDD_80pct_power", "interaction (four-cell)", cv, lab, round(s4, 4), round(exp(s4), 3), n, ""))
# check of the held Cheng contrast at its own spread and n
sd_log = 0.30
p = power(4, log(2.44 / 1.39), sd_log, A_UN, 2)
rows.append(("power_check", "Cheng I1 latency -/- (n 4) vs +/+ (n 10): equal-n approximation at n=4 per arm, CV 0.30", 0.30, "unadjusted", round(log(2.44/1.39), 4), round(2.44/1.39, 3), 4, f"power {p:.3f}"))
# litter arithmetic (global KO only; 0.25 Mendelian, about 1.75 KO per litter, pup brief v2 section 3)
for n in (8, 12, 16, 24):
    rows.append(("litters_global_KO", "two KO arms (vehicle, drug) of n animals; WT arms share the same litters (0.25 each)", "", "", "", "", n, f"KO animals {2*n}; litters at 1.75 KO per litter {math.ceil(2*n/1.75)}"))
with open("adv288_power_output.tsv", "w") as f:
    for r in rows: f.write("\t".join(str(x) for x in r) + "\n")
for r in rows[:1]: print(r)
print(len(rows), "rows")
