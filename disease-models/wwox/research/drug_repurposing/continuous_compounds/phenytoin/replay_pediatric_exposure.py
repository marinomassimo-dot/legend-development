"""Recompute the pediatric parent exposure scale from the published summary values."""
import csv
import sys

from replay_opening import MOLAR_MASS


def to_micromolar(concentration):
    return 1000 * concentration / MOLAR_MASS


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "summary", "free_parent_ug_mL", "value", "unit"))
    serum = (
        ("Sathe ESETT Results", "observed minimum", 1.0),
        ("Sathe ESETT Results", "observed maximum", 2.8),
        ("Bohannon Results", "mean in group of 12", 2.45),
        ("Bohannon Results", "mean in group of 29", 2.52),
    )
    for source, description, concentration in serum:
        writer.writerow((source, description, concentration,
                         f"{to_micromolar(concentration):.4f}", "micromolar"))
    writer.writerow(("Tidball Fig 7D / Sathe Results", "24 micromolar nominal bath / observed max",
                     "NA", f"{24 / to_micromolar(2.8):.4f}", "ratio"))


if __name__ == "__main__":
    main()
