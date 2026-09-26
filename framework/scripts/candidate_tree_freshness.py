#!/usr/bin/env python3
"""Verify the committed generated surfaces against the EXACT tree about to land — nothing else.

WHY THIS EXISTS
---------------
H0 (`governance/design_records/h0_generated_surface_drift_20260924.md`) found four derived
surfaces stale at once, from one cause with three entry points: regeneration exists only in
BATCH_COMMIT Phase 4.7, while their inputs are also written by direct landings — a receipt
recording, a direct propagation, an analysis commit touching the full-text queue — and nothing
on those paths ran the drift checks. Each generator already has its own `--check`/`--verify`;
what was missing is WHEN and AGAINST WHAT they run.

Against what: the candidate tree, exactly. Not the shared working directory, which holds peers'
uncommitted edits, gitignored material and whatever the current actor has not staged — a check
there can pass on a file that will not be committed, or fail on one that will not be either.
The candidate is materialized in a private temporary directory from git objects alone:

    --merge TIP [--base main]   the tree `task_close.py` would produce: TIP merged into BASE
                                (`git merge-tree --write-tree`, the same ort merge); default
    --staged                    HEAD + the index, what a plain `git commit` would record
    --paths P [P ...]           HEAD + the working-tree content of exactly these files, what
                                `scripts/legend_commit.sh "<msg>" P ...` would record
    --candidate REV [--base B]  an existing commit against B (default its first parent) — for
                                auditing a landing after the fact, as H0 did by hand

WHICH surfaces: discovered in the candidate tree by the one discovery the release suite uses
(`scripts/test_generated_surfaces_are_regenerated.generated_surfaces`) — never a second list.
A discovered surface whose generator is not declared in `GENERATORS` below is CHECK_ERROR: an
unknown input set cannot be proven untouched, so the tool refuses rather than guesses.

WHICH checks run: only those whose inputs the candidate changes relative to its base. The
inputs of a surface are its declared data paths, the surface file and its companion outputs,
and the transitive closure of the generator's local Python imports, computed in the candidate
tree — so a change to `fulltext_receipts.py` re-checks every surface that imports it. With
`--all` every check runs.

Per surface: FRESH · STALE · NOT_AFFECTED · CHECK_ERROR, and NO_CHECK for a surface declared
without a freshness check (the surface census photographs a gitignored directory; see
Phase 4.7). NOT_AFFECTED says the candidate cannot have changed the surface's freshness; it
does not say the base was fresh.

Exit codes: 0 nothing stale · 1 at least one STALE · 2 tool error (CHECK_ERROR, a conflicted
merge, an invalid candidate). The temporary tree is released in `finally`, on SIGTERM/SIGHUP,
and — when even that did not run — reaped by the next invocation (`owned_scratch.py`): it is
never a registered worktree, so a kill cannot leave one behind.

    python3 framework/scripts/candidate_tree_freshness.py                  # HEAD into main
    python3 framework/scripts/candidate_tree_freshness.py --paths disease-models/wwox/registries/fulltext_read_receipts.jsonl
    python3 framework/scripts/candidate_tree_freshness.py --candidate c9914f9 --json
"""
from __future__ import annotations

import argparse
import ast
import fnmatch
import json
import os
import signal
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "scripts"))
import owned_scratch  # noqa: E402
from test_generated_surfaces_are_regenerated import generated_surfaces  # noqa: E402

PREFIX = "legend-candidate-tree-"
FRESH, STALE, NOT_AFFECTED, CHECK_ERROR, NO_CHECK = (
    "FRESH", "STALE", "NOT_AFFECTED", "CHECK_ERROR", "NO_CHECK")
DEFAULT_TIMEOUT = 900.0


