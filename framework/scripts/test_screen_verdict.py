#!/usr/bin/env python3
"""Tests for screen_verdict.py — the verdict contract every screen returns.

The suite is organised around the two 2026-09-09 near-errors the contract exists to make
unrepresentable, and each group states which mutation turns it red:

* ``CleanRequiresADigest``     — delete the CLEAN guard in ``__post_init__``.
* ``RefusalNamesItsSignature`` — delete the REFUSED guard.
* ``UninformativeInput``       — delete a branch of ``reject_uninformative``.
* ``TheDigestIsOfTheRightBytes`` — hash something other than the screened content.

The last group is the one that matters most and is the least obvious: a digest that is present
but computed over the wrong bytes is *worse* than no digest, because it looks like evidence.
``covers()`` is the caller-side question a boolean could never answer.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from screen_verdict import (  # noqa: E402
    CLEAN, INSUFFICIENT_DATA, REFUSED, ScreenContractError, ScreenVerdict, as_bytes,
    screened_of)

TEXT = "Using this protocol, osteosarcomas are detected in 100% of the post-natal mice."


class CleanRequiresADigest(unittest.TestCase):
    """🔴 The guarantee: a CLEAN verdict about bytes nobody hashed cannot be built."""

    def test_clean_without_screened_is_refused(self) -> None:
        with self.assertRaises(ScreenContractError) as caught:
            ScreenVerdict(screen="s", verdict=CLEAN)
        self.assertIn("CLEAN requires screened", str(caught.exception))

    def test_clean_over_zero_bytes_is_refused(self) -> None:
        """An empty surface matches no signature. Reporting that as clean is the silent pass."""
        with self.assertRaises(ScreenContractError):
            ScreenVerdict(screen="s", verdict=CLEAN, screened=screened_of(""))
        with self.assertRaises(ScreenContractError):
            ScreenVerdict.clean("s", "")

    def test_clean_with_content_is_allowed_and_carries_the_digest(self) -> None:
        verdict = ScreenVerdict.clean("s", TEXT, detail="signature absent")
        self.assertTrue(verdict.is_clean)
        self.assertEqual(verdict.screened["bytes"], len(TEXT.encode("utf-8")))
        self.assertEqual(verdict.digest,
                         "sha256:" + hashlib.sha256(TEXT.encode("utf-8")).hexdigest())

    def test_the_json_surface_is_not_a_way_around_the_guard(self) -> None:
        with self.assertRaises(ScreenContractError):
            ScreenVerdict.from_dict({"screen": "s", "verdict": CLEAN, "screened": None})

    def test_a_malformed_digest_is_refused(self) -> None:
        for bad in ({"digest": "abc", "bytes": 3},
                    {"digest": "sha256:xyz", "bytes": 3},
                    {"digest": "sha256:" + "a" * 64, "bytes": -1},
                    {"digest": "sha256:" + "a" * 64, "bytes": "3"}):
            with self.subTest(bad=bad), self.assertRaises(ScreenContractError):
                ScreenVerdict(screen="s", verdict=CLEAN, screened=bad)


class RefusalNamesItsSignature(unittest.TestCase):
    """B16: a refusal that cannot say what fired is a verdict nobody can check."""

    def test_refused_without_signature_is_refused(self) -> None:
        with self.assertRaises(ScreenContractError) as caught:
            ScreenVerdict(screen="s", verdict=REFUSED, screened=screened_of(TEXT))
        self.assertIn("name the signature", str(caught.exception))

    def test_refused_without_digest_is_refused(self) -> None:
        with self.assertRaises(ScreenContractError):
            ScreenVerdict(screen="s", verdict=REFUSED, signature="C0_CONTROL")

    def test_refused_names_signature_and_bytes(self) -> None:
        verdict = ScreenVerdict.refused("s", TEXT, signature="C0_CONTROL",
                                        evidence={"count": 191})
        self.assertTrue(verdict.is_refused)
        self.assertEqual(verdict.signature, "C0_CONTROL")
        self.assertEqual(verdict.evidence["count"], 191)
        self.assertIn("C0_CONTROL", verdict.render())

    def test_a_signature_on_a_clean_verdict_is_a_contract_error(self) -> None:
        with self.assertRaises(ScreenContractError):
            ScreenVerdict(screen="s", verdict=CLEAN, screened=screened_of(TEXT),
                          signature="C0_CONTROL")


class InsufficientNamesWhatIsMissing(unittest.TestCase):
    def test_insufficient_without_missing_is_refused(self) -> None:
        with self.assertRaises(ScreenContractError):
            ScreenVerdict(screen="s", verdict=INSUFFICIENT_DATA)

    def test_insufficient_distinguishes_empty_from_absent(self) -> None:
        """Different repairs: re-extract a surface, versus acquire one at all."""
        absent = ScreenVerdict.insufficient("s", missing="artifact")
        empty = ScreenVerdict.insufficient("s", missing="artifact text", data="")
        self.assertIsNone(absent.screened)
        self.assertEqual(empty.screened["bytes"], 0)

    def test_missing_on_a_clean_verdict_is_a_contract_error(self) -> None:
        with self.assertRaises(ScreenContractError):
            ScreenVerdict(screen="s", verdict=CLEAN, screened=screened_of(TEXT),
                          missing="artifact")


class UninformativeInput(unittest.TestCase):
    """The three shapes that produced a silent pass, each caught in one call."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_none_is_insufficient(self) -> None:
        verdict = ScreenVerdict.reject_uninformative("s", None, expected="surface text")
        self.assertEqual(verdict.verdict, INSUFFICIENT_DATA)
        self.assertEqual(verdict.missing, "surface text")

    def test_empty_and_whitespace_are_insufficient(self) -> None:
        for value in ("", "   \n\t "):
            with self.subTest(value=repr(value)):
                verdict = ScreenVerdict.reject_uninformative("s", value)
                self.assertEqual(verdict.verdict, INSUFFICIENT_DATA)

    def test_a_path_object_where_content_belongs_is_insufficient(self) -> None:
        """🔴 The 2026-09-09 inversion, at the contract level."""
        artefact = self.tmp / "PMID16223882.txt"
        artefact.write_text(TEXT, encoding="utf-8")
        verdict = ScreenVerdict.reject_uninformative("s", artefact, expected="surface text")
        self.assertEqual(verdict.verdict, INSUFFICIENT_DATA)
        self.assertIn("always passes", verdict.detail)

    def test_a_path_string_where_content_belongs_is_insufficient(self) -> None:
        """The exact call shape: the argument is a str, and it names a real file."""
        artefact = self.tmp / "PMID16223882.txt"
        artefact.write_text(TEXT, encoding="utf-8")
        verdict = ScreenVerdict.reject_uninformative("s", str(artefact))
        self.assertEqual(verdict.verdict, INSUFFICIENT_DATA)

    def test_genuine_content_passes_through(self) -> None:
        self.assertIsNone(ScreenVerdict.reject_uninformative("s", TEXT))
        self.assertIsNone(ScreenVerdict.reject_uninformative("s", TEXT.encode("utf-8")))

    def test_a_multiline_surface_is_never_mistaken_for_a_path(self) -> None:
        self.assertIsNone(ScreenVerdict.reject_uninformative("s", "line one\nline two"))

    def test_a_string_that_looks_like_a_path_but_is_not_on_disk_passes(self) -> None:
        """Conservative by design: only an existing single-line path is refused."""
        self.assertIsNone(
            ScreenVerdict.reject_uninformative("s", "files/fulltext/PMID99999999.txt"))


