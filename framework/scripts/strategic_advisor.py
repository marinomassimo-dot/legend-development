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
    python3 framework/scripts/strategic_advisor.py brief  --stage A --campaign DIR --mission-file F --constraints-file F [--task-record P]
    python3 framework/scripts/strategic_advisor.py brief  --stage B --campaign DIR --assessment A.md --sealed-intended S.md --constraints-file F
    python3 framework/scripts/strategic_advisor.py run    --stage A|B|S --campaign DIR --brief FILE --model opus --effort high
    python3 framework/scripts/strategic_advisor.py extract --transcript T.jsonl --out FILE
    python3 framework/scripts/strategic_advisor.py check  --campaign DIR

WHAT IS MECHANICAL AND WHAT IS NOT
----------------------------------
Mechanical (this tool, or the runtime flags it passes): the tool list the advisor is born with
(read from the runtime's init event), a deny rule on the sealed folder, the saved assessment
being the result event verbatim (and cross-checked against the persisted session transcript),
the model read back per turn, and a per-campaign attempt log that counts every launch, failed
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
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
AGENT = "legend-strategic-advisor"
TOOLS = ["Read", "Glob", "Grep", "WebFetch"]
DENIED = ["Bash", "Write", "Edit", "NotebookEdit", "Agent", "Task", "WebSearch", "SendMessage", "Skill", "Read(**/advisor_sealed/**)"]
SEALED = "advisor_sealed"
LIMITS = {"A": 2, "B": 2, "S": 1}
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


def _git(*args: str) -> str:
    done = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return done.stdout.strip() if done.returncode == 0 else ""


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
        rows.append({"id": key, "what": what, "patterns": patterns, "matches": len(matches), "last_commit": last})
    return rows


def snapshot(extra: list[str] | None = None) -> dict[str, Any]:
    """Repository state at dispatch: SHA, time, uncommitted paths with digests, dashboard revision."""
    dirty = []
    for line in _git("status", "--porcelain", "--untracked-files=all").splitlines()[:200]:
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
    dash = snap["dashboard"]
    lines.append(f"- Dashboard: {dash['url']} · source revision {dash['package_last_commit'] or 'unknown'} · {dash['note']}")
    return "\n".join(lines)


def render_entrypoints(rows: list[dict[str, Any]]) -> str:
    out = ["| id | what | patterns (relative to the repository root unless absolute) | matches now | last commit |", "|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['id']} | {r['what']} | {'<br>'.join('`' + p + '`' for p in r['patterns'])} | {r['matches']} | {r['last_commit'][:10]} |")
    return "\n".join(out)


CONTRACT = ("Return one assessment with the headings given in your definition. Name every file or page you opened under "
            "'Inspected'. You cannot write, run commands or start agents. The entry points are starting places; follow references past them.")


def build_brief(stage: str, campaign: Path, mission: str, constraints: str, task_record: str = "",
                assessment: Path | None = None, intended: Path | None = None) -> str:
    snap = snapshot()
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
        elif kind == "result":
            result = event
    return {"init": init, "result": result, "calls": calls, "turn_models": models}


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


def run(stage: str, campaign: Path, brief: Path, model: str, effort: str, timeout: int, limits: dict[str, int], extra_reason: str = "") -> int:
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
                                 "total_cost_usd": result.get("total_cost_usd"), "census": census},
            "capture": {"method": "runtime result event of the headless stream (stream-json), saved verbatim", "source_session_id": session,
                        "raw_stream": str(raw), "raw_stream_sha256": sha256_file(raw), "assessment_sha256": sha256_text(text) if ok else "",
                        "transcript_cross_check": agrees, "transcribed_by_caller": False,
                        "published": "assessment.md and this file only; the raw stream and the session transcript stay local"},
            "tool_calls": [{k: c.get(k) for k in ("name", "input", "is_error", "result_head")} for c in facts["calls"]],
            "context": {"brief_chars": len(brief.read_text(encoding="utf-8"))},
        }
        (out / "meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True), encoding="utf-8")
        outcome, code = ("OK" if ok else "FAILED"), (0 if ok else 1)
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
        if meta["runtime_readback"].get("census", {}).get("changed_mid_run"):
            problems.append(f"{meta_path.parent.name}: the model changed mid-run")
        opened = {str((c.get("input") or {}).get("file_path") or (c.get("input") or {}).get("path") or "") for c in meta["tool_calls"]}
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("entrypoints")
    sub.add_parser("snapshot")
    s = sub.add_parser("seal"); s.add_argument("--campaign", required=True); s.add_argument("--index", required=True); s.add_argument("--text-file", required=True)
    b = sub.add_parser("brief"); b.add_argument("--stage", choices=["A", "B"], required=True); b.add_argument("--campaign", required=True)
    b.add_argument("--mission-file"); b.add_argument("--constraints-file"); b.add_argument("--task-record", default="")
    b.add_argument("--assessment"); b.add_argument("--sealed-intended"); b.add_argument("--out")
    r = sub.add_parser("run"); r.add_argument("--stage", choices=["A", "B", "S"], required=True); r.add_argument("--campaign", required=True)
    r.add_argument("--brief", required=True); r.add_argument("--model", required=True); r.add_argument("--effort", required=True, choices=["low", "medium", "high"])
    r.add_argument("--timeout", type=int, default=3600)
    r.add_argument("--extra-attempt", default="", help="reason; allows one recorded attempt beyond the ceiling when every earlier attempt of the stage failed")
    e = sub.add_parser("extract"); e.add_argument("--transcript", required=True); e.add_argument("--out", required=True)
    c = sub.add_parser("check"); c.add_argument("--campaign", required=True)
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
                           Path(args.assessment) if args.assessment else None, Path(args.sealed_intended) if args.sealed_intended else None)
        out = Path(args.out) if args.out else campaign / f"brief_{args.stage}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"{out} sha256 {sha256_file(out)}"); return 0
    if args.cmd == "run":
        return run(args.stage, Path(args.campaign), Path(args.brief), args.model, args.effort, args.timeout, LIMITS, args.extra_attempt)
    if args.cmd == "extract":
        text = extract_transcript(Path(args.transcript))
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"{args.out}: {len(text)} chars sha256 {sha256_text(text)} (extracted from {args.transcript})"); return 0 if text else 1
    return check(Path(args.campaign))


if __name__ == "__main__":
    sys.exit(main())
