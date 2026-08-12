#!/usr/bin/env bash
# legend_launch.sh — fail-closed birth and recovery for ONE LEGEND actor.
#
# MINIMUM RUNTIME KERNEL. Actor and worktree are PARAMETERS: this script holds no
# actor table, so the future registry supplies the same parameters from a versioned
# file without any logic here having to be dismantled.
#
# It governs BIRTH and ENVIRONMENT only. The supervisor governs the session's life,
# and LEGEND adds only the invariants Claude Code does not guarantee:
#
#   --name is a LIVENESS requirement, not a convenience. Measured 2026-08-12:
#   a session whose cwd is .claude/worktrees/evidence-index is named
#   `legend-public-ec`, so the default name does NOT reflect the worktree
#   directory and five nested actors would be mutually indistinguishable.
#   (The mechanism behind the default is OPEN; only the fact is measured.)
#
#   --settings is passed at EVERY process start. A normal resume does not restore
#   `--settings`, so the transport must be supplied by the launcher each time.
#
#   ONE CANONICAL SESSION LINEAGE PER (actor_id, runtime_instance). The lineage
#   store is PER-CELL and NOT versioned: a lineage that travelled with the
#   repository would refuse the first birth on a target host and turn the defence
#   into a block at the first cutover.
#
# Fail-closed here rather than in a hook because a SessionStart hook cannot block a
# session from starting; this is the boundary LEGEND chose, not the only one possible.
#
# Usage:
#   legend_launch.sh birth  <actor_id> <worktree_path> <branch> [extra claude args...]
#   legend_launch.sh resume <actor_id> <worktree_path> <branch> [extra claude args...]
#   legend_launch.sh check  <actor_id> <worktree_path> <branch>
#
# `check` runs every precondition and launches nothing: it is how a fail-closed
# path is tested without creating a session.

set -euo pipefail

CERTIFIED_VERSION="${LEGEND_CERTIFIED_VERSION:-2.1.228}"
RUNTIME_INSTANCE="${LEGEND_RUNTIME_INSTANCE:-$(hostname -s)-$(id -un)}"
LINEAGE_DIR="${LEGEND_LINEAGE_DIR:-$HOME/.legend/lineage}/$RUNTIME_INSTANCE"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
TRANSPORT="${LEGEND_TRANSPORT_SETTINGS:-$SCRIPT_DIR/transport.json}"

die() { printf 'LAUNCH_REFUSED %s: %s\n' "${1}" "${2}" >&2; exit 1; }

[ $# -ge 4 ] || die USAGE "mode, actor_id, worktree and branch are all required"
MODE="$1"; ACTOR="$2"; WORKTREE="$3"; BRANCH="$4"; shift 4

LINEAGE_FILE="$LINEAGE_DIR/$ACTOR.json"

# ---- environment preconditions ------------------------------------------------
[ -f "$TRANSPORT" ] || die TRANSPORT_MISSING "$TRANSPORT"

HAVE_VERSION="$(claude --version 2>/dev/null | awk '{print $1}')"
[ "$HAVE_VERSION" = "$CERTIFIED_VERSION" ] || \
  die HOST_RUNTIME_UNQUALIFIED "claude $HAVE_VERSION != certified $CERTIFIED_VERSION"

# ---- location preconditions, checked from INSIDE the worktree -----------------
[ -d "$WORKTREE" ] || die WORKTREE_ABSENT "$WORKTREE"
cd -- "$WORKTREE"

HERE="$(pwd -P)"
WANT="$(cd -- "$WORKTREE" && pwd -P)"
[ "$HERE" = "$WANT" ] || die CWD_MISMATCH "$HERE != $WANT"

TOPLEVEL="$(git rev-parse --show-toplevel)"
[ "$TOPLEVEL" = "$WANT" ] || die TOPLEVEL_MISMATCH "$TOPLEVEL != $WANT"

HAVE_BRANCH="$(git branch --show-current)"
[ "$HAVE_BRANCH" = "$BRANCH" ] || die BRANCH_MISMATCH "on '$HAVE_BRANCH', expected '$BRANCH'"

# ---- one live binding ---------------------------------------------------------
# Adjudicated from the documented CLI, never from the supervisor's internal state:
# `~/.claude/daemon/roster.json` is mentioned, not contracted, and parsing it is the
# coupling class this project already refused. Parsing is fail-closed: unexpected
# output refuses the launch rather than assuming nobody is alive. Agent View is a
# research preview and its schema may change between releases.
live_named() {
  claude agents --json 2>/dev/null | python3 -c '
import json, sys
raw = sys.stdin.read().strip()
if not raw:
    sys.exit(3)                       # no output at all -> undecidable
try:
    rows = json.loads(raw)
except Exception:
    sys.exit(3)                       # unparseable -> undecidable
if not isinstance(rows, list):
    sys.exit(3)
want = sys.argv[1]
for row in rows:
    if not isinstance(row, dict):
        sys.exit(3)
    if row.get("name") == want and row.get("pid") is not None:
        print(row.get("sessionId") or "", row.get("pid"))
        sys.exit(0)                   # a live process carries this name
sys.exit(1)                           # parsed cleanly, nobody alive by that name
' "$ACTOR"
}

set +e
LIVE="$(live_named)"; LIVE_RC=$?
set -e
case "$LIVE_RC" in
  0) die ACTOR_ALREADY_LIVE "$ACTOR is already running ($LIVE)" ;;
  1) : ;;
  *) die ROSTER_UNREADABLE "claude agents --json gave no usable answer; refusing rather than assuming" ;;
