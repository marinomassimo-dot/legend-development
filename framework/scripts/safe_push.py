#!/usr/bin/env python3
"""Push a ref only when the publication gate PASSes on the EXACT commit being published.

Why this exists. On 2026-09-09 a push ran with the gate in BLOCK_PUBLICATION, because
the gate and the push were chained in one shell command:

    python3 scripts/public_release_gate.py | grep VERDICT; git push development main:main

Chaining with `;` runs the push whatever the gate said, and even `&&` would only couple
the two in time -- not to the same commit. This tool makes both couplings structural:

  1. the working tree must be clean (a dirty tree means the gate did not judge HEAD);
  2. the gate runs here and its exit status decides -- it is never a printed opinion;
  3. HEAD is captured BEFORE the gate and re-read AFTER it, and the push is refused if
     it moved, so the SHA gated is the SHA pushed;
  4. the refspec is checked for force in any spelling;
  5. after the push, `git ls-remote` must return exactly the pushed SHA -- read from the
     remote, never from the local tracking ref, which a failed push leaves stale;
  6. the push SOURCE is the gated SHA itself (`<sha>:refs/heads/<branch>`), never the local
     `<branch>` ref: until 2026-09-24 the tool gated HEAD and pushed `<branch>:<branch>`, so
     a local branch that did not point at HEAD was published ungated and caught only by the
     after-the-fact check in (5).

`-h`/`--help` prints this text and does nothing else. Any other option-shaped remote or branch
is refused before the gate or git runs: `safe_push.py --help` used to take `--help` as the
remote name and walk the whole push workflow (2026-09-24; nothing was published).

  7. `--expect-sha <rev>` binds the caller's INTENTION to the commit: when given, the push is refused
     before the gate runs unless HEAD is exactly that commit. Without it the tool publishes whatever HEAD
     is, which on 2026-11-07 was another session's integration commit: the caller's
     `git merge --ff-only <candidate>` had failed because main moved, the next command ran anyway, and
     the push published the commit that was checked out (gate PASS on the SHA published, but not the SHA
     meant). Callers that merge or check out a candidate first should pass it.

  8. `--serialize` makes publishers take turns. The gate takes 7 to 12 minutes and every other session's push moves the remote under it, so on 2026-11-16 seven gates ran to
     completion and were refused at the push ("HEAD moved" / non-fast-forward) because five sessions gated at once. With `--serialize` the tool takes an exclusive flock on
     `<git common dir>/legend_land.lock` (shared by every worktree of the repository; the kernel releases it when the process dies, so a crashed gate cannot deadlock the queue),
     THEN fetches the branch. When the remote tip is not an ancestor of HEAD, the tool MERGES it under the lock (`git merge --no-edit FETCH_HEAD`) and gates and pushes that merged commit
     (2026-11-16: the lock is not first-come-first-served, and a waiter that acquired it after the holder landed was refused and had to retry, three to eleven minutes a try). Safeguards:
     `--expect-sha` binds the caller's commit BEFORE the merge (the merged commit is not what it names); only a CLEAN merge is accepted: on a conflict the merge is aborted, the tree and
     HEAD are left as they were, the conflicting paths are named and nothing is gated or pushed; the tree is clean before and after; no merge happens when the tip is already an ancestor;
     one line `MERGED <tip> into <old> -> <new> under the landing lock` shows the SHA that changed. Nothing else changes: the clean tree, the expectation, the gate verdict, the HEAD re-read after the gate, the fast-forward push of the gated SHA and the ls-remote confirmation are the same code paths. `--lock-timeout <s>`
     refuses instead of waiting longer than that (default: wait).

  9. The lock alone is not first-come-first-served (waiters poll with LOCK_NB and sleep, so whoever polls at the right instant wins; on 2026-11-16 one publisher waited 44 minutes behind four
     others who kept re-entering). With `--serialize` every waiter therefore takes a TICKET in `<git common dir>/legend_land.queue` (pid, process start time, UTC) and only the HEAD ticket may
     try the lock: publishers land in arrival order. A ticket whose process is gone (killed, crashed) is pruned by the next waiter, so a dead waiter never blocks the queue; the holder's
     ticket is removed when it finishes. The position is printed once ('queue position 3 of 4'). The gate, the expectation, the merge under the lock, the HEAD re-read and the ls-remote
     confirmation are unchanged. A publisher running an OLDER copy of this tool does not take a ticket and still competes for the bare lock: the order is strict only among new copies.
  10. Derived-surface regeneration (THE DEFAULT under `--serialize` since 2026-11-25; `--no-regenerate-derived` opts out; `--regenerate-derived` asks by name; opt-in from 2026-11-19): after the merge, under the lock, `candidate_tree_freshness.py --regenerate` regenerates the derived surfaces that are stale
     on the merged tip and commits exactly those files; the gate then judges that commit and it is the one pushed (`REGENERATED ... a -> b` is printed). Used by whoever records receipts,
     so that coverage_report.md, reading_state.md and ranking.json are not behind their sources on the pushed SHA. About 80 s of lock time (the two lines `derived-surface regeneration step Ns` and
     `landing lock held Ms` give it per push). A failed regeneration refuses only when the flag was asked by name; by default it prints a WARNING and the push goes on. The CI gate is untouched
     (operator-reserved): this is a landing-path change. Without `--serialize` nothing is regenerated.

  11. Committed derived views are checked on the tip that is about to be gated (2026-11-24, ADV): `repurposing_view.py check` (the committed full and shareable pages equal a fresh build)
     `repurposing_view.py i18n --what check` (the committed i18n content inventory equals a fresh collection) and `repurposing_view.py package --check` (the committed `view/shareable_package/` and the DEPLOY.md file table equal a fresh build; about 22 s; added 2026-11-24 after CI #2187/#2188 went red because two page refreshes skipped the package and the first two checks cannot see it) run after the merge and any regeneration, before the gate, and a stale
     answer REFUSES with the exact regeneration commands, so a stale view is caught in about 12 s here instead of by an 18-minute CI suite after it landed (CI red since #2129). It
     applies to every publisher, `--serialize` or not; a repository without `framework/scripts/repurposing_view.py` skips it; nothing is loosened and nothing is written.

  12. Free space is checked at the START and again just before the gate (2026-11-24, ADV-207): `/` was 100% full (219 MB free) and a landing died midway with 'No space left on device'. The tool refuses,
     before any lock, gate or merge, when the directory the gate builds a clone in (tempfile's: TMPDIR, else /tmp) or the repository's own filesystem has less than 2 GB free, names the number and
     the path, and points at `tmp_clone_report.py` once that tool exists. 2 GB = twice the MEASURED peak of one release-mode gate clone: `public_release_gate.py --mode release` run with TMPDIR set to
     an empty folder and `du -sk` of it sampled every 2 s: peak 856,524 KB (tar of `git archive HEAD` 425 MB plus its extraction), clean tree, PASS. The staging-mode gate that this tool runs builds NO clone
     (same sampling: peak 4 KB). `--regenerate-derived` builds a candidate tree under `<tmp>/legend-candidate-tree-*` (the path of the 04:50Z incident): sampled the same way its peak is 444,432 KB with the
     default checks and with `--all`, so the release-mode clone is the larger of the two. The merge writes only the changed files; the 2 GB is headroom for the larger run and the object store.
     `LEGEND_SAFE_PUSH_MIN_FREE_GB` overrides the threshold (tests, or an operator who knows better). Read-only; an unreadable filesystem does not refuse.

  13. Landing suites (THE DEFAULT under `--serialize` since 2026-11-25, ADV; `--landing-suites` asks by name, also without `--serialize`): after the merge and any regeneration, before the gate, the suites that
     `landing_suites.py` selects for the paths this push adds to the branch are run one by one and printed (`LANDING-SUITE PASS|RED|TIMEOUT <entry>`). A suite this push turns red REFUSES the push: a red one is rerun
     in a throwaway shared clone of the remote tip, and only a failing test line that is not there refuses (a suite already red on the tip prints `PRE-EXISTING RED` with the failing tests and the push goes on, the §21d wording "turns no green
     suite red"). A selection that cannot be built is said and does not refuse. `--no-landing-suites` (with `--serialize`) skips them and adds an empty commit carrying the trailer `Landing-Suites: skipped
     (--no-landing-suites)`, so the skip is in the published history. This holds the landing lock for as long as the suites take (95 s for an 8-suite selection on 2026-11-25). A selection is not the release battery.

  14. Concurrent checks (THE DEFAULT under `--serialize`, 2026-11-25, ADV): the view checks, the gate and the landing suites start together instead of one after another. The gate reads the live worktree, so the
     suites do not run in it: they run in a throwaway clone of the commit being gated (`git clone --no-hardlinks`, only `files/` hard-linked when the checkout has one), removed by this tool on success, refusal,
     error, SIGTERM and Ctrl-C (a SIGKILL leaves `<tmp>/legend-landing-suites-*`). Refusals and their order are unchanged: suites, unclean tree, views, gate; a refusal stops what is still running. When no clone
     can be built the suites run in the worktree after the gate and the views have finished. `--serial-checks` runs everything one after another and adds an empty commit with the trailer
     `Landing-Checks: serial (--serial-checks)`. `LANDING CHECKS parallel: ...` gives the wall time and each part. Kept after the first ten such landings (median lock held 138.5 s against 250 s).

  15. Copied card sentences (THE DEFAULT under `--serialize`, 2026-11-25, ADV): before the heavy checks, `copied_card_sentences.py --base <remote tip>` asks whether a view page, a coverage or ranking file or a
     hand-kept investigation table still holds a card sentence that this push replaced, and refuses naming the file, the card and the exact old text (exit 3 of the tool refuses too). Only pushes that change
     a card are affected. `--no-copied-sentence-check` skips it and adds an empty commit with the trailer `Copied-Sentence-Check: skipped (--no-copied-sentence-check)`.

  16. A merge that changes this tool (2026-11-25): the merge of step 11 can bring a newer safe_push.py while this process still runs the sequence it loaded before the merge (a card-changing publication
     went out without check 15 that way, from a worktree one landing behind). When the file differs after the merge the push is refused before any check; the merge commit stays, and running again with
     the merged SHA runs the new sequence.

  17. Free space counts the other live runs that write clones (2026-11-28, ADV-299: free space fell from 3.1 to 1.7 GB under ONE publisher, a regeneration of about 0.46 GB then a suite clone of
     about 0.93 GB, and the 2 GB floor of step 12 did not see a second one). A LIVE heavy run is a `safe_push.py` that has a child process (a publisher waiting in the queue has none and writes
     nothing), a `run_release_regressions.py`, a release-mode `public_release_gate.py` or a `candidate_tree_freshness.py`, seen in /proc, so older copies and other repositories count too; this
     process, its parents and its children are not counted, nor is a test fixture (LEGEND_SAFE_PUSH_ROOT set). Declared peaks: PEAK_GB. Under the lock, before the merge and the regeneration, and
     again before the parallel checks, the floor is 2 GB PLUS the declared peaks of those runs: when it is not met the tool WAITS (`LEGEND_SAFE_PUSH_DISK_WAIT_S`, default 600 s) and refuses only
     if the space does not come back; with no live run it refuses at once, as before. At the start, a `--serialize` push whose shortage the live runs account for (they will give it back) joins the
     queue instead of being refused. A waiting publisher has no child, so two of them never wait for each other. Not covered: two publishers that pass the check in the same instant.

Usage: safe_push.py <remote> [<branch>] [--expect-sha <rev>] [--serialize [--lock-timeout <s>] [--no-regenerate-derived] [--no-landing-suites] [--serial-checks] [--no-copied-sentence-check]] [--landing-suites]      (default branch: main)
"""
from __future__ import annotations
import atexit, contextlib, fcntl, importlib.util, os, shutil, signal, subprocess, sys, tempfile, threading, time
from datetime import datetime, timezone
from pathlib import Path

