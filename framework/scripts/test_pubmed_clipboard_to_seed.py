#!/usr/bin/env python3
"""Regression tests for the privacy-preserving PubMed Clipboard converter."""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pubmed_clipboard_to_seed as converter  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCRIPT = HERE / "pubmed_clipboard_to_seed.py"
REAL_SEED = ROOT / "disease-models/wwox/registries/corpus_seed_pubmed_20260705.tsv"

EXPORT = """Mail\tExample Person <your-email@example.com>
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


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT,
                          capture_output=True, text=True, timeout=120)


def export_from_seed(rows: list[dict[str, str]]) -> str:
    """A Clipboard export that carries exactly the bibliographic facts of a seed's rows."""
    out = []
    for number, row in enumerate(rows, 1):
        citation = "bioRxiv [Preprint]." if row["type"] == "preprint" else "Journal."
        citation += f" {row['year']};1:1."
        if row["doi"]:
            citation += f" doi: {row['doi']}."
        tail = "      Free PMC article." if row["free_full_text"] == "yes" else ""
        tail += "     Review." if row["type"] == "review" else ""
        out.append(f"{number}.\n{row['title']}.\nAuthor A.\n{citation}\nPMID: {row['pmid']}{tail}\n")
    return "".join(out)


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


class TheCliIsDriven(unittest.TestCase):
    """``main`` as a subprocess: ``--out`` writes, ``--check`` compares, the exit codes hold."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)
        self.export = self.root / "clipboard.txt"
        self.export.write_text(EXPORT, encoding="utf-8")

    def test_out_writes_a_deidentified_seed(self) -> None:
        seed = self.root / "corpus_seed_pubmed_20260101.tsv"
        result = run_cli("--input", str(self.export), "--out", str(seed))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("(2 records)", result.stdout)
        text = seed.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("pmid\tyear\tfree_full_text\ttype\tdoi\ttitle\n"))
        self.assertNotIn("your-email@example.com", text)
        self.assertNotIn("Example Person", text)
        self.assertIn("42327583\t2026\tyes\treview\t10.1000/WWOX.1\tA WWOX study", text)

    def test_check_says_ok_on_a_match_and_drift_on_a_change(self) -> None:
        seed = self.root / "seed.tsv"
        run_cli("--input", str(self.export), "--out", str(seed))
        ok = run_cli("--input", str(self.export), "--check", str(seed))
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertIn("OK: 2 records match", ok.stdout)
        seed.write_text(seed.read_text(encoding="utf-8").replace("review", "primary"),
                        encoding="utf-8")
        drift = run_cli("--input", str(self.export), "--check", str(seed))
        self.assertEqual(drift.returncode, 1)
        self.assertIn("DRIFT", drift.stderr)

    def test_the_usage_and_input_errors_exit_2(self) -> None:
        neither = run_cli("--input", str(self.export))
        self.assertEqual(neither.returncode, 2)
        self.assertIn("provide --out or --check", neither.stderr)
        absent = run_cli("--input", str(self.root / "absent.txt"), "--out", str(self.root / "s"))
        self.assertEqual(absent.returncode, 2)
        self.assertIn("ERROR:", absent.stderr)
        self.assertFalse((self.root / "s").exists())


class TheRealSeedRoundTrips(unittest.TestCase):
    """The tracked 2026-07-05 seed is what this parser makes of its own records.

    A Clipboard export is never committed — it carries the sender's address — so the case
    rebuilds one from the seed's bibliographic columns and asks ``--check`` whether the parser
    still produces the seed from it, record for record. A classification change on any one of
    the 459 real records is a DRIFT here. The seed is read and compared; it is never written.
    """

    def test_check_against_the_real_seed_is_ok(self) -> None:
        if not REAL_SEED.is_file():
            self.skipTest(f"skipped: {REAL_SEED.relative_to(ROOT)} absent on this host")
        before = REAL_SEED.read_bytes()
        with REAL_SEED.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        self.assertGreater(len(rows), 100)
        with tempfile.TemporaryDirectory() as tmp:
            export = Path(tmp) / "rebuilt_clipboard.txt"
            export.write_text(export_from_seed(rows), encoding="utf-8")
            result = run_cli("--input", str(export), "--check", str(REAL_SEED.relative_to(ROOT)))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"OK: {len(rows)} records match", result.stdout)
        self.assertEqual(REAL_SEED.read_bytes(), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
