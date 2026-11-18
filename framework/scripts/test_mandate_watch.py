#!/usr/bin/env python3
"""Regressions for mandate_watch.py: the hourly continuity control.
Run: python3 -B framework/scripts/test_mandate_watch.py -v"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import time
import unittest
from unittest import mock
import contextlib
import io
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mandate_watch as mw  # noqa: E402

TASK = "WATCH-TEST-1"
SID = "11111111-2222-3333-4444-555555555555"
NOW = 1_800_000_000.0


def record(state="OPEN", steps=("TODO",)):
    return {"TASK_ID": TASK, "ACTOR_ID": "orchestrator", "AUTHORISED_QUEUE_X": {
        "MANDATE_STATE": state,
        "OBJ_A": {"order": 1, "steps": [{"step": f"s{i}", "status": s, "owner": "o", **({"evidence": "e1"} if s == "DONE" else {})}
                                         for i, s in enumerate(steps)]}}}


class Env:
    def __init__(self, rec, bound=True, age_minutes=120):
        self.tmp = tempfile.TemporaryDirectory()
        t = Path(self.tmp.name)
        self.root = t / "repo"
        (self.root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
        (self.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        self.proj = t / "projects"
        (self.proj / "p").mkdir(parents=True)
        self.tasks = t / "tasks"
        self.tasks.mkdir()
        self.tr = self.proj / "p" / f"{SID}.jsonl"
        text = f"MANDATE_BOUND: {TASK}" if bound else "hello"
        self.tr.write_text(json.dumps({"type": "assistant", "cwd": "/work/dir", "message": {"content": [{"type": "text", "text": text}]}}) + "\n"
                           + json.dumps({"type": "user", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(NOW)), "message": {"content": "hourly watch prompt"}}) + "\n")
        old = NOW - age_minutes * 60
        os.utime(self.tr, (old, old))
        os.environ["LEGEND_MANDATE_WATCH_STATE"] = str(t / "state")

    def check(self, sessions, **kw):
        return mw.check(TASK, root=self.root, projects_dir=self.proj, tasks_root=self.tasks, sessions=sessions, now=NOW, **kw)

    def close(self):
        self.tmp.cleanup()
        os.environ.pop("LEGEND_MANDATE_WATCH_STATE", None)


class Watch(unittest.TestCase):
    def tearDown(self):
        getattr(self, "e", None) and self.e.close()

    def env(self, *a, **k):
        self.e = Env(*a, **k)
        return self.e

    def test_claude_is_found_without_a_path_in_cron(self):
        old = os.environ.get("PATH")
        os.environ["PATH"] = "/usr/bin:/bin"          # what cron provides
        try:
            self.assertTrue(mw.claude_bin().endswith("claude"))
            self.assertTrue(os.path.isabs(mw.claude_bin()))
        finally:
            os.environ["PATH"] = old

    def test_busy_session_is_running_and_never_asked(self):
        e = self.env(record())
        r = e.check([{"sessionId": SID, "status": "busy"}], deliver="resume")
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"))

    def test_all_discovers_mandates_for_every_actor(self):
        e = self.env(record())
        for actor in ("plan", "scientist-a"):
            p = e.root / "ledger" / "tasks" / actor / f"{actor}-work.json"
            p.parent.mkdir(parents=True)
            rec = record()
            rec.update(TASK_ID=f"{actor}-work", ACTOR_ID=actor)
            p.write_text(json.dumps(rec))
        self.assertEqual(set(mw.open_tasks(e.root)), {TASK, "plan-work", "scientist-a-work"})

    def test_all_observes_failed_runtime_once_and_reports_json_without_revival(self):
        e = self.env(record())
        args = SimpleNamespace(root=str(e.root), deliver="resume", quiet_minutes=25, resume_arg=[], json=True)
        output = io.StringIO()
        with mock.patch.object(mw, "open_tasks", return_value=[TASK, "OTHER"]), \
                mock.patch.object(mw, "registered_worktrees", return_value=[e.root]), \
                mock.patch.object(mw, "list_sessions", return_value=None) as listing, \
                mock.patch.object(mw, "find_bound_transcript", return_value=None), \
                mock.patch.object(mw.subprocess, "run") as process, contextlib.redirect_stdout(output):
            self.assertEqual(mw._check_all(args), 0)
        self.assertEqual(listing.call_count, 1)
        process.assert_not_called()
        rows = json.loads(output.getvalue())
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(r["state"] == "UNKNOWN" for r in rows))

    def test_new_unmerged_task_is_checked_in_its_registered_worktree(self):
        e = self.env(record())
        tree = Path(e.tmp.name) / "science-worktree"
        p = tree / "ledger/tasks/scientist-a/SCI-NEW.json"
        p.parent.mkdir(parents=True)
        rec = record()
        rec.update(TASK_ID="SCI-NEW", ACTOR_ID="scientist-a")
        p.write_text(json.dumps(rec))
        args = SimpleNamespace(root=str(e.root), deliver="none", quiet_minutes=25, resume_arg=[], json=True)
        with mock.patch.object(mw, "registered_worktrees", return_value=[e.root, tree]), \
                mock.patch.object(mw, "list_sessions", return_value=[]), \
                mock.patch.object(mw, "check", return_value={"state": "UNKNOWN", "action": "NONE"}) as checked, \
                contextlib.redirect_stdout(io.StringIO()):
            mw._check_all(args)
        roots = {c.args[0]: c.kwargs["root"] for c in checked.call_args_list}
        self.assertEqual(roots["SCI-NEW"], tree)
        self.assertEqual(roots[TASK], e.root)

    def test_stale_open_worktree_does_not_reopen_a_paused_main_record(self):
        e = self.env(record("PAUSED"))
        tree = Path(e.tmp.name) / "old-worktree"
        p = tree / "ledger/tasks/orchestrator" / f"{TASK}.json"
        p.parent.mkdir(parents=True)
        p.write_text(json.dumps(record()))
        args = SimpleNamespace(root=str(e.root), deliver="resume", quiet_minutes=25, resume_arg=[], json=True)
        output = io.StringIO()
        with mock.patch.object(mw, "registered_worktrees", return_value=[e.root, tree]), \
                mock.patch.object(mw, "list_sessions", return_value=[]), \
                mock.patch.object(mw, "find_bound_transcript", return_value=None), \
                contextlib.redirect_stdout(output):
            mw._check_all(args)
        rows = json.loads(output.getvalue())
        self.assertEqual((rows[0]["state"], rows[0]["action"]), ("PAUSED", "NONE"))
        self.assertEqual(rows[0]["record_root"], str(e.root))

    def test_ambiguous_unmerged_records_never_start_a_session(self):
        e = self.env(record())
        (e.root / "ledger/tasks/orchestrator" / f"{TASK}.json").unlink()
        trees = []
        for name in ("copy-a", "copy-b"):
            tree = Path(e.tmp.name) / name
            p = tree / "ledger/tasks/plan" / f"{TASK}.json"
            p.parent.mkdir(parents=True)
            p.write_text(json.dumps(record()))
            trees.append(tree)
        args = SimpleNamespace(root=str(e.root), deliver="resume", quiet_minutes=25, resume_arg=[], json=True)
        output = io.StringIO()
        with mock.patch.object(mw, "registered_worktrees", return_value=[e.root, *trees]), \
                mock.patch.object(mw, "list_sessions", return_value=[]), \
                mock.patch.object(mw, "check") as checked, contextlib.redirect_stdout(output):
            mw._check_all(args)
        checked.assert_not_called()
        row = json.loads(output.getvalue())[0]
        self.assertEqual((row["state"], row["action"]), ("UNKNOWN", "NONE"))
        self.assertIn("multiple unmerged", row["why"])

    def test_waiting_for_science_does_not_block_an_independent_step(self):
        rec = record(steps=("BLOCKED", "TODO"))
        rec["AUTHORISED_QUEUE_X"]["OBJ_A"]["steps"][0]["blocker"] = "waiting for the science batch"
        e = self.env(rec)
        r = e.check([])
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"))
        self.assertIn("s1", r["why"])

    def test_bound_session_reconciles_missing_evidence_instead_of_unknown(self):
        for state in ("OPEN", "COMPLETE"):
            rec = record(state, ("DONE",))
            rec["AUTHORISED_QUEUE_X"]["OBJ_A"]["steps"][0].pop("evidence")
            e = self.env(rec)
            r = e.check([])
            self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"))
            self.assertIn(r["record_verdict"], ("EVIDENCE_PENDING", "INCONSISTENT_COMPLETE"))
            e.close()

    def test_a_running_mandate_still_leaves_a_trace_in_the_event_log(self):
        e = self.env(record())
        r = e.check([{"sessionId": SID, "status": "busy"}], deliver="resume")
        self.assertEqual(r["state"], "RUNNING")
        lines = [json.loads(l) for l in (Path(os.environ["LEGEND_MANDATE_WATCH_STATE"]) / mw.EVENTS_FILE).read_text().splitlines() if l.strip()]
        self.assertTrue(any(x.get("task") == TASK and x.get("state") == "RUNNING" for x in lines))

    def test_recent_background_task_output_is_running_even_when_idle(self):
        e = self.env(record())
        d = e.tasks / "proj" / SID / "tasks"
        d.mkdir(parents=True)
        f = d / "a.output"
        f.write_text("x")
        os.utime(f, (NOW - 60, NOW - 60))
        r = e.check([{"sessionId": SID, "status": "idle"}])
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"))

    def test_idle_and_silent_session_with_open_work_is_resumable(self):
        e = self.env(record())
        r = e.check([{"sessionId": SID, "status": "idle"}])
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"))

    def test_live_session_is_not_resumed_from_outside(self):
        e = self.env(record())
        calls = []
        r = e.check([{"sessionId": SID, "status": "idle"}], deliver="resume", runner=lambda c, cwd=None: calls.append(c))
        self.assertEqual(calls, [])
        self.assertIn("alive", r["delivery"])

    def test_dead_session_is_revived_under_its_own_id_and_only_once(self):
        e = self.env(record())
        calls = []
        run = lambda c, cwd=None: (calls.append(c), SimpleNamespace(returncode=0, stdout="ok", stderr=""))[1]
        r = e.check([], deliver="resume", runner=run)
        self.assertEqual(r["delivery"], "sent")
        self.assertEqual([os.path.basename(calls[0][0])] + calls[0][1:4], ["claude", "--bg", "--resume", SID])
        self.assertEqual(mw.transcript_cwd(e.tr), "/work/dir")
        r2 = e.check([], deliver="resume", runner=run)            # same queue state: request still pending
        self.assertEqual(r2["action"], "NONE")
        self.assertEqual(len(calls), 1)

    def test_a_failed_revival_logs_why_it_failed(self):
        """IT19 P1: `claude --bg --resume` exits 1 with 'Workspace not trusted' until the operator accepts trust; the event must say so."""
        e = self.env(record())
        run = lambda c, cwd=None: SimpleNamespace(returncode=1, stdout="", stderr="Workspace not trusted. Run `claude` in /work/dir once and accept the trust prompt")
        r = e.check([], deliver="resume", runner=run)
        self.assertTrue(r["delivery"].startswith("failed rc=1"))
        events = [json.loads(l) for l in (mw.state_dir() / mw.EVENTS_FILE).read_text().splitlines()]
        self.assertIn("Workspace not trusted", events[-1].get("delivery_output", ""))

    def test_progress_in_the_record_allows_a_new_request(self):
        e = self.env(record(steps=("TODO", "TODO")))
        run = lambda c, cwd=None: SimpleNamespace(returncode=0, stdout="", stderr="")
        e.check([], deliver="resume", runner=run)
        rec = record(steps=("DONE", "TODO"))
        (e.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        self.assertEqual(e.check([], deliver="resume", runner=run)["action"], "RESUME")

    def test_complete_paused_and_blocked_are_never_restarted(self):
        for rec, want in ((record("COMPLETE", ("DONE",)), "COMPLETE"), (record("PAUSED"), "PAUSED"),
                          (record("OPEN", ("DONE",)), "COMPLETE")):
            e = self.env(rec)
            r = e.check([])
            self.assertEqual((r["state"], r["action"]), (want, "NONE"), rec)
            e.close()
        blocked = record("OPEN", ("BLOCKED",))
        blocked["AUTHORISED_QUEUE_X"]["OBJ_A"]["steps"][0]["blocker"] = "waiting for an external dataset"
        e = self.env(blocked)
        r = e.check([])
        self.assertEqual((r["state"], r["action"]), ("BLOCKED", "NONE"))

    def test_unknown_when_nothing_binds_the_task_or_the_listing_fails(self):
        e = self.env(record(), bound=False)
        self.assertEqual(e.check([])["state"], "UNKNOWN")
        e.close()
        e = self.env(record())
        r = e.check(None) if False else mw.classify({"verdict": "CONTINUE", "message": ""}, None, False, True, 9999, {}, "s", NOW)
        self.assertEqual((r["state"], r["action"]), ("UNKNOWN", "NONE"))

    def test_a_marker_inside_a_sentence_is_refused_and_the_diagnosis_names_the_session(self):
        # 2026-11-11, IT46: `MANDATE_BOUND: <id>. Identity: ... ` as the start of a sentence left the mandate UNKNOWN with no hint why
        e = self.env(record(), bound=False)
        e.tr.write_text(json.dumps({"type": "assistant", "timestamp": "2026-11-11T21:48:36.000Z", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}. Identity: orchestrator. The residue is clean."}]}}) + "\n")
        r = e.check([])
        self.assertEqual((r["state"], r["session"]), ("UNKNOWN", None))
        self.assertEqual(r["near_marker"]["session"], SID)
        self.assertIn(f"session {SID} wrote", r["why"])
        self.assertIn("must write that plain line again", r["why"])
        e.tr.write_text(e.tr.read_text() + json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}"}]}}) + "\n")
        bound = e.check([{"sessionId": SID, "status": "idle"}])
        self.assertEqual(bound["session"], SID)                   # the plain line binds, and the near-miss is no longer reported
        self.assertNotIn("near_marker", bound)

    def test_a_fenced_or_unrelated_mention_is_not_a_near_marker(self):
        e = self.env(record(), bound=False)
        e.tr.write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"```\nMANDATE_BOUND: {TASK} extra\n```\nand MANDATE_BOUND: OTHER-TASK. Hello"}]}}) + "\n")
        self.assertNotIn("near_marker", e.check([]))

    def test_self_call_ignores_its_own_work_but_not_subagents_running_before_the_turn(self):
        e = self.env(record(), age_minutes=0)
        d = e.tasks / "proj" / SID / "tasks"
        d.mkdir(parents=True)
        own = d / "own_foreground_command.output"
        own.write_text("x")
        os.utime(own, (NOW + 5, NOW + 5))              # written after the cron turn began: the caller's own command
        r = e.check([{"sessionId": SID, "status": "busy"}], self_call=True)
        self.assertEqual(r["action"], "RESUME")
        agent = d / "agent.output"
        agent.write_text("x")
        os.utime(agent, (NOW - 30, NOW - 30))           # an agent was writing just before the turn began
        self.assertEqual(e.check([{"sessionId": SID, "status": "busy"}], self_call=True)["state"], "RUNNING")
        os.utime(agent, (NOW - 3600, NOW - 3600))       # an hour earlier: finished long ago
        self.assertEqual(e.check([{"sessionId": SID, "status": "busy"}], self_call=True)["state"], "STOPPED_RESUMABLE")   # (the request is already pending: dedupe)


class Jobs(unittest.TestCase):
    """Background jobs are judged by their own process identity, not by output recency."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["LEGEND_MANDATE_WATCH_STATE"] = self.tmp.name
        self.cont = {"verdict": "CONTINUE", "message": "work remains"}

    def tearDown(self):
        for j in mw.load_jobs(TASK):
            if j["state"] == "ALIVE":
                try:
                    os.kill(j["pid"], 9)
                except OSError:
                    pass
        os.environ.pop("LEGEND_MANDATE_WATCH_STATE", None)
        self.tmp.cleanup()

    def wait_state(self, want, secs=8):
        end = time.time() + secs
        while time.time() < end:
            js = mw.load_jobs(TASK)
            if js and js[-1]["state"] == want:
                return js[-1]
            time.sleep(0.1)
        self.fail(f"job never reached {want}: {mw.load_jobs(TASK)}")

    def classify(self, **kw):
        return mw.classify(self.cont, None, True, True, 99999, {}, "sig", NOW, jobs=mw.summarise_jobs(mw.load_jobs(TASK)), **kw)

    def test_silent_long_job_is_running_even_when_the_session_is_idle_and_silent(self):
        mw.job_run(TASK, "battery", ["sleep", "30"])
        r = self.classify()
        self.assertEqual((r["state"], r["action"]), ("RUNNING", "NONE"))
        self.assertIn("alive", r["why"])

    def test_same_label_is_not_started_twice(self):
        a = mw.job_run(TASK, "battery", ["sleep", "30"])
        b = mw.job_run(TASK, "battery", ["sleep", "30"])
        self.assertTrue(a["started"])
        self.assertFalse(b["started"])
        self.assertEqual(a["pid"], b["pid"])

    def test_finished_job_is_collected_once(self):
        mw.job_run(TASK, "quick", ["true"])
        j = self.wait_state("DONE")
        r = self.classify()
        self.assertEqual(r["action"], "RESUME")
        self.assertIn("finished job", r["why"])
        self.assertTrue(mw.job_collect(TASK, j["id"]))
        self.assertNotIn("finished job", self.classify()["why"])

    def test_job_killed_without_an_exit_status_is_dead_not_finished(self):
        j = mw.job_run(TASK, "doomed", ["sleep", "30"])
        os.kill(j["pid"], 9)
        self.wait_state("DEAD")
        r = self.classify()
        self.assertEqual(r["action"], "RESUME")
        self.assertIn("DIED", r["why"])

    def test_reused_pid_with_another_start_time_is_not_alive(self):
        j = mw.job_run(TASK, "reuse", ["sleep", "30"])
        job = mw.load_jobs(TASK)[-1]
        job["start_ticks"] += 1                       # the recorded start time no longer matches the process
        self.assertEqual(mw.job_state(job), "DEAD")

    def test_complete_record_without_the_push_is_not_complete(self):
        done = {"verdict": "RELEASED", "message": "MANDATE_STATE COMPLETE"}
        r = mw.classify(done, None, True, True, 99999, {}, "sig", NOW, push_missing="the closing commit is not on development/main")
        self.assertEqual((r["state"], r["action"]), ("STOPPED_RESUMABLE", "RESUME"))
        self.assertIn("COMPLETE but", r["why"])
        ok = mw.classify(done, None, True, True, 99999, {}, "sig", NOW)
        self.assertEqual((ok["state"], ok["action"]), ("COMPLETE", "NONE"))
        paused = mw.classify({"verdict": "RELEASED", "message": "MANDATE_STATE PAUSED"}, None, True, True, 99999, {}, "sig", NOW, push_missing="x")
        self.assertEqual((paused["state"], paused["action"]), ("PAUSED", "NONE"))


