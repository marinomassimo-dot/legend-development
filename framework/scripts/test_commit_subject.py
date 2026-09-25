#!/usr/bin/env python3
"""Regressions for the commit-subject convention (`commit_subject.py`).

Verified 2026-09-14 on an isolated probe session: the runtime injects a git-status block
INCLUDING RECENT COMMIT SUBJECTS into every fresh session's context before the actor can act.
A blind verifier therefore reads the conclusions of the work it is about to verify. No file in
this repository prints that block, so the runtime side cannot be patched here; what can be
checked is the subject itself: it names the SURFACE touched, never the CONCLUSION reached, and
conclusions go in the body, which the bootstrap block does not print.

Every subject below is quoted from this repository's own history. The expectations were fixed
before `commit_subject.py` existed: the leaky ones carried a conclusion into the bootstrap block
of every session opened after them, and the clean ones are the convention as practised since.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
SCRIPT = HERE / "commit_subject.py"

LEAKY = [
    "ALDAZ-FT-A-003: PMID 28283473 read in full — the positive lung leg is real, and the model is not whole-body",
    "FT-100: il conteggio delle barre era sbagliato alla fonte, e il negativo e piu ampio",
    "BATCH_20260914_005: CLAIM 026 era un overshoot vivo in canonico, e il mirror si muove con la claim",
    "ALDAZ-VERIFY-W5: the terminus holds on every proposition, and the firewall was defeated by the session bootstrap rather than by anyone's practice",
    "ALDAZ-VERIFY-W4 closed: the withheld files reverse no verdict, and they cost me the scope of my own top-ranked finding",
    "Record the second battery run: five baseline reds, none new",
    "Riconciliazione dei 32 PMID: 19 letti su 32, e tre reperti che nessuno aveva nominato",
    "Correction: the closing report claimed every reading had an independent pass, and five did not",
]

CLEAN = [
    "deepdive_manifests: declared revision on two PMID33058734 locators; ledger: close the item",
    "queue: repair FT-100's tail; ledger: correct a finding I recorded too early",
    "BATCH_20260914_006: promote two read papers, extend CLAIM 026, repair two ledger entries",
    "queue + ledger: correct the entry count and the unassigned ordinal",
    "test_stop_policy: guard section numbers; ledger: re-point a lot and re-open three steps",
    "research: write the BLOCK-1 contract; ledger: close OBJ_2(A)",
    "checkpoint: append the end-of-session pointer for 2026-09-14",
    "self_eval: share the declaration definition and match a record by its own Identifier",
    "TASK_CLAIM ALDAZ-LOCATOR-REV-B-20260914: durable claim for two declared locator revisions after a blind R4 audit, committed alone before any edit",
    "prompt_batch_commit Phase 4.7; test_generated_surfaces_are_regenerated marker",
    "deepdive_manifest, locator_audit, scientist_reading_modes: add the rendered_text locator surface",
    "Merge branch 'refs/heads/task/plan-mandate-continuity'",
]


class TheSubjectNamesTheSurfaceNotTheConclusion(unittest.TestCase):
    def setUp(self) -> None:
        import commit_subject  # noqa: PLC0415 - absent before the fix, by design
        self.mod = commit_subject

    def test_every_leaky_subject_from_history_is_refused(self) -> None:
        for subject in LEAKY:
            with self.subTest(subject=subject):
                self.assertTrue(self.mod.check_subject(subject), subject)

    def test_every_clean_subject_from_history_passes(self) -> None:
        for subject in CLEAN:
            with self.subTest(subject=subject):
                self.assertEqual([], self.mod.check_subject(subject))

    def test_a_violation_names_its_rule_and_the_offending_words(self) -> None:
        found = self.mod.check_subject(LEAKY[0])
        rules = {v.rule for v in found}
        self.assertIn("CONCLUSION_IN_SUBJECT", rules)
        self.assertTrue(any("real" in v.detail or " is " in f" {v.detail} " for v in found), found)
        self.assertIn("NO_SURFACE_FIRST", {v.rule for v in self.mod.check_subject(LEAKY[5])})

    def test_only_the_first_line_is_a_subject(self) -> None:
        message = "ledger: record the verification\n\nThe verdict was SUPPORTED and the count is twelve."
        self.assertEqual([], self.mod.check_message(message))

    def test_the_cli_exits_one_on_a_leaky_message_file_and_zero_on_a_clean_one(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            leaky = Path(tmp) / "leaky"
            leaky.write_text(LEAKY[1] + "\n\nbody\n", encoding="utf-8")
            clean = Path(tmp) / "clean"
            clean.write_text(CLEAN[0] + "\n\nThe count is twelve.\n", encoding="utf-8")
            bad = subprocess.run([sys.executable, str(SCRIPT), "check", "--message-file", str(leaky)],
                                 capture_output=True, text=True)
            good = subprocess.run([sys.executable, str(SCRIPT), "check", "--message-file", str(clean)],
                                  capture_output=True, text=True)
        self.assertEqual(1, bad.returncode, bad.stdout + bad.stderr)
        self.assertIn("CONCLUSION_IN_SUBJECT", bad.stdout)
        self.assertEqual(0, good.returncode, good.stdout + good.stderr)

    def test_git_comment_lines_are_not_the_subject(self) -> None:
        """A commit-msg hook receives the editor buffer, comments included."""
        message = "# Please enter the commit message\nqueue: mint FT-113\n"
        self.assertEqual([], self.mod.check_message(message))


if __name__ == "__main__":
    unittest.main(verbosity=2)
