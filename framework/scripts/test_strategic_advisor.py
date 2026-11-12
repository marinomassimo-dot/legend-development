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
        for key in ("limits", "invariants", "dashboard", "investigations", "open_questions", "candidates", "packages", "diagnoses", "memory_dismissals", "radar"):
            self.assertIn(key, rows)
        self.assertGreater(rows["invariants"]["matches"], 0)

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
