#!/usr/bin/env python3
"""IT43 P2 regressions on the written listing table: a listing never acquires direction, a typed claim changes nothing, labelled forms and empty names are not molecules, the counts reproduce."""
import csv, re, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent

class Listing(unittest.TestCase):
    def rows(self):
        with open(HERE / "dgidb_rows_it43.tsv", encoding="utf-8") as f: return list(csv.DictReader(f, delimiter="\t"))
    def test_every_row_is_unknown_listing(self):
        for r in self.rows(): self.assertEqual((r["qualification"], r["reason"]), ("UNKNOWN", "listing_only"))
    def test_typed_claim_is_documented_action_only(self):
        typed = [r for r in self.rows() if r["interaction_type"]]
        self.assertTrue(typed); self.assertTrue(all(r["qualification"] == "UNKNOWN" for r in typed))
    def test_no_radiolabelled_or_empty_names(self):
        for r in self.rows(): self.assertFalse(re.match(r"^\[", r["name"]) or r["name"].lower() in ("null", "none", ""), r["name"])
    def test_summary_reproduces_from_rows(self):
        rows = self.rows()
        with open(HERE / "dgidb_summary_it43.tsv", encoding="utf-8") as f: summ = list(csv.DictReader(f, delimiter="\t"))
        for s in summ:
            rr = [r for r in rows if r["relation_id"] == s["relation_id"]]
            self.assertEqual(int(s["listing_molecules"]), len({r["catalogue_id"] for r in rr}))
            self.assertEqual(int(s["new_molecules"]), len({r["catalogue_id"] for r in rr if r["in_simple_search"] == "no"}))
            self.assertEqual((s["qualification_improved"], s["new_hypotheses"]), ("0", "0"))

if __name__ == "__main__": unittest.main(verbosity=2)
