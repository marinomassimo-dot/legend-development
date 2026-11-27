"""Replay the CoA-Z double-blind registry outcome means and denominators."""
import argparse
import csv
from hashlib import sha256
import json
from pathlib import Path
import sys


SOURCE_DIGEST = "c0c62bb5920e902c83afa859fdd3bdb8b6fa5e926df131a6f86ec7c0ca4ff00e"
MEASURES = {
    "Number of Treatment-emergent Adverse Events Assessed Using CTCAE v4.0": "TEAE",
    "CoASY mRNA Expression": "CoASY_mRNA",
}


def selected_rows(record):
    outcomes = record["resultsSection"]["outcomeMeasuresModule"]["outcomeMeasures"]
    for outcome in outcomes:
        if outcome["title"] not in MEASURES:
            continue
        groups = {group["id"]: group["title"] for group in outcome["groups"]}
        counts = {group["groupId"]: group["value"] for group in outcome["denoms"][0]["counts"]}
        for timepoint, analysis in zip(outcome["classes"], outcome["analyses"], strict=True):
            for category in timepoint["categories"]:
                estimates = {v["groupId"]: float(v["value"]) for v in category["measurements"]}
                placebo, = (key for key in estimates if groups[key] == "Placebo")
                for key, estimate in estimates.items():
                    yield (MEASURES[outcome["title"]], timepoint.get("title", outcome["timeFrame"]),
                           groups[key], counts[key], f"{estimate:.2f}", outcome["unitOfMeasure"],
                           f"{estimate / estimates[placebo]:.4f}", analysis["pValue"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry_json", type=Path)
    args = parser.parse_args()
    source = args.registry_json.read_bytes()
    if sha256(source).hexdigest() != SOURCE_DIGEST:
        raise ValueError("Unexpected registry export. Compare versions before replay.")
    rows = list(selected_rows(json.loads(source)))
    assert len(rows) == 12
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("endpoint", "period", "arm", "registered_n", "estimate", "units",
                  "descriptive_ratio_to_placebo", "registered_global_or_trend_p"))
    out.writerows(rows)


if __name__ == "__main__":
    main()
