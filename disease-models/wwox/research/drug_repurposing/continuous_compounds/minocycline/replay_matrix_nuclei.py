"""Describe per-pool hippocampal coverage with the held LEGEND classifier."""

import argparse
import csv
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("files", type=Path)
args = parser.parse_args()
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "creatine"))
from assess import assigned_nuclei

genes = ["Mmp9", "Mmp2", "Timp1", "Timp2", "Acan", "Bcan", "Hapln1", "Tnr", "Pvalb"]
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("pool", "assigned_class", "n_nuclei", "all_umi", "gene",
                 "positive_nuclei", "gene_umi", "cpm"))
for pool, group, depth, observed in assigned_nuclei(args.files, [], [], genes):
    for g in genes:
        if g in observed:
            counts = observed[g]
            writer.writerow((pool, group, len(depth), int(depth.sum()), g,
                             int((counts > 0).sum()), int(counts.sum()),
                             f"{counts.sum() * 1e6 / depth.sum():.6f}"))
