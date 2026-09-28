#!/usr/bin/env python3
"""Mechanical helper for the BATCH_COMMIT backup/restore phases, and for record-scoped propagation.

`propagate` is Phase 4 for the four scientific current files, all of which Benchmark J supported
(`framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/J3_DECISION.md` for three,
`J5_RESULTS.md` for the paper registry): one atomic batch of record-scoped operations per file,
through `record_scoped_edit.py`, every byte outside the addressed records proven unchanged before
anything is written. When the editor refuses, nothing is written and the file falls back to the
FULL rewrite for that batch — the refusal says so in one greppable line. Any other file is
refused by name.
"""
import argparse
import datetime
import glob
import json
import os
import re
import shutil
import subprocess
import sys
from legend_lint import CURRENTS

# The state manifest and its cold half: a batch writes current values to the first and its
# scope to the second, so an ABORT must restore both or it restores half a batch.
EXTRA = ["framework/state/state_manifest_current.md", "framework/state/state_history.md"]

# 🔴 THE SNAPSHOT'S COVERAGE IS DECLARED, NOT CODED.
# Until 2026-09-28 the snapshot copied `CURRENTS + EXTRA` — six files — while
# `prompt_batch_commit.md` Phase 3 named four more families. The gap was invisible until
# BATCH_20260928_001 edited `therapeutic_strategies_current.md` (named by neither) and had to
# copy it into the snapshot by hand: a file outside the snapshot is a file the Phase 5 / § 5
# ABORT cannot restore, so a silently short snapshot defeats the abort path entirely. The list
# now lives in the protocol that legislates it, as one fenced block under the marker below, and
# this tool reads it. Adding a file to the protocol snapshots it; there is no second list to
# forget. `test_batch_commit_snapshot.py` fails when a declared path is not in the snapshot.
PROTOCOL = "framework/protocols/prompt_batch_commit.md"
DECLARATION_MARKER = "SNAPSHOT_DECLARATION"
_DECLARED_PATH = re.compile(r"^\s*-\s+(\S+)\s*$")


class DeclarationError(RuntimeError):
    """The snapshot declaration is unreadable, incomplete, or names a missing file.

    Raised instead of snapshotting fewer files than declared: Phase 3 says
    "without a complete snapshot: ABORT", and a partial snapshot that reports success is the
    one outcome the abort path cannot survive.
    """


def declared_patterns(repo_root, protocol_rel=PROTOCOL):
    """The repo-relative paths/globs the protocol's SNAPSHOT_DECLARATION block names."""
    path = os.path.join(repo_root, protocol_rel)
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError as error:
        raise DeclarationError(
            f"cannot read the snapshot declaration in {protocol_rel}: {error}") from error
    head, marker, tail = text.partition(DECLARATION_MARKER)
    if not marker:
        raise DeclarationError(
            f"{protocol_rel} carries no {DECLARATION_MARKER} block: the snapshot's coverage "
            "is declared there, so there is nothing to snapshot from")
    block = tail.partition("```")[2].partition("```")[0]
    patterns = [match.group(1) for line in block.splitlines()
                if (match := _DECLARED_PATH.match(line))]
    if not patterns:
        raise DeclarationError(
            f"the {DECLARATION_MARKER} block in {protocol_rel} names no path")
    return patterns


