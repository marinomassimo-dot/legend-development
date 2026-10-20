#!/usr/bin/env python3
"""Regressions for kg_thin_slice.py — one per P2 property, all offline.

The injected `get`/`post` callables stand in for Monarch and DGIdb. A regression that needs
either service to be up is a regression that gets disabled the first week it is not; the live
run is performed by hand and recorded with its date.
"""

from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import kg_thin_slice as kg  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]

SEARCH = {"total": 3, "items": [
    {"id": "HGNC:12799", "name": "WWOX", "category": "biolink:Gene",
     "in_taxon": "NCBITaxon:9606", "in_taxon_label": "Homo sapiens",
     "full_name": "WW domain containing oxidoreductase"},
    {"id": "NCBIGene:610120", "name": "WWOX", "category": "biolink:Gene",
     "in_taxon": "NCBITaxon:9615", "in_taxon_label": "Canis lupus familiaris"},
    {"id": "NCBIGene:100518839", "name": "WWOX", "category": "biolink:Gene",
     "in_taxon": "NCBITaxon:9823", "in_taxon_label": "Sus scrofa"},
]}


def association(object_id: str, label: str, category: str, predicate: str) -> dict:
    return {"object": object_id, "object_label": label, "category": category,
            "predicate": predicate}


def dgidb_response(name: str = "MAPK1", approved: bool = True) -> dict:
    return {"data": {"genes": {"nodes": [{
        "name": name, "longName": f"{name} long name", "conceptId": "hgnc:0001",
        "interactions": [{
            "drug": {"name": "DRUG ONE", "conceptId": "ncit:C1", "approved": approved},
            "interactionScore": 0.5,
            "interactionTypes": [{"type": "inhibitor", "directionality": "INHIBITORY"}],
            "sources": [{"sourceDbName": "DrugBank", "sourceDbVersion": "5.1"}],
            "publications": [{"pmid": 1}],
        }],
    }]}}}


def dgidb_two_nodes(url, payload) -> dict:
    """Both requested symbols come back — the seed is always requested beside its neighbours,
    so a one-node fixture would legitimately read COVERAGE_INCOMPLETE."""
    first = dgidb_response("MAPK1")["data"]["genes"]["nodes"][0]
    second = dgidb_response("WWOX")["data"]["genes"]["nodes"][0]
    return {"data": {"genes": {"nodes": [node for node in (first, second)
                                         if node["name"] in payload["variables"]["names"]]}}}


class ResolutionTests(unittest.TestCase):
    def test_seed_resolves_with_type_and_species_and_keeps_the_rejected_candidates(self):
        seed = kg.resolve_entity("WWOX", get=lambda url: SEARCH)
        self.assertEqual("HGNC:12799", seed["id"])
        self.assertEqual("biolink:Gene", seed["type"])
        self.assertEqual("NCBITaxon:9606", seed["taxon"])
        self.assertEqual("Homo sapiens", seed["taxon_label"])
        self.assertEqual("HGNC", seed["identifier_namespace"])
        self.assertEqual(3, len(seed["candidates_considered"]))
        self.assertIn("category=biolink:Gene", seed["query"])

    def test_a_non_human_taxon_is_not_silently_accepted(self):
        with self.assertRaises(kg.SliceError) as raised:
            kg.resolve_entity("WWOX", taxon="NCBITaxon:10090", get=lambda url: SEARCH)
        self.assertIn("UNRESOLVED seed", str(raised.exception))

    def test_an_unresolved_seed_is_not_an_absence_of_neighbours(self):
        with self.assertRaises(kg.SliceError) as raised:
            kg.resolve_entity("NOTAGENE", get=lambda url: {"items": []})
        self.assertIn("not an absence of neighbours", str(raised.exception).replace("\n", " "))

    def test_resolution_response_is_persisted_at_the_recorded_path(self):
        with tempfile.TemporaryDirectory() as temporary:
            seed = kg.resolve_entity("WWOX", raw_dir=Path(temporary),
                                     get=lambda url: SEARCH)
            path = Path(seed["original_response_path"])
            self.assertEqual(SEARCH, json.loads(path.read_text(encoding="utf-8")))


