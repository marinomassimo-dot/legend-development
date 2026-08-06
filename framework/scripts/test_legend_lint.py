#!/usr/bin/env python3
"""Regression tests for the public structural LINT engine."""

from __future__ import annotations

import json
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fulltext_receipts  # noqa: E402
from legend_lint import (  # noqa: E402
    CURRENTS,
    RECEIPT_LEDGER,
    STATE_MANIFEST,
    _check_commit_candidate_ids,
    _check_discovery_ids,
    _check_dismissals,
    claim_paper_findings,
    lint,
    parse_corpus_ids,
    parse_ids,
)

RECEIPT_EXAMPLE = {
    "event_id": "FTR-20260725-42193054-01",
    "record_kind": "contemporaneous_receipt",
    "study_id": {"pmid": "42193054", "doi": None},
    "event_at": "2026-07-25T20:00:00Z",
    "analysis_at": "2026-07-25T19:30:00Z",
    "workflow": "test",
    "evidence_depth": "complete_fulltext_read",
    "source_locator": "PMC123",
    "source_fingerprint": None,
    "coverage": {key: "read" for key in fulltext_receipts.COVERAGE_KEYS},
    "outputs": ["dossier.md"],
    "evidence_basis": ["coverage_map"],
    "prior_receipt": None,
    "reread_reason": "first_read",
}


def make_repository(root: Path, claims: str, papers: str) -> None:
    mirror_rows = "".join(f"| {claim_id} | mirrored claim |\n" for claim_id in parse_ids(claims, "CLAIM"))
    payloads = {
        CURRENTS[0]: (
            "# Working model\nWM_v1.0\n"
            "# BLOCK 2 — claim registry mirror (baseline)\n"
            "| ID | Title |\n"
            "|---|---|\n"
            f"{mirror_rows}"
            "# BLOCK 3 — flowchart logic summary\n"
        ),
        CURRENTS[1]: claims,
        CURRENTS[2]: papers,
        CURRENTS[3]: "# Literature tracking\n",
    }
    for relative, content in payloads.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


GOOD_CLAIMS = (
    "# Claim Registry\n"
    "## CLAIM 001\n"
    "**Status:** consolidated baseline\n"
    "**Wikilinks:** [[paper_registry_current#PAPER 001]]\n"
)
GOOD_PAPERS = (
    "# Paper Registry\n"
    "## PAPER 001\n"
    "**Status:** integrated\n"
    "## CORPUS P210\n"
    "**Status:** screened\n"
)


