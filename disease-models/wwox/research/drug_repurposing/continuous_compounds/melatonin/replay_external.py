"""Recalculate melatonin trial contrasts, stage-mixture bounds and exposure scales."""

import csv
from math import comb, sqrt
import sys


def wilson(events, n):
    z = 1.959963984540054
    frequency = events / n
    denominator = 1 + z * z / n
    center = (frequency + z * z / (2 * n)) / denominator
    spread = z * sqrt(frequency * (1 - frequency) / n + z * z / (4 * n * n)) / denominator
    return center - spread, center + spread


def infantile_spasms_trial():
    # Sun Table 3, intention-to-treat denominators after the authors' imputation.
    for label, exposed, placebo in (
        ("at least half reduction of spasms", 27, 24),
        ("no spasms for 3 days", 18, 13),
        ("no spasms for 28 days", 15, 10),
        ("post-treatment EEG hypsarrhythmia", 6, 3),
    ):
        n = 35
        p_exposed, p_placebo = exposed / n, placebo / n
        low_exposed, high_exposed = wilson(exposed, n)
        low_placebo, high_placebo = wilson(placebo, n)
        increase = p_exposed - p_placebo
        lower = increase - sqrt((p_exposed - low_exposed) ** 2 + (high_placebo - p_placebo) ** 2)
        upper = increase + sqrt((high_exposed - p_exposed) ** 2 + (p_placebo - low_placebo) ** 2)
        events = exposed + placebo
        observed = comb(n, exposed) * comb(n, placebo)
        weights = (
            comb(n, value) * comb(n, events - value)
            for value in range(max(0, events - n), min(n, events) + 1)
        )
        fisher = sum(weight for weight in weights if weight <= observed) / comb(2 * n, events)
        yield "Sun Table 3", label, "risk difference", f"{exposed}/{n}", f"{placebo}/{n}", increase, lower, upper, fisher


def stage_check():
    # With common nonnegative stage rates, the aggregate ratio is a weighted
    # average of treatment/placebo stage-share ratios, using placebo spikes as weights.
    stage_shares = {
        "N1": (4.0, 4.8),
        "N2": (44.0, 42.6),
        "N3": (32.6, 27.4),
        "REM": (19.4, 25.2),
    }
    ratios = []
    for stage, (melatonin, placebo) in stage_shares.items():
        ratio = melatonin / placebo
        ratios.append(ratio)
        yield "Jain Table 3", f"{stage} stage-share ratio", "ratio", melatonin, placebo, ratio, "NA", "NA", "NA"
    yield "Jain Table 3", "observed marginal spikes per hour ratio", "ratio", 31.7, 71.9, 31.7 / 71.9, "NA", "NA", "NA"
    yield "Jain Table 3", "common-rate stage mixture ratio bounds", "ratio", "NA", "NA", "NA", min(ratios), max(ratios), "NA"
    yield "Jain Table 3", "lowest predicted marginal spikes at fixed stage rates", "spikes/hour of sleep", "NA", 71.9, 71.9 * min(ratios), "NA", "NA", "NA"
    # The N1 and N2 contrasts carry a first-period analysis footnote. The
    # coarser check derives their combined share from the N3 and REM complements.
    early_ratio = (100 - 32.6 - 19.4) / (100 - 27.4 - 25.2)
    coarse_ratios = (early_ratio, ratios[2], ratios[3])
    yield "Jain Table 3", "three-group bounds with common early non-REM rate", "ratio", "NA", "NA", "NA", min(coarse_ratios), max(coarse_ratios), "NA"


def exposure_scale():
    # 1 ng/mL equals 1 microgram/L. Saliva and serum are kept distinct from adult plasma.
    molar_mass = 232.28
    for source, label, pg_ml in (
        ("Sun Table 3", "treated infant 06:00 serum median", 84.8),
        ("Sun Table 3", "placebo infant 06:00 serum median", 17.5),
        ("EMA 5.2", "child prolonged-release saliva Cmax", 410.0),
        ("EMA 5.2", "fed adult prolonged-release plasma Cmax", 3570.0),
    ):
        yield source, label, "nM", pg_ml, "NA", pg_ml / molar_mass, "NA", "NA", "NA"
    adult_cmax = 3570 / molar_mass
    for source, nominal_nm in (("Somalo-Barranco Figure 8", 1000), ("Suofu Figure 5A", 10_000)):
        yield source, "mitochondrial or culture nominal bath / adult label plasma peak", "ratio", nominal_nm, adult_cmax, nominal_nm / adult_cmax, "NA", "NA", "NA"


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("locator", "contrast", "unit", "exposed_input", "control_input", "estimate", "lower", "upper", "two_sided_fisher"))
    for rows in (infantile_spasms_trial(), stage_check(), exposure_scale()):
        for row in rows:
            writer.writerow(f"{value:.7g}" if isinstance(value, float) else value for value in row)


if __name__ == "__main__":
    main()
