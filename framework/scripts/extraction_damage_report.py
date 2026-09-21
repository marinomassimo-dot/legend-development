#!/usr/bin/env python3
"""Measure what an extractor destroyed in a full-text artifact, and say which counts are admissible.

🔴 WHY THIS EXISTS
------------------
On 2026-09-21 nine papers were read through one MCP extractor and **every one of them** came back
with its italicised tokens silently deleted: gene symbols, `in vitro`/`in vivo`, the italic `P` of
every p-value, every `n`, and every inline figure and reference cross-reference. The damage is
invisible unless you look for its scars, and it produces a specific, seductive error — a string
count of zero for a gene symbol, read as the paper being silent about that gene.

It nearly reached the record twice that day. `TRAPPC6A` occurs **zero** times in the body of a
paper that is entirely about it, alongside `APOE`, `APP`, `BIN1`, `CLU` and `PICALM`; the symbol
survives intact in the same paper's PubMed abstract, which is what proved the deletion. In another
paper the knockout **genotype labels** were deleted, so which genotypes a sentence compared could
only be inferred from its grammar.

Every reader that day was warned in prose, in every brief, and one still offered italic-class
zeros as evidence. **A warning that has to be repeated nine times is a measurement that has not
been written yet.** This tool is that measurement.

WHAT IT DOES
------------
Reads an artifact and reports, per class:

  - **fused-token scars** — `thegene`, `ofmRNA`, `includingand`, `knockoutMEF`: a lowercase word
    run into the next because an italic token between them was removed. The single most reliable
    positive signature of the defect.
  - **empty cross-reference stubs** — `()`, `(,)`, `[]`, `[,]`, `(Figure)`, `(Table)`: what is
    left where a figure, table or reference pointer stood.
  - **orphaned statistics** — `(< 0.05)`, `(P<`-less comparisons, `(=3)`: the italic `P` or `n`
    deleted, leaving a bare operator.
  - **reference list present or absent** — because when it is gone, no citation attribution can be
    traced and none may be reconstructed from position or plausibility.

Then it emits a **verdict on admissibility**, which is the only thing a reader actually needs:

  ITALIC-CLASS COUNTS INADMISSIBLE — gene symbols, variant strings, in vitro/in vivo, italic P
  and n are deleted on this surface. A zero for any of them measures the instrument.
  ROMAN-CLASS COUNTS ADMISSIBLE — ordinary method words ("bafilomycin", "blinded", "cycloheximide",
  "electron microscopy") are not italicised, so a zero for one of those is informative.

It never says a paper is silent about anything. It says which questions this surface can answer.

Disease-agnostic and extractor-agnostic: it measures the text, not the tool that produced it.

Run: `extraction_damage_report.py <artifact> [<artifact> ...] [--json]`
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# The positive signature: a short FUNCTION word run straight into the next word, which is what a
# deleted italic token between them leaves behind — "thegene", "ofmRNA", "includingand",
# "knockoutMEF", "wild typeMEF". Anchoring on a closed list of function-word prefixes is what keeps
# this specific: an open-ended "lowercase run followed by a capital" also matches ordinary camelCase
# and, worse, matches INSIDE words, which would make every reported example a truncation. An
# evidence tool whose examples are artefacts of its own regex is the defect it exists to detect.
_FUNCTION = (r"the|of|in|to|for|and|or|a|an|with|by|from|that|this|these|those|"
             r"including|between|wild\s?type|knockout|human|murine|mouse|rat")
_CONTENT = r"(?:gene|genes|mRNA|cDNA|protein|proteins|cells?|mice|rats?|MEFs?|locus|knockout|" \
           r"expression|levels?|and|or|in|of)"
# function word + capitalised token (the italic symbol was between them)
FUSED = re.compile(rf"\b(?:{_FUNCTION})(?:[A-Z][A-Za-z0-9]{{1,}})\b")
# function word + lowercase content word, with no space where one belongs
FUSED_SUFFIX = re.compile(rf"\b(?:{_FUNCTION}){_CONTENT}\b")
EMPTY_PAREN = re.compile(r"\(\s*[,;]*\s*\)|\[\s*[,;]*\s*\]|\((?:Figure|Fig\.?|Table)s?\)")
ORPHAN_STAT = re.compile(r"\(\s*[<>=]\s*[0-9]|\(\s*[nN]?\s*=\s*[0-9]|[^A-Za-z]<\s*0\.[0-9]")
REFLIST = re.compile(r"(?im)^\s*(?:references|bibliography|literature cited)\s*$")

# Real English words the fused patterns can produce. Filtering them is not cosmetic: a tool that
# reports "within" as evidence of deletion teaches readers to discount its other findings.
_REAL_WORDS = {"within", "inthe", "andor", "thean", "forthe", "ofthe", "thatthe", "andin",
               "another", "anda", "thisa", "byand", "toand", "ofa", "ina", "fora", "thegene"} - {"thegene"}

ROMAN_SAFE = ("bafilomycin", "chloroquine", "cycloheximide", "blinded", "electron microscopy",
              "g-ratio", "immunoprecipitation", "rapamycin", "randomi")


def analyse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    fused = sorted(
        m for m in ({m.group(0) for m in FUSED.finditer(text)} |
                    {m.group(0) for m in FUSED_SUFFIX.finditer(text)})
        if m.lower() not in _REAL_WORDS)
    empty = EMPTY_PAREN.findall(text)
    orphan = ORPHAN_STAT.findall(text)
    has_refs = bool(REFLIST.search(text))
    damaged = bool(fused) or len(empty) >= 3
    return {
        "artifact": str(path),
        "bytes": len(text.encode("utf-8")),
        "fused_token_scars": len(fused),
        "fused_examples": fused[:12],
        "empty_cross_reference_stubs": len(empty),
        "orphaned_statistics": len(orphan),
        "reference_list_present": has_refs,
        "italic_class_counts_admissible": not damaged,
        "roman_class_counts_admissible": True,
        "citation_attribution_traceable": has_refs,
        "verdict": _verdict(damaged, has_refs),
    }


def _verdict(damaged: bool, has_refs: bool) -> str:
    if not damaged:
        return ("NO ITALIC-DELETION SIGNATURE FOUND. This is not a guarantee: it means the scars "
                "this tool looks for are absent. Check a known italic token against the PubMed "
                "metadata abstract before relying on any zero.")
    tail = ("" if has_refs else
            " AND THE REFERENCE LIST IS ABSENT — no citation attribution can be traced from this "
            "surface, and none may be reconstructed from position or plausibility.")
    return ("ITALIC-CLASS COUNTS INADMISSIBLE: gene symbols, variant strings, in vitro/in vivo and "
            "the italic P and n are deleted on this surface, so a zero for any of them measures "
            "the instrument and not the paper. ROMAN-CLASS COUNTS ADMISSIBLE: ordinary method "
            "words are not italicised, so a zero for one of those is informative — say which class "
            "you are counting, every time." + tail)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("artifacts", nargs="+")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv[1:])

    reports = []
    for name in args.artifacts:
        path = Path(name)
        if not path.is_file():
            print(f"REFUSED: not a file: {name}", file=sys.stderr)
            return 1
        reports.append(analyse(path))

    if args.json:
        print(json.dumps(reports, indent=2))
        return 0
    for r in reports:
        print(f"\n{r['artifact']}  ({r['bytes']} bytes)")
        print(f"  fused-token scars ........... {r['fused_token_scars']}"
              + (f"   e.g. {', '.join(r['fused_examples'][:6])}" if r["fused_examples"] else ""))
        print(f"  empty cross-ref stubs ....... {r['empty_cross_reference_stubs']}")
        print(f"  orphaned statistics ......... {r['orphaned_statistics']}")
        print(f"  reference list .............. {'present' if r['reference_list_present'] else 'ABSENT'}")
        print(f"  VERDICT: {r['verdict']}")
    print("\nRoman-type words that are safe to count on any surface, as a reminder: "
          + ", ".join(ROMAN_SAFE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