def snapshot_targets(repo_root, protocol_rel=PROTOCOL):
    """Every existing file the declaration names, plus EXTRA; refuses rather than under-cover.

    A glob that matches nothing is allowed (a family can be empty); a literal path that does
    not exist is not, because that is how a renamed current file would leave the snapshot
    quietly short. The four scientific current files must be covered whatever the protocol
    says: a declaration edited down to nothing must not silently shrink the abort path.
    """
    patterns = declared_patterns(repo_root, protocol_rel)
    targets, missing = [], []
    for pattern in patterns:
        if any(character in pattern for character in "*?["):
            matches = glob.glob(os.path.join(repo_root, pattern))
            targets.extend(sorted(os.path.relpath(m, repo_root).replace(os.sep, "/")
                                  for m in matches if os.path.isfile(m)))
            continue
        if os.path.isfile(os.path.join(repo_root, pattern)):
            targets.append(pattern)
        else:
            missing.append(pattern)
    if missing:
        raise DeclarationError(
            "the snapshot declaration names files that do not exist, so the snapshot would be "
            "incomplete: " + ", ".join(missing))
    for rel in EXTRA:
        if rel not in targets and os.path.isfile(os.path.join(repo_root, rel)):
            targets.append(rel)
    uncovered = [rel for rel in CURRENTS
                 if rel not in targets and os.path.isfile(os.path.join(repo_root, rel))]
    if uncovered:
        raise DeclarationError(
            "the snapshot declaration does not cover the scientific current files: "
            + ", ".join(uncovered))
    return list(dict.fromkeys(targets))

# Benchmark J: the families whose every legitimate historical edit the editor reproduced — three
# at J3; the paper registry at J5 (328 / 328, S = 0), once `--under` could name one of its two
# `## Purpose` sections.
RECORD_SCOPED = (
    "disease-models/wwox/registries/working_model_current.md",
    "disease-models/wwox/registries/claim_registry_current.md",
    "disease-models/wwox/registries/literature_tracking_log_current.md",
    "disease-models/wwox/registries/paper_registry_current.md",
)


# 🔴 THE SNAPSHOT CARRIES ITS OWN BASE, BECAUSE THE ABORT COMMAND IS NOT WRITABLE WITHOUT IT.
# `git checkout -- <path>` restores the pre-batch value only while the propagation is neither
# staged nor committed. From the first `git add` onward it restores the BATCH's own output and
# reports success — and the Phase 5 / § 5 ABORT lives partly in that later window, because a
# batch commits its propagation with the surfaces Phase 4.7 regenerates. The only command that
# is correct in both windows names its base: `git checkout <pre-batch SHA> -- <path>`. That SHA
# is knowable exactly once — at Phase 3, before anything is written — so it is recorded here, in
# the snapshot, by the tool that takes it. A SHA an aborting actor has to reconstruct from the
# reflog under time pressure is a SHA that gets guessed.
BASE_FILE = "SNAPSHOT_BASE.json"


def snapshot_base(repo_root, targets):
    """The pre-batch git base of this snapshot, and what the base can and cannot restore.

    `dirty_at_snapshot` is the honest half: for a declared path already modified when the
    snapshot was taken, the base commit holds the value before THAT edit too, so restoring it
    from the SHA discards work the snapshot preserved. For those paths the snapshot directory
    is the only correct source, and the field says which they are instead of leaving an
    aborting actor to find out afterwards.
    """
    def git(*arguments):
        try:
            done = subprocess.run(("git", *arguments), cwd=repo_root, check=True,
                                  capture_output=True, text=True)
        except (OSError, subprocess.CalledProcessError):
            return None
        return done.stdout.strip()

    head = git("rev-parse", "HEAD")
    if head is None:
        return {
            "pre_batch_commit": None,
            "branch": None,
            "dirty_at_snapshot": [],
            "taken_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
            "note": "not a git checkout: the snapshot directory is the only restore source",
        }
    # `git diff --name-only HEAD` and not `git status --porcelain`: the condition that matters
    # is "already differs from the base commit", which is what makes the SHA the wrong source,
    # and it is asked directly instead of being recovered by slicing a status line by column.
    differs = git("diff", "--name-only", "HEAD", "--", *targets) or ""
    dirty = sorted({line.strip() for line in differs.splitlines() if line.strip()})
    return {
        "pre_batch_commit": head,
        "branch": git("rev-parse", "--abbrev-ref", "HEAD"),
        "dirty_at_snapshot": dirty,
        "taken_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "note": ("restore with `batch_commit.py restore`; `git checkout "
                 f"{head} -- <path>` is the base-qualified fallback, and is WRONG for the "
                 "paths in dirty_at_snapshot"),
    }


