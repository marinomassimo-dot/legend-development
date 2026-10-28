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

    def test_units_never_conflated(self):
        n = static_numbers(self.full)
        cur = self.PF["cur"]
        self.assertEqual(n["cur.needs"], "22")
        self.assertEqual(n["cur.cards"], str(len(cur["cands"])))
        self.assertNotEqual(n["cur.cards"], n["funnel.records"])
        for key, unit in (("cur.needs", "needs"), ("cur.cards", "candidate cards"), ("funnel.records", "catalogue records"), ("funnel.families", "catalogue families"),
                          ("funnel.evaluated_records", "records evaluated against WWOX"), ("funnel.families_with_link", "families with a documented link")):
            self.assertRegex(self.full, rf'data-k="{re.escape(key)}"[^<]*</b></span><span class="u">{re.escape(unit)}<')
        self.assertIn("never added or compared as one number", self.full)
        self.assertIn("a family is not a distinct drug and not a candidate", self.full)

    def test_two_goals_and_track_are_separate_dimensions(self):
        n = static_numbers(self.full)
        d, p = n["cur.goal.deep_recovery.cards"], n["cur.goal.partial_benefit.cards"]
        self.assertEqual(int(d) + int(p), len([c for c in self.PF["cur"]["cands"] if c["goal"]]))
        self.assertEqual(int(n["cur.goal.deep_recovery.needs"]) + int(n["cur.goal.partial_benefit.needs"]), 22)
        self.assertEqual(self.full.count('class="goal '), 2)
        self.assertIn("Track (a separate field)", self.full)
        self.assertIn("2026-", re.search(r'data-k="meta.data_date" data-v="([^"]+)"', self.full).group(1))

    def test_groups_are_reasoned_and_unscored(self):
        cur = self.PF["cur"]
        ids = {g["id"] for g in cur["groups"]}
        self.assertEqual(ids, {"G1", "G2", "G3", "G4"})
        for c in cur["cands"]:
            for nid, l in c["links"].items():
                self.assertIn(l["group"], ids)
                self.assertEqual(len(l["reasons"]), 6)
                if l["group"] == "G1":
                    self.assertGreater(l["n_w"], 0)
                if c["abstention"]:
                    self.assertEqual(l["group"], "G4")
        blob = json.dumps(cur)
        for bad in ('"score"', '"rank"', '"probability"', '"cure'):
            self.assertNotIn(bad, blob)
        self.assertIn("no score, no probability and no cure ranking", self.full)

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
        self.assertIn("Data date:", area)
        self.assertIn("Perimeter:", area)
        self.assertNotIn("deepdive_manifests", area)
        self.assertNotRegex(area, r'href="\.\./')

    def test_candidate_profile_five_answers_and_scope_labels(self):
        d = self.dom("#c=need:NEED-T-TYPE-CALCIUM")
        for q in ("1. Why are we studying it?", "2. What was observed in WWOX?", "3. What comes from other diseases or predictions?", "4. Counter-evidence", "5. What proof is missing"):
            self.assertIn(q, d)
        self.assertIn("WWOX experiment in a DEE system", d)
        self.assertIn("Other-disease precedent", d)

    def test_filters_narrow_the_curated_views(self):
        d = self.dom("#c=goal:deep_recovery")
        m = re.search(r'id="c-count"[^>]*>(\d+) of (\d+) needs and (\d+) of (\d+) candidate', d)
        needs = [n for n in self.P["cur"]["needs"] if n["goal"] == "deep_recovery"]
        cands = [c for c in self.P["cur"]["cands"] if c["goal"] == "deep_recovery"]
        self.assertEqual((int(m.group(1)), int(m.group(3))), (len(needs), len(cands)))

    def test_ranking_groups_rendered_with_reasons(self):
        d = self.dom("#c=need:NEED-WWOX-GENE-ADDITION")
        self.assertIn('data-group="G1"', d)
        self.assertIn("reasons for this position (six criteria)", d)

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
        self.assertIn("OPPOSED to the wanted direction", d)
        self.assertIn("raises while", d)
        self.assertIn("No synergy is inferred", d)

    def test_no_horizontal_overflow_at_phone_width(self):
        page = (Path(self.tmp.name) / "v.html").read_text(encoding="utf-8")
        h2 = Path(self.tmp.name) / "sw.html"
        h2.write_text(page.replace("</body>", "<script>setTimeout(function(){document.body.setAttribute('data-sw',document.documentElement.scrollWidth+'/'+window.innerWidth)},400)</script></body>"), encoding="utf-8")
        d = self.dom("", html=h2, width=390)
        a, b = map(int, re.search(r'data-sw="(\d+)/(\d+)"', d).group(1, 2))
        self.assertLessEqual(a, b)


if __name__ == "__main__":
    unittest.main(verbosity=1)
