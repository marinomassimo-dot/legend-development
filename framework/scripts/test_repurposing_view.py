#!/usr/bin/env python3
"""Offline regressions for repurposing_view.py: headline counts equal the module's source JSON,
the shareable build embeds no row outside view/shareable_sources.json, units are never conflated,
exported cards carry public identifiers, opposed actions are visible in a comparison,
the build is deterministic, failed / stale / truncated / not-fetched source states are displayed
distinct from OK and from empty, and (when a Chromium binary exists) the rendered page's filter
counts equal a Python reference filter.
Run: python3 -B framework/scripts/test_repurposing_view.py"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_view as rv  # noqa: E402

DR = rv.DEFAULT_DR
HAVE_DATA = (DR / "coverage/coverage_summary.json").exists()


def static_numbers(page: str) -> dict:
    return {m.group(1): m.group(2) for m in re.finditer(r'data-k="([^"]+)" data-v="([^"]*)"', page)}


def embedded(page: str) -> dict:
    m = re.search(r'<script id="data" type="application/json">(.*?)</script>', page, re.S)
    return json.loads(m.group(1).replace("<\\/", "</").replace("<\\!--", "<!--"))


@unittest.skipUnless(HAVE_DATA, "module data absent")
class RealData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = rv.build(DR)
        cls.nums = static_numbers(cls.page)
        cls.P = embedded(cls.page)
        cls.sm = json.loads((DR / "coverage/coverage_summary.json").read_text())
        cls.cm = json.loads((DR / "coverage/coverage_matrix.json").read_text())
        cls.pr = json.loads((DR / "coverage/priorities.json").read_text())
        cls.st = json.loads((DR / "catalog/catalog_stats.json").read_text())

    def test_headline_counts_match_source(self):
        n, sm, st = self.nums, self.sm, self.st
        exp = {
            "funnel.records": sm["units"]["catalogue_records"], "funnel.families": sm["units"]["families"],
            "funnel.records_with_target_data": sm["catalogue_coverage"]["records_with_any_target_row"],
            "funnel.records_with_link": sm["catalogue_coverage"]["records_with_documented_link_to_a_need"],
            "funnel.families_with_link": sm["catalogue_coverage"]["families_with_documented_link_to_a_need"],
            "funnel.records_with_action": sm["catalogue_coverage"]["records_with_stated_action_on_a_need_target"],
            "funnel.families_with_action": sm["catalogue_coverage"]["families_with_stated_action_on_a_need_target"],
            "funnel.priority_pairs": len(self.pr["priorities"]),
            "funnel.priority_rows": len({p["row_id"] for p in self.pr["priorities"]}),
            "funnel.card_rows": sum(1 for r in self.cm["rows"] if r.get("cards")),
            "funnel.evaluated_records": sm["evaluated_vs_records"]["records_evaluated_against_wwox_needs_with_any_observation"],
            "access.unknown": st["access_unknown_unverified_entries"],
        }
        for k, v in st["access_category_overlapping_counts"].items():
            exp["access." + k] = v
        by = sm["priorities"]["by_disposition"]
        for d, v in by.items():
            exp["disp." + d] = v
        exp["disp.incomplete_or_failed_query"] = by.get("incomplete_or_failed_query", 0)
        for k, v in exp.items():
            self.assertEqual(n[k], str(v), k)
        self.assertIn("not distinct drugs", self.page)

    def test_priority_counts_equal_sum_of_dispositions(self):
        self.assertEqual(sum(d["n"] for d in self.P["dispositions"]), len(self.pr["priorities"]))
        self.assertEqual(len(self.P["dispositions"]), 8)   # 7 + mixed_consistent_and_opposed_actions
        self.assertEqual(len({d["id"] for d in self.P["dispositions"]}), 8)
        got = sum(1 for p in self.P["pairs"] if "p" in p)
        self.assertEqual(got, len(self.pr["priorities"]))
        self.assertEqual(len(self.P["pairs"]), len(self.cm["cells"]))

    def test_needs_panel_matches_data(self):
        self.assertEqual(len(self.P["needs"]), 22)
        per = self.sm["needs"]["per_need"]
        for n in self.P["needs"]:
            self.assertEqual(n["fam_link"], per[n["id"]]["families_with_documented_link"])
            for lv in rv.LEVELS:
                self.assertEqual(sum(n["levels"][lv].values()), n["n_pairs"])  # states of one level partition the cells
        uncertain = [n for n in self.P["needs"] if n["dir"] == "uncertain"]
        self.assertEqual(len(uncertain), self.sm["needs"]["exploration_only"])
        self.assertTrue(all(n["explore"] for n in uncertain))

    def test_link_split_and_excluded_rows_match_source(self):
        cc = self.sm["catalogue_coverage"]
        n = self.nums
        self.assertEqual(n["funnel.union_headline_records"], str(cc["union_headline_records"]))
        self.assertEqual(n["funnel.union_headline_families"], str(cc["union_headline_families"]))
        self.assertEqual(n["funnel.union_pm_records"], str(cc["union_with_pathway_members_records"]))
        self.assertEqual(n["funnel.excluded_records"], str(cc["excluded_rows"]["records"]))
        for k, v in cc["excluded_rows"]["by_reason"].items():
            self.assertEqual(n["funnel.excluded." + k], str(v))
        # the headline never includes the pathway-member union
        self.assertLessEqual(cc["union_headline_records"], cc["union_with_pathway_members_records"])
        self.assertGreater(len(self.P["excluded_detail"]), 0)
        self.assertEqual(len(self.P["excluded_detail"]), cc["excluded_rows"]["records"])

    def test_cells_and_distinct_families_both_shown(self):
        by = self.sm["priorities"]["by_disposition_distinct_families_or_rows"]
        for d in self.P["dispositions"]:
            self.assertEqual(d["fam"], by.get(d["id"]))
            if d["fam"] is not None:
                self.assertEqual(self.nums["dispfam." + d["id"]], str(d["fam"]))
        self.assertIn("Distinct families or rows", self.page)

    def test_leads_match_source(self):
        leads = json.loads((DR / "coverage/lead_dispositions.json").read_text())["dispositions"]
        self.assertEqual(self.nums["leads.n"], str(len(leads)))
        for d in leads:
            self.assertIn(f'data-lead="{d["id"]}"', self.page)
            self.assertIn(d["decision"], self.page)

    def test_non_ok_sources_flagged_prominently(self):
        notok = {k: v for k, v in self.sm["source_states"].items() if isinstance(v, dict) and v.get("state") != "OK"}
        self.assertEqual(self.nums["sources.not_ok"], str(len(notok)) if notok else "0")
        for k in notok:
            self.assertIn(f'data-banner="{k}"', self.page)
        if not notok:
            self.assertNotIn('id="source-banner"', self.page)

    def test_levels_never_summed(self):
        self.assertNotRegex(self.page, r"L1\s*\+\s*L2")
        self.assertTrue(self.P["tech"]["never_summed"])

    def test_dgidb_licence_and_regeneration_present(self):
        self.assertIn("NOT CLEARED FOR PUBLIC RELEASE", self.page)
        self.assertIn("repurposing_coverage.py run", self.page)

    def test_size_and_self_contained(self):
        self.assertLess(len(self.page.encode()), rv.MAX_BYTES)
        self.assertNotRegex(self.page, r'src="https?://')
        self.assertNotRegex(self.page, r"@import|url\(\s*https?:")
        self.assertNotIn("<link ", self.page)
        hosts = set(re.findall(r'href="https?://([^/"]+)', self.page))
        self.assertLessEqual(hosts, {"dgidb.org", "civicdb.org", "www.docm.info", "open.fda.gov", "huggingface.co", "www.ebi.ac.uk", "www.guidetopharmacology.org", "dsld.od.nih.gov", "pubmed.ncbi.nlm.nih.gov", "doi.org"} | {h for h in hosts if h.endswith(".nih.gov") or h.endswith("ebi.ac.uk") or h.endswith("docm.info")})

    def test_determinism(self):
        self.assertEqual(rv.build(DR), self.page)
        self.assertEqual(rv.build(DR, "shareable"), rv.build(DR, "shareable"))

    def test_committed_views_are_current(self):
        for src, name in rv.OUT_NAME.items():
            out = DR / "view" / name
            if out.exists():
                self.assertEqual(out.read_text(encoding="utf-8"), rv.build(DR, src), f"run repurposing_view.py run{' --source shareable' if src == 'shareable' else ''}")

    def test_no_personal_or_contact_data(self):
        self.assertNotRegex(self.page, r"[\w.+-]+@[\w-]+\.[\w.]+")


class States(unittest.TestCase):
    def manifest(self, statuses):
        return {"sources": {k: {"name": k.upper(), "last_attempt": {"status": s, "detail": "d-" + k, "utc": "2026-01-01T00:00:00Z"},
                                "data": {"retrieved_utc": "2026-01-01T00:00:00Z", "version": "v1"}, "licence": "L"} for k, s in statuses.items()}}

    def test_states_distinct_from_ok_and_each_other(self):
        sts = {"a": "OK", "b": "FAILED", "c": "STALE_EXPORT", "d": "PARTIAL", "e": "NOT_FETCHED", "f": "weird", "g": "INCOMPLETE", "h": "STALE_AFTER_FAILED_REFRESH"}
        rows = rv.source_rows(self.manifest(sts), {}, {"source_states": sts})
        classes = {r["id"]: r["state_class"] for r in rows}
        self.assertEqual(classes, {"a": "ok", "b": "failed", "c": "stale", "d": "truncated", "e": "not_fetched", "f": "other", "g": "incomplete", "h": "stale"})
        page = rv.render_sources(rows)
        for c in ("failed", "incomplete", "stale", "truncated", "not_fetched", "other"):
            self.assertIn(f'class="st st-{c}"', page)
        self.assertIn("NOT FETCHED", page)
        self.assertEqual(len(re.findall(r'class="st st-ok"', page)), 1)

    def test_empty_is_not_a_success_and_not_a_state(self):
        page = rv.render_sources([])
        self.assertIn("missing record", page)
        self.assertNotIn("st-ok", page)

    def test_missing_status_is_not_ok(self):
        rows = rv.source_rows({"sources": {"x": {"name": "X"}}}, {}, {"source_states": {}})
        self.assertEqual(rows[0]["state_class"], "other")  # NOT_RECORDED
        self.assertNotEqual(rows[0]["state_class"], "ok")

    def test_summary_stale_overrides_manifest_ok(self):
        rows = rv.source_rows(self.manifest({"dgidb": "OK"}), {}, {"source_states": {"dgidb": {"state": "STALE_EXPORT", "detail": "old export"}}})
        self.assertEqual(rows[0]["state_class"], "stale")
        self.assertEqual(rows[0]["detail"], "old export")

    def test_partial_shows_its_detail(self):
        rows = rv.source_rows(self.manifest({"dsld": "OK"}), {}, {"source_states": {"dsld": {"state": "PARTIAL", "detail": "981 of 4697 names"}}})
        self.assertEqual(rows[0]["state_class"], "truncated")
        self.assertIn("981 of 4697", rv.render_sources(rows))

    def test_classify(self):
        self.assertEqual(rv.classify_state("PARTIAL"), "truncated")
        self.assertEqual(rv.classify_state("error 500"), "failed")
        self.assertEqual(rv.classify_state(None), "other")


@unittest.skipUnless(HAVE_DATA, "module data absent")
class Browser(unittest.TestCase):
    """Runs the page's JS in headless Chromium when available; otherwise skipped."""
    CANDIDATES = ["/snap/chromium/current/usr/lib/chromium-browser/chrome", "chromium", "chromium-browser", "google-chrome"]

    @classmethod
    def setUpClass(cls):
        cls.bin = next((b for b in cls.CANDIDATES if shutil.which(b) or Path(b).exists()), None)
        if not cls.bin:
            raise unittest.SkipTest("no Chromium")
        cls.tmp = tempfile.TemporaryDirectory()
        cls.html = Path(cls.tmp.name) / "v.html"
        cls.html.write_text(rv.build(DR), encoding="utf-8")
        cls.P = embedded(cls.html.read_text())

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def dom(self, frag="", html=None, width=None):
        cmd = [self.bin, "--headless=new", "--disable-gpu", f"--user-data-dir={self.tmp.name}/p", "--virtual-time-budget=5000"]
        if width:
            cmd.append(f"--window-size={width},900")
        r = subprocess.run(cmd + ["--dump-dom", f"file://{html or self.html}{frag}"], capture_output=True, text=True, timeout=120)
        if "data-ready" not in r.stdout:
            self.skipTest("browser could not run the page: " + r.stderr[-200:])
        return r.stdout

    def ref(self, **f):
        P = self.P
        out = []
        for p in P["pairs"]:
            n, r = P["needs"][p["n"]], P["rows"][p["r"]]
            if f.get("need") and n["id"] != f["need"]:
                continue
            if f.get("track") and n["track"] != f["track"]:
                continue
            if f.get("goal") and n["goal"] != f["goal"]:
                continue
            if f.get("access") and f["access"] not in r["acc"]:
                continue
            if f.get("disp") and not ("p" in p and P["dispositions"][p["p"]["d"]]["id"] == f["disp"]):
                continue
            out.append(p)
        return out

    def counts(self, dom):
        g = lambda i: int(re.search(rf'id="{i}">(\d+)<', dom).group(1))
        return g("cnt-pairs"), g("cnt-prio")

    def test_unfiltered_and_filtered_counts(self):
        cases = [({}, ""), ({"disp": "exploration_candidate"}, "#f=disp:exploration_candidate"),
                 ({"track": "B", "goal": "partial_benefit"}, "#f=track:B&goal:partial_benefit"),
                 ({"access": "prescription", "disp": "consistent_mechanism_candidate"}, "#f=access:prescription&disp:consistent_mechanism_candidate")]
        for f, frag in cases:
            exp = self.ref(**f)
            got = self.counts(self.dom(frag))
            self.assertEqual(got, (len(exp), sum(1 for p in exp if "p" in p)), frag)

    def test_distinct_disposition_chips_rendered(self):
        d = self.dom()
        for disp in self.P["dispositions"]:
            self.assertRegex(d, rf'data-dn="{disp["id"]}"')
        self.assertEqual(len(self.P["dispositions"]), 8)   # 7 + mixed_consistent_and_opposed_actions

    def test_new_disposition_filter_and_stale_badge(self):
        ids = [d["id"] for d in self.P["dispositions"]]
        self.assertIn("no_catalogue_link_found", ids)
        exp = self.ref(disp="no_catalogue_link_found")
        self.assertEqual(self.counts(self.dom("#f=disp:no_catalogue_link_found")), (len(exp), len(exp)))
        d = self.dom()
        notok = [x for x in self.P["tech"]["sources"] if x["state_class"] != "ok"]
        for x in notok:
            self.assertRegex(d, rf'data-banner="{x["id"]}"')
            self.assertIn(f'st-{x["state_class"]}', d)

    def test_criteria_and_card_link_navigation(self):
        d = self.dom("#f=need:NEED-T-TYPE-CALCIUM&disp:consistent_mechanism_candidate&openall:1")
        self.assertIn("Discriminating experiment named", d)
        d2 = self.dom("#f=q:bumetanide&openall:1")
        self.assertRegex(d2, r'href="\.\./cards/[A-Za-z0-9_-]+\.card\.json"')


