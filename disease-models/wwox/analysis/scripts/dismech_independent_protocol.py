#!/usr/bin/env python3
"""Fail-closed tooling for the DisMech independent-derivation experiment.

This module does not perform the second scientific derivation.  It prepares and
verifies the isolated input bundle, checks the Phase-2 integrity baseline,
applies diagnostic-only canonicalisation, and compares two completed sidecars
without treating locally assigned ordinals as cross-run semantic identities.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ANALYSIS = HERE.parent
REPO_ROOT = HERE.parents[3]
DATA = ANALYSIS / "data"
BASELINE = DATA / "dismech_phase2_baseline.json"
BLIND_MANIFEST = DATA / "dismech_blind_input_manifest.json"
CANON_CONFIG = DATA / "dismech_canonicalisation_v1.json"
RECEIPT_PROJECTION = DATA / "dismech_blind_receipt_projection.jsonl"
RECEIPT_LEDGER = REPO_ROOT / "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
ARCHIVED_AUTHORED_REL = (
    "disease-models/wwox/analysis/data/"
    "dismech_second_derivation_authored_016_024_035.jsonl"
)
BLIND_MANIFEST_REL = Path(
    "disease-models/wwox/analysis/data/dismech_blind_input_manifest.json")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def production_fp(*parts: object) -> str:
    """Phase-2 production hash contract: UTF-8, `|` join, SHA-256, 12 hex."""
    return hashlib.sha256("|".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:12]


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"expected JSON object at {path}:{number}")
        rows.append(value)
    return rows


def _registry_block(text: str, kind: str, identifier: str) -> str:
    pattern = rf"^## {re.escape(kind)} {re.escape(identifier)}\b(.*?)(?=^## {re.escape(kind)} |\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError(f"missing {kind} {identifier}")
    return match.group(1)


def registry_scope_bytes(text: str, blocks: list[str]) -> bytes:
    """The declared blocks, concatenated in declared order, as sealed bytes.

    A freeze over a *living* registry must pin what the derivation consumed, not the file
    that happened to contain it. `BATCH_20260806_001` edited CLAIM 005 — outside the export
    scope of CLAIM 016/024/035, which had not moved by a byte — and a whole-file hash reported
    that as indistinguishable from an edit to the scope itself. It fires on every registry
    commit and cannot fire harder on the one commit that matters. See `FREEZE_SCOPE_GATE` and
    `scripts/test_freeze_scope.py`.
    """
    parts = []
    for block in blocks:
        kind, _, identifier = block.partition(" ")
        parts.append(f"## {kind} {identifier}" + _registry_block(text, kind, identifier))
    return "".join(parts).encode("utf-8")


def derive_receipt_projection(root: Path = REPO_ROOT,
                              manifest_path: Path | None = None) -> list[dict[str, Any]]:
    """Derive the complete eligibility projection from target claims and live receipts.

    Rule: for every paper cited by target_claim_ids, include the last ledger-ordered
    complete_fulltext_read event, if one exists.  Complete reads of papers outside
    the target claims are excluded.  First-pass locator events are never inputs.
    """
    manifest = load_json(manifest_path or (root / BLIND_MANIFEST_REL))
    claims = (root / "disease-models/wwox/registries/claim_registry_current.md").read_text(
        encoding="utf-8")
    papers = (root / "disease-models/wwox/registries/paper_registry_current.md").read_text(
        encoding="utf-8")
    ledger = load_jsonl(root / "disease-models/wwox/registries/fulltext_read_receipts.jsonl")

    cited: set[str] = set()
    for claim_id in manifest["target_claim_ids"]:
        block = _registry_block(claims, "CLAIM", claim_id)
        cited.update(re.findall(r"\bPAPER\s+(\d{3})\b", block))

    paper_pmids: dict[str, str] = {}
    for paper_id in sorted(cited):
        block = _registry_block(papers, "PAPER", paper_id)
        identifier = re.search(r"^\*\*Identifier:\*\*.*?\bPMID\s+([0-9]{7,8})\b",
                               block, re.MULTILINE)
        if not identifier:
            raise ValueError(f"PAPER {paper_id} has no PMID in its Identifier field")
        paper_pmids[paper_id] = identifier.group(1)

    active_complete: dict[str, dict[str, Any]] = {}
    for event in ledger:
        pmid = str(event.get("study_id", {}).get("pmid", ""))
        if pmid and event.get("evidence_depth") == "complete_fulltext_read":
            active_complete[pmid] = event

    bundle_sources = {entry["paper_id"]: entry["bundle_path"]
                      for entry in manifest["bundle_files"]
                      if entry.get("role") == "locator_source"}
    rows: list[dict[str, Any]] = []
    for paper_id, pmid in sorted(paper_pmids.items()):
        event = active_complete.get(pmid)
        if event is None:
            continue
        if paper_id not in bundle_sources:
            raise ValueError(f"PAPER {paper_id} has a complete receipt but no locator source")
        accession = str(event.get("source_locator", "")).split("|", 1)[0].strip()
        rows.append({
            "active_complete_receipt_event": event["event_id"],
            "evidence_depth": "complete_fulltext_read",
            "paper_id": paper_id,
            "projection_kind": "eligibility_only",
            "source_fingerprint": event.get("source_fingerprint"),
            "source_locator": f"{accession} | {bundle_sources[paper_id]}",
            "study_id": event["study_id"],
        })
    return rows


def render_receipt_projection(root: Path = REPO_ROOT,
                              manifest_path: Path | None = None) -> bytes:
    rows = derive_receipt_projection(root, manifest_path)
    return "".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
                   for row in rows).encode("utf-8")


def verify_receipt_projection(root: Path | None = None,
                              projection_path: Path | None = None) -> list[str]:
    root = root or REPO_ROOT
    expected = render_receipt_projection(root)
    projection = projection_path or (
        root / "disease-models/wwox/analysis/data/dismech_blind_receipt_projection.jsonl")
    if not projection.is_file():
        return ["receipt projection is missing"]
    if projection.read_bytes() != expected:
        return ["receipt projection is not the deterministic target-claim projection"]
    return []


def _git_blob(root: Path, revision: str, relative_path: str) -> bytes:
    result = subprocess.run(
        ["git", "cat-file", "blob", f"{revision}:{relative_path}"],
        cwd=root, capture_output=True)
    if result.returncode:
        raise ValueError(
            f"git blob unavailable: {revision}:{relative_path}: "
            f"{result.stderr.decode('utf-8', errors='replace').strip()}")
    return result.stdout


def _git_ok(root: Path, *arguments: str) -> bool:
    return subprocess.run(["git", *arguments], cwd=root, stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL).returncode == 0


def verify_phase2_baseline(path: Path | None = None, *, verify_git: bool = True) -> list[str]:
    """Return errors; an empty list means every sealed byte still matches."""
    path = path or BASELINE
    baseline = load_json(path)
    errors: list[str] = []
    freeze = baseline.get("git_head_at_freeze")
    if verify_git:
        try:
            relative_baseline = path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
            head_baseline = _git_blob(REPO_ROOT, "HEAD", relative_baseline)
        except (ValueError, OSError) as exc:
            errors.append(f"baseline git anchor unavailable: {exc}")
        else:
            if path.read_bytes() != head_baseline:
                errors.append("baseline working bytes differ from HEAD")
        if not freeze or not _git_ok(REPO_ROOT, "cat-file", "-e", f"{freeze}^{{commit}}"):
            errors.append("git_head_at_freeze is not an available commit")
        elif not _git_ok(REPO_ROOT, "merge-base", "--is-ancestor", freeze, "HEAD"):
            errors.append("git_head_at_freeze is not an ancestor of HEAD")

    for name, record in baseline["inputs"].items():
        source = REPO_ROOT / record["path"]
        if not source.is_file():
            errors.append(f"{name}: missing {record['path']}")
            continue
        if record.get("verification_policy") == "append_only_prefix":
            lines = source.read_bytes().splitlines(keepends=True)
            count = record["prefix_event_count"]
            if len(lines) < count:
                errors.append(f"{name}: ledger has {len(lines)} events, below sealed prefix {count}")
                continue
            prefix = b"".join(lines[:count])
            if sha256_bytes(prefix) != record["prefix_sha256"]:
                errors.append(f"{name}: sealed prefix bytes changed")
            try:
                tail = json.loads(lines[count - 1])
            except json.JSONDecodeError:
                errors.append(f"{name}: sealed prefix tail is not JSON")
            else:
                if tail.get("event_id") != record["prefix_tail_event_id"]:
                    errors.append(f"{name}: sealed prefix tail event changed")
        elif record.get("verification_policy") == "sealed_scope":
            try:
                scope = registry_scope_bytes(source.read_text(encoding="utf-8"),
                                             record["scope_blocks"])
            except ValueError as exc:
                errors.append(f"{name}: sealed scope no longer resolves: {exc}")
            else:
                if sha256_bytes(scope) != record["scope_sha256"]:
                    errors.append(f"{name}: sealed scope changed "
                                  f"({', '.join(record['scope_blocks'])})")
        elif sha256_file(source) != record["sha256"]:
            errors.append(f"{name}: sha256 mismatch")
        if verify_git and freeze:
            try:
                frozen_bytes = _git_blob(REPO_ROOT, freeze, record["path"])
            except ValueError as exc:
                errors.append(f"{name}: {exc}")
            else:
                if record.get("verification_policy") == "append_only_prefix":
                    frozen_lines = frozen_bytes.splitlines(keepends=True)
                    count = record["prefix_event_count"]
                    if len(frozen_lines) < count:
                        errors.append(f"{name}: frozen git blob is shorter than sealed prefix")
                    elif sha256_bytes(b"".join(frozen_lines[:count])) != record["prefix_sha256"]:
                        errors.append(f"{name}: frozen git prefix disagrees with declared hash")
                elif record.get("verification_policy") == "sealed_scope":
                    try:
                        frozen_scope = registry_scope_bytes(
                            frozen_bytes.decode("utf-8"), record["scope_blocks"])
                    except ValueError as exc:
                        errors.append(f"{name}: frozen scope no longer resolves: {exc}")
                    else:
                        if sha256_bytes(frozen_scope) != record["scope_sha256"]:
                            errors.append(
                                f"{name}: frozen git scope disagrees with declared hash")
                elif sha256_bytes(frozen_bytes) != record["sha256"]:
                    errors.append(f"{name}: frozen git blob disagrees with declared hash")

    output = baseline["output"]
    output_path = REPO_ROOT / output["path"]
    if not output_path.is_file():
        errors.append(f"output: missing {output['path']}")
    elif sha256_file(output_path) != output["sha256"]:
        errors.append("output: sha256 mismatch")
    if verify_git and freeze:
        try:
            frozen_output = _git_blob(REPO_ROOT, freeze, output["path"])
        except ValueError as exc:
            errors.append(f"output: {exc}")
        else:
            if sha256_bytes(frozen_output) != output["sha256"]:
                errors.append("output: frozen git blob disagrees with declared hash")
    projection_record = baseline["inputs"].get("blind_receipt_projection")
    if projection_record:
        errors.extend(verify_receipt_projection(
            REPO_ROOT, REPO_ROOT / projection_record["path"]))
    return errors


def _manifest_file_set(manifest: dict[str, Any]) -> set[str]:
    return {entry["bundle_path"] for entry in manifest["bundle_files"]}


def build_blind_bundle(destination: Path) -> None:
    """Materialise only allowlisted inputs; refuse a non-empty destination."""
    baseline_errors = verify_phase2_baseline()
    if baseline_errors:
        raise ValueError("sealed baseline failed: " + "; ".join(baseline_errors))
    manifest = load_json(BLIND_MANIFEST)
    if destination.exists() and any(destination.iterdir()):
        raise ValueError(f"destination is not empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    for entry in manifest["bundle_files"]:
        source = REPO_ROOT / entry["source_path"]
        if not source.is_file():
            raise FileNotFoundError(f"required blind input absent: {entry['source_path']}")
        if sha256_file(source) != entry["sha256"]:
            raise ValueError(f"source hash mismatch: {entry['source_path']}")
        target = destination / entry["bundle_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    shutil.copyfile(BLIND_MANIFEST, destination / "MANIFEST.json")
    errors = verify_blind_bundle(destination, stage="pre")
    if errors:
        raise ValueError("built bundle failed verification: " + "; ".join(errors))


def verify_blind_bundle(bundle: Path, *, stage: str) -> list[str]:
    """Reject missing, modified and undeclared files in an isolated bundle."""
    manifest_path = bundle / "MANIFEST.json"
    if not manifest_path.is_file():
        return ["MANIFEST.json missing"]
    try:
        manifest = load_json(manifest_path)
    except (ValueError, json.JSONDecodeError) as exc:
        return [f"invalid MANIFEST.json: {exc}"]
    if sha256_file(manifest_path) != sha256_file(BLIND_MANIFEST):
        return ["MANIFEST.json does not match the sealed repository allowlist"]
    stage_outputs = {
        "pre": set(),
        "authored": {"output/second_derivation_authored.jsonl",
                     "output/run_attestation.json"},
        "reconciled": set(manifest.get("allowed_outputs", [])),
    }
    if stage not in stage_outputs:
        return [f"unknown verification stage: {stage}"]
    expected = _manifest_file_set(manifest) | {"MANIFEST.json"} | stage_outputs[stage]
    actual = {p.relative_to(bundle).as_posix() for p in bundle.rglob("*") if p.is_file()}
    errors = [f"undeclared file: {p}" for p in sorted(actual - expected)]
    errors.extend(f"missing file: {p}" for p in sorted(_manifest_file_set(manifest) - actual))
    errors.extend(f"missing {stage} output: {p}" for p in sorted(stage_outputs[stage] - actual))
    for entry in manifest.get("bundle_files", []):
        target = bundle / entry["bundle_path"]
        if target.is_file() and sha256_file(target) != entry["sha256"]:
            errors.append(f"hash mismatch: {entry['bundle_path']}")
    return errors


def load_canonicalisation(path: Path = CANON_CONFIG) -> dict[str, Any]:
    config = load_json(path)
    if config.get("version") != "dismech-canonicalisation-v1":
        raise ValueError("unsupported canonicalisation version")
    names = [step.get("name") for step in config.get("transforms_in_order", [])]
    expected = ["unicode_nfc", "dash_unification", "whitespace_collapse_and_trim",
                "closed_biomedical_aliases"]
    if names != expected:
        raise ValueError(f"canonicalisation order changed: {names}")
    return config


def canonicalise(text: str, config: dict[str, Any]) -> tuple[str, list[dict[str, str]]]:
    """Return a reviewable canonical string and the transforms that changed it."""
    current = text
    trace: list[dict[str, str]] = []

    normalised = unicodedata.normalize("NFC", current)
    if normalised != current:
        trace.append({"transform": "unicode_nfc", "before": current, "after": normalised})
        current = normalised

    dash_map = next(s["mapping"] for s in config["transforms_in_order"]
                    if s["name"] == "dash_unification")
    translated = "".join(dash_map.get(char, char) for char in current)
    if translated != current:
        trace.append({"transform": "dash_unification", "before": current, "after": translated})
        current = translated

    collapsed = re.sub(r"\s+", " ", current).strip()
    if collapsed != current:
        trace.append({"transform": "whitespace_collapse_and_trim",
                      "before": current, "after": collapsed})
        current = collapsed

    for alias in config.get("aliases", []):
        for variant in sorted(alias["variants"], key=len, reverse=True):
            pattern = re.compile(rf"(?<![\w]){re.escape(variant)}(?![\w])")
            replaced = pattern.sub(alias["canonical"], current)
            if replaced != current:
                trace.append({"transform": "closed_biomedical_aliases",
                              "before": current, "after": replaced,
                              "entity_id": alias["entity_id"]})
                current = replaced
    return current, trace


def canonical_record(record: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    proposition, p_trace = canonicalise(str(record.get("proposition", "")), config)
    context, c_trace = canonicalise(str(record.get("context", "")), config)
    key = sha256_bytes((proposition + "\0" + context).encode("utf-8"))[:16]
    return {"canonical_proposition": proposition, "canonical_context": context,
            "canonical_candidate_key": "CCK-" + key,
            "transform_trace": {"proposition": p_trace, "context": c_trace}}


def verify_canonicalisation(config: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for index, fixture in enumerate(config.get("positive_fixtures", []), 1):
        left = canonicalise(fixture["left"], config)[0]
        right = canonicalise(fixture["right"], config)[0]
        if left != right:
            errors.append(f"positive fixture {index} did not converge")
    for index, fixture in enumerate(config.get("negative_fixtures", []), 1):
        left = canonicalise(fixture["left"], config)[0]
        right = canonicalise(fixture["right"], config)[0]
        if left == right:
            errors.append(f"negative fixture {index} collapsed")
    return errors


def verify_reconciliation(bundle: Path, ledger_path: Path = RECEIPT_LEDGER) -> list[str]:
    """Prove that provenance reconciliation did not rewrite authored judgement."""
    errors = verify_blind_bundle(bundle, stage="reconciled")
    if errors:
        return errors
    authored = bundle / "output/second_derivation_authored.jsonl"
    reconciled = bundle / "output/second_derivation_reconciled.jsonl"
    attestation_path = bundle / "output/reconciliation_attestation.json"
    left, right = load_jsonl(authored), load_jsonl(reconciled)
    if len(left) != len(right):
        errors.append("reconciliation changed record count")
        return errors
    allowed = {"locator_extraction_receipt_event", "terminal_state", "unreached_tests"}
    for index, (before, after) in enumerate(zip(left, right), 1):
        before_fixed = {k: v for k, v in before.items() if k not in allowed}
        after_fixed = {k: v for k, v in after.items() if k not in allowed}
        if before_fixed != after_fixed:
            errors.append(f"reconciliation rewrote authored content at record {index}")
        mutable_changed = any(before.get(field) != after.get(field) for field in allowed)
        if before.get("terminal_state") != "LOCATOR_PROVENANCE_MISSING":
            if mutable_changed:
                errors.append(
                    f"reconciliation changed a record that was not provenance-blocked at record {index}")
            continue
        receipt_id = after.get("locator_extraction_receipt_event")
        if not receipt_id:
            errors.append(f"reconciliation omitted locator receipt at record {index}")
            continue
        expected_state = (
            "ELIGIBLE_FOR_EXPORT" if (before.get("locator") or {}).get("snippet")
            else "SOURCE_SUPPORT_NOT_FOUND"
        )
        if after.get("terminal_state") != expected_state:
            errors.append(
                f"reconciliation assigned {after.get('terminal_state')!r}, expected "
                f"{expected_state!r} at record {index}")
        if after.get("unreached_tests") != []:
            errors.append(f"reconciliation left unreached tests at record {index}")

    errors.extend(verify_reconciliation_receipt_lineage(bundle, left, right, ledger_path))
    attestation = load_json(attestation_path)
    if attestation.get("authored_sha256") != sha256_file(authored):
        errors.append("reconciliation attestation has wrong authored_sha256")
    if attestation.get("reconciled_sha256") != sha256_file(reconciled):
        errors.append("reconciliation attestation has wrong reconciled_sha256")
    if attestation.get("allowed_changed_fields") != sorted(allowed):
        errors.append("reconciliation attestation declares the wrong mutable fields")
    return errors


def receipt_descends_from(receipts: dict[str, dict[str, Any]], event_id: str,
                          ancestor_id: str) -> bool:
    """Return true when ancestor_id occurs anywhere in event_id's prior chain."""
    seen: set[str] = set()
    current = event_id
    while current and current not in seen:
        seen.add(current)
        if current == ancestor_id:
            return True
        event = receipts.get(current)
        if event is None:
            return False
        current = event.get("prior_receipt")
    return False


