"""IT42 P1: three cases traced mechanically from relation to the public page, and the consistency gate that makes the engine's qualification a reader-facing constraint (an item cannot be shown as emerged, known or probe if the engine EXCLUDES every row of its molecules)."""
import csv, json, re, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent; IT41 = DR / "generation_it41_20261109"
sys.path.insert(0, str(IT41)); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import action_search as A  # noqa: E402
def tsv(p): return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
ROWS = tsv(IT41 / "search_rows.tsv"); CV = tsv(IT41 / "compound_view.tsv"); REL = {r["relation_id"] for r in tsv(IT41 / "relations_it41.tsv")}
def rows_for(item):
    keys = {A.name_key(n.strip()) for n in re.sub(r"\s*\(.*?\)", "", item["name_full"]).split(";") if n.strip()}
    return [r for r in ROWS if r["relation_id"] == item["relation_id"] and any(k and (k in A.name_key(r["name"])) for k in keys)]

class Gate(unittest.TestCase):
    def test_every_item_has_a_relation_and_no_shown_candidate_is_excluded_by_the_engine(self):
        for it in CV:
            self.assertIn(it["relation_id"], REL, it["item_id"])
            rs = rows_for(it)
            if it["kind"] in ("emerged", "known_requalified", "probe") and rs:
                self.assertTrue(any(r["qualification"] in ("CANDIDATE", "UNKNOWN") for r in rs), (it["item_id"], "all rows excluded by the engine"))
            if it["kind"] == "weakened" and it["item_id"] == "V09":
                self.assertTrue(rs and all(r["qualification"] == "UNKNOWN" for r in rs), "DQP-1105 stays unresolved, not negative")

class Case1FavourableConditional(unittest.TestCase):
    def test_relation_to_search_to_selection_to_investigation_to_page(self):
        s1 = [r for r in ROWS if r["relation_id"] == "S1" and r["qualification"] == "CANDIDATE"]
        self.assertTrue({"RADIPRODIL", "onfasprodil", "NP10679"} <= {r["name"] for r in s1})
        self.assertTrue(any(r["name"] == "onfasprodil" and "receptor_site" in r["unknown_fields"] for r in s1), "the unknown site is carried, not dropped")
        inv = {r["inv_id"]: r for r in tsv(DR / "ranking_it8_p9_20261029/investigations_it20.tsv")}
        self.assertIn("ifenprodil 32 percent, radiprodil 45 percent in rat", inv["INV-05"]["next_test"])
        self.assertIn("[IT41] Decision", inv["INV-05"]["feasibility"])
        html = (DR / "view/index_shareable.html").read_text(encoding="utf-8")
        for v in ("V02", "V05", "V06", "V07"): self.assertIn(f'id="cv-{v}"', html)

class Case2AmbiguousIdentity(unittest.TestCase):
    def test_label_conflict_travels_from_the_identity_table_to_the_badge(self):
        s8 = [r for r in ROWS if r["relation_id"] == "S8" and r["name"] == "GYKI53784"]
        self.assertTrue(s8 and all(r["qualification"] == "UNKNOWN" and r["reason"] == "label_conflict" for r in s8))
        self.assertTrue(any(r["name"] == "GYKI53655" and r["qualification"] == "CANDIDATE" for r in ROWS if r["relation_id"] == "S8"), "the distinct structure is not dragged down with it")
        comp = [r for r in tsv(DR / "comparators_it39_20261109/output/comparators.tsv") if r["comparator"] == "GYKI 53655"]
        self.assertTrue(comp and "CHEMBL267450" in comp[0]["target_and_action"] and "different structure" in comp[0]["target_and_action"])
        html = (DR / "view/index_shareable.html").read_text(encoding="utf-8")
        self.assertRegex(html, r'id="cv-V03".{0,400}cv-id-conflict')

class Case3StaysUnknown(unittest.TestCase):
    def test_absence_and_unresolved_values_are_not_negatives(self):
        s6 = [r for r in ROWS if r["relation_id"] == "S6" and r["target_symbol"].upper() == "SLC12A5"]
        self.assertTrue(s6 and all(r["qualification"] == "EXCLUDED" and r["reason"] == "direction_opposite" for r in s6), "KCC2 rows are inhibitors; no enhancer row exists, which is not an absent action")
        v = {r["item_id"]: r for r in CV}
        self.assertEqual(v["V09"]["kind"], "weakened"); self.assertEqual(v["V10"]["kind"], "weakened")
        p = tsv(DR / "generation_it41_20261109/results_s18/proposals_it21.tsv")
        self.assertTrue(all(r["shared_premise_investigation"] == "INV-19" for r in p if r["proposal_id"] in ("IT21P2-0001", "IT21P2-0002", "IT21P2-0003")))

if __name__ == "__main__":
    unittest.main(verbosity=2)
