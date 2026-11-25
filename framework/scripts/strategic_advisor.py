#!/usr/bin/env python3
"""Plumbing for the Strategic Advisor: snapshot, neutral brief, launch, capture, check.

WHY THIS EXISTS
---------------
The advisor (`.claude/agents/legend-strategic-advisor.md`) returns text. This tool does the parts
that must not depend on a model's memory or on a caller retyping an answer: it records what the
repository looked like at dispatch, builds the brief from stable entry points (not from a
shortlist), launches the advisor as a read-only headless run, and saves the complete returned
assessment from the runtime's own result event, with the model read back and the files it opened.
The procedure around it is `.claude/skills/legend-strategic-advisor/SKILL.md`.

    python3 framework/scripts/strategic_advisor.py entrypoints
    python3 framework/scripts/strategic_advisor.py snapshot
    python3 framework/scripts/strategic_advisor.py seal   --campaign DIR --index N --text-file F
    python3 framework/scripts/strategic_advisor.py brief  --stage A --campaign DIR --mission-file F --constraints-file F [--task-record P] [--expect SHA[:FOLDER] ...]
    python3 framework/scripts/strategic_advisor.py brief  --stage B --campaign DIR --assessment A.md --sealed-intended S.md --constraints-file F
    python3 framework/scripts/strategic_advisor.py run    --stage A|B|S --campaign DIR --brief FILE --model opus --effort high
    python3 framework/scripts/strategic_advisor.py extract --transcript T.jsonl --out FILE
    python3 framework/scripts/strategic_advisor.py check  --campaign DIR

WHAT IS MECHANICAL AND WHAT IS NOT
----------------------------------
Mechanical (this tool, or the runtime flags it passes): the tool list the advisor is born with
(read from the runtime's init event), a deny rule on the sealed folder, the saved assessment
being the result event verbatim (and cross-checked against the persisted session transcript),
the model read back per turn (with the runtime's own record of a fallback, and the model of the final turn), whether each announced delivery is in the snapshot and reachable (and how much of it the advisor read), and a per-campaign attempt log that counts every launch, failed
ones included.
Procedural only: the attempt ceilings are enforced by this tool for runs launched through it and
by nothing else; calling `claude` directly bypasses them. Whether the advisor obeys its brief,
reads what it should, or reports honestly what it read is not enforced; `check` compares its list
of inspected files with the tool calls the stream recorded, which catches a false claim but not a
shallow reading.

Exit codes: 0 ok · 1 a check failed or the run failed · 2 invalid invocation or ceiling reached.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import fcntl
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mandate_continuity as mc  # noqa: E402  the existing reader of task-record queues

ROOT = Path(__file__).resolve().parents[2]
AGENT = "legend-strategic-advisor"
TOOLS = ["Read", "Glob", "Grep", "WebFetch"]
DENIED = ["Bash", "Write", "Edit", "NotebookEdit", "Agent", "Task", "WebSearch", "SendMessage", "Skill", "Read(**/advisor_sealed/**)"]
SEALED = "advisor_sealed"
LIMITS = {"A": 2, "B": 2, "S": 1, "P": 3}
DASHBOARD_URL = "https://marinomassimo-dot.github.io/legend-development/"
PORTFOLIO_REL = "disease-models/wwox/research/drug_repurposing/research_portfolio.tsv"
PORTFOLIO_FIELDS = ("id", "theme", "opportunity", "decision", "priority", "why_now", "next_action", "status", "sources", "mandate_id", "resume_when", "outcome", "updated_utc")


def portfolio_rows() -> tuple[list[dict[str, str]], list[str]]:
    """The living work portfolio, not a second copy of evidence or task execution state."""
    path = ROOT / PORTFOLIO_REL
    if not path.exists():
        return [], ["portfolio not present in this checkout"]
    try:
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            if not reader.fieldnames or not {"id", "opportunity", "status"}.issubset(reader.fieldnames):
                return [], ["portfolio needs id, opportunity and status columns"]
            rows = [{k: (v or "").strip() for k, v in row.items() if k is not None} for row in reader if any(row.values())]
        ids = [r["id"] for r in rows]
        errors = ["portfolio has empty or duplicate ids"] if not all(ids) or len(ids) != len(set(ids)) else []
        return rows, errors
    except (OSError, csv.Error, UnicodeError) as exc:
        return [], [f"portfolio unreadable: {exc}"]


def portfolio_snapshot(records: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    """Derive linked execution state and met dependencies; never write a second task status."""
    rows, errors = portfolio_rows()
    records = _records() if records is None else records
    items = []
    for row in rows:
        item = dict(row)
        status = row.get("status", "").lower()
        task = row.get("mandate_id", "")
        record = records.get(task, {})
        item["execution"] = record.get("verdict", "UNKNOWN") if task else "unassigned"
        item["task_path"] = record.get("path", "")
        item["ready"] = not errors and status == "ready" and not task
        item["review_due"] = not errors and bool(task) and item["execution"] == "RELEASED" and status not in ("done", "retired")
        item["dependency_met"] = ""
        if status == "waiting" and row.get("resume_when") and not task:
            item["dependency_met"] = resume_met(row["resume_when"], _now())
            item["ready"] = not errors and bool(item["dependency_met"])
        items.append(item)
    items.sort(key=lambda r: (r.get("priority", ""), r["id"]))
    # Editorial timestamps, row ordering and whitespace do not wake a model. A new action,
    # changed priority, completed linked mandate or met dependency can change the choice.
    semantic = [{k: v for k, v in r.items() if k != "updated_utc"} for r in sorted(items, key=lambda r: r["id"])]
    return {"path": PORTFOLIO_REL, "available": (ROOT / PORTFOLIO_REL).exists(), "items": items,
            "actionable": [r["id"] for r in items if r["ready"] or r["review_due"]], "errors": errors,
            "digest": sha256_text(json.dumps({"items": semantic, "errors": errors}, sort_keys=True))}


def portfolio_update(patch: dict[str, Any]) -> dict[str, str]:
    """Merge one opportunity by id; lock writers and replace atomically. Git keeps history."""
    if not isinstance(patch, dict) or not str(patch.get("id", "")).strip():
        raise ValueError("an update needs one opportunity id")
    unknown = set(patch) - set(PORTFOLIO_FIELDS)
    if unknown or any(not isinstance(v, str) for v in patch.values()):
        raise ValueError("use text values and portfolio columns only: " + ", ".join(sorted(unknown)))
    path = ROOT / PORTFOLIO_REL
    lock = STATE_DIR / ("portfolio-" + sha256_text(str(path.resolve()))[:16] + ".lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open("a") as guard:
        fcntl.flock(guard, fcntl.LOCK_EX)
        rows, errors = portfolio_rows()
        if errors and path.exists():
            raise ValueError("; ".join(errors))
        ident = patch["id"].strip()
        row = next((r for r in rows if r["id"] == ident), None)
        if row is None:
            row = dict.fromkeys(PORTFOLIO_FIELDS, "")
            row.update(status="backlog")
            rows.append(row)
        before = dict(row)
        row.update({k: v.strip() for k, v in patch.items() if k != "updated_utc"})
        if not row.get("opportunity"):
            raise ValueError("an opportunity needs a question or result sought")
        if before and {k: v for k, v in row.items() if k != "updated_utc"} == {k: v for k, v in before.items() if k != "updated_utc"}:
            return row                      # nothing changed: the row keeps its historical date and the file is not rewritten (2026-11-20: a date moved only to look recent hides which rows are stale)
        row["updated_utc"] = _utc(_now())
        # Preserve additional columns from a future/manual extension instead of dropping them.
        fields = list(dict.fromkeys([*PORTFOLIO_FIELDS, *(k for r in rows for k in r)]))
        output = io.StringIO(newline="")
        writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
                tmp = Path(handle.name); handle.write(output.getvalue())
            os.replace(tmp, path)
        finally:
            if tmp is not None:
                tmp.unlink(missing_ok=True)
        return row


def portfolio_brief(snapshot: dict[str, Any]) -> str:
    """A compact index; the complete rows and original packages remain available to Read."""
    lines = ["## Living Research Portfolio", f"Permanent source: `{PORTFOLIO_REL}`. Read on startup/resume and before choosing work or waiting.",
             "The operator roadmap defines the mission; these rows are opportunities, not scientific evidence or automatic assignments.",
             "Read the full selected row and its sources; linked task records own execution status. At handoff the host updates or adds the pertinent row with `strategic_advisor.py portfolio --upsert FILE.json`.",
             "After a result: record its consumer and next question, link the mandate, or park it with a resume condition. No opportunity count is a target."]
    if snapshot["errors"]:
        lines.append("Availability limits: " + "; ".join(snapshot["errors"]))
    for row in snapshot["items"]:
        if row.get("status") in ("done", "retired"):
            continue
        state = "REVIEW RESULT" if row["review_due"] else "READY" if row["ready"] else row.get("status", "unknown")
        lines.append(f"- {row['id']} [{row.get('priority', '?')}; {state}; {row['execution']}]: {row.get('opportunity', '')}; next: {row.get('next_action', '')}")
    return "\n".join(lines)


def apply_portfolio_updates(text: str) -> list[str]:
    """Optional advisory updates from a saved assessment; not a scientific promotion or gate."""
    block = re.search(r"^## Portfolio updates\s*\n```json\s*\n(.*?)\n```", text, re.M | re.S)
    if not block:
        return []
    try:
        updates = json.loads(block.group(1))
        if not isinstance(updates, list):
            raise ValueError("expected a list of opportunity patches")
    except (ValueError, TypeError) as exc:
        return [f"portfolio updates not applied: {exc}"]
    messages = []
    for patch in updates:
        try:
            row = portfolio_update(patch)
            messages.append(f"portfolio {row['id']} updated")
        except (OSError, ValueError) as exc:
            messages.append(f"portfolio update not applied: {exc}")
    return messages


def _memory_dir() -> Path:
    """The private memory directory of the main checkout (a worktree has none of its own)."""
    common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    main = Path(common).parent if common else ROOT
    return Path.home() / ".claude" / "projects" / ("-" + str(main).strip("/").replace("/", "-")) / "memory"


MEMORY_DIR = _memory_dir()
STATE_HOME = Path(os.environ.get("LEGEND_STATE_HOME", str(Path.home() / ".local/state/legend")))

# The entry map. One home. Starting places, not a shortlist: a glob is counted here and listed by the advisor.
ENTRY_POINTS: list[tuple[str, str, list[str]]] = [
    ("research_portfolio", "Living Research Portfolio: persistent opportunities, priorities, dependencies and result pointers", [PORTFOLIO_REL]),
    ("limits", "Authorised mission and resource limits: the task record named in the brief, and its siblings", ["ledger/tasks/*/*.json"]),
    ("invariants", "Canonical project invariants and the operating rules", [
        "CLAUDE.md", "ARCHITECTURE.md", "framework/master/harness_development_principles.md", "framework/master/designed_for_growth.md",
        "framework/master/gold_is_in_the_details.md", "framework/instruction/LEGEND_CORE.md", "framework/instruction/epistemic_discipline.md",
        "disease-models/wwox/mission.md"]),
    ("repurposing_method", "Drug-repurposing roadmap and Standing method", [
        "disease-models/wwox/research/drug_repurposing/roadmap_current.md", "framework/protocols/repurposing_adapter_convention.md"]),
    ("dashboard", "Dashboard: source records of the public page (the page is a map, the records are the facts)", [
        "disease-models/wwox/research/drug_repurposing/view/README.md", "disease-models/wwox/research/drug_repurposing/view/shareable_package/manifest.json",
        "disease-models/wwox/research/drug_repurposing/view/shareable_package/README.md", "disease-models/wwox/research/drug_repurposing/view/DEPLOY.md",
        "disease-models/wwox/research/drug_repurposing/view/evidence_graph.json", "disease-models/wwox/research/drug_repurposing/view/work_order.json",
        "disease-models/wwox/research/drug_repurposing/view/context_verdicts.json", "disease-models/wwox/research/drug_repurposing/view/i18n/content_en.json"]),
    ("investigations", "Investigations (research investment, not efficacy), needs and cards", [
        "disease-models/wwox/research/drug_repurposing/ranking_it*/investigations.tsv", "disease-models/wwox/research/drug_repurposing/ranking_it*/ranking.json",
        "disease-models/wwox/research/drug_repurposing/needs/needs.md", "disease-models/wwox/research/drug_repurposing/cards/*"]),
    ("open_questions", "Open-question maps and rows", ["disease-models/wwox/research/drug_repurposing/**/open_questions*"]),
    ("candidates", "Candidates, comparisons and hypothesis packages", [
        "disease-models/wwox/research/drug_repurposing/generation_it*/", "disease-models/wwox/research/drug_repurposing/**/compound_decisions*.tsv",
        "disease-models/wwox/research/drug_repurposing/**/hypotheses*"]),
    ("packages", "Completed packages and their consumer notes", [
        "disease-models/wwox/research/drug_repurposing/*/README.md", "disease-models/wwox/research/drug_repurposing/**/CONSUMER_NOTE.md"]),
    ("meetings", "MEETING round tables: attributed updates, coordination decisions and original task/source pointers; not scientific evidence or proof of delivery", [
        "disease-models/wwox/research/drug_repurposing/**/meetings/MEETING-*.md"]),
    ("diagnoses", "Diagnoses, evaluations and DREAM (a connection DREAM proposes is a question, not biological evidence)", [
        "disease-models/wwox/research/session_evaluations/*", "disease-models/wwox/research/drug_repurposing/diagnosis_*/*", "disease-models/wwox/research/dream*/README.md",
        "disease-models/wwox/research/drug_repurposing/dream*/README.md"]),
    ("memory_dismissals", "Dismissal and discovery ledgers, memory index (outside the repository)", [
        "disease-models/wwox/research/dismissal_ledger_current.md", "disease-models/wwox/research/discovery_ledger_current.md", str(MEMORY_DIR / "MEMORY.md")]),
    ("radar_science", "Scientific, pharmacological, data and method radars (opportunities, not evidence)", [
        "disease-models/wwox/research/drug_repurposing/radar_*/README.md",
        "disease-models/wwox/research/drug_repurposing/radar_*/*report*.md",
        "disease-models/wwox/research/capability_scout_log.md"]),
    ("harness_scouting", "Harness scouting and repository mining. The weekly candidate tables stop at their last week (see `last commit`); the live feed is the daily scout, whose host cache is outside the repository and is embedded in the Stage P brief by the caller", [
        "governance/candidates/HARNESS-SCOUT-*.md", str(STATE_HOME / "scout_daily_briefing.md")]),
    ("capability_surface", "What the system claims it can do, with maturity", ["SKILLS.md", "CAPABILITIES.md"]),
    ("tools", "Which tool answers which question, and what the shipped censuses and cost tools measure (the advisor has no shell; this explains what the records came from)", [
        "framework/scripts/README.md", "framework/protocols/delegation_budget.md"]),
]


def _git(*args: str, strip: bool = True) -> str:
    done = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if done.returncode != 0:
        return ""
    return done.stdout.strip() if strip else done.stdout.rstrip("\n")  # `status --porcelain` starts with a space: strip() would eat it and shift every slice


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _resolve(pattern: str) -> list[Path]:
    if os.path.isabs(pattern):
        path = Path(pattern)
        return [path] if path.exists() else []
    found = sorted(ROOT.glob(pattern.rstrip("/"))) if any(ch in pattern for ch in "*?[") else ([ROOT / pattern] if (ROOT / pattern).exists() else [])
    return [p for p in found if p.is_dir()] if pattern.endswith("/") else found


def entrypoints() -> list[dict[str, Any]]:
    """Each group with the number of files its patterns match now and the last commit that touched any of them."""
    rows = []
    for key, what, patterns in ENTRY_POINTS:
        matches = [p for pattern in patterns for p in _resolve(pattern)]
        rel = [str(p.relative_to(ROOT)) for p in matches if ROOT in p.parents]
        last = _git("log", "-1", "--format=%cI", "--", *rel[:200]) if rel else ""
        outside = [p for p in matches if p.is_file() and ROOT not in p.parents]
        if outside:                                          # a host-cache file has no commit: say its modification time and that it is one
            stamp = max(dt.datetime.fromtimestamp(p.stat().st_mtime, dt.timezone.utc) for p in outside).strftime("%Y-%m-%d") + " (file time, outside the repository)"
            last = f"{last[:10]}; {stamp}" if last else stamp
        sized = [(p.stat().st_size, p) for p in matches if p.is_file()]
        biggest = max(sized, default=(0, None), key=lambda pair: pair[0])
        rows.append({"id": key, "what": what, "patterns": patterns, "matches": len(matches), "last_commit": last,
                     "largest_chars": biggest[0], "largest": (str(biggest[1].relative_to(ROOT)) if biggest[1] and ROOT in biggest[1].parents else str(biggest[1] or ""))})
    return rows


def main_ahead() -> list[dict[str, Any]]:
    """Commits on main that this checkout does not contain, and the folders they add: material the advisor cannot read from here."""
    seen, out = set(), []
    for ref in ("development/main", "main"):
        tip = _git("rev-parse", "--verify", "--quiet", ref)
        count = _git("rev-list", "--count", f"HEAD..{ref}")
        if not tip or tip in seen or not count.isdigit() or int(count) == 0:
            continue
        seen.add(tip)
        added = _git("diff", "--name-only", "--diff-filter=A", f"HEAD...{ref}").splitlines()
        folders = sorted({"/".join(path.split("/")[:-1][:5]) for path in added if "/" in path})
        out.append({"ref": ref, "tip": tip[:12], "commits": int(count), "new_folders": folders[:12], "new_folders_total": len(folders)})
    return out


def delivery(spec: str) -> dict[str, Any]:
    """One delivery the caller announces, as `REF[:PATH]`: announced, in this snapshot, accessible from the advisor's working directory. 'Read' is filled after the run."""
    ref, _, path = spec.partition(":")
    commit = _git("rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")
    contained = bool(commit) and subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=ROOT, capture_output=True).returncode == 0
    return {"announced": spec, "ref": ref, "path": path, "ref_known": bool(commit), "in_snapshot": contained,
            "accessible": (ROOT / path).exists() if path else None}


def snapshot(extra: list[str] | None = None, expect: list[str] | None = None) -> dict[str, Any]:
    """Repository state at dispatch: SHA, time, uncommitted paths with digests, dashboard revision, what main holds that this checkout lacks."""
    dirty = []
    for line in _git("status", "--porcelain", "--untracked-files=all", strip=False).splitlines()[:200]:
        rel = line[3:].strip().strip('"')
        path = ROOT / rel
        dirty.append({"status": line[:2].strip() or "?", "path": rel, "sha256": sha256_file(path) if path.is_file() else ""})
    package = ROOT / "disease-models/wwox/research/drug_repurposing/view/shareable_package"
    manifest = package / "manifest.json"
    return {
        "repo_sha": _git("rev-parse", "HEAD"),
        "branch": _git("rev-parse", "--abbrev-ref", "HEAD"),
        "dispatch_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "uncommitted": dirty,
        "uncommitted_note": "the advisor reads the working tree: a path listed here is read as it is on disk, not as committed",
        "main_ahead": main_ahead(),
        "deliveries": [delivery(spec) for spec in expect or []],
        "dashboard": {
            "url": DASHBOARD_URL,
            "package_manifest_sha256": sha256_file(manifest) if manifest.exists() else "",
            "package_last_commit": _git("log", "-1", "--format=%H %cI", "--", str(package.relative_to(ROOT))),
            "note": "the public page shows no build stamp; the package commit above is the source revision it is generated from. Publication date of the live page was not checked.",
        },
        "extra": extra or [],
    }


def render_snapshot(snap: dict[str, Any]) -> str:
    lines = [f"- Repository SHA: `{snap['repo_sha']}` (branch `{snap['branch']}`)", f"- Dispatch time (UTC): {snap['dispatch_utc']}"]
    if snap["uncommitted"]:
        lines.append(f"- Uncommitted paths ({len(snap['uncommitted'])}; read as on disk):")
        lines += [f"  - `{d['path']}` ({d['status']}) sha256 `{d['sha256'][:16]}`" for d in snap["uncommitted"][:40]]
    else:
        lines.append("- Uncommitted paths: none")
    for ahead in snap.get("main_ahead", []):
        more = f" (first {len(ahead['new_folders'])} of {ahead['new_folders_total']})" if ahead["new_folders_total"] > len(ahead["new_folders"]) else ""
        lines.append(f"- `{ahead['ref']}` is ahead of this snapshot by {ahead['commits']} commit(s) (tip `{ahead['tip']}`); folders added there and absent here{more}: "
                     + (", ".join(f"`{f}`" for f in ahead["new_folders"]) or "none") + ". Material delivered only through those commits is not readable by the advisor.")
    if snap.get("deliveries"):
        lines += ["- Deliveries the caller announces (announced ≠ in this snapshot ≠ reachable by your tools ≠ read; 'read' is recorded after the run):",
                  "", "  | announced | in this snapshot | reachable from your working directory |", "  |---|---|---|"]
        for d in snap["deliveries"]:
            reach = "n/a (no path given)" if d["accessible"] is None else ("YES" if d["accessible"] else "NO")
            lines.append(f"  | `{d['announced']}` | {'YES' if d['in_snapshot'] else 'NO' + ('' if d['ref_known'] else ' (ref unknown here)')} | {reach} |")
        missing = [d["announced"] for d in snap["deliveries"] if not d["in_snapshot"] or d["accessible"] is False]
        if missing:
            lines.append(f"- **Not available to you:** {', '.join(f'`{m}`' for m in missing)}. Do not describe their content from memory or from the brief's wording; "
                         "list them under 'Not reached' and say what that leaves unchecked. The sibling checkout is outside your tools.")
    dash = snap["dashboard"]
    lines.append(f"- Dashboard: {dash['url']} · source revision {dash['package_last_commit'] or 'unknown'} · {dash['note']}")
    return "\n".join(lines)


def render_entrypoints(rows: list[dict[str, Any]]) -> str:
    out = ["| id | what | patterns (relative to the repository root unless absolute) | matches now | last commit | largest file |", "|---|---|---|---|---|---|"]
    for r in rows:
        big = f"`{r['largest']}` ({r['largest_chars']:,} bytes)" if r["largest_chars"] >= 20000 else ""  # only where it matters: a whole read of it is a large load every later turn pays again
        out.append(f"| {r['id']} | {r['what']} | {'<br>'.join('`' + p + '`' for p in r['patterns'])} | {r['matches']} | {r['last_commit'][:48]} | {big} |")
    return "\n".join(out)


RECALL_PROMPT = ("Proactive Strategic Advisor pilot, hourly mechanical check. Run: cd {root} && python3 framework/scripts/strategic_advisor.py tick --campaign {campaign}. "
                 "First inspect the independent meeting field: when actionable, apply cross-session transport section 13 (MEETING) and run `strategic_advisor.py meeting --campaign {campaign} --open` or resume its existing record. The ordinary verdict NONE does not cancel a due meeting. Use the hosting session, existing messages and current sources; no extra evaluation or cron is required. "
                  "Apply cross-session transport section 12, Laboratory ownership: the ADV host is accountable for programme performance and chooses the next useful question at deliveries and closures; the analyst is a consultant, not permission to act. "
                  "For EMPATHY use the tick's current operator_guidance, not a remembered instruction: choose the relevant situation, its rationale and scope; read the linked original when needed. "
                 "Apply the PERMANENT operator instruction of 2026-11-18 (roadmap_current.md, section 12 \"Autonomous scientific leadership and urgency\"): the operator is a boost, not a dependency; at each consumed delivery run the candidate-to-candidate loop (result, alternative, comparison, deepening, consumers, next choice) and say what \"more promising\" means; a general wait needs an updated evaluation and its ending condition. "
                 "If the verdict is NONE, DEFERRED, RUNNING, PAUSED, RESOURCES or DISABLED/EXPIRED/BUDGET, stay quiet unless something actionable changed; these mechanical verdicts do not establish that all useful work is exhausted: a blocked path is not a blocked portfolio, and an EVALUATE left unrun needs its excluded paths and a resume condition. If EVALUATE, apply the current legend-strategic-advisor skill: reconcile current originals, choose and register a host decision with `strategic_advisor.py assign --campaign {campaign} --text-file <FILE>` when no further consultation is useful, or start `strategic_advisor.py evaluate --campaign {campaign}` "
                 "in the background (run_in_background) for a separate perspective. Read drafted assignments with `status`, check each recipient is listed live by `claude agents --json`, "
                 "deliver each with SendMessage (durable artifact path plus pointer), record `deliver --state SENT --to <the session named in the send's receipt>` or `UNREACHABLE`, and later verify the take-in-charge in the recipient's task record. "
                 "An assignment already drafted and authorised is delivered in the turn that reads it, not at the next recall. Prepare useful work from the standing roadmap without waiting for an operator line or a distant report; read the current recipient record before claiming it is still in flight. Whatever the verdict, also read the real state (the tick's `activity` block, open records and their awaited events, the latest commits): an idle share above half without a written reason is a prompt to send, not a quiet verdict. If `python3 framework/scripts/harness_session_start.py --actor plan` reports SCOUT_DUE or TRIAGE_DUE, tell HE (plan): the weekly harness scout has no other trigger. Help a stuck session in a bounded way (find what blocks it, supply or route the input, correct your own wrong premise; never the recipient's method) and address a role only if `mandate_watch.py route --to <role>` resolves it (for an assignment recipient use the campaign map first, `recipients` in the campaign budget.json: Harness is HE, Orchestrator is IT Orchestrator, Science is SCI, and route that value; the raw role Orchestrator is AMBIGUOUS while an open mandate carries ACTOR_ID orchestrator), else keep a conditional request in the portfolio and do not record a send that did not happen. Never invent work; never write to transcripts; respect the effective operating mode and shared resources.")
RECALL_MARK = "Proactive Strategic Advisor pilot, hourly mechanical check"   # what a session looks for in CronList before creating the recall: one copy only


def recall_prompt(campaign: Path) -> str:
    """The one text of the recall. The campaign is named relative to the primary checkout so every session that restores it creates the same job."""
    rel = Path(campaign)
    rel = rel.relative_to(ROOT) if rel.is_absolute() and ROOT in rel.parents else rel
    body = RECALL_PROMPT.format(root=ROOT, campaign=rel)
    canonical = RECALL_PROMPT.format(root="<root>", campaign=rel)           # the tag must not depend on where the checkout sits (2026-11-16: the same text gave two tags with two roots)
    return body.replace(RECALL_MARK, f"{RECALL_MARK} [text {recall_digest(canonical)}]", 1)


def recall_digest(body: str) -> str:
    """2026-11-16: the installed recall had drifted from the canonical text (the sentence about the meeting was missing) and CronList shows only the head of a prompt, so the difference was found by reading the whole job. The tag sits
    right after the mark, in the part CronList shows: eight hex digits of the text without the tag and with the checkout path replaced by a placeholder, so the same text gives the same tag wherever the checkout sits. Compare the tag of the installed job with the tag `recall` prints; a different tag is a drifted job, replace it (one job only)."""
    return sha256_text(body)[:8]


