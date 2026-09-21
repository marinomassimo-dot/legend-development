#!/usr/bin/env python3
"""Tests for `pdf_text_extract.py` — mostly about the zeros, because zeros are the risk.

The extraction path is the easy half and is covered by a synthesized single-stream PDF. The
half that earns its tests is the part that decides whether a **negative** may be reported:
the positive-control gate, and the binary barrier that stopped a font-program byte run from
being counted as the inactive control peptide on 2026-09-21.

Run: `python3 framework/scripts/test_pdf_text_extract.py`
"""

from __future__ import annotations

import io
import unittest
import zlib
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

import pdf_text_extract as tool


def make_pdf(path: Path, lines: list[str]) -> Path:
    """A minimal PDF carrying one FlateDecode content stream of show-text operators."""
    body = "\n".join(f"({line}) Tj" for line in lines) + "\nT*\n"
    stream = zlib.compress(body.encode("latin-1"))
    path.write_bytes(b"%PDF-1.4\n<< /Length "
                     + str(len(stream)).encode()
                     + b" /Filter /FlateDecode >>\nstream\n" + stream + b"\nendstream\n%%EOF\n")
    return path


class Extraction(unittest.TestCase):
    def test_inflates_a_content_stream_and_recovers_its_strings(self):
        with TemporaryDirectory() as tmp:
            pdf = make_pdf(Path(tmp) / "a.pdf", ["Zfra1-31 protects", "SH-SY5Y cells"])
            text = tool.raw_text(pdf)
        self.assertIn("Zfra1-31 protects", text)
        self.assertIn("SH-SY5Y cells", text)

    def test_a_stream_without_show_text_operators_contributes_nothing(self):
        with TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "b.pdf"
            stream = zlib.compress(b"0 0 100 100 re f\n")
            pdf.write_bytes(b"%PDF-1.4\nstream\n" + stream + b"\nendstream\n")
            self.assertEqual(tool.raw_text(pdf).strip(), "")

    def test_an_undecompressable_stream_is_skipped_not_fatal(self):
        with TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "c.pdf"
            pdf.write_bytes(b"%PDF-1.4\nstream\nnot-deflate-at-all\nendstream\n")
            self.assertEqual(tool.raw_text(pdf), "")

    def test_octal_and_backslash_escapes_resolve(self):
        self.assertEqual(tool._unescape(rb"a\(b\)c"), b"a(b)c")
        self.assertEqual(tool._unescape(rb"\101\102"), b"AB")


class Normalisation(unittest.TestCase):
    def test_ligatures_fold_so_a_common_word_is_findable(self):
        # Untouched, `significant` is spelled with a single fi glyph and a search misses it.
        self.assertEqual(tool.normalise("signiﬁcant"), "significant")
        self.assertEqual(tool.count(tool.normalise("signiﬁcant"), "significant"), 1)

    def test_hyphenation_across_a_line_break_is_rejoined(self):
        self.assertEqual(tool.normalise("mito-\nchondrial"), "mitochondrial")

    def test_a_hyphen_not_at_a_line_break_is_preserved(self):
        self.assertEqual(tool.normalise("Goto-Kakizaki"), "Goto-Kakizaki")

    def test_an_interleaved_language_tag_does_not_break_a_phrase(self):
        """Word-generated PDFs glue `en-US` between every run; a phrase must still match."""
        raw = "WWOXen-US-en-USmitochondriaen-USinteractions"
        self.assertEqual(tool.normalise(raw), "WWOX-mitochondriainteractions")
        supp = "theen-USeffecten-USofen-UShighen-USglucose"
        self.assertEqual(tool.count(tool.normalise(supp), "effectofhighglucose"), 1)

    def test_a_language_tag_standing_alone_as_data_survives(self):
        self.assertEqual(tool.normalise("locale en-US only"), "locale en-US only")


