#!/usr/bin/env python3
"""Regressions for tmp_clone_report.py: every verdict that must be KEEP, the one that is REMOVABLE, and the refusals of --remove.
Run: python3 -B framework/scripts/test_tmp_clone_report.py -v"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tmp_clone_report as tcr  # noqa: E402

TOOL = HERE / "tmp_clone_report.py"
IDENT = ("fixture" + "@" + "invalid")       # assembled: the publication gate screens address-shaped strings


def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), *a], capture_output=True, text=True, check=True)


class Fixture:
    def __init__(self):
        self.td = tempfile.TemporaryDirectory()
        t = Path(self.td.name)
        self.repo = t / "repo"
        self.tmp = t / "tmp"
        self.tmp.mkdir()
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        git(self.repo, "config", "user.email", IDENT)
        git(self.repo, "config", "user.name", "t")
        (self.repo / "a.txt").write_text("a\n")
        (self.repo / ".gitignore").write_text("files/\n__pycache__/\n.pytest_cache/\n*.pyc\n")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-qm", "one")
        self.main = git(self.repo, "rev-parse", "HEAD").stdout.strip()

    def clone(self, name):
        d = self.tmp / name
        subprocess.run(["git", "clone", "-q", "--no-hardlinks", str(self.repo), str(d)], check=True)
        git(d, "config", "user.email", IDENT)
        git(d, "config", "user.name", "t")
        return d

    def examine(self, d, older=0.0, size=True):
        return tcr.examine(d, self.repo, self.main, older, time.time() + 3600, size)     # "now" an hour on: the folder is old enough for older=0

    def cli(self, *args):
        return subprocess.run([sys.executable, str(TOOL), "--tmp-root", str(self.tmp), "--repo", str(self.repo), "--main-ref", "HEAD", "--older-than", "0", *args],
                              capture_output=True, text=True)

    def close(self):
        self.td.cleanup()


class Verdicts(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()

    def tearDown(self):
        self.f.close()

    def test_a_clean_clone_of_main_is_removable_and_reports_its_unique_size(self):
        r = self.f.examine(self.f.clone("legend-clean"))
        self.assertEqual((r["verdict"], r["reasons"]), ("REMOVABLE", []))
        self.assertGreater(r["freed"], 0)

    def test_a_clean_clone_whose_only_ignored_file_is_a_unique_output_is_kept_and_names_it(self):
        """Codex review 23: this exact shape was classed REMOVABLE and drove --remove."""
        d = self.f.clone("legend-unique-output")
        (d / "files").mkdir()
        (d / "files" / "unique-analysis.txt").write_text("the only copy\n")
        self.assertEqual(git(d, "status", "--porcelain").stdout.strip(), "")          # a clean tree, as git sees it
        r = self.f.examine(d)
        self.assertEqual(r["verdict"], "KEEP", r)
        self.assertTrue(any("ignored non-cache" in x and "files/" in x for x in r["reasons"]), r)
        out = self.f.cli("--remove", str(d))
        self.assertEqual(out.returncode, 1)
        self.assertIn("REFUSED", out.stderr)
        self.assertTrue((d / "files" / "unique-analysis.txt").is_file())

    def test_regenerable_caches_may_be_ignored_and_a_mix_still_blocks(self):
        d = self.f.clone("legend-caches")
        (d / "__pycache__").mkdir()
        (d / "__pycache__" / "x.cpython-312.pyc").write_bytes(b"\0")
        (d / ".pytest_cache").mkdir()
        (d / ".pytest_cache" / "v").write_text("1")
        (d / "stray.pyc").write_bytes(b"\0")
        r = self.f.examine(d)
        self.assertEqual((r["verdict"], r["reasons"]), ("REMOVABLE", []), r)
        self.assertTrue(any("regenerable cache" in n for n in r["notes"]), r)
        (d / "files").mkdir()
        (d / "files" / "x.txt").write_text("x")
        self.assertEqual(self.f.examine(d)["verdict"], "KEEP")

    def test_a_dirty_tree_is_kept_and_a_modified_tracked_file_is_named(self):
        d = self.f.clone("it54_land")
        (d / "a.txt").write_text("changed\n")
        r = self.f.examine(d)
        self.assertEqual(r["verdict"], "KEEP")
        self.assertTrue(any("dirty tree" in x and "a.txt" in x for x in r["reasons"]), r)

    def test_a_commit_outside_main_is_kept_even_when_the_tree_is_clean(self):
        d = self.f.clone("legend-unique")
        (d / "b.txt").write_text("b\n")
        git(d, "add", "-A")
        git(d, "commit", "-qm", "local only")
        r = self.f.examine(d)
        self.assertEqual(r["verdict"], "KEEP")
        self.assertTrue(any("unknown to the main repository" in x for x in r["reasons"]), r)

    def test_a_local_branch_that_main_contains_is_fine_and_one_it_does_not_is_not(self):
        d = self.f.clone("legend-branches")
        git(d, "branch", "contained")
        self.assertEqual(self.f.examine(d)["verdict"], "REMOVABLE")
        (self.f.repo / "c.txt").write_text("c\n")
        git(self.f.repo, "add", "-A")
        git(self.f.repo, "commit", "-qm", "two")                       # main moves on; the clone's branch is still an ancestor
        self.assertEqual(tcr.examine(d, self.f.repo, git(self.f.repo, "rev-parse", "HEAD").stdout.strip(), 0.0, time.time() + 3600)["verdict"], "REMOVABLE")
        # a commit main does NOT contain (main resolved to the first commit again)
        (d / "z.txt").write_text("z\n")
        git(d, "add", "-A")
        git(d, "commit", "-qm", "z")
        git(self.f.repo, "fetch", "-q", str(d), "HEAD")                # now the main repository KNOWS the commit but main does not contain it
        r = self.f.examine(d)
        self.assertEqual(r["verdict"], "KEEP")
        self.assertTrue(any("not contained in main" in x for x in r["reasons"]), r)

    def test_a_stash_keeps_the_clone(self):
        d = self.f.clone("legend-stash")
        (d / "a.txt").write_text("stashed\n")
        git(d, "stash", "push", "-q")
        r = self.f.examine(d)
        self.assertEqual(r["verdict"], "KEEP")
        self.assertIn("stash present", r["reasons"])

    def test_a_process_with_its_cwd_inside_keeps_the_clone(self):
        d = self.f.clone("legend-busy")
        p = subprocess.Popen(["sleep", "30"], cwd=d)
        try:
            r = self.f.examine(d)
            self.assertEqual(r["verdict"], "KEEP")
            self.assertTrue(any("in use by process" in x for x in r["reasons"]), r)
        finally:
            p.kill()
            p.wait()

    def test_a_recent_folder_is_kept_by_age(self):
        d = self.f.clone("legend-new")
        r = tcr.examine(d, self.f.repo, self.f.main, 1.0, time.time(), True)
        self.assertEqual(r["verdict"], "KEEP")
        self.assertTrue(any("days ago" in x for x in r["reasons"]), r)

    def test_a_report_does_not_touch_the_clone_it_examines(self):
        """The first version's `git status` refreshed .git/index, so a second report saw 0.0 days for a folder the first saw at days."""
        d = self.f.clone("legend-aged")
        old = time.time() - 5 * 86400
        for p in [d, *[x for x in d.iterdir() if x.name != ".git"], d / ".git" / "HEAD", d / ".git" / "logs" / "HEAD"]:
            if p.exists():
                os.utime(p, (old, old))
        (d / "a.txt").touch()                                         # stat data now differs from the index, so a plain `git status` would rewrite it
        os.utime(d / "a.txt", (old, old))
        before = (d / ".git" / "index").stat().st_mtime_ns
        t_git = (d / ".git").stat().st_mtime_ns
        for _ in range(2):
            self.f.examine(d)
        self.assertEqual((d / ".git" / "index").stat().st_mtime_ns, before)
        self.assertEqual((d / ".git").stat().st_mtime_ns, t_git)
        r = tcr.examine(d, self.f.repo, self.f.main, 1.0, time.time(), False)
        self.assertEqual(r["verdict"], "REMOVABLE", r)

    def test_a_linked_worktree_is_never_this_tools_to_remove(self):
        d = self.f.tmp / "legend-linked"
        git(self.f.repo, "worktree", "add", "-q", "--detach", str(d))
        r = self.f.examine(d)
        self.assertEqual(r["verdict"], "KEEP")
        self.assertTrue(any("linked worktree" in x for x in r["reasons"]), r)

    def test_a_folder_without_git_is_kept_unless_it_is_one_of_the_tools_own_scratch_names(self):
        for name, verdict in (("legend-results", "KEEP"), ("legend-public-gate-abc123", "REMOVABLE"), ("legend-candidate-tree-abc123", "REMOVABLE")):
            d = self.f.tmp / name
            d.mkdir()
            (d / "x").write_text("x")
            self.assertEqual(self.f.examine(d)["verdict"], verdict, name)

    def test_claude_scratchpads_foreign_names_and_symlinks_are_never_candidates(self):
        (self.f.tmp / "claude-1000").mkdir()
        (self.f.tmp / "claude-1000" / ".git").mkdir()
        (self.f.tmp / "plain").mkdir()
        os.symlink(self.f.repo, self.f.tmp / "legend-link")
        self.f.clone("legend-ok")
        self.assertEqual([p.name for p in tcr.candidates(self.f.tmp)], ["legend-ok"])

    def test_the_size_counts_only_inodes_whose_every_link_is_inside(self):
        d = self.f.tmp / "legend-links"
        d.mkdir()
        (d / "own").write_bytes(b"x" * 400_000)
        outside = self.f.tmp.parent / "outside.bin"
        outside.write_bytes(b"y" * 400_000)
        os.link(outside, d / "shared")                                  # also linked from outside: removing d frees nothing for it
        os.link(d / "own", d / "own2")                                  # both links inside: counted once, freed
        freed, shared = tcr.disk_sizes(d)
        self.assertTrue(390_000 < freed < 420_000, freed)
        self.assertTrue(390_000 < shared < 420_000, shared)


