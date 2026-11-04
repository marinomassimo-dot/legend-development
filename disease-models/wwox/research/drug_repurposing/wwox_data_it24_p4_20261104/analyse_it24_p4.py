"""IT24 P4: per-gene contrasts for GSE215425 (counts; P47T vs WT, 4 regions) and GSE158681/2 (TPM; descriptive). Needs numpy only. Deterministic.
Usage: python3 -I analyse_it24_p4.py <GSE215425_processed_data.csv.gz> <GSE158681 hippo.gz> <GSE158682 cortex.gz> <Ensembl92 cdna.fa.gz> <it5 per_gene_in_sets.tsv> <outdir>
Declared in PRE_DECLARATION.md (written before running)."""
import sys, gzip, re, os, json, math
import numpy as np
P215, HIPPO, CORTEX, FASTA, SETS, OUT = sys.argv[1:7]
os.makedirs(OUT, exist_ok=True)
SEED = 20261104; NDRAW = 10000

# ---------- Student t survival via regularised incomplete beta (no scipy) ----------
def betacf(a, b, x):
    tiny = 1e-300; qab = a + b; qap = a + 1; qam = a - 1
    c = 1.0; d = 1 - qab * x / qap
    d = tiny if abs(d) < tiny else d; d = 1 / d; h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d; d = tiny if abs(d) < tiny else d
        c = 1 + aa / c; c = tiny if abs(c) < tiny else c
        d = 1 / d; h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d; d = tiny if abs(d) < tiny else d
        c = 1 + aa / c; c = tiny if abs(c) < tiny else c
        d = 1 / d; de = d * c; h *= de
        if abs(de - 1) < 3e-14: break
    return h
