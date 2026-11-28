"""Replay reported sodium selenate exposures and three cross-checks."""

import argparse
import csv
from hashlib import sha256
from math import comb
from pathlib import Path
import re
import xml.etree.ElementTree as ET

SELENIUM_MASS = 78.971  # g/mol
SELENATE_SALT_MASS = 188.95  # anhydrous disodium salt, PubChem CID 25960
RAT_PK_SHA = "ffaf731c5c46186a60a8e1a1a4beb180f277abc3abd6d6becba14de786e39724"


def human_exposure():
    """Cardoso Table 2: displayed means can use different counts at each visit."""
    rows = (
        ("placebo", "serum", 135.8, 9, 143.8, 8, 8, -51.6, 51.3),
        ("nutritional", "serum", 122.2, 8, 176.7, 8, 8, 20.3, 88.7),
        ("supranutritional", "serum", 145.4, 19, 858.3, 19, 19, 497.4, 928.3),
        ("placebo", "CSF", 1.3, 9, 1.4, 7, 7, -0.4, 0.7),
        ("nutritional", "CSF", 1.6, 6, 2.5, 7, 6, 0.2, 1.6),
        ("supranutritional", "CSF", 1.4, 17, 20.2, 14, 13, 13.4, 24.8),
    )
    for arm, matrix, pre, n_pre, post, n_post, n_paired, low, high in rows:
        yield arm, matrix, pre, n_pre, post, n_post, n_paired, pre / SELENIUM_MASS, post / SELENIUM_MASS, low / SELENIUM_MASS, high / SELENIUM_MASS


def csf_assay():
    # Areas are not mass concentrations and are never used to scale total Se.
    for peak, label, pre, post in (
        (1, "likely_albumin_associated", 4.4, 137.4),
        (2, "likely_SELENO_P_associated", None, 123.3),
        (3, "tentative_selenate", 1347, 1748),
        (4, "suspected_selenite", 351.7, 1551),
    ):
        yield peak, label, pre if pre is not None else "<LOD", post, 11, post - pre if pre is not None else "NA", post / pre if pre is not None else "NA"


def csf_parent_ceiling():
    observed_total = 20.2 / SELENIUM_MASS
    for target in (1, 3, 5, 10):
        yield observed_total, target, target * SELENIUM_MASS, target / observed_total


def read_rat_pk(path):
    contents = path.read_bytes()
    if sha256(contents).hexdigest() != RAT_PK_SHA:
        raise ValueError(f"Unexpected source fingerprint: {path}")
    return ET.fromstring(contents)


def pk_row(study, table, prefix):
    element = study.find(f".//table-wrap[@id='prp21256-tbl-{table:04d}']")
    for row in element.findall(".//tbody/tr"):
        fields = [" ".join("".join(node.itertext()).split()) for node in row]
        if fields[0].startswith(prefix):
            return tuple(float(re.match(r"[0-9.]+", cell).group()) for cell in fields[1:])
    raise ValueError(f"Table {table} does not contain {prefix}")


def rat_auc_consistency(study):
    for analyte, plasma_table, brain_table in (("selenate", 1, 3), ("total_selenium", 2, 4)):
        plasma = pk_row(study, plasma_table, "AUC")
        brain = pk_row(study, brain_table, "AUCbrain (")
        printed = pk_row(study, brain_table, "AUCbrain/AUCplasma")
        for index, route_dose in enumerate(("SC_0.04_mg_kg", "SC_0.2_mg_kg", "IP_1_mg_kg")):
            for side, side_idx in (("left", 0), ("right", 1)):
                offset = index * 2 + side_idx
                yield analyte, route_dose, side, plasma[index], brain[offset], printed[offset], brain[offset] / plasma[index]


def rat_mass_balance(study):
    # At complete systemic delivery with no loss, dose/Cmax is the largest possible plasma volume.
    for dose, route, peak in zip((0.04, 0.2, 1), ("SC", "SC", "IP"), pk_row(study, 1, "C max")):
        for plasma_mL_kg in (20, 30, 40):
            yield route, dose, peak, 1000 * dose / peak, plasma_mL_kg, peak * plasma_mL_kg / (1000 * dose)