# Read once, when the process loads its own code: step 16 compares the file with this after a merge.
LOADED_SELF = Path(__file__).read_bytes()

# The root is overridable so the refusals can be exercised against a throwaway repo with a
# stub gate. A tool whose failure paths cannot be tested is the shape of the defect it exists
# to prevent.
ROOT = Path(os.environ.get("LEGEND_SAFE_PUSH_ROOT", Path(__file__).resolve().parents[2]))
GATE = Path(os.environ.get("LEGEND_SAFE_PUSH_GATE", ROOT / "scripts" / "public_release_gate.py"))
REGEN = Path(os.environ.get("LEGEND_SAFE_PUSH_REGEN", ROOT / "framework" / "scripts" / "candidate_tree_freshness.py"))
COPIES = Path(os.environ.get("LEGEND_SAFE_PUSH_COPIES", ROOT / "framework" / "scripts" / "copied_card_sentences.py"))
VIEWTOOL = Path(os.environ.get("LEGEND_SAFE_PUSH_VIEWTOOL", ROOT / "framework" / "scripts" / "repurposing_view.py"))
VIEW_FIX = ("python3 -B framework/scripts/repurposing_view.py run && python3 -B framework/scripts/repurposing_view.py run --source shareable && "
            "python3 -B framework/scripts/repurposing_view.py package && python3 -B framework/scripts/repurposing_view.py i18n --what collect")


