#!/usr/bin/env python3
"""Re-seal the DisMech Phase-2 baseline against the current commit.

Re-sealing has a fixed shape — re-hash every declared input and output, re-point
`git_head_at_freeze` at HEAD, restate the revision — and it had been done by hand three
times. Each hand-run is an opportunity to hash the wrong file, miss one, or quietly widen
what is sealed. It is a procedure, so it is a script.

**Order matters and is enforced.** A baseline seals bytes that must already be committed:
run this *after* committing the change, then commit the baseline itself. If any declared
path is dirty or untracked, the seal would record bytes that git cannot recover, so this
refuses to write.

The set of sealed paths is never widened here. Adding an input is a deliberate edit to the
baseline, reviewed on its own; this tool only refreshes what is already declared.

🔴 **Absorbing a drift is a declared act.** A `sealed_scope` block's drift is *informational*
by design (`verify_phase2_baseline` does not fail on it, `scope_drift` reports it), so it can
stand for weeks — and a re-seal silently zeroes every such signal, including ones that belong
to somebody else's batch. That happened on 2026-09-27: BATCH_20260927_003 re-sealed for its own
`CLAIM 016` correction and absorbed a `PAPER 019` drift left standing by BATCH_20260927_001,
which it could only disclose in prose afterwards. So every drifted block must be **named** with
`--absorb`, or already acknowledged in `dismech_drift_acknowledgements.jsonl` against its
current digest; otherwise this refuses. A block you did not touch turning up in the refusal is
the finding the seal exists to produce.

`--revision` is required to write, for the same reason: the revision label is where the reason
for a re-seal is recorded, and writing without one leaves the previous batch's reason standing
over new bytes.

🔴 **The label must go UP, and the ordinal is what says so.** `--revision` was free text, and
the labels re-derived from git are not a sequence: `rev.7 → 12 → 7 → 12 → 7 → 8 → 9 → 15 → 16
→ 16 → 17 → 13 → 14 → 18`. A reader who sees `rev.14` on a baseline and `rev.17` in an older
commit cannot tell which seal is later, and nothing stopped the next writer from typing `rev.3`.
Three things close that, all of them here:

  - `revision_ordinal`, an integer, orders seals independently of how the label is spelled.
    It is parsed from `rev.N` in the label, or given outright with `--revision-ordinal`.
  - a refusal when the new ordinal does not EXCEED the stored one. Monotone, not merely
    distinct: a duplicate label (`rev.16` twice, 2026-08) is as unreadable as a lower one.
  - `revision_history`, appended on every write, so the note attached to the seal being
    replaced survives in the file. It did not before: `rev.17`'s substantive note — "extractor
    strips trailing block separators; per-block digests added" — is recoverable only from git,
    and `--history` re-derives exactly that, read-only, for the seals written before this field
    existed.

Nothing is rewritten retroactively: the labels already in git stay as they are, and the history
field starts at the first re-seal after 2026-09-28.

🔴 **THREE CONVENTIONS HAVE GOVERNED THIS LABEL, AND THE NEXT WRITER MUST NOT INVENT A FOURTH.**
The series below is not noise; it is three different rules applied in turn by different actors:

  1. **monotone-per-line** (2026-08-04, `rev.7 → 8 → 9`) — one counter per line of work, restarted
     whenever a new line began, which is why `rev.7` and `rev.12` each occur more than once;
  2. **reset-on-branch** (2026-08-04/06, `rev.12 → 7`, `rev.17 → 13`) — the label was carried over
     from whichever baseline the batch branched from, so it DESCENDS across a branch boundary;
  3. **highest-ever + 1** (2026-09-28, `rev.18`) — the only rule now permitted to write, and the
     one this tool enforces: the new ordinal must exceed the stored one.

Conventions 1 and 2 are history and are not re-applied. A label that would repeat or descend is
refused, so writing under convention 1 or 2 is no longer possible — which is the point.

🔴 **The ordinal is DERIVED, and ordering is never read off the spelling.** `revision_ordinal` is
parsed from `rev.N` ONCE, at the moment of the write, and from then on it is the stored integer
that orders seals. A reader who compares two labels as text is applying convention 3 to a series
written under three, and gets the wrong answer: `rev.14` (2026-09-27) is LATER than `rev.17`
(2026-08-07). `--history` derives the ordinals for the pre-2026-09-28 seals the only way they can
be derived — by parsing their labels out of git — and prints the rule it used beside them, so the
derivation is auditable rather than assumed.

🔴 **The count is a tool answer, not a grep.** The label history has been miscounted three times
by three different actors — 13, 15 and 16 — because three different things are countable: 16
commits touch the file, they carry 13 distinct label STRINGS, and the ordinal series has 16
entries with repeats. `--history` prints all of those numbers with the commits behind them, so the
next reader asks the tool instead of eyeballing `git log`.

Usage
-----
    reseal_dismech_baseline.py --check       # report what would change, and what it would refuse
    reseal_dismech_baseline.py --history     # every label this baseline has carried, from git
    reseal_dismech_baseline.py --revision "rev.19 (why)" --absorb "CLAIM 016"
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dismech_independent_protocol as protocol  # noqa: E402  (the scope reader lives there)

REPO = Path(__file__).resolve().parents[4]
BASELINE = REPO / "disease-models/wwox/analysis/data/dismech_phase2_baseline.json"


def _git(*arguments: str) -> str:
    result = subprocess.run(["git", *arguments], cwd=REPO, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"git {' '.join(arguments)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def _sha256(relative: str) -> str:
    return hashlib.sha256((REPO / relative).read_bytes()).hexdigest()


def _dirty(paths: list[str]) -> list[str]:
    """Paths with uncommitted or untracked content — bytes git could not recover."""
    status = _git("status", "--porcelain", "--", *paths)
    return [line[3:].strip() for line in status.splitlines() if line.strip()]


LABEL_ORDINAL = re.compile(r"(?i)\brev\.\s*(\d+)")


def label_ordinal(label: str | None) -> int | None:
    """The integer in a `rev.N` label, or None when the label does not carry one."""
    if not label:
        return None
    match = LABEL_ORDINAL.search(label)
    return int(match.group(1)) if match else None


def stored_ordinal(baseline: dict) -> int | None:
    """The ordinal of the seal now in the file: the field if present, else its label.

    The field did not exist before 2026-09-28, so the label is the fallback — and the live
    baseline's `rev.18` reads as 18 without any migration. A seal carrying neither is not
    ordered, and the caller must say what ordinal it is writing.
    """
    if isinstance(baseline.get("revision_ordinal"), int):
        return baseline["revision_ordinal"]
    return label_ordinal(baseline.get("revision"))


def next_ordinal(baseline: dict, label: str, given: int | None) -> tuple[int | None, str | None]:
    """(ordinal to write, refusal reason). A label that does not go up is refused."""
    previous = stored_ordinal(baseline)
    ordinal = given if given is not None else label_ordinal(label)
    if ordinal is None:
        return None, ("the revision label carries no `rev.N` ordinal and --revision-ordinal was "
                      "not given, so this seal could not be ordered against the previous one")
    if previous is None:
        return ordinal, None
    if ordinal <= previous:
        return None, (f"revision ordinal {ordinal} does not exceed the stored {previous} "
                      f"({baseline.get('revision', '')[:60]!r}…). A seal's label must go UP: the "
                      "label history is already non-monotone (rev.7 -> 12 -> 7 -> 12 -> 7 -> 8 "
                      "-> 9 -> 15 -> 16 -> 16 -> 17 -> 13 -> 14 -> 18) and a reader cannot tell "
                      f"which seal is later. Use rev.{previous + 1} or higher.")
    return ordinal, None


def history_entry(baseline: dict) -> dict:
    """The record of the seal being replaced, so its note survives this write."""
    return {"revision": baseline.get("revision"),
            "revision_ordinal": stored_ordinal(baseline),
            "frozen_at": baseline.get("frozen_at"),
            "git_head_at_freeze": baseline.get("git_head_at_freeze")}


CONVENTIONS = (
    ("monotone-per-line", "one counter per line of work, restarted when a new line began "
                          "(rev.7 -> 8 -> 9); this is why 7 and 12 each occur more than once"),
    ("reset-on-branch", "the label carried over from the baseline the batch branched from, so it "
                        "DESCENDS across a branch boundary (rev.12 -> 7, rev.17 -> 13)"),
    ("highest-ever + 1", "the only rule that may write today, and the one this tool enforces: the "
                         "new ordinal must EXCEED the stored one"),
)

DERIVATION_RULE = (
    "one row per COMMIT that touched the file (git log --follow), oldest first, with no "
    "deduplication by label; the ordinal of each row is the integer matched by "
    r"/\brev\.\s*(\d+)/ in that commit's `revision` string, which is how a pre-2026-09-28 seal's "
    "ordinal is recoverable at all. A commit whose blob does not parse as JSON, or whose label "
    "carries no rev.N, is printed with an ordinal of `-` and counted in `commits` only."
)


def label_series(relative: str) -> list[tuple[str, str, str | None, int | None]]:
    """(commit, date, label, ordinal) for EVERY commit that touched the file, oldest first.

    🔴 No deduplication. The version this replaced skipped a label it had already printed, so the
    two identical `rev.16` seals (2026-08-04 and 2026-08-06) collapsed into one row and the
    printed list had 13 entries against 16 commits — which is exactly how the history came to be
    counted as 13 by one actor, 15 by another and 16 by a third. Repeats ARE the finding here.
    """
    log = _git("log", "--follow", "--format=%H\t%ad", "--date=short", "--", relative).splitlines()
    rows: list[tuple[str, str, str | None, int | None]] = []
    for line in log:
        commit, _, date = line.partition("\t")
        blob = subprocess.run(["git", "show", f"{commit}:{relative}"], cwd=REPO,
                              capture_output=True, text=True)
        label: str | None = None
        if blob.returncode == 0:
            try:
                label = json.loads(blob.stdout).get("revision")
            except json.JSONDecodeError:
                label = None
        rows.append((commit, date, label, label_ordinal(label)))
    rows.reverse()
    return rows


def print_history(baseline: dict) -> int:
    """Every label this baseline has carried, the counts a reader keeps getting wrong, and the
    rule used to derive them — so the answer comes from the tool and not from a grep."""
    field = baseline.get("revision_history", [])
    print(f"revision_history field ({len(field)} superseded seal(s) recorded in the file; the "
          "field was added 2026-09-28, so earlier seals live only in git):")
    for entry in field:
        print(f"  [{entry.get('revision_ordinal')}] {entry.get('frozen_at')} "
              f"{str(entry.get('git_head_at_freeze'))[:9]} {entry.get('revision')}")
    if not field:
        print("  (none yet)")

    relative = BASELINE.relative_to(REPO).as_posix()
    rows = label_series(relative)
    print(f"\nevery commit that touched {relative}, OLDEST first:")
    for commit, date, label, ordinal in rows:
        mark = "" if ordinal is not None else "  <- no rev.N in the label"
        print(f"  {commit[:9]} {date} [{ordinal if ordinal is not None else '-'}] "
              f"{str(label)[:72]}{mark}")

    series = [ordinal for _c, _d, _l, ordinal in rows if ordinal is not None]
    labels = {label for _c, _d, label, _o in rows if label}
    print(f"\nordinal series, oldest -> newest: {' -> '.join(str(o) for o in series)}")
    print("THREE COUNTS, all correct, which is why this history has been miscounted three times "
          "(13, 15 and 16, by three different actors):")
    print(f"  commits touching the file      : {len(rows)}")
    print(f"  distinct label STRINGS         : {len(labels)}")
    print(f"  ordinals in the series         : {len(series)}"
          f" (highest ever {max(series) if series else '-'};"
          f" repeats {sorted({o for o in series if series.count(o) > 1})})")
    stored = stored_ordinal(baseline)
    print(f"  stored revision_ordinal now    : {stored}"
          f" -> the next seal must be rev.{(stored + 1) if stored is not None else '?'} or higher")
    print(f"\nDERIVATION RULE: {DERIVATION_RULE}")
    print("THE SERIES IS NOT NOISE — three conventions produced it, and only the third may write:")
    for name, description in CONVENTIONS:
        print(f"  - {name}: {description}")
    print("A label is never compared as TEXT to order two seals: rev.14 (2026-09-27) is later "
          "than rev.17 (2026-08-07). Ordering is the stored revision_ordinal, derived once at "
          "the write.")
    return 0


def undeclared_absorptions(baseline: dict, absorb: list[str]) -> list[str]:
    """Sealed blocks whose drift this re-seal would zero without anybody declaring it.

    A block qualifies as declared when it is named on the command line, or when the protocol's
    own drift log already carries an acknowledgement bound to the digest the registry holds NOW
    (`unresolved_drift` expires an acknowledgement the moment the block moves again, so an old
    one cannot license a new absorption).
    """
    named = set(absorb or ())
    pending = protocol.unresolved_drift(BASELINE, REPO)
    return sorted(item["block"] for item in pending
                  if item.get("block") not in named)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report, write nothing")
    parser.add_argument("--revision",
                        help="revision label to record (required to write). Its `rev.N` is "
                             "parsed ONCE, here, into the stored revision_ordinal, which must "
                             "exceed the stored one; from then on that integer orders seals and "
                             "no ordering is ever read off the spelling — rev.14 (2026-09-27) is "
                             "later than rev.17 (2026-08-07). Use --revision-ordinal when the "
                             "label does not spell rev.N")
    parser.add_argument("--revision-ordinal", type=int, default=None,
                        help="the integer that orders this seal, when the label does not spell "
                             "it as rev.N; it must still exceed the stored ordinal")
    parser.add_argument("--history", action="store_true",
                        help="print every label this baseline has carried (field + git) and exit")
    parser.add_argument("--absorb", action="append", metavar="BLOCK", default=[],
                        help="a sealed block whose drift THIS re-seal is meant to absorb, "
                             'e.g. --absorb "CLAIM 016"; repeatable')
    arguments = parser.parse_args()

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    if arguments.history:
        return print_history(baseline)
    # Validated BEFORE any hashing, and in --check too: a label the tool will refuse is better
    # learned while there is still time to choose another one than after the drift report.
    ordinal = None
    if arguments.revision or arguments.revision_ordinal is not None:
        ordinal, refusal = next_ordinal(baseline, arguments.revision or "",
                                        arguments.revision_ordinal)
        if refusal:
            print(f"REFUSED: {refusal}")
            return 2
    declared = [entry["path"] for entry in baseline["inputs"].values()]
    declared.append(baseline["output"]["path"])

    missing = [path for path in declared if not (REPO / path).exists()]
    if missing:
        raise SystemExit("declared path does not exist: " + ", ".join(missing))

    dirty = _dirty(declared)
    if dirty:
        print("REFUSED: declared paths are not committed, so the seal would record "
              "bytes git cannot recover:")
        for path in dirty:
            print(f"  - {path}")
        print("Commit them first, then re-seal, then commit the baseline.")
        return 2

    undeclared = undeclared_absorptions(baseline, arguments.absorb)
    if undeclared:
        print("REFUSED: this re-seal would absorb drift nobody declared, and an absorbed "
              "drift signal cannot be recovered:")
        for block in undeclared:
            print(f"  - {block}")
        print("Name each block this re-seal is MEANT to absorb:")
        print("  " + " ".join(f'--absorb "{block}"' for block in undeclared))
        print("A block you did not change is a finding: acknowledge it in "
              "dismech_drift_acknowledgements.jsonl (dismech_independent_protocol.py drift), "
              "or find out whose batch moved it, before you absorb it here.")
        return 2
    drifted = {item["block"] for item in protocol.scope_drift(BASELINE, REPO)}
    for block in arguments.absorb:
        if block not in drifted:
            print(f"note: --absorb {block!r} names a block that has not drifted")

    if not arguments.check and not arguments.revision:
        print("REFUSED: --revision is required to write. The revision label is where the "
              "reason for a re-seal lives; without one the previous reason would stand over "
              "new bytes.")
        return 2

    changes = []
    for name, entry in sorted(baseline["inputs"].items()):
        # An input sealed by a POLICY does not carry a whole-file `sha256`, and each policy
        # is re-sealed on its own terms. Before 2026-09-27 this loop assumed every input
        # carried a plain `sha256` and died with `KeyError: 'sha256'` on the first policy
        # entry, so the tool could not re-seal the baseline it exists for.
        policy = entry.get("verification_policy")
        if policy == "append_only_prefix":
            # A sealed prefix must never move. Nothing is re-sealed here; if the prefix has
            # changed, that is the incident the seal exists to surface, not bookkeeping.
            lines = (REPO / entry["path"]).read_bytes().splitlines(keepends=True)
            count = entry["prefix_event_count"]
            if len(lines) < count:
                raise SystemExit(f"{name}: {len(lines)} events, below the sealed prefix of "
                                 f"{count} — the ledger was truncated, which is an incident, "
                                 "not a re-seal")
            if hashlib.sha256(b"".join(lines[:count])).hexdigest() != entry["prefix_sha256"]:
                raise SystemExit(f"{name}: the sealed append-only prefix has moved — "
                                 "that is an incident, not a re-seal")
            # The whole-file `sha256` this entry still carries is NOT sealed under this policy
            # (`verify_phase2_baseline` never reads it for an append-only input) and is not
            # refreshed: an append-only ledger's whole-file hash is stale by construction the
            # next time anything is appended. Said out loud so the stale field is not read as
            # an authoritative one.
            if entry.get("sha256") and entry["sha256"] != _sha256(entry["path"]):
                print(f"note: {name} carries a whole-file sha256 that this policy does not "
                      "seal and this tool does not refresh")
            continue
        if policy == "sealed_scope":
            # The scope hashes MUST move with the anchor. `verify_phase2_baseline` treats
            # working-tree scope drift as information ("correction is the product"), but its
            # frozen half compares the declared hash against the blob AT `git_head_at_freeze`
            # — so a re-seal that moves the anchor and leaves the scope hash behind is
            # guaranteed to fail, which is what happened on 2026-09-27 when BATCH_20260927_003
            # corrected `CLAIM 016`. Re-derived here with the protocol's own scope reader, so
            # the sealed bytes are the declared blocks and never the whole file.
            text = (REPO / entry["path"]).read_text(encoding="utf-8")
            try:
                scope = protocol.registry_scope_bytes(text, entry["scope_blocks"])
            except ValueError as exc:
                raise SystemExit(f"{name}: a sealed block no longer resolves ({exc}) — a "
                                 "renamed or removed record is an incident, not a re-seal")
            current = hashlib.sha256(scope).hexdigest()
            if current != entry.get("scope_sha256"):
                changes.append(f"{name} scope: {str(entry.get('scope_sha256'))[:12]}… -> {current[:12]}…")
            entry["scope_sha256"] = current
            for block in entry["scope_blocks"]:
                one = hashlib.sha256(
                    protocol.registry_scope_bytes(text, [block])).hexdigest()
                if one != entry.get("scope_block_sha256", {}).get(block):
                    changes.append(f"{name} {block}: -> {one[:12]}…")
                entry.setdefault("scope_block_sha256", {})[block] = one
            continue
        current = _sha256(entry["path"])
        if current != entry["sha256"]:
            changes.append(f"{name}: {entry['sha256'][:12]}… -> {current[:12]}…")
        entry["sha256"] = current
    output_sha = _sha256(baseline["output"]["path"])
    if output_sha != baseline["output"]["sha256"]:
        changes.append(f"output: {baseline['output']['sha256'][:12]}… -> {output_sha[:12]}…")
    baseline["output"]["sha256"] = output_sha

    head = _git("rev-parse", "HEAD")
    if head != baseline.get("git_head_at_freeze"):
        changes.append(f"anchor: {str(baseline.get('git_head_at_freeze'))[:9]} -> {head[:9]}")

    if not changes:
        print("baseline already current — nothing to re-seal")
        return 0

    print(f"{len(changes)} change(s):")
    for change in changes:
        print(f"  {change}")
    if arguments.check:
        return 0

    # Captured BEFORE the anchor and timestamp move: a history entry written afterwards would
    # record the new seal's anchor against the old seal's label, which is worse than no history.
    superseded = history_entry(baseline)
    baseline["git_head_at_freeze"] = head
    baseline["frozen_at"] = datetime.datetime.now(
        datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if arguments.revision:
        # Append the seal being replaced before overwriting it, so its reason is still in the
        # file afterwards. Before this, every superseded label lived only in git history.
        baseline.setdefault("revision_history", []).append(superseded)
        baseline["revision"] = arguments.revision
        baseline["revision_ordinal"] = ordinal
    BASELINE.write_text(json.dumps(baseline, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    print(f"re-sealed on {head[:9]} — now commit the baseline itself")
    return 0


if __name__ == "__main__":
    sys.exit(main())
