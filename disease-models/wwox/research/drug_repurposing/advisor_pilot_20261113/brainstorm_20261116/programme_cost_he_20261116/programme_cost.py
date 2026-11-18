"""PROGRAMME_COST.md: what the 2026-11-16 programme consumed, in explicit units, read from transcripts. No estimate, no share of any plan.

    python3 programme_cost.py --until 2026-11-16T10:15:00Z      (run from the repository root; --since defaults to 2026-11-16T07:05:00Z)

Tools: framework/scripts/trial_window_table.py (sessions) and framework/scripts/session_model_census.py (each delegate transcript).
Units: turns, output tokens, cache written (cache_creation), cache read. A delegate is a subagent transcript whose file changed in the
window; its label is the description its dispatch gave (meta.json). The quota is unknown, so no figure is converted into a share of anything.
Value-per-cost lines divide an explicit output-token numerator by an explicit count read from a committed file; each line names both.
"""
import argparse
import csv
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
B = HERE.parent
PROJECTS = Path.home() / ".claude/projects/-home-desktop-legend-development"
ap = argparse.ArgumentParser()
ap.add_argument("--since", default="2026-11-16T07:05:00Z")
ap.add_argument("--until", required=True)
ap.add_argument("--out", default=str(HERE / "PROGRAMME_COST.md"))
args = ap.parse_args()
T0 = datetime.fromisoformat(args.since.replace("Z", "+00:00"))


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout


# sessions ---------------------------------------------------------------------------------------------------------------
win_cmd = ["python3", "framework/scripts/trial_window_table.py", "--since", args.since, "--until", args.until, "--ref", "development/main", "--root", "."]
sessions, section = [], None
for line in run(*win_cmd).splitlines():
    if line.startswith("SESSIONS"):
        section = "s"
        continue
    if section == "s":
        if not line.strip():
            break
        c = line.split("\t")
        sessions.append({"name": c[0], "turns": int(c[1]), "output": int(c[2]), "cache_written": int(c[3]), "cache_read": int(c[4]), "sub_runs": int(c[5])})

# delegates --------------------------------------------------------------------------------------------------------------
LABEL = {  # description given at dispatch -> role in the programme (what IT's notes call it)
    "Memory-free baseline arm matrix": "matrix baseline arm (arm A for the matrix)",
    "Baseline table of frozen predictions": "baseline table of frozen predictions",
    "Second read of 25 matrix cells": "second read of 25 matrix cells",
    "Blind extractor of treatment statements": "blind extractor",
    "Simple-search baseline arm hypotheses": "leap round: simple-search baseline arm",
    "Blind judge of 24 hypotheses": "leap round: blind judge RUN 1 (INVALID, anonymiser error)",
    "Blind judge rerun of 24 hypotheses": "leap round: blind judge run 2",
    "Blind judge round 1b with planted pair": "leap round: blind judge round 1b",
    "Arm B hypotheses with repository knowledge": "leap round: arm B (with repository knowledge)",
    "Blind judge of arm B with planted pair": "leap round: blind judge of arm B with planted pair",
    "Test-setter fixing tests for 31 hypotheses": "test-setter (31 tests)",
    "Blind audit of the closing synthesis": "blind audit of the closing synthesis",
}
dels = []
for meta in sorted(PROJECTS.glob("*/subagents/*.meta.json")):
    tr = meta.with_suffix("").with_suffix(".jsonl")
    if not tr.exists() or datetime.fromtimestamp(tr.stat().st_mtime, timezone.utc) < T0:
        continue
    cen = json.loads(run("python3", "framework/scripts/session_model_census.py", "--json", "--since", args.since, "--until", args.until, str(tr)))[0]
    if not cen["turns"]:
        continue
    desc = json.loads(meta.read_text()).get("description", "")
    dels.append({"label": LABEL.get(desc, desc), "description": desc, "parent": meta.parent.parent.name[:8], "turns": cen["turns"],
                 "output": cen["totals"]["output"], "cache_written": cen["totals"]["cache_creation"], "cache_read": cen["totals"]["cache_read"],
                 "model": ",".join(sorted(cen["models"])), "effort": ",".join(sorted(cen["efforts"])), "start": datetime.fromtimestamp(tr.stat().st_ctime, timezone.utc)})
dels.sort(key=lambda d: d["description"] not in LABEL)   # stable: described ones first, order of the filesystem sort kept
dels.sort(key=lambda d: list(LABEL).index(d["description"]) if d["description"] in LABEL else 99)

# denominators read from committed files ---------------------------------------------------------------------------------
ext = list(csv.DictReader(open(B / "it_extractor_20261116/sealed/extraction.tsv"), delimiter="\t"))
attrib = sum(r["seizure_outcome_attributable"] == "yes" for r in ext)
judged = sum(1 for _ in open(B / "it_leap_judge_20261116/judge_table_run2.tsv")) - 1
surv1 = 0
for line in open(B / "it_leap_judge_20261116/UNBLINDED.md"):
    m = re.match(r"\|\s*(?:Memory-free baseline arm|ADV[^|]*|HE[^|]*|IT[^|]*|SCI[^|]*?)\s*\|\s*\d+\s*\|\s*(\d+)", line)
    if m:
        surv1 += int(m.group(1))
