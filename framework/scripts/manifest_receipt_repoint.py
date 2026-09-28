#!/usr/bin/env python3
"""Repair ONE deep-dive manifest's `receipt` field to the value the ledger derives — or refuse.

🔴 WHY THIS EXISTS
------------------
On 2026-09-28 the protocol DECIDED what a manifest's `receipt` means — the ledger event that
PRODUCED the manifest, precisely the EARLIEST same-study event whose `outputs` name that manifest
file — and `manifest_receipt_provenance.py` began CHECKING conformance: 116 manifests, 97
`CONFORMS`, 17 non-conforming, under a declared ceiling. The same commit had to state, in the
protocol and in the checker's own output, that **nothing in the repository could repair one**:
`rechain --repoint-manifests` only moves a `receipt` that is the OLD side of a `--rename` and is
expressly forbidden as a way to *decide* a target; a `receipt_correction` is ledger-side and
`require_work_manifest` returns early for it; nothing else writes the field. And a manifest is not
hand-edited — its `source_artifacts` are fingerprinted and its locators are verified against them.

A decided semantics with a check and no writer leaves exactly one route open, which is the hand
edit the repository forbids. This tool is the missing writer. It is modelled on
`scoped_record_edit.py`, which exists for this shape of problem — a narrow authorized edit made
EXECUTABLE rather than merely careful — and whose own docstring records that its assertion caught
its author's first attempt. The `"receipt": "<old>"` needle and the exactly-once rule are taken
from `fulltext_receipts.repoint_manifests`, the one pre-existing writer of this field.

🔴 IT DERIVES THE TARGET. THERE IS NO `--to`.
---------------------------------------------
A caller-supplied target is how a wrong value gets in — it is how `FTR-20260921-42589397-01` got
in, and it is what `--repoint-manifests` is forbidden to do. So this tool takes a PMID and nothing
else about the value: the new value comes from `manifest_receipt_provenance.assess`, the SAME
function the check uses, so the writer cannot drift from the checker. If the derivation is not
unique, or not possible, the tool refuses and names what is missing.

🔴 WHAT IT REFUSES (each one is a class the ledger cannot settle, not a caller inconvenience)
---------------------------------------------------------------------------------------------
  * more or fewer than one manifest for the PMID, or a manifest that is not readable JSON
  * a manifest with no `receipt` key: this tool SUBSTITUTES a value, it never adds a key. A
    manifest missing the field is refused by `deepdive_manifest.py` already, and the fix belongs
    to whatever writes the manifest.
  * `CONFORMS` — there is nothing to repair, and rewriting a correct field is how a correct field
    becomes a wrong one.
  * `UNCHECKABLE` and `UNKNOWN_EVENT` with no naming event — no same-study event names the
    manifest, so the ledger holds no producer to point at. An append-only ledger is not rewritten
    to manufacture one.
  * a derivation that is not unique: the earliest naming event by APPEND order and the earliest by
    `event_at` disagree. "Earliest" then means two different events, and a tool that picks one is
    deciding, not deriving.
  * 🔴 **artifact divergence.** `require_work_manifest` binds a receipt's
    `source_locator`/`source_fingerprint` to the manifest's own `source_artifacts` at append time.
    If the derived event fingerprints an artifact the manifest does not declare, re-pointing would
    produce a manifest whose `receipt` names a reading of a *different document* — coherent with
    the check and incoherent with the binding the repository already enforces. Measured
    2026-09-28: five of the thirteen `NOT_THE_PRODUCER` manifests are in exactly this state,
    because a later, deeper reading rewrote a manifest an earlier reading had created. That is a
    second decision (which reading does the manifest DESCRIBE), not a mechanical repoint, so it is
    refused rather than waived — there is deliberately no flag for it.
  * a `"receipt": "<old>"` needle that does not occur exactly once in the raw text
  * any pre-write assertion that the substitution touches more than the one field

🔴 EVERY OTHER BYTE SURVIVES IDENTICAL — ASSERTED BEFORE, PROVEN AFTER
----------------------------------------------------------------------
Before writing: the raw text is split at the single needle, both sides must be byte-identical to
the original's, and the parsed objects must differ in the key `receipt` and in nothing else.
After writing: the file is re-read FROM DISK and both assertions are re-made against the bytes
that are actually there; `assess` must now return `CONFORMS`; and `deepdive_manifest` must not
report an error it did not already report before the repair (a pre-existing error is not the
repair's, and rolling back on it would make the tool unusable on exactly the manifests that need
it). On any post-condition failure the original bytes go back and the exit code is 2.

WHAT PINS A MANIFEST'S BYTES — the survey behind the post-conditions
---------------------------------------------------------------------
Nothing digests a manifest. There is no anchor, no sealed baseline and no ledger field carrying a
manifest's SHA-256; a receipt's `outputs` name the manifest as a PATH plus prose. What does bind:

  * `require_work_manifest` → `source_artifacts` (path + sha256) against the receipt's
    `source_locator`/`source_fingerprint`, for a NEW `complete_fulltext_read` append. It never
    reads the manifest's `receipt` field, so the repair cannot disturb it — and the artifact-
    divergence refusal above keeps the repair from contradicting it either.
  * `deepdive_manifest.py` requires `receipt` to be PRESENT and checks nothing about its target
    (that is what `manifest_receipt_provenance.py` was written for), so validation is unmoved.
  * the locators are verified against `source_artifacts`, not against `receipt`.
  * three committed derived surfaces declare the manifest directory among their inputs —
    `coverage_report.md`, `batch_queue.md`, `pathograph_inventory.md` — so `candidate_tree_freshness.py`
    will RUN their freshness checks on any landing that carries this repair. None of the three emits
    a receipt identifier, so they are expected FRESH; that is a claim to verify, not to assume, and
    the tool prints the command.

Point-of-use PROSE is the one thing a repair does leave stale, and prose is not a check: records
and reviews that say the field "still names <old>" become wrong the moment it does not. So a
successful run lists every tracked file naming the old identifier, and says plainly that a
canonical registry sentence moves only through `BATCH_COMMIT`.

    python3 framework/scripts/manifest_receipt_repoint.py --pmid 42589397           # dry run
    python3 framework/scripts/manifest_receipt_repoint.py --pmid 42589397 --apply
    python3 framework/scripts/manifest_receipt_repoint.py --pmid 42589397 --json

Exit codes: 0 success or clean dry run · 1 refusal (nothing written) · 2 tool error (a
post-condition failed and the original bytes were restored).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import manifest_receipt_provenance as provenance  # noqa: E402

REFUSAL = 1
TOOL_ERROR = 2

#: Verdicts this tool can act on. Everything else is a refusal, named in `refuse_reason`.
REPAIRABLE = ("NOT_THE_PRODUCER", "UNNAMED")


class Refusal(Exception):
    """A scope or derivation violation. Nothing has been written when this is raised."""


class PostCondition(Exception):
    """A post-write proof failed. The original bytes have been restored."""


def needle(value: str) -> str:
    """The exact text `fulltext_receipts.repoint_manifests` matches, and for the same reason."""
    return f'"receipt": "{value}"'


def event_index(events: list[dict]) -> dict[str, dict]:
    return {str(event.get("event_id") or ""): event for event in events}


def derive(manifest_path: Path, events: list[dict]) -> tuple[str, str, provenance.Finding]:
    """(old, new, finding) — or raise Refusal. The value comes from the checker, never a caller."""
    finding = provenance.assess(manifest_path, events)
    if not finding.declared:
        raise Refusal(
            f"{manifest_path.name} declares no `receipt` ({finding.verdict}). This tool "
            "substitutes a value and never adds a key; a manifest missing the field is already "
            "refused by deepdive_manifest.py, and the fix belongs to whatever writes the manifest")
    if finding.verdict == "CONFORMS":
        raise Refusal(
            f"{manifest_path.name} CONFORMS: `receipt` already names {finding.declared}, the "
            "earliest same-study event whose outputs name this manifest. Rewriting a correct "
            "field is how a correct field becomes a wrong one")
    if finding.verdict not in REPAIRABLE or not finding.should_be:
        raise Refusal(
            f"{manifest_path.name} is {finding.verdict}: no same-study ledger event names this "
            "manifest among its outputs, so the ledger holds no producer to point at. An "
            "append-only ledger is not rewritten to manufacture one — this is a different defect "
            "(a manifest no recorded reading declares having produced) and needs a receipt, not "
            "a repoint")

    order = {str(event.get("event_id") or ""): position
             for position, event in enumerate(events)}
    known = event_index(events)
    by_event_at = sorted(
        finding.naming,
        key=lambda item: (str(known[item].get("event_at") or ""), order[item]))
    if by_event_at[0] != finding.should_be:
        raise Refusal(
            f"{manifest_path.name}: the derivation is not unique. The earliest naming event by "
            f"APPEND order is {finding.should_be} and by event_at it is {by_event_at[0]}. "
            "'Earliest' then names two different events, and a tool that picks one is deciding, "
            "not deriving")

    declared_digests = {
        str(item.get("sha256") or "")
        for item in (json.loads(manifest_path.read_text(encoding="utf-8"))
                     .get("source_artifacts") or [])
        if isinstance(item, dict) and str(item.get("sha256") or "")}
    target_digest = str(known[finding.should_be].get("source_fingerprint") or "")
    if declared_digests and target_digest and target_digest not in declared_digests:
        raise Refusal(
            f"{manifest_path.name}: ARTIFACT DIVERGENCE. The derived producer "
            f"{finding.should_be} fingerprints {target_digest[:12]}…, which this manifest does "
            f"not declare among its source_artifacts ({', '.join(sorted(d[:12] + '…' for d in declared_digests))}). "
            "require_work_manifest binds a receipt's source_locator/source_fingerprint to those "
            "artifacts, so re-pointing here would name a reading of a different document. Which "
            "reading the manifest DESCRIBES is a second decision, not a mechanical repoint, and "
            "there is deliberately no flag to waive it")

    return finding.declared, finding.should_be, finding


def substitute(text: str, old: str, new: str) -> str:
    """The one-field substitution, with the exactly-once rule and the byte-identity assertion."""
    if old == new:
        raise Refusal("the derived value equals the declared one; there is nothing to repair")
    target = needle(old)
    occurrences = text.count(target)
    if occurrences != 1:
        raise Refusal(
            f"expected exactly one {target}, found {occurrences}; refusing to guess which "
            "occurrence names the reading")
    head, _, tail = text.partition(target)
    after = head + needle(new) + tail
    # The pre-write proof, stated as arithmetic rather than as intention: the bytes before and
    # after the one needle are the original's, and the substitution is the whole difference.
    a_head, a_sep, a_tail = after.partition(needle(new))
    if not a_sep or a_head != head or a_tail != tail:
        raise Refusal("the substitution would move bytes outside the `receipt` value")
    if after.replace(needle(new), target, 1) != text:
        raise Refusal("the substitution is not reversible byte-for-byte; refusing")
    before_object = json.loads(text)
    after_object = json.loads(after)
    changed = sorted(key for key in set(before_object) | set(after_object)
                     if before_object.get(key) != after_object.get(key))
    if changed != ["receipt"]:
        raise Refusal("the substitution would change more than `receipt`: "
                      + ", ".join(changed or ["nothing"]))
    if after_object["receipt"] != new:
        raise Refusal("the parsed `receipt` is not the derived value; refusing")
    return after


def validation_errors(root: Path, disease: str, pmid: str) -> list[str]:
    """`deepdive_manifest`'s own verdict, without artifact re-hashing.

    `files/` is gitignored, so a checkout usually does not hold the fingerprinted artifact and
    `verify_artifacts=True` would fail for a reason the repair did not cause. The comparison that
    matters here is before-versus-after on the SAME setting.
    """
    try:
        import deepdive_manifest
    except ImportError as error:  # pragma: no cover - validator absent
        raise PostCondition(f"deepdive_manifest validator unavailable: {error}") from error
    errors, _ = deepdive_manifest.load_and_validate(
        root.resolve(), disease, pmid, verify_artifacts=False, require_current_schema=False)
    return list(errors)


def stale_prose(root: Path, old: str) -> list[str]:
    """Tracked files naming the old identifier — prose a repair leaves behind, not a check."""
    try:
        found = subprocess.run(["git", "-C", str(root), "grep", "-l", "-F", old],
                               capture_output=True, text=True, check=False)
    except OSError:
        return []
    return sorted(line for line in found.stdout.split("\n") if line.strip())


def repoint(root: Path, disease: str, pmid: str, *, apply: bool) -> dict:
    directory = provenance.manifest_dir(root, disease)
    if not directory.is_dir():
        raise Refusal(f"missing manifest directory: {directory}")
    matches = sorted(directory.glob(f"PMID{pmid}.json"))
    if len(matches) != 1:
        raise Refusal(f"{len(matches)} manifest(s) match PMID{pmid}.json; this tool repairs one")
    manifest_path = matches[0]
    try:
        original = manifest_path.read_text(encoding="utf-8")
        json.loads(original)
    except (OSError, json.JSONDecodeError) as error:
        raise Refusal(f"{manifest_path.name} is not readable JSON: {error}") from error

    events = provenance.load_events(provenance.ledger_path(root, disease))
    old, new, finding = derive(manifest_path, events)
    repaired = substitute(original, old, new)

    proof = {
        "manifest": manifest_path.name,
        "pmid": pmid,
        "verdict_before": finding.verdict,
        "declared": old,
        "derived": new,
        "derived_from": "earliest same-study ledger event whose outputs name this manifest",
        "naming_events": finding.naming,
        "bytes_before": len(original.encode("utf-8")),
        "bytes_after": len(repaired.encode("utf-8")),
        "changed_keys": ["receipt"],
        "applied": False,
    }
    if not apply:
        proof["freshness_check_owed"] = (
            "python3 framework/scripts/candidate_tree_freshness.py --paths "
            f"disease-models/{disease}/research/deepdive_manifests/{manifest_path.name}")
        return proof

    before_errors = validation_errors(root, disease, pmid)
    manifest_path.write_text(repaired, encoding="utf-8")
    try:
        persisted = manifest_path.read_text(encoding="utf-8")
        if persisted != repaired:
            raise PostCondition("the bytes on disk are not what the substitution produced")
        if persisted.replace(needle(new), needle(old), 1) != original:
            raise PostCondition(
                "the file on disk differs from the original in more than the `receipt` value")
        after = provenance.assess(manifest_path, events)
        if after.verdict != "CONFORMS":
            raise PostCondition(f"after the repair the manifest is {after.verdict}, not CONFORMS")
        new_errors = [item for item in validation_errors(root, disease, pmid)
                      if item not in before_errors]
        if new_errors:
            raise PostCondition("deepdive_manifest reports an error the repair introduced: "
                                + "; ".join(new_errors))
    except PostCondition:
        manifest_path.write_text(original, encoding="utf-8")
        raise

    proof["applied"] = True
    proof["verdict_after"] = "CONFORMS"
    proof["preexisting_validation_errors"] = before_errors
    proof["stale_point_of_use_prose"] = stale_prose(root, old)
    proof["freshness_check_owed"] = (
        "python3 framework/scripts/candidate_tree_freshness.py --paths "
        f"disease-models/{disease}/research/deepdive_manifests/{manifest_path.name}")
    return proof


def render(proof: dict) -> str:
    lines = [
        f"{proof['manifest']} · {proof['verdict_before']} → "
        + ("CONFORMS (APPLIED)" if proof["applied"] else "CONFORMS (dry run)"),
        f"  declared  {proof['declared']}",
        f"  derived   {proof['derived']}",
        f"  because   {proof['derived_from']}",
        f"  names it  {', '.join(proof['naming_events']) or '—'}",
        f"  bytes     {proof['bytes_before']} → {proof['bytes_after']} "
        f"(changed keys: {', '.join(proof['changed_keys'])})",
    ]
    if proof["applied"]:
        stale = proof.get("stale_point_of_use_prose") or []
        lines.append("  APPLIED. Every other byte proven identical against the file on disk.")
        if proof.get("preexisting_validation_errors"):
            lines.append("  pre-existing validation errors, not this repair's: "
                         + "; ".join(proof["preexisting_validation_errors"]))
        if stale:
            lines.append(f"  🔴 {len(stale)} tracked file(s) still name the old identifier in "
                         "prose — a repair moves the field, not the sentences about it:")
            lines += [f"      {item}" for item in stale]
            lines.append("      A canonical registry sentence moves only through BATCH_COMMIT; "
                         "route it, do not edit it here.")
        lines.append("  Lower the ceiling in manifest_receipt_provenance.py in the SAME commit, "
                     "and run:")
    else:
        lines.append("  DRY RUN — nothing written. Re-run with --apply.")
        lines.append("  Before landing, run:")
    lines.append(f"      {proof['freshness_check_owed']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--pmid", required=True, help="the ONE manifest to repair, by its PMID")
    parser.add_argument("--apply", action="store_true",
                        help="without this the run is a dry run and writes nothing")
    parser.add_argument("--json", action="store_true")
    arguments = parser.parse_args(argv)

    try:
        proof = repoint(arguments.root, arguments.disease, arguments.pmid, apply=arguments.apply)
    except Refusal as refusal:
        print(f"REFUSED: {refusal}", file=sys.stderr)
        return REFUSAL
    except PostCondition as failure:
        print(f"TOOL ERROR: {failure}. The original bytes were restored.", file=sys.stderr)
        return TOOL_ERROR
    except SystemExit as exit_error:  # provenance raises SystemExit on a missing ledger
        print(f"TOOL ERROR: {exit_error}", file=sys.stderr)
        return TOOL_ERROR

    print(json.dumps(proof, ensure_ascii=False, indent=1) if arguments.json else render(proof))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
