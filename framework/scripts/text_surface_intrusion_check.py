#!/usr/bin/env python3
"""Detect page furniture that has landed INSIDE a sentence in an extracted text surface.

WHY THIS EXISTS, and it is not hypothetical.

On 2026-09-09 a reading of PMID 21731849 — a two-column article with no structured surface —
extracted its text with ``pdftotext -layout``. ``-layout`` preserves the *visual* layout, which
on a two-column page means it interleaves the two columns line by line. The sentence carrying
the paper's headline claim came out as::

    Using this protocol, osteosarcomas are detected in
    588
    100% of the post-natal mice prior to their death.

``588`` is the page number. It is not in that sentence on the page; it is at the foot of it.

A locator quoted across that point would have been verified against the declared artifact and
**passed**, while matching a character sequence no author ever wrote. That is precisely the
failure ``gold_is_in_the_details`` rule 5c names as the worst class this system can produce,
because it is silent and wears the badge of having been checked. The reading caught it by
comparing against the rendered page — a human act that does not scale and that nobody is
obliged to repeat.

So the hazard gets a check. This module answers ONE mechanical question about an extracted
text surface: *are there places where page furniture sits inside a continuing sentence?* Every
such place is a span across which a verbatim quote must not be taken.

WHAT IT DOES NOT CLAIM. It does not detect corrupted characters — ``_refuse_suspect_surface``
in ``deepdive_manifest.py`` owns that, and the two are independent: a surface can be perfectly
encoded and still be interleaved. It does not prove a surface is safe; absence of intrusions
means only that this signature was not found. And it does not repair anything — repairing an
extraction by hand is the move rule 5d forbids. Re-extract in reading order instead
(``pdftotext -nopgbrk`` without ``-layout``), or anchor the affected locators to the page.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys

# A line that is nothing but a small integer is page furniture, not prose. Four digits covers
# journals that number continuously through a volume; more than that and it is likelier data.
PAGE_NUMBER_RE = re.compile(r"^\s*(\d{1,4})\s*$")

# A sentence that has ended does so with terminal punctuation, allowing a closing quote or
# bracket after it. Anything else means the sentence was still running when the line broke.
SENTENCE_END_RE = re.compile(r"[.!?][\"')\]]?\s*$")

# A continuation starts lowercase, or with a digit/percent — "100% of the post-natal mice".
# It does NOT start with a capital, which would suggest a fresh sentence.
CONTINUATION_RE = re.compile(r"^\s*[a-z0-9(\[]")

# How many times a line must repeat before it counts as a running header/footer rather than
# a sentence that happens to recur.
HEADER_MIN_REPEATS = 3
HEADER_MAX_WORDS = 14

# 🔴 How widely a repeated line must be SPREAD through the document before it counts as page
# furniture. Added 2026-09-09 after the second production run, on PMID 18460020, where the
# gap-based exclusion below was defeated: see _running_headers.
HEADER_MIN_SPREAD = 0.25



def _significant_lines(text: str) -> list[tuple[int, str]]:
    """Return (line_number, line) for non-blank lines, 1-based."""
    out: list[tuple[int, str]] = []
    for number, line in enumerate(text.splitlines(), 1):
        if line.strip():
            out.append((number, line))
    return out


# A table row rendered as text is columns separated by wide gaps. Two or more such gaps is a
# reliable signature and keeps repeated table rows out of the running-header set.
TABLE_ROW_RE = re.compile(r"\S {3,}\S.* {3,}\S")


def _running_headers(lines: list[tuple[int, str]]) -> set[str]:
    """Lines that repeat often enough, are short enough, and are SPREAD widely enough to be
    page furniture.

    🔴 Refined twice, and only ever after a production run, which is the only reason either
    refinement is right.

    FIRST (PMID 20530675 supplement, a document of tables): repeated TABLE ROWS
    ('Lung  M  S  +') were reported as running headers. A table row is recognisable by its wide
    inter-column gaps, so rows are excluded via TABLE_ROW_RE rather than the repeat threshold
    being raised, which would have silenced genuine headers on short papers instead.

    SECOND (PMID 18460020, 2026-09-09): that exclusion was DEFEATED, and the way it failed is
    the useful part. TABLE_ROW_RE looks for wide inter-column gaps, which exist only when the
    extractor emits a whole table row on one line. PyMuPDF's get_text() emits ONE CELL PER LINE,
    so a table's cells arrive as short repeated lines with NO gaps to detect, and Table 1's
    values ('3 (9%)', 'Negative', 'Positive') were reported as running headers — 25 false
    positives on a 7-page paper, which is enough noise to make a reader ignore the real ones.

    The discriminator is DISPERSION, and it was chosen by measuring both classes rather than
    guessed. Page furniture recurs once per page, so its occurrences span most of the document;
    table cells recur densely inside one block. Measured over the two papers:

        genuine furniture   span 53.7%-111.5% of the document
        table cell values   span  2.7%-  7.6%

    A threshold of 25% sits in an empty band an order of magnitude wide on either side.

    🔴 THE RATIO IS DELIBERATE AND AN ABSOLUTE LINE FLOOR WAS TRIED AND REJECTED. A floor of
    100 lines ("furniture must cross about a page") separates the measured classes just as
    cleanly, and it silenced the suite's OLDEST regression - the real PMID 21731849 header,
    whose fixture is a short extract. Breaking a genuine existing regression to remove a false
    positive is the wrong trade, so the ratio stands alone. Its own known limit, declared
    rather than hidden: on a SHORT document a table can honestly occupy more than a quarter of
    the text and would be reported again. The defect measured in production was on 7- and
    10-page papers, and there the bands do not overlap.

    🔴 Dispersion, not the median gap between occurrences, and the counterexample decided it:
    the separator '|' of 'Cancer Sci | July 2008 | vol. 99 | no. 7' is genuine furniture with a
    span of 70.2% and a median gap of 2.0, because the pieces of one header line arrive
    together. A gap-based test would have discarded real furniture to remove false furniture.
    """
    if not lines:
        return set()
    first_line, last_line = lines[0][0], lines[-1][0]
    extent = max(last_line - first_line, 1)

    positions: dict[str, list[int]] = {}
    for number, line in lines:
        if len(line.split()) > HEADER_MAX_WORDS or TABLE_ROW_RE.search(line):
            continue
        stripped = line.strip()
        if stripped:
            positions.setdefault(stripped, []).append(number)

    return {
        text
        for text, seen in positions.items()
        if len(seen) >= HEADER_MIN_REPEATS
        and not PAGE_NUMBER_RE.match(text)
        and (seen[-1] - seen[0]) / extent >= HEADER_MIN_SPREAD
    }


def _page_numbers(lines: list[tuple[int, str]]) -> set[str]:
    """Bare integers that actually behave like page numbers.

    🔴 Also refined after the first production run. The first version treated ANY bare integer
    line as a page number, and on a figure-heavy supplement it duly reported chart axis ticks —
    '80', '70', '60' — as page furniture. They are not, and a checker that cries wolf on every
    bar chart is a checker that gets switched off.

    A page number is part of a *numbering*: in document order the values step upward by one at
    least twice. Axis ticks descend, or step by ten, or repeat; none of them form that chain.
    Requiring the chain costs nothing on a real paper, whose page numbers are consecutive by
    construction, and removes the whole false-positive class.
    """
    ordered: list[tuple[int, str]] = []
    for _, line in lines:
        match = PAGE_NUMBER_RE.match(line)
        if match:
            ordered.append((int(match.group(1)), match.group(1)))

    in_chain: set[str] = set()
    for start in range(len(ordered)):
        chain = [ordered[start]]
        for candidate in ordered[start + 1 :]:
            if candidate[0] == chain[-1][0] + 1:
                chain.append(candidate)
        if len(chain) >= 3:
            in_chain.update(text for _, text in chain)
    return in_chain


def find_intrusions(text: str) -> list[dict]:
    """Find page furniture sitting between two halves of a continuing sentence.

    The test is deliberately conservative and needs all three conditions, because each one
    alone is common and harmless:

    1. the intruding line is page furniture — a bare integer belonging to a consecutive
       numbering chain (see ``_page_numbers``), or a non-tabular line that repeats at least
       ``HEADER_MIN_REPEATS`` times in this document (see ``_running_headers``);
    2. the previous prose line does NOT end a sentence;
    3. the next prose line CONTINUES one — it starts lowercase, or with a digit.

    A page number that falls between two complete sentences is ordinary and is not reported:
    no quote can be damaged by it.
    """
    lines = _significant_lines(text)
    headers = _running_headers(lines)
    pages = _page_numbers(lines)
    findings: list[dict] = []

    for index in range(1, len(lines) - 1):
        line_number, line = lines[index]
        stripped = line.strip()

        page_match = PAGE_NUMBER_RE.match(line) and stripped in pages
        is_header = stripped in headers
        if not page_match and not is_header:
            continue

        # Walk outward past any further furniture, so a page-number + running-header pair
        # is reported once with the real prose on both sides.
        def is_furniture(candidate: str) -> bool:
            stripped_candidate = candidate.strip()
            return stripped_candidate in pages or stripped_candidate in headers

        before = index - 1
        while before >= 0 and is_furniture(lines[before][1]):
            before -= 1
        after = index + 1
        while after < len(lines) and is_furniture(lines[after][1]):
            after += 1
        if before < 0 or after >= len(lines):
            continue

        previous = lines[before][1].rstrip()
        following = lines[after][1]

        if SENTENCE_END_RE.search(previous):
            continue
        if not CONTINUATION_RE.match(following):
            continue

        findings.append(
            {
                "line": line_number,
                "intrusion": stripped,
                "kind": "page_number" if page_match else "running_header",
                "before": previous.strip()[-90:],
                "after": following.strip()[:90],
                "reconstructed": f"{previous.strip()[-90:]} {following.strip()[:90]}",
            }
        )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Detect page furniture inside a sentence in an extracted text surface. "
            "Exit 1 when any is found: a verbatim locator must not be quoted across such a span."
        )
    )
    parser.add_argument("text_file", help="the declared article_text artifact")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    try:
        with open(args.text_file, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as exc:
        print(f"ERROR: cannot read {args.text_file}: {exc}", file=sys.stderr)
        return 2

    findings = find_intrusions(text)

    if args.as_json:
        print(json.dumps({"file": args.text_file, "intrusions": findings}, indent=1))
    else:
        if not findings:
            print(
                f"OK: no page furniture found inside a sentence in {args.text_file}. "
                "This is not proof the surface is faithful — only that this signature is absent."
            )
        else:
            print(
                f"INTRUSION: {len(findings)} place(s) in {args.text_file} where page furniture "
                "sits inside a continuing sentence. Do NOT quote a locator across these spans; "
                "re-extract in reading order (pdftotext -nopgbrk, without -layout) or anchor to "
                "the rendered page. Never hand-correct the surface."
            )
            for found in findings:
                print(
                    f"  line {found['line']}: {found['kind']} {found['intrusion']!r}\n"
                    f"    reads as: ...{found['reconstructed']}..."
                )
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
