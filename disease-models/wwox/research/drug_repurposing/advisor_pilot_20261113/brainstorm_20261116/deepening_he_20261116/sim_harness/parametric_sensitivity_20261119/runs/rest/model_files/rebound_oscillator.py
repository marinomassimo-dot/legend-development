#!/usr/bin/env python3
"""I1 two-stage rebound oscillator: a minimal stochastic mean-field model (HYPOTHESIS GENERATOR, NOT EVIDENCE).

Mechanism-level only. No dose, no agent recommendation. Reference genotype class only.
Dependencies: numpy. Everything is seeded; the same seed gives the same numbers.

State per network (all vectorised over a batch of parameter sets x replicate networks):
  u  population activity (0..1)          fast, tau_u
  n  NMDAR-gated synaptic variable       tau_N       (the SUSTAINER)
  r  synaptic resource                   depleted by activity, recovers tau_r
  c  intracellular chloride (mM)         loaded by activity, extruded tau_c (KCC2)
  a  extracellular adenosine (a.u.)      produced by activity, cleared tau_a (adenosine kinase / uptake)
  h  T-type-like availability            inactivated by activity, recovers tau_h  (the TRIGGER)
  eta coloured noise                     tau_eta
  x  = drive:  b0 - J_tonic*G(c)*(1+pam) - J_a*a + J_T*h*psi + J_A*r*u + J_N*r*n - J_I*G(c)*u + s*eta
  u' = (-u + S(x)) / tau_u
  G(c) is the GABA-A driving force scaled to its resting value, from the Nernst potential of Cl-;
  it falls as c rises and changes sign when E_Cl passes the resting potential.
  psi (rebound gate) rises with the hyperpolarisation delivered by tonic GABA-A and adenosine.

Every constant below is ASSUMED unless a comment says HELD. The only held numbers used are the
two Breton 2021 baselines (median interval 26.2 s, median duration 0.66 s [0.53-1.06]) and the
interval-rate IQR 1.1-4.2 per minute (read as the IQR of 60/interval: INFERRED).
"""
import argparse
import hashlib
import json
import sys

import numpy as np

DT = 0.004
V_REF = -65.0      # mV, ASSUMED resting potential for the Cl- driving force
CL_O = 130.0       # mM, ASSUMED slice ACSF chloride

# The fitted parameter set (see fit_baseline); values rounded for readability.
BASE = dict(
    b0=-0.1503, J_tonic=0.30, J_a=0.2053, J_T=0.2752, J_A=0.3542, J_N=1.077, J_I=0.2567,
    tau_u=0.02, tau_N=0.1054, tau_r=5.9994, tau_c=17.7586, tau_a=11.4628, tau_h=15.663,
    kappa_r=0.7766, kappa_c=0.7976, kappa_a=0.3723, kappa_h=3.0,
    c0=6.0, sigma=0.1052, tau_eta=0.05, k=0.08, pam=0.0,
    th_psi=0.45, k_psi=0.15,
    hcn_block=0.0, G_H=0.10, brake=0.0, tonic_gaba=1.0, phasic_gain=1.0, load_coupling=0.0,
)


def Gfun(c):
    e_cl = -26.7 * np.log(CL_O / np.maximum(c, 0.5))
    e0 = -26.7 * np.log(CL_O / BASE["c0"])
    return (V_REF - e_cl) / (V_REF - e0)


