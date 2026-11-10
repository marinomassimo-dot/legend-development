#!/usr/bin/env python3
"""Canned-answer tests for name_source_wikidata.py (no network)."""
import datetime
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import name_source_wikidata as ns  # noqa: E402

NOW = datetime.datetime(2026, 11, 10, 12, 0, tzinfo=datetime.timezone.utc)


def fake(items, labels=None):
    """items: {chembl id: [qids]}; labels: {qid: label}. Answers the two kinds of request the module sends."""
    labels = labels or {}

    def get(url):
        if "list=search" in url:
            cid = url.split("P592%3D")[1].split("&")[0]
            return {"query": {"search": [{"title": q} for q in items.get(cid, [])]}}
        ids = url.split("ids=")[1].split("&")[0].split("%7C")
        return {"entities": {q: ({"labels": {"en": {"value": labels[q]}}} if q in labels else {"labels": {}}) for q in ids}}
    return get


class Rows(unittest.TestCase):
    def test_label_and_missing_item_are_two_states(self):
        rows = ns.fetch(["CHEMBL1", "CHEMBL2"], fake({"CHEMBL1": ["Q10"]}, {"Q10": "ifenprodil"}), NOW)
        self.assertEqual([(r["chembl_id"], r["state"], r["qid"], r["label"]) for r in rows], [("CHEMBL1", "LABEL", "Q10", "ifenprodil"), ("CHEMBL2", "NO_WIKIDATA_ITEM", "", "")])
        self.assertEqual(rows[0]["retrieved_utc"], "2026-11-10T12:00Z")

    def test_a_label_that_is_a_code_name_is_kept_as_stated(self):
        (r,) = ns.fetch(["CHEMBL9"], fake({"CHEMBL9": ["Q7"]}, {"Q7": "CERC-301"}), NOW)
        self.assertEqual(r["label"], "CERC-301")

    def test_ambiguity_and_a_missing_label_refuse_to_choose(self):
        with self.assertRaises(ValueError):
            ns.fetch(["CHEMBL1"], fake({"CHEMBL1": ["Q1", "Q2"]}, {"Q1": "a", "Q2": "b"}), NOW)
        with self.assertRaises(ValueError):
            ns.fetch(["CHEMBL1"], fake({"CHEMBL1": ["Q1"]}, {}), NOW)
        with self.assertRaises(ValueError):
            ns.fetch(["CHEMBL1"], lambda url: {"error": "x"}, NOW)

    def test_ids_must_be_chembl_ids_and_the_query_joins_by_identifier(self):
        with self.assertRaises(ValueError):
            ns.fetch(["ifenprodil"], fake({}), NOW)
        self.assertIn("P592", ns.search_url("CHEMBL1"))       # the join is the identifier statement, never a name search

    def test_nothing_is_written_on_a_failed_fetch_and_a_roundtrip_reads_back(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "out.tsv"
            def boom(url):
                raise OSError("HTTP 500")
            old = ns.http_fetch
            ns.http_fetch = boom
            try:
                self.assertEqual(ns.main(["CHEMBL1", "--out", str(p)]), 3)
            finally:
                ns.http_fetch = old
            self.assertFalse(p.exists())
            ns.write(ns.fetch(["CHEMBL1"], fake({"CHEMBL1": ["Q10"]}, {"Q10": "x"}), NOW), p)
            self.assertEqual(ns.read(p)[0]["qid"], "Q10")


if __name__ == "__main__":
    unittest.main()
