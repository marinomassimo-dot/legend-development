#!/usr/bin/env python3
"""quote_check.py (PRESIDIO-001): verbatim check of the quoted cells in confirmation.tsv.

Each row's `source_verbatim` is split on ' || '; every fragment is searched, after collapsing
whitespace on both sides (no other normalisation), in the union of the source files that the
table names in the `files:` part of `source_locator` (paths relative to the repository root,
found from this file). Fragments starting with 'computed:' are not quotations and are skipped.
Writes quote_check.tsv (item, fragment_index, found yes/no, first 60 characters) and, with
the 'cells' check, counts how many of the 78 non-key cells of levers.tsv appear verbatim in the
generator rows for L1-L6. Idempotent; takes no arguments.
Usage: python3 quote_check.py        |   quote_check.py --help
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "framework").is_dir() and (p / "disease-models").is_dir())
RD = "disease-models/wwox/research/drug_repurposing/"
LEV = RD + "inhibitory_defect_sci47_20261112/output/levers.tsv"
GEN = RD + "generation_it40_20261109/conditional_proposals_packages_it47.tsv"


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    if len(sys.argv) > 1:
        print(__doc__)
        return 0
    with open(HERE / "confirmation.tsv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    files = set()
    for r in rows:
        if "| files:" in r["source_locator"]:
            files.update(x for x in r["source_locator"].split("| files:")[1].strip().split(";") if x)
    text = {p: norm((ROOT / p).read_text(encoding="utf-8")) for p in sorted(files)}
    out, bad = [], 0
    for r in rows:
        for i, frag in enumerate(r["source_verbatim"].split(" || ")):
            if frag.startswith("computed:"):
                continue
            ok = any(norm(frag) in t for t in text.values())
            bad += not ok
            out.append((r["item"], i, "yes" if ok else "no", frag[:60]))
    # cells check: 13 non-key cells of levers.tsv x 6 levers appear verbatim in the generator row
    with open(ROOT / LEV, newline="", encoding="utf-8") as f:
        lev = list(csv.DictReader(f, delimiter="\t"))
    with open(ROOT / GEN, newline="", encoding="utf-8") as f:
        gen = {r["proposal_id"].split("::")[1]: " ".join(r.values()) for r in csv.DictReader(f, delimiter="\t") if "inhibitory_defect_sci47" in r["proposal_id"]}
    cells = sum(v in gen[r["lever_id"]] for r in lev for k, v in r.items() if k != "lever_id")
    with open(HERE / "quote_check.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["item", "fragment_index", "found", "start_of_fragment"])
        w.writerows(out)
        w.writerow(["cells", "", "%d of 78" % cells, "non-key cells of levers.tsv found verbatim in the generator rows"])
    print("fragments %d, not found %d; cells %d of 78" % (len(out), bad, cells))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
