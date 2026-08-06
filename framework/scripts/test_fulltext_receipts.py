#!/usr/bin/env python3
"""Tests for append-only full-text receipt validation and duplicate-work blocking."""

from __future__ import annotations

import copy
import hashlib
import json
import multiprocessing
import sys
import time
import unittest
from unittest import mock
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fulltext_receipts as receipts  # noqa: E402

try:
    import fcntl
except ImportError:  # pragma: no cover - the runtime deliberately fails closed without it
    fcntl = None


def example(event_id: str, depth: str = "complete_fulltext_read") -> dict:
    return {
        "event_id": event_id,
        "record_kind": "contemporaneous_receipt",
        "study_id": {"pmid": "42193054", "doi": "10.1000/example"},
        "event_at": "2026-07-25T20:00:00Z",
        "analysis_at": "2026-07-25T19:30:00Z",
        "workflow": "test",
        "evidence_depth": depth,
        "source_locator": "PMC123",
        "source_fingerprint": None,
        "source_kind": "fulltext_remote",
        "analysis_time_precision": "second",
        "coverage": {key: "read" for key in receipts.COVERAGE_KEYS},
        "outputs": ["dossier_42193054.md"],
        "evidence_basis": ["coverage_map", "dossier"],
        "prior_receipt": None,
        "reread_reason": "first_read",
    }


def append_worker(ledger: str, result_queue: multiprocessing.Queue) -> None:
    try:
        receipts.append_receipt(Path(ledger), example("FTR-20260725-42193054-01"))
        result_queue.put("recorded")
    except Exception as error:  # pragma: no cover - surfaced through the parent assertion
        result_queue.put(f"error:{error}")


class FulltextReceiptTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.ledger = Path(self.temporary.name) / "receipts.jsonl"

    def test_complete_receipt_is_append_only_and_queryable(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipts.append_receipt(self.ledger, receipt)
        loaded = receipts.load_ledger(self.ledger)
        self.assertEqual([item["event_id"] for item in loaded], [receipt["event_id"]])
        self.assertTrue(receipts.same_study(loaded[0], "42193054", ""))

    def test_new_complete_receipt_refuses_pubmed_abstract_url(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipt["source_locator"] = "https://pubmed.ncbi.nlm.nih.gov/42193054/"
        errors = receipts.validate_new_receipt(receipt)
        self.assertTrue(any("PubMed record URL" in error for error in errors))

    def test_authoritative_complete_read_requires_local_snapshot(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        errors = receipts._strict_local_source(receipt, Path(self.temporary.name))
        self.assertTrue(any("require source_kind `fulltext_local`" in error for error in errors))

    def test_abstract_only_receipt_may_name_the_corpus_without_clearing_debt(self) -> None:
        receipt = example("FTR-20260725-42193054-01", "abstract_only")
        receipt.update({
            "source_locator": "files/corpus/wwox.jsonl",
            "source_fingerprint": "a" * 64,
            "source_kind": "corpus_export",
        })
        self.assertEqual(receipts.validate_receipt(receipt), [])
        self.assertEqual(receipts.validate_new_receipt(receipt), [])

    def test_new_receipt_uses_precision_not_midnight_string_guessing(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipt["analysis_at"] = "2026-07-25T00:00:00Z"
        self.assertEqual(receipts.validate_new_receipt(receipt), [])
        del receipt["analysis_time_precision"]
        self.assertTrue(any("analysis_time_precision" in error
                            for error in receipts.validate_new_receipt(receipt)))

    def test_direct_append_to_authoritative_sink_cannot_skip_work_manifest(self) -> None:
        root = Path(self.temporary.name)
        ledger = root / "disease-models/test/registries/fulltext_read_receipts.jsonl"
        state = root / "framework/state/state_manifest_current.md"
        state.parent.mkdir(parents=True)
        state.write_text(
            "fulltext_ledger_events: 0\nfulltext_ledger_head: null\n", encoding="utf-8")
        fulltext = root / "files/fulltext/paper.xml"
        fulltext.parent.mkdir(parents=True)
        fulltext.write_text("<article><body>full text</body></article>", encoding="utf-8")
        receipt = example("FTR-20260725-42193054-01")
        receipt.update({
            "source_locator": "files/fulltext/paper.xml",
            "source_fingerprint": hashlib.sha256(fulltext.read_bytes()).hexdigest(),
            "source_kind": "fulltext_local",
        })
        with self.assertRaisesRegex(ValueError, "no deep-dive work manifest"):
            receipts.append_receipt(ledger, receipt)
        self.assertFalse(ledger.exists(), "the gate ran after persistence")

    def test_declared_manifest_gap_blocks_a_new_complete_read(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        root = Path(self.temporary.name)
        work = root / "disease-models/test/research/deepdive_manifests/PMID42193054.json"
        work.parent.mkdir(parents=True)
        work.write_text(json.dumps({
            "source_artifacts": [{"path": "PMC123", "sha256": ""}]
        }), encoding="utf-8")
        with mock.patch("deepdive_manifest.load_and_validate",
                        return_value=([], ["missing locator surface"])):
            with self.assertRaisesRegex(ValueError, "declared gap"):
                receipts.require_work_manifest(receipt, root, "test", strict=True)

    def test_missing_manifest_validator_fails_closed(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        real_import = __import__

        def refuse_validator(name, *args, **kwargs):
            if name == "deepdive_manifest":
                raise ImportError("simulated missing validator")
            return real_import(name, *args, **kwargs)

        saved = sys.modules.pop("deepdive_manifest", None)
        try:
            with mock.patch("builtins.__import__", side_effect=refuse_validator):
                with self.assertRaisesRegex(ValueError, "validator unavailable"):
                    receipts.require_work_manifest(
                        receipt, Path(self.temporary.name), "test", strict=True)
        finally:
            if saved is not None:
                sys.modules["deepdive_manifest"] = saved

    def test_complete_read_cannot_rest_on_captions_only(self) -> None:
        """A caption is authored prose; the figure is the data (D-14).

        The 2026-07-26 finding — a supplementary figure whose panels contradict its own
        caption — was invisible at caption level. A depth that cannot tell the two apart
        would certify a read that could not have caught it.
        """
        receipt = example("FTR-20260725-42193054-01")
        receipt["coverage"]["figures"] = "captions_only"
        self.assertTrue(
            any("captions_only" in error for error in receipts.validate_receipt(receipt))
        )

    def test_captions_only_is_valid_for_a_partial_read(self) -> None:
        receipt = example("FTR-20260725-42193054-01", depth="partial_fulltext_read")
        receipt["coverage"]["figures"] = "captions_only"
        self.assertEqual([], receipts.validate_receipt(receipt))

    def test_optional_references_coverage_is_accepted_and_not_required(self) -> None:
        """`references` is a ratchet, not a retro-fit: 28 persisted events predate it."""
        without = example("FTR-20260725-42193054-01")
        self.assertEqual([], receipts.validate_receipt(without))
        with_refs = example("FTR-20260725-42193054-02")
        with_refs["coverage"]["references"] = "read"
        self.assertEqual([], receipts.validate_receipt(with_refs))

    def test_unknown_coverage_section_is_still_rejected(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipt["coverage"]["acknowledgements"] = "read"
        self.assertTrue(receipts.validate_receipt(receipt))

    def test_complete_with_unread_section_is_rejected(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipt["coverage"]["supplementary"] = "not_read"
        self.assertTrue(
            any(
                "cannot leave a section not_read" in error
                for error in receipts.validate_receipt(receipt)
            )
        )

    def test_semantically_empty_complete_receipt_is_rejected(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipt["event_at"] = "not-a-date"
        receipt["analysis_at"] = "also-not-a-date"
        receipt["workflow"] = ""
        receipt["source_locator"] = ""
        receipt["outputs"] = []
        receipt["evidence_basis"] = []
        receipt["coverage"] = {key: "unavailable" for key in receipts.COVERAGE_KEYS}
        errors = receipts.validate_receipt(receipt)
        for expected in (
            "invalid event_at",
            "invalid analysis_at",
            "workflow must be non-empty",
            "source_locator must be non-empty",
            "complete_fulltext_read requires at least one read section",
            "outputs must be a non-empty list",
            "evidence_basis must be a non-empty list",
        ):
            self.assertTrue(any(expected in error for error in errors), (expected, errors))

    def test_analysis_timestamp_cannot_follow_receipt_event(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipt["analysis_at"] = "2026-07-25T20:00:01Z"
        self.assertIn(
            "analysis_at cannot be later than event_at",
            receipts.validate_receipt(receipt),
        )

    def test_legacy_unknown_coverage_is_explicit_and_never_complete(self) -> None:
        legacy = example("FTR-20260725-42193054-01", "partial_fulltext_read")
        legacy["record_kind"] = "legacy_reconstruction"
        legacy["analysis_at"] = None
        legacy["coverage"] = {key: "unknown_legacy" for key in receipts.COVERAGE_KEYS}
        self.assertFalse(receipts.validate_receipt(legacy))

        contemporary = copy.deepcopy(legacy)
        contemporary["record_kind"] = "contemporaneous_receipt"
        contemporary["analysis_at"] = "2026-07-25T19:30:00Z"
        self.assertTrue(
            any("unknown_legacy" in error for error in receipts.validate_receipt(contemporary))
        )

        legacy["evidence_depth"] = "complete_fulltext_read"
        self.assertTrue(
            any("unknown_legacy" in error for error in receipts.validate_receipt(legacy))
        )

    def test_missing_ledger_fails_closed_for_reads(self) -> None:
        with self.assertRaisesRegex(ValueError, "ledger does not exist"):
            receipts.load_ledger(self.ledger)

    @unittest.skipIf(fcntl is None, "POSIX file locking unavailable")
    def test_append_waits_for_exclusive_ledger_lock(self) -> None:
        self.ledger.touch()
        context = multiprocessing.get_context("spawn")
        result_queue = context.Queue()
        with self.ledger.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            process = context.Process(
                target=append_worker,
                args=(str(self.ledger), result_queue),
            )
            process.start()
            time.sleep(0.25)
            self.assertTrue(process.is_alive(), "append bypassed the exclusive ledger lock")
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        process.join(timeout=5)
        self.assertEqual(process.exitcode, 0)
        self.assertEqual(result_queue.get(timeout=1), "recorded")
        self.assertEqual(len(receipts.load_ledger(self.ledger)), 1)

    def test_repeat_complete_read_needs_reason_and_lineage(self) -> None:
        first = example("FTR-20260725-42193054-01")
        receipts.append_receipt(self.ledger, first)
        duplicate = example("FTR-20260725-42193054-02")
        with self.assertRaisesRegex(ValueError, "prior_receipt"):
            receipts.append_receipt(self.ledger, duplicate)

        reread = copy.deepcopy(duplicate)
        reread["prior_receipt"] = first["event_id"]
        reread["reread_reason"] = "adversarial_reanalysis"
        receipts.append_receipt(self.ledger, reread)
        self.assertEqual(len(receipts.load_ledger(self.ledger)), 2)

    def test_receipt_correction_can_change_outputs_but_not_reading_evidence(self) -> None:
        first = example("FTR-20260725-42193054-01")
        receipts.append_receipt(self.ledger, first)
        correction = copy.deepcopy(first)
        correction.update({
            "event_id": "FTR-20260725-42193054-02",
            "event_at": "2026-07-25T21:00:00Z",
            "workflow": "output-path correction; no reread",
            "outputs": ["correct_dossier_42193054.md"],
            "evidence_basis": ["prior receipt", "correct output"],
            "prior_receipt": first["event_id"],
            "reread_reason": "receipt_correction",
        })
        receipts.append_receipt(self.ledger, correction)
        index = receipts.receipt_depth_index(self.ledger)
        self.assertEqual(correction["event_id"], index["pmid:42193054"]["event_id"])

        bad = copy.deepcopy(correction)
        bad.update({
            "event_id": "FTR-20260725-42193054-03",
            "event_at": "2026-07-25T22:00:00Z",
            "prior_receipt": correction["event_id"],
            "coverage": dict(correction["coverage"], supplementary="unavailable"),
        })
        with self.assertRaisesRegex(ValueError, "changed substantive fields"):
            receipts.append_receipt(self.ledger, bad)

    def test_receipt_invalidation_quarantines_a_misattributed_legacy_event(self) -> None:
        """Append-only history can retract an index claim without rewriting the bad event."""
        legacy = example("FTR-20260725-42193054-01", "partial_fulltext_read")
        legacy["record_kind"] = "legacy_reconstruction"
        legacy["analysis_at"] = None
        legacy["coverage"] = {key: "unknown_legacy" for key in receipts.COVERAGE_KEYS}
        receipts.append_receipt(self.ledger, legacy)

        invalidation = copy.deepcopy(legacy)
        invalidation.update({
            "event_id": "FTR-20260725-42193054-02",
            "event_at": "2026-07-25T21:00:00Z",
            "record_kind": "receipt_invalidation",
            "workflow": "identity audit; no reread",
            "evidence_basis": ["the persisted output belongs to a different PMID"],
            "prior_receipt": legacy["event_id"],
            "reread_reason": "receipt_invalidation",
            "invalidates_receipt": legacy["event_id"],
            "invalidation_reason": (
                "The legacy reconstruction points to a PAPER entry owned by a different "
                "PMID, so it cannot attest reading depth for this study."
            ),
        })
        receipts.append_receipt(self.ledger, invalidation)

        self.assertEqual(len(receipts.load_ledger(self.ledger)), 2)
        self.assertFalse(receipts.receipt_depth_index(self.ledger))

        bad = copy.deepcopy(invalidation)
        bad.update({
            "event_id": "FTR-20260725-42193054-03",
            "event_at": "2026-07-25T22:00:00Z",
            "prior_receipt": invalidation["event_id"],
            "invalidates_receipt": invalidation["event_id"],
            "invalidation_reason": "too short",
        })
        with self.assertRaisesRegex(ValueError, "substantive invalidation_reason"):
            receipts.append_receipt(self.ledger, bad)

    def test_cited_or_different_study_does_not_match(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipts.append_receipt(self.ledger, receipt)
        self.assertFalse(receipts.same_study(receipt, "22222222", "10.1000/other"))

    def test_partial_receipt_does_not_masquerade_as_complete(self) -> None:
        receipt = example("FTR-20260725-42193054-01", "partial_fulltext_read")
        receipt["coverage"]["supplementary"] = "not_read"
        self.assertFalse(receipts.validate_receipt(receipt))
        receipts.append_receipt(self.ledger, receipt)
        self.assertEqual(receipts.load_ledger(self.ledger)[0]["evidence_depth"], "partial_fulltext_read")

    def test_partial_to_complete_keeps_lineage(self) -> None:
        partial = example("FTR-20260725-42193054-01", "partial_fulltext_read")
        partial["coverage"]["supplementary"] = "not_read"
        receipts.append_receipt(self.ledger, partial)
        complete = example("FTR-20260725-42193054-02")
        with self.assertRaisesRegex(ValueError, "prior_receipt"):
            receipts.append_receipt(self.ledger, complete)
        complete["prior_receipt"] = partial["event_id"]
        complete["reread_reason"] = "inadequate_prior_coverage"
        receipts.append_receipt(self.ledger, complete)
        self.assertEqual(len(receipts.load_ledger(self.ledger)), 2)

    def test_persisted_events_are_chained_and_rewriting_history_is_detected(self) -> None:
        first = receipts.append_receipt(self.ledger, example("FTR-20260725-42193054-01"))
        second = example("FTR-20260725-42193054-02", "partial_fulltext_read")
        second["coverage"]["supplementary"] = "not_read"
        second["prior_receipt"] = first["event_id"]
        second["reread_reason"] = "adversarial_reanalysis"
        receipts.append_receipt(self.ledger, second)

        self.assertIsNone(first[receipts.CHAIN_FIELD])
        loaded = receipts.load_ledger(self.ledger)
        self.assertEqual(loaded[1][receipts.CHAIN_FIELD], receipts.receipt_digest(loaded[0]))

        # Edit the first event in place: every later link must stop matching.
        lines = self.ledger.read_text(encoding="utf-8").splitlines()
        tampered = json.loads(lines[0])
        tampered["workflow"] = "rewritten-after-the-fact"
        lines[0] = json.dumps(tampered, ensure_ascii=False, sort_keys=True)
        self.ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "broken hash chain"):
            receipts.load_ledger(self.ledger)

    def test_deleting_a_historical_event_breaks_the_chain(self) -> None:
        first = receipts.append_receipt(self.ledger, example("FTR-20260725-42193054-01"))
        second = example("FTR-20260725-42193054-02")
        second["prior_receipt"] = first["event_id"]
        second["reread_reason"] = "explicit_operator_request"
        receipts.append_receipt(self.ledger, second)
        lines = self.ledger.read_text(encoding="utf-8").splitlines()
        self.ledger.write_text(lines[1] + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "broken hash chain"):
            receipts.load_ledger(self.ledger)

    def _chain_of_two(self) -> dict:
        first = receipts.append_receipt(self.ledger, example("FTR-20260725-42193054-01"))
        second = example("FTR-20260725-42193054-02", "partial_fulltext_read")
        second["coverage"]["supplementary"] = "not_read"
        second["prior_receipt"] = first["event_id"]
        second["reread_reason"] = "adversarial_reanalysis"
        return receipts.append_receipt(self.ledger, second)

    def _rewrite_line(self, position: int, **changes) -> None:
        lines = self.ledger.read_text(encoding="utf-8").splitlines()
        record = json.loads(lines[position])
        record.update(changes)
        lines[position] = json.dumps(record, ensure_ascii=False, sort_keys=True)
        self.ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def _third_event(self) -> dict:
        follow_up = example("FTR-20260725-42193054-03", "partial_fulltext_read")
        follow_up["coverage"]["supplementary"] = "not_read"
        follow_up["prior_receipt"] = "FTR-20260725-42193054-02"
        follow_up["reread_reason"] = "new_question_outside_prior_coverage"
        return follow_up

    def test_appending_onto_a_rewritten_body_fails_closed(self) -> None:
        """The lock protects concurrency; this protects against extending a corrupted past."""
        self._chain_of_two()
        self._rewrite_line(0, workflow="rewritten-after-the-fact")
        with self.assertRaisesRegex(ValueError, "broken hash chain"):
            receipts.append_receipt(self.ledger, self._third_event())

    def test_appending_cannot_launder_a_rewritten_head(self) -> None:
        """A chain leaves its own last link unbound; only the anchor can hold it.

        Without this check the sequence "edit the newest event, append a fresh one, let the
        append re-anchor" would convert a tampered head into permanently verified history.
        """
        self._chain_of_two()
        manifest = Path(self.temporary.name) / "state_manifest_current.md"
        manifest.write_text(
            "fulltext_ledger_events: 0\nfulltext_ledger_head: null\n", encoding="utf-8"
        )
        receipts.write_state_anchor(manifest, receipts.load_ledger(self.ledger))

        self._rewrite_line(1, evidence_depth="complete_fulltext_read",
                           coverage={key: "read" for key in receipts.COVERAGE_KEYS})
        # The chain alone still sees nothing wrong: the edited record is the last one.
        self.assertFalse(receipts.validate_ledger_chain(receipts.load_ledger(self.ledger)))
        with self.assertRaisesRegex(ValueError, "refusing to append onto unverified history"):
            receipts.append_receipt(self.ledger, self._third_event(), manifest=manifest)

    def test_manifest_bound_append_updates_the_anchor_before_success(self) -> None:
        self.ledger.touch()
        manifest = Path(self.temporary.name) / "state_manifest_current.md"
        manifest.write_text(
            "fulltext_ledger_events: 0\nfulltext_ledger_head: null\n",
            encoding="utf-8",
        )
        persisted = receipts.append_receipt(
            self.ledger,
            example("FTR-20260725-42193054-01"),
            manifest=manifest,
        )
        loaded = receipts.load_ledger(self.ledger)
        self.assertEqual(loaded, [persisted])
        self.assertFalse(
            receipts.validate_state_anchor(manifest.read_text(encoding="utf-8"), loaded)
        )

    def test_failed_anchor_update_rolls_back_the_uncommitted_append(self) -> None:
        self.ledger.touch()
        manifest = Path(self.temporary.name) / "state_manifest_current.md"
        manifest.write_text(
            "fulltext_ledger_events: 0\nfulltext_ledger_head: null\n",
            encoding="utf-8",
        )
        with mock.patch.object(
            receipts, "write_state_anchor", side_effect=OSError("simulated anchor failure")
        ):
            with self.assertRaisesRegex(OSError, "simulated anchor failure"):
                receipts.append_receipt(
                    self.ledger,
                    example("FTR-20260725-42193054-01"),
                    manifest=manifest,
                )
        self.assertEqual(receipts.load_ledger(self.ledger), [])

    def test_manifest_bound_append_refuses_an_absent_anchor(self) -> None:
        """The public persistence route may not silently downgrade its integrity mode."""
        self._chain_of_two()
        manifest = Path(self.temporary.name) / "state_manifest_current.md"
        manifest.write_text("current_state: READY\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "exactly one fulltext_ledger_events"):
            receipts.append_receipt(self.ledger, self._third_event(), manifest=manifest)
        self.assertEqual(len(receipts.load_ledger(self.ledger)), 2)

    def test_tail_truncation_is_invisible_to_the_chain_and_caught_by_the_anchor(self) -> None:
        first = receipts.append_receipt(self.ledger, example("FTR-20260725-42193054-01"))
        second = example("FTR-20260725-42193054-02", "partial_fulltext_read")
        second["coverage"]["supplementary"] = "not_read"
        second["prior_receipt"] = first["event_id"]
        second["reread_reason"] = "adversarial_reanalysis"
        receipts.append_receipt(self.ledger, second)
        manifest = Path(self.temporary.name) / "state_manifest_current.md"
        manifest.write_text(
            "fulltext_ledger_events: 0\nfulltext_ledger_head: null\n", encoding="utf-8"
        )
        self.assertTrue(receipts.write_state_anchor(manifest, receipts.load_ledger(self.ledger)))
        anchored = manifest.read_text(encoding="utf-8")
        self.assertFalse(receipts.validate_state_anchor(anchored, receipts.load_ledger(self.ledger)))

        lines = self.ledger.read_text(encoding="utf-8").splitlines()
        self.ledger.write_text(lines[0] + "\n", encoding="utf-8")
        survivors = receipts.load_ledger(self.ledger)
        # The chain cannot see this: the surviving prefix is still perfectly consistent.
        self.assertFalse(receipts.validate_ledger_chain(survivors))
        problems = receipts.validate_state_anchor(anchored, survivors)
        self.assertTrue(any("truncated" in problem for problem in problems))

    def test_absent_tail_anchor_is_itself_a_failure(self) -> None:
        receipts.append_receipt(self.ledger, example("FTR-20260725-42193054-01"))
        problems = receipts.validate_state_anchor("no anchor here\n", receipts.load_ledger(self.ledger))
        self.assertTrue(any("exactly one fulltext_ledger_events" in problem for problem in problems))

    def test_local_artifact_receipt_must_bind_to_a_digest(self) -> None:
        receipt = example("FTR-20260725-42193054-01")
        receipt["source_locator"] = "files/fulltext/PMID42193054.pdf"
        self.assertTrue(
            any("requires source_fingerprint" in error for error in receipts.validate_receipt(receipt))
        )
        receipt["source_fingerprint"] = "a" * 64
        self.assertFalse(receipts.validate_receipt(receipt))

        for locator in ("paper.pdf", "file:///tmp/paper.pdf", r"C:\\fulltext\\paper.pdf"):
            local = example("FTR-20260725-42193054-01")
            local["source_locator"] = locator
            self.assertTrue(
                any(
                    "requires source_fingerprint" in error
                    for error in receipts.validate_receipt(local)
                ),
                locator,
            )

        # A remote locator has nothing to hash, and a legacy record cannot hash what it
        # never witnessed: neither is required to invent a digest.
        for locator in ("PMC123", "https://example.org/article", "10.1000/example"):
            remote = example("FTR-20260725-42193054-01")
            remote["source_locator"] = locator
            self.assertFalse(receipts.validate_receipt(remote), locator)
        legacy = example("FTR-20260725-42193054-01", "partial_fulltext_read")
        legacy["record_kind"] = "legacy_reconstruction"
        legacy["analysis_at"] = None
        legacy["source_locator"] = "files/fulltext/PMID42193054.pdf"
        legacy["coverage"] = {key: "unknown_legacy" for key in receipts.COVERAGE_KEYS}
        self.assertFalse(receipts.validate_receipt(legacy))

    def test_authored_receipts_carry_no_integrity_bookkeeping(self) -> None:
        """A skill emits the protocol receipt; the ledger owns the chain field."""
        self.assertNotIn(receipts.CHAIN_FIELD, receipts.REQUIRED)
        authored = example("FTR-20260725-42193054-01")
        self.assertFalse(receipts.validate_receipt(authored))
        stray = example("FTR-20260725-42193054-01")
        stray["invented_field"] = "x"
        self.assertTrue(any("unknown fields" in error for error in receipts.validate_receipt(stray)))

    def test_legacy_reconstruction_is_explicit_and_evidence_based(self) -> None:
        legacy = example("FTR-20260725-42193054-01", "partial_fulltext_read")
        legacy["record_kind"] = "legacy_reconstruction"
        legacy["analysis_at"] = None
        legacy["evidence_basis"] = []
        self.assertTrue(
            any("evidence_basis" in error for error in receipts.validate_receipt(legacy))
        )
        legacy["evidence_basis"] = ["surviving dossier with partial coverage"]
        self.assertFalse(receipts.validate_receipt(legacy))

    def test_repeated_study_lineage_must_link_the_latest_event(self) -> None:
        first = receipts.append_receipt(self.ledger, example("FTR-20260725-42193054-01"))
        second = example("FTR-20260725-42193054-02", "partial_fulltext_read")
        second["coverage"]["supplementary"] = "not_read"
        second["prior_receipt"] = first["event_id"]
        second["reread_reason"] = "new_question_outside_prior_coverage"
        receipts.append_receipt(self.ledger, second)

        third = example("FTR-20260725-42193054-03")
        third["prior_receipt"] = first["event_id"]
        third["reread_reason"] = "adversarial_reanalysis"
        with self.assertRaisesRegex(ValueError, "latest prior_receipt"):
            receipts.append_receipt(self.ledger, third)


if __name__ == "__main__":
    unittest.main(verbosity=2)
