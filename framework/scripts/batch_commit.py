#!/usr/bin/env python3
"""Mechanical helper for the BATCH_COMMIT backup/restore phases."""
import argparse
import os
import shutil
from legend_lint import CURRENTS

EXTRA = ["framework/state/state_manifest_current.md"]

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
    args = parser.parse_args(argv)

    if args.command == "snapshot":
        snapshot(args.repo_root, args.dest)
        print(f"Snapshot written to {args.dest}")
        return 0
    if not args.confirm_restore:
        parser.error("restore requires --confirm-restore")
    restore(args.snapshot_dir, args.repo_root)
    print(f"Snapshot restored from {args.snapshot_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
