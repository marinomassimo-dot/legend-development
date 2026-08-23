#!/usr/bin/env python3
"""Regressions for DISCOVERY.

Every test below pins a defect this repository produced on 2026-08-23, on real seats, with
real numbers. They are written so that the *defect* fails the test, not so that today's
output is frozen: a count that will legitimately change as branches are created is never
asserted as a literal.
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SPEC = importlib.util.spec_from_file_location("artifact_index", HERE / "artifact_index.py")
ai = importlib.util.module_from_spec(SPEC)
# Registered before exec: on Python 3.9 `@dataclass` resolves annotations through
# `sys.modules[cls.__module__]`, which is None for a module loaded out of band.
sys.modules["artifact_index"] = ai
SPEC.loader.exec_module(ai)

CONVENTION = (ROOT / ai.CONVENTION).read_text(encoding="utf-8")
CLASSES = ai.parse_classes(CONVENTION)
ROOTS = ai.parse_control_plane_roots((ROOT / ai.DOMAIN_SOURCE).read_text(encoding="utf-8"))


class TheClassListIsParsedNeverRestated(unittest.TestCase):
    """Five modules once held five private copies of one definition; the shortest was wrong."""

    def test_the_convention_is_the_source(self) -> None:
        names = {c.name for c in CLASSES}
        self.assertIn("CAND", names)
        self.assertIn("REVIEW", names)
        self.assertGreaterEqual(len(CLASSES), 4)

    def test_a_changed_convention_changes_the_parse(self) -> None:
        """If this passed against a hardcoded list, the parse would be decorative."""
        mutated = CONVENTION.replace("| 1 | **DEC** |", "| 1 | **DECISION_RENAMED** |", 1)
        self.assertNotEqual(mutated, CONVENTION, "fixture no longer matches the table")
        names = {c.name for c in ai.parse_classes(mutated)}
        self.assertIn("DECISION_RENAMED", names)
        self.assertNotIn("DEC", names)

    def test_an_unparseable_convention_fails_loudly(self) -> None:
        with self.assertRaises(ai.ConventionParseError):
            ai.parse_classes("no table here")

    def test_the_module_does_not_restate_the_class_names(self) -> None:
        """The sixth private copy, caught before it exists."""
        source = (HERE / "artifact_index.py").read_text(encoding="utf-8")
        body = source.split('"""', 2)[-1]          # exclude the module docstring
        for literal in ('"CAND"', "'CAND'", '"REVIEW"', "'REVIEW'", '"PROPOSAL"'):
            self.assertNotIn(
                literal, body,
                f"{literal} is restated in the module; parse it from the convention instead",
            )


class BothEmissionFormsAreRead(unittest.TestCase):
    """A colon-only parser reported 6 of 14 reviews and 3 of 9 manifests as ABSENT."""

    def test_colon_form(self) -> None:
        self.assertEqual(ai.read_field("MIRROR_REVIEW: PASS\n", "MIRROR_REVIEW"),
                         ("PASS", "colon"))

    def test_aligned_form_with_no_colon(self) -> None:
        self.assertEqual(ai.read_field("MIRROR_REVIEW           REQUEST CHANGES\n",
                                       "MIRROR_REVIEW"),
                         ("REQUEST CHANGES", "aligned"))

    def test_a_single_space_is_not_a_declaration(self) -> None:
        """Prose such as `MIRROR_REVIEW not-PASS` inside a sentence must not count."""
        value, form = ai.read_field("the corrected MIRROR_REVIEW not-PASS was noted\n",
                                    "MIRROR_REVIEW")
        self.assertIsNone(value)
        self.assertIsNone(form)

    def test_the_real_corpus_carries_both_forms(self) -> None:
        """Guards the finding itself: if either form vanishes, the rule needs re-deriving."""
        forms = set()
        listing = subprocess.run(
            ("git", "ls-tree", "-r", "--name-only", "HEAD", "governance/candidates/"),
            cwd=str(ROOT), capture_output=True, text=True, check=False,
        ).stdout.split()
        for path in [p for p in listing if "/CAND-" in p]:
            text = subprocess.run(("git", "show", f"HEAD:{path}"), cwd=str(ROOT),
                                  capture_output=True, text=True, check=False).stdout
            _, form = ai.read_field(text, "MIRROR_REVIEW")
            if form:
                forms.add(form)
        self.assertEqual(forms, {"colon", "aligned"},
                         "the corpus no longer exercises both forms; re-derive the rule")


