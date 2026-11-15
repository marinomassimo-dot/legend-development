#!/usr/bin/env python3
"""RP-004 (ADV-011): mechanical check of verbatim.tsv against the saved PMC article page of PMID 18620777, and a string
search for what the body does NOT contain (the second route for every absence claim in README.md).

Every `verbatim` text must occur in the page after the same normalisation on both sides (script/style removed, tags
replaced by a space, entities unescaped, whitespace collapsed, and the space the link markup leaves inside
parentheses and before closing punctuation removed). The absence terms are searched in the body only (before
the reference list). Prints one line per row, the digest of the page, and PASS/FAIL; exit 1 on any miss. It does not judge
what a sentence means, and a count of 0 is a count of strings, not a finding about the paper's figures (images).
Run: python3 -I verify_quotes.py <page.html> [verbatim.tsv]      (--help prints this text)
The page is third-party text kept under files/ (gitignored); its digest is in access.tsv.
"""
import csv
import hashlib
import html
import os
import re
import sys

ABSENT = [
    ("phospho-c-Jun / phospho-JNK readout", r"phospho-?\s?c-?jun|p-?c-?jun|phospho-?\s?jnk|p-?jnk|phosphorylated jnk"),
    ("genetic JNK control", r"jnk1?\s?(sirna|shrna|knock|dominant)|dominant[- ]negative|jnk[12]? (null|deficient|mutant)"),
    ("second JNK inhibitor", r"sp600125|jnk inhibitor ii|ly294002|d-jnki|jnk-in-8|aeg3482"),
    ("replicate count or test named", r"triplicate|independent experiment|n ?= ?\d|student|anova|mann|wilcoxon|error bar|± ?s|sem\b|standard (deviation|error)"),
    ("dose-response", r"dose[- ]response|ic50|concentrations of sp|µm sp|um sp"),
    ("neuronal or non-cancer functional cell", r"neuron|neural|primary hepatocyte|fibroblast|astrocyte|hepatocytes? (were|was)"),
]


def norm(raw):
    raw = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", "", raw)
    raw = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    raw = re.sub(r"\s+", " ", raw).strip()
    # the page puts link markup around citation numbers and figure references: "( 48 )" must equal "(48)"
    return re.sub(r"\s+([,.;:)])", r"\1", re.sub(r"\(\s+", "(", raw))


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 2:
        print(__doc__)
        return 0
    page = sys.argv[1]
    table = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "verbatim.tsv")
    data = open(page, "rb").read()
    text = norm(data.decode("utf-8", "replace"))
    print(f"page sha256 {hashlib.sha256(data).hexdigest()} bytes {len(data)} normalised chars {len(text)}")
    bad = 0
    with open(table, encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            ok = norm(row["verbatim"]) in text
            bad += 0 if ok else 1
            print(f"{row['id']}\t{'FOUND' if ok else 'MISSING'}")
    cut = text.rfind(" REFERENCES ")
    body = text[: cut if cut > 0 else len(text)]
    print(f"body (before the reference list): {len(body)} chars")
    for label, pat in ABSENT:
        hits = [m.group(0) for m in re.finditer(pat, body, flags=re.I)]
        print(f"ABSENCE\t{label}\t{len(hits)} hit(s)\t{sorted(set(h.lower() for h in hits))[:6]}")
    print("PASS" if not bad else f"FAIL: {bad} verbatim row(s) missing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
