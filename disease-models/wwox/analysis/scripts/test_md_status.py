#!/usr/bin/env python3
"""Synthetic tests for the read-only MD status monitor."""

from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).with_name("md_status.py")
spec = importlib.util.spec_from_file_location("md_status", SCRIPT)
monitor = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(monitor)


class MdStatusTests(unittest.TestCase):
    def test_complete_and_recent_runs_are_counted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            complete = root / "WT_seed1"
            complete.mkdir()
            (complete / "summary.json").write_text(
                json.dumps({"status": "EXPLO"}), encoding="utf-8"
            )
            running = root / "Q230P_seed1"
            running.mkdir()
            (running / "state.tsv").write_text(
                "Step\tSpeed (ns/day)\n1000\t22.5\n", encoding="utf-8"
            )
            with (
                patch.object(monitor, "process_running", return_value=False),
                patch.object(
                    monitor,
                    "mac_power_state",
                    return_value={"available": False},
                ),
            ):
                result = monitor.inspect(root, expected_runs=2, stale_minutes=40)
        self.assertEqual(1, result["complete_runs"])
        self.assertEqual("incomplete", result["overall"])
        running_result = next(
            item for item in result["runs"] if item["run"] == "Q230P_seed1"
        )
        self.assertEqual("1000", running_result["progress"]["step"])

    def test_stale_state_and_failure_are_visible(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            run = root / "P252A_seed1"
            run.mkdir()
            state = run / "state.tsv"
            state.write_text("Step\tSpeed\n500\t3.0\n", encoding="utf-8")
            old = time.time() - 3_600
            os.utime(state, (old, old))
            (root / "run.log").write_text(
                "P252A_seed1 FAILED: synthetic\n", encoding="utf-8"
            )
            with (
                patch.object(monitor, "process_running", return_value=False),
                patch.object(
                    monitor,
                    "mac_power_state",
                    return_value={"available": False},
                ),
            ):
                result = monitor.inspect(root, expected_runs=1, stale_minutes=40)
        self.assertEqual("failed", result["overall"])
        self.assertEqual("stalled", result["runs"][0]["status"])
        self.assertEqual(1, len(result["failed_records"]))

    def test_invalid_summary_is_not_complete(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            run = root / "P282A_seed1"
            run.mkdir()
            (run / "summary.json").write_text("{", encoding="utf-8")
            with (
                patch.object(monitor, "process_running", return_value=None),
                patch.object(
                    monitor,
                    "mac_power_state",
                    return_value={"available": False},
                ),
            ):
                result = monitor.inspect(root, expected_runs=1, stale_minutes=40)
        self.assertEqual(0, result["complete_runs"])
        self.assertEqual("invalid_summary", result["runs"][0]["status"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
