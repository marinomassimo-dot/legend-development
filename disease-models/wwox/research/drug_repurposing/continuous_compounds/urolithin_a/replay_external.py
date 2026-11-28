"""Replay selected primary urolithin A comparisons from source cells and reported counts."""

import argparse
import csv
from math import comb, exp, lgamma, log, log1p, pi, sqrt
from pathlib import Path
from statistics import mean
import sys
from zipfile import ZipFile
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[6] / "framework" / "scripts"))
from xlsx_to_text import sheet_names


def numeric_cells(workbook, tab):
    sheet = dict(sheet_names(workbook))[tab]
    cells = {}
    for entry in ET.fromstring(workbook.read(sheet)).iterfind(".//{*}c"):
        value = entry.findtext("{*}v")
        if value is not None and entry.get("t") in (None, "n"):
            cells[entry.attrib["r"]] = float(value)
    return cells


def column(cells, letter, first, last):
    return [cells[f"{letter}{row}"] for row in range(first, last + 1)]


def exact_test(control_events, exposed_events, group_size):
    total_events = control_events + exposed_events
    minimum = max(0, total_events - group_size)
    maximum = min(group_size, total_events)
    weights = {
        n: comb(total_events, n) * comb(2 * group_size - total_events, group_size - n)
        for n in range(minimum, maximum + 1)
    }
    observed = weights[control_events]
    return sum(weight for weight in weights.values() if weight <= observed) / comb(2 * group_size, group_size)


def f_tail_one_numerator_df(statistic, denominator_df):
    # With one numerator degree of freedom, F has the distribution of squared t.
    log_constant = (
        lgamma((denominator_df + 1) / 2)
        - lgamma(denominator_df / 2)
        - log(denominator_df * pi) / 2
    )
    width = sqrt(statistic) / 10_000
    area = width * sum(
        exp(log_constant - (denominator_df + 1) / 2 * log1p(((i + 0.5) * width) ** 2 / denominator_df))
        for i in range(10_000)
    )
    return 1 - 2 * area


def assay_contrasts(workbook):
    fig4 = numeric_cells(workbook, "Figure 4")
    for panel, tissue, first in (("4b", "neuroretina", 3), ("4c", "RPE", 20)):
        for age, letter, size in (("young", "A", 5), ("old", "B", 7)):
            treated = column(fig4, letter, first, first + size - 1)
            yield panel, f"{tissue}, {age} UA", "fold of own vehicle reference", "", size, "", mean(treated), "", ""
    for age, a, b, n_a, n_b in (("young", "A", "B", 5, 5), ("old", "C", "D", 6, 7)):
        ctrl = column(fig4, a, 37, 36 + n_a)
        test = column(fig4, b, 37, 36 + n_b)
        yield "4d", f"{age} UA vs vehicle", "hindlimb clasping score", n_a, n_b, mean(ctrl), mean(test), mean(test) - mean(ctrl), ""

    fig7 = numeric_cells(workbook, "Figure 7")
    for panel, unit, first in (
        ("7b", "mitolysosomes/cell", 3),
        ("7e", "cytosolic DNA foci/cell", 39),
    ):
        differences = []
        for ctrl_col, test_col, condition in (
            ("C", "D", "ABT"),
            ("G", "H", "ABT plus dual PINK1/PRKN knockdown"),
        ):
            ctrl = column(fig7, ctrl_col, first, first + 3)
            test = column(fig7, test_col, first, first + 3)
            difference = mean(test) - mean(ctrl)
            differences.append(difference)
            yield panel, f"UA addition at {condition}", unit, 4, 4, mean(ctrl), mean(test), difference, ""
        yield panel, "change in UA effect under dual knockdown", unit, "", "", "", "", differences[1] - differences[0], ""

    for endpoint, exposed_events in (("any visible seizure", 4), ("tonic-clonic", 3)):
        probability = exact_test(7, exposed_events, 7)
        yield "Mishra 3e", endpoint, "animal event fraction", 7, 7, 1, exposed_events / 7, exposed_events / 7 - 1, probability

    printed_brain_micrograms_per_mg = 0.31
    aliquot_micrograms = printed_brain_micrograms_per_mg * 350
    yield "Jiménez-Loygorri 4a", "mass in 350 mg if printed axis literal", "micrograms", "", "", "", aliquot_micrograms, "", ""
    yield "Jiménez-Loygorri 4a", "mouse mass to supply calculated aliquot at 5 mg/kg", "grams", "", "", "", aliquot_micrograms / 5, "", ""
    yield "Monsalve Acevedo Results", "tail probability implied by printed F(1,15.27)=0.661", "p", "", "", "", f_tail_one_numerator_df(0.661, 15.27), "", ""

    parent_um = 1.038 / 228.20
    glucuronide_um = 1014 / 404.3
    yield "Liu month 4", "adult plasma aglycone", "micromolar", "", "", "", parent_um, "", ""
    yield "Liu month 4", "adult plasma glucuronide", "micromolar", "", "", "", glucuronide_um, "", ""
    yield "Mishra vs Liu", "50 uM bath/adult total unconjugated plasma", "concentration ratio", "", "", "", 50 / parent_um, "", ""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jimenez_workbook", type=Path)
    args = parser.parse_args()
    with ZipFile(args.jimenez_workbook) as workbook:
        writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
        writer.writerow(("panel", "contrast", "unit", "ctrl_n", "test_n", "ctrl", "test", "test_minus_ctrl", "two_sided_fisher"))
        for row in assay_contrasts(workbook):
            values = (f"{value:.7g}" if isinstance(value, float) else value for value in row)
            writer.writerow("NA" if value == "" else value for value in values)


if __name__ == "__main__":
    main()
