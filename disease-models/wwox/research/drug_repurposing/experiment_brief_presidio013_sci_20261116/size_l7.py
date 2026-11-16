#!/usr/bin/env python3
"""Animals per arm for the L7 slice experiment, as a range under stated assumptions (NX1-style; no data are read).

Two-sided test of a difference between two groups with equal n, normal approximation plus the Guenther t correction
(n + z_alpha^2 / 4), as in nx1_sizing_sci_20261115/size_nx1.py. The unit is the ANIMAL: slices or cells are averaged
within animal first (design effect 1 + (m - 1) * ICC for cells within animal).

Prints a table to standard output and, when given a directory, writes sizing.tsv there. No input files, no network.
Usage: size_l7.py [OUTPUT_DIR]
"""
import csv
import math
import os
import sys

Z = {0.05: 1.959964, 0.0083333: 2.638, 0.8: 0.841621, 0.9: 1.281552}


def n_per_group(sd, delta, alpha_key=0.05, power=0.8):
    za, zb = Z[alpha_key], Z[power]
    n = 2.0 * ((za + zb) * sd / delta) ** 2 + za ** 2 / 4.0
    return math.ceil(n)


def main(outdir=None):
    rows = []
    # (1) WO-10 with a genotype contrast: NAM-sensitive fraction, percentage points; Mierau 2004 gives 14% (0-34), n 15/10 cells,
    # a bootstrap interval of about 34 points, hence a between-cell SD of roughly 27 points (rough: ratio of means, not a SD).
    for sd in (20, 27, 35):
        for delta in (26, 20):
            for m, icc in ((3, 0.2), (3, 0.5)):
                n_cells = n_per_group(sd, delta)
                de = 1 + (m - 1) * icc
                animals = math.ceil(n_cells * de / m)
                rows.append(("WO-10 NAM-sensitive fraction, KO v WT", f"SD {sd} pts, delta {delta} pts, {m} cells/animal, ICC {icc}",
                             "one test, alpha 0.05, power 0.8", n_cells, animals))
    # (2) one primary comparison on burst suppression, animal-level proportional change, paired within slice
    for sd in (0.2, 0.3, 0.4):
        for delta in (0.3, 0.4):
            rows.append(("burst suppression, arm v vehicle or arm v arm (one primary comparison)", f"SD of animal-level proportional change {sd}, delta {delta}",
                         "alpha 0.05, power 0.8", n_per_group(sd, delta), n_per_group(sd, delta)))
    # (3) several arms vs one control: Bonferroni over 6 comparisons
    for sd in (0.2, 0.3, 0.4):
        rows.append(("burst suppression, six arms each v vehicle (Bonferroni 0.05/6)", f"SD {sd}, delta 0.4", "alpha 0.0083, power 0.8",
                     n_per_group(sd, 0.4, 0.0083333), n_per_group(sd, 0.4, 0.0083333)))
    # (4) genotype contrast of drug effect: difference of proportional suppression, KO v WT-provoked
    for sd in (0.2, 0.3, 0.4):
        rows.append(("drug-by-genotype: suppression in KO v WT-provoked", f"SD {sd}, delta 0.3", "alpha 0.05, power 0.8",
                     n_per_group(sd, 0.3), n_per_group(sd, 0.3)))
    # (5) ADV H-ADV-5 addendum 2026-11-16: genotype x exposure-level interaction on the ratio scale (two levels per arm, same animals).
    # The contrast is (suppression at level 2 - at level 1) in KO minus the same in provoked WT; its SD is SD * sqrt(2 * (1 - rho)), rho = correlation
    # of an animal's proportional suppression at the two levels. delta = 0.3 difference of differences.
    for rho in (0.0, 0.5, 0.8):
        for sd in (0.2, 0.3, 0.4):
            sdc = sd * math.sqrt(2.0 * (1.0 - rho))
            rows.append(("curve shape: genotype x level interaction, ratio scale (ADV H-ADV-5)", f"SD {sd} per level, rho {rho} (contrast SD {sdc:.2f}), delta 0.3",
                         "alpha 0.05, power 0.8", n_per_group(sdc, 0.3), n_per_group(sdc, 0.3)))
    out = ["test\tassumptions\ttest_setting\tn_per_group_cells_or_animals\tanimals_per_group"]
    out += ["\t".join(str(x) for x in r) for r in rows]
    text = "\n".join(out) + "\n"
    sys.stdout.write(text)
    if outdir:
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "sizing.tsv"), "w") as f:
            f.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
