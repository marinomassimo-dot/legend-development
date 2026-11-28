#!/usr/bin/env python3
"""Replay aggregate population contrasts and a hypothetical GABA reversal bound."""

from math import hypot, log, sqrt
from statistics import NormalDist


def wilson(events, total):
    fraction = events / total
    z = NormalDist().inv_cdf(0.975)
    denominator = 1 + z**2 / total
    center = (fraction + z**2 / (2 * total)) / denominator
    half = z * sqrt(fraction * (1 - fraction) / total + z**2 / (4 * total**2)) / denominator
    return center - half, center + half


def risk_difference(first_events, first_total, second_events, second_total):
    p = first_events / first_total
    q = second_events / second_total
    lower_p, upper_p = wilson(first_events, first_total)
    lower_q, upper_q = wilson(second_events, second_total)
    point = p - q
    return (
        100 * point,
        100 * (point - hypot(p - lower_p, upper_q - q)),
        100 * (point + hypot(upper_p - p, q - lower_q)),
    )


def gaba_reversal(chloride_in, chloride_out, bicarbonate_in, bicarbonate_out, permeability):
    """Two-anion GHK model with concentrations as activity proxies, at 37 C."""
    thermodynamic_mv = 1000 * 8.314462618 * 310.15 / 96485.33212
    return thermodynamic_mv * log(
        (chloride_in + permeability * bicarbonate_in)
        / (chloride_out + permeability * bicarbonate_out)
    )


print("block\tcontrast\tvalue\tlower\tupper\tunit")
# Bjurulf Table 3 and McNally Results. The McNally rows overlap
# and answer questions about different exposure group definitions.
cohort_comparisons = (
    ("Bjurulf_reported_acidosis", (0, 22, 10, 29)),
    ("Bjurulf_7_month_seizure_reduction_gt50pct", (9, 22, 8, 29)),
    ("McNally_recorded_exposure_stones", (4, 198, 11, 105)),
    ("McNally_empiric_policy_acceptors_stones", (1, 106, 13, 195)),
    ("McNally_empiric_era_all_stones", (2, 108, 13, 195)),
)
for contrast, counts in cohort_comparisons:
    value, lower, upper = risk_difference(*counts)
    print(f"observed\t{contrast}\t{value:.3f}\t{lower:.3f}\t{upper:.3f}\tpercentage_points")

# Hypothetical neural saline conditions, never fitted to a clinical pH value.
chloride_out, bicarbonate_out = 130, 18
bicarbonate_in, bicarbonate_increment = 10, 6
for ratio in (0.2, 0.4):
    for chloride_in in (5, 10, 20):
        key = f"permeability_{ratio}_Cl_in_{chloride_in}"
        opening = gaba_reversal(chloride_in, chloride_out, bicarbonate_in, bicarbonate_out, ratio)
        for inside_delta in (0, bicarbonate_increment):
            end = gaba_reversal(
                chloride_in, chloride_out, bicarbonate_in + inside_delta,
                bicarbonate_out + bicarbonate_increment, ratio,
            )
            print(f"hypothetical\t{key}_HCO3_in_delta_{inside_delta}\t{end - opening:.3f}\tNA\tNA\tmV")
        crossover = (
            bicarbonate_increment * (chloride_in + ratio * bicarbonate_in)
            / (chloride_out + ratio * bicarbonate_out)
        )
        print(f"hypothetical\t{key}_HCO3_in_crossover\t{crossover:.3f}\tNA\tNA\tmM")

# Henderson–Hasselbalch illustration at constant chosen pH, using rounded
# 37 C blood buffer constants solely to demonstrate a linked variable.
for bicarbonate in (18, 24):
    pco2 = bicarbonate / (0.03 * 10 ** (7.30 - 6.1))
    print(f"hypothetical\tpCO2_for_HCO3_{bicarbonate}_at_pH_7.30\t{pco2:.3f}\tNA\tNA\tmmHg")
