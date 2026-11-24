"""Illustrative change in a two-halide reversal potential at fixed total halide."""
import csv
import math
import sys

ratio = 1.51  # PBr/PCl from Suzuki et al., PMID 7843172
thermal_mv = 1000 * 8.314462618 * 310.15 / 96485.33212
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(["outside_bromide_mM", "outside_total_halide_mM", "inside_fraction_relative_to_outside", "delta_E_mV"])
for outside_bromide in (10, 20):
    outside_fraction = outside_bromide / 159
    for relative in (0, 0.5, 1, 2):
        inside_fraction = relative * outside_fraction
        shift = thermal_mv * math.log((1 + (ratio - 1) * inside_fraction)
                                      / (1 + (ratio - 1) * outside_fraction))
        writer.writerow([outside_bromide, 159, relative, f"{shift:.3f}"])
