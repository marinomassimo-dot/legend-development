#!/usr/bin/env python3
"""SOURCE -> HANDOFF -> CLEAN RECONSTRUCTION -> RESUME -> SAME REQUIRED STATE.

Losslessness is not declared from reading the code. This builds an isolated source
laboratory that carries every awkward surface the real repository actually has --

    a branch on no remote, refs/preserved/*, refs/pii-backup/*, refs/stash,
    a TREE-typed refs/codex/turn-diffs checkpoint, uncommitted tracked work,
    runtime lineage outside the repository, receipts and a pending queue

-- hands it off, reconstructs the destination from a FRESH CLONE OF THE REMOTE ONLY
(which is what a new machine actually gets), resumes, and compares field by field.

Run `--table` to print the comparison table with its own denominator. A row count is
printed beside the mismatch count on purpose: "0 mismatches" and "0 items compared"
print identically, and only one of them means anything.

The negative controls are the point of the file. A handoff test that only ever passes
has not been tested, so three resumes here MUST fail closed:

    tampered checkpoint  ·  deleted bundle ref  ·  wrong authority secret
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "legend_handoff.py"


def run(cmd, cwd=None, env=None, check=True):
    proc = subprocess.run(
        cmd, cwd=str(cwd) if cwd else None, env=env,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    if check and proc.returncode != 0:
        raise RuntimeError("cmd failed %s\n%s" % (" ".join(cmd), proc.stdout))
    return proc.returncode, proc.stdout


def g(repo, *args, **kw):
    return run(["git", "-C", str(repo)] + list(args), **kw)


def tool(*args, **kw):
    return run([sys.executable, str(TOOL)] + list(args), **kw)


GIT_ENV = {
    "GIT_AUTHOR_NAME": "Fixture",
    "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
    "GIT_COMMITTER_NAME": "Fixture",
    "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
}


def build_source(base):
    """An isolated laboratory carrying every surface the real repository has."""
    env = dict(os.environ)
    env.update(GIT_ENV)
    src = base / "source"
    remote = base / "devremote.git"
    home = base / "home"
    (home / ".legend" / "lineage" / "mac-fixture-001").mkdir(parents=True)

    run(["git", "init", "-q", "-b", "main", str(src)], env=env)
    g(src, "config", "user.email", "fixture@example.invalid")
    g(src, "config", "user.name", "Fixture")
    run(["git", "init", "-q", "--bare", str(remote)], env=env)

    # tracked canonical state, receipts, pending queue
    (src / "disease-models" / "wwox" / "registries").mkdir(parents=True)
    (src / "ledger" / "approvals").mkdir(parents=True)
    (src / "runtime").mkdir(parents=True)
    (src / "framework" / "state").mkdir(parents=True)
    (src / "disease-models" / "wwox" / "registries" / "fulltext_read_receipts.jsonl").write_text(
        '{"pmid":"1","digest":"aaa","chain":"c1"}\n{"pmid":"2","digest":"bbb","chain":"c2"}\n',
        encoding="utf-8",
    )
    (src / "ledger" / "approvals" / "HUMAN_APPROVAL_QUEUE.jsonl").write_text(
        '{"id":"A1","state":"PENDING"}\n{"id":"A2","state":"PENDING"}\n{"id":"A3","state":"PENDING"}\n',
        encoding="utf-8",
    )
    (src / "runtime" / "orchestrator_lease.md").write_text("# lease\nSTATUS: RELEASED\n", encoding="utf-8")
    (src / "README.md").write_text("legend fixture\n", encoding="utf-8")
    g(src, "add", "README.md", "disease-models", "ledger", "runtime")
    g(src, "commit", "-q", "-m", "canonical state")
    g(src, "remote", "add", "development", str(remote))
    g(src, "push", "-q", "development", "main")
    g(src, "fetch", "-q", "development")

    # a branch that exists on NO remote
    g(src, "checkout", "-q", "-b", "unpublished-work")
    (src / "work.md").write_text("work that never reached a remote\n", encoding="utf-8")
    g(src, "add", "work.md")
    g(src, "commit", "-q", "-m", "unpublished work")
    g(src, "checkout", "-q", "main")

    # refs/preserved/* and refs/pii-backup/*: commits no branch reaches
    for ns, name, body in (
        ("refs/preserved", "saved-evidence", "deliberately preserved\n"),
        ("refs/pii-backup", "pre-scrub", "pre-scrub backup\n"),
    ):
        g(src, "checkout", "-q", "-b", "tmp-" + name)
        (src / (name + ".md")).write_text(body, encoding="utf-8")
        g(src, "add", name + ".md")
        g(src, "commit", "-q", "-m", name)
        _, sha = g(src, "rev-parse", "HEAD")
        g(src, "update-ref", ns + "/" + name, sha.strip())
        g(src, "checkout", "-q", "main")
        g(src, "branch", "-q", "-D", "tmp-" + name)

    # a TREE-typed codex checkpoint that no branch reaches
    g(src, "checkout", "-q", "-b", "tmp-codex")
    (src / "codex-turn.md").write_text("a codex turn diff\n", encoding="utf-8")
    g(src, "add", "codex-turn.md")
    g(src, "commit", "-q", "-m", "codex turn")
    _, tree = g(src, "rev-parse", "HEAD^{tree}")
    g(src, "update-ref", "refs/codex/turn-diffs/checkpoints/aaa/bbb/1787/uuid-1", tree.strip())
    g(src, "checkout", "-q", "main")
    g(src, "branch", "-q", "-D", "tmp-codex")

    # a stash
    (src / "README.md").write_text("legend fixture -- stashed edit\n", encoding="utf-8")
    g(src, "stash", "push", "-q", "-m", "parked work")

    # uncommitted tracked work, live at handoff time
    (src / "README.md").write_text("legend fixture -- uncommitted edit\n", encoding="utf-8")

    # durable runtime lineage outside the repository
    (home / ".legend" / "lineage" / "mac-fixture-001" / "plan.json").write_text(
        json.dumps({"actor_id": "plan-handoff", "runtime_instance": "mac-fixture-001",
                    "session_id": "SESSION-FIXTURE-1", "branch": "main"}, indent=2),
        encoding="utf-8",
    )
    return src, remote, home


def do_handoff(src, home, out, extra=None):
    args = [
        "handoff", "--root", str(src), "--out", str(out), "--home", str(home),
        "--actor", "plan-handoff", "--task", "P0.6-P0.8", "--session", "SESSION-FIXTURE-1",
        "--runtime", "claude-code", "--runtime-version", "2.1.251",
        "--authority", "WRITE", "--authority-secret", "correct-horse",
        "--force",
    ]
    return tool(*(args + (extra or [])), check=False)


def fresh_destination(remote, dest):
    """What a new machine actually gets: a clone of the remote and nothing else."""
    env = dict(os.environ)
    env.update(GIT_ENV)
    run(["git", "clone", "-q", str(remote), str(dest)], env=env)
    g(dest, "remote", "rename", "origin", "development")
    g(dest, "fetch", "-q", "development")
    return dest


def collect_state(repo, home, manifest=None):
    """The required state, as fields, from whichever side is asked."""
    st = {}
    _, head = g(repo, "rev-parse", "HEAD")
    st["HEAD"] = head.strip()
    _, br = g(repo, "branch", "--show-current")
    st["branch"] = br.strip()
    for label, ref in (
        ("ref:unpublished-work", "refs/heads/unpublished-work"),
        ("ref:preserved", "refs/preserved/saved-evidence"),
        ("ref:pii-backup", "refs/pii-backup/pre-scrub"),
        ("ref:stash", "refs/stash"),
        ("ref:codex-tree", "refs/codex/turn-diffs/checkpoints/aaa/bbb/1787/uuid-1"),
    ):
        rc, out = g(repo, "rev-parse", ref, check=False)
        st[label] = out.strip() if rc == 0 else "ABSENT"
    rp = repo / "disease-models" / "wwox" / "registries" / "fulltext_read_receipts.jsonl"
    st["receipts"] = (
        subprocess.run(["shasum", "-a", "256", str(rp)], stdout=subprocess.PIPE, text=True)
        .stdout.split()[0] if rp.is_file() else "ABSENT"
    )
    ap = repo / "ledger" / "approvals" / "HUMAN_APPROVAL_QUEUE.jsonl"
    st["pending_queue"] = str(
        len([l for l in ap.read_text(encoding="utf-8").splitlines() if l.strip()])
    ) if ap.is_file() else "ABSENT"
    # the uncommitted tracked edit: the surface most at risk, and the one a captured-
    # but-never-applied patch would silently drop
    rm = repo / "README.md"
    st["worktree:README.md"] = rm.read_text(encoding="utf-8").strip() if rm.is_file() else "ABSENT"
    lin = home / ".legend" / "lineage" / "mac-fixture-001" / "plan.json"
    st["lineage"] = lin.read_text(encoding="utf-8").strip() if lin.is_file() else "ABSENT"
    if manifest:
        st["actor"] = manifest.get("actor_id")
        st["task"] = manifest.get("task_id")
        st["session"] = manifest.get("session_id")
        st["checkpoint"] = manifest.get("last_valid_checkpoint", {}).get("commit")
    return st


class HandoffRoundtrip(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix="legend-handoff-"))
        self.addCleanup(shutil.rmtree, str(self.base), True)
        self.src, self.remote, self.home = build_source(self.base)
        self.out = self.base / "handoff"

    def test_handoff_denies_unknown_required_state(self):
        """An unclassified untracked file is a hard DENY, not a warning."""
        (self.src / "mystery_artifact.md").write_text("nobody classified this\n", encoding="utf-8")
        rc, out = do_handoff(self.src, self.home, self.base / "denied")
        self.assertNotEqual(rc, 0, out)
        self.assertIn("HANDOFF_DENY", out)
        self.assertIn("UNKNOWN_REQUIRED_STATE", out)

    def test_roundtrip_is_lossless(self):
        rc, out = do_handoff(self.src, self.home, self.out)
        self.assertEqual(rc, 0, out)
        self.assertIn("HANDOFF_COMPLETE", out)

        manifest = json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))
        src_state = collect_state(self.src, self.home, manifest)

        # the destination is a FRESH CLONE OF THE REMOTE, and a fresh HOME
        dest = fresh_destination(self.remote, self.base / "dest")
        dhome = self.base / "desthome"
        dhome.mkdir()
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest),
                       "--home", str(dhome), check=False)
        self.assertEqual(rc, 0, out)
        self.assertIn("RESUME_OK", out)
        self.assertIn("AUTHORITY    OBSERVER", out)

        dst_state = collect_state(dest, dhome, manifest)
        # HEAD/branch are the destination's own checkout of main; compare the rest
        compared, mismatches = 0, []
        for key in sorted(src_state):
            if key in ("HEAD", "branch"):
                continue
            compared += 1
            if src_state[key] != dst_state.get(key):
                mismatches.append((key, src_state[key], dst_state.get(key)))
        self.assertGreater(compared, 0, "positive control: nothing was compared")
        self.assertFalse(mismatches, "mismatches: %s" % mismatches)

    def test_negative_control_tampered_checkpoint(self):
        rc, _ = do_handoff(self.src, self.home, self.out)
        self.assertEqual(rc, 0)
        m = json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))
        m["last_valid_checkpoint"]["commit"] = "0" * 40
        (self.out / "manifest.json").write_text(json.dumps(m, indent=2), encoding="utf-8")
        dest = fresh_destination(self.remote, self.base / "dest")
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest), check=False)
        self.assertNotEqual(rc, 0, out)
        self.assertIn("RESUME_FAIL", out)

    def test_negative_control_missing_bundle_ref(self):
        rc, _ = do_handoff(self.src, self.home, self.out)
        self.assertEqual(rc, 0)
        m = json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))
        m["artifact_references"]["bundle"]["refs"].append(
            {"ref": "refs/preserved/never-existed", "object": "1" * 40, "type": "commit"}
        )
        (self.out / "manifest.json").write_text(json.dumps(m, indent=2), encoding="utf-8")
        dest = fresh_destination(self.remote, self.base / "dest")
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest), check=False)
        self.assertNotEqual(rc, 0, out)
        self.assertIn("ref not restored", out)

    def test_negative_control_authority_never_silently_survives(self):
        """The invariant: same ACTOR_ID must not inherit writer authority."""
        rc, _ = do_handoff(self.src, self.home, self.out)
        self.assertEqual(rc, 0)
        dest = fresh_destination(self.remote, self.base / "dest")

        # no secret -> OBSERVER, silently and always
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest), check=False)
        self.assertEqual(rc, 0, out)
        self.assertIn("AUTHORITY    OBSERVER", out)

        # wrong secret -> REJECTED and still OBSERVER
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest),
                       "--claim-authority", "wrong-secret", check=False)
        self.assertNotEqual(rc, 0, out)
        self.assertIn("authority claim REJECTED", out)
        self.assertIn("AUTHORITY    OBSERVER", out)

        # correct out-of-band secret -> WRITE restored, explicitly
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest),
                       "--claim-authority", "correct-horse", check=False)
        self.assertEqual(rc, 0, out)
        self.assertIn("AUTHORITY    WRITE", out)

    def test_negative_control_wrong_repository(self):
        """Resuming into a different repository must fail closed."""
        rc, _ = do_handoff(self.src, self.home, self.out)
        self.assertEqual(rc, 0)
        other = self.base / "other"
        env = dict(os.environ)
        env.update(GIT_ENV)
        run(["git", "init", "-q", "-b", "main", str(other)], env=env)
        (other / "x.md").write_text("unrelated\n", encoding="utf-8")
        g(other, "add", "x.md")
        g(other, "-c", "user.email=f@x.invalid", "-c", "user.name=F", "commit", "-q", "-m", "unrelated")
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(other), check=False)
        self.assertNotEqual(rc, 0, out)
        self.assertIn("repo identity mismatch", out)

    def test_sync_reports_fail_on_divergence(self):
        rc, out = tool("sync", "--root", str(self.src), "--remote", "development", check=False)
        self.assertNotEqual(rc, 0, out)  # the fixture has dirty worktree state
        self.assertIn("SYNC FAIL", out)
        self.assertIn("checks run:", out)


def print_table():
    """The comparison table, printed with its own denominator."""
    base = Path(tempfile.mkdtemp(prefix="legend-handoff-demo-"))
    try:
        src, remote, home = build_source(base)
        out = base / "handoff"
        rc, ho = do_handoff(src, home, out)
        print("=" * 78)
        print("HANDOFF")
        print("=" * 78)
        print(ho.rstrip())
        manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
        src_state = collect_state(src, home, manifest)

        dest = fresh_destination(remote, base / "dest")
        dhome = base / "desthome"
        dhome.mkdir()
        print()
        print("=" * 78)
        print("CLEAN RECONSTRUCTION: fresh clone of the remote, fresh HOME")
        print("=" * 78)
        rc2, ro = tool("resume", "--bundle", str(out), "--into", str(dest), "--home", str(dhome), check=False)
        print(ro.rstrip())
        dst_state = collect_state(dest, dhome, manifest)

        print()
        print("=" * 78)
        print("COMPARISON: SOURCE vs RECONSTRUCTED DESTINATION")
        print("=" * 78)
        print("%-22s %-34s %-34s %s" % ("FIELD", "SOURCE", "DESTINATION", "VERDICT"))
        print("-" * 110)
        compared = 0
        mism = 0
        for key in sorted(src_state):
            s = str(src_state[key])
            d = str(dst_state.get(key))
            if key in ("HEAD", "branch"):
                verdict = "n/a (destination checks out its own main)"
            else:
                compared += 1
                if s == d:
                    verdict = "MATCH"
                else:
                    verdict = "*** MISMATCH ***"
                    mism += 1
            print("%-22s %-34s %-34s %s" % (key, s[:33], d[:33], verdict))
        print("-" * 110)
        print("fields compared: %d      mismatches: %d" % (compared, mism))
        print("(a row count beside the mismatch count on purpose: "
              "'0 mismatches' and '0 compared' print identically)")
        print()
        print("LOSSLESS_HANDOFF = %s" % ("PASS" if rc == 0 else "FAIL"))
        print("LOSSLESS_RESUME  = %s" % ("PASS" if (rc2 == 0 and mism == 0 and compared > 0) else "FAIL"))
    finally:
        shutil.rmtree(str(base), True)


if __name__ == "__main__":
    if "--table" in sys.argv:
        print_table()
    else:
        unittest.main()
