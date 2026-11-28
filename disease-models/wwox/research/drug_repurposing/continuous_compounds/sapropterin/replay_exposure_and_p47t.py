"""Replay sapropterin evidence arithmetic and the adult Wwox-P47T transfer check."""

import argparse
import csv
import gzip
from hashlib import sha256
from math import exp, lgamma, log, log1p, log2
from pathlib import Path
from statistics import mean
import sys


HERE = Path(__file__).resolve().parent
GENES = ("Spr", "Gch1", "Pts", "Qdpr", "Dhfr", "Nos1", "Nos2", "Nos3")
REGIONS = ("HPC", "CTX", "PFC")
P47T_SHA256 = "d654f6bdd2a4ac5b3e24741f16962503a711575c72aa92a2c729a7a0cf04c18c"


def anova_tail(statistic, numerator_df, denominator_df):
    """Integrate the transformed F tail with Simpson quadrature."""
    a, b = denominator_df / 2, numerator_df / 2
    upper = denominator_df / (denominator_df + numerator_df * statistic)
    log_beta = lgamma(a) + lgamma(b) - lgamma(a + b)

    def density(z):
        return exp((a - 1) * log(z) + (b - 1) * log1p(-z) - log_beta)

    panels = 8192
    step = upper / panels
    interior = sum((4 if i % 2 else 2) * density(i * step) for i in range(1, panels))
    return step * (density(upper) + interior) / 3


def exposure_rows():
    yield ("comparison", "source_input_1", "source_input_2", "estimate", "units")
    total = 22.8 / 9.9
    yield ("Winn two_hour_total_biopterin_ratio", "22.8", "9.9", total, "treated_over_vehicle")
    for baseline_reduced in (0.2, 0.5, 0.8):
        yield ("Winn break_even_treated_reduced_fraction", baseline_reduced, total,
               baseline_reduced / total, "fraction_of_total")
    yield ("Winn hypothetical_lower_BH4", 0.2, 0.8, total * (0.2 / 0.8), "treated_over_vehicle")
    for label, statistic, df1, df2 in (
        ("Winn total_biopterin_treatment", 14.4, 3, 79), ("Winn HVA_treatment", 4.077, 3, 79),
        ("Winn 5HIAA_treatment", 15.97, 3, 79), ("Winn reported_5HIAA_genotype_F", 2.37, 1, 79),
    ):
        yield (label, statistic, f"{df1},{df2}", anova_tail(statistic, df1, df2), "F_right_tail")
    for hours, control, bh2 in ((0, 215, 208), (24, 160, 156), (48, 128, 131)):
        yield (f"Heine preloaded_Sf9_nNOS_{hours}h", bh2, control, bh2 / control, "BH2_over_no_BH2")
    for time, bh4, bh2 in (("baseline", 12, 28), ("first_followup", 12, 31), ("second_followup", 16, 27)):
        yield (f"Coughlin CSF_BH4_to_BH2_{time}", bh4, bh2, bh4 / bh2, "molar_ratio")

    # Fig. 4C left white bars and hatched tops (before, 30 min). Height in
    # pixels above the same zero is proportional to biopterin concentration.
    baseline_top, treated_top, baseline_blood, treated_blood, zero = 441, 366, 672, 641, 676
    yield ("Ohashi Fig4C left_rat_total_before_to_30min", treated_top, baseline_top,
           (zero - treated_top) / (zero - baseline_top), "pixel_derived_treated_over_before")
    yield ("Ohashi Fig4C left_rat_blood_subtracted_before_to_30min",
           f"{treated_top},{treated_blood}", f"{baseline_top},{baseline_blood}",
           (treated_blood - treated_top) / (baseline_blood - baseline_top), "pixel_derived_treated_over_before")

    clearance, volume, absorption = 2780, 3870, 0.234
    yield ("SPARK implied_elimination_half_life", clearance, volume, log(2) * volume / clearance, "hours")
    yield ("SPARK implied_absorption_half_life", absorption, "ln(2)", log(2) / absorption, "hours")


def p47t_rows(path):
    sys.path.insert(0, str(HERE.parent.parent / "perampanel_kainate_20261123"))
    from p47t_analysis import contrast

    if sha256(path.read_bytes()).hexdigest() != P47T_SHA256:
        raise ValueError("GSE215425 counts do not match the pinned release")
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        rows = csv.reader(handle, delimiter="\t")
        samples = next(rows)[2:]
        totals = [0] * len(samples)
        counts = {gene: [0] * len(samples) for gene in GENES}
        for _, symbol, *values in rows:
            numeric = [int(value) for value in values]
            totals = [total + value for total, value in zip(totals, numeric, strict=True)]
            if symbol in counts:
                counts[symbol] = [total + value for total, value in zip(counts[symbol], numeric, strict=True)]
    yield ("region", "gene", "wt_n", "p47t_n", "wt_mean_cpm", "p47t_mean_cpm", "sex_balanced_delta_log2",
           "female_delta_log2", "male_delta_log2", "omit_min", "omit_max")
    for region in REGIONS:
        columns = [i for i, name in enumerate(samples) if name.startswith(region + "_")]
        groups = [(samples[i].split("_")[1].split("/")[0], samples[i].split("_")[2][0]) for i in columns]
        wt_n = sum(genotype == "WT" for genotype, _ in groups)
        p47t_n = sum(genotype == "P47T" for genotype, _ in groups)
        if (wt_n, p47t_n) != (5, 5):
            raise ValueError(f"Unexpected animal count in {region}")
        for gene, values in counts.items():
            cpm = [1e6 * values[i] / totals[i] for i in columns]
            group_means = [mean(value for value, (genotype, _) in zip(cpm, groups) if genotype == arm)
                           for arm in ("WT", "P47T")]
            shifts = contrast([log2(1 + value) for value in cpm], groups)
            yield (region, gene, wt_n, p47t_n, *(f"{v:.6g}" for v in (*group_means, *shifts)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--counts", type=Path, help="Emit adult P47T RNA comparison from GSE215425")
    args = parser.parse_args()
    rows = p47t_rows(args.counts) if args.counts else exposure_rows()
    csv.writer(sys.stdout, delimiter="\t", lineterminator="\n").writerows(rows)


if __name__ == "__main__":
    main()