def primary_refusal() -> str:
    """A linked worktree has its own copy of the campaign folder, so its budget and counters would be a second campaign; the state directory is keyed by name and would be shared."""
    if (ROOT / ".git").is_file():
        return (f"REFUSED: {ROOT} is a linked worktree. The campaign (budget.json, invocations, assignments) lives in the primary checkout; run this from "
                "the primary checkout so there is one campaign with one budget.")
    return ""


# What the id-allocating commands read from disk (ADV-243, 2026-11-25): the primary checkout is the one campaign home, and it had stayed 1,535 commits behind the published main for four days, so its commands
# read old task records, portfolio and roadmap and a draft could be numbered on old rows. A commit that touches none of these does not stop anything.
HOME_INPUTS = (":(glob)ledger/tasks/*/*.json", PORTFOLIO_REL, "disease-models/wwox/research/drug_repurposing/roadmap_current.md", "framework/protocols/cross_session_transport.md",
               "disease-models/wwox/research/drug_repurposing/view/shareable_package", "framework/scripts/strategic_advisor.py", "framework/scripts/mandate_continuity.py", "framework/scripts/mandate_watch.py")


def _git_run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def _published_tip() -> tuple[str, str]:
    """(tip, warning) of the published main after one bounded fetch that moves only the remote-tracking ref. No remote: nothing to compare with. A failed fetch is said and the last fetched ref is used."""
    if not _git("remote", "get-url", PUBLISHED_REMOTE):
        return "", ""
    warning = ""
    if os.environ.get("LEGEND_ADVISOR_NOFETCH") != "1":
        try:
            done = subprocess.run(["git", "fetch", "-q", PUBLISHED_REMOTE, "main"], cwd=ROOT, capture_output=True, text=True, timeout=FETCH_TIMEOUT_S)
            if done.returncode != 0:
                warning = (done.stderr.strip().splitlines() or ["fetch failed"])[-1][:160]
        except (OSError, subprocess.SubprocessError) as exc:
            warning = type(exc).__name__
    tip = _git("rev-parse", "--verify", "--quiet", f"refs/remotes/{PUBLISHED_REMOTE}/main")
    if warning or not tip:
        warning = f"UNVERIFIED: {PUBLISHED_REMOTE}/main could not be fetched ({warning or 'no remote-tracking ref'}); compared with the last fetched ref"
    return tip, warning


def home_inputs(campaign: Path | None) -> list[str]:
    paths = list(HOME_INPUTS)
    folder = Path(campaign).resolve() if campaign else None
    if folder and ROOT.resolve() in folder.parents:
        paths.append(folder.relative_to(ROOT.resolve()).as_posix())
    return paths


def behind_line(campaign: Path, tip: str) -> str:
    """The tick reads this checkout's files: say when they are older than the ref it observed. A line, never a refusal."""
    touched = mc.files_behind(ROOT, tip, home_inputs(campaign)) if tip else []
    if not touched:
        return ""
    return (f"CHECKOUT BEHIND on {len(touched)} file(s) this tick read ({', '.join(touched[:3])}{', …' if len(touched) > 3 else ''}): "
            f"run `strategic_advisor.py refresh --campaign {campaign}`, then tick again")


def stale_refusal(campaign: Path) -> str:
    """`assign` and `deliver` read this checkout's files: refuse while a published commit this checkout lacks touches one of them."""
    tip, warning = _published_tip()
    if warning:
        print("WARNING: " + warning, file=sys.stderr)
    if not tip:
        return ""
    touched = mc.files_behind(ROOT, tip, home_inputs(campaign))
    if touched is None:
        return f"REFUSED: cannot compare this checkout with {PUBLISHED_REMOTE}/main"
    if not touched:
        return ""
    return (f"REFUSED: this checkout is behind {PUBLISHED_REMOTE}/main on {len(touched)} file(s) that `assign` and `deliver` read ({', '.join(touched[:3])}{', …' if len(touched) > 3 else ''}). "
            f"Bring it current, then repeat: python3 framework/scripts/strategic_advisor.py refresh --campaign {campaign}")


def _blob(ref: str, path: str) -> str:
    return _git("rev-parse", "--verify", "--quiet", f"{ref}:{path}")


def _work_blob(path: str) -> str:
    full = ROOT / path
    return _git("hash-object", "--", path) if full.is_file() and not full.is_symlink() else ""


def _unlanded_rows(before: str, local: str, published: str) -> list[str] | None:
    """The rows the home appended to `assignments.jsonl` that main does not hold, when they can be put back after the fast-forward; None when they cannot: the file is not a pure append to the
    home's HEAD copy, a row is unreadable, or a draft takes a number main has already drafted (two allocations of one id). A SENT, STRAND or DREAM row naming a published id is not a collision."""
    old, new, there = before.splitlines(), local.splitlines(), published.splitlines()
    if new[:len(old)] != old:
        return None
    held = set(there)
    rows = [line for line in new[len(old):] if line.strip() and line not in held]
    try:
        taken = {row.get("id") for row in map(json.loads, filter(str.strip, there)) if row.get("state") == "DRAFTED"}
        if any(row.get("state") == "DRAFTED" and row.get("id") in taken for row in map(json.loads, rows)):
            return None
    except (ValueError, AttributeError):
        return None
    return rows


def _dirty_paths() -> dict[str, str]:
    """path -> porcelain XY. `-uall`: a new directory is listed file by file, not as one entry; `--no-renames`: one path per entry."""
    done = _git_run("status", "--porcelain", "-z", "--untracked-files=all", "--no-renames")
    if done.returncode != 0:
        raise OSError(done.stderr.strip()[:200])
    return {entry[3:]: entry[:2] for entry in done.stdout.split("\0") if entry}


def refresh(campaign: Path) -> int:
    """Fast-forward the campaign home to the published main without losing a byte. All or nothing: a local change that is not already on the published main, in a file that main changed, stops the
    refresh before anything is touched. What is replaced (bytes equal to main's, or an `assignments.jsonl` whose every line is on main) is first copied under the host state folder; unlanded rows
    appended to `assignments.jsonl` are appended again after the fast-forward and named (ADV, 2026-11-25: the ordinary case, a registration not yet landed while main moved)."""
    lock = _state_path(Path(campaign)).parent / "assignments.lock"
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open("a") as guard:
        fcntl.flock(guard, fcntl.LOCK_EX)
        return _refresh(lock.parent / "refresh" / _utc(_now()).replace(":", ""))


def _refresh(backup: Path) -> int:
    tip, warning = _published_tip()
    if warning:
        print("WARNING: " + warning, file=sys.stderr)
    if not tip:
        print("refresh: no published remote here; nothing to do"); return 0
    head = _git("rev-parse", "HEAD")
    if head == tip:
        print(f"refresh: already at {PUBLISHED_REMOTE}/main {tip[:9]}"); return 0
    if _git_run("merge-base", "--is-ancestor", head, tip).returncode != 0:
        if _git_run("merge-base", "--is-ancestor", tip, head).returncode == 0:
            print(f"refresh: {head[:9]} already contains {PUBLISHED_REMOTE}/main {tip[:9]}"); return 0
        print(f"REFUSED: HEAD {head[:9]} has commits that are not on {PUBLISHED_REMOTE}/main; land them first. Nothing was changed.", file=sys.stderr); return 2
    changed = set(_git_run("diff", "--name-only", "-z", "--no-renames", head, tip).stdout.split("\0")) - {""}
    replace, kept, blockers = [], [], []
    carry: dict[str, list[str]] = {}
    for path, code in sorted(_dirty_paths().items()):
        if path not in changed:
            kept.append(path); continue
        full = ROOT / path
        there, here = _blob(tip, path), _work_blob(path)
        absent = not full.exists() and not full.is_symlink()
        same = (bool(here) and here == there) or (absent and not there)
        if not same and here and there and Path(path).name == "assignments.jsonl":
            theirs = _git_run("show", f"{tip}:{path}").stdout
            local = full.read_text(encoding="utf-8")
            published = set(theirs.splitlines())
            same = all(line in published for line in local.splitlines())
            if not same:
                rows = _unlanded_rows(_git_run("show", f"{head}:{path}").stdout if _blob(head, path) else "", local, theirs)
                if rows is not None:
                    same, carry[path] = True, rows
        (replace if same else blockers).append(path)
    if blockers:
        print(f"REFUSED: {len(blockers)} local change(s) are not on {PUBLISHED_REMOTE}/main, in files it changed. Nothing was changed. Land them from a task worktree, then run `refresh` again:", file=sys.stderr)
        for path in blockers:
            print(f"  KEEP {path}", file=sys.stderr)
        return 2
    saved: dict[str, bytes | None] = {}
    for path in replace:
        full = ROOT / path
        saved[path] = full.read_bytes() if full.is_file() else None
        if saved[path] is not None:
            (backup / path).parent.mkdir(parents=True, exist_ok=True)
            (backup / path).write_bytes(saved[path])
    for path in replace:
        if _blob("HEAD", path):
            step = _git_run("restore", "--source=HEAD", "--staged", "--worktree", "--", path)
        else:
            step = _git_run("rm", "-q", "--cached", "--force", "--ignore-unmatch", "--", path)
            (ROOT / path).unlink(missing_ok=True)
        if step.returncode != 0:
            break
    else:
        step = _git_run("merge", "--ff-only", "--no-overwrite-ignore", "-q", tip)
    if step.returncode != 0:
        for path, data in saved.items():
            full = ROOT / path
            if data is None:
                full.unlink(missing_ok=True)
            else:
                full.parent.mkdir(parents=True, exist_ok=True)
                full.write_bytes(data)
        print(f"REFUSED: git could not fast-forward: {step.stderr.strip()[:400]}. The local files were put back.", file=sys.stderr); return 2
    for path, rows in carry.items():
        full = ROOT / path
        text = full.read_text(encoding="utf-8")
        full.write_text(text + ("" if not text or text.endswith("\n") else "\n") + "".join(row + "\n" for row in rows), encoding="utf-8")
        named = [f"{row.get('id') or ','.join(row.get('ids') or []) or '-'} {row.get('state', '?')}" for row in map(json.loads, rows)]
        print(f"refresh: re-appended {len(rows)} row(s) not yet on main to {path}: {', '.join(named)} — they still have to be landed")
    copies = sum(data is not None for data in saved.values())
    print(f"refresh: {head[:9]} -> {tip[:9]} ({PUBLISHED_REMOTE}/main); {len(replace)} local file(s) already on main replaced" + (f", copies in {backup}" if copies else "")
          + f"; {len(kept)} other local change(s) left as they were")
    for path in kept:
        print(f"  left {path}")
    return 0


CONTRACT = ("Return one assessment with the headings given in your definition. Name every file or page you opened under "
            "'Inspected'. You cannot write, run commands or start agents. The entry points are starting places; follow references past them. "
            "This brief is your prompt: the copy saved in the campaign folder is the same text, so do not open it. A file the table marks over 20,000 bytes is paid for again on every later turn: "
            "Grep for the heading or id you need and read that range, and open the whole file when the question needs all of it; never re-read a range you already hold.")


def build_brief(stage: str, campaign: Path, mission: str, constraints: str, task_record: str = "",
                assessment: Path | None = None, intended: Path | None = None, expect: list[str] | None = None) -> str:
    snap = snapshot(expect=expect)
    parts = [f"# Strategic Advisor brief — Stage {stage}", "", "## Snapshot", render_snapshot(snap), "",
             "## Mission and limits (verbatim from the caller)", mission.strip(), "",
             "## Operational constraints", constraints.strip(), ""]
    if task_record:
        parts += [f"Task record carrying the mission: `{task_record}`", ""]
    if stage == "B":
        if assessment is None or intended is None:
            raise ValueError("Stage B needs the saved Stage A assessment and the sealed intended action")
        parts += ["## Saved Stage A assessment (complete, verbatim)", f"sha256 `{sha256_file(assessment)}`", "", assessment.read_text(encoding="utf-8").strip(), "",
                  "## Orchestrator's intended action (complete, verbatim)", f"sha256 `{sha256_file(intended)}`", "", intended.read_text(encoding="utf-8").strip(), "",
                  "Begin with 'Response to the intended action': refinements, alternatives or a justified disagreement.", ""]
    parts += ["## Neutral entry points", render_entrypoints(entrypoints()), "", f"Memory directory (read-only): `{MEMORY_DIR}`", "", "## Output", CONTRACT, ""]
    return "\n".join(parts)


# ---- the run ------------------------------------------------------------------------------------------------------

