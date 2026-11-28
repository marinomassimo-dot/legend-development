#!/usr/bin/env python3
"""Summarize prespecified gene contrasts by public GEO donor and cell fraction."""
import argparse
import csv
import gzip
from collections import defaultdict
from math import log2
from pathlib import Path
from statistics import mean, median
from xml.etree import ElementTree as ET
from zipfile import ZipFile

MATRIX_SHA256 = "0f0d2cb29f6931173bbacb02987d1c05faeeb943b9305681a73474bb560c8375"
COUNTS_SHA256 = "30fa585f1b4574ef1ba4a0cefe71df3dab05fe7d8245174fd6818bf003c04eba"
PANEL = """
PRKAA1 PRKAA2 STK11 CAMKK2 ACACA ACACB RPTOR ULK1 SLC22A1 SLC22A2 SLC22A3
SLC29A4 SLC47A1 SLC47A2 PDGFRA MYRF MBP PLP1 CNP MAG MOG UGT8 GAL3ST1
""".split()
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


def read_pairs(matrix):
    with gzip.open(matrix, "rt") as stream:
        titles = next(row[1:] for row in csv.reader(stream, delimiter="\t")
                      if row and row[0] == "!Sample_title")
    sample_columns = defaultdict(dict)
    for index, title in enumerate(titles):
        donor, _, age, fraction, condition = title.split("_")
        arms = sample_columns[age, fraction, donor]
        if condition in arms or condition not in {"N1", "MET"}:
            raise ValueError("Unexpected arm or duplicate donor-condition column")
        arms[condition] = index
    pairs = defaultdict(list)
    missing = defaultdict(int)
    for (age, fraction, _), arms in sample_columns.items():
        group = age, fraction
        if arms.keys() == {"N1", "MET"}:
            pairs[group].append((arms["N1"], arms["MET"]))
        else:
            missing[group] += 1
    return titles, pairs, missing


def worksheet_rows(workbook):
    with ZipFile(workbook) as archive:
        with archive.open("xl/sharedStrings.xml") as stream:
            shared = ["".join(node.itertext()) for node in ET.parse(stream).getroot()]
        with archive.open("xl/worksheets/sheet1.xml") as stream:
            rows = ET.iterparse(stream, events=("start", "end"))
            sheet_data = None
            for event, node in rows:
                if event == "start" and node.tag == NS + "sheetData":
                    sheet_data = node
                if event == "end" and node.tag == NS + "row":
                    row = []
                    for cell in node:
                        value = cell.findtext(NS + "v")
                        if value is not None and cell.get("t") == "s":
                            value = shared[int(value)]
                        row.append(value)
                    yield row
                    sheet_data.remove(node)


def read_counts(workbook, titles):
    rows = worksheet_rows(workbook)
    header = next(rows)
    stripped = [label.split("_", maxsplit=1)[1] for label in header[1:]]
    if header[0] != "Symbol" or sorted(stripped) != sorted(titles) or len(set(titles)) != len(titles):
        raise ValueError("Read count headers and public series metadata do not match one-to-one")
    order = [stripped.index(title) for title in titles]
    library_totals = [0] * len(titles)
    log_size_ratios = [[] for _ in titles]
    selected = {}
    for row in rows:
        # Column A is an unlabeled Ensembl identifier and has no header cell.
        if len(row) != len(header) + 1 or any(entry is None for entry in row):
            raise ValueError("Incomplete worksheet row")
        gene_id, symbol, *raw = row
        if not gene_id.startswith("ENSG"):
            raise ValueError("Unexpected gene identifier in column A")
        counts = [int(raw[k]) for k in order]
        if any(count < 0 for count in counts):
            raise ValueError("Negative read count")
        library_totals = [a + b for a, b in zip(library_totals, counts)]
        if min(counts) > 0:
            log_counts = [log2(count) for count in counts]
            log_gene_center = mean(log_counts)
            for sample_ratios, log_count in zip(log_size_ratios, log_counts):
                sample_ratios.append(log_count - log_gene_center)
        if symbol in PANEL:
            if symbol in selected:
                raise ValueError(f"Ambiguous symbol: {symbol}")
            selected[symbol] = counts
    size_factors = [2 ** median(sample) for sample in log_size_ratios]
    return library_totals, size_factors, selected


def direction(values):
    if all(value > 0 for value in values):
        return "up"
    if all(value < 0 for value in values):
        return "down"
    return "mixed_or_zero"


def main():
    from hashlib import sha256

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", type=Path)
    parser.add_argument("workbook", type=Path)
    args = parser.parse_args()
    for path, expected in ((args.matrix, MATRIX_SHA256), (args.workbook, COUNTS_SHA256)):
        if sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f"Input fingerprint mismatch: {path.name}")
    titles, pairs, missing = read_pairs(args.matrix)
    totals, size_factors, selected = read_counts(args.workbook, titles)

    print("age\tfraction\tpairs\tunpaired\tsymbol\tpositive_control\tpositive_metformin\tmean_log2_cpm_difference\tpair_signs\tleave_one_mean_sign\tmean_log2_ratio_normalized_difference\tratio_leave_one_mean_sign")
    for (age, fraction), group in sorted(pairs.items()):
        for symbol in PANEL:
            if symbol not in selected:
                print(age, fraction, len(group), missing[age, fraction], symbol,
                      "not_in_table", "not_in_table", "NA", "NA", "NA", "NA", "NA", sep="\t")
                continue
            counts = selected[symbol]
            log_cpm = [log2(1 + 1e6 * count / size) for count, size in zip(counts, totals)]
            log_ratio = [log2(1 + count / factor) for count, factor in zip(counts, size_factors)]
            deltas = [log_cpm[met] - log_cpm[ctl] for ctl, met in group]
            omit_one = [mean(deltas[:k] + deltas[k+1:]) for k in range(len(deltas))]
            ratio_deltas = [log_ratio[met] - log_ratio[ctl] for ctl, met in group]
            ratio_omit_one = [
                mean(ratio_deltas[:k] + ratio_deltas[k+1:]) for k in range(len(ratio_deltas))
            ]
            print(age, fraction, len(group), missing[age, fraction], symbol,
                  sum(counts[ctl] > 0 for ctl, _ in group), sum(counts[met] > 0 for _, met in group),
                  f"{mean(deltas):.4f}", direction(deltas), direction(omit_one),
                  f"{mean(ratio_deltas):.4f}", direction(ratio_omit_one), sep="\t")


if __name__ == "__main__":
    main()
