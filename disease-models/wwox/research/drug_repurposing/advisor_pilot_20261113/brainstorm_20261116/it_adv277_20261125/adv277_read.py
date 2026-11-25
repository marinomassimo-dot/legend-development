#!/usr/bin/env python3
"""ADV-277 held-table lookup: H1-0 sentinel first, then WWOX, per contrast.

argv[1] = directory holding the downloaded tables (see data_digests.tsv); argv[2] = directory with xlsx.py.
Standard library only. Welch two-sided t test on log2 values; 95 % interval of the mean log2 difference.
"""
import csv, math, sys, statistics as st

csv.field_size_limit(10 ** 9)
D = sys.argv[1]
sys.path.insert(0, sys.argv[2])
from adv277_xlsx import sheets  # noqa: E402


def betacf(a, b, x):
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        for aa in (m * (b - m) * x / ((qam + m2) * (a + m2)),
                   -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))):
            d = 1.0 + aa * d
            d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
            c = 1.0 + aa / (c if abs(c) > 1e-300 else 1e-300)
            h *= d * c
        if abs(d * c - 1) < 1e-12:
            break
    return h


def ibeta(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    f = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return f * betacf(a, b, x) / a
    return 1 - f * betacf(b, a, 1 - x) / b


def tp(t, df):
    return ibeta(df / 2, 0.5, df / (df + t * t))


def tcrit(df):
    lo, hi = 0.0, 1000.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if tp(mid, df) > 0.05 else (lo, mid)
    return lo


def contrast(ctrl, trt):
    """ctrl, trt: linear values; None or 0 = not quantified."""
    c = [v for v in ctrl if v]
    t = [v for v in trt if v]
    if len(c) < 2 or len(t) < 2:
        return "not quantified in 2 units of each arm (n %d/%d)" % (len(c), len(t))
    ratio = (sum(t) / len(t)) / (sum(c) / len(c))
    lc, lt = [math.log2(v) for v in c], [math.log2(v) for v in t]
    if len(c) < 3 or len(t) < 3:
        return "n %d/%d ratio %.2f (descriptive)" % (len(c), len(t), ratio)
    vc, vt = st.variance(lc) / len(lc), st.variance(lt) / len(lt)
    diff = st.mean(lt) - st.mean(lc)
    se = math.sqrt(vc + vt)
    df = (vc + vt) ** 2 / (vc ** 2 / (len(lc) - 1) + vt ** 2 / (len(lt) - 1))
    p = tp(abs(diff / se), df)
    h = tcrit(df) * se
    call = "up" if (p < 0.05 and ratio >= 1.25) else "down" if (p < 0.05 and ratio <= 0.80) else "not distinguished"
    return "n %d/%d ratio %.2f [95%% %.2f to %.2f] p %.4g %s" % (len(c), len(t), ratio, 2 ** (diff - h), 2 ** (diff + h), p, call)


def num(x):
    try:
        v = float(x)
        return v if v == v else None
    except (TypeError, ValueError):
        return None


def report(name, genes, getter, arms):
    """arms: list of (label, ctrl_keys, trt_keys). genes: sentinel first."""
    for label, ck, tk in arms:
        for g in genes:
            row = getter(g)
            if row is None:
                print(name, "|", label, "|", g, "| not in table")
                continue
            cv, tv = [row.get(k) for k in ck], [row.get(k) for k in tk]
            fmt = lambda xs: ",".join("NA" if not v else "%.4g" % v for v in xs)
            print(name, "|", label, "|", g, "|", contrast(cv, tv), "| ctrl", fmt(cv), "| trt", fmt(tv))


# 1. Human dorsal forebrain organoids, MassIVE MSV000097991 (PXD064286), DIA-NN protein groups
rows = list(csv.reader(open(D + "/msv97991/report.pg_matrix.tsv"), delimiter="\t"))
hdr = rows[0]
key = {}
for i, h in enumerate(hdr[5:], 5):
    s = h.split("\\")[-1]
    parts = s.split("_O_")[1].split("_")  # KOLF2_D20_Ctrl-1_QKL...
    key[(parts[0], parts[1], parts[2].rsplit("-", 1)[0], parts[2].rsplit("-", 1)[1])] = i


def org(g):
    acc = {"H1-0": "P07305", "WWOX": "Q9NZC7", "CDKN1A": "P38936"}[g]
    hit = [r for r in rows[1:] if acc in r[0].split(";")]
    if not hit:
        return None
    assert len(hit) == 1, (g, [r[0] for r in hit])
    r = hit[0]
    print("# organoid row", g, "Protein.Group", r[0], "Genes", r[3])
    return {k: num(r[i]) for k, i in key.items()}


cache = {g: org(g) for g in ("H1-0", "WWOX")}
arms = []
for line in ("BIONi", "HMGU1", "KOLF2"):
    for day in ("D35", "D50"):
        arms.append(("%s %s" % (line, day), [(line, day, "Ctrl", str(i)) for i in (1, 2, 3)],
                     [(line, day, "1mMVPA", str(i)) for i in (1, 2, 3)]))
report("organoid-proteome", ["H1-0", "WWOX"], cache.get, arms)
# lines as units: mean of each line's replicates, three lines
for day in ("D35", "D50"):
    for g in ("H1-0", "WWOX"):
        r = cache[g]
        if r is None:
            print("organoid-proteome | lines as units", day, "|", g, "| not in table")
            continue
        per = []
        for line in ("BIONi", "HMGU1", "KOLF2"):
            c = [r[(line, day, "Ctrl", str(i))] for i in (1, 2, 3) if r[(line, day, "Ctrl", str(i))]]
            t = [r[(line, day, "1mMVPA", str(i))] for i in (1, 2, 3) if r[(line, day, "1mMVPA", str(i))]]
            if c and t:
                per.append(math.log2(st.mean(t) / st.mean(c)))
        m, se = st.mean(per), st.stdev(per) / math.sqrt(len(per))
        p = tp(abs(m / se), len(per) - 1)
        h = tcrit(len(per) - 1) * se
        print("organoid-proteome | lines as units", day, "|", g, "| %d lines, ratios %s, geometric mean %.2f [95%% %.2f to %.2f] one-sample p %.4g" %
              (len(per), ",".join("%.2f" % 2 ** v for v in per), 2 ** m, 2 ** (m - h), 2 ** (m + h), p))

# 2. Prenatal VPA mouse prefrontal cortex, PXD036413, authors' quantile-normalised log2 sheet
for name, sheet in sheets(D + "/pride/VPA_PFC_Protein_data.xlsx"):
    if name != "Quantile normalized":
        continue
    h = sheet[0]

    def pfc(g):
        acc = {"H1-0": "P10922", "WWOX": "Q91WL8"}[g]
        hit = [r for r in sheet[1:] if len(r) > 1 and acc in str(r[1])]
        if not hit:
            return None
        return {h[i]: (2 ** num(hit[0][i]) if num(hit[0][i]) is not None else None) for i in range(3, 11)}

    report("prenatal-VPA PFC", ["H1-0", "WWOX"], pfc, [("offspring", ["WT %d" % i for i in range(1, 5)], ["VPA %d" % i for i in range(1, 5)])])

# 3. Prenatal VPA mouse striatum, PXD067574, TMT normalised abundances
s = list(csv.reader(open(D + "/pride/20240820_BRAIN_TMT6_F_Proteins.txt"), delimiter="\t"))
sh = s[0]
cols = [i for i, x in enumerate(sh) if x.startswith("Abundances (Normalized):")]
sal = [sh[i] for i in cols if ", S_" in sh[i]]
vpa = [sh[i] for i in cols if ", V_" in sh[i]]


def stri(g):
    acc = {"H1-0": "P10922", "WWOX": "Q91WL8"}[g]
    ai = sh.index("Accession")
    hit = [r for r in s[1:] if len(r) == len(sh) and r[ai] == acc]
    if not hit:
        return None
    return {sh[i]: num(hit[0][i]) for i in cols}


report("prenatal-VPA striatum", ["H1-0", "WWOX"], stri, [("offspring", sal, vpa)])
