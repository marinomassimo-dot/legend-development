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

    def test_the_owner_is_the_record_that_declares_the_reading(self) -> None:
        """🔴 The case that broke it: a placeholder resolved into a CORPUS record, not a PAPER.

        `receipt_owners` preferred PAPER over CORPUS, which is the right answer only while the
        two candidates differ in kind. On 2026-09-20 `CORPUS-STUB-022` was resolved into
        `CORPUS P022` — both CORPUS — the tie fell to file order, the bare placeholder won
        because stubs sit near the top of the registry, and LINT reported the record that
        actually declares the reading as an UNBACKED_FULLTEXT_DECLARATION.

        Ordered as the defect had it, so the arm fails against the rule it replaces.
        """
        entries = [
            {"_id": "CORPUS-STUB-022", "_kind": "CORPUS", "identifier": "PMID 31075076"},
            {"_id": "CORPUS P022", "_kind": "CORPUS", "identifier": "PMID 31075076",
             "evidence depth": "complete_fulltext_read — `FTR-20260811-31075076-02`"},
        ]
        receipt = {"event_id": "FTR-20260811-31075076-02",
                   "evidence_depth": "complete_fulltext_read"}
        owners = cov.receipt_owners(entries, {"pmid:31075076": receipt})
        self.assertEqual(owners, {"CORPUS P022": receipt},
                         "the owner is the record that claims the reading, not the placeholder")

    def test_kind_still_breaks_the_tie_when_neither_declares_more(self) -> None:
        """The older rule survives underneath: PAPER wins when no candidate declares a reading,
        so this repair narrows nothing."""
        entries = [
            {"_id": "CORPUS 001", "_kind": "CORPUS", "identifier": "PMID 42193054"},
            {"_id": "PAPER 001", "_kind": "PAPER", "identifier": "PMID 42193054"},
        ]
        receipt = {"event_id": "FTR-20260726-42193054-01",
                   "evidence_depth": "complete_fulltext_read"}
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

    def test_the_reading_debt_split_adds_up_and_leaves_the_headline_alone(self) -> None:
        report = cov.build(ROOT, "wwox")
        split = report["reading_debt_split"]
        self.assertEqual(split["receipted_elsewhere"] + split["no_receipt"], report["reading_debt_count"])
        self.assertEqual(split["complete"] + split["partial"], split["receipted_elsewhere"])
        self.assertGreater(split["receipted_elsewhere"], 0, "IT59 2026-11-19 found 115: a split that finds none has lost the receipt join")
        text = cov.render(report)
        self.assertIn("carry a receipt owned by another registry entry", text)
        self.assertIn("the headline count is unchanged", text)

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


def _receipt(event_id, at, depth, read, pmid=None, doi=None, kind="contemporaneous_receipt"):
    sections = ("abstract", "introduction", "methods", "results", "discussion", "limitations", "figures", "tables", "supplementary")
    study = {k: v for k, v in (("pmid", pmid), ("doi", doi)) if v}
    return {"event_id": event_id, "event_at": at, "record_kind": kind, "evidence_depth": depth, "study_id": study,
            "coverage": {s: ("read" if s in read else "not_read") for s in sections}}


class SectionsBestStateTests(unittest.TestCase):
    """ADV-227: the union of the surviving receipts next to the latest receipt, sections and not depth."""

    def test_a_narrow_re_read_loses_sections_under_latest_but_not_under_best_state(self) -> None:
        events = [
            _receipt("E1", "2026-11-01T10:00:00Z", "complete_fulltext_read", ("methods", "results", "discussion"), pmid="1"),
            _receipt("E2", "2026-11-02T10:00:00Z", "partial_fulltext_read", ("results",), pmid="1"),
            _receipt("E3", "2026-11-03T10:00:00Z", "partial_fulltext_read", ("results",), pmid="2"),
            _receipt("E4", "2026-11-04T10:00:00Z", "complete_fulltext_read", ("results", "methods"), pmid="2"),
        ]
        got = cov.sections_best_state(events)
        self.assertEqual(got["studies"], 2)
        self.assertEqual(got["multi_receipt_studies"], 2)
        self.assertEqual(got["latest_narrower"], 1)            # study 1 only: study 2's latest is wider
        self.assertEqual(got["section_reads_best_state"], 3 + 2)
        self.assertEqual(got["section_reads_latest_receipt"], 1 + 2)
        self.assertEqual(got["section_reads_only_earlier"], 2)

    def test_the_order_is_event_at_not_the_ledger_position(self) -> None:
        later_first_in_file = [
            _receipt("E2", "2026-11-02T10:00:00Z", "partial_fulltext_read", ("results",), pmid="1"),
            _receipt("E1", "2026-11-01T10:00:00Z", "complete_fulltext_read", ("methods", "results"), pmid="1"),
        ]
        got = cov.sections_best_state(later_first_in_file)
        self.assertEqual(got["section_reads_latest_receipt"], 1)     # E2 is the latest by time
        self.assertEqual(got["latest_narrower"], 1)

    def test_an_invalidated_receipt_does_not_survive(self) -> None:
        events = [
            _receipt("E1", "2026-11-01T10:00:00Z", "complete_fulltext_read", ("methods", "results"), pmid="1"),
            _receipt("E2", "2026-11-02T10:00:00Z", "partial_fulltext_read", ("results",), pmid="1"),
            {"event_id": "E3", "record_kind": "receipt_invalidation", "invalidates_receipt": "E1"},
        ]
        got = cov.sections_best_state(events)
        self.assertEqual(got["multi_receipt_studies"], 0)
        self.assertEqual(got["section_reads_best_state"], 1)

    def test_only_exactly_read_counts_and_a_doi_keys_a_study_without_a_pmid(self) -> None:
        first = _receipt("E1", "2026-11-01T10:00:00Z", "partial_fulltext_read", ("results",), doi="10.1/X")
        first["coverage"]["methods"] = "captions_only"
        second = _receipt("E2", "2026-11-02T10:00:00Z", "partial_fulltext_read", ("results",), doi="10.1/x")
        got = cov.sections_best_state([first, second])
        self.assertEqual((got["studies"], got["multi_receipt_studies"], got["section_reads_best_state"]), (1, 1, 1))

    def test_the_page_prints_the_line_and_no_depth_number_depends_on_it(self) -> None:
        report = cov.build(ROOT, "wwox")
        text = cov.render(report)
        self.assertIn("**Sections read, best state**", text)
        self.assertIn("this line is about sections, not depth, and changes no number above", text)
        stripped = {k: v for k, v in report.items() if k != "sections_best_state"}
        self.assertEqual(cov.render(stripped).replace(
            [l for l in text.splitlines() if l.startswith("- **Sections read, best state**")][0] + "\n", ""), cov.render(stripped))


if __name__ == "__main__":
    unittest.main(verbosity=2)
