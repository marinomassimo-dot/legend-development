#!/usr/bin/env python3
"""Where a path sits in a MULTI-WORKTREE repository, which is the unit this guard defends.

Revision 8 knew two places: inside `--show-toplevel`, and everywhere else. In a
repository that runs eleven worktrees off one `.git`, "everywhere else" contains every
other actor's working tree, the shared checkout carrying canonical `main`, and the
shared git directory itself — `config`, `hooks/`, `refs/`, `worktrees/*/HEAD`. All of
them were `OUTSIDE_REPO`, and `SHELL_DEFAULT` grants content writes there, so from an
actor worktree the following were all ALLOWED and all measured on 2026-08-29:

```text
echo x > <WORKTREE_B>/framework/pwned.md          rewrite a peer's source
rm -rf <WORKTREE_B>/framework                     delete a peer's work
echo x > <REPO>/CLAUDE.md                         rewrite the shared checkout
echo x > <GIT_COMMON_DIR>/hooks/pre-commit        install a hook in every worktree
echo x > <GIT_COMMON_DIR>/refs/heads/main         move canonical main
echo x > <GIT_COMMON_DIR>/config                  rewrite everyone's git config
```

`--show-toplevel` is the wrong unit because it answers *which working tree am I in*, and
the thing being protected is *the repository*, which is the set of working trees sharing
one object store. So repository identity here is the **git common directory**, and the
worktree is a subdivision of it.

## The nesting trap

This repository puts its worktrees INSIDE the shared checkout:

```text
<REPO>/                                   the shared checkout, branch main
<REPO>/.git/                              the git common dir
<REPO>/.claude/worktrees/<WORKTREE_A>/    an actor worktree
<REPO>/.claude/worktrees/<WORKTREE_B>/    a peer
```

So `<REPO>/.claude/worktrees/<WORKTREE_B>/x` is under the shared checkout AND under a
peer worktree AND under nothing else, and `<REPO>/.git/config` is under the shared
checkout too. A first-match scan over an unordered list of roots answers whichever it
happened to try first. **Longest prefix wins**, which is the only rule that gives the
same answer regardless of iteration order, and it lands each of those three on the
subdivision that actually owns it.

## Symlinks, and why the answer is the stricter of two

A path is classified twice — as written (lexically normalised) and as resolved
(`realpath`, which follows every symlink in its existing prefix) — and the STRICTER of
the two answers is returned. A symlink planted inside the assigned worktree pointing at
a peer is caught by the resolved reading; a `/var/folders` path whose resolved form
`/private/var/folders` might miss a scratch prefix is caught by the lexical one. Taking
the stricter of both needs no faith in either being complete.

## 🔴 Which worktree is the ASSIGNED one — revision 10

`of(cwd)` answers *the topology around this directory*, and revision 9's policy called it
with the EFFECTIVE WORKING DIRECTORY, which comes from `tool_input.workdir`. The model
writes that field, so the model chose which subdivision was `ASSIGNED_WORKTREE` — and a
peer named as the workdir stopped being a peer. Measured, and reported in
`session_binding.py`'s docstring with the six spellings that reached it.

`of_assigned(assigned)` is the repair: it derives the same repository, from the same git,
but pins `ASSIGNED_WORKTREE` to a directory the model does not author. `of()` survives for
the READ-ONLY instruments — the guard-revision census, the parity probes, the corpus's own
scene builder — which ask *what is around this directory* and grant nothing.
"""
from __future__ import annotations

import os
import posixpath
import subprocess
from typing import Dict, List, Optional, Tuple

# ── the scope vocabulary this module assigns ───────────────────────────────────────

#: The worktree this actor was given. Governed by the ordinary authority ladder.
ASSIGNED_WORKTREE = "ASSIGNED_WORKTREE"
#: Another actor's working tree, sharing this object store. Never an ordinary write.
PEER_WORKTREE = "PEER_WORKTREE"
#: The checkout the common dir lives in — canonical `main` here. Never an ordinary write.
SHARED_CHECKOUT = "SHARED_CHECKOUT"
#: `.git` itself: config, hooks, refs, worktree administration. Never a shell write.
GIT_COMMON_DIR = "GIT_COMMON_DIR"
#: `/tmp`, `/var/folders`, a `scratchpad` segment. Working space, and not this guard's
#: business — provided it is not also a working tree, which `of()` checks first.
EXTERNAL_SCRATCH = "EXTERNAL_SCRATCH"
#: Outside this repository and not scratch. Someone else's business, not a peer's.
EXTERNAL_OTHER = "EXTERNAL_OTHER"
#: The answer needs a shell, or the topology could not be derived.
UNDERIVABLE = "UNDERIVABLE"

