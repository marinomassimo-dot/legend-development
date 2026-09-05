#!/usr/bin/env python3
"""`git worktree add` is ALLOWED, `git worktree remove` is allowed without force, and the two
spellings that can still destroy something are refused — on purpose, since 2026-09-05.

Until 2026-09-05 this suite kept provisioning REFUSED: four destination parsers had been
written to judge `git worktree add` by where the checkout lands, three of them shipped live
bypasses onto a peer worktree, and the fourth was reverted at `040dabb` because no instrument
could be shown to fail against the known bypasses. `DEC-20260905-AGILE-HARNESS-MODE`
(LEGEND_CORE §21e) made the destination question moot: provisioning one's own worktree is an
ordinary agent act, and the guard judges it as what it is — an additive creation. Git refuses
a destination that exists and is not empty, and refuses a branch checked out elsewhere, so no
spelling of `add` overwrites a peer's checkout or its in-flight work.

The historical bypass corpus is kept as DATA. Every one of those spellings is now simply
ALLOWED, and the test says so rather than pretending the refusal was narrowed.

What can still destroy something is `remove --force` (discards a dirty checkout) and `move`
(relocates a directory that may be another chat's home). Both stay refused, in every spelling
git accepts — bundled short flags and long-option abbreviations included, because the push
battery already recorded thirteen one-character spelling bypasses of exactly that shape.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import guard_policy as gp  # noqa: E402

# The historical bypass spellings, each of which once placed a checkout on a peer worktree
# past a destination parser. Kept as data: under §21e they are ordinary provisioning.
HISTORICAL_BYPASSES = {
    "kept flag values (v1)": "git worktree add --lock --reason /tmp/ok {peer}",
    "grouped short flags (v2)": "git worktree add -fb hijack {peer}",
    "value-first cluster (v2, found by mutation)": "git worktree add -bf hijack {peer} main",
    "= attached value (v3)": "git worktree add -B= {peer} main",
    "help as a flag value (v3)": "git worktree add --lock --reason -h {peer}",
}

PEER = "/Users/massimo/Desktop/legend-codex-aqeilan/new"


def decide(command: str, cwd: str = "/tmp") -> str:
    outcome, _, _ = gp.classify(command, cwd, None, gp.DEFAULT_AUTHORITY, str(ROOT))
    return outcome


def hook(command: str, cwd: str = str(ROOT)) -> str:
    """What the SHIPPED hook answers: `deny`, or `allow` when it says nothing."""
    payload = json.dumps({"tool_name": "Bash", "cwd": cwd,
                          "tool_input": {"command": command}})
    env = {**os.environ, "LEGEND_ASSIGNED_WORKTREE": str(ROOT)}
    env.pop("CLAUDE_PROJECT_DIR", None)
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "guard_bash_command.py")],
        input=payload, capture_output=True, text=True, env=env)
    if not result.stdout.strip():
        return "allow"
    return json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"]


class ProvisioningIsOrdinary(unittest.TestCase):
    def test_every_historical_bypass_spelling_is_now_simply_allowed(self) -> None:
        """DEC-20260905-AGILE-HARNESS-MODE. Not narrowed: allowed, because `add` cannot
        overwrite anything git considers occupied."""
        for label, template in HISTORICAL_BYPASSES.items():
            with self.subTest(bypass=label):
                self.assertEqual(gp.ALLOWED, decide(template.format(peer=PEER)))

    def test_the_landing_recipe_spellings_are_allowed(self) -> None:
        for command in ("git worktree add /tmp/wt-scratch -b throwaway",
                        "git worktree add -b throwaway /tmp/wt-scratch",
                        "git worktree add --orphan /tmp/wt-scratch",
                        "git worktree add ../legend-junior -b task/scout main",
                        "git worktree add --detach /tmp/base HEAD",
                        "git worktree remove /tmp/wt-scratch",
                        "git worktree remove ../legend-junior",
                        "git worktree prune",
                        "git worktree prune -v",
                        "git worktree list",
                        "git worktree list --porcelain",
                        "git worktree lock /tmp/wt-scratch",
                        "git worktree unlock /tmp/wt-scratch",
                        "git worktree repair",
                        "git worktree -h"):
            with self.subTest(command=command):
                self.assertEqual(gp.ALLOWED, decide(command))

    def test_an_additive_verb_derives_no_effect_at_all(self) -> None:
        """Nothing is overwritten, so there is nothing for `post_effect_verify` to match:
        the authorised effect set is empty, and an empty set is the honest prediction."""
        for command in ("git worktree add /tmp/x -b y", "git worktree remove /tmp/x",
                        "git worktree prune"):
            with self.subTest(command=command):
                derived, _, parse_error = gp.effects(command, "/tmp", None, str(ROOT))
                self.assertIsNone(parse_error)
                self.assertEqual([], list(derived))

    def test_provisioning_reaches_the_shipped_hook_as_allow(self) -> None:
        self.assertEqual("allow", hook(f"git worktree add {PEER}-scratch -b h"))


class WhatCanStillDestroyIsRefused(unittest.TestCase):
    def test_forced_removal_is_refused_in_every_spelling(self) -> None:
        for command in ("git worktree remove --force /tmp/wt",
                        "git worktree remove -f /tmp/wt",
                        "git worktree remove -fv /tmp/wt",
                        "git worktree remove -vf /tmp/wt",
                        "git worktree remove --forc /tmp/wt",
                        "git worktree remove --fo /tmp/wt",
                        "git worktree remove /tmp/wt --force",
                        "git worktree remove --force --force /tmp/wt",
                        f"git worktree remove --force {PEER}"):
            with self.subTest(command=command):
                self.assertNotEqual(gp.ALLOWED, decide(command))

    def test_forced_removal_names_its_hazard(self) -> None:
        """The denial must say what makes force dangerous, not only that it is refused."""
        _, reason, _ = gp.classify("git worktree remove --force /tmp/wt", "/tmp", None,
                                   gp.DEFAULT_AUTHORITY, str(ROOT))
        self.assertIsNotNone(reason)
        self.assertIn("worktree remove --force", reason)

    def test_move_is_refused(self) -> None:
        for command in ("git worktree move /tmp/a /tmp/b",
                        f"git worktree move {PEER} /tmp/elsewhere"):
            with self.subTest(command=command):
                self.assertNotEqual(gp.ALLOWED, decide(command))

    def test_the_refusal_reaches_the_shipped_hook(self) -> None:
        self.assertEqual("deny", hook(f"git worktree remove --force {PEER}"))


class TheDecisionIsRecordedWhereItWillBeRead(unittest.TestCase):
    def test_the_policy_states_why_provisioning_is_ordinary(self) -> None:
        """An actor whose `remove --force` is refused must find the rule at the rule, and an
        actor reading the old refusal must find out that it is gone — both at the code."""
        text = (ROOT / "framework" / "scripts" / "guard_policy.py").read_text(
            encoding="utf-8")
        self.assertIn("DEC-20260905-AGILE-HARNESS-MODE", text)
        self.assertIn("DESTINATION PARSING IS MOOT", text)
        self.assertIn("040dabb", text,
                      "the reverted parser work must stay locatable, or it is lost rather "
                      "than retired")

    def test_no_destination_parser_came_back(self) -> None:
        """A parser would judge a question §21e retired, and would reintroduce the bypass
        surface that three of them shipped. Unreachable-but-present code is how the previous
        regime started; absent is the only state this test accepts."""
        self.assertFalse(hasattr(gp, "parse_worktree_add"))
        self.assertFalse(hasattr(gp, "worktree_add_destination"))
        self.assertFalse(hasattr(gp, "WORKTREE_ADD_VALUE_SHORT"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
