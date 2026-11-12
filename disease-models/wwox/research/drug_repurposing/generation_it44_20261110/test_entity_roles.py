#!/usr/bin/env python3
"""IT44 P4 regressions on entity_roles_it44.tsv: no ion is a drug candidate; an excluded physiological ion stays excluded for its relation and stays visible as a physiological variable; the rule can be overridden with a reason."""
import csv, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
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
    def test_no_rule_means_unqualified_never_candidate(self):
        import entity_roles as er
        self.assertEqual(er.role_of("Synthetic organic", "", [{"field": "gtopdb_type", "value": "Inorganic", "role": "control_or_reagent", "rule_id": "R1"}]), ("unqualified_entity", "default"))
        self.assertEqual(er.role_of("", "approved_any_source", [{"field": "catalogue_status", "value": "approved_any_source", "role": "candidate", "rule_id": "R7"}]), ("candidate", "R7"))
    def test_a_candidate_role_always_comes_from_a_rule_or_an_override(self):
        self.assertEqual([r["name"] for r in rows() if r["role"] == "candidate" and r["role_basis"] == "rule default"], [])
    def test_every_role_is_in_the_vocabulary(self):
        ok = {"candidate", "probe", "control_or_reagent", "physiological_intervention", "unqualified_entity"}; self.assertTrue(all(r["role"] in ok for r in rows()))

    def test_a_peptide_known_only_by_catalogue_modality_is_a_probe(self):
        import entity_roles as er
        rules = er.tsv(er.HERE / "role_rules_it44.tsv")
        self.assertEqual(("probe", "R9"), er.role_of("", "clinical_candidate", rules, "protein_or_peptide"))   # was a candidate by rule R8
        self.assertEqual(("unqualified_entity", "R10"), er.role_of("", "clinical_candidate", rules, "antibody"))
        self.assertEqual(("candidate", "R8"), er.role_of("", "clinical_candidate", rules, "small_molecule"))


if __name__ == "__main__": unittest.main(verbosity=2)
