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


if __name__ == "__main__":
    unittest.main(verbosity=2)
