"""Reweight the held joint transcript counts and replay descriptive reference contrasts."""

import argparse
import csv
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SETS = (
    "Grik1+Neto1", "Grik1+Grik4", "Cacna2d2+Grik1+Neto1",
    "Cacna2d2+Grik1+Grik4+Neto1", "Grik1+Slc12a5",
)
PUBLISHED = (
    ("Orav 2017 Fig. 4B", "P4–6", "CA1 mEPSC frequency after ACET",
     168, 83, 7, 7, "% own baseline", "WT versus Neto1-null"),
    ("Orav 2017 Fig. 5A", "P4–6", "CA3→CA1 evoked EPSC after ATPA",
     66, 99, 6, 9, "% own baseline", "WT versus Neto1-null"),
    ("Orav 2017 Fig. 5B", "P14–16", "CA3→CA1 evoked EPSC after ATPA",
     53, 77, 7, 8, "% own baseline", "WT versus Neto1-null"),
    ("Orav 2019 Fig. 3C", "P4–6", "CA3 interneuron ATPA inward current magnitude",
     39.3, 12.3, 12, 10, "pA", "WT versus Neto1-null"),
    ("Orav 2019 Fig. 6B–C", "P9–10", "Spontaneous interneuron firing, all cells",
     3.27, 2.56, 12, 14, "Hz", "WT versus Neto1-null"),
    ("Orav 2019 Fig. 6B–C", "P9–10", "Spontaneous firing, cells ≤5 Hz only",
     2.43, 1.51, 9, 11, "Hz", "WT versus Neto1-null, selected subset"),
    ("PMID 30570751 Fig. 1A", "P19–26", "CA3 native GABA reversal with UBP310",
     -87.9, -81.5, 5, 5, "mV", "within recordings"),
)


def weights_and_rates(path):
    counts = {}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            key = row["assigned_class"], row["detection_set"], row["depth_comparison"]
            if row["detection_set"] in SETS and row["depth_comparison"] not in ("all", "shared-depth standardized"):
                counts.setdefault(key, {})[row["pool"]] = (int(row["nuclei"]), int(row["positive_nuclei"]))
    for cell in ("exc", "inh"):
        for genes in SETS:
            strata = {
                depth: arms for (cell_class, gene_set, depth), arms in counts.items()
                if (cell_class, gene_set) == (cell, genes)
                and all(arms[arm][0] >= 10 for arm in ("ctrl", "ko"))
            }
            for omit in (None, *strata):
                retained = [arms for depth, arms in strata.items() if depth != omit]
                pooled_weights = [arms["ctrl"][0] + arms["ko"][0] for arms in retained]
                rates = [
                    100 * sum(weight * arms[arm][1] / arms[arm][0]
                              for weight, arms in zip(pooled_weights, retained, strict=True)) / sum(pooled_weights)
                    for arm in ("ctrl", "ko")
                ]
                yield ("WWOX RNA", cell, genes, omit or "none", len(retained), *[f"{v:.4f}" for v in rates],
                       f"{rates[1]-rates[0]:.4f}", "% nuclei", "one pool per genotype")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=HERE / "presynaptic_codetection.tsv")
    args = parser.parse_args()
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "age_or_class", "endpoint", "omitted_depth_bin", "n_bins_or_n_ref_test",
                     "reference", "comparison", "comparison_minus_reference", "unit", "note"))
    for source, age, endpoint, ref, result, first_n, second_n, units, note in PUBLISHED:
        writer.writerow((source, age, endpoint, "NA", f"{first_n}/{second_n}", ref, result,
                         f"{result-ref:.2f}", units, note))
    writer.writerows(weights_and_rates(args.input))


if __name__ == "__main__":
    main()
