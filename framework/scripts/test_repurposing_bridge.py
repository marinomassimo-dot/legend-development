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

from repurposing_bridge import build_card

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
