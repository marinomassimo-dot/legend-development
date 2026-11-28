"""Replay azetukalner exposure bounds, Kv7 scenarios and adult trial endpoints."""

import argparse
import json
from math import exp
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "sodium_benzoate"))
sys.path.insert(0, str(COMPOUNDS / "jbpos0101"))
from coagonist_screen import bulk_panel, tsv
from replay_exposure_and_receptors import verified, verified_expression

MOLECULAR_WEIGHT = 368.5
PANEL = ("Kcnq2", "Kcnq3", "Kcnq5", "Cdipt", "Pip5k1c", "Pip4k2a", "Plcb1", "Isyna1", "Impa1")
HASHES = {
    "NCT03796962.json": "1ce5969a4221f1482a07fedf1a352eb9dd2a144a878abc5325c3fa48288d0cf6",
    "NCT05614063.json": "09ee382987b6514b963d98589094611e709832ea482d88610a5570c208233b33",
    "NCT05667142.json": "cb06848bd3d661e858e6f65557a2935810bb414824bf725e874343fca10f0d0e",
}
PK = (
    ("2h", 15.7, 21.5), ("4h_results", 30.2, 21.9), ("4h_caption", 30.2, 21.1),
    ("6h_results", 42.1, 19.1), ("6h_caption", 44.4, 20.2), ("mean_individual_peak", 59.2, 13.8),
    ("max_placebo_carryover", 8.2, None),
)
MIDPOINTS = (("AES_HEK", 42), ("Lu_HEK", 660))
VHALF_CONTROL, VHALF_LU_TOP = -22.83, -67.61
CIF_HASH = "fd5e2af79b005b55d80e97baa652e952842bb75f8218cca56190f4e4ea1bb3c7"
ASSUMED_REVERSAL = -85
# Breton Table 1 group means in MOhm. Reciprocal of the mean is a descriptive approximation.
CONDUCTANCE_GAP = 1000 / 102.88 - 1000 / 143.03


def exposure_rows():
    for time, ng_ml, sd in PK:
        total = ng_ml * 1000 / MOLECULAR_WEIGHT
        for assay, midpoint in MIDPOINTS:
            yield time, ng_ml, sd, total, assay, midpoint, midpoint / total


def active_fraction(voltage, midpoint, slope):
    return 1 / (1 + exp((midpoint - voltage) / slope))


def conductance_rows():
    # Common maximum shift isolates midpoint sensitivity. The both-assay amplitude and slopes
    # below are assumptions, not fits to native juvenile neurons.
    for time, ng_ml, _ in PK[3:5]:
        total = ng_ml * 1000 / MOLECULAR_WEIGHT
        for assay, midpoint in MIDPOINTS:
            for ratio in (0.01, 0.1, 0.3, 1):
                local = total * ratio
                shift = (VHALF_LU_TOP - VHALF_CONTROL) * local / (midpoint + local)
                for slope in (8, 12, 16):
                    for voltage in (-73.62, -60, -50, -40):
                        f0 = active_fraction(voltage, VHALF_CONTROL, slope)
                        f1 = active_fraction(voltage, VHALF_CONTROL + shift, slope)
                        increment = f1 - f0
                        # Differentiate I=Gmax*f(V)*(V-EK) at equilibrium.
                        df = (f1 * (1 - f1) - f0 * (1 - f0)) / slope
                        slope_increment = increment + (voltage - ASSUMED_REVERSAL) * df
                        reference_gmax = CONDUCTANCE_GAP / slope_increment if voltage == -73.62 else None
                        yield (time, assay, ratio, local, shift, slope, voltage, f0, f1,
                               increment, slope_increment, reference_gmax)


def measurement_map(outcome):
    category, = outcome["classes"][0]["categories"]
    return {row["groupId"]: row for row in category["measurements"]}


def phase_two(registry):
    measures = registry["resultsSection"]["outcomeMeasuresModule"]["outcomeMeasures"]
    primary, response = measures[:2]
    assert primary["title"] == "Median Percent Change in Focal Seizure Frequency"
    assert response["title"] == "50% XEN1101 Response Rate"
    sizes = {r["groupId"]: int(r["value"]) for r in primary["denoms"][0]["counts"]}
    median = measurement_map(primary)
    responders = measurement_map(response)
    safety_by_arm = {25: (114, 18, 36, 17), 20: (51, 7, 13, 11), 10: (46, 1, 3, 5), 0: (114, 4, 8, 8)}
    for arm in primary["groups"]:
        title = arm["title"]
        mg = 0 if title == "Placebo" else int(title.split()[0])
        group_id = arm["id"]
        yield (mg, sizes[group_id], float(median[group_id]["value"]), int(responders[group_id]["value"]),
               *safety_by_arm[mg])


