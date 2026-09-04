#!/usr/bin/env python3
"""The P7 activity/event ledger: one writer per file, a derived consolidated view.

`governance/plan_defined_parameters.md` §P7 chose option (a) of J.1 — a per-actor
append-only JSONL inside each actor's own worktree, consolidated by Plan into a derived
canonical view — and recorded the writer and the validator as a debt. This is that writer
and that validator. §P7 also named the pattern to reuse rather than reinvent:
`fulltext_receipts.py`, whose append-only claim is enforced by a per-event hash chain and
an external tail anchor. What is reused, and what deliberately is not:

* REUSED — `ledger_prev_hash` over the canonical serialization of the preceding event, so
  rewriting or deleting any historical line breaks every line after it; the whole file is
  re-read and chain-verified *inside* an exclusive lock before an append extends it, so an
  append onto a rewritten past fails closed instead of laundering the tamper into
  honest-looking history.
* DIVERGENCE, with its reason — the tail anchor is NOT written into
  `framework/state/state_manifest_current.md`. That manifest is a scientific state file
  whose four siblings change only through `BATCH_COMMIT`; an engineering event ledger that
  rewrote it on every append would put lab telemetry inside the science gate. The anchor
  lives in `ledger/consolidated/anchors.json` instead, and `consolidate` refuses to move an
  actor's anchor backwards — a truncated actor file is an error, not a silently re-anchored
  one. That is strictly more than `fulltext_receipts` does at its own anchor.

The residual limit is the same one `fulltext_receipts` states about itself and is stated
here rather than left to be discovered: someone who truncates an actor file *and*
re-anchors it in the same breath is not caught by arithmetic. Both objects are committed,
so that is a reviewable diff in two files. The integrity claim is "visible in review",
never "impossible".

J.1's other strict rule is honoured by construction: **a written event is never updated,
not even to link it to its closure.** The linkage lives in the closing event, which carries
`closes_event_id` pointing back. `closed_by` exists ONLY in the consolidated view, which is
why that view must be rebuildable by replay rather than maintained in place.

Sovereignty, also from J.1: repository state wins. This ledger is audit and analysis
surface, never a second source of truth.

🔴 **What "one writer per file" is, and is not.** It is a CONVENTION plus a read-time
check, not a construction. Six concurrent processes were run against one actor file and
all six appended successfully — the `flock` held, the chain stayed valid, the sequence
stayed valid, and 120 events landed. Nothing prevents a second process from writing
another actor's ledger; what exists is that `read_all` takes each event's owner from the
FILENAME and rejects any event declaring a different `actor_id`, so a cross-written event
is detected on the next read rather than prevented at the write. The equivalent check
inside `append_event` is a tautology and is marked as one where it sits. Concurrency
safety and single-writership are two claims, and only the first is enforced.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

try:
    import fcntl
except ImportError:  # pragma: no cover - POSIX is required for fail-closed append locking
    fcntl = None


# J.1's "tipi minimi", carried verbatim and in its order. This vocabulary is the annex's,
# not this module's: a loop that needs a transition J.1 did not name is a governance
# question, not a constant to extend here.
EVENT_TYPES = (
    "TASK_ASSIGNED", "TASK_ACKED", "TASK_CLAIMED", "TASK_COMPLETE", "TASK_CANCELLED",
    "CHECKPOINT_WRITTEN", "RESUMED_FROM_MILESTONE", "REVIEW_OPENED", "REVIEW_CLOSED",
    "WORK_COMMIT", "CANDIDATE_CREATED", "BATCH_COMMITTED", "BATCH_ABORTED",
    "ACTOR_DOWN", "ACTOR_ACTIVE", "LEASE_ACQUIRED", "LEASE_STALE",
    "HUMAN_REQUIRED_OPENED", "APPROVAL_RESOLVED", "LEARNING_PROMOTED",
    "GOVERNANCE_UPDATED", "DISSENT_OPENED", "CHALLENGE_ADJUDICATED",
)

# Which closing type may close which opening type. A closure whose `closes_event_id` points
# at a type not listed here is a mis-link, and mis-links are the failure J.1 names under
# DETECTION ("aperture senza chiusura"): the pair has to be checkable, or the detector is
# counting rather than checking.
CLOSES = {
    "TASK_COMPLETE": frozenset({"TASK_ASSIGNED"}),
    "TASK_CANCELLED": frozenset({"TASK_ASSIGNED"}),
    "REVIEW_CLOSED": frozenset({"REVIEW_OPENED"}),
    "APPROVAL_RESOLVED": frozenset({"HUMAN_REQUIRED_OPENED"}),
    "ACTOR_ACTIVE": frozenset({"ACTOR_DOWN"}),
    "LEASE_STALE": frozenset({"LEASE_ACQUIRED"}),
}
# A closure that must carry `closes_event_id`. `ACTOR_ACTIVE` and `LEASE_STALE` are excluded
# on purpose: the first ACTOR_ACTIVE of a session closes nothing, and a lease can go stale
# in a ledger whose acquisition was written by a process that never got to append.
CLOSURE_REQUIRED = frozenset({
    "TASK_COMPLETE", "TASK_CANCELLED", "REVIEW_CLOSED", "APPROVAL_RESOLVED"})

# Types that name a unit of work, so the join key that makes a queue possible must exist.
TASK_SCOPED = frozenset({
    "TASK_ASSIGNED", "TASK_ACKED", "TASK_CLAIMED", "TASK_COMPLETE", "TASK_CANCELLED",
    "CHECKPOINT_WRITTEN", "RESUMED_FROM_MILESTONE", "REVIEW_OPENED", "REVIEW_CLOSED",
    "WORK_COMMIT",
})

CHAIN_FIELD = "ledger_prev_hash"
DERIVED_ONLY = frozenset({"closed_by"})

REQUIRED = ("event_id", "event_at", "actor_id", "event_type", "object")
OPTIONAL = ("task_id", "durable_pointer", "closes_event_id")

ACTOR_ID = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
EVENT_ID = re.compile(r"^EV-[a-z][a-z0-9-]{0,63}-\d{4,}$")

DEFAULT_EVENTS_DIR = Path("ledger") / "events"
DEFAULT_VIEW_DIR = Path("ledger") / "consolidated"


# ---------------------------------------------------------------------------
# chain primitives — the shapes `fulltext_receipts.py` already proved
# ---------------------------------------------------------------------------

def canonical_line(event: dict[str, Any]) -> str:
    """The exact byte sequence an event occupies on disk."""
    return json.dumps(event, ensure_ascii=False, sort_keys=True)


def event_digest(event: dict[str, Any]) -> str:
    """SHA-256 over the whole persisted record, ``ledger_prev_hash`` included.

    Including the chain field is what makes the chain a chain: tampering with one link
    invalidates every link downstream of it, not merely the record that was edited.
    """
    return hashlib.sha256(canonical_line(event).encode("utf-8")).hexdigest()


def ledger_head(events: list[dict[str, Any]]) -> Optional[str]:
    return event_digest(events[-1]) if events else None


def validate_chain(events: list[dict[str, Any]], *, label: str = "") -> list[str]:
    """Verify that persisted history has only ever been appended to."""
    where = f"{label}: " if label else ""
    errors: list[str] = []
    expected: Optional[str] = None
    for number, event in enumerate(events, 1):
        if CHAIN_FIELD not in event:
            errors.append(f"{where}line {number}: missing {CHAIN_FIELD}: the file is not chained")
        elif event[CHAIN_FIELD] != expected:
            errors.append(
                f"{where}line {number}: broken hash chain: earlier history was rewritten "
                "or removed")
        expected = event_digest(event)
    return errors


def parse_lines(text: str, *, label: str = "") -> list[dict[str, Any]]:
    where = f"{label}: " if label else ""
    events: list[dict[str, Any]] = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{where}line {number}: not JSON: {exc}") from exc
        if not isinstance(event, dict):
            raise ValueError(f"{where}line {number}: expected a JSON object")
        events.append(event)
    return events


def load_actor_file(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return parse_lines(path.read_text(encoding="utf-8"), label=path.name)


# ---------------------------------------------------------------------------
# validation of one event, in isolation and in sequence
# ---------------------------------------------------------------------------

def _valid_timestamp(value: Any) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return False
    return True


def validate_event(event: Any, *, actor_id: Optional[str] = None) -> list[str]:
    """Field-level validation of a single persisted event."""
    if not isinstance(event, dict):
        return ["event is not a JSON object"]
    errors: list[str] = []
    for field in REQUIRED:
        if not event.get(field):
            errors.append(f"missing required field `{field}`")
    unknown = set(event) - set(REQUIRED) - set(OPTIONAL) - {CHAIN_FIELD}
    if unknown:
        problem = "fields outside the J.1 event shape: " + ", ".join(sorted(unknown))
        if unknown & DERIVED_ONLY:
            # Named separately because this is the ONE way a source ledger silently
            # becomes a second source of truth: a `closed_by` written at the source is an
            # opening event that learned its own outcome, which J.1 forbids in words.
            problem += ". `closed_by` exists only in the derived view"
        errors.append(problem)
    kind = event.get("event_type")
    if kind and kind not in EVENT_TYPES:
        errors.append(f"`{kind}` is not one of J.1's event types")
    if event.get("actor_id") and not ACTOR_ID.match(str(event["actor_id"])):
        errors.append(f"actor_id `{event['actor_id']}` is not a lowercase slug")
    if actor_id is not None and event.get("actor_id") != actor_id:
        # This has content only where `actor_id` comes from the FILENAME — i.e. in
        # `read_all`. Called from `append_event` it is a tautology, because the record's
        # `actor_id` was assigned from the same parameter moments earlier.
        errors.append(
            f"event declares actor_id `{event.get('actor_id')}` in the ledger of "
            f"`{actor_id}`: a file's events belong to the actor its name declares")
    if event.get("event_id") and not EVENT_ID.match(str(event["event_id"])):
        errors.append(f"event_id `{event['event_id']}` is not `EV-<actor>-<seq>`")
    if event.get("event_at") and not _valid_timestamp(event["event_at"]):
        errors.append(f"event_at `{event['event_at']}` is not `YYYY-MM-DDTHH:MM:SSZ`")
    if kind in TASK_SCOPED and not event.get("task_id"):
        errors.append(f"`{kind}` names a unit of work and must carry `task_id`")
    if event.get("closes_event_id"):
        if kind not in CLOSES:
            errors.append(
                f"`{kind}` is not a closing event and may not carry `closes_event_id`; "
                "J.1 puts the linkage in the closure, and only there")
    elif kind in CLOSURE_REQUIRED:
        errors.append(f"`{kind}` is a closing event and must carry `closes_event_id`")
    return errors


def validate_sequence(events: list[dict[str, Any]], *, label: str = "") -> list[str]:
    """Cross-event rules inside ONE actor file: identity, ordering, monotone time."""
    where = f"{label}: " if label else ""
    errors: list[str] = []
    seen: set[str] = set()
    previous_at: Optional[str] = None
    for number, event in enumerate(events, 1):
        event_id = event.get("event_id")
        if event_id in seen:
            errors.append(f"{where}line {number}: duplicate event_id `{event_id}`")
        if isinstance(event_id, str):
            seen.add(event_id)
            expected = f"EV-{event.get('actor_id')}-{number:04d}"
            if event_id != expected:
                errors.append(
                    f"{where}line {number}: event_id `{event_id}` does not match its "
                    f"position in the file (`{expected}`); the sequence is the position")
        at = event.get("event_at")
        if isinstance(at, str) and previous_at is not None and at < previous_at:
            errors.append(
                f"{where}line {number}: event_at `{at}` precedes line {number - 1}'s "
                f"`{previous_at}`: an append-only file cannot go back in time")
        if isinstance(at, str):
            previous_at = at
    return errors


# ---------------------------------------------------------------------------
# the writer
# ---------------------------------------------------------------------------

def actor_ledger_path(events_dir: Path, actor_id: str) -> Path:
    return events_dir / f"{actor_id}.jsonl"


def append_event(
    events_dir: Path,
    actor_id: str,
    event_type: str,
    obj: str,
    *,
    task_id: Optional[str] = None,
    durable_pointer: Optional[str] = None,
    closes_event_id: Optional[str] = None,
    now: Optional[datetime] = None,
) -> dict[str, Any]:
    """Append one event under an exclusive lock and return the persisted record.

    `event_id` and `event_at` are the tool's, never the caller's: the identifier IS the
    position in the file and the timestamp IS persistence time. A caller that could supply
    either could write an event that claims a place it does not occupy, and the sequence
    check below would then be validating the caller's arithmetic rather than the file.
    """
    if fcntl is None:
        raise RuntimeError("POSIX file locking unavailable; refusing unlocked event append")
    if not ACTOR_ID.match(actor_id):
        raise ValueError(f"actor_id `{actor_id}` is not a lowercase slug")
    path = actor_ledger_path(events_dir, actor_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    with path.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            handle.seek(0)
            existing = parse_lines(handle.read(), label=path.name)
            broken = (validate_chain(existing, label=path.name)
                      + validate_sequence(existing, label=path.name))
            if broken:
                raise ValueError(
                    "refusing to append onto unverified history: " + "; ".join(broken))
            record: dict[str, Any] = {
                "event_id": f"EV-{actor_id}-{len(existing) + 1:04d}",
                "event_at": stamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "actor_id": actor_id,
                "event_type": event_type,
                "object": obj,
            }
            if task_id:
                record["task_id"] = task_id
            if durable_pointer:
                record["durable_pointer"] = durable_pointer
            if closes_event_id:
                record["closes_event_id"] = closes_event_id
            errors = validate_event(record, actor_id=actor_id)
            if errors:
                raise ValueError("; ".join(errors))
            record[CHAIN_FIELD] = ledger_head(existing)
            sequence_errors = validate_sequence(existing + [record], label=path.name)
            if sequence_errors:
                raise ValueError("; ".join(sequence_errors))
            handle.seek(0, os.SEEK_END)
            handle.write(canonical_line(record) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    return record


# ---------------------------------------------------------------------------
# the consolidator — a DERIVED view, rebuilt by replay, never hand-edited
# ---------------------------------------------------------------------------

def actor_files(events_dir: Path) -> list[Path]:
    if not events_dir.is_dir():
        return []
    return sorted(p for p in events_dir.glob("*.jsonl") if p.is_file())


def sequence_number(event: dict[str, Any]) -> int:
    """The integer at the end of an `event_id`, for ordering.

    🔴 Sorting on the id STRING reorders the ledger at 10,000 events: `EV-a-10000` sorts
    before `EV-a-9998` lexically, and `append_event` mints exactly those ids with `:04d`,
    which stops zero-padding at five digits. Every consumer rides this key — the view's
    "first closure wins", the queue's ordering — so the reordering would be silent and
    total, and it is a boundary this module reaches on its own.
    """
    tail = str(event.get("event_id", "")).rsplit("-", 1)[-1]
    return int(tail) if tail.isdigit() else -1


def sort_key(event: dict[str, Any]) -> tuple[str, str, int]:
    return (str(event.get("event_at", "")), str(event.get("actor_id", "")),
            sequence_number(event))


def read_all(events_dir: Path) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]],
                                        list[str]]:
    """Every actor file, chain-verified, keyed by the actor its FILENAME names."""
    events: list[dict[str, Any]] = []
    per_actor: dict[str, list[dict[str, Any]]] = {}
    errors: list[str] = []
    for path in actor_files(events_dir):
        actor_id = path.stem
        try:
            lines = load_actor_file(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        errors += validate_chain(lines, label=path.name)
        errors += validate_sequence(lines, label=path.name)
        for number, event in enumerate(lines, 1):
            for problem in validate_event(event, actor_id=actor_id):
                errors.append(f"{path.name}: line {number}: {problem}")
        per_actor[actor_id] = lines
        events += lines
    events.sort(key=sort_key)
    return events, per_actor, errors


def anchors_for(per_actor: dict[str, list[dict[str, Any]]]) -> dict[str, dict[str, Any]]:
    return {actor: {"events": len(lines), "head": ledger_head(lines)}
            for actor, lines in per_actor.items()}


def cross_actor_findings(events: list[dict[str, Any]]) -> list[tuple[str, str]]:
    """Rules that only the consolidated view can see, because they span writers.

    A closure written by the actor that finished the work points at an opening written by
    the Orchestrator that assigned it. Neither file can check that alone — which is why
    this check lives here and not in `append_event`, and why an append is not proof that
    the event it closes exists.

    🔴 These are FINDINGS, not structural errors, and the difference was learned by being
    bitten. A chain break or a forged view is repairable: restore the file, rebuild the
    view. A mis-linked closure is a permanent fact about an immutable record — the ledger
    is append-only, so there is no edit that removes it. Treating it as blocking meant one
    mistyped `--closes` halted consolidation *forever*, and the audit surface J.1 gives
    Mirror would have stayed unbuildable because of a typo. That happened here, on the
    third use of this tool, to its own author.

    So each finding is returned WITH the event id that carries it, and
    `ledger/consolidated/acknowledged.json` may carry a reason per id. An unacknowledged
    finding still blocks; an acknowledged one is reported and does not. This is not a
    weakening — the acknowledgement demands a written reason, and a stale one is itself an
    error, which is the same discipline this repository already applies to test exemptions.
    """
    findings: list[tuple[str, str]] = []
    by_id = {e.get("event_id"): e for e in events}
    closers: dict[str, str] = {}
    for event in events:
        target_id = event.get("closes_event_id")
        if not target_id:
            continue
        # 🔴 Two closures for one opening. J.1's DETECTION names "aperture senza chiusura"
        # and says nothing about the reverse, so nothing looked for it: a TASK_COMPLETE and
        # a TASK_CANCELLED could both close one assignment, consolidation reported no
        # error, and the view silently kept whichever sorted first — i.e. the outcome of
        # the task became a function of the sort order.
        here = str(event.get("event_id"))
        if target_id in closers:
            findings.append((here,
                f"{target_id} is closed twice: by {closers[str(target_id)]} and by "
                f"{here}. An opening has one outcome"))
        else:
            closers[str(target_id)] = here
        target = by_id.get(target_id)
        if target is None:
            findings.append((here, f"{here} closes `{target_id}`, which is in no actor ledger"))
            continue
        allowed = CLOSES.get(str(event.get("event_type")), frozenset())
        if target.get("event_type") not in allowed:
            findings.append((here,
                f"{here} ({event.get('event_type')}) closes {target_id} "
                f"({target.get('event_type')}), which it may not close"))
        elif event.get("task_id") != target.get("task_id"):
            findings.append((here,
                f"{here} closes {target_id} across a task boundary: "
                f"`{event.get('task_id')}` vs `{target.get('task_id')}`"))
        elif str(event.get("event_at", "")) < str(target.get("event_at", "")):
            findings.append((here, f"{here} closes {target_id} before it was opened"))
    return findings


def load_acknowledgements(view_dir: Path) -> dict[str, str]:
    path = view_dir / "acknowledged.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("events") or {}


MIN_REASON = 40


def triage_findings(findings: list[tuple[str, str]],
                    acknowledged: dict[str, str]) -> tuple[list[str], list[str]]:
    """Split content findings into (blocking, acknowledged) and police the reasons.

    A stale acknowledgement — one naming an event that no longer produces a finding — is an
    error in its own right, so the file cannot accumulate cover for problems that are gone.
    A reason shorter than `MIN_REASON` is refused: an acknowledgement needs an argument,
    not a label.
    """
    blocking: list[str] = []
    excused: list[str] = []
    seen: set[str] = set()
    for event_id, message in findings:
        seen.add(event_id)
        reason = acknowledged.get(event_id)
        if reason is None:
            blocking.append(message)
        elif len(reason.strip()) < MIN_REASON:
            blocking.append(
                f"{message} — acknowledged with a reason too short to be one: {reason!r}")
        else:
            excused.append(f"{message} [ACKNOWLEDGED: {reason}]")
    for event_id in sorted(set(acknowledged) - seen):
        blocking.append(
            f"stale acknowledgement for {event_id}: it produces no finding. Remove it, "
            "rather than leaving cover for a problem that is gone")
    return blocking, excused


def consolidated_view(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """The replayed view. `closed_by` exists HERE and nowhere else — J.1's strict rule.

    The source line is never rewritten, so the only place an opening can learn its own
    outcome is a view derived after the fact. That is the whole reason this view must be
    rebuildable rather than maintained.
    """
    closed_by: dict[str, str] = {}
    for event in events:
        target = event.get("closes_event_id")
        if target and target not in closed_by:
            closed_by[target] = str(event.get("event_id"))
    view = []
    for event in events:
        row = dict(event)
        if row.get("event_id") in closed_by:
            row["closed_by"] = closed_by[str(row["event_id"])]
        view.append(row)
    return view


def anchor_regressions(previous: dict[str, Any], events: dict[str, list[dict[str, Any]]],
                       events_dir: Path) -> list[str]:
    """The anchored history must still be a PREFIX of the current file, byte for byte.

    🔴 The first version of this compared only `(count, head)` and asked whether the count
    had gone down. Mirror broke it in one move: truncate the ledger — refused, correctly —
    then simply append until the count passes the anchor again. `after > before` skipped
    both branches, the anchor advanced, and three real assignments were gone from history
    and from the queue with every check green. Nobody re-anchored by hand, so that was not
    the residual limit this module declares; the tool laundered it.

    A count is not a history. What is checked now is EXTENSION: replay the first N events
    of the current file, where N is the anchored count, and require that prefix to hash to
    exactly the anchored head. Truncate-then-regrow fails because the prefix at position N
    is no longer the history that was anchored — which is the property the docstring
    claimed all along and did not have.
    """
    errors: list[str] = []
    for actor_id, before in (previous.get("actors") or {}).items():
        anchored = int(before.get("events") or 0)
        current = events.get(actor_id)
        if current is None:
            errors.append(
                f"`{actor_id}` was anchored at {anchored} events and its ledger is now "
                f"absent from {events_dir}")
            continue
        if len(current) < anchored:
            errors.append(
                f"`{actor_id}` was anchored at {anchored} events and now has "
                f"{len(current)}: history was truncated")
            continue
        prefix_head = ledger_head(current[:anchored])
        if prefix_head != before.get("head"):
            errors.append(
                f"`{actor_id}` no longer EXTENDS its anchored history: replaying its first "
                f"{anchored} events gives {prefix_head}, and {before.get('head')} was "
                "anchored. Appending past a truncation does not repair it")
    return errors


def view_bytes(events: list[dict[str, Any]]) -> str:
    return "".join(canonical_line(row) + "\n" for row in consolidated_view(events))


def view_disagreements(events: list[dict[str, Any]], view_dir: Path) -> list[str]:
    """The committed view must be exactly what replaying the sources produces.

    🔴 Nothing checked this, and the view is the surface every reader reads: `queue_source`
    prefers it, so `open` and `show` answer from it. Mirror deleted two assignments from
    the committed view, appended a fabricated `TASK-FORGED` row, and the whole battery
    stayed green — `validate` said PASS, the suite said OK, and `open` listed a task nobody
    ever assigned while omitting two that were. The source ledgers were untouched and
    perfectly chained the entire time, which is precisely why chaining them was never
    enough: a derived file that nobody re-derives is an unchecked second source of truth.
    """
    path = view_dir / "events.jsonl"
    if not path.is_file():
        return []
    actual = path.read_text(encoding="utf-8")
    if actual == view_bytes(events):
        return []
    return [f"{path} is not the replay of the actor ledgers: it was edited, or it is stale. "
            "Rebuild it with `event_ledger.py consolidate`; never hand-edit it"]


def consolidate(events_dir: Path, view_dir: Path) -> tuple[list[str], dict[str, Any]]:
    """Rebuild the derived view and advance the anchor, or refuse and change nothing."""
    events, per_actor, errors = read_all(events_dir)
    blocking, excused = triage_findings(cross_actor_findings(events),
                                        load_acknowledgements(view_dir))
    errors += blocking
    anchor_path = view_dir / "anchors.json"
    previous: dict[str, Any] = {}
    if anchor_path.is_file():
        previous = json.loads(anchor_path.read_text(encoding="utf-8"))
    errors += anchor_regressions(previous, per_actor, events_dir)
    if errors:
        return errors, {}
    for note in excused:
        print(f"FINDING: {note}", file=sys.stderr)
    anchors = anchors_for(per_actor)
    view_dir.mkdir(parents=True, exist_ok=True)
    (view_dir / "events.jsonl").write_text(view_bytes(events), encoding="utf-8")
    anchor = {
        "generated_by": "framework/scripts/event_ledger.py consolidate",
        "events": len(events),
        "actors": {k: anchors[k] for k in sorted(anchors)},
    }
    anchor_path.write_text(json.dumps(anchor, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return [], anchor


def load_view(view_dir: Path) -> list[dict[str, Any]]:
    path = view_dir / "events.jsonl"
    if not path.is_file():
        return []
    return parse_lines(path.read_text(encoding="utf-8"), label=path.name)


# ---------------------------------------------------------------------------
# the queue — derived, not a state machine
# ---------------------------------------------------------------------------

def open_tasks(events: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Assignments no closure has closed, oldest first.

    This is a JOIN, not a state machine: openness is "a TASK_ASSIGNED with no
    TASK_COMPLETE or TASK_CANCELLED pointing at it", and the claim/ack columns are the
    same join on `task_id`. Nothing here decides what happens next — a reader does.
    """
    rows = list(events)
    # 🔴 Only a closure that MAY close an assignment removes one from the queue. Built from
    # every event carrying `closes_event_id`, this set was wider than the unit the
    # docstring describes: a `REVIEW_CLOSED` mis-pointed at a `TASK_ASSIGNED` is accepted
    # by the writer — which cannot see peer files — and made a live assignment disappear
    # from the queue. `cross_actor_errors` does catch the mis-link, but the queue is also
    # read straight off the unconsolidated source, where that check never runs.
    closers = {kind for kind, targets in CLOSES.items() if "TASK_ASSIGNED" in targets}
    closed = {str(e["closes_event_id"]) for e in rows
              if e.get("closes_event_id") and e.get("event_type") in closers}
    claimed: dict[str, str] = {}
    acked: set[str] = set()
    for event in rows:
        task = str(event.get("task_id") or "")
        if event.get("event_type") == "TASK_CLAIMED" and task:
            claimed[task] = str(event.get("actor_id"))
        elif event.get("event_type") == "TASK_ACKED" and task:
            acked.add(task)
    out = []
    for event in rows:
        if event.get("event_type") != "TASK_ASSIGNED":
            continue
        if str(event.get("event_id")) in closed:
            continue
        task = str(event.get("task_id") or "")
        out.append({
            "event_id": event.get("event_id"),
            "task_id": event.get("task_id"),
            "assigned_at": event.get("event_at"),
            "assigned_by": event.get("actor_id"),
            "object": event.get("object"),
            "durable_pointer": event.get("durable_pointer"),
            "acked": task in acked,
            "claimed_by": claimed.get(task),
        })
    # 🔴 The SAME numeric key as `read_all`. Fixing the sort in one place and leaving it
    # lexical here was worse than not fixing it: the repair's own comment named "the
    # queue's ordering" as a consumer of the corrected key, and the queue went on sorting
    # `EV-a-10000` before `EV-a-9998`. A claim that a defect is fixed everywhere it matters
    # has to be checked at every site, not at the one that was edited.
    out.sort(key=lambda r: (str(r["assigned_at"]), sequence_number(r)))
    return out