SCOPES: Tuple[str, ...] = (
    ASSIGNED_WORKTREE, PEER_WORKTREE, SHARED_CHECKOUT, GIT_COMMON_DIR,
    EXTERNAL_SCRATCH, EXTERNAL_OTHER, UNDERIVABLE,
)

#: 🔴 Strictness order, used to combine the lexical and resolved readings of one path.
#: Higher is stricter. It is NOT alphabetical and it is NOT the declaration order: it is
#: how much a wrong ALLOW would cost, and `test_repo_topology.py` asserts that every
#: scope appears exactly once so a scope added later cannot default to zero.
STRICTNESS: Dict[str, int] = {
    EXTERNAL_SCRATCH: 0,
    EXTERNAL_OTHER: 1,
    ASSIGNED_WORKTREE: 2,
    PEER_WORKTREE: 3,
    SHARED_CHECKOUT: 4,
    GIT_COMMON_DIR: 5,
    UNDERIVABLE: 6,
}

#: Scratch prefixes in BOTH their lexical and their resolved spelling. On macOS `/tmp`
#: is a symlink to `/private/tmp` and `/var` to `/private/var`, so a resolved path
#: carries the `/private` prefix and a lexical one does not. Listing one form only made
#: the resolved reading of an ordinary scratch write fall through to EXTERNAL_OTHER —
#: harmless here, because both are writable at the same rung, and listed anyway because
#: relying on two wrongs to cancel is not a property anyone can maintain.
SCRATCH_PREFIXES: Tuple[str, ...] = (
    "/tmp/", "/private/tmp/", "/var/tmp/", "/private/var/tmp/",
    "/var/folders/", "/private/var/folders/", "/dev/",
)
SCRATCH_EXACT = frozenset({"/tmp", "/private/tmp", "/var/tmp", "/private/var/tmp"})
SCRATCH_SEGMENT = "scratchpad"


class Topology:
    """One repository, as the set of working trees that share its object store.

    🔴 `ok=False` is not an empty topology. A derivation that failed cannot say a path
    is safe, so `classify` on a failed topology returns `UNDERIVABLE` for everything
    that is not plainly scratch — which denies. The failure direction of not knowing
    where you are is refusal.
    """

    __slots__ = ("repository_id", "assigned_worktree", "shared_checkout",
                 "git_common_dir", "peer_worktrees", "ok", "detail")

    def __init__(self, repository_id: str = "", assigned_worktree: str = "",
                 shared_checkout: str = "", git_common_dir: str = "",
                 peer_worktrees: Optional[List[str]] = None,
                 ok: bool = True, detail: str = "") -> None:
        self.repository_id = repository_id
        self.assigned_worktree = assigned_worktree
        self.shared_checkout = shared_checkout
        self.git_common_dir = git_common_dir
        self.peer_worktrees = list(peer_worktrees or [])
        self.ok = ok
        self.detail = detail

    # ── the ordered root table ─────────────────────────────────────────────────────

    def roots(self) -> List[Tuple[str, str]]:
        """`(root, scope)` for every subdivision, longest first.

        Sorting here rather than at each `classify` call is what makes longest-prefix
        cheap, and sorting by length rather than by declaration order is what makes the
        answer independent of which subdivision happened to be listed first.
        """
        table: List[Tuple[str, str]] = []
        if self.git_common_dir:
            table.append((self.git_common_dir, GIT_COMMON_DIR))
        if self.assigned_worktree:
            table.append((self.assigned_worktree, ASSIGNED_WORKTREE))
        for peer in self.peer_worktrees:
            table.append((peer, PEER_WORKTREE))
        if self.shared_checkout:
            table.append((self.shared_checkout, SHARED_CHECKOUT))
        # Longest root first. A tie can only be two names for one directory, and the
        # order between those does not change the answer.
        return sorted(table, key=lambda pair: len(pair[0]), reverse=True)

    def as_dict(self) -> Dict[str, object]:
        return {
            "repository_id": self.repository_id,
            "assigned_worktree": self.assigned_worktree,
            "shared_checkout": self.shared_checkout,
            "git_common_dir": self.git_common_dir,
            "peer_worktrees": list(self.peer_worktrees),
            "ok": self.ok,
            "detail": self.detail,
        }

    # ── classification ─────────────────────────────────────────────────────────────

    def classify(self, path: str) -> str:
        """Which subdivision does this ABSOLUTE path belong to?

        The caller resolves relative paths against the effective working directory
        before calling; a relative path arriving here is one nobody could anchor, and
        is `UNDERIVABLE` rather than silently joined to this process's cwd.
        """
        if not path or not posixpath.isabs(path):
            return UNDERIVABLE
        lexical = self._one(posixpath.normpath(path))
        resolved = self._one(_realpath(path))
        return lexical if STRICTNESS[lexical] >= STRICTNESS[resolved] else resolved

    def _one(self, path: str) -> str:
        """Classify one already-absolute spelling of a path. Longest prefix wins."""
        for root, scope in self.roots():
            if _under(root, path):
                return scope
        if not self.ok:
            # 🔴 Scratch is still derivable without a topology — it is a property of the
            # path, not of the repository — and refusing it would deny `echo x > /tmp/f`
            # every time `git` was slow. Everything else is refused.
            return EXTERNAL_SCRATCH if _is_scratch(path) else UNDERIVABLE
        if _is_scratch(path):
            return EXTERNAL_SCRATCH
        return EXTERNAL_OTHER


