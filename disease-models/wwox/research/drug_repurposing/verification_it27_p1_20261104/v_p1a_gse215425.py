"""IT27 verifier, P1a: independent re-analysis of GSE215425 (P47T v WT, 4 regions).
Usage: python3 -I v_p1a_gse215425.py <processed_data.csv.gz> <series_matrix.txt.gz> <outdir> <pylib>
Written BEFORE the producer's per-gene tables were opened. pylib = a --target pip dir with scipy, pandas, pydeseq2.
"""
import sys, gzip, json, re, warnings
pylib = sys.argv[4]; sys.path.insert(0, pylib)
import numpy as np, pandas as pd
from scipy import stats
warnings.filterwarnings("ignore")
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
csv, smx, out = sys.argv[1], sys.argv[2], sys.argv[3]

# ---- sample map from the GEO series matrix (independent of CSV header) ----
meta = {}
with gzip.open(smx, "rt") as f:
    for ln in f:
        if ln.startswith("!Sample_title"): titles = [x.strip('"') for x in ln.rstrip("\n").split("\t")[1:]]
        if ln.startswith("!Sample_geo_accession"): gsm = [x.strip('"') for x in ln.rstrip("\n").split("\t")[1:]]
        if ln.startswith("!Sample_characteristics_ch1") and "genotype:" in ln: gt = [x.strip('"').split(": ")[1] for x in ln.rstrip("\n").split("\t")[1:]]
        if ln.startswith("!Sample_characteristics_ch1") and "region:" in ln: rg = [x.strip('"').split(": ")[1] for x in ln.rstrip("\n").split("\t")[1:]]
rows = []
for t, g, geno, reg in zip(titles, gsm, gt, rg):
    m = re.match(r"(PFC|HPC|CTX|CB)_(WT/WT|P47T/P47T)_([MF])(\d+)", t)
    rows.append(dict(title=t, gsm=g, region=m.group(1), geno_title=m.group(2), geno_meta=geno, sex=m.group(3), animal=m.group(3) + m.group(4), region_meta=reg))
smap = pd.DataFrame(rows)
smap["geno_consistent"] = smap.apply(lambda r: (r.geno_title == "WT/WT") == ("WT/WT" in r.geno_meta), axis=1)
smap["genotype"] = np.where(smap.geno_title == "WT/WT", "WT", "P47T")
smap.to_csv(f"{out}/p1a_sample_map.tsv", sep="\t", index=False)
assert smap.geno_consistent.all() and len(set(smap.gsm)) == 37 and len(set(smap.title)) == 37

df = pd.read_csv(csv, sep=None, engine="python")
gene_id, sym = df.columns[0], df.columns[1]
assert list(df.columns[2:]) == list(smap.title), "CSV header order != series matrix order"
X = df.iloc[:, 2:].to_numpy()
isint = bool(np.all(X == np.round(X)))
cnt = pd.DataFrame(X.astype(int).T, index=smap.title, columns=df[gene_id].values)
sy = pd.Series(df[sym].values, index=df[gene_id].values)
info = dict(csv_integer=isint, n_genes=int(X.shape[0]), dup_symbols=int(df[sym].duplicated().sum()), dup_ids=int(df[gene_id].duplicated().sum()))

# animals across regions
an = smap.groupby("animal").agg(regions=("region", lambda s: sorted(set(s))), geno=("genotype", "first"), sex=("sex", "first"), n_libs=("gsm", "count"))
an.to_csv(f"{out}/p1a_animal_map.tsv", sep="\t")
info["animals"] = {a: dict(regions=r.regions, geno=r.geno, sex=r.sex) for a, r in an.iterrows()}
info["n_animals"] = int(len(an))
info["sex_by_genotype"] = {g: {s: int(((an.geno == g) & (an.sex == s)).sum()) for s in "MF"} for g in ["WT", "P47T"]}
# phi coefficient sex ~ genotype (10 animals)
a = (an.geno == "P47T").astype(int).values; b = (an.sex == "F").astype(int).values
info["phi_sex_genotype_animals"] = float(np.corrcoef(a, b)[0, 1])

def sizefactors(c):  # median of ratios over genes with all counts >0
    lc = np.log(c.where(c > 0))
    ok = c.gt(0).all(axis=0)
    ref = lc.loc[:, ok].mean(axis=0)
    return np.exp((lc.loc[:, ok] - ref).median(axis=1))

def filt(c, g):  # filterByExpr-like: CPM >= 10/median lib (M) in >= smaller group size
    lib = c.sum(axis=1); cpm = c.div(lib, axis=0) * 1e6
    thr = 10 / (np.median(lib) / 1e6); mn = g.value_counts().min()
    return (cpm >= thr).sum(axis=0) >= mn

