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


class PhAndTemperature(unittest.TestCase):
    """Cases from the decisive.tsv files of the repurposing packages (ro25_6981, glun2b_comparators, nmda_composition, ampa_comparison)."""
    D09 = "Rat GluN1-1a/GluN2B in Xenopus oocytes, two-electrode voltage clamp at -40 mV, 23 C, 50-100 uM glutamate plus 30 uM glycine, 10 uM EDTA, Mg2+-free (0.5 mM Ba2+), pH 7.6 or 6.9 set with HCl at constant Na+"
    D17 = "Rat GluN1-1a/GluN2B in Xenopus oocytes, conditions as D09; transfer to a slice (bicarbonate buffer, 35 C, Mg2+) is untested; the design needs this as a control for any pH arm"

    def f(self, text, cells=None):
        return ac.parse(text, cells)["fields"]

    def test_ph_is_a_value_not_a_concentration(self):
        f = self.f("Xenopus oocytes, pH 7.4, 10 uM EDTA, 10 mM HEPES")
        self.assertEqual(f["pH"]["values"], [(7.4, 7.4)])
        self.assertEqual(f["EDTA"]["values"], [(1e4, 1e4)])
        self.assertEqual(f["pH"]["values"] + f["EDTA"]["values"], [(7.4, 7.4), (1e4, 1e4)])

    def test_a_series_of_ph_values_agrees_only_with_itself(self):
        self.assertEqual(state(self.D09, self.D09), ac.AGREEMENT)
        self.assertEqual(state("Xenopus oocytes, pH 6.9, -40 mV", "Xenopus oocytes, pH 7.6 or 6.9, -40 mV"), ac.INSUFFICIENT)   # one value of the series is not the series
        self.assertEqual(state("Xenopus oocytes, pH 7.4, -40 mV", "Xenopus oocytes, pH 7.3, -40 mV"), ac.INCOMPATIBILITY)

    def test_a_ph_stated_on_one_side_only_is_not_agreement(self):
        r = ac.compare("Xenopus oocytes, -40 mV, 23 C", "Xenopus oocytes, -40 mV, 23 C, pH 7.4")
        self.assertEqual(r["state"], ac.INSUFFICIENT)
        self.assertIn("pH stated only in b", " ".join(r["reasons"]))

    def test_not_stated_is_declared_and_not_a_value(self):
        f = self.f("HEK293, 3 uM glutamate, 20 mM HEPES (pH not stated), no Zn2+ chelator stated")
        self.assertEqual((f["pH"]["state"], f["pH"]["values"]), ("NOT_STATED", []))
        r = ac.compare("HEK293, 3 uM glutamate, pH 7.4", "HEK293, 3 uM glutamate, 20 mM HEPES (pH not stated)")
        self.assertEqual(r["state"], ac.INSUFFICIENT)
        self.assertEqual(r["one_sided"][0]["other"], "declared not stated on the other side")
        self.assertEqual(self.f("age, temperature, holding potential, Mg2+ and agonist conditions not in the abstract")["temperature_C"]["state"], "NOT_STATED")

    def test_not_applicable_is_not_not_stated(self):
        self.assertEqual(self.f("Purified protein, circular dichroism; pH not applicable to the docking")["pH"]["state"], "NOT_APPLICABLE")

    def test_bath_and_pipette_ph_do_not_meet(self):
        r = ac.compare("Slice, bath pH 7.4, pipette pH 7.2", "Slice, bath pH 7.4")
        self.assertEqual(r["state"], ac.INSUFFICIENT)
        self.assertIn("pH_extracellular", r["agreed"])
        self.assertNotEqual(ac.compare("Slice, pipette solution pH 7.2-7.3", "Slice, bath pH 7.4")["state"], ac.INCOMPATIBILITY)

    def test_unqualified_ph_meets_the_extracellular_one_only_when_equal(self):
        eq = ac.compare("Oocytes, pH 7.4, -40 mV", "Oocytes, aCSF pH 7.4, -40 mV")
        self.assertEqual(eq["state"], ac.AGREEMENT)
        self.assertEqual(eq["notes"], ["pH_extracellular: side stated on one side only"])
        diff = ac.compare("Oocytes, pH 7.2, -40 mV", "Oocytes, aCSF pH 7.4, -40 mV")
        self.assertEqual(diff["state"], ac.INSUFFICIENT)     # the 7.2 may be a pipette, so no documented incompatibility
        self.assertIn("side", diff["reasons"][0])

    def test_a_step_and_a_difference_are_not_absolute_values(self):
        step = self.f("pHo step (7.4 to 7.1, with 7.7) per cell")
        self.assertEqual(step["pH_step"]["values"], [(7.4, 7.1)])
        self.assertNotIn("pH", step)
        self.assertNotIn("pH_extracellular", step)
        self.assertEqual(self.f("a 0.2 pH unit fall of pHo")["pH_delta"]["values"], [(0.2, 0.2)])
        self.assertEqual(state("Slice, pHo step (7.4 to 7.1)", "Slice, pH 7.4"), ac.INSUFFICIENT)
        self.assertEqual(state("Slice, a 0.2 pH unit fall", "Slice, pH 7.2"), ac.INSUFFICIENT)
        self.assertEqual(state("Slice, pHo step (7.4 to 7.1)", "Slice, pHo step (7.4 to 7.2)"), ac.INCOMPATIBILITY)

    def test_a_range_or_a_step_that_the_text_does_not_say_is_left_unplaced(self):
        p = ac.parse("Oocytes, pH 7.4 to 7.2")
        self.assertNotIn("pH", p["fields"])
        self.assertTrue(any("range or a step" in u for u in p["unplaced"]))
        self.assertEqual(self.f("Cs pipette solution, pH 7.2-7.3")["pH_intracellular"]["values"], [(7.2, 7.3)])

    def test_temperature_is_read_where_the_assay_is_run(self):
        self.assertEqual(self.f("slice, 30-32 C, current clamp")["temperature_C"]["values"], [(30.0, 32.0)])
        self.assertEqual(state("Mouse slice, 35 C", "Mouse slice, 35 C"), ac.AGREEMENT)
        self.assertEqual(state("Mouse slice, 35 C", "Mouse slice, room temperature"), ac.INCOMPATIBILITY)
        r = ac.compare("Xenopus oocytes, 23 C", "Xenopus oocytes, room temperature")
        self.assertEqual(r["state"], ac.INSUFFICIENT)     # 23 C is inside the nominal room range: not equal, not different
        self.assertIn("read as 18-26 C", r["reasons"][0])

    def test_loading_temperature_is_not_the_assay_temperature(self):
        p = ac.parse("Fura-2 plate reader; buffer 1 mM Mg2+, pH 7.4; assay temperature not stated (Fura-2 loading 37 C)")
        self.assertEqual(p["fields"]["temperature_C"]["state"], "NOT_STATED")
        self.assertIn("37 C (not an assay temperature)", p["unplaced"])
        self.assertEqual(self.f("oocytes, -40 mV, 23 C, assay 3-4 days after injection")["temperature_C"]["values"], [(23.0, 23.0)])

    def test_a_contrast_clause_is_not_the_assay_condition(self):
        cells = {"D09": self.D09, "D17": self.D17}
        p = ac.parse(self.D17, cells)
        self.assertEqual(p["fields"]["temperature_C"]["values"], [(23.0, 23.0)])      # inherited from D09, not the 35 C of the untested transfer
        self.assertEqual(p["contrast"], ["transfer to a slice (bicarbonate buffer, 35 C, Mg2+) is untested"])
        self.assertEqual(ac.compare(p, ac.parse(self.D09, cells))["state"], ac.AGREEMENT)

    def test_a_local_override_replaces_only_what_it_states(self):
        cells = {"D09": self.D09, "D20": "As D09; 35 C", "D21": "As D09; pH 7.4"}
        a, b = ac.parse(cells["D20"], cells)["fields"], ac.parse(cells["D21"], cells)["fields"]
        self.assertEqual((a["temperature_C"]["values"], a["pH"]["values"]), ([(35.0, 35.0)], [(7.6, 7.6), (6.9, 6.9)]))
        self.assertEqual((b["pH"]["values"], b["temperature_C"]["values"]), ([(7.4, 7.4)], [(23.0, 23.0)]))

    def test_missing_and_circular_references_are_named(self):
        cells = {"D01": "As D02", "D02": "As D01; 5 uM ATP", "D03": "oocytes; 1 mM ATP, 23 C"}
        circ = ac.parse(cells["D01"], cells)
        self.assertEqual(circ["inherit_state"], "CIRCULAR")
        r = ac.compare(ac.parse("oocytes; 1 mM ATP, 23 C", cells), ac.parse("As D99; 1 mM ATP, 23 C", {**cells}))
        self.assertEqual(r["state"], ac.INSUFFICIENT)       # the stated fields agree, but a missing reference must not read as agreement
        self.assertIn("unresolved (missing)", " ".join(r["reasons"]))
        self.assertTrue(any("D99" in u for u in r["unplaced"]))
        self.assertEqual(ac.compare(ac.parse("oocytes; 1 mM ATP, 23 C", cells), ac.parse("oocytes; 1 mM ATP, 23 C", cells))["state"], ac.AGREEMENT)

    def test_partly_overlapping_compositions_stay_insufficient(self):
        r = ac.compare("HEK293, GluA2/GluK1, 4 C", "HEK293, GluA2, 4 C")
        self.assertEqual(r["state"], ac.INSUFFICIENT)
        self.assertEqual(r["partial"][0]["field"], "composition")


