---
artifact: LEGEND protocol — CROSS-HOST HANDOFF (lossless session transfer)
protocol_id: XHOST
governance_version: 3.1.1
status: PROPOSED — MVP, built and demonstrated 2026-08-31; not yet reviewed or ratified
normative: no — this document describes a tool and its measured limits. It legislates nothing.
complements: framework/protocols/cross_session_transport.md (XPORT). XPORT says authoritative
  content must live in a durable repository artifact. XHOST is the consequence XPORT does not
  cover: SOME DURABLE ARTIFACTS ARE NOT REACHABLE FROM THE REMOTE, so "it is committed" and
  "another machine can get it" are different claims.
implemented_by: framework/scripts/legend_handoff.py
demonstrated_by: framework/scripts/test_legend_handoff.py (14 tests, 8 negative controls) and
  its `--reconstruct-real` verb, which resumes an actual payload into a repository holding only
  what the development remote carries
adjudicated_by: framework/state/handoff_adjudication.jsonl (per-file, re-verified every run)
enforcement_mode: MECHANICAL for the gates it runs; PROCEDURAL for running it at all.
  Nothing in this protocol executes between turns.
---

# CROSS-HOST HANDOFF — committed is not the same as transferable

## 0 · The finding that produced this

`git push development main` moves what `main` reaches. It was assumed that this made the
laboratory transferable. It does not.

