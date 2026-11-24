"""ADV-210 step 2: normalisation and marker-weighted composition checks for SLC23A2 (frozen in PREREG_ADV210_SCI_20261124.md).
Usage: python3 slc23a2_composition_adv210.py REPO FILES"""
import sys, gzip
from pathlib import Path
import numpy as np
repo, files = map(Path, sys.argv[1:3])
sys.path.insert(0, str(repo / "disease-models/wwox/research/drug_repurposing/continuous_compounds/creatine"))
from assess import MODELS, load_target, reference
PANELS = {"neuron": "Snap25 Syt1 Rbfox3 Slc17a7 Gad1", "astro": "Gfap Aqp4 Slc1a3 Aldh1l1 Gja1",
          "oligo": "Mbp Plp1 Mog Mag", "opc": "Pdgfra Cspg4", "micro": "Cx3cr1 P2ry12 Tmem119", "endo": "Pecam1 Cldn5"}
gene_map, _ = reference(files)
out = []
def emit(*a):
    line = "\t".join(str(x) for x in a); out.append(line); print(line)
emit("model", "item", "value")
for model, acc, wp, kp in MODELS:
    human = model == "human_organoid"
    src, = (files / "geo" / acc).glob("*count_table.txt.gz" if human else "*TPM_Table.txt.gz")
    genes = ["Slc23a2"] + [g for p in PANELS.values() for g in p.split()]
    sym = [g.upper() if human else g for g in genes]
    names, vals = load_target(src, sym, None if human else gene_map)
    wt = [i for i, n in enumerate(names) if n.startswith(wp)]; ko = [i for i, n in enumerate(names) if n.startswith(kp)]
    emit(model, "libraries_wt_ko", f"{[names[i] for i in wt]} | {[names[i] for i in ko]}")
    emit(model, "genes_found", f"{sorted(k for k in vals)}")
    if human:  # C1: library totals from the whole count table
        tot = None
        with gzip.open(src, "rt") as f:
            hdr = f.readline().rstrip("\n").split("\t"); tot = np.zeros(len(hdr) - 1)
            for line in f:
                tot += np.array(line.rstrip("\n").split("\t")[1:], dtype=float)
        tmap = dict(zip(hdr[1:], tot))
        scale = {n: 1e6 / tmap[n] for n in names}
        emit(model, "library_total_counts", {n: int(tmap[n]) for n in names})
        mat = {g: np.array([vals[g][i] * scale[names[i]] for i in range(len(names))]) for g in vals}  # CPM
        raw = vals
    else:
        mat = vals; raw = vals
    def delta(arr, omit=None):
        l = np.log2(1 + arr); return l[[i for i in ko if i != omit]].mean() - l[[i for i in wt if i != omit]].mean()
    s = "SLC23A2" if human else "Slc23a2"
    if human:
        emit(model, "SLC23A2_delta_rawcount_log2", round(delta(raw[s]), 4))
        # POST-HOC variant (added after the frozen CPM variant was seen; reason: log2(1+CPM) with CPM near 1 is damped by the pseudocount, so the scale differs from the TPM tables): counts scaled to a common 35 million depth, and the log2 ratio of group means
        c35 = np.array([raw[s][i] * 35e6 / tmap[names[i]] for i in range(len(names))])
        emit(model, "SLC23A2_delta_log2_commondepth35M_POSTHOC", round(delta(c35), 4))
        emit(model, "SLC23A2_log2_ratio_group_mean_commondepth35M_POSTHOC", round(float(np.log2(c35[ko].mean() / c35[wt].mean())), 4))
        emit(model, "SLC23A2_log2_ratio_group_mean_rawcount", round(float(np.log2(raw[s][ko].mean() / raw[s][wt].mean())), 4))
        emit(model, "SLC23A2_commondepth_counts_wt_ko", f"{[round(float(c35[i]),1) for i in wt]} | {[round(float(c35[i]),1) for i in ko]}")
    d0 = delta(mat[s]); lo = [delta(mat[s], i) for i in wt + ko]
    emit(model, "SLC23A2_delta_%s" % ("CPM_log2" if human else "TPM_log2"), round(d0, 4)); emit(model, "SLC23A2_leave_one_out_range", f"{min(lo):.4f} to {max(lo):.4f}")
    # C2 class scores
    scores = {}
    for c, p in PANELS.items():
        gs = [(g.upper() if human else g) for g in p.split() if (g.upper() if human else g) in mat]
        if gs: scores[c] = np.mean([np.log2(1 + mat[g]) for g in gs], axis=0)
        emit(model, f"panel_{c}_genes_used", len(gs))
    y = np.log2(1 + mat[s]); g_ind = np.array([1.0 if i in ko else 0.0 for i in range(len(names))]); use = wt + ko
    for c, sc in scores.items():
        shift = sc[ko].mean() - sc[wt].mean()
        r = np.corrcoef(sc[use], y[use])[0, 1] if np.std(sc[use]) > 0 and np.std(y[use]) > 0 else float("nan")
        X = np.column_stack([np.ones(len(use)), g_ind[use], sc[use]])
        beta = np.linalg.lstsq(X, y[use], rcond=None)[0]
        gc = np.corrcoef(sc[use], g_ind[use])[0, 1] if np.std(sc[use]) > 0 else float("nan")
        emit(model, f"POSTHOC_class_{c}_levels", f"mean_score_WT={sc[wt].mean():.2f}; mean_score_KO={sc[ko].mean():.2f}; r_with_genotype={gc:.2f}")
        emit(model, f"class_{c}", f"score_shift_KO_minus_WT={shift:.3f}; r_with_SLC23A2={r:.3f}; adjusted_genotype_delta={beta[1]:.3f}; ratio_adj_to_unadj={beta[1]/d0:.2f}")
Path(sys.argv[0]).with_name("slc23a2_composition_adv210.tsv").write_text("\n".join(out) + "\n")
