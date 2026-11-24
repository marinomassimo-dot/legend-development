"""Reproduce the descriptive slice contrasts from Fueta et al., pp. 244–245."""
import csv
from pathlib import Path
import sys

with Path(__file__).with_name("pup_slice_counts.tsv").open() as source:
    groups = {r["group"]: r for r in csv.DictReader(source, delimiter="\t")}
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(["outcome", "control_fraction", "bromide_fraction", "difference_pp"])
for endpoint in ("spontaneous_discharge_n", "evoked_epileptic_n"):
    fractions = []
    for group in ("control_PTZ", "control_PTZ_plus_Br"):
        row = groups[group]
        fractions.append(int(row[endpoint]) / int(row["slices"]))
    baseline, bromide = fractions
    writer.writerow([endpoint, baseline, bromide, f"{100 * (bromide - baseline):.1f}"])
