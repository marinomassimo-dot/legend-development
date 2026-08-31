#!/usr/bin/env python3
"""WHERE the guard is registered, WHICH engine that resolves to, and what a live probe
would have to observe before it could claim anything. Nothing here deploys anything.

## The two defects this module was written for

**R3 — the revision-9 registration is structurally impossible.** It registers

```toml
command = "python3 framework/scripts/pre_tool_use_guard.py"
```

a RELATIVE path, in a `.codex` that lives on the candidate branch. codex-cli 0.147.0
resolves the project config layer through git to the SHARED CHECKOUT, so:

```text
where the config is read   →  the engine is absent   (main carries the legacy guard)
where the engine exists    →  the config is not read (a linked worktree's .codex never is)
```

and the relative path additionally resolves against whatever directory the runtime
happens to be in. A registration that names its engine relatively is a registration that
names a different file depending on who asks.

**R2 — the revision-9 probe cannot tell which guard answered.** Its named discriminator,
`"Blanket staging is blocked in this repository."`, is byte-identical in the legacy
single-file guard and in `guard_policy.py`; all four of its proposed commands return the
same verdict under both. So it could report `FIRING = YES` while measuring the engine the
candidate replaces. `test_runtime_diagnostics.py` asserts the byte-identity, so this is a
property of the objects rather than a claim about them.

## What a registration must be able to prove

```text
CONFIG_SOURCE           the file the runtime actually reads for this cwd
REGISTERED_ENGINE_PATH  the string that file contains
RESOLVED_ENGINE_PATH    that string, anchored deterministically
ENGINE_HASH             sha256 of the file it resolves to
GUARD_GENERATION        derived from the shape of the engine it resolves to
```

with the anchoring itself classified, because *that* is where revision 9 failed:

| anchoring | what fixes the base | deterministic |
|---|---|---|
| `ABSOLUTE` | nothing to fix | **yes**, and machine-specific |
| `RUNTIME_ANCHORED` | a variable the runtime sets — `$CLAUDE_PROJECT_DIR` | **yes**, while that runtime defines it |
| `UNANCHORED` | the process's cwd, whatever it is | 🔴 **no** |

The Claude side is already `RUNTIME_ANCHORED`: `.claude/settings.json` registers
`$CLAUDE_PROJECT_DIR/scripts/guard_bash_command.py`, and the equivalence this module
enforces is that the Codex side must reach the same strength before a probe may count.

## Not deployed, and no route selected

`ROUTES` compares the four placements against the properties that distinguish them,
including — new in revision 10 — whether ordinary shell authority can still rewrite them.
`effect_model.RUNTIME_CONFIG` changed that column for B and C: they were `SHELL_MUTABLE`
under revision 9 and Mirror measured it. Choosing among the four is
`ARCHITECTURE_DECISION_REQUIRED` and remains the operator's.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard_revision  # noqa: E402

UNDERIVABLE = "UNDERIVABLE"

ABSOLUTE = "ABSOLUTE"
RUNTIME_ANCHORED = "RUNTIME_ANCHORED"
UNANCHORED = "UNANCHORED"
ANCHORINGS: Tuple[str, ...] = (ABSOLUTE, RUNTIME_ANCHORED, UNANCHORED)

#: Variables a runtime sets for its own hook processes, so a path anchored to one is
#: anchored to something the model does not write. `CLAUDE_PROJECT_DIR` is observed:
#: `.claude/settings.json` in this repository uses it and the registration resolves.
RUNTIME_ANCHORS: Tuple[str, ...] = ("CLAUDE_PROJECT_DIR", "CODEX_PROJECT_DIR",
                                    "CODEX_WORKSPACE_ROOT")

#: `$VAR` / `${VAR}` at the head of a path.
_ANCHOR = re.compile(r"^\$\{?([A-Z_][A-Z0-9_]*)\}?/")

#: The interpreter words a registration puts in front of its engine. The ENGINE is the
#: first operand that looks like a path to a `.py` file — reading `argv[0]` would report
#: `python3` as the registered engine, which is true and useless.
_INTERPRETERS = frozenset({"python", "python3", "python3.11", "python3.12", "uv", "sh",
                           "bash", "node", "deno"})


# ── the four placements, and what distinguishes them ───────────────────────────────

PROPERTIES: Tuple[str, ...] = (
    "VERSIONED", "REVIEWABLE", "PORTABLE", "MACHINE_LOCAL",
    "SHELL_MUTABLE", "GOVERNED", "FRESH_CLONE_REPRODUCIBLE",
)

#: 🔴 `SHELL_MUTABLE` is the column revision 10 changed, and it is the reason the route
#: comparison had to be re-run rather than quoted. Under revision 9, Mirror measured
#: ordinary `SHELL_DEFAULT` writing `~/.claude/settings.json` and `~/.codex/config.toml`
#: and deleting `~/.codex` — so routes B and C registered the guard in a file the guard
#: let the actor rewrite. `effect_model.RUNTIME_CONFIG` closes that, and the honest way
#: to say so is that the column is now `no` for all four **and that this is a property of
#: revision 10 being installed**, not of the placement.
#:
#: `GOVERNED` asks whether a CHANGE to the placement passes a review surface. A and B and
#: C are refused-but-ungoverned: nothing reviews them, an operator simply does them.
ROUTES: Dict[str, Dict[str, object]] = {
    "A": {
        "name": "untracked/gitignored `.codex` at the shared checkout",
        "config_path": "<SHARED_CHECKOUT>/.codex/config.toml",
        "VERSIONED": False, "REVIEWABLE": False, "PORTABLE": False,
        "MACHINE_LOCAL": True, "SHELL_MUTABLE": False, "GOVERNED": False,
        "FRESH_CLONE_REPRODUCIBLE": False,
        "shell_mutable_because": "SHARED_CHECKOUT scope — confined since revision 9",
    },
    "B": {
        "name": "user-level `~/.codex/config.toml`",
        "config_path": "<HOME>/.codex/config.toml",
        "VERSIONED": False, "REVIEWABLE": False, "PORTABLE": False,
        "MACHINE_LOCAL": True, "SHELL_MUTABLE": False, "GOVERNED": False,
        "FRESH_CLONE_REPRODUCIBLE": False,
        "shell_mutable_because": "RUNTIME_CONFIG scope — confined in revision 10; it was "
                                 "WRITABLE under revision 9 and Mirror measured it",
    },
    "C": {
        "name": "managed `CODEX_HOME`",
        "config_path": "<CODEX_HOME>/config.toml",
        "VERSIONED": False, "REVIEWABLE": False, "PORTABLE": True,
        "MACHINE_LOCAL": False, "SHELL_MUTABLE": False, "GOVERNED": False,
        "FRESH_CLONE_REPRODUCIBLE": False,
        "shell_mutable_because": "RUNTIME_CONFIG scope — the override is read from the "
                                 "same environment, so a managed home is a member too",
    },
    "D": {
        "name": "tracked `.codex` on development main",
        "config_path": "<SHARED_CHECKOUT>/.codex/config.toml (tracked)",
        "VERSIONED": True, "REVIEWABLE": True, "PORTABLE": True,
        "MACHINE_LOCAL": False, "SHELL_MUTABLE": False, "GOVERNED": True,
        "FRESH_CLONE_REPRODUCIBLE": True,
        "shell_mutable_because": "SHARED_CHECKOUT scope, and a change to it is a commit "
                                 "on the protected branch",
    },
}

#: 🔴 NOT a selection. It records which routes a probe may rely on for the ONE property
#: the probe needs — that the registration it measured is the registration that will
#: still be there — and it is empty of preference between the two that qualify.
ROUTE_SELECTED: Optional[str] = None


# ── reading a registration ─────────────────────────────────────────────────────────

class Registration:
    """One registered engine, and everything needed to say whether it is the right one."""

    __slots__ = ("config_source", "registered_path", "resolved_path", "anchoring",
                 "engine_hash", "guard_generation", "detail")

    def __init__(self, config_source: str = "", registered_path: str = "",
                 resolved_path: str = "", anchoring: str = UNANCHORED,
                 engine_hash: str = UNDERIVABLE, guard_generation: str = UNDERIVABLE,
                 detail: str = "") -> None:
        self.config_source = config_source
        self.registered_path = registered_path
        self.resolved_path = resolved_path
        self.anchoring = anchoring
        self.engine_hash = engine_hash
        self.guard_generation = guard_generation
        self.detail = detail

    @property
    def deterministic(self) -> bool:
        """Does this registration name the same file whoever asks?"""
        return self.anchoring in (ABSOLUTE, RUNTIME_ANCHORED)

    def as_dict(self) -> Dict[str, str]:
        return {
            "CONFIG_SOURCE": self.config_source or UNDERIVABLE,
            "REGISTERED_ENGINE_PATH": self.registered_path or UNDERIVABLE,
            "RESOLVED_ENGINE_PATH": self.resolved_path or UNDERIVABLE,
            "ANCHORING": self.anchoring,
            "ENGINE_HASH": self.engine_hash,
            "GUARD_GENERATION": self.guard_generation,
            "DETAIL": self.detail,
        }


def engine_of(command: str) -> str:
    """The engine path inside a registration command line.

    `python3 $CLAUDE_PROJECT_DIR/scripts/guard_bash_command.py` registers the second
    word, not the first. Reading `argv[0]` would report the interpreter, and a
    registration check that compares interpreters compares nothing.
    """
    try:
        import shlex
        words = shlex.split(command)
    except ValueError:
        return ""
    for word in words:
        if word.startswith("-"):
            continue
        if posixpath.basename(word) in _INTERPRETERS:
            continue
        return word
    return ""


def classify_anchoring(path: str) -> str:
    """`ABSOLUTE`, `RUNTIME_ANCHORED` or `UNANCHORED`. Pure, and the whole of R3.

    🔴 A relative path is `UNANCHORED` even when it happens to resolve today. What makes
    it unanchored is that the base is the process's cwd, and the process is a hook the
    runtime starts wherever it likes — the same class of mistake as deriving the assigned
    worktree from the effective workdir, one layer out.
    """
    if not path:
        return UNANCHORED
    if posixpath.isabs(path):
        return ABSOLUTE
    match = _ANCHOR.match(path)
    if match and match.group(1) in RUNTIME_ANCHORS:
        return RUNTIME_ANCHORED
    return UNANCHORED


def resolve_engine(path: str, env: Optional[Dict[str, str]] = None) -> Tuple[str, str]:
    """`(resolved absolute path, detail)`. An unanchored path resolves to nothing."""
    env = dict(os.environ if env is None else env)
    anchoring = classify_anchoring(path)
    if anchoring == ABSOLUTE:
        return posixpath.normpath(path), ""
    if anchoring == RUNTIME_ANCHORED:
        match = _ANCHOR.match(path)
        name = match.group(1) if match else ""
        base = env.get(name) or ""
        if not base:
            return "", f"the registration is anchored to ${name}, which is not set here"
        return posixpath.normpath(posixpath.join(base, path[match.end():])), ""
    return "", ("the registration names a RELATIVE path, which resolves against "
                "whatever directory the runtime starts the hook in")


#: A `command = "..."` assignment, wherever it sits. Read textually for the same reason
#: `codex_hook_state` reads its config textually: `tomllib` arrived in 3.11 and the guard
#: runs on whatever interpreter the runtime brings.
#:
#: 🔴 NOT anchored to the start of a line. This repository's own `.codex` registers its
#: hooks in INLINE tables — `{ type = "command", command = "python3 …" }` — and a
#: line-anchored pattern read that file as naming no command at all, which is a
#: registration checker reporting "nothing registered" about a file with five
#: registrations in it. The `\b` keeps it off the `type = "command"` VALUE, which is the
#: word this pattern would otherwise collide with.
_COMMAND_LINE = re.compile(r'\bcommand\s*=\s*(?:"([^"]*)"|\'([^\']*)\')')
_JSON_COMMAND = re.compile(r'"command"\s*:\s*"((?:[^"\\]|\\.)*)"')


def read_registration(config_path: str,
                      env: Optional[Dict[str, str]] = None) -> Registration:
    """Read one config file and report what it registers. Never raises.

    Handles the TOML `command = "…"` shape and the JSON `"command": "…"` shape, because
    the two runtimes register the same engine in different files.
    """
    source = Path(config_path)
    try:
        text = source.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return Registration(config_source=str(source), detail=str(exc))

    match = _COMMAND_LINE.search(text) or _JSON_COMMAND.search(text)
    if not match:
        return Registration(config_source=str(source),
                            detail="the config names no hook `command`")
    command = next(group for group in match.groups() if group is not None)
    command = command.replace('\\"', '"')
    registered = engine_of(command)
    anchoring = classify_anchoring(registered)
    resolved, detail = resolve_engine(registered, env)

    engine_hash = UNDERIVABLE
    generation = UNDERIVABLE
    if resolved:
        try:
            engine_hash = hashlib.sha256(Path(resolved).read_bytes()).hexdigest()
        except OSError as exc:
            detail = detail or f"the resolved engine is not readable: {exc}"
        # The generation is a property of the WORKTREE the engine lives in, because a
        # guard is its whole module set and not one file.
        root = _worktree_of(resolved)
        if root:
            generation = guard_revision.generation_of(Path(root))
    return Registration(str(source), registered, resolved, anchoring,
                        engine_hash, generation, detail)


def _worktree_of(path: str) -> str:
    directory = path if os.path.isdir(path) else posixpath.dirname(path)
    try:
        out = subprocess.run(["git", "-C", directory, "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


# ── the REV10 discriminator, and its absence from the legacy engine ────────────────

def discriminators() -> Tuple[str, ...]:
    """Tokens that exist only in a revision-10 engine.

    Structured rather than prose: the revision-9 probe named a SENTENCE, and the sentence
    it named is byte-identical in the legacy guard. These are read out of the modules
    themselves so they cannot drift from what the guard actually emits.
    """
    import effect_model as em  # noqa: PLC0415 - avoids an import cycle at load
    import guard_policy as policy  # noqa: PLC0415
    import pre_tool_use_guard as adapter  # noqa: PLC0415
    return (
        f"{adapter.DECISION_TRAILER} GENERATION={adapter.GUARD_GENERATION}",
        f"DECISION_CODE={policy.CODE_RUNTIME_CONFIG}",
        f"DECISION_CODE={policy.confined_code(em.PEER_WORKTREE)}",
        f"DECISION_CODE={policy.CODE_NO_ASSIGNMENT}",
        "ASSIGNED_WORKTREE_SOURCE=",
    )


def legacy_blob(root: str, ref: str = "main") -> str:
    """The guard blob a named ref carries, read from git rather than from a description."""
    try:
        out = subprocess.run(
            ["git", "-C", root, "show", f"{ref}:{guard_revision.GUARD_ENTRY.as_posix()}"],
            capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout if out.returncode == 0 else ""


# ── the live probe, as preconditions and a verdict ─────────────────────────────────

NOT_FIRING = "NOT_FIRING"
LEGACY_FIRING = "LEGACY_FIRING"
REV10_FIRING = "REV10_FIRING"
REV10_ENFORCING = "REV10_ENFORCING"
PROBE_VERDICTS: Tuple[str, ...] = (NOT_FIRING, LEGACY_FIRING, REV10_FIRING,
                                   REV10_ENFORCING, UNDERIVABLE)

#: The seven things that must hold BEFORE a spend-bearing session is opened. Each is a
#: boolean the caller must supply from a measurement; there is no default that passes.
PRECONDITIONS: Tuple[Tuple[str, str], ...] = (
    ("PROBE_WORKTREE_IDENTIFIED",
     "the cwd the session will use resolves to a session-bound assigned worktree"),
    # 🔴 Revision 11. The precondition is that the worktree carries the CANDIDATE
    # engine, and the rung moved — a probe that confirmed `REV10` would be confirming
    # the engine this candidate replaces.
    ("GUARD_GENERATION_IS_REV12",
     "guard_revision reports REV12 for that worktree"),
    ("REGISTERED_ENGINE_PATH_RESOLVES",
     "the registration's engine path is ABSOLUTE or RUNTIME_ANCHORED and resolves"),
    ("REGISTERED_ENGINE_HASH_MATCHES",
     # 🔴 Revision 12 · D9. This said "the deployed revision-10 engine", two entries
     # below one revision 11 had deliberately moved — so the tuple asserted two different
     # generations at once and the declared `PROBE_VERDICT_NAMES` debt did not cover it.
     # It names the CURRENT rung rather than a number, so it cannot go stale again.
     "the resolved engine hashes to the deployed engine of the current generation"),
    ("HOOK_DISCOVERY_ESTABLISHED",
     "codex_hook_state reports the hook loaded, as far as a static query can say"),
    ("DISCRIMINATOR_ABSENT_FROM_LEGACY",
     "no revision-10 discriminator appears in the legacy guard blob"),
    ("NO_KNOWN_STRUCTURAL_BYPASS",
     "the candidate's hostile corpus reports zero bypasses, declared by the caller"),
)


def preconditions_met(observations: Dict[str, object]) -> Tuple[bool, List[str]]:
    """`(all met, the names that are not)`. A missing key is NOT met.

    🔴 `observations.get(name)` without the membership test would let a caller that
    forgot a precondition pass it, which is the same defect as a diagnostic that reads a
    failed query as an empty answer.
    """
    unmet = [name for name, _ in PRECONDITIONS if observations.get(name) is not True]
    return (not unmet), unmet


def classify_probe(observations: Dict[str, object]) -> str:
    """What a completed live probe actually established. A pure function.

    ```text
    REV10_GENERATION_CONFIRMED
      ∧ REV10_UNIQUE_DENIAL_OBSERVED
      ∧ FORBIDDEN_WRITE_DENIED
      ∧ AUTHORIZED_WRITE_ALLOWED
      ∧ OBSERVED_EFFECT == AUTHORIZED_EFFECT      →  REV10_ENFORCING
    ```

    and the four weaker answers below it, which revision 9's protocol could not tell
    apart because it collapsed everything into ALLOW/DENY:

    - nothing refused anything                            → `NOT_FIRING`
    - something refused, and it was not a revision-10 engine → `LEGACY_FIRING`
    - a revision-10-unique denial was observed, but the floor is not demonstrated
      (the authorised write was refused, or its effect did not match)  → `REV10_FIRING`
    - a required observation is missing                   → `UNDERIVABLE`

    🔴 `LEGACY_FIRING` is the answer revision 9 could not produce, and producing it is
    the whole point: a refusal carrying a sentence both engines contain is evidence that
    *a* guard ran, and no evidence at all about which.
    """
    required = ("FORBIDDEN_WRITE_DENIED", "AUTHORIZED_WRITE_ALLOWED",
                "REV10_GENERATION_CONFIRMED", "REV10_UNIQUE_DENIAL_OBSERVED",
                "OBSERVED_EFFECT_MATCHES_AUTHORIZED")
    if any(observations.get(name) is None for name in required):
        return UNDERIVABLE
    if observations.get("FORBIDDEN_WRITE_DENIED") is not True:
        return NOT_FIRING
    if not (observations.get("REV10_GENERATION_CONFIRMED") is True
            and observations.get("REV10_UNIQUE_DENIAL_OBSERVED") is True):
        # Something refused. Without a revision-10-unique token in the refusal, the
        # engine that refused is not identified, and the legacy guard refuses this too.
        return LEGACY_FIRING
    if (observations.get("AUTHORIZED_WRITE_ALLOWED") is True
            and observations.get("OBSERVED_EFFECT_MATCHES_AUTHORIZED") is True):
        return REV10_ENFORCING
    return REV10_FIRING


# ── reporting ──────────────────────────────────────────────────────────────────────

#: Column headings, abbreviated deliberately rather than truncated. A header cut to
#: `FRESH_CLONE` reads as a different property from `FRESH_CLONE_REPRODUCIBLE`, and a
#: reader has no way to tell that the difference is the terminal width.
_HEADINGS = {
    "VERSIONED": "VERSND", "REVIEWABLE": "REVWBL", "PORTABLE": "PORTBL",
    "MACHINE_LOCAL": "MACHLOC", "SHELL_MUTABLE": "SHMUTBL", "GOVERNED": "GOVRND",
    "FRESH_CLONE_REPRODUCIBLE": "FRESHCL",
}


def route_table() -> str:
    header = f"{'':<3}{'ROUTE':<52}" + "".join(f"{_HEADINGS[p]:<9}" for p in PROPERTIES)
    lines = [header, "-" * len(header)]
    for key in sorted(ROUTES):
        route = ROUTES[key]
        row = f"{key:<3}{str(route['name'])[:51]:<52}"
        row += "".join(f"{('yes' if route[p] else 'no'):<9}" for p in PROPERTIES)
        lines.append(row)
    lines.append("")
    lines.extend(f"  {p:<26} {_HEADINGS[p]}" for p in PROPERTIES)
    lines.append("")
    lines.append(f"ROUTE_SELECTED = {ROUTE_SELECTED or 'NONE — ARCHITECTURE_DECISION_REQUIRED'}")
    return "\n".join(lines)


#: The tool names a Codex registration polices. Kept beside the renderer so the emitted
#: file and the wire contract cannot drift: `pre_tool_use_guard.SHELL_TOOLS` and
#: `CODE_MODE_TOOLS` are the authority, and `test_runtime_diagnostics.py` asserts that
#: every Codex-side name in them appears in what this renders.
def _codex_tool_names() -> List[str]:
    import pre_tool_use_guard as adapter  # noqa: PLC0415
    codex = [name for name, runtime in adapter.SHELL_TOOLS.items() if runtime == "codex"]
    return sorted(set(codex) | adapter.CODE_MODE_TOOLS | adapter.PATCH_TOOLS)


def render_registration(engine_path: str) -> str:
    """The anchored Codex registration, as text, for an operator to place. NOT written.

    🔴 It PRINTS. Writing it would mean this module creating a file at
    `~/.codex/config.toml` or at the shared checkout — the first is `RUNTIME_CONFIG` and
    the second is `SHARED_CHECKOUT`, and both are scopes this guard refuses. A tool that
    installed its own registration would have to be exempt from the policy it installs,
    which is the shape of every control that turned out not to be one.

    `engine_path` must be ABSOLUTE. That is not fussiness: it is the entire R3 repair.
    An absolute path is fine for routes A, B and C because those files are machine-local
    and never committed; route D cannot use one — a tracked config may not carry this
    machine's directory layout — and therefore route D additionally requires a Codex
    runtime anchor variable, which is NOT measured and is recorded as unmeasured.
    """
    anchoring = classify_anchoring(engine_path)
    if anchoring == UNANCHORED:
        raise ValueError(
            f"{engine_path!r} is UNANCHORED. A registration that names a relative path "
            "resolves against whatever directory the runtime starts the hook in, which "
            "is the defect this renderer exists to stop reproducing.")
    lines = [
        "# LEGEND — Codex hook registration, EMITTED. Do not hand-edit the paths.",
        "# Rendered by framework/scripts/codex_registration.py --emit-registration.",
        f"# ANCHORING = {anchoring}",
        "",
    ]
    for tool in _codex_tool_names():
        lines.extend([
            "[[hooks.PreToolUse]]",
            f'matcher = "{tool}"',
            "[[hooks.PreToolUse.hooks]]",
            'type = "command"',
            f'command = "python3 {engine_path}"',
            "",
        ])
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:  # pragma: no cover - CLI
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", help="a config file to read a registration out of")
    parser.add_argument("--emit-registration", metavar="ENGINE",
                        help="print an ANCHORED registration for this absolute engine "
                             "path; it is never written, and never deployed from here")
    parser.add_argument("--routes", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.emit_registration:
        try:
            print(render_registration(args.emit_registration))
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        return 0
    if args.config:
        found = read_registration(args.config)
        print(json.dumps(found.as_dict(), indent=2) if args.json
              else "\n".join(f"{k:<24} {v}" for k, v in found.as_dict().items()))
        return 0 if found.deterministic else 1
    print(route_table())
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI
    raise SystemExit(main())