def _under(directory: str, path: str) -> bool:
    directory = directory.rstrip("/")
    return bool(directory) and (path == directory or path.startswith(directory + "/"))


def _is_scratch(path: str) -> bool:
    if path in SCRATCH_EXACT or path.startswith(SCRATCH_PREFIXES):
        return True
    return SCRATCH_SEGMENT in path.split("/")


def realpath(path: str) -> str:
    """Public alias. `guard_policy` needs the same resolution for its workdir overlay,
    and a second implementation of "resolve what exists, normalise the rest" is the
    shape that drifts until one of the two stops following a symlink."""
    return _realpath(path)


def _realpath(path: str) -> str:
    """`realpath`, resolving what exists and normalising the rest.

    A write target usually does NOT exist yet — that is what makes it a write — so this
    has to answer for `<peer>/newfile` as well as for `<peer>/existing`. POSIX
    `realpath` resolves the existing prefix and appends the remainder, which is the
    behaviour wanted: a symlinked ancestor is followed, a not-yet-created leaf is not
    an error.
    """
    try:
        return posixpath.normpath(os.path.realpath(path))
    except (OSError, ValueError):  # pragma: no cover - realpath is total on POSIX
        return posixpath.normpath(path)


# ── derivation ─────────────────────────────────────────────────────────────────────

