#!/usr/bin/env python3
"""Tests for held_results_index.py: the WNT5A entry points to the Wnt sign note's RESULT section, the index is rebuildable and marked derived, and no source is edited."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import held_results_index as hri  # noqa: E402

WNT = "disease-models/wwox/research/drug_repurposing/gse156243/prediction_wnt_sign_20261025.md"


class HeldResultsIndex(unittest.TestCase):
    def test_wnt5a_points_to_the_result_section_of_the_wnt_sign_note(self) -> None:
        rows = [r for r in hri.build() if r["symbol"] == "WNT5A" and r["file"] == WNT]
        self.assertTrue(rows)
        first = rows[0]
        self.assertEqual(first["accession"], "GSE156243")
        self.assertTrue(first["section"].startswith("RESULT"))
        self.assertEqual(first["words"], "up")                      # "7 of 7 up"
        text = (hri.ROOT / WNT).read_text(encoding="utf-8").splitlines()
        self.assertIn("WNT5A", text[int(first["line"]) - 1])        # the line column is where the symbol is

    def test_the_stored_copy_is_marked_derived_and_equals_a_rebuild(self) -> None:
        stored = (hri.ROOT / hri.OUT).read_text(encoding="utf-8")
        self.assertIn("DERIVED INDEX, not a source of record", stored.splitlines()[0])
        self.assertEqual(stored, hri.render(hri.build()))

    def test_only_result_sections_and_declared_symbols_are_indexed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / hri.FOLDERS[0]
            folder.mkdir(parents=True)
            (folder / "prediction_x.md").write_text("# GSE000001 test\n\n## Gene sets, fixed now\n- A: GENEA, GENEB.\n\n## Prediction\nGENEA is expected up.\n\n# RESULT (appended)\n\nGENEA is down; GENEC is down and so is KO.\n\n# LATER\nGENEB is up.\n", encoding="utf-8")
            rows = hri.build(Path(tmp))
            self.assertEqual([(r["symbol"], r["words"]) for r in rows], [("GENEA", "down")])      # GENEC undeclared, GENEB only outside RESULT, the prediction section skipped

    def test_the_command_line_runs_without_writing_and_lookup_reports_a_miss(self) -> None:
        run = lambda *a: subprocess.run([sys.executable, str(HERE / "held_results_index.py"), *a], capture_output=True, text=True, cwd=hri.ROOT)  # noqa: E731
        self.assertEqual(run("check").returncode, 0)
        hit = run("lookup", "wnt5a")
        self.assertEqual(hit.returncode, 0); self.assertIn("prediction_wnt_sign_20261025.md", hit.stdout)
        miss = run("lookup", "NOSUCHGENE")
        self.assertEqual(miss.returncode, 1); self.assertIn("not about the repository", miss.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
