#!/usr/bin/env python3
"""Plumbing tests for strategic_advisor.py, with a stand-in for the `claude` binary.

These show the snapshot, the neutral brief, the capture path, Stage B reading the saved Stage A,
the attempt ceilings and the check. They do not show that a model obeys its brief; the one real
call is the smoke invocation recorded in the build report.
"""

from __future__ import annotations

import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import strategic_advisor as sa  # noqa: E402

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


class Proactive(Base):
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
        brief = (self.campaign / "brief_P.md").read_text(encoding="utf-8")
        self.assertIn("delivery:", brief)                                       # the tick advanced its own state; the brief must still carry what triggered the evaluation (seen empty in the first pilot)
        self.assertNotIn('"commits_since_last_tick": 0', brief)
        self.at("2026-11-13T13:00:00Z")
        self.assertEqual(sa.tick(self.campaign)["verdict"], "NONE")             # the digest of those events was already evaluated

    def test_a_linked_worktree_refuses_to_become_a_second_campaign_and_the_recall_text_is_one(self) -> None:
        wt = self.tmp / "linked"; wt.mkdir(); (wt / ".git").write_text("gitdir: /elsewhere\n", encoding="utf-8")
        saved, sa.ROOT = sa.ROOT, wt
        try:
            for cmd in ("tick", "evaluate", "deliver", "activate", "disable", "recall"):
                self.assertTrue(sa.primary_refusal(), cmd)
            self.assertEqual(sa.main(["tick", "--campaign", str(self.campaign)]), 2)      # refused before it touches any state
        finally:
            sa.ROOT = saved
        self.assertEqual(sa.primary_refusal(), "")                                   # the primary checkout has a .git directory
        text = sa.recall_prompt(self.campaign)
        self.assertIn(sa.RECALL_MARK, text)
        self.assertEqual(text.count("--campaign"), 2)                                   # tick and evaluate, the same campaign

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
        sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "SENT", "--evidence", "msg 123", "--to", "SCI"])
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
        base = ["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "SENT", "--evidence", "msg 1"]
        self.assertEqual(sa.main(base + ["--to", "HE"]), 2)                                                 # the receipt names HE: not a delivery to SCI
        self.assertEqual(sa.main(base), 2)                                                                  # no receipt at all: the text of a message is not one
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "DRAFTED")
        self.assertEqual(sa.main(base + ["--to", "HE", "--to", "sci"]), 0)                                  # two real sends, one of them to the session in question
        self.assertEqual(sa.assignment_states(self.campaign)["ADV-001"]["highest"], "SENT")
        self.assertIn('"to": ["HE", "sci"]', (self.campaign / "assignments.jsonl").read_text(encoding="utf-8"))
        self.assertEqual(sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "UNREACHABLE", "--evidence", "no live session"]), 0)   # no receipt exists for that
        self.assertEqual(sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-099", "--state", "SENT", "--evidence", "x", "--to", "SCI"]), 2)   # not a drafted assignment

    def test_the_senders_own_records_never_count_as_a_recipient_taking_or_executing_an_assignment(self) -> None:
        os.environ["FAKE_MODE"] = "assign"; sa.evaluate(self.campaign)
        sa.main(["deliver", "--campaign", str(self.campaign), "--id", "ADV-001", "--state", "SENT", "--evidence", "msg 123", "--to", "SCI"])
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
        self.assertEqual((t["verdict"], t["why"]), ("EVALUATE", "roadmap changed"))     # an operator update anticipates the four-hour rhythm
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
        text = (self.campaign / "brief_P.md").read_text(encoding="utf-8")
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
        self.assertIn("legitimate wait", sa.recall_prompt(self.campaign))

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
        self.assertIn("PAUSE: science", (self.campaign / "brief_P.md").read_text(encoding="utf-8"))
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


class OrdinaryWorkDoesNotNeedIt(unittest.TestCase):
    def test_no_other_script_imports_the_advisor_tool(self) -> None:
        here = Path(__file__).resolve().parent
        for path in here.glob("*.py"):
            if path.name in ("strategic_advisor.py", "test_strategic_advisor.py"):
                continue
            self.assertNotIn("strategic_advisor", path.read_text(encoding="utf-8", errors="replace"), path.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
