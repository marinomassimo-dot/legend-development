#!/usr/bin/env python3
"""Dependency-free tests for the public exploratory MD screen."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("md_helix_screen.py")


class MdHelixScreenTests(unittest.TestCase):
    def test_dry_run_is_clean_clone_executable(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--variant",
                "Q230P",
                "--seed",
                "1",
                "--dry-run",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual("EXPLO", payload["status"])
        self.assertEqual(["GLN-230-PRO"], payload["mutations"])
        self.assertIn("not biological evidence", payload["warning"])

    def test_invalid_temperature_fails_fast(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--variant",
                "WT",
                "--seed",
                "1",
                "--temp-k",
                "900",
                "--dry-run",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("--temp-k must be", result.stderr)

if __name__ == "__main__":
    unittest.main(verbosity=2)
