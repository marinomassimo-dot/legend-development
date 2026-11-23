"""Steady-state Hill scenarios, conditional on free concentration in the assay."""
import csv
from pathlib import Path

OUT = Path(__file__).with_name("results")
# Published central potency estimates (µM). None are WWOX measurements.
ORDINARY = {
    "GluA1_gamma8": 10, "GluA1_gamma2": 15, "GluA2Q_gamma2": 49,
    "GluA2Q_gamma8": 48, "GluA1_plus_GluA2Q_gamma2": 23.5,
    "GluA2Q_CTZ_minus60": 48, "GluA2Q_CTZ_minus100": 4.1,
}
EDITED = 1129


def current_block(concentration, ic50, slope):
    return 1 / (1 + (ic50 / concentration) ** slope)


def write(name, header, rows):
    with (OUT / name).open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def main():
    mixtures, thresholds = [], []
    for name, ic50 in ORDINARY.items():
        for slope in (0.5, 1, 1.5):
            for concentration in (0.36, 0.7, 1, 10):
                sensitive = current_block(concentration, ic50, slope)
                resistant = current_block(concentration, EDITED, slope)
                for fraction in (0, 0.1, 0.5, 1):
                    block = fraction * sensitive + (1 - fraction) * resistant
                    mixtures.append((name, ic50, slope, concentration, fraction, block))
                if concentration == 0.36:
                    threshold = (0.10 - resistant) / (sensitive - resistant)
                    thresholds.append((name, slope, resistant, sensitive,
                                       max(0, threshold) if threshold <= 1 else "unattainable"))
    write("mixtures.tsv", ("assembly", "ic50_uM", "slope", "free_uM", "cp_current_fraction",
                           "total_fraction_blocked"), mixtures)
    write("required_fraction.tsv", ("assembly", "slope", "edited_only_block", "cp_only_block",
                                    "cp_fraction_required_for_10pct_total"), thresholds)


if __name__ == "__main__":
    main()
