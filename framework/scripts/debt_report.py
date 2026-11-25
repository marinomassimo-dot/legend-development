#!/usr/bin/env python3
"""One screen of the laboratory's debt, every line sourced, print-only (ADV-221).

The operator's standing rule is that no actor is idle and that the debt is measured at every
round. Measuring it used to take five commands and one wrong number: this is the one command.
It prints, it writes nothing but the held digest index cache in the host state folder, it has no
output path, and it runs from a linked worktree.

    python3 framework/scripts/debt_report.py                 # everything, about 50 s
    python3 framework/scripts/debt_report.py --offline       # no network: skips the PubMed delta and the CI queue
    python3 framework/scripts/debt_report.py --no-advisor    # skips rotation and assignments (about 25 s of the run)
    python3 framework/scripts/debt_report.py --json          # the same, machine-readable

What each block is, and where it comes from (each printed line names its file)
-------------------------------------------------------------------------------
1. COVERAGE. The depth table of `registries/coverage_report.md` (a derived page; its depth rule
   is the DEEPEST surviving receipt per study, `fulltext_receipts.receipt_depth_index`, combined
   with the registry's own declaration). Beside it, computed here from the receipt ledger, three
   readings that must not be mixed up:
     latest-receipt depth    the depth of the chronologically last surviving receipt per study;
     best-state depth        the deepest surviving receipt per study (what coverage_report uses);
     best-state SECTIONS     for studies with two or more receipts, how many sections the union
                             of earlier receipts marks `read` that the latest receipt does not.
   The section figures are this tool's own definition (below); SCI's ADV-219 counts them under
   its own, and the two are not claimed equal.
   One more line says which latest-receipt partial and complete studies have their BYTES on this
   host (`held_studies.py`: file name, else receipt SHA-256). It reads that tool's cached digest
   index, hashing only files new or changed since; it never builds the index cold and says so.
   `coverage_report.md` is not touched: it is committed, and `files/` differs from host to host.
2. PUBMED DELTA. `pubmed_delta_census.py` over the repository (one esearch call, plus one esummary
   for the PMIDs absent by PMID); skipped with --offline.
3. OPEN QUESTIONS. `research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv`:
   rows by status, and the OPEN rows least recently touched.
4. PORTFOLIO. `research/drug_repurposing/research_portfolio.tsv`: rows by status and the oldest
   `waiting` row with its `resume_when`.
5. ROTATION. `strategic_advisor.rotation_status` over `advisor_pilot_20261113/`.
6. ACTORS. Per recipient role in `advisor_pilot_20261113/assignments.jsonl`: the last event, and
   the assignments no DONE step carries (`strategic_advisor.assignment_states`: DRAFTED, SENT or
   TAKEN). That total overstates what is open, because an assignment consumed in a message
   leaves no DONE step; so the ones whose last event is within 48 hours are listed apart.
   No roster of live sessions exists in a checkout, so it prints `roster not readable`.
7. CI QUEUE. `ci_runs.py queue`'s view of the public release gate; skipped with --offline.

Definitions
-----------
A study is keyed by its PMID, else its DOI. A section counts as read when the receipt's coverage
value for it is exactly `read` (`not_read`, `not_present`, `unavailable`, `captions_only` and
`unknown_legacy` do not). "Narrower" means the union of the earlier receipts' read sections holds
at least one section the latest receipt's does not. Nothing here changes `coverage_report.py`:
a different depth definition is a proposal for its owner, never an edit made by a report.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo_root import repo_root  # noqa: E402

WWOX = "disease-models/wwox"
COVERAGE_MD = f"{WWOX}/registries/coverage_report.md"
LEDGER = f"{WWOX}/registries/fulltext_read_receipts.jsonl"
DRUG = f"{WWOX}/research/drug_repurposing"
OPEN_QUESTIONS = f"{DRUG}/batch_sci_20261105/map/open_questions_map.tsv"
PORTFOLIO = f"{DRUG}/research_portfolio.tsv"
CAMPAIGN = f"{DRUG}/advisor_pilot_20261113"
ASSIGNMENTS = f"{CAMPAIGN}/assignments.jsonl"
ROLES = ("Orchestrator", "Science", "Harness")
OPEN_LEVELS = ("DRAFTED", "SENT", "TAKEN")
DEPTH_ORDER = ("complete_fulltext_read", "partial_fulltext_read", "abstract_only",
               "queried_not_full_read", "retrieved_not_read")
DEPTH_SHORT = {"complete_fulltext_read": "complete", "partial_fulltext_read": "partial",
               "abstract_only": "abstract", "queried_not_full_read": "queried",
               "retrieved_not_read": "retrieved"}
DEPTH_RANK = {name: n for n, name in enumerate(reversed(DEPTH_ORDER))}
TABLE_ROW = re.compile(r"^\|\s*\**([^|*]+?)\**\s*\|\s*(\d+)\s*\|\s*(\d+)%\s*\|")


def tsv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle, delimiter="\t", quoting=csv.QUOTE_NONE))
    header, body = rows[0], rows[1:]
    return [dict(zip(header, row)) for row in body if row]


# ----------------------------------------------------------------------------- 1 coverage

def coverage_table(text: str) -> dict[str, int]:
    """The depth rows of the `## Coverage` table of coverage_report.md: label -> records."""
    out: dict[str, int] = {}
    inside = False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = line.strip() == "## Coverage"
            continue
        match = TABLE_ROW.match(line) if inside else None
        if match and match.group(1).strip().lower() != "depth":
            out[match.group(1).strip()] = int(match.group(2))
    return out


def study_key(study: dict) -> str:
    if study.get("pmid"):
        return f"pmid:{study['pmid']}"
    if study.get("doi"):
        return "doi:" + str(study["doi"]).lower().strip()
    return "other:" + json.dumps(study, sort_keys=True)


def read_sections(event: dict) -> set[str]:
    return {name for name, value in (event.get("coverage") or {}).items() if value == "read"}


def receipt_readings(events: list[dict]) -> dict:
    """Latest-receipt depth, best-state depth and the section loss, from the surviving receipts in ledger order."""
    studies: dict[str, list[dict]] = {}
    for event in events:
        if event.get("evidence_depth") in DEPTH_RANK and event.get("coverage") is not None and event.get("study_id"):
            studies.setdefault(study_key(event["study_id"]), []).append(event)
    latest = Counter(DEPTH_SHORT[s[-1]["evidence_depth"]] for s in studies.values())
    best = Counter(DEPTH_SHORT[max((e["evidence_depth"] for e in s), key=DEPTH_RANK.__getitem__)]
                   for s in studies.values())
    multi = {k: s for k, s in studies.items() if len(s) > 1}
    narrower = lost = union_total = 0
    for series in multi.values():
        union = set().union(*(read_sections(e) for e in series))
        gone = union - read_sections(series[-1])
        narrower += bool(gone)
        lost += len(gone)
        union_total += len(union)
    return {"studies": len(studies), "latest_depth": dict(latest), "best_depth": dict(best),
            "multi_receipt_studies": len(multi), "latest_narrower": narrower,
            "section_flags_lost": lost, "section_flags_union": union_total}


def coverage_block(root: Path, events: list[dict] | None = None) -> tuple[list[str], dict]:
    path = root / COVERAGE_MD
    table = coverage_table(path.read_text(encoding="utf-8")) if path.is_file() else {}
    lines = []
    if table:
        lines.append(f"coverage_report.md ({COVERAGE_MD}; depth = deepest receipt per study): "
                     + " · ".join(f"{label} {count}" for label, count in table.items()))
    else:
        lines.append(f"coverage_report.md not readable ({COVERAGE_MD})")
    data = {"table": table}
    if events is None:
        try:
            import fulltext_receipts as receipts
            ledger = root / LEDGER
            events = receipts.active_receipts(receipts.load_ledger(ledger))
        except Exception as error:  # noqa: BLE001 — a failed ledger is a printed fact, not a crash
            lines.append(f"receipt ledger not readable ({LEDGER}): {error}")
            return lines, data
    readings = receipt_readings(events)
    data["receipts"] = readings

    def depth(counter: dict) -> str:
        return " · ".join(f"{DEPTH_SHORT[n]} {counter.get(DEPTH_SHORT[n], 0)}" for n in DEPTH_ORDER)

    lines.append(f"{readings['studies']} studies with a receipt ({LEDGER}); "
                 f"latest-receipt depth: {depth(readings['latest_depth'])}")
    lines.append(f"  best-state depth (deepest receipt, the rule coverage_report uses): {depth(readings['best_depth'])}")
    lines.append(f"  best-state sections: of {readings['multi_receipt_studies']} studies with 2+ receipts, "
                 f"{readings['latest_narrower']} have a latest receipt narrower than the union of earlier ones; "
                 f"{readings['section_flags_lost']} of {readings['section_flags_union']} read-section flags "
                 f"vanish under 'latest' (this tool's own count: union of every earlier receipt, any study; "
                 f"coverage_report.md prints the same idea with the surviving-receipt rule, event_at order)")
    lines.append("  against SCI ADV-219 (primary flags, 2026-11-24): 428 multi-receipt studies and 172 narrower are reproduced exactly; "
                 "its '300 flags gone' is 294 'an earlier receipt already marks the section read' (286 class B + 8 class A) plus 6 "
                 "'an earlier receipt gives a better non-read label' (its best_state ranks read, not_present, captions_only, unavailable, "
                 "not_read across all receipts): a rule difference, stated, not an unknown; 294 is the clean 'already read' figure")
    return lines, data


def held_lines(root: Path, cache: Path | None = None) -> tuple[list[str], dict]:
    """Studies whose bytes are on this host, by name or by receipt digest. A fact about this disk, never about reading."""
    try:
        import held_studies
        cache = cache or held_studies.default_cache()
        if held_studies.files_dir(root) is None:
            return ["held bytes: not measured, this host holds no files/ (held_studies.py)"], {}
        if not cache.is_file():
            return ["held bytes: not indexed yet; run python3 framework/scripts/held_studies.py once (about 2 minutes)"], {}
        rows, numbers = held_studies.measure(root, cache)
        data = {name: held_studies.counts(rows, held_studies.DEPTHS[name]) for name in ("partial", "complete")}
        text = " · ".join(f"latest-{name} {c['studies']}: held {c['held']} (by name {c['held_by_name']}, by digest only "
                          f"{c['held_by_digest_only']}), not held {c['not_held']}" for name, c in data.items())
        return [f"held bytes on this host ({numbers['files_dir']}; held_studies.py, name or receipt SHA-256): {text}"], data
    except Exception as error:  # noqa: BLE001 — a failed count is a printed fact, not a crash
        return [f"held bytes: not measured ({type(error).__name__}: {error})"], {}


# ----------------------------------------------------------------------------- 2 delta

def delta_block(root: Path, offline: bool, runner: Callable | None = None) -> tuple[list[str], dict]:
    if offline:
        return ["skipped (--offline)"], {"skipped": True}
    try:
        import pubmed_delta_census as census
        report = (runner or (lambda: census.build_report(
            census.STANDING_TERM, root, [census.DEFAULT_SCOPE], census.fetch_pmids,
            census.fetch_summaries)))()
    except Exception as error:  # noqa: BLE001 — RouteFailed or any other: printed as the route result
        return [f"ROUTE FAILED: {error} (pubmed_delta_census.py); no claim about the delta"], {"error": str(error)}
    line = (f"PubMed {report['returned']} records on the standing WWOX query: {report['new_count']} true misses"
            + (f" ({', '.join(report['new_pmids'][:6])}{' ...' if report['new_count'] > 6 else ''})" if report["new_pmids"] else "")
            + f", {report['false_absent_count']} false absent, {report['seed_only_count']} seed-only (pubmed_delta_census.py)")
    return [line], {k: report[k] for k in ("returned", "new_count", "new_pmids", "false_absent_count", "seed_only_count")}


# ----------------------------------------------------------------------------- 3 open questions

def questions_block(root: Path) -> tuple[list[str], dict]:
    path = root / OPEN_QUESTIONS
    if not path.is_file():
        return [f"not readable ({OPEN_QUESTIONS})"], {}
    rows = tsv_rows(path)
    status = Counter(r.get("status", "") for r in rows)
    opened = sorted((r for r in rows if r.get("status") == "OPEN"), key=lambda r: (r.get("last_touched", ""), r.get("qid", "")))
    lines = [f"{len(rows)} rows ({OPEN_QUESTIONS}): " + " · ".join(f"{k} {v}" for k, v in sorted(status.items(), key=lambda kv: -kv[1]))]
    if opened:
        lines.append(f"  OPEN {len(opened)}; least recently touched: "
                     + ", ".join(f"{r['qid']} {r.get('last_touched', '?')}" for r in opened[:4])
                     + f"; most recent touch {max(r.get('last_touched', '') for r in opened)}")
    return lines, {"rows": len(rows), "status": dict(status), "open": len(opened),
                   "oldest_open": [(r["qid"], r.get("last_touched", "")) for r in opened[:4]]}


# ----------------------------------------------------------------------------- 4 portfolio

def portfolio_block(root: Path) -> tuple[list[str], dict]:
    path = root / PORTFOLIO
    if not path.is_file():
        return [f"not readable ({PORTFOLIO})"], {}
    rows = tsv_rows(path)
    status = Counter(r.get("status", "") for r in rows)
    lines = [f"{len(rows)} rows ({PORTFOLIO}): " + " · ".join(f"{k} {v}" for k, v in sorted(status.items(), key=lambda kv: -kv[1]))]
    waiting = sorted((r for r in rows if r.get("status") == "waiting"), key=lambda r: r.get("updated_utc", ""))
    data = {"rows": len(rows), "status": dict(status)}
    if waiting:
        oldest = waiting[0]
        lines.append(f"  oldest waiting: {oldest['id']} since {oldest.get('updated_utc', '?')}, resume_when: "
                     f"{(oldest.get('resume_when') or '(none)')[:110]}")
        data["oldest_waiting"] = oldest["id"]
    return lines, data


# ----------------------------------------------------------------------------- 5 and 6 advisor

def default_advisor(root: Path):
    import strategic_advisor as sa
    campaign = root / CAMPAIGN
    return sa.rotation_status(campaign), sa.assignment_states(campaign)


def advisor_block(root: Path, loader: Callable | None = None, now: datetime | None = None) -> tuple[list[str], list[str], dict]:
    try:
        rotation, states = (loader or default_advisor)(root)
    except Exception as error:  # noqa: BLE001 — printed, never guessed
        message = f"not readable ({error})"
        return [f"rotation {message}"], [f"assignments {message}", "roster not readable"], {"error": str(error)}
    path = root / ASSIGNMENTS
    last: dict[str, str] = {}
    stamp: dict[str, str] = {}
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                event = json.loads(line)
                if event.get("id"):
                    stamp[event["id"]] = max(stamp.get(event["id"], ""), str(event.get("utc", "")))
        for ident, info in states.items():
            role = info.get("recipient", "")
            last[role] = max(last.get(role, ""), stamp.get(ident, ""))
    actors = []
    data = {"rotation": rotation.get("state"), "actors": {}}
    cutoff = ((now or datetime.now(timezone.utc)) - timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M:%SZ")
    for role in ROLES:
        opened = sorted(i for i, info in states.items() if info.get("recipient") == role and info.get("highest") in OPEN_LEVELS)
        recent = [i for i in opened if stamp.get(i, "") >= cutoff]
        data["actors"][role] = {"last_event": last.get(role, ""), "without_done_step": len(opened), "recent_48h": recent}
        actors.append(f"{role}: last assignment event {last.get(role) or 'none'}; {len(opened)} without a DONE step, "
                      + (f"{len(recent)} touched in the last 48 h ({', '.join(recent[-6:])})" if recent else "none touched in the last 48 h"))
    actors.append(f"sessions: roster not readable (no roster file in a checkout; {ASSIGNMENTS} for assignments)")
    return [str(rotation.get("line", rotation.get("state", "")))], actors, data


# ----------------------------------------------------------------------------- 7 CI

def ci_block(offline: bool, fetcher: Callable | None = None) -> tuple[list[str], dict]:
    if offline:
        return ["skipped (--offline)"], {"skipped": True}
    try:
        import time
        import ci_runs
        recent = (fetcher or (lambda: ci_runs.fetch_recent(ci_runs.slug("development"))))()
        view = ci_runs.queue_view(recent, time.time())
    except Exception as error:  # noqa: BLE001 — a rate limit is a result
        return [f"not readable ({error}) (ci_runs.py queue)"], {"error": str(error)}
    done = ", ".join(f"{k} {v}" for k, v in sorted(view["window"].items())) or "none"
    return [f"{view['open']} open gate runs ({view['in_progress']} in progress, {view['queued']} queued), oldest "
            f"{ci_runs.human_age(view['oldest_age_seconds']) if view['rows'] else 'n/a'}; last {view['window_runs']} gate runs: {done} (ci_runs.py queue)"], \
        {k: view[k] for k in ("open", "in_progress", "queued", "oldest_age_seconds", "window")}


# ----------------------------------------------------------------------------- the page

def build(root: Path, offline: bool = False, advisor: bool = True, parts: dict | None = None) -> dict:
    parts = parts or {}
    sections: list[tuple[str, list[str], dict]] = []
    lines, data = coverage_block(root, parts.get("events"))
    held, data["held"] = held_lines(root, parts.get("held_cache"))
    sections.append(("COVERAGE", lines + held, data))
    sections.append(("PUBMED DELTA", *delta_block(root, offline, parts.get("delta"))))
    sections.append(("OPEN QUESTIONS", *questions_block(root)))
    sections.append(("PORTFOLIO", *portfolio_block(root)))
    if advisor:
        rotation, actors, data = advisor_block(root, parts.get("advisor"))
        sections.append(("ROTATION", rotation, {"rotation": data.get("rotation")}))
        sections.append(("ACTORS", actors, data.get("actors", {})))
    else:
        sections.append(("ROTATION", ["skipped (--no-advisor)"], {}))
        sections.append(("ACTORS", ["skipped (--no-advisor)"], {}))
    sections.append(("CI QUEUE", *ci_block(offline, parts.get("ci"))))
    return {"sections": [{"name": n, "lines": l, "data": d} for n, l, d in sections]}


def render(report: dict) -> str:
    out = ["DEBT REPORT — print-only; each line names its source file; a census, not evidence"]
    for section in report["sections"]:
        out.append(f"## {section['name']}")
        out += [f"  {line}" if not line.startswith("  ") else line for line in section["lines"]]
    return "\n".join(out)


def main(argv: list[str] | None = None, parts: dict | None = None) -> int:
    parser = argparse.ArgumentParser(description="One screen of the laboratory's debt, sourced and print-only (no write, no spend).")
    parser.add_argument("--offline", action="store_true", help="no network: skip the PubMed delta and the CI queue")
    parser.add_argument("--no-advisor", action="store_true", help="skip rotation and assignments (about 25 s of the run)")
    parser.add_argument("--root", default=None, help="repository root (default: found from here)")
    parser.add_argument("--json", action="store_true", help="print one JSON object")
    args = parser.parse_args(argv)
    root = Path(args.root) if args.root else repo_root()
    report = build(root, offline=args.offline, advisor=not args.no_advisor, parts=parts)
    print(json.dumps(report, indent=2) if args.json else render(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
