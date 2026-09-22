#!/usr/bin/env python3
"""Synthetic tests for the read-only MD status monitor."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
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


class ProcessIdentityTests(unittest.TestCase):
    """🔴 THE DEFECT ITSELF, as a fixture, because it shipped green.

    `pgrep -f <pattern>` matches the full command line of *every* process, including
    the one doing the asking. A monitor invoked from a shell that names its target —
    a `watch`, an `until` loop, a wrapper — is itself a match, so it answers "is the
    target alive?" with "yes, I am" and never stops waiting.

    Observed 2026-09-22: two waiters polling `pgrep -f run_release_regressions`, each
    with that string in its own command line, waited 2h08m and 2h04m for themselves
    to terminate while no such job existed.

    🔴 SECOND DEFECT, found only by checking that these tests fail against the old
    code. The original call was `pgrep -qf`. **`-q` does not exist in procps-ng** (it
    is BSD/macOS): on Linux it exits 2 with "invalid option", so `returncode == 0`
    was *always* False and the monitor could never report a running worker at all.
    The `overall == "running"` branch was unreachable on Linux.

    The two interact, which is why the pair is documented here: **on Linux bug 1
    masks bug 2.** A monitor that always says "not running" cannot say "I am
    running". So `test_a_watcher_naming_the_target_does_not_match_itself` passes
    against the pre-fix code *on this platform* — for the wrong reason — and is
    discriminating only on macOS, where `-q` is valid and the self-match is live.
    The test that actually fails pre-fix on Linux is
    `test_a_real_target_is_still_detected`. Both are kept: they cover the same fix
    on different platforms, and neither alone covers both.
    """

    TOKEN = "legend_selfmatch_fixture_target"

    def test_a_watcher_naming_the_target_does_not_match_itself(self) -> None:
        """The waiter's own command line contains the pattern; no target is running."""
        probe = (
            "import importlib.util, sys;"
            f"spec = importlib.util.spec_from_file_location('m', {str(SCRIPT)!r});"
            "m = importlib.util.module_from_spec(spec);"
            "spec.loader.exec_module(m);"
            f"print(m.process_running({self.TOKEN!r}))"
        )
        # The token is placed in this child's OWN argv, so `pgrep -f` matches it.
        completed = subprocess.run(
            [sys.executable, "-c", probe, f"--pretending-to-watch={self.TOKEN}"],
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
        self.assertEqual("", completed.stderr.strip(), completed.stderr)
        self.assertEqual(
            "False",
            completed.stdout.strip(),
            "a watcher whose own command line names the target reported the target "
            "as running — the query answered itself",
        )

    def test_a_real_target_is_still_detected(self) -> None:
        """Excluding self must not blind the monitor to a genuine worker."""
        with tempfile.TemporaryDirectory() as temporary:
            script = Path(temporary) / f"{self.TOKEN}.py"
            script.write_text("import time; time.sleep(60)\n", encoding="utf-8")
            worker = subprocess.Popen([sys.executable, str(script)])
            try:
                deadline = time.monotonic() + 10
                seen = False
                while time.monotonic() < deadline:
                    if monitor.process_running(self.TOKEN):
                        seen = True
                        break
                    time.sleep(0.1)
                self.assertTrue(seen, "a genuinely running worker was not detected")
            finally:
                worker.kill()
                worker.wait(timeout=10)

    def test_the_waiter_terminates_once_the_target_exits(self) -> None:
        """The end-to-end property the deadlock violated."""
        with tempfile.TemporaryDirectory() as temporary:
            script = Path(temporary) / f"{self.TOKEN}.py"
            script.write_text("import time; time.sleep(60)\n", encoding="utf-8")
            worker = subprocess.Popen([sys.executable, str(script)])
            worker.kill()
            worker.wait(timeout=10)
            deadline = time.monotonic() + 10
            while time.monotonic() < deadline:
                if not monitor.process_running(self.TOKEN):
                    break
                time.sleep(0.1)
            else:
                self.fail("waiter never observed the target exit")

    def test_a_recorded_pid_beats_the_name(self) -> None:
        """Identity is authoritative: a dead PID is dead whatever shares its name."""
        with tempfile.TemporaryDirectory() as temporary:
            pid_file = Path(temporary) / "worker.pid"
            worker = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
            pid_file.write_text(str(worker.pid), encoding="utf-8")
            try:
                self.assertTrue(monitor.process_running("anything", pid_file=pid_file))
            finally:
                worker.kill()
                worker.wait(timeout=10)
            self.assertFalse(monitor.process_running("anything", pid_file=pid_file))

    def test_no_platform_specific_pgrep_flag_is_used(self) -> None:
        """`-q` is BSD/macOS only; procps-ng exits 2 and the result reads as False.

        Guards the silent-false-negative half of the defect, which no behavioural
        test can catch on a platform where the flag happens to be valid.
        """
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertNotIn(
            '"-qf"',
            source,
            "pgrep -q is not portable: procps-ng rejects it and the monitor then "
            "reports every worker as stopped",
        )
        self.assertNotIn('"-q"', source)

    def test_an_unreadable_pid_file_falls_back_rather_than_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "absent.pid"
            self.assertIsNotNone(monitor.process_running(self.TOKEN, pid_file=missing))


if __name__ == "__main__":
    unittest.main(verbosity=2)
