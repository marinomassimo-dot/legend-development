#!/usr/bin/env python3
"""IT20 P4 - three properties of the search layer, on contrasting synthetic fixtures.

These are written BEFORE a verifier sees the change, and they are about PROPERTIES, not about the
four compounds that prompted the work. Every entry here is synthetic; the real-catalogue figures
live in disease-models/wwox/research/drug_repurposing/matching_it20_engine_20261102/.

  P1  DUPLICATED EVIDENCE is not multiplied support.
      A curated record and another database's copy of that same record are ONE assertion. The copy
      stays listed (a reader must see who serves what) but shares the record's `assertion_key`, so a
      consumer that counts assertions counts one.

  P2  IMPROPER TRANSFER between molecules or targets does not happen, through an intermediary either.
      A record written above the gene does not resolve its single curated action to a member gene,
      and neither does a copy of that record. Evidence on one subunit stays on that subunit, and a
      documented measurement for one molecule does not reach another molecule.

  P3  AN UNKNOWN is never turned into a negative, and never into a direction.
      `direction_unresolved` with a reason is not an exclusion: the row keeps its compound, its claim
      source, its action and its place in the listing. An unstated action stays unstated, and the
      guard never overwrites a reason that is already the honest one.

Why THESE cases discriminate (each row below fails at least one plausible wrong implementation):

  | fixture | what it would catch |
  |---|---|
  | improper attribution through an intermediary (`GRPCOPY`) | a guard that only inspects the original source's rows and lets a republished copy through -- the exact IT19 residual |
  | valid specific evidence kept (`DOCD` on the documented gene) | a guard that abstains on every group record, discarding information the module does have |
  | family/complex documented at the relevant level (`FAM`, `CPLX`, `NMDA`) | a guard keyed on "is it a group?" instead of "is it written at the level the module reasons about?" |
  | a copy of a LEGITIMATE record (`FAMCOPY`) | an over-broad republication rule that abstains on every copy regardless of what it copies |
  | unknown pharmacology (`MOD`, `MODCOPY`) | a guard that writes a label, or a new reason, over a row the source itself left unstated |
  | WWOX role unresolved despite known pharmacology (`N-NOROLE`) | a waiver that leaks into the second judgment: what a compound does at a target must not decide whether that target is coupled to the need |
  | opposing signal kept visible (`OPP`, `OPPCOPY`) | an asymmetric rule that protects an unfavourable label it would have removed if favourable, or that hides an exclusion |
  | documented evidence is subunit- and molecule-specific (`DOCD` siblings, `OTHERMOL`) | a waiver read as a class or a compound-family permission |
  | a family-level document offered as a subunit waiver (`test_a_group_level_document_is_refused`) | a table used to launder a class result into a subunit direction |

Offline, synthetic entries only, no network, no real catalogue.
Run: python3 -B framework/scripts/test_repurposing_provenance.py
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_search as rs  # noqa: E402

TTYPE = ["CACNA1G", "CACNA1H", "CACNA1I"]
BIG_GROUP = TTYPE + [f"CACNA{x}" for x in ("1A", "1B", "1C", "1D", "1E", "1F", "1S", "2D1", "2D2", "2D3", "2D4",
                                           "B1", "B2", "B3", "B4", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8")]
NMDA_GROUP = ["GRIN1", "GRIN2A", "GRIN2B", "GRIN2D", "GRIN2C", "GRIN3A", "GRIN3B"]

# the republication datum, exactly as source_artefacts.tsv holds it (evidence shortened)
REPUB = {"claim_source": "ChEMBL", "symbol": "*", "rule": "republication:ChEMBL",
         "evidence": "synthetic: the republishing export carries the action but not the original record id or its level"}
# a documented single-protein measurement for ONE molecule on ONE gene with ONE action
DOCD_RULE = {"claim_source": "ChEMBL", "symbol": "CACNA1H", "rule": "target_level_documented:CHEMBLDOC:BLOCKER:single_protein",
             "evidence": "synthetic: functional patch clamp on recombinant CACNA1H, IC50 0.4 umol/l at -70 mV; no sibling value found"}


def chembl_row(tid, genes, action, ttype):
    return {"source": "ChEMBL curated mechanism", "target_id": tid, "target_name": tid, "target_type": ttype,
            "organism": "Homo sapiens", "gene_symbols": list(genes), "action_type": action,
            "reference_ids": ["PubMed:1"], "mechanism_of_action": "synthetic", "inherited_from_parent": None}


def dgidb_copy(gene, hgnc, interaction, claim_source="ChEMBL"):
    """A republished row as DGIdb serves one: the action, one gene, and NO record id or level."""
    return {"source": "DGIdb interaction", "claim_source": claim_source, "gene": gene, "gene_claim_name": gene,
            "gene_concept_id": hgnc, "interaction_type": interaction, "interaction_type_state": "stated",
            "multiplicity": 1, "identity": {"state": "as_served", "method": "none", "note": "synthetic"}}


def gtopdb_row(gene, hgnc, interaction, iuphar="42"):
    """A DGIdb row whose gene was checked against the source's own target id: it carries a real level."""
    return {"source": "DGIdb interaction", "claim_source": "GuideToPharmacology", "gene": gene,
            "gene_claim_name": f"{gene}|{iuphar}", "gene_concept_id": hgnc, "interaction_type": interaction,
            "interaction_type_state": "stated", "multiplicity": 1, "iuphar_target_id": iuphar,
            "target_level": "single_protein", "identity": {"state": "confirmed", "method": "gtopdb_target_id", "note": "synthetic"}}


