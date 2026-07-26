#!/usr/bin/env python3
"""Dependency-free tests for the exploratory helix analyser."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("md_helix_analyze.py")
spec = importlib.util.spec_from_file_location("md_helix_analyze", SCRIPT)
analyser = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(analyser)


class MdHelixAnalyseTests(unittest.TestCase):
    def test_dry_run_requires_no_optional_dependencies(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--dry-run"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("EXPLO", json.loads(result.stdout)["status"])

    def test_aggregate_preserves_replicates_without_claiming_a_verdict(self) -> None:
        runs = {system: [] for system in analyser.SYSTEMS}
        runs["WT"] = [
            {"helix_hbond_occupancy": 0.8, "helix_rmsf_nm": 0.1},
            {"helix_hbond_occupancy": 0.6, "helix_rmsf_nm": 0.2},
        ]
        payload = analyser.report(runs)
        self.assertEqual("NOT_AUTOMATED", payload["decision"])
        self.assertEqual(2, payload["summary"]["WT"]["n"])
        self.assertAlmostEqual(0.7, payload["summary"]["WT"]["occupancy_mean"])

    def test_topological_bond_is_explicitly_excluded(self) -> None:
        self.assertEqual(226, analyser.EXCLUDED_HBOND_START)
        self.assertIn("not dynamic evidence", analyser.report({})["topological_exclusion"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
