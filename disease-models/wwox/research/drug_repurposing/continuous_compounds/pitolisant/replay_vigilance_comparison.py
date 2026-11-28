"""Replay aggregate uncertainty, exposure scales and a vigilance counterexample."""

import csv
from math import sqrt
import sys


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "scope", "unit", "value"))

    def emit(comparison, scope, unit, value):
        writer.writerow((comparison, scope, unit, f"{value:.6f}"))

    # P03-06 primary abstract. Abolition is a subset and shares the denominator.
    sample_size = 14
    normal_quantile = 1.95996398454
    for label, count in (("reduced_range", 9), ("abolished_response", 6)):
        observed = count / sample_size
        divisor = 1 + normal_quantile**2 / sample_size
        center = (observed + normal_quantile**2 / (2 * sample_size)) / divisor
        radius = normal_quantile * sqrt(
            observed * (1 - observed) / sample_size + normal_quantile**2 / (4 * sample_size**2)
        ) / divisor
        emit("observed", label, "fraction", observed)
        emit("wilson_95_low", label, "fraction", center - radius)
        emit("wilson_95_high", label, "fraction", center + radius)

    # Rusjan serum concentrations; FDA label PK and binding; parent molecular mass.
    molecular_weight = 295.85
    for sample, concentration in (("pet_start", 16.6), ("pet_end", 25.1), ("adult_steady_peak", 73)):
        for endpoint, free_fraction in (("estimated_free_low", 0.04), ("estimated_free_high", 0.09)):
            emit(endpoint, sample, "nM", concentration * 1000 * free_fraction / molecular_weight)

    # Synthetic rates by state and state proportions. No inputs are patient data.
    reference_high_state = 0.60
    for scenario, high_share, high_rate, low_rate in (
        ("baseline", reference_high_state, 12, 2),
        ("state_mix_only", 0.20, 12, 2),
        ("within_state_effect_only", reference_high_state, 6, 1),
    ):
        crude = high_share * high_rate + (1 - high_share) * low_rate
        standardized = reference_high_state * high_rate + (1 - reference_high_state) * low_rate
        emit("synthetic_crude_rate", scenario, "events/hour", crude)
        emit("synthetic_state_standardized_rate", scenario, "events/hour", standardized)


if __name__ == "__main__":
    main()
