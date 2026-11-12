#!/usr/bin/env python3
"""A verification run in its own clone — created, concluded and removed in one place, with its evidence kept outside the clone.

WHY THIS EXISTS
---------------
On 2026-11-11 a manual clean-up of the VPS removed 28 finished temporary clones (26 GB) from /tmp: release batteries, publication checks and receipt trials,
each created by hand by whichever session needed it and left behind by whichever session finished. Nothing created them in one place, so nothing could remove
them in one place. This module is that place. It builds on `owned_scratch.py` (a box stamped with its owner's PID:START; a name that resembles a battery proves
nothing) and adds the lifecycle around it:

    python3 framework/scripts/verify_run.py run --sha <sha> --label battery --mandate <TASK_ID> [--task-record <record.json>] -- python3 -B scripts/run_release_regressions.py
    python3 framework/scripts/verify_run.py reap          # conclude and remove this session's earlier finished or interrupted runs (idempotent); --session ID names another owner exactly
    python3 framework/scripts/verify_run.py status [RUN_ID]
    python3 framework/scripts/verify_run.py unrecognised  # LIST ONLY: clone-like directories in the temp dir with no manifest of ours

`run` clones the repository (`git clone --no-hardlinks`), checks out the SHA, hard-links the untracked `files/` corpus into the clone (`--files none` to skip),
runs the command in it with stdout and stderr going straight to a log OUTSIDE the clone, and when it ends (pass, fail or interrupt) preserves what is needed
to diagnose and reproduce, then removes that exact directory — if, and only if, every check below holds. A long run is started the usual way
(`setsid nohup python3 verify_run.py run ... &`): that process is the supervisor and owns the box; it is not a service and ends with the run.

The evidence (default `/tmp/legend-verify-keep/<run_id>/`, override with LEGEND_VERIFY_KEEP) holds `manifest.json` (run id, session, actor, mandate, source
repository, SHA, command, supervisor and child identity as PID:START, box path, state, exit code, verdict lines, what was freed or why not), `run.log`,
`clone_state.txt`, any `--keep` artefacts, and `unsaved_changes.tar.gz` when the clone held changes that exist nowhere else. A FAIL keeps the same things: the log,
the command and the SHA reproduce it; the clone is not kept.

Removal checks (all must hold, else the directory is KEPT and the reason is written to the manifest and printed — never a failure of the run):
  * the box is a real directory directly inside the temp dir, owned by this user, named legend-verify-*, carrying this run's `.run_id`, and the same inode
    the manifest recorded; a symlink, a stranger or a look-alike is refused;
  * no process uses it: cwd, executable, open file or memory map under the box, for any process but this one (children included; a launcher that ended proves
    nothing). Nothing is ever killed to make removal possible;
  * the SHA, and every commit any ref of the clone points to, exists in the source repository;
  * changes not in the source (modified or untracked files) are archived first (limit `--max-archive-mb`, default 50) and the archive re-read; more than the
    limit, or a file under `files/` that is not a hard link of the corpus (link count 1: unique data), or an ignored non-cache file with no other link, keeps
    the directory;
  * the log exists and the exit code is recorded.
Removal never follows a symlink (the link is unlinked, its target untouched) and a hard-linked file only loses its name in the clone: the corpus original stays.

Not covered, by design: `files/`, datasets and analytical caches themselves, sessions and scratchpads, Python environments, worktrees (they follow the repository's
own closing cycle), and anything another session or an unrecognised run made. Old temporaries without a manifest are listed by `unrecognised`, never removed by
age or name. A clean-up problem is a diagnosis in the manifest; it does not change the verification verdict and blocks nothing.

Exit codes of `run`: the command's own exit code (a clean-up that keeps the box does not change it) · 2 invalid invocation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import tarfile
import tempfile
import time
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import owned_scratch  # noqa: E402
import process_wait  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
PREFIX = "legend-verify-"
CACHE_NAMES = ("__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache")


def keep_root() -> Path:
    return Path(os.environ.get("LEGEND_VERIFY_KEEP") or Path(tempfile.gettempdir()) / "legend-verify-keep")


def now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def identity(pid: int) -> str:
    start = process_wait.start_ticks(pid)
    return f"{pid}:{start}" if start is not None else f"{pid}"


def alive(ident: str | None) -> bool:
    if not ident:
        return False
    try:
        return process_wait.pid_alive(*process_wait.parse_identity(ident))
    except ValueError:
        return False


def git(repo: Path, *args: str, check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=check, timeout=600)


def load(run_dir: Path) -> dict | None:
    try:
        return json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def save(run_dir: Path, m: dict) -> None:
    tmp = run_dir / "manifest.json.tmp"
    tmp.write_text(json.dumps(m, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, run_dir / "manifest.json")


# ---------------------------------------------------------------------------------------------- checks
def box_problem(m: dict) -> str | None:
    """Why the recorded box is not provably this run's own, or None."""
    for field in ("box", "run_id", "box_inode"):
        if not m.get(field):
            return f"manifest incomplete: no {field}"
    box = Path(m["box"])
    if box.is_symlink():
        return f"{box} is a symlink"
    if not box.exists():
        return "box already absent"
    if not box.name.startswith(PREFIX):
        return f"{box.name} does not carry the {PREFIX} prefix"
    if box.stat().st_ino != m["box_inode"]:
        return "box is not the directory the manifest recorded (different inode)"
    try:
        if (box / ".run_id").read_text(encoding="utf-8").strip() != m["run_id"]:
            return "box carries another run's id"
    except OSError:
        return "box has no .run_id"
    try:
        owned_scratch._check_releasable(box)
    except owned_scratch.Refused as exc:
        return str(exc)
    return None


