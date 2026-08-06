#!/usr/bin/env python3
"""Validate, append and query LEGEND FULLTEXT_READ_RECEIPT JSONL ledgers.

The ledger is *append-only*, and that word is enforced, not asserted:

* every persisted event carries ``ledger_prev_hash``, the SHA-256 of the canonical
  serialization of the event before it, so rewriting or deleting any historical line
  breaks the chain of every line after it;
* the tail is anchored in the state manifest (event count + head digest), because a
  hash chain alone cannot detect *truncation* — lopping off the last events leaves a
  chain that is still internally consistent.

Together those two make silent history loss detectable. The residual, honest limit: an
editor who rewrites the ledger *and* the manifest anchor in the same breath is not caught
by arithmetic. That is a reviewable diff in a separate file, which is the point — the
integrity claim degrades to "visible in review", never to "invisible".
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

import corpus_firewall as firewall  # noqa: E402

try:
    import fcntl
except ImportError:  # pragma: no cover - POSIX is required for fail-closed append locking
    fcntl = None


DEPTHS = {
    "retrieved_not_read": 0,
    "queried_not_full_read": 1,
    "abstract_only": 2,
    "partial_fulltext_read": 3,
    "complete_fulltext_read": 4,
}
COVERAGE_KEYS = {
    "abstract",
    "introduction",
    "methods",
    "results",
    "figures",
    "tables",
    "discussion",
    "limitations",
    "supplementary",
}
# Optional because the nine required keys are already anchored in 27 persisted events and an
# append-only ledger cannot be retro-fitted. `references` is added as a ratchet instead: new
# reads may declare it, and the self-eval reports its absence rather than rewriting history.
# It exists because the reference list is where multi-hop expansion starts, and on 2026-07-26
# a read declared `complete_fulltext_read` without ever enumerating it — losing the
# neuron-specific GSK3B isoform (PMID 20067585) that qualified its own inferences.
OPTIONAL_COVERAGE_KEYS = {"references"}
# `captions_only` is not a synonym for `read`. On 2026-07-26 the single most valuable finding
# of a deep dive — a supplementary figure whose panels contradict its own caption — was
# invisible at caption level and visible only in the raster image. A coverage vocabulary that
# cannot tell those two apart cannot distinguish a read that would have caught it.
COVERAGE_STATES = {"read", "captions_only", "not_present", "unavailable", "not_read", "unknown_legacy"}
REREAD_REASONS = {
    "first_read",
    "new_version_or_supplement",
    "inadequate_prior_coverage",
    "contradiction_or_retraction",
    "new_question_outside_prior_coverage",
    "adversarial_reanalysis",
    "explicit_operator_request",
    "receipt_correction",
    "receipt_invalidation",
}
REQUIRED = {
    "event_id",
    "record_kind",
    "study_id",
    "event_at",
    "analysis_at",
    "workflow",
    "evidence_depth",
    "source_locator",
    "source_fingerprint",
    "coverage",
    "outputs",
    "evidence_basis",
    "prior_receipt",
    "reread_reason",
}
OPTIONAL_AUTHORED = {
    "source_kind", "analysis_time_precision", "invalidates_receipt", "invalidation_reason",
}
SOURCE_KINDS = {"fulltext_local", "fulltext_remote", "abstract", "metadata", "corpus_export"}
ANALYSIS_TIME_PRECISIONS = {"second", "minute", "date_only", "unknown"}
# Stamped by the ledger writer, never authored by hand: an author describes a reading
# event, the ledger describes its own history. Keeping it out of REQUIRED means a skill
# or agent emits exactly the receipt documented in the protocol, with no integrity
# bookkeeping to get wrong.
CHAIN_FIELD = "ledger_prev_hash"
LEDGER_MANAGED = {CHAIN_FIELD}
# A locator with a path separator that is neither a URL nor a bare DOI is a local artifact.
# 🔴 A bibliographic export is not a document. The refusal must live HERE, in the writer, not
# only in a regression test: a test that is not run blocks nothing, and `record` appends and
# re-anchors the chain before any suite has a chance to object. Reviewed 2026-08-05, where a
# hand-built receipt naming `files/corpus/*.jsonl` as the document it read passed
# `validate_receipt()` with no complaint at all.
#
# Reviewed again 2026-08-06: recognising a corpus by NAME is a guard against accidents, not
# against the failure mode. `cp files/corpus/wwox.jsonl files/fulltext/paper.jsonl` defeats it
# completely, and nothing about the copy is unusual — it is what someone does when a check
# refuses them. So the definition now lives in `corpus_firewall`, which also asks what the
# file on disk actually IS. A rename does not turn abstracts into a paper.
CORPUS_ARTEFACT = firewall.CORPUS_ARTEFACT
ABSTRACT_ONLY_LOCATOR = re.compile(
    r"(?:https?://)?(?:www\.)?pubmed\.ncbi\.nlm\.nih\.gov/|"
    r"(?:https?://)?eutils\.ncbi\.nlm\.nih\.gov/entrez/eutils/|"
    r"(?:^|/)abstract(?:[/?#]|$)",
    re.IGNORECASE,
)

URL_LOCATOR = re.compile(r"^[a-z][a-z0-9+.-]*://", re.I)
DOI_LOCATOR = re.compile(r"^(?:https?://doi\.org/)?10\.\d{4,9}/\S+$", re.I)
LOCAL_ARTIFACT_SUFFIXES = {
    ".pdf", ".html", ".htm", ".txt", ".xml", ".json", ".md", ".docx"
}


def normalise_doi(value: Optional[str]) -> str:
    return (value or "").strip().lower().removeprefix("https://doi.org/").rstrip(".")


def default_ledger_path(root: Path, disease: str) -> Path:
    return root / "disease-models" / disease / "registries" / "fulltext_read_receipts.jsonl"


def canonical_line(receipt: dict[str, Any]) -> str:
    """The exact byte sequence a receipt occupies on disk."""
    return json.dumps(receipt, ensure_ascii=False, sort_keys=True)


def receipt_digest(receipt: dict[str, Any]) -> str:
    """SHA-256 over the whole persisted record, ``ledger_prev_hash`` included.

    Including the chain field is what makes the chain a chain: tampering with one link
    invalidates every link downstream of it, not merely the record that was edited.
    """
    return hashlib.sha256(canonical_line(receipt).encode("utf-8")).hexdigest()


def is_local_artifact(locator: str) -> bool:
    candidate = (locator or "").strip()
    if not candidate or DOI_LOCATOR.match(candidate):
        return False
    if candidate.lower().startswith("file://"):
        return True
    if URL_LOCATOR.match(candidate):
        return False
    return bool(
        "/" in candidate
        or "\\" in candidate
        or Path(candidate).suffix.lower() in LOCAL_ARTIFACT_SUFFIXES
    )


def ledger_head(receipts: list[dict[str, Any]]) -> Optional[str]:
    return receipt_digest(receipts[-1]) if receipts else None


def validate_ledger_chain(receipts: list[dict[str, Any]]) -> list[str]:
    """Verify that persisted history has only ever been appended to."""
    errors: list[str] = []
    expected: Optional[str] = None
    for number, receipt in enumerate(receipts, 1):
        if CHAIN_FIELD not in receipt:
            errors.append(f"line {number}: missing {CHAIN_FIELD}: the ledger is not chained")
        elif receipt[CHAIN_FIELD] != expected:
            errors.append(
                f"line {number}: broken hash chain: earlier history was rewritten or removed"
            )
        expected = receipt_digest(receipt)
    return errors


def _parse_lines(text: str, *, require_chain: bool = True) -> list[dict[str, Any]]:
    receipts: list[dict[str, Any]] = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"line {number}: invalid JSON: {error.msg}") from error
        if not isinstance(value, dict):
            raise ValueError(f"line {number}: receipt must be a JSON object")
        receipts.append(value)
    # Chain first, deliberately. Any in-place edit both breaks the chain *and* tends to
    # produce a receipt that fails field validation, and the two diagnoses are not equally
    # serious: "this record is malformed" is a defect, "the recorded past changed" is a
    # state you cannot reason from. Reporting the milder one first would let a history
    # rewrite be mistaken for a formatting slip and repaired in place.
    if require_chain:
        chain_errors = validate_ledger_chain(receipts)
        if chain_errors:
            raise ValueError("; ".join(chain_errors))
    for number, value in enumerate(receipts, 1):
        errors = validate_receipt(value)
        if errors:
            raise ValueError(f"line {number}: {'; '.join(errors)}")
    sequence_errors = validate_ledger_sequence(receipts)
    if sequence_errors:
        raise ValueError("; ".join(sequence_errors))
    return receipts


def load_ledger(
    path: Path, *, allow_missing: bool = False, require_chain: bool = True
) -> list[dict[str, Any]]:
    if not path.exists():
        if allow_missing:
            return []
        raise ValueError(f"ledger does not exist: {path}")
    return _parse_lines(path.read_text(encoding="utf-8"), require_chain=require_chain)


def _valid_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    candidate = value.strip()
    if candidate.endswith("Z"):
        candidate = candidate[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(candidate)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _parse_datetime(value: str) -> datetime:
    candidate = value.strip()
    if candidate.endswith("Z"):
        candidate = candidate[:-1] + "+00:00"
    return datetime.fromisoformat(candidate)


def validate_new_receipt(receipt: Any) -> list[str]:
    """Rules applied to a receipt being WRITTEN, never to one already in the ledger.

    History is grandfathered on purpose. `validate_receipt` runs over every line whenever the
    ledger is loaded, so tightening it retroactively would not correct the past — it would
    halt the system on records that can no longer be edited. Same shape as the two ratchets in
    the state manifest: the backlog stays visible, and only new work meets the tighter rule.

    New records carry an explicit source kind and timestamp precision. Exact-midnight string
    matching was intentionally removed: it rejected a real midnight, missed equivalent
    offsets and rewarded changing a fabricated value by one second. The authoritative writer
    stamps ``event_at`` itself; ``analysis_at`` keeps the worker's declared precision.
    """
    if not isinstance(receipt, dict):
        return []
    errors: list[str] = []
    if receipt.get("record_kind") == "contemporaneous_receipt":
        source_kind = receipt.get("source_kind")
        if source_kind not in SOURCE_KINDS:
            errors.append(f"source_kind is required for new receipts: one of {sorted(SOURCE_KINDS)}")
        precision = receipt.get("analysis_time_precision")
        if precision not in ANALYSIS_TIME_PRECISIONS:
            errors.append(
                "analysis_time_precision is required for new contemporaneous receipts: "
                f"one of {sorted(ANALYSIS_TIME_PRECISIONS)}")
        if receipt.get("evidence_depth") in {"partial_fulltext_read", "complete_fulltext_read"}:
            if source_kind not in {"fulltext_local", "fulltext_remote"}:
                errors.append(
                    "partial/complete full-text evidence requires a fulltext source_kind")
            if ABSTRACT_ONLY_LOCATOR.search(str(receipt.get("source_locator") or "")):
                errors.append(
                    "an abstract or PubMed record URL cannot support partial/complete "
                    "full-text evidence")
    return errors


def validate_receipt(receipt: Any) -> list[str]:
    if not isinstance(receipt, dict):
        return ["receipt must be a JSON object"]
    errors: list[str] = []
    depth = receipt.get("evidence_depth")
    reading = depth in {"partial_fulltext_read", "complete_fulltext_read"}
    for field in ("source_locator", "workflow"):
        objection = firewall.corpus_objection(str(receipt.get(field) or "")) if reading else ""
        if objection:
            errors.append(
                f"{field} {objection}. An export of abstracts is not a full-text document — "
                "see CLAUDE.md rule 8. Name the paper's own artefact, or record the depth "
                "honestly as `abstract_only`.")
    for item in receipt.get("evidence_basis") or []:
        if reading and firewall.corpus_objection(str(item)):
            errors.append(
                "evidence_basis cites a bibliographic corpus as the basis of a reading")
            break
    missing = REQUIRED - set(receipt)
    extra = set(receipt) - REQUIRED - OPTIONAL_AUTHORED - LEDGER_MANAGED
    chain = receipt.get(CHAIN_FIELD)
    if chain is not None and not re.fullmatch(r"[a-f0-9]{64}", str(chain)):
        errors.append(f"{CHAIN_FIELD} must be lowercase SHA-256 or null")
    if missing:
        errors.append(f"missing fields: {sorted(missing)}")
    if extra:
        errors.append(f"unknown fields: {sorted(extra)}")
    if missing:
        return errors

    event_id = receipt["event_id"]
    if not isinstance(event_id, str) or not re.fullmatch(
        r"FTR-[0-9]{8}-[A-Za-z0-9._-]+-[0-9]{2}", event_id
    ):
        errors.append("invalid event_id")
    study = receipt["study_id"]
    if not isinstance(study, dict):
        errors.append("study_id must be an object")
    elif set(study) - {"pmid", "doi"}:
        errors.append("study_id contains unknown fields")
    elif not (study.get("pmid") or study.get("doi")):
        errors.append("study_id needs PMID or DOI")
    else:
        if study.get("pmid") and not re.fullmatch(r"[0-9]{1,8}", str(study["pmid"])):
            errors.append("invalid PMID")
        doi = normalise_doi(study.get("doi"))
        if study.get("doi") and not re.fullmatch(r"10\.\d{4,9}/\S+", doi):
            errors.append("invalid DOI")
    if not _valid_datetime(receipt["event_at"]):
        errors.append("invalid event_at: timezone-aware ISO-8601 required")
    if receipt["evidence_depth"] not in DEPTHS:
        errors.append("invalid evidence_depth")
    source_kind = receipt.get("source_kind")
    if source_kind is not None and source_kind not in SOURCE_KINDS:
        errors.append("invalid source_kind")
    precision = receipt.get("analysis_time_precision")
    if precision is not None and precision not in ANALYSIS_TIME_PRECISIONS:
        errors.append("invalid analysis_time_precision")
    if receipt["record_kind"] not in {
        "contemporaneous_receipt", "legacy_reconstruction", "receipt_invalidation",
    }:
        errors.append("invalid record_kind")
    elif receipt["record_kind"] == "contemporaneous_receipt" and receipt["analysis_at"] is None:
        errors.append("contemporaneous receipt requires analysis_at")
    elif receipt["record_kind"] == "legacy_reconstruction" and not receipt["evidence_basis"]:
        errors.append("legacy reconstruction requires evidence_basis")
    elif receipt["record_kind"] == "receipt_invalidation":
        if receipt.get("reread_reason") != "receipt_invalidation":
            errors.append("receipt_invalidation record requires matching reread_reason")
        if receipt.get("invalidates_receipt") != receipt.get("prior_receipt"):
            errors.append("receipt_invalidation must invalidate its direct prior_receipt")
        reason = receipt.get("invalidation_reason")
        if not isinstance(reason, str) or len(reason.strip()) < 40:
            errors.append("receipt_invalidation requires a substantive invalidation_reason")
    if receipt["analysis_at"] is not None and not _valid_datetime(receipt["analysis_at"]):
        errors.append("invalid analysis_at: timezone-aware ISO-8601 required")
    elif (
        receipt["analysis_at"] is not None
        and _valid_datetime(receipt["event_at"])
        and _parse_datetime(receipt["analysis_at"]) > _parse_datetime(receipt["event_at"])
    ):
        errors.append("analysis_at cannot be later than event_at")
    if not isinstance(receipt["workflow"], str) or not receipt["workflow"].strip():
        errors.append("workflow must be non-empty")
    if not isinstance(receipt["source_locator"], str) or not receipt["source_locator"].strip():
        errors.append("source_locator must be non-empty")
    coverage = receipt["coverage"]
    if not isinstance(coverage, dict) or not (
        COVERAGE_KEYS <= set(coverage) <= COVERAGE_KEYS | OPTIONAL_COVERAGE_KEYS
    ):
        errors.append(
            "coverage must contain the nine required sections, plus optionally "
            + ", ".join(sorted(OPTIONAL_COVERAGE_KEYS))
        )
    elif not set(coverage.values()) <= COVERAGE_STATES:
        errors.append("invalid coverage state")
    else:
        values = set(coverage.values())
        if ("unknown_legacy" in values
                and receipt["record_kind"] not in {"legacy_reconstruction",
                                                    "receipt_invalidation"}):
            errors.append("unknown_legacy coverage is allowed only for legacy history")
        if receipt["evidence_depth"] == "complete_fulltext_read":
            if {"not_read", "unknown_legacy"} & values:
                errors.append("complete_fulltext_read cannot leave a section not_read or unknown_legacy")
            if "captions_only" in values:
                errors.append(
                    "complete_fulltext_read cannot rest on captions_only — a caption is "
                    "authored prose, the figure is the data (see D-14). Declare "
                    "partial_fulltext_read, or inspect the images"
                )
            if "read" not in values:
                errors.append("complete_fulltext_read requires at least one read section")
        if (
            receipt["evidence_depth"] == "partial_fulltext_read"
            and receipt["record_kind"] == "contemporaneous_receipt"
            and "read" not in values
        ):
            errors.append("contemporaneous partial_fulltext_read requires at least one read section")
    if receipt["reread_reason"] not in REREAD_REASONS:
        errors.append("invalid reread_reason")
    elif receipt["reread_reason"] == "first_read" and receipt["prior_receipt"] is not None:
        errors.append("first_read cannot name prior_receipt")
    elif receipt["reread_reason"] != "first_read" and receipt["prior_receipt"] is None:
        errors.append("continued or repeated work requires prior_receipt")
    if not receipt["outputs"] or not isinstance(receipt["outputs"], list) or not all(
        isinstance(item, str) and item.strip() for item in receipt["outputs"]
    ):
        errors.append("outputs must be a non-empty list of non-empty strings")
    if not receipt["evidence_basis"] or not isinstance(receipt["evidence_basis"], list) or not all(
        isinstance(item, str) and item.strip() for item in receipt["evidence_basis"]
    ):
        errors.append("evidence_basis must be a non-empty list of non-empty strings")
    fingerprint = receipt["source_fingerprint"]
    if fingerprint is not None and not re.fullmatch(r"[a-f0-9]{64}", str(fingerprint)):
        errors.append("source_fingerprint must be lowercase SHA-256 or null")
    # A receipt naming a local file claims "I read *this* artifact". Without a digest that
    # claim is unfalsifiable: the file can be replaced, truncated or regenerated and the
    # receipt keeps vouching for it. Remote locators legitimately have nothing to hash, and
    # a legacy reconstruction by definition cannot re-hash what it did not witness.
    if (
        receipt["record_kind"] == "contemporaneous_receipt"
        and fingerprint is None
        and isinstance(receipt["source_locator"], str)
        and is_local_artifact(receipt["source_locator"])
    ):
        errors.append(
            "contemporaneous receipt over a local artifact requires source_fingerprint"
        )
    prior = receipt["prior_receipt"]
    if prior is not None and (
        not isinstance(prior, str)
        or not re.fullmatch(r"FTR-[0-9]{8}-[A-Za-z0-9._-]+-[0-9]{2}", prior)
    ):
        errors.append("invalid prior_receipt")
    return errors


def _authoritative_context(path: Path) -> Optional[tuple[Path, str]]:
    """Infer the workspace and disease only for the canonical receipt sink shape."""
    resolved = path.resolve()
    parts = resolved.parts
    try:
        position = len(parts) - 4
        if (
            position >= 0
            and parts[position] == "disease-models"
            and parts[position + 2] == "registries"
            and parts[position + 3] == "fulltext_read_receipts.jsonl"
        ):
            root = Path(*parts[:position])
            if not root.is_absolute():
                root = Path(resolved.anchor, *parts[1:position])
            return root, parts[position + 1]
    except (IndexError, ValueError):
        pass
    return None


def _strict_local_source(receipt: dict[str, Any], root: Path) -> list[str]:
    """Bind a new complete read to a real local full-text artifact at write time."""
    if receipt.get("record_kind") != "contemporaneous_receipt":
        return []
    if receipt.get("evidence_depth") != "complete_fulltext_read":
        return []
    if receipt.get("reread_reason") == "receipt_correction":
        return []
    errors: list[str] = []
    if receipt.get("source_kind") != "fulltext_local":
        errors.append(
            "new complete reads require source_kind `fulltext_local`; snapshot a lawful "
            "full-text PDF/XML/HTML before recording")
        return errors
    locator = str(receipt.get("source_locator") or "")
    if not locator or locator != locator.strip() or " (" in locator:
        errors.append(
            "source_locator for a new complete read must be the exact repository-relative "
            "artifact path, without annotations")
        return errors
    candidate = (root / locator).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        errors.append("source_locator escapes the workspace")
        return errors
    if not candidate.is_file():
        errors.append(f"source full-text artifact does not exist: {locator}")
        return errors
    expected = str(receipt.get("source_fingerprint") or "")
    actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
    if expected != actual:
        errors.append("source_fingerprint does not match the full-text artifact")
    return errors


def same_study(receipt: dict[str, Any], pmid: str, doi: str) -> bool:
    study = receipt["study_id"]
    return bool(
        (pmid and str(study.get("pmid") or "") == pmid)
        or (doi and normalise_doi(study.get("doi")) == doi)
    )


def study_identity_conflict(first: dict[str, Any], second: dict[str, Any]) -> bool:
    first_study = first["study_id"]
    second_study = second["study_id"]
    first_pmid = str(first_study.get("pmid") or "")
    second_pmid = str(second_study.get("pmid") or "")
    first_doi = normalise_doi(first_study.get("doi"))
    second_doi = normalise_doi(second_study.get("doi"))
    shares_identifier = bool(
        (first_pmid and first_pmid == second_pmid)
        or (first_doi and first_doi == second_doi)
    )
    contradicts_identifier = bool(
        (first_pmid and second_pmid and first_pmid != second_pmid)
        or (first_doi and second_doi and first_doi != second_doi)
    )
    return shares_identifier and contradicts_identifier


def validate_ledger_sequence(receipts: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen: list[dict[str, Any]] = []
    event_ids: set[str] = set()
    for number, receipt in enumerate(receipts, 1):
        event_id = receipt["event_id"]
        if event_id in event_ids:
            errors.append(f"line {number}: duplicate event_id: {event_id}")
            continue
        event_ids.add(event_id)
        pmid = str(receipt["study_id"].get("pmid") or "")
        doi = normalise_doi(receipt["study_id"].get("doi"))
        for earlier in seen:
            if study_identity_conflict(earlier, receipt):
                errors.append(f"line {number}: conflicting identifiers for the same study")
        prior_for_study = [item for item in seen if same_study(item, pmid, doi)]
        prior_id = receipt["prior_receipt"]
        if prior_for_study and prior_id != prior_for_study[-1]["event_id"]:
            errors.append(
                f"line {number}: repeated study must link its latest prior_receipt"
            )
        if prior_id is not None:
            matching_prior = [item for item in prior_for_study if item["event_id"] == prior_id]
            if not matching_prior:
                errors.append(f"line {number}: prior_receipt is not an earlier event for this study")
            elif receipt["reread_reason"] in {"receipt_correction", "receipt_invalidation"}:
                prior = matching_prior[0]
                immutable_fields = (
                    "study_id", "analysis_at", "evidence_depth",
                    "source_locator", "source_fingerprint", "coverage",
                )
                changed = [field for field in immutable_fields if receipt[field] != prior[field]]
                if changed:
                    errors.append(
                        f"line {number}: {receipt['reread_reason']} changed substantive fields: "
                        + ", ".join(changed)
                    )
                if (receipt["reread_reason"] == "receipt_correction"
                        and receipt["record_kind"] != prior["record_kind"]):
                    errors.append(
                        f"line {number}: receipt_correction changed substantive fields: "
                        "record_kind")
        seen.append(receipt)
    return errors


def invalidated_event_ids(events: list[dict[str, Any]]) -> set[str]:
    """The `event_id`s a `receipt_invalidation` has withdrawn.

    An invalidation names ONE event — `validate_receipt` refuses it otherwise. Every consumer
    of the ledger must subtract exactly that event and nothing else.
    """
    return {str(event["invalidates_receipt"]) for event in events
            if event.get("record_kind") == "receipt_invalidation"
            and event.get("invalidates_receipt")}


def active_receipts(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Reading events that still stand: neither invalidations nor invalidated.

    Exported because "which receipts still count" was being answered independently in three
    places, and one of them answered it wrong.
    """
    withdrawn = invalidated_event_ids(events)
    return [event for event in events
            if event.get("record_kind") != "receipt_invalidation"
            and str(event.get("event_id")) not in withdrawn]


