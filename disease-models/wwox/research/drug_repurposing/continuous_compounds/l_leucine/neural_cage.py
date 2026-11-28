"""Contrast the existing leucine panel in the four held neural CAGE libraries."""
import csv
import gzip
import math
from pathlib import Path
import statistics
import sys

from screen import GENES, INPUT_ALIASES


archive = Path(sys.argv[1])
with gzip.open(archive, "rt") as stream:
    table = list(csv.DictReader(stream, delimiter="\t"))

lookup = {row["Gene"]: row for row in table}
assert len(lookup) == len(table)
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("stage", "target", "input_symbol", "control_TPM", "shWWOX_TPM",
                 "raw_log2", "background_median", "centered_log2",
                 "centered_log2_prior1", "background_genes"))
for stage, control, silenced in (("progenitor", "hNSC", "hNSC_WWOX_del"),
                                  ("neuron", "Neurons", "Neurons_WWOX_del")):
    measurable = [row for row in table
                  if float(row[control]) >= 1 and float(row[silenced]) >= 1]

    def ratio(row, prior):
        return math.log2((float(row[silenced]) + prior) / (float(row[control]) + prior))

    center_half = statistics.median(ratio(row, 0.5) for row in measurable)
    center_one = statistics.median(ratio(row, 1.0) for row in measurable)
    for gene in (*GENES, "Wwox"):
        symbol = INPUT_ALIASES.get(gene, gene).upper()
        row = lookup[symbol]
        raw = ratio(row, 0.5)
        writer.writerow((stage, gene.upper(), symbol, f"{float(row[control]):.5f}",
                         f"{float(row[silenced]):.5f}", f"{raw:.5f}", f"{center_half:.5f}",
                         f"{raw - center_half:.5f}", f"{ratio(row, 1.0) - center_one:.5f}",
                         len(measurable)))
