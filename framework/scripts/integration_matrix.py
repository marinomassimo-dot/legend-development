#!/usr/bin/env python3
"""Simulate an ordered integration of candidate branches and measure what only composition moves.

🔴 **This tool holds no authority.** It selects no candidates, chooses no order, ratifies no
merge and emits no event. It is given an explicit base and an explicit ordered list of refs, and
it reports what happens when they are composed in that order. Every input that could constitute a
decision is required on the command line, for the same reason `lease_singleton.py` refuses to
discover its own sources: a tool that picked its own inputs would be answering the question it
exists to inform.

It also belongs to no candidate. The properties it measures — a runner entry lost to a merge, a
duplicate enrolment, an executable bit dropped by a resolution, a failure that vanished without
anyone claiming to have fixed it — are properties of the *composition*, not of any one repair.
Committing it inside one repair's branch would make that repair's acceptance carry a tool about
the others.

WHAT IS MEASURED, per prefix step
---------------------------------
runner_entries          how many suites the release runner enrols
duplicate_entries       the same suite enrolled twice — a union resolution that ran twice
mode_bit_offenders      tracked files carrying `#!` at mode 100644; a merge can drop the bit
failures                the set of suites that fail, as a SET and not a count
new_failures            failing here, not failing at the previous step
vanished_failures       failing at the previous step, not failing here
unexplained_vanishings  vanished, and no candidate in this step declared it as a fix

🔴 `unexplained_vanishings` needs the declaration, and the declaration is an INPUT. The tool
cannot infer what a candidate meant to repair, and inferring it is precisely the ownership fiction
this file must not commit. With no `--declares` given, every vanishing is reported unexplained —
which is the fail-closed answer, and is noisy on purpose.

A failure that disappears is not good news by default. It is the same shape as the publication
bypass this laboratory has already met twice: the check did not start passing, it stopped being
run. A suite dropped from the runner by a bad merge disappears from the failure list exactly like
a suite that was repaired.

CANDIDATE IDENTITY
------------------
Each candidate's tip SHA is recorded before the simulation and re-read after, and the
`CANDIDATE_CONTENT_HASH` is carried through verbatim when supplied. The simulation happens in a
throwaway worktree on a throwaway branch: no candidate branch is moved, and the report says so by
showing the same tip on both sides.

CONFLICT RESOLUTION
-------------------
Only one resolution is automated: a conflict in which BOTH sides only added lines is resolved by
keeping every line. It refuses anything else. Union applied to a conflict that also deletes would
silently resurrect deleted content, and "the merge went through" would then be the only evidence
anyone looked at.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field, asdict
from pathlib import Path


CONFLICT_START = re.compile(r"^<{7}")
CONFLICT_MID = re.compile(r"^={7}$")
CONFLICT_END = re.compile(r"^>{7}")


class SimulationError(RuntimeError):
    """Anything that makes the measurement untrustworthy. Never swallowed."""


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args],
                          check=check, capture_output=True, text=True)


def union_resolve(path: Path) -> int:
    """Keep every line of both sides. Refuses unless both sides ONLY added.

    🔴 The refusal is the function. A conflict where one side deleted a line looks identical to
    a pure-addition conflict after the markers are stripped, and the difference between a safe
    automatic resolution and a destructive one is entirely in whether this check ran.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    ours: list[str] = []
    theirs: list[str] = []
    state = "plain"
    blocks = 0
    for line in lines:
        if CONFLICT_START.match(line):
            if state != "plain":
                raise SimulationError(f"{path}: nested conflict marker")
            state, ours, theirs, blocks = "ours", [], [], blocks + 1
            continue
        if CONFLICT_MID.match(line) and state == "ours":
            state = "theirs"
            continue
        if CONFLICT_END.match(line) and state == "theirs":
            merged = list(ours)
            merged.extend(entry for entry in theirs if entry not in merged)
            out.extend(merged)
            state = "plain"
            continue
        if state == "plain":
            out.append(line)
        elif state == "ours":
            ours.append(line)
        else:
            theirs.append(line)
    if state != "plain":
        raise SimulationError(f"{path}: unterminated conflict marker")
    if blocks == 0:
        raise SimulationError(f"{path}: no conflict markers — nothing to resolve")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return blocks


