#!/usr/bin/env python3
"""IT29 P6 case 1: three arms on the same reference list of compounds named in the functional-search tables.

Arm A  current path       : frozen `repurposing_search.py need NEED-MYELINATION` (committed roles, committed needs)
Arm B  simple lookup      : is the named compound in the committed catalogue at all, and does it carry any recorded mechanism
Arm C  contextualised path: same search with signed roles + needs extended by phenotype_roles_it29.py
Retrospective: the reference list and the signs come from the same functional-search sources; `sign_source_is_reference`
marks the compounds whose own study also provided the target sign (circular) so they are reported apart.
Usage: compare_case1_it29.py --a A.json --c C.json --out out.tsv
"""
import argparse, csv, gzip, json, sys
from pathlib import Path

CACHE = Path(__import__("os").environ.get("LEGEND_CATALOG_CACHE", "")) / "chembl"

# name, evidence direction, evidence rows, is the target sign for this compound derived from the SAME study?
REF = [
    ("benztropine", "favourable", "R01 R02 R06 R14", False), ("clemastine", "favourable", "R07 R12 R14 R48", False),
    ("atropine", "favourable", "R08", False), ("ipratropium", "favourable", "R08", False), ("oxybutynin", "favourable", "R08", False),
    ("quetiapine", "favourable", "R13", False), ("miconazole", "favourable", "R22 R24 R28 R30", False),
    ("ketoconazole", "favourable", "R30", True), ("clobetasol", "favourable", "R23 R25 R26", True),
    ("amorolfine", "favourable", "R31", True), ("tamoxifen", "favourable", "R32 R36", False), ("ifenprodil", "favourable", "R36 R37", False),
    ("liothyronine", "favourable", "R35", False), ("bexarotene", "favourable", "R35 R42", False), ("sobetirome", "favourable", "R49", False),
    ("trichostatin", "adverse", "R40", False), ("apicidin", "adverse", "R40", False), ("fimepinostat", "adverse", "R40", False),
    ("mevastatin", "adverse", "R34", True), ("neostigmine", "adverse", "R52", False),
]
ALIAS = {"fimepinostat": ["cudc-907", "fimepinostat"], "trichostatin": ["trichostatin"]}


def load(p):
    return json.load(open(p))["associations"]


def labels(assoc, name):
    keys = ALIAS.get(name, [name])
    out = set()
    for x in assoc:
        if any(k in x["compound"].lower() for k in keys) and not x.get("excluded_from_counts"):
            out.add(x["consistency"])
    return out


def catalogue_names():
    names = {}
    with gzip.open(CACHE / "molecules.jsonl.gz", "rt", encoding="utf-8") as fh:
        for l in fh:
            m = json.loads(l)
            names[(m.get("pref_name") or "").lower()] = m["molecule_chembl_id"]
    return names


def verdict(ev, labs):
    if not labs:
        return "not_reached"
    if "consistent" in labs and "opposed" in labs:
        return "mixed"
    if "consistent" in labs:
        return "right" if ev == "favourable" else "wrong"
    if "opposed" in labs:
        return "right" if ev == "adverse" else "wrong"
    return "abstained"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--a", required=True); ap.add_argument("--c", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    A, C = load(a.a), load(a.c)
    cat = catalogue_names()
    rows = []
    for name, ev, rws, circ in REF:
        keys = ALIAS.get(name, [name])
        in_cat = any(any(k in n for k in keys) for n in cat)
        la, lc = labels(A, name), labels(C, name)
        in_cat = in_cat or bool(lc)
        rows.append([name, ev, rws, "yes" if circ else "no", "yes" if in_cat else "no", ",".join(sorted(la)) or "-", verdict(ev, la),
                     ",".join(sorted(lc)) or "-", verdict(ev, lc)])
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["compound", "evidence_direction", "evidence_rows", "sign_source_is_reference", "in_catalogue_B", "arm_A_labels", "arm_A_verdict", "arm_C_labels", "arm_C_verdict"])
        w.writerows(rows)
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); raise SystemExit(0)
    raise SystemExit(main())
