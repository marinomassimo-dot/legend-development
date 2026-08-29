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

#: Keys observed inside `tool_input` for a shell call, per runtime. This is the object
#: the command is READ OUT OF, so an unknown key here is not a harmless sibling: it may
#: be a second command carrier, or the one the runtime now uses. Refused, and the
#: denial names it.
KNOWN_TOOL_INPUT_KEYS = frozenset({
    # the command itself, under every spelling either runtime uses
    "command", "cmd", "script", "input", "source", "code", "program", "patch", "content",
    # Claude Code's Bash tool
    "description", "timeout", "run_in_background", "shell_executable",
    # Codex
    "workdir", "with_escalated_permissions", "justification", "timeout_ms", "env",
    "sandbox", "yield_time_ms", "max_output_tokens", "shell", "login",
})

SHELL_BINARIES = {"sh", "bash", "zsh", "dash", "ksh", "fish"}
SHELL_SCRIPT_FLAGS = {"-c", "-lc", "-ic", "-lic", "-ilc"}

#: `tools.exec_command({...})` / `tools.shell({...})` inside a code-mode program body.
CODE_MODE_CALL = re.compile(r"\b(?:tools\s*\.\s*)?(exec_command|shell_command|unified_exec|shell)\s*\(")

#: 🔴 REMOVED in revision 8: `PRE_TOOL_USE_GUARD_UNKNOWN_TOOL=allow`.
#:
#: It made an unrecognised tool ALLOW, and it did so by returning before the policy ran
#: at all — so any process that could set an environment variable could turn the guard
#: off for every tool it did not already know, including a renamed shell tool, which is
#: the exact scenario the denial message it printed was warning about. An environment
#: variable is not an authorisation, and "deliberate" is not a property a getenv can
#: check.
#:
#: What replaces it can only ADD policing, never remove it: a comma-separated list of
#: tool names to treat AS SHELL TOOLS. The failure direction of a mistake in this
#: variable is that a harmless tool gets its command parsed, not that a mutating one
#: stops being seen.
EXTRA_SHELL_TOOLS_ENV = "PRE_TOOL_USE_GUARD_EXTRA_SHELL_TOOLS"

#: Top-level payload keys either runtime is known to send. An unknown key means the
#: payload is not the payload this guard was written against — Codex's own input schema
#: declares `additionalProperties: false`, so an extra key is a protocol violation
#: there and an unmeasured runtime change here. Either way it is not a thing to shrug at.
KNOWN_PAYLOAD_KEYS = frozenset({
    # Claude Code, per the harness contract this protocol § 2 recorded.
    "session_id", "transcript_path", "cwd", "hook_event_name", "tool_name", "tool_input",
    "permission_mode",
    # 🔴 OBSERVED, claude-code 2.1.232, 2026-08-29 — and NOT in the § 2 table, which
    # says both input schemas were "read out of the installed runtimes rather than taken
    # from documentation about them". Two keys the live runtime sends on every
    # PreToolUse were missing from it. The table is narrower than the wire, and it was
    # a rule written against the table that found out.
    "effort", "prompt_id",
    # Codex, per `pre-tool-use.command.input` extracted from the installed binary
    "model", "tool_use_id", "turn_id",
    # Declared extension points, so a new field is a one-line change and not a mystery.
    "hook_schema_version", "workspace_root",
})

#: Payload schema versions this guard has been written against. A payload DECLARING a
#: version outside this set is refused.
#:
#: 🔴 This is about the PAYLOAD's declared schema, not about the runtime's version, and
#: the two must not be collapsed. A runtime version this bridge has not measured makes
#: its guarantees UNMEASURED rather than false — `cross_session_transport.md` § 3 — and
#: denying every command on a version bump would make the guard the thing that breaks.
#: A payload that declares a schema this parser does not implement is different: the
#: fields may mean something else, and reading them anyway is guessing.
SUPPORTED_PAYLOAD_SCHEMAS = frozenset({"1", "1.0", "v1"})


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

    # 🔴 Unknown keys HERE deny, unlike unknown keys beside `tool_input`. This is the
    # object the command is read out of: an unrecognised key in it may be a second
    # command carrier, or the one the runtime has moved to, and the loop below would
    # police the first key it recognises and silently ignore the rest.
    unknown = sorted(set(tool_input) - KNOWN_TOOL_INPUT_KEYS)
    if unknown:
        raise Undecidable(
            "tool_input carries keys this guard does not know: "
            + ", ".join(repr(k) for k in unknown)
            + ". A key in the object the command is read out of may itself carry a "
              "command, so this cannot be ignored. Add it to KNOWN_TOOL_INPUT_KEYS in "
              "framework/scripts/pre_tool_use_guard.py once its meaning is established.")

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


