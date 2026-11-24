"""Nominal glycine from the two reference basal formulations, before supplements."""
from decimal import Decimal as D
import csv
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("medium", "glycine_mg_L", "molecular_weight_g_mol", "nominal_uM"))
values = []
for medium, mg_l in [("DMEM_F12_329",D("18.75")),("Neurobasal_251",D("30.0"))]:
    concentration = mg_l / D(75) * 1000
    values.append(concentration)
    writer.writerow((medium,mg_l,75,concentration))
writer.writerow(("equal_volume_basal_mix",D("24.375"),75,sum(values)/2))
