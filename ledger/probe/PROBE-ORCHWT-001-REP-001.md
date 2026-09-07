---
artifact: OPERATIONAL PROBE RECORD — PROBE-ORCHWT-001 leg 3, independent replication 001
probe_id: PROBE-ORCHWT-001
replicates: ledger/probe/PROBE-ORCHWT-001.md, committed at 601787f on 2026-08-20T20:43:36+0200
leg: 3 — root non-perturbation, the one leg that is NOT retrospectively measurable
executed_by: orchestrator
executed_on: 2026-08-20
session_location: repository ROOT checkout (unchanged for the whole probe)
persistence_surface: worktree `orchestrator`, branch `orchestrator`
authority: body § 11 and Annex D.1 — `WORK_COMMIT`, *"ogni attore, PROPRIO worktree/branch …
  obbligatorio, non canonico"*; Annex H.1 — *"WORK_COMMIT | ogni attore, solo proprio branch"*.
  Rank 1, FROZEN. No `ORCHESTRATOR_LEASE` is required: the lease gates
  `CANONICAL_BATCH_COMMIT` (H.1, D.3 GATE 0). None was acquired for this probe and none is claimed
scope: this probe only. It canonicalizes nothing, approves nothing, and binds no candidate
---

# `PROBE-ORCHWT-001` leg 3 — replication 001

## 1 · Why a replication, when the leg was already executed

Because the leg was already executed, and a readiness task asked for it again. **A previous green
result is not a substitute for the measurement**: leg 3 is a claim about two instants, and reading
someone's record of two instants is not observing two instants. The prior execution is not
doubted here and is not re-adjudicated; it is replicated by a second run that did not consult its
values before taking its own.

**This record fixes one weakness of the record it replicates.** `PROBE-ORCHWT-001` § 4 says
"Recorded in the session report that accompanies this commit" — the leg's own result values live
in the commit message, not in the artefact. That is durable, but it puts the measurement one
indirection away from the record that claims it. The BEFORE values are written into the body
below. The AFTER values cannot be, for a structural reason stated in § 4, and that reason is named
rather than worked around.

## 2 · The measurement, and the mechanism the green result rests on

Two independent facts carry root non-perturbation, and conflating them would overstate the result:

```
BRANCH SEPARATION   the root checkout is on `main`; this commit lands on `orchestrator`.
                    A commit to a branch that no working directory has checked out cannot
                    move that working directory's HEAD. THIS IS THE LOAD-BEARING PROPERTY
IGNORE RULE         `.gitignore:72` carries `.claude/worktrees/`, so the worktree's files are
                    invisible to the root's `git status`. It suppresses untracked-file noise
                    and says NOTHING about HEAD or branch ownership
```

The ignore rule was measured rather than assumed: at T0 the root reported **0** porcelain entries
under `-uall`, and **7** rows mentioning `.claude/worktrees/` once ignored files were included.
Seven rows of real filesystem content are being suppressed by that rule. A reader who took the
porcelain zero as proof of branch separation would be reading a number that the ignore rule
would have produced anyway.

## 3 · BEFORE — instant T0, 2026-08-20T19:17:18Z

```
ROOT     toplevel  <REPO_ROOT>
         branch    main
         HEAD      04693e683a254ff0a6d0619fba47103a0fb7d122
         porcelain -uall            0 entries
         porcelain --ignored rows naming .claude/worktrees/    7

ORCHWT   toplevel  <REPO_ROOT>/.claude/worktrees/orchestrator
         branch    orchestrator
         HEAD      601787f9ec3131988a7fadaa7acffc994b9e2919
         porcelain -uall            0 entries
```

### The instrument is shown capable of returning a different answer

A "0" is worth nothing until the same command is shown returning non-zero. At the instant this
file existed uncommitted, one instrument was run against both surfaces:

```
root     git status --porcelain=v1 -uall   ->  0 entries
orchwt   git status --porcelain=v1 -uall   ->  1 entry   (this file, untracked)
```

One command, one instant, two surfaces, two answers. The zero is a measurement, not a silence.

## 4 · AFTER — and why only half of it needed writing down

The AFTER instant falls after this file is committed, so it cannot be inside the file it describes
without a second commit that would perturb what it measures. **But the two halves of leg 3 are not
alike, and treating them alike is what made this leg look wholly unrecoverable.**

```
BEFORE   genuinely unrecoverable. Nothing observable now can establish what the root was
         doing at T0, which is why § 3 exists and why the leg stayed owed since 2026-08-17
AFTER    for root HEAD, root branch and root cleanliness: DURABLE, and therefore checkable
         by any actor at any later time. If this WORK_COMMIT had perturbed the root, the
         root would not be on `main` at 04693e68 with an empty porcelain — it would still
         be off it. A perturbation of persistent state does not evaporate after the probe
```

So the AFTER half needs no privileged witness. **Any actor can falsify the claim of this record**
by running, in the root checkout:

```bash
git -C <REPO_ROOT> rev-parse --abbrev-ref HEAD     # must be   main
git -C <REPO_ROOT> rev-parse HEAD                  # must be   04693e683a254ff0a6d0619fba47103a0fb7d122
git -C <REPO_ROOT> status --porcelain=v1 -uall     # must be   empty
```

The transient residue — a file written into the root and then removed — is the one AFTER failure
mode this leaves unaddressed, and it is named rather than covered: nothing here excludes it, and
nothing in leg 3 as defined ever did.

## 5 · What this record does not do

It does not canonicalize `CAND-20260819-ORCHSURF`, does not request or imply `HUMAN_APPROVAL`,
does not acquire a lease, does not modify any FROZEN document, does not re-open the closed Mirror
review `REV-ORCHSURF-MIRROR-002`, and does not re-bind the reviewed object, which remains
`BASE_HEAD 04693e68` · `CONTENT_TIP 9a70e94d` · `CANDIDATE_CONTENT_HASH 844de909…acb6dc`. It is
append-only: a later probe that supersedes it is a new record, never an edit to this one.