def union_is_safe(repo: Path, relative: str) -> bool:
    """True only when neither side removed a line present in the merge base.

    Read from git rather than from the marked-up file: the working copy no longer contains the
    base, and a union resolution that cannot see the base cannot know what it is resurrecting.
    """
    def blob(stage: int) -> set[str]:
        proc = git(repo, "show", f":{stage}:{relative}", check=False)
        if proc.returncode != 0:
            raise SimulationError(f"{relative}: stage {stage} unavailable; not a normal conflict")
        return set(proc.stdout.splitlines())
    base, ours, theirs = blob(1), blob(2), blob(3)
    return not (base - ours) and not (base - theirs)


def runner_entries(tree: Path) -> list[str]:
    proc = subprocess.run([sys.executable, "scripts/run_release_regressions.py", "--list"],
                          cwd=str(tree), capture_output=True, text=True)
    if proc.returncode != 0:
        raise SimulationError("run_release_regressions.py --list failed:\n" + proc.stderr[-2000:])
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def mode_bit_offenders(tree: Path) -> list[str]:
    """Tracked files with a `#!` first line recorded at mode 100644.

    The index is the population, not the disk: a working tree can carry an executable bit that
    no clone will ever receive, which is the difference this check exists to see.

    🔴 Blobs are read as BYTES through one `cat-file --batch`, not as text through one
    `git show` per path. The first version did the latter and died on the first PNG —
    `UnicodeDecodeError: byte 0x89 in position 0` — after nine minutes of a ten-step run. It
    failed closed, which is the right direction and still a whole measurement lost. A
    repository check that assumes its own repository is all text is a check that has not met
    one.
    """
    listing = git(tree, "ls-files", "-s", "-z").stdout.split("\0")
    wanted: list[tuple[str, str]] = []
    for row in listing:
        if not row:
            continue
        meta, _, relative = row.partition("\t")
        fields = meta.split()
        if len(fields) < 2 or fields[0] != "100644":
            continue
        wanted.append((fields[1], relative))
    if not wanted:
        return []
    proc = subprocess.run(
        ["git", "-C", str(tree), "cat-file", "--batch"],
        input=("\n".join(sha for sha, _ in wanted) + "\n").encode(),
        capture_output=True)
    offenders: list[str] = []
    payload = proc.stdout
    cursor = 0
    for _, relative in wanted:
        newline = payload.find(b"\n", cursor)
        if newline < 0:
            break
        header = payload[cursor:newline].split()
        cursor = newline + 1
        if len(header) < 3:
            continue
        size = int(header[2])
        if payload[cursor:cursor + 2] == b"#!":
            offenders.append(relative)
        cursor += size + 1
    return sorted(offenders)


def failing_suites(tree: Path) -> list[str]:
    """The suites the release runner reports as failing, as a SET.

    🔴 This function reported ZERO failures at all ten steps of a real ten-candidate run, and
    the table looked healthy. `run_release_regressions.py` writes its 1925 lines of test output
    to stdout and its verdict — `REGRESSION VERDICT: FAIL` and one `- suite: exit N` line per
    failure — to **stderr**. The first version read stdout only.

    That is this tool's own headline finding, committed inside the tool: an empty failure list
    because the check stopped being read, indistinguishable from an empty failure list because
    everything passed. It survived a 17-test suite because every fixture's stub runner printed
    to stdout — **the tested surface and the defective surface were disjoint.**

    Two repairs, and the second is the one that matters:

      1. both streams are read;
      2. the exit code and the parsed list must AGREE. A non-zero exit naming no suite, or a
         zero exit naming one, is refused rather than returned. Without (2), the same class of
         defect in some future runner would produce the same silent zero.
    """
    proc = subprocess.run([sys.executable, "scripts/run_release_regressions.py"],
                          cwd=str(tree), capture_output=True, text=True)
    failures = sorted({line[2:].split(":", 1)[0]
                       for line in (proc.stdout + "\n" + proc.stderr).splitlines()
                       if line.startswith("- ") and ": exit" in line})
    if proc.returncode != 0 and not failures:
        raise SimulationError(
            "the release runner exited "
            f"{proc.returncode} and named no failing suite. An empty failure list that "
            "disagrees with the exit code is the defect this tool exists to detect, and it is "
            "not reported as zero failures.\n"
            f"stdout tail:\n{proc.stdout[-800:]}\nstderr tail:\n{proc.stderr[-800:]}")
    if proc.returncode == 0 and failures:
        raise SimulationError(
            "the release runner exited 0 while naming failing suites "
            f"{failures}. The verdict and the list disagree; neither is trustworthy.")
    return failures