def parse_stream(path: Path) -> dict[str, Any]:
    """The facts the runtime recorded about a headless run: init, per-turn model, tool calls, result."""
    init: dict[str, Any] = {}
    result: dict[str, Any] = {}
    calls: list[dict[str, Any]] = []
    models: dict[str, int] = {}
    seen: set[str] = set()
    fallbacks: list[dict[str, Any]] = []
    final_model = ""
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = event.get("type")
        if kind == "system" and event.get("subtype") == "init":
            init = event
        elif kind == "assistant":
            message = event.get("message") or {}
            ident = message.get("id")
            if ident and ident not in seen:
                seen.add(ident)
                models[str(message.get("model"))] = models.get(str(message.get("model")), 0) + 1
            if message.get("model"):
                final_model = str(message["model"])
            for block in message.get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    calls.append({"name": block.get("name"), "input": block.get("input"), "id": block.get("id")})
        elif kind == "user":
            for block in (event.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_result":
                    for call in calls:
                        if call["id"] == block.get("tool_use_id"):
                            call["is_error"] = bool(block.get("is_error"))
                            text = block.get("content")
                            call["result_head"] = (text if isinstance(text, str) else json.dumps(text))[:160]
        elif kind == "system" and event.get("subtype") == "model_refusal_fallback":
            # the runtime's own record of a model change: which model, which category; the withheld text is not kept
            fallbacks.append({k: event.get(k) for k in ("originalModel", "fallbackModel", "trigger", "apiRefusalCategory", "scope", "direction")})
        elif kind == "result":
            result = event
    return {"init": init, "result": result, "calls": calls, "turn_models": models, "fallbacks": fallbacks, "final_turn_model": final_model}


def extract_transcript(path: Path) -> str:
    """Final assistant text of a persisted transcript (a headless session or a subagent): the text blocks of its last API response."""
    last_id, blocks = None, []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = row.get("message") or {}
        if row.get("type") != "assistant" or not isinstance(message, dict):
            continue
        ident = message.get("id") or row.get("uuid")
        if ident != last_id:
            last_id, blocks = ident, []
        blocks += [b.get("text", "") for b in message.get("content") or [] if isinstance(b, dict) and b.get("type") == "text"]
    return "".join(blocks)


DELIVERY_ROW = re.compile(r"^\s*\| `([^`]+)` \| (YES|NO)[^|]*\| ([^|]+?) \|\s*$")


def deliveries_read(brief_text: str, calls: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """The four states of each announced delivery: announced and in-snapshot/reachable come from the brief, 'read' from the calls the runtime recorded."""
    rows = []
    for line in brief_text.splitlines():
        found = DELIVERY_ROW.match(line)
        if not found:
            continue
        announced, in_snapshot, reach = found.groups()
        path = announced.partition(":")[2]
        done = [c for c in calls if not c.get("is_error")]
        files = [c for c in done if c.get("name") == "Read" and path and path in str((c.get("input") or {}).get("file_path") or "")]
        looked = [c for c in done if c.get("name") in ("Grep", "Glob") and path and path in json.dumps(c.get("input") or {})]
        rows.append({"announced": announced, "in_snapshot": in_snapshot == "YES", "reachable": reach.strip(), "files_read": len(files), "listed_or_searched": len(looked)})
    return rows


def _transcript_for(session_id: str) -> Path | None:
    override = os.environ.get("LEGEND_ADVISOR_TRANSCRIPTS")
    bases = [Path(override)] if override else sorted((Path.home() / ".claude" / "projects").glob("*"))
    for base in bases:
        if (base / f"{session_id}.jsonl").exists():
            return base / f"{session_id}.jsonl"
    return None


def _attempts(campaign: Path) -> list[dict[str, Any]]:
    log = campaign / "invocations.jsonl"
    return [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines() if line.strip()] if log.exists() else []


def _append(campaign: Path, row: dict[str, Any]) -> None:
    campaign.mkdir(parents=True, exist_ok=True)
    with (campaign / "invocations.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")


def claude_command(model: str, effort: str) -> list[str]:
    binary = os.environ.get("LEGEND_ADVISOR_CLAUDE", "claude")
    cmd = [binary, "-p", "--agent", AGENT, "--model", model, "--effort", effort, "--output-format", "stream-json", "--verbose",
           "--tools", ",".join(TOOLS), "--allowedTools", "WebFetch", "--disallowedTools", *DENIED,
           "--permission-mode", "dontAsk", "--strict-mcp-config", "--disable-slash-commands"]
    # Not --restricted: it also hides the project agents (measured 2026-11-12, `--agent` not found). Reads outside the working directory and the added memory directory
    # are not allowed by any rule, so dontAsk denies them; that is the runtime's default behaviour, checked in the smoke record.
    if MEMORY_DIR.is_dir():
        cmd += ["--add-dir", str(MEMORY_DIR)]
    return cmd


class _Done:
    def __init__(self, returncode: int, turn_limit_hit: bool) -> None:
        self.returncode, self.turn_limit_hit = returncode, turn_limit_hit


def _launch_limited(cmd: list[str], text: str, stream, err, timeout: int, turn_limit: int) -> _Done:
    """Run the advisor and stop it ourselves when it exceeds `turn_limit` assistant turns. `claude -p` has no turn-limit flag on this host (checked 2026-11-13), so this limit is
    enforced by the launcher that owns the child process, not configured in the runtime; the attempt counts, and the stream up to the stop is kept."""
    import threading
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=err, text=True, cwd=ROOT)
    timer = threading.Timer(timeout, proc.terminate)
    timer.start()
    proc.stdin.write(text); proc.stdin.close()
    seen: set[str] = set(); hit = False
    for line in proc.stdout:
        stream.write(line); stream.flush()
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "assistant":
            ident = (event.get("message") or {}).get("id")
            if ident:
                seen.add(ident)
            if len(seen) > turn_limit:
                hit = True
                proc.terminate()
                break
    code = proc.wait()
    timer.cancel()
    return _Done(code, hit)


def run(stage: str, campaign: Path, brief: Path, model: str, effort: str, timeout: int, limits: dict[str, int], extra_reason: str = "") -> int:
    limits = stage_limits(Path(campaign), limits)
    refusal = budget_refusal(campaign)
    if refusal:
        print(f"CEILING: {refusal}. This ceiling is procedural: it binds runs launched through this tool only.", file=sys.stderr)
        return 2
    turn_limit = int(_budget(campaign).get("turn_limit") or 0)
    used = {a["index"] for a in _attempts(campaign) if a.get("stage") == stage}  # a log row is written at launch and again at the end: count attempts once
    extra = False
    if limits[stage] is not None and len(used) >= limits[stage] and extra_reason:
        # one recorded extra attempt per stage, and only when every earlier attempt of the stage produced no assessment
        concluded = [a for a in _attempts(campaign) if a.get("stage") == stage and a["outcome"] not in ("STARTED", "OK")]
        if len(concluded) == len(used) and not any(a.get("extra") for a in _attempts(campaign) if a.get("stage") == stage):
            extra = True
    if limits[stage] is not None and len(used) >= limits[stage] and not extra:
        print(f"CEILING: stage {stage} already has {len(used)} attempt(s) in {campaign} (limit {limits[stage]}); failed attempts count. "
              "This ceiling is procedural: it binds runs launched through this tool only.", file=sys.stderr)
        return 2
    index = max(used, default=0) + 1
    label = f"{stage}{index}"
    final_out = campaign / label
    out = STATE_DIR / "runs" / f"{campaign.name}-{label}"           # 2026-11-16: assembled outside the shared checkout, moved in one step at the end (a half-written untracked folder in the root blocks every landing)
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True, exist_ok=True)
    raw_dir = Path(os.environ.get("LEGEND_ADVISOR_RAW", "/tmp/legend-advisor-raw")) / f"{campaign.name}-{label}"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw = raw_dir / "stream.jsonl"
    (out / "brief.md").write_text(brief.read_text(encoding="utf-8"), encoding="utf-8")
    started = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    row = {"stage": stage, "index": index, "label": label, "started_utc": started, "model_asked": model, "effort_asked": effort,
           "brief_sha256": sha256_file(brief), "outcome": "STARTED"}
    if extra:
        row.update(extra=True, extra_reason=extra_reason)
    _append(campaign, row)  # logged before the launch: a crash or a timeout still counts
    outcome, code = "FAILED", 1
    try:
        with raw.open("w", encoding="utf-8") as stream, (raw_dir / "stderr.txt").open("w", encoding="utf-8") as err:
            if turn_limit:
                done = _launch_limited(claude_command(model, effort), brief.read_text(encoding="utf-8"), stream, err, timeout, turn_limit)
            else:
                done = subprocess.run(claude_command(model, effort), input=brief.read_text(encoding="utf-8"), text=True, stdout=stream, stderr=err,
                                      cwd=ROOT, timeout=timeout)
        facts = parse_stream(raw)
        result = facts["result"]
        text = result.get("result") if isinstance(result.get("result"), str) else ""
        ok = done.returncode == 0 and result.get("subtype") == "success" and not result.get("is_error") and bool(text.strip())
        if ok:
            (out / "assessment.md").write_text(text, encoding="utf-8")
        session = str(result.get("session_id") or facts["init"].get("session_id") or "")
        transcript = _transcript_for(session) if session else None
        agrees = (extract_transcript(transcript).strip() == text.strip()) if transcript and ok else None
        census = {}
        if transcript:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            from session_model_census import census as _census  # noqa: PLC0415 — reuse of the existing reader
            census = {k: v for k, v in _census(transcript).items() if k in ("turns", "models", "changed_mid_run", "first_turn_context", "peak_context", "efforts", "totals")}
        meta = {
            "stage": stage, "label": label, "snapshot_note": "see the brief for the dispatch snapshot", "started_utc": started,
            "ended_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "profile": {"agent": AGENT, "model_asked": model, "effort_asked": effort, "tools_flag": TOOLS, "denied": DENIED, "restricted": False, "permission_mode": "dontAsk"},
            "runtime_readback": {"init_tools": facts["init"].get("tools"), "init_mcp_servers": facts["init"].get("mcp_servers"), "init_model": facts["init"].get("model"),
                                 "init_permission_mode": facts["init"].get("permissionMode"), "turn_models": facts["turn_models"],
                                 "model_usage": result.get("modelUsage"), "usage": result.get("usage"), "num_turns": result.get("num_turns"),
                                 "final_turn_model": facts["final_turn_model"], "refusal_fallbacks": facts["fallbacks"],
                                 "total_cost_usd": result.get("total_cost_usd"), "census": census},
            "capture": {"method": "runtime result event of the headless stream (stream-json), saved verbatim", "source_session_id": session,
                        "raw_stream": str(raw), "raw_stream_sha256": sha256_file(raw), "assessment_sha256": sha256_text(text) if ok else "",
                        "transcript_cross_check": agrees, "transcribed_by_caller": False,
                        "published": "assessment.md and this file only; the raw stream and the session transcript stay local"},
            "tool_calls": [{k: c.get(k) for k in ("name", "input", "is_error", "result_head")} for c in facts["calls"]],
            "context": {"brief_chars": len(brief.read_text(encoding="utf-8"))},
            "deliveries": deliveries_read(brief.read_text(encoding="utf-8"), facts["calls"]),
        }
        (out / "meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True), encoding="utf-8")
        outcome, code = ("OK" if ok else "FAILED"), (0 if ok else 1)
        if getattr(done, "turn_limit_hit", False):
            outcome = "TURN_LIMIT"
        if not ok:
            print(f"run failed: returncode={done.returncode} subtype={result.get('subtype')} — see {raw_dir}/stderr.txt and {raw}", file=sys.stderr)
    except subprocess.TimeoutExpired:
        outcome = "TIMEOUT"
        print(f"timeout after {timeout}s; the attempt is counted", file=sys.stderr)
    except OSError as error:
        print(f"could not launch: {error}", file=sys.stderr)
    final_out.mkdir(parents=True, exist_ok=True)
    for item in sorted(out.iterdir()):
        os.replace(item, final_out / item.name) if item.is_file() else shutil.copytree(item, final_out / item.name, dirs_exist_ok=True)
    shutil.rmtree(out, ignore_errors=True)
    _append(campaign, {**row, "outcome": outcome, "ended_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
    print(f"{label}: {outcome} → {final_out}")
    return code


def check(campaign: Path) -> int:
    """Re-verify saved assessments against their metadata, stage B against stage A, and the attempt counts."""
    problems = []
    attempts = _attempts(campaign)
    started = [a for a in attempts if a["outcome"] == "STARTED"]
    ended = {(a["stage"], a["index"]) for a in attempts if a["outcome"] != "STARTED"}
    for a in started:
        if (a["stage"], a["index"]) not in ended:
            problems.append(f"{a['label']}: started and never concluded (counts as an attempt)")
    ceilings = stage_limits(campaign)
    for stage in LIMITS:
        n = len({a["index"] for a in attempts if a["stage"] == stage})
        extras = len({a["index"] for a in attempts if a["stage"] == stage and a.get("extra")})
        if ceilings[stage] is not None and n > ceilings[stage] + extras:
            problems.append(f"stage {stage}: {n} attempts exceed the ceiling {ceilings[stage]}")
    for meta_path in sorted(campaign.glob("*/meta.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        assessment = meta_path.parent / "assessment.md"
        if not assessment.exists():
            if not any(a["label"] == meta_path.parent.name and a["outcome"] in ("FAILED", "TIMEOUT") for a in attempts):
                problems.append(f"{meta_path.parent.name}: meta without assessment")
            continue
        if sha256_file(assessment) != meta["capture"]["assessment_sha256"]:
            problems.append(f"{meta_path.parent.name}: assessment.md no longer matches the captured digest")
        if meta["capture"].get("transcript_cross_check") is False:
            problems.append(f"{meta_path.parent.name}: result event and session transcript disagree")
        readback = meta["runtime_readback"]
        if readback.get("census", {}).get("changed_mid_run"):
            fell = readback.get("refusal_fallbacks") or []
            if fell:  # explained by the runtime: disclose it, name the model that wrote the answer, do not call it a failure of the saved record
                print(f"NOTE: {meta_path.parent.name}: model changed mid-run by runtime fallback ({fell[0].get('originalModel')} → {fell[0].get('fallbackModel')}, "
                      f"{fell[0].get('trigger')}/{fell[0].get('apiRefusalCategory')}); per-turn {readback['census'].get('models')}; final turn on {readback.get('final_turn_model')}; the assessment is not a single-model product")
            else:
                problems.append(f"{meta_path.parent.name}: the model changed mid-run, and the runtime recorded no reason")
        for d in meta.get("deliveries", []):
            if not d["in_snapshot"] or d["reachable"].startswith("NO"):
                print(f"NOTE: {meta_path.parent.name}: announced delivery {d['announced']} was not available to the advisor (read {d['files_read']} file(s), searched {d['listed_or_searched']} time(s))")
        # an attempt the runtime refused (is_error) is the deny rule working; only a call that went through counts as having opened it
        opened = {str((c.get("input") or {}).get("file_path") or (c.get("input") or {}).get("path") or "") for c in meta["tool_calls"] if not c.get("is_error")}
        text = assessment.read_text(encoding="utf-8")
        if "Inspected" not in text:
            problems.append(f"{meta_path.parent.name}: no 'Inspected' section")
        brief_hint = [p for p in opened if SEALED in p]
        if brief_hint:
            problems.append(f"{meta_path.parent.name}: the advisor opened a sealed path: {brief_hint}")
    for b in sorted(campaign.glob("B*/")):
        brief = b / "brief.md"
        if brief.exists():
            digests = [line for line in brief.read_text(encoding="utf-8").splitlines() if line.startswith("sha256 `")]
            saved = {sha256_file(p) for p in campaign.glob("A*/assessment.md")}
            if not any(d.split("`")[1] in saved for d in digests):
                problems.append(f"{b.name}: its brief does not embed any saved Stage A assessment")
    for a in attempts:
        if a.get("extra") and a["outcome"] == "STARTED":
            print(f"NOTE: {a['label']} was an extra attempt beyond the ceiling — {a['extra_reason']}")
    for p in problems:
        print("PROBLEM:", p)
    print("check: " + ("OK" if not problems else f"{len(problems)} problem(s)"), f"· attempts: " + ", ".join(f"{s}={len({a['index'] for a in attempts if a['stage'] == s})}" for s in LIMITS))
    return 0 if not problems else 1


# ---- the proactive pilot: observe, decide whether an evaluation is due, prepare assignments, follow them ----------------------------------------------------
# One schedule drives it (an hourly in-session cron that runs `tick`), because delivery to a live session needs a session that can send a message; the host crontab already
# runs the mandate watch and this tool does not repeat it. Everything here is derived from files that already exist: the roadmap section, the task records, the commits of
# main, the mandate watch's own event log and the runtime's list of sessions. The advisor stays read-only; its assignments are text this tool saves.
ROADMAP = ROOT / "disease-models/wwox/research/drug_repurposing/roadmap_current.md"
ROADMAP_BEGIN, ROADMAP_END = "<!-- OPERATOR_ROADMAP:BEGIN -->", "<!-- OPERATOR_ROADMAP:END -->"
STATE_DIR = Path(os.environ.get("LEGEND_ADVISOR_STATE", str(Path.home() / ".local/state/legend/advisor_pilot")))
ASSIGNMENT_FIELDS = ("key", "recipient", "question", "why_now", "roadmap_link", "related_work", "sources", "decision_changed_by_result", "perimeter_and_budget",
                     "method_autonomy", "deliver_to", "duplicate_check")
OPTIONAL_FIELDS = ("mode", "start_condition", "interferes_with", "obsolete_if", "strand")   # HE54: what a recipient needs to place a follow-through: independent | queued | conditional, when it can start, what it may disturb, what makes it useless
OPEN_VERDICTS = ("CONTINUE", "ALL_BLOCKED", "COMPLETE_PENDING")
EVENT_SUBJECT = re.compile(r"COMPLETE|closed|closure|integrate task|delivered|consumed|landed", re.I)
OUTCOMES = ("continue", "switch", "assign", "queue", "wait")        # HE57: the allowed endings of an evaluation; a wait is one of them, and states what it excluded and when it resumes
OUTCOME_FIELDS = ("outcome", "excluded", "reason", "resume_when")
MIN_CALLS_AFTER_FALLBACK = 8        # a run the runtime cut short by a refusal fallback and that opened fewer files than this reasoned from almost nothing (P11, 2026-11-15: 4 calls; P10 went on to 17 and was usable)


def _now() -> dt.datetime:
    forced = os.environ.get("LEGEND_ADVISOR_NOW")
    return dt.datetime.fromisoformat(forced.replace("Z", "+00:00")) if forced else dt.datetime.now(dt.timezone.utc)


def _utc(when: dt.datetime) -> str:
    return when.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _budget(campaign: Path) -> dict[str, Any]:
    path = Path(campaign) / "budget.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


CONTINUOUS = "CONTINUOUS.json"
CONTROL_LINE = re.compile(r"^\s*(?:[-*]\s*)?(PAUSE|STOP|RESUME|URGENT|INTEGRATION)\s*:\s*(.+?)\s*$", re.M)
ADVISOR_SCOPES = ("all", "advisor", "adv", "presidio", "strategic advisor")
ALLOCATION_UNITS = ("output_tokens", "cache_read_tokens")
EVALUATION_USAGE_SCOPE = (
    "Saved model evaluations of this campaign only; excludes the ADV hosting session, "
    "IT/SCI/HE and their delegates. Unmeasured work is not zero-cost. "
    "These observations do not establish total laboratory use or remaining account quota. "
    "Use the existing session_model_census.py / trial_window_table.py for a stated laboratory window."
)


def continuous(campaign: Path) -> dict[str, Any]:
    """The operator's persistent authorisation to continue inside the roadmap, or {} when there is none (or it was ended). It is a mode of the campaign, not a second campaign: the pilot's budget,
    counters, results and failures stay exactly as they were, and removing the file returns the campaign to its bounded pilot rules."""
    path = Path(campaign) / CONTINUOUS
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {} if data.get("ended_utc") else data


def operator_controls(text: str | None = None) -> list[dict[str, str]]:
    """Operator control lines in the roadmap section, in order: `PAUSE: <scope> — why`, `STOP: <scope>`, `RESUME: <scope>` (lifts that scope; `RESUME: all` lifts every one), `URGENT: ...`, `INTEGRATION: ...`.
    The roadmap section is the canonical seat of the operator's chat instructions (sessions transcribe them there); nothing here asks the operator for a second place."""
    block = roadmap_text() if text is None else text
    return [{"kind": m.group(1), "text": m.group(2), "scope": re.split(r"\s+[\u2014-]\s+|;|\(", m.group(2), maxsplit=1)[0].strip().lower()} for m in CONTROL_LINE.finditer(block)]


def active_suspensions(controls: list[dict[str, str]]) -> list[dict[str, str]]:
    live: list[dict[str, str]] = []
    for c in controls:
        if c["kind"] in ("PAUSE", "STOP"):
            live.append(c)
        elif c["kind"] == "RESUME":
            live = [x for x in live if c["scope"] != "all" and x["scope"] != c["scope"]]
    return live


def advisor_suspension(campaign: Path) -> str:
    """The text of an operator pause or stop that covers the Advisor presidio, or ''. A suspension scoped to another perimeter is reported to the evaluation, not applied here."""
    mine = [c for c in active_suspensions(operator_controls()) if c["scope"] in ADVISOR_SCOPES or "advisor" in c["scope"]]
    return f"{mine[-1]['kind']}: {mine[-1]['text']}" if mine else ""


def measured_use(campaign: Path, since: dt.datetime) -> dict[str, int]:
    """What the saved evaluations of this campaign measurably used since `since`, read from their own runtime read-back (never estimated, never converted to a share of a plan)."""
    out = {"evaluations": 0, "output_tokens": 0, "cache_read_tokens": 0}
    for meta in sorted(Path(campaign).glob("*/meta.json")):
        try:
            m = json.loads(meta.read_text(encoding="utf-8"))
            started = dt.datetime.fromisoformat(m["started_utc"].replace("Z", "+00:00"))
        except (OSError, json.JSONDecodeError, KeyError, ValueError):
            continue
        if started >= since:
            totals = (m.get("runtime_readback") or {}).get("census", {}).get("totals", {})
            out["evaluations"] += 1; out["output_tokens"] += int(totals.get("output", 0)); out["cache_read_tokens"] += int(totals.get("cache_read", 0))
    return out


def weekly_state(campaign: Path) -> dict[str, Any]:
    """The Advisor's slice of the shared weekly allocation. The usable limit is the operator's to state (the runtime does not expose it): without a value the state is 'unset' and nothing is blocked."""
    alloc = (continuous(campaign).get("weekly_allocation") or {})
    used = measured_use(campaign, _now() - dt.timedelta(days=7))
    limit, share, unit = alloc.get("usable_limit"), alloc.get("advisor_share"), alloc.get("unit")
    if not (limit and share and unit in ALLOCATION_UNITS):
        return {"state": "unset", "measured_7d": used, "measurement_scope": EVALUATION_USAGE_SCOPE,
                "note": "usable weekly limit not given by the operator and not exposed by the runtime: nothing is blocked and no value is assumed"}
    cap = float(limit) * float(share)
    spent = used[unit]
    return {"state": "exhausted" if spent >= cap else "near" if spent >= 0.8 * cap else "ok", "measured_7d": used,
            "measurement_scope": EVALUATION_USAGE_SCOPE, "unit": unit, "advisor_cap": cap, "advisor_spent": spent}


def stage_limits(campaign: Path, limits: dict[str, int] = LIMITS) -> dict[str, int | None]:
    """The per-stage attempt ceilings. They are the whole rule only without a budget file; with one, the campaign's total (`budget_refusal` counts every stage together, expiry and the disable
    flag included) governs, so a stage may use up to that total: the operator's amendment to 5 invocations was refused at the fourth Stage P run by the stale per-stage 3 (2026-11-14)."""
    if continuous(campaign):
        return {stage: None for stage in limits}            # a declared mode, not a big number: the pilot's per-stage ceilings are not the rule of continuous operation
    total = int(_budget(campaign).get("max_invocations") or 0)
    return {stage: max(n, total) for stage, n in limits.items()} if total else dict(limits)


def budget_refusal(campaign: Path) -> str:
    """Why no further invocation may start in this campaign, or '' (no budget file: the earlier per-stage ceilings apply alone)."""
    b = _budget(campaign)
    if not b:
        return ""
    if (Path(campaign) / "DISABLED").exists():
        return "the campaign is disabled"
    if continuous(campaign):
        # continuous operation: the pilot's expiry and total are historical and do not apply; what binds is the operator's pause or stop, and the shared weekly allocation when it is known
        held = advisor_suspension(campaign)
        if held:
            return f"operator suspension in the roadmap section ({held}); lifted only by a RESUME line"
        week = weekly_state(campaign)
        if week["state"] == "exhausted":
            return f"the Advisor's slice of the weekly allocation is spent ({week['advisor_spent']} of {week['advisor_cap']:.0f} {week['unit']}, measured): checkpoint, verify and deliver open work, no widening"
        return ""
    if b.get("expires_utc") and _now() >= dt.datetime.fromisoformat(b["expires_utc"].replace("Z", "+00:00")):
        return f"the campaign expired at {b['expires_utc']} (no automatic renewal)"
    used = len({(a["stage"], a["index"]) for a in _attempts(Path(campaign))})
    if used >= int(b.get("max_invocations", 10**9)):
        return f"the campaign has used its {used} of {b['max_invocations']} strategic invocations (failed attempts count)"
    return ""


def roadmap_text() -> str:
    text = ROADMAP.read_text(encoding="utf-8") if ROADMAP.exists() else ""
    if ROADMAP_BEGIN in text and ROADMAP_END in text:
        return text.split(ROADMAP_BEGIN, 1)[1].split(ROADMAP_END, 1)[0].strip()
    return ""


def _state_path(campaign: Path) -> Path:
    return STATE_DIR / Path(campaign).name / "state.json"


def _load_state(campaign: Path) -> dict[str, Any]:
    path = _state_path(campaign)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _save_state(campaign: Path, state: dict[str, Any]) -> None:
    path = _state_path(campaign)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=1, sort_keys=True), encoding="utf-8")


# MEETING reuses the existing host and hourly recall. Its small host cache is separate
# from evaluation state, so an evaluation finishing cannot erase a later meeting request.
MEETING_ROLES = ("adv", "orchestrator", "science", "harness", "mirror")


def _meeting_saved(campaign: Path) -> dict[str, Any]:
    path = _state_path(campaign).with_name("meeting.json")
    if path.exists():
        saved = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(saved, dict):
            raise ValueError("MEETING cache must be an object; reconcile it with existing minutes")
        active = saved.get("active") or ""
        if active and (Path(active).name != active or not (campaign / "meetings" / active).is_file()):
            raise ValueError("MEETING's open record is missing or invalid; reconcile its original before reopening")
        return saved
    # A move to a new host can recover the cadence/open record from committed minutes.
    # Requests not yet put in minutes remain a host-cache/transport recovery limit.
    rows = []
    for p in (campaign / "meetings").glob("MEETING-*.md"):
        text = p.read_text(encoding="utf-8")
        stamp = re.search(r"^Started UTC: (\S+)$", text, re.M)
        if stamp:
            # Among records of one start second the open one is the newest (a new one opens only after the last closed); file times can tie or invert.
            rows.append((stamp[1], not re.search(r"^Closed UTC: \S+$", text, re.M), p.stat().st_mtime_ns, p.name))
    if not rows:
        return {}
    started, still_open, _, name = max(rows)
    return {"last_started_utc": started, "active": name if still_open else "",
            "recovered_from_minutes": True}


MEETING_LEAD_MIN = 45


def meeting_status(campaign: Path, saved: dict[str, Any] | None = None) -> dict[str, Any]:
    """Read-only six-hour/event alignment status; no model, message or task launch."""
    saved = _meeting_saved(campaign) if saved is None else saved
    mode = continuous(campaign)
    interval = float(mode.get("meeting_interval_hours", 6))
    if interval <= 0 or not interval < float("inf"):
        raise ValueError("meeting_interval_hours must be a finite positive number")
    anchor = saved.get("last_started_utc") or mode.get("authorised_utc") or _budget(campaign).get("activated_utc")
    due_at = (dt.datetime.fromisoformat(anchor.replace("Z", "+00:00")) + dt.timedelta(hours=interval)) if anchor else _now()
    requests = saved.get("requests") or []
    active = saved.get("active") or ""
    held = "disabled outside continuous operation" if not mode or mode.get("meeting_enabled") is False else budget_refusal(campaign)
    if (campaign / "DISABLED").exists():
        held = "campaign disabled"
    if not held and _running(_load_state(campaign)):
        held = "a strategic evaluation is running; align at its next safe boundary"
    ready = bool(active or requests or _now() >= due_at)
    # 2026-11-20 (ADV, 'Reliable autonomy'): a due time that fell within a minute of the hourly recall was a coin flip that cost a full hour when missed (the 05:36Z meeting was opened 41 minutes late). The minutes of both are
    # not fixed: due times follow the previous meeting's start and the recall follows whatever job the host armed. A meeting due within the next `meeting_lead_minutes` (default 45) is actionable as DUE_SOON, so the check just before the due time opens it; no second timer. Opening early moves the next
    # due time earlier by at most that lead (a reasoned shift, recorded in the new minutes' Started UTC).
    lead = float(mode.get("meeting_lead_minutes", MEETING_LEAD_MIN))
    soon = (not ready) and lead > 0 and _now() >= due_at - dt.timedelta(minutes=lead)
    return {"state": "HELD" if held else "OPEN" if active else "DUE" if ready else "DUE_SOON" if soon else "IDLE",
            "actionable": (ready or soon) and not held, "why": held or ("resume the existing round table" if active else "meaningful event request" if requests else "six-hour alignment" if ready
                                                                          else f"six-hour alignment due at {_utc(due_at)}, within {round(lead)} minutes: open it at this check, the next one would be up to an hour late" if soon else "not due"),
            "next_due_utc": _utc(due_at), "interval_hours": interval,
            "record": str(campaign / "meetings" / active) if active else "",
            "requests": requests, "recovery": saved.get("recovered_from_minutes", False)}


def meeting(campaign: Path, *, request: str = "", source: str = "", actor: str = "",
            open_round: bool = False, close_file: Path | None = None) -> dict[str, Any]:
    """Host-owned alignment, not a second work queue. Peers request it via SendMessage.

    The host records the request, opens one source-linked agenda, then closes it with
    actual participant replies/decisions supplied verbatim. Sending and acceptance are
    evidenced by existing transport, never inferred from opening or closing minutes.
    """
    campaign = Path(campaign)
    actions = int(bool(request)) + int(open_round) + int(close_file is not None)
    if actions > 1:
        raise ValueError("choose one meeting action")
    if not actions:
        return meeting_status(campaign)
    if request and (actor not in MEETING_ROLES or not source.strip() or not request.strip()):
        raise ValueError("a request needs a participant role, a durable source and its coordination reason")
    cache = _state_path(campaign).with_name("meeting.json")
    cache.parent.mkdir(parents=True, exist_ok=True)
    with cache.with_suffix(".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        saved = _meeting_saved(campaign)
        if request:
            key = sha256_text(source.strip() + "|" + request.strip())[:20]
            # Active and already considered signals coalesce; a material new event
            # needs a new source revision/reason. An old message is not a new meeting.
            known = {r["key"] for r in saved.get("requests", [])} | set(saved.get("handled_keys", []))
            if key not in known:
                saved.setdefault("requests", []).append({"key": key, "actor": actor, "source": source.strip(), "reason": request.strip(), "utc": _utc(_now())})
        elif open_round:
            status = meeting_status(campaign, saved)
            if status["state"] == "OPEN":
                return status
            if not status["actionable"]:
                return status
            folder = campaign / "meetings"
            folder.mkdir(parents=True, exist_ok=True)
            stamp = _utc(_now())
            fd, filename = tempfile.mkstemp(prefix="MEETING-" + _now().strftime("%Y%m%dT%H%M%SZ") + "-", suffix=".md", dir=folder)
            os.close(fd)
            path = Path(filename)
            records = _records()
            tasks = [f"- {t}: {r['owner']}; {r['verdict']}; `{r['path']}`" for t, r in records.items() if r.get("state") == "OPEN"]
            signals = [f"- {r['actor']}: {r['reason']} — {r['source']}" for r in saved.get("requests", [])]
            text = (f"# MEETING — {stamp}\n\nStarted UTC: {stamp}\nSnapshot SHA: {_git('rev-parse', 'HEAD')}\n"
                    "Coordination: ADV (direction), Orchestrator (execution and upward report).\n\n"
                    "## Trigger and source index\n" + "\n".join(signals or ["- Six-hour alignment."]) + "\n\n"
                    "## Derived agenda — not participant statements\n"
                    f"Roadmap: `{ROADMAP.relative_to(ROOT)}`\nPortfolio: `{PORTFOLIO_REL}`\n"
                    "Read current priority, pending steps and source material through these existing records; this index does not reprioritise or replace them.\n"
                    + "\n".join(tasks or ["- No open task record found; this does not prove no useful work remains."]) + "\n\n"
                    "## Round table and decisions\n"
                    "Opening state under cross-session transport section 13: ADV, Orchestrator, Science, Harness and Mirror are not yet consulted. Closing notes below record actual follow-through. "
                    "Use live named recipients and actual replies; unavailable or late participants do not block decisions.\n")
            path.write_text(text, encoding="utf-8")
            saved.update(active=path.name, last_started_utc=stamp,
                         active_keys=[r["key"] for r in saved.get("requests", [])])
        else:
            active = saved.get("active") or ""
            if not active:
                raise ValueError("no open meeting to close")
            notes = Path(close_file).read_text(encoding="utf-8")
            if not notes.strip():
                raise ValueError("closing notes must state actual replies, decisions or an explicit no-change/partial result")
            path = campaign / "meetings" / active
            # Append the host's notes exactly; no model rewrite and no false ACK.
            with path.open("a", encoding="utf-8") as handle:
                handle.write("\n## Host closing notes (supplied verbatim)\n\n" + notes + "\n\nClosed UTC: " + _utc(_now()) + "\n")
            consumed = set(saved.get("active_keys", []))
            saved["requests"] = [r for r in saved.get("requests", []) if r["key"] not in consumed]
            saved["handled_keys"] = sorted(set(saved.get("handled_keys", [])) | consumed)
            saved.update(active="", active_keys=[], last_record=str(path))
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=cache.parent, delete=False) as handle:
            tmp = Path(handle.name)
            handle.write(json.dumps(saved, indent=1, sort_keys=True) + "\n")
        os.replace(tmp, cache)
        return meeting_status(campaign, saved)


def _pid_identity(pid: int) -> str:
    try:
        return f"{pid}:{Path(f'/proc/{pid}/stat').read_text().rsplit(')', 1)[1].split()[19]}"
    except (OSError, IndexError):
        return ""


def _running(state: dict[str, Any]) -> bool:
    ident = state.get("running") or ""
    return bool(ident) and _pid_identity(int(ident.split(":")[0])) == ident


def _records() -> dict[str, dict[str, Any]]:
    """Task id -> {state, owner, objective} from the task records; a mandate that carries no state reads as unknown, never as open."""
    out = {}
    for path in sorted((ROOT / "ledger" / "tasks").glob("*/*.json")):
        try:
            d = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(d, dict) and d.get("TASK_ID"):
            try:
                state = str(mc.verdict(d)["verdict"])        # the continuity module's own reading of the queue, not a second one
            except Exception:  # noqa: BLE001 — a record the module cannot read is reported as such
                state = "UNREADABLE"
            out[d["TASK_ID"]] = {"state": "OPEN" if state in OPEN_VERDICTS else state, "verdict": state, "owner": path.parent.name, "path": str(path.relative_to(ROOT))}
    return out


def _sessions() -> dict[str, str] | None:
    agents = _agents()
    return None if agents is None else {str(x.get("name")): str(x.get("status")) for x in agents}


STALE_SESSION_MIN = 1440   # a session whose transcript has not been written for a day is listed but not counted in the idle share: measured, two such sessions were 12 and 6 days quiet
PROJECTS_DIR = Path.home() / ".claude" / "projects"   # where each session's transcript lives; only its modification time is read


def _agents() -> list[dict[str, Any]] | None:
    try:
        import mandate_watch as mw     # claude_bin(): PATH first, then ~/.local/bin/claude: an in-session shell may not have it on PATH (2026-11-19: the whole activity block was silently absent at every in-session tick)
        done = subprocess.run([os.environ.get("LEGEND_ADVISOR_CLAUDE") or mw.claude_bin(), "agents", "--json"], capture_output=True, text=True, timeout=25)
        data = json.loads(done.stdout) if done.returncode == 0 else None
        return data if isinstance(data, list) else None
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError):
        return None


def unpublished_main(now: dt.datetime) -> dict[str, Any]:
    """HE62: commits that local `main` holds and the remote's `main` does not, with the age of the oldest. A peer waiting for 'the landing on development/main' cannot see that the awaited event exists on the root checkout's local
    main (measured 2026-11-15: about 100 minutes). Offline: it compares with the last fetched remote ref and says how old that fetch is, never fetches."""
    for ref in ("development/main", "origin/main"):
        if _git("rev-parse", "--verify", "-q", ref):
            break
    else:
        return {"available": False, "reason": "no remote main ref known offline"}
    stamps = [t for t in _git("log", f"{ref}..main", "--format=%ct").split() if t.isdigit()]
    fetch = Path(_git("rev-parse", "--path-format=absolute", "--git-common-dir") or ".") / "FETCH_HEAD"
    return {"available": True, "against": ref, "commits": len(stamps), "oldest_min": round((now.timestamp() - min(int(t) for t in stamps)) / 60) if stamps else None,
            "ref_checked_min_ago": round((now.timestamp() - fetch.stat().st_mtime) / 60) if fetch.exists() else None}


IDLE_NAMED_MIN = 60      # a recipient idle longer than this, with no blocker that names it, is reported on the tick line

# 2026-11-20 (HE, operator's morning continuation): the restart lines of README section 13 (250k at a closed increment, 350k at the next sub-step, 400k never later) were read by nobody: SCI window
# 2d2e7085 crossed 250k at 00:44Z, 350k at 01:03Z and 400k at 01:16Z and was replaced at 02:08Z at 599k. The tick now prints each recipient's CURRENT context, so the line is read, not remembered.
CONTEXT_LINES = ((400_000, "past the never-later line"), (350_000, "restart at the next sub-step boundary"), (250_000, "restart at a closed increment"))
CONTEXT_TAIL_BYTES = 1 << 20


def last_context_tokens(path: Path) -> int | None:
    """The context of the session's LAST assistant turn: input + cache-creation + cache-read tokens of its usage block (what the next turn re-reads; not output, not cost, not a quota). Only the tail of the
    transcript is read and only the usage integers are taken; None when the tail holds no usage block (a fresh or unreadable session)."""
    try:
        with path.open("rb") as fh:
            fh.seek(0, 2)
            size = fh.tell()
            fh.seek(max(0, size - CONTEXT_TAIL_BYTES))
            tail = fh.read().decode("utf-8", errors="replace").splitlines()
    except OSError:
        return None
    for line in reversed(tail[1:] if size > CONTEXT_TAIL_BYTES else tail):
        if '"usage"' not in line:
            continue
        try:
            usage = (json.loads(line).get("message") or {}).get("usage") or {}
        except (ValueError, AttributeError):
            continue
        if usage:
            return int(usage.get("input_tokens", 0)) + int(usage.get("cache_creation_input_tokens", 0)) + int(usage.get("cache_read_input_tokens", 0))
    return None


def context_flags(view: dict[str, Any]) -> list[str]:
    """One line per recipient at or above a restart line, from the view's `context_tokens`: a fact and the README rule it falls under, never a command to restart (a closed increment is the actor's to judge)."""
    out = []
    for role, row in (view.get("roles") or {}).items():
        tokens = row.get("context_tokens")
        line = next((label for limit, label in CONTEXT_LINES if isinstance(tokens, int) and tokens >= limit), None)
        if line:
            out.append(f"{role} ({row.get('name')}) context {round(tokens / 1000)}k: {line}")
    return out


def recipients_view(agents: list[dict[str, Any]], recipients: dict[str, str] | None, now: dt.datetime) -> dict[str, Any]:
    """The pilot's recipients (budget `recipients`: role -> session name) read as LIVE sessions, not as names. 2026-11-19 (ADV): the share above counts every session of the repository, so dormant
    operator chats made 'over half idle' true while every actual recipient was busy, and two sessions named SCI during a restart overlap collapsed into one row. Here each role resolves through
    `mandate_watch.route`: the marker-host is the recipient and the other same-name sessions are listed as surplus, never chosen. `idle_min` is the minutes a recipient has been idle (its transcript's
    last write), None when it is busy; `recipients_all_idle_min` is the shortest of them, None unless every reachable recipient is idle. Facts, not a verdict."""
    import mandate_watch as mw
    live = [a for a in agents if isinstance(a, dict) and mw.session_is_live(a)]
    out: dict[str, Any] = {}
    for role, name in sorted((recipients or {}).items()):
        res = mw.route(name, live, ROOT)
        row: dict[str, Any] = {"name": name, "state": res["status"]}
        if res["status"] == "RESOLVED":
            sid = res["session_id"]
            agent = next((a for a in live if a.get("sessionId") == sid), {})
            found = sorted(PROJECTS_DIR.glob(f"*/{sid}.jsonl"))
            quiet = round((now.timestamp() - found[-1].stat().st_mtime) / 60) if found else None
            status = str(agent.get("status"))
            row.update(session=str(sid)[:8], status=status, quiet_min=quiet, idle_min=quiet if status == "idle" else None)
            tokens = last_context_tokens(found[-1]) if found else None
            if tokens is not None:
                row["context_tokens"] = tokens
            if res.get("surplus_name_matches"):
                row["surplus"] = [str(x["session_id"])[:8] for x in res["surplus_name_matches"]]
        elif res["status"] == "AMBIGUOUS":
            row["candidates"] = [str(c["session_id"])[:8] for c in res.get("candidates", [])]
        out[role] = row
    reach = [r for r in out.values() if r["state"] == "RESOLVED"]
    idle = [r["idle_min"] for r in reach if r["idle_min"] is not None]
    return {"roles": out, "recipients_all_idle_min": min(idle) if reach and len(idle) == len(reach) else None}


def idle_without_blocker(view: dict[str, Any], waits: list[dict[str, str]]) -> list[str]:
    """Roles idle for more than IDLE_NAMED_MIN with no BLOCKED step in an open mandate that names them (the role, or its session name as a whole word). 'No blocker names it' is what is
    known, not 'no reason': a reason may sit in a message."""
    lines = []
    for role, row in (view.get("roles") or {}).items():
        idle = row.get("idle_min")
        if idle is None or idle <= IDLE_NAMED_MIN:
            continue
        rx = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(x) for x in {role, str(row.get("name", ""))} if x) + r")(?!\w)", re.I)
        if not any(rx.search(f"{w.get('task', '')} {w.get('step', '')} {w.get('blocker', '')}") for w in waits):
            lines.append(f"{role} ({row.get('name')}) idle {idle} min")
    return lines


