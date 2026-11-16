#!/usr/bin/env python3
"""PRESIDIO-015: held-data lookups for the five ADV leap hypotheses (H-ADV-1 to H-ADV-5). Reads only files already held. No network.

    python3 adv_pretests.py --help
    python3 adv_pretests.py run <repo_root> <files_dir> <xlrd_dir> <out_dir>

<repo_root>  checkout holding the committed mouse DE and P47T tables (wwox_data_it24_p4_20261104/results)
<files_dir>  the shared gitignored files/ directory (geo/GSE158684, geo/GSE156243, geo/GSE52564_raw)
<xlrd_dir>   directory holding the xlrd package (python -I hides the user site; GSE52564 is legacy Excel)
Writes snrna_genes.tsv, snrna_composition.tsv, bulk_lookup.tsv, mtorc1_panel.tsv, organoid_markers.tsv, class_localisation.tsv into <out_dir>.
Needs numpy. Descriptive only: single-nucleus pools are ONE pool per arm, bulk contrasts have 2 to 4 samples per arm, the organoid
contrast is 4 knockout against 2 wild-type libraries. The mTORC1 panel is my own declared list, NOT the MSigDB hallmark.
Not medical advice; nothing here is WWOX evidence about a patient.
"""
import sys

if len(sys.argv) != 6 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv, glob, gzip, os, random, re, statistics
from pathlib import Path
import numpy as np

REPO, FILES, XLRD, OUT = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4], Path(sys.argv[5])
OUT.mkdir(parents=True, exist_ok=True)
RES = REPO / "disease-models/wwox/research/drug_repurposing/wwox_data_it24_p4_20261104/results"

H1 = ["Erbb4", "Nrg1", "Nrg2", "Nrg3", "Pvalb", "Gad1", "Gad2", "Slc32a1", "Sst", "Vip", "Lamp5", "Npy", "Cck", "Snap25", "Slc17a7", "Wwox"]
H3 = ["Plp1", "Mbp", "Mobp", "Mog", "Mag", "Cnp", "Olig1", "Olig2", "Sox10", "Pdgfra", "Enpp6", "Cldn11", "Cntnap1", "Cntnap2", "Nfasc"]
H2 = ["Hk1", "Hk2", "Gpi1", "Pfkm", "Pfkl", "Pgk1", "Pkm", "Ldha", "Ldhb", "Slc2a1", "Slc2a3", "Slc16a1", "Slc16a7", "Slc16a3", "Bdh1", "Oxct1",
      "Acat1", "Hmgcs2", "Pdk1", "Pdk2", "Pdk3", "Pdk4", "Pdha1", "Kcnj11", "Abcc8", "Abcc9", "Cpt1a"]
MT = ["Eif4ebp1", "Srebf1", "Hmgcs1", "Hmgcr", "Insig1", "Ldlr", "Fasn", "Acly", "Slc7a5", "Slc3a2", "Cad", "Ppat", "Gart", "Mthfd2", "Shmt2",
      "Pgk1", "Ldha", "Tpi1", "Hk2", "Gpi1", "Eif4a1", "Eef1a1", "Rps6", "Rpl13a", "Rpl3"]
PROG = ["Nes", "Sox2", "Pax6", "Mki67", "Top2a", "Vim", "Hes1"]
NEUR = ["Map2", "Rbfox3", "Syt1", "Snap25", "Dcx", "Stmn2", "Tubb3"]