@unittest.skipUnless(HAVE_DATA, "module data absent")
class Curated(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full = rv.build(DR, "full")
        cls.share = rv.build(DR, "shareable")
        cls.PF, cls.PS = embedded(cls.full), embedded(cls.share)
        cls.allow = json.loads((DR / "view/shareable_sources.json").read_text())

    def test_action_stated_records_are_headlined_before_the_larger_target_listed_count(self):
        cc = json.loads((DR / "coverage/coverage_summary.json").read_text())["catalogue_coverage"]
        self.assertLess(cc["records_with_stated_action_on_a_need_target"], cc["union_headline_records"])
        self.assertEqual(sum(v for k, v in cc["headline_records_by_strongest_relation"].items() if k.startswith("action_stated")), cc["records_with_stated_action_on_a_need_target"])
        for html in (self.full, self.share):
            self.assertLess(html.index('data-step="records_with_action"'), html.index('data-step="records_with_link"'))
            self.assertNotIn("with a documented link", html)
            self.assertIn("Famiglie con un bersaglio elencato", html)

    def test_units_never_conflated(self):
        n = static_numbers(self.full)
        cur = self.PF["cur"]
        self.assertEqual(n["cur.needs"], "22")
        self.assertEqual(n["cur.cards"], str(len(cur["cands"])))
        self.assertNotEqual(n["cur.cards"], n["funnel.records"])
        for key, unit in (("cur.needs", "bisogni"), ("cur.cards", "schede candidato"), ("cur.threads", "filoni biologici")):
            self.assertRegex(self.full, rf'data-k="{re.escape(key)}"[^<]*</b></span><span class="u">{re.escape(unit)}<')
        # the funnel graphic: each step carries its own unit, in the order records, families, families, families, cards; no step mixes two units
        g1 = self.full[self.full.index('id="g1"'):self.full.index('id="g2"')]
        steps = re.findall(r'<li data-step="(\w+)">.*?<span class="unit">(\w+)</span>', g1, re.S)
        self.assertEqual(steps, [("records", "record"), ("families", "famiglie"), ("families_with_link", "famiglie"), ("families_with_action", "famiglie"), ("cards", "schede")])
        sm = json.loads((DR / "coverage/coverage_summary.json").read_text())["catalogue_coverage"]
        st = static_numbers(self.full)
        self.assertEqual(st["funnel.families_with_link"], str(sm["families_with_documented_link_to_a_need"]))
        self.assertEqual(st["funnel.families_with_action"], str(sm["families_with_stated_action_on_a_need_target"]))
        self.assertIn("le schede non sono una frazione delle famiglie", g1)
        self.assertIn("Una famiglia non è un farmaco distinto", g1)
        # record-level numbers are named as records and are never printed in a family row
        self.assertIn(f'{sm["records_with_stated_action_on_a_need_target"]:,}'.replace(",", ".") + " record con azione dichiarata", g1)
        self.assertIn("non si sommano né si confrontano come un solo numero", self.full)

    def test_access_percentages_state_their_denominator(self):
        g2 = self.full[self.full.index('id="g2"'):self.full.index('id="g3"')]
        st = json.loads((DR / "catalog/catalog_stats.json").read_text())
        tot = st["entries_total"]
        self.assertIn(f"{tot:,}".replace(",", "."), g2)
        for k, v in st["access_category_overlapping_counts"].items():
            self.assertIn(f'data-access="{k}"', g2)
            self.assertIn(f"{round(100.0 * v / tot, 1)}".replace(".", ",") + "%", g2)
        self.assertIn("Stati Uniti", g2)
        self.assertIn("non si sommano", g2)

    def test_matrix_cells_carry_letter_and_text_and_pathway_counts_are_not_shown(self):
        g3 = self.full[self.full.index('id="g3"'):self.full.index('id="g4"')]
        cells = re.findall(r'<td data-label="[^"]*"><span class="grp ([fcp][123])"[^>]*>([FCP][123])</span><span class="mxt">([^<]+)</span>', g3)
        links = sum(len(c["links"]) for c in self.PF["cur"]["cands"])
        self.assertEqual(len(cells), links)
        for cls, letter, word in cells:
            self.assertEqual(cls.upper(), letter)
            self.assertEqual(word, rv.UI_IT["g3_cell_" + letter])
        blob = self.full[self.full.index('id="charts"'):self.full.index('id="navigate"')]
        self.assertNotRegex(blob, r"(?i)pathways?\s*(count|touched)|n_pathway|vie biologiche toccate:\s*\d")

    def test_two_goals_and_track_are_separate_dimensions(self):
        n = static_numbers(self.full)
        d, p = n["cur.goal.deep_recovery.cards"], n["cur.goal.partial_benefit.cards"]
        self.assertEqual(int(d) + int(p), len([c for c in self.PF["cur"]["cands"] if c["goal"]]))
        self.assertEqual(int(n["cur.goal.deep_recovery.needs"]) + int(n["cur.goal.partial_benefit.needs"]), 22)
        self.assertEqual(self.full.count('class="goal '), 2)
        self.assertIn("Track (campo separato)", self.full)
        self.assertIn("2026-", re.search(r'data-k="meta.data_date" data-v="([^"]+)"', self.full).group(1))

    def test_positions_are_reasoned_and_unscored(self):
        cur = self.PF["cur"]
        ids = {g["id"] for g in cur["groups"]}
        self.assertEqual(ids, {"F1", "F2", "F3", "C1", "C2", "C3", "P1", "P2", "P3"})
        for c in cur["cands"]:
            for nid, l in c["links"].items():
                self.assertIn(l["group"], ids)
                self.assertEqual(len(l["reasons"]), 8)
                self.assertTrue(l["criteria"])
                self.assertIn("Criteria", [r[0] for r in l["reasons"]])
                if l["group"] == "F1":
                    self.assertGreater(l["n_w"], 0)
                if c["abstention"]:
                    self.assertEqual(l["group"], "P1")
        blob = json.dumps(cur)
        for bad in ('"score"', '"rank"', '"probability"', '"cure'):
            self.assertNotIn(bad, blob)
        self.assertIn("no score, no probability and no cure ranking", self.full)

    def test_overview_position_is_the_set_of_need_positions_never_best_of(self):
        """(a) a card has no single/global group; its overview entry is the set of its need-level positions."""
        cur = self.PF["cur"]
        multi = 0
        for c in cur["cands"]:
            self.assertNotIn("group", c)
            self.assertEqual(c["positions"], rv.overview_positions(c["links"]))
            self.assertEqual(set(c["positions"]), {l["group"] for l in c["links"].values()})
            multi += len(c["positions"]) > 1
        self.assertGreaterEqual(multi, 3)
        by = {c["id"]: c for c in cur["cands"]}
        # real cases whose needs differ: neither position may be dropped in favour of the other
        self.assertEqual(by["C04_aav9_endpoint_families"]["positions"], ["F1", "C2"])
        self.assertEqual(by["EB-VGB-01"]["positions"], ["C2", "P3"])
        self.assertEqual(by["H02_gabaat_inactivator_myelin_exposure"]["positions"], ["F3", "C3", "P3"])
        # synthetic: best-of would say F1; the set keeps the counter-evidence position visible
        self.assertEqual(rv.overview_positions({"n1": {"group": "F1"}, "n2": {"group": "C2"}, "n3": {"group": "F1"}}), ["F1", "C2"])
        self.assertIn("never the best of them", self.full)

    def test_null_or_unfavourable_wwox_result_is_never_promoted_as_favourable(self):
        """(b) on real data and on synthetic facts."""
        for c in self.PF["cur"]["cands"]:
            for nid, l in c["links"].items():
                if l["result"] in ("null", "unfavourable", "mixed"):
                    self.assertTrue(l["group"].startswith("C"), (c["id"], nid, l["group"]))
                if l["group"].startswith("F"):
                    self.assertIn(l["result"], ("favourable", "none"))
        by = {c["id"]: c for c in self.PF["cur"]["cands"]}
        myc = [l for nid, l in by["D01_a51"]["links"].items() if "MYC" in nid]
        self.assertEqual(len(myc), 1)
        if myc:
            self.assertEqual(myc[0]["group"], "C1")   # the wild-type-only row counts neither way, so the null stands alone   # old rule: G1 because a readout in a WWOX system exists
        row = lambda kind, sign, comp="untreated_same_genotype", flags="": {"assertion_id": "a" + sign, "evidence_kind": kind, "sign": sign, "comparator": comp, "flags": flags}
        deep = {"anull": "complete_fulltext_read", "aharm": "complete_fulltext_read", "abenefit": "complete_fulltext_read", "amixed": "complete_fulltext_read"}
        for sign, exp in (("null", "C1"), ("harm", "C1"), ("mixed", "C2")):
            f = rv.classify_rows([row("readout_in_wwox_system", sign)], deep)
            self.assertEqual(rv.assign_need_position(f, False, True, True)[0], exp)
        f = rv.classify_rows([row("readout_in_wwox_system", "benefit"), row("readout_in_wwox_system", "null")], deep)
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "C2")
        f = rv.classify_rows([row("readout_in_wwox_system", "benefit")], deep)
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "F1")
        f = rv.classify_rows([row("readout_in_wwox_system", "benefit", comp="none_uncontrolled_case_report")], deep)
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "F2")
        # a depth-unknown favourable reading is thin, never controlled
        f = rv.classify_rows([row("readout_in_wwox_system", "benefit")], {})
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "F2")
        # an outside-WWOX harm signal with no favourable signal is counter-evidence, not a favourable hypothesis
        f = rv.classify_rows([row("safety_signal", "harm")], {})
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "C3")
        # abstention and missing next step beat everything
        f = rv.classify_rows([row("readout_in_wwox_system", "benefit")], deep)
        self.assertEqual(rv.assign_need_position(f, True, True, True)[0], "P1")
        self.assertEqual(rv.assign_need_position(f, False, False, True)[0], "P2")

    def test_counter_evidence_clarification_and_favourable_hypothesis_have_distinct_labels(self):
        """(c) two reasons, two visibly different labels, colours and kinds."""
        gs = rv.GROUPS
        fav = [g for g in gs if g["kind"] == rv.KIND_FAV]
        con = [g for g in gs if g["kind"] == rv.KIND_COUNTER]
        self.assertTrue(fav and con)
        for g in fav:
            self.assertIn("Favourable hypothesis", g["label"])
            self.assertNotIn("ounter", g["label"])
        for g in con:
            self.assertIn("Counter-evidence to clarify", g["label"])
            self.assertNotIn("avourable hypothesis", g["label"])
        self.assertEqual(len({g["label"].split(":")[1] for g in gs}), len(gs))
        self.assertFalse({g["id"] for g in fav} & {g["id"] for g in con})
        css = (DR / "view/assets/curated.css").read_text(encoding="utf-8")
        for g in gs:
            self.assertIn(".grp." + g["id"].lower(), css)
        for c in self.PF["cur"]["cands"]:
            for l in c["links"].values():
                self.assertEqual(l["kind"], rv.POS_BY_ID[l["group"]]["kind"])

    def test_p11fix_tool_compound_outside_counter_neutral_rows_carrier_and_criteria(self):
        by = {c["id"]: c for c in self.PF["cur"]["cands"]}
        link = lambda cid, frag: [l for n, l in by[cid]["links"].items() if frag in n][0]
        # (1) a tool compound is capped at F2 and tagged
        f01 = link("F01_glutamate_receptor_node", "EXCITATORY")
        self.assertEqual(f01["group"], "F2")
        self.assertIn("tool compound, not a candidate drug", f01["tags"])
        # (2) F positions carry the outside-WWOX counter-evidence tag; the F1 definition says what the test covers
        self.assertTrue(any("outside WWOX" in t for t in link("H01_apinocaltamide_ttype", "T-TYPE")["tags"]))
        self.assertIn("WWOX-system result beside it", rv.POS_BY_ID["F1"]["why"])
        # (3) wild-type-only comparison rows flagged not_a_recovery_comparison count neither way
        r = lambda sign, flags="", comp="untreated_same_genotype", i="x": {"assertion_id": i, "evidence_kind": "genotype_comparison_vs_wild_type", "sign": sign, "comparator": comp, "flags": flags}
        f = rv.classify_rows([r("normalised_vs_wild_type", "not_a_recovery_comparison", i="a"), {"assertion_id": "b", "evidence_kind": "readout_in_wwox_system", "sign": "null", "comparator": "untreated_same_genotype", "flags": ""}], {})
        self.assertEqual(f["result"], "null")
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "C1")
        self.assertEqual(f["n_not_recovery"], 1)
        # (4) F1 is named for what it is and the page names the carrying row
        self.assertIn("controlled WWOX readout", rv.POS_BY_ID["F1"]["label"])
        self.assertNotIn("firm", rv.POS_BY_ID["F1"]["label"].lower())
        c01 = link("C01_aav9_wwox", "GENE-ADDITION")
        self.assertEqual(c01["group"], "F1")
        self.assertIn("DR-C01-001", c01["carrier"][0])
        self.assertIn("high_dose_only", c01["carrier"][0])
        c04 = link("C04_aav9_endpoint_families", "GENE-ADDITION")
        self.assertEqual(len(c04["carrier"]), 1)
        self.assertIn("DR-AAV-GFAP-P5HD", c04["carrier"][0])
        self.assertTrue(any("not normalised vs wild type" in t and "GFAPAREA-LD" in t for t in c04["tags"]))
        # (5) the F2 criteria say which part of the F1 test failed
        etx = [x for x in link("EB-ETX-01", "SEIZURE")["criteria"]]
        met = {x["text"].split(" (found")[0]: x["met"] for x in etx}
        self.assertTrue(met["a favourable WWOX readout has an untreated same-genotype comparator"])
        self.assertFalse(met["a favourable WWOX readout carries no weakening flag"])
        self.assertTrue(any("(found: " in x["text"] for x in etx))

    def test_every_position_prints_criteria_met_and_not_met(self):
        for c in self.PF["cur"]["cands"]:
            for l in c["links"].values():
                txt = dict(l["reasons"])["Criteria"]
                self.assertTrue(txt.startswith("met: "))
                self.assertIn(". Not met: ", txt)

    def test_scope_labels_distinct_and_known(self):
        cur = self.PF["cur"]
        labels = [s["label"] for s in cur["scopes"]]
        self.assertEqual(len(labels), len(set(labels)))
        codes = {s["code"] for s in cur["scopes"]}
        for c in cur["cands"]:
            self.assertLessEqual({a["scope"] for a in c["asserts"]}, codes)
        for want in ("WWOX experiment in a DEE system", "WWOX biology in another context", "Other-disease precedent", "Computational result", "Unverified hypothesis"):
            self.assertIn(want, labels)

    def test_public_identifiers_attached(self):
        cur = self.PF["cur"]
        etx = next(c for c in cur["cands"] if c["id"] == "EB-ETX-01")
        self.assertIn("32000863", [p["id"] for p in etx["pmids"]])
        self.assertIn("CHEMBL696", etx["chembl"])
        for c in cur["cands"]:
            for p in c["pmids"]:
                self.assertRegex(p["id"], r"^\d{6,8}$")

    def test_allowlist_is_the_initial_policy(self):
        self.assertEqual(set(self.allow["dgidb_claim_sources"]), {"NCI", "FDA", "CIViC", "DoCM"})
        self.assertEqual(set(self.allow["name_sources"]), {"MATRIX list name", "openFDA NDC single-ingredient active_ingredient name"})
        for v in list(self.allow["dgidb_claim_sources"].values()) + list(self.allow["name_sources"].values()):
            self.assertTrue(v["licence"] and v["attribution"])

    def test_shareable_embeds_no_non_allowlisted_row(self):
        ok = {"DGIdb:" + k for k in self.allow["dgidb_claim_sources"]}
        for p in self.PS["pairs"]:
            for t in p["l1"][3]:
                self.assertIn(t, ok)
            if "p" in p:
                for t in p["p"]["cr"]["dir"][1]:
                    self.assertIn(t, ok)
        for e in self.PS["excluded_detail"]:
            self.assertEqual(e["genes"], [])
            self.assertIn("detail withheld", e["reason"])
        withheld = [r for r in self.PS["rows"] if r.get("w")]
        self.assertGreater(len(withheld), 1000)
        allowed_names = {c["short"] for c in self.PS["cur"]["cands"]}
        for r in withheld:
            self.assertEqual(r["st"], [])
            self.assertEqual(r["mod"], [])
            self.assertTrue(r["name"] in allowed_names or re.fullmatch(r"(CHEMBL\d+|DGIDB:[0-9a-f]+|[A-Za-z0-9_.:-]+)", r["name"]), r["name"])
        # compound names that only third-party rows carry must be absent from the shareable page and present in the full one
        cm = json.loads((DR / "coverage/coverage_matrix.json").read_text())
        names = [r["name"] for r in cm["rows"] if r.get("origin") == ["dgidb_only"] and r["name"].isalpha() and len(r["name"]) > 7 and not r.get("cards")][:40]
        self.assertTrue(names)
        for nm in names:
            self.assertNotIn(f'"name":"{nm}"', self.share)
        self.assertTrue(any(f'"name":"{nm}"' in self.full for nm in names))
        sources = set()
        for a in rv.read_associations(DR):
            if rv.tag_allowed(rv.assoc_tag(a), self.allow):
                sources.add(rv.assoc_tag(a))
        foot = self.PS["cur"]["footer"]
        for e in foot["embedded"]:
            self.assertTrue(e["licence"] and e["attribution"])
        embedded_labels = " ".join(e["label"] for e in foot["embedded"])
        self.assertNotIn("ChEMBL", embedded_labels)
        self.assertIn("ChEMBL", " ".join(e["label"] for e in foot["counts_only"]))
        self.assertIn('id="attribution"', self.share)
        self.assertIn("CC BY-SA 3.0", self.share)

    def test_shareable_footer_lists_what_is_embedded(self):
        labels = [e["label"] for e in self.PS["cur"]["footer"]["embedded"]]
        self.assertTrue(any("NCI" in x for x in labels))
        for e in self.PS["cur"]["footer"]["embedded"]:
            if e.get("rows"):
                self.assertGreater(e["rows"], 0)
        self.assertEqual(self.PS["source"], "shareable")
        self.assertEqual(self.PF["source"], "full")

    def test_check_covers_both_sources(self):
        self.assertEqual(rv.main(["check"]), 0)
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "x.html"
            out.write_text("stale", encoding="utf-8")
            self.assertEqual(rv.main(["check", "--source", "shareable", "--out", str(out)]), 1)
            self.assertEqual(rv.main(["run", "--source", "shareable", "--out", str(out)]), 0)
            self.assertEqual(rv.main(["check", "--source", "shareable", "--out", str(out)]), 0)
            self.assertEqual(rv.main(["check", "--source", "full", "--out", str(out)]), 1)

    def test_no_third_party_name_in_full_only_fields_of_shareable_actions(self):
        for c in self.PS["cur"]["cands"]:
            for a in c["actions"]:
                self.assertIn("target", a)


