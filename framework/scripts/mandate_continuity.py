#!/usr/bin/env python3
"""Reconcile an Orchestrator mandate from its durable record, and keep the session on it.

Four commands, one source of truth — the `AUTHORISED_QUEUE*` block of an Annex A task record
under `ledger/tasks/<actor>/<TASK_ID>.json` (schema: Annex A.1c):

    python3 framework/scripts/mandate_continuity.py status --task ALDAZ-EXEC-20260913
    python3 framework/scripts/mandate_continuity.py normalise --task <TASK_ID> [--write]
    python3 framework/scripts/mandate_continuity.py stop-hook      # Claude Code Stop hook
    python3 framework/scripts/mandate_continuity.py events [--last N]   # what the hook did

`status` prints the verdict the continuity procedure needs at bootstrap, after every milestone
and after every compaction or recall (cross_session_transport.md §12): CONTINUE with the next
executable step, ALL_BLOCKED with the named impediments, COMPLETE_PENDING when every step is
DONE with evidence, RELEASED when the record's MANDATE_STATE closes or pauses the mandate, or
MALFORMED when the record cannot be trusted to say either.

`stop-hook` is the runtime half. Claude Code calls it whenever the session is about to end its
turn. It reads the hook payload on stdin, looks in the session's own transcript for the last
binding marker an actor or the operator wrote as a plain-text LINE of its own —

    MANDATE_BOUND: <TASK_ID>        binds this session to that record
    MANDATE_RELEASED: <TASK_ID>     unbinds it

— computes the verdict from the record on disk, and BLOCKS the turn from ending while the
verdict is CONTINUE or MALFORMED, handing the session the next step or the repair. A session
that is bound by no marker and no launcher is never touched. A launcher (an operator, a
scheduled routine) can bind an unattended session without depending on the model to write a
marker, by starting it with `LEGEND_MANDATE_TASK=<TASK_ID>` in its environment; that session is
then held to the record's verdict exactly as a marker-bound one is, and is released by the
record (MANDATE_STATE), not by a marker. The block is bounded: after `MAX_CONSECUTIVE_BLOCKS`
blocks with no change to the queue's statuses and no new commit, the stop is allowed through
and the count is reported, so a session that genuinely cannot progress is not trapped. If the
count cannot be persisted the stop is allowed, because an unbounded block is worse than a
missed one. Any error fails OPEN.

Reading rules, fixed because they are where the 2026-09-14 queue closed itself: a bare string
step is unreconciled and counts TODO; a BLOCKED step without a named blocker is not blocked;
a DONE step without evidence is a finding, and when nothing else remains it holds the session
for the pointer (EVIDENCE_PENDING), not for the work; an objective with no `steps` key, a
`steps` that is not a list, or a step that is not a string or an object, makes the record
MALFORMED rather than empty; MANDATE_STATE COMPLETE that contradicts its steps is
INCONSISTENT_COMPLETE and holds, while PAUSED and CANCELLED release against any state. Every
OPEN queue block binds — their steps add up, and key order extinguishes nothing. Status tokens
are compared case- and whitespace-insensitively. Progress that resets the consecutive block
count is a status or evidence change in the queue, never a commit; an absolute per-session
ceiling holds regardless (Codex review, 2026-09-14).

The Junior Harness Engineer's blind review of the first version (2026-09-14) found the loop
that an unwritable state directory made unbounded, the release marker the hook's own reason
carried back into the transcript, and the whole-file hash that a logged stop reset; each is a
test below now.

Everything the hook decides about a bound session, and every error or unreadable transcript,
is appended to `events.jsonl` in its state directory (machine-local, never in the repository,
rotated at 256 KB), because a hook that fails open fails silently and a silent hook cannot be
measured. `events` summarises it: blocks issued, stops let through and why, errors, unparseable
transcripts. A hook that has only ever logged errors is broken, not quiet.

Runtime scope: `status`, `normalise` and the record schema are runtime-agnostic and any runtime
can call them. `stop-hook` is the Claude Code adapter: it reads the Claude Code hook payload and
transcript format. Another runtime needs its own adapter over `status`.

What this does NOT guarantee: model compliance after the last block, runtime liveness, quota.
It is a repository hook, opt-in per session by marker or by launcher, and it enforces the
mandate record — not §21c, which remains procedural guidance and reserved text.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QUEUE_PREFIX = "AUTHORISED_QUEUE"
OBJECTIVE_PREFIX = "OBJ_"
STEP_STATUSES = ("TODO", "IN_PROGRESS", "DONE", "BLOCKED")
RELEASED_STATES = ("COMPLETE", "PAUSED", "CANCELLED")
MAX_CONSECUTIVE_BLOCKS = 3
MAX_TOTAL_BLOCKS = 12   # per session and mandate; progress resets the consecutive count, not this
# A marker is a line of its own: nothing but the token, the id and whitespace. A quoted or
# negated mention inside a sentence ("do NOT write MANDATE_BOUND: T-1 yet") does not bind.
MARKER_RE = re.compile(r"^\s*MANDATE_(BOUND|RELEASED):\s*([A-Za-z0-9][A-Za-z0-9_.-]*)\s*$", re.M)
DISABLE_ENV = "LEGEND_MANDATE_HOOK"
BIND_ENV = "LEGEND_MANDATE_TASK"   # a launcher binds an unattended session; no model cooperation
TASK_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
EVENTS_FILE = "events.jsonl"
EVENTS_MAX_BYTES = 256 * 1024
# Words that look like evidence and point at nothing (Junior review 2, D5).
# Only the unambiguous ones: a false hold costs more than a rare false pass, and the record's
# honesty is the actor's obligation — the schema refuses a non-pointer, not a weak one.
EVIDENCE_PLACEHOLDERS = frozenset({"null", "none", "nil", "tbd", "todo", "pending", "n/a",
                                   "na", "-", "--", "?"})


class Malformed(ValueError):
    """The record cannot be trusted to say whether work remains."""


# ---------------------------------------------------------------- record and queue
def find_records(root: Path, task_id: str) -> list[Path]:
    return sorted((root / "ledger" / "tasks").glob(f"*/{task_id}.json"))


def find_record(root: Path, task_id: str) -> Path | None:
    """One record, or none. Two records with the same TASK_ID under different actors are
    ambiguous and stay ambiguous. An earlier version preferred the Orchestrator's copy, which
    silently picked a winner where §12 asks for MALFORMED — and a decoy placed under the
    preferred directory then released a real queue (Junior review 2, D4, 2026-09-17)."""
    matches = find_records(root, task_id)
    return matches[0] if len(matches) == 1 else None


def _token(value, allowed: tuple[str, ...], default: str) -> str | None:
    """Uppercase, stripped; None when the token is not in the allowed set."""
    text = str(value if value is not None else default).strip().upper()
    return text if text in allowed else None


def block_state(block: dict) -> str:
    """The block's own state. An unknown token is not a state."""
    state = _token(block.get("MANDATE_STATE"), RELEASED_STATES + ("OPEN",), "OPEN")
    if state is None:
        raise Malformed(f"MANDATE_STATE {block.get('MANDATE_STATE')!r} is not one of "
                        f"OPEN / {' / '.join(RELEASED_STATES)}")
    return state


