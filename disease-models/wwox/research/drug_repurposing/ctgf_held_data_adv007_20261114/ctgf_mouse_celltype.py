#!/usr/bin/env python3
"""ADV-007, part B: Ccn2 (mouse Ctgf) in the held mouse bulk TPM tables (GSE158681/2, IT24 and IT27), in the held mouse P47T
DESeq2 results, in the held snRNA matrices (GSE158684), and its cell-type origin in the held GSE73721 table.

Reads only files already held. No network. Needs numpy. Not medical advice; nothing here is WWOX evidence about a patient.

    python3 ctgf_mouse_celltype.py --help
    python3 ctgf_mouse_celltype.py run <repo_root> <files_dir> <out_dir>

<repo_root>  worktree root (committed IT24/IT27 results are read from it)
<files_dir>  the shared gitignored files/ of the main checkout (geo/ and supplement/)
Writes mouse_bulk_ccn2.tsv, p47t_ccn2.tsv, snrna_ccn2.tsv, celltype_origin.tsv, mouse_proxy_identification.json.

The Ensembl-92 cDNA file that IT24/IT27 used to sum transcripts to genes is NOT held. The gene-level Ccn2 value is therefore
rebuilt as a PROXY: the one transcript row (ENSMUST00000020171.11) whose four group means, among all 111,083 rows, fall at 85 to
100 percent of the four gene-level group means that the committed IT24/IT27 tables print for Ccn2 (H_N and H_null, both arms).
It is labelled a proxy everywhere; it is not the gene sum.
"""
import sys

if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv, gzip, json, math, statistics
from pathlib import Path
import numpy as np

REPO, FILES, OUT = Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
OUT.mkdir(parents=True, exist_ok=True)
DR = REPO / "disease-models/wwox/research/drug_repurposing"
SUP = FILES / "supplement/GSE158681_GSE158682_r2b"


def load(fn):
    f = gzip.open(SUP / fn, "rt")
    h = f.readline().rstrip("\n").split("\t")
    return h[3:], {l.split("\t", 1)[0]: np.array(l.rstrip("\n").split("\t")[3:], float) for l in f}


hcols, HIP = load("GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz")
ccols, CTX = load("GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz")

