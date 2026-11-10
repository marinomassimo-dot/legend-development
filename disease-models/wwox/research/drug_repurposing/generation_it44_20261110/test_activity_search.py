#!/usr/bin/env python3
"""IT44 P2 regressions, offline: a fixture cache stands in for the ChEMBL pages. A measured activity is not an action; a truncated read is not absence; the catalogue join is by id."""
import csv, gzip, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent

def page(rows, nxt=None): return json.dumps({"activities": rows, "page_meta": {"next": nxt}}).encode()
def act(mid, name, typ, val, atype="F", doc="CHEMBL_DOC1"):
    return {"molecule_chembl_id": mid, "parent_molecule_chembl_id": mid, "molecule_pref_name": name, "standard_type": typ, "standard_relation": "=", "standard_value": val, "standard_units": "nM", "assay_type": atype,
            "assay_organism": "Homo sapiens", "data_validity_comment": None, "assay_description": "fixture", "document_chembl_id": doc, "pubmed_id": None}

class Offline(unittest.TestCase):
    def run_path(self, pages):
        tmp = Path(tempfile.mkdtemp()); (tmp / "cc/chembl").mkdir(parents=True); (tmp / "act/CHEMBLT1").mkdir(parents=True)
        with gzip.open(tmp / "cc/chembl/targets.jsonl.gz", "wt") as f:
            f.write(json.dumps({"organism": "Homo sapiens", "pref_name": "t", "target_chembl_id": "CHEMBLT1", "target_type": "SINGLE PROTEIN",
                                "target_components": [{"target_component_synonyms": [{"syn_type": "GENE_SYMBOL", "component_synonym": "FAKE1"}]}]}) + "\n")
        for i, p in enumerate(pages): (tmp / f"act/CHEMBLT1/p{i}.json").write_bytes(p)
        (tmp / "rel.tsv").write_text("relation_id\ttarget_symbols\nSX\tFAKE1\n")
        env = dict(os.environ, LEGEND_CATALOG_CACHE=str(tmp / "cc"), LEGEND_ACTIVITY_CACHE=str(tmp / "act"))
        r = subprocess.run([sys.executable, str(HERE / "activity_search.py"), "--relations", str(tmp / "rel.tsv"), "--out", str(tmp / "out"), "--max-pages", str(len(pages))], env=env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        with open(tmp / "out/activity_molecules.tsv") as f: return list(csv.DictReader(f, delimiter="\t"))
    def test_activity_is_never_an_action(self):
        m = self.run_path([page([act("CHEMBL_A", "alpha", "EC50", "40"), act("CHEMBL_B", "", "IC50", "9")])])
        self.assertTrue(all(x["verdict"] == "ACTIVITY_ONLY" and "direction" in x["unknown_fields"] for x in m)); self.assertEqual({x["parent_chembl_id"] for x in m}, {"CHEMBL_A", "CHEMBL_B"})
    def test_truncated_read_is_named(self):
        m = self.run_path([page([act("CHEMBL_A", "alpha", "EC50", "40")], nxt="/more")])
        self.assertIn("TRUNCATED", m[0]["coverage"])
    def test_complete_read_is_named(self):
        m = self.run_path([page([act("CHEMBL_A", "alpha", "EC50", "40")])]); self.assertEqual(m[0]["coverage"], "COMPLETE")
    def test_screening_deposit_is_flagged_and_a_small_document_is_not(self):
        big = [act(f"CHEMBL_S{i}", "", "IC50", "9", doc="BIGSCREEN") for i in range(250)] + [act("CHEMBL_KEEP", "keep", "EC50", "40", doc="SMALLDOC")]
        m = {x["parent_chembl_id"]: x for x in self.run_path([page(big)])}
        self.assertEqual(m["CHEMBL_S1"]["read_state"], "SCREEN_DEPOSIT"); self.assertEqual(m["CHEMBL_KEEP"]["read_state"], "OK")
    def test_symbol_without_target_is_unread_not_empty(self):
        tmp = Path(tempfile.mkdtemp()); (tmp / "cc/chembl").mkdir(parents=True)
        with gzip.open(tmp / "cc/chembl/targets.jsonl.gz", "wt") as f: f.write("")
        (tmp / "rel.tsv").write_text("relation_id\ttarget_symbols\nSX\tNOSUCHGENE\n")
        env = dict(os.environ, LEGEND_CATALOG_CACHE=str(tmp / "cc"), LEGEND_ACTIVITY_CACHE=str(tmp / "act"))
        subprocess.run([sys.executable, str(HERE / "activity_search.py"), "--relations", str(tmp / "rel.tsv"), "--out", str(tmp / "out")], env=env, capture_output=True, text=True)
        self.assertEqual(json.load(open(tmp / "out/activity_manifest.json"))["_symbols"], {"SX:NOSUCHGENE": "UNRESOLVED_IN_CACHED_INDEX"})
    def test_unnamed_molecule_without_catalogue_row_is_status_none(self):
        m = self.run_path([page([act("CHEMBL_ZZ_NOT_IN_CATALOGUE", "", "Ki", "5", atype="B")])]); self.assertEqual((m[0]["catalogue_status"], m[0]["n_functional"]), ("none", "0"))

if __name__ == "__main__": unittest.main(verbosity=2)
