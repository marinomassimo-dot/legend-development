#!/usr/bin/env python3
"""Mechanical helper for the BATCH_COMMIT backup/restore phases, and for record-scoped propagation.

`propagate` is Phase 4 for the current files Benchmark J supported
(`framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/J3_DECISION.md`, PARTIALLY_SUPPORTED):
one atomic batch of record-scoped operations per file, through `record_scoped_edit.py`, every
byte outside the addressed records proven unchanged before anything is written. A file the
benchmark did not support is refused here by name, and keeps the full rewrite.
"""
import argparse
import glob
import json
import os
import re
import shutil
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

# Benchmark J · J3: the families whose every legitimate historical edit the editor reproduced.
# `paper_registry_current.md` lost one (a duplicated `## Purpose` heading) and is NOT here.
RECORD_SCOPED = (
    "disease-models/wwox/registries/working_model_current.md",
    "disease-models/wwox/registries/claim_registry_current.md",
    "disease-models/wwox/registries/literature_tracking_log_current.md",
)


def snapshot(repo_root, dest, protocol_rel=PROTOCOL):
    targets = snapshot_targets(repo_root, protocol_rel)
    os.makedirs(dest, exist_ok=True)
    for rel in targets:
        src = os.path.join(repo_root, rel)
        dst = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    return targets


def snapshot_contents(snapshot_dir):
    """What a snapshot directory actually holds, repo-relative."""
    held = []
    for directory, _children, files in os.walk(snapshot_dir):
        held.extend(os.path.relpath(os.path.join(directory, name), snapshot_dir)
                    .replace(os.sep, "/") for name in files)
    return sorted(held)


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

    Returns (exit code, message). 0 applied or clean dry run · 3 refused (nothing written) ·
    4 the file is not one Benchmark J supported: propagate it by full rewrite.
    """
    import record_scoped_edit as rse
    rel = rel.replace(os.sep, "/")
    if rel not in RECORD_SCOPED:
        return 4, (f"{rel} is not propagated record by record: Benchmark J (J3_DECISION.md) "
                   "did not support it. Use the full rewrite of prompt_batch_commit.md Phase 4 "
                   "for this file.")
    path = os.path.join(repo_root, rel)
    with open(path, "rb") as handle:
        text = handle.read().decode("utf-8")
    with open(ops_path, encoding="utf-8") as handle:
        ops = [rse.Op.from_dict(item) for item in json.load(handle)]
    try:
        out, report = rse.apply_ops(text, ops, rse.levels_for(rel))
    except rse.Refusal as refusal:
        return 3, f"REFUSED — {refusal}. Nothing was written to {rel}."
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
                                  help="JSON list of {op, id|heading|preamble, text|old|new, rename_to}")
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
        return 0
    if args.command == "propagate":
        code, message = propagate(args.repo_root, args.file, args.ops, args.apply)
        print(message, file=sys.stderr if code else sys.stdout)
        return code
    if not args.confirm_restore:
        parser.error("restore requires --confirm-restore")
    restored = restore(args.snapshot_dir, args.repo_root)
    print(f"Snapshot restored from {args.snapshot_dir} — {len(restored)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
