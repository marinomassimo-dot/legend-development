#!/usr/bin/env python3
"""Measure whether each tool's own suite ever drives the tool.

🔴 WHY THIS EXISTS, and it happened three times in one day.

On 2026-09-09 (`2026-09-09_actor_retrospective.md` § 4.1, § 9.3):

* the commit wrapper was smoke-tested against the property its author was worried about
  (it declines to make an empty commit) and shipped broken on the property that mattered
  (a ``-m`` after ``--``, i.e. any message containing spaces);
* ``erratum_scope_check.py`` reported **12/12 green while crashing corpus-wide**, because its
  self-test *"exercises ``parse_panel`` and ``intersects`` and never calls ``check_manifest``"*
  — and ``check_manifest`` is the whole tool;
* ``genre_discriminator.py``'s fixtures all passed while it flagged **every** ordinary primary
  paper as ``UNDER_DESCRIBED``, exposed only by a control run against papers whose genre was
  never in doubt.

One shape: **a test that passes while testing something adjacent to the thing that fails.**
A green suite is then evidence about the fixtures, not about the tool, and the tool's own
count of passing cases — 12/12 — is the most misleading number in the record.

WHAT IS MEASURED, and how, because a static grep would be a fourth instance of the same defect
----------------------------------------------------------------------------------------------

Each suite is **executed**, under a profiler that records every Python function actually
entered, in the suite process *and in every subprocess it spawns* (most of these suites drive
their tool with ``subprocess.run([sys.executable, SCRIPT, …])``, which is exactly the right way
to test a CLI and is invisible to any in-process instrumentation). The same instrumentation
records every file **opened**. Nothing here is inferred from source text except which functions
are candidates.

``entry_point_called``
    True when the suite entered ``main`` **and** at least one of ``main``'s own direct callees
    that is not the self-test dispatch.

    Both halves are load-bearing, and the second is the one that catches the motivating defect.
    ``python3 erratum_scope_check.py --self-test`` enters ``main`` and turns straight around
    into ``self_test()``, which exercises two leaf helpers. ``main`` was entered; the tool was
    never driven. Requiring one non-self-test callee of ``main`` — for that tool,
    ``check_manifest`` — is precisely the distinction, and this module's own suite pins it
    against the two real commits, before and after the repair (``0e33f0f``).

    Depth is 1 by design: ``main``'s *direct* callees. A tool whose ``main`` delegates to a
    single ``_run()`` is therefore judged on ``_run``, not on what ``_run`` calls. That is a
    known limitation, stated rather than hidden; it under-detects, never over-detects.

``real_artifact_case``
    True when the suite (or a child) opened a file under a **corpus root** — ``files/``,
    ``disease-models/``, ``ledger/``, ``framework/state/``, ``_external_repos/`` — rather than
    only fixtures it wrote itself into a temporary directory.

    🔴 ``files/`` is gitignored, so in this checkout **398 of 616 declared artefacts are
    absent**. A real-artefact case must therefore degrade to a **declared skip** when the bytes
    are missing — never to a silent pass, which is the same defect one level up. So the value
    is three-state: ``true``, ``skipped_declared`` (the suite ran and announced a skip), or
    ``false``. Only ``false`` on both axes is a finding.

    🔴 **``real_artifact_case`` means a real artefact is READ. A case that writes a real
    artefact — or runs a tool with ``--write`` against the real root — is the incident, not
    the criterion.** On 2026-09-10 at 22:26 UTC, 54 tracked dossiers under
    ``disease-models/wwox/research/fulltext_dossiers/`` were overwritten with the word
    ``touched`` and a manifest had its snippets normalised, by a mutation matrix that ran a
    deliberately broken tool through its own real-artefact cases against the real root and
    restored the tool but not the artefacts
    (``learning/orchestrator/FINDING-20260911-DOSSIER-TRUNCATION.md``). A criterion that
    rewards reading real artefacts must forbid writing them in the same sentence, or it
    trains exactly that. So the instrumentation does not merely note writes: **any attempt
    to open a file for writing, delete, rename or truncate it under a guarded tree is refused
    in the suite's process before the bytes land**, is recorded with its mode, and marks the
    script ``refused`` — a verdict that outranks both axes and fails ``--enforce``. The
    guarded trees are the corpus roots plus the ones ``scripts/run_release_regressions.py``
    hashes (``GUARDED_TREES``). ``--guarded <command…>`` runs any command under the same
    refusal, which is how a mutation matrix must be run from now on.

USAGE

    python3 framework/scripts/self_test_coverage.py                  # the report
    python3 framework/scripts/self_test_coverage.py --json
    python3 framework/scripts/self_test_coverage.py --script erratum_scope_check.py
    python3 framework/scripts/self_test_coverage.py --enforce        # non-zero on a new false/false or a refusal
    python3 framework/scripts/self_test_coverage.py --guarded python3 framework/scripts/test_x.py
                                                                     # run anything; guarded writes refused and listed

WHAT IT DOES NOT CLAIM. That a suite which drives its entry point tests it *well* — coverage of
the call, not of the behaviour. It cannot see a case that asserts nothing. It measures the one
property whose absence made three green suites meaningless, and only that.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

#: Real repository data a tool operates on in production. A case that opens one of these is a
#: case drawn from the corpus; everything under a temporary directory is a fixture.
CORPUS_ROOTS = ("files", "disease-models", "ledger", "framework/state", "_external_repos")

#: Trees a suite may never write under while it is measured. The corpus roots — an unversioned
#: PDF under ``files/`` is unique material — plus the trees the release runner hashes after each
#: suite (``scripts/run_release_regressions.py`` GUARDED_TREES), so the two guards agree.
GUARDED_TREES = tuple(sorted(set(CORPUS_ROOTS) | {
    "governance", "roles", "framework/protocols", "framework/instruction", "learning"}))

#: Callee names that mean "the suite harness", never "the tool".
SELF_TEST_NAMES = {"self_test", "_self_test", "selftest", "_selftest", "run_self_test"}

#: Scripts that cannot reach the criterion, each with the reason. An entry here is a decision
#: with a stated cost, never a name quietly dropped from the denominator.
EXPECTED_UNREACHABLE: dict[str, str] = {}

SKIP_MARKERS = ("skipped", "SKIP")


# --------------------------------------------------------------------------------------
# instrumentation
# --------------------------------------------------------------------------------------

_TRACER = '''
import atexit, builtins, io, json, os, sys, threading

_dir = os.environ.get("LEGEND_TRACE_DIR")
if _dir:
    _funcs = set()
    _files = set()
    _writes = []
    _guard = [os.path.abspath(g) for g in json.loads(os.environ.get("LEGEND_TRACE_GUARD", "[]"))]

    def _profile(frame, event, arg):
        if event == "call":
            code = frame.f_code
            _funcs.add(code.co_filename + "::" + code.co_qualname)

    def _abs(path):
        try:
            if isinstance(path, int):
                return None
            return os.path.abspath(os.fsdecode(os.fspath(path)))
        except Exception:
            return None

    def _guarded(path):
        return path is not None and any(
            path == g or path.startswith(g + os.sep) for g in _guard)

    def _refuse(path, mode, op):
        # Recorded first, then refused: the attempt is the evidence, and the bytes never land.
        _writes.append({"path": path, "mode": mode, "op": op})
        raise PermissionError(
            "LEGEND self-test guard: %s %r (mode %r) is under a guarded tree. A suite reads "
            "real artefacts; it never writes them (self_test_coverage.py, "
            "FINDING-20260911-DOSSIER-TRUNCATION)" % (op, path, mode))

    def _note_open(file, mode):
        path = _abs(file)
        if path is None:
            return
        _files.add(path)
        if any(flag in str(mode) for flag in "wax+") and _guarded(path):
            _refuse(path, str(mode), "open")

    _bopen = builtins.open
    _iopen = io.open

    def _open(file, mode="r", *a, **k):
        _note_open(file, mode)
        return _bopen(file, mode, *a, **k)

    def _open_io(file, mode="r", *a, **k):
        _note_open(file, mode)
        return _iopen(file, mode, *a, **k)

    builtins.open = _open
    io.open = _open_io

    def _wrap(name, positions):
        original = getattr(os, name)

        def guarded(*a, **k):
            for position in positions:
                if position < len(a):
                    path = _abs(a[position])
                    if _guarded(path):
                        _refuse(path, "-", name)
            return original(*a, **k)

        guarded.__name__ = name
        setattr(os, name, guarded)

    for _name, _positions in (("remove", (0,)), ("unlink", (0,)), ("rmdir", (0,)),
                              ("truncate", (0,)), ("rename", (0, 1)), ("replace", (0, 1))):
        _wrap(_name, _positions)

    @atexit.register
    def _dump():
        try:
            target = os.path.join(_dir, "%d-%d.json" % (os.getpid(), id(_funcs)))
            with _bopen(target, "w") as handle:
                json.dump({"funcs": sorted(_funcs), "files": sorted(_files),
                           "writes": _writes}, handle)
        except Exception:
            pass

    sys.setprofile(_profile)
    threading.setprofile(_profile)
'''


def _tracer_dir() -> Path:
    """A directory holding ``sitecustomize.py``, to be put on ``PYTHONPATH``.

    ``sitecustomize`` is imported by every interpreter start, including the subprocesses the
    suites spawn, which is the only way to see a CLI driven the way these suites drive it.
    """
    path = Path(tempfile.mkdtemp(prefix="legend-selftest-tracer-"))
    (path / "sitecustomize.py").write_text(_TRACER, encoding="utf-8")
    return path


def guarded_paths(root: Path) -> list[str]:
    return [str((root / tree).resolve()) for tree in GUARDED_TREES]


def run_instrumented(command: list[str], tracer: Path, cwd: Path,
                     timeout: int = 600, root: Path | None = None) -> dict:
    """Run ``command``, returning its result plus every function entered and file opened.

    ``writes`` lists every refused attempt to write, delete, rename or truncate under a
    guarded tree of ``root`` (``cwd`` when ``root`` is not given). The attempt was refused in
    the child before any byte landed; the record is the evidence that it was made.
    """
    with tempfile.TemporaryDirectory(prefix="legend-selftest-trace-") as trace_dir:
        env = dict(os.environ)
        env["LEGEND_TRACE_DIR"] = trace_dir
        env["LEGEND_TRACE_GUARD"] = json.dumps(guarded_paths(root or cwd))
        env["PYTHONPATH"] = os.pathsep.join(
            [str(tracer)] + ([env["PYTHONPATH"]] if env.get("PYTHONPATH") else []))
        env.pop("PYTHONDONTWRITEBYTECODE", None)
        try:
            proc = subprocess.run(command, cwd=str(cwd), env=env, capture_output=True,
                                  text=True, timeout=timeout)
            rc, out = proc.returncode, (proc.stdout or "") + (proc.stderr or "")
        except subprocess.TimeoutExpired:
            rc, out = 124, "TIMEOUT"
        funcs: set[str] = set()
        files: set[str] = set()
        writes: list[dict] = []
        for dump in Path(trace_dir).glob("*.json"):
            try:
                payload = json.loads(dump.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            funcs.update(payload.get("funcs", ()))
            files.update(payload.get("files", ()))
            writes.extend(payload.get("writes", ()))
    return {"rc": rc, "output": out, "funcs": funcs, "files": files, "writes": writes}


def guarded_run(command: list[str], root: Path, timeout: int = 600) -> dict:
    """Run any command with writes under ``root``'s guarded trees refused, and say which.

    This is how a mutation matrix is run: a deliberately broken tool driven through its
    real-artefact cases must not be able to reach the corpus, whatever the mutation is.
    """
    result = run_instrumented(command, _tracer_dir(), root, timeout=timeout, root=root)
    result["refused"] = bool(result["writes"])
    return result


# --------------------------------------------------------------------------------------
# static analysis: what the entry point IS
# --------------------------------------------------------------------------------------

def entry_point_of(source: str) -> dict:
    """Return ``{"main": bool, "callees": [...]}`` for a script's production path.

    ``callees`` are the top-level functions ``main`` calls directly, excluding the self-test
    dispatch. Empty callees means ``main`` does all the work itself, and then entering ``main``
    is the whole of the criterion.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return {"main": False, "callees": []}
    top_level = {node.name for node in tree.body
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
    main = next((node for node in tree.body
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                 and node.name == "main"), None)
    if main is None:
        return {"main": False, "callees": []}
    callees = set()
    for node in ast.walk(main):
        if isinstance(node, ast.Call):
            func = node.func
            name = func.id if isinstance(func, ast.Name) else (
                func.attr if isinstance(func, ast.Attribute) else None)
            if name and name in top_level and name not in SELF_TEST_NAMES and name != "main":
                callees.add(name)
    return {"main": True, "callees": sorted(callees)}


def has_self_test(source: str) -> bool:
    """True only when the script really accepts ``--self-test`` on its command line.

    Substring matching was the first version and it was wrong within the hour: this module's
    own docstring names the flag while its CLI does not accept it, so the survey invoked
    ``self_test_coverage.py --self-test``, argparse exited 2, and the tool reported a failing
    suite that does not exist. A tool whose measurement is confounded by prose about the
    measurement is the defect it exists to find, one level up.
    """
    if "--self-test" not in source:
        return False
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "add_argument"
                and any(isinstance(arg, ast.Constant) and arg.value == "--self-test"
                        for arg in node.args)):
            return True
    return False


