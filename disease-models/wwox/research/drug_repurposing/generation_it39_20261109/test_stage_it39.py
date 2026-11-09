#!/usr/bin/env python3
"""IT39: stage S15 against S14. The only change is a new column that brings, to each proposal resting on a mapped premise, the open question and the measurement that resolves it. Public: reads the two committed stage tables only."""
from __future__ import annotations

import csv
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return {r["proposal_id"]: r for r in csv.DictReader(fh, delimiter="\t")}


A = rd(DR / "generation_it38_20261108/results_s14/proposals_it21.tsv")
B = rd(HERE / "results_s15/proposals_it21.tsv")
HA = [r["proposal_id"] for r in csv.DictReader(open(DR / "generation_it38_20261108/results_s14/handoff_it21.tsv", encoding="utf-8"), delimiter="\t")]
HB = list(csv.DictReader(open(HERE / "results_s15/handoff_it21.tsv", encoding="utf-8"), delimiter="\t"))


class StageS15(unittest.TestCase):
    def test_no_existing_column_changed_and_the_selection_is_identical(self):
        self.assertEqual(set(A), set(B))
        for c in A[next(iter(A))]:
            self.assertEqual([A[i][c] for i in sorted(A)], [B[i][c] for i in sorted(B)], c)
        self.assertEqual(HA, [r["proposal_id"] for r in HB])

    def test_the_new_column_exists_exactly_where_a_premise_is_mapped(self):
        for i, r in B.items():
            has = bool(r["shared_premise_investigation"])
            self.assertEqual(bool(r["premise_decisive_test"]), has, i)
            for inv in filter(None, r["shared_premise_investigation"].split("; ")):
                self.assertIn(inv + ": open:", r["premise_decisive_test"])
                self.assertIn("resolved by:", r["premise_decisive_test"])

    def test_five_of_fifteen_hand_overs_carry_the_measurement_that_resolves_their_premise(self):
        n = [r for r in HB if r.get("premise_decisive_test")]
        self.assertEqual(len(HB), 15)
        self.assertEqual(len(n), 5)
        self.assertEqual({r["shared_premise_investigation"] for r in n}, {"INV-14", "INV-16", "INV-17"})


class Dossiers(unittest.TestCase):
    def test_the_question_dossiers_are_what_the_builder_produces_from_the_two_tables(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("bq", HERE / "build_questions.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        self.assertEqual((HERE / "questions_it39.md").read_text(encoding="utf-8"), m.build())
        text = m.build()
        for inv in ("INV-17", "INV-18", "INV-05", "INV-03"):
            self.assertIn("## " + inv, text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
