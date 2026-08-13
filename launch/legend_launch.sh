#!/usr/bin/env bash
# legend_launch.sh — fail-closed birth and recovery for ONE LEGEND actor.
#
# MINIMUM RUNTIME KERNEL. Actor and worktree are PARAMETERS: this script holds no
# actor table, so the future registry supplies the same parameters from a versioned
# file without any logic here having to be dismantled.
#
# It governs BIRTH and ENVIRONMENT only. The supervisor governs the session's life,
# and LEGEND adds only the invariants Claude Code does not guarantee. The spec, with
# the measurement behind each one, is in KERNEL_SPEC.md beside this file:
#
#   IDENTITY IS COINED, NEVER DERIVED. `LEGEND_RUNTIME_INSTANCE` is required. This
#   machine answers to four names — `hostname -s` gives the router's, `scutil --get
#   LocalHostName` gives another — so a cell keyed on the hostname is keyed on which
#   network the laptop is on, and a change of network would empty the namespace and
#   make every actor re-birthable with nothing detecting it. Same reason the runtime
#   version is not part of the key.
#
#   --name is a LIVENESS requirement, not an identity. Measured 2026-08-12/13: three
#   different default names for one unchanged sessionId within 24 hours, on an
#   inconsistent base. It makes an actor findable; it is never a persistable address.
#
#   --settings is passed at EVERY process start. A normal resume does not restore
#   `--settings`, so the transport must be supplied by the launcher each time. The
#   guarantee is per-launch, not per-life: a manual `claude --resume` bypasses it.
#
#   ONE CANONICAL SESSION LINEAGE PER (actor_id, runtime_instance), and the record
#   that authorises the refusal is written BEFORE the act it guards. The lineage
#   store is PER-CELL and NOT versioned: a lineage that travelled with the repository
#   would refuse the first birth on a target host.
#
# Fail-closed here rather than in a hook because a SessionStart hook cannot block a
# session from starting; this is the boundary LEGEND chose, not the only one possible.
#
# Usage:
#   legend_launch.sh birth  <actor_id> <worktree_path> <branch> [extra claude args...]
#   legend_launch.sh resume <actor_id> <worktree_path> <branch> [extra claude args...]
#   legend_launch.sh check  <actor_id> <worktree_path> <branch>
#
# `check` DIAGNOSES: it evaluates every precondition and reports one line each,
# exiting non-zero if any failed. `birth` and `resume` ACT, and stay fail-closed at
# the first refusal. The asymmetry is deliberate — a diagnostic that stops at the
# first problem cannot diagnose the second, which is exactly what happened when the
# version gate made `check` useless for everything behind it.

set -euo pipefail

CERTIFIED_VERSION="${LEGEND_CERTIFIED_VERSION:-2.1.228}"
RUNTIME_INSTANCE="${LEGEND_RUNTIME_INSTANCE:-}"
LINEAGE_BASE="${LEGEND_LINEAGE_DIR:-$HOME/.legend/lineage}"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
TRANSPORT="${LEGEND_TRANSPORT_SETTINGS:-$SCRIPT_DIR/transport.json}"

[ $# -ge 4 ] || {
  printf 'LAUNCH_REFUSED USAGE: mode, actor_id, worktree and branch are all required\n' >&2
  exit 1
}
MODE="$1"; ACTOR="$2"; WORKTREE="$3"; BRANCH="$4"; shift 4

case "$MODE" in
  birth|resume|check) : ;;
  *) printf "LAUNCH_REFUSED USAGE: unknown mode '%s'\n" "$MODE" >&2; exit 1 ;;
esac

FAILURES=0

# In an acting mode a refusal is terminal. In `check` it is one reported line and the
# run continues, so that a single invocation answers every question at once.
refuse() {
  if [ "$MODE" = check ]; then
    printf 'CHECK_FAIL  %-28s %s\n' "$1" "$2"
    FAILURES=$((FAILURES + 1))
    return 0
  fi
  printf 'LAUNCH_REFUSED %s: %s\n' "$1" "$2" >&2
  exit 1
}
ok()   { [ "$MODE" = check ] && printf 'CHECK_PASS  %-28s %s\n' "$1" "$2"; return 0; }
info() { [ "$MODE" = check ] && printf 'CHECK_INFO  %-28s %s\n' "$1" "$2"; return 0; }
skip() { [ "$MODE" = check ] && printf 'CHECK_SKIP  %-28s %s\n' "$1" "$2"; return 0; }

# ---- transport ----------------------------------------------------------------
if [ -f "$TRANSPORT" ]; then
  ok TRANSPORT "$TRANSPORT"
else
  refuse TRANSPORT_MISSING "$TRANSPORT"
fi

