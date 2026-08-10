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
import hashlib
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

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
        "verbatim_locators": {"source_fulltext_indexed": True, "source_fulltext_indexed_evidence": "Europe PMC EXT_ID:1 on 2026-08-07: inEPMC=Y, PMCID PMC1 — fixture lookup", "entries": [
            {"proposition": "WWOX 388-407 is required for the interaction with GSK3beta",
             "snippet": "This indicates that WWOX amino acids 388-407 are required for its interaction with GSK3b.",
             "surface": "body", "anchor": "Results, Fig. 3c"}]},
    }
    manifest.update(overrides)
    return manifest


def schema_v2(artifact_path: str = "files/fulltext/paper.xml", **overrides) -> dict:
    manifest = minimal()
    manifest["schema_version"] = 2
    manifest["source_artifacts"] = [{
        "path": artifact_path,
        "sha256": "a" * 64,
        "kind": "article_text",
    }]
    manifest["verbatim_locators"]["entries"][0]["artifact"] = artifact_path
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

    def test_schema_v2_requires_surface_on_every_locator(self) -> None:
        manifest = schema_v2()
        del manifest["verbatim_locators"]["entries"][0]["surface"]
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("surface: required" in error for error in errors))

    def test_schema_v2_requires_declared_artifact_on_every_locator(self) -> None:
        manifest = schema_v2()
        manifest["verbatim_locators"]["entries"][0]["artifact"] = "other.xml"
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("not declared in source_artifacts" in error for error in errors))

    def test_schema_v2_refuses_even_one_abstract_evidence_locator(self) -> None:
        manifest = schema_v2()
        manifest["verbatim_locators"]["entries"][0]["surface"] = "abstract"
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("cannot be an evidentiary locator" in error for error in errors))

    def test_schema_v2_allows_abstract_snippet_only_as_body_locator_companion(self) -> None:
        manifest = schema_v2()
        manifest["verbatim_locators"]["entries"][0]["abstract_snippet"] = (
            "The abstract independently states the same headline proposition."
        )
        errors, _ = gate.validate(manifest)
        self.assertEqual(errors, [])

    def test_current_schema_is_a_write_time_ratchet(self) -> None:
        errors, _ = gate.validate(minimal(), require_current_schema=True)
        self.assertTrue(any("new complete reads require" in error for error in errors))

    def test_strict_verification_distinguishes_abstract_from_body(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = "files/fulltext/paper.xml"
            artifact = root / relative
            artifact.parent.mkdir(parents=True)
            artifact.write_text(
                "<article><abstract><p>The abstract-only proposition has enough characters "
                "to pass the minimum.</p></abstract><body><p>A different body sentence also "
                "has enough characters.</p></body></article>", encoding="utf-8")
            manifest = schema_v2(relative)
            manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
                artifact.read_bytes()).hexdigest()
            entry = manifest["verbatim_locators"]["entries"][0]
            entry["snippet"] = "The abstract-only proposition has enough characters to pass the minimum."
            entry["surface"] = "body"
            errors, _ = gate.validate(manifest, root=root, verify_artifacts=True)
            self.assertTrue(any("abstract but not the non-abstract body" in e for e in errors))

    def _comparator_fixture(self, root: Path, body: str, snippet: str):
        """A one-locator schema-v2 manifest over a body of our choosing."""
        relative = "files/fulltext/paper.xml"
        artifact = root / relative
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text(
            f"<article><abstract><p>Unrelated abstract sentence of ample length.</p>"
            f"</abstract><body><p>{body}</p></body></article>", encoding="utf-8")
        manifest = schema_v2(relative)
        manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
            artifact.read_bytes()).hexdigest()
        entry = manifest["verbatim_locators"]["entries"][0]
        entry["snippet"] = snippet
        entry["surface"] = "body"
        return gate.validate(manifest, root=root, verify_artifacts=True)

    def test_a_comparator_cannot_be_folded_away(self) -> None:
        """🔴 The defect this repository was one manifest away from institutionalising.

        Alphanumeric folding maps `(P < 0.05)`, `(P > 0.05)` and `(P 0.05)` onto `P005`. A
        quote claiming significance would verify against a source stating the opposite, and
        the gate would stamp it `verified`. That is the CLAIM 005 axis exactly.
        """
        with TemporaryDirectory() as temporary:
            errors, _ = self._comparator_fixture(
                Path(temporary),
                body="The difference was not significant (P &gt; 0.05) in either cohort here.",
                snippet="The difference was not significant (P < 0.05) in either cohort here.",
            )
            self.assertTrue(
                any("UNVERIFIABLE_PUNCTUATION" in error for error in errors),
                f"a flipped comparator must never verify; got {errors}",
            )

    def test_an_absent_comparator_cannot_be_folded_away(self) -> None:
        """The 2026-08-09 corpus case: the source lost the glyph, the quote copied the loss."""
        with TemporaryDirectory() as temporary:
            errors, _ = self._comparator_fixture(
                Path(temporary),
                body="Levels were significantly (P 0.05) higher in mutant than normal rats.",
                snippet="Levels were significantly (P < 0.05) higher in mutant than normal rats.",
            )
            self.assertTrue(any("UNVERIFIABLE_PUNCTUATION" in error for error in errors), errors)

    def test_markup_split_quotes_without_comparators_still_verify(self) -> None:
        """The fold is a real concession to PMC markup and must survive the repair.

        If tightening the matcher had broken this, the fix would have traded a silent false
        positive for a noisy false negative, and sessions would learn to route around it.
        """
        with TemporaryDirectory() as temporary:
            errors, _ = self._comparator_fixture(
                Path(temporary),
                body="Expression rose in the ventricular zone (Figure <italic>3E</italic>).",
                snippet="Expression rose in the ventricular zone (Figure 3E).",
            )
            self.assertEqual(errors, [], "a punctuation-only split must still fold cleanly")

    # 🔴 The first repair asked the wrong question. It asked "does the SNIPPET look risky?"
    # The question that decides correctness is "does normalising change the answer?" — and
    # the four cases below all answer yes while the snippet itself looks perfectly innocent.
    # Deletion, not substitution, is the dangerous direction: a quote that has LOST a
    # character carries nothing decisive to trigger a refusal.

    def test_a_deleted_comparator_cannot_verify_against_a_source_that_has_one(self) -> None:
        """The direction the first repair missed entirely.

        `(P 0.05)` holds no comparator, so no snippet-inspection rule can flag it — and it
        folds onto exactly the same key as the `(P < 0.05)` the source actually states.
        """
        with TemporaryDirectory() as temporary:
            errors, _ = self._comparator_fixture(
                Path(temporary),
                body="Levels were significantly (P &lt; 0.05) higher in mutants than controls.",
                snippet="Levels were significantly (P 0.05) higher in mutants than controls.",
            )
            self.assertNotEqual(
                errors, [],
                "a quote whose comparator is GONE must not verify against a source that has "
                "one; nothing about the snippet looks risky, which is the whole problem",
            )

    def test_a_c0_separator_is_not_whitespace_and_cannot_be_normalised_away(self) -> None:
        """`'\\x1d'.isspace()` is True, so `str.split()` silently eats the corruption.

        This is why the 17803050 locator is stamped `strict`: both sides normalise to the
        same string. A C0 separator is not whitespace in any typography — it is a glyph that
        did not survive extraction.
        """
        with TemporaryDirectory() as temporary:
            errors, _ = self._comparator_fixture(
                Path(temporary),
                body="Values were significantly (P \x1d 0.023) lower in the mutant cohort.",
                snippet="Values were significantly (P 0.023) lower in the mutant cohort.",
            )
            self.assertNotEqual(
                errors, [], "a C0 separator must never be treated as collapsible whitespace")

    def test_a_text_artifact_containing_c0_controls_is_refused_outright(self) -> None:
        """A declared surface holding C0 controls is SUSPECT: refused, not repaired.

        Normalising it would launder the defect into every quote drawn from it.
        """
        # A .txt derived from a PDF is where this defect actually lives — an XML carrying a
        # C0 control is not well-formed and already fails to parse, which is fail-closed but
        # by a different route and would not exercise this check.
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = "staging/derived.txt"
            artifact = root / relative
            artifact.parent.mkdir(parents=True, exist_ok=True)
            artifact.write_text(
                "Values were significantly (P \x1d 0.023) lower in the mutant cohort here.",
                encoding="utf-8")
            manifest = schema_v2(relative)
            manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
                artifact.read_bytes()).hexdigest()
            entry = manifest["verbatim_locators"]["entries"][0]
            entry["snippet"] = "Values were significantly (P 0.023) lower in the mutant cohort."
            entry["surface"] = "body"
            errors, _ = gate.validate(manifest, root=root, verify_artifacts=True)
            self.assertTrue(
                any("SUSPECT" in error for error in errors),
                f"the artifact itself must be refused as a verification surface; got {errors}",
            )

    def test_a_stripped_charge_cannot_verify_against_the_ion(self) -> None:
        """`Ca²⁺` folds to `Ca2`, and so does the plain text `Ca2`. The charge vanishes."""
        with TemporaryDirectory() as temporary:
            errors, _ = self._comparator_fixture(
                Path(temporary),
                body="Concentrations of the divalent cation Ca²⁺ were comparable across groups.",
                snippet="Concentrations of the divalent cation Ca2 were comparable across groups.",
            )
            self.assertNotEqual(
                errors, [], "a stripped ionic charge must not verify against the charged ion")

    def test_a_form_feed_standing_in_for_a_charge_sign_is_refused(self) -> None:
        """The real corpus case, not a constructed one.

        `files/fulltext/PMID17803050_Suzuki2007.html` contains the literal bytes
        `Ca2\\x0c, inorganic phos-` where the paper prints `Ca²⁺`. The form feed replaced the
        superscript plus. If `\\f` is treated as presentation whitespace it collapses to a
        space, `Ca2 ` matches the quoted `Ca2` STRICTLY, and the ion silently loses its charge
        in the record. `\\f` and `\\v` are not typography in extracted text — they are damage,
        and the whitespace class must contain only what a typesetter would set.
        """
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = "staging/derived.txt"
            artifact = root / relative
            artifact.parent.mkdir(parents=True, exist_ok=True)
            artifact.write_text(
                "Serum glucose (GLU), triglyceride (TG), Ca2\x0c, inorganic phosphate (IP) "
                "and creatine phosphokinase were measured in every animal of both cohorts.",
                encoding="utf-8")
            manifest = schema_v2(relative)
            manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
                artifact.read_bytes()).hexdigest()
            entry = manifest["verbatim_locators"]["entries"][0]
            entry["snippet"] = (
                "Serum glucose (GLU), triglyceride (TG), Ca2, inorganic phosphate (IP) "
                "and creatine phosphokinase were measured in every animal of both cohorts.")
            entry["surface"] = "body"
            errors, _ = gate.validate(manifest, root=root, verify_artifacts=True)
            self.assertTrue(
                any("SUSPECT" in error for error in errors),
                f"a form feed standing in for a charge sign must refuse the surface; got {errors}",
            )

    def test_an_image_anchor_must_contain_the_span_it_adjudicates(self) -> None:
        """🔴 Today image anchoring is the looser of the two, and this closes the gap.

        A text locator is compared character by character against its artifact. An image
        locator is believed on its word. On 2026-08-09 a crop declared to adjudicate a table
        row stopped at x=320 while the row ran to x=524, so four values inside the quoted span
        were outside the picture — a locator that would have been "verified" against pixels
        that were not there.

        Both rectangles are already available: the crop is declared, and `search_for` returns
        the span. Containment is arithmetic.
        """
        page_span = (191.0, 523.9, 524.2, 532.2)          # the BUN row, as the page has it
        self.assertFalse(
            gate.crop_contains_span((40, 505, 320, 560), page_span),
            "a crop that stops at x=320 cannot adjudicate a row reaching x=524",
        )
        self.assertTrue(
            gate.crop_contains_span((40, 480, 570, 562), page_span),
            "the corrected full-width crop does contain the row",
        )
        # Touching edges count as contained: a span flush against the crop boundary is fully
        # rendered. Off by a hair in the strict direction would reject correct artifacts and
        # teach people to pad crops arbitrarily.
        self.assertTrue(gate.crop_contains_span((191, 523.9, 524.2, 532.2), page_span))
        self.assertFalse(gate.crop_contains_span((191.5, 523.9, 524.2, 532.2), page_span))

    def _screen(self, name: str, payload: str):
        """Run the surface screen directly and return the refusal message, or ''."""
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / name
            path.write_text(payload, encoding="utf-8")
            try:
                gate._artifact_text(path, "article_text")
            except ValueError as error:
                return str(error)
        return ""

    def test_printable_substitutions_are_caught_though_no_control_is_present(self) -> None:
        """🔴 The C0 screen sees 34 corruptions in PMID 17803050. About 145 more are PRINTABLE.

        Adjudicated at 600 dpi against the page: `q` stands for `±` (140 occurrences in that
        one paper), `D2` for `χ²`, `t` for `×`. No control-character check will ever see them.
        Worse, if someone "repairs" the 34 controls the artifact goes clean at the C0 gate and
        stays wrong on the page — a silent, verified-looking lie.
        """
        for label, payload in (
            ("plus-minus as q", "Weights are given as mean 12 q 3 standard deviation units."),
            ("chi-squared as D2", "Incidence in mutant rats was analyzed by D2 test to confirm."),
            ("times as t", "Relative weight was absolute weight 100 t 100 divided by body mass."),
        ):
            with self.subTest(substitution=label):
                message = self._screen("derived.txt", payload)
                self.assertIn("SUSPECT", message, f"{label} must refuse the surface")

    def test_a_statistical_paper_with_no_operators_at_all_is_suspect(self) -> None:
        """Suspicion by ABSENCE — what the surface does not have.

        Fourteen corpus PDFs carry statistical language and not one of `< > ≤ ≥ ± × −`. Two
        of them are adjudicated corrupt. A paper that tests significance and never once prints
        a comparator is not a tidy paper; it is a text layer that lost them.
        """
        message = self._screen(
            "derived.txt",
            "Differences were significant by t test. The P value was small. Significance "
            "was assessed with a standard deviation of the mean across every cohort tested.")
        self.assertIn("SUSPECT", message)

    def test_the_absence_rule_reads_entities_not_raw_markup(self) -> None:
        """A PMC XML writes `&lt;`, and that IS a comparator. Counting raw bytes would refuse
        every structured artifact in the corpus — the very surfaces that are known good."""
        # Deliberately NOT through a whole XML document: `<article>` and `<p>` put literal
        # `<` and `>` into the raw markup, so a document-level fixture cannot tell an
        # entity-aware count from a byte count — it passes either way. Mutation-testing caught
        # exactly that: "absence counts raw bytes" escaped a document-level version of this
        # test. The function is probed directly so the assertion has nothing to hide behind.
        prose = ("Differences were significant by t test. The P value was small and the "
                 "standard deviation is reported for every cohort.")
        gate._refuse_suspect_surface(Path("paper.xml"), prose + " Threshold was P &lt; 0.05.")
        with self.assertRaises(ValueError) as caught:
            gate._refuse_suspect_surface(Path("paper.xml"), prose + " Threshold was small.")
        self.assertIn("ABSENCE", str(caught.exception))

    def test_day_two_is_not_chi_squared(self) -> None:
        """The real false positive, from PMID 26675548: `two days (D2), D5 and D7`.

        Calibrated against all 51 local PDFs before shipping: bare `\\bD2\\b` flags this
        legitimate timepoint label. The signature is anchored to statistical context instead.
        """
        message = self._screen(
            "derived.txt",
            "Lysates were collected two days (D2), D5 and D7 following transduction of the "
            "cells, and analysed by immunoblot against the loading control.")
        self.assertEqual(message, "", "a day-2 label must not be read as a chi-squared test")

    def test_every_artifact_branch_screens_raw_text_for_controls(self) -> None:
        """The XML branch was covered by accident, and accidents are not defences.

        ElementTree happens to reject C0 controls as not-well-formed, so the XML branch
        refused them without this check ever running. The day a parser becomes tolerant — or
        someone swaps in a lenient one — the defence would vanish and no test would notice.
        Every branch screens the raw decoded bytes, before any normalisation.
        """
        for name, payload in (
            ("paper.xml", "<article><body><p>Values (P \x1d 0.05) differed here.</p></body></article>"),
            ("paper.html", "<html><body><p>Values (P \x1d 0.05) differed here.</p></body></html>"),
            ("derived.txt", "Values (P \x1d 0.05) differed markedly here."),
        ):
            with self.subTest(artifact=name), TemporaryDirectory() as temporary:
                path = Path(temporary) / name
                path.write_text(payload, encoding="utf-8")
                with self.assertRaises(ValueError) as caught:
                    gate._artifact_text(path, "article_text")
                self.assertIn(
                    "SUSPECT", str(caught.exception),
                    f"{name} must be refused by the control screen, not by a parser accident",
                )

    def test_the_normaliser_never_treats_a_c0_control_as_whitespace(self) -> None:
        """A unit-level invariant, deliberately independent of the SUSPECT surface check.

        Mutation-testing showed the two defences overlap: with the surface check in place,
        reverting the normaliser to `str.split()` escaped every other test. Overlapping
        defences are fine; a defence that exists ONLY as a side effect of another is not,
        because the day the outer one is narrowed the inner one silently stops holding.
        """
        self.assertIn(
            "\x1d",
            gate._normalise_text("Values were significantly (P \x1d 0.023) lower."),
            "str.split() and \\s both consume C0 separators; the whitespace class must be "
            "explicit so the corruption survives to reach the SUSPECT check",
        )
        # `\f` and `\v` get their own assertions rather than riding on the one above. Putting
        # `\f` back into the whitespace class ESCAPED the entire suite until this line
        # existed: the SUSPECT surface check refuses the artifact first, so no end-to-end test
        # can ever observe what the normaliser did. Every layer needs one assertion naming it.
        self.assertIn(
            "\x0c", gate._normalise_text("triglyceride (TG), Ca2\x0c, inorganic phosphate"),
            "a form feed replaced the charge sign of Ca²⁺ in the real corpus; collapsing it "
            "to a space lets the stripped `Ca2` match strictly",
        )
        self.assertIn("\x0b", gate._normalise_text("a\x0bb"))
        self.assertEqual(
            gate._normalise_text("a   b\tc\nd"), "a b c d",
            "real presentation whitespace, including NBSP, must still collapse",
        )

    def test_strict_match_is_preferred_over_folding(self) -> None:
        """An intact quote carrying comparators verifies without ever reaching the fold."""
        sentence = "Upregulation exceeded > 1.5 fold (p < .05) across both replicates."
        matched, mode = gate._quote_matches(sentence, f"Context. {sentence} More context.")
        self.assertTrue(matched)
        self.assertEqual(mode, "strict")

    def test_strict_verification_refuses_fingerprint_mismatch(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = "files/fulltext/paper.xml"
            artifact = root / relative
            artifact.parent.mkdir(parents=True)
            artifact.write_text("<article><body><p>" + "a" * 80 + "</p></body></article>",
                                encoding="utf-8")
            errors, _ = gate.validate(schema_v2(relative), root=root, verify_artifacts=True)
            self.assertTrue(any("fingerprint mismatch" in error for error in errors))

    def test_html_abstract_container_is_not_body_evidence(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = "files/fulltext/paper.html"
            artifact = root / relative
            artifact.parent.mkdir(parents=True)
            quote = "This proposition appears only inside the HTML abstract container."
            artifact.write_text(
                f'<html><div class="article-abstract">{quote}</div>'
                '<main>The full article body says something else entirely.</main></html>',
                encoding="utf-8")
            manifest = schema_v2(relative)
            manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
                artifact.read_bytes()).hexdigest()
            manifest["verbatim_locators"]["entries"][0]["snippet"] = quote
            errors, _ = gate.validate(manifest, root=root, verify_artifacts=True)
            self.assertTrue(any("abstract but not the non-abstract body" in e for e in errors))

    def test_fabricated_abstract_snippet_is_refused(self) -> None:
        """An abstract anchor that is not in the abstract verifies nothing.

        Regression for a hole found on 2026-08-06 by mutation-testing a real reading (PMID
        19500159, a bronze-OA source with no PMC deposit). `abstract_snippet` is what keeps a
        locator verifiable when the source is not full-text indexed, yet nothing matched it
        against the abstract: any string discharged the duty. The same fabrication placed in
        `snippet` was caught, so the manifest certified the weaker field and not the stronger.
        """
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = "files/fulltext/paper.xml"
            artifact = root / relative
            artifact.parent.mkdir(parents=True)
            artifact.write_text(
                "<article><abstract><p>The abstract states one specific measured "
                "outcome.</p></abstract><body><p>A different body sentence also has "
                "enough characters to quote.</p></body></article>", encoding="utf-8")
            manifest = schema_v2(relative)
            manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
                artifact.read_bytes()).hexdigest()
            entry = manifest["verbatim_locators"]["entries"][0]
            entry["snippet"] = "A different body sentence also has enough characters to quote."
            entry["surface"] = "body"
            entry["abstract_snippet"] = "The abstract states an outcome it never mentions."
            errors, _ = gate.validate(manifest, root=root, verify_artifacts=True)
            self.assertTrue(any("abstract_snippet" in error for error in errors))

    def test_truthful_abstract_snippet_passes(self) -> None:
        """The guard must accept a real abstract quote, or it would only teach authors to drop the field."""
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = "files/fulltext/paper.xml"
            artifact = root / relative
            artifact.parent.mkdir(parents=True)
            artifact.write_text(
                "<article><abstract><p>The abstract states one specific measured "
                "outcome.</p></abstract><body><p>A different body sentence also has "
                "enough characters to quote.</p></body></article>", encoding="utf-8")
            manifest = schema_v2(relative)
            manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
                artifact.read_bytes()).hexdigest()
            entry = manifest["verbatim_locators"]["entries"][0]
            entry["snippet"] = "A different body sentence also has enough characters to quote."
            entry["surface"] = "body"
            entry["abstract_snippet"] = "The abstract states one specific measured outcome."
            errors, _ = gate.validate(manifest, root=root, verify_artifacts=True)
            self.assertFalse([error for error in errors if "abstract_snippet" in error])

    def test_malformed_xml_fails_closed_instead_of_merging_surfaces(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = "files/fulltext/paper.xml"
            artifact = root / relative
            artifact.parent.mkdir(parents=True)
            artifact.write_text("<article><abstract>" + "a" * 60, encoding="utf-8")
            manifest = schema_v2(relative)
            manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
                artifact.read_bytes()).hexdigest()
            errors, _ = gate.validate(manifest, root=root, verify_artifacts=True)
            self.assertTrue(any("cannot parse structured XML" in error for error in errors))


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
            "waived": False, "source_fulltext_indexed": True, "source_fulltext_indexed_evidence": "Europe PMC EXT_ID:1 on 2026-08-07: inEPMC=Y, PMCID PMC1 — fixture lookup",
            "entries": [{"proposition": "P", "snippet": "a" * 60, "surface": "body",
                         "anchor": "Results"}]}))
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
            "source_fulltext_indexed": True, "source_fulltext_indexed_evidence": "Europe PMC EXT_ID:1 on 2026-08-07: inEPMC=Y, PMCID PMC1 — fixture lookup",
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertEqual(errors, [])

    def test_abstract_only_source_needs_abstract_anchors_or_an_argument(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={
            "source_fulltext_indexed": False, "source_fulltext_indexed_evidence": "Europe PMC EXT_ID:1 on 2026-08-07: inEPMC=Y, PMCID PMC1 — fixture lookup",
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertTrue(any("not full-text indexed" in e for e in errors))

    def test_an_abstract_anchor_satisfies_it(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={
            "source_fulltext_indexed": False, "source_fulltext_indexed_evidence": "Europe PMC EXT_ID:1 on 2026-08-07: inEPMC=Y, PMCID PMC1 — fixture lookup",
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results",
                         "abstract_snippet": "the abstract says this"}]}))
        self.assertEqual(errors, [])

    def test_an_argued_waiver_also_satisfies_it(self) -> None:
        errors, _ = gate.validate(minimal(verbatim_locators={
            "source_fulltext_indexed": False, "source_fulltext_indexed_evidence": "Europe PMC EXT_ID:1 on 2026-08-07: inEPMC=Y, PMCID PMC1 — fixture lookup",
            "abstract_anchoring_waived": "the abstract reports only the headline association "
                                         "and states none of these propositions",
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertEqual(errors, [])

    def test_a_bare_boolean_index_state_is_refused(self) -> None:
        """The last honour-system field in the chain, closed 2026-08-07.

        `source_fulltext_indexed` gates a real duty — `false` obliges every locator to carry
        an abstract anchor or an argued waiver — and until now nothing accompanied it, so
        flipping it to `true` discharged that duty silently. It is not checked online: a
        validator that needs the network fails on a plane and, worse, fails *open* on a
        hiccup. It is made symmetric with `retraction_check` instead: a claim plus its
        evidence, reviewable in a diff.
        """
        manifest = minimal()
        del manifest["verbatim_locators"]["source_fulltext_indexed_evidence"]
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("source_fulltext_indexed_evidence" in e for e in errors))

    def test_the_duty_cannot_be_discharged_by_flipping_the_flag(self) -> None:
        """The attack the evidence field exists to price: `false` -> `true` and the
        abstract-anchoring obligation evaporates. It must now cost a dated, specific,
        checkable string rather than one character."""
        cheap = minimal(verbatim_locators={
            "source_fulltext_indexed": True,
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]})
        errors, _ = gate.validate(cheap)
        self.assertTrue(any("source_fulltext_indexed_evidence" in e for e in errors))

    def test_a_gesture_at_evidence_is_not_evidence(self) -> None:
        manifest = minimal()
        manifest["verbatim_locators"]["source_fulltext_indexed_evidence"] = "checked"
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("source_fulltext_indexed_evidence" in e for e in errors))

    def test_every_shipped_manifest_carries_its_index_evidence(self) -> None:
        """The back-fill window: on 2026-08-07 all eleven declarations were correct against
        Europe PMC, so the requirement shipped with zero grandfathering. This test is what
        keeps that true — the window closes the first time a manifest lands without it."""
        missing = []
        for path in sorted(MANIFESTS.glob("*.json")):
            locators = json.loads(path.read_text(encoding="utf-8")).get("verbatim_locators")
            if not isinstance(locators, dict) or "source_fulltext_indexed" not in locators:
                continue
            evidence = str(locators.get("source_fulltext_indexed_evidence", "")).strip()
            if len(evidence) < gate.MIN_WAIVER_CHARS:
                missing.append(path.name)
        self.assertEqual([], missing,
                         "manifests declaring the index state without evidence for it")

    def test_undeclared_index_state_is_a_visible_gap(self) -> None:
        """Not a block — the lookup needs the network — but never silence."""
        _errors, incomplete = gate.validate(minimal(verbatim_locators={
            "entries": [{"proposition": "P", "snippet": "a" * 60, "anchor": "Results"}]}))
        self.assertTrue(any("source_fulltext_indexed" in item for item in incomplete))


