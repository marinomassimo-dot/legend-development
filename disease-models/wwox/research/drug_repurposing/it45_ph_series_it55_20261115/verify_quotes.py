"""Mechanical quote check for verbatim.tsv (stdlib only).

Usage: python3 -I verify_quotes.py --pages DIR [--tsv verbatim.tsv] [--write]

DIR holds the saved page copies as <page>.html (the copies are third-party text, kept outside git).
Each page is converted to plain text (tags removed, scripts and styles dropped, entities decoded),
whitespace is collapsed on both sides, and the quote must occur as a substring. The script also
prints a few term counts used by the README for statements of absence ("not stated").
"""
import argparse
import csv
import re
import sys
from html.parser import HTMLParser


class _P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0

    def handle_starttag(self, t, a):
        if t in ("script", "style", "noscript"):
            self.skip += 1
        if t in ("p", "div", "h1", "h2", "h3", "h4", "li", "tr", "br", "section", "table", "caption", "figcaption"):
            self.out.append("\n")

    def handle_endtag(self, t):
        if t in ("script", "style", "noscript"):
            self.skip -= 1
        if t in ("td", "th"):
            self.out.append(" | ")

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)


def page_text(path):
    p = _P()
    with open(path, encoding="utf-8", errors="replace") as fh:
        p.feed(fh.read())
    return re.sub(r"\s+", " ", "".join(p.out).replace("\xa0", " ")).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", required=True)
    ap.add_argument("--tsv", default="verbatim.tsv")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    cache = {}
    with open(a.tsv, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE))
    ok = 0
    for r in rows:
        pg = r["page"]
        if pg not in cache:
            cache[pg] = page_text("%s/%s.html" % (a.pages, pg))
        q = re.sub(r"\s+", " ", r["quote"]).strip()
        hit = q in cache[pg]
        r["found_in_page"] = "yes" if hit else "no"
        ok += hit
        print("%s %s %s" % (r["id"], pg, r["found_in_page"]))
    print("found %d of %d" % (ok, len(rows)))
    if a.write:
        with open(a.tsv, "w", encoding="utf-8") as fh:
            fh.write("\t".join(rows[0].keys()) + "\n")
            for r in rows:
                fh.write("\t".join(r.values()) + "\n")
    print("-- term counts in the page text (for statements of absence)")
    for pg, t in sorted(cache.items()):
        c = {k: len(re.findall(k, t)) for k in ("EC50", r"Ba2\+", "barium", "THIK", r"TASK-?3")}
        print(pg, len(t), c)
    return 0 if ok == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
