#!/usr/bin/env python3
"""Candidate [4b]: per-neuron Gabrd and nuclear composition in the S-line hippocampus (GSE158684 single-nucleus RNA-seq). Rule, classes and predictions: PREREGISTRATION_4B_SNUC_S_LINE_SCI.md (hashed before any matrix was downloaded). Hypothesis level; numpy only; seeded.
    python3 snuc_s_line_test.py --help
    python3 snuc_s_line_test.py run <dir with GSE158684_{ctrl,ko}_filtered_{matrix.mtx,barcodes.tsv,features.tsv}.gz> <out_prefix>
Writes <out_prefix>_genes.tsv (per gene and class) and <out_prefix>_composition.tsv (class shares per genotype and per sample group)."""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import gzip
import numpy as np
D, PFX = sys.argv[2], sys.argv[3]
SETS = {"excitatory": ["Slc17a7", "Slc17a6", "Camk2a"], "inhibitory": ["Gad1", "Gad2", "Slc32a1"], "astrocyte": ["Aqp4", "Gja1", "Slc1a2", "Aldh1l1"],
        "oligodendrocyte": ["Mbp", "Plp1", "Mog", "Mobp"], "microglia": ["Cx3cr1", "P2ry12", "Csf1r"]}
PANEL = ["Gabrd", "Gabra5", "Gabra1", "Gabrg2", "Slc6a1", "Npy", "Npy2r", "Sst", "Pvalb", "Gad1", "Grin2b", "Grin2a", "Cacna1h", "Cacna1i", "Hcn2", "Slc12a5", "Slc12a2", "Kcnk2", "Kcnq2", "Adora1", "Gfap", "Gja1", "Kcnj10", "Adk", "Wwox"]
WANT = sorted(set(sum(SETS.values(), [])) | set(PANEL) | {"Prox1"})
rng = np.random.default_rng(1)

def load(geno):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open("%s/GSE158684_%s_filtered_features.tsv.gz" % (D, geno), "rt")]
    bcs = [l.strip() for l in gzip.open("%s/GSE158684_%s_filtered_barcodes.tsv.gz" % (D, geno), "rt")]
    sym = [f[1] for f in feats]
    raw = gzip.open("%s/GSE158684_%s_filtered_matrix.mtx.gz" % (D, geno), "rb").read().split(b"\n")
    i = 0
    while raw[i].startswith(b"%"): i += 1
    ng, nb, nnz = (int(x) for x in raw[i].split()); body = np.array(b" ".join(raw[i + 1:]).split(), dtype=np.int64).reshape(-1, 3)
    g = body[:, 0] - 1; b = body[:, 1] - 1; v = body[:, 2].astype(np.float64)
    lib = np.bincount(b, weights=v, minlength=nb)
    idx = {s: k for k, s in enumerate(sym) if s in WANT}
    X = {}
    for s, k in idx.items():
        m = g == k; arr = np.zeros(nb); np.add.at(arr, b[m], v[m]); X[s] = arr
    return bcs, lib, X, set(sym)

data = {}
for geno in ("ctrl", "ko"):
    bcs, lib, X, allsym = load(geno); data[geno] = (bcs, lib, X)
    print(geno, "nuclei", len(bcs), "median UMI", int(np.median(lib)), "panel/marker genes absent from features:", sorted(set(WANT) - allsym))

def classify(lib, X):
    nb = len(lib); sc = {}
    for c, gs in SETS.items():
        vals = [np.log1p(X[g] / lib * 1e4) for g in gs if g in X]; sc[c] = np.mean(vals, axis=0) if vals else np.zeros(nb)
    M = np.column_stack([sc[c] for c in SETS]); best = M.argmax(1); top = M.max(1)
    return np.array([list(SETS)[k] if t > 0 else "unassigned" for k, t in zip(best, top)])

cls = {g: classify(data[g][1], data[g][2]) for g in data}
def suffix(b): return b.rsplit("-", 1)[-1] if "-" in b else "none"
groups = {g: sorted(set(suffix(b) for b in data[g][0])) for g in data}
print("barcode suffix groups:", groups)
by_sample = False   # Amendment 4B-1: the paper states n = 1 per genotype; the unit is the nucleus, pooled; barcode groups are technical libraries (consistency check only)
print("unit of analysis: nucleus (POOLED, pseudo-replicated); barcode groups are technical libraries:", {g: len(groups[g]) for g in groups})

