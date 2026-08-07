#!/usr/bin/env python3
"""Self-anchoring growth constraints — no number a human must remember to update.

LEGEND never stops growing, so every constant that encodes "how big the system is right now"
is a defect waiting for a quiet birthday. Four such constants existed on 2026-08-06:
``EXPECTED_COUNTS`` in the canonical-structure test, the two grandfathering baselines in the
state manifest, and the DisMech ``scope_sha256`` values. Each required a person to remember,
after doing the work, to also update a number.

**The criterion this module implements is sharper than "automate it": updating a constraint
must cost at least as much as complying with it.** ``fulltext_receipts.py`` is healthy not
because it is automatic but because re-anchoring the ledger requires having produced a valid
append. When updating is cheaper than conforming, the guard is already lost — someone bumps
the number to make the suite green, which is exactly the gesture the check existed to prevent.
That happened here on 2026-08-06, with a diligent explanatory comment attached, and it went
unnoticed until the operator asked whether the design assumed growth.

Two policies, because the constants come in two shapes:

``declared_growth``
    Structural cardinality — canonical claims, integrated papers, corpus placeholders,
    literature records. These *should* grow. A batch may only move them by declaring the
    delta it made, and the recorder recomputes the registries and refuses a declaration that
    does not match. You cannot bump the number without stating a change you actually made,
    so the dishonest path is not merely expensive, it is closed.

``non_increasing``
    Grandfathered debt — registry-only full-text declarations, unread premises. These may
    only fall. An increase blocks; a decrease is re-anchored **by this tool**, because
    tightening a ratchet is always safe and asking a human to lower a number is precisely
    how the number stops being lowered. There is no value here for anyone to type.

The ledger is append-only and hash-chained, and its tail is anchored in the state manifest,
mirroring ``fulltext_receipts.py`` exactly — a proven idiom in this repository rather than a
new one. The two legacy manifest fields are kept in sync rather than moved, because
``legend_lint.py`` and ``session_self_eval.py`` already read them; that asymmetry is
deliberate and is recorded here so the next reader does not take it for an oversight.

Scale assumption, stated out loud as the growth principle requires: this module measures the
whole registry set on every invocation. At the present scale that is milliseconds. It stays
linear in registry size, so it remains cheap into the millions of records; if measurement ever
dominates a batch, cache the measurement, never the anchor.
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
from typing import Any

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
LEDGER_REL = "framework/state/growth_anchors.jsonl"
MANIFEST_REL = "framework/state/state_manifest_current.md"

CHAIN_FIELD = "anchor_prev_hash"

ANCHOR_EVENTS = re.compile(r"(?m)^(growth_anchor_events:\s*)(\S+)\s*$")
ANCHOR_HEAD = re.compile(r"(?m)^(growth_anchor_head:\s*)(\S+)\s*$")
RATCHET_BASELINE = re.compile(
    r"(?m)^(registry_only_fulltext_declarations_baseline:\s*)(\d+)\s*$")
RATCHET_IDS = re.compile(r"(?m)^(registry_only_fulltext_declaration_ids:\s*)(\[[^\n]*\])\s*$")
UNREAD_BASELINE = re.compile(r"(?m)^(unread_premise_baseline:\s*)(\d+)\s*$")
UNREAD_MEASURED = re.compile(r"(?m)^(unread_premise_measured_on:\s*)(\S+)\s*$")

STRUCTURAL_KEYS = ("claims", "papers", "corpus", "literature")

REGISTRIES = {
    "claims": "disease-models/{disease}/registries/claim_registry_current.md",
    "papers": "disease-models/{disease}/registries/paper_registry_current.md",
    "literature": "disease-models/{disease}/registries/literature_tracking_log_current.md",
}
# These four patterns ARE the definition of "a canonical record" for the whole repository.
# They were lifted verbatim from `scripts/test_canonical_structure.py`, which owned the
# cardinality before this module existed, and that test now imports them from here instead of
# keeping a second copy. The reason is the one this module exists to serve: a first draft of
# these patterns used `^## LIT-\d+` and silently missed the six `LIT-EX-NNN` records, which
# would have re-anchored the literature count six lower than the check it replaced. Two
# implementations of "what counts" drift, and the drift is invisible until they disagree about
# a real record.
HEADINGS = {
    "claims": re.compile(r"(?m)^##\s+(CLAIM\s+\d+)\s*$"),
    "papers": re.compile(r"(?m)^##\s+(PAPER\s+\d+)\s*$"),
    "corpus": re.compile(r"(?m)^##\s+(CORPUS(?:-STUB-|\s+P)\d+)\s*$"),
    "literature": re.compile(r"(?m)^##\s+(LIT-(?!\[)[A-Z0-9-]+)\s*$"),
}


# --------------------------------------------------------------------------- measurement

def measure_structural(root: Path, disease: str) -> dict[str, int]:
    """Count canonical records straight from the registries.

    Deliberately re-derived on every call rather than cached. A cached cardinality is the
    same defect as a hardcoded one, one indirection further away.
    """
    papers_text = (root / REGISTRIES["papers"].format(disease=disease)).read_text(
        encoding="utf-8")
    claims_text = (root / REGISTRIES["claims"].format(disease=disease)).read_text(
        encoding="utf-8")
    literature_text = (root / REGISTRIES["literature"].format(disease=disease)).read_text(
        encoding="utf-8")
    return {key: len(identifiers) for key, identifiers in
            structural_identifiers(claims_text, papers_text, literature_text).items()}


def structural_identifiers(claims_text: str, papers_text: str,
                           literature_text: str) -> dict[str, list[str]]:
    """The record identifiers themselves, so callers can check uniqueness as well as count."""
    return {
        "claims": HEADINGS["claims"].findall(claims_text),
        "papers": HEADINGS["papers"].findall(papers_text),
        "corpus": HEADINGS["corpus"].findall(papers_text),
        "literature": HEADINGS["literature"].findall(literature_text),
    }


def measure_registry_only(root: Path, disease: str) -> list[str]:
    """Registry records declaring a full-text review with no persisted complete receipt.

    Reuses the shared registry parser and receipt index rather than re-implementing either:
    a second implementation of "what counts as a full-text declaration" would drift from the
    first, and the drift would be invisible until the two disagreed about a real record.
    """
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    import coverage_report  # noqa: PLC0415
    import fulltext_receipts as engine  # noqa: PLC0415

    papers_path = root / REGISTRIES["papers"].format(disease=disease)
    entries = coverage_report.parse_entries(papers_path.read_text(encoding="utf-8"))
    index = engine.receipt_depth_index(engine.default_ledger_path(root, disease))
    owners = coverage_report.receipt_owners(entries, index)
    return sorted(
        entry["_id"]
        for entry in entries
        if coverage_report.classify_depth(entry) == "full_text"
        and (
            owners.get(entry["_id"]) is None
            or owners[entry["_id"]]["evidence_depth"] != "complete_fulltext_read"
        )
    )


def measure_unread_premises(root: Path, disease: str) -> list[str]:
    """PMIDs the reasoning layer leans on with no receipt, declaration or queue entry."""
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    import fulltext_receipts as engine  # noqa: PLC0415
    import session_self_eval  # noqa: PLC0415

    ledger = engine.default_ledger_path(root, disease)
    receipts = session_self_eval.load_receipts(ledger)
    return sorted(session_self_eval.unread_premises(root, disease, receipts))


def measure_all(root: Path, disease: str) -> dict[str, Any]:
    return {
        "structural": measure_structural(root, disease),
        "registry_only_fulltext": measure_registry_only(root, disease),
        "unread_premises": measure_unread_premises(root, disease),
    }


# --------------------------------------------------------------------------- ledger

def canonical_line(event: dict[str, Any]) -> str:
    return json.dumps(event, ensure_ascii=False, sort_keys=True)


def event_digest(event: dict[str, Any]) -> str:
    """SHA-256 over the whole persisted record, chain field included.

    Including the chain field is what makes the chain a chain: tampering with one link
    invalidates every link after it, not only the record that was edited.
    """
    return hashlib.sha256(canonical_line(event).encode("utf-8")).hexdigest()


def load_ledger(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    events = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as error:
            raise ValueError(f"{path}:{number} is not valid JSON: {error.msg}") from error
    return events


def verify_chain(events: list[dict[str, Any]]) -> list[str]:
    errors = []
    previous = None
    for position, event in enumerate(events, 1):
        if event.get(CHAIN_FIELD) != previous:
            errors.append(
                f"event {position} ({event.get('event_id', '?')}) breaks the chain: "
                f"declares {event.get(CHAIN_FIELD)!r}, expected {previous!r}")
        previous = event_digest(event)
    return errors


def ledger_head(events: list[dict[str, Any]]) -> str | None:
    return event_digest(events[-1]) if events else None


def tail_state(events: list[dict[str, Any]]) -> dict[str, Any] | None:
    """The last recorded value of every anchor, which is what `check` compares against."""
    if not events:
        return None
    state: dict[str, Any] = {}
    for event in events:
        for key, value in (event.get("anchors") or {}).items():
            state[key] = value
    return state


def append_event(root: Path, disease: str, kind: str, anchors: dict[str, Any],
                 note: str, batch: str | None = None) -> dict[str, Any]:
    path = root / LEDGER_REL
    events = load_ledger(path)
    chain_errors = verify_chain(events)
    if chain_errors:
        raise ValueError("refusing to append to a broken chain: " + "; ".join(chain_errors))
    event = {
        "event_id": f"GA-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{kind}",
        "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "kind": kind,
        "disease": disease,
        "batch": batch,
        "anchors": anchors,
        "note": note,
        CHAIN_FIELD: ledger_head(events),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(canonical_line(event) + "\n")
    return event


# --------------------------------------------------------------------------- manifest

def reanchor_manifest(root: Path, disease: str) -> list[str]:
    """Rewrite every manifest field this module owns. Never called with a human-typed value."""
    path = root / MANIFEST_REL
    text = path.read_text(encoding="utf-8")
    events = load_ledger(root / LEDGER_REL)
    state = tail_state(events) or {}
    changed = []

    if len(ANCHOR_EVENTS.findall(text)) != 1 or len(ANCHOR_HEAD.findall(text)) != 1:
        raise ValueError(
            "state manifest must declare exactly one growth_anchor_events and one "
            "growth_anchor_head field")
    text = ANCHOR_EVENTS.sub(lambda m: f"{m.group(1)}{len(events)}", text, count=1)
    text = ANCHOR_HEAD.sub(lambda m: f"{m.group(1)}{ledger_head(events) or 'null'}", text,
                           count=1)
    changed.append(f"growth_anchor_events={len(events)}")

    registry_only = state.get("registry_only_fulltext")
    if registry_only is not None and RATCHET_BASELINE.search(text):
        text = RATCHET_BASELINE.sub(lambda m: f"{m.group(1)}{len(registry_only)}", text,
                                    count=1)
        serialised = json.dumps(sorted(registry_only), ensure_ascii=False)
        text = RATCHET_IDS.sub(lambda m: f"{m.group(1)}{serialised}", text, count=1)
        changed.append(f"registry_only_fulltext_declarations_baseline={len(registry_only)}")

    unread = state.get("unread_premises")
    if unread is not None and UNREAD_BASELINE.search(text):
        text = UNREAD_BASELINE.sub(lambda m: f"{m.group(1)}{len(unread)}", text, count=1)
        if UNREAD_MEASURED.search(text):
            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            text = UNREAD_MEASURED.sub(lambda m: f"{m.group(1)}{today}", text, count=1)
        changed.append(f"unread_premise_baseline={len(unread)}")

    path.write_text(text, encoding="utf-8")
    return changed


# --------------------------------------------------------------------------- policies

def evaluate(root: Path, disease: str) -> tuple[list[str], list[str], dict[str, Any]]:
    """Return (violations, improvements, live measurement)."""
    live = measure_all(root, disease)
    events = load_ledger(root / LEDGER_REL)
    chain_errors = verify_chain(events)
    if chain_errors:
        return ([f"LEDGER_CHAIN_BROKEN: {error}" for error in chain_errors], [], live)

    # The chain alone cannot catch tampering with the *last* event, because no successor
    # commits to its digest — and at bootstrap the last event is the only event. Rewriting
    # history to agree with a false live measurement would otherwise pass `check` silently.
    # The manifest tail anchor closes it, so `check` must consult it rather than leaving that
    # to a separate command nobody runs in the same breath. Found by mutation-testing this
    # module: the tamper test passed against the first implementation.
    anchor_errors = tail_anchor_errors(root, events)
    if anchor_errors:
        return ([f"LEDGER_TAIL_ANCHOR: {error}" for error in anchor_errors], [], live)

    state = tail_state(events)
    if state is None:
        return (["NO_ANCHOR: growth anchors have never been recorded; run `record --bootstrap`"],
                [], live)

    violations: list[str] = []
    improvements: list[str] = []

    anchored = state.get("structural") or {}
    for key in STRUCTURAL_KEYS:
        live_value = live["structural"][key]
        anchored_value = anchored.get(key)
        if anchored_value is None:
            violations.append(f"STRUCTURAL_UNANCHORED: {key} has never been recorded")
        elif live_value != anchored_value:
            direction = "grew" if live_value > anchored_value else "shrank"
            violations.append(
                f"STRUCTURAL_DRIFT: {key} {direction} {anchored_value} -> {live_value} with no "
                f"declared delta. A batch must record what it changed: "
                f"`growth_anchors.py record --batch <ID> --{key} "
                f"{live_value - anchored_value:+d}`")

    for key, label in (("registry_only_fulltext", "registry-only full-text declarations"),
                       ("unread_premises", "unread premises")):
        live_set = set(live[key])
        anchored_set = set(state.get(key) or [])
        new = live_set - anchored_set
        if new:
            violations.append(
                f"RATCHET_VIOLATION: {len(new)} new {label} ({', '.join(sorted(new))}). "
                f"This ratchet may only fall.")
        elif live_set < anchored_set:
            improvements.append(
                f"RATCHET_IMPROVED: {label} fell {len(anchored_set)} -> {len(live_set)}; "
                f"run `growth_anchors.py tighten` to re-anchor")

    return violations, improvements, live


# --------------------------------------------------------------------------- commands

def cmd_measure(root: Path, disease: str, _args) -> int:
    live = measure_all(root, disease)
    print(json.dumps(live, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


def cmd_check(root: Path, disease: str, _args) -> int:
    violations, improvements, live = evaluate(root, disease)
    counts = live["structural"]
    print(f"structural: " + " · ".join(f"{k}={counts[k]}" for k in STRUCTURAL_KEYS)
          + f" | registry_only={len(live['registry_only_fulltext'])}"
          + f" | unread_premises={len(live['unread_premises'])}")
    for item in improvements:
        print(f"  [IMPROVED] {item}")
    for item in violations:
        print(f"  [BLOCK] {item}")
    if violations:
        print("VERDICT: BLOCK — growth anchors disagree with the live model")
        return 1
    print("VERDICT: PASS — every growth anchor matches what the tool measured")
    return 0


def cmd_record(root: Path, disease: str, args) -> int:
    live = measure_all(root, disease)
    events = load_ledger(root / LEDGER_REL)
    state = tail_state(events)

    if args.bootstrap:
        if state is not None:
            print("REFUSED: anchors already exist; --bootstrap is for the first record only")
            return 2
        event = append_event(root, disease, "bootstrap", live,
                             args.note or "initial anchor of the live measurement", args.batch)
        changed = reanchor_manifest(root, disease)
        print(f"RECORDED: {event['event_id']}")
        print("ANCHORED: " + ", ".join(changed))
        return 0

    if state is None:
        print("REFUSED: no anchor exists yet; run with --bootstrap first")
        return 2

    anchored = state.get("structural") or {}
    declared = {key: getattr(args, key) for key in STRUCTURAL_KEYS}
    if all(value is None for value in declared.values()):
        print("REFUSED: declare the structural delta this batch made, e.g. --claims +4. "
              "A recorder that accepts silence is a recorder that anchors anything.")
        return 2

    mismatches = []
    for key in STRUCTURAL_KEYS:
        want = declared[key] or 0
        observed = live["structural"][key] - anchored.get(key, 0)
        if want != observed:
            mismatches.append(f"{key}: declared {want:+d}, registries show {observed:+d}")
    if mismatches:
        print("REFUSED: the declared delta does not match the registries.")
        for item in mismatches:
            print(f"  {item}")
        print("Fix the declaration or the registries — this recorder will not anchor a "
              "number nobody earned.")
        return 1

    if not args.batch:
        print("REFUSED: --batch is required; an anchor with no batch cannot be audited")
        return 2

    anchors = {"structural": live["structural"]}
    # Ratchets ride along so history stays complete, but only when they did not worsen;
    # a worsening ratchet is a violation and must not be laundered through a counts record.
    for key in ("registry_only_fulltext", "unread_premises"):
        if set(live[key]) - set(state.get(key) or []):
            print(f"REFUSED: {key} grew. Resolve the ratchet violation before recording "
                  f"structural growth — see `growth_anchors.py check`.")
            return 1
        anchors[key] = live[key]

    note = args.note or "structural growth declared by " + args.batch
    event = append_event(root, disease, "batch", anchors, note, args.batch)
    changed = reanchor_manifest(root, disease)
    print(f"RECORDED: {event['event_id']}")
    print("ANCHORED: " + ", ".join(changed))
    return 0


def cmd_tighten(root: Path, disease: str, args) -> int:
    """Re-anchor a ratchet that fell. The only direction this tool moves without a declaration.

    Tightening is unconditionally safe: it makes the constraint stricter, so an attacker gains
    nothing and an honest session gains not having to remember a number. Loosening is
    impossible by construction — there is no command for it.
    """
    violations, improvements, live = evaluate(root, disease)
    blocking = [item for item in violations if item.startswith("RATCHET_VIOLATION")]
    if blocking:
        for item in blocking:
            print(f"  [BLOCK] {item}")
        print("REFUSED: a ratchet grew. Tightening cannot paper over a violation.")
        return 1
    if not improvements:
        print("NOTHING TO TIGHTEN: both ratchets already match the live measurement")
        return 0
    events = load_ledger(root / LEDGER_REL)
    state = tail_state(events) or {}
    anchors = {key: live[key] for key in ("registry_only_fulltext", "unread_premises")}
    if state.get("structural"):
        anchors["structural"] = state["structural"]
    event = append_event(root, disease, "tighten", anchors,
                         args.note or "; ".join(improvements), args.batch)
    changed = reanchor_manifest(root, disease)
    for item in improvements:
        print(f"  [IMPROVED] {item}")
    print(f"RECORDED: {event['event_id']}")
    print("ANCHORED: " + ", ".join(changed))
    return 0


def tail_anchor_errors(root: Path, events: list[dict[str, Any]]) -> list[str]:
    """Compare the manifest's declared tail against the ledger's real one.

    A hash chain detects a rewritten *historical* event because every successor commits to it.
    It cannot detect a rewritten *last* event, and at bootstrap the last event is the only
    one. This is the check that closes that gap, and it belongs to both `check` and `verify`.
    """
    manifest_text = (root / MANIFEST_REL).read_text(encoding="utf-8")
    declared_events = ANCHOR_EVENTS.search(manifest_text)
    declared_head = ANCHOR_HEAD.search(manifest_text)
    errors: list[str] = []
    if not declared_events or not declared_head:
        return ["state manifest declares no growth_anchor_events/growth_anchor_head"]
    if declared_events.group(2) != str(len(events)):
        errors.append(
            f"manifest says {declared_events.group(2)} events, ledger holds {len(events)}")
    expected_head = ledger_head(events) or "null"
    if declared_head.group(2) != expected_head:
        errors.append(f"manifest head {declared_head.group(2)} != ledger head {expected_head}")
    return errors


def cmd_verify(root: Path, disease: str, _args) -> int:
    events = load_ledger(root / LEDGER_REL)
    errors = verify_chain(events) + [
        f"tail anchor: {item}" for item in tail_anchor_errors(root, events)]
    if errors:
        for error in errors:
            print(f"  [BLOCK] {error}")
        print("VERDICT: BLOCK")
        return 1
    print(f"OK: {len(events)} chained growth-anchor event(s), tail anchored in "
          f"{MANIFEST_REL}")
    return 0


def cmd_anchor(root: Path, disease: str, _args) -> int:
    changed = reanchor_manifest(root, disease)
    print("ANCHORED: " + ", ".join(changed))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default=str(REPO_ROOT))
    parser.add_argument("--disease", default="wwox")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("measure", help="print the live measurement, write nothing")
    sub.add_parser("check", help="compare live against the anchors")
    sub.add_parser("verify", help="chain-verify the ledger and its manifest tail anchor")
    sub.add_parser("anchor", help="re-anchor the manifest to the ledger tail")

    record = sub.add_parser("record", help="anchor declared structural growth")
    record.add_argument("--batch", help="BATCH_COMMIT identifier")
    record.add_argument("--note")
    record.add_argument("--bootstrap", action="store_true",
                        help="first anchor only; adopts the live measurement")
    for key in STRUCTURAL_KEYS:
        record.add_argument(f"--{key}", type=int, default=None,
                            help=f"declared change in {key}, e.g. +4")

    tighten = sub.add_parser("tighten", help="re-anchor a ratchet that fell")
    tighten.add_argument("--batch")
    tighten.add_argument("--note")
    return parser


COMMANDS = {
    "measure": cmd_measure,
    "check": cmd_check,
    "record": cmd_record,
    "tighten": cmd_tighten,
    "verify": cmd_verify,
    "anchor": cmd_anchor,
}


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()
    try:
        return COMMANDS[args.command](root, args.disease, args)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
