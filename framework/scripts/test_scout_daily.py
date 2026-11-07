#!/usr/bin/env python3
"""scout_daily: baseline selects nothing, no change is silent, a change or a new PMID is selected."""
import json
import tempfile
import unittest
from pathlib import Path

import scout_daily as sd

WATCH = [{"id": "Tool", "kind": "gh", "repo": "o/r", "q": "q?", "vs": "v"},
         {"id": "Acc", "kind": "url", "url": "https://x/ACC", "q": "q?", "vs": "v"},
         {"id": "Db", "kind": "json", "url": "https://x/s", "path": ["v"], "q": "q?", "vs": "v"}]
QUERIES = [("a", "WWOX")]


def make_opener(tag="v1", lic="MIT", acc=401, ver="X_1"):
    def opener(url, method="GET", body=None, etag=None):
        if url.endswith("/releases?per_page=1"):
            return 200, {"ETag": "W/1"}, json.dumps([{"tag_name": tag}]).encode()
        if url.endswith("/repos/o/r"):
            return 200, {}, json.dumps({"license": {"spdx_id": lic}, "archived": False}).encode()
        if url.endswith("/ACC"):
            return acc, {}, b""
        return 200, {}, json.dumps({"v": ver}).encode()
    return opener


def pm(ids):
    def opener(url):
        if "esearch" in url:
            return 200, json.dumps({"esearchresult": {"idlist": ids}}).encode()
        return 200, json.dumps({"result": {i: {"title": f"title {i}"} for i in ids}}).encode()
    return opener


def go(state, **kw):
    ids = kw.pop("ids", ["1", "2"])
    return sd.run(state, WATCH, QUERIES, make_opener(**kw), pm(ids))


class Radar(unittest.TestCase):
    def test_baseline_then_silence_then_changes(self):
        report, state = go({})
        self.assertEqual(("BASELINE", []), (report["verdict"], report["selected"]))
        report, state2 = go(state)
        self.assertEqual("NO_USEFUL_CHANGE", report["verdict"])
        report, _ = go(state2, tag="v2", lic="GPL-3.0", acc=200, ver="X_2", ids=["3", "1", "2"])
        self.assertEqual("SELECTED", report["verdict"])
        by_id = {s["id"]: s for s in report["selected"]}
        self.assertEqual({"Tool", "Acc", "Db", "PubMed:a"}, set(by_id))
        self.assertIn("'MIT' -> 'GPL-3.0'", by_id["Tool"]["detail"])  # licence change is visible
        self.assertIn("401", by_id["Acc"]["detail"])
        self.assertTrue(by_id["PubMed:a"]["detail"].startswith("3 title 3"))

    def test_error_keeps_last_good_fingerprint_and_never_selects(self):
        _, state = go({})
        report, state2 = sd.run(state, WATCH, QUERIES, lambda *a, **k: (500, {}, b""), pm(["1", "2"]))
        self.assertEqual("NO_USEFUL_CHANGE", report["verdict"])
        self.assertEqual(3, len(report["errors"]))
        self.assertEqual(state["watch"], state2["watch"])

    def test_no_contact_parameter_in_pubmed_urls(self):
        urls = []
        def opener(url):
            urls.append(url)
            return 200, json.dumps({"esearchresult": {"idlist": []}}).encode()
        sd.run({}, [], QUERIES, make_opener(), opener)
        self.assertTrue(urls and not any(p in u for u in urls for p in ("email=", "tool=", "api_key=")))

    def test_pending_entry_and_append_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            item = {"id": "Tool", "wwox_question": "q?", "contribution_vs_existing": "v", "detail": "d",
                    "estimated_cost": "c", "licence": "MIT", "proof": "p", "outcome": "TO_TRIAGE"}
            (directory / "scout_daily_pending_log.md").write_text(sd.entry_markdown(item, "2026-10-27T05:20:00"))
            log = directory / "log.md"
            log.write_text("# log\n")
            sd.append_log(directory, log)
            self.assertIn("## 2026-10-27 · scout_daily · Tool", log.read_text())
            self.assertFalse((directory / "scout_daily_pending_log.md").exists())


class RelevantResource(unittest.TestCase):
    """Each probe observes the resource whose change matters; availability is not a capability."""

    def opener(self, hf_card="c1", hf_license=None, explorer=503, commit="2024-05-06T00:00:00Z"):
        def opener(url, method="GET", body=None, etag=None):
            if "huggingface.co/api/datasets/o/d/tree" in url:
                return 200, {}, json.dumps([{"path": "README.md", "oid": hf_card}]).encode()
            if "huggingface.co/api/datasets/o/d" in url:
                card = {"license": hf_license} if hf_license else {}
                return 200, {}, json.dumps({"cardData": card, "tags": [], "gated": False}).encode()
            if url == "https://explorer.example":
                return explorer, {}, b""
            if url.endswith("/releases?per_page=1"):
                return 200, {}, b"[]"
            if "/commits?" in url:
                return 200, {}, json.dumps([{"commit": {"committer": {"date": commit}}}]).encode()
            if url.endswith("/repos/o/r"):
                return 200, {}, json.dumps({"license": {"spdx_id": "MIT"}, "default_branch": "main"}).encode()
            return 404, {}, b""
        return opener

    WATCH = [{"id": "Data", "kind": "hf", "repo": "o/d", "q": "licence stated?", "vs": "v"},
             {"id": "Explorer", "kind": "avail", "url": "https://explorer.example", "signal": "availability",
              "q": "up?", "vs": "v"},
             {"id": "Repo", "kind": "gh", "repo": "o/r", "q": "changed?", "vs": "v"}]

    def test_data_licence_explorer_status_and_commit_are_the_signals(self):
        report, state = sd.run({}, self.WATCH, [], self.opener(), pm([]))
        self.assertEqual("BASELINE", report["verdict"])
        self.assertIsNone(state["watch"]["Data"]["fp"]["license"])
        self.assertFalse(state["watch"]["Explorer"]["fp"]["reachable"])
        self.assertEqual("2024-05-06T00:00:00Z", state["watch"]["Repo"]["fp"]["last_commit"])
        report, state = sd.run(state, self.WATCH, [], self.opener(explorer=503), pm([]))
        self.assertEqual("NO_USEFUL_CHANGE", report["verdict"], "a still-down explorer is silence")
        report, _ = sd.run(state, self.WATCH, [], self.opener(hf_card="c2", hf_license="cc-by-4.0", explorer=200,
                                                              commit="2026-10-27T00:00:00Z"), pm([]))
        by_id = {x["id"]: x for x in report["selected"]}
        self.assertEqual({"Data", "Explorer", "Repo"}, set(by_id))
        self.assertIn("'cc-by-4.0'", by_id["Data"]["detail"])
        self.assertTrue(by_id["Explorer"]["outcome"].startswith("AVAILABILITY SIGNAL"))
        self.assertTrue(by_id["Repo"]["outcome"].startswith("TO_TRIAGE"))

    def test_a_redefined_fingerprint_rebaselines_instead_of_reporting_a_change(self):
        state = {"watch": {"Data": {"fp": {"status": 200, "etag": "x"}}}, "pubmed": {}}
        report, _ = sd.run(state, self.WATCH[:1], [], self.opener(), pm([]))
        self.assertEqual("BASELINE", report["watch"][0]["result"])
        self.assertEqual([], report["selected"])


