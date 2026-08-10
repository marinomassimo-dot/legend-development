#!/usr/bin/env python3
"""Regressions for the mechanical locator audit.

The script answers one question — does this quote occur in the artifact it was taken from —
for the manifests `deepdive_manifest --verify-artifacts` cannot reach. These tests keep it
answering that question and not a nearby one.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
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

    def test_a_manifest_with_no_entries_owes_nothing(self) -> None:
        path = self.workspace.manifest([])
        self.assertIn("no locator entries", self.audit(path)["reason"])

    def test_the_run_summary_does_not_call_an_empty_corpus_clean(self) -> None:
        self.workspace.manifest([entry("restored fertility in Wwox null mice")])
        code = audit.main(["--root", str(self.workspace.root),
                           "--corpus", str(self.workspace.root / "nowhere"), "--strict"])
        self.assertEqual(0, code, "an unauditable corpus is not a failure, and not a pass")

    def test_strict_fails_when_a_quote_is_not_found(self) -> None:
        self.workspace.manifest([entry("restored fertility in Wwox null mice")])
        self.assertEqual(1, audit.main(["--root", str(self.workspace.root),
                                        "--corpus", str(self.workspace.corpus), "--strict"]))
        self.assertEqual(0, audit.main(["--root", str(self.workspace.root),
                                        "--corpus", str(self.workspace.corpus)]))


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
