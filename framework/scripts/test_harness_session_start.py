#!/usr/bin/env python3
"""Weekly scouting is due until there is a correctly dated, actually triaged report."""
import datetime as dt
import tempfile
import unittest
from pathlib import Path

import harness_session_start as hs


class WeeklyScout(unittest.TestCase):
    def test_iso_year_boundary_and_missing_monday_are_due(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for day in (dt.date(2026, 12, 28), dt.date(2027, 1, 3)):
                result = hs.scout_status(root, day)
                self.assertEqual("2026-W53", result["week"])
                self.assertEqual("SCOUT_DUE", result["status"])

    def test_file_existence_and_triaged_label_are_not_completion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day = dt.date(2026, 9, 7)
            path = root / hs.scout_status(root, day)["report"]
            path.parent.mkdir(parents=True)
            path.write_text("empty placeholder")
            self.assertEqual("INVALID_REPORT", hs.scout_status(root, day)["status"])
            header = "---\nrecord_type: HARNESS_SCOUT\nweek: 2026-W37\nstatus: TRIAGED\n---\n"
            path.write_text(header)
            self.assertEqual("TRIAGE_DUE", hs.scout_status(root, day)["status"])
            path.write_text(header + "| 1 | tool | url | adds | 2 | MIT | small | WATCH | |\n")
            self.assertEqual("TRIAGE_DUE", hs.scout_status(root, day)["status"])
            path.write_text(header + "| 1 | tool | url | adds | 2 | MIT | small | WATCH | WATCH |\n")
            self.assertEqual("CURRENT", hs.scout_status(root, day)["status"])
            self.assertEqual("SCOUT_DUE", hs.scout_status(root, day + dt.timedelta(days=7))["status"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
