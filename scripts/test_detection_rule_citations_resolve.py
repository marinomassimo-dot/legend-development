#!/usr/bin/env python3
"""Every `D-nn` detection rule cited from a LIVE surface resolves to something a reader can open.

🔴 WHY THIS EXISTS
------------------
The `DEFAULTS THAT BIT US` table in `dismissal_ledger_current.md` is the repository's register of
defaults that turned out false here, and other surfaces cite its rows by number as detection
rules. On 2026-10-21 a Scientist allocating an id found that `D-31`, `D-33`, `D-35` and `D-36` are
cited as rules and exist in **no row** of the table — so `max(D-nn) + 1`, which the table's own
allocator note prescribes, would have collided with a live reference. It allocated `D-37` and
stated the deviation instead.

Harness Engineering then established the cause by measurement rather than from the batch records:
`git log -S'| **D-nn** |'` over the ledger returns **zero commits for every id from `D-27` to
`D-36`**. No such row was ever written. The ten ids were PROPOSED by seven commit candidates of
2026-09-22; the batches that adjudicated them allocated the next free numbers; three proposals were
minted under lower ids (`D-30`→`D-26`, `D-32`→`D-20`, `D-34`→`D-21`) and four were never minted at
all, because their candidates closed `PROPAGATED` with *"no operation list"* while the prose that
already cited the proposed number stayed. Nothing was lost. Nothing was renumbered after being
written. A reader following `D-31` simply arrives nowhere.

🔴 WHAT THIS IS, AND WHAT IT IS NOT
-----------------------------------
It is a **ratchet**, not a gate (`harness_development_principles.md` principle 3): it runs in under
a second, reports, waits on nobody, and will say the same informative thing at the thousandth
batch — *has anybody cited a detection rule that does not exist?* It does **not** demand that the
four be minted: minting a row in an append-only scientific ledger is a `BATCH_COMMIT` act by the
integrator, and this suite would be a gate on scientific work if it insisted. It holds the line
where it is:

  - a cited id that is a **row** of the table resolves;
  - a cited id the table's **allocator addendum** maps to a minted row resolves (the alias case);
  - a cited id the addendum declares **NEVER MINTED** is a known, declared debt;
  - anything else is a NEW dangling citation, and that is what turns this red.

The baseline lives in the ledger's own addendum table and not in this file, so the constraint is
maintained in the one place the content is (principle 5). When a `BATCH_COMMIT` mints one of the
four, the addendum row stops saying NEVER MINTED, the row appears, and this suite tightens by
itself with nothing to update here.

🔴 LIVE SURFACES ONLY, AND THE DISTINCTION IS THE WHOLE POINT
-------------------------------------------------------------
A commit candidate that PROPOSES `D-31`, and a session evaluation that records *"the proposed
`D-32`"*, are **correct** citations of their own dated act, and a check that flagged them would be
measuring history instead of the state of the repository. Only a surface a reader consults as
CURRENT is in scope. The population comes from `git ls-files`, for the reason
`test_tool_routing.py` states: a count whose denominator is whatever the pattern matched is not a
measurement.

Run: `python3 scripts/test_detection_rule_citations_resolve.py`
"""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "disease-models/wwox/research/dismissal_ledger_current.md"

# Directories whose files are DATED RECORDS of an act, never a current surface. A `D-` number in
# one of them is a citation to what that act proposed or decided on its date.
DATED_RECORD_PARTS = (
    "/analysis/", "/commit_candidates/", "/session_evaluations/", "/orchestration_reviews/",
    "/fulltext_dossiers/", "/receipt_staging/", "/page_adjudications/", "/deepdive_manifests/",
    "learning/", "reviews/", "ledger/",
    "governance/candidates/", "governance/decisions/", "governance/design_records/",
)

# `D-nn` as a citation: in backticks, or bold, or bold-with-backticks. Bare `D-31` in running prose
# is not matched, deliberately — the repository's own convention marks an id up, and a looser
# pattern would start matching dose labels and figure panels.
CITATION = re.compile(r"`(D-\d\d)`|\*\*`?(D-\d\d)`?\*\*")
MINTED_ROW = re.compile(r"^\|\s*\*\*(D-\d\d)\*\*\s*\|", re.M)
# A row of the allocator addendum's mapping table. The ids come from the first cell, the state from
# the second and the id it was minted as, if any, from the third.
ADDENDUM_ROW = re.compile(
    r"^\|\s*((?:`D-\d\d`(?:,\s*)?)+)\s*\|([^|]*)\|([^|]*)\|", re.M)


def tracked_markdown() -> list[str]:
    done = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT,
                          capture_output=True, text=True, check=True)
    return [line for line in done.stdout.splitlines() if line]


def is_live_surface(path: str) -> bool:
    return not any(part in "/" + path for part in DATED_RECORD_PARTS)


def minted_rows(text: str) -> set[str]:
    return set(MINTED_ROW.findall(text))


