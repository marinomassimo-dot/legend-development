#!/usr/bin/env python3
"""ROUND 2 arm B: held-data lookups for IT's five arm-B hypotheses (H-C1 to H-C5). Held files only; no network.

    python3 armb_pretests.py --help
    python3 armb_pretests.py run <repo_root> <files_dir> <xlrd_dir> <out_dir>

<repo_root>  checkout holding the committed mouse DE and P47T tables (wwox_data_it24_p4_20261104/results)
<files_dir>  the shared gitignored files/ directory (geo/GSE158684, geo/GSE156243, geo/GSE52564_raw)
<xlrd_dir>   directory holding the xlrd package
Writes snrna_armb.tsv (one pool per arm; classes: all, neuron-like, excitatory-like, interneuron-like, astrocyte-like nuclei), bulk_armb.tsv,
organoid_armb.tsv and class_armb.tsv. Descriptive only: one snRNA pool per arm; neuron-deletion rows are the |cLFC|>=0.585 file only; P47T 5 v 5;
organoid 4 KO v 2 WT. Transcript is not function. Not medical advice; nothing here is WWOX evidence about a patient.
"""
import sys
if len(sys.argv) != 6 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, glob, gzip, os, re
from pathlib import Path
import numpy as np
REPO, FILES, XLRD, OUT = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4], Path(sys.argv[5])
OUT.mkdir(parents=True, exist_ok=True)
RES = REPO / "disease-models/wwox/research/drug_repurposing/wwox_data_it24_p4_20261104/results"
HC1 = ["Grin1", "Grin2a", "Grin2b", "Grin3a", "Srr", "Dao", "Slc6a9", "Slc6a11", "Slc1a4", "Slc7a10", "Gcat", "Pdxp", "Dldh", "Grid1", "Grid2"]
HC2 = ["Scn1a", "Scn2a", "Scn3a", "Scn8a", "Scn9a", "Scn1b", "Scn2b", "Scn3b", "Scn4b", "Fgf14", "Fgf13", "Ank3", "Cacna1h"]
HC3 = ["Adk", "Adora1", "Adora2a", "Adora2b", "Adora3", "Kcnj3", "Kcnj6", "Kcnj9", "Kcnj2", "Entpd1", "Nt5e", "Ada", "Slc29a1", "Slc28a3", "Gfap", "Aqp4"]
HC5 = ["Erbb4", "Erbb2", "Erbb3", "Egfr", "Nrg1", "Nrg2", "Nrg3", "Nrg4", "Pvalb", "Gad1", "Gad2", "Sst", "Vip", "Wwox"]
MARK = ["Snap25", "Slc17a7", "Aqp4", "Slc1a3"]
want = list(dict.fromkeys(HC1 + HC2 + HC3 + HC5 + MARK))
G = FILES / "geo/GSE158684"
rows = []
for arm in ("ctrl", "ko"):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(G / f"GSE158684_{arm}_filtered_features.tsv.gz", "rt")]
    nb = sum(1 for _ in gzip.open(G / f"GSE158684_{arm}_filtered_barcodes.tsv.gz", "rt"))
    s2r = {}
    for i, fr in enumerate(feats):
        s2r.setdefault(fr[1] if len(fr) > 1 else fr[0], i + 1)
    inv = {s2r[s]: s for s in want if s in s2r}
    tot = np.zeros(nb + 1); cnt = {s: np.zeros(nb + 1) for s in inv.values()}
    f = gzip.open(G / f"GSE158684_{arm}_filtered_matrix.mtx.gz", "rt")
    for l in f:
        if l[0] != "%": break
    for l in f:
        a = l.split(); g, b, v = int(a[0]), int(a[1]), float(a[2]); tot[b] += v
        if g in inv: cnt[inv[g]][b] += v
    neu = cnt["Snap25"] > 0; neu[0] = False
    exc = neu & (cnt["Slc17a7"] > 0)
    inh = neu & ((cnt["Gad1"] + cnt["Gad2"]) > 0)
    ast = ((cnt["Aqp4"] + cnt["Slc1a3"] + cnt["Gfap"]) > 0) & ~neu; ast[0] = False
    allm = np.ones(nb + 1, bool); allm[0] = False
    sets = {"all nuclei": allm, "neuron-like (Snap25)": neu, "excitatory-like": exc, "interneuron-like (Gad1/Gad2)": inh, "astrocyte-like": ast}
    for s in want:
        if s not in cnt:
            rows.append((arm, "not in matrix", 0, s, "", "")); continue
        for nm, m in sets.items():
            rows.append((arm, nm, int(m.sum()), s, round(cnt[s][m].sum() / tot[m].sum() * 1e6, 2), round((cnt[s][m] > 0).mean(), 4)))
