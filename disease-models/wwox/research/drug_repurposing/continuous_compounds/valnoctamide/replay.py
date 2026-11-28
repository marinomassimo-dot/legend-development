"""Reproduce preparation-specific summary contrasts for valnoctamide."""

import csv
from math import exp
import sys


MOLAR_MASS = 143.23
ACSL4_KM_UM = 4.63
ACSL4_KI_MM = 6.38

# Reported group means in published Table 5, in printed column units.
LIPID_FRACTIONS = (
    ("total phospholipid", 30.5, 15.9, 11.2, 6.1),
    ("choline glycerophospholipid", 13.1, 6.74, 20.1, 11.1),
    ("phosphatidylserine", 2.68, 1.29, 20.2, 9.86),
    ("phosphatidylinositol", 10.6, 9.8, 28.9, 23.1),
    ("ethanolamine glycerophospholipid", 4.06, 2.04, 2.57, 1.32),
)


def percentage_reduction(control, exposed):
    return 100 * (1 - exposed / control)


def uncompetitive_reduction(inhibitor_mm, substrate_um):
    """Rising-phase idealization without substrate inhibition."""
    concentration_ratio = inhibitor_mm / ACSL4_KI_MM
    return 100 * concentration_ratio / (1 + ACSL4_KM_UM / substrate_um + concentration_ratio)


def comparison():
    scope = "rat P14–22 dorsal CA1 whole-cell"
    decay_locator = "Spampanato and Dudek 2014 Results and Fig. 1"
    for label, baseline, treated in (
        ("1 mM VCD vs baseline", 6.7, 12.3),
        ("1 mM VCD washout vs baseline", 6.7, 7.0),
        ("500 µM VCD vs baseline", 5.0, 8.1),
        ("flumazenil plus VCD vs VCD", 8.1, 8.1),
        ("diazepam plus VCD vs diazepam", 11.9, 20.0),
    ):
        yield scope, label, "weighted decay time constant ratio", treated / baseline, "ratio of means", decay_locator
    yield scope, "1 mM VCD vs baseline", "decay-area proxy from means", (58 * 12.3) / (61 * 6.7), "ratio of products", "Spampanato and Dudek 2014 Methods, Fig. 1A2 and Fig. 2B"

    scope = "recombinant rat ACSL4 lysate"
    locator = "Modi et al. 2014 Results and Fig. 2; low-substrate idealization"
    yield scope, "two reported candidate models", "relative AICc weight for uncompetitive model", 1 / (1 + exp(-2.595 / 2)), "fraction", locator
    for inhibitor_mm in (0.455, 0.5, 0.6, 1.0, 1.26, 1.25, 2.5, 5.0):
        for substrate_um in (5, 20, 35):
            value = uncompetitive_reduction(inhibitor_mm, substrate_um)
            yield scope, f"{inhibitor_mm:g} mM nominal VCD, {substrate_um:g} µM AA", "model activity reduction", value, "%", locator
    for threshold_mg_l in (65, 85):
        yield "rat single-isomer total plasma", f"approximate {threshold_mg_l} mg/L early scale", "converted nominal concentration", threshold_mg_l / MOLAR_MASS, "mM", "Shekh-Ahmad et al. 2014 Fig. 4 approximate plotted range; PubChem CID 20140"

    for label, control_jfa, treated_jfa, control_ffa, treated_ffa in LIPID_FRACTIONS:
        locator = "Modi et al. 2017 Table 5, control n=12 and valnoctamide n=15"
        scope = "30-day adult rat brain tracer"
        yield scope, label, "JFA reduction vs control denominator", percentage_reduction(control_jfa, treated_jfa), "%", locator
        yield scope, label, "FFA reduction vs control denominator", percentage_reduction(control_ffa, treated_ffa), "%", locator
    scope = "30-day adult rat brain tracer"
    dilution_control, dilution_treated = 0.027, 0.037
    jin_control, jin_treated = 696e-5, 622e-5
    yield scope, "total phospholipid", "plasma incorporation Jin ratio", jin_treated / jin_control, "ratio of means", "Modi et al. 2017 Table 3"
    yield scope, "total phospholipid", "dilution factor lambda ratio", dilution_treated / dilution_control, "ratio of means", "Modi et al. 2017 Table 4"
    yield scope, "fixed Jin sensitivity", "JFA ratio from lambda alone", dilution_control / dilution_treated, "ratio of means", "Modi et al. 2017 Eq. 4; sensitivity at equal Jin"
    yield scope, "substitution of printed group means", "JFA ratio from Jin and lambda", (jin_treated / dilution_treated) / (jin_control / dilution_control), "ratio of quotients", "Modi et al. 2017 Eq. 4 and Tables 3–4; does not reproduce per-rat aggregation"

    yield "adult epilepsy carbamazepine subgroup", "concomitant valnoctamide", "day 4 CBZ epoxide ratio", 7.4 / 1.5, "ratio of means", "Pisani et al. 1993 primary abstract, n=6"
    yield "adult epilepsy carbamazepine subgroup", "concomitant valnoctamide", "day 7 CBZ epoxide ratio", 7.7 / 1.5, "ratio of means", "Pisani et al. 1993 primary abstract, n=6"
    yield "adult healthy epoxide challenge", "with vs without valnoctamide", "epoxide half-life ratio", 19.7 / 6.9, "ratio of means", "Pisani et al. 1992 primary abstract"
    yield "adult healthy epoxide challenge", "without vs with valnoctamide", "apparent epoxide clearance ratio", 109.6 / 28.8, "ratio of means", "Pisani et al. 1992 primary abstract"


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("preparation", "condition", "statistic", "value", "unit", "locator"))
    for preparation, condition, statistic, value, unit, locator in comparison():
        writer.writerow((preparation, condition, statistic, f"{value:.8g}", unit, locator))


if __name__ == "__main__":
    main()
