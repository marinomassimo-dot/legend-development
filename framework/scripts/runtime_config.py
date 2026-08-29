#!/usr/bin/env python3
"""The files that decide whether this guard runs — resolved, not guessed at.

Mirror's independent corpus measured these against the revision-9 engine on 2026-08-29,
at ordinary `SHELL_DEFAULT`, from an actor worktree:

```text
echo x > <HOME>/.claude/settings.json     ALLOW
echo x > <CODEX_HOME>/config.toml         ALLOW
rm -rf  <CODEX_HOME>                      ALLOW
```

Those are the files a runtime reads to learn which `PreToolUse` hook to run.
`~/.claude/settings.json` additionally carries an `env` block, which is where
`session_binding`'s operator row comes from. So an actor governed by this policy could
rewrite the registration that makes the policy govern it — and nothing would look wrong
until the next process start, because the running hook is already loaded.

> **The ACTIVE guard registration must not be writable through the ordinary authority
> that the guard grants.**

## Why this is a resolution and not a prefix

The obvious rule — deny `~/.claude` and `~/.codex` — refuses a runtime's caches, session
transcripts, plugin data and scratch, none of which control anything. A guard that
refuses ordinary work is a guard that gets turned off, and this repository has written
that sentence down often enough to be held to it. So the scope is the **resolved active
control surface**:

```text
<CLAUDE_CONFIG_DIR or ~/.claude>/settings.json          the user hook registration
<CLAUDE_CONFIG_DIR or ~/.claude>/settings.local.json    the same, machine-local layer
<CODEX_HOME or ~/.codex>/config.toml                    the Codex hook registration
… plus any engine path a registration NAMES that lives outside the repository
```

and every **ancestor directory of a member**, because `rm -rf <CODEX_HOME>` destroys the
config without ever naming it. An ancestor is a member only as itself: `~/.codex` is in,
`~/.codex/sessions/x.jsonl` is not, and `~/notes.txt` is not.

🔴 **A member that does not exist yet is still a member.** Creating
`~/.codex/config.toml` where none existed IS the registration act, and a membership test
that stat-ed first would allow exactly the write that installs a hook of the actor's own
choosing.

## What is deliberately NOT in here

**The repository's own `.claude/settings.json`.** It is inside the assigned worktree,
where a shell write is already refused and the only route in is Write/Edit followed by a
named `git add` and a commit — which is a review surface, and the distinct governance
surface this scope is asking for. Pulling it in here would forbid landing a settings
change at all, and would make deployment route D unreachable by the actor who proposes it.

**Everything else under a runtime's home.** Caches, sessions, transcripts, plugin data,
scratch. They are not control surfaces and the corpus carries the positive control that
says so.

## When it cannot be resolved

`HOME` unset, or an override naming something unusable, yields `ok=False` and NO members.
That direction is deliberate and it is the *permissive* one, which is worth stating
plainly: a surface that could not be resolved cannot be protected, and pretending
otherwise by denying a guessed path would refuse ordinary work for a guarantee nobody has.
What `ok=False` buys is that the readiness table must then say
`RUNTIME_CONFIG_SELF_PROTECTION = UNDERIVABLE` rather than `PASS`, and
`codex_registration.py` refuses to call routes B and C self-protected.
"""
from __future__ import annotations

import json
import os
import posixpath
from typing import Dict, FrozenSet, Iterable, List, Optional, Tuple

#: The environment overrides each runtime honours for its own configuration home.
CLAUDE_HOME_ENV = "CLAUDE_CONFIG_DIR"
CODEX_HOME_ENV = "CODEX_HOME"

CLAUDE_HOME_DEFAULT = ".claude"
CODEX_HOME_DEFAULT = ".codex"

#: The registration files themselves, relative to each runtime's configuration home.
CLAUDE_REGISTRATION_FILES: Tuple[str, ...] = ("settings.json", "settings.local.json")
CODEX_REGISTRATION_FILES: Tuple[str, ...] = ("config.toml",)


class Surface:
    """The active runtime control surface, and whether it could be resolved at all."""

    __slots__ = ("members", "ancestors", "ok", "detail", "sources")

    def __init__(self, members: Iterable[str] = (), ok: bool = True,
                 detail: str = "", sources: Optional[Dict[str, str]] = None) -> None:
        self.members: FrozenSet[str] = frozenset(
            posixpath.normpath(m) for m in members if m)
        self.ok = ok
        self.detail = detail
        self.sources = dict(sources or {})
        self.ancestors: FrozenSet[str] = frozenset(_ancestors(self.members))

    def contains(self, path: str) -> bool:
        """Is this ABSOLUTE path the control surface, or a directory holding it?

        🔴 Not "is it under". Under would swallow a runtime's caches; equal-or-ancestor
        is exactly the set whose mutation can remove a registration, and nothing wider.
        """
        if not path or not posixpath.isabs(path):
            return False
        candidate = posixpath.normpath(path)
        return candidate in self.members or candidate in self.ancestors

    def as_dict(self) -> Dict[str, object]:
        return {
            "ok": self.ok,
            "detail": self.detail,
            "members": sorted(self.members),
            "ancestors": sorted(self.ancestors),
            "sources": dict(self.sources),
        }


