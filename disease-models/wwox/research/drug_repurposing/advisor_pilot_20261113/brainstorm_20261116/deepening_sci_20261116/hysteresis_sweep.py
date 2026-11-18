#!/usr/bin/env python3
"""Hysteresis test of the I1 rebound oscillator under a time-varying NMDAR weight J_N.

HYPOTHESIS GENERATOR, NOT EVIDENCE. Mechanism-level only. No dose, no agent. Reference genotype class only.
numpy only; seeded. The protocol and the decision rules are in PREDICTIONS_HYSTERESIS_FROZEN_BEFORE_RUN_SCI.md,
which was hashed before this script was first run for results.

Part A: a transient reduction of J_N (linear ramp down over 30 s, hold D, linear ramp up over 30 s) and a
        comparison of the burst rate, burst duration and fraction of silent networks before and after.
Part B: a slow up-and-down ramp of J_N (1 -> 0.3 -> 1, each leg R seconds) and a comparison of the rate at the
        same J_N on the down leg and on the up leg.
`--smoke` runs a 5 s check of the code path and prints no statistic.
"""
import argparse
import json
import sys
import numpy as np

from rebound_oscillator import BASE, DT

N_NET = 40
BURN = 60.0
SEED_A = 20261117
SEED_B = 20261118
RAMP = 30.0
PRE = 600.0
EARLY = 120.0
LATE = 600.0
V_REF = -65.0
CL_O = 130.0


def run(mfun, T, N, seed):
    """Return per-network lists of (onset, duration) of bursts with duration > 0.1 s; J_N(t) = J_N0 * mfun(t)."""
    p = BASE
    rng = np.random.default_rng(seed)
    u = np.zeros(N); n = np.zeros(N); r = np.ones(N)
    c = np.full(N, p["c0"]); a = np.zeros(N); h = np.ones(N); eta = np.zeros(N)
    on = np.zeros(N, bool); t_on = np.zeros(N)
    res = [[] for _ in range(N)]
    steps = int(T / DT)
    sq = np.sqrt(2 * DT / p["tau_eta"])
    e0 = -26.7 * np.log(CL_O / p["c0"])
    for s in range(steps):
        t = s * DT
        JN = p["J_N"] * mfun(t)
        G = (V_REF + 26.7 * np.log(CL_O / np.maximum(c, 0.5))) / (V_REF - e0)
        x = (p["b0"] - p["J_tonic"] * G * (1 + p["pam"]) * p["tonic_gaba"] - p["J_a"] * a - p["hcn_block"] * p["G_H"]
             + p["J_T"] * h * (1.0 / (1.0 + np.exp(-((p["J_tonic"] * G * (1 + p["pam"]) * p["tonic_gaba"] + p["J_a"] * a + p["hcn_block"] * p["G_H"]) - p["th_psi"]) / p["k_psi"])))
             + (1 - p["brake"]) * (p["J_A"] * r * u + JN * r * n) - p["J_I"] * (1 + p["pam"]) * p["phasic_gain"] * G * u + p["sigma"] * eta)
        S = 1.0 / (1.0 + np.exp(-x / p["k"]))
        u = u + DT * (-u + S) / p["tau_u"]
        n = n + DT * (-n + u) / p["tau_N"]
        r = r + DT * ((1 - r) / p["tau_r"] - p["kappa_r"] * u * r)
        c = c + DT * (p["kappa_c"] * (1 + p["load_coupling"] * p["pam"]) * u * np.maximum(G, 0.0) + (p["c0"] - c) / p["tau_c"])
        a = a + DT * (p["kappa_a"] * u - a / p["tau_a"])
        h = h + DT * ((1 - h) / p["tau_h"] - p["kappa_h"] * u * h)
        eta = eta - DT * eta / p["tau_eta"] + sq * rng.standard_normal(N)
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
    return res


def window_stats(res, t0, t1):
    """Pooled burst rate (per min per network), median duration, per-network counts."""
    counts = []
    durs = []
    for lst in res:
        k = [d for (o, d) in lst if t0 <= o < t1]
        counts.append(len(k)); durs.extend(k)
    counts = np.array(counts)
    rate = counts.sum() / len(res) / ((t1 - t0) / 60.0)
    med = float(np.median(durs)) if durs else float("nan")
    return rate, med, counts


