#!/usr/bin/env python3
"""Regression checks for figure_ppi_preflight.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import fitz

from figure_ppi_preflight import inventory


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


if __name__ == "__main__":
    unittest.main()
