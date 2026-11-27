"""Replay the source-table arithmetic and digitize the published mouse graph."""
import argparse
from csv import DictReader, writer
from hashlib import sha256
from math import sqrt
from pathlib import Path
from statistics import median
from subprocess import check_output
import sys


def clinical_rows():
    # Bottiglieri et al., p. 1097, Table 3. The four paired values were not reported.
    for compartment, before, after, sd_before, sd_after, paired_t in (
        ("CSF", 35.5, 66.0, 13.8, 10.9, 7.24),
        ("plasma", 33.6, 135.4, 4.5, 68.3, 6.33),
    ):
        yield "Bottiglieri Table 3", compartment, "mean_change", after - before, "ng/mL"
        yield "Bottiglieri Table 3", compartment, "change_over_pre_mean", (after / before - 1) * 100, "%"
        yield "Bottiglieri Table 3", compartment, "paired_sd_required_by_reported_t", sqrt(4) * (after - before) / paired_t, "ng/mL"
        yield "Bottiglieri Table 3", compartment, "minimum_paired_sd_at_any_correlation", abs(sd_before - sd_after), "ng/mL"
        yield "Bottiglieri Table 3", compartment, "maximum_paired_t_at_any_correlation", sqrt(4) * (after - before) / abs(sd_before - sd_after), "t"
    yield "Cameron Table 6", "plasma", "fasted_MSI195_vs_commercial_dose_corrected_AUCt", (9434.4 / 800) / (6643.8 / 1600), "ratio"
    yield "Cameron Table 6", "plasma", "MSI195_fed_vs_fasted_AUCt", 5224.7 / 9434.4, "ratio"


def mouse_figure(path):
    expected = "0c2c8b00e9fa736aefd575b443ca97d06e7fdaf3f3c748e83a5bcaedd5f2bc4f"
    if sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError("Expected the indexed Fig. 6 raster")
    pixels = check_output(["convert", str(path), "-depth", "8", "RGB:-"])
    width = 673

    def matches(x, y, condition):
        offset = (y * width + x) * 3
        red, green, blue = pixels[offset:offset + 3]
        if condition == "control":
            return 92 < red < 184 and max(red, green, blue) - min(red, green, blue) < 17
        if condition == "low_SAM_food_arm":
            return red > 210 and 85 < green < 182 and 80 < blue < 190 and red - green > 65
        return red > 195 and green < 70 and blue < 70

    # Axis-zero and top-tick rows read from the original Fig. 6c raster. Each
    # bar top uses median across seven adjacent pixel columns to avoid markers.
    for endpoint, centers, search_begin, axis_zero, axis_two, unit in (
        ("SAM", (634, 648, 662), 478, 616, 449, "relative peak area"),
        ("SAH", (583, 597, 612), 494, 616, 449, "relative peak area"),
        ("SAM_to_SAH", (436, 463, 489), 721, 822, 693, "reported ratio"),
    ):
        for center, condition in zip(centers, ("control", "low_SAM_food_arm", "high_SAM_food_arm"), strict=True):
            edges = [next(y for y in range(search_begin, axis_zero - 8)
                          if all(matches(x, yy, condition) for yy in range(y, y + 8)))
                     for x in range(center - 3, center + 4)]
            value = 2 * (axis_zero - median(edges)) / (axis_zero - axis_two)
            yield "Fustin Figure 6c", endpoint, condition, round(value, 1), unit


def wwo_mouse_rows(root):
    for rel, gene, total_field in (("creatine/nuclei.tsv", "Gamt", "all_UMI"),
                                   ("betaine/cell_types.tsv", "Mat2a", "total_UMI")):
        with (root / rel).open() as stream:
            for row in DictReader(stream, delimiter="\t"):
                if row["gene"] == gene and row["class"] in {"exc", "astro", "NFOL", "MFOL", "MOL"}:
                    unit = "CPM in class of one P17 hippocampal nuclei pool per genotype"
                    yield "GSE158684 replay", gene, f'{row["pool"]}_{row["class"]}', 1e6 * int(row["gene_UMI"]) / int(row[total_field]), unit


def enzyme_examples():
    # Normalized competitive toy model at fixed GAA. These are dimensionless
    # counterexamples, deliberately independent of cross-matrix kinetic values.
    for sam, sah in ((0.4, 0.1), (4, 1), (40, 10)):
        yield "normalized sensitivity", "GAMT", f"SAM/Km={sam};SAH/Ki={sah}", sam / (1 + sam + sah), "fraction of Vmax"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fig6", type=Path)
    args = parser.parse_args()
    out = writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("source", "compartment_or_target", "measure", "value", "unit"))
    root = Path(__file__).resolve().parents[1]
    for data in (clinical_rows(), mouse_figure(args.fig6), wwo_mouse_rows(root), enzyme_examples()):
        for source, target, measure, value, unit in data:
            out.writerow((source, target, measure, f"{value:.5g}", unit))


if __name__ == "__main__":
    main()