def _start_ticks(pid: int) -> str:
    """Process start time in clock ticks from /proc (Linux), so a reused pid is not mistaken for the waiter that died; '' when unreadable."""
    try:
        return Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()[19]
    except (OSError, IndexError):
        return ""


def _alive(pid: int, ticks: str) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        pass
    return ticks == "" or _start_ticks(pid) in ("", ticks)


class Queue:
    """FIFO ticket queue next to the landing lock: `<git common dir>/legend_land.queue`, one line per waiter `pid start_ticks utc`. A short flock on `legend_land.queue.lock`
    guards each read-modify-write. Only the HEAD ticket may try the landing lock; a ticket whose process is gone (killed, crashed) is pruned by the next waiter, so a dead waiter
    never blocks the queue; the ticket of the holder stays until it finishes, which is what keeps the order strict."""

    def __init__(self, common: Path):
        self.path, self.guard = common / "legend_land.queue", common / "legend_land.queue.lock"
        self.me = (os.getpid(), _start_ticks(os.getpid()))

    def _txn(self, fn):
        with open(self.guard, "a+") as g:
            fcntl.flock(g, fcntl.LOCK_EX)
            rows = []
            if self.path.exists():
                for ln in self.path.read_text().splitlines():
                    f = ln.split()
                    if len(f) >= 2 and f[0].isdigit() and _alive(int(f[0]), f[1]):
                        rows.append(ln)
            rows = fn(rows)
            self.path.write_text("".join(r + "\n" for r in rows))
            return rows

    def join(self):
        mine = f"{self.me[0]} {self.me[1]} {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"
        return self._txn(lambda rows: rows + [mine])

    def leave(self):
        self._txn(lambda rows: [r for r in rows if r.split()[0] != str(self.me[0])])

    def position(self):
        rows = self._txn(lambda rows: rows)
        pids = [r.split()[0] for r in rows]
        return (pids.index(str(self.me[0])) + 1 if str(self.me[0]) in pids else 0), len(rows)


def run(*cmd, **kw):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, **kw)


def stale_derived_views(runner=None) -> str:
    """'' when the committed repurposing views and the i18n inventory are current (or the repository has no such tool); otherwise the tool's own words. Read-only: neither check writes."""
    if not VIEWTOOL.is_file():
        return ""
    for args in (["check"], ["i18n", "--what", "check"], ["package", "--check"]):
        r = (runner or run)(sys.executable, "-B", str(VIEWTOOL), *args)
        words = [l.strip() for l in (r.stdout + r.stderr).splitlines() if "STALE" in l]
        if r.returncode != 0 or words:
            return (f"[repurposing_view.py {' '.join(args)}] " + (" | ".join(words) or f"exited {r.returncode}"))[:600]
    return ""


# Free space the gate needs where it builds its clean clone (tempfile's directory: TMPDIR, else /tmp). MEASURED 2026-11-24 (ADV-207): see the module docstring, item 12.
MIN_FREE_GB = float(os.environ.get("LEGEND_SAFE_PUSH_MIN_FREE_GB", "2"))
CLONE_REPORT = ROOT / "framework" / "scripts" / "tmp_clone_report.py"


# Declared peak, in GB, of the scratch copies one live run of each tool holds (step 17; ADV-299 trace of 2026-11-28 for safe_push, the step 12 measurements for the other two; a battery is
# taken as large as a publisher).
PEAK_GB = {"safe_push.py": 1.4, "run_release_regressions.py": 1.4, "public_release_gate.py": 0.86, "candidate_tree_freshness.py": 0.45}
DISK_WAIT_S = float(os.environ.get("LEGEND_SAFE_PUSH_DISK_WAIT_S", "600"))
DISK_POLL_S = 10.0
PROC = Path(os.environ.get("LEGEND_SAFE_PUSH_PROC_ROOT", "/proc"))


def _heavy_script(argv: list[str]) -> str:
    """The name in PEAK_GB of the script a python process runs, or ''. A shell or `timeout` that merely names the script is not it."""
    if not argv or not os.path.basename(argv[0]).startswith("python"):
        return ""
    for i, word in enumerate(argv[1:], 1):
        if word in ("-c", "-m"):
            return ""
        if not word.startswith("-"):
            name = os.path.basename(word)
            rest = argv[i + 1:]
            if name == "public_release_gate.py" and not ("--mode=release" in rest or ("--mode", "release") in zip(rest, rest[1:])):
                return ""      # the staging-mode gate builds no clone
            return name if name in PEAK_GB else ""
    return ""


