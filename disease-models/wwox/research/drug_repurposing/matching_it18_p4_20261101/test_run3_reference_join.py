import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import matching_task as m
import run3_reference_join as r3


def write(p, text):
    Path(p).write_text(text, encoding="utf-8")


class Run3(unittest.TestCase):
    def _gdir(self, d):
        g = Path(d)
        write(g / "ligands.csv", '"# v"\n"Ligand ID","ChEMBL ID"\n"1","CHEMBL1"\n"2","CHEMBL2"\n')
        write(g / "interactions.csv", '"# v"\n"Target ID","Target Species","Ligand ID","Target UniProt ID","Type","Action","PubMed ID"\n'
              '"458","Rat","1","Q00961","Antagonist","Antagonist",""\n'
              '"999","Human","2","P9","Agonist","Agonist",""\n')
        write(g / "targets_and_families.csv", '"# v"\n"Target id","Human SwissProt"\n"458","Q14957"\n')
        return g

    def test_orthologue_row_maps_to_human_uniprot_and_is_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            g = self._gdir(d)
            tid = r3.target_id_to_human_uniprot(g)
            keep = {"dev", "eval"}
            gt, lp = r3.load_gtopdb_any_species(g, {}, keep, tid)
            self.assertIn(("CHEMBL1", "Q14957"), gt)
            self.assertNotIn(("CHEMBL1", "Q00961"), gt)  # rat accession never used as a key
            self.assertEqual(gt[("CHEMBL1", "Q14957")]["species"], {"Rat"})
            self.assertIn(("CHEMBL2", "P9"), gt)  # human row keeps its own accession
            self.assertEqual(r3.human_only(gt).keys(), {("CHEMBL2", "P9")})
            self.assertEqual(lp, {"CHEMBL1", "CHEMBL2"})

    def test_split_filter_drops_rows_on_read(self):
        with tempfile.TemporaryDirectory() as d:
            g = self._gdir(d)
            tid = r3.target_id_to_human_uniprot(g)
            s1 = m.dt.split_of("CHEMBL1")
            gt, lp = r3.load_gtopdb_any_species(g, {}, {"dev", "eval"} - {s1}, tid)
            self.assertNotIn(("CHEMBL1", "Q14957"), gt)
            self.assertNotIn("CHEMBL1", lp)

    def test_family_level_excludes_mostly_outside_records(self):
        big = frozenset("P%d" % i for i in range(10))
        fam = frozenset({"P1", "P2", "P3"})
        row = {"rowsets": {big, fam}, "module_uniprots": frozenset({"P1", "P2"})}
        self.assertEqual(r3.family_uniprots(row), set(fam))

    def test_absence_causes(self):
        row = {"parent": "C1"}
        self.assertEqual(r3.absence_cause(row, {}, set(), ["P1"]), "no_gtopdb_ligand_with_chembl_id")
        self.assertEqual(r3.absence_cause(row, {}, {"C1"}, ["P1"]), "ligand_present_no_interaction_on_these_genes")

    def test_help_and_no_args_write_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            before = set(Path(d).iterdir())
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(r3.main([]), 0)
                with self.assertRaises(SystemExit):
                    r3.main(["--help"])
            self.assertEqual(set(Path(d).iterdir()), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
