#!/usr/bin/env python3
"""I3 in the I1 model: how large must a presynaptic brake on recurrent excitation (NPY-like) be to silence the fitted bursting network,
and does removing a brake on a braked network unmask bursts? Hypothesis generator, not evidence.
    python3 brake_cliff.py --help
    python3 brake_cliff.py run <out_tsv>"""
import os, sys
if len(sys.argv) != 3 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
B = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
# silent networks (a brake of b) then 'unmasking' = the same network with the brake lowered by 0.5*b or removed, and with a compensating extra drive typical of the null
P = {k: np.full(len(B), m.BASE[k]) for k in m.BASE}; P["brake"] = np.array(B)
rows = m.stats(P, 900.0, 77, 16)
with open(sys.argv[2], "w") as f:
    f.write("brake\trate_per_min\tn_bursts\tint_med\tdur_med\n")
    for b, r in zip(B, rows):
        f.write(f"{b}\t{r['rate_per_min']:.3f}\t{r['n_bursts']}\t{r['int_med']:.2f}\t{r['dur_med']:.3f}\n")
print(open(sys.argv[2]).read())
