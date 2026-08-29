#!/usr/bin/env python3
"""OBSERVED EFFECT, and whether it is the effect that was authorised.

A `PreToolUse` hook predicts. It cannot verify, because by construction it has already
returned by the time anything runs. Every revision of this bridge up to and including 7
therefore ended at the prediction, and the sentence "the guard allowed it" was allowed
to stand in for "the command did what the guard thought it would".

Those are different claims, and this module is the second one:

```
snapshot BEFORE  →  execute  →  snapshot AFTER  →  delta  →  compare to AUTHORISED
                                                    ↓
                          extra effect OR missing effect  →  WRITE RESULT INVALID
```

## The three things a naive delta gets wrong, and what is done instead

**1. A rename is observed as a deletion and a creation.** git reports `R` only for a
staged rename; an unstaged `mv` is `D old` + `?? new`. So an authorised `RENAME` would
never match, and every legitimate `mv` would be reported as two unexplained effects.
`RENAME` is therefore expanded into `DELETE(source) + WRITE(destination)` on BOTH sides
before comparison, rather than being matched as itself.

**2. An effect on a DIRECTORY covers the files under it.** `cp -t framework/x /tmp/a`
authorises a write to `framework/x`; what appears is `framework/x/a`. A set comparison
over exact paths reports one missing and one extra, and the two are the same event. So
authorisation of a directory target COVERS observations beneath it — and this is a
widening, stated here rather than hidden in a helper: an authorised write to a directory
authorises everything that lands in it.

**3. `ARCHIVE_EXTRACT` has no signature of its own.** What an extraction produces is
writes. It is treated as a directory-covering `WRITE`, which is exactly the reason the
policy refuses an extraction whose destination is not named: with no named directory
there is nothing for the coverage to be relative to, and every member would be extra.

## 🔴 What this instrument CANNOT see, declared rather than discovered

```
NETWORK_WRITE     bytes that left the machine leave no local delta. An authorised
                  NETWORK_WRITE is exempt from the MISSING check and can never be
                  observed, so this module cannot corroborate or refute a push.
ignored files     `--untracked-files=all` does not report paths matched by .gitignore.
                  Pass `--include-ignored` to widen it; the default is narrow because
                  this repository's ignore set contains whole worktrees and virtualenvs.
outside the repo  a write to /tmp or to another checkout is outside every snapshot here.
content rewrite   a file rewritten with byte-identical content produces no delta, and
                  is correctly reported as no effect.
timestamps        `cp -p` and `git archive` both falsify mtime, so no mtime is read.
```

None of these is a bug to be fixed later. They are the boundary of what a git-shaped
instrument can say, and a verdict that did not name them would be claiming more than it
measured.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import effect_model as em  # noqa: E402

VALID = "WRITE_RESULT_VALID"
INVALID = "WRITE_RESULT_INVALID"
#: 🔴 A third value, because a command that was REFUSED and a command that RAN and did
#: the wrong thing are not the same outcome and must not share a word. Collapsing them
#: makes "INVALID" mean both "the guard worked" and "the guard was bypassed", which is
#: the one distinction a post-effect check exists to draw.
REFUSED = "WRITE_REFUSED"


class Snapshot:
    """The repository state a delta is taken against.

    Content comes from git plumbing and not from the filesystem: a stat-based CONTENT
    snapshot reads mtimes, and this repository has already learned twice that mtimes do
    not attribute work.

    🔴 `modes` is the one exception, and the exception is principled. A file's permission
    bits are not content, git tracks only one of them, and the act being observed —
    `chmod` — leaves no other trace. Stat is not a weaker instrument here, it is the only
    one; and unlike an mtime, a mode is a value the command explicitly sets, so comparing
    two of them attributes exactly what it appears to.
    """

    __slots__ = ("head", "branch", "index", "worktree", "refs", "modes", "ok", "detail")

    def __init__(self, head: str, branch: str, index: Dict[str, str],
                 worktree: Dict[str, str], refs: Dict[str, str],
                 modes: Optional[Dict[str, int]] = None,
                 ok: bool = True, detail: str = "") -> None:
        self.head = head
        self.branch = branch
        self.index = index
        self.worktree = worktree
        self.refs = refs
        self.modes = modes if modes is not None else {}
        self.ok = ok
        self.detail = detail

    def as_dict(self) -> dict:
        return {"head": self.head, "branch": self.branch, "refs": self.refs,
                "index_entries": len(self.index), "worktree_entries": len(self.worktree),
                "mode_entries": len(self.modes)}


def _git(root: str, *args: str) -> Tuple[int, str]:
    try:
        result = subprocess.run(["git", "-C", root, *args],
                                capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as exc:
        return 1, str(exc)
    return result.returncode, result.stdout


def snapshot(root: str, include_ignored: bool = False) -> Snapshot:
    """🔴 A snapshot that cannot be taken is not an empty snapshot.

    `ok=False` propagates to the verdict as INVALID. An unreadable before-state makes
    every after-state unexplainable, and returning empty dicts would instead make every
    observed effect look EXTRA — a different wrong answer, and a noisier one.
    """
    code, head = _git(root, "rev-parse", "HEAD")
    if code != 0:
        return Snapshot("", "", {}, {}, {}, {}, ok=False,
                        detail="HEAD is not readable in this working tree")
    _, branch = _git(root, "branch", "--show-current")

    index: Dict[str, str] = {}
    code, listing = _git(root, "ls-files", "-s", "-z")
    if code != 0:
        return Snapshot("", "", {}, {}, {}, {}, ok=False,
                        detail="the index is not readable")
    for entry in listing.split("\0"):
        if not entry:
            continue
        meta, _, path = entry.partition("\t")
        parts = meta.split()
        if len(parts) >= 3 and path:
            # mode + object + stage. The MODE is in here deliberately: it is the only
            # observable signature a PERMISSION_CHANGE on a tracked file leaves.
            index[path] = f"{parts[0]}:{parts[1]}:{parts[2]}"

    # 🔴 The FILESYSTEM mode of every tracked file, which is the only place a `chmod`
    # leaves a trace this instrument can see.
    #
    # Revision 8 read the mode out of `ls-files -s`, i.e. out of the INDEX — and a bare
    # `chmod +x tracked.sh` does not touch the index. Git reports it as ` M` in the
    # worktree column, `delta` turned that into a WRITE, and an AUTHORISED
    # PERMISSION_CHANGE came back as `EXTRA[WRITE] + MISSING[PERMISSION_CHANGE]` and
    # therefore WRITE_RESULT_INVALID. The index branch was not wrong; it was answering
    # about `git update-index --chmod`, which is a different act.
    #
    # 659 tracked files in this repository cost 8 ms to stat, measured on 2026-08-29, so
    # this is a cheap observation and not a sampled one. Files that vanish between the
    # listing and the stat are simply absent from the map, where the delta reads them as
    # a deletion — which is what they are.
    modes: Dict[str, int] = {}
    for path in index:
        try:
            modes[path] = os.lstat(os.path.join(root, path)).st_mode & 0o7777
        except OSError:
            continue

    worktree: Dict[str, str] = {}
    args = ["status", "--porcelain=v1", "-z", "--untracked-files=all", "--no-renames"]
    if include_ignored:
        args.append("--ignored=matching")
    code, status = _git(root, *args)
    if code != 0:
        return Snapshot("", "", {}, {}, {}, {}, ok=False,
                        detail="status is not readable")
    for entry in status.split("\0"):
        if len(entry) < 4:
            continue
        # 🔴 The WORKTREE column only (`Y`), not the pair.
        #
        # Porcelain `XY` is (index-vs-HEAD, worktree-vs-index). Storing the pair made
        # `git add other.txt` — which moves ` M` to `M `, changing X and not the file —
        # look like a WRITE to a file nothing had written, and the authorised STAGE was
        # then reported alongside an EXTRA effect and the whole result INVALID. The X
        # column is already carried, precisely, by the `ls-files -s` snapshot above;
        # reading it here too double-counts every staging.
        worktree[entry[3:]] = entry[1]

    refs: Dict[str, str] = {}
    code, listing = _git(root, "for-each-ref", "--format=%(refname) %(objectname)")
    if code == 0:
        for line in listing.splitlines():
            name, _, sha = line.partition(" ")
            if name:
                refs[name] = sha

    return Snapshot(head.strip(), branch.strip(), index, worktree, refs, modes)


# ── the delta, in the shared vocabulary ─────────────────────────────────────────────

def _guard_policy_hash(root: str) -> str:
    """The sha256 of the policy that judged this command, or UNDERIVABLE.

    🔴 The policy running in THIS worktree, hashed from disk — not from the module
    already imported into this process. They are the same file in the ordinary case and
    they are not the same file when a receipt is built for a run in another tree, which
    is precisely when the field carries information.
    """
    candidate = Path(root) / "framework" / "scripts" / "guard_policy.py"
    try:
        return hashlib.sha256(candidate.read_bytes()).hexdigest()[:16]
    except OSError:
        return "UNDERIVABLE"


def _guard_generation(root: str) -> str:
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import guard_revision  # noqa: PLC0415
        return guard_revision.generation_of(Path(root))
    except Exception:  # pragma: no cover - the field degrades, the run does not fail
        return "UNDERIVABLE"


def content_moved(root: Optional[str], path: str) -> bool:
    """Did this file's CONTENT change against the index, ignoring its mode?

    🔴 Without a root the answer is TRUE, not false. `git status` said the file is
    modified; being unable to check whether it was only the mode is not evidence that
    the content is intact, and reporting no write on that basis would hide a content
    mutation behind an authorised `chmod`.
    """
    if not root:
        return True
    code, out = _git(root, "diff", "--numstat", "--", path)
    if code != 0:
        return True
    # 🔴 The PRESENCE of a row is not the answer. `git diff --numstat` emits
    # `0<TAB>0<TAB>s.sh` for a mode-only change — the file IS in the diff, and nothing
    # about its content moved. Reading `bool(output)` therefore reported a WRITE beside
    # every observed PERMISSION_CHANGE, which is the revision-8 verdict with one of its
    # two halves fixed and the mismatch intact. The counts are what carry the answer.
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        added, removed = parts[0], parts[1]
        if added == "-" or removed == "-":
            return True  # binary: git will not count, so it is not a no-op
        if (added.isdigit() and int(added)) or (removed.isdigit() and int(removed)):
            return True
    return False


def delta(before: Snapshot, after: Snapshot,
          root: Optional[str] = None) -> List[em.Effect]:
    """Everything that changed, as effects. The observed half of the comparison.

    `root` is optional only so the revision-8 call shape keeps working; without it a
    mode change is still observed, and a file whose mode moved is additionally reported
    as written, because `content_moved` fails towards reporting more.
    """
    if not before.ok or not after.ok:
        return [em.Effect(em.UNKNOWN_EFFECT, None, em.UNDERIVABLE, "snapshot",
                          (before.detail or after.detail) or "a snapshot failed")]

    observed: List[em.Effect] = []

    # ── permission bits ──
    #
    # 🔴 Taken FIRST, and the set of paths whose mode moved is carried into the working
    # tree pass below, because the two observations describe the same `git status` line.
    # A `chmod` makes a tracked file report ` M`; without this, that line becomes a WRITE
    # and the mode change is never observed at all — which is exactly the pair of
    # findings revision 8 produced, `EXTRA[WRITE]` beside `MISSING[PERMISSION_CHANGE]`,
    # for an act it had authorised.
    mode_moved: Dict[str, Tuple[int, int]] = {}
    for path in sorted(set(before.modes) | set(after.modes)):
        was_mode, now_mode = before.modes.get(path), after.modes.get(path)
        if was_mode is None or now_mode is None or was_mode == now_mode:
            # A file that appeared or vanished is a WRITE or a DELETE, and the working
            # tree pass reports it as one. Calling it a permission change as well would
            # invent an effect out of a file's absence.
            continue
        mode_moved[path] = (was_mode, now_mode)
        observed.append(em.Effect(em.PERMISSION_CHANGE, path, em.INSIDE_REPO, "mode",
                                  f"mode {was_mode:04o} -> {now_mode:04o}"))

    # ── working tree ──
    for path in sorted(set(before.worktree) | set(after.worktree)):
        # A path absent from `git status` is clean: identical to the index. That is a
        # state, not a missing observation, so it gets a value rather than None.
        was = before.worktree.get(path, " ")
        now = after.worktree.get(path, " ")
        if was == now:
            continue
        if path in mode_moved and now != "D":
            # The status line is EXPLAINED by the mode change already reported. Whether
            # the CONTENT also moved is a separate question, and `git diff` is the only
            # thing that can answer it — a mode-only change and a mode-plus-content
            # change produce the identical ` M`.
            if not content_moved(root, path):
                continue
        if now == "D":
            observed.append(em.Effect(em.DELETE, path, em.INSIDE_REPO, "worktree",
                                      "gone from the working tree"))
        elif now != " ":
            observed.append(em.Effect(em.WRITE, path, em.INSIDE_REPO, "worktree",
                                      f"worktree status {now!r}"))
        elif before.index.get(path) == after.index.get(path):
            # 🔴 `Y` returned to clean and the INDEX did not move. The two ways that can
            # happen are staging and reverting, and only one of them touches the file —
            # so the index is what tells them apart. Without this branch a
            # `git checkout -- <path>`, which rewrites the file from the index, would
            # be observed as no effect at all: the one destructive act whose whole
            # signature is a file quietly returning to a previous state.
            observed.append(em.Effect(em.WRITE, path, em.INSIDE_REPO, "worktree",
                                      "restored to the index content, unread"))

    # ── index ──
    for path in sorted(set(before.index) | set(after.index)):
        was, now = before.index.get(path), after.index.get(path)
        if was == now:
            continue
        if was is not None and now is not None:
            mode_was, mode_now = was.split(":")[0], now.split(":")[0]
            if mode_was != mode_now:
                observed.append(em.Effect(em.PERMISSION_CHANGE, path, em.INSIDE_REPO,
                                          "index", f"mode {mode_was} -> {mode_now}"))
                if was.split(":")[1] == now.split(":")[1]:
                    continue  # only the mode moved
        observed.append(em.Effect(em.STAGE, path, em.INSIDE_REPO, "index",
                                  "index entry added, changed or removed"))

    # ── HEAD ──
    #
    # 🔴 Whether this is a COMMIT or a REF_MUTATION depends on whether the new HEAD is
    # a CHILD of the old one, and answering that needs another git call — which needs
    # the repository root, which a delta over two snapshots does not have. Rather than
    # guess (a guess here would call every `git reset` a commit), the kind is left
    # provisional and `run()` settles it where the root is in hand. `resolve_head_kind`
    # is that step, and calling `delta` without it is a caller error the tests pin.
    if before.head != after.head:
        observed.append(em.Effect(em.COMMIT, "HEAD", em.INSIDE_REPO, "head",
                                  f"{before.head[:12]} -> {after.head[:12]} "
                                  "(PROVISIONAL: resolve_head_kind not yet applied)"))

    # ── refs ──
    for name in sorted(set(before.refs) | set(after.refs)):
        was, now = before.refs.get(name), after.refs.get(name)
        if was == now:
            continue
        if was is None:
            # A ref that did not exist now does: a creation, which loses nothing. It is
            # still reported, because "loses nothing" is a policy judgement and this
            # module only observes.
            observed.append(em.Effect(em.REF_MUTATION, name, em.INSIDE_REPO, "ref",
                                      "created"))
        else:
            observed.append(em.Effect(em.REF_MUTATION, name, em.INSIDE_REPO, "ref",
                                      f"{(was or '')[:12]} -> {(now or 'deleted')[:12]}"))

    if before.branch != after.branch:
        observed.append(em.Effect(em.REF_MUTATION, "HEAD:branch", em.INSIDE_REPO, "branch",
                                  f"{before.branch!r} -> {after.branch!r}"))
    return observed


def parents_of(root: str, sha: str) -> List[str]:
    code, out = _git(root, "rev-list", "--parents", "-n", "1", sha)
    if code != 0 or not out.strip():
        return []
    return out.split()[1:]


def resolve_head_kind(observed: List[em.Effect], root: str,
                      before: Snapshot, after: Snapshot) -> List[em.Effect]:
    """Settle the provisional HEAD effect: a commit advances, anything else moves.

    A new HEAD that is a descendant of the old one is a COMMIT. A new HEAD that is not
    — a reset, a checkout, a rebase, an amend — is a REF_MUTATION, whatever the actor
    intended and whatever the command was called.
    """
    if not (before.ok and after.ok) or before.head == after.head:
        return observed
    is_child = before.head in parents_of(root, after.head)
    for effect in observed:
        if effect.target == "HEAD" and effect.kind in (em.COMMIT, em.REF_MUTATION):
            effect.kind = em.COMMIT if is_child else em.REF_MUTATION
            effect.detail = f"{before.head[:12]} -> {after.head[:12]}" + (
                "" if is_child else ", not a descendant")
    return observed


# ── comparison ──────────────────────────────────────────────────────────────────────

def expand(effects: Sequence[em.Effect]) -> List[em.Effect]:
    """RENAME becomes DELETE + WRITE, on whichever side it appears.

    A `mv a b` authorises RENAME over both operands; the observation is a deletion and
    a creation. Expanding both sides is the only way the two can meet, and expanding
    only the authorised side would let an observed RENAME (a staged one, which git does
    report) go unmatched.
    """
    out: List[em.Effect] = []
    for effect in effects:
        if effect.kind != em.RENAME:
            out.append(effect)
            continue
        out.append(em.Effect(em.DELETE, effect.target, effect.scope,
                             effect.primitive, "rename source"))
        out.append(em.Effect(em.WRITE, effect.target, effect.scope,
                             effect.primitive, "rename destination"))
    return out


#: Which authorised kinds cover which observed kinds. An extraction produces writes; a
#: staged deletion produces both a DELETE and a STAGE.
COVERS: Dict[str, frozenset] = {
    em.WRITE: frozenset({em.WRITE}),
    em.DELETE: frozenset({em.DELETE}),
    em.ARCHIVE_EXTRACT: frozenset({em.WRITE, em.DELETE}),
    em.STAGE: frozenset({em.STAGE}),
    em.COMMIT: frozenset({em.COMMIT}),
    em.REF_MUTATION: frozenset({em.REF_MUTATION}),
    em.PERMISSION_CHANGE: frozenset({em.PERMISSION_CHANGE}),
    em.NETWORK_WRITE: frozenset(),
    em.READ: frozenset(),
}

#: Authorised kinds that leave no local trace, so their absence is not a MISSING effect.
UNOBSERVABLE = frozenset({em.NETWORK_WRITE, em.READ})


def _under(directory: str, path: str) -> bool:
    directory = em.normalise_target(directory)
    path = em.normalise_target(path)
    if not directory or not path:
        return False
    return path == directory or path.startswith(directory.rstrip("/") + "/")


def commit_covered_refs(current_branch: str, branch_after: Optional[str]) -> frozenset:
    """The refs an authorised COMMIT is allowed to have moved. Usually exactly one.

    🔴 A commit that succeeds with HEAD attached MOVES THE BRANCH. That is not a side
    effect, it is what committing means — and revision 8 reported it as
    `EXTRA[REF_MUTATION refs/heads/<branch>]` and marked every authorised commit
    `WRITE_RESULT_INVALID`. Measured on 2026-08-29 for both `git commit -m x <path>` and
    `git commit --allow-empty`.

    The coverage is deliberately the narrowest thing that makes a commit verifiable:

      - ONE ref, the branch HEAD pointed at BEFORE the command. Not "any ref", which
        would let an authorised commit cover a `git update-ref refs/heads/main <sha>`
        smuggled into the same invocation — the negative control that pins this.
      - Only when the branch did not CHANGE. A command that commits and also switches
        branches did two things, and the second is not part of committing.
      - Nothing at all when HEAD is detached, where a commit moves no ref and an
        observed ref mutation therefore came from somewhere else.
    """
    if not current_branch or branch_after != current_branch:
        return frozenset()
    return frozenset({f"refs/heads/{current_branch}"})


def verify(authorized: Sequence[em.Effect], observed: Sequence[em.Effect],
           repo_root: Optional[str] = None, current_branch: str = "",
           branch_after: Optional[str] = None) -> em.Comparison:
    """Set comparison with coverage. Extra OR missing is INVALID."""
    want = expand(authorized)
    have = expand(observed)
    covered_refs = commit_covered_refs(
        current_branch, current_branch if branch_after is None else branch_after)

    matched: List[em.Effect] = []
    extra: List[em.Effect] = []
    satisfied = set()

    for effect in have:
        hit = None
        for position, candidate in enumerate(want):
            # The compound rule: COMMIT covers the current branch ref moving with it.
            if (candidate.kind == em.COMMIT and effect.kind == em.REF_MUTATION
                    and effect.target in covered_refs):
                hit = position
                break
            if effect.kind not in COVERS.get(candidate.kind, frozenset()):
                continue
            if candidate.target is None:
                continue
            if em.normalise_target(candidate.target, repo_root) == em.normalise_target(
                    effect.target, repo_root) or _under(candidate.target, effect.target or ""):
                hit = position
                break
        if hit is None:
            extra.append(effect)
        else:
            matched.append(effect)
            satisfied.add(hit)

    # 🔴 An effect this instrument cannot see is not a missing effect.
    #
    # Two exemptions, and both were found by running the floor rather than by reading
    # the code. NETWORK_WRITE was declared from the start. The second was not: an
    # authorised write to `/tmp` or to another checkout lands entirely outside every
    # snapshot here, so `echo fine > /tmp/x` — an act SHELL_DEFAULT exists to permit —
    # was being reported MISSING and therefore WRITE_RESULT_INVALID. A verifier that
    # invalidates the writes it authorises is not a verifier.
    missing = [effect for position, effect in enumerate(want)
               if position not in satisfied
               and effect.kind not in UNOBSERVABLE
               and effect.scope == em.INSIDE_REPO]

    verdict = em.MATCH if not extra and not missing else em.MISMATCH
    return em.Comparison(verdict, matched, extra, missing)


# ── the executable model, end to end ────────────────────────────────────────────────

def run(command: str, root: str, actor: Optional[str] = None,
        authority: str = "SHELL_DEFAULT", include_ignored: bool = False,
        execute: bool = True) -> dict:
    """PREDICT → AUTHORISE → EXECUTE → OBSERVE → MATCH, in one call.

    🔴 A refused command is authorised for NOTHING, and this still runs the comparison
    with an empty authorised set — so if it ran anyway, every effect it produced is
    reported as EXTRA. That is the case the whole module exists for: a hook that did
    not fire is indistinguishable from a hook that allowed, unless someone looks after.
    """
    import guard_policy  # local: keeps effect_model importable without the policy

    predicted, _, parse_error = guard_policy.effects(command, cwd=root, repo_root=root)
    decision = em.authorize(predicted, authority)
    authorized = decision.authorized_effects

    before = snapshot(root, include_ignored)
    executed = False
    returncode = None
    if execute and decision.authorized and parse_error is None:
        executed = True
        try:
            completed = subprocess.run(command, shell=True, cwd=root,
                                       capture_output=True, text=True, timeout=600)
            returncode = completed.returncode
        except (OSError, subprocess.SubprocessError) as exc:
            returncode = -1
            executed = False
            parse_error = str(exc)
    after = snapshot(root, include_ignored)

    observed = resolve_head_kind(delta(before, after, root), root, before, after)
    comparison = verify(authorized, observed, root, current_branch=before.branch,
                        branch_after=after.branch)

    if not decision.authorized:
        # Refused. Nothing SHOULD have happened — so anything that did is the finding,
        # and it means the control did not hold. This is the branch that distinguishes
        # "the hook fired" from "the hook did not fire", which no PreToolUse hook can
        # ever report about itself.
        result = REFUSED if not observed else INVALID
    else:
        result = VALID if comparison.valid else INVALID
    # 🔴 Recorded from the run, so a receipt can say WHICH repository, WHICH base and
    # WHICH policy produced this verdict. `GUARD_REVISION_UNIFORM` is NO across this
    # repository — ten worktrees run the legacy guard and one runs this engine — so two
    # receipts that do not name their engine are not comparable, and a reader who
    # assumes they are is comparing verdicts from two different rule sets.
    import repo_topology as rt  # local: keeps this module importable without git
    topology = rt.of(root)
    scopes = sorted({e.scope for e in predicted}) or ["<none derived>"]

    return {
        "command": command,
        "actor": actor,
        "authority": authority,
        "repository_id": topology.repository_id or "UNDERIVABLE",
        "effective_workdir": root,
        "target_scope": ",".join(scopes),
        "guard_generation": _guard_generation(root),
        "guard_policy_hash": _guard_policy_hash(root),
        "predicted_effect": [e.as_dict() for e in predicted],
        "authorized_effect": [e.as_dict() for e in authorized],
        "authorization": decision.verdict,
        "authorization_reason": decision.reason(),
        "executed": executed,
        "returncode": returncode,
        "head_before": before.head,
        "head_after": after.head,
        "observed_effect": [e.as_dict() for e in observed],
        "match": comparison.verdict,
        "extra_effect": [e.as_dict() for e in comparison.extra],
        "missing_effect": [e.as_dict() for e in comparison.missing],
        "result": result,
        "result_reason": decision.reason() or comparison.reason(),
    }


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".")
    parser.add_argument("--actor")
    parser.add_argument("--authority", default="SHELL_DEFAULT")
    parser.add_argument("--include-ignored", action="store_true")
    parser.add_argument("--dry-run", action="store_true",
                        help="predict and authorise, snapshot twice, execute nothing")
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)

    command = " ".join(args.command).lstrip("- ").strip()
    if not command:
        parser.error("no command given")
    root = str(Path(args.root).resolve())
    report = run(command, root, args.actor, args.authority,
                 args.include_ignored, execute=not args.dry_run)
    print(json.dumps(report, indent=2, sort_keys=True))
    # 🔴 REFUSED exits 0: the control did its job, and a non-zero exit would make a
    # working guard look like a broken tool to any caller that checks status.
    return 0 if report["result"] in (VALID, REFUSED) else 1


if __name__ == "__main__":
    sys.exit(main())
