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
            self.assertEqual(myc[0]["group"], "C2")   # IT6 P2: A51 against the untreated knockout is a favourable progenitor row (Supplementary Fig. 7F); the downstream layer-neuron null stands beside it
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
        # IT6 P2 (V5): n = 5, single channel, "limited cohort" is the same flag as the ethosuximide experiment, so C01 is F2 and C04 carries the need
        c01 = link("C01_aav9_wwox", "GENE-ADDITION")
        self.assertEqual(c01["group"], "F2")
        self.assertEqual(c01["carrier"], [])
        c04 = link("C04_aav9_endpoint_families", "GENE-ADDITION")
        # IT6 P2: the survival row carries its untreated-knockout comparator (Figure 3B caption) and a text statement; the panel-only motor and GFAP rows are graphical; partial benefits never carry F1
        self.assertEqual([c.split(":")[0] for c in c04["carrier"]], ["DR-AAV-SURV-HD"])
        self.assertTrue(any("not normalised vs wild type" in t and "GFAPAREA-LD" in t for t in c04["tags"]))
        # (5) the F2 criteria say which part of the F1 test failed
        etx = [x for x in link("EB-ETX-01", "SEIZURE")["criteria"]]
        met = {x["text"].split(" (found")[0]: x["met"] for x in etx}
        self.assertTrue(met["a favourable WWOX readout has an untreated same-genotype comparator"])
        self.assertFalse(met["a favourable WWOX readout carries no reading-limit flag"])   # graphical reading
        self.assertFalse(met["a favourable WWOX readout carries no design-limit flag"])   # one experiment
        self.assertTrue(any("(found: " in x["text"] for x in etx))

    def test_it6_p2_review_rules(self):
        """IT6 P2: engagement nulls are counter-evidence; C3 and F3 read the same support; shallow basis, downstream endpoint and sibling-card counters are tags, not categories."""
        row = lambda kind, sign, i="a", flags="", card="X", need="N", subj="card": {"card_id": card, "need_id": need, "assertion_id": i, "evidence_kind": kind, "sign": sign, "comparator": "", "flags": flags, "subject": subj}
        # (1) a poor target-engagement assay is a counter row; a favourable one is a favourable outside signal for C3 as it already was for F3
        f = rv.classify_rows([row("target_engagement_assay", "null")], {})
        self.assertEqual(f["o_counter"], 1)
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "C3")
        f = rv.classify_rows([row("target_engagement_assay", "benefit", i="b"), row("readout_other_disease", "null", i="c")], {})
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "F3")
        self.assertEqual(f["o_counter"], 1)
        # (2) the shallow tag: no signed row behind the position read beyond abstract/query/unknown depth
        rr = [row("readout_other_disease", "benefit", i="p"), row("readout_other_disease", "benefit", i="q"), row("safety_signal", "harm", i="h")]
        self.assertTrue(rv.display_facts(rr, {"p": "abstract_only", "q": "queried_not_full_read", "h": "complete_fulltext_read"})["shallow"]["F_o"])   # V4: a fully read harm row does not hide shallow favourable rows
        self.assertFalse(rv.display_facts(rr, {"p": "abstract_only", "q": "partial_fulltext_read", "h": "complete_fulltext_read"})["shallow"]["F_o"])
        self.assertFalse(rv.display_facts(rr, {"p": "abstract_only", "q": "queried_not_full_read", "h": "complete_fulltext_read"})["shallow"]["C_o"])
        # V3: a partial benefit never carries F1
        f = rv.classify_rows([row("readout_in_wwox_system", "partial_benefit", i="pb")], {"pb": "complete_fulltext_read"})
        self.assertEqual(rv.assign_need_position(f, False, True, True)[0], "F2")
        # (3) a signed WWOX row flagged as downstream of the need is named
        self.assertEqual(rv.display_facts([row("readout_in_wwox_system", "null", i="d", flags="endpoint_downstream_of_need")], {})["downstream"], ["d"])
        # (4) sibling counters: same compound, same need, other card; never the card itself, never another need
        pert = [row("safety_signal", "harm", i="h1", card="H", need="N1", subj="CHEMBL1"), row("safety_signal", "harm", i="h2", card="H", need="N2", subj="CHEMBL1"),
                row("readout_other_disease", "benefit", i="b1", card="V", need="N1", subj="card"), row("readout_other_disease", "null", i="n1", card="W", need="N1", subj="CHEMBL9")]
        links = {"V": {"links": [{"chembl_id": "CHEMBL1"}]}}
        self.assertEqual(rv.sibling_counters("V", "N1", pert, links), {"H": 1})
        self.assertEqual(rv.sibling_counters("H", "N1", pert, links), {})
        # (5) on the real data
        by = {c["id"]: c for c in self.PF["cur"]["cands"]}
        link = lambda cid, frag: [l for n, l in by[cid]["links"].items() if frag in n][0]
        self.assertTrue(any("counter-evidence outside WWOX" in t for t in link("E02_ldh_inhibition", "LACTATE")["tags"]))
        self.assertEqual(link("H01_apinocaltamide_ttype", "SEIZURE")["group"], "F3")
        self.assertEqual(link("I01_pdk_inhibition_dca_premise_seizure_glycaemia", "LACTATE")["group"], "F3")
        self.assertTrue(any("same compound, other card H02" in t for t in link("EB-VGB-01", "MYELINATION")["tags"]))
        self.assertTrue(any("same compound, other card I01" in t for t in link("E03_pdk_inhibition_dca", "SEIZURE")["tags"]))
        self.assertTrue(any("downstream of the need" in t for t in link("D01_a51", "MYC")["tags"]))
        self.assertTrue(any("downstream of the need" in t for t in link("EB-ETX-01", "T-TYPE")["tags"]))   # V6
        # V4: the depth fact is a criterion, not a tag; E01 rests on four abstracts
        e01 = link("E01_isr_modulators", "ISR")
        self.assertFalse(any("reading depth" in t for t in e01["tags"]))
        self.assertTrue(any(x["text"].startswith("the signed rows behind this position were read beyond") and not x["met"] for x in e01["criteria"]))
        # V1 and V2: the two label corrections
        self.assertEqual(link("D01_a51", "MYC")["group"], "C2")
        self.assertEqual(link("EB-KD-01", "SEIZURE")["group"], "C2")

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
        # NCI moved to counts-only (IT5 P13): its terms were not read at NCI (P1 independent verification)
        self.assertEqual(set(self.allow["dgidb_claim_sources"]), {"FDA", "CIViC", "DoCM"})
        self.assertNotIn("NCI", self.allow["dgidb_claim_sources"])
        self.assertEqual(self.allow["claim_source_policy"]["NCI"]["class"], "C")
        self.assertEqual({k for k, v in self.allow["claim_source_policy"].items() if v["class"] == "A"}, {"FDA", "CIViC", "DoCM"})
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
        self.assertFalse(any("NCI" in x for x in labels), "NCI is counts-only")
        self.assertTrue(any("CIViC" in x for x in labels))
        self.assertIn("NCI Cancer Gene Index (via DGIdb)", " ".join(e["label"] for e in self.PS["cur"]["footer"]["counts_only"]))
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
class ShareableAudit(unittest.TestCase):
    """IT5 P13: the allowlist is a mechanism; the audit is the proof. It reads the bytes of the shareable output and compares them with the FULL catalogue.
    The mutation tests inject third-party rows into the shareable bytes and require the audit to fail on each."""

    @classmethod
    def setUpClass(cls):
        import repurposing_shareable_audit as au
        import repurposing_shareable_package as pk
        cls.au, cls.pk = au, pk
        cls.share = rv.build(DR, "shareable")
        cls.ref = au.Reference(DR)
        cls.allow_pol = json.loads((DR / "view/shareable_sources.json").read_text())["prose_policy"]

    # ---- helpers
    def audit(self, text):
        rep, _ = self.au.audit_html(text, DR, self.ref)
        return rep

    def mutate(self, fn):
        P = embedded(self.share)
        fn(P)
        data = json.dumps(P, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "<\\!--")
        return re.sub(r'(<script id="data" type="application/json">).*?(</script>)', lambda m: m.group(1) + data + m.group(2), self.share, count=1, flags=re.S)

    def kinds(self, text):
        return {v["kind"] for v in self.audit(text).violations}

    def dtc_only_name(self):
        import gzip
        with gzip.open(DR / "catalog/catalog.jsonl.gz", "rt", encoding="utf-8") as fh:
            for line in fh:
                e = json.loads(line)
                cs = {t.get("claim_source") for t in e.get("targets") or []}
                n = e.get("name") or ""
                if e["origin"] == "dgidb_only" and cs == {"DTC"} and n.isalpha() and len(n) >= 8 and self.au.norm(n) not in self.ref.own_grams:
                    return n, e["id"]
        self.fail("no DTC-only compound found")

    # ---- the real output
    def test_shareable_output_passes_the_audit(self):
        rep = self.audit(self.share)
        self.assertEqual(rep.violations, [], rep.violations[:5])
        self.assertGreater(len(self.ref.names), 100000)       # the reference is the whole catalogue, not a sample
        self.assertGreater(len(self.ref.texts), 1000)
        self.assertGreater(len(self.ref.ident), 10000)
        self.assertEqual(self.ref.unclassified_sources, [])
        self.assertEqual(self.ref.assoc_unverified, 0)
        self.assertEqual(self.ref.policy_mismatch, [])

    def test_committed_shareable_output_and_package_pass(self):
        for f in (DR / "view/index_shareable.html", DR / "view/shareable_package/index.html"):
            if f.exists():
                self.assertEqual(self.audit(f.read_text(encoding="utf-8")).violations, [], str(f))

    def test_full_build_fails_the_audit(self):
        k = self.kinds(rv.build(DR, "full"))
        self.assertIn("not-a-shareable-build", k)
        self.assertTrue(k & {"forbidden-name", "pair-link-source-not-class-A", "field-must-be-empty"}, k)

    def test_every_payload_field_has_a_provenance_class(self):
        rep = self.audit(self.share)
        self.assertEqual([v for v in rep.violations if v["kind"] == "unclassified-field"], [])
        classes = {r["class"] for r in rep.rules.values()}
        self.assertTrue({"OWN", "UI", "BIBLIO", "ID", "COUNT", "SRC_A", "SRC_META"} <= classes, classes)
        self.assertEqual(rep.info["identifiers"]["NCT"], 0)

    def test_string_audit_found_a_real_leak_that_is_now_fixed(self):
        # IT5 P13: compound names and genes of DGIdb alias-risk rows were embedded in funnel.excluded_rows
        P = embedded(self.share)
        for x in P["funnel"]["excluded_rows"]["alias_risk_rows_unresolved"]:
            self.assertEqual(set(x), {"catalogue_id"})
        self.assertNotIn("Celecoxib", self.share.split('<script id="data"')[0])

    # ---- mutation: a third-party row injected into the shareable bytes must make the audit fail
    def test_mutation_class_c_compound_name_in_a_withheld_row(self):
        name, rid = self.dtc_only_name()
        t = self.mutate(lambda P: P["rows"][0].__setitem__("name", name))
        self.assertIn("forbidden-name", self.kinds(t))
        self.assertEqual(self.audit(self.share).violations, [])    # the unmutated bytes pass

    def test_mutation_class_c_name_in_free_text(self):
        name, rid = self.dtc_only_name()
        t = self.mutate(lambda P: P["cur"]["cands"][0].__setitem__("why", P["cur"]["cands"][0]["why"] + " " + name))
        self.assertIn("forbidden-name", self.kinds(t))

    def test_mutation_whole_class_c_row_with_attributes(self):
        name, rid = self.dtc_only_name()
        def f(P):
            r = P["rows"][0]
            r.pop("w", None)
            r.update(name=name, st=["approved_any_source"], mod=["small_molecule"], acc=["experimental"])
        k = self.kinds(self.mutate(f))
        self.assertTrue({"forbidden-name", "field-must-be-empty", "row-name-not-from-card-or-class-A-name-source", "access-category-not-class-A"} <= k, k)

    def test_mutation_non_allowlisted_claim_source_in_a_pair(self):
        for src in ("DGIdb:DTC", "DGIdb:NCI", "ChEMBL"):
            def f(P, src=src):
                p = next(q for q in P["pairs"] if q.get("l1"))
                p["l1"][2] = list(p["l1"][2]) + ["TP53"]
                p["l1"][3] = list(p["l1"][3]) + [src]
            k = self.kinds(self.mutate(f))
            self.assertIn("pair-link-source-not-class-A", k, src)
            self.assertIn("pair-target-not-backed-by-class-A-row", k, src)

    def test_mutation_chembl_mechanism_wording_and_third_party_identifiers(self):
        wording = next(w for w in self.ref.texts if len(w.split()) >= 4 and w not in self.ref.own_grams and not all(g in self.ref.own_grams for g in self.au.grams(w.split(), 3)))
        t = self.mutate(lambda P: P["cur"]["cands"][0].__setitem__("pharm", wording))
        self.assertIn("forbidden-wording", self.kinds(t))
        db = next(i for i, k in self.ref.ident.items() if k == "drugbank")
        atc = next(i for i, k in self.ref.ident.items() if k == "atc")
        for ident, kind in ((db, "drugbank"), (atc, "atc")):
            t = self.mutate(lambda P, ident=ident: P["cur"]["cands"][0].__setitem__("identity", "see " + ident))
            self.assertIn("forbidden-identifier:" + kind, self.kinds(t))

    def test_mutation_unclassified_field_repository_link_and_email(self):
        self.assertIn("unclassified-field", self.kinds(self.mutate(lambda P: P["rows"][0].__setitem__("extra", "x"))))
        self.assertIn("link-not-document-or-public-url", self.kinds(re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + '<a href="../cards/A01_pba_class.card.json">card</a>', self.share, count=1)))
        self.assertIn("e-mail-like-string", self.kinds(self.mutate(lambda P: P["cur"]["cands"][0].__setitem__("why", "write to " + "someone" + chr(64) + "example.org"))))

    def test_mutation_restoring_the_excluded_row_names(self):
        def f(P):
            P["funnel"]["excluded_rows"]["alias_risk_rows_unresolved"][0].update(compound="Celecoxib", gene="PDK1")
        self.assertIn("field-must-be-empty", self.kinds(self.mutate(f)))

    def test_mutation_of_the_policy_file_is_caught(self):
        # a temporary copy of the module with DTC wrongly added to the allowlist: the policy table (class C) and the allowlist disagree
        with tempfile.TemporaryDirectory() as td:
            dr = Path(td) / "dr"
            dr.mkdir()
            for p in DR.iterdir():
                if p.name != "view":
                    (dr / p.name).symlink_to(p)
            shutil.copytree(DR / "view", dr / "view", ignore=shutil.ignore_patterns("shareable_package", "preview", "index*.html"))
            pol = json.loads((dr / "view/shareable_sources.json").read_text())
            pol["dgidb_claim_sources"]["DTC"] = {"label": "DTC", "licence": "x", "url": None, "attribution": "x"}
            (dr / "view/shareable_sources.json").write_text(json.dumps(pol), encoding="utf-8")
            ref2 = self.au.Reference(dr)
            self.assertIn("DTC", ref2.policy_mismatch)
            # and an unclassified claim source fails closed
            pol["claim_source_policy"].pop("TTD")
            (dr / "view/shareable_sources.json").write_text(json.dumps(pol), encoding="utf-8")
            self.assertIn("TTD", self.au.Reference(dr).unclassified_sources)

    def test_cli_exit_codes_and_mutated_file(self):
        with tempfile.TemporaryDirectory() as td:
            good, bad = Path(td) / "good.html", Path(td) / "bad.html"
            good.write_text(self.share, encoding="utf-8")
            name, _ = self.dtc_only_name()
            bad.write_text(self.mutate(lambda P: P["rows"][0].__setitem__("name", name)), encoding="utf-8")
            self.assertEqual(rv.main(["audit-shareable", "--html", str(good), "--no-text"]), 0)
            self.assertEqual(rv.main(["audit-shareable", "--html", str(bad), "--no-text"]), 1)

    # ---- provenance of the cards' own text
    def test_text_overlap_catches_a_copied_passage_and_accepts_titles_and_short_quotes(self):
        passage = "the quick brown fox jumps over the lazy dog while the committee of seven scholars reviews the quarterly report on migratory birds crossing the northern sea in late autumn every single year"
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "a.txt").write_text("Intro. " + passage + " End.", encoding="utf-8")
            P = {"cur": {"cands": [{"pmids": [{"title": "Migratory birds crossing the northern sea in late autumn every single year"}],
                                    "why": passage[:200], "short": 'the authors write: "the committee of seven scholars reviews the quarterly report"', "ok": "nothing shared here at all, completely different words"}]}}
            res = self.au.text_overlap(P, [Path(td)])
            rep = self.au.Report()
            s = self.au.judge_text_overlap(res, rep)
            self.assertEqual(s["titles"], 1)
            self.assertEqual(len(s["short_marked_quotations"]) + len(s["attributed_quotations"]), 1)
            self.assertEqual(s["failures"], 1)
            self.assertEqual([v["kind"] for v in rep.violations], ["verbatim-run-over-limit"])

    def test_recorded_text_provenance_has_no_failure(self):
        f = DR / "view/shareable_package/TEXT_PROVENANCE.json"
        if not f.exists():
            self.skipTest("no recorded text provenance (no local corpus when the package was built)")
        d = json.loads(f.read_text())
        self.assertEqual(d["failures"], 0)
        self.assertGreater(d["corpus_files"], 100)
        for q in d["short_marked_quotations"]:
            self.assertLessEqual(q["words"], self.au.SHORT_QUOTE_MAX)
        for q in d["attributed_quotations"]:
            self.assertLessEqual(q["words"], self.au.ATTRIBUTED_QUOTE_MAX)
            self.assertRegex(q["text"], self.au.ATTRIBUTION_WORDS)


    # ---- IT5 P13 fix: prose, pair objects, repository names
    def test_prose_policy_pairs_names_status_and_paths_are_gone(self):
        page = self.share
        for w in ("hesperadin", "ziprasidone", "quetiapine", "flufenamic", "regadenoson", "AZD7545", "VER-246608", "AZD3965", "TTA-A2", "devimistat", "suvecaltamide", "carbenoxolone and flufenamic", "claim source DTC", "81 target rows"):
            self.assertNotIn(w.lower(), page.lower(), w)
        P = embedded(page)
        self.assertFalse([p for p in P["pairs"] if p.get("p") and p["p"]["cr"]["pha"][1]])
        self.assertIn(self.allow_pol["withheld_phrase"], json.dumps(P["leads"]))
        for d in P["leads"]:
            for k in ("card", "record"):
                if d.get(k):
                    self.assertNotRegex(d[k], r"\.(md|json)|/")
        self.assertEqual([m.group(0) for m in rv.FILE_TOKEN_RE.finditer(page) if m.group(0) not in rv.PACKAGE_FILE_NAMES and not m.group(0).startswith("class_b/")], [])
        # the full build keeps everything
        full = rv.build(DR, "full")
        for w in ("Hesperadin", "AZD7545", "claim source DTC"):
            self.assertIn(w, full)

    def test_stale_prose_redaction_fails_the_build(self):
        with tempfile.TemporaryDirectory() as td:
            dr = Path(td) / "dr"
            dr.mkdir()
            for p in DR.iterdir():
                if p.name != "view":
                    (dr / p.name).symlink_to(p)
            shutil.copytree(DR / "view", dr / "view", ignore=shutil.ignore_patterns("shareable_package", "preview", "index*.html"))
            pol = json.loads((dr / "view/shareable_sources.json").read_text())
            pol["prose_policy"]["card_substrings"].append({"find": "text that no card contains", "replace": "x"})
            (dr / "view/shareable_sources.json").write_text(json.dumps(pol), encoding="utf-8")
            with self.assertRaises(SystemExit):
                rv.build(dr, "shareable")

    def test_mutation_bc_only_pair_in_a_lead_sentence_and_in_a_card(self):
        # a sentence that names a compound and a target that the catalogue gives it only through class-B/C claims, with a database named
        name, genes = next((n, g) for n, g in self.ref.pair_bc.items() if n.isalpha() and len(n) > 8 and n not in self.ref.own_grams and not (self.ref.name_records[n] & self.ref.card_cat_ids))
        gene = sorted(genes)[0]
        sentence = f"The catalogue lists {name} against {gene} (claim source DTC, 'inhibitor')."
        t = self.mutate(lambda P: P["leads"][0].__setitem__("why", P["leads"][0]["why"] + " " + sentence))
        self.assertIn("class-bc-compound-target-pair-in-text", self.kinds(t))
        t = self.mutate(lambda P: P["cur"]["cands"][3].__setitem__("mechanism", P["cur"]["cands"][3]["mechanism"] + " " + sentence))
        self.assertIn("class-bc-compound-target-pair-in-text", self.kinds(t))
        # a database-free sentence about a card subject is own analysis (not a violation)
        subj = next(n for n, rids in self.ref.name_records.items() if n in self.ref.pair_bc and (rids & self.ref.card_cat_ids) and n.isalpha())
        sg = sorted(self.ref.pair_bc[subj])[0]
        t = self.mutate(lambda P: P["leads"][0].__setitem__("why", P["leads"][0]["why"] + f" {subj} acts on {sg}."))
        self.assertNotIn("class-bc-compound-target-pair-in-text", self.kinds(t))
        # the same sentence with the pair as a catalogue-only compound is caught when a literature corpus exists
        dirs = self.au.default_corpus_dirs()
        if dirs:
            lit = self.au.Literature(self.au.read_corpus(dirs))
            self.assertFalse(lit.contains(name))
            rep, _ = self.au.audit_html(self.mutate(lambda P: P["leads"][0].__setitem__("why", P["leads"][0]["why"] + f" {name} acts on {gene}.")), DR, self.ref, None, lit)
            self.assertIn("class-bc-compound-target-pair-in-text", {v["kind"] for v in rep.violations})

    def test_mutation_status_class_in_a_pair_object(self):
        def f(P):
            p = next(q for q in P["pairs"] if q.get("p"))
            p["p"]["cr"]["pha"][1] = ["approved_any_source"]
        self.assertIn("field-must-be-empty", self.kinds(self.mutate(f)))

    def test_mutation_repository_file_name_in_visible_text(self):
        t = self.mutate(lambda P: P["leads"][0].__setitem__("record", "closed_loop_it3_20261028/README.md#case-a"))
        self.assertIn("repository-file-name", self.kinds(t))

    # ---- the package
    def test_package_is_current_deterministic_and_self_describing(self):
        files, man = self.pk.build_files(DR, recompute_text=False)
        self.assertEqual(self.pk.check(DR, files), [], "run: python3 -B framework/scripts/repurposing_view.py package")
        files2, _ = self.pk.build_files(DR, recompute_text=False)
        self.assertEqual({k: self.pk.sha(v) for k, v in files.items()}, {k: self.pk.sha(v) for k, v in files2.items()})
        self.assertEqual(files["index.html"].decode("utf-8"), rv.build(DR, "shareable"))
        self.assertEqual(files["index.html"], (DR / "view/index_shareable.html").read_bytes())
        for need in ("index.html", "NOTICE.md", "COMPARISON.md", "README.md", "manifest.json", "LICENSES/CC-BY-SA-3.0.txt", "class_b/chembl_cc-by-sa-3.0/chembl_cc-by-sa-3.0.jsonl",
                     "class_b/chembl_cc-by-sa-3.0/LICENSE_CC-BY-SA-3.0.txt", "class_b/chembl_cc-by-sa-3.0/CREDIT.txt"):
            self.assertIn(need, files)
        self.assertEqual(man["audit"]["violations"], 0)
        self.assertEqual(set(man["files"]), set(files) - {"manifest.json"})
        for rel, spec in man["files"].items():
            self.assertEqual(spec["sha256"], self.pk.sha(files[rel]), rel)
        notice = files["NOTICE.md"].decode()
        self.assertIn("LOCAL PREVIEW", notice)
        self.assertIn("not legal advice", notice.lower())
        for lab in ("CIViC", "DoCM", "openFDA"):
            self.assertIn(lab, notice)
        self.assertIn("the version of ChEMBL is ChEMBL_37", notice + files["class_b/chembl_cc-by-sa-3.0/CREDIT.txt"].decode())

    def test_class_b_file_is_separate_licensed_and_not_merged_into_the_page(self):
        files, man = self.pk.build_files(DR, recompute_text=False)
        rows = [json.loads(x) for x in files[self.pk.CHEMBL_FILE].decode().splitlines()]
        links = json.loads((DR / "catalog/card_links.json").read_text())["cards"]
        ids = sorted({x["chembl_id"] for v in links.values() for x in v.get("links", []) if x.get("chembl_id")})
        self.assertEqual([r["chembl_id"] for r in rows], ids)
        for r in rows:
            self.assertEqual(r["licence"], "CC BY-SA 3.0 Unported")
            self.assertEqual(r["chembl_release"], "ChEMBL_37 2026-05-01")
        credit = files[self.pk.CHEMBL_DIR + "/CREDIT.txt"].decode()
        self.assertIn("https://www.ebi.ac.uk/chembl/", credit)
        self.assertIn("ChEMBL_37", credit)
        self.assertIn("adaptation", credit.lower())
        self.assertIn(b"Attribution-ShareAlike 3.0 Unported", files[self.pk.CHEMBL_DIR + "/LICENSE_CC-BY-SA-3.0.txt"])
        page = files["index.html"].decode()
        wording = [m["mechanism_of_action"] for r in rows for m in r["curated_mechanisms"] if m["mechanism_of_action"] and len(m["mechanism_of_action"].split()) > self.au.WORDING_MAX_WORDS]
        for w in wording:   # passages; short labels (<= 8 words) that a card quotes with attribution are listed by the audit instead
            self.assertNotIn(w, page, "ChEMBL mechanism wording must not be in the single page")
        rep, _ = self.au.audit_html(page, DR, self.ref)
        self.assertNotIn("Voltage-gated T-type calcium channel blocker", page, "the card's quotation of a ChEMBL label is withheld in the shareable build (prose policy)")
        self.assertEqual(rep.violations, [])
        # the other share-alike sources are not shipped
        self.assertFalse([k for k in files if "gtopdb" in k.lower() or "clinpgx" in k.lower() or "pharmgkb" in k.lower()])
        man_b = [x["label"] for x in man["class_b_files"]]
        self.assertEqual(man_b, ["chembl"])

    def test_package_links_work_outside_the_repository(self):
        page = rv.build(DR, "shareable")
        body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", page, flags=re.S)
        for h in re.findall(r'href="([^"]*)"', body):
            self.assertTrue(h.startswith(("#", "https://", "http://")), h)
        P = embedded(page)
        for c in P["cur"]["cands"]:
            self.assertFalse(c["card_path"].startswith(("../", "cards/")), c["card_path"])
        for coll in (P["rows"], P["needs"]):
            for x in coll:
                for cd in x.get("cards") or []:
                    self.assertTrue(cd["path"] is None or cd["path"].startswith("#cand-"), cd)
        self.assertNotRegex(page, r"/home/|/tmp/|\.claude/worktrees")

    def test_zip_is_deterministic(self):
        import zipfile
        files, _ = self.pk.build_files(DR, recompute_text=False)
        with tempfile.TemporaryDirectory() as td:
            a, b = Path(td) / "a.zip", Path(td) / "b.zip"
            self.assertEqual(self.pk.make_zip(DR / self.pk.PKG, files, a), self.pk.make_zip(DR / self.pk.PKG, files, b))
            with zipfile.ZipFile(a) as z:
                names = z.namelist()
                self.assertEqual(names, sorted(names))
                self.assertTrue(all(n.startswith("wwox_repurposing_shareable_package/") for n in names))
                self.assertEqual(z.read("wwox_repurposing_shareable_package/index.html"), files["index.html"])

    def test_checker_and_package_tools_have_safe_help(self):
        for m in ("repurposing_shareable_audit.py", "repurposing_shareable_package.py"):
            r = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve().parent / m), "--help"], capture_output=True, text=True, timeout=60)
            self.assertEqual(r.returncode, 0, r.stderr[-200:])
            self.assertTrue(r.stdout.strip())