def same_study_identity(left: dict[str, Any], right: dict[str, Any]) -> bool:
    """Match on a shared PMID or DOI without requiring identical identifier coverage."""
    left_pmid, right_pmid = str(left.get("pmid", "")), str(right.get("pmid", ""))
    left_doi, right_doi = str(left.get("doi", "")).lower(), str(right.get("doi", "")).lower()
    return bool((left_pmid and left_pmid == right_pmid)
                or (left_doi and left_doi == right_doi))


def verify_reconciliation_receipt_lineage(
        bundle: Path, authored_rows: list[dict[str, Any]],
        reconciled_rows: list[dict[str, Any]],
        ledger_path: Path = RECEIPT_LEDGER) -> list[str]:
    """Validate post-blind locator receipts through full append-only ancestry."""
    errors: list[str] = []
    try:
        ledger_rows = load_jsonl(ledger_path)
        projection_rows = load_jsonl(bundle / "inputs/receipt_eligibility_projection.jsonl")
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        return [f"locator receipt lineage unavailable: {exc}"]
    receipts = {row.get("event_id"): row for row in ledger_rows if row.get("event_id")}
    projection = {f"PAPER {row['paper_id']}": row for row in projection_rows}
    checked: set[tuple[str, str]] = set()
    for number, (before, after) in enumerate(zip(authored_rows, reconciled_rows), 1):
        if before.get("terminal_state") != "LOCATOR_PROVENANCE_MISSING":
            continue
        source_id = str(before.get("source_id"))
        receipt_id = after.get("locator_extraction_receipt_event")
        if not receipt_id or (source_id, receipt_id) in checked:
            continue
        checked.add((source_id, receipt_id))
        projected = projection.get(source_id)
        receipt = receipts.get(receipt_id)
        if projected is None:
            errors.append(f"record {number}: {source_id} is absent from receipt projection")
            continue
        if receipt is None:
            errors.append(f"record {number}: locator receipt {receipt_id!r} is absent from ledger")
            continue
        if receipt.get("workflow") != "phase2_independent_locator_extraction":
            errors.append(f"record {number}: locator receipt has wrong workflow")
        if receipt.get("evidence_depth") != "queried_not_full_read":
            errors.append(f"record {number}: locator receipt has wrong evidence depth")
        if not same_study_identity(receipt.get("study_id", {}),
                                   projected.get("study_id", {})):
            errors.append(f"record {number}: locator receipt has wrong study identity")
        fingerprint = projected.get("source_fingerprint")
        if receipt.get("source_fingerprint") != fingerprint:
            errors.append(f"record {number}: locator receipt fingerprint differs from projection")
        locator = before.get("locator") or {}
        if locator and locator.get("source_fingerprint") != fingerprint:
            errors.append(f"record {number}: locator fingerprint differs from projection")
        qualifying = before.get("eligibility_receipt_event")
        if qualifying != projected.get("active_complete_receipt_event"):
            errors.append(f"record {number}: authored eligibility receipt differs from projection")
        elif not receipt_descends_from(receipts, receipt_id, qualifying):
            errors.append(
                f"record {number}: locator receipt does not descend from qualifying complete read")
        if ARCHIVED_AUTHORED_REL not in receipt.get("outputs", []):
            errors.append(f"record {number}: locator receipt does not name archived authored output")
    return errors


