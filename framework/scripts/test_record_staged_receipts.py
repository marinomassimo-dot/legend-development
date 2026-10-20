#!/usr/bin/env python3
"""Offline tests for record_staged_receipts: the pure parts (what is unrecorded, the time rule)."""
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import record_staged_receipts as m  # noqa: E402

NOW = datetime(2026, 10, 20, 7, 0, 0, tzinfo=timezone.utc)


class TimeRule(unittest.TestCase):
    def test_future_analysis_at_is_set_to_the_date_and_reported(self):
        out, changed = m.normalise({"analysis_at": "2026-10-20T09:00:00Z", "event_at": "2026-10-20T06:00:00Z"}, NOW)
        self.assertEqual("2026-10-20T00:00:00Z", out["analysis_at"])
        self.assertEqual(["analysis_at"], changed)

    def test_future_event_at_is_set_to_now(self):
        out, changed = m.normalise({"analysis_at": "2026-10-20T01:00:00Z", "event_at": "2026-10-21T00:00:00Z"}, NOW)
        self.assertEqual("2026-10-20T07:00:00Z", out["event_at"])
        self.assertEqual(["event_at"], changed)

    def test_past_times_and_content_are_untouched(self):
        receipt = {"analysis_at": "2026-10-19T01:00:00Z", "event_at": "2026-10-19T02:00:00Z", "x": 1}
        out, changed = m.normalise(receipt, NOW)
        self.assertEqual(receipt, out)
        self.assertEqual([], changed)


class Unrecorded(unittest.TestCase):
    def test_only_events_missing_from_the_ledger_come_back_in_event_id_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / m.LEDGER).parent.mkdir(parents=True)
            (root / m.LEDGER).write_text(json.dumps({"event_id": "FTR-1-B"}) + "\n", encoding="utf-8")
            stage = root / m.STAGING / "scientist-x"
            stage.mkdir(parents=True)
            for name in ("FTR-1-C", "FTR-1-B", "FTR-1-A"):
                (stage / f"{name}.json").write_text(json.dumps({"event_id": name}), encoding="utf-8")
            ids = [item[0] for item in m.unrecorded(root, NOW)]
            self.assertEqual(["FTR-1-A", "FTR-1-C"], ids)


if __name__ == "__main__":
    unittest.main(verbosity=2)