def boot_ratio(cnt_a, cnt_b, rng, nb=2000):
    """95% bootstrap interval over networks of sum(cnt_b)/sum(cnt_a) (paired by network)."""
    n = len(cnt_a)
    out = []
    for _ in range(nb):
        i = rng.integers(0, n, n)
        a = cnt_a[i].sum()
        out.append(cnt_b[i].sum() / a if a > 0 else np.nan)
    return np.nanquantile(out, [0.025, 0.975])


def sched_A(f, D):
    t_dn0 = BURN + PRE
    t_dn1 = t_dn0 + RAMP
    t_up0 = t_dn1 + D
    t_up1 = t_up0 + RAMP

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
    return m, dict(pre=(BURN, BURN + PRE), hold=(t_dn1, t_up0), early=(t_up1, t_up1 + EARLY),
                   late=(t_up1 + EARLY, t_up1 + EARLY + LATE), T=t_up1 + EARLY + LATE)


def part_A(N, log):
    rng = np.random.default_rng(1)
    out = {}
    for D in (60.0, 300.0, 1800.0):
        ctrl = None
        for f in (1.0, 0.5, 0.8):
            m, w = sched_A(f, D)
            res = run(m, w["T"], N, SEED_A)
            rp, dp, cp = window_stats(res, *w["pre"])
            rh, dh, ch = window_stats(res, *w["hold"])
            re_, de, ce = window_stats(res, *w["early"])
            rl, dl, cl = window_stats(res, *w["late"])
            silent = float(np.mean((cp >= 3) & (cl == 0)))
            row = dict(f=f, D=D, rate_pre=rp, rate_hold=rh, rate_early=re_, rate_late=rl,
                       dur_pre=dp, dur_hold=dh, dur_early=de, dur_late=dl, silent_frac=silent,
                       ratio_late=rl / rp if rp > 0 else float("nan"),
                       ratio_early=re_ / rp if rp > 0 else float("nan"),
                       ratio_hold=rh / rp if rp > 0 else float("nan"),
                       dur_ratio_late=dl / dp if dp == dp and dp > 0 else float("nan"))
            lo, hi = boot_ratio(cp, cl, rng)
            row["late_ratio_ci"] = [float(lo), float(hi)]
            if f == 1.0:
                ctrl = row
            else:
                row["ctrl_late_ratio_ci"] = ctrl["late_ratio_ci"]
                row["ctrl_dur_ratio_late"] = ctrl["dur_ratio_late"]
                row["ctrl_silent_frac"] = ctrl["silent_frac"]
            out[f"A_f{f}_D{int(D)}"] = row
            log(f"A f={f} D={int(D)} done")
    return out


def part_B(N, log):
    rng = np.random.default_rng(2)
    out = {}
    edges = np.round(np.arange(0.3, 1.0001, 0.1), 3)
    for R in (600.0, 2400.0):
        t0 = BURN + 120.0
        T = t0 + 2 * R + 60.0
        for kind in ("ramp", "ctrl"):
            def m(t, R=R, t0=t0, kind=kind):
                if kind == "ctrl":
                    return 1.0
                if t < t0:
                    return 1.0
                if t < t0 + R:
                    return 1.0 + (0.3 - 1.0) * (t - t0) / R
                if t < t0 + 2 * R:
                    return 0.3 + (1.0 - 0.3) * (t - t0 - R) / R
                return 1.0

            def mval(t, R=R, t0=t0):
                if t < t0 or t >= t0 + 2 * R:
                    return None
                if t < t0 + R:
                    return 1.0 + (0.3 - 1.0) * (t - t0) / R
                return 0.3 + (1.0 - 0.3) * (t - t0 - R) / R
            res = run(m, T, N, SEED_B)
            bins = []
            for b in range(len(edges) - 1):
                lo, hi = edges[b], edges[b + 1]
                dwell = R * (hi - lo) / 0.7
                dn = np.zeros(N); upc = np.zeros(N)
                for i, lst in enumerate(res):
                    for (o, d) in lst:
                        mv = mval(o)
                        if mv is None or not (lo <= mv < hi + (1e-9 if b == len(edges) - 2 else 0)):
                            continue
                        if o < t0 + R:
                            dn[i] += 1
                        else:
                            upc[i] += 1
                rd = dn.sum() / N / (dwell / 60.0)
                ru = upc.sum() / N / (dwell / 60.0)
                ratio = ru / rd if rd > 0 else float("nan")
                ci = [float("nan"), float("nan")]
                if dn.sum() > 0:
                    out_b = []
                    for _ in range(2000):
                        ii = rng.integers(0, N, N)
                        a = dn[ii].sum()
                        out_b.append(upc[ii].sum() / a if a > 0 else np.nan)
                    ci = [float(x) for x in np.nanquantile(out_b, [0.025, 0.975])]
                bins.append(dict(lo=float(lo), hi=float(hi), n_down=int(dn.sum()), n_up=int(upc.sum()),
                                 rate_down=rd, rate_up=ru, ratio=ratio, ci=ci))
            out[f"B_R{int(R)}_{kind}"] = bins
            log(f"B R={int(R)} {kind} done")
    return out


