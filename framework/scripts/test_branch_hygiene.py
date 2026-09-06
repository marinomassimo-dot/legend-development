#!/usr/bin/env python3
"""`branch_hygiene.py` names what is not on `main`, correctly, on a repository it built itself.

The report is what makes LEGEND_CORE §21e's "nothing unmerged at rest" checkable, so it is
tested against a temporary repository whose ground truth is constructed rather than assumed:
one merged branch, one stale unmerged branch with a back-dated commit, one fresh unmerged
branch, one branch held by a dirty worktree. Each must land in its class, the totals line
must count them, `--json` must carry the same rows, and a repository with only `main` must
exit 0 with an empty table — a report that fails on the healthy case is one nobody runs.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import branch_hygiene as bh  # noqa: E402


def run(args, cwd, env=None):
    merged = {**os.environ, **(env or {})}
    result = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True,
                            env=merged)
    if result.returncode != 0:
        raise AssertionError(f"git {' '.join(args)} failed: {result.stderr}")
    return result.stdout


def commit(cwd, name, message, env=None):
    (Path(cwd) / name).write_text(message + "\n", encoding="utf-8")
    run(["add", name], cwd)
    run(["commit", "-q", "-m", message], cwd, env)


class Fixture:
    def __init__(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name) / "repo"
        self.repo.mkdir()
        run(["init", "-q", "-b", "main"], self.repo)
        run(["config", "user.name", "hygiene-test"], self.repo)
        run(["config", "user.email", "hygiene@example.invalid"], self.repo)
        commit(self.repo, "base.txt", "base")
        # DELETE_READY: points at main, checked out nowhere.
        run(["branch", "merged-done"], self.repo)
        # LAND_OVERDUE: one commit ahead, ten days old.
        run(["checkout", "-q", "-b", "old-work"], self.repo)
        stale = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=10)).isoformat()
        commit(self.repo, "old.txt", "old work",
               {"GIT_AUTHOR_DATE": stale, "GIT_COMMITTER_DATE": stale})
        run(["checkout", "-q", "main"], self.repo)
        # IN_PROGRESS: one commit ahead, made now.
        run(["checkout", "-q", "-b", "fresh-work"], self.repo)
        commit(self.repo, "fresh.txt", "fresh work")
        run(["checkout", "-q", "main"], self.repo)
        # DELETE_BLOCKED_CHECKED_OUT: nothing ahead, but a dirty worktree holds it.
        self.wt = Path(self.tmp.name) / "wt"
        run(["worktree", "add", "-q", str(self.wt), "-b", "wt-branch"], self.repo)
        (self.wt / "scratch.txt").write_text("uncommitted\n", encoding="utf-8")

    def close(self) -> None:
        self.tmp.cleanup()


class TheReportClassifiesWhatItBuilt(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fx = Fixture()
        cls.report = bh.build_report(cls.fx.repo, "main", 1, None, None)
        cls.by_name = {r["branch"]: r for r in cls.report["branches"]}

    @classmethod
    def tearDownClass(cls) -> None:
        cls.fx.close()

    def test_each_branch_lands_in_its_class(self) -> None:
        expected = {"main": bh.MAIN, "merged-done": bh.DELETE_READY,
                    "old-work": bh.LAND_OVERDUE, "fresh-work": bh.IN_PROGRESS,
                    "wt-branch": bh.DELETE_BLOCKED_CHECKED_OUT}
        for name, klass in expected.items():
            with self.subTest(branch=name):
                self.assertEqual(klass, self.by_name[name]["class"])

    def test_ahead_and_age_are_measured_not_guessed(self) -> None:
        self.assertEqual(1, self.by_name["old-work"]["ahead"])
        self.assertGreaterEqual(self.by_name["old-work"]["age_days"], 9)
        self.assertEqual(1, self.by_name["fresh-work"]["ahead"])
        self.assertEqual(0, self.by_name["fresh-work"]["age_days"])
        self.assertEqual(0, self.by_name["merged-done"]["ahead"])

    def test_the_checked_out_branch_names_its_worktree(self) -> None:
        self.assertEqual(str(self.fx.wt.resolve()),
                         str(Path(self.by_name["wt-branch"]["checked_out_at"]).resolve()))

    def test_the_dirty_worktree_is_reported_dirty(self) -> None:
        trees = {Path(t["path"]).resolve(): t for t in self.report["worktrees"]}
        self.assertEqual(1, trees[self.fx.wt.resolve()]["dirty"])
        self.assertEqual(0, trees[self.fx.repo.resolve()]["dirty"])

    def test_the_totals_line_counts_the_classes(self) -> None:
        self.assertEqual("5 branches · 2 ahead-of-main commits total · 1 LAND_OVERDUE · "
                         "1 DELETE_READY", self.report["totals"])

    def test_overdue_sorts_first(self) -> None:
        self.assertEqual(bh.LAND_OVERDUE, self.report["branches"][0]["class"])

    def test_json_carries_the_same_rows(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "framework" / "scripts" / "branch_hygiene.py"),
             "--root", str(self.fx.repo), "--json"], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual({r["branch"]: r["class"] for r in self.report["branches"]},
                         {r["branch"]: r["class"] for r in data["branches"]})
        self.assertIn("git -C", data["landing_recipe"])

    def test_markdown_ends_with_the_landing_recipe(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "framework" / "scripts" / "branch_hygiene.py"),
             "--root", str(self.fx.repo)], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("## Landing recipe", result.stdout)
        self.assertIn("python3 framework/scripts/task_close.py", result.stdout)
        self.assertIn("branch -d <branch>", result.stdout)
        self.assertIn("| LAND_OVERDUE | `old-work` |", result.stdout)

    def test_exclude_pattern_drops_rows_but_never_main(self) -> None:
        report = bh.build_report(self.fx.repo, "main", 1, None, r"^(old|fresh)-")
        names = {r["branch"] for r in report["branches"]}
        self.assertIn("main", names)
        self.assertNotIn("old-work", names)
        self.assertNotIn("fresh-work", names)

    def test_max_age_moves_the_overdue_line(self) -> None:
        report = bh.build_report(self.fx.repo, "main", 30, None, None)
        by_name = {r["branch"]: r for r in report["branches"]}
        self.assertEqual(bh.IN_PROGRESS, by_name["old-work"]["class"])


class TheHealthyCaseIsQuiet(unittest.TestCase):
    def test_overdue_uses_elapsed_seconds_not_rounded_days(self) -> None:
        for seconds, expected in ((86399, bh.IN_PROGRESS), (86400, bh.IN_PROGRESS),
                                  (86401, bh.LAND_OVERDUE), (90000, bh.LAND_OVERDUE)):
            with self.subTest(seconds=seconds):
                row = {"branch": "task/x", "ahead": 1, "age_days": seconds // 86400,
                       "age_seconds": seconds}
                self.assertEqual(expected, bh.classify([row], [], "main", 1)[0]["class"])

    def test_25_hour_old_commit_is_overdue_in_real_git(self) -> None:
        fx = Fixture()
        self.addCleanup(fx.close)
        when = dt.datetime.fromisoformat(run(["show", "-s", "--format=%cI", "fresh-work"], fx.repo).strip())
        report = bh.build_report(fx.repo, "main", 1, None, None, when + dt.timedelta(hours=25))
        self.assertEqual(bh.LAND_OVERDUE, next(r["class"] for r in report["branches"]
                                              if r["branch"] == "fresh-work"))

    def test_a_repository_with_only_main_exits_zero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            repo.mkdir()
            run(["init", "-q", "-b", "main"], repo)
            run(["config", "user.name", "hygiene-test"], repo)
            run(["config", "user.email", "hygiene@example.invalid"], repo)
            commit(repo, "base.txt", "base")
            result = subprocess.run(
                [sys.executable, str(ROOT / "framework" / "scripts" / "branch_hygiene.py"),
                 "--root", str(repo)], capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIn("1 branches · 0 ahead-of-main commits total · 0 LAND_OVERDUE · "
                          "0 DELETE_READY", result.stdout)

    def test_outside_a_repository_is_an_error_not_a_crash(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(ROOT / "framework" / "scripts" / "branch_hygiene.py"),
                 "--root", tmp], capture_output=True, text=True)
            self.assertEqual(2, result.returncode)
            self.assertIn("branch_hygiene:", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
