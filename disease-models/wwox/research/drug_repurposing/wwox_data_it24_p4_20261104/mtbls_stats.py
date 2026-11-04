"""IT24 P4 addendum C/D statistics on own-EIC sample areas of MTBLS12344 (gate-passing features only). Needs numpy only.
Usage: python3 -I mtbls_stats.py <mtbls_sample_areas.tsv> <out.tsv>"""
import sys, csv, math, numpy as np
inp, out = sys.argv[1:3]
def betacf(a, b, x):
    tiny = 1e-300; qab = a + b; qap = a + 1; qam = a - 1; c = 1.0; d = 1 - qab * x / qap
    d = tiny if abs(d) < tiny else d; d = 1 / d; h = d
    for m in range(1, 300):
        m2 = 2 * m; aa = m * (b - m) * x / ((qam + m2) * (a + m2)); d = 1 + aa * d; d = tiny if abs(d) < tiny else d
        c = 1 + aa / c; c = tiny if abs(c) < tiny else c; d = 1 / d; h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2)); d = 1 + aa * d; d = tiny if abs(d) < tiny else d
        c = 1 + aa / c; c = tiny if abs(c) < tiny else c; d = 1 / d; de = d * c; h *= de
        if abs(de - 1) < 3e-14: break
    return h
def ibeta(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    return bt * betacf(a, b, x) / a if x < (a + 1) / (a + b + 2) else 1 - bt * betacf(b, a, 1 - x) / b
def t2p(t, df): return ibeta(df / 2, 0.5, df / (df + t * t))
def tq975(df):  # bisection on two-sided p = 0.05
    lo, hi = 0.0, 50.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if t2p(mid, df) > 0.05: lo = mid
        else: hi = mid
    return (lo + hi) / 2

R = list(csv.DictReader(open(inp), delimiter="\t"))
feats = [c[:-len("_area")] for c in R[0] if c.endswith("_area") and not c.endswith("_over_TIC_area")]
feats = [c for c in feats if not c.endswith("_area_over_TIC")]
CON = [("C1_KD_LacZ", "Wwox RNAi", "RNAi Control", "LacZ"), ("C2_KD_AB42", "Wwox RNAi", "RNAi Control", "AB42")]
rows = []
for norm in ("area", "area_over_TIC"):
    for cn, A, B, am in CON:
        res = []
        for f in feats:
            col = f + "_" + norm
            va = np.array([float(r[col]) for r in R if r["group"] == A and r["amyloid"] == am]); vb = np.array([float(r[col]) for r in R if r["group"] == B and r["amyloid"] == am])
            la, lb = np.log2(va), np.log2(vb); d = la.mean() - lb.mean(); v1, v2 = la.var(ddof=1) / len(la), lb.var(ddof=1) / len(lb)
            se = math.sqrt(v1 + v2); df = (v1 + v2) ** 2 / (v1 ** 2 / (len(la) - 1) + v2 ** 2 / (len(lb) - 1)); t = d / se; p = t2p(t, df); ci = tq975(df) * se
            res.append([f, d, d - ci, d + ci, t, df, p, len(la), len(lb)])
        ps = np.array([x[6] for x in res]); o = np.argsort(ps); n = len(ps); adj = np.empty(n); rr = ps[o] * n / (np.arange(n) + 1); rr = np.minimum.accumulate(rr[::-1])[::-1]; adj[o] = np.minimum(rr, 1)
        for x, q in zip(res, adj): rows.append((norm, cn, *x, q))
with open(out, "w") as fo:
    fo.write("normalisation\tcontrast\tmetabolite\tlog2FC_KD_minus_ctl\tCI95_low\tCI95_high\tWelch_t\tdf\tp\tn_KD\tn_ctl\tBH_FDR_over_gate_passing_features\tTier_FDR<0.10\tTier_FDR<0.05&|l2fc|>=0.2\tTier_FDR<0.05&|l2fc|>=0.585\n")
    for x in rows:
        fo.write(f"{x[0]}\t{x[1]}\t{x[2]}\t{x[3]:.3f}\t{x[4]:.3f}\t{x[5]:.3f}\t{x[6]:.2f}\t{x[7]:.1f}\t{x[8]:.3g}\t{x[9]}\t{x[10]}\t{x[11]:.3g}\t{int(x[11]<.10)}\t{int(x[11]<.05 and abs(x[3])>=.2)}\t{int(x[11]<.05 and abs(x[3])>=.585)}\n")
print("done")
