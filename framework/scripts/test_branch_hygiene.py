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
import re
import shutil
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
                         "1 DELETE_READY · base `main` (named with --main)", self.report["totals"])

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
    def test_backup_history_stays_visible_without_a_landing_or_deletion_instruction(self) -> None:
        fx = Fixture()
        self.addCleanup(fx.close)
        run(["branch", "backup/preserved", "old-work"], fx.repo)
        run(["branch", "backup/already-landed", "main"], fx.repo)
        report = bh.build_report(fx.repo, "main", 1, None, None)
        rows = {r["branch"]: r for r in report["branches"]}
        self.assertEqual(bh.PRESERVED_BACKUP, rows["backup/preserved"]["class"])
        self.assertEqual(1, rows["backup/preserved"]["ahead"])
        self.assertGreater(rows["backup/preserved"]["age_days"], 1)
        self.assertEqual(bh.PRESERVED_BACKUP, rows["backup/already-landed"]["class"])
        self.assertEqual(bh.LAND_OVERDUE, rows["old-work"]["class"])
        self.assertEqual(bh.DELETE_READY, rows["merged-done"]["class"])
        self.assertIn("2 PRESERVED_BACKUP", report["totals"])
        markdown = bh.render_markdown(fx.repo, report["branches"], report["worktrees"], 1)
        self.assertIn("| PRESERVED_BACKUP | `backup/preserved` | 1 |", markdown)
        self.assertIn("not task branches to land or delete", markdown)

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

    def test_stale_worktree_metadata_is_reported_prunable_and_left_in_place(self) -> None:
        """A worktree whose directory is gone is git's `prunable`: named, never removed."""
        fx = Fixture()
        self.addCleanup(fx.close)
        gone = Path(fx.tmp.name) / "gone"
        run(["worktree", "add", "-q", "--detach", str(gone)], fx.repo)
        shutil.rmtree(gone)
        report = bh.build_report(fx.repo, "main", 1, None, None)
        stale = [t for t in report["worktrees"] if Path(str(t["path"])).name == "gone"]
        self.assertEqual(1, len(stale))
        self.assertTrue(stale[0].get("prunable"))
        self.assertTrue(bh.worktree_state(stale[0]).startswith("PRUNABLE"))
        live = [t for t in report["worktrees"] if Path(str(t["path"])).name != "gone"]
        self.assertFalse(any(t.get("prunable") for t in live), "a live worktree was called stale")
        markdown = bh.render_markdown(fx.repo, report["branches"], report["worktrees"], 1)
        self.assertIn("`git worktree prune` clears exactly these", markdown)
        self.assertIn(str(gone), run(["worktree", "list"], fx.repo),
                      "the report must not prune anything itself")

    def test_outside_a_repository_is_an_error_not_a_crash(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(ROOT / "framework" / "scripts" / "branch_hygiene.py"),
                 "--root", tmp], capture_output=True, text=True)
            self.assertEqual(2, result.returncode)
            self.assertIn("branch_hygiene:", result.stderr)


