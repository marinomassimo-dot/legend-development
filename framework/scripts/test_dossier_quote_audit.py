#!/usr/bin/env python3
"""Regressions for `dossier_quote_audit.py`.

The tests that matter here are the ones that pin the DISTINCTIONS, because every defect this
tool has had so far was a distinction collapsed: quotation versus identifier, one quotation
versus one line of it, certifying versus locating.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import dossier_quote_audit as dqa

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCRIPT = HERE / "dossier_quote_audit.py"
SUMMARY = re.compile(r"^(\d+) quotation\(s\) across (\d+) dossier\(s\): (\d+) verbatim · "
                     r"(\d+) stitched · (\d+) in another paper · (\d+) not found · "
                     r"(\d+) undecidable$", re.M)


def run_cli(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=cwd,
                          capture_output=True, text=True, timeout=600)

PAPER = (
    "<article><body><p>Mutant rats had significantly increased concentrations of plasma "
    "urea nitrogen, creatinine, and inorganic phosphate.</p>"
    "<p>The heterozygote is indistinguishable from the wild type on every measure.</p>"
    "</body></article>"
)
OTHER = (
    "<article><body><p>A sentence that lives only in the other paper and nowhere else at "
    "all.</p></body></article>"
)


class Shapes(unittest.TestCase):
    def test_consecutive_blockquote_lines_are_one_quotation(self) -> None:
        """A quote split at the author's line wrap is the layout-cut defect, again."""
        raw = "> the first half of a sentence that runs on\n> and the second half of it\n\ntext"
        self.assertEqual(dqa.blockquotes(raw),
                         ["the first half of a sentence that runs on and the second half of it"])

    def test_a_blank_line_separates_two_quotations(self) -> None:
        raw = "> first quotation, long enough to count here\n\n> second one, also long enough\n"
        self.assertEqual(len(dqa.blockquotes(raw)), 2)

    def test_the_wrapper_an_author_typed_is_not_part_of_the_quote(self) -> None:
        self.assertEqual(dqa.clean('*"a quoted sentence"*'), "a quoted sentence")

    def test_backticked_identifiers_are_not_quotations(self) -> None:
        """122 of 207 candidate spans were file paths, digests and epistemic tags."""
        raw = "The digest is `7da156e82cb7014f837d8c29374d888cb99ecc3268d1c383af2c3d0832b988bb`."
        self.assertEqual(dqa.quotations(raw), [])

    def test_a_short_span_is_not_a_quotation(self) -> None:
        self.assertEqual(dqa.quotations("> too short\n"), [])