HGNC = {"CACNA1G": "hgnc:1", "CACNA1H": "hgnc:2", "CACNA1I": "hgnc:3",
        "GRIN1": "hgnc:4", "GRIN2A": "hgnc:5", "GRIN2B": "hgnc:6", "GRIN2D": "hgnc:7"}


def entry(cid, name, targets, chembl=None, parent=None):
    ids = {"skeleton_key": cid}
    if chembl is not False:
        ids["chembl"] = chembl or cid
    return {"id": "CAT:" + cid, "origin": "chembl_selected" if chembl is not False else "dgidb_only", "name": name,
            "synonyms": [], "ids": ids,
            "relations": {"parent": parent, "is_parent": parent is None, "children": []},
            "modality": "small_molecule", "status_records": [{"source": "ChEMBL", "max_phase": 4.0}],
            "status_class": "approved_any_source", "access_categories": ["unknown/unverified"], "targets": targets}


def tgt(sym, kind="intervention_target"):
    return {"symbol": sym, "hgnc_id": HGNC[sym], "target_kind": kind}


def need(nid, syms, direction="down"):
    return {"id": nid, "label": nid, "intervention_direction": {"direction": direction, "on": "x"},
            "targets": [tgt(s) for s in syms], "evidence_scope": [], "counter_evidence": [], "observed": [],
            "sources": {"cards": []}}


N_TTYPE = need("N-TTYPE", TTYPE)
N_NMDA = need("N-NMDA", ["GRIN1", "GRIN2A", "GRIN2B", "GRIN2D"])
N_NOROLE = need("N-NOROLE", TTYPE)          # same targets, but no role row couples them
NEEDS = [N_TTYPE, N_NMDA, N_NOROLE]
MODULE = rs.module_intervention_symbols(NEEDS)
# the WWOX side of the model: N-TTYPE and N-NMDA have a measured coupling, N-NOROLE has none
ROLES = {(n["id"], s): {"coupling": "same", "qualifier": ""} for n in (N_TTYPE, N_NMDA) for s in TTYPE + NMDA_GROUP}

