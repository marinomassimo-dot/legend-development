#!/usr/bin/env python3
"""Weekly scouting is due until there is a correctly dated, actually triaged report."""
import datetime as dt
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import harness_session_start as hs

ROOT = Path(__file__).resolve().parents[2]
STATES = {"SCOUT_DUE", "INVALID_REPORT", "TRIAGE_DUE", "CURRENT"}


def run_main(*argv: str) -> tuple[int, str]:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        code = hs.main(list(argv))
    return code, buffer.getvalue()


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


class TheEntryPointIsDriven(unittest.TestCase):
    """``main`` -> ``startup``: both output modes, both actors, and the argparse refusal.

    Nothing here entered ``main`` or ``startup`` until 2026-09-10; the week arithmetic was
    tested and the command a session actually runs was not (retrospective § 9.3).
    """

    def test_junior_over_a_bare_root_is_scout_due_in_both_modes(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run_main("--actor", "junior-harness", "--root", tmp, "--json")
            self.assertEqual(code, 0)
            payload = json.loads(out)
            self.assertEqual(payload["status"], "SCOUT_DUE")
            self.assertEqual(payload["actor"], "junior-harness")
            self.assertIn("run legend-harness-scout", payload["action"])
            self.assertNotIn("branch_hygiene", payload, "the Junior gets no hygiene sweep")

            code, out = run_main("--actor", "junior-harness", "--root", tmp)
            self.assertEqual(code, 0)
            self.assertRegex(out, r"^HARNESS_SCOUT \d{4}-W\d{2} SCOUT_DUE — governance/candidates/")
            self.assertIn("run legend-harness-scout", out)

    def test_plan_outside_a_repository_gets_a_named_unavailability_not_a_crash(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run_main("--actor", "plan", "--root", tmp, "--json")
            self.assertEqual(code, 0)
            payload = json.loads(out)
            self.assertTrue(str(payload["branch_hygiene"]).startswith("UNAVAILABLE:"),
                            payload["branch_hygiene"])

    def test_an_unknown_actor_is_refused_by_the_parser(self):
        with self.assertRaises(SystemExit) as caught:
            run_main("--actor", "mirror")
        self.assertEqual(caught.exception.code, 2)


class TheRealCheckoutIsRead(unittest.TestCase):
    """The command Harness Engineering runs at session start, over this checkout."""

    def test_plan_startup_over_the_real_root(self):
        code, out = run_main("--actor", "plan", "--root", str(ROOT), "--json")
        self.assertEqual(code, 0)
        payload = json.loads(out)
        self.assertIn(payload["status"], STATES)
        self.assertEqual(payload["report"], f"governance/candidates/HARNESS-SCOUT-{payload['week']}.md")
        self.assertEqual(payload["status"] == "SCOUT_DUE", not (ROOT / payload["report"]).exists())
        # build_report's totals is a one-line summary; outside a repository it is UNAVAILABLE.
        hygiene = payload["branch_hygiene"]
        if hygiene.startswith("UNAVAILABLE:"):
            self.assertNotIn("overdue_branches", payload)
        else:
            self.assertRegex(hygiene, r"^\d+ branches · \d+ ahead-of-main commits total · "
                                      r"\d+ LAND_OVERDUE · \d+ DELETE_READY$")
            self.assertIsInstance(payload["overdue_branches"], list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
