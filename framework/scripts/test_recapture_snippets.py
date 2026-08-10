#!/usr/bin/env python3
"""Regressions for the snippet re-capture, and for the join fix that made it necessary.

Two halves of one job. The join fix changes what the artifact text IS; the re-capture repairs
the quotes the old text had contaminated. Testing either alone would leave the other able to
regress silently, which is the coupling the commit exists to enforce.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import deepdive_manifest as dm  # noqa: E402
import recapture_snippets as rc  # noqa: E402


class TheJoinNoLongerFabricatesASpace(unittest.TestCase):
    """🔴 `<italic>WWOX</italic>‐DEE` is one word. It was extracted as two."""

    def test_an_inline_element_does_not_interrupt_a_word(self) -> None:
        body, _abstract = dm._xml_surfaces(
            b"<article><body><p>our <italic>WWOX</italic>-DEE patients</p></body></article>")
        self.assertIn("WWOX-DEE", body)
        self.assertNotIn("WWOX -DEE", body)

    def test_a_block_element_still_separates(self) -> None:
        """Otherwise the fix would glue two sentences into one word."""
        body, _abstract = dm._xml_surfaces(
            b"<article><body><p>first</p><p>second</p></body></article>")
        self.assertIn("first second", body)

    def test_the_same_holds_for_html(self) -> None:
        body, _abstract = dm._html_surfaces(
            b"<html><body><p>our <i>WWOX</i>-DEE patients</p><p>next</p></body></html>")
        self.assertIn("WWOX-DEE", body)
        self.assertIn("patients next", body)

    def test_the_abstract_is_still_separated(self) -> None:
        """The join changed; the surface split it protects did not."""
        body, abstract = dm._xml_surfaces(
            b"<article><abstract><p>only here</p></abstract>"
            b"<body><p>elsewhere</p></body></article>")
        self.assertIn("only here", abstract)
        self.assertNotIn("only here", body)

    def test_a_printable_substitution_is_still_refused(self) -> None:
        """🔴 The failure mode the join fix must NOT introduce.

        A more permissive normaliser would hide exactly the printable substitutions the 5d
        sentinel exists to find. It cannot here, and this pins the reason: the screen runs on
        the raw decoded bytes upstream of any joining, so the two never meet.
        """
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "suspect.xml"
            path.write_bytes(
                "<article><body><p>Ca2\x0c, inorganic phos-</p></body></article>".encode())
            with self.assertRaises(ValueError) as caught:
                dm._artifact_text(path, "article_text")
            self.assertIn("SUSPECT", str(caught.exception))

    def test_a_clean_surface_stops_producing_the_fabricated_space(self) -> None:
        """The other half: a fix that changed nothing would pass the test above too."""
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "clean.xml"
            path.write_bytes(
                b"<article><body><p>the <italic>Wwox</italic>-null mouse</p></body></article>")
            body, _abstract = dm._artifact_text(path, "article_text")
            self.assertIn("Wwox-null", body)


class TheReCaptureTakesTheAuthorsCharacters(unittest.TestCase):
    TEXT = "the Wwox-null mouse showed no difference between groups (Fig. 2A) and then stopped"

    def test_a_fabricated_space_is_removed_by_re_taking_the_span(self) -> None:
        span, reason = rc.retake("the Wwox -null mouse showed no difference", self.TEXT)
        self.assertEqual(reason, "re-taken")
        self.assertEqual(span, "the Wwox-null mouse showed no difference")

    def test_a_quote_that_already_verifies_is_left_alone(self) -> None:
        span, reason = rc.retake("no difference between groups", self.TEXT)
        self.assertIsNone(span)
        self.assertEqual(reason, "already strict")

    def test_edge_punctuation_the_quote_carried_is_restored(self) -> None:
        """`(Fig. 2A )` came back as `(Fig. 2A` — verbatim, and missing a bracket."""
        span, reason = rc.retake("difference between groups (Fig. 2A )", self.TEXT)
        self.assertEqual(reason, "re-taken")
        self.assertTrue(span.endswith("(Fig. 2A)"), span)

    def test_punctuation_the_quote_did_not_carry_is_not_annexed(self) -> None:
        span, _reason = rc.retake("the Wwox -null mouse", self.TEXT)
        self.assertEqual(span, "the Wwox-null mouse")

    def test_an_ambiguous_span_is_refused_rather_than_chosen(self) -> None:
        """🔴 `_quote_matches` takes the first occurrence, which is safe for a VERDICT and
        unsafe for a REPAIR: the wrong occurrence would be copied in and would then verify."""
        twice = "the Wwox-null held (Fig. 1). Later, the Wwox-null held (Fig. 3)."
        span, reason = rc.retake("the Wwox -null held", twice)
        self.assertIsNone(span)
        self.assertIn("occur 2 times", reason)

    def test_words_absent_from_the_artifact_are_refused(self) -> None:
        span, reason = rc.retake("a sentence this paper never contained at all", self.TEXT)
        self.assertIsNone(span)
        self.assertIn("do not occur", reason)

    def test_the_result_verifies_strictly(self) -> None:
        """A repair that cannot be verified by the check that rejected the original is not one."""
        span, _reason = rc.retake("the Wwox -null mouse showed no difference", self.TEXT)
        self.assertEqual(dm._quote_matches(span, self.TEXT), (True, "strict"))

    def test_the_folded_key_is_unchanged_by_the_repair(self) -> None:
        """The words, their order and their digits may not move — only the characters the
        fold discards. This is the property the three earlier anchor-based attempts broke."""
        original = "the Wwox -null mouse showed no difference"
        span, _reason = rc.retake(original, self.TEXT)
        self.assertEqual(dm._match_key(span), dm._match_key(original))


if __name__ == "__main__":
    unittest.main(verbosity=2)
