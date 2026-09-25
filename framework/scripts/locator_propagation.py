#!/usr/bin/env python3
"""LOCATOR PROPAGATION — a correction that has not yet reached the locator it retires.

## The defect

2026-09-14 (`HARNESS-P-20260914` P5). Verification wave W4 corrected a bar count from six to
twelve. The correction reached the discovery ledger, a dossier and a queue entry, and never
reached the two persisted locators: at `4c1a5dd`, `PMID33058734.json` entries[27] and
entries[29] still asserted "six bars" with no `contradicts_locator`. The batch report of that
day even wrote the pending amendment into a table cell. Nothing counted it, because an
obligation had no form a check could read, so it sat for days until someone stumbled on it.

What already works is the other half: `snippet` and `proposition` are
`locator_contradiction_audit.REVISION_FIELDS`, so changing one needs a declared
`contradicts_locator` and a blind audit, and `--history` / `--working-tree` report a revision
made without one. What was missing is the obligation BEFORE the revision exists.

## The declaration — one line, written where the correction is recorded

    LOCATOR_PROPAGATION_OBLIGATION: PMID<n> entries[<i>] <snippet|proposition> retired="<text>" [source=<ID>]
    LOCATOR_PROPAGATION_WAIVED:     PMID<n> entries[<i>] <snippet|proposition> retired="<text>" reason="<why>"

`retired` is a fragment the corrected locator must no longer carry — the retired claim, not the
new one, because the new wording is the amending actor's to choose. The line may sit in any
Markdown or JSON file under `disease-models/<disease>/` or `ledger/`: a dispositions table, a
batch report, a task record. Duplicates across files count once.

## The states, resolved against the manifest (read-only)

- `OPEN` — the field still contains the retired fragment (case and whitespace folded).
- `DISCHARGED` — the fragment is gone AND the entry declares `contradicts_locator`.
- `UNDECLARED_DISCHARGE` — the fragment is gone and no revision is declared: the text moved
  without the audit trail the contradiction procedure exists for.
- `WAIVED` — a waiver line with a reason names the same obligation.
- `UNRESOLVABLE` — no such manifest, or no such entry.

A declaration that does not parse is `MALFORMED`, reported with `file:line`, never dropped.

## What it does not do

It writes no manifest — applying the amendment is the science actors' act, through the
contradiction procedure. It does not infer obligations from prose: a heuristic over
"still carries the retired …" wording was measured on this corpus and rejected (task record
`HARNESS-P-20260914`, MEASUREMENTS.P5). Exit 0 unless `--fail-on-open` and something is OPEN.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locator_contradiction_audit import REVISION_FIELDS  # noqa: E402

OPEN = "OPEN"
DISCHARGED = "DISCHARGED"
UNDECLARED_DISCHARGE = "UNDECLARED_DISCHARGE"
WAIVED = "WAIVED"
UNRESOLVABLE = "UNRESOLVABLE"

KEYWORDS = re.compile(r"LOCATOR_PROPAGATION_(OBLIGATION|WAIVED):")
_FIELDS = "|".join(re.escape(name) for name in REVISION_FIELDS)
DECLARATION = re.compile(
    r"LOCATOR_PROPAGATION_(?P<kind>OBLIGATION|WAIVED):\s*PMID\s?(?P<pmid>\d+)\s+"
    r"entries\[(?P<entry>\d+)\]\s+(?P<field>" + _FIELDS + r")\s+"
    r"retired=\"(?P<retired>[^\"]+)\""
    r"(?:\s+source=(?P<source>[^\s|`]+))?"
    r"(?:\s+reason=\"(?P<reason>[^\"]+)\")?")


def fold(text: str) -> str:
    return " ".join(str(text).split()).casefold()


@dataclass
class Obligation:
    pmid: str
    entry: int
    field: str
    retired: str
    source: str
    where: str
    state: str = ""
    detail: str = ""

    @property
    def key(self) -> tuple[str, int, str, str]:
        return (self.pmid, self.entry, self.field, fold(self.retired))

    def line(self) -> str:
        return (f"{self.state} PMID{self.pmid} entries[{self.entry}].{self.field} "
                f"retired={self.retired!r} ({self.where}): {self.detail}")


@dataclass
class ScanResult:
    obligations: list[Obligation] = field(default_factory=list)
    malformed: list[str] = field(default_factory=list)

    def count(self, state: str) -> int:
        return sum(1 for item in self.obligations if item.state == state)

    def summary(self) -> str:
        return (f"obligations: {len(self.obligations)} | open: {self.count(OPEN)} | discharged: "
                f"{self.count(DISCHARGED)} | undeclared_discharge: "
                f"{self.count(UNDECLARED_DISCHARGE)} | waived: {self.count(WAIVED)} | "
                f"unresolvable: {self.count(UNRESOLVABLE)} | malformed: {len(self.malformed)}")


def declaration_files(root: Path, disease: str) -> list[Path]:
    bases = [root / "disease-models" / disease, root / "ledger"]
    out: list[Path] = []
    for base in bases:
        if base.is_dir():
            out.extend(sorted(p for p in base.rglob("*")
                              if p.suffix in {".md", ".json"} and p.is_file()
                              and "deepdive_manifests" not in p.parts))
    return out


def read_declarations(root: Path, disease: str) -> tuple[dict, dict, list[str]]:
    obligations: dict[tuple, Obligation] = {}
    waivers: dict[tuple, Obligation] = {}
    malformed: list[str] = []
    for path in declaration_files(root, disease):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if "LOCATOR_PROPAGATION_" not in text:
            continue
        rel = path.relative_to(root).as_posix()
        for number, raw in enumerate(text.splitlines(), start=1):
            line = raw.replace('\\"', '"')
            for hit in KEYWORDS.finditer(line):
                match = DECLARATION.match(line, hit.start())
                where = f"{rel}:{number}"
                if match is None:
                    malformed.append(f"{where}: {line[hit.start():hit.start() + 160]}")
                    continue
                item = Obligation(match["pmid"], int(match["entry"]), match["field"],
                                  match["retired"], match["source"] or "", where,
                                  detail=match["reason"] or "")
                target = waivers if match["kind"] == "WAIVED" else obligations
                if match["kind"] == "WAIVED" and not item.detail:
                    malformed.append(f"{where}: a waiver must state reason=\"…\"")
                    continue
                target.setdefault(item.key, item)
    return obligations, waivers, malformed


def resolve(item: Obligation, root: Path, disease: str, cache: dict) -> None:
    path = root / "disease-models" / disease / "research" / "deepdive_manifests" / f"PMID{item.pmid}.json"
    if path not in cache:
        try:
            cache[path] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            cache[path] = error
    manifest = cache[path]
    if not isinstance(manifest, dict):
        item.state, item.detail = UNRESOLVABLE, f"no readable manifest at {path.name}"
        return
    entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
    if item.entry >= len(entries) or not isinstance(entries[item.entry], dict):
        item.state, item.detail = UNRESOLVABLE, f"{path.name} has no entries[{item.entry}]"
        return
    locator = entries[item.entry]
    if fold(item.retired) in fold(locator.get(item.field, "")):
        item.state = OPEN
        item.detail = "the locator still carries the retired text" + (
            f"; correction recorded by {item.source}" if item.source else "")
    elif isinstance(locator.get("contradicts_locator"), dict):
        item.state, item.detail = DISCHARGED, "retired text gone; revision declared"
    else:
        item.state = UNDECLARED_DISCHARGE
        item.detail = ("retired text gone with no contradicts_locator — declare the revision "
                       "(locator_contradiction_audit.py --history reports it too)")


def scan(root: Path, disease: str) -> ScanResult:
    obligations, waivers, malformed = read_declarations(root, disease)
    result = ScanResult(malformed=malformed)
    cache: dict = {}
    for key in sorted(set(obligations) | set(waivers)):
        waiver = waivers.get(key)
        item = obligations.get(key) or waiver
        if waiver is not None:
            item.state, item.detail = WAIVED, f"waived at {waiver.where}: {waiver.detail}"
        else:
            resolve(item, root, disease, cache)
        result.obligations.append(item)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[2]))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--fail-on-open", action="store_true")
    args = parser.parse_args(argv)
    result = scan(Path(args.root), args.disease)
    if args.json:
        print(json.dumps({"obligations": [vars(o) for o in result.obligations],
                          "malformed": result.malformed}, ensure_ascii=False, indent=1))
    else:
        for item in result.obligations:
            print(item.line())
        for where in result.malformed:
            print(f"MALFORMED {where}")
        print(result.summary())
    return 1 if args.fail_on_open and result.count(OPEN) else 0


if __name__ == "__main__":
    raise SystemExit(main())
