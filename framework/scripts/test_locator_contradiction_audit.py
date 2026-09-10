#!/usr/bin/env python3
"""Regressions for `locator_contradiction_audit.py`.

The module's `--self-test` already calls the entry point on fixtures AND on the live
corpus; this suite pins the properties that must not silently regress and runs that
self-test as one of its cases, so a green suite cannot coexist with a red self-test.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import locator_contradiction_audit as tool


def write(directory: Path, name: str, entries: list[dict], **extra) -> None:
    (directory / name).write_text(
        json.dumps({"pmid": name, "verbatim_locators": {"entries": entries}, **extra}),
        encoding="utf-8",
    )


class ContradictionScreen(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_an_empty_corpus_is_void_not_clean(self) -> None:
        result = tool.screen(self.dir)
        self.assertEqual("INSUFFICIENT_DATA", result.verdict)
        self.assertIn("no manifest JSON", result.missing)
        self.assertEqual(3, tool.main(["--manifest-dir", str(self.dir)]))

    def test_every_verdict_carries_the_digest_of_what_was_screened(self) -> None:
        write(self.dir, "a.json", [{"proposition": "p", "anchor": "Figure 1"}])
        result = tool.screen(self.dir)
        self.assertEqual(64, len(result.digest))
        self.assertGreater(result.screened_bytes, 0)
        self.assertEqual(1, result.screened_entries)

    def test_correction_language_alone_is_not_a_contradiction(self) -> None:
        """The measured reason the retrospective's proposed grep was not implemented."""
        write(self.dir, "a.json", [
            {"proposition": "the authors corrected the medium and revised the dose",
             "anchor": "Methods"},
            {"proposition": "the construct replaces exon 1", "anchor": "Figure 2"},
        ])
        result = tool.screen(self.dir)
        self.assertEqual([], result.findings)
        self.assertEqual(2, result.naive_prose_hits)

    def test_a_correction_naming_a_prior_reading_is_a_candidate(self) -> None:
        write(self.dir, "a.json", [
            {"proposition": "THIS CORRECTS THE PRIOR READING'S FIGURE-1 LOCATOR, see entries[6]",
             "anchor": "Figure 1"},
        ])
        self.assertEqual(1, len(tool.screen(self.dir).candidates))

    def test_proximity_is_measured_per_field_not_across_the_whole_entry(self) -> None:
        """Joining fields is how a detector acquires its false positives."""
        write(self.dir, "a.json", [
            {"proposition": "the medium was corrected to DMEM",
             "anchor": "Methods", "audit_status": "", "snippet": "read on 2026-01-02"},
        ])
        self.assertEqual([], tool.screen(self.dir).findings)

    def test_audit_recorded_only_in_prose_is_prose_not_none(self) -> None:
        write(self.dir, "a.json", [
            {"proposition": "value restated",
             "anchor": "Figure 4. Wording corrected after blind locator audit 2026-09-09 "
                       "(verdict OVERSHOOT)."},
        ])
        found = tool.screen(self.dir).candidates
        self.assertEqual(1, len(found))
        self.assertEqual("PROSE", found[0].audit_evidence)

    def test_a_declared_contradiction_without_an_audit_is_visible(self) -> None:
        write(self.dir, "a.json", [
            {"proposition": "p", "anchor": "Figure 1",
             "contradicts_locator": {"manifest": "b.json", "entry": 3,
                                     "what_changed": "the counts"}},
        ])
        result = tool.screen(self.dir)
        self.assertEqual(1, len(result.declared))
        self.assertEqual([], result.audited)
        self.assertEqual("NONE", result.declared[0].audit_evidence)

    def test_findings_do_not_turn_the_run_into_a_failure(self) -> None:
        """It reports a ratio; a gate that fires on everything gets switched off."""
        write(self.dir, "a.json", [
            {"proposition": "p", "anchor": "Figure 1",
             "contradicts_locator": {"manifest": "b.json", "entry": 3}},
        ])
        self.assertEqual(0, tool.main(["--manifest-dir", str(self.dir), "--queue"]))

    def test_an_unreadable_manifest_is_a_finding_not_a_crash(self) -> None:
        (self.dir / "broken.json").write_text("{not json", encoding="utf-8")
        result = tool.screen(self.dir)
        self.assertEqual("SCREENED", result.verdict)
        self.assertTrue(any(f.kind == "UNREADABLE" for f in result.findings))

    def test_the_modules_own_self_test_passes(self) -> None:
        self.assertEqual(0, tool.self_test())


if __name__ == "__main__":
    unittest.main(verbosity=2)