class Discovery(unittest.TestCase):
    THEMES = [{"id": "t1", "gap": "gap one", "epmc": "WWOX", "gh": "q"},
              {"id": "t2", "gap": "gap two", "epmc": None, "gh": "q2"}]
    NOW = sd.dt.datetime(2026, 10, 27, tzinfo=sd.dt.timezone.utc)

    @staticmethod
    def opener(url, method="GET", body=None, etag=None):
        if "europepmc" in url:
            recs = [{"source": "MED", "id": str(n), "title": f"<i>t{n}</i> &amp; x", "firstPublicationDate": "2026-01-01"}
                    for n in range(6)]
            return 200, {}, json.dumps({"resultList": {"result": recs}}).encode()
        items = [{"full_name": f"o{n}/r{n}", "stargazers_count": n, "html_url": "u", "pushed_at": "2026-01-01T00:00:00Z",
                  "license": None} for n in range(5)]
        return 200, {}, json.dumps({"items": items}).encode()

    def test_rotation_once_a_day_dedup_and_cap(self):
        result, st = sd.discover({}, self.THEMES, self.opener, self.NOW)
        self.assertEqual("t1", result["themes"][0]["theme"])
        self.assertEqual(2 * sd.SHOW, result["new_items"])
        self.assertEqual("t0 & x", result["themes"][0]["items"][0]["title"])  # markup and entities removed
        self.assertIsNone(sd.discover(st, self.THEMES, self.opener, self.NOW)[0], "one search per calendar day")
        later = self.NOW + sd.dt.timedelta(days=1)
        result2, st2 = sd.discover(st, self.THEMES, self.opener, later)
        self.assertEqual("t2", result2["themes"][0]["theme"])
        result3, _ = sd.discover(st2, self.THEMES, self.opener, later + sd.dt.timedelta(days=1))
        self.assertEqual("t1", result3["themes"][0]["theme"])
        self.assertEqual(3, result3["new_items"], "shown items are not shown again; the unshown epmc remainder surfaces")

    def test_failure_is_reported_not_raised_and_empty_is_valid(self):
        result, _ = sd.discover({}, self.THEMES, lambda *a, **k: (403, {}, b""), self.NOW)
        self.assertEqual(0, result["new_items"])
        self.assertTrue(result["themes"][0]["errors"])
        self.assertEqual([], sd.discovery_entries(result, "2026-10-27"))

    def test_radar_status_is_information(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            self.assertEqual("NO_REPORT", sd.radar_status(d)["status"])
            (d / "scout_daily.json").write_text(json.dumps({"run_at": "2026-10-27T05:20:01+00:00", "verdict": "SELECTED",
                                                            "errors": ["x"], "selected": [{"id": "A"}]}))
            (d / "scout_daily_pending_log.md").write_text("\n## one\n\n## two\n")
            info = sd.radar_status(d, sd.dt.datetime(2026, 10, 28, 5, 20, tzinfo=sd.dt.timezone.utc))
            self.assertEqual(("OK", ["A"], 2), (info["status"], info["to_examine"], info["pending_log_entries"]))
            stale = sd.radar_status(d, sd.dt.datetime(2026, 10, 30, tzinfo=sd.dt.timezone.utc))
            self.assertEqual("STALE", stale["status"])
            self.assertIn("RADAR STALE", sd.status_line(stale))


class CatalogueProbes(unittest.TestCase):
    """Release/date/hash probes: changed vs unchanged, and a failure is an error, never 'no change'."""
    W = [{"id": "Ftp", "kind": "regex", "url": "https://x/ftp", "pattern": r'href="(chembl_\d+_sqlite\.tar\.gz)"', "q": "q", "vs": "v"},
         {"id": "Dg", "kind": "json", "method": "POST", "digest": True, "url": "https://x/g",
          "path": ["data", "nodes"], "q": "q", "vs": "v"}]

    @staticmethod
    def opener(listing='<a href="chembl_37_sqlite.tar.gz">', nodes=(("A", "1"),), code=200):
        def opener(url, method="GET", body=None, etag=None):
            if code != 200:
                return code, {}, b""
            if url.endswith("ftp"):
                return 200, {}, listing.encode()
            return 200, {}, json.dumps({"data": {"nodes": [{"n": a, "v": b} for a, b in nodes]}}).encode()
        return opener

    def test_change_unchanged_and_failure(self):
        _, st = sd.run({}, self.W, [], self.opener(), pm([]))
        r, st2 = sd.run(st, self.W, [], self.opener(), pm([]))
        self.assertEqual(["UNCHANGED"] * 2, [x["result"] for x in r["watch"]])
        r, _ = sd.run(st2, self.W, [], self.opener(listing='<a href="chembl_38_sqlite.tar.gz">', nodes=(("A", "2"),)), pm([]))
        self.assertEqual(["CHANGED"] * 2, [x["result"] for x in r["watch"]])
        r, st3 = sd.run(st2, self.W, [], self.opener(code=503), pm([]))
        self.assertEqual(["ERROR"] * 2, [x["result"] for x in r["watch"]])
        self.assertEqual(2, len(r["errors"]))
        self.assertEqual(st2["watch"], st3["watch"], "last good fingerprint kept")

    def test_a_listing_without_the_pattern_is_an_error_not_unchanged(self):
        r, _ = sd.run({}, self.W[:1], [], self.opener(listing="<html>moved</html>"), pm([]))
        self.assertEqual("ERROR", r["watch"][0]["result"])


def fake_git(sha="a" * 40, blobs=None, texts=None, ls_fail=False, have_objects=True, calls=None):
    blobs = blobs or {}
    texts = texts or {}
    calls = calls if calls is not None else []

    def runner(args):
        calls.append(list(args))
        if args[0] == "ls-remote":
            return (2, "") if ls_fail else (0, f"{sha}\trefs/heads/main\n")
        if args[0] == "rev-parse" and args[1].startswith(f"{sha}:"):
            return 0, blobs.get(args[1].split(":", 1)[1], "b0") + "\n"
        if args[0] == "rev-parse":
            return 1, ""
        if args[0] == "cat-file":
            return (0 if have_objects else 1), ""
        if args[0] == "show":
            return 0, texts.get(args[1].split(":", 1)[1], "# x\n")
        return 0, ""
    return runner, calls


ROAD = sd.CONTEXT_FILES[0]
LOGF = sd.CONTEXT_FILES[2]


class ContextRefresh(unittest.TestCase):
    TEXTS = {ROAD: "# Roadmap\n\nUpdated 2026-10-29 by x\n\nsee https://github.com/Old/Repo\n",
             LOGF: "## 2026-10-30 · scout_daily · A\n"}

    def test_cache_hit_refresh_on_advance_and_unchanged_blob_reuse(self):
        runner, calls = fake_git(texts=self.TEXTS, blobs={ROAD: "r1", LOGF: "l1"})
        ctx = sd.resolve_context({}, runner)
        self.assertEqual(("refreshed", "a" * 40), (ctx["cache"], ctx["main_sha"]))
        self.assertIn("old/repo", ctx["files"][ROAD]["repos"])
        shows = sum(c[0] == "show" for c in calls)
        self.assertEqual(3, shows)  # roadmap, readme, log read at the revision
        runner2, calls2 = fake_git(texts=self.TEXTS, blobs={ROAD: "r1", LOGF: "l1"})
        again = sd.resolve_context(ctx, runner2)
        self.assertEqual("hit", again["cache"])
        self.assertFalse([c for c in calls2 if c[0] in ("show", "rev-parse")], "same SHA: nothing re-read")
        runner3, calls3 = fake_git(sha="b" * 40, texts=self.TEXTS, blobs={ROAD: "r1", LOGF: "l2"})
        moved = sd.resolve_context(again, runner3)
        self.assertEqual(("refreshed", "b" * 40), (moved["cache"], moved["main_sha"]))
        self.assertEqual(1, sum(c[0] == "show" for c in calls3), "only the changed blob (log) is re-read")

    def test_old_current_heading_does_not_outrank_later_evidence(self):
        runner, _ = fake_git(texts=self.TEXTS)
        ctx = sd.resolve_context({}, runner)
        self.assertEqual("2026-10-29", ctx["roadmap_dated"])
        self.assertTrue(any("2026-10-30" in x for x in ctx["outranked_by"]))

    def test_unverifiable_remote_states_a_freshness_limit(self):
        runner, _ = fake_git(texts=self.TEXTS)
        ctx = sd.resolve_context({}, runner)
        down, _ = fake_git(ls_fail=True)
        stale = sd.resolve_context(ctx, down)
        self.assertEqual("stale_reused", stale["cache"])
        self.assertIn("NOT verified", stale["freshness_limit"])
        none = sd.resolve_context({}, down)
        self.assertIn("unavailable", none["freshness_limit"])
        gone, _ = fake_git(sha="c" * 40, have_objects=False)
        lag = sd.resolve_context(ctx, gone)
        self.assertIn("not available locally", lag["freshness_limit"])


def channel_opener(gh=200, hf=200, nature=200, hf_items=(), nature_items=(), gh_items=(), calls=None):
    def opener(url, method="GET", body=None, etag=None):
        if calls is not None:
            calls.append(url)
        if "api.github.com/search" in url:
            return gh, {}, json.dumps({"items": list(gh_items)}).encode()
        if "api.github.com/repos" in url and "/commits" in url:
            return 200, {}, json.dumps([{"sha": "f" * 40, "commit": {"committer": {"date": "2026-10-30T00:00:00Z"}}}]).encode()
        if "api.github.com/repos" in url and "/releases/latest" in url:
            return 404, {}, b""
        if "huggingface.co/api/models/" in url or "huggingface.co/api/datasets/" in url:
            return 200, {}, json.dumps({"sha": "c" * 40, "lastModified": "2026-10-01T00:00:00Z",
                                        "cardData": {"license": "mit"}, "siblings": [{"rfilename": "README.md"}]}).encode()
        if "huggingface.co/api" in url:
            return hf, {}, json.dumps(list(hf_items) if "/models?" in url else []).encode()
        if "api.crossref.org" in url:
            return nature, {}, json.dumps({"message": {"items": list(nature_items)}}).encode()
        return 200, {}, json.dumps({"resultList": {"result": []}}).encode()
    return opener


def gh_repo(name, pushed="2026-10-20T00:00:00Z"):
    return {"full_name": name, "stargazers_count": 9999, "html_url": "u/" + name, "pushed_at": pushed,
            "license": {"spdx_id": "MIT"}, "default_branch": "main"}


def hf_model(ident, modified="2026-10-20T00:00:00Z"):
    return {"id": ident, "lastModified": modified, "downloads": 1, "likes": 0, "tags": ["license:apache-2.0"]}


def nat(doi, title, venue="Nature Methods"):
    return {"DOI": doi, "title": [title], "container-title": [venue], "issued": {"date-parts": [[2026, 10, 5]]},
            "type": "journal-article", "license": [{"URL": "https://x/lic"}]}


T = [{"id": "q1", "category": "prediction/evaluation", "gap": "gap one", "decision": "d1", "kw": "kw one", "epmc": None, "gh": "g"},
     {"id": "q2", "category": "databases", "gap": "gap two", "decision": "d2", "kw": "kw two", "epmc": None, "gh": "g2"}]
NOW = sd.dt.datetime(2026, 11, 1, tzinfo=sd.dt.timezone.utc)


class Channels(unittest.TestCase):
    def test_three_channels_each_with_its_own_outcome(self):
        calls = []
        op = channel_opener(gh_items=[gh_repo("a/tool-x")], hf_items=[hf_model("b/model-y")],
                            nature_items=[nat("10.1038/s1", "A long enough title about a method")], calls=calls)
        result, _ = sd.discover({}, T, op, NOW, per_run=1, deep=3)
        ch = result["channels"]
        self.assertEqual(["delta"] * 3, [ch[c]["outcome"] for c in ("github", "huggingface", "nature")])
        self.assertEqual("not_queried", ch["europepmc"]["outcome"])
        self.assertTrue(any("models?" in u for u in calls) and any("datasets?" in u for u in calls)
                        and any("spaces?" in u for u in calls), "models, datasets and Spaces are all searched")
        item = next(i for r in result["themes"] for i in r["items"] if i["channel"] == "github")
        self.assertEqual("fffffffffff"[:11], item["versions"]["last_commit"]["sha"][:11])
        self.assertEqual("none published", item["versions"]["latest_release"], "commit and release kept apart")
        self.assertEqual("unknown", item["claims"]["independently_reproduced"])
        self.assertIn("code", item["licences"])
        hf = next(i for r in result["themes"] for i in r["items"] if i["channel"] == "huggingface")
        self.assertEqual("mit", hf["versions"]["card_licence"])
        self.assertIn("weights", hf["licences"])

    def test_error_is_not_no_news_and_no_news_is_not_error(self):
        result, _ = sd.discover({}, T, channel_opener(gh=403, hf=503), NOW)
        ch = result["channels"]
        self.assertEqual("error", ch["github"]["outcome"])
        self.assertEqual("error", ch["huggingface"]["outcome"])
        self.assertEqual("no_news", ch["nature"]["outcome"], "answered, nothing new: not an error")
        self.assertTrue(ch["github"]["errors"] and "403" in ch["github"]["errors"][0])
        rep = {"run_at": "2026-11-01T00:00:00+00:00", "selected": [], "errors": ["x"], "discovery": result, "context": {}}
        text = sd.briefing(rep, {"state": "ok"})
        self.assertIn("github error", text)
        self.assertIn("nature no_news", text)
        self.assertIn("NEXT STEP: inspect the errors", text)

    def test_a_probe_of_a_known_resource_is_not_a_discovery(self):
        op = channel_opener(gh_items=[gh_repo("Known/Repo")])
        result, _ = sd.discover({}, T, op, NOW, known={"known/repo"})
        self.assertEqual("no_news", result["channels"]["github"]["outcome"])
        self.assertEqual(["known/repo"], result["channels"]["github"]["known_resources"])
        self.assertEqual(0, result["new_items"])

    def test_ranking_is_not_by_popularity(self):
        op = channel_opener(gh_items=[dict(gh_repo("a/old-repo", "2025-01-01T00:00:00Z"), stargazers_count=99999),
                                      dict(gh_repo("a/new-repo", "2026-10-30T00:00:00Z"), stargazers_count=1)])
        result, _ = sd.discover({}, T, op, NOW)
        first = [i for i in result["themes"][0]["items"] if i["channel"] == "github"][0]
        self.assertEqual("a/new-repo", first["title"])
        self.assertIn("stars", first["popularity"])


class LimitsRotationAndFullWatchlist(unittest.TestCase):
    LIM = {"max_teams": 6, "max_repos": 18, "max_per_team": 3}

    def entry(self, team, n, rel=1):
        return {"team": team, "repo": f"{team}/r{n}", "source": "s", "reason": "r", "reopen": "o", "relevance": rel}

    def test_caps_are_enforced_and_replacement_keeps_the_reason(self):
        f = {"entries": []}
        for t in range(6):
            for n in range(3):
                self.assertEqual("added", sd.follow_add(f, self.entry(f"t{t}", n, rel=2), self.LIM, "2026-11-01")[0])
        self.assertEqual(18, sum(e["status"] == "active" for e in f["entries"]))
        self.assertEqual("refused", sd.follow_add(f, self.entry("t9", 0, rel=2), self.LIM, "2026-11-01")[0], "equal relevance does not displace")
        self.assertEqual("refused", sd.follow_add(f, self.entry("t0", 9, rel=2), self.LIM, "2026-11-01")[0], "3 per team")
        verdict, detail = sd.follow_add(f, self.entry("t0", 9, rel=5), self.LIM, "2026-11-01")
        self.assertEqual("replaced", verdict)
        sus = [e for e in f["entries"] if e["status"] == "suspended"]
        self.assertEqual(1, len(sus))
        self.assertTrue(sus[0]["source"] and sus[0]["reason"] and sus[0]["reopen"] and sus[0]["suspended_for"])
        verdict, _ = sd.follow_add(f, self.entry("t9", 0, rel=9), self.LIM, "2026-11-01")
        self.assertEqual("replaced", verdict)
        self.assertLessEqual(len({e["team"] for e in f["entries"] if e["status"] == "active"}), 6)
        self.assertLessEqual(sum(e["status"] == "active" for e in f["entries"]), 18)

    def test_slots_are_not_filled_and_missing_reasons_are_refused(self):
        f = sd.follow_seed()
        self.assertLess(sum(e["status"] == "active" for e in f["entries"]), 18)
        bad = self.entry("x", 1)
        bad["reopen"] = ""
        self.assertEqual("refused", sd.follow_add(f, bad, self.LIM, "2026-11-01")[0])

    def test_weekly_deep_check_rotates_and_never_expands_collaborators(self):
        f = sd.follow_seed()
        now = sd.dt.datetime(2026, 11, 1, tzinfo=sd.dt.timezone.utc)
        self.assertEqual(3, len(sd.follow_due(f, now, 7, 5)))
        f["entries"][0]["last_deep"] = "2026-10-31T00:00:00+00:00"
        f["entries"][1]["last_deep"] = "2026-10-01T00:00:00+00:00"
        due = sd.follow_due(f, now, 7, 5)
        self.assertEqual([f["entries"][2]["repo"], f["entries"][1]["repo"]], [e["repo"] for e in due], "never-checked first, then oldest")
        calls = []
        sd.repo_versions("a/b", channel_opener(calls=calls))
        self.assertFalse([u for u in calls if "contributors" in u or "collaborators" in u or "/members" in u])

    def test_discovery_keeps_running_with_a_full_watchlist(self):
        full = {"entries": [dict(self.entry(f"t{t}", n), status="active", added="2026-11-01") for t in range(6) for n in range(3)]}
        known = sd.known_idents([], full, {})
        op = channel_opener(gh_items=[gh_repo("fresh/finding")])
        result, st = sd.discover({}, T, op, NOW, per_run=2, open_slot=True, known=known)
        self.assertEqual(["q1", "q2", "open-slot"], [r["theme"] for r in result["themes"]])
        self.assertEqual("delta", result["channels"]["github"]["outcome"])
        self.assertEqual(0, st["cursor"], "two questions of two asked: the cursor wrapped")
        again, _ = sd.discover(st, T, op, NOW + sd.dt.timedelta(days=1), per_run=2)
        self.assertEqual(["q1", "q2"], [r["theme"] for r in again["themes"]])

    def test_configuration_overrides_the_limits_only_with_valid_types(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "scout_daily_config.json").write_text(json.dumps(
                {"follow": {"max_teams": 2, "max_repos": "many", "bogus": 1}, "questions_per_run": 3}))
            cfg = sd.load_config(Path(tmp))
        self.assertEqual((2, 18, 3), (cfg["follow"]["max_teams"], cfg["follow"]["max_repos"], cfg["questions_per_run"]))


class DedupTraceAndPersistence(unittest.TestCase):
    def test_papers_and_mirrors_count_once(self):
        a = {"key": "epmc:1", "kind": "paper", "title": "A Benchmark Of Repurposing Methods Across Cohorts", "doi": "10.1/x",
             "channel": "europepmc", "url": "u1", "checks": {}}
        b = {"key": "nature:1", "kind": "paper", "title": "A benchmark of repurposing methods across cohorts!", "doi": "10.1/x",
             "channel": "nature", "url": "u2", "checks": {}}
        c = {"key": "gh:1", "kind": "repository", "title": "o/repurposing-bench", "channel": "github", "url": "u3", "checks": {}}
        d = {"key": "hf:1", "kind": "dataset", "title": "p/repurposing-bench", "channel": "huggingface", "url": "u4", "checks": {}}
        kept = sd.dedup([a, b, c, d])
        self.assertEqual(2, len(kept))
        self.assertEqual({"nature", "huggingface"}, {m["channel"] for k in kept for m in k["mirrors"]})
        self.assertIn("shared origin", kept[0]["checks"]["shared_origin"])

    def test_decision_states_demand_evidence_and_keep_plan_apart_from_verified(self):
        tr = {}
        self.assertFalse(sd.trace_event(tr, "k", "examination", "examined", "source_read", "ref")[0], "no signal yet")
        self.assertTrue(sd.trace_event(tr, "k", "signal", "signalled")[0])
        ok, why = sd.trace_event(tr, "k", "examination", "examined", "log_line", "capability_scout_log.md")
        self.assertFalse(ok)
        self.assertIn("log line", why)
        self.assertFalse(sd.trace_event(tr, "k", "decision", "adopt")[0], "decision needs an examination")
        self.assertTrue(sd.trace_event(tr, "k", "examination", "examined", "source_read", "https://example.org/paper section 2")[0])
        self.assertTrue(sd.trace_event(tr, "k", "decision", "adopt")[0])
        self.assertTrue(sd.trace_event(tr, "k", "integration", "adopted_in_plan")[0])
        summary = sd.trace_summary(tr)["k"]
        self.assertEqual(("integration", False), (summary["furthest"], summary["verified_implementation"]))
        self.assertFalse(sd.trace_event(tr, "k", "integration", "verified", "source_read", "x")[0])
        self.assertTrue(sd.trace_event(tr, "k", "integration", "verified", "test_run", "framework/scripts/test_scout_daily.py::x")[0])
        self.assertTrue(sd.trace_summary(tr)["k"]["verified_implementation"])
        self.assertFalse(sd.trace_event(tr, "k2", "signal", "bogus")[0])

    def test_save_state_preserves_concurrent_edits_and_reports_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.json"
            path.write_text(json.dumps({"watch": {"old": 1}, "follow": {"entries": [{"repo": "added/by-hand", "status": "active"}]},
                                        "trace": {"manual": {"history": []}}}))
            ok, _ = sd.save_state(path, {"watch": {"new": 2}}, None, lambda t: dict(t, auto={"history": []}))
            self.assertTrue(ok)
            cur = json.loads(path.read_text())
            self.assertEqual({"new": 2}, cur["watch"])
            self.assertEqual("added/by-hand", cur["follow"]["entries"][0]["repo"], "concurrent follow edit kept")
            self.assertEqual({"manual", "auto"}, set(cur["trace"]))
            bad = Path(tmp) / "no" / "dir" / "x"
            bad.parent.parent.write_text("a file, so mkdir must fail")
            ok, why = sd.save_state(bad, {})
            self.assertFalse(ok)
            self.assertTrue(why)

    def test_briefing_claims_a_save_only_after_success(self):
        rep = {"run_at": "2026-11-01T00:00:00+00:00", "selected": [], "errors": [], "context": {"main_sha": "a" * 40, "cache": "hit"}}
        quiet = sd.briefing(rep, {"state": "ok", "report": "ok"})
        self.assertIn("NEXT STEP: none; nothing useful today", quiet)
        self.assertIn("No material delta.", quiet)
        self.assertIn("Saved: state", quiet)
        failed = sd.briefing(rep, {"state": "ok", "report": "read-back differs"})
        self.assertIn("SAVE FAILED: report", failed)
        self.assertIn("inspect the errors", failed)
        with tempfile.TemporaryDirectory() as tmp:
            blocker = Path(tmp) / "f"
            blocker.write_text("x")
            ok, why = sd.save_text(blocker / "child.md", "t")
            self.assertFalse(ok)
            p = Path(tmp) / "log.md"
            self.assertTrue(sd.save_text(p, "one\n", append=True)[0])
            self.assertTrue(sd.save_text(p, "two\n", append=True)[0])
            self.assertEqual("one\ntwo\n", p.read_text(), "append preserves earlier entries")

    def test_briefing_puts_one_next_step_first_and_lists_deltas_with_decision(self):
        item = {"id": "Discovery:q1", "wwox_question": "gap one", "decision": "d1", "roadmap": "R3", "detail": "[repository/github] a/b",
                "estimated_cost": "minutes", "licence": "per part", "outcome": "TO_TRIAGE", "test": "reproduce one result"}
        rep = {"run_at": "2026-11-01T00:00:00+00:00", "selected": [item, dict(item, id="Discovery:q2")], "errors": [],
               "context": {"main_sha": "a" * 40, "freshness_limit": "remote main NOT verified"}}
        text = sd.briefing(rep, {"state": "ok"})
        lines = text.splitlines()
        self.assertTrue(lines[1].startswith("NEXT STEP: examine Discovery:q1"))
        self.assertEqual(1, sum(l.startswith("NEXT STEP") for l in lines))
        self.assertIn("FRESHNESS LIMIT", text)
        self.assertIn("-> d1", text)


class VerifierRegressions(unittest.TestCase):
    def test_follow_add_refuses_missing_text_not_the_string_none(self):
        f = sd.follow_seed()
        base = {"team": "t", "repo": "t/r", "relevance": 1}
        for missing in ("source", "reason", "reopen"):
            new = dict(base, source="s", reason="r", reopen="o")
            new[missing] = None
            self.assertEqual("refused", sd.follow_add(f, new, {"max_teams": 6, "max_repos": 18, "max_per_team": 3}, "2026-11-01")[0])
        self.assertFalse(any(e["source"] == "None" or e["reopen"] == "None" for e in f["entries"]))

    def test_trace_ref_must_exist_else_stays_claimed(self):
        tr = {}
        sd.trace_event(tr, "k", "signal", "signalled")
        sd.trace_event(tr, "k", "examination", "examined", "source_read", "https://example.org/paper")
        sd.trace_event(tr, "k", "decision", "adopt")
        ok, why = sd.trace_event(tr, "k", "integration", "verified", "record_file", "no/such/record.md")
        self.assertFalse(ok)
        self.assertIn("claimed", why)
        self.assertFalse(sd.trace_summary(tr)["k"]["verified_implementation"])
        self.assertEqual("claimed", tr["k"]["history"][-1]["state"])
        self.assertTrue(sd.trace_event(tr, "k", "integration", "verified", "record_file", "framework/scripts/scout_daily.py")[0])
        self.assertFalse(sd.trace_event({"z": {"history": [{"stage": "signal", "state": "signalled"}]}}, "z", "integration",
                                        "verified", "record_file", "../../etc/passwd")[0])

    def test_damaged_state_is_moved_aside_not_replaced_or_crashing(self):
        for content in ('{"follow": {"entries": [', "[1, 2]", '"text"', '{"follow": [], "trace": 3}'):
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "scout_daily_state.json"
                path.write_text(content)
                del sd.STATE_NOTES[:]
                state = sd.read_state(path)
                self.assertIsInstance(state, dict)
                self.assertTrue(sd.STATE_NOTES)
                self.assertTrue((Path(tmp) / "scout_daily_state.json.bad").exists())
                ok, _ = sd.save_state(path, {"watch": {}})
                self.assertTrue(ok)
                self.assertIsInstance(json.loads(path.read_text()), dict)

    def test_save_state_keeps_a_damaged_file_as_bad(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "s.json"
            path.write_text('{"trace": {"a": ')
            del sd.STATE_NOTES[:]
            self.assertTrue(sd.save_state(path, {"watch": {}})[0])
            self.assertIn('"a"', (Path(tmp) / "s.json.bad").read_text())
            self.assertTrue(sd.STATE_NOTES)

    def test_total_search_failure_does_not_advance_rotation(self):
        result, st = sd.discover({"cursor": 3, "last_day": "2026-10-31"}, T, channel_opener(gh=500, hf=500, nature=500), NOW)
        self.assertTrue(result["rotation_held"])
        self.assertEqual((3, "2026-10-31"), (st["cursor"], st["last_day"]))
        ok, st2 = sd.discover({"cursor": 0}, T, channel_opener(gh=500), NOW)
        self.assertFalse(ok["rotation_held"], "partial failure still consumes the day")
        self.assertEqual("2026-11-01", st2["last_day"])

    def test_cli_does_not_say_saved_for_a_refusal(self):
        import contextlib
        import io
        import os
        with tempfile.TemporaryDirectory() as tmp:
            os.environ["LEGEND_SCOUT_DIR"] = tmp
            try:
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    rc = sd.main(["--follow-add", "t/r"])
                self.assertEqual(1, rc)
                self.assertNotIn("saved:", buf.getvalue())
                self.assertIn("REFUSED", buf.getvalue())
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    rc = sd.main(["--trace", "nokey", "--stage", "examination", "--state", "examined"])
                self.assertEqual(1, rc)
                self.assertNotIn("saved:", buf.getvalue())
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    rc = sd.main(["--follow-add", "t/r", "--source", "s", "--reason", "r", "--reopen", "o"])
                self.assertEqual((0, True), (rc, "saved:" in buf.getvalue()))
            finally:
                del os.environ["LEGEND_SCOUT_DIR"]

    def test_verdict_is_computed_from_the_final_selection(self):
        self.assertEqual("SELECTED", sd.final_verdict({"selected": [{"id": "Discovery:x"}], "baseline": True}))
        self.assertEqual("BASELINE", sd.final_verdict({"selected": [], "baseline": True}))
        self.assertEqual("NO_USEFUL_CHANGE", sd.final_verdict({"selected": [], "baseline": False}))

# ---------------------------------------------------------------------------------------------
# IT17 P2: questions derived from the current priority surfaces; one level of team exploration.
# Time is CONTROLLED (fixed datetimes passed in): these tests exercise the weekly/cooldown logic, they are NOT a
# multi-week observation of the radar.
import hashlib

MOD = sd.MODULE
TASK_P = f"{sd.TASK_DIR}/ORCH-ROADMAP-IT17-20261101.json"
TASK_OLD = f"{sd.TASK_DIR}/ORCH-ROADMAP-IT16-20261101.json"
DIAG_P = f"{MOD}/diagnosis_it16_20261101/README.md"
PKG_P = f"{MOD}/pkg_it16_p3_20261101/README.md"
WO_P = sd.SURFACE_PATHS["work_order"]
RM_P = sd.SURFACE_PATHS["roadmap"]
RD_P = sd.SURFACE_PATHS["readme"]


def roadmap_text(extra=""):
    return ("# Roadmap\n\nUpdated 2026-11-01 by x\n\n" + extra + "\n| ID | Inc | Out | Crit |\n|---|---|---|---|\n"
            "| R3 / first | **Network prediction comparison.** Reuse LINCS. | A reproducible comparison of signature reversal "
            "and a network method. | Establish added information. |\n")


def diag_text(evaluation="no independent outcome set exists for the evaluation of predictions"):
    return ("# Diagnosis\n\n| Stage | Declared | Implemented | Executed | Advantage | Validation missing |\n|---|---|---|---|---|---|\n"
            f"| Evaluation | R3 | nothing | no | none | **principal bottleneck**: {evaluation} |\n"
            "| Presentation | R10 | view | yes | none | - |\n"
            "| Networks | R1 | typed | partly | not diagnosed | not diagnosed this session |\n")


def task_text(p1="TODO", p3="TODO"):
    steps = lambda *s: {"steps": [{"step": t, "status": st, "owner": "scientist", "evidence": ""} for t, st in s]}
    return json.dumps({"TASK_ID": "ORCH-ROADMAP-IT17-20261101", "AUTHORISED_QUEUE_20261101D": {
        "MANDATE_STATE": "OPEN",
        "OBJ_P1": steps(("P1.1 cache read-side validation of the retrieval responses", p1)),
        "OBJ_P3": steps(("P3 prospective evaluation with an immutable freeze of outcome semantics", p3)),
        "OBJ_P5": steps(("P5 science: only the decision-changing reads", "TODO"))}})


def work_order_text(*needs):
    return json.dumps({"entries": [{"need": n, "question": q, "would_change": w} for n, q, w in needs]})


def readme_text(planned="Only planned: an independent benchmark of repurposing predictions.", link="pkg_it16_p3_20261101/README.md"):
    return (f"# Module\n\n### Roadmap iteration 16 (2026-11-01) - measured state, CURRENT, task `X`\n\nSee [p]({link}). {planned}\n\n"
            "### Roadmap iteration 15 (2026-11-01) - measured state, (previous state)\n\nNext: this must never be read.\n")


def pkg_text(row="| ChEMBL offline dump | WATCH | 5.76 GB; reopen if the REST failures recur beyond a window |"):
    return f"# Pkg\n\n| Resource | Verdict | Note |\n|---|---|---|\n{row}\n"


def plan_files(**over):
    files = {RM_P: roadmap_text(), DIAG_P: diag_text(), TASK_P: task_text(), WO_P: work_order_text(
        ("NEED-A", "Does a pharmacological chaperone restore the missense protein?", "whether the chaperone arm is run")),
        RD_P: readme_text(), PKG_P: pkg_text(), TASK_OLD: task_text()}
    files.update(over)
    return files


def plan_git(files, sha="c" * 40, calls=None):
    blob = lambda t: hashlib.sha1(t.encode()).hexdigest()

    def runner(args):
        if calls is not None:
            calls.append(list(args))
        if args[0] == "ls-tree":
            d = args[3]
            kids = sorted({p[len(d):].split("/")[0] for p in files if p.startswith(d)})
            return 0, "".join(f"{d}{k}\n" for k in kids)
        path = args[1].split(":", 1)[1] if len(args) > 1 and ":" in args[1] else None
        if args[0] == "rev-parse":
            return (0, blob(files[path]) + "\n") if path in files else (128, "")
        if args[0] == "show":
            return (0, files[path]) if path in files else (128, "")
        return 0, ""
    return runner


CTX = {"main_sha": "c" * 40, "cache": "refreshed", "freshness_limit": None}
T0 = sd.dt.datetime(2026, 11, 1, 5, 20, tzinfo=sd.dt.timezone.utc)


def derive(files=None, cached=None, extracts=None, ctx=CTX, calls=None):
    return sd.resolve_plan(cached, extracts, ctx, plan_git(files or plan_files(), calls=calls), T0)


def by_id(plan):
    return {q["id"]: q for q in plan["questions"]}


class PlanFromPriorities(unittest.TestCase):
    def test_each_surface_generates_a_question_with_a_traceable_origin(self):
        plan, _ = derive()
        ids = by_id(plan)
        self.assertEqual({"diagnosis:evaluation", "task_step:OBJ_P1/P1.1", "task_step:OBJ_P3/P3", "work_order:NEED-A",
                          "roadmap:R3", "reopen:pkg_it16_p3_20261101/ChEMBL offline dump"} | {k for k in ids if k.startswith("open_item:")},
                         set(ids))
        q = ids["diagnosis:evaluation"]
        self.assertEqual((DIAG_P, "c" * 40), (q["origin"]["path"], q["origin"]["sha"]))
        self.assertEqual(plan["inputs"][DIAG_P]["blob"], q["origin"]["blob"], "the blob that proves the question is recorded")
        self.assertIn("closing", q["decision"])
        self.assertIn("Evaluation", sd.origin_line(q["origin"]))
        self.assertIn("principal bottleneck", ids["diagnosis:evaluation"]["origin"]["priority"])
        self.assertEqual(4, q["weight"], "a principal bottleneck outweighs an ordinary row")
        self.assertNotIn("task_step:OBJ_P5/P5", ids, "task text without a search hook is internal work, not a search question")
        self.assertFalse([k for k in ids if "Presentation" in k or "Networks" in k], "no gap stated, nothing to ask")
        self.assertEqual([], plan["provisional"])
        self.assertIn("principal", " ".join(sd.key_terms(q["origin"]["priority"], 6)) + " principal")
        self.assertFalse([k for k in ids if "must never" in ids[k]["gap"]], "the previous iteration section is not read")

    def test_open_items_come_only_from_the_section_marked_current(self):
        plan, _ = derive()
        items = [q for q in plan["questions"] if q["id"].startswith("open_item:")]
        self.assertEqual(1, len(items))
        self.assertIn("independent benchmark", items[0]["gap"])

    def test_changing_a_relevant_priority_changes_the_question_and_only_that_one(self):
        plan, _ = derive()
        changed, _ = derive(plan_files(**{DIAG_P: diag_text("no held-out chaperone benchmark exists for repurposing")}))
        a, b = by_id(plan), by_id(changed)
        self.assertEqual(set(a), set(b))
        diff = {k for k in a if a[k]["kw"] != b[k]["kw"]}
        self.assertEqual({"diagnosis:evaluation"}, diff)
        self.assertNotEqual(plan["digest"], changed["digest"])
        self.assertNotEqual(a["diagnosis:evaluation"]["origin"]["blob"], b["diagnosis:evaluation"]["origin"]["blob"])
        asked = {f"{q['id']}|{sd.digest(q['kw'])}": "2026-11-01" for q in plan["questions"]}
        first = sd.pick_questions(changed["questions"], asked, T0 + sd.dt.timedelta(days=1), 1)
        self.assertEqual("diagnosis:evaluation", first[0]["id"], "a reworded priority is asked at once, ahead of answered ones")

    def test_an_irrelevant_edit_changes_nothing(self):
        plan, _ = derive()
        same, _ = derive(plan_files(**{RM_P: roadmap_text("A new introductory paragraph about the dashboard layout."),
                                       DIAG_P: diag_text() + "\nA closing remark.\n"}))
        self.assertEqual(plan["digest"], same["digest"], "the questions are identical although two surface blobs changed")
        self.assertNotEqual(plan["inputs"][RM_P]["blob"], same["inputs"][RM_P]["blob"])

    def test_a_correction_marked_done_stops_generating(self):
        plan, _ = derive()
        done, _ = derive(plan_files(**{TASK_P: task_text(p1="DONE", p3="DONE")}))
        self.assertIn("task_step:OBJ_P1/P1.1", by_id(plan))
        self.assertNotIn("task_step:OBJ_P1/P1.1", by_id(done))
        self.assertNotIn("task_step:OBJ_P3/P3", by_id(done))
        self.assertIn("diagnosis:evaluation", by_id(done), "a DONE step does not silence a different surface")

    def test_a_resolved_reopen_condition_or_removed_need_stops_generating(self):
        key = "reopen:pkg_it16_p3_20261101/ChEMBL offline dump"
        self.assertIn(key, by_id(derive()[0]))
        for row in ("| ChEMBL offline dump | ADOPT | 5.76 GB; adopted after the REST failures recurred |",
                    "| ChEMBL offline dump | WATCH | 5.76 GB; no condition stated |"):
            plan, _ = derive(plan_files(**{PKG_P: pkg_text(row)}))
            self.assertNotIn(key, by_id(plan), row)
        gone, _ = derive(plan_files(**{WO_P: work_order_text()}))
        self.assertNotIn("work_order:NEED-A", by_id(gone))

    def test_unchanged_blobs_are_not_reread_and_a_changed_one_is(self):
        files = plan_files()
        plan, ex = derive(files)
        calls = []
        again, ex2 = derive(files, plan, ex, calls=calls)
        self.assertEqual(("hit", 0), (again["cache"], again["reread"]))
        self.assertFalse([c for c in calls if c[0] == "show"], "no surface text was fetched")
        files[WO_P] = work_order_text(("NEED-B", "Is a glial reactivity assay available?", "whether the glia lever is run"))
        third, _ = derive(files, again, ex2)
        self.assertEqual(("re-derived", 1), (third["cache"], third["reread"]))
        self.assertIn("work_order:NEED-B", by_id(third))

    def test_an_unverified_sha_or_a_missing_surface_is_flagged_not_hidden(self):
        plan, ex = derive()
        stale, _ = derive(cached=plan, extracts=ex, ctx={"main_sha": None, "cache": "refreshed"})
        self.assertTrue(any("STALE" in r for r in stale["provisional"]))
        self.assertEqual(plan["digest"], stale["digest"], "the cached plan is used, labelled provisional")
        none, _ = derive(ctx={"main_sha": None})
        self.assertEqual([], none["questions"])
        self.assertTrue(none["provisional"])
        files = plan_files()
        del files[DIAG_P]
        partial, _ = derive(files)
        self.assertTrue(any("diagnosis" in r for r in partial["provisional"]))
        limited, _ = derive(ctx=dict(CTX, freshness_limit="remote main NOT verified"))
        self.assertIn("remote main NOT verified", limited["provisional"])

    def test_the_latest_record_wins_not_the_first(self):
        old = task_text(p1="TODO")
        plan, _ = derive(plan_files(**{TASK_OLD: old, TASK_P: task_text(p1="DONE")}))
        self.assertNotIn("task_step:OBJ_P1/P1.1", by_id(plan), "IT16 is older than IT17: its open step is not read")

    def test_selection_rotates_by_weight_and_age_and_the_entry_states_its_chain(self):
        plan, _ = derive()
        qs = plan["questions"]
        first = sd.pick_questions(qs, {}, T0, 2)
        self.assertEqual(4, first[0]["weight"])
        asked = {f"{q['id']}|{sd.digest(q['kw'])}": "2026-11-01" for q in first}
        second = sd.pick_questions(qs, asked, T0, 2)
        self.assertFalse({q["id"] for q in first} & {q["id"] for q in second})
        op = channel_opener(gh_items=[gh_repo("someone/tool-x")])
        result, _ = sd.discover({}, first, op, NOW, per_run=2, open_slot=True)
        entries = sd.discovery_entries(result, "2026-11-01")
        text = sd.entry_markdown(entries[0], "2026-11-01T05:20:00")
        self.assertIn("**Why asked.**", text)
        self.assertIn(first[0]["origin"]["path"], text)
        self.assertIn("blob " + first[0]["origin"]["blob"][:10], text)
        self.assertIn("**If confirmed (decision).**", text)
        report = {"run_at": "x", "selected": entries, "errors": [], "discovery": {"channels": result["channels"],
                  "questions": result["questions"]}, "plan": {"sha": "c" * 40, "inputs": plan["inputs"], "cache": "hit", "reread": 0,
                  "questions": len(qs), "digest": plan["digest"], "provisional": ["why"]}}
        brief = sd.briefing(report)
        self.assertIn("because: ", brief)
        self.assertIn("PLAN PROVISIONAL: why", brief)
        self.assertIn("open slot: no priority assumed", brief)


class TeamExploration(unittest.TestCase):
    TERMS = ["chaperone", "missense"]

    @staticmethod
    def listing(owner, n, matching=True, fork=False):
        return [{"full_name": f"{owner}/chaperone-tool{i}" if matching else f"{owner}/other{i}", "fork": fork, "archived": False,
                 "pushed_at": f"2026-10-{10 + i:02d}T00:00:00Z", "description": "missense stability" if matching else "web app",
                 "license": {"spdx_id": "MIT"}, "html_url": f"https://github.com/{owner}/x{i}", "topics": []} for i in range(n)]

    def opener(self, table, calls=None):
        def op(url, method="GET", body=None, etag=None):
            if calls is not None:
                calls.append(url)
            for owner, recs in table.items():
                if f"/users/{owner}/repos" in url or f"author={owner}" in url:
                    return 200, {}, json.dumps(recs if "datasets?" not in url else []).encode()
            return 404, {}, b""
        return op

    def test_one_bounded_level_of_public_work_with_a_motive(self):
        calls = []
        res = sd.explore_team("github", "bigorg", self.TERMS, set(), (), self.opener({"bigorg": self.listing("bigorg", 15)}, calls),
                              limit=3, now=NOW)
        self.assertEqual(3, len(res["candidates"]), "a prolific team lists at most repos_per_team")
        self.assertTrue(all(c["matched"] for c in res["candidates"]), "every lead names the shared term that motivates it")
        self.assertEqual(15, res["scanned"])
        self.assertEqual(1, len(calls), "one listing call, nothing recursive")
        self.assertFalse([u for u in calls if "contributors" in u or "collaborators" in u or "followers" in u or "members" in u])

    def test_unmotivated_forks_archived_known_and_already_listed_are_excluded(self):
        table = {"o": self.listing("o", 3, matching=False) + self.listing("o", 2, fork=True) + self.listing("o", 1)}
        res = sd.explore_team("github", "o", self.TERMS, {"o/chaperone-tool0"}, (), self.opener(table), now=NOW)
        self.assertEqual([], res["candidates"])
        self.assertEqual(3, res["no_match"])
        again = sd.explore_team("github", "o", self.TERMS, set(), (), self.opener(table), now=NOW)
        self.assertEqual(1, len(again["candidates"]))
        later = sd.explore_team("github", "o", self.TERMS, set(), [again["candidates"][0]["ident"]], self.opener(table), now=NOW)
        self.assertEqual([], later["candidates"], "an entry listed before is not listed again")

    def test_an_error_is_reported_and_not_an_empty_result(self):
        res = sd.explore_team("github", "ghost", self.TERMS, set(), (), self.opener({}), now=NOW)
        self.assertEqual(1, len(res["errors"]))
        self.assertEqual([], res["candidates"])

    def test_hugging_face_owner_uses_models_and_datasets_listings(self):
        calls = []

        def op(url, method="GET", body=None, etag=None):
            calls.append(url)
            recs = [{"id": "lab/chaperone-model", "lastModified": "2026-10-10T00:00:00Z", "tags": ["license:mit"]}]
            return 200, {}, json.dumps(recs if "/models?" in url else []).encode()
        res = sd.explore_team("huggingface", "lab", self.TERMS, set(), (), op, now=NOW)
        self.assertEqual(2, len(calls))
        self.assertEqual(["lab/chaperone-model"], [c["title"] for c in res["candidates"]])

    def test_a_prolific_team_does_not_monopolise_discovery_or_exploration(self):
        flood = [gh_repo(f"bigorg/tool-{i}", pushed=f"2026-10-{10 + i:02d}T00:00:00Z") for i in range(12)]
        other = [gh_repo("small/lonely-tool")]
        op = channel_opener(gh_items=flood + other)
        result, _ = sd.discover({}, T, op, NOW, per_run=2)
        shown = [i["title"] for r in result["themes"] for i in r["items"] if i["channel"] == "github"]
        self.assertLessEqual(sum(t.startswith("bigorg/") for t in shown), 2, "at most two items of one owner in a run")
        self.assertIn("small/lonely-tool", shown, "the cap leaves room for a different team")
        self.assertGreater(result["channels"]["github"]["owner_capped"], 0)
        # exploration: one team a day, the longest-unexplored first, and a cooldown
        items = [i for r in result["themes"] for i in r["items"]]
        explored = {}
        picked_days = []
        for day in range(4):
            now = NOW + sd.dt.timedelta(days=day)
            pick = sd.pick_owners(items, None, explored, now, 14, 1)
            self.assertLessEqual(len(pick), 1)
            for _, owner, _ in pick:
                explored[owner] = {"last": now.isoformat(timespec="seconds")}
                picked_days.append(owner)
        self.assertEqual(len(picked_days), len(set(picked_days)), "no team is explored twice inside the cooldown")
        self.assertEqual({"bigorg", "small"}, set(picked_days), "both teams are reached; the prolific one does not repeat")
        late = sd.pick_owners(items, None, explored, NOW + sd.dt.timedelta(days=15), 14, 1)
        self.assertEqual(1, len(late), "after the cooldown a team is eligible again")

    def test_team_step_explores_the_owner_of_a_find_and_traces_each_lead(self):
        plan, _ = derive()
        picked = [by_id(plan)["work_order:NEED-A"]]
        terms = picked[0]["domain"][:2]
        self.assertEqual(2, len(terms))
        listing = [{"full_name": f"lab/{terms[0]}-kit", "fork": False, "archived": False, "pushed_at": "2026-10-20T00:00:00Z",
                    "description": "about " + terms[1], "license": None, "html_url": "https://github.com/lab/k", "topics": []}]
        found = {"themes": [{"theme": q["id"], "origin": q["origin"], "gap": q["gap"], "decision": q["decision"],
                             "category": q["category"], "items": [{"channel": "github", "ident": "lab/first", "title": "lab/first"}
                                                                  if n == 0 else {"channel": "nature", "title": "p"}]}
                            for n, q in enumerate(picked)]}
        cfg = sd.load_config(Path(tempfile.mkdtemp()))
        summary, selected, explored, events = sd.team_step(found, {"entries": []}, {}, picked, set(), cfg,
                                                           self.opener({"lab": listing}), NOW)
        self.assertEqual(1, len(summary["explored"]))
        self.assertEqual(["Team:lab"], [s["id"] for s in selected])
        self.assertIn("owner of discovered lab/first", selected[0]["detail"])
        self.assertIn("other public work matching", selected[0]["detail"])
        self.assertTrue(selected[0]["origin"]["path"], "the lead carries the priority that motivated it")
        self.assertEqual(f"team:lab/{terms[0]}-kit", events[0][0])
        self.assertIn("lab", explored)
        shown = [dict(i, ident="lab/%s-kit" % terms[0]) for i in found["themes"][0]["items"] if i["channel"] == "github"]
        found2 = {"themes": [dict(found["themes"][0], items=shown)]}
        none = sd.team_step(found2, {"entries": []}, {}, picked, set(), cfg, self.opener({"lab": listing}), NOW)
        self.assertEqual([], none[1], "an entry the run already shows as a discovery is not offered again as other work")
        again = sd.team_step(found, {"entries": []}, explored, picked, set(), cfg, self.opener({"lab": listing}), NOW)
        self.assertEqual([], again[0]["explored"], "inside the cooldown nothing is requested")

    def test_a_full_follow_list_does_not_block_new_discovery_or_exploration(self):
        full = {"entries": [dict(team=f"t{t}", repo=f"t{t}/r{n}", status="active", relevance=3, source="s", reason="r", reopen="o",
                                 added="2026-11-01", last_deep=None, fp=None) for t in range(6) for n in range(3)]}
        known = sd.known_idents([], full, {})
        op = channel_opener(gh_items=[gh_repo("fresh/finding")])
        result, _ = sd.discover({}, T, op, NOW, per_run=2, known=known)
        self.assertEqual("delta", result["channels"]["github"]["outcome"])
        owners = sd.pick_owners([i for r in result["themes"] for i in r["items"]], full, {}, NOW, 14, 1)
        self.assertEqual("fresh", owners[0][1], "the newly discovered owner is reachable although 18 repos are followed")


class SignalToDecision(unittest.TestCase):
    def test_a_real_signal_reaches_a_traced_decision_with_evidence_that_exists(self):
        plan, _ = derive()
        picked = sd.pick_questions(plan["questions"], {}, T0, 1)
        op = channel_opener(gh_items=[gh_repo("lab/chaperone-kit")])
        result, _ = sd.discover({}, picked, op, NOW, per_run=1)
        item = result["themes"][0]["items"][0]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "rec.md").write_text("examined: README and head commit read; licence MIT; no WWOX data\n")
            trace = {}
            key, at = item["key"], "2026-11-01T05:20:00"
            self.assertTrue(sd.trace_event(trace, key, "signal", "signalled", at=at, via="question:" + picked[0]["id"], root=root)[0])
            self.assertFalse(sd.trace_event(trace, key, "decision", "defer", at=at, root=root)[0], "no decision before an examination")
            self.assertFalse(sd.trace_event(trace, key, "examination", "examined", "log_line", "rec.md", at, root)[0])
            self.assertFalse(sd.trace_event(trace, key, "examination", "examined", "record_file", "missing.md", at, root)[0],
                             "an evidence file that does not exist leaves the stage claimed")
            self.assertTrue(sd.trace_event(trace, key, "examination", "examined", "record_file", "rec.md", at, root)[0])
            self.assertTrue(sd.trace_event(trace, key, "trial", "not_needed", at=at, root=root)[0])
            self.assertTrue(sd.trace_event(trace, key, "decision", "defer", at=at, root=root)[0])
            summ = sd.trace_summary(trace)[key]
            self.assertEqual("decision", summ["furthest"])
            self.assertFalse(summ["verified_implementation"])
            self.assertEqual("question:" + picked[0]["id"], trace[key]["history"][0]["via"], "the signal names the question that produced it")
            self.assertFalse(sd.trace_event(trace, key, "integration", "adopted_in_plan", at=at, root=root)[0],
                             "integration needs decision adopt; a deferral is not an adoption")


class WeeklyLogicWithControlledTime(unittest.TestCase):
    """The weekly deep check and the exploration cooldown, with injected clocks. NOT a multi-week observation."""

    def test_known_projects_are_due_weekly_and_a_new_discovery_is_due_daily(self):
        follow = {"entries": [dict(team="t", repo="t/r", status="active", relevance=3, source="s", reason="r", reopen="o",
                                   added="2026-10-25", last_deep=T0.isoformat(), fp=None)]}
        self.assertEqual([], sd.follow_due(follow, T0 + sd.dt.timedelta(days=6), 7, 3))
        self.assertEqual(["t/r"], [e["repo"] for e in sd.follow_due(follow, T0 + sd.dt.timedelta(days=8), 7, 3)])
        op = channel_opener(gh_items=[gh_repo("a/one-tool"), gh_repo("b/two-tool")])
        r1, st = sd.discover({}, T, op, NOW, per_run=1)
        r2, _ = sd.discover(st, T, channel_opener(gh_items=[gh_repo("c/three-tool")]), NOW + sd.dt.timedelta(days=1), per_run=1)
        self.assertTrue(r1["new_items"] and r2["new_items"], "each day brings its own discoveries")


class VerifierRound2(unittest.TestCase):
    def test_a_non_utf8_byte_does_not_end_the_run_and_is_flagged(self):
        import subprocess
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["git", "init", "-q", tmp], check=True)
            (Path(tmp) / "f.txt").write_bytes(b"ok \xff\xfe bytes\n")
            subprocess.run(["git", "-C", tmp, "add", "f.txt"], check=True)
            code, out = sd.git(["show", ":f.txt"], cwd=Path(tmp))
            self.assertEqual(0, code)
            self.assertIn("\ufffd", out)
        plan, _ = derive(plan_files(**{WO_P: work_order_text(("NEED-A", "Does a chaperone restore the protein \ufffd?", "whether it runs")).replace("\\ufffd", "\ufffd")}))
        self.assertTrue(any("undecodable" in r for r in plan["provisional"]))
        self.assertIn("work_order:NEED-A", by_id(plan))

    def test_a_surface_that_parses_to_nothing_is_flagged_even_from_cache(self):
        files = plan_files(**{DIAG_P: "# Diagnosis\n\n| Stage | a | b | c | d | Validation missing |\n|---|---|---|---|---|---|\n"})
        plan, ex = derive(files)
        self.assertTrue(any("parsed 0 items" in r and "diagnosis" in r for r in plan["provisional"]))
        again, _ = derive(files, plan, ex)
        self.assertEqual("hit", again["cache"])
        self.assertTrue(any("parsed 0 items" in r for r in again["provisional"]))

    def test_prose_and_heading_reopen_conditions_are_read_only_beside_a_watch_decision(self):
        prose = "# Pkg\n\n## Offline dump\n\nDecision: WATCH.\nReopens when the REST failures recur twice in a day. Other text.\n"
        plan, _ = derive(plan_files(**{PKG_P: prose}))
        keys = [k for k in by_id(plan) if k.startswith("reopen:")]
        self.assertEqual(1, len(keys))
        self.assertIn("Offline dump", keys[0])
        none, _ = derive(plan_files(**{PKG_P: prose.replace("WATCH", "ADOPT")}))
        self.assertFalse([k for k in by_id(none) if k.startswith("reopen:")])

    def test_internal_process_is_not_an_external_question_and_anchors_follow_the_category(self):
        files = plan_files(**{TASK_P: task_text().replace("P3 prospective evaluation", "P3 prospective evaluation"),
                              DIAG_P: diag_text() + "| Presentation | R10 | view | yes | none | the dashboard shareable edition is not online yet |\n"})
        plan, _ = derive(files)
        ids = by_id(plan)
        self.assertNotIn("diagnosis:presentation", ids)
        ev = ids["diagnosis:evaluation"]
        self.assertEqual("drug repurposing", ev["anchor"])
        self.assertNotIn("neuronal", " ".join(q["kw"] for q in plan["questions"] if q["id"].startswith(("diagnosis", "task_step"))))
        for q in plan["questions"]:
            if q["epmc"]:
                self.assertLessEqual(q["epmc"].count("TITLE_ABS"), 2, q["epmc"])
                self.assertNotIn("-", q["epmc"].replace("TITLE_ABS", ""))
            self.assertFalse([w for w in q["plain"] if "-" in w])
        agent = task_text().replace("P4", "P4")
        internal, _ = derive(plan_files(**{TASK_P: json.dumps({"TASK_ID": "T", "AUTHORISED_QUEUE_X": {"OBJ_P4": {"steps": [
            {"step": "P4 fresh actor applies canonical guidance, autonomous checkpoint resume and verification", "status": "TODO", "owner": "o"}]}}})}))
        self.assertFalse([k for k in by_id(internal) if k.startswith("task_step")])

    def test_a_lead_must_share_a_domain_term_not_a_generic_word(self):
        listing = [{"full_name": "lab/agent-evaluation-kit", "fork": False, "archived": False, "pushed_at": "2026-10-20T00:00:00Z",
                    "description": "neuronal agent evaluation", "license": None, "html_url": "u", "topics": []}]
        op = TeamExploration().opener({"lab": listing})
        res = sd.explore_team("github", "lab", ["chaperone"], set(), (), op, now=NOW)
        self.assertEqual([], res["candidates"])
        plan, _ = derive()
        generic = [q for q in plan["questions"] if q["id"] == "diagnosis:evaluation"][0]
        self.assertFalse(set(generic["domain"]) & sd.GENERIC)

    def test_source_read_and_session_check_must_name_something_checkable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.md").write_text("x")
            tr = {}
            sd.trace_event(tr, "k", "signal", "signalled", root=root)
            for kind in ("source_read", "session_check"):
                ok, why = sd.trace_event(tr, "k", "examination", "examined", kind, "I looked at it", root=root)
                self.assertFalse(ok, kind)
            self.assertTrue(sd.trace_event(tr, "k", "examination", "examined", "source_read", "https://x.org/p sec 2", root=root)[0])
            self.assertTrue(sd.trace_event(tr, "k", "examination", "examined", "session_check", "a.md checked", root=root)[0])
            self.assertEqual("claimed", tr["k"]["history"][1]["state"])

    def test_wrong_shaped_state_and_bad_dates_do_not_crash(self):
        plan, ex = derive()
        junk_plan = {"questions": "oops", "sha": 5}
        again, _ = derive(cached=junk_plan, extracts={"p": "x", RM_P: {"blob": 3, "items": "no"}})
        self.assertTrue(again["questions"])
        asked = {f"{q['id']}|{sd.digest(q['kw'])}": "not-a-date" for q in plan["questions"]}
        self.assertEqual(2, len(sd.pick_questions(plan["questions"], asked, T0, 2)))
        self.assertEqual({}, sd.record_asked(asked, None, [], "2026-11-01"))
        self.assertEqual({}, sd.record_asked("junk", None, [], "2026-11-01"))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "s.json"
            path.write_text(json.dumps({"plan": "a string", "plan_asked": ["x"], "explored": 3}))
            data = sd.load_state_file(path)
            self.assertNotIn("plan", data)
            self.assertNotIn("plan_asked", data)
        summary, sel, new, ev = sd.team_step(None, {"entries": []}, {"o": "junk"}, [], set(), sd.load_config(Path(tmp)), None, NOW)
        self.assertEqual({}, new)

    def test_the_last_current_heading_wins_and_two_are_flagged(self):
        text = readme_text("Only planned: new item.") + "\n### Roadmap iteration 17 (2026-11-01) - CURRENT\n\nSee [q](pkg_it16_p3_20261101/README.md). Next: second item.\n"
        section, note = sd.current_section(text)
        self.assertIn("second item", section)
        self.assertIn("2 headings", note)
        plan, _ = derive(plan_files(**{RD_P: text}))
        self.assertTrue(any("2 headings" in r for r in plan["provisional"]))
        self.assertTrue([q for q in plan["questions"] if q["id"].startswith("open_item")])
        self.assertEqual("", sd.current_section(readme_text())[1])