@dataclass(frozen=True)
class Generator:
    """What a generator reads, how its freshness is checked, and how it is regenerated.

    ``inputs``: repository paths with ``{disease}``; a trailing ``/`` is a directory prefix, a
    ``*`` is an fnmatch glob (``*`` crosses ``/``), anything else is one file. Declared from
    each generator's own `derived_inputs.input_state` call and from H0's replay, and widened
    where the generator reads more than it declares (batch_queue scans every `*_current.md`;
    coverage_report reaches research/ through growth_anchors).
    """
    inputs: tuple[str, ...]
    check: tuple[str, ...] | None
    regenerate: str
    outputs: tuple[str, ...] = ()
    code_dirs: tuple[str, ...] = ()
    note: str = ""


_EXPORT = "disease-models/{disease}/analysis/data/pathograph_export.jsonl"
GENERATORS: dict[str, Generator] = {
    "framework/scripts/coverage_report.py": Generator(
        inputs=("disease-models/{disease}/registries/", "disease-models/{disease}/research/"),
        check=("--root", ".", "--disease", "{disease}", "--check", "{surface}"),
        regenerate="python3 framework/scripts/coverage_report.py --disease {disease} --out {surface}"),
    "framework/scripts/reading_state.py": Generator(
        inputs=("disease-models/{disease}/registries/fulltext_read_receipts.jsonl",),
        check=("--root", ".", "--disease", "{disease}", "--check", "{surface}"),
        regenerate="python3 framework/scripts/reading_state.py --disease {disease} --out {surface}"),
    "framework/scripts/batch_queue.py": Generator(
        inputs=("disease-models/{disease}/registries/", "disease-models/{disease}/research/",
                "disease-models/{disease}/*_current.md"),
        check=("--root", ".", "--disease", "{disease}", "--check", "{surface}"),
        regenerate="python3 framework/scripts/batch_queue.py --disease {disease} --out {surface}",
        code_dirs=(".claude/skills/legend-study-intake-triage/scripts",)),
    "framework/scripts/pathograph.py": Generator(
        inputs=("disease-models/{disease}/registries/",
                "disease-models/{disease}/research/deepdive_manifests/"),
        check=("--root", ".", "--disease", "{disease}", "--verify", "--out", "{surface}",
               "--export", _EXPORT),
        regenerate=("python3 framework/scripts/pathograph.py --disease {disease} --out {surface} "
                    "--export " + _EXPORT),
        outputs=(_EXPORT,)),
    "framework/scripts/surface_census.py": Generator(
        inputs=(), check=None,
        regenerate="python3 framework/scripts/surface_census.py --disease {disease} --out {surface}",
        note="a dated photograph of gitignored files/fulltext/, which no candidate tree holds; "
             "no freshness check by design (prompt_batch_commit.md Phase 4.7)"),
}


class CandidateError(RuntimeError):
    """The candidate tree could not be built (conflict, bad revision, unmerged index)."""


@dataclass
class SurfaceResult:
    surface: str
    generator: str
    status: str
    detail: str = ""
    seconds: float = 0.0
    triggers: list[str] = field(default_factory=list)
    regenerate: str = ""


@dataclass
class Report:
    mode: str
    base: str
    candidate_tree: str
    changed: int
    results: list[SurfaceResult]
    seconds: float = 0.0

    @property
    def exit_code(self) -> int:
        statuses = {r.status for r in self.results}
        if CHECK_ERROR in statuses:
            return 2
        return 1 if STALE in statuses else 0

    def stale(self) -> list[SurfaceResult]:
        return [r for r in self.results if r.status == STALE]


# ----------------------------------------------------------------------------- git


def _git(repo: Path, *args: str, env: dict | None = None, check: bool = True,
         timeout: float = 300) -> subprocess.CompletedProcess:
    done = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True,
                          env=env, timeout=timeout)
    if check and done.returncode != 0:
        raise CandidateError(f"git {' '.join(args)}: {(done.stderr or done.stdout).strip()}")
    return done


def top_level(start: Path) -> Path:
    return Path(_git(start, "rev-parse", "--show-toplevel").stdout.strip())


