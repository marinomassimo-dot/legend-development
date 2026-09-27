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

Usage
-----
    reseal_dismech_baseline.py --check       # report what would change
    reseal_dismech_baseline.py --revision "rev.7 (why)"
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report, write nothing")
    parser.add_argument("--revision", help="revision label to record")
    arguments = parser.parse_args()

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
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
            prefix = hashlib.sha256(b"".join(lines[:count])).hexdigest()
            if len(lines) < count or prefix != entry["prefix_sha256"]:
                raise SystemExit(f"{name}: the sealed append-only prefix has moved — "
                                 "that is an incident, not a re-seal")
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
            scope = protocol.registry_scope_bytes(text, entry["scope_blocks"])
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

    baseline["git_head_at_freeze"] = head
    baseline["frozen_at"] = datetime.datetime.now(
        datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if arguments.revision:
        baseline["revision"] = arguments.revision
    BASELINE.write_text(json.dumps(baseline, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    print(f"re-sealed on {head[:9]} — now commit the baseline itself")
    return 0


if __name__ == "__main__":
    sys.exit(main())