**Measured 2026-08-31 at `main` = `788c357d`, with every branch still at its dispatch state
(this protocol's own branch had not yet committed), `git for-each-ref` as the denominator
(144 refs total):**

| Population | Count | How it was measured |
|---|---|---|
| refs in the repository | 144 | `git for-each-ref \| wc -l` |
| refs NOT reachable from any `refs/remotes/development/*` | **35** | reachability against `rev-list --objects` over the development remote-tracking refs |
| of those, reachable from NO local branch either | **16** | same test against `refs/heads/*` |

The 16 are the sharp ones: **pushing every branch still loses them.** They are

```
 9  refs/codex/turn-diffs/checkpoints/**   TREE-typed. A push cannot move a tree-typed ref.
 3  refs/preserved/*                       named "preserved" by an actor who meant it
 2  refs/pii-backup/*                      pre-scrub backups
 1  refs/stash                             (same object as refs/preserved/stash-worktree-evidence-index)
 1  refs/tags/bench-participant/withdrawn-non-orphan
```

> 🔴 **These numbers are POPULATION-DERIVED and decay.** They describe one repository at one
> commit. Do not quote them as current. Re-derive:
> `python3 framework/scripts/legend_handoff.py classify --root .`

Of the 14 `refs/codex/**` checkpoints, **5 are reachable from some local branch and 2 from the
development remote** — the two questions have different answers and must not be quoted for each
other. That the test discriminates *within* one ref family is the reason to trust it discriminates
at all: a sweep that returned "all 14 orphaned" would be a signature, not a measurement.

---

## 1 · The mechanism, and why it is a file

The transport is **`git bundle`**, and that choice carries the whole design:

- a bundle carries **arbitrary refs**, tree-typed ones included — verified by unbundling a
  `refs/codex/**` tree ref into a fresh empty repository and reading it back with `ls-tree`;
- a bundle is a **file**. It is carried, not published.

That second property is not a convenience. `refs/pii-backup/*` are pre-scrub backups. There is
no version of "make the laboratory transferable" that is allowed to mean "push the PII backups
to GitHub". A bundle moves them to the destination host over a private channel while **no remote
ever holds them**, and that is the only honest way to move them at all.

---

## 2 · The four verbs

```bash
python3 framework/scripts/legend_handoff.py classify --root .
python3 framework/scripts/legend_handoff.py handoff  --root . --out DIR --actor A --task T --session S
python3 framework/scripts/legend_handoff.py resume   --bundle DIR --into REPO [--claim-authority SECRET]
python3 framework/scripts/legend_handoff.py sync     --root . --remote development --branch main
```

`handoff` **never pushes**, and without `--check-remote` never touches the network: it *verifies*
parity against the remote-tracking ref and says so. Pushing remains someone else's authority.

---

## 3 · The classification, and the hard gate

Every state surface gets **exactly one** class. Measured 2026-08-31 at `main` = `6b48dff`:
**24 surfaces**.

| Class | Surfaces | What it means for transfer |
|---|---|---|
| `VERSIONED` | 5 | travels with the commit |
| `RUNTIME_DURABLE` | 8 | must be carried; a clone does not have it |
| `REBUILDABLE_CACHE` | 2 | deliberately NOT transferred |
| `EPHEMERAL` | 3 | not transferred; nothing is lost |
| `SECRET_MACHINE_LOCAL` | 3 | never pushed; re-authored or carried privately |
| `EXTERNAL_REFERENCE` | 2 | reachable by URL from any host |
| `UNKNOWN` | 1 | **blocks** when its count is non-zero |

> 🔴 **`UNKNOWN` + required-for-resume → `HANDOFF_DENY`.** A hard gate, not a warning.

**Not everything is versioned, and saying so is the point.** `__pycache__` is
`REBUILDABLE_CACHE` and is deliberately not carried — stale bytecode from a cache outside the
repository has already produced a false measurement here once. `files/` (third-party full texts)
is `EXTERNAL_REFERENCE`: re-fetched from the tracked retrieval manifest, with the hash-chained
receipts proving identity. Running processes are `EPHEMERAL` by declaration — see §5.

### 3.1 · The two hard cases, decided rather than deferred

**`refs/pii-backup/*` → `SECRET_MACHINE_LOCAL`, required for resume, bundle-only.** They are
real work (3 and 4 commits ahead of `main`, touching 3 and 6 files) and deleting them loses an
audit trail. They travel in the bundle and **must never be pushed**. If the destination host is
less trusted than this one, the correct action is to exclude them and declare the exclusion —
not to push them somewhere convenient.

**The unpublished branches → `RUNTIME_DURABLE`, required.** (19 at `6b48dff`; the count moves
with every branch, so re-derive it.) They are not declared debt: they
include the entire `plan-runtime-bridge-p00-rev8…rev13` lineage, which is the lineage that exists
to protect the authority invariant in §4. Losing it loses the reasoning behind the control.

`refs/tags/bench-participant/withdrawn-non-orphan` is a deliberate **withdrawal** record whose
own message says the object it names carried evaluator answers verbatim. It is preserved as an
audit trail and is a positive reason not to publish the bundle.

### 3.2 · Untracked state, adjudicated per file rather than per pattern

`EPHEMERAL_UNTRACKED` is a list of PATTERNS. It cannot speak about a file that is neither junk
nor obviously state — a review nobody committed, a session evaluation a sandbox refused to stage.
Fifteen such files held this repository at `HANDOFF_DENY`.

`framework/state/handoff_adjudication.jsonl` carries one record per file: `worktree`, `path`,
`owner`, `class`, `sha256`, `reason`, `required_for_resume`, `destination_decision`. It is
tracked, so it travels with the repository.

> 🔴 **A record is re-verified, never trusted.** On every run `adjudicate_untracked` recompares
> the declared digest against the disk and recomputes the preservation evidence. A file edited
> after adjudication is `DRIFTED` and returns to `UNKNOWN`. A file declared `VERSIONED` or
> `RUNTIME_DURABLE` whose bytes are reachable from no ref AND have no byte-identical copy under
> `~/.legend/state/payload/` is `UNPRESERVED` and returns to `UNKNOWN`. A line that does not
> parse raises its own `UNKNOWN` surface. **Writing a line cannot, on its own, make a gate green.**

What it deliberately does NOT record is where the file should finally live. Preserving another
actor's work and deciding its canonical home are different questions, and the second belongs to
its owner — recorded per record as `TRUE_HUMAN_REQUIRED`.

**The ref population is the whole finding.** A sweep over `refs/heads refs/tags refs/remotes
refs/preserved refs/pii-backup` — 130 refs — found those fifteen filenames in **zero** of them.
`for-each-ref` with no pattern is 145 refs, and at that denominator **fourteen of the fifteen are
byte-identical to blobs already reachable from `refs/codex/turn-diffs/**`**, which the bundle
already carried. The tool had been choosing its own denominator. The fifteenth was in no ref and
not in the object store at all.

`~/.legend/state/` is the durable payload, sibling to `~/.legend/lineage/`, copied into the
bundle by `handoff` and restored by `resume`. Content whose only other home is a ref namespace
that a different runtime prunes on its own schedule is copied there, so the answer survives that
namespace changing.

---

## 4 · The invariant this exists to keep mechanical

```
ACTOR_ID  !=  RUNTIME  !=  SESSION  !=  WORKTREE  !=  AUTHORITY
```

> 🔴 **`resume` ALWAYS lands as `OBSERVER`.** Same `ACTOR_ID` never inherits writer authority.

Write authority is restored only by presenting `--claim-authority` with a secret whose **sha256
was recorded at handoff**. The secret itself does not travel in the bundle — so **the bundle
alone can never restore write authority**, which is what makes the property structural rather
than a promise. A wrong secret is REJECTED and the session still lands as `OBSERVER`.

This is the invariant the Runtime Bridge lineage exists to protect, and it has been violated in
practice in this repository. That is why it is a mechanism and not a sentence.

---

## 5 · Declared limitations — preferred over widening the architecture

1. **Processes do not migrate.** A checkpoint plus the restart contract in the manifest replaces
   migration. An in-flight turn is lost, by design.
2. **`deployment/local_instance.md` is not transferred.** It is machine-local *by definition* —
   absolute paths carrying a username, a runtime instance id, live session refs. The destination
   authors its own.
3. **`files/` is not transferred** (copyright). Re-fetched by reference.
4. **The chat transcript store (`~/.claude/projects/**`) is not transferred.** Only what was
   committed or bundled survives. A decision that exists only in a transcript does not migrate.
5. **`handoff` verifies remote parity, it does not achieve it.** Without `--check-remote` the
   comparison is against the last fetch.
6. **Nothing runs between turns.** Somebody has to run `handoff` before the machine disappears.
7. **The bundle is unencrypted.** It carries `refs/pii-backup/*`. Channel security is the
   operator's, and this tool does not provide it.
8. **An adjudication records a class and a reason; the reason is not checkable.** The digest and
   the preservation evidence are mechanical. That the stated reason is *true* is not.
9. **A destination is one checkout; a source is many worktrees.** `resume` refuses to apply a
   dirty patch at a commit that is not the one it was taken at, so on a real source most patches
   land only after the destination recreates the worktree at that commit. Refusing is correct —
   the patch is carried and digest-verified either way — but "restored" and "applied" are two
   different counts and must not be quoted for each other.

### 5.1 · Two defects only real state exposed

The fixture roundtrip passed while the real payload restored nothing, because the fixture builds
the surface it then checks.

**Root-set equality refused the right repository.** `repo_identity` hashes the sorted set of
`rev-list --max-parents=0 --all`, which is population-derived: it grows with every orphan-rooted
branch. This repository has two roots (`bench-blind-participant` was started empty) and a clone
of the remote reaches one, so equality failed — *before* the bundle carrying the missing root was
fetched. The relation is now containment: every root the destination holds must be one this
repository knows, and the two must share at least one.

**`git fetch` refuses to write the checked-out branch and aborts the entire refspec.** One such
ref left `refs restored: 0` — all 38 lost together. The fixture never saw it because there `main`
is published and so is never bundled; on a real source `main` is ahead of the remote, so it *is*
bundled, and a fresh clone is always on `main`. The checked-out branch is now landed separately
and only as a fast-forward; a destination whose own commit is not an ancestor gets a refusal.

Re-derive rather than quote:

```bash
python3 framework/scripts/test_legend_handoff.py                     # 14 tests, 8 negative controls
python3 framework/scripts/test_legend_handoff.py --table             # the lossless table, with its denominator
python3 framework/scripts/test_legend_handoff.py --reconstruct-real \
    --root . --payload HANDOFF_DIR --scratch /tmp/recon              # the REAL payload, into a remote-only clone
```

---

## 6 · VPS readiness — prepared, not connected

No VPS was contacted. The external-access boundary is where this stops.

**`VPS_GIT_READY`** — the destination needs: `git` (demonstrated on 2.50.1; no lower bound was
tested, so none is claimed), network reach to
`github.com/marinomassimo-dot/legend-development.git`, and a credential for it. The repository is
identified by root-commit digest, not remote URL, so `resume` refuses to reconstruct into the
wrong repository even if the remote is renamed.

**`VPS_STATE_TRANSFER_READY`** — one directory moves: `manifest.json`, `refs.bundle`,
`dirty/*.patch`, `runtime-artifacts/lineage/`, `runtime-artifacts/state/`, `SHA256SUMS`.
Measured at `6b48dff`: **14 MB total, of which `refs.bundle` is 13,886,219 bytes over 38 refs.**
Transfer with `scp -r` or `rsync -a` over a private channel. **It contains `refs/pii-backup/*`.
Do not put it on a public host and do not push it to a remote.**

> A smaller bundle is not the lever it looks like. Measured by rebuilding the bundle with each
> namespace removed: dropping `refs/pii-backup/*` saves **29,211 bytes — 0.21%**, and both of its
> refs are reachable from no other ref, so dropping them destroys them for the destination.
> `refs/preserved/*` and `refs/stash` contribute **0 unique objects** (`refs/stash` is the same
> object as `refs/preserved/stash-worktree-evidence-index`) and cost nothing but their names,
> which are the record of deliberate preservation. The size is in `refs/heads/*` (1,838 unique
> objects). **The reason to think about the sensitive refs is sensitivity, not size.**

**`VPS_BOOTSTRAP_COMMANDS`**

```bash
git clone https://github.com/marinomassimo-dot/legend-development.git legend-public
cd legend-public && git remote rename origin development && git fetch development
# transfer HANDOFF_DIR to the VPS over a private channel, then:
python3 framework/scripts/legend_handoff.py resume --bundle HANDOFF_DIR --into . --home ~
python3 framework/scripts/legend_handoff.py sync --root . --remote development --branch main
python3 framework/scripts/legend_lint.py .
python3 framework/scripts/fulltext_receipts.py verify
```

**`VPS_RESUME_PROCEDURE`** — `resume` fails closed on: repo identity mismatch, altered transported
file, bundle failing verification, any promised ref not restored at the promised object, a
checkpoint absent at the destination, a dirty patch that does not apply, and a rejected authority
claim. On success it prints the full attestation — `SESSION · ACTOR · TASK · RUNTIME · WORKTREE ·
BRANCH · HEAD · AUTHORITY · CHECKPOINT` — with `AUTHORITY OBSERVER`. Authority is then re-acquired
through the lease, explicitly, never inherited. Finally: author a new
`deployment/local_instance.md`, and rebuild caches and virtualenvs rather than copying them.

**`TRUE_HUMAN_REQUIRED`** — VPS host, credentials and the private transfer channel. Their absence
blocks nothing on the Mac/GitHub side: every verb above runs and is demonstrated locally.