TABLE_P = sd.MODULE + "/pkg_it14_p3_20261101/reopen_searches_it14_p3.tsv"
TABLE_TEXT = ("id\titem\tverdict\tdecisive_datum\tqueries_and_sources\ttrigger_to_reopen\towner_or_route\n"
              "NP1\tGluN2B share of the isolated NMDAR current in layer II/III\tNEEDS-DATUM\tnone\tq\tan electrophysiology report with ifenprodil on the isolated current\tx\n"
              "NP2\tAnswered item about GSK3\tANSWERED\tyes\tq\ta report that is already here\tx\n"
              "NP3\tItem without a condition\tNEEDS-DATUM\tnone\tq\t\tx\n")


def derive_tables(table_text=TABLE_TEXT, extra=None):
    files = plan_files(**{TABLE_P: table_text, **(extra or {})})
    inner = plan_git(files)

    def runner(args):
        if args[:2] == ["ls-tree", "-r"]:
            return 0, "".join(f"{p}\n" for p in sorted(files))
        return inner(args)
    return sd.resolve_plan(None, None, CTX, runner, T0)


class ReopenTables(unittest.TestCase):
    """IT18 P1.1: the open conditions the module keeps as tables reach the plan; closed ones do not."""

    def test_a_table_beyond_the_read_limit_is_named_in_the_plan_not_dropped_silently(self):
        extra = {f"{sd.MODULE}/pkg_it{n}_p1_2026/reopen_searches.tsv": TABLE_TEXT for n in range(1, sd.TABLE_LIMIT + 3)}
        plan, _ = derive_tables(extra=extra)
        notes = " ".join(plan.get("provisional") or [])
        self.assertIn("older reopen/decision table(s) not read", notes)
        self.assertIn("pkg_it1_p1_2026/reopen_searches.tsv", notes)

    def test_an_open_row_becomes_a_question_and_an_answered_or_conditionless_row_does_not(self):
        plan, _ = derive_tables()
        ids = [k for k in by_id(plan) if k.startswith("reopen:pkg_it14")]
        self.assertEqual(["reopen:pkg_it14_p3_20261101/NP1"], ids)
        q = by_id(plan)[ids[0]]
        self.assertIn("reopen condition met?", q["decision"])
        self.assertIn("table row NP1", q["origin"]["locator"])

    def test_a_row_answered_in_a_later_revision_stops_generating(self):
        plan, _ = derive_tables(TABLE_TEXT.replace("NEEDS-DATUM\tnone\tq\tan electro", "ANSWERED\tnone\tq\tan electro"))
        self.assertFalse([k for k in by_id(plan) if k.startswith("reopen:pkg_it14")])

    def test_a_table_without_the_expected_columns_is_ignored_not_misread(self):
        plan, _ = derive_tables("a\tb\n1\t2\n")
        self.assertFalse([k for k in by_id(plan) if k.startswith("reopen:pkg_it14")])

    def test_decisions_table_reads_watch_rows_only(self):
        dec = sd.MODULE + "/scout_it15_p5_20261101/decisions.tsv"
        txt = ("name\turl\tverdict\treopen_condition\nChEMBL dump\tu\tWATCH\tReopen when a task needs gene per subunit\n"
               "Papyrus\tu\tDISCARD for now\tReopen if a newer release appears\n")
        plan, _ = derive_tables(extra={dec: txt})
        keys = [k for k in by_id(plan) if k.startswith("reopen:scout_it15")]
        self.assertEqual(1, len(keys))
        self.assertIn("ChEMBL dump", by_id(plan)[keys[0]]["gap"])


