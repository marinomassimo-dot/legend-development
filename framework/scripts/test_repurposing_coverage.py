#!/usr/bin/env python3
"""Offline regressions for repurposing_search.py and repurposing_coverage.py. A tiny synthetic
needs file, catalogue and card set are written to a temp directory; nothing real is read.
Run: python3 -B framework/scripts/test_repurposing_coverage.py"""
from __future__ import annotations

import copy
import gzip
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_coverage as cov  # noqa: E402
import repurposing_search as rs  # noqa: E402


def entry(cid, name, origin="chembl_selected", parent=None, skel=None, targets=(), status="approved_any_source", access=("unknown/unverified",)):
    return {"id": cid, "origin": origin, "name": name, "synonyms": [], "ids": {"skeleton_key": skel, "chembl": cid.replace("CAT:", "")},
            "relations": {"parent": parent, "is_parent": parent is None, "children": []}, "modality": "small_molecule",
            "status_records": [{"source": "ChEMBL", "max_phase": 4.0}], "status_class": status, "access_categories": list(access),
            "targets": list(targets)}


def chembl_t(sym, action, organism="Homo sapiens", ttype="SINGLE PROTEIN"):
    return {"source": "ChEMBL curated mechanism", "target_id": "CHEMBLT" + sym, "target_name": sym, "target_type": ttype, "organism": organism,
            "gene_symbols": [sym], "action_type": action, "reference_ids": ["PubMed:1"], "mechanism_of_action": f"{sym} {action}"}


def dg_t(hgnc, gene, itype):
    return {"source": "DGIdb interaction", "gene": gene, "gene_concept_id": hgnc, "interaction_type": itype, "claim_source": "X", "multiplicity": 1}


def need(nid, direction, targets, cards=()):
    return {"id": nid, "label": nid, "intervention_direction": {"direction": direction, "on": "x"}, "targets": targets,
            "evidence_scope": ["WWOX_BIOLOGY_OTHER_CONTEXT"], "counter_evidence": ["c1"], "observed": [{"id": "O1", "evidence_scope": "WWOX_EXPERIMENT_IN_DEE_SYSTEM"}],
            "sources": {"cards": list(cards)}}