@dataclass
class Step:
    candidate: str
    tip_before: str
    tip_after: str
    content_hash: str | None
    conflict: str
    conflicted_paths: list[str]
    runner_entries: int
    duplicate_entries: list[str]
    mode_bit_offenders: list[str]
    failures: list[str]
    new_failures: list[str]
    vanished_failures: list[str]
    unexplained_vanishings: list[str]
    declared_fixes: list[str] = field(default_factory=list)


def simulate(repo: Path, base: str, candidates: list[str],
             declares: dict[str, list[str]], hashes: dict[str, str],
             keep: Path | None) -> tuple[list[Step], dict]:
    box = Path(tempfile.mkdtemp(prefix="legend-integration-"))
    tree = keep if keep is not None else box / "tree"
    branch = "integration-matrix-simulation"
    git(repo, "worktree", "prune", check=False)
    git(repo, "worktree", "remove", "--force", str(tree), check=False)
    git(repo, "branch", "-D", branch, check=False)
    git(repo, "worktree", "add", "-q", "--checkout", "-b", branch, str(tree), base)

    tips_before = {c: git(repo, "rev-parse", c).stdout.strip() for c in candidates}
    steps: list[Step] = []
    previous: set[str] = set()
    baseline = True
    try:
        for candidate in candidates:
            merge = git(tree, "merge", "--no-edit", "--no-ff", candidate, check=False)
            conflicted = sorted(set(
                git(tree, "diff", "--name-only", "--diff-filter=U").stdout.split()))
            if merge.returncode == 0:
                conflict = "clean"
            else:
                if not conflicted:
                    git(tree, "merge", "--abort", check=False)
                    raise SimulationError(
                        f"{candidate}: merge failed with no conflicted paths:\n{merge.stderr}")
                for relative in conflicted:
                    if not union_is_safe(tree, relative):
                        git(tree, "merge", "--abort", check=False)
                        raise SimulationError(
                            f"{candidate}: {relative} is not a pure-addition conflict. "
                            "Union would resurrect deleted content; resolve it by hand.")
                    union_resolve(tree / relative)
                    git(tree, "add", relative)
                git(tree, "commit", "-q", "--no-edit")
                conflict = "union"

            entries = runner_entries(tree)
            seen: set[str] = set()
            duplicates = sorted({e for e in entries if e in seen or seen.add(e)})
            failures = set(failing_suites(tree))
            new = sorted(failures - previous) if not baseline else []
            vanished = sorted(previous - failures) if not baseline else []
            declared = declares.get(candidate, [])
            unexplained = [suite for suite in vanished if suite not in declared]
            steps.append(Step(
                candidate=candidate,
                tip_before=tips_before[candidate],
                tip_after=git(repo, "rev-parse", candidate).stdout.strip(),
                content_hash=hashes.get(candidate),
                conflict=conflict,
                conflicted_paths=conflicted,
                runner_entries=len(entries),
                duplicate_entries=duplicates,
                mode_bit_offenders=mode_bit_offenders(tree),
                failures=sorted(failures),
                new_failures=new,
                vanished_failures=vanished,
                unexplained_vanishings=unexplained,
                declared_fixes=declared,
            ))
            previous = failures
            baseline = False
        composed_tip = git(tree, "rev-parse", "HEAD").stdout.strip()
    finally:
        if keep is None:
            git(repo, "worktree", "remove", "--force", str(tree), check=False)
            git(repo, "branch", "-D", branch, check=False)
            git(repo, "worktree", "prune", check=False)
            shutil.rmtree(box, ignore_errors=True)

    identity_preserved = all(step.tip_before == step.tip_after for step in steps)
    summary = {
        "base": git(repo, "rev-parse", base).stdout.strip(),
        "composed_tip": composed_tip,
        "candidate_identity_preserved": identity_preserved,
        "kept_worktree": str(tree) if keep is not None else None,
    }
    return steps, summary