def live_heavy_runs(proc: Path | None = None, me: int | None = None) -> list[tuple[int, str, float]]:
    """[(pid, script, declared peak GB)] of the runs of step 17 that are writing now. Read-only; a process that vanishes or cannot be read is not counted."""
    proc, me = proc or PROC, me or os.getpid()
    parent, heavy = {}, {}
    try:
        entries = [e for e in proc.iterdir() if e.name.isdigit()]
    except OSError:
        return []
    for entry in entries:
        try:
            parent[int(entry.name)] = int((entry / "stat").read_text().rsplit(")", 1)[1].split()[1])
            name = _heavy_script((entry / "cmdline").read_bytes().decode("utf-8", "replace").split("\0"))
            if name:
                heavy[int(entry.name)] = name
        except (OSError, IndexError, ValueError):
            continue

    def chain(pid):
        seen = []
        while pid in parent and pid not in seen:
            seen.append(pid)
            pid = parent[pid]
        return seen

    mine = chain(me) or [me]
    top = next((pid for pid in reversed(mine) if pid == me or pid in heavy), me)      # my own family starts at my outermost heavy ancestor
    working = set(parent.values())
    counted = {pid for pid, name in heavy.items() if pid not in mine and top not in chain(pid) and (name != "safe_push.py" or pid in working)}
    runs = []
    for pid in sorted(counted):
        if any(above in counted for above in chain(pid)[1:]):      # one family is one run
            continue
        try:
            if b"LEGEND_SAFE_PUSH_ROOT=" in (proc / str(pid) / "environ").read_bytes():
                continue
        except OSError:
            pass
        runs.append((pid, heavy[pid], PEAK_GB[heavy[pid]]))
    return runs


def free_space_refusal(floor: float | None = None, why: str = "") -> str:
    """'' when both the directory the gate builds a clone in (tempfile's: TMPDIR, else /tmp) and the repository's own filesystem (the merge, the regeneration and the object store write there)
    have `floor` (default MIN_FREE_GB) free; otherwise the refusal text naming the scarcer one. Read-only."""
    floor = MIN_FREE_GB if floor is None else floor
    worst = None
    for where in (Path(tempfile.gettempdir()), ROOT):
        try:
            free = shutil.disk_usage(where).free / 1e9
        except OSError:
            continue          # an unreadable filesystem is not a reason to refuse; the gate will say what it finds
        if free < floor and (worst is None or free < worst[0]):
            worst = (free, where)
    if worst is None:
        return ""
    hint = " List your dead clones with `python3 framework/scripts/tmp_clone_report.py`." if CLONE_REPORT.is_file() else ""
    return (f"free space {worst[0]:.1f} GB at {worst[1]} is below {floor:g} GB ({why or 'twice the measured peak, 0.86 GB, of one release-mode gate clone'}): remove a clone or a scratch folder of yours first.{hint} "
            "Nothing was gated or pushed.")


def _named(runs) -> str:
    return ", ".join(f"pid {pid} {name} {peak:g} GB" for pid, name, peak in runs)


def wait_for_space() -> str:
    """'' once the free space covers MIN_FREE_GB plus the declared peaks of the other live runs, waiting for them up to DISK_WAIT_S; otherwise the refusal. With no live run nothing will
    give space back, so a shortage refuses at once."""
    started, said = time.time(), False
    while True:
        runs = live_heavy_runs()
        reserved = sum(peak for _, _, peak in runs)
        short = free_space_refusal(MIN_FREE_GB + reserved, f"{MIN_FREE_GB:g} GB plus {reserved:g} GB for the live run(s) {_named(runs)}" if runs else "")
        if not short:
            if said:
                print(f"disk space available after {time.time() - started:.0f}s", flush=True)
            return ""
        if not runs:
            return short
        if time.time() - started >= DISK_WAIT_S:
            return f"{short} Waited {time.time() - started:.0f}s."
        if not said:
            print(f"waiting for disk space (up to {DISK_WAIT_S:.0f}s): {short.split(':')[0]}", flush=True)
            said = True
        time.sleep(min(DISK_POLL_S, max(0.1, DISK_WAIT_S - (time.time() - started))))


SUITE_TIMEOUT_S = 1500
SKIP_TRAILER = "Landing-Suites: skipped (--no-landing-suites)"
NOTICE_UNTIL = "2026-11-26"   # UTC date, inclusive: the one-day announcement in every serialized push log
NOTICE = ("NOTICE (until " + NOTICE_UNTIL + "): safe_push --serialize now runs the selected landing suites and REFUSES a push that turns one red "
          "(a failure already on the remote tip does not refuse); --no-landing-suites skips them and records the skip in the history.")


SERIAL_TRAILER = "Landing-Checks: serial (--serial-checks)"
COPIES_TRAILER = "Copied-Sentence-Check: skipped (--no-copied-sentence-check)"


def held_card_sentences(base: str, sha: str) -> str:
    """'' when no current surface still holds a card sentence that `base..sha` replaced (or the repository has no such tool); otherwise the refusal, in the tool's own words."""
    if not COPIES.is_file():
        return ""
    started = time.time()
    done = run(sys.executable, "-B", str(COPIES), "--repo", str(ROOT), "--base", base, "--head", sha)
    said = (done.stdout + done.stderr).strip()
    print(f"{said.splitlines()[0] if said else 'COPIED_CARD_SENTENCES: (no output)'} ({time.time() - started:.0f}s)", flush=True)
    if done.returncode == 0:
        return ""
    head = ("a copy still holds a card sentence that this push replaced" if done.returncode == 1
            else f"the copied-sentence check could not run (exit {done.returncode})")
    return (f"{head}:\n{said[:6000]}\nRepair, commit, run safe_push again; --no-copied-sentence-check publishes anyway and records it in the history. "
            "Nothing was gated or pushed.")

SUITE_CLONE_PREFIX = "legend-landing-suites-"
_CHILDREN: list[subprocess.Popen] = []      # the processes of the checks that run beside the suites, so that a refusal or a signal leaves none of them running
_STOPPING = threading.Event()


def run_stoppable(*cmd) -> subprocess.CompletedProcess:
    """`run`, with the process on a list that `stop_background` kills."""
    if _STOPPING.is_set():
        return subprocess.CompletedProcess(cmd, -9, "", "stopped")
    process = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    _CHILDREN.append(process)
    out, err = process.communicate()
    return subprocess.CompletedProcess(cmd, process.returncode, out, err)


