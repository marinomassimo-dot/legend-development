#!/usr/bin/env python3
"""When a `git push` is the actor's to make, and when it stays the operator's.

🔴 **SPECIFIED, NOT ENFORCED.** Nothing consults this module: `guard_policy` does not import
it, and every push is refused by the blanket `DENY_NETWORK`. Read everything below as the
shape the guard must take when it is rebuilt, never as a description of what runs today.
`KnownHolesThisSpecificationStillHas` in the battery is the list of what this module still
gets wrong, and it is not short.

Publication used to be refused outright: `DENY_NETWORK` said *"Publication is an operator
act and needs PUBLISH authority, which is never granted by a runtime."* That is the right
rule for `origin`, and it was too coarse for `development` — it made every CI observation
cost an operator round trip, which is where most of this laboratory's stops came from.

The operator's decision of 2026-09-03 replaces the blanket refusal with a discriminator.
The earlier attempt used "is the remote credential-gated", which discriminates nothing:
GitHub gates writes on every repository, `origin` included, so the test was true of exactly
the case it was meant to exclude. These conditions are properties of the PUSH, not of the
remote:

```text
remote is `development`, named explicitly          — never `origin`, never a bare push
no force, no non-fast-forward                      — including --force-with-lease
public_release_gate PASS on the exact tree pushed  — recorded, not re-run here
the push is recorded: branch, SHA, gate, actor     — the record IS the precondition
ref is not `main` … unless the merge that produced it was the agents' to make
```

🔴 **The gate result is read, never computed here.** A `PreToolUse` hook has ten seconds
and runs on every command; walking the tree inside it would make the guard the slowest
thing in the session and would tempt a future revision to cache the answer. So the actor
runs the gate first and records the verdict against a SHA, and the guard checks that a
record exists for the exact SHA being pushed. The recording obligation is discharged by
construction: without the record there is no push.

🔴 **The `main` carve-out is narrow on purpose.** `main` is remote-equivalent to
`development/main`, so pushing it publishes the canonical edition. It is permitted only
when the merge that produced it was itself inside the agents' authority under §21d — which
means it changed no guarantee. A merge that changes a guarantee, and its push, are the
operator's, and the record cannot assert otherwise on the actor's own say-so alone: the
field is written by whoever ran the merge and read by Mirror afterwards.

The ledger is `ledger/push_authorizations.jsonl`, append-only, one object per line:

```json
{"branch": "plan-x", "sha": "<40 hex>", "gate_verdict": "PASS", "gate_blocks": 0,
 "actor": "orchestrator", "recorded_at": "2026-09-03T12:00:00+02:00",
 "merge_changed_no_guarantee": true}
```

`merge_changed_no_guarantee` is required only for `main` and ignored elsewhere.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence

LEDGER_RELATIVE = "ledger/push_authorizations.jsonl"
ALLOWED_REMOTE = "development"
PROTECTED_REF = "main"

#: Flags that make a push destructive, unbounded, or wider than the ref it names.
#: `--force-with-lease` is refused with the rest: it is safer than `--force` against a
#: concurrent writer and exactly as final against a reader who has already fetched.
REFUSED_FLAGS = frozenset({
    "--force", "-f", "--force-with-lease", "--force-if-includes",
    "--mirror", "--delete", "-d", "--prune",
    "--all", "--tags", "--follow-tags",
})

#: 🔴 Short options BUNDLE, and an exact-match list does not see it. The first draft
#: refused `-f` and allowed `-fu`, which is the same forced update with one letter added;
#: Mirror pushed a real non-fast-forward through it. Membership is now tested per letter.
REFUSED_SHORT = frozenset("fd")

#: Global options that move the repository the command acts on. `git_subcommand` skips them
#: to reach the subcommand, so by the time this module is consulted they are gone — which
#: is how `git -C <peer> push` had its SHA verified in one repository and its objects sent
#: from another. The guard passes them back in explicitly.
REDIRECTING_GLOBALS = frozenset({"-C", "--git-dir", "--work-tree", "--namespace",
                                 "--exec-path"})

#: 🔴 `redirected` is not only for option tokens. It is the channel for ANY out-of-band way
#: the command's repository or its executables were moved, and it already refuses whatever it
#: is handed — an earlier note in this file claimed environment prefixes and the payload's
#: `workdir` were "not expressible at this layer", and that was wrong: the parameter takes
#: them today and denies. NO CALLER POPULATES EITHER SET — nothing in the tree reads these
#: two names, and that is the work, not an oversight to be read as done. These are the names
#: a caller must pass through once one exists:
REDIRECTING_ENVIRONMENT = frozenset({
    "GIT_DIR", "GIT_WORK_TREE", "GIT_NAMESPACE", "GIT_EXEC_PATH",
    "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES",
})


def _side(token: str) -> Optional[str]:
    """The branch one side of a refspec names, or None when it does not name a branch.

    🔴 The first draft took the last path segment, so `refs/tags/work` was gated as the
    branch `work` and published an object the release gate had never seen. A qualified ref
    is accepted only under `refs/heads/`; everything else — tags, remotes, `HEAD`, an empty
    side, anything carrying a control character or the parser's OPAQUE sentinel — is not a
    branch this permission covers.
    """
    if token.startswith("refs/"):
        if not token.startswith("refs/heads/"):
            return None
        token = token[len("refs/heads/"):]
    if not token or token == "HEAD" or token.startswith("-"):
        return None
    if any(character.isspace() or not character.isprintable() for character in token):
        return None
    return token


@dataclass(frozen=True)
class Verdict:
    """Allowed, or refused with the condition that failed named in the refusal."""

    allowed: bool
    reason: str = ""
    remote: str = ""
    ref: str = ""


def _resolve_with_git(root: str) -> Callable[[str], Optional[str]]:
    def resolve(ref: str) -> Optional[str]:
        try:
            done = subprocess.run(
                ["git", "-C", root, "rev-parse", "--verify", "--quiet", f"refs/heads/{ref}"],
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, timeout=5)
        except (OSError, ValueError, subprocess.SubprocessError):
            # 🔴 ValueError belongs here: a refspec carrying the parser's OPAQUE sentinel
            # reaches `subprocess` with an embedded null byte and raises. The hook caught
            # only `Undecidable`, so the process died — and on this channel a dead hook is
            # silence, and silence is ALLOW. Failing to resolve must refuse, never crash.
            return None
        sha = done.stdout.strip()
        return sha if done.returncode == 0 and len(sha) == 40 else None
    return resolve


def read_ledger(root: str) -> List[Dict]:
    """Every well-formed record. A malformed line is skipped, never guessed at."""
    path = Path(root) / LEDGER_RELATIVE
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    records = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict):
            records.append(record)
    return records


def branch_of(refspec: str) -> Optional[str]:
    """The branch a refspec pushes TO, or None when it is not one branch to itself.

    A refspec that renames — `local:refs/heads/other` — is outside this permission. Not
    because it is necessarily wrong, but because the record is keyed on one branch name and
    a rename makes "which branch was authorised" a question with two answers. Both sides
    must name the SAME branch under `refs/heads/`, which is also what stops
    `refs/remotes/x/work:refs/heads/work` from publishing an unreviewed object as `work`.
    """
    if ":" not in refspec:
        return _side(refspec)
    source, _, destination = refspec.partition(":")
    left, right = _side(source), _side(destination)
    if not left or not right or left != right:
        return None
    return right


def evaluate(rest: List[str], root: Optional[str] = None,
             records: Optional[List[Dict]] = None,
             resolve: Optional[Callable[[str], Optional[str]]] = None,
             redirected: Sequence[str] = ()) -> Verdict:
    """Judge one `git push`. `rest` is the argv AFTER the `push` subcommand.

    `records` and `resolve` are injectable so the battery can state a case without building
    a repository for it — the same reason `session_binding` takes an env. `redirected`
    carries the repository-moving globals the guard stripped before reaching here.
    """
    if redirected:
        return Verdict(False,
                       f"`{', '.join(sorted(set(redirected)))}` moves the repository this "
                       "command acts on, so the SHA and the ledger would be read in one "
                       "repository while the objects were sent from another")

    for token in rest:
        if not token.startswith("-"):
            continue
        stem = token.split("=", 1)[0]
        if token in REFUSED_FLAGS or stem in REFUSED_FLAGS:
            return Verdict(False, f"`{token}` is refused: a push under this permission is "
                                  "fast-forward, names one ref, and deletes nothing")
        if not token.startswith("--"):
            bundled = sorted(set(token[1:]) & REFUSED_SHORT)
            if bundled:
                return Verdict(False,
                               f"`{token}` bundles `-{'`, `-'.join(bundled)}`, and a short "
                               "option is refused by the letter it carries, not by how it "
                               "was spelled")

    operands = [token for token in rest if not token.startswith("-")]
    if not operands:
        return Verdict(False, "a bare `git push` names no remote, and the default is "
                              "`origin` — a different repository from the one work here "
                              "targets")

    remote = operands[0]
    if remote != ALLOWED_REMOTE:
        return Verdict(False, f"`{remote}` is not `{ALLOWED_REMOTE}`. `origin` is denied to "
                              "every runtime, always; any other remote is underived",
                       remote=remote)

    if len(operands) < 2:
        return Verdict(False, "names a remote but no ref, so what would be pushed depends "
                              "on push.default and is not readable from the command",
                       remote=remote)
    if len(operands) > 2:
        return Verdict(False, "names more than one ref; this permission covers one",
                       remote=remote)

    refspec = operands[1]
    if refspec.startswith("+"):
        return Verdict(False, "a `+` refspec forces a non-fast-forward update",
                       remote=remote, ref=refspec)

    branch = branch_of(refspec)
    if not branch:
        return Verdict(False, f"`{refspec}` renames the ref as it pushes, and the "
                              "authorisation record is keyed on one branch name",
                       remote=remote, ref=refspec)

    if resolve is None:
        if root is None:
            return Verdict(False, "no repository root, so the pushed SHA is underivable",
                           remote=remote, ref=branch)
        resolve = _resolve_with_git(root)
    sha = resolve(branch)
    if not sha:
        return Verdict(False, f"`{branch}` does not resolve to a commit in this repository",
                       remote=remote, ref=branch)

    if records is None:
        if root is None:
            return Verdict(False, "no repository root, so the ledger is unreadable",
                           remote=remote, ref=branch)
        records = read_ledger(root)

    for_branch = [r for r in records if r.get("branch") == branch and r.get("sha") == sha]
    if not for_branch:
        return Verdict(False,
                       f"no authorisation in {LEDGER_RELATIVE} for `{branch}` at {sha[:12]}. "
                       "Run the release gate and record its verdict against this exact SHA "
                       f"first: `python3 framework/scripts/push_authorization.py record "
                       f"--branch {branch}`",
                       remote=remote, ref=branch)

    def clean(entry: Dict) -> bool:
        blocks = entry.get("gate_blocks")
        # `== 0` alone accepts False and 0.0; a boolean in this field means the record was
        # written by something that did not read the gate's output.
        return (entry.get("gate_verdict") == "PASS"
                and isinstance(blocks, int) and not isinstance(blocks, bool)
                and blocks == 0)

    passing = [r for r in for_branch if clean(r)]
    if not passing:
        return Verdict(False, f"the recorded release gate for `{branch}` at {sha[:12]} is "
                              "not a clean PASS, and a red gate is not published",
                       remote=remote, ref=branch)

    unattributed = [r for r in passing if not str(r.get("actor") or "").strip()]
    if len(unattributed) == len(passing):
        return Verdict(False, "the authorisation records no actor, and an unattributed "
                              "publication is not reviewable",
                       remote=remote, ref=branch)
    passing = [r for r in passing if str(r.get("actor") or "").strip()]

    if branch.lower() == PROTECTED_REF:
        cleared = [r for r in passing if r.get("merge_changed_no_guarantee") is True]
        if not cleared:
            return Verdict(False,
                           "`main` is published only when the merge that produced it was "
                           "the agents' to make. The record does not assert "
                           "`merge_changed_no_guarantee`, so this merge — and its push — "
                           "are the operator's",
                           remote=remote, ref=branch)

    return Verdict(True, remote=remote, ref=branch)


# --------------------------------------------------------------------------- recording


def record(root: str, branch: str, actor: str,
           merge_changed_no_guarantee: bool = False) -> int:
    """Run the release gate, then append the authorisation it justifies."""
    resolve = _resolve_with_git(root)
    sha = resolve(branch)
    if not sha:
        print(f"REFUSED: `{branch}` does not resolve to a commit", file=sys.stderr)
        return 2

    gate = subprocess.run([sys.executable, "scripts/public_release_gate.py"],
                          cwd=root, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, text=True)
    verdict, blocks = "UNREADABLE", -1
    for line in gate.stdout.splitlines():
        if line.startswith("VERDICT:"):
            verdict = line.split(":", 1)[1].strip()
        elif line.startswith("BLOCKS:"):
            try:
                blocks = int(line.split(":", 1)[1].strip())
            except ValueError:
                blocks = -1

    entry = {
        "branch": branch,
        "sha": sha,
        "gate_verdict": verdict,
        "gate_blocks": blocks,
        "actor": actor,
        "recorded_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
    }
    if branch.lower() == PROTECTED_REF:
        entry["merge_changed_no_guarantee"] = merge_changed_no_guarantee

    path = Path(root) / LEDGER_RELATIVE
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(json.dumps(entry, ensure_ascii=False))
    return 0 if verdict == "PASS" and blocks == 0 else 1


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    recorder = sub.add_parser("record", help="run the release gate and authorise one push")
    recorder.add_argument("--branch", required=True)
    recorder.add_argument("--actor", default="orchestrator")
    recorder.add_argument("--root", default=".")
    recorder.add_argument("--merge-changed-no-guarantee", action="store_true",
                          help="only meaningful for `main`; asserts the merge was the "
                               "agents' to make under §21d")

    checker = sub.add_parser("check", help="judge a push without running it")
    checker.add_argument("argv", nargs=argparse.REMAINDER)
    checker.add_argument("--root", default=".")

    args = parser.parse_args(argv)
    if args.command == "record":
        return record(str(Path(args.root).resolve()), args.branch, args.actor,
                      args.merge_changed_no_guarantee)

    rest = list(args.argv)
    while rest and rest[0] in ("git", "push"):
        rest.pop(0)
    verdict = evaluate(rest, root=str(Path(args.root).resolve()))
    print("ALLOWED" if verdict.allowed else f"REFUSED: {verdict.reason}")
    return 0 if verdict.allowed else 1


if __name__ == "__main__":
    sys.exit(main())
