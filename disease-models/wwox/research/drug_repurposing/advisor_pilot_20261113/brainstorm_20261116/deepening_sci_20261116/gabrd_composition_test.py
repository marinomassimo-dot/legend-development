#!/usr/bin/env python3
"""Per-animal test of the composition rival for the Gabrd fall in P47T (GSE215425). Predictions frozen first: PREDICTIONS_GABRD_COMPOSITION_FROZEN_BEFORE_RUN.md. Hypothesis level.
    python3 gabrd_composition_test.py --help
    python3 gabrd_composition_test.py run <GSE215425_processed_data.csv.gz> <out_tsv>
numpy only; seeded. Value = log2(count + 1). Scores = mean over marker genes. OLS with sex covariate; residual correlation after genotype and sex; 10,000-draw permutation."""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip
import numpy as np
SETS = {"neuron": ["Snap25", "Rbfox3", "Syt1", "Stmn2", "Slc17a7"], "astrocyte": ["Aqp4", "Slc1a3", "Aldh1l1", "Sox9", "Gja1"], "microglia": ["Aif1", "Cx3cr1", "P2ry12", "Tmem119"],
        "oligodendrocyte": ["Mbp", "Plp1", "Mog", "Mobp"]}
SINGLE = ["Lamp5", "Sst", "Cck", "Pvalb", "Vip", "Npy", "Ndnf", "Gfap"]
f = gzip.open(sys.argv[2], "rt"); rd = csv.reader(f, delimiter="\t"); hdr = next(rd); gene = {}
for r in rd:
    if len(r) > 2: gene.setdefault(r[1], [float(x) for x in r[2:]])
cols = hdr[2:]
def meta(c):
    reg, rest = c.split("_", 1); geno = "P47T" if "P47T" in rest else "WT"; sex = rest.split("_")[-1][0]
    return reg, geno, sex
rng = np.random.default_rng(1)
def ols(y, X):
    b, *_ = np.linalg.lstsq(X, y, rcond=None); return b
out = []
for reg in ("CTX", "PFC", "HPC", "CB"):
    idx = [i for i, c in enumerate(cols) if meta(c)[0] == reg]
    g = np.array([1.0 if meta(cols[i])[1] == "P47T" else 0.0 for i in idx]); s = np.array([1.0 if meta(cols[i])[2] == "M" else 0.0 for i in idx])
    L = lambda name: np.log2(np.array([gene[name][i] for i in idx]) + 1.0)
    y = L("Gabrd"); X0 = np.column_stack([np.ones(len(idx)), g]); X1 = np.column_stack([np.ones(len(idx)), g, s])
    b0 = ols(y, X0)[1]; b1 = ols(y, X1)[1]; out.append((reg, "Gabrd genotype effect (no covariate / sex covariate)", f"{b0:+.2f} / {b1:+.2f}", "", "", len(idx)))
    if reg == "CB": continue
    scores = {k: np.mean([L(x) for x in v if x in gene], axis=0) for k, v in SETS.items()}
    for k in SINGLE:
        if k in gene: scores[k] = L(k)
    for k, sc in scores.items():
        Xa = np.column_stack([np.ones(len(idx)), g, s, sc]); ba = ols(y, Xa)[1]; shrink = 1 - ba / b1
        ry = y - X1 @ ols(y, X1); rs = sc - X1 @ ols(sc, X1)
        r = float(np.corrcoef(ry, rs)[0, 1]); cnt = 0
        for _ in range(10000):
            if abs(np.corrcoef(ry, rng.permutation(rs))[0, 1]) >= abs(r): cnt += 1
        gscore = float(ols(sc, X0)[1])
        out.append((reg, k, f"score genotype effect {gscore:+.2f}", f"adjusted genotype coefficient {ba:+.2f} (shrinkage {shrink:+.0%})", f"residual r {r:+.2f}, perm p {(cnt + 1) / 10001:.3f}", len(idx)))
with open(sys.argv[3], "w", newline="") as fo:
    w = csv.writer(fo, delimiter="\t", lineterminator="\n"); w.writerow(["region", "item", "value1", "value2", "value3", "animals"]); w.writerows(out)
for r in out: print("\t".join(str(x) for x in r))
