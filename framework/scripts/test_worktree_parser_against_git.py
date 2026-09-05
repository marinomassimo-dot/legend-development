#!/usr/bin/env python3
"""The `git worktree add` destination-parser corpus — kept as provenance, retired as a gate.

Until 2026-09-05 this file was the acceptance condition for TASK-GUARD52-A2: a destination
parser could land in `guard_policy.py` only with an instrument shown to FAIL against every
historical bypass below. Four parsers had been written; three shipped live bypasses onto a
peer worktree, each found by blind review and none by the tests written beside it, and the
fourth was reverted at `040dabb` because the oracle built to validate it could not fail on two
of its axes.

`DEC-20260905-AGILE-HARNESS-MODE` (LEGEND_CORE §21e) retired the question the parsers were
answering. Provisioning a worktree is an ordinary agent act, judged as an additive creation:
git refuses a destination that exists and is not empty and a branch checked out elsewhere,
so there is no destination to judge and no bypass to place a checkout past. The corpus stays
here because the PATTERN is the deliverable — every fix closed the dimension just named and
left the next one open — and because a future author who wants to judge destinations again
should meet the five spellings, and the four failed instruments, before writing parser five.

What this file asserts today: the corpus is intact; every spelling in it is ALLOWED, which is
the behaviour §21e requires and the opposite of what this file asserted before; and no parser
has come back, because a parser would reintroduce a bypass surface for no rule that needs it.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import guard_policy as gp  # noqa: E402

#: (label, spelling, what a parser wrongly concluded). `{peer}` is a live peer worktree.
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
PEER = "/Users/massimo/Desktop/legend-codex-aqeilan/new"


def a_parser_exists() -> bool:
    return any(hasattr(gp, name) for name in PARSER_ATTRIBUTES)


class TheCorpusIsProvenance(unittest.TestCase):
    def test_the_bypass_corpus_is_intact(self) -> None:
        """A record with nothing in it records nothing."""
        self.assertGreaterEqual(len(HISTORICAL_BYPASSES), 5)
        for label, spelling, why in HISTORICAL_BYPASSES:
            with self.subTest(label=label):
                self.assertIn("{peer}", spelling)
                self.assertGreater(len(why), 25, "a bypass needs its cause, not a label")

    def test_every_bypass_spelling_is_allowed_under_the_agile_mode(self) -> None:
        """DEC-20260905-AGILE-HARNESS-MODE: provisioning is additive, so a spelling that once
        slipped a checkout past a parser is now simply a provisioning command. This asserts
        the new behaviour rather than the refusal it replaced."""
        for label, spelling, _ in HISTORICAL_BYPASSES:
            with self.subTest(label=label):
                outcome, _, _ = gp.classify(spelling.format(peer=PEER), "/tmp", None,
                                            gp.DEFAULT_AUTHORITY, str(ROOT))
                self.assertEqual(gp.ALLOWED, outcome)

    def test_no_destination_parser_has_come_back(self) -> None:
        """A parser judges a question §21e retired and reintroduces the surface three of
        them shipped bypasses through. If one appears, this names what it would cost."""
        if not a_parser_exists():
            return
        self.fail(
            "a destination parser is back in guard_policy.py. Under LEGEND_CORE §21e "
            "provisioning is an additive act with no destination to judge; a parser adds a "
            "bypass surface (see HISTORICAL_BYPASSES) for no rule that needs it.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
