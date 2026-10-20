#!/usr/bin/env python3
"""Offline regression cases: synthetic entities, no biological or live API validation."""
import copy
import importlib.util
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from repurposing_bridge import build_card, normalise_label_lookup, normalise_p4_fields

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "kg_thin_slice", ROOT / ".claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py")
kg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kg)


def packet():
    context = {key: "synthetic" for key in (
        "disease_id", "genotype", "species", "cell_type", "developmental_stage")}
    row = {"id": "disease-1", "target_id": "TEST:target", "endpoint": "activity",
           "direction": "INCREASE", "source": "synthetic-fixture", "locator": "row 1",
           "epistemic_status": "IPOTESI", "reading_depth": "UNKNOWN", "context": context}
    drug = copy.deepcopy(row)
    drug.update(id="drug-1", direction="DECREASE")
    return {"schema_version": 1, "route": "BENEFICIO_PRECOCE",
            "candidate": {"id": "TEST:drug", "name": "Synthetic compound"},
            "disease_assertion": row, "drug_assertions": [drug],
            "evidence_against": ["Synthetic counterevidence"], "engine_score": 0.8}


class BridgeTests(unittest.TestCase):
    def test_opposition_is_only_hypothesis_and_preserves_packet(self):
        data = packet()
        data["drug_assertions"][0]["relation_assertions"] = [
            {"source": "source-a", "relation": "INHIBITOR"},
            {"source": "source-b", "relation": "TARGET"}]
        original = copy.deepcopy(data)
        card = build_card(data)
        self.assertEqual(card["directional_summary"], "OPPOSES_DISEASE_CHANGE")
        self.assertEqual(card["epistemic_status"], "IPOTESI")
        self.assertFalse(card["canonical"])
        self.assertEqual(card["translation"]["functional_rescue"], "UNKNOWN")
        self.assertEqual(card["input"], original)
        self.assertEqual(data, original)
        self.assertEqual(card, build_card(data))
        self.assertNotIn("relation_conflict", card["input"]["drug_assertions"][0])
        data["route"] = "RECUPERO_PROFONDO"
        self.assertEqual(build_card(data)["input"]["route"], "RECUPERO_PROFONDO")

    def test_unknown_mismatch_empty_and_conflicting_sources(self):
        for dimension in ("direction", "target_id", "endpoint", "cell_type", "genotype"):
            data = packet()
            row = data["drug_assertions"][0]
            (row["context"] if dimension in {"cell_type", "genotype"} else row)[dimension] = "UNKNOWN"
            with self.subTest(dimension=dimension):
                self.assertEqual(build_card(data)["directional_summary"], "UNRESOLVED")
        data = packet()
        second = copy.deepcopy(data["drug_assertions"][0])
        second.update(id="drug-2", direction="INCREASE", source="same-shared-source")
        data["drug_assertions"].append(second)
        self.assertEqual(build_card(data)["directional_summary"], "CONFLICTING")
        data["drug_assertions"] = []
        self.assertEqual(build_card(data)["assessment"], "REQUIRES_QUALIFICATION")

    def test_invalid_packets_and_unbacked_read_declarations_fail(self):
        for mutate in (
            lambda p: p.update(route="clinical"),
            lambda p: p["disease_assertion"].update(direction="inhibitor"),
            lambda p: p["disease_assertion"].update(source=""),
            lambda p: p["disease_assertion"].update(reading_depth="complete_fulltext_read"),
            lambda p: p["drug_assertions"][0].update(id="disease-1"),
        ):
            data = packet()
            mutate(data)
            with self.assertRaises(ValueError):
                build_card(data)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(json.dumps(packet()))
            run = subprocess.run([sys.executable, str(ROOT / "framework/scripts/repurposing_bridge.py"), str(path)],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(run.stdout), build_card(packet()))

    def test_label_lookup_states_stay_four_different_facts(self):
        absent = build_card(packet())
        self.assertEqual(absent["label_lookup"]["status"], "NOT_ATTEMPTED")
        self.assertEqual(absent["label_lookup"]["coverage"], "UNKNOWN")
        self.assertEqual(absent["label_lookup"]["queries"], [])
        self.assertTrue(any("not NO_MATCH_FOUND" in line for line in absent["limits"]))

        empty_response = packet()
        empty_response["label_lookup"] = {
            "status": "NO_MATCH_FOUND", "queries": ["synthetic-generic", "synthetic-brand"],
            "source": "synthetic-archive", "retrieved_at": "2026-10-20",
            "client_version": "fixture-0", "method": "primary_then_alternative"}
        card = build_card(empty_response)
        self.assertEqual(card["label_lookup"]["status"], "NO_MATCH_FOUND")
        self.assertEqual(card["label_lookup"]["coverage"], "UNKNOWN")
        self.assertTrue(any("not proof the label is absent" in line for line in card["limits"]))
        # An outcome never moves the directional comparison, and never drops the candidate.
        self.assertEqual(card["directional_summary"], absent["directional_summary"])
        self.assertEqual(card["assessment"], absent["assessment"])
        self.assertEqual(card["comparisons"], absent["comparisons"])

        failed = copy.deepcopy(empty_response)
        failed["label_lookup"].update(status="QUERY_ERROR", error="HTTP 503 from fixture")
        self.assertTrue(any("never a concluded one" in line
                            for line in build_card(failed)["limits"]))
        self.assertNotEqual(build_card(failed)["label_lookup"]["status"],
                            card["label_lookup"]["status"])

        # Coverage is a second axis: NO_MATCH_FOUND with incomplete coverage is legal.
        truncated = copy.deepcopy(empty_response)
        truncated["label_lookup"].update(coverage="COVERAGE_INCOMPLETE",
                                         coverage_limit="alternative search unavailable")
        both = build_card(truncated)["label_lookup"]
        self.assertEqual((both["status"], both["coverage"]),
                         ("NO_MATCH_FOUND", "COVERAGE_INCOMPLETE"))

        matched = copy.deepcopy(empty_response)
        matched["label_lookup"].update(status="MATCH_FOUND", spl_id="SPL-FIXTURE-1")
        self.assertTrue(any("certifies neither" in line
                            for line in build_card(matched)["limits"]))

        for bad in (
            {"status": "DRUG_HAS_NO_LABEL"},
            {"status": "NOT_ATTEMPTED", "queries": ["x"]},
            {"status": "NO_MATCH_FOUND", "queries": []},
            {"status": "MATCH_FOUND", "queries": ["x"]},
            {"status": "QUERY_ERROR", "queries": ["x"]},
            {"status": "NO_MATCH_FOUND", "queries": ["x"], "coverage": "COVERAGE_INCOMPLETE"},
            {"status": "NO_MATCH_FOUND", "queries": ["x"], "coverage": "PARTIAL"},
            {"status": "NO_MATCH_FOUND", "queries": ["x"], "lookup_score": "0.9"},
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                normalise_label_lookup(bad)

    def test_later_p4_fields_are_present_and_unknown_not_absent(self):
        card = build_card(packet())
        fields = card["p4_fields"]
        self.assertEqual(fields["endpoint_pursued"], "UNKNOWN")
        self.assertEqual(fields["functional_evidence_available"], "UNKNOWN")
        self.assertEqual(fields["temporal_or_model_limit"], "UNKNOWN")
        self.assertEqual(set(fields["cellular_context"]),
                         {"target_expression", "cells_tissue_stage", "coverage", "limits"})
        self.assertEqual(set(fields["cellular_context"].values()), {"UNKNOWN"})

        data = packet()
        data["p4_fields"] = {"endpoint_pursued": "synthetic excitability readout",
                             "cellular_context": {"cells_tissue_stage": "synthetic stage"}}
        filled = build_card(data)["p4_fields"]
        self.assertEqual(filled["endpoint_pursued"], "synthetic excitability readout")
        self.assertEqual(filled["functional_evidence_available"], "UNKNOWN")
        self.assertEqual(filled["cellular_context"]["cells_tissue_stage"], "synthetic stage")
        self.assertEqual(filled["cellular_context"]["target_expression"], "UNKNOWN")
        # A declared P4 field is never allowed to become a score or a ranking input.
        for bad in ({"endpoint_pursued": ""}, {"endpoint_weight": "0.5"},
                    {"cellular_context": {"selectivity": "x"}}, {"cellular_context": "x"}):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                normalise_p4_fields(bad)

    def test_empty_assertion_list_is_an_abstention_not_an_empty_lookup(self):
        data = packet()
        data["drug_assertions"] = []
        card = build_card(data)
        self.assertEqual(card["abstention"], "NO_DRUG_ASSERTIONS_SUPPLIED")
        self.assertEqual(card["directional_summary"], "UNRESOLVED")
        self.assertEqual(card["label_lookup"]["status"], "NOT_ATTEMPTED")
        self.assertIsNone(build_card(packet())["abstention"])

    def test_kg_separates_pathways_and_declares_incomplete_coverage(self):
        raw = {"items": [
            {"object": "HGNC:TEST", "object_label": "GENE", "predicate": "related",
             "category": "biolink:PairwiseGeneToGeneInteraction"},
            {"object": "REACT:TEST", "object_label": "PATHWAY",
             "category": "biolink:GeneToPathwayAssociation"}], "total": 5}
        with patch.object(kg, "_get", return_value=raw):
            self.assertEqual(set(kg.neighbors("HGNC:SEED", 2)), {"GENE"})
            result = kg.neighbor_packet("HGNC:SEED", 2)
            self.assertEqual(result["status"], "INCOMPLETE")
            self.assertEqual(result["raw_response"], raw)

    def test_graphql_errors_empty_results_and_actions_are_distinct(self):
        for raw in ({"errors": [{"message": "unavailable"}]}, {"data": None}, {}):
            with patch.object(kg, "_post", return_value=raw), self.assertRaises(ValueError):
                kg.drugs_for({"GENE"})
        raw = {"data": {"genes": {"nodes": []}}}
        with patch.object(kg, "_post", return_value=raw):
            self.assertEqual(kg.drug_packet({"GENE"})["status"], "NO_MATCH_FOUND")
        interaction = {"drug": {"name": "synthetic", "approved": False},
                       "interactionTypes": [{"type": "inhibitor", "directionality": "inhibitory"}],
                       "interactionScore": 0.5}
        raw["data"]["genes"]["nodes"] = [{"name": "GENE", "interactions": [interaction]}]
        with patch.object(kg, "_post", return_value=raw):
            self.assertEqual(kg.drugs_for({"GENE"})["GENE"], [interaction])
            self.assertEqual(kg.drug_packet({"GENE", "MISSING"})["status"], "INCOMPLETE")
        output = io.StringIO()
        with patch.object(sys, "argv", ["kg", "TEST", "--json"]), \
                patch.object(kg, "resolve_gene", side_effect=ValueError("no match")), \
                contextlib.redirect_stdout(output):
            self.assertEqual(kg.main(), 1)
        self.assertEqual(json.loads(output.getvalue())["status"], "QUERY_ERROR")


if __name__ == "__main__":
    unittest.main(verbosity=2)
