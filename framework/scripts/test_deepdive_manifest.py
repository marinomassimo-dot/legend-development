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
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("deepdive_manifest", HERE / "deepdive_manifest.py")
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)

ROOT = HERE.parents[1]
MANIFESTS = ROOT / "disease-models/wwox/research/deepdive_manifests"


def dependencies_block(**overrides) -> dict:
    """A valid `retraction_check.dependencies` block, the shape `screen --manifest-block` emits."""
    block = {
        "schema": "retraction_check.dependencies/1",
        "tool": "framework/scripts/dependency_integrity.py screen --manifest-block",
        "paper_verdict": "SCREENED_CLEAN", "screened": True,
        "references_declared": 28, "references_with_doi": 26, "references_screened": 26,
        "unscreenable": {"UNSCREENABLE_NO_DOI": 2},
        "flagged": [], "noted": [], "reference_source": "cache",
        "snapshot": {"date": "2026-09-10", "sha256": "8" * 64, "rows": 72476,
                     "days_since_fetch": 0},
    }
    block.update(overrides)
    return block


def flagged_entry(**overrides) -> dict:
    entry = {
        "doi": "10.1073/pnas.0505485102", "verdict": "FLAGGED_EXPRESSION_OF_CONCERN",
        "nature": "Expression of concern", "retraction_pmid": "28373548",
        "retraction_date": "4/3/2017 0:00",
        "reason_verbatim": "Concerns/Issues about Data;Duplication of/in Image;",
        "citing_relation": "reagent source: this paper's adenovirus and both antibodies "
                           "come from the flagged paper",
    }
    entry.update(overrides)
    return entry


def acquisition_recipe(**overrides) -> dict:
    """A valid fetch recipe — the efetch route that replayed byte-identical on 2026-09-10."""
    recipe = {
        "resolved_url": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=2832309",
        "http_method": "GET", "tier": "ncbi_efetch_pmc_xml", "user_agent_policy": "none",
        "acquired_on": "2026-09-09", "derived": False,
    }
    recipe.update(overrides)
    return recipe


def derived_recipe(**overrides) -> dict:
    recipe = {
        "derived": True, "derived_from": "files/fulltext/paper.pdf",
        "extractor": {"name": "PyMuPDF", "version": "1.26.5",
                      "call": "page.get_text() default mode", "join": ""},
        "acquired_on": "2026-09-09",
    }
    recipe.update(overrides)
    return recipe


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
        "retraction_check": {"result": "no retraction notice found",
                             "dependencies": dependencies_block()},
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
        "acquisition_recipe": acquisition_recipe(),
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

    def test_manifest_and_artifacts_may_use_separate_explicit_workspaces(self) -> None:
        """A branch carries the manifest while ignored evidence remains in shared files/."""
        with TemporaryDirectory() as manifest_tmp, TemporaryDirectory() as evidence_tmp:
            manifest_root = Path(manifest_tmp)
            evidence_root = Path(evidence_tmp)
            relative = "files/fulltext/paper.xml"
            artifact = evidence_root / relative
            artifact.parent.mkdir(parents=True)
            sentence = "This body sentence is long enough to act as exact evidentiary text."
            artifact.write_text(
                f"<article><body><p>{sentence}</p></body></article>", encoding="utf-8")
            manifest = schema_v2(relative)
            manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
                artifact.read_bytes()).hexdigest()
            manifest["verbatim_locators"]["entries"][0]["snippet"] = sentence
            work = gate.manifest_path(manifest_root, "wwox", "12345678")
            work.parent.mkdir(parents=True)
            work.write_text(json.dumps(manifest), encoding="utf-8")

            errors, incomplete = gate.load_and_validate(
                manifest_root, "wwox", "12345678", artifact_root=evidence_root,
                verify_artifacts=True, require_current_schema=True)
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

    def test_the_elsevier_substitution_table_is_caught_after_a_repair(self) -> None:
        """🔴 A substitution table belongs to the PRODUCER, not to the corpus.

        Measured on PMID 18674750 against its own clean PMC HTML: the Elsevier/LiveCycle text
        layer holds 74 U+0002 and 5 U+0003, and the HTML holds exactly 74 `-` (minus) and
        exactly 5 `°` — a one-to-one count match that identifies the substitution rather
        than inferring it. On top of the controls sit PRINTABLE substitutions: `¼` for `=`
        (65 occurrences) and the DIGIT 3 for `×` (12, in `× 10` constructions).

        The gap this closes was measured, not supposed. As extracted the surface is refused by
        the C0 check. With the controls stripped — exactly what a well-meaning repair does —
        it was ACCEPTED while every printable substitution survived, and suspicion-by-absence
        could not catch it either, because the text still carried 5 `<` and 9 `>` from
        "p < 0.05". Note also that `×` is substituted as `t` by the extractor behind the
        rule above and as `3` by this one: the same glyph, two producers, two signatures.
        """
        for label, payload in (
            ("equals as one-quarter", "The overall combined analysis provided p ¼ 6.9 3 10 7 for this SNP."),
            ("times as digit three", "Association reached 6.9 3 10 7 in the combined sample of families."),
        ):
            with self.subTest(substitution=label):
                message = self._screen("derived.txt", payload)
                self.assertIn("SUSPECT", message, f"{label} must refuse the surface")

    def test_the_genotype_sign_substitution_is_caught_and_survives_a_repair(self) -> None:
        """🔴 A surface can be refused twice and for neither the right reason.

        Measured on PMID 25245215 (Aqeilan 2014, CMLS). Its PDF text layer renders
        `Wwox +/-` as `Wwox?/-`, `Wwox +/+` as `Wwox?/?`, and once `Wwox +/- mice` as
        `Wwox?/mice` with the minus dropped outright. Four extractor modes agree on the
        literal '?' -- pdftotext default, -layout and -raw, and pdftohtml -- which is rule
        5d's own point that cross-checking extractors detects nothing.

        The gap this closes was measured by counterfactual, not supposed. As extracted the
        surface is refused by the C0 check (8 U+0001, all harmless front-matter separators).
        Strip those -- exactly what a well-meaning repair does -- and it is still refused, by
        suspicion-by-absence. Strip those AND reword the statistical language below threshold
        and the screen returned ACCEPTED with every corrupted genotype intact. Both states are
        ordinary for other papers, and the surface that survives them is one in which
        wild-type and heterozygote are typographically indistinguishable.
        """
        for label, payload in (
            ("het against wild-type", "Tumor formation in Wwox?/- mice was higher than in wild-type (Wwox?/?) mice."),
            ("minus dropped entirely", "Increased tumor multiplicity in Wwox?/mice was observed relative to controls."),
        ):
            with self.subTest(substitution=label):
                message = self._screen("derived.txt", payload)
                self.assertIn("SUSPECT", message, f"{label} must refuse the surface")

    def test_the_genotype_pattern_does_not_fire_on_ordinary_prose(self) -> None:
        """The other half of the upgrade: a pattern that refuses good surfaces is a defect.

        Calibrated over all 45 local text-bearing artifacts in files/fulltext/ before
        shipping: nine hits, all nine in the one defective PDF, zero in the other 44. The
        cases below are the shapes that could plausibly collide -- a question mark ending a
        sentence before a slashed pair, a real genotype correctly rendered, and an ordinary
        and/or construction.
        """
        for label, payload in (
            ("question then slashed pair", "Which allele is lost? /Wwox/ transcripts were then measured in each tumor."),
            ("correct genotype notation", "Tumor formation in Wwox+/- mice was higher than in wild-type (Wwox+/+) mice."),
            ("ordinary slashed words", "Samples were scored as positive/negative by two readers, blinded to genotype."),
        ):
            with self.subTest(prose=label):
                message = self._screen("derived.txt", payload)
                self.assertNotIn("welded", message, f"{label} must survive the screen")

    def test_the_elsevier_patterns_do_not_fire_on_ordinary_prose(self) -> None:
        """The other half of the upgrade: a new pattern that refuses good surfaces is a defect.

        A genuine fraction attached to a number, and an ordinary sentence in which 3 and 10 are
        just numbers with words between them, must both survive.
        """
        for label, payload in (
            ("genuine fraction", "Cells were seeded at 1¼ times the density used previously, p < 0.05."),
            ("digits that are not an operator", "We analysed 3 of the 10 cohorts, and 3 more were excluded."),
        ):
            with self.subTest(payload=label):
                self.assertEqual(
                    self._screen("derived.txt", payload), "",
                    f"{label} must NOT be refused",
                )

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
            "contradicts_needle": "amino acids 388-407",
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
            "contradicts: only a `text_contradicted_by_panel` locator may carry one" in item
            for item in errors))

    def test_the_diagnostic_index_is_zero_based_like_the_pointer(self) -> None:
        """🔴 One error line used to carry two `entries[N]` with opposite meanings.

        The loop counted from ONE while `contradicts` and `adjudications.json` count from
        zero — the notation collision inside the message whose job is to disambiguate. It cost
        twice on 2026-08-10: five needles across three branches would each have been attached
        to the wrong locator by anyone trusting the printed index, and a reader sent to
        `entries[1].abstract_snippet` found no such field because the defect was in entry 0.
        """
        manifest = self._two_entries()
        del manifest["verbatim_locators"]["entries"][1]["anchor"]
        errors, _ = gate.validate(manifest, require_current_schema=True)
        anchor_errors = [item for item in errors if ".anchor:" in item]
        self.assertEqual(len(anchor_errors), 1, errors)
        self.assertIn("entries[1].anchor", anchor_errors[0])

    def test_the_pointer_and_the_diagnostic_agree_on_the_same_entry(self) -> None:
        """The property that makes the two indices interchangeable for a reader."""
        manifest = self._two_entries(contradicts_needle="not in the target at all")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        needle_errors = [item for item in errors if "contradicts_needle" in item]
        self.assertEqual(len(needle_errors), 1, errors)
        # The panel locator is at index 1 and names entries[0]; both appear as written.
        self.assertIn("entries[1].contradicts_needle", needle_errors[0])
        self.assertIn("entries[0]", needle_errors[0])

    @staticmethod
    def _qualifying_pair(**entry_overrides) -> dict:
        """The same fixture for the second coupled relation, so both are exercised alike."""
        manifest = schema_v2()
        manifest["verbatim_locators"]["entries"][0]["panel_text_relation"] = "text_only"
        panel = {
            "proposition": "The panel bears on the sentence and neither agrees nor disagrees",
            "snippet": "[figure attestation] Fig. 3b carries a lane the sentence never cites",
            "surface": "figure",
            "anchor": "Figure 3b, read at 500 dpi",
            "artifact": manifest["source_artifacts"][0]["path"],
            "panel_text_relation": "panel_qualifies_text",
            "qualifies": "entries[0]",
            "qualifies_needle": "amino acids 388-407",
        }
        panel.update(entry_overrides)
        manifest["verbatim_locators"]["entries"].append(panel)
        return manifest

    def test_the_qualifying_baseline_passes(self) -> None:
        """🔴 A red baseline is not a capture — every refusal below needs this to be green."""
        errors, _ = gate.validate(self._qualifying_pair(), require_current_schema=True)
        self.assertEqual([item for item in errors if "qualif" in item], [], errors)

    def test_a_qualification_without_a_pointer_is_a_block(self) -> None:
        manifest = self._qualifying_pair()
        del manifest["verbatim_locators"]["entries"][1]["qualifies"]
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("must name it as `entries[N]`" in item for item in errors), errors)

    def test_a_qualification_without_a_needle_is_a_block(self) -> None:
        """The pointer is an index into a reorderable array; the needle is what pins it."""
        manifest = self._qualifying_pair()
        del manifest["verbatim_locators"]["entries"][1]["qualifies_needle"]
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("qualifies_needle:" in item for item in errors), errors)

    def test_a_qualifying_needle_from_the_wrong_sentence_is_a_block(self) -> None:
        manifest = self._qualifying_pair(qualifies_needle="a span in no snippet at all")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("is not a fragment of the snippet" in item for item in errors),
                        errors)

    def test_a_panel_cannot_qualify_another_panel(self) -> None:
        manifest = self._qualifying_pair()
        manifest["verbatim_locators"]["entries"][0]["surface"] = "figure"
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("is not a text surface" in item for item in errors), errors)

    def test_a_locator_cannot_qualify_itself(self) -> None:
        manifest = self._qualifying_pair(qualifies="entries[1]")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("cannot qualify itself" in item for item in errors), errors)

    def test_a_contradiction_may_not_carry_a_qualification_pointer(self) -> None:
        """Both directions, because one-way checks are how a pair drifts apart."""
        manifest = self._two_entries(qualifies="entries[0]")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any(
            "qualifies: only a `panel_qualifies_text` locator may carry one" in item
            for item in errors), errors)

    def test_a_qualification_may_not_carry_a_contradiction_pointer(self) -> None:
        """The pointers are not interchangeable: each names the relation that owns it."""
        manifest = self._two_entries(panel_text_relation="panel_qualifies_text")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any(
            "contradicts: only a `text_contradicted_by_panel` locator may carry one" in item
            for item in errors), errors)

    def test_the_pointer_grammar_matches_the_adjudication_recipes(self) -> None:
        """Zero-based, as `adjudications.json` writes it — the reference this repo already has.

        The error messages in the validator count from one. A reader copies the reference
        grammar, not the diagnostic text, so `contradicts` follows the recipes; this test is
        what keeps the two from being reconciled in the wrong direction by a later edit.
        """
        manifest = self._two_entries(contradicts="entries[0]")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertEqual([item for item in errors if "contradicts" in item], [])

    def test_a_contradiction_must_address_its_target_by_content_too(self) -> None:
        """🔴 `entries[N]` is a position in a reorderable array; the index can slip.

        Caught in review before the field had a second user. The three checks around the
        pointer — target exists, is a text surface, is not this one — are all blind to a slip
        onto a DIFFERENT text locator. `adjudications.json` never writes `entries[N]` alone;
        the half that makes the address safe had not been copied over with the half that
        makes it an address.
        """
        manifest = self._two_entries()
        del manifest["verbatim_locators"]["entries"][1]["contradicts_needle"]
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("must be accompanied by a fragment" in item for item in errors))

    def test_a_fragment_from_the_wrong_sentence_is_refused(self) -> None:
        manifest = self._two_entries(contradicts_needle="a phrase from nowhere")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("is not a fragment of the snippet of entries[0]" in item
                            for item in errors))

    def test_a_slipped_index_is_caught_by_the_fragment(self) -> None:
        """The failure the needle exists for, staged end to end.

        A third locator is inserted ahead of the target, exactly as a later reading would add
        one. `contradicts: entries[0]` now resolves to the new sentence; every structural
        check still passes, and only the content anchor notices.
        """
        manifest = self._two_entries()
        entries = manifest["verbatim_locators"]["entries"]
        intruder = dict(entries[0])
        intruder["snippet"] = ("A different sentence entirely, long enough to satisfy the "
                               "minimum snippet length imposed by the schema.")
        entries.insert(0, intruder)
        structural = [item for item in gate.validate(manifest, require_current_schema=True)[0]
                      if "contradicts:" in item]
        self.assertEqual([], structural, "the positional checks cannot see a slip")
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("contradicts_needle" in item for item in errors),
                        "only the content anchor catches it")

    def test_a_fragment_matching_two_locators_does_not_identify_one(self) -> None:
        """Uniqueness is the other half of `check_needles`, in this array's terms."""
        manifest = self._two_entries()
        entries = manifest["verbatim_locators"]["entries"]
        twin = dict(entries[0])
        twin["snippet"] = entries[0]["snippet"] + " Repeated: amino acids 388-407 again."
        entries.append(twin)
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any("does not identify one" in item for item in errors))

    def test_only_a_contradiction_may_carry_a_fragment(self) -> None:
        manifest = self._two_entries(panel_text_relation="text_only")
        del manifest["verbatim_locators"]["entries"][1]["contradicts"]
        errors, _ = gate.validate(manifest, require_current_schema=True)
        self.assertTrue(any(
            "only a `text_contradicted_by_panel` locator may carry one" in item
            for item in errors))


