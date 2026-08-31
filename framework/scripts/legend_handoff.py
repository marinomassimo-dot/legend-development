#!/usr/bin/env python3
"""Cross-host handoff for a LEGEND laboratory: classify, handoff, resume, sync.

The problem this exists for is measured, not imagined. On 2026-08-31 this repository
held 35 refs that `git push development main` does not carry, and 16 of those are
reachable from no local branch at all — so pushing *every* branch still loses them.
Among them are refs an actor deliberately named `preserved/` and `pii-backup/`,
plus `refs/stash`. A fresh clone of the development remote receives none of it.

The transport is `git bundle`, and that choice is the design:

  * a bundle carries ARBITRARY refs — `refs/preserved/*`, `refs/pii-backup/*`,
    `refs/stash`, and the tree-typed `refs/codex/turn-diffs/**` checkpoints, none of
    which any branch reaches and none of which a push would move;
  * a bundle is a FILE. It is carried, not published. Privacy-sensitive objects reach
    the destination host without ever being pushed to a remote — which is the only
    honest way to move `refs/pii-backup/*` at all.

Four verbs:

    classify   name every state surface, one class each, and refuse UNKNOWN
    handoff    build a bundle the source machine could then power off behind
    resume     reconstruct on the destination, fail closed on any mismatch
    sync       verify repo/remote/branch/HEAD parity, PASS or FAIL

The invariant this file exists to keep mechanical:

    ACTOR_ID  !=  RUNTIME  !=  SESSION  !=  WORKTREE  !=  AUTHORITY

Same ACTOR_ID never implies inherited writer authority. `resume` ALWAYS lands as
OBSERVER. Write authority is restored only by presenting, out of band, a secret whose
digest was recorded at handoff time — the bundle alone can never restore it, because
everything in the bundle travelled with the bundle.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "legend.handoff.manifest/1"

# ---------------------------------------------------------------------------
# classification vocabulary
# ---------------------------------------------------------------------------

VERSIONED = "VERSIONED"
RUNTIME_DURABLE = "RUNTIME_DURABLE"
REBUILDABLE_CACHE = "REBUILDABLE_CACHE"
EPHEMERAL = "EPHEMERAL"
SECRET_MACHINE_LOCAL = "SECRET_MACHINE_LOCAL"
EXTERNAL_REFERENCE = "EXTERNAL_REFERENCE"
UNKNOWN = "UNKNOWN"

CLASSES = (
    VERSIONED,
    RUNTIME_DURABLE,
    REBUILDABLE_CACHE,
    EPHEMERAL,
    SECRET_MACHINE_LOCAL,
    EXTERNAL_REFERENCE,
    UNKNOWN,
)

# Ref namespaces that a push to the development remote provably does not carry.
# Measured, not assumed: `handoff` recomputes membership every run.
CARRIED_ONLY_BY_BUNDLE = ("refs/preserved/", "refs/pii-backup/", "refs/codex/")

# Untracked paths that are declared non-state. Anything untracked and NOT matching
# one of these is UNKNOWN, and UNKNOWN that is required for resume is a hard DENY.
EPHEMERAL_UNTRACKED = (
    ".DS_Store",
    ".playwright-mcp/",
    "__pycache__/",
    ".pytest_cache/",
    "node_modules/",
    ".venv/",
)


def _utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# git helpers
# ---------------------------------------------------------------------------


def git(root, *args, **kwargs):
    """Run a git command. Returns stdout stripped. Raises on failure unless check=False."""
    check = kwargs.pop("check", True)
    proc = subprocess.run(
        ["git", "-C", str(root)] + list(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(
            "git %s failed (%d): %s" % (" ".join(args), proc.returncode, proc.stderr.strip())
        )
    return proc.stdout.strip()


def git_ok(root, *args):
    proc = subprocess.run(
        ["git", "-C", str(root)] + list(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return proc.returncode == 0, proc.stdout.strip(), proc.stderr.strip()


def all_refs(root):
    """Every ref: list of (refname, objectname, objecttype)."""
    out = git(root, "for-each-ref", "--format=%(refname)%09%(objectname)%09%(objecttype)")
    refs = []
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) == 3:
            refs.append((parts[0], parts[1], parts[2]))
    return refs


def repo_identity(root):
    """Identity independent of remote URL: the sorted set of root commits.

    A remote URL is configuration and can be edited; a root commit cannot. Two
    checkouts of the same project agree here even if one has renamed its remotes.
    """
    ok, out, _ = git_ok(root, "rev-list", "--max-parents=0", "--all")
    roots = sorted(out.split()) if ok and out else []
    digest = hashlib.sha256("\n".join(roots).encode("utf-8")).hexdigest()
    remotes = {}
    ok, out, _ = git_ok(root, "remote")
    if ok:
        for name in out.split():
            _, url, _ = git_ok(root, "remote", "get-url", name)
            remotes[name] = url
    return {"root_commits": roots, "root_digest": digest, "remotes": remotes}


def reachable_objects(root, ref_prefix):
    """Set of object ids reachable from every ref under ref_prefix."""
    ok, tips, _ = git_ok(root, "for-each-ref", "--format=%(objectname)", ref_prefix)
    if not ok or not tips.strip():
        return set()
    proc = subprocess.run(
        ["git", "-C", str(root), "rev-list", "--objects", "--stdin"],
        input=tips,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        return set()
    return set(line.split()[0] for line in proc.stdout.splitlines() if line.strip())


def peel(root, refname, objectname):
    ok, out, _ = git_ok(root, "rev-parse", refname + "^{}")
    return out if ok and out else objectname


def worktrees(root):
    """List of worktree paths, main checkout first."""
    out = git(root, "worktree", "list", "--porcelain")
    paths = []
    for line in out.splitlines():
        if line.startswith("worktree "):
            paths.append(line[len("worktree ") :].strip())
    return paths


def worktree_state(path):
    """(branch_or_detached, head, modified_tracked, untracked_list)."""
    ok, branch, _ = git_ok(path, "branch", "--show-current")
    ok2, head, _ = git_ok(path, "rev-parse", "HEAD")
    ok3, status, _ = git_ok(path, "status", "--porcelain", "--untracked-files=all")
    modified, untracked = [], []
    if ok3:
        for line in status.splitlines():
            if not line.strip():
                continue
            if line.startswith("??"):
                untracked.append(line[3:])
            else:
                modified.append(line[3:])
    return (
        branch if (ok and branch) else "",
        head if ok2 else "",
        modified,
        untracked,
    )


def is_declared_ephemeral(relpath):
    for pat in EPHEMERAL_UNTRACKED:
        if pat.endswith("/"):
            if relpath.startswith(pat) or ("/" + pat) in relpath:
                return True
        elif relpath == pat or relpath.endswith("/" + pat):
            return True
    return False


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# P0.6 — classification
# ---------------------------------------------------------------------------


class Surface(object):
    __slots__ = ("sid", "klass", "count", "required", "detail", "transport")

    def __init__(self, sid, klass, count, required, detail, transport):
        self.sid = sid
        self.klass = klass
        self.count = count
        self.required = required
        self.detail = detail
        self.transport = transport

    def as_dict(self):
        return {
            "id": self.sid,
            "class": self.klass,
            "count": self.count,
            "required_for_resume": self.required,
            "detail": self.detail,
            "transport": self.transport,
        }


def classify(root, home=None):
    """Classify every state surface. Returns (surfaces, unknown_required_count)."""
    home = Path(home) if home else Path(os.path.expanduser("~"))
    root = Path(root)
    surfaces = []

    refs = all_refs(root)
    dev_objects = reachable_objects(root, "refs/remotes/development/")
    head_objects = reachable_objects(root, "refs/heads/")

    heads = [r for r in refs if r[0].startswith("refs/heads/")]
    tags = [r for r in refs if r[0].startswith("refs/tags/")]
    preserved = [r for r in refs if r[0].startswith("refs/preserved/")]
    piibackup = [r for r in refs if r[0].startswith("refs/pii-backup/")]
    codex = [r for r in refs if r[0].startswith("refs/codex/")]
    stash = [r for r in refs if r[0] == "refs/stash"]
    remotes = [r for r in refs if r[0].startswith("refs/remotes/")]

    def not_on_dev(group):
        out = []
        for name, obj, typ in group:
            if peel(root, name, obj) not in dev_objects:
                out.append(name)
        return out

    def not_on_branch(group):
        out = []
        for name, obj, typ in group:
            if peel(root, name, obj) not in head_objects:
                out.append(name)
        return out

    published_heads = [h for h in heads if h[0] not in set(not_on_dev(heads))]
    unpublished_heads = not_on_dev(heads)

    surfaces.append(
        Surface(
            "git.refs.heads.published",
            VERSIONED,
            len(published_heads),
            True,
            "branches whose tip is reachable from the development remote",
            "git push / git clone",
        )
    )
    surfaces.append(
        Surface(
            "git.refs.heads.unpublished",
            RUNTIME_DURABLE,
            len(unpublished_heads),
            True,
            "branches on NO development remote; a fresh clone never receives them",
            "bundle",
        )
    )
    surfaces.append(
        Surface(
            "git.refs.preserved",
            RUNTIME_DURABLE,
            len(preserved),
            True,
            "deliberately preserved work; branch-unreachable, push does not carry it",
            "bundle",
        )
    )
    surfaces.append(
        Surface(
            "git.refs.pii_backup",
            SECRET_MACHINE_LOCAL,
            len(piibackup),
            True,
            "pre-scrub backups. MUST NOT be pushed to any remote. Bundle-only, and the "
            "bundle is carried over a private channel",
            "bundle (never push)",
        )
    )
    surfaces.append(
        Surface(
            "git.refs.stash",
            RUNTIME_DURABLE,
            len(stash),
            True,
            "uncommitted work parked in refs/stash; branch-unreachable",
            "bundle",
        )
    )
    surfaces.append(
        Surface(
            "git.refs.codex_checkpoints",
            RUNTIME_DURABLE,
            len(codex),
            True,
            "tree-typed turn-diff checkpoints; no branch reaches them and push cannot "
            "move a tree-typed ref",
            "bundle",
        )
    )
    surfaces.append(
        Surface(
            "git.refs.tags",
            VERSIONED,
            len(tags),
            True,
            "tags are NOT carried by `git push <remote> main`; push --tags or bundle",
            "bundle",
        )
    )
    stale_remotes = [
        r[0]
        for r in remotes
        if r[0].split("/")[2] not in set(git(root, "remote").split())
    ]
    surfaces.append(
        Surface(
            "git.refs.remotes.stale",
            EPHEMERAL,
            len(stale_remotes),
            False,
            "remote-tracking refs for remotes absent from git config; rebuilt by fetch",
            "not transferred",
        )
    )

    # working trees
    wts = worktrees(root)
    dirty_total, untracked_unknown, untracked_ephemeral = 0, [], 0
    dirty_detail = []
    for wt in wts:
        branch, head, modified, untracked = worktree_state(wt)
        if modified:
            dirty_total += len(modified)
            dirty_detail.append({"worktree": wt, "branch": branch, "modified": len(modified)})
        for rel in untracked:
            if is_declared_ephemeral(rel):
                untracked_ephemeral += 1
            else:
                untracked_unknown.append({"worktree": wt, "path": rel})

    surfaces.append(
        Surface(
            "git.worktree.dirty",
            RUNTIME_DURABLE,
            dirty_total,
            True,
            "uncommitted modifications to tracked files; captured as patches. detail=%s"
            % json.dumps(dirty_detail),
            "patch in bundle",
        )
    )
    surfaces.append(
        Surface(
            "git.worktree.untracked.ephemeral",
            EPHEMERAL,
            untracked_ephemeral,
            False,
            "untracked files matching the declared-ephemeral list",
            "not transferred",
        )
    )
    surfaces.append(
        Surface(
            "git.worktree.untracked.unclassified",
            UNKNOWN,
            len(untracked_unknown),
            True,
            "untracked files nobody has classified. Each is either in-progress work or "
            "junk, and the tool cannot tell which. detail=%s"
            % json.dumps(untracked_unknown[:40]),
            "DENY until committed or declared",
        )
    )

    # non-git durable runtime state
    lineage = home / ".legend" / "lineage"
    lineage_files = sorted(str(p.relative_to(lineage)) for p in lineage.rglob("*") if p.is_file()) if lineage.is_dir() else []
    surfaces.append(
        Surface(
            "fs.legend.lineage",
            RUNTIME_DURABLE,
            len(lineage_files),
            True,
            "~/.legend/lineage — actor lineage, session ids, cell migrations. Outside the "
            "repository, so no clone and no push moves it. files=%s" % json.dumps(lineage_files),
            "copied into bundle",
        )
    )

    local_instance = root / "deployment" / "local_instance.md"
    surfaces.append(
        Surface(
            "fs.deployment.local_instance",
            SECRET_MACHINE_LOCAL,
            1 if local_instance.is_file() else 0,
            False,
            "gitignored by design: absolute paths carrying a username, a runtime instance "
            "id, and live session refs. It is machine-local BY DEFINITION — the destination "
            "host must author its own, not receive this one",
            "NOT transferred (re-authored on destination)",
        )
    )

    receipts = root / "disease-models" / "wwox" / "registries" / "fulltext_read_receipts.jsonl"
    surfaces.append(
        Surface(
            "fs.receipts.fulltext",
            VERSIONED,
            1 if receipts.is_file() else 0,
            True,
            "hash-chained read receipts, tracked in git; travels with the commit",
            "git",
        )
    )

    approvals = root / "ledger" / "approvals" / "HUMAN_APPROVAL_QUEUE.jsonl"
    pending = 0
    if approvals.is_file():
        pending = sum(1 for line in approvals.read_text(encoding="utf-8").splitlines() if line.strip())
    surfaces.append(
        Surface(
            "fs.pending_queue.approvals",
            VERSIONED,
            pending,
            True,
            "human approval queue, tracked; the pending queue is derivable from the commit",
            "git",
        )
    )

    lease = root / "runtime" / "orchestrator_lease.md"
    surfaces.append(
        Surface(
            "fs.runtime.lease",
            VERSIONED,
            1 if lease.is_file() else 0,
            True,
            "tracked lease record; authority is DERIVED from it by lease_state.py and is "
            "never inherited by a resume",
            "git",
        )
    )

    # caches and ephemera
    pycache = sum(1 for p in root.rglob("__pycache__") if p.is_dir())
    surfaces.append(
        Surface(
            "fs.cache.pycache",
            REBUILDABLE_CACHE,
            pycache,
            False,
            "python bytecode; rebuilt on import. Stale bytecode has caused a false "
            "measurement in this repository, so it is deliberately NOT transferred",
            "not transferred",
        )
    )
    venvs = home / ".legend-venvs"
    surfaces.append(
        Surface(
            "fs.cache.venvs",
            REBUILDABLE_CACHE,
            len(list(venvs.iterdir())) if venvs.is_dir() else 0,
            False,
            "~/.legend-venvs — reinstallable from requirements on the destination",
            "rebuilt, not transferred",
        )
    )
    corpus = root / "files"
    surfaces.append(
        Surface(
            "fs.external.fulltext_corpus",
            EXTERNAL_REFERENCE,
            sum(1 for _ in corpus.rglob("*")) if corpus.is_dir() else 0,
            False,
            "files/ — third-party full texts, gitignored for copyright. Re-fetched on the "
            "destination from the tracked retrieval manifest; receipts prove identity",
            "re-fetched by reference",
        )
    )
    surfaces.append(
        Surface(
            "proc.running",
            EPHEMERAL,
            0,
            False,
            "agent processes do not migrate. The checkpoint plus the deterministic restart "
            "contract in the manifest replaces migration, by declaration",
            "checkpoint + restart contract",
        )
    )
    settings_local = root / ".claude" / "settings.local.json"
    surfaces.append(
        Surface(
            "cred.claude_settings_local",
            SECRET_MACHINE_LOCAL,
            1 if settings_local.is_file() else 0,
            False,
            "per-machine harness permissions; re-granted on the destination, never copied",
            "NOT transferred",
        )
    )
    surfaces.append(
        Surface(
            "ext.git_remotes",
            EXTERNAL_REFERENCE,
            len(repo_identity(root)["remotes"]),
            True,
            "GitHub remotes; reachable from any host with credentials",
            "by URL",
        )
    )

    unknown_required = sum(
        1 for s in surfaces if s.klass == UNKNOWN and s.required and s.count > 0
    )
    return surfaces, unknown_required


# ---------------------------------------------------------------------------
# P0.7 — handoff
# ---------------------------------------------------------------------------


def refs_needing_bundle(root):
    """Refs a push to development would not carry. Recomputed every run."""
    dev_objects = reachable_objects(root, "refs/remotes/development/")
    out = []
    for name, obj, typ in all_refs(root):
        if name.startswith("refs/remotes/"):
            continue
        if peel(root, name, obj) not in dev_objects:
            out.append((name, obj, typ))
    return out


def cmd_handoff(args):
    root = Path(args.root).resolve()
    out = Path(args.out).resolve()
    home = Path(args.home).expanduser() if args.home else Path(os.path.expanduser("~"))

    if out.exists():
        if not args.force:
            print("HANDOFF_DENY: output directory exists: %s (use --force)" % out)
            return 2
        shutil.rmtree(str(out))
    out.mkdir(parents=True)

    problems = []

    # 1 — repo identity
    identity = repo_identity(root)
    if not identity["root_commits"]:
        problems.append("repo identity: no root commit found; is %s a git repo?" % root)

    # 2 — classification, and the hard gate
    surfaces, unknown_required = classify(root, home=home)
    if unknown_required and not args.accept_unknown:
        problems.append(
            "UNKNOWN_REQUIRED_STATE=%d — surfaces required for resume that are "
            "unclassified. This is a hard gate." % unknown_required
        )

    # 3 — important versionable work committed?
    dirty = []
    for wt in worktrees(root):
        branch, head, modified, untracked = worktree_state(wt)
        if modified:
            dirty.append((wt, branch, head, modified))

    # 4 — bundle every ref a push would not carry
    bundle_path = out / "refs.bundle"
    bundled = refs_needing_bundle(root)
    bundle_info = {"file": "refs.bundle", "refs": [], "sha256": None}
    if bundled:
        cmd = ["git", "-C", str(root), "bundle", "create", str(bundle_path)]
        cmd += [name for name, _, _ in bundled]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode != 0:
            problems.append("bundle creation failed: %s" % proc.stderr.strip()[:400])
        else:
            bundle_info["refs"] = [
                {"ref": n, "object": o, "type": t} for n, o, t in bundled
            ]
            bundle_info["sha256"] = sha256_file(bundle_path)
            ok, _, err = git_ok(root, "bundle", "verify", str(bundle_path))
            if not ok:
                problems.append("bundle failed self-verification: %s" % err[:300])
    else:
        problems.append("no refs required bundling — nothing to hand off?")

    # 5 — uncommitted tracked work, captured as patches
    patches = []
    pdir = out / "dirty"
    if dirty:
        pdir.mkdir(exist_ok=True)
    for wt, branch, head, modified in dirty:
        name = Path(wt).name or "root"
        target = pdir / (name + ".patch")
        ok, diff, err = git_ok(wt, "diff", "HEAD")
        if not ok:
            problems.append("could not capture dirty diff for %s: %s" % (wt, err[:200]))
            continue
        target.write_text(diff, encoding="utf-8")
        patches.append(
            {
                "worktree_basename": name,
                "branch": branch,
                "head": head,
                "modified_files": len(modified),
                "patch": "dirty/" + name + ".patch",
                "sha256": sha256_file(target),
            }
        )

    # 6 — durable runtime state outside the repository
    runtime_state = []
    lineage = home / ".legend" / "lineage"
    if lineage.is_dir():
        dest = out / "runtime-artifacts" / "lineage"
        shutil.copytree(str(lineage), str(dest))
        for p in sorted(dest.rglob("*")):
            if p.is_file():
                runtime_state.append(
                    {
                        "path": str(p.relative_to(out)),
                        "origin": str(p).replace(str(dest), str(lineage)),
                        "sha256": sha256_file(p),
                    }
                )

    # 7 — remote parity, verified not performed
    ok_local, local_main, _ = git_ok(root, "rev-parse", "refs/heads/" + args.branch)
    ok_rem, remote_main, _ = git_ok(
        root, "rev-parse", "refs/remotes/%s/%s" % (args.remote, args.branch)
    )
    remote_check = {
        "remote": args.remote,
        "branch": args.branch,
        "local": local_main if ok_local else None,
        "remote_tracking": remote_main if ok_rem else None,
        "in_sync": bool(ok_local and ok_rem and local_main == remote_main),
        "network_consulted": False,
        "note": "compared against the remote-tracking ref as of the last fetch. handoff "
        "NEVER pushes and by default never touches the network.",
    }
    if args.check_remote:
        ok, lsr, err = git_ok(root, "ls-remote", args.remote, "refs/heads/" + args.branch)
        if ok and lsr.strip():
            remote_check["live_remote"] = lsr.split()[0]
            remote_check["network_consulted"] = True
            remote_check["in_sync"] = remote_check["live_remote"] == local_main
        else:
            problems.append("--check-remote could not reach %s: %s" % (args.remote, err[:200]))
    if not remote_check["in_sync"]:
        problems.append(
            "%s/%s is not at the local tip — push is authorized elsewhere, but the "
            "divergence must be declared before the source host disappears"
            % (args.remote, args.branch)
        )

    # 8 — the session manifest
    wt_root = Path(args.worktree).resolve() if args.worktree else root
    branch_now, head_now, _, _ = worktree_state(wt_root)
    grant_fp = sha256_text(args.authority_secret) if args.authority_secret else None

    manifest = {
        "schema": SCHEMA,
        "generated_at": _utcnow(),
        "session_id": args.session,
        "actor_id": args.actor,
        "task_id": args.task,
        "runtime": args.runtime,
        "runtime_version": args.runtime_version,
        "worktree": str(wt_root),
        "branch": branch_now,
        "head": head_now,
        "authority": {
            "at_handoff": args.authority,
            "after_resume": "OBSERVER",
            "regrant_required": True,
            "grant_fingerprint": grant_fp,
            "rule": "resume ALWAYS lands as OBSERVER. Write authority is restored only by "
            "presenting --claim-authority with the secret whose sha256 is recorded here. "
            "That secret does not travel in the bundle, so the bundle alone can never "
            "restore write authority.",
        },
        "last_valid_checkpoint": {
            "commit": head_now,
            "branch": branch_now,
            "bundle_sha256": bundle_info["sha256"],
        },
        "pending_queue": [
            s.as_dict() for s in surfaces if s.sid == "fs.pending_queue.approvals"
        ],
        "artifact_references": {
            "bundle": bundle_info,
            "dirty_patches": patches,
            "runtime_state": runtime_state,
        },
        "last_heartbeat": _utcnow(),
        "repo_identity": identity,
        "remote_check": remote_check,
        "classification": {
            "surfaces": [s.as_dict() for s in surfaces],
            "counts": _class_counts(surfaces),
            "unknown_required_state": unknown_required,
        },
        "restart_contract": {
            "processes_migrate": False,
            "procedure": [
                "clone or fetch the development remote",
                "git fetch <bundle> '+refs/*:refs/*' to restore branch-unreachable refs",
                "re-apply dirty/*.patch onto the recorded head",
                "copy runtime-artifacts/lineage to ~/.legend/lineage",
                "author a NEW deployment/local_instance.md on the destination",
                "re-acquire authority explicitly; never inherit it",
            ],
        },
        "declared_limitations": DECLARED_LIMITATIONS,
        "problems": problems,
        "resume_status": "READY" if not problems else "DENY",
    }

    (out / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    # 9 — integrity over every file in the bundle directory
    sums = []
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name != "SHA256SUMS":
            sums.append("%s  %s" % (sha256_file(p), p.relative_to(out)))
    (out / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")

    verdict = "HANDOFF_COMPLETE" if not problems else "HANDOFF_DENY"
    print("%s  out=%s" % (verdict, out))
    print("  refs bundled:           %d" % len(bundle_info["refs"]))
    print("  dirty patches:          %d" % len(patches))
    print("  runtime state files:    %d" % len(runtime_state))
    print("  UNKNOWN_REQUIRED_STATE: %d" % unknown_required)
    for p in problems:
        print("  ! %s" % p)
    return 0 if not problems else 1


def _class_counts(surfaces):
    counts = dict((c, 0) for c in CLASSES)
    for s in surfaces:
        counts[s.klass] = counts.get(s.klass, 0) + 1
    return counts


DECLARED_LIMITATIONS = [
    "Agent processes do not migrate. A checkpoint plus the restart contract replaces "
    "migration; an in-flight turn is lost by design.",
    "deployment/local_instance.md is NOT transferred. It is machine-local by definition "
    "(absolute paths, username, live session refs) and must be re-authored on the "
    "destination host.",
    "files/ (third-party full texts) is not transferred: copyright. It is re-fetched from "
    "the tracked retrieval manifest, and the hash-chained receipts prove identity.",
    "refs/pii-backup/* is carried in the bundle and MUST NOT be pushed to any remote. The "
    "bundle is a file on a private channel, never a publication.",
    "handoff never pushes and, without --check-remote, never touches the network: remote "
    "parity is asserted against the remote-tracking ref as of the last fetch.",
    "The chat transcript store (~/.claude/projects/**) is EXTERNAL_REFERENCE and is not "
    "transferred; only what was committed or bundled survives.",
]


# ---------------------------------------------------------------------------
# P0.7 — resume
# ---------------------------------------------------------------------------


def cmd_resume(args):
    bundle_dir = Path(args.bundle).resolve()
    into = Path(args.into).resolve()
    mismatches = []

    mpath = bundle_dir / "manifest.json"
    if not mpath.is_file():
        print("RESUME_FAIL: no manifest.json in %s" % bundle_dir)
        return 2
    manifest = json.loads(mpath.read_text(encoding="utf-8"))

    if manifest.get("schema") != SCHEMA:
        mismatches.append("schema: expected %s, got %s" % (SCHEMA, manifest.get("schema")))

    # integrity of the transported bundle itself
    sums = bundle_dir / "SHA256SUMS"
    if sums.is_file():
        for line in sums.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            digest, rel = line.split("  ", 1)
            target = bundle_dir / rel
            if not target.is_file():
                mismatches.append("missing transported file: %s" % rel)
            elif sha256_file(target) != digest:
                mismatches.append("digest mismatch on transported file: %s" % rel)
    else:
        mismatches.append("no SHA256SUMS: transported completeness cannot be verified")

    if not into.is_dir():
        mismatches.append("destination is not a directory: %s" % into)
        return _resume_verdict(manifest, mismatches, "OBSERVER")

    # repo identity must match — refuse to resume into the wrong repository
    dest_identity = repo_identity(into)
    src_identity = manifest.get("repo_identity", {})
    if dest_identity["root_digest"] != src_identity.get("root_digest"):
        mismatches.append(
            "repo identity mismatch: destination root_digest %s != manifest %s"
            % (dest_identity["root_digest"][:12], str(src_identity.get("root_digest"))[:12])
        )

    # restore the bundled refs
    restored = []
    bpath = bundle_dir / "refs.bundle"
    if bpath.is_file():
        expect = manifest.get("artifact_references", {}).get("bundle", {})
        if expect.get("sha256") and sha256_file(bpath) != expect["sha256"]:
            mismatches.append("refs.bundle sha256 does not match the manifest")
        ok, _, err = git_ok(into, "bundle", "verify", str(bpath))
        if not ok:
            mismatches.append("refs.bundle failed verification at destination: %s" % err[:200])
        elif not args.dry_run:
            ok2, _, err2 = git_ok(into, "fetch", str(bpath), "+refs/*:refs/*")
            if not ok2:
                mismatches.append("bundle fetch failed: %s" % err2[:300])
        # every ref the manifest promised must now exist at the promised object
        for entry in expect.get("refs", []):
            ok3, got, _ = git_ok(into, "rev-parse", entry["ref"])
            if not ok3 or got != entry["object"]:
                mismatches.append(
                    "ref not restored: %s expected %s got %s"
                    % (entry["ref"], entry["object"][:12], (got or "ABSENT")[:12])
                )
            else:
                restored.append(entry["ref"])
    else:
        mismatches.append("refs.bundle absent from the handoff directory")

    # runtime artefacts
    if args.home:
        home = Path(args.home).expanduser()
        src = bundle_dir / "runtime-artifacts" / "lineage"
        if src.is_dir() and not args.dry_run:
            dest = home / ".legend" / "lineage"
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                shutil.rmtree(str(dest))
            shutil.copytree(str(src), str(dest))
        for entry in manifest.get("artifact_references", {}).get("runtime_state", []):
            p = bundle_dir / entry["path"]
            if not p.is_file() or sha256_file(p) != entry["sha256"]:
                mismatches.append("runtime artefact missing or altered: %s" % entry["path"])

    # checkpoint must exist at the destination
    cp = manifest.get("last_valid_checkpoint", {}).get("commit")
    if cp:
        ok, _, _ = git_ok(into, "cat-file", "-e", cp + "^{commit}")
        if not ok:
            mismatches.append("LAST_VALID_CHECKPOINT %s absent at destination" % cp[:12])

    # HEAD attestation
    if args.expect_head and args.expect_head != manifest.get("head"):
        mismatches.append(
            "HEAD attestation mismatch: caller expected %s, manifest records %s"
            % (args.expect_head[:12], str(manifest.get("head"))[:12])
        )

    # AUTHORITY — always OBSERVER unless the out-of-band secret is presented
    authority = "OBSERVER"
    grant_fp = manifest.get("authority", {}).get("grant_fingerprint")
    if args.claim_authority:
        if grant_fp and sha256_text(args.claim_authority) == grant_fp:
            authority = manifest.get("authority", {}).get("at_handoff", "OBSERVER")
        else:
            mismatches.append(
                "authority claim REJECTED: presented secret does not match the recorded "
                "grant fingerprint. Landing as OBSERVER."
            )

    return _resume_verdict(manifest, mismatches, authority, restored)


def _resume_verdict(manifest, mismatches, authority, restored=None):
    restored = restored or []
    status = "RESUME_OK" if not mismatches else "RESUME_FAIL"
    print("%s" % status)
    print("  SESSION_ID   %s" % manifest.get("session_id"))
    print("  ACTOR_ID     %s" % manifest.get("actor_id"))
    print("  TASK_ID      %s" % manifest.get("task_id"))
    print("  RUNTIME      %s (%s)" % (manifest.get("runtime"), manifest.get("runtime_version")))
    print("  WORKTREE     %s" % manifest.get("worktree"))
    print("  BRANCH       %s" % manifest.get("branch"))
    print("  HEAD         %s" % manifest.get("head"))
    print("  AUTHORITY    %s   (at handoff: %s — never inherited)"
          % (authority, manifest.get("authority", {}).get("at_handoff")))
    print("  CHECKPOINT   %s" % manifest.get("last_valid_checkpoint", {}).get("commit"))
    print("  refs restored: %d" % len(restored))
    for m in mismatches:
        print("  ! %s" % m)
    return 0 if not mismatches else 1


# ---------------------------------------------------------------------------
# P0.7 — sync
# ---------------------------------------------------------------------------


def cmd_sync(args):
    root = Path(args.root).resolve()
    failures = []
    checks = []

    def check(name, ok, detail):
        checks.append((name, "PASS" if ok else "FAIL", detail))
        if not ok:
            failures.append(name)

    identity = repo_identity(root)
    check("repo.is_git", bool(identity["root_commits"]), "root commits: %d" % len(identity["root_commits"]))
    remotes = identity["remotes"]
    check("remote.exists", args.remote in remotes, "remotes: %s" % ",".join(sorted(remotes)))
    if args.expect_remote_url:
        check(
            "remote.url",
            remotes.get(args.remote) == args.expect_remote_url,
            "%s -> %s" % (args.remote, remotes.get(args.remote)),
        )

    ok, local, _ = git_ok(root, "rev-parse", "refs/heads/" + args.branch)
    check("branch.exists", ok, "%s -> %s" % (args.branch, local[:12] if ok else "ABSENT"))

    if args.fetch:
        okf, _, errf = git_ok(root, "fetch", args.remote, args.branch)
        check("fetch", okf, errf[:160] if not okf else "fetched %s/%s" % (args.remote, args.branch))

    okr, remote_tip, _ = git_ok(root, "rev-parse", "refs/remotes/%s/%s" % (args.remote, args.branch))
    check("remote.branch.exists", okr, remote_tip[:12] if okr else "ABSENT")

    if ok and okr:
        check("head.parity", local == remote_tip, "local %s vs remote %s" % (local[:12], remote_tip[:12]))
        okm, base, _ = git_ok(root, "merge-base", local, remote_tip)
        ff = okm and (base == local or base == remote_tip)
        check("ff_only.possible", ff, "merge-base %s" % (base[:12] if okm else "n/a"))

    dirty_wts = []
    for wt in worktrees(root):
        _, _, modified, _ = worktree_state(wt)
        if modified:
            dirty_wts.append(Path(wt).name)
    check("worktree.consistency", not dirty_wts, "dirty: %s" % (",".join(dirty_wts) or "none"))

    print("SYNC %s" % ("PASS" if not failures else "FAIL"))
    for name, verdict, detail in checks:
        print("  %-26s %-5s %s" % (name, verdict, detail))
    print("  checks run: %d   failures: %d" % (len(checks), len(failures)))
    return 0 if not failures else 1


# ---------------------------------------------------------------------------
# classify command
# ---------------------------------------------------------------------------


def cmd_classify(args):
    root = Path(args.root).resolve()
    surfaces, unknown_required = classify(root, home=args.home)
    if args.json:
        print(
            json.dumps(
                {
                    "surfaces": [s.as_dict() for s in surfaces],
                    "counts": _class_counts(surfaces),
                    "unknown_required_state": unknown_required,
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print("%-40s %-22s %7s %9s  %s" % ("SURFACE", "CLASS", "COUNT", "REQUIRED", "TRANSPORT"))
        print("-" * 118)
        for s in surfaces:
            print(
                "%-40s %-22s %7d %9s  %s"
                % (s.sid, s.klass, s.count, "yes" if s.required else "no", s.transport)
            )
        print("-" * 118)
        print("surfaces classified: %d   (positive control: must equal rows above)" % len(surfaces))
        counts = _class_counts(surfaces)
        for c in CLASSES:
            print("  %-22s %d" % (c, counts[c]))
        print("UNKNOWN_REQUIRED_STATE: %d" % unknown_required)
        if unknown_required:
            print("HANDOFF_DENY — unclassified state is required for resume.")
    return 0


# ---------------------------------------------------------------------------


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd")

    c = sub.add_parser("classify", help="classify every state surface")
    c.add_argument("--root", default=".")
    c.add_argument("--home", default=None)
    c.add_argument("--json", action="store_true")
    c.set_defaults(func=cmd_classify)

    h = sub.add_parser("handoff", help="build a handoff bundle")
    h.add_argument("--root", default=".")
    h.add_argument("--out", required=True)
    h.add_argument("--home", default=None)
    h.add_argument("--actor", default="unknown")
    h.add_argument("--task", default="unknown")
    h.add_argument("--session", default="unknown")
    h.add_argument("--runtime", default="claude-code")
    h.add_argument("--runtime-version", default="unknown")
    h.add_argument("--worktree", default=None)
    h.add_argument("--authority", default="OBSERVER")
    h.add_argument("--authority-secret", default=None,
                   help="out-of-band secret; only its sha256 is recorded")
    h.add_argument("--remote", default="development")
    h.add_argument("--branch", default="main")
    h.add_argument("--check-remote", action="store_true", help="consult the network (read-only)")
    h.add_argument("--accept-unknown", action="store_true",
                   help="override the UNKNOWN gate; recorded in the manifest")
    h.add_argument("--force", action="store_true")
    h.set_defaults(func=cmd_handoff)

    r = sub.add_parser("resume", help="reconstruct at the destination")
    r.add_argument("--bundle", required=True)
    r.add_argument("--into", required=True)
    r.add_argument("--home", default=None)
    r.add_argument("--claim-authority", default=None)
    r.add_argument("--expect-head", default=None)
    r.add_argument("--dry-run", action="store_true")
    r.set_defaults(func=cmd_resume)

    s = sub.add_parser("sync", help="verify remote parity")
    s.add_argument("--root", default=".")
    s.add_argument("--remote", default="development")
    s.add_argument("--branch", default="main")
    s.add_argument("--expect-remote-url", default=None)
    s.add_argument("--fetch", action="store_true")
    s.set_defaults(func=cmd_sync)

    args = p.parse_args(argv)
    if not getattr(args, "func", None):
        p.print_help()
        return 2
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
