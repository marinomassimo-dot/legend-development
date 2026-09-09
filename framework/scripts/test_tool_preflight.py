#!/usr/bin/env python3
"""Tests for tool_preflight.py.

The mutation these pin: collapsing REQUIRED and optional into one "missing" state. That
conflation is the whole point of the tool — a fresh container legitimately lacks optional
extractors, and if their absence raised, the check would be disabled within a day and the
REQUIRED signal would be lost with it.
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("tool_preflight", Path(__file__).parent / "tool_preflight.py")
tp = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tp)


class TestProbe(unittest.TestCase):
    def test_python_probe_finds_stdlib(self):
        self.assertTrue(tp.probe("json", "python"))

    def test_python_probe_rejects_absent_module(self):
        self.assertFalse(tp.probe("definitely_not_a_module_xyzzy", "python"))

    def test_binary_probe_finds_python(self):
        self.assertTrue(tp.probe("python3", "binary"))

    def test_binary_probe_rejects_absent_binary(self):
        self.assertFalse(tp.probe("definitely_not_a_binary_xyzzy", "binary"))


class TestRun(unittest.TestCase):
    def setUp(self):
        self.result = tp.run(ROOT)

    def test_every_declared_tool_is_reported(self):
        self.assertEqual(len(self.result["tools"]), len(tp.TOOLS))

    def test_counts_are_consistent(self):
        self.assertEqual(self.result["present"] + self.result["missing"], len(tp.TOOLS))

    def test_required_and_optional_are_separate_states(self):
        """🔴 The mutation guard. Merging these two lists must turn this test red."""
        req = set(self.result["missing_required"])
        opt = set(self.result["missing_optional"])
        self.assertEqual(req & opt, set(), "a tool cannot be both required-missing and optional-missing")
        for row in self.result["tools"]:
            if not row["present"]:
                target = req if row["required"] else opt
                other = opt if row["required"] else req
                self.assertIn(row["tool"], target)
                self.assertNotIn(row["tool"], other)

    def test_referenced_by_points_at_real_files(self):
        for row in self.result["tools"]:
            for rel in row["referenced_by"]:
                self.assertTrue((ROOT / rel).exists(), f"{rel} does not exist")

    def test_preflight_does_not_report_itself(self):
        for row in self.result["tools"]:
            self.assertNotIn("framework/scripts/tool_preflight.py", row["referenced_by"])


class TestCli(unittest.TestCase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, str(Path(__file__).parent / "tool_preflight.py"), "--root", str(ROOT), *args],
            capture_output=True, text=True)

    def test_discovery_not_a_gate_exits_zero(self):
        """Absence of an OPTIONAL tool must never raise status, or the check gets switched off."""
        self.assertEqual(self._run().returncode, 0)

    def test_fail_on_missing_ignores_optional_absences(self):
        result = tp.run(ROOT)
        proc = self._run("--fail-on-missing")
        expected = 1 if result["missing_required"] else 0
        self.assertEqual(proc.returncode, expected)

    def test_json_mode_is_parseable(self):
        import json
        proc = self._run("--json")
        self.assertEqual(proc.returncode, 0)
        payload = json.loads(proc.stdout)
        self.assertIn("tools", payload)


if __name__ == "__main__":
    unittest.main()
