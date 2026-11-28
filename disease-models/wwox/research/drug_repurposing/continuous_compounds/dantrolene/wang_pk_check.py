"""Audit Fig. 1 concentration/AUC workbook identities and exposure intervals."""

import argparse
import csv
from io import BytesIO
from pathlib import Path
from statistics import mean
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile


def sheet_cells(archive, name):
    with ZipFile(BytesIO(archive.read(name))) as workbook:
        root = ET.fromstring(workbook.read("xl/worksheets/sheet1.xml"))
    return {
        cell.attrib["r"]: float(cell.findtext("{*}v"))
        for cell in root.iterfind(".//{*}c")
        if cell.get("t") in (None, "n") and cell.findtext("{*}v") is not None
    }


def auc(points):
    return sum(
        (end - start) * (low + high) / 2
        for (start, low), (end, high) in zip(points, points[1:])
    )


def group_curve(cells, columns):
    values = []
    for row in range(2, 10):
        measurements = [cells[f"{column}{row}"] for column in columns if f"{column}{row}" in cells]
        if measurements:
            values.append((cells[f"A{row}"], len(measurements), mean(measurements)))
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    with ZipFile(args.source) as archive:
        plasma = sheet_cells(archive, "Figure 1 A.xlsx")
        brain = sheet_cells(archive, "Figure 1C.xlsx")
        brain_source = sheet_cells(archive, "Figure 1D.xlsx")
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("measure", "compartment", "route_or_column", "locator", "n", "value", "unit"))
    for name, cells, unit in (("plasma", plasma, "ng/ml"), ("brain", brain, "ng/g")):
        for route, columns in (("intranasal", "BCDEFGHI"), ("oral", "KLMNO")):
            curve = group_curve(cells, columns)
            shared = [(time, level) for time, _, level in curve if 10 <= time <= 120]
            assert [time for time, _ in shared] == [10, 20, 30, 50, 70, 120]
            for time, count, level in curve:
                writer.writerow(("group_mean", name, route, f"{time:g} min", count, f"{level:.5f}", unit))
            writer.writerow(("group_mean_auc", name, route, "10–120 min", "", f"{auc(shared):.5f}", f"{unit}*min"))
            if curve[-1][0] == 180:
                extended = [(time, level) for time, _, level in curve]
                writer.writerow(("group_mean_auc", name, route, "10–180 min", "", f"{auc(extended):.5f}", f"{unit}*min"))

    for index, column in enumerate("KLMNO", 3):
        for compartment, cells, reported_col, unit in (
            ("plasma", plasma, "A", "ng/ml*min"),
            ("brain", brain, "B", "ng/g*min"),
        ):
            curve = [(cells[f"A{row}"], cells[f"{column}{row}"]) for row in range(2, 8)]
            reported = brain_source[f"{reported_col}{index}"]
            recomputed = auc(curve)
            writer.writerow(("oral_series_column_integral", compartment, column, "10–120 min",
                             "", f"{recomputed:.5f}", unit))
            reported_route = "intranasal" if reported_col == "A" else "oral"
            writer.writerow(("reported_brain_auc", "brain", reported_route, f"1D:{reported_col}{index}",
                             "", f"{reported:.5f}", "ng/g*min"))
            writer.writerow(("reported_minus_column_integral", compartment, column,
                             f"1D:{reported_col}{index}", "", f"{reported - recomputed:.5f}", "numeric_difference"))


if __name__ == "__main__":
    main()
