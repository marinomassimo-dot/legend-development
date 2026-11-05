#!/usr/bin/env python3
"""IT29 P5: facts about the committed S10 tables against S9. Offline. Usage: test_stage_it29.py (runs the checks; any argument prints this text)."""
import sys
if len(sys.argv) > 1:
    print(__doc__); raise SystemExit(0)
import csv, unittest
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
rd = lambda p: list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
S9 = {r["proposal_id"]: r for r in rd(DR / "generation_it28_p6_20261105/results_s9/proposals_it21.tsv")}
S10 = {r["proposal_id"]: r for r in rd(DR / "generation_it29_p5_20261105/results_s10/proposals_it21.tsv")}


class T(unittest.TestCase):
    def test_only_carried_limits_moved_and_selection_is_unchanged(self):
        self.assertEqual(set(S9), set(S10))
        moved = [p for p in S9 if S9[p] != S10[p]]
        self.assertTrue(moved)
        for p in moved:
            self.assertEqual({k for k in S9[p] if S9[p][k] != S10[p][k]}, {"carried_limits"}, p)
        self.assertEqual([p for p in S9 if S9[p]["handoff_eligible"] == "yes"], [p for p in S10 if S10[p]["handoff_eligible"] == "yes"])
        h = lambda s: [r["proposal_id"] for r in rd(DR / s / "handoff_it21.tsv")]
        self.assertEqual(h("generation_it28_p6_20261105/results_s9"), h("generation_it29_p5_20261105/results_s10"))

    def test_the_oligodendrocyte_hdac_limit_reaches_hdac3_and_hdac5_proposals_only(self):
        moved = [p for p in S9 if S9[p] != S10[p]]
        self.assertEqual({S10[p]["main_target"] for p in moved}, {"HDAC3", "HDAC5"})
        self.assertTrue(all("oligodendrocyte lineage" in S10[p]["carried_limits"] for p in moved))
        self.assertFalse(any("oligodendrocyte lineage" in r["carried_limits"] and "IT29 phenotype-first" in r["carried_limits"] for p, r in S10.items() if r["main_target"] not in ("HDAC3", "HDAC5")))


if __name__ == "__main__":
    unittest.main()
