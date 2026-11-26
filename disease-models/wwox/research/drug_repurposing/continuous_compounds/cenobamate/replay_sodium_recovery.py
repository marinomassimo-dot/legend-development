"""Reconstruct normalized recoverable amplitudes from Nakamura et al., Fig. 5D."""

import csv
import sys
from math import expm1

# (amplitude, recovery time constant in ms) from §3.4, n=5 animals per fitted curve.
CONTROL = ((0.66, 4.7), (0.36, 25.7))
CENOBAMATE_100_UM = ((0.55, 11.7), (0.38, 134.6))


def recovered_fraction(interval_ms, components):
    recovered = sum(-amplitude * expm1(-interval_ms / tau_ms) for amplitude, tau_ms in components)
    return recovered / sum(amplitude for amplitude, _ in components)


def main():
    table = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    table.writerow(("interval_ms", "vehicle_recovered_pct", "cenobamate_100_uM_recovered_pct",
                    "difference_percentage_points"))
    for interval_ms in (5, 10, 20, 50, 100, 200):
        control = 100 * recovered_fraction(interval_ms, CONTROL)
        cenobamate = 100 * recovered_fraction(interval_ms, CENOBAMATE_100_UM)
        table.writerow((interval_ms, f"{control:.2f}", f"{cenobamate:.2f}", f"{cenobamate - control:.2f}"))


if __name__ == "__main__":
    main()
