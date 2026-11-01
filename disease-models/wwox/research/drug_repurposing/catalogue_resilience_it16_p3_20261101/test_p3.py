#!/usr/bin/env python3
"""Regression for the IT16 P3 package: the scripts answer --help without touching the network or writing a file, the recovered assay-context
table has one width, and the stated reconciliation change (6 of 34 values, none to ASSESSED_ELSEWHERE) matches the shipped table."""
import csv, os, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))


class P3(unittest.TestCase):
    def test_help_is_safe(self):
        for s in ("p3_measure.py", "q5_reconcile_docs.py"):
            with tempfile.TemporaryDirectory() as d:
                r = subprocess.run([sys.executable, os.path.join(HERE, s), "--help"], capture_output=True, text=True, cwd=d)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertEqual(os.listdir(d), [])

    def test_recovered_context_table_is_rectangular_and_nonempty(self):
        rows = list(csv.reader(open(os.path.join(HERE, "assay_context_recovered.tsv"), encoding="utf-8"), delimiter="\t"))
        self.assertGreater(len(rows), 100)
        self.assertEqual({len(r) for r in rows}, {11})

    def test_reconciliation_change_is_what_the_readme_states(self):
        rows = list(csv.DictReader(open(os.path.join(HERE, "queue_reconciliation_reports_searched.tsv"), encoding="utf-8"), delimiter="\t"))
        self.assertEqual(len(rows), 34)
        ch = [r for r in rows if r["change"] == "CHANGES"]
        self.assertEqual(len(ch), 6)
        self.assertTrue(all(r["reconciliation_now"] == "NO_CARD_OR_RECORD_FOUND" and r["reconciliation_if_reports_searched"] == "MENTIONED_ONLY" for r in ch))
        self.assertFalse(any(r["reconciliation_if_reports_searched"] == "ASSESSED_ELSEWHERE" and r["reconciliation_now"] != "ASSESSED_ELSEWHERE" for r in rows))


if __name__ == "__main__":
    unittest.main()
