#!/usr/bin/env python3
"""Read the text layer of a locally-held PDF, and refuse to report a zero it has not earned.

🔴 WHY THIS EXISTS
------------------
On 2026-09-21 the operator supplied the `A9` article (PMID 35984507) and its supplementary
bundle as PDFs, after every automated route had returned a zero-length body. This deployment
has **no** PDF toolchain: `poppler`, `PyMuPDF` and `pypdf` are all absent and `pip install`
fails at interpreter level. Without an extractor the papers were unreadable, so a full text
already in hand would have stayed `EVIDENCE_BLOCKED` — which is the one failure mode
`gold_is_in_the_details.md` exists to prevent.

🔴 AND WHY IT IS NOT JUST AN EXTRACTOR
--------------------------------------
The dangerous output of a text extractor is **zero**. A search that returns no hits means one
of two entirely different things — *the paper does not contain this*, or *the tool did not
read this paper* — and they are indistinguishable from the zero alone. This repository has
already paid for that confusion once: the MCP extractor silently deletes every italicised
token, so italic-class zero counts were instrument readings being read as findings.

So `search` **will not report a query count until named positive controls have come back
non-zero**. If a control is zero the tool reports `INSTRUMENT_UNVERIFIED` and returns a
non-zero exit status, and no negative may be quoted from that run. A negative is a claim about
the paper; it has to be earned like one.

⚠️ WHAT THIS TOOL CANNOT DO, AND SO CANNOT BE CITED FOR
--------------------------------------------------------
It reads the **text layer** only.

  - **No figure panels.** Legends and axis labels come through when they are text; the image
    does not. `D-14` is unaffected by this tool: a figure-asserted negative still needs the
    image.
  - **No scanned or image-only PDF.** There is no OCR here. Such a file yields little or no
    text, which `--controls` is designed to catch rather than pass off as a reading.
  - **No table structure.** Cells arrive as a run of text in drawing order; a table is
    readable but its row/column geometry is not recovered.

Routed in `framework/scripts/README.md`. Run:

    python3 framework/scripts/pdf_text_extract.py extract PAPER.pdf --out text.txt
    python3 framework/scripts/pdf_text_extract.py search PAPER.pdf \\
        --controls 'SH-SY5Y,Western blot' --query 'siRNA,shRNA,knockout'
"""

from __future__ import annotations

import argparse
import re
import sys
import zlib
from pathlib import Path

# PDF string escapes, per PDF 32000-1 § 7.3.4.2.
_ESCAPES = {0x6E: 10, 0x72: 13, 0x74: 9, 0x62: 8, 0x66: 12, 0x28: 40, 0x29: 41, 0x5C: 92}

# Ligatures the typesetter emits as single glyphs. Left un-normalised, `significant` is
# spelled `signi<fi>cant` and a search for it returns zero — an instrument reading again.
_LIGATURES = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl",
    "ﬅ": "st", "ﬆ": "st", "‐": "-", "‑": "-", "–": "-",
    "—": "-", "‘": "'", "’": "'", "“": '"', "”": '"',
}

_TOKENS = re.compile(rb"\((?:[^()\\]|\\.)*\)|\bTJ\b|\bTj\b|\bTd\b|\bTD\b|\bT\*\b", re.S)
_STREAM = re.compile(rb"stream\r?\n")


def _unescape(raw: bytes) -> bytes:
    """Resolve backslash escapes inside a PDF literal string."""
    out = bytearray()
    i = 0
    while i < len(raw):
        char = raw[i]
        if char != 0x5C or i + 1 >= len(raw):
            out.append(char)
            i += 1
            continue
        nxt = raw[i + 1]
        if nxt in _ESCAPES:
            out.append(_ESCAPES[nxt])
            i += 2
        elif 0x30 <= nxt <= 0x37:
            j = i + 1
            digits = b""
            while j < len(raw) and 0x30 <= raw[j] <= 0x37 and len(digits) < 3:
                digits += bytes([raw[j]])
                j += 1
            out.append(int(digits, 8) & 0xFF)
            i = j
        else:
            i += 2
    return bytes(out)


def _strings_from(stream: bytes) -> str:
    """Pull show-text operands out of one inflated content stream, in drawing order."""
    parts: list[str] = []
    for match in _TOKENS.finditer(stream):
        token = match.group(0)
        if token.startswith(b"("):
            parts.append(_unescape(token[1:-1]).decode("latin-1"))
        elif token in (b"Td", b"TD", b"T*"):
            parts.append("\n")
    return "".join(parts)


def raw_text(path: Path) -> str:
    """Inflate every FlateDecode content stream carrying show-text operators."""
    data = path.read_bytes()
    chunks: list[str] = []
    for match in _STREAM.finditer(data):
        start = match.end()
        end = data.find(b"endstream", start)
        if end < 0:
            continue
        blob = data[start:end]
        try:
            inflated = zlib.decompress(blob)
        except zlib.error:
            try:
                inflated = zlib.decompressobj().decompress(blob)
            except zlib.error:
                continue
        if b"Tj" in inflated or b"TJ" in inflated:
            chunks.append(_strings_from(inflated))
    return "\n".join(chunks)


# Word-generated PDFs emit a BCP-47 language tag as a literal show-text string before every
# run, so the supplementary of PMID 35984507 extracts as
# `WWOXen-US-en-USmitochondriaen-USinteractions`. Single words still match through it; a
# PHRASE does not, which would make every phrase-level negative in such a file a false
# negative — the exact failure this tool exists to prevent. The tag is removed only where it
# is glued to surrounding text, so a genuine `en-US` standing alone as data survives.
_LANG_TAG = re.compile(r"(?<=[^\s])(?:en|fr|de|es|it|pt|nl|sv|da|nb|fi|pl|ru|zh|ja|ko)"
                       r"-[A-Z]{2}(?=[^\s])")