def reconcile_locator_receipts(bundle: Path, ledger_path: Path = RECEIPT_LEDGER) -> None:
    """Create the provenance-only reconciled output deterministically from the ledger."""
    errors = verify_blind_bundle(bundle, stage="authored")
    if errors:
        raise ValueError("authored bundle is invalid: " + "; ".join(errors))
    authored_path = bundle / "output/second_derivation_authored.jsonl"
    authored = load_jsonl(authored_path)
    projection_rows = load_jsonl(bundle / "inputs/receipt_eligibility_projection.jsonl")
    projection = {f"PAPER {row['paper_id']}": row for row in projection_rows}
    ledger = load_jsonl(ledger_path)
    receipts = {row.get("event_id"): row for row in ledger if row.get("event_id")}
    selected: dict[str, str] = {}
    for source_id, projected in projection.items():
        qualifying = projected["active_complete_receipt_event"]
        candidates = [
            row for row in ledger
            if row.get("workflow") == "phase2_independent_locator_extraction"
            and same_study_identity(row.get("study_id", {}),
                                    projected.get("study_id", {}))
            and ARCHIVED_AUTHORED_REL in row.get("outputs", [])
            and receipt_descends_from(receipts, row.get("event_id", ""), qualifying)
        ]
        if candidates:
            selected[source_id] = candidates[-1]["event_id"]

    reconciled: list[dict[str, Any]] = []
    for row in authored:
        updated = dict(row)
        if row.get("terminal_state") == "LOCATOR_PROVENANCE_MISSING":
            source_id = str(row.get("source_id"))
            if source_id not in selected:
                raise ValueError(f"no valid independent locator receipt for {source_id}")
            updated["locator_extraction_receipt_event"] = selected[source_id]
            updated["terminal_state"] = (
                "ELIGIBLE_FOR_EXPORT" if (row.get("locator") or {}).get("snippet")
                else "SOURCE_SUPPORT_NOT_FOUND")
            updated["unreached_tests"] = []
        reconciled.append(updated)
    reconciled_path = bundle / "output/second_derivation_reconciled.jsonl"
    reconciled_path.write_text(
        "".join(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n"
                for row in reconciled), encoding="utf-8")
    attestation = {
        "allowed_changed_fields": sorted(
            {"locator_extraction_receipt_event", "terminal_state", "unreached_tests"}),
        "authored_sha256": sha256_file(authored_path),
        "receipt_events": sorted(set(selected.values())),
        "receipt_lineage_check": "full ancestry to qualifying complete-read receipt",
        "reconciled_sha256": sha256_file(reconciled_path),
    }
    (bundle / "output/reconciliation_attestation.json").write_text(
        json.dumps(attestation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    errors = verify_reconciliation(bundle, ledger_path)
    if errors:
        raise ValueError("generated reconciliation is invalid: " + "; ".join(errors))


def verify_measurement_attestations(bundle: Path) -> list[str]:
    errors = verify_reconciliation(bundle)
    if errors:
        return errors
    manifest = bundle / "MANIFEST.json"
    authored = bundle / "output/second_derivation_authored.jsonl"
    run = load_json(bundle / "output/run_attestation.json")
    if run.get("protocol_version") != "blind-contract-v1":
        errors.append("run attestation has wrong protocol_version")
    if run.get("contamination_status") != "CLEAN":
        errors.append("run attestation is not CLEAN")
    if run.get("bundle_manifest_sha256") != sha256_file(manifest):
        errors.append("run attestation has wrong bundle manifest hash")
    if run.get("output_sha256") != sha256_file(authored):
        errors.append("run attestation has wrong authored output hash")
    errors.extend(verify_occurrence_hash_contract(
        bundle / "output/second_derivation_reconciled.jsonl"))
    return errors


def verify_occurrence_hash_contract(path: Path) -> list[str]:
    """Reject a second pass that used different structural or dedup conventions."""
    errors: list[str] = []
    required = {
        "candidate_id", "claim_id", "registry_anchor", "registry_ordinal", "occurrence_id",
        "proposition", "context", "source_id", "epistemic_type", "evidence_relation",
        "content_fingerprint", "locator_fingerprint", "dedup_key",
        "raw_link_role_paper_to_claim", "raw_link_role_claim_to_paper",
        "claim_link_basis", "normalised_role", "unreached_tests",
    }
    for number, row in enumerate(load_jsonl(path), 1):
        if row.get("record_kind") != "assertion_occurrence":
            continue
        missing = required - row.keys()
        if missing:
            errors.append(f"record {number}: occurrence missing {sorted(missing)}")
            continue
        expected_occ = "OCC-" + production_fp(
            row["claim_id"], row["registry_anchor"], row["registry_ordinal"])
        expected_content = "CF-" + production_fp(row["proposition"], row["context"])
        expected_dedup = "DK-" + production_fp(
            row["source_id"], row["proposition"], row["context"],
            row["locator_fingerprint"], row["epistemic_type"], row["evidence_relation"])
        if row["occurrence_id"] != expected_occ:
            errors.append(f"record {number}: occurrence_id violates the hash contract")
        if row["content_fingerprint"] != expected_content:
            errors.append(f"record {number}: content_fingerprint violates the hash contract")
        if row["dedup_key"] != expected_dedup:
            errors.append(f"record {number}: dedup_key violates the hash contract")
    return errors


def _occurrences(path: Path) -> list[dict[str, Any]]:
    rows = [r for r in load_jsonl(path) if r.get("record_kind") == "assertion_occurrence"]
    required = {"claim_id", "registry_anchor", "occurrence_id", "proposition", "context"}
    for row in rows:
        missing = required - row.keys()
        if missing:
            raise ValueError(f"{path}: occurrence missing {sorted(missing)}")
    return rows


def _anchor(record: dict[str, Any]) -> tuple[str, str]:
    return str(record["claim_id"]), str(record["registry_anchor"])


def _text_key(record: dict[str, Any]) -> tuple[str, str]:
    return str(record.get("proposition", "")), str(record.get("context", ""))


def _unique_matches(left: list[dict[str, Any]], right: list[dict[str, Any]], key_fn,
                    band: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]],
                                        list[dict[str, Any]], list[dict[str, Any]]]:
    """Match only unambiguous 1:1 keys; return matches, residuals and ambiguities."""
    l_groups: dict[Any, list[dict[str, Any]]] = defaultdict(list)
    r_groups: dict[Any, list[dict[str, Any]]] = defaultdict(list)
    for row in left:
        l_groups[key_fn(row)].append(row)
    for row in right:
        r_groups[key_fn(row)].append(row)
    matches: list[dict[str, Any]] = []
    used_left: set[str] = set()
    used_right: set[str] = set()
    ambiguous: list[dict[str, Any]] = []
    for key in sorted(set(l_groups) & set(r_groups), key=str):
        ls, rs = l_groups[key], r_groups[key]
        if len(ls) == len(rs) == 1:
            matches.append({"band": band, "baseline_occurrence_id": ls[0]["occurrence_id"],
                            "second_occurrence_id": rs[0]["occurrence_id"]})
            used_left.add(ls[0]["occurrence_id"])
            used_right.add(rs[0]["occurrence_id"])
        else:
            ambiguous.append({"band": band, "key": key,
                              "baseline_occurrence_ids": sorted(r["occurrence_id"] for r in ls),
                              "second_occurrence_ids": sorted(r["occurrence_id"] for r in rs)})
    return (matches,
            [r for r in left if r["occurrence_id"] not in used_left],
            [r for r in right if r["occurrence_id"] not in used_right], ambiguous)


