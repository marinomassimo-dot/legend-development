#!/usr/bin/env python3
"""Regressions for the UNLINKED_SUPPORT cross-check (`support_linkage.py`).

The defect, measured 2026-09-14 before this suite existed: a claim can name a paper as its
evidence while the paper's own registry record says nothing about that claim — or is still an
unscreened `CORPUS-STUB` with `Claim links: none`. PMID 30285739 sat in exactly that state
while three working documents called it the only independent support for a live claim. The
existing ratchets look the other way (a declaration with no receipt); nothing looked here.

Expectations below were written before `support_linkage.py` existed. The LINT-level test is
the proof of the defect: on the unmodified engine it fails because LINT emits no finding at
all for a claim resting on a stub.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from legend_lint import lint  # noqa: E402
from test_legend_lint import make_repository  # noqa: E402

CLAIMS = (
    "# Claim Registry\n"
    "## CLAIM 001\n"
    "**Status:** in observation\n"
    "**Summary:** The only independent support is Bonin 2018 (PMID 30285739).\n"
    "**Source:** Hussain 2018; PMID 30619736\n"
    "**Wikilinks:** [[paper_registry_current#PAPER 001]]\n"
    "\n"
    "## CLAIM 002\n"
    "**Status:** in observation\n"
    "**Summary:** rests on one paper.\n"
    "**Source:** PMID 11111111\n"
    "**Clinical meaning:** incidental mention of PMID 99999991 outside the scoped fields\n"
    "**Wikilinks:** [[paper_registry_current#PAPER 002]]\n"
    "\n"
    "## CLAIM 003\n"
    "**Status:** in observation\n"
    "**Summary:** nothing here.\n"
    "**Evidence boundary (BATCH_20260806_002):** bounded by PMID 22222222 and PMID 33333333\n"
    "**Source:** papers 1-3\n"
    "**Wikilinks:** [[paper_registry_current#PAPER 003]]\n"
    "\n"
    "## CLAIM 004\n"
    "**Status:** in observation\n"
    "**Summary:** cites PMID 44444444.\n"
    "**Source:** PMID 44444444\n"
    "**Wikilinks:** [[paper_registry_current#PAPER 004]]\n"
)

PAPERS = (
    "# Paper Registry\n"
    "## PAPER 001\n"
    "**Identifier:** PMID 30619736 / DOI 10.3389/fonc.2018.00591\n"
    "**Status:** integrated\n"
    "**Claim links:** 001\n"
    "\n"
    "## PAPER 002\n"
    "**Identifier:** PMID 11111111\n"
    "**Status:** integrated\n"
    "**Claim links:** 005 (new) · 006 (supports)\n"
    "\n"
    "## PAPER 003\n"
    "**Identifier:** PMID 22222222\n"
    "**Status:** integrated\n"
    "**Claim links:** 003 (bounds)\n"
    "\n"
    "## PAPER 004\n"
    "**Identifier:** PMID 44444444\n"
    "**Status:** integrated\n"
    "**Claim links:** none — deliberately none. `CLAIM 004` must NOT be linked to this record\n"
    "\n"
    "## CORPUS-STUB-165\n"
    "**Identifier:** PMID 30285739 / DOI 10.1186/s12915-018-0576-6\n"
    "**Status:** not_processed\n"
    "**Claim links:** none\n"
)


def pairs(results, kind):
    return {(r.claim, r.pmid) for r in results if r.kind == kind}


class TheCrossCheckFindsSupportTheRegistryDoesNotLink(unittest.TestCase):
    def setUp(self) -> None:
        import support_linkage  # noqa: PLC0415 - absent before the fix, by design
        self.mod = support_linkage
        self.results = support_linkage.check(CLAIMS, PAPERS)

    def test_a_claim_resting_on_a_stub_is_unlinked_support(self) -> None:
        hit = [r for r in self.results if (r.claim, r.pmid) == ("CLAIM 001", "30285739")]
        self.assertEqual(1, len(hit), self.results)
        self.assertEqual("UNLINKED_SUPPORT", hit[0].kind)
        self.assertEqual("CORPUS-STUB-165", hit[0].record)
        self.assertIn("CORPUS-STUB", hit[0].reason)

    def test_a_paper_whose_claim_links_omit_the_claim_is_unlinked_support(self) -> None:
        self.assertIn(("CLAIM 002", "11111111"), pairs(self.results, "UNLINKED_SUPPORT"))

    def test_a_deliberate_none_that_mentions_the_claim_is_not_a_link(self) -> None:
        """PAPER 082 in the live registry reads exactly like this, and two existing
        parsers take the claim number inside the refusal as a link."""
        self.assertIn(("CLAIM 004", "44444444"), pairs(self.results, "UNLINKED_SUPPORT"))

    def test_a_linked_paper_is_clean(self) -> None:
        clean = {("CLAIM 001", "30619736"), ("CLAIM 003", "22222222")}
        self.assertFalse(clean & pairs(self.results, "UNLINKED_SUPPORT"), self.results)
        self.assertFalse(clean & pairs(self.results, "UNCHECKED"), self.results)

    def test_an_unresolvable_identifier_is_unchecked_not_unlinked(self) -> None:
        self.assertIn(("CLAIM 003", "33333333"), pairs(self.results, "UNCHECKED"))
        self.assertNotIn(("CLAIM 003", "33333333"), pairs(self.results, "UNLINKED_SUPPORT"))

    def test_only_the_scoped_fields_are_read(self) -> None:
        every = {(r.claim, r.pmid) for r in self.results}
        self.assertNotIn(("CLAIM 002", "99999991"), every)

    def test_a_promoted_paper_owns_the_pmid_over_its_preserved_stub(self) -> None:
        papers = PAPERS + (
            "\n## PAPER 095\n"
            "**Identifier:** PMID 30285739 / PMCID PMC6169085\n"
            "**Status:** processed\n"
            "**Claim links:** 001 (second source)\n"
        )
        results = self.mod.check(CLAIMS, papers)
        self.assertNotIn(("CLAIM 001", "30285739"),
                         {(r.claim, r.pmid) for r in results}, results)

    def test_the_claim_links_grammar(self) -> None:
        parse = self.mod.declared_claim_links
        self.assertEqual(set(), parse("none"))
        self.assertEqual(set(), parse("none — triage only"))
        self.assertEqual(set(), parse("pending"))
        self.assertEqual(set(), parse(""))
        self.assertEqual({"CLAIM 002"}, parse("002"))
        self.assertEqual({"CLAIM 014", "CLAIM 015"}, parse("014, 015"))
        self.assertEqual({"CLAIM 021"}, parse("→ CLAIM 021"))
        self.assertEqual({"CLAIM 034", "CLAIM 028", "CLAIM 009"},
                         parse("034 (new) · 028 (supports) · 009 (tensions)"))
        # numbers inside an annotation are not links
        self.assertEqual({"CLAIM 028"},
                         parse("→ CLAIM 028 (source pointer normalized to 207/218/206/214)"))

    def test_the_rendered_line_is_one_pair_per_line(self) -> None:
        lines = self.mod.render(self.results).splitlines()
        unlinked = [line for line in lines if line.startswith("UNLINKED_SUPPORT ")]
        self.assertEqual(len(pairs(self.results, "UNLINKED_SUPPORT")), len(unlinked))
        self.assertTrue(all("CLAIM " in line and "PMID " in line for line in unlinked))

    def test_it_reuses_the_shared_registry_parser(self) -> None:
        """A second record splitter is how CORPUS-STUB bodies once overwrote PAPER 032."""
        import coverage_report  # noqa: PLC0415
        self.assertIs(self.mod.parse_entries, coverage_report.parse_entries)
        self.assertIs(self.mod.PMID, coverage_report.PMID)


# HARNESS-P11-20260914. The three sentences below are VERBATIM from the claim registry: CLAIM
# 036 as it stands on `main` today, CLAIM 003 and CLAIM 007 as they stood at f435cd0^, before
# BATCH_20260914_007 repaired their registry side. Expectations were fixed before the change:
# 036 is a contrast (its subject is a DIFFERENCE of Cre driver, attributed to CLAIM 005, which is
# the claim PAPER 006 does link); 003 and 007 are support, and must stay so.
REAL_036 = (
    "🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK` — **l'ablazione di Wwox nel cervello non è mai "
    "mostrata**: il western copre rene, polmone e milza (identità dei tessuti visibile solo nel "
    "raster di Fig. 2C) e l'IHC solo il rene. Una Cre zigotica rende attesa la delezione globale, "
    "ma l'attesa non è misura. **`REVIVAL_TRIGGER`:** un western o un'IHC su lisato cerebrale da "
    "`EIIA-Cre; Wwox^ΔCre/ΔCre`, da qualunque fonte. 🔴 Driver Cre **diverso** da quello di "
    "[[claim_registry_current#CLAIM 005]]: EIIA-Cre qui, BK5-Cre in PMID 30290271 — allele "
    "floxed condiviso, knockout diverso."
)
REAL_003 = (
    "il lavoro gemello del 2021 dallo stesso laboratorio ([[paper_registry_current#PAPER 005]], "
    "PMID 34747138, letto integralmente) rafforza il meccanismo e ne segna il limite nello stesso "
    "gesto. **Rafforza:** gli oligodendrociti **non sono mai trasdotti** dal vettore "
    "neurone-specifico, verificato con co-staining CC1/anti-WWOX, e la mielinizzazione migliora "
    "comunque — è la prova diretta che l'effetto passa per i neuroni."
)
REAL_007 = (
    "the protein arm is the 10% input lane of a pull-down at n = 2/group, not a dedicated "
    "quantified western, and no densitometry appears anywhere in the paper; the per-lane figures "
    "are direction and rank order, never a fold-change. *(Amended twice on 2026-09-13 and "
    "propagated in `BATCH_20260913_003`: first by independent verification, which found \"normal "
    "protein\" too strong, then in the opposite direction by the blind locator audit that "
    "verification triggered, which refused \"not detectably reduced\" as asserting a negative "
    "the panel contradicts. Mechanism primary: PMID 15064722, read 2026-09-13, receipt "
    "`FTR-20260913-15064722-01`.)*"
)

# Wikilinks are present so LINT's CLAIM_NO_PAPER rule does not block before the property under
# test is reached; they are not part of what is classified.
REAL_CLAIMS = (
    "# Claim Registry\n"
    "## CLAIM 003\n**Status:** consolidated baseline\n**Summary:** x\n"
    f"**Evidence boundary — quanto lontano arriva «non-cell-autonoma» (2026-08-10):** {REAL_003}\n"
    "**Wikilinks:** [[paper_registry_current#PAPER 005]]\n"
    "\n## CLAIM 007\n**Status:** consolidated baseline\n"
    f"**Summary:** {REAL_007}\n"
    "**Wikilinks:** [[paper_registry_current#PAPER 005]]\n"
    "\n## CLAIM 036\n**Status:** in observation\n**Summary:** x\n"
    f"**Evidence boundary:** {REAL_036}\n"
    "**Wikilinks:** [[paper_registry_current#PAPER 006]]\n"
)
REAL_PAPERS = (
    "# Paper Registry\n"
    "## PAPER 005\n**Identifier:** PMID 34747138\n**Status:** integrated\n**Claim links:** 004\n"
    "\n## PAPER 006\n**Identifier:** PMID 30290271\n**Status:** integrated\n**Claim links:** 005\n"
    "\n## CORPUS-STUB-143\n**Identifier:** PMID 15064722\n**Status:** not_processed\n"
    "**Claim links:** none\n"
)


def one(results, claim, pmid):
    hit = [r for r in results if (r.claim, r.pmid) == (claim, pmid)]
    assert len(hit) == 1, results
    return hit[0]


class CitedAsSupportIsNotCitedAsContrast(unittest.TestCase):
    """The flag that nearly wrote a false edge into PAPER 006.

    Before this change the check had two outcomes and reported every unlinked mention as
    UNLINKED_SUPPORT, which invited an integrator to add `036` to PAPER 006's `Claim links` —
    a support the claim's own sentence denies.
    """

    def setUp(self) -> None:
        import support_linkage  # noqa: PLC0415
        self.mod = support_linkage
        self.results = support_linkage.check(REAL_CLAIMS, REAL_PAPERS)

    def test_the_real_claim_036_sentence_is_cited_as_contrast(self) -> None:
        hit = one(self.results, "CLAIM 036", "30290271")
        self.assertEqual("POSSIBLE_CONTRAST", hit.kind, hit)
        self.assertIn("CLAIM 005", hit.reason)          # says WHY: attributed to the linked claim
        self.assertIn("30290271", hit.sentence)         # and shows the sentence it read

    def test_claim_003_before_batch_007_is_still_unlinked_support(self) -> None:
        self.assertEqual("UNLINKED_SUPPORT", one(self.results, "CLAIM 003", "34747138").kind)

    def test_claim_007_before_batch_007_is_still_unlinked_support(self) -> None:
        hit = one(self.results, "CLAIM 007", "15064722")
        self.assertEqual("UNLINKED_SUPPORT", hit.kind, hit)
        self.assertEqual("CORPUS-STUB-143", hit.record)

    def test_every_finding_carries_the_sentence_it_was_classified_on(self) -> None:
        for result in self.results:
            self.assertIn(result.pmid, result.sentence, result)

    # --- the two foreseeable failure modes, each pinned -------------------------------------

    def _kind(self, sentence: str, links: str = "005") -> str:
        claims = f"# C\n## CLAIM 036\n**Status:** x\n**Evidence boundary:** {sentence}\n"
        papers = f"# P\n## PAPER 006\n**Identifier:** PMID 30290271\n**Claim links:** {links}\n"
        return one(self.mod.check(claims, papers), "CLAIM 036", "30290271").kind

    def test_an_unlisted_contrast_phrasing_is_unclassified_never_silent(self) -> None:
        """Failure mode 1: an author's phrasing defeats the vocabulary. The pair must stay
        loud (UNCLASSIFIED), not vanish and not be guessed."""
        self.assertEqual("UNCLASSIFIED", self._kind(
            "Il modello di [[claim_registry_current#CLAIM 005]] (PMID 30290271) non va "
            "confuso con questo: altro driver."))

    def test_a_contrast_word_alone_does_not_suppress_support(self) -> None:
        """Failure mode 2: a contrast word in a supporting sentence, with nothing that
        attributes the PMID to another claim the paper links, is not a contrast."""
        self.assertEqual("UNCLASSIFIED", self._kind(
            "A different cohort (PMID 30290271) independently replicates the phenotype."))

    def test_another_linked_claim_without_a_contrast_marker_is_unclassified(self) -> None:
        """'consistent with CLAIM 005 in PMID X' may be support for both: a human reads it."""
        self.assertEqual("UNCLASSIFIED", self._kind(
            "Same allele as [[claim_registry_current#CLAIM 005]], PMID 30290271."))

    def test_a_named_claim_the_paper_does_not_link_is_no_anchor(self) -> None:
        self.assertEqual("UNCLASSIFIED", self._kind(
            "Unlike [[claim_registry_current#CLAIM 009]], PMID 30290271 used BK5-Cre.",
            links="005"))

    def test_english_and_mixed_language_contrasts_are_recognised(self) -> None:
        for sentence in (
            "Unlike [[claim_registry_current#CLAIM 005]], which used BK5-Cre (PMID 30290271), "
            "this model is zygotic.",
            "Whereas CLAIM 005 rests on PMID 30290271, here the driver is EIIA-Cre.",
            "A differenza di CLAIM 005 (PMID 30290271, BK5-Cre), qui il driver è EIIA-Cre.",
            "Driver distinct from CLAIM 005: BK5-Cre in PMID 30290271, EIIA-Cre qui.",
        ):
            self.assertEqual("POSSIBLE_CONTRAST", self._kind(sentence), sentence)

    def test_the_contrast_scope_is_the_sentence_not_the_field(self) -> None:
        """A contrast in a neighbouring sentence says nothing about the PMID's sentence."""
        self.assertEqual("UNLINKED_SUPPORT", self._kind(
            "Driver diverso da [[claim_registry_current#CLAIM 005]]. "
            "Il fenotipo è confermato in PMID 30290271."))


