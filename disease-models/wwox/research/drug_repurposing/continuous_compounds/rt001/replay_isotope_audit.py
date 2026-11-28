"""Calculate scoped figure contrasts and a free-substrate competition null."""

from collections import defaultdict
import csv
from itertools import product
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PIXEL_MARGIN = 2


def calibrated_height(row, pixel_shift):
    zero = int(row["axis_zero_y"])
    reference = int(row["axis_reference_y"])
    bar = int(row["bar_y"])
    scale = float(row["axis_reference_ng_ml_or_ng_g"])
    return scale * (zero - bar + pixel_shift) / (zero - reference)


def figure_ratios():
    comparisons = defaultdict(dict)
    with (HERE / "figure_anchors.tsv").open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            comparisons[row["comparison"]][row["bar"]] = row
    for name, rows in comparisons.items():
        control = rows["control_light"]
        for bar, measured in rows.items():
            if bar == "control_light":
                continue
            fraction = measured["substrate_fraction"]
            normalize = fraction != "unknown"
            denominator = float(fraction) if normalize else 1.0
            value = calibrated_height(measured, 0) / calibrated_height(control, 0) / denominator
            low = calibrated_height(measured, -PIXEL_MARGIN) / calibrated_height(control, PIXEL_MARGIN) / denominator
            high = calibrated_height(measured, PIXEL_MARGIN) / calibrated_height(control, -PIXEL_MARGIN) / denominator
            label = "ratio_per_known_substrate" if normalize else "raw_reporter_ratio"
            yield name, bar, label, value, low, high, "pixel-height sensitivity only"


def competition_ratios():
    for enzyme, kh, kh_spread, kd, kd_spread in (
        ("human_15_lox_2", 18.0, 3.6, 20.9, 4.2),
        ("human_cox_2", 10.8, 4.1, 10.7, 3.5),
    ):
        fraction = 0.2
        for substrate in (5.0, 20.0, 100.0):
            def light_ratio(light_km, heavy_km):
                denominator = 1 + (1 - fraction) * substrate / light_km + fraction * substrate / heavy_km
                return (1 + substrate / light_km) / denominator

            bounds = [
                light_ratio(light_km, heavy_km)
                for light_km, heavy_km in product(
                    (kh - kh_spread, kh + kh_spread), (kd - kd_spread, kd + kd_spread)
                )
            ]
            yield (enzyme, f"20% heavy at {substrate:g} uM total",
                   "light_flux_per_light_substrate_ratio", light_ratio(kh, kd),
                   min(bounds), max(bounds), "reported Km spreads used as a sensitivity box")


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "condition", "statistic", "value", "sensitivity_low",
                     "sensitivity_high", "range_interpretation"))
    for rows in (figure_ratios(), competition_ratios()):
        for name, condition, value_type, estimate, low, high, scope in rows:
            writer.writerow((name, condition, value_type, f"{estimate:.4f}", f"{low:.4f}", f"{high:.4f}", scope))


if __name__ == "__main__":
    main()
