"""Compare concentrations on a molar scale without transferring between compartments."""

import csv
from decimal import Decimal
from pathlib import Path


with Path(__file__).with_name("exposure_inputs.tsv").open(encoding="utf-8") as source:
    values = {row["key"]: Decimal(row["value"]) for row in csv.DictReader(source, delimiter="\t")}

csf_mass = values["csf_mean"]
csf_nm = 1000 * csf_mass / values["parent_mass"]

print("contrast\tvalue\tunit")
print(f"CSF reported mean, parent basis\t{csf_nm:.4f}\tnM")
print(f"CSF mean / lowest positive mouse enzyme concentration\t{csf_nm / values['mouse_pgk1_low_nominal']:.3f}\tratio")
print(f"human apo PGK1 estimated Kd / CSF mean\t{1000 * values['human_pgk1_apo_kd'] / csf_nm:.1f}\tratio")
print(f"nominal neuronal bath / CSF mean\t{1000 * values['neuronal_bath'] / csf_nm:.1f}\tratio")
print(f"lowest stated plasma calibrator / CSF mean on mass scale\t{values['lowest_described_plasma_calibrator'] / csf_mass:.3f}\tratio")

free_to_csf = values["assumed_free_fraction"] * values["csf_over_estimated_free_plasma"]
print(f"illustrative CSF scale with published plasma unit\t{1000 * values['published_plasma_mean'] * free_to_csf:.5f}\tng/mL")
print(f"illustrative CSF scale with preprint plasma unit as printed\t{values['preprint_plasma_as_printed'] * free_to_csf:.5f}\tng/mL")
