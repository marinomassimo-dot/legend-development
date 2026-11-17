#!/usr/bin/env python3
"""Detect truncation or structural corruption in public machine-readable data."""

from __future__ import annotations

import csv
import json
import os
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "__pycache__", ".venv", "node_modules"}
UTF8_SUFFIXES = {
    ".csv",
    ".json",
    ".md",
    ".pdb",
    ".py",
    ".tsv",
    ".txt",
    ".yaml",
    ".yml",
}


def public_files(root: Path = ROOT):
    """The public data of THIS checkout: what git would ship, never what merely sits on disk.

    🔴 Until 2026-09-14 this was `ROOT.rglob("*")`. On a working laboratory checkout that walked
    13,960 files, of which 12,512 are gitignored — 11,529 inside nested worktrees under
    `.claude/worktrees/`, 909 in the local corpus `files/`, plus `backup/`, `staging/` and
    ignored page crops. So the suite was permanently red here on ragged third-party supplement
    TSVs and empty downloaded figures in `files/`, and green in every fresh clone: its verdict
    described one machine's local corpus, not the published data its own docstring names.

    Same repair `test_release_surface.py` made for the same failure: ask git. Tracked files plus
    untracked-but-not-ignored ones, so a new data file is checked before it is committed.
    Measured at the change: every one of the 1,448 files in that set was already walked
    (dropped non-ignored paths: 0, added: 0), so no publishable file lost coverage.
    A source archive has no `.git`: walk it, pruning nested checkouts.
    """
    named = os.environ.get("LEGEND_STRUCT_PATHS")
    if named:                                      # 2026-11-16: scripts/legend_commit.sh runs these same tests on the files of ONE commit, so a ragged row is refused at the commit, not 19 CI runs later
        return sorted(root / rel for rel in named.split("\n") if rel and (root / rel).is_file())
    if (root / ".git").exists():
        listing = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=root, capture_output=True, text=True, check=True).stdout
        return sorted(root / rel for rel in listing.split("\0")
                      if rel and (root / rel).is_file()
                      and not any(part in IGNORED_PARTS for part in Path(rel).parts))
    found = []
    for directory, children, files in os.walk(root):
        here = Path(directory)
        children[:] = [child for child in children
                       if child not in IGNORED_PARTS
                       and not (here / child / ".git").exists()
                       and not (here / child).is_symlink()]
        found.extend(here / name for name in files)
    return sorted(found)


class StructuredDataIntegrityTests(unittest.TestCase):
    def test_no_public_file_is_empty(self) -> None:
        empty = [
            path.relative_to(ROOT).as_posix()
            for path in public_files()
            if path.stat().st_size == 0
        ]
        self.assertEqual([], empty)

    def test_text_assets_are_utf8(self) -> None:
        failures = []
        for path in public_files():
            if path.suffix.lower() not in UTF8_SUFFIXES:
                continue
            try:
                path.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                failures.append(f"{path.relative_to(ROOT)}: {exc}")
        self.assertFalse(failures, "\n".join(failures))

    def test_json_assets_parse(self) -> None:
        failures = []
        for path in public_files():
            if path.suffix.lower() != ".json":
                continue
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                failures.append(f"{path.relative_to(ROOT)}: {exc}")
        self.assertFalse(failures, "\n".join(failures))

    def test_csv_and_tsv_rows_have_consistent_width(self) -> None:
        failures = []
        for path in public_files():
            if path.suffix.lower() not in {".csv", ".tsv"}:
                continue
            delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
            with path.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.reader(handle, delimiter=delimiter))
            widths = {len(row) for row in rows if row}
            if len(widths) > 1:
                failures.append(
                    f"{path.relative_to(ROOT)}: row widths {sorted(widths)}"
                )
        self.assertFalse(failures, "\n".join(failures))


    def test_ideas_portfolio_ids_are_unique_and_arm_tables_name_only_known_ideas(self) -> None:
        """2026-11-16: two ideas were both named I16 until renumbered (RP-006 row 7). The ideas portfolio must not repeat an id, and every idea token (I<number>) in the `idea` column of an
        ideas arm table must be an id of the portfolio; free text and composite cells ('I1/I10', 'leak reading (I4/SCI)') are read token by token, other words ignored. An idea with no arm
        row is allowed (an idea may have no arm yet)."""
        import re
        portfolios = [p for p in public_files() if p.name == "ideas_portfolio.tsv"]
        failures = []
        for pf in portfolios:
            with pf.open(encoding="utf-8", newline="") as h:
                rows = list(csv.DictReader(h, delimiter="\t"))
            ids = [r["id"] for r in rows]
            dup = sorted({i for i in ids if ids.count(i) > 1})
            if dup:
                failures.append(f"{pf.relative_to(ROOT)}: duplicate idea id {dup}")
            known = set(ids)
            for arm in sorted(pf.parent.glob("ideas_arm_table*.tsv")):
                with arm.open(encoding="utf-8", newline="") as h:
                    for n, r in enumerate(csv.DictReader(h, delimiter="\t"), 2):
                        for tok in re.findall(r"\bI\d+\b", r.get("idea", "") or ""):
                            if tok not in known:
                                failures.append(f"{arm.relative_to(ROOT)} line {n}: idea {tok} is not in {pf.name}")
        self.assertFalse(failures, "\n".join(failures))


if __name__ == "__main__":
    unittest.main(verbosity=2)