def processes_using(box: Path) -> list[str]:
    """pid and command of every process (but this one) whose cwd, executable, open file or memory map lies under the box."""
    root = str(box.resolve())
    inside = lambda p: p == root or p.startswith(root + os.sep)  # noqa: E731
    found = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit() or int(entry.name) == os.getpid():
            continue
        hit = False
        for link in ("cwd", "exe", "root"):
            try:
                hit = hit or inside(os.readlink(entry / link))
            except OSError:
                pass
        if not hit:
            try:
                for fd in (entry / "fd").iterdir():
                    try:
                        if inside(os.readlink(fd)):
                            hit = True
                            break
                    except OSError:
                        continue
            except OSError:
                pass
        if not hit:
            try:
                with open(entry / "maps", encoding="utf-8", errors="replace") as fh:
                    hit = any(root + os.sep in line for line in fh)
            except OSError:
                pass
        if hit:
            try:
                cmd = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode("utf-8", "replace").strip()[:80]
            except OSError:
                cmd = "?"
            found.append(f"{entry.name} ({cmd})")
    return found


def unique_bytes(box: Path) -> int:
    """Allocated bytes that removal really frees: files with link count 1, symlinks not followed."""
    total = 0
    for dp, dns, fns in os.walk(box, followlinks=False):
        for fn in fns:
            try:
                st = os.lstat(os.path.join(dp, fn))
            except OSError:
                continue
            if st.st_nlink == 1:
                total += st.st_blocks * 512
    return total


def unsaved(clone: Path, source: Path, sha: str) -> dict:
    """What the clone holds that the source does not: foreign commits, changed or untracked files, unique data under files/, ignored non-cache files."""
    out = {"foreign_commits": [], "changed": [], "unique_corpus": [], "ignored_unique": []}
    refs = git(clone, "for-each-ref", "--format=%(objectname)").stdout.split()
    head = git(clone, "rev-parse", "HEAD").stdout.strip()
    for obj in dict.fromkeys(refs + [head, sha]):
        if git(source, "cat-file", "-e", obj + "^{commit}").returncode != 0:
            out["foreign_commits"].append(obj)
    status = git(clone, "status", "--porcelain=v1", "--ignored", "-z", "--untracked-files=all").stdout
    for rec in [r for r in status.split("\0") if r]:
        code, path = rec[:2], rec[3:]
        if code == "!!":
            if path.startswith("files/") or path == "files/":
                continue
            top = path.rstrip("/").split("/")
            if any(p in CACHE_NAMES for p in top):
                continue
            full = clone / path
            files = [full] if full.is_file() else [Path(dp) / f for dp, _, fs in os.walk(full) for f in fs] if full.is_dir() else []
            if any(not f.is_symlink() and f.lstat().st_nlink == 1 for f in files):
                out["ignored_unique"].append(path)
        else:
            out["changed"].append(path)
    files_dir = clone / "files"
    if files_dir.is_dir() and not files_dir.is_symlink():
        for dp, _, fs in os.walk(files_dir, followlinks=False):
            for f in fs:
                p = Path(dp) / f
                if not p.is_symlink() and p.lstat().st_nlink == 1:
                    out["unique_corpus"].append(str(p.relative_to(clone)))
    return out


