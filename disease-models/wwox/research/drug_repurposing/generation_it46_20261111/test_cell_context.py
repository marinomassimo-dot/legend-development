import csv, tempfile, unittest
from pathlib import Path
import cell_context as cc


def table(rows):
    d = tempfile.mkdtemp(); p = Path(d) / "t.tsv"
    with open(p, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t"); w.writerow(["gene", "cell_class", "n_samples", "mean_fpkm"]); w.writerows(rows)
    return [dict(key="t", species="mouse", path=p, cls="cell_class", val="mean_fpkm", n="n_samples", neuron=r"^neurons?\b", skip=r"^$")]


class Classify(unittest.TestCase):
    def setUp(self):
        self.keep = cc.TABLES

    def tearDown(self):
        cc.TABLES = self.keep

    def test_states(self):
        cc.TABLES = table([("A", "neurons (P7)", 2, 30), ("A", "astrocytes (P7)", 2, 1),
                           ("B", "neurons (P7)", 2, 1.5), ("B", "astrocytes (P7)", 2, 90),
                           ("C", "neurons (P7)", 2, 8), ("C", "astrocytes (P7)", 2, 5),
                           ("D", "neurons (P7)", 2, 0.2), ("D", "astrocytes (P7)", 2, 0.4)])
        s = {r["gene"]: (r["state"], r["attributable_to_neuron"]) for r in cc.join(["A", "B", "C", "D", "E"])}
        self.assertEqual(("NEURON_ENRICHED", "yes"), s["A"])
        self.assertEqual(("OTHER_ENRICHED", "no"), s["B"])
        self.assertEqual(("SHARED", "partly"), s["C"])
        self.assertEqual(("NOT_DETECTED_IN_TABLE", "unknown"), s["D"])   # below the floor: unknown, not absent
        self.assertEqual(("NOT_IN_TABLE", "unknown"), s["E"])            # never queried: unknown, never low

    def test_a_gene_not_in_the_table_is_not_a_negative(self):
        cc.TABLES = table([("A", "neurons (P7)", 2, 30), ("A", "astrocytes (P7)", 2, 1)])
        rows, text = cc.context_for(["A", "Z"])
        self.assertIn("not in any table (unknown): Z", text)
        self.assertNotIn(" low", text)

    def test_no_gene_known_says_open_question(self):
        cc.TABLES = table([("A", "neurons (P7)", 2, 30)])
        _, text = cc.context_for(["Q"])
        self.assertIn("open question, not an answer", text)

    def test_age_label_travels_with_the_row(self):
        cc.TABLES = table([("A", "neurons (P7)", 2, 30), ("A", "astrocytes (P7)", 2, 1)])
        r = cc.join(["A"])[0]
        self.assertEqual("neurons (P7)", r["neuron_class"])
        self.assertIn("age", r["caveat"])


class RealTables(unittest.TestCase):
    """facts of the held SCI44 tables (a change in the table is a change to read, not a silent pass)"""
    def test_kv7_hcn_and_kir4_1_as_held(self):
        s = {(r["gene"], r["table"]): r["state"] for r in cc.join(["KCNQ2", "KCNQ3", "KCNQ4", "HCN1", "HCN2", "KCNJ10"])}
        self.assertEqual("SHARED", s[("KCNQ2", "mouse")])            # neurons 30.68 against OPC 10.68: 2.9-fold, under the 3-fold convention
        self.assertEqual("OTHER_ENRICHED", s[("KCNQ2", "human")])    # one neuron sample at 0.10 FPKM against fetal astrocytes 4.30
        self.assertEqual("NOT_IN_TABLE", s[("KCNQ4", "mouse")])
        self.assertEqual("NEURON_ENRICHED", s[("HCN1", "mouse")])
        self.assertEqual("OTHER_ENRICHED", s[("HCN2", "mouse")])     # myelinating oligodendrocytes 66.3 against neurons 17.9
        self.assertEqual("OTHER_ENRICHED", s[("KCNJ10", "mouse")])

    def test_gaba_and_chloride_genes_as_held(self):
        s = {(r["gene"], r["table"]): r["state"] for r in cc.join(["SLC12A5", "SLC12A2", "SLC6A1", "ABAT"])}
        self.assertEqual("NEURON_ENRICHED", s[("SLC12A5", "mouse_gaba")])
        self.assertEqual("OTHER_ENRICHED", s[("SLC12A2", "mouse_gaba")])    # newly formed oligodendrocytes 100 against neurons 5
        self.assertEqual("OTHER_ENRICHED", s[("SLC6A1", "mouse_gaba")])     # astrocytes 420 against neurons 129
        self.assertEqual("SHARED", s[("ABAT", "mouse_gaba")])
        _, text = cc.context_for(["SLC12A5", "SLC12A2"])
        self.assertIn("SLC12A5 (mouse neuron-enriched, human neuron-enriched)", text)

    def test_nrf2_axis_genes_as_held(self):
        s = {(r["gene"], r["table"]): r["state"] for r in cc.join(["NFE2L2", "KEAP1", "NQO1", "HMOX1"])}
        self.assertEqual("OTHER_ENRICHED", s[("NFE2L2", "mouse_nrf2")])   # astrocytes 11.87 against neurons 2.11
        self.assertEqual("OTHER_ENRICHED", s[("HMOX1", "mouse_nrf2")])    # microglia 260 against neurons 2.4
        self.assertIn(s[("NQO1", "mouse_nrf2")], ("OTHER_ENRICHED", "NOT_DETECTED_IN_TABLE", "SHARED"))   # at or near the floor in every class

    def test_the_kv7_relation_is_not_assignable_to_neurons_from_these_tables(self):
        _, text = cc.context_for(["KCNQ2", "KCNQ3", "KCNQ4", "KCNQ5"])
        self.assertIn("cannot be assigned to neurons", text)
        # IT47 B1 gave KCNQ4 and KCNQ5 rows: KCNQ4 shared in mouse and not detected in the human sample; KCNQ5 neuron-enriched in both
        self.assertIn("KCNQ4 (mouse shared, human not detected)", text)
        self.assertIn("KCNQ5 (mouse neuron-enriched, human neuron-enriched)", text)

    def test_relations_are_read_without_the_catalogue_cache(self):
        rel = cc.relations()
        self.assertEqual(["KCNQ2", "KCNQ3", "KCNQ4", "KCNQ5"], rel["R5"])
        self.assertIn("S3", rel)


if __name__ == "__main__":
    unittest.main(verbosity=2)
