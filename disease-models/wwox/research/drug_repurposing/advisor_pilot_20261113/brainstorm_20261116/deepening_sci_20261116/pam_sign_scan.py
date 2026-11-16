#!/usr/bin/env python3
"""I1: in which parameter regime does GABA-A potentiation AGGRAVATE (raise the burst rate) instead of suppress? Hypothesis generator, not evidence.
    python3 pam_sign_scan.py --help
    python3 pam_sign_scan.py run <out_tsv> [--n 160] [--seed S]
Draws n random parameter vectors (seeded) around the fitted baseline, widening the rebound gate (J_T, th_psi, k_psi), the tonic weight, the bias b0 and the
noise sigma; keeps those whose own baseline rate is 0.3 to 6 bursts/min with at least 12 bursts; then compares the rate with (a) phasic-only potentiation
(phasic_gain 1.5, benzodiazepine-like), (b) tonic-only potentiation (tonic_gaba 1.5, extrasynaptic-neurosteroid-like), (c) both (pam 0.5). Same seed for the pairs."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out"); ap.add_argument("--n", type=int, default=160)
    ap.add_argument("--seed", type=int, default=5); ap.add_argument("--T", type=float, default=500.0); ap.add_argument("--nrep", type=int, default=6); ap.add_argument("--coupling", type=float, default=0.0, help="1 = chloride load scales with the potentiation (the I6 assumption)")
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed); n = a.n
    base = {k: np.full(n, m.BASE[k]) for k in m.BASE}
    base["J_T"] = m.BASE["J_T"] * rng.uniform(0.5, 4.0, n)
    base["th_psi"] = rng.uniform(0.15, 0.6, n); base["k_psi"] = rng.uniform(0.05, 0.3, n)
    base["J_tonic"] = m.BASE["J_tonic"] * rng.uniform(0.5, 1.6, n)
    base["b0"] = m.BASE["b0"] + rng.uniform(-0.15, 0.25, n); base["sigma"] = m.BASE["sigma"] * rng.uniform(0.8, 1.8, n)
    base["kappa_c"] = m.BASE["kappa_c"] * rng.uniform(0.5, 5.0, n); base["tau_c"] = m.BASE["tau_c"] * rng.uniform(0.5, 4.0, n)
    base["load_coupling"] = np.full(n, a.coupling)
    conds = {"base": {}, "phasic": {"phasic_gain": 1.5}, "tonic": {"tonic_gaba": 1.5}, "both": {"pam": 0.5}}
    out = {}
    for ci, (cn, ch) in enumerate(conds.items()):
        P = {k: v.copy() for k, v in base.items()}
        for k, v in ch.items():
            P[k] = np.full(n, v)
        out[cn] = m.stats(P, a.T, a.seed * 10, a.nrep)
    cols = ["kappa_c_x", "tau_c_x", "J_T_x", "th_psi", "k_psi", "J_tonic_x", "b0", "sigma", "rate_base", "n_base", "rate_phasic", "rate_tonic", "rate_both", "dur_base", "dur_both", "ratio_both", "class_both"]
    rows = []
    for i in range(n):
        rb = out["base"][i]["rate_per_min"]; nb = out["base"][i]["n_bursts"]
        if not (0.3 <= rb <= 6.0 and nb >= 12):
            continue
        rt = {c: out[c][i]["rate_per_min"] for c in ("phasic", "tonic", "both")}
        ratio = rt["both"] / rb
        cl = "AGGRAVATES" if ratio > 1.25 else ("suppresses" if ratio < 0.75 else "neutral")
        rows.append([base["kappa_c"][i] / m.BASE["kappa_c"], base["tau_c"][i] / m.BASE["tau_c"], base["J_T"][i] / m.BASE["J_T"], base["th_psi"][i], base["k_psi"][i], base["J_tonic"][i] / m.BASE["J_tonic"], base["b0"][i], base["sigma"][i], rb, nb,
                     rt["phasic"], rt["tonic"], rt["both"], out["base"][i]["dur_med"], out["both"][i]["dur_med"], ratio, cl])
    with open(a.out, "w") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(f"{x:.3f}" if isinstance(x, (float, np.floating)) else str(x) for x in r) + "\n")
    cnt = {c: sum(1 for r in rows if r[-1] == c) for c in ("AGGRAVATES", "neutral", "suppresses")}
    print("kept", len(rows), "of", n, cnt)
    return 0
if __name__ == "__main__":
    sys.exit(main())
