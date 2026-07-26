#!/usr/bin/env python3
"""Regression tests for the independent privacy scanner."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCANNER_PATH = Path(__file__).with_name("independent_privacy_scan.py")
SPEC = importlib.util.spec_from_file_location("independent_privacy_scan", SCANNER_PATH)
assert SPEC and SPEC.loader
SCANNER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SCANNER
SPEC.loader.exec_module(SCANNER)


class IndependentPrivacyScanTests(unittest.TestCase):
    def make_root(self, text: str) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "note.md").write_text(text, encoding="utf-8")
        return root

    def test_sensitive_city_digest_blocks(self) -> None:
        city = "".join(map(chr, (66, 101, 114, 103, 97, 109, 111)))
        findings, errors = SCANNER.scan(self.make_root(f"Location: {city}."))
        self.assertFalse(errors)
        self.assertIn(
            ("ITALIAN_CITY", "BLOCK"),
            {(item.category, item.severity) for item in findings},
        )

    def test_glued_private_name_blocks(self) -> None:
        findings, errors = SCANNER.scan(
            self.make_root("sample_" + "Bim" + "ba" + "_derived")
        )
        self.assertFalse(errors)
        self.assertIn(
            ("GLUED_NAME_CANDIDATE", "BLOCK"),
            {(item.category, item.severity) for item in findings},
        )

    def test_standalone_private_name_blocks(self) -> None:
        findings, errors = SCANNER.scan(
            self.make_root("Operator: " + "Mas" + "simo")
        )
        self.assertFalse(errors)
        self.assertIn(
            ("PRIVATE_NAME", "BLOCK"),
            {(item.category, item.severity) for item in findings},
        )

    def test_common_lowercase_homonym_does_not_block(self) -> None:
        findings, errors = SCANNER.scan(
            self.make_root("Usare il massimo contesto disponibile.")
        )
        self.assertFalse(errors)
        self.assertNotIn(
            ("PRIVATE_NAME", "BLOCK"),
            {(item.category, item.severity) for item in findings},
        )

    def test_uppercase_private_name_in_compound_token_blocks(self) -> None:
        sensitive = "".join(map(chr, (66, 101, 97))).upper()
        findings, errors = SCANNER.scan(
            self.make_root(f"MODE: {sensitive}_PRIORITY_MATRIX")
        )
        self.assertFalse(errors)
        self.assertIn(
            ("PRIVATE_NAME", "BLOCK"),
            {(item.category, item.severity) for item in findings},
        )

    def test_city_homonym_remains_informational(self) -> None:
        findings, errors = SCANNER.scan(
            self.make_root("La potenza spettrale è aumentata.")
        )
        self.assertFalse(errors)
        self.assertIn(
            ("ITALIAN_CITY", "INFO"),
            {(item.category, item.severity) for item in findings},
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