class DomainComesFromThePrefixMatch(unittest.TestCase):
    """P5.1 settles domain by literal prefix. What an artifact says about itself does not."""

    def test_roots_are_parsed_not_assumed(self) -> None:
        self.assertIn("reviews/", ROOTS)
        self.assertIn("governance/candidates/", ROOTS)

    def test_control_plane_and_content(self) -> None:
        self.assertEqual(ai.domain_of("reviews/mirror/REV-X-001.md", ROOTS), "CONTROL_PLANE")
        self.assertEqual(ai.domain_of("learning/plan/SLR-plan-0001.md", ROOTS), "CONTENT")
        self.assertEqual(ai.domain_of("framework/protocols/x.md", ROOTS), "CONTENT")

    def test_a_false_transcription_loses_to_the_prefix(self) -> None:
        text = "---\ndomain: CONTENT — declared by the author\n---\n"
        rec = ai.build_record("reviews/mirror/REV-X-001.md", text, CLASSES, ROOTS)
        self.assertEqual(rec.domain_by_path, "CONTROL_PLANE")
        self.assertEqual(rec.domain_agreement, "CONFLICT")
        self.assertTrue(any(f.startswith("DOMAIN_CONFLICT") for f in rec.findings))


class PlacementIsJudgedOnlyInsideAGovernedDirectory(unittest.TestCase):
    """B.1.2 gives classes 6 and 7 an author root; flagging those buries the real six."""

    def test_a_handoff_in_a_class_directory_is_a_finding(self) -> None:
        rec = ai.build_record("governance/candidates/HANDOFF-X.md", "", CLASSES, ROOTS)
        self.assertEqual(rec.class_agreement, "CONFLICT")

    def test_a_handoff_in_an_author_root_is_not(self) -> None:
        rec = ai.build_record("learning/plan/HANDOFF-X.md", "", CLASSES, ROOTS)
        self.assertEqual(rec.class_agreement, "author_root")
        self.assertFalse(any("CLASS_DIRECTORY" in f for f in rec.findings))

    def test_governance_is_derived_from_the_table(self) -> None:
        by_name = {c.name: c for c in CLASSES}
        self.assertTrue(ai.is_path_governed(by_name["CAND"]))
        self.assertFalse(ai.is_path_governed(by_name["HANDOFF"]))


class ThePopulationIsEnumeratedBeforeAnyPattern(unittest.TestCase):
    """`0 of 39`, `8` and `14` were each what a pattern found, not a set then measured."""

    def test_a_population_declares_command_instant_and_figure_class(self) -> None:
        population = ai.enumerate_working_tree()
        self.assertTrue(population.command)
        self.assertRegex(population.instant, r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
        self.assertTrue(population.figure_class)
        self.assertGreater(len(population.paths), 0)

    def test_working_tree_and_refs_are_different_populations(self) -> None:
        """git archive cannot see an untracked file; the report must never conflate them."""
        self.assertNotEqual(ai.enumerate_working_tree().figure_class,
                            ai.enumerate_refs().figure_class)

    def test_untracked_paths_are_marked(self) -> None:
        population = ai.enumerate_working_tree()
        self.assertTrue(set(population.untracked) <= set(population.paths))


class TimestampsComeFromTheRawEpoch(unittest.TestCase):
    """`stat -f '%Sm'` renders local time under any format string; a hardcoded Z is a forgery."""

    def test_instant_is_utc_shaped(self) -> None:
        self.assertRegex(ai.utc_now(), r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

    def test_no_stat_rendering_in_the_module(self) -> None:
        source = (HERE / "artifact_index.py").read_text(encoding="utf-8")
        self.assertNotIn("%Sm", source.split('"""', 2)[-1])


class ItReportsAndGatesNothing(unittest.TestCase):
    """Discovery reports; it does not judge. Exit 0 either way, and it writes nothing."""

    def test_exit_zero_with_findings_present(self) -> None:
        proc = subprocess.run((sys.executable, str(HERE / "artifact_index.py")),
                              cwd=str(ROOT), capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 0)
        self.assertIn("FINDINGS", proc.stdout)
        self.assertIn("gating nothing", proc.stdout)

    def test_it_leaves_the_tree_unchanged(self) -> None:
        before = subprocess.run(("git", "status", "--porcelain"), cwd=str(ROOT),
                                capture_output=True, text=True, check=False).stdout
        subprocess.run((sys.executable, str(HERE / "artifact_index.py")), cwd=str(ROOT),
                       capture_output=True, text=True, check=False)
        after = subprocess.run(("git", "status", "--porcelain"), cwd=str(ROOT),
                               capture_output=True, text=True, check=False).stdout
        self.assertEqual(before, after, "discovery must not write into the tree it scans")


if __name__ == "__main__":
    unittest.main(verbosity=2)
