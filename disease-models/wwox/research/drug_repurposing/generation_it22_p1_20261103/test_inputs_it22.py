#!/usr/bin/env python3
"""IT22 P3 tests: the amended generator inputs are valid, the new input reaches the engine, and a guard on a seed row is consumed by the proposals that seed generates.

  python3 test_inputs_it22.py          (unittest; offline; seconds)
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, importlib.util, subprocess, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
sys.path.insert(0, str(DR.parents[3] / "framework/scripts"))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


G = load("run_generation_it21", DR / "generation_it21_p2_20261103" / "run_generation_it21.py")


def rd(p):
    return list(csv.DictReader(open(p, encoding="utf-8", newline=""), delimiter="\t"))


class GuardConsumption(unittest.TestCase):
    def test_a_seed_guard_becomes_a_limit_on_the_proposal_and_an_annotation_does_too(self):
        sidx = {("Q4_expression_tiersAB", "Q4_expression_tiersAB:NPY"): [dict(seed_id="S116", guard_tag="NPY_SIGN_CONTESTED")],
                ("Q2_expression_tiersAB", "Q2_expression_tiersAB:HK2"): [dict(seed_id="S018", guard_tag="IT7_READOUT6")]}
        p = dict(seed_set="Q4_expression_tiersAB", contributing_seed_1="NPY|NPY|down|hops1-3|BTK|1e-5", contributing_seed_2="")
        tags, limits = G.seed_guard_limits(p, sidx)
        self.assertEqual(tags, ["NPY_SIGN_CONTESTED"])
        self.assertTrue(limits and "contested" in limits[0])
        q = dict(seed_set="Q2_expression_tiersAB", contributing_seed_1="HK2|HK2|up|hops1-3|HIF1A|1e-5", contributing_seed_2="")
        self.assertEqual(G.seed_guard_limits(q, sidx)[1], [])                                    # a guard that does not limit support is listed, not a limit
        tags2, limits2 = G.seed_guard_limits(q, sidx, {"S018": {"SECOND_SYSTEM_GATE_FAILED"}})
        self.assertIn("SECOND_SYSTEM_GATE_FAILED", tags2)
        self.assertTrue(limits2)

    def test_a_limited_row_ranks_after_an_unlimited_one_in_the_hand_over_order(self):
        a = dict(n_origins="2", chain_edges="2", zmin="5", seed_support_limited="yes")
        b = dict(n_origins="1", chain_edges="3", zmin="4", seed_support_limited="")
        self.assertLess(G.order_key(b), G.order_key(a))


class Inputs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = HERE / "inputs_it22"
        if not cls.d.exists():
            raise unittest.SkipTest("inputs_it22 absent")

    def test_the_amended_seed_table_passes_the_existing_checker(self):
        r = subprocess.run([sys.executable, str(DR / "generation_it9_p1_20261030" / "check_seeds.py"), "--root", str(DR), "--dir", str(self.d)], capture_output=True, text=True)
        self.assertIn("PASS", r.stdout, r.stdout[-600:])

    def test_only_the_new_question_adds_an_engine_set_and_the_old_sets_keep_their_engine_columns(self):
        new = {p.name for p in (self.d / "seeds_p1").glob("*.tsv") if p.name != "manifest.tsv"}
        old = {p.name for p in (DR / "generation_it9_p2_20261030" / "seeds_p1").glob("*.tsv") if p.name != "manifest.tsv"}
        self.assertEqual(new - old, {"Q8_expression_tiersAB.tsv"})
        for n in old & new:
            cut = lambda p: [line.split("\t")[:12] for line in open(p)]
            self.assertEqual(cut(self.d / "seeds_p1" / n), cut(DR / "generation_it9_p2_20261030" / "seeds_p1" / n), n)

    def test_a_cell_type_marker_set_cannot_become_a_gene_seed(self):
        s79 = [r for r in rd(self.d / "seeds.tsv") if r["seed_id"] == "S079"][0]
        self.assertEqual((s79["usable_for_generation"], s79["reason_class"]), ("no", "UNUSABLE_MATURITY_OR_COMPOSITION"))
        self.assertIn("COMPOSITION_NOT_REGULATION", s79["guard_tag"])


class RealRun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        p = HERE / "results_p3" / "proposals_it21.tsv"
        if not p.exists():
            raise unittest.SkipTest("results_p3 absent")
        cls.rows = rd(p)

    def test_the_new_input_produces_proposals_and_changes_nothing_it_did_not_touch(self):
        q8 = [r for r in self.rows if r["question"] == "Q8"]
        self.assertGreaterEqual(len(q8), 10)
        old = {r["proposal_id"]: r for r in rd(HERE / "results_p2" / "proposals_it21.tsv")}
        same = [r for r in self.rows if r["question"] != "Q8"]
        self.assertEqual(len(same), len(old))
        self.assertEqual({r["compound"] + r["main_target"] + r["hypothesis"] for r in same}, {r["compound"] + r["main_target"] + r["hypothesis"] for r in old.values()})

    def test_every_q2_row_carries_the_second_system_limit(self):
        q2 = [r for r in self.rows if r["question"] == "Q2"]
        self.assertTrue(q2)
        self.assertTrue(all(r["seed_support_limited"] == "yes" for r in q2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