def _git(cwd: str, *args: str) -> Optional[str]:
    try:
        result = subprocess.run(["git", "-C", cwd, *args],
                                capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def _worktrees(cwd: str) -> Optional[List[str]]:
    """Every working tree sharing this object store, in `git worktree list` order.

    The FIRST entry is the main working tree — `git worktree list` documents that
    ordering, and it is how the shared checkout is told apart from the linked worktrees
    without pattern-matching a path.
    """
    listing = _git(cwd, "worktree", "list", "--porcelain")
    if listing is None:
        return None
    found: List[str] = []
    for line in listing.splitlines():
        if line.startswith("worktree "):
            found.append(_realpath(line[len("worktree "):].strip()))
    return found


def of(cwd: Optional[str]) -> Topology:
    """Derive the topology containing `cwd`, taking its toplevel as the assignment.

    🔴 **Not the enforcement path.** The assignment it returns is whatever working tree
    `cwd` happens to sit in, and under the guard `cwd` is the model-selected effective
    workdir. Every caller that DECIDES something uses `of_assigned`; this one is for the
    read-only instruments, which grant nothing and want the topology around a directory.
    """
    if not cwd or not isinstance(cwd, str):
        return Topology(ok=False, detail="no working directory was supplied")

    toplevel = _git(cwd, "rev-parse", "--show-toplevel")
    if not toplevel:
        return Topology(ok=False, detail=f"`{cwd}` is not inside a git working tree")
    return _derive(cwd, _realpath(toplevel))


def of_assigned(assigned: Optional[str]) -> Topology:
    """Derive the repository around the SESSION-BOUND assigned worktree.

    🔴 The one difference from `of` is the whole revision-10 repair: `assigned` comes
    from `session_binding`, not from the payload, so no `workdir`, no `cwd` and no `-C`
    operand can make a peer worktree or the shared checkout become this actor's own.
    The effective workdir keeps its job — it resolves relative operands — and loses the
    one it should never have had.

    A caller that cannot supply an assignment must NOT fall back to `of(cwd)`; it has to
    treat the assignment as `UNDERIVABLE`, which denies. `guard_policy` does exactly that.
    """
    if not assigned or not isinstance(assigned, str):
        return Topology(ok=False, detail="no assigned worktree was supplied")
    root = _realpath(assigned)
    if not os.path.isdir(root):
        return Topology(ok=False, detail=f"the assigned worktree `{assigned}` is not a directory")
    toplevel = _git(root, "rev-parse", "--show-toplevel")
    if not toplevel:
        return Topology(ok=False,
                        detail=f"the assigned worktree `{assigned}` is not a git working tree")
    return _derive(root, _realpath(toplevel))


def _derive(cwd: str, assigned: str) -> Topology:
    """The shared body: one repository, seen from `cwd`, with `assigned` pinned."""
    common = _git(cwd, "rev-parse", "--git-common-dir")
    if not common:
        return Topology(ok=False, detail="the git common directory is not derivable")
    # `--git-common-dir` answers relatively (`.git`) when cwd is the toplevel itself.
    common = _realpath(common if posixpath.isabs(common) else posixpath.join(cwd, common))

    trees = _worktrees(cwd)
    if trees is None:
        return Topology(ok=False, detail="`git worktree list` did not answer")

    shared = trees[0] if trees else ""
    peers = [t for t in trees if t != assigned and t != shared]

    return Topology(
        # 🔴 Repository identity is the COMMON DIR, not the toplevel. Two worktrees of
        # one repository have two toplevels and one common dir, so a receipt keyed on
        # the toplevel says two actors worked in two repositories, which is the fact
        # that would have to be true for a cross-worktree write to be nobody's business.
        repository_id=common,
        assigned_worktree=assigned,
        shared_checkout=shared,
        git_common_dir=common,
        peer_worktrees=peers,
    )


# ── caching ────────────────────────────────────────────────────────────────────────
#
# 🔴 A guard call classifies every operand of every command, and each classification
# would otherwise cost three `git` subprocesses. The cache is keyed on the working
# directory STRING, and it is process-local: a hook process handles one payload and
# exits, so a worktree added mid-life is not a case that can arise there. `reset()`
# exists for the suites, which build and tear down fixtures inside one process.

_CACHE: Dict[str, Topology] = {}
_ASSIGNED_CACHE: Dict[str, Topology] = {}


def cached(cwd: Optional[str]) -> Topology:
    key = cwd or ""
    if key not in _CACHE:
        _CACHE[key] = of(cwd)
    return _CACHE[key]


def cached_for(assigned: Optional[str]) -> Topology:
    """`of_assigned`, memoised. Its own cache: the two answer different questions and a
    shared one keyed on a path would return whichever question was asked first."""
    key = assigned or ""
    if key not in _ASSIGNED_CACHE:
        _ASSIGNED_CACHE[key] = of_assigned(assigned)
    return _ASSIGNED_CACHE[key]


def reset() -> None:
    """Forget every derived topology. Called by fixtures, never by the hook path."""
    _CACHE.clear()
    _ASSIGNED_CACHE.clear()


# ── reporting ──────────────────────────────────────────────────────────────────────

def describe(cwd: str) -> str:
    topology = of(cwd)
    lines = [
        f"REPOSITORY_ID      {topology.repository_id or '<underivable>'}",
        f"ASSIGNED_WORKTREE  {topology.assigned_worktree or '<underivable>'}",
        f"SHARED_CHECKOUT    {topology.shared_checkout or '<underivable>'}",
        f"GIT_COMMON_DIR     {topology.git_common_dir or '<underivable>'}",
        f"PEER_WORKTREES     {len(topology.peer_worktrees)}",
    ]
    lines.extend(f"                   {peer}" for peer in topology.peer_worktrees)
    lines.append(f"OK                 {topology.ok}"
                 + (f"  ({topology.detail})" if topology.detail else ""))
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:  # pragma: no cover - CLI
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--cwd", default=".")
    parser.add_argument("--classify", action="append", default=[],
                        help="an absolute path to place in the topology")
    args = parser.parse_args(argv)
    print(describe(args.cwd))
    if args.classify:
        topology = of(args.cwd)
        print()
        for path in args.classify:
            print(f"{topology.classify(path):<18} {path}")
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI
    raise SystemExit(main())
