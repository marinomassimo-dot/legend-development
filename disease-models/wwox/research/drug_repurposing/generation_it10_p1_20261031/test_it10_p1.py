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
        # two-edge chain A -P-> B -T-> C: A sits inside a complex source record and C inside a complex target record; only B is the junction
        edges = [("A", "B", 1, "P", False, True), ("B", "C", 1, "T", True, False)]
        self.assertGreater(abs(self.influence_at_a(edges, True)), 0.0)

    def test_one_edge_chain_from_a_complex_source_is_kept(self):
        self.assertGreater(abs(self.influence_at_a([("A", "C", 1, "T", False, False)], True)), 0.0)      # compound target inside ARNT_HIF1A-type record

    def test_three_edge_chain_checks_every_junction(self):
        ok = [("A", "B", 1, "P", True, True), ("B", "C", 1, "P", True, True), ("C", "D", 1, "T", True, True)]
        bad2 = [("A", "B", 1, "P", True, True), ("B", "C", 1, "P", True, False), ("C", "D", 1, "T", True, True)]     # B -> C ends in a complex: second junction fails
        for e, expect in ((ok, True), (bad2, False)):
            g = v4.Graph4(e, extras=[]); g.level = "expression"
            S = np.zeros((1, g.N)); S[0, g.idx["D"]] = 1.0
            self.assertEqual(abs(float(g.influence_ind(S, hops=3)[0, g.idx["A"]])) > 0, expect)

    def test_protein_level_uses_the_same_rule(self):
        e = [("A", "B", 1, "P", True, False), ("B", "C", 1, "P", True, True)]       # protein seed C: chain P P, junction B must be alone in A -> B
        g = v4.Graph4(e, extras=[]); g.level = "protein"
        S = np.zeros((1, g.N)); S[0, g.idx["C"]] = 1.0
        self.assertEqual(float(g.influence_ind(S)[0, g.idx["A"]]), 0.0)
        old = v4.JUNCTION; v4.JUNCTION = False
        try:
            self.assertNotEqual(float(g.influence_ind(S)[0, g.idx["A"]]), 0.0)
        finally:
            v4.JUNCTION = old

    def test_with_signs_rebuilds_the_junction_arrays(self):
        e = [("A", "B", 1, "P", True, True), ("B", "C", 1, "T", True, True)]
        g = v4.Graph4(e, extras=[]); g.level = "expression"
        S = np.zeros((1, g.N)); S[0, g.idx["C"]] = 1.0
        flipped = g.with_signs(-g.sg0)
        self.assertAlmostEqual(float(flipped.influence_ind(S)[0, g.idx["A"]]), float(g.influence_ind(S)[0, g.idx["A"]]))   # two flipped edges: sign product unchanged
        one = g.with_signs(np.array([1.0, -1.0]))
        self.assertAlmostEqual(float(one.influence_ind(S)[0, g.idx["A"]]), -float(g.influence_ind(S)[0, g.idx["A"]]))
        self.assertIsInstance(one, v4.Graph4)

    def test_flag_aggregation_is_any_record(self):
        import gzip, tempfile
        with tempfile.TemporaryDirectory() as d:
            hdr = "source_symbol\ttarget_symbol\tsign\ttype\tsources\n"
            with gzip.open(Path(d) / "signor_omnipath_edges.tsv.gz", "wt") as fh:
                fh.write(hdr + "QQA1\tQQB1_QQX1\t1\tpost_translational\tSIGNOR\nQQA1\tQQB1\t1\tpost_translational\tSIGNOR\nQQB1_QQY1\tQQC1\t1\ttranscriptional\tSIGNOR\n")
            with gzip.open(Path(d) / "collectri_omnipath_edges.tsv.gz", "wt") as fh:
                fh.write(hdr)
            E = {(e[0], e[1], e[3]): (e[4], e[5]) for e in v4.read_edges4(d)}
        self.assertTrue(E[("QQA1", "QQB1", "P")][1])          # one of two records names B alone as target: junction-capable
        self.assertFalse(E[("QQB1", "QQC1", "T")][0])         # B appears only inside the complex B_Y as a source: not junction-capable

    def test_best_chain_agrees_with_influence_on_a_toy(self):
        e = [("A", "B", 1, "P", True, False), ("B", "C", 1, "T", True, True), ("A", "D", 1, "P", True, True), ("D", "C", -1, "T", True, True)]
        g = v4.Graph4(e, extras=[]); g.level = "expression"
        ch = g.best_chain("A", "C")
        self.assertIn("A -P(+)-> D", ch)
        self.assertNotIn("-> B", ch)
        S = np.zeros((1, g.N)); S[0, g.idx["C"]] = 1.0
        self.assertLess(float(g.influence_ind(S)[0, g.idx["A"]]), 0.0)              # only the D route (negative) contributes

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
        self.assertIn("HIF1A -T", g.best_chain("HIF1A", "BNIP3") or "")                  # one-edge chain: the start may be a complex member
        ch = g.best_chain("XIAP", "BNIP3")
        self.assertTrue(ch is None or "XIAP -P(+)-> HIF1A" not in ch, ch)                # XIAP -> HIF1A -> BNIP3 needs HIF1A alone as a source: absent for BNIP3