def archive(clone: Path, paths: list[str], dest: Path) -> int | None:
    """tar.gz of the listed files (symlinks stored as links, never followed); re-read to prove it. Returns the member count or None."""
    with tarfile.open(dest, "w:gz", dereference=False) as tar:
        for rel in paths:
            full = clone / rel
            if full.exists() or full.is_symlink():
                tar.add(full, arcname=rel, recursive=True)
    with tarfile.open(dest, "r:gz") as tar:
        names = tar.getnames()
    return len(names) if names else None


def tree_size(clone: Path, paths: list[str]) -> int:
    total = 0
    for rel in paths:
        full = clone / rel
        if full.is_symlink():
            continue
        if full.is_file():
            total += full.stat().st_size
        elif full.is_dir():
            total += sum((Path(dp) / f).lstat().st_size for dp, _, fs in os.walk(full) for f in fs if not (Path(dp) / f).is_symlink())
    return total


def corpus_of(source: Path) -> Path | None:
    """The untracked `files/` corpus the run needs: the source's own, else the one of the checkout the source is a worktree of (a worktree has none of its own; a run
    without it silently skips every suite that reads the corpus, and its verdict would not mean what a full one means)."""
    if (source / "files").is_dir():
        return source / "files"
    common = git(source, "rev-parse", "--path-format=absolute", "--git-common-dir").stdout.strip()
    main = Path(common).parent if common else None
    return main / "files" if main and (main / "files").is_dir() else None


# ---------------------------------------------------------------------------------------------- conclusion
def remove_box(box: Path) -> None:
    """rmtree that never follows a symlink and loosens permissions only on directories inside the box."""
    root = os.path.abspath(box)

    def fix(func, path, _exc):
        parent = os.path.dirname(os.path.abspath(path))
        if parent != root and not parent.startswith(root + os.sep):
            raise _exc
        os.chmod(parent, 0o700)
        func(path)
    shutil.rmtree(box, onexc=fix)


