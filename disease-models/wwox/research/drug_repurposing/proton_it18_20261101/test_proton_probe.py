#!/usr/bin/env python3
"""Offline regressions for proton_probe.py (standard library only; the torch path is exercised by the real run)."""
from __future__ import annotations

import csv
import io
import json
import math
import os
import pickle
import subprocess
import sys
import tempfile
import unittest
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import proton_probe as pp  # noqa: E402


class PureHelpers(unittest.TestCase):
    def test_score_pair_matches_formula_and_is_symmetric(self):
        s, w, d = [1.0, -2.0, 0.5], [0.3, 0.7, -1.0], [-0.5, 2.0, 1.0]
        raw = 1.0 * 0.3 * (-0.005) + (-0.02) * 0.7 * 2.0 + 0.5 * (-1.0) * 1.0
        self.assertAlmostEqual(pp.score_pair(s, w, d), 1 / (1 + math.exp(-raw)))
        self.assertAlmostEqual(pp.score_pair(s, w, d), pp.score_pair(d, w, s))

    def test_relation_index_unique(self):
        et = [("a", "r", "b"), ("drug", "drug_protein", "gene/protein")]
        self.assertEqual(pp.relation_index(et, pp.DRUG_PROTEIN), 1)
        with self.assertRaises(ValueError):
            pp.relation_index(et + [("drug", "drug_protein", "gene/protein")], pp.DRUG_PROTEIN)

    def test_percentile_ties_share_mean_rank(self):
        pr = pp.percentile_ranks({"a": 3, "b": 2, "c": 2, "d": 1})
        self.assertEqual(pr["a"], 0.0)
        self.assertEqual(pr["b"], pr["c"])
        self.assertAlmostEqual(pr["b"], 1.5 / 4)
        self.assertAlmostEqual(pr["d"], 3 / 4)

    def test_tuple_scores_rank_lexicographically(self):
        pr = pp.percentile_ranks({"x": (1, 5), "y": (1, 9), "z": (0, 99)})
        self.assertLess(pr["y"], pr["x"])
        self.assertLess(pr["x"], pr["z"])

    def test_recall_and_empty(self):
        self.assertEqual(pp.recall_at([0.0, 0.04, 0.5, 0.9], 0.05), 0.5)
        self.assertIsNone(pp.recall_at([], 0.05))

    def test_sign_test(self):
        r = pp.sign_test([0.1] * 10, [0.2] * 10)
        self.assertEqual(r["a_better"], 10)
        self.assertAlmostEqual(r["p"], 2 / 1024)
        self.assertEqual(pp.sign_test([0.1], [0.1])["p"], 1.0)

    def test_spearman(self):
        self.assertAlmostEqual(pp.spearman([1, 2, 3, 4], [10, 20, 30, 40]), 1.0)
        self.assertAlmostEqual(pp.spearman([1, 2, 3, 4], [4, 3, 2, 1]), -1.0)


class Unpickler(unittest.TestCase):
    def _zip_with(self, obj_bytes):
        d = tempfile.mkdtemp()
        p = os.path.join(d, "x.pt")
        with zipfile.ZipFile(p, "w") as z:
            z.writestr("arch/data.pkl", obj_bytes)
        return p

    def test_refuses_foreign_global(self):
        p = self._zip_with(b"\x80\x02cos\nsystem\nX\x04\x00\x00\x00trueq\x00\x85R.")
        with self.assertRaises(pickle.UnpicklingError):
            pp.load_pickled_array(p)

    def test_plain_list_loads(self):
        p = self._zip_with(pickle.dumps([1, 2, 3], protocol=2))
        self.assertEqual(pp.load_pickled_array(p), [1, 2, 3])


class Reference(unittest.TestCase):
    def test_catalogue_reference_filters(self):
        recs = [
            {"ids": {"drugbank": ["DB1"], "chembl": "C1"}, "targets": [
                {"source": "ChEMBL curated mechanism", "direct_interaction": 1, "organism": "Homo sapiens",
                 "target_type": "SINGLE PROTEIN", "gene_symbols": ["GRIN1"], "action_type": "ANTAGONIST", "target_id": "T1"},
                {"source": "ChEMBL curated mechanism", "direct_interaction": 0, "organism": "Homo sapiens",
                 "target_type": "SINGLE PROTEIN", "gene_symbols": ["GRIN1"], "action_type": "X", "target_id": "T1"},
                {"source": "ChEMBL curated mechanism", "direct_interaction": 1, "organism": "Rattus norvegicus",
                 "target_type": "SINGLE PROTEIN", "gene_symbols": ["GRIN1"], "action_type": "X", "target_id": "T2"},
                {"source": "DGIdb", "direct_interaction": 1, "organism": "Homo sapiens",
                 "target_type": "SINGLE PROTEIN", "gene_symbols": ["GRIN1"], "action_type": "X", "target_id": "T3"},
                {"source": "ChEMBL curated mechanism", "direct_interaction": 1, "organism": "Homo sapiens",
                 "target_type": "PROTEIN COMPLEX GROUP", "gene_symbols": ["GRIN1", "GRIN2A", "OTHER"],
                 "action_type": "BLOCKER", "target_id": "T4"}]},
            {"ids": {"drugbank": [], "chembl": "C2"}, "targets": [
                {"source": "ChEMBL curated mechanism", "direct_interaction": 1, "organism": "Homo sapiens",
                 "target_type": "SINGLE PROTEIN", "gene_symbols": ["GRIN1"], "action_type": "X", "target_id": "T1"}]},
        ]
        out = pp.catalogue_reference(recs, {"GRIN1", "GRIN2A"})
        self.assertEqual(sorted((r["gene"], r["stratum"]) for r in out),
                         [("GRIN1", "group_level"), ("GRIN1", "single_protein"), ("GRIN2A", "group_level")])

    def test_need_targets_only_intervention(self):
        needs = {"needs": [{"id": "N1", "intervention_direction": {"direction": "down"}, "targets": [
            {"symbol": "A", "target_kind": "intervention_target"}, {"symbol": "B", "target_kind": "readout_marker"}]}]}
        self.assertEqual([t["symbol"] for t in pp.need_targets(needs)], ["A"])
        self.assertEqual(pp.directed_genes(needs), {"A": "down"})