@unittest.skipUnless(HAVE_DATA, "module data absent")
class CuratedBrowser(Browser):
    def test_export_card_has_public_identifiers(self):
        d = self.dom("#export=EB-ETX-01")
        area = d[d.index('id="export-area"'):]
        self.assertIn("exporting", d)
        self.assertIn("https://pubmed.ncbi.nlm.nih.gov/32000863/", area)
        self.assertIn("PMID 32000863", area)
        self.assertIn("CHEMBL696", area)
        self.assertIn("Data dei dati:", area)
        self.assertIn("Perimetro:", area)
        self.assertNotIn("deepdive_manifests", area)
        self.assertNotRegex(area, r'href="\.\./')

    def test_candidate_profile_five_answers_and_scope_labels(self):
        d = self.dom("#c=need:NEED-T-TYPE-CALCIUM")
        for q in ("1. Perché è in elenco", "2. Risultato in WWOX", "3. Precedente esterno o previsione", "4. Evidenza contraria", "5. Evidenza mancante", "6. Prossimo passo"):
            self.assertIn(q, d)
        self.assertIn("Esperimento WWOX in un sistema DEE", d)
        self.assertIn("Precedente in un'altra malattia", d)

    def test_filters_narrow_the_curated_views(self):
        d = self.dom("#c=goal:deep_recovery")
        m = re.search(r'id="c-count"[^>]*>(\d+) di (\d+) bisogni e (\d+) di (\d+) schede', d)
        needs = [n for n in self.P["cur"]["needs"] if n["goal"] == "deep_recovery"]
        cands = [c for c in self.P["cur"]["cands"] if c["goal"] == "deep_recovery"]
        self.assertEqual((int(m.group(1)), int(m.group(3))), (len(needs), len(cands)))

    def test_ranking_groups_rendered_with_reasons(self):
        d = self.dom("#c=need:NEED-WWOX-GENE-ADDITION")
        self.assertIn('data-group="F1"', d)
        self.assertIn("criteria met and not met", d)

    def test_comparison_shows_opposed_actions_and_no_synergy(self):
        page = (Path(self.tmp.name) / "v.html").read_text(encoding="utf-8")
        m = re.search(r'(<script id="data" type="application/json">)(.*?)(</script>)', page, re.S)
        P = json.loads(m.group(2).replace("<\\/", "</").replace("<\\!--", "<!--"))
        by = {c["id"]: c for c in P["cur"]["cands"]}
        by["EB-ETX-01"]["actions"].append({"need": "NEED-T-TYPE-CALCIUM", "target": "CACNA1G", "action": "down", "cons": "opposed", "n": 1})
        by["H01_apinocaltamide_ttype"]["actions"].append({"need": "NEED-T-TYPE-CALCIUM", "target": "CACNA1G", "action": "up", "cons": "consistent", "n": 1})
        j = json.dumps(P, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "<\\!--")
        h2 = Path(self.tmp.name) / "opp.html"
        h2.write_text(page[: m.start(2)] + j + page[m.end(2):], encoding="utf-8")
        d = self.dom("#compare=EB-ETX-01,H01_apinocaltamide_ttype", html=h2)
        self.assertRegex(d, r'data-opposed="[2-9]"')
        self.assertIn("OPPOSTA alla direzione voluta", d)
        self.assertIn("aumenta mentre", d)
        self.assertIn("Non si inferisce alcuna sinergia", d)