class CliVerdictNamesItsVerificationScope(unittest.TestCase):
    def test_default_success_does_not_imply_artifact_verification(self) -> None:
        scope = gate.verification_scope(
            verify_artifacts=False, require_current_schema=False)
        self.assertIn("STRUCTURE ONLY", scope)
        self.assertIn("NOT VERIFIED", scope)

    def test_strict_success_names_every_manifest_persistence_check(self) -> None:
        scope = gate.verification_scope(
            verify_artifacts=True, require_current_schema=True)
        self.assertIn("MANIFEST STRICT", scope)
        self.assertIn("SHA-256", scope)
        self.assertIn("exact text locators verified", scope)


class PanelTextRelationBites(unittest.TestCase):
    """Every refusal added for `panel_text_relation`, and a baseline that proves it can pass.

    A mutation battery rather than a parity check: a red baseline is not a capture. Each test
    below starts from a manifest that validates, changes exactly one thing, and asserts the
    specific refusal — so a check that silently stopped firing would show up here as a pass
    that should have been a failure.
    """

    @staticmethod
    def _two_entries(**entry_overrides) -> dict:
        """A text locator at entries[0] and a panel locator at entries[1]."""
        manifest = schema_v2()
        text_entry = manifest["verbatim_locators"]["entries"][0]
        text_entry["panel_text_relation"] = "text_only"
        panel = {
            "proposition": "The panel shows the comparison was never drawn",
            "snippet": "[figure attestation] Fig. 3b, brackets run WT-vs-KO only",
            "surface": "figure",
            "anchor": "Figure 3b, read at 500 dpi",
            "artifact": manifest["source_artifacts"][0]["path"],
            "panel_text_relation": "text_contradicted_by_panel",
            "contradicts": "entries[0]",
        }
        panel.update(entry_overrides)
        manifest["verbatim_locators"]["entries"].append(panel)
        return manifest

    def test_the_baseline_passes(self) -> None:
        """Without this, every assertion below could be passing for the wrong reason."""
        errors, _ = gate.validate(self._two_entries(), require_current_schema=True)
        self.assertEqual([item for item in errors if "panel_text_relation" in item
                          or "contradicts" in item], [])

    def test_the_field_is_optional_so_the_legacy_corpus_stays_valid(self) -> None:
        """The coverage duty lives in growth_anchors, not here — see §6.4."""
        manifest = schema_v2()
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertEqual([item for item in errors if "panel_text_relation" in item], [])

    def test_a_value_outside_the_enum_is_refused(self) -> None:
        manifest = schema_v2()
        manifest["verbatim_locators"]["entries"][0]["panel_text_relation"] = "probably_fine"
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("panel_text_relation: must be one of" in item for item in errors))

    def test_every_declared_value_is_actually_accepted(self) -> None:
        """The enum and the validator must not drift apart in either direction."""
        for value in sorted(gate.PANEL_TEXT_RELATIONS - {"text_contradicted_by_panel"}):
            with self.subTest(value=value):
                manifest = schema_v2()
                manifest["verbatim_locators"]["entries"][0]["panel_text_relation"] = value
                errors, _ = gate.validate(manifest, require_current_schema=True)
                self.assertEqual(
                    [item for item in errors if "panel_text_relation" in item], [])

    def test_a_contradiction_without_a_pointer_is_a_block(self) -> None:
        manifest = self._two_entries()
        del manifest["verbatim_locators"]["entries"][1]["contradicts"]
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("must name it as `entries[N]`" in item for item in errors))

    def test_a_pointer_to_a_locator_that_does_not_exist_is_a_block(self) -> None:
        manifest = self._two_entries(contradicts="entries[9]")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("no entries[9] in this manifest" in item for item in errors))

    def test_a_locator_cannot_contradict_itself(self) -> None:
        manifest = self._two_entries(contradicts="entries[1]")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("cannot contradict itself" in item for item in errors))

    def test_a_panel_cannot_contradict_another_panel(self) -> None:
        """Two images disagreeing is a different finding and needs its own words."""
        manifest = self._two_entries()
        manifest["verbatim_locators"]["entries"][0]["surface"] = "figure"
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("is not a text surface" in item for item in errors))

    def test_only_a_contradiction_may_carry_the_pointer(self) -> None:
        """Otherwise `contradicts` becomes a free-text field nothing reads."""
        manifest = self._two_entries(panel_text_relation="text_confirmed_by_panel")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any(
            "only `text_contradicted_by_panel` may name a contradicted locator" in item
            for item in errors))

    def test_the_pointer_grammar_matches_the_adjudication_recipes(self) -> None:
        """Zero-based, as `adjudications.json` writes it — the reference this repo already has.

        The error messages in the validator count from one. A reader copies the reference
        grammar, not the diagnostic text, so `contradicts` follows the recipes; this test is
        what keeps the two from being reconciled in the wrong direction by a later edit.
        """
        manifest = self._two_entries(contradicts="entries[0]")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertEqual([item for item in errors if "contradicts" in item], [])


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