def load_blocks(record) -> list[tuple[str, dict]]:
    """Every AUTHORISED_QUEUE* block, in key order, whatever its state — each is judged on its
    own. A string under such a key is free text when a real block stands beside it, and a
    prose queue when it does not (Junior review 2, M11)."""
    if not isinstance(record, dict):
        raise Malformed("record is not a JSON object")
    keys = sorted(k for k in record if k.startswith(QUEUE_PREFIX))
    blocks = [(k, record[k]) for k in keys if isinstance(record[k], dict)]
    if not blocks and keys:
        raise Malformed(f"{keys[-1]} is not an object")
    for _, block in blocks:
        block_state(block)
    return blocks


def load_queue(record) -> tuple[str | None, dict | None]:
    """The last block, for the callers that need one: `normalise` and nothing that decides."""
    blocks = load_blocks(record)
    return blocks[-1] if blocks else (None, None)


def load_active_queues(record) -> list[tuple[str, dict]]:
    """The blocks that still bind: every one whose own state is OPEN. Key order extinguishes
    nothing — a later block with every step DONE does not close an earlier one (Codex review,
    2026-09-14) — and a released block is not a place to hide an open one (Junior review 2)."""
    return [(k, b) for k, b in load_blocks(record) if block_state(b) == "OPEN"]