# ---- cell identity ------------------------------------------------------------
# Checked before the runtime gate: a cell identity that is wrong or absent is wrong
# on a qualified host too, and the operator should hear about it either way.
CELL_DIR=""
LINEAGE_FILE=""
if [ -n "$RUNTIME_INSTANCE" ]; then
  ok RUNTIME_INSTANCE "$RUNTIME_INSTANCE"
  CELL_DIR="$LINEAGE_BASE/$RUNTIME_INSTANCE"
  if [ -d "$CELL_DIR" ]; then
    ok CELL "$CELL_DIR"
    LINEAGE_FILE="$CELL_DIR/$ACTOR.json"
  else
    refuse CELL_UNKNOWN "no cell '$RUNTIME_INSTANCE' at $CELL_DIR — create it deliberately (mkdir -p $CELL_DIR) before the first birth on this cell"
    CELL_DIR=""
  fi
else
  refuse RUNTIME_INSTANCE_UNDECLARED "LEGEND_RUNTIME_INSTANCE must be set explicitly — it is the cell identity and must never be derived from the network"
  skip CELL "runtime instance undeclared"
fi

# ---- host runtime -------------------------------------------------------------
# Still evaluated before every location and lineage check, so an unqualified host
# leaves no residue. Moving this constant requires an argued commit: see MC-2.
HAVE_VERSION="$(claude --version 2>/dev/null | awk '{print $1}')"
if [ "$HAVE_VERSION" = "$CERTIFIED_VERSION" ]; then
  ok HOST_RUNTIME "claude $HAVE_VERSION"
else
  refuse HOST_RUNTIME_UNQUALIFIED "claude $HAVE_VERSION != certified $CERTIFIED_VERSION"
fi

# ---- location, checked from INSIDE the worktree -------------------------------
# There is no `cwd` check here. The old one compared `pwd -P` after `cd` against the
# same path resolved the same way: it could not fail, and a control that cannot fail
# still prints a reassuring line. The top-level comparison below is the real one.
WANT=""
if [ -d "$WORKTREE" ]; then
  cd -- "$WORKTREE"
  WANT="$(pwd -P)"
  ok WORKTREE "$WANT"

  TOPLEVEL="$(git rev-parse --show-toplevel 2>/dev/null || true)"
  if [ "$TOPLEVEL" = "$WANT" ]; then
    ok TOPLEVEL "$TOPLEVEL"
  else
    refuse TOPLEVEL_MISMATCH "${TOPLEVEL:-<not a git worktree>} != $WANT"
  fi

  HAVE_BRANCH="$(git branch --show-current 2>/dev/null || true)"
  if [ "$HAVE_BRANCH" = "$BRANCH" ]; then
    ok BRANCH "$HAVE_BRANCH"
  else
    refuse BRANCH_MISMATCH "on '${HAVE_BRANCH:-<detached or absent>}', expected '$BRANCH'"
  fi
else
  refuse WORKTREE_ABSENT "$WORKTREE"
  skip TOPLEVEL "worktree absent"
  skip BRANCH "worktree absent"
fi

# ---- one live binding ---------------------------------------------------------
# Adjudicated from the documented CLI, never from the supervisor's internal state:
# `~/.claude/daemon/roster.json` is mentioned, not contracted, and parsing it is the
# coupling class this project already refused. Parsing is fail-closed: unexpected
# output refuses the launch rather than assuming nobody is alive. Agent View is a
# research preview and its schema may change between releases — which is why the
# recertification checklist names this parse first.
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
  0) refuse ACTOR_ALREADY_LIVE "$ACTOR is already running ($LIVE)" ;;
  1) ok ACTOR_NOT_LIVE "$ACTOR" ;;
  *) refuse ROSTER_UNREADABLE "claude agents --json gave no usable answer; refusing rather than assuming" ;;
esac

# ---- lineage ------------------------------------------------------------------
# One decision function, three consumers: `check` reports the state and what each
# acting mode would do with it, `birth` and `resume` act on the same verdict. The
# reported line IS the decision, not a simulation of it.
#
# Legacy shape: the previous kernel wrote a record only after resolving a session id,
# so a record carrying one is ACTIVE. `state` is authoritative when present.
# Prints exactly two lines — state, then detail — rather than one delimited line:
# a separator that is invisible in a diff is a defect waiting for someone to
# reformat the file.
read_lineage() {
  python3 -c '
import json, os, sys

def out(state, detail=""):
    print(state)
    print(detail)
    raise SystemExit

path = sys.argv[1]
if not os.path.exists(path):
    out("ABSENT")
try:
    rec = json.load(open(path))
    if not isinstance(rec, dict):
        raise ValueError
except Exception:
    out("UNREADABLE", "not a JSON object")
state = rec.get("state")
sid = (rec.get("session_id") or "").strip()
if state not in ("PENDING_BIRTH", "ACTIVE"):
    state = "ACTIVE" if sid else "PENDING_BIRTH"
if state == "ACTIVE":
    if not sid:
        out("UNREADABLE", "ACTIVE without a session id")
    out("ACTIVE", sid)
ann = rec.get("annotation")
if ann:
    out("PENDING_ANNOTATED", json.dumps(ann, sort_keys=True))
out("PENDING_BARE")
' "$1"
}

