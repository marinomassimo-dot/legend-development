#!/usr/bin/env python3
"""Regression suite for the needle guard in `regenerate_adjudications.py`.

The digest half of that script cannot be exercised here: regenerating a crop needs PyMuPDF
and the copyrighted PDF, and this repository ships neither. The needle half can, and it is
the half that decides whether `adjudicates` is a checkable claim or a promise — so the four
ways it must refuse are pinned here rather than in a session's scratch directory.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from regenerate_adjudications import check_needles  # noqa: E402


class Rect:
    """The two attributes of `fitz.Rect` this guard reads."""

    def __init__(self, x0: float, y0: float, x1: float, y1: float) -> None:
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1


class Page:
    """A page that knows where each needle sits, standing in for `fitz.Page`."""

    def __init__(self, spans: dict[str, list[Rect]]) -> None:
        self.spans = spans

    def search_for(self, needle: str) -> list[Rect]:
        return self.spans.get(needle, [])


PAGE = Page({
    "We detected epileptic seizures": [Rect(427, 461, 543, 470)],
    "Brain": [Rect(58, 238, 77, 246), Rect(58, 388, 77, 396)],
    "the levels of BUN,": [Rect(385, 658, 455, 667)],
})
SNIPPETS = [
    "We detected epileptic seizures in 95% of the mutant rats",
    "hearing loss at 15 KHz (88 dB) in mutant rats",
]


def artifact(*adjudicates, crop=(86, 309, 583, 605)):
    return {"file": "p02.png", "page": 2, "crop": list(crop), "adjudicates": list(adjudicates)}


class NeedleGuardTests(unittest.TestCase):
    def check(self, art, snippets=SNIPPETS):
        return check_needles(PAGE, art, snippets, "17803050 p02.png")

    def test_a_needle_that_resolves_inside_its_crop_passes(self):
        self.assertEqual(
            self.check(artifact({"locator": "entries[0]",
                                 "needle": "We detected epileptic seizures"})),
            [])

    def test_a_bare_locator_is_refused(self):
        """The shape the recipe had before needles: nothing to check the promise against."""
        problems = self.check(artifact("entries[0]"))
        self.assertEqual(len(problems), 1)
        self.assertIn("bare locator", problems[0])

    def test_a_needle_that_matches_twice_does_not_identify_a_location(self):
        problems = self.check(artifact({"locator": "entries[0]", "needle": "Brain"},
                                       crop=(40, 62, 570, 250)))
        self.assertEqual(len(problems), 1)
        self.assertIn("matches 2 span(s)", problems[0])

    def test_a_needle_that_matches_nothing_is_refused(self):
        problems = self.check(artifact({"locator": "entries[0]", "needle": "not on this page"}))
        self.assertEqual(len(problems), 1)
        self.assertIn("matches 0 span(s)", problems[0])

    def test_a_crop_that_stops_before_its_span_is_refused(self):
        """The 2026-08-09 defect: a table crop ending at x=320 while the row ran to x=524."""
        problems = self.check(artifact({"locator": "entries[0]",
                                        "needle": "We detected epileptic seizures"},
                                       crop=(86, 309, 320, 605)))
        self.assertEqual(len(problems), 1)
        self.assertIn("does not contain the span", problems[0])

    def test_a_needle_that_names_one_locator_and_quotes_another_is_refused(self):
        """Unique, inside the crop, and evidence for a different sentence entirely.

        A crop containing the right region is not evidence that it contains *this* locator.
        This is the case the manifest link exists for, and the only one the geometry misses.
        """
        problems = self.check(artifact({"locator": "entries[1]",
                                        "needle": "We detected epileptic seizures"}))
        self.assertEqual(len(problems), 1)
        self.assertIn("not a fragment of the snippet", problems[0])

    def test_a_locator_the_manifest_does_not_have_is_refused(self):
        problems = self.check(artifact({"locator": "entries[99]",
                                        "needle": "We detected epileptic seizures"}))
        self.assertEqual(len(problems), 1)
        self.assertIn("no such locator", problems[0])

    def test_punctuation_between_needle_and_snippet_does_not_break_the_link(self):
        """`search_for` ignores the comma the snippet carries; the fragment check must too."""
        self.assertEqual(
            check_needles(PAGE, artifact({"locator": "entries[0]",
                                          "needle": "the levels of BUN,"},
                                         crop=(300, 630, 580, 690)),
                          ["the levels of BUN CRE and female IP were higher"],
                          "17803050 p03.png"),
            [])

    def test_without_a_manifest_geometry_is_still_enforced(self):
        """Degrading must lose the fragment check and nothing else."""
        drifted = artifact({"locator": "entries[1]",
                            "needle": "We detected epileptic seizures"})
        self.assertEqual(len(self.check(drifted)), 1)          # with a manifest: refused
        self.assertEqual(check_needles(PAGE, drifted, None, "17803050 p02.png"), [])
        problems = check_needles(PAGE, artifact({"locator": "entries[0]", "needle": "Brain"}),
                                 None, "17803050 p02.png")
        self.assertEqual(len(problems), 1)
        self.assertIn("matches 2 span(s)", problems[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
