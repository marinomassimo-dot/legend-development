#!/usr/bin/env python3
"""Regressions for the deep-dive work manifest gate.

The `verbatim_locators` section exists because of a measured failure: on 2026-08-04 an
export to an external knowledge base found that no verbatim locator existed anywhere in
the canonical state, across every complete read in the ledger. A receipt attests that a
document was read; it does not attest which sentence supports which statement. These tests
keep the distinction enforceable.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("deepdive_manifest", HERE / "deepdive_manifest.py")
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)

ROOT = HERE.parents[1]
MANIFESTS = ROOT / "disease-models/wwox/research/deepdive_manifests"


def minimal(**overrides) -> dict:
    manifest = {
        "pmid": "12345678",
        "receipt": "FTR-20260804-12345678-01",
        "landing": ["claim_registry_current.md#CLAIM 999"],
        "skills_considered": [{"skill": "legend-deepdive", "used": True}],
        "group_assessment": {"total_publications": 10, "publications_on_gene": 2,
                             "weighting": "descriptive series; observation weighted above interpretation",
                             "research_type": "descriptive_clinical",
                             "is_primary_group_for_disease": False},
        "field_density": {"queries": [{"query": "WWOX AND GSK3", "count": 5}]},
        "multihop": {"gene_direct_refs_in_source": [], "references_enumerated": 28},
        "corpus_crossquery": {"query": "GSK3 in the existing corpus", "hits": 3},
        "retraction_check": {"result": "no retraction notice found"},
        "verbatim_locators": {"source_fulltext_indexed": True, "entries": [
            {"proposition": "WWOX 388-407 is required for the interaction with GSK3beta",
             "snippet": "This indicates that WWOX amino acids 388-407 are required for its interaction with GSK3b.",
             "anchor": "Results, Fig. 3c"}]},
    }
    manifest.update(overrides)
    return manifest


class SectionIsRequired(unittest.TestCase):
    def test_missing_section_is_an_error(self) -> None:
        manifest = minimal()
        del manifest["verbatim_locators"]
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("verbatim_locators" in e for e in errors))

    def test_wellformed_manifest_passes(self) -> None:
        errors, incomplete = gate.validate(minimal())
        self.assertEqual(errors, [])
        self.assertEqual(incomplete, [])


class EntriesMustBeUsable(unittest.TestCase):
    def test_empty_entries_are_rejected(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={"entries": []}))
        self.assertTrue(any("at least one verbatim quote" in e for e in errors))

    def test_quote_without_a_proposition_is_rejected(self) -> None:
        """A quote that names nothing it supports is decoration."""
        errors, _ = gate.validate(minimal(verbatim_locators={"entries": [
            {"snippet": "a" * 60, "anchor": "Results, Fig. 1"}]}))
        self.assertTrue(any("proposition" in e for e in errors))

    def test_quote_without_an_anchor_is_rejected(self) -> None:
        """A quote nobody can find again is not verifiable."""
        errors, _ = gate.validate(minimal(verbatim_locators={"entries": [
            {"proposition": "P", "snippet": "a" * 60}]}))
        self.assertTrue(any("anchor" in e for e in errors))

    def test_gesture_at_a_quote_is_rejected(self) -> None:
        """Below the threshold it is a fragment, not a locator."""
        errors, _ = gate.validate(minimal(verbatim_locators={"entries": [
            {"proposition": "P", "snippet": "it binds", "anchor": "Results"}]}))
        self.assertTrue(any("verbatim" in e for e in errors))


class WaiverIsAnArgument(unittest.TestCase):
    def test_short_waiver_is_rejected(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={"waived": "n/a"}))
        self.assertTrue(any("verbatim_locators" in e for e in errors))

    def test_declining_to_waive_does_not_read_as_a_waiver(self) -> None:
        """`waived: false` is the idiomatic JSON for "I am not waiving this".

        Found by writing a real manifest (PMID 39507621) rather than by reading the code: the
        gate answered "a waiver must state why", which argues the author into waiving a section
        they meant to fill — and it returned early, so the entries were never validated. A
        guard whose error message points at the omission is worse than no guard.
        """
        errors, incomplete = gate.validate(minimal(verbatim_locators={
            "waived": False, "source_fulltext_indexed": True,
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertEqual(errors, [])
        self.assertEqual(incomplete, [])

    def test_declining_to_waive_still_validates_the_entries(self) -> None:
        """The early return was the real damage: bad entries passed unexamined."""
        errors, _ = gate.validate(minimal(verbatim_locators={
            "waived": False, "entries": []}))
        self.assertTrue(any("at least one verbatim quote" in e for e in errors))

    def test_argued_waiver_is_accepted_but_declared_incomplete(self) -> None:
        """Waiving is allowed; waiving silently is not."""
        errors, incomplete = gate.validate(minimal(verbatim_locators={
            "waived": "the reading supports no proposition in the working model; it was read "
                      "for method transfer only and lands in the discovery ledger"}))
        self.assertEqual(errors, [])
        self.assertIn("verbatim_locators: waived", incomplete)


class CommittedManifestsHold(unittest.TestCase):
    def test_every_committed_manifest_validates(self) -> None:
        found = sorted(MANIFESTS.glob("PMID*.json"))
        self.assertTrue(found, "no deep-dive manifests found")
        for path in found:
            with self.subTest(manifest=path.name):
                errors, _ = gate.validate(json.loads(path.read_text(encoding="utf-8")))
                self.assertEqual(errors, [], f"{path.name}: {errors}")

    def test_locators_carry_a_findable_anchor(self) -> None:
        for path in sorted(MANIFESTS.glob("PMID*.json")):
            section = json.loads(path.read_text(encoding="utf-8"))["verbatim_locators"]
            for entry in section.get("entries", []):
                with self.subTest(manifest=path.name, anchor=entry.get("anchor")):
                    self.assertTrue(str(entry["anchor"]).strip())
                    self.assertGreaterEqual(len(entry["snippet"]), gate.MIN_SNIPPET_CHARS)


class ExternallyVerifiableQuotes(unittest.TestCase):
    """A quote nobody outside LEGEND can check is not usable as external evidence.

    DisMech verifies each snippet by exact substring match against a cached copy of the source.
    Measured 2026-08-05: 2 of 8 read papers are abstract-only in Europe PMC, and 0 of 17
    exportable snippets occur in an abstract — every locator LEGEND produces is a full-text
    locator, by design. For an indexed source that is fine; for an abstract-only one the quote
    cannot be verified at all, and finding that out after the reading means reading again.
    """

    def test_stitched_quote_is_rejected(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={"entries": [
            {"proposition": "P",
             "snippet": "the first half of the sentence […] and the second half of it",
             "anchor": "Results"}]}))
        self.assertTrue(any("stitched quote" in e for e in errors))

    def test_contiguous_quote_is_accepted(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={
            "source_fulltext_indexed": True,
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertEqual(errors, [])

    def test_abstract_only_source_needs_abstract_anchors_or_an_argument(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={
            "source_fulltext_indexed": False,
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertTrue(any("not full-text indexed" in e for e in errors))

    def test_an_abstract_anchor_satisfies_it(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={
            "source_fulltext_indexed": False,
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results",
                         "abstract_snippet": "the abstract says this"}]}))
        self.assertEqual(errors, [])

    def test_an_argued_waiver_also_satisfies_it(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={
            "source_fulltext_indexed": False,
            "abstract_anchoring_waived": "the abstract reports only the headline association "
                                         "and states none of these propositions",
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertEqual(errors, [])

    def test_undeclared_index_state_is_a_visible_gap(self) -> None:
        """Not a block — the lookup needs the network — but never silence."""
        _errors, incomplete = gate.validate(minimal(verbatim_locators={
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertTrue(any("source_fulltext_indexed" in item for item in incomplete))


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
