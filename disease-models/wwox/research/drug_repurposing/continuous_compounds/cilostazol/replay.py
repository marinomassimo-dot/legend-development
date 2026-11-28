"""Recompute the figure readout, marker-fate counterexample and exposure comparison."""
import argparse
import csv
from pathlib import Path


def write_tsv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)


def figure_and_fate(output):
    file = Path(__file__).with_name("figure_coordinates.tsv")
    with file.open(encoding="utf-8") as handle:
        points = list(csv.DictReader(handle, delimiter="\t"))

    measured = []
    fate = []
    for point in points:
        top, bottom, full = (int(point[key]) for key in ("y_px", "y0_px", "y100_px"))
        fraction = (bottom - top) / (bottom - full)
        condition, marker = point["condition"], point["marker"]
        measured.append((condition, marker, f"{100 * fraction:.2f}"))
        if marker == "GST-pi":
            # Identical fate decisions in each arm, with different survival after transition.
            original, true_transitions = 100, 60
            live_other = original - true_transitions
            live_mature = live_other * fraction / (1 - fraction)
            fate.append((condition, original, true_transitions, live_other, f"{live_mature:.2f}",
                         f"{live_mature + live_other:.2f}", f"{100 * fraction:.2f}"))

    write_tsv(output / "figure_replay.tsv", ("condition", "marker", "percent_of_BrdU_digitized"),
              measured)
    write_tsv(output / "fate_counterexample.tsv",
              ("condition", "original", "true_transitions", "live_other", "live_mature_expected",
               "live_BrdU_expected", "mature_percent"), fate)


def exposure(output):
    parent_mass = 369.46
    parent_cmax = (("test", 635.6), ("reference", 623.3))
    rows = []
    for arm, ng_ml in parent_cmax:
        total = ng_ml / parent_mass
        free_low, free_high = total * 0.02, total * 0.05
        for bath in (1, 3, 10):
            rows.append((arm, ng_ml, f"{total:.4f}", f"{free_low:.4f}", f"{free_high:.4f}",
                         bath, f"{bath / free_high:.1f}", f"{bath / free_low:.1f}"))
    write_tsv(output / "exposure_replay.tsv",
              ("adult_crossover_arm", "parent_ng_mL", "total_uM", "illustrative_free_low_uM",
               "illustrative_free_high_uM", "nominal_OPC_bath_uM",
               "nominal_over_adult_free_low_ratio", "nominal_over_adult_free_high_ratio"),
              rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    output = parser.parse_args().output
    output.mkdir(parents=True, exist_ok=True)
    figure_and_fate(output)
    exposure(output)


if __name__ == "__main__":
    main()
