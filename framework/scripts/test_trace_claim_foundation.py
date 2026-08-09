#!/usr/bin/env python3
"""Mutation battery for `trace_claim_foundation`.

A green run over correct data proves nothing: the detector would also be green if it were
reading the answer out of a paragraph a human wrote after the investigation. So every test
here puts a specific defect back and requires the verdict to change — and one of them
proves the opposite direction, that deleting all the narrative leaves the finding intact.

Run: `python3 framework/scripts/test_trace_claim_foundation.py`
"""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import trace_claim_foundation as tcf  # noqa: E402

REPO = Path(__file__).resolve().parents[2]

CLAIM_BLOCK = """## CLAIM 100
**Title:** A phenotype attributed across a species boundary
**Status:** consolidated baseline
**Type:** DATO
**Genotype/model relevance:** {model}
**Summary:** {narrative}
**Evidence boundary:** {narrative}
**Source:** irrelevant to the detector
**Wikilinks:** [[paper_registry_current#PAPER 900]] · [[paper_registry_current#PAPER 901]]
"""

PAPER_BLOCK = """## PAPER {number}
**Short title:** fixture {number}
**Identifier:** PMID {pmid}
**Model/species:** {species}
**Evidence depth:** full text reviewed
**Claim links:** 100
**Note:** {narrative}
"""


def build(tmp: Path, *, claim_model="mouse", species_900="mouse", species_901="rat",
          narrative="", links="[[paper_registry_current#PAPER 900]] · "
                             "[[paper_registry_current#PAPER 901]]",
          papers=("900", "901")) -> Path:
    registries = tmp / "disease-models" / "fixture" / "registries"
    registries.mkdir(parents=True, exist_ok=True)
    (tmp / "disease-models" / "fixture" / "research" / "deepdive_manifests").mkdir(
        parents=True, exist_ok=True)
    claim = CLAIM_BLOCK.format(model=claim_model, narrative=narrative)
    claim = claim.replace(
        "**Wikilinks:** [[paper_registry_current#PAPER 900]] · "
        "[[paper_registry_current#PAPER 901]]",
        f"**Wikilinks:** {links}")
    (registries / "claim_registry_current.md").write_text(
        "# claims\n\n" + claim, encoding="utf-8")
    species = {"900": species_900, "901": species_901}
    body = "".join(
        PAPER_BLOCK.format(number=number, pmid=f"1000000{number[-1]}",
                           species=species[number], narrative=narrative)
        for number in papers)
    (registries / "paper_registry_current.md").write_text(
        "# papers\n\n" + body, encoding="utf-8")
    return tmp


