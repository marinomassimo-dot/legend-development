#!/usr/bin/env python3
"""Tests of the IT10 P1 generation changes. They exercise the production code (engine_v4/seed_engine_v4.py, dispose_it10.py) on toy graphs and on the
committed IT9 data. Each decision test has an inverse: the behaviour changes when the new rule is switched off.

  python3 test_it10_p1.py          # exits 0 when every check passes
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, importlib.util, os, subprocess, tempfile, unittest
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
DR = HERE.parent


def load(name, path, argv=("x", "selftest")):
    saved = list(sys.argv); sys.argv = list(argv)
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m)
    finally:
        sys.argv = saved
    return m


v4 = load("seed_engine_v4_t", HERE / "engine_v4" / "seed_engine_v4.py")
dz = load("dispose_it10_t", HERE / "dispose_it10.py", argv=("x", "run"))


class JunctionRule(unittest.TestCase):
    """F5: a chain a -> b -> c is admissible only if b is a singleton in both records."""

    def influence_at_a(self, edges, junction):
        g = v4.Graph4(edges, extras=[])
        g.level = "expression"
        S = np.zeros((1, g.N)); S[0, g.idx["C"]] = 1.0
        old = v4.JUNCTION; v4.JUNCTION = junction
        try:
            return float(g.influence_ind(S)[0, g.idx["A"]])
        finally:
            v4.JUNCTION = old

    def test_complex_target_blocks_the_join(self):
        # A -P-> B is a record whose target is the complex B_X (B is not alone); B -T-> C has B alone.
        edges = [("A", "B", 1, "P", True, False), ("B", "C", 1, "T", True, True)]
        self.assertEqual(self.influence_at_a(edges, True), 0.0)
        self.assertGreater(abs(self.influence_at_a(edges, False)), 0.0)          # inverse: filter off restores the v3 behaviour

    def test_complex_source_blocks_the_join(self):
        edges = [("A", "B", 1, "P", True, True), ("B", "C", 1, "T", False, True)]    # B -T-> C only from a complex record B_Y
        self.assertEqual(self.influence_at_a(edges, True), 0.0)
        self.assertGreater(abs(self.influence_at_a(edges, False)), 0.0)

    def test_singleton_junction_is_unchanged(self):
        edges = [("A", "B", 1, "P", True, True), ("B", "C", 1, "T", True, True)]
        self.assertEqual(self.influence_at_a(edges, True), self.influence_at_a(edges, False))
        self.assertGreater(abs(self.influence_at_a(edges, True)), 0.0)

    def test_ends_are_not_constrained(self):
        # a compound target inside a complex source record and a seed inside a complex target are allowed (one-edge chain, no junction)
        edges = [("B", "C", 1, "T", False, False)]
        self.assertGreater(abs(self.influence_at_a([("A", "C", 1, "T", False, False)], True)), 0.0)

    def test_junction_off_equals_v3_on_a_toy_graph(self):
        edges4 = [("A", "B", 1, "P", True, False), ("B", "C", 1, "T", False, True), ("A", "C", -1, "T", True, True), ("D", "A", 1, "P", True, True)]
        g4 = v4.Graph4(edges4, extras=[]); g3 = v4.m3.Graph3([e[:4] for e in edges4], extras=[])
        g4.level = g3.level = "expression"
        S = np.zeros((1, g4.N)); S[0, g4.idx["C"]] = 1.0
        old = v4.JUNCTION; v4.JUNCTION = False
        try:
            self.assertTrue(np.allclose(g4.influence_ind(S), g3.influence_ind(S)))
        finally:
            v4.JUNCTION = old

    def test_dimethyl_fumarate_chain_on_the_real_network(self):
        """IT9 P4c-d dropped KEAP1 -P-> RBX1 -P-> NFKBIB -T-> TNF because RBX1 joins two different E3 ligases; the rule now removes the chain itself."""
        g = v4.Graph4(v4.read_edges4(), extras=[]); g.level = "expression"
        v4.JUNCTION = False
        try:
            self.assertIn("RBX1", g.best_chain("KEAP1", "TNF") or "")
        finally:
            v4.JUNCTION = True
        ch = g.best_chain("KEAP1", "TNF")
        self.assertTrue(ch is None or "RBX1" not in ch, ch)

    def test_best_chain_junction_in_chain_text(self):
        g = v4.Graph4(v4.read_edges4(), extras=[]); g.level = "expression"
        self.assertIn("HIF1A", g.best_chain("HIF1A", "BNIP3") or "")                   # one-edge chain: the start may be a complex member
        ch = g.best_chain("XIAP", "BNIP3")
        self.assertTrue(ch is None or "HIF1A -P" in ch or "XIAP -P(+)-> HIF1A" not in ch, ch)   # XIAP -> HIF1A -> BNIP3 needs HIF1A alone as a source: absent


class RoleDispositions(unittest.TestCase):
    unknown = dict(role_status="unknown", role_basis="NONE", leaning="none")

    def test_unknown_role_keeps_both_arms_conditional(self):
        self.assertEqual(dz.disposition("opposes", self.unknown), ("H_HARM", "CONDITIONAL_IF_HARMFUL"))
        self.assertEqual(dz.disposition("mimics", self.unknown), ("H_PROTECT", "CONDITIONAL_IF_PROTECTIVE"))

    def test_source_stated_role_withdraws_the_other_arm(self):
        h = dict(role_status="harmful", role_basis="SOURCE_STATED", leaning="harmful")
        self.assertEqual(dz.disposition("mimics", h)[1], "WITHDRAWN_DISEASE_DIRECTION_CONTROL")
        p = dict(role_status="protective", role_basis="SOURCE_STATED", leaning="protective")
        self.assertEqual(dz.disposition("opposes", p)[1], "WITHDRAWN_OPPOSES_PROTECTIVE_RISK")
        self.assertEqual(dz.disposition("mimics", p)[1], "PRIMARY_SUPPORT")

    def test_a_leaning_orders_but_never_withdraws(self):
        lean = dict(role_status="unknown", role_basis="NONE", leaning="harmful")
        self.assertIn("leaning-first", dz.disposition("opposes", lean)[1])
        self.assertTrue(dz.disposition("mimics", lean)[1].startswith("CONDITIONAL_IF_PROTECTIVE"))
        self.assertNotIn("WITHDRAWN", dz.disposition("mimics", lean)[1])

    def test_composition_role_holds_both_arms(self):
        c = dict(role_status="composition", role_basis="NONE", leaning="none")
        self.assertEqual(dz.disposition("opposes", c)[1], "HELD_UNTIL_COMPOSITION_RESOLVED")
        self.assertEqual(dz.disposition("mimics", c)[1], "HELD_UNTIL_COMPOSITION_RESOLVED")

    def test_a_harmful_role_without_a_source_is_refused(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "roles.tsv"
            p.write_text("question_id\trole_status\trole_basis\tleaning\nQ9\tharmful\tNONE\tharmful\n")
            with self.assertRaises(SystemExit):
                dz.load_roles(p)

    def test_committed_roles_are_valid_and_cover_every_question(self):
        r = dz.load_roles(HERE / "question_roles.tsv")
        self.assertEqual(set(r), {f"Q{i}" for i in range(1, 8)})
        self.assertTrue(all(v["role_status"] != "harmful" for v in r.values()))     # no committed role is asserted without a source yet


class Origins(unittest.TestCase):
    seeds = None

    @classmethod
    def setUpClass(cls):
        cls.seeds = {r["seed_id"]: r for r in dz.rd(DR / "generation_it9_p1_20261030" / "seeds.tsv")}

    def test_the_two_human_deposits_fold_to_one_origin(self):
        keys = {dz.canonical_origin(self.seeds[s])[0] for s in ("S017", "S018", "S019", "S020", "S021")}
        self.assertEqual(len(keys), 1)

    def test_same_article_other_level_is_another_origin(self):
        # S100 (MYC expression) and S101 (MYC protein) are one article at two readout levels: two origins, not one (no PMID-only deduplication)
        self.assertNotEqual(dz.canonical_origin(self.seeds["S100"])[0], dz.canonical_origin(self.seeds["S101"])[0])

    def test_unreconstructable_origin_stays_its_own_and_is_flagged(self):
        fake = dict(seed_id="SX1", source_locator="", context="", level="expression")
        self.assertEqual(dz.canonical_origin(fake), ("SEED:SX1", False))


class PhenotypeFirst(unittest.TestCase):
    def test_phenotype_leads_enter_without_a_graph_row(self):
        v3 = DR / "generation_it9_p2_20261030" / "v3" / "results"
        pf = {r["intervention"].split(",")[0].split(" (")[0]: r for r in dz.phenotype_first(v3, DR, None)}
        self.assertTrue(pf["Ethosuximide"]["graph_status"].startswith("NO_GRAPH_ROW"))
        self.assertTrue(pf["Lithium"]["graph_status"].startswith("NO_GRAPH_ROW"))
        self.assertEqual(pf["Ethosuximide"]["entry"], "PHENOTYPE_FIRST")

    def test_curated_extra_enters_regardless_of_the_graph(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "x.tsv"
            p.write_text("intervention\treadout\tgraph_status\nFixture compound\tfunctional recovery in a WWOX system\tNO_GRAPH_ROW\n")
            v3 = DR / "generation_it9_p2_20261030" / "v3" / "results"
            names = [r["intervention"] for r in dz.phenotype_first(v3, DR, p)]
        self.assertIn("Fixture compound", names)


class ExposureVersusProbe(unittest.TestCase):
    def test_systemic_limit_does_not_remove_the_ex_vivo_probe(self):
        dev = dz.rd(HERE / "dev_constraints.tsv")
        s = dz.dev_scope("Roxadustat", dev)
        self.assertIn("systemic_development_limited", s)
        self.assertIn("ex_vivo_probe_eligible", s)

    def test_a_probe_level_block_is_visible(self):
        dev = [dict(compound="Fixturedrug", scope="probe_specificity", affects_ex_vivo_probe="no")]
        self.assertIn("ex_vivo_probe_blocked", dz.dev_scope("Fixturedrug", dev))


class ThreeProtectedRegressions(unittest.TestCase):
    def test_ranking_pilot_fixtures_still_pass(self):
        r = subprocess.run([sys.executable, "-B", str(DR / "ranking_it8_p9_20261029" / "test_ranking_it8.py"), "-k", "pilot", "-k", "duplicate", "-k", "transfer", "-k", "unknown"],
                           capture_output=True, text=True, cwd=str(DR))
        self.assertEqual(r.returncode, 0, r.stderr[-800:])


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]], verbosity=1)
