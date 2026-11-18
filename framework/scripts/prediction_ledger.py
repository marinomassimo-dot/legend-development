#!/usr/bin/env python3
"""Prediction ledger: find every frozen prediction in git and check what git CAN prove.

    python3 framework/scripts/prediction_ledger.py sweep [--under PATH] [--out FILE]
    python3 framework/scripts/prediction_ledger.py check LEDGER.tsv [--receipts FILE] [--strict]
    python3 framework/scripts/prediction_ledger.py guard LEDGER.tsv --outcome PATH [--require PATH[=SHA256]]...

WHY
---
A prediction counts only if it was fixed before its outcome could be read. Today that rests on
the sentence "frozen before reading" inside a file. This tool separates what git can show from
what only a declaration can carry (2026-11-16, MEETING f4lqagml, item 1).

`sweep` is read-only. It lists candidate files (a prediction/frozen file NAME, or a text that says
"frozen before" / "preregistered") with the commit that first added each one and the sha256 of
the blob then. It writes a candidates TSV: a candidate is a file, not yet a prediction. A person
writes one ledger row per prediction.

`check` reads a ledger TSV and, per row, tests:
  - freeze_commit exists and the statement file at that commit hashes to freeze_blob_sha256;
  - the statement file is unchanged since (EDITED is a warning; --strict makes it fatal);
  - when a row declares `freeze_utc_declared` and the freeze commit is LATER than that, the declared time is not shown by git
    (a rebase or cherry-pick moves a commit's time): printed as a warning, never as proof; freeze commits should be merged, not rebased;
  - the outcome file is NOT in the tree at the freeze commit (a row whose `blindness` cell says `declared`
    states that the table is public and already there: reported as a warning, blindness declared, not shown);
  - the freeze commit precedes the outcome commit: `yes` (ancestor), `same_commit`, `not_ancestor`
    or `unknown` (no outcome commit yet). It never infers an order it cannot see;
  - no read receipt for outcome_study_id (PMIDs or DOIs, `;`-separated) is dated before the freeze commit;
  - predictor and scorer, when both are declared, are different.
Who the predictor was, what it read outside the repository, and model memory of a published
paper are NOT checkable here: every paper_content row is printed with that label.

`guard` answers one question before an outcome table is opened or created: it prints `OUTCOME_MAY_OPEN: ...` (exit 0) only
when every ledger row naming the table holds a real freeze commit that is an ancestor of HEAD and not HEAD, every `--require`d
file (the rule, each freeze, each baseline) is committed and unmodified, and a table that already exists is the sealed one
(its digest recorded in the ledger and equal). Otherwise it prints `OUTCOME_REFUSED: <reason>` lines and exits 1. Once the table
is committed, `check` also requires its digest (outcome_sha256) to be recorded and equal to the blob at outcome_commit.

Exit codes: 0 no violation (warnings allowed) · 1 a violation (or a refusal by `guard`) · 2 invalid invocation or ledger.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_UNDER = "disease-models/wwox/research/drug_repurposing"
DEFAULT_RECEIPTS = "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
NAME_RE = re.compile(r"(prediction|predictions|frozen)[^/]*\.(md|tsv|txt)$|/frozen/", re.I)
TEXT_PATTERN = r"frozen before|predictions? frozen|preregistered|pre-registered"
TEXT_EXT = (".md", ".tsv", ".txt")

COLUMNS = ["pred_id", "package", "statement_ref", "freeze_commit", "freeze_blob_sha256", "kind",
           "outcome_ref", "outcome_study_id", "outcome_commit", "predictor", "scorer",
           "scoring_rule_ref", "status", "notes"]
OPTIONAL_COLUMNS = ["blindness", "outcome_sha256", "freeze_utc_declared"]   # `declared` says the outcome table is public and in the tree at the freeze: blindness is then a declaration, not shown by git
BLINDNESS = {"", "shown", "declared"}   # `outcome_sha256` is the digest of the sealed outcome table (required once outcome_commit is set)
KINDS = {"", "paper_content", "generative"}
STATUSES = {"", "unclassified", "open", "held", "failed", "mixed", "unscorable"}
CANDIDATE_COLUMNS = ["path", "via", "first_add_commit", "first_add_utc", "blob_sha256_at_add",
                     "commits_touching"]


def git(root: Path, *args: str, check: bool = True) -> str:
    done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if check and done.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {done.stderr.strip()}")
    return done.stdout


def git_ok(root: Path, *args: str) -> bool:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True).returncode == 0


def blob_at(root: Path, commit: str, path: str) -> bytes | None:
    done = subprocess.run(["git", "-C", str(root), "show", f"{commit}:{path}"], capture_output=True)
    return done.stdout if done.returncode == 0 else None


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def commit_utc(root: Path, commit: str) -> datetime:
    stamp = git(root, "show", "-s", "--format=%cI", commit).strip()
    return datetime.fromisoformat(stamp).astimezone(timezone.utc)


def first_adds(root: Path, under: str) -> dict[str, tuple[str, str]]:
    """path -> (commit, committer date) of the OLDEST commit that added it, in one pass."""
    out = git(root, "log", "--diff-filter=A", "--name-only", "--format=@@%H %cI", "--", under)
    found: dict[str, tuple[str, str]] = {}
    current = None
    for line in out.splitlines():
        if line.startswith("@@"):
            current = tuple(line[2:].split(" ", 1))
        elif line.strip() and current:
            found[line.strip()] = current  # log runs newest first, so the last write is the oldest
    return found


def touching(root: Path, under: str) -> dict[str, int]:
    out = git(root, "log", "--name-only", "--format=@@%H", "--", under)
    counts: dict[str, int] = {}
    for line in out.splitlines():
        if line.strip() and not line.startswith("@@"):
            counts[line.strip()] = counts.get(line.strip(), 0) + 1
    return counts


def sweep(root: Path, under: str) -> list[dict[str, str]]:
    by_name = {p for p in git(root, "ls-files", "--", under).splitlines() if NAME_RE.search(p)}
    grep = subprocess.run(["git", "-C", str(root), "grep", "-ilE", TEXT_PATTERN, "--", under],
                          capture_output=True, text=True)
    by_text = {p for p in grep.stdout.splitlines() if p.endswith(TEXT_EXT)}
    adds, counts = first_adds(root, under), touching(root, under)
    rows = []
    for path in sorted(by_name | by_text):
        if path not in adds:
            continue
        commit, when = adds[path]
        blob = blob_at(root, commit, path)
        via = "name+text" if path in by_name and path in by_text else "name" if path in by_name else "text"
        rows.append({"path": path, "via": via, "first_add_commit": commit, "first_add_utc": when,
                     "blob_sha256_at_add": sha256(blob) if blob is not None else "",
                     "commits_touching": str(counts.get(path, 0))})
    return rows


def write_tsv(rows: list[dict[str, str]], columns: list[str], out) -> None:
    writer = csv.DictWriter(out, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)


def read_ledger(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"ledger lacks columns: {', '.join(missing)}")
        return [{c: (row.get(c) or "").strip() for c in COLUMNS + OPTIONAL_COLUMNS} for row in reader]


def study_ids(text: str) -> list[str]:
    """`PMID 123; doi:10.1/x` -> ['123', '10.1/x'] (lower case, prefixes removed, empty parts dropped)."""
    out = []
    for part in text.split(";"):
        part = part.strip().lower()
        for prefix in ("pmid", "doi"):
            if part.startswith(prefix):
                part = part[len(prefix):].lstrip(": ")
        if part:
            out.append(part)
    return out


def receipt_times(path: Path, study: str) -> list[tuple[datetime, str, str, str]]:
    """(event time, study id, event id, record kind) of the receipts naming ANY of the `;`-separated study ids."""
    wanted = set(study_ids(study))
    if not wanted or not path.is_file():
        return []
    found = []
    with path.open() as handle:
        for line in handle:
            if not any(w in line.lower() for w in wanted):
                continue
            rec = json.loads(line)
            ids = {str(v).lower() for v in (rec.get("study_id") or {}).values() if v}
            if wanted & ids and rec.get("event_at"):
                found.append((datetime.fromisoformat(rec["event_at"]).astimezone(timezone.utc),
                              ",".join(sorted(wanted & ids)), rec.get("event_id", ""), rec.get("record_kind", "")))
    return found


def check_row(root: Path, row: dict[str, str], receipts: Path) -> tuple[list[str], list[str], str]:
    """-> (violations, warnings, freeze_precedes_outcome)."""
    bad: list[str] = []
    warn: list[str] = []
    order = "unknown"
    if row["kind"] not in KINDS:
        bad.append(f"kind {row['kind']!r} not in {sorted(KINDS - {''})}")
    if row["status"] not in STATUSES:
        bad.append(f"status {row['status']!r} not in {sorted(STATUSES - {''})}")
    blindness = row.get("blindness", "")
    if blindness not in BLINDNESS:
        bad.append(f"blindness {blindness!r} not in {sorted(BLINDNESS - {''})}")
    if row["kind"] == "paper_content":
        warn.append("memory of the paper not excluded")
    freeze = row["freeze_commit"]
    statement = re.split(r"[#\s]", row["statement_ref"].strip(), maxsplit=1)[0]   # `path#anchor` or `path anchor`: repository paths hold no space
    if not freeze or not statement:
        return bad + ["freeze_commit and statement_ref are required"], warn, order
    if not git_ok(root, "cat-file", "-e", f"{freeze}^{{commit}}"):
        return bad + [f"freeze_commit {freeze[:12]} not found"], warn, order
    frozen_blob = blob_at(root, freeze, statement)
    if frozen_blob is None:
        bad.append(f"{statement} is not in the tree at the freeze commit")
    elif row["freeze_blob_sha256"] and sha256(frozen_blob) != row["freeze_blob_sha256"]:
        bad.append("freeze_blob_sha256 does not match the file at the freeze commit")
    elif not row["freeze_blob_sha256"]:
        warn.append("freeze_blob_sha256 not recorded")
    now_blob = blob_at(root, "HEAD", statement)
    if frozen_blob is not None and now_blob is not None and now_blob != frozen_blob:
        warn.append("EDITED: the statement file differs from its frozen blob")
    outcome = re.split(r"[#\s]", row["outcome_ref"].strip(), maxsplit=1)[0]
    if outcome and blob_at(root, freeze, outcome) is not None:
        if blindness == "declared":
            warn.append(f"outcome_in_tree_at_freeze = yes (blindness declared, not shown): {outcome}")
        else:
            bad.append(f"outcome file {outcome} is already in the tree at the freeze commit")
    if row["outcome_commit"]:
        if not git_ok(root, "cat-file", "-e", f"{row['outcome_commit']}^{{commit}}"):
            bad.append(f"outcome_commit {row['outcome_commit'][:12]} not found")
        else:
            full_f = git(root, "rev-parse", freeze).strip()
            full_o = git(root, "rev-parse", row["outcome_commit"]).strip()
            if full_f == full_o:
                order = "same_commit"
                warn.append("freeze and outcome share one commit: order is declared, not shown")
            elif git_ok(root, "merge-base", "--is-ancestor", full_f, full_o):
                order = "yes"
            else:
                order = "not_ancestor"
                bad.append("the freeze commit is not an ancestor of the outcome commit")
    if row["outcome_commit"] and outcome and git_ok(root, "cat-file", "-e", f"{row['outcome_commit']}^{{commit}}"):
        table = blob_at(root, row["outcome_commit"], outcome)
        recorded = row.get("outcome_sha256", "")
        if table is None:
            bad.append(f"outcome table {outcome} is not in the tree at the outcome commit")
        elif not recorded:
            bad.append("the outcome table is committed but its digest (outcome_sha256) is not recorded")
        elif sha256(table) != recorded:
            bad.append("outcome_sha256 does not match the table at the outcome commit")
    stamp = commit_utc(root, freeze)
    declared = row.get("freeze_utc_declared", "")
    if declared:
        try:
            said = datetime.fromisoformat(declared.replace("Z", "+00:00")).astimezone(timezone.utc)
        except ValueError:
            bad.append(f"freeze_utc_declared {declared!r} is not an ISO time")
        else:
            if stamp > said:
                warn.append(f"freeze time declared, not shown by git (rebased): declared {said.isoformat()}, "
                            f"the freeze commit's own time is {stamp.isoformat()}")
    early = [r for r in receipt_times(receipts, row["outcome_study_id"]) if r[0] < stamp]
    if early:
        studies = sorted({r[1] for r in early})
        first = min(early)
        text = (f"{len(studies)} outcome source(s) have a read receipt dated before the freeze {stamp.isoformat()}: "
                f"{'; '.join(studies)} (earliest {first[0].isoformat()}, {first[2]}, {first[3] or 'kind not stated'}); "
                "the receipt does not say who read it")
        if blindness == "declared":
            warn.append(text + " (blindness declared, not shown)")
        else:
            bad.append(text)
    if row["predictor"] and row["scorer"] and row["predictor"] == row["scorer"]:
        bad.append("predictor and scorer are the same actor")
    if not row["predictor"] or not row["scorer"]:
        warn.append("predictor/scorer not both declared")
    return bad, warn, order


def guard(root: Path, ledger: Path, outcome: str, requires: list[str], receipts: Path) -> tuple[bool, list[str]]:
    """May the outcome table be opened? Every ledger row naming it must hold a real, earlier freeze; every required file
    (rule, both freezes, a baseline) must be committed, unmodified and in HEAD's history; a table that already exists must be
    the sealed one (its digest recorded and equal). A table not created yet is allowed: it is created AFTER this line."""
    problems: list[str] = []
    try:
        rows = [r for r in read_ledger(ledger) if r["outcome_ref"].split("#", 1)[0] == outcome]
    except (OSError, ValueError, csv.Error) as exc:
        return False, [f"invalid ledger: {exc}"]
    head = git(root, "rev-parse", "HEAD").strip()
    if not rows:
        problems.append(f"no ledger row names {outcome} as its outcome: nothing was frozen against it")
    freezes = []
    for row in rows:
        bad, _, _ = check_row(root, dict(row, outcome_commit=""), receipts)
        problems += [f"{row['pred_id']}: {b}" for b in bad]
        if not row["freeze_blob_sha256"]:
            problems.append(f"{row['pred_id']}: freeze_blob_sha256 is not recorded")
        full = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", f"{row['freeze_commit']}^{{commit}}"],
                              capture_output=True, text=True).stdout.strip()
        if not full:
            continue
        freezes.append(full[:12])
        if full == head:
            problems.append(f"{row['pred_id']}: the freeze commit is HEAD itself: the outcome would be opened in the freezing commit")
        elif not git_ok(root, "merge-base", "--is-ancestor", full, head):
            problems.append(f"{row['pred_id']}: the freeze commit is not an ancestor of HEAD")
    table = root / outcome
    if table.is_file():
        digests = {r["outcome_sha256"] for r in rows}
        if "" in digests or not digests:
            problems.append(f"{outcome} exists but its digest is not recorded in the ledger")
        elif sha256(table.read_bytes()) not in digests:
            problems.append(f"{outcome} differs from the sealed digest recorded in the ledger")
    present = []
    for spec in requires:
        path, _, pin = spec.partition("=")
        blob = blob_at(root, "HEAD", path)
        if blob is None:
            problems.append(f"required file {path} is not committed in HEAD")
            continue
        if (root / path).read_bytes() != blob:
            problems.append(f"required file {path} differs from HEAD (uncommitted change)")
        if pin and sha256(blob) != pin.lower():
            problems.append(f"required file {path} has sha256 {sha256(blob)}, not the pinned {pin.lower()}")
        present.append(path)
    if problems:
        return False, problems
    return True, [f"OUTCOME_MAY_OPEN: {outcome}; ledger rows {len(rows)}; freeze commits {','.join(sorted(set(freezes)))}; "
                  f"required present and unmodified: {', '.join(present) or 'none required'}; HEAD {head[:12]}"]


def run_check(root: Path, ledger: Path, receipts: Path, strict: bool) -> int:
    try:
        rows = read_ledger(ledger)
    except (OSError, ValueError, csv.Error) as exc:
        print(f"invalid ledger: {exc}", file=sys.stderr)
        return 2
    ids = [r["pred_id"] for r in rows]
    dup = sorted({i for i in ids if ids.count(i) > 1 or not i})
    if dup:
        print(f"invalid ledger: empty or duplicate pred_id: {dup}", file=sys.stderr)
        return 2
    violations = 0
    counts: dict[str, int] = {}
    for row in rows:
        bad, warn, order = check_row(root, row, receipts)
        if strict:
            bad, warn = bad + [w for w in warn if w.startswith("EDITED")], [w for w in warn if not w.startswith("EDITED")]
        counts[order] = counts.get(order, 0) + 1
        verdict = "VIOLATION" if bad else "ok"
        violations += bool(bad)
        print(f"{row['pred_id']}\t{verdict}\tfreeze_precedes_outcome={order}")
        for text in bad:
            print(f"  VIOLATION: {text}")
        for text in warn:
            print(f"  warning: {text}")
    print(f"rows {len(rows)}; violations {violations}; order " +
          ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 1 if violations else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=".", help="repository root (default: current directory)")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sw = sub.add_parser("sweep", help="list candidate files with their first-add commit (read-only)")
    sw.add_argument("--under", default=DEFAULT_UNDER)
    sw.add_argument("--out", help="write the candidates TSV here (default: standard output)")
    ck = sub.add_parser("check", help="check a ledger TSV against git and the receipts ledger")
    ck.add_argument("ledger")
    ck.add_argument("--receipts", default=DEFAULT_RECEIPTS)
    ck.add_argument("--strict", action="store_true", help="a statement edited after its freeze is fatal")
    gd = sub.add_parser("guard", help="may this outcome table be opened? refuses unless the freezes, the digest and the required files exist")
    gd.add_argument("ledger")
    gd.add_argument("--outcome", required=True, help="repository path of the outcome table")
    gd.add_argument("--require", action="append", default=[], metavar="PATH[=SHA256]",
                    help="a file that must be committed and unmodified (rule, freezes, baselines); repeatable")
    gd.add_argument("--receipts", default=DEFAULT_RECEIPTS)
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    if args.cmd == "guard":
        receipts = Path(args.receipts)
        ok, lines = guard(root, Path(args.ledger), args.outcome, args.require, receipts if receipts.is_absolute() else root / receipts)
        for line in lines:
            print(line if ok else f"OUTCOME_REFUSED: {line}")
        return 0 if ok else 1
    if args.cmd == "sweep":
        rows = sweep(root, args.under)
        if args.out:
            with open(args.out, "w", newline="") as handle:
                write_tsv(rows, CANDIDATE_COLUMNS, handle)
        else:
            write_tsv(rows, CANDIDATE_COLUMNS, sys.stdout)
        print(f"candidates {len(rows)}", file=sys.stderr)
        return 0
    receipts = Path(args.receipts)
    return run_check(root, Path(args.ledger), receipts if receipts.is_absolute() else root / receipts, args.strict)


if __name__ == "__main__":
    sys.exit(main())
