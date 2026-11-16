#!/usr/bin/env python3
"""Fairness check: refit the TWO-STAGE oscillator to the same four held targets as the rival (median interval 26.2 s, median duration 0.66 s, interval shape 1.43, duration shape 2.45),
starting from the frozen fit; the frozen model file is not changed (this writes a separate parameter file). Hypothesis generator, not evidence.
    python3 refit_twostage_shapes.py --help
    python3 refit_twostage_shapes.py run <out_json> [--rounds 12] [--pop 64]"""
import argparse, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # frozen rebound_oscillator.py lives in the parent folder
import numpy as np
import rebound_oscillator as m
KEYS = ["J_N", "J_A", "J_I", "b0", "sigma", "kappa_r", "tau_N", "tau_r", "tau_h", "tau_a", "tau_c", "J_a", "J_T", "kappa_a", "kappa_c", "J_tonic"]
LO = dict(J_N=0.6, J_A=0.2, J_I=0.15, b0=-0.3, sigma=0.06, kappa_r=0.15, tau_N=0.05, tau_r=2.0, tau_h=5.0, tau_a=5.0, tau_c=5.0, J_a=0.05, J_T=0.05, kappa_a=0.1, kappa_c=0.2, J_tonic=0.15)
HI = dict(J_N=1.5, J_A=0.6, J_I=0.6, b0=0.0, sigma=0.4, kappa_r=2.5, tau_N=0.5, tau_r=30.0, tau_h=30.0, tau_a=30.0, tau_c=40.0, J_a=0.6, J_T=0.7, kappa_a=0.8, kappa_c=3.0, J_tonic=0.5)
TARGET = dict(int_med=26.2, dur_med=0.66, int_shape=1.43, dur_shape=2.45)
def loss(o):
    if any(not np.isfinite(o[k]) for k in TARGET) or o["n_bursts"] < 20: return 99.0
    return sum(abs(np.log(o[k] / v)) * (1.0 if k.endswith("med") else 0.7) for k, v in TARGET.items())
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out"); ap.add_argument("--rounds", type=int, default=12); ap.add_argument("--pop", type=int, default=64)
    a = ap.parse_args()
    if a.cmd != "run":
        print(__doc__); raise SystemExit(0)
    rng = np.random.default_rng(51); lo = np.array([LO[k] for k in KEYS]); hi = np.array([HI[k] for k in KEYS])
    center = np.array([m.BASE[k] for k in KEYS]); width = (hi - lo) * 0.15; best = (1e9, None, None)
    for rd in range(a.rounds):
        X = np.clip(center + width * rng.uniform(-1, 1, (a.pop, len(KEYS))), lo, hi)
        if rd == 0: X[0] = center
        P = {k: np.full(a.pop, m.BASE[k]) for k in m.BASE}
        for i, k in enumerate(KEYS): P[k] = X[:, i]
        res = m.stats(P, 700.0, 5100 + rd, 4); L = np.array([loss(o) for o in res]); j = int(np.argmin(L)); print("round", rd, "best %.3f" % L[j], flush=True)
        if L[j] < best[0]: best = (float(L[j]), X[j].copy(), res[j])
        idx = np.argsort(L)[:6]; center = X[idx].mean(0); width = np.maximum(X[idx].std(0) * 1.5, (hi - lo) * 0.02)
    json.dump(dict(loss=best[0], params={k: round(float(best[1][i]), 4) for i, k in enumerate(KEYS)}, stats=best[2]), open(a.out, "w"), indent=1, default=float); print(open(a.out).read())
