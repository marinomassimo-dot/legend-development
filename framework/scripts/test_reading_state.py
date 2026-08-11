#!/usr/bin/env python3
"""Regressions for the reading-state view.

The property that matters is the one the view exists for: **summing never chooses.** A merge
that takes one side erases another actor's reading, and it erases it in the record that exists
to say what has been read — so every test below is a way of asking whether something got lost.
"""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import reading_state as view  # noqa: E402

PAGE = ROOT / "disease-models" / "wwox" / "registries" / "reading_state.md"


def receipt(event_id: str, pmid: str, coverage: dict, *, prior: str | None = None,
            depth: str = "partial_fulltext_read") -> dict:
    full = {key: "not_read" for key in
            ("abstract", "introduction", "methods", "results", "figures", "tables",
             "discussion", "limitations", "supplementary")}
    full.update(coverage)
    return {"event_id": event_id, "study_id": {"pmid": pmid, "doi": None},
            "coverage": full, "prior_receipt": prior, "evidence_depth": depth}


class SummingNeverChooses(unittest.TestCase):
    def test_two_parallel_readings_are_summed_not_overwritten(self) -> None:
        """🔴 The whole point. One read Methods, the other Discussion; both are in the state."""
        rows = view.summarise([
            receipt("A-01", "111", {"methods": "read"}),
            receipt("A-02", "111", {"discussion": "read"}, prior="A-01"),
            receipt("A-03", "111", {"methods": "not_read", "results": "read"}, prior="A-01"),
        ])
        union = rows[0]["union"]
        self.assertEqual(union["methods"], "read")
        self.assertEqual(union["discussion"], "read")
        self.assertEqual(union["results"], "read")

    def test_the_later_receipt_cannot_downgrade_the_earlier(self) -> None:
        """A merge that let the last write win is exactly the erasure this prevents."""
        rows = view.summarise([
            receipt("A-01", "111", {"figures": "read"}),
            receipt("A-02", "111", {"figures": "captions_only"}, prior="A-01"),
        ])
        self.assertEqual(rows[0]["union"]["figures"], "read")

    def test_looking_beats_not_looking_and_a_fact_about_the_article_beats_both(self) -> None:
        self.assertGreater(view.rank("read"), view.rank("captions_only"))
        self.assertGreater(view.rank("captions_only"), view.rank("not_present"))
        self.assertGreater(view.rank("not_present"), view.rank("unavailable"))
        self.assertGreater(view.rank("unavailable"), view.rank("not_read"))
        self.assertGreater(view.rank("not_read"), view.rank("unknown_legacy"))

    def test_an_unknown_state_never_outranks_a_known_one(self) -> None:
        """A vocabulary that grows must not silently win over a value someone measured."""
        self.assertEqual(view.rank("a_state_invented_later"), 0)


class ForksAreReportedNotResolved(unittest.TestCase):
    def test_two_receipts_naming_one_parent_are_a_fork(self) -> None:
        rows = view.summarise([
            receipt("A-01", "111", {}),
            receipt("A-02", "111", {}, prior="A-01"),
            receipt("A-03", "111", {}, prior="A-01"),
        ])
        self.assertEqual(rows[0]["forks"], {"A-01": ["A-02", "A-03"]})

    def test_a_linear_history_is_not_a_fork(self) -> None:
        rows = view.summarise([
            receipt("A-01", "111", {}),
            receipt("A-02", "111", {}, prior="A-01"),
            receipt("A-03", "111", {}, prior="A-02"),
        ])
        self.assertEqual(rows[0]["forks"], {})

    def test_the_fork_is_named_in_the_page(self) -> None:
        page = view.render(view.summarise([
            receipt("A-01", "111", {}),
            receipt("A-02", "111", {}, prior="A-01"),
            receipt("A-03", "111", {}, prior="A-01"),
        ]), "wwox")
        self.assertIn("read in parallel", page)
        self.assertIn("`A-02`", page)
        self.assertIn("`A-03`", page)


class ThePageSaysWhatItIs(unittest.TestCase):
    def test_it_declares_it_is_true_of_one_checkout(self) -> None:
        """A count over unmerged state is a count of work that is not in the model."""
        page = view.render(view.summarise([receipt("A-01", "111", {})]), "wwox")
        self.assertIn("true of ONE checkout", page)

    def test_it_declares_itself_generated(self) -> None:
        page = view.render(view.summarise([receipt("A-01", "111", {})]), "wwox")
        self.assertIn("GENERATED", page)
        self.assertIn("reading_state.py", page)

    def test_it_says_no_receipt_asserts_the_union(self) -> None:
        page = view.render(view.summarise([receipt("A-01", "111", {})]), "wwox")
        self.assertIn("asserted by no receipt", page)


class TheCommittedPageIsCurrent(unittest.TestCase):
    def test_the_page_exists_and_matches_the_ledger(self) -> None:
        self.assertTrue(PAGE.is_file(), f"missing generated page: {PAGE}")
        result = subprocess.run(
            [sys.executable, str(ROOT / "framework" / "scripts" / "reading_state.py"),
             "--root", str(ROOT), "--check", str(PAGE)],
            capture_output=True, text=True)
        self.assertEqual(
            result.returncode, 0,
            "The committed reading state has drifted from the receipt ledger. Regenerate it:\n"
            "  python3 framework/scripts/reading_state.py "
            "--out disease-models/wwox/registries/reading_state.md\n"
            f"{result.stdout}{result.stderr}")

    def test_the_drift_check_can_fail(self) -> None:
        """🔴 A drift test with no environment that can break it is not a test."""
        result = subprocess.run(
            [sys.executable, str(ROOT / "framework" / "scripts" / "reading_state.py"),
             "--root", str(ROOT), "--check", str(ROOT / "README.md")],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("DRIFT", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