def normalise(text: str) -> str:
    """De-hyphenate across line breaks and fold ligatures, so a search can find a word."""
    for glyph, plain in _LIGATURES.items():
        text = text.replace(glyph, plain)
    text = _LANG_TAG.sub("", text)
    # `mito-\nchondrial` is one word wherever a reader is concerned.
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    return text


def prose(text: str, *, max_segment: int = 4000, alpha_floor: float = 0.72) -> str:
    """Deduplicate and drop font-program noise, leaving the article's readable body.

    A PDF's content streams repeat heavily (shared resources, re-drawn page furniture), and
    the same inflate pass also catches embedded font programs, which are binary. Segments are
    kept when they are mostly letters and spaces, so what survives is what a person reads.

    ⚠️ This is a **convenience view, not the record**. `extract` without `--prose` is the
    honest artefact to fingerprint in a receipt, because this filter can drop a
    number-dense methods line. The A9 read used the unfiltered text for every negative.
    """
    seen: set[str] = set()
    kept: list[str] = []
    for segment in re.split(r"(?<=[.;])\s+|\n", text):
        segment = segment.strip()
        if not segment or len(segment) > max_segment:
            continue
        key = re.sub(r"\W+", "", segment)[:120]
        if not key or key in seen:
            continue
        seen.add(key)
        alpha = sum(char.isalpha() or char.isspace() for char in segment)
        if len(segment) > 20 and alpha / len(segment) > alpha_floor:
            kept.append(segment)
    return "\n".join(kept)


# Bytes that are not text. An inflate pass over a PDF also catches embedded font programs and
# image data, and a *tolerant* matcher run across those will manufacture hits: on 2026-09-21 a
# search for `S8G` (the inactive Zfra control peptide) returned 1 from the byte run
# `s\x128G` inside an image stream, and that single false positive was on its way into a
# reading as evidence that the control existed. A tolerance wide enough to bridge typesetting
# is wide enough to bridge binary, so the binary is removed before the tolerance is applied.
_NONTEXT = re.compile(r"[^\x09\x0a\x0d\x20-\x7e\u00a0-\u024f]+")

# What may sit between two characters of a term and still be the same word: line wrapping,
# inter-glyph spacing and hyphenation. NOT arbitrary non-word bytes.
_TOLERANCE = r"[\s\-\u00ad]*"


# A run of non-text becomes a BARRIER, not a space. Substituting a space was the first fix
# tried on 2026-09-21 and it did not work: `s\x128G` became `s 8G`, and a tolerance that
# bridges line wrapping bridges a space just as happily, so the false `S8G` survived. The
# sentinel is outside both the tolerance class and any term, so nothing matches across it.
_BARRIER = "\ufffd"


def searchable(text: str) -> str:
    """The text a count may run over: non-text runs replaced by an unbridgeable sentinel."""
    return _NONTEXT.sub(_BARRIER, text)


def count(text: str, term: str) -> int:
    """Count a term tolerantly: case, line wrapping and hyphenation do not hide it.

    🔴 The caller is expected to pass `searchable(text)`; `search` does. Counting over the raw
    inflate output fabricates hits out of font and image bytes — see `_NONTEXT`.
    """
    pattern = _TOLERANCE.join(re.escape(char) for char in re.sub(r"\s+", "", term))
    return len(re.findall(pattern, text, re.IGNORECASE))


def _split(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)

    extract = sub.add_parser("extract", help="write the normalised text layer")
    extract.add_argument("pdf", type=Path)
    extract.add_argument("--out", type=Path, help="write here instead of stdout")
    extract.add_argument("--prose", action="store_true",
                         help="deduplicated readable view; NOT the artefact to fingerprint")

    search = sub.add_parser(
        "search", help="count terms, but only after positive controls have verified the read")
    search.add_argument("pdf", type=Path)
    search.add_argument("--controls", required=True,
                        help="comma-separated terms that MUST be present; a zero here means "
                             "the tool did not read the paper, not that the paper lacks them")
    search.add_argument("--query", required=True, help="comma-separated terms to count")

    args = parser.parse_args(argv)
    if not args.pdf.is_file():
        print(f"ERROR: no such file: {args.pdf}", file=sys.stderr)
        return 2

    text = normalise(raw_text(args.pdf))

    if args.command == "extract":
        body = prose(text) if args.prose else text
        if args.out:
            args.out.write_text(body, encoding="utf-8")
            print(f"{len(body)} characters -> {args.out}")
        else:
            sys.stdout.write(body)
        return 0

    hunting = searchable(text)
    controls = {term: count(hunting, term) for term in _split(args.controls)}
    dead = [term for term, hits in controls.items() if hits == 0]
    print("positive controls:")
    for term, hits in controls.items():
        print(f"  {'OK ' if hits else 'DEAD'}  {hits:>6}  {term}")
    if dead:
        print("\nINSTRUMENT_UNVERIFIED: control(s) returned zero: " + ", ".join(dead))
        print("No query count is reported. A zero from an unverified extractor is a reading "
              "of the tool, not of the paper.")
        return 1

    print("\nquery:")
    for term in _split(args.query):
        print(f"  {count(hunting, term):>6}  {term}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
