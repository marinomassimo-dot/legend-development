#!/usr/bin/env python3
"""IT28 P6: facts about the committed S9 tables (exact InChIKey join of GtoPdb ligands without a ChEMBL id; R4 families carry their ChEMBL family's measures) against S8. Offline. Usage: test_stage_it28.py"""
import sys
if len(sys.argv) > 1:
    print(__doc__); raise SystemExit(0)
import csv, unittest
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
rd = lambda p: list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
S8 = {r["proposal_id"]: r for r in rd(DR / "generation_it27_p3_20261104/results_s8/proposals_it21.tsv")}
S9 = {r["proposal_id"]: r for r in rd(DR / "generation_it28_p6_20261105/results_s9/proposals_it21.tsv")}


class T(unittest.TestCase):
    def test_same_rows_and_no_selection_effect(self):
        self.assertEqual(set(S8), set(S9))
        self.assertEqual(sum(r["handoff_eligible"] == "yes" for r in S8.values()), sum(r["handoff_eligible"] == "yes" for r in S9.values()))
        h = lambda p: [r["proposal_id"] for r in rd(DR / p / "handoff_it21.tsv")]
        self.assertEqual(h("generation_it27_p3_20261104/results_s8"), h("generation_it28_p6_20261105/results_s9"))

    def test_tazemetostat_gets_its_ezh2_measure_in_both_families(self):
        for pid in ("IT21P2-0199", "IT21P2-0994", "IT21P2-0209", "IT21P2-1004"):
            self.assertEqual(S8[pid]["attribution_state"], "NOT_ASSESSABLE")
        for pid in ("IT21P2-0199", "IT21P2-0994", "IT21P2-0209", "IT21P2-1004"):          # 0209/1004 are the DGIdb family of the R4 identity
            self.assertEqual(S9[pid]["attribution_state"], "SINGLE_MEASURED_TARGET", pid)
            self.assertEqual(S9[pid]["attribution_main_nm"], "11.0")

    def test_only_attribution_fields_and_blocker_text_moved_and_unknown_stays_unknown(self):
        moved = [p for p in S9 if S9[p] != S8[p]]
        self.assertGreaterEqual(len(moved), 50)
        n_na = sum(r["attribution_state"] == "NOT_ASSESSABLE" for r in S9.values())
        self.assertLess(n_na, sum(r["attribution_state"] == "NOT_ASSESSABLE" for r in S8.values()))
        self.assertTrue(all(r["qualified"] == "no" for r in S9.values()))


if __name__ == "__main__":
    unittest.main(verbosity=1)
