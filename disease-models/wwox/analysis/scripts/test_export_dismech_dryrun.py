#!/usr/bin/env python3
"""Regressions for the Phase-3 dry run.

Every test here asserts a refusal. An exporter that produces plausible YAML when a rule is
violated is worse than one that produces none, because the output looks reviewable.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "export_dismech_dryrun.py"
SPEC = importlib.util.spec_from_file_location("exporter", SCRIPT)
exporter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(exporter)


def run(*arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *arguments],
                          capture_output=True, text=True)


def occurrence(**overrides) -> dict:
    row = {
        "record_kind": "assertion_occurrence", "occurrence_id": "OCC-test",
        "claim_id": "016", "pmid": "22193544", "source_id": "PAPER 056",
        "proposition": "P", "context": "in vitro pull-down",
        "epistemic_type": "DATO", "evidence_relation": "SUPPORT",
        "terminal_state": "ELIGIBLE_FOR_EXPORT", "evidence_assertion_id": "EA-test",
        "eligibility_receipt_event": "FTR-a", "locator_extraction_receipt_event": "FTR-b",
        "locator": {"snippet": "a verbatim sentence", "anchor": "Results, Fig. 1"},
    }
    row.update(overrides)
    return row


class WriteBoundary(unittest.TestCase):
    def test_refuses_to_write_outside_staging(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = run("--out-dir", tmp)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("staging", result.stderr + result.stdout)


class SchemaPin(unittest.TestCase):
    def test_wrong_pin_is_refused(self) -> None:
        result = run("--out-dir", "staging/_test_pin", "--schema-sha", "deadbeef")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("schema pin mismatch", result.stderr + result.stdout)

    def test_unasserted_pin_is_declared_not_assumed(self) -> None:
        """Silence about verification must not read as verification."""
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "staging" / "run"
            result = run("--out-dir", str(out))
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads((out / "loss_report.json").read_text())
        self.assertFalse(report["schema_pin"]["verified_at_run_time"])
        self.assertEqual(report["run_status"], "DRY_RUN_SCHEMA_UNVERIFIED")


class EpistemicRules(unittest.TestCase):
    def test_inference_exported_as_support_is_refused(self) -> None:
        """Rule F1: an INFERENZA may support PARTIALLY, never as direct support."""
        records = [occurrence(epistemic_type="INFERENZA", evidence_relation="SUPPORT")]
        with self.assertRaises(SystemExit) as caught:
            exporter.build(records)
        self.assertIn("Rule F1", str(caught.exception))

    def test_eligible_without_a_snippet_is_refused(self) -> None:
        records = [occurrence(locator={"snippet": None})]
        with self.assertRaises(SystemExit):
            exporter.build(records)

    def test_confidence_is_never_omitted(self) -> None:
        """Rule E2: the pinned schema reads absence as ESTABLISHED."""
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        nodes = [n for e in built["entries"].values() for n in e["pathophysiology"]]
        self.assertTrue(nodes)
        for node in nodes:
            self.assertIn("mechanism_confidence", node)
            self.assertIn(node["mechanism_confidence"],
                          {"ESTABLISHED", "PROVISIONAL", "HYPOTHETICAL"})

    def test_single_source_is_never_established(self) -> None:
        """Rule E1."""
        confidence, criteria = exporter.confidence_for([occurrence()])
        self.assertNotEqual(confidence, "ESTABLISHED")
        self.assertFalse(criteria["at_least_two_complete_read_sources"])

    def test_unassessed_criteria_are_not_read_as_satisfied(self) -> None:
        """A criterion nobody assessed is None, and None must not pass as true."""
        _confidence, criteria = exporter.confidence_for([occurrence(), occurrence(source_id="X")])
        self.assertIsNone(criteria["sources_independent"])
        self.assertNotEqual(exporter.confidence_for(
            [occurrence(), occurrence(source_id="X")])[0], "ESTABLISHED")


class OutputDiscipline(unittest.TestCase):
    def test_no_modifier_is_emitted(self) -> None:
        """Rule C2: no occurrence records a signed direction, so none may be invented."""
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        text = json.dumps(built["entries"])
        self.assertNotIn('"modifier"', text)

    def test_no_conforms_to_is_emitted(self) -> None:
        """Rule M1: every candidate module is UNASSESSED."""
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        self.assertNotIn('"conforms_to"', json.dumps(built["entries"]))

    def test_every_occurrence_is_accounted_for(self) -> None:
        """Identity A: exported plus classified equals enumerated."""
        records = exporter.load(exporter.SIDECAR)
        built, losses = exporter.build(records)
        total = len([r for r in records if r["record_kind"] == "assertion_occurrence"])
        ledger_a = [l for l in losses if l["kind"] == "ledger_a"]
        self.assertEqual(built["report"]["eligible"] + len(ledger_a), total)

    def test_every_exported_evidence_carries_a_snippet(self) -> None:
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        for entry in built["entries"].values():
            for node in entry["pathophysiology"]:
                for item in node["evidence"]:
                    self.assertTrue(item["snippet"])

    def test_provenance_travels_beside_the_entry_not_inside_it(self) -> None:
        """The schema has no provenance slot; inventing one produces YAML a reader ignores.

        Losing the receipt lineage to satisfy the schema would discard the one thing this
        pipeline carries, so it moves to a companion file rather than disappearing.
        """
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        for entry in built["entries"].values():
            for node in entry["pathophysiology"]:
                for key in node:
                    self.assertFalse(key.startswith("_"),
                                     f"non-schema key {key!r} left inside the entry")
                for item in node["evidence"]:
                    for key in item:
                        self.assertFalse(key.startswith("_"))
        self.assertTrue(built["provenance"])
        for row in built["provenance"]:
            self.assertTrue(row["eligibility_receipt"])
            self.assertTrue(row["locator_extraction_receipt"])
            self.assertTrue(row["occurrence_id"])

    def test_confidence_criteria_are_recorded_beside_the_entry(self) -> None:
        """Rule E1's justification must survive even though the schema cannot hold it."""
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        self.assertTrue(built["confidence"])
        for row in built["confidence"]:
            self.assertIn("criteria", row)
            self.assertIn(row["mechanism_confidence"],
                          {"ESTABLISHED", "PROVISIONAL", "HYPOTHETICAL"})

    def test_output_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "staging/a", Path(tmp) / "staging/b"
            self.assertEqual(run("--out-dir", str(first)).returncode, 0)
            self.assertEqual(run("--out-dir", str(second)).returncode, 0)
            for path in sorted(first.iterdir()):
                self.assertEqual(path.read_bytes(), (second / path.name).read_bytes(),
                                 f"{path.name} differs between runs")


