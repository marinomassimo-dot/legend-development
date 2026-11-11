import csv, unittest
from pathlib import Path
import ladder as L

DR = L.DR
csv.field_size_limit(10**9)
R = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))


class Ladder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = L.build()

    def test_the_four_situations_each_have_rows_and_their_own_next_step(self):
        sit = {}
        for r in self.rows:
            sit.setdefault(r["situation"], set()).add(r["next_verification"])
        for s in ("A_engine_candidate", "B_reached_by_activity_only", "C_probe_or_reagent"):
            self.assertIn(s, sit)
        self.assertEqual({"read the primary documents (activity only)"}, sit["B_reached_by_activity_only"])
        self.assertEqual({"qualify as a tool: identity, selectivity, system"}, sit["C_probe_or_reagent"])
        # the fourth situation is a hypothesis, not a molecule: it lives in the conditional proposals with its decision measure
        cp = R(DR / "generation_it40_20261109/conditional_proposals_it40.tsv")
        self.assertTrue(any(r["nomination"] == "ABSTAIN" and r["decision_measure"] for r in cp))

    def test_no_activity_pointer_is_lost(self):
        have = {(r["relation_id"], r["molecule"].replace("CAT:", "")) for r in self.rows}
        for r in R(DR / "generation_it44_20261110/pointers_it44.tsv"):
            self.assertIn((r["relation_id"], r["parent_chembl_id"]), have, r["catalogue_name"])
        for d in ("s10_dose", "s2_dose"):
            for r in R(DR / "generation_it45_20261111" / d / "activity_molecules.tsv"):
                if r["catalogue_status"] != "none" and r["read_state"] == "OK":
                    self.assertIn((r["relation_id"], r["parent_chembl_id"]), have, r["name"])

    def test_the_six_things_stay_apart_and_nothing_is_empty(self):
        for r in self.rows:
            for k in ("reached_by", "identity", "action", "transfer_to_context", "possible_benefit", "next_verification"):
                self.assertTrue(r[k], (r["relation_id"], r["name"], k))
            self.assertTrue(r["possible_benefit"].startswith("IPOTESI"))

    def test_unqualified_entity_keeps_its_row_and_a_next_step(self):
        u = [r for r in self.rows if r["role"] == "unqualified_entity" and "CANDIDATE" in r["engine_verdicts"]]
        self.assertTrue(u)
        self.assertTrue(all(r["next_verification"] != "none unless the exclusion premise changes (see the engine columns)" for r in u))

    def test_the_hcn1_probe_pointer_is_a_probe_with_a_context_sentence(self):
        r = [x for x in self.rows if "CHEMBL6195028" in x["molecule"]]
        self.assertEqual(1, len(r))
        self.assertEqual("C_probe_or_reagent", r[0]["situation"])
        self.assertIn("HCN1", r[0]["transfer_to_context"])

    def test_an_excluded_row_is_kept_and_says_what_would_reopen_it(self):
        e = [r for r in self.rows if r["situation"] == "E_excluded_and_kept"]
        self.assertTrue(e)
        self.assertTrue(all("exclusion premise" in r["next_verification"] for r in e))


if __name__ == "__main__":
    unittest.main()
