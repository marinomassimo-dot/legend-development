"""Check the predeclared leucine panel in the adult P47T bulk count deposit."""
import argparse
import csv
import gzip
from pathlib import Path
import re
import sys

import numpy as np

from screen import GENES, INPUT_ALIASES


def adjusted_difference(values, genotype, sex):
    design = np.column_stack((np.ones(len(values)), genotype, sex))
    fit, _, rank, _ = np.linalg.lstsq(design, values, rcond=None)
    if rank < design.shape[1]:
        raise ValueError("Genotype and sex are not independently estimable")
    return fit[1]


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("counts", type=Path)
parser.add_argument("--denominator", choices=("total", "upper-quartile"), default="total")
args = parser.parse_args()
source = args.counts
with gzip.open(source, "rt") as stream:
    records = csv.reader(stream, delimiter="\t")
    header = next(records)
    assert header[:2] == ["EnsemblID", "Gene_Symbol"]
    names = [re.fullmatch(r"(PFC|HPC|CTX|CB)_(WT/WT|P47T/P47T)_([MF]\d+)", name)
             for name in header[2:]]
    assert all(names)
    input_symbols = [INPUT_ALIASES.get(gene, gene) for gene in GENES]
    library_depths = np.zeros(len(names))
    total = {}
    all_counts = []
    for _, symbol, *counts in records:
        values = np.array(counts, dtype=float)
        library_depths += values
        all_counts.append(values)
        if symbol in input_symbols:
            total[symbol] = total.get(symbol, 0) + values

if args.denominator == "upper-quartile":
    upper_quartile = np.array([np.quantile(column[column > 0], 0.75)
                               for column in np.array(all_counts).T])
    library_depths = upper_quartile * np.median(library_depths) / np.median(upper_quartile)

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("region", "gene", "input_symbol", "WT_n", "P47T_n", "unadjusted_delta_log2",
                 "sex_adjusted_delta_log2", "omit_min", "omit_max"))
for region in ("PFC", "HPC", "CTX", "CB"):
    selected = [i for i, name in enumerate(names) if name.group(1) == region]
    assert len({names[i].group(3) for i in selected}) == len(selected)
    genotype = np.array([names[i].group(2) == "P47T/P47T" for i in selected], dtype=bool)
    sex = np.array([names[i].group(3).startswith("M") for i in selected], dtype=bool)
    for gene, symbol in zip(GENES, input_symbols, strict=True):
        result = [region, gene.upper(), symbol, int((~genotype).sum()), int(genotype.sum())]
        if symbol not in total:
            writer.writerow(result + [""] * 4)
            continue
        y = np.log2(1 + 1e6 * total[symbol][selected] / library_depths[selected])
        omit = np.arange(len(y))
        bounds = [adjusted_difference(y[omit != i], genotype[omit != i], sex[omit != i])
                  for i in omit]
        quantities = (y[genotype].mean() - y[~genotype].mean(),
                      adjusted_difference(y, genotype, sex), min(bounds), max(bounds))
        writer.writerow(result + [f"{value:.5f}" for value in quantities])
