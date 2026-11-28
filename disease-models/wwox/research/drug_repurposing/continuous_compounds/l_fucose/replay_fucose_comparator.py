"""Replay selected normalized expression contrasts from Di Lucente et al."""

import argparse
import csv
import gzip
import hashlib
from math import log2
from pathlib import Path
from statistics import mean
from xml.etree import ElementTree as ET
from zipfile import ZipFile

GENES = ("Fuk", "Fpgt", "Gmds", "Tsta3", "Slc35c1", "Fut8", "Vamp1", "Stx1b")
ALIASES = {"Fcsk": "Fuk", "Gfus": "Tsta3"}
ACUTE_SHA256 = "41a78e6d37bc82a507fa5229067b7bd290091217d5c7886b74b17b7dbd61b75e"
CHRONIC_SHA256 = "878b488a13a9e01a25ffff3f7161b4971e20214cf40ab54a45620cada9511b87"


def verified(path, expected):
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f"Source digest mismatch for {path.name}")
    return path


def column_index(cell):
    column = 0
    for letter in cell.get("r").rstrip("0123456789"):
        column = 26 * column + ord(letter) - ord("A") + 1
    return column - 1


def chronic_table(path):
    by_gene = {}
    gene_ids = {}
    with ZipFile(verified(path, CHRONIC_SHA256)) as book:
        strings = ["".join(t.text or "" for t in entry.iterfind(".//{*}t"))
                   for entry in ET.fromstring(book.read("xl/sharedStrings.xml")).findall("{*}si")]
        with book.open("xl/worksheets/sheet1.xml") as sheet:
            for _, row in ET.iterparse(sheet, events=("end",)):
                if not row.tag.endswith("}row"):
                    continue
                cells = {}
                for cell in row.findall("{*}c"):
                    value = cell.findtext("{*}v")
                    if value is not None:
                        cells[column_index(cell)] = strings[int(value)] if cell.get("t") == "s" else value
                if row.get("r") == "1":
                    expected = [f"{arm} {index}" for arm in ("WT_CD", "5xFAD_CD", "5xFAD_FD")
                                for index in range(1, 7)]
                    if [cells[i] for i in range(2, 20)] != expected:
                        raise ValueError("Unexpected chronic cohort columns")
                else:
                    symbol = cells.get(1, "")
                    gene = ALIASES.get(symbol, symbol)
                    if gene in GENES:
                        if gene in by_gene:
                            raise ValueError(f"Duplicate mapping for {gene}")
                        gene_ids[cells[0].split(".")[0]] = gene
                        by_gene[gene] = [float(cells[i]) for i in range(2, 20)]
                row.clear()
    return by_gene, gene_ids


def short_table(path, gene_ids):
    by_gene = {}
    with gzip.open(verified(path, ACUTE_SHA256), "rt") as stream:
        rows = csv.reader(stream)
        expected = [f"{arm} {i}" for arm in ("Cont", "Fuc") for i in range(1, 7)]
        if next(rows)[1:] != expected:
            raise ValueError("Unexpected 5-hour cohort columns")
        for identifier, *values in rows:
            if identifier in gene_ids:
                gene = gene_ids[identifier]
                if gene in by_gene:
                    raise ValueError(f"Duplicate mapping for {gene}")
                by_gene[gene] = list(map(float, values))
    return by_gene


def contrast(values, reference, treated):
    x = [log2(1 + value) for value in values[reference]]
    y = [log2(1 + value) for value in values[treated]]
    x_omit = [(sum(x) - value) / (len(x) - 1) for value in x]
    y_omit = [(sum(y) - value) / (len(y) - 1) for value in y]
    omissions = [mean(y) - omitted for omitted in x_omit] + [omitted - mean(x) for omitted in y_omit]
    return mean(y) - mean(x), min(omissions), max(omissions)


def main(inputs):
    chronic, gene_ids = chronic_table(inputs / "GSE295460_Raw_Counts.xlsx")
    short = short_table(inputs / "GSE295285_Raw_Count.csv.gz", gene_ids)
    comparisons = (
        ("GSE295285_WT_5h_fucose_vs_ACSF", short, slice(0, 6), slice(6, 12)),
        ("GSE295460_control_diet_5xFAD_vs_WT", chronic, slice(0, 6), slice(6, 12)),
        ("GSE295460_5xFAD_1mo_fucose_vs_control_diet", chronic, slice(6, 12), slice(12, 18)),
    )
    print("comparison\tgene\treference_n\ttreated_n\tdelta_log2_1p\tomit_min\tomit_max")
    for label, dataset, reference, treated in comparisons:
        for gene in GENES:
            numbers = [f"{value:.6f}" for value in contrast(dataset[gene], reference, treated)]
            print("\t".join((label, gene.upper(), "6", "6", *numbers)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    main(parser.parse_args().inputs)
