#!/usr/bin/env python3
"""Candidate [4d]: per-class readout in a multi-sample single-nucleus series (GSE334405 cortex samples: PV-Cre Scn1a F/+ against +/+). Same marker-set classification as [4b]. Hypothesis level; numpy only; seeded.
    python3 snuc_multi.py --help
    python3 snuc_multi.py run <dir with <prefix>_{matrix.mtx,barcodes.tsv,features.tsv}.gz files> <samples.tsv: prefix<TAB>group (ctrl or mut)> <out_prefix>
Unit: the animal when each sample is one animal (per-animal pseudobulk, bootstrap over animals) and the nucleus (pooled, pseudo-replicated) beside it."""
import sys
if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import gzip
import numpy as np
D, SAMPLES, PFX = sys.argv[2], sys.argv[3], sys.argv[4]
SETS = {"excitatory": ["Slc17a7", "Slc17a6", "Camk2a"], "inhibitory": ["Gad1", "Gad2", "Slc32a1"], "astrocyte": ["Aqp4", "Gja1", "Slc1a2", "Aldh1l1"],
        "oligodendrocyte": ["Mbp", "Plp1", "Mog", "Mobp"], "microglia": ["Cx3cr1", "P2ry12", "Csf1r"]}
GENES = ["Gabrd", "Slc12a2", "Scn1a", "Gabrg2", "Wwox", "Slc12a5", "Grin2b", "Kcnk2", "Gabra5", "Cacna1i"]
WANT = sorted(set(sum(SETS.values(), [])) | set(GENES))
rng = np.random.default_rng(7)
def load(prefix):
    # streaming parse (memory-bounded): same quantities as the first version of this loader (library size per barcode, counts of the wanted genes)
    feats = [l.rstrip("\n").split("\t") for l in gzip.open("%s/%s_features.tsv.gz" % (D, prefix), "rt")]
    nb = sum(1 for _ in gzip.open("%s/%s_barcodes.tsv.gz" % (D, prefix), "rt")); sym = [f[1] for f in feats]
    idx = {s: k for k, s in enumerate(sym) if s in WANT}; want_rows = np.array(sorted(idx.values())); inv = {v: k for k, v in idx.items()}
    lib = np.zeros(nb); X = {s: np.zeros(nb) for s in idx}
    f = gzip.open("%s/%s_matrix.mtx.gz" % (D, prefix), "rb"); header_done = False; rest = b""
    while True:
        blk = f.read(1 << 26)
        if not blk and not rest: break
        buf = rest + blk
        if blk:
            cut = buf.rfind(b"\n"); rest = buf[cut + 1:]; buf = buf[:cut + 1]
        else:
            rest = b""
        if not header_done:
            lines = buf.split(b"\n"); j = 0
            while lines[j].startswith(b"%"): j += 1
            buf = b"\n".join(lines[j + 1:]); header_done = True      # skip the dimension line too
        if not buf.strip(): continue
        body = np.fromstring(buf, dtype=np.int64, sep=" ").reshape(-1, 3); g = body[:, 0] - 1; b = body[:, 1] - 1; v = body[:, 2].astype(np.float64)
        lib += np.bincount(b, weights=v, minlength=nb)
        m = np.isin(g, want_rows)
        for k in np.unique(g[m]):
            mm = m & (g == k); np.add.at(X[inv[int(k)]], b[mm], v[mm])
        if not blk: break
    return lib, X
def classify(lib, X):
    nb = len(lib); sc = {}
    for c, gs in SETS.items():
        vals = [np.log1p(X[g] / lib * 1e4) for g in gs if g in X]; sc[c] = np.mean(vals, axis=0) if vals else np.zeros(nb)
    M = np.column_stack([sc[c] for c in SETS]); return np.array([list(SETS)[k] if t > 0 else "unassigned" for k, t in zip(M.argmax(1), M.max(1))])
samples = [l.rstrip("\n").split("\t") for l in open(SAMPLES) if l.strip()]
data = {}
for pre, grp in samples:
    lib, X = load(pre); data[pre] = (grp, lib, X, classify(lib, X)); print(pre, grp, "nuclei", len(lib), "median UMI", int(np.median(lib)))
cl = lambda x, y: np.log2(x / y * 1e6 + 1.0)
rows = [["gene", "class", "C_per_animal_mean(mut-ctrl log2)", "ci_low", "ci_high", "C_pooled_nuclei", "n_animals_ctrl", "n_animals_mut", "nuclei_expressing_ctrl", "nuclei_expressing_mut", "readable(>=30 each)"]]
for gene in GENES:
    for klass in ("excitatory", "inhibitory", "astrocyte", "oligodendrocyte"):
        pa = {"ctrl": [], "mut": []}; pooled = {"ctrl": [0.0, 0.0], "mut": [0.0, 0.0]}; ne = {"ctrl": 0, "mut": 0}
        for pre, (grp, lib, X, c) in data.items():
            if gene not in X: continue
            m = c == klass
            if m.sum() < 20: continue
            pa[grp].append(cl(X[gene][m].sum(), lib[m].sum())); pooled[grp][0] += X[gene][m].sum(); pooled[grp][1] += lib[m].sum(); ne[grp] += int((X[gene][m] > 0).sum())
        if len(pa["ctrl"]) < 2 or len(pa["mut"]) < 2: continue
        d = np.mean(pa["mut"]) - np.mean(pa["ctrl"]); bt = rng.choice(pa["mut"], (10000, len(pa["mut"]))).mean(1) - rng.choice(pa["ctrl"], (10000, len(pa["ctrl"]))).mean(1)
        dp = cl(*pooled["mut"]) - cl(*pooled["ctrl"])
        rows.append([gene, klass, "%+.2f" % d, "%+.2f" % np.percentile(bt, 2.5), "%+.2f" % np.percentile(bt, 97.5), "%+.2f" % dp, len(pa["ctrl"]), len(pa["mut"]), ne["ctrl"], ne["mut"], "yes" if min(ne.values()) >= 30 else "no"])
open(PFX + "_genes.tsv", "w").write("\n".join("\t".join(map(str, r)) for r in rows) + "\n")
comp = [["sample", "group", "n_nuclei"] + list(SETS) + ["unassigned"]]
for pre, (grp, lib, X, c) in data.items(): comp.append([pre, grp, len(c)] + ["%.3f" % ((c == k).mean()) for k in list(SETS) + ["unassigned"]])
open(PFX + "_composition.tsv", "w").write("\n".join("\t".join(map(str, r)) for r in comp) + "\n"); print("wrote", PFX)
