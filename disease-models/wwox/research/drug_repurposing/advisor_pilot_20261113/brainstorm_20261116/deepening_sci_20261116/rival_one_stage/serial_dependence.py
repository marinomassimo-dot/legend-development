#!/usr/bin/env python3
"""Within-network Spearman rho of burst duration with the following interval, for the one-stage rival and the refitted two-stage model. Hypothesis generator, not evidence.
Predictions: PREDICTIONS_RIVAL_CONFIRM_FROZEN_BEFORE_RUN.md.
    python3 serial_dependence.py --help
    python3 serial_dependence.py run <rival_fit.json> <twostage_refit.json> <out_tsv> [--nets 300]"""
import argparse, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # frozen rebound_oscillator.py lives in the parent folder
import numpy as np
import rebound_oscillator as m
def rank(x):
    o = np.argsort(x, kind="mergesort"); r = np.empty(len(x)); r[o] = np.arange(len(x))
    for v in np.unique(x):
        i = np.nonzero(x == v)[0]
        if len(i) > 1: r[i] = r[i].mean()
    return r
def sp(a, b):
    if len(a) < 4: return float("nan")
    ra, rb = rank(np.asarray(a)), rank(np.asarray(b)); ra -= ra.mean(); rb -= rb.mean(); d = np.sqrt((ra ** 2).sum() * (rb ** 2).sum())
    return float((ra * rb).sum() / d) if d > 0 else float("nan")
def run(P0, nets, T, seed):
    P = {k: np.full(nets, v) for k, v in P0.items()}; res = m.simulate(P, T, seed, nrep=1); nxt = []; prv = []
    for onsets, durs in res:
        o = np.array([x for x, d in zip(onsets, durs) if d > 0.1]); d = np.array([d for d in durs if d > 0.1])
        if len(o) < 8: continue
        iv = np.diff(o); nxt.append(sp(d[:-1], iv)); prv.append(sp(iv, d[1:]))
    return np.nanmean(nxt), np.nanstd(nxt), np.nanmean(prv), len(nxt)
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("rival"); ap.add_argument("twostage"); ap.add_argument("out")
    ap.add_argument("--nets", type=int, default=300); ap.add_argument("--T", type=float, default=900.0); a = ap.parse_args()
    if a.cmd != "run":
        print(__doc__); raise SystemExit(0)
    rb = dict(m.BASE); rb.update({"J_T": 0.0, "J_a": 0.0, "kappa_c": 0.0}); rb.update(json.load(open(a.rival))["params"])
    tb = dict(m.BASE); tb.update(json.load(open(a.twostage))["params"])
    with open(a.out, "w") as f:
        f.write("model\tmean_within_rho_duration_vs_following_interval\tsd\tmean_rho_preceding_interval_vs_duration\tnetworks\n")
        for name, P0 in (("one_stage_rival", rb), ("two_stage_refit", tb), ("two_stage_frozen", dict(m.BASE))):
            r = run(P0, a.nets, a.T, 7); f.write(f"{name}\t{r[0]:.3f}\t{r[1]:.3f}\t{r[2]:.3f}\t{r[3]}\n")
    print(open(a.out).read())
