#!/usr/bin/env python3
"""Tests for docx_to_text.py: paragraphs, table rows, media listing, deleted text, control reporting."""
import sys, tempfile, unittest, zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docx_to_text as D

BODY = ('<w:document xmlns:w="w"><w:body>'
        '<w:p><w:r><w:t>Supplementary Table 1</w:t></w:r></w:p>'
        '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Target</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>Dilution</w:t></w:r></w:p></w:tc></w:tr>'
        '<w:tr><w:tc><w:p><w:r><w:t>GFAP</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>1:500</w:t></w:r><w:r><w:tab/></w:r><w:r><w:t>WB</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
        '<w:p><w:r><w:t>kept</w:t></w:r><w:del><w:r><w:delText>gone</w:delText></w:r></w:del></w:p>'
        '</w:body></w:document>')


def make(path: Path, body: str = BODY, media: bool = True) -> Path:
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("word/document.xml", body)
        if media:
            z.writestr("word/media/image1.tiff", b"II*\x00" + b"0" * 40)
    return path


class DocxToText(unittest.TestCase):
    def test_paragraph_table_and_identity(self):
        with tempfile.TemporaryDirectory() as d:
            out = D.read_docx(make(Path(d) / "a.docx"))
        self.assertIn("sha256=", out)
        self.assertIn("Supplementary Table 1", out)
        self.assertIn("Target | Dilution", out)
        self.assertIn("GFAP | 1:500 WB", out)
        self.assertIn("COUNTS paragraphs=2 tables=1 table_rows=2 embedded_media=1", out)

    def test_media_listed_and_not_read(self):
        with tempfile.TemporaryDirectory() as d:
            out = D.read_docx(make(Path(d) / "a.docx"))
        self.assertIn("MEDIA word/media/image1.tiff bytes=44 (not read as text)", out)

    def test_deleted_text_is_excluded(self):
        with tempfile.TemporaryDirectory() as d:
            out = D.read_docx(make(Path(d) / "a.docx"))
        self.assertIn("kept", out)
        self.assertNotIn("gone", out)

    def test_control_characters_are_reported_not_stripped(self):
        body = '<w:document xmlns:w="w"><w:body><w:p><w:r><w:t>a\x1eb</w:t></w:r></w:p></w:body></w:document>'
        with tempfile.TemporaryDirectory() as d:
            out = D.read_docx(make(Path(d) / "x.docx", body, media=False))
        self.assertIn("CONTROL_CHARACTERS_REPORTED 1", out)
        self.assertIn("a\x1eb", out)

    def test_parts_listing_is_optional(self):
        with tempfile.TemporaryDirectory() as d:
            p = make(Path(d) / "a.docx")
            self.assertNotIn("PARTS ", D.read_docx(p))
            self.assertIn("PARTS word/document.xml", D.read_docx(p, parts=True))


if __name__ == "__main__":
    unittest.main()
