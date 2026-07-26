#!/usr/bin/env python3
"""Regression tests for the privacy-preserving PubMed Clipboard converter."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pubmed_clipboard_to_seed as converter  # noqa: E402


class PubMedClipboardTests(unittest.TestCase):
    def test_headers_are_discarded_and_bibliography_is_preserved(self) -> None:
        source = """Mail\tExample Person <your-email@example.com>
Sent by NCBI <nobody [at] ncbi.example>

PubMed Results
1.
A WWOX study.
Author A.
Journal. 2026 Jan;1:1. doi: 10.1000/WWOX.1.
PMID: 42327583      Free PMC article.     Review.
2.
Another study.
Author B.
bioRxiv [Preprint]. 2025 Dec. doi: 10.1000/preprint.2.
PMID: 40000000
"""
        rows = converter.parse(source)
        output = converter.render(rows)
        self.assertNotIn("Example Person", output)
        self.assertNotIn("your-email@example.com", output)
        self.assertIn("42327583\t2026\tyes\treview\t10.1000/WWOX.1", output)
        self.assertIn("40000000\t2025\tno\tpreprint\t10.1000/preprint.2", output)

    def test_retraction_notice_doi_does_not_replace_article_doi(self) -> None:
        source = """1.
Retracted article.
Author A.
Journal. 2017;1:1. doi: 10.1000/article.1.
Retraction in: Journal. 2022;2:2. doi: 10.1000/retraction.2.
PMID: 28151481      Free PMC article.
"""
        row = converter.parse(source)[0]
        self.assertEqual(row["doi"], "10.1000/article.1")

    def test_duplicate_pmid_fails_closed(self) -> None:
        source = """1.
First.
Journal. 2025.
PMID: 40000000
2.
Second.
Journal. 2025.
PMID: 40000000
"""
        with self.assertRaisesRegex(ValueError, "duplicate PMID"):
            converter.parse(source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
