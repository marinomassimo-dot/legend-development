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


    def make_root_named(self, name: str, text: str) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / name).write_text(text, encoding="utf-8")
        return root

    def blocks(self, name: str, text: str) -> set[tuple[str, str]]:
        findings, errors = SCANNER.scan(self.make_root_named(name, text))
        self.assertFalse(errors)
        return {(item.category, item.severity) for item in findings}

    @staticmethod
    def homonym() -> str:
        return "".join(map(chr, (77, 97, 115, 115, 105, 109, 111))).lower()

    def test_jsonl_is_scanned_like_json(self) -> None:
        token = "".join(map(chr, (66, 105, 109, 98, 97)))
        self.assertIn(("PRIVATE_NAME", "BLOCK"),
                      self.blocks("ledger.jsonl", '{"note": "' + token + '"}\n'))

    def test_lowercase_identifier_in_tracked_path_blocks(self) -> None:
        self.assertIn(("PRIVATE_NAME", "BLOCK"), self.blocks(
            "note.md", "| Worktree | `/Users/" + self.homonym() + "/Desktop/x` |"))

    def test_lowercase_identifier_in_path_inside_jsonl_blocks(self) -> None:
        self.assertIn(("PRIVATE_NAME", "BLOCK"), self.blocks(
            "state.jsonl", '{"path": "/Users/' + self.homonym() + '/Desktop/x"}\n'))

    def test_lowercase_homonym_still_does_not_block_in_jsonl(self) -> None:
        self.assertNotIn(("PRIVATE_NAME", "BLOCK"), self.blocks(
            "ledger.jsonl", '{"note": "al ' + self.homonym() + ' Tier 3"}\n'))

    def test_italian_slash_pair_is_not_a_path(self) -> None:
        """F-1 (Mirror, 2026-08-26): a superlative pair has no path root."""
        self.assertNotIn(("PRIVATE_NAME", "BLOCK"), self.blocks(
            "prose.md", "Il valore minimo/" + self.homonym() + " del parametro.\n"))

    def test_path_terminated_by_prose_punctuation_blocks(self) -> None:
        for text in (
            "It lives under /Users/" + self.homonym() + ".\n",
            "Root is **/Users/" + self.homonym() + "**\n",
            "/Users/" + self.homonym() + ": permission denied\n",
            "moves inside `~/.legend/lineage/AIR-DI-X-" + self.homonym() + "/`\n",
        ):
            with self.subTest(text=text):
                self.assertIn(("PRIVATE_NAME", "BLOCK"), self.blocks("form.md", text))

    def test_a_path_followed_by_list_punctuation_and_the_homonym_is_two_runs(self) -> None:
        for name, text in (
            ("cells.csv", "/home/legend," + self.homonym() + "\n"),
            ("table.md", "|/home/legend|" + self.homonym() + "|3|\n"),
        ):
            with self.subTest(text=text):
                self.assertNotIn(("PRIVATE_NAME", "BLOCK"), self.blocks(name, text))

    def test_path_context_is_decided_before_the_digest_skip(self) -> None:
        """`/var/folders/<tok>9f2c4e1d0/T` is a path carrying the token even though the
        token sits inside a hex-looking run."""
        self.assertIn(("PRIVATE_NAME", "BLOCK"), self.blocks(
            "tmp.md", "/var/folders/" + self.homonym() + "9f2c4e1d0/T/x\n"))

    def test_identifier_like_substring_inside_sha256_does_not_block(self) -> None:
        """The three-letter token occurs by chance inside SHA-256 seals in this
        repository, and every such match was a false BLOCK before the hex-run skip."""
        self.assertNotIn(("PRIVATE_NAME", "BLOCK"), self.blocks(
            "seal.jsonl",
            '{"sha256": "40ba0b73c00215625b086c9' + "".join(map(chr, (98, 101, 97)))
            + '071b270f47fb34aa11bb22cc33dd44ee"}\n'))

    def test_identifier_inside_a_content_address_fragment_does_not_block(self) -> None:
        token = "".join(map(chr, (98, 101, 97)))
        self.assertNotIn(("PRIVATE_NAME", "BLOCK"), self.blocks(
            "export.jsonl", '{"candidate_id": "RPC-' + token + '596753ac3"}\n'))
        self.assertIn(("PRIVATE_NAME", "BLOCK"), self.blocks(
            "short.jsonl", '{"candidate_id": "RPC-' + token + '5967531"}\n'))
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
