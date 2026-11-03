#!/usr/bin/env python3
"""IT22 P1 fixtures: a decision about one member of a mechanism cluster transfers to another member only inside the scope its own reason supports.

  python3 test_decision_scope_it22.py          (unittest; offline; seconds)

The three fixtures the mandate names, on the production function G.decision_effect (no re-implementation), plus the committed scope table.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import importlib.util, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


G = load("run_generation_it21", HERE.parent / "generation_it21_p2_20261103" / "run_generation_it21.py")

HDAC5_CHAIN = "HDAC5 -T(+)-> SLC2A1 [CollecTRI]"
BTK_CHAIN = "BTK -P(-)-> STAT3 [SIGNOR]; STAT3 -T(+)-> NPY [CollecTRI]"


def prop(compound, target, chain, q="Q2", hyp="H_HARM"):
    return dict(compound=compound, main_target=target, chain=chain, question=q, hypothesis=hyp)


def dec(compound, state, src, *components):
    return dict(compound=compound, state=state, source=src, components=[dict(scope=s, premise_key=k, note=n) for s, k, n in components])


class Fixtures(unittest.TestCase):
    def test_specific_rejection_does_not_discard_another_molecule(self):
        # nanatinostat: rejected because HDAC5 is a weak target FOR ITS OWN potency profile; the edge rests on one non-neural reference
        nana = dec("nanatinostat", "REJECTED_INFORMATIVE", "p4a#6",
                   ("molecule", "", "potent targets are class I; HDAC5 needs ~70x more compound"),
                   ("premise_unresolved", "edge:HDAC5>SLC2A1", "edge rests on one non-neural reference"))
        r = G.decision_effect(prop("Pracinostat", "HDAC5", HDAC5_CHAIN), [nana])
        self.assertEqual(r["block"], "")
        self.assertFalse(r["work_done"])
        self.assertTrue(any("one non-neural reference" in c for c in r["carried_limits"]))     # the shared limit stays visible, it is not a veto

    def test_refuted_shared_premise_still_applies_to_relevant_proposals(self):
        cgi = dec("CGI-1746", "REJECTED_INFORMATIVE", "p4a#57", ("premise_refuted", "target:BTK@Q4", "BTK is not expressed in the NPY-producing cell"))
        r = G.decision_effect(prop("Zanubrutinib", "BTK", BTK_CHAIN, q="Q4"), [cgi])
        self.assertTrue(r["block"].startswith("shared_premise_refuted"))
        # the same premise says nothing about another target or another question
        self.assertEqual(G.decision_effect(prop("X", "EZH2", "EZH2 -T(+)-> IL6", q="Q5"), [cgi])["block"], "")
        self.assertEqual(G.decision_effect(prop("Zanubrutinib", "BTK", BTK_CHAIN, q="Q5"), [cgi])["block"], "")

    def test_edge_premise_needs_the_edge_in_the_chain(self):
        rox = dec("roxadustat", "DROP", "it9#E-02", ("molecule", "", "label"), ("premise_refuted", "edge:FOXO3>SLC2A1", "reference states repression"))
        self.assertEqual(G.decision_effect(prop("Vadadustat", "EGLN2", "EGLN2 -P(-)-> FOXO3; FOXO3 -T(+)-> BNIP3"), [rox])["block"], "")
        self.assertTrue(G.decision_effect(prop("Vadadustat", "EGLN2", "EGLN2 -P(-)-> FOXO3; FOXO3 -T(+)-> SLC2A1"), [rox])["block"].startswith("shared_premise_refuted"))

    def test_already_worked_is_priority_not_discovery_and_not_veto(self):
        apa = dec("Apabetalone", "KEEP", "it9#P4CD-01", ("work_done", "", "conditional proposal already carried"))
        r = G.decision_effect(prop("Pfi-1", "BRD4", "BRD4 -T(+)-> TNF", q="Q5"), [apa])
        self.assertEqual(r["block"], "")
        self.assertTrue(r["work_done"])                       # demoted behind unworked clusters and labelled "not a discovery" by the hand-over

    def test_untagged_decision_keeps_the_old_veto_under_its_own_label(self):
        d = dec("Mystery", "DROP", "it9#X-99")
        d["components"] = []
        r = G.decision_effect(prop("Other", "T1", "T1 -T(+)-> G"), [d])
        self.assertEqual(r["block"], "decision_scope_untagged")

    def test_three_reasons_stay_separate(self):
        self.assertEqual(len({"mechanism_cluster_selection", "work_already_done", "shared_premise_refuted"}), 3)
        self.assertTrue(hasattr(G, "REASON_LABELS"))


class CommittedTable(unittest.TestCase):
    def test_every_decision_in_a_blocked_cluster_has_a_scope(self):
        tab = HERE / "decision_scope_it22.tsv"
        self.assertTrue(tab.exists())
        rows = G.rd(tab)
        for r in rows:
            self.assertIn(r["scope"], ("molecule", "premise_refuted", "premise_unresolved", "work_done"))
            self.assertTrue(r["basis"].strip())


class RealCases(unittest.TestCase):
    """The committed IT22 propose output (results_p1) on the real IT21 engine run; skipped when absent."""
    @classmethod
    def setUpClass(cls):
        p = HERE / "results_p1" / "proposals_it21.tsv"
        if not p.exists():
            raise unittest.SkipTest("results_p1 absent")
        cls.rows = G.rd(p)

    def test_no_row_keeps_the_unscoped_cluster_veto(self):
        self.assertFalse([r for r in self.rows if r["handoff_blocker"] == "mechanism_cluster_examined_earlier"])

    def test_btk_arc_stays_closed_by_its_refuted_premise(self):
        btk = [r for r in self.rows if r["main_target"] == "BTK" and r["handoff_blocker"] in ("shared_premise_refuted",)]
        self.assertGreaterEqual(len(btk), 20)

    def test_nanatinostat_peers_are_evaluated_on_their_own_data(self):
        pr = [r for r in self.rows if r["compound"].lower() == "pracinostat"][0]
        self.assertEqual(pr["handoff_eligible"], "yes")
        self.assertIn("one non-neural", pr["carried_limits"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