def tgt(sym, hgnc, kind="intervention_target"):
    return {"symbol": sym, "hgnc_id": hgnc, "target_kind": kind}


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "cat").mkdir()
        (self.root / "dr/cards").mkdir(parents=True)
        (self.root / "dr/cards_early").mkdir()
        self.needs = [
            need("N-DOWN", "down", [tgt("GRIN1", "HGNC:4584"), tgt("LDHC", "HGNC:6544", "identity_guard")], cards=["C-DRUG"]),
            need("N-UNC", "uncertain", [tgt("PDK1", "HGNC:8809"), tgt("HK2", "HGNC:4923", "readout_marker")]),
            need("N-SHARE", "down", [tgt("GRIN1", "HGNC:4584")]),
            need("N-GENE", "restore", [tgt("WWOX", "HGNC:12799", "disease_gene_product")], cards=["C-AAV"]),
        ]
        self.entries = [
            entry("CAT:CHEMBL1", "Blockerine", skel="AAA", targets=[chembl_t("GRIN1", "NEGATIVE ALLOSTERIC MODULATOR"), chembl_t("PDPK1", "INHIBITOR")]),
            entry("CAT:CHEMBL2", "Blockerine hydrochloride", parent="CAT:CHEMBL1", skel="AAA", targets=[chembl_t("GRIN1", "ANTAGONIST")]),
            entry("CAT:CHEMBL3", "Agonistine", skel="BBB", targets=[chembl_t("GRIN1", "AGONIST"), chembl_t("GRIN1", "AGONIST", organism="Rattus norvegicus")]),
            entry("CAT:CHEMBL4", "Mutedine", skel="CCC", targets=[]),
            entry("CAT:CHEMBL5", "Pdkone", skel="DDD", targets=[chembl_t("PDK1", "INHIBITOR")]),
            entry("CAT:CHEMBL6", "Guardine", skel="EEE", targets=[chembl_t("LDHC", "INHIBITOR")]),
            entry("CAT:DGIDB:aa", "Dgonly", origin="dgidb_only", targets=[dg_t("hgnc:4584", "GRIN1", None), dg_t("hgnc:8816", "PDPK1", "inhibitor")]),
            entry("CAT:DGIDB:bb", "Blockerine", origin="dgidb_only", targets=[dg_t("hgnc:4584", "GRIN1", "antagonist")]),
        ]
        self.write()

    def write(self, src_state="OK"):
        with gzip.open(self.root / "cat/catalog.jsonl.gz", "wt") as fh:
            for e in self.entries:
                fh.write(json.dumps(e) + "\n")
        (self.root / "cat/catalog_stats.json").write_text(json.dumps({"generated_utc": "t", "sources": {k: {"state": src_state} for k in ("chembl", "dgidb", "unichem", "matrix", "openfda_ndc", "dsld")}}))
        (self.root / "cat/card_links.json").write_text(json.dumps({"cards": {
            "C-DRUG": {"links": [{"catalogue_id": "CAT:CHEMBL1", "role": "identity", "rule": "declared"}]},
            "C-AAV": {"links": []}}}))
        (self.root / "cat/non_molecule_modalities.tsv").write_text("card_id\tmodality\twhy\tsource\nC-AAV\tgene_replacement_vector\tvector\tt\n")
        (self.root / "needs.json").write_text(json.dumps({"needs": self.needs}))
        (self.root / "roles.tsv").write_text("need_id\tsymbol\tcoupling\tbasis\nN-DOWN\tGRIN1\tsame\tb\nN-SHARE\tGRIN1\tsame\tb\nN-GENE\tWWOX\tsame\tb\nN-GONE\tXXX\tsame\tstale\n")
        for stem, sub, cand, assertions, comps in (
            ("C-DRUG", "cards", "Blockerine", [
                {"id": "A1", "direction": "DECREASE", "epistemic_status": "DATO", "reading_depth": "complete_fulltext_read", "source": "s1", "context": {"disease_id": "Wwox-null mouse WOREE", "species": "mouse"}},
                {"id": "A2", "direction": "DECREASE", "epistemic_status": "DATO", "reading_depth": "abstract_only", "source": "s2", "context": {"disease_id": "epilepsy (not WWOX)", "species": "rat"}},
                {"id": "A3", "direction": "UNKNOWN", "epistemic_status": "INFERENZA", "reading_depth": "x", "source": "s3", "context": {"disease_id": "WWOX-DEE", "species": "human"}}],
             {"A1": "OPPOSES_DISEASE_CHANGE", "A2": "UNRESOLVED", "A3": "UNRESOLVED"}),
            ("C-AAV", "cards", "AAV", [], {})):
            (self.root / "dr" / sub / f"{stem}.packet.json").write_text(json.dumps({"candidate": {"id": stem, "name": cand}, "route": "r", "drug_assertions": assertions}))
            (self.root / "dr" / sub / f"{stem}.card.json").write_text(json.dumps({"comparisons": [{"assertion_id": k, "status": v} for k, v in comps.items()], "p4_fields": {"endpoint_pursued": "E"}, "next_step": "n", "limits": []}))

    def run_build(self):
        return cov.build(needs_path=self.root / "needs.json", catalog_dir=self.root / "cat", dr=self.root / "dr", roles_path=self.root / "roles.tsv")

    def idx(self):
        return rs.Index(self.entries), rs.load_roles(self.root / "roles.tsv")


class Identity(Fixture):
    def test_pdk1_is_not_pdpk1_by_symbol_or_hgnc(self):
        idx, roles = self.idx()
        r = rs.associations_for_need(self.needs[1], idx, roles)
        ids = {a["catalogue_id"] for a in r["associations"] if a["target"] == "PDK1"}
        self.assertEqual(ids, {"CAT:CHEMBL5"})  # CHEMBL1 (PDPK1 inhibitor) and DGIdb PDPK1 (hgnc:8816) are not PDK1

    def test_identity_guard_is_reported_not_linked_and_nonhuman_set_aside(self):
        idx, roles = self.idx()
        r = rs.associations_for_need(self.needs[0], idx, roles)
        self.assertNotIn("CAT:CHEMBL6", {a["catalogue_id"] for a in r["associations"]})
        self.assertEqual(r["nonhuman_chembl_rows_set_aside"], 1)
        r2 = rs.associations_for_need(need("N-G", "uncertain", [tgt("LDHC", "HGNC:6544", "identity_guard")]), idx, roles)
        self.assertEqual(len(r2["identity_guard_hits"]), 1)
        self.assertEqual(r2["associations"], [])

    def test_salt_and_name_twin_are_separate_records_with_one_family_where_declared(self):
        idx, _ = self.idx()
        self.assertEqual(idx.family["CAT:CHEMBL1"], idx.family["CAT:CHEMBL2"])       # parent link / skeleton
        self.assertNotEqual(idx.family["CAT:CHEMBL1"], idx.family["CAT:DGIDB:bb"])   # same name, no identifier: not merged
        res = self.run_build()
        row = next(r for r in res["matrix"]["rows"] if r["row_id"] == "FAM:CAT:DGIDB:bb")
        self.assertGreaterEqual(row["n_possible_duplicates"], 1)


