"""Reconstruct carisbamate exposure scales, registry scope and kinetic controls."""

import argparse
import csv
import hashlib
import json
from math import exp, expm1, sqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
MOLAR_MASS = 215.63  # PubChem CID 6918474, g/mol
TRIALS = {
    "NCT00740623": "b39b868fbabe63a18f7a875b31fb115c9cd087c7b0248745df17366b293c9210",
    "NCT03731715": "ee086583caf0f9769d1c7dca64f9b899dcf11cb77e7332979ea810e6a6460de2",
    "NCT04062981": "4eaaaa0800e4e0e1aa6b7e5e320d4392fb839205d67e6a246c63fe3b95306892",
    "NCT05219617": "6497bcb38f3e8283a13b21fb2f2f0fdc35801fc49b6cf27cc847551be138535e",
}
ASSAYS = (
    ("Liu_abstract_rat_hippocampal_Na_peak_IC50_minus67mV", 89),
    ("Liu_abstract_rat_Nav1_2_peak_IC50_minus67mV", 68),
    ("Liu_abstract_rat_repetitive_firing_46pct_reduction", 30),
    ("Lee_abstract_rat_DG_evoked_glutamate_lowest_nominal_bath", 30),
    ("Kim_Fig6B_recombinant_Cav3_1_16.8pct_reduction", 100),
    ("Kim_Fig6D_recombinant_Cav3_1_inactivation_shift", 300),
    ("Hung_Fig1B_rat_GH3_late_sodium_IC50", 11.4),
    ("Hung_Fig1B_rat_GH3_transient_sodium_IC50", 56.4),
    ("Hung_Fig6B_rat_GH3_Ih_IC50", 38),
)


def tsv(path, header, rows):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def registry_rows(files):
    for nct, expected_hash in TRIALS.items():
        raw = (files / f"{nct}.json").read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected_hash:
            raise ValueError(f"Frozen public trial data differ for {nct}")
        trial = json.loads(raw)
        data = trial["protocolSection"]
        status = data["statusModule"]
        age = data["eligibilityModule"]
        design = data["designModule"]
        endpoints = data["outcomesModule"]["primaryOutcomes"]
        yield (nct, status["lastUpdatePostDateStruct"]["date"], status["overallStatus"], age["minimumAge"],
               age.get("maximumAge", "NA"), design["designInfo"]["allocation"], design["enrollmentInfo"]["count"],
               design["enrollmentInfo"]["type"], " | ".join(item["measure"] for item in endpoints), trial["hasResults"])


def exposure_rows():
    # Adult means. The refractory-focal 0–2 h strata are cross-sectional counts, not individual Cmax.
    references = (
        ("Sperling_Table2B_study1_0to2h_400mg_no_inducer", "0–2 h sample-bin mean", 6.74),
        ("Sperling_Table2B_study1_0to2h_400mg_inducer", "0–2 h sample-bin mean", 4.53),
        ("Chien_Table4_250mg_q12h_healthy_adults_monotherapy", "steady-state Cmax mean", 8.13),
        ("Chien_Table4_500mg_q12h_healthy_adults_monotherapy_LTG_study", "steady-state Cmax mean", 15.8),
        ("Chien_Table4_500mg_q12h_healthy_adults_monotherapy_VPA_study", "steady-state Cmax mean", 17.1),
    )
    for source, statistic, mg_l in references:
        total = 1000 * mg_l / MOLAR_MASS
        for fraction in (0.4, 0.56, 0.7):
            free = total * fraction
            for endpoint, bath in ASSAYS:
                yield source, statistic, mg_l, f"{total:.3f}", fraction, f"{free:.3f}", endpoint, bath, f"{bath/free:.3f}"


def required_plasma_rows():
    # No child-level total concentrations or measured unbound partition are supplied to this calculation.
    for endpoint, bath in ASSAYS:
        for ratio in (0.3, 1.0, 3.0):
            total_mg_l = bath * MOLAR_MASS / (1000 * 0.56 * ratio)
            yield endpoint, bath, 0.56, ratio, f"{total_mg_l:.3f}"


