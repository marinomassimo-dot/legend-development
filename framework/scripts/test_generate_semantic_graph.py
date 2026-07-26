#!/usr/bin/env python3
"""Synthetic-fixture tests for the public semantic graph generator."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import generate_semantic_graph as graph


PAPERS = """# Paper Registry
## PAPER 001
**Short title:** Public WWOX network study
**Status:** integrated
**Primary pathway:** P4
**Claim links:** 1
**Disease relevance:** high
**Note:** A public disease-level summary mentioning myelination and EEG; promoted from [[paper_registry_current#CORPUS P383]].
"""

CLAIMS = """# Claim Registry
## CLAIM 001
**Title:** Network and myelination result
**Status:** consolidated baseline
**Pathway:** P4
**Disease relevance:** high
**Summary:** Public disease-level result.
**Wikilinks:** [[paper_registry_current#PAPER 001]]
"""

RESEARCH_LINES = """# Research Lines
## RL-NET-001 — Public network line
**Status:** active
**Primary pathway:** P4
**Disease relevance:** high
"""

BIOMARKERS = """# Biomarker candidates

> Public functional-state framework.

---

## Candidate template
"""


class SemanticGraphTests(unittest.TestCase):
    def test_slug_removes_unsafe_filename_characters(self) -> None:
        self.assertEqual(graph.slug('A [title]: "x"?'), "A title x")

    def test_split_blocks(self) -> None:
        blocks = graph.split_blocks(PAPERS, "PAPER")
        self.assertEqual(set(blocks), {"001"})
        self.assertIn("Public WWOX network study", blocks["001"])

    def test_generate_and_safe_replace(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            papers = root / "papers.md"
            claims = root / "claims.md"
            lines = root / "lines.md"
            biomarkers = root / "biomarkers.md"
            output = root / "graph"
            papers.write_text(PAPERS, encoding="utf-8")
            claims.write_text(CLAIMS, encoding="utf-8")
            lines.write_text(RESEARCH_LINES, encoding="utf-8")
            biomarkers.write_text(BIOMARKERS, encoding="utf-8")

            counts = graph.generate(
                papers,
                claims,
                output,
                research_lines=lines,
                biomarkers=biomarkers,
            )
            self.assertEqual(counts["papers"], 1)
            self.assertEqual(counts["claims"], 1)
            self.assertEqual(counts["research_lines"], 1)
            self.assertEqual(counts["concepts"], len(graph.CONCEPT_RULES) + 1)
            self.assertTrue((output / graph.MARKER).is_file())
            self.assertTrue(
                (
                    output
                    / "concepts"
                    / "biomarker - candidate framework.md"
                ).is_file()
            )
            index = (output / "Semantic Graph Index.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("| Papers | 1 |", index)
            self.assertIn("## Entry points", index)
            self.assertIn("therapy - vigabatrin safety", index)
            all_text = "\n".join(
                path.read_text(encoding="utf-8")
                for path in output.rglob("*.md")
            )
            self.assertIn("Disease relevance", all_text)
            self.assertNotIn("patient-level export", all_text)
            self.assertNotIn("paper_registry_current", all_text)
            self.assertNotIn("claim_registry_current", all_text)
            self.assertNotIn("biomarker_candidates_current", all_text)
            self.assertEqual([], graph.unresolved_generated_wikilinks(output))

            counts_again = graph.generate(
                papers,
                claims,
                output,
                research_lines=lines,
                biomarkers=biomarkers,
                replace=True,
            )
            self.assertEqual(counts_again, counts)

    def test_refuses_to_replace_unmarked_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "unmarked"
            output.mkdir()
            (output / "user-file.md").write_text("keep", encoding="utf-8")
            with self.assertRaises(ValueError):
                graph.prepare_output(output, replace=True)
            self.assertTrue((output / "user-file.md").is_file())


if __name__ == "__main__":
    unittest.main()
