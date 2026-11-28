"""Compare substrate-routing and electron-transfer genes in held WWOX datasets."""
import argparse
import csv
import gzip
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "cannabidivarin"))
from replay_trp_expression import compare_expression


def raw_pool_detection(geo, destination):
    targets = {"Dmgdh", "Sardh", "Etfa", "Etfb", "Etfdh"}
    with destination.open("w", newline="") as out:
        writer = csv.writer(out, delimiter="\t", lineterminator="\n")
        writer.writerow(("pool", "gene", "nuclei", "gene_UMI", "positive_nuclei"))
        for arm in ("ctrl", "ko"):
            features = geo / f"GSE158684_{arm}_filtered_features.tsv.gz"
            counts = geo / f"GSE158684_{arm}_filtered_matrix.mtx.gz"
            with gzip.open(features, "rt") as source:
                names = [row.split("\t")[1] for row in source]
            wanted = {gene: index for index, gene in enumerate(names, 1) if gene in targets}
            if set(wanted) != targets:
                raise ValueError("A prespecified feature is missing from the matrix header")
            with gzip.open(counts, "rt") as source:
                dimensions = next(row for row in source if not row.startswith("%"))
                _, nuclei, _ = map(int, dimensions.split())
                events = np.fromstring(source.read(), dtype=np.int64, sep=" ").reshape(-1, 3)
            for gene, index in sorted(wanted.items()):
                selected = events[events[:, 0] == index]
                writer.writerow((arm, gene, nuclei, int(selected[:, 2].sum()),
                                 len(np.unique(selected[:, 1]))))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    genes = ("Dmgdh", "Sardh", "Bhmt", "Gnmt", "Etfa", "Etfb", "Etfdh", "Slc25a32",
             "Shmt2", "Mthfd2", "Mthfd2l", "Mthfd1l")
    compare_expression(args.drug_repurposing, args.files, args.output, genes, "native_bulk.tsv")
    raw_pool_detection(args.files / "geo/GSE158684", args.output / "nuclear_coverage.tsv")
