#!/usr/bin/env python3
"""Tests of the IT11 P2.1 wrapper (phenotype_first_it11.py) and of the committed reconstruction (pairs.tsv). Each decision test has an inverse.

  python3 test_it11_p21.py          # exits 0 when every check passes
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, importlib.util, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.argv = ["x", "run"]
spec = importlib.util.spec_from_file_location("pf11", HERE / "phenotype_first_it11.py")
pf = importlib.util.module_from_spec(spec); sys.modules["pf11"] = pf; spec.loader.exec_module(pf)
R4 = pf.IT10 / "results_v4"


class TruncationArtefact(unittest.TestCase):
    def test_lithium_is_seed_specific_in_the_full_list_and_missing_from_the_truncated_tables(self):
        orig = {r["intervention"].split(",")[0].split(" (")[0]: r for r in pf.dz.phenotype_first(R4, pf.DR, None)}
        self.assertTrue(orig["Lithium"]["graph_status"].startswith("NAME_TWIN_SCORED_NOT_SPECIFIC"))        # the IT10 label
        ext = {r["intervention"].split(",")[0].split(" (")[0]: r for r in pf.extended(R4)}
        self.assertEqual(ext["Lithium"]["graph_status_it11"], "IN_SEED_SPECIFIC_ARM:Q6/mimics")
        # inverse: the truncated candidate tables (the IT10 source) hold no seed-specific lithium row, which is the artefact
        trunc = [r for q in range(1, 8) for r in pf.dz.rd(R4 / f"candidates_Q{q}.tsv") if "lithium" in r["name"].lower() and r["seed_specific_all_three_nulls"] == "1"]
        self.assertEqual(trunc, [])
        full = pf.seed_specific_full(R4)
        self.assertTrue(any("lithium" in k for k in full))

    def test_other_leads_are_unchanged(self):
        ext = {r["intervention"].split(",")[0].split(" (")[0]: r for r in pf.extended(R4)}
        for k in ("Ethosuximide", "Vigabatrin"):
            self.assertEqual(ext[k]["graph_status_it11"], ext[k]["graph_status"])
        self.assertEqual(ext["d-APV"]["graph_status_it11"], ext["d-APV"]["graph_status"])


class Reachability(unittest.TestCase):
    E = [("A", "B", 1, "T"), ("C", "A", 1, "P")]

    def test_codes_on_a_toy_network(self):
        self.assertEqual(pf.reachability({"B"}, self.E), "TARGETS_SINK_ONLY")
        self.assertEqual(pf.reachability({"A"}, self.E), "TARGETS_HAVE_OUT_EDGES")
        self.assertEqual(pf.reachability({"Z"}, self.E), "TARGETS_NOT_IN_NETWORK")
        self.assertEqual(pf.reachability(set(), self.E), "NO_SIGNED_TARGET")

    def test_inverse_one_added_edge_changes_the_code(self):
        self.assertEqual(pf.reachability({"B"}, self.E + [("B", "A", -1, "P")]), "TARGETS_HAVE_OUT_EDGES")

    def test_the_real_leads(self):
        r = {x["intervention"].split(",")[0].split(" (")[0]: x["reachability"] for x in pf.extended(R4)}
        self.assertEqual(r["Ethosuximide"], "TARGETS_SINK_ONLY")           # CACNA1G/H have in-edges only, CACNA1I none
        self.assertEqual(r["Vigabatrin"], "TARGETS_NOT_IN_NETWORK")        # ABAT, SLC32A1 are not nodes
        self.assertEqual(r["Lithium"], "TARGETS_HAVE_OUT_EDGES")
        self.assertEqual(r["d-APV"], "TARGETS_HAVE_OUT_EDGES")


class ClassMates(unittest.TestCase):
    ROWS = [dict(family_id="F1", target_symbol="X", mean_sign="-1"), dict(family_id="F2", target_symbol="X", mean_sign="-1"),
            dict(family_id="F3", target_symbol="X", mean_sign="1"), dict(family_id="F4", target_symbol="Y", mean_sign="-1")]

    def test_same_sign_only(self):
        m, _ = pf.class_mates({"X": -1.0}, self.ROWS)
        self.assertEqual([f for f, _ in m], ["F1", "F2"])

    def test_inverse_opposite_sign_returns_the_other_family(self):
        m, _ = pf.class_mates({"X": 1.0}, self.ROWS)
        self.assertEqual([f for f, _ in m], ["F3"])

    def test_the_lead_is_not_its_own_class_mate_and_nothing_is_transferred(self):
        r = {x["intervention"].split(",")[0].split(" (")[0]: x for x in pf.extended(R4)}
        self.assertNotIn("CHEMBL696[", r["Ethosuximide"]["class_mates_top"])
        self.assertNotIn("6998a1a2d947", r["Ethosuximide"]["class_mates_top"])
        self.assertNotIn("CHEMBL89598[", r["Vigabatrin"]["class_mates_top"])


class Context(unittest.TestCase):
    def test_context_columns(self):
        r = {x["intervention"].split(",")[0].split(" (")[0]: x for x in pf.extended(R4)}
        self.assertEqual(r["Ethosuximide"]["ctx_species"], "mouse")
        self.assertEqual(r["Vigabatrin"]["ctx_species"], "human")
        self.assertEqual(r["Vigabatrin"]["ctx_depth"], "queried_not_full_read")
        self.assertIn("ex vivo slice", r["d-APV"]["ctx_system"])


class Reconstruction(unittest.TestCase):
    P = list(csv.DictReader(open(HERE / "pairs.tsv"), delimiter="\t"))

    def test_ethosuximide_and_vigabatrin_have_no_pair_at_all(self):
        for mol in ("ethosuximide", "vigabatrin", "A51"):
            self.assertEqual([r for r in self.P if r["molecule"] == mol and r["signed_usable"] == "1"], [])

    def test_apv_only_direct(self):
        rows = [r for r in self.P if r["molecule"] == "d-APV"]
        self.assertEqual([(r["target"], r["seed_gene"], r["direct_target_is_seed"]) for r in rows], [("GRIN2C", "GRIN2C", "1")])

    def test_lithium_has_a_v4_chain_to_myc_at_expression_level_and_none_at_protein_level(self):
        e = [r for r in self.P if r["molecule"] == "lithium" and r["seed_set"].startswith("Q6_expression") and r["signed_usable"] == "1" and r["chain_v4"]]
        p = [r for r in self.P if r["molecule"] == "lithium" and r["seed_set"].startswith("Q6_protein") and r["signed_usable"] == "1" and r["chain_v4"]]
        self.assertTrue(e)
        self.assertEqual(p, [])                                   # inverse: the protein level has no admissible chain under F1 + F5


if __name__ == "__main__":
    unittest.main(argv=["x"])
