"""Count detected arginine-recycling transcripts in pooled GSE158684 nuclei."""
import argparse
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "ganaxolone_20261123"))
from analyze import assigned_nuclei, tsv

GENES = ["Ass1", "Asl", "Nos1", "Nos2", "Nos3"]
SETS = [("Ass1",), ("Asl",), ("Nos1",), ("Nos2",), ("Nos3",),
        ("Ass1", "Asl"), ("Asl", "Nos1"), ("Ass1", "Asl", "Nos1")]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    rows = []
    for pool, cell_class, depth, counts in assigned_nuclei(args.files, [], [], GENES):
        for minimum in (500, 1000):
            retained = depth >= minimum
            n = int(retained.sum())
            total = int(depth[retained].sum())
            for genes in SETS:
                present = retained.copy()
                for gene in genes:
                    present &= counts[gene] > 0
                positive = int(present.sum())
                umi = int(counts[genes[0]][retained].sum()) if len(genes) == 1 else "NA"
                cpm = f"{1e6 * umi / total:.4f}" if len(genes) == 1 and total else "NA"
                rows.append([pool, cell_class, minimum, n, total, "+".join(genes),
                             positive, f"{100 * positive / n:.4f}" if n else "NA", umi, cpm])
    tsv(args.out, ["pool", "assigned_class", "min_UMI", "nuclei", "total_UMI",
                   "co_detection_set", "positive_nuclei", "positive_pct",
                   "single_gene_UMI", "single_gene_CPM"], rows)


if __name__ == "__main__":
    main()
