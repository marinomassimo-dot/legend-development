#!/usr/bin/env python3
"""Read a supplementary .docx as text with the standard library only, and say what was read.

Why this exists: supplements arrive as Word files (antibody and primer tables, cohort tables,
analysis code, figure legends with embedded images) and the Python in this deployment has no
Word library. One lot (2026-10-20) wrote a throwaway reader for four different supplements and
declared its extractor by hand each time. This is the shared one, with the things the throwaway
did not do:

  * it prints, before any text, the SHA-256 and byte count of exactly the document examined;
  * it counts paragraphs, tables and rows and LISTS every embedded media member (name and size),
    because a legend-only reading of a figure document is a coverage fact (captions_only), and a
    reader should see how many images stayed unopened;
  * table rows are written one per line with cells joined by " | ", tab and line-break runs
    become a space or a newline, and a text box or a tracked deletion is not silently merged;
  * a C0 control character in the output is REPORTED, never stripped (the manifest validator
    refuses a text surface that carries one).

Formatting, comments, headers and footers are not read; ``--parts`` also lists every archive
member so that omission is visible. Nothing is evaluated.

Usage:
    python3 framework/scripts/docx_to_text.py FILE.docx [--out OUT.txt] [--parts]
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import sys
import zipfile
from pathlib import Path

_CTRL = re.compile(r"[\x00-\x08\x0b-\x1f]")
_SEG = re.compile(r"<w:tr[ >].*?</w:tr>|<w:p[ >].*?</w:p>", re.S)


def _runs(xml: str) -> str:
    """Visible text of one paragraph or cell: w:t runs, tabs and breaks; deleted text excluded."""
    xml = re.sub(r"<w:del\b.*?</w:del>", "", xml, flags=re.S)
    xml = re.sub(r"<w:tab\s*/>", "\t", xml)
    xml = re.sub(r"<w:(?:br|cr)\b[^>]*/>", "\n", xml)
    xml = re.sub(r"</w:p>", "\n", xml)
    text = html.unescape(re.sub(r"<[^>]+>", "", xml))
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\s*\n\s*", " / ", text).strip(" /")


def read_docx(path: Path, parts: bool = False) -> str:
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        body = z.read("word/document.xml").decode("utf8", "replace")
        media = [(n, z.getinfo(n).file_size) for n in names if n.startswith("word/media/")]
    lines: list[str] = []
    n_par = n_tbl = n_row = 0
    n_tbl = len(re.findall(r"<w:tbl>", body))
    for m in _SEG.finditer(body):
        seg = m.group(0)
        if seg.startswith("<w:tr"):
            n_row += 1
            cells = [_runs(c) for c in re.findall(r"<w:tc>.*?</w:tc>", seg, flags=re.S)]
            lines.append(" | ".join(cells))
        else:
            t = _runs(seg)
            if t:
                n_par += 1
                lines.append(t)
    head = [f"DOCX {path.name} sha256={sha} bytes={len(data)}",
            f"COUNTS paragraphs={n_par} tables={n_tbl} table_rows={n_row} embedded_media={len(media)}"]
    for n, size in media:
        head.append(f"MEDIA {n} bytes={size} (not read as text)")
    if parts:
        head.append("PARTS " + " ".join(names))
    text = "\n".join(head + [""] + lines)
    n = len(_CTRL.findall(text))
    if n:
        text += f"\nCONTROL_CHARACTERS_REPORTED {n} (not stripped)"
    return text


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("file")
    ap.add_argument("--out", help="write the text here as well as printing the header")
    ap.add_argument("--parts", action="store_true", help="list every archive member")
    a = ap.parse_args(argv)
    text = read_docx(Path(a.file), a.parts)
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="utf8")
        print("\n".join(text.splitlines()[:2]))
        print(f"written {a.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
