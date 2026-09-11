#!/usr/bin/env python3
"""Exercise task closure on real Git repositories, including interrupted and unsafe cases."""
from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

import task_close as tc
from test_branch_hygiene import run, commit

SCRIPT = Path(__file__).resolve().parent / "task_close.py"


def run_cli(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=cwd,
                          capture_output=True, text=True, timeout=120)


class TaskClosure(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="legend-close-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "root"
        self.repo.mkdir()
        run(["init", "-q", "-b", "main"], self.repo)
        run(["config", "user.name", "close-test"], self.repo)
        run(["config", "user.email", "close@example.invalid"], self.repo)
        commit(self.repo, "base", "base")
        self.wt = Path(self.tmp.name) / "task space"
        run(["worktree", "add", "-b", "task/test", str(self.wt)], self.repo)
        commit(self.wt, "task", "completed task")
        self.tip = run(["rev-parse", "HEAD"], self.wt).strip()

    def assert_kept(self):
        self.assertEqual(self.tip, run(["rev-parse", "task/test"], self.repo).strip())
        self.assertTrue(self.wt.exists())

    def test_lands_detaches_deletes_and_keeps_reusable_worktree(self):
        tc.close_task(self.wt)
        self.assertEqual("", run(["branch", "--show-current"], self.wt).strip())
        self.assertEqual(self.tip, run(["rev-parse", "HEAD"], self.wt).strip())
        self.assertEqual("", run(["branch", "--list", "task/test"], self.repo).strip())
        run(["merge-base", "--is-ancestor", self.tip, "main"], self.repo)
        self.assertEqual("", run(["status", "--porcelain"], self.repo))

    def test_optional_removal(self):
        tc.close_task(self.wt, remove_worktree=True)
        self.assertFalse(self.wt.exists())
        self.assertEqual("", run(["branch", "--list", "task/test"], self.repo).strip())

    def test_dry_run_changes_nothing(self):
        before = run(["rev-parse", "main"], self.repo)
        self.assertEqual(3, len(tc.close_task(self.wt, dry_run=True)))
        self.assertEqual(before, run(["rev-parse", "main"], self.repo))
        self.assert_kept()

    def test_dirty_checkout_is_refused(self):
        for checkout in (self.repo, self.wt):
            with self.subTest(checkout=checkout):
                path = checkout / "uncommitted"
                path.write_text("preserve")
                with self.assertRaises(tc.GitError):
                    tc.close_task(self.wt)
                self.assert_kept()
                path.unlink()

    def test_ignored_material_prevents_removal(self):
        (self.wt / ".gitignore").write_text("private-cache\n")
        run(["add", ".gitignore"], self.wt)
        run(["commit", "-m", "ignore cache"], self.wt)
        (self.wt / "private-cache").write_text("keep")
        with self.assertRaises(tc.GitError):
            tc.close_task(self.wt, remove_worktree=True)
        self.assertTrue((self.wt / "private-cache").exists())

    def test_landing_never_overwrites_ignored_material_on_main(self):
        commit(self.repo, ".gitignore", "local-data")
        (self.repo / "local-data").write_text("preserve this ignored file")
        commit(self.wt, "local-data", "tracked task output")
        self.tip = run(["rev-parse", "HEAD"], self.wt).strip()
        with self.assertRaises(tc.GitError):
            tc.close_task(self.wt)
        self.assertEqual("preserve this ignored file", (self.repo / "local-data").read_text())
        self.assert_kept()

    def test_main_is_never_a_task(self):
        with self.assertRaises(tc.GitError):
            tc.close_task(self.repo)
        self.assert_kept()

    def test_unrelated_ignored_material_does_not_block_landing(self):
        commit(self.repo, ".gitignore", "cache/")
        (self.repo / "cache").mkdir()
        (self.repo / "cache" / "data").write_text("keep")
        tc.close_task(self.wt)
        self.assertEqual("keep", (self.repo / "cache" / "data").read_text())

    def test_ignored_directory_file_collision_is_refused(self):
        commit(self.repo, ".gitignore", "local-dir/")
        (self.repo / "local-dir").mkdir()
        (self.repo / "local-dir" / "data").write_text("keep")
        commit(self.wt, "local-dir", "file replaces directory")
        with self.assertRaises(tc.GitError):
            tc.close_task(self.wt)
        self.assertEqual("keep", (self.repo / "local-dir" / "data").read_text())

    def test_conflict_restores_main_and_keeps_task_for_retry(self):
        """A conflicted merge left in the checkout holding main would refuse EVERY other
        actor's closure until a human resolved it by hand (blind review, 2026-09-06)."""
        commit(self.repo, "base", "main change")
        commit(self.wt, "base", "task change")
        self.tip = run(["rev-parse", "HEAD"], self.wt).strip()
        main_before = run(["rev-parse", "main"], self.repo).strip()
        with self.assertRaises(tc.GitError) as caught:
            tc.close_task(self.wt)
        self.assertIn("conflict", str(caught.exception).lower())
        self.assertIn("base", str(caught.exception), "the cause names the conflicted path")
        self.assert_kept()
        self.assertEqual("task/test", run(["branch", "--show-current"], self.wt).strip())
        # main is exactly as it was: same tip, clean tree, no merge in progress.
        self.assertEqual(main_before, run(["rev-parse", "main"], self.repo).strip())
        self.assertEqual("", run(["status", "--porcelain"], self.repo))
        self.assertFalse((self.repo / ".git" / "MERGE_HEAD").exists())
        # An unrelated actor lands while the conflict is still unrepaired.
        other = Path(self.tmp.name) / "other"
        run(["worktree", "add", "-b", "task/other", str(other), "main"], self.repo)
        commit(other, "elsewhere", "unrelated work")
        tc.close_task(other)
        # The repair is made on the task side, then the closure is retried.
        with self.assertRaises(AssertionError):
            run(["merge", "--no-edit", "main"], self.wt)
        (self.wt / "base").write_text("resolved\n")
        run(["add", "base"], self.wt)
        run(["commit", "--no-edit"], self.wt)
        tc.close_task(self.wt)
        self.assertEqual("", run(["branch", "--list", "task/test"], self.repo).strip())
        self.assertEqual("resolved\n", (self.repo / "base").read_text())

    def test_resume_after_detachment(self):
        run(["merge", "--no-ff", "--no-edit", "task/test"], self.repo)
        run(["switch", "--detach", "HEAD"], self.wt)
        tc.close_task(self.wt, resume_branch="task/test")
        self.assertEqual("", run(["branch", "--list", "task/test"], self.repo).strip())

    def test_cannot_close_a_peers_branch(self):
        peer = Path(self.tmp.name) / "peer"
        run(["worktree", "add", "-b", "task/peer", str(peer)], self.repo)
        with self.assertRaises(tc.GitError):
            tc.close_task(self.wt, resume_branch="task/peer")
        self.assert_kept()

    def test_concurrent_closer_is_refused(self):
        lock = self.repo / ".git" / "legend-task-close.lock"
        lock.write_text("another closer")
        with self.assertRaises(tc.GitError):
            tc.close_task(self.wt)
        self.assertTrue(lock.exists())
        self.assert_kept()

    def test_locked_worktree_is_not_partially_closed_for_removal(self):
        run(["worktree", "lock", str(self.wt)], self.repo)
        with self.assertRaises(tc.GitError):
            tc.close_task(self.wt, remove_worktree=True)
        self.assert_kept()
        self.assertEqual("task/test", run(["branch", "--show-current"], self.wt).strip())

class TheCliIsDriven(unittest.TestCase):
    """``main`` as a subprocess from the task worktree — what §21e tells an actor to run.

    ``close_task`` was exercised in-process fourteen ways; the command line, its exit codes
    and what it prints were certified by nothing (retrospective § 9.3).
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="legend-close-cli-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "root"
        self.repo.mkdir()
        run(["init", "-q", "-b", "main"], self.repo)
        run(["config", "user.name", "close-test"], self.repo)
        run(["config", "user.email", "close@example.invalid"], self.repo)
        commit(self.repo, "base", "base")
        self.wt = Path(self.tmp.name) / "task space"
        run(["worktree", "add", "-b", "task/test", str(self.wt)], self.repo)
        commit(self.wt, "task", "completed task")
        self.tip = run(["rev-parse", "HEAD"], self.wt).strip()

    def test_dry_run_prints_the_sequence_and_changes_nothing(self):
        main_before = run(["rev-parse", "main"], self.repo)
        result = run_cli(self.wt, "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(lines[-1], "DRY_RUN")
        self.assertEqual(len(lines), 4, "three git commands, then the verdict")
        self.assertTrue(all(line.startswith("git ") for line in lines[:3]), lines)
        self.assertEqual(main_before, run(["rev-parse", "main"], self.repo))
        self.assertEqual(self.tip, run(["rev-parse", "task/test"], self.repo).strip())

    def test_closure_lands_and_says_task_closed(self):
        result = run_cli(self.wt)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines()[-1], "TASK_CLOSED")
        run(["merge-base", "--is-ancestor", self.tip, "main"], self.repo)
        self.assertEqual("", run(["branch", "--list", "task/test"], self.repo).strip())
        self.assertEqual("", run(["branch", "--show-current"], self.wt).strip())

    def test_a_refusal_is_exit_2_with_the_reason_on_stderr(self):
        result = run_cli(self.repo)
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stderr.startswith("task_close: "), result.stderr)
        self.assertEqual("", result.stdout)
        self.assertEqual(self.tip, run(["rev-parse", "task/test"], self.repo).strip())


if __name__ == "__main__":
    unittest.main(verbosity=2)
