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


def dg_t2(hgnc, gene, itype, claim):
    t = dg_t(hgnc, gene, itype)
    t["claim_source"] = claim
    return t


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "cat").mkdir()
        (self.root / "dr/cards").mkdir(parents=True)
        (self.root / "dr/cards_early").mkdir()
        self.needs = [
            need("N-DOWN", "down", [tgt("GRIN1", "HGNC:4584"), tgt("GRIA1", "HGNC:4571"), tgt("LDHC", "HGNC:6544", "identity_guard")], cards=["C-DRUG"]),
            need("N-UNC", "uncertain", [tgt("PDK1", "HGNC:8809"), tgt("HK2", "HGNC:4923", "readout_marker")]),
            need("N-SHARE", "down", [tgt("GRIN1", "HGNC:4584")]),
            need("N-GENE", "restore", [tgt("WWOX", "HGNC:12799", "disease_gene_product")], cards=["C-AAV"]),
            need("N-KIND", "uncertain", [tgt("PDK1", "HGNC:8809"), tgt("MAPT", "HGNC:6893", "effector_constraint"), tgt("HIF1A", "HGNC:4910", "pathway_member"), tgt("HK2", "HGNC:4923", "readout_marker")]),
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
            entry("CAT:DGIDB:art", "Adenoish", origin="dgidb_only", targets=[dg_t2("hgnc:4584", "GRIN1", "agonist", "GuideToPharmacology")]),
            entry("CAT:DGIDB:ok2", "Realish", origin="dgidb_only", targets=[dg_t2("hgnc:4584", "GRIN1", "inhibitor", "GuideToPharmacology"), dg_t2("hgnc:4584", "GRIN1", "inhibitor", "TTD")]),
            entry("CAT:DGIDB:null", "Null", origin="dgidb_only", targets=[dg_t2("hgnc:4584", "GRIN1", "inhibitor", "TTD")]),
            entry("CAT:DGIDB:alias", "Aliasine", origin="dgidb_only", targets=[dg_t2("hgnc:8809", "PDK1", "inhibitor", "TdgClinicalTrial"), dg_t2("hgnc:8816", "PDPK1", "inhibitor", "DTC")]),
            entry("CAT:DGIDB:tau", "Tauish", origin="dgidb_only", targets=[dg_t2("hgnc:6893", "MAPT", None, "TTD"), dg_t2("hgnc:4923", "HK2", None, "TTD")]),
            entry("CAT:DGIDB:exp", "Expandine", origin="dgidb_only", targets=[dg_t2("hgnc:1", "AAAA1", "inhibitor", "GuideToPharmacology"), dg_t2("hgnc:2", "AAAA2", "agonist", "GuideToPharmacology"), dg_t2("hgnc:3", "AAAA3", None, "GuideToPharmacology")]),
            entry("CAT:DGIDB:fill", "Filler", origin="dgidb_only", targets=[dg_t2(f"hgnc:{100+i}", f"G{i:03d}", None, "TTD") for i in range(80)]),
            entry("CAT:DGIDB:hif", "Hifish", origin="dgidb_only", targets=[dg_t2("hgnc:4910", "HIF1A", None, "TTD")]),
        ]
        self.write()

    def write(self, src_state="OK", extra_stats=None):
        with gzip.open(self.root / "cat/catalog.jsonl.gz", "wt") as fh:
            for e in self.entries:
                fh.write(json.dumps(e) + "\n")
        st = {"generated_utc": "2026-10-28T00:00:00Z", "sources": {k: {"state": src_state} for k in ("chembl", "dgidb", "unichem", "matrix", "openfda_ndc", "dsld")}}
        st.update(extra_stats or {})
        (self.root / "cat/catalog_stats.json").write_text(json.dumps(st))
        (self.root / "cat/card_links.json").write_text(json.dumps({"cards": {
            "C-DRUG": {"links": [{"catalogue_id": "CAT:CHEMBL1", "role": "identity", "rule": "declared"}]},
            "C-AAV": {"links": []}}}))
        (self.root / "cat/non_molecule_modalities.tsv").write_text("card_id\tmodality\twhy\tsource\nC-AAV\tgene_replacement_vector\tvector\tt\n")
        (self.root / "needs.json").write_text(json.dumps({"needs": self.needs}))
        (self.root / "roles.tsv").write_text("need_id\tsymbol\tcoupling\tbasis\tqualifier\nN-DOWN\tGRIN1\tsame\tb\tone full block only\nN-DOWN\tGRIA1\tunresolved\tb\tguess\nN-SHARE\tGRIN1\tsame\tb\t\nN-GENE\tWWOX\tsame\tb\t\nN-GONE\tXXX\tsame\tstale\t\n")
        (self.root / "artefacts.tsv").write_text("claim_source\tsymbol\trule\tevidence\nGuideToPharmacology\tGRIN1\trequire_second_source\ttest\nGuideToPharmacology\t*\tearly_alphabet_run:min=3:top=0.08\ttest\n*\tPDK1\talias_risk:PDPK1\ttest\n")
        P = [("C-DRUG", "A1", "N-DOWN", "card", "readout_in_wwox_system", "benefit", "yes", "yes", "high_dose_arm", "b"),
             ("C-DRUG", "A2", "N-DOWN", "CHEMBL3", "readout_other_disease", "harm", "no", "no", "", "b"),
             ("C-DRUG", "A3", "N-DOWN", "card", "target_engagement_assay", "benefit", "no", "no", "", "b"),
             ("C-DRUG", "A4", "N-DOWN", "card", "readout_in_wwox_system", "mixed", "yes", "no", "low_dose_arm", "b"),
             ("C-DRUG", "A5", "N-DOWN", "tool_no_catalogue_identity", "readout_in_wwox_system", "benefit", "yes", "no", "", "b")]
        (self.root / "pert.tsv").write_text("\t".join(cov.PERT_COLS) + "\n" + "\n".join("\t".join(x) for x in P) + "\n")
        for stem, sub, cand, assertions, comps in (
            ("C-DRUG", "cards", "Blockerine", [
                {"id": "A1", "direction": "DECREASE", "epistemic_status": "DATO", "reading_depth": "complete_fulltext_read", "source": "s1", "context": {"disease_id": "Wwox-null mouse WOREE", "species": "mouse"}},
                {"id": "A2", "direction": "DECREASE", "epistemic_status": "DATO", "reading_depth": "abstract_only", "source": "s2", "context": {"disease_id": "epilepsy (not WWOX)", "species": "rat"}},
                {"id": "A3", "direction": "DECREASE", "epistemic_status": "DATO", "reading_depth": "x", "source": "s3", "context": {"disease_id": "enzyme assay (not WWOX)", "species": "human"}},
                {"id": "A4", "direction": "INCREASE", "epistemic_status": "DATO", "reading_depth": "complete_fulltext_read", "source": "s4", "context": {"disease_id": "Wwox-null mouse WOREE", "species": "mouse"}},
                {"id": "A5", "direction": "DECREASE", "epistemic_status": "DATO", "reading_depth": "complete_fulltext_read", "source": "s5", "context": {"disease_id": "Wwox-null slices", "species": "mouse"}},
                {"id": "A6", "direction": "NO_CHANGE", "epistemic_status": "DATO", "reading_depth": "complete_fulltext_read", "source": "s6", "context": {"disease_id": "Wwox-null mouse WOREE", "species": "mouse"}}],
             {"A1": "OPPOSES_DISEASE_CHANGE", "A2": "UNRESOLVED", "A3": "UNRESOLVED", "A4": "OPPOSES_DISEASE_CHANGE", "A5": "UNRESOLVED", "A6": "UNRESOLVED"}),
            ("C-AAV", "cards", "AAV", [], {})):
            (self.root / "dr" / sub / f"{stem}.packet.json").write_text(json.dumps({"candidate": {"id": stem, "name": cand}, "route": "r", "drug_assertions": assertions}))
            (self.root / "dr" / sub / f"{stem}.card.json").write_text(json.dumps({"comparisons": [{"assertion_id": k, "status": v} for k, v in comps.items()], "p4_fields": {"endpoint_pursued": "E"}, "next_step": "n", "limits": []}))

    def run_build(self):
        return cov.build(needs_path=self.root / "needs.json", catalog_dir=self.root / "cat", dr=self.root / "dr", roles_path=self.root / "roles.tsv",
                         artefacts_path=self.root / "artefacts.tsv", pertinence_path=self.root / "pert.tsv")

    def idx(self):
        return rs.Index(self.entries, rs.load_artefacts(self.root / "artefacts.tsv")), rs.load_roles(self.root / "roles.tsv")


