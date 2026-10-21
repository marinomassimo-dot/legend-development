#!/usr/bin/env python3
"""supplement_symbol_search finds a symbol in a workbook row, with its sheet, and says nothing when absent."""
import importlib.util
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sss", ROOT / "framework" / "scripts" / "supplement_symbol_search.py")
sss = importlib.util.module_from_spec(spec)
sys.modules["sss"] = sss
spec.loader.exec_module(sss)


def make_xlsx(path: Path) -> None:
    ws = ('<worksheet><sheetData><row r="1"><c r="A1" t="s"><v>0</v></c></row>'
          '<row r="2"><c r="A2" t="s"><v>1</v></c><c r="B2" t="s"><v>2</v></c><c r="C2"><v>-1.02</v></c></row></sheetData></worksheet>')
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("xl/workbook.xml", '<workbook><sheets><sheet name="HPC" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels", '<Relationships><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/sharedStrings.xml", "<sst><si><t>Symbol</t></si><si><t>ENSMUSG1</t></si><si><t>CACNA1H</t></si></sst>")
        z.writestr("xl/worksheets/sheet1.xml", ws)


class T(unittest.TestCase):
    def test_hit_has_sheet_and_row(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "files" / "supplement" / "PMID1").mkdir(parents=True)
            make_xlsx(root / "files" / "supplement" / "PMID1" / "a.xlsx")
            res = sss.run(["CACNA1H", "CACNA1G"], root)
            self.assertEqual(len(res), 1)
            hit = res[0]["hits"][0]
            self.assertEqual(hit["sheet"], "HPC")
            self.assertIn(("B", "CACNA1H"), hit["row"])
            self.assertIn(("C", "-1.02"), hit["row"])

    def test_absent_symbol_is_an_empty_result(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "files" / "supplement" / "PMID1").mkdir(parents=True)
            make_xlsx(root / "files" / "supplement" / "PMID1" / "a.xlsx")
            self.assertEqual(sss.run(["CACNA1I"], root), [])

    def test_whole_token_only(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "files" / "supplement" / "p").mkdir(parents=True)
            (root / "files" / "supplement" / "p" / "t.txt").write_text("XCACNA1H2 only\nCACNA1H here\n")
            res = sss.run(["CACNA1H"], root)
            self.assertEqual([h["line"] for h in res[0]["hits"]], [2])


if __name__ == "__main__":
    unittest.main()
