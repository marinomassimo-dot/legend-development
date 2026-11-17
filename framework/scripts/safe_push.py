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

Usage: safe_push.py <remote> [<branch>] [--expect-sha <rev>] [--serialize [--lock-timeout <s>]]      (default branch: main)
"""
from __future__ import annotations
import atexit, fcntl, os, signal, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

# The root is overridable so the refusals can be exercised against a throwaway repo with a
# stub gate. A tool whose failure paths cannot be tested is the shape of the defect it exists
# to prevent.
ROOT = Path(os.environ.get("LEGEND_SAFE_PUSH_ROOT", Path(__file__).resolve().parents[2]))
GATE = Path(os.environ.get("LEGEND_SAFE_PUSH_GATE", ROOT / "scripts" / "public_release_gate.py"))


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
        return fail("usage: safe_push.py <remote> [<branch>] [--expect-sha <rev>] [--serialize [--lock-timeout <s>]]")
    remote, branch = args[0], (args[1] if len(args) == 2 else "main")

    for bad in ("+", "--force", "-f", "--force-with-lease"):
        if bad in remote or bad in branch:
            return fail(f"force spelling {bad!r} in the refspec; this tool pushes fast-forward only")
    for name, value in (("remote", remote), ("branch", branch)):
        if value.startswith("-"):
            return fail(f"{name} {value!r} is option-shaped; usage: safe_push.py <remote> [<branch>]")

    dirty = run("git", "status", "--porcelain").stdout.strip()
    if dirty:
        return fail("working tree is not clean, so the gate would not be judging HEAD:\n" + dirty)

    before = run("git", "rev-parse", "HEAD").stdout.strip()
    print(f"HEAD before gate: {before}")
    if expect is not None:
        want = run("git", "rev-parse", "--verify", "--quiet", f"{expect}^{{commit}}").stdout.strip()
        if not want:
            return fail(f"--expect-sha {expect!r} is not a commit of this repository. Nothing was gated or pushed.")
        if want != before:
            return fail(f"HEAD is {before} but the caller expected {want} (a failed merge or checkout before this call?). "
                        "Nothing was gated or pushed.")

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

    gate = run(sys.executable, str(GATE))
    verdict = [l for l in gate.stdout.splitlines() if l.startswith("VERDICT")]
    print(verdict[0] if verdict else "(gate printed no VERDICT line)")
    if gate.returncode != 0:
        return fail(f"publication gate exit {gate.returncode} -- not PASS. Nothing was pushed.\n"
                    + "\n".join(l for l in gate.stdout.splitlines() if "[BLOCK]" in l))

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