def tree_of(repo: Path, rev: str) -> str:
    return _git(repo, "rev-parse", "--verify", f"{rev}^{{tree}}").stdout.strip()


def commit_of(repo: Path, rev: str) -> str:
    return _git(repo, "rev-parse", "--verify", f"{rev}^{{commit}}").stdout.strip()


def merge_candidate(repo: Path, tip: str, base: str = "main") -> tuple[str, str]:
    """(base tree, merged tree) — the ort merge `git merge` would perform, with no checkout."""
    base_commit, tip_commit = commit_of(repo, base), commit_of(repo, tip)
    done = _git(repo, "merge-tree", "--write-tree", "--no-messages", base_commit, tip_commit,
                check=False)
    if done.returncode == 1:
        raise CandidateError(f"merging {tip} into {base} conflicts; the landing would refuse too")
    if done.returncode != 0:
        raise CandidateError(f"git merge-tree failed: {done.stderr.strip()}")
    return tree_of(repo, base_commit), done.stdout.splitlines()[0].strip()


def staged_candidate(repo: Path) -> tuple[str, str]:
    """(HEAD tree, index tree)."""
    return tree_of(repo, "HEAD"), _git(repo, "write-tree").stdout.strip()


def paths_candidate(repo: Path, paths: list[str], scratch: Path) -> tuple[str, str]:
    """(HEAD tree, HEAD + the working-tree content of ``paths``), via a private index."""
    top = top_level(repo)
    relative = []
    for raw in paths:
        path = Path(raw)
        absolute = path if path.is_absolute() else top / path
        if absolute.is_dir():
            raise CandidateError(f"{raw} is a directory; name the files")
        try:
            relative.append(absolute.resolve().relative_to(top.resolve()).as_posix()
                            if absolute.exists() else absolute.relative_to(top).as_posix())
        except ValueError as exc:
            raise CandidateError(f"{raw} is outside the repository") from exc
    env = dict(os.environ, GIT_INDEX_FILE=str(scratch / "paths.index"))
    _git(top, "read-tree", "HEAD", env=env)
    if relative:
        _git(top, "update-index", "--add", "--remove", "--", *relative, env=env)
    return tree_of(top, "HEAD"), _git(top, "write-tree", env=env).stdout.strip()


def changed_paths(repo: Path, base_tree: str, candidate_tree: str) -> list[str]:
    out = _git(repo, "diff-tree", "-r", "--name-only", "--no-renames", "-z",
               base_tree, candidate_tree).stdout
    return [p for p in out.split("\0") if p]


def materialize(repo: Path, tree: str, scratch: Path) -> Path:
    """Write ``tree`` into ``scratch/tree`` from git objects alone. No worktree is registered."""
    dest = scratch / "tree"
    dest.mkdir()
    env = dict(os.environ, GIT_INDEX_FILE=str(scratch / "materialize.index"))
    _git(repo, "read-tree", tree, env=env)
    _git(repo, "checkout-index", "-a", "-f", f"--prefix={dest}/", env=env)
    return dest


# ----------------------------------------------------------------------- inputs


def disease_of(surface: str) -> str | None:
    parts = surface.split("/")
    return parts[1] if len(parts) > 2 and parts[0] == "disease-models" else None


def code_closure(tree: Path, script: str, extra_dirs: tuple[str, ...] = ()) -> set[str]:
    """The generator plus every local module it imports, transitively, as repository paths."""
    search = [tree / "framework" / "scripts", *(tree / d for d in extra_dirs)]
    todo, seen = [tree / script], set()
    while todo:
        current = todo.pop()
        relative = current.relative_to(tree).as_posix()
        if relative in seen:
            continue
        seen.add(relative)
        try:
            module = ast.parse(current.read_text(encoding="utf-8"))
        except (OSError, SyntaxError, ValueError):
            continue
        names = set()
        for node in ast.walk(module):
            if isinstance(node, ast.Import):
                names.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                names.add(node.module.split(".")[0])
        for name in names:
            for directory in (current.parent, *search):
                candidate = directory / f"{name}.py"
                if candidate.is_file():
                    todo.append(candidate)
                    break
    return seen