class LintSurfacesTheCrossCheckWithoutBlocking(unittest.TestCase):
    """The proof of the defect: LINT said nothing about any of the pairs above."""

    def test_lint_reports_unlinked_support_and_does_not_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            make_repository(Path(temporary), CLAIMS, PAPERS)
            result = lint(temporary)
        codes = [(f.severity, f.code, f.message) for f in result.findings]
        unlinked = [c for c in codes if c[1] == "UNLINKED_SUPPORT"]
        self.assertTrue(unlinked, f"LINT emitted no UNLINKED_SUPPORT finding: {codes}")
        self.assertTrue(all(c[0] == "WARN_BUT_PROCEED" for c in unlinked), unlinked)
        self.assertTrue(any("CLAIM 001" in c[2] and "30285739" in c[2] for c in unlinked))
        unchecked = [c for c in codes if c[1] == "UNLINKED_SUPPORT_UNCHECKED"]
        self.assertTrue(unchecked and all(c[0] == "INFO" for c in unchecked), codes)
        self.assertFalse(result.blocks_commit, codes)

    def test_lint_reports_possible_contrast_and_unclassified_as_warn(self) -> None:
        claims = REAL_CLAIMS + (
            "\n## CLAIM 040\n**Status:** in observation\n"
            "**Evidence boundary:** A different cohort (PMID 34747138) replicates it.\n"
            "**Wikilinks:** [[paper_registry_current#PAPER 005]]\n")
        with tempfile.TemporaryDirectory() as temporary:
            make_repository(Path(temporary), claims, REAL_PAPERS)
            result = lint(temporary)
        codes = [(f.severity, f.code, f.message) for f in result.findings]
        contrast = [c for c in codes if c[1] == "POSSIBLE_CONTRAST"]
        self.assertTrue(contrast and all(c[0] == "WARN_BUT_PROCEED" for c in contrast), codes)
        self.assertTrue(any("CLAIM 036" in c[2] for c in contrast), codes)
        self.assertFalse(any(c[1] == "UNLINKED_SUPPORT" and "CLAIM 036" in c[2] for c in codes))
        unclassified = [c for c in codes if c[1] == "UNLINKED_SUPPORT_UNCLASSIFIED"]
        self.assertTrue(unclassified and all(c[0] == "WARN_BUT_PROCEED" for c in unclassified))
        self.assertFalse(result.blocks_commit, codes)

    def test_a_registry_without_pmids_stays_pass(self) -> None:
        from test_legend_lint import GOOD_CLAIMS, GOOD_PAPERS  # noqa: PLC0415
        with tempfile.TemporaryDirectory() as temporary:
            make_repository(Path(temporary), GOOD_CLAIMS, GOOD_PAPERS)
            self.assertEqual("PASS", lint(temporary).verdict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
