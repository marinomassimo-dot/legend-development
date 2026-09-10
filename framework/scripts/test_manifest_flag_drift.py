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

import json
import subprocess
import tempfile

import manifest_flag_drift as M  # noqa: E402
from manifest_flag_drift import _has_note, improvements  # noqa: E402

SCRIPT = Path(__file__).resolve().with_name("manifest_flag_drift.py")
ROOT = SCRIPT.parents[2]
MANIFESTS = Path("disease-models") / "wwox" / "research" / "deepdive_manifests"
#: The manifest of the motivating edit: multihop.performed flipped false -> true in the same
#: revision that corrected a reference count. Tracked, so it is present in a fresh clone.
MOTIVATING = MANIFESTS / "PMID38499540.json"


def run_cli(*args):
    proc = subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


def git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args],
                          capture_output=True, text=True, check=True)


class ARepoFixture:
    """A throwaway git repository holding one manifest, revision by revision."""

    def __init__(self, tmp: Path):
        self.root = tmp
        git(tmp, "init", "-q")
        git(tmp, "config", "user.email", "t@example.invalid")
        git(tmp, "config", "user.name", "t")
        self.rel = MANIFESTS / "PMID00000001.json"
        (tmp / MANIFESTS).mkdir(parents=True)

    def commit(self, manifest: dict, message: str = "rev"):
        (self.root / self.rel).write_text(json.dumps(manifest, indent=1), encoding="utf-8")
        git(self.root, "add", str(self.rel))
        git(self.root, "commit", "-q", "-m", message)


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


class TheVerdictSaysWhatWasCompared(unittest.TestCase):
    """Retrospective 9.2. The uninformative pass here is a manifest with nothing to compare."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.repo = ARepoFixture(self.tmp)

    def screen(self):
        return M.screen_manifest(self.tmp, self.repo.rel.as_posix(), 25)

    def test_a_single_revision_is_insufficient_data_not_a_pass(self):
        """🔴 The defect: a flag cannot drift across one revision, and the tool said PASS.

        Every manifest is in this state on the day it is minted. Corpus-wide, 36 of 81
        manifests in this checkout are single-revision, and all 36 were counted as scanned.
        """
        self.repo.commit({"multihop": {"performed": False}})
        verdict = self.screen()
        self.assertTrue(verdict.is_insufficient, verdict)
        self.assertIn("a second revision", verdict.missing)
        self.assertGreater(verdict.screened["bytes"], 0, "what there was, was still hashed")

    def test_an_untracked_manifest_is_insufficient_data(self):
        verdict = self.screen()
        self.assertTrue(verdict.is_insufficient, verdict)
        self.assertIn("git history", verdict.missing)
        self.assertIsNone(verdict.screened, "there were no bytes to hash")

    def test_two_revisions_without_a_drift_are_clean_and_say_how_many(self):
        self.repo.commit({"multihop": {"performed": False}})
        self.repo.commit({"multihop": {"performed": False}, "other": 1})
        verdict = self.screen()
        self.assertTrue(verdict.is_clean, verdict)
        self.assertEqual(verdict.evidence["revisions_compared"], 2)
        self.assertIn("2 revision(s) compared", verdict.detail)

    def test_a_drift_is_refused_and_names_the_signature(self):
        self.repo.commit({"multihop": {"performed": False}})
        self.repo.commit({"multihop": {"performed": True}})
        verdict = self.screen()
        self.assertTrue(verdict.is_refused, verdict)
        self.assertEqual(verdict.signature, "EFFORT_FLAG_IMPROVED")
        self.assertEqual(len(verdict.evidence["unnoted"]), 1)

    def test_the_digest_covers_the_compared_revisions_and_changes_with_depth(self):
        self.repo.commit({"multihop": {"performed": False}})
        self.repo.commit({"multihop": {"performed": False}, "a": 1})
        self.repo.commit({"multihop": {"performed": False}, "a": 2})
        deep = M.screen_manifest(self.tmp, self.repo.rel.as_posix(), 25)
        shallow = M.screen_manifest(self.tmp, self.repo.rel.as_posix(), 2)
        self.assertNotEqual(deep.digest, shallow.digest,
                            "a different range is a different screened surface")
        self.assertEqual(deep.evidence["revisions_compared"], 3)
        self.assertEqual(shallow.evidence["revisions_compared"], 2)


class TheCommandLine(unittest.TestCase):
    """Nothing in this suite entered main() until 2026-09-10."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_a_missing_manifest_directory_exits_two_and_is_not_a_pass(self):
        code, out = run_cli("--workspace", str(self.tmp))
        self.assertEqual(code, 2)
        self.assertIn("[INSUFFICIENT_DATA]", out)

    def test_the_run_separates_what_was_screened_from_what_was_not(self):
        repo = ARepoFixture(self.tmp)
        repo.commit({"multihop": {"performed": False}})
        repo.commit({"multihop": {"performed": True}})
        code, out = run_cli("--workspace", str(self.tmp))
        self.assertEqual(code, 0)
        self.assertIn("screened: 1", out)
        self.assertIn("INSUFFICIENT_DATA: 0", out)
        self.assertIn("EFFORT_FLAG_IMPROVED", out)

    def test_a_run_that_screened_nothing_exits_two(self):
        """🔴 Found by mutation: nothing asserted this, and it is the whole point.

        The directory exists and holds manifests, but none is tracked, so nothing can be
        compared. A caller that only checks for a zero exit code would read that silence as
        a clean corpus — the same defect as a screen returning CLEAN on an unscreened
        surface, one level up.
        """
        repo = ARepoFixture(self.tmp)
        (self.tmp / repo.rel).write_text('{"multihop": {"performed": false}}',
                                         encoding="utf-8")
        code, out = run_cli("--workspace", str(self.tmp))
        self.assertEqual(code, 2, out)
        self.assertIn("INSUFFICIENT_DATA: 1", out)
        self.assertIn("VERDICT: INSUFFICIENT_DATA", out)
        self.assertNotIn("VERDICT: PASS", out)

    def test_json_emits_verdict_records(self):
        repo = ARepoFixture(self.tmp)
        repo.commit({"multihop": {"performed": False}})
        code, out = run_cli("--workspace", str(self.tmp), "--json")
        records = json.loads(out)
        self.assertEqual(records[0]["verdict"], "INSUFFICIENT_DATA")
        self.assertIn("a second revision", records[0]["missing"])


