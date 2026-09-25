#!/usr/bin/env python3
"""Regressions for `quota_state.py`.

🔴 EVERY EXPECTATION HERE IS WRITTEN BY HAND against fixtures written by hand. No test asks
`read_state` what a window is in order to decide what it should have found, and no test reads the
live `~/.claude.json` — a suite that asserted against the real cache would pass on the day the
cache is fresh and fail on the day it is stale, which is the opposite of what it must pin.

The shapes below were copied from the real cache observed on 2026-09-12 and then reduced.
"""

from __future__ import annotations

import json
import sys
import time
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import quota_state as qs      # noqa: E402

FRESH_MS = None               # filled per-test, so a fixture is never accidentally time-dependent


def _write(directory: str, payload: dict, name: str = "config.json") -> Path:
    path = Path(directory) / name
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _cache(fetched_ms: float, windows: dict, limits: list | None = None) -> dict:
    block = {"fetchedAtMs": fetched_ms, "utilization": dict(windows)}
    if limits is not None:
        block["utilization"]["limits"] = limits
    return {"cachedUsageUtilization": block}


class AbsenceIsAResultAndNeverAZero(unittest.TestCase):
    def test_a_config_without_the_key_reports_no_reading(self) -> None:
        with TemporaryDirectory() as tmp:
            state = qs.read_state(_write(tmp, {"somethingElse": 1}))
        self.assertFalse(state["available"])
        self.assertEqual(2, qs.verdict(state, 30)[0])
        self.assertIn("not evidence that quota is unspent", " ".join(state["notes"]))

    def test_a_missing_file_reports_no_reading(self) -> None:
        state = qs.read_state(Path("/nonexistent/claude.json"))
        self.assertFalse(state["available"])
        self.assertEqual(2, qs.verdict(state, 30)[0])

    def test_malformed_json_reports_no_reading_and_says_why(self) -> None:
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "config.json"
            path.write_text("not json", encoding="utf-8")
            state = qs.read_state(path)
        self.assertFalse(state["available"])
        self.assertEqual(2, qs.verdict(state, 30)[0])
        self.assertIn("unreadable", " ".join(state["notes"]))

    def test_a_block_with_no_fetchedAtMs_is_refused_as_a_measurement(self) -> None:
        """A percentage whose age cannot be established is not a reading. The live cache carries
        the key; a client that stopped writing it must not degrade to a silent pass."""
        with TemporaryDirectory() as tmp:
            payload = {"cachedUsageUtilization": {"utilization": {"five_hour": {"utilization": 40}}}}
            state = qs.read_state(_write(tmp, payload))
        self.assertFalse(state["available"])
        self.assertEqual(2, qs.verdict(state, 30)[0])


class AgeIsReadFromTheBlockAndNeverFromTheFile(unittest.TestCase):
    """Observed 2026-09-12 at 21:08 UTC: the config had been rewritten 26 seconds earlier while
    the quota block was 23.5 hours old. Judging freshness by mtime reads the previous day."""

    def test_a_freshly_written_file_with_an_old_block_is_stale(self) -> None:
        with TemporaryDirectory() as tmp:
            old = (time.time() - 23.5 * 3600) * 1000
            path = _write(tmp, _cache(old, {"five_hour": {"utilization": 13,
                                                          "resets_at": "2030-01-01T00:00:00+00:00"}}))
            state = qs.read_state(path)      # the file's mtime is a second old
        self.assertTrue(state["available"])
        self.assertGreater(state["age_minutes"], 1400)
        code, line = qs.verdict(state, 30)
        self.assertEqual(1, code)
        self.assertIn("STALE", line)

    def test_a_recent_block_inside_the_window_is_fresh(self) -> None:
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache((time.time() - 120) * 1000,
                                      {"five_hour": {"utilization": 13,
                                                     "resets_at": "2030-01-01T00:00:00+00:00"}}))
            state = qs.read_state(path)
        self.assertEqual((0, "FRESH"), qs.verdict(state, 30))
        self.assertLess(state["age_minutes"], 5)

    def test_the_output_says_mtime_is_not_the_age(self) -> None:
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache(time.time() * 1000, {"five_hour": {"utilization": 1,
                                                                         "resets_at": None}}))
            state = qs.read_state(path)
        self.assertIn("file mtime is NOT the reading's age", " ".join(state["notes"]))


