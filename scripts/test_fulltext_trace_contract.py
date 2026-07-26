#!/usr/bin/env python3
"""Regression contract: no full-text analysis route may be memoryless."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKEN = "FULLTEXT_READ_RECEIPT"
ROUTE_REGISTRY = "framework/config/fulltext_route_registry.json"
VALID_POLICIES = {
    "complete_analysis",
    "non_exhaustive",
    "retrieval_only",
    "receipt_reuse_only",
    "not_applicable",
}


class FulltextTraceContractTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_normative_layers_make_receipts_universal(self) -> None:
        for relative in ("AGENTS.md", "CLAUDE.md", "framework/instruction/LEGEND_CORE.md"):
            self.assertIn(TOKEN, self.read(relative), relative)

    def test_normative_write_rules_name_the_append_only_carveout(self) -> None:
        for relative in (
            "CLAUDE.md",
            "framework/instruction/LEGEND_CORE.md",
            "framework/state/state_manifest_current.md",
        ):
            text = self.read(relative).lower()
            self.assertIn("state-control", text, relative)
            self.assertIn("append-only", text, relative)
            self.assertIn("carve-out", text, relative)

    def test_every_analysis_surface_returns_a_receipt(self) -> None:
        registry = json.loads(self.read(ROUTE_REGISTRY))
        analysis_surfaces = [
            relative for relative, policy in registry.items() if policy == "complete_analysis"
        ]
        missing = [relative for relative in analysis_surfaces if TOKEN not in self.read(relative)]
        self.assertFalse(missing, f"analysis routes without a durable read receipt: {missing}")

    def test_analysis_surfaces_name_the_persistence_obligation(self) -> None:
        """Naming the token is not the contract; naming who makes it durable is.

        A route may mention `FULLTEXT_READ_RECEIPT` in passing and still leave the reader
        believing that emitting one into chat closed the reading debt. It does not: an
        unpersisted receipt is indistinguishable from no receipt at the next session.
        """
        registry = json.loads(self.read(ROUTE_REGISTRY))
        for relative, policy in registry.items():
            if policy != "complete_analysis":
                continue
            text = self.read(relative).lower()
            self.assertTrue(
                "persist" in text,
                f"{relative} returns a receipt without naming who persists it",
            )

    def test_the_persisting_route_names_the_executable(self) -> None:
        """An obligation with no named mechanism is a wish.

        The orchestrator is the surface that actually appends to the ledger, so it is the
        one place that must carry the command — including the fact that hand-editing the
        ledger breaks its hash chain rather than quietly succeeding.
        """
        text = self.read(".claude/skills/legend/SKILL.md")
        self.assertIn("framework/scripts/fulltext_receipts.py", text)
        self.assertIn("record --receipt", text)
        self.assertIn("ANALYSIS_DONE_RECEIPT_NOT_PERSISTED", text)

    def test_append_only_guarantee_is_documented_with_its_limit(self) -> None:
        """Publishing an integrity claim without its boundary is the overclaim this repo polices."""
        text = self.read("framework/protocols/fulltext_read_receipt.md")
        for phrase in ("ledger_prev_hash", "fulltext_ledger_head", "honest limit"):
            self.assertIn(phrase, text)

    def test_retrieval_and_rag_cannot_masquerade_as_complete_reading(self) -> None:
        registry = json.loads(self.read(ROUTE_REGISTRY))
        for relative, policy in registry.items():
            if policy not in {"non_exhaustive", "retrieval_only"}:
                continue
            text = self.read(relative)
            self.assertIn(TOKEN, text, relative)
            required_state = (
                "retrieved_not_read" if policy == "retrieval_only" else "queried_not_full_read"
            )
            self.assertIn(required_state, text, f"{relative} does not name {required_state}")

    def test_every_skill_and_agent_route_is_explicitly_classified(self) -> None:
        registry = json.loads(self.read(ROUTE_REGISTRY))
        discovered = {
            str(path.relative_to(ROOT))
            for path in [
                *ROOT.glob(".claude/skills/*/SKILL.md"),
                *ROOT.glob(".claude/agents/*.md"),
            ]
        }
        self.assertEqual(discovered, set(registry), "route registry is incomplete or stale")
        self.assertFalse(set(registry.values()) - VALID_POLICIES)

    def test_receipt_reuse_routes_cannot_silently_reread(self) -> None:
        registry = json.loads(self.read(ROUTE_REGISTRY))
        for relative, policy in registry.items():
            if policy != "receipt_reuse_only":
                continue
            text = self.read(relative)
            self.assertIn(TOKEN, text, relative)
            self.assertIn("prior_receipt", text, relative)

    def test_protocol_requires_preflight_persistence_and_reread_reason(self) -> None:
        text = self.read("framework/protocols/fulltext_read_receipt.md")
        for phrase in (
            "duplicate-work gate",
            "before closing the turn",
            "reread_reason",
            "prior_receipt",
            "ANALYSIS_DONE_RECEIPT_NOT_PERSISTED",
        ):
            self.assertIn(phrase, text)

    def test_machine_schema_has_identity_depth_coverage_and_lineage(self) -> None:
        schema = json.loads(self.read("framework/schemas/fulltext_read_receipt.schema.json"))
        required = set(schema["required"])
        self.assertTrue(
            {"study_id", "evidence_depth", "coverage", "prior_receipt", "reread_reason"}
            <= required
        )
        self.assertTrue({"record_kind", "analysis_at", "evidence_basis"} <= required)
        self.assertEqual(
            set(schema["properties"]["record_kind"]["enum"]),
            {"contemporaneous_receipt", "legacy_reconstruction"},
        )
        depths = set(schema["properties"]["evidence_depth"]["enum"])
        self.assertEqual(
            depths,
            {
                "retrieved_not_read",
                "queried_not_full_read",
                "abstract_only",
                "partial_fulltext_read",
                "complete_fulltext_read",
            },
        )
        self.assertEqual(len(schema["properties"]["coverage"]["required"]), 9)
        coverage_states = set(schema["$defs"]["coverageState"]["enum"])
        self.assertIn("unknown_legacy", coverage_states)
        # Ledger-managed, so declared but deliberately not required of an authored receipt.
        self.assertIn("ledger_prev_hash", schema["properties"])
        self.assertNotIn("ledger_prev_hash", required)

    def test_active_receipts_never_name_an_output_that_cannot_ship(self) -> None:
        """A shipped receipt may not promise a file the public edition excludes.

        The ledger ships; `staging/`, `files/` and `backup/` never do. On 2026-07-26 three
        active receipts named their staging drafts as outputs, so a fresh clone opened with
        four `UNRESOLVED_OUTPUT_FILE` blocks — the repository shipped a reading history that
        pointed at nothing, and the first command in the README returned BLOCK instead of the
        PASS it promises. The remedy is not a softer checker: after a BATCH_COMMIT a reading
        lives in the canonical registries, so that is what its receipt must name. Superseded
        receipts are exempt by design — history is corrected by appending, never by rewriting.
        """
        ledger = ROOT / "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
        receipts = [
            json.loads(line)
            for line in ledger.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        corrected = {r.get("prior_receipt") for r in receipts if r.get("prior_receipt")}
        unshippable = ("staging/", "files/", "backup/", "tmp/", "overlay/", "_qa/")
        offenders = [
            f"{r['event_id']}: {output}"
            for r in receipts
            if r["event_id"] not in corrected
            for output in r.get("outputs") or []
            if any(root in output for root in unshippable)
        ]
        self.assertEqual(
            [],
            offenders,
            "Active receipts name outputs under a private root that never ships:\n"
            + "\n".join(offenders),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
