#!/usr/bin/env python3
"""IT27 P6: read-only join of the committed S8 proposal rows, the IT24 P6 decomposition and the IT24 P10 sensitivity for the cases of P6.
Writes cases_it27p6.tsv (one row per compound x seed set). Standard library only; no network; no engine call."""
import csv, gzip, sys
from pathlib import Path
csv.field_size_limit(10**9)
DR = Path(__file__).resolve().parent.parent
P = {r["proposal_id"]: r for r in csv.DictReader(open(DR/"generation_it27_p3_20261104/results_s8/proposals_it21.tsv"), delimiter="\t")}
D = {r["proposal_id"]: r for r in csv.DictReader(open(DR/"multitarget_it24_p6_20261104/proposals_decomposed.tsv"), delimiter="\t")}
S = {r["proposal_id"]: r for r in csv.DictReader(open(DR/"reverse_it24_p10_20261104/decomposition_sensitivity.tsv"), delimiter="\t")}
CASES = {  # case -> proposal ids (Q2 HDAC5/XIAP, Q5 and Q8 EZH2, Q5 ROCK2)
 "HDAC5": ["IT21P2-0005", "IT21P2-0010", "IT21P2-0004", "IT21P2-0032"],
 "XIAP": ["IT21P2-0014", "IT21P2-0017", "IT21P2-0034"],
 "EZH2": ["IT21P2-0198", "IT21P2-0199", "IT21P2-0200", "IT21P2-0993", "IT21P2-0994", "IT21P2-0995"],
 "ROCK2": ["IT21P2-0221", "IT21P2-0222", "IT21P2-0223", "IT21P2-0230"],
}
cols = ["case", "proposal_id", "question", "compound", "main_target", "handoff_eligible", "handoff_blocker", "z_reach", "n_origins", "chain",
        "p6_kind", "p6_targets_favourable", "p6_targets_contrary", "p6_dominant_share", "p10_label_1pct_floor",
        "attribution_state", "attribution_main_nm", "attribution_best_other_target", "attribution_best_other_nm", "attribution_main_measure", "max_phase", "seed_guards"]
out = []
for case, ids in CASES.items():
    for pid in ids:
        p, d, s = P[pid], D.get(pid, {}), S.get(pid, {})
        out.append([case, pid, p["question"], p["compound"], p["main_target"], p["handoff_eligible"], p["handoff_blocker"], p["z_reach"], p["n_origins"], p["chain"][:90],
                    d.get("kind", ""), d.get("targets_pos", ""), d.get("targets_neg", ""), d.get("dominant_share", ""), s.get("floor1pct", ""),
                    p["attribution_state"], p["attribution_main_nm"], p["attribution_best_target"], p["attribution_best_nm"], p["attribution_main_measure"], p["max_phase"], p["seed_guards"]])
w = csv.writer(open(Path(__file__).resolve().parent/"cases_it27p6.tsv", "w", newline=""), delimiter="\t", lineterminator="\n")
w.writerow(cols); w.writerows(out)
print(len(out), "rows")
