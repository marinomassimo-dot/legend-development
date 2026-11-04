"""IT27 verifier, P1b: descriptive re-derivation of GSE158681 (hippocampus) and GSE158682 (cortex), P17.
Usage: python3 -I v_p1b_gse1586.py <hippo_TPM.gz> <cortex_TPM.gz> <series_matrix_81.gz> <series_matrix_82.gz> <ensembl92_cdna.fa.gz> <outdir>
Written before the producer's mouse_p17 tables were opened. numpy only. No p-values (n 2-4)."""
import sys, gzip, json, itertools, re
import numpy as np
hip, ctx, sm1, sm2, fa, out = sys.argv[1:7]

def readtpm(p):
    with gzip.open(p, "rt") as f:
        h = f.readline().rstrip("\n").split("\t"); rows = [l.rstrip("\n").split("\t") for l in f]
    ids = [r[0].split(".")[0] for r in rows]; X = np.array([[float(x) for x in r[3:]] for r in rows])
    return h[3:], ids, X
def series(p):
    d = {}
    with gzip.open(p, "rt") as f:
        for l in f:
            if l.startswith("!Sample_title"): d["title"] = [x.strip('"') for x in l.rstrip("\n").split("\t")[1:]]
            if l.startswith("!Sample_geo_accession"): d["gsm"] = [x.strip('"') for x in l.rstrip("\n").split("\t")[1:]]
            if "genotype:" in l and l.startswith("!Sample_char"): d["geno"] = [x.strip('"').split(": ")[1] for x in l.rstrip("\n").split("\t")[1:]]
    return d
t2g, g2s = {}, {}
with gzip.open(fa, "rt") as f:
    for l in f:
        if l[0] == ">":
            t = l[1:].split()[0].split(".")[0]; m = re.search(r"gene:(ENSMUSG\d+)", l); s = re.search(r"gene_symbol:(\S+)", l)
            if m: t2g[t] = m.group(1)
            if m and s: g2s[m.group(1)] = s.group(1)
res = {}
def togene(ids, X):
    gi = {}; miss = 0; keep = []
    for i, t in enumerate(ids):
        g = t2g.get(t)
        if g is None: miss += 1; continue
        gi.setdefault(g, []).append(i)
    genes = sorted(gi); G = np.array([X[gi[g]].sum(0) for g in genes]); return genes, G, miss
H, Hid, HX = readtpm(hip); C, Cid, CX = readtpm(ctx)
s1, s2 = series(sm1), series(sm2)
res["header_equals_series_titles"] = dict(hip=H == s1["title"], ctx=C == s2["title"])
res["gsm_map"] = {"hip": dict(zip(s1["title"], zip(s1["gsm"], s1["geno"]))), "ctx": dict(zip(s2["title"], zip(s2["gsm"], s2["geno"])))}
Hg, HG, hm = togene(Hid, HX); Cg, CG, cm = togene(Cid, CX)
res["tx_total_hip"] = len(Hid); res["tx_unmapped_hip"] = hm; res["genes_hip"] = len(Hg)
res["tx_total_ctx"] = len(Cid); res["tx_unmapped_ctx"] = cm; res["genes_ctx"] = len(Cg)
res["tpm_column_sums_hip"] = [float(x) for x in HX.sum(0)]; res["tpm_column_sums_ctx"] = [float(x) for x in CX.sum(0)]
res["tpm_column_sums_hip_after_gene_map"] = [float(x) for x in HG.sum(0)]
res["integers_in_tpm"] = bool(np.all(HX == np.round(HX)))
hi = {n: i for i, n in enumerate(H)}; ci = {n: i for i, n in enumerate(C)}
arms_h = {"S_Ctrl": ["S_Ctrl_1", "S_Ctrl_2"], "S_KO": ["S_KO_1", "S_KO_2", "S_KO_3"], "N_Ctrl": ["N_Ctrl_1", "N_Ctrl_2"], "N_KO": ["N_KO_1", "N_KO_2"], "null": ["KO_1", "KO_2"], "WT": ["WT_1", "WT_2", "WT_3"]}
arms_c = {"CS_Ctrl": [n for n in C if "S_Ctrl" in n], "CS_KO": [n for n in C if "S_KO" in n]}
def contrast(G, idx, a, b, thr=1.0, pc=0.5):  # b minus a (b = perturbed, a = reference)
    A = G[:, [idx[n] for n in a]]; B = G[:, [idx[n] for n in b]]
    ma, mb = A.mean(1), B.mean(1); lfc = np.log2((mb + pc) / (ma + pc))
    sep = (B.min(1) > A.max(1)) | (B.max(1) < A.min(1)); expr = np.maximum(ma, mb) >= thr
    lfc_c = lfc - np.median(lfc[expr])  # centre on the median over EXPRESSED genes (mean TPM>=1 in the higher arm); all-gene median is 0 by construction (many zero genes)
    return dict(lfc=lfc, lfc_c=lfc_c, sep=sep, expr=expr, ma=ma, mb=mb, med=float(np.median(lfc[expr])))