def snapshot(repo_root, dest, protocol_rel=PROTOCOL):
    targets = snapshot_targets(repo_root, protocol_rel)
    os.makedirs(dest, exist_ok=True)
    for rel in targets:
        src = os.path.join(repo_root, rel)
        dst = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    with open(os.path.join(dest, BASE_FILE), "w", encoding="utf-8") as handle:
        json.dump(snapshot_base(repo_root, targets), handle, indent=2)
        handle.write("\n")
    return targets


def read_base(snapshot_dir):
    """The recorded base of a snapshot, or None for a snapshot taken before it was recorded."""
    path = os.path.join(snapshot_dir, BASE_FILE)
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def base_report(snapshot_dir):
    """The ABORT paragraph an actor can paste, or None when this snapshot records no base."""
    base = read_base(snapshot_dir)
    if base is None:
        return None
    head = base.get("pre_batch_commit")
    lines = [f"PRE_BATCH_COMMIT: {head or '(not a git checkout)'}"
             f"   branch: {base.get('branch') or '-'}"]
    lines.append(f"Record it in the activity log beside the snapshot path ({snapshot_dir}).")
    lines.append("ABORT restores with, in this order:")
    lines.append(f"  python3 framework/scripts/batch_commit.py restore "
                 f"--snapshot-dir {snapshot_dir} --confirm-restore")
    if head:
        lines.append(f"  git checkout {head} -- <path>      "
                     "# base-qualified fallback for a path the snapshot does not hold")
        lines.append("  `git checkout -- <path>` WITHOUT a base is correct only until the "
                     "propagation is staged or committed; after that it restores the batch.")
    dirty = base.get("dirty_at_snapshot") or []
    if dirty:
        lines.append("  NOT restorable from the SHA — already modified when the snapshot was "
                     "taken; use the snapshot directory:")
        lines.extend(f"    {rel}" for rel in dirty)
    return "\n".join(lines)


def snapshot_contents(snapshot_dir):
    """What a snapshot directory actually holds, repo-relative.

    `SNAPSHOT_BASE.json` is metadata ABOUT the snapshot, not a file of the repository, and is
    excluded: `restore` copies back exactly what this returns, so including it would write the
    metadata into the repository root on every abort.
    """
    held = []
    for directory, _children, files in os.walk(snapshot_dir):
        held.extend(os.path.relpath(os.path.join(directory, name), snapshot_dir)
                    .replace(os.sep, "/") for name in files)
    return sorted(rel for rel in held if rel != BASE_FILE)


def restore(snapshot_dir, repo_root):
    """Restore exactly what the snapshot holds — not what a list says it should hold.

    Restoring from a fixed list was the second half of the same defect: a snapshot widened by
    the protocol would have been taken and then only partly put back.
    """
    restored = snapshot_contents(snapshot_dir)
    for rel in restored:
        dst = os.path.join(repo_root, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(snapshot_dir, rel), dst)
    return restored


