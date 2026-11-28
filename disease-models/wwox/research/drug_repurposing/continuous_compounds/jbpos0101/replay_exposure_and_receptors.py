"""Replay JBPOS0101 registry summaries and the held WWOX receptor RNA screen."""

import argparse
import csv
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent
sys.path.insert(0, str(HERE.parent / "sodium_benzoate"))
sys.path.insert(0, str(HERE.parent / "probenecid"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_purine_exposure import verified

MOLAR_MASS = 229.66  # PubChem CID 57524523, g/mol
SNAPSHOT_SHA256 = "df82a2a2d0dc7d4f998b9eb463a8d6cf6a511b6715b25d7b4ca349f53ac53264"
PANEL = ("Grm1", "Grm4", "Grm5", "Grm7", "Elfn1", "Elfn2", "Slc1a2", "Gad1", "Slc17a7")


def single_summary(outcome):
    """Return the one posted group-level value, spread and denominator."""
    classes, = outcome["classes"]
    category, = classes["categories"]
    measure, = category["measurements"]
    population, = outcome["denoms"]
    count, = population["counts"]
    assert count["groupId"] == measure["groupId"]
    return float(measure["value"]), measure.get("spread"), int(count["value"])


def concentration_rows(outcomes):
    for index, outcome in enumerate(outcomes, 1):
        if "Concentration" not in outcome["title"]:
            continue
        assert outcome["paramType"] == "MEAN" and outcome["dispersionType"] == "Standard Deviation"
        assert "ng/mL" in outcome["unitOfMeasure"]
        value, spread, count = single_summary(outcome)
        compartment = "plasma" if "Plasma" in outcome["title"] else "urine"
        yield (index, compartment, outcome["title"], outcome["timeFrame"], count, f"{value:.2f}", spread,
               f"{value/MOLAR_MASS:.4f}", f"{float(spread)/MOLAR_MASS:.4f}")


def window_rows(concentrations):
    plasma = [r for r in concentrations if r[1] == "plasma"]
    assert len(plasma) == 6
    for day1, day21 in zip(plasma[:3], plasma[3:]):
        assert "Day 1" in day1[2] and "Day 21" in day21[2]
        ratio = float(day21[5]) / float(day1[5])
        yield day1[2], day1[4], day21[2], day21[4], f"{ratio:.4f}", f"{ratio/(15/6):.4f}"


def safety_rows(results):
    events = results["adverseEventsModule"]
    aggregate, = events["eventGroups"]
    for prefix, label in (("deaths", "All-cause mortality"), ("serious", "Any serious adverse event"),
                          ("other", "Any other adverse event")):
        yield "aggregate", label, aggregate[f"{prefix}NumAffected"], aggregate[f"{prefix}NumAtRisk"], "NA"
    for category in ("seriousEvents", "otherEvents"):
        for event in events[category]:
            stat, = event["stats"]
            yield category, event["term"], stat["numAffected"], stat["numAtRisk"], stat["numEvents"]


def coverage_rows(trial):
    result = trial["resultsSection"]
    protocol = trial["protocolSection"]
    outcomes = result["outcomeMeasuresModule"]["outcomeMeasures"]
    titles = [outcome["title"] for outcome in outcomes]
    flow, = result["participantFlowModule"]["periods"]
    yield "registry_actual_enrollment", protocol["designModule"]["enrollmentInfo"]["count"], "Design module"
    for row in flow["milestones"]:
        count, = row["achievements"]
        yield row["type"], count["numSubjects"], "Participant flow"
    for item, token in (("day28_eeg_response", "electroencephalogram"), ("spasm_or_hypsarrhythmia_response", "spasm"),
                        ("taper_relapse", "relapse"), ("seizure_diary_response", "diary"), ("CGI-C", "global impression")):
        found = [title for title in titles if token in title.lower()]
        assert not found, found
        yield item, "not_posted", "Prespecified analysis plan §6.2 and table shells 14.2.1–14.2.4"
    yield "EAS_or_mEAS_denominator", "not_posted", "Completion and PK denominators do not establish EEG evaluability"
    yield "raw_posted_outcome_count", len(outcomes), "Outcome measures module"


def exposure_scenarios(child_early_day21_total):
    # The two adult values are mean steady-state Cmax, Hwang et al. Table 3, not window means.
    adult_no_cbz, adult_cbz = (22287.51 / MOLAR_MASS, 14763.88 / MOLAR_MASS)
    yield "pediatric_day21_first_window_mean", f"{child_early_day21_total:.4f}", "NA", "NA", "NA"
    yield "adult_mean_Cmax_alone", f"{adult_no_cbz:.4f}", "NA", "NA", "NA"
    yield "adult_mean_Cmax_with_CBZ", f"{adult_cbz:.4f}", "NA", "NA", "NA"
    for fu in (0.1, 0.5, 0.9):
        for ratio in (0.1, 0.3, 1.0):
            yield ("pediatric_day21_first_window_sensitivity", f"{child_early_day21_total:.4f}", fu, ratio,
                   f"{child_early_day21_total * fu * ratio:.4f}")


def verified_expression(files):
    manifest = RESEARCH / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as stream:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    patterns = (("reference_ensembl_r92", "*.fa.gz"), ("geo/GSE156243", "*count_table.txt.gz"),
                ("geo/GSE158681", "*TPM_Table.txt.gz"), ("geo/GSE158682", "*TPM_Table.txt.gz"),
                ("geo/GSE158684", "*filtered_features.tsv.gz"), ("geo/GSE158684", "*filtered_matrix.mtx.gz"))
    for folder, pattern in patterns:
        paths = sorted((files / folder).glob(pattern))
        assert len(paths) == (2 if folder.endswith("GSE158684") else 1), (folder, paths)
        for path in paths:
            verified(path, hashes[path.name])


def main(files, out):
    trial_path = files / "deepening_downloads/jbpos0101_20261127/NCT03976076.json"
    trial = json.loads(verified(trial_path, SNAPSHOT_SHA256))
    assert trial["hasResults"] and trial["protocolSection"]["statusModule"]["overallStatus"] == "TERMINATED"
    out.mkdir(parents=True, exist_ok=True)
    results = trial["resultsSection"]
    outcomes = results["outcomeMeasuresModule"]["outcomeMeasures"]
    concentrations = list(concentration_rows(outcomes))
    tsv(out / "concentrations.tsv", "posted_row matrix outcome time_window analyzed_n mean_ng_mL SD_ng_mL mean_uM SD_uM".split(), concentrations)
    tsv(out / "window_ratios.tsv", "day1_outcome day1_n day21_outcome day21_n ratio_of_means ratio_per_nominal_dose_step".split(),
        window_rows(concentrations))
    tsv(out / "safety.tsv", "category endpoint participants_affected participants_at_risk events".split(), safety_rows(results))
    tsv(out / "coverage.tsv", "endpoint value locator".split(), coverage_rows(trial))
    child_early = next(float(r[5]) / MOLAR_MASS for r in concentrations if r[0] == 5)
    tsv(out / "exposure_sensitivity.tsv", "source total_plasma_uM assumed_fu_plasma assumed_Kpuu scenario_free_brain_uM".split(),
        exposure_scenarios(child_early))
    verified_expression(files)
    tsv(out / "bulk_receptors.tsv", "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(files, PANEL))
    tsv(out / "nuclei_receptors.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(), nuclei_panel(files, PANEL))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    main(args.files, args.out)
