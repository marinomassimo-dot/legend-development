#!/usr/bin/env python3
"""The measurement table of a time window [T0, T1): consumption and counts, no interpretation.

Read-only. Per session transcript: main-session turns, output tokens, cache written, cache read
(session_model_census.census, not reimplemented) and, apart, the same figures summed over the session's own
subagent transcripts. Per Advisor evaluation P<n>: the same figures from its meta.json, complete or incomplete
(strategic_advisor.incomplete_run). From git and the ledger: commits, task records created and their final
state, assignment ids by latest state, presidio-decided and operator-directed PRESIDIO-00n files, receipts
appended to fulltext_read_receipts.jsonl. No threshold, no verdict, no file written unless --tsv names one.

  python3 framework/scripts/trial_window_table.py --since 2026-11-14T15:29:29Z --until 2026-11-15T15:29:29Z
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import session_model_census as smc  # noqa: E402
import strategic_advisor as sa  # noqa: E402

DEFAULT_SINCE = "2026-11-14T15:29:29Z"
CAMPAIGN = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113"
RECEIPTS = "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
PROJECTS = Path.home() / ".claude" / "projects"
STATE_ORDER = ["DRAFTED", "SENT", "TAKEN", "EXECUTED"]
CAMPAIGN_ROOT: Path | None = None   # set by main(): where the evaluations' meta.json files are


def git(root: Path, *args: str) -> str:
    done = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return done.stdout if done.returncode == 0 else ""


def in_window(stamp: str, since: str, until: str) -> bool:
    return bool(stamp) and since <= stamp < until


def utc(iso: str) -> str:
    return dt.datetime.fromisoformat(iso).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def figures(row: dict[str, Any]) -> dict[str, int]:
    t = row.get("totals") or {}
    return {"turns": int(row.get("turns") or 0), "output": int(t.get("output", 0)), "cache_written": int(t.get("cache_creation", 0)), "cache_read": int(t.get("cache_read", 0))}


def session_names(projects: Path) -> dict[str, str]:
    names = {}
    for f in projects.glob("*/*/custom-title.json"):
        try:
            names[f.parent.name] = str(json.loads(f.read_text(encoding="utf-8")).get("customTitle") or "")
        except (OSError, json.JSONDecodeError):
            continue
    for meta in sorted(CAMPAIGN_ROOT.glob("P[0-9]*/meta.json")) if CAMPAIGN_ROOT else []:   # an Advisor evaluation run is a session of its own
        try:
            m = json.loads(meta.read_text(encoding="utf-8"))
            names[str((m.get("capture") or {}).get("source_session_id"))] = f"Advisor evaluation {meta.parent.name}"
        except (OSError, json.JSONDecodeError):
            continue
    for a in sa._agents() or []:                                   # a live session without a saved title
        names.setdefault(str(a.get("sessionId")), str(a.get("name")))
    return names


def sessions(projects: Path, since: str, until: str) -> list[dict[str, Any]]:
    names, out = session_names(projects), []
    for path in sorted(projects.glob("*/*.jsonl")):
        if not path.parent.name.startswith("-home-desktop-legend-development"):
            continue
        main = figures(smc.census(path, since, until))
        if not main["turns"]:
            continue
        subs = [figures(smc.census(p, since, until)) for p in sorted((path.parent / path.stem / "subagents").glob("*.jsonl"))]
        subs = [x for x in subs if x["turns"]]
        out.append({"session": names.get(path.stem) or path.stem[:8], "id": path.stem[:8], **main,
                    "subagent_runs": len(subs), **{f"sub_{k}": sum(x[k] for x in subs) for k in ("turns", "output", "cache_written", "cache_read")}})
    return out


def evaluations(root: Path, campaign: Path, since: str, until: str) -> list[dict[str, Any]]:
    out = []
    for meta_path in sorted(campaign.glob("P[0-9]*/meta.json"), key=lambda p: int(p.parent.name[1:])):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not in_window(str(meta.get("started_utc") or ""), since, until):
            continue
        census = (meta.get("runtime_readback") or {}).get("census") or {}
        why = sa.incomplete_run(campaign, meta_path.parent.name)
        out.append({"evaluation": meta_path.parent.name, "started_utc": meta["started_utc"], **figures(census), "state": "incomplete" if why else "complete"})
    return out


def counts(root: Path, ref: str, campaign: Path, since: str, until: str) -> dict[str, Any]:
    window = ["--since", since, "--until", until]
    shas = git(root, "log", ref, *window, "--format=%H").split()
    merges = git(root, "log", ref, *window, "--merges", "--format=%H").split()
    created = sorted({p for p in git(root, "log", ref, *window, "--diff-filter=A", "--name-only", "--format=", "--", "ledger/tasks").split() if re.fullmatch(r"ledger/tasks/[^/]+/[^/]+\.json", p)})
    states: dict[str, int] = {}
    for p in created:
        try:
            rec = json.loads(git(root, "show", f"{ref}:{p}"))
            state = str(sa.mc.verdict(rec)["verdict"])                    # the existing reader of a record's state
        except json.JSONDecodeError:
            state = "UNREADABLE"
        states[state] = states.get(state, 0) + 1
    latest: dict[str, tuple[int, str]] = {}
    events: dict[str, int] = {}
    af = campaign / "assignments.jsonl"
    if af.exists():
        for line in af.read_text(encoding="utf-8").splitlines():
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not in_window(str(row.get("utc") or ""), since, until):
                continue
            events[row["state"]] = events.get(row["state"], 0) + 1
            rank = STATE_ORDER.index(row["state"]) if row["state"] in STATE_ORDER else -1
            if row["id"] not in latest or rank >= latest[row["id"]][0]:
                latest[row["id"]] = (rank, row["state"])
    by_latest: dict[str, int] = {}
    for _, st in latest.values():
        by_latest[st] = by_latest.get(st, 0) + 1
    presidio = {"presidio_decided": [], "operator_directed": []}
    for f in sorted((campaign / "assignments").glob("PRESIDIO-*.md")):
        first_commit = git(root, "log", ref, "--diff-filter=A", "--format=%cI", "--", str(f.relative_to(root))).split()
        if first_commit and in_window(utc(first_commit[-1]), since, until):
            head = f.read_text(encoding="utf-8").splitlines()[0] if f.stat().st_size else ""
            presidio["operator_directed" if "OPERATOR-DIRECTED" in head.upper() else "presidio_decided"].append(f.stem)
    receipts, kinds = 0, {}
    rp = root / RECEIPTS
    if rp.exists():
        for line in rp.read_text(encoding="utf-8").splitlines():
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if in_window(str(row.get("event_at") or ""), since, until):
                receipts += 1
                kinds[str(row.get("record_kind"))] = kinds.get(str(row.get("record_kind")), 0) + 1
    return {"ref": ref, "commits": len(shas), "merge_commits": len(merges), "task_records_created": len(created), "task_final_states": states,
            "assignment_events_by_state": events, "assignment_ids_by_latest_state": by_latest, **presidio, "receipts_appended": receipts, "receipts_by_record_kind": kinds}


def render(since: str, until: str, sess: list[dict], evals: list[dict], cnt: dict[str, Any]) -> str:
    L = [f"WINDOW [{since}, {until})  (turns, output tokens, cache written, cache read; subagent columns are summed from the session's own subagent transcripts)", "",
         "SESSIONS\tturns\toutput\tcache_written\tcache_read\tsub_runs\tsub_turns\tsub_output\tsub_cache_written\tsub_cache_read"]
    for r in sorted(sess, key=lambda r: r["session"]):
        L.append("\t".join(str(x) for x in (f"{r['session']} ({r['id']})", r["turns"], r["output"], r["cache_written"], r["cache_read"], r["subagent_runs"], r["sub_turns"], r["sub_output"], r["sub_cache_written"], r["sub_cache_read"])))
    L += ["", "ADVISOR EVALUATIONS\tturns\toutput\tcache_written\tcache_read\tstate"]
    L += ["\t".join(str(x) for x in (e["evaluation"] + " " + e["started_utc"], e["turns"], e["output"], e["cache_written"], e["cache_read"], e["state"])) for e in evals] or ["(none in the window)"]
    L += ["", "COUNTS"] + [f"{k}\t{json.dumps(v, sort_keys=True) if isinstance(v, (dict, list)) else v}" for k, v in cnt.items()]
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--since", default=DEFAULT_SINCE, help="T0, ISO UTC (default: the trial start)")
    ap.add_argument("--until", required=True, help="T1, ISO UTC; the window is [T0, T1)")
    ap.add_argument("--ref", default="main", help="git ref whose commits and records are counted (default: main)")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--projects", default=str(PROJECTS), help="the transcripts directory (only turn usage is read)")
    ap.add_argument("--campaign", default="", help="the Advisor campaign folder (default: the pilot folder under --root)")
    ap.add_argument("--tsv", default="", help="also write the printed table to this file")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    campaign = Path(a.campaign) if a.campaign else root / CAMPAIGN
    global CAMPAIGN_ROOT
    CAMPAIGN_ROOT = campaign
    table = render(a.since, a.until, sessions(Path(a.projects), a.since, a.until), evaluations(root, campaign, a.since, a.until), counts(root, a.ref, campaign, a.since, a.until))
    print(table)
    if a.tsv:
        Path(a.tsv).write_text(table + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