class TheRealManifestOfTheMotivatingEdit(unittest.TestCase):
    """A case drawn from the corpus: the manifest whose flag flip motivated the tool."""

    def test_the_motivating_manifest_is_still_refused(self):
        if not (ROOT / MOTIVATING).exists():
            self.skipTest(f"real artefact absent: {MOTIVATING}")
        verdict = M.screen_manifest(ROOT, MOTIVATING.as_posix(), 25)
        if verdict.is_insufficient:
            self.skipTest(f"history absent in this checkout: {verdict.missing}")
        self.assertTrue(verdict.is_refused, verdict.render())
        self.assertTrue(any("multihop.performed" in text
                            for text in verdict.evidence["findings"]), verdict.evidence)
        self.assertGreaterEqual(verdict.evidence["revisions_compared"], 2)

        # 🔴 The verdict is about history; the reader is looking at the working tree. If the
        # newest compared revision is not what is on disk, the verdict describes a document
        # the reader does not have. So the working copy is opened and compared, which is also
        # what makes this a case drawn from a real corpus artefact rather than from git alone.
        on_disk = json.loads((ROOT / MOTIVATING).read_text(encoding="utf-8"))
        newest = M.manifest_at(ROOT, "HEAD", MOTIVATING.as_posix())
        self.assertEqual(on_disk, newest,
                         "the manifest on disk differs from HEAD; the verdict above is about "
                         "committed revisions, not about this file")
        # The drift stays in HISTORY whatever the flag reads today, and today it reads
        # false: the claim was retracted after the 2026-09-09 sweep. Retraction is the
        # behaviour this tool exists to encourage and is deliberately never reported as a
        # drift, so this asserts the SHAPE and not a value that is allowed to move -- the
        # first version of this line asserted True, and the corpus said otherwise.
        self.assertIsInstance(on_disk["multihop"]["performed"], bool)


if __name__ == "__main__":
    unittest.main()
