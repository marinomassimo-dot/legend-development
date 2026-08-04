#!/usr/bin/env python3
"""PreToolUse guard for Bash: two failures that already happened, made impossible.

Both of these were committed in this repository on 2026-08-04 by an agent that had
every relevant instruction in front of it. An instruction that can be bypassed by
choosing a different tool is not a control; this is the control.

**1. Blanket staging.** `git add -A` staged another actor's uncommitted work — a blind
derivation run in progress — into a commit whose message described something else
entirely. The author never saw the files. Blanket staging assumes the working tree
belongs to one actor, and in this repository it does not: Claude and Codex work in it
concurrently. Stage paths you name.

**2. Inline heredoc writes.** The `Write` tool refuses to overwrite a file the session
has not read. That guard was bypassed by doing the write from Bash instead —
`python3 - <<'PY' ... Path(x).write_text(...)` — which destroyed a file another actor
had authored and declared. The guard existed; the shell was the way around it. Use
`Write`/`Edit`, whose read-before-overwrite rule is the point, or invoke a committed
script by name.

Temp-only writes are allowed: scratchpad and /tmp work is not what went wrong.
"""
from __future__ import annotations

import json
import re
import sys

BLANKET_STAGING = re.compile(
    r"""\bgit\s+
        (?:
            add\s+(?:-A\b|--all\b|(?:-[A-Za-z]*\s+)*\.\s*(?:$|[;&|]))
          | commit\s+(?:[^;&|]*\s)?(?:-a\b|--all\b|-[a-zA-Z]*a[a-zA-Z]*\b)
        )""",
    re.VERBOSE,
)

# `python3 - <<EOF`, `python <<'PY'`, `cat <<EOF > file` — a script body fed on stdin.
HEREDOC = re.compile(r"<<-?\s*['\"]?\w+['\"]?")
INLINE_INTERPRETER = re.compile(r"\b(?:python3?|perl|ruby|node)\s+-\s*(?=<<)")

WRITE_PRIMITIVE = re.compile(
    r"""\.write_text\s*\(
      | \.write_bytes\s*\(
      | \bopen\s*\([^)]*['"][wa]b?\+?['"]
      | \bjson\.dump\s*\(
      | \bshutil\.(?:copy|move|copyfile|copy2)\s*\(
      | \bos\.replace\s*\(
      | \bPath\s*\([^)]*\)\s*\.\s*write
    """,
    re.VERBOSE,
)

# A write is tolerated when every path literal in the command is scratch space.
TEMP_PATH = re.compile(r"['\"](?:/private)?/tmp/[^'\"]*['\"]|['\"][^'\"]*scratchpad[^'\"]*['\"]")
PATH_LITERAL = re.compile(r"['\"][^'\"\n]*\.[A-Za-z0-9]{1,6}['\"]")

DENY_STAGING = (
    "Blanket staging is blocked in this repository.\n\n"
    "`git add -A` / `git add .` / `git commit -a` stage everything in the working tree, "
    "including work another actor has in flight. That is not hypothetical here: it "
    "already happened, and put an unreviewed blind-derivation run inside a commit whose "
    "message described unrelated work.\n\n"
    "Stage the paths you actually changed:  git add <path> [<path> ...]\n"
    "Check first with:  git status --short"
)

DENY_INLINE_WRITE = (
    "Writing repository files from an inline heredoc is blocked.\n\n"
    "The Write tool refuses to overwrite a file this session has not read. Doing the "
    "same write from Bash bypasses that guard — which is how a file authored and "
    "declared by another actor was destroyed unread.\n\n"
    "Use Write or Edit (they enforce read-before-overwrite), or invoke a committed "
    "script by name. Heredoc writes confined to /tmp or the scratchpad are allowed."
)


QUOTED = re.compile(r"'[^']*'|\"[^\"]*\"", re.S)


def _outside_quotes(command: str) -> str:
    """Blank out quoted spans so message text is not read as an invocation.

    Found by the guard blocking the very commit that documented it: the message
    quoted `git add -A` as an example, and substring matching cannot tell an
    example from a command. A real blanket-staging invocation is never quoted.
    """
    return QUOTED.sub(lambda m: " " * len(m.group(0)), command)


def verdict(command: str) -> str | None:
    """Return a denial reason, or None to allow."""
    if BLANKET_STAGING.search(_outside_quotes(command)):
        return DENY_STAGING

    is_inline = bool(HEREDOC.search(command)) and bool(INLINE_INTERPRETER.search(command))
    if is_inline and WRITE_PRIMITIVE.search(command):
        literals = PATH_LITERAL.findall(command)
        temp_only = bool(literals) and all(TEMP_PATH.fullmatch(p) for p in literals)
        if not temp_only:
            return DENY_INLINE_WRITE
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never block on a malformed payload
    command = str((payload.get("tool_input") or {}).get("command", ""))
    reason = verdict(command)
    if reason is None:
        return 0
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
