#!/usr/bin/env python3
"""A commit hash written into a tracked record is written at full length, or the publication
gate can block on it.

🔴 WHAT THIS GUARDS, AND WHY IT IS NOT A PRIVACY RULE. `scripts/public_release_gate.py` hashes
every alphabetic run of 3–24 characters against a set of private-identifier digests, and skips
runs that sit inside a hexadecimal span of 32+ characters or a 12+ hex content-address fragment —
because the letters inside a digest are not a name. A **7-character abbreviated hash** is below
both thresholds, so a three-letter run that happens to fall inside one is evaluated as a word.

Measured on 2026-09-12: `ledger/tasks/orchestrator/ORCH-USE-TRIAL-20260912.json` carried a
7-character `started_at_head`, the gate returned `BLOCK_PUBLICATION` on that one line, and the
commit that shipped it asserted in its own message «gate PASS with 0 blocks». The block was then
removed by an unrelated actor as a side effect of rewriting the same field at full length — nobody
was auditing it. Reproduced by `ORCH-M4B-COST-20260912B` in an isolated worktree: one scratch file
carrying that abbreviation, `VERDICT: BLOCK_PUBLICATION`, `BLOCKS: 1`; file removed, gate `PASS`.

🔴 THIS DOES NOT WEAKEN THE GATE, AND THAT IS THE POINT. The alternative repair — exempting short
hex runs — would widen a privacy rule to make a bookkeeping habit convenient, and a 7-character
run carrying a real identifier is exactly what the rule is for. So the gate is untouched and the
INPUT is fixed: a full 40-character hash lands inside the existing digest exemption, is what `git
rev-parse` returns anyway, and is unambiguous for a reader. Expanding an abbreviation loses
nothing; it is the same commit spelled out.

The scope is deliberately narrow — the named commit-hash fields of the task records, where the
defect actually occurred. It is not a repository-wide ban on short hashes in prose.
"""

from __future__ import annotations

import json
import re
import subprocess
import unittest
from pathlib import Path

# parents[1] is `framework/`, not the repository root, and the population guard below caught
# exactly that on this file's first run: it looked under framework/ledger/tasks, found nothing,
# and refused rather than passing over an empty set. That is the guard working on its author.
ROOT = Path(__file__).resolve().parents[2]
TASKS = ROOT / "ledger" / "tasks"
HASH_FIELDS = ("started_at_head", "base_commit", "landed_at", "merged_at_head")
FULL_HASH = re.compile(r"^[0-9a-f]{40}$")
ABBREVIATED = re.compile(r"^[0-9a-fA-F]{4,39}$")


def task_records() -> list[Path]:
    return sorted(TASKS.rglob("*.json")) if TASKS.is_dir() else []


# 🔴 FORTY HEX CHARACTERS IS NOT A COMMIT. This file's first version checked length and alphabet
# only, and on the same day, in the same task, its author wrote a 40-character string into three
# records that RESOLVES TO NO OBJECT: it had been composed from the abbreviation `d3bc0fe` rather
# than resolved with `git rev-parse`. The guard passed it. An independent verifier caught it by
# trying to resolve it. So existence is checked here too, and only inside a real checkout — an
# exported release copy has no object database and must not fail for that reason.


def resolves(value: str) -> bool | None:
    """True/False inside a checkout with an object database; None where the question cannot be
    asked, which is not the same as a pass and is reported as a skip."""
    if not (ROOT / ".git").exists():
        return None
    try:
        done = subprocess.run(["git", "cat-file", "-e", f"{value}^{{commit}}"],
                              cwd=ROOT, capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    return done.returncode == 0


class ACommitHashInATaskRecordIsWrittenInFull(unittest.TestCase):

    def test_the_population_is_not_empty(self) -> None:
        """An empty population is a guard that checks nothing, which is the vacuous pass this
        file would otherwise arrive at on a day somebody moves the ledger."""
        self.assertTrue(task_records(), f"no task records found under {TASKS}")

    def test_every_named_hash_field_carries_forty_hex_characters(self) -> None:
        offenders: list[str] = []
        for path in task_records():
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                offenders.append(f"{path.relative_to(ROOT)}: not valid JSON ({exc})")
                continue
            if not isinstance(record, dict):
                continue
            for field in HASH_FIELDS:
                value = record.get(field)
                if not isinstance(value, str) or not value:
                    continue
                if FULL_HASH.match(value):
                    continue
                if ABBREVIATED.match(value):
                    offenders.append(
                        f"{path.relative_to(ROOT)}: `{field}` is {len(value)} characters. Write "
                        "the full 40-character hash — `git rev-parse` gives it — so the "
                        "publication gate's digest exemption covers it."
                    )
        self.assertEqual([], offenders, "\n".join(offenders))


    def test_every_full_hash_resolves_to_a_commit_that_exists(self) -> None:
        """A pointer that asserts a guarantee must resolve, or the guarantee is unverifiable."""
        unresolved: list[str] = []
        asked = 0
        for path in task_records():
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict):
                continue
            for field in HASH_FIELDS:
                value = record.get(field)
                if not isinstance(value, str) or not FULL_HASH.match(value):
                    continue
                verdict = resolves(value)
                if verdict is None:
                    continue
                asked += 1
                if not verdict:
                    unresolved.append(
                        f"{path.relative_to(ROOT)}: `{field}` = {value} resolves to no commit in "
                        "this repository. Forty hex characters is not a commit: resolve the value "
                        "with `git rev-parse` instead of composing it from an abbreviation."
                    )
        if not asked:
            self.skipTest("no object database here, so existence could not be asked")
        self.assertEqual([], unresolved, "\n".join(unresolved))


if __name__ == "__main__":
    unittest.main(verbosity=2)
