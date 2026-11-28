#!/usr/bin/env python3
"""Hourly watch over an actor's open mandate: is the authorised work running, and if it
stopped while work remains, ask the bound session to continue.

    python3 framework/scripts/mandate_watch.py check --task ORCH-ROADMAP-IT4-20261028
    python3 framework/scripts/mandate_watch.py check --task <ID> --deliver none --json
    python3 framework/scripts/mandate_watch.py events [--last N]
    python3 framework/scripts/mandate_watch.py route --to ADV [--to HE --first-line "IT to ADV and HE: ..."]
    python3 framework/scripts/mandate_watch.py handoff --task <ID> --old <old session id> --new <successor id> [--within 5] [--wait 600]   # after a restart: released, bound, first tool call?

One control, two triggers, no new coordinator:

* the host crontab runs `check --deliver resume` hourly. If the bound session has no live
  process at all, it is revived under the SAME session id with `claude --bg --resume <id>`
  (a supported Claude Code command); a session that is alive is never "resumed" this way,
  because the CLI would start a copy of it.
* the live Orchestrator session arms ONE in-session cron (`CronCreate`, hourly) whose prompt
  is "run `check --self-call`, and if it says RESUME, continue". The runtime enqueues a
  session cron only while the session is idle, so an active turn is never interrupted, and the
  enqueued prompt is delivered by the runtime itself, not by writing to a conversation store.

State machine (derived from the mandate record, `claude agents --json`, and activity):

  RUNNING            the session is busy, or its transcript / background tasks changed within
                     --quiet-minutes. Waiting for a subagent is running, not stopped.
                     The transcript's mtime counts only up to its last real turn (a timestamped
                     user or assistant entry): runtime metadata appended to the tail is not
                     progress, whether the session is absent from the listing or listed idle
                     (ADV-206, 2026-11-24). A busy session and a live job are decided first.
  STOPPED_RESUMABLE  record verdict CONTINUE, session idle (or dead) for longer than
                     --quiet-minutes, and no request pending for the current queue state.
  PAUSED / COMPLETE  the record releases the mandate (MANDATE_STATE PAUSED / CANCELLED /
                     COMPLETE, or every step DONE). Never restarted.
  BLOCKED            ALL_BLOCKED: the cause is kept in the log; independent steps would already
                     make the verdict CONTINUE, so they are not held back by a blocked one.
  UNKNOWN            no bound session found, the session list is unreadable, or the record is
                     malformed. Nothing is started on a hypothesis; the limit is logged.

Background work is judged by its own process, never by output recency: start a long job with
`mandate_watch.py job run --task <ID> --label <label> -- <command>` (detached, tagged with
LEGEND_MANDATE_JOB, exit status recorded, idempotent per label so a resume request cannot start
the same work twice). A live job keeps the mandate RUNNING even if it prints nothing; a finished
job not yet collected, or a job that DIED without an exit status, is reported in the restart
request (`job list`, `job collect`). A mandate whose record says COMPLETE is not complete while
the commit that closed it is missing from the development remote: the watch asks again.
Subagents run inside the session, so only the live session can see them: the in-session cron
prompt tells the session to call ListAgents and to treat any running subagent as RUNNING.
Trust: reviving a dead session with `claude --bg --resume` needs the CLI workspace trust of this
repository, which only the operator can give: run `claude` once in the repository directory and
accept the trust dialog. The watch never edits the global trust configuration.
The absence of recent commits proves nothing about stopped work and is never read.
Identity comes from the record and from the session's own `MANDATE_BOUND: <TASK_ID>` line
(mandate_continuity.py), never from a directory or a process name. The marker must START its line in
the session's own text; the same words after a prefix in a sentence bind nothing (measured 2026-10-29).
What this does NOT guarantee: that the resumed model chooses well, quota, or a session whose
host is powered off.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import os
import shlex
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mandate_continuity as mc  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
QUIET_MINUTES = 25            # idle and silent for this long before a session counts as stopped
REREQUEST_MINUTES = 180       # a pending request with no progress is repeated no sooner than this, while the session it went to is live
STARTUP_GRACE_MINUTES = 10    # a revival that was just sent is not repeated while the revived session may still be starting
EVENTS_FILE = "events.jsonl"
EVENTS_MAX_BYTES = 256 * 1024
_SESSIONS_UNSET = object()


def claude_bin() -> str:
    """cron runs with a minimal PATH, so `claude` (installed under ~/.local/bin) is not found by name."""
    return shutil.which("claude") or os.path.expanduser("~/.local/bin/claude")


def state_dir() -> Path:
    base = os.environ.get("LEGEND_MANDATE_WATCH_STATE") or os.path.join(
        os.environ.get("XDG_STATE_HOME", os.path.expanduser("~/.local/state")), "legend", "mandate_watch")
    return Path(base)


def log_event(kind: str, **fields) -> None:
    try:
        d = state_dir()
        d.mkdir(parents=True, exist_ok=True)
        p = d / EVENTS_FILE
        if p.exists() and p.stat().st_size > EVENTS_MAX_BYTES:
            p.replace(d / (EVENTS_FILE + ".1"))
        entry = {"at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "kind": kind, **fields}
        with p.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, sort_keys=True) + "\n")
    except OSError:
        pass


def _load(task: str) -> dict:
    p = state_dir() / f"{task}.json"
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _save(task: str, data: dict) -> None:
    try:
        d = state_dir()
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{task}.json").write_text(json.dumps(data, indent=1, sort_keys=True), encoding="utf-8")
    except OSError:
        pass


# ---------------------------------------------------------------- observations
def session_is_live(entry: dict) -> bool:
    """Is the process of this listing entry running? `claude agents --json` keeps a session that was killed or stopped in its list, WITHOUT a pid
    and without a status (measured 2026-11-18 with a scratch session: after `claude stop` and after a kill the entry stayed, 'state: working'), so an
    entry in the list is not a live session. An entry is live when it names a pid and /proc/<pid> holds a process that is not a zombie."""
    pid = entry.get("pid")
    if isinstance(pid, str) and pid.isdigit():
        pid = int(pid)
    if not isinstance(pid, int) or pid <= 0:
        return False
    return _proc_state(pid) not in (None, "Z")


def list_sessions() -> list[dict] | None:
    """Live sessions from the runtime's own listing (entries whose process is not running are dropped); None when the listing cannot be read."""
    try:
        out = subprocess.run([claude_bin(), "agents", "--json"], capture_output=True, text=True, timeout=60)
        data = json.loads(out.stdout)
        return [x for x in data if isinstance(x, dict) and session_is_live(x)] if isinstance(data, list) else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def session_name_inventory() -> list[dict] | None:
    """Names include stopped sessions: stopping a host does not rename its old row."""
    try:
        result = subprocess.run([claude_bin(), "agents", "--all", "--json"],
                                capture_output=True, text=True, timeout=60)
        data = json.loads(result.stdout) if result.returncode == 0 else None
        return [row for row in data if isinstance(row, dict)] if isinstance(data, list) else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def session_name_state(task: str, sessions: list[dict] | None, inventory: list[dict] | None = None,
                       projects_dir: Path | None = None) -> dict:
    """Read-only naming plan. Binding elects the host; CURRENT never elects anything.

    Native rename remains the launcher's action. No transcript/job store writes,
    model launch, process stop or scientific gate is hidden in this observation.
    """
    out = {"task": task, "state": "UNKNOWN", "renames": []}
    hosts = live_bound_sessions(task, sessions, projects_dir)
    if sessions is None or len(hosts) != 1:
        return dict(out, reason="need one verified live bound host; names and timestamps do not choose it")
    sid = hosts[0]["session_id"]
    path = transcript_for_session(sid, projects_dir)
    timeline = bind_timeline(path, task) if path else {}
    if not timeline.get("tool_calls_after_bind"):
        return dict(out, reason="bound successor has not acted; do not promote its display name")
    rows = session_name_inventory() if inventory is None else inventory
    if rows is None:
        return dict(out, reason="complete runtime name inventory unavailable")
    current = [row for row in rows if row.get("sessionId") == sid]
    if len(current) != 1 or not isinstance(current[0].get("name"), str) or not current[0]["name"].strip():
        return dict(out, reason="current host name missing or ambiguous")
    role = re.split(r"\s+-\s+(?:CURRENT|PREVIOUS|CANDIDATE)\b", current[0]["name"],
                    maxsplit=1, flags=re.I)[0].strip()
    if not role:
        return dict(out, reason="no display role; do not invent one")
    plan = []
    for row in rows:
        old_id, name = row.get("sessionId"), row.get("name")
        if (old_id == sid or not isinstance(old_id, str) or not UUID_RE.fullmatch(old_id)
                or not isinstance(name, str) or not re.search(r"\bCURRENT\b", name)):
            continue
        old = transcript_for_session(old_id, projects_dir)
        released = bind_timeline(old, task) if old is not None and cached_binding(old) is None else {}
        if released.get("state") == "RELEASED" and released.get("active_tasks") == []:
            plan.append({"session_id": old_id, "from": name,
                         "to": f"{role} - PREVIOUS {old_id[:8]}"})
    expected = f"{role} - CURRENT {sid[:8]}"
    if current[0]["name"] != expected:
        plan.append({"session_id": sid, "from": current[0]["name"], "to": expected})
    return dict(out, state="PENDING" if plan else "CURRENT", current_session=sid, renames=plan,
                next="Native rename by exact session id, demotions before promotion; verify --all names. No model launch or history deletion.")


# ---------------------------------------------------------------- routing: who a message really goes to
UUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I)
TO_LINE = re.compile(r"^\s*[\w .-]+?\s+to\s+(?P<who>[^:\n(]+?)\s*(?:\((?P<cc>[^)]*)\))?\s*[:\u2014\n]", re.I)


def _tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", (text or "").lower()) if t}


def declared_recipients(first_line: str) -> list[str]:
    """The recipients a message's own first line names ("IT to ADV and HE: ...", "(cc SCI)"). A name in a text is a claim about the recipients, not an address."""
    m = TO_LINE.match((first_line or "").strip() + "\n")
    if not m:
        return []
    names = re.split(r"\s*(?:,|&|\+|/|\band\b)\s*", m.group("who"))
    cc = re.sub(r"^\s*cc\s*", "", m.group("cc") or "", flags=re.I)
    names += [n for n in re.split(r"\s*(?:,|&|\+|/|\band\b)\s*", cc) if n]
    return [n.strip() for n in names if n.strip()]