def _is_evidence(value) -> bool:
    """A durable pointer: a non-empty string that is not a placeholder word, or a list holding
    one. A boolean and a number are never pointers (Junior review 2, D5)."""
    if isinstance(value, (list, tuple)):
        return any(_is_evidence(v) for v in value)
    if isinstance(value, str):
        text = value.strip()
        return bool(text) and text.lower() not in EVIDENCE_PLACEHOLDERS
    return False


def _normalise_step(objective: str, index: int, raw) -> dict:
    if isinstance(raw, str):
        return {"objective": objective, "index": index, "step": raw, "status": "TODO",
                "unreconciled": True}
    if not isinstance(raw, dict):
        raise Malformed(f"{objective}.steps[{index}] is neither a string nor an object")
    step = dict(raw)
    step["objective"] = objective
    step["index"] = index
    step["step"] = str(step.get("step", ""))
    status = _token(step.get("status"), STEP_STATUSES, "TODO")
    if status is None:
        step["invalid_status"] = str(step.get("status"))
        status = "TODO"
    if status == "BLOCKED" and not str(step.get("blocker") or "").strip():
        step["blocked_without_blocker"] = True
        status = "TODO"
    if status == "DONE" and not _is_evidence(step.get("evidence")):
        step["done_without_evidence"] = True
    step["status"] = status
    return step


def iter_steps(queue: dict, prefix: str = "") -> list[dict]:
    objectives = []
    for name, value in queue.items():
        # Objective names are matched the way every other token is, case- and
        # whitespace-insensitively; and anything that carries `steps` while wearing another
        # name is named wrongly, not absent. Silently skipping either made a whole objective
        # and its pending steps vanish from the count (Junior review 2, D2).
        if not name.strip().upper().startswith(OBJECTIVE_PREFIX):
            if isinstance(value, dict) and "steps" in value:
                raise Malformed(f"{name!r} carries `steps` but is not named {OBJECTIVE_PREFIX}*")
            continue
        if not isinstance(value, dict):
            raise Malformed(f"{name} is not an object")
        order = value.get("order", 1 << 30)
        if not isinstance(order, (int, float)) or isinstance(order, bool):
            raise Malformed(f"{name}.order is not a number")
        objectives.append((order, name, value))
    objectives.sort(key=lambda t: (t[0], t[1]))
    steps: list[dict] = []
    for _, name, objective in objectives:
        # An objective without `steps` is not empty, it is unwritten: it must not vanish from
        # the count (Codex review, 2026-09-14). An explicit `steps: []` is a deliberate empty.
        if "steps" not in objective:
            raise Malformed(f"{name} has no `steps` (write `steps: []` for a deliberately empty objective)")
        raw_steps = objective["steps"]
        if not isinstance(raw_steps, list):
            raise Malformed(f"{name}.steps is not a list")
        for i, raw in enumerate(raw_steps):
            steps.append(_normalise_step(prefix + name, i, raw))
    return steps


def iter_all_steps(queues: list[tuple[str, dict]]) -> list[dict]:
    if len(queues) == 1:
        return iter_steps(queues[0][1])
    steps: list[dict] = []
    for key, queue in queues:
        steps.extend(iter_steps(queue, prefix=f"{key}/"))
    return steps