class StructuredCells(unittest.TestCase):
    """Cells written as key=value (SCI46 decisive tables): readout class, loss arm, whether the loss was verified, cell type."""
    D07 = "species=Homo sapiens (female-derived cell line); system=annonacin 20 nM, glucose-reduced medium; cell=LUHMES differentiated; time=48 h; compound conc=40 uM; readout=calcein viability and Tuj-1 neurite; knockdown=none in this panel"
    D10 = "species=Rattus norvegicus; system=irradiated primary microglia (neonatal spinal cord) stable shRNA or CRISPR lines; cell=microglia; time=72 h after radiation, drug pre-treatment; compound conc=1 uM; readout=mRNA, CCK-8, TUNEL; knockdown=shRNA about 0.1 and KO about 0.05 Nrf2 mRNA (figure-read)"

    def test_the_labels_are_read_from_the_cell(self):
        a, b = ac.parse(self.D07)["fields"], ac.parse(self.D10)["fields"]
        self.assertEqual((a["readout_class"]["values"], a["nrf2_loss_arm"]["values"], "nrf2_loss_verified" in a), (["viability", "function"], ["none"], False))
        self.assertEqual((b["readout_class"]["values"], b["nrf2_loss_arm"]["values"], b["nrf2_loss_verified"]["values"]), (["mRNA", "viability"], ["shRNA", "knockout"], ["yes"]))
        self.assertEqual((a["system"]["values"], b["system"]["values"]), (["cultured_cells"], ["cultured_cells"]))     # the system strings now parse

    def test_a_loss_arm_against_no_loss_arm_is_a_documented_incompatibility(self):
        r = ac.compare(self.D07, self.D10)
        self.assertEqual(r["state"], ac.INCOMPATIBILITY)
        self.assertEqual([d["field"] for d in r["differ"]], ["nrf2_loss_arm"])

    def test_reporter_and_enzyme_readouts_are_not_one_assay(self):
        a = "system=U2OS cell line; readout=ARE reporter; knockdown=none; cell=U2OS"
        b = "system=U2OS cell line; readout=NQO1 enzyme activity; knockdown=none; cell=U2OS"
        self.assertEqual(state(a, b), ac.INCOMPATIBILITY)
        self.assertEqual(state(a, a), ac.AGREEMENT)

    def test_cell_type_wording_alone_never_makes_an_incompatibility(self):
        a = "system=cell line; readout=mRNA; knockdown=siRNA verified; cell=differentiated neuron-like"
        b = "system=cell line; readout=mRNA; knockdown=siRNA verified; cell=LUHMES differentiated"
        r = ac.compare(a, b)
        self.assertEqual(r["state"], ac.INSUFFICIENT)
        self.assertEqual(r["partial"][0]["field"], "cell")

    def test_unverified_and_incomplete_losses_are_not_verified(self):
        for kd, want in (("NRF2 siRNA, unverified in the record", "unstated"), ("siRNA incomplete at protein level", "no"), ("shRNA over 95 % knockdown declared", "yes")):
            self.assertEqual(ac.parse(f"system=cell line; readout=mRNA; knockdown={kd}")["fields"]["nrf2_loss_verified"]["values"], [want], kd)


if __name__ == "__main__":
    unittest.main(verbosity=2)