class Direction(Fixture):
    def test_uncertain_need_is_exploration_not_consistent(self):
        idx, roles = self.idx()
        r = rs.associations_for_need(self.needs[1], idx, roles)
        self.assertTrue(r["exploration_only"])
        self.assertTrue(all(a["consistency"] == "direction_unresolved" for a in r["associations"]))
        self.assertTrue(all("exploration" in a["list_label"] for a in r["associations"]))
        res = self.run_build()
        self.assertTrue(all(p["exploration_only"] for p in res["priorities"]["priorities"] if p["need"] == "N-UNC"))
        self.assertNotIn("consistent_mechanism_candidate", {p["disposition"] for p in res["priorities"]["priorities"] if p["need"] == "N-UNC"})

    def test_down_need_consistent_opposed_unresolved(self):
        idx, roles = self.idx()
        r = rs.associations_for_need(self.needs[0], idx, roles)
        by = {(a["catalogue_id"], a["link_source"][:4]): a["consistency"] for a in r["associations"]}
        self.assertEqual(by[("CAT:CHEMBL1", "ChEM")], "consistent")
        self.assertEqual(by[("CAT:CHEMBL3", "ChEM")], "opposed")
        self.assertEqual(by[("CAT:DGIDB:aa", "DGId")], "direction_unresolved")  # unstated type is unknown, not opposed

    def test_no_role_row_means_unresolved(self):
        idx, _ = self.idx()
        r = rs.associations_for_need(self.needs[0], idx, {})
        self.assertTrue(all(a["consistency"] != "consistent" for a in r["associations"]))

    def test_compound_without_a_card_reaches_needs(self):
        idx, roles = self.idx()
        c = rs.resolve_compound(idx, "agonistine")
        self.assertEqual([e["id"] for e in c], ["CAT:CHEMBL3"])
        touched = rs.compound_to_needs(c[0], self.needs, idx, roles)
        self.assertEqual({(t["need"], t["consistency"]) for t in touched}, {("N-DOWN", "opposed"), ("N-SHARE", "opposed")})

    def test_salt_targets_reach_the_parent_via_family(self):
        idx, roles = self.idx()
        parent_only = [e for e in self.entries if e["id"] == "CAT:CHEMBL2"][0]
        t = rs.compound_to_needs(parent_only, self.needs, idx, roles)
        self.assertTrue(any(x["via_family_member"] == "CAT:CHEMBL1" for x in t))


class UnknownVsFailed(Fixture):
    def test_no_target_rows_is_queried_without_result_and_failed_source_is_distinct(self):
        self.needs[0]["sources"]["cards"] = ["C-DRUG"]
        self.write()
        res = self.run_build()
        self.assertEqual(res["summary"]["source_states"]["chembl"], "OK")
        # a card-cited record with no target rows
        self.entries[0]["targets"] = []
        self.entries[1]["targets"] = []
        self.write()
        d = {p["row_id"]: p["disposition"] for p in self.run_build()["priorities"]["priorities"] if p["need"] == "N-DOWN"}
        self.assertEqual(d["FAM:CAT:CHEMBL1"], "source_queried_without_result")
        self.write(src_state="FAILED")
        d2 = {p["disposition"] for p in self.run_build()["priorities"]["priorities"]}
        self.assertEqual(d2, {"incomplete_or_failed_query"})

    def test_target_known_but_not_this_need_is_not_relevant(self):
        self.entries[0]["targets"] = [chembl_t("ZZZ1", "INHIBITOR")]
        self.entries[1]["targets"] = []
        self.write()
        d = {p["row_id"]: p["disposition"] for p in self.run_build()["priorities"]["priorities"] if p["need"] == "N-DOWN"}
        self.assertEqual(d["FAM:CAT:CHEMBL1"], "not_relevant")

    def test_opposite_mechanism_and_insufficient_data_are_reachable(self):
        self.entries[0]["targets"] = [chembl_t("GRIN1", "AGONIST")]
        self.entries[1]["targets"] = []
        self.write()
        p = {(x["row_id"], x["need"]): x["disposition"] for x in self.run_build()["priorities"]["priorities"]}
        self.assertEqual(p[("FAM:CAT:CHEMBL1", "N-DOWN")], "opposite_mechanism")
        self.assertEqual(p[("INT:C-AAV", "N-GENE")], "insufficient_data")

    def test_stale_role_rows_are_reported(self):
        self.assertEqual(self.run_build()["summary"]["inputs_status"]["stale_role_rows"], ["N-GONE/XXX"])