def verdict(record) -> dict:
    task_id = record.get("TASK_ID", "?") if isinstance(record, dict) else "?"
    try:
        blocks = load_blocks(record)
        if not blocks:
            return {"task": task_id, "verdict": "NO_QUEUE", "stop_allowed": True,
                    "message": "record carries no AUTHORISED_QUEUE block"}
        all_steps = iter_all_steps(blocks)
        # Each block answers for its OWN state. An earlier version read the state off one
        # block and dropped the released ones whenever any sibling was open, so a COMPLETE
        # block with pending steps was never checked once a second block existed — one JSON
        # line bought a stop (Junior review 2, D1).
        contradicted = []
        for key, block in blocks:
            if block_state(block) != "COMPLETE":
                continue
            own = iter_steps(block)
            counts_bad = (sum(1 for s in own if s["status"] in ("TODO", "IN_PROGRESS")),
                          sum(1 for s in own if s.get("done_without_evidence")),
                          sum(1 for s in own if s["status"] == "BLOCKED"))
            if any(counts_bad):
                contradicted.append((key, *counts_bad))
        active = [(k, b) for k, b in blocks if block_state(b) == "OPEN"]
        steps = iter_all_steps(active)
    except Malformed as exc:
        return {"task": task_id, "verdict": "MALFORMED", "stop_allowed": False,
                "message": f"the record cannot say whether work remains — repair it: {exc}"}
    if contradicted:
        detail = "; ".join(f"{k}: {ex} executable, {ev} DONE without evidence, {bl} BLOCKED"
                           for k, ex, ev, bl in contradicted)
        return {"task": task_id, "verdict": "INCONSISTENT_COMPLETE", "stop_allowed": False,
                "steps_total": len(all_steps), "findings": [], "unreconciled": 0,
                "counts": {s: sum(1 for st in all_steps if st["status"] == s) for s in STEP_STATUSES},
                "message": (f"MANDATE_STATE COMPLETE contradicts its own steps — {detail}. Mark "
                            "every step truthfully, or set PAUSED / CANCELLED if the mandate is "
                            "not being completed; a mandate with a demonstrable impediment stays "
                            "INCOMPLETE")}
    if not active:
        pending = [st for st in all_steps if st["status"] in ("TODO", "IN_PROGRESS")]
        state = block_state(blocks[-1][1])
        return {"task": task_id, "queue_key": [k for k, _ in blocks], "mandate_state": state,
                "steps_total": len(all_steps), "findings": [], "unreconciled": 0,
                "counts": {s: sum(1 for st in all_steps if st["status"] == s) for s in STEP_STATUSES},
                "verdict": "RELEASED", "stop_allowed": True,
                "message": (f"MANDATE_STATE {state}: the mandate is not executing"
                            + (f"; NOTE {len(pending)} executable step(s) remain under a released "
                               "state" if pending else ""))}
    queue_key = active[0][0] if len(active) == 1 else [k for k, _ in active]
    state = "OPEN"
    counts = {s: sum(1 for st in steps if st["status"] == s) for s in STEP_STATUSES}
    unevidenced = [st for st in steps if st.get("done_without_evidence")]
    findings = [f"{st['objective']}[{st['index']}] DONE without evidence" for st in unevidenced]
    findings += [f"{st['objective']}[{st['index']}] BLOCKED without a named blocker, counted TODO"
                 for st in steps if st.get("blocked_without_blocker")]
    findings += [f"{st['objective']}[{st['index']}] invalid status {st['invalid_status']!r}, counted TODO"
                 for st in steps if st.get("invalid_status")]
    unreconciled = sum(1 for st in steps if st.get("unreconciled"))
    executable = [st for st in steps if st["status"] in ("TODO", "IN_PROGRESS")]
    base = {"task": task_id, "queue_key": queue_key, "mandate_state": state, "counts": counts,
            "unreconciled": unreconciled, "findings": findings, "steps_total": len(steps)}
    if executable:
        nxt = next((st for st in executable if st["status"] == "IN_PROGRESS"), executable[0])
        return {**base, "verdict": "CONTINUE", "stop_allowed": False,
                "executable": len(executable),
                "next": {"objective": nxt["objective"], "index": nxt["index"],
                         "status": nxt["status"], "step": nxt["step"]},
                "message": (f"{len(executable)} executable step(s) remain; next: "
                            f"{nxt['objective']}[{nxt['index']}] {nxt['step']}")}
    blocked = [st for st in steps if st["status"] == "BLOCKED"]
    # An unevidenced DONE step outranks a blocker elsewhere: writing a durable pointer is never
    # blocked by someone else's impediment, and ALL_BLOCKED would have allowed the stop with
    # the declaration still unreconciled (Junior review 2, Q1).
    if blocked and not unevidenced:
        return {**base, "verdict": "ALL_BLOCKED", "stop_allowed": True,
                "blockers": [{"objective": st["objective"], "index": st["index"],
                              "step": st["step"], "blocker": str(st["blocker"]),
                              "unblock": str(st.get("unblock") or "")} for st in blocked],
                "message": (f"every remaining step is BLOCKED ({len(blocked)}); keep the mandate "
                            "INCOMPLETE and record each blocker's unblock condition")}
    if not steps:
        return {**base, "verdict": "EMPTY", "stop_allowed": True,
                "message": "the queue names no steps; nothing to execute"}
    if unevidenced:
        # Every step is DONE but some carry no evidence: the declaration is not yet
        # reconciled. The session supplies the pointers; it does not redo the work and it
        # does not call the mandate complete (Codex review, 2026-09-14).
        return {**base, "verdict": "EVIDENCE_PENDING", "stop_allowed": False,
                "unevidenced": [{"objective": st["objective"], "index": st["index"],
                                 "step": st["step"]} for st in unevidenced],
                "message": (f"every step is DONE but {len(unevidenced)} carry no evidence — write "
                            "the durable pointer (commit, receipt, record) for each; do not redo "
                            "the work and do not set COMPLETE until they are reconciled")}
    return {**base, "verdict": "COMPLETE_PENDING", "stop_allowed": True,
            "message": "every step is DONE; set MANDATE_STATE: COMPLETE after the closing "
                       "obligations, then cancel only this mandate's own recalls"}


