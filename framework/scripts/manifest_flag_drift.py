#!/usr/bin/env python3
"""Detect a deep-dive manifest flag that IMPROVED without the work behind it.

Why this exists
---------------
On 2026-09-09, minting the receipt for PMID 38499540, `scientist-b` edited that paper's
manifest and — in the same edit that corrected `references_enumerated` from 55 to 73 by
element count — flipped ``multihop.performed`` from ``false`` to ``true``. No multi-hop
expansion had been performed that wave. Correcting a count is not an expansion.

**Nothing in this repository would have caught it.** `deepdive_manifest.py` checks that a
key is PRESENT and that its shape is right; it has no opinion about whether the value is
EARNED, and it cannot have one, because it sees a single manifest at a single instant. The
strict validator returned PASS on the manifest carrying the flipped flag, twice.

The defect was found by the session self-evaluation, by a human-style re-read, before any
closing report was written. That is the protocol working — and it is also exactly the kind
of catch that should not depend on the author being conscientious twice in a row.

What it measures
----------------
A manifest's own git history. For each *declared-effort flag* it reports a **monotonic
self-improvement**: a value that moved in the direction that claims more work was done,
between two consecutive revisions of the same file. Each finding is annotated with whether
the author wrote anything in that block in the same edit (`· noted`).

It annotates rather than suppresses, and that was learned the hard way — twice, on this same
manifest. A first version stayed silent whenever a note EXISTED in the block, and a month-old
note about reference numbering silenced the very edit the tool was written for. A second
version required the note to be NEW or CHANGED in that revision, and the motivating commit
had changed one — about the reference count, not about the flag. Both versions returned PASS
on the case they existed to catch. No string test can decide whether a note is ABOUT a flag,
so the design changed instead of the threshold.

Effort flags move in one direction when work is genuinely done. That asymmetry is the whole
signal: a flag going ``false -> true`` asserts new effort, so it must be accompanied by the
evidence of that effort or by a note saying why it was already true. A flag going
``true -> false`` is a retraction and is never reported — retracting an unearned claim is
the behaviour this tool exists to encourage, and flagging it would punish the fix.

What it deliberately does NOT do
--------------------------------
It does not fail a build, block a commit or edit anything. It is read-only and advisory.
A drift finding is a QUESTION for the author — "you claimed more effort in this edit; where
is it?" — and there are legitimate answers: the work was done in the same session, or the
flag was wrong before. Both are cheap to write down, and writing them down is the point.

It also does not judge whether a note is about the flag. It shows what changed and who wrote
what; a reader decides. Overreaching there is how an advisory tool earns the habit of being
ignored.

Disease- and gene-agnostic: it reads any manifest under any disease model, and knows nothing
about WWOX.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

# Flags whose "true" asserts that a unit of work was performed. `verbatim_locators.waived`
# is inverted: waiving is the ADMISSION, so un-waiving (true -> false) is the improvement.
EFFORT_FLAGS: tuple[tuple[str, str, bool], ...] = (
    ("multihop", "performed", False),
    ("group_assessment", "performed", False),
    ("field_density", "performed", False),
    ("corpus_crossquery", "performed", False),
    ("retraction_check", "performed", False),
    ("verbatim_locators", "waived", True),
)

# A note anywhere in the same block whose key contains one of these is taken as the author
# acknowledging the change. Deliberately generous: the goal is to prompt a sentence, not to
# police its wording.
NOTE_HINTS = ("note", "correction", "why", "reason", "performed_note", "evidence")


def _git(root: Path, *args: str) -> str:
    out = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True, text=True, check=False)
    if out.returncode != 0:
        return ""
    return out.stdout


def revisions(root: Path, rel: str, limit: int) -> list[str]:
    """Commits touching this manifest, newest first."""
    raw = _git(root, "log", f"-n{limit}", "--format=%H", "--", rel)
    return [line.strip() for line in raw.splitlines() if line.strip()]


def manifest_at(root: Path, rev: str, rel: str) -> dict | None:
    raw = _git(root, "show", f"{rev}:{rel}")
    if not raw.strip():
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def _block(manifest: dict, block: str) -> dict:
    value = manifest.get(block)
    return value if isinstance(value, dict) else {}


def _notes(block: dict) -> dict[str, str]:
    """Note-ish keys with non-empty string values, as a comparable mapping."""
    return {
        key: value for key, value in block.items()
        if isinstance(value, str) and value.strip()
        and any(hint in key.lower() for hint in NOTE_HINTS)
    }


def _has_note(block: dict) -> bool:
    """Whether the block carries any note at all. Presence only — see `_acknowledged`."""
    return bool(_notes(block))


def _acknowledged(older: dict, newer: dict) -> bool:
    """Whether THIS revision added or changed a note in the block.

    🔴 Presence is not acknowledgement, and getting this wrong made the first version of
    this tool return PASS on the exact edit it was written to catch. The `multihop` block
    of `PMID38499540.json` already carried a long-standing `note` key, so a check for "is
    there a note here" was satisfied by prose written a month earlier about something else,
    and the flag flip sailed through. The tool passed its own unit tests and failed on the
    real history — the same shape as `<fig\\b` matching `<fig-count>`: a plausible predicate
    answering a different question from the one asked.

    An author acknowledging a change writes something NEW. So the note must have been added,
    or its text changed, in the same revision that moved the flag.
    """
    before, after = _notes(older), _notes(newer)
    return any(after[key] != before.get(key) for key in after)


def improvements(older: dict, newer: dict) -> list[str]:
    """Unacknowledged effort-flag improvements. Thin wrapper over `drifts`, kept because
    it is the predicate the regressions are written against."""
    return [text for text, noted in drifts(older, newer) if not noted]


def drifts(older: dict, newer: dict) -> list[tuple[str, bool]]:
    """Every effort-flag improvement, each paired with whether it was noted in this edit.

    🔴 This tool does NOT silence a drift because a note exists, and that is the second
    lesson the real data taught. Version 2 suppressed a finding whenever the same revision
    added or changed any note in the block — and the motivating edit did exactly that, in
    the same commit, about the REFERENCE COUNT rather than about the flag. So version 2 also
    returned PASS on the edit the tool exists to catch, for a subtler reason than version 1.

    No string test can decide whether a note is ABOUT a flag, and tightening one until it
    caught this case would have produced false positives that teach people to ignore the
    output. So the design changed instead of the threshold: **always surface the drift, and
    annotate whether the author wrote anything here in the same edit.** Suppression was the
    bug; annotation is the fix. The reader decides, which is what an advisory tool is for.
    """
    found: list[tuple[str, bool]] = []
    for block, flag, inverted in EFFORT_FLAGS:
        was = _block(older, block).get(flag)
        now = _block(newer, block).get(flag)
        if not isinstance(was, bool) or not isinstance(now, bool) or was == now:
            continue
        improved = (was and not now) if inverted else (not was and now)
        if not improved:
            continue
        noted = _acknowledged(_block(older, block), _block(newer, block))
        found.append((f"{block}.{flag}: {json.dumps(was)} -> {json.dumps(now)}", noted))
    return found


def scan(root: Path, rel: str, depth: int) -> list[tuple[str, bool]]:
    revs = revisions(root, rel, depth)
    findings: list[tuple[str, bool]] = []
    for newer_rev, older_rev in zip(revs, revs[1:]):
        newer = manifest_at(root, newer_rev, rel)
        older = manifest_at(root, older_rev, rel)
        if newer is None or older is None:
            continue
        for drift, noted in drifts(older, newer):
            subject = _git(root, "log", "-1", "--format=%s", newer_rev).strip()
            findings.append(
                (f"{rel} @ {newer_rev[:9]}  {drift}\n      commit: {subject}", noted))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--pmid", help="one PMID; default scans every manifest")
    parser.add_argument("--depth", type=int, default=25,
                        help="how many revisions back per manifest (default 25)")
    args = parser.parse_args()

    root = Path(args.workspace).resolve()
    base = Path("disease-models") / args.disease / "research" / "deepdive_manifests"
    if args.pmid:
        targets = [base / f"PMID{args.pmid}.json"]
    else:
        directory = root / base
        if not directory.is_dir():
            print(f"REFUSED: no manifest directory at {base}")
            return 2
        targets = sorted(base / p.name for p in directory.glob("PMID*.json"))

    findings: list[tuple[str, bool]] = []
    scanned = 0
    for rel in targets:
        if not (root / rel).is_file():
            print(f"REFUSED: no manifest at {rel}")
            return 2
        scanned += 1
        findings.extend(scan(root, rel.as_posix(), args.depth))

    unnoted = [text for text, noted in findings if not noted]
    for text, noted in findings:
        print(f"  [FLAG DRIFT{' · noted' if noted else ''}] {text}")
    print(f"manifests scanned: {scanned} | flag drifts: {len(findings)} "
          f"| unaccompanied by a note written in the same edit: {len(unnoted)}")
    if findings:
        print("VERDICT: FINDINGS — a declared-effort flag moved in the direction that claims "
              "more work. That is a QUESTION, not an accusation: point at the work, or put "
              "the flag back. A `· noted` drift means the author wrote something in that "
              "block in the same edit; whether it is ABOUT the flag is for a reader to judge, "
              "which is why it is shown rather than suppressed. Advisory; nothing is blocked.")
    else:
        print("VERDICT: PASS — no declared-effort flag improved in the scanned range")
    return 0


if __name__ == "__main__":
    sys.exit(main())