def counts(c):
    o = {}
    for t in (0.585, 1, 2):
        sel = c["sep"] & c["expr"] & (np.abs(c["lfc_c"]) >= t)
        o[f"cLFC>={t}"] = dict(up=int((sel & (c["lfc_c"] > 0)).sum()), down=int((sel & (c["lfc_c"] < 0)).sum()))
    o["median_lfc_expressed_genes_removed_by_centring"] = c["med"]; o["n_expr"] = int(c["expr"].sum())
    return o
Ctr = {}
res["contrasts"] = {}
spec = [("H_S", "S_Ctrl", "S_KO"), ("H_N", "N_Ctrl", "N_KO"), ("H_null", "WT", "null")]
for nm, a, b in spec:
    c = contrast(HG, hi, arms_h[a], arms_h[b]); Ctr[nm] = c; res["contrasts"][nm] = counts(c)
cc = contrast(CG, ci, arms_c["CS_Ctrl"], arms_c["CS_KO"]); Ctr["C_S"] = cc; res["contrasts"]["C_S"] = counts(cc)
# background controls: control v control (no Wwox deficiency); the null yardstick for a separation rule
for nm, a, b in [("ctl_WT_vs_S_Ctrl", "WT", "S_Ctrl"), ("ctl_WT_vs_N_Ctrl", "WT", "N_Ctrl"), ("ctl_S_Ctrl_vs_N_Ctrl", "S_Ctrl", "N_Ctrl")]:
    c = contrast(HG, hi, arms_h[a], arms_h[b]); Ctr[nm] = c; res["contrasts"][nm] = counts(c)
# within-group split of a larger control (WT: 3 animals -> 1 v 2) as a further null: leave out
# gene-level overlap of KO calls with control-vs-control calls
for nm, ctlnm in [("H_S", "ctl_WT_vs_S_Ctrl"), ("H_N", "ctl_WT_vs_N_Ctrl"), ("H_null", "ctl_WT_vs_S_Ctrl")]:
    c = Ctr[nm]; k = Ctr[ctlnm]
    sel = c["sep"] & c["expr"] & (np.abs(c["lfc_c"]) >= .585)
    selk = k["sep"] & k["expr"] & (np.abs(k["lfc_c"]) >= .585)
    res["contrasts"][nm]["calls_0.585"] = int(sel.sum()); res["contrasts"][nm]["also_in_" + ctlnm] = int((sel & selk).sum())
# exact: chance that a gene shows animal separation under no difference
import math
res["chance_separation_if_exchangeable"] = {f"{a}v{b}": 2.0 / math.comb(a + b, a) for a, b in [(2, 2), (2, 3), (3, 3), (3, 4)]}
# Wwox
wid = [g for g in Hg if g2s.get(g) == "Wwox"]; res["Wwox_ensembl"] = wid
if wid:
    k = Hg.index(wid[0]); res["Wwox_TPM_hip"] = {n: float(HG[k, hi[n]]) for n in H}
    kc = Cg.index(wid[0]); res["Wwox_TPM_ctx"] = {n: float(CG[kc, ci[n]]) for n in C}
    for nm, a, b in spec:
        ma = np.mean([HG[k, hi[n]] for n in arms_h[a]]); mb = np.mean([HG[k, hi[n]] for n in arms_h[b]]); res["contrasts"][nm]["Wwox_pct_reduction"] = float(100 * (1 - mb / ma))
    ma = np.mean([CG[kc, ci[n]] for n in arms_c["CS_Ctrl"]]); mb = np.mean([CG[kc, ci[n]] for n in arms_c["CS_KO"]]); res["contrasts"]["C_S"]["Wwox_pct_reduction"] = float(100 * (1 - mb / ma))
