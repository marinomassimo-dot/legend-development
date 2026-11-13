"""IT49: the eight remaining hypotheses (SCI43 KH1-KH5, HCN HY1-HY3) are read by the generator, cell by cell, without inventing a direction or an expectation."""
import csv, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(DR / "generation_it40_20261109")); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import conditional_proposals as cp  # noqa: E402
csv.field_size_limit(10 ** 9)


class RemainingHypotheses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.unmapped = cp.package_rows()
        cls.by = {r["proposal_id"].split("::")[-1]: r for r in cls.rows if r["proposal_id"].startswith(("CP-potassium_conductances_sci43", "CP-hcn_20261107"))}

    def test_eight_rows_and_nothing_left_unmapped(self):
        self.assertEqual({"KH1", "KH2", "KH3", "KH4", "KH5", "HY1", "HY2", "HY3"}, set(self.by))
        self.assertEqual({}, self.unmapped)
        self.assertEqual(24, len(self.rows))

    def test_no_direction_is_invented_and_hcn_rows_state_no_expectation(self):
        for r in self.by.values():
            self.assertTrue(r["direction_stated"].startswith("none"))
        for k in ("HY1", "HY2", "HY3"):
            self.assertIn("not stated by the package (missing)", self.by[k]["expected_result_by_explanation"])

    def test_what_would_favour_a_row_is_a_measure_not_an_expected_result(self):
        kh1 = self.by["KH1"]
        self.assertIn("favourable_context", kh1["decision_measure"])
        self.assertNotIn("favourable_context", kh1["expected_result_by_explanation"])
        self.assertIn("opposite_context", kh1["reopen_or_abandon"])
        self.assertIn("weakening_result", self.by["HY2"]["reopen_or_abandon"])

    def test_kh1_carries_the_sci43_corrections(self):
        prem = self.by["KH1"]["premise_and_action"]
        for needle in ("does not identify Kir2", "not additive", "pertinent age band", "neither supported nor refuted"):
            self.assertIn(needle, prem)

    def test_context_is_joined_per_row_and_unknown_is_not_low(self):
        self.assertIn("KCNQ2", self.by["KH2"]["cell_context"])
        self.assertIn("HCN1", self.by["HY2"]["cell_context"])
        self.assertNotIn("KCNQ2", self.by["HY2"]["cell_context"])
        self.assertTrue(self.by["KH4"]["cell_context"].startswith("not joined"))

    def test_the_earlier_sixteen_rows_say_the_reopen_cell_is_not_stated(self):
        for r in self.rows:
            if "nrf2_inv08" in r["proposal_id"] or "gsk3_eif2b" in r["proposal_id"] or "ph_k2p" in r["proposal_id"]:
                self.assertEqual("not stated by the package", r["reopen_or_abandon"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
