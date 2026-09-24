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

Usage: safe_push.py <remote> [<branch>]      (default branch: main)
"""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path

# The root is overridable so the refusals can be exercised against a throwaway repo with a
# stub gate. A tool whose failure paths cannot be tested is the shape of the defect it exists
# to prevent.
ROOT = Path(os.environ.get("LEGEND_SAFE_PUSH_ROOT", Path(__file__).resolve().parents[2]))
GATE = Path(os.environ.get("LEGEND_SAFE_PUSH_GATE", ROOT / "scripts" / "public_release_gate.py"))


def run(*cmd, **kw):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, **kw)


def fail(msg: str) -> int:
    print(f"REFUSED: {msg}", file=sys.stderr)
    return 1


def main(argv: list[str]) -> int:
    if any(arg in ("-h", "--help") for arg in argv[1:]):
        print(__doc__)
        return 0
    if not 2 <= len(argv) <= 3:
        return fail("usage: safe_push.py <remote> [<branch>]")
    remote, branch = argv[1], (argv[2] if len(argv) == 3 else "main")

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
