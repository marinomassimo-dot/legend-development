"""Replay reported sodium-channel curves, aggregate outcomes and conditional exposure."""

import argparse
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
COMPOUNDS = HERE.parent
sys.path[:0] = [str(COMPOUNDS / "sodium_benzoate"), str(COMPOUNDS / "jbpos0101")]
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_exposure_and_receptors import verified_expression

# Kahlig et al. (2022), Table 1. Each group is IC50 nM, Hill slope, maximum block.
ASSAYS = ("persistent", "peak_tonic", "peak_10Hz", "peak_voltage_dependent")
CURVES = {
    "relutrigine": ((141, 1.2, 1), (8472, 1, 1), (271, 1.3, .75), (317, 1, 1)),
    "carbamazepine": ((77490, 1.1, 1), (2307000, 1, 1), (1418000, .9, 1), (44370, .9, 1)),
    "lamotrigine": ((78480, 1, 1), (1249000, .8, 1), (515800, 1, 1), (39090, .9, 1)),
    "cenobamate": ((71690, 1.1, 1), (1719000, 1.1, 1), (749300, .7, 1), (66710, .9, 1)),
    "phenytoin": ((59820, .8, 1), None, (876600, .6, 1), (47780, 1, 1)),
    "lacosamide": ((832700, .9, 1), None, (682200, 1.3, 1), (269300, 1.2, 1)),
}
BULK_PANEL = ("Scn1a", "Scn2a", "Scn3a", "Scn8a", "Scn1b", "Scn2b", "Scn3b", "Scn4b",
              "Fgf13", "Fgf14", "Ank3")
NUCLEI_PANEL = tuple(gene for gene in BULK_PANEL if gene not in {"Scn2b", "Scn3b"})
TRIAL_SNAPSHOTS = {
    "NCT05818553": "6e10c26c227160abdd738741392a118df2d1e7d66563cfa59560d2c93d1448af",
    "NCT07010471": "96e93f6850af97cd374700a2d1b97fbcb7db3b577cd4a484189c39ba2e2275fd",
}
MOLAR_MASS = 407.27
UNBOUND_PLASMA = .05
# Phase 1 poster Fig. 3, 90-mg historical cohort, day 14 +24 h.
# Broad graphical read-off of the plotted mean, not a confidence interval.
PLASMA_READ_OFF = (700, 850)


def block_at(concentration, curve):
    midpoint, slope, maximum = curve
    return maximum / (1 + (midpoint / concentration) ** slope)


def concentration_for(effect, curve):
    midpoint, slope, maximum = curve
    return midpoint * (effect / (maximum - effect)) ** (1 / slope)


def fit_rows():
    for drug, curves in CURVES.items():
        for assay, curve in zip(ASSAYS, curves, strict=True):
            if curve is None:
                yield drug, assay, "NA", "NA", "NA", "NA"
                continue
            midpoint, slope, maximum = curve
            yield drug, assay, midpoint, slope, maximum, f"{midpoint / curves[0][0]:.5f}"


def scenario_rows():
    matches = (("peak_voltage_dependent", (.05, .1, .2, .3, .5)),
               ("persistent", (.25, .5)))
    for drug, curves in CURVES.items():
        for assay, targets in matches:
            for target in targets:
                concentration = concentration_for(target, curves[ASSAYS.index(assay)])
                effects = [f"{block_at(concentration, curve):.5f}" if curve else "" for curve in curves]
                yield drug, assay, target, f"{concentration:.5f}", *effects


def exposure_rows():
    for partition in (.1, .25, .5, 1, 2):
        for endpoint, target in (("mutant_N1768D_persistent", 75), ("WT_NaV1_6_persistent", 141),
                                 ("WT_NaV1_6_peak_10Hz_fit_midpoint", 271),
                                 ("WT_NaV1_6_peak_voltage_dependent", 317)):
            plasma = target * MOLAR_MASS / (1000 * UNBOUND_PLASMA * partition)
            brain = [level * 1000 / MOLAR_MASS * UNBOUND_PLASMA * partition for level in PLASMA_READ_OFF]
            yield endpoint, target, UNBOUND_PLASMA, partition, f"{plasma:.2f}", *(f"{level:.2f}" for level in brain)


