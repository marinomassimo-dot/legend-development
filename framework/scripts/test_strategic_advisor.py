#!/usr/bin/env python3
"""Plumbing tests for strategic_advisor.py, with a stand-in for the `claude` binary.

These show the snapshot, the neutral brief, the capture path, Stage B reading the saved Stage A,
the attempt ceilings and the check. They do not show that a model obeys its brief; the one real
call is the smoke invocation recorded in the build report.
"""

from __future__ import annotations

import datetime as dt
import contextlib
import io
import json
import re
import ast
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import strategic_advisor as sa  # noqa: E402
_REAL_AGENTS = sa._agents
sa._agents = lambda: None   # no test reads the real runtime's session list; the activity tests pass their own

FAKE = '''#!/usr/bin/env python3
import json, os, sys
brief = sys.stdin.read()
mode = os.environ.get("FAKE_MODE", "ok")
session = "11111111-2222-3333-4444-555555555555"
def emit(o): print(json.dumps(o), flush=True)
emit({"type": "system", "subtype": "init", "session_id": session, "model": "claude-opus-fake", "tools": ["Read", "Glob", "Grep", "WebFetch"], "mcp_servers": [], "permissionMode": "dontAsk"})
if mode == "fail":
    emit({"type": "result", "subtype": "error_during_execution", "is_error": True, "session_id": session})
    sys.exit(1)
text = "## Principal decision\\nX\\n\\n## Inspected\\n- a.md\\nbrief_chars=%d" % len(brief)
if mode == "assign":
    text += ("\\n\\n## Assignments\\n### ASSIGNMENT 1\\nkey: kir2-heteromer-composition\\nrecipient: Science\\nquestion: which Kir2 subunits form the current\\nwhy_now: it gates the Ba2+ arm\\n"
             "roadmap_link: priority 2\\nrelated_work: IT50 closed\\nsources: kir2_drugname_sci49_20261112\\ndecision_changed_by_result: whether any Cys311 activator can act\\n"
             "perimeter_and_budget: one reading package\\nmethod_autonomy: free; negative results welcome\\ndeliver_to: Orchestrator\\nduplicate_check: searched the records for the key\\n"
             "\\n### ASSIGNMENT 2\\nkey: half-written\\nrecipient: Harness\\nquestion: x\\n")
if os.environ.get("FAKE_PORTFOLIO"):
    text += "\\n\\n## Portfolio updates\\n```json\\n" + os.environ["FAKE_PORTFOLIO"] + "\\n```"
outcome = os.environ.get("FAKE_OUTCOME")
if outcome:
    text += "\\n\\n## Outcome\\n" + outcome.replace("|", "\\n")
if mode == "many":
    for i in range(30):
        emit({"type": "assistant", "message": {"id": "t%d" % i, "model": "claude-opus-fake", "content": [{"type": "text", "text": "thinking"}], "usage": {"input_tokens": 1, "output_tokens": 1}}})
if mode == "drift":
    text_t = text + " (changed)"
else:
    text_t = text
second = "claude-opus-fake-2" if mode in ("fallback", "silentswitch") else "claude-opus-fake"
emit({"type": "assistant", "message": {"id": "m1", "model": "claude-opus-fake", "content": [{"type": "tool_use", "id": "t1", "name": "Read", "input": {"file_path": "a.md"}}], "usage": {"input_tokens": 3, "output_tokens": 2}}})
emit({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t1", "content": "ok"}]}})
for i in range(int(os.environ.get("FAKE_CALLS", "0"))):
    emit({"type": "assistant", "message": {"id": "c%d" % i, "model": "claude-opus-fake", "content": [{"type": "tool_use", "id": "x%d" % i, "name": "Read", "input": {"file_path": "b%d.md" % i}}], "usage": {"input_tokens": 1, "output_tokens": 1}}})
    emit({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "x%d" % i, "content": "ok"}]}})
if mode == "fallback":
    emit({"type": "system", "subtype": "model_refusal_fallback", "trigger": "refusal", "apiRefusalCategory": "bio", "scope": "session", "direction": "retry",
          "originalModel": "claude-opus-fake", "fallbackModel": second, "content": "withheld"})
emit({"type": "assistant", "message": {"id": "m2", "model": second, "content": [{"type": "text", "text": text}], "usage": {"input_tokens": 3, "output_tokens": 9}}})
emit({"type": "result", "subtype": "success", "is_error": False, "result": text, "session_id": session, "num_turns": 2, "total_cost_usd": 0.0, "modelUsage": {"claude-opus-fake": {}}, "usage": {"output_tokens": 11}})
root = os.environ.get("LEGEND_ADVISOR_TRANSCRIPTS")
if root:
    rows = [{"type": "assistant", "uuid": "u1", "timestamp": "2026-11-12T00:00:01Z", "message": {"id": "m1", "model": "claude-opus-fake", "content": [{"type": "tool_use", "id": "t1", "name": "Read", "input": {}}], "usage": {"input_tokens": 3, "output_tokens": 2}}},
            {"type": "assistant", "uuid": "u2", "timestamp": "2026-11-12T00:00:02Z", "message": {"id": "m2", "model": second, "content": [{"type": "text", "text": text_t}], "usage": {"input_tokens": 3, "output_tokens": 9}}}]
    open(os.path.join(root, session + ".jsonl"), "w").write("\\n".join(json.dumps(r) for r in rows) + "\\n")
'''


class Base(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="sadv_test_"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)       # 2026-11-24: 19,593 of these were left in /tmp, one per test, ever since the suite was written
        fake = self.tmp / "fake_claude.py"
        fake.write_text(FAKE, encoding="utf-8")
        fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
        self.env = {"LEGEND_ADVISOR_CLAUDE": str(fake), "LEGEND_ADVISOR_RAW": str(self.tmp / "raw"), "LEGEND_ADVISOR_TRANSCRIPTS": str(self.tmp / "tr")}
        (self.tmp / "tr").mkdir()
        self.saved = {k: os.environ.get(k) for k in list(self.env) + ["FAKE_MODE"]}
        os.environ.update(self.env)
        os.environ.pop("FAKE_MODE", None)
        self.campaign = self.tmp / "campaign"
        self.brief = self.tmp / "brief.md"
        self.brief.write_text("# brief\nsome mission\n", encoding="utf-8")

    def tearDown(self) -> None:
        for k, v in self.saved.items():
            os.environ.pop(k, None) if v is None else os.environ.__setitem__(k, v)

    def run_stage(self, stage: str = "A") -> int:
        return sa.run(stage, self.campaign, self.brief, "opus", "high", 60, sa.LIMITS)


class Capture(Base):
    def test_assessment_is_the_result_event_verbatim_and_metadata_reads_back(self) -> None:
        self.assertEqual(self.run_stage(), 0)
        meta = json.loads((self.campaign / "A1" / "meta.json").read_text())
        text = (self.campaign / "A1" / "assessment.md").read_text()
        self.assertTrue(text.startswith("## Principal decision"))
        self.assertEqual(meta["capture"]["assessment_sha256"], sa.sha256_text(text))
        self.assertIs(meta["capture"]["transcript_cross_check"], True)
        self.assertFalse(meta["capture"]["transcribed_by_caller"])
        self.assertEqual(meta["runtime_readback"]["init_tools"], ["Read", "Glob", "Grep", "WebFetch"])
        self.assertEqual(meta["runtime_readback"]["turn_models"], {"claude-opus-fake": 2})
        self.assertEqual(meta["tool_calls"][0]["name"], "Read")
        self.assertEqual(sa.check(self.campaign), 0)

    def test_a_disagreeing_transcript_is_reported(self) -> None:
        os.environ["FAKE_MODE"] = "drift"
        self.assertEqual(self.run_stage(), 0)
        self.assertIs(json.loads((self.campaign / "A1" / "meta.json").read_text())["capture"]["transcript_cross_check"], False)
        self.assertEqual(sa.check(self.campaign), 1)

    def test_sealed_path_refused_is_fine_but_opened_is_a_problem(self) -> None:
        self.run_stage()
        meta_path = self.campaign / "A1" / "meta.json"
        meta = json.loads(meta_path.read_text())
        meta["tool_calls"].append({"name": "Read", "input": {"file_path": f"x/{sa.SEALED}/INTENDED_ACTION_1.md"}, "is_error": True})
        meta_path.write_text(json.dumps(meta))
        self.assertEqual(sa.check(self.campaign), 0)
        meta["tool_calls"][-1]["is_error"] = False
        meta_path.write_text(json.dumps(meta))
        self.assertEqual(sa.check(self.campaign), 1)

    def test_editing_the_saved_assessment_is_detected(self) -> None:
        self.run_stage()
        with (self.campaign / "A1" / "assessment.md").open("a") as handle:
            handle.write("\nquietly added")
        self.assertEqual(sa.check(self.campaign), 1)

    def test_extract_keeps_only_the_last_response(self) -> None:
        rows = [{"type": "assistant", "uuid": "1", "message": {"id": "a", "content": [{"type": "text", "text": "early"}]}},
                {"type": "assistant", "uuid": "2", "message": {"id": "b", "content": [{"type": "text", "text": "final "}]}},
                {"type": "assistant", "uuid": "3", "message": {"id": "b", "content": [{"type": "text", "text": "answer"}]}}]
        path = self.tmp / "t.jsonl"
        path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
        self.assertEqual(sa.extract_transcript(path), "final answer")


class Ceilings(Base):
    def test_failed_attempts_count_and_the_third_stage_a_is_refused(self) -> None:
        os.environ["FAKE_MODE"] = "fail"
        self.assertEqual(self.run_stage(), 1)
        os.environ.pop("FAKE_MODE")
        self.assertEqual(self.run_stage(), 0)
        self.assertEqual(self.run_stage(), 2)
        rows = sa._attempts(self.campaign)
        self.assertEqual(sorted({(r["stage"], r["index"]) for r in rows}), [("A", 1), ("A", 2)])

    def test_smoke_has_its_own_single_allowance(self) -> None:
        self.assertEqual(self.run_stage("S"), 0)
        self.assertEqual(self.run_stage("S"), 2)
        self.assertEqual(self.run_stage("A"), 0)

    def test_one_recorded_extra_attempt_after_a_failure_only(self) -> None:
        os.environ["FAKE_MODE"] = "fail"
        self.assertEqual(self.run_stage("S"), 1)
        self.assertEqual(sa.run("S", self.campaign, self.brief, "opus", "high", 60, sa.LIMITS), 2)      # no reason: refused
        os.environ.pop("FAKE_MODE")
        self.assertEqual(sa.run("S", self.campaign, self.brief, "opus", "high", 60, sa.LIMITS, "S1 failed before any model call"), 0)
        self.assertEqual(sa.run("S", self.campaign, self.brief, "opus", "high", 60, sa.LIMITS, "again"), 2)  # one extra only
        self.assertEqual(sa.check(self.campaign), 0)

    def test_unfinished_attempt_is_reported_by_check(self) -> None:
        sa._append(self.campaign, {"stage": "A", "index": 1, "label": "A1", "outcome": "STARTED"})
        self.assertEqual(sa.check(self.campaign), 1)


class StageBReadsStageA(Base):
    def test_stage_b_brief_embeds_the_saved_assessment_and_the_sealed_intention(self) -> None:
        self.run_stage("A")
        intended = self.tmp / "intended.md"
        intended.write_text("Continue branch Q.", encoding="utf-8")
        sealed = self.tmp / "sealed.txt"
        sealed.write_text("Continue branch Q.", encoding="utf-8")
        text = sa.build_brief("B", self.campaign, "mission", "constraints", "", self.campaign / "A1" / "assessment.md", intended)
        self.assertIn((self.campaign / "A1" / "assessment.md").read_text(), text)
        self.assertIn("Continue branch Q.", text)
        self.assertIn(sa.sha256_file(self.campaign / "A1" / "assessment.md"), text)
        (self.campaign / "brief_B.md").write_text(text, encoding="utf-8")
        self.brief = self.campaign / "brief_B.md"
        self.assertEqual(self.run_stage("B"), 0)
        self.assertEqual(sa.check(self.campaign), 0)

    def test_stage_b_without_stage_a_is_refused_and_stage_a_takes_no_intention(self) -> None:
        with self.assertRaises(ValueError):
            sa.build_brief("B", self.campaign, "m", "c")
        text = sa.build_brief("A", self.campaign, "mission text", "constraints text")
        self.assertNotIn("intended action", text.lower().replace("orchestrator's intended action (complete", ""))
        self.assertEqual(sa.main(["brief", "--stage", "A", "--campaign", str(self.campaign), "--sealed-intended", "x"]), 2)

    def test_seal_writes_inside_the_denied_folder(self) -> None:
        src = self.tmp / "i.md"
        src.write_text("x", encoding="utf-8")
        self.assertEqual(sa.main(["seal", "--campaign", str(self.campaign), "--index", "1", "--text-file", str(src)]), 0)
        self.assertTrue((self.campaign / sa.SEALED / "INTENDED_ACTION_1.md").exists())
        self.assertTrue(any(sa.SEALED in rule for rule in sa.DENIED))


class RecipientsView(unittest.TestCase):
    """2026-11-19 (ADV): the recipients are read as live sessions through route, a restart overlap does not collapse two sessions named SCI, dormant chats are outside the view, and the tick line says
    'no blocker names it'."""
    NOW = dt.datetime(2026, 11, 19, 16, 0, tzinfo=dt.timezone.utc)
    SID = {"HE": "11111111-0000-0000-0000-00000000000a", "IT": "22222222-0000-0000-0000-00000000000b",
           "SCI_OLD": "33333333-0000-0000-0000-00000000000c", "SCI_NEW": "44444444-0000-0000-0000-00000000000d", "CHAT": "55555555-0000-0000-0000-00000000000e"}

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        t = Path(self.tmp.name)
        (t / "ledger" / "tasks").mkdir(parents=True)
        self.proj = t / "projects" / "p"; self.proj.mkdir(parents=True)
        for sid, minutes in ((self.SID["HE"], 0), (self.SID["IT"], 75), (self.SID["SCI_OLD"], 90), (self.SID["SCI_NEW"], 80), (self.SID["CHAT"], 1200)):
            f = self.proj / f"{sid}.jsonl"; f.write_text("{}\n")
            ts = self.NOW.timestamp() - minutes * 60
            os.utime(f, (ts, ts))
        self.patches = [patch.object(sa, "ROOT", t), patch.object(sa, "PROJECTS_DIR", t / "projects")]
        for q in self.patches:
            q.start(); self.addCleanup(q.stop)

    def agents(self, sci_both=True):
        a = lambda key, name, status: {"sessionId": self.SID[key], "name": name, "pid": os.getpid(), "status": status, "kind": "background", "cwd": str(sa.ROOT)}
        out = [a("HE", "HE", "busy"), a("IT", "IT Orchestrator", "idle"), a("SCI_NEW", "SCI", "idle"), a("CHAT", "legend-development-6f", "idle")]
        return out + [a("SCI_OLD", "SCI", "idle")] if sci_both else out

    RECIP = {"Harness": "HE", "Orchestrator": "IT Orchestrator", "Science": "SCI"}

    def test_a_restart_overlap_resolves_to_the_marker_host_and_lists_the_other_as_surplus(self):
        host = lambda task, sessions, projects_dir=None: [{"session_id": self.SID["SCI_NEW"]}] if task == "ORCH-SCI-X" else []
        rec = {"TASK_ID": "ORCH-SCI-X", "ACTOR_ID": "orchestrator", "AUTHORISED_QUEUE_A": {"MANDATE_STATE": "OPEN", "OBJ": {"order": 1, "steps": [{"step": "s", "status": "TODO", "owner": "o"}]}}}
        (sa.ROOT / "ledger" / "tasks" / "x").mkdir(exist_ok=True)
        (sa.ROOT / "ledger" / "tasks" / "x" / "ORCH-SCI-X.json").write_text(json.dumps(rec))
        with patch("mandate_watch.live_bound_sessions", side_effect=host):
            view = sa.recipients_view(self.agents(), self.RECIP, self.NOW)
        sci = view["roles"]["Science"]
        self.assertEqual((sci["state"], sci["session"], sci["surplus"]), ("RESOLVED", self.SID["SCI_NEW"][:8], [self.SID["SCI_OLD"][:8]]))
        self.assertEqual(set(view["roles"]), {"Harness", "Orchestrator", "Science"})                  # the dormant operator chat is not a recipient

    def test_idle_minutes_and_the_all_idle_figure(self):
        view = sa.recipients_view(self.agents(sci_both=False), self.RECIP, self.NOW)
        self.assertEqual((view["roles"]["Harness"]["idle_min"], view["roles"]["Orchestrator"]["idle_min"], view["roles"]["Science"]["idle_min"]), (None, 75, 80))
        self.assertIsNone(view["recipients_all_idle_min"])                                           # HE is busy: not all idle
        agents = [dict(a, status="idle") for a in self.agents(sci_both=False)]
        self.assertEqual(sa.recipients_view(agents, self.RECIP, self.NOW)["recipients_all_idle_min"], 0)   # HE written 0 minutes ago: the shortest idle time

    def test_the_tick_line_says_no_blocker_names_it_and_a_blocker_that_names_the_role_silences_it(self):
        view = sa.recipients_view(self.agents(sci_both=False), self.RECIP, self.NOW)
        self.assertEqual(sa.idle_without_blocker(view, []), ["Orchestrator (IT Orchestrator) idle 75 min", "Science (SCI) idle 80 min"])
        waits = [{"task": "ORCH-SCI-9", "step": "L", "blocker": "SCI waits for the supply of texts"}]
        self.assertEqual(sa.idle_without_blocker(view, waits), ["Orchestrator (IT Orchestrator) idle 75 min"])
        self.assertEqual(sa.idle_without_blocker(view, [{"task": "T", "step": "ITEM two", "blocker": "WITHIN reach"}]), ["Orchestrator (IT Orchestrator) idle 75 min", "Science (SCI) idle 80 min"])   # whole words only
        view["roles"]["Orchestrator"]["idle_min"] = 59
        self.assertEqual(sa.idle_without_blocker(view, waits), [])                                   # at or below the threshold nothing is said


class ContextLines(unittest.TestCase):
    """2026-11-20 (HE): the restart lines of README section 13 are read from the transcript's last usage block and printed on the tick; SCI window 2d2e7085 passed 400k unflagged and ended at 599k."""
    def usage_line(self, cache_read, cache_creation=10, inp=5, output=900):
        return json.dumps({"type": "assistant", "message": {"id": "m", "usage": {"input_tokens": inp, "cache_creation_input_tokens": cache_creation, "cache_read_input_tokens": cache_read, "output_tokens": output}}})

    def write(self, lines, pad=0):
        f = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False); self.addCleanup(os.unlink, f.name)
        f.write("\n".join(lines) + "\n"); f.close()
        return Path(f.name)

    def test_the_last_turn_counts_input_and_both_cache_kinds_and_not_output(self):
        p = self.write([self.usage_line(100_000), '{"type": "user", "message": {"content": "x"}}', self.usage_line(289_985, cache_creation=10, inp=5, output=70_000)])
        self.assertEqual(sa.last_context_tokens(p), 290_000)

    def test_no_usage_block_gives_none_and_a_huge_tail_entry_is_not_misread(self):
        self.assertIsNone(sa.last_context_tokens(self.write(['{"type": "user"}'])))
        self.assertIsNone(sa.last_context_tokens(Path("/nonexistent/x.jsonl")))
        big = json.dumps({"type": "user", "message": {"content": "y" * (sa.CONTEXT_TAIL_BYTES + 10)}})
        self.assertIsNone(sa.last_context_tokens(self.write([self.usage_line(500_000), big])))        # the usage line lies beyond the tail: unknown, never a stale guess presented as current

    def test_each_line_names_its_rule_and_a_quiet_recipient_is_not_flagged(self):
        view = {"roles": {"Science": {"name": "SCI", "context_tokens": 289_000}, "Orchestrator": {"name": "IT Orchestrator", "context_tokens": 407_500},
                          "Advisor": {"name": "ADV", "context_tokens": 206_000}, "Harness": {"name": "HE", "context_tokens": 360_000}, "Unread": {"name": "X"}}}
        flags = sa.context_flags(view)
        self.assertEqual(len(flags), 3)
        self.assertIn("Science (SCI) context 289k: restart at a closed increment", flags)
        self.assertIn("Orchestrator (IT Orchestrator) context 408k: past the never-later line", flags)
        self.assertIn("Harness (HE) context 360k: restart at the next sub-step boundary", flags)


