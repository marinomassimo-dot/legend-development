#!/usr/bin/env python3
"""PRESIDIO-016 (SCI): held-data lookups for the four HE leap hypotheses (H-HE-1 to H-HE-4), read only from held files, no network.

    python3 he_pretests.py run <repo_root> <files_dir> <xlrd_dir> <out_dir>

Writes class_means.tsv (GSE52564 purified classes, mean FPKM, all replicates), snrna_classes.tsv (GSE158684 control pool, P17 hippocampus,
CPM by nucleus class), lincs_context.tsv (held LINCS family and signature scores for antiseizure compounds against the whole table).
Needs numpy and xlrd (give the directory that holds xlrd). Descriptive only; not WWOX evidence about a patient.
"""
import sys

if len(sys.argv) != 6 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv, glob, gzip, os, re, statistics
from pathlib import Path
import numpy as np

REPO, FILES, XLRD, OUT = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4], Path(sys.argv[5])
OUT.mkdir(parents=True, exist_ok=True)
GENES = ["Scn1a", "Scn2a", "Scn3a", "Scn8a", "Scn1b", "Scn2b", "Snap25", "Slc6a1", "Slc6a11", "Abat", "Nr3c1", "Gabrg2", "Gabra1", "Aqp4", "Slc1a3"]
sys.path.insert(0, XLRD)
import xlrd
CL = {"Astrocyte": "astrocyte P7", "Neuron": "neuron P7", "OPC": "OPC P17", "NFO": "NFO P17", "MO": "myelinating oligodendrocyte P17", "Microglia": "microglia", "Endothelial": "endothelial"}
acc = {}
for fn in sorted(glob.glob(str(FILES / "geo/GSE52564_raw/*.xls.gz"))):
    cls = re.sub(r"\d+$", "", re.sub(r"^GSM\d+_", "", os.path.basename(fn)[:-7]))
    if cls not in CL:
        continue
    s = xlrd.open_workbook(file_contents=gzip.open(fn).read()).sheet_by_index(0)
    names = {str(s.cell_value(r, 0)).strip().upper(): r for r in range(s.nrows)}
    for g in GENES:
        if g.upper() in names:
            acc.setdefault(g, {}).setdefault(cls, []).append(float(s.cell_value(names[g.upper()], 1)))
with open(OUT / "class_means.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["gene"] + [CL[c] for c in CL] + ["neuron/Snap25 ratio (P7)"])
    sn = statistics.mean(acc["Snap25"]["Neuron"]) if "Snap25" in acc else None
    for g, d in acc.items():
        vals = [round(statistics.mean(d[c]), 2) if c in d else "" for c in CL]
        ratio = round(statistics.mean(d["Neuron"]) / sn, 4) if sn and "Neuron" in d else ""
        w.writerow([g] + vals + [ratio])
G = FILES / "geo/GSE158684"
feats = [l.rstrip("\n").split("\t") for l in gzip.open(G / "GSE158684_ctrl_filtered_features.tsv.gz", "rt")]
nb = sum(1 for _ in gzip.open(G / "GSE158684_ctrl_filtered_barcodes.tsv.gz", "rt"))
sym = {}
for i, fr in enumerate(feats):
    sym.setdefault(fr[1] if len(fr) > 1 else fr[0], i + 1)
want = [g for g in GENES if g in sym] + ["Slc17a7", "Gad1", "Gad2", "Gfap"]
inv = {sym[g]: g for g in want if g in sym}
tot = np.zeros(nb + 1); cnt = {g: np.zeros(nb + 1) for g in inv.values()}
f = gzip.open(G / "GSE158684_ctrl_filtered_matrix.mtx.gz", "rt")
for l in f:
    if l[0] != "%":
        break
for l in f:
    a = l.split(); g, b, v = int(a[0]), int(a[1]), float(a[2]); tot[b] += v
    if g in inv:
        cnt[inv[g]][b] += v
neu = cnt["Snap25"] > 0
astro = ((cnt["Aqp4"] + cnt["Slc1a3"] + cnt["Gfap"]) > 0) & ~neu
rows = []
for name, m in (("neuron-like nuclei (Snap25 UMI > 0)", neu), ("astrocyte-like nuclei (Aqp4/Slc1a3/Gfap UMI > 0, no Snap25)", astro)):
    m = m.copy(); m[0] = False
    for g in want:
        rows.append((name, int(m.sum()), g, round(cnt[g][m].sum() / tot[m].sum() * 1e6, 2), round((cnt[g][m] > 0).mean(), 4)))
with open(OUT / "snrna_classes.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["nucleus class (control pool, P17 hippocampus)", "n_nuclei", "gene", "CPM", "frac_detected"]); w.writerows(rows)
R = REPO / "disease-models/wwox/research/drug_repurposing/network_comparison_it7_p3_20261029/results/"
sig = list(csv.DictReader(open(R / "signature_scores.tsv"), delimiter="\t"))
fam = list(csv.DictReader(open(R / "family_scores.tsv"), delimiter="\t"))
neuv = [float(r["opposition_score"]) for r in sig if r["cell_id"] == "NEU"]
out = [("all NEU signatures", len(neuv), "median", round(statistics.median(neuv), 3)),
       ("all NEU signatures", len(neuv), "share <= -1.05", round(sum(x <= -1.05 for x in neuv) / len(neuv), 3)),
       ("all NEU signatures", len(neuv), "share >= +1.05", round(sum(x >= 1.05 for x in neuv) / len(neuv), 3))]
AED = ["VALPROIC ACID", "CARBAMAZEPINE", "LAMOTRIGINE", "PHENYTOIN", "ETHOSUXIMIDE", "TOPIRAMATE", "LEVETIRACETAM", "VIGABATRIN", "CLOBAZAM", "DIAZEPAM", "PHENOBARBITAL", "ZONISAMIDE", "OXCARBAZEPINE", "LACOSAMIDE", "PERAMPANEL", "CANNABIDIOL", "TIAGABINE"]
for r in fam:
    if r["name"].upper() in AED:
        out.append((r["name"], "family", "O_E (neuron-like) / O_B_SIG (progenitor-like) / freq_hit_rate_SIG", f"{r['O_E']} / {r['O_B_SIG']} / {r['freq_hit_rate_SIG']}"))
o_e = sorted(float(r["O_E"]) for r in fam if r["O_E"] not in ("", "NA"))
out.append(("all families", len(o_e), "share with O_E <= -1.2768 (valproic acid)", round(sum(x <= -1.2768 for x in o_e) / len(o_e), 3)))
out.append(("all families", len(o_e), "median freq_hit_rate_SIG", round(statistics.median(float(r["freq_hit_rate_SIG"]) for r in fam if r["freq_hit_rate_SIG"] not in ("", "NA")), 3)))
with open(OUT / "lincs_context.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["item", "n", "quantity", "value"]); w.writerows(out)
print("done")
