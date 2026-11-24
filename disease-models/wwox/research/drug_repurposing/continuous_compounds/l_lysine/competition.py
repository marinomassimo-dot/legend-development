"""One shared carrier: conditional flux changes; these parameters are not fitted to WWOX."""
from itertools import product
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("input", "Lys_uM", "Arg_uM", "Orn_uM", "Lys_multiplier",
                 "Lys_flux_ratio_min", "Lys_flux_ratio_max", "Arg_flux_ratio_min",
                 "Arg_flux_ratio_max"))
lys, arg, orn = 321, 103, 53  # Healthy mouse plasma group means in Dolgodilina Table 1
for change in (1.1, 1.25, 1.5):
    lys_ratios, arg_ratios = [], []
    for k_l, k_a, k_o in product((50, 100), repeat=3):
        first = 1 + lys/k_l + arg/k_a + orn/k_o
        second = first + (change-1)*lys/k_l
        arg_ratios.append(first/second)
        lys_ratios.append(change*first/second)
    writer.writerow(("plasma_scenario", lys, arg, orn, change,
                     *(f"{v:.4f}" for v in (min(lys_ratios), max(lys_ratios),
                                             min(arg_ratios), max(arg_ratios)))))