# ---- 1. identify the proxy row from the four published gene-level group means (committed IT24/IT27 tables)
rows = [r for r in csv.DictReader(open(DR / "wwox_data_it24_p4_20261104/results/mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t") if r["symbol"] == "Ctgf"]
pub = {r["contrast"]: (float(r["mean_TPM_control"]), float(r["mean_TPM_KO"])) for r in rows}
H = lambda ns: [hcols.index(n) for n in ns]
ARMS_H = {"H_S": (["S_Ctrl_1", "S_Ctrl_2"], ["S_KO_1", "S_KO_2", "S_KO_3"]), "H_N": (["N_Ctrl_1", "N_Ctrl_2"], ["N_KO_1", "N_KO_2"]),
          "H_null": (["WT_1", "WT_2", "WT_3"], ["KO_1", "KO_2"])}
target = np.array([pub["H_N"][0], pub["H_N"][1], pub["H_null"][0], pub["H_null"][1]])  # N_Ctrl, N_KO, WT, null_KO (TPM, 2-decimal rounding)
gm = lambda v, names: float(v[H(names)].mean())
ids = list(HIP)
M = np.array([[gm(HIP[i], ARMS_H["H_N"][0]), gm(HIP[i], ARMS_H["H_N"][1]), gm(HIP[i], ARMS_H["H_null"][0]), gm(HIP[i], ARMS_H["H_null"][1])] for i in ids])
cand = np.where(np.all((M >= 0.85 * target) & (M <= target + 0.01), axis=1))[0]
assert len(cand) == 1, f"proxy not unique: {[ids[i] for i in cand]}"
PROXY = ids[cand[0]]
wide = [ids[i] for i in np.where(np.all((M >= 0.70 * target) & (M <= 1.05 * target), axis=1))[0]]
ident = {"proxy_transcript": PROXY, "rows_scanned": len(ids), "unique_row_within_85_to_100_percent_of_all_four_published_means": True,
         "rows_within_70_to_105_percent_of_all_four_published_means": wide,
         "status": "inference by number matching, not by annotation; no single row reproduces the published gene-level means exactly, so the gene value is a sum over several transcripts and the proxy is a lower bound",
         "published_gene_level_means_N_Ctrl_N_KO_WT_nullKO": target.tolist(), "proxy_means": M[cand[0]].round(3).tolist(),
         "proxy_fraction_of_published": (M[cand[0]] / target).round(3).tolist(),
         "reading": "the remaining 0.4 to 12.5 percent are other Ccn2 transcripts (not identified); the proxy undercounts the gene by about 0.4 to 12.5 percent in these four numbers, so absolute TPM is a lower bound and a ratio is slightly biased towards no change where a small transcript moves the other way"}
json.dump(ident, open(OUT / "mouse_proxy_identification.json", "w"), indent=1)

# ---- 2. per-contrast values (proxy), uncentred and centred by the committed median shift of each contrast
summ = json.load(open(DR / "wwox_data_it24_p4_20261104/results/mouse_p17_summary.json"))["contrasts"]
medshift = {k: v["median_shift"] for k, v in summ.items()}
CONTRASTS = [("H_S", HIP, hcols, *ARMS_H["H_S"], "S deletion hippocampus (S_KO v S_Ctrl)"),
             ("H_N", HIP, hcols, *ARMS_H["H_N"], "N deletion hippocampus (N_KO v N_Ctrl)"),
             ("H_null", HIP, hcols, *ARMS_H["H_null"], "null deletion hippocampus (KO v WT)"),
             ("C_S", CTX, ccols, [f"CRTX_S_Ctrl_{i}" for i in range(1, 5)], [f"CRTX_S_KO_{i}" for i in range(1, 4)], "S deletion cortex (S_KO v S_Ctrl)")]
BG = [("CC_WT_vs_SCtrl", ["WT_1", "WT_2", "WT_3"], ["S_Ctrl_1", "S_Ctrl_2"]), ("CC_WT_vs_NCtrl", ["WT_1", "WT_2", "WT_3"], ["N_Ctrl_1", "N_Ctrl_2"]),
      ("CC_SCtrl_vs_NCtrl", ["S_Ctrl_1", "S_Ctrl_2"], ["N_Ctrl_1", "N_Ctrl_2"])]
COMMITTED = {"H_N": 1.111, "H_null": -0.773}  # centred log2 at gene level, mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv and p1b_own_contrasts_*.tsv
out = []
for name, T, cols, ctl, ko, desc in CONTRASTS:
    v = T[PROXY]
    a = [float(v[cols.index(n)]) for n in ko]
    b = [float(v[cols.index(n)]) for n in ctl]
    ma, mb = statistics.fmean(a), statistics.fmean(b)
    unc = math.log2((ma + .5) / (mb + .5))
    sep = bool(min(a) > max(b) or max(a) < min(b))
    ref_wwox = None
    out.append(dict(contrast=name, description=desc, proxy_ko_tpm_per_animal=";".join(f"{x:.2f}" for x in a), proxy_control_tpm_per_animal=";".join(f"{x:.2f}" for x in b),
                    mean_ko=round(ma, 2), mean_ctl=round(mb, 2), log2_uncentred=round(unc, 3), median_shift_committed=round(medshift[name], 3),
                    log2_centred=round(unc - medshift[name], 3), committed_gene_level_centred_log2=COMMITTED.get(name, "not in the committed called list (below 0.585, not separated, or TPM < 1)"), animals_separate=sep, n_ko=len(a), n_ctl=len(b),
                    direction="up" if unc > 0 else "down"))
for name, a_n, b_n in BG:
    v = HIP[PROXY]
    a = [float(v[hcols.index(n)]) for n in a_n]
    b = [float(v[hcols.index(n)]) for n in b_n]
    ma, mb = statistics.fmean(a), statistics.fmean(b)
    unc = math.log2((ma + .5) / (mb + .5))
    out.append(dict(contrast=name, description="control v control (no deletion contrast)", proxy_ko_tpm_per_animal=";".join(f"{x:.2f}" for x in a),
                    proxy_control_tpm_per_animal=";".join(f"{x:.2f}" for x in b), mean_ko=round(ma, 2), mean_ctl=round(mb, 2), log2_uncentred=round(unc, 3),
                    median_shift_committed="", log2_centred="", committed_gene_level_centred_log2="", animals_separate=bool(min(a) > max(b) or max(a) < min(b)), n_ko=len(a), n_ctl=len(b),
                    direction="first_group_higher" if unc > 0 else "first_group_lower"))
cols_out = list(out[0])
with open(OUT / "mouse_bulk_ccn2.tsv", "w", encoding="utf-8") as f:
    f.write("\t".join(cols_out) + "\n")
    for r in out:
        f.write("\t".join(str(r[c]) for c in cols_out) + "\n")

# ---- 3. P47T (missense knock-in), committed DESeq2 table of IT27 and the IT24 OLS table
p47 = []
import io
for r in csv.DictReader(io.TextIOWrapper(gzip.open(DR / "verification_it27_p1_20261104/results/p1a_all_regions_own_results.tsv.gz"), encoding="utf-8"), delimiter="\t"):
    if r["symbol"] == "Ccn2":
        p47.append(dict(region=r["region"], deseq2_log2FC=r["log2FoldChange"], deseq2_pvalue=r["pvalue"], deseq2_padj_within_region=r["padj"], deseq2_padj_pooled_4_regions=r["fdr_pooled_4regions"],
                        deseq2_log2FC_no_sex_term=r["log2FoldChange_nosex"], deseq2_padj_no_sex_term=r["padj_nosex"], ols_lfc=r["ols_lfc"], ols_fdr=r["ols_fdr"]))
with open(OUT / "p47t_ccn2.tsv", "w", encoding="utf-8") as f:
    c = list(p47[0]); f.write("\t".join(c) + "\n")
    for r in p47:
        f.write("\t".join(str(r[k]) for k in c) + "\n")

# ---- 4. snRNA pools (GSE158684): one pool per arm; nuclei-level counts of Ccn2 and a few cell-type markers
G = FILES / "geo/GSE158684"
MARK = {"Ccn2": "Ccn2/Ctgf", "Wwox": "Wwox", "Snap25": "neuron", "Aqp4": "astrocyte", "Gfap": "astrocyte/reactive", "Slc1a3": "astrocyte/radial glia",
        "Cldn5": "endothelial", "Flt1": "endothelial", "Pecam1": "endothelial", "Vim": "progenitor/reactive/endothelial", "Nes": "progenitor",
        "Plp1": "oligodendrocyte", "Pdgfra": "OPC", "Cx3cr1": "microglia"}
sn = []
nuc_detail = {}
for arm in ("ctrl", "ko"):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(G / f"GSE158684_{arm}_filtered_features.tsv.gz", "rt")]
    nb = sum(1 for _ in gzip.open(G / f"GSE158684_{arm}_filtered_barcodes.tsv.gz", "rt"))
    sym2row = {}
    for i, fr in enumerate(feats):
        sym2row.setdefault(fr[1] if len(fr) > 1 else fr[0], i + 1)
    sym2row["Ccn2"] = sym2row.get("Ccn2") or sym2row.get("Ctgf")
    inv = {sym2row[s]: s for s in MARK if sym2row.get(s)}
    tot = np.zeros(nb + 1)
    cnt = {s: np.zeros(nb + 1) for s in inv.values()}
    f = gzip.open(G / f"GSE158684_{arm}_filtered_matrix.mtx.gz", "rt")
    for l in f:
        if l[0] != "%":
            break
    for l in f:
        a = l.split()
        g, b, v = int(a[0]), int(a[1]), float(a[2])
        tot[b] += v
        if g in inv:
            cnt[inv[g]][b] += v
    nuc_detail[arm] = (nb, tot, cnt)
    for s, c in cnt.items():
        sn.append(dict(arm=arm, gene=s, class_=MARK[s], nuclei=nb, umi=int(c.sum()), nuclei_detected=int((c > 0).sum()), frac_nuclei_detected=round((c > 0).sum() / nb, 4),
                       pseudobulk_cpm=round(c.sum() / tot.sum() * 1e6, 2), total_umi=int(tot.sum())))
