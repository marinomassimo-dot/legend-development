#!/usr/bin/env python3
"""HE43 H5: a compound name reaches the shareable view only from a class-A name source, joined by identifier. Synthetic data; no network."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_view as rv  # noqa: E402

CV = ["order", "item_id", "inv_id", "kind", "name_full", "label", "action", "rationale", "open_premise", "counter", "next_test", "source_rows", "registry_note", "moves", "where_done", "relation_id"]


def tsv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def make(dr, join, table, wd):
    tsv(dr / rv.COMPOUND_FILE, CV, [[i + 1, f"V0{i + 1}", "INV-X", "probe", "full name", "own label", "a", "r", "o", "c", "n", "s", "reg", "m", "in_silico", "S1"] for i in range(len(join))])
    tsv(dr / rv.IDENTITY_JOIN_FILE, ["item_id", "name", "identity_state", "label_conflict", "expected_gene", "evidence_level", "selectivity", "link"],
        [[f"V0{i + 1}", n, "NAME_EXACT", "no", "G", "L", "NOT_ASSESSED", link] for i, (n, link) in enumerate(join)])
    tsv(dr / rv.IDENTITY_TABLE_FILE, ["query_name", "record_chembl_refs", "declared_chembl_id"], table)
    tsv(dr / rv.NAME_WD_FILE, ["chembl_id", "state", "qid", "label", "retrieved_utc", "source", "licence_url"], wd)


class PublicNames(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dr = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def names(self, full=False):
        return {c["item_id"]: c for c in rv.compound_view(self.dr, full)}

    def test_an_exact_link_with_one_chembl_id_and_a_label_gets_the_name_with_its_item(self):
        make(self.dr, [("ifenprodil", "EXACT")], [["ifenprodil", "CHEMBL1", "CHEMBL1"]], [["CHEMBL1", "LABEL", "Q10", "ifenprodil", "2026-11-10T12:00Z", "s", "u"]])
        c = self.names()["V01"]
        self.assertEqual(c["names_public"], [{"label": "ifenprodil", "qid": "Q10", "chembl_id": "CHEMBL1"}])
        self.assertNotIn("name_full", c)                       # the shareable edition never carries the catalogue-derived name
        self.assertNotIn("names_public", self.names(full=True)["V01"])

    def test_no_name_without_an_exact_link_a_single_id_and_a_label(self):
        make(self.dr, [("(S)-X", "QUALIFIED"), ("frag", "PROPOSED_ONLY"), ("two", "EXACT"), ("nolabel", "EXACT"), ("noid", "EXACT")],
             [["(s)-x", "CHEMBL1", ""], ["two", "CHEMBL2;CHEMBL3", ""], ["nolabel", "CHEMBL4", ""], ["noid", "", ""]],
             [["CHEMBL1", "LABEL", "Q1", "x", "t", "s", "u"], ["CHEMBL2", "LABEL", "Q2", "two", "t", "s", "u"], ["CHEMBL3", "LABEL", "Q3", "three", "t", "s", "u"],
              ["CHEMBL4", "NO_WIKIDATA_ITEM", "", "", "t", "s", "u"]])
        got = self.names()
        self.assertTrue(all(c["names_public"] == [] for c in got.values()), {k: c["names_public"] for k, c in got.items()})

    def test_a_label_that_is_not_the_tables_bare_name_is_not_shown(self):
        make(self.dr, [("GYKI 52466", "EXACT"), ("EVT-101", "EXACT"), ("rislenemdaz", "EXACT")],
             [["gyki 52466", "CHEMBL1", ""], ["evt-101", "CHEMBL2", ""], ["rislenemdaz", "CHEMBL3", ""]],
             [["CHEMBL1", "LABEL", "Q1", "GYKI-2466", "t", "s", "u"], ["CHEMBL2", "LABEL", "Q2", "EVT-101 dihydrochloride", "t", "s", "u"], ["CHEMBL3", "LABEL", "Q3", "CERC-301", "t", "s", "u"]])
        got = self.names()
        self.assertEqual([got[k]["names_public"] for k in ("V01", "V02", "V03")], [[], [], []])     # a misspelling, a salt form and a code name: withheld

    def test_absent_name_file_means_no_names_and_no_error(self):
        make(self.dr, [("ifenprodil", "EXACT")], [["ifenprodil", "CHEMBL1", ""]], [])
        (self.dr / rv.NAME_WD_FILE).unlink()
        self.assertEqual(self.names()["V01"]["names_public"], [])

    def test_the_credit_reaches_the_footer_only_when_a_name_is_shown(self):
        from collections import Counter
        allow = {"name_sources": {rv.WD_SOURCE_KEY: {"label": "Wikidata item labels (English)", "licence": "CC0", "attribution": "credit", "url": "u"}}}
        cur = {}
        rv.credit_name_source(cur, [{"names_public": []}], allow)
        self.assertNotIn("wd_name_rows", cur)
        cv = [{"names_public": [{"label": "a", "qid": "Q1", "chembl_id": "C"}]}, {"names_public": [{"label": "b", "qid": "Q2", "chembl_id": "D"}]}]
        rv.credit_name_source(cur, cv, allow)
        self.assertEqual(cur["wd_name_rows"], 2)
        ft = rv.build_footer("shareable", allow, Counter({"name:" + rv.WD_SOURCE_KEY: 2}), [])
        self.assertIn(("Wikidata item labels (English)", 2), [(e["label"], e["rows"]) for e in ft["embedded"]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
