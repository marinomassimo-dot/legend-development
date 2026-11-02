#!/usr/bin/env python3
"""Tests for the external-only versus WWOX-qualified comparison (IT20 P5).

The arms are tested on synthetic universes, so the suite is fast and does not load the catalogue. One test reads the
committed comparison_summary.json and checks the properties the package's conclusions rest on - if a later catalogue
build changes those numbers, this is the test that says so.

Run: python3 -B -m unittest -v disease-models.wwox.research.drug_repurposing.hypotheses_it20_20261102.test_compare_universe
"""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("compare_universe_mod", HERE / "compare_universe.py")
cu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cu)


def a(need, fam, target, action, consistency, status="approved_any_source", abst=None, direction="down"):
    return {"need": need, "need_direction": direction, "family": fam, "compound": fam.lower(), "target": target,
            "action_on_target": action, "consistency": consistency, "abstention_class": abst,
            "link_source": "ChEMBL curated mechanism", "target_level": "single_protein",
            "relation_kind": "curated_mechanism", "status_class": status}


class Arms(unittest.TestCase):
    def test_the_external_arm_keeps_only_a_documented_up_or_down_action(self):
        u = [a("N1", "F1", "T1", "down", "consistent"), a("N1", "F2", "T1", "unresolved", "direction_unresolved")]
        rows = cu.arm_external(u)
        self.assertEqual([r["family"] for r in rows], ["F1"])

    def test_the_external_arm_orders_by_targets_touched_which_is_the_coverage_reflex(self):
        u = [a("N1", "PROMISCUOUS", f"T{i}", "down", "direction_unresolved") for i in range(4)]
        u += [a("N1", "SPECIFIC", "T9", "down", "consistent")]
        rows = cu.arm_external(u)
        self.assertEqual(rows[0]["family"], "PROMISCUOUS")
        self.assertEqual(rows[0]["rank_external"], 1)
        self.assertEqual(rows[1]["family"], "SPECIFIC")

    def test_the_external_arm_prefers_an_approved_status_over_an_unstated_one(self):
        u = [a("N1", "UNSTATED", "T1", "down", "consistent", status="no_status_statement"),
             a("N1", "APPROVED", "T1", "down", "consistent", status="approved_any_source")]
        self.assertEqual(cu.arm_external(u)[0]["family"], "APPROVED")

    def test_the_wwox_arm_keeps_only_a_direction_coherent_association(self):
        u = [a("N1", "COHERENT", "T1", "down", "consistent"),
             a("N1", "UNRESOLVED", "T1", "down", "direction_unresolved"),
             a("N1", "OPPOSED", "T1", "up", "opposed")]
        rows, _ = cu.arm_wwox(u)
        self.assertEqual([r["family"] for r in rows], ["COHERENT"])

    def test_the_wwox_arm_flags_a_family_that_is_opposed_on_another_need(self):
        u = [a("N1", "F1", "T1", "down", "consistent"), a("N2", "F1", "T2", "up", "opposed")]
        rows, _ = cu.arm_wwox(u)
        self.assertTrue(rows[0]["opposed_elsewhere"])

    def test_an_uncertain_direction_need_is_returned_apart_and_not_dropped(self):
        u = [a("N-UNC", "F1", "T1", "down", "direction_unresolved", abst="need_direction_not_evaluable", direction="uncertain")]
        rows, unresolved = cu.arm_wwox(u)
        self.assertEqual(rows, [])
        self.assertEqual(len(unresolved), 1)

    def test_a_need_with_an_unresolved_direction_is_reported_with_that_reason(self):
        needs = [{"id": "N-UNC", "intervention_direction": {"direction": "uncertain"}}]
        u = [a("N-UNC", "F1", "T1", "down", "direction_unresolved", abst="need_direction_not_evaluable", direction="uncertain")]
        out = cu.needs_without_a_tool(u, needs)
        self.assertEqual(len(out), 1)
        self.assertIn("direction of the need is unresolved", out[0]["why_no_tool"])

    def test_a_need_with_no_association_at_all_is_distinguished_from_one_with_an_unresolved_direction(self):
        needs = [{"id": "N-EMPTY", "intervention_direction": {"direction": "restore"}}]
        out = cu.needs_without_a_tool([], needs)
        self.assertIn("no catalogue association at all", out[0]["why_no_tool"])

    def test_a_need_that_qualifies_something_is_not_listed_as_toolless(self):
        needs = [{"id": "N1", "intervention_direction": {"direction": "down"}}]
        u = [a("N1", "F1", "T1", "down", "consistent")]
        self.assertEqual(cu.needs_without_a_tool(u, needs), [])


class CommittedResult(unittest.TestCase):
    """The properties the package's conclusions rest on. A later catalogue build may change them; then this fails on purpose."""

    def setUp(self):
        p = HERE / "comparison_summary.json"
        if not p.exists():
            self.skipTest("comparison_summary.json not generated in this checkout")
        self.s = json.loads(p.read_text(encoding="utf-8"))

    def test_both_arms_read_one_identical_universe(self):
        self.assertIn("identical for both arms", self.s["universe"]["definition"])
        self.assertGreater(self.s["universe"]["associations"], 0)

    def test_the_summary_states_that_the_order_is_research_investment_and_not_efficacy(self):
        self.assertIn("not a ranking of efficacy", self.s["plain_statement"])
        self.assertIn("medical advice", self.s["plain_statement"])

    def test_the_wwox_qualified_arm_is_a_subset_of_the_external_arm(self):
        """The measured finding of IT20 P5: the qualification filters, it does not surface a candidate of its own."""
        self.assertEqual(self.s["overlap"]["wwox_only"], [],
                         "the WWOX arm now surfaces a family the external arm misses: the generation finding has changed "
                         "and the package README must be re-read")

    def test_the_qualified_arm_reaches_only_a_minority_of_the_needs(self):
        self.assertLess(len(self.s["arm_wwox"]["needs_covered"]), 6)

    def test_most_needs_have_no_adequate_tool_and_each_says_why(self):
        rows = self.s["needs_without_an_adequate_tool"]
        self.assertGreater(len(rows), 10)
        for r in rows:
            self.assertTrue(r["why_no_tool"].strip())
            self.assertIn(r["need_direction"], ("restore", "up", "down", "uncertain", "modulate"))

    def test_the_unresolved_direction_bucket_is_named_a_gap_and_not_a_rejection(self):
        self.assertIn("not a rejection", self.s["direction_unresolved"]["statement"])
        self.assertGreater(self.s["direction_unresolved"]["associations"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
