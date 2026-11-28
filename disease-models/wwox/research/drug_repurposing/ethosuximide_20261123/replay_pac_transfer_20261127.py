"""Separate synthetic spike-driven PAC from residual phase-gated gamma."""
import csv
from pathlib import Path

import numpy as np


FS = 512
CYCLE_SAMPLES = 640
CYCLES = 96
BINS = 20
T = np.arange(CYCLE_SAMPLES) / FS - CYCLE_SAMPLES / (2 * FS)
OUT = Path(__file__).with_name("results")


def analytic_gamma(signal):
    frequencies = np.fft.fftfreq(signal.size, 1 / FS)
    gamma = (frequencies >= 40) & (frequencies <= 80)
    return np.fft.ifft(2 * gamma * np.fft.fft(signal))


def modulation_index(analytic_signal):
    amplitude = np.abs(analytic_signal).reshape(CYCLES, CYCLE_SAMPLES)
    bins = amplitude.mean(axis=0).reshape(BINS, CYCLE_SAMPLES // BINS).mean(axis=1)
    distribution = bins / bins.sum()
    return np.sum(distribution * np.log(distribution * BINS)) / np.log(BINS)


def simulate(seed, condition, jitter_ms, amplitude_cv):
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, 0.35, (CYCLES, CYCLE_SAMPLES))
    slow = np.cos(2 * np.pi * 0.8 * T)
    scale = 1 + amplitude_cv * rng.normal(size=(CYCLES, 1))
    delay = (jitter_ms / 1000) * rng.normal(size=(CYCLES, 1))
    spike = 2.0 * scale * np.exp(-0.5 * ((T - delay) / 0.005) ** 2)
    random_carrier_phase = rng.uniform(0, 2 * np.pi, size=(CYCLES, 1))
    gamma = 0.5 * np.exp(-0.5 * (T / 0.075) ** 2) * np.sin(2 * np.pi * 60 * T + random_carrier_phase)
    signal = noise + slow
    if condition in {"spike_only", "spike_plus_gated_gamma"}:
        signal += spike
    if condition in {"gated_gamma", "spike_plus_gated_gamma"}:
        signal += gamma
    analytic = analytic_gamma(signal.ravel()).reshape(CYCLES, CYCLE_SAMPLES)
    residual = analytic - analytic.mean(axis=0)
    return modulation_index(analytic), modulation_index(residual)


def write_table(path, header, rows):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def main():
    rows = []
    for condition in ("slow_only", "spike_only", "gated_gamma", "spike_plus_gated_gamma"):
        for jitter_ms, amplitude_cv in ((0, 0), (5, .30), (15, .30)):
            outcomes = np.array([simulate(seed, condition, jitter_ms, amplitude_cv) for seed in range(32)])
            summary = [f"{x:.6f}" for quantile in (0.5, 0.05, 0.95) for x in np.quantile(outcomes, quantile, axis=0)]
            rows.append((condition, jitter_ms, amplitude_cv, 32, *summary))
    write_table(OUT / "pac_waveform_transfer_20261127.tsv",
                ("signal", "spike_jitter_ms", "spike_amplitude_cv", "seeds",
                 "raw_median", "residual_median", "raw_p05", "residual_p05", "raw_p95", "residual_p95"), rows)

    # Sahu et al. prospective D/EE-SWAS study reports only these marginal counts.
    # These are sharp logical bounds without assuming repeated endpoints coincide.
    n = 39
    seizure_free = 28
    pairs = (("seizure_free_and_EEG_improved", 29), ("seizure_free_and_EEG_normalized", 8),
             ("seizure_free_without_EEG_normalization", n - 8))
    write_table(OUT / "swas_endpoint_bounds_20261127.tsv", ("outcome", "n", "seizure_free", "other", "min", "max"),
                ((name, n, seizure_free, other, max(0, seizure_free + other - n), min(seizure_free, other))
                 for name, other in pairs))


if __name__ == "__main__":
    main()
