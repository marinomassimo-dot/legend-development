#!/usr/bin/env python3
"""IT19 P7: how long do reopen questions wait under the radar's existing selector?

Uses the real plan (scout_daily.resolve_plan at HEAD) and the real pick_questions with questions_per_run from CONFIG; simulates
DAYS days, asking the picked questions each day (asked date = that day) and prints, for each question, the day it is first asked and
how often. No network, no state file touched. Usage: wait_model.py [DAYS] [OUT_JSON]   (--help prints this text)
"""
import datetime as dt, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
import scout_daily as sd  # noqa: E402


def simulate(days: int = 60):
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True, cwd=ROOT).strip()
    plan, _ = sd.resolve_plan(None, None, {"main_sha": sha})
    qs = plan["questions"]
    asked, first, count = {}, {}, {}
    start = dt.datetime(2026, 11, 3, 5, 20, tzinfo=dt.timezone.utc)
    for d in range(days):
        now = start + dt.timedelta(days=d)
        for q in sd.pick_questions(qs, asked, now, sd.CONFIG["questions_per_run"]):
            key = f"{q['id']}|{sd.digest(q['kw'])}"
            asked[key] = now.date().isoformat()
            first.setdefault(q["id"], d + 1)
            count[q["id"]] = count.get(q["id"], 0) + 1
    rows = [{"id": q["id"], "weight": q["weight"], "first_asked_day": first.get(q["id"]), "times_asked": count.get(q["id"], 0)} for q in qs]
    return {"sha": sha, "questions": len(qs), "per_run": sd.CONFIG["questions_per_run"], "days": days, "rows": rows}


def main(argv):
    if any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0
    days = int(argv[0]) if argv else 60
    res = simulate(days)
    if len(argv) > 1:
        Path(argv[1]).write_text(json.dumps(res, indent=1))
    for kind in ("reopen", "diagnosis", "work_order", "roadmap", "task_step", "open_item"):
        r = [x for x in res["rows"] if x["id"].startswith(kind + ":")]
        if not r:
            continue
        waits = sorted(x["first_asked_day"] if x["first_asked_day"] else days + 1 for x in r)
        print(f"{kind:10} n={len(r):3} median first-asked day={waits[len(waits)//2]:3} max={waits[-1]:3} never within {days} d={sum(1 for x in r if not x['first_asked_day'])} "
              f"asked >14d later={sum(1 for w in waits if w>14)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
