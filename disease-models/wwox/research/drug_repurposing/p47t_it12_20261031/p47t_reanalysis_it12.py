#!/usr/bin/env python3
"""IT12 P2-P47T: limited reanalysis of GSE215425 (Wwox P47T knock-in mouse brain, bulk RNA-seq) for the HIF target set and the NRF2 set.

Usage:
  p47t_reanalysis_it12.py --help                       this text; no work is done
  p47t_reanalysis_it12.py run --counts GSE215425_processed_data.csv.gz --hallmark mh.gmt --authors-deg Supplementary_data_all_sheets_derived.txt --out DIR

Stdlib + numpy only. Deterministic (seed 20261031). Units are animals. Gene sets and decision rules are those of PRE_ANALYSIS.md.
Hallmark GSEA here is a re-implementation (pre-ranked by Welch t, weight 1, gene-label permutation), not the authors' clusterProfiler run.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help") or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, itertools, math, os, collections
import numpy as np

SEED = 20261031
def arg(n, d=None):
    a = sys.argv
    return a[a.index(n) + 1] if n in a else d
OUT = arg("--out"); os.makedirs(OUT, exist_ok=True)

SETS = {
 "HIF_SEL_UP6": ["Adm", "Bhlhe40", "P4ha1", "Ankrd37", "Ddit4", "Egln3"],
 "HIF_FLAT6": ["Pgk1", "Aldoa", "Eno1", "Pkm", "Pfkp", "Ndrg1"],
 "NRF2_5": ["Nqo1", "Hmox1", "Gclm", "Srxn1", "Txnrd1"],
 "ACTIVITY_IEG": ["Fos", "Fosb", "Junb", "Jun", "Egr1", "Egr2", "Egr4", "Arc", "Npas4", "Nr4a1", "Nptx2", "Bdnf", "Dusp1"],
 "ASTRO": ["Gfap", "Aqp4", "Aldh1l1", "Slc1a3", "Slc1a2", "Gja1", "Sox9", "Vim", "Cd44", "Serpina3n", "Lcn2"],
 "MICRO": ["Aif1", "Cx3cr1", "Tmem119", "P2ry12", "Csf1r", "Hexb", "Cd68", "Trem2"],
 "OLIGO": ["Mbp", "Plp1", "Mog", "Mobp", "Mag"],
 "NEURON": ["Snap25", "Syt1", "Rbfox3", "Slc17a7", "Gad1", "Gad2", "Stmn2", "Camk2a"],
}
SINGLE_OTHER = ["Vegfa"]
IT7_OBS6 = ["Slc2a1", "Hk2", "Ldha", "Ldhb", "Bnip3", "Pdk1"]
REGULATORS = ["Wwox", "Hif1a", "Epas1", "Hif3a", "Arnt", "Egln1", "Egln2", "Egln3", "Vhl", "Nfe2l2", "Keap1"]
CANON_HIF = set("Adm Aldoa Ankrd37 Bhlhe40 Bnip3 Bnip3l Car9 Ddit4 Egln3 Ero1l Eno1 Hilpda Hk2 Ldha Ndrg1 P4ha1 P4ha2 Pdk1 Pfkl Pfkp Pgk1 Pkm Plod2 Slc2a1 Vegfa Lox Pgm1 Tpi1 Gapdh".split())
IEG_STRESS = set("Fos Fosb Jun Junb Atf3 Ier2 Ier3 Egr1 Klf6 Btg1 Btg2 Ppp1r15a Cdkn1a Dusp1 Nr4a1 Zfp36 Sik1 Ddit3".split())
GLIA_REACT = set("Gfap Vim Cd44 Timp1 Serpine1 Serpina3n Lcn2 S100a10 S100a6 Lgals3 Mt1 Mt2 Cp Ccn1 Ccn2 Tgfbi Tnfrsf12a".split())
def klass(g):
    return "CANON_HIF" if g in CANON_HIF else "IEG_STRESS" if g in IEG_STRESS else "GLIA_REACTIVE" if g in GLIA_REACT else "OTHER"

# ---------- statistics helpers ----------
def betacf(a, b, x):
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    d = 1 / (d if abs(d) > 1e-300 else 1e-300); h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d; d = 1 / (d if abs(d) > 1e-300 else 1e-300)
        c = 1 + aa / c; c = c if abs(c) > 1e-300 else 1e-300
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d; d = 1 / (d if abs(d) > 1e-300 else 1e-300)
        c = 1 + aa / c; c = c if abs(c) > 1e-300 else 1e-300
        de = d * c; h *= de
        if abs(de - 1) < 3e-12: break
    return h
def ibeta(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
    return bt * betacf(a, b, x) / a if x < (a + 1) / (a + b + 2) else 1 - bt * betacf(b, a, 1 - x) / b
def t_two_sided_p(t, df):
    if not np.isfinite(t) or df <= 0: return float("nan")
    return ibeta(df / 2.0, 0.5, df / (df + t * t))
def welch(x, y):
    nx, ny = len(x), len(y)
    mx, my = x.mean(), y.mean()
    vx, vy = x.var(ddof=1), y.var(ddof=1)
    se2 = vx / nx + vy / ny
    if se2 <= 0: return my - mx, float("nan"), float("nan")
    t = (my - mx) / math.sqrt(se2)
    df = se2 ** 2 / ((vx / nx) ** 2 / (nx - 1) + (vy / ny) ** 2 / (ny - 1))
    return my - mx, t, df
def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = np.empty(n)
    prev = 1.0
    for rank in range(n, 0, -1):
        i = o[rank - 1]; prev = min(prev, p[i] * n / rank); q[i] = prev
    return q
def exact_perm_p(vals, n_mut, mut_idx):
    """two-sided exact permutation p on difference of means, all splits"""
    n = len(vals); idx = np.arange(n)
    obs = vals[mut_idx].mean() - np.delete(vals, mut_idx).mean()
    cnt = tot = 0
    for comb in itertools.combinations(range(n), n_mut):
        m = np.zeros(n, bool); m[list(comb)] = True
        d = vals[m].mean() - vals[~m].mean(); tot += 1
        if abs(d) >= abs(obs) - 1e-12: cnt += 1
    return cnt / tot, tot
def spearman(a, b):
    def rk(v):
        o = np.argsort(v, kind="mergesort"); r = np.empty(len(v)); r[o] = np.arange(len(v))
        for u in np.unique(v):
            m = v == u
            if m.sum() > 1: r[m] = r[m].mean()
        return r
    ra, rb = rk(np.asarray(a, float)), rk(np.asarray(b, float))
    if ra.std() == 0 or rb.std() == 0: return float("nan")
    return float(np.corrcoef(ra, rb)[0, 1])
def tmm_factors(counts):
    """edgeR-style TMM, reference = library whose 75th-percentile-scaled count is closest to the mean of those"""
    lib = counts.sum(0).astype(float)
    q75 = np.array([np.percentile(counts[:, j][counts[:, j] > 0] / lib[j], 75) for j in range(counts.shape[1])])
    ref = int(np.argmin(np.abs(q75 - q75.mean())))
    f = np.ones(counts.shape[1])
    for j in range(counts.shape[1]):
        if j == ref: continue
        a, b = counts[:, j].astype(float), counts[:, ref].astype(float)
        ok = (a > 0) & (b > 0)
        a, b = a[ok], b[ok]
        la, lb = lib[j], lib[ref]
        M = np.log2((a / la) / (b / lb)); A = 0.5 * np.log2((a / la) * (b / lb))
        w = (la - a) / (la * a) + (lb - b) / (lb * b); w = 1 / w
        keepM = (M >= np.quantile(M, 0.30)) & (M <= np.quantile(M, 0.70))
        keepA = (A >= np.quantile(A, 0.05)) & (A <= np.quantile(A, 0.95))
        k = keepM & keepA
        f[j] = 2 ** (np.sum(w[k] * M[k]) / np.sum(w[k]))
    f = f / np.exp(np.mean(np.log(f)))
    return f, ref
def logcpm(counts, lib_eff, prior=2.0):
    avg = lib_eff.mean()
    pc = prior * lib_eff / avg
    return np.log2((counts + pc) / (lib_eff + 2 * pc) * 1e6)
def ols_geno_t(y, g, sex):
    """y ~ 1 + genotype + sex ; returns coef, t, df, p for genotype"""
    X = np.column_stack([np.ones(len(y)), g, sex]); n, k = X.shape
    beta, *_ = np.linalg.lstsq(X, y, rcond=None); res = y - X @ beta
    s2 = res @ res / (n - k); cov = s2 * np.linalg.inv(X.T @ X)
    se = math.sqrt(cov[1, 1]); t = beta[1] / se if se > 0 else float("nan")
    return beta[1], t, n - k, t_two_sided_p(t, n - k)

# ---------- load ----------
op = gzip.open if arg("--counts").endswith(".gz") else open
with op(arg("--counts"), "rt") as fh:
    rd = csv.reader(fh, delimiter="\t"); head = next(rd); rows = list(rd)
cols = head[2:]
meta = []
for c in cols:
    reg, geno, animal = c.split("_", 2)
    meta.append((reg, geno, animal, animal[0]))
ens = [r[0] for r in rows]; sym = [r[1] for r in rows]
C = np.array([[float(v) for v in r[2:]] for r in rows])
# symbol -> row (duplicates: keep the row with the highest total count; record the others)
by_sym = collections.defaultdict(list)
for i, s in enumerate(sym): by_sym[s].append(i)
dups = {s: v for s, v in by_sym.items() if len(v) > 1}
def row_of(s):
    if s not in by_sym: return None
    v = by_sym[s]; return v[int(np.argmax([C[i].sum() for i in v]))]

REGIONS = ["HPC", "CTX", "PFC", "CB"]
log = open(os.path.join(OUT, "run_log.txt"), "w")
def L(*a):
    s = " ".join(str(x) for x in a); print(s); log.write(s + "\n")
L("genes", len(sym), "libraries", len(cols), "duplicate symbols", len(dups))
L("library sizes (M):", {r: [float(round(C[:, j].sum() / 1e6, 1)) for j, m in enumerate(meta) if m[0] == r] for r in REGIONS})

# ---------- per region ----------
named_all = {g for s in SETS.values() for g in s} | set(SINGLE_OTHER) | set(IT7_OBS6) | set(REGULATORS)
gene_rows, set_rows, set_animal_rows, corr_rows, mut_rows, gsea_rows, le_rows, val_rows = [], [], [], [], [], [], [], []
hallmark = {}
for line in open(arg("--hallmark")):
    p = line.rstrip("\n").split("\t"); hallmark[p[0]] = [g for g in p[2:] if g]
_it7 = set(IT7_OBS6)
_glia_ieg = GLIA_REACT | IEG_STRESS | set(SETS["ASTRO"]) | set(SETS["ACTIVITY_IEG"])
for _h in ("HALLMARK_HYPOXIA", "HALLMARK_GLYCOLYSIS"):
    hallmark[_h + "_minus_IT7six"] = [g for g in hallmark[_h] if g not in _it7]
    hallmark[_h + "_minus_IT7six_glia_ieg"] = [g for g in hallmark[_h] if g not in _it7 and g not in _glia_ieg]
region_data = {}
for reg in REGIONS:
    idx = [j for j, m in enumerate(meta) if m[0] == reg]
    geno = np.array([1 if meta[j][1] == "Wwox P47T/P47T" or meta[j][1] == "P47T/P47T" else 0 for j in idx])
    sex = np.array([1 if meta[j][3] == "F" else 0 for j in idx])
    animals = [meta[j][2] for j in idx]
    cnt = C[:, idx]
    f, ref = tmm_factors(cnt[cnt.sum(1) > 0])
    lib_eff = cnt.sum(0) * f
    lc = logcpm(cnt, lib_eff)
    cpm = cnt / lib_eff * 1e6
    nmin = min(int(geno.sum()), int((1 - geno).sum()))
    keep = (cpm >= 1).sum(1) >= nmin
    mut = np.where(geno == 1)[0]
    L(reg, "n WT", int((1 - geno).sum()), "n P47T", int(geno.sum()), "TMM factors", np.round(f, 3).tolist(), "genes kept", int(keep.sum()), "reference lib", animals[ref])
    # transcriptome-wide Welch t (for BH context, GSEA ranking, authors' validation)
    t_all = np.full(len(sym), np.nan); lfc_all = np.full(len(sym), np.nan); p_all = np.full(len(sym), np.nan)
    for i in np.where(keep)[0]:
        d, t, df = welch(lc[i, geno == 0], lc[i, geno == 1])
        lfc_all[i] = d; t_all[i] = t; p_all[i] = t_two_sided_p(t, df)
    q_all = np.full(len(sym), np.nan); q_all[keep] = bh(p_all[keep])
    region_data[reg] = dict(idx=idx, geno=geno, sex=sex, animals=animals, lc=lc, keep=keep, t=t_all, lfc=lfc_all, p=p_all, q=q_all, cpm=cpm, cnt=cnt)
    # named genes
    for g in sorted(named_all):
        i = row_of(g)
        if i is None:
            gene_rows.append([reg, g, "NOT_IN_TABLE"] + [""] * 12); continue
        y = lc[i]
        d, t, df = welch(y[geno == 0], y[geno == 1]); pw = t_two_sided_p(t, df)
        pp, ntot = exact_perm_p(y, int(geno.sum()), mut)
        cs, ts, dfs, ps = ols_geno_t(y, geno, sex)
        grp = [k for k, v in SETS.items() if g in v] + (["HIF_OTHER_1"] if g in SINGLE_OTHER else []) + (["IT7_OBS6"] if g in IT7_OBS6 else []) + (["REGULATOR"] if g in REGULATORS else [])
        gene_rows.append([reg, g, ";".join(grp), ens[i], int(keep[i]), "%.2f" % cpm[i][geno == 0].mean(), "%.2f" % cpm[i][geno == 1].mean(),
                          "%.3f" % d, "%.2f" % t, "%.3g" % pw, "%.3g" % q_all[i] if keep[i] else "NA", "%.3f" % pp, "%.3f" % cs, "%.3g" % ps,
                          "|".join(str(int(v)) for v in cnt[i][geno == 0]) + " / " + "|".join(str(int(v)) for v in cnt[i][geno == 1])])
    # sets: per-animal score = mean over set genes of (logCPM - mean over the region's animals)
    scores = {}
    for sname, genes in list(SETS.items()) + [("HIF_ALL_NONIT7_13", SETS["HIF_SEL_UP6"] + SETS["HIF_FLAT6"] + SINGLE_OTHER), ("IT7_OBS6", IT7_OBS6)]:
        ii = [row_of(g) for g in genes if row_of(g) is not None and keep[row_of(g)]]
        used = [sym[i] for i in ii]
        if not ii: continue
        Z = lc[ii] - lc[ii].mean(1, keepdims=True)
        sc = Z.mean(0); scores[sname] = sc
        d, t, df = welch(sc[geno == 0], sc[geno == 1]); pp, ntot = exact_perm_p(sc, int(geno.sum()), mut)
        cs, ts, dfs, ps = ols_geno_t(sc, geno, sex)
        gl = lfc_all[ii]
        set_rows.append([reg, sname, len(genes), len(ii), ",".join(used), "%.3f" % d, "%.2f" % t, "%.3g" % t_two_sided_p(t, df), "%.3f" % pp, ntot, "%.3f" % cs, "%.3g" % ps,
                         int((gl > 0).sum()), int((gl < 0).sum())])
        for a, s, gv in zip(animals, sc, geno):
            set_animal_rows.append([reg, sname, a, "P47T" if gv else "WT", "%.4f" % s])
    # contrast SEL_UP minus FLAT per animal
    if "HIF_SEL_UP6" in scores and "HIF_FLAT6" in scores:
        sc = scores["HIF_SEL_UP6"] - scores["HIF_FLAT6"]
        d, t, df = welch(sc[geno == 0], sc[geno == 1]); pp, ntot = exact_perm_p(sc, int(geno.sum()), mut)
        set_rows.append([reg, "HIF_SEL_UP6_minus_FLAT6", "", "", "", "%.3f" % d, "%.2f" % t, "%.3g" % t_two_sided_p(t, df), "%.3f" % pp, ntot, "", "", "", ""])
    # composition correlations
    for target in ["HIF_SEL_UP6", "HIF_FLAT6", "NRF2_5", "ACTIVITY_IEG", "HIF_ALL_NONIT7_13"]:
        for comp in ["ASTRO", "MICRO", "OLIGO", "NEURON", "ACTIVITY_IEG"]:
            if target == comp or target not in scores or comp not in scores: continue
            corr_rows.append([reg, target, comp, "all10" if len(geno) == 10 else "all7", "%.2f" % spearman(scores[target], scores[comp]),
                              "WT", "%.2f" % spearman(scores[target][geno == 0], scores[comp][geno == 0]),
                              "P47T", "%.2f" % spearman(scores[target][geno == 1], scores[comp][geno == 1])])
    # validation against the authors' DEG list
    # (done after the loop for all regions)

# ---------- authors' DEG list: validation ----------
auth = collections.defaultdict(dict)
with open(arg("--authors-deg")) as fh:
    rd = csv.DictReader(fh, delimiter="\t")
    for r in rd:
        try:
            auth[r["sheet"]][r["Symbol"].lower()] = (float(r["Expr_Log_Ratio"]), float(r["Expr_FDR"]) if r["Expr_FDR"] != "" else float("nan"))
        except (ValueError, KeyError, TypeError):
            continue
L("authors sheets", {k: len(v) for k, v in auth.items()})
low2sym = {}
for s in sym: low2sym.setdefault(s.lower(), s)
for reg in REGIONS:
    sh = auth.get(reg, {})
    rdd = region_data[reg]
    xs, ys, agree, tot, found = [], [], 0, 0, 0
    for low, (lr, fdr) in sh.items():
        s = low2sym.get(low)
        if s is None: continue
        i = row_of(s)
        if i is None or not rdd["keep"][i]: continue
        found += 1; xs.append(lr); ys.append(rdd["lfc"][i]); tot += 1; agree += int(np.sign(lr) == np.sign(rdd["lfc"][i]))
    xs, ys = np.array(xs), np.array(ys)
    r = float(np.corrcoef(xs, ys)[0, 1]) if len(xs) > 2 else float("nan")
    slope = float(np.polyfit(xs, ys, 1)[0]) if len(xs) > 2 else float("nan")
    val_rows.append([reg, len(sh), found, "%.3f" % r, "%.2f" % slope, "%.3f" % (agree / tot if tot else float("nan")),
                     "authors' logFC sign convention checked as P47T over WT by sign agreement; slope is mine on theirs"])
    # which of the named genes are on the authors' list
    for g in sorted(named_all):
        v = sh.get(g.lower())
        if v: val_rows.append([reg, "named_gene_on_authors_DEG_list", g, "%.3f" % v[0], "%.3g" % v[1], "", ""])

# ---------- GSEA re-implementation ----------
rng = np.random.default_rng(SEED)
NPERM = 2000
def es_of(sorted_stat_abs, pos_mask):
    k = pos_mask.sum(); N = len(pos_mask)
    hit = np.where(pos_mask, sorted_stat_abs, 0.0); nr = hit.sum()
    run = np.cumsum(np.where(pos_mask, hit / nr, -1.0 / (N - k)))
    mx, mn = run.max(), run.min()
    return (mx if abs(mx) >= abs(mn) else mn), run
for reg in REGIONS:
    rdd = region_data[reg]; keep = rdd["keep"]
    gi = np.where(keep & np.isfinite(rdd["t"]))[0]
    # one row per symbol (highest expression)
    seen = {}
    for i in gi:
        s = sym[i]
        if s not in seen or rdd["cpm"][i].mean() > rdd["cpm"][seen[s]].mean(): seen[s] = i
    gi = np.array(sorted(seen.values(), key=lambda i: -rdd["t"][i]))
    stat = rdd["t"][gi]; names = [sym[i] for i in gi]; pos = {n: k for k, n in enumerate(names)}
    absstat = np.abs(stat); N = len(gi)
    res = []
    for hs, genes in hallmark.items():
        gg = [g for g in genes if g in pos]
        if len(gg) < 15: continue
        mask = np.zeros(N, bool); mask[[pos[g] for g in gg]] = True
        es, run = es_of(absstat, mask)
        perm = np.empty(NPERM)
        for b in range(NPERM):
            m = np.zeros(N, bool); m[rng.choice(N, size=len(gg), replace=False)] = True
            perm[b] = es_of(absstat, m)[0]
        pe = perm[perm >= 0] if es >= 0 else perm[perm < 0]
        nes = es / np.abs(pe).mean() if len(pe) else float("nan")
        pval = (np.sum(np.abs(pe) >= abs(es)) + 1) / (len(pe) + 1)
        res.append([hs, len(gg), es, nes, pval, mask, run])
    # FDR over hallmarks (simple BH on permutation p, within region; permutation p is gene-label, anti-conservative)
    ps = np.array([r[4] for r in res]); qs = bh(ps)
    for r, q in zip(res, qs):
        hs, k, es, nes, pval, mask, run = r
        # leading edge
        if es >= 0:
            peak = int(np.argmax(run)); le = [names[j] for j in np.where(mask[:peak + 1])[0]]
        else:
            peak = int(np.argmin(run)); le = [names[j] for j in np.where(mask[peak:])[0] + peak]
        gsea_rows.append([reg, hs, k, "%.3f" % es, "%.2f" % nes, "%.3g" % pval, "%.3g" % q, len(le)])
        if hs in ("HALLMARK_HYPOXIA", "HALLMARK_GLYCOLYSIS", "HALLMARK_APOPTOSIS", "HALLMARK_REACTIVE_OXIGEN_SPECIES_PATHWAY"):
            cls = collections.Counter(klass(g) for g in le)
            le_rows.append([reg, hs, "NES %.2f" % nes, len(le), cls.get("CANON_HIF", 0), cls.get("IEG_STRESS", 0), cls.get("GLIA_REACTIVE", 0), cls.get("OTHER", 0),
                            ";".join("%s(%+.2f)" % (g, rdd["lfc"][seen[g]]) for g in le[:40])])

def w(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="") as fh:
        cw = csv.writer(fh, delimiter="\t", lineterminator="\n"); cw.writerow(header); cw.writerows(rows)
w("genes_it12.tsv", ["region", "gene", "set", "ensembl", "kept_by_expression_filter", "meanCPM_WT", "meanCPM_P47T", "log2FC_P47T_over_WT", "welch_t", "welch_p", "BH_q_region_wide", "exact_perm_p", "log2FC_sex_adjusted", "p_sex_adjusted", "raw_counts_WT / P47T"], gene_rows)
w("sets_it12.tsv", ["region", "set", "n_declared", "n_used", "genes_used", "mean_log2FC_P47T_minus_WT", "welch_t", "welch_p", "exact_perm_p", "n_splits", "sex_adj_diff", "sex_adj_p", "genes_up", "genes_down"], set_rows)
w("set_scores_per_animal_it12.tsv", ["region", "set", "animal", "genotype", "score_log2_centered"], set_animal_rows)
w("composition_correlations_it12.tsv", ["region", "set", "vs_marker_set", "pool", "spearman_all", "grp1", "spearman_grp1", "grp2", "spearman_grp2"], corr_rows)
w("gsea_reimpl_it12.tsv", ["region", "hallmark", "n_genes", "ES", "NES", "perm_p_gene_label", "BH_q_over_50", "leading_edge_size"], gsea_rows)
w("leading_edge_it12.tsv", ["region", "hallmark", "NES", "leading_edge_size", "CANON_HIF", "IEG_STRESS", "GLIA_REACTIVE", "OTHER", "first_40_genes_with_log2FC"], le_rows)
w("validation_vs_authors_it12.tsv", ["region", "metric_or_gene", "n_or_gene", "value1", "value2", "value3", "note"], val_rows)
# ---------- sensitivities: leave-one-animal-out, expression-matched random-set null ----------
loo_rows, null_rows = [], []
rng2 = np.random.default_rng(SEED + 1)
for reg in REGIONS:
    rdd = region_data[reg]; geno = rdd["geno"]; keep = rdd["keep"]; lc = rdd["lc"]; animals = rdd["animals"]
    meanlc = lc.mean(1)
    kidx = np.where(keep)[0]
    edges = np.quantile(meanlc[kidx], np.linspace(0, 1, 21)); bins = np.clip(np.searchsorted(edges, meanlc, side="right") - 1, 0, 19)
    pool = {b: kidx[bins[kidx] == b] for b in range(20)}
    for sname in ["HIF_SEL_UP6", "HIF_FLAT6", "NRF2_5", "ACTIVITY_IEG", "ASTRO"]:
        ii = [row_of(g) for g in SETS[sname] if row_of(g) is not None and keep[row_of(g)]]
        Z = lc[ii] - lc[ii].mean(1, keepdims=True); sc = Z.mean(0)
        full = sc[geno == 1].mean() - sc[geno == 0].mean()
        diffs = []
        for k in range(len(animals)):
            m = np.ones(len(animals), bool); m[k] = False
            if geno[m].sum() < 2 or (1 - geno[m]).sum() < 2: continue
            diffs.append((sc[m & (geno == 1)].mean() - sc[m & (geno == 0)].mean(), animals[k], "P47T" if geno[k] else "WT"))
        lo = min(diffs); hi = max(diffs)
        loo_rows.append([reg, sname, "%.3f" % full, "%.3f" % lo[0], "drop " + lo[1] + "(" + lo[2] + ")", "%.3f" % hi[0], "drop " + hi[1] + "(" + hi[2] + ")"])
        obs = float(np.mean(rdd["lfc"][ii]))
        nulls = np.empty(5000)
        for b in range(5000):
            pick = [rng2.choice(pool[bins[i]]) for i in ii]; nulls[b] = np.mean(rdd["lfc"][pick])
        null_rows.append([reg, sname, len(ii), "%.3f" % obs, "%.3f" % nulls.mean(), "%.3f" % nulls.std(), "%.3f" % ((np.sum(nulls >= obs) + 1) / 5001), "%.3f" % ((np.sum(nulls <= obs) + 1) / 5001)])
w("leave_one_animal_out_it12.tsv", ["region", "set", "full_diff", "min_diff_after_drop", "dropped_for_min", "max_diff_after_drop", "dropped_for_max"], loo_rows)
w("matched_null_it12.tsv", ["region", "set", "n_genes", "observed_mean_log2FC", "null_mean", "null_sd", "p_one_sided_up", "p_one_sided_down"], null_rows)
L("done")
