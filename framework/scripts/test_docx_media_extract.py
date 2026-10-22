#!/usr/bin/env python3
"""Tests for docx_media_extract.py: unchanged media, EMF+ bitmap decode, honest refusals."""
import struct, sys, tempfile, unittest, zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docx_media_extract as M


def emf_with_bitmap(w, h, pf=0xE200B, pixels=None):
    bpp = 4
    stride = w * bpp
    pixels = pixels or bytes((10, 20, 30, 255)) * (w * h)  # B, G, R, A
    obj = struct.pack("<II", 0xDBC01002, 1) + struct.pack("<iiiII", w, h, stride, pf, 0) + pixels
    rec = struct.pack("<HHII", 0x4008, (5 << 8) | 1, 12 + len(obj), len(obj)) + obj
    comment = b"EMF+" + rec
    emr = struct.pack("<II", 70, 12 + len(comment)) + struct.pack("<I", len(comment)) + comment
    header = struct.pack("<II", 1, 8)
    return header + emr


def make(path, members):
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("word/document.xml", "<w:document xmlns:w='w'/>")
        for n, b in members.items():
            z.writestr("word/media/" + n, b)
    return path


class Extract(unittest.TestCase):
    def test_media_written_unchanged_and_emf_decoded(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            emf = emf_with_bitmap(3, 2)
            make(d / "a.docx", {"image1.emf": emf, "image2.png": b"\x89PNGfake"})
            lines = M.extract(d / "a.docx", d / "out")
            self.assertEqual((d / "out" / "image1.emf").read_bytes(), emf)
            self.assertEqual((d / "out" / "image2.png").read_bytes(), b"\x89PNGfake")
            png = (d / "out" / "image1_decoded.png").read_bytes()
            self.assertTrue(png.startswith(b"\x89PNG\r\n\x1a\n"))
            self.assertEqual(struct.unpack(">II", png[16:24]), (3, 2))
            self.assertTrue(any("decoded=image1_decoded.png 3x2 32bppPARGB" in l for l in lines))

    def test_pixel_values_survive(self):
        bmp = M.emf_plus_bitmap(emf_with_bitmap(2, 1, pixels=bytes((1, 2, 3, 255, 4, 5, 6, 255))))
        self.assertEqual(bmp[:2], (2, 1))
        self.assertEqual(bmp[2], bytes((3, 2, 1, 6, 5, 4)))  # BGRA -> RGB

    def test_vector_emf_is_not_decoded_and_says_so(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            make(d / "b.docx", {"image1.emf": struct.pack("<II", 1, 8) + b"\x00" * 16})
            lines = M.extract(d / "b.docx", d / "out")
            self.assertIn("not decoded", lines[0])
            self.assertFalse((d / "out" / "image1_decoded.png").exists())

    def test_unsupported_pixel_format_is_refused(self):
        self.assertIsNone(M.emf_plus_bitmap(emf_with_bitmap(2, 2, pf=0x30101)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
