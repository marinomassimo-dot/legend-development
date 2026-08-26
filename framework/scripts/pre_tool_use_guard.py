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
CODEX   PreToolUse  in  schema `pre-tool-use.command.input`   extracted from
                        /Applications/ChatGPT.app/Contents/Resources/codex 0.147.0
        PreToolUse  out schema `pre-tool-use.command.output`  same binary
```

🔴 **The OUTPUT schemas agree.** Codex's `pre-tool-use.command.output` declares
`hookSpecificOutput.hookEventName: "PreToolUse"` and
`permissionDecision: allow|deny|ask` — the object this guard already emitted for Claude.
So no output adapter exists, because none is needed. The **input** side differs in two
places only: the tool's name, and the key holding the command.

## The one thing this file does that a naive port would get wrong

Codex's shell tool takes its script under a different key, and other Codex tool payloads
carry `command` as an **argv list** (`{"command":["apply_patch","..."]}` is documented in
the installed binary). Stringifying a list and handing it to a regex policy is not an
adapter, it is an accident: `str(["bash","-lc","git add -A"])` puts the whole invocation
inside quotes, and `guard_policy._outside_quotes` blanks quoted spans — so the shape
would have been **allowed under Codex while denied under Claude**. That is a runtime that
grants authority, and it is the failure this module exists to prevent. Argv is therefore
reduced deliberately: a `-c`/`-lc` shell wrapper yields its script argument, anything else
is joined with `shlex.join`.

## Fail-closed boundary

Denial is the answer whenever the guard cannot establish what it is being asked about:
unparseable stdin, a wrong event name, a tool it does not recognise, or a command it
cannot read as text. `EXIT` stays `0` in every case — the decision travels in the JSON,
and a non-zero exit is a *broken hook*, not a denial.
"""
from __future__ import annotations

import json
import os
import shlex
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard_policy  # noqa: E402

HOOK_EVENT = "PreToolUse"

# Shell tools, per runtime, each name taken from that runtime's own surface.
SHELL_TOOLS = {
    "Bash": "claude-code",          # PreToolUse matcher used by .claude/settings.json
    "shell_command": "codex",       # codex 0.147.0: core/src/tools/handlers/shell/shell_command.rs
    "unified_exec": "codex",        # codex 0.147.0: ConfigShellToolType variant
}

# Keys that have been observed to hold the command, in the order they are tried.
COMMAND_KEYS = ("command", "cmd", "script")

SHELL_BINARIES = {"sh", "bash", "zsh", "dash", "ksh", "fish"}
SHELL_SCRIPT_FLAGS = {"-c", "-lc", "-ic", "-lic", "-ilc"}

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


def _from_argv(argv: list[str]) -> str:
    """`['bash','-lc','git add -A']` is the shell script, not a quoted string.

    Joining first and policing the join would hide the script inside quotes, which the
    policy deliberately ignores. Unwrap the wrapper, then police what actually runs.
    """
    if not argv:
        raise Undecidable("`command` is an empty list")
    program = Path(argv[0]).name
    if program in SHELL_BINARIES:
        for index, part in enumerate(argv[1:], start=1):
            if part in SHELL_SCRIPT_FLAGS and index + 1 < len(argv):
                return argv[index + 1]
    return shlex.join(argv)


def decide(payload: object) -> dict | None:
    """Return the hook object to emit, or None to stay silent and allow."""
    if not isinstance(payload, dict):
        raise Undecidable("the hook payload is not a JSON object")

    event = payload.get("hook_event_name")
    if event is not None and event != HOOK_EVENT:
        raise Undecidable(f"payload declares hook_event_name={event!r}, not {HOOK_EVENT!r}")

    tool_name = payload.get("tool_name")
    if not isinstance(tool_name, str) or not tool_name:
        raise Undecidable("payload carries no `tool_name`")

    if tool_name not in SHELL_TOOLS:
        if os.environ.get(UNKNOWN_TOOL_ENV) == "allow":
            return None
        raise Undecidable(
            f"`{tool_name}` is not a shell tool this guard knows.\n\n"
            "Either this hook is registered against tools it does not police — scope the "
            f"matcher, or set {UNKNOWN_TOOL_ENV}=allow deliberately — or the runtime has "
            "renamed its shell tool, in which case the guard has stopped covering the "
            "shell and must be taught the new name in "
            "framework/scripts/pre_tool_use_guard.py:SHELL_TOOLS."
        )

    reason = guard_policy.verdict(command_text(payload.get("tool_input")))
    return _deny(reason) if reason else None


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