def code_mode_commands(body: str) -> "list[tuple[str, object]]":
    """Every shell command a code-mode program invokes, each with ITS OWN argument object.

    An `exec_command` call whose argument cannot be read is `Undecidable`, not empty: a
    body the guard cannot parse is a body it cannot clear.

    🔴 The argument object travels back with the command because the `workdir` is IN it.
    The recorded session that motivated code-mode support called
    `tools.exec_command({"cmd": …, "workdir": …})` twenty times, each with its own
    directory — so a code-mode program is exactly where one payload carries several
    execution bases, and judging them all against the session's `cwd` is the revision-8
    mistake with more than one chance to be wrong per call.
    """
    commands: "list[tuple[str, object]]" = []
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
        commands.append((command_text(argument), argument))
    return commands


# ── decision ───────────────────────────────────────────────────────────────────────

def derive_workdir(payload: dict, tool_input: object) -> "str":
    """The directory the command will ACTUALLY run in. Relative targets resolve here.

    🔴 Revision 8 read `tool_input.workdir` only to declare it a known key, and anchored
    every relative path to the payload's `cwd`. Codex's `exec_command` takes a `workdir`
    and honours it, so the two differ routinely — and the divergence was measured on
    2026-08-29 to falsify target prediction in BOTH directions:

    ```text
    cwd=<REPO>  workdir=<REPO>   echo x > framework/probe.md   DENY   correct
    cwd=/tmp    workdir=<REPO>   echo x > framework/probe.md   ALLOW  the repository write
                                                                     the guard exists to stop
    cwd=<REPO>  workdir=/tmp     echo x > framework/probe.md   DENY   a scratch write refused
    ```

    The first wrong answer is a bypass; the second is a guard that blocks ordinary work,
    which is the failure that gets guards turned off. One rule fixes both:

        EFFECTIVE_WORKDIR = tool_input.workdir, resolved, when it is present and usable
                            else the payload's cwd

    A `workdir` that is present but NOT usable — not a string, empty, expanding, or not
    an existing directory — is not ignored and is not guessed at. The command will run
    somewhere this guard cannot name, so no relative target it carries can be placed,
    and the answer is `Undecidable`, which denies. Ignoring it would silently restore
    exactly the revision-8 behaviour for the one input designed to defeat it.
    """
    cwd = payload.get("cwd")
    cwd = cwd if isinstance(cwd, str) and cwd else None

    workdir = tool_input.get("workdir") if isinstance(tool_input, dict) else None
    if workdir is None:
        return cwd or ""
    if not isinstance(workdir, str) or not workdir.strip():
        raise Undecidable(
            "`tool_input.workdir` is present but is not a usable directory "
            f"({workdir!r}), so the directory this command runs in — and therefore what "
            "its relative paths mean — is not derivable.")
    if any(marker in workdir for marker in ("$", "`", "*", "?")):
        raise Undecidable(
            f"`tool_input.workdir` is {workdir!r}, which needs a shell to resolve. The "
            "execution directory has to be known before a relative target can be placed "
            "in the repository.")

    # A relative workdir is relative to the session's cwd, which is the only anchor there
    # is. Without one, a relative workdir names nothing.
    if not os.path.isabs(workdir):
        if not cwd:
            raise Undecidable(
                f"`tool_input.workdir` is the relative path {workdir!r} and the payload "
                "carries no `cwd` to resolve it against.")
        workdir = os.path.join(cwd, workdir)

    resolved = os.path.realpath(workdir)
    if not os.path.isdir(resolved):
        raise Undecidable(
            f"`tool_input.workdir` names {workdir!r}, which is not an existing "
            "directory. A command whose execution directory does not exist has no "
            "derivable target for any relative path it carries.")
    return resolved


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

    # 🔴 A payload declaring a schema this parser does not implement is refused. Its
    # fields may mean something other than what is read below, and reading them anyway
    # is guessing about the one input the whole decision rests on.
    declared = payload.get("hook_schema_version")
    if declared is not None and str(declared) not in SUPPORTED_PAYLOAD_SCHEMAS:
        raise Undecidable(
            f"payload declares hook_schema_version={declared!r}; this guard implements "
            + ", ".join(sorted(SUPPORTED_PAYLOAD_SCHEMAS))
            + ". A schema this parser does not implement is not a schema it may read "
              "leniently.")

    # 🔴 An unknown top-level key is RECORDED, not refused, and the distinction was
    # settled by the live runtime within a minute of the first draft.
    #
    # The first draft denied on any key outside KNOWN_PAYLOAD_KEYS. Claude Code 2.1.232
    # sends `effort` and `prompt_id`, neither of which appears in the input-schema table
    # this protocol § 2 says it MEASURED out of the installed runtimes — so the rule
    # refused every command in the session that wrote it, immediately, including the one
    # that would have diagnosed it.
    #
    # That is a real finding about the schema table and a bad rule. The reconciliation
    # is about WHERE the key is. The decision rests on `tool_name`, `tool_input`, `cwd`
    # and `hook_event_name`; an unknown SIBLING of those does not change what they mean,
    # while an unknown key inside `tool_input` sits in the object the command is read
    # out of and can change which key that is. So:
    #
    #   unknown key beside the decision fields  → UNMEASURED, recorded, does not deny
    #   unknown key inside tool_input           → Undecidable, denies (see command_text)
    #
    # Denying on a sibling would make the guard fail on every runtime release, and a
    # guard that fails on every release is a guard that gets disabled.
    unmeasured_keys = sorted(set(payload) - KNOWN_PAYLOAD_KEYS)

    tool_name = payload.get("tool_name")
    if not isinstance(tool_name, str) or not tool_name:
        raise Undecidable("payload carries no `tool_name`")

    extra = {
        name.strip() for name in os.environ.get(EXTRA_SHELL_TOOLS_ENV, "").split(",")
        if name.strip()
    }
    known = set(SHELL_TOOLS) | CODE_MODE_TOOLS | PATCH_TOOLS | extra
    if tool_name not in known:
        raise Undecidable(
            f"`{tool_name}` is not a tool this guard knows.\n\n"
            "Either this hook is registered against tools it does not police — scope the "
            "matcher — or the runtime has renamed its shell tool, in which case the "
            "guard has stopped covering the shell and must be taught the new name in "
            "framework/scripts/pre_tool_use_guard.py:SHELL_TOOLS.\n\n"
            f"{EXTRA_SHELL_TOOLS_ENV} adds a name to the POLICED set; there is no "
            "variable that removes one."
        )

    tool_input = payload.get("tool_input")

    # 🔴 The base every relative target is placed against, and the ONE value that must be
    # right for the whole prediction to mean anything. `PREDICTED_TARGET_BASE ==
    # ACTUAL_EXECUTION_BASE` is the invariant; `derive_workdir` establishes it or denies.
    #
    # `(command, its own tool_input)` pairs: under code mode each inner call carries its
    # own `workdir`, so the base is per-command and not per-payload.
    if tool_name in CODE_MODE_TOOLS:
        calls = code_mode_commands(program_text(tool_input))
    elif tool_name in PATCH_TOOLS:
        # An envelope is policed as the `apply_patch` shell form, which the policy already
        # knows how to read: it names its own targets.
        calls = [("apply_patch <<'PATCH'\n" + program_text(tool_input) + "\nPATCH",
                  tool_input)]
    else:
        calls = [(command_text(tool_input), tool_input)]

    for command, carrier in calls:
        workdir = derive_workdir(payload, carrier)
        root = repo_root_of(workdir)
        reason = guard_policy.verdict(command, cwd=workdir or None, repo_root=root)
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