def task_history(events: Iterable[dict[str, Any]], task_id: str) -> list[dict[str, Any]]:
    return [e for e in events if e.get("task_id") == task_id]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def queue_source(events_dir: Path, view_dir: Path) -> tuple[list[dict[str, Any]], str]:
    """Read the queue from the derived view, and say so when it falls back to the source.

    A reader that silently substitutes one surface for the other cannot tell "the queue is
    empty" from "the view was never built". The caller gets the provenance with the rows.
    """
    if (view_dir / "events.jsonl").is_file():
        return load_view(view_dir), str(view_dir / "events.jsonl")
    return read_all(events_dir)[0], f"{events_dir} (UNCONSOLIDATED — run `consolidate`)"


def _dirs(args) -> tuple[Path, Path, Path]:
    root = Path(args.root).resolve()
    events_dir = Path(args.events_dir) if args.events_dir else root / DEFAULT_EVENTS_DIR
    view_dir = Path(args.view_dir) if args.view_dir else root / DEFAULT_VIEW_DIR
    return root, events_dir, view_dir


def main() -> int:
    parser = argparse.ArgumentParser(
        description="P7 event ledger: per-actor append-only writer + consolidated view")
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--events-dir", default=None, help="override ledger/events")
    parser.add_argument("--view-dir", default=None, help="override ledger/consolidated")
    sub = parser.add_subparsers(dest="command", required=True)

    append = sub.add_parser("append", help="append one event to an actor's own ledger")
    append.add_argument("--actor", required=True)
    append.add_argument("--type", required=True, choices=EVENT_TYPES, dest="event_type")
    append.add_argument("--object", required=True, dest="obj")
    append.add_argument("--task", default=None, dest="task_id")
    append.add_argument("--pointer", default=None, dest="durable_pointer")
    append.add_argument("--closes", default=None, dest="closes_event_id")

    sub.add_parser("validate", help="chain-verify every actor ledger and the anchor")
    sub.add_parser("consolidate", help="rebuild the derived view and advance the anchor")

    queue = sub.add_parser("open", help="assignments no closure has closed")
    queue.add_argument("--json", action="store_true")

    show = sub.add_parser("show", help="every event carrying one task_id")
    show.add_argument("--task", required=True)

    args = parser.parse_args()
    root, events_dir, view_dir = _dirs(args)

    if args.command == "append":
        try:
            record = append_event(
                events_dir, args.actor, args.event_type, args.obj,
                task_id=args.task_id, durable_pointer=args.durable_pointer,
                closes_event_id=args.closes_event_id)
        except (ValueError, RuntimeError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2
        print(canonical_line(record))
        return 0

    if args.command == "validate":
        events, per_actor, errors = read_all(events_dir)
        blocking, excused = triage_findings(cross_actor_findings(events),
                                            load_acknowledgements(view_dir))
        errors += blocking
        errors += view_disagreements(events, view_dir)
        for note in excused:
            print(f"FINDING: {note}")
        anchor_path = view_dir / "anchors.json"
        if anchor_path.is_file():
            previous = json.loads(anchor_path.read_text(encoding="utf-8"))
            errors += anchor_regressions(previous, per_actor, events_dir)
        else:
            print(f"NOTE: no anchor at {anchor_path}; truncation is undetectable until "
                  "`consolidate` writes one")
        for problem in errors:
            print(f"ERROR: {problem}", file=sys.stderr)
        print(f"VERDICT: {'BLOCK' if errors else 'PASS'} — {len(events)} events, "
              f"{len(per_actor)} actor ledgers")
        return 2 if errors else 0

    if args.command == "consolidate":
        errors, anchor = consolidate(events_dir, view_dir)
        for problem in errors:
            print(f"ERROR: {problem}", file=sys.stderr)
        if errors:
            print("VERDICT: BLOCK — the view was NOT rebuilt and the anchor did not move")
            return 2
        print(f"VERDICT: PASS — {anchor['events']} events from "
              f"{len(anchor['actors'])} actor ledgers")
        return 0

    if args.command == "open":
        events, source = queue_source(events_dir, view_dir)
        rows = open_tasks(events)
        if args.json:
            print(json.dumps(rows, indent=2, ensure_ascii=False))
            return 0
        print(f"# queue read from {source}")
        if not rows:
            print("queue empty: every assignment has a closure")
        for row in rows:
            state = ("claimed by " + row["claimed_by"]) if row["claimed_by"] else (
                "acked" if row["acked"] else "unclaimed")
            print(f"{row['task_id']:<28} {state:<24} {row['object']}")
        return 0

    if args.command == "show":
        events, _ = queue_source(events_dir, view_dir)
        for event in task_history(events, args.task):
            print(canonical_line(event))
        return 0

    return 1  # pragma: no cover - argparse requires a subcommand


if __name__ == "__main__":
    raise SystemExit(main())
