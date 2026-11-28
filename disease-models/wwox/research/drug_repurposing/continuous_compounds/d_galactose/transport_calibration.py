"""Replay the SLC35A2 control in the eLife Fig. 4G and Fig. 5B workbooks."""

import argparse
import csv
from itertools import combinations
from pathlib import Path
from statistics import mean
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile


def numeric_cells(workbook, sheet):
    with ZipFile(workbook) as archive:
        uri = f"xl/worksheets/sheet{sheet}.xml"
        root = ET.fromstring(archive.read(uri))
        strings_root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    strings = ["".join(node.text or "" for node in item.iterfind(".//{*}t")) for item in strings_root]
    cells = {}
    for cell in root.iterfind(".//{*}c"):
        value = cell.findtext("{*}v")
        if value is None:
            continue
        if cell.get("t") == "s":
            value = strings[int(value)]
        try:
            cells[cell.attrib["r"]] = float(value)
        except ValueError:
            continue
    return cells


def contrast(control, restored):
    omissions = [
        mean(test) / mean(reference)
        for test in combinations(restored, 2)
        for reference in combinations(control, 2)
    ]
    return mean(control), mean(restored), mean(restored) / mean(control), min(omissions), max(omissions)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    args = parser.parse_args()
    abundance = numeric_cells(args.inputs / "elife-65417-fig4-data1-v2.xlsx", 6)
    uptake = numeric_cells(args.inputs / "elife-65417-fig5-data1-v2.xlsx", 1)
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("panel", "readout", "analyte", "control_mean", "SLC35A2OE_mean",
                     "OE_to_control", "paired_omission_min", "paired_omission_max"))

    for name, column in (("UDP_Gal", "C"), ("UDP_Glc", "B"), ("UDP_HexNAc", "D"), ("CMP_Sia", "I")):
        raw = [abundance[f"{column}{i}"] for i in range(2, 8)]
        tic_scaled = [value / abundance[f"J{i}"] for i, value in enumerate(raw, 2)]
        normalized = [abundance[f"{column}{i}"] for i in range(11, 17)]
        for stored, recomputed in zip(normalized, tic_scaled, strict=True):
            assert abs(stored - recomputed / mean(tic_scaled[:3])) < 1e-9
        for readout, values in (("raw_ion_signal", raw), ("TIC_normalized", normalized)):
            result = contrast(values[:3], values[3:])
            writer.writerow(("4G", readout, name, *(f"{value:.5f}" for value in result)))

    tic = [abundance[f"J{i}"] for i in range(2, 8)]
    result = contrast(tic[:3], tic[3:])
    writer.writerow(("4G", "normalization_denominator", "TIC", *(f"{value:.5f}" for value in result)))

    for name, control_col, overexpression_col in (
        ("UDP_Gal", "G", "J"), ("UDP_Glc", "B", "E"), ("UDP_GlcNAc", "L", "O"),
    ):
        control = [uptake[f"{control_col}{i}"] for i in range(3, 6)]
        overexpression = [uptake[f"{overexpression_col}{i}"] for i in range(3, 6)]
        result = contrast(control, overexpression)
        writer.writerow(("5B", "normalized_filter_retention", name, *(f"{value:.5f}" for value in result)))


if __name__ == "__main__":
    main()
