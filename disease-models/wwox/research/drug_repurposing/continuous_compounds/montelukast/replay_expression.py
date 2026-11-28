"""Replay receptor, leukotriene availability and maturation markers in WWOX models."""
import argparse
import csv
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "cannabidivarin"))
from replay_trp_expression import compare_expression


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    targets = ("Gpr17", "Cysltr1", "Alox5", "Alox5ap", "Ltc4s", "Pdgfra", "Cspg4",
               "Tcf7l2", "Bcas1", "Myrf", "Mbp", "Plp1", "Mog")
    compare_expression(args.drug_repurposing, args.files, args.output, targets, "native_bulk.tsv")

    # Standard class assignment uses Gpr17 as a COP marker. Keep the
    # tissue-wide replay and test stage-local contrasts without that marker.
    from analyze import assigned_nuclei

    with (args.output / "stage_blind.tsv").open("w", newline="") as table:
        writer = csv.writer(table, delimiter="\t", lineterminator="\n")
        writer.writerow(("pool", "class", "gene", "nuclei", "total_UMI", "gene_UMI", "positive", "CPM"))
        for arm, stage, depth, counts in assigned_nuclei(
            args.files, [], [], targets, exclude_markers=("Gpr17",)
        ):
            total = int(depth.sum())
            for gene in targets:
                umi = int(counts[gene].sum())
                writer.writerow((arm, stage, gene, len(depth), total, umi,
                                 int((counts[gene] > 0).sum()), 1e6 * umi / total))