def compare_derivations(baseline_path: Path, second_path: Path,
                        config: dict[str, Any]) -> dict[str, Any]:
    left = _occurrences(baseline_path)
    right = _occurrences(second_path)
    left_anchors, right_anchors = {_anchor(r) for r in left}, {_anchor(r) for r in right}
    shared = left_anchors & right_anchors
    union = left_anchors | right_anchors
    report: dict[str, Any] = {
        "comparison_contract": "independent-comparison-v1",
        "aggregate_verdict": None,
        "axis_1_anchor_selection": {
            "intersection_count": len(shared), "union_count": len(union),
            "jaccard_diagnostic": (len(shared) / len(union)) if union else 1.0,
            "baseline_only": sorted(left_anchors - right_anchors),
            "second_only": sorted(right_anchors - left_anchors),
        },
    }

    axis2 = []
    all_matches: list[dict[str, Any]] = []
    all_ambiguous: list[dict[str, Any]] = []
    unmatched_left: list[dict[str, Any]] = []
    unmatched_right: list[dict[str, Any]] = []
    left_by_anchor: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    right_by_anchor: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in left:
        left_by_anchor[_anchor(row)].append(row)
    for row in right:
        right_by_anchor[_anchor(row)].append(row)

    def values(rows, field):
        return sorted({str(r.get(field)) for r in rows})

    for anchor in sorted(shared):
        ls, rs = left_by_anchor[anchor], right_by_anchor[anchor]
        axis2.append({"anchor": anchor, "baseline_occurrence_count": len(ls),
                      "second_occurrence_count": len(rs),
                      "source_ids": [values(ls, "source_id"), values(rs, "source_id")],
                      "epistemic_types": [values(ls, "epistemic_type"), values(rs, "epistemic_type")],
                      "evidence_relations": [values(ls, "evidence_relation"),
                                             values(rs, "evidence_relation")]})
        exact, l_res, r_res, ambiguous = _unique_matches(ls, rs, _text_key, "IDENTICAL")
        for row in l_res:
            row["_canonical"] = canonical_record(row, config)
        for row in r_res:
            row["_canonical"] = canonical_record(row, config)
        canonical, l_res, r_res, ambiguous2 = _unique_matches(
            l_res, r_res, lambda r: r["_canonical"]["canonical_candidate_key"],
            "CANONICAL_CANDIDATE")
        l_lookup = {r["occurrence_id"]: r for r in ls}
        r_lookup = {r["occurrence_id"]: r for r in rs}
        for match in canonical:
            match["canonical_review"] = {
                "baseline": l_lookup[match["baseline_occurrence_id"]]["_canonical"],
                "second": r_lookup[match["second_occurrence_id"]]["_canonical"],
            }
        for match in exact + canonical:
            match["anchor"] = anchor
        for item in ambiguous + ambiguous2:
            item["anchor"] = anchor
        all_matches.extend(exact + canonical)
        all_ambiguous.extend(ambiguous + ambiguous2)
        unmatched_left.extend(l_res)
        unmatched_right.extend(r_res)

    # Cross-run occurrence correspondence is defined only by unambiguous semantic matches.
    left_lookup = {r["occurrence_id"]: r for r in left}
    right_lookup = {r["occurrence_id"]: r for r in right}
    structural_id_collisions = []
    for occurrence_id in sorted(set(left_lookup) & set(right_lookup)):
        first, second = left_lookup[occurrence_id], right_lookup[occurrence_id]
        if _text_key(first) != _text_key(second):
            structural_id_collisions.append({
                "occurrence_id": occurrence_id,
                "baseline_anchor": _anchor(first),
                "second_anchor": _anchor(second),
                "baseline_content_fingerprint": first.get("content_fingerprint"),
                "second_content_fingerprint": second.get("content_fingerprint"),
            })
    production_disagreements = []
    canonical_disagreements = []
    for i, first in enumerate(all_matches):
        for second in all_matches[i + 1:]:
            la, lb = left_lookup[first["baseline_occurrence_id"]], left_lookup[second["baseline_occurrence_id"]]
            ra, rb = right_lookup[first["second_occurrence_id"]], right_lookup[second["second_occurrence_id"]]
            left_same = bool(la.get("dedup_key")) and la.get("dedup_key") == lb.get("dedup_key")
            right_same = bool(ra.get("dedup_key")) and ra.get("dedup_key") == rb.get("dedup_key")
            if left_same != right_same:
                production_disagreements.append([first, second])
            lck_a = canonical_record(la, config)["canonical_candidate_key"]
            lck_b = canonical_record(lb, config)["canonical_candidate_key"]
            rck_a = canonical_record(ra, config)["canonical_candidate_key"]
            rck_b = canonical_record(rb, config)["canonical_candidate_key"]
            if (lck_a == lck_b) != (rck_a == rck_b):
                canonical_disagreements.append([first, second])

    report["axis_2_atomisation_and_sources"] = axis2
    report["axis_3_proposition_correspondence"] = {
        "unambiguous_matches": all_matches,
        "ambiguous_match_groups": all_ambiguous,
        "baseline_unmatched": [{"occurrence_id": r["occurrence_id"], "anchor": _anchor(r),
                                "proposition": r.get("proposition"), "context": r.get("context")}
                               for r in unmatched_left],
        "second_unmatched": [{"occurrence_id": r["occurrence_id"], "anchor": _anchor(r),
                              "proposition": r.get("proposition"), "context": r.get("context")}
                             for r in unmatched_right],
        "structural_id_content_collisions": structural_id_collisions,
        "ordinal_used_as_join_key": False,
    }
    report["axis_4_deduplication"] = {
        "comparison_universe": "unambiguous cross-run matches only",
        "measurement_status": (
            "MEASURED" if all_matches else "NOT_MEASURABLE_EMPTY_CORRESPONDENCE"),
        "production_partition_disagreements": production_disagreements,
        "canonical_candidate_partition_disagreements": canonical_disagreements,
        "production_key_modified": False,
    }
    report["review_required"] = bool(
        report["axis_1_anchor_selection"]["baseline_only"]
        or report["axis_1_anchor_selection"]["second_only"]
        or all_ambiguous or unmatched_left or unmatched_right
        or any(m["band"] == "CANONICAL_CANDIDATE" for m in all_matches)
        or structural_id_collisions or production_disagreements or canonical_disagreements)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("verify-baseline")
    build = sub.add_parser("build-blind-bundle")
    build.add_argument("destination", type=Path)
    verify = sub.add_parser("verify-blind-bundle")
    verify.add_argument("bundle", type=Path)
    verify.add_argument("--stage", choices=("pre", "authored", "reconciled"), default="pre")
    sub.add_parser("verify-canonicalisation")
    sub.add_parser("verify-receipt-projection")
    reconcile = sub.add_parser("verify-reconciliation")
    reconcile.add_argument("bundle", type=Path)
    build_reconciliation = sub.add_parser("reconcile-locator-receipts")
    build_reconciliation.add_argument("bundle", type=Path)
    compare = sub.add_parser("compare")
    compare.add_argument("baseline", type=Path)
    compare.add_argument("bundle", type=Path)
    args = parser.parse_args(argv)

    try:
        if args.command == "verify-baseline":
            errors = verify_phase2_baseline()
        elif args.command == "build-blind-bundle":
            build_blind_bundle(args.destination)
            print(f"BLIND BUNDLE READY: {args.destination}")
            return 0
        elif args.command == "verify-blind-bundle":
            errors = verify_phase2_baseline() + verify_blind_bundle(args.bundle, stage=args.stage)
        elif args.command == "verify-canonicalisation":
            errors = verify_canonicalisation(load_canonicalisation())
        elif args.command == "verify-receipt-projection":
            errors = verify_receipt_projection()
        elif args.command == "verify-reconciliation":
            errors = verify_reconciliation(args.bundle)
        elif args.command == "reconcile-locator-receipts":
            errors = verify_phase2_baseline()
            if errors:
                raise ValueError("baseline invalid: " + "; ".join(errors))
            reconcile_locator_receipts(args.bundle)
            print("RECONCILIATION WRITTEN AND VERIFIED")
            return 0
        else:
            errors = verify_phase2_baseline() + verify_measurement_attestations(args.bundle)
            if errors:
                print("MEASUREMENT VOID", file=sys.stderr)
                for error in errors:
                    print(f"- {error}", file=sys.stderr)
                return 2
            second = args.bundle / "output/second_derivation_reconciled.jsonl"
            report = compare_derivations(args.baseline, second, load_canonicalisation())
            print(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False))
            return 0
    except (FileNotFoundError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"PROTOCOL INVALID: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("PROTOCOL INVALID", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 2
    print("PROTOCOL VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
