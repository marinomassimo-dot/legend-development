#!/usr/bin/env python3
"""Regression checks for figure_ppi_preflight.py."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import fitz

from figure_ppi_preflight import inventory

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCRIPT = HERE / "figure_ppi_preflight.py"


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT,
                          capture_output=True, text=True, timeout=300)


def fixture_pdf(path: Path) -> None:
    document = fitz.open()
    raster_page = document.new_page(width=612, height=792)
    pixmap = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 600, 300), False)
    raster_page.insert_image(fitz.Rect(72, 72, 360, 216), pixmap=pixmap)
    vector_page = document.new_page(width=612, height=792)
    vector_page.draw_rect(fitz.Rect(72, 72, 144, 144))
    document.save(path)
    document.close()


class FigurePpiPreflightTest(unittest.TestCase):
    def test_reports_effective_ppi_and_vector_page(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "fixture.pdf"
            document = fitz.open()
            raster_page = document.new_page(width=612, height=792)
            pixmap = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 600, 300), False)
            raster_page.insert_image(fitz.Rect(72, 72, 360, 216), pixmap=pixmap)
            vector_page = document.new_page(width=612, height=792)
            vector_page.draw_rect(fitz.Rect(72, 72, 144, 144))
            document.save(path)
            document.close()

            result = inventory(path)

        self.assertEqual(result["page_count"], 2)
        ceiling = result["pages"][0]["raster_ceiling"]
        self.assertEqual(ceiling["minimum"], 150.0)
        self.assertEqual(ceiling["maximum"], 150.0)
        self.assertIsNone(result["pages"][1]["raster_ceiling"])
        self.assertEqual(result["pages"][1]["note"], "vector_or_text_only")


class TheCliIsDriven(unittest.TestCase):
    """``main`` as a subprocess: the text report, the JSON report, and a missing PDF."""

    def test_text_and_json_reports_through_main(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "fixture.pdf"
            fixture_pdf(path)
            text = run_cli(str(path))
            self.assertEqual(text.returncode, 0, text.stderr)
            self.assertIn(f"{path}: 2 pages", text.stdout)
            self.assertIn("page 1: 1 raster image(s); effective PPI min/median/max "
                          "150.0/150.0/150.0", text.stdout)
            self.assertIn("page 2: vector/text only; no raster PPI ceiling", text.stdout)

            machine = run_cli(str(path), "--json")
            self.assertEqual(machine.returncode, 0, machine.stderr)
            payload = json.loads(machine.stdout)
            self.assertEqual(payload["page_count"], 2)
            self.assertEqual(payload["pages"][0]["raster_ceiling"]["minimum"], 150.0)
            self.assertIsNone(payload["pages"][1]["raster_ceiling"])

    def test_a_missing_pdf_is_not_reported_as_zero_pages(self) -> None:
        result = run_cli("/nonexistent/paper.pdf")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("0 pages", result.stdout)


class TheRealPdfIsInventoried(unittest.TestCase):
    """A preflight over a real PDF under ``files/fulltext`` — read, digested, never modified."""

    def test_the_first_real_pdf_yields_a_full_inventory(self) -> None:
        corpus = ROOT / "files" / "fulltext"
        pdfs = sorted(corpus.glob("PMID*.pdf")) if corpus.is_dir() else []
        if not pdfs:
            self.skipTest("skipped: no PDF under files/fulltext on this host (files/ is gitignored)")
        pdf = pdfs[0]
        digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
        result = run_cli(str(pdf.relative_to(ROOT)), "--json")
        self.assertEqual(result.returncode, 0, result.stderr[-2000:])
        payload = json.loads(result.stdout)
        self.assertEqual(payload["source"], pdf.relative_to(ROOT).as_posix())
        self.assertGreaterEqual(payload["page_count"], 1)
        self.assertEqual(len(payload["pages"]), payload["page_count"])
        for page in payload["pages"]:
            self.assertIn(page["note"], ("vector_or_text_only", "measured_before_render"))
            self.assertEqual(page["raster_ceiling"] is None, page["note"] == "vector_or_text_only")
        self.assertEqual(hashlib.sha256(pdf.read_bytes()).hexdigest(), digest,
                         "a preflight modified the PDF it inventoried")


if __name__ == "__main__":
    unittest.main()
