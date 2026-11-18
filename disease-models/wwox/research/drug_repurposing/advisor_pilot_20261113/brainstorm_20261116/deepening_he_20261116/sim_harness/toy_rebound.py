"""TOY model for the harness test only: a two-stage rebound oscillator with gamma-distributed intervals and durations. NOT SCI's model and NOT a claim about any biology."""
import numpy as np

PARAMS = {
    "J_T": [1.0, 0.2, 3.0, "trigger drive (1/s scale)"],
    "tau_c": [20.0, 5.0, 60.0, "chloride-like slow time constant (s)"],
    "stages_T": [1.4, 1.0, 4.0, "gamma shape of the interval"],
    "tau_N": [0.26, 0.05, 1.0, "duration scale (s)"],
    "pam": [0.0, 0.0, 2.0, "GABA-A positive modulation (aggravates in this toy)"],
}


def simulate(params, seed):
    rng = np.random.default_rng(seed)
    scale = params["tau_c"] / (params["J_T"] * (1.0 + 0.3 * params["pam"])) / params["stages_T"] * 1.0
    t, isi, dur = 0.0, [], []
    while t < 600.0:
        d = rng.gamma(params["stages_T"], scale); t += d; isi.append(d)
        dur.append(rng.gamma(2.5, params["tau_N"]))
    isi = np.array(isi[1:]) if len(isi) > 2 else np.array(isi)
    dur = np.array(dur)
    return {"isi_median_s": float(np.median(isi)), "isi_gamma_shape": float(np.mean(isi) ** 2 / np.var(isi)) if len(isi) > 2 else float("nan"),
            "dur_median_s": float(np.median(dur)), "n_bursts": float(len(dur)), "rate_per_min": float(len(dur) / 10.0)}
