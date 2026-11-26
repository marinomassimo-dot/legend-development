"""Describe branch ratios within SLC17A5 disease and control donor lines."""

import argparse
from collections import defaultdict
import csv
from pathlib import Path
import re
from statistics import mean
import sys
from zipfile import ZipFile
from xml.etree import ElementTree as ET


SHEETS = {"cortical_neurons": 4, "immature_astrocytes": 5, "mature_astrocytes": 6}
PRODUCTS = ("GM2", "GM1a", "GD1a", "GD1b", "GT1b")
LABEL = re.compile(r"([A-Z]+\d+): (HD|FSASD)([12])")


def read_samples(workbook, sheet_index):
    with ZipFile(workbook) as archive:
        shared = ["".join(node.itertext()) for node in ET.fromstring(archive.read("xl/sharedStrings.xml"))]
        path = f"xl/worksheets/sheet{sheet_index}.xml"
        owner = None
        samples = {}
        for row in ET.fromstring(archive.read(path)).findall(".//{*}row"):
            values = {}
            for cell in row.findall("{*}c"):
                value = cell.findtext("{*}v")
                if value is not None:
                    column = cell.get("r").rstrip("0123456789")
                    values[column] = shared[int(value)] if cell.get("t") == "s" else value
            label = LABEL.fullmatch(values.get("A", ""))
            if label:
                sample, group, donor = label.groups()
                owner = (group, donor, sample)
                samples[owner] = {}
            peak = values.get("B")
            if owner and peak in ("GM3", "Lac", *PRODUCTS) and "K" in values:
                if peak in samples[owner]:
                    raise ValueError(f"Duplicate {peak} in {owner}")
                samples[owner][peak] = float(values["K"])
    if len(samples) != 12:
        raise ValueError(f"Expected 12 annotated runs, found {len(samples)}")
    return samples


def line_means(samples):
    runs = defaultdict(list)
    for (group, line, _sample), peaks in samples.items():
        gm3 = peaks["GM3"]
        secondary = sum(peaks[product] for product in PRODUCTS)
        runs[group, line].append((gm3, peaks["Lac"], gm3 / peaks["Lac"], secondary, secondary / gm3))
    if any(len(samples) != 3 for samples in runs.values()) or len(runs) != 4:
        raise ValueError("Expected three runs from each of four lines")
    for key, samples in sorted(runs.items()):
        yield *key, *(f"{mean(column):.6g}" for column in zip(*samples))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    args = parser.parse_args()
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("cell_type", "group", "line", "gm3_pmol_mg", "lac_pmol_mg", "gm3_div_lac",
                     "secondary_pmol_mg", "secondary_div_gm3"))
    for cell_type, sheet_index in SHEETS.items():
        for values in line_means(read_samples(args.workbook, sheet_index)):
            writer.writerow((cell_type, *values))


if __name__ == "__main__":
    main()
