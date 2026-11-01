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
        items = [{"full_name": f"o/r{n}", "stargazers_count": n, "html_url": "u", "pushed_at": "2026-01-01T00:00:00Z",
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
        self.assertTrue(sd.trace_event(tr, "k", "examination", "examined", "source_read", "paper section 2")[0])
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
        sd.trace_event(tr, "k", "examination", "examined", "source_read", "paper")
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
