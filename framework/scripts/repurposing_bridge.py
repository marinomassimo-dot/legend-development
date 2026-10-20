#!/usr/bin/env python3
"""Build non-canonical candidate cards from explicitly qualified local assertions.

No network, ranking, source verification or scientific promotion. Direction is a
comparison on the SAME target/endpoint/context, never inferred from graph proximity.
Work is linear in supplied assertions; raw source-specific fields survive unchanged.

Two P4 card surfaces are declared, never performed here, because this tool has no
network: the drug-label search (`label_lookup`) and the later P4 fields (`p4_fields`).
The label search carries its outcome and its coverage on two separate axes, so that
NOT_ATTEMPTED, NO_MATCH_FOUND and QUERY_ERROR stay three different facts and neither
one removes a candidate, scores it or becomes biological counterevidence.
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
LOOKUP_STATUS = {"MATCH_FOUND", "NO_MATCH_FOUND", "QUERY_ERROR", "NOT_ATTEMPTED"}
LOOKUP_COVERAGE = {"COMPLETE_FOR_QUERIES_RUN", "COVERAGE_INCOMPLETE", "UNKNOWN"}
LOOKUP_METHOD = {"primary", "alternative", "primary_then_alternative", "UNKNOWN"}
LOOKUP_TEXT = ("source", "retrieved_at", "client_version", "product_name", "active_ingredient",
               "formulation", "spl_id", "error", "coverage_limit")
P4_TEXT = ("endpoint_pursued", "functional_evidence_available", "temporal_or_model_limit")
P4_CONTEXT = ("target_expression", "cells_tissue_stage", "coverage", "limits")


def normalise_label_lookup(block: object) -> dict:
    """Declare what a pharmacological-label search returned, outcome and coverage apart."""
    if block is None:
        block = {"status": "NOT_ATTEMPTED"}
    if not isinstance(block, dict):
        raise ValueError("label_lookup must be an object")
    allowed = {"status", "coverage", "method", "queries", *LOOKUP_TEXT}
    if set(block) - allowed:
        raise ValueError(f"unknown label_lookup field(s): {sorted(set(block) - allowed)}")
    status = block.get("status")
    if status not in LOOKUP_STATUS:
        raise ValueError(f"label_lookup status must be one of {sorted(LOOKUP_STATUS)}")
    coverage = block.get("coverage", "UNKNOWN")
    if coverage not in LOOKUP_COVERAGE:
        raise ValueError(f"label_lookup coverage must be one of {sorted(LOOKUP_COVERAGE)}")
    method = block.get("method", "UNKNOWN")
    if method not in LOOKUP_METHOD:
        raise ValueError(f"label_lookup method must be one of {sorted(LOOKUP_METHOD)}")
    queries = block.get("queries", [])
    if not isinstance(queries, list) or any(
            not isinstance(item, str) or not item.strip() for item in queries):
        raise ValueError("label_lookup queries must be a list of nonempty strings")
    out = {"status": status, "coverage": coverage, "method": method, "queries": list(queries)}
    for field in LOOKUP_TEXT:
        value = block.get(field, "UNKNOWN")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"label_lookup {field} must be a nonempty string or UNKNOWN")
        out[field] = value
    if status == "NOT_ATTEMPTED":
        if queries:
            raise ValueError("NOT_ATTEMPTED cannot carry queries: it means no search was run")
    elif not queries:
        raise ValueError("a concluded label search must record the queries actually run")
    if status == "MATCH_FOUND" and out["product_name"] == "UNKNOWN" and out["spl_id"] == "UNKNOWN":
        raise ValueError("MATCH_FOUND requires the product identity or its SPL identifier")
    if status == "QUERY_ERROR" and out["error"] == "UNKNOWN":
        raise ValueError("QUERY_ERROR requires the error actually returned")
    if coverage == "COVERAGE_INCOMPLETE" and out["coverage_limit"] == "UNKNOWN":
        raise ValueError("COVERAGE_INCOMPLETE requires the limit that makes it incomplete")
    return out


def normalise_p4_fields(block: object) -> dict:
    """Keep the later P4 fields present and UNKNOWN rather than absent."""
    if block is None:
        block = {}
    if not isinstance(block, dict):
        raise ValueError("p4_fields must be an object")
    allowed = {*P4_TEXT, "cellular_context"}
    if set(block) - allowed:
        raise ValueError(f"unknown p4_fields field(s): {sorted(set(block) - allowed)}")
    context = block.get("cellular_context") or {}
    if not isinstance(context, dict):
        raise ValueError("p4_fields cellular_context must be an object")
    if set(context) - set(P4_CONTEXT):
        raise ValueError(f"unknown cellular_context field(s): {sorted(set(context) - set(P4_CONTEXT))}")
    out: dict = {}
    for field in P4_TEXT:
        value = block.get(field, "UNKNOWN")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"p4_fields {field} must be a nonempty string or UNKNOWN")
        out[field] = value
    resolved = {}
    for field in P4_CONTEXT:
        value = context.get(field, "UNKNOWN")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"cellular_context {field} must be a nonempty string or UNKNOWN")
        resolved[field] = value
    out["cellular_context"] = resolved
    return out


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
    lookup = normalise_label_lookup(payload.get("label_lookup"))
    p4_fields = normalise_p4_fields(payload.get("p4_fields"))
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
    limits = ["Technical comparison is not efficacy, safety or experimental validation.",
              "Sources and receipt references are retained, not independently verified.",
              "Shared sources are not independent confirmations; scores are not pooled."]
    if lookup["status"] == "NOT_ATTEMPTED":
        limits.append("No pharmacological-label search was run: the label is unknown here, "
                      "which is not NO_MATCH_FOUND and not an absent label.")
    if lookup["status"] == "NO_MATCH_FOUND":
        limits.append("NO_MATCH_FOUND is information not available for those queries and that "
                      "coverage: it is not proof the label is absent, not DRUG_HAS_NO_LABEL, not "
                      "biological counterevidence and not a reason to drop the candidate.")
    if lookup["status"] == "QUERY_ERROR":
        limits.append("QUERY_ERROR is a failed search, never a concluded one: the question "
                      "remains open and the pharmacological gap stands.")
    if lookup["status"] == "MATCH_FOUND":
        limits.append("A label exists for the product identified; presence certifies neither "
                      "approval, currency, paediatric suitability nor WOREE relevance.")
    if lookup["coverage"] == "COVERAGE_INCOMPLETE":
        limits.append("Coverage is incomplete and is recorded apart from the query outcome: "
                      f"{lookup['coverage_limit']}")
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()
    return {
        "schema_version": 1, "input_sha256": hashlib.sha256(raw).hexdigest(),
        "epistemic_status": "IPOTESI", "canonical": False,
        "assessment": "REQUIRES_QUALIFICATION" if unresolved or len(known) > 1
        else "DIRECTIONAL_COMPARISON_ONLY",
        "directional_summary": summary, "comparisons": results,
        "abstention": "NO_DRUG_ASSERTIONS_SUPPLIED" if not results else None,
        "label_lookup": lookup, "p4_fields": p4_fields,
        "input": copy.deepcopy(payload),
        "translation": {key: "UNKNOWN" for key in (
            "pediatric_suitability", "cns_exposure", "interactions", "access",
            "time_to_benefit", "functional_rescue")},
        "next_step": "Qualify provenance and context; specify a proximal functional experiment; apply legend-safety-triage.",
        "limits": limits,
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
