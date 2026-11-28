"""Replay PK summaries and a conditional one-site competition sensitivity check."""

import csv
import sys


# Observed sources: Park Discussion, PubChem 1884, Vyklický et al. abstract.
CSF_REPORTED_THRESHOLD_NG_ML = 1.4
ACTIVE_MOLAR_MASS = 223.61
ANTAGONIST_DISSOCIATION_NM = 280.0


def competition_fraction(antagonist_nm, coagonist_over_ka):
    antagonist_over_kb = antagonist_nm / ANTAGONIST_DISSOCIATION_NM
    return antagonist_over_kb / (1 + coagonist_over_ka + antagonist_over_kb)


def comparison():
    csf_threshold = 1000 * CSF_REPORTED_THRESHOLD_NG_ML / ACTIVE_MOLAR_MASS
    yield "adult lumbar CSF analytical scale", "reported 7-chlorokynurenate threshold", csf_threshold, "nM", "Park 2020 Discussion; PubChem 1884"
    for name, functional_ic50 in (("late current", 2250), ("peak current", 8960)):
        yield "embryonic mouse hippocampal current", f"{name} IC50 / CSF threshold", functional_ic50 / csf_threshold, "ratio of concentrations", "Vyklický 1990 abstract at 3 µM added glycine; Park 2020 Discussion"
    yield "embryonic mouse hippocampal current", "peak / late functional IC50", 8960 / 2250, "ratio", "Vyklický 1990 abstract at 3 µM added glycine"

    for coagonist_over_ka in (0.1, 1.0, 5.0, 10.0):
        scenario = f"one-site model at coagonist/Ka={coagonist_over_ka:g}"
        locus = "conditional model; Vyklický 1990 280 nM antagonist estimate"
        for size in (1, 10):
            fraction = competition_fraction(size * csf_threshold, coagonist_over_ka)
            yield scenario, f"inhibition at {size} × threshold", 100 * fraction, "% of matched baseline", locus
        target_inhibition = 0.20
        needed = ANTAGONIST_DISSOCIATION_NM * (1 + coagonist_over_ka) * target_inhibition / (1 - target_inhibition)
        yield scenario, "antagonist producing 20% effect", needed, "nM", locus
        yield scenario, "20% effect concentration / CSF threshold", needed / csf_threshold, "ratio", locus

    locus = "Patel et al. 2021 Table 1 author manuscript"
    yield "rat PFC dialysate highest inhibitor arm", "Cmax ratio of means", 4212 / 44, "ratio", locus
    yield "rat PFC dialysate highest inhibitor arm", "AUC0–240 ratio of means", 554308 / 5867, "ratio", locus
    yield "rat PFC dialysate distinct comparison", "Cmax ratio of means", 2630 / 77, "ratio", "Patel et al. Figure 4 and Supplementary Table 3 as reported in text"

    locus = "Patel et al. Figure 2F–G, fits in transfected HEK293 cells"
    concentration = 250.0
    fraction_without = concentration / (577.2 + concentration)
    fraction_with = concentration / (1799 + concentration)
    yield "LAT1 fit at 250 µM parent", "with/without amino acid mix at equal Vmax", fraction_with / fraction_without, "estimated fraction", locus
    yield "LAT1 fit at 250 µM parent", "with/without amino acid mix using both fitted Vmax means", 4522 * fraction_with / (6048 * fraction_without), "estimated fraction", locus


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "statistic", "value", "unit", "locator"))
    for name, statistic, value, unit, locator in comparison():
        writer.writerow((name, statistic, f"{value:.8g}", unit, locator))


if __name__ == "__main__":
    main()
