#!/usr/bin/env python3
"""Regression suite for the needle guard in `regenerate_adjudications.py`.

The digest half of that script cannot be exercised here: regenerating a crop needs PyMuPDF
and the copyrighted PDF, and this repository ships neither. The needle half can, and it is
the half that decides whether `adjudicates` is a checkable claim or a promise — so the four
ways it must refuse are pinned here rather than in a session's scratch directory.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCRIPT = HERE / "regenerate_adjudications.py"
ADJUDICATIONS = ROOT / "disease-models/wwox/research/page_adjudications"


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT,
                          capture_output=True, text=True, timeout=600)


def real_recipes() -> list[tuple[str, Path, bool]]:
    """(pmid, recipe path, source PDF present) for every recipe in this checkout — a READ."""
    found = []
    for recipe in sorted(ADJUDICATIONS.glob("PMID*/adjudications.json")):
        try:
            data = json.loads(recipe.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        source = ROOT / str(data.get("source_pdf", {}).get("path", ""))
        found.append((recipe.parent.name.removeprefix("PMID"), recipe, source.is_file()))
    return found

import deepdive_manifest as gate  # noqa: E402
import regenerate_adjudications as regenerate  # noqa: E402
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
        # check_needles now also reports how much it verified; the problems are element 0.
        return check_needles(PAGE, art, snippets, "17803050 p02.png")[0]

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
                          "17803050 p03.png")[0],
            [])

    def test_without_a_manifest_geometry_is_still_enforced(self):
        """Degrading must lose the fragment check and nothing else."""
        drifted = artifact({"locator": "entries[1]",
                            "needle": "We detected epileptic seizures"})
        self.assertEqual(len(self.check(drifted)), 1)          # with a manifest: refused
        self.assertEqual(check_needles(PAGE, drifted, None, "17803050 p02.png")[0], [])
        problems = check_needles(PAGE, artifact({"locator": "entries[0]", "needle": "Brain"}),
                                 None, "17803050 p02.png")[0]
        self.assertEqual(len(problems), 1)
        self.assertIn("matches 2 span(s)", problems[0])


class TwoImplementationsAreWorthMoreThanOne(unittest.TestCase):
    """🔴 Until 2026-08-11 this module imported `crop_contains_span` from the validator it was
    supposed to corroborate, so its geometric verdict was the validator quoting itself.

    Two implementations only buy anything if their disagreement is observable, so the pairing
    is tested rather than asserted: the containment predicate is asked in two arithmetics —
    comparison of coordinates over there, clipped-area equality here — over a grid dense
    enough to include every boundary case that matters. Flush edges, one-sided overhang on
    each of the four sides, spans larger than the crop, degenerate zero-area spans, and
    crossings that overlap without being contained.

    If a future edit changes one and not the other, this fails. That is the whole point: the
    failure mode of this repository is uneven application.
    """

    def test_the_two_implementations_agree_everywhere_on_a_dense_grid(self) -> None:
        crop = (100.0, 200.0, 300.0, 400.0)
        coordinates = [
            60.0, 99.9, 100.0, 100.1, 150.0, 199.9, 200.0, 200.1,
            250.0, 299.9, 300.0, 300.1, 350.0, 400.0, 400.1, 450.0,
        ]
        disagreements = []
        checked = 0
        for x0 in coordinates:
            for x1 in coordinates:
                for y0 in coordinates:
                    for y1 in coordinates:
                        span = (x0, y0, x1, y1)
                        checked += 1
                        if (gate.crop_contains_span(crop, span)
                                != regenerate.span_is_fully_shown(crop, span)):
                            disagreements.append(span)
        self.assertGreater(checked, 60000, "the grid must actually be dense")
        self.assertEqual(
            disagreements[:8], [],
            f"{len(disagreements)} span(s) where the two implementations disagree; one of "
            "them is wrong and the adjudication route cannot tell you which")

    def test_the_grid_contains_both_answers(self) -> None:
        """🔴 A differential test over inputs that are all contained — or all not — would agree
        perfectly while checking nothing. A green baseline is not a capture either."""
        crop = (100.0, 200.0, 300.0, 400.0)
        self.assertTrue(regenerate.span_is_fully_shown(crop, (150.0, 250.0, 250.0, 350.0)))
        self.assertTrue(regenerate.span_is_fully_shown(crop, crop))
        self.assertFalse(regenerate.span_is_fully_shown(crop, (150.0, 250.0, 350.0, 350.0)))
        self.assertFalse(regenerate.span_is_fully_shown(crop, (50.0, 250.0, 250.0, 350.0)))
        self.assertFalse(regenerate.span_is_fully_shown(crop, (150.0, 150.0, 250.0, 350.0)))
        self.assertFalse(regenerate.span_is_fully_shown(crop, (150.0, 250.0, 250.0, 450.0)))

    def test_this_module_no_longer_imports_the_predicate_it_corroborates(self) -> None:
        """The echo is closed by absence, so absence is what is pinned.

        Pinned on the module NAMESPACE rather than on the source text: the first version
        grepped for the name and failed on the docstring that explains why the name is gone.
        A check that cannot tell an import from a sentence about an import is not checking
        the import.
        """
        self.assertFalse(
            hasattr(regenerate, "crop_contains_span"),
            "the geometric predicate is bound in this module again, so its verdict is once "
            "more produced by the code it exists to corroborate")


class TheCliIsDriven(unittest.TestCase):
    """``main`` -> ``run`` as a subprocess, over this checkout's real recipes.

    ``test_regenerate_adjudications_fails_closed.py`` drives a *copy* of the script in a
    sandbox, which the meta-test cannot attribute to this file. These cases drive the script
    itself. ``verify`` reads recipes and PDFs and writes nothing; every case below asserts the
    recipe tree is byte-identical afterwards. The PDFs live under gitignored ``files/``, so the
    two cases that need a PDF present, or absent, each declare a skip when the host has no
    recipe in that state — never a silent pass.
    """

    def setUp(self) -> None:
        try:
            import fitz  # noqa: F401
        except ImportError:
            self.skipTest("skipped: PyMuPDF (fitz) not installed on this host")
        self.recipes = real_recipes()
        if not self.recipes:
            self.skipTest(f"skipped: no adjudication recipe under {ADJUDICATIONS}")
        self.before = {r: r.read_bytes() for _, r, _ in self.recipes}
        self.listing = sorted(p.relative_to(ROOT).as_posix() for p in ADJUDICATIONS.rglob("*"))

    def assert_nothing_written(self) -> None:
        self.assertEqual({r: r.read_bytes() for _, r, _ in self.recipes}, self.before,
                         "verify wrote a recipe")
        self.assertEqual(sorted(p.relative_to(ROOT).as_posix()
                                for p in ADJUDICATIONS.rglob("*")), self.listing,
                         "verify added or removed a file under page_adjudications/")

    def test_a_pmid_that_selects_no_study_fails_closed_through_main(self) -> None:
        result = run_cli("verify", "--pmid", "00000000")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("selected no study", result.stderr)
        self.assertIn(f"{len(self.recipes)} recipe(s) exist", result.stderr)
        self.assertNotIn("OK:", result.stdout)
        self.assert_nothing_written()

    def test_a_recipe_whose_pdf_is_present_verifies_by_digest(self) -> None:
        present = [(pmid, recipe) for pmid, recipe, here in self.recipes if here]
        if not present:
            self.skipTest("skipped: no recipe's source PDF is on this host "
                          f"(files/ is gitignored; {len(self.recipes)} recipes looked at)")
        pmid, recipe = present[0]
        declared = len(json.loads(recipe.read_text(encoding="utf-8"))["artifacts"])
        result = run_cli("verify", "--pmid", pmid)
        self.assertEqual(result.returncode, 0, result.stderr[-3000:])
        match = re.search(r"OK: (\d+) of (\d+) declared digest\(s\) matched across (\d+) "
                          r"rendered artifact\(s\) in 1 study\(ies\)", result.stdout)
        self.assertIsNotNone(match, result.stdout[-2000:])
        matched, declared_seen, rendered = (int(g) for g in match.groups())
        self.assertEqual((matched, declared_seen, rendered), (declared, declared, declared))
        self.assertIn("SCOPE: this verifies RECIPES", result.stdout)
        self.assertIn("OBSERVED, NOT VERIFIED", result.stdout)
        self.assert_nothing_written()

    def test_a_recipe_whose_pdf_is_absent_names_the_absence_and_the_way_round(self) -> None:
        absent = [(pmid, recipe) for pmid, recipe, here in self.recipes if not here]
        if not absent:
            self.skipTest("skipped: every recipe's source PDF is on this host")
        pmid, _recipe = absent[0]
        result = run_cli("verify", "--pmid", pmid)
        self.assertEqual(result.returncode, 1)
        self.assertIn("source PDF absent", result.stderr)
        self.assertIn("--artifact-workspace", result.stderr)
        self.assertIn("0 artifact(s) rendered", result.stderr)
        self.assert_nothing_written()


if __name__ == "__main__":
    unittest.main(verbosity=2)
