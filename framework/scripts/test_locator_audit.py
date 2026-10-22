#!/usr/bin/env python3
"""Regressions for the mechanical locator audit.

The script answers one question — does this quote occur in the artifact it was taken from —
for the manifests `deepdive_manifest --verify-artifacts` cannot reach. These tests keep it
answering that question and not a nearby one.
"""
from __future__ import annotations

import importlib.util
import io
import json
import re
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("locator_audit", HERE / "locator_audit.py")
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)

ARTICLE = (
    "<article><body><sec><p>The rescue restored survival in Wwox null mice at the high "
    "dose.</p><p>No difference in time to onset was observed between the groups.</p>"
    "</sec></body></article>"
)


class Workspace:
    def __init__(self, stack: TemporaryDirectory):
        self.root = Path(stack.name)
        self.corpus = self.root / "files" / "fulltext"
        self.corpus.mkdir(parents=True)
        (self.corpus / "PMID12345678_Author2020_PMC.xml").write_text(ARTICLE, encoding="utf-8")
        self.manifests = self.root / "disease-models/wwox/research/deepdive_manifests"
        self.manifests.mkdir(parents=True)

    def manifest(self, entries, schema=None, artifacts=None) -> Path:
        payload = {"pmid": "12345678", "verbatim_locators": {"entries": entries}}
        if schema:
            payload["schema_version"] = schema
        if artifacts:
            payload["source_artifacts"] = artifacts
        path = self.manifests / "PMID12345678.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path


def entry(snippet, surface="body"):
    return {"proposition": "p", "snippet": snippet, "surface": surface, "anchor": "a"}


