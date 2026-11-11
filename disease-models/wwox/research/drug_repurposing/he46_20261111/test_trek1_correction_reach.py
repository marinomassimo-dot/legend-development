#!/usr/bin/env python3
"""HE46 H2: the TREK-1 residual-current correction (Imin 0.25, Bagriantsev 2011 Table S1) is still where its consumers read it.

The chain is source -> parameter -> size check -> hypothesis -> consumer delta -> INV-18 -> view; the three tests cover the links that carry a number or a pointer and
that a regeneration of the investigations table could silently drop."""
import csv, re, unittest
from pathlib import Path

DR = Path(__file__).resolve().parents[1]
csv.field_size_limit(10**9)


def closure(ph, p50, n, imin):
    return imin + (1 - imin) / (1 + 10 ** (n * (p50 - ph)))


class CorrectionReach(unittest.TestCase):
    def test_size_check_table_is_the_formula_with_the_reported_parameters(self):
        rows = [r for r in csv.DictReader(open(DR / "ph_k2p_sci45_20261111/size_check_imin.tsv"), delimiter="\t") if float(r["Imin"]) == 0.25]
        self.assertEqual(len(rows), 24)
        for r in rows:
            f = 1 - closure(float(r["pH0"]) - float(r["delta_pH"]), 7.51, float(r["hill_n"]), 0.25) / closure(float(r["pH0"]), 7.51, float(r["hill_n"]), 0.25)
            self.assertAlmostEqual(f, float(r["closure_f"]), places=3)
            self.assertEqual(r["reaches_0.28"], "no")     # no sourced parameter set carries the whole pair

    def test_inv18_carries_the_residual_current(self):
        inv = {r["inv_id"]: r for r in csv.DictReader(open(DR / "ranking_it8_p9_20261029/investigations.tsv"), delimiter="\t")}["INV-18"]
        self.assertRegex(inv["next_test"], r"partial contributor only \(TREK-1 Imin 0\.25\)")

    def test_older_documents_point_to_the_correction(self):
        for f in ("pdh_pdk_sci44_20261110/S7_coda.md", "kchan_expression_sci44_20261111/README.md"):
            text = (DR / f).read_text(encoding="utf-8")
            self.assertRegex(text, r"Update 2026-11-11 \(HE46, from SCI45 `ph_k2p_sci45_20261111`")
            self.assertIn("ph_k2p_sci45_20261111/README.md", text.split("Update 2026-11-11 (HE46")[-1])
        self.assertIn("Update 2026-11-11 (HE46, clarification", (DR / "ph_k2p_sci45_20261111/README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
