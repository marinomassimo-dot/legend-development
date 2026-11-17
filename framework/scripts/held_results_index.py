#!/usr/bin/env python3
"""Which held result speaks about gene X? A DERIVED index of the RESULT sections of the prediction and analysis notes of a dataset folder, keyed by gene symbol.

Why it exists (2026-11-17, ADV-023): a held result filed by dataset folder (`gse156243/prediction_wnt_sign_20261025.md`) was not reached from the text of a prediction about
WNT5A by any of ten routes (0 of 10 before a README pointer). The surfaces a searcher starts from are filed by paper, need or record, not by gene.

What it is: one pass over the markdown notes of the dataset folders that have a `# RESULT` section; a symbol is a token declared in a gene-set, readout, calculation or
marker section of the same folder (or in `marker_sets_declared.tsv`); a row is one paragraph of a RESULT section that names it, with file, line, accession, and the
words `up`/`down` found IN THAT SENTENCE (a line label, not a reading of the result). It never edits a source; the markdown file it writes is derived and never a source of
record. `build --write` regenerates it, `check` fails if the stored copy differs from a rebuild, `lookup SYMBOL` prints from a live rebuild (so it is never stale).
Limits: only RESULT sections (not the later "second analyst" sections); a symbol must have been declared in a gene-set section; gene-family names such as LDH are not excluded;
the sign words are those of the statement and can mix several genes.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FOLDERS = ["disease-models/wwox/research/drug_repurposing/gse156243"]
OUT = "disease-models/wwox/research/drug_repurposing/gse156243/HELD_RESULTS_BY_GENE_derived.md"
SYMBOL = re.compile(r"\b[A-Z][A-Z0-9]{2,9}(?:-[A-Z0-9]+)?\b")
NOT_SYMBOLS = {"CPM", "PDH", "LDH", "ISR", "UPR", "RNA", "DNA", "THE", "AND", "NOT", "FDR", "UMI"}
DECLARING = re.compile(r"gene sets?|fixed readout|the calculation|marker", re.I)
ACCESSION = re.compile(r"\b(?:GSE\d+|E-MTAB-\d+)\b")
UP = re.compile(r"\b(?:up|raised|higher|elevated|increased?)\b", re.I)
DOWN = re.compile(r"\b(?:down|lower|reduced|decreased?)\b", re.I)
HEAD = re.compile(r"^(#{1,6}) +(.*)$")


def _sections(lines: list[str]) -> list[tuple[int, str, int, int]]:
    """(level, title, first body line, end line exclusive): a section runs to the next heading of the same or a higher level."""
    heads = [(i, len(m.group(1)), m.group(2)) for i, l in enumerate(lines) if (m := HEAD.match(l))]
    out = []
    for n, (i, level, title) in enumerate(heads):
        end = next((j for j, lv, _ in heads[n + 1:] if lv <= level), len(lines))
        out.append((level, title, i + 1, end))
    return out


def _declared(lines: list[str], sections) -> set[str]:
    found: set[str] = set()
    for _level, title, a, b in sections:
        if DECLARING.search(title):
            for line in lines[a:b]:
                found.update(t for t in SYMBOL.findall(line.split(":", 1)[-1]) if t not in NOT_SYMBOLS)
    return found


def _sign(text: str) -> str:
    up, down = bool(UP.search(text)), bool(DOWN.search(text))
    return "both" if up and down else "up" if up else "down" if down else "none"


def build(root: Path = ROOT) -> list[dict[str, str]]:
    docs, vocab = {}, set()
    for folder in FOLDERS:
        base = root / folder
        tsv = base / "marker_sets_declared.tsv"
        if tsv.is_file():
            for row in tsv.read_text(encoding="utf-8").splitlines()[1:]:
                vocab.update(t for t in re.split(r"[,\s]+", row.split("\t")[-1]) if SYMBOL.fullmatch(t) and t not in NOT_SYMBOLS)
        for path in sorted(base.glob("*.md")):
            lines = path.read_text(encoding="utf-8").splitlines()
            secs = _sections(lines)
            vocab |= _declared(lines, secs)
            docs[path] = (lines, secs)
    rows = []
    for path, (lines, secs) in docs.items():
        found = ACCESSION.search("\n".join(lines[:8]))
        accession = found.group(0) if found else path.parent.name
        for level, title, a, b in secs:
            if not title.upper().startswith("RESULT"):
                continue
            start = a
            while start < b:
                while start < b and not lines[start].strip():
                    start += 1
                end = start
                while end < b and lines[end].strip() and not HEAD.match(lines[end]):
                    end += 1
                para = " ".join(l.strip() for l in lines[start:end])
                for sym in sorted(set(SYMBOL.findall(para)) & vocab):
                    at = para.find(sym)
                    begin = max(para.rfind(". ", 0, at) + 2, 0)
                    stop = para.find(". ", at)
                    statement = para[begin:stop if stop != -1 else len(para)][:240].replace("|", "/")      # the sentence that names it
                    rows.append({"symbol": sym, "accession": accession, "file": str(path.relative_to(root)), "line": str(next(k for k in range(start, end) if re.search(rf"\b{re.escape(sym)}\b", lines[k])) + 1), "section": title[:60].replace("|", "/"),
                                 "words": _sign(statement), "statement": statement})
                start = max(end, start + 1)
    return sorted(rows, key=lambda r: (r["symbol"], r["file"], int(r["line"])))


def render(rows: list[dict[str, str]]) -> str:
    head = ("# Held results by gene symbol — DERIVED INDEX, not a source of record\n\n"
            "Rebuilt from the RESULT sections of the notes of this folder by `python3 framework/scripts/held_results_index.py build --write`; `check` fails when this copy differs from a rebuild. "
            "Never edit it by hand and never cite it instead of the note: the `file` and `line` columns are the source. `words` are the words up/down found in the statement, a label and not a reading "
            "(a statement can mix genes). Only RESULT sections of notes that declare a gene set are indexed; absence here is not absence of a held result.\n\n")
    table = ["| symbol | accession | file | line | section | words | statement |", "|---|---|---|---|---|---|---|"]
    table += [f"| {r['symbol']} | {r['accession']} | `{r['file']}` | {r['line']} | {r['section']} | {r['words']} | {r['statement']} |" for r in rows]
    return head + "\n".join(table) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="print the derived index; --write stores it")
    b.add_argument("--write", action="store_true")
    sub.add_parser("check", help="exit 1 if the stored copy differs from a rebuild")
    lk = sub.add_parser("lookup", help="which held result speaks about SYMBOL (live rebuild)")
    lk.add_argument("symbol")
    args = ap.parse_args(argv)
    rows = build()
    if args.cmd == "lookup":
        hit = [r for r in rows if r["symbol"] == args.symbol.upper()]
        for r in hit:
            print(f"{r['file']}:{r['line']}\t{r['accession']}\t{r['section']}\twords={r['words']}\t{r['statement']}")
        if not hit:
            print(f"no RESULT section of the indexed folders names {args.symbol.upper()} (a statement about these folders, not about the repository)")
        return 0 if hit else 1
    text = render(rows)
    if args.cmd == "build":
        if args.write:
            (ROOT / OUT).write_text(text, encoding="utf-8")
            print(f"wrote {OUT}: {len(rows)} row(s)")
        else:
            sys.stdout.write(text)
        return 0
    stored = (ROOT / OUT).read_text(encoding="utf-8") if (ROOT / OUT).is_file() else ""
    print("OK: the stored index equals a rebuild" if stored == text else f"DRIFT: rebuild with `python3 framework/scripts/held_results_index.py build --write` ({OUT})")
    return 0 if stored == text else 1


if __name__ == "__main__":
    sys.exit(main())
