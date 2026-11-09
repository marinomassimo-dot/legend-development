#!/usr/bin/env python3
"""Regressions for framework/scripts/hypothesis_package.py (the reader that carries physiological hypotheses to a consumer).

Pinned: rows are carried verbatim and none is lost; rivals, experiments and matrix columns are reached by literal
ids only; a link that needs interpretation is a committed row validated against real ids; a physiological
hypothesis is never a gene arc; a missing link or experiment is UNLINKED / NO_EXPERIMENT, not evidence against;
a CARRIED_IN_TEXT claim fails when the text it names is gone; the reader writes nothing.
"""
from __future__ import annotations

import copy
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hypothesis_package as hp  # noqa: E402


def _digest(root: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(root.rglob("*")):
        if f.is_file():
            h.update(f.read_bytes())
    return h.hexdigest()


class Committed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pkgs = hp.load_all()

    def rec(self, inv):
        return hp.record_for(self.pkgs, inv)

    def test_committed_links_validate(self):
        self.assertEqual([e for p in self.pkgs for e in hp.validate(p)], [])

    def test_every_hypothesis_is_linked_and_verbatim(self):
        for p in self.pkgs:
            linked = {l["hyp_id"] for l in p["links"]}
            self.assertEqual(linked, set(p["hyps"]), "a hypothesis with no link row would be silently dropped")
        got = {h["hyp_id"]: h for i in ("INV-05", "INV-18") for h in self.rec(i)["hypotheses"]}
        for p in self.pkgs:
            for hid, row in p["hyps"].items():
                self.assertEqual(got[hid]["hypothesis"], row)

    def test_experiments_are_not_lost(self):
        # independent count: an experiment belongs to a hypothesis when its cell names the id as a whole word
        import re
        for p in self.pkgs:
            for hid in p["hyps"]:
                want = sorted(e for e, r in p["exps"].items() if re.search(rf"\b{hid}\b", r["hypothesis"]))
                inv = next(l["inv_id"] for l in p["links"] if l["hyp_id"] == hid)
                h = next(x for x in self.rec(inv)["hypotheses"] if x["hyp_id"] == hid)
                self.assertEqual(sorted(e["row"]["exp_id"] for e in h["experiments"]), want)

    def test_physiological_without_gene_pair(self):
        for h in self.rec("INV-18")["hypotheses"]:
            self.assertIs(h["gene_arc"], False)
            self.assertEqual(h["kind"], "physiological_hypothesis")
            self.assertFalse([k for k in h if "hgnc" in k.lower() or k in ("gene_a", "gene_b", "relation")])
        mh1 = next(h for h in self.rec("INV-18")["hypotheses"] if h["hyp_id"] == "MH1")
        self.assertTrue({"A04", "A05", "A06"} <= {a["alt_id"] for a in mh1["alternatives"]})

    def test_ampa_nmda_keeps_rivals_and_matrix(self):
        bh2 = next(h for h in self.rec("INV-05")["hypotheses"] if h["hyp_id"] == "BH2")
        self.assertTrue({"AB04", "AB05"} <= {a["alt_id"] for a in bh2["alternatives"]})
        arms = {a["arm_id"] for e in bh2["experiments"] for a in e["arms"]}
        self.assertTrue({"M04", "M05", "M06"} <= arms)
        a = next(x for e in bh2["experiments"] for x in e["arms"] if x["arm_id"] == "M05")
        self.assertIn("INFERENZA", a["prediction_label"])  # the label that says no cell is a measured result survives

    def test_unresolved_rival_link_is_reported_not_guessed(self):
        # BH1 cites no alternative id in any cell; its rivals are matrix columns only. The reader must not map them.
        bh1 = next(h for h in self.rec("INV-05")["hypotheses"] if h["hyp_id"] == "BH1")
        self.assertEqual(bh1["alternatives"], [])
        self.assertIn("H1_AMPA_dependent_drive", bh1["matrix_columns_cited"].values())

    def test_carried_case_stays_carried(self):
        for inv, hid in (("INV-18", "MH2"), ("INV-05", "BH2")):
            h = next(x for x in self.rec(inv)["hypotheses"] if x["hyp_id"] == hid)
            self.assertEqual(h["link_state"], "CARRIED_IN_TEXT")

    def test_absent_link_is_unlinked_not_negative(self):
        r = self.rec("INV-01")
        self.assertEqual((r["state"], r["hypotheses"]), ("UNLINKED", []))
        self.assertIn("not evidence against", hp._brief(r))

    def test_reader_writes_nothing(self):
        before = _digest(hp.DR)
        hp.record_for(self.pkgs, "INV-05")
        hp.main(["check"])
        self.assertEqual(before, _digest(hp.DR))


class Synthetic(unittest.TestCase):
    def pkg(self, tmp: Path, links: str, exps: str = "exp_id\thypothesis\tcomparison_arms\nE1\tX1\tnone\n") -> dict:
        o = tmp / "p" / "output"
        o.mkdir(parents=True)
        (o / "hypotheses.tsv").write_text("hyp_id\tstatus\tchain\tcompeting_explanation\tcounter_evidence\tweakening_result\tdiscriminating_experiment\twhat_would_change_the_decision\nX1\ts\tc\tA01 and Q9\t\t\t\t\nX2\ts\tc\t\t\t\t\t\n")
        (o / "alternatives.tsv").write_text("alt_id\texplanation\nA01\trival\n")
        (o / "experiments.tsv").write_text(exps)
        (o / "consumer_links.tsv").write_text(links)
        return hp.load_package(tmp / "p")

    L = "hyp_id\tkind\tneed_id\tinv_id\tcard_ids\tlink_state\tcarried_check\tsource\n"
    INVS = {"INV-9": {"next_test": "a d-APV arm", "intervention": "tool"}}

    def test_missing_experiment_is_no_experiment(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.pkg(Path(t), self.L + "X2\tphysiological_hypothesis\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n")
            h = hp.record_for([p], "INV-9")["hypotheses"][0]
            self.assertEqual((h["experiment_state"], h["experiments"]), ("NO_EXPERIMENT", []))

    def test_unknown_token_is_unresolved(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.pkg(Path(t), self.L + "X1\tphysiological_hypothesis\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n")
            h = hp.record_for([p], "INV-9")["hypotheses"][0]
            self.assertEqual([a["alt_id"] for a in h["alternatives"]], ["A01"])
            self.assertEqual(h["unresolved_refs"], ["Q9"])

    def test_validation_refuses_bad_rows(self):
        bad = ("X9\tphysiological_hypothesis\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n"      # unknown hypothesis
               "X1\tgene_bridge\tN1\tINV-9\t\tPROPOSED_NOT_APPLIED\t\ts\n"                       # not a physiological hypothesis
               "X1\tphysiological_hypothesis\tNOPE\tINV-0\tNOCARD\tAPPLIED\t\ts\n"               # need, inv, card, state
               "X1\tphysiological_hypothesis\tN1\tINV-9\t\tCARRIED_IN_TEXT\t\ts\n"               # no check
               "X1\tphysiological_hypothesis\tN1\tINV-9\t\tCARRIED_IN_TEXT\tnext_test:gone\ts\n")  # check not in text
        with tempfile.TemporaryDirectory() as t:
            errs = hp.validate(self.pkg(Path(t), self.L + bad), needs={"N1"}, invs=self.INVS, cards=Path(t))
        for frag in ("hypothesis id not in", "kind 'gene_bridge'", "need 'NOPE'", "investigation 'INV-0'", "card 'NOCARD'",
                     "link_state 'APPLIED'", "without a carried_check", "carried_check 'next_test:gone'"):
            self.assertTrue(any(frag in e for e in errs), frag)

    def test_good_carried_row_passes(self):
        with tempfile.TemporaryDirectory() as t:
            p = self.pkg(Path(t), self.L + "X1\tphysiological_hypothesis\tN1\tINV-9\t\tCARRIED_IN_TEXT\tnext_test:d-APV\ts\n")
            self.assertEqual(hp.validate(p, needs={"N1"}, invs=self.INVS, cards=Path(t)), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