class Identity(Fixture):
    def test_pdk1_is_not_pdpk1_by_symbol_or_hgnc(self):
        idx, roles = self.idx()
        r = rs.associations_for_need(self.needs[1], idx, roles)
        ids = {a["catalogue_id"] for a in r["associations"] if a["target"] == "PDK1" and not a["excluded_from_counts"]}
        self.assertEqual(ids, {"CAT:CHEMBL5"})  # CHEMBL1 (PDPK1 inhibitor) and DGIdb PDPK1 (hgnc:8816) are not PDK1
        alias = [a for a in r["associations"] if a["catalogue_id"] == "CAT:DGIDB:alias"]
        self.assertTrue(alias and all(a["excluded_from_counts"].startswith("alias_risk") for a in alias))   # PDK1 row on a PDPK1 record: unresolved, listed, not counted

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
        self.assertTrue(all(a["consistency"] == "direction_unresolved" for a in r["associations"] if not a["excluded_from_counts"]))
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
        self.assertEqual(res["summary"]["source_states"]["chembl"]["state"], "OK")
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
        self.assertEqual(d["FAM:CAT:CHEMBL1"], "no_catalogue_link_found")

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

    def test_levels_are_separate_and_signs_are_carried(self):
        res = self.run_build()
        c = self.cell(res, "FAM:CAT:CHEMBL1", "N-DOWN")
        self.assertEqual(c["L1_documented_link"]["state"], "documented")
        self.assertEqual(c["L2_mechanistic_coherence"]["state"], "coherent")
        self.assertIn("one full block only", c["L2_mechanistic_coherence"]["certainty_qualifiers"])
        l3 = c["L3_observed_effect"]
        self.assertEqual(l3["state"], "observed_wwox_system")
        self.assertEqual(l3["signs_wwox_system_readouts"], {"benefit": 1, "mixed": 1})       # dose arms: benefit and mixed, never pooled into one sign
        self.assertEqual(l3["target_engagement_assays_not_readouts"], 1)                      # an enzyme assay is not an observed effect
        self.assertEqual(l3["assertion_ids"], ["A1", "A4"])
        l4 = c["L4_observed_recovery_in_wwox_system"]
        self.assertEqual((l4["state"], l4["assertion_ids"]), ("observed_experimental", ["A1"]))   # the low-dose-arm assertion A4 is not recovery
        # a link without any pertinent assertion is not an observation
        c2 = self.cell(res, "FAM:CAT:CHEMBL3", "N-DOWN")
        self.assertEqual((c2["L1_documented_link"]["state"], c2["L3_observed_effect"]["state"], c2["L4_observed_recovery_in_wwox_system"]["state"]), ("documented", "precedent_other_disease_only", "none_in_record"))

    def test_harm_is_attached_to_its_subject_and_not_pooled_with_benefit(self):
        res = self.run_build()
        c = self.cell(res, "FAM:CAT:CHEMBL3", "N-DOWN")                      # A2 (harm) has subject CHEMBL3, not the card's declared CHEMBL1
        self.assertEqual(c["L3_observed_effect"]["signs_other_disease_precedent_not_observed_here"], {"harm": 1})
        self.assertEqual(self.cell(res, "FAM:CAT:CHEMBL1", "N-DOWN")["L3_observed_effect"]["signs_other_disease_precedent_not_observed_here"], {})

    def test_tool_subject_is_its_own_row_and_never_attached_to_a_named_drug(self):
        res = self.run_build()
        r = next(r for r in res["matrix"]["rows"] if r["row_id"] == "INT:C-DRUG:tool")
        self.assertEqual(r["kind"], "tool_compound_or_genetic_precedent_not_in_catalogue")
        c = self.cell(res, "INT:C-DRUG:tool", "N-DOWN")
        self.assertEqual(c["L3_observed_effect"]["assertion_ids"], ["A5"])
        self.assertEqual(c["L1_documented_link"]["state"], "not_evaluable")
        self.assertNotIn("A5", self.cell(res, "FAM:CAT:CHEMBL1", "N-DOWN")["L3_observed_effect"]["assertion_ids"])

    def test_mention_in_card_text_does_not_attach_observations(self):
        links = json.loads((self.root / "cat/card_links.json").read_text())
        links["cards"]["C-DRUG"]["links"].append({"catalogue_id": "CAT:CHEMBL3", "rule": "chembl_id_mentioned_in_card_text"})   # no role = a mention
        (self.root / "cat/card_links.json").write_text(json.dumps(links))
        res = self.run_build()
        r = next(r for r in res["matrix"]["rows"] if r["row_id"] == "FAM:CAT:CHEMBL3")
        self.assertFalse([c for c in r["cards"] if c["attachment"] not in ("assertion_subject",)])

    def test_non_molecule_intervention_has_own_row_and_is_not_evaluable_not_zero(self):
        res = self.run_build()
        r = next(r for r in res["matrix"]["rows"] if r["row_id"] == "INT:C-AAV")
        self.assertEqual(r["kind"], "non_molecule_intervention")
        self.assertEqual(r["modality"], "gene_replacement_vector")
        c = self.cell(res, "INT:C-AAV", "N-GENE")
        self.assertEqual(c["L1_documented_link"]["state"], "not_evaluable")

    def test_source_artefact_rows_are_excluded_but_listed(self):
        res = self.run_build()
        ass = {a["catalogue_id"]: a for a in res["associations"] if a["need"] == "N-DOWN" and a["target"] == "GRIN1" and a["link_source"].startswith("DGIdb")}
        self.assertTrue(ass["CAT:DGIDB:art"]["excluded_from_counts"].startswith("source_artefact"))     # lone Guide-to-Pharmacology row
        self.assertIsNone(ass["CAT:DGIDB:ok2"]["excluded_from_counts"])                                  # same source corroborated by TTD
        self.assertTrue(ass["CAT:DGIDB:null"]["excluded_from_counts"].startswith("placeholder"))
        cells = {(c["row_id"], c["need"]) for c in res["matrix"]["cells"]}
        self.assertNotIn(("FAM:CAT:DGIDB:art", "N-DOWN"), cells)
        self.assertNotIn(("FAM:CAT:DGIDB:null", "N-DOWN"), cells)
        self.assertIn(("FAM:CAT:DGIDB:ok2", "N-DOWN"), cells)
        by_reason = res["summary"]["catalogue_coverage"]["excluded_rows"]["by_reason"]
        self.assertGreaterEqual(by_reason.get("source_artefact", 0), 1)
        self.assertGreaterEqual(by_reason.get("placeholder", 0), 1)

    def test_only_intervention_targets_are_headline_links(self):
        res = self.run_build()
        per = res["summary"]["needs"]["per_need"]["N-KIND"]
        kinds = per["by_target_kind_records_families"]
        self.assertEqual(kinds["effector_constraint"]["records"], 1)      # MAPT: listed, counted by kind
        self.assertEqual(kinds["pathway_member"]["records"], 1)
        self.assertEqual(per["headline_records_intervention_targets"], 1)  # PDK1 (CHEMBL5) only
        self.assertEqual(per["records_incl_pathway_members"], 2)           # pathway members counted apart
        self.assertNotIn(("FAM:CAT:DGIDB:tau", "N-KIND"), {(c["row_id"], c["need"]) for c in res["matrix"]["cells"]})   # MAPT/readout-only: no cell
        hif = self.cell(res, "FAM:CAT:DGIDB:hif", "N-KIND")
        self.assertEqual(hif["L1_documented_link"]["state"], "pathway_member_only")
        cov_ = res["summary"]["catalogue_coverage"]
        self.assertLess(cov_["union_headline_records"], cov_["union_with_pathway_members_records"])

    def test_gria_role_unresolved_never_consistent(self):
        idx, roles = self.idx()
        n = self.needs[0]
        label, why = rs.consistency(n, tgt("GRIA1", "HGNC:4571"), "down", roles)
        self.assertEqual(label, "direction_unresolved")
        self.assertIn("inferred, not measured", why)

    def test_stale_export_is_a_state_and_caveats_absence(self):
        self.entries[0]["targets"] = [chembl_t("ZZZ1", "INHIBITOR")]
        self.entries[1]["targets"] = []
        self.write(extra_stats={"dgidb_age": {"export_in_use": {"last_modified": "Mon, 10 Jun 2024 16:04:52 GMT"}}})
        res = self.run_build()
        self.assertEqual(res["summary"]["source_states"]["dgidb"]["state"], "STALE_EXPORT")
        self.assertEqual(res["summary"]["inputs_status"]["stale_sources"], ["dgidb"])
        p = next(p for p in res["priorities"]["priorities"] if p["row_id"] == "FAM:CAT:CHEMBL1" and p["need"] == "N-DOWN")
        self.assertEqual(p["disposition"], "no_catalogue_link_found")
        self.assertIn("STALE", p["disposition_reason"])                      # absence on a stale source says so
        self.assertTrue(p["source_caveats"])

    def test_any_source_failure_blocks_dispositions(self):
        raw = json.loads((self.root / "cat/catalog_stats.json").read_text())
        raw["sources"]["openfda_ndc"] = {"state": "FAILED"}
        (self.root / "cat/catalog_stats.json").write_text(json.dumps(raw))
        self.assertEqual({p["disposition"] for p in self.run_build()["priorities"]["priorities"]}, {"incomplete_or_failed_query"})

    def test_each_family_counts_once_per_need_and_shared_targets_do_not_double_count(self):
        res = self.run_build()
        cells = [c for c in res["matrix"]["cells"] if c["row_id"] == "FAM:CAT:CHEMBL1"]
        self.assertEqual(sorted(c["need"] for c in cells), ["N-DOWN", "N-SHARE"])        # GRIN1 is in two needs: two cells, not four
        c = self.cell(res, "FAM:CAT:CHEMBL1", "N-DOWN")
        self.assertEqual(c["L1_documented_link"]["targets"], ["GRIN1"])                  # the two records of the family collapse into one cell
        cc_ = res["summary"]["catalogue_coverage"]
        head = [a for a in res["associations"] if not a["excluded_from_counts"] and a["target_kind"] in rs.LINK_KINDS]
        self.assertEqual(cc_["union_headline_families"], len({a["family"] for a in head}))
        self.assertEqual(sum(int(k) * v for k, v in cc_["families_by_number_of_needs_touched"].items()), len({(a["family"], a["need"]) for a in head}))

    def test_cells_vs_distinct_families_are_both_reported(self):
        res = self.run_build()
        pr = res["summary"]["priorities"]
        self.assertGreaterEqual(pr["by_disposition_cells"]["consistent_mechanism_candidate"], pr["by_disposition_distinct_families_or_rows"]["consistent_mechanism_candidate"])

    def test_summary_reconciles_with_matrix_and_priorities(self):
        res = self.run_build()
        m, cells = res["summary"]["matrix"], res["matrix"]["cells"]
        self.assertEqual(m["cells_nonempty"], len(cells))
        for k in ("L1_states", "L2_states", "L3_states", "L4_states"):
            self.assertEqual(sum(m[k].values()), len(cells))
        pri = res["priorities"]
        self.assertEqual(len(pri["priorities"]) + sum(pri["pairs_not_prioritised"].values()), len(cells))
        self.assertEqual(sum(res["summary"]["priorities"]["by_disposition_cells"].values()), len(pri["priorities"]))
        u = res["summary"]["units"]
        self.assertEqual(u["families"], u["chembl_families"] + u["source_only_families_unresolved_identity"])
        x = res["summary"]["catalogue_coverage"]["pct_records_with_headline_link"]
        self.assertEqual(x["percent"], round(100.0 * x["numerator"] / x["denominator"], 1))
        o = res["summary"]["observations"]
        self.assertEqual(o["assertions_listed_in_pertinence_table"] + o["assertions_not_assessed_for_pertinence_not_counted"], o["data_assertions_in_intervention_cards"])

    def test_deterministic_regeneration(self):
        a, b = self.run_build(), self.run_build()
        self.assertEqual(cov.dump(a["matrix"], True), cov.dump(b["matrix"], True))
        self.assertEqual(cov.dump(a["priorities"], True), cov.dump(b["priorities"], True))
        self.assertEqual(cov.dump(a["summary"]), cov.dump(b["summary"]))
        out = self.root / "out"
        cov.write_all(a, out)
        self.assertEqual((out / "priorities.json").read_text(), cov.dump(b["priorities"], True))


