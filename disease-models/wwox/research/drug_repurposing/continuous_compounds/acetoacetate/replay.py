"""Reproduce the local figure readout and the slice recipe comparison."""

import csv
from pathlib import Path

DIRECTORY = Path(__file__).resolve().parent


def write_tsv(name, headers, rows):
    with (DIRECTORY / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(rows)


def midpoint(row, pixel_error=0):
    pixel = float(row["x_cross_px"]) + pixel_error
    low = float(row["x_left_px"])
    position = (pixel - low) / (float(row["x_right_px"]) - low)
    log_low = float(row["log10_left_M"])
    log_high = float(row["log10_right_M"])
    return 1000 * 10 ** (log_low + position * (log_high - log_low))


def main():
    with (DIRECTORY / "figure_coordinates.tsv").open(encoding="utf-8") as handle:
        inputs = list(csv.DictReader(handle, delimiter="\t"))
    write_tsv(
        "chloride_midpoints.tsv",
        ("acac_mM", "hill", "cl_midpoint_mM", "x_minus_2_px", "x_plus_2_px"),
        [
            (
                row["acac_mM"],
                row["hill"],
                *(f"{midpoint(row, error):.3f}" for error in (0, -2, 2)),
            )
            for row in inputs
        ],
    )

    def uptake(row, chloride):
        return 1 / (1 + (midpoint(row) / chloride) ** float(row["hill"]))

    rows = []
    for chloride in (4, 10, 20, 100):
        baseline = uptake(inputs[0], chloride)
        for row in inputs:
            normalized = uptake(row, chloride)
            rows.append((chloride, row["acac_mM"], f"{normalized:.4f}", f"{normalized / baseline:.4f}"))
    write_tsv(
        "chloride_sensitivity.tsv",
        ("external_assay_cl_mM", "acac_mM", "uptake_own_vmax", "ratio_to_baseline_normalized_uptake"),
        rows,
    )
    basal_chloride = 110 + 2.5 + 2 * 4 + 2 * 4
    write_tsv(
        "slice_replay.tsv",
        ("condition", "acac_mM_nominal", "lithium_mM_added", "cl_mM_recipe", "mEPSC_pA_mean", "mEPSC_pA_SEM", "n_reported"),
        [
            ("LiCl control", 0, 10, basal_chloride + 10, 9.03, 1.23, 15),
            ("LiAcAc", 10, 10, basal_chloride, 6.88, 0.69, 15),
        ],
    )


if __name__ == "__main__":
    main()
