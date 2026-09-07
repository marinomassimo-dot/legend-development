#!/usr/bin/env python3
"""Regressions for the pathograph assembler.

The assembler's whole value is a refusal: it must materialise the graph the registries
declare and must not add one edge, one type or one endpoint of its own. A suite that only
checked the happy path would pass on a version that invented half the graph, so most of what
follows is negative — a fixture that *could* tempt an inference, and an assertion that the
tool declined it.

Run: `python3 framework/scripts/test_pathograph.py`
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pathograph  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SURFACE = "disease-models/wwox/analysis/pathograph_inventory.md"
EXPORT = "disease-models/wwox/analysis/data/pathograph_export.jsonl"


def claim(identifier: str, title: str, *, status: str = "consolidated baseline",
          kind: str = "DATO", pathway: str = "P1 — network", wikilinks: str = "",
          source: str = "", body: str = "") -> str:
    return "\n".join([
        f"## CLAIM {identifier}",
        f"**Title:** {title}",
        f"**Status:** {status}",
        f"**Type:** {kind}",
        f"**Pathway:** {pathway}",
        "**Genotype/model relevance:** murine",
        "**Transferability:** T2",
        "**clinical relevance:** MODERATE",
        f"**Summary:** {body}" if body else "**Summary:** unremarkable text.",
        f"**Source:** {source}" if source else "**Source:** none",
        f"**Wikilinks:** {wikilinks}" if wikilinks else "**Wikilinks:**",
        "",
    ])


def paper(identifier: str, *, pmid: str = "", claims: str = "") -> str:
    return "\n".join([
        f"## PAPER {identifier}",
        f"**Identifier:** PMID {pmid}" if pmid else "**Identifier:** preprint",
        "**Model/species:** mouse",
        f"**Claim links:** {claims}",
        "**Wikilinks:**",
        "",
    ])


def build(tmp: Path, *, claims: str, papers: str = "", working_model: str = "",
          manifests: dict[str, dict] | None = None, disease: str = "wwox") -> Path:
    registries = tmp / "disease-models" / disease / "registries"
    manifest_dir = tmp / "disease-models" / disease / "research" / "deepdive_manifests"
    registries.mkdir(parents=True, exist_ok=True)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    (registries / "claim_registry_current.md").write_text(claims, encoding="utf-8")
    (registries / "paper_registry_current.md").write_text(
        papers or paper("001"), encoding="utf-8")
    (registries / "working_model_current.md").write_text(
        working_model or "# Working Model\n\n## Architecture\n\nNothing.\n", encoding="utf-8")
    for name, payload in (manifests or {}).items():
        (manifest_dir / name).write_text(json.dumps(payload), encoding="utf-8")
    return tmp


def assemble(tmp: Path, disease: str = "wwox") -> dict:
    return pathograph.Pathograph(tmp, disease).assemble()


class EdgesAreDeclaredNeverDerived(unittest.TestCase):
    def test_only_declared_links_become_edges(self) -> None:
        """Three claims on one pathway, one link. A derived graph would find more."""
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "WWOX loss causes hyperexcitability",
                      wikilinks="[[claim_registry_current#CLAIM 002]]"),
                claim("002", "Hyperexcitability drives seizures"),
                claim("003", "Seizures worsen development"),
            ]))
            graph = assemble(tmp)
        self.assertEqual([edge["edge_id"] for edge in graph["edges"]],
                         ["CLAIM 001 <-> CLAIM 002"])
        self.assertEqual(
            sorted(item["claim"] for item in graph["findings"]["isolated_claims"]),
            ["CLAIM 003"])

    def test_the_three_link_denominators_stay_distinct(self) -> None:
        """Occurrences, distinct directed links and undirected edges are 2, 1 and 1 here.

        On the real registry they are 41, 30 and 20 — three numbers that read as one another
        if the report quotes whichever it happened to compute.
        """
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "First",
                      body="See [[claim_registry_current#CLAIM 002]] for the counterpart.",
                      wikilinks="[[claim_registry_current#CLAIM 002]]"),
                claim("002", "Second"),
            ]))
            graph = assemble(tmp)
        self.assertEqual(graph["coverage"]["claim_link_occurrences"], 2)
        self.assertEqual(graph["coverage"]["claim_links_directed_distinct"], 1)
        self.assertEqual(len(graph["edges"]), 1)

    def test_a_shared_pathway_never_creates_an_edge(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "First", pathway="P4 — myelination"),
                claim("002", "Second", pathway="P4 — myelination"),
            ]))
            graph = assemble(tmp)
        self.assertEqual(graph["edges"], [])

    def test_shared_evidence_is_a_review_candidate_not_an_edge(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(
                Path(raw),
                claims="".join([claim("001", "First"), claim("002", "Second")]),
                papers=paper("001", pmid="12345678", claims="001, 002"))
            graph = assemble(tmp)
        self.assertEqual(graph["edges"], [])
        self.assertEqual(graph["findings"]["shared_evidence_without_edge"],
                         [{"claims": ["CLAIM 001", "CLAIM 002"],
                           "shared_papers": ["PAPER 001"]}])


class TypingComesFromAnAnnotationOrNotAtAll(unittest.TestCase):
    def test_an_unannotated_link_stays_untyped_with_its_reason(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "First", wikilinks="[[claim_registry_current#CLAIM 002]]"),
                claim("002", "Second"),
            ]))
            graph = assemble(tmp)
        edge = graph["edges"][0]
        self.assertEqual(edge["relation_type"], "UNTYPED")
        self.assertEqual(edge["relation_type_basis"], "NO_DECLARED_RELATION_ANNOTATION")
        self.assertEqual(edge["review_state"], "AWAITING_SCIENTIST_TYPING")

    def test_two_baseline_data_claims_do_not_become_a_direct_edge(self) -> None:
        """The inference this tool exists to refuse."""
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "WWOX deletion reduces inhibitory currents",
                      status="consolidated baseline", kind="DATO",
                      wikilinks="[[claim_registry_current#CLAIM 002]]"),
                claim("002", "Cortical networks are hyperexcitable",
                      status="consolidated baseline", kind="DATO",
                      wikilinks="[[claim_registry_current#CLAIM 001]]"),
            ]))
            graph = assemble(tmp)
        self.assertEqual(graph["edges"][0]["relation_type"], "UNTYPED")
        self.assertEqual(graph["findings"]["typing"]["edges_typed"], 0)

    def test_a_declared_annotation_is_read_back(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "First", wikilinks=(
                    "[[claim_registry_current#CLAIM 002]] "
                    "(relation: DIRECT — the same experiment measures both)")),
                claim("002", "Second"),
            ]))
            graph = assemble(tmp)
        edge = graph["edges"][0]
        self.assertEqual(edge["relation_type"], "DIRECT")
        self.assertEqual(edge["relation_type_basis"], "DECLARED_ANNOTATION")
        self.assertEqual(edge["review_state"], "TYPED")
        self.assertEqual(graph["findings"]["typing"]["edges_typed"], 1)

    def test_every_vocabulary_value_round_trips(self) -> None:
        for value in pathograph.RELATION_VOCABULARY:
            with self.subTest(value=value), tempfile.TemporaryDirectory() as raw:
                tmp = build(Path(raw), claims="".join([
                    claim("001", "First",
                          wikilinks=f"[[claim_registry_current#CLAIM 002]] (relation: {value})"),
                    claim("002", "Second"),
                ]))
                graph = assemble(tmp)
                self.assertEqual(graph["edges"][0]["relation_type"], value)

    def test_an_unrecognised_type_is_a_named_loss_not_a_guess(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "First", wikilinks=(
                    "[[claim_registry_current#CLAIM 002]] (relation: PROBABLY_CAUSAL)")),
                claim("002", "Second"),
            ]))
            graph = assemble(tmp)
        self.assertEqual(graph["edges"][0]["relation_type"], "UNTYPED")
        self.assertEqual(graph["edges"][0]["relation_type_basis"], "RELATION_TYPE_UNRECOGNISED")
        self.assertEqual([loss["state"] for loss in graph["losses"]],
                         ["RELATION_TYPE_UNRECOGNISED"])


class CandidatesAreExtractedNeverResolved(unittest.TestCase):
    def test_a_candidate_never_claims_resolved_endpoints(self) -> None:
        graph = assemble(ROOT)
        self.assertTrue(graph["candidates"], "the extractor found nothing at all")
        for candidate in graph["candidates"]:
            self.assertFalse(candidate["lexical_split"]["endpoints_resolved"],
                             f"{candidate['candidate_id']} claims resolved endpoints")
            self.assertEqual(candidate["review_state"], "AWAITING_SCIENTIST_REVIEW")

    def test_the_accounting_balances_on_the_real_registries(self) -> None:
        graph = assemble(ROOT)
        coverage = graph["coverage"]
        self.assertEqual(
            coverage["candidates_emitted"] + coverage["candidates_without_connective"],
            coverage["propositions_scanned"])

    def test_an_ambiguous_bare_form_is_quarantined_not_deleted(self) -> None:
        """`reduced` is usually an adjective here and sometimes a verb. Both survive."""
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "Reduced g-ratio in treated animals"),
                claim("002", "WWOX loss reduces inhibitory drive"),
            ]))
            graph = assemble(tmp)
        by_claim = {candidate["bound_claims"][0]: candidate
                    for candidate in graph["candidates"]
                    if candidate["source_kind"] == "claim_title"}
        self.assertEqual(by_claim["CLAIM 001"]["review_priority"], "LOW")
        self.assertEqual(by_claim["CLAIM 001"]["morphology"], "AMBIGUOUS_BARE_FORM")
        self.assertEqual(by_claim["CLAIM 002"]["review_priority"], "NORMAL")
        self.assertEqual(by_claim["CLAIM 002"]["morphology"], "FINITE_OR_MULTIWORD")

    def test_an_unambiguous_form_anchors_the_split_wherever_it_sits(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims=claim(
                "001", "The control cohort shows that the allele abolishes protein"))
            graph = assemble(tmp)
        candidate = graph["candidates"][0]
        self.assertEqual(candidate["connective"], "abolishes")
        self.assertEqual(candidate["lexical_split"]["left"],
                         "The control cohort shows that the allele")

    def test_a_proposition_with_no_connective_yields_no_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims=claim("001", "A registry of reported variants"))
            graph = assemble(tmp)
        self.assertEqual(graph["candidates"], [])
        self.assertEqual(graph["coverage"]["candidates_without_connective"], 1)

    def test_locator_propositions_carry_their_evidence(self) -> None:
        manifest = {
            "pmid": "12345678",
            "receipt": "FTR-20260101-12345678-01",
            "verbatim_locators": {"entries": [{
                "proposition": "Neuronal deletion induces hypomyelination",
                "snippet": "myelination was impaired in the conditional mutant",
                "surface": "body", "artifact": "files/fulltext/x.xml",
                "anchor": "Results, first paragraph"}]},
        }
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw),
                        claims=claim("001", "A flat statement",
                                     source="PMID 12345678"),
                        papers=paper("001", pmid="12345678", claims="001"),
                        manifests={"PMID12345678.json": manifest})
            graph = assemble(tmp)
        candidates = [item for item in graph["candidates"]
                      if item["source_kind"] == "locator_proposition"]
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["evidence"]["snippet"],
                         "myelination was impaired in the conditional mutant")
        self.assertEqual(candidates[0]["evidence"]["receipt"], "FTR-20260101-12345678-01")
        self.assertEqual(candidates[0]["bound_claims"], ["CLAIM 001"])


class AbsencesAreSeparatedByKind(unittest.TestCase):
    def test_a_one_way_link_is_reported_and_a_reciprocal_one_is_not(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "First", wikilinks="[[claim_registry_current#CLAIM 002]]"),
                claim("002", "Second"),
                claim("003", "Third", wikilinks="[[claim_registry_current#CLAIM 004]]"),
                claim("004", "Fourth", wikilinks="[[claim_registry_current#CLAIM 003]]"),
            ]))
            graph = assemble(tmp)
        asymmetric = graph["findings"]["asymmetric_links"]
        self.assertEqual([item["edge_id"] for item in asymmetric],
                         ["CLAIM 001 <-> CLAIM 002"])
        self.assertEqual(asymmetric[0]["missing"], "CLAIM 002 -> CLAIM 001")

    def test_a_prose_mention_without_a_wikilink_is_an_annotation_gap(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "First", body="This tensions with CLAIM 002 on the redox sign."),
                claim("002", "Second"),
            ]))
            graph = assemble(tmp)
        self.assertEqual(graph["findings"]["unlinked_prose_mentions"],
                         [{"source": "CLAIM 001", "target": "CLAIM 002", "field": "Summary"}])
        verdicts = {item["claim"]: item["verdict"]
                    for item in graph["findings"]["isolated_claims"]}
        self.assertEqual(verdicts["CLAIM 001"], "ANNOTATION_GAP_CONFIRMED")

    def test_a_wikilinked_mention_is_not_reported_as_unlinked(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims="".join([
                claim("001", "First",
                      body="This tensions with [[claim_registry_current#CLAIM 002]]."),
                claim("002", "Second"),
            ]))
            graph = assemble(tmp)
        self.assertEqual(graph["findings"]["unlinked_prose_mentions"], [])
        self.assertEqual(len(graph["edges"]), 1)

    def test_the_working_model_version_history_is_not_a_relationship(self) -> None:
        """Positive and negative control in one fixture.

        The same two claims are named twice: once in a changelog line and once in a model
        sentence. Only the second is a co-mention, and a detector that reported neither
        would pass a test that only asserted the exclusion.
        """
        model = "\n".join([
            "# Working Model",
            "**Last update:** 2026-08-15 — `BATCH_20260815_001`: CLAIM 001 and CLAIM 002 "
            "were both promoted.",
            "| 2026-03-29 | v1.2 | CLAIM 001 refined; CLAIM 002 added |",
            "",
            "## Architecture",
            "",
            "The metabolic branch rests on CLAIM 003 and CLAIM 004 together.",
            "",
        ])
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), working_model=model, claims="".join([
                claim("001", "First"), claim("002", "Second"),
                claim("003", "Third"), claim("004", "Fourth"),
            ]))
            graph = assemble(tmp)
        comentions = graph["findings"]["working_model_comentions"]
        self.assertEqual([item["claims"] for item in comentions],
                         [["CLAIM 003", "CLAIM 004"]])
        self.assertGreater(graph["findings"]["working_model_history_lines_excluded"], 0)

    def test_an_isolated_claim_with_nothing_around_it_says_so_about_the_repository(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), claims=claim("001", "A flat statement of fact"))
            graph = assemble(tmp)
        entry = graph["findings"]["isolated_claims"][0]
        self.assertEqual(entry["verdict"], "NO_RELATION_MATERIAL_IN_REPOSITORY")
        self.assertEqual(entry["material"], [])

    def test_a_relational_title_is_reported_as_material_not_as_a_gap(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw),
                        claims=claim("001", "WWOX deletion induces hypomyelination"))
            graph = assemble(tmp)
        entry = graph["findings"]["isolated_claims"][0]
        self.assertEqual(entry["verdict"], "REVIEW_MATERIAL_PRESENT")
        self.assertEqual(entry["material"], ["SELF_RELATIONAL_TITLE"])
        self.assertEqual([item["claim"] for item in graph["findings"]["self_relational_nodes"]],
                         ["CLAIM 001"])


class TheTwoWordingsOfANodeAreCompared(unittest.TestCase):
    MODEL = "\n".join([
        "# Working Model", "", "## BLOCK 2", "",
        "| ID | Title | Status |", "|---|---|---|",
        "| 001 | A flat restatement | consolidated baseline |",
        "| 002 | Second → third | consolidated baseline |", "",
    ])

    def test_a_relation_on_one_side_only_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), working_model=self.MODEL, claims="".join([
                claim("001", "WWOX loss causes hypomyelination"),
                claim("002", "Second → third"),
            ]))
            graph = assemble(tmp)
        disagreement = graph["findings"]["mirror_relational_disagreement"]
        self.assertEqual([item["claim"] for item in disagreement], ["CLAIM 001"])
        self.assertEqual(disagreement[0]["relational_in"], "registry title only")
        self.assertEqual(disagreement[0]["other_wording"], "A flat restatement")

    def test_agreement_reports_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp = build(Path(raw), working_model=self.MODEL, claims="".join([
                claim("001", "A flat restatement"),
                claim("002", "Second → third"),
            ]))
            graph = assemble(tmp)
        self.assertEqual(graph["findings"]["mirror_relational_disagreement"], [])


class TheRealGraphIsStillThere(unittest.TestCase):
    """Guards against a matcher that has quietly stopped matching anything."""

    def setUp(self) -> None:
        self.graph = assemble(ROOT)

    def test_the_assembled_graph_is_not_empty(self) -> None:
        self.assertGreater(len(self.graph["nodes"]), 0)
        self.assertGreater(len(self.graph["edges"]), 0)
        self.assertGreater(len(self.graph["findings"]["self_relational_nodes"]), 0)

    def test_no_node_carries_an_invented_biological_scale(self) -> None:
        for node in self.graph["nodes"]:
            self.assertEqual(node["biological_scale"], pathograph.UNANNOTATED,
                             f"{node['id']} was given a scale no registry declares")

    def test_every_edge_endpoint_is_a_node(self) -> None:
        identifiers = {node["id"] for node in self.graph["nodes"]}
        for edge in self.graph["edges"]:
            for endpoint in edge["endpoints"]:
                self.assertIn(endpoint, identifiers)


class TheCommittedSurfacesAreCurrent(unittest.TestCase):
    def test_the_generated_surfaces_have_not_drifted(self) -> None:
        result = subprocess.run(
            [sys.executable, "framework/scripts/pathograph.py", "--disease", "wwox",
             "--verify", "--out", SURFACE, "--export", EXPORT],
            cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0,
                         f"{SURFACE} / {EXPORT} have drifted from the registries:\n"
                         f"{result.stdout}{result.stderr}")

    def test_verify_without_a_target_refuses_rather_than_passing(self) -> None:
        result = subprocess.run(
            [sys.executable, "framework/scripts/pathograph.py", "--disease", "wwox",
             "--verify"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)

    def test_the_export_is_one_json_object_per_line(self) -> None:
        lines = (ROOT / EXPORT).read_text(encoding="utf-8").splitlines()
        self.assertGreater(len(lines), 1)
        first = json.loads(lines[0])
        self.assertEqual(first["record_kind"], "derivation_manifest")
        for line in lines[1:]:
            self.assertIn("kind", json.loads(line))

    def test_a_plain_run_writes_nothing(self) -> None:
        """The registries are inputs. A read-only tool must leave them byte-identical."""
        registries = ROOT / "disease-models" / "wwox" / "registries"
        before = {path.name: path.read_bytes()
                  for path in sorted(registries.glob("*_current.md"))}
        subprocess.run([sys.executable, "framework/scripts/pathograph.py", "--disease", "wwox"],
                       cwd=ROOT, capture_output=True, text=True, check=True)
        after = {path.name: path.read_bytes()
                 for path in sorted(registries.glob("*_current.md"))}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main(verbosity=2)
