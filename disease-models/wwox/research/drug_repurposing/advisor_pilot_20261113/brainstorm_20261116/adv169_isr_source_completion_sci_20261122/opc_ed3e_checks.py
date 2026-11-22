"""ADV-169: well-level and repeat-level checks of Extended Data Fig. 3e (Chen et al. 2025, Source Data Extended Data Fig. 3 workbook).
Stdlib only. Usage: python3 -I opc_ed3e_checks.py <Source Data Extended Data Fig. 3 xlsx>. Writes nothing; prints the tables.
Layout of the sheet: O1+ block (columns D WT, E R132H) and MBP+ block (columns I WT, J R132H); 'Repeat n' rows group wells; 'nd' = not determined.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xlsx_min  # noqa: E402


def betacf(a, b, x):
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > 1e-30 else 1e-30)
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > 1e-30 else 1e-30)
        c = 1.0 + aa / c
        c = c if abs(c) > 1e-30 else 1e-30
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > 1e-30 else 1e-30)
        c = 1.0 + aa / c
        c = c if abs(c) > 1e-30 else 1e-30
        de = d * c
        h *= de
        if abs(de - 1.0) < 3e-14:
            break
    return h


def betai(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x)
    if x < (a + 1) / (a + b + 2):
        return math.exp(lbt) * betacf(a, b, x) / a
    return 1 - math.exp(lbt) * betacf(b, a, 1 - x) / b


def t_two_sided_p(t, df):
    return betai(df / 2.0, 0.5, df / (df + t * t))


def mean(v):
    return sum(v) / len(v)


def sd(v):
    m = mean(v)
    return math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))


def welch(a, b):
    ma, mb = mean(a), mean(b)
    va, vb = sd(a) ** 2 / len(a), sd(b) ** 2 / len(b)
    t = (ma - mb) / math.sqrt(va + vb)
    df = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
    return t, df, t_two_sided_p(t, df)


def blocks(rows, wt_col, mu_col):
    out, cur = {}, None
    for r in rows:
        r = list(r) + [None] * 12
        if r[2] == "P-value" or r[7] == "P-value":
            break
        lab = r[1] if wt_col == 3 else r[6]
        if isinstance(lab, str) and lab.startswith("Repeat"):
            cur = lab
            out[cur] = ([], [])
        if cur is None:
            continue
        wt, mu = r[wt_col], r[mu_col]
        if isinstance(wt, float):
            out[cur][0].append(wt)
        if isinstance(mu, float):
            out[cur][1].append(mu)
    return out


def report(name, b):
    print("== %s ==" % name)
    allwt, allmu = [], []
    rm = []
    for k, (wt, mu) in b.items():
        allwt += wt
        allmu += mu
        rm.append((mean(wt), mean(mu)))
        print("  %s: wells WT %d (mean %.3f) R132H %d (mean %.3f); ratio of means %.3f; all R132H wells below every WT well: %s"
              % (k, len(wt), mean(wt), len(mu), mean(mu), mean(mu) / mean(wt), max(mu) < min(wt)))
    t, df, p = welch(allwt, allmu)
    print("  well level (n %d against %d): Welch t %.2f, df %.1f, P %.2e (the workbook prints P %s from the same pooled wells; the Methods say outliers were removed by a ROUT test first)" % (len(allwt), len(allmu), t, df, p, "1.0e-18 (O1+) and 3.5e-17 (MBP+)"))
    ratios = [m / w for w, m in rm]
    print("  repeat level (n = 3 independent experiments): ratios R132H/WT = %s; mean %.3f; max %.3f" % (", ".join("%.3f" % r for r in ratios), mean(ratios), max(ratios)))
    # one-sample t of the three repeat ratios against 1 (WT normalised to about 1 in each repeat)
    m, s = mean(ratios), sd(ratios)
    t1 = (m - 1) / (s / math.sqrt(len(ratios)))
    print("  one-sample t of the three repeat ratios against 1: t %.2f, df 2, P %.4f" % (t1, t_two_sided_p(t1, 2)))
    wtmeans = [w for w, _ in rm]
    print("  WT repeat means: %s (normalisation per repeat or overall is not stated in the sheet)" % ", ".join("%.3f" % x for x in wtmeans))


def main(path):
    rows = xlsx_min.read_rows(path)
    report("O1+", blocks(rows, 3, 4))
    report("MBP+", blocks(rows, 8, 9))


if __name__ == "__main__":
    main(sys.argv[1])
