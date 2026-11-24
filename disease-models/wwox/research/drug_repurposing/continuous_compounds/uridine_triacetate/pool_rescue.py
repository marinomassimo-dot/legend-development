"""Recalculate whole-cell dNTP contrasts from Pontarin et al., Table 1 (PMID 22847445)."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("pool", "ctrl_vehicle", "ctrl_CdR_GdR", "mut_vehicle", "mut_CdR_GdR",
                 "mut_treated_over_vehicle", "mut_treated_over_ctrl_vehicle",
                 "mut_treated_over_ctrl_treated"))
for name, control, control_pair, mutant, mutant_pair in (
    ("dCTP", 2.9, 4.5, 1.2, 3.8),
    ("dGTP", 0.5, 1.2, 0.2, 0.8),
    ("dTTP", 2.6, 2.9, 2.7, 3.4),
    ("dATP", 2.4, 2.0, 1.4, 1.4),
):
    ratios = (mutant_pair / mutant, mutant_pair / control, mutant_pair / control_pair)
    writer.writerow([name, control, control_pair, mutant, mutant_pair, *(f"{v:.3f}" for v in ratios)])
