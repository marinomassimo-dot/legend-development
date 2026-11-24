"""Sensitivity of two-GluN1 receptor compositions to pairing of cassette-bearing units."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("population", "unit_fraction", "endpoint", "min_pct", "independent_pct", "max_pct"))
for arm, p in [("control", 0.2209), ("KO", 0.3223)]:
    # Let b be the fraction of receptors with two included units. Then
    # the fraction with exactly one is 2*p-2*b, and with at least one is 2*p-b.
    lower, upper = max(0, 2*p-1), p
    for name, low, independent, high in [
        ("two_included", lower, p*p, upper),
        ("any_included", 2*p-upper, 2*p-p*p, 2*p-lower)
    ]:
        writer.writerow((arm, p, name, *(f"{100*v:.2f}" for v in (low, independent, high))))