@unittest.skipUnless(HAVE_DATA, "module data absent")
class ShareableAuditRendered(unittest.TestCase):
    """The rendered surfaces of the shareable page (first screen, every export, standalone download, comparison, PDF text) hold nothing the static audit forbids."""

    def test_rendered_exports_standalone_comparison_and_pdf_text_pass(self):
        import repurposing_shareable_audit as au
        if not rv.find_chromium():
            self.skipTest("no Chromium binary: the rendered surfaces were NOT scanned")
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "s.html"
            text = rv.build(DR, "shareable")
            f.write_text(text, encoding="utf-8")
            try:
                extra, info = au.dynamic_surfaces(f, embedded(text))
            except Exception as e:
                self.skipTest("browser could not be driven: " + str(e)[:120])
            rep, _ = au.audit_html(text, DR, None, extra)
        self.assertEqual(rep.violations, [], rep.violations[:5])
        self.assertEqual(info["exports"], info["standalone_downloads"])
        self.assertGreater(info["exports"], 20)
        kinds = {w.split(":")[1] for w, _ in extra if w.startswith("rendered:")}
        self.assertTrue({"first-screen", "export", "standalone", "compare"} <= kinds, kinds)


@unittest.skipUnless(HAVE_DATA, "module data absent")
class CuratedBrowser(Browser):
    def test_export_card_has_public_identifiers(self):
        d = self.dom("#export=EB-ETX-01")
        area = d[d.index('id="export-area"'):]
        self.assertIn("exporting", d)
        self.assertIn("https://pubmed.ncbi.nlm.nih.gov/32000863/", area)
        self.assertIn("PMID 32000863", area)
        self.assertIn("CHEMBL696", area)
        self.assertIn("Dati aggiornati al:", area)
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
        self.assertEqual(n_links, 51)
        goals = re.findall(r'<div class="goal (?:deep|partial)".*?<span class="mini mut">\((\d+)\)</span></div></div>', self.page, re.S)
        self.assertEqual(sum(map(int, goals)), n_links)
        self.assertIn("I 51 legami candidato-bisogno sono contati tutti", self.page)

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
        consts = repr([sorted(rv.FAV_SIGNS), sorted(rv.CARRIER_SIGNS), sorted(rv.WWOX_KINDS), sorted(rv.OUT_KINDS), rv.READING_FLAGS, rv.DESIGN_FLAGS, rv.WEAK_FLAGS, rv.NOT_RECOVERY, sorted(rv.FIRM_DEPTHS)])   # IT6 P2 (V7): the constants that decide positions are part of the pin
        h = hashlib.sha256((inspect.getsource(rv.classify_rows) + inspect.getsource(rv.assign_need_position) + inspect.getsource(rv.overview_positions) + consts).encode()).hexdigest()[:16]
        self.assertEqual(h, "56e4bfd5f4023311", "the F/C/P rules changed: this view only displays them (IT5 P11 verified revision; re-pinned by IT6 P2 twice: engagement nulls are counter rows, C3 and F3 share one support, reading-limit and design-limit split, partial benefit never carries F1; the pin now also covers the constants that decide positions)")


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
            if m["scenario"] in ("brief", "evidence_graph", "work_order"):
                self.assertEqual(m["ready"], "1", m)      # IT6 P13 scenarios are exercised at every viewport
            if m["scenario"] == "first_screen" and m["mobile"]:
                self.assertLess(m["legendBottom"], dict((w, h) for w, h, _ in rv.VIEWPORTS)[m["requested"]], "the F/C/P legend must sit above the fold")
        names = {m["scenario"] for m in res}
        self.assertTrue({"brief", "evidence_graph", "work_order", "print_brief", "print_brief_all", "selection", "hypotheses", "predictive", "contexts", "section_selection", "section_predictive",
                         "print_section_selection", "print_section_hypotheses", "print_section_predictive"} <= names, names)
        for sc in ("selection", "hypotheses", "predictive", "contexts"):
            for m in res:
                if m["scenario"] == sc:
                    self.assertEqual(m["ready"], "1", m)      # IT7 P7 sections are exercised at every viewport
        for sc, mx in (("print_section_selection", 8), ("print_section_hypotheses", 14), ("print_section_predictive", 8)):
            pg = next(m for m in res if m["scenario"] == sc)["pdf_pages"]
            self.assertTrue(1 <= pg <= mx, (sc, pg))      # a section prints on a handful of A4 pages, not on the whole page
        pb = {m["scenario"]: m for m in res if m["scenario"].startswith("print_brief")}
        self.assertEqual(pb["print_brief"]["pdf_pages"], 1, "the longest one-page synthesis must print on ONE A4 page")
        self.assertEqual(pb["print_brief_all"]["pdf_pages"], len(rv.build_payload(DR, "shareable")["cur"]["cands"]), "every card's synthesis prints on exactly one A4 page")


