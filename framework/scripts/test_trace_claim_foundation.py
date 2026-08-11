#!/usr/bin/env python3
"""Mutation battery for `trace_claim_foundation`.

A green run over correct data proves nothing: the detector would also be green if it were
reading the answer out of a paragraph a human wrote after the investigation. So every test
here puts a specific defect back and requires the verdict to change — and one of them
proves the opposite direction, that deleting all the narrative leaves the finding intact.

Run: `python3 framework/scripts/test_trace_claim_foundation.py`
"""

from __future__ import annotations

import re
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
**Claim links:** {claim_links}
**Wikilinks:** {links}
**Note:** {narrative}
"""


def build(tmp: Path, *, claim_model="mouse", species=None, narrative="",
          links="[[paper_registry_current#PAPER 900]] · "
                "[[paper_registry_current#PAPER 901]]",
          papers=("900", "901"), paper_links=None, claim_links=None) -> Path:
    """Write a minimal two-registry fixture.

    `paper_links` seeds paper-to-paper bonds; `claim_links` overrides which claim a paper
    declares. The default gives every paper `100`, which is right for the single-hop tests
    and wrong for the lineage ones: a paper meant to sit one hop away must not also be a
    direct support, or the walk is measured against a distance it never travelled.
    """
    species = {"900": "mouse", "901": "rat", **(species or {})}
    paper_links = paper_links or {}
    claim_links = claim_links or {}
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
    body = "".join(
        PAPER_BLOCK.format(
            number=number, pmid=f"1000000{number[-1]}", species=species[number],
            narrative=narrative, claim_links=claim_links.get(number, "100"),
            links=" · ".join(f"[[paper_registry_current#PAPER {target}]]"
                             for target in paper_links.get(number, ())) or "none")
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
        self.assertEqual(self.trace(species={"901": "mouse"})["species_drift"], [])

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
        self.assertEqual(
            self.trace(claim_model="rat", species={"900": "rat"})["species_drift"], [])

    def test_mutation_species_removed_is_a_named_loss_not_a_silent_drop(self) -> None:
        result = self.trace(species={"901": ""})
        self.assertEqual(result["species_drift"], [])
        self.assertIn("SPECIES_UNDECLARED", {loss["state"] for loss in result["losses"]})

    def test_mutation_multi_organism_is_a_loss_not_a_guess(self) -> None:
        """The defect that produced three false positives on the first live run."""
        result = self.trace(species={"901": "ratto `lde/lde` e topo `Wwox`-null sistemico"})
        self.assertEqual(result["species_drift"], [],
                         "a record declaring two models is not crossing a boundary")
        self.assertIn("SPECIES_MULTIPLE", {loss["state"] for loss in result["losses"]})

    def test_mutation_scope_value_is_a_loss_not_an_organism(self) -> None:
        """`revisione mista (cellulare/animale/umano)` names organisms without being one."""
        result = self.trace(
            species={"901": "revisione mista (cellulare/animale/umano indiretti)"})
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

    def test_mutation_wikilink_only_edge_is_a_reference_not_evidence(self) -> None:
        """A cross-reference must not be able to raise a drift finding.

        Defect 27 of the DisMech export contract: a paper named in a claim's `Source` field
        normalises to `SUPPORTING`, one that only appears in its wikilinks normalises to
        `UNQUALIFIED_REFERENCE`. Live, this is the whole difference between `CLAIM 005`,
        whose rat source declares the bond from the paper side, and `CLAIM 031`, which cites
        a murine gene-therapy paper for convergence with a therapeutic inference.
        """
        build(self.tmp)
        papers = (self.tmp / "disease-models" / "fixture" / "registries"
                  / "paper_registry_current.md")
        papers.write_text(
            papers.read_text(encoding="utf-8").replace(
                "**Claim links:** 100", "**Claim links:** 777"),
            encoding="utf-8")
        result = tcf.Foundation(self.tmp, "fixture").trace("CLAIM 100")
        self.assertEqual({entry["edge"] for entry in result["supports"]}, {"wikilink_only"})
        self.assertEqual(result["species_drift"], [],
                         "a wikilink-only reference is navigation, not evidence")

    def test_coverage_is_always_reported(self) -> None:
        coverage = self.trace()["coverage"]
        self.assertEqual(coverage["supporting_papers"], 2)
        self.assertEqual(coverage["manifest_backed"], 0,
                         "the fixture ships no manifests, and the report must say so")


class RecordSplitBattery(unittest.TestCase):
    """The paper registry interleaves 49 PAPER records with 356 CORPUS placeholders."""

    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="trace-split-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_a_corpus_placeholder_cannot_donate_a_field_to_the_paper_above_it(self) -> None:
        """Split on one convention and the placeholder's body joins its neighbour's.

        The live registries survived that defect only because every PAPER happened to
        declare its own fields and the parser keeps the first occurrence. This fixture
        removes that luck: PAPER 900 declares no species, and the CORPUS placeholder
        immediately below it declares one. Inheriting it would be silent and wrong.
        """
        build(self.tmp, papers=("900",))
        papers = (self.tmp / "disease-models" / "fixture" / "registries"
                  / "paper_registry_current.md")
        # The field must be *absent*, not empty. An empty declaration is still a first
        # occurrence, and `declared_fields` keeps the first — so a fixture that merely
        # blanks it would pass against the broken split too, and prove nothing.
        text = "\n".join(line for line in papers.read_text(encoding="utf-8").splitlines()
                         if not line.startswith("**Model/species:**"))
        papers.write_text(
            text + "\n## CORPUS-STUB-004\n**Model/species:** rat\n**Claim links:** none\n",
            encoding="utf-8")
        foundation = tcf.Foundation(self.tmp, "fixture")
        self.assertEqual(foundation.papers["PAPER 900"].get("Model/species", ""), "",
                         "PAPER 900 declares no species and must not inherit the "
                         "placeholder's")
        self.assertNotIn("CORPUS-STUB-004", foundation.papers)

    def test_the_live_paper_registry_splits_into_exactly_its_papers(self) -> None:
        """🔴 The count is derived from the file, never pinned.

        This assertion read `== 49` until 2026-08-10, when `PAPER 060` was promoted and the
        suite went red for a correct change. That is the defect `CLAUDE.md` names first: a
        number a human must remember to update is a number someone will bump to make the
        suite green, which is the gesture the check exists to prevent. What the test actually
        means is that splitting the registry yields one record per `## PAPER` heading and
        absorbs nothing — no placeholder, no stray block — so it counts the headings and
        compares. Updating it now costs exactly as much as complying with it: nothing, and
        it still fails the moment a record is swallowed.
        """
        foundation = tcf.Foundation(REPO, "wwox")
        headings = re.findall(
            r"(?m)^## (PAPER \d+)\s*$",
            (REPO / "disease-models" / "wwox" / "registries"
             / "paper_registry_current.md").read_text(encoding="utf-8"))
        self.assertTrue(all(pid.startswith("PAPER ") for pid in foundation.papers))
        self.assertEqual(sorted(foundation.papers), sorted(headings))


class LineageBattery(unittest.TestCase):
    """The multi-hop half: the 2026-08-06 defect was three hops, not one."""

    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="trace-lineage-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def lineage(self, **kwargs) -> dict:
        for child in list(self.tmp.iterdir()):
            shutil.rmtree(child, ignore_errors=True)
        build(self.tmp, **kwargs)
        return tcf.Foundation(self.tmp, "fixture").lineage("CLAIM 100")

    def test_an_indirect_hop_reaches_a_different_organism(self) -> None:
        """A mouse claim resting on a mouse paper that cites a rat paper."""
        result = self.lineage(
            claim_model="mouse", papers=("900", "902"),
            species={"900": "mouse", "902": "rat"},
            links="[[paper_registry_current#PAPER 900]]",
            claim_links={"902": "777"},
            paper_links={"900": ("902",)})
        crossings = result["indirect_species_crossings"]
        self.assertEqual([hop["paper"] for hop in crossings], ["PAPER 902"])
        self.assertEqual(crossings[0]["path"], ["PAPER 900", "PAPER 902"])
        self.assertEqual(crossings[0]["depth"], 1)

    def test_mutation_cutting_the_bond_removes_the_reach(self) -> None:
        """Proves the walk is driven by declared bonds and nothing else."""
        result = self.lineage(
            claim_model="mouse", papers=("900", "902"),
            species={"900": "mouse", "902": "rat"},
            links="[[paper_registry_current#PAPER 900]]",
            claim_links={"902": "777"},
            paper_links={})
        self.assertEqual(result["indirect_species_crossings"], [])
        self.assertEqual([hop["paper"] for hop in result["reached"]], ["PAPER 900"])

    def test_a_reference_only_paper_does_not_seed_the_walk(self) -> None:
        """Only evidential edges seed the lineage; a cross-reference is not a foundation."""
        build(self.tmp, papers=("900", "902"), species={"900": "mouse", "902": "rat"},
              links="[[paper_registry_current#PAPER 900]]", claim_links={"902": "777"},
              paper_links={"900": ("902",)})
        papers = (self.tmp / "disease-models" / "fixture" / "registries"
                  / "paper_registry_current.md")
        papers.write_text(
            papers.read_text(encoding="utf-8").replace(
                "**Claim links:** 100", "**Claim links:** 777"),
            encoding="utf-8")
        result = tcf.Foundation(self.tmp, "fixture").lineage("CLAIM 100")
        self.assertEqual(result["reached"], [],
                         "nothing evidential to start from means nothing to walk")


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

    def test_claim_005_lineage_reaches_the_true_terminus(self) -> None:
        """The Phase-2 criterion, written down before the paper graph was inspected.

        Following declared paper-to-paper bonds outward from CLAIM 005 must reach
        PMID 17803050 — the terminal source of the imported-premise chain — which the claim
        does not link directly. One hop short of that, the lineage adds nothing the
        single-hop species check did not already have.
        """
        result = tcf.Foundation(REPO, "wwox").lineage("CLAIM 005")
        reached = {hop["pmid"]: hop for hop in result["reached"]}
        self.assertIn("17803050", reached, "the true terminus was not reached")
        self.assertGreaterEqual(reached["17803050"]["depth"], 1,
                                "reaching it directly would mean the claim already linked it")
        self.assertEqual(reached["17803050"]["species"], "rat")

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