def receipt_depth_index(path: Path) -> dict[str, dict[str, Any]]:
    """Deepest surviving receipt per identifier.

    🔴 This used to drop the whole *study key* when it met an invalidation:
    `index.pop(f"pmid:{pmid}")`. An invalidation names one event, so withdrawing a July
    `partial_fulltext_read` also erased a June `complete_fulltext_read` for the same paper —
    a correction aimed at one receipt silently deleted the reading history around it. In a
    system where a false negative is a compounding loss, that is the worst direction to fail:
    a paper genuinely read in full reappears as unread, re-enters the debt, and gets read
    again. Reproduced 2026-08-06 with two receipts and one invalidation; the index came back
    empty. Only the named event is subtracted now.
    """
    index: dict[str, dict[str, Any]] = {}
    for receipt in active_receipts(load_ledger(path)):
        study = receipt["study_id"]
        keys = []
        if study.get("pmid"):
            keys.append(f"pmid:{study['pmid']}")
        if study.get("doi"):
            keys.append(f"doi:{normalise_doi(study['doi'])}")
        for key in keys:
            current = index.get(key)
            if current is None or DEPTHS[receipt["evidence_depth"]] >= DEPTHS[current["evidence_depth"]]:
                index[key] = receipt
    return index


def append_receipt(
    path: Path, receipt: dict[str, Any], *, manifest: Optional[Path] = None
) -> dict[str, Any]:
    """Append one event under an exclusive lock and return the persisted record.

    The whole existing history is re-read and chain-verified *inside* the lock, so an
    append onto a ledger whose past was rewritten fails closed instead of extending a
    corrupted history with a fresh, honest-looking link.

    Passing ``manifest`` also checks the tail anchor first, and that is not optional
    ceremony. A chain binds each event to its predecessor, which leaves the **last** event
    bound by nothing: edit it, append on top, let the append re-anchor, and the tamper is
    laundered into verified history forever. Checking the anchor before extending is what
    makes the head as protected as the body.
    """
    if fcntl is None:
        raise RuntimeError("POSIX file locking unavailable; refusing unlocked receipt append")
    record = {key: value for key, value in receipt.items() if key not in LEDGER_MANAGED}
    authoritative = _authoritative_context(path)
    if authoritative is not None:
        root, disease = authoritative
        expected_manifest = default_manifest_path(root).resolve()
        if manifest is None:
            manifest = expected_manifest
        elif manifest.resolve() != expected_manifest:
            raise ValueError(
                "the authoritative receipt sink must use its repository state manifest")
        # `event_at` is persistence time, not a value a worker guesses. `analysis_at` remains
        # the worker's statement and carries its own explicit precision.
        if record.get("record_kind") == "contemporaneous_receipt":
            record["event_at"] = datetime.now(timezone.utc).isoformat(
                timespec="seconds").replace("+00:00", "Z")
        require_work_manifest(record, root, disease, strict=True)
        strict_errors = _strict_local_source(record, root)
    else:
        strict_errors = []
    errors = validate_receipt(record) + validate_new_receipt(record) + strict_errors
    if errors:
        raise ValueError("; ".join(errors))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            handle.seek(0)
            existing = _parse_lines(handle.read())
            if manifest is not None:
                if not manifest.is_file():
                    raise ValueError(f"state manifest does not exist: {manifest}")
                manifest_text = manifest.read_text(encoding="utf-8")
                anchor_errors = validate_state_anchor(manifest_text, existing)
                if anchor_errors:
                    raise ValueError(
                        "refusing to append onto unverified history: "
                        + "; ".join(anchor_errors)
                    )
            record[CHAIN_FIELD] = ledger_head(existing)
            sequence_errors = validate_ledger_sequence(existing + [record])
            if sequence_errors:
                raise ValueError("; ".join(sequence_errors))
            handle.seek(0, os.SEEK_END)
            original_size = handle.tell()
            handle.write(canonical_line(record) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            if manifest is not None:
                try:
                    if not write_state_anchor(manifest, existing + [record]):
                        raise ValueError(
                            f"{manifest} declares no unique full-text ledger anchor"
                        )
                except Exception:
                    handle.seek(original_size)
                    handle.truncate()
                    handle.flush()
                    os.fsync(handle.fileno())
                    raise
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    return record


ANCHOR_EVENTS = re.compile(r"(?m)^(fulltext_ledger_events:\s*)(\S+)\s*$")
ANCHOR_HEAD = re.compile(r"(?m)^(fulltext_ledger_head:\s*)(\S+)\s*$")


def read_state_anchor(manifest_text: str) -> Optional[tuple[int, Optional[str]]]:
    """Extract the declared (event count, head digest) tail anchor, if the manifest has one."""
    events = list(ANCHOR_EVENTS.finditer(manifest_text))
    heads = list(ANCHOR_HEAD.finditer(manifest_text))
    if len(events) != 1 or len(heads) != 1:
        return None
    try:
        count = int(events[0].group(2))
    except ValueError:
        return None
    declared = heads[0].group(2).strip().strip('"')
    return count, (None if declared in {"null", "none", ""} else declared)


def validate_state_anchor(
    manifest_text: str, receipts: list[dict[str, Any]]
) -> list[str]:
    """A hash chain proves nothing about events that were removed from the *end*.

    Truncating the tail leaves the surviving prefix perfectly self-consistent. Only an
    external anchor — held in the one file LEGEND allows to be written outside a
    BATCH_COMMIT — makes that loss visible.
    """
    event_fields = list(ANCHOR_EVENTS.finditer(manifest_text))
    head_fields = list(ANCHOR_HEAD.finditer(manifest_text))
    if len(event_fields) != 1 or len(head_fields) != 1:
        return [
            "state manifest must declare exactly one fulltext_ledger_events and "
            "one fulltext_ledger_head field"
        ]
    anchor = read_state_anchor(manifest_text)
    if anchor is None:
        return ["state manifest fulltext ledger tail anchor is malformed"]
    count, head = anchor
    errors: list[str] = []
    if count != len(receipts):
        errors.append(
            f"ledger holds {len(receipts)} event(s); the state manifest anchors {count}: "
            "events were truncated, or the anchor was not updated after an append"
        )
    actual = ledger_head(receipts)
    if head != actual:
        errors.append(
            f"ledger head digest {actual} does not match the anchored {head}"
        )
    return errors


def write_state_anchor(manifest_path: Path, receipts: list[dict[str, Any]]) -> bool:
    """Atomically re-anchor the manifest; refuse missing or ambiguous anchor fields."""
    text = manifest_path.read_text(encoding="utf-8")
    if len(ANCHOR_EVENTS.findall(text)) != 1 or len(ANCHOR_HEAD.findall(text)) != 1:
        return False
    head = ledger_head(receipts)
    text = ANCHOR_EVENTS.sub(lambda m: f"{m.group(1)}{len(receipts)}", text, count=1)
    text = ANCHOR_HEAD.sub(lambda m: f"{m.group(1)}{head or 'null'}", text, count=1)
    mode = stat.S_IMODE(manifest_path.stat().st_mode)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{manifest_path.name}.", dir=manifest_path.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_name, mode)
        os.replace(temporary_name, manifest_path)
        directory = os.open(manifest_path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except Exception:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise
    return True


def default_manifest_path(root: Path) -> Path:
    return root / "framework" / "state" / "state_manifest_current.md"


def require_work_manifest(
    receipt: Any, root: Path, disease: str, *, strict: bool = True
) -> None:
    """Refuse the strongest claim until the work behind it exists.

    `complete_fulltext_read` is the only depth that clears reading debt, so it is the only
    one worth over-claiming. Verifying it after the fact cannot help: by then the receipt is
    chained and immutable. Gating it here makes the claim unavailable rather than merely
    auditable — the difference between reducing the gap and closing it.

    Deliberately narrow: retrieval, partial reads and legacy reconstructions are untouched.
    New complete reads fail closed when the validator or any required artifact is absent.
    """
    if not isinstance(receipt, dict):
        return
    if receipt.get("evidence_depth") != "complete_fulltext_read":
        return
    if receipt.get("record_kind") != "contemporaneous_receipt":
        return
    if receipt.get("reread_reason") == "receipt_correction":
        return
    pmid = (receipt.get("study_id") or {}).get("pmid")
    if not pmid:
        return
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    try:
        import deepdive_manifest
    except ImportError as exc:  # pragma: no cover - validator absent
        raise ValueError(
            "complete_fulltext_read refused — deepdive_manifest validator unavailable"
        ) from exc
    errors, incomplete = deepdive_manifest.load_and_validate(
        root.resolve(), disease, str(pmid),
        verify_artifacts=strict,
        require_current_schema=strict,
    )
    for item in incomplete:
        print(f"  [DECLARED GAP] {item}", file=sys.stderr)
    if strict and incomplete:
        errors.extend(f"declared gap: {item}" for item in incomplete)

    manifest_file = deepdive_manifest.manifest_path(root.resolve(), disease, str(pmid))
    if not errors and strict:
        try:
            work = json.loads(manifest_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"cannot read work manifest for source binding: {exc}")
        else:
            source = str(receipt.get("source_locator") or "")
            digest = str(receipt.get("source_fingerprint") or "")
            declared = {
                str(item.get("path")): str(item.get("sha256"))
                for item in work.get("source_artifacts", [])
                if isinstance(item, dict)
            }
            if declared.get(source) != digest:
                errors.append(
                    "receipt source_locator/source_fingerprint is not the same fingerprinted "
                    "article artifact declared by the work manifest")
    if errors:
        raise ValueError(
            "complete_fulltext_read refused — "
            + "; ".join(errors)
            + ". Record the depth you can evidence, or complete the manifest."
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="status options: --pmid/--doi; record option: --receipt",
    )
    parser.add_argument("--ledger", default="", help="append-only receipt JSONL; defaults to the disease workspace sink")
    parser.add_argument("--root", default=".", help="repository root used for the default sink")
    parser.add_argument("--disease", default="wwox", help="disease model used for the default sink")
    parser.add_argument(
        "--manifest",
        default="",
        help="state manifest holding the ledger tail anchor; defaults to the repository manifest",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="parse and chain-verify the ledger")
    subparsers.add_parser(
        "verify", help="validate, then check the tail anchor in the state manifest"
    )
    subparsers.add_parser(
        "anchor", help="re-anchor the state manifest to the current ledger tail"
    )
    status = subparsers.add_parser("status")
    status.add_argument("--pmid", default="")
    status.add_argument("--doi", default="")
    record = subparsers.add_parser("record")
    record.add_argument("--receipt", required=True, help="one receipt JSON file")
    args = parser.parse_args()
    ledger = (
        Path(args.ledger)
        if args.ledger
        else default_ledger_path(Path(args.root), args.disease)
    )
    manifest = Path(args.manifest) if args.manifest else default_manifest_path(Path(args.root))

    try:
        if args.command == "validate":
            receipts = load_ledger(ledger)
            print(f"OK: {len(receipts)} valid receipt(s)")
            return 0
        if args.command == "verify":
            receipts = load_ledger(ledger)
            if not manifest.is_file():
                raise ValueError(f"state manifest does not exist: {manifest}")
            anchor_errors = validate_state_anchor(
                manifest.read_text(encoding="utf-8"), receipts
            )
            if anchor_errors:
                raise ValueError("; ".join(anchor_errors))
            print(f"OK: {len(receipts)} chained receipt(s), tail anchored in {manifest}")
            return 0
        if args.command == "anchor":
            receipts = load_ledger(ledger)
            if not write_state_anchor(manifest, receipts):
                raise ValueError(
                    f"{manifest} declares no fulltext_ledger_events/fulltext_ledger_head anchor"
                )
            print(f"ANCHORED: {len(receipts)} event(s), head {ledger_head(receipts)}")
            return 0
        if args.command == "record":
            receipt = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
            persisted = append_receipt(ledger, receipt, manifest=manifest)
            print(f"RECORDED: {persisted['event_id']}")
            return 0

        pmid = args.pmid.strip()
        doi = normalise_doi(args.doi)
        if not pmid and not doi:
            raise ValueError("status needs --pmid or --doi")
        matches = [item for item in load_ledger(ledger) if same_study(item, pmid, doi)]
        matches.sort(key=lambda item: DEPTHS[item["evidence_depth"]], reverse=True)
        print(json.dumps(matches, indent=2, ensure_ascii=False))
        return 0 if any(item["evidence_depth"] == "complete_fulltext_read" for item in matches) else 1
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