def run_deseq(c, md, design, nc=1):
    dds = DeseqDataSet(counts=c, metadata=md, design=design, refit_cooks=True, n_cpus=nc, quiet=True)
    dds.deseq2()
    ds = DeseqStats(dds, contrast=["genotype", "P47T", "WT"], quiet=True)
    ds.summary()
    r = ds.results_df.copy()
    return r, dds

def ols_producer_like(c, md, sf, with_sex=True):
    y = np.log2(c.div(sf, axis=0) + 0.5).to_numpy()
    g = (md.genotype == "P47T").astype(float).to_numpy()
    cols = [np.ones(len(g)), g] + ([(md.sex == "F").astype(float).to_numpy()] if with_sex else [])
    D = np.column_stack(cols); n, p = D.shape
    beta, *_ = np.linalg.lstsq(D, y, rcond=None)
    res = y - D @ beta; s2 = (res ** 2).sum(0) / (n - p)
    XtXi = np.linalg.inv(D.T @ D); se = np.sqrt(s2 * XtXi[1, 1])
    t = beta[1] / se; pv = 2 * stats.t.sf(np.abs(t), n - p)
    return pd.DataFrame(dict(lfc=beta[1], p=pv), index=c.columns)

def bh(p):
    p = pd.Series(p); m = p.notna().sum(); o = p.rank(method="first")
    q = p * m / o
    s = p.dropna().sort_values(ascending=False)
    qq = (s * m / o[s.index]).cummin().clip(upper=1)
    out = pd.Series(np.nan, index=p.index); out[qq.index] = qq
    return out

