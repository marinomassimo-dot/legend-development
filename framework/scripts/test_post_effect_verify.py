#!/usr/bin/env python3
"""POST_EFFECT_VERIFICATION, against a real repository rather than a mock.

Every test here builds an actual git working tree in a temporary directory, runs actual
commands in it, and reads the actual delta. A mocked snapshot would let the comparison
agree with an instrument that was never pointed at anything — and the whole point of
this module is that a prediction and an observation can disagree.

🔴 The fixtures live under the system temp directory, and until revision 8 that alone
made them useless: `classify_target` returned SCRATCH for anything under `/tmp`,
`/private/tmp` or `/var/folders` BEFORE consulting the repository root, so a fixture
repository was entirely unguarded and the first run of the live floor watched
`echo tampered > kept.txt` rewrite a committed file while the guard said ALLOW.
`AFixtureRepositoryIsStillARepository` is that regression, pinned.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import effect_model as em  # noqa: E402
import guard_policy as policy  # noqa: E402
import post_effect_verify as pev  # noqa: E402


class Fixture(unittest.TestCase):
    """A real repository with two committed files, torn down after each test."""

    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="rev8-pev-")).resolve()
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "t@example.invalid")
        self.git("config", "user.name", "t")
        (self.root / "kept.txt").write_text("original\n")
        (self.root / "other.txt").write_text("other\n")
        self.git("add", "kept.txt", "other.txt")
        self.git("commit", "-q", "-m", "base")

    def git(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", "-C", str(self.root), *args],
                              capture_output=True, text=True)

    def observe(self, command: str, authority: str = "SHELL_DEFAULT") -> dict:
        # 🔴 Not `run`. `unittest.TestCase.run` IS the test runner, and overriding it
        # made every test in this file call `pev.run` with a TestResult as its command
        # and fail before setUp had ever executed.
        return pev.run(command, str(self.root), actor="test", authority=authority)


class AFixtureRepositoryIsStillARepository(Fixture):
    """🔴 Repository membership beats the scratch prefix, and it did not until rev8."""

    def test_a_write_into_a_repo_under_the_temp_directory_is_denied(self) -> None:
        target = str(self.root / "kept.txt")
        self.assertIsNotNone(policy.verdict(f"echo x > {target}",
                                            str(self.root), str(self.root)))

    def test_the_scratch_exemption_still_holds_outside_the_repository(self) -> None:
        self.assertIsNone(policy.verdict("echo x > /tmp/elsewhere.txt",
                                         str(self.root), str(self.root)))

    def test_the_forbidden_write_does_not_reach_the_file(self) -> None:
        report = self.observe("echo tampered > kept.txt")
        self.assertEqual(pev.REFUSED, report["result"])
        self.assertFalse(report["executed"])
        self.assertEqual("original\n", (self.root / "kept.txt").read_text())


class TheObservedSetMustEqualTheAuthorisedSet(Fixture):
    """TEST FLOOR 6 and 7."""

    def test_an_extra_observed_effect_invalidates_the_write(self) -> None:
        before = pev.snapshot(str(self.root))
        (self.root / "planted.txt").write_text("nobody authorised this\n")
        after = pev.snapshot(str(self.root))
        comparison = pev.verify([], pev.delta(before, after), str(self.root))
        self.assertEqual(em.MISMATCH, comparison.verdict)
        self.assertEqual(1, len(comparison.extra))
        self.assertIn("EXTRA", comparison.reason())

    def test_a_missing_authorised_effect_invalidates_the_write(self) -> None:
        want = [em.Effect(em.WRITE, "never_written.txt", em.INSIDE_REPO)]
        comparison = pev.verify(want, [], str(self.root))
        self.assertEqual(em.MISMATCH, comparison.verdict)
        self.assertEqual(1, len(comparison.missing))
        self.assertIn("MISSING", comparison.reason())

    def test_an_exactly_authorised_write_is_valid(self) -> None:
        """The positive half. A verifier that only ever says INVALID verifies nothing."""
        (self.root / "other.txt").write_text("other, modified\n")
        report = self.observe("git add other.txt")
        self.assertEqual("AUTHORIZED", report["authorization"])
        self.assertEqual(pev.VALID, report["result"])
        self.assertEqual([], report["extra_effect"])
        self.assertEqual([], report["missing_effect"])

    def test_a_no_op_staging_reports_the_authorised_effect_as_missing(self) -> None:
        """🔴 Declared over-strictness, not an accident.

        `git add` on an unmodified path changes nothing, so the authorised STAGE never
        happens. Reporting that as INVALID is the deliberate reading: the alternative
        cannot distinguish 'the write did not happen' from 'the write happened
        somewhere this instrument cannot see'.
        """
        report = self.observe("git add other.txt")
        self.assertEqual(pev.INVALID, report["result"])
        self.assertEqual(1, len(report["missing_effect"]))


class TheDeltaReadsTheRightColumn(Fixture):

    def test_staging_a_file_is_one_effect_and_not_two(self) -> None:
        """🔴 Porcelain `XY` is (index-vs-HEAD, worktree-vs-index).

        Reading the pair made `git add` — which moves X and not the file — look like a
        WRITE to a file nothing had written, and every legitimate staging came out
        INVALID with a phantom EXTRA beside it.
        """
        (self.root / "other.txt").write_text("changed\n")
        before = pev.snapshot(str(self.root))
        self.git("add", "other.txt")
        after = pev.snapshot(str(self.root))
        observed = pev.delta(before, after)
        self.assertEqual([em.STAGE], [e.kind for e in observed])

    def test_a_new_file_is_a_write(self) -> None:
        before = pev.snapshot(str(self.root))
        (self.root / "new.txt").write_text("new\n")
        after = pev.snapshot(str(self.root))
        self.assertEqual([(em.WRITE, "new.txt")],
                         [(e.kind, e.target) for e in pev.delta(before, after)])

    def test_a_deleted_file_is_a_delete(self) -> None:
        before = pev.snapshot(str(self.root))
        (self.root / "kept.txt").unlink()
        after = pev.snapshot(str(self.root))
        self.assertEqual([(em.DELETE, "kept.txt")],
                         [(e.kind, e.target) for e in pev.delta(before, after)])

    def test_a_restore_is_a_write_and_not_silence(self) -> None:
        """The destructive act whose whole signature is a file quietly going back."""
        (self.root / "kept.txt").write_text("work in progress\n")
        before = pev.snapshot(str(self.root))
        self.git("checkout", "--", "kept.txt")
        after = pev.snapshot(str(self.root))
        self.assertEqual([(em.WRITE, "kept.txt")],
                         [(e.kind, e.target) for e in pev.delta(before, after)])

    def test_a_commit_is_a_commit_and_a_reset_is_a_ref_mutation(self) -> None:
        """Both move HEAD. Only one of them is a commit, and the difference is descent."""
        (self.root / "kept.txt").write_text("v2\n")
        self.git("add", "kept.txt")
        before = pev.snapshot(str(self.root))
        self.git("commit", "-q", "-m", "v2")
        after = pev.snapshot(str(self.root))
        observed = pev.resolve_head_kind(pev.delta(before, after), str(self.root),
                                         before, after)
        self.assertIn(em.COMMIT, [e.kind for e in observed if e.target == "HEAD"])

        before = pev.snapshot(str(self.root))
        self.git("reset", "-q", "--hard", "HEAD~1")
        after = pev.snapshot(str(self.root))
        observed = pev.resolve_head_kind(pev.delta(before, after), str(self.root),
                                         before, after)
        self.assertIn(em.REF_MUTATION, [e.kind for e in observed if e.target == "HEAD"])

    def test_a_new_ref_is_observed(self) -> None:
        before = pev.snapshot(str(self.root))
        self.git("branch", "a-new-branch")
        after = pev.snapshot(str(self.root))
        kinds = [(e.kind, e.target) for e in pev.delta(before, after)]
        self.assertIn((em.REF_MUTATION, "refs/heads/a-new-branch"), kinds)

    def test_a_mode_change_is_observed_as_a_permission_change(self) -> None:
        self.git("update-index", "--chmod=+x", "kept.txt")
        before = pev.snapshot(str(self.root))
        self.git("update-index", "--chmod=-x", "kept.txt")
        after = pev.snapshot(str(self.root))
        kinds = [e.kind for e in pev.delta(before, after)]
        self.assertIn(em.PERMISSION_CHANGE, kinds)

    def test_a_failed_snapshot_is_an_unknown_effect_and_not_an_empty_one(self) -> None:
        """An unreadable before-state makes every after-state unexplainable. Returning
        empty would instead report every observed effect as EXTRA — a noisier wrong."""
        outside = Path(tempfile.mkdtemp(prefix="rev8-norepo-"))
        self.addCleanup(shutil.rmtree, outside, ignore_errors=True)
        broken = pev.snapshot(str(outside))
        self.assertFalse(broken.ok)
        observed = pev.delta(broken, pev.snapshot(str(self.root)))
        self.assertEqual([em.UNKNOWN_EFFECT], [e.kind for e in observed])


class CoverageAndRenames(Fixture):

    def test_a_rename_is_expanded_into_a_delete_and_a_write(self) -> None:
        """git reports an unstaged `mv` as `D old` + `?? new`, never as a rename."""
        want = [em.Effect(em.RENAME, "a.txt", em.INSIDE_REPO)]
        expanded = [e.kind for e in pev.expand(want)]
        self.assertEqual([em.DELETE, em.WRITE], expanded)

    def test_an_authorised_directory_covers_what_lands_in_it(self) -> None:
        want = [em.Effect(em.WRITE, "outbox", em.INSIDE_REPO)]
        have = [em.Effect(em.WRITE, "outbox/a.txt", em.INSIDE_REPO),
                em.Effect(em.WRITE, "outbox/b.txt", em.INSIDE_REPO)]
        self.assertTrue(pev.verify(want, have, str(self.root)).valid)

    def test_a_directory_does_not_cover_a_sibling(self) -> None:
        want = [em.Effect(em.WRITE, "outbox", em.INSIDE_REPO)]
        have = [em.Effect(em.WRITE, "outboxes/a.txt", em.INSIDE_REPO)]
        self.assertFalse(pev.verify(want, have, str(self.root)).valid)

    def test_an_extraction_covers_writes_beneath_its_destination(self) -> None:
        want = [em.Effect(em.ARCHIVE_EXTRACT, "vendor", em.INSIDE_REPO)]
        have = [em.Effect(em.WRITE, "vendor/lib/a.js", em.INSIDE_REPO)]
        self.assertTrue(pev.verify(want, have, str(self.root)).valid)

    def test_a_network_write_is_never_missing_because_it_is_never_observable(self) -> None:
        want = [em.Effect(em.NETWORK_WRITE, "origin", em.NONLOCAL)]
        self.assertTrue(pev.verify(want, [], str(self.root)).valid)

    def test_an_authorised_write_outside_the_repository_is_never_missing(self) -> None:
        """🔴 Found by running the floor, not by reading the code: `echo fine > /tmp/x`
        is an act SHELL_DEFAULT exists to permit, and it lands outside every snapshot
        here. A verifier that invalidates the writes it authorises is not a verifier."""
        want = [em.Effect(em.WRITE, "/tmp/out.txt", em.SCRATCH)]
        self.assertTrue(pev.verify(want, [], str(self.root)).valid)


class TheRefusedCaseIsItsOwnOutcome(Fixture):
    """A command that was REFUSED and one that RAN and did the wrong thing differ."""

    def test_a_refused_command_executes_nothing_and_reports_refused(self) -> None:
        for command in ("git add -A", "echo x 1> kept.txt", "chmod 777 kept.txt",
                        "git clean -fd", "git push origin main",
                        "echo hi\necho x > kept.txt", "cp -t . /etc/hosts"):
            with self.subTest(command=command):
                report = self.observe(command)
                self.assertEqual("DENIED", report["authorization"])
                self.assertFalse(report["executed"])
                self.assertEqual(pev.REFUSED, report["result"])

    def test_a_refused_command_is_authorised_for_nothing_so_any_effect_is_extra(self) -> None:
        """The case the module exists for: a hook that did not fire is
        indistinguishable from a hook that allowed, unless someone looks after."""
        before = pev.snapshot(str(self.root))
        (self.root / "kept.txt").write_text("as if the hook had not fired\n")
        after = pev.snapshot(str(self.root))
        comparison = pev.verify([], pev.delta(before, after), str(self.root))
        self.assertFalse(comparison.valid)
        self.assertEqual(1, len(comparison.extra))

    def test_the_positive_floor_and_the_negative_floor_in_one_fixture(self) -> None:
        """🔴 The rev8 brief's condition: BOTH halves, same runtime, same session, same
        guard revision, same worktree, same actor binding. Split across two fixtures
        they would be two measurements of two trees."""
        forbidden = ("echo tampered > kept.txt", "git add -A", "git reset --hard HEAD",
                     "chmod +x kept.txt", "tar -xf /tmp/a.tar")
        permitted = ("git status --short", "git branch --show-current",
                     "git worktree list", "echo fine > /tmp/rev8-floor-probe.txt",
                     "git checkout -b a-fresh-branch")
        for command in forbidden:
            with self.subTest(direction="REFUSED", command=command):
                self.assertEqual("DENIED", self.observe(command)["authorization"])
        for command in permitted:
            with self.subTest(direction="ALLOWED", command=command):
                self.assertEqual("AUTHORIZED", self.observe(command)["authorization"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
