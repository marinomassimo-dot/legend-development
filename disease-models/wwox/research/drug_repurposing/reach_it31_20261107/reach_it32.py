#!/usr/bin/env python3
"""IT32 P1: the IT31 reachability counts again, with identity resolved through the catalogue ids in catalogue_ids_it32.tsv
(regenerate that file with `catalog/catalog_build.py query --name <x>`; it needs the local catalogue cache, the rest does not).
Read-only. A mention in a card, question or investigation is not a relation consumed by the generator: those layers are curated text,
and only the stage proposals are computed from seeds."""
import csv
import glob
import re
import sys
from pathlib import Path

DR = Path(__file__).resolve().parents[1]


def rows(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def has_id(text: str, key: str) -> bool:
    """Whole-identifier match: CAT:CHEMBL40 must not match CAT:CHEMBL4000123 (a substring test did, and counted eight false rows)."""
    return re.search(re.escape(key) + r"(?![A-Za-z0-9])", text) is not None


def main() -> int:
    ids = rows(Path(__file__).with_name("catalogue_ids_it32.tsv"))
    stage = rows(DR / "generation_it30_p5_20261105/results_s11/proposals_it21.tsv")
    hand = {r["proposal_id"] for r in rows(DR / "generation_it30_p5_20261105/results_s11/handoff_it21.tsv")}
    cq = rows(DR / "context_it30_20261105/results/conditional_questions_it30.tsv")
    inv = rows(DR / "ranking_it8_p9_20261029/investigations_it20.tsv")
    cards = {p: Path(p).read_text(encoding="utf-8", errors="replace").lower() for p in glob.glob(str(DR / "cards/*.card.json"))}
    out = [["compound", "catalogue_records", "neighbours_not_merged", "stage_by_family_id", "stage_by_name_only", "handed_over",
            "cards_mentioning", "conditional_questions", "investigations"]]
    for q in dict.fromkeys(r["query_name"] for r in ids):
        mine = [r for r in ids if r["query_name"] == q]
        same = [r for r in mine if r["role"] == "same_substance_or_salt"]
        keys = {r["catalogue_id"] for r in same}
        names = {r["catalogue_name"].lower() for r in same}
        by_fam = [s for s in stage if any(has_id(s["family_id"], k) for k in keys)]
        by_name = [s for s in stage if s["proposal_id"] not in {x["proposal_id"] for x in by_fam}
                   and (s["compound"].lower() in names or s["base_name"].lower() in names)]
        chembl = {k.split(":")[-1].lower() for k in keys if k.startswith("CAT:CHEMBL")}
        n_cards = sum(any(n in t for n in names | chembl) for t in cards.values())
        n_cq = sum(any(n in " ".join(r.values()).lower() for n in names | {q}) for r in cq)
        n_inv = sum(any(n in " ".join((r.get(c) or "") for c in ("intervention", "question", "evidence_available", "chembl_ids")).lower() for n in names | {q} | chembl) for r in inv)
        out.append([q, len(same), len(mine) - len(same), len(by_fam), len(by_name),
                    sum(s["proposal_id"] in hand for s in by_fam + by_name), n_cards, n_cq, n_inv])
    csv.writer(sys.stdout, delimiter="\t", lineterminator="\n").writerows(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
