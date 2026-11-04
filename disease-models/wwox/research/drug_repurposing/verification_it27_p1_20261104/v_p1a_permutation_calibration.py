"""IT27 verifier P1a: null calibration by genotype-label permutation (animals relabelled; sex kept in the design).
Only relabellings sharing <=2 animals (CB: <=1) with the true mutant set are used, so a real genotype effect cannot leak much.
Usage: python3 -I v_p1a_permutation_calibration.py <processed_data.csv.gz> <series_matrix.txt.gz> <outdir> <pylib> <n_perm>"""
import sys, gzip, re, json, itertools, warnings
sys.path.insert(0, sys.argv[4]); warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from scipy import stats
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
csv, smx, out, _, nperm = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
with gzip.open(smx, "rt") as f:
    for ln in f:
        if ln.startswith("!Sample_title"): titles = [x.strip('"') for x in ln.rstrip("\n").split("\t")[1:]]
smap = pd.DataFrame([dict(title=t, region=re.match(r"(\w+?)_", t).group(1), genotype=("WT" if "WT/WT" in t else "P47T"), sex=t.split("_")[-1][0], animal=t.split("_")[-1]) for t in titles])
df = pd.read_csv(csv, sep=None, engine="python"); cnt = pd.DataFrame(df.iloc[:, 2:].to_numpy().astype(int).T, index=smap.title, columns=df.iloc[:, 0].values)
def filt(c, g):
    lib = c.sum(axis=1); cpm = c.div(lib, axis=0) * 1e6
    return ((cpm >= 10 / (np.median(lib) / 1e6)).sum(axis=0) >= g.value_counts().min())
def sf_(c):
    lc = np.log(c.where(c > 0)); ok = c.gt(0).all(axis=0); return np.exp((lc.loc[:, ok] - lc.loc[:, ok].mean(axis=0)).median(axis=1))
def ols(c, md, sf):
    y = np.log2(c.div(sf, axis=0) + .5).to_numpy(); D = np.column_stack([np.ones(len(md)), (md.genotype == "P47T").astype(float), (md.sex == "F").astype(float)])
    b, *_ = np.linalg.lstsq(D, y, rcond=None); r = y - D @ b; n, p = D.shape; s2 = (r ** 2).sum(0) / (n - p); se = np.sqrt(s2 * np.linalg.inv(D.T @ D)[1, 1])
    pv = 2 * stats.t.sf(np.abs(b[1] / se), n - p); o = np.argsort(pv); m = len(pv); q = np.empty(m); q[o] = np.minimum.accumulate((pv[o] * m / (np.arange(m) + 1))[::-1])[::-1]; return np.minimum(q, 1)
rng = np.random.default_rng(20261104); res = {}
for reg, maxov in [("HPC", 2), ("CTX", 2), ("PFC", 2), ("CB", 1)]:
    sm = smap[smap.region == reg].set_index("title"); an = list(sm.animal); true = set(sm.animal[sm.genotype == "P47T"]); k = len(true)
    cand = [s for s in itertools.combinations(an, k) if len(set(s) & true) <= maxov]
    pick = [cand[i] for i in rng.choice(len(cand), size=min(nperm, len(cand)), replace=False)]
    c = cnt.loc[sm.index]; c = c.loc[:, filt(c, sm.genotype)]; sf = sf_(c); rows = []
    for s in pick:
        md = sm[["sex"]].copy(); md["genotype"] = pd.Categorical(["P47T" if a in s else "WT" for a in sm.animal], categories=["WT", "P47T"])
        dds = DeseqDataSet(counts=c, metadata=md, design="~sex+genotype", refit_cooks=True, n_cpus=1, quiet=True); dds.deseq2()
        ds = DeseqStats(dds, contrast=["genotype", "P47T", "WT"], quiet=True); ds.summary(); r = ds.results_df
        q = ols(c, md, sf)
        rows.append(dict(mutant_labels=list(s), overlap_with_true=len(set(s) & true), deseq_padj10=int((r.padj < .1).sum()), deseq_padj05=int((r.padj < .05).sum()), deseq_p05_nominal=int((r.pvalue < .05).sum()), ols_fdr10=int((q < .1).sum()), n_genes=int(len(r))))
        print(reg, rows[-1], flush=True)
    res[reg] = rows
json.dump(res, open(f"{out}/p1a_permutation_calibration.json", "w"), indent=1)
