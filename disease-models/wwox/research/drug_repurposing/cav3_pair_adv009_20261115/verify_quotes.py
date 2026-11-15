#!/usr/bin/env python3
"""ADV-009: mechanical verbatim check of readings.tsv against the saved PMC article pages.

For every row whose read_status is read_in_original, the `verbatim` text must occur in the saved page of the named PMC id
after the same normalisation on both sides (HTML tags and script/style removed, entities unescaped, whitespace collapsed).
Prints one line per row and a final PASS/FAIL; exit code 1 on any miss. It does not judge what a sentence means.
Run: python3 -I verify_quotes.py <pages_dir> [readings.tsv] [--help]
The pages are third-party text, kept under files/ (gitignored) with their sha256 in access.tsv.
"""
import csv
import hashlib
import html
import os
import re
import sys


def norm(raw):
    raw = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", "", raw)
    raw = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return re.sub(r"\s+", " ", raw).strip()


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 2:
        print(__doc__)
        return 0
    pages = sys.argv[1]
    table = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "readings.tsv")
    cache, bad, n = {}, 0, 0
    with open(table, encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["read_status"] != "read_in_original":
                continue
            n += 1
            pid = row["pmc_id"]
            if pid not in cache:
                path = os.path.join(pages, f"{pid}_pmc_article_page.html")
                data = open(path, "rb").read()
                cache[pid] = (norm(data.decode("utf-8", "replace")), hashlib.sha256(data).hexdigest())
            text, digest = cache[pid]
            ok = norm(row["verbatim"]) in text
            bad += 0 if ok else 1
            print(f"{row['row']}\t{pid}\t{'FOUND' if ok else 'MISSING'}\t{digest[:12]}")
    print(f"{'PASS' if bad == 0 else 'FAIL'}: {n - bad} of {n} read_in_original rows found")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
