#!/usr/bin/env python3
"""IT38: stage S14 against S13. The MYC relations reach the proposals as carried limits and change nothing else that selection reads. Public: reads the two committed stage tables only."""
from __future__ import annotations

import csv
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return {r["proposal_id"]: r for r in csv.DictReader(fh, delimiter="\t")}


A = rd(DR / "generation_it33_p4_20261107/results_s13/proposals_it21.tsv")
B = rd(HERE / "results_s14/proposals_it21.tsv")


class StageS14(unittest.TestCase):
    def test_same_proposals_same_eligibility_same_selection_columns(self):
        self.assertEqual(set(A), set(B))
        for k in ("handoff_eligible", "handoff_blocker", "status", "hypothesis", "qualified", "chain", "z_total", "n_origins", "cluster_work_done", "blocker_detail"):
            self.assertEqual([A[i][k] for i in sorted(A)], [B[i][k] for i in sorted(B)], k)

    def test_carried_limits_change_only_where_the_investigation_premise_is_mapped(self):
        changed = {i for i in A if A[i]["carried_limits"] != B[i]["carried_limits"]}
        inv17 = {i for i in B if B[i]["shared_premise_investigation"] == "INV-17"}
        self.assertEqual(changed, inv17)
        self.assertEqual(len(inv17), 555)
        for i in A:
            if i not in inv17:
                self.assertEqual(B[i].get("relation_use", ""), "")

    def test_each_limit_carries_its_status_label_and_never_blocks(self):
        for i in B:
            if B[i]["shared_premise_investigation"] != "INV-17":
                continue
            lim = B[i]["carried_limits"]
            self.assertIn("RELATION_CONTEXT_LIMIT [INFERRED (not measured)]", lim)
            self.assertIn("RELATION_OCCUPANCY_NOT_AMOUNT [EXPLORATORY", lim)
            self.assertEqual("RELATION_UNINFORMATIVE" in lim, B[i]["hypothesis"] == "H_PROTECT")
            self.assertNotIn("relation", B[i]["handoff_blocker"].lower())

    def test_the_uninformative_result_is_not_turned_into_evidence_against(self):
        lim = next(B[i]["carried_limits"] for i in B if B[i]["hypothesis"] == "H_PROTECT" and "RELATION_UNINFORMATIVE" in B[i]["carried_limits"])
        self.assertIn("not carried as evidence against it", lim)
        self.assertEqual([A[i]["handoff_eligible"] for i in sorted(A)], [B[i]["handoff_eligible"] for i in sorted(B)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