def conclude(run_dir: Path, task_record: Path | None = None) -> dict:
    """Preserve, check and remove. Always returns the manifest (state and `cleanup` say what happened); never raises for a clean-up problem."""
    m = load(run_dir)
    if m is None or not m.get("run_id"):
        return {"cleanup": {"state": "KEPT", "reasons": ["manifest unreadable or incomplete: nothing removed"]}, "run_dir": str(run_dir)}
    cl = m.get("cleanup") or {}
    if cl.get("state") == "REMOVED":
        return m
    reasons: list[str] = []
    if m.get("state") == "RUNNING":
        if alive(m.get("supervisor")) or alive(m.get("child")):
            return {**m, "cleanup": {"state": "KEPT", "reasons": ["the run is still alive (supervisor or command)"]}}   # not written: the supervisor owns this manifest
        m["state"], m["finished"] = "INTERRUPTED", now()
        m.setdefault("exit_code", None)
    elif m.get("state") not in ("CONCLUDED", "INTERRUPTED"):
        m["cleanup"] = {"state": "KEPT", "reasons": [f"state {m.get('state')!r} is not a finished run"], "at": now()}
        save(run_dir, m)
        return m
    problem = box_problem(m)
    if problem == "box already absent":
        m["cleanup"] = {"state": "REMOVED", "reasons": ["box already absent"], "at": now()}
        save(run_dir, m)
        return m
    if problem:
        reasons.append(problem)
    else:
        box, clone, source = Path(m["box"]), Path(m["box"]) / "clone", Path(m["source_repo"])
        if not (run_dir / "run.log").is_file():
            reasons.append("no run.log kept")
        if m.get("exit_code") is None and m.get("state") == "CONCLUDED":
            reasons.append("exit code not recorded")
        if not source.is_dir():
            reasons.append("source repository not found")
        elif clone.is_dir():
            state = git(clone, "status", "--short", "--branch").stdout
            (run_dir / "clone_state.txt").write_text(f"HEAD {git(clone, 'rev-parse', 'HEAD').stdout.strip()}\n{state}", encoding="utf-8")
            u = unsaved(clone, source, m["sha"])
            if u["foreign_commits"]:
                reasons.append("clone holds commits absent from the source: " + ", ".join(c[:10] for c in u["foreign_commits"]))
            if u["unique_corpus"]:
                reasons.append(f"{len(u['unique_corpus'])} file(s) under files/ with no other link (unique data), first: {u['unique_corpus'][0]}")
            extra = u["changed"] + u["ignored_unique"]
            m["unsaved"] = {"changed": u["changed"][:50], "ignored_unique": u["ignored_unique"][:50], "count": len(extra)}
            if extra and not reasons:
                if tree_size(clone, extra) > m.get("max_archive_mb", 50) * 1024 * 1024:
                    reasons.append(f"{len(extra)} unsaved file(s) exceed the {m.get('max_archive_mb', 50)} MB archive limit")
                else:
                    n = archive(clone, extra, run_dir / "unsaved_changes.tar.gz")
                    if not n:
                        reasons.append("the archive of unsaved changes could not be re-read")
                    else:
                        m["unsaved"]["archived_members"] = n
            for pattern in m.get("keep_globs") or []:
                for src in sorted(clone.glob(pattern)):
                    if src.is_file() and not src.is_symlink():
                        dest = run_dir / "artefacts" / src.relative_to(clone)
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(src, dest)
                        if hashlib.sha256(src.read_bytes()).hexdigest() != hashlib.sha256(dest.read_bytes()).hexdigest():
                            reasons.append(f"artefact {src.name} did not copy intact")
        using = processes_using(box)
        if using:
            reasons.append("in use by process " + "; ".join(using[:3]))
    if reasons:
        m["cleanup"] = {"state": "KEPT", "reasons": reasons, "at": now()}
    else:
        box = Path(m["box"])
        freed = unique_bytes(box)
        again = box_problem(m) or (f"in use by process {processes_using(box)[0]}" if processes_using(box) else None)   # last look before the removal itself
        if again:
            m["cleanup"] = {"state": "KEPT", "reasons": [again], "at": now()}
        else:
            remove_box(box)
            m["cleanup"] = {"state": "REMOVED", "freed_bytes": freed, "at": now()}
    save(run_dir, m)
    if task_record is None and m.get("task_record"):
        task_record = Path(m["task_record"])
    if task_record is not None:
        point_record(task_record, m, run_dir)
    return m


