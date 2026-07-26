#!/usr/bin/env python3
"""Detect truncation or structural corruption in public machine-readable data."""

from __future__ import annotations

import csv
import json
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


def public_files():
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in IGNORED_PARTS for part in path.relative_to(ROOT).parts)
    )


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
