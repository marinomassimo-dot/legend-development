#!/usr/bin/env python3
"""Are the figure captions inside the `<body>` of the surface you are about to declare?

🔴 This asks a READING question, not a verification one, and the difference is the whole
point. `deepdive_manifest._xml_surfaces` walks the ARTICLE and separates only the abstract,
so a caption locator verifies wherever the caption sits — the contract is sound and this
script does not police it. What it policies is the surface an agent actually reads: an
extractor scoped to `<body>` shows no caption at all on some deposits, raises no error, and
returns text that reads as complete. The manifest still passes, because a validator checks
what you QUOTED, not what you were able to SEE.

Measured 2026-08-10 on the shared checkout: 7 of 34 parseable XML surfaces place every one
of their `<fig>` elements outside `<body>`, and 2 more place some of them there. One of the
seven is `PMID 24308844`, read here through a body-scoped extractor — its manifest carries
seven figure entries and not one caption locator, an absence that looked like a budget
choice and was a surface nobody had seen. Two of the corpus's sharpest findings came from
captions: an inverted agent name, and the word "Hypothetical" on a model figure.

Two rules this script exists to keep executable rather than remembered:

- **The predicate is printed, not implied.** Two counts that do not name their definition
  are not in disagreement — they are not yet comparable. A first census of this class by
  another actor reported a different number and a second reported another; neither had
  written down what it counted, and one had measured the wrong tree entirely.
- **The root is a required argument and is echoed back.** That census was wrong because a
  shell had inherited a worktree's cwd. `files/` is gitignored, so it exists in exactly one
  checkout, and a relative path measures whatever tree you happen to be standing in.

🔴 Count elements by TAG NAME, never by regex over the markup. A competing census of this
same class used `re.findall(r"<fig\b|<figure\b", ...)` and reported five extra surfaces as
partially outside the body. `<fig\b` matches `<fig-count>`: after `fig` comes a hyphen, which
is a word boundary, so `\b` is satisfied. `<fig-count>` is a JATS metadata counter living in
`<article-meta>` — always outside the body, always exactly one — so every article with a
figure count looked like it had one caption stranded. It is the same shape as a prefix
matching inside a longer identifier: syntactically valid, pointing at the wrong thing, and
invisible to any check that only asks whether the count is well formed. A plausible count is
not a verified one, and the difference is never visible in the result — only in the predicate.
That is why this module parses and iterates by tag, and why it prints its predicate.

HTML surfaces are counted SEPARATELY and never folded into the denominator: a page has
exactly one `<body>` and everything is inside it by construction, so "figures outside the
body" is not false for an HTML surface, it is undefined. Summing them dilutes a risk class
with cases that cannot belong to it.
"""
import argparse
import glob
import os
import sys
import xml.etree.ElementTree as ET


def census(root: str) -> dict:
    """Count `<fig>` inside `<body>` against `<fig>` anywhere in the article."""
    rows, broken, empty = [], [], []
    for path in sorted(glob.glob(os.path.join(root, "files/fulltext/*.xml"))):
        name = os.path.basename(path)
        try:
            article = ET.parse(path).getroot()
        except ET.ParseError as exc:
            broken.append((name, f"unparseable: {exc}"))
            continue
        body = article.find(".//body")
        if body is None:
            # Not this class and worse: a surface that answers 200 and carries no text.
            # `PMID 42395553` and `PMID 18487609` are both metadata dressed as full text.
            empty.append(name)
            continue
        rows.append((name, len(list(body.iter("fig"))), len(list(article.iter("fig")))))
    return {
        "rows": rows,
        "broken": broken,
        "absent_body": empty,
        "html": [os.path.basename(p)
                 for p in sorted(glob.glob(os.path.join(root, "files/fulltext/*.html")))],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("root", help="absolute path to the checkout whose files/ holds the "
                                     "artifacts — required, and echoed back")
    args = parser.parse_args()
    root = os.path.abspath(args.root)

    print(f"root      = {root}")
    print("predicate = inbody |{fig in descendants(body)}| vs total |{fig in "
          "descendants(article)}|\n")

    result = census(root)
    rows = result["rows"]
    pure = [r for r in rows if r[2] > 0 and r[1] == 0]
    partial = [r for r in rows if r[2] > 0 and 0 < r[1] < r[2]]
    clean = [r for r in rows if r[2] > 0 and r[1] == r[2]]
    nofigs = [r for r in rows if r[2] == 0]

    print(f"XML surfaces parsed        : {len(rows)}")
    print(f"  all captions in <body>   : {len(clean)}")
    print(f"  SOME captions outside    : {len(partial)}")
    print(f"  ALL captions outside     : {len(pure)}")
    print(f"  no figures at all        : {len(nofigs)}")
    print(f"XML with no <body> at all  : {len(result['absent_body'])}  "
          f"{result['absent_body']}")
    print(f"XML unparseable            : {len(result['broken'])}  "
          f"{[b[0] for b in result['broken']]}")
    print(f"HTML surfaces (separate, question does not apply) : {len(result['html'])}\n")

    print("ALL CAPTIONS OUTSIDE <body> — read the captions separately or change route:")
    for name, inb, tot in pure:
        print(f"  {name:48} {inb}/{tot}")
    if partial:
        print("\nSOME captions outside <body>:")
        for name, inb, tot in partial:
            print(f"  {name:48} {inb}/{tot}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
