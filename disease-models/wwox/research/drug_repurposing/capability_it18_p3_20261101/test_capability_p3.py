#!/usr/bin/env python3
"""Offline tests for the IT18 P3 scripts (synthetic fixtures; no network, no third-party package)."""
import csv
import gzip
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


def io_open(p):
    return Path(p).read_text().splitlines()
sys.path.insert(0, str(HERE))
import dc_direction as dcd  # noqa: E402

DC_HDR = ["DRUG_NAME", "STRUCT_ID", "TARGET_NAME", "TARGET_CLASS", "ACCESSION", "GENE", "SWISSPROT", "ACT_VALUE", "ACT_UNIT", "ACT_TYPE",
          "ACT_COMMENT", "ACT_SOURCE", "RELATION", "MOA", "MOA_SOURCE", "ACT_SOURCE_URL", "MOA_SOURCE_URL", "ACTION_TYPE", "TDL", "ORGANISM"]


def mech(action, uniprot, genes):
    return {"source": "ChEMBL curated mechanism", "organism": "Homo sapiens", "inherited_from_parent": None, "action_type": action,
            "uniprot": [uniprot], "gene_symbols": genes, "reference_ids": []}


class Fixture(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp(prefix="p3_"))
        recs = [
            {"ids": {"chembl": "CHEMBL1", "inchikey": "AAAA-BBBB-N"}, "relations": {}, "targets": [mech("ANTAGONIST", "P1", ["CACNA1G"])]},
            {"ids": {"chembl": "CHEMBL2", "inchikey": "CCCC-DDDD-N"}, "relations": {}, "targets": [mech("AGONIST", "P2", ["GENEX"])]},
            {"ids": {"chembl": "CHEMBL3", "inchikey": "EEEE-FFFF-N"}, "relations": {}, "targets": [mech("INHIBITOR", "P3", ["GENEY"])]},
        ]
        with gzip.open(self.d / "cat.jsonl.gz", "wt") as f:
            for r in recs:
                f.write(json.dumps(r) + "\n")
        g = self.d / "gt"
        g.mkdir()
        (g / "ligands.csv").write_text('"release"\n"Ligand ID","ChEMBL ID"\n"10","CHEMBL1"\n')
        (g / "interactions.csv").write_text('"release"\n"Ligand ID","Target Species","Target UniProt ID","Type","Action","PubMed ID"\n'
                                            '"10","Human","P1","Antagonist","Antagonist",""\n')
        rows = [  # struct 1 -> CHEMBL1 by UniChem; struct 2 by exact InChIKey only; struct 3 shares only the skeleton of CHEMBL3
            {"STRUCT_ID": "1", "ACCESSION": "P1", "GENE": "CACNA1G", "ACTION_TYPE": "BLOCKER", "ACT_SOURCE": "CHEMBL", "MOA_SOURCE": "DRUG LABEL"},
            {"STRUCT_ID": "2", "ACCESSION": "P2", "GENE": "GENEX", "ACTION_TYPE": "ANTAGONIST", "ACT_SOURCE": "SCIENTIFIC LITERATURE", "MOA_SOURCE": ""},
            {"STRUCT_ID": "3", "ACCESSION": "P3", "GENE": "GENEY", "ACTION_TYPE": "INHIBITOR", "ACT_SOURCE": "IUPHAR", "MOA_SOURCE": ""},
        ]
        with gzip.open(self.d / "dc.tsv.gz", "wt") as f:
            w = csv.DictWriter(f, fieldnames=DC_HDR, delimiter="\t")
            w.writeheader()
            for r in rows:
                w.writerow({**{k: "" for k in DC_HDR}, "ORGANISM": "Homo sapiens", **r})
        with gzip.open(self.d / "uc.txt.gz", "wt") as f:
            f.write("From src:'1'\tTo src:'34'\nCHEMBL1\t1\n")
        (self.d / "keys.tsv").write_text("struct_id\tinchikey\n1\tAAAA-BBBB-N\n2\tCCCC-DDDD-N\n3\tEEEE-ZZZZ-N\n")
        (self.d / "needs.json").write_text(json.dumps({"needs": [
            {"id": "N1", "targets": [{"symbol": "CACNA1G", "target_kind": "intervention_target"}], "intervention_direction": {"direction": "down"}},
            {"id": "N2", "targets": [{"symbol": "GENEX", "target_kind": "intervention_target"}], "intervention_direction": {"direction": "uncertain"}}]}))

    def tearDown(self):
        import shutil
        shutil.rmtree(self.d, ignore_errors=True)

    def run_compare(self, extra=()):
        argv = ["compare", "--catalog", str(self.d / "cat.jsonl.gz"), "--gtopdb-dir", str(self.d / "gt"), "--dc", str(self.d / "dc.tsv.gz"),
                "--unichem", str(self.d / "uc.txt.gz"), "--needs", str(self.d / "needs.json"), "--out-json", str(self.d / "r.json"),
                "--out-tsv", str(self.d / "c.tsv"), "--out-disc", str(self.d / "x.tsv"), *extra]
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            dcd.main(argv)
        return json.loads((self.d / "r.json").read_text())

    def test_registered_join_uses_unichem_only(self):
        r = self.run_compare()
        self.assertEqual(r["counts"]["dc_determinate_any"], 1)
        self.assertEqual(r["counts"]["dc_determinate_independent"], 1)
        self.assertEqual(r["agreement"]["module_vs_dc_independent"]["k"], 1)
        self.assertEqual(r["matching_universe_counts_only"]["directed_dc_independent_determinate"], 1)

    def test_inchikey_amendment_adds_exact_keys_never_skeletons(self):
        r = self.run_compare(["--inchikeys", str(self.d / "keys.tsv")])
        self.assertEqual(r["drugcentral_load"]["structs_added_by_inchikey"], 1)  # struct 2 only; struct 3 shares a skeleton, not the key
        self.assertEqual(r["drugcentral_load"]["inchikey_agrees_with_unichem"], 1)
        self.assertEqual(r["counts"]["dc_determinate_any"], 2)
        # CHEMBL2: module AGONIST vs DrugCentral ANTAGONIST from literature -> listed as an independent discordance, no GtoPdb pair
        disc = list(csv.DictReader(io_open(self.d / "x.tsv"), delimiter="\t"))
        self.assertEqual([(x["parent_chembl_id"], x["gtopdb_class"], x["dc_independent_labels"]) for x in disc],
                         [("CHEMBL2", "", "ANTAGONIST@SCIENTIFIC LITERATURE")])
        self.assertEqual(r["counts"]["mi_new_n"], 1)

    def test_origin_rule_and_vocabulary(self):
        self.assertEqual(dcd.origin_of({"MOA_SOURCE": "", "ACT_SOURCE": "IUPHAR"}), "IUPHAR")
        self.assertEqual(dcd.origin_of({"MOA_SOURCE": "KEGG DRUG", "ACT_SOURCE": "CHEMBL"}), "KEGG DRUG")
        self.assertEqual([dcd.origin_class(o) for o in ("CHEMBL", "DRUG LABEL", "WOMBAT-PK")], ["SHARED", "INDEPENDENT", "OTHER"])
        self.assertEqual(dcd.dc_class("gating inhibitor"), "DECREASE")
        self.assertIsNone(dcd.dc_class("PARTIAL AGONIST"))
        self.assertIsNone(dcd.dc_class("MODULATOR"))
        self.assertEqual(dcd.resolve([{"class": "DECREASE", "oclass": "SHARED"}, {"class": "INCREASE", "oclass": "SHARED"}]), (None, "conflict"))
        self.assertEqual(dcd.resolve([{"class": "DECREASE", "oclass": "SHARED"}], {"INDEPENDENT"}), (None, "absent"))


class HelpIsInert(unittest.TestCase):
    def test_help_writes_nothing_and_imports_no_third_party(self):
        for script in ("dc_direction.py", "tu_trial.py", "dc_inchikeys.py"):
            with self.subTest(script=script), tempfile.TemporaryDirectory() as t:
                code = ("import runpy,sys; sys.argv=['x','--help']\n"
                        f"try: runpy.run_path({str(HERE / script)!r}, run_name='__main__')\n"
                        "except SystemExit: pass\n"
                        "assert 'tooluniverse' not in sys.modules and 'rdkit' not in sys.modules\n")
                done = subprocess.run([sys.executable, "-B", "-c", code], cwd=t, capture_output=True, text=True)
                self.assertEqual(done.returncode, 0, done.stderr)
                self.assertIn("usage", done.stdout)
                self.assertEqual(list(Path(t).iterdir()), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