RESERVED_BARE_TEXT="a previous birth did not complete before spawning. This record holds no session id, so deleting it is safe. An ACTIVE record is not: never delete one."

if [ -n "$LINEAGE_FILE" ]; then
  LINEAGE_RAW="$(read_lineage "$LINEAGE_FILE")"
  LINEAGE_STATE="$(printf '%s\n' "$LINEAGE_RAW" | sed -n 1p)"
  LINEAGE_DETAIL="$(printf '%s\n' "$LINEAGE_RAW" | sed -n 2p)"

  case "$MODE" in
    check)
      info LINEAGE "$LINEAGE_STATE ${LINEAGE_DETAIL}"
      case "$LINEAGE_STATE" in
        ABSENT)            info LINEAGE_VERDICT "birth would proceed · resume would refuse LINEAGE_ABSENT" ;;
        ACTIVE)            info LINEAGE_VERDICT "birth would refuse LINEAGE_EXISTS · resume would proceed" ;;
        PENDING_BARE)      info LINEAGE_VERDICT "birth would refuse LINEAGE_RESERVED (bare) · resume would refuse LINEAGE_UNBOUND" ;;
        PENDING_ANNOTATED) info LINEAGE_VERDICT "birth would refuse LINEAGE_RESERVED (annotated) · resume would refuse LINEAGE_UNBOUND" ;;
        UNREADABLE)        info LINEAGE_VERDICT "birth and resume would both refuse LINEAGE_UNREADABLE" ;;
      esac
      ;;
    birth)
      case "$LINEAGE_STATE" in
        ABSENT) : ;;
        ACTIVE)
          refuse LINEAGE_EXISTS "$ACTOR already has a canonical lineage on $RUNTIME_INSTANCE ($LINEAGE_FILE, session $LINEAGE_DETAIL) — recover it, do not re-birth" ;;
        PENDING_BARE)
          refuse LINEAGE_RESERVED "$ACTOR has a PENDING_BIRTH record on $RUNTIME_INSTANCE ($LINEAGE_FILE). bare — $RESERVED_BARE_TEXT" ;;
        PENDING_ANNOTATED)
          refuse LINEAGE_RESERVED "$ACTOR has a PENDING_BIRTH record on $RUNTIME_INSTANCE ($LINEAGE_FILE). annotated — a session may exist: $LINEAGE_DETAIL. Check \`claude agents --json\` and the transcript store BEFORE removing this record: it is the only pointer to it." ;;
        UNREADABLE)
          refuse LINEAGE_UNREADABLE "$LINEAGE_FILE cannot be interpreted ($LINEAGE_DETAIL) — resolve it by hand; refusing rather than overwriting a record that may point at a session" ;;
      esac
      ;;
    resume)
      case "$LINEAGE_STATE" in
        ACTIVE) SESSION_ID="$LINEAGE_DETAIL" ;;
        ABSENT)
          refuse LINEAGE_ABSENT "no lineage for $ACTOR on $RUNTIME_INSTANCE — a recovery cannot invent the session it recovers" ;;
        PENDING_BARE|PENDING_ANNOTATED)
          refuse LINEAGE_UNBOUND "$ACTOR's lineage is PENDING_BIRTH — there is no session id to resume" ;;
        UNREADABLE)
          refuse LINEAGE_UNREADABLE "$LINEAGE_FILE cannot be interpreted ($LINEAGE_DETAIL) — resolve it by hand" ;;
      esac
      ;;
  esac
else
  skip LINEAGE "no cell to look in"
fi

if [ "$MODE" = check ]; then
  if [ "$FAILURES" -eq 0 ]; then
    printf 'PRECONDITIONS_PASS actor=%s worktree=%s branch=%s cell=%s\n' \
      "$ACTOR" "${WANT:-$WORKTREE}" "$BRANCH" "${RUNTIME_INSTANCE:-<undeclared>}"
    exit 0
  fi
  printf 'PRECONDITIONS_FAIL actor=%s failures=%d\n' "$ACTOR" "$FAILURES"
  exit 1
fi

# ---- act ----------------------------------------------------------------------
if [ "$MODE" = resume ]; then
  printf 'RECOVERY actor=%s session=%s\n' "$ACTOR" "$SESSION_ID" >&2
  exec claude --resume "$SESSION_ID" --settings "$TRANSPORT" "$@"
