#!/usr/bin/env python3
"""The release runner names any suite that writes a tracked file under a guarded tree.

On 2026-09-10, during an unattended run, 54 tracked dossiers were overwritten with the seven
bytes "touched" while suites were being exercised by three sessions at once. No suite, tool
or transcript contained that literal, and the runner could not say which suite did it: it
measured exit codes and nothing else. `tracked_state` is the half that can be tested in
isolation; the half that wires it into the loop is asserted at the source, because running
the real runner against a fixture that writes a real tracked file is the incident.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_release_regressions as runner  # noqa: E402


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


class TrackedStateSeesWorkingTreeWrites(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "config", "user.email", "t@example.invalid")
        git(self.repo, "config", "user.name", "t")
        (self.repo / "disease-models").mkdir()
        self.dossier = self.repo / "disease-models" / "PMID1.md"
        self.dossier.write_text("# a real dossier\n", encoding="utf-8")
        (self.repo / "scratch.md").write_text("untracked-tree file\n", encoding="utf-8")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-q", "-m", "seed")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_an_unstaged_overwrite_changes_the_state(self) -> None:
        """The index blob does not move on a plain write; the working tree hash must."""
        before = runner.tracked_state(("disease-models",), root=self.repo)
        self.dossier.write_text("touched", encoding="utf-8")
        after = runner.tracked_state(("disease-models",), root=self.repo)
        self.assertNotEqual(before, after)
        self.assertEqual({"disease-models/PMID1.md"},
                         {p for p, _ in set(after.items()) ^ set(before.items())})

    def test_a_write_outside_the_guarded_trees_is_not_reported(self) -> None:
        before = runner.tracked_state(("disease-models",), root=self.repo)
        (self.repo / "scratch.md").write_text("changed\n", encoding="utf-8")
        self.assertEqual(before, runner.tracked_state(("disease-models",), root=self.repo))

    def test_restoring_the_bytes_restores_the_state(self) -> None:
        before = runner.tracked_state(("disease-models",), root=self.repo)
        self.dossier.write_text("touched", encoding="utf-8")
        self.dossier.write_text("# a real dossier\n", encoding="utf-8")
        self.assertEqual(before, runner.tracked_state(("disease-models",), root=self.repo))

    def test_the_guarded_trees_include_the_ones_the_incident_hit(self) -> None:
        self.assertIn("disease-models", runner.GUARDED_TREES)
        for tree in ("governance", "roles", "framework/protocols", "ledger"):
            self.assertIn(tree, runner.GUARDED_TREES)


class TheMtimeVerdictExoneratesByArithmetic(unittest.TestCase):
    """A peer's edit outside the suite's window is not the suite's; inside stays ambiguous."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name) / "f.md"
        self.path.write_text("x", encoding="utf-8")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_an_edit_before_the_window_is_not_the_suite(self) -> None:
        now = self.path.stat().st_mtime
        self.assertIn("BEFORE THE SUITE", runner.mtime_verdict(self.path, now + 100, now + 200))

    def test_an_edit_after_the_window_is_not_the_suite(self) -> None:
        now = self.path.stat().st_mtime
        self.assertIn("AFTER THE SUITE", runner.mtime_verdict(self.path, now - 200, now - 100))

    def test_an_edit_inside_the_window_stays_ambiguous_and_says_so(self) -> None:
        now = self.path.stat().st_mtime
        verdict = runner.mtime_verdict(self.path, now - 10, now + 10)
        self.assertIn("INSIDE", verdict)
        self.assertIn("concurrent editor", verdict)

    def test_a_deleted_path_does_not_crash_the_runner(self) -> None:
        self.path.unlink()
        self.assertIn("unavailable", runner.mtime_verdict(self.path, 0.0, 1.0))


class TheLoopIsWired(unittest.TestCase):
    """Asserted at the source: the runner cannot be run against a fixture repo."""

    def setUp(self) -> None:
        self.source = (ROOT / "scripts" / "run_release_regressions.py").read_text(encoding="utf-8")

    def test_state_is_taken_after_every_suite_and_a_writer_fails_the_verdict(self) -> None:
        self.assertRegex(self.source, r"after = tracked_state\(GUARDED_TREES\)")
        self.assertIn("TRACKED_FILES_WRITTEN_BY_SUITE", self.source)
        self.assertIn("if failures or writers:", self.source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