def route(target: str, sessions: list[dict] | None, root: Path = ROOT) -> dict:
    """Resolve a name, a role alias ("ADV", "IT") or a session id to ONE live session, from the runtime's own listing and from the SESSION_NAME / SESSION_BINDING of the task records.
    Never falls back to the last conversation's address: an unresolved or ambiguous target is reported as such, with the candidates."""
    out = {"target": target, "status": "UNRESOLVED", "recipient": None, "session_id": None, "via": None, "candidates": []}
    if sessions is None:
        out["why"] = "the session listing could not be read"
        return out
    live = {str(x.get("sessionId")): x for x in sessions if x.get("sessionId")}
    want = _tokens(target)
    found: dict[str, str] = {}
    for sid, x in live.items():                                                      # 1 the runtime's own name, whole name or whole-word alias; or a session id
        name = str(x.get("name") or "")
        if target.strip().lower() == name.lower() or (len(target.strip()) >= 6 and sid.startswith(target.strip().lower())):
            found.setdefault(sid, "live name or id")
        elif want and want <= _tokens(name):
            found.setdefault(sid, "live name token")
    bound_gone = []
    bound_live: dict[str, str] = {}
    for path in sorted((root / "ledger" / "tasks").glob("*/*.json")):                # 2 the binding a record states for the session that holds the role
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(rec, dict) or not want or not want <= _tokens(str(rec.get("SESSION_NAME") or "")):
            continue
        for host in live_bound_sessions(str(rec.get("TASK_ID")), list(live.values())):      # the live session that carries the marker of a record this role owns, whatever its display name is now
            found.setdefault(host["session_id"], f"MANDATE_BOUND of {rec.get('TASK_ID')}")
            bound_live.setdefault(host["session_id"], str(rec.get("TASK_ID")))
        bind = rec.get("SESSION_BINDING")
        sid = (bind.get("session_id") if isinstance(bind, dict) else (UUID_RE.search(str(bind or "")) or [None])[0]) if bind else None
        if sid and sid in live:
            found.setdefault(sid, f"binding of {rec.get('TASK_ID')}")
            bound_live.setdefault(sid, str(rec.get("TASK_ID")))
        elif sid:
            bound_gone.append({"task": rec.get("TASK_ID"), "session_id": sid})
    actor_hits: set[str] = set()
    actor = target.strip().lower()                                                   # 3 an ACTOR_ID as the recipient ("advisor", "orchestrator"): the live sessions bound to an OPEN record of that actor
    if re.fullmatch(r"[a-z][a-z0-9-]*", actor):
        for path in sorted((root / "ledger" / "tasks").glob("*/*.json")):
            try:
                rec = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(rec, dict) or str(rec.get("ACTOR_ID") or "").lower() != actor:
                    continue
                if "OPEN" not in [mc.block_state(b) for _, b in mc.load_blocks(rec)]:
                    continue
            except (OSError, ValueError, mc.Malformed, AttributeError):
                continue
            task = str(rec.get("TASK_ID") or path.stem)
            hosts = {h["session_id"] for h in live_bound_sessions(task, list(live.values()))}
            bind = rec.get("SESSION_BINDING")
            sid = (bind.get("session_id") if isinstance(bind, dict) else (UUID_RE.search(str(bind or "")) or [None])[0]) if bind else None
            if sid and sid in live:
                hosts.add(sid)
            for h in hosts:
                found.setdefault(h, f"ACTOR_ID {actor}: binding of {task}")
                bound_live.setdefault(h, task)
                actor_hits.add(h)
    out["candidates"] = [{"recipient": live[sid].get("name"), "session_id": sid, "via": why} for sid, why in found.items()]
    # 2026-11-18: two live sessions answered to 'ADV' (the bound session and an operator chat named after the mandate) and 'HE' matched 'HE-PROBE' by token. A whole-name match beats a token match, and when several
    # names still answer, the session a record's SESSION_BINDING names for that role is the one; the others are listed as surplus, never chosen and never silently dropped.
    bound = [sid for sid in found if sid in bound_live]
    if len(found) > 1 and len(bound) == 1 and not actor_hits:                        # (not for an ACTOR_ID alias: a name-token session that no record binds is another candidate, not a surplus duplicate) identity follows the binding (record or marker), not the display name
        out["surplus_name_matches"] = [{"recipient": live[sid].get("name"), "session_id": sid} for sid in found if sid not in bound]
        found = {bound[0]: f"binding of {bound_live[bound[0]]} (the other live sessions that answer to the name are not its host)"}
    if len(found) > 1 and not actor_hits and len(bound) != 1:
        # 2026-11-19 (ADV-078 trial, measured): a fresh window of a record that carries no SESSION_NAME left two live sessions named SCI and route said AMBIGUOUS although only one of them held the mandate:
        # the old session had written MANDATE_RELEASED. Identity follows the marker: among the same-name sessions, the one that is the live marker-host of an OPEN record is the target.
        hosts = {}
        for path in sorted((root / "ledger" / "tasks").glob("*/*.json")):
            try:
                rec = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(rec, dict) or "OPEN" not in [mc.block_state(b) for _, b in mc.load_blocks(rec)]:
                    continue
            except (OSError, ValueError, mc.Malformed, AttributeError):
                continue
            task = str(rec.get("TASK_ID") or path.stem)
            for h in live_bound_sessions(task, [live[sid] for sid in found]):
                hosts.setdefault(h["session_id"], task)
        if len(hosts) == 1:
            host = next(iter(hosts))
            out["surplus_name_matches"] = [{"recipient": live[sid].get("name"), "session_id": sid} for sid in found if sid != host]
            found = {host: f"MANDATE_BOUND of {hosts[host]} (the other live sessions that answer to the name are not hosts of an open record)"}
    exact = [sid for sid in found if found[sid] == "live name or id"]
    if len(found) > 1 and exact and len(exact) < len(found):
        out["surplus_token_matches"] = [{"recipient": live[sid].get("name"), "session_id": sid} for sid in found if sid not in exact]
        found = {sid: found[sid] for sid in exact}
    if len(found) == 1:
        sid = next(iter(found))
        out.update(status="RESOLVED", recipient=live[sid].get("name"), session_id=sid, via=found[sid])
    elif len(found) > 1:
        out.update(status="AMBIGUOUS", why="more than one live session answers to this name or role; none is chosen")
    else:
        out["why"] = ("the session a record binds to this role is not live under that id" if bound_gone else "no live session and no record binding answers to it")
        out["bound_not_live"] = bound_gone
    return out


def check_recipients(first_line: str, used: list[str], sessions: list[dict] | None, root: Path = ROOT) -> dict:
    """Compare who a message SAYS it is for with who it was actually sent to. `used` are the recipients of the real sends (one per send: the tool takes one `to`).
    Verdict OK only when every declared recipient resolves to a session that was a real target and every real target was declared or is a stated copy."""
    declared = declared_recipients(first_line)
    decl = {d: route(d, sessions, root) for d in declared}
    real = {u: route(u, sessions, root) for u in used}
    real_ids = {r["session_id"] for r in real.values() if r["status"] == "RESOLVED"}
    decl_ids = {r["session_id"] for r in decl.values() if r["status"] == "RESOLVED"}
    missing = [d for d, r in decl.items() if r["status"] == "RESOLVED" and r["session_id"] not in real_ids]
    unresolved = [d for d, r in decl.items() if r["status"] != "RESOLVED"] + [u for u, r in real.items() if r["status"] != "RESOLVED"]
    stray = [u for u, r in real.items() if r["status"] == "RESOLVED" and decl_ids and r["session_id"] not in decl_ids]
    ok = bool(declared) and not missing and not unresolved and not stray
    return {"verdict": "OK" if ok else ("NO_DECLARED_RECIPIENT" if not declared else "MISMATCH"), "declared": declared, "used": used,
            "missing_send_to": missing, "unresolved_or_ambiguous": unresolved, "sent_to_undeclared": stray,
            "note": "a send is accepted when the transport says so; it is read when the recipient answers or acts; it is taken in charge when its record says so"}



_BIND_CACHE: dict[tuple[str, float, int], str | None] = {}


def cached_binding(path: Path) -> str | None:
    """`mc.binding_from_transcript`, once per (file, mtime, size) in this process: a transcript of tens of megabytes was read again for every task of an `--all` run (the hourly check took about
    four minutes of which nearly all was re-reading the same files)."""
    try:
        st = path.stat()
    except OSError:
        return None
    key = (str(path), st.st_mtime, st.st_size)
    if key not in _BIND_CACHE:
        _BIND_CACHE[key] = mc.binding_from_transcript(path)
    return _BIND_CACHE[key]


def transcript_for_session(session_id: str, projects_dir: Path | None = None) -> Path | None:
    """The transcript file of a session id (one file per id under ~/.claude/projects/<cwd>/), or None."""
    base = projects_dir or Path(os.path.expanduser("~/.claude/projects"))
    try:
        exact = next(iter(base.glob(f"*/{session_id}.jsonl")), None)
        if exact or len(session_id) < 8 or "/" in session_id:
            return exact
        found = {f.stem: f for f in base.glob(f"*/{session_id}*.jsonl")}     # a unique prefix of at least 8 characters (2026-11-19: a short id answered MISSING for 10 minutes of waiting)
        return next(iter(found.values())) if len(found) == 1 else None
    except OSError:
        return None


def bind_timeline(path: Path, task: str) -> dict:
    """Where a session stands on ONE task, from its own transcript: the state of the last marker line, when the current BOUND was written, and whether any tool call came after it. 2026-11-20 (operator's
    morning continuation): the SCI successor of checkpoint L wrote its bind line as a text-only message, the turn ended, and it sat 41 minutes waiting for a message that went to its predecessor. A bind line
    written in the SAME response as a tool call is found at once and the turn goes on (probe 2026-11-20 07:25Z); this reads the difference from the transcript, not from the recipient's word."""
    out = {"state": "NEVER_BOUND", "bound_at": None, "released_at": None, "tool_calls_after_bind": 0, "first_action_at": None, "last_action_at": None, "last_write": None}
    active = set()
    try:
        with path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(entry, dict):
                    continue
                stamp = entry.get("timestamp")
                if isinstance(stamp, str):
                    out["last_write"] = stamp
                for text in mc._text_blocks(entry):
                    for kind, t in mc.MARKER_RE.findall(mc._outside_fences(text)):
                        if kind == "BOUND":
                            active.add(t)
                        else:
                            active.discard(t)
                        if t == task:
                            out["state"] = "BOUND" if kind == "BOUND" else "RELEASED"
                            out["bound_at" if kind == "BOUND" else "released_at"] = stamp
                            if kind == "BOUND":
                                out["tool_calls_after_bind"] = 0
                                out["first_action_at"] = None
                                out["last_action_at"] = None
                content = (entry.get("message") or {}).get("content") if entry.get("type") == "assistant" and not entry.get("isSidechain") else None
                if out["state"] == "BOUND" and isinstance(content, list):
                    calls = sum(1 for b in content if isinstance(b, dict) and b.get("type") == "tool_use")
                    out["tool_calls_after_bind"] += calls
                    if calls and out["first_action_at"] is None:
                        out["first_action_at"] = stamp
                    if calls:
                        out["last_action_at"] = stamp
    except OSError:
        return {"state": "MISSING", "bound_at": None, "released_at": None, "tool_calls_after_bind": 0, "last_write": None}
    out["active_tasks"] = sorted(active)
    return out


def _age_min(stamp: str | None, now: datetime) -> int | None:
    try:
        return round((now - datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))).total_seconds() / 60)
    except (TypeError, ValueError):
        return None