# ---------------------------------------------------------------------------- IT6 P13: one-page synthesis, evidence graph, work order
@unittest.skipUnless(HAVE_DATA, "module data absent")
class It6P13Data(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.P = rv.build_payload(DR)
        cls.cur = cls.P["cur"]
        cls.page = rv.build(DR)
        cls.titles = rv.load_titles(DR)
        cls.eg_doc = json.loads((DR / rv.GRAPH_NAME).read_text())
        cls.wo_doc = json.loads((DR / rv.WORK_ORDER_NAME).read_text())
        cls.cards = [c["id"] for c in cls.cur["cands"]]
        cls.needs = [n["id"] for n in cls.cur["needs"]]
        cls.groups = {n: {l["group"] for c in cls.cur["cands"] for k, l in c["links"].items() if k == n} for n in cls.needs}

    @staticmethod
    def static_html(page):
        return re.sub(r"<script\b.*?</script>", "", page, flags=re.S)

    # ---- (1) brief
    def test_brief_has_eight_fields_and_at_most_five_titled_sources(self):
        for c in self.cur["cands"]:
            b = c["brief"]
            for k in ("wwox", "external", "counter", "missing", "next"):
                self.assertTrue(str(b[k]).strip(), (c["id"], k))
            self.assertLessEqual(len(b["sources"]), rv.BRIEF_SOURCES_MAX)
            titled = [x for x in b["sources"] if x["kind"] == "PMID"]
            for x in titled:
                self.assertIn(x["id"], {p["id"] for p in c["pmids"]})
                self.assertEqual(x["title"], (self.titles.get(x["id"]) or {}).get("title"), (c["id"], x["id"]))
            self.assertLessEqual(rv.brief_chars(c), 4800, c["id"])     # the budget that keeps one card on one A4 page (measured in the print test)
        js = (DR / "view/assets/curated.js").read_text()
        self.assertIn("#brief=", js)
        self.assertIn("data-brief", js)
        for i in range(1, 9):
            self.assertTrue(rv.UI_IT[f"bf_f{i}"])
            self.assertIn(f"T.bf_f{i}", js)
        self.assertIn("x-dl", js)     # standalone download, like the dossier
        self.assertEqual(rv.UI_IT["cd_brief"], "Sintesi (1 pagina)")

    def test_brief_data_date_and_catalogue_build_are_separate_fields(self):
        js = (DR / "view/assets/curated.js").read_text()
        self.assertIn('data-date="data"', js)
        self.assertIn('data-date="catalogo"', js)
        m = self.cur["meta"]
        self.assertNotEqual(m["data_date"], m["catalogue_generated"])      # a date and a timestamp: two different facts, never merged

    # ---- (2) graph
    def test_graph_validates_and_names_the_iteration6_chains(self):
        errs = rv.validate_evidence_graph(self.eg_doc, self.cards, self.needs, self.titles, DR)
        self.assertEqual(errs, [])
        self.assertEqual([c["id"] for c in self.eg_doc["chains"]], ["glia", "nmdar-gate", "missense-route", "rescue-window", "isr-sign"])
        used = {x for ch in self.eg_doc["chains"] for n in ch["nodes"] for x in n.get("cards", [])}
        self.assertTrue({"J01_glial_reactivity_modulation", "F01_glutamate_receptor_node", "P11_magnesium_nmdar_gate", "A02_proteasome_inhibitor_class"} <= used)
        isr = next(c for c in self.eg_doc["chains"] if c["id"] == "isr-sign")
        self.assertEqual(isr["state"], "non risolto")
        self.assertTrue(any(n.get("unresolved") for n in isr["nodes"]))
        self.assertTrue(any(n["col"] == "esperimento" and "phospho" in n["label"] for n in isr["nodes"]))

    def mutated_graph(self, fn):
        d = json.loads(json.dumps(self.eg_doc))
        fn(d)
        return rv.validate_evidence_graph(d, self.cards, self.needs, self.titles, DR)

    def test_graph_mutations_fail(self):
        first = lambda d: d["chains"][0]
        self.assertTrue(self.mutated_graph(lambda d: first(d)["nodes"][3].__setitem__("needs", ["NEED-DOES-NOT-EXIST"])))         # dangling need id
        self.assertTrue(self.mutated_graph(lambda d: first(d)["nodes"][6].__setitem__("cards", ["ZZ99_no_card"])))                # dangling card id
        self.assertTrue(self.mutated_graph(lambda d: first(d)["nodes"][0].__setitem__("pmids", ["99999999"])))                    # unknown PMID
        self.assertTrue(self.mutated_graph(lambda d: first(d)["edges"][0].__setitem__("source", "PMID:99999999")))                # unknown source PMID
        self.assertTrue(self.mutated_graph(lambda d: first(d)["edges"][0].__setitem__("to", "nope")))                             # dangling node
        self.assertTrue(self.mutated_graph(lambda d: first(d)["edges"][0].pop("type")))                                           # untyped edge
        self.assertTrue(self.mutated_graph(lambda d: first(d)["edges"][0].__setitem__("type", "causa")))                         # type outside the closed list
        self.assertTrue(self.mutated_graph(lambda d: first(d)["edges"][0].pop("source")))                                         # edge without a source id
        self.assertTrue(self.mutated_graph(lambda d: first(d)["edges"][0].__setitem__("source", "DOC:UNDECLARED")))
        self.assertTrue(self.mutated_graph(lambda d: first(d)["edges"].pop()))                                                    # chain no longer leads to an experiment
        self.assertTrue(self.mutated_graph(lambda d: first(d)["edges"][0].update({"from": "n1", "to": "o1"})))                    # backwards edge
        self.assertTrue(self.mutated_graph(lambda d: d["chains"][0]["nodes"].append({"id": "orph", "col": "evidenza", "scope": "none", "label": "orphan"})))
        self.assertTrue(self.mutated_graph(lambda d: d.__setitem__("columns", list(reversed(d["columns"])))))

    def test_interactome_is_never_a_causal_edge(self):
        def add(d, typ):
            ch = d["chains"][0]
            ch["nodes"].append({"id": "ia", "col": "osservazione WWOX", "scope": "wwox", "label": "Interactome: list of interactors of the protein", "interactome": True})
            ch["edges"].append({"from": "ia", "to": "n1", "type": typ, "source": "DOC:P10"})
        self.assertTrue(any("interactome" in e for e in self.mutated_graph(lambda d: add(d, "inferenza"))))
        self.assertTrue(any("interactome" in e for e in self.mutated_graph(lambda d: add(d, "risultato sperimentale"))))
        self.assertEqual(self.mutated_graph(lambda d: add(d, "associazione")), [])      # an association is the most it may be
        self.assertFalse(any(re.search(r"interactom|interactor", n["label"], re.I) for ch in self.eg_doc["chains"] for n in ch["nodes"]))

    def test_graph_is_server_rendered_with_three_edge_styles_legend_and_table(self):
        h = self.static_html(self.page)
        self.assertEqual(h.count('<svg class="eg"'), len(self.eg_doc["chains"]))
        eg = self.cur["evidence_graph"]
        for ch in eg["chains"]:
            for n in ch["nodes"]:       # no JS-only content: every node label and the table of edges are in the markup with scripts removed
                self.assertIn(html_escape(n["label"]), h, n["id"])
        n_edges = sum(len(c["edges"]) for c in eg["chains"])
        self.assertEqual(len(re.findall(r'<g class="eg-e" data-edge-type=', h)), n_edges)
        for code, typ in (("R", "risultato sperimentale"), ("I", "inferenza"), ("A", "associazione")):
            self.assertIn(f'class="eg-line e-{code}"', h)
            self.assertEqual(len(re.findall(rf'<g class="eg-e" data-edge-type="{typ}"', h)), sum(1 for c in eg["chains"] for e in c["edges"] if e["type"] == typ))
        css = (DR / "view/assets/curated.css").read_text()
        self.assertRegex(css, r"\.eg-line\.e-I\{[^}]*stroke-dasharray:8 5")
        self.assertRegex(css, r"\.eg-line\.e-A\{[^}]*stroke-dasharray:1\.5 5")
        self.assertNotRegex(re.search(r"\.eg-line\.e-R\{[^}]*\}", css).group(0), "dasharray")
        for ch in eg["chains"]:      # table rows == edges (the printed count in each summary equals the data)
            m = re.search(rf'id="chain-{ch["id"]}".*?<summary>[^<]*\((\d+)\)</summary>(.*?)</article>', h, re.S)
            self.assertEqual(int(m.group(1)), len(ch["edges"]))
            self.assertEqual(m.group(2).count("<tr>") - 1, len(ch["edges"]))
        self.assertIn('id="chains"', h)
        self.assertIn("scorre in orizzontale al suo interno", h)
        self.assertNotIn("<script", re.search(r'<section id="chains".*?</section>', h, re.S).group(0))

    # ---- (3) work order
    def test_work_order_follows_needs_order_and_covers_the_priority_needs(self):
        ids = [e["need"] for e in self.wo_doc["entries"]]
        self.assertEqual(ids, sorted(ids, key=self.needs.index))      # the order is the order of needs.json
        review = (DR / "priority_review_it6_20261029.md").read_text()
        sec = review[review.index("## 6. Work order"):review.index("## 7.")]
        eleven = {"NEED-WWOX-GENE-ADDITION", "NEED-SEIZURE-CONTROL-SYMPTOMATIC", "NEED-T-TYPE-CALCIUM", "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", "NEED-LACTATE-LDH", "NEED-PDH-PYRUVATE-AXIS",
                  "NEED-ISR-ATTENUATION", "NEED-MYC-PROGENITOR-PROLIFERATION", "NEED-SYSTEMIC-GLYCAEMIA-GROWTH", "NEED-MYELINATION", "NEED-WWOX-MISSENSE-PROTEIN-RESCUE"}
        self.assertEqual(len([l for l in sec.splitlines() if l.startswith("| ")]), 12)       # header and the eleven rows of the review's table
        self.assertEqual(set(ids), eleven | {"NEED-NEUROINFLAMMATION-GLIA"})
        self.assertEqual(self.mutated_wo(lambda d: None), [])
        by = {e["need"]: e for e in self.wo_doc["entries"]}
        for nid, upd in (("NEED-NEUROINFLAMMATION-GLIA", "P10"), ("NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", "P11"), ("NEED-ISR-ATTENUATION", "P4"), ("NEED-WWOX-MISSENSE-PROTEIN-RESCUE", "P6"), ("NEED-WWOX-GENE-ADDITION", "P7")):
            self.assertIn(upd, by[nid]["updated_by"], nid)
        self.assertEqual(self.wo_doc["research_update"], "2026-10-29")

    def mutated_wo(self, fn):
        d = json.loads(json.dumps(self.wo_doc))
        fn(d)
        return rv.validate_work_order(d, self.needs, self.groups, self.cards, DR)

    def test_kind_agrees_with_the_fcp_positions_of_the_need(self):
        for e in self.wo_doc["entries"]:
            self.assertIn(e["kind"], rv.allowed_kinds(self.groups[e["need"]]), e["need"])
        # the rule itself
        self.assertEqual(rv.allowed_kinds(set()), {"risolvere una premessa"})
        self.assertEqual(rv.allowed_kinds({"F2"}), {"verificare un'ipotesi"})
        self.assertEqual(rv.allowed_kinds({"F3", "C2", "P1"}), set(rv.WO_KINDS))
        # mutations: a kind the positions do not support, a dangling need, a swapped order, a score field, an empty feasibility, a bad date
        e0 = next(i for i, e in enumerate(self.wo_doc["entries"]) if e["need"] == "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR")
        self.assertTrue(self.mutated_wo(lambda d: d["entries"][e0].__setitem__("kind", "chiarire una controevidenza")))      # F2 only: no counter-evidence on record
        g0 = next(i for i, e in enumerate(self.wo_doc["entries"]) if e["need"] == "NEED-NEUROINFLAMMATION-GLIA")
        if not self.groups["NEED-NEUROINFLAMMATION-GLIA"]:      # no card is linked to the need yet: only its premise can be addressed (after the merge that links J01 this branch is skipped)
            self.assertTrue(self.mutated_wo(lambda d: d["entries"][g0].__setitem__("kind", "verificare un'ipotesi")))
        self.assertTrue(self.mutated_wo(lambda d: d["entries"][0].__setitem__("kind", "ordinare")))
        self.assertTrue(self.mutated_wo(lambda d: d["entries"][0].__setitem__("need", "NEED-NOPE")))
        self.assertTrue(self.mutated_wo(lambda d: d["entries"].reverse()))
        self.assertTrue(self.mutated_wo(lambda d: d["entries"][0].__setitem__("score", 0.9)))
        self.assertTrue(self.mutated_wo(lambda d: d["entries"][0].__setitem__("feasibility", "")))
        self.assertTrue(self.mutated_wo(lambda d: d["entries"][0].__setitem__("date", "29/10/2026")))
        self.assertTrue(self.mutated_wo(lambda d: d["entries"][0].__setitem__("cards", ["ZZ99"])))

    def test_work_order_is_shown_by_need_with_separate_dates_and_unknown_feasibility(self):
        h = self.static_html(self.page)
        sec = re.search(r'<div id="work-order".*?(?=<div class="btns">)', h, re.S).group(0)
        wo = self.cur["work_order"]
        self.assertEqual(sec.count('class="wo-item"'), len(wo["entries"]))
        self.assertEqual([m for m in re.findall(r'data-need="([^"]+)" data-kind', sec)], [e["need"] for e in wo["entries"]])
        self.assertIn('data-k="cur.work_order_date" data-v="2026-10-29"', sec)
        self.assertIn(f'data-k="cur.catalogue_generated" data-v="{self.cur["meta"]["catalogue_generated"]}"', sec)
        self.assertIn("due date diverse", sec)
        for e in wo["entries"]:
            self.assertIn(html_escape(e["kind"]), sec)
            self.assertIn(html_escape(e["feasibility"]), sec)
        self.assertNotIn("Ordine di lavoro", sec)      # the heading is 'Piano di verifiche': no implied sequence
        self.assertEqual(sec.count("non nota"), sum(e["feasibility_it"].count("non nota") for e in wo["entries"]) + sec.count("«non nota»"))
        for e in wo["entries"]:      # an Italian one-line summary and the Italian feasibility line stand above the English scientific text
            self.assertIn(html_escape(e["summary_it"]), sec)
            self.assertIn(html_escape(e["feasibility_it"]), sec)
            self.assertNotIn("non nota", e["feasibility"])
        self.assertNotRegex(sec, r"<ol\b")                      # an ordered list would read as a ranking
        for bad in ("score", "punteggio:", "probabilit"):
            self.assertNotIn(bad, re.sub(r"non ha punteggio", "", sec))
        # printed counts equal the data: positions chips of each entry are the need's set
        for e in wo["entries"]:
            self.assertEqual(e["positions"], sorted(self.groups[e["need"]]))

    # ---- window state (P7)
    def test_window_state_is_in_the_gene_addition_entry_and_the_c01_c04_briefs(self):
        wo = self.cur["work_order"]
        e = next(x for x in wo["entries"] if x["need"] == "NEED-WWOX-GENE-ADDITION")
        self.assertEqual([x["state"] for x in e["window_state"]], ["prevented_early_window", "recovered_post_onset_model", "unmeasured"])
        self.assertEqual(set(wo["window_states"]), set(rv.WINDOW_STATES))
        for cid in ("C01_aav9_wwox", "C04_aav9_endpoint_families"):
            c = next(x for x in self.cur["cands"] if x["id"] == cid)
            self.assertEqual(c["brief"]["window"]["states"], ["prevented_early_window", "unmeasured"])
        self.assertTrue(all(c["brief"].get("window") is None for c in self.cur["cands"] if c["id"] not in wo["card_windows"]))
        h = self.static_html(self.page)
        for st in ("prevenzione (finestra precoce)", "recupero dopo l'esordio (solo in un modello)", "non misurato"):
            self.assertIn(html_escape(st), h)
        # the card wording itself carries the early-window statement (data-driven check at build)
        for cid in wo["card_windows"]:
            self.assertRegex(json.dumps(rv.load_cards(DR)[cid][0]), r"(?i)early-window")

    def test_window_state_mutations_fail(self):
        self.assertTrue(self.mutated_wo(lambda d: d["entries"][0]["window_state"][0].__setitem__("state", "cured")))
        self.assertTrue(self.mutated_wo(lambda d: d["card_windows"].__setitem__("ZZ99", {"states": ["unmeasured"], "note": "x"})))
        d = json.loads(json.dumps(self.wo_doc))
        d["card_windows"]["F01_glutamate_receptor_node"] = {"states": ["prevented_early_window"], "note": "x"}
        texts = {c: json.dumps(v[0]) for c, v in rv.load_cards(DR).items()}
        self.assertTrue(any("early-window" in e for e in rv.validate_work_order(d, self.needs, self.groups, self.cards, DR, texts)))   # F01 does not say early-window

    def test_nmdar_chain_uses_f04_with_three_unranked_readings_and_e1(self):
        ch = next(c for c in self.eg_doc["chains"] if c["id"] == "nmdar-gate")
        cards = {x for n in ch["nodes"] for x in n.get("cards", [])}
        self.assertEqual(cards, {"F01_glutamate_receptor_node", "F04_nmdar_intervention_class", "P11_magnesium_nmdar_gate"})
        self.assertEqual(sum(1 for n in ch["nodes"] if n["label"].startswith("Reading ")), 3)
        self.assertTrue(any(n["label"].startswith("E1:") and n["col"] == "esperimento" for n in ch["nodes"]))
        e = next(x for x in self.wo_doc["entries"] if x["need"] == "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR")
        self.assertIn("F04_nmdar_intervention_class", e["cards"])
        self.assertIn("P9", e["updated_by"])
        self.assertIn("E1", e["data"])

    # ---- IT6 P13 verifier repairs
    def card(self, cid):
        return next(c for c in self.cur["cands"] if c["id"] == cid)

    def test_p11_brief_names_the_tool_compound_and_the_card_is_linked_to_its_need(self):
        b = self.card("P11_magnesium_nmdar_gate")["brief"]["wwox"]
        self.assertIn("d-APV", b)
        self.assertIn("competitive", b)
        self.assertIn("five slices from three animals", b)
        self.assertEqual(self.card("P11_magnesium_nmdar_gate")["needs"], ["NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR"])      # the need record lists the card (needs.json sources.cards)

    def test_counter_evidence_is_ordered_by_category_and_safety_comes_first(self):
        b = self.card("EB-VGB-01")["brief"]
        self.assertEqual(len(b["counter"]), 3)
        self.assertEqual([x["cat"] for x in b["counter"]], sorted(x["cat"] for x in b["counter"]))
        self.assertIn("MRI", b["counter"][0]["text"])      # the brain MRI abnormality signals are not buried
        self.assertEqual(b["counter"][0]["cat"], 0)
        self.assertGreater(b["counter_more"], 0)
        self.assertTrue(all(x["category"] in rv.COUNTER_CATEGORIES for x in b["counter"]))
        # the rule itself: category first, stored order inside a category, independent of how the card lists the items
        items = [(2, "outside"), (1, "wwox null"), (0, "harm"), (0, "harm 2"), (2, "outside 2")]
        self.assertEqual([t for _, t in rv.order_counter(items)], ["harm", "harm 2", "wwox null", "outside", "outside 2"])
        self.assertEqual(rv.order_counter(items, flip=True)[0][1], "outside")      # mutation: a reversed ranking puts a non-safety item first
        self.assertNotIn("MRI", rv.order_counter([(rv.counter_category(t), t) for t in ("Organoid markers are up", "vigabatrin MRI abnormality (safety signal)")], flip=True)[0][1])
        self.assertEqual(rv.counter_category("two children with brain MRI abnormalities"), 0)
        self.assertEqual(rv.counter_category("The knockout slices showed no effect of the drug"), 1)
        self.assertEqual(rv.counter_category("A step and a continuum are indistinguishable"), 2)
        self.assertNotIn("decisiva", rv.UI_IT["bf_f5"].lower())      # the label does not claim a weighting

    def test_counter_placeholder_is_not_shown_as_evidence(self):
        b = self.card("EB-PDANCHOR-AX-01")["brief"]
        self.assertEqual(b["counter"][0]["text"], rv.UI_IT["bf_counter_none"])
        self.assertIn("nessuna controevidenza registrata nella scheda", b["counter"][0]["text"].lower())

    def test_brief_text_is_cut_only_at_sentence_boundaries_and_has_no_repository_identifiers(self):
        import repurposing_view as m
        for c in self.cur["cands"]:
            b = c["brief"]
            for f in ("wwox", "external", "missing", "next"):
                self.assertFalse(b[f].endswith("…"), (c["id"], f))
            for x in b["counter"]:      # a counter item may be cut at a clause (never mid-word) so that the page stays one A4 page; the dossier keeps it whole
                self.assertTrue(len(x["text"]) <= 240 * 1.5 + 3 or not x["text"].endswith("…"), c["id"])
            blob = " ".join([b["wwox"], b["external"], b["missing"], b["next"]] + [x["text"] for x in b["counter"]])
            self.assertNotRegex(blob, r"CLAIM \d|DL-[A-Z]+-\d|HYP-\d{8}|MECHANISM_TRANSFER|\bN-\d+\b|needs audit")
        long_t = "First sentence is here. " + "Second sentence goes on and on without end " * 12 + "Last."
        out = m.clip_sentence(long_t, 60)
        self.assertTrue(out.endswith("."), out)
        self.assertEqual(m.clip_sentence("Short text.", 60), "Short text.")
        self.assertEqual(m.scrub_ids("A result (CLAIM 031, DL-BIO-009) stands."), "A result stands.")

    def test_three_dates_are_separate_and_the_research_date_is_not_the_catalogue_date(self):
        m = self.cur["meta"]
        self.assertEqual(m["research_update"], m["data_date"])
        self.assertGreaterEqual(m["research_update"], m["needs_built_on"])
        self.assertGreaterEqual(m["research_update"], m["catalogue_generated"][:10])
        self.assertGreaterEqual(m["research_update"], self.wo_doc["research_update"])
        h = self.static_html(self.page)
        for k in ("meta.data_date", "meta.needs_built_on", "meta.catalogue_generated"):
            self.assertIn(f'data-k="{k}"', h)
        js = (DR / "view/assets/curated.js").read_text()
        for d in ("data", "registro", "catalogo"):
            self.assertIn(f'data-date="{d}"', js)
        self.assertIn("META.research_update", js)
        self.assertEqual(rv.research_update_date(DR, "2026-01-01"), max("2026-01-01", rv.research_update_date(DR)))

    def test_candidate_line_keeps_the_goal_prefix_and_window_chip_carries_its_qualifiers(self):
        js = (DR / "view/assets/curated.js").read_text()
        self.assertIn("esc(goalTxt(c.goal))", js)
        self.assertTrue(rv.UI_IT["chip_goal"].strip())
        e = next(x for x in self.cur["work_order"]["entries"] if x["need"] == "NEED-WWOX-GENE-ADDITION")
        note = next(x["note"] for x in e["window_state"] if x["state"] == "recovered_post_onset_model")
        for q in ("about 3 weeks", "different organoid cohorts", "week 16 only", "persistence not measured", "one endpoint family", "radial-glia"):
            self.assertIn(q, note)
        h = self.static_html(self.page)
        self.assertIn(f'title="{html_escape(note)}"', h)      # the chip's tooltip
        node = next(n for c in self.eg_doc["chains"] if c["id"] == "rescue-window" for n in c["nodes"] if n["id"] == "e2")
        self.assertIn("other cohorts", node["label"])
        self.assertIn("radial glia not corrected", node["label"])
        for s in ("prevenzione (finestra precoce)", "recupero dopo l'esordio (solo in un modello)"):
            self.assertIn(html_escape(s), h)
        self.assertNotIn("prevenuto", " ".join(str(v) for k, v in rv.UI_IT.items() if k.startswith("ws_")))

    def test_graph_repairs_isr_nmdar_missense(self):
        ch = {c["id"]: c for c in self.eg_doc["chains"]}
        n = {(c, x["id"]): x for c in ch for x in ch[c]["nodes"]}
        self.assertIn("knockdown not shown", n[("isr-sign", "o2")]["label"])
        self.assertNotIn("silenced", n[("isr-sign", "o2")]["label"])
        e = next(x for x in ch["nmdar-gate"]["edges"] if x["from"] == "o2" and x["to"] == "n1")
        self.assertEqual(e["type"], "inferenza")
        self.assertIn("competitive NMDAR antagonist", n[("nmdar-gate", "o2")]["label"])
        w = next(x for x in ch["nmdar-gate"]["edges"] if x["to"] == "e3")
        self.assertNotIn("efficacy signal", w["note"])
        self.assertEqual(sorted(x["source"] for x in ch["missense-route"]["edges"] if x["to"] in ("e2", "e3", "e4")), ["PMID:33914734", "PMID:37319242", "PMID:39041895"])
        self.assertIn("tolerated", n[("missense-route", "e4")]["label"])
        self.assertNotIn("tolerated", n[("missense-route", "e2")]["label"])
        self.assertNotIn("inert", n[("missense-route", "e3")]["label"])
        self.assertTrue(rv.load_titles(DR).get("33914734"))

    def test_graph_is_legible_on_a_phone(self):
        css = (DR / "view/assets/curated.css").read_text()
        self.assertRegex(css, r"\.eg-n text\{font:12\.5px")
        self.assertIn("nav .in a{display:inline-block;min-height:26px", css)
        h = self.static_html(self.page)
        self.assertEqual(h.count('class="mini eg-cue"'), len(self.eg_doc["chains"]))
        self.assertIn("background-attachment:local,local,scroll,scroll", css)      # scroll shadows: a visible cue on the figure itself

    def test_shareable_build_carries_graph_brief_and_work_order(self):
        sh = rv.build_payload(DR, "shareable")["cur"]
        self.assertEqual(sh["evidence_graph"]["chains"], self.cur["evidence_graph"]["chains"])
        self.assertEqual(sh["work_order"]["entries"], self.cur["work_order"]["entries"])
        for path in ("view/evidence_graph.json", "view/work_order.json", "isr_kinase", ".md"):     # no repository path or file name in the shareable page
            self.assertNotIn(path, self.static_html(rv.build(DR, "shareable")), path)

    def test_leak_audit_catches_a_class_c_name_in_the_graph_and_in_a_brief(self):
        import repurposing_shareable_audit as au
        share = rv.build(DR, "shareable")
        ref = au.Reference(DR)
        name = None
        import gzip
        with gzip.open(DR / "catalog/catalog.jsonl.gz", "rt", encoding="utf-8") as fh:
            for line in fh:
                e = json.loads(line)
                cs = {t.get("claim_source") for t in e.get("targets") or []}
                n = e.get("name") or ""
                if e["origin"] == "dgidb_only" and cs == {"DTC"} and n.isalpha() and len(n) >= 8 and au.norm(n) not in ref.own_grams:
                    name = n
                    break
        self.assertTrue(name)
        def mut(fn):
            P = embedded(share)
            fn(P)
            data = json.dumps(P, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "<\\!--")
            return re.sub(r'(<script id="data" type="application/json">).*?(</script>)', lambda m: m.group(1) + data + m.group(2), share, count=1, flags=re.S)
        for fn in (lambda P: P["cur"]["evidence_graph"]["chains"][0]["nodes"][0].__setitem__("label", "x " + name),
                   lambda P: P["cur"]["cands"][0]["brief"].__setitem__("wwox", "x " + name),
                   lambda P: P["cur"]["work_order"]["entries"][0].__setitem__("question", "x " + name)):
            rep, _ = au.audit_html(mut(fn), DR, ref)
            self.assertIn("forbidden-name", {v["kind"] for v in rep.violations})
        rep, _ = au.audit_html(share, DR, ref)
        self.assertEqual(rep.violations, [])


def html_escape(s):
    import html
    return html.escape(s)


class BriefBrowser(Browser):
    def test_brief_route_renders_eight_fields_and_two_dates(self):
        cid = "EB-ETX-01"
        d = self.dom("#brief=" + cid)
        area = d[d.index('id="export-area"'):]
        self.assertIn("exporting", d)
        self.assertEqual(len(re.findall(r'<dt data-field="\d">', area)), 8)
        for i in range(1, 9):
            self.assertIn(rv.UI_IT[f"bf_f{i}"], area)
        self.assertRegex(area, r'data-date="data">\d{4}-\d{2}-\d{2}<')
        self.assertRegex(area, r'data-date="catalogo">\d{4}-\d{2}-\d{2}T')
        self.assertIn('href="#export=' + cid + '"', area)
        self.assertIn("PMID 32000863", area)
        self.assertEqual(len(re.findall(r"PMID \d+</a>", area)), len(self.cards_brief(cid)))

    def cards_brief(self, cid):
        return next(c for c in self.P["cur"]["cands"] if c["id"] == cid)["brief"]["sources"]

    def test_profile_has_the_brief_button_beside_the_export_button(self):
        d = self.dom("#c=need:NEED-T-TYPE-CALCIUM")
        self.assertRegex(d, r'data-export="EB-ETX-01">[^<]*</button><button type="button" data-brief="EB-ETX-01">Sintesi \(1 pagina\)</button>')

    def test_graph_and_work_order_render_with_javascript_too(self):
        d = self.dom("")
        self.assertEqual(d.count('<svg class="eg"'), 5)
        self.assertIn('data-wo="NEED-ISR-ATTENUATION"', d)       # priorities by need link to the work order


# ---------------------------------------------------------------------------- IT7 P7: selection funnel, hypothesis comparison, predictive test, context concordance
@unittest.skipUnless(HAVE_DATA, "module data absent")
class It7P7Data(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.P = rv.build_payload(DR)
        cls.cur = cls.P["cur"]
        cls.page = rv.build(DR)
        cls.h = re.sub(r"<script\b.*?</script>", "", cls.page, flags=re.S)
        cls.counts = json.loads((DR / rv.P2_DIR / "counts.json").read_text())
        cls.p3 = json.loads((DR / rv.P3_DIR / "results/results_summary.json").read_text())
        cls.e1 = json.loads((DR / rv.P3_DIR / "results/e1_p47t_summary.json").read_text())
        cls.rows4 = rv.read_tsv(DR / rv.P4_DIR / "context_matrix.tsv")
        cls.rows5 = rv.read_tsv(DR / rv.P5_DIR / "comparison.tsv")
        cls.nums = static_numbers(cls.h)
        cls.units = json.loads((DR / "coverage/coverage_summary.json").read_text())["units"]

    def ind(self, i):
        return next(x for st in self.cur["selection"]["steps"] for x in st["indicators"] if x["id"] == i)

    # ---- (1) funnel
    def test_funnel_follows_the_declared_order_and_every_indicator_names_unit_and_meaning(self):
        self.assertEqual([st["id"] for st in self.cur["selection"]["steps"]], ["catalogued", "usable", "evaluated", "pertinent", "ready"])
        for st in self.cur["selection"]["steps"]:
            self.assertIn("sel_s_" + st["id"], rv.UI_IT)
            for i in st["indicators"]:
                for k in ("sel_i_" + i["id"], "sel_n_" + i["id"], "sel_u_" + i["unit"]):
                    self.assertTrue(rv.UI_IT[k].strip(), k)
        order = [m.start() for m in (re.search(rf'data-step="{s}"', self.h) for s in ("catalogued", "usable", "evaluated", "pertinent", "ready"))]
        self.assertEqual(order, sorted(order))

    def test_funnel_counts_reproduce_from_the_per_record_flags(self):
        re_ = rv.recompute_p2(DR)
        self.assertEqual(rv.validate_p2_counts(self.counts, re_, self.units), [])
        f = self.counts["funnel"]
        for iid, key in (("catalogued", "L0_catalogued"), ("l1", "L1_with_any_target_row"), ("l2", "L2_documented_action_row_passes_artefact_rules"), ("mnet", "L3_Mnet_usable_signed_action_on_human_target_with_stable_id"),
                         ("mnet_corr", "L3b_Mnet_corroborated_by_ChEMBL_or_GtoPdb_support"), ("msig_testable", "Msig_testable_denominator_has_structure_key"), ("msig_unknown", "Msig_UNKNOWN_NO_STRUCTURE_KEY"),
                         ("msig_any", "Msig_any_context_trt_cp_signature"), ("msig_neural", "Msig_neural_lineage_context_strict")):
            self.assertEqual(self.nums[f"sel.{iid}.records"], str(f["records"][key]), iid)
            self.assertEqual(self.nums[f"sel.{iid}.families"], str(f["families"][key]), iid)
        self.assertEqual(self.nums["sel.eval_methods.records"], "0")
        self.assertEqual(self.nums["sel.eval_p3.families"], str(self.p3["nU"]))
        self.assertEqual(self.nums["sel.eval_wwox_readout.value"], str(self.cur["selection"]["steps"][2]["indicators"][2]["records"]))

    def test_funnel_percentages_and_overlaps_equal_their_numbers(self):
        for k, v in self.nums.items():
            m = re.match(r"sel\.(\w+)\.(records|families)\.pct(_testable|_catalogue)?$", k)
            if not m:
                continue
            i = self.ind(m.group(1))
            den = {"": lambda: i["den_" + m.group(2)], "_testable": lambda: i["testable_" + ("rec" if m.group(2) == "records" else "fam")], "_catalogue": lambda: i.get("den2_fam")}[m.group(3) or ""]()
            self.assertEqual(v, f"{100 * i[m.group(2)] / den:.1f}", k)
        for u in ("records", "families"):
            ov = self.cur["selection"]["overlap"][u]
            self.assertEqual(ov["both"] + ov["only_net_usable"] + ov["only_sig_neural"] + ov["neither"], ov["denominator"])
            self.assertEqual(self.nums[f"sel.overlap.{u}.denominator"], str(ov["denominator"]))
        t = self.ind("msig_unknown")
        self.assertEqual(sum(b["records"] for b in t["breakdown"]), t["records"])      # the unknown share is fully explained by named reasons
        self.assertEqual(self.ind("msig_testable")["records"] + t["records"], self.ind("catalogued")["records"])

    def test_funnel_mutations_are_refused(self):
        re_ = rv.recompute_p2(DR)
        for path in (("funnel", "records", "L1_with_any_target_row"), ("funnel", "families", "L3_Mnet_usable_signed_action_on_human_target_with_stable_id"), ("funnel", "records", "Msig_neural_lineage_context_strict")):
            c = json.loads(json.dumps(self.counts))
            d = c
            for k in path[:-1]:
                d = d[k]
            d[path[-1]] += 1
            self.assertTrue(rv.validate_p2_counts(c, re_, self.units), path)
        c = json.loads(json.dumps(self.counts))
        c["funnel"]["families"]["overlap_Mnet_vs_Msig_neural_strict_testable_only"]["both"] += 1
        self.assertTrue(rv.validate_p2_counts(c, re_, self.units))
        c = json.loads(json.dumps(self.counts))
        c["funnel"]["records"]["actually_evaluated"] = 5
        self.assertTrue(any("actually_evaluated" in e for e in rv.validate_p2_counts(c, re_, self.units)))
        c = json.loads(json.dumps(self.counts))
        c["catalogue"]["records"] += 1
        self.assertTrue(rv.validate_p2_counts(c, re_, self.units))

    def test_present_is_not_evaluated_and_the_pilot_is_not_a_screening(self):
        self.assertIn("Presenti nel catalogo non significa valutati", self.h)
        self.assertEqual(self.p3["nU"], 256)
        self.assertIn("NON è uno screening del catalogo", self.h)
        self.assertEqual(self.ind("eval_p3")["den_families"], self.counts["pilot"]["union_families"])
        self.assertIn("non è una quota di malattia trattata", self.h.replace("Una quota di vie biologiche o di bersagli collegati ", ""))
        self.assertIn("Una quota di vie biologiche o di bersagli collegati non è una quota di malattia trattata", self.h)

    def test_no_probability_and_no_model_percentile_anywhere(self):
        self.assertIn("il percentile del modello non è mostrato affatto", self.h)
        self.assertIn("Nessuna probabilità clinica calibrata è mostrata", self.h)
        body = re.sub(r"<[^>]+>", " ", self.h)
        self.assertEqual(len(re.findall(r"percentil", body, re.I)), body.count("il percentile del modello non è mostrato affatto") + len(re.findall(r"95° percentile", body)) + len(re.findall(r"stesso percentile", body)))
        for e in self.cur["hypotheses"]:
            self.assertNotIn("pct_OE", json.dumps(e))
        self.assertNotIn("pct_OE", json.dumps(self.cur["predictive"]))

    # ---- (2) hypotheses
    def test_hypotheses_keep_priority_model_and_observation_apart(self):
        hy = self.cur["hypotheses"]
        self.assertEqual([x["id"] for x in hy], [r["record_id"] for r in self.rows5])
        art = re.findall(r'<article class="hyp".*?</article>', self.h, re.S)
        self.assertEqual(len(art), len(hy))
        cm = {c["id"]: c for c in self.cur["cands"]}
        for a, x in zip(art, hy):
            for cls in ("hyp-prio", "hyp-model", "hyp-obs"):
                self.assertIn(cls, a)
            row = next(r for r in self.rows5 if r["record_id"] == x["id"])
            self.assertEqual(x["model"], "none")      # no record has a model position of its own: P5 says so for every compound
            self.assertIn("No model position", row["MODEL_position_P3_P2"] + ("" if row["MODEL_position_P3_P2"].startswith("P3") else " No model position"))
            self.assertIn(html_escape(rv.UI_IT["hyp_model_none"]), a)
            self.assertEqual(x["model_axis"], row["MODEL_position_P3_P2"].startswith("P3"))
            self.assertTrue(x["model_reasons"], x["id"])      # every record states why it has no model position
            for r in x["model_reasons"]:
                self.assertIn(html_escape(rv.UI_IT["hyp_r_" + r]), a)
            for c, ps in x["positions"].items():
                for p in ps:
                    self.assertEqual(p["group"], cm[c]["links"][p["need"]]["group"])      # priority = the position the view assigns, not the comparison file's prose
            for lab in ("hyp_dem", "hyp_opp", "hyp_missing", "hyp_ext", "hyp_next"):
                self.assertIn(html_escape(rv.UI_IT[lab]), a)
        by = {x["id"]: x for x in hy}
        self.assertEqual(sorted(x["id"] for x in hy if x["model_axis"]), ["CMP-04", "CMP-05"])      # the P3 axis result is quoted for the glycolysis axis only, and as a result about methods
        self.assertEqual(self.h.count(html_escape(rv.UI_IT["hyp_axis"])), 2)
        self.assertEqual(self.h.count(html_escape(rv.UI_IT["hyp_axis_note"])), 2)
        self.assertIn("firewalled", by["CMP-05"]["model_reasons"])
        self.assertIn("firewalled", by["CMP-07"]["model_reasons"])
        self.assertTrue(by["CMP-07"]["model_usable"])        # memantine and perampanel are in the usable census
        self.assertIn("not_compound", by["CMP-03"]["model_reasons"])
        self.assertIn("not_compound", by["CMP-06"]["model_reasons"])
        for k in ("hyp_intro_model", "hyp_key"):
            self.assertIn(html_escape(rv.UI_IT[k]), self.h)
        self.assertIn("mai un composto", rv.UI_IT["hyp_intro_model"])
        self.assertNotIn("hyp_model_no_added_value", rv.UI_IT)

    def test_hypothesis_mutations_are_refused(self):
        cards, needs = {c["id"] for c in self.cur["cands"]}, {n["id"] for n in self.cur["needs"]}
        self.assertEqual(rv.validate_hypotheses(self.rows5, cards, needs, set()), [])
        r = json.loads(json.dumps(self.rows5))
        r[0]["MODEL_position_P3_P2"] = "Positive: ranks first"
        self.assertTrue(rv.validate_hypotheses(r, cards, needs, set()))
        r = json.loads(json.dumps(self.rows5))
        r[4]["MODEL_position_P3_P2"] = r[4]["MODEL_position_P3_P2"].replace("No model position for this compound", "")
        self.assertTrue(rv.validate_hypotheses(r, cards, needs, set()))      # an axis result that no longer says the compound has no position
        r = json.loads(json.dumps(self.rows5))
        r[1]["MODEL_position_P3_P2"] = "None."
        self.assertTrue(rv.validate_hypotheses(r, cards, needs, set()))      # no reason can be read
        r = json.loads(json.dumps(self.rows5))
        r[1]["hypothesis_cards"] = "ZZ99_missing_card"
        self.assertTrue(rv.validate_hypotheses(r, cards, needs, set()))
        r = json.loads(json.dumps(self.rows5))
        r[2]["need_link"] = "NEED-NOPE"
        self.assertTrue(rv.validate_hypotheses(r, cards, needs, set()))
        r = json.loads(json.dumps(self.rows5))
        r[3]["premise_missing"] = ""
        self.assertTrue(rv.validate_hypotheses(r, cards, needs, set()))

    # ---- (3) predictive test
    def test_predictive_test_numbers_equal_the_results_and_label_is_exploratory(self):
        pr = self.cur["predictive"]
        self.assertTrue(pr["exploratory"])
        self.assertIn("ESPLORATIVO: un risultato computazionale non è efficacia terapeutica", self.h)
        self.assertEqual([v["verdict"] for v in pr["verdicts"]], ["no_added_value", "not_detected_not_excluded", "no_added_value", "inconclusive"])
        for vi, v in enumerate(pr["verdicts"]):
            for ni, n in enumerate(v["numbers"]):
                self.assertEqual(self.nums[f"pred.v{vi}.{ni}"], str(n["value"]))
        self.assertEqual(pr["verdicts"][1]["numbers"][0]["value"], round(self.p3["rho"]["SIG"], 3))
        self.assertEqual(pr["verdicts"][3]["numbers"][2]["value"], round(self.e1["regions"]["HPC"]["exact_p_one_sided"], 3))
        self.assertEqual(self.nums["pred.universe"], "256")
        self.assertEqual([n["value"] for n in pr["verdicts"][3]["numbers"]], [0.329, 0.389, 0.06, 0.396])      # both draws of the matched null are on the page
        self.assertIn("circa 0,39", self.h)
        self.assertIn("intervallo di confidenza al 90%", self.h)
        self.assertNotIn("IC90", self.h)
        for v in pr["verdicts"]:
            self.assertTrue(v["reopen_it"])
        self.assertIn("effetto non rilevato, non escluso", self.h)

    def test_predictive_mutations_are_refused(self):
        doc = json.loads((DR / rv.PRED_NAME).read_text())
        self.assertEqual(rv.validate_predictive(doc, self.p3, self.e1), [])
        d = json.loads(json.dumps(doc))
        d["verdicts"][1]["numbers"][0]["expect"] = 0.15
        self.assertTrue(rv.validate_predictive(d, self.p3, self.e1))
        d = json.loads(json.dumps(doc))
        d["verdicts"][0]["verdict"] = "improved"
        self.assertTrue(rv.validate_predictive(d, self.p3, self.e1))
        d = json.loads(json.dumps(doc))
        d["exploratory"] = False
        self.assertTrue(rv.validate_predictive(d, self.p3, self.e1))
        d = json.loads(json.dumps(doc))
        d["verdicts"][2]["numbers"][0]["path"] = "rho.NOPE"
        self.assertTrue(rv.validate_predictive(d, self.p3, self.e1))
        d = json.loads(json.dumps(doc))
        d["verdicts"][3]["external_values"][0]["check_text"] = "0.999"
        self.assertTrue(rv.validate_predictive(d, self.p3, self.e1, DR))      # the verifier's draw must still be in the verifier's report
        self.assertEqual(rv.validate_predictive(doc, self.p3, self.e1, DR), [])
        p3 = json.loads(json.dumps(self.p3))
        p3["rho"]["SIG"] = 0.2
        self.assertTrue(rv.validate_predictive(doc, p3, self.e1))      # the data moved: the text must be re-read

    # ---- (4) contexts
    def test_context_view_counts_equal_the_matrix(self):
        cx = self.cur["contexts"]
        self.assertEqual((cx["cells"], cx["measured"], cx["unknown"], cx["contexts"], cx["quantities"], cx["models"]), (182, 93, 89, 13, 14, 6))
        self.assertEqual(sum(1 for r in self.rows4 if r["direction"] == "UNKNOWN"), cx["unknown"])
        for r in cx["rows"]:
            cells = [x for x in self.rows4 if x["quantity_id"] == r["id"]]
            self.assertEqual(r["higher"], sum(1 for x in cells if x["direction"] == "higher"))
            self.assertEqual(r["lower"], sum(1 for x in cells if x["direction"] == "lower"))
            self.assertEqual(r["unknown"], sum(1 for x in cells if x["direction"] == "UNKNOWN"))
            self.assertEqual(r["higher"] + r["lower"] + r["other"] + r["unknown"], 13)
            for k in ("higher", "lower", "other", "unknown"):
                self.assertEqual(self.nums[f"ctx.{r['id']}.{k}"], str(r[k]))
        v = {r["id"]: r["verdict"] for r in cx["rows"]}
        self.assertEqual(v, {"Q01": "no_resolved_sign", "Q02": "discordant", "Q03": "single_system", "Q04": "no_resolved_sign", "Q05": "concordant", "Q06": "no_resolved_sign", "Q07": "discordant",
                             "Q08": "no_resolved_sign", "Q09": "discordant", "Q10": "discordant", "Q11": "discordant", "Q12": "single_system", "Q13": "discordant", "Q14": "concordant"})
        self.assertIn("Nessun sottogruppo di pazienti è sostenuto da questi dati", self.h)
        self.assertEqual(cx["verdict_counts"], {"no_resolved_sign": 4, "discordant": 6, "single_system": 2, "concordant": 2})
        # the printed legend IS the rule: re-derive every verdict from the matrix cells, independently of the builder's helper
        for r in cx["rows"]:
            cells = [x for x in self.rows4 if x["quantity_id"] == r["id"] and x["direction"] != "UNKNOWN"]
            signs = {x["direction"] for x in cells if x["direction"] in ("higher", "lower")}
            models = {}
            for x in cells:
                if x["direction"] in ("higher", "lower"):
                    models.setdefault(x["direction"], set()).add(cx["models_of"][x["context_id"]])
            want = ("no_data" if not cells else "discordant" if len(signs) == 2 else ("concordant" if len(next(iter(models.values()))) >= 2 else "single_system") if signs else "no_resolved_sign")
            self.assertEqual(r["verdict"], want, r["id"])
            self.assertTrue(r["note_it"])
        for r in cx["rows"]:      # the matrix shows Italian words, not raw tokens, and the full matrix is labelled with the Italian quantity names
            for d in r["directions"]:
                self.assertIn("ctx_d_" + d, rv.UI_IT)
        for tok in ("no_resolvable_sign", "lower_non_specific", "set_dependent", ">UNKNOWN<"):
            self.assertNotIn(tok, re.sub(r'data-[a-z]+="[^"]*"', "", self.h.split('id="contexts"')[1]))
        self.assertIn("Ipereccitabilità", self.h)
        for bad in ("Iperecitabilità", "deposito murino", "nullo appaiato", "furono registrati", "ricongelato", "consigliate"):
            self.assertNotIn(bad, self.h, bad)
        self.assertIn("Drosophila (mosca)", self.h)

    def test_context_mutations_are_refused(self):
        cv = json.loads((DR / rv.CTX_NAME).read_text())
        st = rv.context_stats(self.rows4, cv)
        self.assertEqual(rv.validate_contexts(cv, self.rows4, st), [])
        for q, wrong in (("Q01", "concordant"), ("Q14", "discordant"), ("Q02", "no_resolved_sign"), ("Q05", "no_resolved_sign"), ("Q07", "no_data"), ("Q03", "no_data"), ("Q12", "concordant")):
            c = json.loads(json.dumps(cv)); c["verdicts"][q]["expect"] = wrong
            self.assertTrue(rv.validate_contexts(c, self.rows4, st), (q, wrong))      # the full rule, not a necessary condition
        c = json.loads(json.dumps(cv)); c["verdicts"]["Q01"]["expect"] = "unresolved"
        self.assertTrue(rv.validate_contexts(c, self.rows4, st))
        c = json.loads(json.dumps(cv)); c["verdicts"]["Q04"]["note_it"] = ""
        self.assertTrue(rv.validate_contexts(c, self.rows4, st))
        c = json.loads(json.dumps(cv)); c["expect"]["unknown"] = 90
        self.assertTrue(rv.validate_contexts(c, self.rows4, st))
        c = json.loads(json.dumps(cv)); c["model_labels_it"].pop("rat")
        self.assertTrue(any("Italian label" in e for e in rv.validate_contexts(c, self.rows4, st)))
        c = json.loads(json.dumps(cv)); del c["verdicts"]["Q05"]
        self.assertTrue(rv.validate_contexts(c, self.rows4, st))
        rows = [dict(r) for r in self.rows4[:-1]]
        self.assertTrue(rv.validate_contexts(cv, rows, rv.context_stats(rows, cv)))      # a missing cell
        r2 = [dict(r) for r in self.rows4]
        r2[0]["direction"] = "UNKNOWN"
        self.assertTrue(rv.validate_contexts(cv, r2, rv.context_stats(r2, cv)))          # the unknown count moved
        r3 = [dict(r) for r in self.rows4]
        for r in r3:
            if r["quantity_id"] == "Q06" and r["context_id"] == "ORG_KO":
                r["direction"] = "higher"
        self.assertTrue(rv.validate_contexts(cv, r3, rv.context_stats(r3, cv)))          # a matrix change that moves a verdict must be re-read

    def test_tables_stack_on_a_phone_and_summaries_are_tappable(self):
        css = (DR / "view/assets/curated.css").read_text()
        self.assertIn(".tbl.stk td[data-label]::before", css)
        self.assertIn("details>summary{padding:3px 0;min-height:24px}", css)
        for t in re.findall(r'<table class="tbl[^"]*stk">.*?</table>', self.h, re.S):
            self.assertIn("data-label=", t)
        self.assertEqual(len(re.findall(r'<table class="tbl[^"]*stk">', self.h)), 3 + len(self.cur["ranking"]["units"]) + 2)     # three IT7 tables; IT8 P9: one pathway table per ranked entry, the uncarded items and the triggers

    def test_p4_matrix_checker_passes(self):
        r = subprocess.run([sys.executable, "-I", str(DR / rv.P4_DIR / "check_context_matrix.py")], capture_output=True, text=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stdout[-400:] + r.stderr[-400:])

    # ---- (5) readability and no JS-only content
    def test_new_sections_are_server_rendered_in_italian_and_in_the_navigation(self):
        for sid, tok in (("selection", "Selezione"), ("hypotheses", "Ipotesi a confronto"), ("predictive", "Prova e contesti")):
            self.assertIn(f'id="{sid}"', self.h)
            self.assertIn(f'<a href="#{sid}">{tok}</a>', self.h)
        self.assertIn('id="contexts"', self.h)
        js = (DR / "view/assets/curated.js").read_text()
        self.assertIn("#section=", js)
        self.assertEqual(self.h.count('href="#section='), 7)     # selection, hypotheses, predictive and, from IT8 P9, four on the ranking (controls, print, section end, one-page)
        for k in ("sec_print", "sec_unknown", "sec_title"):
            self.assertTrue(rv.UI_IT[k])

    def test_shareable_build_carries_the_new_sections_without_third_party_wording(self):
        sh = rv.build_payload(DR, "shareable")["cur"]
        self.assertEqual(sh["selection"], self.cur["selection"])
        self.assertEqual(sh["predictive"], self.cur["predictive"])
        page = re.sub(r"<script\b.*?</script>", "", rv.build(DR, "shareable"), flags=re.S)
        text = " ".join(re.sub(r"<[^>]+>", " ", re.search(rf'<section id="{i}".*?</section>', page, re.S).group(0)) for i in ("selection", "hypotheses", "predictive"))
        for bad in ("DTC", "TTD", "OncoKB", "CancerCommons", "MyCancerGenome", "TALC", "Drug Target Commons", "DrugBank", "alvocidib", "saracatinib", "pyruvate dehydrogenase kinase inhibitor"):
            self.assertNotIn(bad, text, bad)


class It7P7Browser(Browser):
    def test_section_print_route_shows_one_section_without_duplicate_ids(self):
        for sid, h2 in (("selection", "Selezione dei composti"), ("hypotheses", "Ipotesi a confronto"), ("predictive", "Prova predittiva")):
            d = self.dom("#section=" + sid)
            area = d[d.index('id="export-area"'):]
            self.assertIn("exporting", d)
            self.assertIn(f'data-section="{sid}"', area)
            self.assertIn(h2, area)
            self.assertNotIn('class="btnlink"', area)       # the print links of the section itself are not repeated inside it

    def test_sections_render_with_javascript_too(self):
        d = self.dom("#selection")
        self.assertEqual(d.count('class="sel-ind"'), sum(len(st["indicators"]) for st in self.P["cur"]["selection"]["steps"]))
        self.assertEqual(d.count('class="hyp"'), 9)


@unittest.skipUnless(HAVE_DATA, "module data absent")
class It7P7Deployment(unittest.TestCase):
    """The deployment is PREPARED, not performed: a generated file table, a manual-only workflow kept as a proposal outside .github, and the reserved decision stated."""

    @classmethod
    def setUpClass(cls):
        import hashlib
        import repurposing_shareable_package as pk
        cls.pk, cls.hashlib = pk, hashlib
        cls.text = (DR / "view/DEPLOY.md").read_text(encoding="utf-8")
        cls.wf = (DR / "view/DEPLOY_pages_workflow.proposal.yml").read_text(encoding="utf-8")
        cls.base = DR / "view/shareable_package"

    def table(self):
        a, b = self.text.index(self.pk.DEPLOY_BEGIN), self.text.index(self.pk.DEPLOY_END)
        return {m.group(1): (int(m.group(2)), m.group(3)) for m in re.finditer(r"^\| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})` \|$", self.text[a:b], re.M)}

    def test_file_table_equals_the_package_on_disk_and_the_manifest(self):
        t = self.table()
        on_disk = {str(p.relative_to(self.base)): p for p in self.base.rglob("*") if p.is_file()}
        self.assertEqual(set(t), set(on_disk))
        man = json.loads((self.base / "manifest.json").read_text())["files"]
        for rel, (n, h) in t.items():
            b = on_disk[rel].read_bytes()
            self.assertEqual((n, h), (len(b), self.hashlib.sha256(b).hexdigest()), rel)
            if rel != "manifest.json":
                self.assertEqual(man[rel]["sha256"], h, rel)
        self.assertIn("NOTICE.md", t)
        self.assertTrue(any(k.startswith("LICENSES/") for k in t))
        self.assertTrue(any(k.startswith("class_b/") for k in t))
        files = {rel: p.read_bytes() for rel, p in on_disk.items()}
        self.assertEqual(self.pk.deploy_text(DR, files), self.text)      # `package --check` would also pass
        files["index.html"] += b" "
        self.assertNotEqual(self.pk.deploy_text(DR, files), self.text)    # mutation: a changed byte makes the table stale

    def test_workflow_is_a_manual_only_proposal_outside_github_dir(self):
        self.assertIn("PROPOSAL ONLY", self.wf)
        on = re.search(r"^on:\n((?:  .*\n)+)", self.wf, re.M).group(1)
        self.assertEqual([l.strip() for l in on.splitlines() if l.strip()], ["workflow_dispatch:"])
        for bad in ("push", "schedule", "pull_request", "workflow_run"):
            self.assertNotRegex(on, bad)
        self.assertIn("manifest.json", self.wf)
        top = re.search(r"^permissions:\n((?:  .*\n)+)", self.wf, re.M).group(1)
        self.assertNotIn("pages", top)          # least privilege: the verify job cannot write Pages
        self.assertNotIn("id-token", top)
        dep = self.wf[self.wf.index("  deploy:"):]
        self.assertIn("pages: write", dep)
        self.assertIn("id-token: write", dep)
        self.assertIn("sections 6 and 9", self.wf)
        self.assertIn("DEPLOY_DOC", self.wf)      # the verify job also checks manifest.json, against the table of DEPLOY.md
        tracked = subprocess.run(["git", "-C", str(DR), "ls-files", "--full-name", "../../../../.github"], capture_output=True, text=True).stdout.split()
        self.assertEqual(tracked, [".github/workflows/public-release-gate.yml"])      # nothing was added under .github

    def test_document_states_destinations_rollback_preconditions_and_the_reserved_decision(self):
        for h in ("## 1. What is deployed", "## 2. Proposed destinations", "## 4. The exact file set and hashes", "## 5. Reproducible build and check", "## 6. Modifications needed",
                  "## 7. Preconditions", "## 8. Rollback", "## 9. What is reserved to the operator"):
            self.assertIn(h, self.text)
        for needle in ("without creating an account or spending", "package --check", "audit-shareable --dynamic", "does not change what the history already holds", "act of external publication",
                       "history or visibility remedy", "Nothing has been published", "not verifiable from inside the repository"):
            self.assertIn(needle, self.text.replace("\n", " ").replace("  ", " "))
        for needle in ("default branch", "robots", "disable the Pages source", "integrity check, not a content check"):
            self.assertIn(needle, self.text.replace("\n", " ").replace("  ", " "))
        self.assertNotRegex(self.text, r"[Àèéìòù]")      # English, as the repository's other files


if __name__ == "__main__":
    unittest.main(verbosity=1)
