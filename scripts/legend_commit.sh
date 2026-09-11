#!/usr/bin/env bash
# Serialized, path-scoped WORK_COMMIT on the shared checkout.
#
# WHY THIS FILE IS VERSIONED. On 2026-09-08 this wrapper was written into a session
# scratchpad, did not survive the session, was re-created the next morning and shipped
# with an argument-ordering defect that the first actor to use it hit immediately
# (2026-09-09_actor_retrospective.md § 4.1). A tool three actors depend on cannot live
# outside the repository, and its smoke test must exercise the property that broke —
# a message containing spaces, passed alongside a `--` pathspec — not an adjacent one.
#
#   usage: scripts/legend_commit.sh "<commit message>" <path> [<path> ...]
#
# Concurrent actors share one checkout, so every commit takes an exclusive lock:
# `git commit` races on .git/index.lock. The commit is path-scoped, so an actor can
# never sweep up a peer's in-flight files — the control that answers "whose
# uncommitted file is this?" (§ 4.3) is discipline, and this is its mechanical half.
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "usage: legend_commit.sh \"<message>\" <path> [<path> ...]" >&2
  exit 2
fi

MSG="$1"; shift
ROOT="$(git rev-parse --show-toplevel)"

# FILE paths only. `git add -- <dir>` and `git commit -- <dir>` are directory-scoped, and a
# directory sweeps every peer's in-flight file beneath it under this actor's message - which
# is the authorship incident this wrapper exists to prevent (Mirror REV-EXPOST-20260911-001 F3,
# reproduced: "dir pathspec" committed a peer's file). Name the files.
for p in "$@"; do
  if [ -d "$ROOT/$p" ] || [ -d "$p" ]; then
    echo "refused: '$p' is a directory - name the files you own, one by one" >&2
    exit 4
  fi
done
LOCK="${LEGEND_COMMIT_LOCK:-$ROOT/.git/legend_commit.lock}"

exec 9>"$LOCK"
flock -w 900 9 || { echo "could not take the commit lock within 900s" >&2; exit 3; }

cd "$ROOT"
git add -- "$@"
if git diff --cached --quiet -- "$@"; then
  echo "NOTHING_TO_COMMIT"
  exit 0
fi
git commit -q -m "$MSG" -- "$@"
git --no-pager log -1 --oneline