with open(OUT / "snrna_armb.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["arm", "nuclei_set", "n_nuclei", "gene", "CPM", "frac_detected"]); w.writerows(rows)
de = list(csv.DictReader(open(RES / "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t"))
f = gzip.open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rt"); h = f.readline().rstrip("\n").split("\t"); P47 = {}
for l in f:
    r = dict(zip(h, l.rstrip("\n").split("\t"))); P47[(r["symbol"], r["region"])] = r
bl = []
for hyp, gl in (("H-C1", HC1), ("H-C2", HC2), ("H-C3", HC3), ("H-C5", HC5)):
    for g in gl:
        hits = [r for r in de if r["symbol"] == g]
        if not hits: bl.append((hyp, g, "neuron-deletion", "not among |cLFC|>=0.585 rows", ""))
        for r in hits:
            bl.append((hyp, g, "neuron-deletion " + r["contrast"], r["direction"], f"KO {r['mean_TPM_KO']} v control {r['mean_TPM_control']} TPM; cLFC {r['centred_log2_ratio']}; n {r['n_KO']} v {r['n_control']}"))
        for rg in ("CTX", "HPC", "PFC", "CB"):
            r = P47.get((g, rg))
            if r: bl.append((hyp, g, "P47T " + rg, "up" if float(r["log2FC_centred"]) > 0 else "down", f"WT {float(r['mean_norm_count_WT']):.0f}; log2FC {float(r['log2FC_centred']):.2f}; FDR(no sex) {float(r['FDR_no_sex']):.2g}; n {r['n_WT']} v {r['n_P47T']}"))
with open(OUT / "bulk_armb.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["hypothesis", "gene", "table", "direction", "values"]); w.writerows(bl)
cnts = {}
for l in gzip.open(FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt"):
    a = l.rstrip("\n").split("\t")
    if a[0] == "gene": cols = a[1:]; continue
    cnts[a[0].upper()] = np.array(a[1:], float)
lib = np.array(list(cnts.values())).sum(axis=0)
ko = [cols.index(c) for c in cols if c.startswith("cko")]; wt = [cols.index(c) for c in cols if c.startswith("cwt")]
og = []
for g in HC1 + HC2 + HC3 + HC5:
    if g.upper() in cnts:
        c = cnts[g.upper()] / lib * 1e6
        og.append((g, round(float(np.log2((c[ko].mean() + 1) / (c[wt].mean() + 1))), 3), round(float(c[ko].mean()), 1), round(float(c[wt].mean()), 1)))
with open(OUT / "organoid_armb.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "log2FC_KO_v_WT", "KO_mean_CPM", "WT_mean_CPM"]); w.writerows(og)
sys.path.insert(0, XLRD)
import xlrd
CL = {"Astrocyte": "astrocyte", "Neuron": "neuron", "OPC": "OPC", "NFO": "NFO", "MO": "myelinating oligodendrocyte", "Microglia": "microglia", "Endothelial": "endothelial"}
acc = {}
for fn in sorted(glob.glob(str(FILES / "geo/GSE52564_raw/*.xls.gz"))):
    cls = re.sub(r"\d+$", "", re.sub(r"^GSM\d+_", "", os.path.basename(fn)[:-7]))
    if cls not in CL: continue
    s = xlrd.open_workbook(file_contents=gzip.open(fn).read()).sheet_by_index(0)
    names = {str(s.cell_value(r, 0)).strip().upper(): r for r in range(s.nrows)}
    for g in HC1 + HC2 + HC3 + HC5:
        if g.upper() in names: acc.setdefault(g, {}).setdefault(cls, []).append(float(s.cell_value(names[g.upper()], 1)))
with open(OUT / "class_armb.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["gene"] + [CL[c] for c in CL])
    for g, d in acc.items(): w.writerow([g] + [round(sum(d[c]) / len(d[c]), 2) if c in d else "" for c in CL])
print("done")