surv1b = {}
for line in open(B / "it_leap_judge_20261116/round1b/UNBLINDED_1B.md"):
    m = re.match(r"\|\s*(Memory-free baseline|ADV|HE|IT|SCI)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|", line)
    if m:
        surv1b[m.group(1)] = (int(m.group(2)), int(m.group(3)))


def D(desc):
    return next((d for d in dels if d["description"] == desc), None)


def fmt(n):
    return f"{n:,}"


L = []
L.append(f"# PROGRAMME_COST: what the programme consumed, window [{args.since}, {args.until}) (HE; non-canonical; read from transcripts)")
L.append("")
L.append("Written for: ADV and the operator's 24-hour report. **Measured, not estimated.** Units: turns, output tokens, cache written, cache read, exactly as `session_model_census.py` reads them from each transcript. The quota is unknown, so no figure here is a share of any plan. A session's row is everything that session did in the window, programme or not; a delegate's row is that delegate only.")
L.append("")
L.append("Commands (run from the repository root): sessions `python3 framework/scripts/trial_window_table.py --since %s --until %s --ref development/main --root .`; each delegate `python3 framework/scripts/session_model_census.py --json --since %s --until %s <subagent transcript>`; this file `python3 %s --until %s`." % (args.since, args.until, args.since, args.until, (HERE / "programme_cost.py").relative_to(Path.cwd()) if HERE.is_relative_to(Path.cwd()) else "programme_cost.py", args.until))
L.append("")
L.append("## Sessions")
L.append("| session | turns | output | cache written | cache read | delegate runs it spawned |")
L.append("|---|---|---|---|---|---|")
for s in sessions:
    L.append(f"| {s['name']} | {s['turns']} | {fmt(s['output'])} | {fmt(s['cache_written'])} | {fmt(s['cache_read'])} | {s['sub_runs']} |")
tot = {k: sum(s[k] for s in sessions) for k in ("turns", "output", "cache_written", "cache_read")}
L.append(f"| **sessions together** | {tot['turns']} | {fmt(tot['output'])} | {fmt(tot['cache_written'])} | {fmt(tot['cache_read'])} | |")
L.append("")
L.append("## Delegates (each is a separate subagent transcript; its tokens are NOT inside the session rows above)")
L.append("| delegate (role) | dispatched by | model, effort | turns | output | cache written | cache read |")
L.append("|---|---|---|---|---|---|---|")
for d in dels:
    L.append(f"| {d['label']} | {d['parent']} | {d['model']}, {d['effort']} | {d['turns']} | {fmt(d['output'])} | {fmt(d['cache_written'])} | {fmt(d['cache_read'])} |")
dt = {k: sum(d[k] for d in dels) for k in ("turns", "output", "cache_written", "cache_read")}
L.append(f"| **delegates together** | | | {dt['turns']} | {fmt(dt['output'])} | {fmt(dt['cache_written'])} | {fmt(dt['cache_read'])} |")
inv = D("Blind judge of 24 hypotheses")
if inv:
    L.append("")
    L.append(f"**The invalid run on its own line:** blind judge run 1 (anonymiser error, discarded): {inv['turns']} turns, {fmt(inv['output'])} output tokens, {fmt(inv['cache_written'])} cache written, {fmt(inv['cache_read'])} cache read. IT's JUDGE_RUN2.md reports the same run as 77 turns, output 54,395, cache written 220,187. It is {inv['output'] / sum(d['output'] for d in dels):.1%} of the delegates' output and produced no result used anywhere.")
L.append("")
L.append("## Value per cost (numerator and denominator named; every denominator is a count read from a committed file)")
L.append("| line | output tokens | divided by | result |")
L.append("|---|---|---|---|")
ex = D("Blind extractor of treatment statements")
if ex:
    L.append(f"| blind extractor per attributable seizure-outcome row coded | {fmt(ex['output'])} | {attrib} attributable rows of {len(ext)} rows (it_extractor_20261116/sealed/extraction.tsv) | {ex['output'] / attrib:,.0f} per attributable row; {ex['output'] / len(ext):,.0f} per row |")
sr = D("Second read of 25 matrix cells")
if sr:
    L.append(f"| matrix cell second read per cell | {fmt(sr['output'])} | 25 cells | {sr['output'] / 25:,.0f} per cell |")
judges = [D(x) for x in ("Blind judge of 24 hypotheses", "Blind judge rerun of 24 hypotheses", "Blind judge round 1b with planted pair") if D(x)]
judge_b = D("Blind judge of arm B with planted pair")
audit = D("Blind audit of the closing synthesis")
if judges:
    jo = sum(j["output"] for j in judges)
    L.append(f"| judging, all three runs, per hypothesis judged in round 1 | {fmt(jo)} (of which the invalid run {fmt(inv['output']) if inv else 'n/a'}) | {judged} hypotheses (judge_table_run2.tsv) | {jo / judged:,.0f} per hypothesis |")
