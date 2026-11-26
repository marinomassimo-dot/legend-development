"""Replay figure estimates and F tests with one numerator degree of freedom."""

import argparse
import csv
from math import atan, cos, pi, sqrt
from pathlib import Path


def simpson_cos_power(lower, exponent):
    steps = 2048
    step = (pi / 2 - lower) / steps
    total = cos(lower) ** exponent
    for pos in range(1, steps):
        weight = 4 if pos % 2 else 2
        total += weight * cos(lower + step * pos) ** exponent
    total += cos(pi / 2) ** exponent
    return total * step / 3


def f_tail(f_value, df_denominator):
    # F(1, nu) is squared Student t(nu). With t = sqrt(nu)*tan(theta),
    # the two-sided t tail reduces to a ratio of integrals of cos(theta)^(nu-1).
    lower = atan(sqrt(f_value / df_denominator))
    exponent = df_denominator - 1
    return simpson_cos_power(lower, exponent) / simpson_cos_power(0, exponent)


def estimate(row, field):
    if row[field] == "NA":
        return None
    upper_y = float(row["upper_y"])
    lower_y = float(row["lower_y"])
    upper_value = float(row["upper_value"])
    lower_value = float(row["lower_value"])
    position = (float(row[field]) - lower_y) / (upper_y - lower_y)
    return lower_value + position * (upper_value - lower_value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("figure_inputs", type=Path)
    parser.add_argument("f_inputs", type=Path)
    args = parser.parse_args()
    fields = ("ctl_vehicle", "pa_or_challenge_vehicle", "ctl_pea", "pa_or_challenge_pea", "mk886", "gw9662")
    print("figure_endpoint", *fields, "difference_in_differences", sep="	")
    with args.figure_inputs.open() as stream:
        for row in csv.DictReader(stream, delimiter="	"):
            values = [estimate(row, field) for field in fields]
            difference = None
            if all(value is not None for value in values[:4]):
                control, injured, control_treated, injured_treated = values[:4]
                difference = (injured_treated - injured) - (control_treated - control)
            formatted = ["NA" if value is None else f"{value:.2f}" for value in (*values, difference)]
            print(row["endpoint"], *formatted, sep="	")
    print("tested_endpoint", "term", "printed_p", "recomputed_p", sep="	")
    with args.f_inputs.open() as stream:
        for row in csv.DictReader(stream, delimiter="	"):
            p = f_tail(float(row["F"]), int(row["df_denominator"]))
            print(row["endpoint"], row["term"], row["printed_p"], f"{p:.6f}", sep="	")


if __name__ == "__main__":
    main()