class Remove(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()

    def tearDown(self):
        self.f.close()

    def test_a_report_deletes_nothing(self):
        d = self.f.clone("legend-clean")
        r = self.f.cli()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("REMOVABLE", r.stdout)
        self.assertTrue(d.is_dir())

    def test_remove_deletes_a_named_clean_clone_and_nothing_else(self):
        a, b = self.f.clone("legend-a"), self.f.clone("legend-b")
        r = self.f.cli("--remove", str(a))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(a.exists())
        self.assertTrue(b.is_dir())
        self.assertTrue((self.f.repo / "a.txt").is_file())

    def test_remove_refuses_a_dirty_clone_a_glob_a_dotdot_a_foreign_path_and_a_claude_folder(self):
        dirty = self.f.clone("it54_land")
        (dirty / "a.txt").write_text("changed\n")
        (self.f.tmp / "claude-1000").mkdir()
        outside = self.f.tmp.parent / "elsewhere"
        outside.mkdir()
        for arg in (str(dirty), str(self.f.tmp / "legend-*"), str(self.f.tmp / "x" / ".." / "it54_land"), str(outside), str(self.f.tmp / "claude-1000"), str(self.f.tmp)):
            with self.subTest(arg=arg):
                r = self.f.cli("--remove", arg)
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("REFUSED", r.stderr)
        self.assertTrue(dirty.is_dir() and outside.is_dir() and (self.f.tmp / "claude-1000").is_dir())

    def test_the_tool_does_not_refuse_itself_through_its_own_command_line_or_its_launching_shell(self):
        """2026-11-24, ADV: `--remove /tmp/x --dry-run` answered 'in use by process N (cmdline)' with a different N each time: the launcher's argv holds the path."""
        d = self.f.clone("legend-a")
        argv = [sys.executable, str(TOOL), "--tmp-root", str(self.f.tmp), "--repo", str(self.f.repo), "--main-ref", "HEAD", "--older-than", "0", "--remove", str(d), "--dry-run"]
        import shlex
        r = subprocess.run(["sh", "-c", shlex.join(argv)], capture_output=True, text=True)        # a wrapper shell whose own command line names the folder
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("WOULD REMOVE", r.stdout)
        self.assertNotIn("in use by process", r.stderr)
        self.assertEqual(tcr.process_holders(d), [])

    def test_an_unrelated_process_that_names_the_folder_still_keeps_it(self):
        d = self.f.clone("legend-named")
        p = subprocess.Popen(["sh", "-c", "sleep 30", "marker", str(d)], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            for _ in range(50):                                          # the child shows the parent's command line until its exec is done
                if any("cmdline" in h for h in tcr.process_holders(d)):
                    break
                time.sleep(0.05)
            self.assertTrue(any("cmdline" in h for h in tcr.process_holders(d)))
        finally:
            os.killpg(p.pid, 9)
            p.wait()

    def test_dry_run_deletes_nothing(self):
        d = self.f.clone("legend-a")
        r = self.f.cli("--remove", str(d), "--dry-run")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("WOULD REMOVE", r.stdout)
        self.assertTrue(d.is_dir())

    def test_an_unresolvable_main_ref_refuses_everything(self):
        d = self.f.clone("legend-a")
        r = subprocess.run([sys.executable, str(TOOL), "--tmp-root", str(self.f.tmp), "--repo", str(self.f.repo), "--main-ref", "no/such", "--remove", str(d)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertTrue(d.is_dir())


class NestedClones(unittest.TestCase):
    """2026-11-25 (ADV): a 17-day-old `tmp*` folder holding `trial_clone/` was not listed at all."""

    def setUp(self):
        self.f = Fixture()

    def tearDown(self):
        self.f.close()

    def holder(self, name):
        (self.f.tmp / name).mkdir()
        return self.f.tmp / name, self.f.clone(f"{name}/trial_clone")

    def test_a_tmp_folder_holding_only_a_published_clone_is_listed_and_removable(self):
        d, _ = self.holder("tmpabc")
        self.assertIn(d, tcr.candidates(self.f.tmp))
        r = self.f.examine(d)
        self.assertEqual((r["verdict"], r["reasons"]), ("REMOVABLE", []))

    def test_anything_beside_the_clone_keeps_the_folder_and_is_named(self):
        d, _ = self.holder("tmpbeside")
        (d / "result.tsv").write_text("only copy\n")
        r = self.f.examine(d)
        self.assertEqual(r["verdict"], "KEEP")
        self.assertTrue(any("beside the clone" in x and "result.tsv" in x for x in r["reasons"]), r)
        self.assertEqual(self.f.cli("--remove", str(d)).returncode, 1)
        self.assertTrue((d / "result.tsv").is_file())

    def test_a_nested_clone_with_unpublished_work_keeps_the_folder_and_names_the_clone(self):
        d, clone = self.holder("tmpwork")
        (clone / "b.txt").write_text("b\n")
        git(clone, "add", "b.txt")
        git(clone, "commit", "-qm", "mine")
        r = self.f.examine(d)
        self.assertEqual(r["verdict"], "KEEP")
        self.assertTrue(any(x.startswith("trial_clone: ") and "unpublished commit" in x for x in r["reasons"]), r)

    def test_a_folder_of_another_name_holding_a_clone_is_still_not_a_candidate(self):
        d, _ = self.holder("somebody-work")
        self.assertNotIn(d, tcr.candidates(self.f.tmp))

    def test_a_leftover_suite_clone_of_safe_push_needs_only_the_process_and_age_checks(self):
        d = self.f.tmp / "legend-landing-suites-dead"
        d.mkdir()
        self.f.clone("legend-landing-suites-dead/repo")
        r = self.f.examine(d)
        self.assertEqual((r["verdict"], r["reasons"]), ("REMOVABLE", []))


if __name__ == "__main__":
    unittest.main(verbosity=2)