def scripts_under(directory: Path) -> list[Path]:
    """Every script carrying a ``--self-test`` or a ``test_*.py`` beside it."""
    found = []
    for path in sorted(directory.glob("*.py")):
        if path.name.startswith("test_") or path.name == "__init__.py":
            continue
        try:
            source = path.read_text(encoding="utf-8")
        except OSError:
            continue
        if has_self_test(source) or (path.parent / f"test_{path.name}").exists():
            found.append(path)
    return found


# --------------------------------------------------------------------------------------
# the measurement
# --------------------------------------------------------------------------------------

def _touched_corpus(files: set[str], root: Path) -> list[str]:
    hits = []
    for name in files:
        try:
            rel = Path(name).resolve().relative_to(root)
        except (ValueError, OSError):
            continue
        text = rel.as_posix()
        if any(text == r or text.startswith(r + "/") for r in CORPUS_ROOTS):
            hits.append(text)
    return sorted(hits)


def measure_script(script: Path, tracer: Path, root: Path,
                   timeout: int = 600) -> dict:
    """Run every suite that belongs to ``script`` and judge the two criteria."""
    source = script.read_text(encoding="utf-8")
    entry = entry_point_of(source)
    suites: list[dict] = []
    commands: list[tuple[str, list[str]]] = []

    test_file = script.parent / f"test_{script.name}"
    if test_file.exists():
        commands.append((test_file.relative_to(root).as_posix(),
                         [sys.executable, str(test_file)]))
    if has_self_test(source):
        commands.append((f"{script.name} --self-test",
                         [sys.executable, str(script), "--self-test"]))

    funcs: set[str] = set()
    files: set[str] = set()
    writes: list[dict] = []
    for label, command in commands:
        result = run_instrumented(command, tracer, root, timeout=timeout, root=root)
        funcs |= result["funcs"]
        files |= result["files"]
        for attempt in result["writes"]:
            writes.append({"suite": label, **attempt})
        suites.append({"suite": label, "rc": result["rc"],
                       "skips": _skip_lines(result["output"])})

    script_path = str(script.resolve())
    entered = {name.split("::", 1)[1] for name in funcs
               if name.split("::", 1)[0] == script_path}
    main_called = "main" in entered
    callees_called = sorted(set(entry["callees"]) & entered)
    if not entry["main"]:
        entry_called = bool(entered)          # no main: any function of the tool counts
    elif entry["callees"]:
        entry_called = main_called and bool(callees_called)
    else:
        entry_called = main_called

    corpus = _touched_corpus(files, root)
    skipped = any(suite["skips"] for suite in suites)
    if corpus:
        real = "true"
    elif skipped:
        real = "skipped_declared"
    else:
        real = "false"

    return {
        "script": script.relative_to(root).as_posix(),
        "suites": suites,
        "entry_point": {"main": entry["main"], "callees": entry["callees"]},
        "entry_point_called": entry_called,
        "entry_point_evidence": {"main_entered": main_called,
                                 "callees_entered": callees_called},
        "real_artifact_case": real,
        "real_artifact_paths": corpus[:10],
        # 🔴 A suite that tried to write under a guarded tree. The attempt was refused before
        # the bytes landed; the record outranks both axes and fails --enforce.
        "guarded_writes": [{"suite": w["suite"], "op": w["op"], "mode": w["mode"],
                            "path": _relative(w["path"], root)} for w in writes],
        "refused": bool(writes),
        "failing": [s["suite"] for s in suites if s["rc"] != 0],
    }


