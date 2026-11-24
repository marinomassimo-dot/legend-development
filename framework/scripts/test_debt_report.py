#!/usr/bin/env python3
"""Regressions for `debt_report.py`: fixture trees, no network, the sourcing of every line."""
import contextlib
import io
import json
import tempfile
import time
import unittest
from datetime import datetime, timezone
from pathlib import Path

import debt_report as dr

COVERAGE_MD = """# Corpus coverage

## Coverage

| Depth | Records | Share | What it means |
|---|---:|---:|---|
| **Full text depth** | 310 | 33% | complete |
| Partial full text | 297 | 32% | partial |
| Catalogued only | 310 | 33% | the debt |

## Receipt trace
| Not a depth | 5 | 1% | ignored |
"""


def event(pmid=None, doi=None, depth="partial_fulltext_read", read=()):
    sections = ("abstract", "introduction", "methods", "results", "discussion")
    return {"study_id": {k: v for k, v in (("pmid", pmid), ("doi", doi)) if v},
            "evidence_depth": depth, "coverage": {s: ("read" if s in read else "not_read") for s in sections}}


def tree(tmp: str, files: dict[str, str]) -> Path:
    root = Path(tmp)
    for name, text in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return root


class Coverage(unittest.TestCase):
    def test_only_the_depth_table_rows_are_read(self):
        self.assertEqual(dr.coverage_table(COVERAGE_MD),
                         {"Full text depth": 310, "Partial full text": 297, "Catalogued only": 310})

    def test_latest_and_best_state_differ_when_a_later_receipt_is_narrower(self):
        events = [event("1", depth="complete_fulltext_read", read=("methods", "results")),
                  event("1", depth="partial_fulltext_read", read=("results",)),     # narrower, shallower
                  event("2", depth="partial_fulltext_read", read=("results",)),
                  event("2", depth="complete_fulltext_read", read=("results", "methods")),  # wider
                  event(doi="10.1/x", depth="abstract_only", read=("abstract",))]
        got = dr.receipt_readings(events)
        self.assertEqual(got["studies"], 3)
        self.assertEqual((got["latest_depth"]["complete"], got["best_depth"]["complete"]), (1, 2))
        self.assertEqual(got["latest_depth"]["partial"], 1)
        self.assertEqual((got["multi_receipt_studies"], got["latest_narrower"]), (2, 1))
        self.assertEqual((got["section_flags_lost"], got["section_flags_union"]), (1, 4))

    def test_a_doi_study_is_keyed_by_its_doi_and_equal_sets_are_not_narrower(self):
        got = dr.receipt_readings([event(doi="10.1/X", read=("results",)), event(doi="10.1/x", read=("results",))])
        self.assertEqual((got["studies"], got["multi_receipt_studies"], got["latest_narrower"]), (1, 1, 0))

    def test_only_read_counts_as_read(self):
        e = event("1", read=("results",))
        e["coverage"]["methods"] = "captions_only"
        self.assertEqual(dr.read_sections(e), {"results"})

    def test_the_block_names_its_sources_and_says_which_depth_the_registry_uses(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = tree(tmp, {dr.COVERAGE_MD: COVERAGE_MD})
            lines, data = dr.coverage_block(root, events=[event("1", depth="complete_fulltext_read", read=("results",))])
        text = "\n".join(lines)
        self.assertIn(dr.COVERAGE_MD, text)
        self.assertIn(dr.LEDGER, text)
        self.assertIn("latest-receipt depth", text)
        self.assertIn("best-state depth (deepest receipt, the rule coverage_report uses)", text)
        self.assertEqual(data["table"]["Full text depth"], 310)

    def test_a_missing_page_is_said_not_guessed(self):
        with tempfile.TemporaryDirectory() as tmp:
            lines, data = dr.coverage_block(Path(tmp), events=[])
        self.assertIn("not readable", lines[0])
        self.assertEqual(data["table"], {})


class Tables(unittest.TestCase):
    QUESTIONS = ("qid\tsource_ref\tquestion\tdecision\tkind\tstatus\tpublished_on\tstatus_evidence\tlast_touched\tblock\texec\tclaimed_by\n"
                 "Q1\ts\tq\td\tk\tOPEN\tp\te\t2026-10-31\t\tno\t\n"
                 "Q2\ts\tq\td\tk\tOPEN\tp\te\t2026-11-20\t\tno\t\n"
                 "Q3\ts\tq\td\tk\tCONCLUDED\tp\te\t2026-11-01\t\tno\t\n")
    PORTFOLIO = ("id\ttheme\topportunity\tdecision\tpriority\twhy_now\tnext_action\tstatus\tsources\tmandate_id\tresume_when\toutcome\tupdated_utc\n"
                 "RP-1\tt\to\td\tP1\tw\tn\twaiting\ts\t\tthe operator answers\t\t2026-11-15T10:00:00Z\n"
                 "RP-2\tt\to\td\tP1\tw\tn\twaiting\ts\t\tlater\t\t2026-11-20T10:00:00Z\n"
                 "RP-3\tt\to\td\tP2\tw\tn\tdone\ts\t\t\t\t2026-11-01T10:00:00Z\n")

    def test_open_questions_by_status_and_the_least_recently_touched(self):
        with tempfile.TemporaryDirectory() as tmp:
            lines, data = dr.questions_block(tree(tmp, {dr.OPEN_QUESTIONS: self.QUESTIONS}))
        self.assertIn("3 rows", lines[0])
        self.assertIn(dr.OPEN_QUESTIONS, lines[0])
        self.assertEqual(data["open"], 2)
        self.assertEqual(data["oldest_open"][0], ("Q1", "2026-10-31"))

    def test_portfolio_by_status_and_the_oldest_waiting_row_with_its_resume_when(self):
        with tempfile.TemporaryDirectory() as tmp:
            lines, data = dr.portfolio_block(tree(tmp, {dr.PORTFOLIO: self.PORTFOLIO}))
        self.assertIn(dr.PORTFOLIO, lines[0])
        self.assertIn("oldest waiting: RP-1 since 2026-11-15T10:00:00Z", lines[1])
        self.assertIn("the operator answers", lines[1])
        self.assertEqual(data["oldest_waiting"], "RP-1")

    def test_a_missing_file_is_named(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIn("not readable", dr.questions_block(Path(tmp))[0][0])
            self.assertIn("not readable", dr.portfolio_block(Path(tmp))[0][0])


class Advisor(unittest.TestCase):
    ASSIGNMENTS = "\n".join(json.dumps(r) for r in [
        {"id": "ADV-1", "state": "DRAFTED", "recipient": "Harness", "utc": "2026-11-20T10:00:00Z"},
        {"id": "ADV-2", "state": "DRAFTED", "recipient": "Harness", "utc": "2026-11-24T20:00:00Z"},
        {"id": "ADV-2", "state": "SENT", "to": ["HE"], "utc": "2026-11-24T21:00:00Z"},
        {"id": "ADV-3", "state": "DRAFTED", "recipient": "Science", "utc": "2026-11-24T21:30:00Z"}]) + "\n"
    NOW = datetime(2026, 11, 24, 22, 0, tzinfo=timezone.utc)

    @staticmethod
    def loader(root):
        return ({"state": "OK", "line": "scientific rotation: 1/3 in strand 'x'"},
                {"ADV-1": {"recipient": "Harness", "highest": "SENT"}, "ADV-2": {"recipient": "Harness", "highest": "SENT"},
                 "ADV-3": {"recipient": "Science", "highest": "DONE"}})

    def test_open_means_no_done_step_and_the_recent_ones_are_listed_apart(self):
        with tempfile.TemporaryDirectory() as tmp:
            rotation, actors, data = dr.advisor_block(tree(tmp, {dr.ASSIGNMENTS: self.ASSIGNMENTS}), self.loader, self.NOW)
        self.assertIn("1/3", rotation[0])
        harness = next(a for a in actors if a.startswith("Harness"))
        self.assertIn("2 without a DONE step, 1 touched in the last 48 h (ADV-2)", harness)
        self.assertIn("last assignment event 2026-11-24T21:00:00Z", harness)
        science = next(a for a in actors if a.startswith("Science"))
        self.assertIn("0 without a DONE step", science)
        self.assertEqual(data["actors"]["Harness"]["recent_48h"], ["ADV-2"])

    def test_no_roster_is_said_and_never_guessed(self):
        with tempfile.TemporaryDirectory() as tmp:
            _r, actors, _d = dr.advisor_block(tree(tmp, {dr.ASSIGNMENTS: self.ASSIGNMENTS}), self.loader, self.NOW)
        self.assertTrue(any("roster not readable" in a for a in actors))

    def test_a_failing_advisor_is_printed_not_a_crash(self):
        def broken(root):
            raise RuntimeError("REFUSED: a linked worktree")
        with tempfile.TemporaryDirectory() as tmp:
            rotation, actors, _d = dr.advisor_block(Path(tmp), broken, self.NOW)
        self.assertIn("not readable", rotation[0])
        self.assertIn("roster not readable", actors)


class NetworkBlocks(unittest.TestCase):
    def test_offline_skips_both_and_makes_no_call(self):
        called = []
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIn("skipped", dr.delta_block(Path(tmp), True, lambda: called.append(1))[0][0])
        self.assertIn("skipped", dr.ci_block(True, lambda: called.append(1))[0][0])
        self.assertEqual(called, [])

    def test_the_delta_line_carries_the_census_counts_and_names_its_tool(self):
        report = {"returned": 708, "new_count": 2, "new_pmids": ["43000001", "43000002"], "false_absent_count": 1, "seed_only_count": 0}
        with tempfile.TemporaryDirectory() as tmp:
            lines, data = dr.delta_block(Path(tmp), False, lambda: report)
        self.assertIn("708 records", lines[0])
        self.assertIn("2 true misses (43000001, 43000002)", lines[0])
        self.assertIn("pubmed_delta_census.py", lines[0])

    def test_a_failed_route_is_a_result(self):
        def broken():
            raise RuntimeError("E-utilities unreachable")
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIn("ROUTE FAILED", dr.delta_block(Path(tmp), False, broken)[0][0])
        self.assertIn("not readable", dr.ci_block(False, broken)[0][0])

    def test_the_ci_line_counts_open_runs_and_the_window(self):
        now = time.time()
        stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now - 600))
        runs = [{"run_number": 5, "name": "Public release gate", "status": "in_progress", "head_sha": "a" * 40, "head_branch": "main",
                 "event": "push", "created_at": stamp},
                {"run_number": 4, "name": "Public release gate", "status": "completed", "conclusion": "failure", "head_sha": "b" * 40,
                 "head_branch": "main", "event": "push", "created_at": stamp}]
        lines, data = dr.ci_block(False, lambda: runs)
        self.assertIn("1 open gate runs (1 in progress, 0 queued)", lines[0])
        self.assertIn("failure 1", lines[0])
        self.assertIn("ci_runs.py queue", lines[0])