class BusyIsNotProgress(unittest.TestCase):
    """IT39: a session reported busy while its record still lists authorised work must say so (a session that stopped to wait on a monitor read 'session busy' as progress)."""

    def test_the_busy_answer_names_the_work_the_record_still_lists_and_the_self_call_flag(self):
        st = {"verdict": "CONTINUE", "message": "MANDATE T CONTINUE \u2014 3 executable step(s) remain; next: A"}
        out = mw.classify(st, {"status": "busy"}, True, True, 0, {}, "sig", 0, 10, jobs=None, push_missing=None)
        self.assertEqual((out["state"], out["action"]), ("RUNNING", "NONE"))
        self.assertIn("3 executable step(s)", out["why"])
        self.assertIn("--self-call", out["why"])

    def test_without_remaining_work_the_busy_answer_is_unchanged(self):
        st = {"verdict": "CONTINUE", "message": "MANDATE T CONTINUE"}
        out = mw.classify(st, {"status": "busy"}, True, True, 0, {}, "sig", 0, 10, jobs=None, push_missing=None)
        self.assertEqual(out["why"], "session busy")



class Routing(unittest.TestCase):
    """HE53: a message's recipients are the sends actually made, resolved to live sessions; a name in the text is only a claim (IT answered 'IT to ADV and HE' and the transport receipt named HE alone)."""
    ADV_ID = "e6526331-6b7c-4631-8c9b-9e9d79867e90"
    OTHER_ID = "99999999-aaaa-bbbb-cccc-dddddddddddd"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
        rec = {"TASK_ID": "ORCH-ADV-X", "SESSION_NAME": "ADV \u2014 Strategic Advisor", "SESSION_BINDING": {"session_id": self.ADV_ID, "pid_at_start": 1}}
        (self.root / "ledger" / "tasks" / "orchestrator" / "ORCH-ADV-X.json").write_text(json.dumps(rec), encoding="utf-8")
        self.live = [{"name": "HE", "sessionId": "11111111-0000-0000-0000-000000000001"}, {"name": "IT Orchestrator", "sessionId": "11111111-0000-0000-0000-000000000002"},
                     {"name": "legend-development-39", "sessionId": self.ADV_ID}]

    def test_a_role_resolves_to_the_session_the_record_binds_and_not_to_another_name(self):
        r = mw.route("ADV", self.live, self.root)
        self.assertEqual((r["status"], r["recipient"], r["session_id"]), ("RESOLVED", "legend-development-39", self.ADV_ID))
        self.assertEqual(mw.route("IT", self.live, self.root)["recipient"], "IT Orchestrator")             # a whole-word alias of a live name
        self.assertEqual(mw.route("legend-development-39", self.live, self.root)["session_id"], self.ADV_ID)

    def test_two_recipients_declared_and_one_send_is_a_mismatch_naming_the_missing_one(self):
        res = mw.check_recipients("IT to ADV and HE: baseline", ["HE"], self.live, self.root)       # the 14 Nov case: the receipt named HE only
        self.assertEqual((res["verdict"], res["missing_send_to"]), ("MISMATCH", ["ADV"]))
        self.assertEqual(mw.check_recipients("IT to ADV and HE: baseline", ["HE", "legend-development-39"], self.live, self.root)["verdict"], "OK")

    def test_an_address_no_longer_associated_with_the_awaited_session_is_not_reused(self):
        live = [dict(x) for x in self.live]
        live[2] = {"name": "legend-development-39", "sessionId": self.OTHER_ID}                       # the name now belongs to another session
        r = mw.route("ADV", live, self.root)
        self.assertEqual((r["status"], r["recipient"]), ("UNRESOLVED", None))
        self.assertEqual(r["bound_not_live"], [{"task": "ORCH-ADV-X", "session_id": self.ADV_ID}])    # said, not guessed
        res = mw.check_recipients("HE to ADV: ping", ["legend-development-39"], live, self.root)
        self.assertEqual(res["verdict"], "MISMATCH")

    def test_two_live_sessions_answering_to_one_role_are_ambiguous_and_none_is_chosen(self):
        live = self.live + [{"name": "IT scratch", "sessionId": "11111111-0000-0000-0000-000000000003"}]
        r = mw.route("IT", live, self.root)
        self.assertEqual((r["status"], r["recipient"]), ("AMBIGUOUS", None))
        self.assertEqual(len(r["candidates"]), 2)

    def test_an_unreadable_listing_is_not_a_guess_and_the_first_line_forms_are_read(self):
        self.assertEqual(mw.route("ADV", None, self.root)["status"], "UNRESOLVED")
        self.assertEqual(mw.declared_recipients("HE to ADV (cc IT): delivery"), ["ADV", "IT"])
        self.assertEqual(mw.declared_recipients("ORCH to HE (cc ADV): BASELINE ACQUIRED."), ["HE", "ADV"])
        self.assertEqual(mw.declared_recipients("no addressing line here"), [])
        self.assertEqual(mw.check_recipients("no addressing line here", ["HE"], self.live, self.root)["verdict"], "NO_DECLARED_RECIPIENT")


