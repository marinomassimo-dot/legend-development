#!/usr/bin/env python3
"""HE44 H2: the quantity survives to the IT41 search table, and the internal check is not read as agreement with the source."""
import csv
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
sys.path.insert(0, str(DR / "generation_it41_20261109"))
import action_search as A  # noqa: E402


def rows():
    with open(DR / "generation_it41_20261109/search_rows.tsv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


class QuantityKept(unittest.TestCase):
    def test_the_old_column_is_unchanged_and_the_original_quantity_sits_beside_it(self):
        r = next(x for x in rows() if x["name"] == "DQP-1105" and x["target_symbol"] == "Grin2b")
        self.assertTrue(r["affinity"].startswith("6.9") and r["affinity"].endswith("pIC50 (=)"))   # as before
        self.assertEqual((r["affinity_type"], r["affinity_nM_column"]), ("IC50", "= 113.0 nM"))

    def test_the_cs_hcn_rows_are_flagged_and_the_flag_names_no_column_as_wrong(self):
        flagged = {(x["name"], x["target_symbol"]) for x in rows() if x["affinity_check"] == "UNIT_CONFLICT_SUSPECT"}
        self.assertEqual(flagged, {("Cs<sup>+</sup>", "HCN1"), ("Cs<sup>+</sup>", "HCN2"), ("Cs<sup>+</sup>", "HCN4")})

    def test_an_internally_consistent_row_can_still_be_wrong_against_the_source(self):
        """DQP-1105: the registry's log value and nanomolar column agree with each other (AGREE) although two rows differ from the primary table by 1000: the internal check must not be quoted as agreement with the source."""
        for x in rows():
            if x["name"] == "DQP-1105" and x["target_symbol"] in ("Grin2b", "Grin2c"):
                self.assertEqual(x["affinity_check"], "AGREE")

    def test_a_registry_range_is_written_smallest_to_largest_with_its_unit(self):
        """The registry's low and high are low and high affinity, so the nM 'low' is the larger number (a real row read [300000.0-130000.0]): the column writes the range ascending and labelled."""
        rng = [x["affinity_nM_column"] for x in rows() if "range" in x["affinity_nM_column"]]
        self.assertTrue(rng)
        import re
        for c in rng:
            a, b = map(float, re.search(r"range ([\d.]+)-([\d.]+) nM", c).groups())
            self.assertLessEqual(a, b, c)
        g = {"Original Affinity Units": "IC50", "Original Affinity Median nm": "180000.0", "Original Affinity Low nm": "300000.0", "Original Affinity High nm": "130000.0", "Original Affinity Relation": "=",
             "Affinity Median": "3.7", "Affinity Units": "pIC50", "Affinity Low": "3.5", "Affinity High": "3.9", "Target": "t", "Target Species": "Human"}
        self.assertIn("(range 130000-300000 nM)", A.affinity_columns(g)["affinity_nM_column"])

    def test_potency_and_its_log_transform_use_the_one_conversion(self):
        self.assertTrue(A.same_datum(8.08, 8.3176))
        self.assertFalse(A.same_datum(8.08, 22.9))


if __name__ == "__main__":
    unittest.main(verbosity=2)
