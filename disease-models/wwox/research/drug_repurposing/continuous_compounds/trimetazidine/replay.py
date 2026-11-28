"""Replay published aggregate contrasts and two illustrative inhibition models."""

import csv
from statistics import mean, stdev
import sys


def percent_change(reference, comparison):
    return 100 * (comparison / reference - 1)


def reaction_rate(substrate, vmax, km):
    return vmax * substrate / (km + substrate)


def comparison():
    # Kantor et al., abstract, working rat heart, 0.4 mM palmitate.
    yield "rat cardiac flux", "palmitate", percent_change(488, 408), "% change", "PMID 10720420 abstract"
    yield "rat cardiac flux", "glucose", percent_change(1889, 2378), "% change", "PMID 10720420 abstract"

    # A constructive example. These are chosen model parameters, not fitted observations.
    # Both models have the same drug curve and the same untreated rate at S=2.5 µM.
    locus = "illustrative model prompted by PMID 12869392 Figure 1"
    for substrate in (2.5, 5, 10, 15):
        treated = reaction_rate(substrate, vmax=0.6, km=5)
        competitive_control = reaction_rate(substrate, vmax=0.6, km=1.25)
        noncompetitive_control = reaction_rate(substrate, vmax=1.2, km=5)
        for model, untreated in (
            ("competitive", competitive_control),
            ("noncompetitive", noncompetitive_control),
        ):
            label = f"{model} at {substrate:g} µM immediate substrate"
            yield label, "untreated rate", untreated, "arbitrary rate", locus
            yield label, "treated rate", treated, "arbitrary rate", locus
            yield label, "remaining inhibition", 100 * (1 - treated / untreated), "% of same-substrate control", locus

    # Under simple competition, 50% at S1 sets Km*[I]/Ki = Km + S1.
    # At S2, the residual inhibition increases with Km for S2 > S1.
    low_substrate, high_substrate = 2.5, 15
    floor = low_substrate / (low_substrate + high_substrate)
    yield "competitive model with exactly 50% at 2.5 µM", "infimum at 15 µM", 100 * floor, "% inhibition", locus

    # Dedkova et al. Table 1 and Figure 4C, different endpoints. Calculate
    # contrasts from means and keep them separate from the paper's mean ratios.
    for agent, respiration, pore_signal in (("trimetazidine", 405.7, 101), ("4-bromotiglic acid", 391.5, 387)):
        yield f"rabbit myocyte {agent}", "state 3 palmitoylcarnitine respiration", percent_change(522.0, respiration), "% change of group means", "PMID 23388837 Table 1"
        yield f"rabbit myocyte {agent}", "palmitate-induced pore readout", percent_change(408, pore_signal), "% change of group means", "PMID 23388837 Figure 4C"

    # WO2018236745A1 Table 68. One late, total whole-tissue observation per rat.
    brain = (35.4, 36.8, 39.5)
    paired_ratios = (1.56, 2.63, 2.80)
    yield "rat patent distribution", "whole-brain mean", mean(brain), "ng/g wet tissue", "WO2018236745A1 Table 68"
    yield "rat patent distribution", "mean paired total brain/plasma", mean(paired_ratios), "ratio", "WO2018236745A1 Table 68"
    yield "rat patent distribution", "SD of paired total brain/plasma", stdev(paired_ratios), "ratio", "WO2018236745A1 Table 68"
    yield "rat patent distribution", "whole-brain mean as molar amount/mass", mean(brain) / 266.34, "µmol/kg wet tissue", "WO2018236745A1 Table 68 and PubChem 21109"
    yield "mouse PTZ kindling", "low-arm hippocampal IL-6", percent_change(402.78, 123.15), "% change of group means", "PMID 40894200 Table 1"


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "statistic", "value", "unit", "locator"))
    for name, statistic, value, unit, locator in comparison():
        writer.writerow((name, statistic, f"{value:.8g}", unit, locator))


if __name__ == "__main__":
    main()