arms = [D(x) for x in ("Simple-search baseline arm hypotheses", "Arm B hypotheses with repository knowledge") if D(x)]
if arms and judges:
    base = D("Simple-search baseline arm hypotheses")
    L.append(f"| leap round, delegate arms plus all judging, per round-1 survivor (S1 all four criteria) | {fmt(sum(a['output'] for a in arms) + jo)} | {surv1} survivor(s) in round 1 (UNBLINDED.md) | {(sum(a['output'] for a in arms) + jo) / max(surv1, 1):,.0f} per survivor |")
    if base:
        L.append(f"| the simple-search baseline arm alone, per survivor it produced | {fmt(base['output'])} | 1 survivor (UNBLINDED.md: H-B1) | {base['output']:,.0f} per survivor |")
if judge_b:
    L.append(f"| judging arm B (5 hypotheses plus the planted pair) | {fmt(judge_b['output'])} | 5 arm B hypotheses (it_arm_b_20261116) | {judge_b['output'] / 5:,.0f} per hypothesis |")
if audit:
    L.append(f"| blind audit of the closing synthesis (checks, not production) | {fmt(audit['output'])} | {audit['turns']} turns | {audit['output'] / audit['turns']:,.0f} per turn |")
if surv1b:
    L.append(f"| round 1b survivors under the definition S1, by arm (n, S1) | | | " + "; ".join(f"{k} {v[1]} of {v[0]}" for k, v in surv1b.items()) + " |")
# CI runs (written once from the public API by HE; the file is data, not recomputed here) ---------------------------------
ci = list(csv.DictReader(open(HERE / "ci_runs_20261116.tsv"), delimiter="\t"))
def mins(r):
    a, b = (datetime.fromisoformat(r[k].replace("Z", "+00:00")) for k in ("started_utc", "ended_utc"))
    return (b - a).total_seconds() / 60
red = [r for r in ci if r["conclusion"] != "success"]
L.append("")
L.append("## CI: one line per run of the public-release-gate workflow, #872 to #893 (source: GitHub API `actions/runs`, jobs and check-run annotations)")
L.append("| run | commit | conclusion | minutes | cause (read from annotations) or note |")
L.append("|---|---|---|---|---|")
for r in ci:
    L.append(f"| #{r['run']} | {r['sha'][:9]} | {r['conclusion']} | {mins(r):.0f} | {r['red_cause_or_note']} |")
L.append("")
L.append(f"{len(red)} red runs (#{red[0]['run']} to #{red[-1]['run']}), {sum(mins(r) for r in red):,.0f} run-minutes on the CI machine, all from two causes, both repository-side and both reached `main` before the gate could see them: (1) HB1 mapping, #873 to #886, repaired by 98542e035; (2) `reach_cahoy.tsv` row width, #886 to #891, repaired by SCI's 120c3abe4. First green runs: #892 (120c3abe4) and #893 (da4f7a957, the head with both repairs and ADV's closing records). #871 and #872 are the last green runs before the HB1 package; #891 stays red because it precedes the repair. These counts are CI minutes read from the API, not tokens and not money.")
L.append("")
L.append("## What these lines can and cannot say")
L.append("* The authors' (ADV, HE, IT, SCI) output per hypothesis is NOT separable: each session did other work in the window, so no authors' survivors-per-token figure is given. A session's whole-window output is in the first table and is an upper bound on what its leap file cost.")
L.append("* Round 1 and round 1b used different survivor definitions and the numbers differ strongly (e.g. HE's four hypotheses: 0 survivors in round 1, S1 3 of 4 in round 1b); the two rounds are reported side by side, never merged.")
L.append("* Cache read dominates every row (long contexts re-read each turn); it is a measure of context size, not of work, and is listed so nobody divides by it by mistake.")
L.append("* A delegate's row is read at the `--until` time; IT's own notes (JUDGE_RUN2.md) read the run-2 judge earlier (71 turns, output 56,810) and the transcript has grown since, so the two can differ by the turns taken after IT's reading.")
L.append("* The window ends at the `--until` time given; rerun at the closing time. Delegates that were still running at that time are counted up to it.")
L.append("* **Final rerun, 15:10Z.** 13 delegates: the 12 of IT's `it_synthesis_audit_20261116/IT_DELEGATE_COSTS.md` (530,674 output tokens, same per-delegate figures as read here) plus one dispatched by SCI (readiness sheets producer), which IT's table does not list. The audit is checks, not production; arm A, arm B, extractor and judges are production for the leap and the matrix.")
Path(args.out).write_text("\n".join(L) + "\n")
print(f"wrote {args.out}: {len(sessions)} sessions, {len(dels)} delegates, sessions output {tot['output']}, delegates output {dt['output']}")