# ---------------- 1. single-nucleus pools (GSE158684), one pool per arm
G = FILES / "geo/GSE158684"
want = list(dict.fromkeys(H1 + H3 + H2 + MT + PROG + NEUR))
snrows, comp = [], []
sub = {}
for arm in ("ctrl", "ko"):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(G / f"GSE158684_{arm}_filtered_features.tsv.gz", "rt")]
    nb = sum(1 for _ in gzip.open(G / f"GSE158684_{arm}_filtered_barcodes.tsv.gz", "rt"))
    sym2row = {}
    for i, fr in enumerate(feats):
        sym2row.setdefault(fr[1] if len(fr) > 1 else fr[0], i + 1)
    ribo = {i + 1 for i, fr in enumerate(feats) if re.match(r"^(Rps|Rpl)\d", fr[1] if len(fr) > 1 else fr[0])}
    inv = {sym2row[s]: s for s in want if s in sym2row}
    tot = np.zeros(nb + 1); rib = np.zeros(nb + 1)
    cnt = {s: np.zeros(nb + 1) for s in inv.values()}
    f = gzip.open(G / f"GSE158684_{arm}_filtered_matrix.mtx.gz", "rt")
    for l in f:
        if l[0] != "%":
            break
    for l in f:
        a = l.split(); g, b, v = int(a[0]), int(a[1]), float(a[2])
        tot[b] += v
        if g in ribo:
            rib[b] += v
        if g in inv:
            cnt[inv[g]][b] += v
    sub[arm] = (nb, tot, cnt)
    for s in want:
        if s not in cnt:
            snrows.append((arm, s, nb, "not in matrix", "", "", ""))
            continue
        c = cnt[s]
        snrows.append((arm, s, nb, int(c.sum()), int((c > 0).sum()), round((c > 0).sum() / nb, 4), round(c.sum() / tot.sum() * 1e6, 2)))
    comp.append((arm, "ribosomal-protein UMI share (Rps/Rpl) of all UMI", nb, round(rib.sum() / tot.sum(), 4), "", ""))
    inter = ((cnt["Gad1"] + cnt["Gad2"] + cnt["Slc32a1"]) > 0) & (cnt["Snap25"] > 0)
    oligo = ((cnt["Mobp"] + cnt["Mog"] + cnt["Mag"]) > 0)
    prog = ((cnt["Nes"] + cnt["Sox2"] + cnt["Mki67"] + cnt["Top2a"]) > 0)
    for name, m, genes in (("interneuron-like nuclei (>=1 UMI of Gad1/Gad2/Slc32a1 and Snap25)", inter, ["Erbb4", "Pvalb", "Nrg1", "Sst", "Vip", "Npy", "Wwox"]),
                           ("mature-oligodendrocyte nuclei (>=1 UMI of Mobp/Mog/Mag)", oligo, ["Mbp", "Plp1", "Mobp", "Mog", "Cntnap1", "Wwox"]),
                           ("progenitor-like nuclei (>=1 UMI of Nes/Sox2/Mki67/Top2a)", prog, ["Nes", "Sox2", "Mki67", "Wwox"])):
        mm = m.copy(); mm[0] = False
        comp.append((arm, name, nb, int(mm.sum()), round(mm.sum() / nb, 4), ""))
        for g in genes:
            c = cnt[g]
            comp.append((arm, f"  within {name.split(' (')[0]}: {g} CPM", int(mm.sum()), round(c[mm].sum() / tot[mm].sum() * 1e6, 2), round((c[mm] > 0).mean(), 4), ""))
