#!/usr/bin/env python3
"""A local abstract corpus must never become the thing a claim rests on.

Harvesting 706 abstracts into a local file is useful and dangerous in the same motion. The
danger is not that anyone decides to cut corners; it is that the corpus is *there*, greppable,
and answering from it feels like working. LEGEND's founding principle says the opposite: the
decisive detail is routinely absent from an abstract. On 2026-08-04 a figure panel in Cheng 2020
showed lithium suppressing seizures in all three genotypes, reversing what the running text
said — no abstract on earth carried that.

`CLAUDE.md` already forbids grep as a method of analysis, and the receipt vocabulary already
separates `abstract_only` from `complete_fulltext_read`. What was missing is the join: nothing
stopped the corpus being named as the source of evidence. This is that join.

Three prohibitions, each mechanical:

* no `FULLTEXT_READ_RECEIPT` may name the corpus as its `source_locator`;
* no deep-dive manifest may name it as an artefact or a locator anchor;
* the harvester must keep declaring the corpus non-evidential, so the artefact carries its own
  terms of use rather than relying on this file being read.

What this deliberately does NOT forbid: using the corpus for triage, census and export
pre-flight. Those are the reasons it exists.
"""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
MANIFESTS = ROOT / "disease-models/wwox/research/deepdive_manifests"
HARVESTER = ROOT / "framework/scripts/pubmed_corpus_harvest.py"

# How a corpus artefact is recognised wherever it is written.
CORPUS_MARKERS = re.compile(
    r"files/corpus/|corpus_seed_pubmed|_corpus\.jsonl|corpus_abstracts", re.IGNORECASE)


def _receipts() -> list[dict]:
    if not LEDGER.is_file():
        return []
    return [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines()
            if line.strip()]


class CorpusIsNotASource(unittest.TestCase):
    def test_no_receipt_reads_the_abstract_corpus(self) -> None:
        offenders = [r["event_id"] for r in _receipts()
                     if CORPUS_MARKERS.search(str(r.get("source_locator") or ""))]
        self.assertFalse(
            offenders,
            "these receipts name an abstract corpus as the document they read:\n  "
            + "\n  ".join(offenders)
            + "\nA corpus of abstracts is not a document. Read the paper.")

    def test_no_complete_read_is_backed_by_a_corpus_artefact(self) -> None:
        offenders = []
        for path in sorted(MANIFESTS.glob("PMID*.json")):
            text = path.read_text(encoding="utf-8")
            if CORPUS_MARKERS.search(text):
                offenders.append(path.name)
        self.assertFalse(
            offenders,
            "these deep-dive manifests reference an abstract corpus:\n  "
            + "\n  ".join(offenders)
            + "\nA locator must point into the paper, not into a bibliographic export.")

    def test_locator_anchors_never_point_at_a_corpus(self) -> None:
        for path in sorted(MANIFESTS.glob("PMID*.json")):
            section = json.loads(path.read_text(encoding="utf-8")).get(
                "verbatim_locators", {})
            for position, entry in enumerate(section.get("entries") or [], 1):
                with self.subTest(manifest=path.name, entry=position):
                    self.assertIsNone(CORPUS_MARKERS.search(str(entry.get("anchor", ""))),
                                      "an anchor must name a section, figure or table")


class ArtefactCarriesItsOwnTerms(unittest.TestCase):
    """The guard must not depend on anyone having read this test file."""

    def test_the_harvester_declares_the_corpus_non_evidential(self) -> None:
        source = HARVESTER.read_text(encoding="utf-8")
        self.assertIn('"evidential_status": "NOT_EVIDENCE"', source)
        self.assertIn('"forbidden_uses"', source)
        self.assertIn('"permitted_uses"', source)

    def test_the_permitted_uses_still_include_the_reasons_it_exists(self) -> None:
        source = HARVESTER.read_text(encoding="utf-8")
        for reason in ("triage", "census", "pre-flight"):
            with self.subTest(use=reason):
                self.assertIn(reason, source)

    def test_reading_is_named_as_forbidden(self) -> None:
        source = HARVESTER.read_text(encoding="utf-8")
        self.assertIn("An abstract is not the paper", source)


class InstructionSurfacesCarryTheDistinction(unittest.TestCase):
    """A capability the operating instructions do not mention is a capability nobody uses.

    The inverse also holds and is worse: a corpus the instructions do not *bound* is one an
    agent may quietly treat as a shortcut.
    """

    SURFACES = ("CLAUDE.md", "AGENTS.md")

    def test_the_bootstrap_bounds_the_corpus(self) -> None:
        for name in self.SURFACES:
            with self.subTest(file=name):
                text = (ROOT / name).read_text(encoding="utf-8")
                self.assertIn("pubmed_corpus_harvest", text,
                              f"{name} does not mention the corpus harvester at all")
                self.assertTrue(
                    re.search(r"non è (una )?lettura|is not a read|not evidence|non è evidenza",
                              text, re.IGNORECASE),
                    f"{name} mentions the corpus without bounding what it may be used for")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
