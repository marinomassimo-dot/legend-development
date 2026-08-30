#!/usr/bin/env python3
"""Regressions for the Bash PreToolUse guard, as Claude Code registers it.

Every DENY case below is a command shape that actually ran in this repository and
caused damage, or a wrapper around one. Every ALLOW case is a shape that must keep
working, because a guard that blocks ordinary work gets disabled and then guards nothing.

This is the **Claude side** of the parity battery deliberately: it exercises the policy
through `scripts/guard_bash_command.py`, the path `.claude/settings.json` actually names,
so a change that reaches the engine but not this entry point fails here.
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location("guard", HERE / "guard_bash_command.py")
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


def verdict(command: str):
    """Judge as the hook does from this repository: a real cwd, root and ASSIGNMENT.

    🔴 `assigned=` is stated, and stating it is the revision-10 discipline. The
    assignment is session-bound, so a suite that omitted it would be judged under
    whatever `CLAUDE_PROJECT_DIR` this process inherited — the session's own worktree
    under `python -m unittest`, and nothing at all under a runner that clears the
    environment. Both answers are wrong for a suite about this repository, and the
    second denies every positive control with `SESSION_ASSIGNMENT_UNDERIVABLE`, which
    would look like a policy result.
    """
    return guard.verdict(command, cwd=str(ROOT), repo_root=str(ROOT),
                         assigned=str(ROOT))


HEREDOC_WRITE = (
    "python3 - <<'PY'\n"
    "from pathlib import Path\n"
    'Path("disease-models/wwox/analysis/data/x.json").write_text("y")\n'
    "PY"
)
HEREDOC_TEMP_WRITE = (
    "python3 - <<'PY'\n"
    "from pathlib import Path\n"
    'Path("/tmp/claude-501/scratchpad/x.txt").write_text("y")\n'
    "PY"
)
HEREDOC_READ_ONLY = (
    "python3 - <<'PY'\n"
    "import json\n"
    'print(json.load(open("DATA_SOURCES.md")))\n'
    "PY"
)


class BlanketStagingIsBlocked(unittest.TestCase):
    """`git add -A` swept another actor's in-flight work into an unrelated commit."""

    def test_denied_shapes(self) -> None:
        for command in (
            "git add -A",
            "git add -A && git commit -m x",
            "git add --all",
            "git add .",
            'git commit -am "message"',
            "git commit -a",
            "git commit --all",
            'bash -c "git add -A"',
            "git -C /tmp/elsewhere add -A",
            "git ls-files | xargs git add",
        ):
            with self.subTest(command=command):
                self.assertIsNotNone(verdict(command), "should have been denied")

    def test_quoted_mention_is_not_an_invocation(self) -> None:
        """The guard blocked the commit that documented it. A quote is not a command.

        🔴 The third case used to end `>> notes.txt` and expected ALLOW. That redirect is
        now a repository write and is denied on its own merits, which is a different
        property from the one this test is about — so the redirect is gone rather than the
        expectation being flipped. The mention-is-not-an-invocation property is unchanged,
        and it is now structural: the quoted span is an argument to `echo`, not a script.
        """
        for command in (
            'git commit -m "git add -A staged another actor\'s work"',
            "git commit -m 'do not use git add --all here'",
            'echo "git commit -a is blocked"',
            "grep -rn 'git add -A' framework/",
        ):
            with self.subTest(command=command):
                self.assertIsNone(verdict(command),
                                  "a mention inside quotes must not be denied")

    def test_named_paths_are_allowed(self) -> None:
        for command in (
            "git add scripts/foo.py framework/scripts/bar.py",
            'git commit -m "message"',
            "git status --short",
            "git add disease-models/wwox/analysis/data/x.json",
            "git diff --stat",
        ):
            with self.subTest(command=command):
                self.assertIsNone(verdict(command), "ordinary work must not be blocked")