class RadarAndDueWaits(unittest.TestCase):
    """2026-11-20 (HE): the 05:20Z briefing and the BLOCKED step that named 05:20Z both sat until a meeting asked (114 minutes); the tick now says a named time has passed and that a new briefing exists, once."""
    NOW = dt.datetime(2026, 11, 20, 7, 18, tzinfo=dt.timezone.utc)

    def test_a_blocker_that_names_a_past_time_is_due_and_a_future_or_vague_one_is_not(self):
        waits = [{"task": "PLAN-X", "step": "Read the first radar briefing", "blocker": "the first briefing is produced at 2026-11-20T05:20Z by the daily scout"},
                 {"task": "T2", "step": "s", "blocker": "awaits 2026-11-20T09:00Z"}, {"task": "T3", "step": "s", "blocker": "awaits 2026-11-20T07:15Z"},
                 {"task": "T4", "step": "s", "blocker": "the supply of texts, tomorrow, 2026-11-19"}, {"task": "T5", "step": "s", "blocker": "bad 2026-13-45T25:61Z"}]
        lines = sa.due_waits(waits, self.NOW)
        self.assertEqual(len(lines), 1)
        self.assertIn("PLAN-X", lines[0]); self.assertIn("past by 118 min", lines[0])                   # 3 minutes late (07:15) is inside the grace; 09:00 is the future

    def test_a_new_briefing_is_reported_once_with_its_items_and_nothing_when_it_has_no_item(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "scout_daily_briefing.md"
            f.write_text("RADAR BRIEFING x\nDelta 1: Discovery:reopen:glia/NP4G2\n  detail\nDelta 2: Discovery:open-slot\n", encoding="utf-8")
            state: dict = {}
            first = sa.radar_news(state, f)
            self.assertIn("2 item(s) to examine", first); self.assertIn("Discovery:open-slot", first); self.assertIn("forward the useful ones by name", first)
            self.assertEqual(sa.radar_news(state, f), "")                                               # the same briefing is not reported again
            os.utime(f, (f.stat().st_mtime + 3600, f.stat().st_mtime + 3600))
            self.assertIn("NEW RADAR BRIEFING", sa.radar_news(state, f))                               # a later run is new
            f.write_text("RADAR BRIEFING y\nNEXT STEP: none\n", encoding="utf-8"); os.utime(f, (f.stat().st_mtime + 7200,) * 2)
            self.assertEqual(sa.radar_news(state, f), "")                                               # a briefing without items is silent
            self.assertEqual(sa.radar_news({}, Path(td) / "absent.md"), "")


class UncheckedWaits(unittest.TestCase):
    """2026-11-20: prose blockers were never evaluated against main; the line names the BLOCKED steps with no machine-checkable `unblock_when`, once per change."""
    WAITS = [{"task": "ORCH-IT-X", "step": "a", "blocker": "SCI's reading lands", "checkable": False}, {"task": "ORCH-IT-X", "step": "b", "blocker": "x", "checkable": False},
             {"task": "PLAN-Y", "step": "c", "blocker": "file", "checkable": True}]

    def test_counts_per_task_once_per_change_and_silent_when_all_are_checkable(self):
        state: dict = {}
        first = sa.unchecked_waits(self.WAITS, state)
        self.assertIn("ORCH-IT-X x2", first); self.assertNotIn("PLAN-Y", first); self.assertIn("unblock_when", first)
        self.assertEqual(sa.unchecked_waits(self.WAITS, state), "")                                      # the same set is not repeated every hour
        self.assertIn("ORCH-IT-X x1", sa.unchecked_waits(self.WAITS[:1] + self.WAITS[2:], state))        # a change is reported
        self.assertEqual(sa.unchecked_waits([dict(w, checkable=True) for w in self.WAITS], state), "")

    def test_the_waits_reader_marks_a_step_with_unblock_when_as_checkable(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); (root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
            rec = {"TASK_ID": "ORCH-Z", "AUTHORISED_QUEUE_X": {"MANDATE_STATE": "OPEN", "OBJ_1": {"order": 1, "steps": [
                {"step": "p", "status": "BLOCKED", "owner": "o", "blocker": "b1", "unblock_when": {"path": "no/such/file.txt"}},
                {"step": "q", "status": "BLOCKED", "owner": "o", "blocker": "b2"}, {"step": "r", "status": "TODO", "owner": "o"}]}}}
            (root / "ledger" / "tasks" / "orchestrator" / "ORCH-Z.json").write_text(json.dumps(rec))
            with patch.object(sa, "ROOT", root):
                waits = {w["step"]: w["checkable"] for w in sa._waits()}
        self.assertEqual(waits, {"p": True, "q": False})


class RotationReconcileDream(unittest.TestCase):
    """2026-11-20 (operator): scientific rotation after three increments in one strand, daily portfolio reconciliation by Europe/Rome day, and the dream pass after a significant result. Every obligation is derived
    from the files (the assignment log, the portfolio, the task records), so a new session finds it; none of it blocks work."""
    NOW = dt.datetime(2026, 11, 20, 12, 0, tzinfo=dt.timezone.utc)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.campaign = self.root / "camp"; self.campaign.mkdir()
        (self.root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
        (self.root / sa.PORTFOLIO_REL).parent.mkdir(parents=True)
        for each in (patch.object(sa, "ROOT", self.root), patch.object(sa, "DREAM_RULE_FROM", "2026-11-20T00:00:00Z"), patch.dict(os.environ, {"LEGEND_ADVISOR_NOW": "2026-11-20T12:00:00Z"})):
            each.start(); self.addCleanup(each.stop)

    def log(self, **row):
        with (self.campaign / "assignments.jsonl").open("a") as fh:
            fh.write(json.dumps({"utc": "2026-11-20T08:00:00Z", **row}) + "\n")

    def inc(self, ident, strand, hhmm, **extra):
        sa.record_strand(self.campaign, ident, strand, "test basis", at=f"2026-11-20T{hhmm}:00Z", **extra)

    def portfolio(self, rows):
        head = "\t".join(sa.PORTFOLIO_FIELDS)
        body = ["\t".join(r.get(k, "") for k in sa.PORTFOLIO_FIELDS) for r in rows]
        (self.root / sa.PORTFOLIO_REL).write_text("\n".join([head, *body]) + "\n", encoding="utf-8")

    def test_three_increments_in_one_strand_make_the_rotation_due_and_two_do_not(self):
        self.inc("X1", "agents", "01:00"); self.inc("X2", "agents", "02:00")
        self.assertEqual(sa.rotation_status(self.campaign)["state"], "OK")
        self.inc("X3", "agents", "03:00")
        r = sa.rotation_status(self.campaign)
        self.assertEqual((r["state"], r["run"]), ("DUE", 3)); self.assertIn("SCIENTIFIC ROTATION DUE", r["line"]); self.assertIn("not another compound in the same question", r["line"])
        self.assertTrue(any("ROTATION DUE" in ln for ln in sa.discipline_lines(self.campaign)))

    def test_a_different_strand_in_between_breaks_the_run_and_folded_or_harness_work_is_not_counted(self):
        self.inc("X1", "agents", "01:00"); self.inc("X2", "agents", "02:00"); self.inc("X2b", "agents", "02:30", counts_with="X2")      # producer and verifier of one result: one increment
        self.inc("H1", "harness", "02:40")                                                                                                  # harness work is not a scientific increment
        self.assertEqual(sa.rotation_status(self.campaign)["run"], 2)
        self.inc("Y1", "other", "03:00"); self.inc("X4", "agents", "04:00"); self.inc("X5", "agents", "05:00")
        self.assertEqual(sa.rotation_status(self.campaign)["run"], 2)                                                                       # the run is the trailing one

    def test_an_open_assignment_in_another_strand_is_the_rotation_under_way_and_none_is_duplicated(self):
        for i, h in enumerate(("01:00", "02:00", "03:00")):
            self.inc(f"X{i}", "agents", h)
        self.log(id="ADV-899", state="DRAFTED", key="old", recipient="Science", strand="myelin", utc="2026-11-19T09:00:00Z"); self.log(id="ADV-899", state="SENT", to=["SCI"])
        self.assertEqual(sa.rotation_status(self.campaign)["state"], "DUE")                                         # an old assignment still open in another strand is not the rotation
        self.log(id="ADV-900", state="DRAFTED", key="k", recipient="Science", strand="agents")                       # open work in the dominant strand does not count as a rotation
        self.assertEqual(sa.rotation_status(self.campaign)["state"], "DUE")
        self.assertEqual(sa.rotation_status(self.campaign)["open_same"], ["ADV-900"])
        self.log(id="ADV-901", state="DRAFTED", key="k2", recipient="Science", strand="myelin"); self.log(id="ADV-901", state="SENT", to=["SCI"])
        r = sa.rotation_status(self.campaign)
        self.assertEqual((r["state"], r["open_other"]), ("IN_PROGRESS", ["ADV-901"])); self.assertIn("no second rotation", r["line"])

    def test_an_assignment_counts_once_its_recipient_marks_a_step_naming_it_done(self):
        self.log(id="ADV-910", state="DRAFTED", key="a", recipient="Science", strand="agents"); self.log(id="ADV-910", state="SENT", to=["SCI"])
        self.assertEqual(sa.increments(self.campaign), [])
        rec = {"TASK_ID": "ORCH-SCI-T", "ACTOR_ID": "orchestrator", "AUTHORISED_QUEUE_X": {"OBJ_1": {"order": 1, "steps": [{"step": "ADV-910 work", "status": "DONE", "evidence": "commit abc"}]}}}
        (self.root / "ledger/tasks/orchestrator/ORCH-SCI-T.json").write_text(json.dumps(rec))
        self.assertEqual([r["id"] for r in sa.increments(self.campaign)], ["ADV-910"])
        rec["AUTHORISED_QUEUE_X"]["OBJ_1"]["steps"][0]["updated_at"] = "2026-11-20T11:30:00Z"
        (self.root / "ledger/tasks/orchestrator/ORCH-SCI-T.json").write_text(json.dumps(rec))
        self.assertEqual(sa.increments(self.campaign)[0]["at"], "2026-11-20T11:30:00Z")                            # concluded when the recipient marked it DONE, not when it was sent
        self.assertNotIn("STRAND", sa.assignment_states(self.campaign)["ADV-910"]["levels"])                          # the metadata events are not evidence levels

    def test_a_deferral_is_recorded_stays_visible_and_ends_when_another_strand_concludes(self):
        for i, h in enumerate(("01:00", "02:00", "03:00")):
            self.inc(f"X{i}", "agents", h)
        sa.defer_rotation(self.campaign, "a concrete urgency", "after the pilot brief is signed")
        r = sa.rotation_status(self.campaign)
        self.assertEqual(r["state"], "DEFERRED"); self.assertIn("still due", r["line"]); self.assertIn("after the pilot brief is signed", r["line"])
        self.assertEqual(len(sa.defer_rotation(self.campaign, "", "")["warnings"]), 2)                               # nothing refuses: a deferral without reason or resume point is recorded with two warnings
        sa.defer_rotation(self.campaign, "a concrete urgency", "after the pilot brief is signed")
        self.log(state="STRAND", id="Z1", strand="myelin", basis="b", at="2026-11-20T11:00:00Z", utc="2026-11-20T11:00:01Z")
        self.assertEqual(sa.rotation_status(self.campaign)["state"], "OK")

    def test_unclassified_recent_executed_work_is_listed_not_counted(self):
        self.log(id="ADV-920", state="DRAFTED", key="u", recipient="Science"); self.log(id="ADV-920", state="SENT", to=["SCI"], utc="2026-11-20T09:00:00Z")
        rec = {"TASK_ID": "ORCH-SCI-U", "ACTOR_ID": "orchestrator", "AUTHORISED_QUEUE_X": {"OBJ_1": {"order": 1, "steps": [{"step": "ADV-920", "status": "DONE", "evidence": "commit abc"}]}}}
        (self.root / "ledger/tasks/orchestrator/ORCH-SCI-U.json").write_text(json.dumps(rec))
        self.inc("X1", "agents", "01:00")
        r = sa.rotation_status(self.campaign)
        self.assertEqual(r["unclassified"], ["ADV-920"]); self.assertIn("UNCLASSIFIED", r["line"])

    def test_the_daily_reconciliation_is_due_once_per_europe_rome_day_and_residuals_stay_visible(self):
        self.portfolio([{"id": "RP-001", "opportunity": "o", "status": "ready", "updated_utc": "2026-11-01T00:00:00Z"}])
        self.assertTrue(sa.reconcile_state(self.campaign, self.NOW)["due"])
        row = sa.attest_reconciliation(self.campaign, "NO_CHANGE", ["RP-404"], [], now=self.NOW)                      # an unknown id is a warning, the attestation is still recorded
        self.assertTrue(any("not portfolio ids" in w for w in row["warnings"]))
        self.assertFalse(sa.reconcile_state(self.campaign, self.NOW)["due"])
        self.log(state="RECONCILED", rome_date="2026-11-19", result="NO_CHANGE", changed=[], residual=[])
        self.assertFalse(sa.reconcile_state(self.campaign, self.NOW)["due"])
        late = dt.datetime(2026, 11, 20, 23, 30, tzinfo=dt.timezone.utc)                                          # 00:30 on 21 November in Rome: a new day
        self.assertTrue(sa.reconcile_state(self.campaign, late)["due"])
        sa.attest_reconciliation(self.campaign, "CHANGED", ["RP-001"], ["RP-002:Science"], now=late)
        st = sa.reconcile_state(self.campaign, late)
        self.assertFalse(st["due"]); self.assertIn("RESIDUAL INCOHERENCES: RP-002 (Science)", st["line"])
        self.assertEqual(st["last"]["result"], "CHANGED+RESIDUAL")

    def test_reconciliation_finds_rows_whose_event_already_happened(self):
        self.log(id="ADV-930", state="DRAFTED", key="w", recipient="Science"); self.log(id="ADV-930", state="SENT", to=["SCI"])
        rec = {"TASK_ID": "ORCH-SCI-W", "ACTOR_ID": "orchestrator", "AUTHORISED_QUEUE_X": {"OBJ_1": {"order": 1, "steps": [{"step": "ADV-930", "status": "DONE", "evidence": "commit abc"}]}}}
        (self.root / "ledger/tasks/orchestrator/ORCH-SCI-W.json").write_text(json.dumps(rec))
        self.portfolio([{"id": "RP-001", "opportunity": "o", "status": "waiting", "resume_when": "ADV-930 delivers", "updated_utc": "2026-11-01T00:00:00Z"},
                        {"id": "RP-002", "opportunity": "o", "status": "waiting", "resume_when": "a new paper", "updated_utc": "2026-11-01T00:00:00Z"}])
        found = {c["id"]: c for c in sa.reconcile_findings(self.campaign, self.NOW)}
        self.assertEqual(list(found), ["RP-001"]); self.assertIn("already concluded", found["RP-001"]["why"]); self.assertEqual(found["RP-001"]["owner"], "Science")

    def test_reconciliation_also_lists_ready_rows_named_by_a_later_assignment_and_backlog_rows_named_in_a_delivery(self):
        (self.campaign / "assignments").mkdir()
        (self.campaign / "assignments" / "ADV-940.md").write_text("roadmap_link: RP-001 and nothing else\n")
        self.log(id="ADV-940", state="DRAFTED", key="k", recipient="Science", utc="2026-11-20T09:00:00Z")
        self.portfolio([{"id": "RP-001", "opportunity": "o", "status": "ready", "updated_utc": "2026-11-01T00:00:00Z"},
                        {"id": "RP-002", "opportunity": "o", "status": "backlog", "updated_utc": "2026-11-01T00:00:00Z"},
                        {"id": "RP-003", "opportunity": "o", "status": "ready", "updated_utc": "2026-11-20T10:00:00Z"}])
        with patch.object(sa, "_git", return_value="abc1234 SCI: RP-002 result delivered"):
            found = {c["id"]: c["why"] for c in sa.reconcile_findings(self.campaign, self.NOW)}
        self.assertEqual(sorted(found), ["RP-001", "RP-002"])                                                    # RP-003 was updated after the assignment: not listed
        self.assertIn("ADV-940", found["RP-001"]); self.assertIn("recent delivery", found["RP-002"])

    def test_a_dream_connection_reaches_its_consumer_and_is_listed_until_the_consumer_absorbs_it(self):
        self.portfolio([{"id": "RP-001", "opportunity": "o", "status": "ready", "updated_utc": "2026-11-20T09:00:00Z"}])
        self.inc("X1", "agents", "10:00")
        self.log(state="DREAM", ids=["X1"], connections=[{"to": "RP-001", "what": "a comparator the myelin row lacks"}], none_reason="", counter="contrary result kept", utc="2026-11-20T11:00:00Z")
        found = {c["id"]: c["why"] for c in sa.reconcile_findings(self.campaign, self.NOW)}
        self.assertIn("DREAM connection from X1", found["RP-001"])
        sa.portfolio_update({"id": "RP-001", "next_action": "use the comparator"})                                 # the consumer absorbs it: no longer listed
        self.assertNotIn("RP-001", {c["id"] for c in sa.reconcile_findings(self.campaign, self.NOW)})

    def test_an_unchanged_portfolio_row_keeps_its_historical_date_and_a_changed_one_moves(self):
        self.portfolio([{"id": "RP-001", "opportunity": "o", "status": "ready", "next_action": "n", "updated_utc": "2026-11-01T00:00:00Z"}])
        before = (self.root / sa.PORTFOLIO_REL).read_text()
        row = sa.portfolio_update({"id": "RP-001", "status": "ready", "next_action": "n"})
        self.assertEqual(row["updated_utc"], "2026-11-01T00:00:00Z"); self.assertEqual((self.root / sa.PORTFOLIO_REL).read_text(), before)
        row = sa.portfolio_update({"id": "RP-001", "next_action": "something else"})
        self.assertEqual(row["updated_utc"], "2026-11-20T12:00:00Z")

    def test_a_portfolio_patch_works_in_a_linked_worktree_on_its_own_tsv_while_the_campaign_commands_still_refuse(self):
        self.portfolio([{"id": "RP-001", "opportunity": "o", "status": "ready", "next_action": "n", "updated_utc": "2026-11-01T00:00:00Z"}])
        (self.root / ".git").write_text("gitdir: /elsewhere\n", encoding="utf-8")                   # this checkout is now a linked worktree
        self.assertTrue(sa.primary_refusal())
        patch_file = self.root / "patch.json"; patch_file.write_text(json.dumps({"id": "RP-001", "next_action": "patched in the worktree"}), encoding="utf-8")
        with patch.dict(os.environ, {"LEGEND_ADVISOR_STATE": str(self.root / "state")}), patch.object(sa, "STATE_DIR", self.root / "state"):
            self.assertEqual(sa.main(["portfolio", "--upsert", str(patch_file)]), 0)                  # the refusal protects the campaign state, not this checkout's own TSV
        self.assertIn("patched in the worktree", (self.root / sa.PORTFOLIO_REL).read_text(encoding="utf-8"))
        self.assertEqual(sa.main(["tick", "--campaign", str(self.campaign)]), 2)                      # the campaign commands still refuse a linked worktree

    def test_the_dream_pass_is_pending_until_recorded_and_an_unread_consumer_is_a_warning_not_a_refusal(self):
        self.portfolio([{"id": "RP-001", "opportunity": "o", "status": "ready"}])
        self.inc("X1", "agents", "10:00")
        self.assertEqual(sa.dream_pending(self.campaign, self.NOW), ["X1"]); self.assertTrue(any("DREAM PENDING" in ln for ln in sa.discipline_lines(self.campaign)))
        self.assertTrue(sa.record_dream(self.campaign, [], [], "")["warnings"])                                      # an empty pass is recorded and reported, never refused
        out = sa.record_dream(self.campaign, ["X1"], [("RP-001", "a comparator for the myelin row"), ("NOWHERE-7", "x")], "")
        self.assertEqual(len(out["warnings"]), 2)                                                                  # unknown consumer, and no statement on contrary results
        self.assertEqual(sa.dream_pending(self.campaign, self.NOW), [])
        self.inc("X2", "agents", "11:00")
        sa.record_dream(self.campaign, ["X2"], [], "no connection: nothing in the held record bears on it", counter="no contrary result")
        self.assertEqual(sa.dream_pending(self.campaign, self.NOW), [])

    def test_a_new_session_finds_every_obligation_from_the_files_alone(self):
        for i, h in enumerate(("01:00", "02:00", "03:00")):
            self.inc(f"X{i}", "agents", h)
        sa.defer_rotation(self.campaign, "r", "p")
        sa.attest_reconciliation(self.campaign, "NO_CHANGE", [], [], now=self.NOW)
        import importlib
        fresh = importlib.reload(sa)                                                                                # nothing is kept in memory: reload and read again
        with patch.object(fresh, "ROOT", self.root):
            self.assertEqual(fresh.rotation_status(self.campaign)["state"], "DEFERRED")
            self.assertFalse(fresh.reconcile_state(self.campaign, self.NOW)["due"])


class CiOnMain(unittest.TestCase):
    """ADV-108: a red publication gate on main must reach the tick, with the run that began the streak; unreadable or in progress is never read as green or red."""
    NOW = dt.datetime(2026, 11, 20, 14, 0, tzinfo=dt.timezone.utc)

    def run_(self, n, concl, status="completed", branch="main", name="Public release gate"):
        return {"run_number": n, "conclusion": concl, "status": status, "head_branch": branch, "head_sha": f"{n:040x}", "name": name}

    def test_the_red_streak_ends_at_the_last_green_run_and_skips_runs_in_progress(self):
        import ci_runs
        runs = [self.run_(1512, "success"), self.run_(1513, "failure"), self.run_(1514, "failure"), self.run_(1515, None, "in_progress"), self.run_(1516, "failure"), self.run_(1599, "failure", branch="other")]
        r = ci_runs.red_streak(runs)
        self.assertEqual((r["red"], r["latest"], r["first_red"], r["streak"]), (True, 1516, 1513, 3))
        self.assertFalse(ci_runs.red_streak([self.run_(1, "failure"), self.run_(2, "success")])["red"])
        self.assertEqual(ci_runs.red_streak([self.run_(1, None, "in_progress")]), {})

    def test_the_tick_line_names_the_first_red_run_is_cached_and_a_failed_read_is_silent(self):
        import ci_runs
        runs = [self.run_(1512, "success"), self.run_(1513, "failure"), self.run_(1514, "failure")]
        state: dict = {}
        with patch.object(ci_runs, "fetch_recent", return_value=runs) as fetch, patch.object(ci_runs, "slug", return_value="o/r"):
            line = sa.ci_main_line(state, self.NOW)
            self.assertIn("CI RED ON MAIN", line); self.assertIn("red since #1513", line); self.assertIn("2 run(s)", line)
            self.assertEqual(sa.ci_main_line(state, self.NOW + dt.timedelta(minutes=10)), line)
            self.assertEqual(fetch.call_count, 1)                                                         # one request per half hour at most
        with patch.object(ci_runs, "fetch_recent", side_effect=OSError("offline")), patch.object(ci_runs, "slug", return_value="o/r"):
            self.assertEqual(sa.ci_main_line(state, self.NOW + dt.timedelta(minutes=40)), line)           # unreadable keeps the last known line, never claims green
            self.assertEqual(sa.ci_main_line({}, self.NOW), "")


class AssignmentFlow(unittest.TestCase):
    """2026-11-20 (ADV, 'Reliable autonomy'): SENT -> TAKEN (a recipient record names the exact id) -> FIRST OUTPUT (a commit subject or added file naming it); flags for a send nobody took and a take with no output."""
    NOW = dt.datetime(2026, 11, 20, 12, 0, tzinfo=dt.timezone.utc)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.campaign = self.root / "camp"; self.campaign.mkdir()
        (self.root / "ledger" / "tasks" / "orchestrator").mkdir(parents=True)
        for cmd in (["init", "-q", "-b", "main"], ["config", "user.email", "t@example.invalid"], ["config", "user.name", "t"]):
            subprocess.run(["git", *cmd], cwd=self.root, check=True)
        self.patch = patch.object(sa, "ROOT", self.root); self.patch.start(); self.addCleanup(self.patch.stop)

    def event(self, ident, state, hhmm, **extra):
        row = {"id": ident, "state": state, "utc": f"2026-11-20T{hhmm}:00Z", **extra}
        with (self.campaign / "assignments.jsonl").open("a") as fh:
            fh.write(json.dumps(row) + "\n")

    def commit(self, subject, hhmm, files=()):
        for f in files:
            (self.root / f).parent.mkdir(parents=True, exist_ok=True); (self.root / f).write_text("x")
        (self.root / "n.txt").write_text(subject)
        env = {**os.environ, "GIT_COMMITTER_DATE": f"2026-11-20T{hhmm}:00Z", "GIT_AUTHOR_DATE": f"2026-11-20T{hhmm}:00Z"}
        subprocess.run(["git", "add", "-A"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-q", "-m", subject], cwd=self.root, check=True, env=env)

    def record(self, task, step_text, accepted):
        rec = {"TASK_ID": task, "AUTHORISED_QUEUE_X": {"MANDATE_STATE": "OPEN", "OBJ_1": {"order": 1, "steps": [{"step": step_text, "status": "IN_PROGRESS", "owner": "x", "source": step_text, "accepted_at": f"2026-11-20T{accepted}:00Z"}]}}}
        (self.root / "ledger" / "tasks" / "orchestrator" / f"{task}.json").write_text(json.dumps(rec))

    def flow(self):
        return {r["id"]: r for r in sa.assignment_flow(self.campaign, self.NOW, ref="HEAD")}

    def test_taken_and_output_are_found_by_exact_id_and_the_presidios_own_commit_is_not_output(self):
        self.event("ADV-777", "DRAFTED", "09:00", recipient="Science"); self.event("ADV-777", "SENT", "09:05")
        self.record("ORCH-SCI-X", "ADV-777 take the reading", "09:20")
        self.commit("ADV: registered and sent ADV-777", "09:06")                                    # the sender's commit: not output
        self.commit("SCI: ADV-7770 something else", "09:30")                                        # another id that starts with the digits: not a match
        self.commit("SCI: ADV-777 increment 1", "09:50")
        r = self.flow()["ADV-777"]
        self.assertEqual((r["taken_utc"], r["taken_in"]), ("2026-11-20T09:20:00Z", "ORCH-SCI-X"))
        self.assertTrue(r["output_utc"].startswith("2026-11-20T09:50")); self.assertIn("increment 1", r["output"])
        self.assertEqual(r["flag"], "")
        self.assertIn("TAKEN 09:20Z (+15 min", sa.flow_line(r))

    def test_a_send_nobody_took_is_flagged_after_30_minutes_and_a_take_with_no_output_after_3_hours(self):
        self.event("ADV-778", "DRAFTED", "11:00", recipient="Harness"); self.event("ADV-778", "SENT", "11:20")      # 40 minutes ago, no record, no commit
        self.event("ADV-779", "DRAFTED", "07:00", recipient="Science"); self.event("ADV-779", "SENT", "07:05")      # taken at 07:30, silent for 4.5 hours
        self.record("ORCH-SCI-Y", "ADV-779 do it", "07:30")
        self.commit("unrelated work", "11:00")
        flows = self.flow()
        self.assertEqual(flows["ADV-778"]["flag"], "SENT, NOT TAKEN after 40 min")
        self.assertEqual(flows["ADV-779"]["flag"], "TAKEN, no output after 4.5 h")
        self.event("ADV-780", "DRAFTED", "11:50", recipient="Science"); self.event("ADV-780", "SENT", "11:50")
        self.assertEqual(self.flow()["ADV-780"]["flag"], "")                                         # ten minutes: inside the allowed time

    def test_a_checkpoint_that_names_the_id_before_the_take_is_shown_apart_from_the_first_work_and_the_presidios_record_is_not_a_take(self):
        self.event("ADV-781", "DRAFTED", "08:00", recipient="Science"); self.event("ADV-781", "SENT", "08:05")
        self.commit("SCI: checkpoint M, next ADV-781", "08:10")
        self.record("ORCH-SCI-Z", "ADV-781 accepted", "08:40")
        rec = {"TASK_ID": "ORCH-ADV-FOLLOWTHROUGH-1", "AUTHORISED_QUEUE_X": {"MANDATE_STATE": "OPEN", "OBJ_1": {"order": 1, "steps": [{"step": "ADV-781 sent", "status": "DONE", "owner": "adv", "accepted_at": "2026-11-20T08:06:00Z", "evidence": "e1 recorded and verified"}]}}}
        (self.root / "ledger" / "tasks" / "orchestrator" / "ORCH-ADV-FOLLOWTHROUGH-1.json").write_text(json.dumps(rec))
        self.commit("SCI: ADV-781 first result", "09:00")
        r = self.flow()["ADV-781"]
        self.assertEqual(r["taken_in"], "ORCH-SCI-Z")                                                 # the sender's record is excluded
        self.assertTrue(r["output_utc"].startswith("2026-11-20T08:10")); self.assertTrue(r["output_after_take_utc"].startswith("2026-11-20T09:00"))
        self.assertIn("FIRST OUTPUT AFTER TAKEN 09:00Z", sa.flow_line(r))

    def test_a_done_step_in_a_recipient_record_ends_the_no_output_flag(self):
        self.event("ADV-784", "DRAFTED", "07:00", recipient="Harness"); self.event("ADV-784", "SENT", "07:05")
        self.record("PLAN-X", "ADV-784 disk", "07:30")
        self.commit("unrelated", "11:00")
        self.assertEqual(self.flow()["ADV-784"]["flag"], "TAKEN, no output after 4.5 h")
        path = self.root / "ledger" / "tasks" / "orchestrator" / "PLAN-X.json"
        path.write_text(path.read_text().replace("IN_PROGRESS", "DONE"))
        self.assertEqual(self.flow()["ADV-784"]["flag"], "")

    def test_old_assignments_are_listed_but_not_flagged_and_nothing_sent_gives_nothing(self):
        self.assertEqual(sa.assignment_flow(self.campaign, self.NOW, ref="HEAD"), [])
        self.event("ADV-782", "DRAFTED", "10:00", recipient="Science")
        self.assertEqual(sa.assignment_flow(self.campaign, self.NOW, ref="HEAD"), [])                 # drafted is not sent
        with (self.campaign / "assignments.jsonl").open("a") as fh:
            fh.write(json.dumps({"id": "ADV-783", "state": "SENT", "utc": "2026-11-18T10:00:00Z"}) + "\n")
        self.commit("x", "08:00")
        r = self.flow()["ADV-783"]
        self.assertEqual(r["flag"], "")                                                                # 50 hours old: inside the listing window, outside the flag window


class ClaudeBinary(unittest.TestCase):
    """2026-11-19 (ADV): in the session's own shell `claude` is not on PATH; the activity block was silently omitted at every in-session tick."""

    def test_the_listing_uses_the_known_install_path_when_path_lacks_claude(self):
        calls = []

        def fake_run(cmd, **kw):
            calls.append(cmd[0])
            class R: returncode = 0; stdout = "[]"
            return R()
        with patch.dict(os.environ, {"LEGEND_ADVISOR_CLAUDE": ""}), patch("mandate_watch.shutil.which", return_value=None), patch.object(sa.subprocess, "run", fake_run):
            self.assertEqual(_REAL_AGENTS(), [])
        self.assertTrue(calls[0].endswith("/.local/bin/claude"))                                    # the fallback of mandate_watch.claude_bin, not a bare 'claude'
        with patch.dict(os.environ, {"LEGEND_ADVISOR_CLAUDE": "/opt/x/claude"}), patch.object(sa.subprocess, "run", fake_run):
            _REAL_AGENTS()
        self.assertEqual(calls[1], "/opt/x/claude")                                                  # the explicit override still wins


class Profile(unittest.TestCase):
    def test_launch_flags_are_read_only_and_never_bare(self) -> None:
        cmd = sa.claude_command("opus", "high")
        joined = " ".join(cmd)
        self.assertIn("--agent legend-strategic-advisor", joined)
        self.assertIn("--tools Read,Glob,Grep,WebFetch", joined)
        self.assertNotIn("--restricted", cmd)  # it hides the project agents: measured
        self.assertEqual(cmd[cmd.index("--allowedTools") + 1], "WebFetch")
        self.assertIn("--strict-mcp-config", cmd)
        self.assertNotIn("--bare", cmd)  # --bare would require an API key: new spend
        self.assertNotIn("--dangerously-skip-permissions", cmd)
        deny = cmd[cmd.index("--disallowedTools") + 1:]
        for tool in ("Bash", "Write", "Edit", "Agent", "SendMessage"):
            self.assertIn(tool, deny)

    def test_agent_definition_declares_the_same_read_only_tools(self) -> None:
        text = (Path(__file__).resolve().parents[2] / ".claude/agents/legend-strategic-advisor.md").read_text(encoding="utf-8")
        header = text.split("---")[1]
        tools = [line for line in header.splitlines() if line.startswith("tools:")][0].split(":", 1)[1]
        self.assertEqual({t.strip() for t in tools.split(",")}, set(sa.TOOLS))
        words = len(text.split("---", 2)[2].split())
        self.assertTrue(500 <= words <= 1400, words)


class ModelChange(Base):
    def test_a_runtime_fallback_is_disclosed_with_the_model_that_wrote_the_answer(self) -> None:
        os.environ["FAKE_MODE"] = "fallback"
        self.assertEqual(self.run_stage(), 0)
        read_back = json.loads((self.campaign / "A1" / "meta.json").read_text())["runtime_readback"]
        self.assertEqual(read_back["init_model"], "claude-opus-fake")
        self.assertEqual(read_back["final_turn_model"], "claude-opus-fake-2")
        self.assertEqual([(f["originalModel"], f["fallbackModel"], f["apiRefusalCategory"]) for f in read_back["refusal_fallbacks"]], [("claude-opus-fake", "claude-opus-fake-2", "bio")])
        self.assertNotIn("withheld", json.dumps(read_back))  # the runtime's free text is not carried
        self.assertTrue(read_back["census"]["changed_mid_run"])
        self.assertEqual(sa.check(self.campaign), 0)  # explained and disclosed, not a failed record

    def test_a_model_change_with_no_runtime_reason_stays_a_problem(self) -> None:
        os.environ["FAKE_MODE"] = "silentswitch"
        self.assertEqual(self.run_stage(), 0)
        self.assertEqual(sa.check(self.campaign), 1)


def mock_entry_points(rows):
    from unittest import mock
    return mock.patch.object(sa, "ENTRY_POINTS", rows)


def _git_repo() -> tuple[Path, dict[str, str]]:
    """A repository whose `main` is ahead of the branch the advisor would be run from — the 2026-11-12 SCI48 case."""
    tmp = Path(tempfile.mkdtemp(prefix="sadv_git_"))
    unittest.addModuleCleanup(shutil.rmtree, tmp, ignore_errors=True)       # a plain function, not a TestCase: the module's teardown removes it
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}

    def git(*args: str) -> str:
        return subprocess.run(["git", *args], cwd=tmp, check=True, capture_output=True, text=True, env=env).stdout.strip()
    git("init", "-q", "-b", "main")
    (tmp / "tracked.md").write_text("one", encoding="utf-8")
    git("add", "."); git("commit", "-q", "-m", "base")
    git("checkout", "-q", "-b", "task")
    git("checkout", "-q", "main")
    (tmp / "pkg_sci48").mkdir()
    (tmp / "pkg_sci48" / "README.md").write_text("delivered", encoding="utf-8")
    git("add", "."); git("commit", "-q", "-m", "SCI48 delivered")
    git("checkout", "-q", "task")
    return tmp, {"delivered": git("rev-parse", "main"), "run": "git"}



EXCL = "ORCH-A: its intake is blocked on a source that needs a human check"      # a path (a record id) with its actual cause, as a hold now requires


def _record(task: str, state: str, extra: dict | None = None) -> dict:
    """A task record the continuity module reads: an OPEN one has a step still to do, a COMPLETE one has its step done with evidence."""
    step = {"step": "work", "status": "TODO" if state == "OPEN" else "DONE", "owner": "x", "evidence": "" if state == "OPEN" else "evidence recorded and verified in full"}
    return {"TASK_ID": task, "AUTHORISED_QUEUE_X": {"MANDATE_STATE": state, "OBJ_1": {"order": 1, "title": "t", "steps": [step]}}, **(extra or {})}


def _repo_with_records(tmp: Path, records: dict[str, str]) -> Path:
    """A throwaway git repository with task records and a roadmap section: what the hourly check reads."""
    repo, env = tmp / "repo", {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}
    (repo / "ledger/tasks/orchestrator").mkdir(parents=True)
    (repo / "disease-models/wwox/research/drug_repurposing").mkdir(parents=True)
    for task, state in records.items():
        (repo / f"ledger/tasks/orchestrator/{task}.json").write_text(json.dumps(_record(task, state)), encoding="utf-8")
    (repo / "disease-models/wwox/research/drug_repurposing/roadmap_current.md").write_text(f"x\n{sa.ROADMAP_BEGIN}\nMission v1\n{sa.ROADMAP_END}\n", encoding="utf-8")
    for cmd in (["git", "init", "-q", "-b", "main"], ["git", "add", "."], ["git", "commit", "-q", "-m", "base"]):
        subprocess.run(cmd, cwd=repo, check=True, capture_output=True, env=env)
    return repo


class DirectionBeforeStatus(Base):
    """Input delivery and ordering only: these fixtures cannot certify strategic judgment."""

    def setUp(self) -> None:
        super().setUp()
        self.repo = _repo_with_records(self.tmp, {})
        self.patches = [patch.object(sa, "ROOT", self.repo),
                        patch.object(sa, "ROADMAP", self.repo / "disease-models/wwox/research/drug_repurposing/roadmap_current.md"),
                        patch.object(sa, "STATE_DIR", self.tmp / "state")]
        for p in self.patches:
            p.start()
        self.canonical = self.repo / "framework/protocols/cross_session_transport.md"
        self.canonical.parent.mkdir(parents=True, exist_ok=True)
        self.rule = "**Direction before status (fixture).** Choose from the mission and source map, then reconcile the laboratory wait."
        self.canonical.write_text("# Transport\n\n" + self.rule + "\n\nUnrelated later policy.\n")
        self.obs = {"events": [], "open_mandates": [], "waits": ["laboratory unavailable"],
                    "queue": {"exhausted": True}, "sessions": {}, "commits_since_last_tick": 0}

    def tearDown(self) -> None:
        for p in reversed(self.patches):
            p.stop()
        super().tearDown()

    def test_source_map_precedes_operational_wait_and_previous_assessment_without_hiding_them(self) -> None:
        prior = self.campaign / "P7/assessment.md"
        prior.parent.mkdir(parents=True)
        prior.write_text("Earlier decision: wait for a laboratory.")
        brief = sa.build_brief_p(self.campaign, self.obs)
        headings = ["## Operator roadmap", "## Direction before status", "## Neutral entry points",
                    "## Observed state", "## Previous assessment"]
        positions = [brief.index(h) for h in headings]
        self.assertEqual(positions, sorted(positions))
        self.assertIn(self.rule, brief)
        self.assertIn("laboratory unavailable", brief)
        self.assertIn(str(prior), brief)
        self.assertEqual(brief.count("## Neutral entry points"), 1)
        self.assertEqual(brief.count("Unrelated later policy"), 0)
        self.assertEqual(sa._attempts(self.campaign), [], "building a brief must not call a model")

    def test_canonical_revision_reaches_next_brief_without_a_second_policy_copy(self) -> None:
        first = sa.build_brief_p(self.campaign, self.obs)
        revised = self.rule.replace("Choose from the mission", "Compare a different scientific branch from the mission")
        self.canonical.write_text("# Transport\n\n" + revised + "\n\nUnrelated later policy.\n")
        second = sa.build_brief_p(self.campaign, self.obs)
        self.assertIn(self.rule, first)
        self.assertIn(revised, second)
        self.assertNotIn(self.rule, second)
        self.assertEqual(sa._attempts(self.campaign), [])

    def test_missing_guidance_is_visible_and_does_not_invent_a_strategic_outcome(self) -> None:
        self.canonical.unlink()
        brief = sa.build_brief_p(self.campaign, self.obs)
        self.assertIn("Canonical guidance unavailable", brief)
        self.assertIn("laboratory unavailable", brief)
        self.assertEqual(sa.parse_assignments(brief), [])
        self.assertEqual(sa._attempts(self.campaign), [])


class WaitingWork(Base):
    """2026-11-21 (ADV): the tick states, read-only, how long ago the host last edited the portfolio or recorded a DREAM, and which waiting rows name nothing to wait for."""
    NOW = dt.datetime(2026, 11, 21, 13, 0, tzinfo=dt.timezone.utc)

    def rows(self, *specs):
        return [{"id": i, "status": st, "resume_when": rw, "updated_utc": up} for i, st, rw, up in specs]

    def test_bare_or_empty_resume_when_of_a_waiting_row_is_listed_and_nothing_else(self) -> None:
        self.campaign.mkdir()
        rows = self.rows(("RP-015", "waiting", "", "2026-11-17T13:28:30Z"), ("RP-017", "waiting", "event", "2026-11-15T07:29:20Z"),
                         ("RP-018", "waiting", "An eIF2-alpha datum", "2026-11-20T14:53:20Z"), ("RP-040", "ready", "", "2026-11-21T12:10:00Z"),
                         ("RP-041", "waiting", "after:2026-12-01T00:00:00Z", "2026-11-21T11:00:00Z"))
        with patch.object(sa, "portfolio_rows", return_value=(rows, [])):
            out = sa.waiting_work(self.campaign, self.NOW)
        self.assertEqual(out["waiting_without_resume"], ["RP-015", "RP-017"])
        self.assertEqual(out["minutes_since_host_edit"], 50)                         # newest row edit 12:10Z, now 13:00Z
        self.assertTrue(out["line"].startswith("waiting_work: 50 min since the last portfolio edit RP-040"))
        self.assertIn("RP-015, RP-017", out["line"])

    def test_a_later_dream_line_is_the_last_host_edit_and_no_record_is_stated_not_guessed(self) -> None:
        self.campaign.mkdir()
        rows = self.rows(("RP-017", "waiting", "event", "2026-11-21T12:10:00Z"))
        (self.campaign / "assignments.jsonl").write_text(json.dumps({"state": "DREAM", "ids": ["ADV-1"], "utc": "2026-11-21T12:40:00Z"}) + "\n"
                                                        + json.dumps({"state": "DRAFTED", "id": "ADV-2", "utc": "2026-11-21T12:55:00Z"}) + "\n", encoding="utf-8")
        with patch.object(sa, "portfolio_rows", return_value=(rows, [])):
            out = sa.waiting_work(self.campaign, self.NOW)
        self.assertEqual((out["minutes_since_host_edit"], out["last_host_edit"]["kind"]), (20, "DREAM"))          # a DRAFTED line is not a DREAM
        with patch.object(sa, "portfolio_rows", return_value=([], [])):
            empty = sa.waiting_work(self.tmp / "no_campaign", self.NOW)
        self.assertIsNone(empty["minutes_since_host_edit"])
        self.assertEqual(empty["waiting_without_resume"], [])
        self.assertIn("no DREAM or portfolio edit on record", empty["line"])

    def test_the_tick_carries_the_field_and_its_verdict_does_not_depend_on_it(self) -> None:
        repo = _repo_with_records(self.tmp, {"ORCH-CLOSED": "COMPLETE"})
        with patch.object(sa, "ROOT", repo), patch.object(sa, "STATE_DIR", self.tmp / "state"), patch.object(sa, "_sessions", return_value={}), \
                patch.dict(os.environ, {"LEGEND_ADVISOR_NOW": "2026-11-21T13:00:00Z"}):
            self.campaign.mkdir()
            plain = sa.tick(self.campaign)
            self.assertIn("waiting_work", plain)
            with patch.object(sa, "waiting_work", return_value={"line": "x"}):
                other = sa.tick(self.campaign)
        self.assertEqual({"minutes_since_host_edit", "last_host_edit", "waiting_without_resume", "line"}, set(plain["waiting_work"]))
        self.assertEqual(plain["verdict"], other["verdict"])


class HostDecisions(Base):
    """Exercise the real host path, not model obedience or scientific judgment."""

    def setUp(self) -> None:
        super().setUp()
        self.repo = _repo_with_records(self.tmp, {"ORCH-CLOSED": "COMPLETE"})
        self.patches = [patch.object(sa, "ROOT", self.repo),
                        patch.object(sa, "ROADMAP", self.repo / "disease-models/wwox/research/drug_repurposing/roadmap_current.md"),
                        patch.object(sa, "STATE_DIR", self.tmp / "state"),
                        patch.object(sa, "_sessions", return_value={"SCI": "idle"}),
                        patch.dict(os.environ, {"LEGEND_ADVISOR_NOW": "2026-11-17T16:00:00Z"})]
        for p in self.patches:
            p.start()
        self.campaign.mkdir(exist_ok=True)
        (self.campaign / "budget.json").write_text(json.dumps({"expires_utc": "2026-11-14T00:00:00Z", "max_invocations": 1, "max_assignments": 1}))
        (self.campaign / sa.CONTINUOUS).write_text(json.dumps({"mode": "continuous", "authorised_utc": "2026-11-14T00:00:00Z"}))
        self.text = ("## Assignments\n### ASSIGNMENT 1\nkey: next-scientific-question\nrecipient: Science\n"
                     "question: Which current observation distinguishes the competing mechanisms?\n"
                     "why_now: the previous result is consumed; the laboratory branch is blocked, this reading is not\n"
                     "roadmap_link: generation and open questions\nrelated_work: previous case closed\n"
                     "sources: held original and current question row\ndecision_changed_by_result: choose the next comparison\n"
                     "perimeter_and_budget: one original-source pass; shared allocation; no spend\n"
                     "method_autonomy: correct the premise or propose a better method\ndeliver_to: Orchestrator\n"
                     "duplicate_check: existing owner records checked\n")

    def tearDown(self) -> None:
        for p in reversed(self.patches):
            p.stop()
        super().tearDown()

    def test_host_choice_has_honest_provenance_no_model_or_fake_send_and_no_renewed_budget(self) -> None:
        frozen_budget = (self.campaign / "budget.json").read_bytes()
        with patch.object(sa, "run", side_effect=AssertionError("must not call a consultant")):
            self.assertEqual(sa.host_assign(self.campaign, self.text), 0)
        self.assertEqual(sa._attempts(self.campaign), [])
        self.assertEqual((self.campaign / "budget.json").read_bytes(), frozen_budget)
        rows = sa._events(self.campaign)
        self.assertEqual([(r["state"], r["origin"]) for r in rows], [("DRAFTED", "host")])
        self.assertIn("not an independent assessment", (self.campaign / "assignments/ADV-001.md").read_text())
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "DRAFTED")
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["origin"], "host")
        self.assertNotIn("last_evaluation_utc", sa._load_state(self.campaign))
        self.assertEqual(sa.host_assign(self.campaign, self.text), 0)
        self.assertEqual(sum(r["state"] == "DRAFTED" for r in sa._events(self.campaign)), 1)

    def test_a_host_choice_settles_its_event_but_a_later_delivery_remains_actionable(self) -> None:
        sa.tick(self.campaign)
        state = sa._load_state(self.campaign)
        state.update(pending_events=["delivery: abc1234 previous result consumed"], pending_commits=1)
        sa._save_state(self.campaign, state)
        self.assertEqual(sa.host_assign(self.campaign, self.text), 0)
        quiet = sa.tick(self.campaign)
        self.assertEqual(quiet["verdict"], "NONE")
        self.assertEqual(sa._load_state(self.campaign)["pending_events"], [])
        self.assertEqual(quiet["evaluation_clock"]["source"], "recorded host decision (not a model evaluation)")
        original = sa.observe
        def delivered(campaign, state):
            obs = original(campaign, state)
            obs["events"].append("delivery: def5678 new independent result")
            return obs
        with patch.object(sa, "observe", side_effect=delivered):
            self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")

    def test_pause_disable_and_bounded_pilot_cannot_be_bypassed_by_a_host_draft(self) -> None:
        for refusal in ["operator suspension", "weekly allocation exhausted", "campaign disabled"]:
            with self.subTest(refusal=refusal), patch.object(sa, "budget_refusal", return_value=refusal):
                self.assertEqual(sa.host_assign(self.campaign, self.text), 2)
        (self.campaign / sa.CONTINUOUS).unlink()
        self.assertEqual(sa.host_assign(self.campaign, self.text), 2)
        self.assertEqual(sa._events(self.campaign), [])

    def test_a_delivery_arriving_during_registration_is_not_consumed_with_the_old_choice(self) -> None:
        sa.tick(self.campaign)
        register = sa.register_assignments
        def arrived(*args, **kwargs):
            state = sa._load_state(self.campaign)
            state["pending_events"] = ["delivery: abc1234 result arriving during registration"]
            state["pending_commits"] = 1
            sa._save_state(self.campaign, state)
            return register(*args, **kwargs)
        with patch.object(sa, "register_assignments", side_effect=arrived):
            self.assertEqual(sa.host_assign(self.campaign, self.text), 0)
        self.assertEqual(sa._load_state(self.campaign)["pending_events"], ["delivery: abc1234 result arriving during registration"])
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")

    def test_independent_host_help_does_not_interrupt_or_replace_a_running_consultation(self) -> None:
        sa._save_state(self.campaign, {"running": "fixture", "pending_events": ["delivery: pending"], "last_outcome": {"evaluation": "P7"}})
        before = sa._load_state(self.campaign)
        with patch.object(sa, "_running", return_value=True):
            self.assertEqual(sa.host_assign(self.campaign, self.text), 0)
        self.assertEqual(sa._load_state(self.campaign), before)
        self.assertEqual(sa._events(self.campaign)[0]["origin"], "host")

    def test_current_source_index_deduplicates_history_and_follows_observed_main(self) -> None:
        rel = "disease-models/wwox/research/result.md"
        calls = []
        def git(*args, **kwargs):
            calls.append(args)
            if args[:2] == ("diff", "--name-only"):
                return rel
            if args[:2] == ("rev-parse", "--verify"):
                return "current-blob" if args[-1] == "feed1234:" + rel else "stale-blob"
            if args[0] == "hash-object":
                return "current-blob"
            return ""
        (self.repo / rel).parent.mkdir(parents=True, exist_ok=True)
        (self.repo / rel).write_text("current consumed result")
        with patch.object(sa, "_git", side_effect=git):
            rendered = sa.current_result_sources({"main_sha": "feed1234", "events": ["delivery: abc1234 first result", "delivery: def5678 merged correction"]}, {"repo_sha": "oldhead", "main_ahead": []})
        self.assertEqual(rendered.count("- `" + rel + "`"), 1)
        self.assertIn("same bytes readable here", rendered)
        self.assertIn("Change provenance: abc1234, def5678", rendered)
        self.assertIn(("diff", "--name-only", "def5678^", "def5678"), calls)
        self.assertNotIn("DIFFERS OR UNAVAILABLE", rendered)

    def test_removed_current_source_is_not_presented_as_a_live_old_delivery(self) -> None:
        rel = "disease-models/wwox/research/removed.md"
        with patch.object(sa, "_git", side_effect=lambda *a, **k: rel if a[0] == "diff" else ""):
            rendered = sa.current_result_sources({"main_sha": "feed1234", "events": ["delivery: abc1234 old file"]}, {"repo_sha": "feed1234"})
        self.assertIn("removed at observed main", rendered)

    def test_a_newer_ref_modifying_an_existing_source_is_explicit_even_without_a_new_folder(self) -> None:
        rel = "disease-models/wwox/research/existing.md"
        def git(*args, **kwargs):
            if args[0] == "diff":
                return rel
            if args[0] == "rev-parse":
                return "new-blob" if args[-1].startswith("newtip:") else "old-blob"
            return ""
        with patch.object(sa, "_git", side_effect=git):
            rendered = sa.current_result_sources({"main_sha": "oldtip", "events": []},
                {"repo_sha": "oldtip", "main_ahead": [{"tip": "newtip", "new_folders": []}]})
        self.assertIn(rel, rendered)
        self.assertIn("Newer known ref `newtip`", rendered)
        self.assertIn("NOT supplied by the observed-main copy", rendered)

    def test_activity_and_canonical_accountability_reach_the_analyst_without_a_launch(self) -> None:
        path = self.repo / "framework/protocols/cross_session_transport.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("### Laboratory ownership (fixture)\n\nThe host owns the programme.\n\n### Next section\nDo not copy this.\n")
        obs = sa.observe(self.campaign, {})
        obs["activity"] = {"available": True, "idle_share": "3/4", "idle_over_half": True}
        brief = sa.build_brief_p(self.campaign, obs)
        self.assertIn('"idle_share": "3/4"', brief)
        self.assertIn("The host owns the programme.", brief)
        self.assertNotIn("Do not copy this.", brief)
        self.assertEqual(sa._attempts(self.campaign), [])


class ProactiveFixture(Base):
    """The proactive pilot: bounded hourly check, one evaluation per decision, assignments with evidence levels, budget and disable. Fixtures: they do not show the real runtime."""

    def setUp(self) -> None:
        super().setUp()
        self.repo = _repo_with_records(self.tmp, {"ORCH-A": "OPEN", "ORCH-B": "COMPLETE"})
        self.state = self.tmp / "state"
        self.saved_attrs = {k: getattr(sa, k) for k in ("ROOT", "ROADMAP", "STATE_DIR", "_sessions")}
        sa.ROOT, sa.ROADMAP, sa.STATE_DIR = self.repo, self.repo / "disease-models/wwox/research/drug_repurposing/roadmap_current.md", self.state
        sa._sessions = lambda: {"IT Orchestrator": "idle", "SCI": "idle", "HE": "busy"}
        self.campaign = self.tmp / "pilot"
        sa.main(["activate", "--campaign", str(self.campaign), "--recipient", "Science=SCI"])
        self.env_now = os.environ.get("LEGEND_ADVISOR_NOW")
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T10:00:00Z"

    def tearDown(self) -> None:
        for k, v in self.saved_attrs.items():
            setattr(sa, k, v)
        os.environ.pop("LEGEND_ADVISOR_NOW", None) if self.env_now is None else os.environ.__setitem__("LEGEND_ADVISOR_NOW", self.env_now)
        super().tearDown()

    def land(self, subject: str, record: tuple[str, str] | None = None) -> None:
        env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}
        if record:
            (self.repo / f"ledger/tasks/orchestrator/{record[0]}.json").write_text(json.dumps(_record(record[0], record[1])), encoding="utf-8")
        (self.repo / "ledger/tasks/orchestrator/touch.txt").write_text(subject, encoding="utf-8")
        for cmd in (["git", "add", "."], ["git", "commit", "-q", "-m", subject]):
            subprocess.run(cmd, cwd=self.repo, check=True, capture_output=True, env=env)

    def at(self, stamp: str) -> None:
        os.environ["LEGEND_ADVISOR_NOW"] = stamp



class Empathy(ProactiveFixture):
    """The existing hourly decision gets the current reason, including with an old recall job."""

    def guidance(self, text: str, control: str = "") -> None:
        sa.ROADMAP.write_text(sa.ROADMAP_BEGIN + "\n" + control + "\n" + sa.mc.GUIDANCE_BEGIN + "\n" + text
                              + "\n" + sa.mc.GUIDANCE_END + "\n" + sa.ROADMAP_END, encoding="utf-8")

    def test_tick_reads_revised_guidance_without_recreating_the_recall(self) -> None:
        self.guidance("At a closure compare other branches. Why: continuity.")
        first = sa.tick(self.campaign)
        self.assertTrue(first["operator_guidance"]["available"])
        self.assertIn("Why: continuity", first["operator_guidance"]["text"])
        self.guidance("Revised criterion and source after an operator correction.")
        self.assertIn("Revised criterion", sa.tick(self.campaign)["operator_guidance"]["text"])
        self.assertIn("operator_guidance", sa.recall_prompt(self.campaign))

    def test_guidance_cannot_lift_an_operator_pause_or_launch_an_evaluation(self) -> None:
        self.guidance("Continue useful work without a fresh prompt.", "PAUSE: advisor")
        self.assertEqual(sa.main(["authorise-continuous", "--campaign", str(self.campaign), "--source", "fixture operator authorisation"]), 0)
        out = sa.tick(self.campaign)
        self.assertEqual(out["verdict"], "PAUSED")
        self.assertIn("Continue useful", out["operator_guidance"]["text"])
        self.assertEqual(list(self.campaign.glob("P[0-9]*")), [])


class Proactive(ProactiveFixture):
    """The proactive pilot: bounded hourly check, one evaluation per decision, assignments with evidence levels, budget and disable. Fixtures: they do not show the real runtime."""

    def test_the_first_tick_starts_the_campaign_and_then_nothing_new_costs_no_evaluation(self) -> None:
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")        # campaign start: a strategic choice from the roadmap and the first observation
        sa.evaluate(self.campaign)                                              # counted (1 of 3)
        self.at("2026-11-13T11:00:00Z")
        quiet = sa.tick(self.campaign)
        self.assertEqual((quiet["verdict"], quiet["events"]), ("NONE", []))     # nothing changed: the previous assessment stands, no model call
        self.assertEqual(len({(a["stage"], a["index"]) for a in sa._attempts(self.campaign)}), 1)

    def test_a_new_delivery_triggers_exactly_one_evaluation_and_the_same_events_do_not_repeat_it(self) -> None:
        sa.evaluate(self.campaign)
        self.at("2026-11-13T11:00:00Z"); sa.tick(self.campaign)
        self.land("SCI51 record COMPLETE; package delivered")
        self.at("2026-11-13T12:00:00Z")
        first = sa.tick(self.campaign)
        self.assertEqual(first["verdict"], "EVALUATE")
        self.assertTrue(any(e.startswith("delivery:") for e in first["events"]))
        sa.evaluate(self.campaign)
        brief = (sa._state_path(self.campaign).parent / "brief_P.md").read_text(encoding="utf-8")
        self.assertIn("delivery:", brief)                                       # the tick advanced its own state; the brief must still carry what triggered the evaluation (seen empty in the first pilot)
        self.assertNotIn('"commits_since_last_tick": 0', brief)
        self.at("2026-11-13T13:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")             # the digest of those events was already evaluated

    def test_a_linked_worktree_refuses_to_become_a_second_campaign_and_the_recall_text_is_one(self) -> None:
        wt = self.tmp / "linked"; wt.mkdir(); (wt / ".git").write_text("gitdir: /elsewhere\n", encoding="utf-8")
        saved, sa.ROOT = sa.ROOT, wt
        try:
            for cmd in ("tick", "evaluate", "meeting", "deliver", "activate", "disable", "recall"):
                self.assertTrue(sa.primary_refusal(), cmd)
            self.assertEqual(sa.main(["tick", "--campaign", str(self.campaign)]), 2)      # refused before it touches any state
            self.assertEqual(sa.main(["meeting", "--campaign", str(self.campaign), "--open"]), 2)
            self.assertEqual(sa.main(["refresh", "--campaign", str(self.campaign)]), 2)
        finally:
            sa.ROOT = saved
        self.assertEqual(sa.primary_refusal(), "")                                   # the primary checkout has a .git directory
        text = sa.recall_prompt(self.campaign)
        self.assertIn(sa.RECALL_MARK, text)
        for cmd in ("tick", "meeting", "evaluate"):
            self.assertIn(f"strategic_advisor.py {cmd} --campaign {self.campaign}", text)
        self.assertEqual(text.count(sa.RECALL_MARK), 1)
        for must in ("idle share above half", "activity", "route --to <role>", "do not record a send that did not happen"):
            self.assertIn(must, text)  # preserve HE60's monitor-and-help coverage

    def test_the_live_scout_briefing_reaches_the_brief_dated_without_addresses_and_absence_is_stated(self) -> None:
        saved = sa.STATE_HOME
        try:
            sa.STATE_HOME = self.tmp / "no_such_cache"
            self.assertIn("no live scouting briefing", sa.scout_briefing())
            sa.STATE_HOME = self.tmp / "cache"; sa.STATE_HOME.mkdir()
            (sa.STATE_HOME / "scout_daily_briefing.md").write_text("RADAR BRIEFING\nNEXT STEP: read x (contact " + "someone" + chr(64) + "example.org" + ")\n" + "z" * 7000, encoding="utf-8")
            text = sa.scout_briefing()
            self.assertIn("file time", text); self.assertIn("first 6000", text); self.assertNotIn("someone" + chr(64), text); self.assertIn("[address removed]", text)
        finally:
            sa.STATE_HOME = saved

    def test_a_running_evaluation_is_not_overlapped_and_a_waiting_session_is_not_called_stalled(self) -> None:
        sa.evaluate(self.campaign)
        state = sa._load_state(self.campaign); state["running"] = sa._pid_identity(os.getpid()); sa._save_state(self.campaign, state)
        self.land("IT99 closed")
        self.at("2026-11-13T15:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "RUNNING")
        # a mandate the watch calls resumable is reported to the watch, never restarted here; a mandate that is merely waiting does not appear at all
        state["running"] = ""; sa._save_state(self.campaign, state)
        log = self.tmp / "watch.txt"; log.write_text("STOPPED_RESUMABLE RESUME ORCH-A: session idle", encoding="utf-8")
        real = sa.subprocess.run
        sa.subprocess.run = lambda cmd, **kw: subprocess.CompletedProcess(cmd, 0, stdout=log.read_text(), stderr="") if "mandate_watch.py" in " ".join(map(str, cmd)) else real(cmd, **kw)
        try:
            events = sa.tick(self.campaign)["events"]
        finally:
            sa.subprocess.run = real
        self.assertTrue(any(e.startswith("stalled-for-the-watch: ORCH-A") for e in events))
        self.assertFalse(any("ORCH-B" in e for e in events))                    # a COMPLETE mandate is never reported as stalled

    def test_assignments_are_drafted_once_with_their_fields_and_an_incomplete_or_duplicate_one_is_refused(self) -> None:
        os.environ["FAKE_MODE"] = "assign"
        self.assertEqual(sa.evaluate(self.campaign), 0)
        drafted = [e for e in sa._events(self.campaign)]
        self.assertEqual([(e["id"], e["state"]) for e in drafted if e["state"] == "DRAFTED"], [("ADV-001", "DRAFTED")])
        self.assertTrue(any(e["state"] == "REJECTED" and "missing fields" in e["why"] for e in drafted))   # the half-written block is not an assignment
        self.assertIn("kir2-heteromer-composition", (self.campaign / "assignments/ADV-001.md").read_text())
        text = (self.campaign / "P1/assessment.md").read_text()
        sa.register_assignments(self.campaign, "P1", text)                      # the same key again
        self.assertTrue(any(e["state"] == "DUPLICATE" for e in sa._events(self.campaign)))
        (self.repo / "ledger/tasks/orchestrator/ORCH-A.json").write_text(json.dumps(_record("ORCH-A", "OPEN", {"x": "kir2-heteromer-composition"})), encoding="utf-8")
        self.assertEqual(sa.register_assignments(self.campaign, "P2", text.replace("kir2-heteromer-composition", "kir2-heteromer-composition")), [])   # already named in a task record

    def test_the_evidence_levels_of_an_assignment_stay_apart(self) -> None:
        os.environ["FAKE_MODE"] = "assign"; sa.evaluate(self.campaign)
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "DRAFTED")           # saved is not sent
        sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "SENT", "--evidence", "msg 5361f893-5cdd-41aa-9bc3-0123456789ab", "--to", "SCI"])
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "SENT")              # sent is not taken in charge
        rec = self.repo / "ledger/tasks/orchestrator/ORCH-A.json"
        rec.write_text(json.dumps(_record("ORCH-A", "OPEN", {"Q": {"s": {"step": "ADV-001 taken", "status": "TODO"}}})), encoding="utf-8")
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "TAKEN")
        rec.write_text(json.dumps(_record("ORCH-A", "OPEN", {"Q": {"s": {"step": "ADV-001 taken", "status": "DONE"}}})), encoding="utf-8")
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "EXECUTED")          # executed is not useful: nothing here says so

    def test_a_receipt_for_another_session_is_not_a_delivery_and_a_missing_receipt_is_refused(self) -> None:
        os.environ["FAKE_MODE"] = "assign"; sa.evaluate(self.campaign)
        row = [e for e in sa._events(self.campaign) if e["id"] == "ADV-001"][0]
        self.assertEqual(row["recipient"], "Science")                                                       # the budget maps Science to the session SCI
        base = ["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "SENT", "--evidence", "msg 5361f893-5cdd-41aa-9bc3-0123456789ab"]
        self.assertEqual(sa.main(base + ["--to", "HE"]), 2)                                                 # the receipt names HE: not a delivery to SCI
        self.assertEqual(sa.main(base), 2)                                                                  # no receipt at all: the text of a message is not one
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "DRAFTED")
        self.assertEqual(sa.main(base + ["--to", "HE", "--to", "sci"]), 0)                                  # two real sends, one of them to the session in question
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "SENT")
        self.assertIn('"to": ["HE", "sci"]', (self.campaign / "assignments.jsonl").read_text(encoding="utf-8"))
        self.assertEqual(sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "UNREACHABLE", "--evidence", "no live session"]), 0)   # no receipt exists for that
        self.assertEqual(sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-099", "--state", "SENT", "--evidence", "msg 5361f893-5cdd-41aa-9bc3-0123456789ab", "--to", "SCI"]), 2)   # not a drafted assignment

    def test_a_sent_needs_the_sends_own_receipt_id(self) -> None:
        """2026-11-19 (ADV, three times in two days): a SENT recorded before the send happened. The msg_id SendMessage returns (a UUID) is required in --receipt or inside --evidence."""
        os.environ["FAKE_MODE"] = "assign"; sa.evaluate(self.campaign)
        base = ["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "SENT", "--to", "SCI"]
        self.assertEqual(sa.main(base + ["--evidence", "msg 1"]), 2)                                      # no receipt id: refused
        self.assertEqual(sa.main(base + ["--evidence", "sent it", "--receipt", "not-a-uuid"]), 2)          # something that is not a receipt id: refused
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "DRAFTED")             # nothing was recorded
        rid = "6e1f2a9c-0b3d-4c5e-8f70-a1b2c3d4e5f6"
        self.assertEqual(sa.main(base + ["--evidence", "sent to SCI", "--receipt", rid]), 0)
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "SENT")
        self.assertIn(rid, (self.campaign / "assignments.jsonl").read_text(encoding="utf-8"))               # the receipt id is kept in the log
        self.assertEqual(sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "UNREACHABLE", "--evidence", "no live session"]), 0)   # UNREACHABLE needs none

    def test_a_recipient_revived_under_another_name_is_still_the_recipient_and_a_dead_listed_one_is_not(self) -> None:
        """2026-11-18: the Science session came back as 'orch-adv004-mandate-reconciliation'; the budget said 'SCI', so a real send could not be recorded. Identity is the session id, resolved against LIVE sessions."""
        os.environ["FAKE_MODE"] = "assign"; sa.evaluate(self.campaign)
        sci, he, dead = "9400b253-0000-0000-0000-000000000001", "29e50812-0000-0000-0000-000000000002", "deadbeef-0000-0000-0000-000000000003"
        live = [{"sessionId": sci, "name": "orch-adv004-mandate-reconciliation", "pid": os.getpid(), "status": "idle"},
                {"sessionId": he, "name": "HE", "pid": os.getpid(), "status": "busy"},
                {"sessionId": dead, "name": "SCI", "state": "working"}]                      # a killed session still listed: no pid, no status
        budget = json.loads((self.campaign / "budget.json").read_text()); budget["recipients"]["Science"] = "9400b253"       # the budget names the session by its id prefix
        (self.campaign / "budget.json").write_text(json.dumps(budget), encoding="utf-8")
        base = ["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "SENT", "--evidence", "msg 5361f893-5cdd-41aa-9bc3-0123456789ab"]
        with patch.object(sa, "_agents", lambda: live):
            self.assertEqual(sa.main(base + ["--to", "HE"]), 2)                                              # another live session: not a delivery to Science
            self.assertEqual(sa.main(base + ["--to", "SCI"]), 2)                                             # the name SCI now belongs to a dead entry: it does not resolve to the live session
            self.assertEqual(sa.main(base + ["--to", "orch-adv004-mandate-reconciliation"]), 0)               # the receipt names the session by its current name: same id, accepted
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "SENT")

    def test_a_recipient_role_that_resolves_to_no_live_session_cannot_be_recorded_as_sent(self) -> None:
        os.environ["FAKE_MODE"] = "assign"; sa.evaluate(self.campaign)
        budget = json.loads((self.campaign / "budget.json").read_text()); budget["recipients"]["Science"] = "NOBODY"
        (self.campaign / "budget.json").write_text(json.dumps(budget), encoding="utf-8")
        live = [{"sessionId": "11111111-0000-0000-0000-000000000009", "name": "HE", "pid": os.getpid(), "status": "idle"}]
        with patch.object(sa, "_agents", lambda: live):
            msg = sa.delivery_refusal(self.campaign, "ADV-001", "SENT", ["HE"], "msg 5361f893-5cdd-41aa-9bc3-0123456789ab")
        self.assertIn("does not resolve to exactly one live session", msg)
        self.assertIn("UNREACHABLE", msg)

    def test_the_senders_own_records_never_count_as_a_recipient_taking_or_executing_an_assignment(self) -> None:
        os.environ["FAKE_MODE"] = "assign"; sa.evaluate(self.campaign)
        sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "SENT", "--evidence", "msg 5361f893-5cdd-41aa-9bc3-0123456789ab", "--to", "SCI"])
        for name in ("ORCH-ADV-PRESIDIO-X", "PLAN-PROACTIVE-ADVISOR-X"):
            (self.repo / f"ledger/tasks/orchestrator/{name}.json").write_text(
                json.dumps(_record(name, "OPEN", {"Q": {"s": {"step": "ADV-001 delivered by message", "status": "DONE"}}})), encoding="utf-8")   # the delivery step of the sender: DONE, naming the id
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "SENT")              # seen as EXECUTED a minute after SENT in the pilot
        (self.repo / "ledger/tasks/orchestrator/ORCH-RECIPIENT.json").write_text(
            json.dumps(_record("ORCH-RECIPIENT", "OPEN", {"Q": {"s": {"step": "ADV-001 taken", "status": "TODO"}}})), encoding="utf-8")
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "TAKEN")             # a recipient's own record still counts
        (self.repo / "ledger/tasks/orchestrator/ORCH-RECIPIENT.json").unlink()
        (self.repo / "ledger/tasks/orchestrator/PLAN-ADV-SESSION-X.json").write_text(                          # Harness is a recipient too: its record is not a sender record
            json.dumps(_record("PLAN-ADV-SESSION-X", "OPEN", {"Q": {"s": {"step": "ADV-001 taken", "status": "TODO"}}})), encoding="utf-8")
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "TAKEN")

    def test_an_unreachable_recipient_is_an_explicit_residual_not_a_delivery(self) -> None:
        os.environ["FAKE_MODE"] = "assign"; sa.evaluate(self.campaign)
        sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "UNREACHABLE", "--evidence", "no live session named SCI"])
        v = sa.assignment_states(self.campaign)["ADV-001"]
        self.assertTrue(v["unreachable"])
        self.assertEqual(v["highest"], "DRAFTED")
        self.assertIn("UNREACHABLE (residual stays in the queue)", sa.status(self.campaign))

    def test_an_operator_instruction_in_the_roadmap_triggers_a_new_evaluation_with_the_new_text(self) -> None:
        sa.evaluate(self.campaign)
        self.at("2026-11-13T11:00:00Z"); self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        road = sa.ROADMAP; road.write_text(road.read_text().replace("Mission v1", "Mission v1\nOperator 2026-11-13: pause the EBP thread"), encoding="utf-8")
        self.at("2026-11-13T11:30:00Z")
        t = sa.tick(self.campaign)
        self.assertEqual(t["verdict"], "EVALUATE")
        self.assertTrue(t["why"].startswith("roadmap changed"), t["why"])     # an operator update anticipates the four-hour rhythm (the stubbed listing adds the ACTIVITY UNAVAILABLE line after it)
        self.assertIn("pause the EBP thread", sa.build_brief_p(self.campaign, sa.observe(self.campaign, sa._load_state(self.campaign))))

    def test_the_budget_stops_further_invocations_and_the_expiry_does_not_renew(self) -> None:
        for _ in range(3):
            self.assertEqual(sa.evaluate(self.campaign), 0)
        self.assertEqual(sa.evaluate(self.campaign), 2)                          # a fourth invocation is refused, the third is the last
        self.assertEqual(len({(a["stage"], a["index"]) for a in sa._attempts(self.campaign)}), 3)
        self.assertEqual(sa.tick(self.campaign)["verdict"], "BUDGET")
        sa.main(["activate", "--campaign", str(self.tmp / "p2"), "--hours", "1"])
        self.at("2026-11-13T12:00:01Z")
        self.assertEqual(sa.tick(self.tmp / "p2")["verdict"], "EXPIRED")

    def test_the_campaign_total_governs_the_stage_ceiling_when_a_budget_exists(self) -> None:
        self.assertEqual(sa.stage_limits(self.tmp / "no_budget_here")["P"], 3)                      # no budget file: the per-stage ceilings are the whole rule
        budget = self.campaign / "budget.json"; data = json.loads(budget.read_text(encoding="utf-8"))
        self.assertEqual(sa.stage_limits(self.campaign)["P"], 3)                                    # budget 3: unchanged
        data["max_invocations"] = 5; budget.write_text(json.dumps(data), encoding="utf-8")          # the operator's amendment to a total of 5
        for _ in range(5):
            self.assertEqual(sa.evaluate(self.campaign), 0)                                         # the fourth and fifth Stage P runs were refused by the stale per-stage 3
        self.assertEqual(sa.evaluate(self.campaign), 2)                                             # the total is still the ceiling
        self.assertEqual(len({(a["stage"], a["index"]) for a in sa._attempts(self.campaign)}), 5)
        self.assertEqual(sa.check(self.campaign), 0)                                                # check no longer calls five Stage P attempts a breach of the stale ceiling
        (self.campaign / "budget.json").unlink()
        self.assertEqual(sa.check(self.campaign), 1)                                                # without a budget file the same five attempts do exceed P=3

    def test_the_brief_says_what_the_turn_limit_means_with_the_campaign_value(self) -> None:
        sa.evaluate(self.campaign)
        text = (sa._state_path(self.campaign).parent / "brief_P.md").read_text(encoding="utf-8")
        self.assertIn("turn_limit is 20, a hard stop: at turn 21 the run is killed", text); self.assertIn("by turn 14 at the latest", text)
        budget = self.campaign / "budget.json"; data = json.loads(budget.read_text(encoding="utf-8")); data["turn_limit"] = 12; budget.write_text(json.dumps(data), encoding="utf-8")
        self.assertIn("turn_limit is 12, a hard stop: at turn 13", sa.turn_limit_text(self.campaign))      # the sentence follows the budget, not a constant
        data.pop("turn_limit"); budget.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(sa.turn_limit_text(self.campaign), "")                                             # no limit configured: no sentence

    def test_a_failed_attempt_counts_and_the_turn_limit_is_enforced_by_the_launcher(self) -> None:
        os.environ["FAKE_MODE"] = "many"
        self.assertEqual(sa.evaluate(self.campaign), 1)
        rows = [a for a in sa._attempts(self.campaign) if a["outcome"] != "STARTED"]
        self.assertEqual([a["outcome"] for a in rows], ["TURN_LIMIT"])           # stopped after 20 turns, counted in the budget
        self.assertEqual(len({(a["stage"], a["index"]) for a in sa._attempts(self.campaign)}), 1)

    def test_disabling_stops_the_pilot_and_nothing_else(self) -> None:
        sa.main(["disable", "--campaign", str(self.campaign)])
        self.assertEqual(sa.tick(self.campaign)["verdict"], "DISABLED")
        self.assertEqual(sa.evaluate(self.campaign), 2)
        self.assertEqual(sa.run_stage_independent_of_pilot(), 0) if hasattr(sa, "run_stage_independent_of_pilot") else None
        # the ordinary consultation in a campaign with no budget file is unchanged by any of this
        plain = self.tmp / "plain"; self.brief.write_text("# b\n", encoding="utf-8")
        self.assertEqual(sa.run("A", plain, self.brief, "opus", "high", 60, sa.LIMITS), 0)



