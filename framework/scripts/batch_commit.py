#!/usr/bin/env python3
"""Mechanical helper for the BATCH_COMMIT backup/restore phases, and for record-scoped propagation.

`propagate` is Phase 4 for the current files Benchmark J supported
(`framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/J3_DECISION.md`, PARTIALLY_SUPPORTED):
one atomic batch of record-scoped operations per file, through `record_scoped_edit.py`, every
byte outside the addressed records proven unchanged before anything is written. A file the
benchmark did not support is refused here by name, and keeps the full rewrite.
"""
import argparse
import json
import os
import shutil
import sys
from legend_lint import CURRENTS

# The state manifest and its cold half: a batch writes current values to the first and its
# scope to the second, so an ABORT must restore both or it restores half a batch.
EXTRA = ["framework/state/state_manifest_current.md", "framework/state/state_history.md"]

# Benchmark J · J3: the families whose every legitimate historical edit the editor reproduced.
# `paper_registry_current.md` lost one (a duplicated `## Purpose` heading) and is NOT here.
RECORD_SCOPED = (
    "disease-models/wwox/registries/working_model_current.md",
    "disease-models/wwox/registries/claim_registry_current.md",
    "disease-models/wwox/registries/literature_tracking_log_current.md",
)


def snapshot(repo_root, dest):
    os.makedirs(dest, exist_ok=True)
    for rel in CURRENTS + EXTRA:
        src = os.path.join(repo_root, rel)
        if os.path.isfile(src):
            dst = os.path.join(dest, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
    return dest

def restore(snapshot_dir, repo_root):
    for rel in CURRENTS + EXTRA:
        src = os.path.join(snapshot_dir, rel)
        if os.path.isfile(src):
            dst = os.path.join(repo_root, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)


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
        snapshot(args.repo_root, args.dest)
        print(f"Snapshot written to {args.dest}")
        return 0
    if args.command == "propagate":
        code, message = propagate(args.repo_root, args.file, args.ops, args.apply)
        print(message, file=sys.stderr if code else sys.stdout)
        return code
    if not args.confirm_restore:
        parser.error("restore requires --confirm-restore")
    restore(args.snapshot_dir, args.repo_root)
    print(f"Snapshot restored from {args.snapshot_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