class TypingTests(unittest.TestCase):
    PAGE = {"total": 3, "items": [
        association("HGNC:6871", "MAPK1", kg.GENE_GENE, "biolink:interacts_with"),
        association("REACT:R-HSA-1", "Signal transduction", kg.GENE_PATHWAY,
                    "biolink:participates_in"),
        association("UniProtKB:P12345", "Some protein", kg.GENE_GENE,
                    "biolink:interacts_with"),
    ]}

    def test_pathways_and_unresolved_ids_are_typed_apart_from_genes(self):
        packet = kg.neighbor_packet("HGNC:12799", 10, get=lambda url: self.PAGE)
        kinds = {entity["label"]: entity["type"] for entity in packet["entities"]}
        self.assertEqual("GENE", kinds["MAPK1"])
        self.assertEqual("PATHWAY", kinds["Signal transduction"])
        self.assertEqual("UNRESOLVED", kinds["Some protein"])
        self.assertEqual({"GENE": 1, "PATHWAY": 1, "UNRESOLVED": 1},
                         packet["counts_by_type"])

    def test_only_gene_labels_reach_the_dgidb_request(self):
        requested: list[list[str]] = []

        def post(url, payload):
            requested.append(payload["variables"]["names"])
            return dgidb_response()

        packet = kg.neighbor_packet("HGNC:12799", 10, get=lambda url: self.PAGE)
        genes = {entity["label"] for entity in packet["entities"]
                 if entity["type"] == "GENE"}
        kg.drug_packet(genes, post=post)
        self.assertEqual([["MAPK1"]], requested)
        self.assertNotIn("Signal transduction", requested[0])
        self.assertNotIn("Some protein", requested[0])


class PaginationTests(unittest.TestCase):
    def test_offset_pagination_reaches_the_registry_total(self):
        calls: list[str] = []

        def get(url):
            calls.append(url)
            offset = int(url.split("offset=")[1])
            return {"total": 3, "items": [
                association(f"HGNC:{offset}", f"G{offset}", kg.GENE_GENE, "p")]}

        packet = kg.neighbor_packet("HGNC:12799", 10, page_size=1, get=get)
        self.assertEqual(3, packet["associations_read"])
        self.assertEqual("OK", packet["status"])
        self.assertFalse(packet["truncation"]["truncated"])
        self.assertEqual(3, len(calls))
        self.assertEqual(3, len(packet["pages"]))

    def test_the_ceiling_reports_coverage_incomplete_with_an_explicit_statement(self):
        def get(url):
            offset = int(url.split("offset=")[1])
            return {"total": 825, "items": [
                association(f"HGNC:{offset}", f"G{offset}", kg.GENE_GENE, "p")]}

        packet = kg.neighbor_packet("HGNC:12799", 2, page_size=1, get=get)
        self.assertEqual("COVERAGE_INCOMPLETE", packet["status"])
        self.assertTrue(packet["truncation"]["truncated"])
        self.assertIn("read 2 of 825 associations", packet["truncation"]["statement"])
        self.assertIn("NOT read", packet["truncation"]["statement"])
        self.assertEqual(825, packet["registry_total"])


class ActionsAndSourcesTests(unittest.TestCase):
    def test_actions_and_sources_are_preserved_in_the_packet(self):
        packet = kg.drug_packet({"MAPK1"}, post=lambda url, payload: dgidb_response())
        interaction = packet["interactions"]["MAPK1"][0]
        self.assertEqual([{"type": "inhibitor", "directionality": "INHIBITORY"}],
                         interaction["interactionTypes"])
        self.assertEqual("DrugBank", interaction["sources"][0]["sourceDbName"])
        self.assertEqual("5.1", interaction["sources"][0]["sourceDbVersion"])
        self.assertEqual("MAPK1 long name", packet["long_names"]["MAPK1"])

    def test_missing_action_or_source_is_printed_as_unknown_not_dropped(self):
        bare = {"drug": {"name": "X", "approved": False}}
        self.assertEqual("action UNKNOWN", kg.describe_actions(bare))
        self.assertEqual("source UNKNOWN", kg.describe_sources(bare))
        self.assertIn("UNKNOWN direction", kg.describe_actions(
            {"interactionTypes": [{"type": "binder"}]}))
        self.assertIn("unversioned", kg.describe_sources(
            {"sources": [{"sourceDbName": "TTD"}]}))


class ErrorStateTests(unittest.TestCase):
    def test_graphql_errors_are_an_api_error_not_zero_results(self):
        with self.assertRaises(kg.ApiError):
            kg.drug_packet({"MAPK1"},
                           post=lambda url, payload: {"errors": [{"message": "boom"}]})

    def test_api_error_is_a_subclass_of_slice_error_and_both_differ_from_no_match(self):
        self.assertTrue(issubclass(kg.ApiError, kg.SliceError))
        packet = kg.drug_packet({"MAPK1"}, post=lambda url, payload: {
            "data": {"genes": {"nodes": []}}})
        self.assertEqual("NO_MATCH", packet["status"])
        self.assertEqual([], packet["interactions"].get("MAPK1", []))

    def test_an_unknown_symbol_is_coverage_incomplete_with_a_statement(self):
        packet = kg.drug_packet({"MAPK1", "NOTAGENE"},
                                post=lambda url, payload: dgidb_response())
        self.assertEqual("COVERAGE_INCOMPLETE", packet["status"])
        self.assertEqual(["NOTAGENE"], packet["unmatched_symbols"])
        self.assertIn("not the same as a gene with no drugs", packet["coverage_statement"])

    def test_a_malformed_dgidb_document_is_an_error_state(self):
        with self.assertRaises(kg.SliceError):
            kg.drug_packet({"MAPK1"}, post=lambda url, payload: {
                "data": {"genes": {"nodes": [{"name": 1, "interactions": None}]}}})

    def test_a_malformed_monarch_document_is_an_error_state(self):
        with self.assertRaises(kg.SliceError):
            kg.neighbor_packet("HGNC:12799", 5, get=lambda url: {"items": "nope"})


