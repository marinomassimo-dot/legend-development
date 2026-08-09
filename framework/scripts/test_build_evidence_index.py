#!/usr/bin/env python3
"""Mutation battery for the derived evidence index.

The index makes one promise that matters: it never reports unverifiable evidence as
verified, and it never lets a query look complete when it has searched a third of the
literature. Each test below removes one of those guarantees and requires the output to
change.

Run: `python3 framework/scripts/test_build_evidence_index.py`
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_evidence_index as bei  # noqa: E402
import trace_claim_foundation as tcf  # noqa: E402

REPO = Path(__file__).resolve().parents[2]

CLAIMS = """# claims

## CLAIM 100
**Status:** consolidated baseline
**Type:** DATO
**Genotype/model relevance:** mouse
**Source:** PMID 10000001
**Wikilinks:** [[paper_registry_current#PAPER 900]]
"""

PAPERS = """# papers

## PAPER 900
**Identifier:** PMID 10000001
**Model/species:** mouse
**Claim links:** 100
"""


def manifest(entries: list[dict], **extra) -> dict:
    return {"schema_version": 2, "pmid": "10000001", "receipt": "FTR-fixture-01",
            "verbatim_locators": {"entries": entries}, **extra}


def build(tmp: Path, entries: list[dict], pmid: str = "10000001") -> Path:
    disease = tmp / "disease-models" / "fixture"
    (disease / "registries").mkdir(parents=True, exist_ok=True)
    manifests = disease / "research" / "deepdive_manifests"
    manifests.mkdir(parents=True, exist_ok=True)
    (disease / "registries" / "claim_registry_current.md").write_text(CLAIMS, encoding="utf-8")
    (disease / "registries" / "paper_registry_current.md").write_text(PAPERS, encoding="utf-8")
    (manifests / f"PMID{pmid}.json").write_text(
        json.dumps(manifest(entries)), encoding="utf-8")
    return tmp


VERIFIABLE_ENTRY = {
    "proposition": "The mutant protein is undetectable in hippocampus.",
    "snippet": "no 47 kDa species was detected in hippocampus",
    "anchor": "Results, Figure 3B",
    "surface": "body",
    "artifact": "files/fulltext/fixture.html",
}
LEGACY_ENTRY = {
    "proposition": "An older reading, captured before schema v2.",
    "snippet": "the phenotype was fully penetrant",
    "anchor": "Results, second paragraph",
}


class IndexBattery(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="evidence-index-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def index(self, entries: list[dict]) -> bei.EvidenceIndex:
        for child in list(self.tmp.iterdir()):
            shutil.rmtree(child, ignore_errors=True)
        build(self.tmp, entries)
        return bei.EvidenceIndex(self.tmp, "fixture")

    def test_a_verifiable_locator_is_tiered_as_verifiable(self) -> None:
        index = self.index([VERIFIABLE_ENTRY])
        self.assertEqual([r["tier"] for r in index.records], [bei.VERIFIABLE])
        self.assertEqual(index.records[0]["claims"], ["CLAIM 100"])

    def test_mutation_removing_the_artifact_demotes_the_tier(self) -> None:
        """The whole promise: no quote is called verified without something to check it."""
        entry = {key: value for key, value in VERIFIABLE_ENTRY.items() if key != "artifact"}
        index = self.index([entry])
        self.assertEqual([r["tier"] for r in index.records], [bei.LEGACY_UNANCHORED])
        self.assertEqual(index.coverage()["verifiable_share"], 0.0)

    def test_mutation_removing_the_surface_demotes_the_tier(self) -> None:
        entry = {key: value for key, value in VERIFIABLE_ENTRY.items() if key != "surface"}
        self.assertEqual([r["tier"] for r in self.index([entry]).records],
                         [bei.LEGACY_UNANCHORED])

    def test_an_abstract_surface_is_not_verifiable_evidence(self) -> None:
        """An abstract is not a reading, and the tier has to say so on its own."""
        entry = {**VERIFIABLE_ENTRY, "surface": "abstract"}
        self.assertEqual([r["tier"] for r in self.index([entry]).records],
                         [bei.ABSTRACT_ONLY])

    def test_a_locator_without_a_quote_is_lost_not_emitted(self) -> None:
        entry = {**VERIFIABLE_ENTRY, "snippet": "   "}
        index = self.index([entry])
        self.assertEqual(index.records, [])
        self.assertIn("LOCATOR_INCOMPLETE", {loss["state"] for loss in index.losses})
        self.assertEqual(len(index.records) + 1, index.candidates,
                         "emitted + lost must equal candidates")

    def test_mixed_tiers_are_reported_separately_never_summed(self) -> None:
        index = self.index([VERIFIABLE_ENTRY, LEGACY_ENTRY])
        coverage = index.coverage()
        self.assertEqual(coverage["by_tier"],
                         {bei.VERIFIABLE: 1, bei.LEGACY_UNANCHORED: 1})
        self.assertEqual(coverage["verifiable_share"], 0.5)

    def test_evidence_ids_are_content_derived_and_order_independent(self) -> None:
        forward = [r["evidence_id"] for r in self.index([VERIFIABLE_ENTRY, LEGACY_ENTRY]).records]
        backward = [r["evidence_id"] for r in self.index([LEGACY_ENTRY, VERIFIABLE_ENTRY]).records]
        self.assertEqual(set(forward), set(backward))
        self.assertNotEqual(forward[0], forward[1])

    def test_a_wikilink_only_paper_binds_no_evidence_to_the_claim(self) -> None:
        build(self.tmp, [VERIFIABLE_ENTRY])
        papers = self.tmp / "disease-models" / "fixture" / "registries" / "paper_registry_current.md"
        papers.write_text(papers.read_text(encoding="utf-8").replace(
            "**Claim links:** 100", "**Claim links:** none"), encoding="utf-8")
        claims = self.tmp / "disease-models" / "fixture" / "registries" / "claim_registry_current.md"
        claims.write_text(claims.read_text(encoding="utf-8").replace(
            "**Source:** PMID 10000001", "**Source:** a different paper entirely"),
            encoding="utf-8")
        index = bei.EvidenceIndex(self.tmp, "fixture")
        self.assertEqual(index.records[0]["claims"], [],
                         "a cross-reference must not bind evidence to a claim")


class LiveIndex(unittest.TestCase):
    def setUp(self) -> None:
        self.index = bei.EvidenceIndex(REPO, "wwox")

    def test_the_index_declares_its_own_incompleteness(self) -> None:
        coverage = self.index.coverage()
        self.assertGreater(coverage["evidence_records"], 0)
        self.assertLess(coverage["papers_with_evidence_records"],
                        coverage["papers_in_registry"],
                        "the denominator is the registry, and it must stay visible")
        self.assertLess(coverage["verifiable_share"], 1.0,
                        "legacy locators exist; reporting 100% would be the failure")

    def test_the_accounting_identity_holds_on_live_data(self) -> None:
        lost = sum(1 for loss in self.index.losses if loss["state"] == "LOCATOR_INCOMPLETE")
        self.assertEqual(len(self.index.records) + lost, self.index.candidates)

    def test_manifested_readings_without_a_paper_record_are_named(self) -> None:
        """Three readings carry a work manifest but no integrated PAPER record.

        They are corpus placeholders, not papers. The index must say so rather than bind
        their evidence to nothing and move on — that is a state finding for the operator,
        not a detail for the tool to absorb.
        """
        orphans = {loss["subject"] for loss in self.index.losses
                   if loss["state"] == "MANIFEST_WITHOUT_PAPER"}
        self.assertTrue(orphans, "the loss state exists to be used when it applies")
        for record in self.index.records:
            if record["paper"] is None:
                self.assertEqual(record["claims"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