def _assistant_turns_after(path: Path | None, stamp: str | None) -> int:
    """Assistant entries of the session itself (not its sub-agents) written after `stamp`: how much a successor has done since the predecessor's release, whatever it said about its own state."""
    if path is None or not stamp:
        return 0
    n = 0
    try:
        with path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                if isinstance(entry, dict) and entry.get("type") == "assistant" and not entry.get("isSidechain") and str(entry.get("timestamp") or "") > stamp:
                    n += 1
    except OSError:
        return 0
    return n


def handoff_state(task: str, old_path: Path | None, new_path: Path | None, now: datetime, within_min: int = 5, sessions: list[dict] | None = None, new_id: str = "") -> dict:
    """The restart's verification, one verdict: RUNNING (the successor is bound and has made a tool call), STALLED (bound and silent for longer than `within_min`), or the step it is still at
    (WAITING_FOR_RELEASE, WAITING_FOR_BIND, BOUND_WAITING_FIRST_ACTION), BOTH_BOUND (two hosts) or NEW_NOT_FOUND. A READ of two transcripts: it starts, stops and sends nothing. When the successor is stalled it names the
    row to address: the listing shows the successor and its predecessor under ONE name, told apart only by their start times, and a reference is not derivable from the session id (measured 2026-11-20: ListAgents [90ee47]
    for session 1ac4ca4b), so the row is described by its age and the sender must take the row whose age matches."""
    old = bind_timeline(old_path, task) if old_path else {"state": "MISSING"}
    new = bind_timeline(new_path, task) if new_path else {"state": "MISSING"}
    out = {"task": task, "old": old, "new": new}
    if new["state"] == "MISSING":
        out.update(verdict="NEW_NOT_FOUND", next="no transcript for the successor's id (a short id works only as a unique prefix of at least 8 characters): launch it again or correct the id")
        return out
    if old["state"] == "BOUND" and new["state"] == "BOUND":
        out.update(verdict="BOTH_BOUND", next="two hosts: the predecessor must write the plain line `MANDATE_RELEASED: " + task + "` (or be stopped once idle)")
        return out
    if new["state"] != "BOUND":
        if old["state"] != "RELEASED":
            out.update(verdict="WAITING_FOR_RELEASE", next="the predecessor has not released the task (its own checkpoint and release come first); the successor must not bind before it")
        else:
            waited = _age_min(old.get("released_at"), now)
            out.update(verdict="WAITING_FOR_BIND", waited_min=waited,
                       next="the predecessor released; the successor has not bound" + (": send it the follow-up now" if waited is not None and waited >= within_min else " (inside the allowed minutes)"))
            # 2026-11-20 (SCI successor T): it reported itself BOUND and worked for 9 m 42 s with no plain marker line in its transcript, so the verdict stayed WAITING_FOR_BIND with the advice "send the
            # follow-up", which did not say WHY. When the successor has been writing since the release, say it: a claim of being bound in a message is not the marker.
            active = _assistant_turns_after(new_path, old.get("released_at"))
            if active >= 3 and waited is not None and waited >= within_min:
                out.update(successor_turns_since_release=active,
                           next=f"the successor has written {active} assistant entries since the release but its transcript holds no plain `MANDATE_BOUND: {task}` line (a message saying it is bound does not count): "
                                "tell it to write that line ALONE in its own text block, in the same response as its next tool call")
        return out
    bound_for = _age_min(new.get("bound_at"), now)
    out["bound_min"] = bound_for
    if new["tool_calls_after_bind"] > 0:
        try:
            lag = round((datetime.fromisoformat(new["first_action_at"].replace("Z", "+00:00")) - datetime.fromisoformat(new["bound_at"].replace("Z", "+00:00"))).total_seconds() / 60, 1)
        except (AttributeError, TypeError, ValueError):
            lag = None
        out.update(verdict="RUNNING", first_action_after_bind_min=lag, next="bound and acting: nothing to do")
        return out
    stalled = bound_for is not None and bound_for >= within_min
    out.update(verdict="STALLED" if stalled else "BOUND_WAITING_FIRST_ACTION",
               next=("the bind line ended the turn: send the follow-up to THE SUCCESSOR (" + _address_hint(sessions, new_id, now) + "), then check again") if stalled else "bound a moment ago; check again within the allowed minutes")
    return out


def _address_hint(sessions: list[dict] | None, new_id: str, now: datetime) -> str:
    """How to pick the listing row: by name and start time, never by position or apparent recency alone."""
    rows = []
    for x in sessions or []:
        started = x.get("startedAt")
        age = round((now.timestamp() - started / 1000) / 60) if isinstance(started, (int, float)) else None
        rows.append((str(x.get("sessionId") or ""), x.get("name"), age))
    mine = next((r for r in rows if new_id and r[0].startswith(new_id)), None)
    if not mine:
        return "its row is not in the live listing: check that it is alive"
    same = [r for r in rows if r[1] == mine[1] and r[0] != mine[0]]
    text = f"name {mine[1]}, started {mine[2]} min ago"
    if same:
        text += "; the other row(s) with that name started " + ", ".join(f"{r[2]} min ago" for r in same) + " and belong to other sessions (the predecessor among them): in ListAgents take the row whose 'started' matches, after re-running it"
    return text


def _descendants(pid: int) -> list[int] | None:
    """Linux observation, not a kill list. Unknown process inventory prevents retirement."""
    parents = {}
    try:
        for path in Path("/proc").iterdir():
            if path.name.isdigit():
                try:
                    fields = (path / "stat").read_text().rsplit(")", 1)[1].split()
                    if fields[0] != "Z":
                        parents[int(path.name)] = int(fields[1])
                except FileNotFoundError:             # exited while enumerating
                    continue
    except (OSError, ValueError, IndexError):
        return None
    found = {pid}
    while True:
        more = {child for child, parent in parents.items() if parent in found} - found
        if not more:
            return sorted(found - {pid})
        found.update(more)


