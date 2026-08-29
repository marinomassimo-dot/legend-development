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

#: 🔴 THE FRAME, stated once and passed explicitly — revision 10.
#:
#: Three directories, and revision 9 had one name for two of them. `cwd` is the
#: EFFECTIVE WORKDIR, which the model writes and which anchors relative operands;
#: `assigned` is the SESSION-BOUND worktree, which decides the authority perimeter. They
#: are equal in this suite because these cases are about command SHAPES and not about
#: the frame — the cases that vary them live in
#: `test_confinement_and_delegation.py::TheAssignedWorktreeIsSessionBound`.
#:
#: It is a keyword argument rather than an environment variable on purpose. Setting
#: `LEGEND_ASSIGNED_WORKTREE` for the process would be shorter and would leak into every
#: other suite a runner imports beside this one, which is how a suite that forgot to
#: state its frame goes on passing because another one stated it.
FRAME = {"cwd": str(ROOT), "repo_root": str(ROOT), "assigned": str(ROOT)}

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
    # 🔴 The session assignment is supplied through the ENVIRONMENT and the payload is
    # left alone, which is the revision-10 separation under test: the model writes the
    # payload, and the perimeter is not in it. `CLAUDE_PROJECT_DIR` is cleared first so
    # this suite's answer does not depend on whether the runner happens to be a live
    # session — under one it would be set to this worktree and the tests would pass for
    # a reason the suite never stated.
    base = {**os.environ, "LEGEND_ASSIGNED_WORKTREE": str(ROOT)}
    base.pop("CLAUDE_PROJECT_DIR", None)
    result = subprocess.run(
        [sys.executable, str(ENTRY)], input=raw, capture_output=True, text=True,
        env={**base, **(env or {})},
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

    def test_no_environment_variable_can_turn_an_unknown_tool_into_an_allow(self) -> None:
        """🔴 `PRE_TOOL_USE_GUARD_UNKNOWN_TOOL=allow` is REMOVED in revision 8.

        It returned ALLOW before the policy ran at all, so any process that could set an
        environment variable could turn the guard off for every tool it did not already
        know — including a renamed shell tool, which is precisely the scenario the
        denial message it printed was warning about. An environment variable is not an
        authorisation, and "deliberate" is not a property that `getenv` can check.

        The old name is asserted dead, not merely unused: a variable that still worked
        while nothing set it would be a bypass waiting for one line of config.
        """
        payload = claude_payload(READ_ONLY)
        payload["tool_name"] = "Read"
        for name in ("PRE_TOOL_USE_GUARD_UNKNOWN_TOOL", guard.EXTRA_SHELL_TOOLS_ENV):
            for value in ("allow", "1", "true", "*"):
                with self.subTest(variable=name, value=value):
                    _, out = run_entry(json.dumps(payload), env={name: value})
                    self.assertEqual(decision_of(out), "deny")

    def test_the_replacement_variable_can_only_add_policing(self) -> None:
        """Naming a tool makes it POLICED. There is no spelling that unpolices one."""
        payload = claude_payload("git add -A")
        payload["tool_name"] = "SomeNewShell"
        _, out = run_entry(json.dumps(payload),
                           env={guard.EXTRA_SHELL_TOOLS_ENV: "SomeNewShell"})
        self.assertEqual(decision_of(out), "deny", "the command must reach the policy")
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("Blanket staging", reason, "and be judged BY the policy")

        payload = claude_payload(READ_ONLY)
        payload["tool_name"] = "SomeNewShell"
        _, out = run_entry(json.dumps(payload),
                           env={guard.EXTRA_SHELL_TOOLS_ENV: "SomeNewShell"})
        self.assertEqual(decision_of(out), "allow")

    def test_an_unknown_key_inside_tool_input_denies(self) -> None:
        """🔴 The asymmetry, and why it is not arbitrary.

        A key BESIDE `tool_input` cannot change what `tool_input` means, so it is
        recorded and does not deny — a rule that denied on those refused every command
        in the session that wrote it, because claude-code 2.1.232 sends two of them.

        A key INSIDE `tool_input` is different: that is the object the command is read
        out of, and the reduction below it takes the FIRST key it recognises. An
        unrecognised sibling there may be a second command, or the key the runtime has
        moved to, and either way the guard would police something other than what runs.
        """
        payload = claude_payload(READ_ONLY)
        payload["tool_input"]["cmd2"] = "git add -A"
        code, out = run_entry(json.dumps(payload))
        self.assertEqual(decision_of(out), "deny")
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("cmd2", reason, "the denial must name the key")

    def test_the_live_runtimes_own_tool_input_keys_are_all_known(self) -> None:
        """The other direction: the rule above must not refuse the runtime that runs."""
        for key in ("command", "description", "timeout", "run_in_background"):
            self.assertIn(key, guard.KNOWN_TOOL_INPUT_KEYS)

    def test_a_payload_declaring_an_unsupported_schema_denies(self) -> None:
        payload = claude_payload(READ_ONLY)
        payload["hook_schema_version"] = "2"
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "deny")

    def test_a_payload_declaring_a_supported_schema_is_read_normally(self) -> None:
        payload = claude_payload(READ_ONLY)
        payload["hook_schema_version"] = "1"
        self.assertEqual(decision_of(run_entry(json.dumps(payload))[1]), "allow")

    def test_the_live_runtimes_own_payload_keys_are_all_known(self) -> None:
        """🔴 Measured against the runtime, not against the schema table.

        `runtime_bridge.md` § 2 says both input schemas were read out of the installed
        runtimes. `effort` and `prompt_id` arrive on every Claude Code 2.1.232
        PreToolUse and are in neither the table nor the harness contract it cites. A
        first draft of the unknown-key rule denied on them and refused every command in
        the session that wrote it, which is how they were found.
        """
        for key in ("effort", "prompt_id"):
            self.assertIn(key, guard.KNOWN_PAYLOAD_KEYS)

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

        # ── revision 8 ────────────────────────────────────────────────────────────
        #
        # 🔴 These were asserted only in `test_runtime_parity.py::GUARD_CLOSED_DEBT`
        # when they were closed, and the mutation harness said so: M32, M33, M34 and
        # M36 all SURVIVED a run of the guard's OWN suite. A bypass closed in the
        # policy and pinned only in another file is a bypass one refactor away from
        # returning, because the suite a reviewer runs for the guard does not bite.
        ("numbered redirect", "echo x 1> AGENTS.md"),
        ("numbered append", "echo x 2>> AGENTS.md"),
        ("both-streams redirect", "echo x &> AGENTS.md"),
        ("exec fd redirect", "exec 3> AGENTS.md"),
        ("a newline hides the write", "echo hi\necho x > AGENTS.md"),
        ("a newline hides the staging", "echo hi\ngit add -A"),
        ("a newline hides the delete", "ls\nrm AGENTS.md"),
        ("destination in -t", "cp -t framework/scripts /tmp/a"),
        ("destination in --target-directory",
         "cp --target-directory=framework/scripts /tmp/a"),
        ("mv into a directory flag", "mv -t framework/scripts /tmp/a"),
        ("install into a directory flag", "install -t framework/scripts /tmp/a"),
        ("touch", "touch AGENTS.md"),
        ("curl to a named file", "curl -o AGENTS.md https://example.com/x"),
        ("curl remote-name into cwd", "curl -O https://example.com/x"),
        ("wget to a named file", "wget -O AGENTS.md https://example.com/x"),
        ("wget into a directory", "wget -P framework/scripts https://example.com/x"),
        ("tar extraction into the repo", "tar -xf /tmp/a.tar -C framework"),
        ("tar extraction with no destination", "tar -xf /tmp/a.tar"),
        ("unzip with no destination", "unzip /tmp/a.zip"),
        ("git apply", "git apply /tmp/p.diff"),
        ("git rm", "git rm AGENTS.md"),
        ("git mv", "git mv AGENTS.md OTHER.md"),
        ("git restore", "git restore AGENTS.md"),
        ("git checkout --", "git checkout -- ."),
        ("git checkout a branch", "git checkout main"),
        ("git reset --hard", "git reset --hard HEAD~1"),
        ("git clean", "git clean -fd"),
        ("git push", "git push development HEAD"),
        ("git push --force", "git push --force origin main"),
        ("git branch -D", "git branch -D lettore"),
        ("git update-ref", "git update-ref refs/heads/main HEAD"),
        ("git stash", "git stash push -u -m x"),
        ("git rebase", "git rebase -i HEAD~3"),
        ("chmod", "chmod 777 AGENTS.md"),
        ("chown", "chown root AGENTS.md"),
        ("scp out of the machine", "scp AGENTS.md host:/b"),
        ("an unclassified git subcommand", "git frobnicate --all"),
    )

    def test_a_denial_names_the_effect_it_derived_and_not_merely_no(self) -> None:
        """🔴 "deny" is not enough, and a mutation run is what showed it.

        `M36` deletes the branch that makes `git push` a NETWORK_WRITE, and every suite
        still passed: the command falls through to the positive-listing catch-all and is
        refused as UNKNOWN_EFFECT. The verdict is unchanged and the DERIVATION is gone —
        the guard would be refusing a publication because it could not classify it, not
        because it recognised it, and the next person to add `push` to the read list
        would silently reopen it.

        A denial that names its effect is the difference between a control and a
        coincidence, so each row below pins the sentence, not just the answer.
        """
        for label, command, fragment in (
            ("git push is a publication", "git push development HEAD",
             "off this machine"),
            ("git push --force too", "git push --force origin main",
             "off this machine"),
            ("scp is a publication", "scp AGENTS.md host:/b", "off this machine"),
            ("reset --hard rewrites history", "git reset --hard HEAD~1",
             "not yours to discard"),
            ("clean deletes untracked work", "git clean -fd",
             "not yours to discard"),
            ("chmod is a permission change", "chmod 777 AGENTS.md", "mode"),
            ("an undeclared extraction", "tar -xf /tmp/a.tar",
             "does not name"),
            ("an unclassified git subcommand", "git frobnicate --all",
             "could not be derived"),
            ("blanket staging", "git add -A", "Blanket staging"),
            ("a shell write", "echo x > AGENTS.md", "Write and Edit"),
        ):
            with self.subTest(shape=label):
                reason = policy.verdict(command, **FRAME)
                self.assertIsNotNone(reason, f"{label} must deny")
                self.assertIn(fragment, reason,
                              f"{label} denied, but not for the reason it should: "
                              f"{reason.splitlines()[0]}")

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
        ("substitution inside double quotes", 'echo "$(git add -A)"'),
        ("assignment prefix", "FOO=1 git add -A"),
        ("two assignment prefixes", "A=1 B=2 git add -A"),
        ("assignment prefix before a wrapper", "FOO=1 bash -c 'git add -A'"),
        ("assignment prefix before rm", "FOO=1 rm AGENTS.md"),
        ("a substitution assigned to a variable", "a=$(git add -A)"),
        ("backtick inside double quotes", 'echo "`git add -A`"'),
        ("write inside a quoted substitution", 'echo "$(echo x > AGENTS.md)"'),
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
                    policy.verdict(command, **FRAME),
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
        ("read-only substitution in double quotes", 'echo "$(git rev-parse HEAD)"'),
        ("a variable assigned from a read-only substitution", "a=$(git rev-parse HEAD)"),
        ("an environment prefix on a read", "GIT_PAGER=cat git log --oneline -5"),
        ("a bare assignment", "SC=/tmp/work"),
        ("a substitution inside SINGLE quotes is inert", "echo '$(git add -A)'"),
        ("an escaped dollar is not a substitution", 'echo "\\$(git add -A)"'),
        ("an arrow inside a quoted substitution",
         'printf "%s\\n" "$([ 1 = 1 ] && echo "A -> B")"'),
        ("xargs grep", "find . -name '*.py' | xargs grep -l guard"),
        ("fd redirect", "python3 framework/scripts/legend_lint.py . 2>&1 | head"),

        # ── revision 8 ────────────────────────────────────────────────────────────
        #
        # 🔴 Revision 8 refuses nineteen more families, and the cost of that has to be
        # asserted in the same file, in the same run. Every line below is something an
        # actor NEEDS in order to land work here, and several of them are one flag away
        # from something now refused.
        ("create its own branch", "git checkout -b plan-a-new-branch"),
        ("create its own branch with switch", "git switch -c plan-a-new-branch"),
        ("name a new branch without moving to it", "git branch plan-a-new-branch"),
        ("read the current branch", "git branch --show-current"),
        ("list branches", "git branch"),
        ("list worktrees", "git worktree list"),
        ("list stashes", "git stash list"),
        ("show a stash", "git stash show"),
        ("read the reflog", "git reflog"),
        ("list tags", "git tag -l"),
        ("create a tag", "git tag v1.2.3"),
        ("commit named paths", "git commit -m 'msg' framework/scripts/guard_policy.py"),
        ("fetch without pushing", "git fetch origin"),
        ("list remotes", "git remote -v"),
        ("a numbered redirect into scratch", "echo x 1> /tmp/probe.txt"),
        ("a newline between two reads", "git status --short\ngit log --oneline -3"),
        ("a multi-line block whose lines are all reads",
         "cd /tmp\nls -la\ngrep -rn guard ."),
        ("cp into a scratch directory by flag", "cp -t /tmp/out /tmp/a"),
        ("tar extraction into scratch", "tar -xf /tmp/a.tar -C /tmp/out"),
        ("curl to a scratch file", "curl -o /tmp/out.json https://example.com/x"),
        ("touch a scratch file", "touch /tmp/probe.txt"),
        ("mkdir in scratch", "mkdir -p /tmp/out/nested"),
        ("chmod a scratch file", "chmod 755 /tmp/probe.sh"),
        ("a continuation is one command, not two",
         "python3 framework/scripts/legend_lint.py \\\n    ."),
    )

    def test_blanket_is_about_the_target_not_the_flag(self) -> None:
        """`-u` with a path names its targets; `-u` alone does not. `-A` never does.

        Both directions are asserted together, because a rule that only checks the
        prohibited half would pass a policy that refused `git add -u framework/scripts/` —
        which is the guard blocking the very behaviour its denial message asks for.
        """
        for command, expected in (
            ("git add -A", "deny"),
            ("git add --all", "deny"),
            ("git add -A framework/", "deny"),
            ("git add .", "deny"),
            ("git add -u", "deny"),
            ("git add --update", "deny"),
            ("git add -p", "deny"),
            ("git add -u framework/scripts/", "allow"),
            ("git add --update framework/", "allow"),
            ("git add framework/scripts/guard_policy.py", "allow"),
        ):
            with self.subTest(command=command):
                reason = policy.verdict(command, **FRAME)
                self.assertEqual("deny" if reason else "allow", expected)

    def test_every_negative_control_is_allowed(self) -> None:
        for label, command in self.ALLOWED:
            with self.subTest(control=label):
                self.assertIsNone(
                    policy.verdict(command, **FRAME),
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
        """🔴 The floor is 0.90 in revision 8, and it was 0.94 in revision 7.

        Lowering a threshold to admit one's own change is how a gate stops being one,
        so the number is not the claim — the DELTA is, and it was measured with the
        corpus held fixed and the policy as the only variable:

            corpus 211 lines   rev7 denied 9 (95.7%)   rev8 denied 16 (92.4%)
            newly denied 7 · newly allowed 0

        All seven are consequences of closing a real defect, and none is a runnable
        command that stopped working:

          2  this protocol's own `GUARD_HARDENING_DEBT` table, harvested out of a fenced
             block. The rows literally read `git clean -fd  git push`, and the rule now
             fires on them. Self-reference, not regression.
          2  prose fragments beginning with the word `git` — "git at session open and",
             "git identity · lease derivation" — now UNKNOWN_EFFECT because a git
             subcommand this policy has not classified is refused rather than assumed
             harmless.
          2  `candidate_content_hash.py … --tip <any tip ≥ e839db38>`, a PLACEHOLDER
             carrying an unbalanced `>`. Revision 7 allowed these only because its own
             `\\d+>` ate the `38>` out of the SHA — the same bug that hid `1>` from the
             redirection rule. Fixing one fixed both, and exposed these.
          1  `git clone --no-local "$LEGEND_SOURCE" "$clone_dir"` — a real write to a
             destination held in a variable from an EARLIER command. UNDERIVABLE, and
             the declared failure direction.

        The ratio is kept as a floor, but the assertion that carries the weight is the
        second one: the escape hatch every denial message recommends must never be in
        the denied set.
        """
        cases = self.harvest()
        self.assertGreater(len(cases), 150, "the harvest itself must not silently empty")
        denied = []
        for rel, line, command in cases:
            outcome, _, _ = policy.classify(command, **FRAME)
            if outcome != policy.ALLOWED:
                denied.append((rel, line, command))
        ratio = 1 - len(denied) / len(cases)
        self.assertGreaterEqual(
            ratio, 0.90,
            f"only {ratio:.1%} of {len(cases)} documented commands survive:\n"
            + "\n".join(f"{r}:{l}  {c[:90]}" for r, l, c in denied[:20]))

    def test_the_escape_hatch_every_denial_recommends_actually_works(self) -> None:
        """Invoking a committed script by name is what every denial message offers.

        🔴 Mined out of the documented corpus this property cannot be measured: the
        corpus lines that name a script also carry redirects into the repository root
        and `<placeholder>` spans, so they are denied for reasons that have nothing to
        do with the invocation. A first draft of this test asserted over those lines
        and failed on six of them, none of which was an escape-hatch failure. The
        property is about the INVOCATION, so it is asserted over invocations.

        Every committed Python script in the repository, invoked plainly, must pass.
        That is a corpus of its own and it grows on its own.
        """
        scripts = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "*.py"],
            capture_output=True, text=True).stdout.split()
        self.assertGreater(len(scripts), 30, "the script listing must not silently empty")
        refused = []
        for script in scripts:
            for command in (f"python3 {script}", f"python3 {script} --help"):
                outcome, reason, _ = policy.classify(command, **FRAME)
                if outcome != policy.ALLOWED:
                    refused.append(f"{command}\n    {reason.splitlines()[0]}")
        self.assertEqual(
            [], refused,
            "the guard refuses the alternative its own denial message recommends:\n"
            + "\n".join(refused[:10]))

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
                self.assertIsNone(policy.verdict(command, **FRAME))


