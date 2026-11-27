"""Recalculate Figure 3G count ratios and two published exposure scales."""

import argparse
import csv
from itertools import product
from pathlib import Path
import sys


def read_coordinates():
    with Path(__file__).with_name("figure_coordinates.tsv").open(newline="") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            yield (row["measure"], row["group"]), {
                col: int(row[col]) for col in ("x", "y_top", "y_zero", "y_tick", "tick_count")
            }


def check_image(pdf, points):
    import pymupdf

    with pymupdf.open(pdf) as document:
        image = pymupdf.Pixmap(document, 93)
        if (image.width, image.height) != (2140, 2462):
            raise ValueError("Unexpected raster size for Sy et al. Figure 3")
        for (_, group), point in points.items():
            for y in range(point["y_tick"], point["y_zero"]):
                red, green, blue = image.pixel(point["x"], y)[:3]
                is_control = group == "control" and red > 170 and green < 80 and blue < 100
                is_treated = group == "GlcNAc" and blue > 140 and red < 100 and green < 100
                if is_control or is_treated:
                    if y != point["y_top"]:
                        raise ValueError(f"Digitized y does not match image at x={point['x']}")
                    break
            else:
                raise ValueError(f"No bar color found for {point}")


def per_field(points, offsets):
    return {
        key: point["tick_count"] * (point["y_zero"] - point["y_top"] - offset)
        / (point["y_zero"] - point["y_tick"])
        for (key, point), offset in zip(points.items(), offsets)
    }


def fractions(counts):
    return [
        100 * counts["myelinated_axons", group] / counts["total_axons", group]
        for group in ("control", "GlcNAc")
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, help="Optionally validate the bar edges against the original PDF")
    args = parser.parse_args()
    points = dict(read_coordinates())
    if args.pdf:
        check_image(args.pdf, points)

    counts = per_field(points, [0] * len(points))
    control, treated = fractions(counts)
    differences = []
    for offsets in product((-2, 2), repeat=len(points)):
        perturbed_control, perturbed_treated = fractions(per_field(points, offsets))
        differences.append(perturbed_treated - perturbed_control)

    results = [
        (f"{measure}_{group}", count, "axons/105_um2_field")
        for (measure, group), count in counts.items()
    ]
    results.extend((
        ("control_myelinated_share_ratio_of_means", control, "percent"),
        ("GlcNAc_myelinated_share_ratio_of_means", treated, "percent"),
        ("myelinated_share_difference", treated - control, "percentage_points"),
        ("myelinated_share_minimum_two_pixel_sensitivity", min(differences), "percentage_points"),
        ("myelinated_share_maximum_two_pixel_sensitivity", max(differences), "percentage_points"),
        ("mouse_drinking_water_1_mg_mL", 1000 / 221.21, "mmol/L"),
        ("cell_bath_40mM_over_human_group_mean_plot_axis_max_2500nM", 40e6 / 2500, "ratio"),
        ("cell_bath_40mM_over_human_participant_average_plot_axis_max_8000nM", 40e6 / 8000, "ratio"),
    ))
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "value", "unit"))
    writer.writerows((name, f"{value:.3f}", unit) for name, value, unit in results)


if __name__ == "__main__":
    main()