def rat_steady_state():
    parent_salt_ng_mL, total_se_ng_mL = 50_000, 350  # Results, Fig. 5 narrative, approximate.
    parent_se_ng_mL = parent_salt_ng_mL * SELENIUM_MASS / SELENATE_SALT_MASS
    yield parent_salt_ng_mL, total_se_ng_mL, parent_se_ng_mL, parent_se_ng_mL / total_se_ng_mL


def fisher_two_sided(active_events, active_n, control_events, control_n):
    successes = active_events + control_events
    denominator = comb(active_n + control_n, successes)
    observed_weight = comb(active_n, active_events) * comb(control_n, control_events)
    lower = max(0, successes - control_n)
    upper = min(active_n, successes)
    weights = [comb(active_n, a) * comb(control_n, successes - a) for a in range(lower, upper + 1)]
    return sum(weight for weight in weights if weight <= observed_weight) / denominator


def rat_vEEG():
    for label, zero, available in (
        ("vehicle_analyzed", 0, 10),
        ("vehicle_two_missing_both_seizures", 0, 12),
        ("vehicle_two_missing_one_seizure_free", 1, 12),
        ("vehicle_two_missing_both_seizure_free", 2, 12),
    ):
        yield label, 4, 12, zero, available, 4 / 12 - zero / available, fisher_two_sided(4, 12, zero, available)
    yield "levetiracetam_analyzed", 4, 12, 0, 12, 4 / 12, fisher_two_sided(4, 12, 0, 12)


def cell_tau():
    # Mean bar top pixels in Fig. 4 rendered at width 1050 px. Output is approximate.
    for panel, mark, zero_y, five_y, bars in (
        ("4B", "pS202_label", 354, 106, ((0, 304), (1, 264), (3, 228), (5, 251), (10, 213))),
        ("4C", "pS396", 965, 717, ((0, 916), (1, 826), (3, 831), (5, 831), (10, 749))),
    ):
        for nominal, mean_y in bars:
            yield panel, mark, nominal, mean_y, zero_y, five_y, 5 * (zero_y - mean_y) / (zero_y - five_y)


def write_table(path, header, rows):
    with path.open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header.split())
        for row in rows:
            writer.writerow(f"{x:.5g}" if isinstance(x, float) else x for x in row)


def main(inputs, out):
    rat = read_rat_pk(inputs / "PMC11540874.xml")
    out.mkdir(parents=True, exist_ok=True)
    write_table(out / "human_elemental_exposure.tsv",
                "arm matrix baseline_ug_Se_L n_baseline week24_ug_Se_L n_week24 n_paired baseline_uM_Se week24_uM_Se paired_delta_95CI_lo_uM_Se paired_delta_95CI_hi_uM_Se",
                human_exposure())
    write_table(out / "human_csf_peaks.tsv", "peak provisional_identity baseline_area week24_area n delta_area fold_area", csf_assay())
    write_table(out / "human_csf_parent_ceiling.tsv", "week24_mean_total_uM_Se nominal_cell_selenate_uM minimum_parent_ug_Se_L fold_above_maximum_mean_parent", csf_parent_ceiling())
    write_table(out / "rat_auc_consistency.tsv", "analyte group cortex_side printed_plasma_AUC printed_brain_AUC printed_ratio recomputed_ratio", rat_auc_consistency(rat))
    write_table(out / "rat_parent_mass_balance.tsv", "route single_dose_mg_salt_kg printed_Cmax_ug_salt_mL maximum_plasma_mL_kg scenario_plasma_mL_kg implied_fraction_of_administered_dose", rat_mass_balance(rat))
    write_table(out / "rat_steady_state_consistency.tsv", "reported_salt_ng_mL reported_total_Se_ng_mL Se_implied_by_parent_ng_mL parent_Se_over_total_Se", rat_steady_state())
    write_table(out / "rat_vEEG_sensitivity.tsv", "contrast active_zero_count active_n control_zero_count control_n risk_difference fisher_two_sided_unadjusted", rat_vEEG())
    write_table(out / "cell_tau_digitization.tsv", "panel marker nominal_selenate_uM y_bar_px y_0_px y_5_px approximate_phospho_over_total_normalized", cell_tau())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    main(args.inputs, args.out)
