#!/usr/bin/env python3
"""process_wait.py waits by identity, always ends, and cannot be satisfied by its own name.

Each case is the property the self-matching `pgrep -f` waiters violated (2026-09-22 twice,
2026-09-24 once): the waiter must finish when THE target finishes, must not care what else
shares the target's name — including itself — and must stop at its deadline regardless.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "process_wait.py"
sys.path.insert(0, str(HERE))
import process_wait as pw  # noqa: E402

TOKEN = "legend_process_wait_fixture_target"


def sleeper(seconds: float) -> subprocess.Popen:
    # The fixture's argv carries TOKEN, so a textual matcher would find it.
    return subprocess.Popen([sys.executable, "-c", f"import time; time.sleep({seconds})", TOKEN])


def run(*args: str, timeout: float = 60) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(TOOL), *args],
                          capture_output=True, text=True, timeout=timeout)


class WaitsByIdentity(unittest.TestCase):
    def test_a_live_process_is_waited_for_until_it_exits(self) -> None:
        target = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(1.5)"])
        try:
            started = time.monotonic()
            done = run("--pid", str(target.pid), "--timeout", "30", "--interval", "0.1")
            self.assertEqual(done.returncode, 0, done.stderr)
            self.assertGreater(time.monotonic() - started, 1.0, "returned before the target ended")
        finally:
            target.kill()
            target.wait(timeout=10)

    def test_an_already_ended_process_returns_promptly(self) -> None:
        target = subprocess.Popen([sys.executable, "-c", "pass"])
        target.wait(timeout=10)
        started = time.monotonic()
        done = run("--pid", str(target.pid), "--timeout", "30")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertLess(time.monotonic() - started, 5)

    def test_the_deadline_is_a_bounded_failure(self) -> None:
        target = sleeper(60)
        try:
            started = time.monotonic()
            done = run("--pid", str(target.pid), "--timeout", "1", "--interval", "0.1")
            self.assertEqual(done.returncode, pw.TIMED_OUT, done.stderr)
            self.assertLess(time.monotonic() - started, 10)
        finally:
            target.kill()
            target.wait(timeout=10)

    def test_timeout_is_required(self) -> None:
        self.assertEqual(run("--pid", "1").returncode, pw.INVALID)
        self.assertEqual(run("--pid", "1", "--timeout", "0").returncode, pw.INVALID)

    def test_an_unrelated_process_with_the_same_name_is_irrelevant(self) -> None:
        target, twin = sleeper(1), sleeper(60)
        try:
            done = run("--pid", str(target.pid), "--timeout", "30", "--interval", "0.1")
            self.assertEqual(done.returncode, 0, "a same-named survivor kept the wait open")
        finally:
            for proc in (target, twin):
                proc.kill()
                proc.wait(timeout=10)

    def test_a_waiter_whose_command_line_names_the_target_does_not_wait_on_itself(self) -> None:
        """The literal defect: the target's text in the waiter's own argv."""
        target = sleeper(1)
        try:
            done = subprocess.run(
                [sys.executable, str(TOOL), "--pid", str(target.pid), "--timeout", "30",
                 "--interval", "0.1"],
                capture_output=True, text=True, timeout=60,
                env={"PATH": "/usr/bin:/bin", "WATCHING": TOKEN})
            self.assertEqual(done.returncode, 0, done.stderr)
        finally:
            target.kill()
            target.wait(timeout=10)

    def test_waiting_on_itself_or_an_ancestor_is_refused(self) -> None:
        import os
        done = run("--pid", str(os.getpid()), "--timeout", "5")
        self.assertEqual(done.returncode, pw.INVALID, "a wait on an ancestor can only time out")

    def test_malformed_identities_are_rejected(self) -> None:
        for bad in ("", "abc", "-5", "0", "12:x", "12:"):
            with self.subTest(identity=bad):
                self.assertEqual(run("--pid", bad, "--timeout", "5").returncode, pw.INVALID)
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "absent.pid"
            self.assertEqual(run("--pid-file", str(missing), "--timeout", "5").returncode,
                             pw.INVALID)

    def test_a_recycled_pid_is_a_different_process(self) -> None:
        """PID:START pins one incarnation; a live PID with another start time is not it."""
        target = sleeper(60)
        try:
            start = pw.start_ticks(target.pid)
            self.assertIsNotNone(start)
            self.assertTrue(pw.pid_alive(target.pid, start))
            self.assertFalse(pw.pid_alive(target.pid, start + 1))
            done = run("--pid", f"{target.pid}:{start + 1}", "--timeout", "5")
            self.assertEqual(done.returncode, 0, "a stale identity must resolve at once")
        finally:
            target.kill()
            target.wait(timeout=10)

    def test_the_identity_command_records_what_a_pid_file_should_hold(self) -> None:
        target = sleeper(60)
        try:
            shown = run("--identity", str(target.pid))
            self.assertEqual(shown.returncode, 0, shown.stderr)
            self.assertEqual(pw.parse_identity(shown.stdout), (target.pid, pw.start_ticks(target.pid)))
            with tempfile.TemporaryDirectory() as temporary:
                pid_file = Path(temporary) / "job.pid"
                pid_file.write_text(shown.stdout, encoding="utf-8")
                self.assertTrue(pw.process_running("anything", pid_file=pid_file))
                target.kill()
                target.wait(timeout=10)
                self.assertFalse(pw.process_running("anything", pid_file=pid_file))
        finally:
            if target.poll() is None:
                target.kill()
                target.wait(timeout=10)

    def test_an_unreaped_child_counts_as_finished(self) -> None:
        target = subprocess.Popen([sys.executable, "-c", "pass"])
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline and pw._stat_fields(target.pid) and \
                pw._stat_fields(target.pid)[0] != "Z":
            time.sleep(0.05)
        try:
            self.assertFalse(pw.pid_alive(target.pid), "a zombie is finished work")
        finally:
            target.wait(timeout=10)

    def test_a_completion_file_is_waited_for(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            flag = Path(temporary) / "DONE"
            writer = subprocess.Popen([sys.executable, "-c",
                                       f"import time,pathlib; time.sleep(1); pathlib.Path({str(flag)!r}).touch()"])
            try:
                done = run("--file", str(flag), "--timeout", "30", "--interval", "0.1")
                self.assertEqual(done.returncode, 0, done.stderr)
            finally:
                writer.wait(timeout=10)
            gone = Path(temporary) / "NEVER"
            self.assertEqual(run("--file", str(gone), "--timeout", "0.5").returncode, pw.TIMED_OUT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