class ShellWritesOntoRepositoryFilesAreBlocked(unittest.TestCase):
    """The Write tool's read-before-overwrite guard was bypassed from the shell."""

    def test_repository_write_is_denied(self) -> None:
        self.assertIsNotNone(verdict(HEREDOC_WRITE))

    def test_json_dump_to_repository_file_is_denied(self) -> None:
        command = (
            "python3 - <<'PY'\n"
            "import json\n"
            'json.dump(d, open("DATA_SOURCES.md", "w"))\n'
            "PY"
        )
        self.assertIsNotNone(verdict(command))

    def test_every_shell_shaped_write_onto_a_tracked_file_is_denied(self) -> None:
        for command in (
            "echo x > AGENTS.md",
            "echo x >> AGENTS.md",
            "echo x | tee AGENTS.md",
            "sed -i '' 's/a/b/' AGENTS.md",
            "cp /tmp/x.md AGENTS.md",
            "mv /tmp/x.md AGENTS.md",
            "rm AGENTS.md",
            "truncate -s 0 AGENTS.md",
            "perl -pi -e 's/a/b/' AGENTS.md",
            "python3 -c \"open('AGENTS.md','w')\"",
        ):
            with self.subTest(command=command):
                self.assertIsNotNone(verdict(command),
                                     "the shape does not matter; the write does")

    def test_read_only_heredoc_is_allowed(self) -> None:
        self.assertIsNone(verdict(HEREDOC_READ_ONLY))

    def test_scratchpad_write_is_allowed(self) -> None:
        """Temp work is not what went wrong."""
        self.assertIsNone(verdict(HEREDOC_TEMP_WRITE))

    def test_committed_script_by_name_is_allowed(self) -> None:
        command = (
            "python3 disease-models/wwox/analysis/scripts/derive_dismech_sidecar.py "
            "--out disease-models/wwox/analysis/data/sidecar.jsonl"
        )
        self.assertIsNone(verdict(command), "invoking a reviewed script must work")


