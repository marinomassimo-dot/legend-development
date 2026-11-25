"""ADV-231 post hoc (NOT frozen): per-animal STAT3-axis score in the P47T per-animal table. Print-only; held file only.
For each region and each P47T animal: mean over the genes of log2((count+0.5)/(mean WT count+0.5)); then the same with the animal's
region leave-one-out comparison. Reported as post hoc beside the frozen result, never replacing it.

Usage: python3 -I p47t_animal_posthoc_adv231.py <p47t_processed.csv.gz>
"""
import sys

if len(sys.argv) != 2:
    print(__doc__)
    raise SystemExit(0)
import gzip
import numpy as np

GENES = ["Stat3", "Jak2", "Il6st", "Socs3", "Socs1", "Osmr", "Bcl3", "Pim1"]
f = gzip.open(sys.argv[1], "rt")
head = f.readline().rstrip("\n").split("\t")[2:]
rows = {}
for l in f:
    p = l.rstrip("\n").split("\t")
    s = p[1].upper()
    if s not in rows:
        rows[s] = np.array([float(x) if x not in ("", "NA") else 0.0 for x in p[2:]])
print("region\tanimal\tgenotype\tscore_mean_log2_vs_WTmean\tper_gene_log2_" + "_".join(GENES))
for reg in ("PFC", "HPC", "CTX", "CB"):
    wt = [i for i, a in enumerate(head) if a.startswith(reg + "_WT")]
    ko = [i for i, a in enumerate(head) if a.startswith(reg + "_P47T")]
    for i in wt + ko:
        vals = []
        for g in GENES:
            base = rows[g.upper()][wt].mean()
            vals.append(np.log2((rows[g.upper()][i] + .5) / (base + .5)))
        print("%s\t%s\t%s\t%.3f\t%s" % (reg, head[i].split("_", 1)[1], "WT" if i in wt else "P47T", np.mean(vals), ";".join("%.2f" % v for v in vals)))
