#!/usr/bin/env python3
"""IT33 stage S13: S12 with the widened premise map (INV-14, INV-16, INV-17). Only the new column may differ; the column must follow the curated patterns."""
import csv
import re
import unittest
from pathlib import Path

DR = Path(__file__).resolve().parents[1]


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


S12 = {r["proposal_id"]: r for r in rd(DR / "generation_it32_p3_20261107/results_s12/proposals_it21.tsv")}
S13 = {r["proposal_id"]: r for r in rd(DR / "generation_it33_p4_20261107/results_s13/proposals_it21.tsv")}
PREM = rd(DR / "generation_it21_p2_20261103/investigation_premises_it32.tsv")
COL = "shared_premise_investigation"


class StageS13(unittest.TestCase):
    def test_only_the_premise_column_differs_from_s12(self):
        self.assertEqual(set(S12), set(S13))
        for p in S12:
            self.assertEqual({k: v for k, v in S13[p].items() if k != COL}, {k: v for k, v in S12[p].items() if k != COL}, p)

    def test_the_column_equals_the_curated_patterns_applied_to_the_chain(self):
        for p, r in S13.items():
            want = "; ".join(sorted({m["inv_id"] for m in PREM if re.search(m["chain_pattern"], r["chain"])}))
            self.assertEqual(r[COL], want, p)

    def test_the_counts_reported_in_the_readme_hold(self):
        marked = {}
        for r in S13.values():
            for i in filter(None, r[COL].split("; ")):
                marked[i] = marked.get(i, 0) + 1
        self.assertEqual(marked, {"INV-14": 30, "INV-16": 20, "INV-17": 555})

    def test_ablation_of_the_added_rows_gives_the_s12_column(self):
        keep = [m for m in PREM if m["inv_id"] == "INV-16"]
        for p, r in S13.items():
            want = "; ".join(sorted({m["inv_id"] for m in keep if re.search(m["chain_pattern"], r["chain"])}))
            self.assertEqual(want, S12[p][COL], p)

    def test_selection_and_handover_are_unchanged(self):
        self.assertEqual([p for p, r in S12.items() if r["handoff_eligible"] == "yes"], [p for p, r in S13.items() if r["handoff_eligible"] == "yes"])
        a = [r["proposal_id"] for r in rd(DR / "generation_it32_p3_20261107/results_s12/handoff_it21.tsv")]
        b = [r["proposal_id"] for r in rd(DR / "generation_it33_p4_20261107/results_s13/handoff_it21.tsv")]
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