ENTRIES = [
    # 1. improper attribution, and the SAME assertion republished as a bare gene row by a second database
    entry("CHEMBLGRP", "Groupine", [chembl_row("CHEMBL2363032", BIG_GROUP, "BLOCKER", "PROTEIN COMPLEX GROUP"),
                                    dgidb_copy("CACNA1G", HGNC["CACNA1G"], "blocker")]),
    # 2. the same copy with NO ChEMBL identifier of its own: the original record cannot be resolved at all
    entry("GRPCOPY", "Groupine copy", [dgidb_copy("CACNA1G", HGNC["CACNA1G"], "blocker")], chembl=False),
    # 3. records written at the level the module reasons about, each with a copy of itself
    entry("FAM", "Familine", [chembl_row("CHEMBL2362995", TTYPE, "BLOCKER", "PROTEIN FAMILY"),
                              dgidb_copy("CACNA1G", HGNC["CACNA1G"], "blocker")]),
    entry("FAMCOPY", "Familine copy", [dgidb_copy("CACNA1G", HGNC["CACNA1G"], "blocker")], chembl=False),
    entry("NMDA", "Nmdine", [chembl_row("CHEMBL2094124", NMDA_GROUP, "ANTAGONIST", "PROTEIN COMPLEX GROUP"),
                             dgidb_copy("GRIN2A", HGNC["GRIN2A"], "inhibitor")]),
    entry("CPLX", "Complexine", [chembl_row("CHEMBL1907603", ["GRIN1", "GRIN2B"], "ANTAGONIST", "PROTEIN COMPLEX")]),
    # 4. unknown pharmacology: the source states no up/down action, in the record and in the copy
    entry("MOD", "Moduline", [chembl_row("CHEMBL2363032", BIG_GROUP, "MODULATOR", "PROTEIN COMPLEX GROUP")]),
    entry("MODCOPY", "Moduline copy", [dgidb_copy("CACNA1G", HGNC["CACNA1G"], "modulator")], chembl=False),
    # 5. an opposing signal on a direction-down need, as a record and as a copy
    entry("OPP", "Opposine", [chembl_row("CHEMBL2094124", NMDA_GROUP, "AGONIST", "PROTEIN COMPLEX GROUP")]),
    entry("OPPCOPY", "Opposine copy", [dgidb_copy("GRIN2A", HGNC["GRIN2A"], "agonist")], chembl=False),
    # 6. a salt record whose only mechanism is the 26-component group, with a documented CACNA1H measurement
    #    declared for its PARENT molecule (the identifier chain the catalogue holds)
    entry("CHEMBLDOCSALT", "Documine hydrochloride",
          [chembl_row("CHEMBL2363032", BIG_GROUP, "BLOCKER", "PROTEIN COMPLEX GROUP"),
           dgidb_copy("CACNA1H", HGNC["CACNA1H"], "blocker")], chembl="CHEMBLDOCSALT", parent="CAT:CHEMBLDOC"),
    entry("CHEMBLDOC", "Documine", [], chembl="CHEMBLDOC"),
    # 7. a DIFFERENT molecule on the same group record and the same gene: the waiver must not reach it
    entry("OTHERMOL", "Othermoline", [chembl_row("CHEMBL2363032", BIG_GROUP, "BLOCKER", "PROTEIN COMPLEX GROUP")]),
    # 8. a specific record checked against its own source's target id: untouched by any of this
    entry("GTO", "Gtopdbine", [gtopdb_row("CACNA1H", HGNC["CACNA1H"], "blocker")], chembl=False),
    # 9. THE TWO REAL VOCABULARY PAIRS. The two sources use different words for one assertion, and the
    #    first draft of assertion_key used the raw string, so a copy and its original got different keys
    #    and the copy was still counted as support. BLOCKER/blocker (used above) happens to match after
    #    upper-casing, which is exactly why the suite passed while the defect was live. These two do not.
    entry("VOCABDOWN", "Antagonine", [chembl_row("CHEMBL2094124", NMDA_GROUP, "ANTAGONIST", "PROTEIN COMPLEX GROUP"),
                                      dgidb_copy("GRIN2A", HGNC["GRIN2A"], "inhibitor")]),
    entry("VOCABUP", "Partialine", [chembl_row("CHEMBL2094124", NMDA_GROUP, "PARTIAL AGONIST", "PROTEIN COMPLEX GROUP"),
                                    dgidb_copy("GRIN2A", HGNC["GRIN2A"], "agonist")]),
]


