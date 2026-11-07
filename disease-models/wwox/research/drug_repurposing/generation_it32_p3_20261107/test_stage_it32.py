#!/usr/bin/env python3
"""IT32 stage S12: S11 plus one column (shared_premise_investigation). Everything else must be identical, and the column must follow the curated chain prefix."""
import csv
import unittest
from pathlib import Path

DR = Path(__file__).resolve().parents[1]


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


S11 = {r["proposal_id"]: r for r in rd(DR / "generation_it30_p5_20261105/results_s11/proposals_it21.tsv")}
S12 = {r["proposal_id"]: r for r in rd(DR / "generation_it32_p3_20261107/results_s12/proposals_it21.tsv")}


class StageS12(unittest.TestCase):
    def test_only_the_new_column_differs_from_s11(self):
        self.assertEqual(set(S11), set(S12))
        for p in S11:
            self.assertEqual({k: v for k, v in S12[p].items() if k != "shared_premise_investigation"}, S11[p], p)

    def test_the_column_marks_exactly_the_proposals_on_the_shared_chain(self):
        marked = {p for p, r in S12.items() if r["shared_premise_investigation"]}
        chain = {p for p, r in S12.items() if r["chain"].startswith("HDAC5 -T(+)-> SLC2A1")}
        self.assertEqual(marked, chain)
        self.assertEqual({S12[p]["shared_premise_investigation"] for p in marked}, {"INV-16"})
        self.assertEqual(len(marked), 20)

    def test_selection_and_handover_are_unchanged(self):
        self.assertEqual([p for p, r in S11.items() if r["handoff_eligible"] == "yes"], [p for p, r in S12.items() if r["handoff_eligible"] == "yes"])
        a = [r["proposal_id"] for r in rd(DR / "generation_it30_p5_20261105/results_s11/handoff_it21.tsv")]
        b = [r["proposal_id"] for r in rd(DR / "generation_it32_p3_20261107/results_s12/handoff_it21.tsv")]
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