# composition
rows = [["genotype", "sample_group", "n_nuclei"] + list(SETS) + ["unassigned"]]
for g in ("ctrl", "ko"):
    c = cls[g]; sg = np.array([suffix(b) for b in data[g][0]])
    for grp in ["all"] + groups[g]:
        m = np.ones(len(c), bool) if grp == "all" else sg == grp
        n = m.sum(); rows.append([g, grp, n] + ["%.3f" % ((c[m] == k).sum() / n) for k in list(SETS) + ["unassigned"]])
with open(PFX + "_composition.tsv", "w") as f:
    for r in rows: f.write("\t".join(str(x) for x in r) + "\n")

def cpm_log(sub_counts, sub_lib_total):
    return np.log2(sub_counts / sub_lib_total * 1e6 + 1.0)
def pseudobulk(gene, klass, unit):
    out = {}
    for g in ("ctrl", "ko"):
        bcs, lib, X = data[g]; m = cls[g] == klass if klass != "neuron" else np.isin(cls[g], ["excitatory", "inhibitory"])
        if gene not in X: return None
        if unit == "sample":
            sg = np.array([suffix(b) for b in bcs]); vals = []
            for grp in groups[g]:
                mm = m & (sg == grp)
                if mm.sum() >= 20: vals.append(cpm_log(X[gene][mm].sum(), lib[mm].sum()))
            out[g] = np.array(vals)
        else:
            out[g] = (X[gene][m], lib[m])
    return out
res = [["gene", "class", "unit", "C_log2_KO_over_ctrl", "ci_low", "ci_high", "n_nuclei_ctrl", "n_nuclei_ko", "frac_expressing_ctrl", "frac_expressing_ko", "per_library_log2CPM_ctrl", "per_library_log2CPM_ko"]]
for gene in PANEL:
    for klass in ["excitatory", "inhibitory", "astrocyte", "oligodendrocyte", "microglia"]:
        nc = int((cls["ctrl"] == klass).sum()); nk = int((cls["ko"] == klass).sum())
        if nc < 30 or nk < 30 or gene not in data["ctrl"][2]: continue
        mc = cls["ctrl"] == klass; mk = cls["ko"] == klass
        fc = float((data["ctrl"][2][gene][mc] > 0).mean()); fk = float((data["ko"][2][gene][mk] > 0).mean())
        if by_sample:
            pb = pseudobulk(gene, klass, "sample")
            if len(pb["ctrl"]) < 3 or len(pb["ko"]) < 3: continue
            d = pb["ko"].mean() - pb["ctrl"].mean()
            bt = rng.choice(pb["ko"], (10000, len(pb["ko"]))).mean(1) - rng.choice(pb["ctrl"], (10000, len(pb["ctrl"]))).mean(1)
            unit = "sample"
        else:
            (xc, lc), (xk, lk) = pseudobulk(gene, klass, "nucleus")["ctrl"], pseudobulk(gene, klass, "nucleus")["ko"]
            d = cpm_log(xk.sum(), lk.sum()) - cpm_log(xc.sum(), lc.sum()); bt = []
            for _ in range(1000):
                ic = rng.integers(0, len(xc), len(xc)); ik = rng.integers(0, len(xk), len(xk))
                bt.append(cpm_log(xk[ik].sum(), lk[ik].sum()) - cpm_log(xc[ic].sum(), lc[ic].sum()))
            bt = np.array(bt); unit = "nucleus (pseudo-replicated)"
        def libs(g, m, gg):
            bcs, lib, X = data[g]; sg = np.array([suffix(b) for b in bcs]); o = []
            for grp in groups[g]:
                mm = m & (sg == grp)
                o.append("%.2f" % cpm_log(X[gene][mm].sum(), lib[mm].sum()) if mm.sum() >= 20 else "NA")
            return ",".join(o)
        res.append([gene, klass, unit, "%+.2f" % d, "%+.2f" % np.percentile(bt, 2.5), "%+.2f" % np.percentile(bt, 97.5), nc, nk, "%.3f" % fc, "%.3f" % fk, libs("ctrl", mc, gene), libs("ko", mk, gene)])
with open(PFX + "_genes.tsv", "w") as f:
    for r in res: f.write("\t".join(str(x) for x in r) + "\n")
print("wrote", PFX + "_genes.tsv", PFX + "_composition.tsv")