def addendum_map(text: str) -> tuple[dict[str, str], set[str], set[str]]:
    """(id -> the minted id it maps to), the ids declared NEVER MINTED, and every id declared."""
    aliases: dict[str, str] = {}
    never: set[str] = set()
    declared: set[str] = set()
    for ids, state, minted_as in ADDENDUM_ROW.findall(text):
        found = re.findall(r"D-\d\d", ids)
        target = re.findall(r"D-\d\d", minted_as)
        declared.update(found)
        if "NEVER MINTED" in state.upper():
            never.update(found)
        elif target:
            for ident in found:
                aliases[ident] = target[0]
    return aliases, never, declared


def live_citations() -> dict[str, set[str]]:
    """Which live surfaces cite which `D-nn`, excluding the ledger itself.

    🔴 The ledger does not cite itself. It is the register: a number in its allocator note or its
    addendum is bookkeeping ABOUT the numbering, not a rule being applied. Counting it made this
    suite report `D-27`, `D-28`, `D-29` and the `D-39` in the sentence explaining that `max + 1`
    now returns `D-39` — four findings about its own prose, which is how a check teaches a reader
    to ignore it.
    """
    out: dict[str, set[str]] = {}
    for path in tracked_markdown():
        if not is_live_surface(path) or Path(path) == LEDGER.relative_to(ROOT):
            continue
        try:
            text = (ROOT / path).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for match in CITATION.finditer(text):
            ident = match.group(1) or match.group(2)
            out.setdefault(ident, set()).add(path)
    return out


class EveryCitedDetectionRuleResolves(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = LEDGER.read_text(encoding="utf-8")
        cls.minted = minted_rows(cls.text)
        cls.aliases, cls.never, cls.declared = addendum_map(cls.text)
        cls.cited = live_citations()

    def test_the_premise_holds_the_table_and_the_addendum_both_parse(self) -> None:
        """Asserted rather than assumed: a silent parse failure would make this suite vacuous."""
        self.assertGreater(len(self.minted), 20, "the DEFAULTS table did not parse into rows")
        self.assertIn("D-01", self.minted)
        self.assertIn("D-38", self.minted)
        self.assertNotIn("D-17", self.minted, "D-17 is reserved and must never be a row")
        self.assertIn("D-17", self.declared,
                      "D-17 is reserved by the operator and cited; the addendum must declare it")
        self.assertGreater(len(self.cited), 10, "no live surface cites a detection rule at all?")

    def test_every_alias_the_addendum_declares_points_at_a_row_that_exists(self) -> None:
        """An alias to a row that is not there would resolve a citation onto nothing."""
        self.assertTrue(self.aliases, "the addendum declares no alias; the mapping table moved")
        for ident, target in sorted(self.aliases.items()):
            self.assertIn(target, self.minted, f"{ident} is mapped to {target}, which is not a row")
            self.assertNotIn(ident, self.minted, f"{ident} is both aliased and minted")

    def test_no_id_is_both_minted_and_declared_never_minted(self) -> None:
        self.assertEqual(set(), self.never & self.minted,
                         "an id cannot be a row and declared never minted; the addendum is stale")

    def test_the_unresolved_set_is_exactly_the_declared_debt_and_has_not_grown(self) -> None:
        """🔴 THE RATCHET. A fifth dangling citation from a live surface turns this red."""
        unresolved = {ident: sorted(where) for ident, where in sorted(self.cited.items())
                      if ident not in self.minted and ident not in self.declared}
        self.assertEqual(
            {}, unresolved,
            "a live surface cites a detection rule that is neither a row of the DEFAULTS table, "
            "nor mapped by the allocator addendum, nor declared never minted:\n  "
            + "\n  ".join(f"{k} cited in {', '.join(v)}" for k, v in unresolved.items())
            + "\nEither cite a row that exists, or declare the id in the addendum's mapping table "
              "with what happened to it. Declaring is the cheaper repair and it loses nothing; "
              "what is not allowed is a number a reader cannot follow anywhere.")

    def test_the_declared_debt_does_not_quietly_widen(self) -> None:
        """A declaration is a repair that loses nothing — and a growing one is a repair nobody made."""
        self.assertLessEqual(
            len(self.never), 4,
            f"the addendum now declares {len(self.never)} ids NEVER MINTED ({sorted(self.never)}). "
            "Four is the measured baseline of 2026-10-21. Declaring a fifth is recording a new "
            "dangling rule rather than minting it, and the lower bound for this suite must be "
            "lowered by the BATCH_COMMIT that mints one, never raised.")

    def test_every_id_the_addendum_declares_never_minted_is_actually_cited(self) -> None:
        """Otherwise the declaration is bookkeeping about nothing, and the baseline is inflated."""
        for ident in sorted(self.never):
            self.assertIn(ident, self.cited,
                          f"{ident} is declared NEVER MINTED but no live surface cites it; a "
                          "declaration exists to resolve a citation")


if __name__ == "__main__":
    unittest.main(verbosity=2)
