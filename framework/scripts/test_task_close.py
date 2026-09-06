#!/usr/bin/env python3
"""Exercise task closure on real Git repositories, including interrupted and unsafe cases."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import guard_policy as gp
import task_close as tc
from test_branch_hygiene import run, commit


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

    def test_git_proves_why_force_and_reset_are_not_ordinary_creation(self):
        import shlex
        run(["branch", "existing", self.tip], self.repo)
        reset = ["git", "worktree", "add", "-B", "existing",
                 str(Path(self.tmp.name) / "reset"), "main"]
        self.assertNotEqual(gp.ALLOWED, gp.classify(shlex.join(reset), str(self.repo), None,
                                                   gp.DEFAULT_AUTHORITY, str(self.repo))[0])
        run(reset[1:], self.repo)
        self.assertNotEqual(self.tip, run(["rev-parse", "existing"], self.repo).strip())
        force = ["git", "worktree", "add", "--force",
                 str(Path(self.tmp.name) / "duplicate"), "task/test"]
        self.assertNotEqual(gp.ALLOWED, gp.classify(shlex.join(force), str(self.repo), None,
                                                   gp.DEFAULT_AUTHORITY, str(self.repo))[0])
        run(force[1:], self.repo)
        holders = [t for t in tc.worktrees(self.repo) if t["branch"] == "task/test"]
        self.assertEqual(2, len(holders))

    def test_guard_allows_the_recipe_but_confines_detach(self):
        import shlex
        for command in tc.close_task(self.wt, dry_run=True):
            with self.subTest(command=command):
                self.assertEqual(gp.ALLOWED, gp.classify(shlex.join(command), str(self.wt),
                                                        None, gp.DEFAULT_AUTHORITY, str(self.wt))[0])
        for command in (f'git -C "{self.repo}" switch --detach HEAD',
                        "git switch --detach main", "git switch --detach HEAD --force",
                        "git switch --detach HEAD --discard-changes", "git switch -C task/test"):
            with self.subTest(command=command):
                self.assertNotEqual(gp.ALLOWED, gp.classify(command, str(self.wt), None,
                                                           gp.DEFAULT_AUTHORITY, str(self.wt))[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
