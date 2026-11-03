#!/usr/bin/env python3
"""IT23 P1: freeze input and output of the CURRENT generative method for the contrasting cases, before any new capability is added.

  freeze_current_method.py            writes frozen_inputs.tsv (path, bytes, sha256) and frozen_current_method.tsv (the current method's rows for the cases)

Reads only committed files of the IT22 final state (generation_it22_p1_20261103/results_p4: the stage tables the IT22 reverse test and verification used). Recomputes nothing.
Cases (chosen from current data, see README.md): Q5 cytokines (direction sustained across two mouse models, role unknown), Q6 MYC in radial glia (one within-cell-type
contrast, the rise may be compensatory), Q8 NFE2L2 (lower; second system failed its control; role unknown). No case is chosen because a gene is differentially expressed or central.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
CASES = ("Q5", "Q6", "Q8")
INPUTS = ["generation_it22_p1_20261103/inputs_it22/seeds.tsv", "generation_it22_p1_20261103/inputs_it22/seeds_p1/Q5_expression_tiersAB.tsv",
          "generation_it22_p1_20261103/inputs_it22/seeds_p1/Q6_expression_tiersAB.tsv", "generation_it22_p1_20261103/inputs_it22/seeds_p1/Q6_protein_tiersAB.tsv",
          "generation_it22_p1_20261103/inputs_it22/seeds_p1/Q8_expression_tiersAB.tsv", "generation_it22_p1_20261103/inputs_it22/question_roles.tsv",
          "generation_it22_p1_20261103/inputs_it22/seed_annotations.tsv", "generation_it21_p2_20261103/results/actions/family_actions.tsv.gz",
          "generation_it22_p1_20261103/results_p4/proposals_it21.tsv", "generation_it22_p1_20261103/results_p4/handoff_it21.tsv", "generation_it22_p1_20261103/decision_scope_it22.tsv",
          "generation_it21_p2_20261103/run_generation_it21.py", "generation_it21_p2_20261103/attribution_screen_it21.py", "generation_it9_p2_20261030/seed_engine.py",
          "generation_it10_p1_20261031/engine_v4/seed_engine_v4.py"]
KEEP = ["proposal_id", "question", "seed_set", "hypothesis", "status", "compound", "family_id", "main_target", "z_total", "z_reach", "zmin", "n_origins", "chain", "chain_edges",
        "handoff_eligible", "handoff_blocker", "attribution_state", "carried_limits", "seed_guards", "earlier_decision", "earlier_thread"]


def main():
    with open(HERE / "frozen_inputs.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["path", "bytes", "sha256"])
        for rel in INPUTS:
            b = (DR / rel).read_bytes()
            w.writerow([rel, len(b), hashlib.sha256(b).hexdigest()])
    rows = list(csv.DictReader(open(DR / "generation_it22_p1_20261103/results_p4/proposals_it21.tsv", encoding="utf-8", newline=""), delimiter="\t"))
    H = {r["proposal_id"] for r in csv.DictReader(open(DR / "generation_it22_p1_20261103/results_p4/handoff_it21.tsv", encoding="utf-8", newline=""), delimiter="\t")}
    out = [dict({k: r.get(k, "") for k in KEEP}, handed_over="yes" if r["proposal_id"] in H else "") for r in rows if r["question"] in CASES]
    with open(HERE / "frozen_current_method.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=KEEP + ["handed_over"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    import collections
    c = collections.Counter((r["question"], r["handoff_eligible"]) for r in out)
    print(len(out), "rows;", dict(c))


if __name__ == "__main__":
    main()