class Continuous(Proactive):
    """HE52: continuous operation under the operator's persistent authorisation is a mode of the existing campaign. The pilot's counters, results and failures stay; the pilot's ceilings stop being the rule;
    an operator pause or stop prevails; resources stay disciplined. Fixtures: they do not show the real runtime."""

    def exhaust_the_pilot(self) -> None:
        for n in range(3):
            self.at(f"2026-11-13T{11 + 2 * n}:00:00Z")
            self.land(f"SCI5{n} record COMPLETE; package delivered")
            self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
            self.assertEqual(sa.evaluate(self.campaign), 0)

    def authorise(self, *extra: str) -> None:
        self.assertEqual(sa.main(["authorise-continuous", "--campaign", str(self.campaign), "--source", "Operator roadmap line, 2026-11-14", *extra]), 0)

    def roadmap(self, *lines: str) -> None:
        sa.ROADMAP.write_text(f"x\n{sa.ROADMAP_BEGIN}\nMission v1\n" + "\n".join(lines) + f"\n{sa.ROADMAP_END}\n", encoding="utf-8")

    def write_waiting(self, task: str, blocker: str, other_step: str = "TODO") -> None:
        rec = {"TASK_ID": task, "AUTHORISED_QUEUE_X": {"MANDATE_STATE": "OPEN", "OBJ_1": {"order": 1, "steps": [
            {"step": "use the battery result", "status": "BLOCKED", "blocker": blocker, "owner": "x"},
            {"step": "independent work", "status": other_step, "owner": "x", **({"evidence": "e1 recorded and verified"} if other_step == "DONE" else {})}]}}}
        (self.repo / f"ledger/tasks/orchestrator/{task}.json").write_text(json.dumps(rec), encoding="utf-8")

    def test_a_new_wait_is_an_event_a_standing_wait_is_not_and_the_wait_is_visible_without_an_evaluation(self) -> None:
        self.write_waiting("ORCH-W1", "battery run 77 in progress")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")                     # first tick of the campaign
        sa.evaluate(self.campaign)
        self.at("2026-11-13T15:00:00Z")
        quiet = sa.tick(self.campaign)                                                      # the same wait, still standing: nothing new
        self.assertEqual((quiet["verdict"], quiet["events"]), ("NONE", []))
        self.assertEqual(quiet["waiting_on"], ["ORCH-W1: battery run 77 in progress"])      # visible to the recall, which costs one line
        self.assertTrue(quiet["presidio"].startswith(("idle inside the pilot", "WAITING")))
        self.write_waiting("ORCH-W2", "CI run 740 in progress")
        self.at("2026-11-13T20:00:00Z")
        new = sa.tick(self.campaign)
        self.assertEqual(new["verdict"], "EVALUATE")                                         # a new wait changes what could be anticipated; grouped with the others, at the ordinary rhythm
        self.assertIn("waiting: ORCH-W2: CI run 740 in progress", new["events"])
        sa.evaluate(self.campaign)
        brief = (sa._state_path(self.campaign).parent / "brief_P.md").read_text(encoding="utf-8")
        self.assertIn('"waits"', brief); self.assertIn("CI run 740 in progress", brief); self.assertIn("battery run 77 in progress", brief)
        self.assertIn("## Waiting and follow-through", brief)
        self.assertIn("keep waiting because nothing would justify its cost or risk", brief)      # waiting stays a valid outcome
        self.assertIn("does not touch the candidate or the clones, processes and directories under verification", brief)
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")                          # reused: the same waits are not re-evaluated

    def test_the_working_brief_stays_outside_the_checkout_and_the_saved_one_keeps_the_run_reproducible(self) -> None:
        """HE56: the scheduler regenerated brief_P.md inside the shared checkout and left the tree dirty during landings."""
        sa.evaluate(self.campaign)
        self.assertFalse((self.campaign / "brief_P.md").exists())                                                        # nothing regenerated in the campaign folder of the checkout
        work = sa._state_path(self.campaign).parent / "brief_P.md"
        self.assertTrue(work.is_file())                                                                                # the working copy is with the host state
        saved = self.campaign / "P1" / "brief.md"
        self.assertEqual(saved.read_text(encoding="utf-8"), work.read_text(encoding="utf-8"))                          # the brief of the run, byte for byte, is saved with its assessment and metadata
        self.assertTrue((self.campaign / "P1" / "meta.json").is_file())

    def test_optional_follow_through_fields_travel_and_the_old_format_still_registers(self) -> None:
        text = ("### ASSIGNMENT 1\nkey: anticipated-reading-during-the-wait\nrecipient: Science\nquestion: q\nwhy_now: w\nroadmap_link: r\nrelated_work: rw\nsources: s\ndecision_changed_by_result: d\nperimeter_and_budget: p\n"
                "method_autonomy: m\ndeliver_to: Orchestrator\nduplicate_check: c\nmode: queued\nstart_condition: after the battery of ORCH-W1 concludes\ninterferes_with: nothing under verification\nobsolete_if: the battery fails\n")
        parsed = sa.parse_assignments(text)[0]
        self.assertEqual((parsed["mode"], parsed["obsolete_if"], parsed["_missing"]), ("queued", "the battery fails", ""))
        self.assertEqual(sa.parse_assignments(text.split("mode: queued")[0])[0]["_missing"], "")      # without the optional fields nothing is missing
        made = sa.register_assignments(self.campaign, "P9", text)
        self.assertEqual(len(made), 1)
        self.assertIn("start_condition: after the battery", (self.campaign / "assignments" / f"{made[0]['id']}.md").read_text(encoding="utf-8"))

    def test_the_pilots_assignment_cap_is_history_in_continuous_operation(self) -> None:
        budget = json.loads((self.campaign / "budget.json").read_text(encoding="utf-8")); budget["max_assignments"] = 1
        (self.campaign / "budget.json").write_text(json.dumps(budget), encoding="utf-8")
        mk = lambda k: ("### ASSIGNMENT 1\nkey: %s\nrecipient: Science\nquestion: q\nwhy_now: w\nroadmap_link: r\nrelated_work: rw\nsources: s\ndecision_changed_by_result: d\nperimeter_and_budget: p\n"
                        "method_autonomy: m\ndeliver_to: Orchestrator\nduplicate_check: c\n") % k
        self.assertEqual(len(sa.register_assignments(self.campaign, "P1", mk("one"))), 1)
        self.assertEqual(len(sa.register_assignments(self.campaign, "P2", mk("two"))), 0)       # bounded pilot: over budget
        self.authorise()
        self.assertEqual(len(sa.register_assignments(self.campaign, "P3", mk("three"))), 1)     # continuous: no cap

    def test_the_pilot_ends_at_its_ceilings_and_continuous_mode_continues_without_resetting_anything(self) -> None:
        self.exhaust_the_pilot()
        self.land("SCI60 record COMPLETE; delivered"); self.at("2026-11-13T18:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "BUDGET")              # the bounded pilot keeps its own limits
        budget_before = (self.campaign / "budget.json").read_text(encoding="utf-8")
        rows_before = (self.campaign / "invocations.jsonl").read_text(encoding="utf-8")
        self.authorise()
        t = sa.tick(self.campaign)
        self.assertEqual((t["verdict"], t["mode"]), ("EVALUATE", "continuous"))
        self.assertEqual(sa.evaluate(self.campaign), 0)
        self.assertEqual((self.campaign / "budget.json").read_text(encoding="utf-8"), budget_before)          # no reset, no renewal, no bigger number
        self.assertTrue((self.campaign / "invocations.jsonl").read_text(encoding="utf-8").startswith(rows_before))   # the history is kept row for row
        self.assertEqual(len({(a["stage"], a["index"]) for a in sa._attempts(self.campaign)}), 4)
        data = json.loads((self.campaign / sa.CONTINUOUS).read_text(encoding="utf-8"))
        self.assertEqual((data["pilot_at_authorisation"]["invocations_executed"], data["pilot_at_authorisation"]["max_invocations"]), (3, 3))
        st = sa.status(self.campaign)
        self.assertIn("pilot invocations 4/3", st); self.assertIn("CONTINUOUS", st); self.assertIn("are history, not the rule", st)   # ceilings and executed activity are told apart
        self.assertEqual(sa.main(["check", "--campaign", str(self.campaign)]), 0)

    def test_the_pilot_expiry_does_not_stop_continuous_operation_and_removing_the_mode_restores_it(self) -> None:
        self.at("2026-12-01T10:00:00Z")                                                 # the fixture's pilot was activated at the real clock: a month later it has expired
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EXPIRED")
        self.authorise()
        self.land("SCI61 record COMPLETE; delivered"); self.at("2026-12-01T11:30:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        sa.main(["end-continuous", "--campaign", str(self.campaign), "--reason", "operator ended it"])
        self.assertTrue((self.campaign / sa.CONTINUOUS).exists())                    # history kept
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EXPIRED")

    def test_an_assignment_that_ends_does_not_end_the_presidio_and_a_quiet_wait_says_what_it_is(self) -> None:
        self.authorise()
        sa.evaluate(self.campaign)
        self.at("2026-11-13T12:00:00Z")
        quiet = sa.tick(self.campaign)
        self.assertEqual(quiet["verdict"], "NONE")
        self.assertTrue(quiet["presidio"].startswith("WAITING (legitimate)"))
        self.assertNotIn("PILOT ENDED", quiet["presidio"])
        # The recall routes the current policy; it no longer certifies that every
        # mechanical NONE/DEFERRED means the whole portfolio should wait.

    def test_operator_pause_and_stop_in_the_roadmap_prevail_and_resume_lifts_them(self) -> None:
        self.authorise()
        self.roadmap("PAUSE: advisor \u2014 the operator asked for a pause")
        held = sa.tick(self.campaign)
        self.assertEqual(held["verdict"], "PAUSED")
        self.assertTrue(held["presidio"].startswith("SUSPENDED by the operator"))
        self.assertEqual(sa.evaluate(self.campaign), 2)                              # the launcher refuses as well, not only the tick
        self.assertEqual(len(sa._attempts(self.campaign)), 0)
        self.roadmap("PAUSE: advisor \u2014 the operator asked for a pause", "RESUME: advisor")
        self.assertNotEqual(sa.tick(self.campaign)["verdict"], "PAUSED")
        self.roadmap("STOP: all", "URGENT: look at the AMPA contradiction first")
        t = sa.tick(self.campaign)
        self.assertEqual(t["verdict"], "PAUSED"); self.assertIn("URGENT: look at the AMPA contradiction first", t["operator_controls"])
        self.roadmap("STOP: all", "RESUME: all")
        self.assertNotEqual(sa.tick(self.campaign)["verdict"], "PAUSED")

    def test_a_pause_for_another_perimeter_is_reported_and_not_applied_and_the_disable_flag_still_wins(self) -> None:
        self.authorise()
        self.roadmap("PAUSE: science \u2014 hold the SCI reading packages")
        t = sa.tick(self.campaign)
        self.assertNotEqual(t["verdict"], "PAUSED")
        self.assertIn("PAUSE: science \u2014 hold the SCI reading packages", t["operator_controls"])      # the evaluation still sees it
        sa.evaluate(self.campaign)
        self.assertIn("PAUSE: science", (sa._state_path(self.campaign).parent / "brief_P.md").read_text(encoding="utf-8"))
        sa.main(["disable", "--campaign", str(self.campaign)])
        self.assertEqual(sa.tick(self.campaign)["verdict"], "DISABLED")

    def test_the_shared_weekly_allocation_blocks_only_when_the_operator_stated_it_and_the_use_is_measured(self) -> None:
        self.authorise()
        meta = self.campaign / "P1" / "meta.json"; meta.parent.mkdir()
        meta.write_text(json.dumps({"started_utc": "2026-11-12T10:00:00Z", "runtime_readback": {"census": {"totals": {"output": 30000, "cache_read": 900000}}}}), encoding="utf-8")
        self.assertEqual(sa.weekly_state(self.campaign)["state"], "unset")               # no value is assumed and nothing is blocked
        self.assertEqual(sa.budget_refusal(self.campaign), "")
        self.assertIn("not exposed by the runtime", sa.status(self.campaign))
        self.assertEqual(sa.weekly_state(self.campaign)["measured_7d"], {"evaluations": 1, "output_tokens": 30000, "cache_read_tokens": 900000})
        self.authorise("--weekly-limit", "100000", "--advisor-share", "0.25", "--unit", "output_tokens")       # cap 25,000: 30,000 measured
        self.assertEqual(sa.weekly_state(self.campaign)["state"], "exhausted")
        self.at("2026-11-13T12:00:00Z"); self.land("SCI62 record COMPLETE; delivered")
        t = sa.tick(self.campaign)
        self.assertEqual(t["verdict"], "RESOURCES"); self.assertIn("checkpoint, verify and deliver open work, no widening", t["why"])
        self.assertEqual(sa.evaluate(self.campaign), 2)
        self.authorise("--weekly-limit", "400000", "--advisor-share", "0.25", "--unit", "output_tokens")       # cap 100,000: 30,000 measured
        self.assertEqual(sa.weekly_state(self.campaign)["state"], "ok")
        self.assertEqual(json.loads((self.campaign / sa.CONTINUOUS).read_text(encoding="utf-8"))["authorised_utc"], "2026-11-13T12:00:00Z".replace("12", "10", 1))   # re-running keeps the original date
        old = {"started_utc": "2026-11-01T10:00:00Z", "runtime_readback": {"census": {"totals": {"output": 10**9}}}}
        (self.campaign / "P2").mkdir(); (self.campaign / "P2" / "meta.json").write_text(json.dumps(old), encoding="utf-8")
        self.assertEqual(sa.weekly_state(self.campaign)["measured_7d"]["output_tokens"], 30000)           # only the last seven days count

    def test_continuous_mode_needs_an_existing_campaign_and_a_stated_limit_needs_its_share_and_unit(self) -> None:
        (self.campaign / "budget.json").unlink()
        self.assertEqual(sa.main(["authorise-continuous", "--campaign", str(self.campaign), "--source", "x"]), 2)
        sa.main(["activate", "--campaign", str(self.campaign)])
        self.assertEqual(sa.main(["authorise-continuous", "--campaign", str(self.campaign), "--source", "x", "--weekly-limit", "5"]), 2)
        self.assertFalse((self.campaign / sa.CONTINUOUS).exists())

    def test_evaluation_usage_is_never_presented_as_the_whole_laboratory_cost(self) -> None:
        self.authorise()
        meta = self.campaign / "P1" / "meta.json"
        meta.parent.mkdir()
        meta.write_text(json.dumps({"started_utc": "2026-11-13T10:00:00Z",
            "runtime_readback": {"census": {"totals": {"output": 123, "cache_read": 456}}}}))
        before = sa._attempts(self.campaign)
        for allocated in (False, True):
            if allocated:
                self.authorise("--weekly-limit", "100000", "--advisor-share", "0.25", "--unit", "output_tokens")
            week = sa.weekly_state(self.campaign)
            self.assertEqual(week["measured_7d"], {"evaluations": 1, "output_tokens": 123, "cache_read_tokens": 456})
            for text in (week["measurement_scope"], sa.operating_mode_text(self.campaign), sa.status(self.campaign)):
                self.assertIn("excludes the ADV hosting session", text)
                self.assertIn("Unmeasured work is not zero-cost", text)
                self.assertIn("remaining account quota", text)
            if allocated:
                self.assertEqual(week["advisor_spent"], 123)
                self.assertEqual(week["advisor_cap"], 25000)
            else:
                self.assertEqual(week["state"], "unset")
        self.assertEqual(sa._attempts(self.campaign), before, "scope disclosure does not launch a model or renew a budget")


    # ---- HE64: a hold recorded by the host, without a model run -------------------------------------------------------------------------------------------------------------------------------

    def held_campaign(self) -> None:
        """A continuous campaign with one evaluation behind it and one unevaluated delivery pending: the state in which the real tick re-fired EVALUATE at every recall."""
        self.authorise()
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        self.assertEqual(sa.evaluate(self.campaign), 0)
        self.at("2026-11-13T16:00:00Z")
        self.land("SCI70 record COMPLETE; package delivered")

    def test_without_a_hold_the_same_pending_digest_re_fires_every_tick(self) -> None:
        """The measured obstacle (2026-11-15, a copy of the real state): no evaluation completes, so last_digest never moves and every hourly tick says EVALUATE."""
        self.held_campaign()
        first = sa.tick(self.campaign)
        self.at("2026-11-13T17:00:00Z")
        second = sa.tick(self.campaign)
        self.assertEqual((first["verdict"], second["verdict"]), ("EVALUATE", "EVALUATE"))
        self.assertEqual(first["digest"], second["digest"])

    def test_a_hold_consumes_what_it_lists_and_is_not_an_evaluation(self) -> None:
        self.held_campaign()
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        attempts, last_eval = len(sa._attempts(self.campaign)), sa._load_state(self.campaign)["last_evaluation_utc"]
        meeting = sa._state_path(self.campaign).with_name("meeting.json")
        meeting_before = meeting.read_bytes() if meeting.exists() else None
        self.at("2026-11-13T17:00:00Z")
        self.assertEqual(sa.main(["hold", "--campaign", str(self.campaign), "--reason", "both intakes blocked, queue exhausted", "--resume-when", "record:ORCH-A=COMPLETE", "--excluded", EXCL]), 0)
        rows = [json.loads(line) for line in (self.campaign / "holds.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(rows), 1)
        self.assertTrue(any("SCI70 record COMPLETE" in e for e in rows[0]["events_cleared"]), rows[0])        # nothing silently discarded: the cleared events are in the record
        self.assertGreaterEqual(rows[0]["commits_cleared"], 1)
        self.assertEqual((rows[0]["reason"], rows[0]["resume_when"]), ("both intakes blocked, queue exhausted", "record:ORCH-A=COMPLETE"))
        self.at("2026-11-13T18:00:00Z")
        quiet = sa.tick(self.campaign)
        self.assertEqual((quiet["verdict"], quiet["events"]), ("NONE", []))
        self.assertTrue(quiet["presidio"].startswith("HELD by host at 2026-11-13T17:00:00Z: both intakes blocked"), quiet["presidio"])
        self.assertIn("resume_when record:ORCH-A=COMPLETE", quiet["presidio"])
        self.assertEqual(len(sa._attempts(self.campaign)), attempts)                                          # no invocation, no P<n>, no budget
        self.assertEqual(sa._load_state(self.campaign)["last_evaluation_utc"], last_eval)                     # the evaluation clock is untouched
        self.assertEqual(sa._load_state(self.campaign)["last_outcome"]["evaluation"], "HOLD")
        self.assertIn("holds recorded 1 (not evaluations", sa.status(self.campaign))
        self.assertEqual(meeting.read_bytes() if meeting.exists() else None, meeting_before)                  # the meeting cache is not touched

    def test_a_new_event_after_a_hold_re_fires_within_the_hour(self) -> None:
        self.held_campaign()
        self.at("2026-11-13T17:00:00Z")
        self.assertEqual(sa.main(["hold", "--campaign", str(self.campaign), "--reason", "waiting for the intake record", "--resume-when", "record:ORCH-A=COMPLETE", "--excluded", EXCL]), 0)
        self.at("2026-11-13T17:30:00Z")
        self.land("SCI71 record COMPLETE; package delivered")
        new = sa.tick(self.campaign)
        self.assertEqual(new["verdict"], "EVALUATE")
        self.assertEqual([e for e in new["events"] if e.startswith("delivery:")], [e for e in new["events"] if "SCI71" in e])     # only the new delivery, not the cleared one
        self.assertFalse(any("SCI70" in e for e in new["events"]))

    def test_a_hold_ends_at_its_resume_condition(self) -> None:
        self.held_campaign()
        self.at("2026-11-13T17:00:00Z")
        self.assertEqual(sa.main(["hold", "--campaign", str(self.campaign), "--reason", "waiting for ORCH-A", "--resume-when", "record:ORCH-A=COMPLETE", "--excluded", EXCL]), 0)
        self.at("2026-11-13T20:00:00Z")                                                                       # three hours after the hold: still inside min_hours_between
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        (self.repo / "ledger/tasks/orchestrator/ORCH-A.json").write_text(json.dumps(_record("ORCH-A", "COMPLETE")), encoding="utf-8")
        self.at("2026-11-13T23:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")

    def test_a_hold_is_refused_without_a_reason_an_external_form_a_pending_event_or_while_an_evaluation_runs(self) -> None:
        def attempt(reason: str, resume: str) -> int:
            with patch("sys.stderr", new=__import__("io").StringIO()):
                return sa.main(["hold", "--campaign", str(self.campaign), "--reason", reason, "--resume-when", resume, "--excluded", EXCL])
        self.authorise()
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        sa.evaluate(self.campaign)
        self.at("2026-11-13T16:00:00Z")
        self.assertEqual(attempt("quiet", "record:ORCH-A=COMPLETE"), 2)                                       # nothing pending: nothing to hold
        self.land("SCI72 record COMPLETE; package delivered")
        self.assertEqual(attempt("  ", "record:ORCH-A=COMPLETE"), 2)                                         # no reason
        self.assertEqual(attempt("r", "after:2026-11-14T00:00:00Z"), 2)                                       # a time alone would make a hold a timer for silence
        self.assertEqual(attempt("r", "event"), 2)
        self.assertEqual(attempt("r", "nonsense"), 2)
        self.assertEqual(attempt("r", "record:ORCH-NOT-THERE=COMPLETE"), 2)                                   # a record that does not exist would never resume
        state = sa._load_state(self.campaign); state["running"] = sa._pid_identity(os.getpid()); sa._save_state(self.campaign, state)
        self.assertEqual(attempt("r", "record:ORCH-A=COMPLETE"), 2)                                           # an evaluation is running
        self.assertFalse((self.campaign / "holds.jsonl").exists(), "every refusal must leave no record")
        state["running"] = ""; sa._save_state(self.campaign, state)
        self.assertEqual(attempt("r", "path:disease-models/wwox/research/drug_repurposing/roadmap_current.md~Mission v2"), 0)   # a named path with text is an external form

    def test_the_test_never_touches_the_real_campaign_state(self) -> None:
        self.assertTrue(str(sa.STATE_DIR).startswith(str(self.tmp)), sa.STATE_DIR)
        real = Path.home() / ".local/state/legend/advisor_pilot"
        before = sorted((p.as_posix(), p.stat().st_mtime_ns) for p in real.rglob("*") if p.is_file()) if real.exists() else []
        self.held_campaign()
        self.at("2026-11-13T17:00:00Z")
        sa.main(["hold", "--campaign", str(self.campaign), "--reason", "r", "--resume-when", "record:ORCH-A=COMPLETE", "--excluded", EXCL])
        after = sorted((p.as_posix(), p.stat().st_mtime_ns) for p in real.rglob("*") if p.is_file()) if real.exists() else []
        self.assertEqual(before, after)


class ValueContinuity(Continuous):
    """HE57: the end of the executable queue is a moment to choose what comes next, not to wait for an event. A wait states what it excluded and when it resumes; the same situation is not evaluated twice;
    the advisor's own updates are not news. Fixtures: they do not show that a model writes the outcome block or ranks well."""

    WAIT = "outcome: wait|excluded: continue the lever thread (no new result); a Harness refactor (cost above its benefit now)|reason: every open question waits on a recipient's reading|resume_when: %s"

    def evaluate_with(self, block: str) -> None:
        os.environ["FAKE_OUTCOME"] = block
        try:
            self.assertEqual(sa.evaluate(self.campaign), 0)
        finally:
            os.environ.pop("FAKE_OUTCOME", None)

    def legacy(self) -> None:
        st = sa._load_state(self.campaign)
        st.pop("last_outcome", None); st.pop("unstated_streak", None)
        sa._save_state(self.campaign, st)

    def complete(self, task: str) -> None:
        (self.repo / f"ledger/tasks/orchestrator/{task}.json").write_text(json.dumps(_record(task, "COMPLETE")), encoding="utf-8")

    def started(self) -> None:
        self.authorise()
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        sa.evaluate(self.campaign)

    def test_an_exhausted_queue_with_no_radar_and_no_event_still_gets_one_decision_on_what_is_next(self) -> None:
        self.started(); self.legacy()                                       # an evaluation made before the outcome existed
        self.complete("ORCH-A")
        self.at("2026-11-13T11:30:00Z")
        closing = sa.tick(self.campaign)                                    # the closure itself is observed ...
        self.assertEqual(closing["verdict"], "EVALUATE"); self.assertTrue(closing["queue"]["exhausted"])
        sa.evaluate(self.campaign); self.legacy()  # consume the closure, then simulate an old run without an outcome
        self.at("2026-11-13T16:00:00Z")                                     # no unconsumed event, radar or instruction
        idle = sa.tick(self.campaign)
        self.assertEqual(idle["verdict"], "EVALUATE")
        self.assertIn("no executable work remains: decide what is next from the portfolio", idle["why"])
        sa.evaluate(self.campaign)
        brief = (sa._state_path(self.campaign).parent / "brief_P.md").read_text(encoding="utf-8")
        self.assertIn("## Portfolio selection", brief); self.assertIn('"exhausted": true', brief)
        self.assertIn("## Outcome", brief); self.assertIn("without it the wait is not motivated", brief)
        self.assertIn("Do not repeat an evaluation that is still valid", brief)

    def test_that_decision_is_asked_once_and_the_same_situation_is_not_evaluated_again(self) -> None:
        self.started(); self.legacy(); self.complete("ORCH-A")
        self.at("2026-11-13T11:30:00Z"); sa.tick(self.campaign)
        self.at("2026-11-13T16:00:00Z"); self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        sa.evaluate(self.campaign)                                          # the stand-in model writes no outcome block
        self.assertEqual(sa._load_state(self.campaign)["unstated_streak"], 1)
        self.at("2026-11-13T23:00:00Z")
        again = sa.tick(self.campaign)
        self.assertEqual(again["verdict"], "NONE")                          # no second costly evaluation of the same situation
        self.assertTrue(again["presidio"].startswith("IDLE without a stated outcome")); self.assertIn("not asked again", again["presidio"])

    def test_a_stated_wait_is_motivated_visible_and_not_re_evaluated_while_nothing_changed(self) -> None:
        self.started(); self.complete("ORCH-A")
        self.write_waiting("ORCH-W", "battery run 77 in progress", other_step="DONE")
        self.at("2026-11-13T12:00:00Z"); self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        self.evaluate_with(self.WAIT % "record:ORCH-W=COMPLETE")
        self.at("2026-11-13T20:00:00Z")
        quiet = sa.tick(self.campaign)
        self.assertEqual(quiet["verdict"], "NONE")
        self.assertTrue(quiet["queue"]["exhausted"]); self.assertEqual(quiet["queue"]["blocked_only"], ["ORCH-W"])
        self.assertTrue(quiet["presidio"].startswith("WAITING (motivated)"))
        for part in ("every open question waits on a recipient's reading", "a Harness refactor", "record:ORCH-W=COMPLETE"):
            self.assertIn(part, quiet["presidio"])                          # the excluded alternatives, the reason and the resume condition are on the one line the recall reads

    def test_a_met_resume_condition_a_passed_time_or_a_new_result_reconsiders_the_choice(self) -> None:
        self.started(); self.complete("ORCH-A")
        self.write_waiting("ORCH-W", "battery run 77 in progress", other_step="DONE")
        self.at("2026-11-13T12:00:00Z"); sa.tick(self.campaign)
        self.evaluate_with(self.WAIT % "record:ORCH-W=COMPLETE")
        self.at("2026-11-13T14:00:00Z"); self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        self.complete("ORCH-W")                                             # what the wait rested on arrived (the transition is also an event; the resume reason is shown first only when no event is)
        self.at("2026-11-13T15:00:00Z")
        met = sa.tick(self.campaign)
        self.assertEqual(met["verdict"], "EVALUATE")
        self.evaluate_with(self.WAIT % "after:2026-11-13T20:00:00Z")
        self.at("2026-11-13T19:00:00Z"); self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        self.at("2026-11-13T21:00:00Z")
        late = sa.tick(self.campaign)
        self.assertEqual(late["verdict"], "EVALUATE"); self.assertIn("resume condition", late["why"])
        self.evaluate_with(self.WAIT % "event")
        self.land("SCI52 record COMPLETE; package delivered")               # a new pertinent result arrives during a stated wait
        self.at("2026-11-13T23:00:00Z")
        new = sa.tick(self.campaign)
        self.assertEqual(new["verdict"], "EVALUATE"); self.assertTrue(any(e.startswith("delivery:") for e in new["events"]))

    def test_a_wait_that_is_over_the_moment_it_is_stated_or_names_an_unreadable_condition_cannot_loop(self) -> None:
        self.started(); self.complete("ORCH-A")
        self.at("2026-11-13T12:00:00Z"); sa.tick(self.campaign)
        self.evaluate_with(self.WAIT % "after:2026-11-13T09:00:00Z")        # already past
        out = sa._load_state(self.campaign)["last_outcome"]
        self.assertEqual(out["resume_when"], "event"); self.assertIn("already met", out["problem"])
        self.at("2026-11-13T18:00:00Z"); self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        self.evaluate_with(self.WAIT % "when the weather is better")
        self.assertIn("not one of event", sa._load_state(self.campaign)["last_outcome"]["problem"])
        self.at("2026-11-13T22:00:00Z"); self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")

    def test_a_resume_on_a_record_that_does_not_exist_cannot_strand_the_wait_and_other_outcomes_ignore_resume_when(self) -> None:
        self.started(); self.complete("ORCH-A")
        self.at("2026-11-13T12:00:00Z"); sa.tick(self.campaign)
        self.evaluate_with(self.WAIT % "record:ORCH-NOT-YET-CREATED=COMPLETE")
        out = sa._load_state(self.campaign)["last_outcome"]
        self.assertEqual(out["resume_when"], "event"); self.assertIn("does not exist", out["problem"])
        self.evaluate_with("outcome: assign|resume_when: record:ORCH-NOT-YET-CREATED=COMPLETE")        # P8: not a wait, so the id is never read
        self.at("2026-11-13T14:00:00Z")  # before the separate ordinary next-choice cadence
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        brief = (sa._state_path(self.campaign).parent / "brief_P.md").read_text(encoding="utf-8")
        self.assertIn("read only for a wait", brief)

    def test_a_wait_without_its_alternatives_or_reason_is_not_a_stated_outcome(self) -> None:
        got = sa.parse_outcome("## Outcome\noutcome: wait\nreason: nothing to do\nresume_when: event\n")
        self.assertFalse(got["stated"]); self.assertIn("must say what it excluded", got["problem"])
        for kind in ("continue", "switch", "assign", "queue"):
            self.assertTrue(sa.parse_outcome(f"## Outcome\noutcome: {kind}\n")["stated"])
        self.assertFalse(sa.parse_outcome("## Outcome\noutcome: rest\n")["stated"])

    def test_the_pilot_without_the_continuous_mode_does_not_gain_idle_evaluations(self) -> None:
        sa.tick(self.campaign); sa.evaluate(self.campaign); self.legacy(); self.complete("ORCH-A")
        self.at("2026-11-13T11:30:00Z"); sa.tick(self.campaign); sa.evaluate(self.campaign)
        self.at("2026-11-13T18:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")

    def test_the_advisors_own_updates_and_the_senders_records_are_not_news_but_a_recipients_result_is(self) -> None:
        inside = self.repo / "disease-models/wwox/research/drug_repurposing/advisor_x"
        (inside / "P1").mkdir(parents=True); (inside / "assignments").mkdir()
        (self.repo / "ledger/tasks/orchestrator/ORCH-ADV-FOLLOWTHROUGH-X.json").write_text(json.dumps(_record("ORCH-ADV-FOLLOWTHROUGH-X", "OPEN")), encoding="utf-8")
        specs = sa._own_updates(inside)
        self.assertTrue(any("P[0-9]*" in x for x in specs)); self.assertTrue(any("ADV-FOLLOWTHROUGH" in x for x in specs))
        state = {"main_sha": sa._git("rev-parse", "main")}
        env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}

        def commit(rel: str, subject: str) -> None:
            (self.repo / rel).write_text(subject, encoding="utf-8")
            for cmd in (["git", "add", "."], ["git", "commit", "-q", "-m", subject]):
                subprocess.run(cmd, cwd=self.repo, check=True, capture_output=True, env=env)
        base = "disease-models/wwox/research/drug_repurposing/advisor_x"
        commit(f"{base}/P1/assessment.md", "ADV evaluation recorded; lever thread closed")
        commit(f"{base}/assignments/ADV-001.md", "ADV draft delivered")
        commit("ledger/tasks/orchestrator/ORCH-ADV-FOLLOWTHROUGH-X.json", "ADV record COMPLETE")
        self.assertEqual(sa.observe(inside, state)["events"], [])           # three commits that match the delivery pattern, all the advisor's own
        (self.repo / "disease-models/wwox/research/drug_repurposing/deepening_adv_x").mkdir(parents=True, exist_ok=True)
        commit("disease-models/wwox/research/drug_repurposing/research_portfolio.tsv", "ADV: evaluation P9 recorded (assign; delivered to IT)")
        commit("disease-models/wwox/research/drug_repurposing/deepening_adv_x/IDEAS_ORDER_DREAM5_ADV.md", "ADV: DREAM-5 update (R4 consumed)")
        self.assertEqual([e for e in sa.observe(inside, state)["events"] if e.startswith("delivery:")], [])   # HE95: the portfolio update and the DREAM note an evaluation leaves are the advisor's own too
        commit(f"{base}/ADV-002_result.md", "HE result delivered")
        self.assertEqual(len([e for e in sa.observe(inside, state)["events"] if e.startswith("delivery:")]), 1)
        commit(f"{base}/ADV-003_brief.md", "ADV: evaluation P10 recorded (delivered); brief file touched")
        self.assertEqual(len([e for e in sa.observe(inside, state)["events"] if e.startswith("delivery:")]), 2)   # a commit that also touches a file outside the advisor's own still counts
        # ADV-180 (2026-11-22): the advisor's own hold log is not a delivery either; a hold beside a recipient's result in one commit still is
        self.assertTrue(any(x.endswith("/holds.jsonl") and x.startswith(":(exclude)") for x in specs))
        commit(f"{base}/holds.jsonl", "ADV: EVALUATE closed by a recorded hold; delivered nothing")
        self.assertEqual(len([e for e in sa.observe(inside, state)["events"] if e.startswith("delivery:")]), 2)   # a hold-only commit adds no delivery
        (self.repo / f"{base}/holds.jsonl").write_text("second hold", encoding="utf-8"); (self.repo / f"{base}/ADV-004_result.md").write_text("SCI result", encoding="utf-8")
        for cmd in (["git", "add", "."], ["git", "commit", "-q", "-m", "ADV: hold recorded; SCI result delivered"]):
            subprocess.run(cmd, cwd=self.repo, check=True, capture_output=True, env=env)
        self.assertEqual(len([e for e in sa.observe(inside, state)["events"] if e.startswith("delivery:")]), 3)   # the mixed commit stays actionable

    def test_the_assignment_render_names_each_mandate_once_and_loses_no_field(self) -> None:
        """HE95: the compact render keeps every assignment's recipient, key, origin, evidence level and mandates, and each mandate's verdict and path once."""
        states = {"ADV-001": {"recipient": "Science", "key": "k1", "origin": "assessment", "highest": "EXECUTED",
                              "mandates": [{"task": "T-A", "verdict": "RELEASED", "path": "ledger/tasks/plan/T-A.json"}, {"task": "T-B", "verdict": "OPEN", "path": "ledger/tasks/plan/T-B.json"}]},
                  "ADV-002": {"recipient": "Harness", "key": "k2", "highest": "SENT", "mandates": [{"task": "T-A", "verdict": "RELEASED", "path": "ledger/tasks/plan/T-A.json"}]}}
        text = sa.render_assignment_states(states)
        for needle in ("ADV-001", "ADV-002", "Science", "Harness", "k1", "k2", "EXECUTED", "SENT", "T-A", "T-B", "RELEASED", "OPEN", "ledger/tasks/plan/T-A.json", "ledger/tasks/plan/T-B.json"):
            self.assertIn(needle, text)
        self.assertEqual(text.count("ledger/tasks/plan/T-A.json"), 1)         # named once, referenced by id under each assignment
        self.assertIn('"origin": "assessment"', text)                           # an absent origin reads as assessment, as before
        self.assertEqual(sa.render_assignment_states({}), "none")

    def test_session_activity_shows_who_is_idle_and_for_how_long(self) -> None:
        """HE60: the idle share and each session's quiet time come from the runtime and the transcript mtime, only for this repository's sessions."""
        proj = self.tmp / "projects" / "-x"
        proj.mkdir(parents=True)
        now = sa._now()
        for sid, minutes in (("s-it", 47), ("s-sci", 3), ("s-old", 3000)):
            f = proj / f"{sid}.jsonl"
            f.write_text("{}\n", encoding="utf-8")
            os.utime(f, (now.timestamp() - minutes * 60,) * 2)
        agents = [{"name": "IT", "status": "idle", "cwd": str(sa.ROOT), "sessionId": "s-it"},
                  {"name": "SCI", "status": "busy", "cwd": str(sa.ROOT) + "/.claude/worktrees/w", "sessionId": "s-sci"},
                  {"name": "old", "status": "idle", "cwd": str(sa.ROOT), "sessionId": "s-old"},
                  {"name": "elsewhere", "status": "idle", "cwd": "/home/other", "sessionId": "s-it"},
                  {"name": "nofile", "status": "idle", "cwd": str(sa.ROOT), "sessionId": "s-missing"}]
        saved = sa.PROJECTS_DIR
        sa.PROJECTS_DIR = self.tmp / "projects"
        self.addCleanup(setattr, sa, "PROJECTS_DIR", saved)
        act = sa.session_activity(now, agents)
        self.assertEqual(set(act["sessions"]), {"IT", "SCI", "old", "nofile"})      # another repository's session is not counted
        self.assertEqual((act["sessions"]["IT"]["quiet_min"], act["sessions"]["SCI"]["quiet_min"]), (47, 3))
        self.assertEqual(act["sessions"]["old"]["quiet_min"], 3000)                  # a stale session shows as stale
        self.assertIsNone(act["sessions"]["nofile"]["quiet_min"])
        self.assertEqual(act["idle_share"], "1/2")                                   # the stale and the unfound session are listed, not counted
        self.assertFalse(act["idle_over_half"])
        self.assertTrue(sa.session_activity(now, [agents[0], dict(agents[0], name="IT2")])["idle_over_half"])
        self.assertFalse(sa.session_activity(now, [])["available"])                 # no list from the runtime: said, not guessed

    def test_local_commits_the_remote_does_not_hold_are_counted_with_their_age(self) -> None:
        """HE62: 'the awaited event exists locally' is visible without a fetch; the figure is relative to the last fetched remote ref and says how old that fetch is."""
        remote, clone = self.tmp / "remote.git", self.tmp / "clone"
        run = lambda *a, cwd=clone: subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True, text=True)
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(remote)], check=True)
        subprocess.run(["git", "clone", "-q", str(remote), str(clone)], check=True, capture_output=True)
        run("config", "user.email", "t" + chr(64) + "example.org"); run("config", "user.name", "t")
        run("remote", "rename", "origin", "development")
        for n, when in (("a", "2026-11-15T10:00:00+00:00"), ("b", "2026-11-15T11:00:00+00:00")):
            (clone / n).write_text(n, encoding="utf-8"); run("add", n)
            subprocess.run(["git", "commit", "-q", "-m", n], cwd=clone, check=True, env={**os.environ, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when})
        run("push", "-q", "development", "main"); run("fetch", "-q", "development")
        for n, when in (("c", "2026-11-15T12:00:00+00:00"), ("d", "2026-11-15T13:00:00+00:00")):          # two local commits the remote does not hold
            (clone / n).write_text(n, encoding="utf-8"); run("add", n)
            subprocess.run(["git", "commit", "-q", "-m", n], cwd=clone, check=True, env={**os.environ, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when})
        saved = sa.ROOT
        sa.ROOT = clone
        try:
            now = dt.datetime(2026, 11, 15, 14, 0, tzinfo=dt.timezone.utc)
            got = sa.unpublished_main(now)
            self.assertEqual((got["against"], got["commits"], got["oldest_min"]), ("development/main", 2, 120))
            self.assertIsNotNone(got["ref_checked_min_ago"])
            run("push", "-q", "development", "main"); run("fetch", "-q", "development")
            self.assertEqual((sa.unpublished_main(now)["commits"], sa.unpublished_main(now)["oldest_min"]), (0, None))
            run("remote", "remove", "development")
            self.assertFalse(sa.unpublished_main(now)["available"])                                      # no remote ref offline: said, not guessed
        finally:
            sa.ROOT = saved

    def test_the_tick_carries_the_activity_block(self) -> None:
        sa.session_activity_saved = sa.session_activity
        sa.session_activity = lambda now, agents=None, recipients=None: {"available": True, "idle_share": "0/0", "idle_over_half": False, "main_quiet_min": 5}
        try:
            out = sa.tick(self.campaign)
        finally:
            sa.session_activity = sa.session_activity_saved
        self.assertEqual(out["activity"]["main_quiet_min"], 5)

    def test_an_unavailable_activity_block_is_said_on_the_tick_line_not_omitted(self) -> None:
        """2026-11-19 (ADV): the block was silently absent when the listing failed; the tick now names it."""
        saved = sa.session_activity
        sa.session_activity = lambda now, agents=None, recipients=None: {"available": False}
        try:
            out = sa.tick(self.campaign)
        finally:
            sa.session_activity = saved
        self.assertIn("ACTIVITY UNAVAILABLE", out["why"])
        sa.session_activity = lambda now, agents=None, recipients=None: {"available": True, "idle_share": "0/0", "idle_over_half": False, "main_quiet_min": 5}
        try:
            self.assertNotIn("ACTIVITY UNAVAILABLE", sa.tick(self.campaign)["why"])
        finally:
            sa.session_activity = saved

    def test_a_run_cut_short_by_a_fallback_is_not_acted_on(self) -> None:
        """HE59: P11 was stopped by a classifier after 4 calls and its portfolio updates and wait were applied. A short run with a recorded fallback takes nothing; a long one with the same fallback is used."""
        self.started()
        os.environ["FAKE_MODE"] = "fallback"
        os.environ["FAKE_PORTFOLIO"] = json.dumps({"id": "RP-001", "status": "in flight"})
        try:
            self.evaluate_with(self.WAIT)
            st = sa._load_state(self.campaign)
            self.assertIn("refusal fallback", st["last_incomplete"]["reason"])
            self.assertNotEqual(st["last_outcome"]["evaluation"], st["last_incomplete"]["evaluation"])        # the incomplete run took no outcome; the earlier one stands
            self.assertEqual(sa.tick(self.campaign)["last_incomplete"]["evaluation"], st["last_incomplete"]["evaluation"])
            os.environ["FAKE_CALLS"] = str(sa.MIN_CALLS_AFTER_FALLBACK)
            self.evaluate_with(self.WAIT)
            st = sa._load_state(self.campaign)
            self.assertEqual(st["last_incomplete"], {})
            self.assertTrue(st["last_outcome"]["stated"])
        finally:
            for k in ("FAKE_MODE", "FAKE_PORTFOLIO", "FAKE_CALLS"):
                os.environ.pop(k, None)

    def test_a_legacy_incomplete_wait_is_superseded_without_rewriting_history(self) -> None:
        self.started(); self.complete("ORCH-A")
        folder = self.campaign / "P99"
        folder.mkdir()
        original = "## Outcome\noutcome: wait\nexcluded: other branches\nreason: review later\nresume_when: after:2026-11-14T20:00:00Z\n"
        (folder / "assessment.md").write_text(original)
        (folder / "meta.json").write_text(json.dumps({"runtime_readback": {"refusal_fallbacks": [{"trigger": "refusal"}]}, "tool_calls": [{"name": "Read"}] * 4}))
        state = sa._load_state(self.campaign)
        state["last_outcome"] = {**sa.parse_outcome(original), "evaluation": "P99"}
        sa._save_state(self.campaign, state)
        self.at("2026-11-13T10:15:00Z")
        tick = sa.tick(self.campaign)
        self.assertEqual(tick["verdict"], "EVALUATE")
        self.assertIn("incomplete", tick["why"])
        saved = sa._load_state(self.campaign)
        self.assertEqual(saved["last_outcome"], {})
        self.assertEqual(saved["last_invalidated_outcome"]["outcome"]["evaluation"], "P99")
        self.assertEqual((folder / "assessment.md").read_text(), original)
        self.assertEqual(sa._attempts(self.campaign)[-1]["label"], "P1")  # the repair made no model call
        sa.ROADMAP.write_text(sa.ROADMAP.read_text().replace("Mission v1", "Mission v1\nPAUSE: advisor operator pause"))
        self.assertEqual(sa.tick(self.campaign)["verdict"], "PAUSED")

    def test_a_short_complete_run_does_not_lose_its_supported_wait(self) -> None:
        self.started()
        folder = self.campaign / "P99"
        folder.mkdir()
        (folder / "meta.json").write_text(json.dumps({"runtime_readback": {"refusal_fallbacks": []}, "tool_calls": [{"name": "Read"}]}))
        state = sa._load_state(self.campaign)
        state["last_outcome"] = {**sa.parse_outcome("## Outcome\n" + (self.WAIT % "after:2026-11-14T20:00:00Z").replace("|", "\n")), "evaluation": "P99"}
        sa._save_state(self.campaign, state)
        self.at("2026-11-13T18:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        self.assertEqual(sa._load_state(self.campaign)["last_outcome"]["evaluation"], "P99")

    def test_brief_uses_numeric_assessment_order_and_current_recipient_state(self) -> None:
        self.started()
        for n in (9, 10, 11):
            path = self.campaign / f"P{n}" / "assessment.md"
            path.parent.mkdir(); path.write_text(f"assessment {n}")
        sa._log_assignment(self.campaign, {"id": "ADV-001", "state": "DRAFTED", "recipient": "Science", "key": "case"})
        record = _record("ORCH-CASE", "COMPLETE")
        record["OBJECTIVE"] = "ADV-001 delivered; consumer checked separately"
        (self.repo / "ledger/tasks/orchestrator/ORCH-CASE.json").write_text(json.dumps(record))
        obs = sa.observe(self.campaign, sa._load_state(self.campaign))
        brief = sa.build_brief_p(self.campaign, obs)
        previous = brief.split("## Previous assessment\n", 1)[1].split("\n", 1)[0]
        self.assertTrue(previous.startswith("P11:"), previous)
        state = sa.assignment_states(self.campaign)["ADV-001"]
        self.assertEqual(state["highest"], "TAKEN")  # historical evidence is not silently upgraded
        self.assertEqual(state["mandates"][0]["verdict"], "RELEASED")
        self.assertIn('"verdict": "RELEASED"', brief)
        self.assertIn('ledger/tasks/orchestrator/ORCH-CASE.json', brief)

    def test_an_invalidated_attempt_cannot_return_as_the_reusable_previous_assessment(self) -> None:
        self.started()
        for n in (9, 10, 11):
            path = self.campaign / f"P{n}" / "assessment.md"
            path.parent.mkdir(); path.write_text(f"assessment {n}")
        (self.campaign / "P11/meta.json").write_text(json.dumps({"runtime_readback": {"refusal_fallbacks": [{"trigger": "refusal"}]}, "tool_calls": [{"name": "Read"}] * 4}))
        state = sa._load_state(self.campaign)
        state.update(last_outcome={}, last_invalidated_outcome={"outcome": {"evaluation": "P11", "outcome": "wait"}, "reason": "incomplete"})
        sa._save_state(self.campaign, state)
        brief = sa.build_brief_p(self.campaign, sa.observe(self.campaign, state))
        previous = brief.split("## Previous assessment\n", 1)[1].split("\n", 1)[0]
        self.assertTrue(previous.startswith("P10:"), previous)
        self.assertIn("## Previous outcome superseded", brief)
        self.assertIn('"P11":', brief.split("## Incomplete attempts", 1)[1])
        self.assertEqual((self.campaign / "P11/assessment.md").read_text(), "assessment 11")


    def test_legacy_start_metadata_prevents_missing_the_hourly_recall_by_seconds(self) -> None:
        self.started()
        state = sa._load_state(self.campaign)
        state.pop("last_evaluation_started_utc", None)
        state["last_evaluation_utc"] = "2026-11-13T10:02:04Z"
        state["last_outcome"] = {"evaluation": "P1", "stated": True, "outcome": "assign"}
        sa._save_state(self.campaign, state)
        path = self.campaign / "P1/meta.json"
        meta = json.loads(path.read_text())
        meta.update(started_utc="2026-11-13T10:00:00Z", ended_utc="2026-11-13T10:02:04Z")
        path.write_text(json.dumps(meta))
        self.land("SCI delivery: completed package")
        self.at("2026-11-13T11:01:55Z")  # 61m55 from start, 59m51 from completion: the live failure
        result = sa.tick(self.campaign)
        self.assertEqual(result["verdict"], "EVALUATE")
        self.assertEqual(result["evaluation_clock"]["source"], "matching legacy runtime metadata")
        saved = sa._load_state(self.campaign)
        self.assertEqual(saved["last_evaluation_utc"], "2026-11-13T10:02:04Z")
        self.assertEqual(saved["last_evaluation_started_utc"], "2026-11-13T10:00:00Z")
        self.assertEqual(len({(a["stage"], a["index"]) for a in sa._attempts(self.campaign)}), 1)  # tick never launches the model

    def test_a_mismatched_legacy_runtime_does_not_invent_an_earlier_start(self) -> None:
        self.started()
        state = sa._load_state(self.campaign)
        state.pop("last_evaluation_started_utc", None)
        state["last_evaluation_utc"] = "2026-11-13T10:02:04Z"
        state["last_outcome"] = {"evaluation": "P1", "stated": True, "outcome": "assign"}
        sa._save_state(self.campaign, state)  # P1's actual metadata does not finish at 10:02:04
        self.land("SCI delivery: completed package")
        self.at("2026-11-13T11:01:55Z")
        result = sa.tick(self.campaign)
        self.assertEqual(result["verdict"], "DEFERRED")
        self.assertEqual(result["evaluation_clock"]["source"], "legacy completion (start unavailable)")
        self.assertIn("anticipating events pending", result["why"])
        self.assertIn("11:02:04Z", result["why"])
        self.assertNotIn("last_evaluation_started_utc", sa._load_state(self.campaign))

    def test_a_new_run_records_start_and_finish_separately_for_its_cadence(self) -> None:
        self.authorise()
        sa.tick(self.campaign)
        original = sa.run
        def slower(*args, **kwargs):
            self.at("2026-11-13T10:02:04Z")
            return original(*args, **kwargs)
        sa.run = slower
        try:
            self.assertEqual(sa.evaluate(self.campaign), 0)
        finally:
            sa.run = original
        state = sa._load_state(self.campaign)
        self.assertEqual(state["last_evaluation_started_utc"], "2026-11-13T10:00:00Z")
        self.assertEqual(state["last_evaluation_utc"], "2026-11-13T10:02:04Z")
        self.land("SCI delivery: completed package")
        self.at("2026-11-13T11:01:55Z")
        result = sa.tick(self.campaign)
        self.assertEqual(result["verdict"], "EVALUATE")
        self.assertEqual(result["evaluation_clock"]["source"], "recorded evaluation start")


    def test_a_deferred_delivery_survives_the_tick_that_updates_the_observation(self) -> None:
        self.started()
        self.land("SCI52 record COMPLETE; package delivered")
        self.at("2026-11-13T10:30:00Z")
        early = sa.tick(self.campaign)
        self.assertEqual(early["verdict"], "DEFERRED")
        self.assertTrue(any(e.startswith("delivery:") for e in early["events"]))
        self.at("2026-11-13T11:00:00Z")
        due = sa.tick(self.campaign)  # no further commit, mandate transition or radar
        self.assertEqual(due["verdict"], "EVALUATE")
        self.assertTrue(any(e.startswith("delivery:") for e in due["events"]))
        sa.evaluate(self.campaign)
        self.at("2026-11-13T12:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")

    def test_a_running_evaluation_does_not_consume_a_later_delivery(self) -> None:
        self.started()
        state = sa._load_state(self.campaign)
        before = state["main_sha"]
        state["running"] = sa._pid_identity(os.getpid())
        sa._save_state(self.campaign, state)
        self.land("SCI52 record COMPLETE; package delivered")
        self.at("2026-11-13T11:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "RUNNING")
        state = sa._load_state(self.campaign)
        self.assertEqual(state["main_sha"], before)
        state["running"] = ""
        sa._save_state(self.campaign, state)
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")


    def test_an_empty_continuous_pipeline_can_assess_pending_delivery_without_a_cooldown_gate(self) -> None:
        self.started()
        self.complete("ORCH-A")
        self.land("SCI53 record COMPLETE; package delivered")
        self.at("2026-11-13T10:10:00Z")
        result = sa.tick(self.campaign)
        self.assertTrue(result["queue"]["exhausted"])
        self.assertEqual(result["verdict"], "EVALUATE")
        self.assertIn("idle pipeline", result["why"])
        self.assertEqual(len({(a["stage"], a["index"]) for a in sa._attempts(self.campaign)}), 1)

    def test_a_stated_choice_with_an_empty_queue_gets_a_next_decision_without_new_inputs(self) -> None:
        self.started()
        self.complete("ORCH-A")
        self.at("2026-11-13T11:30:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        self.evaluate_with("outcome: assign")
        self.at("2026-11-13T14:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        self.at("2026-11-13T16:00:00Z")
        result = sa.tick(self.campaign)
        self.assertFalse(result["events"])
        self.assertEqual(result["verdict"], "EVALUATE")
        self.assertIn("previous choice", result["why"])
        self.evaluate_with(self.WAIT % "after:2026-11-13T23:00:00Z")
        self.at("2026-11-13T21:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")  # a supported stated wait is not busy work

    def test_an_empty_bounded_pilot_keeps_its_existing_cadence_and_limits(self) -> None:
        sa.tick(self.campaign); sa.evaluate(self.campaign)
        self.complete("ORCH-A")
        self.land("SCI53 record COMPLETE; package delivered")
        self.at("2026-11-13T10:10:00Z")
        result = sa.tick(self.campaign)
        self.assertTrue(result["queue"]["exhausted"])
        self.assertEqual(result["verdict"], "DEFERRED")
        self.assertEqual(len({(a["stage"], a["index"]) for a in sa._attempts(self.campaign)}), 1)


    # ---- 2026-11-16: a blocked path is not a blocked portfolio ---------------------------------------------------------------------------------------------------------------------------------
    # The observed case: two intakes blocked, `exhausted` true because it reads task records only, a general hold or wait recorded, and the portfolio holding ready rows that nobody named
    # (the 13:21Z closing: nine rows ready, five waiting, five backlog; every session answered 'nothing queued, awaiting X').

    def portfolio_rows(self, *rows: tuple[str, str]) -> None:
        path = sa.ROOT / sa.PORTFOLIO_REL
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = ["\t".join(sa.PORTFOLIO_FIELDS)] + ["\t".join({"id": i, "opportunity": f"opportunity {i}", "status": st, "priority": "1", "resume_when": "record:ORCH-A=COMPLETE" if st == "waiting" else ""}.get(f, "") for f in sa.PORTFOLIO_FIELDS) for i, st in rows]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def blocked_and_portfolio(self) -> None:
        """Both written mandates blocked (the intakes), the portfolio with two ready rows and one waiting row."""
        self.held_campaign()
        self.write_waiting("ORCH-A", "the human check of the source pages", other_step="DONE")
        self.portfolio_rows(("RP-101", "ready"), ("RP-102", "ready"), ("RP-103", "waiting"))

    def test_the_tick_never_shows_exhausted_without_its_scope_and_the_blocked_paths(self) -> None:
        self.blocked_and_portfolio()
        self.at("2026-11-13T17:00:00Z")
        t = sa.tick(self.campaign)
        q = t["queue"]
        self.assertTrue(q["exhausted"])                                                                      # kept for compatibility
        self.assertEqual(q["scope"], "written executable tasks only; not a statement about the portfolio")
        self.assertEqual([b["task"] for b in q["blocked_paths"]], ["ORCH-A"])
        self.assertIn("human check", q["blocked_paths"][0]["blocker"])
        self.assertEqual(q["portfolio_ready"], ["RP-101", "RP-102"])                                         # the rows the queue statement says nothing about

    def test_a_quiet_tick_names_the_ready_rows_in_its_own_why_line(self) -> None:
        """ADV-047: the 2026-11-18 idle statements followed ticks that said only 'nothing new: the previous assessment stands' while two portfolio rows were ready."""
        self.blocked_and_portfolio()
        self.at("2026-11-13T17:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")                                      # first tick of the campaign
        sa.evaluate(self.campaign)
        self.at("2026-11-13T18:00:00Z")
        t = sa.tick(self.campaign)
        self.assertEqual(t["verdict"], "NONE", t["why"])
        self.assertIn("ready portfolio rows: RP-101, RP-102", t["why"])
        self.assertIn("nothing new", t["why"])                                                               # the event statement is kept, the scope is added

    def test_a_general_hold_over_ready_portfolio_rows_is_refused_and_a_hold_that_names_them_is_not(self) -> None:
        """BEFORE (HE64 code, same fixture): the hold with the reason 'intakes blocked, queue exhausted' was recorded and the next ticks said NONE for as long as ORCH-A stayed blocked."""
        self.blocked_and_portfolio()
        self.at("2026-11-13T17:00:00Z")
        with patch("sys.stderr", new=__import__("io").StringIO()) as err:
            rc = sa.main(["hold", "--campaign", str(self.campaign), "--reason", "intake blocked, queue exhausted", "--resume-when", "record:ORCH-A=COMPLETE", "--excluded", EXCL])
        self.assertEqual(rc, 2)
        self.assertIn("RP-101", err.getvalue()); self.assertIn("A blocked path is not a blocked portfolio", err.getvalue())
        self.assertFalse((self.campaign / "holds.jsonl").exists())
        with patch("sys.stderr", new=__import__("io").StringIO()) as err2:
            self.assertEqual(sa.main(["hold", "--campaign", str(self.campaign), "--reason", "waiting", "--resume-when", "record:ORCH-A=COMPLETE", "--excluded", "no path here, only prose"]), 2)
        self.assertIn("--excluded", err2.getvalue())                                                        # a hold that names no path is a general wait
        ok = sa.main(["hold", "--campaign", str(self.campaign), "--reason", "ORCH-A blocked; RP-101 needs ORCH-A's result, RP-102 needs the same source check", "--resume-when", "record:ORCH-A=COMPLETE",
                      "--excluded", "ORCH-A: source pages need a human check; RP-101 and RP-102: both read those pages"])
        self.assertEqual(ok, 0)                                                                              # a considered wait is still allowed
        row = json.loads((self.campaign / "holds.jsonl").read_text(encoding="utf-8").splitlines()[0])
        self.assertIn("RP-102", row["excluded"])
        self.at("2026-11-13T18:00:00Z")
        quiet = sa.tick(self.campaign)
        self.assertEqual(quiet["verdict"], "NONE")
        self.assertIn("excluded paths: ORCH-A: source pages need a human check", quiet["presidio"])
        self.assertNotIn("NOT A VALID GENERAL WAIT", quiet["presidio"])

    def test_a_hold_lapses_at_min_hours_between_instead_of_silencing_the_ticks_all_night(self) -> None:
        """The overnight 22:55-04:22Z run of NONE verdicts under a host hold: six hours, no comparison. After the change the hold answers NONE for min_hours_between (4 h) and then EVALUATE with its excluded paths."""
        self.held_campaign()
        self.portfolio_rows(("RP-201", "waiting"))
        self.at("2026-11-13T17:00:00Z")
        self.assertEqual(sa.main(["hold", "--campaign", str(self.campaign), "--reason", "waiting for ORCH-A", "--resume-when", "record:ORCH-A=COMPLETE", "--excluded", EXCL]), 0)
        verdicts = []
        for hour in range(18, 24):
            self.at(f"2026-11-13T{hour}:00:00Z")
            verdicts.append(sa.tick(self.campaign)["verdict"])
        self.assertEqual(verdicts[:3], ["NONE", "NONE", "NONE"])                                             # 18, 19, 20: inside the 4 hours
        self.assertEqual(verdicts[3], "EVALUATE")                                                           # 21:00: the hold lapsed
        self.at("2026-11-13T21:00:00Z")
        lapsed = sa.tick(self.campaign)
        self.assertIn("hold lapsed", lapsed["why"]); self.assertIn("ORCH-A", lapsed["why"])

    def test_a_stated_wait_that_leaves_out_ready_rows_is_asked_once_per_portfolio_state(self) -> None:
        self.started()
        self.evaluate_with(self.WAIT % "record:ORCH-A=COMPLETE")
        self.at("2026-11-13T15:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")                                          # no portfolio rows: the old behaviour, unchanged
        self.portfolio_rows(("RP-301", "ready"))
        st = sa._load_state(self.campaign); st["portfolio_digest"] = sa.portfolio_snapshot()["digest"]; sa._save_state(self.campaign, st)      # a wait saved BEFORE this rule, with the portfolio already consumed (a new row alone is already an event): the real P16-era state
        self.at("2026-11-13T16:00:00Z")
        first = sa.tick(self.campaign)
        self.assertEqual(first["verdict"], "EVALUATE"); self.assertIn("RP-301", first["why"])
        self.at("2026-11-13T17:00:00Z")
        again = sa.tick(self.campaign)
        self.assertEqual(again["verdict"], "NONE")                                                          # asked once for this portfolio state, not every hour
        self.assertIn("NOT A VALID GENERAL WAIT", again["presidio"])                                         # and the presidio line says so

    def test_an_evaluation_cannot_state_a_wait_that_does_not_name_the_ready_rows(self) -> None:
        self.started()
        self.portfolio_rows(("RP-401", "ready"))
        self.evaluate_with(self.WAIT % "record:ORCH-A=COMPLETE")
        last = sa._load_state(self.campaign)["last_outcome"]
        self.assertFalse(last["stated"]); self.assertIn("RP-401", last["problem"])
        self.at("2026-11-13T17:00:00Z")
        self.evaluate_with("outcome: wait|excluded: RP-401 needs the lever result that ORCH-A has not delivered|reason: RP-401 is the only ready row and it depends on ORCH-A|resume_when: record:ORCH-A=COMPLETE")
        self.assertTrue(sa._load_state(self.campaign)["last_outcome"]["stated"])                             # a wait that names the row and its cause is kept
        self.at("2026-11-13T18:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")

    def test_the_operator_pause_and_real_waits_are_not_touched(self) -> None:
        self.started()
        self.portfolio_rows(("RP-501", "ready"))
        self.roadmap("PAUSE: science \u2014 hold the SCI reading packages")
        self.at("2026-11-13T17:00:00Z")
        self.assertIn("PAUSE: science", " ".join(sa.tick(self.campaign)["operator_controls"]))              # an operator pause is still shown and honoured as before
        self.portfolio_rows(("RP-502", "waiting"), ("RP-503", "backlog"))                                    # no ready row: a general wait is allowed
        self.roadmap()
        self.evaluate_with(self.WAIT % "record:ORCH-A=COMPLETE")
        self.assertTrue(sa._load_state(self.campaign)["last_outcome"]["stated"])

    def test_the_run_folder_is_assembled_outside_the_checkout_and_moved_in_one_step(self) -> None:
        self.authorise()
        seen = []
        real = os.replace
        def spy(src, dst, *a, **k):
            if Path(dst).parent.name == "P1" and Path(dst).parent.parent == self.campaign:
                seen.append(sorted(x.name for x in (self.campaign / "P1").iterdir()))                       # what the shared folder holds just before each move
            return real(src, dst, *a, **k)
        with patch.object(sa.os, "replace", side_effect=spy):
            self.assertEqual(sa.evaluate(self.campaign), 0)
        self.assertTrue(seen and seen[0] == [], seen)                                                        # nothing was written into the campaign folder before the final move
        self.assertTrue((self.campaign / "P1/assessment.md").exists() and (self.campaign / "P1/meta.json").exists() and (self.campaign / "P1/brief.md").exists())
        self.assertFalse((sa.STATE_DIR / "runs" / f"{self.campaign.name}-P1").exists())                     # the spool is gone

    def test_the_recall_text_carries_the_clause_and_there_is_one_canonical_text(self) -> None:
        text = sa.recall_prompt(self.campaign)
        self.assertIn("a blocked path is not a blocked portfolio", text)
        self.assertIn("an EVALUATE left unrun needs its excluded paths and a resume condition", text)
        self.assertIn("the operator is a boost, not a dependency", text)                                    # ADV-049: the 2026-11-18 permanent instruction reaches the hourly recall
        self.assertEqual(text.count(sa.RECALL_MARK), 1)
        tag = re.search(r"\[text ([0-9a-f]{8})\]", text)
        self.assertTrue(tag and text.index(tag.group(0)) < 120, "the digest tag must sit where CronList shows the prompt")
        self.assertEqual(tag.group(1), sa.recall_digest(text.replace(" " + tag.group(0), "", 1).replace(str(sa.ROOT), "<root>")))      # eight hex digits of the text without the tag, the path as a placeholder
        saved_root, sa.ROOT = sa.ROOT, Path("/somewhere/else/checkout")
        try:
            elsewhere = re.search(r"\[text ([0-9a-f]{8})\]", sa.recall_prompt(self.campaign)).group(1)
        finally:
            sa.ROOT = saved_root
        self.assertEqual(elsewhere, tag.group(1))                                                           # the same text gives the same tag in any checkout (the 2026-11-16 mismatch: 047a03cd against b00417e1)
        drifted = sa.RECALL_PROMPT.replace("The ordinary verdict NONE does not cancel a due meeting. ", "")      # the 2026-11-16 drift: the meeting sentence was missing from the installed job
        self.assertNotEqual(sa.recall_digest(drifted.format(root=sa.ROOT, campaign=self.campaign)), tag.group(1))


class ObservedRef(ProactiveFixture):
    """2026-11-18: the tick read only the local `main`, which in the primary checkout was 13 hours behind the published branch, so it could say 'nothing new' while work landed. Fixtures with a real bare remote."""

    GENV = None

    def git(self, cwd: Path, *args: str) -> str:
        env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}
        return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True, env=env).stdout.strip()

    def remote(self) -> Path:
        """A bare `development` remote holding the repository's main, and a second clone that can publish to it."""
        bare = self.tmp / "development.git"
        self.git(self.tmp, "init", "-q", "--bare", "-b", "main", str(bare))
        self.git(self.repo, "remote", "add", "development", str(bare))
        self.git(self.repo, "push", "-q", "development", "main")
        self.git(self.repo, "fetch", "-q", "development", "main")
        other = self.tmp / "other"
        self.git(self.tmp, "clone", "-q", str(bare), str(other))
        return other

    def publish(self, other: Path, subject: str) -> str:
        (other / "ledger/tasks/orchestrator").mkdir(parents=True, exist_ok=True)
        (other / "ledger/tasks/orchestrator/pub.txt").write_text(subject, encoding="utf-8")
        self.git(other, "add", "."); self.git(other, "commit", "-q", "-m", subject)
        self.git(other, "push", "-q", "origin", "main")
        return self.git(other, "rev-parse", "HEAD")

    def test_a_remote_ahead_of_a_stale_local_main_is_read_and_the_tick_does_not_say_nothing_new(self) -> None:
        other = self.remote()
        sa.evaluate(self.campaign)
        self.at("2026-11-13T11:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")
        tip = self.publish(other, "SCI77 record COMPLETE; package delivered")       # published; this checkout's local main and remote-tracking ref know nothing of it
        self.assertNotEqual(self.git(self.repo, "rev-parse", "main"), tip)           # the 2026-11-18 situation: the old read ('main') is behind
        self.assertNotEqual(self.git(self.repo, "rev-parse", "development/main"), tip)
        self.at("2026-11-13T12:00:00Z")
        t = sa.tick(self.campaign)
        self.assertEqual(t["verdict"], "EVALUATE")
        self.assertTrue(any(e.startswith("delivery:") and "SCI77" in e for e in t["events"]), t["events"])
        ref = t["reference"]
        self.assertEqual((ref["ref"], ref["state"], ref["sha"]), ("development/main", "VERIFIED", tip))
        self.assertEqual(ref["local_main"]["behind_observed"], 1)                    # local main is reported as behind, not silently used
        self.assertEqual(self.git(self.repo, "rev-parse", "main"), self.git(self.repo, "rev-parse", "HEAD"))   # nothing was reset, checked out or merged

    def test_a_failed_fetch_is_said_and_nothing_new_is_not_claimed_as_proof(self) -> None:
        self.remote()
        sa.evaluate(self.campaign)
        self.git(self.repo, "remote", "set-url", "development", str(self.tmp / "gone.git"))      # the remote cannot be reached
        self.at("2026-11-13T11:00:00Z")
        t = sa.tick(self.campaign)
        self.assertEqual(t["verdict"], "NONE")
        self.assertEqual(t["reference"]["state"], "UNVERIFIED")
        self.assertIn("NOT VERIFIED", t["why"])
        self.assertIn("fetch", t["why"])

    def test_a_commit_only_on_local_main_is_labelled_unpublished(self) -> None:
        self.remote()
        sa.evaluate(self.campaign)
        self.land("a local-only change")
        self.at("2026-11-13T11:00:00Z")
        t = sa.tick(self.campaign)
        self.assertEqual((t["reference"]["ref"], t["reference"]["state"]), ("main", "LOCAL_ONLY"))
        self.assertIn("NOT VERIFIED", t["why"])

    def test_a_repository_without_the_published_remote_is_not_flagged(self) -> None:
        sa.evaluate(self.campaign)
        self.at("2026-11-13T11:00:00Z")
        t = sa.tick(self.campaign)
        self.assertEqual(t["reference"]["state"], "NO_REMOTE")
        self.assertNotIn("NOT VERIFIED", t["why"])

    def test_the_recall_arming_is_recorded_and_the_tick_warns_before_the_seven_day_expiry(self) -> None:
        self.assertEqual(sa.main(["authorise-continuous", "--campaign", str(self.campaign), "--source", "Operator roadmap line, 2026-11-14"]), 0)
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        sa.evaluate(self.campaign)
        self.at("2026-11-13T11:00:00Z")
        before = sa.tick(self.campaign)
        self.assertEqual(before["recall"]["armed_utc"], None)                        # nothing recorded yet: said, not guessed
        self.assertFalse(before["recall"]["renew_due"])
        self.assertEqual(sa.main(["recall-armed", "--campaign", str(self.campaign), "--job-id", "069fe752"]), 0)
        self.at("2026-11-15T11:00:00Z")
        two = sa.tick(self.campaign)
        self.assertEqual((two["recall"]["job_id"], two["recall"]["renew_due"]), ("069fe752", False))
        self.at("2026-11-18T12:00:00Z")
        due = sa.tick(self.campaign)
        self.assertTrue(due["recall"]["renew_due"])
        if due["verdict"] in ("NONE", "DEFERRED"):
            self.assertIn("RECALL RENEWAL DUE", due["why"])

    def test_repeated_ticks_with_nothing_landed_do_not_move_the_observed_state(self) -> None:
        """The hourly check by itself is not progress: ten empty ticks leave the reference, the events and the evaluation clock where they were."""
        self.remote()
        sa.evaluate(self.campaign)
        first = None
        for i in range(10):
            self.at(f"2026-11-13T{11 + (i // 2):02d}:{(i % 2) * 30:02d}:00Z")
            t = sa.tick(self.campaign)
            self.assertEqual((t["verdict"], t["events"]), ("NONE", []))
            first = first or (t["reference"]["sha"], t["evaluation_clock"])
            self.assertEqual((t["reference"]["sha"], t["evaluation_clock"]), first)


class CampaignHome(ProactiveFixture):
    """ADV-243: the primary checkout is the one campaign home and had stayed 1,535 commits behind the published main, so `assign` and `deliver` read old files. A fixture home with a real bare remote."""

    git, remote = ObservedRef.git, ObservedRef.remote

    def setUp(self) -> None:
        super().setUp()
        self.other = self.remote()
        self.home = self.repo / "campaign"
        self.log = "campaign/assignments.jsonl"
        self.write(self.other, self.log, '{"id": "ADV-001"}\n')
        self.send(self.other, "ADV: first row")
        self.git(self.repo, "pull", "-q", "--ff-only", "development", "main")

    def write(self, where: Path, rel: str, text: str) -> None:
        (where / rel).parent.mkdir(parents=True, exist_ok=True)
        (where / rel).write_text(text, encoding="utf-8")

    def send(self, other: Path, subject: str) -> str:
        self.git(other, "add", "."); self.git(other, "commit", "-q", "-m", subject)
        self.git(other, "push", "-q", "origin", "main")
        return self.git(other, "rev-parse", "HEAD")

    def head(self) -> str:
        return self.git(self.repo, "rev-parse", "HEAD")

    def refresh(self) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            code = sa.main(["refresh", "--campaign", str(self.home)])
        return code, out.getvalue()

    def stale(self) -> str:
        with contextlib.redirect_stderr(io.StringIO()):
            return sa.stale_refusal(self.home)

    def test_a_commit_that_touches_nothing_the_commands_read_stops_nothing(self) -> None:
        self.write(self.other, "notes/unrelated.md", "x\n"); self.send(self.other, "unrelated")
        self.assertEqual(self.stale(), "")

    def test_the_tick_says_when_the_files_it_read_are_older_than_the_ref_it_observed(self) -> None:
        self.assertNotIn("CHECKOUT BEHIND", sa.tick(self.campaign)["why"])
        self.write(self.other, "ledger/tasks/orchestrator/NEW.json", "{}\n"); self.send(self.other, "record")
        why = sa.tick(self.campaign)["why"]
        self.assertIn("CHECKOUT BEHIND on 1 file(s)", why)
        self.assertIn("refresh --campaign", why)

    def test_a_published_task_record_or_campaign_file_refuses_assign_and_deliver_and_writes_nothing(self) -> None:
        for rel in ("ledger/tasks/orchestrator/NEW.json", "campaign/assignments/ADV-002.md"):
            self.write(self.other, rel, "{}\n"); self.send(self.other, rel)
            self.assertIn("refresh --campaign", self.stale(), rel)
        before = (self.repo / self.log).read_bytes()
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            self.assertEqual(sa.main(["deliver", "--campaign", str(self.home), "--id", "ADV-001", "--state", "UNREACHABLE", "--evidence", "x"]), 2)
            self.assertEqual(sa.main(["assign", "--campaign", str(self.home), "--text-file", str(self.brief)]), 2)
        self.assertEqual(err.getvalue().count("is behind development/main"), 2)
        self.assertEqual((self.repo / self.log).read_bytes(), before)
        self.assertEqual(self.refresh()[0], 0)
        self.assertEqual(self.stale(), "")

    def test_refresh_replaces_only_what_main_already_holds_keeps_a_copy_and_leaves_other_changes(self) -> None:
        self.write(self.other, self.log, '{"id": "ADV-001"}\n{"id": "ADV-002"}\n{"id": "ADV-003"}\n')
        self.write(self.other, "campaign/assignments/ADV-002.md", "brief two\n")
        tip = self.send(self.other, "ADV: landed from a worktree")
        self.write(self.repo, self.log, '{"id": "ADV-001"}\n{"id": "ADV-002"}\n')       # the rows the home wrote, all published
        self.write(self.repo, "campaign/assignments/ADV-002.md", "brief two\n")          # untracked, in a new directory, identical to main
        self.write(self.repo, "campaign/scratch.txt", "mine\n")                          # nothing on main has this path
        code, said = self.refresh()
        self.assertEqual(code, 0, said)
        self.assertEqual(self.head(), tip)
        self.assertIn("ADV-003", (self.repo / self.log).read_text())
        self.assertEqual((self.repo / "campaign/scratch.txt").read_text(), "mine\n")
        copies = {p.name for p in (sa.STATE_DIR / "campaign" / "refresh").rglob("*") if p.is_file()}
        self.assertEqual(copies, {"assignments.jsonl", "ADV-002.md"})
        self.assertIn("already at", self.refresh()[1])

    def test_a_local_row_or_file_that_main_does_not_hold_stops_the_refresh_before_anything_is_touched(self) -> None:
        self.write(self.other, self.log, '{"id": "ADV-001"}\n{"id": "ADV-002", "state": "DRAFTED", "key": "theirs"}\n')
        self.write(self.other, "campaign/assignments/ADV-002.md", "brief two\n")
        self.write(self.other, "campaign/assignments/ADV-003.md", "published text\n")
        self.send(self.other, "ADV: landed")
        self.write(self.repo, self.log, '{"id": "ADV-001"}\n{"id": "ADV-002", "state": "DRAFTED", "key": "mine"}\n')        # one number, two drafts
        self.write(self.repo, "campaign/assignments/ADV-002.md", "brief two\n")
        self.write(self.repo, "campaign/assignments/ADV-003.md", "my own text\n")
        head, row = self.head(), (self.repo / self.log).read_bytes()
        code, said = self.refresh()
        self.assertEqual(code, 2)
        self.assertIn(f"KEEP {self.log}", said)
        self.assertIn("KEEP campaign/assignments/ADV-003.md", said)
        self.assertNotIn("KEEP campaign/assignments/ADV-002.md", said)
        self.assertEqual((self.head(), (self.repo / self.log).read_bytes()), (head, row))
        self.assertTrue((self.repo / "campaign/assignments/ADV-002.md").exists())

    def test_unlanded_appended_rows_are_put_back_after_the_fast_forward_and_named(self) -> None:
        self.write(self.other, self.log, '{"id": "ADV-001"}\n{"id": "ADV-002", "state": "DRAFTED", "key": "theirs"}\n')
        tip = self.send(self.other, "ADV: landed from a worktree")
        mine = ['{"id": "ADV-009", "state": "DRAFTED", "key": "mine"}', '{"id": "ADV-001", "state": "SENT"}']      # a send names a published id: not a collision
        self.write(self.repo, self.log, '{"id": "ADV-001"}\n' + "\n".join(mine) + "\n")
        self.write(self.repo, "campaign/assignments/ADV-009.md", "brief nine\n")
        code, said = self.refresh()
        self.assertEqual(code, 0, said)
        self.assertEqual(self.head(), tip)
        self.assertEqual((self.repo / self.log).read_text().splitlines(), ['{"id": "ADV-001"}', '{"id": "ADV-002", "state": "DRAFTED", "key": "theirs"}', *mine])
        self.assertEqual((self.repo / "campaign/assignments/ADV-009.md").read_text(), "brief nine\n")
        self.assertIn("ADV-009 DRAFTED, ADV-001 SENT", said)

    def test_rows_are_not_put_back_when_the_home_edited_an_earlier_line_or_wrote_an_unreadable_one(self) -> None:
        for before, local, published in (('a\n', 'b\nc\n', 'a\n'), ('', 'not json\n', ''), ('', '[1]\n', '')):
            self.assertIsNone(sa._unlanded_rows(before, local, published), local)
        self.assertEqual(sa._unlanded_rows('', '{"id": "ADV-1", "state": "SENT"}\n', ''), ['{"id": "ADV-1", "state": "SENT"}'])

    def test_a_fast_forward_git_refuses_puts_the_local_files_back(self) -> None:
        self.write(self.other, "campaign/assignments/ADV-002.md", "brief two\n")
        self.write(self.other, "campaign/ignored.txt", "published\n")
        self.send(self.other, "ADV: landed")
        (self.repo / ".git/info").mkdir(exist_ok=True)
        (self.repo / ".git/info/exclude").write_text("ignored.txt\n", encoding="utf-8")
        self.write(self.repo, "campaign/ignored.txt", "only here\n")                     # ignored, so `status` does not list it: git itself must refuse
        self.write(self.repo, "campaign/assignments/ADV-002.md", "brief two\n")
        head = self.head()
        code, said = self.refresh()
        self.assertEqual(code, 2, said)
        self.assertEqual(self.head(), head)
        self.assertEqual((self.repo / "campaign/assignments/ADV-002.md").read_text(), "brief two\n")
        self.assertEqual((self.repo / "campaign/ignored.txt").read_text(), "only here\n")

    def test_a_home_with_its_own_commits_is_never_reset(self) -> None:
        self.write(self.other, "notes/a.md", "a\n"); self.send(self.other, "theirs")
        self.write(self.repo, "notes/b.md", "b\n"); self.git(self.repo, "add", "."); self.git(self.repo, "commit", "-q", "-m", "mine")
        head = self.head()
        code, said = self.refresh()
        self.assertEqual(code, 2)
        self.assertIn("land them first", said)
        self.assertEqual(self.head(), head)

    def test_an_unreachable_remote_is_said_and_the_last_fetched_ref_still_counts(self) -> None:
        self.write(self.other, "ledger/tasks/orchestrator/NEW.json", "{}\n"); self.send(self.other, "record")
        self.git(self.repo, "fetch", "-q", "development", "main")
        self.git(self.repo, "remote", "set-url", "development", str(self.tmp / "gone.git"))
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            self.assertIn("REFUSED", sa.stale_refusal(self.home))
        self.assertIn("UNVERIFIED", err.getvalue())


class NoticeNews(unittest.TestCase):
    def test_a_flagged_notice_is_named_once_and_an_absent_or_empty_summary_says_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path, state = Path(folder) / "summary.json", {}
            self.assertEqual(sa.notice_news(state, path), "")
            path.write_text(json.dumps({"new_flagged": [["19357348", "retraction", "42583763", "2026-08-12"]]}), encoding="utf-8")
            line = sa.notice_news(state, path)
            self.assertIn("NEW NOTICE", line)
            self.assertIn("PMID 19357348 retraction (notice 42583763, 2026-08-12)", line)
            self.assertEqual(sa.notice_news(state, path), "")


class LivingPortfolio(Base):
    """Permanent opportunities reach a real brief and wake decisions without a new radar."""

    def setUp(self) -> None:
        super().setUp()
        self.repo = _repo_with_records(self.tmp, {"ORCH-A": "COMPLETE"})
        self.saved_attrs = {k: getattr(sa, k) for k in ("ROOT", "ROADMAP", "STATE_DIR", "_sessions")}
        sa.ROOT, sa.ROADMAP, sa.STATE_DIR = self.repo, self.repo / "disease-models/wwox/research/drug_repurposing/roadmap_current.md", self.tmp / "state"
        sa._sessions = lambda: {"SCI": "idle"}
        self.env_now = os.environ.get("LEGEND_ADVISOR_NOW")
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T10:00:00Z"
        self.campaign = self.tmp / "pilot"
        sa.main(["activate", "--campaign", str(self.campaign)])
        sa.main(["authorise-continuous", "--campaign", str(self.campaign), "--source", "operator"])

    def tearDown(self) -> None:
        for k, v in self.saved_attrs.items():
            setattr(sa, k, v)
        if self.env_now is None:
            os.environ.pop("LEGEND_ADVISOR_NOW", None)
        else:
            os.environ["LEGEND_ADVISOR_NOW"] = self.env_now
        super().tearDown()

    def add(self, **values: str) -> None:
        sa.portfolio_update({"id": "RP-TEST", "opportunity": "Which comparison discriminates the new mechanism?", "status": "ready",
                             "priority": "P1", "sources": "original.md", "next_action": "read the primary comparison", **values})

    def test_upsert_preserves_sources_and_other_rows_and_editorial_timestamps_do_not_wake(self) -> None:
        self.add()
        before = sa.portfolio_snapshot({})["digest"]
        sa.portfolio_update({"id": "RP-TEST", "outcome": "consumer now uses the limit"})
        after = sa.portfolio_snapshot({})
        self.assertNotEqual(before, after["digest"])
        self.assertEqual(after["items"][0]["sources"], "original.md")
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T11:00:00Z"
        sa.portfolio_update({"id": "RP-TEST"})
        self.assertEqual(sa.portfolio_snapshot({})["digest"], after["digest"])
        self.add(id="RP-OTHER", opportunity="A separate opportunity")
        self.assertEqual(len(sa.portfolio_rows()[0]), 2)

    def test_a_new_row_is_in_the_saved_brief_and_a_later_change_is_a_distinct_event(self) -> None:
        self.add()
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        self.assertEqual(sa.evaluate(self.campaign), 0)
        brief = (self.campaign / "P1/brief.md").read_text()
        self.assertIn("## Living Research Portfolio", brief)
        self.assertIn("RP-TEST", brief)
        self.assertIn("read the primary comparison", brief)
        self.assertNotIn("RP-TEST", sa.tick(self.campaign)["events"])
        self.assertFalse(any(e.startswith("portfolio:") for e in sa.tick(self.campaign)["events"]))
        self.add(next_action="a different comparison")
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T12:00:00Z"
        tick = sa.tick(self.campaign)
        self.assertEqual(tick["verdict"], "EVALUATE")
        self.assertTrue(any(e.startswith("portfolio:") for e in tick["events"]))

    def test_a_deferred_change_remains_visible_until_evaluated_and_pause_still_prevails(self) -> None:
        (self.repo / "ledger/tasks/orchestrator/ORCH-A.json").write_text(json.dumps(_record("ORCH-A", "OPEN")))
        self.add(); sa.tick(self.campaign); sa.evaluate(self.campaign)
        self.add(next_action="new decisive source")
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T10:10:00Z"
        self.assertEqual(sa.tick(self.campaign)["verdict"], "DEFERRED")
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T11:10:00Z"
        self.assertEqual(sa.tick(self.campaign)["verdict"], "EVALUATE")
        (self.campaign / "DISABLED").write_text("operator")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "DISABLED")

    def test_the_advisors_own_portfolio_patch_is_consumed_not_a_new_signal(self) -> None:
        self.add()
        sa.tick(self.campaign)
        os.environ["FAKE_PORTFOLIO"] = json.dumps([{"id": "RP-TEST", "outcome": "examined; not adopted"}])
        try:
            self.assertEqual(sa.evaluate(self.campaign), 0)
        finally:
            os.environ.pop("FAKE_PORTFOLIO", None)
        self.assertEqual(sa.portfolio_rows()[0][0]["outcome"], "examined; not adopted")
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T10:10:00Z"
        result = sa.tick(self.campaign)
        self.assertEqual(result["verdict"], "NONE")
        self.assertFalse(any(e.startswith("portfolio:") for e in result["events"]))

    def test_an_external_portfolio_change_during_evaluation_is_not_swallowed_with_its_patch(self) -> None:
        self.add()
        sa.tick(self.campaign)
        original = sa.run
        def changed(*args, **kwargs):
            sa.portfolio_update({"id": "RP-TEST", "next_action": "external new source to inspect"})
            return original(*args, **kwargs)
        sa.run = changed
        os.environ["FAKE_PORTFOLIO"] = json.dumps([{"id": "RP-TEST", "outcome": "advisory note"}])
        try:
            self.assertEqual(sa.evaluate(self.campaign), 0)
        finally:
            sa.run = original
            os.environ.pop("FAKE_PORTFOLIO", None)
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T10:10:00Z"
        result = sa.tick(self.campaign)
        self.assertEqual(result["verdict"], "EVALUATE")
        self.assertTrue(any(e.startswith("portfolio:") for e in result["events"]))
        self.assertEqual(sa.portfolio_rows()[0][0]["next_action"], "external new source to inspect")

    def test_linked_tasks_own_execution_and_release_requests_a_review_not_completion(self) -> None:
        self.add(mandate_id="ORCH-A")
        active = sa.portfolio_snapshot({"ORCH-A": {"verdict": "CONTINUE", "path": "task.json"}})
        self.assertEqual(active["actionable"], [])
        self.assertEqual(active["items"][0]["execution"], "CONTINUE")
        released = sa.portfolio_snapshot({"ORCH-A": {"verdict": "RELEASED", "path": "task.json"}})
        self.assertTrue(released["items"][0]["review_due"])
        self.assertEqual(released["items"][0]["status"], "ready")
        sa.portfolio_update({"id": "RP-TEST", "status": "done", "outcome": "consumer and next question recorded"})
        self.assertEqual(sa.portfolio_snapshot({"ORCH-A": {"verdict": "RELEASED"}})["actionable"], [])

    def test_a_resolved_dependency_becomes_actionable_without_a_radar(self) -> None:
        self.add(status="waiting", resume_when="after:2026-11-13T12:00:00Z")
        before = sa.portfolio_snapshot({})
        self.assertEqual(before["actionable"], [])
        os.environ["LEGEND_ADVISOR_NOW"] = "2026-11-13T12:01:00Z"
        after = sa.portfolio_snapshot({})
        self.assertEqual(after["actionable"], ["RP-TEST"])
        self.assertNotEqual(before["digest"], after["digest"])

    def test_saved_assessment_updates_feed_the_portfolio_without_rewriting_the_assessment(self) -> None:
        patch = [{"id": "RP-FOLLOWUP", "opportunity": "Which follow-up separates the two explanations?", "status": "ready", "sources": "checked-result.md"}]
        old = os.environ.get("FAKE_PORTFOLIO")
        os.environ["FAKE_PORTFOLIO"] = json.dumps(patch)
        try:
            sa.tick(self.campaign)
            self.assertEqual(sa.evaluate(self.campaign), 0)
        finally:
            if old is None:
                os.environ.pop("FAKE_PORTFOLIO", None)
            else:
                os.environ["FAKE_PORTFOLIO"] = old
        self.assertIn('"RP-FOLLOWUP"', (self.campaign / "P1/assessment.md").read_text())
        self.assertEqual(sa.portfolio_snapshot({})["actionable"], ["RP-FOLLOWUP"])
        self.assertEqual(sa.check(self.campaign), 0)
        before = (sa.ROOT / sa.PORTFOLIO_REL).read_text()
        warning = sa.apply_portfolio_updates('## Portfolio updates\n```json\n[{"id":"RP-FOLLOWUP","invalid":"x"}]\n```')
        self.assertTrue(warning)
        self.assertEqual((sa.ROOT / sa.PORTFOLIO_REL).read_text(), before)


class Snapshot(unittest.TestCase):
    def test_a_modified_tracked_file_keeps_its_first_character(self) -> None:
        tmp, _ = _git_repo()
        (tmp / "tracked.md").write_text("changed", encoding="utf-8")  # status line " M tracked.md": its leading space once shifted the path to 'racked.md'
        saved, sa.ROOT = sa.ROOT, tmp
        try:
            snap = sa.snapshot()
        finally:
            sa.ROOT = saved
        self.assertEqual([(d["status"], d["path"]) for d in snap["uncommitted"]], [("M", "tracked.md")])
        self.assertEqual(snap["uncommitted"][0]["sha256"], sa.sha256_text("changed"))

    def test_a_delivery_announced_but_absent_from_the_snapshot_is_stated_not_assumed(self) -> None:
        tmp, ids = _git_repo()
        spec = f"{ids['delivered']}:pkg_sci48"
        saved, sa.ROOT = sa.ROOT, tmp
        try:
            snap = sa.snapshot(expect=[spec])
            brief = sa.build_brief("A", tmp / "c", "mission", "constraints", expect=[spec])
            self.assertEqual(snap["main_ahead"][0]["commits"], 1)
            self.assertIn("pkg_sci48", snap["main_ahead"][0]["new_folders"])
            self.assertEqual((snap["deliveries"][0]["in_snapshot"], snap["deliveries"][0]["accessible"]), (False, False))
            self.assertIn("**Not available to you:**", brief)
            self.assertIn("is ahead of this snapshot by 1 commit", brief)
            rows = sa.deliveries_read(brief, [{"name": "Grep", "input": {"pattern": "SCI48", "path": "/x"}, "is_error": False}])
            self.assertEqual((rows[0]["in_snapshot"], rows[0]["reachable"], rows[0]["files_read"]), (False, "NO", 0))
            subprocess.run(["git", "merge", "-q", "main"], cwd=tmp, check=True, capture_output=True, env={**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"})
            synced = sa.snapshot(expect=[spec])
            self.assertEqual((synced["deliveries"][0]["in_snapshot"], synced["deliveries"][0]["accessible"], synced["main_ahead"]), (True, True, []))
            read = sa.deliveries_read(sa.build_brief("A", tmp / "c", "m", "c", expect=[spec]),
                                      [{"name": "Read", "input": {"file_path": str(tmp / "pkg_sci48" / "README.md")}, "is_error": False}])
            self.assertEqual((read[0]["in_snapshot"], read[0]["files_read"]), (True, 1))
            self.assertNotIn("Not available", sa.build_brief("A", tmp / "c", "m", "c", expect=[spec]))
        finally:
            sa.ROOT = saved

    def test_an_unannounced_main_ahead_still_surfaces_without_blocking(self) -> None:
        tmp, _ = _git_repo()
        saved, sa.ROOT = sa.ROOT, tmp
        try:
            brief = sa.build_brief("A", tmp / "c", "mission", "constraints")
        finally:
            sa.ROOT = saved
        self.assertIn("folders added there and absent here", brief)
        self.assertNotIn("Not available to you", brief)  # nothing was announced, so nothing is claimed missing

    def test_the_prompt_is_not_to_be_reopened(self) -> None:
        self.assertIn("do not open it", sa.CONTRACT)

    def test_uncommitted_input_is_listed_with_a_digest(self) -> None:
        tmp = Path(tempfile.mkdtemp(prefix="sadv_git_"))
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        for cmd in (["git", "init", "-q"], ["git", "-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-q", "--allow-empty", "-m", "x"]):
            subprocess.run(cmd, cwd=tmp, check=True, capture_output=True)
        (tmp / "new.md").write_text("draft", encoding="utf-8")
        saved = sa.ROOT
        sa.ROOT = tmp
        try:
            snap = sa.snapshot()
        finally:
            sa.ROOT = saved
        self.assertEqual(len(snap["repo_sha"]), 40)
        self.assertEqual([d["path"] for d in snap["uncommitted"]], ["new.md"])
        self.assertEqual(snap["uncommitted"][0]["sha256"], sa.sha256_text("draft"))

    def test_original_external_radars_are_discoverable_without_an_advisor_addressee(self) -> None:
        with tempfile.TemporaryDirectory(prefix="sadv_radar_") as name:
            root = Path(name)
            folder = root / "disease-models/wwox/research/drug_repurposing/radar_inputs_fixture"
            folder.mkdir(parents=True)
            addressed = folder / "operator_scout_report.md"
            addressed.write_text("For Plan: compare a public method.\n", encoding="utf-8")
            unaddressed = folder / "drug_report.md"
            unaddressed.write_text("An unresolved mechanism and a possible comparison.\n", encoding="utf-8")
            saved, sa.ROOT = sa.ROOT, root
            try:
                rows = {r["id"]: r for r in sa.entrypoints()}
                discovered = {p for pattern in rows["radar_science"]["patterns"] for p in sa._resolve(pattern)}
                self.assertEqual(rows["radar_science"]["matches"], 2)
                self.assertIn(addressed, discovered)
                self.assertIn(unaddressed, discovered)
            finally:
                sa.ROOT = saved

    def test_entry_points_cover_the_required_sources_and_resolve(self) -> None:
        rows = {r["id"]: r for r in sa.entrypoints()}
        for key in ("limits", "invariants", "dashboard", "investigations", "open_questions", "candidates", "packages", "diagnoses", "memory_dismissals", "radar_science", "harness_scouting", "capability_surface"):
            self.assertIn(key, rows)
        self.assertGreater(rows["invariants"]["matches"], 0)
        # the weekly scouting tables are one stale pattern and the live feed an absolute host-cache path: they must be told apart, not blended into SKILLS.md's date
        self.assertTrue(any(p.endswith("scout_daily_briefing.md") for p in rows["harness_scouting"]["patterns"]))
        self.assertTrue(any("dream" in p and "drug_repurposing" in p for p in rows["diagnoses"]["patterns"]))
        self.assertTrue(any("radar_" in p for p in rows["radar_science"]["patterns"]))

    def test_a_large_file_is_marked_with_its_size_and_a_small_one_is_not(self) -> None:
        tmp, _ = _git_repo()
        (tmp / "big.md").write_text("x" * 25000, encoding="utf-8")
        saved, sa.ROOT = sa.ROOT, tmp
        try:
            with mock_entry_points([("probe", "probe", ["big.md", "tracked.md"]), ("quiet", "quiet", ["tracked.md"])]):
                text = sa.render_entrypoints(sa.entrypoints())
        finally:
            sa.ROOT = saved
        self.assertIn("`big.md` (25,000 bytes)", text)
        self.assertEqual(text.count("bytes)"), 1)  # tracked.md is far below the threshold


class Meeting(unittest.TestCase):
    """Behavioural controls: cadence/event retention without a model or new scheduler."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="legend_meeting_test_")
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.campaign = root / "campaign"
        self.campaign.mkdir()
        self.roadmap = root / "roadmap.md"
        self.roadmap.write_text(sa.ROADMAP_BEGIN + "\nResearch\n" + sa.ROADMAP_END)
        for name, value in {"ROOT": root, "ROADMAP": self.roadmap, "STATE_DIR": root / "state",
                            "_git": lambda *a: "snapshot-sha", "_records": lambda: {"SCI-X": {
                                "owner": "scientist-a", "state": "OPEN", "verdict": "CONTINUE", "path": "ledger/tasks/scientist-a/SCI-X.json"}}}.items():
            replacement = patch.object(sa, name, value)
            replacement.start(); self.addCleanup(replacement.stop)
        clock = patch.dict(os.environ, {"LEGEND_ADVISOR_NOW": "2026-11-15T01:00:00Z"})
        clock.start(); self.addCleanup(clock.stop)
        (self.campaign / "budget.json").write_text(json.dumps({"activated_utc": "2026-11-15T00:00:00Z", "max_invocations": 3}))
        self.mode = self.campaign / sa.CONTINUOUS
        self.mode.write_text(json.dumps({"authorised_utc": "2026-11-15T00:00:00Z"}))

    def at(self, stamp: str) -> None:
        os.environ["LEGEND_ADVISOR_NOW"] = stamp

    def request(self, source: str = "package/result.md", reason: str = "a shared premise changed") -> dict:
        return sa.meeting(self.campaign, request=reason, source=source, actor="science")

    def close(self, notes: str = "Science replied; Harness not consulted. Continue SCI-X; no new assignment.") -> dict:
        path = Path(self.tmp.name) / "notes.md"
        path.write_text(notes)
        return sa.meeting(self.campaign, close_file=path)

    def test_exact_six_hour_boundary_and_next_cadence_is_from_start_not_close(self) -> None:
        self.at("2026-11-15T05:14:59Z")
        self.assertEqual(sa.meeting_status(self.campaign)["state"], "IDLE")
        self.at("2026-11-15T05:59:59Z")
        self.assertEqual(sa.meeting_status(self.campaign)["state"], "DUE_SOON")                          # inside the 45-minute lead: actionable now
        self.at("2026-11-15T06:00:00Z")
        self.assertEqual(sa.meeting_status(self.campaign)["state"], "DUE")
        self.assertTrue(sa.meeting_status(self.campaign)["actionable"])
        sa.meeting(self.campaign, open_round=True)
        self.at("2026-11-15T07:00:00Z")
        self.close()
        self.at("2026-11-15T11:14:59Z")
        self.assertEqual(sa.meeting_status(self.campaign)["state"], "IDLE")
        self.at("2026-11-15T12:00:00Z")
        self.assertEqual(sa.meeting_status(self.campaign)["state"], "DUE")

    def test_a_meeting_due_within_the_lead_is_opened_early_once_and_the_cadence_moves_by_at_most_the_lead(self) -> None:
        """2026-11-20: a meeting due at 12:18:14 met an hourly check that fires at about :17 to :18; DUE_SOON lets the check before it open the round."""
        self.at("2026-11-15T05:30:00Z")
        status = sa.meeting_status(self.campaign)
        self.assertEqual((status["state"], status["actionable"]), ("DUE_SOON", True))
        self.assertIn("within 45 minutes", status["why"])
        record = sa.meeting(self.campaign, open_round=True)["record"]
        self.assertTrue(record)
        self.assertEqual(sa.meeting(self.campaign, open_round=True)["record"], record)                  # one round, not one per check
        self.at("2026-11-15T06:00:00Z")
        self.close()
        self.at("2026-11-15T10:44:59Z")
        self.assertEqual(sa.meeting_status(self.campaign)["state"], "IDLE")                              # next due 11:30 (started 05:30) minus the lead is 10:45
        self.at("2026-11-15T10:45:00Z")
        self.assertEqual(sa.meeting_status(self.campaign)["state"], "DUE_SOON")

    def test_event_anticipates_cadence_and_duplicate_sends_do_not_multiply_rounds(self) -> None:
        first = self.request()
        self.assertEqual(first["state"], "DUE")
        self.assertEqual(self.request()["requests"], first["requests"])
        record = sa.meeting(self.campaign, open_round=True)["record"]
        self.assertEqual(sa.meeting(self.campaign, open_round=True)["record"], record)
        self.assertEqual(len(list((self.campaign / "meetings").glob("*.md"))), 1)
        self.close()
        self.assertEqual(self.request()["state"], "IDLE")
        self.assertEqual(self.request("package/revised.md")["state"], "DUE")

    def test_new_request_during_round_survives_closure(self) -> None:
        self.request()
        sa.meeting(self.campaign, open_round=True)
        later = self.request("harness/issue.md", "a second shared blocker")
        self.assertEqual(len(later["requests"]), 2)
        result = self.close()
        self.assertEqual(result["state"], "DUE")
        self.assertEqual([r["source"] for r in result["requests"]], ["harness/issue.md"])

    def test_concurrent_signals_and_an_evaluation_save_do_not_erase_requests(self) -> None:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=3) as pool:
            list(pool.map(lambda n: self.request(f"result/{n}.md"), [0, 1, 2, 0, 1, 2]))
        sa._save_state(self.campaign, {"last_outcome": {"outcome": "continue"}})
        self.assertEqual(len(sa.meeting_status(self.campaign)["requests"]), 3)

    def test_round_table_is_derived_not_a_false_consultation_or_task_completion(self) -> None:
        self.request()
        opened = sa.meeting(self.campaign, open_round=True)
        text = Path(opened["record"]).read_text()
        self.assertIn("not participant statements", text)
        self.assertIn("not yet consulted", text)
        self.assertIn("ledger/tasks/scientist-a/SCI-X.json", text)
        notes = "  Science: read result.\nHarness: unavailable.\nDecision: retain SCI-X.\n"
        self.close(notes)
        self.assertIn(notes, Path(opened["record"]).read_text())
        self.assertFalse((self.campaign / "assignments.jsonl").exists())

    def test_pause_disabled_resources_and_running_evaluation_preserve_pending_signal(self) -> None:
        self.request()
        for name, change in (
            ("pause", lambda: self.roadmap.write_text(sa.ROADMAP_BEGIN + "\nPAUSE: all — test\n" + sa.ROADMAP_END)),
            ("disabled", lambda: (self.campaign / "DISABLED").write_text("test")),
            ("off", lambda: self.mode.write_text(json.dumps({"authorised_utc": "2026-11-15T00:00:00Z", "meeting_enabled": False}))),
        ):
            with self.subTest(name=name):
                change()
                self.assertEqual(sa.meeting(self.campaign, open_round=True)["state"], "HELD")
                self.assertFalse((self.campaign / "meetings").exists())
                self.roadmap.write_text(sa.ROADMAP_BEGIN + "\nResearch\n" + sa.ROADMAP_END)
                (self.campaign / "DISABLED").unlink(missing_ok=True)
                self.mode.write_text(json.dumps({"authorised_utc": "2026-11-15T00:00:00Z"}))
        with patch.object(sa, "weekly_state", return_value={"state": "exhausted", "advisor_spent": 10, "advisor_cap": 10, "unit": "output_tokens"}):
            self.assertEqual(sa.meeting(self.campaign, open_round=True)["state"], "HELD")
        with patch.object(sa, "_running", return_value=True):
            self.assertEqual(sa.meeting(self.campaign, open_round=True)["state"], "HELD")
        self.assertEqual(len(sa.meeting_status(self.campaign)["requests"]), 1)
        self.assertEqual(sa.meeting(self.campaign, open_round=True)["state"], "OPEN")

    def test_bounded_pilot_is_not_extended_and_counters_are_not_changed(self) -> None:
        before = (self.campaign / "budget.json").read_text()
        self.mode.unlink()
        self.at("2026-11-16T00:00:00Z")
        self.request()
        self.assertEqual(sa.meeting(self.campaign, open_round=True)["state"], "HELD")
        self.assertEqual((self.campaign / "budget.json").read_text(), before)
        self.assertFalse((self.campaign / "invocations.jsonl").exists())

    def test_new_host_recovers_open_and_closed_rounds_from_minutes(self) -> None:
        self.request()
        opened = sa.meeting(self.campaign, open_round=True)
        cache = sa._state_path(self.campaign).with_name("meeting.json")
        cache.unlink()
        recovered = sa.meeting(self.campaign, open_round=True)
        self.assertEqual(recovered["record"], opened["record"])
        self.assertTrue(recovered["recovery"])
        self.close()
        cache.unlink()
        self.assertEqual(sa.meeting_status(self.campaign)["state"], "IDLE")

    def test_recovery_selects_the_latest_round_even_with_two_starts_in_one_second(self) -> None:
        self.request()
        first = sa.meeting(self.campaign, open_round=True)["record"]
        self.close()
        self.request("result/revised.md")
        second = sa.meeting(self.campaign, open_round=True)["record"]
        self.assertNotEqual(first, second)
        sa._state_path(self.campaign).with_name("meeting.json").unlink()
        self.assertEqual(sa.meeting_status(self.campaign)["record"], second)
        # File times do not order two records written within one filesystem tick (this test was red once in a loaded landing run, 2026-11-25):
        # give the closed record the later time, and the open one must still be recovered.
        later = os.stat(second).st_mtime_ns + 1_000_000_000
        os.utime(first, ns=(later, later))
        self.assertEqual(sa.meeting_status(self.campaign)["record"], second)

    def test_empty_notes_invalid_requests_and_missing_open_record_are_honest_errors(self) -> None:
        with self.assertRaises(ValueError):
            sa.meeting(self.campaign, request="event", actor="science")
        self.request()
        opened = sa.meeting(self.campaign, open_round=True)
        with self.assertRaises(ValueError):
            self.close(" ")
        Path(opened["record"]).unlink()
        with self.assertRaisesRegex(ValueError, "missing or invalid"):
            sa.meeting(self.campaign, open_round=True)

    def test_due_meeting_survives_an_ordinary_none_without_launching_a_model(self) -> None:
        sa._save_state(self.campaign, {"last_evaluation_utc": "2026-11-15T00:00:00Z", "last_outcome": {
            "stated": True, "outcome": "wait", "reason": "real resource outside this branch", "resume_when": "event"}})
        obs = {"main_sha": "snapshot-sha", "roadmap_sha256": "r", "commits_since_last_tick": 0, "events": [],
               "open_mandates": [], "mandates": {}, "waits": [], "queue": {"exhausted": True}, "sessions": {},
               "portfolio": {"path": "p", "available": False, "actionable": [], "errors": []}}
        self.at("2026-11-15T06:00:00Z")
        with patch.object(sa, "observe", return_value=obs), patch.object(sa, "run", side_effect=AssertionError("must not launch")):
            tick = sa.tick(self.campaign)
        self.assertEqual(tick["verdict"], "NONE")
        self.assertEqual(tick["meeting"]["state"], "DUE")
        cache = sa._state_path(self.campaign).with_name("meeting.json")
        cache.write_text("invalid JSON")
        with patch.object(sa, "observe", return_value=obs):
            self.assertEqual(sa.tick(self.campaign)["meeting"]["state"], "ERROR")


class OrdinaryWorkDoesNotNeedIt(unittest.TestCase):
    def test_ordinary_tools_do_not_require_the_advisor_and_measurement_only_reads_it(self) -> None:
        here = Path(__file__).resolve().parent
        measurement_readers = {"trial_window_table.py": {"_agents", "incomplete_run", "mc"},
                               "debt_report.py": {"rotation_status", "assignment_states"}}
        for path in here.glob("*.py"):
            if path.name in ("strategic_advisor.py", "test_strategic_advisor.py"):
                continue
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
            imports = [node for node in ast.walk(tree) if
                       (isinstance(node, ast.Import) and any(a.name == "strategic_advisor" for a in node.names)) or
                       (isinstance(node, ast.ImportFrom) and node.module == "strategic_advisor")]
            if path.name in measurement_readers:
                # HE61 / ADV-221: a measurement tool reads existing metadata, runtime names and task verdicts.
                # It reuses the named readers and nothing else; it must never drive the Advisor or research.
                aliases = {a.asname or a.name for node in imports if isinstance(node, ast.Import)
                           for a in node.names if a.name == "strategic_advisor"}
                self.assertFalse(any(isinstance(node, ast.ImportFrom) for node in imports))
                attrs = {node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute)
                         and isinstance(node.value, ast.Name) and node.value.id in aliases}
                self.assertLessEqual(attrs, measurement_readers[path.name], path.name)
            else:
                self.assertFalse(imports, path.name)

if __name__ == "__main__":
    unittest.main(verbosity=2)
