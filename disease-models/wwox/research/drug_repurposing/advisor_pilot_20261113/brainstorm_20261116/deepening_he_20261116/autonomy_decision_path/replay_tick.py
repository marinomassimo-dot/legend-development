#!/usr/bin/env python3
"""Replay of the overnight case of 2026-11-16 on COPIES: the real advisor state, the real campaign folder and the real portfolio, ticked by the code before and after the change.

    python3 replay_tick.py --repo <primary checkout> --before <commit> --after <commit-or-branch> --state <real advisor state dir> --now 2026-11-16T04:00:00Z --out <dir>
    python3 replay_tick.py --help

What it builds: two throwaway clones of the repository (one per code version; the tick refuses a linked worktree), the real state directory copied and edited ONLY in last_outcome (the real hold recorded 2026-11-15T21:54:29Z:
reason, resume_when and the absence of any excluded paths), `running` cleared and the pending events cleared (the hold had consumed them); LEGEND_ADVISOR_STATE points at the copy and LEGEND_ADVISOR_NOW fixes the clock.
It then runs `strategic_advisor.py tick` in each clone and keeps three things apart: the TICK RESULT (verdict, why), the HOLD (what was recorded and what it names) and the PRESIDIO line (what the presidio reads).
Nothing is written to the real state, the real campaign folder or the shared checkout. Not medical advice.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
for k in ("--repo", "--before", "--after", "--state", "--now", "--out"): ap.add_argument(k)
ap.add_argument("--scenario", choices=["hold"], default="hold", help="hold: the host hold of 2026-11-15T21:54Z (the overnight case). The state of the P16 era (the incomplete evaluation of 12:00Z) is not preserved: the real state file now holds the outcome of P17, so that period cannot be replayed")
a = ap.parse_args()
if not all([a.repo, a.before, a.after, a.state, a.now, a.out]):
    ap.print_help(); sys.exit(0)
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
CAMPAIGN = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113"
tmp = Path(tempfile.mkdtemp(prefix="replay_tick_"))
result = {}
for name, ref in (("before", a.before), ("after", a.after)):
    clone = tmp / name
    subprocess.run(["git", "clone", "-q", "--no-hardlinks", "--no-checkout", a.repo, str(clone)], check=True)
    subprocess.run(["git", "-C", str(clone), "checkout", "-q", ref], check=True)
    state = tmp / f"state_{name}"
    shutil.copytree(Path(a.state), state / Path(CAMPAIGN).name)
    sp = state / Path(CAMPAIGN).name / "state.json"
    st = json.loads(sp.read_text())
    holds = [json.loads(l) for l in (clone / CAMPAIGN / "holds.jsonl").read_text().splitlines() if l.strip()]
    h = holds[-1]
    st.update(running="", pending_events=[], pending_commits=0, unstated_streak=0)
    if a.scenario == "hold":
        st.update(last_outcome={"stated": True, "outcome": "wait", "reason": h["reason"], "excluded": h.get("excluded", ""), "problem": "", "resume_when": h["resume_when"], "evaluation": "HOLD", "utc": h["utc"]})
    # a quiet baseline, so that only the decision path is compared: the clone's own main, roadmap, mandates, waits and portfolio digest are taken as already seen; the evaluation clock is the one before the hold
    rd = subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0, 'framework/scripts'); import strategic_advisor as sa; print(sa.portfolio_snapshot()['digest'])"], cwd=clone, capture_output=True, text=True).stdout.strip()
    st.update(main_sha=subprocess.run(["git", "-C", str(clone), "rev-parse", "main"], capture_output=True, text=True).stdout.strip() or subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(),
              roadmap_sha256=None, mandates={}, portfolio_digest=rd, last_evaluation_utc=((h.get("previous_outcome") or {}).get("utc") or st.get("last_evaluation_utc")) if a.scenario == "hold" else st.get("last_evaluation_utc"))
    st.pop("waits_seen", None); st.pop("last_evaluation_started_utc", None)
    sp.write_text(json.dumps(st, indent=1, sort_keys=True))
    env = dict(os.environ, LEGEND_ADVISOR_STATE=str(state), LEGEND_ADVISOR_NOW=a.now)
    r = subprocess.run([sys.executable, "framework/scripts/strategic_advisor.py", "tick", "--campaign", CAMPAIGN], cwd=clone, capture_output=True, text=True, env=env)
    try:
        t = json.loads(r.stdout)
    except ValueError:
        result[name] = {"error": (r.stdout + r.stderr)[-600:]}; continue
    q = t.get("queue", {})
    result[name] = {"commit": subprocess.run(["git", "-C", str(clone), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip(),
                    "TICK_RESULT": {"verdict": t["verdict"], "why": t["why"], "hours_since_last_evaluation": t.get("hours_since_last_evaluation")},
                    "saved_outcome": ({"utc": h["utc"], "reason": h["reason"][:200], "resume_when": h["resume_when"], "excluded_paths_named": h.get("excluded", "") or "(none: the field did not exist)"} if a.scenario == "hold" else {k: str(st["last_outcome"].get(k, ""))[:200] for k in ("evaluation", "outcome", "stated", "reason", "resume_when", "utc")}),
                    "PRESIDIO_line": t["presidio"],
                    "queue": {k: q.get(k) for k in ("exhausted", "executable", "blocked_only", "scope", "blocked_paths", "portfolio_ready") if k in q},
                    "portfolio_actionable_in_tick": t.get("portfolio", {}).get("actionable")}
(out / f"replay_tick_result_{a.scenario}.json").write_text(json.dumps({"now": a.now, **result}, indent=1, sort_keys=True) + "\n")
print(json.dumps({"now": a.now, **result}, indent=1, sort_keys=True))
shutil.rmtree(tmp, ignore_errors=True)
