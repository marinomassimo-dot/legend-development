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

#: A per-file adjudication of untracked state, tracked in git so it travels with the
#: repository. It is a DECLARATION, not a waiver: `adjudicate_untracked` re-verifies
#: every record against the disk and against the live object store on every run, and a
#: record whose evidence no longer holds returns its file to UNKNOWN. Writing a line
#: here can therefore never, on its own, make a gate green.
ADJUDICATION_FILE = "framework/state/handoff_adjudication.jsonl"

#: The durable non-git surface. `~/.legend/lineage` already existed; `~/.legend/state`
#: is its sibling for content that must outlive this machine but that no ref carries.
#: `payload/<worktree-basename>/<path-relative-to-that-worktree>` mirrors the origin
#: layout so a destination can put each file back where it came from.
LEGEND_STATE_DIR = ("state",)
LEGEND_STATE_PAYLOAD = "payload"

#: Classes whose declaration is only honoured if the content is DEMONSTRABLY preserved
#: somewhere that survives this machine. The other classes assert the opposite — that
#: the content is not worth carrying — so demanding preservation of them would be
#: incoherent.
CLASSES_REQUIRING_PRESERVATION = (VERSIONED, RUNTIME_DURABLE)


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


def all_reachable_blobs(root):
    """Every blob id reachable from EVERY ref, tree-typed refs included.

    🔴 The denominator here is `for-each-ref` with no pattern, and that is the whole
    point of the function. A sweep restricted to `refs/heads`, `refs/tags` and
    `refs/remotes` — the three `--all` covers — reports that this repository's
    `learning/mirror/*` documents exist in NO ref. Adding `refs/codex/**` to the
    population changes that answer to fourteen of fifteen files. The tool must never
    be the thing that decides which refs count.
    """
    ok, tips, _ = git_ok(root, "for-each-ref", "--format=%(objectname)")
    if not ok or not tips.strip():
        return set()
    proc = subprocess.run(
        ["git", "-C", str(root), "rev-list", "--objects", "--stdin"],
        input=tips, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    )
    if proc.returncode != 0:
        return set()
    return set(line.split()[0] for line in proc.stdout.splitlines() if line.strip())


def load_adjudications(root):
    """(records keyed by (worktree_basename, relpath), list of parse problems).

    A malformed line is a problem, never a silently skipped record: an adjudication
    file that half-parses would quietly return files to UNKNOWN with no explanation.
    """
    path = Path(root) / ADJUDICATION_FILE
    records, problems = {}, []
    if not path.is_file():
        return records, problems
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        try:
            rec = json.loads(line)
        except ValueError as exc:
            problems.append("%s:%d is not JSON: %s" % (ADJUDICATION_FILE, lineno, exc))
            continue
        wt, rel, klass = rec.get("worktree"), rec.get("path"), rec.get("class")
        if not wt or not rel:
            problems.append("%s:%d has no worktree/path" % (ADJUDICATION_FILE, lineno))
            continue
        if klass not in CLASSES:
            problems.append(
                "%s:%d declares class %r, which is not one of %s"
                % (ADJUDICATION_FILE, lineno, klass, ", ".join(CLASSES))
            )
            continue
        records[(wt, rel)] = rec
    return records, problems


def durable_payload_path(home, worktree_basename, relpath):
    return Path(home).joinpath(".legend", *LEGEND_STATE_DIR) / LEGEND_STATE_PAYLOAD \
        / worktree_basename / relpath


