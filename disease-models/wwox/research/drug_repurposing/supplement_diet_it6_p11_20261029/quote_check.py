#!/usr/bin/env python3
"""Check every verbatim quote in locators.tsv against the article XML it names (IT6-P11, scientist-b).

The XML files are NOT in the repository (files/ is gitignored). Re-acquire each one from its recipe in README.md
(Europe PMC full-text endpoint, GET, no User-Agent policy beyond curl's default), check its SHA-256 against the
README, and run:

  python3 -I quote_check.py KEY=path/to/article.xml [KEY=path ...]

Text layer: block tags (p, sec, title, caption, tr, abstract, label) become a line break, every other tag is removed,
entities are unescaped, runs of whitespace collapse to one space. Table cells therefore run together, which is why the
Table 1 quotation has no space between cells. The quotations were NOT hand-corrected: a quote that does not match
fails. Exit code 1 if any fails.
"""
import sys as _sys
if len(_sys.argv) > 1 and _sys.argv[1] in ('-h', '--help'):
    print(__doc__)
    raise SystemExit(0)

import csv, hashlib, html, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def text_layer(path):
    t = Path(path).read_text(encoding="utf8")
    t = re.sub(r"<(/?)(p|sec|title|caption|tr|abstract|label)\b[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\s+", " ", html.unescape(t))


def main(argv):
    srcs = dict(a.split("=", 1) for a in argv)
    texts = {k: text_layer(v) for k, v in srcs.items()}
    for k, v in srcs.items():
        print(f"{k}\tsha256 {hashlib.sha256(Path(v).read_bytes()).hexdigest()}")
    bad = 0
    with open(HERE / "locators.tsv", encoding="utf8", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            q = re.sub(r"\s+", " ", r["verbatim_quote"])
            if r["source_key"] not in texts:
                print(f"{r['id']}\tSOURCE_NOT_SUPPLIED\t{r['source_key']}")
                bad += 1
                continue
            hit = q in texts[r["source_key"]]
            print(f"{r['id']}\t{'MATCH' if hit else 'NO_MATCH'}")
            bad += 0 if hit else 1
    print(f"failures: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