def session_activity(now: dt.datetime, agents: list[dict[str, Any]] | None = None, recipients: dict[str, str] | None = None) -> dict[str, Any]:
    """HE60: who is working and who has been quiet, since when, so the operator's durable check (an idle share above half without a written reason is a prompt to send) is read, not rebuilt. Git cannot say it: every
    actor commits under one author. The runtime says each session's status and its transcript's last write; only that modification time is read, never the content. `quiet_min` is minutes since the transcript was
    last written (None when it is not found), `idle_share` counts this repository's sessions written within the last day (older ones are listed, not counted). Facts, not a verdict: a written reason is still read by the presidio."""
    agents = _agents() if agents is None else agents
    last = _git("log", "-1", "--format=%ct", observed_ref(fetch=False, now=now)["ref"])      # the observed ref, not a stale local main
    main_quiet = round((now.timestamp() - int(last)) / 60) if last.isdigit() else None
    published = unpublished_main(now)
    if not agents:
        return {"available": False, "main_quiet_min": main_quiet, "main_unpublished": published}
    rows = {}
    for a in agents:
        if not str(a.get("cwd") or "").startswith(str(ROOT)):
            continue
        found = sorted(PROJECTS_DIR.glob(f"*/{a.get('sessionId')}.jsonl")) if a.get("sessionId") else []
        rows[str(a.get("name"))] = {"status": str(a.get("status")), "quiet_min": round((now.timestamp() - found[-1].stat().st_mtime) / 60) if found else None}
    live = [r for r in rows.values() if r["quiet_min"] is not None and r["quiet_min"] < STALE_SESSION_MIN]
    idle = sum(1 for r in live if r["status"] == "idle")
    return {"available": True, "main_quiet_min": main_quiet, "main_unpublished": published, "sessions": rows, "idle_share": f"{idle}/{len(live)}", "idle_over_half": bool(live) and idle * 2 > len(live),
            "recipients": recipients_view(agents, recipients, now)}


def _waits() -> list[dict[str, str]]:
    """What the open mandates are waiting for, from their own records: every BLOCKED step with its named blocker (a battery, a CI run, a delivery, an answer). One cheap read of the task records: no transcript,
    no process listing. A step whose `unblock_when` is already met is not a wait (the continuity check counts it executable)."""
    out = []
    for path in sorted((ROOT / "ledger" / "tasks").glob("*/*.json")):
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(rec, dict) or not rec.get("TASK_ID") or mc.verdict(rec)["verdict"] not in OPEN_VERDICTS or any(m in rec["TASK_ID"] for m in SENDER_RECORDS):
                continue                                          # the presidio's own wait for events is the wait itself, not something to anticipate during
            for _, queue in mc.load_active_queues(rec):
                for st in mc.iter_steps(queue):
                    if st["status"] == "BLOCKED":
                        out.append({"task": rec["TASK_ID"], "step": st["step"][:80], "blocker": str(st.get("blocker") or "")[:160], "checkable": bool(st.get("unblock_when"))})
        except Exception:  # noqa: BLE001 — a record the continuity module cannot read is not a wait
            continue
    return out


WAIT_TIME_RX = re.compile(r"\b(20\d\d-\d\d-\d\dT\d\d:\d\d)(?::\d\d)?Z?\b")
WAIT_DUE_GRACE_MIN = 10


def due_waits(waits: list[dict[str, str]], now: dt.datetime) -> list[str]:
    """2026-11-20 (HE, operator's morning continuation): the 05:20Z radar step of the HE mandate was BLOCKED with a blocker that NAMED the awaited time, so the idle rule rightly said 'a blocker names it', and nothing
    looked again when the time had passed: the briefing waited 114 minutes for a recall. A blocker or step that names a UTC time (YYYY-MM-DDTHH:MM) already past by more than a few minutes is reported as due: a fact about the
    record, one line each, so the recipient (or the recall that reads the tick) goes and looks. Only the explicit T-form counts; a date alone or a word like 'tomorrow' is never parsed."""
    out = []
    for w in waits:
        for stamp in WAIT_TIME_RX.findall(f"{w.get('step', '')} {w.get('blocker', '')}"):
            try:
                at = dt.datetime.strptime(stamp, "%Y-%m-%dT%H:%M").replace(tzinfo=dt.timezone.utc)
            except ValueError:
                continue
            late = round((now - at).total_seconds() / 60)
            if late > WAIT_DUE_GRACE_MIN:
                out.append(f"{w.get('task')}: '{str(w.get('step', ''))[:60]}' awaits {stamp}Z, past by {late} min")
                break
    return out


