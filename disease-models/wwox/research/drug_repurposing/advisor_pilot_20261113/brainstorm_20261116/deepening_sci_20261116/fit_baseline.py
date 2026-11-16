#!/usr/bin/env python3
"""Seeded random search that fits rebound_oscillator.BASE to the held Breton 2021 baseline statistics.
Targets (HELD): median interval 26.2 s; median duration 0.66 s, IQR 0.53-1.06 s; interval-rate IQR 1.1-4.2 per
minute, read as the IQR of 60/interval (INFERRED), i.e. interval Q1 14.3 s, Q3 54.5 s.
A fit shows the model CAN reproduce the held numbers; it does not show the mechanism is true."""
import argparse, json, sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0] or '.')
import rebound_oscillator as m

TARGET = dict(int_q1=14.3, int_med=26.2, int_q3=54.5, dur_q1=0.53, dur_med=0.66, dur_q3=1.06)
FREE = dict(J_N=(0.6, 1.3), J_A=(0.2, 0.6), J_I=(0.2, 0.7), b0=(-0.25, 0.1), sigma=(0.10, 0.35),
            kappa_r=(0.15, 2.0), tau_N=(0.1, 0.4), tau_r=(4.0, 14.0), tau_h=(6.0, 25.0), tau_a=(6.0, 25.0),
            tau_c=(8.0, 30.0), J_a=(0.1, 0.5), J_T=(0.1, 0.6), kappa_a=(0.1, 0.6), kappa_c=(0.5, 3.0))

def loss(o):
    if not np.isfinite(o['int_med']) or not np.isfinite(o['dur_med']) or o['n_bursts'] < 20:
        return 99.0
    l = 0.0
    for k, v in TARGET.items():
        if not np.isfinite(o[k]):
            return 99.0
        l += abs(np.log(o[k] / v)) * (1.0 if k.endswith('med') else 0.5)
    return l

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--rounds', type=int, default=4)
    ap.add_argument('--pop', type=int, default=48)
    ap.add_argument('--T', type=float, default=500.0)
    ap.add_argument('--nrep', type=int, default=4)
    ap.add_argument('--out', default='fit_baseline_result.json')
    ap.add_argument('--init', default=None, help='JSON written by an earlier fit; start the search around it')
    a = ap.parse_args(argv)
    rng = np.random.default_rng(a.seed)
    lo = np.array([FREE[k][0] for k in FREE]); hi = np.array([FREE[k][1] for k in FREE])
    keys = list(FREE)
    center = np.array([m.BASE[k] if k in m.BASE else (lo[i]+hi[i])/2 for i, k in enumerate(keys)])
    center[keys.index('J_N')] = 0.9; center[keys.index('kappa_r')] = 1.0
    if a.init:
        pr = json.load(open(a.init))['params']
        center = np.array([pr[k] for k in keys])
    width = (hi - lo) * (0.2 if a.init else 0.5)
    best = (1e9, None, None)
    for rd in range(a.rounds):
        X = np.clip(center + width * rng.uniform(-1, 1, (a.pop, len(keys))), lo, hi)
        if rd == 0:
            X[0] = center
        P = {k: np.full(a.pop, m.BASE[k]) for k in m.BASE}
        for i, k in enumerate(keys):
            P[k] = X[:, i]
        out = m.stats(P, a.T, a.seed * 100 + rd, a.nrep)
        L = np.array([loss(o) for o in out])
        j = int(np.argmin(L))
        print('round', rd, 'best loss %.3f' % L[j], {k: round(float(X[j, i]), 3) for i, k in enumerate(keys)}, flush=True)
        if L[j] < best[0]:
            best = (float(L[j]), X[j].copy(), out[j])
        idx = np.argsort(L)[:6]
        center = X[idx].mean(0); width = np.maximum(X[idx].std(0) * 1.5, (hi - lo) * 0.03)
    params = {k: round(float(best[1][i]), 4) for i, k in enumerate(keys)}
    json.dump(dict(loss=best[0], params=params, stats=best[2]), open(a.out, 'w'), indent=1, default=float)
    print(json.dumps(dict(loss=best[0], params=params, stats=best[2]), default=float))
    return 0

if __name__ == '__main__':
    sys.exit(main())
