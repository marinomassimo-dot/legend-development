"""Replay peer-checkable sensitivity and exposure calculations with the standard library."""
import argparse
import csv
import math
from pathlib import Path


def write_tsv(path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)


def pulse_peak(source, transfer, removal):
    return source * transfer * -math.expm1(-removal) / removal


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    output = parser.parse_args().output
    output.mkdir(parents=True, exist_ok=True)

    base_source, base_transfer, base_removal = 1.0, 0.4, 1.0
    slow_removal = 0.25
    target_peak = pulse_peak(base_source, base_transfer, slow_removal)
    peak_ratio = target_peak / pulse_peak(base_source, base_transfer, base_removal)
    scenarios = (
        ("baseline", base_source, base_transfer, base_removal),
        ("higher_transfer", base_source, base_transfer * peak_ratio, base_removal),
        ("larger_source", base_source * peak_ratio, base_transfer, base_removal),
        ("slower_removal", base_source, base_transfer, slow_removal),
    )
    rows = []
    for label, source, transfer, removal in scenarios:
        peak = pulse_peak(source, transfer, removal)
        values = source, transfer, removal, peak, math.log(2) / removal, peak / removal
        rows.append((label, *(f"{value:.6f}" for value in values)))
    write_tsv(
        output / "pulse_sensitivity.tsv",
        ("scenario", "source_area", "transfer_gain", "removal", "matrix_peak",
         "postpulse_half_life", "postpulse_area"),
        rows,
    )

    mw_parent = 281.42
    exposures = (
        ("Grachev single exposure pool", 589),
        ("PRIDE-HD steady state as cited by Grachev", 618),
    )
    rows = []
    for label, total_ng_ml in exposures:
        total_um = total_ng_ml / mw_parent
        rows.append((label, total_ng_ml, mw_parent, f"{total_um:.6f}",
                     f"{1 / total_um:.6f}", f"{5 / total_um:.6f}"))
    write_tsv(
        output / "exposure_replay.tsv",
        ("adult_cohort", "total_plasma_ng_mL", "parent_g_mol", "total_plasma_uM",
         "nominal_1uM_over_adult_total", "nominal_5uM_over_adult_total"),
        rows,
    )


if __name__ == "__main__":
    main()