def trial_rows(phase2):
    phase3 = ((0, 125, -10.43, 26, 125, 4, 4, 9), (15, 125, -34.45, 47, 125, 6, 12, 10),
              (25, 124, -53.15, 68, 124, 18, 39, 12))
    for trial, arms in (("X_TOLE_8_week", list(phase_two(phase2))), ("X_TOLE2_12_week", phase3)):
        control, = [row for row in arms if row[0] == 0]
        _, ref_n, ref_change, ref_respond, ref_safety, ref_stop, ref_dizzy, ref_sleep = control
        for mg, efficacy_n, med, respond, safety_n, stop, dizzy, sleep in arms:
            response_rate = respond / efficacy_n
            stop_rate = stop / safety_n
            yield (trial, mg, efficacy_n, med, med - ref_change, respond, response_rate,
                   response_rate - ref_respond / ref_n, safety_n, stop, stop_rate,
                   stop_rate - ref_stop / ref_safety, dizzy, (dizzy / safety_n) - (ref_dizzy / ref_safety),
                   sleep, (sleep / safety_n) - (ref_sleep / ref_safety))


def registry_rows(registries):
    for name, data in registries.items():
        p = data["protocolSection"]
        status = p["statusModule"]
        yield (name.removesuffix(".json"), p["eligibilityModule"]["minimumAge"],
               status["overallStatus"], data["hasResults"], status["lastUpdatePostDateStruct"]["date"])


def ligand_rows(cif):
    scheme = cif.split("_pdbx_nonpoly_scheme.pdb_ins_code", 1)[1].split("#", 1)[0]
    for row in scheme.splitlines():
        fields = row.split()
        if fields:
            asym, _, component, _, pdb_sequence, author_sequence, _, _, chain, _ = fields
            yield "22BI", asym, component, pdb_sequence, author_sequence, chain


def main(files, out):
    evidence = files / "deepening_downloads/azetukalner_20261127"
    registries = {name: json.loads(verified(evidence / name, digest)) for name, digest in HASHES.items()}
    out.mkdir(parents=True, exist_ok=True)
    ligands = list(ligand_rows(verified(evidence / "22BI.cif", CIF_HASH).decode()))
    assert sum(row[2] == "A1EY8" for row in ligands) == 4
    tables = (
        ("structure_components.tsv", "pdb label_asym component pdb_position author_position author_chain", ligands),
        ("plasma_to_nominal_midpoints.tsv", "time plasma_mean_ng_mL plasma_sd_ng_mL total_nM assay nominal_midpoint_nM unbound_brain_to_total_plasma_ratio_to_midpoint", exposure_rows()),
        ("kv7_voltage_scenarios.tsv", "time assay assumed_local_free_to_total_plasma local_free_nM delta_vhalf_mV slope_mV voltage_mV fraction_control fraction_active delta_fraction_of_Gmax delta_slope_conductance_per_Gmax_EK_minus85 Gmax_for_2p73_nS_at_KO_rest", conductance_rows()),
        ("adult_trials.tsv", "trial research_arm_mg efficacy_n median_individual_change_pct difference_of_arm_medians_pp responders_50pct response_rate response_risk_diff safety_n TEAE_permanent_stop stop_rate stop_risk_diff dizziness_n dizziness_risk_diff somnolence_n somnolence_risk_diff", trial_rows(registries["NCT03796962.json"])),
        ("trial_registry.tsv", "registry minimum_age overall_status has_posted_results last_update_posted", registry_rows(registries)),
    )
    for name, header, rows in tables:
        tsv(out / name, header.split(), ([f"{v:.6g}" if isinstance(v, float) else "NA" if v is None else v for v in row] for row in rows))
    verified_expression(files)
    tsv(out / "wwox_channel_and_pip2.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(files, PANEL))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    main(args.files, args.out)
