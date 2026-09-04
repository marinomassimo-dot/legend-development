#!/usr/bin/env python3
"""The instrument TASK-GUARD52-A2 must satisfy before a destination parser lands again.

There is no parser to test right now: four were written, three shipped live bypasses onto
peer worktrees, and the fourth was reverted at `040dabb`. This file is what survives, and
it is deliberately not a test of code that does not exist. It is the ACCEPTANCE CONDITION
for the code that will, expressed as something runnable rather than as a paragraph in a
commit message nobody will find.

The condition, stated once: a parser may land only with an instrument that FAILS against
every historical bypass below. Each was a live hole; each was found by blind review; none
was found by the tests written alongside the parser that shipped it. The point is not the
five strings — it is that "the instrument catches the bugs we already know about" is the
weakest possible bar, and three instruments in a row failed to clear even that.

Why each instrument failed, because the pattern is the deliverable:

  v1 tests    hand-written cases          missed the option shapes not thought of
  v2 tests    hand-written, wrong cwd     a stronger neighbouring rule masked the subject
  v3 oracle   real git, hand-written list omitted the `=`-attachment family
  v4 oracle   real git, generated options generated one grammar, hand-fixed the operand one
              and, once operands were generated too, still excluded the `-bf` family on a
              premise of mine that is false of git, and could not fail on the `help` axis
              at all

Every fix closed the dimension that had just been named and left the next one open. So the
bar for A2 is not "pass this list" — passing this list is what v4 did. It is: the
instrument must be shown to fail against each of these BEFORE the parser is trusted, and a
mutation battery over the parser must reach zero survivors, including mutants confined to a
single option family.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import guard_policy as gp  # noqa: E402

#: (label, spelling, what the guard wrongly concluded). `{peer}` is a live peer worktree.
HISTORICAL_BYPASSES = (
    ("v1 kept flag values",
     "git worktree add --lock --reason /tmp/ok {peer}",
     "judged the --reason value as the destination"),
    ("v2 grouped short flags",
     "git worktree add -fb hijack {peer}",
     "read -fb as one opaque flag and judged the branch name"),
    ("v2 value-first cluster",
     "git worktree add -bf hijack {peer} main",
     "excluded by a false premise that the value letter must come last"),
    ("v3 = attached value",
     "git worktree add -B= {peer} main",
     "lstrip('=') made the attached value read as empty"),
    ("v3 help as a flag value",
     "git worktree add --lock --reason -h {peer}",
     "an arity-blind -h scan returned help before parsing"),
)

PARSER_ATTRIBUTES = ("parse_worktree_add", "worktree_add_destination")


def a_parser_exists() -> bool:
    return any(hasattr(gp, name) for name in PARSER_ATTRIBUTES)


class TheAcceptanceConditionIsRecorded(unittest.TestCase):
    def test_the_bypass_corpus_is_not_empty(self) -> None:
        """A condition with nothing in it is satisfied by everything."""
        self.assertGreaterEqual(len(HISTORICAL_BYPASSES), 5)
        for label, spelling, why in HISTORICAL_BYPASSES:
            with self.subTest(label=label):
                self.assertIn("{peer}", spelling)
                self.assertGreater(len(why), 25, "a bypass needs its cause, not a label")

    def test_every_bypass_spelling_is_refused_today(self) -> None:
        """While no parser exists the blanket refusal covers all of them. This is what
        makes the revert safe, and it is checked rather than assumed."""
        peer = "/Users/massimo/Desktop/legend-codex-aqeilan/new"
        for label, spelling, _ in HISTORICAL_BYPASSES:
            with self.subTest(label=label):
                outcome, _, _ = gp.classify(spelling.format(peer=peer), "/tmp", None,
                                            gp.DEFAULT_AUTHORITY, str(ROOT))
                self.assertNotEqual(gp.ALLOWED, outcome)

    def test_a_returning_parser_must_bring_its_instrument(self) -> None:
        """🔴 The gate for TASK-GUARD52-A2.

        If a destination parser reappears in `guard_policy` while this file is still the
        placeholder it is today, this test fails and names what is missing. It is the one
        assertion here that is meant to go red: it goes red exactly when someone lands
        parser number five without first replacing this file with a real instrument.
        """
        if not a_parser_exists():
            self.skipTest("no destination parser in guard_policy; the revert holds")
        self.fail(
            "a destination parser is back in guard_policy.py while this file is still the "
            "acceptance-condition placeholder. Replace it with an instrument that is SHOWN "
            "to fail against every entry in HISTORICAL_BYPASSES, plus a mutation battery "
            "over the parser reaching zero survivors — including mutants confined to one "
            "option family, which is how the fourth attempt died.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
