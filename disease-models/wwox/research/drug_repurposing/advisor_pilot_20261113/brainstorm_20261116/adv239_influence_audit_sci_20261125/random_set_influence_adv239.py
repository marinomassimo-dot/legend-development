"""ADV-239 post hoc (not pre-registered): which animal has the largest leave-one-out influence on RANDOM gene sets of
GSE215425? 2000 random sets of 100 expressed genes (mean CPM >= 1) per region, same TMM log2CPM and set-mean effect as
influence_adv239.py. An animal that tops the list far above 1/n is influential as a library, not through a pathway.

Usage: python3 -I random_set_influence_adv239.py <GSE215425_processed.csv.gz> <out.tsv>
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import gzip
import numpy as np

ns = {}
src = open(__file__.replace("random_set_influence_adv239.py", "influence_adv239.py")).read()
exec(src[src.index("def tmm_factors"):src.index("UNITS, SUMMARY")], {"np": np}, ns)
with gzip.open(sys.argv[1], "rt") as fh:
    head = fh.readline().rstrip("\n").split("\t")[2:]
    rows = [l.rstrip("\n").split("\t") for l in fh]
C = np.array([[float(v) for v in r[2:]] for r in rows])
rng = np.random.default_rng(20261125)
out = open(sys.argv[2], "w")
out.write("region\tanimal\tarm\tfraction_of_random_sets_where_most_influential\tchance\tmean_signed_unit_score\n")
for reg in ("HPC", "CTX", "PFC", "CB"):
    cols = [j for j, c in enumerate(head) if c.startswith(reg + "_")]
    ids = [head[j].split("_", 2)[2] for j in cols]
    mut = np.array(["P47T" in head[j] for j in cols])
    cnt = C[:, cols]
    f, _ = ns["tmm_factors"](cnt[cnt.sum(1) > 0])
    lib_eff = cnt.sum(0) * f
    lc = ns["logcpm"](cnt, lib_eff)
    expr = np.where((cnt / lib_eff * 1e6).mean(1) >= 1)[0]
    cen = lc - lc.mean(1, keepdims=True)
    hits = np.zeros(len(ids)); score = np.zeros(len(ids))
    for _ in range(2000):
        s = cen[rng.choice(expr, 100, replace=False)].mean(0)
        full = s[mut].mean() - s[~mut].mean()
        change = []
        for k in range(len(ids)):
            m = np.ones(len(ids), bool); m[k] = False
            change.append(abs((s[m & mut].mean() - s[m & ~mut].mean()) - full))
        hits[int(np.argmax(change))] += 1
        score += np.abs(s)
    for k, a in enumerate(ids):
        out.write("%s\t%s\t%s\t%.3f\t%.3f\t%.4f\n" % (reg, a, "P47T" if mut[k] else "WT", hits[k] / 2000, 1 / len(ids), score[k] / 2000))
out.close()
print("done")
