#!/usr/bin/env python3
"""IT31 P7a: for contrasting reference compounds, which layer of the module holds them and which consumers read them (read-only, no generation)."""
import csv, glob, json, sys
from pathlib import Path

DR = Path(__file__).resolve().parents[1]
COMPOUNDS = ["vorinostat", "phenobarbital", "bumetanide", "rapamycin", "vigabatrin", "benztropine", "clemastine", "clonazepam",
             "ethosuximide", "levetiracetam", "perampanel", "ifenprodil", "memantine", "efonidipine"]


def rows(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def count(rowset, name, cols=None):
    n = 0
    for r in rowset:
        vals = [r.get(c, "") for c in cols] if cols else r.values()
        if any(name in str(v).lower() for v in vals):
            n += 1
    return n


def text_hits(pattern, name):
    n = 0
    for p in glob.glob(str(DR / pattern)):
        n += name in Path(p).read_text(encoding="utf-8", errors="replace").lower()
    return n


def main() -> int:
    stage = rows(DR / "generation_it30_p5_20261105/results_s11/proposals_it21.tsv")
    hand = rows(DR / "generation_it30_p5_20261105/results_s11/handoff_it21.tsv")
    cmp1 = rows(DR / "phenotype_first_it29_20261105/comparison_case1_it29.tsv")
    cq = rows(DR / "context_it30_20261105/results/conditional_questions_it30.tsv")
    inv = rows(DR / "ranking_it8_p9_20261029/investigations_it20.tsv")
    out = [["compound", "stage_proposals_it21", "handed_over", "case1_comparison", "conditional_questions", "investigations", "cards"]]
    for c in COMPOUNDS:
        out.append([c, count(stage, c, ["compound", "base_name"]), count(hand, c), count(cmp1, c, ["compound"]), count(cq, c),
                    count(inv, c, ["intervention", "question", "evidence_available"]), text_hits("cards/*.card.json", c)])
    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerows(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