def render(steps: list[Step], summary: dict) -> str:
    width = max((len(s.candidate) for s in steps), default=10)
    out = [f"BASE {summary['base'][:12]}    "
           f"CANDIDATE IDENTITY PRESERVED: {summary['candidate_identity_preserved']}", ""]
    head = (f"{'PREFIX STEP':<{width}}  {'RUNNER':>6}  {'DUP':>3}  {'MODE':>4}  "
            f"{'FAILS':>5}  {'CONFLICT':<8}  NEW / VANISHED")
    out += [head, "-" * len(head)]
    for step in steps:
        movement = []
        if step.new_failures:
            movement.append("NEW " + ",".join(step.new_failures))
        if step.vanished_failures:
            tag = "VANISHED"
            if step.unexplained_vanishings:
                tag = "VANISHED-UNEXPLAINED"
            movement.append(tag + " " + ",".join(step.vanished_failures))
        out.append(
            f"{step.candidate:<{width}}  {step.runner_entries:>6}  "
            f"{len(step.duplicate_entries):>3}  {len(step.mode_bit_offenders):>4}  "
            f"{len(step.failures):>5}  {step.conflict:<8}  "
            f"{'; '.join(movement) if movement else ('(baseline)' if step is steps[0] else 'none')}")
    return "\n".join(out)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=".", help="repository to simulate in")
    parser.add_argument("--base", required=True, help="ref every candidate is based on")
    parser.add_argument("--candidate", action="append", required=True, metavar="REF",
                        help="candidate ref, repeated; ORDER IS SIGNIFICANT and is yours")
    parser.add_argument("--declares", action="append", default=[], metavar="REF=SUITE[,SUITE]",
                        help="suites a candidate claims to repair; without it every vanishing "
                             "is reported unexplained")
    parser.add_argument("--content-hash", action="append", default=[], metavar="REF=HASH",
                        help="carry a candidate's CANDIDATE_CONTENT_HASH into the report")
    parser.add_argument("--keep-worktree", metavar="PATH",
                        help="leave the composed worktree in place for inspection")
    parser.add_argument("--json", metavar="PATH", help="write the machine-readable report")
    return parser.parse_args()


def split_pairs(entries: list[str], name: str) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for entry in entries:
        ref, sep, value = entry.partition("=")
        if not sep:
            raise SystemExit(f"--{name} expects REF=VALUE, got {entry!r}")
        mapping[ref] = [v for v in value.split(",") if v]
    return mapping


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).resolve()
    declares = split_pairs(args.declares, "declares")
    hashes = {k: v[0] for k, v in split_pairs(args.content_hash, "content-hash").items() if v}
    unknown = (set(declares) | set(hashes)) - set(args.candidate)
    if unknown:
        raise SystemExit(f"declared for refs that are not candidates: {sorted(unknown)}")
    keep = Path(args.keep_worktree).resolve() if args.keep_worktree else None
    try:
        steps, summary = simulate(repo, args.base, args.candidate, declares, hashes, keep)
    except SimulationError as exc:
        print(f"SIMULATION_REFUSED: {exc}", file=sys.stderr)
        return 3
    print(render(steps, summary))
    report = {"summary": summary, "steps": [asdict(s) for s in steps]}
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    problems = [s for s in steps
                if s.duplicate_entries or s.mode_bit_offenders or s.new_failures
                or s.unexplained_vanishings]
    print()
    if not summary["candidate_identity_preserved"]:
        print("CANDIDATE IDENTITY MOVED DURING SIMULATION — the report is about a different set")
        return 2
    if problems:
        print("INTEGRATION FINDINGS: " + ", ".join(sorted({p.candidate for p in problems})))
        return 1
    print("INTEGRATION FINDINGS: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
