#!/usr/bin/env python3
"""One-stage rival of the I1 oscillator: a sub-model of the frozen model (J_T = 0, J_a = 0, kappa_c = 0) fitted by a seeded random search to four held Breton 2021 targets
(median interval 26.2 s, median duration 0.66 s, interval gamma shape 1.43, duration gamma shape 2.45). Hypothesis generator, not evidence. Predictions: PREDICTIONS_ONE_STAGE_RIVAL_FROZEN_BEFORE_FIT.md.
    python3 rival_one_stage.py --help
    python3 rival_one_stage.py fit <out_json> [--rounds 10] [--pop 64]
    python3 rival_one_stage.py show <result_json> [--T 1500 --nrep 32]
Imports the frozen rebound_oscillator.py unchanged. numpy only; seeded."""
import argparse, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # frozen rebound_oscillator.py lives in the parent folder
import numpy as np
import rebound_oscillator as m
FIXED = {"J_T": 0.0, "J_a": 0.0, "kappa_c": 0.0}
FREE = dict(J_N=(0.5, 1.4), J_A=(0.15, 0.6), J_I=(0.1, 0.6), J_tonic=(0.1, 0.5), b0=(-0.3, 0.05), sigma=(0.06, 0.4), kappa_r=(0.2, 2.5), tau_r=(2.0, 40.0), tau_N=(0.05, 0.5))
TARGET = dict(int_med=26.2, dur_med=0.66, int_shape=1.43, dur_shape=2.45)
def base():
    P = dict(m.BASE); P.update(FIXED); return P
def loss(o):
    if not np.isfinite(o["int_med"]) or not np.isfinite(o["dur_med"]) or o["n_bursts"] < 20: return 99.0
    if not np.isfinite(o["int_shape"]) or not np.isfinite(o["dur_shape"]): return 99.0
    return sum(abs(np.log(o[k] / v)) * (1.0 if k.endswith("med") else 0.7) for k, v in TARGET.items())
def fit(out, rounds, pop, T=700.0, nrep=4, seed=31, init=None):
    rng = np.random.default_rng(seed); keys = list(FREE); lo = np.array([FREE[k][0] for k in keys]); hi = np.array([FREE[k][1] for k in keys])
    center = (lo + hi) / 2; width = (hi - lo) * 0.5; best = (1e9, None, None)
    if init:
        pr = json.load(open(init))['params']; center = np.array([pr[k] for k in keys]); width = (hi - lo) * 0.2
    for rd in range(rounds):
        X = np.clip(center + width * rng.uniform(-1, 1, (pop, len(keys))), lo, hi)
        P = {k: np.full(pop, v) for k, v in base().items()}
        for i, k in enumerate(keys): P[k] = X[:, i]
        res = m.stats(P, T, seed * 100 + rd, nrep); L = np.array([loss(o) for o in res]); j = int(np.argmin(L))
        print("round", rd, "best loss %.3f" % L[j], flush=True)
        if L[j] < best[0]: best = (float(L[j]), X[j].copy(), res[j])
        idx = np.argsort(L)[:6]; center = X[idx].mean(0); width = np.maximum(X[idx].std(0) * 1.5, (hi - lo) * 0.03)
    params = {k: round(float(best[1][i]), 4) for i, k in enumerate(keys)}
    json.dump(dict(loss=best[0], params=params, stats=best[2]), open(out, "w"), indent=1, default=float); print(open(out).read())
def show(path, T, nrep):
    pr = json.load(open(path))["params"]; P = base(); P.update(pr)
    print(json.dumps(m.stats(P, T, 5, nrep)[0], default=float, sort_keys=True))
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd", choices=["fit", "show"]); ap.add_argument("out")
    ap.add_argument("--rounds", type=int, default=10); ap.add_argument("--pop", type=int, default=64); ap.add_argument("--T", type=float, default=1500.0); ap.add_argument("--nrep", type=int, default=32); ap.add_argument("--init", default=None); ap.add_argument("--seed", type=int, default=31)
    a = ap.parse_args()
    fit(a.out, a.rounds, a.pop, seed=a.seed, init=a.init) if a.cmd == "fit" else show(a.out, a.T, a.nrep)
