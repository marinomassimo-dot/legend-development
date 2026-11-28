"""Replay scale comparisons and the recombinant redox sensitivity calculation."""

import csv
from math import sqrt
from pathlib import Path


with Path(__file__).with_name("exposure_inputs.tsv").open(newline="") as stream:
    inputs = {row["id"]: float(row["value"]) for row in csv.DictReader(stream, delimiter="\t")}

parent_mw = inputs["parent_mw"]
adult_plasma_uM = inputs["adult_parent"] / parent_mw
print(f"Adult plasma parent, total protein-bound plus unbound: {adult_plasma_uM * 1000:.2f} nM")
for binding_id in ("parent_bound_dialysis", "parent_bound_filter_low", "parent_bound_filter_high"):
    unbound_fraction = 1 - inputs[binding_id] / 100
    print(f"  Illustrative unbound plasma at {inputs[binding_id]:g}% binding: "
          f"{adult_plasma_uM * unbound_fraction * 1000:.2f} nM")

print("Oral EAE mouse and IV rat CSF, comparison to nominal neuronal bath")
for exposure_id in ("eae_csf_1", "eae_csf_2", "eae_csf_3", "rat_iv_csf"):
    csf_uM = inputs[exposure_id] / parent_mw
    print(f"  {exposure_id}: {csf_uM * 1000:.2f} nM and "
          f"{inputs['rat_neural_reserve'] / csf_uM:.0f}x to acute neuronal bath")

print("Conditional FRDA plasma arithmetic. Method and sampling-time alignment unknown.")
for free_key in ("frda_ide_reported_free_low", "frda_ide_reported_free_high"):
    free_mass = inputs["frda_child_total_peak"] * inputs[free_key] / 100
    print(f"  Reported-free parent scenario: {free_mass:.2f} ng/mL, "
          f"{free_mass / parent_mw * 1000:.1f} nM")
qs10_free_mass = inputs["frda_child_total_peak"] * inputs["frda_qs10_reported_free"] / 100
print(f"  Reported-free QS10 scenario: {qs10_free_mass:.2f} ng/mL, "
      f"{qs10_free_mass / inputs['qs10_mw']:.3f} uM")

qs10_pool = inputs["adult_qs10_pool"]
qs10_extreme_uM = qs10_pool * (1 - inputs["qs10_bound_dialysis"] / 100)
print(f"Unconjugated-only extreme for adult unbound plasma QS10: {qs10_extreme_uM:.3f} uM, "
      f"{inputs['qs10_embryo_bath'] / qs10_extreme_uM:.1f}x below embryo bath and "
      f"{inputs['qs10_pre_reduced_bath'] / qs10_extreme_uM:.0f}x below the pre-reduced cell bath")

for name in ("parent", "qs10"):
    print(f"Recombinant NADPH-supported dilute-substrate slope ({name}): "
          f"{inputs[f'{name}_vmax'] / inputs[f'{name}_km']:.3f} umol/mg/min/uM")
for substrate_uM in (0.01, 0.1, inputs["rat_neural_reserve"]):
    percent_vmax = 100 * substrate_uM / (inputs["parent_km"] + substrate_uM)
    print(f"  Idebenone at {substrate_uM:g} uM in the enzyme-only model: {percent_vmax:.3f}% of Vmax")

rgc5_pct_points = inputs["rgc5_delayed_rescue"] * inputs["rgc5_rotenone_loss"] / 100
print(f"RGC-5 {inputs['rgc5_delayed']:g} nM delayed comparison: "
      f"~{rgc5_pct_points:.1f} percentage points on the unchallenged vehicle ATP scale")

for arm in ("lower", "higher"):
    change = inputs[f"melas_{arm}_mean"] - inputs["melas_control_mean"]
    se = sqrt((inputs[f"melas_{arm}_sd"] ** 2 + inputs["melas_control_sd"] ** 2)
              / inputs["melas_arm_n"])
    print(f"MELAS MRS lactate change, {arm} arm minus placebo: "
          f"{change:+.2f} IU, unadjusted independent-group SE {se:.2f} IU")