class ItalianFix(unittest.TestCase):
    """P12 verification fixes: counts, wording, header codes, glossary."""

    @classmethod
    def setUpClass(cls):
        if not HAVE_DATA:
            raise unittest.SkipTest("module data absent")
        cls.page = rv.build(DR, "shareable")
        cls.P = embedded(cls.page)

    def test_goal_tiles_count_every_position_link(self):
        cur = self.P["cur"]
        n_links = sum(len(c["links"]) for c in cur["cands"])
        self.assertEqual(n_links, 48)
        goals = re.findall(r'<div class="goal (?:deep|partial)".*?<span class="mini mut">\((\d+)\)</span></div></div>', self.page, re.S)
        self.assertEqual(sum(map(int, goals)), n_links)
        self.assertIn("I 48 legami candidato-bisogno sono contati tutti", self.page)

    def test_no_raw_status_code_in_the_header_and_italian_labels(self):
        head = self.page[:self.page.index('<nav ')]
        for code in ("STALE_EXPORT", "PARTIAL", "NOT_FETCHED", "FAILED"):
            self.assertNotIn(code, head)
        self.assertIn("esportazione non aggiornata", head)
        self.assertIn("parziale", head)

    def test_wording_fixes_hold(self):
        txt = json.dumps(rv.UI_IT, ensure_ascii=False) + json.dumps(rv.POS_IT, ensure_ascii=False)
        for bad in ("prima di sperare", "Controprova", "controprova", "Prova mancante", "e o nessun", "disegnare un test", "una indicazione", "Perché lo studiamo", "Nessun risultato di assenza"):
            self.assertNotIn(bad, txt)
        self.assertIn("prima di considerare l'ipotesi", txt)
        self.assertIn("progettare un test", txt)
        self.assertIn("in sperimentazione", rv.UI_IT["acc_experimental"])
        self.assertIn("ipotesi dal bersaglio, nessun test in WWOX", rv.UI_IT["g3_cell_F3"])
        self.assertIn("ipotesi, esito WWOX debole", rv.UI_IT["g3_cell_F2"])
        self.assertIn("prevalentemente USA", rv.UI_IT["g2_h"])
        self.assertIn("non specifiche di un paese", rv.UI_IT["g2_note"])

    def test_export_explains_internal_tokens_and_does_not_mix_languages(self):
        self.assertIn("CLAIM 031", rv.UI_IT["ex_lim_4"])
        self.assertIn("non sono consultabili fuori dal repository", rv.UI_IT["ex_lim_4"])
        js = (DR / "view/assets/curated.js").read_text(encoding="utf-8")
        self.assertIn("T.ex_lim_card", js)
        self.assertEqual(rv.UI_IT["ex_lim_card"].count("inglese"), 1)

    def test_wwox_material_is_kept_out_of_the_external_precedent_section(self):
        js = (DR / "view/assets/curated.js").read_text(encoding="utf-8")
        self.assertIn("wwoxAssert", js)
        self.assertIn("T.q2_other", js)

    def test_readme_has_no_stale_family_count(self):
        self.assertNotIn("603 families", (DR / "view/README.md").read_text(encoding="utf-8"))