esac

# ---- lineage ------------------------------------------------------------------
case "$MODE" in
  birth)
    [ -e "$LINEAGE_FILE" ] && \
      die LINEAGE_EXISTS "$ACTOR already has a canonical lineage on $RUNTIME_INSTANCE ($LINEAGE_FILE) — recover it, do not re-birth"
    ;;
  resume)
    [ -e "$LINEAGE_FILE" ] || \
      die LINEAGE_ABSENT "no lineage for $ACTOR on $RUNTIME_INSTANCE — a recovery cannot invent the session it recovers"
    ;;
  check)
    ;;
  *) die USAGE "unknown mode '$MODE'" ;;
esac

if [ "$MODE" = "check" ]; then
  printf 'PRECONDITIONS_PASS actor=%s worktree=%s branch=%s cell=%s lineage=%s\n' \
    "$ACTOR" "$WANT" "$BRANCH" "$RUNTIME_INSTANCE" \
    "$([ -e "$LINEAGE_FILE" ] && echo present || echo absent)"
  exit 0
fi

# ---- act ----------------------------------------------------------------------
if [ "$MODE" = "resume" ]; then
  SESSION_ID="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["session_id"])' "$LINEAGE_FILE")"
  printf 'RECOVERY actor=%s session=%s\n' "$ACTOR" "$SESSION_ID" >&2
  exec claude --resume "$SESSION_ID" --settings "$TRANSPORT" "$@"
fi

# BIRTH. Never `exec`: the launcher must outlive the launch to capture the session
# it created and persist the lineage. A birth that is not recorded is a birth that
# the next launcher call cannot refuse.
BIRTH_OUT="$(claude --name "$ACTOR" --bg --settings "$TRANSPORT" "$@" 2>&1)" || {
  printf '%s\n' "$BIRTH_OUT" >&2
  die BIRTH_FAILED "claude exited non-zero"
}
printf '%s\n' "$BIRTH_OUT"

# Adjudicate the created session from the roster rather than from the launch output:
# the short id is printed, but the sessionId is what `--resume` takes as a direct
# handle, and a name is only a label.
SESSION_ID="$(claude agents --json 2>/dev/null | python3 -c '
import json, sys
try:
    rows = json.loads(sys.stdin.read() or "[]")
except Exception:
    sys.exit(1)
hits = [r for r in rows if isinstance(r, dict) and r.get("name") == sys.argv[1] and r.get("sessionId")]
if len(hits) != 1:
    sys.exit(1)                       # zero, or ambiguous -> do not guess
print(hits[0]["sessionId"])
' "$ACTOR")" || die LINEAGE_UNRESOLVED "born, but the session could not be identified uniquely — record it by hand before any resume"

mkdir -p "$LINEAGE_DIR"
umask 077
python3 - "$LINEAGE_FILE" "$ACTOR" "$RUNTIME_INSTANCE" "$SESSION_ID" "$WANT" "$BRANCH" <<'PY'
import json, os, sys, time
path, actor, cell, session_id, worktree, branch = sys.argv[1:7]
tmp = path + ".tmp"
with open(tmp, "w") as fh:
    json.dump({
        "actor_id": actor,
        "runtime_instance": cell,
        "session_id": session_id,
        "worktree": worktree,
        "branch": branch,
        "born_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }, fh, indent=2, sort_keys=True)
    fh.write("\n")
os.replace(tmp, path)          # atomic: a half-written lineage would refuse every future launch
PY

printf 'BIRTH_PASS actor=%s session=%s cell=%s worktree=%s branch=%s\n' \
  "$ACTOR" "$SESSION_ID" "$RUNTIME_INSTANCE" "$WANT" "$BRANCH"