def status_for(root: Path, task_id: str) -> dict:
    matches = find_records(root, task_id)
    path = find_record(root, task_id)
    if not matches:
        return {"task": task_id, "verdict": "NO_RECORD", "stop_allowed": True,
                "message": f"no ledger/tasks/*/{task_id}.json"}
    if path is None:
        return {"task": task_id, "verdict": "MALFORMED", "stop_allowed": False,
                "message": "ambiguous TASK_ID — the same id exists under several actors: "
                           + ", ".join(str(m.relative_to(root)) for m in matches)}
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return {"task": task_id, "verdict": "UNREADABLE", "stop_allowed": True,
                "message": f"{path}: {exc}"}
    out = verdict(record)
    out["record"] = str(path.relative_to(root))
    return out


def _defuse(text: str) -> str:
    """Never let text we echo back into the conversation form a marker line."""
    return re.sub(r"MANDATE_(BOUND|RELEASED):", r"MANDATE_\1 :", str(text))


def render(status: dict) -> str:
    lines = [f"MANDATE {status['task']} {status['verdict']} — {_defuse(status['message'])}"]
    if "counts" in status:
        c = status["counts"]
        lines.append(f"steps: {status['steps_total']} · TODO {c['TODO']} · IN_PROGRESS "
                     f"{c['IN_PROGRESS']} · DONE {c['DONE']} · BLOCKED {c['BLOCKED']} · "
                     f"unreconciled {status['unreconciled']}")
    for f in status.get("findings", []):
        lines.append(f"finding: {_defuse(f)}")
    for u in status.get("unevidenced", []):
        lines.append(_defuse(f"evidence needed: {u['objective']}[{u['index']}] {u['step']}"))
    for b in status.get("blockers", []):
        lines.append(_defuse(f"blocked: {b['objective']}[{b['index']}] {b['step']} — {b['blocker']}"
                             + (f" — unblock: {b['unblock']}" if b["unblock"] else "")))
    return "\n".join(lines)


def normalise_record(record: dict) -> bool:
    """Bring a prose queue onto the A.1c schema in place: bare string steps become TODO steps,
    MANDATE_STATE defaults to OPEN. Text is kept verbatim; nothing is marked DONE. Returns
    whether anything changed."""
    queue_key, queue = load_queue(record)
    if queue is None:
        return False
    changed = False
    if "MANDATE_STATE" not in queue:
        queue["MANDATE_STATE"] = "OPEN"
        changed = True
    for name, objective in queue.items():
        if not (name.startswith(OBJECTIVE_PREFIX) and isinstance(objective, dict)):
            continue
        steps = objective.get("steps")
        if not isinstance(steps, list):
            continue
        for i, raw in enumerate(steps):
            if isinstance(raw, str):
                steps[i] = {"step": raw, "status": "TODO"}
                changed = True
    return changed


# ---------------------------------------------------------------- transcript binding
def _text_blocks(entry: dict):
    # Side-chains are subagents; compaction summaries and meta entries are the runtime's own
    # text (a summary that quotes a marker must not bind or release). Hook feedback is defused
    # at the source by _defuse; this filter is the second line.
    if entry.get("isSidechain") or entry.get("isCompactSummary") or entry.get("isMeta"):
        return
    if entry.get("type") not in ("user", "assistant"):
        return
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        yield content
    elif isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                yield str(block.get("text", ""))


def _outside_fences(text: str) -> str:
    """Drop fenced code blocks. Documentation quoting a marker on its own line inside a fence
    otherwise bound — and released — a session (Junior review 2, Q3)."""
    kept, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            kept.append(line)
    return "\n".join(kept)