def decide(A, B):
    """Frozen decision rules (see the prediction file)."""
    outA = {}
    for k, r in A.items():
        if r["f"] == 1.0:
            continue
        lo, hi = r["ctrl_late_ratio_ci"]
        rate_flag = (not (0.75 <= r["ratio_late"] <= 1.33)) and (r["ratio_late"] < lo or r["ratio_late"] > hi)
        dur_flag = (not (0.75 <= r["dur_ratio_late"] <= 1.33)) and abs(np.log(r["dur_ratio_late"] / r["ctrl_dur_ratio_late"])) > np.log(1.25)
        sil_flag = r["silent_frac"] > 0.10 and r["silent_frac"] > r["ctrl_silent_frac"] + 0.05
        outA[k] = dict(rate_flag=bool(rate_flag), dur_flag=bool(dur_flag), silent_flag=bool(sil_flag),
                       hysteresis=bool(rate_flag or dur_flag or sil_flag))
    outB = {}
    for R in (600, 2400):
        flags = 0
        evaluable = 0
        for bd in B[f"B_R{R}_ramp"]:
            if bd["n_down"] >= 40 and bd["n_up"] >= 40:
                evaluable += 1
                if (not (0.75 <= bd["ratio"] <= 1.33)) and (bd["ci"][0] > 1.0 or bd["ci"][1] < 1.0):
                    flags += 1
        outB[f"R{R}"] = dict(evaluable_bins=evaluable, flagged_bins=flags, hysteresis=bool(flags >= 2))
    headline = (not any(v["hysteresis"] for v in outA.values())) and (not any(v["hysteresis"] for v in outB.values()))
    return outA, outB, bool(headline)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Hysteresis test of the I1 oscillator under a time-varying NMDAR weight (hypothesis generator, not evidence).")
    ap.add_argument("--smoke", action="store_true", help="5 s code-path check; prints no statistic")
    ap.add_argument("--out", default="hysteresis_result.json", help="result JSON path")
    ap.add_argument("--part", default="AB", choices=["A", "B", "AB"], help="which part to run; the decision rules need both, applied by --decide")
    ap.add_argument("--decide", nargs=2, metavar=("A_JSON", "B_JSON"), help="apply the frozen decision rules to two result files")
    a = ap.parse_args(argv)
    if a.smoke:
        res = run(lambda t: 1.0, 5.0, 2, 1)
        window_stats(res, 0.0, 5.0)
        print("smoke ok")
        return 0
    if a.decide:
        A = json.load(open(a.decide[0]))["A"]
        B = json.load(open(a.decide[1]))["B"]
        flagsA, flagsB, headline = decide(A, B)
        json.dump(dict(decisionA=flagsA, decisionB=flagsB, headline_no_hysteresis=headline), open(a.out, "w"), indent=1, default=float)
        print("decided")
        return 0
    log = lambda s: print(s, file=sys.stderr, flush=True)
    res = {}
    if "A" in a.part:
        res["A"] = part_A(N_NET, log)
    if "B" in a.part:
        res["B"] = part_B(N_NET, log)
    json.dump(res, open(a.out, "w"), indent=1, default=float)
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
