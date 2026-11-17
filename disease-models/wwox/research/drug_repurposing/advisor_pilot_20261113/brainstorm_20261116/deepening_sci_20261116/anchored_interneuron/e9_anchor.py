#!/usr/bin/env python3
"""E9 re-check for the anchored arms 91 to 94 (SCI, 2026-11-17): at strength s = 1, S-KO rel_bursts and S-HT incidence change (arm minus baseline), 5 seeds from base seed 1000, same adapter as the bisection.
    python3 e9_anchor.py --help
    python3 e9_anchor.py run <dir containing pilot_bisect_anchor_model.py and rebound_oscillator.py> <out.tsv>"""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import os
sys.path.insert(0, sys.argv[2])
import numpy as np
import pilot_bisect_anchor_model as M
rows = [["arm", "geno", "median_rel_bursts_s1", "mean_incidence_baseline", "mean_incidence_arm", "mean_incidence_change", "n_seeds"]]
for arm in (91, 92, 93, 94, 9, 8):
    for geno, name in ((0, "S-KO"), (1, "S-HT")):
        res = [M.simulate({"geno": geno, "arm": arm, "strength": 1.0}, 1000 + k) for k in range(5)]
        rb = [r["rel_bursts"] for r in res]; ib = [r["incidence_baseline"] for r in res]; ia = [r["incidence_arm"] for r in res]
        rows.append([arm, name, "%.3f" % np.nanmedian(rb), "%.3f" % np.mean(ib), "%.3f" % np.mean(ia), "%+.3f" % (np.mean(ia) - np.mean(ib)), len(res)])
open(sys.argv[3], "w").write("\n".join("\t".join(map(str, r)) for r in rows) + "\n")
print("wrote", sys.argv[3])