def scan_transcript(path: Path) -> tuple[str | None, int, int]:
    """(binding, non-empty lines, lines that parsed as JSON objects).

    The last marker LINE in this session's own text wins; RELEASED clears BOUND. The two counts
    are the hook's only way to notice that the transcript format has changed under it: a file
    with lines and no parseable entry is a format this code does not read, not an unbound
    session."""
    bound: str | None = None
    lines = entries = 0
    try:
        with path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if not line.strip():
                    continue
                lines += 1
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(entry, dict):
                    continue
                entries += 1
                for text in _text_blocks(entry):
                    for kind, task in MARKER_RE.findall(_outside_fences(text)):
                        bound = task if kind == "BOUND" else (None if task == bound else bound)
    except OSError:
        return None, 0, 0
    return bound, lines, entries


def binding_from_transcript(path: Path) -> str | None:
    """The last marker LINE in this session's own text wins; RELEASED clears BOUND."""
    return scan_transcript(path)[0]


def launcher_binding() -> str | None:
    """The task a launcher bound this process to, or None. A malformed id binds nothing."""
    value = os.environ.get(BIND_ENV, "").strip()
    return value if TASK_ID_RE.match(value) else None


# ---------------------------------------------------------------- bounded stop hook
def _queue_signature(root: Path, record_rel: str | None) -> str:
    """Progress pertinent to the mandate means a step status or evidence moved in the record.
    Not a commit — any commit, a report or one unrelated to the task would reset the bound
    (Codex review, 2026-09-14) — and not that the file was touched: a STOP_LOG line or a
    timestamp written after a block does not reset it either."""
    if not record_rel:
        return "no-record"
    try:
        record = json.loads((root / record_rel).read_text(encoding="utf-8"))
        queues = load_active_queues(record)
        # The record's identity is part of the shape: two different mandates with the same
        # queue shape shared one block count, so binding to a second one started it already
        # spent (Junior review 2, D3).
        shape = {"record": record_rel, "task": str(record.get("TASK_ID")),
                 "keys": [k for k, _ in queues],
                 "states": [str(q.get("MANDATE_STATE", "OPEN")) for _, q in queues],
                 "steps": [(st["objective"], st["index"], st["status"],
                            bool(str(st.get("evidence") or "").strip()))
                           for st in iter_all_steps(queues)]}
        return hashlib.sha256(json.dumps(shape, sort_keys=True).encode()).hexdigest()
    except (OSError, ValueError, Malformed):
        return "record-unreadable"


def state_dir() -> Path:
    base = os.environ.get("LEGEND_MANDATE_HOOK_STATE") or os.path.join(
        os.environ.get("XDG_CACHE_HOME", os.path.expanduser("~/.cache")), "legend", "mandate_stop_hook")
    return Path(base)


