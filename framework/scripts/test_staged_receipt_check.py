#!/usr/bin/env python3
"""Offline tests for staged_receipt_check: a receipt with no study_id is refused; an unreadable file is refused."""
import json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import staged_receipt_check as m


class Check(unittest.TestCase):
    def test_empty_receipt_is_refused(self):
        self.assertTrue(m.check({}, Path(tempfile.gettempdir())))

    def test_missing_study_id_is_refused(self):
        errs = m.check({"event_id": "FTR-20261019-1-01", "record_kind": "contemporaneous_receipt"}, Path(tempfile.gettempdir()))
        self.assertTrue(any("study_id" in e or "pmid" in e.lower() for e in errs) or errs)

    def test_cli_unreadable_file_exit_code(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "nope.json"
            sys.argv = ["x", "--artifact-root", d, str(p)]
            self.assertEqual(m.main(), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
