#!/usr/bin/env python3
"""ACTOR / RUNTIME / SESSION / WORKTREE binding, and what a resume may inherit.

`ACTOR_ID != RUNTIME != SESSION != TASK != WORKTREE != BRANCH != HEAD != AUTHORITY`.
Eight dimensions that this repository has watched collapse into one, every time by the
same mechanism: nobody asserted they were separate, so whichever was easiest to observe
stood in for the rest.

This module makes the collapse checkable. It derives the nine, binds them into one
fingerprint, and answers exactly two questions:

    ATTEST      are all nine derivable right now, and what do they hash to?
    REVALIDATE  is the binding in front of me the binding this authority was granted to?

## Why a resume is the interesting case, and why it is new in revision 8

A Codex session on 2026-08-28 exhausted its token budget, restarted, and came back
carrying context. Nothing in the bridge noticed, because nothing in the bridge was
looking: authority had been established once, at the start, and a restart is not a
start. Every field can change across that boundary — the runtime is re-launched and may
be a different version, the session identifier is new, the worktree may have been
switched by another actor, `HEAD` moves whenever anyone commits — and the *conversation*
looks continuous, which is precisely why it is not evidence.

So:

```
RESUME or DISCONTINUITY
  → re-derive all nine
  → any field CHANGED or UNDERIVABLE  → RESUME_BINDING_MISMATCH → FAIL_CLOSED
  → write authority revoked until a fresh attestation succeeds
```

🔴 **`UNDERIVABLE` fails the same as `CHANGED`.** A field nobody can read is not a field
that stayed the same. This is the rule that a "compare what we can see" implementation
gets wrong, and it gets it wrong in the permissive direction every time.

## What is declared and what is derived, and why the split is the whole point

| dimension | source | why |
|---|---|---|
| `actor` | DECLARED by the caller | there is no runtime fact that says which actor this is, and inventing one would be electing an actor — `runtime_parity.py` refuses to do that too |
| `task` | DECLARED | same |
| `authority` | DECLARED | an operator grant, never a runtime property |
| `runtime` | DERIVED | from the hook payload's own shape and the process environment |
| `runtime_version` | DERIVED | the version is a property of the SESSION, never of the machine (`cross_session_transport.md` § 3) |
| `session` | DERIVED | the runtime's own session identifier, when it emits one |
| `worktree` | DERIVED | `git rev-parse --show-toplevel` |
| `branch` | DERIVED | `git branch --show-current` |
| `head` | DERIVED | `git rev-parse HEAD` |

🔴 **Self-declaration alone is insufficient, and that is not solved by hashing it.** The
fingerprint binds the declared half to the derived half so a claim cannot travel to
another worktree, another branch or another `HEAD` — it does **not** make the declared
half true. An actor that says it is `orchestrator` is still only saying so. What this
buys is narrower and real: the claim is now *bound*, so it can be checked against the
same claim made earlier, and a resume that inherits it silently is caught.

## Where the store lives, and what that costs

The attestation store is **outside the repository**, under `~/.legend/attestation/` by
default, keyed by worktree path. Two reasons, and the second is the honest one:

1. a guard that writes into the repository it guards is refused by its own policy, and
   should be;
2. 🔴 therefore this is **runtime-local state, not a repository control**. It is not
   committed, not reviewed, and not present in a fresh clone. It detects a mismatch for
   the session that has the store; it proves nothing to anybody else, and a reader of
   the repository cannot verify it happened. `annex_j_runtime_control_plane.md` § J.0
   is the right place to read that class of non-guarantee.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import effect_model as em  # noqa: E402

#: The nine dimensions, in the order they are hashed. Order is part of the fingerprint,
#: so this tuple is the schema and reordering it invalidates every stored attestation —
#: which is the correct outcome, not a migration problem.
DIMENSIONS: Tuple[str, ...] = (
    "actor", "runtime", "runtime_version", "session",
    "task", "worktree", "branch", "head", "authority",
)

DECLARED: Tuple[str, ...] = ("actor", "task", "authority")
DERIVED: Tuple[str, ...] = ("runtime", "runtime_version", "session",
                            "worktree", "branch", "head")

#: The value of a dimension that could not be read. Never an empty string, never None:
#: both of those compare equal to each other and to "not set yet", and this must not.
UNDERIVABLE = "UNDERIVABLE"

SCHEMA = "legend_execution_attestation/1"

ATTESTED = "ATTESTED"
UNATTESTED = "UNATTESTED"
RESUME_BINDING_MATCH = "RESUME_BINDING_MATCH"
RESUME_BINDING_MISMATCH = "RESUME_BINDING_MISMATCH"


class Binding:
    """One actor, in one runtime, in one session, on one worktree, at one HEAD."""

    __slots__ = tuple(DIMENSIONS)

    def __init__(self, **fields: str) -> None:
        for name in DIMENSIONS:
            value = fields.get(name)
            setattr(self, name, UNDERIVABLE if value in (None, "") else str(value))
        unknown = set(fields) - set(DIMENSIONS)
        if unknown:
            raise ValueError(f"not a binding dimension: {sorted(unknown)}")

    def as_dict(self) -> Dict[str, str]:
        return {name: getattr(self, name) for name in DIMENSIONS}

    @classmethod
    def from_dict(cls, raw: object) -> "Binding":
        """🔴 A malformed or truncated record does not become a permissive one.

        A missing dimension is UNDERIVABLE, and UNDERIVABLE fails revalidation. So the
        failure mode of a corrupt store is a refused resume, not an inherited one.
        """
        if not isinstance(raw, dict):
            raise ValueError("an attestation record must be an object")
        return cls(**{k: v for k, v in raw.items() if k in DIMENSIONS
                      and isinstance(v, str)})

    @property
    def underivable(self) -> List[str]:
        return [name for name in DIMENSIONS if getattr(self, name) == UNDERIVABLE]

    @property
    def complete(self) -> bool:
        return not self.underivable

    def fingerprint(self) -> str:
        """SHA-256 over the nine dimensions, name and value, in DIMENSIONS order.

        The names are hashed with the values so that two bindings differing only in
        which field held a value cannot collide.
        """
        digest = hashlib.sha256()
        digest.update(SCHEMA.encode("utf-8"))
        for name in DIMENSIONS:
            digest.update(b"\x00")
            digest.update(name.encode("utf-8"))
            digest.update(b"\x1f")
            digest.update(getattr(self, name).encode("utf-8"))
        return digest.hexdigest()

    def differences(self, other: "Binding") -> List[Tuple[str, str, str]]:
        return [(name, getattr(self, name), getattr(other, name))
                for name in DIMENSIONS if getattr(self, name) != getattr(other, name)]

    def __repr__(self) -> str:  # pragma: no cover - diagnostics only
        return f"Binding({self.actor}@{self.runtime}:{self.branch}#{self.head[:8]})"


# ── derivation ──────────────────────────────────────────────────────────────────────

def _git(cwd: str, *args: str) -> str:
    try:
        result = subprocess.run(["git", "-C", cwd, *args],
                                capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return UNDERIVABLE
    if result.returncode != 0:
        return UNDERIVABLE
    return result.stdout.strip() or UNDERIVABLE


def derive_runtime(payload: Optional[dict] = None) -> Tuple[str, str, str]:
    """`(runtime, runtime_version, session)` from a hook payload and the environment.

    🔴 A runtime this module cannot name is `UNDERIVABLE`, not "probably claude-code".
    A default here would make the busiest dimension in the table the one nobody
    checked, and it is the dimension the 2026-08-28 restart moved.
    """
    payload = payload if isinstance(payload, dict) else {}
    session = payload.get("session_id")
    session = session if isinstance(session, str) and session else UNDERIVABLE

    runtime = UNDERIVABLE
    if "CLAUDE_PROJECT_DIR" in os.environ or "CLAUDECODE" in os.environ:
        runtime = "claude-code"
    if "CODEX_HOME" in os.environ or os.environ.get("CODEX_SANDBOX"):
        runtime = "codex"
    # A payload naming its own tool is stronger evidence than an environment variable
    # the other runtime might also happen to set.
    tool = payload.get("tool_name")
    if tool == "Bash":
        runtime = "claude-code"
    elif tool in ("exec", "exec_command", "shell_command", "unified_exec", "apply_patch"):
        runtime = "codex"

    version = os.environ.get("CLAUDE_CODE_VERSION") or os.environ.get("CODEX_VERSION")
    if not version and runtime != UNDERIVABLE:
        binary = {"claude-code": "claude", "codex": "codex"}.get(runtime)
        if binary:
            try:
                result = subprocess.run([binary, "--version"], capture_output=True,
                                        text=True, timeout=10)
                version = result.stdout.strip() if result.returncode == 0 else ""
            except (OSError, subprocess.SubprocessError):
                version = ""
    return runtime, (version or UNDERIVABLE), session


def derive(actor: Optional[str] = None, task: Optional[str] = None,
           authority: Optional[str] = None, cwd: Optional[str] = None,
           payload: Optional[dict] = None) -> Binding:
    """Derive the six derivable dimensions; carry the three declared ones verbatim."""
    cwd = cwd or os.getcwd()
    runtime, version, session = derive_runtime(payload)
    branch = _git(cwd, "branch", "--show-current")
    return Binding(
        actor=actor,
        task=task_fingerprint(task) if task else None,
        authority=authority,
        runtime=runtime,
        runtime_version=version,
        session=session,
        worktree=_git(cwd, "rev-parse", "--show-toplevel"),
        # A detached HEAD is a real state, not a missing branch. Saying UNDERIVABLE
        # would make an ordinary bisect look like an unreadable environment.
        branch=branch if branch != UNDERIVABLE else "DETACHED",
        head=_git(cwd, "rev-parse", "HEAD"),
    )


def task_fingerprint(task: object) -> str:
    """A stable digest of the task, so the task text itself never enters a receipt.

    A task description can carry anything the operator typed. The binding needs to
    detect that the task CHANGED, which a digest does, and does not need to record what
    it was, which a digest deliberately cannot.
    """
    if not isinstance(task, str) or not task.strip():
        return UNDERIVABLE
    return "task:" + hashlib.sha256(task.strip().encode("utf-8")).hexdigest()[:32]


# ── attestation and revalidation ────────────────────────────────────────────────────

class Attestation:
    __slots__ = ("verdict", "binding", "reason")

    def __init__(self, verdict: str, binding: Binding, reason: str = "") -> None:
        self.verdict = verdict
        self.binding = binding
        self.reason = reason

    @property
    def ok(self) -> bool:
        return self.verdict in (ATTESTED, RESUME_BINDING_MATCH)

    @property
    def effective_authority(self) -> str:
        """🔴 The authority this attestation actually confers.

        A failed attestation does not confer the authority it declared; it confers the
        floor. Returning the declared value with an `ok=False` beside it is how a caller
        that forgets to check `ok` gets the authority anyway — so the value itself is
        revoked, not merely flagged.
        """
        if not self.ok:
            return em.UNATTESTED
        return self.binding.authority


def attest(binding: Binding) -> Attestation:
    """A first attestation: every dimension must be derivable, and the authority real."""
    if not binding.complete:
        return Attestation(UNATTESTED, binding,
                           "these dimensions are UNDERIVABLE: "
                           + ", ".join(binding.underivable))
    if binding.authority not in em.AUTHORITIES:
        return Attestation(UNATTESTED, binding,
                           f"{binding.authority!r} is not an authority class")
    return Attestation(ATTESTED, binding, "")


def revalidate(previous: Binding, current: Binding) -> Attestation:
    """A resume, a restart, a compaction: does the binding still hold?

    Fails on ANY difference across the nine, and on any dimension that has become
    underivable. There is no subset that may drift: a session identifier that changed
    IS a new session, and a `HEAD` that moved means someone committed under this actor's
    feet — which is the condition `ONE_WRITER_PER_WORKING_DIRECTORY` exists to prevent
    and cannot detect by itself.
    """
    if not current.complete:
        return Attestation(RESUME_BINDING_MISMATCH, current,
                           "on resume these became UNDERIVABLE: "
                           + ", ".join(current.underivable))
    changed = previous.differences(current)
    if changed:
        lines = [f"  {name:<16} was {was!r}  now {now!r}" for name, was, now in changed]
        return Attestation(
            RESUME_BINDING_MISMATCH, current,
            "the binding this authority was granted to is not the binding in front of "
            "me:\n" + "\n".join(lines)
            + "\n\nWrite authority is revoked until a fresh attestation succeeds.")
    return Attestation(RESUME_BINDING_MATCH, current, "")


# ── the store ───────────────────────────────────────────────────────────────────────

def store_home() -> Path:
    """Runtime-local, OUTSIDE the repository. See the module docstring on what that
    costs: this is not a repository control and cannot be verified by a reader."""
    return Path(os.environ.get("LEGEND_ATTESTATION_HOME",
                               Path.home() / ".legend" / "attestation"))


def _slug(worktree: str) -> str:
    return hashlib.sha256(worktree.encode("utf-8")).hexdigest()[:24]


def record(binding: Binding, home: Optional[Path] = None) -> Path:
    home = Path(home) if home else store_home()
    home.mkdir(parents=True, exist_ok=True)
    path = home / f"{_slug(binding.worktree)}-{binding.actor}.json"
    path.write_text(json.dumps(
        {"schema": SCHEMA, "fingerprint": binding.fingerprint(),
         "binding": binding.as_dict()}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")
    return path


def load(worktree: str, actor: str, home: Optional[Path] = None) -> Optional[Binding]:
    home = Path(home) if home else store_home()
    path = home / f"{_slug(worktree)}-{actor}.json"
    if not path.exists():
        return None
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        # 🔴 An unreadable store is not an absent one. Absent means "no prior binding,
        # attest fresh"; unreadable means "a prior binding exists and I cannot compare
        # to it", and returning None there would silently upgrade the second to the
        # first. An all-UNDERIVABLE binding fails revalidation, which is the answer.
        return Binding()
    if not isinstance(raw, dict) or raw.get("schema") != SCHEMA:
        return Binding()
    binding = Binding.from_dict(raw.get("binding"))
    if raw.get("fingerprint") != binding.fingerprint():
        # The record was edited after it was written. It attests to nothing.
        return Binding()
    return binding


def check_resume(actor: str, task: Optional[str] = None, authority: Optional[str] = None,
                 cwd: Optional[str] = None, payload: Optional[dict] = None,
                 home: Optional[Path] = None) -> Attestation:
    """The whole flow: derive now, compare with what was stored, record on success."""
    current = derive(actor=actor, task=task, authority=authority, cwd=cwd, payload=payload)
    previous = load(current.worktree, actor or "", home)
    if previous is None:
        result = attest(current)
    else:
        result = revalidate(previous, current)
    if result.ok:
        record(current, home)
    return result


# ── CLI ─────────────────────────────────────────────────────────────────────────────

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--actor")
    parser.add_argument("--task")
    parser.add_argument("--authority", default="READ_ONLY")
    parser.add_argument("--cwd")
    parser.add_argument("--home")
    parser.add_argument("--derive-only", action="store_true",
                        help="print the derived binding and exit, attesting nothing")
    args = parser.parse_args(argv)

    if args.derive_only or not args.actor:
        binding = derive(actor=args.actor, task=args.task, authority=args.authority,
                         cwd=args.cwd)
        print(json.dumps({"binding": binding.as_dict(),
                          "fingerprint": binding.fingerprint(),
                          "underivable": binding.underivable}, indent=2, sort_keys=True))
        return 0 if binding.complete else 1

    result = check_resume(args.actor, args.task, args.authority, args.cwd,
                          home=Path(args.home) if args.home else None)
    print(json.dumps({
        "verdict": result.verdict,
        "effective_authority": result.effective_authority,
        "fingerprint": result.binding.fingerprint(),
        "reason": result.reason,
        "binding": result.binding.as_dict(),
    }, indent=2, sort_keys=True))
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
