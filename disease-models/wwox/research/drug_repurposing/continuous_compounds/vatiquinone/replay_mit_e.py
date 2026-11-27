"""Replay public week-24 primary and all-cause safety comparisons for MIT-E."""

import argparse
import csv
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
NCT = "https://clinicaltrials.gov/api/v2/studies/NCT04378075"


def two_sided_fisher(events_a, size_a, events_b, size_b):
    total = events_a + events_b
    observed = comb(size_a, events_a) * comb(size_b, events_b)
    support = range(max(0, total - size_b), min(size_a, total) + 1)
    weights = (comb(size_a, count) * comb(size_b, total - count) for count in support)
    return sum(weight for weight in weights if weight <= observed) / comb(size_a + size_b, total)


def comparison(primary, safety):
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
           analysis["pValue"], "reported ANCOVA comparison")
    active, placebo = safety["ae_groups"][:2]
    assert active["id"] == "EG000" and placebo["id"] == "EG001"
    for endpoint, key in (("serious_adverse_event", "serious"), ("all_cause_death", "deaths")):
        events_active = active[f"{key}NumAffected"]
        events_placebo = placebo[f"{key}NumAffected"]
        n_active = active[f"{key}NumAtRisk"]
        n_placebo = placebo[f"{key}NumAtRisk"]
        p_value = two_sided_fisher(events_active, n_active, events_placebo, n_placebo)
        difference = 100 * (events_active / n_active - events_placebo / n_placebo)
        yield (endpoint, "participants", n_active, n_placebo, events_active, events_placebo,
               f"{difference:.2f}", "", "", "", f"{p_value:.6f}",
               "exploratory Fisher exact, unadjusted, difference in percentage points")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot_dir", type=Path)
    args = parser.parse_args()
    primary = json.loads((args.snapshot_dir / "MIT_E_primary_registry_projection.json").read_text())
    safety = json.loads((args.snapshot_dir / "MIT_E_status_age_safety_projection.json").read_text())
    assert primary["source"] == safety["source"] == NCT
    assert primary["retrieved_date"] == safety["retrieved"]
    with (HERE / "mit_e_comparison.tsv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow((
            "endpoint", "unit", "n_vatiquinone", "n_placebo", "vatiquinone", "placebo",
            "unadjusted_difference_pp", "reported_ancova_difference_pp", "ci95_low_pp",
            "ci95_high_pp", "p_value", "contrast",
        ))
        writer.writerows(comparison(primary, safety))


if __name__ == "__main__":
    main()
