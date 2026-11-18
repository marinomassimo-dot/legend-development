#!/usr/bin/env python3
"""Offline tests for epmc_notice_sweep.py: partial-date comparison and the receipt index (no network)."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import epmc_notice_sweep as m  # noqa: E402


class DateTests(unittest.TestCase):
    def test_post_pre_between(self):
        self.assertEqual(m.compare("2026-11-20", "2026-07-26", "2026-08-06"), "POST")
        self.assertEqual(m.compare("2026-07-17", "2026-07-26", "2026-08-06"), "PRE")
        self.assertEqual(m.compare("2026-08-01", "2026-07-26", "2026-08-06"), "BETWEEN")

    def test_partial_dates_compare_at_their_own_precision(self):
        self.assertEqual(m.compare("2012 May", "2026-11-07", "2026-11-07"), "PRE")
        self.assertEqual(m.compare("2026 Nov", "2026-11-04", "2026-11-04"), "SAME_DAY_OR_PERIOD")

    def test_unreadable_date_is_unknown_never_pre(self):
        self.assertEqual(m.compare("", "2026-11-07", "2026-11-07"), "UNKNOWN")
        self.assertEqual(m.compare("Oncogene.", "2026-11-07", "2026-11-07"), "UNKNOWN")


class ReferenceTests(unittest.TestCase):
    def test_citation_only_notice_gets_its_date(self):
        self.assertEqual(m.reference_date("Oncogene. 2006 Dec 7;25(58):7662"), "2006 Dec 7")
        self.assertEqual(m.reference_date("Nature.2014 Jul 17;511(7509):370"), "2014 Jul 17")
        self.assertEqual(m.reference_date("PLoS One. 2013;8(8). doi:10.1371/annotation/x"), "2013")
        self.assertEqual(m.compare(m.reference_date("Ann Oncol. 2015 Feb;26(2):445"), "2026-11-04", "2026-11-04"), "PRE")
        self.assertEqual(m.reference_date("no date here"), "")


class IndexTests(unittest.TestCase):
    def test_receipt_index_groups_by_pmid_and_skips_rows_without_one(self):
        rows = [{"event_at": "2026-08-06T11:30:00Z", "event_id": "A", "evidence_depth": "abstract_only", "study_id": {"pmid": "1"}},
                {"event_at": "2026-07-26T07:52:50+02:00", "event_id": "B", "evidence_depth": "partial_fulltext_read", "study_id": {"pmid": "1"}},
                {"event_at": "2026-07-26T07:52:50+02:00", "event_id": "C", "evidence_depth": "abstract_only", "study_id": {"doi": "10.1/x"}}]
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "l.jsonl"
            p.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
            idx = m.receipt_index(p)
        self.assertEqual(sorted(idx), ["1"])
        self.assertEqual(len(idx["1"]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
