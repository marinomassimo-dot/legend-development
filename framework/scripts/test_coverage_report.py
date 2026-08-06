#!/usr/bin/env python3
"""Regression suite for the corpus-coverage view.

Two things are guarded. First, the classifier: a record must not be counted as read
because a status string looks encouraging. Second, and more important, **drift**: the
committed report is generated, so if a registry changes and the report is not regenerated,
a reader is shown numbers that no longer describe the repository. That failure is silent
by nature, which is exactly the kind this project turns into a test.
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent))

import coverage_report as cov  # noqa: E402
import fulltext_receipts as receipts  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "disease-models" / "wwox" / "registries" / "coverage_report.md"


class ClassifierTests(unittest.TestCase):
    def test_full_text_marker_wins(self) -> None:
        entry = {
            "_kind": "PAPER",
            "evidence depth": "full text reviewed (coverage_status: complete_fulltext_read)",
            "status": "claim_linked",
        }
        self.assertEqual(cov.classify_depth(entry), "full_text")

    def test_partial_is_not_counted_as_full(self) -> None:
        entry = {
            "_kind": "PAPER",
            "evidence depth": "partial full text (non open access)",
            "status": "processed",
        }
        self.assertEqual(cov.classify_depth(entry), "partial_full_text")

    def test_corpus_placeholder_is_debt_not_read(self) -> None:
        entry = {"_kind": "CORPUS", "evidence depth": "", "status": "screened — corpus placeholder"}
        self.assertEqual(cov.classify_depth(entry), "catalogued")

    def test_integrated_without_full_text_is_abstract_depth(self) -> None:
        """`integrated` describes pipeline state, never that anybody read the paper."""
        entry = {"_kind": "PAPER", "evidence depth": "", "status": "integrated"}
        self.assertEqual(cov.classify_depth(entry), "abstract")

    def test_filtered_state_is_reported_separately(self) -> None:
        entry = {"_kind": "PAPER", "evidence depth": "", "status": "superseded"}
        self.assertEqual(cov.classify_depth(entry), "filtered")


class ReportIntegrityTests(unittest.TestCase):
    def test_complete_receipt_updates_coverage_before_registry_promotion(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            registries = root / "disease-models" / "wwox" / "registries"
            registries.mkdir(parents=True)
            (registries / "paper_registry_current.md").write_text(
                "## PAPER 001\n**Identifier:** PMID 42193054 / DOI 10.1000/example\n"
                "**Status:** integrated\n",
                encoding="utf-8",
            )
            ledger = registries / "fulltext_read_receipts.jsonl"
            ledger.touch()
            receipt = {
                "event_id": "FTR-20260726-42193054-01",
                "record_kind": "contemporaneous_receipt",
                "study_id": {"pmid": "42193054", "doi": "10.1000/example"},
                "event_at": "2026-07-26T08:00:00+02:00",
                "analysis_at": "2026-07-26T07:00:00+02:00",
                "workflow": "test",
                "evidence_depth": "complete_fulltext_read",
                "source_locator": "PMC123",
                "source_fingerprint": None,
                "source_kind": "fulltext_remote",
                "analysis_time_precision": "second",
                "coverage": {key: "read" for key in receipts.COVERAGE_KEYS},
                "outputs": ["dossier.md"],
                "evidence_basis": ["coverage_map", "dossier"],
                "prior_receipt": None,
                "reread_reason": "first_read",
            }
            scratch_ledger = root / "receipt_fixture.jsonl"
            receipts.append_receipt(scratch_ledger, receipt)
            scratch_ledger.replace(ledger)
            report = cov.build(root, "wwox")
            self.assertEqual(report["depth"]["full_text"], 1)
            self.assertEqual(report["receipt_backed_complete_records"], 1)
            self.assertEqual(report["registry_only_full_records"], 0)

    def test_missing_receipt_ledger_fails_closed(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            registries = root / "disease-models" / "wwox" / "registries"
            registries.mkdir(parents=True)
            (registries / "paper_registry_current.md").write_text(
                "## PAPER 001\n**Identifier:** PMID 42193054\n**Status:** integrated\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(SystemExit, "missing full-text receipt ledger"):
                cov.build(root, "wwox")

    def test_promoted_placeholder_does_not_double_count_one_receipt(self) -> None:
        entries = [
            {"_id": "PAPER 001", "_kind": "PAPER", "identifier": "PMID 42193054"},
            {"_id": "CORPUS 001", "_kind": "CORPUS", "identifier": "PMID 42193054"},
        ]
        receipt = {
            "event_id": "FTR-20260726-42193054-01",
            "evidence_depth": "complete_fulltext_read",
        }
        owners = cov.receipt_owners(entries, {"pmid:42193054": receipt})
        self.assertEqual(owners, {"PAPER 001": receipt})

    def test_report_exists_and_is_current(self) -> None:
        self.assertTrue(REPORT.is_file(), f"missing generated report: {REPORT}")
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "framework" / "scripts" / "coverage_report.py"),
                "--root",
                str(ROOT),
                "--check",
                str(REPORT),
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            "The committed coverage report has drifted from the registries. "
            "Regenerate it:\n"
            "  python3 framework/scripts/coverage_report.py "
            "--out disease-models/wwox/registries/coverage_report.md\n"
            f"{result.stdout}{result.stderr}",
        )

    def test_totals_are_internally_consistent(self) -> None:
        report = cov.build(ROOT, "wwox")
        self.assertEqual(
            sum(report["depth"].values()),
            report["entries_total"],
            "every entry must land in exactly one depth bucket",
        )
        self.assertEqual(
            report["paper_records"] + report["corpus_placeholders"],
            report["entries_total"],
        )
        self.assertGreater(report["entries_total"], 0)
        self.assertEqual(report["reading_debt_count"], report["depth"].get("catalogued", 0))

    def test_coverage_is_not_overstated(self) -> None:
        """The read share must never exceed the number of records claiming a full text."""
        registry = (
            ROOT / "disease-models" / "wwox" / "registries" / "paper_registry_current.md"
        ).read_text(encoding="utf-8")
        claimed = sum(
            registry.lower().count(marker) for marker in cov.FULL_TEXT_MARKERS
        )
        report = cov.build(ROOT, "wwox")
        self.assertLessEqual(
            report["depth"].get("full_text", 0),
            claimed + report["receipt_backed_complete_records"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