def ob(aid, kind, sign="benefit", depth="complete_fulltext_read", l3=True, l4=False, comp="OPPOSES_DISEASE_CHANGE", flags=""):
    return {"id": aid, "kind": kind, "sign": sign, "reading_depth": depth, "counts_L3": l3, "counts_L4": l4, "comparison": comp, "flags": flags, "card_id": "C"}


class ObservationRules(unittest.TestCase):
    def test_unknown_reading_depth_never_reaches_observed_wwox_system(self):
        l3, l4 = cov.observation_levels([ob("X1", "readout_in_wwox_system", depth="UNKNOWN", l4=True)])
        self.assertEqual(l3["state"], "observed_depth_unknown")
        self.assertEqual(l4["state"], "none_in_record")
        self.assertEqual(l3["signs_depth_unknown_not_counted_as_observed"], {"benefit": 1})

    def test_uninformative_report_and_control_arm_do_not_make_a_null_or_an_observation(self):
        l3, _ = cov.observation_levels([ob("W7", "case_report_uninformative", sign="null", l3=False), ob("L2", "control_arm_same_experiment")])
        self.assertEqual(l3["state"], "none_in_cards")
        self.assertIn("W7:case_report_uninformative", l3["listed_not_counted"])
        self.assertEqual(l3["signs_control_arms_of_the_same_experiment"], {"benefit": 1})

    def test_null_of_the_same_experiment_stays_visible_beside_a_benefit(self):
        l3, _ = cov.observation_levels([ob("A", "readout_in_wwox_system"), ob("B", "readout_in_wwox_system", sign="null")])
        self.assertEqual(l3["signs_wwox_system_readouts"], {"benefit": 1, "null": 1})
        self.assertEqual(l3["state"], "observed_wwox_system")

    def test_growth_l4_carries_the_body_weight_note(self):
        _, l4 = cov.observation_levels([ob("W", "readout_in_wwox_system", l4=True, flags="growth=body_weight_only")])
        self.assertIn("body weight only", l4["endpoint_note"])


