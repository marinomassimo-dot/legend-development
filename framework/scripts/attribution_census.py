#!/usr/bin/env python3
"""How were this repository's caught errors caught, and did §21c's output survive the session.

WHY THIS EXISTS
---------------
The 2026-09-09 retrospective had to reconstruct its attribution table by hand from nine
prose diagnoses written in inconsistent vocabularies, and its own analyst called the
reconstruction "contestable at the margins" — over the number that is the most
decision-relevant thing in the record. It is what tells the operator whether to invest in
gates, in blind auditors, or in reader practice.

The aggregate that reconstruction produced was machine 24 · self 23 · blind auditor 5 ·
peer 5 across 57 incidents, which reads as a repository whose machines do the work. On the
six near-errors that were one step from LANDING, the split was self 3 · blind auditor 2 ·
peer 1 · **machine 0**. That inversion is the whole reason `severity_high · of which self`
is a required line and not a nice-to-have.

`session_self_evaluation.md` Part 3 now requires a fixed block at the end of every
diagnosis, and Part 4 sends §21c's `DEFAULTS_TAKEN` and `STOP_LOG` into the task contract
JSON, where per-wave state already survives a session death. This script reads both.

WHAT IT DOES NOT DO
-------------------
It never blocks. A census is a measurement, and a measurement that can fail a build gets
written to pass the build. Exit status reports whether the screen could RUN, not whether
it liked what it found.

🔴 It also cannot see what nobody caught. Every diagnosis is written by the actor whose
work it grades, so an undetected error appears in no list. That is why `undetected_known`
— defects found later and attributed back to an earlier wave — is a required line, and why
a corpus where it is always 0 is reported here as a finding rather than as health.

    python3 framework/scripts/attribution_census.py [--json] [--queue]
    python3 framework/scripts/attribution_census.py --self-test

Exit codes:
  0  the surfaces were screened and the ratios reported (findings do NOT change this)
  2  invalid invocation
  3  nothing could be screened - the result is void, not clean
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVAL_GLOBS = (
    "disease-models/*/research/session_evaluations/*.md",
    "learning/*/*.md",
)
TASK_GLOB = "ledger/tasks/*/*.json"

BLOCK_HEAD = re.compile(r"^ *ATTRIBUTION_CENSUS *$", re.M)
COUNT_FIELDS = ("incidents", "machine", "blind_auditor", "peer", "self",
                "severity_high", "undetected_known")
SEVERITY_SELF = re.compile(
    r"severity_high\s*:\s*(\d+)\s*(?:·|\|)?\s*of\s+which\s+self\s*:\s*(\d+)", re.I)
WAVE_KEY = re.compile(r"^WAVE_(\d+)_RESULT$")
# A contract that records waves in prose instead of structured keys. Reported as its own
# state: calling it "no waves" would flatter the number, and calling it a wave would
# invent a denominator.
WAVE_PROSE = re.compile(r"\bwave\s*\d+\b", re.I)


@dataclass
class Census:
    source: str
    counts: dict[str, int] = field(default_factory=dict)
    severity_self: int | None = None
    complete: bool = False
    inconsistency: str = ""


@dataclass
class WaveRecord:
    contract: str
    wave: str
    has_defaults: bool
    has_stop_log: bool
    structured: bool
    # SINGLE_WAVE is not a lesser shape. A task that runs once records the two keys at the
    # top level of its contract, and the first version of this parser counted only
    # WAVE_n_RESULT keys - so three actors that complied on 2026-09-10 were reported as
    # 0 of 4 and did not appear at all. The instrument was wrong and the record was right.
    shape: str = "WAVE"


@dataclass
class Result:
    verdict: str
    screened_files: int = 0
    screened_bytes: int = 0
    digest: str = ""
    missing: str = ""
    eval_files: int = 0
    censuses: list[Census] = field(default_factory=list)
    waves: list[WaveRecord] = field(default_factory=list)
    unstructured_contracts: list[str] = field(default_factory=list)

    @property
    def complete_censuses(self) -> list[Census]:
        return [c for c in self.censuses if c.complete]


def parse_census_block(text: str, source: str) -> Census | None:
    match = BLOCK_HEAD.search(text)
    if not match:
        return None
    tail = text[match.end(): match.end() + 800]
    census = Census(source=source)
    for name in COUNT_FIELDS:
        found = re.search(rf"\b{name}\s*:\s*(\d+)", tail)
        if found:
            census.counts[name] = int(found.group(1))
    severity = SEVERITY_SELF.search(tail)
    if severity:
        census.counts["severity_high"] = int(severity.group(1))
        census.severity_self = int(severity.group(2))
    census.complete = (
        all(name in census.counts for name in COUNT_FIELDS)
        and census.severity_self is not None
    )
    # Mirror REV-EXPOST-20260911-001 F5: the first version parsed `incidents: 3 / machine: 5 /
    # severity_high: 1 / of which self: 4` as complete and printed "4/1". The block is the number
    # the operator invests by; arithmetic that cannot be true is INCOMPLETE, with the reason.
    if census.complete:
        c = census.counts
        catchers = c["machine"] + c["blind_auditor"] + c["peer"] + c["self"]
        if catchers != c["incidents"]:
            census.complete = False
            census.inconsistency = (f"catchers sum to {catchers}, incidents say {c['incidents']}")
        elif census.severity_self > c["severity_high"]:
            census.complete = False
            census.inconsistency = (f"severity_high self {census.severity_self} exceeds "
                                    f"severity_high {c['severity_high']}")
        elif c["severity_high"] > c["incidents"]:
            census.complete = False
            census.inconsistency = (f"severity_high {c['severity_high']} exceeds incidents "
                                    f"{c['incidents']}")
    return census


def screen(root: Path = ROOT) -> Result:
    result = Result(verdict="SCREENED")
    digest = hashlib.sha256()

    eval_paths: list[Path] = []
    for pattern in EVAL_GLOBS:
        eval_paths.extend(sorted(root.glob(pattern)))
    task_paths = sorted(root.glob(TASK_GLOB))

    if not eval_paths and not task_paths:
        return Result(
            verdict="INSUFFICIENT_DATA",
            missing=f"no session evaluations and no task contracts under {root}",
        )

    for path in eval_paths:
        raw = path.read_bytes()
        digest.update(raw)
        result.screened_bytes += len(raw)
        result.screened_files += 1
        text = raw.decode("utf-8", errors="replace")
        if "ATTRIBUTION_CENSUS" not in text:
            # Only files that are diagnoses count in the denominator, and the only
            # machine-visible marker of one is that it lives in session_evaluations/.
            if "session_evaluations" in str(path):
                result.eval_files += 1
                result.censuses.append(Census(source=str(path.relative_to(root))))
            continue
        result.eval_files += 1
        census = parse_census_block(text, str(path.relative_to(root)))
        if census:
            result.censuses.append(census)

    for path in task_paths:
        raw = path.read_bytes()
        digest.update(raw)
        result.screened_bytes += len(raw)
        result.screened_files += 1
        try:
            contract = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        relative = str(path.relative_to(root))
        structured = [key for key in contract if WAVE_KEY.match(key)]
        for key in sorted(structured):
            body = contract[key]
            serialised = json.dumps(body) if not isinstance(body, str) else body
            result.waves.append(WaveRecord(
                contract=relative, wave=key,
                has_defaults="DEFAULTS_TAKEN" in serialised,
                has_stop_log="STOP_LOG" in serialised,
                structured=True,
            ))
        if structured:
            continue
        top_level = "DEFAULTS_TAKEN" in contract or "STOP_LOG" in contract
        if top_level:
            result.waves.append(WaveRecord(
                contract=relative, wave="(single wave, top level)",
                has_defaults="DEFAULTS_TAKEN" in contract,
                has_stop_log="STOP_LOG" in contract,
                structured=True, shape="SINGLE_WAVE",
            ))
        elif WAVE_PROSE.search(json.dumps(contract)):
            result.unstructured_contracts.append(relative)

    result.digest = digest.hexdigest()
    return result


def render(result: Result, queue: bool) -> str:
    if result.verdict == "INSUFFICIENT_DATA":
        return f"INSUFFICIENT_DATA: {result.missing}"

    lines = [
        f"screened: files={result.screened_files} bytes={result.screened_bytes} "
        f"digest={result.digest[:16]}",
    ]
    complete = result.complete_censuses
    lines.append(f"diagnoses carrying a parseable census: "
                 f"{len(complete)}/{result.eval_files}")

    if complete:
        totals = {name: sum(c.counts.get(name, 0) for c in complete)
                  for name in COUNT_FIELDS}
        severity_self = sum(c.severity_self or 0 for c in complete)
        lines.append(
            f"  incidents={totals['incidents']}  machine={totals['machine']}  "
            f"blind_auditor={totals['blind_auditor']}  peer={totals['peer']}  "
            f"self={totals['self']}"
        )
        high = totals["severity_high"]
        ratio = f"{severity_self}/{high}" if high else "0/0"
        lines.append(f"  severity_high self-caught: {ratio}   "
                     f"undetected_known: {totals['undetected_known']}")
        if high and totals["undetected_known"] == 0:
            lines.append("  [FINDING] undetected_known is 0 across every census - "
                         "the line exists because that is unlikely, not because it is good")

    structured = [w for w in result.waves if w.structured]
    both = [w for w in structured if w.has_defaults and w.has_stop_log]
    single = [w for w in structured if w.shape == "SINGLE_WAVE"]
    lines.append(f"waves carrying DEFAULTS_TAKEN and STOP_LOG: "
                 f"{len(both)}/{len(structured)}"
                 + (f"  (of which {len(single)} single-wave contracts recording them at "
                    f"top level)" if single else ""))
    if result.unstructured_contracts:
        lines.append(
            f"  contracts recording waves in prose rather than WAVE_n_RESULT keys: "
            f"{len(result.unstructured_contracts)} (their waves are not counted above)"
        )

    if queue:
        for census in result.censuses:
            if not census.complete:
                state = "ABSENT" if not census.counts else (
                    "INCONSISTENT" if census.inconsistency else "INCOMPLETE")
                missing = [f for f in COUNT_FIELDS if f not in census.counts]
                lines.append(f"  [CENSUS_{state}] {census.source}"
                             + (f" missing={missing}" if missing else "")
                             + (f" {census.inconsistency}" if census.inconsistency else ""))
        for wave in structured:
            if not (wave.has_defaults and wave.has_stop_log):
                absent = [n for n, present in
                          (("DEFAULTS_TAKEN", wave.has_defaults),
                           ("STOP_LOG", wave.has_stop_log)) if not present]
                lines.append(f"  [WAVE_KEYS_ABSENT] {wave.contract} {wave.wave} "
                             f"missing={absent}")
        for contract in result.unstructured_contracts:
            lines.append(f"  [WAVES_UNSTRUCTURED] {contract}")
    return "\n".join(lines)


def self_test() -> int:
    """Calls `screen`, the entry point, on fixtures AND on the live repository."""
    import tempfile

    passed, failed = 0, 0

    def check(name: str, condition: bool) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"  ok   {name}")
        else:
            failed += 1
            print(f"  FAIL {name}")

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        check("an empty tree is INSUFFICIENT_DATA, not clean",
              screen(root).verdict == "INSUFFICIENT_DATA")

        evals = root / "disease-models" / "wwox" / "research" / "session_evaluations"
        evals.mkdir(parents=True)
        (evals / "full.md").write_text(
            "prose\n\nATTRIBUTION_CENSUS\nincidents: 10\nmachine: 4   blind_auditor: 1   "
            "peer: 1   self: 4\nseverity_high: 2   of which self: 1\n"
            "undetected_known: 0\n", encoding="utf-8")
        (evals / "absent.md").write_text("a diagnosis with no census\n", encoding="utf-8")
        (evals / "partial.md").write_text(
            "ATTRIBUTION_CENSUS\nincidents: 3\nmachine: 3\n", encoding="utf-8")

        result = screen(root)
        check("a complete block parses and an incomplete one does not count",
              len(result.complete_censuses) == 1 and result.eval_files == 3)
        check("the two-value severity line is read as two values",
              result.complete_censuses[0].severity_self == 1
              and result.complete_censuses[0].counts["severity_high"] == 2)

        tasks = root / "ledger" / "tasks" / "actor"
        tasks.mkdir(parents=True)
        (tasks / "T1.json").write_text(json.dumps({
            "TASK_ID": "T1",
            "WAVE_1_RESULT": {"outcome": "closed",
                              "DEFAULTS_TAKEN": [], "STOP_LOG": []},
            "WAVE_2_RESULT": {"outcome": "closed", "DEFAULTS_TAKEN": []},
        }), encoding="utf-8")
        (tasks / "T2.json").write_text(json.dumps({
            "TASK_ID": "T2", "TASK_CLAIM": {"wave": "wave 2 of the lot"},
        }), encoding="utf-8")
        result = screen(root)
        structured = [w for w in result.waves if w.structured]
        check("a wave missing STOP_LOG is not counted as compliant",
              len(structured) == 2
              and len([w for w in structured if w.has_defaults and w.has_stop_log]) == 1)
        check("a contract recording waves in prose is its own state, not a zero",
              result.unstructured_contracts == ["ledger/tasks/actor/T2.json"])
        check("an empty census block is reported ABSENT, not counted",
              any(not c.complete for c in result.censuses))

    live = screen()
    check("the entry point runs against the live repository",
          live.verdict == "SCREENED" and live.screened_files > 0)

    print(f"\nself-test: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--queue", action="store_true", help="list what is missing")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    result = screen(args.root)
    if args.json:
        structured = [w for w in result.waves if w.structured]
        print(json.dumps({
            "verdict": result.verdict,
            "screened": {"files": result.screened_files,
                         "bytes": result.screened_bytes,
                         "digest": result.digest},
            "diagnoses": result.eval_files,
            "diagnoses_with_census": len(result.complete_censuses),
            "waves": len(structured),
            "waves_with_both_keys": len(
                [w for w in structured if w.has_defaults and w.has_stop_log]),
            "contracts_with_unstructured_waves": result.unstructured_contracts,
            "missing": result.missing,
        }, indent=1))
    else:
        print(render(result, args.queue))
    return 3 if result.verdict == "INSUFFICIENT_DATA" else 0


if __name__ == "__main__":
    sys.exit(main())