class QueryObjects(unittest.TestCase):
    """IT18 P1.2: a question names the objects of its priority, not the commonest words of its prose."""

    def test_objects_methods_and_local_labels(self):
        objs, methods = sd.entities("GluN2B-sensitive share in layer II/III with ifenprodil; patch-clamp of P10 and C2 (H02) in Ca2 medium, GSK3 and ATP")
        self.assertEqual(["glun2b", "gsk3", "ifenprodil"], sorted(objs))
        self.assertEqual(["patch clamp"], methods)

    def test_the_question_leads_with_the_object_and_drops_the_generic_anchor(self):
        plan, _ = derive_tables()
        q = by_id(plan)["reopen:pkg_it14_p3_20261101/NP1"]
        self.assertTrue(q["kw"].startswith("glun2b nmdar"), q["kw"])
        self.assertNotIn("epilepsy", q["kw"])
        self.assertEqual("glun2b", q["hf"])

    def test_a_text_without_objects_keeps_the_old_frequency_terms(self):
        self.assertEqual(([], []), sd.entities("independent evaluation of predictive outcomes"))
        plan, _ = derive()
        self.assertIn("diagnosis:evaluation", by_id(plan))


class NoQuestionStarves(unittest.TestCase):
    """IT19 P7: a never-asked light question is asked before a heavy one is asked again."""

    def test_unasked_light_question_beats_a_heavy_repeat(self):
        qs = [{"id": f"roadmap:R{i}", "kw": f"kw{i}", "weight": 1} for i in range(3)] + [{"id": "diagnosis:x", "kw": "heavy", "weight": 2}]
        now = sd.dt.datetime(2026, 11, 3, 5, 20, tzinfo=sd.dt.timezone.utc)
        asked = {f"diagnosis:x|{sd.digest('heavy')}": "2026-10-04"}      # asked 30 days ago: a due repeat, weight 3 x 30
        picked = [q["id"] for q in sd.pick_questions(qs, asked, now, 2)]
        self.assertEqual(picked, ["roadmap:R0", "roadmap:R1"], "weight 1 x 90 outranks weight 2 x 30 (a weight-3 repeat ties at 90 and goes by id)")

    def test_simulation_asks_every_question_within_the_cycle(self):
        qs = [{"id": f"q{i}", "kw": f"kw{i}", "weight": 1 + i % 3} for i in range(30)]
        asked, first = {}, {}
        for d in range(16):
            now = sd.dt.datetime(2026, 11, 3, 5, 20, tzinfo=sd.dt.timezone.utc) + sd.dt.timedelta(days=d)
            for q in sd.pick_questions(qs, asked, now, 2):
                asked[f"{q['id']}|{sd.digest(q['kw'])}"] = now.date().isoformat()
                first.setdefault(q["id"], d)
        self.assertEqual(len(first), 30, "30 questions at 2 a day are all asked in 15 days")


