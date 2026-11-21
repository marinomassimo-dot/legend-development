"""ADV-165: apply the pre-registered rules to the per-animal values of Ma et al. 2025 (S1 Data workbook, sheets Fig4C and FigS8).
Stdlib only. Usage: python3 -I cyfip2_chronology.py <workbook.xlsx>  (run from any directory; xlsx_min.py sits next to this file).
Writes nothing; prints the tables. Welch intervals as pre-registered; the rank and exceedance lines are POST-HOC and labelled so.
"""
import itertools
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xlsx_min  # noqa: E402

SHEETS = {"Fig4C": 10, "FigS8": 29}  # sheet file numbers in this workbook (rIdN -> sheetN.xml)
AGES = [1, 7, 14, 28]
LEFT = ["NeuN", "IBA1"]   # first-column panels (left block) in row-group order
RIGHT = ["Olig2", "GFAP"]


def betacf(a, b, x):
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = tiny if abs(d) < tiny else d
    d = 1.0 / d
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c
        c = tiny if abs(c) < tiny else c
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < 1e-14:
            break
    return h


def betai(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return front * betacf(a, b, x) / a
    return 1 - front * betacf(b, a, 1 - x) / b


def t_cdf(t, df):
    x = df / (df + t * t)
    p = 0.5 * betai(df / 2.0, 0.5, x)
    return 1 - p if t > 0 else p


def t_quant(p, df):
    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def mean(v):
    return sum(v) / len(v)


def var(v):
    m = mean(v)
    return sum((x - m) ** 2 for x in v) / (len(v) - 1)


def welch(a, b, level):
    """difference mean(b) - mean(a) with a two-sided Welch interval at `level` (e.g. 0.975 -> 97.5 percent)."""
    se2 = var(a) / len(a) + var(b) / len(b)
    se = math.sqrt(se2)
    df = se2 ** 2 / ((var(a) / len(a)) ** 2 / (len(a) - 1) + (var(b) / len(b)) ** 2 / (len(b) - 1))
    q = t_quant(1 - (1 - level) / 2, df)
    d = mean(b) - mean(a)
    return d, d - q * se, d + q * se, df, se2


def perm_p(a, b):
    """exact two-sided permutation p on the difference of means (POST-HOC robustness)."""
    n = len(a) + len(b)
    allv = a + b
    obs = abs(mean(b) - mean(a))
    cnt = tot = 0
    for idx in itertools.combinations(range(n), len(a)):
        ga = [allv[i] for i in idx]
        gb = [allv[i] for i in range(n) if i not in idx]
        tot += 1
        if abs(mean(gb) - mean(ga)) >= obs - 1e-12:
            cnt += 1
    return cnt / tot


def parse(path, sheet_no):
    rows = xlsx_min.read_rows(path, f"xl/worksheets/sheet{sheet_no}.xml")
    groups, cur = [], []
    for r in rows:
        lab = r[0] if r and isinstance(r[0], str) else ""
        if lab.startswith("Animal"):
            cur.append(r)
        elif cur:
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    out = {}
    for g_i, g in enumerate(groups[:2]):
        for side, name in ((0, LEFT[g_i]), (1, RIGHT[g_i])):
            base = 1 if side == 0 else 11
            data = {}
            for ai, age in enumerate(AGES):
                wt = [r[base + 2 * ai] for r in g if len(r) > base + 2 * ai + 1 and isinstance(r[base + 2 * ai], float)]
                ko = [r[base + 2 * ai + 1] for r in g if len(r) > base + 2 * ai + 1 and isinstance(r[base + 2 * ai + 1], float)]
                data[age] = (wt, ko)
            out[name] = data
    return out


def report(region, data, markers):
    print(f"\n=== {region} (genotype difference R87C minus WT, per age; Welch; 97.5% interval as pre-registered) ===")
    print(f"{'marker':6} {'age':>4} {'nWT':>3} {'nKI':>3} {'meanWT':>7} {'meanKI':>7} {'diff':>7} {'lo97.5':>7} {'hi97.5':>7} {'lo95':>7} {'hi95':>7}  KI>maxWT  perm_p(post-hoc)")
    res = {}
    for m in markers:
        for age in AGES:
            wt, ko = data[m][age]
            d, lo, hi, df, se2 = welch(wt, ko, 0.975)
            _, lo95, hi95, _, _ = welch(wt, ko, 0.95)
            exc = sum(1 for x in ko if x > max(wt))
            pp = perm_p(wt, ko)
            res[(m, age)] = (d, lo, hi, se2, df)
            print(f"{m:6} {age:>4} {len(wt):>3} {len(ko):>3} {mean(wt):7.3f} {mean(ko):7.3f} {d:7.3f} {lo:7.3f} {hi:7.3f} {lo95:7.3f} {hi95:7.3f}  {exc}/{len(ko)}      {pp:.4f}")
    print("\ndifference of differences PWK14 minus PWK7 (descriptive; Welch-Satterthwaite on the four groups; 95% interval)")
    for m in markers:
        d7, _, _, v7, df7 = res[(m, 7)]
        d14, _, _, v14, df14 = res[(m, 14)]
        dd = d14 - d7
        se2 = v7 + v14
        df = se2 ** 2 / (v7 ** 2 / df7 + v14 ** 2 / df14)
        q = t_quant(0.975, df)
        print(f"{m:6} dd={dd:7.3f}  [{dd - q * math.sqrt(se2):7.3f}, {dd + q * math.sqrt(se2):7.3f}]")
    return res


def rules(region, res):
    print(f"\n--- pre-registered rules, {region} ---")
    ol7 = res[("Olig2", 7)]
    gate = ol7[1] > 0
    print(f"rule 1 (Olig2 PWK 7 visible, 97.5% interval excludes zero): {gate}  [diff {ol7[0]:.3f}, {ol7[1]:.3f} to {ol7[2]:.3f}]")
    p_hits, w_ok, w_late = [], True, False
    for m in ("IBA1", "GFAP"):
        d7, lo7, hi7, _, _ = res[(m, 7)]
        d14, lo14, hi14, _, _ = res[(m, 14)]
        p = lo7 > 0 and d14 > 0
        if p:
            p_hits.append(m)
        if not (lo7 <= 0 and hi7 < 0.5 * d14):
            w_ok = False
        if lo14 > 0:
            w_late = True
        print(f"{m}: PWK7 diff {d7:.3f} [{lo7:.3f},{hi7:.3f}]; PWK14 diff {d14:.3f} [{lo14:.3f},{hi14:.3f}]; P-condition {p}; half-PWK14 {0.5*d14:.3f}; W-condition (interval includes 0 and upper < half PWK14) {lo7 <= 0 and hi7 < 0.5 * d14}")
    if p_hits:
        call = f"P-weak (marker {', '.join(p_hits)})"
    elif gate and w_ok and w_late:
        call = "W"
    else:
        call = "U"
    print(f"CALL (primary rules 2 to 4, sensitivity gate included): {call}")
    return call


def fig5d(path):
    """Rule 8 descriptive context: Fig5D qRT-PCR, R87C expression per animal relative to WT (the sheet carries no WT replicates,
    so the interval is one-sample on log ratio against 0; WT variability is NOT in the sheet). Hippocampus block, columns 7 (gene), 9-12 (PWK 1,7,14,28)."""
    rows = xlsx_min.read_rows(path, "xl/worksheets/sheet14.xml")
    genes = {}
    cur = None
    for r in rows:
        if len(r) > 8 and isinstance(r[7], str) and r[7] and r[7] != "Hippocampus":
            cur = r[7]
        if cur and len(r) > 12 and isinstance(r[8], str) and r[8].startswith("Animal"):
            for ai, age in enumerate(AGES):
                v = r[9 + ai]
                if isinstance(v, float) and v > 0:
                    genes.setdefault(cur, {}).setdefault(age, []).append(math.log(v))
    print("\n=== Fig5D hippocampus qRT-PCR, R87C relative to WT (geometric mean ratio; 97.5% one-sample interval on log ratio; n per cell in brackets) ===")
    print(f"{'gene':7}" + "".join(f"{'PWK ' + str(a):>34}" for a in AGES))
    n_up7 = 0
    for g, d in genes.items():
        line = f"{g:7}"
        for age in AGES:
            v = d.get(age, [])
            if len(v) < 3:
                line += f"{'n<3':>34}"
                continue
            m, sd = mean(v), math.sqrt(var(v))
            q = t_quant(0.9875, len(v) - 1)
            lo, hi = m - q * sd / math.sqrt(len(v)), m + q * sd / math.sqrt(len(v))
            if age == 7 and lo > 0:
                n_up7 += 1
            line += f"{math.exp(m):9.2f} [{math.exp(lo):6.2f},{math.exp(hi):6.2f}] ({len(v)})   "
        print(line)
    print(f"genes with a PWK 7 interval excluding 1 (upward): {n_up7} of {len(genes)}")


def fig1b(path):
    rows = xlsx_min.read_rows(path, "xl/worksheets/sheet2.xml")
    print("\n=== Fig1B behavioural seizure events per day, R87C (counts as in the sheet) ===")
    per = {14: [[], [], [], []], 28: [[], [], [], []]}
    started = False
    for r in rows:
        cells = [c for c in r if c is not None]
        if any(isinstance(c, str) and c.startswith("R87C 1") for c in cells):
            started = True
            continue
        if started:
            k = next((i for i, c in enumerate(r) if isinstance(c, str) and c.startswith("Day")), None)
            if k is None:
                continue
            vals = r[k + 1:k + 9]
            if len(vals) == 8 and all(isinstance(x, float) for x in vals):
                for i in range(4):
                    per[14][i].append(vals[i])
                    per[28][i].append(vals[4 + i])
    for age in (14, 28):
        tot = [sum(x) for x in per[age]]
        print(f"PWK {age}: per-mouse 5-day totals {tot}; daily minimum per mouse {[min(x) for x in per[age]]}; all four mice with events on every day: {all(min(x) > 0 for x in per[age])}; mean per mouse-day {sum(tot) / 20:.2f}")


def posthoc(path):
    """POST-HOC sensitivity, not part of the pre-registered rules: (a) age-multiplicity interval for IBA1 and GFAP CA1 (2 markers x 4 ages = 8 tests,
    alpha 0.05/8 -> 99.375% interval); (b) WT spread and KI per-animal values for IBA1 and GFAP at PWK 14 (heterogeneity)."""
    data = parse(path, SHEETS["Fig4C"])
    print("\n=== POST-HOC sensitivity, CA1 (not pre-registered) ===")
    for m in ("IBA1", "GFAP"):
        for age in AGES:
            wt, ko = data[m][age]
            d, lo, hi, _, _ = welch(wt, ko, 0.99375)
            print(f"{m:5} PWK {age:>2}: diff {d:6.3f}  99.375% [{lo:6.3f},{hi:6.3f}]  WT SD {math.sqrt(var(wt)):.3f}  KI SD {math.sqrt(var(ko)):.3f}  excludes 0: {lo > 0}")
    for m in ("IBA1", "GFAP", "NeuN"):
        print(f"{m} PWK 14 R87C per animal (sheet order): {[round(x, 2) for x in data[m][14][1]]}")


if __name__ == "__main__":
    wb = sys.argv[1]
    for region, sheet in (("hippocampal CA1 (Fig4C) PRIMARY", SHEETS["Fig4C"]), ("prelimbic mPFC (FigS8) SECONDARY", SHEETS["FigS8"])):
        data = parse(wb, sheet)
        res = report(region, data, ["NeuN", "Olig2", "IBA1", "GFAP"])
        rules(region, res)
    fig5d(wb)
    fig1b(wb)
    posthoc(wb)
