#!/usr/bin/env python3
"""Hourly watch over an open Orchestrator mandate: is the authorised work running, and if it
stopped while work remains, ask the bound session to continue.

    python3 framework/scripts/mandate_watch.py check --task ORCH-ROADMAP-IT4-20261028
    python3 framework/scripts/mandate_watch.py check --task <ID> --deliver none --json
    python3 framework/scripts/mandate_watch.py events [--last N]

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
  STOPPED_RESUMABLE  record verdict CONTINUE, session idle (or dead) for longer than
                     --quiet-minutes, and no request pending for the current queue state.
  PAUSED / COMPLETE  the record releases the mandate (MANDATE_STATE PAUSED / CANCELLED /
                     COMPLETE, or every step DONE). Never restarted.
  BLOCKED            ALL_BLOCKED: the cause is kept in the log; independent steps would already
                     make the verdict CONTINUE, so they are not held back by a blocked one.
  UNKNOWN            no bound session found, the session list is unreadable, or the record is
                     malformed. Nothing is started on a hypothesis; the limit is logged.

The absence of recent commits proves nothing about stopped work and is never read.
Identity comes from the record and from the session's own `MANDATE_BOUND: <TASK_ID>` line
(mandate_continuity.py), never from a directory or a process name.
What this does NOT guarantee: that the resumed model chooses well, quota, or a session whose
host is powered off.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
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
REREQUEST_MINUTES = 180       # a pending request with no progress is repeated no sooner than this
EVENTS_FILE = "events.jsonl"
EVENTS_MAX_BYTES = 256 * 1024


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
def list_sessions() -> list[dict] | None:
    """Live sessions from the runtime's own listing; None when it cannot be read."""
    try:
        out = subprocess.run([claude_bin(), "agents", "--json"], capture_output=True, text=True, timeout=60)
        data = json.loads(out.stdout)
        return data if isinstance(data, list) else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


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
        if mc.binding_from_transcript(p) == task:
            return p
    return None


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


def last_activity(transcript: Path, tasks_root: Path | None = None, include_transcript: bool = True, before: float | None = None) -> float:
    """Latest mtime of the transcript and of that session's background-task output files.
    A session calling the check on itself (the in-session cron) leaves its own transcript out:
    its turn is the request, and counting it would always read as activity."""
    latest = 0.0
    if include_transcript:
        try:
            latest = transcript.stat().st_mtime
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


# ---------------------------------------------------------------- the decision (pure)
def classify(status: dict, session: dict | None, session_list_ok: bool, bound: bool,
             idle_seconds: float | None, pending: dict, signature: str, now: float,
             quiet_minutes: int = QUIET_MINUTES) -> dict:
    """Return {state, action, why}. action is RESUME or NONE. No I/O."""
    v = status.get("verdict")
    if v in ("COMPLETE_PENDING",) or v == "RELEASED":
        msg = status.get("message", "")
        state = "PAUSED" if "PAUSED" in msg.upper() or "CANCELLED" in msg.upper() else "COMPLETE"
        return {"state": state, "action": "NONE", "why": f"record verdict {v}"}
    if v == "ALL_BLOCKED":
        return {"state": "BLOCKED", "action": "NONE", "why": status.get("message", "all steps blocked")}
    if v != "CONTINUE":
        return {"state": "UNKNOWN", "action": "NONE", "why": f"record verdict {v}: {status.get('message', '')}"[:300]}
    if not bound:
        return {"state": "UNKNOWN", "action": "NONE", "why": "no session transcript carries MANDATE_BOUND for this task"}
    if not session_list_ok:
        return {"state": "UNKNOWN", "action": "NONE", "why": "the session listing could not be read"}
    if session is not None and session.get("status") == "busy":
        return {"state": "RUNNING", "action": "NONE", "why": "session busy"}
    if idle_seconds is not None and idle_seconds < quiet_minutes * 60:
        return {"state": "RUNNING", "action": "NONE", "why": f"activity {int(idle_seconds // 60)} min ago (quiet threshold {quiet_minutes})"}
    last = pending.get("requested_at")
    if last and pending.get("signature") == signature and now - last < REREQUEST_MINUTES * 60:
        return {"state": "STOPPED_RESUMABLE", "action": "NONE", "why": "a request is already pending for this queue state"}
    return {"state": "STOPPED_RESUMABLE", "action": "RESUME",
            "why": "session " + ("absent from the live listing" if session is None else "idle") +
                   f" and silent, authorised work remains ({status.get('message', '')[:120]})"}


