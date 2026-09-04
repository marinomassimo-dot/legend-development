#!/usr/bin/env python3
"""`git worktree add` is judged by WHERE it lands, and the branch that does so is reached.

§21d's operator decision of 2026-09-03 grants worktree provisioning to agents "once the
guard false refusal is fixed (0B)". The refusal was not a policy anyone wrote: the branch
at `guard_policy.py` that classifies `git worktree add` as a `FILE_WRITE` at its
destination was UNREACHABLE, because `worktree` is a key of `GIT_SUB_READ` and so the outer
`if` matched, the inner membership test failed, and the whole `elif` chain below — the one
written for this exact command — was skipped. What reached the actor was the generic ref
handling.

Unreachable logic and absent logic produce identical evidence from a failing case and have
opposite repairs, so the distinction is asserted here rather than assumed: the case that
must now be ALLOWED proves the branch runs, and the cases that must still be DENIED prove
it did not become an allowance.

🔴 The destinations are enumerated from `git worktree list`, never invented. The first
version of this measurement used `../legend-mirror` — a plausible-looking peer name that
does not exist on disk — saw it allowed, and concluded the repair let an actor write a
whole checkout into a peer's path. It does not. A non-existent sibling is not a peer, and
generalising from it was letting the instrument define the population.
"""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import guard_policy as gp  # noqa: E402


def live_worktrees() -> list[str]:
    """Every checkout git itself reports for this repository, this one excluded."""
    out = subprocess.run(["git", "-C", str(ROOT), "worktree", "list", "--porcelain"],
                         capture_output=True, text=True)
    paths = [line.split(" ", 1)[1].strip()
             for line in out.stdout.splitlines() if line.startswith("worktree ")]
    return [p for p in paths if Path(p).resolve() != ROOT.resolve()]


def decide(command: str) -> str:
    outcome, _, _ = gp.classify(command, str(ROOT), None, gp.DEFAULT_AUTHORITY, str(ROOT))
    return outcome


class ProvisioningIsJudgedByDestination(unittest.TestCase):
    def test_a_scratch_destination_is_allowed(self) -> None:
        """The case that proves the branch is REACHED. Before the repair this was refused
        as a ref mutation, so a green here is the whole behaviour change."""
        self.assertEqual(gp.ALLOWED, decide("git worktree add /tmp/wt-scratch -b throwaway"))

    def test_every_live_peer_worktree_is_still_refused(self) -> None:
        """The population is git's, not this file's.

        🔴 SKIPPED, not failed, where there are no peers. A fresh clone has exactly one
        worktree, so asserting that peers exist made this suite red in every clone — it was
        measuring the checkout it happened to run in and calling that a property of the
        repository. The scratch case below carries the behaviour claim on its own.
        """
        peers = live_worktrees()
        if not peers:
            self.skipTest("this checkout has no peer worktrees; nothing to refuse")
        for peer in peers:
            with self.subTest(peer=peer):
                self.assertNotEqual(
                    gp.ALLOWED, decide(f"git worktree add {peer} -b hijack"),
                    f"provisioning may not write a checkout over the live worktree {peer}")

    def test_the_relative_spelling_of_a_peer_is_refused_the_same_way(self) -> None:
        """A path is not safer for being spelled `../`."""
        for peer in live_worktrees():
            name = Path(peer).name
            if Path(peer).parent != ROOT.parent:
                continue
            with self.subTest(peer=name):
                self.assertNotEqual(gp.ALLOWED,
                                    decide(f"git worktree add ../{name} -b hijack"))

    def test_it_matches_what_a_plain_write_to_the_same_path_decides(self) -> None:
        """The cross-check that makes this a scope decision and not a special case.

        If `git worktree add <p>` and `echo x > <p>/CLAUDE.md` disagreed about a path, one
        of the two would be deciding on the command rather than on the destination.
        """
        targets = live_worktrees() + ["/tmp/wt-scratch"]
        for path in targets:
            with self.subTest(path=path):
                self.assertEqual(
                    decide(f"echo x > {path}/CLAUDE.md") == gp.ALLOWED,
                    decide(f"git worktree add {path} -b b") == gp.ALLOWED,
                    f"the two disagree about {path}, so one is judging the command")

    def test_reads_are_untouched(self) -> None:
        """`git worktree list` must still return early — the repair moved that test out of
        an `if/elif` chain, which is exactly where a read could have been lost."""
        self.assertEqual(gp.ALLOWED, decide("git worktree list"))

    def test_removal_is_not_covered_by_this_change(self) -> None:
        """`add` is additive; `remove` destroys a checkout and stays refused. Naming it
        here keeps the change's scope honest rather than leaving it to be discovered."""
        self.assertNotEqual(gp.ALLOWED, decide("git worktree remove ../legend-codex-aqeilan"))


class TheBranchIsActuallyTheOneRunning(unittest.TestCase):
    """Reached, not merely no-longer-denied: absent and unreachable logic look alike."""

    def test_the_finding_names_a_worktree_write_and_not_a_ref_mutation(self) -> None:
        _, _, findings = gp.classify("git worktree add /tmp/wt-scratch -b throwaway",
                                     str(ROOT), None, gp.DEFAULT_AUTHORITY, str(ROOT))
        self.assertTrue(findings, "no effect derived at all")
        rules = {f.rule for f in findings}
        self.assertIn("FILE_WRITE", rules, f"the destination branch did not run: {rules}")
        self.assertNotIn("REF_MUTATION", rules,
                         "the generic ref handling is still what fires")

    def test_the_destination_is_the_target_and_not_the_branch_name(self) -> None:
        """`-b <name>` names a ref to create, not a path to write."""
        _, _, findings = gp.classify("git worktree add /tmp/wt-scratch -b throwaway",
                                     str(ROOT), None, gp.DEFAULT_AUTHORITY, str(ROOT))
        self.assertEqual(["/tmp/wt-scratch"], findings[0].targets)


if __name__ == "__main__":
    unittest.main(verbosity=2)