class LevelsAndCounts(Fixture):
    def cell(self, res, rid, nid):
        return next(c for c in res["matrix"]["cells"] if c["row_id"] == rid and c["need"] == nid)

    def test_levels_are_separate(self):
        res = self.run_build()
        c = self.cell(res, "FAM:CAT:CHEMBL1", "N-DOWN")
        self.assertEqual(c["L1_documented_link"]["state"], "documented")
        self.assertEqual(c["L2_mechanistic_coherence"]["state"], "coherent")
        self.assertEqual(c["L3_observed_effect"]["by_scope"], {"other_disease_precedent": 1, "wwox_experimental": 1})
        self.assertEqual(c["L4_observed_recovery_in_wwox_system"]["assertion_ids"], ["A1"])   # only the WWOX one with OPPOSES
        self.assertEqual(c["L3_observed_effect"]["inference_assertions"], 1)                   # the inference is not an observation
        # a link without any card is not an observation
        c2 = self.cell(res, "FAM:CAT:CHEMBL3", "N-DOWN")
        self.assertEqual((c2["L1_documented_link"]["state"], c2["L3_observed_effect"]["state"], c2["L4_observed_recovery_in_wwox_system"]["state"]), ("documented", "none_in_cards", "none_in_record"))
        self.assertIn("never", json.dumps(res["matrix"]["never_summed"]).lower() + "never")

    def test_non_molecule_intervention_has_own_row_and_is_not_evaluable_not_zero(self):
        res = self.run_build()
        r = next(r for r in res["matrix"]["rows"] if r["row_id"] == "INT:C-AAV")
        self.assertEqual(r["kind"], "non_molecule_intervention")
        self.assertEqual(r["modality"], "gene_replacement_vector")
        c = self.cell(res, "INT:C-AAV", "N-GENE")
        self.assertEqual(c["L1_documented_link"]["state"], "not_evaluable")

    def test_each_family_counts_once_per_need_and_shared_targets_do_not_double_count(self):
        res = self.run_build()
        cells = [c for c in res["matrix"]["cells"] if c["row_id"] == "FAM:CAT:CHEMBL1"]
        self.assertEqual(sorted(c["need"] for c in cells), ["N-DOWN", "N-SHARE"])        # GRIN1 is in two needs: two cells, not four
        c = self.cell(res, "FAM:CAT:CHEMBL1", "N-DOWN")
        self.assertEqual(c["L1_documented_link"]["targets"], ["GRIN1"])                  # the two records of the family collapse into one cell
        cc_ = res["summary"]["catalogue_coverage"]
        self.assertEqual(cc_["families_touching_at_least_one_need_counted_once"], len({a["family"] for a in res["associations"] if a["target_kind"] in rs.LINK_KINDS}))
        self.assertEqual(sum(int(k) * v for k, v in cc_["families_by_number_of_needs_touched"].items()), len({(a["family"], a["need"]) for a in res["associations"] if a["target_kind"] in rs.LINK_KINDS}))

    def test_summary_reconciles_with_matrix_and_priorities(self):
        res = self.run_build()
        m, cells = res["summary"]["matrix"], res["matrix"]["cells"]
        self.assertEqual(m["cells_nonempty"], len(cells))
        self.assertEqual(m["L1_documented"] + m["L1_none_found"] + m["L1_not_evaluable"] + sum(1 for c in cells if c["L1_documented_link"]["state"] == "source_incomplete"), len(cells))
        pri = res["priorities"]
        self.assertEqual(len(pri["priorities"]) + sum(pri["pairs_not_prioritised"].values()), len(cells))
        self.assertEqual(sum(res["summary"]["priorities"]["by_disposition"].values()), len(pri["priorities"]))
        u = res["summary"]["units"]
        self.assertEqual(u["families"], u["chembl_families"] + u["source_only_families_unresolved_identity"])
        for k in ("pct_records_with_link",):
            x = res["summary"]["catalogue_coverage"][k]
            self.assertEqual(x["percent"], round(100.0 * x["numerator"] / x["denominator"], 1))

    def test_deterministic_regeneration(self):
        a, b = self.run_build(), self.run_build()
        self.assertEqual(cov.dump(a["matrix"], True), cov.dump(b["matrix"], True))
        self.assertEqual(cov.dump(a["priorities"], True), cov.dump(b["priorities"], True))
        self.assertEqual(cov.dump(a["summary"]), cov.dump(b["summary"]))
        out = self.root / "out"
        cov.write_all(a, out)
        self.assertEqual((out / "priorities.json").read_text(), cov.dump(b["priorities"], True))


if __name__ == "__main__":
    unittest.main(verbosity=1)
