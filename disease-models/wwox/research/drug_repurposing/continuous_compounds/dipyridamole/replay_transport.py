"""Replay descriptive contrasts and assay-window sensitivity for dipyridamole."""

import argparse
import csv
from math import expm1
from pathlib import Path

HERE = Path(__file__).resolve().parent
MOLAR_MASS = 504.63  # FDA NDA 20-884, Description
ENT_ASSAYS = (
    ("Ward_Fig6B_human_PK15_uridine_IC50", 5.0, 356),
    ("Kiss_Table1_mouse_oocyte_uridine_IC50", 75, 2204),
    ("Kiss_Table1_mouse_Ehrlich_uridine_Ki", 66, 371),
)


def write_table(path, fields, rows):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)


def observation_rows():
    # Values transcribed from the stated source locations. Rat rows use reported means.
    observations = (
        ("Nguyen_Fig3C", "rat caudate-putamen in vivo", "spontaneous duration", "s", "6 rats", 3.2, 3.2, "0.6921"),
        ("Nguyen_Fig3D", "rat caudate-putamen in vivo", "fitted spontaneous decay rate", "s^-1", "6 rats", 0.39, 0.31, "0.0141"),
        ("Nguyen_Fig3F", "rat caudate-putamen in vivo", "spontaneous adenosine peak", "uM", "6 rats", 0.12, 0.13, "0.4893"),
        ("Nguyen_Fig8B", "rat caudate-putamen slices", "external adenosine pulse decay rate", "s^-1", "6 slices", 0.51, 0.46, "0.5209"),
        ("Nguyen_Fig8A", "rat caudate-putamen slices; NBTI arm", "external adenosine pulse decay rate", "s^-1", "4 slices", 0.23, 0.16, "0.0002"),
        ("Park_Table1_control", "neonatal piglet frontal cortex; local perfusion", "basal dialysate adenosine", "uM", "10 piglets, paired probes", 0.20, 0.45, "<0.05"),
        ("Park_Table1_ischemia", "neonatal piglet frontal cortex; local perfusion", "dialysate adenosine during ischemia", "uM", "10 piglets, paired probes", 1.14, 1.07, "NS"),
        ("Park_Table1_P1", "neonatal piglet frontal cortex; local perfusion", "dialysate adenosine, first 5 min of reperfusion", "uM", "10 piglets, paired probes", 3.05, 3.58, "NS"),
        ("Park_Table1_P2", "neonatal piglet frontal cortex; local perfusion", "dialysate adenosine, second 5 min of reperfusion", "uM", "10 piglets, paired probes", 0.65, 2.05, "<0.05"),
        ("Park_Table1_P3", "neonatal piglet frontal cortex; local perfusion", "dialysate adenosine, third 5 min of reperfusion", "uM", "10 piglets, paired probes", 0.22, 0.76, "<0.05"),
    )
    for source, system, endpoint, unit, sample, control, drug, p in observations:
        yield source, system, endpoint, unit, sample, control, drug, p, f"{drug / control:.4f}"


def window_rows():
    # Same monotonic Hill slope in both assays, with unit maximum. Ki is a separate scale scenario.
    for source, ent1, ent2 in ENT_ASSAYS:
        for hill in (0.75, 1.0, 1.25):
            lower = ent1 * 4 ** (1 / hill)  # 80% ENT1 inhibition
            upper = ent2 / 9 ** (1 / hill)  # 10% ENT2 inhibition
            yield source, ent1, ent2, f"{ent2 / ent1:.3f}", hill, f"{lower:.3f}", f"{upper:.3f}", lower <= upper


def exposure_rows():
    # Adult Aggrenox label §12.3. Free fraction assumed, not measured in the cohort.
    for statistic, total_ug_ml in (("peak_range_low", 1.01), ("peak", 1.98), ("peak_range_high", 3.99), ("trough", 0.53)):
        total_nm = 1e6 * total_ug_ml / MOLAR_MASS
        for fraction in (0.005, 0.01, 0.03):
            free_nm = total_nm * fraction
            yield (statistic, total_ug_ml, f"{total_nm:.3f}", fraction, f"{free_nm:.3f}",
                   *(f"{reference / free_nm:.3f}" for reference in (5, 20, 32, 64, 356, 1000)))


def pulse_rows():
    # One-compartment illustrative model, dA/dt = J(t) - k*A, with J constant during the input.
    # Both dimensions are ratios or scaled by vehicle k. No fit to humans, WWOX or joined studies.
    for scaled_input_time in (0.25, 1.0, 4.0):
        vehicle_peak_per_unit_source = -expm1(-scaled_input_time)
        for decay_ratio in (1, 0.8, 0.6):
            drug_peak_per_unit_source = -expm1(-decay_ratio * scaled_input_time) / decay_ratio
            peak_gain = drug_peak_per_unit_source / vehicle_peak_per_unit_source
            for source_ratio in (1, 0.85, 0.6):
                yield (scaled_input_time, decay_ratio, source_ratio, f"{source_ratio * peak_gain:.4f}",
                       f"{1 / peak_gain:.4f}", f"{source_ratio / decay_ratio:.4f}", f"{1 / decay_ratio:.4f}")


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    write_table(out / "observations.tsv", ("locator", "system", "endpoint", "unit", "sample",
                "reference_mean", "exposed_mean", "reported_p", "ratio_of_means"), observation_rows())
    write_table(out / "assay_window.tsv", ("locator_and_assay", "ENT1_nM", "ENT2_nM", "ENT2_to_ENT1",
                "assumed_hill", "80pct_ENT1_min_nM", "10pct_ENT2_max_nM", "overlap"), window_rows())
    write_table(out / "exposure_sensitivity.tsv", ("adult_label_statistic", "total_plasma_ug_mL", "total_plasma_nM",
                "assumed_fu_plasma", "estimated_free_plasma_nM", "Kpuu_to_5nM_hENT1_assay",
                "Kpuu_to_20nM_model_window_start", "Kpuu_to_32nM_rat_uptake_assay", "Kpuu_to_64nM_rat_release_assay",
                "Kpuu_to_356nM_hENT2_assay", "Kpuu_to_1000nM_juvenile_slice_range_start"), exposure_rows())
    write_table(out / "pulse_identifiability.tsv", ("input_T_times_vehicle_k", "drug_to_vehicle_k", "drug_to_vehicle_J",
                "evoked_peak_ratio", "J_ratio_to_keep_same_peak", "evoked_full_AUC_ratio", "matched_external_pulse_half_life_ratio"), pulse_rows())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=HERE)
    main(parser.parse_args().out)
