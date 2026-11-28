"""Descriptive positive-entry coverage, using published fetal GSE155488 values."""
import csv
import gzip
import hashlib
from pathlib import Path
import sys

source = Path(sys.argv[1])
assert hashlib.sha256(source.read_bytes()).hexdigest() == (
    "c3e3e6fa4190fa50b0101e3017ed022fb7457afe7dee0cb73bff04fe04e3b5eb"
)
markers = ("PDGFRA", "GPR17", "TCF7L2", "MBP", "SLC23A2", "TET1", "TET2", "TET3")
detected = {}
n_cells = 359
depth = [0] * n_cells
with gzip.open(source, "rt", newline="") as handle:
    for row in csv.reader(handle):
        gene, *values = row
        assert len(values) == n_cells
        positive = [float(value) > 0 for value in values]
        if gene in markers:
            assert gene not in detected, gene
            detected[gene] = positive
        depth = [count + present for count, present in zip(depth, positive, strict=True)]
assert set(detected) == set(markers)
median = sorted(depth)[n_cells // 2]
groups = {
    "all_columns": list(range(n_cells)),
    "PDGFRA_positive_no_transition_or_MBP": [
        i for i in range(n_cells) if detected["PDGFRA"][i]
        and not any(detected[g][i] for g in ("GPR17", "TCF7L2", "MBP"))
    ],
    "GPR17_TCF7L2_double_positive_MBP_negative": [
        i for i in range(n_cells) if detected["GPR17"][i] and detected["TCF7L2"][i]
        and not detected["MBP"][i]
    ],
    "MBP_positive": [i for i in range(n_cells) if detected["MBP"][i]],
}
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("marker_gate", "detected_genes_filter", "cells", "gene", "positive", "positive_pct"))
for group, indices in groups.items():
    for stratum, subset in (
        ("all", indices), (f"ge_median_{median}", [i for i in indices if depth[i] >= median])
    ):
        for gene in markers[4:]:
            positives = sum(detected[gene][i] for i in subset)
            writer.writerow((group, stratum, len(subset), gene, positives,
                             round(100 * positives / len(subset), 2) if subset else "NA"))
