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


class TargetIdentity(Base):
    """DGIdb Guide-to-Pharmacology rows: gene_claim_name NCBIGENE:<n> is a GtoPdb TARGET id; identity is checked against the release."""

    def gtopdb(self):
        d = self.cache / "gtopdb"
        d.mkdir(parents=True, exist_ok=True)
        with open(d / "targets_and_families.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["# GtoPdb Version: T"])
            w.writerow(["Type", "Family id", "Target id", "Subunit id", "Target name", "HGNC id", "HGNC symbol"])
            w.writerows([["lgic", "75", "456", "", "GluN2A", "4585", "GRIN2A"], ["lgic", "75", "457", "", "GluN2B", "4586", "GRIN2B"],
                         ["enzyme", "9", "2893", "", "BCAT2", "977", "BCAT2"], ["enzyme", "10", "2464", "", "ABAT", "23", "ABAT"],
                         ["lgic", "68", "373", "", "5-HT3A", "5297", "HTR3A"], ["lgic", "68", "374", "", "5-HT3B", "5298", "HTR3B"],
                         ["lgic", "68", "378", "373|374", "5-HT3AB", "", ""]])
        with open(d / "interactions.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["# GtoPdb Version: T"])
            w.writerow(["Target ID", "Target Species", "Ligand ID", "Type", "Selectivity", "Primary Target"])
            w.writerows([["456", "Human", "4168", "Antagonist", "Selective", "false"], ["457", "Human", "4168", "Antagonist", "Selective", "false"],
                         ["2893", "Human", "777", "Inhibitor", "Not Determined", "false"], ["378", "Human", "888", "Agonist", "", "true"]])
        self.src("gtopdb", "T")

    def row(self, claim_n, gene, hgnc, lig):
        return [f"NCBIGENE:{claim_n}", hgnc, gene, "GuideToPharmacology", "2024.1", "inhibitor", "1", f"IUPHAR.LIGAND:{lig}", f"iuphar.ligand:{lig}", "LIGX", "FALSE", "FALSE", "FALSE"]

    def targets(self, rows):
        self.chembl([mol("CHEMBL1", "Ligx", 4.0)])
        self.dgidb([["LIGX", "n", "chembl:CHEMBL1", "LIGX", "FALSE", "FALSE", "FALSE", "ChEMBL", "33"]], [[*r] for r in rows])
        self.write_manifest()
        entries, stats = self.build()
        return [t for t in entries[0]["targets"] if t["source"] == "DGIdb interaction"], stats

    def test_collision_independent_of_any_listed_symbol_is_corrected_through_the_target_id(self):
        self.gtopdb()
        # BCAT2 inhibitor served by DGIdb as GRIA4 because 2893 was read as an NCBI Gene id
        t, stats = self.targets([self.row(2893, "GRIA4", "hgnc:4574", 777)])
        self.assertEqual([(x["gene"], x["identity"]["state"], x["dgidb_served_gene"]["gene"]) for x in t], [("BCAT2", "corrected", "GRIA4")])
        self.assertEqual(stats["dgidb"]["target_identity_by_claim_source_and_state"], {"GuideToPharmacology|corrected": 1})

    def test_genuine_link_on_a_receptor_family_is_confirmed_and_siblings_are_counted(self):
        self.gtopdb()
        t, _ = self.targets([self.row(456, "GRIN2A", "hgnc:4585", 4168)])
        self.assertEqual((t[0]["gene"], t[0]["identity"]["state"], t[0]["same_family_targets_of_this_ligand"], t[0]["target_level"]), ("GRIN2A", "confirmed", 1, "single_protein"))

    def test_complex_target_expands_to_subunits_without_selectivity(self):
        self.gtopdb()
        t, _ = self.targets([self.row(378, "HTR3A", "hgnc:5297", 888)])
        self.assertEqual(sorted(x["gene"] for x in t), ["HTR3A", "HTR3B"])
        self.assertTrue(all(x["target_level"] == "complex" for x in t))

    def test_unresolvable_pair_is_unverified_not_confirmed_and_without_the_release_nothing_is_confirmed(self):
        self.gtopdb()
        t, _ = self.targets([self.row(2464, "ABAT", "hgnc:23", 999)])       # pair absent from the release
        self.assertEqual(t[0]["identity"]["state"], "unverified")
        import shutil
        shutil.rmtree(self.cache / "gtopdb")
        self.manifest["sources"].pop("gtopdb")
        t, _ = self.targets([self.row(456, "GRIN2A", "hgnc:4585", 4168)])
        self.assertEqual(t[0]["identity"]["state"], "unverified")

    def test_pseudogene_or_antisense_resolution_of_a_symbol_claim_is_flagged_not_trusted(self):
        r = {"gene_claim_name": "MCL1", "gene_name": "ADAMTSL4-AS1", "interaction_source_db_name": "DTC"}
        self.assertIn("non-coding", cb.claim_symbol_anomaly(r))
        self.assertIsNone(cb.claim_symbol_anomaly({"gene_claim_name": "IL8", "gene_name": "CXCL8", "interaction_source_db_name": "NCI"}))   # a renamed symbol is not an anomaly
        self.assertIsNone(cb.claim_symbol_anomaly({"gene_claim_name": "TP53", "gene_name": "TP53", "interaction_source_db_name": "NCI"}))

    def test_uniprot_accession_and_viral_protein_claims_resolved_to_noncoding_or_retroelement_loci_are_flagged(self):
        for claim, gene, src, word in (("UNIPROT:Q07820", "ADAMTSL4-AS1", "TdgClinicalTrial", "UniProt accession"), ("UNIPROT:Q9Y233", "LINC00473", "TEND", "UniProt accession"),
                                       ("POL", "ERVW-4", "ChEMBL", "retrovirus"), ("ENV", "ERVK-20", "ChEMBL", "retrovirus"), ("PROTEASE", "ERVK-10", "ChEMBL", "retrovirus")):
            self.assertIn(word, cb.claim_symbol_anomaly({"gene_claim_name": claim, "gene_name": gene, "interaction_source_db_name": src}), claim)
        for claim, gene in (("UNIPROT:P08588", "ADRB1"), ("UNIPROT:Q9Y5Y9", "SCN10A"), ("ERVW-1", "ERVW-1"), ("HERV-K", "ERVK-6"), ("NCBIGENE:2902", "GRIN1")):   # an accession served as its own protein gene is not flagged
            self.assertIsNone(cb.claim_symbol_anomaly({"gene_claim_name": claim, "gene_name": gene, "interaction_source_db_name": "TEND"}), claim)


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


class LigandReconciliation(Base):
    """DGIdb-only records with an IUPHAR ligand id -> GtoPdb ligand -> ChEMBL id -> ChEMBL record.  Identifiers and structure decide, never a name."""

    LIG_COLS = ["Ligand ID", "Name", "Species", "Type", "Approved", "Withdrawn", "Labelled", "Radioactive", "ChEMBL ID", "InChIKey"]

    def world(self, mols, ligands, drugs, lookup=None, ligands_file=True):
        """ligands = [(id, name, chembl, inchikey, {extra column: value})]; drugs = [(drug_name, [ligand ids], extra concept ids)]"""
        self.chembl(mols)
        d = self.cache / "gtopdb"
        d.mkdir(parents=True, exist_ok=True)
        for f, hdr in (("targets_and_families.csv", ["Type", "Family id", "Target id", "Subunit id", "Target name", "HGNC id", "HGNC symbol"]),
                       ("interactions.csv", ["Target ID", "Target Species", "Ligand ID", "Type", "Selectivity", "Primary Target"])):
            with open(d / f, "w", newline="", encoding="utf-8") as fh:
                w = csv.writer(fh)
                w.writerow(["# GtoPdb Version: T"])
                w.writerow(hdr)
        if ligands_file:
            with open(d / "ligands.csv", "w", newline="", encoding="utf-8") as fh:
                w = csv.writer(fh)
                w.writerow(["# GtoPdb Version: T"])
                w.writerow(self.LIG_COLS)
                for lid, name, ch, ik, extra in ligands:
                    row = {"Ligand ID": lid, "Name": name, "Type": "Synthetic organic", "ChEMBL ID": ch, "InChIKey": ik} | extra
                    w.writerow([row.get(c, "") for c in self.LIG_COLS])
        if lookup is not None:
            (self.cache / cb.GTOPDB_REF_LOOKUP).write_text(json.dumps({"status_by_id": lookup}))
        self.src("gtopdb", "T")
        rows = []
        for name, lids, extra in drugs:
            for lid in lids:
                rows.append([name, "n", f"iuphar.ligand:{lid}", name, "FALSE", "FALSE", "FALSE", "GuideToPharmacology", "2024.1"])
            for c in extra:
                rows.append([name, "n", c, name, "FALSE", "FALSE", "FALSE", "DrugBank", "5"])
        self.dgidb(rows)
        self.write_manifest()
        return self.build()

    @staticmethod
    def m(cid, name, ik, parent=None, **kw):
        r = mol(cid, name, 4.0, parent=parent, ik=ik)
        r.update(kw)
        return r

    def rels(self, entries):
        return {e["ids"]["dgidb_drug_name"]: e["relations"] for e in entries if e["origin"] == "dgidb_only"}

    def dec(self, entries):
        return {k: [(r["ligand_id"], r["decision"], r["reason"]) for r in v.get("gtopdb_reconciliation", [])] for k, v in self.rels(entries).items()}

    def test_merge_on_equal_inchikey_keeps_the_record_and_adds_a_tagged_relation(self):
        K = "AAAAAAAAAAAAAA-BBBBBBBBSA-N"
        entries, stats = self.world([self.m("CHEMBL1", "Drugine", K)], [("11", "Drugine", "CHEMBL1", K, {})], [("DRUGINE-X", ["11"], [])])
        by = {e["id"]: e for e in entries}
        rec = [e for e in entries if e["origin"] == "dgidb_only"][0]
        self.assertEqual(len(entries), 2)                                       # nothing fused or deleted
        self.assertEqual(rec["relations"]["reconciled_via"], "gtopdb_ligand_chembl_ref")
        self.assertEqual(rec["relations"]["family_join"], ["CAT:CHEMBL1"])
        self.assertEqual(by["CAT:CHEMBL1"]["relations"]["reconciled_source_records"], [rec["id"]])
        r = rec["relations"]["gtopdb_reconciliation"][0]
        self.assertEqual((r["decision"], r["chembl_ref"], r["source_tag"]), ("merged", "CHEMBL1", "gtopdb_ligand_chembl_ref"))
        self.assertIn("share-alike", r["terms"]["chembl"] + r["terms"]["gtopdb"])  # licence terms travel with the relation
        self.assertIn("GtoPdb Version: T", r["asserted_by"]["chembl_ref"])
        self.assertEqual(stats["gtopdb_ligand_reconciliation"]["decisions_all_pairs_with_a_relation"]["merged"], 1)
        self.assertEqual(stats["merge_report"]["entries_merged_away"], 0)

    def test_family_follows_a_merged_relation_only(self):
        sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
        import repurposing_search as rs  # noqa: PLC0415
        K, K2 = "AAAAAAAAAAAAAA-BBBBBBBBSA-N", "CCCCCCCCCCCCCC-BBBBBBBBSA-N"
        entries, _ = self.world([self.m("CHEMBL1", "Drugine", K), self.m("CHEMBL2", "Other", K2)],
                                [("11", "Drugine", "CHEMBL1", K, {}), ("12", "Other", "CHEMBL2", "CCCCCCCCCCCCCC-DDDDDDDDSA-N", {})],
                                [("DRUGINE-X", ["11"], []), ("OTHER-X", ["12"], [])])
        fam = rs.families(entries)
        ids = {e["ids"]["dgidb_drug_name"]: e["id"] for e in entries if e["origin"] == "dgidb_only"}
        self.assertEqual(fam[ids["DRUGINE-X"]], fam["CAT:CHEMBL1"])
        self.assertNotEqual(fam[ids["OTHER-X"]], fam["CAT:CHEMBL2"])             # related_not_merged: relation kept, family not joined
        self.assertEqual(self.dec(entries)["OTHER-X"][0][1], "related_not_merged")

    def test_parent_and_salt_forms(self):
        P, S = "AAAAAAAAAAAAAA-BBBBBBBBSA-N", "ZZZZZZZZZZZZZZ-BBBBBBBBSA-M"
        mols = [self.m("CHEMBL10", "Drugine", P), self.m("CHEMBL11", "Drugine sodium", S, parent="CHEMBL10")]
        entries, _ = self.world(mols, [("1", "d parent", "CHEMBL10", P, {}), ("2", "d salt as given", "CHEMBL11", S, {}), ("3", "d parent id on a salt ref", "CHEMBL11", P, {})],
                                [("D-PARENT", ["1"], []), ("D-SALT", ["2"], []), ("D-AMBIGUOUS", ["3"], [])])
        d = self.dec(entries)
        self.assertEqual(d["D-PARENT"][0][1:], ("merged", "full_inchikey_equal"))
        self.assertEqual(d["D-SALT"][0][1:], ("merged", "full_inchikey_equal"))   # the salt record itself, by its own key
        self.assertEqual(d["D-AMBIGUOUS"][0][1], "related_not_merged")            # structure of the parent, reference to the salt: form not settled
        self.assertIn("parent_form", d["D-AMBIGUOUS"][0][2])

    def test_stereoisomer_racemate_and_undefined_stereo_are_not_merged(self):
        K = "AAAAAAAAAAAAAA-BBBBBBBBSA-N"
        entries, _ = self.world([self.m("CHEMBL20", "Single enantiomer", K)],
                                [("21", "other enantiomer", "CHEMBL20", "AAAAAAAAAAAAAA-CCCCCCCCSA-N", {}), ("22", "racemate or flat drawing", "CHEMBL20", "AAAAAAAAAAAAAA-UHFFFAOYSA-N", {}),
                                 ("23", "protonated form", "CHEMBL20", "AAAAAAAAAAAAAA-BBBBBBBBSA-M", {})],
                                [("ENANTIOMER", ["21"], []), ("RACEMATE", ["22"], []), ("CHARGE", ["23"], [])])
        d = self.dec(entries)
        self.assertEqual(d["ENANTIOMER"][0][1:], ("related_not_merged", "stereoisomers_or_isotopologues_differ"))
        self.assertEqual(d["RACEMATE"][0][1:], ("related_not_merged", "stereo_or_isotopes_undefined_in_gtopdb_defined_in_chembl"))
        self.assertEqual(d["CHARGE"][0][1], "related_not_merged")
        self.assertFalse(any("family_join" in v for v in self.rels(entries).values()))

    def test_one_to_many_in_both_directions(self):
        K, K2 = "AAAAAAAAAAAAAA-BBBBBBBBSA-N", "CCCCCCCCCCCCCC-BBBBBBBBSA-N"
        mols = [self.m("CHEMBL1", "One", K), self.m("CHEMBL2", "Two", K2)]
        lig = [("1", "a", "CHEMBL1", K, {}), ("2", "b", "CHEMBL1", K, {}), ("3", "c", "CHEMBL1", K, {"Radioactive": "yes"}), ("4", "d", "CHEMBL2", K2, {})]
        entries, stats = self.world(mols, lig, [("MANY-A", ["1"], []), ("MANY-B", ["2"], []), ("LABELLED", ["3"], []), ("BRIDGE", ["1", "4"], [])])
        d = self.dec(entries)
        self.assertEqual(d["MANY-A"][0][1], "merged")
        self.assertEqual(d["MANY-B"][0][1], "merged")                            # several ligands -> one ChEMBL id: each decided on its own structure
        self.assertEqual(d["LABELLED"][0][2], "labelled_or_radioactive_form_of_the_ligand")
        ev = [e for e in entries if e["ids"].get("dgidb_drug_name") == "MANY-A"][0]["relations"]["gtopdb_reconciliation"][0]["evidence"]
        self.assertEqual(ev["gtopdb_ligands_sharing_this_chembl_ref"], 3)
        self.assertEqual({x[1:] for x in d["BRIDGE"]}, {("unresolved", "one_dgidb_record_would_join_several_chembl_families")})   # one record, two families
        self.assertNotIn("family_join", self.rels(entries)["BRIDGE"])
        self.assertEqual(stats["gtopdb_ligand_reconciliation"]["records_refused_for_bridging_several_chembl_families"], 1)

    def test_one_record_with_two_ligands_in_one_family_is_not_a_bridge(self):
        P, S = "AAAAAAAAAAAAAA-BBBBBBBBSA-N", "ZZZZZZZZZZZZZZ-BBBBBBBBSA-M"
        mols = [self.m("CHEMBL10", "Drugine", P), self.m("CHEMBL11", "Drugine sodium", S, parent="CHEMBL10")]
        entries, _ = self.world(mols, [("1", "p", "CHEMBL10", P, {}), ("2", "s", "CHEMBL11", S, {})], [("BOTH", ["1", "2"], [])])
        self.assertEqual(self.rels(entries)["BOTH"]["family_join"], ["CAT:CHEMBL10", "CAT:CHEMBL11"])

    def test_chembl_id_outside_the_selection_is_kept_as_a_reference_not_dropped(self):
        K = "AAAAAAAAAAAAAA-BBBBBBBBSA-N"
        lookup = {"CHEMBL900": {"entity_type": "COMPOUND", "status": "ACTIVE"}, "CHEMBL901": {"entity_type": "COMPOUND", "status": "INACTIVE"},
                  "CHEMBL902": {"entity_type": None, "status": "NOT_RETURNED"}, "CHEMBL903": {"entity_type": "DOCUMENT", "status": "ACTIVE"}}
        lig = [(str(i), f"x{i}", f"CHEMBL{900 + i - 1}", K, {}) for i in range(1, 5)]
        entries, stats = self.world([self.m("CHEMBL1", "In", "QQQQQQQQQQQQQQ-BBBBBBBBSA-N")], lig,
                                    [("OUT-ACTIVE", ["1"], []), ("OUT-INACTIVE", ["2"], []), ("OUT-UNKNOWN", ["3"], []), ("OUT-DOC", ["4"], [])], lookup=lookup)
        d = self.dec(entries)
        self.assertEqual(d["OUT-ACTIVE"][0][1:], ("out_of_selection", "chembl_id_active_but_not_in_catalogue_selection"))
        self.assertEqual(d["OUT-INACTIVE"][0][1:], ("unresolved", "chembl_id_obsolete_or_inactive"))
        self.assertEqual(d["OUT-UNKNOWN"][0][1:], ("unresolved", "chembl_id_unknown_to_chembl_lookup"))
        self.assertEqual(d["OUT-DOC"][0][1:], ("unresolved", "chembl_id_is_not_a_compound_record"))
        rec = [e for e in entries if e["ids"].get("dgidb_drug_name") == "OUT-ACTIVE"][0]["relations"]["gtopdb_reconciliation"][0]
        self.assertEqual((rec["chembl_ref"], rec["chembl_ref_in_catalogue"]), ("CHEMBL900", False))
        self.assertFalse(any("family_join" in v for v in self.rels(entries).values()))
        self.assertEqual(stats["gtopdb_ligand_reconciliation"]["decisions_all_pairs_with_a_relation"]["out_of_selection"], 1)
        # without the lookup file the status is not known: said so, still not dropped
        (self.cache / cb.GTOPDB_REF_LOOKUP).unlink()
        entries2, _ = self.world([self.m("CHEMBL1", "In", "QQQQQQQQQQQQQQ-BBBBBBBBSA-N")], lig[:1], [("OUT-ACTIVE", ["1"], [])])
        self.assertEqual(self.dec(entries2)["OUT-ACTIVE"][0][1:], ("out_of_selection", "chembl_id_not_in_selection_status_not_checked"))

    def test_identifier_structure_conflict_is_rejected_even_with_the_same_name(self):
        entries, _ = self.world([self.m("CHEMBL1", "Lx2931", "AAAAAAAAAAAAAA-BBBBBBBBSA-N")],
                                [("5", "LX2931", "CHEMBL1", "MMMMMMMMMMMMMM-BBBBBBBBSA-N", {})], [("LX2931", ["5"], [])])
        r = self.rels(entries)["LX2931"]
        self.assertEqual(r["gtopdb_reconciliation"][0]["decision"], "rejected_conflict")
        self.assertTrue(r["gtopdb_reconciliation"][0]["evidence"]["name_agrees_not_a_basis"])   # the name agreed; it decided nothing
        self.assertNotIn("family_join", r)

    def test_withdrawn_is_an_annotation_not_an_identity_change_but_a_contradicting_drugbank_id_blocks(self):
        K = "AAAAAAAAAAAAAA-BBBBBBBBSA-N"
        mols = [self.m("CHEMBL1", "Gone", K, withdrawn_flag=True)]
        entries, _ = self.world(mols, [("7", "Gone", "CHEMBL1", K, {"Withdrawn": "yes"})], [("GONE", ["7"], [])])
        r = [e for e in entries if e["origin"] == "dgidb_only"][0]["relations"]["gtopdb_reconciliation"][0]
        self.assertEqual(r["decision"], "merged")
        self.assertEqual((r["evidence"]["gtopdb_withdrawn"], r["evidence"]["chembl_withdrawn_flag"]), ("yes", True))
        for n in (2, 7, 14):
            unichem(self.cache / f"unichem/src1src{n}.txt.gz", [("CHEMBL1", "DB99999")] if n == 2 else [])
        self.src("unichem", "T")
        entries, _ = self.world(mols, [("7", "Gone", "CHEMBL1", K, {})], [("GONE", ["7"], ["drugbank:DB00001"])])
        self.assertEqual(self.dec(entries)["GONE"][0][1:], ("unresolved", "drugbank_ids_disjoint_between_dgidb_and_chembl_unichem"))
        self.assertNotIn("family_join", self.rels(entries)["GONE"])

    def test_unresolved_cases_are_preserved_with_a_reason_and_listed_in_the_tables(self):
        mols = [self.m("CHEMBL1", "Antibody", None), self.m("CHEMBL2", "Peptide", "AAAAAAAAAAAAAA-BBBBBBBBSA-N")]
        lig = [("31", "ab", "CHEMBL1", "", {"Type": "Antibody"}), ("32", "pep", "CHEMBL2", "", {}), ("33", "nochembl", "", "", {})]
        entries, stats = self.world(mols, lig, [("AB", ["31"], []), ("PEP", ["32"], []), ("NOCHEMBL", ["33"], []), ("ABSENT", ["999"], [])])
        d = self.dec(entries)
        self.assertEqual(d["AB"][0][1:], ("unresolved", "structure_unavailable_both_sides"))
        self.assertEqual(d["PEP"][0][1:], ("unresolved", "structure_unavailable_gtopdb_side"))
        self.assertEqual(d["ABSENT"][0][1:], ("unresolved", "ligand_id_absent_from_gtopdb_release"))
        self.assertEqual(d["NOCHEMBL"], [])                                  # no ChEMBL id in GtoPdb: no relation, but counted
        s = stats["gtopdb_ligand_reconciliation"]
        self.assertEqual((s["pairs_ligand_without_chembl_id_in_gtopdb_no_relation_made"], s["pairs_ligand_absent_from_release"]), (1, 1))
        self.assertFalse(any("family_join" in v for v in self.rels(entries).values()))
        rows = cb.reconciliation_rows(entries)
        self.assertEqual(sorted((r["candidate"] != "", r["decision"]) for r in rows), [(True, "unresolved")] * 3)

    def test_without_ligands_csv_the_step_is_absent_not_zero(self):
        entries, stats = self.world([self.m("CHEMBL1", "A", "AAAAAAAAAAAAAA-BBBBBBBBSA-N")], [], [("A-X", ["1"], [])], ligands_file=False)
        self.assertEqual(stats["gtopdb_ligand_reconciliation"]["state"], "NOT_AVAILABLE")
        self.assertFalse(any("gtopdb_reconciliation" in e["relations"] for e in entries))

    def test_counts_reconcile_and_tables_are_written_and_deterministic(self):
        K = "AAAAAAAAAAAAAA-BBBBBBBBSA-N"
        old = (cb.OUT_RECON, cb.OUT_RECON_OPEN)
        cb.OUT_RECON, cb.OUT_RECON_OPEN = self.root / "r.tsv", self.root / "ro.tsv"
        try:
            entries, stats = self.world([self.m("CHEMBL1", "A", K)], [("1", "a", "CHEMBL1", K, {}), ("2", "b", "CHEMBL1", "AAAAAAAAAAAAAA-CCCCCCCCSA-N", {})],
                                        [("A-OK", ["1"], []), ("A-REL", ["2"], [])])
            info = cb.write_reconciliation_tables(entries)
            lines = cb.OUT_RECON.read_text().splitlines()
            first = cb.OUT_RECON.read_bytes()
            cb.write_reconciliation_tables(entries)
            self.assertEqual(first, cb.OUT_RECON.read_bytes())
            self.assertEqual((info["rows_all"], info["rows_not_merged"]), (2, 1))
            self.assertEqual(len(lines), 3)
            self.assertEqual(len(cb.OUT_RECON_OPEN.read_text().splitlines()), 2)
        finally:
            cb.OUT_RECON, cb.OUT_RECON_OPEN = old
        s = stats["gtopdb_ligand_reconciliation"]
        self.assertEqual(sum(s["decisions_all_pairs_with_a_relation"].values()), s["pairs_with_a_chembl_reference_all"] + s["pairs_ligand_absent_from_release"])

    def test_compare_structures_layers(self):
        self.assertEqual(cb.compare_structures("A" * 14 + "-" + "B" * 8 + "SA-N", "A" * 14 + "-" + "B" * 8 + "SA-N"), ("equal", "full_inchikey_equal"))
        self.assertEqual(cb.compare_structures("A" * 14 + "-UHFFFAOYSA-N", "B" * 14 + "-UHFFFAOYSA-N")[0], "conflict")
        self.assertEqual(cb.compare_structures(None, None)[0], "unavailable")
        self.assertEqual(cb.compare_structures("", "A" * 14 + "-UHFFFAOYSA-N"), ("unavailable", "structure_unavailable_gtopdb_side"))

    def test_reconciled_build_is_independent_of_hash_randomisation(self):
        import subprocess
        K = "AAAAAAAAAAAAAA-BBBBBBBBSA-N"
        self.world([self.m("CHEMBL1", "A", K), self.m("CHEMBL2", "B", "CCCCCCCCCCCCCC-BBBBBBBBSA-N")],
                   [("1", "a", "CHEMBL1", K, {}), ("2", "b", "CHEMBL1", K, {}), ("3", "c", "CHEMBL2", "CCCCCCCCCCCCCC-DDDDDDDDSA-N", {})],
                   [("A1", ["1"], []), ("A2", ["2"], []), ("B3", ["3"], [])])
        code = ("import importlib.util,sys,json,hashlib;"
                f"s=importlib.util.spec_from_file_location('cb',{str(HERE / 'catalog_build.py')!r});m=importlib.util.module_from_spec(s);sys.modules['cb']=m;s.loader.exec_module(m);"
                f"m.CACHE=m.Path({str(self.cache)!r});m.MANIFEST=m.Path({str(cb.MANIFEST)!r});"
                "e,st=m.build_catalog();print(hashlib.sha256(json.dumps([e,st['gtopdb_ligand_reconciliation']],sort_keys=True).encode()).hexdigest())")
        seen = {subprocess.run([sys.executable, "-B", "-c", code], capture_output=True, text=True, check=True, env={"PYTHONHASHSEED": h, "PATH": "/usr/bin:/bin"}).stdout for h in ("1", "2", "777")}
        self.assertEqual(len(seen), 1)


class DeclaredInputsAndSafeRebuild(Base):
    """The build must know which inputs reproduce the declared version, refuse (or declare partial) otherwise,
    and never replace the last valid outputs with an impoverished result."""

    SENTINEL = b"LAST VALID OUTPUT"

    def setUp(self):
        super().setUp()
        self.out = self.root / "out"
        self.out.mkdir()
        self._old = (cb.OUT_CATALOG, cb.OUT_STATS, cb.OUT_LINKS, cb.OUT_MODALITIES)
        cb.OUT_CATALOG, cb.OUT_STATS, cb.OUT_LINKS, cb.OUT_MODALITIES = (self.out / n for n in ("catalog.jsonl.gz", "catalog_stats.json", "card_links.json", "mod.tsv"))
        self.addCleanup(lambda: (setattr(cb, "OUT_CATALOG", self._old[0]), setattr(cb, "OUT_STATS", self._old[1]),
                                 setattr(cb, "OUT_LINKS", self._old[2]), setattr(cb, "OUT_MODALITIES", self._old[3])))
        for p in (cb.OUT_CATALOG, cb.OUT_STATS, cb.OUT_LINKS):
            p.write_bytes(self.SENTINEL)

    def declare(self, src, rels):
        """Put the sha256 of the cache files into the manifest, as `fetch` does."""
        files = [{"path": r, "sha256": cb.sha256_file(self.cache / r)} for r in rels]
        self.manifest["sources"][src]["data"]["files"] = files

    def world(self, with_gtopdb=True):
        self.chembl([mol("CHEMBL1", "A", 4.0)])
        self.declare("chembl", ["chembl/molecules.jsonl.gz", "chembl/mechanisms.jsonl.gz", "chembl/targets.jsonl.gz"])
        if with_gtopdb:
            for f in cb.GTOPDB_FILES:
                (self.cache / "gtopdb").mkdir(parents=True, exist_ok=True)
                (self.cache / "gtopdb" / f).write_text("# GtoPdb Version: T\nh1,h2\n" if f.startswith("inter") else "# GtoPdb Version: T\nTarget id,Target name\n")
            self.src("gtopdb", "T")
            self.declare("gtopdb", ["gtopdb/" + f for f in cb.GTOPDB_FILES])
        self.write_manifest()

    def untouched(self):
        for p in (cb.OUT_CATALOG, cb.OUT_STATS, cb.OUT_LINKS):
            self.assertEqual(p.read_bytes(), self.SENTINEL, p.name)
        self.assertEqual(sorted(q.name for q in self.out.iterdir()), ["card_links.json", "catalog.jsonl.gz", "catalog_stats.json"])

    def args(self, **kw):
        import argparse
        return argparse.Namespace(**({"partial": False, "check": False} | kw))

    def run_build(self, **kw):
        import contextlib
        import io
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            rc = cb.cmd_build(self.args(**kw))
        return rc, err.getvalue()

    def test_required_inputs_name_source_version_hash_and_how(self):
        self.world()
        rows = {r["path"]: r for r in cb.check_inputs(self.cache, cb.load_manifest())}
        self.assertEqual(rows["gtopdb/interactions.csv"]["status"], "OK")
        self.assertEqual(rows["gtopdb/interactions.csv"]["how"], "fetch --only gtopdb")
        self.assertEqual(len(rows["chembl/molecules.jsonl.gz"]["sha256"]), 64)
        self.assertEqual(rows["chembl/id_lookup.json"]["kind"], "auxiliary")  # needed by the card links, not hashed by the manifest

    def test_complete_cache_builds_and_replaces_the_outputs(self):
        self.world()
        (self.cache / "chembl/id_lookup.json").write_text("{}")
        rc, _ = self.run_build()
        self.assertEqual(rc, 0)
        self.assertNotEqual(cb.OUT_CATALOG.read_bytes(), self.SENTINEL)
        self.assertEqual([e["id"] for e in cb.read_gz_jsonl(cb.OUT_CATALOG)], ["CAT:CHEMBL1"])
        self.assertEqual(json.loads(cb.OUT_STATS.read_text())["catalog_file"]["sha256"], cb.sha256_file(cb.OUT_CATALOG))

    def test_missing_required_file_refuses_names_it_and_leaves_last_output_untouched(self):
        self.world()
        (self.cache / "gtopdb/interactions.csv").unlink()
        rc, err = self.run_build()
        self.assertEqual(rc, 3)
        self.assertIn("BUILD REFUSED", err)
        self.assertIn("gtopdb/interactions.csv", err)
        self.assertIn("LEGEND_CATALOG_CACHE", err)
        self.assertIn("fetch --only gtopdb", err)
        self.untouched()

    def test_empty_cache_refuses_and_leaves_last_output_untouched(self):
        self.world()
        import shutil
        shutil.rmtree(self.cache)
        rc, _ = self.run_build()
        self.assertEqual(rc, 3)
        self.untouched()

    def test_file_that_does_not_match_the_declared_hash_refuses(self):
        self.world()
        (self.cache / "gtopdb/targets_and_families.csv").write_text("# another release\n")
        rc, err = self.run_build()
        self.assertEqual(rc, 3)
        self.assertIn("HASH_MISMATCH", err)
        self.untouched()

    def test_partial_is_declared_kept_apart_and_never_overwrites_the_complete_files(self):
        self.world()
        (self.cache / "gtopdb/interactions.csv").unlink()
        rc, _ = self.run_build(partial=True)
        self.assertEqual(rc, 0)
        for p in (cb.OUT_CATALOG, cb.OUT_STATS, cb.OUT_LINKS):
            self.assertEqual(p.read_bytes(), self.SENTINEL)
        self.assertEqual(sorted(q.name for q in self.out.iterdir()),
                         sorted(["card_links.json", "card_links.PARTIAL.json", "catalog.jsonl.gz", "catalog.PARTIAL.jsonl.gz", "catalog_stats.json", "catalog_stats.PARTIAL.json"]))
        st = json.loads((self.out / "catalog_stats.PARTIAL.json").read_text())
        self.assertIn("NOT equivalent", st["PARTIAL_BUILD"]["declared"])
        self.assertEqual(st["PARTIAL_BUILD"]["sources_excluded"], ["gtopdb"])
        self.assertEqual(st["sources"]["gtopdb"]["state"], "EXCLUDED_MISSING_OR_MISMATCHING_INPUT")
        self.assertEqual(st["catalog_file"]["path"], "catalog.PARTIAL.jsonl.gz")

    def test_partial_without_the_chembl_backbone_is_refused_too(self):
        self.world()
        (self.cache / "chembl/targets.jsonl.gz").unlink()
        rc, _ = self.run_build(partial=True)
        self.assertEqual(rc, 3)
        self.untouched()

    def test_check_never_writes_and_reports_match_or_difference(self):
        self.world()
        (self.cache / "chembl/id_lookup.json").write_text("{}")
        self.assertEqual(self.run_build()[0], 0)
        before = {p.name: p.read_bytes() for p in self.out.iterdir()}
        self.assertEqual(self.run_build(check=True)[0], 0)  # rebuilt == the file just built
        cb.OUT_CATALOG.write_bytes(b"something else")
        self.assertEqual(self.run_build(check=True)[0], 4)
        cb.OUT_CATALOG.write_bytes(before["catalog.jsonl.gz"])
        self.assertEqual({p.name: p.read_bytes() for p in self.out.iterdir()}, before)

    def test_failed_reconciliation_writes_nothing(self):
        self.world()
        (self.cache / "chembl/id_lookup.json").write_text("{}")
        orig = cb.reconcile
        cb.reconcile = lambda e, s: ["forced"]
        try:
            rc, _ = self.run_build()
        finally:
            cb.reconcile = orig
        self.assertEqual(rc, 2)
        self.untouched()

    def test_output_is_independent_of_hash_randomisation(self):
        import subprocess
        self.world()
        code = ("import importlib.util,sys,json,hashlib;"
                f"s=importlib.util.spec_from_file_location('cb',{str(HERE / 'catalog_build.py')!r});m=importlib.util.module_from_spec(s);sys.modules['cb']=m;s.loader.exec_module(m);"
                f"m.CACHE=m.Path({str(self.cache)!r});m.MANIFEST=m.Path({str(cb.MANIFEST)!r});"
                "e,_=m.build_catalog();print(hashlib.sha256(json.dumps(e,sort_keys=True).encode()).hexdigest())")
        seen = {subprocess.run([sys.executable, "-B", "-c", code], capture_output=True, text=True, check=True, env={"PYTHONHASHSEED": h, "PATH": "/usr/bin:/bin"}).stdout for h in ("1", "2", "31337")}
        self.assertEqual(len(seen), 1)


if __name__ == "__main__":
    unittest.main(verbosity=1)
