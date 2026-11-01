#!/usr/bin/env python3
"""Regressions for the graded same-document comparison (IT15 P2). Synthetic rows are copies of the four real contrasting cases
(apinocaltamide T-type against L-type; the same document's liability panel; ezogabine homomer against heteromer; Ro 25-6981 generic NMDA
complex; ethosuximide censored values); the last test also reads the committed output. `--help` is safe."""
import csv, importlib.util, os, sys, unittest

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("selectivity_p6", os.path.join(H, "selectivity_p6.py"))
sp = importlib.util.module_from_spec(spec); spec.loader.exec_module(sp)


def row(gene, val, rel="=", assay="A1", label="x", species="Homo sapiens"):
    return {"source": "chembl_activity", "compound": "c", "gene": gene, "target_label": label, "action": "", "measure_type": "IC50", "relation": rel,
            "value_nM": "" if val is None else str(val), "species": species, "ref": f"T;D;{assay}"}


def ctx(**kw):
    base = {"assay_cell_type": "HEK293", "description": "inhibition of recombinant channel in HEK293 cells by FLIPR", "data_validity_comment": ""}
    return {a: dict(base, assay_id=a, **v) for a, v in kw.items()}


def grade(rows, c):
    g = sp.collect(rows)
    (k, obs), = g.items()
    return sp.grade_group(obs, c)


class Grades(unittest.TestCase):
    def test_informative_same_system_pair_is_interpretable(self):
        r = [row("CACNA1G", 6.4, assay="A1"), row("CACNA1C", 2410, assay="A2")]
        gr, why, by, comp, attr = grade(r, ctx(A1={}, A2={}))
        self.assertEqual(gr, "INTERPRETABLE", why)

    def test_same_document_but_different_families_is_a_panel_not_selectivity(self):
        r = [row("CACNA1G", 6.4, assay="A1"), row("CYP3A4", 46000, assay="A3"), row("KCNH2", 5500, assay="A4")]
        gr, why, *_ = grade(r, ctx(A1={}, A3={"description": "inhibition of human CYP3A4 using testosterone"}, A4={"description": "ERG by patch clamp"}))
        self.assertEqual(gr, "PANEL_NOT_SELECTIVITY")

    def test_complex_against_component_is_limited(self):
        r = [row("KCNQ2", 930, assay="A1"), row("KCNQ2|KCNQ3", 1720, assay="A2")]
        gr, why, *_ = grade(r, ctx(A1={}, A2={}))
        self.assertEqual(gr, "LIMITED")
        self.assertTrue(any("composition" in w for w in why))

    def test_generic_complex_cannot_be_attributed_to_a_subunit(self):
        r = [row("GRIN1|GRIN2A|GRIN2B|GRIN2C|GRIN2D|GRIN3A|GRIN3B", 5.6), row("ADRA1A|ADRA1B|ADRA1D", 180)]
        gr, why, *_ = grade(r, {})
        self.assertEqual(gr, "NOT_DETERMINABLE")
        self.assertTrue(any("cannot be attributed to one member" in w for w in why))

    def test_missing_assay_context_limits_never_drops(self):
        r = [row("GRIN1|GRIN2A", 911), row("GRIN1|GRIN2B", 1020)]
        gr, why, *_ = grade(r, {})
        self.assertEqual(gr, "LIMITED")
        self.assertTrue(any("assay context not retained" in w for w in why))

    def test_censored_value_is_listed_and_never_a_number(self):
        r = [row("CACNA1G", 6.4), row("CACNA1I", 5e6, rel=">")]
        gr, why, by, comp, attr = grade(r, ctx(A1={}))
        self.assertEqual(gr, "NOT_DETERMINABLE")
        self.assertEqual(by["CACNA1I"]["cens"], [">5e+06"])
        self.assertEqual(by["CACNA1I"]["vals"], [])

    def test_row_without_value_is_counted_and_not_a_negative(self):
        r = [row("CACNA1G", 6.4), row("CACNA1H", None)]
        gr, why, by, comp, attr = grade(r, ctx(A1={}))
        self.assertEqual(by["CACNA1H"]["novalue"], 1)
        self.assertEqual(gr, "NOT_DETERMINABLE")

    def test_minimum_is_not_the_summary_and_discordance_is_flagged(self):
        r = [row("GRIN1|GRIN2A", 10), row("GRIN1|GRIN2A", 1000), row("GRIN1|GRIN2B", 100)]
        gr, why, by, comp, attr = grade(r, {})
        self.assertEqual(gr, "LIMITED")
        self.assertTrue(any("discordant" in w for w in why))
        import statistics
        self.assertEqual(statistics.median(by["GRIN1|GRIN2A"]["vals"]), 505)

    def test_validity_comment_limits(self):
        r = [row("CACNA1G", 6.4, assay="A1"), row("CACNA1C", 2410, assay="A2")]
        gr, why, *_ = grade(r, ctx(A1={}, A2={"data_validity_comment": "Outside typical range"}))
        self.assertEqual(gr, "LIMITED")


