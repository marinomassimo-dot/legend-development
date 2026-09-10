#!/usr/bin/env python3
"""Tests for the public semantic graph generator — fixtures, and then the real registries.

🔴 The fixture half of this file was green on 2026-09-10 while the README's own command
failed on the real registries: ``generate()`` returned any wikilink it could not retarget
unchanged, ``render_field_table`` emitted registry fields without rewriting them at all, and
the vault's self-containment check then refused the result. The fixtures carried none of the
link shapes the registries actually hold. ``TheDocumentedCommandRunsOnTheRealRegistries`` is
the case that exposed it; ``main`` is driven as a subprocess because that is what the README
tells a reader to run.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import generate_semantic_graph as graph

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCRIPT = HERE / "generate_semantic_graph.py"

# The four inputs of the command README.md documents, verbatim.
REAL_INPUTS = {
    "--paper-registry": "disease-models/wwox/registries/paper_registry_current.md",
    "--claim-registry": "disease-models/wwox/registries/claim_registry_current.md",
    "--research-lines": "disease-models/wwox/research/research_lines_current.md",
    "--biomarkers": "disease-models/wwox/biomarker_endpoint/biomarker_candidates_current.md",
}
CANONICAL_BASENAMES = ("paper_registry_current", "claim_registry_current",
                       "dismissal_ledger_current", "discovery_ledger_current",
                       "full_text_queue_current", "meta_metabolism_current")


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT,
                          capture_output=True, text=True, timeout=300)


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


class TheCliIsDriven(unittest.TestCase):
    """``main`` — argument parsing, the error path and its exit code — run as a process."""

    def write_fixtures(self, root: Path) -> dict[str, Path]:
        files = {"papers": PAPERS, "claims": CLAIMS, "lines": RESEARCH_LINES,
                 "biomarkers": BIOMARKERS}
        paths = {}
        for name, text in files.items():
            paths[name] = root / f"{name}.md"
            paths[name].write_text(text, encoding="utf-8")
        return paths

    def test_generates_refuses_to_overwrite_and_replaces_on_request(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths = self.write_fixtures(root)
            output = root / "graph"
            args = ("--paper-registry", str(paths["papers"]),
                    "--claim-registry", str(paths["claims"]),
                    "--research-lines", str(paths["lines"]),
                    "--biomarkers", str(paths["biomarkers"]),
                    "--out", str(output))
            first = run_cli(*args)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertIn("Generated semantic graph:", first.stdout)
            self.assertIn("'papers': 1", first.stdout)
            self.assertTrue((output / graph.MARKER).is_file())

            again = run_cli(*args)
            self.assertEqual(again.returncode, 1, "an existing vault must be refused")
            self.assertIn("ERROR:", again.stderr)
            self.assertIn("--replace", again.stderr)

            replaced = run_cli(*args, "--replace")
            self.assertEqual(replaced.returncode, 0, replaced.stderr)
            self.assertIn("Generated semantic graph:", replaced.stdout)

    def test_a_missing_registry_is_an_error_exit_not_a_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            result = run_cli("--paper-registry", str(root / "absent.md"),
                             "--claim-registry", str(root / "absent.md"),
                             "--out", str(root / "graph"))
            self.assertEqual(result.returncode, 1)
            self.assertIn("ERROR:", result.stderr)
            self.assertNotIn("Traceback", result.stderr)


class LinksTheVaultCannotCarryBecomeText(unittest.TestCase):
    """The five link shapes the real registries hold and the fixtures did not."""

    NAMES = ({"001": "PAPER 001 - Public WWOX network study"},
             {"001": "CLAIM 001 - Network and myelination result"})

    def rewrite(self, text: str) -> str:
        return graph.rewrite_registry_links(text, *self.NAMES)

    def test_a_registry_link_with_a_fragment_becomes_a_vault_link(self) -> None:
        out = self.rewrite("see [[paper_registry_current#PAPER 001]] and "
                           "[[claim_registry_current#CLAIM 001|the claim]]")
        self.assertIn("[[papers/PAPER 001 - Public WWOX network study|PAPER 001]]", out)
        self.assertIn("[[claims/CLAIM 001 - Network and myelination result|the claim]]", out)

    def test_a_link_to_another_canonical_file_keeps_its_words_and_loses_the_link(self) -> None:
        cases = {
            "[[dismissal_ledger_current#DIS-008 — «La calpaina» → ⏸️ **NON STABILITA**]]":
                "DIS-008 — «La calpaina» → ⏸️ **NON STABILITA** (dismissal ledger)",
            "[[full_text_queue_current#FT-024]]": "FT-024 (full text queue)",
            "[[meta_metabolism_current]]": "meta metabolism",
            "[[discovery_ledger_current#DL-MECH-061 — long title|DL-MECH-061]]": "DL-MECH-061",
            "[[paper_registry_current]]": "paper registry",
        }
        for source, expected in cases.items():
            with self.subTest(link=source):
                out = self.rewrite(f"before {source} after")
                self.assertEqual(out, f"before {expected} after")
                self.assertNotIn("[[", out)

    def test_a_registry_field_outside_the_summary_is_rewritten_too(self) -> None:
        """PAPER 088's *Source type* carried a registry link; the table emitted it raw."""
        papers = PAPERS.replace(
            "**Status:** integrated",
            "**Status:** integrated\n**Source type:** secondary — unlike "
            "[[paper_registry_current#PAPER 001]] and [[full_text_queue_current#FT-001]]")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "papers.md").write_text(papers, encoding="utf-8")
            (root / "claims.md").write_text(CLAIMS, encoding="utf-8")
            output = root / "graph"
            graph.generate(root / "papers.md", root / "claims.md", output)
            note = next((output / "papers").glob("PAPER 001*.md")).read_text(encoding="utf-8")
            self.assertIn("| Source type |", note)
            self.assertIn("[[papers/PAPER 001 - Public WWOX network study|PAPER 001]]", note)
            self.assertIn("FT-001 (full text queue)", note)
            for basename in CANONICAL_BASENAMES:
                self.assertNotIn(basename, note)
            self.assertEqual([], graph.unresolved_generated_wikilinks(output))


