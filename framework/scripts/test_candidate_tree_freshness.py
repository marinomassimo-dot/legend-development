#!/usr/bin/env python3
"""Regressions for `candidate_tree_freshness.py` and `owned_scratch.py`, on real Git repositories.

The property under test is EXACTNESS: the verdict is about the tree that will be committed or
merged — never the shared working directory. So most tests below make the working directory
and the candidate disagree on purpose, and assert the verdict follows the candidate.

Run: `python3 framework/scripts/test_candidate_tree_freshness.py`
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import candidate_tree_freshness as ctf  # noqa: E402
import owned_scratch  # noqa: E402

SURFACE = "disease-models/toy/registries/toy_surface.md"
INPUT = "disease-models/toy/registries/input.txt"
TOY_GEN = '''\
import argparse, sys
from pathlib import Path
import toy_helper

HEADER = "<!-- Generated file. Regenerate: python3 framework/scripts/toy_gen.py -->\\n"

def render():
    return HEADER + toy_helper.shape(Path("disease-models/toy/registries/input.txt").read_text())

parser = argparse.ArgumentParser()
parser.add_argument("--out", default="")
parser.add_argument("--check", default="")
parser.add_argument("--crash", action="store_true")
args = parser.parse_args()
if Path("CRASH").exists():
    raise RuntimeError("generator bug")
if args.check:
    if Path(args.check).read_text() != render():
        print(f"DRIFT: {args.check}")
        sys.exit(1)
    print("OK")
    sys.exit(0)
Path(args.out).write_text(render())
'''
TOY_HELPER = "def shape(text):\n    return text.upper()\n"
TOY = {"framework/scripts/toy_gen.py": ctf.Generator(
    inputs=("disease-models/{disease}/registries/input.txt",),
    check=("--check", "{surface}"),
    regenerate="python3 framework/scripts/toy_gen.py --out {surface}")}


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True,
                           text=True).stdout.strip()


def scratch_boxes() -> set[Path]:
    return set(Path(tempfile.gettempdir()).glob(ctf.PREFIX + "*"))


class ToyRepo(unittest.TestCase):
    """A repository with one generated surface, its input, its generator and a helper module."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory(prefix="legend-ctf-test-")
        self.addCleanup(self._tmp.cleanup)
        self.repo = Path(self._tmp.name) / "repo"
        self.repo.mkdir()
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "config", "user.name", "ctf-test")
        git(self.repo, "config", "user.email", "ctf@example.invalid")
        self.write("framework/scripts/toy_gen.py", TOY_GEN)
        self.write("framework/scripts/toy_helper.py", TOY_HELPER)
        self.write(INPUT, "alpha\n")
        self.write("unrelated.txt", "x\n")
        self.regenerate()
        self.commit("seed", ".")
        patcher = mock.patch.dict(ctf.GENERATORS, TOY, clear=True)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.boxes_before = scratch_boxes()

    def tearDown(self) -> None:
        def owner(box: Path) -> str:
            try:
                return (box / owned_scratch.OWNER).read_text().split(":")[0].strip()
            except OSError:
                return ""
        mine = {box for box in scratch_boxes() - self.boxes_before
                if owner(box) == str(os.getpid())}
        self.assertEqual(set(), mine, "a candidate tree was left behind")

    def write(self, relative: str, text: str) -> None:
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def regenerate(self) -> None:
        subprocess.run([sys.executable, "framework/scripts/toy_gen.py", "--out", SURFACE],
                       cwd=self.repo, check=True)

    def commit(self, message: str, *paths: str) -> None:
        git(self.repo, "add", "--", *paths)
        git(self.repo, "commit", "-q", "-m", message)

    def branch(self) -> None:
        git(self.repo, "switch", "-q", "-c", "task/x")

    def status_of(self, report: ctf.Report) -> str:
        [result] = [r for r in report.results if r.surface == SURFACE]
        return result.status