def train_rows():
    # Whalley et al., Fig. 4 and adjoining Results, in vitro rat piriform spikes at nominal high baths.
    fits = (
        (25, 399, 0.42, 59, 0.53),
        (50, 145, 0.23, 32, 0.44),
        (100, 55, 0.21, 9, 0.45),
    )
    for hz, caris_tau, caris_plateau, lid_tau, lid_plateau in fits:
        last_ms = 14000 / hz
        for pulse in (2, 5, 8, 15):
            time_ms = 1000 * (pulse - 1) / hz
            caris_rel = expm1(-time_ms / caris_tau) / expm1(-last_ms / caris_tau)
            lid_rel = expm1(-time_ms / lid_tau) / expm1(-last_ms / lid_tau)
            yield (hz, pulse, f"{time_ms:.1f}", caris_tau, lid_tau, caris_plateau, lid_plateau,
                   f"{caris_rel:.4f}", f"{lid_rel:.4f}", f"{1 - 0.4*caris_rel:.4f}", f"{1 - 0.4*lid_rel:.4f}")


def ca_rows():
    # Fig. 6A/D from Kim et al. fit illustrative slopes and normalize each curve to -110 mV.
    # Effects at 300 uM use 0.712 times the shifted relative availability. This is a sensitivity analysis.
    def available(voltage, midpoint, slope):
        return 1 / (1 + exp((voltage - midpoint) / slope))

    for slope in (4, 6, 8):
        for voltage in (-110, -90, -80, -75, -70, -65):
            before = available(voltage, -62.6, slope) / available(-110, -62.6, slope)
            after = 0.712 * available(voltage, -68.9, slope) / available(-110, -68.9, slope)
            yield slope, voltage, f"{before:.4f}", f"{after:.4f}", f"{after/before:.4f}"


def focal_rows():
    # EU CTR EudraCT 2008-007687-41. Marginal proportions with descriptive Wilson intervals.
    for group, n, response, median in (("placebo", 183, 48, 20.59), ("800_mg_day", 176, 49, 29.93),
                                       ("1200_mg_day", 181, 66, 36.3)):
        p = response / n
        z = 1.96
        denom = 1 + z * z / n
        center = (p + z * z / (2 * n)) / denom
        margin = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
        yield group, n, response, f"{100*p:.3f}", f"{100*(center-margin):.3f}", f"{100*(center+margin):.3f}", median


def main(files, out):
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "clinical_registry.tsv", ("NCT", "last_update", "status", "eligible_min_age", "eligible_max_age", "allocation",
        "enrollment", "enrollment_type", "primary_outcome_measures", "has_posted_us_results"), registry_rows(files))
    tsv(out / "exposure_sensitivity.tsv", ("adult_source", "statistic", "total_mg_L", "total_uM", "assumed_fu_plasma",
        "estimated_free_plasma_uM", "assay_endpoint", "nominal_assay_uM", "required_Kpuu_to_equal_nominal"), exposure_rows())
    tsv(out / "required_plasma.tsv", ("assay_endpoint", "nominal_assay_uM", "assumed_fu_plasma", "assumed_Kpuu",
        "required_total_plasma_mg_L"), required_plasma_rows())
    tsv(out / "pulse_train.tsv", ("frequency_Hz", "pulse", "time_ms", "carisbamate_tau_ms", "lidocaine_tau_ms",
        "carisbamate_published_plateau", "lidocaine_published_plateau", "carisbamate_fraction_of_own_pulse15_block",
        "lidocaine_fraction_of_own_pulse15_block", "carisbamate_amplitude_at_matched_40pct_final_block",
        "lidocaine_amplitude_at_matched_40pct_final_block"), train_rows())
    tsv(out / "cav3_voltage.tsv", ("assumed_slope_mV", "conditioning_voltage_mV", "vehicle_fraction_of_own_minus110mV",
        "exposed_fraction_of_vehicle_minus110mV", "exposed_to_vehicle_same_voltage"), ca_rows())
    tsv(out / "adult_focal_response.tsv", ("group", "n_analysed", "n_with_50pct_or_greater_reduction", "response_pct",
        "Wilson_lower_pct", "Wilson_upper_pct", "median_frequency_reduction_pct"), focal_rows())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trial_snapshot_dir", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    main(args.trial_snapshot_dir, args.out)
