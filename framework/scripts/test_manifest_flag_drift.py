#!/usr/bin/env python3
"""Regressions for `manifest_flag_drift.py`.

Written against the BEHAVIOUR wanted, not against what the implementation happens to do.
The case that motivated the tool is `test_the_case_that_motivated_it`, reproduced from the
real 2026-09-09 edit on PMID 38499540.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manifest_flag_drift import _has_note, improvements  # noqa: E402


class FlagDriftTests(unittest.TestCase):

    def test_the_case_that_motivated_it(self):
        """multihop.performed false -> true with no note is reported."""
        older = {"multihop": {"performed": False, "references_enumerated": 55}}
        newer = {"multihop": {"performed": True, "references_enumerated": 73}}
        self.assertEqual(improvements(older, newer),
                         ["multihop.performed: false -> true"])

    def test_a_NEW_note_in_the_same_block_silences_it(self):
        """The tool asks for a sentence; a sentence written in THIS edit is accepted."""
        older = {"multihop": {"performed": False}}
        newer = {"multihop": {"performed": True,
                              "performed_note_20260909": "resolved refs 17 and 38 this wave"}}
        self.assertEqual(improvements(older, newer), [])

    def test_a_PREEXISTING_note_does_NOT_silence_it(self):
        """The regression for the bug that made v1 useless on real data.

        The multihop block of PMID38499540.json already carried a long-standing `note` about
        which reference number is which. A presence check was satisfied by that month-old
        prose and returned PASS on the exact edit this tool was written to catch.
        """
        stale = "The reference list holds 55 entries, and ref 36 is the conflict."
        older = {"multihop": {"performed": False, "note": stale}}
        newer = {"multihop": {"performed": True, "note": stale}}
        self.assertEqual(improvements(older, newer),
                         ["multihop.performed: false -> true"])

    def test_a_CHANGED_note_silences_it(self):
        """Editing the existing note in the same revision is acknowledgement too."""
        older = {"multihop": {"performed": False, "note": "nothing resolved yet"}}
        newer = {"multihop": {"performed": True, "note": "resolved ref 17 this wave"}}
        self.assertEqual(improvements(older, newer), [])

    def test_an_unrelated_note_changing_elsewhere_still_silences(self):
        """Accepted limit, stated rather than hidden: the tool cannot judge whether a note
        is ABOUT the flag, only that the author wrote something here in this edit. It prompts
        a sentence; it does not grade it."""
        older = {"multihop": {"performed": False, "note": "a"}}
        newer = {"multihop": {"performed": True, "note": "b"}}
        self.assertEqual(improvements(older, newer), [])

    def test_retraction_is_never_reported(self):
        """true -> false is the FIX. Flagging it would punish putting a flag back."""
        older = {"multihop": {"performed": True}}
        newer = {"multihop": {"performed": False}}
        self.assertEqual(improvements(older, newer), [])

    def test_waived_is_inverted(self):
        """For `waived`, un-waiving is the claim of more work, so true -> false is reported."""
        older = {"verbatim_locators": {"waived": True}}
        newer = {"verbatim_locators": {"waived": False}}
        self.assertEqual(improvements(older, newer),
                         ["verbatim_locators.waived: true -> false"])

    def test_waiving_is_not_reported(self):
        """Admitting a waiver is an admission, not an improvement."""
        older = {"verbatim_locators": {"waived": False}}
        newer = {"verbatim_locators": {"waived": True}}
        self.assertEqual(improvements(older, newer), [])

    def test_unchanged_flags_are_silent(self):
        older = {"multihop": {"performed": True}}
        newer = {"multihop": {"performed": True}}
        self.assertEqual(improvements(older, newer), [])

    def test_absent_and_non_boolean_flags_are_ignored(self):
        """A missing or non-boolean flag is deepdive_manifest.py's business, not this tool's."""
        self.assertEqual(improvements({}, {"multihop": {"performed": True}}), [])
        self.assertEqual(
            improvements({"multihop": {"performed": "yes"}},
                         {"multihop": {"performed": True}}), [])

    def test_non_dict_block_does_not_raise(self):
        """A malformed block must not crash an advisory tool."""
        self.assertEqual(improvements({"multihop": None}, {"multihop": ["x"]}), [])

    def test_every_effort_flag_is_covered(self):
        """All six declared-effort flags are detected, not just multihop."""
        for block in ("group_assessment", "field_density",
                      "corpus_crossquery", "retraction_check"):
            with self.subTest(block=block):
                self.assertEqual(
                    improvements({block: {"performed": False}},
                                 {block: {"performed": True}}),
                    [f"{block}.performed: false -> true"])

    def test_several_drifts_in_one_edit_are_all_reported(self):
        older = {"multihop": {"performed": False}, "field_density": {"performed": False}}
        newer = {"multihop": {"performed": True}, "field_density": {"performed": True}}
        self.assertEqual(len(improvements(older, newer)), 2)

    def test_note_detection_ignores_empty_and_non_string(self):
        self.assertFalse(_has_note({"note": "   "}))
        self.assertFalse(_has_note({"note": 5}))
        self.assertFalse(_has_note({"performed": True}))
        self.assertTrue(_has_note({"correction_20260810": "the first version was wrong"}))
        self.assertTrue(_has_note({"why": "already resolved upstream"}))




class DriftAnnotationTests(unittest.TestCase):
    """`drifts` surfaces every improvement; only the annotation changes."""

    def test_a_noted_drift_is_still_surfaced(self):
        """The redesign: a note annotates, it never suppresses."""
        from manifest_flag_drift import drifts
        older = {"multihop": {"performed": False, "note": "a"}}
        newer = {"multihop": {"performed": True, "note": "b"}}
        self.assertEqual(drifts(older, newer),
                         [("multihop.performed: false -> true", True)])

    def test_an_unnoted_drift_is_marked_unnoted(self):
        from manifest_flag_drift import drifts
        older = {"multihop": {"performed": False}}
        newer = {"multihop": {"performed": True}}
        self.assertEqual(drifts(older, newer),
                         [("multihop.performed: false -> true", False)])

    def test_a_stale_note_does_not_count_as_acknowledgement(self):
        from manifest_flag_drift import drifts
        stale = "written a month earlier about something else"
        older = {"multihop": {"performed": False, "note": stale}}
        newer = {"multihop": {"performed": True, "note": stale}}
        self.assertEqual(drifts(older, newer),
                         [("multihop.performed: false -> true", False)])

    def test_retraction_is_absent_from_drifts_entirely(self):
        from manifest_flag_drift import drifts
        self.assertEqual(drifts({"multihop": {"performed": True}},
                                {"multihop": {"performed": False}}), [])


if __name__ == "__main__":
    unittest.main()
