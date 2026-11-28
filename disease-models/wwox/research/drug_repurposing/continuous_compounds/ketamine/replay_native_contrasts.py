"""Recompute descriptive ketamine contrasts from published within-assay summaries."""
import argparse
import csv
from pathlib import Path


RATIOS = (
    ("Olah_S1", "CA1 WT miniature IPSC frequency", "mean frequency ratio per cell", 10, 1.0, 0.60),
    ("Olah_S1", "CA1 PV-GluN2D-KO miniature IPSC frequency", "mean frequency ratio per cell", 9, 1.0, 0.94),
    ("Olah_S1", "CA1 vehicle miniature IPSC frequency", "mean frequency ratio per cell", 10, 1.0, 1.02),
    ("Olah_S1", "CA1 WT miniature IPSC frequency", "ratio of group means, Hz", 10, 1.40, 0.89),
    ("Olah_S1", "CA1 PV-GluN2D-KO miniature IPSC frequency", "ratio of group means, Hz", 9, 1.24, 1.11),
    ("Olah_S2", "CA1 WT miniature IPSC amplitude", "mean amplitude ratio per cell", 10, 1.0, 0.99),
    ("Olah_S2", "CA1 PV-GluN2D-KO miniature IPSC amplitude", "mean amplitude ratio per cell", 9, 1.0, 1.03),
    ("Bieber_Fig6", "intracortical NMDA EPSP area", "ratio of medians", 6, 1115, 521),
    ("Bieber_Fig7A", "spontaneous IPSC frequency without AP5", "ratio of medians, Hz", 8, 1.2, 1.5),
    ("Bieber_Fig7B", "spontaneous IPSC frequency with AP5", "ratio of medians, Hz", 10, 1.370, 2.442),
    ("Bieber_Fig8A", "intracortical AMPA EPSP area", "ratio of medians", 6, 294, 472),
    ("Bieber_Fig9A", "thalamocortical AMPA EPSP area", "ratio of medians", 10, 337, 399),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    rows = [(source, readout, estimand, n, baseline, exposed, f"{100 * (exposed / baseline - 1):.3f}")
            for source, readout, estimand, n, baseline, exposed in RATIOS]
    rows.append(("Olah_S1", "WT minus PV-GluN2D-KO", "difference in mean cell-ratio changes, percentage points", "10/9",
                 "NA", "NA", f"{100 * (0.60 - 0.94):.3f}"))
    rows.append(("Olah_S1", "WT minus PV-GluN2D-KO", "difference in ratios of means, percentage points", "10/9",
                 "NA", "NA", f"{100 * (0.89 / 1.40 - 1.11 / 1.24):.3f}"))
    with args.output.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(("source", "readout", "estimand", "n_recordings", "baseline", "exposed", "change_percent_or_pp"))
        writer.writerows(rows)


if __name__ == "__main__":
    main()
