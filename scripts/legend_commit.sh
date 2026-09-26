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
#   exit:  0 committed / nothing to commit · 2 usage · 3 lock timeout · 4 directory pathspec
#          5 generated surfaces stale or unverifiable on the candidate commit (see below)
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
# The lock lives in the COMMON git directory, so every worktree of this repository contends for
# one lock. `$ROOT/.git` is a directory only in the main checkout; in a linked worktree it is a
# gitfile, and the old `$ROOT/.git/legend_commit.lock` path could not even be opened there.
COMMON="$(git rev-parse --path-format=absolute --git-common-dir)"
LOCK="${LEGEND_COMMIT_LOCK:-$COMMON/legend_commit.lock}"

exec 9>"$LOCK"
flock -w 900 9 || { echo "could not take the commit lock within 900s" >&2; exit 3; }

cd "$ROOT"

# Generated-surface freshness on the EXACT commit this call makes: HEAD + the named files'
# working-tree content (candidate_tree_freshness.py --paths) — not the shared workspace, which
# holds peers' edits. H0 (2026-09-24): three direct commits of inputs (a receipt, a direct
# propagation, a queue edit) left four generated surfaces stale, and nothing on this path
# looked. Name the regenerated surface alongside its input, or state why not:
#   LEGEND_STALE_SURFACES_BECAUSE="<reason>" scripts/legend_commit.sh "<msg>" <paths>
# The reason is printed and recorded as a trailer of the commit message.
FRESHNESS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/framework/scripts/candidate_tree_freshness.py"
if [ -f "$FRESHNESS" ]; then
  set +e
  REPORT="$(python3 "$FRESHNESS" --repo "$ROOT" --paths "$@" 2>&1)"
  CODE=$?
  set -e
  if [ "$CODE" -ne 0 ]; then
    printf '%s\n' "$REPORT" >&2
    if [ -n "${LEGEND_STALE_SURFACES_BECAUSE:-}" ]; then
      echo "committing although generated surfaces are not fresh, because: $LEGEND_STALE_SURFACES_BECAUSE" >&2
      MSG="$MSG

Stale-surfaces-because: $LEGEND_STALE_SURFACES_BECAUSE"
    else
      echo "refused: this commit would leave generated surfaces stale or unverifiable (exit $CODE)." >&2
      echo "Regenerate and name the surface too, or set LEGEND_STALE_SURFACES_BECAUSE=\"<reason>\"." >&2
      exit 5
    fi
  fi
fi

git add -- "$@"
if git diff --cached --quiet -- "$@"; then
  echo "NOTHING_TO_COMMIT"
  exit 0
fi
git commit -q -m "$MSG" -- "$@"
git --no-pager log -1 --oneline
