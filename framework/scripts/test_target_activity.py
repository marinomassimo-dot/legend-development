#!/usr/bin/env python3
"""Tests for target_activity.py with synthetic adapter answers in the shape of framework/adapters/chembl.py. Case names are the pre-registered ones (HE44 H1)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import target_activity as ta  # noqa: E402

GTOPDB = [{"HGNC symbol": "KCNQ2", "Human SwissProt": "O43526"}, {"HGNC symbol": "DUP", "Human SwissProt": "P1"}, {"HGNC symbol": "DUP", "Human SwissProt": "P2"}]


def act(mol, value, unit="nM", rel="=", typ="EC50", target="CHEMBL2476", ttype="SINGLE PROTEIN", parent=None, name=None):
    return {"kind": "activity", "molecule_chembl_id": mol, "parent_molecule_chembl_id": parent or mol, "molecule_pref_name": name, "standard_type": typ, "standard_relation": rel,
            "standard_value": value, "standard_units": unit, "pchembl_value": None, "target_chembl_id": target, "target_organism": "Homo sapiens", "target_pref_name": "KCNQ2",
            "assay_chembl_id": "CHEMBL_A1", "assay_description": "patch clamp", "assay_context": {"organism": "Homo sapiens"}, "document_chembl_id": "CHEMBL_D1", "document_year": 2020,
            "data_validity_comment": None, "potential_duplicate": 0, "target_type": ttype, "target_gene_symbols": ["KCNQ2"]}


def fake(targets, answers):
    """targets: hits for the accession lookup; answers: {target id: adapter answer}."""
    def q(req):
        if "uniprot" in req:
            return {"status": "MATCH_FOUND" if targets else "NO_MATCH_FOUND", "hits": targets, "source_version": "ChEMBL_TEST"}
        return answers[req["target"]]
    return q


TG = [{"kind": "target", "target_chembl_id": "CHEMBL2476", "pref_name": "KCNQ2", "organism": "Homo sapiens", "target_type": "SINGLE PROTEIN", "accessions": ["O43526"]}]


def full(hits, cov="COMPLETE", total=None):
    return {"status": "MATCH_FOUND" if hits else "NO_MATCH_FOUND", "coverage": cov, "retrieved": len(hits), "total_count": total if total is not None else len(hits), "hits": hits}


class Reach(unittest.TestCase):
    def test_a_molecule_with_an_activity_and_no_mechanism_row_is_reached_and_keeps_its_quantity(self):
        r = ta.activities_for_gene("KCNQ2", fake(TG, {"CHEMBL2476": full([act("CHEMBL5095264", 98.0, name="AZETUKALNER"), act("CHEMBL41355", 150.0, rel="<", name="EZOGABINE")])}), GTOPDB,
                                   reached={"CHEMBL41355"}, catalogue_ids={"CAT:CHEMBL5095264"})
        by = {m["molecule_chembl_id"]: m for m in r["molecules"]}
        self.assertEqual(r["state"], "OK")
        self.assertFalse(by["CHEMBL5095264"]["reached_by_target_path"])
        self.assertTrue(by["CHEMBL41355"]["reached_by_target_path"])
        self.assertTrue(by["CHEMBL5095264"]["in_catalogue"])
        self.assertFalse(by["CHEMBL41355"]["in_catalogue"])
        row = by["CHEMBL5095264"]["rows"][0]
        q = row["measurement"]
        self.assertEqual((q["kind"], q["original"]["value"], q["original"]["unit"], q["converted_nM"], q["source"], q["species"]), ("EC50", 98.0, "nM", 98.0, "CHEMBL_D1", "Homo sapiens"))
        self.assertEqual((row["direction"], row["selectivity"]), ("", "NOT_ASSESSED"))      # an activity assigns neither direction nor selectivity
        self.assertIn("CENSORED", by["CHEMBL41355"]["rows"][0]["measurement"]["flags"])      # a bound is kept as a bound

    def test_a_complex_target_is_marked_and_a_missing_unit_is_a_flag(self):
        tg = TG + [{"kind": "target", "target_chembl_id": "CHEMBL9", "pref_name": "KCNQ2/KCNQ3", "organism": "Homo sapiens", "target_type": "PROTEIN COMPLEX", "accessions": ["O43526", "O43525"]}]
        r = ta.activities_for_gene("KCNQ2", fake(tg, {"CHEMBL2476": full([]), "CHEMBL9": full([act("CHEMBL1", 5.0, unit=None, target="CHEMBL9", ttype="PROTEIN COMPLEX")])}), GTOPDB)
        row = r["molecules"][0]["rows"][0]
        self.assertTrue(row["target_is_complex"])
        self.assertIn("UNIT_MISSING", row["measurement"]["flags"])
        self.assertIsNone(row["measurement"]["converted_nM"])


class CatalogueReach(unittest.TestCase):
    def test_a_salt_record_with_a_target_row_reaches_its_parent(self):
        es = [{"id": "CAT:CHEMBL1695", "ids": {"chembl": "CHEMBL1695"}, "relations": {"parent": "CAT:CHEMBL1027"}, "targets": [{"gene_symbols": ["SLC6A1"]}]},
              {"id": "CAT:CHEMBL5", "ids": {"chembl": "CHEMBL5"}, "targets": [{"gene": "OTHER"}]}]
        self.assertEqual(ta.catalogue_reach(es, "slc6a1"), {"CHEMBL1695", "CHEMBL1027"})


class FailureBehaviour(unittest.TestCase):
    def test_a_symbol_without_one_accession_is_unresolved_not_empty(self):
        for sym in ("NOPE", "DUP"):
            r = ta.activities_for_gene(sym, fake(TG, {}), GTOPDB)
            self.assertTrue(r["state"].startswith("UNRESOLVED_SYMBOL"), sym)
            self.assertEqual(r["molecules"], [])

    def test_an_adapter_failure_is_a_read_error_never_no_compounds(self):
        r = ta.activities_for_gene("KCNQ2", lambda req: {"status": "QUERY_ERROR", "error": "HTTP 500", "hits": []}, GTOPDB)
        self.assertEqual(r["state"], "READ_ERROR")
        r = ta.activities_for_gene("KCNQ2", fake(TG, {"CHEMBL2476": {"status": "QUERY_ERROR", "error": "HTTP 500", "hits": []}}), GTOPDB)
        self.assertEqual(r["state"], "READ_ERROR")

    def test_a_truncated_read_lists_what_it_read_and_says_it_is_not_all(self):
        r = ta.activities_for_gene("KCNQ2", fake(TG, {"CHEMBL2476": full([act("CHEMBL1", 1.0)], cov="TRUNCATED", total=900)}), GTOPDB)
        self.assertEqual(r["state"], "READ_INCOMPLETE")
        self.assertEqual(len(r["molecules"]), 1)
        self.assertEqual((r["reads"][0]["retrieved"], r["reads"][0]["total_count"]), (1, 900))

    def test_no_rows_is_stated_for_the_scope_only_when_the_read_was_complete(self):
        r = ta.activities_for_gene("KCNQ2", fake(TG, {"CHEMBL2476": full([])}), GTOPDB)
        self.assertEqual(r["state"], "NO_ACTIVITY_ROWS")
        self.assertIn("not about any compound", r["note"])
        r2 = ta.activities_for_gene("KCNQ2", fake([], {}), GTOPDB)       # no human target carries the accession
        self.assertEqual(r2["state"], "NO_ACTIVITY_ROWS")
        self.assertIn("no Homo sapiens ChEMBL target", r2["note"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