# composition: oligodendrocyte / myelin genes vs neuronal gene share (TPM is compositional)
mark = {"oligo_myelin": ["Mbp", "Plp1", "Mog", "Mobp", "Mag", "Cnp", "Mal", "Opalin", "Ermn", "Cldn11"], "OPC": ["Pdgfra", "Cspg4", "Olig1", "Olig2", "Sox10"],
        "astro": ["Gfap", "Aqp4", "Slc1a3", "Aldh1l1", "Slc1a2"], "microglia": ["Cx3cr1", "P2ry12", "Tmem119", "Aif1", "Csf1r"], "neuron_exc": ["Slc17a7", "Camk2a", "Satb2", "Neurod6"], "neuron_inh": ["Gad1", "Gad2", "Slc32a1"], "pan_neuron": ["Rbfox3", "Syt1", "Snap25", "Stmn2"]}
s2g = {}
for g, s in g2s.items(): s2g.setdefault(s, g)
def comp(G, genes, idx, arms):
    gi = {g: i for i, g in enumerate(genes)}; o = {}
    for ct, syms in mark.items():
        ids = [gi[s2g[s]] for s in syms if s in s2g and s2g[s] in gi]
        o[ct] = {arm: float(np.mean([G[ids][:, idx[n]].sum() for n in ns])) for arm, ns in arms.items()}
        o[ct]["n_genes"] = len(ids)
    return o
res["marker_TPM_sum_per_arm_hip"] = comp(HG, Hg, hi, arms_h); res["marker_TPM_sum_per_arm_ctx"] = comp(CG, Cg, ci, arms_c)
# per-marker-gene cLFC in each contrast (is the median shift explained by composition?)
res["marker_cLFC"] = {}
for nm in ["H_S", "H_N", "H_null", "C_S", "ctl_WT_vs_S_Ctrl", "ctl_WT_vs_N_Ctrl", "ctl_S_Ctrl_vs_N_Ctrl"]:
    genes = Cg if nm == "C_S" else Hg; gi = {g: i for i, g in enumerate(genes)}
    res["marker_cLFC"][nm] = {ct: float(np.median([Ctr[nm]["lfc_c"][gi[s2g[s]]] for s in syms if s in s2g and s2g[s] in gi])) for ct, syms in mark.items()}
    res["marker_cLFC"][nm]["median_shift_removed"] = Ctr[nm]["med"]
# sample-level correlation of log TPM (animal separation): hip all samples
L = np.log2(HG + 1); keep = HG.mean(1) >= 1; Cm = np.corrcoef(L[keep].T)
res["hip_sample_corr_min_within_arm"] = {arm: float(min(Cm[hi[a], hi[b]] for a, b in itertools.combinations(ns, 2))) for arm, ns in arms_h.items() if len(ns) > 1}
res["hip_sample_corr_median_between_arm"] = float(np.median([Cm[hi[a], hi[b]] for ar1, ar2 in itertools.combinations(arms_h, 2) for a in arms_h[ar1] for b in arms_h[ar2]]))
Lc = np.log2(CG + 1); kc2 = CG.mean(1) >= 1; Cc = np.corrcoef(Lc[kc2].T)
res["ctx_corr_matrix_rounded"] = {a: {b: round(float(Cc[ci[a], ci[b]]), 4) for b in C} for a in C}
# write per-contrast full table for the 4 KO contrasts + controls (gene, symbol, means, cLFC, sep)
import csv
with open(f"{out}/p1b_own_contrasts_cLFC_ge0.585_separated.tsv", "w") as f:
    w = csv.writer(f, delimiter="\t"); w.writerow(["contrast", "ensembl", "symbol", "mean_ref_TPM", "mean_pert_TPM", "lfc_uncentred", "cLFC", "separated", "also_in_ctl_vs_ctl_0.585"])
    for nm in ["H_S", "H_N", "H_null", "C_S"]:
        c = Ctr[nm]; genes = Cg if nm == "C_S" else Hg
        ctl = Ctr["ctl_WT_vs_S_Ctrl"] if nm in ("H_S", "H_null") else (Ctr["ctl_WT_vs_N_Ctrl"] if nm == "H_N" else None)
        selk = (ctl["sep"] & ctl["expr"] & (np.abs(ctl["lfc_c"]) >= .585)) if ctl is not None else None
        sel = c["sep"] & c["expr"] & (np.abs(c["lfc_c"]) >= .585)
        for i in np.where(sel)[0]:
            w.writerow([nm, genes[i], g2s.get(genes[i], ""), f"{c['ma'][i]:.3f}", f"{c['mb'][i]:.3f}", f"{c['lfc'][i]:.3f}", f"{c['lfc_c'][i]:.3f}", 1, ("NA" if selk is None else int(selk[i]))])
json.dump(res, open(f"{out}/p1b_summary.json", "w"), indent=1)
print("ok")
