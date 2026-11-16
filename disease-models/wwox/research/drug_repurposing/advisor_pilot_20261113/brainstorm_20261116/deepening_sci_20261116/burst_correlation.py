#!/usr/bin/env python3
"""Within-network Spearman correlation of burst duration with the following (and preceding) inter-burst interval in the fitted oscillator. Hypothesis generator, not evidence.
Predictions frozen first: PREDICTIONS_BURST_CORR_FROZEN_BEFORE_RUN.md.
    python3 burst_correlation.py --help
    python3 burst_correlation.py run <out_tsv> [--nets 300]"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
def rank(x):
    o = np.argsort(x, kind="mergesort"); r = np.empty(len(x)); r[o] = np.arange(len(x)); 
    # average ties
    for v in np.unique(x):
        i = np.nonzero(x == v)[0]
        if len(i) > 1: r[i] = r[i].mean()
    return r
def sp(a, b):
    if len(a) < 4: return float("nan")
    ra, rb = rank(np.asarray(a)), rank(np.asarray(b)); ra -= ra.mean(); rb -= rb.mean()
    d = np.sqrt((ra ** 2).sum() * (rb ** 2).sum()); return float((ra * rb).sum() / d) if d > 0 else float("nan")
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--nets", type=int, default=300); ap.add_argument("--seed", type=int, default=20261122); ap.add_argument("--T", type=float, default=900.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    P = {k: np.full(a.nets, v) for k, v in m.BASE.items()}
    res = m.simulate(P, a.T, a.seed, nrep=1)
    nxt, prv, pooled_d, pooled_n, pooled_p = [], [], [], [], []
    for onsets, durs in res:
        o = np.array([x for x, d in zip(onsets, durs) if d > 0.1]); d = np.array([d for d in durs if d > 0.1])
        if len(o) < 8: continue
        iv = np.diff(o)                       # iv[i] = interval after burst i
        nxt.append(sp(d[:-1], iv)); prv.append(sp(iv, d[1:]))
        pooled_d += list(d[:-1]); pooled_n += list(iv)
    with open(a.out, "w") as f:
        f.write("statistic\tvalue\tnetworks\n")
        f.write(f"mean_within_rho_duration_vs_following_interval\t{np.nanmean(nxt):.3f}\t{len(nxt)}\n")
        f.write(f"sd_within_rho_duration_vs_following_interval\t{np.nanstd(nxt):.3f}\t{len(nxt)}\n")
        f.write(f"mean_within_rho_preceding_interval_vs_duration\t{np.nanmean(prv):.3f}\t{len(prv)}\n")
        f.write(f"pooled_rho_duration_vs_following_interval\t{sp(pooled_d, pooled_n):.3f}\t{len(nxt)}\n")
    print(open(a.out).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
