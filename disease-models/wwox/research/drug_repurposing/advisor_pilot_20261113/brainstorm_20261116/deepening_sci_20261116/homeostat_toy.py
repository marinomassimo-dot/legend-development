#!/usr/bin/env python3
"""LABELLED TOY: the I1 rebound oscillator plus a slow homeostatic gain w. HYPOTHESIS GENERATOR, NOT EVIDENCE.

Mechanism-level only. No dose, no agent. Reference genotype class only. numpy only; seeded.
w multiplies the excitatory recurrent weights (J_A and J_N); it is driven by the deviation of a slow running mean
of activity (tau_bar = 120 s) from the baseline mean a0, which this script measures itself from a calibration run
(seed 777, 600 s, w fixed at 1): dw/dt = w * (a0 - abar) / (a0 * tau_w), clipped to [0.5, 2.0].
J_N is multiplied by f during a block (linear ramps of 30 s). The toy was written to ask whether a slow homeostatic
variable can reproduce a washout overshoot; it is tuned on nothing and cannot confirm the structure.
Predictions and decision rules: PREDICTIONS_HOMEOSTAT_TOY_FROZEN_BEFORE_RUN_SCI.md (hashed before the run).
`--smoke` is a 5 s code-path check; `--cell TAU D F OUT` runs one cell.
"""
import argparse
import json
import sys
import numpy as np

from rebound_oscillator import BASE, DT

BURN = 60.0
PRE = 600.0
RAMP = 30.0
SEED = 20261117
SEED_CAL = 777
N_NET = 20
TAU_BAR = 120.0
W_MIN, W_MAX = 0.5, 2.0
V_REF = -65.0
CL_O = 130.0


def run(mfun, T, N, seed, tau_w, a0):
    p = BASE
    rng = np.random.default_rng(seed)
    u = np.zeros(N); n = np.zeros(N); r = np.ones(N)
    c = np.full(N, p["c0"]); a = np.zeros(N); h = np.ones(N); eta = np.zeros(N)
    w = np.ones(N); abar = np.full(N, a0 if a0 is not None else 0.0)
    on = np.zeros(N, bool); t_on = np.zeros(N)
    res = [[] for _ in range(N)]
    wtrace = []
    umean = np.zeros(N)
    steps = int(T / DT)
    sq = np.sqrt(2 * DT / p["tau_eta"])
    e0 = -26.7 * np.log(CL_O / p["c0"])
    for s in range(steps):
        t = s * DT
        JN = p["J_N"] * mfun(t)
        G = (V_REF + 26.7 * np.log(CL_O / np.maximum(c, 0.5))) / (V_REF - e0)
        vh = p["J_tonic"] * G * (1 + p["pam"]) * p["tonic_gaba"] + p["J_a"] * a + p["hcn_block"] * p["G_H"]
        psi = 1.0 / (1.0 + np.exp(-(vh - p["th_psi"]) / p["k_psi"]))
        x = (p["b0"] - p["J_tonic"] * G * (1 + p["pam"]) * p["tonic_gaba"] - p["J_a"] * a - p["hcn_block"] * p["G_H"]
             + p["J_T"] * h * psi
             + (1 - p["brake"]) * w * (p["J_A"] * r * u + JN * r * n) - p["J_I"] * (1 + p["pam"]) * p["phasic_gain"] * G * u + p["sigma"] * eta)
        S = 1.0 / (1.0 + np.exp(-x / p["k"]))
        u = u + DT * (-u + S) / p["tau_u"]
        n = n + DT * (-n + u) / p["tau_N"]
        r = r + DT * ((1 - r) / p["tau_r"] - p["kappa_r"] * u * r)
        c = c + DT * (p["kappa_c"] * (1 + p["load_coupling"] * p["pam"]) * u * np.maximum(G, 0.0) + (p["c0"] - c) / p["tau_c"])
        a = a + DT * (p["kappa_a"] * u - a / p["tau_a"])
        h = h + DT * ((1 - h) / p["tau_h"] - p["kappa_h"] * u * h)
        eta = eta - DT * eta / p["tau_eta"] + sq * rng.standard_normal(N)
        abar = abar + DT * (u - abar) / TAU_BAR
        if tau_w is not None and a0 is not None:
            w = np.clip(w + DT * w * (a0 - abar) / (a0 * tau_w), W_MIN, W_MAX)
        umean += u
        if s % 2500 == 0:
            wtrace.append((t, float(w.mean())))
        up = (~on) & (u > 0.5)
        dn = on & (u < 0.25)
        if up.any():
            on[up] = True; t_on[up] = t
        if dn.any():
            on[dn] = False
            for i in np.nonzero(dn)[0]:
                d = t - t_on[i]
                if d > 0.1:
                    res[i].append((t_on[i], d))
    return res, float(umean.mean() / steps), wtrace


def rate(res, t0, t1):
    n = sum(1 for lst in res for (o, d) in lst if t0 <= o < t1)
    return n / len(res) / ((t1 - t0) / 60.0)


def calibrate():
    _, a0, _ = run(lambda t: 1.0, BURN + 600.0, 10, SEED_CAL, None, None)
    return a0


def cell(tau, D, f, a0):
    t_dn0 = BURN + PRE; t_dn1 = t_dn0 + RAMP; t_up0 = t_dn1 + D; t_up1 = t_up0 + RAMP

    def m(t):
        if t < t_dn0:
            return 1.0
        if t < t_dn1:
            return 1.0 + (f - 1.0) * (t - t_dn0) / RAMP
        if t < t_up0:
            return f
        if t < t_up1:
            return f + (1.0 - f) * (t - t_up0) / RAMP
        return 1.0
    w3 = min(3 * tau, 7200.0)
    T = t_up1 + w3 + 600.0
    res, um, wt = run(m, T, N_NET, SEED, tau, a0)
    pre = rate(res, BURN, BURN + PRE)
    out = dict(tau_w=tau, D=D, f=f, a0=a0, rate_pre=pre, rate_hold=rate(res, t_dn1, t_up0),
               early=rate(res, t_up1, t_up1 + 120.0) / pre if pre > 0 else float("nan"),
               mid=rate(res, t_up1 + 120.0, t_up1 + 720.0) / pre if pre > 0 else float("nan"),
               w3_start=w3, late=rate(res, t_up1 + w3, t_up1 + w3 + 600.0) / pre if pre > 0 else float("nan"),
               w_max_seen=max(x[1] for x in wt), w_trace=wt[::max(1, len(wt) // 40)])
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Labelled toy: oscillator plus a slow homeostatic gain (hypothesis generator, not evidence).")
    ap.add_argument("--smoke", action="store_true", help="5 s code-path check; prints no statistic")
    ap.add_argument("--calibrate", action="store_true", help="print the baseline mean activity a0 and exit")
    ap.add_argument("--cell", nargs=4, metavar=("TAU", "D", "F", "OUT"), help="run one cell: tau_w (s), hold (s), block factor (1 = control), output JSON path")
    a = ap.parse_args(argv)
    if a.smoke:
        run(lambda t: 1.0, 5.0, 2, 1, 600.0, 0.1)
        print("smoke ok")
        return 0
    if a.calibrate:
        print(calibrate())
        return 0
    if a.cell:
        tau, D, f, out = float(a.cell[0]), float(a.cell[1]), float(a.cell[2]), a.cell[3]
        a0 = calibrate()
        json.dump(cell(tau, D, f, a0), open(out, "w"), indent=1)
        print("done")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
