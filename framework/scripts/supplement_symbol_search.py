#!/usr/bin/env python3
"""Search every text-readable supplementary file on disk for gene or protein symbols, with row context.

WHY THIS EXISTS (2026-10-21, scientist-b, repurposing batch R2)
---------------------------------------------------------------
A full-text index (Europe PMC, PubMed) does not reach supplementary tables. The question
"does any WWOX-deficient dataset we already hold list a T-type channel gene" was therefore
answered "no" by every index query, and the answer was false: the hippocampal differential-
expression sheet of one supplementary workbook lists CACNA1G (up) and CACNA1H (down). The
authors never mention either gene in the text. The shared `files/supplement/` tree holds the
workbooks; nothing in the repository searched them. A zero from the full-text index is a statement
about the index (dismissal ledger D-37); this tool is the other half of that question.

WHAT IT DOES
------------
Walks `files/supplement/` (under --workspace, default the repository root or the shared checkout),
opens `.xlsx`/`.xlsm` (every sheet, with the sheet name and the row's cells), `.docx` (paragraph
text), and `.csv`/`.tsv`/`.txt`, and prints each file that contains one of the symbols, with the
sheet and the row. Matching is whole-token and case-insensitive. It reads; it writes nothing.

WHAT IT CANNOT SEE
------------------
PDF supplements (no text layer is read here: use the extracted `*_pdftotext.txt` if one exists),
images, and a symbol a sheet spells another way (aliases, Ensembl-only tables). A zero is a
statement about these files on this disk on this date, never about the literature.

  python3 framework/scripts/supplement_symbol_search.py CACNA1G CACNA1H CACNA1I [--workspace DIR] [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

TEXT_EXT = {".csv", ".tsv", ".txt"}
ZIP_EXT = {".xlsx", ".xlsm", ".docx"}


def _strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    raw = zf.read("xl/sharedStrings.xml").decode("utf-8", "replace")
    return ["".join(re.findall(r"<t[^>]*>([^<]*)</t>", si)) for si in re.findall(r"<si>(.*?)</si>", raw, flags=re.S)]


def _sheet_names(zf: zipfile.ZipFile) -> dict[str, str]:
    wb = zf.read("xl/workbook.xml").decode("utf-8", "replace")
    rels = zf.read("xl/_rels/workbook.xml.rels").decode("utf-8", "replace")
    target = {}
    for rel in re.findall(r"<Relationship\b[^>]*>", rels):
        i = re.search(r'Id="([^"]+)"', rel)
        t = re.search(r'Target="([^"]+)"', rel)
        if i and t:
            target[i.group(1)] = t.group(1).lstrip("/").replace("xl/", "")
    out = {}
    for tag in re.findall(r"<sheet\b[^>]*>", wb):
        n = re.search(r'name="([^"]+)"', tag)
        r = re.search(r'r:id="([^"]+)"', tag)
        if n and r and r.group(1) in target:
            out["xl/" + target[r.group(1)]] = n.group(1)
    return out


def search_xlsx(path: Path, rx: re.Pattern) -> list[dict]:
    hits: list[dict] = []
    with zipfile.ZipFile(path) as zf:
        strs = _strings(zf)
        for part, sheet in _sheet_names(zf).items():
            if part not in zf.namelist():
                continue
            xml = zf.read(part).decode("utf-8", "replace")
            for row in re.findall(r"<row\b[^>]*>(.*?)</row>", xml, flags=re.S):
                cells = []
                for col, attr, val in re.findall(r'<c r="([A-Z]+)\d+"([^>]*)>(?:<f>.*?</f>)?<v>([^<]*)</v>', row):
                    cells.append((col, strs[int(val)] if 't="s"' in attr and val.isdigit() and int(val) < len(strs) else val))
                if any(rx.search(v) for _, v in cells):
                    hits.append({"sheet": sheet, "row": cells})
    return hits


def search_docx(path: Path, rx: re.Pattern) -> list[dict]:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", "replace")
    out = []
    for p in re.findall(r"<w:p\b.*?</w:p>", xml, flags=re.S):
        text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
        if rx.search(text):
            out.append({"paragraph": text[:300]})
    return out


def search_text(path: Path, rx: re.Pattern) -> list[dict]:
    out = []
    for n, line in enumerate(path.read_text("utf-8", "replace").splitlines(), 1):
        if rx.search(line):
            out.append({"line": n, "text": line[:300]})
    return out


def run(symbols: list[str], root: Path) -> list[dict]:
    rx = re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(re.escape(s) for s in symbols) + r")(?![A-Za-z0-9])", re.I)
    results = []
    base = root / "files" / "supplement"
    if not base.is_dir():
        return results
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        ext = path.suffix.lower()
        try:
            if ext in (".xlsx", ".xlsm"):
                h = search_xlsx(path, rx)
            elif ext == ".docx":
                h = search_docx(path, rx)
            elif ext in TEXT_EXT:
                h = search_text(path, rx)
            else:
                continue
        except (zipfile.BadZipFile, KeyError, OSError):
            results.append({"file": str(path.relative_to(root)), "error": "unreadable (not a valid archive or file)"})
            continue
        if h:
            results.append({"file": str(path.relative_to(root)), "hits": h})
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("symbols", nargs="+")
    ap.add_argument("--workspace", default=None, help="root holding files/supplement (default: repository root)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    root = Path(a.workspace) if a.workspace else Path(__file__).resolve().parents[2]
    res = run(a.symbols, root)
    if a.json:
        print(json.dumps(res, indent=1))
    else:
        for r in res:
            print(r["file"], r.get("error", ""))
            for h in r.get("hits", [])[:8]:
                print("   ", json.dumps(h, ensure_ascii=False)[:400])
        print(f"{len(res)} file(s) with a match; a zero is a statement about the files on this disk, not the literature")
    return 0


if __name__ == "__main__":
    sys.exit(main())
