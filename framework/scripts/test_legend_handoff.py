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


ADJ_REL = "framework/state/handoff_adjudication.jsonl"


def sha256_of(path):
    import hashlib
    h = hashlib.sha256()
    with open(str(path), "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def adjudicate(src, records):
    """Write the per-file adjudication the classifier consults."""
    p = src / ADJ_REL
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(json.dumps(r, sort_keys=True) for r in records) + "\n",
                 encoding="utf-8")
    return p


def preserve(home, worktree_basename, relpath, src_file):
    """Put a byte-identical copy in the durable payload, as `handoff` would carry it."""
    dest = home / ".legend" / "state" / "payload" / worktree_basename / relpath
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(str(src_file), str(dest))
    return dest


def declared_untracked(src, home, klass="RUNTIME_DURABLE", preserved=True,
                       body="an adjudicated artefact\n"):
    """An untracked file plus its adjudication. Returns (path, record)."""
    f = src / "adjudicated_artifact.md"
    f.write_text(body, encoding="utf-8")
    rec = {
        "worktree": Path(src).name, "path": "adjudicated_artifact.md",
        "owner": "fixture-actor", "class": klass, "sha256": sha256_of(f),
        "required_for_resume": True, "reason": "fixture record",
        "adjudicated_by": "test", "adjudicated_at": "2026-08-31T00:00:00Z",
    }
    if preserved:
        preserve(home, Path(src).name, "adjudicated_artifact.md", f)
    # the adjudication file is itself untracked state, so it must be tracked or the
    # classifier correctly reports the very file that resolves the others.
    adjudicate(src, [rec])
    g(src, "add", ADJ_REL)
    g(src, "-c", "user.email=fixture@example.invalid", "-c", "user.name=Fixture",
      "commit", "-q", "-m", "adjudication")
    # keep remote parity: this commit is fixture scaffolding, and letting it diverge
    # would make every test here fail for a reason none of them is about.
    g(src, "push", "-q", "development", "main")
    g(src, "fetch", "-q", "development")
    return f, rec


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
    # the durable payload: adjudicated untracked work whose ONLY copy may be here.
    # A handoff that carried the adjudication and dropped the bytes it points at would
    # pass every other row in this table.
    pay = home / ".legend" / "state" / "payload"
    st["durable_payload"] = ";".join(
        "%s=%s" % (p.relative_to(pay), sha256_of(p))
        for p in sorted(pay.rglob("*")) if p.is_file()
    ) if pay.is_dir() else "ABSENT"
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

    def test_adjudicated_untracked_state_resolves_the_gate(self):
        """A verified adjudication clears UNKNOWN — and the bytes actually travel."""
        f, _ = declared_untracked(self.src, self.home)
        rc, out = do_handoff(self.src, self.home, self.out)
        self.assertEqual(rc, 0, out)
        self.assertIn("HANDOFF_COMPLETE", out)
        m = json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))
        by_id = dict((s["id"], s) for s in m["classification"]["surfaces"])
        self.assertEqual(by_id["git.worktree.untracked.unclassified"]["count"], 0)
        self.assertEqual(by_id["git.worktree.untracked.adjudicated"]["count"], 1)
        self.assertEqual(by_id["git.worktree.untracked.adjudicated"]["class"], "RUNTIME_DURABLE")
        # positive control: the payload is in the handoff directory, not merely named
        carried = self.out / "runtime-artifacts" / "state" / "payload" / \
            Path(self.src).name / "adjudicated_artifact.md"
        self.assertTrue(carried.is_file(), "durable payload did not travel")
        self.assertEqual(sha256_of(carried), sha256_of(f))

    def test_negative_control_adjudication_drifted(self):
        """Editing a file AFTER adjudicating it returns it to UNKNOWN.

        Without this, a declaration written once would keep vouching for bytes that
        have since changed — which is how a stale record becomes a false green.
        """
        f, _ = declared_untracked(self.src, self.home)
        f.write_text("edited after the adjudication was written\n", encoding="utf-8")
        rc, out = do_handoff(self.src, self.home, self.base / "drifted")
        self.assertNotEqual(rc, 0, out)
        self.assertIn("HANDOFF_DENY", out)
        m = json.loads((self.base / "drifted" / "manifest.json").read_text(encoding="utf-8"))
        by_id = dict((s["id"], s) for s in m["classification"]["surfaces"])
        self.assertEqual(by_id["git.worktree.untracked.unclassified"]["count"], 1)
        self.assertIn("DRIFTED", by_id["git.worktree.untracked.unclassified"]["detail"])

    def test_negative_control_adjudication_without_preservation(self):
        """Declaring RUNTIME_DURABLE does not make anything durable."""
        declared_untracked(self.src, self.home, preserved=False)
        rc, out = do_handoff(self.src, self.home, self.base / "unpreserved")
        self.assertNotEqual(rc, 0, out)
        self.assertIn("HANDOFF_DENY", out)
        m = json.loads((self.base / "unpreserved" / "manifest.json").read_text(encoding="utf-8"))
        by_id = dict((s["id"], s) for s in m["classification"]["surfaces"])
        self.assertEqual(by_id["git.worktree.untracked.unclassified"]["count"], 1)
        self.assertIn("UNPRESERVED", by_id["git.worktree.untracked.unclassified"]["detail"])

    def test_negative_control_malformed_adjudication(self):
        """An unreadable record is not an absent one, and must not pass silently."""
        declared_untracked(self.src, self.home)
        p = self.src / ADJ_REL
        p.write_text(p.read_text(encoding="utf-8") + "{not json at all\n", encoding="utf-8")
        rc, out = do_handoff(self.src, self.home, self.base / "malformed")
        self.assertNotEqual(rc, 0, out)
        m = json.loads((self.base / "malformed" / "manifest.json").read_text(encoding="utf-8"))
        by_id = dict((s["id"], s) for s in m["classification"]["surfaces"])
        self.assertIn("git.worktree.untracked.adjudication_malformed", by_id)
        self.assertEqual(by_id["git.worktree.untracked.adjudication_malformed"]["class"], "UNKNOWN")

    def test_roundtrip_is_lossless(self):
        declared_untracked(self.src, self.home)
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

    def test_destination_with_fewer_roots_still_resumes(self):
        """A fresh clone reaches fewer root commits than the source, and that is normal.

        `bench-blind-participant` in the real repository was started empty, so the
        source has two root commits and a clone of the remote has one. Equality of the
        root SET refused the right repository, before the bundle that carries the
        missing root had been fetched.
        """
        env = dict(os.environ)
        env.update(GIT_ENV)
        # an orphan-rooted branch that no remote reaches: a second root commit
        g(self.src, "checkout", "-q", "--orphan", "orphan-rooted")
        g(self.src, "rm", "-q", "-rf", ".")
        (self.src / "orphan.md").write_text("its own root\n", encoding="utf-8")
        g(self.src, "add", "orphan.md")
        g(self.src, "-c", "user.email=fixture@example.invalid", "-c", "user.name=Fixture",
          "commit", "-q", "-m", "orphan root")
        g(self.src, "checkout", "-q", "-f", "main")

        _, roots = g(self.src, "rev-list", "--max-parents=0", "--all")
        self.assertEqual(len(roots.split()), 2, "positive control: the source needs 2 roots")

        rc, out = do_handoff(self.src, self.home, self.out)
        self.assertEqual(rc, 0, out)
        dest = fresh_destination(self.remote, self.base / "dest")
        _, droots = g(dest, "rev-list", "--max-parents=0", "--all")
        self.assertEqual(len(droots.split()), 1,
                         "positive control: the destination must have FEWER roots")
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest), check=False)
        self.assertNotIn("repo identity mismatch", out)
        self.assertEqual(rc, 0, out)

    def test_bundled_checked_out_branch_is_landed(self):
        """A bundled `refs/heads/main` must land even though main is checked out.

        `git fetch` refuses to write the checked-out branch and aborts the entire
        refspec, so one such ref left `refs restored: 0` — every other ref lost with it.
        A real source has main ahead of the remote, so main IS bundled; the fixture
        publishes main, so it never saw this.
        """
        # take main past the remote so it becomes an unpublished, therefore bundled, ref
        (self.src / "ahead.md").write_text("local main is ahead of the remote\n",
                                           encoding="utf-8")
        g(self.src, "add", "ahead.md")
        g(self.src, "-c", "user.email=fixture@example.invalid", "-c", "user.name=Fixture",
          "commit", "-q", "-m", "ahead of the remote")
        _, want = g(self.src, "rev-parse", "refs/heads/main")
        want = want.strip()

        rc, out = do_handoff(self.src, self.home, self.out)
        m = json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))
        bundled = [e["ref"] for e in m["artifact_references"]["bundle"]["refs"]]
        self.assertIn("refs/heads/main", bundled,
                      "positive control: main must be bundled for this test to mean anything")

        dest = fresh_destination(self.remote, self.base / "dest")
        _, cur = g(dest, "branch", "--show-current")
        self.assertEqual(cur.strip(), "main", "positive control: destination is on main")
        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest), check=False)
        self.assertNotIn("bundle fetch failed", out)
        _, got = g(dest, "rev-parse", "refs/heads/main")
        self.assertEqual(got.strip(), want, out)
        self.assertIn("refs restored: %d" % len(bundled), out)

    def test_negative_control_checked_out_branch_diverged(self):
        """Landing the checked-out branch must never discard destination work."""
        (self.src / "ahead.md").write_text("source side\n", encoding="utf-8")
        g(self.src, "add", "ahead.md")
        g(self.src, "-c", "user.email=fixture@example.invalid", "-c", "user.name=Fixture",
          "commit", "-q", "-m", "source ahead")
        # handoff itself reports DENY here because main is deliberately ahead of the
        # remote; the payload is still written, and the payload is what this tests.
        do_handoff(self.src, self.home, self.out)
        self.assertTrue((self.out / "manifest.json").is_file())

        dest = fresh_destination(self.remote, self.base / "dest")
        (dest / "dest_only.md").write_text("work that exists only here\n", encoding="utf-8")
        g(dest, "add", "dest_only.md")
        g(dest, "-c", "user.email=fixture@example.invalid", "-c", "user.name=Fixture",
          "commit", "-q", "-m", "destination-only commit")
        _, before = g(dest, "rev-parse", "HEAD")

        rc, out = tool("resume", "--bundle", str(self.out), "--into", str(dest), check=False)
        self.assertNotEqual(rc, 0, out)
        self.assertIn("Refusing to discard destination work", out)
        _, after = g(dest, "rev-parse", "HEAD")
        self.assertEqual(before, after, "destination HEAD was moved despite the refusal")

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
        g(other, "-c", "user.email=fixture@example.invalid", "-c", "user.name=Fixture",
          "commit", "-q", "-m", "unrelated")
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
        # Without this the durable_payload row compares ABSENT to ABSENT and prints
        # MATCH — a row that measures nothing while looking exactly like one that does.
        declared_untracked(src, home)
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


