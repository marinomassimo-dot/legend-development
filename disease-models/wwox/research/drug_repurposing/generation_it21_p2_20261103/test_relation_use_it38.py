#!/usr/bin/env python3
"""IT38: a qualified relation of a package reaches the proposals it concerns as a carried limit, with its status label, and never as a veto or an evidence of absence."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_generation_it21 as g  # noqa: E402

REL = {"subject": "MYC gain in tissue models", "relation": "gives_opposite_sign_to", "object": "WWOX-knockout organoid state", "context": "transfer", "status": "inferred", "evidence_id": "E11;E30"}
USE = {"inv_id": "INV-17", "relation_ids": "E11;E30", "use": "context_limit", "applies_chain": "", "applies_hypothesis": "", "relation": REL}
P = {"shared_premise_investigation": "INV-17", "chain": "X -P(+)-> MYC", "hypothesis": "H_PROTECT"}


class RelationUse(unittest.TestCase):
    def test_a_sign_contrast_is_a_context_limit_with_its_status_and_no_sign(self):
        lim, tags = g.relation_limits(P, [USE])
        self.assertEqual(len(lim), 1)
        self.assertIn("INFERRED (not measured)", lim[0])
        self.assertIn("gives no sign for another", lim[0])
        self.assertEqual(tags, ["E11;E30:context_limit"])

    def test_a_control_outside_the_investigation_is_unchanged(self):
        other = dict(P, shared_premise_investigation="INV-16", chain="HDAC5 -T(+)-> SLC2A1")
        self.assertEqual(g.relation_limits(other, [USE]), ([], []))
        self.assertEqual(g.relation_limits(dict(P, shared_premise_investigation=""), [USE]), ([], []))

    def test_the_hypothesis_filter_and_the_uninformative_wording(self):
        un = dict(USE, use="uninformative_not_negative", applies_hypothesis="^H_PROTECT$", relation=dict(REL, status="uninformative_other_disease", relation="uninformative_about"), relation_ids="E27")
        lim, _ = g.relation_limits(P, [un])
        self.assertIn("not carried as evidence against it", lim[0])
        self.assertIn("neither support nor refutation", lim[0])
        self.assertEqual(g.relation_limits(dict(P, hypothesis="H_HARM"), [un]), ([], []))

    def test_an_auditor_reading_is_labelled_exploratory_and_amount_is_kept_from_occupancy(self):
        au = dict(USE, use="occupancy_not_amount", relation=dict(REL, status="observed_auditor", relation="is_lost_in", evidence_id="E80"), relation_ids="E80")
        lim, _ = g.relation_limits(P, [au])
        self.assertIn("EXPLORATORY", lim[0])
        self.assertIn("kept apart", lim[0])
        self.assertIn("premise to verify, not a measurement", lim[0])

    def test_the_shipped_table_resolves_every_relation_to_exactly_one_row(self):
        uses = g.load_relation_uses()
        self.assertEqual(len(uses), 3)
        self.assertEqual({u["use"] for u in uses}, set(g.RELATION_USE_TEMPLATES))
        self.assertEqual(next(u for u in uses if u["relation_ids"] == "E80")["relation"]["status"], "observed_auditor")

    def test_a_missing_relation_is_an_error_not_a_silent_skip(self):
        import tempfile
        t = Path(tempfile.mkdtemp()) / "u.tsv"
        t.write_text("inv_id\trelations_file\trelation_ids\tuse\tapplies_chain\tapplies_hypothesis\nINV-17\tnb1_myc_20261107/output/generator_relations.tsv\tE999\tcontext_limit\t\t\n", encoding="utf-8")
        with self.assertRaises(SystemExit):
            g.load_relation_uses(t)


class PremiseTest(unittest.TestCase):
    """IT39: the measurement that resolves a premise travels with the proposal that rests on it (presentation of the qualification; selection is untouched)."""
    INV = {"INV-17": {"inv_id": "INV-17", "decisive_uncertainty": "whether the MYC rise is a driver", "next_test": "graded genetic MYC lowering in two windows"},
           "INV-99": {"inv_id": "INV-99", "decisive_uncertainty": "x", "next_test": ""}}

    def test_a_mapped_premise_brings_its_open_question_and_its_test(self):
        t = g.premise_decisive_test("INV-17", self.INV)
        self.assertIn("open: whether the MYC rise is a driver", t)
        self.assertIn("resolved by: graded genetic MYC lowering", t)

    def test_no_premise_or_an_investigation_without_a_test_adds_nothing(self):
        self.assertEqual(g.premise_decisive_test("", self.INV), "")
        self.assertEqual(g.premise_decisive_test("INV-99", self.INV), "")
        self.assertEqual(g.premise_decisive_test("INV-404", self.INV), "")

    def test_the_premise_the_proposal_assumes_comes_first_when_a_mapping_row_matched_its_chain(self):
        prem = [{"inv_id": "INV-17", "chain_pattern": "-> MYC", "premise": "assumes a direction for MYC"}, {"inv_id": "INV-16", "chain_pattern": "HIF1A", "premise": "assumes HIF1A drives HK2"}]
        t = g.premise_decisive_test("INV-17", self.INV, chain="X -P(+)-> MYC", premises=prem)
        self.assertTrue(t.startswith("INV-17: assumed: assumes a direction for MYC | open: "))
        self.assertNotIn("assumed:", g.premise_decisive_test("INV-17", self.INV, chain="X -P(+)-> Y", premises=prem))      # no matching row: no assumed text invented

    def test_two_premises_are_both_listed(self):
        inv = dict(self.INV, **{"INV-16": {"inv_id": "INV-16", "decisive_uncertainty": "q", "next_test": "catalytic-dead rescue"}})
        t = g.premise_decisive_test("INV-16; INV-17", inv)
        self.assertEqual(t.count("resolved by"), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
