"""Recalculate Tyurina et al. Fig. 2f and the PE half of Fig. 2g."""

import argparse
import csv
import hashlib
import sys
import xml.etree.ElementTree as ET
from statistics import mean
from zipfile import ZipFile


WORKBOOK_SHA = "9478a46bea7939d38a0d8844c01e24a43288e98fa069e4b046b84d1e60421809"


def comparison(sheet):
    numeric = {
        cell.attrib["r"]: float(cell.findtext("{*}v"))
        for cell in sheet.findall(".//{*}c")
        if cell.attrib.get("t", "n") == "n" and cell.findtext("{*}v") is not None
    }
    for panel, condition, rows, diacyl_column, alkenyl_column in (
        ("2f", "15-LOX-2, HT22 lipid liposomes, 2.5 min", range(3, 6), "J", "L"),
        ("2f", "15-LOX-2, HT22 lipid liposomes, 5 min", range(3, 6), "K", "M"),
        ("2g", "AMVN, DOPC liposomes", range(9, 12), "K", "M"),
    ):
        diacyl = mean(numeric[f"{diacyl_column}{row}"] for row in rows)
        alkenyl = mean(numeric[f"{alkenyl_column}{row}"] for row in rows)
        yield panel, condition, len(rows), diacyl, alkenyl
    diacyl_control = mean(numeric[f"J{row}"] for row in range(9, 12))
    alkenyl_control = mean(numeric[f"L{row}"] for row in range(9, 12))
    diacyl_amvn = mean(numeric[f"K{row}"] for row in range(9, 12))
    alkenyl_amvn = mean(numeric[f"M{row}"] for row in range(9, 12))
    yield "2g", "AMVN, subtract corresponding control mean", 3, (
        diacyl_amvn - diacyl_control
    ), alkenyl_amvn - alkenyl_control


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=argparse.FileType("rb"))
    args = parser.parse_args()
    if hashlib.file_digest(args.workbook, "sha256").hexdigest() != WORKBOOK_SHA:
        parser.error("workbook differs from the pinned PMC source-data release")
    args.workbook.seek(0)
    with args.workbook, ZipFile(args.workbook) as workbook:
        sheet = ET.fromstring(workbook.read("xl/worksheets/sheet2.xml"))
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("panel", "condition", "n_per_condition", "diacyl_mean_pmol_per_nmol_precursor",
                     "alkenyl_mean_pmol_per_nmol_precursor", "alkenyl_to_diacyl_ratio"))
    for panel, condition, count, diacyl, alkenyl in comparison(sheet):
        writer.writerow((panel, condition, count, f"{diacyl:.3f}", f"{alkenyl:.3f}",
                         f"{alkenyl / diacyl:.3f}"))


if __name__ == "__main__":
    main()
