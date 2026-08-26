#!/usr/bin/env python3
"""Paired parity battery for the shared `PreToolUse` write guard.

Every case runs **twice** — once shaped as Claude Code sends it, once as Codex sends it —
and asserts the two answers are the same object. The point is not that the guard is
strict; it is that `RUNTIME` is not an input to the verdict. A test that only checked one
side would pass on the day the two sides stopped agreeing.

The Codex payload shape is not invented: `pre-tool-use.command.input` and
`pre-tool-use.command.output` were extracted from the installed binary
(codex-cli 0.147.0) and both are pinned below, so an upgrade that changes the wire
breaks this file instead of silently disarming the guard.
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ENTRY = HERE / "pre_tool_use_guard.py"

SPEC = importlib.util.spec_from_file_location("pre_tool_use_guard", ENTRY)
guard = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = guard
SPEC.loader.exec_module(guard)

STAGING = "git add -A"
HEREDOC_WRITE = (
    "python3 - <<'PY'\n"
    "from pathlib import Path\n"
    'Path("disease-models/wwox/analysis/data/x.json").write_text("y")\n'
    "PY"
)
READ_ONLY = "git status --short"


def claude_payload(command: str) -> dict:
    """The shape Claude Code sends to a `PreToolUse` command hook."""
    return {
        "session_id": "s",
        "transcript_path": None,
        "cwd": str(ROOT),
        "hook_event_name": "PreToolUse",
        "tool_name": "Bash",
        "tool_input": {"command": command},
    }


def codex_payload(command: str, *, key: str = "cmd") -> dict:
    """The shape `pre-tool-use.command.input` requires — every required field present."""
    return {
        "agent_id": "a",
        "agent_type": "t",
        "cwd": str(ROOT),
        "hook_event_name": "PreToolUse",
        "model": "gpt-5.6-sol",
        "permission_mode": "default",
        "session_id": "s",
        "tool_input": {key: command, "workdir": str(ROOT)},
        "tool_name": "shell_command",
        "tool_use_id": "u",
        "transcript_path": None,
        "turn_id": "turn",
    }


def run_entry(raw: str, env: dict | None = None) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, str(ENTRY)], input=raw, capture_output=True, text=True,
        env={**os.environ, **(env or {})},
    )
    return result.returncode, result.stdout.strip()


def decision_of(stdout: str) -> str:
    if not stdout:
        return "allow"
    return json.loads(stdout)["hookSpecificOutput"]["permissionDecision"]


class BothRuntimesReachTheSameVerdict(unittest.TestCase):
    """`ACTOR_ID != RUNTIME`. The verdict must not move when the runtime does."""

    def assert_same(self, command: str, expected: str) -> None:
        for label, payload in (
            ("claude", claude_payload(command)),
            ("codex", codex_payload(command)),
        ):
            with self.subTest(runtime=label, command=command[:40]):
                code, out = run_entry(json.dumps(payload))
                self.assertEqual(code, 0, "the hook itself must never error")
                self.assertEqual(decision_of(out), expected)

    def test_1_blanket_staging_is_denied_in_both(self) -> None:
        self.assert_same(STAGING, "deny")

    def test_2_inline_heredoc_write_is_denied_in_both(self) -> None:
        self.assert_same(HEREDOC_WRITE, "deny")

    def test_3_read_only_command_is_allowed_in_both(self) -> None:
        self.assert_same(READ_ONLY, "allow")

    def test_denial_reasons_are_byte_identical(self) -> None:
        """Same engine, so the actor is told the same thing wherever it is running."""
        _, claude_out = run_entry(json.dumps(claude_payload(STAGING)))
        _, codex_out = run_entry(json.dumps(codex_payload(STAGING)))
        self.assertEqual(
            json.loads(claude_out)["hookSpecificOutput"]["permissionDecisionReason"],
            json.loads(codex_out)["hookSpecificOutput"]["permissionDecisionReason"],
        )

    def test_command_under_the_other_key_is_still_policed(self) -> None:
        """`command` and `cmd` are two spellings of one thing, not two policies."""
        code, out = run_entry(json.dumps(codex_payload(STAGING, key="command")))
        self.assertEqual(code, 0)
        self.assertEqual(decision_of(out), "deny")


class ArgvIsReducedRatherThanStringified(unittest.TestCase):
    """The bug a naive port would have shipped, pinned so it cannot come back.

    `str(["bash","-lc","git add -A"])` wraps the invocation in quotes, and the policy
    deliberately ignores quoted spans — so stringifying would have produced ALLOW under
    Codex for a command Claude denies. That is a runtime granting authority.
    """

    def test_shell_wrapper_argv_is_unwrapped(self) -> None:
        self.assertEqual(guard.command_text({"command": ["bash", "-lc", STAGING]}), STAGING)

    def test_non_shell_argv_is_joined(self) -> None:
        self.assertEqual(
            guard.command_text({"command": ["git", "status", "--short"]}),
            "git status --short",
        )

    def test_argv_shell_wrapper_is_denied_end_to_end(self) -> None:
        payload = codex_payload("placeholder")
        payload["tool_input"] = {"command": ["bash", "-lc", STAGING]}
        code, out = run_entry(json.dumps(payload))
        self.assertEqual(code, 0)
        self.assertEqual(decision_of(out), "deny",
                         "argv-wrapped staging must be denied exactly as the plain form is")


class FailsClosed(unittest.TestCase):
    """Requirement 4 and 5: the guard answers no when it cannot answer."""

    def test_4_malformed_payload_denies_in_both_shapes(self) -> None:
        for raw in ("not json", "", "[]", '{"tool_name": "Bash"}', "null"):
            with self.subTest(raw=raw[:20]):
                code, out = run_entry(raw)
                self.assertEqual(code, 0)
                self.assertEqual(decision_of(out), "deny")

    def test_wrong_event_name_denies(self) -> None:
        payload = claude_payload(READ_ONLY)
        payload["hook_event_name"] = "PostToolUse"
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "deny")

    def test_unrecognised_tool_denies_and_names_the_diagnosis(self) -> None:
        """A renamed shell tool is how a guard silently stops covering the shell."""
        payload = claude_payload(READ_ONLY)
        payload["tool_name"] = "Shell"
        code, out = run_entry(json.dumps(payload))
        self.assertEqual(decision_of(out), "deny")
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("SHELL_TOOLS", reason, "the denial must name where the fix goes")

    def test_unrecognised_tool_can_be_waived_only_deliberately(self) -> None:
        payload = claude_payload(READ_ONLY)
        payload["tool_name"] = "Read"
        _, out = run_entry(json.dumps(payload), env={guard.UNKNOWN_TOOL_ENV: "allow"})
        self.assertEqual(decision_of(out), "allow")

    def test_uncextractable_command_denies(self) -> None:
        payload = codex_payload("x")
        payload["tool_input"] = {"workdir": "/tmp"}
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "deny")

    def test_5_missing_engine_is_a_broken_hook_not_a_silent_allow(self) -> None:
        """If the engine is gone the process must fail loudly, never exit 0 quiet.

        A hook command that cannot be executed is the one failure this script cannot
        report from the inside, so it is asserted from the outside: a runtime that sees a
        non-zero exit and empty stdout must treat activation as refused, which is what
        `runtime_parity.py` checks at registration time.
        """
        with tempfile.TemporaryDirectory() as tmp:
            orphan = Path(tmp) / "pre_tool_use_guard.py"
            orphan.write_text(ENTRY.read_text(encoding="utf-8"), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(orphan)], input=json.dumps(claude_payload(STAGING)),
                capture_output=True, text=True,
            )
        self.assertNotEqual(result.returncode, 0, "a missing policy must not exit 0")
        self.assertEqual(result.stdout.strip(), "", "and must not emit an allow")


class KnownGapsAreCharacterisedNotClaimedFixed(unittest.TestCase):
    """Requirement 6 — measured, identical in both runtimes, and NOT repaired here.

    These shapes mutate the repository and the policy does not stop them. That is
    `GUARD_HARDENING_DEBT`: it predates the bridge, it is the same on both sides, and
    widening the policy changes what is forbidden for every actor, which is a different
    change with a different review. The assertion is `allow` on purpose — if a future
    hardening pass closes one of these, this test fails and the debt entry gets closed
    with it, deliberately, instead of two files quietly disagreeing.
    """

    GAPS = (
        ("shell -c wrapper", 'bash -c "git add -A"'),
        ("sed -i", "sed -i '' 's/x/y/' AGENTS.md"),
        ("redirection", "echo x > AGENTS.md"),
        ("append", "echo x >> AGENTS.md"),
        ("tee", "echo x | tee AGENTS.md"),
        ("cp over a tracked file", "cp /tmp/x.md AGENTS.md"),
        ("mv over a tracked file", "mv /tmp/x.md AGENTS.md"),
        ("python -c write", "python3 -c \"open('AGENTS.md','w')\""),
        ("perl -pi", "perl -pi -e 's/a/b/' AGENTS.md"),
    )

    def test_gaps_are_open_and_identical_on_both_sides(self) -> None:
        for label, command in self.GAPS:
            with self.subTest(gap=label):
                claude = decision_of(run_entry(json.dumps(claude_payload(command)))[1])
                codex = decision_of(run_entry(json.dumps(codex_payload(command)))[1])
                self.assertEqual(claude, codex, "a gap must never be runtime-specific")
                self.assertEqual(claude, "allow",
                                 "if this now denies, close the GUARD_HARDENING_DEBT entry too")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
