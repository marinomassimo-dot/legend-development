#!/usr/bin/env python3
"""Check each quote in verbatim.tsv against the saved PMC524435 article text (whitespace and citation-link markup normalised on both sides)."""
import csv, html, re, sys

def norm(s, markup=False):
    if markup:
        s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\s+([,.;:)])", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()

def main(page, tsv):
    # a plain-text body keeps its "<" (P < 0.01); only an .html page is stripped of tags
    body = norm(open(page, encoding="utf8", errors="replace").read(), markup=page.endswith(".html"))
    rows = list(csv.DictReader(open(tsv, encoding="utf8"), delimiter="\t"))
    ok = 0
    for r in rows:
        hit = norm(r["quote"]) in body
        ok += hit
        print(f"{r['id']}\t{'FOUND' if hit else 'MISSING'}")
    print(f"{ok}/{len(rows)} found")
    return 0 if ok == len(rows) else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
