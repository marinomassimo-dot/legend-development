#!/usr/bin/env python3
"""Tests for IT21 P5 (decoy arm, decision rule, committed tables). Standard library plus the repository's own modules; no network.

  test_p5_it21.py            run all
"""
import sys
if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, importlib.util, json, re, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
RES = HERE / "results"


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec)
    saved, sys.argv = sys.argv, [name, "run"]
    sys.modules[name] = m
    try:
        spec.loader.exec_module(m)
    finally:
        sys.argv = saved
    return m


CA = load("compare_arms")
DA = load("decoy_arm")


def rd(p):
    with (gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


class DecisionRule(unittest.TestCase):
    def test_truth_table(self):
        self.assertEqual(CA.decide(True, True, True, False), "informative addition")
        self.assertEqual(CA.decide(True, True, False, True), "informative addition")
        self.assertEqual(CA.decide(True, True, False, False), "inconclusive")
        self.assertEqual(CA.decide(True, False, True, True), "inconclusive")
        self.assertEqual(CA.decide(False, True, True, True), "inconclusive")
        self.assertEqual(CA.decide(False, False, True, True), "no advantage")
        self.assertEqual(CA.decide(False, False, False, False), "no advantage")

    def test_upper_p_add_one(self):
        self.assertAlmostEqual(CA.upper_p(10, [1, 2, 3, 4]), 1 / 5)
        self.assertAlmostEqual(CA.upper_p(0, [1, 2, 3, 4]), 1.0)
        self.assertAlmostEqual(CA.upper_p(2, [1, 2, 3, 4]), 4 / 5)

    def test_percentile(self):
        self.assertEqual(CA.pct([1, 2, 3, 4, 5], 0.5), 3)
        self.assertEqual(CA.pct([1, 2, 3, 4, 5], 0.95), 4.8)
        self.assertIsNone(CA.pct([], 0.5))

    def test_sets_above_toy(self):
        real = {sn: {"m": 10} for sn in CA.SETS}
        dec = {(sn, v): [{"m": i} for i in range(5)] for sn in CA.SETS for v in CA.FINE}
        n, detail = CA.sets_above(real, dec, "m", CA.FINE)
        self.assertEqual(n, len(CA.SETS))
        real["Q2_expression_tiersAB"]["m"] = 2
        n, _ = CA.sets_above(real, dec, "m", CA.FINE)
        self.assertEqual(n, len(CA.SETS) - 1)

    def test_capped_handover(self):
        self.assertEqual(CA.capped({("Q5", "H_HARM"): {"a", "b", "c", "d"}, ("Q5", "H_PROTECT"): {"a"}}), 4)


class DecoyConstruction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fac = DA.DecoyFactory()

    def rows(self, sn):
        return DA.read_tsv(DA.SEEDS / f"{sn}.tsv")

    def test_deterministic(self):
        r = self.rows("Q5_expression_tiersAB")
        a, ga = self.fac.decoy_rows(r, 7, "deg")
        b, gb = self.fac.decoy_rows(r, 7, "deg")
        self.assertEqual(ga, gb)
        self.assertNotEqual(ga, self.fac.decoy_rows(r, 8, "deg")[1])

    def test_everything_but_the_gene_is_kept(self):
        r = self.rows("Q5_expression_tiersAB")
        for v in DA.VARIANTS:
            new, genes = self.fac.decoy_rows(r, 3, v)
            self.assertEqual(len(new), len(r))
            for o, n in zip(r, new):
                for col in ("direction", "level", "direction_status", "readout_level", "evidence_class", "species", "guard_tag"):
                    self.assertEqual(o[col], n[col], (v, col))
            self.assertFalse(set(genes) & {x["gene"] for x in r}, "a decoy must not contain a real seed gene")

    def test_coarse_decoy_is_in_the_same_degree_decile(self):
        r = self.rows("Q4_expression_tiersAB")
        new, genes = self.fac.decoy_rows(r, 5, "coarse")
        real_genes = [x["gene"] for x in r if self.fac.unit_bin(x["gene"]) is not None]
        self.assertEqual([self.fac.unit_bin(g) for g in genes], [self.fac.unit_bin(g) for g in real_genes])

    def test_fine_decoy_degree_is_close(self):
        r = self.rows("Q6_expression_tiersAB")
        j = self.fac.G.idx[self.fac.canon("MYC")]
        for k in range(1, 6):
            _, genes = self.fac.decoy_rows(r, k, "deg")
            jd = self.fac.G.idx[genes[0]]
            rank = abs(self.fac.deg - self.fac.deg[j]).argsort().tolist().index(jd)
            self.assertLessEqual(rank, DA.NEAREST + 1)

    def test_off_graph_seed_gene_is_omitted(self):
        r = self.rows("Q4_expression_tiersAB")
        self.assertIsNone(self.fac.unit_bin("KCNA2"))
        new, genes = self.fac.decoy_rows(r, 1, "coarse")
        self.assertEqual(len(new), 3)

    def test_process_seed_keeps_member_count(self):
        r = self.rows("Q2_expression_tiersAB")
        new, _ = self.fac.decoy_rows(r, 2, "coarse")
        proc_o = [x for x in r if x["kind"] == "process"][0]
        proc_n = [x for x in new if x["kind"] == "process"][0]
        self.assertEqual(len(proc_o["members"].split(";")), len(proc_n["members"].split(";")))
        self.assertNotEqual(proc_o["members"], proc_n["members"])


@unittest.skipUnless((RES / "summary_p5.json").exists(), "results not built")
class CommittedResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.S = json.loads((RES / "summary_p5.json").read_text())

    def test_control_reproduces_p2(self):
        c = self.S["control"]
        self.assertEqual(c["pooled_by_question_like_P2"], dict(eligible=141, clusters=32, capped=13))
        self.assertEqual(c["real_spec_rows"], {"Q2_expression_tiersAB": 51, "Q4_expression_tiersAB": 87, "Q5_expression_tiersAB": 286,
                                               "Q6_expression_tiersAB": 420, "Q6_protein_tiersAB": 148})

    def test_decoy_file_replicate_zero_equals_p2_list(self):
        ref = {}
        for r in rd(HERE.parent / "generation_it21_p2_20261103" / "results" / "engine" / "v3_seed_specific_all_nulls.tsv"):
            ref.setdefault(r["seed_set"], set()).add((r["family_id"], r["arm"]))
        mine = {}
        for r in rd(RES / "decoy_rows.tsv.gz"):
            if r["rep"] == "0":
                mine.setdefault(r["seed_set"], set()).add((r["family_id"], "opposes" if r["sign"] == "1" else "mimics"))
        self.assertEqual(mine, ref)

    def test_decision_follows_the_rule(self):
        c = self.S["criteria"]
        self.assertEqual(self.S["decision"], CA.decide(c["C1"], c["C2"], c["C3"], c["C4"]))

    def test_every_decoy_design_has_the_nominal_replicates(self):
        k = self.S["k_decoys_per_design"]
        rows = rd(RES / "per_replicate_p5.tsv")
        for sn in CA.SETS:
            for v in CA.VARIANTS:
                self.assertEqual(len([r for r in rows if r["seed_set"] == sn and r["variant"] == v]), k, (sn, v))

    def test_readme_states_the_decision_first(self):
        txt = (HERE / "README.md").read_text(encoding="utf-8")
        head = txt[:2500].lower()
        self.assertIn(self.S["decision"], head)

    def test_nothing_is_called_qualified(self):
        for f in HERE.rglob("*.tsv"):
            t = f.read_text(encoding="utf-8")
            self.assertNotRegex(t, r"\bQUALIFIED_HYPOTHESIS\b(?!\s*0)", f.name) if f.name != "qualification_funnel_p5.tsv" else None

    def test_no_email_like_string(self):
        for f in list(HERE.glob("*.py")) + list(HERE.glob("*.md")) + list(RES.glob("*.tsv")) + list(RES.glob("*.json")):
            self.assertIsNone(re.search(r"[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}", f.read_text(encoding="utf-8")), f.name)


if __name__ == "__main__":
    unittest.main(verbosity=1)
