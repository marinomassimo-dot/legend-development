"""Reproduce figure readouts and descriptive recovery contrasts for OV329."""

import argparse
import csv
from math import log2
from pathlib import Path


# In the local full-height AES poster crop (see dossier), coordinates count from top left.
# Each row is the visual marker center or the upper edge of a mean bar, with no error-bar reading.
PANELS = (
    ("4B", "OV329", "single_30mg_kg", "brain_parent", "ng_mL_as_labeled", 546, 381, 20,
     ((0.5, 445, 476), (1, 470, 523), (2, 520, 535), (4, 619, 546))),
    ("4B", "OV329", "single_30mg_kg", "ABAT_activity", "pct_vehicle", 546, 396, 100,
     ((0, 420, 396), (0.5, 445, 421), (1, 470, 421), (2, 520, 440), (4, 619, 442))),
    ("5A", "OV329", "single_10mg_kg", "ABAT_activity", "pct_vehicle", 1127, 1018, 100,
     ((0, 159, 1019), (4, 198, 1034), (24, 237, 1065), (72, 276, 1045), (168, 315, 1030),
      (336, 354, 1028))),
    ("5C", "vigabatrin", "single_300mg_kg", "ABAT_activity", "pct_vehicle", 1304, 1190, 100,
     ((0, 171, 1192), (4, 231, 1221), (24, 289, 1214), (72, 348, 1192))),
)


def digitized():
    for panel, agent, cohort, measure, unit, zero_y, ref_y, ref_value, points in PANELS:
        scale = ref_value / (zero_y - ref_y)
        for hours, x, y in points:
            value = (zero_y - y) * scale
            flag = "vehicle_reference" if hours == 0 else "approximate_marker"
            if measure == "brain_parent" and hours == 4:
                flag = "at_plot_floor_LLOQ_unknown"
            yield panel, agent, cohort, measure, unit, hours, x, y, zero_y, ref_y, ref_value, value, flag


def recovery(points):
    estimates = {row[5]: row[11] for row in points if row[0] == "5A"}
    for first, last in ((24, 72), (72, 168), (24, 168)):
        early, late = 100 - estimates[first], 100 - estimates[last]
        # A small digitization perturbation must not be read as a sampling CI.
        for scenario, offset in (("central", 0), ("faster", 3), ("slower", -3)):
            initial, final = early + offset, late - offset
            half_time = (last - first) / log2(initial / final)
            yield first, last, scenario, initial, final, half_time


def contrasts():
    yield "mouse_ABAT_6d", 62.6, 100, "pct_vehicle", 62.6 / 100, "6_mice_each"
    yield "mouse_bulk_GABA_6d", 134, 100, "pct_vehicle", 134 / 100, "6_mice_each"
    yield "mouse_tonic_current_6d_vs_vehicle", 60.8, 9.7, "pA", 60.8 / 9.7, "15_cells_4_mice_vs_16_cells_5_mice"
    yield "mouse_tonic_current_6d_vs_1d", 60.8, 13.2, "pA", 60.8 / 13.2, "15_cells_4_mice_vs_8_cells_5_mice"
    for muscle, active, placebo, n in (("APB", -53, 24.9, "10_vs_4"), ("FDI", -44.3, 59.5, "15_vs_5")):
        normalized_active = 1 + active / 100
        normalized_placebo = 1 + placebo / 100
        yield f"adult_LICI150_{muscle}_day7_over_baseline", normalized_active, normalized_placebo, "ratio", normalized_active / normalized_placebo, n


def write_table(path, header, rows):
    with path.open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header.split())
        for row in rows:
            writer.writerow(f"{value:.4f}" if isinstance(value, float) else value for value in row)


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    points = list(digitized())
    write_table(out / "poster_digitization.tsv",
                "panel analyte cohort measure unit nominal_time_h x_px y_px zero_y_px reference_y_px reference_value estimate flag",
                points)
    write_table(out / "apparent_recovery.tsv",
                "start_h end_h digitization_scenario initial_deficit_pp final_deficit_pp apparent_half_time_h", recovery(points))
    write_table(out / "replayed_contrasts.tsv",
                "comparison numerator denominator unit descriptive_ratio experimental_units", contrasts())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    main(parser.parse_args().out)
