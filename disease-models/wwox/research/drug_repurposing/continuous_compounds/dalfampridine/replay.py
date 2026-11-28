"""Rebuild source comparisons and a synthetic recruitment counterexample.

Run with Python 3 and an output directory. Inputs are the two checked-in TSVs.
The estimate from plot pixels is a group-mean readback, not an animal-level fit.
"""
from __future__ import annotations

import argparse
import csv
from math import exp
from pathlib import Path
from statistics import linear_regression

HERE = Path(__file__).resolve().parent
MOLECULAR_WEIGHT = 94.11
CHRONIC_INJURY_BATH_UM = (0.5, 1.0)
BAR_EDGE_UNCERTAINTY_PX = 2.0


def rows(filename: str):
    with (HERE / filename).open(encoding="utf-8", newline="") as source:
        yield from csv.DictReader(source, delimiter="\t")


def tsv(path: Path, header, values):
    with path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.writer(target, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(values)


def replay_exposure(out: Path):
    converted = []
    for row in rows("exposure_inputs.tsv"):
        low = float(row["low_ng_ml"]) / MOLECULAR_WEIGHT
        high = float(row["high_ng_ml"]) / MOLECULAR_WEIGHT
        if row["free_low"]:
            free_low = low * float(row["free_low"])
            free_high = high * float(row["free_high"])
            free = [f"{v:.4f}" for v in (free_low, free_high)]
            bridge = [
                f"{CHRONIC_INJURY_BATH_UM[0] / free_high:.2f}",
                f"{CHRONIC_INJURY_BATH_UM[1] / free_low:.2f}",
            ]
        else:
            free = ["NA", "NA"]
            bridge = ["NA", "NA"]
        converted.append(
            [row["source"], row["compartment"], row["statistic"],
             f"{low:.4f}", f"{high:.4f}", *free, *bridge]
        )
    tsv(
        out / "exposure.tsv",
        ("source", "compartment", "statistic", "total_low_uM", "total_high_uM",
         "free_plasma_low_uM", "free_plasma_high_uM",
         "nominal_bath_to_free_plasma_low", "nominal_bath_to_free_plasma_high"),
        converted,
    )


def replay_figure(out: Path):
    means = {}
    display_per_pixel = {}
    for row in rows("figure6_pixels.tsv"):
        bottom = int(row["y_zero"])
        scale = float(row["top_tick_m_s"]) / (bottom - int(row["y_top_tick"]))
        means.setdefault(row["panel"], {})[row["group"]] = (bottom - int(row["y_bar"])) * scale
        display_per_pixel[row["panel"]] = scale

    group_order = ("sham_vehicle", "sham_dalfampridine", "tbi_vehicle", "tbi_dalfampridine")
    comparisons = []
    for panel, group in means.items():
        sham_shift = group["sham_dalfampridine"] - group["sham_vehicle"]
        injury_shift = group["tbi_dalfampridine"] - group["tbi_vehicle"]
        interaction = injury_shift - sham_shift
        edge = 4 * BAR_EDGE_UNCERTAINTY_PX * display_per_pixel[panel]
        values = [*(group[name] for name in group_order), sham_shift, injury_shift, interaction,
                  interaction - edge, interaction + edge]
        comparisons.append([panel, *(f"{v:.3f}" for v in values)])
    tsv(
        out / "figure6_readback.tsv",
        ("panel", "sham_vehicle_m_s", "sham_dalfampridine_m_s", "tbi_vehicle_m_s",
         "tbi_dalfampridine_m_s", "sham_shift_m_s", "tbi_shift_m_s",
         "interaction_m_s", "pixel_only_low_m_s", "pixel_only_high_m_s"),
        comparisons,
    )


def replay_recruitment(out: Path):
    distances = (0.4, 0.8, 1.2, 1.6)
    time_grid = [step / 1000 for step in range(5001)]
    widths_ms = 0.24
    rows_out = []

    for label, fast_weight, fast_speed, slow_speed in (
        ("baseline", 0.2, 0.8, 0.5),
        ("recruitment_only", 0.8, 0.8, 0.5),
        ("same_weights_faster_axons", 0.2, 1.28, 0.8),
    ):
        peaks = []
        for distance in distances:
            fast_arrival = 0.2 + distance / fast_speed
            slow_arrival = 0.2 + distance / slow_speed

            def field(t):
                fast = exp(-0.5 * ((t - fast_arrival) / widths_ms) ** 2)
                slow = exp(-0.5 * ((t - slow_arrival) / widths_ms) ** 2)
                return fast_weight * fast + (1 - fast_weight) * slow

            peaks.append(max(time_grid, key=field))
        slope, intercept = linear_regression(distances, peaks)
        rows_out.append(
            [label, fast_weight, fast_speed, slow_speed, 1.0,
             *(f"{v:.3f}" for v in peaks), f"{intercept:.3f}", f"{1 / slope:.3f}"]
        )
    tsv(
        out / "recruitment_control.tsv",
        ("synthetic_case", "fast_trace_weight", "true_fast_m_s", "true_slow_m_s",
         "sum_component_weights", *(f"peak_ms_at_{x:.1f}_mm" for x in distances),
         "fitted_intercept_ms", "apparent_peak_speed_m_s"),
        rows_out,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=HERE)
    out = parser.parse_args().out
    out.mkdir(parents=True, exist_ok=True)
    replay_exposure(out)
    replay_figure(out)
    replay_recruitment(out)


if __name__ == "__main__":
    main()
