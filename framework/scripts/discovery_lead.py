#!/usr/bin/env python3
"""Validated writer for the discovery ledger: check a lead, stage it, append it with its number.

WHY. In the metabolic batch of 2026-10-19 every lead from every Scientist reached
`discovery_ledger_current.md` through BATCH_COMMIT ops, because the ledger had no writer of
its own: a Scientist wrote the lead into a commit candidate, and the integrator re-typed it as a
record-scoped op and assigned "the next free number" (N2 of
PLAN-HARNESS-FROM-METABOLIC-BATCH-20261020). The ledger is a designated non-canonical
append-only carve-out (state manifest § 3.3), so a validated append is all it needs.

THE SHAPE. A lead is a small JSON spec. Numbers are assigned only at append time, because two
parallel branches that each pick "the next free number" collide (LINT
`DUPLICATE_DISCOVERY_ID`), and two branches that each append at the end of one file conflict
at landing. So:

    on a task branch   discovery_lead.py check lead.json            # validate, write nothing
                       discovery_lead.py stage lead.json --actor scientist-b
                       # -> research/lead_staging/<actor>/<name>.json, committed on the branch
    on main            discovery_lead.py append --staged             # dry run: what would land
                       discovery_lead.py append --staged --apply     # number, append, then
                       bash scripts/legend_commit.sh "<msg>" <ledger>

`append FILE...` also takes specs directly. A staged spec already appended (its path is named
in the entry's Created line) is skipped, so `append --staged --apply` is idempotent and anyone
landing on main may run it. Nothing is deleted. The tool never re-statuses or edits an existing
lead: that is a record-scoped edit (`record_scoped_edit.py`), not an append.

SPEC (JSON object):
    kind              BIO | MOL | REPO | MECH
    title             one line
    tag               DATO / INFERENZA / IPOTESI / ESPANSIONE, or several joined by " + "
    status            open (default) | maturing | promoted-to-CC | parked | refuted
    source            provenance: actor, task, receipt or PMID, and the reading it came from
    causal_statement  what the lead says, with its epistemic qualification
    falsifier         the experiment or observation that would refute it
    transfer_limit    what does NOT transfer to the reference genotype, and why
    links             optional list of extra lines (wikilinks, interconnections)

Scale assumption (designed_for_growth consequence 4): the ledger is read whole once per append
(about 0.8 MB, about 200 leads, on 2026-10-20). A shard of the ledger changes `LEDGER` only.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = "disease-models/{disease}/research/discovery_ledger_current.md"
STAGING = "disease-models/{disease}/research/lead_staging"
KINDS = ("BIO", "MOL", "REPO", "MECH")
TAGS = ("DATO", "INFERENZA", "IPOTESI", "ESPANSIONE")
STATUSES = ("open", "maturing", "promoted-to-CC", "parked", "refuted")
REQUIRED = ("kind", "title", "tag", "source", "causal_statement", "falsifier", "transfer_limit")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
HEADING = re.compile(r"^###\s+(?:[^\w\n]*\s*)?DL-([A-Z]+)-(\d+)\b", re.M)
SECTION = "## Run {day} — leads appended by the validated writer (discovery_lead.py)"


def validate(spec: object, ledger_text: str = "") -> list[str]:
    """Every reason this spec cannot be appended; empty means it can."""
    if not isinstance(spec, dict):
        return ["a lead spec is a JSON object"]
    errors = [f"missing or empty field: {key}" for key in REQUIRED
              if not str(spec.get(key) or "").strip()]
    unknown = set(spec) - set(REQUIRED) - {"status", "links"}
    if unknown:
        errors.append(f"unknown field(s): {', '.join(sorted(unknown))}")
    if spec.get("kind") and spec["kind"] not in KINDS:
        errors.append(f"kind must be one of {', '.join(KINDS)}")
    tags = [t.strip() for t in str(spec.get("tag") or "").split("+") if t.strip()]
    if tags and any(t not in TAGS for t in tags):
        errors.append(f"tag must be {', '.join(TAGS)}, or several joined by ' + '")
    if spec.get("status", "open") not in STATUSES:
        errors.append(f"status must be one of {', '.join(STATUSES)}")
    if "\n" in str(spec.get("title") or ""):
        errors.append("title must be one line")
    links = spec.get("links", [])
    if not isinstance(links, list) or not all(isinstance(x, str) for x in links):
        errors.append("links must be a list of strings")
    text = json.dumps(spec, ensure_ascii=False)
    if EMAIL.search(text):
        errors.append("an e-mail-looking string is not allowed in a lead (release gate)")
    title = str(spec.get("title") or "").strip()
    if title and ledger_text and re.search(
            r"^###\s+DL-[A-Z]+-\d+\s+—\s+" + re.escape(title) + r"\s*$", ledger_text, re.M):
        errors.append("a lead with this exact title is already in the ledger")
    return errors


def next_numbers(ledger_text: str) -> dict[str, int]:
    found: dict[str, int] = {kind: 0 for kind in KINDS}
    for kind, number in HEADING.findall(ledger_text):
        found[kind] = max(found.get(kind, 0), int(number))
    return found


def render(spec: dict, identifier: str, day: str, staged_as: str = "") -> str:
    origin = f" Staged as `{staged_as}`." if staged_as else ""
    lines = [f"### {identifier} — {spec['title'].strip()}", "",
             f"- **Tag:** {spec['tag'].strip()}",
             f"- **Status:** {spec.get('status', 'open')}",
             f"- **Created:** {day} · {spec['source'].strip().rstrip('.')}. Appended by "
             f"`discovery_lead.py`.{origin}",
             f"- **Causal statement:** {spec['causal_statement'].strip()}",
             f"- **Falsifying experiment / counter:** {spec['falsifier'].strip()}",
             f"- **Transfer limit to WWOX:** {spec['transfer_limit'].strip()}"]
    lines += [f"- {line.strip()}" for line in spec.get("links", []) if line.strip()]
    lines.append("- **Not medical advice.**")
    return "\n".join(lines) + "\n"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def staged_specs(root: Path, disease: str) -> list[Path]:
    return sorted((root / STAGING.format(disease=disease)).glob("*/*.json"))


def append(root: Path, disease: str, files: list[Path], *, apply: bool,
           day: str | None = None) -> list[str]:
    """Validate every spec, then append all or none. Returns one line per lead."""
    ledger = root / LEDGER.format(disease=disease)
    day = day or date.today().isoformat()
    with ledger.open("r+" if apply else "r", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX if apply else fcntl.LOCK_SH)
        text = handle.read()
        numbers = next_numbers(text)
        report, blocks, errors = [], [], []
        for path in files:
            try:
                relative = path.resolve().relative_to(root.resolve()).as_posix()
            except ValueError:
                relative = ""
            if relative and f"Staged as `{relative}`" in text:
                report.append(f"SKIP {relative}: already appended")
                continue
            try:
                spec = load(path)
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{path}: {exc}")
                continue
            problems = validate(spec, text)
            if problems:
                errors.append(f"{path}: " + "; ".join(problems))
                continue
            numbers[spec["kind"]] += 1
            identifier = f"DL-{spec['kind']}-{numbers[spec['kind']]:03d}"
            blocks.append(render(spec, identifier, day,
                                 relative if "lead_staging/" in relative else ""))
            report.append(f"{'APPEND' if apply else 'WOULD APPEND'} {identifier} — "
                          f"{spec['title'].strip()}  ({path.name})")
        if errors:
            raise ValueError("nothing appended:\n  " + "\n  ".join(errors))
        if apply and blocks:
            section = SECTION.format(day=day)
            last = [line for line in text.splitlines() if line.startswith("## ")]
            prefix = "" if text.endswith("\n") else "\n"
            if not last or last[-1] != section:
                prefix += f"\n{section}\n"
            handle.seek(0, 2)
            handle.write(prefix + "".join("\n" + block for block in blocks))
            handle.flush()
        return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--disease", default="wwox")
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="validate spec(s) against the ledger; write nothing")
    check.add_argument("specs", nargs="+", type=Path)
    stage = sub.add_parser("stage", help="validate and copy a spec into lead_staging/<actor>/")
    stage.add_argument("spec", type=Path)
    stage.add_argument("--actor", required=True)
    stage.add_argument("--name", help="file name under the actor's directory (default: spec's)")
    app = sub.add_parser("append", help="number and append specs (dry run unless --apply)")
    app.add_argument("specs", nargs="*", type=Path)
    app.add_argument("--staged", action="store_true", help="every staged spec not yet appended")
    app.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.root)
    ledger = root / LEDGER.format(disease=args.disease)
    try:
        if args.command == "check":
            text = ledger.read_text(encoding="utf-8")
            bad = 0
            for path in args.specs:
                problems = validate(load(path), text)
                bad += bool(problems)
                print(f"{'REFUSED' if problems else 'OK'} {path}"
                      + "".join(f"\n  {p}" for p in problems))
            return 1 if bad else 0
        if args.command == "stage":
            spec = load(args.spec)
            problems = validate(spec, ledger.read_text(encoding="utf-8"))
            if problems:
                raise ValueError("; ".join(problems))
            if not re.fullmatch(r"[a-z0-9-]+", args.actor):
                raise ValueError("--actor is an ACTOR_ID such as scientist-b")
            target = (root / STAGING.format(disease=args.disease) / args.actor
                      / (args.name or args.spec.name))
            if target.exists():
                raise ValueError(f"{target} exists; staged specs are never overwritten")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n",
                              encoding="utf-8")
            print(f"STAGED {target.relative_to(root)} — commit it on your branch; it is "
                  "numbered and appended on main by `append --staged --apply`")
            return 0
        files = list(args.specs) + (staged_specs(root, args.disease) if args.staged else [])
        if not files:
            print("NOTHING TO APPEND")
            return 0
        for line in append(root, args.disease, files, apply=args.apply):
            print(line)
        if args.apply:
            print(f"then: bash scripts/legend_commit.sh \"<msg>\" {LEDGER.format(disease=args.disease)}")
        else:
            print("DRY RUN: nothing written; add --apply")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"discovery_lead: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
