"""Recompute the Slc6a9 pooled CPM contrast after omitting each broad nuclear class."""
import csv
import sys
from pathlib import Path

with Path(sys.argv[1]).open() as source:
    rows = [r for r in csv.DictReader(source, delimiter="\t") if r["gene"] == "Slc6a9"]

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(["omitted_class", "control_CPM", "KO_CPM", "KO_minus_control_CPM"])
for omitted in ["none", *sorted({r["class"] for r in rows})]:
    means = []
    for arm in ["ctrl", "ko"]:
        subset = [r for r in rows if r["pool"] == arm and r["class"] != omitted]
        means.append(1e6 * sum(int(r["gene_UMI"]) for r in subset)
                     / sum(int(r["UMI"]) for r in subset))
    writer.writerow([omitted, *(f"{v:.4f}" for v in [*means, means[1] - means[0]])])