def adjudicate_untracked(root, home, worktree_basename, relpath, abspath,
                         records, blobs):
    """(class, reason) for one untracked file. UNKNOWN is the failure direction.

    Four ways to stay UNKNOWN, and each is a separate sentence in the reason so a
    reader never has to guess which one fired:

        undeclared        nobody adjudicated it
        drifted           the file changed after it was adjudicated
        unpreserved       it is declared worth keeping and is nowhere durable
        declared UNKNOWN  an honest residual, recorded rather than rounded away
    """
    rec = records.get((worktree_basename, relpath))
    if rec is None:
        return UNKNOWN, "no adjudication record in " + ADJUDICATION_FILE
    klass = rec["class"]

    declared = rec.get("sha256")
    try:
        actual = sha256_file(abspath)
    except (IOError, OSError) as exc:
        return UNKNOWN, "adjudicated but unreadable on disk: %s" % exc
    if not declared or declared != actual:
        return UNKNOWN, (
            "DRIFTED: adjudicated at sha256 %s, on disk now %s. The adjudication "
            "describes bytes that are no longer there."
            % (str(declared)[:12], actual[:12])
        )

    if klass == UNKNOWN:
        return UNKNOWN, rec.get("reason") or "declared UNKNOWN"

    if klass in CLASSES_REQUIRING_PRESERVATION:
        held = []
        blob = git(root, "hash-object", str(abspath), check=False)
        if blob and blob in blobs:
            held.append("git-object:" + blob[:12])
        copy = durable_payload_path(home, worktree_basename, relpath)
        if copy.is_file() and sha256_file(copy) == actual:
            held.append("durable-copy:" + str(copy))
        if not held:
            return UNKNOWN, (
                "UNPRESERVED: declared %s, but its bytes are reachable from no ref and "
                "no byte-identical copy exists under ~/.legend/%s/%s. A class that "
                "promises survival is not honoured by the promise."
                % (klass, "/".join(LEGEND_STATE_DIR), LEGEND_STATE_PAYLOAD)
            )
        return klass, "%s; preserved by %s" % (rec.get("reason", ""), " + ".join(held))

    return klass, rec.get("reason") or "declared %s with no reason given" % klass


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
    records, adj_problems = load_adjudications(root)
    blobs = all_reachable_blobs(root)
    adjudicated = []
    adjudicated_counts = dict((c, 0) for c in CLASSES)
    for wt in wts:
        branch, head, modified, untracked = worktree_state(wt)
        if modified:
            dirty_total += len(modified)
            dirty_detail.append({"worktree": wt, "branch": branch, "modified": len(modified)})
        base = Path(wt).name or "root"
        for rel in untracked:
            if is_declared_ephemeral(rel):
                untracked_ephemeral += 1
                continue
            klass, why = adjudicate_untracked(
                root, home, base, rel, Path(wt) / rel, records, blobs
            )
            if klass == UNKNOWN:
                untracked_unknown.append({"worktree": wt, "path": rel, "why": why})
            else:
                adjudicated_counts[klass] += 1
                adjudicated.append(
                    {"worktree": base, "path": rel, "class": klass,
                     "owner": records[(base, rel)].get("owner"), "why": why}
                )

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
            "git.worktree.untracked.adjudicated",
            RUNTIME_DURABLE,
            len(adjudicated),
            True,
            "untracked files with a per-file adjudication in %s whose evidence was "
            "RE-VERIFIED this run: the declared digest still matches the disk, and any "
            "class promising survival is backed by a reachable blob or a byte-identical "
            "durable copy. by_class=%s detail=%s"
            % (ADJUDICATION_FILE,
               json.dumps(dict((k, v) for k, v in adjudicated_counts.items() if v)),
               json.dumps(adjudicated[:40])),
            "bundle (durable payload) + refs already carried",
        )
    )
    surfaces.append(
        Surface(
            "git.worktree.untracked.unclassified",
            UNKNOWN,
            len(untracked_unknown),
            True,
            "untracked files nobody has classified, or whose adjudication no longer "
            "holds. Each is either in-progress work or junk, and the tool cannot tell "
            "which. detail=%s" % json.dumps(untracked_unknown[:40]),
            "DENY until committed or declared",
        )
    )
    if adj_problems:
        surfaces.append(
            Surface(
                "git.worktree.untracked.adjudication_malformed",
                UNKNOWN,
                len(adj_problems),
                True,
                "lines of %s that could not be read as an adjudication. An unreadable "
                "record is not an absent one: it may be the record that was supposed to "
                "cover a file. detail=%s" % (ADJUDICATION_FILE, json.dumps(adj_problems[:20])),
                "DENY until the record parses",
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

    lstate = home.joinpath(".legend", *LEGEND_STATE_DIR)
    state_files = sorted(
        str(p.relative_to(lstate)) for p in lstate.rglob("*") if p.is_file()
    ) if lstate.is_dir() else []
    surfaces.append(
        Surface(
            "fs.legend.state",
            RUNTIME_DURABLE,
            len(state_files),
            True,
            "~/.legend/%s — the durable payload for adjudicated state that no ref "
            "carries. Outside the repository, so no clone and no push moves it. "
            "files=%s" % ("/".join(LEGEND_STATE_DIR), json.dumps(state_files[:40])),
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
        # NOT git_ok: it strips, and a stripped trailing newline is a corrupt patch.
        proc = subprocess.run(
            ["git", "-C", str(wt), "diff", "--binary", "HEAD"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
        if proc.returncode != 0:
            problems.append(
                "could not capture dirty diff for %s: %s" % (wt, proc.stderr.strip()[:200])
            )
            continue
        target.write_text(proc.stdout, encoding="utf-8")
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
    for name, src_dir in (
        ("lineage", home / ".legend" / "lineage"),
        ("/".join(LEGEND_STATE_DIR), home.joinpath(".legend", *LEGEND_STATE_DIR)),
    ):
        if not src_dir.is_dir():
            continue
        dest = out / "runtime-artifacts" / name
        shutil.copytree(str(src_dir), str(dest))
        for p in sorted(dest.rglob("*")):
            if p.is_file():
                runtime_state.append(
                    {
                        "path": str(p.relative_to(out)),
                        "origin": str(p).replace(str(dest), str(src_dir)),
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
                "copy runtime-artifacts/state to ~/.legend/state — its payload/ holds "
                "adjudicated untracked work; put each file back at "
                "<worktree>/<path> named by framework/state/handoff_adjudication.jsonl",
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
    "framework/state/handoff_adjudication.jsonl records a CLASS and a REASON for an "
    "untracked file; it does not record where that file should finally live. A file can "
    "be losslessly preserved and still be waiting on its owner to decide whether it "
    "belongs in a commit — those are two different questions and this tool answers one.",
    "An adjudication is re-verified, never trusted: the declared digest is recompared to "
    "the disk and the preservation evidence recomputed on every run, so a file edited "
    "after adjudication returns to UNKNOWN and re-raises the gate. What the mechanism "
    "cannot check is whether the stated REASON is true.",
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
    # 🔴 Equality of root-commit sets was WRONG, and only real state showed it. The set
    # is population-derived: it grows with every orphan-rooted branch. This repository
    # has two roots because `bench-blind-participant` was started empty; a fresh clone
    # of the development remote — which is exactly what a destination is — reaches one.
    # Equality therefore refused the RIGHT repository, and refused it BEFORE fetching
    # the bundle that carries the missing root. Containment is the honest relation:
    # every root the destination already has must be one this repository knows, and the
    # two must share at least one. An unrelated repository shares none and still fails.
    dest_roots = set(dest_identity["root_commits"])
    src_roots = set(src_identity.get("root_commits") or [])
    foreign = sorted(dest_roots - src_roots)
    if not src_roots:
        mismatches.append("manifest records no root commit; identity cannot be checked")
    elif foreign:
        mismatches.append(
            "repo identity mismatch: destination has %d root commit(s) this repository "
            "does not know (%s) — that is foreign history, not a subset"
            % (len(foreign), ", ".join(r[:12] for r in foreign))
        )
    elif dest_roots and not (dest_roots & src_roots):
        mismatches.append(
            "repo identity mismatch: destination shares no root commit with the manifest"
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
            # 🔴 `git fetch` REFUSES to write the branch the destination has checked
            # out, and aborts the WHOLE refspec when it does — so one such ref left
            # `refs restored: 0`. The fixture never saw it: there `main` is published,
            # so it is not bundled. On a real source `main` is usually AHEAD of the
            # remote, so it IS bundled, and the destination is always on `main`.
            _, checked_out, _ = git_ok(into, "branch", "--show-current")
            skip = "refs/heads/" + checked_out if checked_out else None
            refspecs = ["+refs/*:refs/*"]
            if skip and any(e["ref"] == skip for e in expect.get("refs", [])):
                # everything except the checked-out branch, which is landed below
                refspecs = [
                    "+%s:%s" % (e["ref"], e["ref"])
                    for e in expect.get("refs", []) if e["ref"] != skip
                ]
            ok2, _, err2 = git_ok(into, "fetch", str(bpath), *refspecs)
            if not ok2:
                mismatches.append("bundle fetch failed: %s" % err2[:300])
            elif skip and any(e["ref"] == skip for e in expect.get("refs", [])):
                want = [e["object"] for e in expect.get("refs", []) if e["ref"] == skip][0]
                _, have, _ = git_ok(into, "rev-parse", "HEAD")
                okf, _, _ = git_ok(into, "merge-base", "--is-ancestor", have, want)
                if have == want:
                    pass
                elif okf:
                    # a fast-forward of the checked-out branch onto the handed-off tip:
                    # the destination held only the remote's tip, which is behind
                    okr, _, errr = git_ok(into, "reset", "--hard", want)
                    if not okr:
                        mismatches.append(
                            "could not land %s at %s: %s" % (skip, want[:12], errr[:200])
                        )
                else:
                    mismatches.append(
                        "%s is checked out at %s, which is NOT an ancestor of the "
                        "handed-off %s. Refusing to discard destination work."
                        % (skip, have[:12], want[:12])
                    )
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

    # uncommitted tracked work — captured at handoff, RE-APPLIED here.
    # Capturing a patch and never applying it is not losslessness, it is a receipt for
    # work that did not arrive.
    applied = []
    already = []
    for entry in manifest.get("artifact_references", {}).get("dirty_patches", []):
        p = bundle_dir / entry["patch"]
        if not p.is_file():
            mismatches.append("dirty patch absent: %s" % entry["patch"])
            continue
        if sha256_file(p) != entry["sha256"]:
            mismatches.append("dirty patch altered in transit: %s" % entry["patch"])
            continue
        if entry.get("head"):
            okc, _, _ = git_ok(into, "cat-file", "-e", entry["head"] + "^{commit}")
            if not okc:
                mismatches.append(
                    "dirty patch %s was taken at %s, which is absent at the destination"
                    % (entry["patch"], entry["head"][:12])
                )
                continue
        # the destination must be at the same commit, or the patch is being applied blind
        _, dest_head, _ = git_ok(into, "rev-parse", "HEAD")
        if entry.get("head") and dest_head != entry["head"]:
            if not args.apply_dirty_anywhere:
                mismatches.append(
                    "dirty patch %s belongs to %s but destination HEAD is %s "
                    "(use --apply-dirty-anywhere to force)"
                    % (entry["patch"], entry["head"][:12], dest_head[:12])
                )
                continue
        okchk, _, errchk = git_ok(into, "apply", "--check", str(p))
        if not okchk:
            # Already applied is not a failure: resume must be idempotent, or a retry
            # after a partial reconstruction reports a loss that did not happen.
            okrev, _, _ = git_ok(into, "apply", "--check", "--reverse", str(p))
            if okrev:
                already.append(entry["patch"])
                continue
            mismatches.append("dirty patch does not apply cleanly: %s: %s"
                              % (entry["patch"], errchk[:200]))
            continue
        if not args.dry_run:
            oka, _, erra = git_ok(into, "apply", str(p))
            if not oka:
                mismatches.append("dirty patch failed to apply: %s: %s"
                                  % (entry["patch"], erra[:200]))
                continue
        applied.append(entry["patch"])

    # runtime artefacts
    if args.home:
        home = Path(args.home).expanduser()
        for name, dest in (
            ("lineage", home / ".legend" / "lineage"),
            ("/".join(LEGEND_STATE_DIR), home.joinpath(".legend", *LEGEND_STATE_DIR)),
        ):
            src = bundle_dir / "runtime-artifacts" / name
            if src.is_dir() and not args.dry_run:
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

    return _resume_verdict(manifest, mismatches, authority, restored, applied, already)


def _resume_verdict(manifest, mismatches, authority, restored=None, applied=None,
                    already=None):
    restored = restored or []
    applied = applied or []
    already = already or []
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
    print("  refs restored: %d   dirty patches applied: %d (already present: %d)"
          % (len(restored), len(applied), len(already)))
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
    r.add_argument("--apply-dirty-anywhere", action="store_true",
                   help="apply a captured patch even when destination HEAD differs from "
                        "the commit it was taken at")
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