class APassedResetMeansTheReadingDescribesThePreviousWindow(unittest.TestCase):
    def test_a_reset_in_the_past_fails_even_when_the_block_is_recent(self) -> None:
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache((time.time() - 60) * 1000,
                                      {"five_hour": {"utilization": 13,
                                                     "resets_at": "2020-01-01T00:00:00+00:00"}}))
            state = qs.read_state(path)
        self.assertTrue(state["windows"][0]["reset_passed"])
        code, line = qs.verdict(state, 30)
        self.assertEqual(1, code)
        self.assertIn("RESET", line)

    def test_an_unparseable_reset_is_labelled_and_not_guessed(self) -> None:
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache(time.time() * 1000,
                                      {"five_hour": {"utilization": 5, "resets_at": "soon"}}))
            state = qs.read_state(path)
        self.assertIsNone(state["windows"][0]["reset_passed"])
        self.assertIn("unparseable", state["windows"][0]["resets_at"])


class TheWeeklyWindowIsNotTheFiveHourWindow(unittest.TestCase):
    """The operator's own point: a five-hour reset does not help if another limit still binds.
    On 2026-09-12 the live cache had five_hour at 13 % and a scoped weekly limit at 90 %,
    severity critical, is_active true."""

    def test_both_windows_are_reported_separately(self) -> None:
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache(time.time() * 1000,
                                      {"five_hour": {"utilization": 13, "resets_at": None},
                                       "seven_day": {"utilization": 84, "resets_at": None}}))
            state = qs.read_state(path)
        found = {row["window"]: row["percent"] for row in state["windows"]}
        self.assertEqual(13, found["five_hour"])
        self.assertEqual(84, found["seven_day"])

    def test_a_scoped_weekly_limit_keeps_its_severity_scope_and_binding_flag(self) -> None:
        limits = [{"kind": "weekly_scoped", "group": "weekly", "percent": 90,
                   "severity": "critical", "resets_at": None, "is_active": True,
                   "scope": {"model": {"id": None, "display_name": "Fable"}}}]
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache(time.time() * 1000,
                                      {"five_hour": {"utilization": 13, "resets_at": None}},
                                      limits))
            state = qs.read_state(path)
        row = [r for r in state["windows"] if r["window"] == "limit:weekly_scoped"][0]
        self.assertEqual(90, row["percent"])
        self.assertEqual("critical", row["severity"])
        self.assertTrue(row["is_active"])
        self.assertEqual("Fable", row["scope"])

    def test_a_window_with_a_null_utilization_is_omitted_rather_than_read_as_zero(self) -> None:
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache(time.time() * 1000,
                                      {"five_hour": {"utilization": 13, "resets_at": None},
                                       "seven_day_opus": None,
                                       "extra_usage": {"utilization": None}}))
            state = qs.read_state(path)
        self.assertEqual(["five_hour"], [r["window"] for r in state["windows"]])


class ItRefusesToBeReadAsAnEstimate(unittest.TestCase):
    def test_neither_the_docstring_nor_the_output_converts_context_to_quota(self) -> None:
        self.assertIn("NEVER ESTIMATES QUOTA FROM CONTEXT TOKENS", qs.__doc__ or "")
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache(time.time() * 1000, {"five_hour": {"utilization": 1,
                                                                         "resets_at": None}}))
            state = qs.read_state(path)
        text = qs.render(state, *qs.verdict(state, 30))
        self.assertIn("never estimates quota from context size", text)

    def test_record_appends_one_json_line_per_call_and_keeps_the_exit_code(self) -> None:
        with TemporaryDirectory() as tmp:
            path = _write(tmp, _cache((time.time() - 24 * 3600) * 1000,
                                      {"five_hour": {"utilization": 13, "resets_at": None}}))
            log = Path(tmp) / "readings.jsonl"
            first = qs.main(["record", "--config", str(path), "--log", str(log)])
            second = qs.main(["record", "--config", str(path), "--log", str(log)])
            rows = [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(1, first)
        self.assertEqual(1, second)
        self.assertEqual(2, len(rows))
        for row in rows:
            self.assertIn("read_at", row)
            self.assertIn("STALE", row["verdict"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
