#!/usr/bin/env python3
"""Tests of the provisional ranking (IT8 P9): rule, reproducibility, anti-inflation, missing data, counter-evidence, snapshots, agreement with the view,
and mutation tests that must FAIL the rule when an input is damaged. Offline; needs the module data and LEGEND_CATALOG_CACHE for the view tests.

  python3 -B disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/test_ranking_it8.py        (about 60 s)
"""
from __future__ import annotations

import copy
import csv
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ranking_it8 as rk  # noqa: E402

_CACHE: dict = {}


def state():
    if not _CACHE:
        ctx = rk.load_all()
        cat = rk.load_catalog()
        _CACHE.update(ctx=ctx, cat=cat, uni=rk.assemble(ctx, cat))
    return _CACHE


def by_id(uni, uid):
    return next(u for u in uni["units"] if u["unit_id"] == uid)


def unit_by_label(uni, frag):
    return next(u for u in uni["units"] if frag.lower() in u["label"].lower())


class SyntheticRule(unittest.TestCase):
    """view_assessment on hand-made units: every branch of the group rule, in both directions."""

    def mk(self, positions, flags=None, coherent=False, declared=("deep_recovery",), cells=None):
        needs = {f"NEED-{i}": {"goal": "deep_recovery", "short": f"n{i}"} for i in range(len(positions))}
        per_need = {f"NEED-{i}": {"position": p, "links": {}, "by_card": {"C": p}} for i, p in enumerate(positions)}
        pert = []
        for i, p in enumerate(positions):
            pert.append({"card_id": "C", "assertion_id": f"A{i}", "need_id": f"NEED-{i}", "evidence_kind": "readout_in_wwox_system", "sign": "benefit", "flags": ";".join(flags or [])})
        u = {"per_need": per_need, "declared_goals": list(declared), "pert": pert,
             "cells": ([{"need": f"NEED-{i}", "L2_mechanistic_coherence": {"state": "coherent"}} for i in range(len(positions))] if coherent else (cells or []))}
        return u, {"needs": needs}

    def grp(self, positions, **kw):
        u, ctx = self.mk(positions, **kw)
        return rk.view_assessment(u, ctx, "broad")

    def test_every_branch(self):
        self.assertEqual(self.grp(["F1"])["group"], "G1")
        self.assertEqual(self.grp(["F2"])["group"], "G2a")
        self.assertEqual(self.grp(["F2"], flags=["nonspecific_also_in_wild_type"])["group"], "G2b")
        self.assertEqual(self.grp(["F2"], flags=["tool_compound_d-APV"])["group"], "G2b")
        self.assertEqual(self.grp(["F2"], flags=["no_drug_by_genotype_test"])["group"], "G2b")
        self.assertEqual(self.grp(["F2"], flags=["control_variability_comparable_to_effect"])["group"], "G2b")
        self.assertEqual(self.grp(["F2"], flags=["graphical_reading"])["group"], "G2a")
        self.assertEqual(self.grp(["C2"])["group"], "G3")
        self.assertEqual(self.grp(["C1"])["group"], "G3")
        self.assertEqual(self.grp(["F3"], coherent=True)["group"], "G4a")
        self.assertEqual(self.grp(["F3"], coherent=False)["group"], "G4b")
        self.assertEqual(self.grp(["C3"])["group"], "G5")
        self.assertEqual(self.grp(["P3"])["group"], "G5")
        self.assertEqual(self.grp(["P1"])["group"], "GU")
        self.assertEqual(self.grp(["P1", "P2"])["group"], "GU")

    def test_lead_is_the_best_position_and_counter_evidence_is_kept(self):
        a = self.grp(["F2", "C2"])
        self.assertEqual((a["group"], a["contested"]), ("G2a", True))
        self.assertEqual(len(a["counter_needs"]), 1)
        self.assertEqual(self.grp(["C2", "F3"])["group"], "G3")     # WWOX-system evidence, even contested, outranks a target hypothesis
        self.assertEqual(self.grp(["F3", "C3"])["lead"], "F3")
        self.assertTrue(self.grp(["F3", "C3"])["contested"])

    def test_more_needs_never_raise_the_group(self):
        self.assertEqual(self.grp(["F3"])["group"], self.grp(["F3", "F3", "F3", "F3"])["group"])
        self.assertEqual(self.grp(["P3"])["group"], self.grp(["P3"] * 6)["group"])

    def test_merge_order_never_hides_a_counter_position(self):
        mo = rk.MERGE_ORDER
        self.assertLess(mo.index("C3"), mo.index("F3"))
        self.assertLess(mo.index("C2"), mo.index("F3"))
        self.assertLess(mo.index("F2"), mo.index("C2"))
        self.assertEqual(min(["F3", "C3"], key=mo.index), "C3")

    def test_declared_objective_without_position_is_unorderable_not_negative(self):
        u, ctx = self.mk([])
        va = rk.view_assessment(u, ctx, "broad")
        self.assertEqual((va["member"], va["group"]), (True, "GU"))
        va2 = rk.view_assessment(u, ctx, "partial")
        self.assertFalse(va2["member"])

    def test_group_order_places_unorderable_last_without_a_verdict(self):
        self.assertEqual(rk.GROUP_ORDER[-1], "GU")
        self.assertNotIn("GU", rk.IN_SELECTION)
        self.assertNotIn("G4b", rk.IN_SELECTION)
        self.assertIn("not a finding", rk.GROUPS["GU"][2].lower())

    def test_display_key_collapses_salts_and_case(self):
        k = rk.display_group_key
        self.assertEqual(k("Memantine Hydrochloride"), k("MEMANTINE"))
        self.assertEqual(k("Acamprosate Calcium"), k("ACAMPROSATE"))
        self.assertEqual(k("EVT-101 FREE BASE"), k("Evt-101"))
        self.assertNotEqual(k("Ketamine"), k("Esketamine"))     # stereoisomers are pharmacologically different and are not merged by this display key


