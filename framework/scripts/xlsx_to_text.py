#!/usr/bin/env python3
"""Read a supplementary .xlsx as text with the standard library only, and say what was read.

Why this exists: a supplement spreadsheet is a reading surface, and the Python in this
deployment has no spreadsheet library. Two readings in one wave (2026-10-19) wrote a throwaway
reader each. This is the shared one, with the two things the throwaway ones did not do:

  * it prints, before any cell, the SHA-256 and byte count of exactly the workbook examined and
    the NAME of every sheet (a screen's verdict is read for what it screened);
  * ``--dedupe a.xlsx b.xlsx ...`` groups workbooks by SHA-256. Three deposited files labelled
    "seizure review", "background EEG review" and "neuropathologic scores" were byte-identical
    and held only the first of the three; no one looks for that unless a tool asks.

A cell is its stored value: formulas are not evaluated, dates stay serial numbers, and a
shared string is resolved. A C0 control character in the output is REPORTED, never stripped
(the manifest validator refuses a text surface that carries one).

Usage:
    python3 framework/scripts/xlsx_to_text.py FILE.xlsx [--max-rows N]
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


def read_workbook(path: Path, max_rows: int | None = None) -> str:
    sha, size = _sha(path)
    lines = [f"WORKBOOK {path.name} sha256={sha} bytes={size}"]
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
    text = "\n".join(lines)
    n = len(_CTRL.findall(text))
    if n:
        text += f"\nCONTROL_CHARACTERS_REPORTED {n} (not stripped)"
    return text


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
    for p in paths:
        print(read_workbook(p, a.max_rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
