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
import tempfile
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


class TheDestinationSurvivesEveryArgumentORDER(unittest.TestCase):
    """🔴 The regression this suite SHIPPED, and the reason it shipped green.

    The first destination check was `[t for t in rest if not t.startswith("-")][1:2]`,
    which keeps flag VALUES. So `git worktree add --lock --reason /tmp/ok <peer>` judged
    the reason string and never looked at the peer, and `-b hijack <peer>` judged the
    branch name — both ALLOWED, both PROHIBITED before the repair. A guard made weaker
    while its own suite stayed green.

    It stayed green because every case here spelled the destination FIRST
    (`add <path> -b <branch>`). One argument order was tested and one was not, and the
    untested order is the one an attacker writes. The population is now the ORDERS, not a
    path that happened to occur to me.

    The peer is BUILT rather than borrowed: a fresh clone has no peer worktrees, so the
    borrowed-population version of these checks skipped in exactly the environment
    `run_release_regressions.py` runs in — which is the other half of why this shipped.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        base = Path(cls._tmp.name)
        cls.origin = base / "origin"
        cls.origin.mkdir()
        for argv in (["init", "-q", "-b", "main"], ["add", "-A"],
                     ["-c", "user.email=t@t", "-c", "user.name=t",
                      "commit", "-q", "--allow-empty", "-m", "base"]):
            subprocess.run(["git", "-C", str(cls.origin), *argv], check=True,
                           capture_output=True, text=True)
        cls.peer = base / "peer"
        subprocess.run(["git", "-C", str(cls.origin), "worktree", "add", "-q",
                        str(cls.peer), "-b", "peer-branch"], check=True,
                       capture_output=True, text=True)
        listed = subprocess.run(["git", "-C", str(cls.origin), "worktree", "list"],
                                capture_output=True, text=True).stdout
        assert str(cls.peer) in listed, f"the fixture peer was not created: {listed}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def decide_in_fixture(self, command: str, cwd: str = "/tmp") -> str:
        """🔴 cwd defaults to OUTSIDE the fixture repo, and that is not incidental.

        The first version ran these with cwd inside the repo, where a peer destination is
        refused by `SHELL_WRITE_IN_ASSIGNED_WORKTREE` for an unrelated reason. So the suite
        went green against the very code that shipped F2: `-b hijack <peer>` was denied,
        but by the wrong rule, and the destination check it claimed to exercise was never
        consulted. A test whose subject is masked by a stronger neighbouring rule is
        measuring the neighbour.
        """
        outcome, _, _ = gp.classify(command, cwd, None,
                                    gp.DEFAULT_AUTHORITY, str(self.origin))
        return outcome

    def test_the_fixture_peer_is_refused_in_every_argument_order(self) -> None:
        target = f"{self.peer}/new"
        for label, command in (
            ("destination first", f"git worktree add {target} -b hijack"),
            ("-b before it", f"git worktree add -b hijack {target}"),
            ("--reason before it", f"git worktree add --lock --reason /tmp/ok {target}"),
            ("--reason= inline", f"git worktree add --reason=x {target}"),
            ("-B before it", f"git worktree add -B hijack {target}"),
            ("after --", f"git worktree add -- {target}"),
            ("flags both sides", f"git worktree add --detach -b h {target} HEAD"),
            # 🔴 Grouped short flags. `-fb hijack` is `-f -b hijack` to git, confirmed
            # against real git, and the second parser judged `hijack` as the destination
            # and let a checkout land on a live peer. An option grammar is not a list of
            # the spellings that occurred to me.
            ("grouped -fb", f"git worktree add -fb hijack {target}"),
            ("grouped -fB", f"git worktree add -fB hijack {target}"),
            ("grouped -qb", f"git worktree add -qb hijack {target}"),
            ("grouped inline -fbname", f"git worktree add -fbhijack {target}"),
            ("short inline -bname", f"git worktree add -bhijack {target}"),
        ):
            with self.subTest(order=label):
                self.assertNotEqual(gp.ALLOWED, self.decide_in_fixture(command),
                                    f"`{command}` reached a peer worktree")

    def test_a_scratch_destination_still_passes_in_those_same_orders(self) -> None:
        """The positive control: the parse must not have become "refuse everything"."""
        for command in ("git worktree add /tmp/wt-ok -b b",
                        "git worktree add -b b /tmp/wt-ok",
                        "git worktree add --lock --reason r /tmp/wt-ok",
                        "git worktree add --reason=r /tmp/wt-ok",
                        "git worktree add -- /tmp/wt-ok",
                        "git worktree add -fb b /tmp/wt-ok",
                        "git worktree add -bb /tmp/wt-ok",
                        # `--orphan` takes NO value: git derives the branch from the path's
                        # basename. Listing it as value-taking swallowed the destination
                        # and refused a legitimate scratch worktree — a control wrongly
                        # refused is a defect in the same way a bypass is.
                        "git worktree add --orphan /tmp/wt-ok",
                        "git worktree add /tmp/wt-ok --orphan"):
            with self.subTest(command=command):
                self.assertEqual(gp.ALLOWED, self.decide_in_fixture(command))

    def test_an_unknown_option_denies_rather_than_guessing_past_it(self) -> None:
        """The failure direction, inverted after two parsers guessed wrong.

        An option the allowlist does not know makes the parse return None, which becomes
        UNNAMED and denies. A future git flag therefore costs a refusal until it is added,
        which is the direction a guard should fail in.
        """
        for command in (f"git worktree add --brand-new-flag {self.peer}/new",
                        f"git worktree add -Z {self.peer}/new",
                        "git worktree add --brand-new-flag /tmp/wt-ok"):
            with self.subTest(command=command):
                self.assertNotEqual(gp.ALLOWED, self.decide_in_fixture(command))

    def test_help_is_a_read_and_is_not_refused(self) -> None:
        """`git worktree add -h` prints usage and writes nothing. The allowlist refuses it
        for having no operand unless help is recognised first."""
        for command in ("git worktree add -h", "git worktree add --help"):
            with self.subTest(command=command):
                self.assertEqual(gp.ALLOWED, self.decide_in_fixture(command))

    def test_the_destination_parser_picks_the_path_and_not_a_flag_value(self) -> None:
        """Unit-level, so a failure names the parse rather than a verdict."""
        cases = {
            "add /p -b b": "/p",
            "add -b b /p": "/p",
            "add --lock --reason /decoy /p": "/p",
            "add --reason=/decoy /p": "/p",
            "add -- /p": "/p",
            "add --detach -B b /p HEAD": "/p",
            "add -fb decoy /p": "/p",
            "add -fB decoy /p": "/p",
            "add -qb decoy /p": "/p",
            "add -fbdecoy /p": "/p",
            "add -bdecoy /p": "/p",
            "add --orphan /p": "/p",
            "add /p --orphan": "/p",
        }
        for spelling, expected in cases.items():
            with self.subTest(spelling=spelling):
                self.assertEqual(expected, gp.worktree_add_destination(spelling.split()))
        self.assertIsNone(gp.worktree_add_destination(["add", "-b", "only-a-branch"]),
                          "with no operand there is no destination, and None denies")


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