allres = {}; summ = {}
regions = ["PFC", "CTX", "HPC", "CB"]
for reg in regions:
    sm = smap[smap.region == reg].set_index("title")
    c0 = cnt.loc[sm.index]
    keep = filt(c0, sm.genotype)
    c = c0.loc[:, keep]
    md = sm[["genotype", "sex"]].copy()
    md["genotype"] = pd.Categorical(md.genotype, categories=["WT", "P47T"])
    sf = sizefactors(c)
    S = dict(n=int(len(sm)), n_wt=int((sm.genotype == "WT").sum()), n_mut=int((sm.genotype == "P47T").sum()), genes_kept=int(keep.sum()),
             libsize_ratio_mut_over_wt=float(c0.sum(1)[sm.genotype == "P47T"].mean() / c0.sum(1)[sm.genotype == "WT"].mean()),
             sf_ratio_mut_over_wt=float(sf[sm.genotype == "P47T"].mean() / sf[sm.genotype == "WT"].mean()))
    r1, dds = run_deseq(c, md, "~sex+genotype")
    r2, _ = run_deseq(c, md, "~genotype")
    o1 = ols_producer_like(c, md, sf, True); o1["fdr"] = bh(o1.p)
    o2 = ols_producer_like(c, md, sf, False); o2["fdr"] = bh(o2.p)
    S["lfc_median_deseq_sex"] = float(r1.log2FoldChange.median())
    S["lfc_median_ols_sex"] = float(o1.lfc.median())
    # global-shift check: genes by expression decile -> median LFC (a global shift would sit in all deciles)
    bm = r1.baseMean; dec = pd.qcut(bm.rank(method="first"), 5, labels=False)
    S["median_lfc_by_expr_quintile"] = [float(r1.log2FoldChange[dec == k].median()) for k in range(5)]
    for nm, r in [("sex", r1), ("nosex", r2)]:
        S[f"deseq_{nm}"] = dict(padj_lt10=int((r.padj < .10).sum()), padj_lt05=int((r.padj < .05).sum()),
                               padj05_abs1_5=int(((r.padj < .05) & (r.log2FoldChange.abs() >= .585)).sum()),
                               padj05_abs2=int(((r.padj < .05) & (r.log2FoldChange.abs() >= 1)).sum()),
                               up10=int(((r.padj < .10) & (r.log2FoldChange > 0)).sum()), dn10=int(((r.padj < .10) & (r.log2FoldChange < 0)).sum()),
                               n_padj_na=int(r.padj.isna().sum()))
    for nm, o in [("sex", o1), ("nosex", o2)]:
        S[f"ols_{nm}"] = dict(fdr_lt10=int((o.fdr < .10).sum()), fdr_lt05=int((o.fdr < .05).sum()),
                             fdr05_abs1_5_centred=int(((o.fdr < .05) & ((o.lfc - o.lfc.median()).abs() >= .585)).sum()))
    # concordance deseq vs ols (same filtered set, same design)
    j = r1.join(o1, how="inner")
    S["spearman_lfc_deseq_vs_ols"] = float(stats.spearmanr(j.log2FoldChange, j.lfc).correlation)
    S["pearson_lfc_deseq_vs_ols_centred"] = float(np.corrcoef(j.log2FoldChange - j.log2FoldChange.median(), j.lfc - j.lfc.median())[0, 1])
    S["slope_ols_on_deseq"] = float(np.polyfit(j.log2FoldChange - j.log2FoldChange.median(), j.lfc - j.lfc.median(), 1)[0])
    d10, o10 = set(r1.index[r1.padj < .10]), set(o1.index[o1.fdr < .10])
    S["calls_FDR10_overlap"] = dict(deseq=len(d10), ols=len(o10), both=len(d10 & o10), jaccard=float(len(d10 & o10) / max(1, len(d10 | o10))),
                                    same_sign_in_both=int(sum(np.sign(r1.log2FoldChange[g]) == np.sign(o1.lfc[g]) for g in d10 & o10)))
    d5 = set(r1.index[(r1.padj < .05) & (r1.log2FoldChange.abs() >= 1)]); o5 = set(o1.index[(o1.fdr < .05) & ((o1.lfc - o1.lfc.median()).abs() >= 1)])
    S["calls_FDR05_2x_overlap"] = dict(deseq=len(d5), ols=len(o5), both=len(d5 & o5), jaccard=float(len(d5 & o5) / max(1, len(d5 | o5))))
    # sex term sensitivity
    jj = r1.join(r2, rsuffix="_ns", how="inner")
    S["sex_sensitivity"] = dict(spearman_lfc=float(stats.spearmanr(jj.log2FoldChange, jj.log2FoldChange_ns).correlation),
                                calls10_with=int((jj.padj < .1).sum()), calls10_without=int((jj.padj_ns < .1).sum()),
                                both=int(((jj.padj < .1) & (jj.padj_ns < .1)).sum()))
    # Wwox
    w = [g for g in r1.index if sy.get(g) == "Wwox"]
    S["Wwox"] = {g: dict(lfc=float(r1.log2FoldChange[g]), padj=float(r1.padj[g]), baseMean=float(r1.baseMean[g])) for g in w}
    # sex genes
    sg = {}
    for s in ["Xist", "Ddx3y", "Uty", "Kdm5d"]:
        ids = [g for g in c0.columns if sy.get(g) == s]
        if ids:
            v = c0[ids[0]]; sg[s] = dict(F_min_max=[int(v[sm.sex == "F"].min()), int(v[sm.sex == "F"].max())], M_min_max=[int(v[sm.sex == "M"].min()), int(v[sm.sex == "M"].max())])
    S["sex_genes_counts"] = sg
    # BH over regions later; store
    out_r = r1.join(r2[["log2FoldChange", "pvalue", "padj"]], rsuffix="_nosex").join(o1.rename(columns={"lfc": "ols_lfc", "p": "ols_p", "fdr": "ols_fdr"}))
    out_r.insert(0, "symbol", sy.reindex(out_r.index).values); out_r.insert(0, "region", reg)
    allres[reg] = out_r
    summ[reg] = S
    # ---- LOAO for PFC and CTX ----
    if reg in ("PFC", "CTX"):
        full_strong = set(r1.index[(r1.padj < .05) & (r1.log2FoldChange.abs() >= 1)])
        full_mid = set(r1.index[(r1.padj < .10)])
        full_sign = r1.log2FoldChange
        loao = {}; keepcount = {g: 0 for g in full_mid}; keepstrong = {g: 0 for g in full_strong}
        lfc_range = {g: [] for g in full_strong}
        for an_ in sorted(sm.animal.unique()):
            sub = sm[sm.animal != an_]
            cs = c.loc[sub.index]; mds = md.loc[sub.index].copy()
            mds["genotype"] = pd.Categorical(mds.genotype.astype(str), categories=["WT", "P47T"])
            rr, _ = run_deseq(cs, mds, "~sex+genotype")
            loao[an_] = dict(calls_padj10=int((rr.padj < .10).sum()), strong_kept_padj10_same_sign=int(sum((rr.padj.get(g, 1) < .10) and np.sign(rr.log2FoldChange[g]) == np.sign(full_sign[g]) for g in full_strong)),
                             strong_n=len(full_strong))
            for g in full_mid:
                if g in rr.index and rr.padj[g] < .10 and np.sign(rr.log2FoldChange[g]) == np.sign(full_sign[g]): keepcount[g] += 1
            for g in full_strong:
                if g in rr.index:
                    lfc_range[g].append(float(rr.log2FoldChange[g]))
                    if rr.padj[g] < .10 and np.sign(rr.log2FoldChange[g]) == np.sign(full_sign[g]): keepstrong[g] += 1
        S["LOAO"] = dict(per_animal=loao,
                         strong_genes_FDR05_2x=len(full_strong), strong_kept_in_all10=int(sum(v == 10 for v in keepstrong.values())),
                         strong_kept_in_ge8=int(sum(v >= 8 for v in keepstrong.values())),
                         mid_genes_FDR10=len(full_mid), mid_kept_in_all10=int(sum(v == 10 for v in keepcount.values())), mid_kept_in_ge8=int(sum(v >= 8 for v in keepcount.values())),
                         strong_sign_flip_any=int(sum(np.sign(min(v)) != np.sign(max(v)) for v in lfc_range.values() if v)))
        lo = pd.DataFrame(dict(symbol=sy.reindex(list(keepcount)).values, loao_kept_of10=list(keepcount.values()), full_lfc=[full_sign[g] for g in keepcount], full_padj=[r1.padj[g] for g in keepcount]), index=list(keepcount))
        lo.to_csv(f"{out}/p1a_{reg}_loao_stability_FDR10genes.tsv", sep="\t")
    print(reg, "done", flush=True)

