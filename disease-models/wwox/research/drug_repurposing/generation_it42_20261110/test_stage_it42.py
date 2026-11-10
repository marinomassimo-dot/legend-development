"""IT42 P4: the smallest regressions that intercept the errors found in the IT41 consumers (not copies of the implementation)."""
import csv, re, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(DR / "generation_it41_20261109"))
import action_search as A  # noqa: E402
def tsv(p):
    with open(p, encoding="utf-8") as f: return list(csv.DictReader(f, delimiter="\t"))

class Propagation(unittest.TestCase):
    def test_no_consumer_assumes_a_shared_triheteromer_ceiling(self):
        cells = []
        for f in ("investigations_it20.tsv", "investigations.tsv"):
            cells += [r["next_test"] for r in tsv(DR / "ranking_it8_p9_20261029" / f) if r["inv_id"] == "INV-05"]
        for r in tsv(DR / "comparators_it39_20261109/output/comparators.tsv"):
            if r["inv_id"] == "INV-05": cells += [r["what_it_separates"], r["what_it_does_not_separate"], r["selectivity_limits"]]
        for c in cells: self.assertNotRegex(c, r"same (triheteromer )?ceiling(?!.{0,80}not assumed)", c[:80])

    def test_the_two_gyki_compounds_stay_distinct_in_the_comparator_table(self):
        c = {r["comparator"]: r for r in tsv(DR / "comparators_it39_20261109/output/comparators.tsv") if r["inv_id"] == "INV-05"}
        self.assertIn("CHEMBL267450", c["GYKI 53655"]["target_and_action"]); self.assertIn("different structure", c["GYKI 53655"]["target_and_action"])
        self.assertNotIn("CHEMBL267450", c["NBQX"]["target_and_action"])

    def test_ifenprodil_values_are_not_carried_to_ro_25_6981(self):
        c = {r["comparator"]: r for r in tsv(DR / "comparators_it39_20261109/output/comparators.tsv") if r["inv_id"] == "INV-05"}
        self.assertIn("72 nM", c["ifenprodil"]["selectivity_limits"]); self.assertNotIn("72 nM", c["Ro 25-6981"]["selectivity_limits"])

class Datum(unittest.TestCase):
    def test_potency_and_its_log_transform_are_one_datum(self):
        self.assertTrue(A.same_datum(8.08, 8.3)); self.assertTrue(A.same_datum(8.08, 8.3176)); self.assertTrue(A.same_datum(7.64, 22.9))
        self.assertFalse(A.same_datum(8.08, 22.9))
        reg = " ".join(r["registry_note"] for r in tsv(DR / "generation_it41_20261109/compound_view.tsv"))
        self.assertNotRegex(reg, r"pIC50 8\.08 and 8\.30")

class PhaseApprovalAccess(unittest.TestCase):
    def test_approval_words_are_scoped_to_what_the_catalogue_says(self):
        for r in tsv(DR / "generation_it41_20261109/compound_view.tsv"):
            for k in ("action", "rationale", "open_premise", "counter", "next_test", "moves"):
                for m in re.finditer(r"approv\w*", r[k], re.I):
                    ctx = r[k][max(0, m.start() - 25): m.end() + 40].lower()
                    self.assertTrue("no approval statement" in ctx, (r["item_id"], k, ctx))

class SpeciesPreparation(unittest.TestCase):
    def test_radiprodil_keeps_species_and_assembly(self):
        r = {x["item_id"]: x for x in tsv(DR / "generation_it41_20261109/compound_view.tsv")}["V05"]
        self.assertTrue(re.search(r"rat", r["action"]) and re.search(r"human", r["action"]) and "triheteromer" in r["action"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
