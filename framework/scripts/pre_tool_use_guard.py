#!/usr/bin/env python3
"""The `PreToolUse` write guard — ONE engine, registered by every runtime.

`ACTOR_ID != RUNTIME != SESSION != WORKTREE != AUTHORITY`. A control that exists in one
runtime and not another turns the choice of runtime into a choice of authority, which is
exactly the invariant this file defends. So the policy lives in `guard_policy.py`, this
file adapts a runtime's payload onto it, and both runtimes register *this* script.

## What was measured, and where

Both wire schemas were read out of the **installed** runtimes rather than assumed:

```
CLAUDE  PreToolUse  in  {session_id, transcript_path, cwd, hook_event_name,
                         tool_name, tool_input}                 — harness contract
        PreToolUse  out {hookSpecificOutput:{hookEventName, permissionDecision,
                         permissionDecisionReason}}
CODEX   PreToolUse  in  schema `pre-tool-use.command.input`   extracted from the
                        installed codex binary; REQUIRES cwd, hook_event_name, model,
                        permission_mode, session_id, tool_input, tool_name, tool_use_id,
                        transcript_path, turn_id — and `additionalProperties: false`
        PreToolUse  out schema `pre-tool-use.command.output`  same binary
```

🔴 **The OUTPUT schemas agree.** Codex's `pre-tool-use.command.output` declares
`hookSpecificOutput.hookEventName: "PreToolUse"` and
`permissionDecision: allow|deny|ask` — the object this guard already emitted for Claude.
So no output adapter exists, because none is needed. The **input** side differs in the
tool's name, in the key holding the command, and — under code mode — in whether there is
a command in the payload at all.

## The three shapes this adapter has to reduce

1. **a command string** under `command` / `cmd` / `script` — Claude's `Bash`, Codex's
   `shell_command`;
2. **an argv list**. Stringifying a list and handing it to a regex policy is not an
   adapter, it is an accident: `str(["bash","-lc","git add -A"])` puts the whole
   invocation inside a quoted string. Argv is therefore reduced deliberately — a
   `-c`/`-lc` shell wrapper yields its script argument, anything else is `shlex.join`ed;
3. 🔴 **a code-mode program.** The Codex session recorded at
   `~/.codex/sessions/2026/08/28/rollout-2026-08-28T10-14-22-…jsonl` did not call a shell
   tool at all: every one of its 20 tool calls was `exec`, carrying a JavaScript body that
   called `tools.exec_command({"cmd": …, "workdir": …})`. A guard whose matcher list is
   `shell_command`/`unified_exec` never sees that command. `CODE_MODE_CALL` extracts the
   inner invocations so the same policy judges them.

## Fail-closed boundary

Denial is the answer whenever the guard cannot establish what it is being asked about:
unparseable stdin, a wrong event name, a tool it does not recognise, or a command it
cannot read as text. `EXIT` stays `0` in every case — the decision travels in the JSON,
and a non-zero exit is a *broken hook*, not a denial.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard_policy  # noqa: E402

HOOK_EVENT = "PreToolUse"

# Shell tools, per runtime, each name taken from that runtime's own surface.
SHELL_TOOLS = {
    "Bash": "claude-code",          # PreToolUse matcher used by .claude/settings.json
    "shell_command": "codex",       # ConfigShellToolType variant, config-mode shell
    "unified_exec": "codex",        # ConfigShellToolType variant
    "exec_command": "codex",        # the inner call a code-mode program makes
}

# Code-mode tools: `tool_input` carries a PROGRAM, and the shell calls are inside it.
# Observed in a real session rather than inferred from the binary — see the module docstring.
CODE_MODE_TOOLS = {"exec"}

# Tools whose payload is a patch envelope rather than a shell command.
PATCH_TOOLS = {"apply_patch"}

# Keys that have been observed to hold the command, in the order they are tried.
COMMAND_KEYS = ("command", "cmd", "script")
# Keys that have been observed to hold a program body or a patch envelope.
PROGRAM_KEYS = ("input", "source", "code", "program", "patch", "content")

SHELL_BINARIES = {"sh", "bash", "zsh", "dash", "ksh", "fish"}
SHELL_SCRIPT_FLAGS = {"-c", "-lc", "-ic", "-lic", "-ilc"}

#: `tools.exec_command({...})` / `tools.shell({...})` inside a code-mode program body.
CODE_MODE_CALL = re.compile(r"\b(?:tools\s*\.\s*)?(exec_command|shell_command|unified_exec|shell)\s*\(")

UNKNOWN_TOOL_ENV = "PRE_TOOL_USE_GUARD_UNKNOWN_TOOL"


class Undecidable(Exception):
    """The guard cannot tell what it is being asked about. That is a denial."""


def _deny(reason: str) -> dict:
    return {
        "hookSpecificOutput": {
            "hookEventName": HOOK_EVENT,
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


# ── payload reduction ──────────────────────────────────────────────────────────────

def command_text(tool_input: object) -> str:
    """Reduce a runtime's tool input to the shell text the policy reasons about.

    Raises `Undecidable` rather than guessing. A guard that guesses is a guard that
    can be steered by choosing a payload shape.
    """
    if isinstance(tool_input, str):
        return tool_input
    if not isinstance(tool_input, dict):
        raise Undecidable(f"tool_input is {type(tool_input).__name__}, not an object or a string")

    for key in COMMAND_KEYS:
        if key not in tool_input:
            continue
        value = tool_input[key]
        if isinstance(value, str):
            return value
        if isinstance(value, list):
            if not all(isinstance(part, str) for part in value):
                raise Undecidable(f"`{key}` is a list containing non-string elements")
            return _from_argv(value)
        raise Undecidable(f"`{key}` is {type(value).__name__}, which is not a command")

    raise Undecidable(
        "no command found under any of " + ", ".join(f"`{k}`" for k in COMMAND_KEYS)
    )


def _from_argv(argv: list) -> str:
    """`['bash','-lc','git add -A']` is the shell script, not a quoted string.

    Joining first and policing the join would hide the script inside quotes. Unwrap the
    wrapper, then police what actually runs.
    """
    if not argv:
        raise Undecidable("`command` is an empty list")
    program = Path(argv[0]).name
    if program in SHELL_BINARIES:
        for index, part in enumerate(argv[1:], start=1):
            if part in SHELL_SCRIPT_FLAGS and index + 1 < len(argv):
                return argv[index + 1]
    return shlex.join(argv)


def program_text(tool_input: object) -> str:
    """The program body of a code-mode or patch-shaped call."""
    if isinstance(tool_input, str):
        return tool_input
    if not isinstance(tool_input, dict):
        raise Undecidable(f"tool_input is {type(tool_input).__name__}, not an object or a string")
    for key in PROGRAM_KEYS + COMMAND_KEYS:
        value = tool_input.get(key)
        if isinstance(value, str):
            return value
        if isinstance(value, list) and all(isinstance(part, str) for part in value):
            return "\n".join(value)
    raise Undecidable(
        "no program body found under any of "
        + ", ".join(f"`{k}`" for k in PROGRAM_KEYS + COMMAND_KEYS)
    )


def _json_object_at(text: str, start: int) -> "tuple[object, int]":
    """Read one balanced `{…}` span starting at `start`, quotes respected."""
    depth = 0
    quote = ""
    index = start
    while index < len(text):
        char = text[index]
        if quote:
            if char == "\\":
                index += 2
                continue
            if char == quote:
                quote = ""
        elif char in "\"'":
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                span = text[start : index + 1]
                try:
                    return json.loads(span), index + 1
                except ValueError:
                    raise Undecidable("a code-mode shell call whose argument is not JSON")
        index += 1
    raise Undecidable("a code-mode shell call with an unbalanced argument")


def code_mode_commands(body: str) -> "list[str]":
    """Every shell command a code-mode program invokes.

    An `exec_command` call whose argument cannot be read is `Undecidable`, not empty: a
    body the guard cannot parse is a body it cannot clear.
    """
    commands: "list[str]" = []
    for match in CODE_MODE_CALL.finditer(body):
        cursor = match.end()
        while cursor < len(body) and body[cursor] in " \t\n":
            cursor += 1
        if cursor >= len(body) or body[cursor] != "{":
            raise Undecidable(
                f"`{match.group(1)}` is called with an argument this guard cannot read; "
                "it cannot clear a shell call it cannot see"
            )
        argument, _ = _json_object_at(body, cursor)
        commands.append(command_text(argument))
    return commands


# ── decision ───────────────────────────────────────────────────────────────────────

def repo_root_of(cwd: object) -> "str | None":
    """The working-tree root containing `cwd`, or None when it is not derivable.

    🔴 `None` is not "no repository, therefore nothing to protect". `guard_policy`
    treats an unknown root by classifying every non-scratch path as repository space,
    which is the fail-closed reading.
    """
    if not isinstance(cwd, str) or not cwd:
        return None
    try:
        result = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    root = result.stdout.strip()
    return root or None


def decide(payload: object) -> "dict | None":
    """Return the hook object to emit, or None to stay silent and allow."""
    if not isinstance(payload, dict):
        raise Undecidable("the hook payload is not a JSON object")

    event = payload.get("hook_event_name")
    if event is not None and event != HOOK_EVENT:
        raise Undecidable(f"payload declares hook_event_name={event!r}, not {HOOK_EVENT!r}")

    tool_name = payload.get("tool_name")
    if not isinstance(tool_name, str) or not tool_name:
        raise Undecidable("payload carries no `tool_name`")

    known = set(SHELL_TOOLS) | CODE_MODE_TOOLS | PATCH_TOOLS
    if tool_name not in known:
        if os.environ.get(UNKNOWN_TOOL_ENV) == "allow":
            return None
        raise Undecidable(
            f"`{tool_name}` is not a tool this guard knows.\n\n"
            "Either this hook is registered against tools it does not police — scope the "
            f"matcher, or set {UNKNOWN_TOOL_ENV}=allow deliberately — or the runtime has "
            "renamed its shell tool, in which case the guard has stopped covering the "
            "shell and must be taught the new name in "
            "framework/scripts/pre_tool_use_guard.py:SHELL_TOOLS."
        )

    cwd = payload.get("cwd")
    cwd = cwd if isinstance(cwd, str) else None
    root = repo_root_of(cwd)
    tool_input = payload.get("tool_input")

    if tool_name in CODE_MODE_TOOLS:
        commands = code_mode_commands(program_text(tool_input))
    elif tool_name in PATCH_TOOLS:
        # An envelope is policed as the `apply_patch` shell form, which the policy already
        # knows how to read: it names its own targets.
        commands = ["apply_patch <<'PATCH'\n" + program_text(tool_input) + "\nPATCH"]
    else:
        commands = [command_text(tool_input)]

    for command in commands:
        reason = guard_policy.verdict(command, cwd=cwd, repo_root=root)
        if reason:
            return _deny(reason)
    return None


def main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, ValueError) as exc:
        print(json.dumps(_deny(
            "The write guard could not read its own input, so it cannot say whether this "
            f"command is safe, and answers no.\n\nstdin did not parse as JSON: {exc}"
        )))
        return 0

    try:
        emit = decide(payload)
    except Undecidable as exc:
        print(json.dumps(_deny(
            "The write guard could not establish what it was asked about, and answers "
            f"no rather than assuming.\n\n{exc}"
        )))
        return 0

    if emit is not None:
        print(json.dumps(emit))
    return 0


if __name__ == "__main__":
    sys.exit(main())