SID2 = "99999999-aaaa-bbbb-cccc-dddddddddddd"


def listed(sid, name, pid=None, status="idle", kind="background"):
    return {"sessionId": sid, "name": name, "pid": os.getpid() if pid is None else pid, "status": status, "kind": kind}


class Continuity20261118(unittest.TestCase):
    """The defects of 2026-11-18 (OOM of the desktop service): a dead session still LISTED, two hosts, an alias that follows a display name, a revival that renames the session, a substitute that nobody
    authorised, and work accepted by message that no record listed. Fixtures: they do not show the real runtime; the scratch-session demonstration (governance/design_records/wakeup_continuity_20261118.md) does."""

    def tearDown(self):
        getattr(self, "e", None) and self.e.close()

    def env(self, *a, **k):
        self.e = Env(*a, **k)
        return self.e

    def test_a_listed_session_without_a_running_process_is_not_live(self):
        """Measured with a scratch session: after `claude stop` and after a kill, `claude agents --json` still listed it, with no pid and no status."""
        self.assertTrue(mw.session_is_live({"pid": os.getpid()}))
        self.assertFalse(mw.session_is_live({"pid": None, "state": "working"}))
        self.assertFalse(mw.session_is_live({"name": "x"}))
        self.assertFalse(mw.session_is_live({"pid": 2 ** 22 + 12345}))                 # no such process
        raw = json.dumps([{"sessionId": SID, "name": "DEAD", "state": "working"}, {"sessionId": SID2, "name": "ALIVE", "pid": os.getpid(), "status": "idle"}])
        with mock.patch.object(mw.subprocess, "run", return_value=SimpleNamespace(stdout=raw, returncode=0)):
            self.assertEqual([x["name"] for x in mw.list_sessions()], ["ALIVE"])

    def test_a_dead_but_listed_bound_session_is_revived_not_called_alive(self):
        e = self.env(record())
        before = e.check([{"sessionId": SID, "name": "H", "state": "working"}], deliver="none")      # the old reading of the listing: this entry would count as a session
        self.assertEqual(before["state"], "STOPPED_RESUMABLE")                      # the check itself reads only what it is given: the filter is in list_sessions
        with mock.patch.object(mw, "list_sessions", return_value=[]):
            out = e.check(mw._SESSIONS_UNSET, deliver="resume", runner=lambda cmd, cwd=None: SimpleNamespace(returncode=0, stdout="ok", stderr=""))
        self.assertEqual((out["action"], out["delivery"]), ("RESUME", "sent"))

    def test_two_live_sessions_that_carry_the_marker_are_a_duplicate_host_and_nothing_is_resumed(self):
        e = self.env(record())
        (e.proj / "p" / f"{SID2}.jsonl").write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}"}]}}) + "\n")
        out = e.check([listed(SID, "ADV"), listed(SID2, "ADV chat")], deliver="resume")
        self.assertEqual((out["state"], out["action"]), ("DUPLICATE_HOST", "NONE"))
        self.assertEqual(len(out["live_bound_sessions"]), 2)
        self.assertIn("MANDATE_RELEASED", out["why"])

    def test_two_sessions_that_only_share_a_name_are_not_a_duplicate_host(self):
        """The legitimate case seen on 2026-11-18: the bound session and an operator chat that investigated both answered to 'ADV'. Only the marker makes a host."""
        e = self.env(record(), age_minutes=1)
        (e.proj / "p" / f"{SID2}.jsonl").write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": "an investigation, unbound"}]}}) + "\n")
        out = e.check([listed(SID, "ADV", status="busy"), listed(SID2, "ADV")], deliver="resume")
        self.assertEqual((out["state"], out["action"]), ("RUNNING", "NONE"))
        self.assertNotIn("live_bound_sessions", out)

    def test_the_record_binding_chooses_the_host_among_live_bound_sessions_and_the_rest_are_named(self):
        e = self.env(record())
        rec = record(); rec["SESSION_BINDING"] = {"session_id": SID2}
        (e.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        (e.proj / "p" / f"{SID2}.jsonl").write_text(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": f"MANDATE_BOUND: {TASK}"}]}}) + "\n")
        out = e.check([listed(SID, "one"), listed(SID2, "two")], deliver="none")
        self.assertEqual(out["state"], "DUPLICATE_HOST")
        self.assertEqual(out["session"], SID2)                                       # the record's binding is the one the answer names as the host

    def test_route_prefers_a_whole_name_and_the_record_binding_over_token_matches(self):
        root = Path(tempfile.mkdtemp())
        rec = record(); rec.update(TASK_ID="ADV-TASK", SESSION_NAME="ADV — Strategic Advisor", SESSION_BINDING={"session_id": SID})
        (root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
        (root / "ledger" / "tasks" / "orchestrator" / "ADV-TASK.json").write_text(json.dumps(rec))
        live = [listed(SID, "ADV"), listed(SID2, "ORCH-ADV-FOLLOWTHROUGH-20261114"), listed("33333333-4444-5555-6666-777777777777", "HE-PROBE")]
        res = mw.route("ADV", live, root)
        self.assertEqual((res["status"], res["session_id"]), ("RESOLVED", SID))
        self.assertEqual([c["session_id"] for c in res["surplus_name_matches"]], [SID2])
        self.assertEqual(mw.route("HE", live, root)["session_id"], "33333333-4444-5555-6666-777777777777")      # the only 'HE' token match here, listed as such
        live2 = [listed(SID, "something else"), listed(SID2, "ADV")]                # the bound session was renamed, another session took the name
        res2 = mw.route("ADV", live2, root)
        self.assertEqual((res2["status"], res2["session_id"]), ("RESOLVED", SID))   # identity follows the binding, not the name
        self.assertTrue(res2["surplus_name_matches"])

    def test_a_role_alias_follows_the_marker_of_its_record_after_a_rename(self):
        e = self.env(record())
        rec = record(); rec["SESSION_NAME"] = "SCI — Scientist"
        (e.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        with mock.patch.object(mw, "transcript_for_session", lambda sid, pd=None: e.tr if sid == SID else None):
            res = mw.route("SCI", [listed(SID, "orch-adv004-mandate-reconciliation")], e.root)
        self.assertEqual((res["status"], res["session_id"]), ("RESOLVED", SID))

    def test_a_revival_never_passes_a_flag_to_a_session_that_has_saved_options(self):
        """Measured: a flag on a background session with saved options starts a COPY under a new id; without flags the same command continues the session itself."""
        e = self.env(record())
        e.tr.write_text(e.tr.read_text() + json.dumps({"type": "custom-title", "customTitle": "SCI"}) + "\n")
        jobs = Path(e.tmp.name) / "jobs"
        (jobs / SID[:8]).mkdir(parents=True)
        (jobs / SID[:8] / "state.json").write_text("{}")
        os.environ["LEGEND_CLAUDE_JOBS"] = str(jobs)
        self.addCleanup(os.environ.pop, "LEGEND_CLAUDE_JOBS", None)
        seen = {}
        out = e.check([], deliver="resume", runner=lambda cmd, cwd=None: (seen.update(cmd=cmd), SimpleNamespace(returncode=0, stdout="ok", stderr=""))[1])
        self.assertEqual(out["delivery"], "sent")
        self.assertNotIn("--name", seen["cmd"])
        self.assertEqual(seen["cmd"][1:4], ["--bg", "--resume", SID])

    def test_the_revival_passes_the_chosen_name_and_the_recall_clause_and_never_a_second_recall(self):
        e = self.env(record())
        os.environ["LEGEND_CLAUDE_JOBS"] = str(Path(e.tmp.name) / "no_jobs")                  # an interactive session: no saved options, the chosen name is passed
        self.addCleanup(os.environ.pop, "LEGEND_CLAUDE_JOBS", None)
        e.tr.write_text(e.tr.read_text() + json.dumps({"type": "custom-title", "customTitle": "SCI"}) + "\n")
        rec = record(); rec["RECALL"] = {"mark": "Proactive Strategic Advisor pilot, hourly mechanical check", "command": "strategic_advisor.py recall --campaign X", "renew_days": 6}
        (e.root / "ledger" / "tasks" / "orchestrator" / f"{TASK}.json").write_text(json.dumps(rec))
        seen = {}
        def runner(cmd, cwd=None):
            seen["cmd"] = cmd
            return SimpleNamespace(returncode=0, stdout="ok", stderr="")
        out = e.check([], deliver="resume", runner=runner)
        self.assertEqual(out["delivery"], "sent")
        cmd = seen["cmd"]
        self.assertEqual(cmd[cmd.index("--name") + 1], "SCI")                          # a revived session keeps the name the operator gave it
        text = cmd[-1]
        self.assertIn("call CronList", text)
        self.assertIn("do NOT create another", text)
        self.assertIn("before day 6", text)
        self.assertEqual(mw.recall_clause(None), "")                                  # a mandate without a recall field gets no recall sentence

    def test_a_session_that_died_again_after_its_revival_is_revived_again_but_not_while_it_may_still_be_starting(self):
        e = self.env(record())
        calls = []
        run = lambda c, cwd=None: (calls.append(c), SimpleNamespace(returncode=0, stdout="ok", stderr=""))[1]
        e.check([], deliver="resume", runner=run)
        mw.check(TASK, root=e.root, projects_dir=e.proj, tasks_root=e.tasks, sessions=[], now=NOW + 5 * 60, deliver="resume", runner=run)     # five minutes later: the revival may still be starting
        self.assertEqual(len(calls), 1)
        later = mw.check(TASK, root=e.root, projects_dir=e.proj, tasks_root=e.tasks, sessions=[], now=NOW + 40 * 60, deliver="resume", runner=run)
        self.assertEqual((later["action"], later["delivery"]), ("RESUME", "sent"))          # forty minutes later and still not live: it died again, ask again
        self.assertEqual(len(calls), 2)
        live = mw.check(TASK, root=e.root, projects_dir=e.proj, tasks_root=e.tasks, sessions=[listed(SID, "H")], now=NOW + 80 * 60, deliver="resume", runner=run)
        self.assertEqual(len(calls), 2)                                                      # a live session that was asked is left alone for the long window

    def test_rebind_needs_an_explicit_authorisation_a_single_live_target_and_no_second_host(self):
        e = self.env(record())
        live = [listed(SID, "ADV", status="idle"), listed(SID2, "substitute")]
        with self.assertRaises(PermissionError):
            mw.rebind(TASK, SID2, "", root=e.root, sessions=live, projects_dir=e.proj)                          # no pointer: nothing happens
        with self.assertRaises(PermissionError) as c:
            mw.rebind(TASK, SID2, "operator message 2026-11-18 20:10Z", root=e.root, sessions=live, projects_dir=e.proj)   # SID still carries the marker and is live
        self.assertIn("exactly one host", str(c.exception))
        with self.assertRaises(ValueError):
            mw.rebind(TASK, "nobody", "operator message 2026-11-18 20:10Z", root=e.root, sessions=live, projects_dir=e.proj)
        out = mw.rebind(TASK, SID2, "operator message 2026-11-18 20:10Z", root=e.root, sessions=[listed(SID2, "substitute")], projects_dir=e.proj)   # the old host is gone
        self.assertEqual(out["session_id"], SID2)
        saved = json.loads((e.root / out["record"]).read_text())
        self.assertEqual(saved["SESSION_BINDING"]["session_id"], SID2)
        self.assertEqual(saved["SESSION_BINDING"]["authorised_by"], "operator message 2026-11-18 20:10Z")
        self.assertFalse(out["marker_present"])                                       # the substitute has not yet written its own marker line
        ev = mw.state_dir() / mw.EVENTS_FILE
        self.assertIn('"kind": "rebind"', ev.read_text())

    def test_rebind_never_reopens_an_operator_stop(self):
        e = self.env(record(state="PAUSED"))
        with self.assertRaises(PermissionError):
            mw.rebind(TASK, SID2, "operator message 2026-11-18 20:10Z", root=e.root, sessions=[listed(SID2, "substitute")], projects_dir=e.proj)


class MemoryContainment(unittest.TestCase):
    """The opt-in memory scope of `job run` and the read-only `resources` view. The real-kernel
    proof (a capped job OOM-killed alone while the desktop service stays untouched) is recorded in
    governance/design_records/wakeup_continuity_20261118.md; these are fixtures."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["LEGEND_MANDATE_WATCH_STATE"] = str(Path(self.tmp.name) / "state")
        self.bin = Path(self.tmp.name) / "bin"
        self.bin.mkdir()
        fake = self.bin / "systemd-run"                       # records its arguments, then runs the command after `--`
        fake.write_text('#!/bin/sh\necho "$@" > "%s/args"\nwhile [ "$1" != "--" ]; do shift; done\nshift\nexec "$@"\n' % self.tmp.name)
        fake.chmod(0o755)

    def tearDown(self):
        os.environ.pop("LEGEND_MANDATE_WATCH_STATE", None)
        self.tmp.cleanup()

    def test_value_is_validated_and_a_missing_systemd_run_never_means_uncapped(self):
        for bad in ("3GB", "0", "", "-1G", "3 G", "G"):
            with self.assertRaises(ValueError, msg=bad):
                mw.memory_scope(["true"], bad)
        with mock.patch.object(mw.shutil, "which", return_value=None):
            with self.assertRaises(RuntimeError):
                mw.memory_scope(["true"], "3G")
            with self.assertRaises(RuntimeError):
                mw.job_run("T", "l", ["true"], memory_max="3G")
        self.assertFalse((mw.jobs_dir("T")).exists())            # nothing was started

    def test_wrapped_command_carries_the_cap_and_the_user_scope(self):
        with mock.patch.object(mw.shutil, "which", return_value="/usr/bin/systemd-run"):
            cmd = mw.memory_scope(["python3", "x.py"], "2.5G")
        self.assertEqual(cmd[1:6], ["--user", "--scope", "--quiet", "-p", "MemoryMax=2.5G"])
        self.assertEqual(cmd[-3:], ["--", "python3", "x.py"])

    def test_job_run_with_cap_runs_the_command_inside_the_wrapper_and_records_the_cap(self):
        with mock.patch.object(mw.shutil, "which", return_value=str(self.bin / "systemd-run")):
            j = mw.job_run("T", "capped", ["sh", "-c", "echo hello"], memory_max="1G")
        self.assertTrue(j["started"])
        self.assertEqual(j["memory_max"], "1G")
        self.assertEqual(j["cmd"], ["sh", "-c", "echo hello"])      # the caller's command is what is recorded
        for _ in range(100):
            if Path(j["exit_file"]).exists():
                break
            time.sleep(0.05)
        self.assertEqual(Path(j["exit_file"]).read_text().strip(), "0")
        self.assertIn("hello", Path(j["log"]).read_text())
        self.assertIn("MemoryMax=1G", (Path(self.tmp.name) / "args").read_text())

    def test_job_run_without_cap_is_unchanged(self):
        j = mw.job_run("T", "plain", ["true"])
        self.assertNotIn("memory_max", j)
        self.assertFalse((Path(self.tmp.name) / "args").exists())

    def _fake_proc(self):
        proc = Path(self.tmp.name) / "proc"
        (proc / "pressure").mkdir(parents=True)
        (proc / "meminfo").write_text("MemTotal: 16000000 kB\nMemAvailable: 8000000 kB\nSwapTotal: 0 kB\nSwapFree: 0 kB\n")
        (proc / "pressure" / "memory").write_text("some avg10=1.50 avg60=0.00 avg300=0.00 total=5\nfull avg10=0.25 avg60=0.00 avg300=0.00 total=3\n")
        (proc / "loadavg").write_text("2.50 1.00 0.50 1/100 1234\n")
        for pid, cg, rss, comm in ((10, "/system.slice/a.service", 2048, "big"), (11, "/system.slice/a.service", 1024, "small"),
                                   (12, "/user.slice/b.scope", 512, "other")):
            d = proc / str(pid)
            d.mkdir()
            (d / "cgroup").write_text(f"0::{cg}\n")
            (d / "status").write_text(f"Name:\t{comm}\nVmRSS:\t{rss} kB\n")
            (d / "comm").write_text(comm + "\n")
        (proc / "self").mkdir()                                     # non-numeric entries are ignored
        return proc

    def test_resources_groups_by_cgroup_and_reports_pressure_without_thresholds(self):
        proc = self._fake_proc()
        out = mw.resource_state(str(proc), top=5, jobs_base=Path(self.tmp.name) / "none",
                                sessions=[{"name": "X", "sessionId": "abcdef12-0000", "pid": 12}, {"name": "Y", "sessionId": "ff", "pid": 999}])
        self.assertEqual((out["mem_total_mb"], out["mem_available_mb"], out["swap_total_mb"]), (15625, 7812, 0))
        self.assertEqual(out["pressure"]["some"]["avg10"], "1.50")
        self.assertEqual(out["load1"], "2.50")
        top = out["groups"][0]
        self.assertEqual((top["cgroup"], top["rss_mb"], top["procs"], top["largest"]["comm"]), ("/system.slice/a.service", 3, 2, "big"))
        self.assertEqual([s["cgroup"] for s in out["sessions"]], ["b.scope", "?"])   # a vanished pid is "?", not an error
        self.assertNotIn("verdict", out)
        self.assertNotIn("allowed", out)                                          # facts only

    def test_resources_lists_live_jobs_with_their_caps(self):
        with mock.patch.object(mw.shutil, "which", return_value=str(self.bin / "systemd-run")):
            j = mw.job_run("T", "sleeper", ["sleep", "30"], memory_max="1G")
        try:
            out = mw.resource_state(str(self._fake_proc()), jobs_base=mw.state_dir() / "jobs")
            self.assertEqual([(x["label"], x["memory_max"]) for x in out["alive_jobs"]], [("sleeper", "1G")])
        finally:
            try:
                os.killpg(j["pid"], 15)
            except OSError:
                pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