# does the Ccn2 signal sit in nuclei carrying endothelial markers?  (descriptive overlap; not a cell-type assignment)
for arm, (nb, tot, cnt) in nuc_detail.items():
    endo = (cnt.get("Cldn5", 0) + cnt.get("Flt1", 0) + cnt.get("Pecam1", 0)) > 0
    astro = (cnt.get("Aqp4", 0) + cnt.get("Gfap", 0) + cnt.get("Slc1a3", 0)) > 0
    pos = cnt["Ccn2"] > 0
    sn.append(dict(arm=arm, gene="OVERLAP", class_="Ccn2+ nuclei carrying >=1 UMI of endothelial markers (Cldn5/Flt1/Pecam1) | of astro markers (Aqp4/Gfap/Slc1a3) | of neither",
                   nuclei=nb, umi=int(cnt["Ccn2"].sum()), nuclei_detected=int(pos[1:].sum()),
                   frac_nuclei_detected=f"{int((pos & endo)[1:].sum())}|{int((pos & astro)[1:].sum())}|{int((pos & ~endo & ~astro)[1:].sum())}",
                   pseudobulk_cpm="", total_umi=int(tot.sum())))
    nonendo = ~endo
    sn.append(dict(arm=arm, gene="Ccn2_in_nuclei_without_endothelial_marker_UMI", class_="pseudobulk over nuclei with 0 UMI of Cldn5/Flt1/Pecam1", nuclei=int(nonendo[1:].sum()),
                   umi=int(cnt["Ccn2"][nonendo].sum()), nuclei_detected=int((pos & nonendo)[1:].sum()), frac_nuclei_detected="",
                   pseudobulk_cpm=round(cnt["Ccn2"][nonendo].sum() / tot[nonendo].sum() * 1e6, 2), total_umi=int(tot[nonendo].sum())))
