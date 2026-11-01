#!/usr/bin/env python3
"""Tests for controls.py (synthetic inputs only; no cache, no network). Run: python3 test_controls.py"""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import controls as c  # noqa: E402


class Controls(unittest.TestCase):
    def test_help_is_safe(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(c.main([]), 0)
        self.assertIn("usage", buf.getvalue())

    def test_percentile_mid_rank(self):
        p = c.percentile_map({"a": 1, "b": 3}, [1, 2, 3, 4])
        self.assertEqual(p["a"], 12.5)
        self.assertEqual(p["b"], 62.5)

    def test_auc_ties_and_empty(self):
        self.assertEqual(c.mw_auc([2, 2], [1, 2]), 0.75)
        self.assertIsNone(c.mw_auc([], [1]))

    def test_popularity_path_takes_k_per_need_with_hash_ties(self):
        rows = [("N1", "A"), ("N1", "B"), ("N1", "C"), ("N2", "A")]
        sel = c.popularity_path(rows, {"A": 5, "B": 9, "C": 5}, {"N1": 2, "N2": 0})
        self.assertIn(("N1", "B"), sel)
        self.assertEqual(len(sel), 2)
        self.assertNotIn(("N2", "A"), sel)
        tie = min(["A", "C"], key=c.sha256_text)
        self.assertIn(("N1", tie), sel)

    def test_leak_is_whole_word_and_min_length(self):
        terms = c.name_terms(["ETHOSUXIMIDE", "ETX", "Lith"])
        self.assertEqual(terms, ["ethosuximide", "lith"])
        self.assertEqual(c.leaked(terms, '{"label": "Ethosuximide sensitivity"}'), ["ethosuximide"])
        self.assertEqual(c.leaked(["lith"], "lithium chloride"), [])

    def test_dgidb_join_by_chembl_and_name_counts_distinct_genes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "i.tsv"
            p.write_text("gene_name\tdrug_concept_id\tdrug_name\n"
                         "G1\tchembl:CHEMBL9\tX\nG2\trxcui:1\tFOO\nG1\trxcui:1\tfoo\nNULL\trxcui:1\tFOO\nG3\trxcui:2\tBAR\n", encoding="utf-8")
            pop = c.dgidb_pop(p, {"CHEMBL1": {"CHEMBL1", "CHEMBL9"}}, {"CHEMBL1": {"Foo"}})
        self.assertEqual(pop, {"CHEMBL1": 2})

    def _inputs(self, leak_determinate):
        rows = [("N", "A", "dev"), ("N", "B", "eval"), ("N", "C", "eval")]
        labels = {("N", "A"): "compatible", ("N", "B"): "compatible", ("N", "C"): "indeterminable"}
        truth = {("N", "A"): "compatible", ("N", "B"): "unknown_no_counterpart", ("N", "C"): "unknown_no_counterpart"}
        names = {"A": {"alphazine"}, "B": {"betamab"}, "C": {"gammol"}}
        text = {"N": "built on %s" % ("alphazine" if leak_determinate else "betamab")}
        return rows, labels, truth, {"A": 1, "B": 5, "C": 9}, {"A": {"N03AX"}}, names, text, [1, 5, 9, 20]

    def test_leaked_determinate_row_is_flagged_and_removed(self):
        r = c.analyse(*self._inputs(True))
        c2 = r["C2_leakage_and_indication_shortcut"]
        self.assertEqual(c2["leaked_determinate"], 1)
        self.assertIn("circular", c2["decision"])
        self.assertEqual(c2["L_precision_without_leaked"]["determinate"], 0)
        self.assertEqual(c2["N03_rows_L_compatible_per_need"], {"N": 1})

    def test_leak_without_reference_is_construction_fact(self):
        r = c.analyse(*self._inputs(False))
        self.assertIn("construction fact", r["C2_leakage_and_indication_shortcut"]["decision"])

    def test_small_denominator_never_claims_reference_bias(self):
        r = c.analyse(*self._inputs(False))["C1_popularity"]
        self.assertIn("no popularity bias", r["decision_reference_bias"])
        self.assertIn("cannot be discriminated", r["decision_discrimination"])
        self.assertEqual(r["P_popularity_path"]["per_need"]["N"]["k_L_compatible"], 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
