#!/usr/bin/env python3
"""Tests for assay_conditions.py. The cells are wording found in the comparison packages' decisive tables (shortened), not invented formats."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assay_conditions as ac  # noqa: E402

OOC = "Xenopus oocytes, two-electrode voltage clamp, -40 mV, "


def state(a, b):
    return ac.compare(a, b)["state"]


class ConcentrationTests(unittest.TestCase):
    def test_one_mM_against_one_uM_is_documented_incompatibility(self):
        r = ac.compare("oocytes, 1 mM ATP", "oocytes, 1 uM ATP")
        self.assertEqual(r["state"], ac.INCOMPATIBILITY)
        self.assertIn("power of 1000", r["differ"][0]["b"])

    def test_one_mM_equals_1000_uM(self):
        self.assertEqual(state("oocytes, 1 mM ATP", "oocytes, 1000 uM ATP"), ac.AGREEMENT)

    def test_micro_sign_variants_read_as_micromolar(self):
        for sign in ("u", "µ", "μ"):
            self.assertEqual(state("oocytes, 5 uM ATP", f"oocytes, 5 {sign}M ATP"), ac.AGREEMENT, sign)

    def test_decimal_and_thousands_separators(self):
        self.assertEqual(state("oocytes, 0.5 mM ATP", "oocytes, 500 uM ATP"), ac.AGREEMENT)
        self.assertEqual(state("oocytes, 0,5 mM ATP", "oocytes, 500 uM ATP"), ac.AGREEMENT)
        self.assertEqual(state("oocytes, 1,000 uM ATP", "oocytes, 1 mM ATP"), ac.AGREEMENT)

    def test_declared_against_missing_is_insufficient_not_compatible(self):
        r = ac.compare("oocytes, 5 uM ATP", "oocytes")
        self.assertEqual(r["state"], ac.INSUFFICIENT)
        self.assertEqual(r["one_sided"][0]["field"], "ATP")

    def test_stated_against_declared_not_stated_names_the_other_side(self):
        r = ac.compare(OOC + "100 uM glutamate plus 30 uM glycine", "Xenopus oocytes; glutamate, glycine and holding potential not stated")
        self.assertEqual(r["state"], ac.INSUFFICIENT)
        self.assertTrue(any("declared not stated" in o["other"] for o in r["one_sided"]))

    def test_unrecognised_systems_are_not_the_same_system(self):
        self.assertEqual(state("a hepatic preparation, 5 uM ATP", "a mitochondrial preparation, 5 uM ATP"), ac.INSUFFICIENT)

    def test_only_the_system_in_common_is_not_agreement(self):
        self.assertEqual(state("oocytes", "oocytes"), ac.INSUFFICIENT)

    def test_range_overlap_is_insufficient_and_disjoint_is_incompatible(self):
        self.assertEqual(state("oocytes, 50-100 uM glutamate", "oocytes, 80 uM glutamate"), ac.INSUFFICIENT)
        self.assertEqual(state("oocytes, 50-100 uM glutamate", "oocytes, 1 mM glutamate"), ac.INCOMPATIBILITY)
        self.assertEqual(state("oocytes, 50-100 uM glutamate", "oocytes, 50-100 uM glutamate"), ac.AGREEMENT)

    def test_a_drug_concentration_is_not_an_assay_condition(self):
        f = ac.parse("Rat GluA2 in HEK293, -60 mV and other potentials, 3 mM Glu, 30 uM cyclothiazide")["fields"]
        self.assertEqual(sorted(f), ["composition", "glutamate", "holding_potential_mV", "system"])
        self.assertEqual(f["glutamate"]["values"], [(3e6, 3e6)])

    def test_two_conditions_in_one_proposition_each_keep_their_value(self):
        f = ac.parse(OOC + "100 uM glutamate plus 50 uM glycine")["fields"]
        self.assertEqual((f["glutamate"]["values"], f["glycine"]["values"]), ([(1e5, 1e5)], [(5e4, 5e4)]))
        f = ac.parse("HEK293, 3 uM glutamate and 3 uM glycine, 1 mM Ca2+")["fields"]
        self.assertEqual((f["glutamate"]["values"], f["glycine"]["values"], f["Ca"]["values"]), ([(3e3, 3e3)], [(3e3, 3e3)], [(1e6, 1e6)]))

    def test_a_number_between_two_solutes_is_left_unplaced(self):
        r = ac.parse("glutamate 100 uM glycine 50 uM")
        self.assertTrue(any("between two solutes" in u for u in r["unplaced"]))


class OtherFieldTests(unittest.TestCase):
    def test_voltage_range_and_open_potentials(self):
        f = ac.parse("slice, whole-cell voltage clamp -70 to +20 mV")["fields"]["holding_potential_mV"]
        self.assertEqual(f["values"], [(-70.0, 20.0)])
        r = ac.compare("HEK293, -60 mV and other potentials, 3 mM Glu", "HEK293, -40 mV, 3 mM Glu")
        self.assertEqual(r["state"], ac.INSUFFICIENT)   # an open list of potentials is not a documented difference
        self.assertEqual(state("HEK293, -60 mV, 3 mM Glu", "HEK293, -40 mV, 3 mM Glu"), ac.INCOMPATIBILITY)

    def test_scaffold_contrast_is_not_a_single_scaffold(self):
        self.assertEqual(state("recombinant kinase assay, core-free", "recombinant kinase assay, core-bound"), ac.INCOMPATIBILITY)
        self.assertEqual(state("recombinant kinase assay, 5 uM ATP, core-free versus core-bound", "recombinant kinase assay, 5 uM ATP, core-free"), ac.INSUFFICIENT)

    def test_free_of_a_cation_is_a_zero(self):
        f = ac.parse("oocytes, Mg2+-free, Zn2+-free")["fields"]
        self.assertEqual((f["Mg"]["values"], f["Zn"]["values"]), ([(0.0, 0.0)], [(0.0, 0.0)]))

    def test_same_gene_family_with_another_composition_differs(self):
        self.assertEqual(state(OOC + "human GluN1/GluN2B", OOC + "rat NR1/NR2A"), ac.INCOMPATIBILITY)
        self.assertEqual(state(OOC + "human GluN1/GluN2B", OOC + "rat NR1-1a plus NR2B"), ac.AGREEMENT)
        self.assertEqual(state(OOC + "GluN1/GluN2A, GluN1/GluN2B", OOC + "GluN1/GluN2B"), ac.INSUFFICIENT)   # one proposition spans compositions

    def test_enzyme_wordings_without_the_word_purified_are_a_known_system(self):
        for text in ("PDK1 kinase assay, 5 uM ATP", "recombinant human PDK1, 5 uM ATP", "enzyme assay, 5 uM ATP", "PDH complex activity assay, 5 uM ATP"):
            self.assertEqual(ac.parse(text)["fields"]["system"]["values"], ["purified_protein"], text)
        self.assertEqual(ac.parse("Recombinant rat GluK2 in HEK-293")["fields"]["system"]["values"], ["HEK"])   # recombinant alone is not an enzyme
        self.assertEqual(state("recombinant human PDK1, 5 uM ATP", "PDK1 kinase assay, 5 mM ATP"), ac.INCOMPATIBILITY)

    def test_a_negated_system_is_not_a_system(self):
        self.assertEqual(ac.parse("Recombinant rat GluK2 in HEK-293; no neuron datum")["fields"]["system"]["values"], ["HEK"])

    def test_different_systems_differ(self):
        self.assertEqual(state("Xenopus oocytes, -40 mV", "Mouse slice, -40 mV"), ac.INCOMPATIBILITY)

    def test_cell_that_refers_to_another_keeps_its_system_and_overrides_the_rest(self):
        cells = {"D01": OOC + "100 uM glutamate plus 50 uM glycine",
                 "D03": "As D01 with 300 nM Zn2+; the tonic Zn2+ in a neocortical slice is not measured",
                 "D04": "As D01; glycine 3 uM with 100 uM glutamate"}
        f = ac.parse(cells["D03"], cells)
        self.assertEqual((f["inherits"], f["fields"]["system"]["values"]), ("D01", ["oocyte"]))
        self.assertEqual(ac.parse(cells["D04"], cells)["fields"]["glycine"]["values"], [(3e3, 3e3)])
        self.assertEqual(ac.compare(ac.parse(cells["D04"], cells), ac.parse(cells["D01"], cells))["differ"][0]["field"], "glycine")

    def test_a_reference_that_cannot_be_resolved_is_not_guessed(self):
        self.assertEqual(ac.parse("As D99; 5 uM ATP", {"D01": "x"})["inherits"], "")

    def test_empty_text_has_no_fields(self):
        self.assertEqual(ac.parse("")["fields"], {})
        self.assertEqual(state("", ""), ac.INSUFFICIENT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