def clinical_rows():
    # EMBOLD Cohort 2. SEC slides 60–64, and EILAT XVIII §11.6.
    active_arm, delayed_arm = 28, 25
    active_records, placebo_records = 51, 25
    active_rate, placebo_rate = 196.6, 418.4
    active_days, placebo_days = 17.34, 10.43
    return (
        ("randomized", active_arm + delayed_arm, "participants", "28 immediate plus 25 delayed"),
        ("analyzed_both_exposures_implied", active_records + placebo_records - active_arm - delayed_arm,
         "participants", "union 53 reported by sponsor; 51 active plus 25 placebo minus 53"),
        ("placebo_adjusted_motor_seizure_reduction", f"{100 * (1 - active_rate / placebo_rate):.3f}",
         "percent", "arithmetic from published NB1 fitted margins; not a refit"),
        ("reduction_CI_lower_reported_transform", 30, "percent", "1 minus upper reported IRR 0.70"),
        ("reduction_CI_upper_reported_transform", 68, "percent", "1 minus lower reported IRR 0.32"),
        ("additional_motor_seizure_free_days", f"{active_days - placebo_days:.2f}", "days per 28 days",
         "difference in fitted means, not 28-day remission"),
        ("motor_seizure_free_day_ratio", f"{active_days / placebo_days:.4f}", "ratio",
         "17.34 / 10.43; arithmetic, not a refit"),
    )


def registry_rows(files):
    snapshots = files / "deepening_downloads" / "relutrigine_20261127"
    for trial, expected in TRIAL_SNAPSHOTS.items():
        payload = (snapshots / f"{trial}.json").read_bytes()
        if hashlib.sha256(payload).hexdigest() != expected:
            raise ValueError(f"Unexpected snapshot for {trial}")
        record = json.loads(payload)
        protocol = record["protocolSection"]
        eligibility = protocol["eligibilityModule"]
        yield (trial, protocol["statusModule"]["overallStatus"], record["hasResults"],
               eligibility["minimumAge"], eligibility["maximumAge"],
               protocol["designModule"]["enrollmentInfo"]["count"],
               "wwox" in eligibility["eligibilityCriteria"].casefold())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, help="Directory containing the pinned GEO and trial snapshots")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    for filename, header, rows in (
        ("sodium_state_fits.tsv", "drug assay midpoint_nM hill maximum_block midpoint_vs_persistent", fit_rows()),
        ("matched_block_scenarios.tsv", "drug matched_assay match_fraction concentration_nM block_persistent "
         "block_peak_tonic block_peak_10Hz block_peak_voltage_dependent", scenario_rows()),
        ("human_exposure_scenarios.tsv", "assay target_free_nM assumed_fu_plasma assumed_Kpuu required_total_plasma_ng_mL "
         "phase1_scenario_low_free_brain_nM phase1_scenario_high_free_brain_nM", exposure_rows()),
        ("clinical_aggregate_replay.tsv", "metric value unit basis", clinical_rows()),
        ("registry_checkpoint.tsv", "trial status posted_results lower_age upper_age enrollment_figure wwox_named", registry_rows(args.files)),
    ):
        tsv(args.output / filename, header.split(), rows)

    verified_expression(args.files)
    tsv(args.output / "wwox_sodium_bulk.tsv", "model accession gene ctrl_n ko_n ctrl_positive ko_positive "
        "ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(), bulk_panel(args.files, BULK_PANEL))
    tsv(args.output / "wwox_sodium_nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, NUCLEI_PANEL))


if __name__ == "__main__":
    main()