class NextPriorityRule(unittest.TestCase):
    def va(self, lead, group, question="a named discriminating step", kind="verificare un'ipotesi", feas="Animal work; access not known"):
        return {"lead": lead, "group": group, "next": {"question": question, "kind": kind, "feasibility": feas}}

    def test_levels_follow_the_decision_at_stake(self):
        self.assertEqual(rk.next_priority(self.va("F2", "G2b"))["level"], "NX1")
        self.assertEqual(rk.next_priority(self.va("C2", "G3"))["level"], "NX1")
        self.assertEqual(rk.next_priority(self.va("F3", "G4a"))["level"], "NX1")
        self.assertEqual(rk.next_priority(self.va("F3", "G4b"))["level"], "NX2")
        self.assertEqual(rk.next_priority(self.va("F1", "G1"))["level"], "NX2")
        self.assertEqual(rk.next_priority(self.va("P3", "G5"))["level"], "NX3")
        self.assertEqual(rk.next_priority(self.va(None, "GU", kind="risolvere una premessa"))["level"], "NX2")
        self.assertEqual(rk.next_priority(self.va(None, "GU", kind="verificare un'ipotesi"))["level"], "NX3")

    def test_no_named_step_is_low_and_cost_never_moves_the_level(self):
        self.assertEqual(rk.next_priority(self.va("F2", "G2b", question=""))["level"], "NX3")
        a = rk.next_priority(self.va("F2", "G2b", feas="Slice electrophysiology; line held"))
        b = rk.next_priority(self.va("F2", "G2b", feas="Animal work; access not known; none known"))
        self.assertEqual(a["level"], b["level"])
        self.assertNotEqual(a["feasibility_flags"], b["feasibility_flags"])
        self.assertIn("access_or_material_not_known", b["feasibility_flags"])

    def test_the_rule_reads_no_publication_count(self):
        import inspect
        src = inspect.getsource(rk.next_priority)
        for w in ("pmids", "receipts", "n_pmid", "count"):
            self.assertNotIn(w, src)


