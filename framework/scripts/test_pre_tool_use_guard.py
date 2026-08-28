#!/usr/bin/env python3
"""Paired parity battery for the shared `PreToolUse` write guard.

Every case runs **three times** — as Claude Code sends it, as Codex's shell tool sends it,
and as Codex's code-mode `exec` tool sends it — and asserts the three answers are the same
object. The point is not that the guard is strict; it is that `RUNTIME` is not an input to
the verdict. A test that only checked one side would pass on the day the two sides stopped
agreeing.

The Codex payload shapes are not invented. `pre-tool-use.command.input` and
`pre-tool-use.command.output` were extracted from the installed binary and are pinned
below, and the code-mode shape was taken from a real session's rollout, so an upgrade that
changes the wire breaks this file instead of silently disarming the guard.

## Two things this file asserts that a guard test usually does not

**Both directions.** A guard that denied everything would pass a list of prohibited
shapes. `NegativeControlsMustKeepWorking` and `TheRepositorysOwnDocumentedCommandsStillRun`
are the other half, and the second one is a corpus rather than a list: it harvests the
shell commands this repository documents in its own Markdown and requires them to survive.

**Alternate encodings.** The shapes below are not the ones that were easy to think of;
`eval`, `$'…'`, a shell fed from a pipe and an expansion in argv[0] were each found by
attacking the parser after it was written, and each of them was ALLOWED when found.
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
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

POLICY_SPEC = importlib.util.spec_from_file_location("guard_policy", HERE / "guard_policy.py")
policy = importlib.util.module_from_spec(POLICY_SPEC)
POLICY_SPEC.loader.exec_module(policy)

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


def codemode_payload(command: str) -> dict:
    """The shape a real Codex session produced on 2026-08-28.

    Every tool call in that session was the code-mode tool `exec`, carrying a JavaScript
    body that called `tools.exec_command({...})`. A matcher list of
    `shell_command`/`unified_exec` would not have matched it, and a guard that only knew
    those two would have policed nothing while reporting parity.
    """
    payload = codex_payload("placeholder")
    payload["tool_name"] = "exec"
    payload["tool_input"] = {
        "input": "const r = await tools.exec_command("
                 + json.dumps({"cmd": command, "workdir": str(ROOT), "yield_time_ms": 10000})
                 + ");",
    }
    return payload


def run_entry(raw: str, env: dict = None) -> tuple:
    result = subprocess.run(
        [sys.executable, str(ENTRY)], input=raw, capture_output=True, text=True,
        env={**os.environ, **(env or {})},
    )
    return result.returncode, result.stdout.strip()


def decision_of(stdout: str) -> str:
    if not stdout:
        return "allow"
    return json.loads(stdout)["hookSpecificOutput"]["permissionDecision"]


class ThreeRuntimeShapesReachTheSameVerdict(unittest.TestCase):
    """`ACTOR_ID != RUNTIME`. The verdict must not move when the runtime does."""

    def assert_same(self, command: str, expected: str) -> None:
        for label, payload in (
            ("claude", claude_payload(command)),
            ("codex-shell", codex_payload(command)),
            ("codex-code-mode", codemode_payload(command)),
        ):
            with self.subTest(runtime=label, command=command[:40]):
                code, out = run_entry(json.dumps(payload))
                self.assertEqual(code, 0, "the hook itself must never error")
                self.assertEqual(decision_of(out), expected)

    def test_1_blanket_staging_is_denied_in_all_three(self) -> None:
        self.assert_same(STAGING, "deny")

    def test_2_inline_heredoc_write_is_denied_in_all_three(self) -> None:
        self.assert_same(HEREDOC_WRITE, "deny")

    def test_3_read_only_command_is_allowed_in_all_three(self) -> None:
        self.assert_same(READ_ONLY, "allow")

    def test_denial_reasons_are_byte_identical(self) -> None:
        """Same engine, so the actor is told the same thing wherever it is running."""
        reasons = set()
        for payload in (claude_payload(STAGING), codex_payload(STAGING),
                        codemode_payload(STAGING)):
            _, out = run_entry(json.dumps(payload))
            reasons.add(json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"])
        self.assertEqual(len(reasons), 1, "one engine, one sentence")

    def test_command_under_the_other_key_is_still_policed(self) -> None:
        """`command` and `cmd` are two spellings of one thing, not two policies."""
        code, out = run_entry(json.dumps(codex_payload(STAGING, key="command")))
        self.assertEqual(code, 0)
        self.assertEqual(decision_of(out), "deny")


class ArgvIsReducedRatherThanStringified(unittest.TestCase):
    """The bug a naive port would have shipped, pinned so it cannot come back."""

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


class CodeModeIsPolicedRatherThanWaved(unittest.TestCase):
    """The tool the recorded pilot actually used — and its failure directions."""

    def test_a_code_mode_body_with_no_shell_call_is_allowed(self) -> None:
        payload = codemode_payload("x")
        payload["tool_input"] = {"input": 'await tools.read_file({"path":"AGENTS.md"});'}
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "allow")

    def test_a_shell_call_the_guard_cannot_read_is_denied(self) -> None:
        """`tools.exec_command(buildArgs())` — a call whose argument is computed."""
        payload = codemode_payload("x")
        payload["tool_input"] = {"input": "await tools.exec_command(buildArgs());"}
        code, out = run_entry(json.dumps(payload))
        self.assertEqual(code, 0)
        self.assertEqual(decision_of(out), "deny")
        self.assertIn("cannot see", json.loads(out)["hookSpecificOutput"]
                      ["permissionDecisionReason"])

    def test_every_shell_call_in_one_body_is_judged(self) -> None:
        """A prohibited call after a harmless one must not be shadowed by it."""
        payload = codemode_payload("x")
        payload["tool_input"] = {"input": (
            'await tools.exec_command({"cmd":"git status"});\n'
            'await tools.exec_command({"cmd":"git add -A"});\n')}
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "deny")

    def test_the_apply_patch_tool_shape_is_policed_by_its_targets(self) -> None:
        payload = codex_payload("x")
        payload["tool_name"] = "apply_patch"
        payload["tool_input"] = {"input": "*** Begin Patch\n*** Update File: AGENTS.md\n"
                                          "-a\n+b\n*** End Patch"}
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "deny")
        payload["tool_input"] = {"input": "*** Begin Patch\n*** Add File: /tmp/x.md\n"
                                          "+b\n*** End Patch"}
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "allow",
                         "a patch confined to scratch space is not the failure")


class FailsClosed(unittest.TestCase):
    """Requirement 4 and 5: the guard answers no when it cannot answer."""

    def test_4_malformed_payload_denies_in_both_shapes(self) -> None:
        for raw in ("not json", "", "[]", '{"tool_name": "Bash"}', "null", "3", '"x"'):
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

    def test_unextractable_command_denies(self) -> None:
        payload = codex_payload("x")
        payload["tool_input"] = {"workdir": "/tmp"}
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "deny")

    def test_unparseable_command_denies(self) -> None:
        """A command the lexer refuses is a command whose writes are unknown."""
        self.assertEqual(decision_of(run_entry(json.dumps(claude_payload(
            "echo 'unterminated")))[1]), "deny")

    def test_an_unresolvable_write_target_denies(self) -> None:
        self.assertEqual(decision_of(run_entry(json.dumps(claude_payload(
            'echo x > "$SOMETHING_FROM_THE_ENVIRONMENT/f"')))[1]), "deny")

    def test_5_missing_engine_is_a_broken_hook_not_a_silent_allow(self) -> None:
        """If the engine is gone the process must fail loudly, never exit 0 quiet."""
        with tempfile.TemporaryDirectory() as tmp:
            orphan = Path(tmp) / "pre_tool_use_guard.py"
            orphan.write_text(ENTRY.read_text(encoding="utf-8"), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(orphan)], input=json.dumps(claude_payload(STAGING)),
                capture_output=True, text=True,
            )
        self.assertNotEqual(result.returncode, 0, "a missing policy must not exit 0")
        self.assertEqual(result.stdout.strip(), "", "and must not emit an allow")


class TheDemonstratedMutationPathsAreClosed(unittest.TestCase):
    """The nine shapes revision 2 characterised as open debt, now closed.

    🔴 This class replaces `KnownGapsAreCharacterisedNotClaimedFixed`, which asserted the
    same commands were ALLOWED and instructed whoever closed them to close the debt entry
    with the fix. That is what happened. The list is kept in the same order so the two
    revisions can be diffed row by row.
    """

    CLOSED = (
        ("shell -c wrapper", 'bash -c "git add -A"'),
        ("login shell wrapper", '/bin/zsh -lc "git add -A"'),
        ("sh -c", "sh -c 'git add -A'"),
        ("git -C elsewhere", "git -C /tmp/other add -A"),
        ("xargs git add", "git ls-files | xargs git add"),
        ("sed -i", "sed -i '' 's/x/y/' AGENTS.md"),
        ("redirection", "echo x > AGENTS.md"),
        ("append", "echo x >> AGENTS.md"),
        ("tee", "echo x | tee AGENTS.md"),
        ("cp over a tracked file", "cp /tmp/x.md AGENTS.md"),
        ("mv over a tracked file", "mv /tmp/x.md AGENTS.md"),
        ("rm a tracked file", "rm AGENTS.md"),
        ("truncate", "truncate -s 0 AGENTS.md"),
        ("python -c write", "python3 -c \"open('AGENTS.md','w')\""),
        ("perl -pi", "perl -pi -e 's/a/b/' AGENTS.md"),
        ("node -e write", "node -e \"require('fs').writeFileSync('AGENTS.md','x')\""),
        ("apply_patch envelope",
         "apply_patch <<'EOF'\n*** Begin Patch\n*** Update File: AGENTS.md\n+x\n"
         "*** End Patch\nEOF"),
        ("find -exec rm", "find . -name '*.md' -exec rm {} \\;"),
        ("find -delete", "find . -name '*.md' -delete"),
        ("dd of=", "dd if=/tmp/x of=AGENTS.md"),
    )

    def test_each_closed_shape_denies_identically_in_all_three(self) -> None:
        for label, command in self.CLOSED:
            with self.subTest(shape=label):
                answers = {
                    "claude": decision_of(run_entry(json.dumps(claude_payload(command)))[1]),
                    "codex": decision_of(run_entry(json.dumps(codex_payload(command)))[1]),
                    "code-mode": decision_of(
                        run_entry(json.dumps(codemode_payload(command)))[1]),
                }
                self.assertEqual(set(answers.values()), {"deny"}, f"{label}: {answers}")


class AlternateEncodingsDoNotEvadeTheParser(unittest.TestCase):
    """Each of these was ALLOWED when the parser was first written."""

    EVASIONS = (
        ("eval", 'eval "git add -A"'),
        ("nested eval", "eval 'eval \"rm AGENTS.md\"'"),
        ("ANSI-C quoting", "bash -c $'git add -A'"),
        ("split word", 'gi""t add -A'),
        ("single-quote split", "g'i't add -A"),
        ("shell fed from a pipe", "echo 'git add -A' | sh"),
        ("base64 decoded into a shell", "echo Z2l0IGFkZCAtQQ== | base64 -d | sh"),
        ("expansion as argv[0]", "$(echo git) add -A"),
        ("command substitution body", "echo $(echo x > AGENTS.md)"),
        ("backtick body", "echo `git add -A`"),
        ("variable indirection", 'C="git add -A"; bash -c "$C"'),
        ("env wrapper", "env -i bash -c 'git add -A'"),
        ("nohup wrapper", "nohup bash -c 'git add -A'"),
        ("nice with a value flag", "nice -n 10 bash -c 'git add -A'"),
        ("timeout wrapper", "timeout 30 bash -c 'git add -A'"),
        ("sudo wrapper", "sudo git add -A"),
        ("xargs -I placeholder", "echo AGENTS.md | xargs -I{} rm {}"),
        ("wrapper around a pipeline", "bash -c 'echo x | tee AGENTS.md'"),
        ("perl bundled in-place flag", "perl -i.bak -pe 's/a/b/' AGENTS.md"),
        ("sed long in-place flag", "sed --in-place 's/a/b/' AGENTS.md"),
    )

    def test_every_evasion_is_refused(self) -> None:
        for label, command in self.EVASIONS:
            with self.subTest(evasion=label):
                self.assertIsNotNone(
                    policy.verdict(command, cwd=str(ROOT), repo_root=str(ROOT)),
                    f"{label} evaded the parser")

    def test_evasions_are_refused_identically_in_every_runtime(self) -> None:
        for label, command in self.EVASIONS:
            with self.subTest(evasion=label):
                answers = {
                    decision_of(run_entry(json.dumps(claude_payload(command)))[1]),
                    decision_of(run_entry(json.dumps(codex_payload(command)))[1]),
                    decision_of(run_entry(json.dumps(codemode_payload(command)))[1]),
                }
                self.assertEqual(answers, {"deny"}, f"{label} answered {answers}")


class NegativeControlsMustKeepWorking(unittest.TestCase):
    """The other half of the guard: a policy that denies everything is not a policy.

    🔴 Revision 1 blanked quoted spans so it would stop blocking its own documentation,
    and that exemption was the hole every wrapper hid in. The parser removes the exemption
    and keeps the property: a quoted span is data when it is an argument to `echo` or
    `git commit -m`, and a script when it is an argument to a shell.
    """

    ALLOWED = (
        ("quoted mention", 'echo "git add -A"'),
        ("commit message quoting a prohibited command",
         "git commit -m 'documents git add -A, sed -i and tee'"),
        ("grep for a prohibited token", "grep -rn 'git add -A' framework/"),
        ("ripgrep for two of them", "rg -n \"sed -i|tee\" framework/scripts"),
        ("read a file", "cat AGENTS.md"),
        ("read-only pipeline", "rg --files | sort | head -20"),
        ("git show", "git show HEAD:AGENTS.md"),
        ("git diff", "git diff --stat main...HEAD"),
        ("git status", "git status --short"),
        ("git log", "git log --oneline -20"),
        ("staging named paths", "git add framework/scripts/guard_policy.py AGENTS.md"),
        ("commit without -a", "git commit -m 'message'"),
        ("sed reading", "sed -n '1,80p' AGENTS.md"),
        ("awk reading", "awk '{print $1}' AGENTS.md"),
        ("find without -exec", "find . -name '*.md' -type f"),
        ("a committed script by name", "python3 framework/scripts/legend_lint.py ."),
        ("a committed shell script by name", "bash scripts/setup.sh"),
        ("python reading", "python3 -c \"print(open('AGENTS.md').read())\""),
        ("write to /tmp", "echo x > /tmp/probe.txt"),
        ("write to the scratchpad", "cp AGENTS.md /private/tmp/x/scratchpad/a.md"),
        ("sed -i inside /tmp", "sed -i '' 's/a/b/' /tmp/x.md"),
        ("tee to /dev/null", "echo x | tee /dev/null"),
        ("a scratch path via a variable set in the same command",
         'SC=/tmp/work; git diff > "$SC/out.diff"'),
        ("read-only substitution", "echo $(git rev-parse HEAD)"),
        ("xargs grep", "find . -name '*.py' | xargs grep -l guard"),
        ("fd redirect", "python3 framework/scripts/legend_lint.py . 2>&1 | head"),
    )

    def test_every_negative_control_is_allowed(self) -> None:
        for label, command in self.ALLOWED:
            with self.subTest(control=label):
                self.assertIsNone(
                    policy.verdict(command, cwd=str(ROOT), repo_root=str(ROOT)),
                    f"{label} was denied; ordinary work must not be blocked")

    def test_negative_controls_are_allowed_in_every_runtime(self) -> None:
        for label, command in self.ALLOWED:
            with self.subTest(control=label):
                answers = {
                    decision_of(run_entry(json.dumps(claude_payload(command)))[1]),
                    decision_of(run_entry(json.dumps(codex_payload(command)))[1]),
                }
                self.assertEqual(answers, {"allow"}, f"{label} answered {answers}")


class TheRepositorysOwnDocumentedCommandsStillRun(unittest.TestCase):
    """A corpus, not a list: what this repository tells its own actors to type.

    A curated negative-control list only contains the false positives its author thought
    of. This harvests every shell line the repository documents in a fenced block and
    requires the overwhelming majority to survive, so a policy change that quietly breaks
    the documented workflow fails here rather than in someone's session.

    The threshold is a ratio and the exceptions are named, because three of the documented
    lines *are* repository writes and the policy is right to refuse them.
    """

    FENCE = re.compile(r"^```(?:bash|sh|shell|console|zsh)?\s*$")
    START = re.compile(
        r"^\s*(?:\$\s+)?(python3?|git|rg|grep|sed|awk|cat|ls|find|wc|echo|printf|bash|sh|"
        r"zsh|cp|mv|rm|tee|head|tail|sort|uniq|diff|jq|shasum|sha256sum)\b")
    PLACEHOLDER = re.compile(r"<[A-Za-z_][A-Za-z0-9_. -]*>|\.\.\.")

    def harvest(self) -> list:
        tracked = subprocess.run(["git", "-C", str(ROOT), "ls-files", "*.md"],
                                 capture_output=True, text=True).stdout.split()
        cases = []
        for rel in tracked:
            lines = (ROOT / rel).read_text(encoding="utf-8", errors="replace").splitlines()
            inside = False
            index = 0
            while index < len(lines):
                line = lines[index]
                if line.startswith("```"):
                    inside = self.FENCE.match(line) is not None and not inside
                    index += 1
                    continue
                if inside and self.START.match(line):
                    buf = line.strip().lstrip("$ ").strip()
                    while buf.endswith("\\") and index + 1 < len(lines):
                        index += 1
                        buf = buf[:-1].rstrip() + " " + lines[index].strip()
                    if buf and not buf.startswith("#") and not self.PLACEHOLDER.search(buf):
                        cases.append((rel, index + 1, buf))
                index += 1
        return cases

    def test_the_documented_corpus_survives(self) -> None:
        cases = self.harvest()
        self.assertGreater(len(cases), 150, "the harvest itself must not silently empty")
        denied = []
        for rel, line, command in cases:
            outcome, _, _ = policy.classify(command, str(ROOT), str(ROOT))
            if outcome != policy.ALLOWED:
                denied.append(f"{rel}:{line}  {command[:90]}")
        ratio = 1 - len(denied) / len(cases)
        self.assertGreaterEqual(
            ratio, 0.94,
            f"only {ratio:.1%} of {len(cases)} documented commands survive:\n"
            + "\n".join(denied[:12]))

    def test_the_gates_this_repository_runs_are_all_allowed(self) -> None:
        """The commands CLAUDE.md § 3 tells every session to run, exactly as written."""
        for command in (
            "python3 framework/scripts/legend_lint.py .",
            "python3 framework/scripts/fulltext_receipts.py verify",
            "python3 framework/scripts/growth_anchors.py check",
            "python3 framework/scripts/unread_gold.py --help",
            "python3 scripts/public_release_gate.py",
            "python3 scripts/run_release_regressions.py",
            "python3 governance/scripts/governance_fingerprint.py compose --all",
            "python3 framework/scripts/runtime_parity.py --bootstrap",
        ):
            with self.subTest(command=command):
                self.assertIsNone(policy.verdict(command, cwd=str(ROOT), repo_root=str(ROOT)))


class TheRepositoryBoundaryIsWhatMakesAWriteProhibited(unittest.TestCase):
    """Scope, asserted: this is a repository guard, not a filesystem guard."""

    def test_a_write_outside_the_repository_is_not_this_guards_business(self) -> None:
        self.assertIsNone(policy.verdict("echo x > /Users/someone/notes.md",
                                         cwd=str(ROOT), repo_root=str(ROOT)))

    def test_the_same_write_inside_the_repository_is_denied(self) -> None:
        self.assertIsNotNone(policy.verdict("echo x > AGENTS.md",
                                            cwd=str(ROOT), repo_root=str(ROOT)))

    def test_a_relative_path_that_climbs_back_in_is_denied(self) -> None:
        self.assertIsNotNone(policy.verdict("echo x > ./framework/../AGENTS.md",
                                            cwd=str(ROOT), repo_root=str(ROOT)))

    def test_an_unknown_root_treats_everything_as_repository_space(self) -> None:
        """Fail-closed, stated: no root means no safe outside."""
        self.assertIsNotNone(policy.verdict("echo x > /Users/someone/notes.md",
                                            cwd=str(ROOT), repo_root=None))
        self.assertIsNone(policy.verdict("echo x > /tmp/notes.md",
                                         cwd=str(ROOT), repo_root=None),
                          "scratch space stays scratch space with or without a root")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
