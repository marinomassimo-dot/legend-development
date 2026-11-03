#!/usr/bin/env python3
"""IT22 P6 forward snapshot (reads the committed IT22 stage tables, recomputes nothing).

Writes forward_snapshot_it22.tsv next to this file: for each contrast case, what the generative path (results_p3) says BEFORE any reverse analysis of the case:
every proposal row of the molecule family (question, arm, main target, status, eligibility and blocker, attribution state, carried limits, seed guards, hand-over flag).
It is committed before the reverse analysis (git log shows the order). Cases are chosen for contrast (a known case, a case tied to a newly connected input, a case whose exclusion must stay valid),
not for passing; no case is a target the engine must recover.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
G = DR / "generation_it22_p1_20261103" / "results_p3"
CASES = [("vorinostat", "known case (IT21 V1 case; attribution, HDAC5 chain)", ["vorinostat"]),
         ("tapinarof", "tied to the newly connected Q8 input (NFE2L2 tone)", ["tapinarof"]),
         ("omaveloxolone", "canonical NRF2 activator: does the newly connected Q8 input reach it?", ["omaveloxolone"]),
         ("ezh2_inhibitors", "arm now reached from two WWOX observations (Q5 glia cytokines, Q8 NRF2 tone)", ["gsk343", "gsk2816126", "tazemetostat", "mevrometostat", "valemetostat", "tulmimetostat"]),
         ("btk_inhibitors", "exclusion that must stay valid (premise refuted for the BTK arm)", ["ibrutinib", "zanubrutinib", "acalabrutinib", "tirabrutinib", "cgi1746"]),
         ("pracinostat_cluster", "released from the nanatinostat veto: evaluated on its own data", ["pracinostat", "nanatinostat", "quisinostat", "cudc101"])]
norm = lambda s: "".join(c for c in (s or "").lower() if c.isalnum())


def main():
    P = list(csv.DictReader(open(G / "proposals_it21.tsv", encoding="utf-8", newline=""), delimiter="\t"))
    H = {r["proposal_id"] for r in csv.DictReader(open(G / "handoff_it21.tsv", encoding="utf-8", newline=""), delimiter="\t")}
    cols = ["case", "why_this_case", "proposal_id", "compound", "question", "hypothesis", "main_target", "status", "handoff_eligible", "handoff_blocker", "handed_over", "attribution_state",
            "attribution_comparison_basis", "carried_limits", "seed_guards", "earlier_decision", "earlier_thread"]
    out = []
    for case, why, names in CASES:
        for r in P:
            if any(norm(r["compound"]).startswith(n) or n in norm(r["base_name"]) for n in names):
                out.append(dict(case=case, why_this_case=why, handed_over="yes" if r["proposal_id"] in H else "", **{k: (r.get(k) or "")[:240] for k in cols if k not in ("case", "why_this_case", "handed_over")}))
    with open(HERE / "forward_snapshot_it22.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print(len(out), "rows for", len({o["case"] for o in out}), "cases")


if __name__ == "__main__":
    main()
