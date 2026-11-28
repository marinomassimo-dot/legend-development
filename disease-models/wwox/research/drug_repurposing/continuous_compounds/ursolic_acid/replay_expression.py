"""Replay WWOX astrocytic CNTF and target-cell receptor RNA."""
import argparse
from itertools import combinations
import math
from pathlib import Path
import sys


TARGETS = ("Pparg", "Creb1", "Cntf", "Cntfr", "Lifr", "Il6st", "Lif", "Stat3", "Socs3")


RECEPTOR = ("Cntfr", "Lifr", "Il6st")
DEPTH = 1000


def absent_probability(depth, gene_counts, retained):
    """Chance that all queried transcript UMIs are missed in a fixed-depth subset."""
    if gene_counts > depth - retained:
        return 0.0
    return math.prod((depth - retained - offset) / (depth - offset)
                     for offset in range(gene_counts))


def all_detected_probability(depth, counts, retained):
    if not all(counts):
        return 0.0
    probability = 0.0
    for size in range(len(counts) + 1):
        for subset in combinations(counts, size):
            probability += (-1) ** size * absent_probability(depth, sum(subset), retained)
    return max(0.0, min(1.0, probability))


def summarize_co_detection(drug_repurposing, files, output):
    sys.path.insert(0, str(drug_repurposing / "ganaxolone_20261123"))
    from analyze import assigned_nuclei, tsv

    rows = []
    for arm, cell_class, depth, counts in assigned_nuclei(files, [], [], RECEPTOR):
        quantities = [counts[gene].astype(int) for gene in RECEPTOR]
        for label, feature_indices in [(gene, (i,)) for i, gene in enumerate(RECEPTOR)] + [
                ("all_three", (0, 1, 2))]:
            values = [quantities[i] for i in feature_indices]
            raw = 0
            deep = 0
            predicted = 0.0
            for library, *subunits in zip(depth.astype(int), *values):
                raw += all(subunits)
                if library >= DEPTH:
                    deep += 1
                    predicted += all_detected_probability(library, subunits, DEPTH)
            rows.append((arm, cell_class, label, len(depth), raw, deep, predicted,
                         predicted / deep if deep else "NA"))
    tsv(output / "receptor_detection.tsv",
        ("pool", "class", "feature", "n_nuclei", "observed_positive",
         "n_at_least_1000_UMI", "expected_positive_at_1000_UMI", "fraction_at_1000_UMI"),
        rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    cbdv = args.drug_repurposing / "continuous_compounds" / "cannabidivarin"
    sys.path.insert(0, str(cbdv))
    from replay_trp_expression import compare_expression

    compare_expression(args.drug_repurposing, args.files, args.output, TARGETS, "expression.tsv")
    summarize_co_detection(args.drug_repurposing, args.files, args.output)


if __name__ == "__main__":
    main()