def _ancestors(members: Iterable[str]) -> List[str]:
    """Every proper ancestor directory of every member, `/` excluded.

    `/` is excluded because a rule that made the filesystem root a control surface would
    classify every absolute path's root and say nothing useful; the members that matter
    are two or three directories deep and their ancestors stop well above that.
    """
    found = set()
    for member in members:
        current = posixpath.dirname(member)
        while current and current != "/" and current not in found:
            found.add(current)
            current = posixpath.dirname(current)
    return sorted(found)


def _home(env: Dict[str, str]) -> Optional[str]:
    home = env.get("HOME") or ""
    if not home:
        return None
    home = posixpath.normpath(os.path.expanduser(home))
    return home if posixpath.isabs(home) else None


def _config_home(env: Dict[str, str], override: str, home: Optional[str],
                 default: str) -> Optional[str]:
    raw = env.get(override) or ""
    if raw.strip():
        value = posixpath.normpath(os.path.expanduser(raw.strip()))
        return value if posixpath.isabs(value) else None
    return posixpath.join(home, default) if home else None


def resolve(env: Optional[Dict[str, str]] = None,
            extra: Iterable[str] = ()) -> Surface:
    """The active control surface for THIS process's environment. Never raises.

    `extra` carries engine paths a registration names — `codex_registration.py` supplies
    them once it has resolved one. They are members only when they lie outside every
    working tree, which that module decides; this one records what it is handed.
    """
    env = dict(os.environ if env is None else env)
    home = _home(env)
    sources: Dict[str, str] = {}
    rejected: List[str] = []

    claude_home = _config_home(env, CLAUDE_HOME_ENV, home, CLAUDE_HOME_DEFAULT)
    codex_home = _config_home(env, CODEX_HOME_ENV, home, CODEX_HOME_DEFAULT)

    members: List[str] = []
    if claude_home:
        sources["claude_config_home"] = claude_home
        members.extend(posixpath.join(claude_home, name)
                       for name in CLAUDE_REGISTRATION_FILES)
    else:
        rejected.append("the claude configuration home is not derivable")
    if codex_home:
        sources["codex_config_home"] = codex_home
        members.extend(posixpath.join(codex_home, name)
                       for name in CODEX_REGISTRATION_FILES)
    else:
        rejected.append("the codex configuration home is not derivable")

    for engine in extra:
        if isinstance(engine, str) and posixpath.isabs(engine):
            members.append(posixpath.normpath(engine))

    ok = bool(members) and not rejected
    return Surface(members, ok, "; ".join(rejected), sources)


# ── caching ────────────────────────────────────────────────────────────────────────
#
# Keyed on the two overrides plus HOME, so a fixture that moves them gets a fresh answer
# and a hook process that handles one payload pays for one resolution.

_CACHE: Dict[Tuple[str, str, str, Tuple[str, ...]], Surface] = {}


def cached(env: Optional[Dict[str, str]] = None,
           extra: Iterable[str] = ()) -> Surface:
    env = os.environ if env is None else env
    key = (str(env.get("HOME") or ""), str(env.get(CLAUDE_HOME_ENV) or ""),
           str(env.get(CODEX_HOME_ENV) or ""), tuple(sorted(extra)))
    if key not in _CACHE:
        _CACHE[key] = resolve(dict(env), extra)
    return _CACHE[key]


def reset() -> None:
    """Forget every resolved surface. Called by fixtures, never by the hook path."""
    _CACHE.clear()


def describe(env: Optional[Dict[str, str]] = None) -> str:  # pragma: no cover - CLI
    surface = resolve(env)
    lines = [f"RUNTIME_CONFIG_RESOLVED    {surface.ok}"]
    if surface.detail:
        lines.append(f"DETAIL                     {surface.detail}")
    lines.append("MEMBERS")
    lines.extend(f"  {m}" for m in sorted(surface.members))
    lines.append("ANCESTORS (a mutation of one of these removes a member)")
    lines.extend(f"  {a}" for a in sorted(surface.ancestors))
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:  # pragma: no cover - CLI
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    print(json.dumps(resolve().as_dict(), indent=2) if args.json else describe())
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI
    raise SystemExit(main())
