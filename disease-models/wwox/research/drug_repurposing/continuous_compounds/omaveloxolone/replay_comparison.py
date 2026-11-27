"""Replay omaveloxolone comparisons from reported numbers and fixed plot coordinates."""

import csv
from math import atan, comb, cos, gamma, pi, sqrt
from statistics import mean
import sys

FDA_MODELED_TOTAL_PLASMA_PEAK_NG_ML = 72.0
FDA_UNBOUND_PLASMA_FRACTION = 0.03
MOLAR_MASS_G_MOL = 554.72


def figure_rows():
    # Reisman p. 1264, PDF p. 6 rendered at 175 dpi. Allow two pixels
    # for each border on the log axis independently. Units remain mL/g.
    decade_px = (1528 - 1257) / 3
    for arm, plasma_y, brain_y in (
        ("low", 1494, 1451),
        ("middle", 1460, 1402),
        ("high", 1410, 1359),
    ):
        log_delta_px = plasma_y - brain_y
        ratio = 10 ** (log_delta_px / decade_px)
        lo = 10 ** ((log_delta_px - 4) / decade_px)
        hi = 10 ** ((log_delta_px + 4) / decade_px)
        yield ("Reisman Fig. 3", f"{arm} arm total brain/plasma",
               f"{ratio:.2f}", "mL/g", f"Digitized means. Pixel sensitivity {lo:.2f}–{hi:.2f}; not an uncertainty interval.")

    # Shekh-Ahmad 2018 UCL accepted manuscript p. 44 at 145 dpi.
    # Top of contiguous colored fill rather than the central error bar.
    vehicle_y = (514, 518, 497, 507, 485, 484, 477, 462, 430, 436, 428, 395)
    treated_y = (529, 523, 523, 523, 529, 529, 529, 521, 523, 528, 531, 528)
    y_zero, y_40 = 536, 317
    for label, start, stop in (("weeks 1–2", 0, 2), ("weeks 9–12", 8, 12)):
        vehicle = mean(40 * (y_zero - y) / (y_zero - y_40) for y in vehicle_y[start:stop])
        treated = mean(40 * (y_zero - y) / (y_zero - y_40) for y in treated_y[start:stop])
        yield ("Shekh-Ahmad Fig. 5C", f"vehicle in {label}", f"{vehicle:.2f}", "seizures/week", "Mean of plotted weekly means.")
        yield ("Shekh-Ahmad Fig. 5C", f"RTA 408 in {label}", f"{treated:.2f}", "seizures/week", "Mean of plotted weekly means.")
        yield ("Shekh-Ahmad Fig. 5C", f"relative change in {label}",
               f"{100 * (treated / vehicle - 1):.2f}", "percent", "Descriptive and event-aligned; no animal-level values.")


def two_sided_t_p(statistic, df):
    # Integrate after the substitution t = sqrt(df) * tan(theta).
    steps = 2000
    start = atan(abs(statistic) / sqrt(df))
    step = (pi / 2 - start) / steps
    area = step * sum(cos(start + (i + 0.5) * step) ** (df - 1) for i in range(steps))
    return 2 * gamma((df + 1) / 2) * area / (sqrt(pi) * gamma(df / 2))


def rows():
    yield from figure_rows()
    for panel, statistic, printed_p in (("2C", 1.644, 0.129), ("2D", 2.245, 0.811)):
        yield ("Shekh-Ahmad 2018", f"two-sided p implied by Fig. {panel} t(11)",
               f"{two_sided_t_p(statistic, 11):.4f}", "p", f"Printed p = {printed_p:.3f}; no correction inferred.")
    # One seizure-free control and OR=4 with 9 rats in each arm imply 3 seizure-free treated rats.
    weights = [comb(9, count) * comb(9, 4 - count) for count in range(5)]
    fisher_p = sum(weight for weight in weights if weight <= weights[3]) / sum(weights)
    yield ("Shekh-Ahmad 2018", "seizure-free Fisher exact reconstruction",
           f"{fisher_p:.4f}", "p", "Assumes the implied counts 3/9 vs 1/9; not a published test.")
    free_plasma_peak_nm = (
        1_000 * FDA_MODELED_TOTAL_PLASMA_PEAK_NG_ML
        * FDA_UNBOUND_PLASMA_FRACTION / MOLAR_MASS_G_MOL
    )
    yield (
        "FDA QT review",
        "modeled free plasma peak",
        f"{free_plasma_peak_nm:.4f}",
        "nM",
        "Plasma estimate, with 3% unbound fraction and rounded total Cmax.",
    )
    for nominal_culture_nm in (50, 200):
        yield (
            "Shekh-Ahmad Fig. 2 vs FDA QT review",
            f"{nominal_culture_nm} nM nominal culture divided by plasma estimate",
            f"{nominal_culture_nm / free_plasma_peak_nm:.2f}",
            "ratio",
            "Different compartments and binding conditions.",
        )
    # Sensitivity only: no brain unbound fraction was measured here.
    for species, plasma_unbound, total_ratio_range in (
        ("mouse", 0.073, (0.877, 1.40)),
        ("rat", 0.053, (1.40, 1.51)),
        ("cynomolgus monkey", 0.052, (3.94, 5.27)),
    ):
        minimum_ratio, maximum_ratio = total_ratio_range
        yield (
            "FDA nonclinical review and EMA EPAR",
            f"{species} brain unbound fraction needed for unbound ratio of one",
            f"{100 * plasma_unbound / maximum_ratio:.2f}–{100 * plasma_unbound / minimum_ratio:.2f}",
            "percent",
            "Illustrative whole-tissue relation using time-specific total ratios, not a measured free ratio.",
        )
    yield (
        "Shekh-Ahmad Results/Fig. 5",
        "relative change using printed rounded medians",
        f"{100 * (1 / 23 - 1):.2f}",
        "percent",
        "Printed endpoints are 23 and 1 seizures/week. Authors report a 94% reduction.",
    )
    yield (
        "Shekh-Ahmad Fig. 5C-D",
        "fraction of initial EEG group contributing to extended follow-up",
        f"{100 * 4 / 9:.2f}",
        "percent",
        "Four of nine per arm beyond week 12.",
    )


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "comparison", "value", "unit", "limitation"))
    writer.writerows(rows())


if __name__ == "__main__":
    main()
