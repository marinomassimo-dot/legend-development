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

from repurposing_bridge import (build_card, normalise_label_lookup, normalise_p4_fields,
                                normalise_translation)

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

    def test_reported_null_is_not_an_unmeasured_cell(self):
        def with_direction(value, **ctx):
            data = packet()
            data["drug_assertions"][0]["direction"] = value
            data["drug_assertions"][0]["context"].update(ctx)
            return build_card(data)
        null, unmeasured = with_direction("NO_CHANGE"), with_direction("UNKNOWN")
        self.assertEqual(null["comparisons"][0]["status"], "NO_EFFECT_REPORTED")
        self.assertEqual(unmeasured["comparisons"][0]["status"], "UNRESOLVED")
        self.assertNotEqual(null["directional_summary"], unmeasured["directional_summary"])
        self.assertNotIn("OPPOSES", null["directional_summary"])
        self.assertNotIn("REINFORCES", null["directional_summary"])
        self.assertTrue(any("not UNKNOWN" in line for line in null["limits"]))
        # A null in a non-comparable cell stays unresolved but says it was measured.
        off = with_direction("NO_CHANGE", genotype="other")
        self.assertEqual(off["comparisons"][0]["status"], "UNRESOLVED")
        self.assertTrue(any("measured null" in r for r in off["comparisons"][0]["reasons"]))
        self.assertFalse(any("measured null" in r
                             for r in unmeasured["comparisons"][0]["reasons"]))
        # A null beside a positive is a conflict, never a pooled value; a null disease is refused.
        data = packet()
        second = copy.deepcopy(data["drug_assertions"][0])
        second.update(id="drug-2", direction="NO_CHANGE")
        data["drug_assertions"].append(second)
        self.assertEqual(build_card(data)["directional_summary"], "CONFLICTING")
        data = packet()
        data["disease_assertion"]["direction"] = "NO_CHANGE"
        self.assertEqual(build_card(data)["comparisons"][0]["status"], "UNRESOLVED")
        # The label outcome still never moves the comparison.
        data = packet()
        data["drug_assertions"][0]["direction"] = "NO_CHANGE"
        data["label_lookup"] = {"status": "NO_MATCH_FOUND", "queries": ["q"]}
        self.assertEqual(build_card(data)["comparisons"], null["comparisons"])

    def test_translation_is_reachable_and_stays_unknown_by_default(self):
        default = build_card(packet())["translation"]
        self.assertEqual(set(default.values()), {"UNKNOWN"})
        data = packet()
        data["translation"] = {"access": "synthetic access statement"}
        filled = build_card(data)["translation"]
        self.assertEqual(filled["access"], "synthetic access statement")
        self.assertEqual(filled["time_to_benefit"], "UNKNOWN")
        data["translation"]["time_to_benefit"] = "synthetic benefit statement"
        both = build_card(data)["translation"]
        self.assertNotEqual(both["access"], both["time_to_benefit"])
        self.assertEqual(data["translation"], build_card(data)["input"]["translation"])
        for bad in ({"access": ""}, {"time_to_access_score": "1"}, {"access": 3}, "x"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                normalise_translation(bad)

    def test_roadmap_rows_a_card_cannot_do_without(self):
        data = packet()
        data["p4_roadmap_fields"] = {"indication_and_transfer": "UNKNOWN",
                                     "verification_scope": "synthetic", "other": "free"}
        self.assertEqual(build_card(data)["input"]["p4_roadmap_fields"]["other"], "free")
        for mutate in (lambda b: b.pop("verification_scope"),
                       lambda b: b.update(indication_and_transfer="")):
            broken = copy.deepcopy(data)
            mutate(broken["p4_roadmap_fields"])
            with self.assertRaises(ValueError):
                build_card(broken)
        self.assertNotIn("p4_roadmap_fields", build_card(packet())["input"])

    def test_several_disease_endpoints_each_compare_on_their_own(self):
        data = packet()
        first = data.pop("disease_assertion")
        second = copy.deepcopy(first)
        second.update(id="disease-2", endpoint="other endpoint", direction="DECREASE")
        data["disease_assertions"] = [first, second]
        other = copy.deepcopy(data["drug_assertions"][0])
        other.update(id="drug-2", endpoint="other endpoint", direction="DECREASE")
        third = copy.deepcopy(other)
        third.update(id="drug-3", endpoint="third endpoint")
        data["drug_assertions"] += [other, third]
        by_id = {c["assertion_id"]: c for c in build_card(data)["comparisons"]}
        self.assertEqual(by_id["drug-1"]["status"], "OPPOSES_DISEASE_CHANGE")
        self.assertEqual(by_id["drug-2"]["status"], "REINFORCES_DISEASE_CHANGE")
        self.assertEqual(by_id["drug-3"]["status"], "UNRESOLVED")
        self.assertIn("no disease assertion", by_id["drug-3"]["reasons"][0])
        self.assertEqual(build_card(data)["directional_summary"], "CONFLICTING")
        # Singular and plural spellings of one endpoint give the same comparison.
        single = packet()
        plural = packet()
        plural["disease_assertions"] = [plural.pop("disease_assertion")]
        self.assertEqual(build_card(single)["comparisons"], build_card(plural)["comparisons"])
        # No disease side at all is legal and never resolves; both spellings together are refused.
        plural["disease_assertions"] = []
        self.assertEqual(build_card(plural)["directional_summary"], "UNRESOLVED")
        both = packet()
        both["disease_assertions"] = []
        for bad in (both, {**packet(), "disease_assertions": "x"}):
            with self.assertRaises(ValueError):
                build_card(bad)

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