class AFileCanBeWellFormedAndDeclareTheFalse(unittest.TestCase):
    """🔴 Rule 5d proved at the level of the font rather than the text.

    `PMID 16061658` extracts `p73β` as `p73h` and `µg` as `Ag`, and every extractor agrees,
    because the file is not corrupt — it is well formed and states something false. Its fonts
    are embedded subsets declaring `WinAnsiEncoding` with no `ToUnicode` CMap, so an extractor
    obeying the declaration yields the Latin-1 letter that shares each glyph slot. Comparing
    extractors detects nothing: they are all obeying the same lie.

    Measured over the 55 local PDFs on 2026-08-11: **11 declare no `ToUnicode` anywhere**, and
    9 of those the existing text screen already refuses. The two it adds — `27308504` and
    `38355659` — are the valuable ones, because the text screen calls them clean.
    """

    def setUp(self) -> None:
        try:
            import fitz  # noqa: F401,PLC0415
        except ImportError:  # pragma: no cover - environment without PyMuPDF
            self.skipTest("PyMuPDF unavailable")
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def _pdf(self, name: str, *, embedded: bool) -> Path:
        import fitz  # noqa: PLC0415

        path = self.root / name
        document = fitz.open()
        page = document.new_page()
        if embedded:
            page.insert_text((72, 72), "P < 0.05",
                             fontfile="/System/Library/Fonts/Supplemental/Arial.ttf",
                             fontname="ari")
        else:
            page.insert_text((72, 72), "P < 0.05", fontname="helv")
        document.save(path)
        document.close()
        return path

    def test_a_pdf_with_no_tounicode_anywhere_is_untrustworthy(self) -> None:
        verdict, detail = gate.font_encoding_verdict(self._pdf("bare.pdf", embedded=False))
        self.assertEqual(verdict, "UNTRUSTWORTHY")
        self.assertIn("ToUnicode", detail)

    def test_font_screen_cli_accepts_a_pdf_file_without_reporting_zero_pdfs(self) -> None:
        """A file target used to fall through ``Path.glob`` and print a false 0-PDF pass."""
        path = self._pdf("single.pdf", embedded=False)
        completed = subprocess.run(
            [sys.executable, str(Path(gate.__file__)), "--font-screen", str(path)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("matched and screened 1 PDF(s) of 1 regular file(s)", completed.stdout)
        self.assertIn("complement: 0 non-PDF file(s)", completed.stdout)

    def test_font_screen_uses_the_same_case_insensitive_pdf_predicate_for_a_directory(self) -> None:
        """A deposited `.PDF` must not disappear only because the target is a directory."""
        self._pdf("lower.pdf", embedded=False)
        self._pdf("upper.PDF", embedded=False)
        completed = subprocess.run(
            [sys.executable, str(Path(gate.__file__)), "--font-screen", str(self.root)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("matched and screened 2 PDF(s) of 2 regular file(s)", completed.stdout)
        self.assertIn("complement: 0 non-PDF file(s)", completed.stdout)

    def test_font_screen_directory_reports_the_non_pdf_complement(self) -> None:
        self._pdf("paper.PDF", embedded=False)
        (self.root / "readme.txt").write_text("not a PDF", encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(Path(gate.__file__)), "--font-screen", str(self.root)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("matched and screened 1 PDF(s) of 2 regular file(s)", completed.stdout)
        self.assertIn("complement: 1 non-PDF file(s)", completed.stdout)

    def test_font_screen_cli_refuses_an_empty_directory(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(Path(gate.__file__)), "--font-screen", str(self.root)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 2, completed.stdout + completed.stderr)
        self.assertIn("contains no PDF files", completed.stderr)

    def test_having_a_tounicode_is_never_a_clearance(self) -> None:
        """🔴 The limit that keeps this from becoming the inverse defect — a guard that CLEARS
        incorrect practice. 26 of the 55 local PDFs carry a CMap and still fail the text
        screen, so a present CMap answers nothing."""
        try:
            path = self._pdf("embedded.pdf", embedded=True)
        except Exception:  # pragma: no cover - no system font to embed
            self.skipTest("no embeddable system font available")
        verdict, detail = gate.font_encoding_verdict(path)
        self.assertEqual(verdict, "UNDECIDED")
        self.assertIn("NOT a clearance", detail)

    def test_a_structured_surface_abstains_rather_than_passing(self) -> None:
        """XML and HTML have no fonts, so the question is meaningless — and the difference
        between 'not applicable' and 'clean' is the difference between a metadata-only stub
        and a real paper."""
        for name in ("paper.xml", "paper.html", "notes.txt"):
            with self.subTest(name=name):
                verdict, _ = gate.font_encoding_verdict(self.root / name)
                self.assertEqual(verdict, "NOT_APPLICABLE")

    def test_an_unreadable_pdf_is_undecided_and_not_clean(self) -> None:
        """Fail-open here would be worse than useless: it would report a verdict on a file
        nobody inspected."""
        broken = self.root / "broken.pdf"
        broken.write_bytes(b"not a pdf at all")
        verdict, _ = gate.font_encoding_verdict(broken)
        self.assertEqual(verdict, "UNDECIDED")

    def _workspace(self, *, with_derived_text: bool) -> tuple[Path, dict]:
        """A manifest declaring an untrustworthy PDF, with or without a derived `.txt`."""
        workspace = self.root / ("with_txt" if with_derived_text else "xml_only")
        fulltext = workspace / "files" / "fulltext"
        fulltext.mkdir(parents=True)
        pdf = self._pdf("scratch.pdf", embedded=False)
        (fulltext / "paper.pdf").write_bytes(pdf.read_bytes())
        artifacts = [{
            "path": "files/fulltext/paper.pdf",
            "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            "kind": "article_binary",
        }]
        quote = ("This indicates that WWOX amino acids 388-407 are required for its "
                 "interaction with GSK3b.")
        name = "paper.txt" if with_derived_text else "paper.xml"
        body = quote if with_derived_text else f"<article><body><p>{quote}</p></body></article>"
        (fulltext / name).write_text(body, encoding="utf-8")
        artifacts.append({
            "path": f"files/fulltext/{name}",
            "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
            "kind": "article_text",
        })
        manifest = schema_v2(artifact_path=f"files/fulltext/{name}")
        manifest["source_artifacts"] = artifacts
        return workspace, manifest

    def test_a_derived_text_surface_beside_an_untrustworthy_pdf_is_refused(self) -> None:
        """🔴 The narrow case where the false declaration can actually carry a quote."""
        workspace, manifest = self._workspace(with_derived_text=True)
        errors, _ = gate.validate(manifest, root=workspace, verify_artifacts=True,
                                  require_current_schema=True)
        self.assertTrue(any("ToUnicode" in item for item in errors), errors)

    def test_the_same_pdf_beside_a_structured_surface_does_not_block(self) -> None:
        """🔴 And the case that must NOT block, which is why the check is scoped this way.

        `PMID27308504` declares exactly such a PDF as `article_binary` next to a PMC XML, and
        its complete read is anchored to the XML — rule 5d already routed around the file.
        Refusing there would punish the correct practice, which is the failure mode this
        repository catalogued four times on 2026-08-11.
        """
        workspace, manifest = self._workspace(with_derived_text=False)
        errors, _ = gate.validate(manifest, root=workspace, verify_artifacts=True,
                                  require_current_schema=True)
        self.assertFalse([item for item in errors if "ToUnicode" in item], errors)

    def test_no_input_ever_produces_a_passing_verdict(self) -> None:
        """The vocabulary carries the negative-test design: there is no value meaning "this
        file is fine", because one would be read as a clearance whatever the docstring said.

        🔴 Pinned on returned VALUES, not on the source text. The first version grepped the
        module for `"CLEAN"` and failed on the sentence in the docstring saying that no such
        verdict exists — a predicate that cannot tell a value from a sentence about the value,
        which is the third instance of that shape found in this repository on 2026-08-11
        alone.
        """
        broken = self.root / "broken.pdf"
        broken.write_bytes(b"not a pdf at all")
        inputs = [self._pdf("bare2.pdf", embedded=False), broken,
                  self.root / "paper.xml", self.root / "missing.pdf"]
        verdicts = {gate.font_encoding_verdict(path)[0] for path in inputs}
        self.assertTrue(verdicts)
        self.assertLessEqual(
            verdicts,
            {"UNTRUSTWORTHY", "SUSPECT_FONTS", "UNDECIDED", "NOT_APPLICABLE"})

    def test_the_symbol_font_names_that_actually_carry_the_defect_are_matched(self) -> None:
        """🔴 The per-file question was the wrong one, and this is the predicate that replaced
        it.

        Asking *does this file have at least one mapped font* passes 10 of the 55 local PDFs
        whose running text is mapped and whose SYMBOL subsets are not — and those subsets are
        where `α β × ± µ Δ` live. The names below are the real ones observed in this corpus,
        written out rather than derived from the pattern, so the pattern is checked against
        the world instead of against itself.
        """
        carriers = ["GIJFJH+MathematicalPi-One", "IAAMID+Universal-GreekwithMathPi",
                    "ILLLOP+AdvGreek_B", "OCBFJF+AdvItcSymbol-M", "DIPGNL+Symbol",
                    "MPUDFL+PazoMath", "SymbolStd-Identity-H"]
        for name in carriers:
            with self.subTest(name=name):
                self.assertTrue(gate.font_is_symbolic(name))
        # 🔴 `POTJPI+TimesNewRomanPS-ItalicMT` is an ordinary italic serif whose arbitrary
        # six-letter SUBSET TAG happens to end in `PI`, and `(?i)Pi\b` matched it because the
        # `+` is a word boundary. Found by this hand-written list of real names; a list
        # generated from the pattern would have agreed with the bug.
        for ordinary in ["POTJPI+TimesNewRomanPS-ItalicMT", "AdvTT3713a231",
                         "WarnockPro-It", "ABCDEF+Helvetica", "MATHXX+Garamond"]:
            with self.subTest(name=ordinary):
                self.assertFalse(gate.font_is_symbolic(ordinary))

    def test_an_unmapped_symbol_font_alone_is_not_enough_to_refuse(self) -> None:
        """🔴 Necessary, never sufficient — the limit that keeps this a triage signal.

        6 of the 10 files with an unmapped symbol font extract sentinel characters perfectly
        well: `17803050` (SymbolStd, 2 sentinels), `33916893` (PazoMath, 22), `25012504` (34).
        A font can be unmapped and never used for anything that matters. Refusing on the font
        alone would flag six healthy files, which is the shape of a guard that punishes the
        practice it exists to protect.
        """
        workspace, manifest = self._workspace(with_derived_text=True)
        original = gate.font_encoding_verdict
        gate.font_encoding_verdict = lambda path: (
            "SUSPECT_FONTS", f"{path.name}: symbol fonts unmapped, sentinels still present")
        try:
            errors, _ = gate.validate(manifest, root=workspace, verify_artifacts=True,
                                      require_current_schema=True)
        finally:
            gate.font_encoding_verdict = original
        self.assertFalse([item for item in errors if "symbol fonts unmapped" in item], errors)


def pptx_part(*paragraphs: list[str]) -> bytes:
    """A minimal DrawingML part. Each paragraph is a list of RUNS, as PowerPoint stores it."""
    body = ""
    for runs in paragraphs:
        cells = "".join(f"<a:r><a:t>{run}</a:t></a:r>" for run in runs)
        body += f"<a:p>{cells}</a:p>"
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        f"<p:cSld><p:spTree><p:sp><p:txBody>{body}</p:txBody></p:sp></p:spTree></p:cSld>"
        "</p:sld>"
    ).encode("utf-8")


def write_pptx(path: Path, parts: dict[str, bytes]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("[Content_Types].xml", "<Types/>")
        for name, payload in parts.items():
            archive.writestr(name, payload)
    return path


class ABinarySupplementCanBeDeclared(unittest.TestCase):
    """§ 6.3 H4 / census P3: a `.pptx` supplement was declarable by nothing.

    `supplement_text` was the only supplement kind, and its own text verification refuses a
    `.pptx`. So four deposited files sat on disk outside every manifest, and the single most
    consequential sentence of the PMID 38499540 reading — the authors' note that the t-tests
    were computed over microscopy FIELDS and not per MOUSE — lived in a speaker-notes pane,
    in the dossier and in no machine-verified locator.
    """

    NOTE = "all the t-tests were done over all the fields and not over each mouse"

    def _deck(self, parts: dict[str, bytes]) -> tuple[Path, Path]:
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        return root, write_pptx(root / "files/supplement/deck.pptx", parts)

    def _manifest(self, root: Path, deck: Path, snippet: str) -> dict:
        relative = "files/supplement/deck.pptx"
        manifest = schema_v2(relative)
        manifest["source_artifacts"][0]["kind"] = "supplement_binary"
        manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
            deck.read_bytes()).hexdigest()
        entry = manifest["verbatim_locators"]["entries"][0]
        entry["surface"] = "supplement"
        entry["snippet"] = snippet
        entry["anchor"] = "Supplementary deck, slide 1 speaker notes"
        return manifest

    def test_supplement_binary_is_an_accepted_kind(self) -> None:
        self.assertIn("supplement_binary", gate.ARTIFACT_KINDS)

    def test_a_locator_verifies_against_slide_text(self) -> None:
        sentence = "Scale bars represent twenty micrometres in every panel shown here."
        root, deck = self._deck({"ppt/slides/slide1.xml": pptx_part([sentence])})
        errors, _ = gate.validate(self._manifest(root, deck, sentence), root=root,
                                  verify_artifacts=True, require_current_schema=True)
        self.assertEqual(errors, [])

    def test_a_locator_verifies_against_the_speaker_notes_pane(self) -> None:
        """🔴 The whole reason this exists. Slides alone would have missed the sentence."""
        root, deck = self._deck({
            "ppt/slides/slide1.xml": pptx_part(["Figure S2"]),
            "ppt/notesSlides/notesSlide1.xml": pptx_part([self.NOTE]),
        })
        errors, _ = gate.validate(self._manifest(root, deck, self.NOTE), root=root,
                                  verify_artifacts=True, require_current_schema=True)
        self.assertEqual(errors, [])

    def test_runs_inside_a_paragraph_are_joined_without_a_fabricated_space(self) -> None:
        """PowerPoint splits a word across runs at a formatting or script boundary.

        🔴 Measured on the real deposit: the notes pane carries `ה` and `ttest` as separate
        runs, so a space-joining extractor writes `ה ttest` — a space the author never typed,
        in the single most consequential sentence of that reading. A quote re-captured from
        that output would carry the fabrication and verify against it.
        """
        text = gate._pptx_part_text(pptx_part(["WWO", "X", "-DEE"]))
        self.assertEqual(text, "WWOX-DEE")

    def test_paragraphs_are_separated_and_parts_ordered_deterministically(self) -> None:
        root, deck = self._deck({
            "ppt/slides/slide1.xml": pptx_part(["first slide"]),
            "ppt/notesSlides/notesSlide1.xml": pptx_part(["note on one"]),
            "ppt/slides/slide2.xml": pptx_part(["second slide"]),
            "ppt/slides/slide10.xml": pptx_part(["tenth slide"]),
        })
        body, abstract = gate._artifact_text(deck, "supplement_binary")
        self.assertEqual(abstract, "")
        self.assertEqual(body.split("\n"),
                         ["first slide", "note on one", "second slide", "tenth slide"])

    def test_the_suspect_surface_screen_runs_on_the_deck_too(self) -> None:
        """Rule 5c: same screen, same order — raw decoded bytes, before any parser."""
        _root, deck = self._deck({
            "ppt/slides/slide1.xml": pptx_part(["The value was (P \x1d 0.023) in that run."])})
        with self.assertRaises(gate.SuspectSurface) as caught:
            gate._artifact_text(deck, "supplement_binary")
        self.assertEqual(caught.exception.verdict.signature, gate.SIGNATURE_C0_CONTROL)

    def test_a_zip_that_is_not_a_deck_says_so(self) -> None:
        _root, deck = self._deck({"docProps/app.xml": b"<Properties/>"})
        with self.assertRaises(ValueError) as caught:
            gate._artifact_text(deck, "supplement_binary")
        self.assertIn("no slide or notes part", str(caught.exception))

    def test_an_unreadable_suffix_under_this_kind_is_an_error_not_an_empty_surface(self) -> None:
        """A locator would otherwise fail with 'exact text not found' for the wrong reason."""
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        book = Path(tmp.name) / "table.xlsx"
        book.write_bytes(b"not really a workbook")
        with self.assertRaises(ValueError) as caught:
            gate._artifact_text(book, "supplement_binary")
        self.assertIn("unsupported", str(caught.exception))

    def test_an_article_binary_pdf_stays_silent(self) -> None:
        """🔴 The green half. article_binary beside a structured surface is correct practice
        and must not start raising — blocking there would punish the practice."""
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        pdf = Path(tmp.name) / "paper.pdf"
        pdf.write_bytes(b"%PDF-1.4 not parsed here")
        self.assertEqual(gate._artifact_text(pdf, "article_binary"), ("", ""))

    def test_the_real_deposits_are_now_readable(self) -> None:
        """The four containers the census counted, on the production bytes."""
        deposits = [
            ROOT / "files/fulltext/PMID38499540_BidanyMizrahi2024_supplement"
                 / "41420_2024_1878_MOESM1_ESM.pptx",
            ROOT / "files/fulltext/PMID38499540_BidanyMizrahi2024_supplement"
                 / "41420_2024_1878_MOESM2_ESM.pptx",
            ROOT / "files/fulltext/PMID38499540_BidanyMizrahi2024_supplement"
                 / "41420_2024_1878_MOESM4_ESM.pptx",
            ROOT / "files/supplement/PMID33916893/s001/supplementary materials"
                 / "Supplemental Figure 1.pptx",
        ]
        present = [path for path in deposits if path.is_file()]
        if not present:  # files/ is gitignored by design
            self.skipTest("no .pptx deposits in this checkout")
        for path in present:
            body, abstract = gate._artifact_text(path, "supplement_binary")
            self.assertEqual(abstract, "")
            self.assertTrue(body.strip(), f"{path.name} yielded no text")

    def test_the_fields_not_mice_note_is_now_quotable(self) -> None:
        """The sentence the census named, verified as a locator would verify it."""
        deposit = (ROOT / "files/fulltext/PMID38499540_BidanyMizrahi2024_supplement"
                        / "41420_2024_1878_MOESM2_ESM.pptx")
        if not deposit.is_file():
            self.skipTest("PMID 38499540 supplement absent from this checkout")
        body, _abstract = gate._artifact_text(deposit, "supplement_binary")
        self.assertIn("fields", body)
        matched, _mode = gate._quote_matches("נעשו על כל הfields ולא על כל עכבר", body)
        self.assertTrue(matched, body)

    def test_undeclared_binary_supplements_are_a_falling_ratchet(self) -> None:
        """🔴 Measured 4 on 2026-09-10, and only a scientist can lower it.

        Making them DECLARABLE is harness work and is done. DECLARING them edits a manifest
        under `disease-models/`, which this task has read access to and nothing more. So the
        number is asserted as a ratchet that may only fall, never as an equality that would
        go red the day somebody does the right thing.
        """
        deposits = sorted(p for p in (ROOT / "files").rglob("*.pptx") if p.is_file())
        if not deposits:
            self.skipTest("no .pptx deposits in this checkout")
        declared: set[str] = set()
        directory = ROOT / "disease-models/wwox/research/deepdive_manifests"
        for path in directory.glob("PMID*.json"):
            manifest = json.loads(path.read_text(encoding="utf-8"))
            for artifact in manifest.get("source_artifacts") or []:
                declared.add(str(artifact.get("path", "")))
        undeclared = [p for p in deposits
                      if str(p.relative_to(ROOT)) not in declared]
        self.assertLessEqual(
            len(undeclared), 4,
            f"undeclared binary supplements rose above the 2026-09-10 baseline: {undeclared}")


class TheSuspectSurfaceScreenReturnsAVerdict(unittest.TestCase):
    """§ 9.2: every screen must say what it screened.

    A boolean is a claim with its evidence deleted. `True` cannot say what it looked at —
    which is how a call with inverted arguments screened a FILENAME and returned CLEAN over
    a PDF text layer carrying 191 C0 controls — and `False` cannot say what fired, which is
    how a refusal over 8 harmless front-matter separators was one step from being accepted
    as a verdict about a genotype corruption it had matched with nothing.
    """

    CLEAN_TEXT = ("A perfectly ordinary sentence from a paper, long enough to be a surface "
                  "and carrying no signature at all.")

    def _path(self, name: str = "PMID99999999_Fixture.txt") -> Path:
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        return Path(tmp.name) / name

    def test_a_clean_surface_returns_a_verdict_that_names_the_bytes(self) -> None:
        verdict = gate.screen_suspect_surface(self._path(), self.CLEAN_TEXT)
        self.assertTrue(verdict.is_clean)
        self.assertEqual(verdict.screened["bytes"], len(self.CLEAN_TEXT.encode("utf-8")))
        self.assertTrue(verdict.digest.startswith("sha256:"))
        self.assertTrue(verdict.covers(self.CLEAN_TEXT))

    def test_the_digest_is_over_what_was_screened_not_over_the_file(self) -> None:
        """Two parts are screened as one; the digest must cover exactly that."""
        verdict = gate.screen_suspect_surface(self._path(), "First half of it. ", "Second.")
        self.assertTrue(verdict.covers("First half of it. \nSecond."))
        self.assertFalse(verdict.covers("First half of it. "))

    def test_a_clean_verdict_never_claims_the_surface_is_faithful(self) -> None:
        verdict = gate.screen_suspect_surface(self._path(), self.CLEAN_TEXT)
        self.assertIn("NOT proof the surface is faithful", verdict.detail)

    def test_a_c0_control_refusal_names_its_signature_and_its_evidence(self) -> None:
        text = "The value was (P \x1d 0.023) in that experiment, which the page prints with <."
        verdict = gate.screen_suspect_surface(self._path(), text)
        self.assertTrue(verdict.is_refused)
        self.assertEqual(verdict.signature, gate.SIGNATURE_C0_CONTROL)
        self.assertEqual(verdict.evidence["codepoint"], "U+001D")
        self.assertTrue(verdict.covers(text))

    def test_a_printable_substitution_refusal_names_its_signature(self) -> None:
        text = ("Densitometry gave a ratio of 3 ¼ 7 across the lanes, which is the Elsevier "
                "text layer writing an equals sign as a fraction glyph.")
        verdict = gate.screen_suspect_surface(self._path(), text)
        self.assertTrue(verdict.is_refused)
        self.assertEqual(verdict.signature, gate.SIGNATURE_PRINTABLE_SUBSTITUTION)

    def test_the_absence_signature_carries_the_counts_it_refused_on(self) -> None:
        """🔴 B16: 'the gate said no' is not a finding; 'the gate said no because X' is."""
        text = ("The difference was significant by t-test, and the P-value was reported for "
                "every comparison, with significance throughout and a standard deviation "
                "given per group.")
        verdict = gate.screen_suspect_surface(self._path(), text)
        self.assertTrue(verdict.is_refused)
        self.assertEqual(verdict.signature, gate.SIGNATURE_COMPARATORS_ABSENT)
        self.assertGreaterEqual(verdict.evidence["statistical_mentions"],
                                gate.MIN_STATISTICAL_MENTIONS)
        self.assertEqual(verdict.evidence["typographic_operators"], 0)

    def test_an_empty_surface_is_insufficient_data_and_never_clean(self) -> None:
        """A zero-length surface is not a clean surface; that is the quietest silent pass."""
        verdict = gate.screen_suspect_surface(self._path(), "")
        self.assertTrue(verdict.is_insufficient)
        self.assertFalse(verdict.is_clean)

    def test_the_screen_returns_a_refusal_instead_of_raising_it(self) -> None:
        """A caller may inspect a refusal without exception handling — that is the point."""
        verdict = gate.screen_suspect_surface(self._path(), "Bad \x0c surface text here now.")
        self.assertTrue(verdict.is_refused)

    def test_the_refusing_wrapper_still_raises_and_carries_the_verdict(self) -> None:
        path = self._path()
        with self.assertRaises(gate.SuspectSurface) as caught:
            gate._refuse_suspect_surface(path, "The value was (P \x1d 0.023) in that run.")
        self.assertEqual(caught.exception.verdict.signature, gate.SIGNATURE_C0_CONTROL)
        self.assertIn("SUSPECT text surface", str(caught.exception))

    def test_the_refusal_is_still_a_valueerror(self) -> None:
        """Compatibility: validate() catches ValueError, and so do the shape regressions."""
        self.assertTrue(issubclass(gate.SuspectSurface, ValueError))
        with self.assertRaises(ValueError):
            gate._refuse_suspect_surface(self._path(), "Bad \x1e surface text right here.")

    def test_insufficient_data_raises_rather_than_passing(self) -> None:
        with self.assertRaises(gate.SuspectSurface) as caught:
            gate._refuse_suspect_surface(self._path(), "")
        self.assertTrue(caught.exception.verdict.is_insufficient)

    def test_the_wrapper_returns_the_verdict_on_a_clean_surface(self) -> None:
        verdict = gate._refuse_suspect_surface(self._path(), self.CLEAN_TEXT)
        self.assertTrue(verdict.is_clean)
        self.assertTrue(verdict.covers(self.CLEAN_TEXT))

    def test_an_inverted_call_is_a_typeerror_and_not_a_verdict(self) -> None:
        """🔴 A verdict record about the wrong bytes is what the contract makes impossible.

        The argument-shape violations stay exceptions rather than becoming
        INSUFFICIENT_DATA: they are caller bugs, and returning a well-formed verdict for
        them would hand the caller exactly the green result to point at that the whole
        contract exists to withhold.
        """
        path = self._path()
        with self.assertRaises(TypeError):
            gate.screen_suspect_surface("the text goes here, inverted", str(path))
        with self.assertRaises(TypeError):
            gate.screen_suspect_surface(path, path.name)


class IdentifiersAndCountsMustComeFromTheArtefact(unittest.TestCase):
    """§ 9.4: a value asserted in a proposition is in the artefact, or it is DECLARED.

    🔴 A WARN, never a BLOCK, and the tests assert that too — `test_warnings_never_change
    _the_verdict`. An identifier absent from the artefact is not thereby wrong; what the
    warning says is the checkable thing: nothing in the record says where this value came
    from. The declaration is the point, because a value that must be declared external is a
    value someone can challenge.
    """

    SENTENCE = "This body sentence is long enough to act as exact evidentiary text."

    def _run(self, proposition: str, *, declaration=None, artefact_extra: str = ""):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        relative = "files/fulltext/paper.xml"
        artifact = root / relative
        artifact.parent.mkdir(parents=True)
        artifact.write_text(
            f"<article><body><p>{self.SENTENCE}</p><p>{artefact_extra}</p></body></article>",
            encoding="utf-8")
        manifest = schema_v2(relative)
        manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
            artifact.read_bytes()).hexdigest()
        entry = manifest["verbatim_locators"]["entries"][0]
        entry["snippet"] = self.SENTENCE
        entry["proposition"] = proposition
        if declaration is not None:
            entry["external_provenance"] = declaration
        warnings: list[str] = []
        errors, _ = gate.validate(manifest, root=root, verify_artifacts=True,
                                  require_current_schema=True, warnings=warnings)
        return errors, warnings

    def test_a_declared_date_off_the_calendar_is_a_defective_declaration(self) -> None:
        """Mirror REV-EXPOST-20260911-001 F6 / MF-5: `2026-13-45` matched the shape and passed."""
        self.assertIsNone(gate.external_provenance_defect(
            {"source": "PubMed esearch, run this session", "date": "2026-09-11"}))
        defect = gate.external_provenance_defect(
            {"source": "PubMed esearch, run this session", "date": "2026-13-45"})
        self.assertIsNotNone(defect)
        self.assertIn("calendar", defect)
        _errors, warnings = self._run(
            "The upstream work is 29581896 by the same group.",
            declaration={"source": "PubMed esearch, run this session", "date": "2026-13-45"})
        self.assertTrue([w for w in warnings if "29581896" in w and "calendar" in w], warnings)

    def test_an_undeclared_identifier_warns(self) -> None:
        _errors, warnings = self._run("The upstream work is 29581896 by the same group.")
        self.assertTrue([w for w in warnings if "29581896" in w and "undeclared" in w],
                        warnings)

    def test_a_complete_declaration_silences_it(self) -> None:
        """The target state for every manifest minted after this change."""
        _errors, warnings = self._run(
            "The upstream work is 29581896 by the same group.",
            declaration="PubMed esearch author query, 2026-09-10")
        self.assertEqual(warnings, [])

    def test_a_dict_shaped_declaration_is_accepted(self) -> None:
        _errors, warnings = self._run(
            "The upstream work is 29581896 by the same group.",
            declaration={"source": "PubMed esearch", "date": "2026-09-10"})
        self.assertEqual(warnings, [])

    def test_a_declaration_without_a_date_still_warns(self) -> None:
        """C9 was a group count carried forward from a measurement three weeks old."""
        _errors, warnings = self._run(
            "The upstream work is 29581896 by the same group.",
            declaration="PubMed esearch author query")
        self.assertTrue([w for w in warnings if "no ISO date" in w], warnings)

    def test_a_declaration_without_a_source_still_warns(self) -> None:
        _errors, warnings = self._run(
            "The upstream work is 29581896 by the same group.", declaration="2026-09-10")
        self.assertTrue([w for w in warnings if "no command or index" in w], warnings)

    def test_an_identifier_present_in_the_artefact_never_warns(self) -> None:
        """🔴 The green half: without it, a checker that warned on everything would pass."""
        _errors, warnings = self._run(
            "The upstream work is 29310447 by the same group.",
            artefact_extra="<ext-link ext-link-type='pmid'>29310447</ext-link>")
        self.assertEqual(warnings, [])

    def test_a_source_identity_claim_is_not_waivable_by_a_declaration(self) -> None:
        """The peer tool's hardest-won rule, preserved rather than overridden.

        Written naively this checker would have MISSED the error it exists for: the failing
        proposition carried a legitimate declaration ABOUT THE LEDGER in the same sentence as
        a claim only the ARTEFACT can adjudicate.
        """
        _errors, warnings = self._run(
            "Attributed to ref 1, PMID 29581896, no receipt here.",
            declaration="PubMed esearch author query, 2026-09-10")
        self.assertTrue([w for w in warnings if "citation OF THE SOURCE" in w], warnings)

    def test_an_undeclared_count_warns(self) -> None:
        """A12: Zfra written as 2 when it is 13, with a false sentence built on it."""
        _errors, warnings = self._run(
            "The corpus holds only 2 mentions of Zfra across every manifest read so far.")
        self.assertTrue([w for w in warnings if "the count" in w and "2 mentions" in w],
                        warnings)

    def test_a_declared_count_does_not_warn(self) -> None:
        _errors, warnings = self._run(
            "The corpus holds only 2 mentions of Zfra across every manifest read so far.",
            declaration="grep -c over deepdive_manifests, 2026-09-10")
        self.assertEqual(warnings, [])

    def test_a_count_that_occurs_in_the_artefact_does_not_warn(self) -> None:
        _errors, warnings = self._run(
            "The authors report 13 mentions of the residue in their own discussion.",
            artefact_extra="a total of 13 separate observations")
        self.assertEqual(warnings, [])

    def test_warnings_never_change_the_verdict(self) -> None:
        errors, warnings = self._run("The upstream work is 29581896 by the same group.")
        self.assertEqual(errors, [])
        self.assertTrue(warnings)

    def test_a_caller_that_passes_no_sink_is_unaffected(self) -> None:
        """Backwards compatibility, asserted: session_self_eval.py passes no sink."""
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        relative = "files/fulltext/paper.xml"
        artifact = root / relative
        artifact.parent.mkdir(parents=True)
        artifact.write_text(f"<article><body><p>{self.SENTENCE}</p></body></article>",
                            encoding="utf-8")
        manifest = schema_v2(relative)
        manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
            artifact.read_bytes()).hexdigest()
        manifest["verbatim_locators"]["entries"][0]["snippet"] = self.SENTENCE
        manifest["verbatim_locators"]["entries"][0]["proposition"] = "Ref 1 is 29581896."
        with_sink: list[str] = []
        a_errors, a_incomplete = gate.validate(
            manifest, root=root, verify_artifacts=True, require_current_schema=True)
        b_errors, b_incomplete = gate.validate(
            manifest, root=root, verify_artifacts=True, require_current_schema=True,
            warnings=with_sink)
        self.assertEqual((a_errors, a_incomplete), (b_errors, b_incomplete))
        self.assertTrue(with_sink)

    def test_absent_evidence_is_reported_as_unmeasurable_not_as_a_flood(self) -> None:
        """files/ is gitignored: an empty haystack would make EVERY value undeclared."""
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        manifest = schema_v2("files/fulltext/absent.xml")
        manifest["verbatim_locators"]["entries"][0]["proposition"] = (
            "Refs 29581896, 30158849 and 31275852 are all cited here.")
        warnings = gate.provenance_warnings(manifest, root)
        self.assertEqual(len(warnings), 1)
        self.assertIn("NOT checked", warnings[0])
        self.assertIn("evidence-locality fact", warnings[0])

    def test_the_corpus_baseline_is_reproduced(self) -> None:
        """The § 9.4 measurement as an executable claim, re-derived from the tool's buckets."""
        directory = ROOT / "disease-models/wwox/research/deepdive_manifests"
        if not directory.is_dir():  # pragma: no cover
            self.skipTest("no manifests in this workspace")
        measurable = unmeasurable = 0
        for path in sorted(directory.glob("PMID*.json")):
            manifest = json.loads(path.read_text(encoding="utf-8"))
            found = gate.provenance_warnings(manifest, ROOT)
            if found and "NOT checked" in found[0]:
                unmeasurable += 1
            else:
                measurable += 1
        self.assertEqual(measurable + unmeasurable, len(list(directory.glob("PMID*.json"))))
        self.assertGreater(measurable, 0, "no manifest could be measured at all")


class PageFurnitureInsideAQuote(unittest.TestCase):
    """§ 9.5(b): a locator may not be quoted ACROSS page furniture in a derived text surface.

    The document below is the real shape of the 2026-09-09 failure: `pdftotext -layout` on a
    two-column page put the page number `588` between the two halves of the sentence carrying
    the headline claim. A quote taken across it verifies — that is what makes it dangerous.

    🔴 Three of these five tests exist to keep the check from becoming a false-positive
    factory. The wiring is a FILTER over a peer-owned detector, so the detector's counts are
    not the budget: what must stay at zero is locators refused on documents that contain
    intrusions the locators do not touch.
    """

    DOCUMENT = (
        "WWOX in bone biology and osteosarcoma\n"
        "\n"
        "Some earlier prose that ends properly here.\n"
        "587\n"
        "\n"
        "A fresh sentence begins after that page break.\n"
        "WWOX in bone biology and osteosarcoma\n"
        "\n"
        "imaging as a guide for sectioning. Using\n"
        "this protocol, osteosarcomas are detected in\n"
        "\n"
        "588\n"
        "\n"
        "100% of the post-natal mice prior to their death.\n"
        "Analyses by others of other Wwox null rodent\n"
        "models are broadly consistent with\n"
        "WWOX in bone biology and osteosarcoma\n"
        "\n"
        "589\n"
        "\n"
        "this observation in every reported cohort.\n"
    )

    def _workspace(self, snippet: str, *, kind: str = "article_text",
                   relative: str = "files/fulltext/paper.txt"):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        artifact = root / relative
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text(self.DOCUMENT, encoding="utf-8")
        manifest = schema_v2(relative)
        manifest["source_artifacts"][0]["kind"] = kind
        manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
            artifact.read_bytes()).hexdigest()
        manifest["verbatim_locators"]["entries"][0]["snippet"] = snippet
        return root, manifest

    def _errors(self, snippet: str, **kwargs) -> list[str]:
        root, manifest = self._workspace(snippet, **kwargs)
        errors, _ = gate.validate(manifest, root=root, verify_artifacts=True,
                                  require_current_schema=True)
        return errors

    def test_the_detector_sees_this_document(self) -> None:
        """🔴 A red baseline is not a capture: without an intrusion here, all of this is air."""
        spans = gate.intrusion_spans(self.DOCUMENT)
        self.assertTrue(spans, "the fixture must actually contain a detected intrusion")
        self.assertIn("588", [found["intrusion"] for _s, _e, found in spans])

    def test_a_quote_taken_across_the_page_number_is_a_block(self) -> None:
        errors = self._errors(
            "this protocol, osteosarcomas are detected in 588 100% of the post-natal mice")
        self.assertTrue([e for e in errors if "ACROSS page furniture" in e], errors)
        # The message must carry the evidence, not merely the verdict (§ 2.3: "the gate said
        # no because X" is a finding; "the gate said no" is not).
        self.assertTrue([e for e in errors if "'588'" in e and "page_number" in e], errors)

    def test_a_quote_that_stops_before_the_furniture_passes(self) -> None:
        """The false-positive guard: same document, same 3 intrusions, clean quote."""
        errors = self._errors(
            "imaging as a guide for sectioning. Using this protocol, osteosarcomas are "
            "detected in")
        self.assertEqual(errors, [])

    def test_a_quote_that_starts_after_the_furniture_passes(self) -> None:
        errors = self._errors(
            "100% of the post-natal mice prior to their death. Analyses by others of other "
            "Wwox null rodent models are broadly consistent with")
        self.assertEqual(errors, [])

    def test_a_quote_across_a_running_header_is_a_block(self) -> None:
        """Both furniture classes the detector reports, not only the numeric one."""
        errors = self._errors(
            "Wwox null rodent models are broadly consistent with WWOX in bone biology and "
            "osteosarcoma 589 this observation in every reported cohort.")
        self.assertTrue([e for e in errors if "ACROSS page furniture" in e], errors)

    # 🔴 An XML deposit whose RAW BYTES carry the same page-number chain the .txt fixture
    # does. The first version of the out-of-scope test below used a single-line XML, so the
    # detector found nothing in it and the test passed whether or not the scope guard
    # existed — it survived the mutant that deletes the guard entirely. A structured surface
    # is out of scope because it is not PDF-derived, and asserting that requires a fixture in
    # which an unscoped screen WOULD fire.
    STRUCTURED_DOCUMENT = (
        "<article><body>\n"
        "<p>Some earlier prose that ends properly here.\n"
        "587\n"
        "A fresh sentence begins after that page break.</p>\n"
        "<p>this protocol, osteosarcomas are detected in\n"
        "588\n"
        "100% of the post-natal mice prior to their death.</p>\n"
        "<p>models are broadly consistent with\n"
        "589\n"
        "this observation in every reported cohort.</p>\n"
        "</body></article>\n"
    )

    def test_a_structured_surface_is_out_of_scope(self) -> None:
        """An XML deposit is not PDF-derived; screening it would invent a hazard."""
        self.assertTrue(
            gate.intrusion_spans(self.STRUCTURED_DOCUMENT),
            "the fixture must be one an UNSCOPED screen would fire on, or this proves nothing")
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        relative = "files/fulltext/paper.xml"
        artifact = root / relative
        artifact.parent.mkdir(parents=True)
        artifact.write_text(self.STRUCTURED_DOCUMENT, encoding="utf-8")
        manifest = schema_v2(relative)
        manifest["source_artifacts"][0]["sha256"] = hashlib.sha256(
            artifact.read_bytes()).hexdigest()
        manifest["verbatim_locators"]["entries"][0]["snippet"] = (
            "this protocol, osteosarcomas are detected in 588 100% of the post-natal mice")
        errors, _ = gate.validate(manifest, root=root, verify_artifacts=True,
                                  require_current_schema=True)
        self.assertEqual(errors, [])

    def test_a_supplement_text_surface_is_in_scope(self) -> None:
        """The measured widening beyond § 9.5(b)'s letter, asserted so it cannot regress."""
        errors = self._errors(
            "this protocol, osteosarcomas are detected in 588 100% of the post-natal mice",
            kind="supplement_text")
        self.assertTrue([e for e in errors if "ACROSS page furniture" in e], errors)

    def test_the_real_pmid_21731849_sentence_blocks_and_its_neighbours_do_not(self) -> None:
        """The production case, on the production bytes, when this checkout has them."""
        surface = ROOT / "files/fulltext/PMID21731849_DelMare2011_AJCR.txt"
        if not surface.is_file():  # files/ is gitignored by design
            self.skipTest("PMID 21731849 article text absent from this checkout")
        text = surface.read_text(encoding="utf-8")
        spans = gate.intrusion_spans(text)
        self.assertEqual(len(spans), 13, "the tuned detector baseline moved")
        self.assertIsNotNone(gate.snippet_spans_intrusion(
            "Using this protocol, osteosarcomas are detected in 588 100% of the post-natal "
            "mice prior to their death.", text, spans))
        for clean in (
            "imaging as a guide for sectioning [23]. Using this protocol, osteosarcomas "
            "are detected in",
            "100% of the post-natal mice prior to their death. Analyses by others of other "
            "Wwox null rodent",
        ):
            self.assertIsNone(gate.snippet_spans_intrusion(clean, text, spans), clean)

    def test_every_landed_manifest_still_passes_the_screen(self) -> None:
        """The false-positive budget itself: 0 locators refused across the whole corpus."""
        directory = ROOT / "disease-models/wwox/research/deepdive_manifests"
        if not directory.is_dir():  # pragma: no cover
            self.skipTest("no manifests in this workspace")
        refused = []
        for path in sorted(directory.glob("PMID*.json")):
            manifest = json.loads(path.read_text(encoding="utf-8"))
            declared = {a.get("path"): a for a in (manifest.get("source_artifacts") or [])}
            for relative, meta in declared.items():
                if meta.get("kind") not in gate.DERIVED_TEXT_KINDS:
                    continue
                if not str(relative).lower().endswith(".txt"):
                    continue
                surface = ROOT / str(relative)
                if not surface.is_file():
                    continue
                text = surface.read_text(encoding="utf-8", errors="replace")
                spans = gate.intrusion_spans(text)
                entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
                for index, entry in enumerate(entries):
                    named = entry.get("artifact")
                    named = [named] if isinstance(named, str) else (named or [])
                    if relative not in named:
                        continue
                    if gate.snippet_spans_intrusion(
                            str(entry.get("snippet", "")), text, spans):
                        refused.append((path.name, index, relative))
        self.assertEqual(refused, [], "the wiring added a false positive to the corpus")


class QueueIdentifiersAreCrossChecked(unittest.TestCase):
    """§ 9.5(a): a queued hop may not point at another paper's queue entry.

    The unit tests of the check itself live in `test_manifest_queue_id_crosscheck.py`. What
    is asserted HERE is the property that was missing on 2026-09-09 and that only the
    validator can provide: that `deepdive_manifest.validate` actually calls it, and refuses.
    A check nobody invokes is a check that catches the defect only when someone remembers.
    """

    QUEUE = (
        "# FULL TEXT QUEUE\n\n"
        "## FT-071 — This paper's own entry\n"
        "**Paper:** PMID 12345678 — the manifest under test.\n\n"
        "## FT-072 — An unrelated paper\n"
        "**Paper:** PMID 20530675 — Kurek KC et al., Oncogene 2010.\n"
    )

    def _workspace(self, queue_id: str, *, with_queue: bool = True):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        if with_queue:
            queue = root / "disease-models/wwox/research/full_text_queue_current.md"
            queue.parent.mkdir(parents=True)
            queue.write_text(self.QUEUE, encoding="utf-8")
        manifest = minimal()
        manifest["multihop"] = {
            "gene_direct_refs_in_source": ["ref 42"],
            "references_enumerated": 48,
            "resolved": ["17086198"],
            "queued": [{"ref": 46, "pmid": "16941225", "queue": queue_id,
                        "reason": "a hop this reading owes"}],
        }
        return root, manifest

    def test_a_foreign_queue_identifier_is_a_block(self) -> None:
        root, manifest = self._workspace("FT-072")
        errors, _ = gate.validate(manifest, root=root)
        self.assertTrue([e for e in errors if "FT-072" in e and "different paper" in e], errors)

    def test_an_unresolvable_queue_identifier_is_a_block(self) -> None:
        root, manifest = self._workspace("FT-999")
        errors, _ = gate.validate(manifest, root=root)
        self.assertTrue([e for e in errors if "FT-999" in e and "no entry" in e], errors)

    def test_the_paper_s_own_entry_passes(self) -> None:
        """🔴 The green half. Without it, a check that refused everything would pass above."""
        root, manifest = self._workspace("FT-071")
        errors, incomplete = gate.validate(manifest, root=root)
        self.assertEqual(errors, [])
        self.assertEqual(incomplete, [])

    def test_a_workspace_without_the_queue_declares_the_gap_instead_of_passing(self) -> None:
        """Not silence: the identifiers that went unchecked are named."""
        root, manifest = self._workspace("FT-072", with_queue=False)
        errors, incomplete = gate.validate(manifest, root=root)
        self.assertEqual(errors, [])
        self.assertTrue([i for i in incomplete if "FT-072" in i and "NOT checked" in i],
                        incomplete)

    def test_the_queue_is_looked_up_beside_the_manifest_not_beside_the_evidence(self) -> None:
        """A branch carries the manifest and the queue; gitignored evidence stays elsewhere."""
        with TemporaryDirectory() as evidence_tmp:
            root, manifest = self._workspace("FT-072")
            work = gate.manifest_path(root, "wwox", "12345678")
            work.parent.mkdir(parents=True, exist_ok=True)
            work.write_text(json.dumps(manifest), encoding="utf-8")
            errors, _ = gate.load_and_validate(
                root, "wwox", "12345678", artifact_root=Path(evidence_tmp))
            self.assertTrue([e for e in errors if "FT-072" in e], errors)


def load_mutated(*substitutions):
    """Load deepdive_manifest.py with textual substitutions applied — the shipped file, mutated."""
    src = (HERE / "deepdive_manifest.py").read_text(encoding="utf-8")
    for old, new in substitutions:
        if old not in src:
            raise AssertionError(f"mutation target not present in source: {old!r}")
        src = src.replace(old, new, 1)
    spec = importlib.util.spec_from_loader("deepdive_manifest_mutant", loader=None)
    module = importlib.util.module_from_spec(spec)
    module.__dict__["__file__"] = str(HERE / "deepdive_manifest.py")
    exec(compile(src, str(HERE / "deepdive_manifest.py") + " [MUTANT]", "exec"), module.__dict__)
    return module


class TheDependencyScreenIsAManifestSlot(unittest.TestCase):
    """S7 / H6: a per-PMID retraction check cannot see what a paper depends on.

    The slot is optional and a ratchet: shape-checked when present, a `[DECLARED GAP]` when
    absent, never a block, no historical manifest rewritten. What it refuses is exactly what
    `dependency_integrity.py` already refuses one layer down — a collapsed nature class and
    an UNSCREENABLE that reads as clean — so the slot cannot weaken the tool it carries.
    """

    def _with(self, **block_overrides) -> dict:
        manifest = minimal()
        manifest["retraction_check"]["dependencies"] = dependencies_block(**block_overrides)
        return manifest

    def test_a_valid_block_is_neither_an_error_nor_a_ratchet(self) -> None:
        ratchets: list[str] = []
        errors, incomplete = gate.validate(minimal(), ratchets=ratchets)
        self.assertEqual(errors, [])
        self.assertFalse([i for i in ratchets if gate.DEPENDENCY_GAP in i])

    def test_absence_is_a_ratchet_never_a_gap_and_never_a_block(self) -> None:
        """🔴 Not `incomplete`: the strict receipt writer refuses every declared gap, by design,
        so an absence emitted there refused every manifest minted before the slot existed
        (test_legend_lint.py, 5 ERRORs, caught before landing). A ratchet is its own sink."""
        manifest = minimal()
        del manifest["retraction_check"]["dependencies"]
        ratchets: list[str] = []
        errors, incomplete = gate.validate(manifest, ratchets=ratchets)
        self.assertEqual(errors, [])
        self.assertFalse([i for i in incomplete if gate.DEPENDENCY_GAP in i], incomplete)
        self.assertTrue([i for i in ratchets if i.startswith(gate.DEPENDENCY_GAP)], ratchets)
        # a caller that passes no sink is byte-for-byte unaffected
        self.assertEqual(gate.validate(manifest), (errors, incomplete))

    def test_every_committed_manifest_is_a_ratchet_not_a_block_here(self) -> None:
        """History is not rewritten: committed manifests without the slot validate, ratchet noted."""
        found = sorted(MANIFESTS.glob("PMID*.json"))
        self.assertTrue(found)
        for path in found:
            manifest = json.loads(path.read_text(encoding="utf-8"))
            ratchets: list[str] = []
            errors, incomplete = gate.validate(manifest, ratchets=ratchets)
            self.assertEqual(errors, [], path.name)
            self.assertFalse([i for i in incomplete if gate.DEPENDENCY_GAP in i], path.name)
            retraction = manifest["retraction_check"]
            if "dependencies" not in retraction and not retraction.get("waived"):
                self.assertTrue([i for i in ratchets if i.startswith(gate.DEPENDENCY_GAP)],
                                path.name)

    def test_the_vocabulary_is_the_tools_own_by_identity(self) -> None:
        self.assertIs(gate.dependency_screen.UNSCREENABLE,
                      sys.modules["dependency_integrity"].UNSCREENABLE)
        self.assertIs(gate.dependency_screen.INTEGRITY_FLAGS,
                      sys.modules["dependency_integrity"].INTEGRITY_FLAGS)

    def test_a_flagged_dependency_needs_a_stated_citing_relation(self) -> None:
        placeholder = gate.dependency_screen.CITING_RELATION_PLACEHOLDER
        errors, _ = gate.validate(self._with(
            paper_verdict="FLAGGED_EXPRESSION_OF_CONCERN",
            flagged=[flagged_entry(citing_relation=placeholder)]))
        self.assertTrue(any("citing_relation" in e for e in errors), errors)
        errors, _ = gate.validate(self._with(
            paper_verdict="FLAGGED_EXPRESSION_OF_CONCERN", flagged=[flagged_entry()]))
        self.assertEqual(errors, [])

    def test_the_natures_are_never_collapsed(self) -> None:
        errors, _ = gate.validate(self._with(
            paper_verdict="FLAGGED_RETRACTION",
            flagged=[flagged_entry(nature="Expression of concern", verdict="FLAGGED_RETRACTION")]))
        self.assertTrue(any("never collapsed" in e for e in errors), errors)

    def test_a_correction_may_not_sit_under_flagged(self) -> None:
        errors, _ = gate.validate(self._with(
            paper_verdict="FLAGGED_EXPRESSION_OF_CONCERN",
            flagged=[flagged_entry(),
                     flagged_entry(doi="10.1038/sj.onc.1209323", nature="Correction",
                                   verdict="NOTED_CORRECTION")]))
        self.assertTrue(any("belongs under `noted`" in e for e in errors), errors)

    def test_unscreenable_is_never_clean(self) -> None:
        errors, _ = gate.validate(self._with(
            paper_verdict="UNSCREENABLE_NO_REFERENCE_LIST", screened=True,
            references_declared=0, references_screened=0, unscreenable={}))
        self.assertTrue(any("UNSCREENABLE verdict cannot carry screened=true" in e
                            for e in errors), errors)

    def test_clean_over_zero_screened_references_is_refused(self) -> None:
        errors, _ = gate.validate(self._with(
            references_declared=0, references_screened=0, unscreenable={}))
        self.assertTrue(any("looked at nothing" in e for e in errors), errors)

    def test_the_counts_must_add_up(self) -> None:
        errors, _ = gate.validate(self._with(references_screened=20))
        self.assertTrue(any("must equal references_declared" in e for e in errors), errors)

    def test_an_unknown_unscreenable_class_is_refused(self) -> None:
        errors, _ = gate.validate(self._with(unscreenable={"NOT_A_CLASS": 2}))
        self.assertTrue(any("not an unscreenable class" in e for e in errors), errors)

    def test_the_snapshot_date_is_required(self) -> None:
        errors, _ = gate.validate(self._with(snapshot={"date": "yesterday"}))
        self.assertTrue(any("snapshot.date" in e for e in errors), errors)

    def test_the_emitted_block_validates_once_the_relation_is_stated(self) -> None:
        """The real emitter's output, on the real S7 manifest, pastes in and validates."""
        di = gate.dependency_screen
        path, pin, problems = di.verify_snapshot()
        if problems:
            self.skipTest("Retraction Watch snapshot unusable: " + "; ".join(problems))
        cache = Path(di.REFS_CACHE) / "10_1111_j_1349_7006_2008_00841_x.json"
        if not cache.is_file():
            self.skipTest("Crossref reference cache for PMID 18460020 absent (files/ is gitignored)")
        res = di.screen_paper("10.1111/j.1349-7006.2008.00841.x", di.load_index(path),
                              pmid="18460020", offline=True, stale_days=0)
        block = di.manifest_block(res, pin, 0)
        self.assertEqual(block["paper_verdict"], "FLAGGED_EXPRESSION_OF_CONCERN")
        manifest = json.loads((MANIFESTS / "PMID18460020.json").read_text(encoding="utf-8"))
        manifest["retraction_check"]["dependencies"] = block
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("citing_relation" in e for e in errors), "placeholder accepted")
        for entry in block["flagged"]:
            entry["citing_relation"] = ("reagent source: the adenovirus and both antibodies "
                                        "descend from the flagged paper (PMID18460020.md § 7)")
        ratchets: list[str] = []
        errors, _incomplete = gate.validate(manifest, ratchets=ratchets)
        self.assertEqual(errors, [])
        self.assertFalse([i for i in ratchets if gate.DEPENDENCY_GAP in i])

    # --- mutation battery: each names the invariant it breaks -------------------------
    def test_mutation_collapsing_natures_is_caught(self) -> None:
        mut = load_mutated(('        if entry.get("verdict") != expected:',
                            '        if False:'))
        manifest = self._with(paper_verdict="FLAGGED_RETRACTION",
                              flagged=[flagged_entry(nature="Expression of concern",
                                                     verdict="FLAGGED_RETRACTION")])
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_letting_unscreenable_read_as_screened_is_caught(self) -> None:
        mut = load_mutated(('    if verdict in dependency_screen.UNSCREENABLE and screened is True:',
                            '    if False:'))
        manifest = self._with(paper_verdict="UNSCREENABLE_NO_REFERENCE_LIST", screened=True,
                              references_declared=0, references_screened=0, unscreenable={})
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_accepting_clean_over_nothing_is_caught(self) -> None:
        mut = load_mutated(('        if counts.get("references_screened", 0) == 0:',
                            '        if False:'))
        manifest = self._with(references_declared=0, references_screened=0, unscreenable={})
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_accepting_the_placeholder_relation_is_caught(self) -> None:
        mut = load_mutated(('        if relation == dependency_screen.CITING_RELATION_PLACEHOLDER \\\n'
                            '                or len(relation) < MIN_REASON_CHARS:',
                            '        if False:'))
        manifest = self._with(paper_verdict="FLAGGED_EXPRESSION_OF_CONCERN",
                              flagged=[flagged_entry(
                                  citing_relation=gate.dependency_screen.CITING_RELATION_PLACEHOLDER)])
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_dropping_the_count_arithmetic_is_caught(self) -> None:
        mut = load_mutated(('    if len(counts) == 2 and all(isinstance(c, int) for c in unscreenable.values()):',
                            '    if False:'))
        manifest = self._with(references_screened=20)
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_silencing_the_absence_ratchet_is_caught(self) -> None:
        mut = load_mutated(('        elif ratchets is not None:\n            ratchets.append(',
                            '        elif False:\n            ratchets.append('))
        manifest = minimal()
        del manifest["retraction_check"]["dependencies"]
        sink: list[str] = []
        mut.validate(manifest, ratchets=sink)
        self.assertFalse([i for i in sink if mut.DEPENDENCY_GAP in i])
        sink = []
        gate.validate(manifest, ratchets=sink)
        self.assertTrue([i for i in sink if gate.DEPENDENCY_GAP in i])

    def test_mutation_routing_the_ratchet_into_incomplete_is_caught(self) -> None:
        """The defect that was caught before landing, kept as a mutant so it stays caught."""
        mut = load_mutated(('        elif ratchets is not None:\n            ratchets.append(',
                            '        else:\n            incomplete.append('))
        manifest = minimal()
        del manifest["retraction_check"]["dependencies"]
        self.assertTrue([i for i in mut.validate(manifest)[1] if mut.DEPENDENCY_GAP in i])
        self.assertFalse([i for i in gate.validate(manifest)[1] if gate.DEPENDENCY_GAP in i])