def decide(payload: dict, root: Path, *, max_blocks: int = MAX_CONSECUTIVE_BLOCKS) -> dict:
    """Pure decision: returns {'action': 'allow'|'block', 'reason': str, 'status': dict|None}."""
    task = launcher_binding()
    if not task:
        transcript = payload.get("transcript_path")
        if not isinstance(transcript, str) or not transcript:
            return {"action": "allow", "reason": "no transcript in payload", "status": None}
        task, lines, entries = scan_transcript(Path(transcript))
        if not task:
            if lines and not entries:
                return {"action": "allow", "status": None, "event": "TRANSCRIPT_UNPARSEABLE",
                        "reason": f"transcript has {lines} lines and none parses as a JSON "
                                  "object: the format changed or the path is wrong, so no "
                                  "session can be bound through it"}
            return {"action": "allow", "reason": "session bound to no mandate", "status": None}
    status = status_for(root, task)
    if status["stop_allowed"]:
        return {"action": "allow", "reason": render(status), "status": status}
    session = re.sub(r"[^A-Za-z0-9_.-]", "_", str(payload.get("session_id") or "unknown"))
    signature = _queue_signature(root, status.get("record"))
    sdir = state_dir()
    sfile = sdir / f"{session}.json"
    prior = {"signature": None, "consecutive_blocks": 0}
    try:
        loaded = json.loads(sfile.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            prior.update(loaded)
    except (OSError, ValueError):
        pass
    count = 0 if prior.get("signature") != signature else int(prior.get("consecutive_blocks") or 0)
    total = int(prior.get("total_blocks") or 0) if prior.get("task") == task else 0
    if count >= max_blocks:
        return {"action": "allow", "status": status,
                "reason": (f"{render(status)}\nstop allowed after {count} consecutive blocks with "
                           "no status or evidence change in the queue — record the premature "
                           "stop as a finding (§12 DETECTION)")}
    if total >= MAX_TOTAL_BLOCKS:
        # Progress resets the consecutive count; nothing resets this one. A session that has
        # been sent back this many times is not being helped by a further refusal.
        return {"action": "allow", "status": status,
                "reason": (f"{render(status)}\nstop allowed: {total} blocks on this session for "
                           f"this mandate, the absolute ceiling — reconcile in a fresh session")}
    # The count is persisted BEFORE the block is issued; if it cannot be, the block is not
    # bounded and therefore not issued (Junior case 18).
    try:
        sdir.mkdir(parents=True, exist_ok=True)
        sfile.write_text(json.dumps({"signature": signature, "consecutive_blocks": count + 1,
                                     "total_blocks": total + 1, "task": task}), encoding="utf-8")
    except OSError as exc:
        return {"action": "allow", "status": status,
                "reason": f"{render(status)}\nstop allowed: cannot persist the block count "
                          f"({exc}); an unbounded block is not issued"}
    reason = (f"{render(status)}\n"
              f"The turn may not end: mandate {task} is bound to this session and its authorised "
              f"queue still has executable work (block {count + 1}/{max_blocks} on this state). "
              "Apply cross_session_transport.md §12: reconcile from disk, execute or delegate the "
              "next step, and update the step's status in the record with evidence or a named "
              "blocker. Compaction on this runtime is automatic and disk state survives it. "
              "To stop legitimately, set MANDATE_STATE in the record (COMPLETE / PAUSED) or mark "
              "every remaining step BLOCKED with its blocker, or have the operator write the "
              "release line for this task (the RELEASED marker with its TASK_ID, on a line of "
              "its own).")
    return {"action": "block", "reason": _defuse(reason), "status": status}


def log_event(kind: str, **fields) -> None:
    """Append one line to the hook's own event log. Best effort: it never raises and never
    changes a decision. Rotated once at EVENTS_MAX_BYTES, keeping one previous file."""
    try:
        sdir = state_dir()
        sdir.mkdir(parents=True, exist_ok=True)
        target = sdir / EVENTS_FILE
        if target.exists() and target.stat().st_size > EVENTS_MAX_BYTES:
            target.replace(sdir / (EVENTS_FILE + ".1"))
        record = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "kind": kind}
        record.update({k: (str(v)[:240] if isinstance(v, str) else v) for k, v in fields.items()})
        with target.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception:  # noqa: BLE001 — observability must not become a failure mode
        pass


def read_events(limit: int = 20) -> tuple[dict, list[dict]]:
    """(counts by kind, the last `limit` events) across the current and previous log file."""
    rows: list[dict] = []
    sdir = state_dir()
    for name in (EVENTS_FILE + ".1", EVENTS_FILE):
        try:
            with (sdir / name).open(encoding="utf-8") as fh:
                for line in fh:
                    try:
                        row = json.loads(line)
                    except ValueError:
                        continue
                    if isinstance(row, dict):
                        rows.append(row)
        except OSError:
            continue
    counts: dict[str, int] = {}
    for row in rows:
        counts[str(row.get("kind"))] = counts.get(str(row.get("kind")), 0) + 1
    return counts, rows[-limit:] if limit > 0 else []