class ApprovalViewTests(unittest.TestCase):
    ITEMS = [{"drug": {"name": "A", "approved": True}},
             {"drug": {"name": "B", "approved": False}}]

    def test_the_default_view_drops_nothing(self):
        self.assertEqual(2, len(kg.select_by_approval(self.ITEMS, "all")))

    def test_approved_and_investigational_are_both_selectable(self):
        self.assertEqual(["A"], [item["drug"]["name"]
                                 for item in kg.select_by_approval(self.ITEMS, "approved")])
        self.assertEqual(["B"], [item["drug"]["name"]
                                 for item in
                                 kg.select_by_approval(self.ITEMS, "investigational")])

    def test_the_command_line_exposes_the_choice_and_defaults_to_all(self):
        completed = subprocess.run(
            [sys.executable,
             str(ROOT / ".claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py"),
             "--help"], capture_output=True, text=True, check=False, timeout=30)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("--drug-approval", completed.stdout)
        for choice in ("all", "approved", "investigational"):
            self.assertIn(choice, completed.stdout)

    def test_the_text_output_states_the_view_and_keeps_actions_and_sources(self):
        buffer = io.StringIO()
        monkey = {"search": SEARCH,
                  "assoc": {"total": 1, "items": [
                      association("HGNC:6871", "MAPK1", kg.GENE_GENE, "biolink:interacts")]}}

        def get(url):
            return monkey["search"] if "/search?" in url else monkey["assoc"]

        with redirect_stdout(buffer):
            code = kg.main(["WWOX"], get=get, post=dgidb_two_nodes)
        output = buffer.getvalue()
        self.assertEqual(0, code)
        self.assertIn("--drug-approval all", output)
        self.assertIn("Homo sapiens", output)
        self.assertIn("inhibitor/INHIBITORY", output)
        self.assertIn("DrugBank@5.1", output)
        self.assertIn("PATHWAY and UNRESOLVED never reach DGIdb", output)


class StructuredOutputTests(unittest.TestCase):
    def test_json_carries_query_date_version_provenance_and_response_paths(self):
        assoc = {"total": 1, "items": [
            association("HGNC:6871", "MAPK1", kg.GENE_GENE, "biolink:interacts")]}

        def get(url):
            return SEARCH if "/search?" in url else assoc

        with tempfile.TemporaryDirectory() as temporary:
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                code = kg.main(["WWOX", "--json", "--raw-dir", temporary], get=get,
                               post=dgidb_two_nodes)
            self.assertEqual(0, code)
            packet = json.loads(buffer.getvalue())
            self.assertEqual(kg.SCHEMA_VERSION, packet["schema_version"])
            self.assertEqual(kg.TOOL_VERSION, packet["tool"])
            self.assertEqual("OK", packet["status"])
            self.assertEqual("ESPANSIONE", packet["epistemic_status"])
            self.assertTrue(packet["retrieved_at"].startswith("20"))
            self.assertEqual("NCBITaxon:9606", packet["provenance"]["taxon"])
            self.assertEqual("all", packet["provenance"]["drug_approval_view"])
            self.assertIn("association?subject=", packet["monarch"]["query"])
            for path in packet["monarch"]["raw_response_pages"]:
                self.assertTrue(Path(path).is_file())
            self.assertTrue(Path(
                packet["dgidb"]["batches"][0]["original_response_path"]).is_file())
            self.assertTrue(Path(packet["seed"]["original_response_path"]).is_file())

    def test_an_error_exits_nonzero_and_names_the_state(self):
        def boom(url):
            raise kg.SliceError("HTTP 503")

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = kg.main(["WWOX", "--json"], get=boom)
        self.assertEqual(1, code)
        self.assertEqual("QUERY_ERROR", json.loads(buffer.getvalue())["status"])

    def test_coverage_incomplete_exits_three(self):
        def get(url):
            if "/search?" in url:
                return SEARCH
            offset = int(url.split("offset=")[1])
            return {"total": 99, "items": [
                association(f"HGNC:{offset}", "MAPK1", kg.GENE_GENE, "p")]}

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = kg.main(["WWOX", "--json", "--limit", "1"], get=get,
                           post=lambda url, payload: dgidb_response())
        self.assertEqual(3, code)
        self.assertEqual("COVERAGE_INCOMPLETE", json.loads(buffer.getvalue())["status"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