class MergeCandidate(ToyRepo):
    def test_a_change_outside_the_inputs_runs_no_check(self):
        self.branch()
        self.write("unrelated.txt", "y\n")
        self.commit("unrelated", "unrelated.txt")
        report = ctf.evaluate(self.repo, tip="task/x", base="main")
        self.assertEqual(ctf.NOT_AFFECTED, self.status_of(report))
        self.assertEqual(0, report.exit_code)

    def test_an_input_landed_without_its_surface_is_stale_with_the_command(self):
        self.branch()
        self.write(INPUT, "beta\n")
        self.commit("input only", INPUT)
        report = ctf.evaluate(self.repo, tip="task/x", base="main")
        self.assertEqual(ctf.STALE, self.status_of(report))
        self.assertEqual(1, report.exit_code)
        self.assertIn("toy_gen.py --out " + SURFACE, ctf.render(report))

    def test_an_input_landed_with_its_regenerated_surface_is_fresh(self):
        self.branch()
        self.write(INPUT, "beta\n")
        self.regenerate()
        self.commit("input and surface", INPUT, SURFACE)
        report = ctf.evaluate(self.repo, tip="task/x", base="main")
        self.assertEqual(ctf.FRESH, self.status_of(report))

    def test_a_generator_dependency_change_triggers_the_check(self):
        """The code closure: toy_gen imports toy_helper, and a helper edit re-renders."""
        self.branch()
        self.write("framework/scripts/toy_helper.py", "def shape(text):\n    return text\n")
        self.commit("helper", "framework/scripts/toy_helper.py")
        report = ctf.evaluate(self.repo, tip="task/x", base="main")
        self.assertEqual(ctf.STALE, self.status_of(report))
        [result] = report.results
        self.assertEqual(["framework/scripts/toy_helper.py"], result.triggers)

    def test_the_base_is_the_current_main_not_the_branch_point(self):
        """main moved on (input + regeneration); the branch touched nothing of the surface.
        The landing changes only unrelated.txt relative to main, so nothing is affected."""
        self.branch()
        self.write("unrelated.txt", "y\n")
        self.commit("unrelated", "unrelated.txt")
        git(self.repo, "switch", "-q", "main")
        self.write(INPUT, "gamma\n")
        self.regenerate()
        self.commit("main moves", INPUT, SURFACE)
        report = ctf.evaluate(self.repo, tip="task/x", base="main")
        self.assertEqual(ctf.NOT_AFFECTED, self.status_of(report))
        self.assertEqual(1, report.changed)

    def test_all_runs_unaffected_checks(self):
        report = ctf.evaluate(self.repo, tip="main", base="main", run_all=True)
        self.assertEqual(ctf.FRESH, self.status_of(report))

    def test_a_conflicted_merge_is_a_candidate_error(self):
        self.branch()
        self.write(INPUT, "branch\n")
        self.commit("b", INPUT)
        git(self.repo, "switch", "-q", "main")
        self.write(INPUT, "main\n")
        self.commit("m", INPUT)
        with self.assertRaises(ctf.CandidateError) as caught:
            ctf.evaluate(self.repo, tip="task/x", base="main")
        self.assertIn("conflicts", str(caught.exception))


class ExactnessAgainstTheWorkingDirectory(ToyRepo):
    def test_paths_mode_ignores_an_unnamed_dirty_input(self):
        """A peer's in-flight input edit is in the workspace but not in this commit."""
        self.write(INPUT, "peer in flight\n")
        self.write("unrelated.txt", "mine\n")
        report = ctf.evaluate(self.repo, mode="paths", paths=["unrelated.txt"])
        self.assertEqual(ctf.NOT_AFFECTED, self.status_of(report))

    def test_paths_mode_sees_a_named_input_without_its_surface(self):
        self.write(INPUT, "receipt appended\n")
        report = ctf.evaluate(self.repo, mode="paths", paths=[INPUT])
        self.assertEqual(ctf.STALE, self.status_of(report))

    def test_paths_mode_fresh_when_the_surface_is_named_too(self):
        self.write(INPUT, "receipt appended\n")
        self.regenerate()
        report = ctf.evaluate(self.repo, mode="paths", paths=[INPUT, SURFACE])
        self.assertEqual(ctf.FRESH, self.status_of(report))

    def test_paths_mode_rejects_a_directory(self):
        with self.assertRaises(ctf.CandidateError):
            ctf.evaluate(self.repo, mode="paths", paths=["disease-models"])

    def test_staged_mode_judges_the_index_not_the_disk(self):
        """Index: input + regenerated surface (fresh). Disk: a further unstaged edit (stale)."""
        self.write(INPUT, "staged\n")
        self.regenerate()
        git(self.repo, "add", INPUT, SURFACE)
        self.write(INPUT, "unstaged afterthought\n")
        report = ctf.evaluate(self.repo, mode="staged")
        self.assertEqual(ctf.FRESH, self.status_of(report))

    def test_candidate_mode_audits_a_landed_commit_against_its_parent(self):
        self.write(INPUT, "landed alone\n")
        self.commit("direct", INPUT)
        report = ctf.evaluate(self.repo, mode="candidate", tip="HEAD")
        self.assertEqual(ctf.STALE, self.status_of(report))


class UnknownIsNeverAPass(ToyRepo):
    def test_an_undeclared_generator_is_a_check_error(self):
        self.write("disease-models/toy/other.md",
                   "<!-- generated by python3 framework/scripts/mystery.py -->\n")
        self.commit("mystery surface", "disease-models/toy/other.md")
        report = ctf.evaluate(self.repo, mode="candidate", tip="HEAD")
        statuses = {r.surface: r.status for r in report.results}
        self.assertEqual(ctf.CHECK_ERROR, statuses["disease-models/toy/other.md"])
        self.assertEqual(2, report.exit_code)

    def test_a_crashing_check_is_a_check_error_not_stale(self):
        self.write("CRASH", "")
        self.write(INPUT, "beta\n")
        self.commit("crash", "CRASH", INPUT)
        report = ctf.evaluate(self.repo, mode="candidate", tip="HEAD")
        self.assertEqual(ctf.CHECK_ERROR, self.status_of(report))
        self.assertEqual(2, report.exit_code)

    def test_the_cli_exits_two_on_an_undeclared_surface(self):
        """The CLI uses the real GENERATORS, which do not declare toy_gen.py."""
        done = subprocess.run([sys.executable, str(HERE / "candidate_tree_freshness.py"),
                               "--repo", str(self.repo), "--merge", "HEAD", "--base", "HEAD", "--all"],
                              capture_output=True, text=True, timeout=120)
        self.assertEqual(2, done.returncode, done.stdout + done.stderr)
        self.assertIn("undeclared generator", done.stdout)


