#!/usr/bin/env python3
"""`git worktree add` is refused, and this suite exists to keep it refused ON PURPOSE.

§21d's operator decision of 2026-09-03 grants worktree provisioning to agents "once the
guard false refusal is fixed (0B)". Four parsers were written to fix it. Three shipped live
bypasses that put a checkout on a peer worktree — each found by blind review, none by this
repository's own tests — and the fourth was reverted with no known bypass, because the
instrument that was supposed to demonstrate its correctness could not fail on two axes.

The full account is in `guard_policy.py` above `GIT_VERB_SUBCOMMANDS`; the reverted work is
at `040dabb` and re-queued as TASK-GUARD52-A2.

So the assertion here is inverted from what it was. It is not "provisioning works"; it is
"provisioning is refused, uniformly, and the refusal has not been quietly narrowed". A
refusal is a fact worth guarding: three of the four parsers made it stop being one.
"""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import guard_policy as gp  # noqa: E402

# The three historical bypasses, each a spelling that reached a peer worktree at some
# revision. They are kept as DATA rather than prose: TASK-GUARD52-A2 must show that any
# future instrument fails against every one of them before a parser may land again.
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


class ProvisioningIsRefusedAndStaysRefused(unittest.TestCase):
    def test_every_historical_bypass_spelling_is_refused(self) -> None:
        """None of these may be allowed while no parser judges destinations."""
        for label, template in HISTORICAL_BYPASSES.items():
            with self.subTest(bypass=label):
                self.assertNotEqual(gp.ALLOWED, decide(template.format(peer=PEER)))

    def test_a_scratch_destination_is_refused_too(self) -> None:
        """The honest cost of the revert, asserted so it is not forgotten.

        A worktree in `/tmp` is harmless and is refused anyway, because the guard has no
        way to tell one destination from another without the parser that was reverted.
        This test failing means someone re-enabled provisioning; it should fail only in the
        commit that lands TASK-GUARD52-A2 together with its instrument.
        """
        for command in ("git worktree add /tmp/wt-scratch -b throwaway",
                        "git worktree add -b throwaway /tmp/wt-scratch",
                        "git worktree add --orphan /tmp/wt-scratch"):
            with self.subTest(command=command):
                self.assertNotEqual(gp.ALLOWED, decide(command))

    def test_the_parser_that_was_reverted_is_actually_gone(self) -> None:
        """Not merely unreferenced. Unreachable-but-present code is how this started:
        revision 9 left a `FILE_WRITE` branch that no input could reach, and it sat there
        for three revisions being cited as the behaviour."""
        self.assertFalse(hasattr(gp, "parse_worktree_add"))
        self.assertFalse(hasattr(gp, "worktree_add_destination"))
        self.assertFalse(hasattr(gp, "WORKTREE_ADD_VALUE_SHORT"))

    def test_reads_are_still_reads(self) -> None:
        """The revert must not have taken `git worktree list` with it."""
        self.assertEqual(gp.ALLOWED, decide("git worktree list"))

    def test_the_refusal_reaches_the_shipped_hook_and_not_only_the_policy(self) -> None:
        import json
        import os
        payload = json.dumps({"tool_name": "Bash", "cwd": str(ROOT),
                              "tool_input": {"command": f"git worktree add {PEER} -b h"}})
        env = {**os.environ, "LEGEND_ASSIGNED_WORKTREE": str(ROOT)}
        env.pop("CLAUDE_PROJECT_DIR", None)
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "guard_bash_command.py")],
            input=payload, capture_output=True, text=True, env=env)
        self.assertTrue(result.stdout.strip(), "the hook said nothing, which is allow")
        self.assertEqual(
            "deny", json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"])


class TheRevertIsRecordedWhereItWillBeRead(unittest.TestCase):
    def test_the_policy_states_why_provisioning_is_refused(self) -> None:
        """An actor refused by this rule must find the reason at the rule, not in a commit
        message it has no way to know exists."""
        text = (ROOT / "framework" / "scripts" / "guard_policy.py").read_text(
            encoding="utf-8")
        self.assertIn("ATTEMPTED AND REVERTED", text)
        self.assertIn("TASK-GUARD52-A2", text)
        self.assertIn("040dabb", text,
                      "the reverted work must be locatable, or it is lost rather than "
                      "parked")


if __name__ == "__main__":
    unittest.main(verbosity=2)