with open(OUT / "snrna_ccn2.tsv", "w", encoding="utf-8") as f:
    c = list(sn[0]); f.write("\t".join(c) + "\n")
    for r in sn:
        f.write("\t".join(str(r[k]) for k in c) + "\n")

# ---- 5. cell-type origin: GSE73721 purified human and mouse cell-type RNA-seq (FPKM), gene row Ctgf
f = gzip.open(FILES / "geo/GSE73721/GSE73721_Human_and_mouse_table.csv.gz", "rt", encoding="latin-1")
rd = csv.reader(f)
hdr = next(rd)
row = next(r for r in rd if r and r[0].upper() in ("CTGF", "CCN2"))
groups = {}
for n, v in zip(hdr[1:], row[1:]):
    n = n.strip()
    if "tumor" in n:
        g = "human astrocyte, tumour"
    elif n.startswith("Fetal") and "astro" in n:
        g = "human astrocyte, fetal"
    elif n.startswith("Mouse"):
        g = "mouse astrocyte, 1-9 months"
    elif "astro" in n:
        g = "human astrocyte, postnatal non-tumour"
    elif "oligo" in n:
        g = "human oligodendrocyte"
    elif "myeloid" in n:
        g = "human myeloid"
    elif "endo" in n:
        g = "human endothelium"
    elif "neuron" in n:
        g = "human neuron (one sample)"
    elif "whole cortex" in n:
        g = "human whole cortex"
    else:
        g = "other"
    groups.setdefault(g, []).append(float(v))
with open(OUT / "celltype_origin.tsv", "w", encoding="utf-8") as f:
    f.write("group\tn_samples\tmin_fpkm\tmedian_fpkm\tmax_fpkm\n")
    for g, v in groups.items():
        f.write(f"{g}\t{len(v)}\t{min(v)}\t{statistics.median(v)}\t{max(v)}\n")
# ---- 6. human NSC shWWOX CAGE (GSE126075): one library per arm, TPM as deposited
f = gzip.open(FILES / "geo/GSE126075/GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz", "rt")
ch = f.readline().rstrip("\n").split("\t")
crow = next(l.rstrip("\n").split("\t") for l in f if l.split("\t", 1)[0] in ("CTGF", "CCN2"))
cv = dict(zip(ch[1:], map(float, crow[1:])))
with open(OUT / "cage_ctgf.tsv", "w", encoding="utf-8") as g:
    g.write("cell_state\tcontrol_tpm\tshWWOX_tpm\tratio\tnote\n")
    g.write(f"progenitors_hNSC\t{cv['hNSC']}\t{cv['hNSC_WWOX_del']}\t{cv['hNSC_WWOX_del']/cv['hNSC']:.2f}\tthe deposit's own WWOX control failed in progenitors (IT24 README row O6); one library per arm\n")
    g.write(f"neurons_d14\t{cv['Neurons']}\t{cv['Neurons_WWOX_del']}\t{cv['Neurons_WWOX_del']/cv['Neurons']:.2f}\tsub-2 TPM, one library per arm, direction depends on normalisation (verifier read tag counts 26 v 58 with median shifts +0.19 and -1.43)\n")
print(open(OUT / "cage_ctgf.tsv").read())
print(open(OUT / "mouse_bulk_ccn2.tsv").read())
print(open(OUT / "p47t_ccn2.tsv").read())
print(open(OUT / "snrna_ccn2.tsv").read())
print(open(OUT / "celltype_origin.tsv").read())
print(json.dumps(ident, indent=1))