with open(OUT / "snrna_genes.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["arm", "gene", "nuclei", "UMI", "nuclei_detected", "frac_nuclei_detected", "pseudobulk_CPM"]); w.writerows(snrows)
with open(OUT / "snrna_composition.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["arm", "quantity", "n_nuclei", "value", "frac_detected_or_share", "note"]); w.writerows(comp)

# ---------------- 2. bulk tables: neuron-deletion DE rows (|cLFC| >= 0.585 only) and P47T (all tested genes)
de = list(csv.DictReader(open(RES / "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t"))
f = gzip.open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rt"); h = f.readline().rstrip("\n").split("\t")
P47 = {}
for l in f:
    r = dict(zip(h, l.rstrip("\n").split("\t"))); P47[(r["symbol"], r["region"])] = r
bl = []
for hyp, gl in (("H-ADV-1", H1), ("H-ADV-3", H3), ("H-ADV-2", H2), ("H-ADV-4 panel", MT)):
    for g in gl:
        hits = [r for r in de if r["symbol"] == g]
        if not hits:
            bl.append((hyp, g, "neuron-deletion", "not among |cLFC|>=0.585 rows", "", ""))
        for r in hits:
            bl.append((hyp, g, "neuron-deletion " + r["contrast"], r["direction"], f"KO {r['mean_TPM_KO']} v control {r['mean_TPM_control']} TPM; cLFC {r['centred_log2_ratio']}; n {r['n_KO']} v {r['n_control']}",
                       "background-confounded" if r["BACKGROUND_CONFOUNDED"] == "1" else ""))
        for rg in ("CTX", "HPC", "PFC", "CB"):
            r = P47.get((g, rg))
            if r:
                bl.append((hyp, g, "P47T " + rg, "up" if float(r["log2FC_centred"]) > 0 else "down", f"WT {float(r['mean_norm_count_WT']):.0f}; log2FC {float(r['log2FC_centred']):.2f}; FDR(no sex) {float(r['FDR_no_sex']):.2g}; n {r['n_WT']} v {r['n_P47T']}", ""))
with open(OUT / "bulk_lookup.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["hypothesis", "gene", "table", "direction", "values", "flag"]); w.writerows(bl)

# ---------------- 3. mTORC1 panel against random same-size gene sets, P47T (independent line) and organoids
rng = random.Random(20261116)
pr = []
for rg in ("CTX", "HPC", "PFC", "CB"):
    allg = {s: float(r["log2FC_centred"]) for (s, reg), r in P47.items() if reg == rg and float(r["mean_norm_count_WT"]) >= 50}
    panel = [allg[g] for g in MT if g in allg]
    ribo = [v for s, v in allg.items() if re.match(r"^(Rps|Rpl)\d", s)]
    pool = list(allg.values())
    def pval(vals):
        obs = statistics.median(vals); n = len(vals); c = 0
        for _ in range(5000):
            if abs(statistics.median(rng.sample(pool, n))) >= abs(obs):
                c += 1
        return obs, c / 5000
    o, p = pval(panel); ro, rp = pval(ribo)
    pr.append(("P47T " + rg, "declared panel (n=%d genes present)" % len(panel), round(o, 3), round(p, 4)))
    pr.append(("P47T " + rg, "Rps/Rpl ribosomal-protein genes (n=%d)" % len(ribo), round(ro, 3), round(rp, 4)))
cnts = {}
for l in gzip.open(FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt"):
    a = l.rstrip("\n").split("\t")
    if a[0] == "gene":
        cols = a[1:]; continue
    cnts[a[0].upper()] = np.array(a[1:], float)
mat = np.array(list(cnts.values())); lib = mat.sum(axis=0)
ko = [cols.index(c) for c in cols if c.startswith("cko")]; wt = [cols.index(c) for c in cols if c.startswith("cwt")]
cpm = {g: v / lib * 1e6 for g, v in cnts.items()}
lfc = {g: float(np.log2((c[ko].mean() + 1) / (c[wt].mean() + 1))) for g, c in cpm.items() if (c[ko].mean() + c[wt].mean()) / 2 >= 5}
pool = list(lfc.values())
def opval(vals):
    obs = statistics.median(vals); n = len(vals); c = 0
    for _ in range(5000):
        if abs(statistics.median(rng.sample(pool, n))) >= abs(obs):
            c += 1
    return obs, c / 5000
op = [lfc[g.upper()] for g in MT if g.upper() in lfc]
orb = [v for s, v in lfc.items() if re.match(r"^RP[SL]\d", s)]
for name, vals in (("declared panel (n=%d)" % len(op), op), ("RPS/RPL ribosomal-protein genes (n=%d)" % len(orb), orb)):
    o, p = opval(vals); pr.append(("organoid GSE156243 KO(4) v WT(2)", name, round(o, 3), round(p, 4)))
with open(OUT / "mtorc1_panel.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["table", "gene set", "median_log2FC", "empirical_p_vs_random_same_size_sets"]); w.writerows(pr)
om = []
for grp, gl in (("progenitor", PROG), ("neuronal maturation", NEUR)):
    for g in gl:
        if g.upper() in lfc:
            om.append((grp, g, round(lfc[g.upper()], 3), round(float(cpm[g.upper()][ko].mean()), 1), round(float(cpm[g.upper()][wt].mean()), 1)))
with open(OUT / "organoid_markers.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["group", "gene", "log2FC_KO_v_WT", "KO_mean_CPM", "WT_mean_CPM"]); w.writerows(om)

# ---------------- 4. where the genes live: GSE52564 purified classes (mean FPKM)
sys.path.insert(0, XLRD)
import xlrd
CL = {"Astrocyte": "astrocyte", "Neuron": "neuron", "OPC": "OPC", "NFO": "NFO", "MO": "myelinating oligodendrocyte", "Microglia": "microglia", "Endothelial": "endothelial"}
acc = {}
for fn in sorted(glob.glob(str(FILES / "geo/GSE52564_raw/*.xls.gz"))):
    cls = re.sub(r"\d+$", "", re.sub(r"^GSM\d+_", "", os.path.basename(fn)[:-7]))
    if cls not in CL:
        continue
    s = xlrd.open_workbook(file_contents=gzip.open(fn).read()).sheet_by_index(0)
    names = {str(s.cell_value(r, 0)).strip().upper(): r for r in range(s.nrows)}
    for g in ["Erbb4", "Nrg1", "Nrg3", "Pvalb", "Gad1", "Plp1", "Mbp", "Mobp", "Mog", "Cntnap1", "Hk1", "Hk2", "Slc16a1", "Slc16a7", "Bdh1", "Oxct1", "Kcnj11", "Abcc8", "Ldha", "Eif4ebp1"]:
        if g.upper() in names:
            acc.setdefault(g, {}).setdefault(cls, []).append(float(s.cell_value(names[g.upper()], 1)))
with open(OUT / "class_localisation.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["gene"] + [CL[c] for c in CL])
    for g, d in acc.items():
        w.writerow([g] + [round(sum(d[c]) / len(d[c]), 2) if c in d else "" for c in CL])
print("done:", sorted(p.name for p in OUT.iterdir()))
