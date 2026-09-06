#!/usr/bin/env python3
"""The aggregate release verdict must disclose skipped verification."""
from __future__ import annotations

import importlib.util
import io
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = ROOT / "scripts/run_release_regressions.py"
SPEC = importlib.util.spec_from_file_location("release_runner", RUNNER_PATH)
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)
PROTOCOL_TEST = "disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py"


class EveryTestSuiteIsActuallyRun(unittest.TestCase):
    """🔴 A suite nobody runs is not a suite, and the inventory is hand-maintained.

    `TESTS` in the runner is a literal tuple, so a new file is only verified if its author
    remembers to register it. Two did not: `test_dossier_quote_audit.py` and
    `test_reading_state.py` were both written, both green, and neither was in the release
    battery — which reported PASS over 57 targets while ignoring them.

    `test_release_surface.py` already checks a convention on new script files (the executable
    bit) and caught a missing one the same day it shipped. It just checks the wrong level:
    whether the file looks right, not whether anything runs it. Same defence, next site — the
    uneven-application failure this repository keeps finding in itself.
    """

    # Since 2026-09-06 the runner discovers suites itself (`discover_tests`), so "every
    # tracked test file is in TESTS" holds by construction and a test restating it with the
    # same `git ls-files` call could never fail (blind review finding 4). What can still
    # go wrong is now asserted instead: an exclusion that names nothing on disk, a priority
    # entry that no longer exists, and a battery that is not exactly discovery minus the
    # recorded exclusions.

    def test_the_battery_is_discovery_minus_recorded_exclusions(self) -> None:
        discovered = set(runner.discover_tests(ROOT))
        expected = (set(runner.PRIORITY_TESTS) | discovered) - set(runner.NOT_RUN_BY_DESIGN)
        self.assertEqual(expected, set(runner.TESTS))
        for path, reason in runner.NOT_RUN_BY_DESIGN.items():
            with self.subTest(excluded=path):
                self.assertTrue((ROOT / path).is_file(), "an exclusion must name a real suite")
                self.assertTrue(reason.strip(), "an exclusion must carry its reason")
                self.assertNotIn(path, runner.TESTS)

    def test_an_exclusion_actually_removes_the_suite(self) -> None:
        """Positive control for the mechanism the test above relies on."""
        self.assertEqual(("a.py", "b.py"),
                         runner.battery(("a.py",), ("b.py", "c.py"), {"c.py": "why"}))
        self.assertEqual(("b.py",),
                         runner.battery(("a.py",), ("a.py", "b.py"), {"a.py": "priority too"}))

    def test_the_runner_names_no_file_that_is_gone(self) -> None:
        """The other direction: a target that no longer exists would fail loudly, but a
        target renamed to something already covered would quietly shrink the battery."""
        absent = sorted(name for name in runner.TESTS if not (ROOT / name).is_file())
        self.assertEqual(absent, [], "TESTS names files that do not exist")


class VerdictFormattingTests(unittest.TestCase):
    def test_discovery_includes_untracked_suites_and_excludes_ignored_suites(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            (root / "test_new.py").write_text("pass\n")
            (root / "test_ignored.py").write_text("pass\n")
            (root / ".gitignore").write_text("test_ignored.py\n")
            self.assertEqual(("test_new.py",), runner.discover_tests(root))

    def test_archive_discovery_prunes_nested_checkouts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "test_source.py").write_text("pass\n")
            peer = root / "peer"
            peer.mkdir()
            (peer / ".git").write_text("gitdir: elsewhere")
            (peer / "test_peer.py").write_text("pass\n")
            self.assertEqual(("test_source.py",), runner.discover_tests(root))

    def test_plain_pass_requires_zero_skips(self) -> None:
        self.assertEqual(runner.format_success_verdict(40, []),
                         ["REGRESSION VERDICT: PASS (40 targets)"])

    def test_skips_are_counted_and_named(self) -> None:
        lines = runner.format_success_verdict(
            40, [(PROTOCOL_TEST, "Git object database absent")])
        self.assertEqual(lines[0],
                         "REGRESSION VERDICT: PASS WITH SKIPS (40 targets, 1 skipped)")
        self.assertIn("Git object database absent", lines[1])

    def test_unittest_skip_reason_is_parsed(self) -> None:
        output = (
            "test_anchor (...) ... skipped 'Git object database absent; verification unavailable'\n"
            "OK (skipped=1)\n")
        self.assertEqual(runner.extract_skip_reasons(output),
                         ["Git object database absent; verification unavailable"])


class ArchiveVerdictIntegrationTests(unittest.TestCase):
    def test_archive_runner_qualifies_git_anchor_skip(self) -> None:
        with tempfile.TemporaryDirectory(prefix="legend-runner-archive-") as temporary:
            archive_root = Path(temporary) / "archive"
            archive_root.mkdir()
            git_available = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"], cwd=ROOT,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
            if git_available:
                completed = subprocess.run(
                    ["git", "archive", "HEAD"], cwd=ROOT, check=True,
                    capture_output=True)
                with tarfile.open(fileobj=io.BytesIO(completed.stdout), mode="r:") as archive:
                    archive.extractall(archive_root)
            else:
                # We are already running from a legitimate source archive. Copy its
                # complete public surface, preserving the no-.git condition and avoiding
                # a second, hand-maintained approximation of protocol dependencies.
                shutil.copytree(ROOT, archive_root, dirs_exist_ok=True)

            result = subprocess.run(
                [sys.executable, "scripts/run_release_regressions.py",
                 "--only", PROTOCOL_TEST], cwd=archive_root,
                capture_output=True, text=True)
        combined = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, combined)
        # The property under test is that a git-anchored verification which cannot run is
        # REPORTED as unrun, not folded into a clean PASS. How MANY such tests exist is
        # incidental and grows every time another check learns to fail closed without a git
        # object database — which is the desirable direction. Pinning "1 skipped" made that
        # improvement look like a regression: adding the sealed-blob skip to
        # `test_two_file_reseal_disagrees_with_pinned_git_tree` turned this red while the
        # runner was doing exactly what it should.
        self.assertIn("REGRESSION VERDICT: PASS WITH SKIPS (1 targets,", combined)
        self.assertIn("Git object database absent", combined)
        self.assertNotIn("REGRESSION VERDICT: PASS (1 targets)", combined)


if __name__ == "__main__":
    unittest.main(verbosity=2)
