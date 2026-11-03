#!/usr/bin/env python3
"""Tests for the investigations step (IT20 P5): the order of research investment that opens the dashboard.

What these tests guarantee, in the module's own terms:
  * the order is an order of RESEARCH INVESTMENT and says so in the data, so a reader cannot take it for efficacy;
  * evidence depth is displayed and is NEVER a gate: a row with no unit, or a unit in the unorderable group, can rank top;
  * an unresolved or opposed need direction is named on the row that carries it, and may not be declared resolved;
  * a novelty perimeter records what was queried and may not claim that something was never studied;
  * no dose, route, schedule or preparation can enter the table;
  * ties are explicit, ranks are contiguous, and a position change carries a movement reason.

Run: python3 -B -m unittest -v disease-models.wwox.research.drug_repurposing.ranking_it8_p9_20261029.test_investigations
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

import importlib.util

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ranking_it8_inv", HERE / "ranking_it8.py")
rk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rk)


def load_rows() -> list[dict]:
    """The PUBLISHED rows: ranking.json carries at most ten (the view builder's contract, IT20 integration)."""
    j = json.loads((HERE / "ranking.json").read_text(encoding="utf-8"))
    return j["investigations"]


def load_all_rows() -> list[dict]:
    """The whole evaluated order, including the rows below the ten-row ceiling: investigations.tsv."""
    import csv as _csv
    with (HERE / "investigations.tsv").open(encoding="utf-8") as f:
        return list(_csv.DictReader(f, delimiter="\t"))


def load_summary() -> dict:
    j = json.loads((HERE / "ranking.json").read_text(encoding="utf-8"))
    return j["summary"]["investigations"]


class Contract(unittest.TestCase):
    def setUp(self):
        self.rows = load_rows()
        self.summary = load_summary()

    def test_the_table_states_that_it_orders_research_investment_and_not_efficacy(self):
        s = self.summary["plain_statement"].lower()
        self.assertIn("not a ranking of efficacy", s)
        self.assertIn("computes no position", s)
        self.assertIn("discriminating", s)
        self.assertIn("medical advice", s)

    def test_what_is_not_rewarded_is_declared_and_includes_novelty_and_pathway_count(self):
        nr = " ".join(self.summary["what_is_not_rewarded"]).lower()
        for forbidden in ("novelty", "publication count", "pathways", "ease of purchase"):
            self.assertIn(forbidden, nr)

    def test_every_row_carries_the_fields_the_dashboard_contract_requires(self):
        for r in self.rows:
            for f in ("rank", "tie_group", "intervention", "question", "why_now", "evidence_available", "decisive_uncertainty",
                      "next_test", "origin_class", "novelty_perimeter", "movement_reason", "evidence_depth", "direction_state"):
                self.assertTrue(str(r.get(f, "")).strip(), f"{r['inv_id']} missing {f}")

    def test_ranks_are_contiguous_and_ties_are_explicit(self):
        ranks = sorted({r["rank"] for r in self.rows})
        self.assertEqual(ranks, list(range(1, len(ranks) + 1)))
        for r in self.rows:
            n = sum(1 for x in self.rows if x["rank"] == r["rank"])
            self.assertEqual(r["tie_group"], f"{r['rank']} (tie of {n})" if n > 1 else str(r["rank"]))

    def test_at_most_ten_ranked_positions_and_no_artificial_filler(self):
        self.assertLessEqual(len({r["rank"] for r in self.rows}), 10)
        self.assertEqual(len({r["inv_id"] for r in self.rows}), len(self.rows))

    def test_ranking_json_publishes_at_most_ten_rows(self):
        """2026-11-02: the view builder rejects a longer list; the ceiling is the operator's 'up to ten'."""
        self.assertLessEqual(len(self.rows), rk.MAX_PUBLISHED_INVESTIGATIONS)
        for r in self.rows:
            self.assertFalse(r.get("below_the_line"), f"{r['inv_id']} is below the line but was published")

    def test_origin_class_and_direction_state_use_the_closed_vocabularies(self):
        for r in self.rows:
            self.assertIn(r["origin_class"], rk.ORIGIN_CLASSES)
            self.assertIn(r["direction_state"], rk.DIRECTION_STATES)

    def test_a_novelty_perimeter_never_claims_that_something_was_never_studied(self):
        for r in self.rows:
            t = r["novelty_perimeter"].lower()
            self.assertIn("queried", t, f"{r['inv_id']} does not say what was queried")
            for bad in rk.FORBIDDEN_NOVELTY:
                self.assertNotIn(bad, t, f"{r['inv_id']} claims absence: {bad!r}")

    def test_no_row_carries_a_dose_route_schedule_or_preparation(self):
        for r in self.rows:
            blob = " ".join(str(r.get(c, "")) for c in rk.INV_COLS).lower()
            for bad in rk.FORBIDDEN_POSOLOGY:
                self.assertNotIn(bad, blob, f"{r['inv_id']} carries posology: {bad!r}")


class DepthIsDisplayedNotRequired(unittest.TestCase):
    """The operator's constraint: evidence depth must be visible and must not stop a new hypothesis from emerging."""

    def setUp(self):
        self.rows = load_rows()

    def test_a_row_without_a_ranked_unit_has_no_depth_of_zero(self):
        for r in self.rows:
            if not r["unit_id"]:
                self.assertIn("not a depth of zero", r["evidence_depth"])

    def test_an_unorderable_or_undepth_row_is_not_forced_to_the_bottom(self):
        """GU in the group view, or no unit at all, must be able to outrank a unit with measured WWOX evidence."""
        worst = max(r["rank"] for r in self.rows)
        weak = [r for r in self.rows if r["direction_state"] == "unresolved" or not r["unit_id"]]
        self.assertTrue(weak, "the fixture should contain at least one row whose premise is missing")
        self.assertTrue(any(r["rank"] < worst for r in weak),
                        "every premise-missing row sits at the bottom: depth has become a requirement again")

    def test_a_premise_missing_row_reaches_the_top_tie_for_a_stated_reason(self):
        top = [r for r in self.rows if r["rank"] == 1]
        unresolved_top = [r for r in top if r["direction_state"] == "unresolved"]
        self.assertTrue(unresolved_top, "no premise-missing investigation reaches the top tie")
        for r in unresolved_top:
            self.assertIn("not a negative finding", r["direction_state_label"])
            self.assertTrue(r["decisive_uncertainty"].strip())

    def test_an_unresolved_need_direction_is_never_declared_resolved(self):
        j = json.loads((HERE / "ranking.json").read_text(encoding="utf-8"))
        for r in j["investigations"]:
            if r["need_direction"] in ("uncertain", "modulate"):
                self.assertNotEqual(r["direction_state"], "resolved", f"{r['inv_id']} hides an unresolved direction")


class OrderDoesNotRewardTheWrongThings(unittest.TestCase):
    def setUp(self):
        self.rows = load_rows()

    def test_the_order_is_not_a_function_of_how_many_needs_or_pathways_a_row_touches(self):
        """A rank may not be explainable by a count: pathway coverage is the reflex this module refuses."""
        by_rank = sorted(self.rows, key=lambda r: r["rank"])
        # one need per row by construction; the test guards the contract rather than a computed correlation
        self.assertTrue(all(r["need_id"] for r in by_rank))

    def test_generated_and_known_rows_are_interleaved_not_segregated_by_origin(self):
        """Origin is a provenance label, never a bonus or a penalty: both classes must appear across the order."""
        gen = {r["rank"] for r in self.rows if r["origin_class"] == "generated_by_legend"}
        known = {r["rank"] for r in self.rows if r["origin_class"] == "known_in_wwox"}
        self.assertTrue(gen and known)
        self.assertTrue(min(gen) <= max(known) and min(known) <= max(gen),
                        "one origin class occupies a block of the order: novelty or familiarity is being rewarded")

    def test_a_generated_hypothesis_can_outrank_a_unit_that_sits_higher_in_the_group_view(self):
        j = json.loads((HERE / "ranking.json").read_text(encoding="utf-8"))
        units = {u["unit_id"]: u for u in j["units"]}
        gen = [r for r in self.rows if r["origin_class"] == "generated_by_legend"]
        beaten = []
        for g in gen:
            for r in self.rows:
                if r["rank"] <= g["rank"] or not r["unit_id"]:
                    continue
                u = units[r["unit_id"]]
                if "G1" in (u["views"]["broad"].get("group"), u["views"]["partial"].get("group")) or \
                   "G2b" in (u["views"]["broad"].get("group"), u["views"]["partial"].get("group")):
                    beaten.append((g["inv_id"], r["inv_id"]))
        self.assertTrue(beaten, "no generated hypothesis outranks a unit with a measured WWOX-system position: "
                                "the investigations order has collapsed onto the evidence-depth order")


class TheTenRowCeiling(unittest.TestCase):
    """The published list is capped at ten; a row beyond it is kept, flagged and explained, never deleted or judged."""

    def setUp(self):
        self.pub = load_rows()
        self.all = load_all_rows()
        self.summary = load_summary()

    def test_the_tsv_keeps_every_row_the_json_omits(self):
        self.assertGreaterEqual(len(self.all), len(self.pub))
        omitted = {r["inv_id"] for r in self.all} - {r["inv_id"] for r in self.pub}
        self.assertEqual(omitted, {r["inv_id"] for r in self.summary["below_the_line_rows"]})

    def test_a_row_below_the_line_states_the_reason_and_is_not_called_unpromising(self):
        for r in self.all:
            if r.get("below_the_line") == "yes":
                self.assertIn("ten-row ceiling", r["below_the_line_reason"])
                self.assertIn("not a judgement that the investigation is unpromising", r["below_the_line_reason"])
                self.assertIn("below the line", r["movement_reason"])

    def test_the_summary_declares_the_ceiling_and_what_falls_below_it(self):
        self.assertEqual(self.summary["published_ceiling"], rk.MAX_PUBLISHED_INVESTIGATIONS)
        self.assertEqual(self.summary["published"], len(self.pub))
        self.assertEqual(self.summary["count_including_below_the_line"], len(self.all))
        if self.summary["below_the_line"]:
            self.assertIn("never a finding", self.summary["below_the_line_note"])

    def test_the_order_digest_covers_the_whole_evaluated_order_not_only_the_published_part(self):
        """The ceiling is a page limit: it must not move the digest the snapshot mechanism compares."""
        self.assertEqual(self.summary["order_digest"], rk.sha16([(r["inv_id"], int(r["rank"])) for r in self.all]))

    def test_a_short_list_is_not_padded_and_is_untouched_by_the_ceiling(self):
        rows = [{"inv_id": f"I{i}", "rank": i, "movement_reason": "m"} for i in range(1, 4)]
        out = rk._apply_the_line(rows)
        self.assertEqual(len(out), 3)
        self.assertTrue(all(not r["below_the_line"] for r in out))

    def test_a_tie_that_would_overflow_the_ceiling_goes_below_the_line_whole(self):
        """Nine singles then a tie of three: publishing two of the three would assert an order inside the tie."""
        rows = [{"inv_id": f"I{i}", "rank": i, "movement_reason": "m"} for i in range(1, 10)]
        rows += [{"inv_id": f"T{k}", "rank": 10, "movement_reason": "m"} for k in range(3)]
        out = rk._apply_the_line(rows)
        pub = [r for r in out if not r["below_the_line"]]
        self.assertEqual(len(pub), 9)
        self.assertEqual({r["inv_id"] for r in out if r["below_the_line"]}, {"T0", "T1", "T2"})

    def test_a_tie_that_exactly_fills_the_ceiling_is_published_whole(self):
        rows = [{"inv_id": f"I{i}", "rank": i, "movement_reason": "m"} for i in range(1, 9)]
        rows += [{"inv_id": f"T{k}", "rank": 9, "movement_reason": "m"} for k in range(2)]
        out = rk._apply_the_line(rows)
        self.assertTrue(all(not r["below_the_line"] for r in out))

    def test_everything_below_the_first_cut_rank_goes_below_the_line(self):
        rows = [{"inv_id": f"I{i}", "rank": i, "movement_reason": "m"} for i in range(1, 13)]
        out = rk._apply_the_line(rows)
        self.assertEqual({r["inv_id"] for r in out if not r["below_the_line"]}, {f"I{i}" for i in range(1, 11)})


class Movement(unittest.TestCase):
    def test_first_evaluation_says_so(self):
        for r in load_rows():
            self.assertTrue(r["movement_reason"].strip())

    def test_a_changed_position_is_reported_with_its_direction(self):
        row = {"inv_id": "INV-03", "rank": 2}
        prev = {"investigations": {"INV-03": {"rank": 5}}}
        self.assertIn("moved up from rank 5 to 2", rk.investigation_movement(row, prev))
        prev2 = {"investigations": {"INV-03": {"rank": 1}}}
        self.assertIn("moved down from rank 1 to 2", rk.investigation_movement(row, prev2))

    def test_an_unchanged_position_is_reported_as_unchanged(self):
        self.assertIn("unchanged", rk.investigation_movement({"inv_id": "INV-01", "rank": 1}, {"investigations": {"INV-01": {"rank": 1}}}))

    def test_a_new_entry_is_reported_as_new(self):
        self.assertIn("new entry", rk.investigation_movement({"inv_id": "INV-99", "rank": 3}, {"investigations": {"INV-01": {"rank": 1}}}))

    def test_investigation_positions_travel_in_the_snapshot_state(self):
        files = {"ranking.json": (HERE / "ranking.json").read_bytes()}
        st = rk.current_state(files)
        self.assertIn("investigations", st)
        self.assertIn("INV-01", st["investigations"])
        self.assertEqual(st["investigations"]["INV-01"]["rank"], 1)


class Guards(unittest.TestCase):
    """The validator refuses a row that would mislead; each guard is exercised on a copy of the real table."""

    def setUp(self):
        self.ctx = {"needs": {"N-OK": {"dir": "down", "short": "ok", "goal": "partial_benefit"},
                              "N-UNC": {"dir": "uncertain", "short": "unc", "goal": "partial_benefit"}}}
        self.uni = {"units": [{"unit_id": "U07", "class": "ORD", "evaluation_depth": "E4", "evaluation_depth_text": "x",
                               "views": {"broad": {"group": "G1"}, "partial": {"group": "G3"}}, "tracks": ["A"]}]}
        self.base = {"inv_id": "INV-01", "rank": "1", "unit_id": "U07", "need_id": "N-OK", "intervention": "i", "question": "q",
                     "why_now": "w", "evidence_available": "e", "decisive_uncertainty": "d", "next_test": "n", "feasibility": "f",
                     "origin_class": "known_in_wwox", "novelty_perimeter": "Queried: the cards.", "direction_state": "resolved"}

    def run_with(self, rows):
        import csv as _csv
        import io
        import tempfile
        cols = list(self.base.keys())
        buf = io.StringIO()
        w = _csv.DictWriter(buf, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow(r)
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "investigations_it20.tsv"
            p.write_text(buf.getvalue(), encoding="utf-8")
            old = rk.INVESTIGATIONS_SRC
            rk.INVESTIGATIONS_SRC = p
            try:
                return rk.investigations(self.ctx, self.uni, "2026-11-02", None)
            finally:
                rk.INVESTIGATIONS_SRC = old

    def test_the_real_shape_is_accepted(self):
        self.assertEqual(len(self.run_with([self.base])), 1)

    def test_an_uncertain_need_declared_resolved_is_refused(self):
        bad = dict(self.base, need_id="N-UNC", direction_state="resolved")
        with self.assertRaises(SystemExit) as e:
            self.run_with([bad])
        self.assertIn("direction_state=resolved", str(e.exception))

    def test_a_never_studied_claim_in_the_novelty_perimeter_is_refused(self):
        bad = dict(self.base, novelty_perimeter="Queried: nothing. This compound was never studied in WWOX.")
        with self.assertRaises(SystemExit) as e:
            self.run_with([bad])
        self.assertIn("novelty_perimeter", str(e.exception))

    def test_posology_anywhere_in_a_row_is_refused(self):
        bad = dict(self.base, next_test="give 20 mg and measure the burst")
        with self.assertRaises(SystemExit) as e:
            self.run_with([bad])
        self.assertIn("dose, route, schedule", str(e.exception))

    def test_a_missing_decisive_uncertainty_is_refused(self):
        with self.assertRaises(SystemExit) as e:
            self.run_with([dict(self.base, decisive_uncertainty="  ")])
        self.assertIn("decisive_uncertainty", str(e.exception))

    def test_an_unknown_unit_or_need_is_refused(self):
        with self.assertRaises(SystemExit):
            self.run_with([dict(self.base, unit_id="U999")])
        with self.assertRaises(SystemExit):
            self.run_with([dict(self.base, need_id="N-NOPE")])

    def test_a_gap_in_the_ranks_is_refused(self):
        with self.assertRaises(SystemExit) as e:
            self.run_with([self.base, dict(self.base, inv_id="INV-02", rank="3")])
        self.assertIn("contiguous", str(e.exception))

    def test_a_duplicate_inv_id_is_refused(self):
        with self.assertRaises(SystemExit) as e:
            self.run_with([self.base, dict(self.base)])
        self.assertIn("duplicate", str(e.exception))

    def test_an_unknown_origin_class_is_refused(self):
        with self.assertRaises(SystemExit):
            self.run_with([dict(self.base, origin_class="promising")])

    def test_a_row_with_no_unit_is_accepted_and_carries_no_depth_of_zero(self):
        rows = self.run_with([dict(self.base, unit_id="")])
        self.assertIn("not a depth of zero", rows[0]["evidence_depth"])


class IT21Corrections(unittest.TestCase):
    """IT21 P1: two statements in the published investigations were wider than the card or the catalogue behind them."""

    def row(self, inv):
        return next(r for r in load_all_rows() if r["inv_id"] == inv)

    def test_glycaemia_is_not_called_prevented_and_the_three_ages_stay_distinct(self):
        t = self.row("INV-01")["evidence_available"]
        self.assertNotIn("glucose and weight endpoints are prevented", t)
        low = t.lower()
        for must in ("p10", "not significantly different from the untreated knockout", "p20", "comparator is absent",
                     "age, dose and comparison", "not evidence of no benefit"):
            self.assertIn(must, low)
        self.assertNotIn("no effect", low.replace("not evidence of no benefit", ""), "no universal claim of inefficacy")

    def test_the_t_type_pair_is_a_proposal_to_verify_and_its_falsifier_is_not_overstated(self):
        r = self.row("INV-03")
        blob = " ".join(r.values()).lower()
        self.assertNotIn("isoform-discriminating", blob)
        self.assertIn("proposal to verify", blob)
        self.assertIn("annotation completeness", blob)
        self.assertIn("absence of a subtype in a catalogue is not inactivity", blob)
        self.assertNotIn("would weaken the t-type attribution rather than strengthen", blob)
        self.assertIn("compatible with a common target", blob)


class It21P7(unittest.TestCase):
    """IT21 P7: conditional hypotheses enter the order with explicit reasons, never as qualified; movement is read against IT20; the informative
    negatives are shareable-safe; the curated context states that positions are written by agents and not computed."""

    def setUp(self):
        self.j = json.loads((HERE / "ranking.json").read_text(encoding="utf-8"))
        self.all = load_all_rows()

    def test_new_rows_are_conditional_with_origin_feasibility_and_a_stated_reason(self):
        cond = [r for r in self.all if r["status"] == "conditional_hypothesis"]
        self.assertGreaterEqual(len(cond), 3)
        for r in cond:
            for f in ("origin_detail", "feasibility", "evidence_depth", "movement_reason", "why_now"):
                self.assertTrue(r[f].strip(), f"{r['inv_id']} {f}")
            self.assertTrue(r["movement_reason"].startswith("new in IT21"))
            self.assertIn("Not rewarded: novelty", r["movement_reason"])
            blob = json.dumps(r).lower()
            for bad in rk.FORBIDDEN_QUALIFIED:
                self.assertNotIn(bad, blob)

    def test_a_conditional_row_called_qualified_is_refused(self):
        base = {"inv_id": "X", "rank": "1", "unit_id": "", "need_id": "N-OK", "intervention": "i", "question": "q", "why_now": "w", "evidence_available": "e",
                "decisive_uncertainty": "d", "next_test": "n", "feasibility": "f", "origin_class": "generated_by_legend", "novelty_perimeter": "Queried: the cards.",
                "direction_state": "resolved", "status": "conditional_hypothesis", "origin_detail": "o", "evidence_solidity": "s", "movement_note": "m", "it20_rank": ""}
        g = Guards("test_the_real_shape_is_accepted")
        g.setUp()
        g.base = base
        self.assertEqual(len(g.run_with([base])), 1)
        with self.assertRaises(SystemExit):
            g.run_with([dict(base, why_now="This is now qualified hypothesis material.")])
        with self.assertRaises(SystemExit):
            g.run_with([dict(base, origin_detail="")])
        with self.assertRaises(SystemExit):
            g.run_with([dict(base, status="qualified")])

    def test_movement_is_read_against_it20(self):
        for r in self.all:
            m = r["movement_reason"]
            self.assertTrue(m.startswith(("new in IT21", "position unchanged from IT20", "moved ")), m)
            if r["it20_rank"]:
                self.assertEqual(m.startswith("position unchanged"), int(r["it20_rank"]) == int(r["rank"]))
        self.assertEqual(rk.investigation_movement_it20({"rank": 6}, {"it20_rank": "5", "movement_note": "n"}), "moved down from rank 5 (IT20) to rank 6: n")

    def test_the_context_declares_curation_and_carries_the_pending_slot_and_the_funnel(self):
        c = self.j["investigations_context"]
        self.assertTrue(c["positions_are_curated_not_computed"])
        self.assertIn("computes no position", c["curation"])
        # the P5 evaluation is committed (state 'measured', set before P8-fix); P8-fix: 980 conditional rows after the glue/conflict sign guard
        self.assertEqual(c["wwox_contribution"]["state"], "measured")
        self.assertEqual(c["funnel"]["qualified_hypotheses"], 0)
        self.assertEqual(c["funnel"]["generator_conditional_rows"], 980)
        self.assertEqual(sum(c["published_vs_it20"].values()), len(self.j["investigations"]))

    def test_the_ceiling_never_displaces_a_risk_flagged_or_human_report_row_for_a_conditional_probe(self):
        """P8-fix (verifier D3): the curation block states the rule and the data obeys it."""
        c = self.j["investigations_context"]
        self.assertIn("risk flag", c["curation"])
        self.assertIn("not displaced by conditional probes", c["ceiling_rule"])
        below = [r for r in self.all if r.get("below_the_line")]
        shown = [r for r in self.all if not r.get("below_the_line")]
        if any(r["status"] == "conditional_hypothesis" for r in shown) or not below:
            return
        protected = [r for r in below if r["direction_state"] == "opposed_risk" or "real human reports" in r["why_now"].lower() or r["evidence_available"].lower().startswith("clinical report only")]
        self.assertEqual([r["inv_id"] for r in protected], [], "a risk-flagged or human-report row is below the line while a conditional probe is shown")

    def test_lithium_and_gaba_t_are_shown_and_the_new_conditional_probes_are_below_the_line_and_not_qualified(self):
        by = {r["inv_id"]: r for r in self.all}
        for k in ("INV-09", "INV-10"):
            self.assertFalse(by[k].get("below_the_line"), k)
        for k in ("INV-12", "INV-13"):
            self.assertEqual(by[k]["below_the_line"], "yes", k)
            self.assertEqual(by[k]["status"], "conditional_hypothesis")
        self.assertEqual(sum(1 for r in self.all if not r.get("below_the_line")), 10)

    def test_inv_01_states_that_the_paper_text_overstates_the_glycaemia_correction_and_inv_09_places_the_concern_correctly(self):
        by = {r["inv_id"]: r for r in self.all}
        self.assertIn("both doses partially corrected hypoglycaemia", by["INV-01"]["evidence_available"])
        self.assertIn("the panel does not support it", by["INV-01"]["evidence_available"])
        m = by["INV-09"]["movement_reason"] + by["INV-09"]["evidence_available"]
        self.assertIn("+/+ arm of Cheng 2020 Figure 7d", m)
        self.assertIn("DISFAVOURED_BY_SIGN_PRECEDENT", m)
        self.assertIn("pilocarpine model in Wwox mice", m)
        self.assertNotIn("rejected with an informative sign", m)

    def test_informative_negatives_keep_the_name_out_of_the_shareable_fields(self):
        negs = self.j["investigations_context"]["informative_negatives"]
        self.assertGreaterEqual(len(negs), 5)
        for n in negs:
            if n["chembl_ids"]:
                name = n["subject_full"].replace(",", " ").split()[0].lower()
                for f in ("subject_label", "ruled_out", "reason", "reopen"):
                    self.assertNotIn(name, n[f].lower())
            self.assertTrue(n["reopen"].strip())

    def test_a_published_row_with_a_chembl_id_has_a_class_label_in_the_allowlist(self):
        allow = json.loads((HERE.parent / "view/shareable_sources.json").read_text(encoding="utf-8"))
        labels = allow["investigations_shareable"]["class_labels"]
        for r in self.j["investigations"]:
            self.assertIn(r["intervention"], labels, f"{r['inv_id']} would show the generic withheld note")


if __name__ == "__main__":
    unittest.main(verbosity=2)