class TheDocumentedCommandRunsOnTheRealRegistries(unittest.TestCase):
    """README.md § semantic graph, run verbatim against this checkout's registries.

    The registries are tracked, so the inputs are present in every clone; the skip below is
    the contract for a checkout that has them elsewhere, and it is declared, never silent.
    """

    def test_the_readme_command_generates_a_self_contained_vault(self) -> None:
        missing = [rel for rel in REAL_INPUTS.values() if not (ROOT / rel).is_file()]
        if missing:
            self.skipTest(f"skipped: real registries absent on this host: {missing}")
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "legend-semantic-graph"
            args = [item for flag, rel in REAL_INPUTS.items() for item in (flag, rel)]
            result = run_cli(*args, "--out", str(output))
            self.assertEqual(result.returncode, 0,
                             f"the README command failed on the real registries:\n"
                             f"{result.stderr[:2000]}")
            self.assertIn("Generated semantic graph:", result.stdout)
            self.assertEqual([], graph.unresolved_generated_wikilinks(output))
            papers = list((output / "papers").glob("*.md"))
            claims = list((output / "claims").glob("*.md"))
            self.assertGreater(len(papers), 50, "the real paper registry holds dozens of papers")
            self.assertGreater(len(claims), 20)
            leaked = [path.name for path in output.rglob("*.md")
                      if any(name in path.read_text(encoding="utf-8")
                             for name in CANONICAL_BASENAMES)]
            self.assertEqual([], leaked, "a canonical filename leaked into the vault")


if __name__ == "__main__":
    unittest.main()