def ibeta(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    return bt * betacf(a, b, x) / a if x < (a + 1) / (a + b + 2) else 1 - bt * betacf(b, a, 1 - x) / b
def t2p(t, df):  # two-sided
    return ibeta(df / 2, 0.5, df / (df + t * t))
def bh(p):
    p = np.asarray(p); n = len(p); o = np.argsort(p); q = np.empty(n)
    r = p[o] * n / (np.arange(n) + 1); r = np.minimum.accumulate(r[::-1])[::-1]; q[o] = np.minimum(r, 1); return q

# ---------- Part A: GSE215425 ----------
f = gzip.open(P215, "rt"); head = f.readline().rstrip("\n").split("\t")
cols = head[2:]; ens, sym, rows = [], [], []
for l in f:
    p = l.rstrip("\n").split("\t"); ens.append(p[0]); sym.append(p[1]); rows.append(p[2:])
C = np.array(rows, dtype=float); sym = np.array(sym)
meta = []
for c in cols:
    reg, gt, an = c.split("_", 2)[0], c.split("_")[1], c.split("_")[2]
    meta.append((reg, "MUT" if gt.startswith("P47T") else "WT", "M" if an[0] == "M" else "F", an))
REG = ["PFC", "HPC", "CTX", "CB"]
def idx(reg): return [i for i, m in enumerate(meta) if m[0] == reg]
setrows = [l.rstrip("\n").split("\t") for l in open(SETS)][1:]
sets = {}
for r in setrows:
    sets.setdefault(r[0], []).append(r[2])
sets = {k: sorted(set(v)) for k, v in sets.items() if k not in ("ATF4_gene",) or True}
rng = np.random.default_rng(SEED)
summary = {"dataset": "GSE215425", "regions": {}}
allrows = []
ctrl = []
for reg in REG:
    ii = idx(reg); Y = C[:, ii]; gt = np.array([meta[i][1] for i in ii]); sx = np.array([meta[i][2] for i in ii]); names = [meta[i][3] for i in ii]
    lib = Y.sum(0); cpm = Y / lib * 1e6
    keep = (cpm >= 1).sum(1) >= 3
    Yk = Y[keep]; gsym = sym[keep]; gens = np.array(ens)[keep]
    # median-of-ratios size factors
    with np.errstate(divide="ignore"):
        lg = np.log(Yk); fin = np.isfinite(lg).all(1); ref = lg[fin].mean(1)
        sf = np.exp(np.median(lg[fin] - ref[:, None], axis=0))
    Z = np.log2(Yk / sf + 0.5)
    mut = (gt == "MUT").astype(float)
    def fit(Xcols):
        X = np.column_stack([np.ones(len(gt))] + Xcols); XtXi = np.linalg.inv(X.T @ X)
        B = XtXi @ X.T @ Z.T; R = Z.T - X @ B; df = X.shape[0] - X.shape[1]
        s2 = (R ** 2).sum(0) / df; se = np.sqrt(s2 * XtXi[1, 1]); b = B[1]
        t = np.where(se > 0, b / np.where(se > 0, se, 1), 0.0); p = np.array([t2p(x, df) for x in t])
        return b, t, p, df
    male = (sx == "M").astype(float)
    b, t, p, df = fit([mut, male])
    b0, t0, p0, df0 = fit([mut])
    q = bh(p); q0 = bh(p0); med = np.median(b); cb = b - med
    mean_wt = (Yk[:, gt == "WT"] / sf[gt == "WT"]).mean(1); mean_mut = (Yk[:, gt == "MUT"] / sf[gt == "MUT"]).mean(1)
    for k in range(len(gsym)):
        allrows.append((reg, gens[k], gsym[k], f"{mean_wt[k]:.2f}", f"{mean_mut[k]:.2f}", f"{b[k]:.4f}", f"{cb[k]:.4f}", f"{t[k]:.3f}", f"{p[k]:.3g}", f"{q[k]:.3g}", f"{q0[k]:.3g}", int((gt == 'WT').sum()), int(mut.sum())))
    thr = {"T1_FDR<0.10": q < 0.10, "T2_FDR<0.05&|cLFC|>=0.585": (q < 0.05) & (np.abs(cb) >= 0.585), "T3_FDR<0.05&|cLFC|>=1": (q < 0.05) & (np.abs(cb) >= 1)}
    thr_nosex = {"T1_FDR<0.10": q0 < 0.10, "T2_FDR<0.05&|cLFC|>=0.585": (q0 < 0.05) & (np.abs(cb) >= 0.585), "T3_FDR<0.05&|cLFC|>=1": (q0 < 0.05) & (np.abs(cb) >= 1)}
    R = {"n_WT": int((gt == "WT").sum()), "n_MUT": int(mut.sum()), "genes_tested": int(keep.sum()), "median_shift_log2": float(med), "df": int(df),
         "calls": {k: {"up": int((v & (cb > 0)).sum()), "down": int((v & (cb < 0)).sum()), "up_nosex": int((thr_nosex[k] & (cb > 0)).sum()), "down_nosex": int((thr_nosex[k] & (cb < 0)).sum())} for k, v in thr.items()}}
    # controls
    def gene(s):
        w = np.where(gsym == s)[0]
        if len(w) != 1: return None
        return int(w[0])
    cw = {}
    for s in ["Wwox", "Gfap", "Aif1", "Hk2", "Ldha", "Ldhb", "Slc2a1", "Bnip3", "Pdk1", "Atf4", "Chac1", "Trib3", "Sesn2", "Ddit3", "Asns"]:
        k = gene(s)
        cw[s] = None if k is None else {"mean_norm_WT": float(mean_wt[k]), "mean_norm_MUT": float(mean_mut[k]), "cLFC": float(cb[k]), "p": float(p[k]), "FDR": float(q[k])}
    R["genes"] = cw
    # sex check on all libraries incl. non-filtered
    sxg = {}
    for s in ["Xist", "Ddx3y", "Uty"]:
        w = np.where(sym == s)[0]
        if len(w) == 1:
            v = cpm[w[0]]; sxg[s] = {"F_min_max": [float(v[sx == "F"].min()), float(v[sx == "F"].max())], "M_min_max": [float(v[sx == "M"].min()), float(v[sx == "M"].max())]}
    R["sex_check"] = sxg
    R["sex_balance"] = {"WT_M": int(((gt == "WT") & (sx == "M")).sum()), "WT_F": int(((gt == "WT") & (sx == "F")).sum()), "MUT_M": int(((gt == "MUT") & (sx == "M")).sum()), "MUT_F": int(((gt == "MUT") & (sx == "F")).sum())}
    # sets: centred mean cLFC vs decile-matched null
    lm = np.log2(((Yk / sf).mean(1)) + 1); dec = np.digitize(lm, np.quantile(lm, np.linspace(0, 1, 11)[1:-1]))
    sres = {}
    symidx = {s: k for k, s in enumerate(gsym)}
    for sn, mem in sets.items():
        mk = [symidx[m_] for m_ in [x for x in mem] if m_ in symidx]
        # mouse symbol: capitalise human symbol
        mk = sorted(set(symidx[x] for x in [m_.capitalize() if m_.capitalize() in symidx else m_ for m_ in mem] if x in symidx))
        if len(mk) < 3: sres[sn] = {"n_measurable": len(mk), "mean_cLFC": None}; continue
        obs = float(cb[mk].mean()); null = []
        pools = {d: np.where(dec == d)[0] for d in range(10)}
        for _ in range(NDRAW):
            pick = [rng.choice(pools[dec[k]]) for k in mk]
            null.append(cb[pick].mean())
        null = np.array(null)
        sres[sn] = {"n_measurable": len(mk), "mean_cLFC": obs, "null_2.5": float(np.quantile(null, .025)), "null_97.5": float(np.quantile(null, .975)), "outside_null": bool(obs < np.quantile(null, .025) or obs > np.quantile(null, .975))}
    R["sets"] = sres
    # lists
    tab = []
    for k in np.where(thr["T1_FDR<0.10"])[0]:
        tab.append((reg, gens[k], gsym[k], mean_wt[k], mean_mut[k], b[k], cb[k], p[k], q[k], q0[k]))
    summary["regions"][reg] = R
    with open(os.path.join(OUT, f"p47t_{reg}_genes_FDR10.tsv"), "w") as g:
        g.write("region\tensembl_id\tsymbol\tmean_norm_count_WT\tmean_norm_count_P47T\tlog2FC_uncentred\tlog2FC_centred\tp\tFDR_with_sex\tFDR_no_sex\tT2\tT3\tdirection\n")
        for r_ in sorted(tab, key=lambda r: r[8]):
            T2 = (r_[8] < .05) and abs(r_[6]) >= .585; T3 = (r_[8] < .05) and abs(r_[6]) >= 1
            g.write(f"{r_[0]}\t{r_[1]}\t{r_[2]}\t{r_[3]:.2f}\t{r_[4]:.2f}\t{r_[5]:.3f}\t{r_[6]:.3f}\t{r_[7]:.3g}\t{r_[8]:.3g}\t{r_[9]:.3g}\t{int(T2)}\t{int(T3)}\t{'up' if r_[6] > 0 else 'down'}\n")
# full table, gz
with gzip.open(os.path.join(OUT, "p47t_all_regions_tested_genes.tsv.gz"), "wt") as g:
    g.write("region\tensembl_id\tsymbol\tmean_norm_count_WT\tmean_norm_count_P47T\tlog2FC_uncentred\tlog2FC_centred\tt\tp\tFDR_with_sex\tFDR_no_sex\tn_WT\tn_P47T\n")
    for r in allrows: g.write("\t".join(map(str, r)) + "\n")
json.dump(summary, open(os.path.join(OUT, "p47t_summary.json"), "w"), indent=1)

# ---------- Part B: mouse P17 (descriptive) ----------
tx2g, gsym2, patch = {}, {}, set()
for l in gzip.open(FASTA, "rt"):
    if l[0] != ">": continue
    tid = l[1:].split(" ", 1)[0]; gid = re.search(r"gene:(\S+)", l).group(1); s = re.search(r"gene_symbol:(\S+)", l)
    if "_PATCH" in l.split(" ", 3)[2]: patch.add(tid); continue
    tx2g[tid] = gid; gsym2[gid] = s.group(1) if s else ""
def loadtpm(path):
    f = gzip.open(path, "rt"); h = f.readline().rstrip("\n").split("\t"); an = h[3:]; ids, rows = [], []
    for l in f:
        p = l.rstrip("\n").split("\t"); ids.append(p[0]); rows.append(p[3:])
    M = np.array(rows, dtype=float); gl = sorted(set(tx2g[i] for i in ids if i in tx2g)); gi = {g: k for k, g in enumerate(gl)}
    G = np.zeros((len(gl), M.shape[1]))
    for k, i in enumerate(ids):
        if i in tx2g: G[gi[tx2g[i]]] += M[k]
    return an, gl, G
DATA = {"hippo": loadtpm(HIPPO), "cortex": loadtpm(CORTEX)}
CON = [("H_S", "hippo", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"]), ("H_N", "hippo", ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"]),
       ("H_null", "hippo", ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"]), ("C_S", "cortex", ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"])]
