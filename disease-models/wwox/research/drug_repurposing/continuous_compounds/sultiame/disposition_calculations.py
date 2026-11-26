#!/usr/bin/env python3
"""Reproduce selected Manthey Table 5 contrasts and the exposure sensitivity."""
import csv
import sys


writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("comparison", "endpoint", "reference", "comparison_value", "derived", "quantity"))

# Manthey thesis p. 42, means per mm³, P7 at dosing, 24 h. Single high-dose group.
for region, vehicle, sultiame in (
    ("frontal_cortex_II", 1626, 16072),
    ("mediodorsal_thalamus", 136, 21940),
    ("dentate_gyrus", 220, 2729),
    ("CA1", 327, 2106),
):
    writer.writerow(("rat_histology_300_mg_per_kg", region, vehicle, sultiame,
                     f"{sultiame / vehicle:.3f}", "sultiame_over_vehicle_mean"))

# SmPC protein binding is a conditional assumption, not a cohort measurement.
plasma_unbound_fraction = 0.71
sodium_bath_low = 1000 / 290.4
sodium_bath_high = 10000 / 290.4
acidification_bath_low = 1000
for sample, total_micromolar in (
    ("adult_single_peak_geometric_mean", 1.88 * 1000 / 290.4),
    ("adult_repeat_high_group_mean_trough", 5.68 * 1000 / 290.4),
    ("adult_repeat_high_group_max_trough", 9.37 * 1000 / 290.4),
):
    for endpoint, nominal in (
        ("reported_sodium_lower", sodium_bath_low),
        ("reported_sodium_upper", sodium_bath_high),
        ("reported_slice_acidification_lower", acidification_bath_low),
    ):
        required_ratio = nominal / (total_micromolar * plasma_unbound_fraction)
        writer.writerow((sample, endpoint, f"{total_micromolar:.4f}", f"{nominal:.4f}",
                         f"{required_ratio:.4f}", "required_unbound_brain_to_plasma_ratio"))
