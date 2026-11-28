"""Replay labeled allopregnanolone mass scenarios for one hippocampal specimen."""

import csv
from pathlib import Path
from math import exp

HERE = Path(__file__).resolve().parent

# The rat tissue means and anatomical mouse volumes are independent references.
BASELINES = {"Kudova_P12": 0.254, "Kudova_P25": 0.119}  # ng/g, intact groups, Table 1
P17_MRI_VOLUME = 22.0 / (1 + exp(-(18.5 + 17 - 24.7) / 3.7))  # Chuang Table 2, mm³
# Density of 1 mg/mm³ used for volume proxies, before dissection and slice losses.
MASS_SCENARIOS = {
    "histology_P14_equal_split": 13.3 / 2,
    "P17_MRI_equal_split": P17_MRI_VOLUME / 2,
    "histology_P14_full_region": 13.3,
    "P17_MRI_full_region": P17_MRI_VOLUME,
}
LABEL_FRACTION = 0.25  # Planning scenario only.
ON_COLUMN_LLOQ_PG = 0.050  # Jin, human plasma.
INJECTED_FRACTION = 10 / 200  # Jin, final extract aliquot; assume full upstream recovery.
HIGASHI_INPUT_LOQ_PG = 0.25 * 20  # ng/g x mg, adult rat brain.


def rows():
    for reference, baseline in BASELINES.items():
        for allocation, wet_mg in MASS_SCENARIOS.items():
            for product_ratio in (1.0, 0.5):
                labeled_ng_g = baseline * LABEL_FRACTION * product_ratio
                pre_recovery_pg = labeled_ng_g * wet_mg
                on_column_fg = 1000 * pre_recovery_pg * INJECTED_FRACTION
                return_to_input = ON_COLUMN_LLOQ_PG / INJECTED_FRACTION
                yield (reference, allocation, f"{wet_mg:.3f}", LABEL_FRACTION, product_ratio,
                       f"{labeled_ng_g:.6f}", f"{pre_recovery_pg:.4f}", f"{on_column_fg:.2f}",
                       f"{ON_COLUMN_LLOQ_PG / pre_recovery_pg:.4f}",
                       f"{return_to_input / labeled_ng_g:.2f}",
                       f"{HIGASHI_INPUT_LOQ_PG / labeled_ng_g:.2f}")


if __name__ == "__main__":
    with (HERE / "assay_budget.tsv").open("w", encoding="utf-8", newline="") as stream:
        table = csv.writer(stream, delimiter="\t", lineterminator="\n")
        table.writerow([
            "baseline_reference", "anatomical_scenario", "wet_mass_proxy_mg",
            "reference_label_fraction", "product_ratio_to_reference",
            "labeled_product_ng_g", "labeled_product_in_input_pg",
            "jin_best_case_on_column_fg", "net_fraction_needed_for_jin_on_column_lloq",
            "mass_mg_for_jin_threshold_in_ideal_transfer",
            "mass_mg_for_higashi_equivalent_input_threshold",
        ])
        table.writerows(rows())