def stop_background() -> None:
    _STOPPING.set()
    for process in list(_CHILDREN):
        if process.poll() is None:
            process.kill()
    _CHILDREN.clear()


class Background:
    """One check on a daemon thread; `get` waits for it and returns what it returned."""

    def __init__(self, job):
        self.seconds, self._value, self._error = 0.0, None, None
        self._thread = threading.Thread(target=self._go, args=(job,), daemon=True)
        self._thread.start()

    def _go(self, job) -> None:
        started = time.time()
        try:
            self._value = job()
        except BaseException as exc:      # raised again by get(), in the thread that decides
            self._error = exc
        self.seconds = time.time() - started

    def get(self):
        self._thread.join()
        if self._error is not None:
            raise self._error
        return self._value


@contextlib.contextmanager
def suite_clone(sha: str, remote: str):
    """(clone, '') of `sha` in a throwaway folder, or (None, why). The recipe of the release battery: `git clone --no-hardlinks`, only `files/` hard-linked (a hard-linked whole copy lets a suite
    rewrite tracked files of the real checkout). The remote-tracking refs of `remote` are copied so a suite sees them as in the worktree. The folder is removed on the way out, whatever happened."""
    holder, clone, why = None, None, ""
    try:
        try:
            holder = Path(tempfile.mkdtemp(prefix=SUITE_CLONE_PREFIX))
            target = holder / "repo"
            steps = [("git", "clone", "-q", "--no-hardlinks", "--no-checkout", str(ROOT), str(target))]
            if (ROOT / "files").exists():
                steps.append(("cp", "-al", str(ROOT / "files"), str(target / "files")))
            if remote in run("git", "remote").stdout.split():      # a URL or a path has no remote-tracking refs to copy
                steps.append(("git", "-C", str(target), "fetch", "-q", str(ROOT), f"+refs/remotes/{remote}/*:refs/remotes/{remote}/*"))
            steps.append(("git", "-C", str(target), "checkout", "-q", "--detach", sha))
            for step in steps:
                done = run(*step)
                if done.returncode != 0:
                    why = f"{step[0]} {step[3] if step[1] == '-C' else step[1]} failed: {done.stderr.strip()[:200]}"
                    break
            else:
                clone = target
        except OSError as exc:
            why = f"{type(exc).__name__}: {str(exc)[:200]}"
        yield clone, why
    finally:
        if holder is not None:
            shutil.rmtree(holder, ignore_errors=True)
            if holder.exists():
                print(f"WARNING: the suite clone {holder} could not be removed completely; remove it by hand", flush=True)


def _run_suite(entry: str, cwd: Path) -> tuple[str, set[str], str, float]:
    """(PASS|RED|TIMEOUT, the failing test lines, one line saying why, seconds) of one selector entry (`path` or `path Class`) run in `cwd`."""
    started, env = time.time(), dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    try:
        done = subprocess.run([sys.executable, "-B", *entry.split()], cwd=cwd, env=env, stdin=subprocess.DEVNULL, capture_output=True, text=True, errors="replace", timeout=SUITE_TIMEOUT_S)
    except (subprocess.TimeoutExpired, OSError) as exc:
        return ("TIMEOUT" if isinstance(exc, subprocess.TimeoutExpired) else "RED"), {type(exc).__name__}, type(exc).__name__, time.time() - started
    if done.returncode == 0:
        return "PASS", set(), "", time.time() - started
    lines = (done.stderr + "\n" + done.stdout).splitlines()
    failing = {l.strip() for l in lines if l.startswith(("FAIL: ", "ERROR: "))}
    if not failing:   # a crash or a suite that is not unittest: its last line is its identity
        failing = {next((l.strip() for l in reversed(lines) if l.strip()), f"exit {done.returncode}")}
    why = next((l for l in lines if l.startswith(("FAIL", "ERROR", "AssertionError"))), f"exit {done.returncode}")
    return "RED", failing, why, time.time() - started


def _red_at_base(base: str, reds: dict[str, set[str]]) -> dict[str, set[str]]:
    """The failing test lines of each of `reds` at `base`, in a throwaway shared clone. An empty set: the suite passes there, does not exist there, or could not be run there, so the push's red is its own."""
    found = {entry: set() for entry in reds}
    holder = Path(tempfile.mkdtemp(prefix="legend-landing-base-"))
    try:
        clone = holder / "base"
        ready = run("git", "clone", "-q", "--shared", "--no-checkout", str(ROOT), str(clone)).returncode == 0
        if not (ready and run("git", "-C", str(clone), "checkout", "-q", "--detach", base).returncode == 0):
            print(f"LANDING SUITES: no clone of {base[:12]} could be built; a red suite counts as this push's own", flush=True)
            return found
        for entry in reds:
            if not (clone / entry.split()[0]).is_file():
                continue
            word, failing, _, seconds = _run_suite(entry, clone)
            found[entry] = failing
            print(f"LANDING-SUITE AT-BASE {word} {entry} ({seconds:.0f}s) on {base[:12]}", flush=True)
        return found
    finally:
        shutil.rmtree(holder, ignore_errors=True)


def landing_selection(base: str) -> list[str] | None:
    """The suites the selector names for what `base..HEAD` changes, or None when no selection can be built (said here; it does not refuse)."""
    selector_path = ROOT / "framework" / "scripts" / "landing_suites.py"
    if not selector_path.is_file():
        selector_path = Path(__file__).resolve().parent / "landing_suites.py"
    wrote_bytecode, sys.dont_write_bytecode = sys.dont_write_bytecode, True      # importing the selector must not add a file to the tree the gate judges
    try:
        spec = importlib.util.spec_from_file_location("landing_suites_for_push", selector_path)
        selector = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(selector)
        return selector.select(selector.changes(ROOT, base), ROOT)
    except Exception as exc:   # a selection that cannot be built is said and does not refuse
        print(f"LANDING SUITES not run: {type(exc).__name__}: {str(exc)[:200]} (the push is not refused for this)", flush=True)
        return None
    finally:
        sys.dont_write_bytecode = wrote_bytecode


