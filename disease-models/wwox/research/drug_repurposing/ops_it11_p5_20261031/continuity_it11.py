#!/usr/bin/env python3
"""IT11 P5 (C): recompute, from the host's own state files, the hourly-control coverage, gaps above 1.5 h, failures and repeated actions, and the
daily-radar evidence. Read-only. Usage: python3 -I continuity_it11.py [--state DIR]   (default ~/.local/state/legend)
Cron slot of the hourly control: minute 37 (crontab). Radar slot: 05:20 UTC. Both are read from `crontab -l` text given in CRON below."""
import argparse, collections, datetime as D, json, os, sys

ap = argparse.ArgumentParser(); ap.add_argument("--state", default=os.path.expanduser("~/.local/state/legend")); a = ap.parse_args()
ev = [json.loads(l) for l in open(os.path.join(a.state, "mandate_watch/events.jsonl")) if l.strip()]
ck = [e for e in ev if e.get("kind") == "check"]
t = lambda s: D.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
print(f"events {len(ev)} (checks {len(ck)}); first {ev[0]['at']}; last {ev[-1]['at']}")
# one run = all checks within 3 minutes of each other at the same hour slot
runs = []
for e in sorted(ck, key=lambda e: e["at"]):
    if runs and (t(e["at"]) - runs[-1][-1]).total_seconds() < 180: runs[-1].append(t(e["at"]))
    else: runs.append([t(e["at"])])
starts = [r[0] for r in runs]
print(f"runs (clusters of checks, manual and cron runs within 3 minutes merge) {len(runs)}")
gaps = [(a_, b_, (b_ - a_).total_seconds() / 3600) for a_, b_ in zip(starts, starts[1:]) if (b_ - a_).total_seconds() > 1.5 * 3600]
print("gaps above 1.5 h between consecutive runs:", [(x.isoformat(), y.isoformat(), round(h, 2)) for x, y, h in gaps] or "none")
# a cron run is any check event at minute 37 or 38 (a manual run within 3 minutes of it would merge into one cluster above, so clusters are not used here)
hrs = {t(e["at"]).strftime("%Y-%m-%dT%H") for e in ck if t(e["at"]).minute in (37, 38)}
h0 = D.datetime(2026, 10, 28, 19); h1 = starts[-1].replace(minute=0, second=0)
exp = []; x = h0
while x <= h1: exp.append(x.strftime("%Y-%m-%dT%H")); x += D.timedelta(hours=1)
print(f"cron slots :37 expected {len(exp)} from {exp[0]}Z to {exp[-1]}Z; present {sum(h in hrs for h in exp)}; missing {[h for h in exp if h not in hrs] or 'none'}")
act = [e for e in ck if e["action"] != "NONE"]
print(f"actions other than NONE: {len(act)}; by task {dict(collections.Counter(e['task'] for e in act))}")
print("failed deliveries:", [(e['at'], e['task']) for e in ck if (e.get('delivery') or '').startswith('failed')])
print("repeated RESUME for the same task within 180 min:", [(a_['task'], a_['at'], b_['at'], b_.get('delivery')) for i, a_ in enumerate(act) for b_ in act[i + 1:] if a_['task'] == b_['task'] and 0 < (t(b_['at']) - t(a_['at'])).total_seconds() < 180 * 60])
last = {}
print("state changes per task:")
for e in sorted(ck, key=lambda e: e["at"]):
    if last.get(e["task"]) != e["state"]:
        print(f"  {e['at']} {e['task']} -> {e['state']}"); last[e["task"]] = e["state"]
sd = json.load(open(os.path.join(a.state, "scout_daily.json")))
print("radar last run", sd.get("run_at"), "verdict", sd.get("verdict"), "errors", sd.get("errors"))
st = json.load(open(os.path.join(a.state, "scout_daily_state.json")))
print("radar discovery: last_day", st["discovery"].get("last_day"), "cursor", st["discovery"].get("cursor"), "seen by date", dict(collections.Counter(st["discovery"]["seen"].values())))
for f in ("scout_daily.log", "scout_daily_pending_log.md", "daily_push_check.log", "mandate_watch.log"):
    p = os.path.join(a.state, f)
    print(f"{f}: {os.path.getsize(p)} bytes, mtime {D.datetime.fromtimestamp(os.path.getmtime(p), D.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")}Z")
