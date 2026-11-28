"""Replay losigamone scope-specific sodium, release, exposure and clinical contrasts."""

import csv
import sys


MOLAR_MASS = 254.66

# Pixel coordinates in the 359 × 640 official PMC figure rasters, origin at upper left.
# Each group lists manually checked bar-top rows in dose order. The first entry is vehicle.
RELEASE_PANELS = (
    ("1a", "S(+)", "potassium", 288, 32, (57, 51, 177, 216), (44, 67, 133, 198)),
    ("1b", "S(+)", "veratridine", 620, 377, (406, 409, 508, 545), (419, 428, 493, 541)),
    ("2a", "R(−)", "potassium", 286, 19, (45, 73, 74, 82), (33, 42, 40, 58)),
    ("2b", "R(−)", "veratridine", 618, 374, (399, 409, 411, 420), (387, 392, 392, 411)),
)


def comparison():
    for panel, isomer, stimulus, zero, hundred, glutamate, aspartate in RELEASE_PANELS:
        concentrations = (0, 50, 100, 200) if isomer == "S(+)" else (0, 100, 200, 400)
        for amino_acid, tops in (("glutamate", glutamate), ("aspartate", aspartate)):
            for level, top in zip(concentrations, tops):
                label = f"{stimulus}, {isomer}, {level} µM, {amino_acid}"
                locus = f"Srinivasan 1999 Fig. {panel}; y0={zero}, y100={hundred}, bar top={top}"
                s2_s1 = 100 * (zero - top) / (zero - hundred)
                relative = 100 * (tops[0] - top) / (zero - tops[0])
                yield "mouse cortical slice effluent", label, "graphical S2/S1", s2_s1, "% of first pulse", locus
                yield "mouse cortical slice effluent", label, "graphical relative change vs own plotted control", relative, "% of control S2/S1", locus

    for name, control, treated, units, locator in (
        ("rheobase mean change", 166.4, 248.2, "pA", "Boehlen et al. 2013 Results, Fig. 7 and Table 2"),
        ("excitability threshold demand", 166.4, 248.2, "ratio of means", "Boehlen et al. 2013 Results, Fig. 7 and Table 2"),
        ("normalized afterpotentials, 25 µM", 104.9, 37, "ratio of means", "Srinivasan et al. 1997 Table 1"),
        ("normalized spontaneous depolarizations, 25 µM", 102.1, 96.9, "ratio of means", "Srinivasan et al. 1997 Table 1"),
        ("normalized spontaneous depolarizations, 100 µM", 102.1, 67.7, "ratio of means", "Srinivasan et al. 1997 Table 1"),
        ("normalized spontaneous depolarizations, 200 µM", 102.1, 49.2, "ratio of means", "Srinivasan et al. 1997 Table 1"),
    ):
        outcome = treated / control if units == "ratio of means" else treated - control
        preparation = "rat entorhinal layer II" if "Boehlen" in locator else "mouse cortical wedge, zero added Mg"
        yield preparation, "exposure versus vehicle", name, outcome, units, locator

    for name, concentration, locator in (
        ("Biber 0.7 µg/mL", 0.7, "Biber and Dienel 1996 primary abstract"),
        ("Biber 1.7 µg/mL", 1.7, "Biber and Dienel 1996 primary abstract"),
        ("Biber 4.4 µg/mL", 4.4, "Biber and Dienel 1996 primary abstract"),
        ("Peeters racemate parent", 1.99, "Peeters et al. 1998 Table I"),
        ("Peeters pure S(+)", 1.69, "Peeters et al. 1998 Table I"),
        ("Peeters pure R(−)", 0.44, "Peeters et al. 1998 Table I"),
    ):
        total = 1000 * concentration / MOLAR_MASS
        yield "healthy adult plasma", name, "converted Cmax", total, "µM total", locator
        yield "healthy adult plasma", name, "conditional Cmax at fu=0.50", total * 0.50, "µM unbound scenario", locator
    comparator = 1000 * 4.4 / MOLAR_MASS * 0.50
    for bath in (25, 100, 200):
        yield "cross-preparation scale", f"{bath} µM nominal bath", "bath / illustrative adult unbound Cmax", bath / comparator, "ratio", "Biber and Dienel 1996 primary abstract; Peeters et al. 1998 plasma binding"
    for category, value, locator in (
        ("pure S(+) / R(−) Cmax", 1690 / 440, "Peeters et al. 1998 Table I"),
        ("pure S(+) / R(−) AUC", 10460 / 1260, "Peeters et al. 1998 Table I"),
        ("racemate S(+) / R(−) AUC", 9110 / 1110, "Peeters et al. 1998 Table II"),
        ("pure R(−) / S(+) apparent oral clearance", 1863 / 171, "Peeters et al. 1998 Table I"),
    ):
        yield "healthy adult chiral plasma", category, "reported-value ratio", value, "ratio of means", locator

    for trial, placebo, arms, locator in (
        ("Bauer 2001", (6.7, 14.6, 37.5), (("active", (14.9, 22.3, 59.6)),), "Bauer et al. 2001 primary abstract"),
        ("Baulac 2003", (3.3, 11.8, 58.8), (("lower", (19.7, 17.2, 62.1)), ("higher", (25.3, 29.3, 76.1))), "Baulac and Klement 2003 primary abstract"),
    ):
        outcomes = ("median frequency reduction", "reported responder rate", "any adverse event")
        for arm, values in arms:
            for outcome, treated, control in zip(outcomes, values, placebo):
                yield trial, arm, f"{outcome} difference versus placebo", treated - control, "percentage points", locator


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("preparation", "condition", "statistic", "value", "unit", "locator"))
    for preparation, condition, statistic, value, unit, locator in comparison():
        writer.writerow((preparation, condition, statistic, f"{value:.7g}", unit, locator))


if __name__ == "__main__":
    main()