class HonestEmptiness(unittest.TestCase):
    """These test the behaviour, not the current routing.

    An earlier version asserted that SCAR12 was empty and that assertions were unassigned.
    Both were true of the data at the time and neither was a rule; when the routing changed
    on evidence, the tests failed for the wrong reason. A test that breaks when data
    legitimately changes was testing the data.
    """

    def test_every_declared_target_appears_even_with_no_nodes(self) -> None:
        """A disease that receives nothing must be visible as a gap, not omitted."""
        original = exporter.CLAIM_TARGETS
        exporter.CLAIM_TARGETS = {k: ["MONDO:0014533"] for k in original}
        try:
            built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        finally:
            exporter.CLAIM_TARGETS = original
        self.assertIn("MONDO:0013687", built["entries"])
        self.assertEqual(built["entries"]["MONDO:0013687"]["pathophysiology"], [])

    def test_unassigned_assertions_are_reported_not_dropped(self) -> None:
        original = exporter.CLAIM_TARGETS
        exporter.CLAIM_TARGETS = dict.fromkeys(original, [])
        try:
            built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        finally:
            exporter.CLAIM_TARGETS = original
        unassigned = built["report"]["unassigned_to_any_disease_entry"]
        self.assertTrue(unassigned, "assertions with no disease target must surface")
        self.assertEqual(sum(len(e["pathophysiology"]) for e in built["entries"].values()), 0)
        for row in unassigned:
            self.assertTrue(row["originating_claim_ids"])

    def test_routing_states_whether_its_own_basis_is_backed_by_a_receipt(self) -> None:
        """The routing must declare the standing of the claims that license it.

        This asserted `basis_is_exportable is False` until 2026-08-04 — a hardcoded constant
        that was true when written and stopped being true the moment PAPER 018 and PAPER 015
        reached `complete_fulltext_read`, without anything failing. That is precisely what
        this class's docstring warns against, committed inside the class itself. The value is
        now measured from the receipt ledger and the test checks the contract: whichever way
        it comes out, the report must say so and must justify it.
        """
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        justification = built["report"]["routing_justification"]
        self.assertTrue(any("CLAIM 008" in b for b in justification["basis"]))
        self.assertIn("basis_receipts", justification)
        if justification["basis_is_exportable"]:
            self.assertTrue(justification["basis_receipts"],
                            "an exportable basis must name the receipts backing it")
            self.assertNotIn("basis_blocked_by", justification)
        else:
            self.assertFalse(justification["basis_receipts"])
            self.assertTrue(justification["basis_blocked_by"],
                            "a blocked basis must name what blocks it")
        self.assertTrue(justification["consequence"])

    def test_routing_basis_is_measured_from_the_ledger_not_asserted(self) -> None:
        """Point it at a ledger with no complete read and it must report blocked."""
        with tempfile.TemporaryDirectory() as tmp:
            empty = Path(tmp) / "ledger.jsonl"
            empty.write_text(json.dumps({
                "event_id": "FTR-TEST-36779245-01",
                "study_id": {"pmid": "36779245"},
                "evidence_depth": "partial_fulltext_read"}) + "\n", encoding="utf-8")
            justification = exporter.routing_justification(empty)
        self.assertFalse(justification["basis_is_exportable"])
        self.assertTrue(justification["basis_blocked_by"])
        self.assertFalse(justification["basis_receipts"])

    def test_attachments_are_counted_separately_from_assertions(self) -> None:
        """A shared proposition attaches once per entry; the two counts must not be equated."""
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        report = built["report"]
        emitted = sum(len(e["pathophysiology"]) for e in built["entries"].values())
        self.assertEqual(report["node_evidence_attachments"], emitted)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