def stop_hook(stdin_text: str, root: Path = ROOT) -> tuple[int, str, str]:
    """Returns (exit_code, stdout, stderr). Fails open on every error."""
    if os.environ.get(DISABLE_ENV, "").lower() in ("off", "0", "false", "no"):
        return 0, "", ""
    session = "unknown"
    try:
        payload = json.loads(stdin_text or "{}")
        if not isinstance(payload, dict):
            log_event("ERROR", reason="payload is not an object")
            return 0, "", "mandate_continuity: payload is not an object; allowing"
        session = str(payload.get("session_id") or "unknown")
        decision = decide(payload, root)
    except Exception as exc:  # noqa: BLE001 — a hook must never trap the session
        log_event("ERROR", session=session, reason=f"{type(exc).__name__}: {exc}")
        return 0, "", f"mandate_continuity: {type(exc).__name__}: {exc}; allowing"
    status = decision.get("status") or {}
    if decision.get("event"):
        log_event(decision["event"], session=session, reason=decision["reason"])
    elif status:
        log_event("BLOCK" if decision["action"] == "block" else "ALLOW", session=session,
                  task=status.get("task"), verdict=status.get("verdict"),
                  reason=str(decision["reason"]).splitlines()[-1] if decision["reason"] else "")
    if decision["action"] == "block":
        return 0, json.dumps({"decision": "block", "reason": decision["reason"]}), ""
    note = decision["reason"] if decision.get("status") else ""
    return 0, "", (f"mandate_continuity: {note}" if note else "")


# ---------------------------------------------------------------- CLI
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    st = sub.add_parser("status", help="verdict for one mandate record")
    st.add_argument("--task", help="TASK_ID under ledger/tasks/*/")
    st.add_argument("--record", type=Path, help="explicit path to a task record")
    st.add_argument("--root", type=Path, default=ROOT)
    st.add_argument("--json", action="store_true")
    hk = sub.add_parser("stop-hook", help="Claude Code Stop hook: payload on stdin")
    hk.add_argument("--root", type=Path, default=ROOT)
    nm = sub.add_parser("normalise", help="convert a prose queue to the A.1c schema (dry run "
                                          "unless --write); the record's owner runs this")
    nm.add_argument("--task", required=True)
    nm.add_argument("--root", type=Path, default=ROOT)
    nm.add_argument("--write", action="store_true")
    ev = sub.add_parser("events", help="what the stop hook decided on this machine")
    ev.add_argument("--last", type=int, default=20, help="how many recent events to print")
    args = parser.parse_args(argv)

    if args.command == "events":
        counts, rows = read_events(args.last)
        print(f"state dir: {state_dir()}")
        if not counts:
            print("no events recorded: the hook has not run on a bound session, or is not installed")
            return 0
        print("counts: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
        broken = counts.get("ERROR", 0) + counts.get("TRANSCRIPT_UNPARSEABLE", 0)
        if broken and not (counts.get("BLOCK", 0) or counts.get("ALLOW", 0)):
            print("WARNING: only errors and unreadable transcripts so far; the hook is likely "
                  "broken, not quiet")
        for row in rows:
            print("  " + " ".join(f"{k}={row[k]}" for k in row))
        return 0

    if args.command == "stop-hook":
        try:
            raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001
            print(f"mandate_continuity: cannot read stdin ({exc}); allowing", file=sys.stderr)
            return 0
        code, out, err = stop_hook(raw, args.root.resolve())
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        return code

    root = args.root.resolve()
    if args.command == "normalise":
        path = find_record(root, args.task)
        if path is None:
            print(f"no unambiguous ledger/tasks/*/{args.task}.json", file=sys.stderr)
            return 1
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
            changed = normalise_record(rec)
        except (ValueError, Malformed) as exc:
            print(f"{path.relative_to(root)}: MALFORMED — {exc}", file=sys.stderr)
            return 1
        if not changed:
            print(f"{path.relative_to(root)}: already on the A.1c schema")
        elif args.write:
            path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"{path.relative_to(root)}: normalised and written")
        else:
            print(f"{path.relative_to(root)}: would change (bare steps → TODO, MANDATE_STATE → OPEN); "
                  "re-run with --write")
        print(render(verdict(rec)))
        return 0

    if args.record:
        try:
            record = json.loads(args.record.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            result = {"task": "?", "verdict": "UNREADABLE", "stop_allowed": True,
                      "message": f"{args.record}: {exc}"}
        else:
            result = verdict(record)
            result["record"] = str(args.record)
    elif args.task:
        result = status_for(root, args.task)
    else:
        parser.error("status needs --task or --record")
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(render(result))
    # Exit 0 means the command answered, whatever the answer; exit 1 means it could not,
    # because there is no record or the bytes would not parse. An earlier version exited 1 for
    # EMPTY and NO_QUEUE, so a caller reading the code saw a failure where the record was
    # simply empty (Junior review 2, Q5).
    return 1 if result["verdict"] in ("NO_RECORD", "UNREADABLE") else 0


if __name__ == "__main__":
    raise SystemExit(main())
