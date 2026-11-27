"""Recompute published-exposure and safety contrasts without pooling populations."""
import argparse
import csv
import math
from pathlib import Path
from statistics import NormalDist


def wilson(events, n):
    p = events / n
    z = NormalDist().inv_cdf(0.975)
    divisor = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / divisor
    half_width = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / divisor
    return center - half_width, center + half_width


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    randomized = 83
    gg_events, gg_completers = 6, 34
    control_events, control_completers = 5, 32
    gg_rate = gg_events / gg_completers
    control_rate = control_events / control_completers
    gg_low, gg_high = wilson(gg_events, gg_completers)
    control_low, control_high = wilson(control_events, control_completers)
    difference = gg_rate - control_rate
    diff_low = difference - math.hypot(gg_rate - gg_low, control_high - control_rate)
    diff_high = difference + math.hypot(gg_high - gg_rate, control_rate - control_low)

    adult = "Gheith et al. 2023, §§2.2 and 3.4; denominators are study completers"
    kotti = "Kotti et al. 2008, nominal bath concentration in Fig. 2D and Results"
    rows = [
        ("Adult randomized", randomized, "participants", adult),
        ("Adult analyzed", gg_completers + control_completers, "participants", adult),
        ("Adult not in analysis", randomized - gg_completers - control_completers,
         "participants", adult),
        ("Adult at least one reported AE, active", f"{gg_rate * 100:.3f}", "%", adult),
        ("Adult at least one reported AE, placebo", f"{control_rate * 100:.3f}", "%", adult),
        ("Adult difference active minus placebo", f"{difference * 100:.3f}", "percentage points", adult),
        ("Adult difference Newcombe 95% lower", f"{diff_low * 100:.3f}", "percentage points", adult),
        ("Adult difference Newcombe 95% upper", f"{diff_high * 100:.3f}", "percentage points", adult),
        ("Adult zero-serious-event upper limit under active completer denominator",
         f"{(1 - 0.05**(1 / gg_completers)) * 100:.3f}", "%, one-sided 95% exact binomial", adult),
        ("Minimum exact two-sided signed-rank p for three nonzero pairs",
         f"{2 / 2**3:.3f}", "probability", "Sediva et al. 2024, Fig. S1, 3 paired adults"),
        ("Slice concentration", 200, "µM, nominal in perfusate", kotti),
        ("Slice concentration", f"{200 * 290.4834 / 1000:.3f}", "µg/mL, nominal in perfusate", kotti),
    ]
    with args.output.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(("comparison", "value", "unit", "basis"))
        writer.writerows(rows)


if __name__ == "__main__":
    main()