class ExtractAndCoverage(unittest.TestCase):
    def test_extract_and_coverage_on_synthetic_graph(self):
        d = tempfile.mkdtemp()
        nodes = os.path.join(d, "nodes.csv")
        with open(nodes, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["node_index", "node_id", "node_type", "node_name", "node_source"])
            w.writerow([0, "51741", "gene/protein", "WWOX", "NCBI"])
            w.writerow([1, "2902", "gene/protein", "GRIN1", "NCBI"])
            w.writerow([2, "DB0001", "drug", "Drug A", "DrugBank"])
            w.writerow([3, "14533", "disease", "developmental and epileptic encephalopathy, 28", "MONDO"])
            w.writerow([4, "999", "gene/protein", "OTHER", "NCBI"])
        hdr = "edge_index,index_label,direction,relation,display_relation,full_relation,x_index,x_id,x_type,x_name,x_source,y_index,y_id,y_type,y_name,y_source\n"
        rows = [
            "0,l,forward,drug_protein,target,f,2,DB0001,drug,Drug A,DrugBank,1,2902,gene/protein,GRIN1,NCBI",
            "1,l,reverse,rev_drug_protein,target,f,1,2902,gene/protein,GRIN1,NCBI,2,DB0001,drug,Drug A,DrugBank",
            "2,l,forward,disease_protein,associated with,f,3,14533,disease,DEE28,MONDO,0,51741,gene/protein,WWOX,NCBI",
            "3,l,forward,protein_protein,ppi,f,1,2902,gene/protein,GRIN1,NCBI,4,999,gene/protein,OTHER,NCBI",
        ]
        ez = os.path.join(d, "edges.csv.zip")
        with zipfile.ZipFile(ez, "w") as z:
            z.writestr("edges.csv", hdr + "\n".join(rows) + "\n")
        needs = os.path.join(d, "needs.json")
        json.dump({"needs": [{"id": "N", "intervention_direction": {"direction": "down"},
                              "targets": [{"symbol": "GRIN1", "target_kind": "intervention_target"},
                                          {"symbol": "ABSENT1", "target_kind": "intervention_target"}]}]}, open(needs, "w"))
        out = os.path.join(d, "ex")
        self.assertEqual(pp.main(["extract", "--nodes", nodes, "--edges-zip", ez, "--needs", needs, "--out-dir", out]), 0)
        self.assertEqual(open(os.path.join(out, "drug_protein.tsv")).read(), "2\t1\ttarget\n")
        self.assertEqual(open(os.path.join(out, "ppi_targets.tsv")).read(), "1\t4\n")
        canon = json.load(open(os.path.join(out, "canonical_etypes.json")))
        self.assertEqual(canon["rows"], 4)
        self.assertEqual([tuple(e[:3]) for e in canon["etypes"]], sorted(tuple(e[:3]) for e in canon["etypes"]))
        cov = os.path.join(d, "cov.json")
        self.assertEqual(pp.main(["coverage", "--nodes", nodes, "--needs", needs, "--extract-dir", out, "--out", cov]), 0)
        c = json.load(open(cov))
        self.assertEqual(c["wwox"]["node_index"], [0])
        self.assertEqual(c["need_targets_absent"], ["ABSENT1"])
        self.assertEqual(c["diseases"]["DEE28 (WOREE)"]["disease_protein_genes"], ["WWOX"])
        self.assertFalse(c["woree_word_as_node_name"])


class Cli(unittest.TestCase):
    def test_help_is_safe(self):
        before = set(os.listdir(HERE))
        r = subprocess.run([sys.executable, os.path.join(HERE, "proton_probe.py"), "--help"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0)
        self.assertIn("chembl-check", r.stdout)
        self.assertEqual(before, set(os.listdir(HERE)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