class Italian(unittest.TestCase):
    """The physician-facing orientation text is Italian data (UI_IT and its companions), complete for every key the page uses."""

    def test_every_token_and_script_key_has_an_italian_string(self):
        assets = DR / "view/assets"
        toks = set(re.findall(r"\{\{(\w+)\}\}", (assets / "curated.html").read_text(encoding="utf-8")))
        js = (assets / "curated.js").read_text(encoding="utf-8")
        keys = set(re.findall(r"\bT\.([A-Za-z_0-9]+)\b", js))
        dyn = {"pos", "scopeL", "goalL", "thread", "need", "statusL", "countryL", "crit"}
        for k in (toks | keys) - dyn:
            self.assertIn(k, rv.UI_IT, f"no Italian string for {k}")
            self.assertTrue(str(rv.UI_IT[k]).strip(), k)
        src = Path(rv.__file__).read_text(encoding="utf-8")
        for k in set(re.findall(r'U\["([a-z_0-9A-Z]+)"\]', src)):
            self.assertIn(k, rv.UI_IT, k)
        for k in ("act_down", "act_up", "act_unresolved", "cons_consistent", "cons_opposed", "cons_direction_unresolved", "dir_restore", "dir_down", "dir_up", "dir_uncertain", "acc_supplement", "acc_OTC", "acc_prescription", "acc_experimental", "acc_unknown/unverified"):
            self.assertIn(k, rv.UI_IT)
        for k in ("g3_cell_F1", "g3_cell_F2", "g3_cell_F3", "g3_cell_C1", "g3_cell_C2", "g3_cell_C3", "g3_cell_P1", "g3_cell_P2", "g3_cell_P3", "res_favourable", "res_mixed", "res_null", "res_unfavourable", "res_unresolved", "res_none"):
            self.assertIn(k, rv.UI_IT)

    def test_italian_covers_positions_scopes_needs_threads_goals_criteria(self):
        self.assertEqual(set(rv.POS_IT), {g["id"] for g in rv.GROUPS})
        for v in rv.POS_IT.values():
            self.assertTrue(v["short"] and v["label"] and v["plain"])
        self.assertEqual(set(rv.SCOPE_IT), {c for c, _, _ in rv.SCOPES})
        self.assertEqual(set(rv.GOALS_IT), set(rv.GOALS))
        self.assertTrue({"WWOX restoration", "Stress signalling and metabolism", "Network excitability", "Signalling", "Development and glia", "Symptom-level"} <= set(rv.THREAD_IT))
        if HAVE_DATA:
            P = rv.build_payload(DR)["cur"]
            self.assertEqual({n["id"] for n in P["needs"]}, set(rv.NEED_IT))
            self.assertEqual({t["id"] for t in P["threads"]}, set(rv.THREAD_IT))
            self.assertLessEqual({c["status"] for c in P["cands"]}, set(rv.STATUS_IT))
            self.assertLessEqual({c["country"] for c in P["cands"]}, set(rv.COUNTRY_IT))
            seen = {x["text"].split(" (found")[0] for c in P["cands"] for l in c["links"].values() for x in l["criteria"]}
            self.assertLessEqual(seen, set(rv.CRIT_IT))

    def test_italian_strings_are_not_english_placeholders(self):
        for k, v in rv.UI_IT.items():
            if isinstance(v, str):
                self.assertNotRegex(v, r"\b(the|which|with the|and the)\b", k)

    def test_first_screen_is_italian_and_orients(self):
        if not HAVE_DATA:
            self.skipTest("module data absent")
        page = rv.build(DR, "shareable")
        head = page[:page.index('id="charts"')]
        for must in ("Panoramica", "Filoni biologici", "Motivo della priorità", "Tipo di evidenza osservata nei bisogni", "Lacuna decisiva", "Composti e interventi da studiare",
                     "Recupero ampio e duraturo", "Beneficio parziale utile", "Track (campo separato)", "non consiglio medico", "Dettagli tecnici"):
            self.assertIn(must, head)
        # versions, hashes and regeneration live only in the drill-down
        first = page[:page.index('<details id="technical"')]
        for tech in ("sha256", "Input digests", "repurposing_coverage.py run", "schema legend"):
            self.assertNotIn(tech, first)
        self.assertIn('<details id="technical"', page)
        self.assertTrue(page.startswith('<!doctype html>\n<html lang="it">'))


