#!/usr/bin/env python3
"""Report weekly harness work due at session start; never gate or invent a completed scout."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path

from branch_hygiene import GitError, LAND_OVERDUE, build_report


def scout_status(root: Path, today: dt.date | None = None) -> dict:
    today = today or dt.date.today()
    year, week, _ = today.isocalendar()
    week_id = f"{year}-W{week:02d}"
    relative = f"governance/candidates/HARNESS-SCOUT-{week_id}.md"
    path = root / relative
    result = {"week": week_id, "report": relative, "status": "SCOUT_DUE"}
    if not path.exists():
        return result
    text = path.read_text(encoding="utf-8")
    header = re.match(r"\A---\s*\n(.*?)\n---", text, re.S)
    fields = dict(re.findall(r"^([a-z_]+):\s*(.*?)\s*$", header[1], re.M)) if header else {}
    if fields.get("record_type") != "HARNESS_SCOUT" or fields.get("week") != week_id:
        result["status"] = "INVALID_REPORT"
        return result
    result["status"] = "TRIAGE_DUE"
    rows = [line.split("|")[1:-1] for line in text.splitlines()
            if re.match(r"^\|\s*\d+\s*\|", line)]
    if (fields.get("status") == "TRIAGED" and rows
            and all(len(row) == 9 and row[-1].strip() in {"ADOPT", "TRIAL", "WATCH", "REJECT"}
                    for row in rows)):
        result["status"] = "CURRENT"
    return result


def startup(root: Path, actor: str, today: dt.date | None = None) -> dict:
    result = scout_status(root, today)
    result["actor"] = actor
    result["action"] = {
        "SCOUT_DUE": "Junior: run legend-harness-scout and write the weekly report; Plan: report missing input.",
        "INVALID_REPORT": "Repair the weekly report metadata before treating it as completed.",
        "TRIAGE_DUE": "Plan: fill HE verdicts, implement ADOPT/TRIAL, record landed commits.",
        "CURRENT": "Weekly report triaged; follow recorded ADOPT/TRIAL outcomes.",
    }[result["status"]]
    if actor == "plan":
        try:
            report = build_report(root, "main", 1, None, None)
            result["branch_hygiene"] = report["totals"]
            result["overdue_branches"] = [r["branch"] for r in report["branches"]
                                         if r["class"] == LAND_OVERDUE]
        except GitError as exc:
            result["branch_hygiene"] = f"UNAVAILABLE: {exc}"
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actor", required=True, choices=("plan", "junior-harness"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = startup(args.root.resolve(), args.actor)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"HARNESS_SCOUT {result['week']} {result['status']} — {result['report']}")
        print(result["action"])
        if "branch_hygiene" in result:
            print(result["branch_hygiene"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
