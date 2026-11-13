"""IT50: the INV-02 ISR hypotheses are read by the generator; the rows state no direction and no prediction; the other rows are untouched in order."""
import csv, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(DR / "generation_it40_20261109")); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import conditional_proposals as cp  # noqa: E402
csv.field_size_limit(10 ** 9)


class IsrRows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.unmapped = cp.package_rows()
        cls.isr = {r["proposal_id"].split("::")[-1]: r for r in cls.rows if "isr_inv02_it50" in r["proposal_id"]}

    def test_three_rows_nothing_unmapped_and_earlier_order_kept(self):
        self.assertEqual({"ISR1", "ISR2", "ISR3"}, set(self.isr))
        self.assertEqual({}, self.unmapped)
        invs = [r["inv_id"] for r in self.rows]
        self.assertEqual(["INV-18"] * 13 + ["INV-08"] * 6 + ["INV-09"] * 5 + ["INV-02"] * 3, invs)   # the earlier order is unchanged; the new investigation is appended

    def test_no_direction_no_prediction_no_favourable_compound(self):
        for r in self.isr.values():
            self.assertTrue(r["direction_stated"].startswith("none"))
        self.assertIn("not stated by the package", self.isr["ISR3"]["reopen_or_abandon"])
        self.assertIn("(missing)", self.isr["ISR2"]["expected_result_by_explanation"])
        self.assertIn("not a candidate", self.isr["ISR1"]["compound_or_probe_named_by_package"])

    def test_the_isr_sign_is_an_unresolved_premise_and_the_join_is_unknown(self):
        for r in self.isr.values():
            self.assertRegex(r["premise_and_action"], r"(?i)protein.level|sign")
            self.assertIn("PPP1R15B", r["cell_context"])          # the twelfth symbol of IT49-Q02 is joined
            self.assertIn("cannot be assigned to neurons", r["cell_context"])   # no ISR gene is neuron-enriched in either held table (HE50 values)
        self.assertNotRegex(" ".join(r["cell_context"] for r in self.isr.values()), r"neuron-enriched in every")

    def test_kinase_panel_rows_of_the_target_search_are_not_carried_as_hits(self):
        t = self.isr["ISR2"]["compound_or_probe_named_by_package"]
        self.assertIn("none is carried here as a hit", t)
        self.assertNotRegex(t, r"RIPK1|Cdk2|GSK2606414|GSK2656157")


if __name__ == "__main__":
    unittest.main(verbosity=2)