# cross-region: BH over all four regions pooled (DESeq2 p, sex model)
P = pd.concat([allres[r][["pvalue"]].assign(region=r) for r in regions])
P["fdr_pooled"] = bh(P.pvalue.reset_index(drop=True)).values
cr = {}
for r in regions:
    q = P[P.region == r]
    cr[r] = dict(within_region_padj10=int((allres[r].padj < .10).sum()), pooled_fdr10=int((q.fdr_pooled < .10).sum()),
                 within_region_padj05=int((allres[r].padj < .05).sum()), pooled_fdr05=int((q.fdr_pooled < .05).sum()))
    allres[r]["fdr_pooled_4regions"] = q.fdr_pooled.values
# also Bonferroni-like over regions: padj*4
for r in regions: cr[r]["padj_x4_lt05"] = int((allres[r].padj * 4 < .05).sum())
info["correction_scope"] = cr
# cross-region concordance PFC v CTX (NOT independent evidence: same animals)
j = allres["PFC"].join(allres["CTX"], lsuffix="_PFC", rsuffix="_CTX", how="inner")
both = j[(j.padj_PFC < .10) & (j.padj_CTX < .10)]
info["PFC_CTX_same_animals_concordance"] = dict(n_shared_genes=int(len(j)), spearman_lfc_all=float(stats.spearmanr(j.log2FoldChange_PFC, j.log2FoldChange_CTX).correlation),
                                                 n_both_padj10=int(len(both)), same_sign_both=int((np.sign(both.log2FoldChange_PFC) == np.sign(both.log2FoldChange_CTX)).sum()))
# animal effect shared across regions: correlation of genotype-adjusted residual of log2 normalized expression, per animal, across PFC & CTX, over genes
def resid(reg):
    sm = smap[smap.region == reg].set_index("title"); c = cnt.loc[sm.index]; c = c.loc[:, filt(c, sm.genotype)]
    y = np.log2(c.div(sizefactors(c), axis=0) + .5); y.index = sm.animal.values
    g = pd.Series((sm.genotype == "P47T").astype(float).values, index=y.index)
    return y - y.groupby(g.values).transform("mean")
rp, rc = resid("PFC"), resid("CTX"); common = [a for a in rp.index if a in rc.index]; cg = rp.columns.intersection(rc.columns)
# per-animal vector over genes -> correlate pairwise (same animal v different animal)
same = [np.corrcoef(rp.loc[a, cg], rc.loc[a, cg])[0, 1] for a in common]
diff = [np.corrcoef(rp.loc[a, cg], rc.loc[b, cg])[0, 1] for a in common for b in common if a != b]
info["animal_effect_PFC_CTX_resid_corr"] = dict(same_animal_mean=float(np.mean(same)), different_animal_mean=float(np.mean(diff)))

json.dump(dict(info=info, regions=summ), open(f"{out}/p1a_summary.json", "w"), indent=1, default=str)
pd.concat(allres.values()).reset_index(names="ensembl").to_csv(f"{out}/p1a_all_regions_own_results.tsv.gz", sep="\t", index=False, float_format="%.5g")
print("ok")
