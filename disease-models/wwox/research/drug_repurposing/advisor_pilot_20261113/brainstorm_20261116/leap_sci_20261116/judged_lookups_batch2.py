#!/usr/bin/env python3
"""Held-data lookups J04 (projection from the held maturation calibration set), J06, J17, J19. Held files only; no network.

    python3 judged_lookups_batch2.py run <repo_root> <files_dir> <out_dir>

Writes j04_projection.tsv, j06_j19_neuronlike_nuclei.tsv (GSE158684, one pool per arm), j17_npy_receptors.tsv (committed bulk tables).
J04: slopes of log2(CPM+1) against log2(differentiation day) within iPSC line in GSE150123 (WWOX-unperturbed spheroids), and the KO shift of
GSE156243 projected from the progenitor and neuronal markers by the same composite; observed against projected. Descriptive only.
"""
import sys
if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, importlib.util, math, statistics
from pathlib import Path
import numpy as np
REPO, FILES, OUT = Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]); OUT.mkdir(parents=True, exist_ok=True)
DR = REPO / "disease-models/wwox/research/drug_repurposing/"
# ---- J04
spec = importlib.util.spec_from_file_location("mc", DR / "gse156243/maturation_calibration.py")
mc = importlib.util.module_from_spec(spec); sys.argv = ["x"]; spec.loader.exec_module(mc)
s2e = mc.symbol_to_ensg()
TARGET = ["GRIN2B", "GRIN2A", "SLC12A2", "SLC12A5", "CCN2"]
MARK_P = ["NES", "VIM", "SOX2"]; MARK_N = ["MAP2", "SYT1", "SNAP25"]
want = {g: s2e[g] for g in TARGET + MARK_P + MARK_N if g in s2e}
meta, cnt = mc.calibration_matrix(want)
samples = [s for s in cnt if s in meta]
def val(s, g):
    c, lib = cnt[s]["genes"], cnt[s]["total"]
    return math.log2(c.get(g, 0) / lib * 1e6 + 1)
lines = [meta[s]["iPSc line"] for s in samples]; days = [math.log2(float(meta[s]["differentiation day"])) for s in samples]
def slope(g):
    y = [val(s, g) for s in samples]
    ym = {}; xm = {}
    for l in set(lines):
        idx = [i for i, ll in enumerate(lines) if ll == l]
        for i in idx: pass
        ym[l] = statistics.mean(y[i] for i in idx); xm[l] = statistics.mean(days[i] for i in idx)
    xs = [days[i] - xm[lines[i]] for i in range(len(samples))]; ys = [y[i] - ym[lines[i]] for i in range(len(samples))]
    den = sum(x * x for x in xs)
    return sum(x * y for x, y in zip(xs, ys)) / den if den else float("nan")
