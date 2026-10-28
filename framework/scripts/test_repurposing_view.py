#!/usr/bin/env python3
"""Offline regressions for repurposing_view.py: headline counts equal the module's source JSON,
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
        self.assertEqual(len(self.P["dispositions"]), 7)
        self.assertEqual(len({d["id"] for d in self.P["dispositions"]}), 7)
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

    def test_levels_never_summed(self):
        self.assertNotRegex(self.page, r"L1\s*\+\s*L2")
        self.assertTrue(self.P["tech"]["never_summed"])

    def test_dgidb_licence_and_regeneration_present(self):
        self.assertIn("NOT CLEARED FOR PUBLIC RELEASE", self.page)
        self.assertIn("repurposing_coverage.py run", self.page)

    def test_size_and_self_contained(self):
        self.assertLess(len(self.page.encode()), rv.MAX_BYTES)
        self.assertNotRegex(self.page, r'(src|href)="https?://')
        self.assertNotIn("<link ", self.page)

    def test_determinism(self):
        self.assertEqual(rv.build(DR), self.page)

    def test_committed_view_is_current(self):
        out = DR / "view/index.html"
        if out.exists():
            self.assertEqual(out.read_text(encoding="utf-8"), self.page, "run repurposing_view.py run")

    def test_no_personal_or_contact_data(self):
        self.assertNotRegex(self.page, r"[\w.+-]+@[\w-]+\.[\w.]+")


class States(unittest.TestCase):
    def manifest(self, statuses):
        return {"sources": {k: {"name": k.upper(), "last_attempt": {"status": s, "detail": "d-" + k, "utc": "2026-01-01T00:00:00Z"},
                                "data": {"retrieved_utc": "2026-01-01T00:00:00Z", "version": "v1"}, "licence": "L"} for k, s in statuses.items()}}

    def test_states_distinct_from_ok_and_each_other(self):
        sts = {"a": "OK", "b": "FAILED", "c": "STALE", "d": "TRUNCATED", "e": "NOT_FETCHED", "f": "weird"}
        rows = rv.source_rows(self.manifest(sts), {}, {"source_states": sts})
        classes = {r["id"]: r["state_class"] for r in rows}
        self.assertEqual(classes, {"a": "ok", "b": "failed", "c": "stale", "d": "truncated", "e": "not_fetched", "f": "other"})
        page = rv.render_sources(rows)
        for c in ("failed", "stale", "truncated", "not_fetched", "other"):
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
        rows = rv.source_rows(self.manifest({"dgidb": "OK"}), {}, {"source_states": {"dgidb": "stale"}})
        self.assertEqual(rows[0]["state_class"], "stale")

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

    def dom(self, frag=""):
        r = subprocess.run([self.bin, "--headless=new", "--disable-gpu", "--no-sandbox", f"--user-data-dir={self.tmp.name}/p",
                            "--virtual-time-budget=5000", "--dump-dom", f"file://{self.html}{frag}"], capture_output=True, text=True, timeout=120)
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
        self.assertEqual(len(self.P["dispositions"]), 7)

    def test_criteria_and_card_link_navigation(self):
        d = self.dom("#f=need:NEED-T-TYPE-CALCIUM&disp:consistent_mechanism_candidate&openall:1")
        self.assertIn("Discriminating experiment named", d)
        d2 = self.dom("#f=q:bumetanide&openall:1")
        self.assertRegex(d2, r'href="\.\./cards/[A-Za-z0-9_-]+\.card\.json"')


if __name__ == "__main__":
    unittest.main(verbosity=1)
