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


class DoiCheck(unittest.TestCase):
    @staticmethod
    def fake(doi):
        return lambda url: json.dumps({"result": {"1": {"articleids": [{"idtype": "pubmed", "value": "1"}, {"idtype": "doi", "value": doi}]}}})

    def test_matching_doi_passes(self):
        r = {"study_id": {"pmid": "1", "doi": "10.1/Abc"}}
        self.assertEqual(m.doi_errors(r, self.fake("10.1/abc")), [])

    def test_last_digit_wrong_is_refused(self):
        r = {"study_id": {"pmid": "1", "doi": "10.1007/s10142-025-01601-0"}}
        errs = m.doi_errors(r, self.fake("10.1007/s10142-025-01601-5"))
        self.assertTrue(errs and "differs" in errs[0])

    def test_unreadable_pubmed_is_not_silence(self):
        r = {"study_id": {"pmid": "1", "doi": "10.1/x"}}
        self.assertTrue(m.doi_errors(r, lambda url: "not json")[0].startswith("doi check: PubMed DOI"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
