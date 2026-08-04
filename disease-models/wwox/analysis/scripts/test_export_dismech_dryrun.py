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

    def test_every_exported_evidence_carries_both_receipts(self) -> None:
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        for entry in built["entries"].values():
            for node in entry["pathophysiology"]:
                for item in node["evidence"]:
                    provenance = item["_provenance"]
                    self.assertTrue(provenance["eligibility_receipt"])
                    self.assertTrue(provenance["locator_extraction_receipt"])
                    self.assertTrue(item["snippet"])

    def test_output_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "staging/a", Path(tmp) / "staging/b"
            self.assertEqual(run("--out-dir", str(first)).returncode, 0)
            self.assertEqual(run("--out-dir", str(second)).returncode, 0)
            for path in sorted(first.iterdir()):
                self.assertEqual(path.read_bytes(), (second / path.name).read_bytes(),
                                 f"{path.name} differs between runs")


class HonestEmptiness(unittest.TestCase):
    def test_an_entry_with_no_evidence_is_emitted_empty_not_omitted(self) -> None:
        """A disease that received nothing must be visible as a gap."""
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        self.assertIn("MONDO:0013687", built["entries"])
        self.assertEqual(built["entries"]["MONDO:0013687"]["pathophysiology"], [])

    def test_unassigned_assertions_are_reported_not_dropped(self) -> None:
        built, _ = exporter.build(exporter.load(exporter.SIDECAR))
        unassigned = built["report"]["unassigned_to_any_disease_entry"]
        self.assertTrue(unassigned, "molecular assertions with no disease target must surface")
        for row in unassigned:
            self.assertTrue(row["originating_claim_ids"])


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
