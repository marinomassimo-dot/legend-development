#!/usr/bin/env python3
"""Which worktree is THIS ACTOR'S, asked of something the model does not author.

Revision 9 derived the assigned worktree from `git rev-parse --show-toplevel` run in
the EFFECTIVE WORKING DIRECTORY, and the effective working directory comes from
`tool_input.workdir` — a field the model writes. So the model chose the reference frame,
and the frame decides which subdivision of the repository is "mine". Measured on
2026-08-29 against the revision-9 engine, at ordinary `SHELL_DEFAULT`:

```text
workdir=<PEER_WORKTREE>     git add framework/probe.md            ALLOW
workdir=<PEER_WORKTREE>     git commit -m x framework/probe.md    ALLOW
workdir=<SHARED_CHECKOUT>   git add CLAUDE.md                     ALLOW
workdir=<SHARED_CHECKOUT>   git commit -m x CLAUDE.md             ALLOW
cwd=<PEER_WORKTREE>         git add framework/probe.md            ALLOW
cwd=<SHARED_CHECKOUT>       git commit -m x CLAUDE.md             ALLOW
code mode, inner workdir=<PEER_WORKTREE>, git add                 ALLOW

git -C <PEER_WORKTREE> commit -m x framework/probe.md             DENY
```

The last line is the tell. The same act, spelled as a retargeted subcommand, was refused;
spelled as a rotation of the execution frame it was granted. That is not a hole in the
authority table — the table is right, and `PEER_WORKTREE` reaches no rung of it. Rotating
the frame removes the target from the confined class **before the table is consulted**,
because the peer stops being a peer and becomes the assignment.

## The distinction this module exists to hold open

```text
EXECUTION_WORKDIR      where the command runs. Model-selected. Decides what a RELATIVE
                       path means, and nothing else.
ASSIGNED_WORKTREE      which worktree this actor was given. Session-bound. Decides the
                       AUTHORITY PERIMETER, and is never read out of a tool payload.
```

> **MODEL-SELECTED EXECUTION LOCATION MUST NOT CHANGE THE ACTOR'S AUTHORITY PERIMETER.**

`repo_topology.of_assigned` takes the second; `guard_policy.classify_target` takes both
and keeps them apart. If the two ever collapse again, the mutation operators
`ASSIGNED_FROM_WORKDIR` and `ASSIGNED_FROM_CWD` in `mutate_guard_suite.py` are what says so.

## The sources, and why each one is not the model's to write

Tried in the order below. The FIRST that resolves to a git working tree wins, and the
source that answered travels with the answer, because "the guard decided I own this
directory" is only reviewable beside "and it learned that from here".

| # | source | who writes it | why it is not model-controlled |
|---|---|---|---|
| 1 | `assigned=` argument | the adapter, or a fixture | the caller has already done this derivation, or IS the test declaring its own scene |
| 2 | `LEGEND_ASSIGNED_WORKTREE` | the operator or the launcher | a shell command's exports do not reach the hook process: the runtime spawns the hook from ITS environment, not from the model's shell |
| 3 | `CLAUDE_PROJECT_DIR` | claude-code, for every hook process | the runtime sets it from the directory the session was opened in; `.claude/settings.json` already names the guard through it |
| 4 | `payload["workspace_root"]` | a runtime, in the payload ENVELOPE | the model authors `tool_input`; it does not author the envelope around it |
| — | nothing resolved | — | `UNDERIVABLE` — and a mutating effect under an underivable assignment is refused |

🔴 **Row 2 depends on row R7 and would be a hole without it.** An environment variable is
outside the model's reach only while the model cannot edit the file that sets the
runtime's environment. `.claude/settings.json` has an `env` block, and revision 9 allowed
ordinary shell writes to it. `effect_model.RUNTIME_CONFIG` is what closes that, and the
two repairs are load-bearing for each other: without the confinement this table's second
row is writable, and without this table the confinement protects a binding nobody reads.

🔴 **`payload["cwd"]` is deliberately NOT a source.** It is the session's working
directory, and a `cd` moves it. A binding that a `cd` can move is the defect with one
more step in it.

## What UNDERIVABLE costs, and why it is the right cost

An actor whose assignment cannot be established keeps every READ and loses every write
into repository space — including into the directory it is standing in, because "the
directory it is standing in" is exactly the claim that could not be checked. Scratch
writes survive: scratch is a property of the path, not of the repository, and refusing
`echo x > /tmp/f` because a hook could not read an environment variable is how a guard
gets turned off.
"""
from __future__ import annotations

