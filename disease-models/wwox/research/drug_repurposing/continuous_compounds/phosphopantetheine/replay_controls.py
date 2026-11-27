"""Summarize the original PPCS and PANK4 source observations without new hypothesis tests."""
import argparse
import csv
from hashlib import sha256
from pathlib import Path
from statistics import mean, stdev
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile


PPCS_HASH = "5772d4579bd5a3f8e3c9cf26c1d04289bc5d00511f54d9ee2bf571cdca4ada44"
PANK4_HASH = "08c0a11bd9dfe1fbe5b607a17fee2705eb559bf493a3289899315a59b161009c"
NS = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
LINE_LABELS = {"NHDF": "control", "95595": "PPCS line A", "103596": "PPCS line B"}


def verify(path, expected):
    if sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f"Unexpected source version for {path}")


def ppcs_rows(path):
    verify(path, PPCS_HASH)
    with path.open(encoding="utf-8-sig") as handle:
        rows = list(csv.reader(handle, delimiter="\t"))
    for column, header in enumerate(rows[0][1:], 1):
        line, _, condition = header.partition(" ")
        obs = [float(row[column].replace(",", ".")) for row in rows[1:]
               if len(row) > column and row[column].strip()]
        yield ("40745475", "Fig S5", LINE_LABELS[line], condition or "untreated",
               "pct untreated control fibroblasts", obs)


def numeric_cells(workbook, sheet_filename):
    root = ET.fromstring(workbook.read(f"xl/worksheets/{sheet_filename}.xml"))
    return {cell.get("r"): float(value) for cell in root.findall(".//x:c", NS)
            if cell.get("t") not in {"s", "inlineStr", "str"}
            and (value := cell.findtext("x:v", namespaces=NS)) is not None}


def pank4_rows(path):
    verify(path, PANK4_HASH)
    with ZipFile(path) as workbook:
        activity = numeric_cells(workbook, "sheet14")
        tracer = numeric_cells(workbook, "sheet15")
    for name, column in (("Water blank", "A"), ("4'-phosphopantothenate", "B"),
                         ("4'-phosphopantetheine", "C")):
        readings = [activity[f"{column}{row}"] for row in (6, 7, 8)]
        yield ("35896750", "Fig 4c", "immunopurified full-length PANK4", name,
               "relative phosphate release", readings)
    for construct, pos in (("vector", 6), ("WT PANK4", 7), ("D623A", 8), ("D659A", 9)):
        for endpoint, row in (("total CoA", pos), ("M+4 CoA from vitamin B5", pos + 7)):
            readings = [tracer[f"{column}{row}"] for column in ("B", "C", "D")]
            yield ("35896750", "Fig 4d source workbook", construct, endpoint,
                   "pct change vs vector mean, protein-normalized", readings)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ppcs_tsv", type=Path)
    parser.add_argument("pank4_xlsx", type=Path)
    args = parser.parse_args()
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("PMID", "locator", "model", "condition", "unit", "observations", "mean", "SD"))
    for rows in (ppcs_rows(args.ppcs_tsv), pank4_rows(args.pank4_xlsx)):
        for pmid, where, model, condition, unit, obs in rows:
            out.writerow((pmid, where, model, condition, unit, len(obs),
                          f"{mean(obs):.5f}", f"{stdev(obs):.5f}"))


if __name__ == "__main__":
    main()