class Detector(Fixture):
    def test_generic_alphabetical_prefix_expansion_is_flagged_and_a_lone_early_gene_is_not(self):
        idx, _ = self.idx()
        e = next(x for x in self.entries if x["id"] == "CAT:DGIDB:exp")
        flagged = [rs.artefact_reason(e, t, idx.artefacts, idx.early) for t in e["targets"]]
        self.assertTrue(all(f and f.startswith("source_artefact") for f in flagged))
        e2 = dict(e, targets=[e["targets"][0]])                      # one early symbol only: not an expansion run
        self.assertIsNone(rs.artefact_reason(e2, e2["targets"][0], idx.artefacts, idx.early))
        e3 = dict(e, targets=e["targets"] + [dg_t2("hgnc:1", "AAAA1", "inhibitor", "TTD")])   # a second source corroborates AAAA1
        self.assertIsNone(rs.artefact_reason(e3, e3["targets"][0], idx.artefacts, idx.early))

    def test_excluded_rows_carry_an_explicit_reason(self):
        res = self.run_build()
        reasons = {a["excluded_reason"] for a in res["associations"] if a["excluded_from_counts"]}
        self.assertEqual(reasons, {"source_artefact", "alias_risk", "placeholder"})
        self.assertTrue(all(a["excluded_reason"] is None for a in res["associations"] if not a["excluded_from_counts"]))

    def test_unassessed_assertion_is_flagged_per_cell_and_dsld_partial_is_carried(self):
        self.write(extra_stats={"dsld": {"bulk_list_probed": 981, "bulk_list_planned_names": 4697}})
        raw = json.loads((self.root / "cat/catalog_stats.json").read_text())
        res = self.run_build()
        c = next(c for c in res["matrix"]["cells"] if c["row_id"] == "FAM:CAT:CHEMBL1" and c["need"] == "N-DOWN")
        self.assertEqual(c["L3_observed_effect"]["unassessed_assertions_on_card"], ["C-DRUG/A6"])   # A6 (a null of the same experiment) is not listed
        self.assertEqual(res["summary"]["source_states"]["dsld"]["state"], "PARTIAL")
        self.assertTrue(res["summary"]["access_caveats"])
        p = next(p for p in res["priorities"]["priorities"] if p["row_id"] == "FAM:CAT:CHEMBL1")
        self.assertIn("name-only", p["criteria"]["pharmacology_safety_info"]["access_caveat"])


