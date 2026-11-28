"""Replay chiral exposure scales and reported synaptic or structural contrasts."""

import csv
from pathlib import Path


with Path(__file__).with_name("window_inputs.tsv").open(newline="") as handle:
    inputs = {row["id"]: float(row["value"]) for row in csv.DictReader(handle, delimiter="\t")}

mw = inputs["baclofen_mw"]
csf_low = inputs["csf_r_low"] / mw
csf_high = inputs["csf_r_high"] / mw
print(f"Observed clinical R-baclofen CSF span: {csf_low:.4f}–{csf_high:.4f} uM")
for study, concentration in (
    ("Serrano-Regal 2022", inputs["serrat_2022_r"]),
    ("Serrano-Regal 2020", inputs["serrat_2020_r"]),
    ("Pascual-Guerra 2025", inputs["pascual_total"] * inputs["pascual_fraction_r"]),
):
    print(f"{study}: {concentration:g} uM nominal R component, {concentration / csf_high:.1f}x to highest R CSF sample")

print(f"Pascual-Guerra segments per MBP-positive cell ratio: "
      f"{inputs['pascual_wrap_baclofen'] / inputs['pascual_wrap_control']:.2f}x")
print(f"Caillard neonatal eIPSC depression: {100 - inputs['caillard_eipsc_neonatal']:g} percentage points "
      f"at {inputs['caillard_bath']:g} uM nominal bath")
print(f"Lei and McBain half-max excitatory to inhibitory concentration ratio: "
      f"{inputs['lei_epscs_ic50'] / inputs['lei_ipscs_ic50']:g}x")
print(f"Lei and McBain retained EPSC minus retained IPSC at {inputs['lei_bath']:g} uM: "
      f"{inputs['lei_epsc_remaining'] - inputs['lei_ipsc_remaining']:g} percentage points")
print(f"Grigoras main drug contrast partial eta squared: "
      f"{inputs['grigoras_drug_f'] / (inputs['grigoras_drug_f'] + inputs['grigoras_drug_df']):.3f}")
