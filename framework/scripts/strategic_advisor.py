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
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mandate_continuity as mc  # noqa: E402  the existing reader of task-record queues

ROOT = Path(__file__).resolve().parents[2]
AGENT = "legend-strategic-advisor"
TOOLS = ["Read", "Glob", "Grep", "WebFetch"]
DENIED = ["Bash", "Write", "Edit", "NotebookEdit", "Agent", "Task", "WebSearch", "SendMessage", "Skill", "Read(**/advisor_sealed/**)"]
SEALED = "advisor_sealed"
LIMITS = {"A": 2, "B": 2, "S": 1, "P": 3}
DASHBOARD_URL = "https://marinomassimo-dot.github.io/legend-development/"


def _memory_dir() -> Path:
    """The private memory directory of the main checkout (a worktree has none of its own)."""
    common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    main = Path(common).parent if common else ROOT
    return Path.home() / ".claude" / "projects" / ("-" + str(main).strip("/").replace("/", "-")) / "memory"


MEMORY_DIR = _memory_dir()

# The entry map. One home. Starting places, not a shortlist: a glob is counted here and listed by the advisor.
ENTRY_POINTS: list[tuple[str, str, list[str]]] = [
    ("limits", "Authorised mission and resource limits: the task record named in the brief, and its siblings", ["ledger/tasks/*/*.json"]),
    ("invariants", "Canonical project invariants and the operating rules", [
        "CLAUDE.md", "ARCHITECTURE.md", "framework/master/harness_development_principles.md", "framework/master/designed_for_growth.md",
        "framework/master/gold_is_in_the_details.md", "framework/instruction/LEGEND_CORE.md", "framework/instruction/epistemic_discipline.md",
        "disease-models/wwox/mission.md"]),
    ("repurposing_method", "Drug-repurposing roadmap and Standing method", [
        "disease-models/wwox/research/drug_repurposing/roadmap_current.md", "framework/protocols/repurposing_adapter_convention.md"]),
    ("dashboard", "Dashboard: source records of the public page (the page is a map, the records are the facts)", [
        "disease-models/wwox/research/drug_repurposing/view/README.md", "disease-models/wwox/research/drug_repurposing/view/shareable_package/manifest.json",
        "disease-models/wwox/research/drug_repurposing/view/shareable_package/README.md", "disease-models/wwox/research/drug_repurposing/view/DEPLOY.md"]),
    ("investigations", "Investigations (research investment, not efficacy), needs and cards", [
        "disease-models/wwox/research/drug_repurposing/ranking_it*/investigations.tsv", "disease-models/wwox/research/drug_repurposing/ranking_it*/ranking.json",
        "disease-models/wwox/research/drug_repurposing/needs/needs.md", "disease-models/wwox/research/drug_repurposing/cards/*"]),
    ("open_questions", "Open-question maps and rows", ["disease-models/wwox/research/drug_repurposing/**/open_questions*"]),
    ("candidates", "Candidates, comparisons and hypothesis packages", [
        "disease-models/wwox/research/drug_repurposing/generation_it*/", "disease-models/wwox/research/drug_repurposing/**/compound_decisions*.tsv",
        "disease-models/wwox/research/drug_repurposing/**/hypotheses*"]),
    ("packages", "Completed packages and their consumer notes", [
        "disease-models/wwox/research/drug_repurposing/*/README.md", "disease-models/wwox/research/drug_repurposing/**/CONSUMER_NOTE.md"]),
    ("diagnoses", "Diagnoses, evaluations and DREAM", [
        "disease-models/wwox/research/session_evaluations/*", "disease-models/wwox/research/drug_repurposing/diagnosis_*/*", "disease-models/wwox/research/dream*/README.md"]),
    ("memory_dismissals", "Dismissal and discovery ledgers, memory index (outside the repository)", [
        "disease-models/wwox/research/dismissal_ledger_current.md", "disease-models/wwox/research/discovery_ledger_current.md", str(MEMORY_DIR / "MEMORY.md")]),
    ("radar", "Radar findings and capability gaps", [
        "governance/candidates/HARNESS-SCOUT-*.md", "disease-models/wwox/research/capability_scout_log.md", "SKILLS.md", "CAPABILITIES.md"]),
    ("tools", "Which tool answers which question (the advisor has no shell; this explains what the records came from)", ["framework/scripts/README.md"]),
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
        out.append(f"| {r['id']} | {r['what']} | {'<br>'.join('`' + p + '`' for p in r['patterns'])} | {r['matches']} | {r['last_commit'][:10]} | {big} |")
    return "\n".join(out)


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
    refusal = budget_refusal(campaign)
    if refusal:
        print(f"CEILING: {refusal}. This ceiling is procedural: it binds runs launched through this tool only.", file=sys.stderr)
        return 2
    turn_limit = int(_budget(campaign).get("turn_limit") or 0)
    used = {a["index"] for a in _attempts(campaign) if a.get("stage") == stage}  # a log row is written at launch and again at the end: count attempts once
    extra = False
    if len(used) >= limits[stage] and extra_reason:
        # one recorded extra attempt per stage, and only when every earlier attempt of the stage produced no assessment
        concluded = [a for a in _attempts(campaign) if a.get("stage") == stage and a["outcome"] not in ("STARTED", "OK")]
        if len(concluded) == len(used) and not any(a.get("extra") for a in _attempts(campaign) if a.get("stage") == stage):
            extra = True
    if len(used) >= limits[stage] and not extra:
        print(f"CEILING: stage {stage} already has {len(used)} attempt(s) in {campaign} (limit {limits[stage]}); failed attempts count. "
              "This ceiling is procedural: it binds runs launched through this tool only.", file=sys.stderr)
        return 2
    index = max(used, default=0) + 1
    label = f"{stage}{index}"
    out = campaign / label
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
    _append(campaign, {**row, "outcome": outcome, "ended_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
    print(f"{label}: {outcome} → {out}")
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
    for stage in LIMITS:
        n = len({a["index"] for a in attempts if a["stage"] == stage})
        extras = len({a["index"] for a in attempts if a["stage"] == stage and a.get("extra")})
        if n > LIMITS[stage] + extras:
            problems.append(f"stage {stage}: {n} attempts exceed the ceiling {LIMITS[stage]}")
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
OPEN_VERDICTS = ("CONTINUE", "ALL_BLOCKED", "COMPLETE_PENDING")
EVENT_SUBJECT = re.compile(r"COMPLETE|closed|closure|integrate task|delivered|consumed|landed", re.I)


def _now() -> dt.datetime:
    forced = os.environ.get("LEGEND_ADVISOR_NOW")
    return dt.datetime.fromisoformat(forced.replace("Z", "+00:00")) if forced else dt.datetime.now(dt.timezone.utc)


def _utc(when: dt.datetime) -> str:
    return when.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _budget(campaign: Path) -> dict[str, Any]:
    path = Path(campaign) / "budget.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def budget_refusal(campaign: Path) -> str:
    """Why no further invocation may start in this campaign, or '' (no budget file: the earlier per-stage ceilings apply alone)."""
    b = _budget(campaign)
    if not b:
        return ""
    if (Path(campaign) / "DISABLED").exists():
        return "the campaign is disabled"
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
            out[d["TASK_ID"]] = {"state": "OPEN" if state in OPEN_VERDICTS else state, "owner": path.parent.name, "path": str(path.relative_to(ROOT))}
    return out


def _sessions() -> dict[str, str] | None:
    try:
        done = subprocess.run([os.environ.get("LEGEND_ADVISOR_CLAUDE", "claude"), "agents", "--json"], capture_output=True, text=True, timeout=25)
        return {str(x.get("name")): str(x.get("status")) for x in json.loads(done.stdout)} if done.returncode == 0 else None
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError):
        return None


def observe(campaign: Path, state: dict[str, Any]) -> dict[str, Any]:
    """The bounded facts a decision needs, read mechanically: roadmap digest, commits since the last tick, mandate transitions, stalled mandates reported by the watch, sessions."""
    main_sha = _git("rev-parse", "main")
    last = state.get("main_sha") or main_sha
    commits = [c for c in _git("log", "--format=%h %s", f"{last}..main", "--", "ledger/tasks", "disease-models/wwox/research/drug_repurposing").splitlines()[:60] if c.strip()]
    recs = _records()
    before = state.get("mandates") or {}
    transitions = [f"{t}: {before[t]} -> {r['state']}" for t, r in recs.items() if t in before and before[t] != r["state"]]
    opened = [t for t in recs if before and t not in before and recs[t]["state"] == "OPEN"]
    stalled = []
    try:
        watch = subprocess.run([sys.executable, str(ROOT / "framework/scripts/mandate_watch.py"), "events", "--last", "30"], capture_output=True, text=True, timeout=30).stdout
        stalled = sorted({m.group(1) for m in re.finditer(r"RESUME ((?:[A-Z0-9]+-)+[A-Z0-9]+)", watch) if recs.get(m.group(1), {}).get("state") == "OPEN"})
    except (OSError, subprocess.SubprocessError):
        pass
    events = ([f"delivery: {c}" for c in commits if EVENT_SUBJECT.search(c)] + [f"mandate: {t}" for t in transitions] + [f"opened: {t}" for t in opened]
              + [f"stalled-for-the-watch: {t}" for t in stalled])
    rm = roadmap_text()
    return {"main_sha": main_sha, "roadmap_sha256": sha256_text(rm) if rm else "", "commits_since_last_tick": len(commits), "events": events,
            "open_mandates": sorted(t for t, r in recs.items() if r["state"] == "OPEN"), "mandates": {t: r["state"] for t, r in recs.items()},
            "sessions": _sessions()}


def tick(campaign: Path) -> dict[str, Any]:
    """The hourly check: mostly mechanical, no model. Verdicts: NONE (nothing new: reuse the previous assessment), EVALUATE (one strategic evaluation is due), and the reasons it is not
    (RUNNING, DISABLED, EXPIRED, BUDGET, DEFERRED). A stalled mandate is reported, not restarted: recovery stays with the mandate watch."""
    campaign = Path(campaign)
    state = _load_state(campaign)
    now = _now()
    obs = observe(campaign, state)
    first = not state
    refusal = budget_refusal(campaign)
    anticipating = [e for e in obs["events"] if e.startswith(("delivery:", "mandate:", "stalled"))] or ([f"roadmap changed"] if state.get("roadmap_sha256") not in (None, obs["roadmap_sha256"]) else [])
    changed = state.get("roadmap_sha256") not in (None, obs["roadmap_sha256"])
    digest = sha256_text(obs["roadmap_sha256"] + "|" + "|".join(sorted(obs["events"])))
    last_eval = dt.datetime.fromisoformat(state["last_evaluation_utc"].replace("Z", "+00:00")) if state.get("last_evaluation_utc") else None
    hours = (now - last_eval).total_seconds() / 3600 if last_eval else None
    verdict, why = "NONE", "nothing new: the previous assessment stands"
    if (campaign / "DISABLED").exists():
        verdict, why = "DISABLED", "the campaign is disabled"
    elif refusal:
        verdict, why = ("EXPIRED" if "expired" in refusal else "BUDGET"), refusal
    elif first and (campaign / "budget.json").exists():
        verdict, why = "EVALUATE", "campaign start: the roadmap and the first observation"
    elif first:
        why = "first tick: baseline recorded, no evaluation from history"
    elif _running(state):
        verdict, why = "RUNNING", "an evaluation is already running (same process identity)"
    elif obs["events"] or changed:
        if digest == state.get("last_digest"):
            why = "the same events were already evaluated"
        elif changed or (anticipating and (hours is None or hours >= 1)) or (hours is None or hours >= 4):
            verdict, why = "EVALUATE", ("roadmap changed" if changed else "; ".join(anticipating[:3] or obs["events"][:3]))
        else:
            verdict, why = "DEFERRED", f"events present but the last evaluation was {hours:.1f} h ago and none is anticipating"
    state.update(main_sha=obs["main_sha"], mandates=obs["mandates"], roadmap_sha256=obs["roadmap_sha256"], last_tick_utc=_utc(now))
    if verdict == "EVALUATE":
        state["pending_digest"] = digest
    _save_state(campaign, state)
    return {"verdict": verdict, "why": why, "events": obs["events"][:12], "open_mandates": obs["open_mandates"], "sessions": obs["sessions"], "digest": digest,
            "hours_since_last_evaluation": None if hours is None else round(hours, 1)}


def parse_assignments(text: str) -> list[dict[str, str]]:
    """The `### ASSIGNMENT n` blocks of an assessment: `field: value` lines (a value may continue on the following lines). A block missing a required field is kept and flagged."""
    out = []
    for block in re.split(r"^### ASSIGNMENT\b.*$", text, flags=re.M)[1:]:
        block = block.split("\n## ", 1)[0]
        fields, cur = {}, None
        for line in block.splitlines():
            m = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if m and m.group(1) in ASSIGNMENT_FIELDS:
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


def _log_assignment(campaign: Path, row: dict[str, Any]) -> None:
    with (Path(campaign) / "assignments.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({**row, "utc": _utc(_now())}, sort_keys=True) + "\n")


def register_assignments(campaign: Path, label: str, text: str) -> list[dict[str, str]]:
    """Save the drafts of an assessment as `assignments/ADV-nnn.md`, within the campaign's assignment budget and without duplicating a key already drafted or already named in a task record."""
    campaign = Path(campaign)
    cap = int(_budget(campaign).get("max_assignments", 10**9))
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
        (out / f"{ident}.md").write_text(f"# {ident} (assessment {label}, campaign {campaign.name})\n\nRecipient: {block['recipient']}\n\n{block['_text']}\n", encoding="utf-8")
        row = {"id": ident, "state": "DRAFTED", "key": key, "recipient": block["recipient"], "assessment": label}
        _log_assignment(campaign, row); drafted[ident] = row; made.append({"id": ident, **block})
    return made


def assignment_states(campaign: Path) -> dict[str, dict[str, Any]]:
    """Per assignment, the evidence levels kept apart: DRAFTED (saved) -> SENT (the channel accepted a message: recorded by the sender) -> TAKEN (its id is in a task record) -> EXECUTED (a
    DONE step in a record carries its id) . UNREACHABLE and the other rows are states of their own. None of them says the result was useful."""
    out: dict[str, dict[str, Any]] = {}
    for e in _events(campaign):
        if e.get("id"):
            out.setdefault(e["id"], {"recipient": e.get("recipient", ""), "key": e.get("key", ""), "levels": []})["levels"].append(e["state"])
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
                if "PROACTIVE-ADVISOR" in path.name:
                    continue                                      # the campaign's own record names the drafts: that is not a recipient taking one in charge
                if h and "TAKEN" not in out[ident]["levels"]:
                    out[ident]["levels"].append("TAKEN")
                if o and "EXECUTED" not in out[ident]["levels"]:
                    out[ident]["levels"].append("EXECUTED")
    for v in out.values():
        order = ["DRAFTED", "SENT", "TAKEN", "EXECUTED"]
        v["highest"] = max((x for x in v["levels"] if x in order), key=order.index, default="")
        v["unreachable"] = "UNREACHABLE" in v["levels"] and v["highest"] in ("", "DRAFTED")
    return out


def build_brief_p(campaign: Path, obs: dict[str, Any]) -> str:
    campaign = Path(campaign)
    states = assignment_states(campaign)
    prior = sorted(campaign.glob("P*/assessment.md"))
    parts = ["# Strategic Advisor brief — Stage P (proactive evaluation)", "", "## Snapshot", render_snapshot(snapshot()), "",
             "## Operator roadmap (authoritative; operator instructions prevail over any automatic plan)", roadmap_text() or "(no roadmap section found: say so, and propose nothing beyond keeping the plan)", "",
             "## Campaign limits", json.dumps({k: v for k, v in _budget(campaign).items() if k in ("expires_utc", "max_invocations", "max_assignments", "turn_limit")}), "",
             "## Observed state (mechanical, this tick)", json.dumps({k: obs[k] for k in ("events", "open_mandates", "sessions", "commits_since_last_tick")}, indent=1), "",
             "## Assignments already drafted, with their evidence level (do not duplicate; follow what was taken in charge)",
             json.dumps({k: {"recipient": v["recipient"], "key": v["key"], "highest": v["highest"]} for k, v in states.items()}, indent=1) or "none", "",
             f"## Previous assessment\n{prior[-1].parent.name}: `{prior[-1]}` (read it; reuse it when nothing relevant changed)" if prior else "## Previous assessment\nnone", "",
             "## Neutral entry points", render_entrypoints(entrypoints()), "", f"Memory directory (read-only): `{MEMORY_DIR}`", "", "## Output", CONTRACT,
             "Give the usual headings, then `## Assignments`: either `none: <reason>` (continuing the plan can be the best decision) or one `### ASSIGNMENT n` block per assignment with exactly these "
             "`field: value` lines: " + ", ".join(ASSIGNMENT_FIELDS) + ". recipient is Orchestrator, Science or Harness. At most as many blocks as the campaign allows; none to show independence.", ""]
    return "\n".join(parts)


def evaluate(campaign: Path, model: str = "opus", effort: str = "high", timeout: int = 3600) -> int:
    """One strategic evaluation: brief, run (counted in the campaign budget), save, register the assignment drafts. Returns the run's exit code."""
    campaign = Path(campaign)
    refusal = budget_refusal(campaign)
    if refusal:
        print(f"REFUSED: {refusal}", file=sys.stderr); return 2
    state = _load_state(campaign)
    if _running(state):
        print("REFUSED: an evaluation is already running", file=sys.stderr); return 2
    state["running"] = _pid_identity(os.getpid()); _save_state(campaign, state)
    try:
        obs = observe(campaign, state)
        brief = campaign / "brief_P.md"
        brief.write_text(build_brief_p(campaign, obs), encoding="utf-8")
        code = run("P", campaign, brief, model, effort, timeout, LIMITS)
        label = f"P{max((a['index'] for a in _attempts(campaign) if a['stage'] == 'P'), default=0)}"
        assessment = campaign / label / "assessment.md"
        if code == 0 and assessment.exists():
            made = register_assignments(campaign, label, assessment.read_text(encoding="utf-8"))
            print(f"{label}: {len(made)} assignment draft(s) registered: " + ", ".join(m["id"] for m in made))
        state = _load_state(campaign)
        state.update(last_evaluation_utc=_utc(_now()), last_digest=state.get("pending_digest", state.get("last_digest")), running="")
        _save_state(campaign, state)
        return code
    finally:
        state = _load_state(campaign); state["running"] = ""; _save_state(campaign, state)


def status(campaign: Path) -> str:
    campaign = Path(campaign)
    b = _budget(campaign)
    att = _attempts(campaign)
    n = len({(a["stage"], a["index"]) for a in att})
    lines = [f"campaign {campaign.name}: activated {b.get('activated_utc', '-')}, expires {b.get('expires_utc', '-')}, invocations {n}/{b.get('max_invocations', '-')}, "
             f"assignments drafted {len([1 for e in _events(campaign) if e['state'] == 'DRAFTED'])}/{b.get('max_assignments', '-')}, {'DISABLED' if (campaign / 'DISABLED').exists() else 'enabled'}"]
    for ident, v in sorted(assignment_states(campaign).items()):
        lines.append(f"  {ident} [{v['recipient']}] {v['key']}: highest evidence {v['highest'] or 'none'}; levels {','.join(v['levels'])}" + ("; UNREACHABLE (residual stays in the queue)" if v["unreachable"] else ""))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("entrypoints")
    sub.add_parser("snapshot")
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
    t = sub.add_parser("tick", help="the hourly bounded check (no model unless you then run `evaluate`)"); t.add_argument("--campaign", required=True)
    ev = sub.add_parser("evaluate", help="one strategic evaluation, counted in the campaign budget"); ev.add_argument("--campaign", required=True)
    ev.add_argument("--model", default="opus"); ev.add_argument("--effort", default="high", choices=["low", "medium", "high"]); ev.add_argument("--timeout", type=int, default=3600)
    st = sub.add_parser("status", help="budget and the evidence level of every assignment"); st.add_argument("--campaign", required=True)
    dl = sub.add_parser("deliver", help="record what the channel did with an assignment (SENT with the message id, or UNREACHABLE with the reason)"); dl.add_argument("--campaign", required=True)
    dl.add_argument("--id", required=True); dl.add_argument("--state", choices=["SENT", "UNREACHABLE"], required=True); dl.add_argument("--evidence", required=True)
    ac = sub.add_parser("activate", help="write the campaign budget (24 h by default, no renewal)"); ac.add_argument("--campaign", required=True)
    ac.add_argument("--hours", type=int, default=24); ac.add_argument("--max-invocations", type=int, default=3); ac.add_argument("--max-assignments", type=int, default=3)
    ac.add_argument("--turn-limit", type=int, default=20); ac.add_argument("--recipient", action="append", default=[], help="role=session name, e.g. Orchestrator='IT Orchestrator'")
    dis = sub.add_parser("disable", help="stop the pilot: later ticks and runs refuse; ordinary scheduling and the sessions' work continue"); dis.add_argument("--campaign", required=True)
    args = ap.parse_args(argv)

    if args.cmd == "entrypoints":
        print(render_entrypoints(entrypoints())); return 0
    if args.cmd == "snapshot":
        print(json.dumps(snapshot(), indent=2)); return 0
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
    if args.cmd == "tick":
        print(json.dumps(tick(campaign), indent=1)); return 0
    if args.cmd == "evaluate":
        return evaluate(campaign, args.model, args.effort, args.timeout)
    if args.cmd == "status":
        print(status(campaign)); return 0
    if args.cmd == "deliver":
        _log_assignment(campaign, {"id": args.id, "state": args.state, "evidence": args.evidence}); print(f"{args.id}: {args.state} recorded"); return 0
    if args.cmd == "activate":
        now = _now()
        campaign.mkdir(parents=True, exist_ok=True)
        data = {"activated_utc": _utc(now), "expires_utc": _utc(now + dt.timedelta(hours=args.hours)), "max_invocations": args.max_invocations, "max_assignments": args.max_assignments,
                "turn_limit": args.turn_limit, "recipients": dict(r.split("=", 1) for r in args.recipient)}
        (campaign / "budget.json").write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8"); print(json.dumps(data)); return 0
    (campaign / "DISABLED").write_text(_utc(_now()) + "\n", encoding="utf-8"); print("disabled"); return 0


if __name__ == "__main__":
    sys.exit(main())
