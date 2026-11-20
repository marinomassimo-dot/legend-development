#!/usr/bin/env python3
"""sheet_query.py: verbatim bullets with file and line, comparable and dated caveats, batch-level absences, origin groups. Synthetic sheets only."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sheet_query as sq  # noqa: E402

SHEET = """# ADV-098 batch 99: test
Intro line.

## COMPARABLE?
- **Alphaxol potency is one origin, quoted.** Alphaxol: all rows come from ONE document.
- **Betaxol only.** Betaxol is measured at -60 mV.

## Alphaxol (CHEMBL1)
- **Potency (2 rows):** IC50 10 nM at -80 mV (2011).
- **Exposure:** brain concentration in adult mouse, total.
- **Not found by these routes:** a juvenile value for Alphaxol.

## Betaxol (CHEMBL2)
- **Potency:** IC50 20 nM.

## What is not found by these routes
Any measured exposure for the two agents; a harm profile.

## Dated line 2026-11-20: Alphaxol correction
The 10 nM value is a unit slip; the paper says 10 uM.
"""
TSV = "agent\\ttarget_genes\\tvalue\\tunits\\tdocument\\tyear\\nalphaxol\\tG1\\t10\\tnM\\tDOC1\\t2011\\nalphaxol\\tG1\\t10\\tnM\\tDOC2\\t2020\\nalphaxol\\tG2\\t50\\tnM\\tDOC1\\t2011\\nbetaxol\\tG1\\t20\\tnM\\tDOC3\\t2015\\n".replace("\\t", "\t").replace("\\n", "\n")


class SheetQuery(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        (self.dir / "BATCH99_test.md").write_text(SHEET, encoding="utf-8")
        (self.dir / "activities_expected_targets.tsv").write_text(TSV, encoding="utf-8")

    def test_every_returned_text_is_verbatim_at_its_file_and_line(self):
        a = sq.query(self.dir, "Alphaxol", "all")
        lines = (self.dir / "BATCH99_test.md").read_text().splitlines()
        shown = [b for k in ("bullets", "comparable", "corrections", "batch_caveats") for b in a[k]]
        self.assertTrue(shown)
        for b in shown:
            self.assertIn(b["text"], lines[b["line"] - 1])

    def test_the_question_picks_the_quantity_and_the_caveats_come_with_it(self):
        a = sq.query(self.dir, "Alphaxol", "exposure")
        self.assertTrue(any("brain concentration" in b["text"] for b in a["bullets"]))
        self.assertFalse(any("IC50 10 nM" in b["text"] for b in a["bullets"]))                          # the potency bullet is not an exposure answer
        self.assertEqual(len(a["comparable"]), 1); self.assertIn("one origin", a["comparable"][0]["text"])
        self.assertEqual(len(a["corrections"]), 1); self.assertIn("unit slip", a["corrections"][0]["text"])   # a dated PARAGRAPH is indexed, not only bullets
        self.assertTrue(any("harm profile" in b["text"] for b in a["batch_caveats"]))                    # the absence paragraph names no agent and still comes back

    def test_an_agent_name_is_matched_as_a_whole_word_and_another_agent_is_not_pulled_in(self):
        a = sq.query(self.dir, "Betaxol", "comparable")
        self.assertEqual(len(a["comparable"]), 1)                                                    # only the bullet that names Betaxol
        self.assertEqual(a["bullets"], [])
        self.assertEqual(sq.query(self.dir, "Alpha", "all")["bullets"], [])                              # a prefix is not the name
        self.assertIn("not named in these sheets", sq.render(sq.query(self.dir, "Gammaxol", "all")))

    def test_rows_from_one_document_are_one_origin_and_the_same_value_in_two_documents_is_flagged(self):
        o = sq.query(self.dir, "Alphaxol", "potency")["origin"]
        self.assertEqual(o["documents"], {"DOC1 (2011)": 2, "DOC2 (2020)": 1})
        self.assertEqual([(r["target"], r["value"], r["documents"]) for r in o["same_value_in_several_documents"]], [("G1", "10", ["DOC1", "DOC2"])])
        self.assertIn("SAME VALUE IN SEVERAL DOCUMENTS", sq.render(sq.query(self.dir, "Alphaxol", "potency")))
        self.assertEqual(sq.query(self.dir, "Alphaxol", "exposure")["structured_rows"], [])               # rows only with the potency question


if __name__ == "__main__":
    unittest.main(verbosity=2)
