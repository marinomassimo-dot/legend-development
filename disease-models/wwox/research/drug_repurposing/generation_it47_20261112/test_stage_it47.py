"""IT47 P1: the generator consumes the hypotheses_only packages through hypotheses_for, with an explicit cell mapping; no direction is invented; the dashboard rows carry no compound name."""
import csv, re, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = HERE.parent
sys.path.insert(0, str(DR / "generation_it40_20261109")); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import conditional_proposals as cp  # noqa: E402
csv.field_size_limit(10**9)


class PackageRows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.unmapped = cp.package_rows()

    def test_sixteen_rows_from_three_packages_of_different_structure(self):
        ids = sorted(r["proposal_id"] for r in self.rows)
        self.assertEqual(16, len([i for i in ids if "potassium_conductances_sci43" not in i and "hcn_20261107" not in i and "isr_inv02_it50" not in i and "inhibitory_defect_sci47" not in i]))   # IT49: the two later packages are counted in test_stage_it49; HE53: the six SCI47 levers (INV-05) in test_design_rows_he50
        self.assertEqual({"INV-18", "INV-08", "INV-09", "INV-02", "INV-05"}, {r["inv_id"] for r in self.rows})   # IT50 added INV-02; HE53 added INV-05 (the SCI47 levers)
        self.assertEqual(5, sum(1 for r in self.rows if "gsk3_eif2b" in r["proposal_id"]))
        self.assertEqual(5, sum(1 for r in self.rows if "ph_k2p" in r["proposal_id"]))
        self.assertEqual(6, sum(1 for r in self.rows if "nrf2_inv08" in r["proposal_id"]))

    def test_packages_reachable_but_not_mapped_are_reported_not_hidden(self):
        self.assertEqual({}, self.unmapped)   # IT49 mapped the last eight; the report mechanism stays (a new unmapped package would appear here)

    def test_every_slot_is_filled_or_says_it_is_not_stated(self):
        for r in self.rows:
            for f in ("starting_observation_and_chain", "context", "competing_explanations", "premise_and_action", "decision_measure", "package_ref"):
                self.assertTrue(r[f].strip(), (r["proposal_id"], f))
            self.assertTrue(r["direction_stated"].startswith("none"))
            self.assertTrue("CONDITIONAL" in r["nomination"] or r["nomination"].startswith(("NOT PROPOSED: the package drops this row", "the package's own status: ")))   # HE53: a row the package drops is labelled so; HE54: SCI47's levers follow their own status
            self.assertNotRegex(" ".join(r.values()), r"HGNC:\d|gene_arc\s*=\s*True")

    def test_a_missing_action_is_taken_from_a_named_relation_and_labelled(self):
        h = [r for r in self.rows if r["proposal_id"].endswith("nrf2_inv08_20261107::H1")][0]
        self.assertIn("not stated by the package; taken from relation S10", h["premise_and_action"])

    def test_other_rows_are_listed_without_calling_them_rivals(self):
        h5 = [r for r in self.rows if r["proposal_id"].endswith("nrf2_inv08_20261107::H5")][0]
        for k in ("H1", "H2", "H3", "H4", "H6"):
            self.assertIn(k + ":", h5["competing_explanations"])
        self.assertIn("does not classify them as rivals, complementary or compatible", h5["competing_explanations"])

    def test_nrf2_observation_support_and_prediction_are_kept_apart(self):
        """IT47 integration: what_supports is recorded support (with audit remarks), not an observation and not a prediction; a missing prediction is declared missing"""
        for r in [x for x in self.rows if "nrf2_inv08" in x["proposal_id"]]:
            self.assertTrue(r["starting_observation_and_chain"].startswith("not stated by the package as an observation"), r["proposal_id"])
            self.assertTrue(r["recorded_support"].startswith("what_supports:"), r["proposal_id"])
            self.assertTrue(r["expected_result_by_explanation"].startswith("not stated by the package (missing)"), r["proposal_id"])

    def test_gsk3_package_prerequisite_is_a_premise_and_the_refuting_outcomes_are_the_measure(self):
        """reader R0 (IT47 P4): requires_first names a prerequisite, refuted_or_replaced_by the discriminating outcomes"""
        for r in [x for x in self.rows if "gsk3_eif2b" in x["proposal_id"]]:
            self.assertIn("requires_first:", r["premise_and_action"])
            self.assertTrue(r["decision_measure"].startswith("refuted_or_replaced_by:"), r["proposal_id"])
            self.assertIn("none", r["direction_stated"])

    def test_cell_context_changes_the_k2p_proposal(self):
        kp1 = [r for r in self.rows if r["proposal_id"].endswith("ph_k2p_sci45_20261111::KP1")][0]
        self.assertIn("KCNK2", kp1["cell_context"])
        self.assertIn("cell-specific control", kp1["cell_context"])


class DashboardRows(unittest.TestCase):
    def test_reader_rows_exist_with_their_source_and_no_compound_name(self):
        rows = {r["hyp_id"]: r for r in csv.DictReader(open(DR / "generation_it40_20261109/reader_view.tsv", encoding="utf-8"), delimiter="\t")}
        for k, inv in (("KP1", "INV-18"), ("NRF2-H1", "INV-08"), ("NRF2-H2", "INV-08"), ("GSK3-H1", "INV-09")):
            self.assertEqual(inv, rows[k]["inv_id"])
            self.assertIn("hypotheses.tsv:", rows[k]["source_rows"])
            self.assertNotRegex(" ".join(rows[k].values()), r"ML365|PK-THPP|ONO-TR|fumarate|bardoxolone|KI-696|sulforaphane|LY-2090314|laduviglusib|TDZD-8|SB-216763|SB-415286")


if __name__ == "__main__":
    unittest.main(verbosity=2)
