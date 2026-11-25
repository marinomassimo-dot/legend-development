#!/usr/bin/env python3
"""Read a supplementary .xlsx (standard library only) or .xls (through xlrd) as text, and say what was read.

Why this exists: a supplement spreadsheet is a reading surface, and the Python in this
deployment has no spreadsheet library. Two readings in one wave (2026-10-19) wrote a throwaway
reader each. This is the shared one, with the two things the throwaway ones did not do:

  * it prints, before any cell, the SHA-256 and byte count of exactly the workbook examined and
    the NAME of every sheet (a screen's verdict is read for what it screened);
  * ``--dedupe a.xlsx b.xlsx ...`` groups workbooks by SHA-256. Three deposited files labelled
    "seizure review", "background EEG review" and "neuropathologic scores" were byte-identical
    and held only the first of the three; no one looks for that unless a tool asks.

The format is decided by the first bytes, never by the name. A legacy binary ``.xls`` needs xlrd (BSD): ``python3 -I`` hides
user-installed packages, so run ``python3 -P -E`` for that, which still keeps the working and script folders off the import path
(2026-11-25: a workbook was reported unreadable while xlrd sat in the user site). A file that is neither, an HTML page saved
as ``.xls`` for instance, is named as such and not read.

A cell is its stored value: formulas are not evaluated, dates stay serial numbers, and a
shared string is resolved. A C0 control character in the output is REPORTED, never stripped
(the manifest validator refuses a text surface that carries one).

Usage:
    python3 framework/scripts/xlsx_to_text.py FILE.xlsx|FILE.xls [--max-rows N]
    python3 framework/scripts/xlsx_to_text.py --dedupe A.xlsx B.xlsx C.xlsx
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
OLE2 = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"          # the container of a legacy .xls


class NotRead(Exception):
    """The file was not read, and the message says why."""


def _sha(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), len(data)


def sheet_names(z: zipfile.ZipFile) -> list[tuple[str, str]]:
    """(display name, archive member) in workbook order."""
    wb = z.read("xl/workbook.xml").decode("utf8", "replace")
    names = re.findall(r"<sheet\b[^>]*?name=\"([^\"]*)\"[^>]*?r:id=\"([^\"]+)\"", wb)
    rels = z.read("xl/_rels/workbook.xml.rels").decode("utf8", "replace")
    target = {m[1]: m[0] for m in re.findall(r"<Relationship\b[^>]*?Target=\"([^\"]+)\"[^>]*?Id=\"([^\"]+)\"", rels)}
    target.update({m[0]: m[1] for m in re.findall(r"<Relationship\b[^>]*?Id=\"([^\"]+)\"[^>]*?Target=\"([^\"]+)\"", rels)})
    out = []
    for name, rid in names:
        t = target.get(rid, "")
        t = t.lstrip("/")
        out.append((html.unescape(name), t if t.startswith("xl/") else "xl/" + t))
    return out


def _reported(lines: list[str]) -> str:
    text = "\n".join(lines)
    n = len(_CTRL.findall(text))
    if n:
        text += f"\nCONTROL_CHARACTERS_REPORTED {n} (not stripped)"
    return text


def _xls_value(value, kind: int, xlrd) -> str:
    """The stored value as the .xlsx path prints it: a whole number without '.0', a boolean as 1 or 0, a date as its serial."""
    if kind == xlrd.XL_CELL_ERROR:
        return xlrd.error_text_from_code.get(value, f"#ERR{value}")
    if isinstance(value, float) and value.is_integer() and abs(value) < 1e15:
        return str(int(value))
    return str(value)


def _read_xls(path: Path, lines: list[str], max_rows: int | None) -> str:
    try:
        import xlrd
    except ImportError:
        raise NotRead(f"{path.name} is a legacy .xls and xlrd is not importable here. `python3 -I` (or -s) hides "
                      "user-installed packages: run `python3 -P -E` instead; if it is absent there too, it is not installed.") from None
    try:
        book = xlrd.open_workbook(str(path))
    except Exception as why:                      # xlrd raises several unrelated types on a damaged or non-Excel OLE2 file
        raise NotRead(f"{path.name}: xlrd {xlrd.__version__} could not open it: {type(why).__name__}: {why}") from None
    lines.append("SHEETS " + " | ".join(book.sheet_names()))
    for sheet in book.sheets():
        lines.append(f"## sheet {sheet.name!r} (xls, xlrd {xlrd.__version__}) rows={sheet.nrows}")
        for i in range(sheet.nrows):
            if max_rows is not None and i >= max_rows:
                lines.append(f"... {sheet.nrows - i} further rows not printed")
                break
            lines.append("\t".join(_xls_value(v, k, xlrd) for v, k in zip(sheet.row_values(i), sheet.row_types(i))))
    return _reported(lines)


def read_workbook(path: Path, max_rows: int | None = None) -> str:
    sha, size = _sha(path)
    lines = [f"WORKBOOK {path.name} sha256={sha} bytes={size}"]
    with path.open("rb") as handle:
        head = handle.read(8)
    if head == OLE2:
        return _read_xls(path, lines, max_rows)
    if not zipfile.is_zipfile(path):
        raise NotRead(f"{path.name} is neither .xlsx nor .xls (first bytes {head!r}); sha256={sha}. A saved web page or a "
                      "challenge page is not the supplement.")
    with zipfile.ZipFile(path) as z:
        strings: list[str] = []
        if "xl/sharedStrings.xml" in z.namelist():
            raw = z.read("xl/sharedStrings.xml").decode("utf8", "replace")
            strings = [html.unescape(re.sub(r"<[^>]+>", "", m)) for m in re.findall(r"<si>(.*?)</si>", raw, re.S)]
        sheets = sheet_names(z)
        lines.append("SHEETS " + " | ".join(n for n, _ in sheets))
        for name, member in sheets:
            body = z.read(member).decode("utf8", "replace")
            rows = re.findall(r"<row\b[^>]*>(.*?)</row>", body, re.S)
            lines.append(f"## sheet {name!r} ({member}) rows={len(rows)}")
            for i, row in enumerate(rows):
                if max_rows is not None and i >= max_rows:
                    lines.append(f"... {len(rows) - i} further rows not printed")
                    break
                cells = []
                for m in re.finditer(r"<c\b([^>]*?)(?:/>|>(.*?)</c>)", row, re.S):
                    attrs, inner = m.group(1), m.group(2) or ""
                    v = re.search(r"<v>(.*?)</v>", inner, re.S)
                    val = v.group(1) if v else ""
                    if 't="s"' in attrs and val.isdigit() and int(val) < len(strings):
                        val = strings[int(val)]
                    elif 't="inlineStr"' in attrs:
                        val = html.unescape(re.sub(r"<[^>]+>", "", inner))
                    cells.append(html.unescape(val) if 't="s"' not in attrs else val)
                lines.append("\t".join(cells))
    return _reported(lines)


def dedupe(paths: list[Path]) -> str:
    groups: dict[str, list[str]] = {}
    for p in paths:
        groups.setdefault(_sha(p)[0], []).append(p.name)
    out = []
    for sha, names in groups.items():
        tag = "IDENTICAL" if len(names) > 1 else "unique"
        out.append(f"{tag}  sha256={sha}  {', '.join(names)}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--dedupe", action="store_true", help="group the given workbooks by SHA-256 and stop")
    ap.add_argument("--max-rows", type=int, default=None)
    a = ap.parse_args(argv)
    paths = [Path(f) for f in a.files]
    if a.dedupe:
        print(dedupe(paths))
        return 0
    status = 0
    for p in paths:
        try:
            print(read_workbook(p, a.max_rows))
        except NotRead as why:
            print(f"NOT_READ {why}")
            status = 1
    return status


if __name__ == "__main__":
    sys.exit(main())
