#!/usr/bin/env python3
"""Tests for xlsx_to_text.py: shared strings, sheet names, identity grouping, control reporting."""
import contextlib, io, sys, tempfile, unittest, zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import xlsx_to_text as X

WB = ('<?xml version="1.0"?><workbook xmlns:r="r"><sheets><sheet name="HI" sheetId="1" r:id="rId1"/>'
      '<sheet name="LPS" sheetId="2" r:id="rId2"/></sheets></workbook>')
RELS = ('<Relationships><Relationship Id="rId1" Type="t" Target="worksheets/sheet1.xml"/>'
        '<Relationship Id="rId2" Type="t" Target="worksheets/sheet2.xml"/></Relationships>')
SS = '<sst><si><t>Seizure #</t></si><si><t>BSS</t></si></sst>'
S1 = '<worksheet><sheetData><row><c t="s"><v>0</v></c><c t="s"><v>1</v></c></row><row><c><v>3</v></c><c><v>6</v></c></row></sheetData></worksheet>'
S2 = '<worksheet><sheetData><row><c t="inlineStr"><is><t>only here</t></is></c></row></sheetData></worksheet>'


def make(path: Path, extra: str = "") -> Path:
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("xl/workbook.xml", WB)
        z.writestr("xl/_rels/workbook.xml.rels", RELS)
        z.writestr("xl/sharedStrings.xml", SS)
        z.writestr("xl/worksheets/sheet1.xml", S1 + extra)
        z.writestr("xl/worksheets/sheet2.xml", S2)
    return path


class XlsxToText(unittest.TestCase):
    def test_reads_sheets_strings_and_names_what_it_examined(self):
        with tempfile.TemporaryDirectory() as d:
            p = make(Path(d) / "a.xlsx")
            out = X.read_workbook(p)
            self.assertIn("sha256=", out)
            self.assertIn("SHEETS HI | LPS", out)
            self.assertIn("Seizure #\tBSS", out)
            self.assertIn("3\t6", out)
            self.assertIn("only here", out)

    def test_dedupe_groups_byte_identical_workbooks(self):
        with tempfile.TemporaryDirectory() as d:
            a = make(Path(d) / "a.xlsx")
            b = Path(d) / "b.xlsx"
            b.write_bytes(a.read_bytes())
            c = make(Path(d) / "c.xlsx", extra="<!-- different -->")
            out = X.dedupe([a, b, c])
            self.assertEqual(out.count("IDENTICAL"), 1)
            self.assertIn("a.xlsx, b.xlsx", out)
            self.assertIn("unique", out)

    def test_a_legacy_xls_is_read_through_xlrd_and_printed_like_xlsx(self):
        sheet = SimpleNamespace(name="S1", nrows=3,
                                row_values=lambda i: [["Gene", "FC"], ["WWOX", 3.0], ["X", 7]][i],
                                row_types=lambda i: [[1, 1], [1, 2], [1, 5]][i])
        fake = SimpleNamespace(__version__="0.test", XL_CELL_ERROR=5, error_text_from_code={7: "#DIV/0!"},
                               open_workbook=lambda p: SimpleNamespace(sheet_names=lambda: ["S1"], sheets=lambda: [sheet]))
        with tempfile.TemporaryDirectory() as d, mock.patch.dict(sys.modules, {"xlrd": fake}):
            p = Path(d) / "named.xlsx"                     # the bytes decide, not the name
            p.write_bytes(X.OLE2 + b"rest")
            out = X.read_workbook(p)
            self.assertIn("SHEETS S1", out)
            self.assertIn("WWOX\t3\n", out)
            self.assertIn("X\t#DIV/0!", out)
            self.assertIn("1 further rows not printed", X.read_workbook(p, max_rows=2))

    def test_without_xlrd_an_xls_says_why_and_how(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.dict(sys.modules, {"xlrd": None}):
            p = Path(d) / "a.xls"
            p.write_bytes(X.OLE2)
            with self.assertRaises(X.NotRead) as why:
                X.read_workbook(p)
            self.assertIn("python3 -P -E", str(why.exception))

    def test_a_web_page_saved_as_xls_is_not_read_and_the_run_exits_1(self):
        with tempfile.TemporaryDirectory() as d:
            bad = Path(d) / "page.xls"
            bad.write_bytes(b"<!doctype html><title>challenge</title>")
            good = make(Path(d) / "a.xlsx")
            said = io.StringIO()
            with contextlib.redirect_stdout(said):
                code = X.main([str(bad), str(good)])
            self.assertEqual(code, 1)
            self.assertIn("NOT_READ page.xls is neither", said.getvalue())
            self.assertIn("SHEETS HI | LPS", said.getvalue())

    def test_control_characters_are_reported_not_stripped(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "x.xlsx"
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("xl/workbook.xml", WB)
                z.writestr("xl/_rels/workbook.xml.rels", RELS)
                z.writestr("xl/worksheets/sheet1.xml",
                           '<worksheet><sheetData><row><c t="inlineStr"><is><t>a\x1eb</t></is></c></row></sheetData></worksheet>')
                z.writestr("xl/worksheets/sheet2.xml", S2)
            self.assertIn("CONTROL_CHARACTERS_REPORTED 1", X.read_workbook(p))


if __name__ == "__main__":
    unittest.main(verbosity=2)