class PublicLintTests(unittest.TestCase):
    def test_good_repository_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            make_repository(Path(temporary), GOOD_CLAIMS, GOOD_PAPERS)
            self.assertEqual(lint(temporary).verdict, "PASS")

    def test_missing_currents_block_system(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_SYSTEM")
            self.assertTrue(result.blocks_deepdive)

    def test_duplicate_and_invalid_status_block_commit(self) -> None:
        papers = GOOD_PAPERS + "## PAPER 001\n**Status:** invalid\n"
        with tempfile.TemporaryDirectory() as temporary:
            make_repository(Path(temporary), GOOD_CLAIMS, papers)
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_BATCH_COMMIT")
            self.assertFalse(result.blocks_deepdive)
            self.assertTrue(result.blocks_commit)
            self.assertTrue(any(item.code == "DUPLICATE_ID" for item in result.findings))
            self.assertTrue(any(item.code == "INVALID_STATUS" for item in result.findings))

    def test_identifier_parsers(self) -> None:
        self.assertEqual(parse_ids("## PAPER 001\n## PAPER 002\n", "PAPER"), ["001", "002"])
        self.assertEqual(parse_corpus_ids("## CORPUS P210\n"), ["210"])

    def test_claim_link_discipline(self) -> None:
        dangling = (
            "## CLAIM 001\n"
            "**Status:** consolidated baseline\n"
            "**Wikilinks:** [[paper_registry_current#PAPER 999]]\n"
        )
        findings = claim_paper_findings(dangling, {"001"}, {"210"})
        self.assertTrue(any(item.code == "DANGLING_WIKILINK" for item in findings))

        corpus = (
            "## CLAIM 002\n"
            "**Status:** consolidated baseline\n"
            "**Wikilinks:** [[paper_registry_current#CORPUS P210]]\n"
        )
        self.assertFalse(claim_paper_findings(corpus, {"001"}, {"210"}))

    def test_claim_link_to_publication_integrity_hold_blocks_batch_commit(self) -> None:
        papers = (
            "# Paper Registry\n"
            "## PAPER 001\n"
            "**Status:** integrated\n"
            "**Identifier:** PMID: 11111111\n"
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_repository(root, GOOD_CLAIMS, papers)
            registries = root / "disease-models/wwox/registries"
            (registries / "corpus_seed_pubmed_20260806.tsv").write_text(
                "pmid\tyear\tpubmed_free_full_text_link\ttype\tdoi\tcorrections\ttitle\n"
                "11111111\t2025\tyes\tprimary\t\tRetractionIn:9\tHeld paper\n",
                encoding="utf-8",
            )
            result = lint(temporary)

        self.assertEqual(result.verdict, "BLOCK_BATCH_COMMIT")
        self.assertTrue(any(
            item.code == "CLAIM_CITES_PUBLICATION_INTEGRITY_HOLD"
            for item in result.findings
        ))

    def test_ordinary_erratum_does_not_block_a_claim(self) -> None:
        papers = (
            "# Paper Registry\n"
            "## PAPER 001\n"
            "**Status:** integrated\n"
            "**Identifier:** PMID: 11111111\n"
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_repository(root, GOOD_CLAIMS, papers)
            registries = root / "disease-models/wwox/registries"
            (registries / "corpus_seed_pubmed_20260806.tsv").write_text(
                "pmid\tyear\tpubmed_free_full_text_link\ttype\tdoi\tcorrections\ttitle\n"
                "11111111\t2025\tyes\tprimary\t\tErratumIn:9\tCorrected paper\n",
                encoding="utf-8",
            )
            result = lint(temporary)

        self.assertEqual(result.verdict, "PASS")

    def test_working_model_claim_mirror_must_match_registry(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            make_repository(root, GOOD_CLAIMS, GOOD_PAPERS)
            working_model = root / CURRENTS[0]
            working_model.write_text(
                "# Working model\nWM_v1.0\n"
                "# BLOCK 2 — claim registry mirror (baseline)\n"
                "| ID | Title |\n"
                "|---|---|\n"
                "# BLOCK 3 — flowchart logic summary\n",
                encoding="utf-8",
            )
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_BATCH_COMMIT")
            self.assertTrue(
                any(item.code == "CLAIM_MISSING_FROM_MIRROR" for item in result.findings)
            )

    def test_learned_duplicate_gates(self) -> None:
        findings = []
        _check_discovery_ids(
            findings,
            "### DL-BIO-002 — lead A\n### DL-BIO-002 — duplicate\n",
        )
        self.assertTrue(any(item.code == "DUPLICATE_DISCOVERY_ID" for item in findings))

        findings = []
        _check_commit_candidate_ids(
            findings,
            "## CC-2026-07-19-001\n## CC-2026-07-19-001\n",
        )
        self.assertTrue(
            any(item.code == "DUPLICATE_COMMIT_CANDIDATE_ID" for item in findings)
        )

    def _receipt_repository(self, root: Path, papers: str, receipts_list: list[dict]) -> Path:
        """A fixture repository whose state manifest declares and anchors a receipt ledger."""
        make_repository(root, GOOD_CLAIMS, papers)
        ledger = root / RECEIPT_LEDGER
        ledger.parent.mkdir(parents=True, exist_ok=True)
        ledger.write_text("", encoding="utf-8")
        manifest = root / STATE_MANIFEST
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(
            "fulltext_ledger_path: " + RECEIPT_LEDGER + "\n"
            "fulltext_ledger_events: 0\n"
            "fulltext_ledger_head: null\n"
            "registry_only_fulltext_declarations_baseline: 0\n"
            "registry_only_fulltext_declaration_ids: []\n",
            encoding="utf-8",
        )
        complete = []
        for source_receipt in receipts_list:
            receipt = json.loads(json.dumps(source_receipt))
            receipt["source_kind"] = "fulltext_local"
            receipt["analysis_time_precision"] = "second"
            pmid = receipt["study_id"]["pmid"]
            artifact_relative = f"files/fulltext/PMID{pmid}.xml"
            artifact = root / artifact_relative
            artifact.parent.mkdir(parents=True, exist_ok=True)
            quote = "a verbatim sentence long enough to be a real locator"
            artifact.write_text(
                f"<article><body><p>{quote}</p></body></article>", encoding="utf-8")
            digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
            receipt["source_locator"] = artifact_relative
            receipt["source_fingerprint"] = digest

            manifest_dir = root / "disease-models/wwox/research/deepdive_manifests"
            manifest_dir.mkdir(parents=True, exist_ok=True)
            work_manifest = {
                "schema_version": 2,
                "pmid": pmid,
                "receipt": receipt["event_id"],
                "source_artifacts": [{
                    "path": artifact_relative, "sha256": digest, "kind": "article_text"}],
                "group_assessment": {
                    "total_publications": 10,
                    "publications_on_gene": 2,
                    "research_type": "experimental_lab",
                    "is_primary_group_for_disease": False,
                    "weighting": "Observation and interpretation are weighted separately for this test fixture.",
                },
                "field_density": {
                    "queries": [{"query": "gene AND mechanism", "count": 2}],
                    "verdict": "sparse test intersection",
                },
                "multihop": {"gene_direct_refs_in_source": [], "resolved": [], "queued": [],
                             "references_enumerated": 12},
                "corpus_crossquery": {"query": "mechanism", "hits": 1, "verdict": "represented"},
                "retraction_check": {"method": "test fixture", "result": "none"},
                "verbatim_locators": {"source_fulltext_indexed": True, "entries": [{
                    "proposition": "fixture proposition",
                    "snippet": quote,
                    "surface": "body",
                    "artifact": artifact_relative,
                    "anchor": "Results, Fig. 1"}]},
                "landing": ["DL-MECH-001"],
                "skills_considered": [{"skill": "find-fulltext", "used": True}],
            }
            (manifest_dir / f"PMID{pmid}.json").write_text(
                json.dumps(work_manifest), encoding="utf-8")
            fulltext_receipts.append_receipt(ledger, receipt)
            if receipt.get("evidence_depth") == "complete_fulltext_read":
                complete.append(receipt)

        landing = root / "disease-models/wwox/research/discovery_ledger_current.md"
        landing.parent.mkdir(parents=True, exist_ok=True)
        sections = []
        for index, receipt in enumerate(complete, start=1):
            pmid = receipt["study_id"]["pmid"]
            sections.append(f"### DL-MECH-{index:03d} — test landing\nPMID {pmid}\n")
            for output in receipt.get("outputs") or []:
                if output.endswith(".md"):
                    target = root / output
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(f"# Output for PMID {pmid}\n", encoding="utf-8")
        landing.write_text("\n".join(sections) or "# No complete reads\n", encoding="utf-8")
        return ledger

    def test_self_evaluation_failures_reach_lint_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._receipt_repository(root, GOOD_PAPERS, [RECEIPT_EXAMPLE])
            (root / "disease-models/wwox/research/discovery_ledger_current.md").write_text(
                "### Process note\nPMID 42193054 is not landed.\n", encoding="utf-8"
            )
            result = lint(temporary)
            self.assertEqual("BLOCK_BATCH_COMMIT", result.verdict)
            self.assertTrue(any(item.code == "ORPHAN_COMPLETE_READ" for item in result.findings))

    def test_declared_but_absent_receipt_ledger_blocks_the_system(self) -> None:
        """A reading history that cannot be produced is worse than none: recover, don't proceed."""
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            ledger = self._receipt_repository(root, GOOD_PAPERS, [RECEIPT_EXAMPLE])
            self.assertEqual(lint(temporary).verdict, "PASS")
            ledger.unlink()
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_SYSTEM")
            self.assertTrue(
                any(item.code == "RECEIPT_LEDGER_MISSING" for item in result.findings)
            )

    def test_rewritten_receipt_history_blocks_the_system(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            second = dict(RECEIPT_EXAMPLE)
            second["event_id"] = "FTR-20260725-42193054-02"
            second["prior_receipt"] = RECEIPT_EXAMPLE["event_id"]
            second["reread_reason"] = "adversarial_reanalysis"
            ledger = self._receipt_repository(root, GOOD_PAPERS, [RECEIPT_EXAMPLE, second])
            lines = ledger.read_text(encoding="utf-8").splitlines()
            record = json.loads(lines[0])
            record["workflow"] = "rewritten-after-the-fact"
            lines[0] = json.dumps(record, ensure_ascii=False, sort_keys=True)
            ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_SYSTEM")
            self.assertTrue(
                any(
                    item.code == "RECEIPT_LEDGER_HISTORY_UNTRUSTED"
                    for item in result.findings
                )
            )

    def test_truncated_receipt_tail_blocks_the_system(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            second = dict(RECEIPT_EXAMPLE)
            second["event_id"] = "FTR-20260725-42193054-02"
            second["prior_receipt"] = RECEIPT_EXAMPLE["event_id"]
            second["reread_reason"] = "adversarial_reanalysis"
            ledger = self._receipt_repository(root, GOOD_PAPERS, [RECEIPT_EXAMPLE, second])
            lines = ledger.read_text(encoding="utf-8").splitlines()
            ledger.write_text(lines[0] + "\n", encoding="utf-8")
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_SYSTEM")
            self.assertTrue(
                any(
                    item.code == "RECEIPT_LEDGER_ANCHOR_MISMATCH"
                    for item in result.findings
                )
            )

    def test_new_unbacked_fulltext_declaration_blocks_commit(self) -> None:
        """The ratchet: history is grandfathered by count, new declarations are not."""
        backed = (
            "# Paper Registry\n"
            "## PAPER 001\n"
            "**Status:** integrated\n"
            "**Identifier:** PMID: 42193054\n"
            "**Evidence depth:** full text reviewed\n"
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._receipt_repository(root, backed, [RECEIPT_EXAMPLE])
            self.assertEqual(lint(temporary).verdict, "PASS")

        unbacked = backed + (
            "## PAPER 002\n"
            "**Status:** integrated\n"
            "**Identifier:** PMID: 11111111\n"
            "**Evidence depth:** full text reviewed\n"
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._receipt_repository(root, unbacked, [RECEIPT_EXAMPLE])
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_BATCH_COMMIT")
            self.assertTrue(
                any(
                    item.code == "UNBACKED_FULLTEXT_DECLARATION"
                    for item in result.findings
                )
            )

    def test_grandfathered_declaration_cannot_be_exchanged_one_for_one(self) -> None:
        """A count-only ratchet misses substitution; identities must be frozen too."""
        papers = (
            "# Paper Registry\n"
            "## PAPER 001\n**Status:** integrated\n"
            "**Identifier:** PMID: 11111111\n"
            "## PAPER 002\n**Status:** integrated\n"
            "**Identifier:** PMID: 22222222\n"
            "**Evidence depth:** full text reviewed\n"
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._receipt_repository(root, papers, [])
            manifest = root / STATE_MANIFEST
            text = manifest.read_text(encoding="utf-8")
            text = text.replace(
                "registry_only_fulltext_declarations_baseline: 0\n"
                "registry_only_fulltext_declaration_ids: []",
                "registry_only_fulltext_declarations_baseline: 1\n"
                'registry_only_fulltext_declaration_ids: ["PAPER 001"]',
            )
            manifest.write_text(text, encoding="utf-8")
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_BATCH_COMMIT")
            self.assertTrue(
                any(item.code == "UNBACKED_FULLTEXT_DECLARATION" for item in result.findings)
            )

    def test_receipt_manifest_fields_are_unique_and_path_is_authoritative(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._receipt_repository(root, GOOD_PAPERS, [])
            manifest = root / STATE_MANIFEST
            manifest.write_text(
                manifest.read_text(encoding="utf-8")
                + "fulltext_ledger_events: 0\nfulltext_ledger_head: null\n",
                encoding="utf-8",
            )
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_SYSTEM")
            self.assertTrue(
                any(item.code == "RECEIPT_LEDGER_ANCHOR_MISMATCH" for item in result.findings)
            )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._receipt_repository(root, GOOD_PAPERS, [])
            manifest = root / STATE_MANIFEST
            manifest.write_text(
                manifest.read_text(encoding="utf-8").replace(
                    RECEIPT_LEDGER, "disease-models/wwox/registries/other.jsonl"
                ),
                encoding="utf-8",
            )
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_SYSTEM")
            self.assertTrue(
                any(item.code == "RECEIPT_LEDGER_PATH_INVALID" for item in result.findings)
            )

    def test_missing_ratchet_configuration_blocks_commit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._receipt_repository(root, GOOD_PAPERS, [])
            manifest = root / STATE_MANIFEST
            manifest.write_text(
                "\n".join(
                    line
                    for line in manifest.read_text(encoding="utf-8").splitlines()
                    if not line.startswith("registry_only_fulltext_declaration")
                )
                + "\n",
                encoding="utf-8",
            )
            result = lint(temporary)
            self.assertEqual(result.verdict, "BLOCK_BATCH_COMMIT")
            self.assertTrue(
                any(item.code == "RECEIPT_RATCHET_UNDECLARED" for item in result.findings)
            )

    def test_repository_without_a_declared_ledger_is_unaffected(self) -> None:
        """The gate binds instances that declare a ledger; it does not invent one."""
        with tempfile.TemporaryDirectory() as temporary:
            make_repository(Path(temporary), GOOD_CLAIMS, GOOD_PAPERS)
            self.assertEqual(lint(temporary).verdict, "PASS")

    def test_negative_premise_gate(self) -> None:
        findings = []
        _check_dismissals(
            findings,
            "### DIS-001 — rejection\n- Verdict: active\n",
        )
        self.assertTrue(any(item.code == "DISMISSAL_WITHOUT_PREMISE" for item in findings))

        findings = []
        _check_dismissals(
            findings,
            "### DIS-002 — rejection\n"
            "- PREMISE: DEFAULT_FROM_TEXTBOOK\n"
            "- REVIVAL_TRIGGER: reopen if direct evidence appears\n",
        )
        self.assertFalse(findings)


if __name__ == "__main__":
    unittest.main()
