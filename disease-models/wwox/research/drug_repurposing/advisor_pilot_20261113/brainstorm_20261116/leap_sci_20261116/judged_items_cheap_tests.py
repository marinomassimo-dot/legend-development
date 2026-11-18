#!/usr/bin/env python3
"""Held-data lookups for the judged items J04 (maturation axis), J08 (astrocyte K+ clearance) and J18 (excision fraction). Held files only; no network.

    python3 judged_items_cheap_tests.py run <repo_root> <files_dir> <out_dir>

Writes j04_organoid.tsv (GSE156243, 4 KO against 2 WT libraries; library-size normalised log2 fold change of a fixed gene list), j08_astro_nuclei.tsv
(GSE158684, one pool per arm, astrocyte-like nuclei) and j18_wwox_nuclei.tsv (fraction of nuclei with a Wwox UMI). Descriptive only.
"""
import sys
if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, os
from pathlib import Path
import numpy as np
REPO, FILES, OUT = Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]); OUT.mkdir(parents=True, exist_ok=True)
J04 = ["GRIN2B", "GRIN2A", "GRIN2C", "SLC12A2", "SLC12A5", "NES", "SOX2", "VIM", "MAP2", "SYT1", "SNAP25", "CCN2", "KCNK2", "KCNK3", "KCNK9"]
cnt = {}
for l in gzip.open(FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt"):
    a = l.rstrip("\n").split("\t")
    if a[0] == "gene":
        cols = a[1:]; continue
    cnt[a[0].upper()] = np.array(a[1:], float)
lib = np.array(list(cnt.values())).sum(axis=0)
ko = [i for i, c in enumerate(cols) if c.startswith("cko")]; wt = [i for i, c in enumerate(cols) if c.startswith("cwt")]
with open(OUT / "j04_organoid.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "log2FC_KO_v_WT", "KO_mean_CPM", "WT_mean_CPM"])
    for g in J04:
        if g in cnt:
            c = cnt[g] / lib * 1e6
            w.writerow([g, round(float(np.log2((c[ko].mean() + 1) / (c[wt].mean() + 1))), 3), round(float(c[ko].mean()), 1), round(float(c[wt].mean()), 1)])
G = FILES / "geo/GSE158684"
W = ["Kcnj10", "Slc1a2", "Slc1a3", "Atp1a2", "Aqp4", "Gja1", "Gfap", "Kcnk1", "Slc6a11", "Snap25", "Wwox", "Aldh1l1"]
rows, wrow = [], []
for arm in ("ctrl", "ko"):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(G / f"GSE158684_{arm}_filtered_features.tsv.gz", "rt")]
    nb = sum(1 for _ in gzip.open(G / f"GSE158684_{arm}_filtered_barcodes.tsv.gz", "rt"))
    sym = {}
    for i, fr in enumerate(feats):
        sym.setdefault(fr[1] if len(fr) > 1 else fr[0], i + 1)
    inv = {sym[g]: g for g in W if g in sym}
    tot = np.zeros(nb + 1); c = {g: np.zeros(nb + 1) for g in inv.values()}
    f = gzip.open(G / f"GSE158684_{arm}_filtered_matrix.mtx.gz", "rt")
    for l in f:
        if l[0] != "%": break
    for l in f:
        a = l.split(); gi, b, v = int(a[0]), int(a[1]), float(a[2]); tot[b] += v
        if gi in inv: c[inv[gi]][b] += v
    neu = c["Snap25"] > 0
    astro = ((c["Aqp4"] + c["Slc1a3"] + c["Gfap"]) > 0) & ~neu; astro[0] = False
    for g in ("Kcnj10", "Slc1a2", "Slc1a3", "Atp1a2", "Aqp4", "Gja1", "Gfap", "Slc6a11"):
        rows.append((arm, int(astro.sum()), g, round(c[g][astro].sum() / tot[astro].sum() * 1e6, 2), round((c[g][astro] > 0).mean(), 4)))
    for name, m in (("all nuclei", np.ones(nb + 1, bool)), ("neuron-like (Snap25)", neu), ("astrocyte-like", astro)):
        m = m.copy(); m[0] = False
        wrow.append((arm, name, int(m.sum()), round((c["Wwox"][m] > 0).mean(), 4), round(c["Wwox"][m].sum() / tot[m].sum() * 1e6, 2)))
with open(OUT / "j08_astro_nuclei.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["arm", "n_astrocyte_like_nuclei", "gene", "CPM", "frac_detected"]); w.writerows(rows)
with open(OUT / "j18_wwox_nuclei.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["arm", "nuclei_set", "n", "frac_with_Wwox_UMI", "Wwox_CPM"]); w.writerows(wrow)
print("done")
