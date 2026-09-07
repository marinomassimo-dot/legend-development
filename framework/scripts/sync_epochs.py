#!/usr/bin/env python3
"""SYNC_EPOCH ledger — when the shared checkout moved, and when it deliberately did not.

## Why this exists

Several actors work in their own worktrees against one shared checkout. Realigning that
checkout is what makes a landed state a *dependency* other actors must consume, so the
decision to move it — and the decision NOT to move it — is operational state, not chatter.
Announced in a message it survives until the session ends; recorded here it survives the
session, which is the whole difference.

## What it is not

Not a canonical scientific file. It records who moved a checkout and why. It never touches
the working model, the four current files, branches or the checkout itself. `record` writes
exactly two paths: this ledger, and the tail anchor in the state manifest.

## Reuse, not reinvention

The chain, the digest, the tail anchor and the atomic anchor write all come from
`fulltext_receipts`. `PATTERN_ALREADY_SOLVED_GATE`: an append-only ledger whose truncation is
invisible without an external anchor is a solved problem in this repository, and solving it a
second time is how two implementations of one idea drift apart — the exact defect that cost a
morning on 2026-08-11.

🔴 That is reuse of a MECHANISM and not an echo, and the distinction matters because they look
alike. An echo is a checker importing the predicate of the thing it audits, so a defect in the
predicate is invisible to the check built to confirm it. Here nothing audits anything: two
ledgers share one hash chain the way two files share one filesystem. Should this ledger ever
need to *corroborate* the receipt ledger, that shared import becomes an echo and must be
broken.

## Separation of decision from measurement

🔴 A measurement reported by another actor does not become Plan's measurement. Every entry in
`observations` names `measured_by`, when, in which workspace, at which commit, what was
measured and what came back. On 2026-08-11 the cleanliness of the shared checkout was measured
by the orchestrator with `git status`; Plan could not measure it at all, because the harness
refuses even a read-only `git -C` into another checkout. Recording it as Plan's would have been
a small, invisible lie of the kind this repository spent that day cataloguing.

## Usage

    sync_epochs.py record --event event.json
    sync_epochs.py verify
    sync_epochs.py status
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_root import RootError, repo_root  # noqa: E402
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fulltext_receipts as chain  # noqa: E402

SCHEMA_VERSION = 1
ANCHOR_PREFIX = "sync_epoch_ledger"
ANCHOR_EVENTS, ANCHOR_HEAD = chain.anchor_patterns(ANCHOR_PREFIX)

LEDGER_RELATIVE = "framework/state/sync_epochs.jsonl"
MANIFEST_RELATIVE = "framework/state/state_manifest_current.md"

ACTIONS = {"MOVE", "NO_MOVE"}
REASONS = {
    "merge_dependency",
    "batch_commit_open",
    "batch_commit_close",
    "urgent_gate",
    "operator_request",
    "other_declared",
}
RECORD_KINDS = {"contemporaneous", "contemporaneous_reconstruction"}

REQUIRED = (
    "schema_version", "event_id", "recorded_at", "record_kind", "workspace", "action",
    "previous_commit", "current_commit", "branch_or_detached", "reason",
    "dependency_commit", "landed_artifacts", "actors_required_to_consume",
    "invalidates_active_work", "required_action_by_readers", "validation_status",
    "announced_by", "observations",
)
OBSERVATION_FIELDS = (
    "measured_by", "measured_at", "workspace", "branch_or_detached", "commit",
    "measurement", "result",
)
COMMIT_LIKE = {"unknown", "none", "null"}


def default_ledger(root: Path) -> Path:
    return root / LEDGER_RELATIVE


def default_manifest(root: Path) -> Path:
    return root / MANIFEST_RELATIVE


def _is_commitish(value: Any) -> bool:
    text = str(value or "").strip()
    if text.lower() in COMMIT_LIKE:
        return True
    return len(text) >= 7 and all(character in "0123456789abcdef" for character in text.lower())


def validate_event(event: Any) -> list[str]:
    """Every way an event can be wrong, before anything is written."""
    errors: list[str] = []
    if not isinstance(event, dict):
        return ["event must be a JSON object"]

    for field in REQUIRED:
        if field not in event:
            errors.append(f"missing required field: {field}")
    if errors:
        return errors

    if event["schema_version"] != SCHEMA_VERSION:
        errors.append(f"schema_version: this writer records version {SCHEMA_VERSION}")
    if event["record_kind"] not in RECORD_KINDS:
        errors.append(f"record_kind: must be one of {sorted(RECORD_KINDS)}")
    if event["record_kind"] == "contemporaneous_reconstruction" and \
            not str(event.get("time_precision", "")).strip():
        errors.append(
            "time_precision: a reconstruction must declare how precisely its time is known — "
            "'unknown' is an honest value, silence is not")
    if event["action"] not in ACTIONS:
        errors.append(f"action: must be one of {sorted(ACTIONS)}")
    if event["reason"] not in REASONS:
        errors.append(f"reason: must be one of {sorted(REASONS)}")
    if event["reason"] == "other_declared" and \
            not str(event.get("reason_detail", "")).strip():
        errors.append(
            "reason_detail: 'other_declared' names no reason by itself; state the dependency")

    for field in ("previous_commit", "current_commit", "dependency_commit"):
        if not _is_commitish(event[field]):
            errors.append(f"{field}: must be a hex commit id, or 'none'/'unknown'")

    # 🔴 The one invariant that makes the two actions mean different things. An action is a
    # claim about whether the shared checkout moved, and a record that says MOVE while naming
    # one commit twice is not a typo — it is a claim nobody can check against the repository.
    if event["action"] == "MOVE" and event["previous_commit"] == event["current_commit"]:
        errors.append(
            "action MOVE with previous_commit == current_commit: a move that changes nothing "
            "is not a move")
    if event["action"] == "NO_MOVE" and event["previous_commit"] != event["current_commit"]:
        errors.append(
            "action NO_MOVE with previous_commit != current_commit: the checkout is recorded "
            "as unmoved while the two commits differ")

    # Explicit, even when empty. An absent list and an empty list are the same JSON to a
    # reader and completely different facts: "nobody must consume this" is a decision, and
    # a missing field is a decision nobody made.
    for field in ("landed_artifacts", "actors_required_to_consume"):
        if not isinstance(event[field], list):
            errors.append(f"{field}: must be a list, explicitly empty when there is nothing")

    if not isinstance(event["invalidates_active_work"], bool):
        errors.append("invalidates_active_work: must be true or false, never a prose hedge")

    for field in ("workspace", "branch_or_detached", "required_action_by_readers",
                  "validation_status", "announced_by", "recorded_at"):
        if not str(event[field]).strip():
            errors.append(f"{field}: must not be empty")

    observations = event["observations"]
    if not isinstance(observations, list):
        errors.append("observations: must be a list, explicitly empty when nothing was measured")
    else:
        for position, observation in enumerate(observations):
            prefix = f"observations[{position}]"
            if not isinstance(observation, dict):
                errors.append(f"{prefix}: must be an object")
                continue
            for field in OBSERVATION_FIELDS:
                if not str(observation.get(field, "")).strip():
                    errors.append(
                        f"{prefix}.{field}: an observation must name who measured what, "
                        f"where and with what result — an unattributed measurement becomes "
                        f"Plan's by default, which is how a borrowed number turns into a "
                        f"declared one")
    return errors


def load_ledger(path: Path) -> list[dict[str, Any]]:
    """Parse and verify the chain. Chain first, for the reason the receipt ledger gives:
    'this record is malformed' and 'the recorded past changed' are not equally serious."""
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"line {number}: invalid JSON: {error.msg}") from error
        if not isinstance(value, dict):
            raise ValueError(f"line {number}: event must be a JSON object")
        events.append(value)
    chain_errors = chain.validate_ledger_chain(events)
    if chain_errors:
        raise ValueError("; ".join(chain_errors))
    for number, event in enumerate(events, 1):
        errors = validate_event(event)
        if errors:
            raise ValueError(f"line {number}: {'; '.join(errors)}")
    identifiers = [event["event_id"] for event in events]
    duplicates = sorted({i for i in identifiers if identifiers.count(i) > 1})
    if duplicates:
        raise ValueError(f"duplicate event_id: {', '.join(duplicates)}")
    return events


def append_event(event: dict[str, Any], *, ledger: Path, manifest: Path) -> dict[str, Any]:
    """Append one event and re-anchor, refusing anything the ledger cannot carry.

    The prior history is re-read and re-verified here, inside this call, so an append can
    never extend — or launder — a corrupted past.
    """
    record = dict(event)
    record.pop(chain.CHAIN_FIELD, None)
    errors = validate_event({**record, chain.CHAIN_FIELD: None})
    errors = [item for item in errors if not item.startswith("missing required field: "
                                                             f"{chain.CHAIN_FIELD}")]
    if errors:
        raise ValueError("; ".join(errors))

    existing = load_ledger(ledger)
    if any(item["event_id"] == record["event_id"] for item in existing):
        raise ValueError(f"event_id already recorded: {record['event_id']}")

    # 🔴 The anchor is checked BEFORE the append, and the first version was not.
    #
    # It appended, then tried to anchor, and on failure raised an error whose own wording
    # admitted the damage: *"the ledger was appended but could not be anchored"*. That is
    # exactly the state this module's own LINT check calls `SYNC_EPOCH_LEDGER_UNTRUSTED` /
    # `BLOCK_SYSTEM` — so the writer's failure path manufactured the condition the reader's
    # failure path treats as unrecoverable. Reproduced before fixing: one line written, no
    # anchor, `verify` red.
    #
    # The test that was supposed to cover this asserted only that a `ValueError` was raised.
    # **A test for a refusal has to assert what was NOT written, not merely that something was
    # thrown** — otherwise it passes while the damage happens behind the exception.
    #
    # Reported by another actor reading the source; the wording of my own error message was
    # the evidence.
    if not manifest.exists():
        raise ValueError(f"{manifest} does not exist; refusing to append an unanchorable event")
    manifest_text = manifest.read_text(encoding="utf-8")
    if len(ANCHOR_EVENTS.findall(manifest_text)) != 1 or \
            len(ANCHOR_HEAD.findall(manifest_text)) != 1:
        raise ValueError(
            f"{manifest} declares no single {ANCHOR_PREFIX}_events/{ANCHOR_PREFIX}_head "
            f"anchor pair; refusing to append an event that could not then be anchored")

    record[chain.CHAIN_FIELD] = chain.ledger_head(existing)
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with open(ledger, "a", encoding="utf-8") as handle:
        handle.write(chain.canonical_line(record) + "\n")
        handle.flush()
        os.fsync(handle.fileno())

    persisted = load_ledger(ledger)
    if not chain.write_state_anchor(manifest, persisted,
                                    events_pattern=ANCHOR_EVENTS, head_pattern=ANCHOR_HEAD):
        # Unreachable through the preflight above; kept because the manifest is a shared file
        # and another writer can change it between the two reads. The ledger is now ahead of
        # the anchor, so it says so instead of returning as if it had not.
        raise ValueError(
            f"{manifest} lost its {ANCHOR_PREFIX} anchor pair between the preflight and the "
            f"write: the event IS persisted and the anchor is NOT updated. Re-anchor before "
            f"anything else reads this ledger")
    return record


def anchor_errors(manifest_text: str, events: list[dict[str, Any]]) -> list[str]:
    """A hash chain cannot see truncation: lopping off the tail leaves a valid prefix."""
    found_events = list(ANCHOR_EVENTS.finditer(manifest_text))
    found_head = list(ANCHOR_HEAD.finditer(manifest_text))
    if len(found_events) != 1 or len(found_head) != 1:
        return [f"state manifest must declare exactly one {ANCHOR_PREFIX}_events and one "
                f"{ANCHOR_PREFIX}_head field"]
    try:
        count = int(found_events[0].group(2))
    except ValueError:
        return [f"{ANCHOR_PREFIX} anchor is malformed"]
    declared = found_head[0].group(2).strip().strip('"')
    declared_head = None if declared in {"null", "none", ""} else declared
    problems: list[str] = []
    if count != len(events):
        problems.append(
            f"sync epoch ledger holds {len(events)} event(s); the state manifest anchors "
            f"{count}: events were truncated, or the anchor was not updated after an append")
    actual = chain.ledger_head(events)
    if declared_head != actual:
        problems.append(f"sync epoch ledger head {actual} does not match anchored {declared_head}")
    return problems


def verify(root: Path) -> list[str]:
    ledger, manifest = default_ledger(root), default_manifest(root)
    if not ledger.exists():
        return [f"{LEDGER_RELATIVE} does not exist"]
    try:
        events = load_ledger(ledger)
    except ValueError as error:
        return [str(error)]
    if not manifest.exists():
        return [f"{MANIFEST_RELATIVE} does not exist"]
    return anchor_errors(manifest.read_text(encoding="utf-8"), events)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    # See repo_root: a "." default reported "no sync epoch recorded" from any
    # subdirectory — an absence produced by looking in the wrong place, at exit 0.
    parser.add_argument("--root", default=None,
                        help="repository root (default: derived from the working tree)")
    subparsers = parser.add_subparsers(dest="command", required=True)
    recorder = subparsers.add_parser("record", help="append one SYNC_EPOCH and re-anchor")
    recorder.add_argument("--event", required=True, help="path to the event JSON")
    subparsers.add_parser("verify", help="chain plus tail anchor")
    subparsers.add_parser("status", help="the latest epoch and what it asked of readers")
    args = parser.parse_args()
    try:
        root = Path(args.root).resolve() if args.root else repo_root()
    except RootError as exc:
        print(f"SYNC EPOCH UNDERIVABLE: {exc}", file=sys.stderr)
        return 2

    if args.command == "record":
        payload = json.loads(Path(args.event).read_text(encoding="utf-8"))
        try:
            record = append_event(payload, ledger=default_ledger(root),
                                  manifest=default_manifest(root))
        except ValueError as error:
            print(f"REFUSED: {error}", file=sys.stderr)
            return 1
        total = len(load_ledger(default_ledger(root)))
        print(f"RECORDED: {record['event_id']} ({record['action']}, {record['reason']})")
        print(f"ANCHORED: {total} event(s) in {MANIFEST_RELATIVE}")
        return 0

    if args.command == "verify":
        problems = verify(root)
        if problems:
            print("FAILED:", file=sys.stderr)
            for problem in problems:
                print(f"- {problem}", file=sys.stderr)
            return 1
        events = load_ledger(default_ledger(root))
        print(f"OK: {len(events)} chained sync epoch(s), tail anchored in {MANIFEST_RELATIVE}")
        return 0

    events = load_ledger(default_ledger(root))
    if not events:
        print("no sync epoch recorded")
        return 0
    latest = events[-1]
    print(f"latest:      {latest['event_id']}  {latest['action']}  ({latest['reason']})")
    print(f"workspace:   {latest['workspace']}")
    print(f"commit:      {latest['current_commit']}  [{latest['branch_or_detached']}]")
    print(f"consumers:   {latest['actors_required_to_consume'] or 'none'}")
    print(f"invalidates: {latest['invalidates_active_work']}")
    print(f"readers:     {latest['required_action_by_readers']}")
    for observation in latest["observations"]:
        print(f"  measured by {observation['measured_by']}: {observation['measurement']} "
              f"-> {observation['result']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
