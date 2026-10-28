#!/usr/bin/env python3
"""Offline regressions for catalog_build.py.  No network: a tiny synthetic cache is written to a
temp directory and the module's paths are pointed at it.  Run: python3 -B test_catalog_build.py"""
from __future__ import annotations

import csv
import gzip
import importlib.util
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("catalog_build", HERE / "catalog_build.py")
cb = importlib.util.module_from_spec(spec)
sys.modules["catalog_build"] = cb
spec.loader.exec_module(cb)


def mol(cid, name, phase, parent=None, ik="AAAAAAAAAAAAAA-BBBBBBBBBB-N", probe=0):
    return {"molecule_chembl_id": cid, "pref_name": name, "max_phase": phase, "first_approval": None, "molecule_type": "Small molecule",
            "molecule_hierarchy": {"molecule_chembl_id": cid, "parent_chembl_id": parent or cid},
            "molecule_structures": {"standard_inchi_key": ik}, "molecule_synonyms": [{"molecule_synonym": name or "x"}],
            "chemical_probe": probe, "chirality": 2, "_selection": "selected"}


def gz(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")


def unichem(path, pairs):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as fh:
        fh.write("From src:'1'\tTo src:'x'\n")
        for a, b in pairs:
            fh.write(f"{a}\t{b}\n")


def ndc_product(unii, name, pt, mc, n_ing=1):
    return {"product_ndc": f"0-{unii}", "product_type": pt, "marketing_category": mc, "finished": True,
            "active_ingredients": [{"name": name}] * n_ing, "openfda": {"unii": [unii]}}


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.cache = self.root / "cache"
        cb.CACHE = self.cache
        cb.MANIFEST = self.root / "manifest.json"
        self.addCleanup(self.tmp.cleanup)
        self.manifest = {"schema_version": 1, "sources": {}}

    def src(self, name, version, status="OK", files=()):
        e = {"name": name, "licence": "L", "terms": "T", "last_attempt": {"utc": "2026-10-27T00:00:00Z", "status": status, "detail": ""}}
        if status == "OK":
            e["data"] = {"status": "OK", "retrieved_utc": "2026-10-27T00:00:00Z", "version": version, "files": list(files),
                         "chembl_status": {"disinct_compounds": 1000}}
        self.manifest["sources"][name] = e

    def write_manifest(self):
        cb.MANIFEST.write_text(json.dumps(self.manifest))

    def chembl(self, mols, mechs=(), targets=()):
        gz(self.cache / "chembl/molecules.jsonl.gz", mols)
        gz(self.cache / "chembl/mechanisms.jsonl.gz", list(mechs))
        gz(self.cache / "chembl/targets.jsonl.gz", list(targets))
        self.src("chembl", "ChEMBL_T 2026-01-01")

    def dgidb(self, drugs, inters=()):
        d = self.cache / "dgidb"
        d.mkdir(parents=True, exist_ok=True)
        cols = ["drug_claim_name", "nomenclature", "concept_id", "drug_name", "approved", "immunotherapy", "anti_neoplastic", "source_db_name", "source_db_version"]
        with open(d / "drugs.tsv", "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(cols)
            w.writerows(drugs)
        icols = ["gene_claim_name", "gene_concept_id", "gene_name", "interaction_source_db_name", "interaction_source_db_version", "interaction_type",
                 "interaction_score", "drug_claim_name", "drug_concept_id", "drug_name", "approved", "immunotherapy", "anti_neoplastic"]
        with open(d / "interactions.tsv", "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(icols)
            w.writerows(inters)
        self.src("dgidb", "T")

    def build(self):
        return cb.build_catalog()


class IdentityAndDedup(Base):
    def test_salts_and_stereoisomers_are_not_merged(self):
        same = "SKELETONSKELET-AAAAAAAAAA-N"
        self.chembl([mol("CHEMBL1", "Drugine", 4.0, ik="SKELETONSKELET-AAAAAAAAAA-N"),
                     mol("CHEMBL2", "Drugine hydrochloride", 4.0, parent="CHEMBL1", ik="SKELETONSKELET-CCCCCCCCCC-N"),
                     mol("CHEMBL3", "Drugine, (R)-", 2.0, ik="SKELETONSKELET-DDDDDDDDDD-N")])
        self.write_manifest()
        entries, stats = self.build()
        ids = {e["id"] for e in entries}
        self.assertEqual(ids, {"CAT:CHEMBL1", "CAT:CHEMBL2", "CAT:CHEMBL3"})
        by = {e["id"]: e for e in entries}
        self.assertEqual(by["CAT:CHEMBL2"]["relations"]["parent"], "CAT:CHEMBL1")
        self.assertEqual(by["CAT:CHEMBL1"]["relations"]["children"], ["CAT:CHEMBL2"])
        self.assertEqual(stats["merge_report"]["entries_merged_away"], 0)
        self.assertEqual(stats["relations_kept"]["entries_in_shared_skeleton_groups"], 3)

    def test_name_alone_never_links_a_source_only_row(self):
        self.chembl([mol("CHEMBL1", "Aspirin", 4.0)])
        self.dgidb([["ASPIRIN", "Primary Name", "rxcui:1191", "ASPIRIN", "TRUE", "FALSE", "FALSE", "RxNorm", "1"]])
        self.write_manifest()
        entries, stats = self.build()
        self.assertEqual(stats["by_origin"].get("dgidb_only"), 1)
        self.assertEqual(len(entries), 2)  # same name, no identifier: stays separate, declared as a possible duplicate
        self.assertIn("possible_cross_source_duplicates", stats["merge_report"])

    def test_dgidb_chembl_concept_links_by_identifier(self):
        self.chembl([mol("CHEMBL1", "Aspirin", 4.0)])
        self.dgidb([["ASPIRIN", "Primary Name", "chembl:CHEMBL1", "ASPIRIN", "TRUE", "FALSE", "FALSE", "ChEMBL", "33"]],
                   [["PTGS1", "hgnc:9604", "PTGS1", "DrugBank", "1", "inhibitor", "0.5", "ASPIRIN", "chembl:CHEMBL1", "ASPIRIN", "TRUE", "FALSE", "FALSE"]])
        self.write_manifest()
        entries, stats = self.build()
        self.assertEqual(len(entries), 1)
        t = [x for x in entries[0]["targets"] if x["source"] == "DGIdb interaction"]
        self.assertEqual(t[0]["gene"], "PTGS1")
        self.assertNotIn("score", json.dumps(t))  # no potency/score is copied


class UnknownIsNotNegative(Base):
    def test_no_evidence_is_unknown_not_none(self):
        self.chembl([mol("CHEMBL9", None, None)])
        self.write_manifest()
        entries, _ = self.build()
        e = entries[0]
        self.assertEqual(e["access_categories"], ["unknown/unverified"])
        self.assertEqual(e["status_class"], "no_status_statement")
        self.assertEqual(e["appropriateness"], "NOT_ASSESSED")

    def test_dgidb_null_flags_and_interaction_type_stay_unknown(self):
        self.chembl([mol("CHEMBL1", "X", 1.0)])
        self.dgidb([["X", "Primary Name", "chembl:CHEMBL1", "X", "NULL", "NULL", "NULL", "ChEMBL", "33"]],
                   [["G1", "hgnc:1", "G1", "S", "1", "NULL", "0.1", "X", "chembl:CHEMBL1", "X", "NULL", "NULL", "NULL"]])
        self.write_manifest()
        e = self.build()[0][0]
        rec = [s for s in e["status_records"] if s["source"] == "DGIdb"][0]
        self.assertEqual(rec["approved_aggregate"], "UNKNOWN")
        t = [x for x in e["targets"] if x["source"] == "DGIdb interaction"][0]
        self.assertEqual(t["interaction_type_state"], "UNKNOWN")
        self.assertIsNone(t["interaction_type"])
        self.assertEqual(e["status_class"], "clinical_candidate")
        self.assertEqual(e["access_categories"], ["experimental"])

    def test_approved_without_ndc_is_unknown_access_not_inaccessible(self):
        self.chembl([mol("CHEMBL1", "Oldmycin", 4.0)])
        self.write_manifest()
        e = self.build()[0][0]
        self.assertEqual(e["access_categories"], ["unknown/unverified"])
        self.assertIn("not a negative", e["access"][0]["scope"])


class NdcAccess(Base):
    def test_unii_link_otc_rx_and_homeopathic_exclusion(self):
        self.chembl([mol("CHEMBL1", "Zolpidem", 4.0), mol("CHEMBL2", "Belladonna", 4.0)])
        unichem(self.cache / "unichem/src1src14.txt.gz", [("CHEMBL1", "UNIIRX0001"), ("CHEMBL2", "UNIIHOM002")])
        unichem(self.cache / "unichem/src1src2.txt.gz", [])
        unichem(self.cache / "unichem/src1src7.txt.gz", [])
        self.src("unichem", "T")
        res = [ndc_product("UNIIRX0001", "ZOLPIDEM", "HUMAN PRESCRIPTION DRUG", "ANDA"),
               ndc_product("UNIIRX0001", "ZOLPIDEM", "HUMAN OTC DRUG", "OTC MONOGRAPH FINAL"),
               ndc_product("UNIIHOM002", "BELLADONNA", "HUMAN OTC DRUG", "UNAPPROVED HOMEOPATHIC"),
               ndc_product("UNIIHOM003", "ARNICA", "HUMAN OTC DRUG", "UNAPPROVED HOMEOPATHIC"),
               ndc_product("UNIIONLY04", "NEWSTUFF", "HUMAN PRESCRIPTION DRUG", "UNAPPROVED DRUG OTHER")]
        zp = self.cache / "openfda/n.zip"
        zp.parent.mkdir(parents=True)
        with zipfile.ZipFile(zp, "w") as z:
            z.writestr("n.json", json.dumps({"results": res}))
        self.src("openfda_ndc", "export_date T", files=[{"path": "openfda/n.zip"}])
        self.write_manifest()
        entries, stats = self.build()
        by = {e["id"]: e for e in entries}
        self.assertEqual(by["CAT:CHEMBL1"]["access_categories"], ["OTC", "prescription"])
        # homeopathic listing alone is not OTC access for the molecule
        self.assertNotIn("OTC", by["CAT:CHEMBL2"]["access_categories"])
        self.assertIn("CAT:UNII:UNIIONLY04", by)  # unmatched, non-homeopathic: becomes an entry
        self.assertNotIn("CAT:UNII:UNIIHOM003", by)  # homeopathic-only unmatched: counted, not an entry
        self.assertEqual(stats["openfda_ndc"]["homeopathic_only_uniis_not_made_entries"], 1)
        self.assertEqual(by["CAT:UNII:UNIIONLY04"]["status_class"], "marketed_unapproved_us")


class FetchStates(Base):
    def test_truncated_download_is_incomplete_not_empty_and_keeps_old_data(self):
        m = {"schema_version": 1, "sources": {}}
        old = {"status": "OK", "retrieved_utc": "2026-01-01T00:00:00Z", "version": "old", "files": [], "problems": []}
        cb.record(m, "dgidb", "OK", "complete", old)
        orig = cb.http
        cb.http = lambda url, **kw: (200, b"short", {"Content-Length": "9999"})
        try:
            cb.fetch_file(m, "dgidb", [("http://x/drugs.tsv", "dgidb/drugs.tsv")], lambda v: "v", True)
        finally:
            cb.http = orig
        e = m["sources"]["dgidb"]
        self.assertEqual(e["last_attempt"]["status"], "INCOMPLETE")
        self.assertIn("truncated", e["last_attempt"]["detail"])
        self.assertEqual(e["data"]["version"], "old")  # last complete retrieval is not overwritten
        self.assertFalse((cb.CACHE / "dgidb/drugs.tsv").exists())

    def test_failed_http_is_failed(self):
        m = {"schema_version": 1, "sources": {}}
        orig = cb.http
        cb.http = lambda url, **kw: (503, b"", {})
        try:
            cb.fetch_file(m, "dgidb", [("http://x/drugs.tsv", "dgidb/drugs.tsv")], lambda v: "v", True)
        finally:
            cb.http = orig
        self.assertEqual(m["sources"]["dgidb"]["last_attempt"]["status"], "INCOMPLETE")
        self.assertNotIn("data", m["sources"]["dgidb"])

    def test_build_refuses_without_complete_chembl_and_shows_unavailable_not_zero(self):
        self.src("chembl", "x", status="INCOMPLETE")
        self.manifest["sources"]["chembl"]["last_attempt"]["detail"] = "expected 100, received 50"
        self.write_manifest()
        with self.assertRaises(SystemExit):
            self.build()

    def test_missing_optional_source_is_not_fetched_state_not_zero(self):
        self.chembl([mol("CHEMBL1", "A", 4.0)])
        self.write_manifest()
        _, stats = self.build()
        self.assertEqual(stats["sources"]["dgidb"]["state"], "NOT_FETCHED")
        self.assertEqual(stats["dgidb"], {})  # absent, not zero-filled

    def test_freshness(self):
        m = {"schema_version": 1, "sources": {}}
        self.assertFalse(cb.fresh(m, "dgidb"))
        cb.record(m, "dgidb", "OK", "c", {"status": "OK", "retrieved_utc": cb.now(), "files": [], "version": "v"})
        self.assertTrue(cb.fresh(m, "dgidb"))
        m["sources"]["dgidb"]["data"]["retrieved_utc"] = "2020-01-01T00:00:00Z"
        self.assertFalse(cb.fresh(m, "dgidb"))


class Reconcile(Base):
    def test_sum_of_parts_equals_total_and_targets_carry_no_potency(self):
        self.chembl([mol("CHEMBL1", "A", 4.0), mol("CHEMBL2", "B", 2.0), mol("CHEMBL3", "C", -1.0), mol("CHEMBL4", "D", 0.0, probe=1)],
                    mechs=[{"mec_id": 1, "molecule_chembl_id": "CHEMBL1", "target_chembl_id": "CHEMBLT1", "action_type": "INHIBITOR",
                            "mechanism_of_action": "x inhibitor", "mechanism_refs": [{"ref_type": "PubMed", "ref_id": "123"}]}],
                    targets=[{"target_chembl_id": "CHEMBLT1", "pref_name": "Tgt", "target_type": "SINGLE PROTEIN", "organism": "Homo sapiens",
                              "target_components": [{"accession": "P1", "target_component_synonyms": [{"syn_type": "GENE_SYMBOL", "component_synonym": "TGT1"}]}]}])
        self.write_manifest()
        entries, stats = self.build()
        self.assertEqual(cb.reconcile(entries, stats), [])
        self.assertEqual(stats["by_status_class"], {"approved_any_source": 1, "clinical_candidate": 1, "phase_unknown": 1, "tool_probe": 1})
        t = entries[0]["targets"][0]
        self.assertEqual((t["action_type"], t["gene_symbols"], t["reference_ids"]), ("INHIBITOR", ["TGT1"], ["PubMed:123"]))
        self.assertIn("NOT_CARRIED", t["potency"])

    def test_build_is_deterministic(self):
        self.chembl([mol("CHEMBL2", "B", 2.0), mol("CHEMBL1", "A", 4.0)])
        self.write_manifest()
        a, _ = self.build()
        b, _ = self.build()
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))
        self.assertEqual([e["id"] for e in a], ["CAT:CHEMBL1", "CAT:CHEMBL2"])


class OfflineBuildAndHook(Base):
    def test_build_and_card_link_never_touch_the_network(self):
        self.chembl([mol("CHEMBL1", "A", 4.0)])
        self.write_manifest()
        def boom(*a, **k):
            raise AssertionError("network used during build")
        o1, o2 = cb.jget, cb.http
        cb.jget = cb.http = boom
        try:
            entries, _ = self.build()
            links = cb.cmd_cards(entries)  # reads the real cards of the repo; ids absent from the lookup cache stay UNRESOLVED
        finally:
            cb.jget, cb.http = o1, o2
        self.assertGreater(links["cards_considered"], 0)
        self.assertTrue(all(l.get("catalogue_id") is None or l["rule"] for c in links["cards"].values() for l in c["links"]))

    def test_units_keep_records_families_and_wwox_evaluation_apart(self):
        self.chembl([mol("CHEMBL1", "A", 4.0, ik="SKEL-AAA-N"), mol("CHEMBL2", "A salt", 4.0, parent="CHEMBL1", ik="SKEL-BBB-N"), mol("CHEMBL3", "B", 2.0, ik="OTHER-CCC-N")])
        self.write_manifest()
        _, stats = self.build()
        u = stats["units"]
        self.assertEqual((u["records_enumerated"], u["chemical_families_reconciled"]["families"]), (3, 2))
        self.assertEqual(u["compounds_evaluated_against_WWOX_needs"], 0)
        self.assertIn("NOT distinct drugs", u["records_are"])

    def test_generic_lookup_module(self):
        self.chembl([mol("CHEMBL1", "Aspirin", 4.0)])
        self.write_manifest()
        entries, _ = self.build()
        spec2 = importlib.util.spec_from_file_location("compound_catalog", HERE.parents[4] / "framework/scripts/compound_catalog.py")
        cc = importlib.util.module_from_spec(spec2)
        spec2.loader.exec_module(cc)
        self.assertEqual([e["id"] for e in cc.find(entries, name="aspir")], ["CAT:CHEMBL1"])
        self.assertEqual(cc.find(entries, access="supplement"), [])  # no evidence is an empty list, not a negative claim


if __name__ == "__main__":
    unittest.main(verbosity=1)
