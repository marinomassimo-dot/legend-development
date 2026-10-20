#!/usr/bin/env python3
"""Tests for xlsx_to_text.py: shared strings, sheet names, identity grouping, control reporting."""
import sys, tempfile, unittest, zipfile
from pathlib import Path

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