def radar_news(state: dict[str, Any], briefing: Path | None = None) -> str:
    """A daily-scout briefing newer than the last one this tick reported, once per briefing. 2026-11-20: the briefing is written to a host file by cron and reaches an actor only through a full evaluation, so a briefing of
    05:20Z was worked at 06:18Z after a meeting asked. The tick line names the file's time, how many deltas it holds and which, and the rule that routes it (README section 13 and cross_session_transport.md section 12: judge each
    signal, forward the useful ones by name). Sets `radar_seen_utc` in the state it is given; returns '' when there is nothing new."""
    path = briefing or (STATE_HOME / "scout_daily_briefing.md")
    try:
        mtime = path.stat().st_mtime
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    stamp = dt.datetime.fromtimestamp(mtime, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if stamp <= str(state.get("radar_seen_utc") or ""):
        return ""
    state["radar_seen_utc"] = stamp
    deltas = re.findall(r"^Delta \d+: (.+)$", text, re.M)
    if not deltas:
        return ""
    return (f"NEW RADAR BRIEFING {stamp} ({len(deltas)} item(s) to examine: " + "; ".join(d[:70] for d in deltas[:4]) + f"): file {path}; judge each (deepen, assign, reuse, defer or discard, one reason) and forward the useful ones "
            "by name; the harness and tool items are HE's to triage, the scientific ones go to SCI or IT")


def notice_news(state: dict[str, Any], summary: Path | None = None) -> str:
    """ADV-258: the weekly notice sweep (scout_daily) lists retractions and expressions of concern that appeared since its previous run. The tick names each one once; corrections are in the table, not flagged."""
    path = summary or Path(os.environ.get("LEGEND_NOTICE_STATE") or STATE_HOME / "notice_sweep") / "summary.json"
    try:
        rows = json.loads(path.read_text(encoding="utf-8")).get("new_flagged") or []
    except (OSError, ValueError, AttributeError):
        return ""
    told = set(state.get("notices_told") or [])
    fresh = [r for r in rows if "|".join(r[:3]) not in told]
    if not fresh:
        return ""
    state["notices_told"] = sorted(told | {"|".join(r[:3]) for r in fresh})
    return ("NEW NOTICE on a catalogued paper: " + "; ".join(f"PMID {r[0]} {r[1]} (notice {r[2]}, {r[3]})" for r in fresh[:5])
            + (f"; {len(fresh) - 5} more" if len(fresh) > 5 else "") + f": table {path.parent / 'notices.tsv'}; check what leans on each before building on it")


def unchecked_waits(waits: list[dict[str, str]], state: dict[str, Any]) -> str:
    """2026-11-20 (ADV 'Reliable autonomy', item 3): IT listed SCI's GSK-3 reading as awaited for two hours after it had landed, because the awaited event was prose in a blocker and nothing evaluated it. SIZED: matching the
    prose against commit subjects was measured on the eight live waits and is too fuzzy (3 to 84 hits per wait, the matches carried generic words such as batch, table, decision, page, item), so it is NOT built. The existing precise
    mechanism is `unblock_when` on a BLOCKED step (a file, a commit subject, a commit sha or a record state: `mandate_continuity.unblock_met`); only 2 of 11 BLOCKED steps carried it. This line names, per task, the BLOCKED steps
    that carry none, only when the set changes, so the recipient types the condition when it writes the wait. Returns '' when nothing changed."""
    counts: dict[str, int] = {}
    for w in waits:
        if not w.get("checkable"):
            counts[w["task"]] = counts.get(w["task"], 0) + 1
    signature = sha256_text(json.dumps(sorted(counts.items())))[:12]
    if signature == state.get("unchecked_waits_sig"):
        return ""
    state["unchecked_waits_sig"] = signature
    if not counts:
        return ""
    return ("WAITS NO CHECK CAN EVALUATE (BLOCKED steps without `unblock_when`; an event that already happened stays a dependency until someone reads it): "
            + ", ".join(f"{t} x{n}" for t, n in sorted(counts.items(), key=lambda kv: -kv[1])[:6]) + "; type the awaited fact when writing the wait (README section 13, 'a BLOCKED step')")


def _own_updates(campaign: Path) -> list[str]:
    """Pathspecs that leave out what the Advisor itself writes (its saved assessments, its assignment and invocation logs, its portfolio updates and DREAM notes, the sender records): a commit that touches only those is not news to the Advisor
    (HE57: 2 of the last 23 commits of the campaign folder matched the delivery pattern). A recipient's result file in the folder is still news. Outside the repository there is nothing to exclude."""
    try:
        rel = Path(campaign).resolve().relative_to(ROOT.resolve())
    except ValueError:
        return []
    return [f":(exclude,glob){rel}/P[0-9]*/**", f":(exclude){rel}/assignments", f":(exclude){rel}/assignments.jsonl", f":(exclude){rel}/invocations.jsonl", f":(exclude){rel}/holds.jsonl",   # a hold is the advisor's own reason logged, not a delivery (2026-11-22: commit d066c7902 changed only assignments.jsonl and holds.jsonl and woke the 02:34Z tick); its expiry or typed resume trigger is read elsewhere (resume_when), untouched
            f":(exclude,glob){rel}/meetings/**",
            f":(exclude){PORTFOLIO_REL}",                          # an evaluation records its portfolio updates in the same commit; a changed portfolio is its own event (the digest), not a delivery
            ":(exclude,glob)**/IDEAS_ORDER_DREAM*_ADV.md",         # the Advisor's DREAM pass notes
            *[f":(exclude,glob)ledger/tasks/*/*{m}*" for m in SENDER_RECORDS]]


def _is_sender(task: str) -> bool:
    return any(m in task for m in SENDER_RECORDS)


PATH_TOKEN = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b|[\w.\-]+/[\w./\-]+")      # a record id, a portfolio row id or a file path: what a wait must name


def names_a_path(text: str) -> bool:
    return bool(PATH_TOKEN.search(text or ""))


def unaccounted_ready(portfolio: dict[str, Any], *texts: str) -> list[str]:
    """2026-11-16: the portfolio rows that are ready (or due for review) and that a wait or hold does not name. A blocked path (an intake, a laboratory, a source) is not a blocked portfolio: a general wait is valid
    only for the rows it names with their cause."""
    blob = " ".join(t or "" for t in texts)
    return [i for i in (portfolio.get("actionable") or []) if i not in blob]


def queue_state(recs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """HE57: is there executable work left in the portfolio's records? The sender's own records (the presidio's standing objective) are not work to execute; a mandate with only blocked steps is not executable."""
    mine = {t: r for t, r in recs.items() if not _is_sender(t)}
    return {"executable": sorted(t for t, r in mine.items() if r.get("verdict") == "CONTINUE"),
            "blocked_only": sorted(t for t, r in mine.items() if r.get("verdict") == "ALL_BLOCKED"),
            "exhausted": not any(r.get("verdict") == "CONTINUE" for r in mine.values())}


def parse_outcome(text: str) -> dict[str, Any]:
    """The `## Outcome` block that closes an evaluation: `outcome` (continue | switch | assign | queue | wait) and, for a wait, `excluded` (the relevant alternatives left out, with why), `reason` and `resume_when`.
    `stated` is true only when the block is complete for what it says; anything else is reported as unstated and never guessed."""
    m = re.search(r"^## Outcome\b[^\n]*\n(.*?)(?=^## |\Z)", text or "", re.M | re.S)
    fields: dict[str, str] = {}
    cur = None
    for line in (m.group(1) if m else "").splitlines():
        f = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if f and f.group(1) in OUTCOME_FIELDS:
            cur = f.group(1); fields[cur] = f.group(2).strip()
        elif cur and line.strip():
            fields[cur] += " " + line.strip()
    kind = (fields.get("outcome", "").split() or [""])[0].strip("`*.,;:").lower()
    out: dict[str, Any] = {"outcome": kind if kind in OUTCOMES else "", "excluded": fields.get("excluded", ""), "reason": fields.get("reason", ""), "resume_when": fields.get("resume_when", "").strip("` ") or "event"}
    out["stated"] = bool(out["outcome"]) and (out["outcome"] != "wait" or bool(out["excluded"] and out["reason"]))
    out["problem"] = "" if out["stated"] else ("no `## Outcome` block" if not m else "the outcome is not one of " + "/".join(OUTCOMES) if not out["outcome"] else "a wait must say what it excluded and why")
    return out


def resume_met(spec: str, now: dt.datetime) -> str:
    """Has what a wait was resting on arrived? `event` is never met here (events are read by the tick itself). `record:<TASK>=<STATE>` and `path:<file>[~<text>]` use the continuity module's own reader of the same facts;
    `after:<UTC>` is a time. Returns why it is met, or ''. A form this does not read is not met and is reported by `resume_problem`."""
    spec = (spec or "").strip()
    if spec.startswith("record:") and "=" in spec:
        task, state = spec[7:].split("=", 1)
        return mc.unblock_met({"record": task.strip(), "state": state.strip()})
    if spec.startswith("path:"):
        path, _, text = spec[5:].partition("~")
        return mc.unblock_met({"path": path.strip(), **({"contains": text.strip()} if text.strip() else {})})
    if spec.startswith("after:"):
        try:
            when = dt.datetime.fromisoformat(spec[6:].strip().replace("Z", "+00:00"))
        except ValueError:
            return ""
        return f"the time {spec[6:].strip()} has passed" if now >= when else ""
    return ""


def resume_problem(spec: str) -> str:
    spec = (spec or "").strip()
    if spec == "event" or (spec.startswith("record:") and "=" in spec) or spec.startswith(("path:", "after:")):
        return ""
    return f"resume_when {spec!r} is not one of event | record:<TASK_ID>=<STATE> | path:<file>[~<text>] | after:<UTC>; read as event"


PUBLISHED_REMOTE = "development"
FETCH_TIMEOUT_S = 25


def _ref_time(ref: str) -> int:
    out = _git("log", "-1", "--format=%ct", ref)
    return int(out) if out.isdigit() else 0


RECALL_RENEW_DAYS = 5      # a session cron expires after 7 days (CronCreate says so); the warning leaves two days to renew


def recall_status(state: dict[str, Any], now: dt.datetime) -> dict[str, Any]:
    """The age of the one in-session recall, from the host's own `recall-armed` note. A session cron is session-only and auto-expires after 7 days; a revival restores it under the same job id (measured 2026-11-18,
    Claude Code 2.1.327) but nothing re-arms it before it expires except the host. The tick cannot see CronList, so it counts from what the host recorded and says when that note is missing."""
    rec = state.get("recall") or {}
    armed = rec.get("armed_utc")
    if not armed:
        return {"armed_utc": None, "age_days": None, "renew_due": False, "note": "no arming recorded: after CronCreate run `strategic_advisor.py recall-armed` so the 7-day expiry is watched"}
    try:
        age = (now - dt.datetime.fromisoformat(armed.replace("Z", "+00:00"))).total_seconds() / 86400
    except ValueError:
        return {"armed_utc": armed, "age_days": None, "renew_due": False, "note": "the recorded arming time is not readable"}
    due = age >= RECALL_RENEW_DAYS
    return {"armed_utc": armed, "job_id": rec.get("job_id", ""), "age_days": round(age, 1), "renew_due": due,
            "note": (f"armed {age:.1f} days ago (job {rec.get('job_id') or '?'}); renew before day 7: CronList, CronDelete the job carrying the mark, CronCreate the text of `recall`, then `recall-armed`"
                     if due else f"armed {age:.1f} days ago")}


def observed_ref(fetch: bool = True, now: dt.datetime | None = None) -> dict[str, Any]:
    """2026-11-18: the ref the presidio reads as "main", and how far it can be trusted. The tick used to read ONLY the local `main`; on 2026-11-18 the primary checkout's `main` was 13 hours behind `development/main`
    (the checkout held the newer work detached, the published branch held it too, local `main` held neither), and a presidio that reads a stale ref says "nothing new" while work lands. Now: one bounded fetch of
    the published remote's `main` (it moves only the remote-tracking ref: no checkout, branch or index is touched, nothing is reset), then the NEWEST of development/main, origin/main and local main by commit time is
    the observed ref, and the answer says which ref it is, whether the fetch succeeded, how old the last fetch is when it did not, and how far local `main` and the checkout lag behind it. States: VERIFIED (published ref
    fetched now), UNVERIFIED (the fetch failed: the published ref is as old as the last fetch), LOCAL_ONLY (the newest commit is on local `main` and not published), NO_REMOTE (a repository without the published remote:
    nothing to verify). A state other than VERIFIED and NO_REMOTE is said in the tick's `why`; the tick never reads it as proof that nothing landed."""
    now = now or _now()
    has_remote = bool(_git("remote", "get-url", PUBLISHED_REMOTE))
    fetch_info: dict[str, Any] = {"attempted": False, "ok": None, "error": ""}
    if fetch and has_remote and os.environ.get("LEGEND_ADVISOR_NOFETCH") != "1":
        fetch_info["attempted"] = True
        try:
            done = subprocess.run(["git", "fetch", "-q", PUBLISHED_REMOTE, "main"], cwd=ROOT, capture_output=True, text=True, timeout=FETCH_TIMEOUT_S)
            fetch_info["ok"] = done.returncode == 0
            fetch_info["error"] = "" if done.returncode == 0 else (done.stderr.strip().splitlines() or ["fetch failed"])[-1][:160]
        except (OSError, subprocess.SubprocessError) as exc:
            fetch_info["ok"], fetch_info["error"] = False, type(exc).__name__
    fetch_head = Path(_git("rev-parse", "--path-format=absolute", "--git-common-dir") or ".") / "FETCH_HEAD"
    fetch_age = round((now.timestamp() - fetch_head.stat().st_mtime) / 60) if fetch_head.exists() else None
    cands = {r: _git("rev-parse", "--verify", "--quiet", r) for r in (f"{PUBLISHED_REMOTE}/main", "origin/main", "main")}
    cands = {r: sha for r, sha in cands.items() if sha}
    if not cands:
        return {"ref": "main", "sha": "", "state": "NO_REMOTE", "fetch": fetch_info, "fetch_age_min": fetch_age, "local_main": {}, "checkout": {}, "note": "no main ref is known"}
    def _is_ancestor(old: str, new: str) -> bool:
        return old == new or subprocess.run(["git", "merge-base", "--is-ancestor", old, new], cwd=ROOT, capture_output=True).returncode == 0
    order = [r for r in (f"{PUBLISHED_REMOTE}/main", "origin/main", "main") if r in cands]
    tips = [r for r in order if all(_is_ancestor(cands[o], cands[r]) for o in order)]       # a ref that contains all the others: the real tip (ties go to the published remote first)
    ref = tips[0] if tips else max(order, key=lambda r: (_ref_time(r), r == f"{PUBLISHED_REMOTE}/main"))      # diverged refs: the newest commit
    sha = cands[ref]
    published = cands.get(f"{PUBLISHED_REMOTE}/main", "")
    local_only = ref == "main" and bool(published) and sha != published and subprocess.run(["git", "merge-base", "--is-ancestor", sha, published], cwd=ROOT, capture_output=True).returncode != 0
    if not has_remote:
        state = "NO_REMOTE"
    elif local_only:
        state = "LOCAL_ONLY"
    elif fetch_info["attempted"] and fetch_info["ok"]:
        state = "VERIFIED"
    else:
        state = "UNVERIFIED"
    behind = _git("rev-list", "--count", f"main..{ref}") if "main" in cands and ref != "main" else "0"
    head = _git("rev-parse", "HEAD")
    head_behind = _git("rev-list", "--count", f"HEAD..{ref}")
    note = {"VERIFIED": f"{ref} fetched now", "NO_REMOTE": "no published remote in this repository",
            "LOCAL_ONLY": f"the newest commit is on local main and is not published ({published[:8] or 'no published ref'} is the published tip)",
            "UNVERIFIED": (f"the fetch of {PUBLISHED_REMOTE}/main failed ({fetch_info['error'] or 'not attempted'}); {ref} is as old as the last fetch ({fetch_age} min ago)" if fetch_age is not None
                           else f"the fetch of {PUBLISHED_REMOTE}/main failed ({fetch_info['error'] or 'not attempted'}) and no earlier fetch is recorded")}[state]
    return {"ref": ref, "sha": sha, "state": state, "fetch": fetch_info, "fetch_age_min": fetch_age, "note": note,
            "local_main": {"sha": cands.get("main", "")[:12], "behind_observed": int(behind) if behind.isdigit() else None},
            "checkout": {"head": head[:12], "branch": _git("rev-parse", "--abbrev-ref", "HEAD"), "behind_observed": int(head_behind) if head_behind.isdigit() else None}}


def observe(campaign: Path, state: dict[str, Any]) -> dict[str, Any]:
    """The bounded facts a decision needs, read mechanically: roadmap digest, commits since the last tick, mandate transitions, stalled mandates reported by the watch, sessions."""
    ref = observed_ref()
    main_sha = ref["sha"] or _git("rev-parse", "main")
    last = state.get("main_sha") or main_sha
    commits = [c for c in _git("log", "--format=%h %s", f"{last}..{main_sha}", "--", "ledger/tasks", "disease-models/wwox/research/drug_repurposing", *_own_updates(campaign)).splitlines()[:60] if c.strip()]
    recs = _records()
    before = state.get("mandates") or {}
    transitions = [f"{t}: {before[t]} -> {r['state']}" for t, r in recs.items() if t in before and before[t] != r["state"] and not _is_sender(t)]       # HE57: the sender's own records changing are not an event
    opened = [t for t in recs if before and t not in before and recs[t]["state"] == "OPEN" and not _is_sender(t)]
    stalled = []
    try:
        watch = subprocess.run([sys.executable, str(ROOT / "framework/scripts/mandate_watch.py"), "events", "--last", "30"], capture_output=True, text=True, timeout=30).stdout
        stalled = sorted({m.group(1) for m in re.finditer(r"RESUME ((?:[A-Z0-9]+-)+[A-Z0-9]+)", watch) if recs.get(m.group(1), {}).get("state") == "OPEN"})
    except (OSError, subprocess.SubprocessError):
        pass
    waits = _waits()
    seen_waits = set(state.get("waits_seen") or [])
    new_waits = [w for w in waits if sha256_text(w["task"] + "|" + w["blocker"])[:12] not in seen_waits] if state.get("waits_seen") is not None else []   # the first tick records the waits as they are; only a NEW wait is an event
    switched = ([f"reference: the observed ref moved to {ref['ref']}@{main_sha[:8]} (local main {ref['local_main'].get('behind_observed')} commits behind it)"]
                if state.get("main_sha") and state.get("main_ref") and state.get("main_ref") != ref["ref"] else [])
    events = (switched + [f"delivery: {c}" for c in commits if EVENT_SUBJECT.search(c)] + [f"mandate: {t}" for t in transitions] + [f"opened: {t}" for t in opened]
              + [f"stalled-for-the-watch: {t}" for t in stalled] + [f"waiting: {w['task']}: {w['blocker'][:100]}" for w in new_waits])
    portfolio = portfolio_snapshot(recs)
    if (portfolio["available"] or state.get("portfolio_digest")) and portfolio["digest"] != state.get("portfolio_digest"):
        events.append(f"portfolio: {portfolio['digest'][:16]} opportunities, priorities or executable dependencies changed")
    rm = roadmap_text()
    return {"main_sha": main_sha, "main_ref": ref, "roadmap_sha256": sha256_text(rm) if rm else "", "commits_since_last_tick": len(commits), "events": events,
            "open_mandates": sorted(t for t, r in recs.items() if r["state"] == "OPEN"), "mandates": {t: r["state"] for t, r in recs.items()}, "waits": waits,
            "queue": queue_state(recs), "sessions": _sessions(), "portfolio": portfolio}


def presidio_state(verdict: str, why: str, is_continuous: bool, outcome: dict[str, Any] | None = None, exhausted: bool = False, streak: int = 0, unaccounted: list[str] | None = None) -> str:
    """What the presidio is doing, in words that cannot be mistaken for having been abandoned: a wait is a state of the mandate, not its end and not a request for a new prompt."""
    if verdict in ("EVALUATE", "RUNNING"):
        return "ACTIVE: an evaluation is due or running"
    if verdict in ("NONE", "DEFERRED"):
        if not is_continuous:
            return "idle inside the pilot: nothing new"
        outcome = outcome or {}
        if outcome.get("evaluation") == "HOLD":
            return (f"HELD by host at {outcome.get('utc', '?')}: {outcome.get('reason', '')[:140]}; excluded paths: {outcome.get('excluded', '')[:200] or 'none stated'}; resume_when {outcome.get('resume_when', '?')}; "
                    "ends at that condition, a roadmap change, the first new event or its lapse (not an evaluation, no model run)" + (f"; NOT A VALID GENERAL WAIT, ready portfolio rows not named: {', '.join(unaccounted[:6])}" if unaccounted else ""))
        if outcome.get("stated") and outcome.get("outcome") == "wait":
            return (f"WAITING (motivated): {outcome.get('reason', '')[:140]}; excluded: {outcome.get('excluded', '')[:160]}; resumes when: {outcome.get('resume_when', 'event')}"
                    + (f"; NOT A VALID GENERAL WAIT, ready portfolio rows not named: {', '.join(unaccounted[:6])}" if unaccounted else ""))
        if outcome.get("stated"):
            return f"ACTING ON the last choice ({outcome['outcome']}): {outcome.get('reason', '')[:140] or 'no event needs a new choice'}; the next triggers are a delivery, a mandate transition, a stalled mandate or a roadmap change"
        if exhausted:
            return ("IDLE without a stated outcome: no written executable step (a statement about task records, not about the portfolio): the closing comparison of section 12 is the next step, and the last evaluation did not say what it chose or why it waits"
                    + ("; it was already asked once, so it is not asked again until something changes" if streak else ""))
        return "WAITING (legitimate): no event needs a strategic choice; the next triggers are a roadmap change, a delivery, a mandate transition or a stalled mandate"
    if verdict == "PAUSED":
        return f"SUSPENDED by the operator: {why}"
    if verdict == "RESOURCES":
        return f"SUSPENDED for resources: {why}"
    if verdict == "DISABLED":
        return "STOPPED: the campaign was disabled"
    return "PILOT ENDED: " + why + " (no continuous authorisation is in force)"


def evaluation_clock(campaign: Path, state: dict[str, Any]) -> tuple[dt.datetime | None, str]:
    """Start-to-start cadence; legacy completion times remain historical facts, not dispatch times."""
    end_text = state.get("last_evaluation_utc")
    choice = state.get("last_outcome") or {}
    if choice.get("evaluation") == "HOST":
        try:
            stamp = dt.datetime.fromisoformat(choice["utc"].replace("Z", "+00:00"))
            if stamp.tzinfo is not None and (not end_text or stamp >= dt.datetime.fromisoformat(end_text.replace("Z", "+00:00"))):
                return stamp, "recorded host decision (not a model evaluation)"
        except (KeyError, TypeError, ValueError):
            pass
    if not end_text:
        return None, "no previous evaluation"
    end = dt.datetime.fromisoformat(end_text.replace("Z", "+00:00"))
    try:
        start = dt.datetime.fromisoformat(state["last_evaluation_started_utc"].replace("Z", "+00:00"))
        if start.tzinfo is not None and start <= end:
            return start, "recorded evaluation start"
    except (KeyError, TypeError, ValueError, AttributeError):
        pass
    label = (state.get("last_outcome") or {}).get("evaluation", "")
    if re.fullmatch(r"P\d+", label):
        try:
            meta = json.loads((campaign / label / "meta.json").read_text(encoding="utf-8"))
            finish = dt.datetime.fromisoformat(meta["ended_utc"].replace("Z", "+00:00"))
            start = dt.datetime.fromisoformat(meta["started_utc"].replace("Z", "+00:00"))
            if finish == end and start.tzinfo is not None and start <= finish:
                state["last_evaluation_started_utc"] = _utc(start)
                return start, "matching legacy runtime metadata"
        except (OSError, KeyError, TypeError, ValueError, AttributeError):
            pass
    return end, "legacy completion (start unavailable)"


def waiting_work(campaign: Path, now: dt.datetime | None = None) -> dict[str, Any]:
    """2026-11-21 (ADV): read-only facts for the tick, no verdict and no rule. `minutes_since_host_edit` is the age of the newest of the host's last DREAM line (assignments.jsonl) and the newest `updated_utc`
    of a portfolio row; `waiting_without_resume` lists the rows whose status is waiting and whose resume_when is empty or the bare word `event`, i.e. waits that name nothing to wait for."""
    now = now or _now()
    stamps: list[tuple[dt.datetime, str]] = []
    try:
        stamps += [(t, "DREAM") for e in _events(campaign) if e.get("state") == "DREAM" for t in [_stamp(e.get("utc"))] if t]
    except (OSError, ValueError):
        pass
    rows, _errors = portfolio_rows()
    stamps += [(t, "portfolio edit " + r["id"]) for r in rows for t in [_stamp(r.get("updated_utc"))] if t]
    bare = [r["id"] for r in rows if r.get("status", "").lower() == "waiting" and r.get("resume_when", "").strip().strip("`").lower() in ("", "event")]
    last, kind = max(stamps) if stamps else (None, "")
    minutes = None if last is None else max(0, int((now - last).total_seconds() // 60))
    line = ("waiting_work: " + ("no DREAM or portfolio edit on record" if minutes is None else f"{minutes} min since the last {kind} ({_utc(last)})")
            + "; waiting rows with no stated resume_when (empty or bare 'event'): " + (", ".join(bare) or "none"))
    return {"minutes_since_host_edit": minutes, "last_host_edit": {"utc": _utc(last) if last else None, "kind": kind}, "waiting_without_resume": bare, "line": line}


def tick(campaign: Path) -> dict[str, Any]:
    """The hourly check: mostly mechanical, no model. Verdicts: NONE (nothing new: reuse the previous assessment), EVALUATE (one strategic evaluation is due), and the reasons it is not
    (RUNNING, DISABLED, EXPIRED, BUDGET, DEFERRED). A stalled mandate is reported, not restarted: recovery stays with the mandate watch."""
    campaign = Path(campaign)
    state = _load_state(campaign)
    now = _now()
    # A deployed fix must also repair a decision saved before that fix. Keep the
    # original assessment and the superseded outcome; never let P11's old wait
    # survive merely because the incomplete-run check was added afterwards.
    invalidated = ""
    saved_outcome = state.get("last_outcome") or {}
    label = saved_outcome.get("evaluation", "")
    if re.fullmatch(r"P\d+", label):
        invalidated = incomplete_run(campaign, label)
        if invalidated:
            state.update(last_invalidated_outcome={"outcome": saved_outcome, "reason": invalidated, "utc": _utc(now)},
                         last_outcome={}, unstated_streak=0,
                         last_incomplete={"evaluation": label, "reason": invalidated, "utc": _utc(now)})
    obs = observe(campaign, state)
    obs["events"] = list(dict.fromkeys(list(state.get("pending_events") or []) + obs["events"]))
    obs["commits_since_last_tick"] += int(state.get("pending_commits") or 0)
    first = not state
    refusal = budget_refusal(campaign)
    cont = continuous(campaign)
    anticipating = [e for e in obs["events"] if e.startswith(("delivery:", "mandate:", "stalled", "portfolio:"))] or ([f"roadmap changed"] if state.get("roadmap_sha256") not in (None, obs["roadmap_sha256"]) else [])
    changed = state.get("roadmap_sha256") not in (None, obs["roadmap_sha256"])
    digest = sha256_text(obs["roadmap_sha256"] + "|" + "|".join(sorted(obs["events"])))
    last_eval, clock_source = evaluation_clock(campaign, state)
    hours = (now - last_eval).total_seconds() / 3600 if last_eval else None
    verdict, why = "NONE", "nothing new: the previous assessment stands"
    if (campaign / "DISABLED").exists():
        verdict, why = "DISABLED", "the campaign is disabled"
    elif refusal:
        verdict, why = ("PAUSED" if refusal.startswith("operator suspension") else "RESOURCES" if "weekly allocation" in refusal else "EXPIRED" if "expired" in refusal else "BUDGET"), refusal
    elif first and (campaign / "budget.json").exists():
        verdict, why = "EVALUATE", "campaign start: the roadmap and the first observation"
    elif first:
        why = "first tick: baseline recorded, no evaluation from history"
    elif _running(state):
        verdict, why = "RUNNING", "an evaluation is already running (same process identity)"
    elif invalidated:
        verdict, why = "EVALUATE", "the saved outcome came from an incomplete evaluation and has been superseded: " + invalidated
    elif obs["events"] or changed:
        if digest == state.get("last_digest"):
            why = "the same events were already evaluated"
        elif changed or (cont and anticipating and obs["queue"]["exhausted"]) or (anticipating and (hours is None or hours >= float(cont.get("min_hours_anticipating", 1)))) or (hours is None or hours >= float(cont.get("min_hours_between", 4))):
            verdict, why = "EVALUATE", ("roadmap changed" if changed else "; ".join(anticipating[:3] or obs["events"][:3]))
            if cont and anticipating and obs["queue"]["exhausted"] and not changed:
                why += "; idle pipeline: assess pending signals without a cadence gate"
        else:
            interval = float(cont.get("min_hours_anticipating", 1) if anticipating else cont.get("min_hours_between", 4))
            eligible = _utc(last_eval + dt.timedelta(hours=interval))
            verdict, why = "DEFERRED", f"{'anticipating' if anticipating else 'ordinary'} events pending; next eligible at {eligible} ({clock_source})"
    outcome = state.get("last_outcome") or {}
    streak = int(state.get("unstated_streak") or 0)
    unacc_wait = unaccounted_ready(obs["portfolio"], outcome.get("reason", ""), outcome.get("excluded", "")) if outcome.get("stated") and outcome.get("outcome") == "wait" else []
    if verdict in ("NONE", "DEFERRED") and cont and not first and last_eval is not None:
        # HE57: a quiet tick is not always a reason to wait. A wait that stated what it rests on is resumed when that arrives; an evaluation that left no outcome while nothing executable remains gets ONE more
        # evaluation to decide what is next (it is not asked again until it says something); a stated wait or choice is otherwise left alone.
        met = resume_met(outcome.get("resume_when", ""), now) if outcome.get("stated") and outcome.get("outcome") == "wait" else ""
        held_since = None
        if outcome.get("evaluation") == "HOLD":
            try:
                held_since = (now - dt.datetime.fromisoformat(str(outcome.get("utc", "")).replace("Z", "+00:00"))).total_seconds() / 3600
            except ValueError:
                held_since = None
        if met:
            verdict, why = "EVALUATE", f"the resume condition of the last wait is met: {met}"
        elif held_since is not None and held_since >= float(cont.get("min_hours_between", 4)):
            verdict, why = "EVALUATE", f"hold lapsed after {held_since:.1f} h: re-compare (a hold is a wait for the paths it names, not a standing answer; excluded then: {str(outcome.get('excluded', ''))[:160] or 'none stated'})"
        elif unacc_wait and state.get("unaccounted_asked") != obs["portfolio"]["digest"]:
            verdict, why = "EVALUATE", f"the last wait does not name ready portfolio rows ({', '.join(unacc_wait[:6])}): a blocked path is not a blocked portfolio; asked once per portfolio state"
            state["unaccounted_asked"] = obs["portfolio"]["digest"]
        elif not outcome.get("stated") and streak < 1 and obs["queue"]["exhausted"] and hours is not None and hours >= float(cont.get("min_hours_between", 4)):
            verdict, why = "EVALUATE", "the last evaluation left no stated outcome and no executable work remains: decide what is next from the portfolio"
        elif outcome.get("stated") and outcome.get("outcome") in ("continue", "switch", "assign", "queue") and obs["queue"]["exhausted"] and hours is not None and hours >= float(cont.get("min_hours_between", 4)):
            verdict, why = "EVALUATE", "the previous choice leaves no executable work: choose what is next from the standing portfolio"
    recall = recall_status(state, now)
    if verdict in ("NONE", "DEFERRED") and cont and recall["renew_due"]:
        why += f"; RECALL RENEWAL DUE: {recall['note']}"
    ref = obs.get("main_ref") or {"ref": "main", "sha": "", "state": "NO_REMOTE", "note": "no reference was observed", "fetch": {}, "fetch_age_min": None, "local_main": {}, "checkout": {}}
    if verdict in ("NONE", "DEFERRED") and ref["state"] in ("UNVERIFIED", "LOCAL_ONLY"):
        # 2026-11-18: "nothing new" about a reference that could not be verified is not a statement that nothing landed.
        why += f"; NOT VERIFIED: {ref['note']}"
    if verdict == "NONE" and not first and obs["portfolio"].get("actionable"):
        # ADV-047: NONE answers "did an event, a roadmap change or a met resume condition arrive", not "is there work"; the tick line itself names the ready rows so a quiet hour is not read as an empty portfolio
        why += "; this says nothing about opportunities, ready portfolio rows: " + ", ".join(obs["portfolio"]["actionable"][:6])
    behind = behind_line(campaign, ref.get("sha", "")) if ref["state"] != "NO_REMOTE" else ""
    if behind:
        why += "; " + behind
    activity = session_activity(now, recipients=_budget(campaign).get("recipients"))
    named = idle_without_blocker((activity.get("recipients") or {}), obs["waits"]) if activity.get("available") else []
    if not activity.get("available"):
        why += "; ACTIVITY UNAVAILABLE: the runtime's session listing could not be read (claude not found or `claude agents --json` failed), so the idle rule cannot be applied from this tick"
    if named:
        why += "; IDLE WITHOUT A BLOCKER THAT NAMES IT: " + "; ".join(named)         # facts about the recipients, not a verdict on useful work
    due = due_waits(obs["waits"], now)
    if due:
        why += "; WAIT NAMES A TIME THAT HAS PASSED: " + "; ".join(due[:4])
    stuck = [f"{r['id']} [{r['recipient']}]: {r['flag']}" for r in assignment_flow(campaign, now) if r["flag"]] if campaign else []
    if stuck:
        why += "; ASSIGNMENT FLOW (sent is not taken is not started): " + "; ".join(stuck[:4])
    disc = discipline_lines(campaign) if campaign else []
    if disc:
        why += "; " + "; ".join(disc)
    ci_line = ci_main_line(state, now)
    if ci_line:
        why += "; " + ci_line
    unchecked = unchecked_waits(obs["waits"], state)
    if unchecked:
        why += "; " + unchecked
    news = radar_news(state)
    if news:
        why += "; " + news
    notices = notice_news(state)
    if notices:
        why += "; " + notices
    flagged = context_flags(activity.get("recipients") or {}) if activity.get("available") else []
    if flagged:
        why += "; CONTEXT AT A RESTART LINE (README section 13; last turn's input and cache tokens, not cost): " + "; ".join(flagged)
    state["last_tick_utc"] = _utc(now)
    if verdict != "RUNNING":
        state.update(main_sha=obs["main_sha"], main_ref=(obs.get("main_ref") or {}).get("ref", "main"), mandates=obs["mandates"], roadmap_sha256=obs["roadmap_sha256"],
                     waits_seen=sorted({sha256_text(w["task"] + "|" + w["blocker"])[:12] for w in obs["waits"]}))
    # A deferred tick observes without consuming. While a run is active, leave its
    # baseline alone so deliveries arriving after its snapshot reach the next run.
    if verdict in ("EVALUATE", "DEFERRED"):
        state["pending_digest"] = digest
        state["pending_events"] = obs["events"]            # keep deferred observations until an evaluation actually consumes them
        state["pending_commits"] = obs["commits_since_last_tick"]
    _save_state(campaign, state)
    ctl = operator_controls()
    try:
        alignment = meeting_status(campaign)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        alignment = {"state": "ERROR", "actionable": False, "why": str(exc)}
    return {"verdict": verdict, "why": why, "mode": "continuous" if cont else "pilot", "presidio": presidio_state(verdict, why, bool(cont), outcome, obs["queue"]["exhausted"], streak, unacc_wait),
            "meeting": alignment,
            "operator_guidance": mc.operator_guidance(ROOT),
            "last_outcome": {k: outcome.get(k) for k in ("outcome", "reason", "excluded", "resume_when", "stated", "evaluation") if outcome.get(k) not in (None, "")},
            "queue": {**obs["queue"], "scope": "written executable tasks only; not a statement about the portfolio", "blocked_paths": [{k: w.get(k, "") for k in ("task", "step", "blocker")} for w in obs["waits"]], "portfolio_ready": list(obs["portfolio"].get("actionable") or [])},
            "last_incomplete": state.get("last_incomplete") or {},
            "operator_controls": [f"{c['kind']}: {c['text']}" for c in (active_suspensions(ctl) + [c for c in ctl if c["kind"] in ("URGENT", "INTEGRATION")])[-6:]],
            "events": obs["events"][:12], "open_mandates": obs["open_mandates"], "waiting_on": [f"{w['task']}: {w['blocker'][:70]}" for w in obs["waits"]][:4] + ([f"... {len(obs['waits'])} in all"] if len(obs["waits"]) > 4 else []),
             "portfolio": {k: obs["portfolio"][k] for k in ("path", "available", "actionable", "errors")},
            "sessions": obs["sessions"], "activity": activity, "digest": digest,
            "recall": recall,
            "reference": {k: ref[k] for k in ("ref", "sha", "state", "note", "fetch", "fetch_age_min", "local_main", "checkout")},
            "evaluation_clock": {"utc": _utc(last_eval) if last_eval else None, "source": clock_source},
            "waiting_work": waiting_work(campaign, now),
            "hours_since_last_evaluation": None if hours is None else round(hours, 1)}


def parse_assignments(text: str) -> list[dict[str, str]]:
    """The `### ASSIGNMENT n` blocks of an assessment: `field: value` lines (a value may continue on the following lines). A block missing a required field is kept and flagged."""
    out = []
    for block in re.split(r"^### ASSIGNMENT\b.*$", text, flags=re.M)[1:]:
        block = block.split("\n## ", 1)[0]
        fields, cur = {}, None
        for line in block.splitlines():
            m = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if m and m.group(1) in ASSIGNMENT_FIELDS + OPTIONAL_FIELDS:
                cur = m.group(1); fields[cur] = m.group(2).strip()
            elif cur and line.strip():
                fields[cur] += " " + line.strip()
        fields["_missing"] = ",".join(f for f in ASSIGNMENT_FIELDS if not fields.get(f))
        fields["_text"] = block.strip()
        out.append(fields)
    return out


def _events(campaign: Path) -> list[dict[str, Any]]:
    path = Path(campaign) / "assignments.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path.exists() else []


RECEIPT_ID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I)


def delivery_refusal(campaign: Path, ident: str, state: str, to: list[str], evidence: str = "", receipt: list[str] | None = None) -> str:
    """SENT is a claim about a transport receipt, and the receipt names a recipient. An assignment's recipient role maps to a session in the campaign budget; a SENT whose receipts do not
    include that session is refused (2026-11-14: a message headed 'to ADV and HE' was received by HE alone and ADV waited). UNREACHABLE needs no receipt."""
    if state != "SENT":
        return ""
    row = next((e for e in _events(campaign) if e.get("id") == ident and e.get("state") == "DRAFTED"), None)
    if row is None:
        return f"{ident} is not a drafted assignment of this campaign"
    session = (_budget(campaign).get("recipients") or {}).get(row.get("recipient", ""))
    if not any(RECEIPT_ID.fullmatch(r.strip()) for r in (receipt or [])) and not RECEIPT_ID.search(evidence or ""):
        # 2026-11-19 (ADV, three times in two days): a SENT recorded before the send happened. The send's own receipt id (the msg_id that SendMessage returns, a UUID) is the proof that it did.
        return (f"SENT needs the send's own receipt id (the msg_id SendMessage returned, a UUID) in --receipt or inside --evidence: {ident} may not be recorded as sent before the send has happened. "
                "UNREACHABLE needs none")
    if not to:
        return (f"SENT needs --to <session> for the real send(s): the receipt, not the text of the message, says who received it. {ident} is for {row.get('recipient')}"
                + (f" = session {session!r}" if session else ""))
    if session and session.lower() in {t.strip().lower() for t in to}:
        return ""
    # 2026-11-18: a session revived under another display name made a real send unregistrable (the receipt named the new name, the budget the old one). Identity is the session, not its name: both sides are
    # resolved against the LIVE sessions (a listed entry without a process is not live), with a record's binding or marker before a display name, and compared by session id.
    live = _live_agents()
    if session and live:
        import mandate_watch as mw
        want = mw.route(session, live, ROOT)
        got = [mw.route(t.strip(), live, ROOT) for t in to]
        if want["status"] == "RESOLVED" and any(g["status"] == "RESOLVED" and g["session_id"] == want["session_id"] for g in got):
            return ""
        if want["status"] == "RESOLVED":
            names = ", ".join(f"{g.get('recipient') or t} ({g['status']})" for t, g in zip(to, got))
            return (f"the receipt names {names}; {ident} is for {row.get('recipient')} = session {want['recipient']!r} [{want['session_id'][:8]}]. Send it to that session (one send per recipient) and record that receipt")
        return (f"{row.get('recipient')} = {session!r} does not resolve to exactly one live session ({want['status']}: {want.get('why', '')}); a send to it cannot be recorded as SENT: record UNREACHABLE, "
                "or name the session by its id in the budget recipients")
    if session:
        return f"the receipt names {', '.join(to)}; {ident} is for {row.get('recipient')} = session {session!r}. Send it to that session (one send per recipient) and record that receipt"
    return ""


def _live_agents() -> list[dict[str, Any]]:
    """The runtime's listing, minus the entries whose process is gone (`claude agents --json` keeps killed and stopped sessions without a pid)."""
    import mandate_watch as mw
    return [x for x in (_agents() or []) if isinstance(x, dict) and mw.session_is_live(x)]


def _log_assignment(campaign: Path, row: dict[str, Any]) -> None:
    with (Path(campaign) / "assignments.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({**row, "utc": _utc(_now())}, sort_keys=True) + "\n")


def register_assignments(campaign: Path, label: str, text: str, *, origin: str = "assessment") -> list[dict[str, str]]:
    """Serialise only draft-id allocation, not research, delivery or consultation."""
    lock = _state_path(Path(campaign)).parent / "assignments.lock"
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open("a") as guard:
        fcntl.flock(guard, fcntl.LOCK_EX)
        return _register_assignments(campaign, label, text, origin=origin)


def _register_assignments(campaign: Path, label: str, text: str, *, origin: str) -> list[dict[str, str]]:
    """Save the drafts of an assessment as `assignments/ADV-nnn.md`, within the campaign's assignment budget and without duplicating a key already drafted or already named in a task record."""
    campaign = Path(campaign)
    cap = 10**9 if continuous(campaign) else int(_budget(campaign).get("max_assignments", 10**9))      # the pilot's assignment cap is history in continuous operation
    known = _events(campaign)
    drafted = {e["id"]: e for e in known if e["state"] == "DRAFTED"}
    records = "\n".join((ROOT / r["path"]).read_text(encoding="utf-8", errors="replace") for r in _records().values() if "PROACTIVE-ADVISOR" not in r["path"])
    made = []
    for block in parse_assignments(text):
        key = block.get("key", "").strip()
        if not key or block["_missing"]:
            _log_assignment(campaign, {"id": "", "state": "REJECTED", "key": key, "why": f"missing fields: {block['_missing'] or 'key'}", "assessment": label}); continue
        if any(e["key"] == key for e in drafted.values()) or key in records:
            _log_assignment(campaign, {"id": "", "state": "DUPLICATE", "key": key, "why": "key already drafted or already named in a task record", "assessment": label}); continue
        if len(drafted) >= cap:
            _log_assignment(campaign, {"id": "", "state": "OVER_BUDGET", "key": key, "why": f"the campaign allows {cap} assignments", "assessment": label}); continue
        ident = f"ADV-{len(drafted) + 1:03d}"
        out = campaign / "assignments"
        out.mkdir(exist_ok=True)
        attribution = "host decision (not an independent assessment)" if origin == "host" else f"assessment {label}"
        (out / f"{ident}.md").write_text(f"# {ident} ({attribution}, campaign {campaign.name})\n\nRecipient: {block['recipient']}\n\n{block['_text']}\n", encoding="utf-8")
        row = {"id": ident, "state": "DRAFTED", "key": key, "recipient": block["recipient"], "assessment": label, "origin": origin}
        if block.get("strand"):
            row["strand"] = block["strand"]                      # the thread this increment belongs to (scientific rotation); optional, never a reason to refuse a draft
        _log_assignment(campaign, row); drafted[ident] = row; made.append({"id": ident, **block})
    return made


def host_assign(campaign: Path, text: str) -> int:
    """The authorised ADV host can choose work without commissioning its consultant.

    Uses the existing drafts, duplicate check and delivery receipts. It does not send,
    launch a model or manufacture acceptance/consumption. A completed host choice settles
    its observed event boundary; later deliveries remain pending.
    The bounded pilot is unchanged; a continuous campaign must already be authorised.
    """
    campaign = Path(campaign)
    refusal = primary_refusal() or budget_refusal(campaign)
    if not refusal and not continuous(campaign):
        refusal = "direct host assignments require the existing continuous authorisation"
    if refusal:
        print(f"REFUSED: {refusal}", file=sys.stderr)
        return 2
    blocks = parse_assignments(text)
    if not blocks or any(b.get("_missing") for b in blocks):
        print("No assignments registered: use the existing complete ASSIGNMENT blocks", file=sys.stderr)
        return 2
    before = _load_state(campaign)
    obs = observe(campaign, before)
    handled = list(dict.fromkeys(list(before.get("pending_events") or []) + obs["events"]))
    made = register_assignments(campaign, "HOST", text, origin="host")
    if not made:
        print("No new draft: the same work is already recorded; follow its existing owner")
        return 0
    state = _load_state(campaign)
    if _running(state):
        print("Host decision registered (not sent): " + ", ".join(b["id"] for b in made)
              + "; consultant still running: preserve its observation boundary and reconcile its returned drafts")
        return 0
    state["last_outcome"] = {
        "evaluation": "HOST", "origin": "host", "utc": _utc(_now()), "stated": True,
        "outcome": "assign", "reason": " | ".join(f"{b['id']}: {b['why_now']}" for b in made),
        "excluded": "See each assignment's related_work and duplicate_check; host choice, not independent review",
        "resume_when": "event", "problem": "",
    }
    later = [e for e in state.get("pending_events", []) if e not in handled]
    state.update(main_sha=obs["main_sha"], main_ref=(obs.get("main_ref") or {}).get("ref", "main"), mandates=obs["mandates"], roadmap_sha256=obs["roadmap_sha256"],
                 portfolio_digest=obs["portfolio"]["digest"],
                 last_digest=sha256_text(obs["roadmap_sha256"] + "|" + "|".join(sorted(handled))),
                 pending_events=later, pending_commits=state.get("pending_commits", 0) if later else 0,
                 waits_seen=sorted({sha256_text(w["task"] + "|" + w["blocker"])[:12] for w in obs["waits"]}))
    _save_state(campaign, state)
    print("Host decision registered (not sent): " + ", ".join(b["id"] for b in made))
    return 0


SENDER_RECORDS = ("PROACTIVE-ADVISOR", "ADV-PRESIDIO", "ADV-FOLLOWTHROUGH")   # the records of the sessions that draft and deliver (the pilot implementation, the presidio): their naming a draft or its delivery is not a recipient taking it in charge. Harness is also a recipient: its own record (PLAN-ADV-SESSION) is NOT excluded


def assignment_states(campaign: Path) -> dict[str, dict[str, Any]]:
    """Per assignment, the evidence levels kept apart: DRAFTED (saved) -> SENT (the channel accepted a message: recorded by the sender) -> TAKEN (its id is in a task record) -> EXECUTED (a
    DONE step in a record carries its id) . UNREACHABLE and the other rows are states of their own. None of them says the result was useful."""
    out: dict[str, dict[str, Any]] = {}
    for e in _events(campaign):
        if e.get("id") and e.get("state") not in META_STATES:
            out.setdefault(e["id"], {"recipient": e.get("recipient", ""), "key": e.get("key", ""), "origin": e.get("origin", "assessment"), "levels": []})["levels"].append(e["state"])
    taken, done = set(), set()
    def walk(node: Any, ident: str) -> tuple[bool, bool]:
        hit, ok = False, False
        if isinstance(node, dict):
            blob = json.dumps(node)
            if ident in blob and str(node.get("status", "")).upper() == "DONE":
                ok = True
            for v in node.values():
                h, o = walk(v, ident); hit, ok = hit or h, ok or o
        elif isinstance(node, list):
            for v in node:
                h, o = walk(v, ident); hit, ok = hit or h, ok or o
        elif isinstance(node, str) and ident in node:
            hit = True
        return hit, ok
    if out:
        for path in (ROOT / "ledger" / "tasks").glob("*/*.json"):
            try:
                d = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            for ident in out:
                h, o = walk(d, ident)
                if any(tag in path.name for tag in SENDER_RECORDS):
                    continue                                      # the sender's own records name the drafts and their delivery (a DONE delivery step included): that is not a recipient taking one in charge
                if h and "TAKEN" not in out[ident]["levels"]:
                    out[ident]["levels"].append("TAKEN")
                if h:
                    try:
                        verdict = mc.verdict(d)["verdict"]
                    except Exception:  # noqa: BLE001 — unknown is never in flight or complete
                        verdict = "UNREADABLE"
                    out[ident].setdefault("mandates", []).append({"task": d.get("TASK_ID", path.stem), "verdict": verdict, "path": str(path.relative_to(ROOT))})
                if o and "EXECUTED" not in out[ident]["levels"]:
                    out[ident]["levels"].append("EXECUTED")
    for v in out.values():
        order = ["DRAFTED", "SENT", "TAKEN", "EXECUTED"]
        v["highest"] = max((x for x in v["levels"] if x in order), key=order.index, default="")
        v["unreachable"] = "UNREACHABLE" in v["levels"] and v["highest"] in ("", "DRAFTED")
    return out


def scout_briefing(limit: int = 6000) -> str:
    """The daily scout's latest briefing from the host cache (outside the repository, so outside the advisor's reach): read here by the caller, dated, shortened, addresses removed."""
    path = STATE_HOME / "scout_daily_briefing.md"
    if not path.is_file():
        return "(no live scouting briefing found on this host: harness and repository opportunities cannot be assessed from the weekly tables, whose last week is old)"
    text = re.sub(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", "[address removed]", path.read_text(encoding="utf-8", errors="replace"))
    stamp = dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    return f"file time {stamp}; {'first %d of %d characters' % (limit, len(text)) if len(text) > limit else 'complete'}\n\n" + text[:limit]


def turn_limit_text(campaign: Path) -> str:
    """What the launcher's turn limit means for the run, from the campaign's own value: the advisor saw it only as a number inside the limits JSON and P4 spent all its turns reading (2026-11-14)."""
    n = int(_budget(campaign).get("turn_limit") or 0)
    if not n:
        return ""
    return (f"## Turn limit\nturn_limit is {n}, a hard stop: at turn {n + 1} the run is killed, counts as one of the campaign's invocations and returns nothing. Count your turns; "
            f"stop opening files by turn {max(n - 6, 1)} at the latest and write the assessment (with the Assignments section) in your last turns; a partial assessment is better than none.")


def followthrough_text() -> str:
    """HE54: what an evaluation does with a wait. A judgment, never a duty to fill every wait: `none: <reason>` is a complete answer when waiting is the cheaper choice."""
    return ("## Waiting and follow-through\nWhen sessions or a chain of dependencies wait for a battery, a CI run, a delivery or another answer (see `waits` above; an expected long wait can be enough, you need not wait until every session is idle), "
            "judge whether to: (independent) anticipate an activity that does not depend on the awaited result, does not touch the candidate or the clones, processes and directories under verification, and that the shared resources allow; "
            "(queued) prepare an assignment to run after the current work, which the recipient holds as a BLOCKED step with `unblock_when` in its own record; (conditional) prepare only the question or the alternative that depends on the expected result, "
            "never executing every branch ahead; or keep waiting because nothing would justify its cost or risk. Say which, and why. An assignment names why it is useful, its `mode`, `start_condition`, the result expected and the decision it touches, "
            "`interferes_with` and `obsolete_if` (optional fields; no new contract). The recipient may anticipate part, keep it queued, reorder it or declare it superseded, giving the reason in its own record, without asking anyone; reconcile a queued "
            "assignment with the results that arrived before you propose to start it. A new integration that needs changes to a frozen candidate is a later increment, not an edit of the proof. Keep queues short and reviewable. "
            "Group events and reuse an assessment that is still pertinent; do not turn every WAITING into an expensive evaluation. An assignment already drafted and authorised is delivered in the turn that reads it.")


def portfolio_text() -> str:
    """HE57: the principle in a few lines, with its single home named. The evaluation is where the choice of what comes next is made, also when no radar, result or instruction arrived."""
    return ("## Portfolio selection (cross-session transport section 12, 'Continuity is a choice of what comes next')\n"
            "A closed mandate, an empty queue or no new radar does not end the work by itself. When no written executable step remains (see `queue` below: a statement about task records with its blocked paths, not about the portfolio), decide what is next from what you can reach: the roadmap and the "
            "objectives still pursuable; open questions (which answer would change a decision, which part can be approached now); scientific threads (unresolved premises, rival explanations, promising or contrary results); the source "
            "records and dashboards; knowledge held but not consumed or combined; the DREAM pass when new associations can orient a concrete question; earlier radars not yet evaluated; harness obstacles and tools used badly or little; "
            "project invariants (rigidity, duplication, cost, complexity, a chance to simplify). Reasoning aids, not a checklist: an open experimental question does not oblige the bibliography to go on, a possible improvement is not a mission. "
            "Rank in prose, no score: importance of the decision, concrete probability of progress, marginal benefit, what it could unblock, total and shared cost, coherence with the roadmap, simplicity, reversibility. "
            "A broad opportunity is planning work: narrow it to a useful question or ask the Orchestrator to select a sourced case; do not reject it merely because no small task is already written. "
            "Generate competing hypotheses and pharmacological comparisons as well as checking old ones. Consider unread WWOX literature through coverage tools, not just the newest radar hits; abstracts are census, never a completed reading. "
            "A wet-lab gap blocks its branch, not every other branch. A distant trial report is reporting work, not a reservation of all sessions' capacity. Operator silence neither pauses the roadmap nor supplies a missing assignment. "
            "Before a whole-portfolio wait, inspect the live records that support it; an existing mandate file does not mean its work is in flight. Read the originals that bear on the chosen decision. "
            "Outcomes: continue, switch thread, assign independent work, queue a conditional follow-up, or wait; a wait says which relevant alternatives it excluded and why, and when it resumes, and it names every ready portfolio row it leaves out with the cause: a blocked path (an intake, a laboratory, a source) is not a blocked portfolio. "
            "Do not repeat an evaluation that is still valid, do not draft what is already drafted or taken in charge, do not treat your own updates as news, and do not invent work to stay busy. Operator pauses, resource limits, reserved acts and real dependencies still bind.")


def previous_outcome_text(campaign: Path) -> str:
    state = _load_state(campaign)
    o = state.get("last_outcome") or {}
    if not o:
        rejected = state.get("last_invalidated_outcome") or {}
        if rejected:
            return ("## Previous outcome superseded\nThe stored decision was invalidated, not silently forgotten. Do not reuse its recommendation.\n"
                    + json.dumps(rejected, indent=1))
        return "## Previous outcome\nnone recorded (an evaluation before this field existed, or the first one)."
    return "## Previous outcome (what the last evaluation decided; reconsider it when something that bears on it changed, reuse it when nothing did)\n" + json.dumps({k: o.get(k) for k in ("evaluation", "utc", "outcome", "reason", "excluded", "resume_when", "stated", "problem")}, indent=1)


def operating_mode_text(campaign: Path) -> str:
    """The brief's statement of the operating mode. In continuous operation the pilot's ceilings are history and the one thing that binds the run is the turn limit; nothing here asks for work to be invented."""
    cont = continuous(campaign)
    if not cont:
        return "## Operating mode\nbounded pilot: the limits above are the rule.\n\n" + followthrough_text()
    week = weekly_state(campaign)
    ctl = [f"{c['kind']}: {c['text']}" for c in operator_controls()][-8:]
    return ("## Operating mode\ncontinuous: the operator authorised the Advisor to continue inside the roadmap, the existing boundaries and the available resources (authorisation of "
            f"{cont['authorised_utc']}; the pilot's totals and expiry above are history). An assignment that ends does not end the presidio. Select and prepare useful work from the standing roadmap; operator silence and a future review are not dependencies. "
            "A supported whole-portfolio constraint can justify waiting; no active-work quota applies. Radar and scouting items are opportunities to compare with the current thread, the other open questions, the promising comparisons, "
            "knowledge already held and concrete obstacles; they are not orders and not a second roadmap, and nothing is installed because a radar recommends it. "
            f"Shared weekly allocation: {week['state']} ({week.get('note', 'measured and enforced for this presidio')}). Measurement scope: {week['measurement_scope']} "
            f"Operator control lines in the roadmap section (most recent last): {json.dumps(ctl)}.\n\n" + followthrough_text())


def direction_before_status_text() -> str:
    """Render the shared rule from its one home; do not maintain a second prompt policy."""
    path = ROOT / "framework/protocols/cross_session_transport.md"
    try:
        paragraphs = path.read_text(encoding="utf-8").split("\n\n")
    except OSError:
        paragraphs = []
    paragraph = next((p.strip() for p in paragraphs if p.startswith("**Direction before status (")), "")
    return "## Direction before status\n" + (paragraph or
        "Canonical guidance unavailable in framework/protocols/cross_session_transport.md section 12. "
        "Disclose the missing input; do not treat it as evidence that useful research is exhausted.")


def laboratory_ownership_text() -> str:
    """Source the effective accountability rule; do not fork it in the runtime prompt."""
    try:
        text = (ROOT / "framework/protocols/cross_session_transport.md").read_text(encoding="utf-8")
    except OSError:
        text = ""
    match = re.search(r"^### Laboratory ownership[^\n]*\n(.*?)(?=^### |\Z)", text, re.M | re.S)
    return "## Laboratory ownership\n" + (match.group(1).strip() if match else
        "Canonical accountability guidance unavailable in cross_session_transport.md section 12; disclose the missing input.")


def current_result_sources(obs: dict[str, Any], snap: dict[str, Any]) -> str:
    """Index originals at pinned revisions, including changes to existing files.

    No source is summarised, copied, fetched or declared read. The host can reconcile
    an unavailable original at a safe boundary; the analyst cannot assume it saw it.
    """
    lines = ["## Current result sources", f"Observed main: `{obs.get('main_sha') or 'unknown'}`; readable checkout: `{snap.get('repo_sha') or 'unknown'}`.",
             "These are source locations, not evidence or a shortlist. Read the relevant original and current recipient record before proposing work already reported complete."]
    refs: dict[str, set[str]] = {}
    ahead_sources: dict[str, list[str]] = {}
    for event in obs.get("events", []):
        match = re.match(r"delivery: ([0-9a-f]{7,40})\b", event)
        if match:
            ref = match.group(1)
            refs.setdefault(ref, set()).update(_git("diff", "--name-only", f"{ref}^", ref).splitlines())
    for ahead in snap.get("main_ahead", []):
        ref = ahead["tip"]
        changed = _git("diff", "--name-only", "HEAD", ref).splitlines()
        refs.setdefault(ref, set()).update(changed)
        for rel in changed:
            ahead_sources.setdefault(rel, []).append(ref)
    by_path: dict[str, list[str]] = {}
    for ref, paths in refs.items():
        relevant = sorted(p for p in paths if p.startswith(("disease-models/wwox/research/", "ledger/tasks/"))
                          and Path(p).suffix in (".md", ".tsv", ".json")
                          and "/assignments/" not in p and not re.search(r"/P\d+/", p))
        for rel in relevant:
            by_path.setdefault(rel, []).append(ref)
    current = obs.get("main_sha") or snap.get("repo_sha") or "HEAD"
    for rel, provenance in list(by_path.items())[:24]:
        blob = _git("rev-parse", "--verify", f"{current}:{rel}")
        local = _git("hash-object", "--", rel) if (ROOT / rel).is_file() else ""
        availability = ("removed at observed main; do not resurrect the older delivery" if not blob else
                        "same bytes readable here" if blob == local else
                        "DIFFERS OR UNAVAILABLE here; host must reconcile the original")
        lines.append(f"- `{rel}` @ `{current}`: {availability}. Change provenance: {', '.join(provenance)}.")
        for ref in ahead_sources.get(rel, []):
            newer = _git("rev-parse", "--verify", f"{ref}:{rel}")
            if newer != blob:
                lines.append(f"  Newer known ref `{ref}` has different or removed content; it is NOT supplied by the observed-main copy. Reconcile before relying on that copy as current.")
    if len(by_path) > 24:
        lines.append(f"Index shows 24 of {len(by_path)} changed source paths; the pinned revisions retain every original. This is not a coverage census.")
    if not by_path:
        lines.append("No changed result path identified from these events; use the permanent source map and portfolio. This does not establish exhaustion.")
    return "\n".join(lines)


def _compact(obj: Any) -> str:
    """HE95 (2026-11-17): the same JSON with no indentation (the separators keep one space, as the readers and tests of the brief expect): one line, every key and value kept."""
    return json.dumps(obj, separators=(", ", ": "))


def render_assignment_states(states: dict[str, Any]) -> str:
    """One line per assignment; each mandate named once with its verdict and path (the same four mandates were repeated under most assignments). Nothing is dropped: every assignment keeps its
    recipient, key, origin, highest evidence level and its mandates, and every mandate keeps its verdict and path."""
    if not states:
        return "none"
    mandates: dict[str, dict[str, Any]] = {}
    lines = []
    for k, v in states.items():
        ids = []
        for m in v.get("mandates", []):
            mandates.setdefault(m["task"], {key: val for key, val in m.items() if key != "task"})
            ids.append(m["task"])
        lines.append(_compact({"id": k, "recipient": v["recipient"], "key": v["key"], "origin": v.get("origin", "assessment"), "highest": v["highest"], "mandates": ids}))
    return "Mandates referenced below (task: verdict and path):\n" + "\n".join(f"{t}: {_compact(m)}" for t, m in mandates.items()) + "\nAssignments (one per line):\n" + "\n".join(lines)


def build_brief_p(campaign: Path, obs: dict[str, Any]) -> str:
    campaign = Path(campaign)
    states = assignment_states(campaign)
    attempts = sorted((p for p in campaign.glob("P*/assessment.md") if re.fullmatch(r"P\d+", p.parent.name)), key=lambda p: int(p.parent.name[1:]))
    incomplete = {p.parent.name: why for p in attempts if (why := incomplete_run(campaign, p.parent.name))}
    prior = [p for p in attempts if p.parent.name not in incomplete]
    snap = snapshot()
    activity = obs.get("activity") or session_activity(_now())
    parts = ["# Strategic Advisor brief — Stage P (proactive evaluation)", "", "## Snapshot", render_snapshot(snap), "",
             "## Operator roadmap (authoritative; operator instructions prevail over any automatic plan)", roadmap_text() or "(no roadmap section found: say so, and propose nothing beyond keeping the plan)", "",
             "## Campaign limits", json.dumps({k: v for k, v in _budget(campaign).items() if k in ("expires_utc", "max_invocations", "max_assignments", "turn_limit")}), "",
             operating_mode_text(campaign), "",
             laboratory_ownership_text(), "",
             direction_before_status_text(), "",
             "## Neutral entry points", render_entrypoints(entrypoints()), "", f"Memory directory (read-only): `{MEMORY_DIR}`", "",
             current_result_sources(obs, snap), "",
             "## Live harness scouting (daily scout briefing, read by the caller: opportunities, not evidence)", scout_briefing(), "",
             portfolio_text(), "",
              portfolio_brief(obs.get("portfolio") or portfolio_snapshot()), "",
              "For a material portfolio change you may add an optional `## Portfolio updates` section with a fenced json list of partial row objects (stable `id` required). The procedure saves the assessment verbatim, then applies these advisory patches. "
              "No section is needed when nothing changes. Preserve sources, link the recipient's mandate when known, record the actual consumer and the next question; do not mark an opportunity done merely because an assignment was sent. "
              "This does not alter the operator mission or promote any scientific conclusion.", "",
            "## Observed state (mechanical, this tick)", _compact({k: obs[k] for k in ("events", "open_mandates", "waits", "queue", "sessions", "commits_since_last_tick")}), "",
            "## Laboratory activity (observation, not a verdict on useful work)", _compact(activity), "",
            previous_outcome_text(campaign), "",
             "## Assignments already drafted, with their evidence level (do not duplicate; follow what was taken in charge)",
             render_assignment_states(states), "",
             "Evidence levels are historical transport facts. Current mandate verdicts and their paths are listed separately: TAKEN does not mean still running, RELEASED does not prove consumption. Read the relevant complete record before relying on its state. "
             "The latest saved assessment is historical context; it is not evidence that its old premises remain true.", "",
             f"## Previous assessment\n{prior[-1].parent.name}: `{prior[-1]}` (historical decision; reconcile after framing the direction; reuse while its premises and expected value still hold)" if prior else "## Previous assessment\nnone", "",
             "## Incomplete attempts (history, not reusable decisions)\n" + (_compact(incomplete) if incomplete else "none"), "",
             turn_limit_text(campaign), "",
             "## Output", CONTRACT,
             "Give the usual headings, then `## Assignments`: either `none: <reason>` (continuing the plan can be the best decision) or one `### ASSIGNMENT n` block per assignment with exactly these "
             "`field: value` lines: " + ", ".join(ASSIGNMENT_FIELDS) + ". recipient is Orchestrator, Science or Harness. At most as many blocks as the campaign allows; none to show independence.",
             "Finish with `## Outcome`, four `field: value` lines: `outcome:` one of " + ", ".join(OUTCOMES) + "; `excluded:` (for a wait: the relevant alternatives you left out, each with why); `reason:`; "
             "`resume_when:` event | record:<TASK_ID>=<STATE> | path:<file>[~<text>] | after:<UTC>; it is read only for a wait (write `event` for any other outcome), and `record:` only with an id that already exists in the records "
             "(an id the recipient has not created yet is read as `event`). The tick reads this block and nothing else of your decision: without it the wait is not motivated and one more evaluation is asked for.", ""]
    return "\n".join(parts)


def incomplete_run(campaign: Path, label: str) -> str:
    """Why a finished run must not be acted on, or "". P11 (2026-11-15) was cut short by a classifier stop after 4 tool calls, did not read the records it reasoned from and believed a delivery was still in flight; evaluate applied its portfolio updates and took its wait. The test is two measured facts: the runtime recorded a refusal fallback AND the run made fewer than MIN_CALLS_AFTER_FALLBACK tool calls."""
    try:
        meta = json.loads((campaign / label / "meta.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ""
    fell = (meta.get("runtime_readback") or {}).get("refusal_fallbacks") or []
    calls = len(meta.get("tool_calls") or [])
    if fell and calls < MIN_CALLS_AFTER_FALLBACK:
        return f"a runtime refusal fallback ({fell[0].get('apiRefusalCategory')}) cut the run short after {calls} tool call(s), fewer than {MIN_CALLS_AFTER_FALLBACK}"
    return ""


def evaluate(campaign: Path, model: str = "opus", effort: str = "high", timeout: int = 3600) -> int:
    """One strategic evaluation: brief, run (counted in the campaign budget), save, register the assignment drafts. Returns the run's exit code."""
    campaign = Path(campaign)
    refusal = budget_refusal(campaign)
    if refusal:
        print(f"REFUSED: {refusal}", file=sys.stderr); return 2
    state = _load_state(campaign)
    if _running(state):
        print("REFUSED: an evaluation is already running", file=sys.stderr); return 2
    started_utc = _utc(_now())
    state["running"] = _pid_identity(os.getpid()); _save_state(campaign, state)
    try:
        obs = observe(campaign, state)
        obs["events"] = list(dict.fromkeys(list(state.get("pending_events") or []) + obs["events"]))
        obs["commits_since_last_tick"] += int(state.get("pending_commits") or 0)
        consumed_portfolio_digest = obs["portfolio"]["digest"]
        brief = _state_path(campaign).parent / "brief_P.md"       # the working copy lives with the host state, outside the checkout: regenerating it no longer dirties the tree during a landing; the brief that matters for reproducibility is saved in P<n>/brief.md by `run`
        brief.parent.mkdir(parents=True, exist_ok=True)
        brief.write_text(build_brief_p(campaign, obs), encoding="utf-8")
        code = run("P", campaign, brief, model, effort, timeout, LIMITS)
        label = f"P{max((a['index'] for a in _attempts(campaign) if a['stage'] == 'P'), default=0)}"
        assessment = campaign / label / "assessment.md"
        outcome = parse_outcome("")
        incomplete = incomplete_run(campaign, label) if code == 0 and assessment.exists() else ""
        if incomplete:
            print(f"{label}: INCOMPLETE — {incomplete}; no assignment, portfolio update or outcome was taken from it")
            state = _load_state(campaign)
            state.update(last_evaluation_utc=_utc(_now()), last_evaluation_started_utc=started_utc, running="", last_incomplete={"evaluation": label, "utc": _utc(_now()), "reason": incomplete})      # the triggers stay pending: the next evaluation still has to see them
            _save_state(campaign, state)
            return code
        if code == 0 and assessment.exists():
            text = assessment.read_text(encoding="utf-8")
            made = register_assignments(campaign, label, text)
            print(f"{label}: {len(made)} assignment draft(s) registered: " + ", ".join(m["id"] for m in made))
            unchanged_since_read = portfolio_snapshot()["digest"] == obs["portfolio"]["digest"]
            for message in apply_portfolio_updates(text):
                print(message)
            if unchanged_since_read:
                consumed_portfolio_digest = portfolio_snapshot()["digest"]  # own annotations are not new evidence
            outcome = parse_outcome(text)
            if outcome["stated"] and outcome["outcome"] == "wait":
                problem = resume_problem(outcome["resume_when"])
                if not problem and outcome["resume_when"].startswith("record:") and not list((ROOT / "ledger" / "tasks").glob(f"*/{outcome['resume_when'][7:].split('=', 1)[0].strip()}.json")):
                    problem = f"resume_when names a record that does not exist ({outcome['resume_when'][7:].split('=', 1)[0].strip()}); read as event"      # P8 (2026-11-14) wrote an id the recipient had not created yet: a wait on it would never resume
                if problem:
                    outcome.update(resume_when="event", problem=problem)
                elif resume_met(outcome["resume_when"], _now()):
                    outcome.update(resume_when="event", problem="the resume condition was already met when the wait was stated; read as event")     # a wait that is over the moment it starts would be evaluated again every hour
            if outcome["stated"] and outcome["outcome"] == "wait":
                missing = unaccounted_ready(portfolio_snapshot(), outcome["reason"], outcome["excluded"])
                if missing:                                       # 2026-11-16: 'nothing queued, awaiting X' while nine portfolio rows were ready; a wait names every ready row it leaves out, with the cause
                    outcome.update(stated=False, problem="a wait must name each ready portfolio row it leaves out, with its cause: " + ", ".join(missing[:8]))
        print(f"{label}: outcome {outcome['outcome'] or 'unstated'}" + (f" ({outcome['problem']})" if outcome["problem"] else ""))
        state = _load_state(campaign)
        state.update(last_evaluation_utc=_utc(_now()), last_evaluation_started_utc=started_utc, last_digest=state.get("pending_digest", state.get("last_digest")), running="", pending_events=[], pending_commits=0, last_incomplete={},
                     portfolio_digest=consumed_portfolio_digest,
                     last_outcome={**outcome, "evaluation": label, "utc": _utc(_now())}, unstated_streak=0 if outcome["stated"] else int(state.get("unstated_streak") or 0) + 1)
        _save_state(campaign, state)
        return code
    finally:
        state = _load_state(campaign); state["running"] = ""; _save_state(campaign, state)


def _holds(campaign: Path) -> list[dict[str, Any]]:
    path = Path(campaign) / "holds.jsonl"
    out = []
    for line in path.read_text(encoding="utf-8").splitlines() if path.exists() else []:
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def hold(campaign: Path, reason: str, resume_when: str, excluded: str = "") -> int:
    """HE64: record a hold WITHOUT a model run. Until now the pending digest was consumed only when an evaluation completed (`evaluate`, last_digest), so a hold decided by hand re-fired EVALUATE at every hourly tick
    (measured on a copy of the real state, 2026-11-15: two ticks, same digest, 12 events carried, ten recalls since the last evaluation). A hold consumes what it lists and nothing else: the events and the commit count it clears
    are written into holds.jsonl; it is not an evaluation (no invocation, no P<n> folder, no budget, last_evaluation_utc untouched); it ends at its resume_when (an external form), at a roadmap change or at the first NEW event."""
    campaign = Path(campaign)
    refusal = budget_refusal(campaign)
    if refusal:
        print(f"REFUSED: {refusal}", file=sys.stderr); return 2
    state = _load_state(campaign)
    if _running(state):
        print("REFUSED: an evaluation is running; a hold would race its own consumption of the pending events", file=sys.stderr); return 2
    if not (reason or "").strip():
        print("REFUSED: a hold needs a reason (what makes waiting the right choice)", file=sys.stderr); return 2
    if not names_a_path(excluded):
        print("REFUSED: a hold needs --excluded: the paths it leaves out (record ids, portfolio rows or files) and the actual cause of each; a hold that names no path is a general wait", file=sys.stderr); return 2
    spec = (resume_when or "").strip()
    problem = resume_problem(spec)
    if problem or not spec.startswith(("record:", "path:")):
        print("REFUSED: resume_when must name an external event: `record:<TASK>=<STATE>` or `path:<file>[~<text>]` (a time or `event` alone would make a hold a timer for silence)" + (f"; {problem}" if problem else ""), file=sys.stderr); return 2
    if spec.startswith("record:") and not list((ROOT / "ledger" / "tasks").glob(f"*/{spec[7:].split('=', 1)[0].strip()}.json")):
        print(f"REFUSED: resume_when names a record that does not exist ({spec[7:].split('=', 1)[0].strip()}); a hold on it would never end", file=sys.stderr); return 2
    if not state:
        print("REFUSED: no tick state yet; the first tick records the baseline", file=sys.stderr); return 2
    obs = observe(campaign, state)
    events = list(dict.fromkeys(list(state.get("pending_events") or []) + obs["events"]))
    commits = obs["commits_since_last_tick"] + int(state.get("pending_commits") or 0)
    if not events:
        print("REFUSED: nothing is pending, so there is nothing to hold; the verdict is already quiet", file=sys.stderr); return 2
    missing = unaccounted_ready(obs["portfolio"], reason, excluded)
    if missing:
        print(f"REFUSED: the portfolio has ready rows this hold does not name ({', '.join(missing[:8])}); take them, queue them with a reason, mark them waiting with a resume_when, or name each in --excluded with its cause. A blocked path is not a blocked portfolio", file=sys.stderr); return 2
    digest = sha256_text(obs["roadmap_sha256"] + "|" + "|".join(sorted(events)))
    now = _utc(_now())
    record = {"utc": now, "reason": reason.strip(), "excluded": excluded.strip(), "resume_when": spec, "digest": digest, "events_cleared": events, "commits_cleared": commits,
              "previous_digest": state.get("last_digest", ""), "previous_outcome": {k: (state.get("last_outcome") or {}).get(k, "") for k in ("evaluation", "outcome", "utc")}, "main_sha": obs["main_sha"]}
    with (campaign / "holds.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")
    state.update(main_sha=obs["main_sha"], main_ref=(obs.get("main_ref") or {}).get("ref", "main"), mandates=obs["mandates"], roadmap_sha256=obs["roadmap_sha256"], waits_seen=sorted({sha256_text(w["task"] + "|" + w["blocker"])[:12] for w in obs["waits"]}),   # what a tick records as observed: the listed events must not be read again
                 last_digest=digest, pending_digest=digest, pending_events=[], pending_commits=0, portfolio_digest=obs["portfolio"]["digest"], unstated_streak=0,
                 last_outcome={"stated": True, "outcome": "wait", "reason": reason.strip(), "excluded": excluded.strip(), "problem": "", "resume_when": spec, "evaluation": "HOLD", "utc": now})
    _save_state(campaign, state)
    print(f"HOLD recorded {now}: {len(events)} event(s) and {commits} commit(s) cleared and listed in {campaign / 'holds.jsonl'}; resume_when {spec}")
    return 0


FLOW_WINDOW_H = 72
FLOW_FLAG_H = 24
FLOW_NOT_TAKEN_MIN = 30
FLOW_NO_OUTPUT_H = 3.0


def _flow_rx(ident: str) -> re.Pattern:
    """The exact token of an assignment id: ADV-101 in text, adv101 or ADV_101 in a file name; never a prefix of a longer number (ADV-10 does not match ADV-101)."""
    m = re.fullmatch(r"([A-Za-z]+)-(\d+)", ident)
    if not m:
        return re.compile(r"(?<![\w-])" + re.escape(ident) + r"(?![\w-])")
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(m.group(1)) + r"[-_ ]?" + m.group(2) + r"(?!\d)", re.I)


def _stamp(text: Any) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(str(text).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def assignment_flow(campaign: Path, now: dt.datetime | None = None, ref: str | None = None, window_h: int = FLOW_WINDOW_H) -> list[dict[str, Any]]:
    """2026-11-20 (ADV, 'Reliable autonomy'): 'message sent' proves neither take-in-charge, start nor consumption. One row per assignment SENT in the last `window_h` hours: SENT (the receipt event) -> TAKEN (a record of a
    RECIPIENT, not of the presidio, names the exact id in a step, with that step's accepted or updated time) -> FIRST OUTPUT (the earliest commit subject on the observed ref, or file added under the repository, naming the id
    after the send). Only subjects, file names and record text are read for the exact token; nothing is matched fuzzily. A reply message leaves no durable trace and is not seen. Flags: 'SENT, NOT TAKEN after N min' (30)
    and 'TAKEN, no output after N h' (3 by default; a DRAFTED row may carry `expect_hours`; not raised once a recipient record holds a DONE step with the id). The ids are the tokens; an id that appears in a recipient record before the send (a carried-over mention) does not count as TAKEN."""
    now = now or _now()
    events = _events(campaign)
    drafted = {e["id"]: e for e in events if e.get("state") == "DRAFTED"}
    sent: dict[str, dict[str, Any]] = {}
    for e in events:
        if e.get("state") == "SENT" and _stamp(e.get("utc")) and (now - _stamp(e["utc"])).total_seconds() <= window_h * 3600:
            sent[e["id"]] = e
    if not sent:
        return []
    oldest = min(_stamp(e["utc"]) for e in sent.values()) - dt.timedelta(minutes=5)
    rows = {i: {"id": i, "recipient": (drafted.get(i) or {}).get("recipient", ""), "sent_utc": e["utc"], "taken_utc": None, "taken_in": None, "output_utc": None, "output": None,
                "expect_hours": float((drafted.get(i) or {}).get("expect_hours") or FLOW_NO_OUTPUT_H)} for i, e in sent.items()}
    rx = {i: _flow_rx(i) for i in rows}
    for path in sorted((ROOT / "ledger" / "tasks").glob("*/*.json")):
        try:
            text = path.read_text(encoding="utf-8")
            hit = [i for i in rows if rx[i].search(text)]
            if not hit:
                continue
            rec = json.loads(text)
            if not isinstance(rec, dict) or any(m in str(rec.get("TASK_ID", "")) for m in SENDER_RECORDS):
                continue

            def walk(o):
                if isinstance(o, dict):
                    own = json.dumps({k: v for k, v in o.items() if not isinstance(v, (dict, list))}, ensure_ascii=False)
                    for i in hit:
                        if rx[i].search(own):
                            at = _stamp(o.get("accepted_at")) or _stamp(o.get("updated_at"))        # the time the recipient took it: accepted_at when the step has one, never a later update of the same step
                            if at and at >= _stamp(rows[i]["sent_utc"]) - dt.timedelta(minutes=5) and (rows[i]["taken_utc"] is None or at < _stamp(rows[i]["taken_utc"])):
                                rows[i]["taken_utc"], rows[i]["taken_in"] = _utc(at), str(rec.get("TASK_ID"))
                    for v in o.values():
                        walk(v)
                elif isinstance(o, list):
                    for v in o:
                        walk(v)
            walk(rec)
        except (OSError, ValueError):
            continue
    ref = ref or observed_ref(fetch=False, now=now)["ref"]
    log = _git("log", ref, f"--since={oldest.strftime('%Y-%m-%dT%H:%M:%SZ')}", "--name-status", "--format=%x01%cI%x09%h%x09%s")
    for chunk in (log or "").split("\x01")[1:]:
        head, _, body = chunk.partition("\n")
        when, _, rest = head.partition("\t")
        sha, _, subject = rest.partition("\t")
        at = _stamp(when)
        if re.match(r"\s*ADV\b", subject):
            continue          # the presidio's own commits (registering and sending an assignment) are the SEND, not the recipient's output
        names = [ln.split("\t", 1)[1] for ln in body.splitlines() if ln.startswith("A\t") and "\t" in ln and "/assignments/" not in ln and "/meetings/" not in ln]
        for i, row in rows.items():
            if at is None or at < _stamp(row["sent_utc"]):
                continue
            what = subject if rx[i].search(subject) else next((n for n in names if rx[i].search(n)), None)
            if what and (row["output_utc"] is None or at < _stamp(row["output_utc"])):
                row["output_utc"], row["output"] = _utc(at), f"{sha} {what[:90]}"
            # the first one AFTER the recipient's record took it: a checkpoint that merely names the id as next work comes earlier and is not the work (ADV-101: named at +3 min, first work at +18)
            if what and row["taken_utc"] and at >= _stamp(row["taken_utc"]) and (row.get("output_after_take_utc") is None or at < _stamp(row["output_after_take_utc"])):
                row["output_after_take_utc"], row["output_after_take"] = _utc(at), f"{sha} {what[:90]}"
    # 2026-11-25 (ADV-226): the result was in a record and in the assignment file, which is not "output" here, and the line kept saying 'no output' for hours about work already DONE.
    executed = {i for i, state in assignment_states(campaign).items() if "EXECUTED" in state["levels"]}
    out = []
    for i, row in sorted(rows.items()):
        sent_at = _stamp(row["sent_utc"])
        age = round((now - sent_at).total_seconds() / 60)
        row["sent_age_min"] = age
        flag = ""
        if age > FLOW_FLAG_H * 60:
            pass          # older than the flag window: listed by `status`, not raised again (a historical gap is not today's prompt)
        elif row["taken_utc"] is None and row["output_utc"] is None and age > FLOW_NOT_TAKEN_MIN:
            flag = f"SENT, NOT TAKEN after {age} min"
        elif row["output_utc"] is None and row["taken_utc"] is not None and i not in executed:
            held = (now - _stamp(row["taken_utc"])).total_seconds() / 3600
            if held > row["expect_hours"]:
                flag = f"TAKEN, no output after {round(held, 1)} h"
        row["flag"] = flag
        out.append(row)
    return out


def flow_line(row: dict[str, Any]) -> str:
    def age(a, b):
        x, y = _stamp(a), _stamp(b)
        return f"{round((y - x).total_seconds() / 60)} min" if x and y else "?"
    parts = [f"{row['id']} [{row['recipient']}] SENT {row['sent_utc'][11:16]}Z"]
    parts.append(f"TAKEN {row['taken_utc'][11:16]}Z (+{age(row['sent_utc'], row['taken_utc'])}, {row['taken_in']})" if row["taken_utc"] else "not taken")
    parts.append(f"FIRST NAMED IN A COMMIT {row['output_utc'][11:16]}Z (+{age(row['sent_utc'], row['output_utc'])}: {row['output']})" if row["output_utc"] else "no output yet")
    if row.get("output_after_take_utc") and row["output_after_take_utc"] != row["output_utc"]:
        parts.append(f"FIRST OUTPUT AFTER TAKEN {row['output_after_take_utc'][11:16]}Z (+{age(row['sent_utc'], row['output_after_take_utc'])}: {row['output_after_take']})")
    return " -> ".join(parts) + (f"  ** {row['flag']}" if row["flag"] else "")


# ---------------------------------------------------------------- scientific rotation, daily reconciliation, DREAM (cross_session_transport.md section 14)
META_STATES = ("STRAND", "RECONCILED", "DREAM", "ROTATION_DEFERRED")   # events of the assignment log that are not assignments: the log stays the one durable record, no second register
ROTATION_RUN = 3                  # the operator's initial cadence: three substantial scientific increments in one strand make a rotation due (2026-11-20); a constant, not a limit on activity
DREAM_WINDOW_H = 72
UNCLASSIFIED_WINDOW_H = 24
DREAM_RULE_FROM = "2026-11-20T12:30:00Z"          # a dream pass is owed by increments concluded after the rule exists; the older ones, reconstructed for the count, are not a debt
ROME = ZoneInfo("Europe/Rome")
NOT_SCIENTIFIC = ("harness", "none", "editorial")


def _strands(campaign: Path) -> dict[str, dict[str, Any]]:
    """Per id, the strand an increment belongs to: the optional `strand:` line of its assignment, overridden by a later STRAND event. A STRAND event for an id that is not an assignment records a concluded increment
    done outside the assignment channel (a self-directed comparison), with the time `at` it concluded and its `basis` (a commit or record). `counts_with` folds an increment into another one (producer, verifier and
    integration of one result are one increment)."""
    out: dict[str, dict[str, Any]] = {}
    for e in _events(campaign):
        if e.get("state") == "DRAFTED" and e.get("strand"):
            out[e["id"]] = {"strand": e["strand"], "outside": False, "at": "", "counts_with": "", "basis": "assignment"}
        elif e.get("state") == "STRAND" and e.get("id"):
            prev = out.get(e["id"], {})
            drafted = prev.get("outside") is False or any(x.get("id") == e["id"] and x.get("state") == "DRAFTED" for x in _events(campaign))
            out[e["id"]] = {"strand": e.get("strand", prev.get("strand", "")), "outside": not drafted, "at": e.get("at", prev.get("at", "")), "counts_with": e.get("counts_with", prev.get("counts_with", "")),
                            "basis": e.get("basis", prev.get("basis", ""))}
    return out


def done_times(ids: set[str]) -> dict[str, str]:
    """When a recipient marked a step naming each id DONE (that step's `updated_at`): the time the assignment concluded, which is later than the time it was sent. One read of the task records."""
    out: dict[str, str] = {}
    if not ids:
        return out
    for path in sorted((ROOT / "ledger" / "tasks").glob("*/*.json")):
        if any(tag in path.name for tag in SENDER_RECORDS):
            continue
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue

        def walk(o):
            if isinstance(o, dict):
                if str(o.get("status", "")).upper() == "DONE" and o.get("updated_at"):
                    own = json.dumps({k: v for k, v in o.items() if not isinstance(v, (dict, list))}, ensure_ascii=False)
                    for i in ids:
                        if i in own and (i not in out or str(o["updated_at"]) < out[i]):
                            out[i] = str(o["updated_at"])
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(rec)
    return out


def increments(campaign: Path) -> list[dict[str, Any]]:
    """The substantial scientific increments, in the order they concluded. Counted: an assignment that carries a strand and whose recipient took it to DONE (the tick's EXECUTED level), or an outside increment
    recorded with its time. Not counted: harness, editorial and unclassified work, commits, messages, and an increment folded into another by `counts_with`. A negative or inconclusive result that narrowed a
    question counts; classifying that is the host's reading, recorded with its basis."""
    smap, states = _strands(campaign), assignment_states(campaign)
    sent = {}
    for e in _events(campaign):
        if e.get("state") == "SENT" and e.get("id") and e["id"] not in sent:
            sent[e["id"]] = e.get("utc", "")
    done = done_times({i for i, m in smap.items() if not m["outside"] and not m["at"]})
    out = []
    for ident, m in smap.items():
        if not m["strand"] or m["strand"].lower() in NOT_SCIENTIFIC or m["counts_with"]:
            continue
        if m["outside"]:
            at = m["at"]
        else:
            at = (m["at"] or done.get(ident) or sent.get(ident, "")) if "EXECUTED" in states.get(ident, {}).get("levels", []) else ""   # when the host recorded it, else when the recipient marked it DONE, else the send time
        if at:
            out.append({"id": ident, "strand": m["strand"], "at": at, "basis": m["basis"]})
    return sorted(out, key=lambda r: r["at"])


def rotation_status(campaign: Path) -> dict[str, Any]:
    """Scientific rotation: after ROTATION_RUN consecutive concluded increments in the same strand, the next scientific assignment goes to another strand. Derived from the assignment log, never stored; work already
    in flight keeps its priority, and an open assignment in another strand is the rotation already under way (no second one is drafted). A deferral is recorded with its reason and resume point and stays visible."""
    incs = increments(campaign)
    smap, states = _strands(campaign), assignment_states(campaign)
    if not incs:
        return {"state": "NO_DATA", "run": 0, "strand": "", "ids": [], "open_other": [], "deferred": None, "unclassified": [], "line": "SCIENTIFIC ROTATION: no classified increment yet (record `strand` for the recent ones)"}
    strand = incs[-1]["strand"]
    full = []
    for r in reversed(incs):
        if r["strand"] != strand:
            break
        full.append(r)
    full.reverse()
    run = [r["id"] for r in full]
    # a rotation is an assignment drafted once the threshold was reached (at the conclusion of the ROTATION_RUN-th increment of the run), not an old assignment still open in another strand
    threshold = full[ROTATION_RUN - 1]["at"] if len(full) >= ROTATION_RUN else ""
    drafted_at = {e["id"]: e.get("utc", "") for e in _events(campaign) if e.get("state") == "DRAFTED"}
    open_all = [i for i, m in smap.items() if not m["outside"] and m["strand"] and m["strand"].lower() not in NOT_SCIENTIFIC and "EXECUTED" not in states.get(i, {}).get("levels", []) and i in states
                and (not threshold or drafted_at.get(i, "") >= threshold)]
    open_other = [i for i in open_all if smap[i]["strand"] != strand]
    open_same = [i for i in open_all if smap[i]["strand"] == strand]
    deferred = next((e for e in reversed(_events(campaign)) if e.get("state") == "ROTATION_DEFERRED"), None)
    if deferred and incs and (deferred.get("utc", "") < incs[-1]["at"] and incs[-1]["strand"] != deferred.get("strand")):
        deferred = None                      # a later increment in another strand ended the deferral
    cutoff = _now() - dt.timedelta(hours=UNCLASSIFIED_WINDOW_H)
    sent = {e["id"]: e.get("utc", "") for e in _events(campaign) if e.get("state") == "SENT" and e.get("id")}
    unclassified = sorted(i for i, v in states.items() if "EXECUTED" in v["levels"] and i not in smap and (v.get("recipient") or "").lower() != "harness" and _stamp(sent.get(i)) and _stamp(sent[i]) >= cutoff)
    if len(run) >= ROTATION_RUN and open_other:
        state, line = "IN_PROGRESS", f"SCIENTIFIC ROTATION IN PROGRESS: {', '.join(open_other)} open in another strand than '{strand}' ({len(run)} consecutive increments there); draft no second rotation assignment"
    elif len(run) >= ROTATION_RUN and deferred:
        state, line = "DEFERRED", f"SCIENTIFIC ROTATION DEFERRED ({deferred.get('utc', '')[:16]}Z): {deferred.get('reason', '')}; resume {deferred.get('resume', '')}; still due: {len(run)} consecutive increments in '{strand}'"
    elif len(run) >= ROTATION_RUN:
        state = "DUE"
        line = (f"SCIENTIFIC ROTATION DUE: the last {len(run)} concluded scientific increments are all in strand '{strand}' ({', '.join(run[-5:])}); the next scientific assignment available goes to another "
                f"opportunity of the roadmap (a different strand or group of candidates, a neglected row, a candidate reopened for a documented reason, or a question that widens the comparison; not another compound in the same "
                f"question). Work already in flight keeps priority; a concrete urgency may defer it with `rotation --defer --reason ... --resume ...` (no approval)"
                + (f". Open in the same strand: {', '.join(open_same)}" if open_same else ""))
    else:
        state, line = "OK", f"scientific rotation: {len(run)}/{ROTATION_RUN} consecutive increments in strand '{strand}'" + (f"; open in another strand: {', '.join(open_other)}" if open_other else "")
    if unclassified:
        line += f"; UNCLASSIFIED executed assignments of the last {UNCLASSIFIED_WINDOW_H} h (not counted: record `strand`): {', '.join(unclassified[:4])}" + (f" and {len(unclassified) - 4} more" if len(unclassified) > 4 else "")
    return {"state": state, "run": len(run), "strand": strand, "ids": run, "open_other": open_other, "open_same": open_same, "deferred": deferred, "unclassified": unclassified, "line": line}


def dream_pending(campaign: Path, now: dt.datetime | None = None) -> list[str]:
    """Concluded scientific increments of the last DREAM_WINDOW_H hours with no DREAM line: the existing dream pass (legend-dream) runs after a significant result and its outcome, connections or an
    explained absence, is recorded with `dream`. Visible, never a block; whether the result was significant is the host's reading (`dream --none` says so)."""
    now = now or _now()
    done = {i for e in _events(campaign) if e.get("state") == "DREAM" for i in (e.get("ids") or [])}
    for path in sorted((ROOT / "ledger" / "tasks").glob("advisor/*.json")):           # a dated `dream` line of the host's standing record that names the delivery counts too (the host attested one on 2026-11-20)
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for e in (rec.get("DAILY_RECONCILIATION") or []) if isinstance(rec, dict) else []:
            if isinstance(e, dict) and e.get("dream"):
                done |= set(re.findall(r"\b[A-Z][A-Za-z0-9]*-[A-Za-z0-9-]+\b", str(e["dream"])))
    return [r["id"] for r in increments(campaign) if r["id"] not in done and r["at"] >= DREAM_RULE_FROM and _stamp(r["at"]) and (now - _stamp(r["at"])).total_seconds() <= DREAM_WINDOW_H * 3600]


def rome_day(now: dt.datetime) -> str:
    return now.astimezone(ROME).date().isoformat()


def reconcile_findings(campaign: Path, now: dt.datetime | None = None) -> list[dict[str, str]]:
    """Candidate incoherences between the portfolio and what happened, for the daily reconciliation. A candidate is a place to look, not a verdict: the owner of the row decides. Read only; never rewrites a row."""
    now = now or _now()
    snap, states = portfolio_snapshot(), assignment_states(campaign)
    out = []
    for r in snap["items"]:
        status, text = r.get("status", "").lower(), " ".join(r.get(k, "") for k in ("next_action", "mandate_id", "resume_when"))
        named = sorted(set(re.findall(r"\bADV-\d{3}\b", text)))
        concluded = [i for i in named if "EXECUTED" in states.get(i, {}).get("levels", [])]
        if r["review_due"]:
            out.append({"id": r["id"], "why": f"{status} row whose linked mandate {r.get('mandate_id')} is RELEASED: the result is to be reviewed", "owner": "ADV"})
        if status in ("assigned", "ready") and named and len(concluded) == len(named):
            out.append({"id": r["id"], "why": f"{status} row names {', '.join(named)}, all concluded (a DONE step carries each id): close, supersede or update it", "owner": states[named[0]].get("recipient", "ADV")})
        elif status in ("waiting", "parked") and r.get("dependency_met"):
            out.append({"id": r["id"], "why": f"{status} row whose typed resume condition is met ({r['dependency_met'][:80]}): reopen or update it", "owner": "ADV"})
        elif status in ("waiting", "parked") and named and len(concluded) == len(named):
            out.append({"id": r["id"], "why": f"{status} row waits on {', '.join(named)}, already concluded: the event happened", "owner": states[named[0]].get("recipient", "ADV")})
    # ready rows named by an assignment drafted after the row's last update, and backlog rows named in a recent delivery (commit subject): the two places where a row goes stale without anyone editing it
    named_by: dict[str, list[tuple[str, str]]] = {}
    for e in _events(campaign):
        if e.get("state") == "DRAFTED" and e.get("id"):
            f = Path(campaign) / "assignments" / f"{e['id']}.md"
            for rid in set(re.findall(r"\bRP-\d{3}\b", f.read_text(encoding="utf-8", errors="replace") if f.exists() else "")):
                named_by.setdefault(rid, []).append((e["id"], e.get("utc", "")))
    recent = _git("log", "HEAD", f"--since={_utc(now - dt.timedelta(hours=DREAM_WINDOW_H))}", "--format=%h %s")
    seen = {c["id"] for c in out}
    for r in snap["items"]:
        status = r.get("status", "").lower()
        if r["id"] in seen:
            continue
        later = [a for a, at in named_by.get(r["id"], []) if at > r.get("updated_utc", "")]
        if status == "ready" and later:
            out.append({"id": r["id"], "why": f"ready row named by {', '.join(later[:3])}, drafted after the row's last update: consumed, superseded or still ready?", "owner": "ADV"})
        elif status == "backlog":
            hit = [ln for ln in recent.splitlines() if re.search(rf"\b{re.escape(r['id'])}\b", ln)]
            if hit:
                out.append({"id": r["id"], "why": f"backlog row named in a recent delivery ({hit[0][:70]}): does the result change it?", "owner": "ADV"})
    # a DREAM connection carried to a portfolio row that the row has not absorbed yet (the row was last updated before the connection was recorded): the association must reach its consumer to count
    rows = {r["id"]: r for r in snap["items"]}
    seen = {c["id"] for c in out}
    for e in _events(campaign):
        if e.get("state") != "DREAM":
            continue
        for c in e.get("connections") or []:
            row = rows.get(c.get("to", ""))
            if row and row["id"] not in seen and row.get("updated_utc", "") < e.get("utc", ""):
                out.append({"id": row["id"], "why": f"DREAM connection from {', '.join(e.get('ids') or [])} not yet absorbed by this row (last updated before it): {c.get('what', '')[:90]}", "owner": "ADV"})
                seen.add(row["id"])
    return out


def attestations(campaign: Path) -> list[dict[str, Any]]:
    """Every daily reconciliation attestation, from the two places it may be written, in one shape: a `RECONCILED` line of the assignment log (`reconcile --attest`) and an entry of `DAILY_RECONCILIATION` in
    the host's standing record (`ledger/tasks/advisor/*.json`, where the ADV host attested on 2026-11-20). Reading both means whichever the host used counts; nothing is copied from one to the other."""
    out = [{"rome_date": e.get("rome_date", ""), "result": e.get("result", ""), "residual": e.get("residual") or [], "source": "assignment log"} for e in _events(campaign) if e.get("state") == "RECONCILED"]
    for path in sorted((ROOT / "ledger" / "tasks").glob("advisor/*.json")):
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for e in (rec.get("DAILY_RECONCILIATION") or []) if isinstance(rec, dict) else []:
            if isinstance(e, dict) and e.get("day_europe_rome"):
                out.append({"rome_date": e["day_europe_rome"], "result": str(e.get("kind", "")),
                            "residual": [{"id": x.get("row", x.get("id", "")), "owner": x.get("owner", "")} for x in (e.get("residual_inconsistencies") or []) if isinstance(x, dict)], "source": "standing record"})
    return sorted(out, key=lambda a: a["rome_date"])


def reconcile_state(campaign: Path, now: dt.datetime | None = None) -> dict[str, Any]:
    now = now or _now()
    today = rome_day(now)
    done = attestations(campaign)
    last = done[-1] if done else None
    due = not any(e.get("rome_date") == today for e in done)
    residual = (last or {}).get("residual") or []
    line = (f"PORTFOLIO RECONCILIATION DUE (Europe/Rome {today}): none attested today; `strategic_advisor.py reconcile --campaign ...` lists candidate incoherences, correct what is yours, then `--attest`" if due else
            f"portfolio reconciled {today} ({last['result']}, in the {last['source']})") + (f"; RESIDUAL INCOHERENCES: " + "; ".join(f"{x.get('id')} ({x.get('owner')})" for x in residual[:6]) if residual else "")
    return {"due": due, "today": today, "last": last, "line": line}


def attest_reconciliation(campaign: Path, result: str, changed: list[str], residual: list[str], note: str = "", now: dt.datetime | None = None) -> dict[str, Any]:
    """Nothing here refuses: an incomplete attestation is recorded with its warnings, visible and recoverable."""
    now = now or _now()
    warn = []
    if result not in ("NO_CHANGE", "CHANGED"):
        warn.append(f"result {result!r} is not NO_CHANGE or CHANGED: recorded as given")
    ids = {r["id"] for r in portfolio_rows()[0]}
    bad = [c for c in changed if c not in ids]
    if bad:
        warn.append("not portfolio ids (recorded as given): " + ", ".join(bad))
    if result == "CHANGED" and not changed:
        warn.append("CHANGED names no corrected row")
    res = []
    for x in residual:
        rid, _, owner = x.partition(":")
        res.append({"id": rid.strip(), "owner": owner.strip() or "ADV"})
    row = {"state": "RECONCILED", "rome_date": rome_day(now), "result": result if not res else result + "+RESIDUAL", "changed": changed, "residual": res, "note": note}
    _log_assignment(campaign, row)
    return {**row, "warnings": warn}


def record_strand(campaign: Path, ident: str, strand: str, basis: str, at: str = "", counts_with: str = "") -> dict[str, Any]:
    """Nothing here refuses: a missing basis or time is recorded as such and reported."""
    warn = []
    if not basis:
        warn.append("no --basis (the commit or record showing it concluded): recorded without one")
    known = {e.get("id") for e in _events(campaign) if e.get("state") == "DRAFTED"}
    if ident not in known and not at:
        at = _utc(_now())
        warn.append(f"{ident} is not an assignment and no --at was given: the time recorded is now ({at}); correct it with a later STRAND line if it concluded earlier")
    row = {"state": "STRAND", "id": ident, "strand": strand, "basis": basis, **({"at": at} if at else {}), **({"counts_with": counts_with} if counts_with else {})}
    _log_assignment(campaign, row)
    return {**row, "warnings": warn}


def record_dream(campaign: Path, ids: list[str], connections: list[tuple[str, str]], none_reason: str, counter: str = "") -> dict[str, Any]:
    """The outcome of the dream pass after a significant result: where each useful connection was carried (a consumer that exists: a portfolio row, an assignment, a file), whether contrary results, a context
    mismatch, a reusable control or an avoidable duplicate were considered, or why there is no connection. Warnings are returned, nothing is refused: an incomplete line is visible, not a block."""
    warn = []
    if not ids:
        warn.append("no --id: the line names no increment, so it closes nothing")
    if not connections and not none_reason:
        warn.append("neither a connection (--to, --what) nor --none REASON: recorded as an unexplained empty pass")
    portfolio_ids = {r["id"] for r in portfolio_rows()[0]}
    assignment_ids = {e.get("id") for e in _events(campaign) if e.get("state") == "DRAFTED"}
    for consumer, _what in connections:
        if consumer not in portfolio_ids and consumer not in assignment_ids and not (ROOT / consumer).exists():
            warn.append(f"consumer {consumer!r} is not an accepted form (a portfolio row id such as RP-005, an assignment id such as ADV-109, or an existing repository path): a connection nobody reads is not recovered")
    if connections and not counter:
        warn.append("no --counter: say whether contrary results, a context mismatch, a reusable control or an avoidable duplicate were considered")
    row = {"state": "DREAM", "ids": ids, "connections": [{"to": c, "what": w} for c, w in connections], "none_reason": none_reason, "counter": counter}
    _log_assignment(campaign, row)
    return {**row, "warnings": warn}


def defer_rotation(campaign: Path, reason: str, resume: str) -> dict[str, Any]:
    warn = ["no --reason" if not reason else "", "no --resume point" if not resume else ""]
    row = {"state": "ROTATION_DEFERRED", "reason": reason, "resume": resume, "strand": rotation_status(campaign).get("strand", "")}
    _log_assignment(campaign, row)
    return {**row, "warnings": [w for w in warn if w]}


CI_CHECK_MIN = 30


def ci_main_line(state: dict[str, Any], now: dt.datetime | None = None) -> str:
    """One line when the latest completed publication-gate run on main is red, with the run that began the unbroken red streak (ADV-108, 2026-11-20: red for ~40 commits and ~7 hours, found by a person).
    One request of the public API at most every CI_CHECK_MIN minutes (the answer is kept in the tick state and repeated meanwhile); a rate limit, a network failure or no GitHub remote is silent, never read as
    green. The local publication gate does not run the regression suites, so a green `safe_push` says nothing about this line."""
    now = now or _now()
    last = _stamp(state.get("ci_main_checked_utc"))
    if last and (now - last).total_seconds() < CI_CHECK_MIN * 60:
        return state.get("ci_main_line", "")
    state["ci_main_checked_utc"] = _utc(now)
    line = ""
    try:
        import ci_runs
        recent = ci_runs.fetch_recent(ci_runs.slug("development", ROOT))
        res = ci_runs.red_streak(recent)
        if res.get("red"):
            line = (f"CI RED ON MAIN: the latest completed run #{res['latest']} ({res['latest_sha']}) is {res['conclusion']}; red since #{res['first_red']} ({res['first_red_sha']}), {res['streak']} run(s) in a row "
                    f"(the local gate does not run the regression suites; `ci_runs.py status <sha>`, annotations of the check run list the failing suites)")
    except (Exception, SystemExit):  # noqa: BLE001 — unreadable is not green and not red: say nothing
        line = state.get("ci_main_line", "")
    state["ci_main_line"] = line
    return line


def discipline_lines(campaign: Path) -> list[str]:
    """The three recall lines of the standing method (rotation, daily reconciliation, DREAM), for the tick and `status`."""
    lines = []
    rot = rotation_status(campaign)
    if rot["state"] != "OK" or rot["unclassified"]:
        lines.append(rot["line"])
    rec = reconcile_state(campaign)
    if rec["due"] or (rec["last"] or {}).get("residual"):
        lines.append(rec["line"])
    dp = dream_pending(campaign)
    if dp:
        lines.append(f"DREAM PENDING for concluded increment(s) of the last {DREAM_WINDOW_H} h: {', '.join(dp[:8])} (legend-dream pass, then `dream --id ... --to CONSUMER --what ... --counter ...` or `--none REASON`)")
    return lines



def status(campaign: Path) -> str:
    campaign = Path(campaign)
    b = _budget(campaign)
    att = _attempts(campaign)
    n = len({(a["stage"], a["index"]) for a in att})
    cont = continuous(campaign)
    drafted = len([1 for e in _events(campaign) if e['state'] == 'DRAFTED'])
    lines = [f"campaign {campaign.name}: activated {b.get('activated_utc', '-')}, pilot expiry {b.get('expires_utc', '-')}{' (historical)' if cont else ''}, pilot invocations {n}/{b.get('max_invocations', '-')}, "
             f"assignments drafted {drafted}/{b.get('max_assignments', '-')}, {'DISABLED' if (campaign / 'DISABLED').exists() else 'enabled'}"]
    if cont:
        since = [a for a in {(a['stage'], a['index']): a for a in att if a.get('started_utc', '') >= cont['authorised_utc']}.values()]
        week = weekly_state(campaign)
        held = advisor_suspension(campaign)
        lines.append(f"  mode CONTINUOUS since {cont['authorised_utc']} ({cont.get('source', 'source not stated')}): {len(since)} evaluation(s) since; the pilot ceilings above were executed "
                     f"{n}/{b.get('max_invocations', '-')} and {drafted}/{b.get('max_assignments', '-')} and are history, not the rule of this mode; "
                     f"{'SUSPENDED: ' + held if held else 'no operator suspension'}; weekly allocation {week['state']} (measured 7 d: {week['measured_7d']['evaluations']} evaluation(s), "
                     f"{week['measured_7d']['output_tokens']} output, {week['measured_7d']['cache_read_tokens']} cache-read tokens)" + ("" if week["state"] != "unset" else "; " + week["note"]))
        lines.append("  Measurement scope: " + week["measurement_scope"])
    held = _holds(campaign)
    if held:
        last = held[-1]
        lines.append(f"  holds recorded {len(held)} (not evaluations, not counted above); last {last['utc']}: cleared {len(last['events_cleared'])} event(s) and {last['commits_cleared']} commit(s), resume_when {last['resume_when']}: {last['reason'][:160]}")
    for row in assignment_flow(campaign):
        lines.append("  flow " + flow_line(row))
    for ln in discipline_lines(campaign):
        lines.append("  " + ln)
    for ident, v in sorted(assignment_states(campaign).items()):
        lines.append(f"  {ident} [{v['recipient']}] {v['key']}: highest evidence {v['highest'] or 'none'}; origin {v.get('origin', 'assessment')}; levels {','.join(v['levels'])}" + ("; UNREACHABLE (residual stays in the queue)" if v["unreachable"] else ""))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("entrypoints")
    sub.add_parser("snapshot")
    pf = sub.add_parser("portfolio", help="read the permanent work portfolio, or merge one opportunity from a JSON object")
    pf.add_argument("--upsert", metavar="FILE.json", help="patch by stable id; other fields are preserved")
    pf.add_argument("--id", help="read one complete opportunity")
    pf.add_argument("--json", action="store_true", help="read all rows and their derived execution states")
    s = sub.add_parser("seal"); s.add_argument("--campaign", required=True); s.add_argument("--index", required=True); s.add_argument("--text-file", required=True)
    b = sub.add_parser("brief"); b.add_argument("--stage", choices=["A", "B"], required=True); b.add_argument("--campaign", required=True)
    b.add_argument("--mission-file"); b.add_argument("--constraints-file"); b.add_argument("--task-record", default="")
    b.add_argument("--assessment"); b.add_argument("--sealed-intended"); b.add_argument("--out")
    b.add_argument("--expect", action="append", default=[], metavar="REF[:PATH]", help="a delivery the mission text announces (SHA or ref, optionally the folder it adds); the brief states whether it is in this snapshot and reachable")
    r = sub.add_parser("run"); r.add_argument("--stage", choices=["A", "B", "S", "P"], required=True); r.add_argument("--campaign", required=True)
    r.add_argument("--brief", required=True); r.add_argument("--model", required=True); r.add_argument("--effort", required=True, choices=["low", "medium", "high"])
    r.add_argument("--timeout", type=int, default=3600)
    r.add_argument("--extra-attempt", default="", help="reason; allows one recorded attempt beyond the ceiling when every earlier attempt of the stage failed")
    e = sub.add_parser("extract"); e.add_argument("--transcript", required=True); e.add_argument("--out", required=True)
    c = sub.add_parser("check"); c.add_argument("--campaign", required=True)
    rf = sub.add_parser("refresh", help="fast-forward this campaign home to development/main without losing a local byte; refuses, changing nothing, while a local change is not on main"); rf.add_argument("--campaign", required=True)
    t = sub.add_parser("tick", help="the hourly bounded check (no model unless you then run `evaluate`)"); t.add_argument("--campaign", required=True)
    ev = sub.add_parser("evaluate", help="one strategic evaluation, counted in the campaign budget"); ev.add_argument("--campaign", required=True)
    ha = sub.add_parser("assign", help="register the continuous ADV host's decision in the existing assignment channel, without a consultant call or a send")
    ha.add_argument("--campaign", required=True); ha.add_argument("--text-file", required=True, help="existing ASSIGNMENT blocks; preserve original premises and recipient autonomy")
    hd = sub.add_parser("hold", help="record a hold without a model run: consumes the pending digest, lists what it clears in holds.jsonl, is not an evaluation"); hd.add_argument("--campaign", required=True); hd.add_argument("--reason", required=True); hd.add_argument("--resume-when", required=True, help="record:<TASK>=<STATE> or path:<file>[~<text>]"); hd.add_argument("--excluded", required=True, help="the paths the hold leaves out (record ids, portfolio rows, files) with the actual cause of each; a hold lapses at min_hours_between")
    ev.add_argument("--model", default="opus"); ev.add_argument("--effort", default="high", choices=["low", "medium", "high"]); ev.add_argument("--timeout", type=int, default=3600)
    st = sub.add_parser("status", help="budget and the evidence level of every assignment"); st.add_argument("--campaign", required=True)
    sd = sub.add_parser("strand", help="record which strand a concluded scientific increment belongs to (scientific rotation): an assignment id, or an outside increment with --at")
    sd.add_argument("--campaign", required=True); sd.add_argument("--id", required=True); sd.add_argument("--strand", required=True); sd.add_argument("--basis", required=True, help="the commit or record showing it concluded")
    sd.add_argument("--at", default="", help="UTC time it concluded (needed for an increment that is not an assignment)"); sd.add_argument("--counts-with", default="", help="fold this increment into another id (one result, not two increments)")
    ro = sub.add_parser("rotation", help="scientific rotation status, or record a deferral with its reason and resume point")
    ro.add_argument("--campaign", required=True); ro.add_argument("--defer", action="store_true"); ro.add_argument("--reason", default=""); ro.add_argument("--resume", default="")
    rc2 = sub.add_parser("reconcile", help="daily portfolio reconciliation: list candidate incoherences (read only), or attest the day's check")
    rc2.add_argument("--campaign", required=True); rc2.add_argument("--attest", choices=["NO_CHANGE", "CHANGED"]); rc2.add_argument("--changed", action="append", default=[], help="portfolio id corrected (repeat)")
    rc2.add_argument("--residual", action="append", default=[], help="ID:OWNER of an incoherence left open (repeat)"); rc2.add_argument("--note", default="")
    dm = sub.add_parser("dream", help="record the outcome of the dream pass after a significant result: connections carried to a consumer, or why there is none")
    dm.add_argument("--campaign", required=True); dm.add_argument("--id", action="append", default=[], help="the increment(s) followed (repeat)")
    dm.add_argument("--to", action="append", default=[], help="consumer: a portfolio row, an assignment id or a repository path (repeat; pair with --what)"); dm.add_argument("--what", action="append", default=[])
    dm.add_argument("--none", default="", help="no useful connection: the reason"); dm.add_argument("--counter", default="", help="contrary results, context mismatch, reusable control or avoidable duplicate considered")
    mt = sub.add_parser("meeting", help="six-hour/event alignment through the existing host; status unless one action is supplied")
    mt.add_argument("--campaign", required=True)
    action = mt.add_mutually_exclusive_group()
    action.add_argument("--request", help="why a material event needs cross-role coordination")
    action.add_argument("--open", action="store_true", help="open the due round table, or return the existing one")
    action.add_argument("--close", metavar="NOTES.md", help="close with actual replies/decisions from this file, saved verbatim")
    mt.add_argument("--source", default="", help="durable original/event pointer for a request")
    mt.add_argument("--actor", choices=MEETING_ROLES, default="", help="requesting participant role, not a new actor identity")
    dl = sub.add_parser("deliver", help="record what the channel did with an assignment (SENT with the message id, or UNREACHABLE with the reason)"); dl.add_argument("--campaign", required=True)
    dl.add_argument("--id", required=True); dl.add_argument("--state", choices=["SENT", "UNREACHABLE"], required=True); dl.add_argument("--evidence", required=True)
    dl.add_argument("--receipt", action="append", default=[], help="SENT only: the send's own receipt id (the msg_id SendMessage returned, a UUID), one per real send; or put it inside --evidence")
    dl.add_argument("--to", action="append", default=[], help="SENT only: the session the transport receipt names, one per real send (an assignment's own recipient must be among them)")
    ac = sub.add_parser("activate", help="write the campaign budget (24 h by default, no renewal)"); ac.add_argument("--campaign", required=True)
    ac.add_argument("--hours", type=int, default=24); ac.add_argument("--max-invocations", type=int, default=3); ac.add_argument("--max-assignments", type=int, default=3)
    ac.add_argument("--turn-limit", type=int, default=20); ac.add_argument("--recipient", action="append", default=[], help="role=session name, e.g. Orchestrator='IT Orchestrator'")
    rc = sub.add_parser("recall", help="print the one canonical text of the hourly recall (what to pass to CronCreate when restoring it); CronList first, so there is one copy only"); rc.add_argument("--campaign", required=True)
    ra = sub.add_parser("recall-armed", help="record that the host armed (or renewed) the one in-session recall just now: a session cron expires after 7 days, so the tick warns from day 5; run it right after CronCreate")
    ra.add_argument("--campaign", required=True); ra.add_argument("--job-id", default="", help="the job id CronCreate returned")
    ec = sub.add_parser("authorise-continuous", help="record the operator's persistent authorisation to continue inside the roadmap (a mode of this campaign: budget, counters and history are untouched; `end-continuous` returns to the bounded pilot)")
    ec.add_argument("--campaign", required=True); ec.add_argument("--source", required=True, help="where the operator's authorisation is recorded (the Operator roadmap line)")
    ec.add_argument("--min-hours-between", type=float, default=4.0); ec.add_argument("--min-hours-anticipating", type=float, default=1.0)
    ec.add_argument("--weekly-limit", type=float, help="the shared usable weekly limit in --unit, only when the operator has stated it"); ec.add_argument("--advisor-share", type=float, help="the Advisor's fraction of it, 0-1")
    ec.add_argument("--unit", choices=ALLOCATION_UNITS)
    en = sub.add_parser("end-continuous", help="end the continuous mode (history kept); the campaign then follows its bounded pilot rules"); en.add_argument("--campaign", required=True); en.add_argument("--reason", required=True)
    dis = sub.add_parser("disable", help="stop the pilot: later ticks and runs refuse; ordinary scheduling and the sessions' work continue"); dis.add_argument("--campaign", required=True)
    args = ap.parse_args(argv)

    if args.cmd == "entrypoints":
        print(render_entrypoints(entrypoints())); return 0
    if args.cmd == "snapshot":
        print(json.dumps(snapshot(), indent=2)); return 0
    if args.cmd == "portfolio":
        if args.upsert:
            # 2026-11-20 (ADV, HE meeting item): no primary-checkout refusal here. The refusal protects the campaign state (budget, invocations, assignments); `portfolio_update` touches only the portfolio TSV
            # of THIS checkout (ROOT / PORTFOLIO_REL, a file under git) and a lock keyed by that file's own path, so a linked worktree cannot become a second campaign by patching its own copy.
            try:
                updated = portfolio_update(json.loads(Path(args.upsert).read_text(encoding="utf-8")))
            except (OSError, ValueError) as exc:
                print(f"Portfolio update not applied: {exc}", file=sys.stderr); return 2
            print(json.dumps(updated, indent=1)); return 0
        data = portfolio_snapshot()
        if args.id:
            item = next((r for r in data["items"] if r["id"] == args.id), None)
            print(json.dumps(item, indent=1) if item else f"Opportunity {args.id!r} not found")
            return 0 if item else 1
        print(json.dumps(data, indent=1) if args.json else portfolio_brief(data)); return 0
    if args.cmd == "seal":
        target = Path(args.campaign) / SEALED / f"INTENDED_ACTION_{args.index}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(Path(args.text_file).read_text(encoding="utf-8"), encoding="utf-8")
        print(f"{target} sha256 {sha256_file(target)}"); return 0
    if args.cmd == "brief":
        campaign = Path(args.campaign)
        mission = Path(args.mission_file).read_text(encoding="utf-8") if args.mission_file else ""
        constraints = Path(args.constraints_file).read_text(encoding="utf-8") if args.constraints_file else ""
        if args.stage == "A" and args.sealed_intended:
            print("Stage A takes no intended action: that is Stage B's input.", file=sys.stderr); return 2
        text = build_brief(args.stage, campaign, mission, constraints, args.task_record,
                           Path(args.assessment) if args.assessment else None, Path(args.sealed_intended) if args.sealed_intended else None, args.expect)
        out = Path(args.out) if args.out else campaign / f"brief_{args.stage}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        for line in text.splitlines():  # say it now, before a launch is spent: the brief itself carries the same statement
            if "is ahead of this snapshot" in line or line.startswith("- **Not available to you:**"):
                print("WARNING:", line.lstrip("- "), file=sys.stderr)
        print(f"{out} sha256 {sha256_file(out)}"); return 0
    if args.cmd == "run":
        return run(args.stage, Path(args.campaign), Path(args.brief), args.model, args.effort, args.timeout, LIMITS, args.extra_attempt)
    if args.cmd == "extract":
        text = extract_transcript(Path(args.transcript))
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"{args.out}: {len(text)} chars sha256 {sha256_text(text)} (extracted from {args.transcript})"); return 0 if text else 1
    if args.cmd == "check":
        return check(Path(args.campaign))
    campaign = Path(args.campaign)
    if args.cmd in ("recall", "tick", "evaluate", "assign", "meeting", "deliver", "activate", "disable", "authorise-continuous", "end-continuous", "refresh") and primary_refusal():
        print(primary_refusal(), file=sys.stderr); return 2
    if args.cmd == "refresh":
        try:
            return refresh(campaign)
        except OSError as exc:
            print(f"refresh: {exc}", file=sys.stderr); return 2
    if args.cmd in ("assign", "deliver"):
        stale = stale_refusal(campaign)
        if stale:
            print(stale, file=sys.stderr); return 2
    if args.cmd == "recall":
        print(recall_prompt(campaign)); return 0
    if args.cmd == "recall-armed":
        st = _load_state(campaign); now = _now()
        st["recall"] = {"armed_utc": _utc(now), "job_id": args.job_id, "tag": re.search(r"\[text ([0-9a-f]{8})\]", recall_prompt(campaign)).group(1)}
        _save_state(campaign, st); print(json.dumps(st["recall"])); return 0
    if args.cmd == "tick":
        print(json.dumps(tick(campaign), indent=1)); return 0
    if args.cmd == "meeting":
        try:
            result = meeting(campaign, request=args.request or "", source=args.source, actor=args.actor,
                             open_round=args.open, close_file=Path(args.close) if args.close else None)
        except (OSError, ValueError, TypeError, KeyError) as exc:
            print("MEETING: " + str(exc), file=sys.stderr); return 2
        print(json.dumps(result, indent=1)); return 0
    if args.cmd == "evaluate":
        return evaluate(campaign, args.model, args.effort, args.timeout)
    if args.cmd == "assign":
        try:
            return host_assign(campaign, Path(args.text_file).read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print(f"Host assignment not registered: {exc}", file=sys.stderr); return 2
    if args.cmd == "hold":
        return hold(campaign, args.reason, args.resume_when, args.excluded)
    if args.cmd in ("strand", "rotation", "reconcile", "dream"):
        campaign = Path(args.campaign)
        try:
            def show(row):
                for w in row.pop("warnings", []):
                    print("WARNING: " + w, file=sys.stderr)
                print(json.dumps(row, ensure_ascii=False))
            if args.cmd == "strand":
                show(record_strand(campaign, args.id, args.strand, args.basis, args.at, args.counts_with))
            elif args.cmd == "rotation":
                show(defer_rotation(campaign, args.reason, args.resume)) if args.defer else print(rotation_status(campaign)["line"])
            elif args.cmd == "reconcile":
                if args.attest:
                    show(attest_reconciliation(campaign, args.attest, args.changed, args.residual, args.note))
                else:
                    print(reconcile_state(campaign)["line"])
                    cands = reconcile_findings(campaign)
                    for c in cands:
                        print(f"  candidate {c['id']} (owner {c['owner']}): {c['why']}")
                    print(f"  {len(cands)} candidate(s); a candidate is a place to look, not a verdict. Also check by reading: ready rows consumed or superseded, backlog rows touched by later results, parked rows whose reopening condition is met in prose, questions that live only in reports.")
            else:
                pairs = [(t, args.what[i] if i < len(args.what) else "") for i, t in enumerate(args.to)]
                show(record_dream(campaign, args.id, pairs, args.none, args.counter))
        except (OSError, ValueError) as exc:
            print(f"NOT RECORDED: {exc}", file=sys.stderr)
            return 1
        return 0
    if args.cmd == "status":
        print(status(campaign)); return 0
    if args.cmd == "deliver":
        refusal = delivery_refusal(campaign, args.id, args.state, args.to, args.evidence, args.receipt)
        if refusal:
            print("REFUSED: " + refusal, file=sys.stderr); return 2
        _log_assignment(campaign, {"id": args.id, "state": args.state, "evidence": args.evidence, **({"to": args.to} if args.to else {}), **({"receipt": args.receipt} if args.receipt else {})}); print(f"{args.id}: {args.state} recorded"); return 0
    if args.cmd == "activate":
        now = _now()
        campaign.mkdir(parents=True, exist_ok=True)
        data = {"activated_utc": _utc(now), "expires_utc": _utc(now + dt.timedelta(hours=args.hours)), "max_invocations": args.max_invocations, "max_assignments": args.max_assignments,
                "turn_limit": args.turn_limit, "recipients": dict(r.split("=", 1) for r in args.recipient)}
        (campaign / "budget.json").write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8"); print(json.dumps(data)); return 0
    if args.cmd == "authorise-continuous":
        path = campaign / CONTINUOUS
        prior = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        b, att = _budget(campaign), _attempts(campaign)
        if not b:
            print("REFUSED: no campaign budget here; continuous operation is a mode of an existing campaign, not a new one", file=sys.stderr); return 2
        data = {"mode": "continuous", "authorised_utc": prior.get("authorised_utc") or _utc(_now()), "source": args.source,
                "scope": "inside the Operator roadmap, the existing boundaries and exclusions, and the available resources; operator stop, pause and new instructions prevail",
                "pilot_at_authorisation": prior.get("pilot_at_authorisation") or {"invocations_executed": len({(a["stage"], a["index"]) for a in att}), "max_invocations": b.get("max_invocations"),
                                                                                   "assignments_drafted": len([1 for e in _events(campaign) if e["state"] == "DRAFTED"]), "max_assignments": b.get("max_assignments"),
                                                                                   "expires_utc": b.get("expires_utc")},
                "min_hours_between": args.min_hours_between, "min_hours_anticipating": args.min_hours_anticipating}
        if args.weekly_limit:
            if not (args.advisor_share and args.unit and 0 < args.advisor_share <= 1):
                print("REFUSED: a weekly limit needs --advisor-share (0-1] and --unit", file=sys.stderr); return 2
            data["weekly_allocation"] = {"usable_limit": args.weekly_limit, "advisor_share": args.advisor_share, "unit": args.unit, "stated_by": "operator"}
        else:
            data["weekly_allocation"] = {"usable_limit": None, "note": "not given by the operator and not exposed by the runtime: declared unknown, never assumed"}
        first = not path.exists()
        path.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        if first:                                           # the authorisation is itself recorded in the roadmap section: the next tick reads it as a roadmap change and evaluates once
            state = _load_state(campaign)
            if state:
                state["roadmap_sha256"] = ""; _save_state(campaign, state)
        print(json.dumps(data)); return 0
    if args.cmd == "end-continuous":
        path = campaign / CONTINUOUS
        if not path.exists():
            print("no continuous authorisation here"); return 0
        data = json.loads(path.read_text(encoding="utf-8")); data.update(ended_utc=_utc(_now()), ended_reason=args.reason)
        path.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8"); print("continuous mode ended; the bounded pilot rules apply again"); return 0
    (campaign / "DISABLED").write_text(_utc(_now()) + "\n", encoding="utf-8"); print("disabled"); return 0


if __name__ == "__main__":
    sys.exit(main())
