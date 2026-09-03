#!/usr/bin/env python3
"""When a `git push` is the actor's to make, and when it stays the operator's.

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
from typing import Callable, Dict, List, Optional

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
        except (OSError, subprocess.SubprocessError):
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
    """The branch a refspec pushes TO, or None when the two ends disagree.

    A refspec that renames — `local:refs/heads/other` — is outside this permission. Not
    because it is necessarily wrong, but because the record is keyed on one branch name
    and a rename makes "which branch was authorised" a question with two answers.
    """
    if ":" not in refspec:
        return refspec.rsplit("/", 1)[-1] or None
    source, _, destination = refspec.partition(":")
    if not source or not destination:
        return None
    if source.rsplit("/", 1)[-1] != destination.rsplit("/", 1)[-1]:
        return None
    return destination.rsplit("/", 1)[-1] or None


def evaluate(rest: List[str], root: Optional[str] = None,
             records: Optional[List[Dict]] = None,
             resolve: Optional[Callable[[str], Optional[str]]] = None) -> Verdict:
    """Judge one `git push`. `rest` is the argv AFTER the `push` subcommand.

    `records` and `resolve` are injectable so the battery can state a case without
    building a repository for it — the same reason `session_binding` takes an env.
    """
    flags = [token for token in rest if token.startswith("-")]
    for flag in flags:
        if flag in REFUSED_FLAGS:
            return Verdict(False, f"`{flag}` is refused: a push under this permission is "
                                  "fast-forward, names one ref, and deletes nothing")

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

    passing = [r for r in for_branch
               if r.get("gate_verdict") == "PASS" and r.get("gate_blocks") == 0]
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

    if branch == PROTECTED_REF:
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
    if branch == PROTECTED_REF:
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