class ExplainsTheCalculation(unittest.TestCase):
    """P1.1: the shown chain is ONE walk of the strongest seed; the score is a signed sum over seeds and over every admissible walk."""

    def test_walk_sum_equals_influence_on_a_toy_with_two_routes(self):
        e = [("T", "B", 1, "P", True, True), ("T", "C", 1, "P", True, True), ("B", "S", 1, "T", True, True), ("C", "S", -1, "T", True, True), ("T", "S", 1, "T", True, True)]
        g = v4.Graph4(e, extras=[]); g.level = "expression"
        S = np.zeros((1, g.N)); S[0, g.idx["S"]] = 1.0
        w = g.walks("T", "S")
        self.assertEqual(len(w), 3)
        self.assertAlmostEqual(sum(v for _, v in w), float(g.influence_ind(S)[0, g.idx["T"]]))
        n, best, opp = v4.walk_summary(w)
        self.assertEqual(n, 3)
        self.assertGreater(opp, 0.0)                                  # one route opposes the net: the single strongest walk would hide it

    def test_walk_sum_equals_influence_on_real_pairs_at_both_levels(self):
        for lvl, pairs in (("expression", [("PPP3CA", "TNF"), ("BRD4", "TNF"), ("NFE2L2", "IL1B")]), ("protein", [("METTL3", "MYC"), ("AURKB", "MYC")])):
            g = v4.Graph4(v4.read_edges4(), extras=[]); g.level = lvl
            for t, s_ in pairs:
                S = np.zeros((1, g.N)); S[0, g.idx[s_]] = 1.0
                self.assertAlmostEqual(sum(v for _, v in g.walks(t, s_)), float(g.influence_ind(S)[0, g.idx[t]]), places=9, msg=f"{lvl} {t}->{s_}")

    def test_the_walk_decomposition_respects_the_junction_rule(self):
        e = [("A", "B", 1, "P", True, False), ("B", "C", 1, "T", True, True)]
        g = v4.Graph4(e, extras=[]); g.level = "expression"
        self.assertEqual(g.walks("A", "C"), [])
        old = v4.JUNCTION; v4.JUNCTION = False
        try:
            self.assertEqual(len(g.walks("A", "C")), 1)
        finally:
            v4.JUNCTION = old

    def contrib(self, vals):
        return [dict(contrib_total=str(v), main_target_hops1to3="", main_target_hop0="", contrib_hops1to3="0", gene="G%d" % i) for i, v in enumerate(vals)]

    def test_one_dominant_seed_is_a_dominant_chain(self):
        self.assertEqual(dz.explain_columns(self.contrib([1.0, 0.01]), "expression")[0], "DOMINANT_CHAIN")

    def test_many_equal_seeds_make_the_shown_chain_a_partial_example(self):
        note = dz.explain_columns(self.contrib([0.1] * 6), "expression")[0]
        self.assertTrue(note.startswith("PARTIAL_EXAMPLE"), note)
        self.assertIn("17%", note)

    def test_contrary_contributions_are_reported(self):
        note, top, contrary = dz.explain_columns(self.contrib([1.0, -0.3]), "expression")[:3]
        self.assertTrue(note.startswith("PARTIAL_EXAMPLE"))
        self.assertAlmostEqual(float(contrary), 0.3 / 1.3, places=3)

    def test_px478_row_names_what_the_chain_does_not_show(self):
        rows = {r["name"]: r for r in dz.rd(HERE / "results" / "dispositions_Q2.tsv") if r["arm"] == "opposes"}
        self.assertTrue(rows["Px-478"]["chain_note"].startswith("PARTIAL_EXAMPLE"))     # 15 seed rows, the strongest carries about a tenth


