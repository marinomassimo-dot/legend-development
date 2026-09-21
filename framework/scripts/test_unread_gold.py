#!/usr/bin/env python3
"""Regressions for `unread_gold.py`.

Three defects are pinned here, all found on 2026-09-21 while chasing a scientific question
rather than while auditing the harness. That is the order they matter in: each one made the
tool answer "nothing to read" when there was something to read.

1. **The selector regexes matched the wrong field spelling.** `tier` looked for
   `**Tier (PHASE 1):**` and the registry writes `**Tier (FASE 1):**` (187 records, zero in
   English); `relevance` looked for `**Relevance:**` and the registry writes
   `**clinical relevance:**` (254 records, zero of the short form). Both selectors matched
   NOTHING, so the default filter could never fire and printed
   "No unread Tier-A / Relevance-HIGH CORPUS" — a parse failure wearing the costume of an
   all-clear. This is the repository's own rule applied to its own tool: a zero from a parser
   is not evidence of absence until the parser is shown to be reading the document.

2. **The mechanism lens had no vocabulary for catalysis.** It hunts the proteostasis half of
   the missense question (*is the protein there?*) and had no term for the other half
   (*does the protein work?*). `PMID 21476439` — the only published measurement of WWOX
   enzymatic activity, with steroid substrates, NAD+/NADP+ dependence and Km values — was
   invisible to BOTH paths while sitting on the registry as Tier C, `background only`.

3. **The tool never consulted the reading ledger.** It decided what to read next from the
   registry's own `Status` field alone, and that field goes stale: 19 placeholders advertised
   as "never deep-dived" carry complete- or partial-read receipts. A reading queue that cannot
   see the reading ledger dispatches duplicate work.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import unread_gold as ug  # noqa: E402

REPO = Path(__file__).resolve().parents[2]

FASE_RECORD = """## CORPUS P999
**Short title:** A test placeholder
**Full title:** WWOX oxidoreductase--substrate and enzymatic characterization
**Authors:** Nobody et al.
**Year:** 2011
**Source type:** Article
**Journal/source:** Test
**Identifier:** PMID 21476439
**Tier (FASE 1):** A
**Status:** screened — corpus placeholder
**clinical relevance:** HIGH
**Primary pathway:** P5
**Note:** no deep-dive performed
"""


class FieldSpelling(unittest.TestCase):
    def test_italian_tier_field_is_parsed(self):
        rec = ug.parse_blocks(FASE_RECORD)[0]
        self.assertEqual(rec["tier"], "A", "**Tier (FASE 1):** must parse; the registry has no "
                                           "record spelled PHASE")

    def test_clinical_relevance_field_is_parsed(self):
        rec = ug.parse_blocks(FASE_RECORD)[0]
        self.assertEqual(rec["relevance"], "HIGH", "**clinical relevance:** must parse; the "
                                                   "registry has no bare **Relevance:** record")

    def test_english_tier_spelling_still_parses(self):
        rec = ug.parse_blocks(FASE_RECORD.replace("FASE", "PHASE"))[0]
        self.assertEqual(rec["tier"], "A", "the English spelling this tool was written against "
                                           "must keep working")

    def test_the_live_registry_actually_yields_tiers(self):
        """The unit test above can pass on a fixture while the real registry yields nothing.

        That is exactly how defect 1 survived: nobody measured the tool against the document.
        """
        text = (REPO / ug.REGISTRY).read_text(encoding="utf-8")
        recs = ug.parse_blocks(text)
        tiered = [r for r in recs if r["tier"].strip()]
        self.assertGreater(len(tiered), 100,
                           "the live registry must yield tiers; if this drops to ~0 the field "
                           "spelling has drifted again and the default filter is dead")


class MechanismLens(unittest.TestCase):
    def test_enzymology_title_is_a_mechanism_signal(self):
        rec = ug.parse_blocks(FASE_RECORD)[0]
        self.assertTrue(ug.has_mechanism_signal(rec),
                        "a paper titled 'oxidoreductase -- substrate and enzymatic "
                        "characterization' is the assay TX-003 is blocked on; the lens must see it")

    def test_catalysis_terms_are_covered(self):
        for title in ("Km determination for a recombinant dehydrogenase",
                      "NADPH cofactor specificity of a reductase",
                      "Crystal structure of the SDR domain",
                      "Deep mutational scanning of a tumour suppressor",
                      "Thermal stability of purified protein"):
            rec = dict(title=title, short="", note="", pathway="")
            self.assertTrue(ug.has_mechanism_signal(rec), f"lens missed: {title}")

    def test_lens_still_catches_the_proteostasis_half(self):
        """The catalysis clause must ADD, never displace. Defect 2 was a gap, not a swap."""
        for title in ("Lysosomal degradation of a missense variant",
                      "Chaperone-mediated autophagy and protein turnover",
                      "p.Gln230Pro destabilises the fold"):
            rec = dict(title=title, short="", note="", pathway="")
            self.assertTrue(ug.has_mechanism_signal(rec), f"lens lost: {title}")

    def test_substrate_class_terms_are_covered(self):
        """Defect 2 had a second layer: a census run WITH catalysis terms but WITHOUT substrate
        terms still concluded the substrate question was 'steroids or nothing', because its own
        vocabulary contained no retinoid. A lens that names only the substrate class it already
        suspects will keep confirming it."""
        for title in ("A retinal oxidoreductase acting on all-trans-retinal",
                      "Steroid dehydrogenase specificity",
                      "Fatty acid substrate preference of an orphan enzyme",
                      "Retinol metabolism in neural tissue"):
            rec = dict(title=title, short="", note="", pathway="")
            self.assertTrue(ug.has_mechanism_signal(rec), f"lens missed: {title}")

    def test_pure_epidemiology_is_not_a_mechanism_signal(self):
        rec = dict(title="WWOX expression correlates with overall survival in a cohort",
                   short="", note="", pathway="")
        self.assertFalse(ug.has_mechanism_signal(rec),
                         "the lens must stay selective; widening it to everything is the same "
                         "as switching it off")


class LedgerCrossCheck(unittest.TestCase):
    def test_absent_ledger_yields_empty_mapping_not_a_false_negative(self):
        self.assertEqual(ug.ledger_depths(Path("/nonexistent-workspace")), {},
                         "an absent ledger must annotate NOTHING; absent ledger != absent "
                         "receipt, and the tool must not report the second when it means the "
                         "first")

    def test_live_ledger_is_readable_and_keyed_by_pmid(self):
        depths = ug.ledger_depths(REPO)
        self.assertGreater(len(depths), 50, "the live receipt ledger must be readable and keyed "
                                            "by study_id.pmid")
        self.assertIn("19936220", depths, "a known complete read must be found by PMID")
        self.assertIn("complete_fulltext_read", depths["19936220"])

    def test_record_pmid_extraction(self):
        rec = {"ident": "PMID 21476439"}
        self.assertEqual(ug.record_pmid(rec), "21476439")
        self.assertEqual(ug.record_pmid({"ident": "PMID 19936220 / PMC2777388 / DOI 10.1371/x"}),
                         "19936220")
        self.assertEqual(ug.record_pmid({"ident": "no identifier here"}), "")

    def test_already_read_rows_are_flagged_in_json_output(self):
        """The regression that matters operationally: a read paper must not be offered as unread
        without a warning attached to it."""
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ug.main([str(REPO), "--all", "--json"])
        rows = json.loads(buf.getvalue())
        stale = [r for r in rows if r.get("already_read")]
        self.assertTrue(stale, "at least one placeholder is known to carry a read receipt; if "
                               "this goes to zero the cross-check has stopped working, not the "
                               "registry become clean — verify before believing it")
        self.assertTrue(all(r["receipt_depths"] for r in stale),
                        "a flagged row must name the depths that flagged it")


if __name__ == "__main__":
    unittest.main(verbosity=2)
