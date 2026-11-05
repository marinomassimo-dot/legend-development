#!/usr/bin/env python3
"""IT30 P5: the carried limits are kept whole (S11 against S10). Offline. Usage: test_stage_it30.py (runs the checks; any argument prints this text)."""
import sys
if len(sys.argv) > 1:
    print(__doc__); raise SystemExit(0)
import csv, importlib.util, unittest
from pathlib import Path
csv.field_size_limit(10 ** 9)
DR = Path(__file__).resolve().parent.parent
rd = lambda p: list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
S10 = {r["proposal_id"]: r for r in rd(DR / "generation_it29_p5_20261105/results_s10/proposals_it21.tsv")}
S11 = {r["proposal_id"]: r for r in rd(DR / "generation_it30_p5_20261105/results_s11/proposals_it21.tsv")}
spec = importlib.util.spec_from_file_location("gen21", DR / "generation_it21_p2_20261103/run_generation_it21.py")
gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)


class T(unittest.TestCase):
    def test_a_qualification_at_the_end_of_a_long_limit_survives(self):
        long_ = "A " * 900 + "scope clause: class IIa-selective compounds NOT covered"
        out = gen.join_limits(["first limit", long_, "first limit"])
        self.assertTrue(out.endswith("class IIa-selective compounds NOT covered"))
        self.assertGreater(len(out), 1600)
        self.assertEqual(out.count("first limit"), 1)

    def test_nothing_is_dropped_only_repeats_collapse(self):
        parts = ["a | b", "b | c", "c"]
        self.assertEqual(gen.join_limits(parts), "a | b | c")
        self.assertEqual(gen.join_limits([]), "")

    def test_selection_is_unchanged_and_only_two_columns_moved(self):
        self.assertEqual(set(S10), set(S11))
        cols = set()
        for p in S10:
            cols |= {k for k in S10[p] if S10[p][k] != S11[p][k]}
        self.assertEqual(cols, {"carried_limits", "target_named_in_legend_material"})
        el = lambda S: sorted(p for p in S if S[p]["handoff_eligible"] == "yes")
        self.assertEqual(el(S10), el(S11))
        self.assertEqual(len(el(S11)), 220)

    def test_no_limit_is_shorter_than_before_and_the_hdac5_scope_clause_is_present(self):
        for p in S10:
            self.assertGreaterEqual(len(S11[p]["carried_limits"]), len(S10[p]["carried_limits"]), p)
        hd5 = [p for p in S11 if "IT29 (non-WWOX" in S11[p]["carried_limits"] and S11[p]["main_target"] == "HDAC5"]
        self.assertEqual(len(hd5), 20)
        for p in hd5:
            self.assertIn("NOT covered", S11[p]["carried_limits"], p)
        self.assertIn("NOT covered", S11["IT21P2-0019"]["carried_limits"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
