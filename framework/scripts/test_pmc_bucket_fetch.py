#!/usr/bin/env python3
"""Offline tests for pmc_bucket_fetch: a restricted stub is never reported as full text; keys are classified; no overwrite."""
import json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pmc_bucket_fetch as m

STUB = '<?xml version="1.0"?><article><!--The publisher of this article does not allow downloading of the full text in XML form.--><front/></article>'
FULL = "<article><front/><body><p>" + "x" * 21000 + '</p><graphic xlink:href="f1.jpg"/></body></article>'


def make_get(xml):
    def get(url, out=None):
        if "esummary" in url:
            return "200", json.dumps({"result": {"1": {"articleids": [{"idtype": "pmc", "value": "PMC9"}, {"idtype": "doi", "value": "10.1/x"}]}}})
        if "efetch" in url:
            return "200", xml
        if "list-type" in url:
            return "200", "<Key>PMC9.1/f1.jpg</Key><Key>PMC9.1/PMC9.1.xml</Key><Key>PMC9.1/PMC9.1.pdf</Key><Key>PMC9.1/s1.pdf</Key><Key>PMC9.1/PMC9.1.json</Key>"
        return "200", "bytes"
    return get


class Fetch(unittest.TestCase):
    def test_stub_is_classified_restricted(self):
        self.assertEqual(m.classify_xml(STUB), "restricted_stub")
        self.assertEqual(m.classify_xml(FULL), "full")

    def test_key_classification(self):
        self.assertEqual(m.wanted("PMC9.1/f1.jpg", "PMC9"), "figure")
        self.assertEqual(m.wanted("PMC9.1/PMC9.1.pdf", "PMC9"), "article_pdf")
        self.assertEqual(m.wanted("PMC9.1/s1.pdf", "PMC9"), "supplement")
        self.assertIsNone(m.wanted("PMC9.1/PMC9.1.json", "PMC9"))

    def test_full_run_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            r = m.fetch("1", "A2024", Path(d), get=make_get(FULL))
            self.assertEqual(r["xml_state"], "full")
            self.assertEqual({f["kind"] for f in r["files"]}, {"article_text", "figure", "article_pdf", "supplement"})
            self.assertTrue(all(len(f["sha256"]) == 64 for f in r["files"]))
            self.assertIn("error", m.fetch("1", "A2024", Path(d), get=make_get(FULL)))

    def test_stub_run_reports_state(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(m.fetch("1", "A2024", Path(d), get=make_get(STUB))["xml_state"], "restricted_stub")


if __name__ == "__main__":
    unittest.main(verbosity=2)