def landing_check(base: str, picked: list[str], where: Path) -> str:
    """Run `picked` in `where`. Returns '' when nothing this push turns red, else the refusal text."""
    reds: dict[str, set[str]] = {}
    for entry in picked:
        word, failing, why, seconds = _run_suite(entry, where)
        if word != "PASS":
            reds[entry] = failing
        print(f"LANDING-SUITE {word} {entry} ({seconds:.0f}s)" + (f": {why[:200]}" if why else ""), flush=True)
    new: dict[str, list[str]] = {}
    if reds:
        before = _red_at_base(base, reds)
        for entry, failing in reds.items():
            fresh = sorted(failing - before[entry])
            if fresh:
                new[entry] = fresh
            else:
                print(f"LANDING-SUITE PRE-EXISTING RED {entry}: the same failure is on {base[:12]}; not this push's, and main stays red until it is repaired: "
                      + "; ".join(sorted(failing)[:6])[:600], flush=True)
    print(f"LANDING SUITES: {len(picked)} run, {len(reds)} not passing, {len(new)} turned red by this push", flush=True)
    if not new:
        return ""
    shown = "\n".join(f"  {entry}\n" + "\n".join(f"    {line[:200]}" for line in lines[:6]) for entry, lines in new.items())
    return ("this push turns a suite red that passes (or does not fail this way) on the remote tip:\n" + shown +
            "\nFix: run the suite in your worktree (python3 -B <suite>), repair, commit, run safe_push again. "
            "If the red must be published, --no-landing-suites skips the suites and records that in the history. Nothing was gated or pushed.")


def checks(remote: str, base: str, sha: str, landing: bool, parallel: bool) -> str:
    """The landing suites, the view checks and the gate on commit `sha`: '' when all pass, else the first refusal in that order. With `parallel` they run at the same time, the suites in a
    throwaway clone, because the gate reads the worktree."""
    views_job = gate_job = None
    started, suites_s, clone_s = time.time(), 0.0, 0.0
    if parallel:
        short = wait_for_space()      # a waiter can sit in the queue for many minutes while other clones fill the disk
        if short:
            return short
        _STOPPING.clear()
        atexit.register(stop_background)
        views_job = Background(lambda: stale_derived_views(run_stoppable))
        gate_job = Background(lambda: run_stoppable(sys.executable, str(GATE)))

    if landing:
        picked = landing_selection(base)
        refusal, dirty = "", ""
        if picked is not None and parallel and picked:
            clone_from = time.time()
            with suite_clone(sha, remote) as (clone, why):
                clone_s = time.time() - clone_from
                if clone is None:
                    print(f"PARALLEL CHECKS: no suite clone ({why}); the suites run in the worktree after the gate and the view checks", flush=True)
                    views_job.get()
                    gate_job.get()
                suites_from = time.time()
                refusal = landing_check(base, picked, clone or ROOT)
                suites_s = time.time() - suites_from
                if clone is not None:
                    dirty = run("git", "-C", str(clone), "status", "--porcelain").stdout.strip()
        elif picked is not None:
            refusal = landing_check(base, picked, ROOT)
        if dirty or run("git", "status", "--porcelain").stdout.strip():
            return "a landing suite left the working tree unclean, so the gate would not be judging HEAD. Nothing was gated or pushed."
        if refusal:
            return refusal

    if not parallel:
        short = free_space_refusal()
        if short:
            return short

    stale = views_job.get() if views_job else stale_derived_views()
    if stale:
        return ("a committed derived view is behind its sources on the commit that would be gated, so CI would go red on it (2026-11-24: CI red from #2129). " + stale +
                "\nRegenerate on the merged tip, commit, and run safe_push again:\n  " + VIEW_FIX + "\nNothing was gated or pushed.")

    gate = gate_job.get() if gate_job else run(sys.executable, str(GATE))
    if parallel:
        print(f"LANDING CHECKS parallel: wall {time.time() - started:.0f}s (views {views_job.seconds:.0f}s, gate {gate_job.seconds:.0f}s, suites {suites_s:.0f}s, suite clone {clone_s:.0f}s)", flush=True)
    verdict = [l for l in gate.stdout.splitlines() if l.startswith("VERDICT")]
    print(verdict[0] if verdict else "(gate printed no VERDICT line)", flush=True)
    for line in gate.stderr.splitlines():      # how the side scans ran (serial, fallback) and why a gate failed closed reach the landing log
        if line.startswith(("GATE_SIDE_SCANS:", "GATE_ERROR:")):
            print(line, flush=True)
    if gate.returncode != 0:
        return (f"publication gate exit {gate.returncode} -- not PASS. Nothing was pushed.\n"
                + "\n".join(l for l in gate.stdout.splitlines() if "[BLOCK]" in l))
    return ""


def fail(msg: str) -> int:
    print(f"REFUSED: {msg}", file=sys.stderr)
    return 1


