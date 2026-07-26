#!/usr/bin/env python3
"""Apply the public disease-level proband priority matrix to sweep records."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_MATRIX = (
    Path(__file__).resolve().parents[1]
    / "references"
    / "proband_priority_matrix.json"
)


def load_records(path: Path) -> list[dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and isinstance(payload.get("records"), list):
        return payload["records"]
    if isinstance(payload, list):
        return payload
    raise ValueError("Input JSON must be a list or an object with a records list")


def term_hit(text: str, terms: list[str]) -> bool:
    haystack = text.lower()
    for term in terms:
        needle = term.lower()
        if len(needle) <= 4 and needle.replace("-", "").isalnum():
            if re.search(rf"(?<![a-z0-9]){re.escape(needle)}(?![a-z0-9])", haystack):
                return True
        elif needle in haystack:
            return True
    return False


def condition_hit(record: dict[str, object], condition: str) -> bool:
    key, separator, value = condition.partition(":")
    return bool(separator and key and value and str(record.get(key, "")) == value)


def apply_matrix(
    record: dict[str, object], matrix: dict[str, object]
) -> dict[str, object]:
    text = " ".join(
        str(record.get(key, ""))
        for key in ("title", "abstract", "sweep_reason", "journal")
    )
    axes_hit: list[dict[str, object]] = []
    score = 0

    for axis in matrix.get("axes", []):
        if term_hit(text, axis.get("terms", [])):
            weight = int(axis.get("weight", 0))
            score += weight
            axes_hit.append(
                {
                    "id": axis["id"],
                    "label": axis.get("label", axis["id"]),
                    "weight": weight,
                }
            )

    axis_ids = {str(axis["id"]) for axis in axes_hit}
    penalties_hit: list[dict[str, object]] = []
    for penalty in matrix.get("penalties", []):
        unless = set(penalty.get("unless_any_axis", []))
        if unless and axis_ids.intersection(unless):
            continue
        if term_hit(text, penalty.get("terms", [])):
            weight = int(penalty.get("weight", 0))
            score += weight
            penalties_hit.append({"id": penalty["id"], "weight": weight})

    boosts_hit: list[dict[str, object]] = []
    for boost in matrix.get("boosts", []):
        if condition_hit(record, str(boost.get("condition", ""))):
            weight = int(boost.get("weight", 0))
            score += weight
            boosts_hit.append({"condition": boost["condition"], "weight": weight})

    tier = "P4_BACKGROUND"
    for candidate in matrix.get("tiers", []):
        if score >= int(candidate.get("min_score", -999)):
            tier = str(candidate["name"])
            break

    enriched = dict(record)
    enriched["proband_score"] = score
    enriched["proband_priority_tier"] = tier
    enriched["proband_axes"] = axes_hit
    enriched["proband_penalties"] = penalties_hit
    enriched["proband_boosts"] = boosts_hit
    labels = ", ".join(str(axis["label"]) for axis in axes_hit[:5])
    enriched["proband_rationale"] = labels or "No strong disease-model axis hit"
    return enriched


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--matrix", default=str(DEFAULT_MATRIX))
    args = parser.parse_args()

    matrix = json.loads(Path(args.matrix).read_text(encoding="utf-8"))
    records = [apply_matrix(record, matrix) for record in load_records(Path(args.input))]
    records.sort(
        key=lambda item: (
            -int(item.get("proband_score", 0)),
            -int(item.get("sweep_score", 0)),
            str(item.get("pmid", "")),
        )
    )
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(
            {"matrix_version": matrix.get("version"), "records": records},
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