@unittest.skipUnless(HAVE_DATA, "module data absent")
class Titles(unittest.TestCase):
    def test_cache_covers_every_referenced_pmid_and_builder_is_offline(self):
        have = json.loads((DR / rv.TITLES_NAME).read_text(encoding="utf-8"))["titles"]
        ids = rv.referenced_pmids(DR)
        self.assertEqual([i for i in ids if i not in have], [])
        for i in ids:
            self.assertTrue(have[i]["title"])
        cur = rv.build_payload(DR)["cur"]
        self.assertTrue(all(p["title"] for c in cur["cands"] for p in c["pmids"]))

    def test_refresh_is_batched_keyless_and_sends_no_contact_string(self):
        calls, urls = [], []

        def fake(ids):
            calls.append(len(ids))
            return {i: {"title": "t" + i, "journal": "J", "year": "2020"} for i in ids}
        with tempfile.TemporaryDirectory() as td:
            dr = Path(td)
            (dr / "view").mkdir()
            doc = rv.refresh_titles(dr, [str(10000000 + i) for i in range(250)], fetch=fake, sleep=0)
            self.assertEqual(calls, [100, 100, 50])
            self.assertEqual(len(doc["titles"]), 250)
            self.assertEqual(rv.refresh_titles(dr, [str(10000000 + i) for i in range(250)], fetch=fake, sleep=0)["titles"].keys(), doc["titles"].keys())
            self.assertEqual(calls, [100, 100, 50])   # nothing missing: no new call

        class R:
            def __enter__(s): return s
            def __exit__(s, *a): return False
            def read(s): return b'{"result":{}}'

        def opener(req, timeout=0):
            urls.append((req.full_url, dict(req.header_items())))
            return R()
        rv.esummary_batch(["1", "2"], opener=opener)
        url, hdr = urls[0]
        self.assertNotRegex(url, r"[?&](email|tool|api_key)=")
        self.assertNotRegex(json.dumps(hdr), r"[\w.+-]+@[\w-]+\.")
        self.assertGreaterEqual(rv.ESUMMARY_SLEEP, 0.4)
        self.assertEqual(rv.ESUMMARY_BATCH, 100)