class Buckets(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.corpus = self.root / "files" / "fulltext"
        self.corpus.mkdir(parents=True)
        (self.corpus / "PMID11111111_Paper.xml").write_text(PAPER, encoding="utf-8")
        (self.corpus / "PMID22222222_Other.xml").write_text(OTHER, encoding="utf-8")
        self.dossiers = self.root / "disease-models/wwox/research/fulltext_dossiers"
        self.dossiers.mkdir(parents=True)
        self.manifests = self.root / "disease-models/wwox/research/deepdive_manifests"
        self.manifests.mkdir(parents=True)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, name: str, body: str) -> None:
        (self.dossiers / name).write_text(body, encoding="utf-8")

    def run_audit(self) -> list[dict]:
        return dqa.audit(self.root, self.corpus, "wwox")["results"]

    def test_a_quotation_of_its_own_paper_is_verbatim(self) -> None:
        self.write("PMID11111111.md",
                   "> The heterozygote is indistinguishable from the wild type on every "
                   "measure.\n")
        entry = self.run_audit()[0]
        self.assertEqual(entry["verbatim"], 1)
        self.assertEqual(entry["not_found"], [])

    def test_a_quotation_of_another_paper_is_located_not_condemned(self) -> None:
        """The bucket that earns the tool: it says WHERE, so a reader can judge."""
        self.write("PMID11111111.md",
                   "> A sentence that lives only in the other paper and nowhere else at all.\n")
        entry = self.run_audit()[0]
        self.assertEqual(entry["not_found"], [])
        self.assertEqual([pmid for pmid, _ in entry["elsewhere"]], ["22222222"])

    def test_an_ellipsis_makes_it_stitched_and_not_not_found(self) -> None:
        """The shape `deepdive_manifest.validate` refuses by name, unrefused in prose."""
        self.write("PMID11111111.md",
                   "> Mutant rats had significantly increased concentrations … inorganic "
                   "phosphate.\n")
        entry = self.run_audit()[0]
        self.assertEqual(len(entry["stitched"]), 1)
        self.assertEqual(entry["not_found"], [])
        self.assertEqual(entry["verbatim"], 0)

    def test_a_coined_phrase_lands_in_not_found_and_that_is_correct(self) -> None:
        self.write("PMID11111111.md", "The reading calls this “half protein, normal brain”.\n")
        entry = self.run_audit()[0]
        self.assertEqual(len(entry["not_found"]), 1)

    def test_a_paper_with_no_readable_surface_is_undecidable_not_clean(self) -> None:
        self.write("PMID99999999.md", "> A quotation of a paper this checkout does not hold.\n")
        entry = [e for e in self.run_audit() if e["pmid"] == "99999999"][0]
        self.assertEqual(entry["undecidable"], 1)
        self.assertEqual(entry["verbatim"], 0)
        self.assertEqual(entry["not_found"], [])

    def test_a_declared_artifact_beats_a_filename_guess(self) -> None:
        """`locator_audit` learned this by manufacturing a failure; it is the same rule."""
        (self.corpus / "PMID11111111_wrong_guess.xml").write_text(OTHER, encoding="utf-8")
        (self.manifests / "PMID11111111.json").write_text(json.dumps({
            "source_artifacts": [{"path": "files/fulltext/PMID11111111_Paper.xml",
                                  "sha256": "x", "kind": "article_text"}]}), encoding="utf-8")
        self.write("PMID11111111.md",
                   "> The heterozygote is indistinguishable from the wild type on every "
                   "measure.\n")
        entry = self.run_audit()[0]
        self.assertEqual(entry["verbatim"], 1)