class RealDescriptions(unittest.TestCase):
    """The apinocaltamide Cav1.2 and Cav3.x assays (ChEMBL CHEMBL4181722 and CHEMBL4181719) differ in stimulus: KCl against CaCl2 re-addition."""

    def test_different_stimulus_limits_and_offers_no_ratio(self):
        c = ctx(A1={"description": "Inhibition of recombinant Cav3.1 expressed in HEK293 cells assessed as decrease in calcium flux preincubated for 3 mins followed by CaCl2 addition by Fluo-4-AM dye-based FLIPR assay"},
                A2={"description": "Inhibition of recombinant Cav1.2 expressed in HEK293 cells assessed as decrease in calcium flux preincubated for 3 mins followed by KCl addition by Fluo-4-AM dye-based FLIPR assay"})
        gr, why, by, comp, attr = grade([row("CACNA1G", 6.4, assay="A1"), row("CACNA1C", 2410, assay="A2")], c)
        self.assertEqual(gr, "LIMITED")
        self.assertTrue(any("stimulus" in w for w in why))

    def test_unrelated_transporters_are_not_one_family(self):
        self.assertNotEqual(sp.family("SLC1A2"), sp.family("SLC12A5"))
        self.assertEqual(sp.family("GRIN2A"), sp.family("GRIN1"))


class Composition(unittest.TestCase):
    def test_isoform_pair_is_a_group_not_a_complex(self):
        self.assertEqual(sp.composition("GSK3A|GSK3B"), "generic_complex")
        self.assertEqual(sp.composition("CACNA1G|CACNA1H"), "generic_complex")

    def test_true_heteromers_stay_defined(self):
        self.assertEqual(sp.composition("GRIN1|GRIN2B"), "defined_complex")
        self.assertEqual(sp.composition("KCNQ2|KCNQ3"), "defined_complex")

    def test_chembl_target_type_decides_when_present(self):
        self.assertEqual(sp.composition("GRIN1|GRIN2B", "PROTEIN COMPLEX GROUP"), "generic_complex")
        self.assertEqual(sp.composition("CDK5|CDK5R1", "PROTEIN COMPLEX"), "defined_complex")
        self.assertEqual(sp.composition("GSK3B", "SINGLE PROTEIN"), "single")


class CommittedOutput(unittest.TestCase):
    def test_every_ratio_has_a_grade_that_allows_it(self):
        rows = list(csv.DictReader(open(os.path.join(H, "selectivity_same_document.tsv")), delimiter="\t"))
        self.assertTrue(rows)
        for r in rows:
            self.assertIn(r["grade"], {"INTERPRETABLE", "LIMITED", "NOT_DETERMINABLE", "PANEL_NOT_SELECTIVITY"})
            if r["ratio_extreme_target_medians"]:
                self.assertIn(r["grade"], {"INTERPRETABLE", "LIMITED"}, r["document"])
            if r["grade"] == "LIMITED":
                self.assertTrue(r["limits"], r["document"])

    def test_no_generic_complex_row_carries_a_ratio(self):
        for r in csv.DictReader(open(os.path.join(H, "selectivity_same_document.tsv")), delimiter="\t"):
            if "cannot be attributed to one member" in r["limits"] and r["grade"] == "NOT_DETERMINABLE":
                self.assertEqual(r["ratio_extreme_target_medians"], "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
