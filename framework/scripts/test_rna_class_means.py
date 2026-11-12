#!/usr/bin/env python3
"""Regressions for framework/scripts/rna_class_means.py: missing is not zero, a duplicated symbol is reported, an empty cell is left out and counted,
and (when the public inputs are given) the committed SCI44, SCI46 and IT46 outputs are reproduced byte for byte."""
import gzip
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rna_class_means as rc  # noqa: E402

DR = Path(__file__).resolve().parents[2] / "disease-models/wwox/research/drug_repurposing"


class Tiny(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp(prefix="rna_test_"))
        self.addCleanup(lambda: __import__("shutil").rmtree(self.d, ignore_errors=True))

    def human(self, text):
        p = self.d / "h.csv.gz"
        with gzip.open(p, "wt", encoding="latin1") as f:
            f.write(text)
        return str(p)

    def test_a_requested_gene_that_the_table_lacks_is_missing_and_never_a_zero(self):
        out, rep = rc.extract_human(self.human("symbol,Ctx neuron,Mouse ctx neuron\nGFAP,1.5,2.5\n"), ["Gfap", "Hcar2"])
        self.assertEqual([(r[0], r[2], r[3]) for r in out], [("GFAP", 2, "2.00")])
        self.assertIn(("human", "Hcar2", "NOT_FOUND"), [(a, b, c) for a, b, c, *_ in rep])
        self.assertFalse([r for r in out if r[0] == "HCAR2"])

    def test_a_symbol_carried_by_two_rows_is_reported_and_both_rows_are_kept(self):
        out, rep = rc.extract_human(self.human("symbol,Ctx neuron\nGFAP,1\nGFAP,3\n"), ["Gfap"])
        self.assertEqual([r[3] for r in out], ["1.00", "3.00"])
        self.assertEqual([r[2] for r in rep], ["DUPLICATE_ROWS"])

    def test_an_empty_cell_is_left_out_of_the_mean_and_counted(self):
        out, rep = rc.extract_human(self.human("symbol,A neuron,B neuron,C neuron\nGFAP,2,,4\n"), ["Gfap"])
        self.assertEqual((out[0][2], out[0][3]), (2, "3.00"))
        self.assertIn("1 empty or non-numeric", rep[0][3])

    def test_a_column_group_with_only_empty_cells_writes_no_line(self):
        out, _ = rc.extract_human(self.human("symbol,Ctx neuron,Ctx oligo\nGFAP,5,\n"), ["Gfap"])
        self.assertEqual([r[1] for r in out], ["neuron_ctx"])

    def test_the_extra_human_symbol_is_read_without_being_a_request(self):
        out, rep = rc.extract_human(self.human("symbol,Ctx neuron\nG6PD,7\n"), ["G6pdx"], ["G6PD"])
        self.assertEqual([r[0] for r in out], ["G6PD"])
        self.assertEqual([r[2] for r in rep], ["NOT_FOUND"])     # the requested symbol is still reported as not found under that name

    def test_mouse_values_are_kept_per_sample_and_a_duplicate_symbol_inside_a_file_is_reported(self):
        for n in ("GSM1_Neuron1.xls.gz", "GSM2_Neuron2.xls.gz", "GSM3_WC.xls.gz"):
            (self.d / n).write_bytes(n.encode())
        sheets = {"GSM1_Neuron1.xls.gz": [["Gfap", 1.0], ["Gfap", 2.0], ["Rbfox3", 9.0]], "GSM2_Neuron2.xls.gz": [["Gfap", 3.0]]}
        rows, rep, files = rc.extract_mouse(str(self.d), ["Gfap", "Rbfox3", "Hcar2"], reader=lambda path: sheets[os.path.basename(path)])
        self.assertEqual([x[0] for x in rows[("Gfap", "neurons (P7)")]], [1.0, 2.0, 3.0])
        self.assertEqual(len(files), 2)                                       # the WC file is not read
        states = {(g, s) for _, g, s, *_ in rep}
        self.assertTrue({("Gfap", "DUPLICATE_ROWS"), ("Hcar2", "NOT_FOUND"), ("Rbfox3", "FOUND")} <= states)


@unittest.skipUnless(os.environ.get("RNA_REPRO_RAW") and os.environ.get("RNA_REPRO_CSV"), "public inputs not given (RNA_REPRO_RAW, RNA_REPRO_CSV)")
class Reproduction(unittest.TestCase):
    CASES = (("kchan_expression_sci44_20261111", "kchan_expression", "Kcnj11,Abcc8,Kcnj8,Abcc9,Kcnj10,Kcnj2,Kcnj3,Kcnj6,Kcnk1,Kcnk2,Kcnk3,Kcnk9,Kcnq2,Kcnq3,Hcn1,Hcn2,Kcnc1,Kcna1,Rbfox3,Gfap,Cldn5", ""),
             ("nrf2_expression_sci46_20261111", "nrf2_expression", "Keap1,Nfe2l2,Nqo1,Hmox1,Gclm,Gclc,Txnrd1,Srxn1,G6pdx,Gsr,Gpx4,Slc7a11,Fth1,Hcar2,Niacr1,Bach1,Gsk3b,Btrc,Wwox,Rbfox3,Gfap,Cx3cr1,Mog", "G6PD"))

    def test_the_committed_outputs_are_reproduced_byte_for_byte(self):
        for folder, prefix, genes, extra in self.CASES:
            out = tempfile.mkdtemp(prefix="rna_repro_")
            self.addCleanup(lambda o=out: __import__("shutil").rmtree(o, ignore_errors=True))
            rc.main(["--genes", genes, "--prefix", prefix, "--human-extra", extra, "--mouse-raw", os.environ["RNA_REPRO_RAW"], "--human-csv", os.environ["RNA_REPRO_CSV"], "--out", out]
                    + (["--xlrd-dir", os.environ["RNA_REPRO_XLRD"]] if os.environ.get("RNA_REPRO_XLRD") else []))
            for organism in ("mouse", "human"):
                self.assertEqual((Path(out) / f"{prefix}_{organism}.tsv").read_bytes(), (DR / folder / f"{prefix}_{organism}.tsv").read_bytes(), (prefix, organism))


if __name__ == "__main__":
    unittest.main(verbosity=2)