def point_record(record: Path, m: dict, run_dir: Path) -> None:
    """The mandate record points at the persistent evidence: one entry per run, replaced if the run is concluded again."""
    try:
        data = json.loads(record.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return
    entry = {"run_id": m["run_id"], "label": m.get("label"), "sha": m["sha"], "state": m.get("state"), "exit_code": m.get("exit_code"),
             "evidence_dir": str(run_dir), "log_sha256": hashlib.sha256((run_dir / "run.log").read_bytes()).hexdigest() if (run_dir / "run.log").is_file() else None,
             "clone": (m.get("cleanup") or {}).get("state")}
    items = [x for x in data.get("VERIFICATION_EVIDENCE", []) if x.get("run_id") != m["run_id"]] + [entry]
    data["VERIFICATION_EVIDENCE"] = items
    tmp = record.with_suffix(record.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, record)


# ---------------------------------------------------------------------------------------------- commands
def cmd_run(a) -> int:
    source = Path(a.repo or REPO).resolve()
    sha = git(source, "rev-parse", "--verify", "-q", a.sha + "^{commit}").stdout.strip()
    if not sha:
        print(f"verify_run: {a.sha} is not a commit of {source}", file=sys.stderr)
        return 2
    command = [c for c in a.command if c != "--"] if a.command and a.command[0] == "--" else a.command
    if not command:
        print("verify_run: no command given after --", file=sys.stderr)
        return 2
    cleanup_previous(os.environ.get("CLAUDE_CODE_SESSION_ID", ""))            # an interrupted earlier run of this session is concluded first
    run_id = time.strftime("%Y%m%d-%H%M%S", time.gmtime()) + "-" + uuid.uuid4().hex[:8]
    run_dir = keep_root() / run_id
    run_dir.mkdir(parents=True)
    box = owned_scratch.make(PREFIX)
    (box / ".run_id").write_text(run_id + "\n", encoding="utf-8")
    m = {"run_id": run_id, "state": "STARTING", "label": a.label, "session": os.environ.get("CLAUDE_CODE_SESSION_ID", ""), "actor": a.actor or os.environ.get("LEGEND_ACTOR_ID", ""),
         "mandate": a.mandate or "", "source_repo": str(source), "sha": sha, "command": command, "supervisor": identity(os.getpid()), "box": str(box),
         "box_inode": box.stat().st_ino, "created": now(), "log": str(run_dir / "run.log"), "keep_globs": a.keep, "max_archive_mb": a.max_archive_mb,
         "task_record": str(Path(a.task_record).resolve()) if a.task_record else "", "host": os.uname().nodename}
    save(run_dir, m)
    print(f"RUN {run_id}\nEVIDENCE {run_dir}\nBOX {box}", flush=True)
    clone = box / "clone"
    try:
        for step in (["git", "clone", "-q", "--no-hardlinks", str(source), str(clone)], ["git", "-C", str(clone), "checkout", "-q", sha]):
            subprocess.run(step, check=True, capture_output=True, timeout=1800)
        corpus = corpus_of(source) if a.files == "link" else None
        if corpus is not None:
            subprocess.run(["cp", "-al", str(corpus), str(clone / "files")], check=True, capture_output=True, timeout=1800)
        m["files_linked_from"] = str(corpus) if corpus else None
        save(run_dir, m)
    except (subprocess.SubprocessError, OSError) as exc:
        m.update(state="CONCLUDED", exit_code=125, finished=now(), verdict_lines=[f"setup failed: {exc}"])
        save(run_dir, m)
        return finish(run_dir, m, 125)
    with open(run_dir / "run.log", "wb") as log:
        child = subprocess.Popen(command, cwd=clone, stdout=log, stderr=subprocess.STDOUT, start_new_session=True,
                                 env={**os.environ, "LEGEND_VERIFY_RUN_ID": run_id})
        m.update(state="RUNNING", child=identity(child.pid), started=now())
        save(run_dir, m)
        interrupted = []

        def forward(signum, _frame):
            interrupted.append(signum)
            try:
                os.killpg(child.pid, signum)       # the operator's own interrupt reaches the run; nothing is killed to make a removal possible
            except OSError:
                pass
        old = {s: signal.signal(s, forward) for s in (signal.SIGTERM, signal.SIGINT)}
        code = child.wait()
        for s, h in old.items():
            signal.signal(s, h)
    tail = (run_dir / "run.log").read_text(encoding="utf-8", errors="replace").splitlines()[-15:]
    m.update(state="INTERRUPTED" if interrupted else "CONCLUDED", exit_code=code, finished=now(), signals=interrupted,
             verdict_lines=[l for l in tail if l.startswith(("VERDICT", "RESULT", "FAILED", "OK", "PASS", "FAIL"))][:6] or tail[-3:])
    save(run_dir, m)
    return finish(run_dir, m, code if not interrupted else 128 + interrupted[0])


def finish(run_dir: Path, m: dict, code: int) -> int:
    m = conclude(run_dir)
    cl = m.get("cleanup", {})
    freed = cl.get("freed_bytes")
    print(f"STATE {m.get('state')} exit {m.get('exit_code')} | clone {cl.get('state')}"
          + (f" (freed {freed / 1e9:.2f} GB)" if freed else "") + ("; kept because: " + "; ".join(cl.get("reasons", [])) if cl.get("state") == "KEPT" else ""))
    for line in m.get("verdict_lines", []):
        print("  " + line)
    print(f"EVIDENCE {run_dir}")
    return code


def cleanup_previous(session: str) -> list[dict]:
    """Conclude earlier runs of exactly this session that are finished or whose processes are gone. Others are never touched: two sessions may share an
    ACTOR_ID, which names a role and not an owner (HE47 H6)."""
    done = []
    root = keep_root()
    if not root.is_dir() or not session:
        return done
    for run_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        m = load(run_dir)
        if not m or (m.get("cleanup") or {}).get("state") == "REMOVED" or m.get("session") != session:
            continue
        done.append(conclude(run_dir))
    return done


def other_sessions_of(actor: str, own: str) -> list[dict]:
    """Unremoved runs that carry this actor but belong to another session: listed so their owner can reap them, never concluded here."""
    root = keep_root()
    found = []
    for run_dir in sorted(p for p in root.iterdir() if p.is_dir()) if root.is_dir() else []:
        m = load(run_dir)
        if m and (m.get("cleanup") or {}).get("state") != "REMOVED" and actor and m.get("actor") == actor and m.get("session") != own:
            found.append(m)
    return found


def cmd_reap(a) -> int:
    own = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    session = a.session or own
    if not session:
        print("verify_run: no session id in the environment; pass --session with the exact id of the owner", file=sys.stderr)
        return 2
    results = cleanup_previous(session)
    for m in results:
        cl = m.get("cleanup", {})
        print(f"{m.get('run_id')} {m.get('state')} -> clone {cl.get('state')}" + ("; " + "; ".join(cl.get("reasons", [])) if cl.get("state") == "KEPT" else ""))
    print(f"{len(results)} run(s) examined")
    for m in other_sessions_of(a.actor, own) if a.actor else []:
        print(f"NOT TOUCHED {m.get('run_id')} actor {m.get('actor')} belongs to session {m.get('session')}; its owner reaps it, or reap --session {m.get('session')}")
    return 0


def cmd_status(a) -> int:
    root = keep_root()
    for run_dir in sorted(p for p in root.iterdir() if p.is_dir()) if root.is_dir() else []:
        if a.run_id and run_dir.name != a.run_id:
            continue
        m = load(run_dir)
        if m:
            cl = m.get("cleanup") or {}
            print(f"{m['run_id']} {m.get('state')} exit={m.get('exit_code')} clone={cl.get('state', 'PRESENT')} {m.get('label')} {m['sha'][:10]} mandate={m.get('mandate')}")
    return 0


def cmd_unrecognised(_a) -> int:
    tmp = Path(tempfile.gettempdir())
    known = set()
    root = keep_root()
    for run_dir in root.iterdir() if root.is_dir() else []:
        m = load(run_dir)
        if m and m.get("box"):
            known.add(m["box"])
    n = 0
    for p in sorted(tmp.iterdir()):
        if p.is_symlink() or not p.is_dir() or str(p) in known:
            continue
        if (p / ".git").exists() or (p / "clone" / ".git").exists():
            n += 1
            print(f"{p}\tmtime {time.strftime('%Y-%m-%d %H:%M', time.localtime(p.stat().st_mtime))}\towner file {'yes' if (p / owned_scratch.OWNER).exists() else 'no'}\tNOT REMOVED (no manifest of ours)")
    print(f"{n} clone-like director(ies) with no manifest of ours; listed only")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--sha", required=True)
    r.add_argument("--repo", default="")
    r.add_argument("--label", default="verification")
    r.add_argument("--mandate", default="")
    r.add_argument("--actor", default="")
    r.add_argument("--task-record", default="")
    r.add_argument("--files", choices=("link", "none"), default="link")
    r.add_argument("--keep", action="append", default=[], help="glob under the clone whose matches are copied to the evidence directory")
    r.add_argument("--max-archive-mb", type=int, default=50)
    r.add_argument("command", nargs=argparse.REMAINDER)
    p = sub.add_parser("reap")
    p.add_argument("--session", default="", help="exact session id whose runs to conclude (default: this session)")
    p.add_argument("--actor", default="", help="list, without touching, runs of this actor that belong to other sessions")
    s = sub.add_parser("status")
    s.add_argument("run_id", nargs="?", default="")
    sub.add_parser("unrecognised")
    a = ap.parse_args(argv)
    return {"run": cmd_run, "reap": cmd_reap, "status": cmd_status, "unrecognised": cmd_unrecognised}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