fi

# BIRTH, in two phases.
#
# Phase 1 reserves the lineage with O_EXCL BEFORE anything irreversible happens. The
# old kernel tested `[ -e ]` here and wrote the record on the far side of the spawn,
# so a crash in between left a live session with no record — a state in which resume
# is refused and a second birth is PERMITTED. The liveness check covered that only
# while the first session lived, and sessions die. O_EXCL also closes the concurrent
# -birth race that a `[ -e ]` test cannot.
python3 - "$LINEAGE_FILE" "$ACTOR" "$RUNTIME_INSTANCE" "$WANT" "$BRANCH" <<'PY' || {
import json, os, sys, time
path, actor, cell, worktree, branch = sys.argv[1:6]
rec = {
    "actor_id": actor,
    "runtime_instance": cell,
    "state": "PENDING_BIRTH",
    "worktree": worktree,
    "branch": branch,
    "reserved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "reserved_by_pid": os.getppid(),
}
fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
with os.fdopen(fd, "w") as fh:
    json.dump(rec, fh, indent=2, sort_keys=True)
    fh.write("\n")
PY
  printf 'LAUNCH_REFUSED LINEAGE_RESERVED: could not reserve %s — another birth of %s may be in flight\n' \
    "$LINEAGE_FILE" "$ACTOR" >&2
  exit 1
}

# Phase 2 spawns. From here on the reservation exists, so every exit path below must
# either complete it or annotate it: an unannotated reservation left after a spawn
# would tell the next operator that deleting it is safe, when it is the only pointer
# to a session that exists.
annotate() {
  python3 - "$LINEAGE_FILE" "$1" "$2" <<'PY'
import json, os, sys, time
path, reason, evidence = sys.argv[1:4]
rec = json.load(open(path))
rec["annotation"] = {
    "reason": reason,
    "spawn_evidence": evidence[:400],
    "annotated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}
tmp = path + ".tmp"
with open(tmp, "w") as fh:
    json.dump(rec, fh, indent=2, sort_keys=True)
    fh.write("\n")
os.replace(tmp, path)
PY
}

set +e
BIRTH_OUT="$(claude --name "$ACTOR" --bg --settings "$TRANSPORT" "$@" 2>&1)"
BIRTH_RC=$?
set -e

if [ "$BIRTH_RC" -ne 0 ]; then
  # Nothing was spawned, so the reservation stays bare and is safe to remove. Remove
  # it here rather than leaving the operator to reason about it.
  rm -f -- "$LINEAGE_FILE"
  printf '%s\n' "$BIRTH_OUT" >&2
  printf 'LAUNCH_REFUSED BIRTH_FAILED: claude exited %d; the bare reservation was withdrawn\n' "$BIRTH_RC" >&2
  exit 1
fi
printf '%s\n' "$BIRTH_OUT"

# Adjudicate the created session from the roster rather than from the launch output:
# the short id is printed, but the sessionId is what `--resume` takes as a direct
# handle, and a name is only a label. The launch output is kept verbatim as spawn
# evidence rather than parsed — an unverified parse of an uncontracted format is the
# exact coupling the recertification checklist exists to re-test.
set +e
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
' "$ACTOR")"
RESOLVE_RC=$?
set -e

if [ "$RESOLVE_RC" -ne 0 ] || [ -z "$SESSION_ID" ]; then
  annotate "session spawned; the roster did not resolve a unique sessionId" "$BIRTH_OUT"
  printf 'LAUNCH_REFUSED LINEAGE_UNRESOLVED: %s was born but its session could not be identified uniquely. The reservation at %s has been ANNOTATED and is now the only pointer to that session — do not delete it blindly; find the session and complete the record by hand.\n' \
    "$ACTOR" "$LINEAGE_FILE" >&2
  exit 1
fi

# Complete the reservation. `os.replace` is atomic: a half-written lineage would
# refuse every future launch.
python3 - "$LINEAGE_FILE" "$SESSION_ID" <<'PY'
import json, os, sys, time
path, session_id = sys.argv[1:3]
rec = json.load(open(path))
rec["state"] = "ACTIVE"
rec["session_id"] = session_id
rec["born_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
rec.pop("reserved_by_pid", None)
tmp = path + ".tmp"
with open(tmp, "w") as fh:
    json.dump(rec, fh, indent=2, sort_keys=True)
    fh.write("\n")
os.replace(tmp, path)
PY

printf 'BIRTH_PASS actor=%s session=%s cell=%s worktree=%s branch=%s\n' \
  "$ACTOR" "$SESSION_ID" "$RUNTIME_INSTANCE" "$WANT" "$BRANCH"