sl = {g: slope(g) for g in want}
# KO shift in GSE156243
ko = {}
for l in gzip.open(FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt"):
    a = l.rstrip("\n").split("\t")
    if a[0] == "gene": cols = a[1:]; continue
    ko[a[0].upper()] = np.array(a[1:], float)
lib = np.array(list(ko.values())).sum(axis=0)
ki = [i for i, c in enumerate(cols) if c.startswith("cko")]; wi = [i for i, c in enumerate(cols) if c.startswith("cwt")]
def kos(g):
    g = {"CCN2": "CTGF"}.get(g, g) if g not in ko else g  # the organoid table uses the older symbol
    c = ko[g] / lib * 1e6
    return math.log2((c[ki].mean() + 1) / (c[wi].mean() + 1))
# maturation shift in log2-day units, from markers whose calibration slope is clearly nonzero
d_est = [kos(g) / sl[g] for g in MARK_P + MARK_N if g in sl and abs(sl[g]) > 0.05]
dt = statistics.median(d_est) if d_est else float("nan")
with open(OUT / "j04_projection.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["gene", "calibration_slope_log2cpm_per_log2day", "observed_KO_log2FC", "projected_KO_log2FC", "role"])
    for g in MARK_P + MARK_N + TARGET:
        if g in sl:
            w.writerow([g, round(sl[g], 3), round(kos(g), 3), round(sl[g] * dt, 3), "marker" if g in MARK_P + MARK_N else "target"])
    w.writerow(["# composite maturation shift (median of marker KO/slope, log2-day units)", round(dt, 3), "", "", f"n markers {len(d_est)}"])
# ---- J06 and J19, J17 in the single-nucleus pool
G = FILES / "geo/GSE158684"
W = ["Fos", "Arc", "Npas4", "Egr1", "Slc12a5", "Slc12a2", "Snap25", "Npy", "Npy1r", "Npy2r", "Npy5r", "Slc17a7", "Gad1", "Gad2"]
rows = []
for arm in ("ctrl", "ko"):
    feats = [l.rstrip("\n").split("\t") for l in gzip.open(G / f"GSE158684_{arm}_filtered_features.tsv.gz", "rt")]
    nb = sum(1 for _ in gzip.open(G / f"GSE158684_{arm}_filtered_barcodes.tsv.gz", "rt"))
    sym = {}
    for i, fr in enumerate(feats): sym.setdefault(fr[1] if len(fr) > 1 else fr[0], i + 1)
    inv = {sym[g]: g for g in W if g in sym}
    tot = np.zeros(nb + 1); c = {g: np.zeros(nb + 1) for g in inv.values()}
    f = gzip.open(G / f"GSE158684_{arm}_filtered_matrix.mtx.gz", "rt")
    for l in f:
        if l[0] != "%": break
    for l in f:
        a = l.split(); gi, b, v = int(a[0]), int(a[1]), float(a[2]); tot[b] += v
        if gi in inv: c[inv[gi]][b] += v
    sets = {"neuron-like (Snap25)": c["Snap25"] > 0, "excitatory-like (Snap25 and Slc17a7)": (c["Snap25"] > 0) & (c["Slc17a7"] > 0),
            "interneuron-like (Snap25 and Gad1/Gad2)": (c["Snap25"] > 0) & ((c["Gad1"] + c["Gad2"]) > 0)}
    for name, m in sets.items():
        m = m.copy(); m[0] = False
        for g in ("Fos", "Arc", "Npas4", "Egr1", "Slc12a5", "Slc12a2", "Npy", "Npy1r", "Npy2r", "Npy5r"):
            if g in c:
                rows.append((arm, name, int(m.sum()), g, round(c[g][m].sum() / tot[m].sum() * 1e6, 2), round(float((c[g][m] > 0).mean()), 4)))
with open(OUT / "j06_j19_neuronlike_nuclei.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["arm", "nucleus_set", "n_nuclei", "gene", "CPM", "frac_detected"]); w.writerows(rows)
# ---- J17 committed bulk tables
RES = DR / "wwox_data_it24_p4_20261104/results/"
de = list(csv.DictReader(open(RES / "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t"))
f = gzip.open(RES / "p47t_all_regions_tested_genes.tsv.gz", "rt"); h = f.readline().rstrip("\n").split("\t"); P = {}
for l in f:
    r = dict(zip(h, l.rstrip("\n").split("\t"))); P[(r["symbol"], r["region"])] = r
with open(OUT / "j17_npy_receptors.tsv", "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "table", "values"])
    for g in ("Npy", "Npy1r", "Npy2r", "Npy5r", "Npy4r"):
        hits = [r for r in de if r["symbol"] == g]
        if not hits: w.writerow([g, "neuron-deletion", "not among |cLFC|>=0.585 rows"])
        for r in hits: w.writerow([g, "neuron-deletion " + r["contrast"], f"KO {r['mean_TPM_KO']} v control {r['mean_TPM_control']} TPM; cLFC {r['centred_log2_ratio']}"])
        for rg in ("CTX", "HPC", "PFC", "CB"):
            r = P.get((g, rg))
            if r: w.writerow([g, "P47T " + rg, f"log2FC {float(r['log2FC_centred']):.2f}; FDR {float(r['FDR_no_sex']):.2g}; WT {float(r['mean_norm_count_WT']):.0f}"])
print("done")