class RealData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.S = state()
        cls.uni = cls.S["uni"]

    def test_units_cover_cards_exactly_once(self):
        cards = [c for u in self.uni["units"] for c in u["cards"]]
        self.assertEqual(sorted(cards), sorted(self.S["ctx"]["cands"]))
        self.assertEqual(len(cards), len(set(cards)))

    def test_mutation_unit_map_missing_a_card_is_refused(self):
        ctx = copy.deepcopy(self.S["ctx"])
        ctx["unit_map"] = [r for r in ctx["unit_map"] if r["unit_id"] != "U17"]
        with self.assertRaises(SystemExit):
            rk.build_units(ctx, self.S["cat"])
        ctx = copy.deepcopy(self.S["ctx"])
        ctx["unit_map"] = ctx["unit_map"] + [dict(ctx["unit_map"][0], unit_id="U99")]
        with self.assertRaises(SystemExit):
            rk.build_units(ctx, self.S["cat"])

    def test_classes_partition_the_units(self):
        cls = {u["class"] for u in self.uni["units"]}
        self.assertLessEqual(cls, set(rk.CLASSES))
        for u in self.uni["units"]:
            if u["class"] == "INSUFF":
                self.assertTrue(all(c in u["abstention_cards"] for c in u["cards"]) or all(p["position"] in ("P1", "P2") for p in u["pathways"]), u["unit_id"])
            if u["class"] == "ORD":
                self.assertTrue(any(p["position"] in ("F1", "F2", "F3") for p in u["pathways"]), u["unit_id"])
            if u["class"] == "WEAK":
                self.assertFalse(any(p["position"] in ("F1", "F2", "F3") for p in u["pathways"]), u["unit_id"])
        self.assertEqual({u["unit_id"] for u in self.uni["units"] if u["class"] == "EXCL" and u["kind"] != "it9_proposal"}, {"X01", "X02", "X03"})

    def test_insufficient_is_not_at_the_bottom_and_names_the_missing_datum(self):
        for u in self.uni["units"]:
            if u["class"] == "INSUFF":
                for v in u["views"].values():
                    if v.get("member"):
                        self.assertEqual(v["group"], "GU")
                self.assertIn("not placed at the bottom", u["class_reason"])

    def test_known_positions_are_reproduced(self):
        self.assertEqual(unit_by_label(self.uni, "AAV9")["views"]["broad"]["group"], "G1")
        self.assertEqual(unit_by_label(self.uni, "AAV9")["views"]["partial"]["group"], "G3")      # the same intervention sits differently by objective
        self.assertEqual(unit_by_label(self.uni, "Ethosuximide")["views"]["partial"]["group"], "G2b")     # not having tested specificity is an unknown, never clean
        self.assertEqual(unit_by_label(self.uni, "Ethosuximide")["views"]["partial"]["group"], unit_by_label(self.uni, "Lithium")["views"]["partial"]["group"])
        self.assertEqual(unit_by_label(self.uni, "Lithium")["views"]["partial"]["group"], "G2b")     # nonspecific: also acts in wild type
        self.assertEqual(unit_by_label(self.uni, "NMDAR")["views"]["partial"]["group"], "G2b")        # the WWOX readout is a tool compound
        self.assertEqual(unit_by_label(self.uni, "Ketogenic")["views"]["partial"]["group"], "G3")
        self.assertEqual(unit_by_label(self.uni, "Vigabatrin")["views"]["partial"]["group"], "G3")

    def test_counter_evidence_and_opposed_positions_are_preserved(self):
        v = unit_by_label(self.uni, "Vigabatrin")
        pw = {p["need"]: p for p in v["pathways"]}
        self.assertEqual(pw["NEED-SEIZURE-CONTROL-SYMPTOMATIC"]["position"], "C2")                  # H02's F3 does not hide the case-report nulls
        self.assertTrue(pw["NEED-SEIZURE-CONTROL-SYMPTOMATIC"]["same_need_conflict"])
        self.assertEqual(pw["NEED-MYELINATION"]["position"], "C3")                                   # the harm signal is kept
        d = unit_by_label(self.uni, "Dichloroacetate")
        self.assertEqual({p["need"]: p["position"] for p in d["pathways"]}["NEED-PDH-PYRUVATE-AXIS"], "C3")
        self.assertTrue(d["views"]["partial"]["contested"])
        opp = [u["unit_id"] for u in self.uni["units"] if u["components"]["M_mechanism"]["opposed_needs"]]
        self.assertTrue(all(isinstance(x, str) for x in opp))

    def test_missing_data_are_unknown_not_zero(self):
        for u in self.uni["units"]:
            if u["class"] == "EXCL":
                continue
            p = u["components"]["P_pharmacology"]
            self.assertIn("UNKNOWN", p["state"] + p["potency_with_assay_context"] + p["human_exposure"], u["unit_id"])
            self.assertTrue(u["components"]["U_uncertainty"]["unknown"], u["unit_id"])
        sp = unit_by_label(self.uni, "Splice-correcting")
        self.assertIn("none", sp["components"]["W_wwox_evidence"]["text"])
        self.assertEqual(sp["views"]["broad"]["group"], "GU")

    def test_g1_requires_f1_and_selection_is_bounded(self):
        sel = rk.build_selections(self.uni)
        for view, s in sel.items():
            self.assertLessEqual(len(s["top"]), 10)
            for uid, g in s["top_groups"].items():
                self.assertIn(g, rk.IN_SELECTION)
            self.assertFalse(set(s["top"]) & {a["unit_id"] for a in s["not_in_top_listed_apart"]})
        for u in self.uni["units"]:
            for v in u["views"].values():
                if v.get("member") and v.get("group") == "G1":
                    self.assertEqual(v["lead"], "F1")

    def test_a_family_duplicate_does_not_inflate_a_position(self):
        """Name twins and salts: duplicating a member family of a unit (a name twin with the same cells) changes no group."""
        ctx = copy.deepcopy(self.S["ctx"])
        rows = ctx["matrix"]["rows"]
        cells = ctx["matrix"]["cells"]
        add_r, add_c = [], []
        for r in rows:
            if r["kind"] == "molecule_family" and r.get("cards"):
                t = copy.deepcopy(r)
                t["row_id"] = r["row_id"] + ":TWIN"
                t["name"] = r["name"].title()
                add_r.append(t)
                for c in cells:
                    if c["row_id"] == r["row_id"]:
                        c2 = copy.deepcopy(c)
                        c2["row_id"] = t["row_id"]
                        add_c.append(c2)
        rows.extend(add_r)
        cells.extend(add_c)
        uni2 = rk.assemble(ctx, self.S["cat"])
        g = lambda uni: [(u["unit_id"], u["class"], u["views"]["broad"].get("group"), u["views"]["partial"].get("group")) for u in uni["units"]]
        self.assertEqual(g(self.uni), g(uni2))
        self.assertEqual(rk.build_selections(self.uni)["general"]["top"], rk.build_selections(uni2)["general"]["top"])

    def test_mutation_a_damaged_position_moves_the_group(self):
        ctx = copy.deepcopy(self.S["ctx"])
        etx = ctx["cands"]["EB-ETX-01"]
        for lk in etx["links"].values():
            lk["group"] = "C2"
        u2 = rk.assemble(ctx, self.S["cat"])
        self.assertEqual(unit_by_label(u2, "Ethosuximide")["views"]["partial"]["group"], "G3")
        # removing the specificity flags (an actual wild-type / drug-by-genotype test would clear them) is the only way to G2a
        ctx = copy.deepcopy(self.S["ctx"])
        for r in ctx["pert"]:
            if r["card_id"] == "EB-ETX-01":
                r["flags"] = ";".join(f for f in r["flags"].split(";") if not rk.is_spec_flag(f))
        u3 = rk.assemble(ctx, self.S["cat"])
        self.assertEqual(unit_by_label(u3, "Ethosuximide")["views"]["partial"]["group"], "G2a")
        ctx = copy.deepcopy(self.S["ctx"])
        for lk in ctx["cands"]["C04_aav9_endpoint_families"]["links"].values():
            if lk["group"] == "F1":
                lk["group"] = "F2"
        for lk in ctx["cands"]["C01_aav9_wwox"]["links"].values():
            lk["group"] = "F2"
        u4 = rk.assemble(ctx, self.S["cat"])
        self.assertEqual(unit_by_label(u4, "AAV9")["views"]["broad"]["group"], "G2a")

    def test_mutation_inputs_digest_changes_with_the_input(self):
        ctx = copy.deepcopy(self.S["ctx"])
        for r in ctx["pert"]:
            if r["card_id"] == "EB-ETX-01":
                r["sign"] = "null"
        u2 = rk.assemble(ctx, self.S["cat"])
        a, b = unit_by_label(self.uni, "Ethosuximide")["inputs"], unit_by_label(u2, "Ethosuximide")["inputs"]
        self.assertNotEqual(a["T2_pertinence"], b["T2_pertinence"])
        self.assertEqual(a["T5_pharmacology"], b["T5_pharmacology"])
        o, p = unit_by_label(self.uni, "Lithium")["inputs"], unit_by_label(u2, "Lithium")["inputs"]
        self.assertEqual(o, p)       # unrelated units are untouched

    def test_caveats_reach_the_selected_items(self):
        sel = {r["unit_id"]: r for r in rk.build_all_rows()} if hasattr(rk, "build_all_rows") else {}
        a = unit_by_label(self.uni, "Apinocaltamide")["views"]["partial"]
        self.assertIn("T-type mediation is NOT measured", a["main_limit"])
        self.assertIn("ethosuximide result", a["main_limit"])
        aav = unit_by_label(self.uni, "AAV9")["views"]["broad"]
        self.assertTrue(any("52 versus about 26" in t for t in aav["counter_statements"]))
        self.assertIn("audit_repair_not_rejudged", aav["main_limit"])
        self.assertIn("prevention", aav["objective_note"])
        self.assertIn("test coverage", aav["view_note"])
        self.assertNotIn("moves the position to a counter-evidence group (C1/C2) by rule", aav["triggers"]["fall"])
        v = {p["need"]: p for p in unit_by_label(self.uni, "Vigabatrin")["pathways"]}
        self.assertEqual(v["NEED-MYELINATION"]["link_evidence"], "other_disease_precedent_plus_wwox_case_level_signal")
        n = unit_by_label(self.uni, "d-APV")["views"]["partial"]
        self.assertIn("carbenoxolone", n["main_limit"])
        self.assertIn("no WWOX data", n["main_limit"])
        self.assertIn("GSK3beta/IMPase", unit_by_label(self.uni, "Lithium")["views"]["partial"]["triggers"]["rise"])

    def test_type_and_origin_are_present_and_valid_for_every_unit(self):
        for u in self.uni["units"]:
            self.assertIn(u["unit_type"], rk.UNIT_TYPES)
            self.assertIn(u["origin"], rk.ORIGINS)
        self.assertEqual(unit_by_label(self.uni, "AAV9")["unit_type"], "gene_therapy")
        self.assertEqual(unit_by_label(self.uni, "Ketogenic")["unit_type"], "diet")
        self.assertEqual(unit_by_label(self.uni, "Ethosuximide")["unit_type"], "molecule")
        self.assertEqual(unit_by_label(self.uni, "d-APV")["unit_type"], "tool_compound_and_class")
        self.assertEqual({u["origin"] for u in self.uni["units"] if u["cards"] and u["unit_id"] not in ("U28", "U59", "U63")}, {"known_track_before_it9"})      # U63: the IT11 card unit (M01)
        self.assertEqual({u["origin"] for u in self.uni["units"] if u["unit_id"] in ("U28", "U29")}, {"generated_in_it9"})
        self.assertEqual(by_id(self.uni, "U59")["origin"], "generated_in_it10")       # the NRF2 card unit (IT10 P2.2): a mechanism probe generated in IT10

    def test_mutation_missing_or_invalid_type_or_origin_is_refused(self):
        for col, val in (("origin", ""), ("origin", "invented"), ("unit_type", ""), ("unit_type", "invented")):
            ctx = copy.deepcopy(self.S["ctx"])
            ctx["unit_map"][3][col] = val
            with self.assertRaises(SystemExit):
                rk.build_units(ctx, self.S["cat"])

    def test_member_evidence_never_credits_a_member_with_another_members_result(self):
        mem = {m["member"]: m for m in by_id(self.uni, "U21")["member_evidence"]}
        for name in ("Memantine", "Perampanel", "Radiprodil", "Selfotel"):
            self.assertEqual(mem[name]["tested_in_wwox_system"], "no", name)
        tool = next(m for m in mem.values() if m["member_type"] == "tool_compound")
        self.assertEqual(tool["tested_in_wwox_system"], "yes")
        self.assertIn("d-APV", tool["member"])
        note = by_id(self.uni, "U21")["evidence_level_note"]
        self.assertIn("MECHANISM only", note["of_mechanism_or_class"])
        self.assertIn("Memantine", note["untested_members"])
        v = {m["member"]: m for m in by_id(self.uni, "U20")["member_evidence"]}
        self.assertEqual(v["Vigabatrin"]["tested_in_wwox_system"], "yes")
        self.assertEqual(v["Cpp-115 Free Base"]["tested_in_wwox_system"], "no")      # vigabatrin data are not data of the other GABA-AT inactivators

    def test_mutation_a_misattributed_row_is_detected(self):
        ctx = copy.deepcopy(self.S["ctx"])
        for r in ctx["pert"]:
            if r["assertion_id"] == "DR-W2-001":
                r["subject"] = "CHEMBL807"          # the d-APV burst result attributed to memantine
        u2 = rk.assemble(ctx, self.S["cat"])
        mem = {m["member"]: m for m in by_id(u2, "U21")["member_evidence"]}
        self.assertEqual(mem["Memantine"]["tested_in_wwox_system"], "yes")               # the table follows the attribution ...
        self.assertNotEqual(mem["Memantine"]["tested_in_wwox_system"], {m["member"]: m for m in by_id(self.uni, "U21")["member_evidence"]}["Memantine"]["tested_in_wwox_system"])   # ... and differs from the frozen reading
        # a hand-edited table that credits an assertion twice, or to a member that does not own it, fails the validator
        unit = rk.build_units(self.S["ctx"], self.S["cat"])
        u21 = next(u for u in unit if u["unit_id"] == "U21")
        table = copy.deepcopy(rk.member_evidence(u21))
        self.assertEqual(rk.validate_attribution(u21, table), [])
        tool = next(m for m in table if m["member_type"] == "tool_compound")
        mem2 = next(m for m in table if m["member"] == "Memantine")
        mem2["assertion_ids"] = list(tool["assertion_ids"])
        mem2["tested_in_wwox_system"] = "yes"
        self.assertTrue(rk.validate_attribution(u21, table))

    def test_three_fields_are_separate_and_groups_did_not_move(self):
        for u in self.uni["units"]:
            for v in u["views"].values():
                if v.get("member"):
                    self.assertIn(v["next_priority"]["level"], rk.NX_LEVELS)
        before = {"U07": "G1", "U17": "G2b", "U24": "G2b", "U21": "G2b", "U10": "G3", "U15": "G3", "U20": "G3", "U25": "G4a"}
        got = {k: min(((rk.GROUP_ORDER.index(v["group"]), v["group"]) for v in by_id(self.uni, k)["views"].values() if v.get("member")))[1] for k in before}
        self.assertEqual(got, before)

    def test_it9_candidates_enter_by_the_documented_rule(self):
        qual = rk.load_qualification()
        self.assertEqual(len(qual), 32)
        self.assertEqual({q["state"] for q in qual.values()}, {"KEEP", "INCONCLUSIVE", "DROP", "REFERENCE"})
        pm = rk.read_tsv(rk.HERE / "proposals_map.tsv")
        self.assertEqual({r["cand_id"] for r in pm}, set(qual) - {"E-01"})        # E-01 (PX-478) is the card K01
        units = {u["unit_id"]: u for u in self.uni["units"]}
        for r in pm:
            u = units[r["unit_id"]]
            st = qual[r["cand_id"]]["state"]
            self.assertEqual(u["class"], rk.STATE_CLASS[st], r["cand_id"])
            self.assertEqual(u["origin"], r["origin"])
            v = u["views"]["partial"]
            if st == "KEEP":
                self.assertEqual((v["group"], v["lead"]), ("G4b", "F3"), r["cand_id"])
            elif st == "INCONCLUSIVE":
                self.assertEqual(v["group"], "GU", r["cand_id"])
            else:
                self.assertFalse(v.get("member"), r["cand_id"])
                self.assertTrue(u["class_reason"])
            if st == "REFERENCE":
                self.assertEqual(u["origin"], "reference_or_control")
        k = units["U28"]
        self.assertEqual((k["unit_type"], k["origin"], k["views"]["partial"]["group"]), ("mechanism_probe", "generated_in_it9", "G4b"))
        self.assertEqual(len({r["unit_id"] for r in self.uni["it9_records"]}), 31)
        self.assertEqual(len(self.uni["it9_records"]), 32)

    def test_no_existing_group_moved_and_selections_unchanged(self):
        snap = rk.jload(rk.HERE / "snapshots" / "units_2026-10-30_ba74e7d9792ea776.json")
        for uid, old in snap["units"].items():
            u = by_id(self.uni, uid)
            self.assertEqual((u["views"]["broad"].get("group", "-"), u["views"]["partial"].get("group", "-"), u["class"]), (old["broad"], old["partial"], old["class"]), uid)
        sel = rk.build_selections(self.uni)
        self.assertEqual(sel["general"]["top"], ["U07", "U17", "U24", "U21", "U10", "U15", "U20", "U25"])
        for u in self.uni["units"]:
            if u["origin"] != "known_track_before_it9":
                for v in u["views"].values():
                    self.assertNotIn(v.get("group"), rk.IN_SELECTION[:4])          # a generated proposal is never selectable without a WWOX-system result

    def test_mutation_candidate_state_and_coverage(self):
        import unittest.mock as mock
        qual = rk.load_qualification()
        ctx = self.S["ctx"]
        gone = {k: v for k, v in qual.items() if k != "P3-08"}
        with mock.patch.object(rk, "load_qualification", return_value=gone):
            with self.assertRaises(SystemExit):
                rk.proposal_units(ctx)
        flipped = {k: dict(v, state="DROP") if k == "P3-08" else v for k, v in qual.items()}
        with mock.patch.object(rk, "load_qualification", return_value=flipped):
            units, _ = rk.proposal_units(ctx)
        self.assertEqual(next(u for u in units if u["unit_id"] == "U29")["class"], "EXCL")
        flipped = {k: dict(v, state="KEEP") if k == "P3-03" else v for k, v in qual.items()}
        with mock.patch.object(rk, "load_qualification", return_value=flipped):
            units, _ = rk.proposal_units(ctx)
        self.assertEqual(next(u for u in units if u["unit_id"] == "U32")["views"]["partial"]["group"], "G4b")      # belzutifan would be ordered only if its state changed

    def test_inventory_counts_reconcile(self):
        inv, summ = rk.inventory(self.S["ctx"], self.S["cat"], self.uni)
        self.assertEqual(sum(summ["by_first_order"].values()), summ["families"])
        self.assertEqual(summ["families"], 40268)
        self.assertEqual(summ["records"], 44211)
        self.assertEqual(len(inv), summ["families"])
        self.assertEqual(len({r["family_id"] for r in inv}), len(inv))
        self.assertLessEqual(summ["distinct_display_names_total"], summ["families"])
        for r in inv:
            if r["first_order"] == "UNIT":
                self.assertTrue(r["units"])
            else:
                self.assertFalse(r["units"], r["family_id"])
        # a database-only family is insufficiently evaluated by definition, never evaluated
        self.assertTrue(all(r["class"] in ("INSUFF", "EXCL") or r["class"].startswith("UNIT") for r in inv))