class ThePage(unittest.TestCase):
    def test_every_section_prints_and_nothing_is_written(self):
        files = {dr.COVERAGE_MD: COVERAGE_MD, dr.OPEN_QUESTIONS: Tables.QUESTIONS, dr.PORTFOLIO: Tables.PORTFOLIO,
                 dr.ASSIGNMENTS: Advisor.ASSIGNMENTS}
        with tempfile.TemporaryDirectory() as tmp:
            root = tree(tmp, files)
            before = sorted(str(p) for p in root.rglob("*"))
            report = dr.build(root, offline=True, advisor=True,
                              parts={"events": [], "advisor": Advisor.loader})
            self.assertEqual(sorted(str(p) for p in root.rglob("*")), before)
        names = [s["name"] for s in report["sections"]]
        self.assertEqual(names, ["COVERAGE", "PUBMED DELTA", "OPEN QUESTIONS", "PORTFOLIO", "ROTATION", "ACTORS", "CI QUEUE"])
        text = dr.render(report)
        self.assertIn("## ACTORS", text)
        self.assertIn("skipped (--offline)", text)

    def test_no_advisor_skips_rotation_and_actors(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = dr.build(tree(tmp, {dr.COVERAGE_MD: COVERAGE_MD}), offline=True, advisor=False, parts={"events": []})
        by = {s["name"]: s["lines"] for s in report["sections"]}
        self.assertEqual(by["ROTATION"], ["skipped (--no-advisor)"])
        self.assertEqual(by["ACTORS"], ["skipped (--no-advisor)"])


class TheRealCheckout(unittest.TestCase):
    def test_the_command_runs_over_this_checkout_offline_without_the_advisor(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = dr.main(["--offline", "--no-advisor", "--json"])
        self.assertEqual(code, 0)
        report = json.loads(out.getvalue())
        coverage = report["sections"][0]["data"]
        self.assertGreater(coverage["table"].get("Full text depth", 0), 0)
        self.assertGreaterEqual(coverage["receipts"]["studies"], coverage["receipts"]["multi_receipt_studies"])
        # the registry's rule is the deepest receipt: the best-state complete count is never below the latest-receipt one
        self.assertGreaterEqual(coverage["receipts"]["best_depth"].get("complete", 0), coverage["receipts"]["latest_depth"].get("complete", 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