import os
import posixpath
import subprocess
from typing import Dict, List, Optional, Tuple

#: The value of an assignment that no source could supply. Never `""` and never `None`
#: at the reporting boundary: both compare equal to "not asked yet", and this must not.
UNDERIVABLE = "UNDERIVABLE"

#: Source names, in precedence order. Reported verbatim so a receipt records WHICH
#: binding answered, not merely that one did.
CALLER = "CALLER"                      # an explicit `assigned=` argument
OPERATOR_ENV = "OPERATOR_ENV"          # LEGEND_ASSIGNED_WORKTREE
RUNTIME_ENV = "RUNTIME_ENV"            # CLAUDE_PROJECT_DIR
RUNTIME_PAYLOAD = "RUNTIME_PAYLOAD"    # payload["workspace_root"]
NONE = "NONE"

SOURCES: Tuple[str, ...] = (CALLER, OPERATOR_ENV, RUNTIME_ENV, RUNTIME_PAYLOAD, NONE)

#: The operator/launcher binding. Named LEGEND_ rather than reusing a runtime's variable
#: so that setting it is always a deliberate act by whoever starts the session.
OPERATOR_ENV_VAR = "LEGEND_ASSIGNED_WORKTREE"
#: claude-code sets this for every hook process. Observed: `.claude/settings.json` in
#: this repository registers the guard as `$CLAUDE_PROJECT_DIR/scripts/guard_bash_command.py`,
#: and that registration resolves — which is what makes it a measurement rather than a hope.
RUNTIME_ENV_VAR = "CLAUDE_PROJECT_DIR"
#: A declared extension point in `pre_tool_use_guard.KNOWN_PAYLOAD_KEYS`. Ranked BELOW
#: the observed variable precisely because it is declared and not yet observed on any
#: wire: an unobserved field that outranked an observed one would be a precedence rule
#: written for a runtime nobody has measured.
PAYLOAD_KEY = "workspace_root"


class Assignment:
    """The worktree this actor was given, and the source that said so."""

    __slots__ = ("worktree", "source", "detail")

    def __init__(self, worktree: Optional[str], source: str, detail: str = "") -> None:
        self.worktree = worktree or None
        self.source = source
        self.detail = detail

    @property
    def ok(self) -> bool:
        return self.worktree is not None

    def as_dict(self) -> Dict[str, str]:
        return {
            "session_assigned_worktree": self.worktree or UNDERIVABLE,
            "session_assigned_worktree_source": self.source,
            "detail": self.detail,
        }

    def __repr__(self) -> str:  # pragma: no cover - diagnostics only
        return f"Assignment({self.worktree!r}, {self.source})"


UNBOUND = Assignment(None, NONE, "no trusted source supplied an assigned worktree")


