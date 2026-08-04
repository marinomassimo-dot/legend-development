#!/usr/bin/env python3
"""The aggregate release verdict must disclose skipped verification."""
from __future__ import annotations

import importlib.util
import io
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
                # We are already running from a legitimate source archive. Copy only
                # the runner and its selected target, preserving the no-.git condition.
                for relative in ("scripts/run_release_regressions.py", PROTOCOL_TEST,
                                 "disease-models/wwox/analysis/scripts/dismech_independent_protocol.py",
                                 "disease-models/wwox/analysis/scripts/derive_dismech_sidecar.py",
                                 "disease-models/wwox/analysis/data/dismech_phase2_baseline.json",
                                 "disease-models/wwox/analysis/data/dismech_blind_input_manifest.json",
                                 "disease-models/wwox/analysis/data/dismech_blind_receipt_projection.jsonl",
                                 "disease-models/wwox/analysis/data/dismech_canonicalisation_v1.json",
                                 "disease-models/wwox/analysis/data/dismech_sidecar_016_024_035.jsonl",
                                 "disease-models/wwox/analysis/dismech_blind_derivation_contract.md",
                                 "disease-models/wwox/registries/claim_registry_current.md",
                                 "disease-models/wwox/registries/paper_registry_current.md",
                                 "disease-models/wwox/registries/fulltext_read_receipts.jsonl"):
                    source, target = ROOT / relative, archive_root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(source.read_bytes())

            result = subprocess.run(
                [sys.executable, "scripts/run_release_regressions.py",
                 "--only", PROTOCOL_TEST], cwd=archive_root,
                capture_output=True, text=True)
        combined = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, combined)
        self.assertIn("REGRESSION VERDICT: PASS WITH SKIPS (1 targets, 1 skipped)", combined)
        self.assertIn("Git object database absent", combined)
        self.assertNotIn("REGRESSION VERDICT: PASS (1 targets)", combined)


if __name__ == "__main__":
    unittest.main(verbosity=2)