def retirement_state(task: str, old_id: str, new_id: str, sessions: list[dict] | None,
                     projects_dir: Path | None = None) -> dict:
    """Read-only, exact-identity preconditions for stopping ONE released background host.

    `id` from the runtime listing is the stop address; `sessionId` is the transcript identity.
    Display names and a guessed UUID prefix never authorise an arrest.
    """
    out = {"task": task, "old_session": old_id, "new_session": new_id, "verdict": "KEPT"}
    def keep(reason):
        return dict(out, reason=reason)
    if not UUID_RE.fullmatch(old_id) or not UUID_RE.fullmatch(new_id) or old_id == new_id:
        return keep("distinct full session UUIDs required")
    if sessions is None:
        return keep("runtime inventory unavailable")
    old_path = transcript_for_session(old_id, projects_dir)
    new_path = transcript_for_session(new_id, projects_dir)
    if old_path is None or new_path is None:
        return keep("transcript missing or ambiguous; absence is not a release")
    old, new = bind_timeline(old_path, task), bind_timeline(new_path, task)
    if old.get("state") != "RELEASED" or not old.get("bound_at") or old.get("active_tasks") != []:
        return keep("predecessor has not released every bound mandate")
    if new.get("state") != "BOUND" or not new.get("tool_calls_after_bind"):
        return keep("successor has not bound and acted")
    try:
        release = datetime.fromisoformat(old["released_at"].replace("Z", "+00:00"))
        bound = datetime.fromisoformat(new["bound_at"].replace("Z", "+00:00"))
        action = datetime.fromisoformat(new["last_action_at"].replace("Z", "+00:00"))
        if action < release:
            return keep("successor has not acted after predecessor release")
        if bound < release:
            out["overlap_observed"] = True           # preserve the mistake; do not make it an eternal cleanup block
    except (AttributeError, KeyError, TypeError, ValueError):
        return keep("release/bind timestamps unavailable or incompatible")
    hosts = live_bound_sessions(task, sessions, projects_dir)
    if [h["session_id"] for h in hosts] != [new_id]:
        return keep("successor is not the unique live bound host")
    rows = [s for s in sessions if s.get("sessionId") == old_id]
    if not rows:
        return dict(out, verdict="ALREADY_STOPPED", reason="released predecessor absent from live inventory")
    if len(rows) != 1:
        return keep("predecessor inventory ambiguous")
    old_row = rows[0]
    runtime_id = old_row.get("id")
    if not isinstance(runtime_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", runtime_id) or sum(s.get("id") == runtime_id for s in sessions) != 1:
        return keep("unique runtime stop address unavailable")
    if old_row.get("kind") != "background" or old_row.get("status") != "idle" or old_row.get("state") != "done":
        return keep("predecessor is not an idle, completed background turn")
    pid = old_row.get("pid")
    start = _start_ticks(pid) if isinstance(pid, int) and pid > 1 else None
    if start is None or pid == os.getpid():
        return keep("predecessor process identity unavailable")
    children = _descendants(pid)
    if children is None or children:
        return keep("predecessor has live descendants or process inventory is unavailable")
    # Jobs are currently task-tagged, not session-owned: do not infer that they belong
    # only to the successor. A later recall can retry after completion.
    try:
        files = list(jobs_dir(task).glob("*.json"))
        jobs = load_jobs(task)
        if any(j.get("state") == "ALIVE" for j in jobs):
            return keep("task still has a live job; ownership is not session-specific")
        if len(jobs) != len(files):
            return keep("task job inventory incomplete")
    except (OSError, ValueError, KeyError):
        return keep("task job inventory unavailable")
    return dict(out, verdict="ELIGIBLE", runtime_id=runtime_id, pid=pid, start_ticks=start,
                reason="released background predecessor; unique acting successor; no observed work")


def legacy_bound_tasks(task: str, old_path: Path | None, root: Path = ROOT) -> list[dict]:
    """Mandates other than `task` that the released predecessor's own transcript still carries as bound (a bind line with no release line in that chat), with what each RECORD says now. 2026-11-21: the handoff
    to this window said KEPT for the old interactive HE chat because two mandates bound there (a mandate record closed on 2026-11-14 and one released by its record) had no release line in a chat that
    went idle two days earlier; nothing said which actor owned them or that the records already closed them, so the verdict read as an open item for the operator. A release line is written only by the chat
    that holds the bind and is never written for it from another session: these mandates are reconciled by their record and its owner, and the list below is what that owner reads."""
    if old_path is None:
        return []
    out = []
    for other in bind_timeline(old_path, task).get("active_tasks", []):
        if other != task:
            st = mc.status_for(ROOT if root is None else root, other)
            out.append({"task": other, "record_verdict": st.get("verdict"), "record": st.get("record"), "steps": st.get("counts")})
    return out


def handoff_next(retired: str, names: dict, legacy: list[dict], old_in_inventory: bool) -> str:
    """The one line the launcher reads after a handoff: the predecessor's retirement, the display names still to be corrected, and the legacy bound lines. A printed rename list does not complete a handoff: the
    launcher applies each rename natively and reads `labels` again until it says CURRENT (operator, 2026-11-21). A released chat is not a recipient of new work and its closure is never an operator item."""
    text = "successor running; predecessor retirement " + retired + (" (use --retire-old to execute the guarded stop)" if retired == "ELIGIBLE" else "")
    if names.get("state") == "PENDING":
        text += (f"; SESSION NAMES PENDING ({len(names.get('renames') or [])}): the launcher applies each rename natively now (claude agents, the exact row, ctrl+r; demotions first) and reads "
                 f"`labels --task {names.get('task')}` again until it says CURRENT; the printed list is not the end of the handoff")
    if retired == "KEPT" and legacy:
        text += ("; the old chat still carries bound lines for " + ", ".join(f"{x['task']} (record {x['record_verdict']})" for x in legacy)
                 + ": reconcile them by their records and owners, never by a release line written for that chat from another session")
    if retired == "KEPT" and not old_in_inventory:
        text += "; the old session is absent from the live inventory, so no window is left to close"
    return text


def retire_predecessor(task: str, old_id: str, new_id: str, *, execute: bool = False,
                       projects_dir: Path | None = None) -> dict:
    """Supported stop only, followed by independent liveness verification. Never rm/kill.

    A runtime refusal is returned once, not retried through another command or permission mode.
    Two fresh observations reduce races; the runtime does not provide atomic compare-and-stop.
    """
    plan = retirement_state(task, old_id, new_id, list_sessions(), projects_dir)
    if execute and plan["verdict"] == "ALREADY_STOPPED" and _load("retirement-" + old_id).get("verdict") in ("STOP_PENDING", "STOP_UNVERIFIED"):
        _save("retirement-" + old_id, plan)
        log_event("predecessor_retirement", **plan)
    if not execute or plan["verdict"] != "ELIGIBLE":
        return plan
    held = _load("retirement-" + old_id)
    if held.get("verdict") in ("STOP_PENDING", "STOP_REFUSED", "STOP_UNVERIFIED"):
        return dict(plan, verdict="STOP_UNVERIFIED" if held["verdict"] == "STOP_PENDING" else held["verdict"],
                    retry_suppressed=True, reason="previous stop attempt needs runtime resolution; not retried automatically")
    fresh = retirement_state(task, old_id, new_id, list_sessions(), projects_dir)
    identity = ("runtime_id", "pid", "start_ticks")
    if fresh["verdict"] != "ELIGIBLE" or any(fresh.get(k) != plan.get(k) for k in identity):
        return dict(fresh, verdict="KEPT", reason="preconditions or process identity changed before stop")
    key = "retirement-" + old_id
    pending = dict(fresh, verdict="STOP_PENDING")
    _save(key, pending)
    if _load(key) != pending:
        return dict(fresh, verdict="KEPT", reason="cannot persist the stop attempt; no stop issued")
    try:
        result = subprocess.run([claude_bin(), "stop", fresh["runtime_id"]],
                                capture_output=True, text=True, timeout=30)
        if result.returncode:
            out = dict(fresh, verdict="STOP_REFUSED", reason=(result.stderr or result.stdout or "runtime stop failed")[:300])
        else:
            out = dict(fresh, verdict="STOP_UNVERIFIED", reason="stop returned success but retirement is not independently verified")
            # The supported stop acknowledges before process teardown completes (live
            # probe, 2026-11-20). Observe briefly; never issue a second stop.
            for attempt in range(11):
                remaining = list_sessions()
                alive = _start_ticks(fresh["pid"]) == fresh["start_ticks"] and _proc_state(fresh["pid"]) not in (None, "Z")
                hosts = live_bound_sessions(task, remaining, projects_dir)
                if remaining is not None and not alive and not any(s.get("sessionId") == old_id for s in remaining) and [h["session_id"] for h in hosts] == [new_id]:
                    out = dict(fresh, verdict="RETIRED", reason="predecessor absent from live inventory and original process no longer alive; files untouched")
                    break
                if attempt < 10:
                    time.sleep(0.5)
    except (OSError, subprocess.SubprocessError) as exc:
        out = dict(fresh, verdict="STOP_REFUSED", reason=str(exc)[:300])
    _save(key, out)
    log_event("predecessor_retirement", **out)
    return out


# Mandate states in which the catch-up may look for released predecessors of the unique acting host. Retiring an old, already released host is housekeeping about
# THAT host; it is independent of whether the successor's queue still has work (RUNNING, STOPPED_RESUMABLE), is waiting on the operator or on a dependency (BLOCKED) or
# is complete with closure pending (COMPLETE). Until 2026-11-20 only RUNNING and STOPPED_RESUMABLE reached it, so a released predecessor stayed alive whenever its
# successor was BLOCKED or COMPLETE_PENDING (the standing mandates of this laboratory sit in COMPLETE by design). Not here: PAUSED (an operator stop: nothing about the
# mandate is touched), UNKNOWN (an observation that could not be made) and DUPLICATE_HOST (no unique successor). retire_released and retirement_state still require
# exactly one live acting host, a released and idle background predecessor with no descendants, no live task job and an exact runtime id and process identity.
RETIRE_STATES = ("RUNNING", "STOPPED_RESUMABLE", "BLOCKED", "COMPLETE")


def retire_released(task: str, sessions: list[dict] | None, *, execute: bool = False) -> list[dict]:
    """Existing watch's catch-up: exact released predecessors of a unique acting task host.
    No name-based sweep, no new scheduler, no revival or deletion of a historical session.
    """
    hosts = live_bound_sessions(task, sessions)
    if len(hosts) != 1:
        return []
    new_id = hosts[0]["session_id"]
    out = []
    for row in sessions or []:
        old_id = row.get("sessionId", "")
        if old_id == new_id or row.get("kind") != "background":
            continue
        path = transcript_for_session(old_id)
        if path is not None and cached_binding(path) is None and mc.marker_state(path, task) == "RELEASED":
            result = retire_predecessor(task, old_id, new_id, execute=execute)
            out.append(result)
            if result["verdict"] in ("STOP_REFUSED", "STOP_UNVERIFIED"):
                break                                      # no alternate wrapper or immediate retry
    return out


def live_bound_sessions(task: str, sessions: list[dict] | None, projects_dir: Path | None = None) -> list[dict]:
    """The LIVE sessions whose own last marker line binds this task. The key is the bound session id, never a display name: two live sessions may legitimately answer to one name (the bound session
    and an operator chat that investigated), and only the ones that carry `MANDATE_BOUND: <task>` are hosts of it."""
    out = []
    for sess in sessions or []:
        sid = str(sess.get("sessionId") or "")
        path = transcript_for_session(sid, projects_dir) if sid else None
        if path is not None and cached_binding(path) == task:
            out.append({"session_id": sid, "name": sess.get("name"), "kind": sess.get("kind"), "status": sess.get("status")})
    return out


def has_saved_options(session_id: str) -> bool:
    """Does the runtime's background-job store hold saved options (name, model) for this session? `~/.claude/jobs/<first 8 characters of the id>/state.json` is written when a session has been a background
    session. MEASURED 2026-11-18 on a scratch session: for such a session the runtime says "keeps its own saved options, so the flags you passed started a copy"; a revival WITH any flag forks a second session
    under a new id, and WITHOUT flags it continues the session itself under the same id and the same name."""
    base = Path(os.environ.get("LEGEND_CLAUDE_JOBS") or os.path.expanduser("~/.claude/jobs"))
    return (base / session_id[:8] / "state.json").is_file()


def last_session_name(transcript: Path) -> str | None:
    """The name the operator gave the session (its last `custom-title` record). A session that has NO saved options (an interactive one: the Science session after the 2026-11-18 OOM) comes back with a
    name generated from the resume prompt ('orch-adv004-mandate-reconciliation'), which breaks every name-based address; for those the revival passes the chosen name again. Never for a session that has saved
    options: any flag on such a session starts a COPY (see has_saved_options)."""
    name = None
    try:
        with transcript.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"custom-title"' not in line:
                    continue
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                if isinstance(entry, dict) and entry.get("type") == "custom-title" and isinstance(entry.get("customTitle"), str) and entry["customTitle"].strip():
                    name = entry["customTitle"].strip()
    except OSError:
        return None
    return name


def find_bound_transcript(task: str, projects_dir: Path | None = None, max_age_days: int = 5) -> Path | None:
    """The newest session transcript whose last marker line binds this task."""
    base = projects_dir or Path(os.path.expanduser("~/.claude/projects"))
    cutoff = time.time() - max_age_days * 86400
    cands = []
    try:
        for p in base.glob("*/*.jsonl"):
            try:
                if p.stat().st_mtime >= cutoff:
                    cands.append(p)
            except OSError:
                continue
    except OSError:
        return None
    for p in sorted(cands, key=lambda q: q.stat().st_mtime, reverse=True):
        if cached_binding(p) == task:
            return p
    return None


def find_near_marker(task: str, projects_dir: Path | None = None, max_age_days: int = 5) -> dict | None:
    """When no session binds the task: the newest line that names `MANDATE_BOUND: <task>` but is not a marker (it sits inside a longer line, or the id carries trailing
    punctuation). The canonical reader refuses such a line on purpose (a quoted or negated mention must not bind), so the owner has to write the plain line again; saying
    which session wrote the near-miss turns "unknown" into an instruction. Nothing is bound by this."""
    base = projects_dir or Path(os.path.expanduser("~/.claude/projects"))
    cutoff = time.time() - max_age_days * 86400
    try:
        cands = [p for p in base.glob("*/*.jsonl") if p.stat().st_mtime >= cutoff]
    except OSError:
        return None
    rx = re.compile(r"MANDATE_BOUND:\s*" + re.escape(task))
    for p in sorted(cands, key=lambda q: q.stat().st_mtime, reverse=True):
        found = None
        try:
            with p.open(encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    if task not in line or "MANDATE_BOUND" not in line:
                        continue
                    try:
                        entry = json.loads(line)
                    except ValueError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    for text in mc._text_blocks(entry):
                        for l in mc._outside_fences(text).splitlines():
                            if rx.search(l) and not mc.MARKER_RE.match(l):
                                found = {"session": p.stem, "at": entry.get("timestamp", ""), "line": l.strip()[:100]}
        except OSError:
            continue
        if found:
            return found
    return None


def find_near_release(path: Path | str, task: str) -> dict | None:
    """The last line of the session's own assistant text, after its last binding of the task, that opens with `MANDATE_RELEASED` but is no marker (no task id, words after
    the id, bold or backticks around it). 2026-11-28: a predecessor wrote the bare word, `released` answered only BOUND, and the cause was found by grepping its transcript.
    A hint for the checker; nothing is released by it."""
    found = None
    try:
        with Path(path).open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(entry, dict) or entry.get("type") != "assistant":
                    continue
                for text in mc._text_blocks(entry):
                    for l in mc._outside_fences(text).splitlines():
                        marker = mc.MARKER_RE.match(l)
                        if marker and marker.groups() == ("BOUND", task):
                            found = None
                        elif l.strip().lstrip("*`> ").startswith("MANDATE_RELEASED") and (not marker or marker.group(2).rstrip("._-") == task != marker.group(2)):
                            found = {"at": entry.get("timestamp", ""), "line": l.strip()[:100]}
    except OSError:
        return None
    return found


def transcript_cwd(transcript: Path) -> str | None:
    """The working directory the session ran in (a revival must start there: the runtime
    resolves workspace trust and the project's permissions from it)."""
    try:
        with transcript.open(encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh):
                if i > 200:
                    break
                try:
                    c = json.loads(line).get("cwd")
                except (ValueError, AttributeError):
                    continue
                if isinstance(c, str) and c:
                    return c
    except OSError:
        pass
    return None


def turn_start(transcript: Path) -> float | None:
    """Epoch time of the latest real user/prompt entry (not a tool result): the start of the turn
    that is asking. For the in-session cron this is the cron prompt's arrival."""
    last = None
    try:
        with transcript.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(e, dict) or e.get("type") != "user" or e.get("isSidechain"):
                    continue
                c = (e.get("message") or {}).get("content")
                if isinstance(c, list) and all(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
                    continue
                if isinstance(c, list) and not any(isinstance(b, dict) and b.get("type") == "text" for b in c):
                    continue
                ts = e.get("timestamp")
                if isinstance(ts, str):
                    try:
                        last = datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
                    except ValueError:
                        pass
    except OSError:
        return None
    return last


def last_real_turn(transcript: Path, block: int = 1 << 20) -> float | None:
    """Epoch time of the latest `user` or `assistant` entry that carries a timestamp: a real turn (a message, a tool call or its result).
    The runtime also appends title, mode, cost, bridge and queue records to the tail, and those move the file's mtime with nobody working
    (measured 2026-11-24: IT59 and SCI65 read 'active 2 min ago' on a last turn five hours old). Read backwards in blocks; None when none is found."""
    try:
        with transcript.open("rb") as fh:
            pos = fh.seek(0, os.SEEK_END)
            carry = b""
            while pos > 0:
                step = min(block, pos)
                pos -= step
                fh.seek(pos)
                lines = (fh.read(step) + carry).split(b"\n")
                carry = lines[0] if pos > 0 else b""        # the first line of a block may be cut: it is completed by the next block back
                for raw in reversed(lines[1:] if pos > 0 else lines):
                    if b'"user"' not in raw and b'"assistant"' not in raw:
                        continue
                    try:
                        e = json.loads(raw)
                    except ValueError:
                        continue
                    ts = e.get("timestamp") if isinstance(e, dict) and e.get("type") in ("user", "assistant") else None
                    if isinstance(ts, str):
                        try:
                            return datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
                        except ValueError:
                            continue
    except OSError:
        pass
    return None


def last_activity(transcript: Path, tasks_root: Path | None = None, include_transcript: bool = True, before: float | None = None, real_turns_only: bool = False) -> float:
    """Latest mtime of the transcript and of that session's background-task output files.
    A session calling the check on itself (the in-session cron) leaves its own transcript out:
    its turn is the request, and counting it would always read as activity.
    `real_turns_only`: the transcript counts at its last real turn, never later than its mtime,
    so runtime metadata written to the tail is not progress; a transcript with no timestamped turn keeps its mtime."""
    latest = 0.0
    if include_transcript:
        try:
            latest = transcript.stat().st_mtime
            if real_turns_only:
                turn = last_real_turn(transcript)
                if turn is not None:
                    latest = min(latest, turn)
        except OSError:
            pass
    sid = transcript.stem
    root = tasks_root or Path(f"/tmp/claude-{os.getuid()}")
    try:
        for f in root.glob(f"*/{sid}/tasks/*.output"):
            try:
                m = f.stat().st_mtime
                if before is None or m <= before:     # after `before` it is the caller's own work
                    latest = max(latest, m)
            except OSError:
                continue
    except OSError:
        pass
    return latest


# ---------------------------------------------------------------- background jobs
# A long silent job is only "alive" if its OWN process is alive: identity is PID plus the
# process start time read from /proc (a reused PID has another start time), never an output
# file's mtime and never a process name. Jobs are started through `job run`, which tags the
# environment (LEGEND_MANDATE_JOB=<task>), detaches the job and records its exit status.
JOB_ENV = "LEGEND_MANDATE_JOB"


def _start_ticks(pid: int) -> int | None:
    try:
        stat = Path(f"/proc/{pid}/stat").read_text()
        return int(stat.rsplit(")", 1)[1].split()[19])      # field 22: start time in clock ticks
    except (OSError, ValueError, IndexError):
        return None


def _proc_state(pid: int) -> str | None:
    try:
        return Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()[0]
    except (OSError, IndexError):
        return None


def jobs_dir(task: str) -> Path:
    return state_dir() / "jobs" / task


def job_state(job: dict) -> str:
    """ALIVE | DONE | DEAD: an exit file means the job ended and said how; no exit file and no
    live process with the recorded start time means it died without reporting."""
    if Path(job["exit_file"]).exists():
        return "DONE"
    if _start_ticks(job["pid"]) == job["start_ticks"] and _proc_state(job["pid"]) not in (None, "Z"):
        return "ALIVE"
    return "DEAD"


def load_jobs(task: str, base: Path | None = None) -> list[dict]:
    out = []
    for f in sorted((base or jobs_dir(task)).glob("*.json")):
        try:
            j = json.loads(f.read_text(encoding="utf-8"))
            j["_file"] = str(f)
            j["state"] = job_state(j)
            if j["state"] == "DONE":
                try:
                    j["exit_code"] = int(Path(j["exit_file"]).read_text().strip() or "-1")
                except (OSError, ValueError):
                    j["exit_code"] = -1
            out.append(j)
        except (OSError, ValueError, KeyError):
            continue
    return out


def summarise_jobs(jobs: list[dict]) -> dict:
    return {"alive": [j for j in jobs if j["state"] == "ALIVE"],
            "to_collect": [j for j in jobs if j["state"] == "DONE" and not j.get("collected")],
            "dead": [j for j in jobs if j["state"] == "DEAD" and not j.get("collected")]}


def memory_scope(cmd: list[str], memory_max: str) -> list[str]:
    """Wrap `cmd` in a transient systemd user scope with a hard memory cap. The kernel then
    confines an out-of-memory kill to this scope and systemd stops only the scope, so a runaway
    battery or browser cannot widen into the desktop service (whose OOMPolicy=stop kills every
    process it holds). Opt-in: nothing is capped unless asked; no threshold is imposed here."""
    if not re.fullmatch(r"[1-9]\d*(\.\d+)?[KMGT]?", memory_max):
        raise ValueError(f"--memory-max must look like 3G, 800M or 2500000000, not {memory_max!r}")
    exe = shutil.which("systemd-run")
    if not exe:
        raise RuntimeError("systemd-run is not available: the job is NOT started uncapped, since a cap was requested")
    return [exe, "--user", "--scope", "--quiet", "-p", f"MemoryMax={memory_max}", "-p", "OOMPolicy=stop", "--", *cmd]


def job_run(task: str, label: str, cmd: list[str], cwd: str | None = None, memory_max: str | None = None) -> dict:
    """Start `cmd` detached and tagged. Idempotent per (task, label): a live job with the same
    label is returned instead of starting a second execution of the same work. With `memory_max`
    the job runs in its own memory-capped scope (see `memory_scope`); the recorded `cmd` stays
    the caller's command and `memory_max` is recorded beside it."""
    for j in load_jobs(task):
        if j["label"] == label and j["state"] == "ALIVE":
            return dict(j, started=False, note="already running: not started a second time")
    run_cmd = memory_scope(cmd, memory_max) if memory_max else cmd
    d = jobs_dir(task)
    d.mkdir(parents=True, exist_ok=True)
    jid = f"{int(time.time())}-{label}"
    exit_file, log = d / f"{jid}.exit", d / f"{jid}.log"
    script = " ".join(shlex.quote(c) for c in run_cmd) + f"; echo $? > {shlex.quote(str(exit_file))}"
    with open(log, "ab") as fh:
        p = subprocess.Popen(["/bin/sh", "-c", script], start_new_session=True, stdin=subprocess.DEVNULL,
                             stdout=fh, stderr=subprocess.STDOUT, cwd=cwd, env=dict(os.environ, **{JOB_ENV: task}))
    job = {"id": jid, "task": task, "label": label, "cmd": cmd, "pid": p.pid, "start_ticks": _start_ticks(p.pid),
           "log": str(log), "exit_file": str(exit_file), "started_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "collected": False}
    if memory_max:
        job["memory_max"] = memory_max
    (d / f"{jid}.json").write_text(json.dumps(job, indent=1), encoding="utf-8")
    log_event("job_started", task=task, label=label, pid=p.pid)
    return dict(job, started=True, state="ALIVE")


def _kv_kb(path: Path, keys: tuple[str, ...]) -> dict:
    out: dict = {}
    try:
        for line in path.read_text().splitlines():
            k, _, v = line.partition(":")
            if k in keys:
                out[k] = int(v.split()[0])
    except (OSError, ValueError, IndexError):
        pass
    return out


def resource_state(proc: str = "/proc", top: int = 8, jobs_base: Path | None = None, sessions: list[dict] | None = None) -> dict:
    """Observed memory facts for coordinating heavy work. READ-ONLY and threshold-free: it states
    what is loaded and who holds it, and the caller decides. RSS counts a shared page once per
    process (a group's RSS is an upper bound); `pss_mb` splits it and is the figure to size a limit on (measured 2026-11-18: desktop service 4.4 GB RSS, 3.3 GB PSS). `groups` are cgroups (the unit that an OOM
    event would stop or kill together), not processes: that is the blast radius."""
    root = Path(proc)
    mem = _kv_kb(root / "meminfo", ("MemTotal", "MemAvailable", "SwapTotal", "SwapFree"))
    psi: dict = {}
    try:
        for line in (root / "pressure" / "memory").read_text().splitlines():
            kind, _, rest = line.partition(" ")
            psi[kind] = dict(x.split("=") for x in rest.split())
    except OSError:
        pass
    groups: dict[str, dict] = {}
    for d in root.iterdir():
        if not d.name.isdigit():
            continue
        try:
            cg = (d / "cgroup").read_text().strip().splitlines()[-1].rsplit(":", 1)[-1]
            rss = _kv_kb(d / "status", ("VmRSS",)).get("VmRSS", 0)
            comm = (d / "comm").read_text().strip()
        except (OSError, IndexError):
            continue
        pss = _kv_kb(d / "smaps_rollup", ("Pss",)).get("Pss")      # proportional: a shared page is split among its users (absent for another user's process)
        g = groups.setdefault(cg, {"cgroup": cg, "rss_mb": 0, "pss_mb": 0, "procs": 0, "largest": ("", 0)})
        g["rss_mb"] += rss // 1024
        g["pss_mb"] += (pss if pss is not None else rss) // 1024
        g["procs"] += 1
        if rss // 1024 > g["largest"][1]:
            g["largest"] = (comm, rss // 1024)
    ranked = sorted(groups.values(), key=lambda g: -g["pss_mb"])[:top]
    for g in ranked:
        g["largest"] = {"comm": g["largest"][0], "rss_mb": g["largest"][1]}
    alive = []
    base = jobs_base or (state_dir() / "jobs")
    if base.is_dir():
        for tdir in sorted(base.iterdir()):
            for j in load_jobs(tdir.name, tdir):
                if j["state"] == "ALIVE":
                    alive.append({"task": j.get("task", tdir.name), "label": j["label"], "pid": j["pid"],
                                  "memory_max": j.get("memory_max"), "cmd": " ".join(j["cmd"])[:80]})
    held = []
    for x in sessions or []:
        try:
            leaf = (root / str(x["pid"]) / "cgroup").read_text().strip().splitlines()[-1].rsplit("/", 1)[-1]
        except (OSError, IndexError, KeyError):
            leaf = "?"
        held.append({"name": x.get("name"), "session": str(x.get("sessionId", ""))[:8], "pid": x.get("pid"), "cgroup": leaf})
    load = ""
    try:
        load = (root / "loadavg").read_text().split()[0]
    except (OSError, IndexError):
        pass
    return {"mem_total_mb": mem.get("MemTotal", 0) // 1024, "mem_available_mb": mem.get("MemAvailable", 0) // 1024,
            "swap_total_mb": mem.get("SwapTotal", 0) // 1024, "swap_free_mb": mem.get("SwapFree", 0) // 1024,
            "pressure": psi, "load1": load, "groups": ranked, "alive_jobs": alive, "sessions": held,
            "note": "facts only, no threshold. `sessions[].cgroup` is the unit an OOM event stops together with the session; start a heavy job with `job run --memory-max` so its OOM kill stays in its own scope"}


def job_collect(task: str, jid: str) -> bool:
    f = jobs_dir(task) / f"{jid}.json"
    try:
        j = json.loads(f.read_text(encoding="utf-8"))
        j["collected"] = True
        f.write_text(json.dumps(j, indent=1), encoding="utf-8")
        return True
    except (OSError, ValueError):
        return False


def push_confirmation_missing(root: Path, record_rel: str | None, timeout: int = 40) -> str | None:
    """For a mandate whose record says COMPLETE: the commit that closed it must be on the
    development remote. Returns a reason when it is NOT, None when confirmed or unknown."""
    if not record_rel:
        return None
    try:
        last = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%H", "--", record_rel],
                              capture_output=True, text=True, timeout=20).stdout.strip()
        urls = subprocess.run(["git", "-C", str(root), "remote", "-v"], capture_output=True, text=True, timeout=20).stdout
        remote = next((ln.split()[0] for ln in urls.splitlines() if "marinomassimo-dot/legend-development" in ln), None)
        if not last or not remote:
            return None
        subprocess.run(["git", "-C", str(root), "fetch", "-q", remote, "main"], capture_output=True, timeout=timeout, check=True)
        r = subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", last, f"{remote}/main"], timeout=20)
        return None if r.returncode == 0 else f"the commit that closed the record ({last[:8]}) is not on {remote}/main"
    except (OSError, subprocess.SubprocessError):
        return None


# ---------------------------------------------------------------- the decision (pure)
def classify(status: dict, session: dict | None, session_list_ok: bool, bound: bool,
             idle_seconds: float | None, pending: dict, signature: str, now: float,
             quiet_minutes: int = QUIET_MINUTES, jobs: dict | None = None, push_missing: str | None = None, near_marker: dict | None = None,
             dup_hosts: list | None = None) -> dict:
    """Return {state, action, why}. action is RESUME or NONE. No I/O."""
    v = status.get("verdict")
    jobs = jobs or {"alive": [], "to_collect": [], "dead": []}
    closing = False
    if v in ("COMPLETE_PENDING",) or v == "RELEASED":
        msg = status.get("message", "")
        state = "PAUSED" if "PAUSED" in msg.upper() or "CANCELLED" in msg.upper() else "COMPLETE"
        if state == "PAUSED" or not push_missing:
            return {"state": state, "action": "NONE", "why": f"record verdict {v}"}
        closing = True      # COMPLETE, but a confirmation the mandate requires (the push) is missing: not complete yet
        v = "CONTINUE"
    if v == "ALL_BLOCKED":
        return {"state": "BLOCKED", "action": "NONE", "why": status.get("message", "all steps blocked")}
    if v in ("EVIDENCE_PENDING", "INCONSISTENT_COMPLETE"):
        # These are known unfinished closure obligations, not an unreadable runtime.
        # A bound session can supply the missing pointers without repeating the science.
        v = "CONTINUE"
    if v != "CONTINUE":
        return {"state": "UNKNOWN", "action": "NONE", "why": f"record verdict {v}: {status.get('message', '')}"[:300]}
    if not bound:
        hint = (f"; session {near_marker['session']} wrote `{near_marker['line']}` at {near_marker['at'][:19]}: not a marker, because the line must contain only `MANDATE_BOUND: <id>` "
                "(nothing before or after it, no trailing punctuation, not in a code fence), so that session must write that plain line again" if near_marker else "")
        return {"state": "UNKNOWN", "action": "NONE", "why": "no session transcript carries MANDATE_BOUND for this task (the line must start a line of the session's own persisted text; after writing it, run `mandate_watch.py check --task <id> --deliver none --json` and expect a session id, else write it again in a message of its own)" + hint}
    if not session_list_ok:
        return {"state": "UNKNOWN", "action": "NONE", "why": "the session listing could not be read"}
    if dup_hosts and len(dup_hosts) > 1:
        names = ", ".join(f"{d.get('name')} [{str(d.get('session_id'))[:8]}]" for d in dup_hosts)
        return {"state": "DUPLICATE_HOST", "action": "NONE",
                "why": (f"{len(dup_hosts)} live sessions carry `MANDATE_BOUND` for this task ({names}): none is revived, none is chosen, and no second recall may be armed. Release the surplus one "
                        "with the plain line `MANDATE_RELEASED: <TASK_ID>` in its own text (or stop it) and keep the one the record's SESSION_BINDING names; two sessions that only share a display name are not hosts")}
    if jobs["alive"]:
        j = jobs["alive"][0]
        return {"state": "RUNNING", "action": "NONE", "why": f"job '{j['label']}' is alive (pid {j['pid']}) even if its output is silent"}
    if session is not None and session.get("status") == "busy":
        left = re.search(r"(\d+) executable step", status.get("message", "") or "")
        # IT39: a busy session is not progress. The hourly in-session cron must pass --self-call (the caller's own turn is then not "busy work"); without it a session waiting on a
        # monitor is answered RUNNING whatever the queue holds. Say how much authorised work the record still lists, so the answer cannot be read as "nothing to do".
        return {"state": "RUNNING", "action": "NONE", "why": "session busy" + (f"; the record still lists {left.group(1)} executable step(s): busy is not progress, and an in-session check should use --self-call" if left else "")}
    if idle_seconds is not None and idle_seconds < quiet_minutes * 60:
        return {"state": "RUNNING", "action": "NONE", "why": f"activity {int(idle_seconds // 60)} min ago (quiet threshold {quiet_minutes})"}
    last = pending.get("requested_at")
    if last and pending.get("signature") == signature and now - last < REREQUEST_MINUTES * 60 and (session is not None or now - last < STARTUP_GRACE_MINUTES * 60):
        # The pending guard protects a LIVE session that was asked and has not answered yet, and a revival that is still starting (the grace window: a second `--bg --resume` of the same session while the first
        # is coming up would be a copy). A session that is not live after the grace window was revived once and died again (a second OOM, a second kill): asking it again is the recovery, not spam, and the
        # hourly cron is the only rate (measured 2026-11-18 on a scratch session: a second death within the window was refused for three hours).
        return {"state": "STOPPED_RESUMABLE", "action": "NONE", "why": "a request is already pending for this queue state"}
    extra = ""
    if jobs["to_collect"]:
        extra += "; finished job(s) to collect: " + ", ".join(f"{j['label']} (exit {j.get('exit_code')})" for j in jobs["to_collect"])
    if jobs["dead"]:
        extra += "; job(s) that DIED without an exit status: " + ", ".join(j["label"] for j in jobs["dead"])
    what = f"mandate COMPLETE but {push_missing}" if closing else f"authorised work remains ({status.get('message', '')[:120]})"
    return {"state": "STOPPED_RESUMABLE", "action": "RESUME",
            "why": "session " + ("absent from the live listing" if session is None else "idle") + f" and silent, {what}{extra}"}


def recall_clause(recall) -> str:
    """The sentence a revival adds for a mandate whose host keeps an in-session recall (a record field `RECALL: {"mark": ..., "command": ...}`). Measured 2026-11-18 on a scratch session (Claude Code
    2.1.327): a session cron survives the death of its process and a resume, under the SAME job id, so the right first move is to look, not to create: a second CronCreate would be a second recall."""
    if not isinstance(recall, dict) or not recall.get("mark"):
        return ""
    cmd = f" The text of the recall is the output of `{recall['command']}`." if recall.get("command") else ""
    return (f" This mandate keeps ONE in-session recall (its text starts with {recall['mark']!r}).{cmd} First call CronList: the runtime restores the session's recall job when a session is resumed "
            "(same job id), so if a job carrying that mark is listed, do NOT create another; create it only when none is listed; never two. Session cron jobs expire after 7 days, so note when it was "
            f"created and renew it (CronDelete, then CronCreate) before day {recall.get('renew_days', 6)}.")


def request_text(task: str, status: dict, record_path: str = "", recall=None, *, root: Path | None = None) -> str:
    where = f" The record is {record_path}." if record_path else ""
    return (f"Mandate {task} is open with authorised work remaining ({status.get('message', '')[:200]}).{where} "
            "Hourly watch: the session had stopped. Resume from the checkpoint in the mandate record, "
            "choose the next useful authorised step yourself, and keep going until the record releases "
            "the mandate. Before starting any job check `mandate_watch.py job list --task <id>` and the worktree list: "
            "never start a second execution of work that is already running or a second integrator. "
            "If only closure evidence is missing, supply the verified pointers; do not repeat completed science. "
            "Do not ask the operator for anything the mandate already authorises." + recall_clause(recall)
            + "\n\n" + mc.guidance_text(root if root is not None else ROOT))


# ---------------------------------------------------------------- command
def record_dict(root: Path, rec_rel: str | None) -> dict:
    try:
        data = json.loads((root / rec_rel).read_text(encoding="utf-8")) if rec_rel else {}
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def record_binding_id(rec: dict) -> str | None:
    bind = rec.get("SESSION_BINDING") if isinstance(rec, dict) else None
    if isinstance(bind, dict):
        return str(bind.get("session_id") or "") or None
    m = UUID_RE.search(str(bind or ""))
    return m.group(0) if m else None


def check(task: str, *, root: Path = ROOT, deliver: str = "none", quiet_minutes: int = QUIET_MINUTES, resume_args: tuple = (),
          projects_dir: Path | None = None, tasks_root: Path | None = None,
          sessions=_SESSIONS_UNSET, now: float | None = None, runner=None, self_call: bool = False) -> dict:
    now = time.time() if now is None else now
    status = mc.status_for(root, task)
    rec_rel = status.get("record")
    signature = mc._queue_signature(root, rec_rel)
    # None is an observed listing failure. Do not repeat a runtime query per mandate
    # in --all; only the default sentinel requests a fresh observation.
    live = list_sessions() if sessions is _SESSIONS_UNSET else sessions
    rec = record_dict(root, rec_rel)
    bind_sid = record_binding_id(rec)
    dups = live_bound_sessions(task, live, projects_dir) if live else []
    transcript = None
    if dups:                      # a live session that carries the marker is the host; the record's SESSION_BINDING decides among several
        pick = next((d["session_id"] for d in dups if d["session_id"] == bind_sid), dups[0]["session_id"])
        transcript = transcript_for_session(pick, projects_dir)
    if transcript is None:
        transcript = find_bound_transcript(task, projects_dir)
    sid = transcript.stem if transcript else None
    session = next((s for s in (live or []) if s.get("sessionId") == sid), None) if sid else None
    if self_call and session is not None:
        session = dict(session, status="idle")      # the caller's own turn is not "busy work"
    if self_call and transcript:
        start = turn_start(transcript) or now
        act = last_activity(transcript, tasks_root, include_transcript=False, before=start)
        idle = (start - act) if act else None       # activity before the asking turn began
    else:
        idle = (now - last_activity(transcript, tasks_root, real_turns_only=True)) if transcript else None   # metadata-only mtime is not progress (a busy session and a live job are decided before idle is read)
    pend = _load(task)
    jobs = summarise_jobs(load_jobs(task))
    push_missing = None
    if status.get("verdict") == "RELEASED" and "COMPLETE" in status.get("message", "").upper():
        push_missing = push_confirmation_missing(root, rec_rel)
    near = find_near_marker(task, projects_dir) if transcript is None and status.get("verdict") not in ("RELEASED", "COMPLETE_PENDING") else None
    out = classify(status, session, live is not None, transcript is not None, idle, pend, signature, now, quiet_minutes,
                   jobs=jobs, push_missing=push_missing, near_marker=near, dup_hosts=dups)
    out.update({"task": task, "session": sid, "signature": signature[:12],
                "record_verdict": status.get("verdict")})
    if len(dups) > 1:
        out["live_bound_sessions"] = dups
    if near:
        out["near_marker"] = near
    if out["action"] == "RESUME" and deliver == "resume":
        if session is not None:
            out["delivery"] = "not sent: the session is alive; the in-session cron delivers to a live session"
        else:
            chosen = None if has_saved_options(sid) else last_session_name(transcript)
            cmd = [claude_bin(), "--bg", *resume_args, *(["--name", chosen] if chosen else []), "--resume", sid,
                   request_text(task, status, str(root / rec_rel) if rec_rel else "", rec.get("RECALL") if isinstance(rec, dict) else None, root=root)]
            try:
                cwd = transcript_cwd(transcript)
                res = (runner or (lambda c, cwd=None: subprocess.run(c, capture_output=True, text=True, timeout=120, cwd=cwd)))(cmd, cwd=cwd)
                ok = getattr(res, "returncode", 1) == 0
                out["delivery"] = "sent" if ok else f"failed rc={getattr(res, 'returncode', '?')}"
                out["delivery_output"] = (getattr(res, "stdout", "") or getattr(res, "stderr", ""))[:300]
                if ok:
                    _save(task, {"requested_at": now, "signature": signature, "session": sid})
            except (OSError, subprocess.SubprocessError) as exc:
                out["delivery"] = f"failed: {exc}"
    elif out["action"] == "RESUME" and deliver == "none" and self_call:
        _save(task, {"requested_at": now, "signature": signature, "session": sid, "via": "in-session"})
        out["delivery"] = "the caller is the session: continue now"
    # Every scheduled look is recorded, RUNNING included (iteration 7): a healthy long run used to leave no trace, so
    # "did the scheduler look at this mandate this hour?" could not be answered from the log.
    # IT19: a failed revival says WHY in the log (for example "Workspace not trusted"), not only that it failed.
    log_event("check", **{k: out[k] for k in ("task", "state", "action", "why") if k in out}, delivery=out.get("delivery"),
              **({"delivery_output": out["delivery_output"][:200]} if str(out.get("delivery", "")).startswith("failed") and out.get("delivery_output") else {}))
    return out


def rebind(task: str, to: str, authorised_by: str, *, root: Path = ROOT, sessions=_SESSIONS_UNSET, projects_dir: Path | None = None, now: float | None = None) -> dict:
    """Transfer the host role of a mandate to a SUBSTITUTE session. Nothing transfers by itself: a revived session keeps its own id, a name is not an identity, and the watch never picks a new host.
    The operator's authorisation is an explicit pointer (`authorised_by`: the message, roadmap line or record where it was given); without it nothing happens. Refused when: the record is PAUSED or CANCELLED
    (a stop is the operator's); the target is not exactly one live session; another LIVE session still carries `MANDATE_BOUND` for the task (no two hosts: stop it or have it write
    `MANDATE_RELEASED: <task>` first). On success the record's SESSION_BINDING names the target (and the previous binding is kept in the entry), one `rebind` event is logged, and the answer says what
    the new host must do: write the plain line `MANDATE_BOUND: <task>` in its own text, call CronList, and arm the ONE recall only if none carries the mark."""
    pointer = (authorised_by or "").strip()
    if len(pointer) < 8:
        raise PermissionError("rebind needs --authorised-by: a pointer to where the operator authorised this substitute (message, roadmap entry, record line)")
    status = mc.status_for(root, task)
    rec_rel = status.get("record")
    if not rec_rel:
        raise ValueError(f"no record for {task}: {status.get('message')}")
    path = root / rec_rel
    rec = json.loads(path.read_text(encoding="utf-8"))
    for key, block in mc.load_blocks(rec):
        if mc.block_state(block) in mc.OPERATOR_STOPS:
            raise PermissionError(f"{key} is {mc.block_state(block)}: a stop is the operator's; a substitute does not reopen it")
    live = list_sessions() if sessions is _SESSIONS_UNSET else sessions
    target = route(to, live, root)
    if target["status"] != "RESOLVED":
        raise ValueError(f"the substitute {to!r} does not resolve to exactly one live session ({target['status']}: {target.get('why', '')})")
    others = [d for d in live_bound_sessions(task, live, projects_dir) if d["session_id"] != target["session_id"]]
    if others:
        raise PermissionError("another live session still carries MANDATE_BOUND for this task (" + ", ".join(f"{d['name']} [{d['session_id'][:8]}]" for d in others)
                              + "): stop it or have it write `MANDATE_RELEASED: <TASK_ID>` first, so that there is exactly one host")
    previous = rec.get("SESSION_BINDING")
    stamp = datetime.fromtimestamp(now or time.time(), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rec["SESSION_BINDING"] = {"session_id": target["session_id"], "name_at_binding": target.get("recipient"), "bound_at": stamp, "authorised_by": pointer,
                              **({"previous": previous} if previous else {})}
    mc._write_record(path, rec)
    log_event("rebind", task=task, session=target["session_id"], name=target.get("recipient"), authorised_by=pointer[:200],
              previous=(previous or {}).get("session_id") if isinstance(previous, dict) else None)
    tpath = transcript_for_session(target["session_id"], projects_dir)
    return {"task": task, "record": rec_rel, "session_id": target["session_id"], "name": target.get("recipient"), "authorised_by": pointer,
            "marker_present": bool(tpath and cached_binding(tpath) == task),
            "next": f"the new host writes the plain line `MANDATE_BOUND: {task}` in its own text, then CronList; the ONE recall is created only if no job carries its mark. Commit the record."}


def open_tasks(root: Path) -> list[str]:
    """Mandates of every actor with an OPEN queue, or a recently touched COMPLETE queue.

    Delivery still needs an explicitly bound Claude Code session; a record directory
    is not an identity or permission to start one.
    """
    ids = set()
    for p in sorted((root / "ledger" / "tasks").glob("*/*.json")):
        try:
            rec = json.loads(p.read_text(encoding="utf-8"))
            blocks = [mc.block_state(b) for _, b in mc.load_blocks(rec)]
            recent = time.time() - p.stat().st_mtime < 3 * 86400
            if "OPEN" in blocks or ("COMPLETE" in blocks and recent):     # a recent COMPLETE may still lack its push
                ids.add(str(rec.get("TASK_ID") or p.stem))
        except (OSError, ValueError, mc.Malformed, AttributeError):
            continue
    return sorted(ids)


def registered_worktrees(root: Path) -> list[Path]:
    """Registered views of this repository, not arbitrary directories on the host."""
    roots = [root]
    try:
        result = subprocess.run(["git", "-C", str(root), "worktree", "list", "--porcelain"],
                                capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if line.startswith("worktree "):
                    tree = Path(line[len("worktree "):])
                    if tree.is_dir() and tree not in roots:
                        roots.append(tree)
    except (OSError, subprocess.SubprocessError):
        pass
    return roots


def published_copies(root: Path, trees: list[Path], task: str, ref: str = "development/main") -> list[str]:
    """Which of the record paths found in `trees` the published ref carries. Used only to say WHY a task is ambiguous: a record that
    landed on the published ref but is absent from a root checkout that lags behind it shows up as several unmerged copies, and the fix
    is to advance the root (merge --ff-only), not to guess a winner."""
    found = []
    for tree in trees:
        for p in mc.find_records(tree, task):
            rel = p.relative_to(tree).as_posix()
            try:
                r = subprocess.run(["git", "-C", str(root), "cat-file", "-e", f"{ref}:{rel}"], capture_output=True, timeout=10)
            except (OSError, subprocess.SubprocessError):
                continue
            if r.returncode == 0 and rel not in found:
                found.append(rel)
    return found


def note_checkout_behind(root: Path, ref: str = "development/main", say: bool = True) -> list[str]:
    """The watch classifies records read from `root`. When `root` is behind the published ref on task records, say it (2026-11-25: root stayed 1,535 commits behind for four days and one
    resume carried a stale step count). No fetch: the ref is as the last fetch left it. Logged once per set of files, printed at every run. Never changes a classification."""
    if not (root / ".git").exists():
        return []                                                  # not a checkout: nothing to compare with, and no process to start
    touched = mc.files_behind(root, ref, (":(glob)ledger/tasks/*/*.json",)) or []
    if _load("checkout-behind") != {"files": touched}:
        _save("checkout-behind", {"files": touched})
        if touched:
            log_event("checkout_behind", root=str(root), files=touched[:10], count=len(touched))
    if touched and say:
        print(f"CHECKOUT_BEHIND {root}: {len(touched)} task record(s) are older here than on {ref} ({', '.join(touched[:3])}{', …' if len(touched) > 3 else ''}); "
              "records read from here may be stale (the campaign home is advanced with `strategic_advisor.py refresh`)")
    return touched


def _check_all(a) -> int:
    sessions = list_sessions()
    results = []
    root = Path(a.root)
    note_checkout_behind(root, say=not getattr(a, "json", False))
    candidates = {}
    for tree in registered_worktrees(root):
        for task in open_tasks(tree):
            candidates.setdefault(task, []).append(tree)
    for task, trees in sorted(candidates.items()):
        # Main's record wins over stale OPEN copies in old worktrees (including PAUSED
        # or CANCELLED main records). A new, uniquely located task can be watched before
        # landing; identity still requires its own transcript binding in check().
        if mc.find_records(root, task):
            record_root = root
        elif len(trees) == 1:
            record_root = trees[0]
        else:
            out = {"task": task, "state": "UNKNOWN", "action": "NONE",
                   "why": "multiple unmerged task records; no authoritative root copy",
                   "record_roots": [str(t) for t in trees]}
            landed = published_copies(root, trees, task)
            if landed:
                out["why"] += (f"; the record IS on the published ref ({landed[0]}) and the root checkout lacks it: advance the root with "
                               "`git merge --ff-only development/main` (nothing is guessed here), after which this record is watched")
                out["published"] = True
            results.append(out)
            log_event("check", **out)
            continue
        out = check(task, root=record_root, deliver=a.deliver, quiet_minutes=a.quiet_minutes,
                    sessions=sessions, resume_args=tuple(a.resume_arg))
        out["record_root"] = str(record_root)
        names = session_name_state(task, sessions)
        out["session_names"] = names
        name_key = "session-names-" + task
        changed_names = a.deliver == "resume" and _load(name_key) != names
        if changed_names:
            _save(name_key, names)
        if names["state"] == "PENDING":
            if changed_names:
                log_event("session_names_pending", **names)
            if not getattr(a, "json", False):
                print(f"SESSION_NAMES_PENDING {task}: " + json.dumps(names["renames"], ensure_ascii=False))
        if out.get("state") in RETIRE_STATES:
            retirements = retire_released(task, sessions, execute=a.deliver == "resume")
            if retirements:
                out["predecessor_retirement"] = retirements
                if not getattr(a, "json", False):
                    for r in retirements:
                        if r["verdict"] in ("RETIRED", "STOP_REFUSED", "STOP_UNVERIFIED") and not r.get("retry_suppressed"):
                            print(f"{r['verdict']} predecessor {r['old_session']}: {r['reason']}")
        results.append(out)
        if not getattr(a, "json", False) and out["action"] == "RESUME":
            print(f"{out['state']} {out['action']} {task}: {out['why']}" + (f" [{out['delivery']}]" if out.get("delivery") else ""))
    if getattr(a, "json", False):
        print(json.dumps(results, indent=2, sort_keys=True))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="classify the mandate and, when allowed, request a restart")
    c.add_argument("--task", help="a TASK_ID; --all checks mandates of every actor")
    c.add_argument("--all", action="store_true", help="check mandates under every actor in ledger/tasks/*/")
    c.add_argument("--deliver", choices=("none", "resume"), default="none")
    c.add_argument("--quiet-minutes", type=int, default=QUIET_MINUTES)
    c.add_argument("--resume-arg", action="append", default=[], help="extra claude option for the revival command, e.g. --permission-mode (never a permission bypass)")
    c.add_argument("--self-call", action="store_true", help="the session itself (in-session cron) asks")
    c.add_argument("--json", action="store_true")
    c.add_argument("--root", default=str(ROOT))
    jb = sub.add_parser("job", help="start, list or collect a long background job of a mandate")
    jsub = jb.add_subparsers(dest="jcmd", required=True)
    jr = jsub.add_parser("run", help="start detached and tagged; idempotent per label")
    jr.add_argument("--task", required=True)
    jr.add_argument("--label", required=True)
    jr.add_argument("--cwd")
    jr.add_argument("--memory-max", help="opt-in hard memory cap for this job (3G, 800M): runs it in its own systemd user scope")
    jr.add_argument("jobcmd", nargs=argparse.REMAINDER)
    jl = jsub.add_parser("list")
    jl.add_argument("--task", required=True)
    jc = jsub.add_parser("collect", help="mark a finished job as collected")
    jc.add_argument("--task", required=True)
    jc.add_argument("--id", required=True)
    rt = sub.add_parser("route", help="resolve a name, role alias or session id to one live session; with --first-line compare the recipients a message names with the sends actually made")
    rt.add_argument("--to", action="append", required=True, help="a recipient actually used (repeat once per send), or the target to resolve")
    rt.add_argument("--first-line", default="", help="the message's first line, e.g. 'IT to ADV and HE: ...'")
    rt.add_argument("--root", default=str(ROOT))
    rb = sub.add_parser("rebind", help="operator-authorised transfer of a mandate's host role to a live substitute session (explicit authorisation pointer required)")
    rb.add_argument("--task", required=True)
    rb.add_argument("--to", required=True, help="the substitute: a session id, its name, or a role alias")
    rb.add_argument("--authorised-by", default="", help="where the operator authorised the substitute (message, roadmap entry, record line)")
    rb.add_argument("--root", default=str(ROOT))
    rl = sub.add_parser("released", help="has the OLD session released this task? (a successor's check, by session id: MISSING, NEVER_BOUND, BOUND or RELEASED; exit 0 only for RELEASED)")
    rl.add_argument("--session", required=True, help="the old session's id (the transcript is found by id, in whichever project folder it lives)")
    rl.add_argument("--task", required=True)
    nl = sub.add_parser("labels", help="read-only CURRENT/PREVIOUS name reconciliation; binding determines the host, never the label")
    nl.add_argument("--task", required=True)
    ho = sub.add_parser("handoff", help="verify a restart; read-only unless --retire-old is explicitly requested")
    ho.add_argument("--task", required=True)
    ho.add_argument("--old", required=True, help="the predecessor's FULL session id")
    ho.add_argument("--new", required=True, help="the successor's session id (a unique prefix of at least 8 characters is enough)")
    ho.add_argument("--within", type=int, default=5, help="minutes a bound successor may take for its first tool call before it is STALLED")
    ho.add_argument("--wait", type=int, default=0, help="seconds to keep checking until RUNNING or STALLED (default: one look)")
    ho.add_argument("--retire-old", action="store_true", help="after RUNNING, stop only an eligible released background predecessor; preserve conversation and worktree")
    rs = sub.add_parser("resources", help="observed memory, pressure, swap, the cgroups holding most RSS and the live jobs (read-only, no thresholds)")
    rs.add_argument("--top", type=int, default=8)
    e = sub.add_parser("events", help="what the watch decided on this machine")
    e.add_argument("--last", type=int, default=20)
    a = ap.parse_args(argv)
    if a.cmd == "job":
        if a.jcmd == "run":
            cmd = a.jobcmd[1:] if a.jobcmd and a.jobcmd[0] == "--" else a.jobcmd
            if not cmd:
                ap.error("job run needs a command after --")
            try:
                started = job_run(a.task, a.label, cmd, a.cwd, a.memory_max)
            except (ValueError, RuntimeError) as exc:
                print(f"REFUSED: {exc}", file=sys.stderr)
                return 2
            print(json.dumps({k: v for k, v in started.items() if k != "_file"}, sort_keys=True))
        elif a.jcmd == "list":
            for j in load_jobs(a.task):
                print(f"{j['id']}\t{j['state']}\tpid={j['pid']}\t{'collected' if j.get('collected') else 'open'}\t{' '.join(j['cmd'])[:80]}")
        else:
            print("collected" if job_collect(a.task, a.id) else "not found")
        return 0
    if a.cmd == "released":
        path = transcript_for_session(a.session)
        state = mc.marker_state(path, a.task) if path else "MISSING"
        print(f"{state} (session {a.session[:8]}, task {a.task}" + (f", {path}" if path else ", no transcript found for that id (a short id works only as a unique prefix of at least 8 characters)") + ")")
        near = find_near_release(path, a.task) if state == "BOUND" else None
        if near:
            print(f"NEAR_MISS: it wrote `{near['line']}` at {near['at'][:19]}, which releases nothing; that session must write, alone on its line: MANDATE_RELEASED: {a.task}")
        return 0 if state == "RELEASED" else (2 if state == "MISSING" else 1)
    if a.cmd == "labels":
        print(json.dumps(session_name_state(a.task, list_sessions()), indent=1, ensure_ascii=False))
        return 0
    if a.cmd == "handoff":
        deadline = time.time() + a.wait
        while True:
            now = datetime.now(timezone.utc)
            res = handoff_state(a.task, transcript_for_session(a.old), transcript_for_session(a.new), now, a.within, list_sessions(), a.new)
            if res["verdict"] in ("RUNNING", "STALLED", "BOTH_BOUND", "NEW_NOT_FOUND") or time.time() >= deadline:
                break
            time.sleep(15)
        if res["verdict"] == "RUNNING":
            old_path, new_path = transcript_for_session(a.old), transcript_for_session(a.new)
            old_id, new_id = (old_path.stem if old_path else a.old), (new_path.stem if new_path else a.new)
            inventory = list_sessions()
            res["session_names"] = session_name_state(a.task, inventory)
            res["predecessor_retirement"] = retire_predecessor(a.task, old_id, new_id, execute=a.retire_old)
            retired = res["predecessor_retirement"]["verdict"]
            res["legacy_bound_tasks"] = legacy_bound_tasks(a.task, old_path)
            res["next"] = handoff_next(retired, res["session_names"], res["legacy_bound_tasks"], any(r.get("sessionId") == old_id for r in (inventory or [])))
            if a.retire_old and res["predecessor_retirement"]["verdict"] not in ("RETIRED", "ALREADY_STOPPED"):
                print(json.dumps(res, indent=1, sort_keys=True, ensure_ascii=False))
                return 5
        print(json.dumps(res, indent=1, sort_keys=True, ensure_ascii=False))
        return {"RUNNING": 0, "STALLED": 4, "BOTH_BOUND": 3, "NEW_NOT_FOUND": 2}.get(res["verdict"], 1)
    if a.cmd == "resources":
        print(json.dumps(resource_state(top=a.top, sessions=list_sessions()), indent=1, sort_keys=True))
        return 0
    if a.cmd == "rebind":
        try:
            print(json.dumps(rebind(a.task, a.to, a.authorised_by, root=Path(a.root)), indent=1, sort_keys=True, ensure_ascii=False))
        except PermissionError as exc:
            print(f"REFUSED: {exc}", file=sys.stderr)
            return 3
        except (ValueError, OSError) as exc:
            print(f"REFUSED: {exc}", file=sys.stderr)
            return 2
        return 0
    if a.cmd == "route":
        sessions = list_sessions()
        res = check_recipients(a.first_line, a.to, sessions, Path(a.root)) if a.first_line else {t: route(t, sessions, Path(a.root)) for t in a.to}
        print(json.dumps(res, indent=1, sort_keys=True))
        bad = res.get("verdict", "OK") != "OK" if a.first_line else any(r["status"] != "RESOLVED" for r in res.values())
        return 2 if bad else 0
    if a.cmd == "events":
        p = state_dir() / EVENTS_FILE
        lines = p.read_text(encoding="utf-8").splitlines()[-a.last:] if p.exists() else []
        print("\n".join(lines) if lines else "no events")
        return 0
    if a.all:
        return _check_all(a)
    if not a.task:
        ap.error("--task or --all is required")
    out = check(a.task, root=Path(a.root), deliver=a.deliver, quiet_minutes=a.quiet_minutes, self_call=a.self_call, resume_args=tuple(a.resume_arg))
    if a.json:
        print(json.dumps(out, sort_keys=True))
    elif out["state"] != "RUNNING" and not (out["action"] == "NONE" and out["state"] in ("COMPLETE", "PAUSED")):
        # silent when running, complete or paused; one line otherwise
        print(f"{out['state']} {out['action']} {out['task']}: {out['why']}" + (f" [{out['delivery']}]" if out.get("delivery") else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