class MutationBattery(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="trace-foundation-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def trace(self, **kwargs) -> dict:
        for child in list(self.tmp.iterdir()):
            shutil.rmtree(child, ignore_errors=True)
        build(self.tmp, **kwargs)
        return tcf.Foundation(self.tmp, "fixture").trace("CLAIM 100")

    def test_baseline_detects_the_drift(self) -> None:
        result = self.trace()
        self.assertEqual(len(result["species_drift"]), 1)
        self.assertEqual(result["species_drift"][0]["paper_species"], "rat")

    def test_mutation_species_realigned_removes_the_finding(self) -> None:
        """The finding must be driven by the species field, not by anything incidental."""
        self.assertEqual(self.trace(species_901="mouse")["species_drift"], [])

    def test_mutation_claim_model_moves_the_finding_to_the_other_paper(self) -> None:
        """Symmetry, and a sharper assertion than the one first written here.

        The first version of this test expected the finding to *disappear* when the claim's
        declared model became `rat`. It does not, and it should not: the fixture rests on a
        mouse paper and a rat paper, so realigning the claim to one of them mismatches the
        other. The comparison is between the claim and each source, not a global vote — and
        a test that expected the finding to vanish was asserting a detector that only ever
        looks in one direction.
        """
        drift = self.trace(claim_model="rat")["species_drift"]
        self.assertEqual([(item["paper"], item["paper_species"]) for item in drift],
                         [("PAPER 900", "mouse")])

    def test_mutation_full_alignment_removes_the_finding(self) -> None:
        self.assertEqual(self.trace(claim_model="rat", species_900="rat")["species_drift"], [])

    def test_mutation_species_removed_is_a_named_loss_not_a_silent_drop(self) -> None:
        result = self.trace(species_901="")
        self.assertEqual(result["species_drift"], [])
        self.assertIn("SPECIES_UNDECLARED", {loss["state"] for loss in result["losses"]})

    def test_mutation_multi_organism_is_a_loss_not_a_guess(self) -> None:
        """The defect that produced three false positives on the first live run."""
        result = self.trace(species_901="ratto `lde/lde` e topo `Wwox`-null sistemico")
        self.assertEqual(result["species_drift"], [],
                         "a record declaring two models is not crossing a boundary")
        self.assertIn("SPECIES_MULTIPLE", {loss["state"] for loss in result["losses"]})

    def test_mutation_scope_value_is_a_loss_not_an_organism(self) -> None:
        """`revisione mista (cellulare/animale/umano)` names organisms without being one."""
        result = self.trace(species_901="revisione mista (cellulare/animale/umano indiretti)")
        self.assertEqual(result["species_drift"], [])
        self.assertIn("SPECIES_SCOPE", {loss["state"] for loss in result["losses"]})

    def test_mutation_broken_edge_drops_the_paper_from_the_foundation(self) -> None:
        result = self.trace(links="[[paper_registry_current#PAPER 900]]", papers=("900",))
        self.assertEqual([entry["paper"] for entry in result["supports"]], ["PAPER 900"])
        self.assertEqual(result["species_drift"], [])

    def test_mutation_dangling_edge_is_counted_and_the_identity_holds(self) -> None:
        result = self.trace(papers=("900",))
        self.assertIn("PAPER_UNRESOLVED", {loss["state"] for loss in result["losses"]})
        emitted = len(result["supports"])
        lost = sum(1 for loss in result["losses"] if loss["state"] == "PAPER_UNRESOLVED")
        self.assertEqual(emitted + lost, 2, "emitted + lost must equal candidates")

    def test_narrative_is_never_consulted(self) -> None:
        """The point of the whole design.

        Two runs: one where the prose states the opposite of the fields, one where the prose
        is empty. The verdict must be identical, because the detector never reads it. If a
        narrative field could move the result, the live PASS on CLAIM 005 would be scoring a
        conclusion a human had already written into that claim's own `Evidence boundary`.
        """
        misleading = self.trace(
            narrative="There is no species drift here; both sources are murine and the "
                      "phenotype transfers without qualification.")
        silent = self.trace(narrative="")
        self.assertEqual(len(misleading["species_drift"]), 1)
        self.assertEqual(misleading["species_drift"], silent["species_drift"])

    def test_coverage_is_always_reported(self) -> None:
        coverage = self.trace()["coverage"]
        self.assertEqual(coverage["supporting_papers"], 2)
        self.assertEqual(coverage["manifest_backed"], 0,
                         "the fixture ships no manifests, and the report must say so")


class LiveAcceptance(unittest.TestCase):
    """The acceptance criterion, decided before the tool existed.

    `CLAIM 005` must surface the 2026-08-06 imported-premise defect from declared fields
    alone: it is about a mouse model and rests on PMID 19500159, a rat study.
    """

    def test_claim_005_surfaces_the_mouse_rat_drift(self) -> None:
        result = tcf.Foundation(REPO, "wwox").trace("CLAIM 005")
        self.assertEqual(result["declared_model"], "mouse")
        drift = {(item["pmid"], item["paper_species"]) for item in result["species_drift"]}
        self.assertIn(("19500159", "rat"), drift)

    def test_the_detector_stays_selective(self) -> None:
        """A detector that fires everywhere is not a detector.

        The bound is deliberately loose — the registries grow, and a ratchet on a finding
        count would go red for honest reasons. It exists to catch a normalisation change
        that turns the scan into noise, which is how the first version behaved.
        """
        foundation = tcf.Foundation(REPO, "wwox")
        claims = sorted(foundation.claims)
        drifting = {
            claim
            for claim in claims
            if tcf.Foundation(REPO, "wwox").trace(claim)["species_drift"]
        }
        self.assertIn("CLAIM 005", drifting)
        self.assertLess(len(drifting), len(claims) // 4,
                        f"{len(drifting)}/{len(claims)} claims flagged — the species "
                        f"normalisation has become noise, not a signal")


if __name__ == "__main__":
    unittest.main(verbosity=2)