class Counting(unittest.TestCase):
    def test_case_and_wrapping_do_not_hide_a_term(self):
        self.assertEqual(tool.count("we used SIRNA here", "siRNA"), 1)
        self.assertEqual(tool.count("knock-\ndown", "knockdown"), 1)
        self.assertEqual(tool.count("S H - S Y 5 Y", "SH-SY5Y"), 1)

    def test_a_term_genuinely_absent_counts_zero(self):
        self.assertEqual(tool.count("differentiated neuronal cells", "CRISPR"), 0)

    # --- the regression that this module exists for -------------------------------------
    def test_binary_noise_cannot_manufacture_a_hit(self):
        """`s\\x128G` inside an image stream must not be counted as `S8G`.

        The inactive Zfra control peptide is `S8G`. On 2026-09-21 a tolerant matcher run over
        unfiltered inflate output found exactly one `S8G` in PMID 35984507 — in a font
        program — and a reading was one step away from recording that the specificity control
        existed. It does not.
        """
        raw = "...\xff\xff\xffg$\xe9\xff\xeds\x128G@&\xaa\xf7..."
        self.assertEqual(tool.count(tool.searchable(raw), "S8G"), 0)

    def test_substituting_a_space_would_not_have_been_enough(self):
        """Guards the fix itself: the barrier must be unbridgeable by the tolerance."""
        raw = "s\x128G"
        self.assertEqual(tool.count(raw.replace("\x12", " "), "S8G"), 1)   # the failed fix
        self.assertEqual(tool.count(tool.searchable(raw), "S8G"), 0)       # the real one

    def test_accented_latin_survives_the_barrier(self):
        # Seica/Seiça and the +/- sign are real text, not noise, and must not be cut out.
        self.assertIn("ç", tool.searchable("Seiça"))
        self.assertEqual(tool.count(tool.searchable("mean ± SEM"), "SEM"), 1)


class ControlGate(unittest.TestCase):
    def _run(self, lines, controls, query):
        with TemporaryDirectory() as tmp:
            pdf = make_pdf(Path(tmp) / "p.pdf", lines)
            out = io.StringIO()
            with redirect_stdout(out):
                code = tool.main(["search", str(pdf), "--controls", controls, "--query", query])
        return code, out.getvalue()

    def test_live_controls_let_the_query_through(self):
        code, out = self._run(["Zfra1-31 in SH-SY5Y cells"], "Zfra1-31,SH-SY5Y", "siRNA")
        self.assertEqual(code, 0)
        self.assertIn("query:", out)
        self.assertRegex(out, r"0\s+siRNA")

    def test_a_dead_control_refuses_to_report_any_zero(self):
        code, out = self._run(["Zfra1-31 in SH-SY5Y cells"],
                              "Zfra1-31,NOT-IN-THIS-PAPER", "siRNA")
        self.assertEqual(code, 1)
        self.assertIn("INSTRUMENT_UNVERIFIED", out)
        self.assertNotIn("query:", out)

    def test_a_pdf_with_no_readable_text_layer_fails_the_gate(self):
        """A scanned, image-only PDF must not silently report every term as absent."""
        with TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "scan.pdf"
            pdf.write_bytes(b"%PDF-1.4\n%%EOF\n")
            out = io.StringIO()
            with redirect_stdout(out):
                code = tool.main(["search", str(pdf), "--controls", "the", "--query", "siRNA"])
        self.assertEqual(code, 1)
        self.assertIn("INSTRUMENT_UNVERIFIED", out.getvalue())

    def test_a_missing_file_is_an_error_not_an_empty_reading(self):
        out = io.StringIO()
        with redirect_stdout(out):
            code = tool.main(["search", "/nonexistent.pdf", "--controls", "x", "--query", "y"])
        self.assertEqual(code, 2)


class Prose(unittest.TestCase):
    def test_duplicate_segments_collapse(self):
        text = "The cells were differentiated for seven days.\n" * 3
        self.assertEqual(tool.prose(text).count("differentiated"), 1)

    def test_binary_heavy_segments_are_dropped(self):
        keep = "Differentiated SH-SY5Y cells were exposed to high glucose for forty-eight hours."
        self.assertIn("SH-SY5Y", tool.prose(keep + "\n" + "\xff\xfe\x01\x02" * 40))
        self.assertNotIn("\xff", tool.prose(keep + "\n" + "\xff\xfe\x01\x02" * 40))


if __name__ == "__main__":
    unittest.main(verbosity=2)
