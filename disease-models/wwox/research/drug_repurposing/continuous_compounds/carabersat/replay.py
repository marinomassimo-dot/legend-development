"""Replay the digitized analogue plot and compartment-scale sensitivities."""

import csv
from math import log
from pathlib import Path
from random import Random
from statistics import correlation


with Path(__file__).with_name("figure6_points.tsv").open(encoding="utf-8") as source:
    points = [(r["compound"], float(r["x_px"]), float(r["y_px"])) for r in csv.DictReader(source, delimiter="\t")]


def pki(x):
    return 5 + 3.5 * (x - 624) / (957 - 624)


def threshold_increase(y):
    return 150 * (1266 - y) / (1266 - 1016)


def pearson(series):
    return correlation([pki(x) for x, _ in series], [threshold_increase(y) for _, y in series])


def perturb(series, rng):
    return [(x + rng.uniform(-2, 2), y + rng.uniform(-2, 2)) for x, y in series]


def emit(label, statistic, value):
    print(f"{label}\t{statistic}\t{value:.4f}")


print("comparison\tmetric\tvalue")
for name, x, y in points:
    emit(name, "pKi_digitized", pki(x))
    emit(name, "percent_MEST_threshold_increase", threshold_increase(y))

series = [(x, y) for _, x, y in points]
for size in (12, 6, 4):
    subset = series[-size:]
    rng = Random(202)
    simulations = sorted(pearson(perturb(subset, rng)) for _ in range(5000))
    emit(f"top_{size}", "pearson_r", pearson(subset))
    emit(f"top_{size}", "pixel_jitter_p025", simulations[125])
    emit(f"top_{size}", "pixel_jitter_p975", simulations[4874])

loo = [pearson(series[:i] + series[i + 1:]) for i in range(len(series))]
emit("all_analogues", "leave_one_out_min_r", min(loo))
emit("all_analogues", "leave_one_out_max_r", max(loo))
emit("slice_midpoint_versus_homologous_Ki", "nominal_ratio", 200 / 48)
emit("slice_midpoint_versus_saturation_Kd", "nominal_ratio", 200 / 32)
emit("8.5_versus_2.5_mM_K_out_at_32_C", "Nernst_shift_mV", 8.314462618 * 305.15 / 96485.33212 * 1000 * log(8.5 / 2.5))
for free_fraction in (0.01, 0.10, 0.30, 1):
    # The reported 0.12 µmol/kg is total whole brain. Density of 1 kg/L is illustrative.
    emit(f"rat_total_120_nM_equivalent_free_fraction_{free_fraction:.2f}", "hypothetical_free_nM", 120 * free_fraction)
for reference in (32, 48, 200):
    emit(f"reference_{reference}_nM_over_120_nM_equivalent_total", "hypothetical_free_fraction_required", reference / 120)