def _git_toplevel(path: str) -> Optional[str]:
    """The working-tree root containing `path`, or None.

    A candidate that names a SUBDIRECTORY of a worktree still binds the worktree — that
    is what `CLAUDE_PROJECT_DIR` does when a session is opened below the root — but a
    candidate outside any working tree binds nothing and is not guessed at.
    """
    try:
        result = subprocess.run(["git", "-C", path, "rev-parse", "--show-toplevel"],
                                capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    root = result.stdout.strip()
    if result.returncode != 0 or not root:
        return None
    return posixpath.normpath(os.path.realpath(root))


def _usable(raw: object) -> Optional[str]:
    """A candidate is usable when it is an absolute, existing directory naming no shell.

    🔴 The expansion check is the same one `derive_workdir` applies to `workdir`, and for
    the same reason one level up: a binding that needs a shell to resolve is a binding
    established by running something, and the authority perimeter has to be known before
    anything runs.
    """
    if not isinstance(raw, str):
        return None
    value = raw.strip()
    if not value:
        return None
    if any(marker in value for marker in ("$", "`", "*", "?")):
        return None
    value = os.path.expanduser(value)
    if not posixpath.isabs(value):
        return None
    return value if os.path.isdir(value) else None


def candidates(payload: Optional[dict] = None,
               env: Optional[Dict[str, str]] = None,
               assigned: Optional[str] = None) -> List[Tuple[str, object]]:
    """`(source, raw value)` for every source, in precedence order. Pure."""
    env = os.environ if env is None else env
    payload = payload if isinstance(payload, dict) else {}
    return [
        (CALLER, assigned),
        (OPERATOR_ENV, env.get(OPERATOR_ENV_VAR)),
        (RUNTIME_ENV, env.get(RUNTIME_ENV_VAR)),
        (RUNTIME_PAYLOAD, payload.get(PAYLOAD_KEY)),
    ]


def derive(payload: Optional[dict] = None, env: Optional[Dict[str, str]] = None,
           assigned: Optional[str] = None) -> Assignment:
    """The session-bound assigned worktree, or `UNBOUND`. Never raises.

    🔴 A candidate that is present and does NOT resolve to a working tree does not fall
    through silently — the fall-through is recorded in `detail`, so "the operator set the
    variable to the wrong directory" and "nobody set anything" are different sentences.
    """
    rejected: List[str] = []
    for source, raw in candidates(payload, env, assigned):
        if raw is None:
            continue
        usable = _usable(raw)
        if usable is None:
            rejected.append(f"{source} is set and is not an absolute existing directory")
            continue
        root = _git_toplevel(usable)
        if root is None:
            rejected.append(f"{source} names a directory that is not inside a git working tree")
            continue
        return Assignment(root, source, "; ".join(rejected))
    return Assignment(None, NONE, "; ".join(rejected) or UNBOUND.detail)


# ── caching ────────────────────────────────────────────────────────────────────────
#
# 🔴 Keyed on the inputs, not global. A hook process handles one payload and exits, but
# the suites drive many scenes in one interpreter, and a global would make the second
# scene inherit the first one's binding — which is the collapse this module exists to
# prevent, reintroduced by its own cache.

_CACHE: Dict[Tuple[str, str, str], Assignment] = {}


def cached(payload: Optional[dict] = None, env: Optional[Dict[str, str]] = None,
           assigned: Optional[str] = None) -> Assignment:
    env = os.environ if env is None else env
    payload = payload if isinstance(payload, dict) else {}
    key = (str(assigned or ""),
           str(env.get(OPERATOR_ENV_VAR) or "") + "\x00" + str(env.get(RUNTIME_ENV_VAR) or ""),
           str(payload.get(PAYLOAD_KEY) or ""))
    if key not in _CACHE:
        _CACHE[key] = derive(payload, env, assigned)
    return _CACHE[key]


def reset() -> None:
    """Forget every derived assignment. Called by fixtures, never by the hook path."""
    _CACHE.clear()


def describe(payload: Optional[dict] = None,
             env: Optional[Dict[str, str]] = None) -> str:  # pragma: no cover - CLI
    found = derive(payload, env)
    lines = [f"SESSION_ASSIGNED_WORKTREE  {found.worktree or UNDERIVABLE}",
             f"SOURCE                     {found.source}"]
    if found.detail:
        lines.append(f"DETAIL                     {found.detail}")
    lines.append("")
    lines.append("candidates, in precedence order:")
    for source, raw in candidates(payload, env):
        shown = "<unset>" if raw is None else repr(raw)
        lines.append(f"  {source:<18} {shown}")
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:  # pragma: no cover - CLI
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.parse_args(argv)
    print(describe())
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI
    raise SystemExit(main())
