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

    def test_a_negated_audit_status_is_not_audit_evidence(self) -> None:
        """Mirror F2 G2: `audit_status: "NOT AUDITED - pending"` read as STRUCTURED."""
        write(self.dir, "a.json", [
            {"proposition": "p", "anchor": "Figure 1",
             "audit_status": "NOT AUDITED \u2014 pending 2026-09-12",
             "contradicts_locator": {"manifest": "b.json", "entry": 3}},
        ])
        result = tool.screen(self.dir)
        self.assertEqual(1, len(result.declared))
        self.assertEqual("NONE", result.declared[0].audit_evidence)

    def test_a_manifest_level_audit_key_never_credits_an_entry(self) -> None:
        """Mirror F2 G1: a top-level `figure_audit_table` credited every contradiction."""
        write(self.dir, "a.json", [
            {"proposition": "p", "anchor": "Figure 1",
             "contradicts_locator": {"manifest": "b.json", "entry": 3}},
        ], figure_audit_table="see dossier", audit_note="all figures audited 2026-09-09")
        self.assertEqual("NONE", tool.screen(self.dir).declared[0].audit_evidence)

    def test_a_dated_positive_audit_status_is_structured(self) -> None:
        write(self.dir, "a.json", [
            {"proposition": "p", "anchor": "Figure 1",
             "audit_status": "AUDITED 2026-09-09 - blind locator audit, verdict applied",
             "contradicts_locator": {"manifest": "b.json", "entry": 3}},
        ])
        self.assertEqual("STRUCTURED", tool.screen(self.dir).declared[0].audit_evidence)

    def test_a_string_declaration_is_malformed_not_invisible(self) -> None:
        """Mirror F2: `contradicts_locator: "yes"` was silently not a declaration."""
        write(self.dir, "a.json", [
            {"proposition": "p", "anchor": "Figure 1", "contradicts_locator": "yes"},
        ])
        result = tool.screen(self.dir)
        self.assertEqual([], result.declared)
        self.assertEqual(1, len(result.malformed))
        self.assertIn("MALFORMED", tool.render(result, False))

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


class TheSilentReversalIsVisibleAsADiff(unittest.TestCase):
    """Mirror REV-EXPOST-20260911-001 F2 (MF-3b): an in-place reversal with no declaration
    passes every file-level gate; only history shows it. A throwaway git repository with dated
    commits is the fixture, so the same-day / cross-date distinction is exercised, not assumed.
    """

    REL = "disease-models/wwox/research/deepdive_manifests/PMID11111111.json"

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.path = self.root / self.REL
        self.path.parent.mkdir(parents=True)
        self._git("init", "-q", "-b", "main")
        self._git("config", "user.email", "fixture@invalid")
        self._git("config", "user.name", "fixture")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _git(self, *args: str, date: str = "2026-09-01T10:00:00") -> None:
        import os
        import subprocess
        env = dict(os.environ, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
        subprocess.run(["git", "-C", str(self.root), *args], check=True, env=env,
                       capture_output=True)

    def _commit(self, entries: list[dict], date: str) -> None:
        self.path.write_text(json.dumps({"pmid": "11111111",
                                         "verbatim_locators": {"entries": entries}}),
                             encoding="utf-8")
        self._git("add", "-A", date=date)
        self._git("commit", "-q", "-m", f"revision {date}", date=date)

    ORIGINAL = [{"proposition": "control 4/18 versus cKO 11/12 developed liver tumours",
                 "snippet": "Eleven of twelve cKO mice developed tumours", "anchor": "Fig 6A"},
                {"proposition": "unchanged", "snippet": "unchanged sentence", "anchor": "Fig 1"}]

    def test_no_git_repository_is_void_not_clean(self) -> None:
        with tempfile.TemporaryDirectory() as plain:
            d = Path(plain) / "m"
            d.mkdir()
            (d / "a.json").write_text("{}", encoding="utf-8")
            self.assertEqual("INSUFFICIENT_DATA", tool.screen_history(d).verdict)
            self.assertEqual(3, tool.main(["--history", "--manifest-dir", str(d)]))

    def test_a_cross_date_reversal_with_no_declaration_is_listed(self) -> None:
        self._commit(self.ORIGINAL, "2026-09-01T10:00:00")
        reversed_ = json.loads(json.dumps(self.ORIGINAL))
        reversed_[0]["proposition"] = "NOT: " + reversed_[0]["proposition"]
        self._commit(reversed_, "2026-09-09T10:00:00")
        result = tool.screen_history(self.path.parent)
        self.assertEqual("SCREENED", result.verdict)
        self.assertEqual(1, result.revision_pairs)
        listed = result.undeclared(include_same_day=False)
        self.assertEqual(1, len(listed))
        self.assertEqual((0, "proposition", True), (listed[0].entry, listed[0].field, listed[0].cross_date))
        self.assertIn("NOT:", listed[0].after)

    def test_a_same_day_edit_is_counted_but_not_listed_by_default(self) -> None:
        self._commit(self.ORIGINAL, "2026-09-01T10:00:00")
        edited = json.loads(json.dumps(self.ORIGINAL))
        edited[1]["snippet"] = "unchanged sentence, re-anchored"
        self._commit(edited, "2026-09-01T15:00:00")
        result = tool.screen_history(self.path.parent)
        self.assertEqual(0, len(result.undeclared(include_same_day=False)))
        self.assertEqual(1, result.same_day_undeclared)
        self.assertEqual(1, len(result.undeclared(include_same_day=True)))

    def test_a_declared_revision_is_not_a_candidate(self) -> None:
        self._commit(self.ORIGINAL, "2026-09-01T10:00:00")
        declared = json.loads(json.dumps(self.ORIGINAL))
        declared[0]["proposition"] = "control 4/18 versus cKO 11/12 — stacked by genotype within outcome"
        declared[0]["contradicts_locator"] = {"manifest": self.REL, "entry": 0,
                                             "what_changed": "read at 400 dpi, bars stacked by genotype"}
        self._commit(declared, "2026-09-09T10:00:00")
        result = tool.screen_history(self.path.parent)
        self.assertEqual(1, len(result.revisions))
        self.assertTrue(result.revisions[0].declared)
        self.assertEqual([], result.undeclared(include_same_day=True))

    def test_the_working_tree_is_checked_before_it_lands(self) -> None:
        self._commit(self.ORIGINAL, "2026-09-01T10:00:00")
        reversed_ = json.loads(json.dumps(self.ORIGINAL))
        reversed_[0]["snippet"] = "One of twelve cKO mice developed tumours"
        self.path.write_text(json.dumps({"pmid": "11111111",
                                         "verbatim_locators": {"entries": reversed_}}),
                             encoding="utf-8")
        result = tool.screen_working_tree(self.path.parent)
        self.assertEqual(1, len(result.undeclared(include_same_day=True)))
        self.assertEqual("WORKING_TREE", result.revisions[0].commit)
        self.assertEqual(1, tool.main(["--working-tree", "--fail-on-undeclared",
                                       "--manifest-dir", str(self.path.parent)]))
        self.assertEqual(0, tool.main(["--working-tree", "--manifest-dir", str(self.path.parent)]))

    def test_a_clean_working_tree_exits_zero_under_the_gate(self) -> None:
        self._commit(self.ORIGINAL, "2026-09-01T10:00:00")
        self.assertEqual(0, tool.main(["--working-tree", "--fail-on-undeclared",
                                       "--manifest-dir", str(self.path.parent)]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