class NoLeftovers(ToyRepo):
    def test_no_worktree_is_ever_registered(self):
        before = git(self.repo, "worktree", "list", "--porcelain").count("worktree ")
        self.branch()
        self.write(INPUT, "beta\n")
        self.commit("input", INPUT)
        ctf.evaluate(self.repo, tip="task/x", base="main")
        self.assertEqual(before, git(self.repo, "worktree", "list", "--porcelain").count("worktree "))

    def test_a_dead_owners_box_is_reaped_and_a_live_one_kept(self):
        child = subprocess.Popen([sys.executable, "-c", "pass"])
        child.wait()
        dead = Path(tempfile.mkdtemp(prefix="legend-reap-test-"))
        (dead / owned_scratch.OWNER).write_text(f"{child.pid}\n")
        live = owned_scratch.make("legend-reap-test-")
        try:
            reaped = owned_scratch.reap("legend-reap-test-")
            self.assertIn(dead, reaped)
            self.assertFalse(dead.exists())
            self.assertTrue(live.exists())
        finally:
            owned_scratch.release(live)
            if dead.exists():
                owned_scratch.release(dead)

    def test_reap_removes_a_registered_worktree_under_a_dead_box(self):
        child = subprocess.Popen([sys.executable, "-c", "pass"])
        child.wait()
        box = Path(tempfile.mkdtemp(prefix="legend-reap-wt-"))
        (box / owned_scratch.OWNER).write_text(f"{child.pid}\n")
        git(self.repo, "worktree", "add", "-q", "--detach", str(box / "tree"), "HEAD")
        (box / "tree" / "planted.txt").write_text("a test's planted edit\n")
        owned_scratch.reap("legend-reap-wt-", self.repo)
        self.assertFalse(box.exists())
        self.assertNotIn(str(box), git(self.repo, "worktree", "list"))


class TheRealDeclarations(unittest.TestCase):
    """The map in this repository: every discovered surface declared, every input real."""

    def test_discovery_is_the_release_suites_own(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import test_generated_surfaces_are_regenerated as suite
        self.assertIs(suite.generated_surfaces, ctf.generated_surfaces)

    def test_every_surface_in_this_checkout_has_a_declared_generator(self):
        for path, scripts in ctf.generated_surfaces(ROOT).items():
            with self.subTest(surface=path.relative_to(ROOT).as_posix()):
                self.assertTrue(scripts & set(ctf.GENERATORS),
                                f"{path} names {sorted(scripts)}, none declared")

    def test_every_declared_generator_and_input_exists(self):
        """A renamed input would make its surface NOT_AFFECTED forever — a silent pass."""
        for script, generator in ctf.GENERATORS.items():
            self.assertTrue((ROOT / script).is_file(), script)
            for pattern in generator.inputs:
                resolved = pattern.format(disease="wwox")
                with self.subTest(script=script, input=resolved):
                    if "*" in resolved:
                        hits = list(ROOT.glob(resolved.replace("/*", "/**/*", 1)))
                    else:
                        hits = [ROOT / resolved] if (ROOT / resolved).exists() else []
                    self.assertTrue(hits, f"{resolved} matches nothing")

    def test_each_generators_own_derived_inputs_are_covered(self):
        """What each generator declares to derived_inputs must trigger its check."""
        cases = {
            "framework/scripts/coverage_report.py": "disease-models/wwox/registries/paper_registry_current.md",
            "framework/scripts/reading_state.py": "disease-models/wwox/registries/fulltext_read_receipts.jsonl",
            "framework/scripts/batch_queue.py": "disease-models/wwox/research/full_text_queue_current.md",
            "framework/scripts/pathograph.py": "disease-models/wwox/research/deepdive_manifests/PMID1.json",
        }
        surfaces = {script: path.relative_to(ROOT).as_posix()
                    for path, scripts in ctf.generated_surfaces(ROOT).items() for script in scripts}
        for script, changed in cases.items():
            with self.subTest(script=script):
                triggers = ctf.triggers_for(ROOT, surfaces[script], script,
                                            ctf.GENERATORS[script], [changed])
                self.assertEqual([changed], triggers)

    def test_a_harness_only_change_triggers_nothing(self):
        surfaces = {script: path.relative_to(ROOT).as_posix()
                    for path, scripts in ctf.generated_surfaces(ROOT).items() for script in scripts}
        for script, generator in ctf.GENERATORS.items():
            if generator.check is None:
                continue
            with self.subTest(script=script):
                self.assertEqual([], ctf.triggers_for(
                    ROOT, surfaces[script], script, generator,
                    ["framework/scripts/task_close.py", "governance/ANNEX_INDEX.md"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
