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


class VerdictFormattingTests(unittest.TestCase):
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