class RulesUntouched(unittest.TestCase):
    def test_position_rules_are_byte_identical_to_the_verified_revision(self):
        import hashlib
        import inspect
        h = hashlib.sha256((inspect.getsource(rv.classify_rows) + inspect.getsource(rv.assign_need_position) + inspect.getsource(rv.overview_positions)).encode()).hexdigest()[:16]
        self.assertEqual(h, "244882c7cd5d1965", "the F/C/P rules changed: this view only displays them (IT5 P11 verified revision)")


@unittest.skipUnless(HAVE_DATA, "module data absent")
class RealViewports(unittest.TestCase):
    """Device-metrics emulation over the DevTools protocol (no sandbox flag): the page's own innerWidth and scrollWidth are measured at 360 and 390 px."""

    def test_no_horizontal_overflow_at_360_and_390(self):
        if not rv.find_chromium():
            self.skipTest("no Chromium binary: viewports were NOT measured")
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "v.html"
            f.write_text(rv.build(DR, "shareable"), encoding="utf-8")
            try:
                res = rv.measure_viewports(f, widths=[360, 390])
            except Exception as e:   # the browser could not be driven here
                self.skipTest("viewport emulation unavailable: " + str(e)[:120])
        self.assertTrue(res)
        for m in res:
            if m["scenario"].startswith("print"):
                continue
            self.assertEqual(m["ready"], "1", m)
            self.assertLessEqual(m["scrollWidth"], m["requested"], (m["scenario"], m["mobile"], m["offenders"]))
            if not m["mobile"]:
                self.assertEqual(m["innerWidth"], m["requested"])
            if m["scenario"] == "first_screen" and m["mobile"]:
                self.assertLess(m["legendBottom"], dict((w, h) for w, h, _ in rv.VIEWPORTS)[m["requested"]], "the F/C/P legend must sit above the fold")


if __name__ == "__main__":
    unittest.main(verbosity=1)