class HookContract(unittest.TestCase):
    """The guard is only useful if the harness understands its answer."""

    def _run(self, command: str):
        payload = json.dumps({"tool_name": "Bash", "cwd": str(ROOT),
                              "tool_input": {"command": command}})
        # 🔴 The assignment travels in the ENVIRONMENT, never in the payload — that
        # separation is the revision-10 repair, and a suite that put it in the payload
        # would be testing the shape the repair removed. Without it every denial here
        # would read `SESSION_ASSIGNMENT_UNDERIVABLE`, which is a true answer to a
        # different question, and the way-forward assertions below would fail for a
        # reason that has nothing to do with what they check.
        env = {**os.environ, "LEGEND_ASSIGNED_WORKTREE": str(ROOT)}
        env.pop("CLAUDE_PROJECT_DIR", None)
        result = subprocess.run(
            [sys.executable, str(HERE / "guard_bash_command.py")],
            input=payload, capture_output=True, text=True, env=env,
        )
        return result.returncode, result.stdout.strip()

    def test_a_denial_carries_the_generation_that_emitted_it(self) -> None:
        """🔴 R2. Every denial ends with a token the legacy guard does not contain.

        The revision-9 probe named `"Blanket staging is blocked in this repository."` as
        the sentence that proves the hook fired. It is BYTE-IDENTICAL in the legacy
        single-file guard on `main`, so the probe could have reported FIRING while
        measuring the engine this candidate replaces.
        """
        _, out = self._run("git add -A")
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("LEGEND_GUARD GENERATION=REV12", reason)
        self.assertIn("DECISION_CODE=BLANKET_STAGING", reason)
        self.assertIn("ASSIGNED_WORKTREE_SOURCE=OPERATOR_ENV", reason)

    def test_a_wrapped_blanket_staging_keeps_the_code_that_names_the_harm(self) -> None:
        """🔴 Revision 11, and it closes a hole revision 11 itself opened (`M06`).

        `bash -c $'git add -A'` is ANSI-C quoting: the `$` is syntax, not part of the
        word, and without `ANSI_C_QUOTE` the line parses as a program called `$git`. At
        revision 10 removing that substitution flipped the verdict to ALLOW and the
        mutation died. At revision 11 the verdict SURVIVES — `unclassified()` refuses an
        unstateable program name — so the mutant lived, because nothing asserted the
        DECISION CODE.

        The verdict is not the whole guarantee. `BLANKET_STAGING` is the sentence the
        actor has already learned for this harm, the probe reads decision codes to
        identify which engine answered, and this policy's own rule is that a denial which
        does not name the hazard is a denial the reader will try to route around. So the
        code is asserted, not merely the refusal.

        Verified as a discriminator before being written: it HOLDS on the real tree and
        FAILS with `ANSI_C_QUOTE.sub` removed.
        """
        for command in ("bash -c $'git add -A'", "sh -c $'git add -A'"):
            with self.subTest(command=command):
                _, out = self._run(command)
                reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
                self.assertIn("DECISION_CODE=BLANKET_STAGING", reason)

    def test_denial_emits_a_deny_decision_with_a_reason(self) -> None:
        code, out = self._run("git add -A")
        self.assertEqual(code, 0, "the hook itself must not error")
        decision = json.loads(out)["hookSpecificOutput"]
        self.assertEqual(decision["hookEventName"], "PreToolUse")
        self.assertEqual(decision["permissionDecision"], "deny")
        self.assertIn("git add <path>", decision["permissionDecisionReason"],
                      "a denial must name the alternative, or it just obstructs")

    def test_every_denial_names_a_way_forward(self) -> None:
        """A guard that only says no teaches its actors to route around it."""
        for command in ("git add -A", "echo x > AGENTS.md", 'echo x > "$UNKNOWN/f"',
                        "git ls-files | xargs rm"):
            with self.subTest(command=command):
                _, out = self._run(command)
                reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
                self.assertTrue(
                    any(hint in reason for hint in
                        ("git add <path>", "Write or Edit", "Write/Edit")),
                    f"denial for {command!r} names no alternative")

    def test_allowed_command_emits_nothing(self) -> None:
        code, out = self._run("git status --short")
        self.assertEqual(code, 0)
        self.assertEqual(out, "")

    def test_malformed_payload_fails_closed(self) -> None:
        """🔴 REVERSED on 2026-08-26, and the reversal is the point of the change.

        This assertion read `test_malformed_payload_never_blocks` and pinned the
        opposite behaviour: stdin that did not parse produced no output, and the command
        ran. That was defensible while one runtime registered the guard — a malformed
        payload then meant a harness bug, and blocking every command on a harness bug is
        worse than the bug. It stops being defensible the moment a second runtime
        registers the same engine, because "the payload did not parse" becomes
        indistinguishable from "this runtime's payload is shaped differently", and the
        fail-open answer hands the unrecognised runtime a guard that says yes to
        everything. A guard that cannot read its input does not know the command is safe.
        """
        result = subprocess.run(
            [sys.executable, str(HERE / "guard_bash_command.py")],
            input="not json", capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, "a denial is not an error")
        decision = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual(decision["permissionDecision"], "deny")
        self.assertIn("did not parse as JSON", decision["permissionDecisionReason"])


class TheRegistrationNamesThisEntryPoint(unittest.TestCase):
    """A guard nobody registers is a file, and this is where that goes wrong quietly."""

    def test_claude_settings_registers_this_script_on_bash(self) -> None:
        settings = json.loads((ROOT / ".claude" / "settings.json").read_text(encoding="utf-8"))
        groups = settings.get("hooks", {}).get("PreToolUse", [])
        self.assertTrue(groups, "no PreToolUse hook is registered for Claude")
        commands = json.dumps(groups)
        self.assertIn("guard_bash_command.py", commands)
        self.assertTrue(any(g.get("matcher") == "Bash" for g in groups),
                        "the Bash matcher is what puts this guard on the shell")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