def request_text(task: str, status: dict, record_path: str = "") -> str:
    where = f" The record is {record_path}." if record_path else ""
    return (f"Mandate {task} is open with authorised work remaining ({status.get('message', '')[:200]}).{where} "
            "Hourly watch: the session had stopped. Resume from the checkpoint in the mandate record, "
            "choose the next useful authorised step yourself, and keep going until the record releases "
            "the mandate. Do not ask the operator for anything the mandate already authorises.")


# ---------------------------------------------------------------- command
def check(task: str, *, root: Path = ROOT, deliver: str = "none", quiet_minutes: int = QUIET_MINUTES, resume_args: tuple = (),
          projects_dir: Path | None = None, tasks_root: Path | None = None,
          sessions: list[dict] | None = None, now: float | None = None, runner=None, self_call: bool = False) -> dict:
    now = time.time() if now is None else now
    status = mc.status_for(root, task)
    rec_rel = status.get("record")
    signature = mc._queue_signature(root, rec_rel)
    transcript = find_bound_transcript(task, projects_dir)
    live = sessions if sessions is not None else list_sessions()
    sid = transcript.stem if transcript else None
    session = next((s for s in (live or []) if s.get("sessionId") == sid), None) if sid else None
    if self_call and session is not None:
        session = dict(session, status="idle")      # the caller's own turn is not "busy work"
    if self_call and transcript:
        start = turn_start(transcript) or now
        act = last_activity(transcript, tasks_root, include_transcript=False, before=start)
        idle = (start - act) if act else None       # activity before the asking turn began
    else:
        idle = (now - last_activity(transcript, tasks_root)) if transcript else None
    pend = _load(task)
    out = classify(status, session, live is not None, transcript is not None, idle, pend, signature, now, quiet_minutes)
    out.update({"task": task, "session": sid, "signature": signature[:12]})
    if out["action"] == "RESUME" and deliver == "resume":
        if session is not None:
            out["delivery"] = "not sent: the session is alive; the in-session cron delivers to a live session"
        else:
            cmd = [claude_bin(), "--bg", *resume_args, "--resume", sid, request_text(task, status, str(root / rec_rel) if rec_rel else "")]
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
    if out["state"] != "RUNNING" or out.get("delivery"):
        log_event("check", **{k: out[k] for k in ("task", "state", "action", "why") if k in out}, delivery=out.get("delivery"))
    return out


def open_tasks(root: Path) -> list[str]:
    """TASK_IDs of orchestrator records that still hold an OPEN queue block."""
    ids = []
    for p in sorted((root / "ledger" / "tasks" / "orchestrator").glob("*.json")):
        try:
            rec = json.loads(p.read_text(encoding="utf-8"))
            if any(mc.block_state(b) == "OPEN" for _, b in mc.load_blocks(rec)):
                ids.append(str(rec.get("TASK_ID") or p.stem))
        except (OSError, ValueError, mc.Malformed, AttributeError):
            continue
    return ids


def _check_all(a) -> int:
    sessions = list_sessions()
    for task in open_tasks(Path(a.root)):
        out = check(task, root=Path(a.root), deliver=a.deliver, quiet_minutes=a.quiet_minutes,
                    sessions=sessions, resume_args=tuple(a.resume_arg))
        if out["action"] == "RESUME":      # UNKNOWN / BLOCKED / RUNNING are logged by check(), not printed
            print(f"{out['state']} {out['action']} {task}: {out['why']}" + (f" [{out['delivery']}]" if out.get("delivery") else ""))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="classify the mandate and, when allowed, request a restart")
    c.add_argument("--task", help="a TASK_ID; with --all every open orchestrator record is checked")
    c.add_argument("--all", action="store_true")
    c.add_argument("--deliver", choices=("none", "resume"), default="none")
    c.add_argument("--quiet-minutes", type=int, default=QUIET_MINUTES)
    c.add_argument("--resume-arg", action="append", default=[], help="extra claude option for the revival command, e.g. --permission-mode (never a permission bypass)")
    c.add_argument("--self-call", action="store_true", help="the session itself (in-session cron) asks")
    c.add_argument("--json", action="store_true")
    c.add_argument("--root", default=str(ROOT))
    e = sub.add_parser("events", help="what the watch decided on this machine")
    e.add_argument("--last", type=int, default=20)
    a = ap.parse_args(argv)
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
