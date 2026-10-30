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
        self.assertEqual({u["unit_id"] for u in self.uni["units"] if u["class"] == "EXCL"}, {"X01", "X02", "X03"})

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


if __name__ == "__main__":
    unittest.main(verbosity=1)