def main(argv: list[str]) -> int:
    if any(arg in ("-h", "--help") for arg in argv[1:]):
        print(__doc__)
        return 0
    args, expect, serialize, lock_timeout = list(argv[1:]), None, False, None
    if "--serialize" in args:
        serialize = True
        args.remove("--serialize")
    suites_asked, suites_declined = "--landing-suites" in args, "--no-landing-suites" in args
    for flag in ("--landing-suites", "--no-landing-suites"):
        while flag in args:
            args.remove(flag)
    if suites_asked and suites_declined:
        return fail("--landing-suites and --no-landing-suites together. Nothing was gated or pushed.")
    # 2026-11-25 (ADV after ADV-274: a red suite the selection had named was landed anyway): the default under --serialize, and a suite this push turns red refuses it.
    landing = suites_asked or (serialize and not suites_declined)
    skip_recorded = serialize and suites_declined
    serial_asked = "--serial-checks" in args
    while "--serial-checks" in args:
        args.remove("--serial-checks")
    copies_declined = "--no-copied-sentence-check" in args
    while "--no-copied-sentence-check" in args:
        args.remove("--no-copied-sentence-check")
    parallel = serialize and landing and not serial_asked      # without the lock, or with nothing to run beside them, the checks stay one after another
    asked, declined = "--regenerate-derived" in args, "--no-regenerate-derived" in args
    for flag in ("--regenerate-derived", "--no-regenerate-derived"):
        while flag in args:
            args.remove(flag)
    if asked and declined:
        return fail("--regenerate-derived and --no-regenerate-derived together. Nothing was gated or pushed.")
    # 2026-11-25 (ADV, CI #2353): the default under --serialize. Without it nothing on the landing path checked ranking.json, and a stale one was published.
    regenerate = asked or (serialize and not declined)
    for i, a in enumerate(args):
        if a == "--lock-timeout":
            if i + 1 >= len(args) or not args[i + 1].isdigit():
                return fail("--lock-timeout needs a number of seconds")
            lock_timeout = int(args[i + 1])
            del args[i:i + 2]
            break
    for i, a in enumerate(args):
        if a == "--expect-sha":
            if i + 1 >= len(args) or args[i + 1].startswith("-"):
                return fail("--expect-sha needs a revision")
            expect = args[i + 1]
            del args[i:i + 2]
            break
        if a.startswith("--expect-sha="):
            expect = a.split("=", 1)[1]
            del args[i]
            break
    if not 1 <= len(args) <= 2:
        return fail("usage: safe_push.py <remote> [<branch>] [--expect-sha <rev>] [--serialize [--lock-timeout <s>] [--no-regenerate-derived] [--no-landing-suites] [--serial-checks] [--no-copied-sentence-check]] [--landing-suites]")
    remote, branch = args[0], (args[1] if len(args) == 2 else "main")

    for bad in ("+", "--force", "-f", "--force-with-lease"):
        if bad in remote or bad in branch:
            return fail(f"force spelling {bad!r} in the refspec; this tool pushes fast-forward only")
    for name, value in (("remote", remote), ("branch", branch)):
        if value.startswith("-"):
            return fail(f"{name} {value!r} is option-shaped; usage: safe_push.py <remote> [<branch>]")

    short = free_space_refusal()
    if short and serialize:
        runs = live_heavy_runs()
        coming = sum(peak for _, _, peak in runs)
        if runs and not free_space_refusal(MIN_FREE_GB - coming):      # what they hold will come back: queue instead of refusing (step 17)
            print(f"free space is short while {_named(runs)} write(s): queueing, and the disk is checked again under the lock", flush=True)
            short = ""
    if short:
        return fail(short)

    dirty = run("git", "status", "--porcelain").stdout.strip()
    if dirty:
        return fail("working tree is not clean, so the gate would not be judging HEAD:\n" + dirty)

    before = run("git", "rev-parse", "HEAD").stdout.strip()
    if serialize and datetime.now(timezone.utc).strftime("%Y-%m-%d") <= NOTICE_UNTIL:
        print(NOTICE, flush=True)
    print(f"HEAD before gate: {before}")
    if expect is not None:
        want = run("git", "rev-parse", "--verify", "--quiet", f"{expect}^{{commit}}").stdout.strip()
        if not want:
            return fail(f"--expect-sha {expect!r} is not a commit of this repository. Nothing was gated or pushed.")
        if want != before:
            return fail(f"HEAD is {before} but the caller expected {want} (a failed merge or checkout before this call?). "
                        "Nothing was gated or pushed.")

    if asked and not serialize:
        return fail("--regenerate-derived needs --serialize: the derived surfaces are regenerated under the landing lock, on the tip being published. Nothing was gated or pushed.")

    lock_fh = None
    if serialize:
        common = run("git", "rev-parse", "--git-common-dir").stdout.strip()
        lock_path = (ROOT / common if not os.path.isabs(common) else Path(common)) / "legend_land.lock"
        lock_fh = open(lock_path, "a+")
        queue = Queue(lock_path.parent)
        queue.join()
        atexit.register(queue.leave)
        signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))
        waited, t0 = False, time.time()
        while True:
            pos, n = queue.position()
            if pos <= 1:      # head of the queue (or the queue file was lost: fall back to trying the lock)
                try:
                    fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except OSError:
                    pass
            if not waited:
                print(f"waiting for the landing lock {lock_path}: queue position {pos} of {n}" + (" (another publisher is gating)" if pos <= 1 else ""), flush=True)
                waited = True
            if lock_timeout is not None and time.time() - t0 > lock_timeout:
                return fail(f"the landing lock was not free within {lock_timeout}s. Nothing was gated or pushed.")
            time.sleep(2)
        print(f"landing lock acquired after {time.time() - t0:.0f}s", flush=True)
        held_from = time.time()
        atexit.register(lambda: print(f"landing lock held {time.time() - held_from:.0f}s", flush=True))
        short = wait_for_space()      # before the merge and the regeneration write anything (step 17)
        if short:
            return fail(short)
        current = run("git", "rev-parse", "HEAD").stdout.strip()
        if current != before:
            return fail(f"HEAD moved while waiting for the landing lock ({before} -> {current}). "
                        "Reconcile the intended commit in your own worktree. Nothing was gated or pushed.")
        if run("git", "status", "--porcelain").stdout.strip():
            return fail("working tree changed while waiting for the landing lock. Nothing was gated or pushed.")
        fetched = run("git", "fetch", remote, branch)
        if fetched.returncode != 0:
            return fail(f"git fetch {remote} {branch} failed under the landing lock: {fetched.stderr.strip()[:300]}. Nothing was gated or pushed.")
        tip = run("git", "rev-parse", "FETCH_HEAD").stdout.strip()
        if run("git", "merge-base", "--is-ancestor", tip, before).returncode != 0:
            merged = run("git", "merge", "--no-edit", "FETCH_HEAD")
            if merged.returncode != 0:
                conflicts = run("git", "diff", "--name-only", "--diff-filter=U").stdout.split()
                run("git", "merge", "--abort")
                now = run("git", "rev-parse", "HEAD").stdout.strip()
                left = run("git", "status", "--porcelain").stdout.strip()
                state = "tree and HEAD restored" if (now == before and not left) else f"WARNING: HEAD {now[:12]} / tree not restored: {left[:200]}"
                why = ("conflicting paths: " + ", ".join(conflicts)) if conflicts else (merged.stderr.strip()[:300] or merged.stdout.strip()[:300])
                return fail(f"the remote tip {tip[:12]} does not merge cleanly into HEAD {before[:12]} ({why}); {state}. Nothing was gated or pushed.")
            new_head = run("git", "rev-parse", "HEAD").stdout.strip()
            if run("git", "status", "--porcelain").stdout.strip():
                return fail(f"working tree is not clean after the merge of {tip[:12]}; nothing was gated or pushed.")
            print(f"MERGED {tip[:12]} into {before[:12]} -> {new_head[:12]} under the landing lock", flush=True)
            before = new_head
            if Path(__file__).read_bytes() != LOADED_SELF:
                return fail(f"the merge of {tip[:12]} changed safe_push.py itself, and this process still runs the sequence it loaded before the merge. "
                            f"Run the same command again with --expect-sha {new_head[:12]}. The merge commit stays; nothing was gated or pushed.")

    if regenerate:
        # 2026-11-19, third recurrence in a day: a receipts landing left coverage_report.md and reading_state.md behind the ledger and CI failed on the pushed SHA. The repair is a
        # step of the sequence, not a refusal: under the lock, on the merged tip, the existing freshness tool regenerates what is stale and commits exactly those files; the gate then
        # judges the commit that is pushed. Opt-in; nothing happens without the flag.
        if asked and not REGEN.is_file():
            return fail(f"--regenerate-derived: no freshness tool at {REGEN}. Nothing was gated or pushed.")
        regen_from = time.time()
        regen = run(sys.executable, str(REGEN), "--regenerate", "--repo", str(ROOT)) if REGEN.is_file() else subprocess.CompletedProcess([], 0, "no freshness tool in this repository\n", "")
        print("\n".join(l for l in regen.stdout.splitlines() if l.strip())[-400:], flush=True)
        print(f"derived-surface regeneration step {time.time() - regen_from:.0f}s", flush=True)
        if regen.returncode != 0:
            said = (regen.stderr or regen.stdout).strip()[-300:]
            if asked:
                return fail(f"--regenerate-derived: the freshness tool exited {regen.returncode}: {said}. Nothing was gated or pushed.")
            run("git", "restore", "--source=HEAD", "--staged", "--worktree", "--", ".")      # the tree was clean just before: tracked changes here are the failed regeneration's
            print(f"WARNING: derived surfaces NOT regenerated (the freshness tool exited {regen.returncode}): {said}\nThe push goes on; a stale surface turns CI red, so regenerate it by hand.", flush=True)
        if run("git", "status", "--porcelain").stdout.strip():
            return fail("--regenerate-derived left the working tree unclean. Nothing was gated or pushed.")
        regenerated = run("git", "rev-parse", "HEAD").stdout.strip()
        if regenerated != before:
            print(f"REGENERATED derived surfaces under the landing lock: {before[:12]} -> {regenerated[:12]}", flush=True)
            before = regenerated

    if skip_recorded:
        marked = run("git", "commit", "--allow-empty", "-m", "safe_push: landing suites skipped\n\n" + SKIP_TRAILER)
        if marked.returncode != 0:
            return fail(f"--no-landing-suites: the commit that records the skip failed: {marked.stderr.strip()[:300]}. Nothing was gated or pushed.")
        before = run("git", "rev-parse", "HEAD").stdout.strip()
        print(f"LANDING SUITES SKIPPED (--no-landing-suites): recorded in the empty commit {before[:12]} ({SKIP_TRAILER})", flush=True)

    if serialize and serial_asked:
        marked = run("git", "commit", "--allow-empty", "-m", "safe_push: checks run one after another\n\n" + SERIAL_TRAILER)
        if marked.returncode != 0:
            return fail(f"--serial-checks: the commit that records it failed: {marked.stderr.strip()[:300]}. Nothing was gated or pushed.")
        before = run("git", "rev-parse", "HEAD").stdout.strip()
        print(f"SERIAL CHECKS (--serial-checks): recorded in the empty commit {before[:12]} ({SERIAL_TRAILER})", flush=True)

    if serialize and copies_declined:
        marked = run("git", "commit", "--allow-empty", "-m", "safe_push: copied-sentence check skipped\n\n" + COPIES_TRAILER)
        if marked.returncode != 0:
            return fail(f"--no-copied-sentence-check: the commit that records it failed: {marked.stderr.strip()[:300]}. Nothing was gated or pushed.")
        before = run("git", "rev-parse", "HEAD").stdout.strip()
        print(f"COPIED-SENTENCE CHECK SKIPPED (--no-copied-sentence-check): recorded in the empty commit {before[:12]} ({COPIES_TRAILER})", flush=True)
    elif serialize:
        refusal = held_card_sentences(tip, before)
        if refusal:
            return fail(refusal)

    base = ""
    if landing:
        known = run("git", "rev-parse", "--verify", "--quiet", f"refs/remotes/{remote}/{branch}").stdout.strip()
        base = tip if serialize else known or f"{remote}/{branch}"
    try:
        refusal = checks(remote, base, before, landing, parallel)
    finally:
        stop_background()
    if refusal:
        return fail(refusal)

    after = run("git", "rev-parse", "HEAD").stdout.strip()
    if after != before:
        return fail(f"HEAD moved during the gate ({before} -> {after}); the gated commit is not "
                    "the commit that would be pushed")

    push = run("git", "push", remote, f"{before}:refs/heads/{branch}")
    sys.stderr.write(push.stderr)
    if push.returncode != 0:
        return fail(f"git push exited {push.returncode}")
    if "forced update" in push.stderr:
        return fail("the remote reports a FORCED update; this tool pushes fast-forward only")

    ls = run("git", "ls-remote", remote, f"refs/heads/{branch}").stdout.split()
    remote_sha = ls[0] if ls else ""
    if remote_sha != after:
        return fail(f"post-push verification failed: remote is {remote_sha or '(absent)'}, "
                    f"expected {after}")

    print(f"PUBLISHED  remote={remote}  branch={branch}  sha={after}  gate=PASS  verified=ls-remote")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
