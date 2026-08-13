#!/usr/bin/env python3
"""Regression suite for the LEGEND runtime kernel launcher.

Hermetic by construction: it builds a throwaway git repository and a stub `claude`
on PATH, so it exercises the launcher's own decisions rather than whatever CLI
happens to be installed. A suite that can only run on one qualified host is a suite
that stops running.

Covers the two amendments implemented in `KERNEL_SPEC.md` v1.1:

  MC-1  cell identity is declared, never derived
  MC-3  the lineage reservation precedes the act, and the refusal distinguishes a
        bare pending (safe to delete) from an annotated one (the only pointer to a
        session that may exist)

plus the properties they were built on top of: the runtime gate still fires before
every location and lineage check, and `check` diagnoses everything instead of dying
at the first refusal.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LAUNCHER = os.path.join(HERE, "legend_launch.sh")
STUB_VERSION = "9.9.9"

FAILURES = []


def check(label, condition, detail=""):
    if condition:
        print(f"  ok    {label}")
    else:
        print(f"  FAIL  {label}  {detail}")
        FAILURES.append(label)


class Bed:
    """A temporary world: a git worktree, a lineage base, and a stub `claude`."""

    def __init__(self, root):
        self.root = root
        self.repo = os.path.join(root, "repo")
        self.lineage = os.path.join(root, "lineage")
        self.bin = os.path.join(root, "bin")
        self.cell = "test-cell"
        self.cell_dir = os.path.join(self.lineage, self.cell)

        os.makedirs(self.repo)
        os.makedirs(self.cell_dir)
        os.makedirs(self.bin)

        # A stub CLI. `--version` prints a version we control; `agents --json`
        # returns an empty roster, which is the "nobody alive by that name" path.
        stub = os.path.join(self.bin, "claude")
        with open(stub, "w") as fh:
            fh.write(
                "#!/usr/bin/env bash\n"
                'if [ "$1" = "--version" ]; then echo "%s (stub)"; exit 0; fi\n'
                'if [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
                "echo 'stub refuses to launch anything' >&2; exit 97\n" % STUB_VERSION
            )
        os.chmod(stub, 0o755)

        env = dict(os.environ, PATH=self.bin + os.pathsep + os.environ["PATH"])
        for args in (
            ["git", "init", "-q", "-b", "testbranch"],
            ["git", "config", "user.email", "t@example.invalid"],
            ["git", "config", "user.name", "t"],
            ["git", "commit", "-q", "--allow-empty", "-m", "root"],
        ):
            subprocess.run(args, cwd=self.repo, check=True, env=env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def write_record(self, actor, record):
        with open(os.path.join(self.cell_dir, actor + ".json"), "w") as fh:
            json.dump(record, fh, indent=2, sort_keys=True)
            fh.write("\n")

    def write_raw(self, actor, text):
        with open(os.path.join(self.cell_dir, actor + ".json"), "w") as fh:
            fh.write(text)

    def run(self, mode, actor, worktree=None, branch="testbranch",
            cell="__default__", certified=STUB_VERSION):
        env = dict(os.environ)
        env["PATH"] = self.bin + os.pathsep + env["PATH"]
        env["LEGEND_LINEAGE_DIR"] = self.lineage
        env["LEGEND_TRANSPORT_SETTINGS"] = os.path.join(HERE, "transport.json")
        env["LEGEND_CERTIFIED_VERSION"] = certified
        env.pop("LEGEND_RUNTIME_INSTANCE", None)
        if cell == "__default__":
            env["LEGEND_RUNTIME_INSTANCE"] = self.cell
        elif cell is not None:
            env["LEGEND_RUNTIME_INSTANCE"] = cell
        proc = subprocess.run(
            [LAUNCHER, mode, actor, worktree or self.repo, branch],
            capture_output=True, text=True, env=env, cwd=self.root)
        return proc.returncode, proc.stdout, proc.stderr


PENDING_BARE = {
    "actor_id": "bare", "runtime_instance": "test-cell", "state": "PENDING_BIRTH",
    "worktree": "/x", "branch": "y", "reserved_at": "2026-08-13T00:00:00Z",
}
PENDING_ANNOTATED = dict(
    PENDING_BARE, actor_id="annotated",
    annotation={"reason": "session spawned; the roster did not resolve a unique sessionId",
                "spawn_evidence": "Started background session abc123",
                "annotated_at": "2026-08-13T00:00:01Z"})
ACTIVE = {
    "actor_id": "active", "runtime_instance": "test-cell", "state": "ACTIVE",
    "session_id": "1111-2222", "worktree": "/x", "branch": "y",
}
LEGACY = {  # written by the pre-amendment kernel: no `state`, but a session id
    "actor_id": "legacy", "runtime_instance": "test-cell",
    "session_id": "aaaa-bbbb", "worktree": "/x", "branch": "y",
}


def main():
    root = tempfile.mkdtemp(prefix="legend-launch-test-")
    try:
        bed = Bed(root)
        bed.write_record("bare", PENDING_BARE)
        bed.write_record("annotated", PENDING_ANNOTATED)
        bed.write_record("active", ACTIVE)
        bed.write_record("legacy", LEGACY)
        bed.write_raw("broken", "[not an object]\n")

        print("MC-1 — cell identity is declared, never derived")
        rc, _, err = bed.run("birth", "anyone", cell=None)
        check("undeclared identity refuses", rc == 1 and "RUNTIME_INSTANCE_UNDECLARED" in err, err)
        check("and says it must not be derived", "derived from the network" in err, err)

        rc, _, err = bed.run("birth", "anyone", cell="no-such-cell")
        check("unknown cell refuses", rc == 1 and "CELL_UNKNOWN" in err, err)
        check("and names the command that creates it", "mkdir -p" in err, err)

        # The identity checks precede the runtime gate on purpose: a wrong cell is
        # wrong on a qualified host too.
        rc, _, err = bed.run("birth", "anyone", cell=None, certified="not-this-version")
        check("identity is judged before the runtime gate",
              "RUNTIME_INSTANCE_UNDECLARED" in err, err)

        print("MC-2 — the runtime gate still fires before location and lineage")
        rc, _, err = bed.run("birth", "bare", worktree=os.path.join(root, "absent"),
                             certified="not-this-version")
        check("unqualified host refuses", rc == 1 and "HOST_RUNTIME_UNQUALIFIED" in err, err)
        check("and does so before the location check", "WORKTREE_ABSENT" not in err, err)

        print("MC-3 — the reservation precedes the act, and pendings differ")
        rc, _, bare_err = bed.run("birth", "bare")
        check("birth on a bare pending refuses", rc == 1 and "LINEAGE_RESERVED" in bare_err, bare_err)
        check("bare pending says deleting it is safe", "is safe" in bare_err, bare_err)

        rc, _, ann_err = bed.run("birth", "annotated")
        check("birth on an annotated pending refuses",
              rc == 1 and "LINEAGE_RESERVED" in ann_err, ann_err)
        check("annotated pending warns BEFORE removing", "BEFORE removing" in ann_err, ann_err)
        check("annotated pending carries the spawn evidence", "abc123" in ann_err, ann_err)
        # N1: same refusal name, opposite remedies. If these ever converge, the
        # distinction that keeps a live session's only pointer alive is lost.
        # Both directions are asserted, because each catches a different collapse —
        # and `bare_err != ann_err` would NOT: the two messages differ by the actor
        # name alone, so string inequality is satisfied by a launcher that gives
        # identical instructions. That assertion was written, survived the mutation
        # that broke the distinction, and was replaced by these two.
        check("only the bare one is called safe to delete", "is safe" not in ann_err, ann_err)
        check("only the annotated one warns against removing",
              "BEFORE removing" not in bare_err, bare_err)

        rc, _, err = bed.run("resume", "bare")
        check("resume on a pending refuses", rc == 1 and "LINEAGE_UNBOUND" in err, err)

        rc, _, err = bed.run("birth", "broken")
        check("an uninterpretable record refuses", rc == 1 and "LINEAGE_UNREADABLE" in err, err)
        check("and refuses rather than overwriting", "rather than overwriting" in err, err)

        rc, _, err = bed.run("birth", "active")
        check("birth on an ACTIVE lineage refuses", rc == 1 and "LINEAGE_EXISTS" in err, err)

        rc, _, err = bed.run("resume", "nobody")
        check("resume without a lineage refuses", rc == 1 and "LINEAGE_ABSENT" in err, err)

        rc, out, _ = bed.run("check", "legacy")
        check("a pre-amendment record still reads as ACTIVE",
              "LINEAGE" in out and "ACTIVE aaaa-bbbb" in out, out)

        print("OQ-3 — check diagnoses, actions stay fail-closed at the first refusal")
        rc, out, _ = bed.run("check", "bare", certified="not-this-version")
        check("check exits non-zero when a precondition failed", rc == 1, out)
        check("check reports the runtime failure", "HOST_RUNTIME_UNQUALIFIED" in out, out)
        check("check keeps going past it", "CHECK_PASS  BRANCH" in out, out)
        check("check reaches the lineage verdict", "LINEAGE_VERDICT" in out, out)
        check("the verdict names what each mode would do",
              "birth would refuse LINEAGE_RESERVED (bare)" in out
              and "resume would refuse LINEAGE_UNBOUND" in out, out)

        rc, out, _ = bed.run("check", "nobody")
        check("check passes when every precondition holds",
              rc == 0 and "PRECONDITIONS_PASS" in out, out)

        print("existing behaviour still enforced")
        rc, _, err = bed.run("birth", "nobody", branch="wrong-branch")
        check("a wrong branch refuses", rc == 1 and "BRANCH_MISMATCH" in err, err)
        check("no record was written for a refused birth",
              not os.path.exists(os.path.join(bed.cell_dir, "nobody.json")))
    finally:
        shutil.rmtree(root, ignore_errors=True)

    print()
    if FAILURES:
        print(f"VERDICT: FAIL — {len(FAILURES)} assertion(s): {', '.join(FAILURES)}")
        return 1
    print("VERDICT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