class FallbackThemeList(unittest.TestCase):
    """IT21 P6: the fixed fallback list stays well formed and keeps discovery and follow-up of known projects in balance."""

    def test_shape_and_ids(self):
        ids = [t["id"] for t in sd.THEMES]
        self.assertEqual(len(ids), len(set(ids)), "ids are unique")
        for t in sd.THEMES:
            for key in ("id", "category", "gap", "decision", "kw"):
                self.assertTrue(t.get(key), f"{t.get('id')}: {key} is required")
            self.assertIn(t["category"], sd.CATEGORY_ROADMAP, "every category maps to a roadmap item")

    def test_it21_changes(self):
        ids = {t["id"] for t in sd.THEMES}
        self.assertTrue({"gene-knockdown-neural", "genetic-suppression-rescue"} <= ids)
        self.assertNotIn("open-compound-resources", ids, "retired: IT14/IT15/IT21 found nothing beyond the existing sources")

    def test_balance(self):
        cats = {t["category"] for t in sd.THEMES}
        self.assertGreaterEqual(len(cats), 5, "no single category crowds the rotation")
        self.assertIn("negative results", cats, "counter-evidence stays in the rotation")
        self.assertIn("experiments", cats, "follow-up of a known project stays in the rotation")


if __name__ == "__main__":
    unittest.main(verbosity=2)