class TheRepositoryBoundaryIsWhatMakesAWriteProhibited(unittest.TestCase):
    """Scope, asserted: this is a repository guard, not a filesystem guard."""

    def test_repository_membership_beats_the_scratch_prefix_without_a_topology(self) -> None:
        """🔴 The lexical root comparison is DEFENCE IN DEPTH, and it is reachable.

        Revision 9 consults the topology first, which answers ASSIGNED_WORKTREE for a
        path inside the tree — so for every caller in this repository the lexical
        comparison below it never decides anything, and the mutation deleting it
        survived the whole suite as an apparently equivalent mutant.

        It is not equivalent. The topology is derived from `cwd`; the root is passed
        separately. A caller that hands this function a `cwd` OUTSIDE any repository
        together with a `repo_root` — which the hook path never does, and a direct API
        call may — gets `topology.ok == False`, no topology answer, and then only this
        branch stands between a repository under `TMPDIR` and the scratch prefixes.

        Revision 8 shipped exactly that hole with the ordering the other way round, and
        a fixture repository was writable for a whole revision. Deleting the redundant
        check because the newer one usually fires first is how it comes back.
        """
        with tempfile.TemporaryDirectory() as raw:
            repo = Path(raw) / "repo"
            repo.mkdir()
            subprocess.run(["git", "-C", str(repo), "init", "-q"], capture_output=True)
            outside = Path(raw) / "not-a-repo"
            outside.mkdir()
            self.assertEqual(
                policy.classify_target(str(repo / "a.md"), cwd=str(outside),
                                       repo_root=str(repo), assigned=str(ROOT)),
                policy.INSIDE_REPO,
                "a path inside the named root is repository space even when it belongs "
                "to no worktree of the SESSION's repository and sits under TMPDIR")

    def test_the_two_path_spellings_are_both_compared(self) -> None:
        """🔴 Case K1 in unit form, and the half a same-spelling fixture cannot reach.

        `git rev-parse --show-toplevel` answers `/private/var/folders/…` on macOS while a
        runtime's `cwd` says `/var/folders/…`. Same directory, two strings, and a lexical
        comparison between them returns False — which is how a fixture repository under
        `TMPDIR` was writable for a whole revision. The test above builds both sides from
        one spelling, so it passes with the resolved reading deleted; this one deliberately
        does not.

        It SKIPS where the platform has no such symlink, and the skip is stated rather than
        silent: on Linux `realpath(tmpdir) == tmpdir` and there is nothing to compare.
        """
        with tempfile.TemporaryDirectory() as raw:
            if os.path.realpath(raw) == raw:
                self.skipTest("this platform's temp directory is already resolved")
            repo = Path(raw) / "repo"
            repo.mkdir()
            subprocess.run(["git", "-C", str(repo), "init", "-q"], capture_output=True)
            outside = Path(raw) / "not-a-repo"
            outside.mkdir()
            # repo_root in the RESOLVED spelling, the target in the unresolved one —
            # which is exactly the pair the hook receives.
            self.assertEqual(
                policy.classify_target(str(repo / "a.md"), cwd=str(outside),
                                       repo_root=os.path.realpath(str(repo)),
                                       assigned=str(ROOT)),
                policy.INSIDE_REPO,
                "a repository is a repository under either spelling of its own path")

    def test_the_same_path_with_no_assignment_is_underivable_not_scratch(self) -> None:
        """🔴 The revision-10 half of the branch above, and it fails DIFFERENTLY.

        With no session assignment there is no perimeter, so "inside the effective
        workdir's repository" does not say WHICH repository — and `INSIDE_REPO` is a
        GRANT for `STAGE` and `COMMIT`. The overlay therefore reads `UNDERIVABLE` when
        unbound, which denies every mutation instead of granting two of them.

        Both answers deny a shell write, which is exactly why this needs its own
        assertion: a verdict-level test could not tell them apart, and the corpus caught
        the difference only because case `F11` commits rather than writes.
        """
        with tempfile.TemporaryDirectory() as raw:
            repo = Path(raw) / "repo"
            repo.mkdir()
            subprocess.run(["git", "-C", str(repo), "init", "-q"], capture_output=True)
            outside = Path(raw) / "not-a-repo"
            outside.mkdir()
            self.assertEqual(
                policy.classify_target(str(repo / "a.md"), cwd=str(outside),
                                       repo_root=str(repo), assigned=None),
                policy.UNDERIVABLE)

    def test_a_write_outside_the_repository_is_not_this_guards_business(self) -> None:
        self.assertIsNone(policy.verdict("echo x > /Users/someone/notes.md",
                                         cwd=str(ROOT), repo_root=str(ROOT),
                                         assigned=str(ROOT)))

    def test_the_same_write_inside_the_repository_is_denied(self) -> None:
        self.assertIsNotNone(policy.verdict("echo x > AGENTS.md",
                                            cwd=str(ROOT), repo_root=str(ROOT),
                                            assigned=str(ROOT)))

    def test_a_relative_path_that_climbs_back_in_is_denied(self) -> None:
        self.assertIsNotNone(policy.verdict("echo x > ./framework/../AGENTS.md",
                                            cwd=str(ROOT), repo_root=str(ROOT),
                                            assigned=str(ROOT)))

    def test_a_shell_out_is_judged_as_the_command_it_runs(self) -> None:
        """The escape hatch must survive being taken from inside a program.

        🔴 `\\bsubprocess\\.` was once a write primitive outright, so a heredoc that invoked
        a committed script through `subprocess.run` was denied — the guard forbidding the
        alternative its own denial message recommends. Reading the argument as a command
        instead is both more permissive here and stricter where it matters.
        """
        body = "python3 - <<'PY'\n{}\nPY"
        for program, expected in (
            ('import subprocess, sys\n'
             'subprocess.run([sys.executable, "framework/scripts/legend_lint.py", "."])', "allow"),
            ('import subprocess\nsubprocess.run(["git", "log", "--oneline", "-5"])', "allow"),
            ('import subprocess\nsubprocess.run(["git", "add", "-A"])', "deny"),
            ('import subprocess\nsubprocess.run(["rm", "-rf", "framework/scripts"])', "deny"),
            ('import os\nos.system("git add -A")', "deny"),
            ("import subprocess\nsubprocess.run(build_argv())", "deny"),
        ):
            with self.subTest(program=program.splitlines()[-1][:50]):
                reason = policy.verdict(body.format(program), **FRAME)
                self.assertEqual("deny" if reason else "allow", expected)

    def test_the_directory_decides_when_only_the_filename_expands(self) -> None:
        """A loop writing one file per iteration into a directory it just named.

        🔴 This is a deliberate narrowing of fail-closed, so it is asserted in BOTH
        directions in one table: a known-scratch directory allows an expanding *filename*,
        a known-repository directory does not, and an expansion anywhere but the last
        segment — or a `..` anywhere — goes back to being undecidable.
        """
        for command, expected in (
            ('SC=/tmp/w; git show a:b > "$SC/out/gp_$rev.py"', "allow"),
            ('SC=/tmp/w; echo x > "$SC/$f"', "allow"),
            ("echo x > /private/tmp/x/scratchpad/f_$i.txt", "allow"),
            ("rm /tmp/w/*.pyc", "allow"),
            ('echo x > "framework/scripts/gen_$n.py"', "deny"),
            ('SC=/tmp/w; echo x > "$SC/$d/f"', "deny"),
            ('SC=/tmp/w; echo x > "$SC/../$f"', "deny"),
            ('echo x > "$TARGET"', "deny"),
            ('echo x > "$SOMETHING/f"', "deny"),
            ("rm framework/scripts/*.pyc", "deny"),
        ):
            with self.subTest(command=command):
                reason = policy.verdict(command, **FRAME)
                self.assertEqual("deny" if reason else "allow", expected)

    def test_an_unknown_root_treats_everything_as_repository_space(self) -> None:
        """Fail-closed, stated — and revision 10 moved WHERE the closing happens.

        🔴 Revision 9 read `repo_root=None` as *we do not know where we are*, and made
        every non-scratch path repository space on that basis. It no longer means that:
        the SESSION ASSIGNMENT establishes the repository, `repo_root` only anchors the
        workdir overlay, and with an assignment in hand an unknown root leaves a path
        outside the repository outside it — which is the correct answer and not a
        weakening, because the perimeter was derived from something better.

        The fail-closed arm therefore moved to the assignment, and it is asserted
        immediately below rather than deleted. If a later edit lets an UNBOUND session
        write outside scratch, that test goes red — this one would not, and reading it
        as the fail-closed check is exactly the mistake this docstring exists to stop.
        """
        self.assertIsNone(policy.verdict("echo x > /Users/someone/notes.md",
                                         cwd=str(ROOT), repo_root=None,
                                         assigned=str(ROOT)),
                          "an assignment establishes the repository; an unknown root "
                          "does not make an outside path this guard's business")
        self.assertIsNone(policy.verdict("echo x > /tmp/notes.md",
                                         cwd=str(ROOT), repo_root=None,
                                         assigned=str(ROOT)),
                          "scratch space stays scratch space with or without a root")

    def test_an_unknown_assignment_treats_everything_as_repository_space(self) -> None:
        """The fail-closed arm, where revision 10 put it: on the ASSIGNMENT.

        No trusted source answered, so there is no perimeter, so every mutation outside
        scratch is refused — including one that revision 9 would have allowed as
        `OUTSIDE_REPO`. Reads and scratch writes survive, because a guard that refuses
        `echo x > /tmp/f` when a variable is unset is a guard that gets turned off.
        """
        self.assertIsNotNone(policy.verdict("echo x > /Users/someone/notes.md",
                                            cwd=str(ROOT), repo_root=None,
                                            assigned=None))
        self.assertIsNotNone(policy.verdict("git commit -m x framework/probe.md",
                                            cwd=str(ROOT), repo_root=str(ROOT),
                                            assigned=None),
                             "a commit with no perimeter is a commit into an "
                             "unidentified repository")
        self.assertIsNone(policy.verdict("echo x > /tmp/notes.md",
                                         cwd=str(ROOT), repo_root=None, assigned=None),
                          "scratch is a property of the path, not of the repository")
        self.assertIsNone(policy.verdict("git status --short",
                                         cwd=str(ROOT), repo_root=str(ROOT),
                                         assigned=None),
                          "READ is granted with no assignment; only mutation is not")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
