"""Replay a published-figure readback and conditional, matched-geometry predictions."""

import csv
from pathlib import Path
import sys


def read_panel_values(path):
    with path.open(newline="") as source:
        for row in csv.DictReader(source, delimiter="\t"):
            bottom = int(row["axis_zero_y"])
            scale = float(row["axis_top_value"]) / (bottom - int(row["axis_top_y"]))
            control = (bottom - int(row["control_y"])) * scale
            knockout = (bottom - int(row["knockout_y"])) * scale
            yield row["metric"], row["unit"], control, knockout, scale


def main():
    path = Path(__file__).with_name("propagation_readback.tsv")
    measurements = {metric: (unit, control, knockout, scale)
                    for metric, unit, control, knockout, scale in read_panel_values(path)}
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("comparison", "point_or_model", "unit", "estimate",
                  "readback_low", "readback_high"))
    for metric, (unit, control, knockout, scale) in measurements.items():
        bar_error = 2 * scale  # Allow two pixels on each horizontal summary line.
        for group, value in (("S-Control", control), ("S-KO", knockout)):
            out.writerow((metric, group, unit, f"{value:.3f}",
                          f"{value - bar_error:.3f}", f"{value + bar_error:.3f}"))

    _, control, knockout, scale = measurements["N1_latency"]
    n1_gap = knockout - control
    gap_error = 4 * scale
    for distance in (0.5, 1.0, 1.5, 2.0):
        for model, factor in (("fixed_offset", 1.0), ("propagation_only", distance)):
            out.writerow((f"N1_gap_at_{distance:g}_times_reference_path", model, "ms",
                          f"{factor * n1_gap:.3f}", f"{factor * (n1_gap - gap_error):.3f}",
                          f"{factor * (n1_gap + gap_error):.3f}"))

    _, control, knockout, scale = measurements["N1_over_N2_amplitude"]
    ratio_of_plotted_ratios = knockout / control
    ratio_error = 2 * scale
    low = (knockout - ratio_error) / (control + ratio_error)
    high = (knockout + ratio_error) / (control - ratio_error)
    for model, value, lower, upper in (
        ("N1_change_if_N2_fixed", ratio_of_plotted_ratios, low, high),
        ("N2_change_if_N1_fixed", 1 / ratio_of_plotted_ratios, 1 / high, 1 / low),
    ):
        out.writerow(("conditional_amplitude_example", model, "KO_over_control",
                      f"{value:.3f}", f"{lower:.3f}", f"{upper:.3f}"))


if __name__ == "__main__":
    main()
