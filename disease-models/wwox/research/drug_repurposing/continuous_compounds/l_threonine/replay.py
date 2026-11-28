"""Reproduce aggregate L-threonine contrasts and exact paired sign comparisons."""

import csv
from math import comb
import sys


# Hauser et al. p. 925, paired outcome figure, 21 completers.
# Rows are placebo, columns L-threonine. Both follow improved, same, worse.
HAUSER_MATRICES = {
    "clinician spasticity": ((1, 3, 1), (8, 4, 0), (2, 2, 0)),
    "patient spasticity": ((1, 2, 1), (3, 3, 4), (4, 1, 2)),
    "clinician global": ((2, 4, 1), (5, 3, 3), (1, 1, 1)),
    "patient global": ((1, 1, 1), (2, 5, 4), (3, 1, 3)),
}


def relative_change(placebo, treatment):
    return 100 * (treatment / placebo - 1)


def exact_sign_p(wins, losses):
    n = wins + losses
    return min(1.0, 2 * sum(comb(n, k) for k in range(min(wins, losses) + 1)) / 2**n)


def comparison():
    hauser_locus = "Hauser 1992 p. 925 paired figure"
    for name, matrix in HAUSER_MATRICES.items():
        wins = sum(matrix[row][col] for row in range(3) for col in range(row))
        losses = sum(matrix[row][col] for row in range(3) for col in range(row + 1, 3))
        ties = sum(matrix[i][i] for i in range(3))
        assert wins + losses + ties == 21
        yield name, "favors threonine", wins, "participants", hauser_locus
        yield name, "favors placebo", losses, "participants", hauser_locus
        yield name, "ties", ties, "participants", hauser_locus
        yield name, "exact two-sided sign p", exact_sign_p(wins, losses), "probability", hauser_locus

    # Clinician scale, reduced to I versus S/W. This tests a different endpoint.
    matrix = HAUSER_MATRICES["clinician spasticity"]
    threonine_only = matrix[1][0] + matrix[2][0]
    placebo_only = matrix[0][1] + matrix[0][2]
    yield "clinician spasticity", "improved on threonine only", threonine_only, "participants", hauser_locus
    yield "clinician spasticity", "improved on placebo only", placebo_only, "participants", hauser_locus
    yield "clinician spasticity", "binary improvement exact McNemar p", exact_sign_p(threonine_only, placebo_only), "probability", hauser_locus

    for name, placebo, treatment, unit, locus in (
        ("Growdon lumbar threonine", 51.0, 101.0, "µM", "Growdon 1991 Table 3"),
        ("Growdon lumbar glycine", 8.4, 7.6, "µM", "Growdon 1991 Table 3"),
        ("Hauser lumbar threonine", 33.3, 118.8, "table units unstated", "Hauser 1992 labeled Table 3"),
        ("Hauser lumbar glycine", 6.8, 6.0, "table units unstated", "Hauser 1992 labeled Table 3"),
        ("juvenile rat C vs B brain tissue glycine", 4.4, 6.0, "nmol/mg protein", "Castagné 1994 Table II"),
        ("juvenile rat C vs B brain tissue threonine", 10.3, 43.4, "nmol/mg protein", "Castagné 1994 Table II"),
        ("juvenile rat C vs B plasma glycine", 342, 922, "nmol/mL", "Castagné 1994 Table II"),
    ):
        yield name, "difference of reported means", treatment - placebo, unit, locus
        yield name, "relative difference of means", relative_change(placebo, treatment), "%", locus

    for diet, glycine, carbon_dioxide in (("control", 1.6, 15), ("free Thr", 3.5, 49), ("protein Thr", 3.4, 45)):
        locus = "Darling 2000 abstract, ratio of rate means"
        fraction = glycine / (glycine + carbon_dioxide)
        yield f"adult systemic tracer {diet}", "glycine share of two modeled disposal routes", 100 * fraction, "%", locus


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("comparison", "statistic", "value", "unit", "locator"))
    for name, statistic, value, unit, locator in comparison():
        writer.writerow((name, statistic, f"{value:.8g}", unit, locator))


if __name__ == "__main__":
    main()
