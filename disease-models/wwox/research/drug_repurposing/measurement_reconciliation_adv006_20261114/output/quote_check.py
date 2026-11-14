#!/usr/bin/env python3
"""quote_check.py (ADV-006 producer P): verbatim check of every quote in this folder's tables.

Reads output/crosswalk.tsv (request_verbatim, pieces separated by ' || ', in source_path),
output/conflicts.tsv (quote_A in source_A, quote_B in source_B; 'path#locator') and
output/measurement_quotes.tsv (quote in source_path). Each quote is searched in the named
source file after collapsing whitespace on both sides (no other normalisation).
Writes output/quote_check.tsv with the columns conflict_or_req_id, side, source, found (yes/no).
Idempotent; paths in the tables are relative to the repository root (found from this file).
Usage: python3 quote_check.py        (no arguments)   |   quote_check.py --help
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "framework").is_dir() and (p / "disease-models").is_dir())


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


_cache = {}


def has(source, quote):
    path = source.split("#")[0]
    if path not in _cache:
        p = ROOT / path
        _cache[path] = norm(p.read_text(encoding="utf-8")) if p.is_file() else None
    text = _cache[path]
    if text is None:
        return "no"
    return "yes" if norm(quote) in text else "no"


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return 0
    out = []
    for r in read(HERE / "crosswalk.tsv"):
        for i, piece in enumerate(r["request_verbatim"].split(" || "), 1):
            out.append((r["req_id"], f"request_verbatim[{i}]", r["source_path"], has(r["source_path"], piece)))
    for r in read(HERE / "conflicts.tsv"):
        out.append((r["conflict_id"], "A", r["source_A"], has(r["source_A"], r["quote_A"])))
        out.append((r["conflict_id"], "B", r["source_B"], has(r["source_B"], r["quote_B"])))
    for i, r in enumerate(read(HERE / "measurement_quotes.tsv"), 1):
        out.append((f"{r['m_id']}#q{i}", r["field"], r["source_path"], has(r["source_path"], r["quote"])))
    with open(HERE / "quote_check.tsv", "w", newline="", encoding="utf-8") as f:
        f.write("conflict_or_req_id\tside\tsource\tfound\n")
        for row in out:
            f.write("\t".join(row) + "\n")
    bad = [r for r in out if r[3] == "no"]
    print(f"{len(out)} quotes checked, {len(bad)} not found")
    for r in bad:
        print("NOT FOUND:", r[0], r[1], r[2])
    return 0


if __name__ == "__main__":
    sys.exit(main())