class TheBaseIsWhereOtherActorsLanded(unittest.TestCase):
    """2026-11-24: the root checkout's local `main` lagged `development/main` by 449 commits, so
    the report called 25 branches LAND_OVERDUE and 7 DELETE_READY where the truth was 0 and 37.
    The base is the furthest-ahead of local main and the remote-tracking main, says which it
    used, and falls back to local main when there is no remote ref or it is not a descendant."""

    def make(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        repo = Path(tmp.name) / "repo"
        repo.mkdir()
        run(["init", "-q", "-b", "main"], repo)
        run(["config", "user.name", "hygiene-test"], repo)
        run(["config", "user.email", "hygiene@example.invalid"], repo)
        commit(repo, "base.txt", "base")
        return repo

    def landed_elsewhere(self, repo):
        """A branch whose commit is already on the remote's main but not on local main."""
        run(["checkout", "-q", "-b", "landed"], repo)
        commit(repo, "landed.txt", "landed by another actor")
        tip = run(["rev-parse", "HEAD"], repo).strip()
        run(["checkout", "-q", "main"], repo)
        return tip

    def test_a_lagging_local_main_is_not_the_base(self) -> None:
        repo = self.make()
        tip = self.landed_elsewhere(repo)
        run(["update-ref", "refs/remotes/development/main", tip], repo)
        explicit = bh.build_report(repo, "main", 1, None, None)
        auto = bh.build_report(repo, None, 1, None, None)
        self.assertEqual("main", explicit["main"])
        self.assertEqual("development/main", auto["main"])
        by = {r["branch"]: r for r in auto["branches"]}
        self.assertEqual("DELETE_READY", by["landed"]["class"])
        self.assertEqual("MAIN", by["main"]["class"], "local main is never a task branch")
        self.assertEqual(1, by["main"]["behind"], "how far it lags is shown, not hidden")
        misread = {r["branch"]: r for r in explicit["branches"]}
        self.assertNotEqual("DELETE_READY", misread["landed"]["class"],
                            "the old base is the misreading this guards against")
        self.assertIn("base `development/main` (local `main` is 1 commit(s) behind it)",
                      auto["totals"])

    def test_no_remote_ref_falls_back_to_local_main_and_says_so(self) -> None:
        repo = self.make()
        report = bh.build_report(repo, None, 1, None, None)
        self.assertEqual("main", report["main"])
        self.assertIn("base `main` (local; no remote-tracking main ahead of it)", report["totals"])

    def test_a_remote_ref_that_is_not_a_descendant_is_ignored(self) -> None:
        repo = self.make()
        tip = self.landed_elsewhere(repo)
        run(["update-ref", "refs/remotes/development/main", tip], repo)
        commit(repo, "local-only.txt", "local main moved on")  # main now diverges from the remote
        report = bh.build_report(repo, None, 1, None, None)
        self.assertEqual("main", report["main"])

    def test_the_furthest_ahead_remote_wins_and_origin_is_a_fallback(self) -> None:
        repo = self.make()
        mid = self.landed_elsewhere(repo)
        run(["checkout", "-q", "landed"], repo)
        commit(repo, "later.txt", "later")
        later = run(["rev-parse", "HEAD"], repo).strip()
        run(["checkout", "-q", "main"], repo)
        run(["update-ref", "refs/remotes/origin/main", mid], repo)
        self.assertEqual("origin/main", bh.build_report(repo, None, 1, None, None)["main"])
        run(["update-ref", "refs/remotes/development/main", later], repo)
        self.assertEqual("development/main", bh.build_report(repo, None, 1, None, None)["main"])

    def test_a_named_base_wins(self) -> None:
        repo = self.make()
        tip = self.landed_elsewhere(repo)
        run(["update-ref", "refs/remotes/development/main", tip], repo)
        report = bh.build_report(repo, "main", 1, None, None)
        self.assertEqual("main", report["main"])
        self.assertIn("named with --main", report["totals"])

    def test_the_command_line_and_json_say_which_base_was_used(self) -> None:
        repo = self.make()
        tip = self.landed_elsewhere(repo)
        run(["update-ref", "refs/remotes/development/main", tip], repo)
        script = str(ROOT / "framework" / "scripts" / "branch_hygiene.py")
        text = subprocess.run([sys.executable, script, "--root", str(repo)],
                              capture_output=True, text=True)
        self.assertEqual(0, text.returncode, text.stderr)
        self.assertIn("Compared with: base `development/main`", text.stdout)
        data = json.loads(subprocess.run([sys.executable, script, "--root", str(repo), "--json"],
                                         capture_output=True, text=True).stdout)
        self.assertEqual("development/main", data["main"])
        self.assertIn("development/main", data["base_note"])


class TheRemovalCheckNamesEveryReasonToKeep(unittest.TestCase):
    """One linked worktree per reason, and two that give none. The ignored file is the one that matters:
    `git worktree remove` takes it without a word."""

    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.box = Path(tmp.name).resolve()
        self.repo = self.box / "repo"
        self.projects = self.box / "projects"
        self.repo.mkdir()
        self.projects.mkdir()
        run(["init", "-q", "-b", "main"], self.repo)
        run(["config", "user.name", "hygiene-test"], self.repo)
        run(["config", "user.email", "hygiene@example.invalid"], self.repo)
        commit(self.repo, ".gitignore", "backup/\n__pycache__/")

    def tree(self, name):
        path = self.box / name
        run(["worktree", "add", "-q", "--detach", str(path), "main"], self.repo)
        return path

    def transcript(self, path, hours_ago):
        folder = self.projects / re.sub(r"[^A-Za-z0-9]", "-", str(path))
        folder.mkdir()
        (folder / "s.jsonl").write_text("{}\n", encoding="utf-8")
        when = dt.datetime.now().timestamp() - hours_ago * 3600
        os.utime(folder / "s.jsonl", (when, when))

    def keep(self):
        report = bh.build_report(self.repo, "main", 1, None, None)
        return {Path(str(r["path"])).name: "; ".join(r["keep"])
                for r in bh.removal_rows(self.repo, report["worktrees"], "main", self.projects)}

    def test_each_reason_is_named_and_a_clean_idle_tree_has_none(self) -> None:
        self.tree("idle")
        self.transcript(self.box / "idle", 30)
        cached = self.tree("cached")
        (cached / "__pycache__").mkdir()
        (cached / "__pycache__" / "x.pyc").write_bytes(b"x")
        ignored = self.tree("ignored")
        (ignored / "backup").mkdir()
        (ignored / "backup" / "only_copy.md").write_text("x\n", encoding="utf-8")
        (self.tree("dirty") / "scratch.txt").write_text("x\n", encoding="utf-8")
        commit(self.tree("unmerged"), "new.txt", "not on main")
        run(["worktree", "lock", str(self.tree("locked"))], self.repo)
        self.transcript(self.tree("recent"), 2)
        held = self.tree("held")
        holder = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"], cwd=str(held))
        self.addCleanup(holder.wait)
        self.addCleanup(holder.kill)
        keep = self.keep()
        self.assertNotIn("repo", keep, "the primary checkout is never a candidate")
        self.assertEqual("", keep["idle"])
        self.assertEqual("", keep["cached"])
        self.assertIn("backup/", keep["ignored"])
        self.assertIn("deleted silently", keep["ignored"])
        self.assertIn("1 changed or untracked", keep["dirty"])
        self.assertIn("HEAD not on main", keep["unmerged"])
        self.assertIn("locked", keep["locked"])
        self.assertIn("wrote 2.0 h ago", keep["recent"])
        eligible = dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=22)
        stated = dt.datetime.strptime(keep["recent"].split("eligible after ")[1].split(" ")[0], "%Y-%m-%dT%H:%MZ")
        self.assertLess(abs((stated.replace(tzinfo=dt.timezone.utc) - eligible).total_seconds()), 180)
        self.assertIn(f"{holder.pid} ", keep["held"])
        self.assertIn("(cwd)", keep["held"])
        self.assertTrue((ignored / "backup" / "only_copy.md").exists(), "a report removes nothing")

    def test_the_flag_prints_the_section_and_the_default_report_does_not(self) -> None:
        self.tree("idle")
        script = str(ROOT / "framework" / "scripts" / "branch_hygiene.py")
        base = [sys.executable, script, "--root", str(self.repo), "--projects-dir", str(self.projects)]
        plain = subprocess.run(base, capture_output=True, text=True, check=True).stdout
        asked = subprocess.run(base + ["--removal"], capture_output=True, text=True, check=True).stdout
        self.assertNotIn("Removal check", plain)
        self.assertIn("none found", asked.split("## Removal check")[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