class Reproducible(unittest.TestCase):
    def test_regeneration_is_byte_identical_to_the_committed_files(self):
        files = rk.build_all()
        for name, data in files.items():
            self.assertTrue((HERE / name).exists(), name)
            self.assertEqual((HERE / name).read_bytes(), data, f"{name} differs from a fresh regeneration")
        self.assertEqual(files["ranking.json"], rk.build_all()["ranking.json"])


class Snapshots(unittest.TestCase):
    def run_cmd(self, fn, **kw):
        buf, err = io.StringIO(), io.StringIO()
        with redirect_stdout(buf), redirect_stderr(err):
            code = fn(type("A", (), kw)())
        return code, buf.getvalue(), err.getvalue()

    def test_snapshot_is_idempotent_and_demands_a_reason_for_a_move(self):
        files = rk.build_all()
        orig_build, orig_here = rk.build_all, rk.HERE
        with tempfile.TemporaryDirectory() as td:
            rk.HERE = Path(td)
            rk.build_all = lambda: files
            try:
                code, out, _ = self.run_cmd(rk.cmd_snapshot, reason="", note="")
                self.assertEqual(code, 0)
                n1 = sorted(p.name for p in (Path(td) / "snapshots").glob("*"))
                code, out, _ = self.run_cmd(rk.cmd_snapshot, reason="", note="")
                self.assertIn("nothing changed", out)
                self.assertEqual(n1, sorted(p.name for p in (Path(td) / "snapshots").glob("*")))
                ch = (Path(td) / "changes.tsv").read_text(encoding="utf-8").splitlines()
                self.assertTrue(all(l.split("\t")[4] == "new_entry" for l in ch[1:]))
                # damage one group
                j = json.loads(files["ranking.json"])
                for u in j["units"]:
                    if u["label"].startswith("Ethosuximide"):
                        u["views"]["partial"]["group"] = "G3"
                files2 = dict(files)
                files2["ranking.json"] = (json.dumps(j, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")
                rk.build_all = lambda: files2
                code, out, err = self.run_cmd(rk.cmd_snapshot, reason="", note="")
                self.assertEqual(code, 2)
                self.assertIn("--reason", err)
                code, out, err = self.run_cmd(rk.cmd_snapshot, reason="counter_evidence", note="test")
                self.assertEqual(code, 0)
                last = (Path(td) / "changes.tsv").read_text(encoding="utf-8").splitlines()[-1].split("\t")
                self.assertEqual((last[2], last[3], last[4]), ("group_moved", "assessment_change", "counter_evidence"))
            finally:
                rk.build_all, rk.HERE = orig_build, orig_here

    def test_unchanged_inputs_give_unchanged_state(self):
        files = rk.build_all()
        cur = rk.current_state(files)
        self.assertEqual(rk.compare(cur, cur), [])


class WithTheView(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import repurposing_view as rv
        cls.rv = rv
        cls.P = rv.build_payload(rv.DEFAULT_DR, "full")
        cls.Ps = rv.build_payload(rv.DEFAULT_DR, "shareable")
        cls.J = json.loads((HERE / "ranking.json").read_text(encoding="utf-8"))

    def test_view_and_generated_data_agree(self):
        R = self.P["cur"]["ranking"]
        J = self.J
        self.assertEqual({u["id"]: (u["class"], u["views"]["broad"].get("group"), u["views"]["partial"].get("group")) for u in R["units"]},
                         {u["unit_id"]: (u["class"], u["views"]["broad"].get("group"), u["views"]["partial"].get("group")) for u in J["units"]})
        for v in ("general", "broad", "partial"):
            self.assertEqual(R["selections"][v]["top"], J["summary"]["selections"][v]["top"])
        self.assertEqual(R["meta"]["order_digest"], J["summary"]["order_digest"])
        html = self.rv.render(self.P)
        for v in ("general", "broad", "partial"):
            self.assertIn(f'data-k="rk.top.{v}" data-v="{len(R["selections"][v]["top"])}"', html)
        for u in R["units"]:
            self.assertEqual(html.count(f'class="rk-row" data-unit="{u["id"]}"'), 1, u["id"])

    def test_every_listed_item_has_a_reconstructible_reason(self):
        for v, s in self.P["cur"]["ranking"]["selections"].items():
            for uid in s["top"]:
                u = next(x for x in self.P["cur"]["ranking"]["units"] if x["id"] == uid)
                va = u["views"][s["objective"][uid]]
                for k in ("group", "lead", "lead_need", "evidence", "next", "triggers", "main_limit"):
                    self.assertTrue(va.get(k), (uid, k))
                self.assertTrue(va["triggers"]["rise"] and va["triggers"]["fall"] and va["triggers"]["leave"])
                # the lead position is the card's own position on that need (re-derivable with repurposing_view.py positions)
                got = {p["need"]: p["position"] for p in u["pathways"]}[va["lead_need"]]
                self.assertEqual(got, va["lead"])
                cands = {c["id"]: c for c in self.P["cur"]["cands"]}
                self.assertIn(va["lead"], [cands[c]["links"][va["lead_need"]]["group"] for c in u["cards"] if va["lead_need"] in cands[c]["links"]])

    def test_shareable_edition_carries_no_catalogue_member_and_only_class_a_access(self):
        R = self.Ps["cur"]["ranking"]
        for u in R["units"]:
            self.assertIsInstance(u["members"], int)
            self.assertNotIn("potency_with_assay_context", u["comp"]["P"])
            self.assertNotIn("ChEMBL", u["access"].replace("(licence class B/C)", ""))
            self.assertNotIn("DSLD", u["access"])
        self.assertNotIn("deepening", json.dumps(R).lower())

    def test_italian_orientation_is_complete(self):
        U = self.rv.UI_IT
        html = self.rv.render(self.P)
        sec = html[html.index('id="ranking"'):html.index('id="rankingprint"')]
        for must in ("Graduatoria provvisoria", "non è consiglio medico", "Gruppi di priorità", "Elenco completo", "Evoluzione"):
            self.assertIn(must, sec)
        for k in ("rk_btn_tsv", "rk_btn_json", "rk_btn_print1", "rk_count", "nav_ranking"):
            self.assertTrue(U[k].strip())


class LatestSnapshotOrder(unittest.TestCase):
    def test_latest_follows_append_order_not_the_hash_in_the_name(self):
        with tempfile.TemporaryDirectory() as td:
            from pathlib import Path
            here = Path(td)
            (here / "snapshots").mkdir()
            for sid in ("units_2026-10-30_6361aaaa", "units_2026-10-30_35d7bbbb"):
                (here / "snapshots" / (sid + ".json")).write_text(json.dumps({"id": sid}), encoding="utf-8")
            (here / "changes.tsv").write_text("snapshot\tunit_id\nunits_2026-10-30_6361aaaa\tU01\nunits_2026-10-30_35d7bbbb\tU01\n", encoding="utf-8")
            old = rk.HERE
            rk.HERE = here
            try:
                path, data = rk.latest_snapshot()
            finally:
                rk.HERE = old
            self.assertEqual(data["id"], "units_2026-10-30_35d7bbbb")


class MatchingV3Fixtures(unittest.TestCase):
    """Concrete cases through the existing attribution, ranking and view functions."""

    @staticmethod
    def fixture(name):
        return json.loads((HERE / "fixtures" / (name + ".json")).read_text())

    def raw_unit(self, uid):
        s = state()
        return copy.deepcopy(next(u for u in rk.build_units(s["ctx"], s["cat"]) if u["unit_id"] == uid))

    def test_duplicate_evidence_does_not_inflate_evaluation(self):
        f = self.fixture("duplicate_evidence")
        u = self.raw_unit(f["unit_id"])
        before = rk.member_evidence(u)
        comp = rk.component_wwox(u)
        groups = [rk.view_assessment(u, state()["ctx"], obj) for obj in rk.OBJECTIVES]
        row = next(r for r in u["pert"] if r["assertion_id"] == f["assertion_id"])
        u["pert"].append(dict(row, access_route=f["duplicate_access_route"]))
        self.assertEqual(rk.member_evidence(u), before)
        self.assertEqual(rk.component_wwox(u), comp)
        self.assertEqual([rk.view_assessment(u, state()["ctx"], obj) for obj in rk.OBJECTIVES], groups)
        member = next(m for m in before if m["member_key"] == f["expected_member"])
        self.assertEqual(member["assertion_ids"].count(f["assertion_id"]), 1)

    def test_dapv_evidence_does_not_become_memantine_evidence(self):
        f = self.fixture("no_molecule_transfer")
        u = self.raw_unit(f["unit_id"])
        table = rk.member_evidence(u)
        by = {m["member_key"]: m for m in table}
        self.assertIn(f["assertion_id"], by[f["tested_member"]]["assertion_ids"])
        self.assertEqual(by[f["untested_member"]]["tested_in_wwox_system"], "no")
        self.assertEqual(by[f["untested_member"]]["assertion_ids"], [])
        corrupted = copy.deepcopy(table)
        target = next(m for m in corrupted if m["member_key"] == f["untested_member"])
        target.update(tested_in_wwox_system="yes", assertion_ids=[f["assertion_id"]], wwox_assertions=1)
        self.assertTrue(rk.validate_attribution(u, corrupted))
        cases = {c["case_id"]: c for c in rk.matching_pilot(state()["uni"]["units"])}
        self.assertIn(f["assertion_id"], cases[f["tested_case"]]["evidence_of_this_member"]["assertion_ids"])
        self.assertEqual(cases[f["untested_case"]]["evidence_of_this_member"]["assertion_ids"], [])

    def test_unknown_requirement_stays_unknown_without_cancelling_research(self):
        f = self.fixture("unknown_is_not_negative")
        inputs = json.loads((HERE / "matching_pilot_cases.json").read_text())
        out = {c["case_id"]: c for c in rk.matching_pilot(state()["uni"]["units"], inputs)}[f["case_id"]]
        self.assertIn(f["question"], out["development_status"][f["state"]])
        self.assertNotIn(f["question"], out["development_status"]["unfavorable"])
        self.assertIn(f["research_question_contains"], out["research_question"])
        alternative = copy.deepcopy(inputs)
        c = next(c for c in alternative if c["case_id"] == f["case_id"])
        next(r for r in c["development_requirements"] if r["question"] == f["question"])["state"] = f["alternative_state"]
        changed = {c["case_id"]: c for c in rk.matching_pilot(state()["uni"]["units"], alternative)}[f["case_id"]]
        self.assertIn(f["question"], changed["development_status"]["unfavorable"])
        self.assertEqual(changed["research_question"], out["research_question"])
        self.assertEqual(changed["evidence_of_this_member"], out["evidence_of_this_member"])

    def test_pilot_reaches_existing_export_and_full_view(self):
        import repurposing_view as v
        exported = json.loads(rk.build_all()["ranking.json"])["matching_pilot"]
        self.assertEqual(len(exported), 7)  # four contrasting cases (NMDA has two actual members) plus the IT10 cases NRF2-omaveloxolone and ACK1-dasatinib
        self.assertEqual({c["case_id"] for c in exported}, {"NMDA-tool", "NMDA-member", "chloride", "residual-product", "HIF-emergent", "NRF2-omaveloxolone", "ACK1-dasatinib"})
        cur = state()["ctx"]["cur"]
        full = v.build_ranking(rk.DR, cur, "full")
        self.assertEqual(full["matching_pilot"], exported)
        html = v.render_matching_pilot(full["matching_pilot"])
        self.assertIn('id="matching-v3"', html)
        self.assertIn("PX-478", html)
        self.assertIn("sconosciuto", html)
        self.assertIn("nessun risultato WWOX attribuito", html)
        for label in ("Perché è emerso", "Evidenza a sostegno", "Che cosa potrebbe confutarlo", "Perché merita ricerca nonostante i requisiti irrisolti"):
            self.assertEqual(html.count(label), 7, label)          # the five questions of the mandate are shown for every pilot case
        self.assertIn("NFE2L2 -T(-)-&gt; IL1B", html)
        self.assertIn("ACK1-dasatinib".split("-")[0], html)
        self.assertIn("Percorso non da grafo", html)
        self.assertEqual(v.build_ranking(rk.DR, cur, "shareable")["matching_pilot"], [])
        self.assertEqual(v.render_matching_pilot([]), "")


class It10Integration(unittest.TestCase):
    """IT10 P5: the NRF2 card unit, the IT10 qualification entries, the ACK1 uncarded item and its reopenable searches, the dated correction overlay, and the two new pilot cases."""

    @staticmethod
    def fixture(name):
        return json.loads((HERE / "fixtures" / (name + ".json")).read_text())

    def test_nrf2_card_unit_enters_by_the_existing_rule_and_nothing_moves(self):
        S = state()
        u = by_id(S["uni"], "U59")
        self.assertEqual((u["unit_type"], u["origin"], u["cards"]), ("mechanism_probe", "generated_in_it10", ["L01_nrf2_axis"]))
        v = u["views"]["partial"]
        self.assertEqual((v["group"], v["lead"], v["lead_need"]), ("G4b", "F3", "NEED-REDOX-NRF2"))
        self.assertEqual(v["next_priority"]["level"], "NX2")                                    # F3 in G4b: first test, direction not established
        self.assertNotIn(u["unit_id"], sum((s_["top"] for s_ in rk.build_selections(S["uni"]).values()), []))     # never selectable without a WWOX-system result
        # the unit's members are attributed by subject: no WWOX-system assertion belongs to omaveloxolone or to the fumarates
        for m in u["member_evidence"]:
            self.assertEqual(m["tested_in_wwox_system"], "no", m["member"])
        # K01 / U28 did not move
        k = by_id(S["uni"], "U28")
        self.assertEqual((k["class"], k["views"]["partial"]["group"], k["views"]["partial"]["lead"], k["origin"]), ("ORD", "G4b", "F3", "generated_in_it9"))

    def test_it10_qualification_entries_follow_the_stated_states(self):
        q = rk.load_qualification_it10()
        self.assertEqual({q["P22-04"]["state"], q["P22-05"]["state"], q["P22-06"]["state"], q["P22-02"]["state"]}, {"DROP", "REFERENCE", "CONDITIONAL"})
        self.assertTrue(set(q).isdisjoint(rk.load_qualification()))
        units = {u["unit_id"]: u for u in state()["uni"]["units"]}
        self.assertEqual((units["U60"]["class"], units["U60"]["origin"], units["U60"]["era"]), ("EXCL", "generated_in_it10", "IT10"))
        for uid in ("U61", "U62"):
            self.assertEqual((units[uid]["class"], units[uid]["origin"]), ("EXCL", "reference_or_control"))
            self.assertFalse(units[uid]["views"]["partial"].get("member"))
            self.assertTrue(units[uid]["class_reason"])
        recs = {r["cand_id"]: r for r in state()["uni"]["it10_records"]}
        self.assertEqual({k: recs[k]["unit_id"] for k in ("P22-01", "P22-02", "P22-03", "P22-04", "P22-05", "P22-06")}, {"P22-01": "U59", "P22-02": "U59", "P22-03": "U59", "P22-04": "U60", "P22-05": "U61", "P22-06": "U62"})
        self.assertEqual(len(state()["uni"]["it9_records"]), 32)                             # the IT9 list is unchanged

    def test_mutation_it10_map_must_name_a_known_record_and_a_carded_unit(self):
        import unittest.mock as mock
        ctx = state()["ctx"]
        q = rk.load_qualification_it10()
        gone = {k: v for k, v in q.items() if k != "P22-04"}
        with mock.patch.object(rk, "load_qualification_it10", return_value=gone):
            with self.assertRaises(SystemExit):
                rk.proposal_units(ctx)
        flipped = {k: dict(v, state="KEEP") if k == "P22-04" else v for k, v in q.items()}
        with mock.patch.object(rk, "load_qualification_it10", return_value=flipped):
            units, _ = rk.proposal_units(ctx)
        self.assertEqual(next(u for u in units if u["unit_id"] == "U60")["views"]["partial"]["group"], "G4b")      # voclosporin would be ordered only if its state changed

    def test_qualification_correction_is_an_overlay_and_the_original_is_untouched(self):
        e02 = rk.load_qualification()["E-02"]
        self.assertIn("WITHDRAWN", e02["datum"])
        self.assertNotIn("by construction", e02["datum"].split("[Corrected")[0])
        self.assertEqual(e02["corrected_fields"], ["datum"])
        orig = [r for r in rk.read_tsv(rk.DR / "qualification_it9_p4c_e_20261030/qualification_E.tsv") if r["cand_id"] == "E-02"][0]
        self.assertIn("by construction", orig["decisive_datum"])                              # the stored record is never rewritten
        self.assertEqual(e02["state"], "DROP")                                                # the DROP stands
        with self.assertRaises(SystemExit):                                                   # a correction naming a field the record does not have is refused
            rk._apply_qual_corrections({"E-02": {"nope": "x"}})

    def test_ack1_is_an_uncarded_item_with_its_counter_evidence_and_reopenable_searches(self):
        unc = {r["item_id"]: r for r in state()["ctx"]["uncarded"]}
        n12 = unc["N12"]
        self.assertEqual((n12["class"], n12["provenance"], n12["related_unit"]), ("INSUFF", "own_search", ""))
        for needle in ("NOT counter-evidence for lowering ACK1", "supports ONLY the direction", "not replicates", "main-text sentence", "CONDITIONAL on WWOX protein"):
            self.assertIn(needle, n12["reason"])
        self.assertFalse(any("N12" in u["label"] for u in state()["uni"]["units"]))             # no card, no unit
        trig = {r["trigger"]: r for r in rk.triggers_rows()}
        for i in range(1, 10):      # R8 added by IT11 P4 (Tnk2-null material or a second shRNA with WWOX mRNA); R9 by IT12 P6 (G372R band above the knockout floor)
            self.assertIn(f"R{i}_q1_complement", trig)
        self.assertIn("N12", trig["R3_q1_complement"]["re_evaluates"])
        for i in range(1, 5):      # N-P1B-1 to N-P1B-4 added by IT12 P6 (genetic-interaction slice, caveats only)
            self.assertIn(f"NP1B{i}_modifiers", trig)
        self.assertIn("E03", trig["NP1B1_modifiers"]["re_evaluates"])
        self.assertEqual(len(trig), 8 + 9 + 4)      # 8 + 7 before IT11 P4 (R8), +1 R9 and +4 modifiers in IT12 P6
        import unittest.mock as mock
        with mock.patch.object(rk, "REOPEN_SEARCHES", rk.HERE / "absent.tsv"), mock.patch.object(rk, "REOPEN_SEARCHES_P1B", rk.HERE / "absent.tsv"):
            self.assertEqual(len(rk.triggers_rows()), 8)
        self.assertIn("substrate for a stability lever is UNCONFIRMED", n12["reason"])
        self.assertIn("not shown above the assay floor", n12["reason"])

    def test_every_pilot_case_answers_the_mandate_questions(self):
        cases = json.loads((HERE / "matching_pilot_cases.json").read_text())
        out = rk.matching_pilot(state()["uni"]["units"], cases)
        for c in out:
            for k in rk.PILOT_NARRATIVE:
                self.assertTrue(c[k].strip(), (c["case_id"], k))
        broken = copy.deepcopy(cases)
        del broken[0]["refutation"]
        with self.assertRaises(ValueError):
            rk.matching_pilot(state()["uni"]["units"], broken)

    def test_nrf2_probe_verdict_and_development_verdict_are_separate(self):
        f = self.fixture("nrf2_probe_vs_development")
        inputs = json.loads((HERE / "matching_pilot_cases.json").read_text())
        out = {c["case_id"]: c for c in rk.matching_pilot(state()["uni"]["units"], inputs)}[f["case_id"]]
        self.assertIn("NFE2L2 -T(-)-> IL1B", out["generating_path"])
        self.assertIn(f["question"], out["development_status"][f["state"]])
        self.assertIn(f["research_question_contains"], out["research_question"])
        self.assertEqual(out["evidence_of_this_member"]["tested_in_wwox_system"], "no")        # no WWOX-system result is attributed to the molecule
        # an unfavourable or unknown development requirement removes neither the research question nor the unit's group
        alt = copy.deepcopy(inputs)
        c = next(c for c in alt if c["case_id"] == f["case_id"])
        for r in c["development_requirements"]:
            r["state"] = "unfavorable"
        changed = {c["case_id"]: c for c in rk.matching_pilot(state()["uni"]["units"], alt)}[f["case_id"]]
        self.assertEqual((changed["research_question"], changed["research_priority"], changed["evidence_of_this_member"]), (out["research_question"], out["research_priority"], out["evidence_of_this_member"]))
        self.assertEqual(by_id(state()["uni"], out["unit_id"])["views"]["partial"]["group"], "G4b")
        self.assertEqual(out["development_status"]["favorable"], [])

    def test_ack1_case_is_conditional_on_protein_and_attributes_nothing(self):
        f = self.fixture("ack1_conditional_on_protein")
        inputs = json.loads((HERE / "matching_pilot_cases.json").read_text())
        out = {c["case_id"]: c for c in rk.matching_pilot(state()["uni"]["units"], inputs)}[f["case_id"]]
        self.assertIn(f["question"], out["development_status"][f["state"]])               # unknown, not negative
        self.assertNotIn(f["question"], out["development_status"]["unfavorable"])
        self.assertIn(f["research_question_contains"], out["research_question"])
        self.assertEqual(out["evidence_of_this_member"], {"tested_in_wwox_system": "no", "assertion_ids": [], "signs": {}, "source_pmids": [], "depth": "", "outside_wwox_assertions": 0})
        self.assertIn("Non si applica a Q230P".lower(), out["context"].lower())
        alt = copy.deepcopy(inputs)
        c = next(c for c in alt if c["case_id"] == f["case_id"])
        next(r for r in c["development_requirements"] if r["question"] == f["question"])["state"] = f["alternative_state"]
        changed = {c["case_id"]: c for c in rk.matching_pilot(state()["uni"]["units"], alt)}[f["case_id"]]
        self.assertIn(f["question"], changed["development_status"]["unfavorable"])
        self.assertEqual(changed["research_question"], out["research_question"])
        # the item must exist as an uncarded row: without it the case cannot be projected
        with self.assertRaises(KeyError):
            rk.matching_pilot(state()["uni"]["units"], inputs, [r for r in state()["ctx"]["uncarded"] if r["item_id"] != f["item_id"]])




class It11Integration(unittest.TestCase):
    """IT11 P4: the M01 card unit, the IT11 reference and drop entries, and the mapping mechanism."""

    def test_m01_card_unit_enters_by_the_rule_and_is_not_selectable(self):
        u = by_id(state()["uni"], "U63")
        self.assertEqual((u["unit_type"], u["cards"], u["class"]), ("mechanism_probe", ["M01_neurogenic_output_myc_window"], "ORD"))
        self.assertEqual(u["views"]["partial"]["group"], "G4b")
        self.assertEqual(u["views"]["partial"]["lead"], "F3")
        import json as _j
        sel = _j.load(open(rk.HERE / "ranking.json"))["summary"]["selections"]
        self.assertFalse(any("U63" in v["top"] for v in sel.values()))

    def test_it11_entries_follow_the_stated_states_and_no_group_moves_by_text(self):
        recs = {r["cand_id"]: r for r in state()["uni"]["it11_records"]}
        self.assertEqual({k: (v["state"], v["class"]) for k, v in recs.items()},
                         {"M01": ("CONDITIONAL", "ORD"), "M02": ("CONDITIONAL", "ORD"), "M05": ("REFERENCE", "EXCL"), "M06": ("DROP", "EXCL"), "M07": ("CONDITIONAL", "ORD"), "M08": ("REFERENCE", "EXCL")})
        units = {u["unit_id"]: u for u in state()["uni"]["units"]}
        for uid in ("U64", "U65", "U66"):
            self.assertEqual((units[uid]["class"], units[uid]["era"]), ("EXCL", "IT11"))

    def test_mutation_it11_map_must_name_a_known_record(self):
        import unittest.mock as mock
        q = rk.load_qualification_it11()
        gone = {k: v for k, v in q.items() if k != "M06"}
        with mock.patch.object(rk, "load_qualification_it11", return_value=gone):
            with self.assertRaises(SystemExit):
                rk.proposal_units(state()["ctx"])

class It12Integration(unittest.TestCase):
    """IT12 P6: the IT12 packages enter as caveats and corrections; no entry is added and no group moves."""

    def test_caveats_are_present_and_no_group_changed(self):
        cav = rk.read_tsv(HERE / "unit_caveats.tsv")
        txt = {u: " ".join(r["text"] for r in cav if r["unit_id"] == u) for u in ("U17", "U25", "U28", "U59", "U63")}
        self.assertIn("GIRK", txt["U17"])
        self.assertIn("BELOW", txt["U17"])
        self.assertIn("T-type evidence", txt["U25"])
        self.assertIn("narrow and separate", txt["U28"])
        self.assertIn("ONE allele", txt["U63"])
        for u in ("U28", "U59", "U63"):
            self.assertIn("although development is unresolved", txt[u])
        groups = {x["unit_id"]: (x["general_group"], x["partial_group"]) for x in rk.read_tsv(HERE / "units.tsv")}
        self.assertEqual(groups["U17"][0], "G2b")
        self.assertEqual(groups["U25"][0], "G4a")

    def test_changes_carry_a_reason_class_per_unit(self):
        rows = [r for r in rk.read_tsv(HERE / "changes.tsv") if r["note"].startswith(("figure audit", "ethosuximide result", "P47T reanalysis"))]
        self.assertTrue(rows)
        self.assertTrue(all(r["reason_class"] == "counter_evidence" for r in rows))


if __name__ == "__main__":
    unittest.main(verbosity=2)