def _matches(path: str, pattern: str) -> bool:
    if pattern.endswith("/"):
        return path.startswith(pattern)
    if "*" in pattern or "?" in pattern:
        return fnmatch.fnmatchcase(path, pattern)
    return path == pattern


def triggers_for(tree: Path, surface: str, script: str, generator: Generator,
                 changed: list[str]) -> list[str]:
    disease = disease_of(surface) or ""
    patterns = [p.format(disease=disease) for p in (*generator.inputs, *generator.outputs)]
    patterns.append(surface)
    code = code_closure(tree, script, generator.code_dirs)
    return [p for p in changed if p in code or any(_matches(p, pat) for pat in patterns)]


# ------------------------------------------------------------------------- run


def _fill(template, surface: str, disease: str):
    return [part.format(surface=surface, disease=disease) for part in template]


def run_check(tree: Path, surface: str, script: str, generator: Generator,
              timeout: float) -> tuple[str, str, float]:
    disease = disease_of(surface) or ""
    command = [sys.executable, script, *_fill(generator.check, surface, disease)]
    started = time.monotonic()
    try:
        done = subprocess.run(command, cwd=tree, capture_output=True, text=True, timeout=timeout,
                              env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    except subprocess.TimeoutExpired:
        return CHECK_ERROR, f"timed out after {timeout:.0f}s", time.monotonic() - started
    elapsed = time.monotonic() - started
    text = (done.stdout + done.stderr).strip()
    last = text.splitlines()[-1] if text else ""
    if done.returncode == 0:
        return FRESH, last, elapsed
    if done.returncode == 1 and "Traceback" not in text:
        return STALE, last, elapsed
    return CHECK_ERROR, f"exit {done.returncode}: {text[-400:]}", elapsed


def evaluate(repo: Path, *, mode: str = "merge", tip: str = "HEAD", base: str | None = None,
             paths: list[str] | None = None, run_all: bool = False, jobs: int = 4,
             timeout: float = DEFAULT_TIMEOUT,
             generators: dict[str, Generator] | None = None) -> Report:
    """Build the candidate, discover its surfaces, run the affected checks. Raises CandidateError."""
    generators = GENERATORS if generators is None else generators
    started = time.monotonic()
    repo = top_level(repo)
    owned_scratch.reap(PREFIX)
    scratch = owned_scratch.make(PREFIX)
    try:
        if mode == "merge":
            base = base or "main"
            base_tree, candidate = merge_candidate(repo, tip, base)
            label = f"{tip} merged into {base}"
        elif mode == "staged":
            base_tree, candidate = staged_candidate(repo)
            base, label = "HEAD", "HEAD + index"
        elif mode == "paths":
            base_tree, candidate = paths_candidate(repo, list(paths or []), scratch)
            base, label = "HEAD", f"HEAD + {len(paths or [])} named path(s)"
        elif mode == "candidate":
            base = base or f"{tip}^1"
            base_tree, candidate = tree_of(repo, base), tree_of(repo, tip)
            label = f"{tip} against {base}"
        else:
            raise CandidateError(f"unknown mode {mode!r}")
        changed = changed_paths(repo, base_tree, candidate)
        tree = materialize(repo, candidate, scratch)
        results: list[SurfaceResult] = []
        pending: list[tuple[SurfaceResult, str, Generator]] = []
        for path, scripts in sorted(generated_surfaces(tree).items()):
            surface = path.relative_to(tree).as_posix()
            declared = sorted(s for s in scripts if s in generators)
            if not declared:
                results.append(SurfaceResult(
                    surface, ", ".join(sorted(scripts)), CHECK_ERROR,
                    "undeclared generator: add its inputs and check to GENERATORS in "
                    "framework/scripts/candidate_tree_freshness.py"))
                continue
            for script in declared:
                generator = generators[script]
                disease = disease_of(surface) or ""
                result = SurfaceResult(surface, script, NOT_AFFECTED,
                                       regenerate=generator.regenerate.format(
                                           surface=surface, disease=disease))
                results.append(result)
                if generator.check is None:
                    result.status, result.detail = NO_CHECK, generator.note
                    continue
                if any("{disease}" in part for part in generator.check) and not disease:
                    result.status = CHECK_ERROR
                    result.detail = "surface is outside disease-models/<disease>/"
                    continue
                result.triggers = triggers_for(tree, surface, script, generator, changed)
                if result.triggers or run_all:
                    pending.append((result, script, generator))
        with ThreadPoolExecutor(max_workers=max(1, jobs)) as pool:
            outcomes = pool.map(lambda item: run_check(tree, item[0].surface, item[1], item[2],
                                                       timeout), pending)
            for (result, _, _), (status, detail, seconds) in zip(pending, outcomes):
                result.status, result.detail, result.seconds = status, detail, round(seconds, 2)
        return Report(label, base or "", candidate, len(changed), results,
                      round(time.monotonic() - started, 2))
    finally:
        owned_scratch.release(scratch)


def render(report: Report) -> str:
    lines = [f"CANDIDATE {report.mode} · tree {report.candidate_tree[:12]} · "
             f"{report.changed} path(s) changed vs {report.base}"]
    for r in report.results:
        why = f" · triggered by {', '.join(r.triggers[:3])}" + (
            f" (+{len(r.triggers) - 3})" if len(r.triggers) > 3 else "") if r.triggers else ""
        took = f" · {r.seconds:.1f}s" if r.seconds else ""
        lines.append(f"  {r.status:<12} {r.surface}{took}{why}"
                     + (f"\n               {r.detail}" if r.detail and r.status != FRESH else ""))
    stale = report.stale()
    if stale:
        lines.append("REGENERATE on the task side (inputs committed there, so no reason is "
                     "needed), commit, and retry:")
        lines.extend(f"  {r.regenerate}" for r in stale)
    verdict = {0: "FRESH", 1: "STALE", 2: "CHECK_ERROR"}[report.exit_code]
    lines.append(f"VERDICT: {verdict} ({report.seconds:.1f}s)")
    return "\n".join(lines)


def _terminate(signum, _frame):
    raise SystemExit(128 + signum)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--merge", metavar="TIP", help="candidate = TIP merged into --base (default)")
    mode.add_argument("--staged", action="store_true", help="candidate = HEAD + the index")
    mode.add_argument("--paths", nargs="+", metavar="PATH",
                      help="candidate = HEAD + these files' working-tree content")
    mode.add_argument("--candidate", metavar="REV", help="candidate = REV's tree")
    parser.add_argument("--base", help="base revision (merge: main; candidate: REV^1)")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--all", action="store_true", help="run every check, affected or not")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT,
                        help="per-check deadline in seconds")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    for signum in (signal.SIGTERM, signal.SIGHUP):
        signal.signal(signum, _terminate)
    if args.staged:
        kwargs = {"mode": "staged"}
    elif args.paths:
        kwargs = {"mode": "paths", "paths": args.paths}
    elif args.candidate:
        kwargs = {"mode": "candidate", "tip": args.candidate, "base": args.base}
    else:
        kwargs = {"mode": "merge", "tip": args.merge or "HEAD", "base": args.base}
    try:
        report = evaluate(Path(args.repo), run_all=args.all, jobs=args.jobs,
                          timeout=args.timeout, **kwargs)
    except (CandidateError, OSError, subprocess.TimeoutExpired) as exc:
        print(f"candidate_tree_freshness: {exc}", file=sys.stderr)
        return 2
    if args.json:
        payload = asdict(report) | {"exit_code": report.exit_code}
        print(json.dumps(payload, indent=2))
    else:
        print(render(report))
    return report.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
