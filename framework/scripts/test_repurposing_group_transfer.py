#!/usr/bin/env python3
"""Regressions for the group-transfer guard in repurposing_search.py (IT19 P5 step 4).

A ChEMBL mechanism curated on a PROTEIN FAMILY or PROTEIN COMPLEX GROUP target carries one action
for every component. Expanding it onto each component gene gave a member a direction the source
never measured. The three cases below are the three the fix must get right at once:

  1. a case that previously received an improper attribution, and must now abstain with the reason;
  2. a correctly attributed case at the level the record is written in, which must stay usable;
  3. a case whose action is unknown, which must stay unknown and never gain a label.

Offline, synthetic entries only. Run: python3 -B framework/scripts/test_repurposing_group_transfer.py
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_search as rs  # noqa: E402

TTYPE = ["CACNA1G", "CACNA1H", "CACNA1I"]
BIG_GROUP = TTYPE + ["CACNA1A", "CACNA1B", "CACNA1C", "CACNA1D", "CACNA1E", "CACNA1F", "CACNA1S",
                     "CACNA2D1", "CACNA2D2", "CACNA2D3", "CACNA2D4", "CACNB1", "CACNB2", "CACNB3",
                     "CACNB4", "CACNG1", "CACNG2", "CACNG3", "CACNG4", "CACNG5", "CACNG6", "CACNG7",
                     "CACNG8", "CACNA1G2", "CACNA1H2"]
NMDA_GROUP = ["GRIN1", "GRIN2A", "GRIN2B", "GRIN2D", "GRIN2C", "GRIN3A", "GRIN3B"]


def target(tid, genes, action, ttype):
    return {"source": "ChEMBL curated mechanism", "target_id": tid, "target_name": tid, "target_type": ttype,
            "organism": "Homo sapiens", "gene_symbols": list(genes), "action_type": action,
            "reference_ids": ["PubMed:1"], "mechanism_of_action": "synthetic"}


def entry(cid, name, targets):
    return {"id": "CAT:" + cid, "origin": "chembl_selected", "name": name, "synonyms": [],
            "ids": {"skeleton_key": cid, "chembl": cid}, "relations": {"parent": None, "is_parent": True, "children": []},
            "modality": "small_molecule", "status_records": [{"source": "ChEMBL", "max_phase": 4.0}],
            "status_class": "approved_any_source", "access_categories": ["unknown/unverified"], "targets": targets}


def tgt(sym, hgnc="HGNC:0"):
    return {"symbol": sym, "hgnc_id": hgnc, "target_kind": "intervention_target"}


NEED_SEIZURE = {"id": "N-SEIZURE", "label": "s", "intervention_direction": {"direction": "down", "on": "x"},
                "targets": [tgt("CACNA1G")], "evidence_scope": [], "counter_evidence": [], "observed": [], "sources": {"cards": []}}
NEED_TTYPE = {"id": "N-TTYPE", "label": "t", "intervention_direction": {"direction": "down", "on": "x"},
              "targets": [tgt(s) for s in TTYPE], "evidence_scope": [], "counter_evidence": [], "observed": [], "sources": {"cards": []}}
NEED_NMDA = {"id": "N-NMDA", "label": "n", "intervention_direction": {"direction": "down", "on": "x"},
             "targets": [tgt(s) for s in ("GRIN1", "GRIN2A", "GRIN2B", "GRIN2D")], "evidence_scope": [], "counter_evidence": [],
             "observed": [], "sources": {"cards": []}}
NEEDS = [NEED_SEIZURE, NEED_TTYPE, NEED_NMDA]
ROLES = {(n["id"], s): {"coupling": "same", "qualifier": ""} for n in NEEDS for s in (TTYPE + NMDA_GROUP)}

ENTRIES = [
    entry("CHEMBLGRP", "Groupine", [target("CHEMBL2363032", BIG_GROUP, "BLOCKER", "PROTEIN COMPLEX GROUP")]),
    entry("CHEMBLFAM", "Familine", [target("CHEMBL2362995", TTYPE, "BLOCKER", "PROTEIN FAMILY")]),
    entry("CHEMBLNMDA", "Nmdine", [target("CHEMBL2094124", NMDA_GROUP, "ANTAGONIST", "PROTEIN COMPLEX GROUP")]),
    entry("CHEMBLCPLX", "Complexine", [target("CHEMBL1907603", ["GRIN1", "GRIN2B"], "ANTAGONIST", "PROTEIN COMPLEX")]),
    entry("CHEMBLSING", "Singleine", [target("CHEMBL1859", ["CACNA1H"], "BLOCKER", "SINGLE PROTEIN")]),
    entry("CHEMBLMOD", "Moduline", [target("CHEMBL2363032", BIG_GROUP, "MODULATOR", "PROTEIN COMPLEX GROUP")]),
]
MODULE = rs.module_intervention_symbols(NEEDS)


def rows(need, guard=True):
    idx = rs.Index(ENTRIES, [], MODULE if guard else None)
    return {(a["catalogue_id"], a["target"]): a for a in rs.associations_for_need(need, idx, ROLES)["associations"]}


class GroupTransfer(unittest.TestCase):
    def test_1_previously_improper_attribution_now_abstains_with_the_reason(self):
        before = rows(NEED_TTYPE, guard=False)[("CAT:CHEMBLGRP", "CACNA1G")]
        self.assertEqual(before["consistency"], "consistent")        # the defect, as it was
        after = rows(NEED_TTYPE)[("CAT:CHEMBLGRP", "CACNA1G")]
        self.assertEqual(after["consistency"], "direction_unresolved")
        self.assertIn("group_record_mostly_outside_module_targets", after["consistency_why"])
        self.assertIn("3 of %d components" % len(BIG_GROUP), after["consistency_why"])
        self.assertFalse(after["excluded_from_counts"])               # still visible, not excluded
        self.assertEqual(after["action_raw"], "BLOCKER")              # the source action is not rewritten

    def test_2_records_written_at_the_modules_level_stay_usable(self):
        # T-type family under BOTH needs, including the one that lists a single member
        self.assertEqual(rows(NEED_TTYPE)[("CAT:CHEMBLFAM", "CACNA1G")]["consistency"], "consistent")
        self.assertEqual(rows(NEED_SEIZURE)[("CAT:CHEMBLFAM", "CACNA1G")]["consistency"], "consistent")
        # NMDA receptor group (4 of 7 components among the module's targets), defined complex, single protein
        self.assertEqual(rows(NEED_NMDA)[("CAT:CHEMBLNMDA", "GRIN2A")]["consistency"], "consistent")
        self.assertEqual(rows(NEED_NMDA)[("CAT:CHEMBLCPLX", "GRIN2B")]["consistency"], "consistent")
        self.assertEqual(rows(NEED_TTYPE)[("CAT:CHEMBLSING", "CACNA1H")]["consistency"], "consistent")

    def test_3_unknown_action_stays_unknown_and_never_gains_a_label(self):
        for guard in (False, True):
            a = rows(NEED_TTYPE, guard=guard)[("CAT:CHEMBLMOD", "CACNA1G")]
            self.assertEqual(a["consistency"], "direction_unresolved")
        # the reason is unchanged by the guard: the row was already unresolved because the SOURCE states
        # no direction, and that is the honest reason to keep. The guard never overwrites it.
        for guard in (False, True):
            self.assertIn("no up/down action", rows(NEED_TTYPE, guard=guard)[("CAT:CHEMBLMOD", "CACNA1G")]["consistency_why"])

    def test_guard_is_off_when_no_module_symbols_are_given(self):
        self.assertIsNone(rs.group_transfer_unresolved("ChEMBL curated mechanism",
                                                       target("x", BIG_GROUP, "BLOCKER", "PROTEIN COMPLEX GROUP"), None))
        self.assertIsNone(rs.Index(ENTRIES, []).module_symbols)

    def test_compound_to_needs_applies_the_same_guard(self):
        idx = rs.Index(ENTRIES, [], MODULE)
        e = next(x for x in ENTRIES if x["id"] == "CAT:CHEMBLGRP")
        got = {(x["need"], x["target"]): x for x in rs.compound_to_needs(e, NEEDS, idx, ROLES)}
        self.assertEqual(got[("N-TTYPE", "CACNA1G")]["consistency"], "direction_unresolved")
        fam = next(x for x in ENTRIES if x["id"] == "CAT:CHEMBLFAM")
        got2 = {(x["need"], x["target"]): x for x in rs.compound_to_needs(fam, NEEDS, idx, ROLES)}
        self.assertEqual(got2[("N-SEIZURE", "CACNA1G")]["consistency"], "consistent")


class VisibleLevelAndAbstention(unittest.TestCase):
    """IT19 P6: every association row carries the level of the target the source row is about, the component counts the guard read,
    and a closed abstention class whenever it carries no direction, so a reader can see why a relation is held back."""

    def test_group_abstention_names_level_counts_and_class(self):
        a = rows(NEED_TTYPE, guard=True)[("CAT:CHEMBLGRP", "CACNA1G")]
        self.assertEqual(a["target_level"], "protein_complex_group")
        self.assertEqual((a["record_components"], a["components_in_module_targets"]), (len(BIG_GROUP), 3))
        self.assertEqual(a["abstention_class"], "group_record_mostly_outside_module_targets")

    def test_directed_rows_have_no_abstention_class_and_keep_their_level(self):
        r = rows(NEED_TTYPE, guard=True)
        self.assertIsNone(r[("CAT:CHEMBLSING", "CACNA1H")]["abstention_class"])
        self.assertEqual(r[("CAT:CHEMBLSING", "CACNA1H")]["target_level"], "single_protein")
        self.assertIsNone(r[("CAT:CHEMBLSING", "CACNA1H")]["record_components"])

    def test_unknown_action_is_classed_as_not_stated(self):
        self.assertEqual(rows(NEED_TTYPE, guard=True)[("CAT:CHEMBLMOD", "CACNA1G")]["abstention_class"], "action_not_stated")

    def test_every_reason_the_code_writes_has_a_class_and_an_unknown_one_fails(self):
        self.assertEqual(rs.abstention_class("direction_unresolved", "the need's direction is 'uncertain': exploration only"), "need_direction_not_evaluable")
        self.assertEqual(rs.abstention_class("direction_unresolved", "no explicit role row couples this target"), "no_coupling_row")
        self.assertEqual(rs.abstention_class("direction_unresolved", "role row for X is 'unresolved'"), "coupling_not_measured")
        self.assertEqual(rs.abstention_class("not_evaluable", "anything", "artefact"), "excluded_source_artefact")
        self.assertIsNone(rs.abstention_class("consistent", "anything"))
        with self.assertRaises(ValueError):
            rs.abstention_class("direction_unresolved", "a reason no code path writes")

    def test_dgidb_row_is_a_gene_listing_unless_the_correction_states_a_level(self):
        self.assertEqual(rs.target_level("DGIdb interaction", {}), "gene_listing")
        self.assertEqual(rs.target_level("DGIdb interaction", {"target_level": "complex"}), "protein_complex")
        self.assertEqual(rs.target_level("ChEMBL curated mechanism", {"target_type": "PROTEIN FAMILY"}), "protein_family")

    def test_compound_to_needs_carries_the_same_fields(self):
        idx = rs.Index(ENTRIES, [], MODULE)
        e = next(x for x in ENTRIES if x["id"] == "CAT:CHEMBLGRP")
        got = {(x["need"], x["target"]): x for x in rs.compound_to_needs(e, NEEDS, idx, ROLES)}
        self.assertEqual(got[("N-TTYPE", "CACNA1G")]["abstention_class"], "group_record_mostly_outside_module_targets")
        self.assertEqual(got[("N-TTYPE", "CACNA1G")]["target_level"], "protein_complex_group")


if __name__ == "__main__":
    unittest.main(verbosity=2)