class SelftestCommand(unittest.TestCase):
    """P1.4: the generator's selftest failed on 3-tuple toy edges (fixture incompatibility with the typed Graph3; not a production regression). It now runs on a typed toy graph."""

    def run_selftest(self, script, *extra):
        return subprocess.run([sys.executable, "-B", str(script), "selftest", *extra], capture_output=True, text=True)

    def test_v3_and_v4_selftest_pass(self):
        for script in (DR / "generation_it9_p2_20261030" / "v3" / "seed_engine_v3.py", HERE / "engine_v4" / "seed_engine_v4.py"):
            r = self.run_selftest(script)
            self.assertEqual(r.returncode, 0, r.stdout[-300:] + r.stderr[-300:])
            self.assertIn("selftest PASS", r.stdout)

    def test_the_selftest_fails_when_edge_typing_is_switched_off(self):
        r = self.run_selftest(HERE / "engine_v4" / "seed_engine_v4.py", "--mode", "all")
        self.assertNotEqual(r.returncode, 0)                  # the P-edge-into-an-expression-seed and T-first controls then score, so the typing controls are not vacuous


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

    def test_any_stated_role_without_a_source_is_refused(self):
        for status in ("harmful", "protective", "composition", "mixed"):
            with tempfile.TemporaryDirectory() as d:
                p = Path(d) / "roles.tsv"
                p.write_text(f"question_id\trole_status\trole_basis\tleaning\trole_source\nQ9\t{status}\tNONE\tnone\t\n")
                with self.assertRaises(SystemExit, msg=status):
                    dz.load_roles(p)
        with tempfile.TemporaryDirectory() as d:                      # SOURCE_STATED without a locator is refused too
            p = Path(d) / "roles.tsv"
            p.write_text("question_id\trole_status\trole_basis\tleaning\trole_source\nQ9\tharmful\tSOURCE_STATED\tharmful\t\n")
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

    def test_a_seed_citing_two_articles_carries_two_origins(self):
        keys = {k for k, _ in dz.canonical_origins(self.seeds["S085"])}
        self.assertEqual(keys, {"PMID:30290271|expression", "PMID:36828035|expression"})

    def test_a_non_significant_observation_is_not_an_origin(self):
        self.assertEqual({k for k, _ in dz.canonical_origins_checked(self.seeds["S085"])}, {"PMID:36828035|expression"})
        self.assertEqual({k for k, _ in dz.canonical_origins_checked(self.seeds["S086"])}, {"PMID:30290271|expression"})

    def test_hnpc_and_organoid_locators_fold_in_any_letter_case(self):
        self.assertEqual({dz.canonical_origins(self.seeds[s])[0][0] for s in ("S040", "S044", "S017")}, {"DEPOSITS:GSE156243+GSE126075(+neurons)"})

    def test_unreconstructable_origin_stays_its_own_and_is_flagged(self):
        fake = dict(seed_id="SX1", source_locator="", context="", level="expression")
        self.assertEqual(dz.canonical_origins(fake), [("SEED:SX1", False)])


class PhenotypeFirst(unittest.TestCase):
    def test_phenotype_leads_enter_without_a_graph_row(self):
        v3 = DR / "generation_it9_p2_20261030" / "v3" / "results"
        pf = {r["intervention"].split(",")[0].split(" (")[0]: r for r in dz.phenotype_first(v3, DR, None)}
        self.assertTrue(pf["Ethosuximide"]["graph_status"].startswith("NO_GRAPH_ROW"))
        self.assertTrue(pf["Lithium"]["graph_status"].startswith("NAME_TWIN_SCORED_NOT_SPECIFIC"))     # salts are separate rows, scored, none seed-specific
        self.assertTrue(pf["d-APV"]["graph_status"].startswith("DIRECT_HIT_ZERO_SCORE"))                 # its own molecule, not memantine's score
        self.assertNotIn("SCORED_NOT_SPECIFIC", pf["Vigabatrin"]["graph_status"])
        self.assertEqual(pf["Ethosuximide"]["entry"], "PHENOTYPE_FIRST")

    def test_curated_extra_enters_regardless_of_the_graph(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "x.tsv"
            p.write_text("intervention\treadout\tgraph_status\nFixture compound\tfunctional recovery in a WWOX system\tNO_GRAPH_ROW\n")
            v3 = DR / "generation_it9_p2_20261030" / "v3" / "results"
            names = [r["intervention"] for r in dz.phenotype_first(v3, DR, p)]
        self.assertIn("Fixture compound", names)


class ExposureVersusProbe(unittest.TestCase):
    def test_systemic_limit_does_not_remove_the_ex_vivo_probe_but_the_confound_is_visible(self):
        dev = dz.rd(HERE / "dev_constraints.tsv")
        s = dz.dev_scope("Roxadustat", dev)
        self.assertIn("systemic_development_limited", s)
        self.assertIn("ex_vivo_probe_with_confound(probe_specificity)", s)          # usable as a probe, with the thyromimetic confound stated
        self.assertNotIn("blocked", s)

    def test_a_clean_systemic_limit_leaves_the_probe_eligible(self):
        dev = [dict(compound="Fixturedrug", scope="systemic_development", affects_ex_vivo_probe="no")]
        s = dz.dev_scope("Fixturedrug", dev)
        self.assertEqual(s, "systemic_development_limited;ex_vivo_probe_eligible")

    def test_a_probe_level_confound_is_never_reported_as_eligible(self):
        dev = [dict(compound="Fixturedrug", scope="probe_specificity", affects_ex_vivo_probe="yes")]
        self.assertNotIn("ex_vivo_probe_eligible", dz.dev_scope("Fixturedrug", dev))


class ThreeProtectedRegressions(unittest.TestCase):
    def test_ranking_pilot_fixtures_still_pass(self):
        r = subprocess.run([sys.executable, "-B", str(DR / "ranking_it8_p9_20261029" / "test_ranking_it8.py"), "-k", "pilot", "-k", "duplicate", "-k", "transfer", "-k", "unknown"],
                           capture_output=True, text=True, cwd=str(DR))
        self.assertEqual(r.returncode, 0, r.stderr[-800:])


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]], verbosity=1)
