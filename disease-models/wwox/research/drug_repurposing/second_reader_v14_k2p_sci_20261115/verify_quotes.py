#!/usr/bin/env python3
"""Check that each quote of verbatim.tsv occurs in the saved text named in its row (whitespace and citation-link markup normalised on both sides).
Run:  python3 -I verify_quotes.py <verbatim.tsv> <dir holding the saved .txt files>      (--help prints this text)"""
import csv
import re
import sys


def norm(s):
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\s+([,.;:)])", r"\1", s)
    return s.strip()


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 3:
        print(__doc__)
        return 0
    bad = 0
    cache = {}
    with open(sys.argv[1], encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            f = r["source_file"]
            if f not in cache:
                with open(sys.argv[2].rstrip("/") + "/" + f, encoding="utf-8") as g:
                    cache[f] = norm(g.read())
            ok = norm(r["quote"]) in cache[f]
            bad += (not ok)
            print(r["id"], "FOUND" if ok else "MISSING")
    print("quotes missing: %d" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