class TheDigestIsOfTheRightBytes(unittest.TestCase):
    """A digest over the wrong bytes looks like evidence and is not."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_covers_is_true_for_the_screened_bytes_only(self) -> None:
        verdict = ScreenVerdict.clean("s", TEXT)
        self.assertTrue(verdict.covers(TEXT))
        self.assertTrue(verdict.covers(TEXT.encode("utf-8")))
        self.assertFalse(verdict.covers(TEXT + " "))

    def test_a_verdict_about_a_filename_does_not_cover_the_surface(self) -> None:
        """The inversion, expressed as the question the caller can now ask."""
        artefact = self.tmp / "PMID16223882.txt"
        artefact.write_text(TEXT, encoding="utf-8")
        # A screen that (wrongly) hashed the file NAME rather than its content.
        wrong = ScreenVerdict.clean("s", artefact.name)
        self.assertFalse(wrong.covers(artefact.read_text(encoding="utf-8")))

    def test_a_path_cannot_be_hashed_as_content(self) -> None:
        with self.assertRaises(ScreenContractError) as caught:
            screened_of(Path("files/fulltext/PMID16223882.txt"))
        self.assertIn("not a path", str(caught.exception))

    def test_a_parsed_object_cannot_be_hashed_as_content(self) -> None:
        with self.assertRaises(ScreenContractError):
            screened_of({"text": TEXT})

    def test_str_and_bytes_agree(self) -> None:
        self.assertEqual(as_bytes(TEXT), TEXT.encode("utf-8"))
        self.assertEqual(screened_of(TEXT), screened_of(TEXT.encode("utf-8")))

    def test_the_digest_is_reproducible_from_the_shell(self) -> None:
        """A stored digest a later session cannot recompute is not provenance."""
        artefact = self.tmp / "surface.txt"
        artefact.write_bytes(TEXT.encode("utf-8"))
        verdict = ScreenVerdict.clean("s", artefact.read_text(encoding="utf-8"))
        on_disk = hashlib.sha256(artefact.read_bytes()).hexdigest()
        self.assertEqual(verdict.digest, "sha256:" + on_disk)


class RecordShape(unittest.TestCase):
    def test_round_trip_through_json(self) -> None:
        for verdict in (ScreenVerdict.clean("s", TEXT, detail="d"),
                        ScreenVerdict.refused("s", TEXT, signature="SIG", evidence={"n": 2}),
                        ScreenVerdict.insufficient("s", missing="artifact")):
            with self.subTest(verdict=verdict.verdict):
                again = ScreenVerdict.from_dict(json.loads(json.dumps(verdict.as_dict())))
                self.assertEqual(again, verdict)

    def test_unknown_fields_are_refused(self) -> None:
        with self.assertRaises(ScreenContractError):
            ScreenVerdict.from_dict({"screen": "s", "verdict": CLEAN,
                                     "screened": screened_of(TEXT), "extra": 1})

    def test_a_verdict_must_name_its_screen(self) -> None:
        with self.assertRaises(ScreenContractError):
            ScreenVerdict(screen="  ", verdict=CLEAN, screened=screened_of(TEXT))

    def test_an_unknown_verdict_word_is_refused(self) -> None:
        with self.assertRaises(ScreenContractError):
            ScreenVerdict(screen="s", verdict="PASS", screened=screened_of(TEXT))

    def test_the_record_is_immutable(self) -> None:
        verdict = ScreenVerdict.clean("s", TEXT)
        with self.assertRaises(Exception):
            verdict.verdict = REFUSED  # type: ignore[misc]

    def test_render_always_carries_the_digest_or_says_it_screened_nothing(self) -> None:
        self.assertIn("sha256:", ScreenVerdict.clean("s", TEXT).render())
        self.assertIn("screened nothing",
                      ScreenVerdict.insufficient("s", missing="artifact").render())


class TheContractIsUsableAsDocumented(unittest.TestCase):
    """The docstring's worked example is executed, not admired.

    A peer session implements against this module without asking its author; the example in
    the docstring is that contract's only interface documentation, so it is run here.
    """

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    @staticmethod
    def screen_surface(path: Path) -> ScreenVerdict:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            return ScreenVerdict.insufficient("my_screen", missing=f"artifact {path}",
                                              detail=str(exc))
        bad = ScreenVerdict.reject_uninformative("my_screen", text, expected="the surface text")
        if bad is not None:
            return bad
        hits = [ch for ch in text if ord(ch) < 32 and ch not in "\n\t"]
        if hits:
            return ScreenVerdict.refused("my_screen", text, signature="C0_CONTROL",
                                         detail=f"{len(hits)} control characters",
                                         evidence={"count": len(hits)})
        return ScreenVerdict.clean("my_screen", text, detail="no C0 controls")

    def test_the_three_outcomes_of_the_documented_example(self) -> None:
        good = self.tmp / "good.txt"
        good.write_text(TEXT, encoding="utf-8")
        self.assertTrue(self.screen_surface(good).is_clean)

        bad = self.tmp / "bad.txt"
        bad.write_text("P \x0c< 0.023", encoding="utf-8")
        verdict = self.screen_surface(bad)
        self.assertEqual(verdict.signature, "C0_CONTROL")

        empty = self.tmp / "empty.txt"
        empty.write_bytes(b"")
        self.assertTrue(self.screen_surface(empty).is_insufficient)

        self.assertTrue(self.screen_surface(self.tmp / "absent.txt").is_insufficient)


if __name__ == "__main__":
    unittest.main(verbosity=2)
