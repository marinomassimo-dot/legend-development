"""Recompute descriptive contrasts from the indicated published condition means."""
import csv
import sys


def percent_change(values):
    baseline, exposed = values
    return (exposed / baseline - 1) * 100


def fraction_recovered(values):
    intact, inhibited, exposed = values
    return (exposed - inhibited) / (intact - inhibited) * 100


# Nominal dye exposures are assay conditions, not measured free concentrations.
ROWS = (
    ("30734287", "Fig 2A", "rotenone O2 loss recovered", "nmol/min/mg",
     (121.4, 1.95, 21.0), fraction_recovered, "% lost"),
    ("30734287", "Fig 2B", "antimycin O2 after dye", "nmol/min/mg",
     (15.6, 20.2), percent_change, "% change"),
    ("30734287", "Fig 1", "peroxide with pyruvate and malate", "pmol/min/mg",
     (76.3, 1460), percent_change, "% change"),
    ("33669457", "Fig 1D", "antimycin O2 after dye, before ADP", "nmol/min/mg",
     (36.7, 58.7), percent_change, "% change"),
    ("33669457", "Fig 1D", "antimycin O2 after ADP versus after dye", "nmol/min/mg",
     (58.7, 36.4), percent_change, "% change"),
    ("33669457", "Fig 1D", "antimycin O2 after ADP versus pre-dye", "nmol/min/mg",
     (36.7, 36.4), percent_change, "% change"),
    ("33669457", "Fig 1C", "myxothiazol O2 after dye, before ADP", "nmol/min/mg",
     (4.5, 22.7), percent_change, "% change"),
    ("28495375", "Fig 2B", "ATP with oligomycin/AP5, alpha-ketoglutarate", "nmol/min/mg",
     (47, 81), percent_change, "% change"),
    ("28495375", "Fig 2D", "ATP with oligomycin/AP5, glutamate", "nmol/min/mg",
     (31, 54), percent_change, "% change"),
    ("28495375", "Fig 2C", "ATP with oligomycin/AP5, succinate", "nmol/min/mg",
     (19, 19), percent_change, "% change"),
)


def main():
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("PMID", "locator", "comparison", "mean_units", "ordered_means",
                  "contrast", "contrast_units"))
    for pmid, locator, label, units, values, calculate, contrast_units in ROWS:
        means = ",".join(map(str, values))
        out.writerow((pmid, locator, label, units, means, f"{calculate(values):.3f}",
                      contrast_units))


if __name__ == "__main__":
    main()