def simulate(P, T, seed, nrep=1, burn=60.0, u0=0.0, rec=None):
    """P: dict of floats or arrays of shape (B,). Returns list over B*nrep networks of (onsets, durations)."""
    names = list(P.keys())
    arr = {k: np.atleast_1d(np.asarray(v, float)) for k, v in P.items()}
    B = max(len(v) for v in arr.values())
    for k in arr:
        if len(arr[k]) == 1:
            arr[k] = np.repeat(arr[k], B)
    N = B * nrep
    p = {k: np.repeat(arr[k], nrep) for k in names}
    rng = np.random.default_rng(seed)
    u = np.full(N, u0); n = np.full(N, u0); r = np.ones(N)
    c = p["c0"].copy(); a = np.zeros(N); h = np.ones(N); eta = np.zeros(N)
    on = np.zeros(N, bool); t_on = np.zeros(N)
    res = [([], []) for _ in range(N)]
    steps = int((T + burn) / DT)
    nb = int(burn / DT)
    sq = np.sqrt(2 * DT / p["tau_eta"])
    e0 = -26.7 * np.log(CL_O / BASE["c0"])
    for s in range(steps):
        t = s * DT
        G = (V_REF + 26.7 * np.log(CL_O / np.maximum(c, 0.5))) / (V_REF - e0)
        vh = p["J_tonic"] * G * (1 + p["pam"]) * p["tonic_gaba"] + p["J_a"] * a + p["hcn_block"] * p["G_H"]
        psi = 1.0 / (1.0 + np.exp(-(vh - p["th_psi"]) / p["k_psi"]))
        x = (p["b0"] - p["J_tonic"] * G * (1 + p["pam"]) * p["tonic_gaba"] - p["J_a"] * a - p["hcn_block"] * p["G_H"]
             + p["J_T"] * h * psi
             + (1 - p["brake"]) * (p["J_A"] * r * u + p["J_N"] * r * n) - p["J_I"] * (1 + p["pam"]) * p["phasic_gain"] * G * u + p["sigma"] * eta)
        S = 1.0 / (1.0 + np.exp(-x / p["k"]))
        u = u + DT * (-u + S) / p["tau_u"]
        n = n + DT * (-n + u) / p["tau_N"]
        r = r + DT * ((1 - r) / p["tau_r"] - p["kappa_r"] * u * r)
        c = c + DT * (p["kappa_c"] * (1 + p["load_coupling"] * p["pam"]) * u * np.maximum(G, 0.0) + (p["c0"] - c) / p["tau_c"])
        a = a + DT * (p["kappa_a"] * u - a / p["tau_a"])
        h = h + DT * ((1 - h) / p["tau_h"] - p["kappa_h"] * u * h)
        eta = eta - DT * eta / p["tau_eta"] + sq * rng.standard_normal(N)
        if rec is not None and s % 25 == 0:
            rec.append((t, u[0], n[0], r[0], c[0], a[0], h[0], x[0]))
        up = (~on) & (u > 0.5)
        dn = on & (u < 0.25)
        if up.any():
            on[up] = True; t_on[up] = t
        if dn.any():
            on[dn] = False
            if s >= nb:
                for i in np.nonzero(dn)[0]:
                    res[i][0].append(t_on[i]); res[i][1].append(t - t_on[i])
    return res


def summarise(res_list):
    ints, durs = [], []
    for onsets, d in res_list:
        o = np.array(onsets); dd = np.array(d)
        keep = dd > 0.1
        o = o[keep]; dd = dd[keep]
        if len(o) > 1:
            ints.extend(np.diff(o).tolist())
        durs.extend(dd.tolist())
    ints = np.array(ints); durs = np.array(durs)
    def q(x):
        return (np.nan, np.nan, np.nan, 0) if len(x) < 3 else (*np.quantile(x, [.25, .5, .75]), len(x))
    return q(ints), q(durs)


def gamma_shape(x):
    x = np.asarray(x)
    if len(x) < 5:
        return float("nan")
    return float(np.mean(x) ** 2 / np.var(x))


def stats(P, T, seed, nrep):
    """Per parameter set: median interval, interval CV^-2 (gamma shape), median duration, duration shape, burst rate."""
    res = simulate(P, T, seed, nrep)
    B = len(res) // nrep
    out = []
    for b in range(B):
        grp = res[b * nrep:(b + 1) * nrep]
        ints, durs, nb = [], [], 0
        for onsets, d in grp:
            o = np.array(onsets); dd = np.array(d); keep = dd > 0.1
            o = o[keep]; dd = dd[keep]
            nb += len(o)
            if len(o) > 1:
                ints.extend(np.diff(o).tolist())
            durs.extend(dd.tolist())
        ints = np.array(ints); durs = np.array(durs)
        rate = nb / (nrep * T) * 60.0
        row = dict(rate_per_min=rate, n_bursts=nb)
        if len(ints) >= 5:
            row.update(int_q1=float(np.quantile(ints, .25)), int_med=float(np.median(ints)), int_q3=float(np.quantile(ints, .75)),
                       int_shape=gamma_shape(ints))
        else:
            row.update(int_q1=np.nan, int_med=np.nan, int_q3=np.nan, int_shape=np.nan)
        if len(durs) >= 5:
            row.update(dur_q1=float(np.quantile(durs, .25)), dur_med=float(np.median(durs)), dur_q3=float(np.quantile(durs, .75)),
                       dur_shape=gamma_shape(durs))
        else:
            row.update(dur_q1=np.nan, dur_med=np.nan, dur_q3=np.nan, dur_shape=np.nan)
        out.append(row)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="I1 rebound-oscillator model: hypothesis generator, not evidence. numpy only; seeded.")
    ap.add_argument("--seed", type=int, default=20261116)
    ap.add_argument("--T", type=float, default=600.0, help="seconds simulated per network after the burn-in")
    ap.add_argument("--nrep", type=int, default=16)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    row = stats(BASE, a.T, a.seed, a.nrep)[0]
    txt = json.dumps(row, sort_keys=True, default=float)
    print(txt)
    print("sha256", hashlib.sha256(txt.encode()).hexdigest()[:16])
    return 0


if __name__ == "__main__":
    sys.exit(main())