class TheSearchMaySayWhereAndNeverVerified(unittest.TestCase):
    """🔴 The distinction the `elsewhere` search was built on, pinned so it cannot erode."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "suspect.html"
        # A C0 control is exactly what `_refuse_suspect_surface` refuses, and exactly what a
        # locating search must be able to see past.
        self.path.write_text("<p>a sentence with a \x01 control character in it</p>",
                             encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_the_screen_still_refuses_the_surface_for_certification(self) -> None:
        self.assertEqual(dqa.read_text_surfaces(self.path), [])

    def test_the_diagnostic_reader_can_still_locate_a_sentence_in_it(self) -> None:
        text = dqa.diagnostic_text(self.path)
        self.assertIn("control character in it", text)

    def test_the_module_writes_nothing(self) -> None:
        """What makes 'may say where, may never say verified' a property and not an intention."""
        source = Path(dqa.__file__).read_text(encoding="utf-8")
        for forbidden in ("write_text(", "write_bytes(", "open(", "append_receipt"):
            self.assertNotIn(forbidden, source, f"this module must not {forbidden}")


class TheCliIsDriven(unittest.TestCase):
    """``main`` run as a process over a fixture root: the buckets it prints, and its totals.

    Until 2026-09-10 nothing in this file entered ``main``; the buckets were tested through
    ``audit()`` and the report a reader actually sees — the per-dossier line, the totals, the
    NOTHING AUDITED sentinel — was certified by no case (retrospective § 9.3).
    """

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.corpus = self.root / "files" / "fulltext"
        self.corpus.mkdir(parents=True)
        (self.corpus / "PMID11111111_Paper.xml").write_text(PAPER, encoding="utf-8")
        (self.corpus / "PMID22222222_Other.xml").write_text(OTHER, encoding="utf-8")
        self.dossiers = self.root / "disease-models/wwox/research/fulltext_dossiers"
        self.dossiers.mkdir(parents=True)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_every_bucket_reaches_the_report_with_its_own_label(self) -> None:
        (self.dossiers / "PMID11111111.md").write_text(
            "> The heterozygote is indistinguishable from the wild type on every measure.\n"
            "\n"
            "> Mutant rats had significantly increased concentrations … inorganic phosphate.\n"
            "\n"
            "> A sentence that lives only in the other paper and nowhere else at all.\n"
            "\n"
            "The reading calls this “a coined phrase that no paper anywhere contains”.\n",
            encoding="utf-8")
        result = run_cli("--root", str(self.root), "--corpus", str(self.corpus))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PMID11111111.md", result.stdout)
        self.assertRegex(result.stdout, r"4 quotation\(s\) ·\s+1 verbatim ·\s+1 stitched ·"
                                        r"\s+1 elsewhere ·\s+1 not found")
        self.assertIn("[stitched] Mutant rats", result.stdout)
        self.assertIn("[elsewhere → PMID 22222222] A sentence that lives", result.stdout)
        self.assertIn("[not found] a coined phrase", result.stdout)
        match = SUMMARY.search(result.stdout)
        self.assertIsNotNone(match, result.stdout)
        self.assertEqual([int(g) for g in match.groups()], [4, 1, 1, 1, 1, 1, 0])
        self.assertNotIn("NOTHING AUDITED", result.stdout)
        self.assertIn("HOW TO READ THIS", result.stdout)

    def test_an_unreadable_paper_is_undecidable_in_the_report(self) -> None:
        (self.dossiers / "PMID99999999.md").write_text(
            "> A quotation of a paper this checkout does not hold anywhere.\n", encoding="utf-8")
        result = run_cli("--root", str(self.root), "--corpus", str(self.corpus))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("no readable text surface for this paper here", result.stdout)
        match = SUMMARY.search(result.stdout)
        self.assertEqual([int(g) for g in match.groups()], [1, 1, 0, 0, 0, 0, 1])

    def test_no_dossiers_is_announced_not_reported_as_clean(self) -> None:
        result = run_cli("--root", str(self.root), "--corpus", str(self.corpus))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("NOTHING AUDITED", result.stdout)
        self.assertEqual([int(g) for g in SUMMARY.search(result.stdout).groups()],
                         [0, 0, 0, 0, 0, 0, 0])


class TheRealDossiersAreAudited(unittest.TestCase):
    """The tool over this checkout's own dossiers — what a session actually runs.

    The dossiers are tracked; the text surfaces under ``files/`` mostly are not, so on a host
    without them every quotation is ``undecidable`` and that is the correct answer. What this
    case pins is that the corpus-wide run completes, reports every dossier, and writes nothing.
    """

    def test_the_corpus_wide_run_reports_every_dossier_and_writes_nothing(self) -> None:
        dossiers = ROOT / "disease-models/wwox/research/fulltext_dossiers"
        named = sorted(p for p in dossiers.glob("PMID*.md")) if dossiers.is_dir() else []
        if not named:
            self.skipTest(f"skipped: no dossiers under {dossiers} on this host")
        before = {p: p.read_bytes() for p in named}
        result = run_cli("--root", str(ROOT))
        self.assertEqual(result.returncode, 0, result.stderr[-2000:])
        match = SUMMARY.search(result.stdout)
        self.assertIsNotNone(match, result.stdout[-2000:])
        total, dossier_count = int(match.group(1)), int(match.group(2))
        self.assertEqual(dossier_count, len(named),
                         "every PMID-named dossier must appear in the totals")
        self.assertGreater(total, 0, "the real dossiers quote their papers")
        for path in named:
            self.assertIn(path.name, result.stdout)
        self.assertEqual({p: p.read_bytes() for p in named}, before,
                         "the audit must never write a dossier")


if __name__ == "__main__":
    unittest.main(verbosity=2)