class TheAcquisitionRecipeIsPublishedWhereTheBytesCannotBe(unittest.TestCase):
    """Census P2: `files/` is gitignored, so a fresh checkout holds none of the bytes its
    manifests fingerprint. `regenerate_adjudications.py` already publishes the RECIPE for
    page crops; acquisitions carried a digest and no recipe. This slot is the recipe.
    """

    def _v2(self, recipe) -> dict:
        manifest = schema_v2()
        manifest["source_artifacts"][0]["acquisition_recipe"] = recipe
        return manifest

    def test_a_fetch_recipe_validates_and_closes_the_ratchet(self) -> None:
        ratchets: list[str] = []
        errors, _incomplete = gate.validate(schema_v2(), ratchets=ratchets)
        self.assertEqual(errors, [])
        self.assertFalse([i for i in ratchets if gate.RECIPE_GAP in i])

    def test_absence_is_a_ratchet_never_a_gap_and_never_a_block(self) -> None:
        manifest = schema_v2()
        del manifest["source_artifacts"][0]["acquisition_recipe"]
        ratchets: list[str] = []
        errors, incomplete = gate.validate(manifest, ratchets=ratchets)
        self.assertEqual(errors, [])
        self.assertFalse([i for i in incomplete if gate.RECIPE_GAP in i], incomplete)
        gap = [i for i in ratchets if i.startswith(gate.RECIPE_GAP)]
        self.assertEqual(len(gap), 1, ratchets)
        self.assertIn("1 of 1 artefact(s)", gap[0])
        self.assertEqual(gate.validate(manifest), (errors, incomplete))

    def test_a_stated_no_recipe_is_accepted_and_still_counted_as_a_ratchet(self) -> None:
        manifest = self._v2({"no_recipe": "the route was never recorded; the note names "
                                          "only the PMCID and the day"})
        ratchets: list[str] = []
        errors, _incomplete = gate.validate(manifest, ratchets=ratchets)
        self.assertEqual(errors, [])
        gap = [i for i in ratchets if i.startswith(gate.RECIPE_GAP)]
        self.assertIn("(1 with a stated no_recipe reason)", gap[0])

    def test_a_manifest_without_the_two_blocks_still_supports_a_complete_receipt(self) -> None:
        """🔴 The acceptance case, through the real strict receipt gate, mutated both ways.

        A manifest minted before the slots existed must still back a `complete_fulltext_read`;
        a malformed block must still refuse it. `fulltext_receipts.require_work_manifest` is
        called as it is shipped — it is the consumer that turned red on 2026-09-11.
        """
        import fulltext_receipts
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            relative = "files/fulltext/paper.xml"
            artifact = root / relative
            artifact.parent.mkdir(parents=True)
            sentence = "This body sentence is long enough to act as exact evidentiary text."
            artifact.write_text(f"<article><body><p>{sentence}</p></body></article>", encoding="utf-8")
            manifest = schema_v2(relative)
            del manifest["source_artifacts"][0]["acquisition_recipe"]
            del manifest["retraction_check"]["dependencies"]
            digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
            manifest["source_artifacts"][0]["sha256"] = digest
            manifest["verbatim_locators"]["entries"][0]["snippet"] = sentence
            work = gate.manifest_path(root, "wwox", "12345678")
            work.parent.mkdir(parents=True)
            work.write_text(json.dumps(manifest), encoding="utf-8")
            receipt = {"evidence_depth": "complete_fulltext_read",
                       "record_kind": "contemporaneous_receipt", "reread_reason": "first_read",
                       "study_id": {"pmid": "12345678"}, "source_locator": relative,
                       "source_fingerprint": digest}
            # 1. absent slots: the complete receipt is allowed
            fulltext_receipts.require_work_manifest(receipt, root, "wwox", strict=True)
            # 2. a malformed block: refused, naming the block
            manifest["retraction_check"]["dependencies"] = {"paper_verdict": "SCREENED_CLEAN",
                                                            "screened": True}
            work.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "retraction_check.dependencies"):
                fulltext_receipts.require_work_manifest(receipt, root, "wwox", strict=True)
            del manifest["retraction_check"]["dependencies"]
            manifest["source_artifacts"][0]["acquisition_recipe"] = {"resolved_url": "ftp://x",
                                                                     "derived": False}
            work.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "acquisition_recipe"):
                fulltext_receipts.require_work_manifest(receipt, root, "wwox", strict=True)
            # 3. mutation both ways, through the same gate: the ratchet routed into
            #    `incomplete` refuses the clean manifest; the shape check dropped admits the bad one
            del manifest["source_artifacts"][0]["acquisition_recipe"]
            work.write_text(json.dumps(manifest), encoding="utf-8")
            routed = load_mutated(('            if (without_recipe or named_no_recipe) and ratchets is not None:\n'
                                   '                total = with_recipe + without_recipe + named_no_recipe\n'
                                   '                ratchets.append(',
                                   '            if (without_recipe or named_no_recipe):\n'
                                   '                total = with_recipe + without_recipe + named_no_recipe\n'
                                   '                incomplete.append('))
            self.assertTrue([i for i in routed.load_and_validate(
                root, "wwox", "12345678", verify_artifacts=True, require_current_schema=True)[1]
                if routed.RECIPE_GAP in i])
            self.assertFalse([i for i in gate.load_and_validate(
                root, "wwox", "12345678", verify_artifacts=True, require_current_schema=True)[1]
                if gate.RECIPE_GAP in i])
            manifest["retraction_check"]["dependencies"] = {"paper_verdict": "SCREENED_CLEAN",
                                                            "screened": True}
            work.write_text(json.dumps(manifest), encoding="utf-8")
            lax = load_mutated(('            errors.extend(dependency_screen_defects(retraction["dependencies"]))',
                                '            pass'))
            self.assertEqual(lax.load_and_validate(root, "wwox", "12345678", verify_artifacts=True,
                                                   require_current_schema=True)[0], [])
            self.assertNotEqual(gate.load_and_validate(root, "wwox", "12345678", verify_artifacts=True,
                                                       require_current_schema=True)[0], [])

    def test_a_hollow_no_recipe_is_refused(self) -> None:
        errors, _ = gate.validate(self._v2({"no_recipe": "unknown"}))
        self.assertTrue(any("no_recipe" in e for e in errors), errors)

    def test_no_email_address_ever_rides_in_a_recipe_url(self) -> None:
        for url in ("https://api.unpaywall.org/v2/10.1/x?email=someone@example.invalid",
                    "https://x.org/?mailto=a@b.c"):
            errors, _ = gate.validate(self._v2(acquisition_recipe(resolved_url=url)))
            self.assertTrue(any("email address" in e for e in errors), url)

    def test_the_user_agent_policy_is_part_of_the_route(self) -> None:
        errors, _ = gate.validate(self._v2(acquisition_recipe(user_agent_policy="whatever")))
        self.assertTrue(any("user_agent_policy" in e for e in errors), errors)
        for policy in sorted(gate.UA_POLICIES):
            errors, _ = gate.validate(self._v2(acquisition_recipe(user_agent_policy=policy)))
            self.assertEqual(errors, [], policy)

    def test_a_result_digest_that_disagrees_with_the_entry_is_refused(self) -> None:
        errors, _ = gate.validate(self._v2(acquisition_recipe(result_sha256="b" * 64)))
        self.assertTrue(any("describes a different artefact" in e for e in errors), errors)
        errors, _ = gate.validate(self._v2(acquisition_recipe(result_sha256="a" * 64)))
        self.assertEqual(errors, [])

    def test_a_derived_artefact_names_its_source_and_its_extractor_version(self) -> None:
        manifest = schema_v2()
        manifest["source_artifacts"].append({
            "path": "files/fulltext/paper.pdf", "sha256": "c" * 64, "kind": "article_binary",
            "acquisition_recipe": acquisition_recipe(tier="pmc_pow")})
        manifest["source_artifacts"][0]["acquisition_recipe"] = derived_recipe()
        errors, incomplete = gate.validate(manifest)
        self.assertEqual(errors, [])
        self.assertFalse([i for i in incomplete if gate.RECIPE_GAP in i])
        # version missing: drift could never be named
        manifest["source_artifacts"][0]["acquisition_recipe"] = derived_recipe(
            extractor={"name": "PyMuPDF", "call": "page.get_text()"})
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("extractor.version" in e for e in errors), errors)
        # source not declared in this manifest
        manifest["source_artifacts"][0]["acquisition_recipe"] = derived_recipe(
            derived_from="files/fulltext/elsewhere.pdf")
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("derived_from" in e for e in errors), errors)
        # a source may not be itself
        manifest["source_artifacts"][0]["acquisition_recipe"] = derived_recipe(
            derived_from="files/fulltext/paper.xml")
        errors, _ = gate.validate(manifest)
        self.assertTrue(any("derived_from" in e for e in errors), errors)

    def test_the_gap_counts_every_artefact_once(self) -> None:
        manifest = schema_v2()
        manifest["source_artifacts"].append({
            "path": "files/figures/f1.png", "sha256": "d" * 64, "kind": "figure"})
        manifest["source_artifacts"].append({
            "path": "files/figures/f2.png", "sha256": "e" * 64, "kind": "figure",
            "acquisition_recipe": {"no_recipe": "figure render dpi lives only in a locator "
                                                "anchor, so no derivation is stated here"}})
        ratchets: list[str] = []
        gate.validate(manifest, ratchets=ratchets)
        gap = [i for i in ratchets if i.startswith(gate.RECIPE_GAP)][0]
        self.assertIn("2 of 3 artefact(s) (1 with a stated no_recipe reason)", gap)

    def test_legacy_v1_manifests_carry_no_recipe_ratchet(self) -> None:
        """No source_artifacts, nothing to have a recipe for — the ratchet starts at v2."""
        ratchets: list[str] = []
        gate.validate(minimal(), ratchets=ratchets)
        self.assertFalse([i for i in ratchets if gate.RECIPE_GAP in i])

    def test_every_committed_v2_manifest_reports_the_ratchet_and_none_is_blocked(self) -> None:
        found = sorted(MANIFESTS.glob("PMID*.json"))
        with_gap = declared = 0
        for path in found:
            manifest = json.loads(path.read_text(encoding="utf-8"))
            ratchets: list[str] = []
            errors, incomplete = gate.validate(manifest, ratchets=ratchets)
            self.assertEqual(errors, [], path.name)
            self.assertFalse([i for i in incomplete if gate.RECIPE_GAP in i], path.name)
            if manifest.get("schema_version", 1) >= 2:
                if [i for i in ratchets if i.startswith(gate.RECIPE_GAP)]:
                    with_gap += 1
                else:
                    declared += 1
        self.assertGreater(with_gap + declared, 0)

    # --- mutation battery -------------------------------------------------------------
    def test_mutation_admitting_an_address_in_the_url_is_caught(self) -> None:
        mut = load_mutated(('RECIPE_URL_RE = re.compile(r"^https?://[^\\s@]+$")',
                            'RECIPE_URL_RE = re.compile(r"^https?://\\S+$")'))
        manifest = self._v2(acquisition_recipe(resolved_url="https://x.org/?mailto=a@b.c"))
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_dropping_the_extractor_version_requirement_is_caught(self) -> None:
        mut = load_mutated(('            for key in ("name", "version", "call"):',
                            '            for key in ("name", "call"):'))
        manifest = schema_v2()
        manifest["source_artifacts"].append({
            "path": "files/fulltext/paper.pdf", "sha256": "c" * 64, "kind": "article_binary"})
        manifest["source_artifacts"][0]["acquisition_recipe"] = derived_recipe(
            extractor={"name": "PyMuPDF", "call": "page.get_text()"})
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_accepting_a_foreign_result_digest_is_caught(self) -> None:
        mut = load_mutated(('    if result is not None and str(result) != declared_sha256:',
                            '    if False:'))
        manifest = self._v2(acquisition_recipe(result_sha256="b" * 64))
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_silencing_the_recipe_ratchet_is_caught(self) -> None:
        mut = load_mutated(('            if (without_recipe or named_no_recipe) and ratchets is not None:',
                            '            if False:'))
        manifest = schema_v2()
        del manifest["source_artifacts"][0]["acquisition_recipe"]
        sink: list[str] = []
        mut.validate(manifest, ratchets=sink)
        self.assertFalse([i for i in sink if mut.RECIPE_GAP in i])
        sink = []
        gate.validate(manifest, ratchets=sink)
        self.assertTrue([i for i in sink if gate.RECIPE_GAP in i])

    def test_mutation_letting_a_derived_artefact_source_itself_is_caught(self) -> None:
        mut = load_mutated(('        if not source or source == own_path or source not in declared_paths:',
                            '        if not source:'))
        manifest = self._v2(derived_recipe(derived_from="files/fulltext/paper.xml"))
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])

    def test_mutation_widening_the_user_agent_policies_is_caught(self) -> None:
        mut = load_mutated(('UA_POLICIES = {"none", "identified", "browser_like"}',
                            'UA_POLICIES = {"none", "identified", "browser_like", "whatever"}'))
        manifest = self._v2(acquisition_recipe(user_agent_policy="whatever"))
        self.assertEqual(mut.validate(manifest)[0], [])
        self.assertNotEqual(gate.validate(manifest)[0], [])


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
