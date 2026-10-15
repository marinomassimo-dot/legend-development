#!/usr/bin/env python3
"""Build non-canonical candidate cards from explicitly qualified local assertions.

No network, ranking, source verification or scientific promotion. Direction is a
comparison on the SAME target/endpoint/context, never inferred from graph proximity.
Work is linear in supplied assertions; raw source-specific fields survive unchanged.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path


CONTEXT = ("disease_id", "genotype", "species", "cell_type", "developmental_stage")
SIGNS = {"INCREASE": 1, "DECREASE": -1, "UNKNOWN": None}
TAGS = {"DATO", "INFERENZA", "IPOTESI", "ESPANSIONE"}
READING = {"complete_fulltext_read", "partial_fulltext_read", "abstract_only",
           "retrieved_not_read", "queried_not_full_read", "UNKNOWN"}


def validate_assertion(row: dict) -> None:
    if not isinstance(row, dict):
        raise ValueError("assertion must be an object")
    for field in ("id", "target_id", "endpoint", "source", "locator"):
        if not isinstance(row.get(field), str) or not row[field].strip():
            raise ValueError(f"assertion requires nonempty {field}")
    if row.get("direction") not in SIGNS:
        raise ValueError("direction must be INCREASE, DECREASE or UNKNOWN")
    if row.get("epistemic_status") not in TAGS:
        raise ValueError("invalid epistemic_status")
    if row.get("reading_depth", "UNKNOWN") not in READING:
        raise ValueError("invalid reading_depth")
    context = row.get("context")
    if not isinstance(context, dict) or any(
        not isinstance(context.get(key), str) or not context[key].strip() for key in CONTEXT
    ):
        raise ValueError("context must declare all dimensions (UNKNOWN is allowed)")
    if row.get("reading_depth") == "complete_fulltext_read" and not row.get("receipt"):
        raise ValueError("a complete-read declaration requires a receipt reference")


def build_card(payload: dict) -> dict:
    """Retain the input packet and compare signs without claiming efficacy."""
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise ValueError("input schema_version must be 1")
    if payload.get("route") not in {"RECUPERO_PROFONDO", "BENEFICIO_PRECOCE"}:
        raise ValueError("route must name one of the two research objectives")
    if not isinstance(payload.get("candidate"), dict) or any(
        not isinstance(payload["candidate"].get(key), str) or not payload["candidate"][key].strip()
        for key in ("id", "name")
    ):
        raise ValueError("candidate requires id and name")
    disease = payload.get("disease_assertion")
    validate_assertion(disease)
    assertions = payload.get("drug_assertions")
    if not isinstance(assertions, list):
        raise ValueError("drug_assertions must be a list (empty permits abstention)")
    for row in assertions:
        validate_assertion(row)
    ids = [disease["id"]] + [row["id"] for row in assertions]
    if len(ids) != len(set(ids)):
        raise ValueError("assertion identifiers must be unique")
    results = []
    for row in assertions:
        reasons = []
        for key in ("target_id", "endpoint"):
            if disease[key] != row[key] or disease[key] == "UNKNOWN":
                reasons.append(f"{key}: mismatch or unknown")
        for key in CONTEXT:
            if disease["context"][key] != row["context"][key] or disease["context"][key] == "UNKNOWN":
                reasons.append(f"context.{key}: mismatch or unknown")
        if disease["direction"] == "UNKNOWN" or row["direction"] == "UNKNOWN":
            reasons.append("direction unknown")
        status = "UNRESOLVED" if reasons else (
            "OPPOSES_DISEASE_CHANGE" if SIGNS[disease["direction"]] != SIGNS[row["direction"]]
            else "REINFORCES_DISEASE_CHANGE")
        results.append({"assertion_id": row["id"], "status": status, "reasons": reasons})
    known = {row["status"] for row in results} - {"UNRESOLVED"}
    unresolved = not results or any(row["status"] == "UNRESOLVED" for row in results)
    summary = ("CONFLICTING" if len(known) > 1 else "UNRESOLVED" if unresolved
               else next(iter(known)))
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()
    return {
        "schema_version": 1, "input_sha256": hashlib.sha256(raw).hexdigest(),
        "epistemic_status": "IPOTESI", "canonical": False,
        "assessment": "REQUIRES_QUALIFICATION" if unresolved or len(known) > 1
        else "DIRECTIONAL_COMPARISON_ONLY",
        "directional_summary": summary, "comparisons": results,
        "input": copy.deepcopy(payload),
        "translation": {key: "UNKNOWN" for key in (
            "pediatric_suitability", "cns_exposure", "interactions", "access",
            "time_to_benefit", "functional_rescue")},
        "next_step": "Qualify provenance and context; specify a proximal functional experiment; apply legend-safety-triage.",
        "limits": ["Technical comparison is not efficacy, safety or experimental validation.",
                   "Sources and receipt references are retained, not independently verified.",
                   "Shared sources are not independent confirmations; scores are not pooled."],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="local JSON evidence packet")
    args = parser.parse_args(argv)
    try:
        card = build_card(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, TypeError) as exc:
        print(f"INVALID_INPUT: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(card, indent=2, ensure_ascii=False, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