BCTL = [("CC_WT_vs_SCtrl", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["WT_1", "WT_2", "WT_3"]), ("CC_WT_vs_NCtrl", "hippo", ["N_Ctrl_1", "N_Ctrl_2"], ["WT_1", "WT_2", "WT_3"]), ("CC_NCtrl_vs_SCtrl", "hippo", ["N_Ctrl_1", "N_Ctrl_2"], ["S_Ctrl_1", "S_Ctrl_2"])]
def contrast(name, reg, a, b_):
    an, gl, G = DATA[reg]; ia = [an.index(x) for x in a]; ib = [an.index(x) for x in b_]
    ma = G[:, ia].mean(1); mb = G[:, ib].mean(1); r = np.log2((ma + .5) / (mb + .5)); c = r - np.median(r[(ma >= 1) | (mb >= 1)])
    sep = (G[:, ia].min(1) > G[:, ib].max(1)) | (G[:, ia].max(1) < G[:, ib].min(1))
    return dict(name=name, gl=gl, ma=ma, mb=mb, c=c, sep=sep, na=len(a), nb=len(b_), ia=ia, ib=ib, G=G)
RES = {n: contrast(n, r, a, b_) for n, r, a, b_ in CON}
CCs = {n: contrast(n, r, a, b_) for n, r, a, b_ in BCTL}
gl = RES["H_S"]["gl"]
def thresholds(c): return [0.585, 1.0, 2.0]
msum = {"dataset": "GSE158681/2", "contrasts": {}, "Wwox": {}}
out = []
for n, R_ in RES.items():
    reg = [x for x in CON if x[0] == n][0][1]
    gls = R_["gl"]; hi = np.maximum(R_["ma"], R_["mb"]) >= 1
    cc_hit = np.zeros(len(gls), bool)
    cc_avail = (reg == "hippo")
    if reg == "hippo":
        for cn, C_ in CCs.items(): cc_hit |= (np.abs(C_["c"]) >= 0.585) & C_["sep"] & (np.maximum(C_["ma"], C_["mb"]) >= 1)
    counts = {}
    for t in [0.585, 1.0, 2.0]:
        hit = hi & R_["sep"] & (np.abs(R_["c"]) >= t)
        counts[str(t)] = {"up": int((hit & (R_["c"] > 0)).sum()), "down": int((hit & (R_["c"] < 0)).sum()), "of_which_BACKGROUND_CONFOUNDED": (int((hit & cc_hit).sum()) if cc_avail else "NA_no_control_vs_control_in_cortex")}
    msum["contrasts"][n] = {"n_KO": R_["na"], "n_ctl": R_["nb"], "genes_mean_TPM_ge1": int(hi.sum()), "calls_by_threshold": counts, "median_shift": float(np.median(np.log2((R_["ma"] + .5) / (R_["mb"] + .5))[hi]))}
    w = [k for k, g in enumerate(gls) if gsym2.get(g) == "Wwox"]
    if len(w) == 1: msum["Wwox"][n] = {"mean_TPM_KO": float(R_["ma"][w[0]]), "mean_TPM_ctl": float(R_["mb"][w[0]])}
    for k in np.where(hi & R_["sep"] & (np.abs(R_["c"]) >= 0.585))[0]:
        out.append((n, gls[k], gsym2.get(gls[k], ""), R_["ma"][k], R_["mb"][k], R_["c"][k], R_["na"], R_["nb"], (int(cc_hit[k]) if cc_avail else "NA")))
with open(os.path.join(OUT, "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), "w") as g:
    g.write("contrast\tensembl_gene\tsymbol\tmean_TPM_KO\tmean_TPM_control\tcentred_log2_ratio\tn_KO\tn_control\tBACKGROUND_CONFOUNDED\ttier_T1_0.585\ttier_T2_1\ttier_T3_2\tdirection\tinference\n")
    for r in sorted(out, key=lambda r: (r[0], -abs(r[5]))):
        a = abs(r[5]); g.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]:.2f}\t{r[4]:.2f}\t{r[5]:.3f}\t{r[6]}\t{r[7]}\t{r[8]}\t1\t{int(a>=1)}\t{int(a>=2)}\t{'up' if r[5]>0 else 'down'}\tdescriptive_only_n{r[6]}v{r[7]}\n")
json.dump(msum, open(os.path.join(OUT, "mouse_p17_summary.json"), "w"), indent=1)
print("done")