def propagate(repo_root, rel, ops_path, apply=False):
    """Apply one atomic batch of record-scoped operations to one supported current file.

    Returns (exit code, message). 0 applied or clean dry run · 3 refused (nothing written; the
    file takes the FULL rewrite for this batch, recorded in the report) · 4 not a record-scoped
    current file.
    """
    import record_scoped_edit as rse
    rel = rel.replace(os.sep, "/")
    if rel not in RECORD_SCOPED:
        return 4, (f"{rel} is not a record-scoped current file ({', '.join(RECORD_SCOPED)}); "
                   "nothing was written.")
    path = os.path.join(repo_root, rel)
    with open(path, "rb") as handle:
        text = handle.read().decode("utf-8")
    with open(ops_path, encoding="utf-8") as handle:
        ops = [rse.Op.from_dict(item) for item in json.load(handle)]
    try:
        out, report = rse.apply_ops(text, ops, rse.levels_for(rel))
    except rse.Refusal as refusal:
        # 🔴 A REFUSAL IS NEVER FORCED. It is either a mistake in the operation list — fix it and
        # rerun — or an edit outside what the editor can prove, which that file takes by FULL
        # rewrite for this batch. The marker line is what later measures how often that is.
        return 3, (f"REFUSED — {refusal}. Nothing was written to {rel}.\n"
                   f"FULL_FALLBACK {rel} {refusal.code} — fix the operation list if it is wrong; "
                   "otherwise propagate this file by full rewrite for this batch and record this "
                   "line in the batch report (prompt_batch_commit.md Phase 4.0).")
    if apply and out != text:
        with open(path, "wb") as handle:
            handle.write(out.encode("utf-8"))
    verb = "APPLIED" if apply else "DRY RUN (add --apply)"
    return 0, f"{verb}: {rel} — {len(report.ops)} op(s) on {report.changed_keys}"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    snapshot_parser = subparsers.add_parser(
        "snapshot", help="copy current/state files into a snapshot directory"
    )
    snapshot_parser.add_argument("--repo-root", default=".")
    snapshot_parser.add_argument("--dest", required=True)

    restore_parser = subparsers.add_parser(
        "restore", help="restore current/state files from a snapshot"
    )
    restore_parser.add_argument("--snapshot-dir", required=True)
    restore_parser.add_argument("--repo-root", default=".")
    restore_parser.add_argument(
        "--confirm-restore",
        action="store_true",
        help="required acknowledgement because restore overwrites current files",
    )
    base_parser = subparsers.add_parser(
        "base",
        help="print the pre-batch commit a snapshot recorded, and the ABORT commands that "
             "are correct after the propagation has been staged or committed",
    )
    base_parser.add_argument("--snapshot-dir", required=True)

    propagate_parser = subparsers.add_parser(
        "propagate",
        help="Phase 4 for a record-scoped current file: one atomic batch of "
             "record_scoped_edit.py operations (dry run unless --apply)",
    )
    propagate_parser.add_argument("--repo-root", default=".")
    propagate_parser.add_argument("--file", required=True,
                                  help="repo-relative current file, e.g. "
                                       "disease-models/wwox/registries/claim_registry_current.md")
    propagate_parser.add_argument("--ops", required=True,
                                  help="JSON list of {op, id|heading[+under]|preamble, text|old|new, rename_to}")
    propagate_parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    if args.command == "snapshot":
        try:
            targets = snapshot(args.repo_root, args.dest)
        except DeclarationError as error:
            print(f"REFUSED: {error}\nNothing was written; Phase 3 says ABORT without a "
                  "complete snapshot.", file=sys.stderr)
            return 2
        print(f"Snapshot written to {args.dest} — {len(targets)} file(s):")
        for rel in targets:
            print(f"  {rel}")
        print()
        print(base_report(args.dest))
        return 0
    if args.command == "base":
        report = base_report(args.snapshot_dir)
        if report is None:
            print(f"{args.snapshot_dir} records no base (taken before "
                  f"{BASE_FILE} existed): restore from the snapshot directory, and derive the "
                  "pre-batch SHA from the activity log entry Phase 3 requires.",
                  file=sys.stderr)
            return 1
        print(report)
        return 0
    if args.command == "propagate":
        code, message = propagate(args.repo_root, args.file, args.ops, args.apply)
        print(message, file=sys.stderr if code else sys.stdout)
        if code:
            # Measured 2026-09-28: a peer read this refusal as exit 0 through `| head`. A pipeline
            # reports its LAST command's status, which would hide an exit 3 mid-batch exactly so.
            print(f"exit {code}: this refusal is carried by the exit status, which a pipeline "
                  "does not preserve — read $? directly or run under `set -o pipefail`.",
                  file=sys.stderr)
        return code
    if not args.confirm_restore:
        parser.error("restore requires --confirm-restore")
    restored = restore(args.snapshot_dir, args.repo_root)
    print(f"Snapshot restored from {args.snapshot_dir} — {len(restored)} file(s)")
    base = read_base(args.snapshot_dir)
    if base and base.get("pre_batch_commit"):
        print(f"Pre-batch commit of this snapshot: {base['pre_batch_commit']} — a path the "
              "snapshot does not hold is restored with `git checkout "
              f"{base['pre_batch_commit']} -- <path>`, never with a bare `git checkout --`.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
