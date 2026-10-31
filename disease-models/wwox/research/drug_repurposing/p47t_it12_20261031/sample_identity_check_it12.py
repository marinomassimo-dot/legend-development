#!/usr/bin/env python3
"""IT12 P2-P47T: sample-identity and separation checks on GSE215425.
Usage: sample_identity_check_it12.py run COUNTS.csv.gz OUT.tsv   (stdlib + numpy; --help prints this)
(1) per region: ratio of mean between-genotype to mean within-genotype Euclidean distance on the 2000 most variable genes (log2 CPM+1), and the PC1 coordinates;
(2) per animal, the same marker per region: Nptx2, Bdnf, Gfap log2 CPM, so a P47T animal can be followed across regions (identity/ordering sanity)."""
import sys
if len(sys.argv) < 2 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, numpy as np
rows = list(csv.reader(gzip.open(sys.argv[2], "rt"), delimiter="\t")); head = rows[0]; rows = rows[1:]
sym = [r[1] for r in rows]; C = np.array([[float(v) for v in r[2:]] for r in rows]); cols = head[2:]
out = [["check", "region", "item", "value"]]
for reg in ["HPC", "CTX", "PFC", "CB"]:
    idx = [j for j, c in enumerate(cols) if c.startswith(reg + "_")]; X = C[:, idx]
    cpm = X / X.sum(0) * 1e6; L = np.log2(cpm + 1); g = np.array(["P47T" in cols[j] for j in idx])
    keep = (cpm >= 1).sum(1) >= 3; v = L[keep].var(1); top = np.argsort(-v)[:2000]; M = L[keep][top].T
    D = np.sqrt(((M[:, None, :] - M[None, :, :]) ** 2).sum(2))
    bw = np.mean([D[i, j] for i in range(len(g)) for j in range(len(g)) if g[i] != g[j]])
    wi = np.mean([D[i, j] for i in range(len(g)) for j in range(i + 1, len(g)) if g[i] == g[j]])
    Mc = M - M.mean(0); U, S, Vt = np.linalg.svd(Mc, full_matrices=False); pc1 = U[:, 0] * S[0]
    out.append(["separation", reg, "between/within distance ratio (top 2000 variable genes)", "%.3f" % (bw / wi)])
    for j, p in zip(idx, pc1): out.append(["PC1", reg, cols[j], "%.2f" % p])
    for gname in ["Nptx2", "Bdnf", "Gfap", "Wwox"]:
        ii = [i for i, s in enumerate(sym) if s == gname]; i = max(ii, key=lambda k: C[k].sum())
        for j, n in zip(range(len(idx)), idx): out.append(["marker_log2CPM_" + gname, reg, cols[n], "%.2f" % L[i, j]])
with open(sys.argv[3], "w", newline="") as fh: csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(out)
for r in out:
    if r[0] == "separation": print(r)