def reconstruct_real(root, payload, scratch, remote="development", branch="main"):
    """Reconstruct from a REAL handoff payload, into what a fresh clone actually gets.

    The fixture roundtrip proves the mechanism. It cannot prove that THIS machine's
    payload reconstructs, because the fixture builds every surface it then checks. So
    this builds the destination the way the destination really arrives — a repository
    holding only what `refs/remotes/<remote>/*` carries, which is exactly a fresh clone
    of the remote and nothing else — and resumes the real payload into it.

    It is a verification, not a test case: it needs a payload that already exists on
    disk, so it cannot run in the fixture suite.
    """
    root, payload, scratch = Path(root), Path(payload), Path(scratch)
    dest, dhome = scratch / "dest", scratch / "desthome"
    for d in (dest, dhome):
        shutil.rmtree(str(d), True)
    dest.mkdir(parents=True)
    dhome.mkdir(parents=True)
    env = dict(os.environ)
    env.update(GIT_ENV)

    run(["git", "init", "-q", "-b", branch, str(dest)], env=env)
    # exactly what the remote carries, under both the branch and the tracking name
    run(["git", "-C", str(dest), "fetch", "-q", str(root),
         "+refs/remotes/%s/*:refs/remotes/%s/*" % (remote, remote)], env=env)
    rc, tip = g(dest, "rev-parse", "refs/remotes/%s/%s" % (remote, branch), check=False)
    if rc != 0:
        print("RECONSTRUCT_FAIL: the source has no refs/remotes/%s/%s" % (remote, branch))
        return 2
    # `fetch` refuses to write the branch that is checked out, so land the tip with a
    # reset: same result, and it also populates the working tree the patches apply to.
    g(dest, "reset", "-q", "--hard", tip.strip())

    manifest = json.loads((payload / "manifest.json").read_text(encoding="utf-8"))
    print("=" * 78)
    print("CLEAN RECONSTRUCTION FROM THE REAL PAYLOAD")
    print("=" * 78)
    print("source root      %s" % root)
    print("payload          %s" % payload)
    print("destination      %s   (holds ONLY refs/remotes/%s/*)" % (dest, remote))
    print("destination tip  %s" % tip.strip())
    print("source HEAD      %s" % manifest.get("head"))
    print()

    rc, out = tool("resume", "--bundle", str(payload), "--into", str(dest),
                   "--home", str(dhome), check=False)
    print(out.rstrip())
    print()

    # Every promise in the manifest, checked against the destination. The denominator
    # is printed beside the failure count because they print identically at zero.
    rows = []
    for entry in manifest.get("artifact_references", {}).get("bundle", {}).get("refs", []):
        rcx, got = g(dest, "rev-parse", entry["ref"], check=False)
        rows.append(("ref " + entry["ref"],
                     entry["object"] == (got.strip() if rcx == 0 else "ABSENT")))
    for entry in manifest.get("artifact_references", {}).get("runtime_state", []):
        p = payload / entry["path"]
        rows.append(("runtime " + entry["path"],
                     p.is_file() and sha256_of(p) == entry["sha256"]))
    # the adjudicated files: present in the destination's payload, at the declared digest
    adj = root / ADJ_REL
    adj_rows = 0
    if adj.is_file():
        for line in adj.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            landed = dhome / ".legend" / "state" / "payload" / r["worktree"] / r["path"]
            rows.append(("adjudicated %s/%s" % (r["worktree"], r["path"]),
                         landed.is_file() and sha256_of(landed) == r["sha256"]))
            adj_rows += 1

    # Dirty patches: a real source has many worktrees, each at its own commit, and a
    # destination is ONE checkout. `resume` refuses to apply a patch at the wrong
    # commit — correctly — so "not applied here" is not "lost". What losslessness
    # requires is that each patch DOES apply at the commit it was taken at, and that
    # commit is one of the refs just restored. Check exactly that.
    patch_rows = 0
    for entry in manifest.get("artifact_references", {}).get("dirty_patches", []):
        p = payload / entry["patch"]
        head = entry.get("head")
        ok = p.is_file() and sha256_of(p) == entry["sha256"]
        if ok and head:
            wt = scratch / ("wt-" + entry["worktree_basename"])
            shutil.rmtree(str(wt), True)
            rcw, _ = g(dest, "worktree", "add", "-q", "--detach", str(wt), head, check=False)
            ok = rcw == 0
            if ok:
                rca, _ = g(wt, "apply", "--check", str(p), check=False)
                ok = rca == 0
        rows.append(("dirty %s applies at %s" % (entry["patch"], (head or "?")[:12]), ok))
        patch_rows += 1

    bad = [name for name, ok in rows if not ok]
    print("checks run: %d   (refs %d · runtime %d · adjudicated %d · dirty %d)   "
          "failures: %d"
          % (len(rows),
             len(manifest.get("artifact_references", {}).get("bundle", {}).get("refs", [])),
             len(manifest.get("artifact_references", {}).get("runtime_state", [])),
             adj_rows, patch_rows, len(bad)))
    for name in bad[:40]:
        print("  ! %s" % name)
    # `resume` returning non-zero solely because a patch belongs to a commit this
    # single checkout is not on is a correct refusal, not a loss — provided the patch
    # was proved to apply at its own commit just above.
    only_patch_placement = all(
        "belongs to" in m and "destination HEAD is" in m
        for m in [l.strip(" !") for l in out.splitlines() if l.strip().startswith("!")]
    ) and any(l.strip().startswith("!") for l in out.splitlines())
    ok = (rc == 0 or only_patch_placement) and not bad and len(rows) > 0
    print()
    print("REAL_MAC_RESUME_RECONSTRUCTION = %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: test_legend_handoff.py [unittest options]\n"
              "  --table: print the losslessness table\n"
              "  --reconstruct-real --root ROOT --payload DIR --scratch DIR\n"
              "                     [--remote development] [--branch main]\n"
              "With no mode selected, run the regression tests.")
    elif "--table" in sys.argv:
        print_table()
    elif "--reconstruct-real" in sys.argv:
        import argparse
        ap = argparse.ArgumentParser()
        ap.add_argument("--reconstruct-real", action="store_true")
        ap.add_argument("--root", required=True)
        ap.add_argument("--payload", required=True)
        ap.add_argument("--scratch", required=True)
        ap.add_argument("--remote", default="development")
        ap.add_argument("--branch", default="main")
        a = ap.parse_args()
        sys.exit(reconstruct_real(a.root, a.payload, a.scratch, a.remote, a.branch))
    else:
        unittest.main()
