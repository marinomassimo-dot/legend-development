#!/usr/bin/env python3
"""Dependency-free tests for the public exploratory MD pilot."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("md_q230p_pilot.py")
ROOT = SCRIPT.resolve().parents[4]
spec = importlib.util.spec_from_file_location("md_q230p_pilot", SCRIPT)
pilot = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(pilot)


class MdPilotTests(unittest.TestCase):
    def test_public_variant_set(self) -> None:
        self.assertEqual(
            {"WT", "Q230P", "P252A", "P282A"}, set(pilot.MUTATIONS)
        )

    def test_dry_run_requires_no_optional_dependencies(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--variant",
                "Q230P",
                "--dry-run",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("EXPLO", payload["status"])
        self.assertIn("not biological evidence", payload["purpose"])

    def test_missing_input_fails_before_loading_dependencies(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "missing.pdb"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--variant",
                    "WT",
                    "--input",
                    str(missing),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(1, completed.returncode)
        self.assertIn("input PDB does not exist", completed.stderr)

    def test_optional_environment_and_outputs_are_declared(self) -> None:
        environment = (ROOT / "environment-md.yml").read_text(encoding="utf-8")
        for dependency in ("openmm=8.1.1", "pdbfixer=1.12", "mdtraj=1.10.3"):
            self.assertIn(dependency, environment)
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("md-output/", gitignore)
        self.assertIn("*.dcd", gitignore)


if __name__ == "__main__":
    unittest.main(verbosity=2)
