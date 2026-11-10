#!/usr/bin/env python3
"""IT44 P4 regressions on entity_roles_it44.tsv: no ion is a drug candidate; an excluded physiological ion stays excluded for its relation and stays visible as a physiological variable; the rule can be overridden with a reason."""
import csv, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
def rows():
    with open(HERE / "entity_roles_it44.tsv", encoding="utf-8") as f: return list(csv.DictReader(f, delimiter="\t"))
class Roles(unittest.TestCase):
    def test_no_inorganic_entity_is_a_candidate(self):
        bad = [r["name"] for r in rows() if r["gtopdb_type"] == "Inorganic" and r["role"] == "candidate"]; self.assertEqual(bad, [])
    def test_excluded_physiological_ion_keeps_its_verdict_and_gains_a_role(self):
        zn = [r for r in rows() if r["name"] == "Zn2+" and r["relation_id"] == "S5"]; self.assertTrue(zn)
        self.assertTrue(all(r["engine_verdicts"] == "EXCLUDED" and r["role"] == "physiological_intervention" for r in zn))
    def test_override_wins_and_keeps_the_rule_role(self):
        mg = [r for r in rows() if r["name"] == "Mg2+" and r["relation_id"] == "S2"][0]
        self.assertEqual((mg["rule_role"], mg["role"]), ("control_or_reagent", "physiological_intervention")); self.assertTrue(mg["role_basis"].startswith("override"))
    def test_registry_metabolite_type_is_not_blindly_a_function(self):
        oc = [r for r in rows() if r["name"] == "octanol"][0]; self.assertEqual((oc["rule_role"], oc["role"]), ("physiological_intervention", "control_or_reagent"))
    def test_every_role_is_in_the_vocabulary(self):
        ok = {"candidate", "probe", "control_or_reagent", "physiological_intervention", "unqualified_entity"}; self.assertTrue(all(r["role"] in ok for r in rows()))
if __name__ == "__main__": unittest.main(verbosity=2)