class TheAuditFindsWhatItShould(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = TemporaryDirectory()
        self.addCleanup(self.stack.cleanup)
        self.workspace = Workspace(self.stack)

    def audit(self, path):
        return audit.audit_one(path, self.workspace.corpus)

    def test_a_quote_present_in_the_artifact_matches(self) -> None:
        path = self.workspace.manifest([entry("restored survival in Wwox null mice")])
        result = self.audit(path)
        self.assertEqual([0], result["matched"])
        self.assertEqual([], result["missing"])

    def test_a_quote_absent_from_the_artifact_is_reported(self) -> None:
        path = self.workspace.manifest([entry("restored fertility in Wwox null mice")])
        self.assertEqual([0], self.audit(path)["missing"])

    def test_a_figure_locator_is_not_matched_as_text(self) -> None:
        """Matching pixels as a string asks the wrong question and answers it wrongly."""
        path = self.workspace.manifest([entry("[figure attestation] panel b", "figure")])
        result = self.audit(path)
        self.assertEqual([0], result["image"])
        self.assertEqual([], result["missing"])

    def test_text_read_from_a_rendered_page_is_not_matched_against_the_text_layer(self) -> None:
        """HARNESS-P-20260914 P10: `rendered_text` is running text read as pixels because the
        text layer was refused. Matching it against that layer would report a faithful quote
        as missing, and re-admit the surface the reading rejected."""
        path = self.workspace.manifest(
            [entry("a sentence the text layer mangles beyond recognition", "rendered_text")])
        result = self.audit(path)
        self.assertEqual([0], result["image"], result)
        self.assertEqual([], result["missing"])

    def test_an_unreadable_corpus_reports_that_it_could_not_look(self) -> None:
        """🔴 Not finding anything and not being able to look are different statements.

        `files/` is gitignored, so this is the ordinary condition in a worktree. A run that
        reported "no defects" from an empty corpus would be the most expensive kind of quiet.
        """
        path = self.workspace.manifest([entry("restored fertility in Wwox null mice")])
        result = audit.audit_one(path, self.workspace.root / "nowhere")
        self.assertIn("unauditable", result["reason"])
        self.assertEqual([], result["missing"])

    def test_a_declared_artifact_beats_a_resolved_one(self) -> None:
        """The first run of this script manufactured a failure by guessing.

        A schema-v2 manifest may quote a supplement; resolving one file per study and matching
        everything against it reported entry 16 of PMID 37519886 as missing while
        `--verify-artifacts` passed it, because the quote was in a declared surface the guess
        had not picked.
        """
        supplement = self.workspace.corpus / "PMID12345678_supplement.txt"
        supplement.write_text("A sentence that lives only in the supplement.", encoding="utf-8")
        path = self.workspace.manifest(
            [entry("lives only in the supplement", "supplement")],
            schema=2,
            artifacts=[{"path": "files/fulltext/PMID12345678_supplement.txt",
                        "sha256": "a" * 64, "kind": "supplement_text"}])
        result = self.audit(path)
        self.assertEqual([0], result["matched"], result)

    def test_a_declared_surface_absent_from_this_tree_is_not_a_missing_surface(self) -> None:
        """🔴 Two opposite causes had been wearing the same word.

        Reported by a reader who hit it on `PMID 34747138`: their checkout had no hardlink for
        the declared XML, and the script said `unauditable` — the same word it uses for a
        paper that has no structured deposit anywhere. One is a limit the reading must live
        with; the other is an errand, repaired by fetching, and it is the COMMON case, since
        anyone running from a branch other than the one that fetched the artifacts lands
        there. A reader who cannot tell them apart treats both as neither.
        """
        path = self.workspace.manifest(
            [entry("restored survival in Wwox null mice")],
            schema=2,
            artifacts=[{"path": "files/fulltext/PMID12345678_absent.xml",
                        "sha256": "a" * 64, "kind": "article_text"}])
        result = audit.audit_one(path, self.workspace.root / "nowhere")
        self.assertEqual("surface_absent_here", result["cause"])
        self.assertIn("absent from this tree", result["reason"])
        self.assertIn("not a defect in the reading", result["reason"])

    def test_a_study_with_no_structured_surface_anywhere_says_so_differently(self) -> None:
        path = self.workspace.manifest([entry("restored survival in Wwox null mice")])
        result = audit.audit_one(path, self.workspace.root / "nowhere")
        self.assertEqual("no_surface_known", result["cause"])

    def test_the_scope_note_does_not_claim_the_class_is_sealed(self) -> None:
        """The gate is real and narrower than it is tempting to say.

        `require_work_manifest` returns early for anything that is not a contemporaneous
        `complete_fulltext_read`, so partial reads, legacy reconstructions and receipt
        corrections write locators the persistence gate never sees. Calling the backlog closed
        would be exactly the over-claim this tool exists to find in other people's sentences.
        """
        self.assertIn("NOT sealed", audit.CLOSED_SET_NOTE)
        for exempted in ("partial reads", "legacy reconstructions", "receipt corrections"):
            self.assertIn(exempted, audit.CLOSED_SET_NOTE)

    def test_a_manifest_with_no_entries_owes_nothing(self) -> None:
        path = self.workspace.manifest([])
        self.assertIn("no locator entries", self.audit(path)["reason"])

    def test_the_run_summary_does_not_call_an_empty_corpus_clean(self) -> None:
        self.workspace.manifest([entry("restored fertility in Wwox null mice")])
        code = audit.main(["--root", str(self.workspace.root),
                           "--corpus", str(self.workspace.root / "nowhere"), "--strict"])
        self.assertEqual(0, code, "an unauditable corpus is not a failure, and not a pass")

    def run_main(self, *extra) -> str:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            audit.main(["--root", str(self.workspace.root), *extra])
        return buffer.getvalue()

    def test_a_declared_surface_absent_here_prints_the_corpus_hint(self) -> None:
        """HANDOFF-2 of CC-20260826-PMID36828035-DURABILITY-01.

        In a worktree `files/` is gitignored and absent, which is the normal state. The run
        used to say `unauditable` and stop; the reader then spent one failed run per worktree
        finding `--corpus`. The hint names the flag in the same output.
        """
        self.workspace.manifest(
            [entry("restored survival in Wwox null mice")],
            schema=2,
            artifacts=[{"path": "files/fulltext/PMID12345678_absent.xml",
                        "sha256": "a" * 64, "kind": "article_text"}])
        out = self.run_main("--corpus", str(self.workspace.root / "nowhere"))
        hint = [line for line in out.splitlines() if line.startswith("HINT:")]
        self.assertEqual(1, len(hint), out)
        self.assertIn("1 manifest(s) declare surfaces absent from this tree", hint[0])
        self.assertIn("--corpus", hint[0])

    def test_a_readable_corpus_with_every_surface_present_prints_no_hint(self) -> None:
        self.workspace.manifest([entry("restored survival in Wwox null mice")])
        out = self.run_main("--corpus", str(self.workspace.corpus))
        self.assertNotIn("HINT:", out)

    def test_the_hint_names_the_primary_checkout_corpus_only_when_it_exists(self) -> None:
        """A hint must never name a place that is not there; a non-repository gets the
        placeholder, not a guessed path."""
        line = audit.corpus_hint(self.workspace.root, self.workspace.root / "nowhere", 0)
        self.assertIn("no corpus at", line)
        self.assertIn("<checkout that holds files/>", line)
        self.assertEqual("", audit.corpus_hint(self.workspace.root, self.workspace.corpus, 0))

    def test_strict_fails_when_a_quote_is_not_found(self) -> None:
        self.workspace.manifest([entry("restored fertility in Wwox null mice")])
        self.assertEqual(1, audit.main(["--root", str(self.workspace.root),
                                        "--corpus", str(self.workspace.corpus), "--strict"]))
        self.assertEqual(0, audit.main(["--root", str(self.workspace.root),
                                        "--corpus", str(self.workspace.corpus)]))


class TheRealManifestsAreAudited(unittest.TestCase):
    """One real manifest through ``main`` — read, audited or declared unauditable, unchanged.

    The manifests are tracked; the text artefacts under files/ mostly are not, so on a bare
    host the manifest is *unauditable* and the run says so. Either way the tool completed a
    real read and wrote nothing; the skip fires only when the checkout has no manifest.
    """

    ROOT = Path(__file__).resolve().parents[2]
    SUMMARY = re.compile(r"^(\d+) manifest\(s\) audited, (\d+) unauditable, (\d+) quote\(s\) "
                         r"not found$", re.M)

    def test_one_real_manifest_is_read_and_left_unchanged(self) -> None:
        manifests = sorted((self.ROOT / "disease-models/wwox/research/deepdive_manifests")
                           .glob("PMID*.json"))
        if not manifests:
            self.skipTest("skipped: no deepdive manifest in this checkout")
        chosen = manifests[0]
        before = chosen.read_bytes()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = audit.main(["--root", str(self.ROOT), "--pmid", chosen.stem.removeprefix("PMID")])
        out = buffer.getvalue()
        self.assertEqual(code, 0, out)
        match = self.SUMMARY.search(out)
        self.assertIsNotNone(match, out)
        audited, unauditable, _missing = (int(g) for g in match.groups())
        self.assertEqual(audited + unauditable, 1, "--pmid must select exactly one manifest")
        self.assertIn(chosen.stem.removeprefix("PMID"), out)
        self.assertEqual(chosen.read_bytes(), before, "the audit wrote a real manifest")


class TheStrengthScanReadsWords(unittest.TestCase):
    """`--strength-scan`: advisory, read-only, exit 0. Each case is a real audit failure."""

    def flags(self, proposition, snippet, loose=False):
        return [f[0] for f in audit.strength_flags(
            {"proposition": proposition, "snippet": snippet}, loose)]

    def test_a_proposition_word_the_quote_lacks_is_flagged(self) -> None:
        """R4b: 'the clinical endpoint was null' written over a quote that never says null."""
        self.assertIn("null", self.flags(
            "the clinical endpoint was null",
            "resulting in a placebo-adjusted difference of -0.34 (-1.55, 0.87)"))

    def test_a_passing_proposition_is_not_flagged(self) -> None:
        self.assertEqual([], self.flags(
            "the median age was 75 years", "The median age for the cohort was 75 years."))

    def test_a_word_present_in_both_is_not_flagged(self) -> None:
        self.assertEqual([], self.flags(
            "the response was dose-dependent", "the response appeared dose-dependent"))

    def test_a_dropped_hedge_is_flagged(self) -> None:
        """R3c: 'plays a significant role in mediating' became 'mediates'."""
        self.assertIn("hedge-dropped", self.flags(
            "the drug mediates the protection",
            "the drug plays a significant role in mediating the protection"))

    def test_a_negation_phrase_with_its_qualifier_dropped_is_flagged(self) -> None:
        """R4b_R2b: 'no significant difference' became 'did not differ'."""
        self.assertIn("qualifier-dropped", self.flags(
            "the responder proportion did not differ by age",
            "there was no significant difference in the proportion of responders"))
        self.assertEqual([], self.flags(
            "no significant difference in responders",
            "there was no significant difference in the proportion of responders"))

    def test_the_noisy_quantifiers_need_loose(self) -> None:
        self.assertEqual([], self.flags("every bar spans zero", "the bars span zero"))
        self.assertIn("every", self.flags("every bar spans zero", "the bars span zero", loose=True))

    def test_an_entry_with_no_quote_is_reported_and_nothing_is_written(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = root / "disease-models/wwox/research/deepdive_manifests"
            directory.mkdir(parents=True)
            path = directory / "PMID12345678.json"
            path.write_text(json.dumps({"pmid": "12345678", "verbatim_locators": {"entries": [
                {"proposition": "the endpoint was null", "snippet": ""},
                {"proposition": "the endpoint was null", "snippet": "the endpoint was reached"},
                {"proposition": "x", "snippet": "[figure attestation - pixels] bars"}]}}))
            before = path.read_bytes()
            out = io.StringIO()
            with redirect_stdout(out):
                status = audit.main(["--root", str(root), "--strength-scan"])
            text = out.getvalue()
            self.assertEqual(0, status, "an advisory scan must never fail a build")
            self.assertIn("no quote", text)
            self.assertRegex(text, r"#1\s+null\s+\"null\"")
            self.assertIn("1 figure attestations and 1 entries without a quote", text)
            self.assertEqual(before, path.read_bytes(), "the scan wrote into a manifest")

    def test_every_row_names_the_audit_triple_that_justified_it(self) -> None:
        for row in audit.STRENGTH_WORDS + audit.LOOSE_WORDS:
            self.assertRegex(row[-1], r"\d{8} #\d+", row[0])


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
