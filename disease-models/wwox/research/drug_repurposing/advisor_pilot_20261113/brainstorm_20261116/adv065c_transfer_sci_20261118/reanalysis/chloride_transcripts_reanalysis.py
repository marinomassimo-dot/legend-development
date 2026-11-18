"""Descriptive reanalysis of SLC12A5 and SLC12A2 transcripts in two held Wwox-deficient neural datasets (GSE156243 organoids, GSE158684 nuclei).

Held files only; no network. Usage:

    python3 chloride_transcripts_reanalysis.py run <files_dir> <out_dir>

No p-value across genotypes is computed: GSE156243 is six organoid libraries from one parental line and GSE158684 is one library per arm.
The plan, frozen before the run, is PLAN_FROZEN_BEFORE_RUN.md in this folder.
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv
import gzip
import math
from pathlib import Path

import numpy as np

FILES, OUT = Path(sys.argv[2]), Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)


def tsv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


# ---------------------------------------------------------------- organoids
cnt, cols = {}, None
for line in gzip.open(FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt"):
    a = line.rstrip("\n").split("\t")
    if a[0] == "gene":
        cols = a[1:]
        continue
    cnt[a[0].upper()] = np.array(a[1:], float)
lib = np.array(list(cnt.values())).sum(axis=0)
cpm = {g: v / lib * 1e6 for g, v in cnt.items()}
NEU = ["MAP2", "RBFOX3", "SYT1", "SNAP25", "STMN2", "TUBB3", "NEFL"]
PROG = ["SOX2", "VIM", "NES", "GFAP", "AQP4"]


def gmean(genes, i):
    return math.exp(np.mean([math.log(cpm[g][i] + 1.0) for g in genes if g in cpm]))


rows = []
for i, c in enumerate(cols):
    k5, k2 = cpm["SLC12A5"][i], cpm["SLC12A2"][i]
    ni, pi = gmean(NEU, i), gmean(PROG, i)
    rows.append([c, "KO" if c.startswith("cko") else "WT", int(lib[i]), round(k5, 1), round(k2, 1), round(k2 / k5, 3),
                 round(ni, 1), round(pi, 1), round(k5 / ni, 3), round(k2 / ni, 3), round(k2 / pi, 3), round(cpm["WWOX"][i], 2)])
tsv(OUT / "organoid_per_library.tsv",
    ["library", "genotype", "total_counts", "SLC12A5_CPM", "SLC12A2_CPM", "ratio_A2_over_A5", "neuronal_panel_gmean_CPM",
     "progenitor_glia_panel_gmean_CPM", "A5_over_neuronal", "A2_over_neuronal", "A2_over_progenitor_glia", "WWOX_CPM"], rows)
ko = [r for r in rows if r[1] == "KO"]
wt = [r for r in rows if r[1] == "WT"]
summ = []
for name, j in (("SLC12A5_CPM", 3), ("SLC12A2_CPM", 4), ("ratio_A2_over_A5", 5), ("neuronal_panel", 6), ("A5_over_neuronal", 8),
                ("A2_over_neuronal", 9), ("A2_over_progenitor_glia", 10)):
    kv, wv = [r[j] for r in ko], [r[j] for r in wt]
    overlap = "overlap" if (min(kv) <= max(wv) and min(wv) <= max(kv)) else "separated"
    summ.append([name, round(float(np.mean(kv)), 3), round(float(np.mean(wv)), 3), round(math.log2((np.mean(kv) + 1e-9) / (np.mean(wv) + 1e-9)), 3),
                 round(min(kv), 3), round(max(kv), 3), round(min(wv), 3), round(max(wv), 3), overlap])
tsv(OUT / "organoid_summary.tsv",
    ["metric", "KO_mean", "WT_mean", "log2_KO_over_WT", "KO_min", "KO_max", "WT_min", "WT_max", "ranges"], summ)

# ------------------------------------------------------------------- nuclei
MARK = {
    "exc": ["Slc17a7", "Camk2a", "Neurod6", "Satb2", "Slc17a6", "Prox1"],
    "inh": ["Gad1", "Gad2", "Slc32a1", "Pvalb", "Sst", "Vip", "Lhx6"],
    "astro": ["Aqp4", "Gja1", "Slc1a2", "Slc1a3", "Aldh1l1", "Gfap"],
    "oligo": ["Mbp", "Plp1", "Mog", "Mobp", "Mag"],
    "micro": ["Csf1r", "Cx3cr1", "P2ry12", "Tmem119", "C1qa"],
    "opc": ["Pdgfra", "Cspg4"],
}
CLASSES = list(MARK) + ["unassigned"]
TARGET = ["Slc12a5", "Slc12a2", "Slc12a7", "Slc12a6", "Wwox", "Snap25"]
G = FILES / "geo/GSE158684"
res = {}
for arm in ("ctrl", "ko"):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(G / f"GSE158684_{arm}_filtered_features.tsv.gz", "rt")]
    nb = sum(1 for _ in gzip.open(G / f"GSE158684_{arm}_filtered_barcodes.tsv.gz", "rt"))
    sym = {}
    for i, fr in enumerate(feats):
        sym.setdefault(fr[1] if len(fr) > 1 else fr[0], i + 1)
    role = {}
    for cl, gl in MARK.items():
        for g in gl:
            if g in sym:
                role[sym[g]] = ("m", cl)
    for g in TARGET:
        if g in sym:
            role.setdefault(sym[g], ("t", g))
    tgt_idx = {sym[g]: g for g in TARGET if g in sym}
    mark_cl = {sym[g]: cl for cl, gl in MARK.items() for g in gl if g in sym}
    tot = np.zeros(nb + 1)
    sc = {cl: np.zeros(nb + 1) for cl in MARK}
    tc = {g: np.zeros(nb + 1) for g in TARGET}
    f = gzip.open(G / f"GSE158684_{arm}_filtered_matrix.mtx.gz", "rt")
    for l in f:
        if l[0] != "%":
            break
    for l in f:
        a = l.split()
        gi, b, v = int(a[0]), int(a[1]), float(a[2])
        tot[b] += v
        if gi in mark_cl:
            sc[mark_cl[gi]][b] += v
        if gi in tgt_idx:
            tc[tgt_idx[gi]][b] += v
    tot[0] = 0
    keep = tot > 0
    M = np.vstack([sc[cl] / np.where(tot > 0, tot, 1) for cl in MARK])
    best = M.argmax(axis=0)
    has = M.max(axis=0) > 0
    cls = np.where(has, best, len(MARK))
    cls = np.where(keep, cls, -1)
    res[arm] = dict(n=int(keep.sum()), tot=tot, tc=tc, cls=cls, nb=nb)

comp_rows, gene_rows = [], []
cpm_cls = {}
for arm in ("ctrl", "ko"):
    r = res[arm]
    for ci, cn in enumerate(CLASSES):
        m = r["cls"] == ci
        n = int(m.sum())
        comp_rows.append([arm, cn, n, round(n / r["n"], 4)])
        for g in ("Slc12a5", "Slc12a2", "Slc12a7", "Slc12a6", "Wwox"):
            den = r["tot"][m].sum()
            c = r["tc"][g][m].sum() / den * 1e6 if den > 0 else float("nan")
            det = float((r["tc"][g][m] > 0).mean()) if n else float("nan")
            cpm_cls[(arm, cn, g)] = c
            gene_rows.append([arm, cn, g, n, round(c, 2), round(det, 4)])
    keepm = r["cls"] >= 0
    for g in ("Slc12a5", "Slc12a2", "Slc12a7", "Slc12a6", "Wwox"):
        c = r["tc"][g][keepm].sum() / r["tot"][keepm].sum() * 1e6
        cpm_cls[(arm, "ALL", g)] = c
        gene_rows.append([arm, "ALL", g, r["n"], round(c, 2), round(float((r["tc"][g][keepm] > 0).mean()), 4)])
tsv(OUT / "nuclei_composition.tsv", ["arm", "class", "n_nuclei", "fraction"], comp_rows)
tsv(OUT / "nuclei_gene_by_class.tsv", ["arm", "class", "gene", "n_nuclei", "CPM", "frac_nuclei_detected"], gene_rows)

wC = {cn: [x for x in comp_rows if x[0] == "ctrl" and x[1] == cn][0][3] for cn in CLASSES}
wK = {cn: [x for x in comp_rows if x[0] == "ko" and x[1] == cn][0][3] for cn in CLASSES}
dec = []
for g in ("Slc12a5", "Slc12a2"):
    # all-nuclei CPM is a UMI-weighted mean of class CPMs, weights proportional to nuclei x total UMI of the class
    def weights(arm):
        r = res[arm]
        wt_ = {}
        for ci, cn in enumerate(CLASSES):
            wt_[cn] = float(r["tot"][r["cls"] == ci].sum())
        s = sum(wt_.values())
        return {k: v / s for k, v in wt_.items()}
    uc, uk = weights("ctrl"), weights("ko")
    obs_c = sum(uc[cn] * cpm_cls[("ctrl", cn, g)] for cn in CLASSES if uc[cn] > 0 and not math.isnan(cpm_cls[("ctrl", cn, g)]))
    obs_k = sum(uk[cn] * cpm_cls[("ko", cn, g)] for cn in CLASSES if uk[cn] > 0 and not math.isnan(cpm_cls[("ko", cn, g)]))
    cf = sum(uk[cn] * cpm_cls[("ctrl", cn, g)] for cn in CLASSES if uk[cn] > 0 and not math.isnan(cpm_cls[("ctrl", cn, g)]))
    d_obs, d_cf = math.log2(obs_k / obs_c), math.log2(cf / obs_c)
    share = d_cf / d_obs if abs(d_obs) > 1e-9 else float("nan")
    verdict = "composition-explained" if share >= 0.7 else ("within-class" if share < 0.3 else "mixed")
    dec.append([g, round(obs_c, 2), round(obs_k, 2), round(cf, 2), round(d_obs, 3), round(d_cf, 3), round(share, 3), verdict])
tsv(OUT / "nuclei_counterfactual_decomposition.tsv",
    ["gene", "ctrl_all_CPM", "ko_all_CPM", "counterfactual_ko_composition_ctrl_class_values_CPM", "log2_ko_over_ctrl_observed",
     "log2_counterfactual_over_ctrl", "share_explained_by_composition", "rule_verdict"], dec)

neu = []
for g in ("Slc12a5", "Slc12a2"):
    for cn in ("exc", "inh", "astro", "oligo", "micro", "opc"):
        c, k = cpm_cls[("ctrl", cn, g)], cpm_cls[("ko", cn, g)]
        neu.append([g, cn, round(c, 2), round(k, 2), round(math.log2((k + 1e-9) / (c + 1e-9)), 3) if c > 0 and k > 0 else "NA"])
tsv(OUT / "nuclei_per_class_log2.tsv", ["gene", "class", "ctrl_CPM", "ko_CPM", "log2_ko_over_ctrl_descriptive_one_pool_per_arm"], neu)
print("done")