def rc_module():
    """repurposing_coverage, imported on demand: the properties are about the search layer, and only the
    support-counting ones need the coverage layer."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import repurposing_coverage as rc
    return rc


def rows(need_, arte, roles=None):
    idx = rs.Index(ENTRIES, arte, MODULE)
    return {(a["catalogue_id"], a["target"]): a for a in rs.associations_for_need(need_, idx, roles if roles is not None else ROLES)["associations"]}


FULL = [REPUB, DOCD_RULE]
NO_RULES: list[dict] = []


class P1DuplicatedEvidence(unittest.TestCase):
    """A copy of a record is not a second support."""

    def test_a_copy_shares_the_assertion_key_of_the_record_it_copies(self):
        # the ChEMBL row and the DGIdb copy of it live on the SAME entry, so (id, target) names both:
        # read them from the association list rather than the keyed helper
        idx = rs.Index(ENTRIES, FULL, MODULE)
        got = [a for a in rs.associations_for_need(N_TTYPE, idx, ROLES)["associations"]
               if a["catalogue_id"] == "CAT:FAM" and a["target"] == "CACNA1G"]
        self.assertEqual(len(got), 2, "the record and its copy must BOTH stay listed")
        self.assertEqual(len({a["assertion_key"] for a in got}), 1, "record and copy are ONE assertion")
        self.assertEqual({a["consistency"] for a in got}, {"consistent"}, "a copy of a usable record stays usable")
        self.assertEqual(sorted(a["link_source"] for a in got), ["ChEMBL curated mechanism", "DGIdb interaction"])

    def test_a_copy_collapses_although_the_two_sources_use_different_words(self):
        """The real vocabulary pairs: ChEMBL ANTAGONIST / DGIdb `inhibitor` (18 rows on the real
        catalogue) and ChEMBL PARTIAL AGONIST / DGIdb `agonist` (3 rows). The key must be the action
        CLASS, not the raw string, or the copy is still counted as a second support. Measured
        2026-11-02: with a raw-string key all 21 resolved copies mismatched."""
        idx = rs.Index(ENTRIES, FULL, MODULE)
        assoc = rs.associations_for_need(N_NMDA, idx, ROLES)["associations"]
        for cid, expect in (("CAT:VOCABDOWN", "consistent"), ("CAT:VOCABUP", "opposed")):
            got = [a for a in assoc if a["catalogue_id"] == cid and a["target"] == "GRIN2A"]
            self.assertEqual(len(got), 2, cid)
            self.assertNotEqual(got[0]["action_raw"], got[1]["action_raw"], f"{cid}: the fixture must use DIFFERENT words")
            self.assertEqual({a["consistency"] for a in got}, {expect}, cid)
            self.assertEqual(len({a["assertion_key"] for a in got}), 1,
                             f"{cid}: record and copy are one assertion whatever each source calls the action")
            ctx = rc_module().action_contexts(got)
            self.assertEqual(len(ctx), 2, cid)
            self.assertEqual(rc_module().distinct_assertions(ctx), 1, cid)

    def test_two_different_molecules_on_one_group_record_are_two_assertions(self):
        """The record id alone is NOT the assertion: CHEMBL2363032 carries an action for many molecules."""
        idx = rs.Index(ENTRIES, FULL, MODULE)
        a = {x["catalogue_id"]: x for x in rs.associations_for_need(N_TTYPE, idx, ROLES)["associations"]
             if x["target"] == "CACNA1G" and x["link_source"].startswith("ChEMBL")}
        self.assertNotEqual(a["CAT:CHEMBLGRP"]["assertion_key"], a["CAT:OTHERMOL"]["assertion_key"])

    def test_an_unresolvable_copy_keeps_its_own_key_rather_than_claiming_to_be_a_copy_of_something(self):
        r = rows(N_TTYPE, FULL)
        grp = r[("CAT:CHEMBLGRP", "CACNA1G")]
        orphan = r[("CAT:GRPCOPY", "CACNA1G")]
        self.assertNotEqual(grp["assertion_key"], orphan["assertion_key"])
        self.assertIsNone(orphan["claim_provenance"]["original_record"])

    def test_the_coverage_layer_counts_assertions_not_rows(self):
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import repurposing_coverage as rc
        idx = rs.Index(ENTRIES, FULL, MODULE)
        cons = [a for a in rs.associations_for_need(N_TTYPE, idx, ROLES)["associations"]
                if a["catalogue_id"] == "CAT:FAM" and a["consistency"] == "consistent"]
        ctx = rc.action_contexts(cons)
        # CAT:FAM carries the family record on all 3 genes and ONE copy of it, on CACNA1G: 4 rows stay visible
        self.assertEqual(len(ctx), 4, "the record's 3 gene rows and the 1 copy all stay visible")
        self.assertEqual(rc.distinct_assertions(ctx), 3, "the copy is not a fourth assertion")
        self.assertEqual(sum(1 for c in ctx if c["republished_copy_of"] == "CHEMBL2362995"), 1)
        self.assertEqual(sum(1 for c in ctx if not c["adds_independent_support"]), 1)


class P2ImproperTransfer(unittest.TestCase):
    """No action, and no measurement, travels to a molecule or a target it was not made on."""

    def test_the_intermediary_route_is_closed(self):
        """The IT19 residual: the record abstains, the copy of it must not assert what the record cannot."""
        # NOTE: `rows()` is keyed (catalogue_id, target) and CAT:CHEMBLGRP carries BOTH the ChEMBL row and its
        # copy on CACNA1G, so the helper's value is the later of the two. Pick the ChEMBL row explicitly.
        idx = rs.Index(ENTRIES, NO_RULES, MODULE)
        before = [a for a in rs.associations_for_need(N_TTYPE, idx, ROLES)["associations"]
                  if a["catalogue_id"] == "CAT:CHEMBLGRP" and a["target"] == "CACNA1G"
                  and a["link_source"].startswith("ChEMBL")][0]
        self.assertEqual(before["consistency"], "direction_unresolved")      # the ChEMBL row, guarded since IT19
        orphan_before = rows(N_TTYPE, NO_RULES)[("CAT:GRPCOPY", "CACNA1G")]
        self.assertEqual(orphan_before["consistency"], "consistent")         # the residual, as it was
        after = rows(N_TTYPE, FULL)[("CAT:GRPCOPY", "CACNA1G")]
        self.assertEqual(after["consistency"], "direction_unresolved")
        self.assertEqual(after["abstention_class"], "republished_claim_level_not_carried")
        self.assertEqual(after["effective_target_level"], "unresolved")
        self.assertFalse(after["excluded_from_counts"], "the row stays in the listing")
        self.assertEqual(after["action_raw"], "blocker", "the source's own action is never rewritten")

    def test_a_resolved_copy_is_asked_exactly_what_the_record_is_asked(self):
        idx = rs.Index(ENTRIES, FULL, MODULE)
        got = [a for a in rs.associations_for_need(N_TTYPE, idx, ROLES)["associations"]
               if a["catalogue_id"] == "CAT:CHEMBLGRP" and a["target"] == "CACNA1G" and a["link_source"].startswith("DGIdb")][0]
        self.assertEqual(got["claim_provenance"]["original_record"], "CHEMBL2363032")
        self.assertEqual(got["claim_provenance"]["republished_record_level"], "protein_complex_group")
        self.assertEqual(got["consistency"], "direction_unresolved")
        self.assertEqual(got["abstention_class"], "group_record_mostly_outside_module_targets",
                         "the copy inherits the ORIGINAL record's abstention, not a new one")
        self.assertEqual((got["record_components"], got["components_in_module_targets"]), (len(BIG_GROUP), 3))

    def test_a_documented_measurement_is_specific_to_its_gene(self):
        r = rows(N_TTYPE, FULL)
        self.assertEqual(r[("CAT:CHEMBLDOCSALT", "CACNA1H")]["consistency"], "consistent")
        self.assertTrue(r[("CAT:CHEMBLDOCSALT", "CACNA1H")]["documented_level_waiver"])
        for sib in ("CACNA1G", "CACNA1I"):
            a = r[("CAT:CHEMBLDOCSALT", sib)]
            self.assertEqual(a["consistency"], "direction_unresolved", sib)
            self.assertEqual(a["abstention_class"], "group_record_mostly_outside_module_targets", sib)
            self.assertIsNone(a["documented_level_waiver"], sib)

    def test_a_documented_measurement_is_specific_to_its_molecule(self):
        a = rows(N_TTYPE, FULL)[("CAT:OTHERMOL", "CACNA1H")]
        self.assertEqual(a["consistency"], "direction_unresolved")
        self.assertIsNone(a["documented_level_waiver"], "another molecule on the same record gains nothing")

    def test_the_waiver_matches_through_the_declared_parent_and_only_through_an_identifier(self):
        self.assertEqual(rs.molecule_ids(next(e for e in ENTRIES if e["id"] == "CAT:CHEMBLDOCSALT"), {}),
                         {"CHEMBLDOCSALT", "CHEMBLDOC"})
        self.assertEqual(rs.molecule_ids(next(e for e in ENTRIES if e["id"] == "CAT:GRPCOPY"), {}), set())

    def test_a_group_level_document_is_refused_rather_than_accepted_as_a_subunit_waiver(self):
        bad = dict(DOCD_RULE, rule="target_level_documented:CHEMBLDOC:BLOCKER:protein_family")
        with self.assertRaises(ValueError):
            rows(N_TTYPE, [REPUB, bad])

    def test_a_malformed_documented_level_row_fails_whatever_gene_it_names(self):
        """The rule's shape is checked before its subject, so a bad row cannot sit unnoticed until it
        happens to name the gene under inspection."""
        for bad_rule in ("target_level_documented:CHEMBLDOC:BLOCKER",
                         "target_level_documented:CHEMBLDOC:BLOCKER:single_protein:extra",
                         "target_level_documented:CHEMBLDOC:MODULATOR:single_protein"):
            with self.assertRaises(ValueError, msg=bad_rule):
                rows(N_TTYPE, [REPUB, dict(DOCD_RULE, symbol="GRIN1", rule=bad_rule)])

    def test_a_waiver_does_not_reach_a_different_action(self):
        a = rows(N_TTYPE, [REPUB, dict(DOCD_RULE, rule="target_level_documented:CHEMBLDOC:ACTIVATOR:single_protein")])
        self.assertEqual(a[("CAT:CHEMBLDOCSALT", "CACNA1H")]["consistency"], "direction_unresolved")

    def test_records_written_at_the_modules_level_keep_their_direction(self):
        self.assertEqual(rows(N_TTYPE, FULL)[("CAT:FAM", "CACNA1G")]["consistency"], "consistent")
        self.assertEqual(rows(N_NMDA, FULL)[("CAT:NMDA", "GRIN2A")]["consistency"], "consistent")
        self.assertEqual(rows(N_NMDA, FULL)[("CAT:CPLX", "GRIN2B")]["consistency"], "consistent")
        self.assertEqual(rows(N_TTYPE, FULL)[("CAT:FAMCOPY", "CACNA1G")]["consistency"], "direction_unresolved",
                         "a copy with no resolvable original still carries no level, even of a legitimate record")

    def test_a_record_checked_against_its_own_sources_target_id_is_untouched(self):
        a = rows(N_TTYPE, FULL)[("CAT:GTO", "CACNA1H")]
        self.assertEqual(a["consistency"], "consistent")
        self.assertEqual(a["target_level"], "single_protein")
        self.assertIsNone(a["claim_provenance"], "a non-republished claim source has no republication datum")


class P3UnknownStaysUnknown(unittest.TestCase):
    """An abstention is not an exclusion, and an unstated action never gains a label or a new reason."""

    def test_an_unstated_action_keeps_the_sources_own_reason_in_record_and_in_copy(self):
        for arte in (NO_RULES, FULL):
            for cid in ("CAT:MOD", "CAT:MODCOPY"):
                a = rows(N_TTYPE, arte)[(cid, "CACNA1G")]
                self.assertEqual(a["consistency"], "direction_unresolved", cid)
                self.assertEqual(a["abstention_class"], "action_not_stated", cid)
                self.assertIn("no up/down action", a["consistency_why"], cid)

    def test_an_abstained_row_is_not_excluded_and_keeps_everything_a_reader_needs(self):
        a = rows(N_TTYPE, FULL)[("CAT:GRPCOPY", "CACNA1G")]
        self.assertFalse(a["excluded_from_counts"])
        self.assertIsNone(a["excluded_reason"])
        self.assertEqual(a["compound"], "Groupine copy")
        self.assertEqual(a["claim_source"], "ChEMBL")
        self.assertEqual(a["action_raw"], "blocker")
        self.assertTrue(a["action_stated"])
        self.assertTrue(any("republished claim" in l for l in a["limits"]))
        self.assertIn("not carried by the republishing export", a["consistency_why"])

    def test_every_new_reason_has_a_class_and_an_unknown_reason_still_fails_loudly(self):
        self.assertEqual(rs.abstention_class("direction_unresolved", "republished_claim_level_not_carried: x"),
                         "republished_claim_level_not_carried")
        self.assertIn("republished_claim_level_not_carried", rs.ABSTENTION_CLASSES)
        with self.assertRaises(ValueError):
            rs.abstention_class("direction_unresolved", "a reason no code path writes")

    def test_an_unresolved_wwox_coupling_is_not_decided_by_pharmacology(self):
        """The two judgments stay separate: a documented measurement at the target cannot supply the
        coupling between that target's activity and the need's quantity."""
        r = rows(N_NOROLE, FULL, roles={})
        a = r[("CAT:CHEMBLDOCSALT", "CACNA1H")]
        self.assertEqual(a["consistency"], "direction_unresolved")
        self.assertEqual(a["abstention_class"], "no_coupling_row")
        self.assertEqual(r[("CAT:FAM", "CACNA1G")]["consistency"], "direction_unresolved")
        self.assertEqual(r[("CAT:GTO", "CACNA1H")]["abstention_class"], "no_coupling_row")

    def test_an_opposing_signal_stays_visible_and_is_not_privileged(self):
        """The record keeps its `opposed` label; the copy with no resolvable original abstains exactly as a
        favourable copy would. No asymmetry is built in either direction."""
        self.assertEqual(rows(N_NMDA, FULL)[("CAT:OPP", "GRIN2A")]["consistency"], "opposed")
        copy = rows(N_NMDA, FULL)[("CAT:OPPCOPY", "GRIN2A")]
        self.assertEqual(rows(N_NMDA, NO_RULES)[("CAT:OPPCOPY", "GRIN2A")]["consistency"], "opposed")
        self.assertEqual(copy["consistency"], "direction_unresolved")
        self.assertEqual(copy["abstention_class"], "republished_claim_level_not_carried")
        self.assertEqual(copy["action_raw"], "agonist", "the unfavourable action is still readable on the row")

    def test_compound_to_needs_carries_the_same_three_properties(self):
        idx = rs.Index(ENTRIES, FULL, MODULE)
        for cid, target, expect, cls in (("CAT:GRPCOPY", "CACNA1G", "direction_unresolved", "republished_claim_level_not_carried"),
                                         ("CAT:FAM", "CACNA1G", "consistent", None),
                                         ("CAT:CHEMBLDOCSALT", "CACNA1H", "consistent", None),
                                         ("CAT:CHEMBLDOCSALT", "CACNA1G", "direction_unresolved", "group_record_mostly_outside_module_targets"),
                                         ("CAT:MODCOPY", "CACNA1G", "direction_unresolved", "action_not_stated")):
            e = next(x for x in ENTRIES if x["id"] == cid)
            got = {(x["need"], x["target"], x["link_source"]): x for x in rs.compound_to_needs(e, NEEDS, idx, ROLES, family=False)}
            key = next(k for k in got if k[0] == "N-TTYPE" and k[1] == target)
            self.assertEqual(got[key]["consistency"], expect, f"{cid} {target}")
            self.assertEqual(got[key]["abstention_class"], cls, f"{cid} {target}")


class P4CompatibleMatchIsNotIdentifiedOrigin(unittest.TestCase):
    """IT21 P1. A copy matched to ChEMBL by molecule id + gene + action class is a COMPATIBLE match. When two records are
    compatible, the descent is not identified and must not depend on the order the rows are listed in; when one is, it is kept
    and labelled as a compatible match; the direct ChEMBL evidence is never touched."""

    SINGLE = chembl_row("CHEMBLSP1", ["CACNA1G"], "BLOCKER", "SINGLE PROTEIN")
    GROUP = chembl_row("CHEMBL2363032", BIG_GROUP, "BLOCKER", "PROTEIN COMPLEX GROUP")
    COPY = dgidb_copy("CACNA1G", HGNC["CACNA1G"], "blocker")

    def prov_for(self, targets):
        e = entry("AMBIG", "Ambigine", targets)
        copy = next(t for t in e["targets"] if t["source"] == "DGIdb interaction")
        return rs.claim_provenance(e, copy, [REPUB])

    def test_two_compatible_records_leave_the_descent_unresolved_in_either_order(self):
        for order in ((self.SINGLE, self.GROUP), (self.GROUP, self.SINGLE)):
            p = self.prov_for([*order, dict(self.COPY)])
            self.assertIsNone(p["original_record"], "the first listed record must not be chosen")
            self.assertIsNone(p["duplicate_of_record"])
            self.assertEqual(p["republished_record_level"], "unresolved")
            self.assertEqual(p["origin_basis"], "ambiguous_compatible_matches")
            self.assertEqual(p["candidate_records"], ["CHEMBL2363032", "CHEMBLSP1"], "both candidates are named, sorted, order-free")
            self.assertIn("not identified", p["missing"])

    def test_an_ambiguous_copy_abstains_but_is_not_excluded_and_the_direct_rows_keep_their_direction(self):
        for order in ((self.SINGLE, self.GROUP), (self.GROUP, self.SINGLE)):
            idx = rs.Index([entry("AMBIG", "Ambigine", [*order, dict(self.COPY)])], FULL, MODULE)
            got = rs.associations_for_need(N_TTYPE, idx, ROLES)["associations"]
            copy = next(a for a in got if a["link_source"] == "DGIdb interaction")
            self.assertEqual(copy["consistency"], "direction_unresolved")
            self.assertEqual(copy["abstention_class"], "republished_claim_level_not_carried")
            self.assertFalse(copy["excluded_from_counts"])
            self.assertEqual(copy["action_raw"], "blocker", "an unresolved descent is not a negative")
            direct = next(a for a in got if a["link_source"] == "ChEMBL curated mechanism" and a["target"] == "CACNA1G"
                          and a.get("target_level") == "single_protein")
            self.assertEqual(direct["consistency"], "consistent", "valid direct evidence is kept")
            self.assertNotEqual(direct["assertion_key"], copy["assertion_key"], "an unresolved copy keeps its own key")

    def test_one_compatible_record_is_kept_and_labelled_a_compatible_match(self):
        p = self.prov_for([self.SINGLE, dict(self.COPY)])
        self.assertEqual(p["original_record"], "CHEMBLSP1")
        self.assertEqual(p["origin_basis"], "unique_compatible_match")
        self.assertEqual(p["republished_record_level"], "single_protein")
        p2 = self.prov_for([self.SINGLE, dict(self.SINGLE), dict(self.COPY)])
        self.assertEqual(p2["origin_basis"], "unique_compatible_match", "two rows of ONE record are one candidate")

    def test_no_compatible_record_is_stated_as_such(self):
        p = self.prov_for([chembl_row("CHEMBLSP1", ["CACNA1G"], "ACTIVATOR", "SINGLE PROTEIN"), dict(self.COPY)])
        self.assertEqual(p["origin_basis"], "no_compatible_record")
        self.assertIsNone(p["original_record"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
