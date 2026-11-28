"""Replay public week-24 primary and all-cause safety comparisons for MIT-E."""

import argparse
import csv
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
NCT = "https://clinicaltrials.gov/api/v2/studies/NCT04378075"
EUDRACT = "https://www.clinicaltrialsregister.eu/ctr-search/trial/2020-002100-39/results"


def two_sided_fisher(events_a, size_a, events_b, size_b):
    total = events_a + events_b
    observed = comb(size_a, events_a) * comb(size_b, events_b)
    support = range(max(0, total - size_b), min(size_a, total) + 1)
    weights = (comb(size_a, count) * comb(size_b, total - count) for count in support)
    return sum(weight for weight in weights if weight <= observed) / comb(size_a + size_b, total)


def comparison(primary, safety, eu_safety):
    outcome, = primary["primary_outcome"]
    assert outcome["timeFrame"] == "Baseline to Week 24"
    active, placebo = outcome["groups"]
    assert active["id"] == "OG000" and "Vatiquinone" in active["title"]
    assert placebo["id"] == "OG001" and "Placebo" in placebo["title"]
    denominator, = outcome["denoms"]
    counts = {item["groupId"]: int(item["value"]) for item in denominator["counts"]}
    outcome_class, = outcome["classes"]
    category, = outcome_class["categories"]
    medians = {m["groupId"]: float(m["value"]) for m in category["measurements"]}
    analysis, = outcome["analyses"]
    yield ("primary_week24_change", "percent", counts["OG000"], counts["OG001"],
           medians["OG000"], medians["OG001"], f"{medians['OG000'] - medians['OG001']:.2f}",
           analysis["paramValue"], analysis["ciLowerLimit"], analysis["ciUpperLimit"],
           analysis["pValue"], "reported Hodges–Lehmann estimate and rank ANCOVA p-value")
    active, placebo = safety["ae_groups"][:2]
    assert active["id"] == "EG000" and placebo["id"] == "EG001"
    n_active, n_placebo = active["seriousNumAtRisk"], placebo["seriousNumAtRisk"]
    serious = [active["seriousNumAffected"], placebo["seriousNumAffected"]]
    assert eu_safety["column_order"] == ["double_blind_vatiquinone", "double_blind_placebo"]
    assert eu_safety["participants_exposed"] == [n_active, n_placebo]
    assert eu_safety["participants_with_serious_adverse_event"] == serious
    delta = 100 * (serious[0] / n_active - serious[1] / n_placebo)
    p_value = two_sided_fisher(serious[0], n_active, serious[1], n_placebo)
    yield ("serious_adverse_event", "participants", n_active, n_placebo, *serious,
           f"{delta:.2f}", "", "", "", f"{p_value:.6f}",
           "both registries agree, exploratory Fisher exact and risk difference")

    double_blind = primary["participant_flow"]["periods"][0]
    assert double_blind["title"] == "Double-blind (24 Weeks)"
    death, = (entry for entry in double_blind["dropWithdraws"] if entry["type"] == "Death")
    reasons = {entry["groupId"]: int(entry["numSubjects"]) for entry in death["reasons"]}
    disposition = [reasons["FG000"], reasons["FG001"]]
    assert disposition == eu_safety["fatal_serious_adverse_event_as_reason_for_noncompletion"]
    assert [active["deathsNumAtRisk"], placebo["deathsNumAtRisk"]] == [n_active, n_placebo]
    for endpoint, counts, source in (
        ("death_as_noncompletion_reason", disposition, "both registry disposition tables"),
        ("all_cause_death_us_ae_summary", [active["deathsNumAffected"], placebo["deathsNumAffected"]],
         "ClinicalTrials.gov adverse event table, timing unresolved across registries"),
        ("all_cause_death_eu_ae_summary", eu_safety["all_cause_deaths_in_adverse_event_summary"],
         "EudraCT adverse event table, timing unresolved across registries"),
    ):
        yield (endpoint, "participants", n_active, n_placebo, *counts, "", "", "", "", "", source)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot_dir", type=Path)
    args = parser.parse_args()
    primary = json.loads((args.snapshot_dir / "MIT_E_primary_registry_projection.json").read_text())
    safety = json.loads((args.snapshot_dir / "MIT_E_status_age_safety_projection.json").read_text())
    eu_safety = json.loads((args.snapshot_dir / "MIT_E_eudract_safety_projection.json").read_text())
    assert primary["source"] == safety["source"] == NCT
    assert eu_safety["source"] == EUDRACT
    assert primary["retrieved_date"] == safety["retrieved"] == eu_safety["retrieved_date"]
    with (HERE / "mit_e_comparison.tsv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow((
            "endpoint", "unit", "n_vatiquinone", "n_placebo", "vatiquinone", "placebo",
            "unadjusted_difference_pp", "reported_hodges_lehmann_difference_pp", "ci95_low_pp",
            "ci95_high_pp", "p_value", "contrast",
        ))
        writer.writerows(comparison(primary, safety, eu_safety))


if __name__ == "__main__":
    main()