def _relative(path: str, root: Path) -> str:
    try:
        return Path(path).resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path


def _skip_lines(output: str) -> list[str]:
    return [line.strip() for line in output.splitlines()
            if any(marker in line for marker in SKIP_MARKERS)][:5]


def survey(root: Path, only: list[str] | None = None, workers: int = 8,
           timeout: int = 600) -> list[dict]:
    """Measure every qualifying script under ``framework/scripts``."""
    directory = root / "framework" / "scripts"
    targets = scripts_under(directory)
    if only:
        wanted = {Path(name).name for name in only}
        targets = [path for path in targets if path.name in wanted]
    tracer = _tracer_dir()
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        rows = list(pool.map(
            lambda path: measure_script(path, tracer, root, timeout=timeout), targets))
    return sorted(rows, key=lambda row: row["script"])


def render(rows: list[dict]) -> str:
    lines = ["SELF-TEST ENTRY-POINT COVERAGE",
             f"scripts measured: {len(rows)}", ""]
    width = max((len(r["script"]) for r in rows), default=10)
    for row in rows:
        lines.append(
            f"  {row['script']:<{width}}  entry_point_called: "
            f"{str(row['entry_point_called']).lower():<5}  real_artifact_case: "
            f"{row['real_artifact_case']}"
            + ("  REFUSED — wrote under a guarded tree" if row.get("refused") else ""))
    refused = [r for r in rows if r.get("refused")]
    both_false = [r["script"] for r in rows
                  if not r["entry_point_called"] and r["real_artifact_case"] == "false"]
    no_entry = [r["script"] for r in rows if not r["entry_point_called"]]
    no_real = [r["script"] for r in rows if r["real_artifact_case"] == "false"]
    lines += ["",
              f"entry_point_called false : {len(no_entry)}",
              f"real_artifact_case false : {len(no_real)}",
              f"BOTH false               : {len(both_false)}"]
    for name in both_false:
        lines.append(f"    - {name}" + (f"  [expected: {EXPECTED_UNREACHABLE[name]}]"
                                        if name in EXPECTED_UNREACHABLE else ""))
    lines.append(f"REFUSED (wrote under a guarded tree): {len(refused)}")
    for row in refused:
        for attempt in row["guarded_writes"]:
            lines.append(f"    - {row['script']}: {attempt['suite']} {attempt['op']} "
                         f"{attempt['path']} (mode {attempt['mode']})")
    unexpected = [n for n in both_false if n not in EXPECTED_UNREACHABLE]
    lines.append("")
    if refused:
        verdict = (f"REFUSED — {len(refused)} suite(s) tried to write a real artefact; a "
                   "real-artefact case READS, never writes")
    elif unexpected:
        verdict = f"REVIEW — {len(unexpected)} script(s) blind on both axes"
    else:
        verdict = "PASS — no script is blind on both axes, no suite wrote a guarded tree"
    lines.append("VERDICT: " + verdict)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--script", action="append",
                        help="measure only these scripts (by file name)")
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--enforce", action="store_true",
                        help="exit 1 when a script is false on both axes and not expected, "
                             "or when any suite tried to write under a guarded tree")
    parser.add_argument("--guarded", nargs=argparse.REMAINDER, metavar="COMMAND",
                        help="run COMMAND with writes under the guarded trees refused; exit "
                             "1 and list the attempts if any were made, else COMMAND's status")
    args = parser.parse_args()

    if args.guarded:
        result = guarded_run(args.guarded, Path(args.root).resolve(), timeout=args.timeout)
        sys.stdout.write(result["output"])
        for attempt in result["writes"]:
            print(f"GUARDED_WRITE_REFUSED {attempt['op']} {attempt['path']} "
                  f"(mode {attempt['mode']})")
        return 1 if result["refused"] else result["rc"]

    rows = survey(Path(args.root).resolve(), only=args.script, workers=args.workers,
                  timeout=args.timeout)
    if args.as_json:
        print(json.dumps(rows, indent=1))
    else:
        print(render(rows))
    if args.enforce:
        unexpected = [r["script"] for r in rows
                      if not r["entry_point_called"] and r["real_artifact_case"] == "false"
                      and r["script"] not in EXPECTED_UNREACHABLE]
        refused = [r["script"] for r in rows if r.get("refused")]
        return 1 if unexpected or refused else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