REAL = rs.DR
@unittest.skipUnless((REAL / "coverage/priorities.json").exists() and (REAL / "catalog/catalog.jsonl.gz").exists(), "real module data not present")
class RealFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.cat = Path(cls.tmp.name) / "cat"
        cls.cat.mkdir()
        for f in ("catalog.jsonl.gz", "catalog_stats.json", "card_links.json", "non_molecule_modalities.tsv"):
            (cls.cat / f).write_bytes((REAL / "catalog" / f).read_bytes())
        cls.base = cov.build()

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_hard_failed_source_on_the_real_files_turns_every_disposition_incomplete(self):
        st = json.loads((self.cat / "catalog_stats.json").read_text())
        st["sources"]["unichem"] = {"state": "FAILED"}
        (self.cat / "catalog_stats.json").write_text(json.dumps(st))
        res = cov.build(catalog_dir=self.cat)
        self.assertEqual({p["disposition"] for p in res["priorities"]["priorities"]}, {"incomplete_or_failed_query"})
        self.assertEqual(len(res["priorities"]["priorities"]), len(self.base["priorities"]["priorities"]))   # all of them flip, none is dropped
        self.assertEqual(res["summary"]["inputs_status"]["hard_problem_sources"], ["unichem"])
        st["sources"]["unichem"] = {"state": "OK"}
        (self.cat / "catalog_stats.json").write_text(json.dumps(st))

    def test_real_outcomes_of_the_audit_corrections(self):
        per = self.base["summary"]["needs"]["per_need"]
        self.assertEqual(per["NEED-INHIBITORY-HYPOFUNCTION"]["headline_records_intervention_targets"], 11)
        self.assertEqual(per["NEED-GSK3B-DEREPRESSION"]["headline_records_intervention_targets"], 51)
        cells = {(c["row_id"], c["need"]): c for c in self.base["matrix"]["cells"]}
        a51 = cells[("INT:D01_a51", "NEED-MYC-PROGENITOR-PROLIFERATION")]
        self.assertEqual(a51["L3_observed_effect"]["state"], "observed_depth_unknown")
        self.assertEqual(a51["L4_observed_recovery_in_wwox_system"]["state"], "none_in_record")
        pera = [c for (r, n), c in cells.items() if r == "FAM:CAT:CHEMBL1214124" and n == "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR"][0]
        self.assertEqual(pera["L3_observed_effect"]["state"], "none_in_cards")                           # n=1 polytherapy supports nothing
        self.assertTrue(all(not c["L3_observed_effect"]["unassessed_assertions_on_card"] for c in cells.values() if c["L3_observed_effect"]["state"].startswith("observed")))
        self.assertIn("None of the interventions", self.base["summary"]["plain_statement"])



if __name__ == "__main__":
    unittest.main(verbosity=1)
