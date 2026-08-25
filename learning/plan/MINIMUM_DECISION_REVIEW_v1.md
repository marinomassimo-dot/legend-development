---
artifact: REVIEW of LEGEND_MINIMUM_DECISION_PATH_v1 — is { OPS-DEC-01, OPS-DEC-02 } the minimum
  viable decision set?
record_id: MINIMUM-DECISION-REVIEW-V1
task_id: MINIMUM_DECISION_REVIEW_v1
author: plan seat, unactivated — `roles/plan.md` reads `status: PROPOSED` and confers nothing
actor_id: NOT ESTABLISHED
authored_on: 2026-08-24
dispatcher: operator
governance_version: 3.1.1 — read and cited, neither exercised nor modified
mode: REVIEW_ONLY

STATUS: REVIEW_DELIVERED
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none
creates_no_dec: true
chooses_no_outcome: true
proposes_no_implementation: true

object_under_review: >
  learning/orchestrator/LEGEND_MINIMUM_DECISION_PATH_v1.md — 674 lines, 40 933 bytes,
  blob fe4d9052e86ba538728aa81f3f44540ab517245d, SHA-256
  7934830af673f6e307ffd87958d0735dd3f7875cc8e15352a75524056bb47cde, on disk at the ROOT CHECKOUT
  <repo-root>, untracked on every one of 57 refs
  (`git log --all -- <path>` → no output).

measurement_plane: >
  This review was executed from the worktree
  `<repo-root>/.claude/worktrees/evidence-index`,
  branch `plan-orchsurf-r4-transcription` @ e4aa80c, on 2026-08-24T14:35Z–15:05Z.
  The reviewed record measured at branch `legend-operating-convention-v1` @ 30cb4f3, which is
  the ROOT CHECKOUT's head and is NOT an ancestor of this worktree's head
  (`git merge-base --is-ancestor 30cb4f3 HEAD` → false).
  🔴 **Consequence, stated because it changes what can be compared:** wherever the reviewed
  record writes `HEAD` it means 30cb4f3, and this review does not reproduce that token. Every
  re-derivation below is anchored to a NAMED object — `main` @ 788c357, `30cb4f3`, a named ref,
  or the root checkout's disk — never to `HEAD`. The refs are shared across all worktrees of
  this repository, so ref-scoped sweeps are directly comparable; disk-scoped figures are not,
  and are labelled ROOT CHECKOUT DISK where they occur.

carried_nothing: >
  Every figure the reviewed record reports was re-executed in this session. Two classes were
  NOT re-derived and are marked AS REPORTED where they appear: (i) the Mirror independence
  census (39/39, 25/30, ~29/36), which the record itself carries AS REPORTED — see O-4;
  (ii) the readiness plan's own hostile-review finding IDs (M-n, P-n), which are cited as
  locators into that record, not as measurements.

domain: >
  CONTENT. `plan_defined_parameters.md` § P5.1 declares CONTROL_PLANE_ROOTS exhaustively as
  `governance/candidates/`, `ledger/`, `reviews/`. `learning/` is under none of them, so this
  file is inside the content domain of any candidate spanning this branch — the same as the
  record it reviews.

self_note: >
  This file is written in the `evidence-index` worktree on branch
  `plan-orchsurf-r4-transcription`. It therefore does NOT grow the 12-file untracked corpus in
  the root checkout that `D-1` governs. It starts a second untracked corpus, on a second branch,
  subject to the same hazard and covered by no preservation act anyone has named. That is
  recorded, not resolved.
---

# REVIEW — `LEGEND_MINIMUM_DECISION_PATH_v1`

> **This review decides nothing.** It creates no `DEC`, selects no outcome among any enumerated
> option set, proposes no implementation, no code, no schema and no repository change. It
> contains no recommendation column. Where it says a decision is *missing*, that is a finding
> about the reduction's completeness, not a request that the decision be answered a particular
> way.

---

## 0 · Where the dispatch's four questions are answered

| Dispatch asks | Answered in |
|---|---|
| 1 · Decision compression — can five really become two? Are apparent successors actually prerequisites? | `M-1`, `M-4`, `M-5`, and § MINIMUM DECISION SET |
| 2 · Hidden decisions — operational assumptions, implicit architecture, buried governance readings | `M-1`, `M-9`, `M-10`, `O-1`, `O-2`, `O-7` |
| 3 · Dependency map — decision → what it unblocks → what stays blocked | § MINIMUM DECISION SET, the corrected map |
| 4 · Rehearsal vs governed execution — does the distinction reduce decision load correctly? | `M-9`, and § MINIMUM DECISION SET · *The switch, tested* |

Tags follow the reviewed record's own scheme: `OBS` measured this session with the command
shown; `INF` derived from `OBS`, falsifiable, with the falsifier stated.

---

# CONFIRMED

Re-executed this session. Each row reproduces the record's figure at a named object.

### C-1 · Runtime authority is absent, exactly as described
`OBS` `python3 framework/scripts/lease_state.py` → **`ACTIVE by derivation: 0`**; 5 leases; the
most recent released `2026-08-18T14:05:20Z`. Stored/derived agree on four and disagree on one
(#3: stored `EXPIRED`, derived `STALE`) — which does not move the count.

### C-2 · The event ledger is absent on every ref, with its positive control
`OBS` Sweep over `git for-each-ref` → **57 refs**. `ledger/events` resolves on **0 of 57**.
Positive control `ledger/approvals` resolves on **34 of 57**. `ledger/` on disk holds
`approvals`, `checkpoints`, `retirements`, `tasks` — no `events`, no `consolidated`.
⚠️ The sweep must brace the ref variable: `"${r}:ledger/events"`, never `"$r:ledger/events"` —
zsh applies `:l` / `:r` / `:p` as history modifiers and returns a silent false negative on
every ref. A control that resolves on 34 is what proves the sweep ran.

### C-3 · The Agent Card registry confers nothing, on one ref
`OBS` Path match `agent.card` over 57 refs → **1 ref**, `refs/heads/orchestrator`. Its
frontmatter: `status: PARTIALLY REGISTERED — 3 of 6`, `authority: none — this file records
verified state. It assigns nothing and confers nothing.` **23** occurrences of `UNVERIFIED`,
**21** of `last_verified: NONE`. Its own § reads `CONFIGURED != PROVEN … at the time of writing
there are none, in any actor, of any role.`

### C-4 · The `PROPOSED` population, mechanically classified
`OBS` `git grep -n "^status: PROPOSED" main` → **16 hits**. Each hit line compared to the end of
that file's own frontmatter block (`awk` on the second `---`): **12 FRONTMATTER**, **4
QUOTATION in 3 files** (`PROPOSAL-C9-STATE-MODEL.md:388`,
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md:45` and `:173`,
`SCIENTIFIC-PIPELINE-PREPARATION-001.md:187`). Tracked denominator on `main`: **580**.
The 12 include `BOOTSTRAP.md`, `deployment/deployment_profile.md` and
`governance/plan_defined_parameters.md`, which is where `P7 · EVENT LEDGER — one-writer design`
lives (line 406) — the record's parenthetical is correct.

### C-5 · Three reviewed protocols, no approval requested, and the counter-evidence holds
`OBS` `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` on `main`: **6 lines**; `XPORT` → **0**;
`SCIAB|SCIENTIST-AB` → **0**; control `GOV311` → **5**. `APR-20260816-GOV311-001` carries
`REQUESTED_BY: plan`. The record's own counter-evidence — that the absence is not explained by a
missing requester, because a non-Orchestrator has raised an approval before — **stands as
measured**.

### C-6 · The XPORT bundle is complete except for the operator's half
`OBS` `governance/candidates/CAND-20260819-XPORT.md` is present on `main` and on **17 of 44**
branch refs. `CANDIDATE_CONTENT_HASH 81f241f26ed668ee02e6b04d191c98a4deaa025355d9212bc999b80c6e056e1f`
at `BASE_HEAD 4454feab72b7a0edf65f191be62aeedd899a15ad`;
`human_approval: NOT REQUESTED — no APPROVAL_ID is prefilled here, and none exists`.
`git show mirror:reviews/mirror/REV-XPORT-MIRROR-002.md` → `verdict: ACCEPT`, 4 non-blocking
findings, `reviewer: mirror`.

### C-7 · The C-9 hold, and what it suspends
`OBS` `PROPOSAL-C9-STATE-MODEL.md` frontmatter: `status: ACCEPTED`, `authored_on: 2026-08-17`,
`acceptance_is_not_adoption: true`, and `hold: no implementation and no governance modification
until that review completes; L2 suspended; the status/C-8 batch frozen pending a later operator
decision`.

### C-8 · Every annex citation in the record resolves
`OBS`, each at `main`:

| Cited as | Source | Verbatim |
|---|---|---|
| `H.1` `WORK_COMMIT` | `annex_h_authority_matrix.md:34` | `ogni attore, solo proprio branch, granularità milestone` |
| `H.1` operator row | `annex_h_authority_matrix.md:35` | `Spese / MAJOR approval / governance \| Operatore` |
| `I.2` steps | `annex_i_bootstrap_deployment.md` § I.2 | 3 = repo identity · root state · GOVERNANCE_VERSION · concurrent root writer · worktree; 4 = create/verify worktrees; 7 = registration; 8 = L1 smoke → L2 capability smoke; 9 = lease acquisition; 10 = `ORCHESTRATOR_REGISTRATION` durevole → `ACTIVE_ORCHESTRATOR` |
| `I.3` | same file § I.3 | `reacquisition SOLO su STALE/RELEASED con successione registrata` |
| `C.1` ladder | `annex_c_review_protocol.md:21` | `R0 · R1 PEER · R2 INDEPENDENT (semi-blind) · R3 TRIADIC · R4 METHOD (Mirror) · R5 CROSS-MODEL (Codex)` — **six rungs** |
| `G.2` | `annex_g_mirror.md:27` | `reviewer indipendente scelto da Orchestrator` |
| `G.3` cadence | `annex_g_mirror.md:31` · `ANNEX_INDEX.md:65` | `MIRROR_RETROSPECTIVE ogni N batch`; `**UNASSIGNED** by the annexes; left UNRESOLVED, not filled in by Plan` |
| `ESC-3` | `APPROVAL-GOV311-DEVIATIONS.md:280` | `MIRROR_RETROSPECTIVE interval N: UNRESOLVED, and left so` |
| `J.0` compensator | `annex_j_runtime_control_plane.md:33` | `RBAC enforced a runtime (attori interattivi) \| authority matrix testuale + audit + event ledger (H.1, J.1)` |
| `P7` | `plan_defined_parameters.md:406–416` | design **(a)**, `ledger/events/<ACTOR_ID>.jsonl`, `ledger/consolidated/` derived |

### C-9 · `learning/` is CONTENT, and the record classifies itself correctly
`OBS` `plan_defined_parameters.md` § P5.1 declares `CONTROL_PLANE_ROOTS` exhaustively:
`governance/candidates/`, `ledger/`, `reviews/`. `learning/` is under none. The record's
`domain: CONTENT` is right.

### C-10 · The record's self-count is correct — 11 before it, 12 with it
`OBS` Object-derived, ROOT CHECKOUT DISK vs `git ls-tree -r --name-only 30cb4f3`, with the
`.gitignore` roots excluded: **21 paths exist on disk and are not tracked at 30cb4f3**. Of those,
8 never appear as `??` (7 `page_adjudications/*.png` matched by
`disease-models/*/research/page_adjudications/**/*.png`, plus `deployment/local_instance.md`,
both ignored by the repository's own `.gitignore`), and `.claude/settings.local.json` is ignored
by the operator's **global** ignore file (`git check-ignore -v` →
`~/.config/git/ignore:1`). What remains, and what `git status --porcelain | grep
'^??'` therefore counts:

```
learning/orchestrator/  ................................ 11 records (incl. the reviewed record)
LEGEND_DEVELOPMENT_BOOTSTRAP_AUDIT_v1.md  .............. 1 record, at the repository ROOT
                                                        ──
                                                        12
```

`INF` **11 → 12 is reproducible and the record is right.** I set out to falsify it — 11 of the
12 are under `learning/`, so the obvious reading is that the corpus was 10 — and the twelfth is
the bootstrap audit at the root, which the `??` count includes and a `learning/`-scoped count
does not. Recorded because the near-miss is the finding: the population is *"untracked records
repo-wide, minus everything `.gitignore` hides"*, and only a listing shows that. See `M-10`.

### C-11 · The § 7 demotions that hold
`OBS`/`INF` `D-23` (worktree prune) and `D-24` (exec bits, action pins) sit in the readiness
plan's § 4.2 **IMPORTANT — they do not block the experiment** tier; the record's demotion matches
its source. The 12 `PROPOSED` files are in a state `DEC-20260822` consequence 2 defines rather
than leaves undefined; `undecided ≠ undefined` is sound.

### C-12 · D5's structural claim survives a sweep that could have broken it
`OBS` Union of `reviews/**.md` over all 57 refs → **82 files**: `reviews/mirror` 60,
`reviews/orchestrator` 15, `reviews/plan` 7.
`INF` This does **not** falsify *"Mirror performs the reviews"*, and the temptation to report it
as though it did is the failure this repository has logged before — two populations under one
label. Read at the object level: of the 60 under `reviews/mirror`, **47** are `REV-*` verdict
records; the 15 under `reviews/orchestrator` are `OPEN-`/`CLOSE-` review-management records plus
one patch specification — Orchestrator *opening and closing* reviews under `C.3`, not performing
them; the 7 under `reviews/plan` are `AUTHOR-RESPONSE-*` plus one non-author contribution.
**82 files, but 47 verdicts, and no verdict record is authored by a non-Mirror seat.** The
record's characterisation of the review graph is confirmed. Its *numbers* are not — see `O-4`.

---

# MODIFIED

## `M-1` 🔴 The reduction drops a blocking decision: the redaction of the identifier-bearing records

**What the record says.** § 7: *"Preserving the untracked corpus — **`Φ−1a` needs no decision at
all** — it is a byte copy outside the repository, requiring no git act and no actorhood. Only
`Φ−1c`, the commit, needs `OPS-DEC-01`."* `IMP-1` is *"`WORK_COMMIT` of the untracked corpus"*,
gated by `OPS-DEC-01` and nothing else. NEXT OPERATOR ACTION item 1 is the byte copy.

**What is measured.**

`OBS` The reviewed record contains **0** occurrences of `redact`, `identifier`, `privacy`,
`personal identifier` or `PRIVATE_NAME`. Its 7 occurrences of `D-1` all describe the
*destructibility* hazard (records that could be lost); none describes the *identifier* hazard.

`OBS` Re-derived this session, not carried: the 12-file untracked corpus staged into a scratch
directory and scanned with the repository's own instrument,
`python3 scripts/independent_privacy_scan.py --json <corpus>` → exit **2**,
**5 findings, all severity `BLOCK`, all category `PRIVATE_NAME`, in exactly 2 files**:

```
3  learning/orchestrator/FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md
2  learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md
```

*(Counts only. The matched values are not reproduced here, in this record or anywhere else.)*
This independently reproduces readiness `D-1`'s *"**2** carry 5 registered identifier hits"*.

`OBS` The readiness plan's § 10 operating order states `Φ−1c` as **three acts, not one**:

```
Φ−1c  DURABLE STATE   operator act · needs D-1 · requires an ACTOR
      redact 2 records · preserve design v1's pre-redaction bytes FIRST (M-7) · commit
```

with three EXIT criteria, one of which is *"the gate reports 0 `DIRECT_IDENTIFIER` over the
committed set"*.

`OBS` Readiness `D-1` is a four-option decision in the **BLOCKING** tier — *(a) commit all ·
(b) byte-copy out NOW, then redact the 2 and commit · (c) commit only the clean ones ·
(d) nothing* — and its own text records the consequence of (a): *"(a) writes registered personal
identifiers into the public edition."*

`OBS` Readiness `D-6` — the decision the record maps `OPS-DEC-01` onto — carries
`Depends on: D-1` in its own dependency column.

`OBS` `M-7`, quoted in the readiness plan: *"before any redaction, design v1's pre-redaction
bytes must be preserved: redaction changes its hash, and two records that will be committed cite
the old one."* Re-derived: `LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md` — one of the two
identifier-bearing files — has **no git object for its current bytes** (`git hash-object` on the
disk file, then `git cat-file -e` on the result → absent), and 6 other records in the corpus
reference design v1.

**The defect.** The readiness plan says *"(b), and **its first half** needs no decision from
anyone but you — it is a file copy."* The reviewed record generalises **its first half** to the
whole of `D-1`. That is how the decision disappears: `D-1` is re-described by its cheapest
sub-act, `Φ−1a`, and the sub-act's correct property (*needs no authority*) is inherited by the
parent it does not hold.

**Consequences that follow mechanically.**
1. `IMP-1` as written — *`WORK_COMMIT` of the untracked corpus, gated by `OPS-DEC-01`* — is, on
   the measured corpus, the act that writes 5 `BLOCK`-severity `PRIVATE_NAME` findings into the
   public edition. No gate in the record stands between `OPS-DEC-01` and that outcome.
2. `Φ−1c` in the record is one act; in its source it is three, and the other two are the ones
   that carry the privacy and the hash-integrity constraints.
3. By the record's own criterion — *on the minimum path iff no defined default lets execution
   proceed with durable output* — `D-1` qualifies: there is no defined default under which the
   corpus is committed, and every option that reaches durable output passes through it.
4. The dependency is **upstream** of `OPS-DEC-01`, not parallel to it: `D-6 → D-1` in the source.

`INF` **The minimum set is not two. Under the record's own criterion it is three.**
**Falsifier:** if the operator holds that the first run produces no commit at all — that the
corpus is preserved only by the out-of-repository copy and `Φ−1c` never opens — then `D-1`'s
remaining content is the copy, which the record correctly prices at zero, and the set returns to
two. That reading is available only when `OPS-DEC-01 = (d) defer`, which the record itself
describes as leaving `IMP-1` blocked.

---

## `M-2` The 12-file figure is attached to a clause only 7 files carry

**What the record says.** `OPS-DEC-02` § WHY OPERATOR: *"Both branches turn on the meaning of the
clause **"binding once Mirror hostile review passes and the operator approves"**, present in the
frontmatter of **12 files** on `main`."*

`OBS` `git grep -n "^status: PROPOSED — binding once Mirror hostile review passes and the
operator approves" main` → **9 hits**, of which **7 in frontmatter** (`BOOTSTRAP.md`,
`deployment/deployment_profile.md`, `framework/protocols/cross_session_transport.md`, and the
four `roles/`) and 2 quotations (`PROPOSAL-C9-STATE-MODEL.md:388`, `DEC-20260822…:45`).

`OBS` The other 5 of the 12 carry **four different clauses**:

| File | Its own clause |
|---|---|
| `framework/protocols/controlled_benchmark_ab.md` | `binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC. The` |
| `framework/protocols/scientist_reading_modes.md` | `binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC, after` |
| `governance/candidates/CAND-20260819-P5DOMAIN.md` | `awaiting Mirror hostile review, which Orchestrator opens (Annex C.3)` |
| `governance/design_records/claude_md_migration_map.md` | `part of INTEGRATION_CANDIDATE v3.1.1, subject to Mirror hostile review` |
| `governance/plan_defined_parameters.md` | `normative once Mirror hostile review passes and the operator approves` — **`normative`, not `binding`** |

**The defect.** `12` is the count of *files whose frontmatter carries `status: PROPOSED`*. The
sentence attaches it to *files carrying one specific clause*. These are different populations,
and the difference is load-bearing for `OPS-DEC-02`: two of the five are gated on the **canonical
execution of a different candidate**, not on an operator approval, so an operator act on the
clause the sentence names does not reach them. The record's own § 2.3 states this correctly —
*"binding only on canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC`"* — and § 6 then
counts them under a clause they do not carry.

**Correction, per object:** the clause is in the frontmatter of **7** files; the `PROPOSED`
frontmatter population is **12**; `OPS-DEC-02`'s object list is one of those two, and the record
does not say which.

---

## `M-3` The `12 ≠ 7` discrepancy is reconcilable in one command, and § 8 risk 2 dissolves

**What the record says.** § 2.1: *"**12 ≠ 7 and this record does not reconcile them** — the two
populations may be differently defined … and reconciling them is a measurement nobody has run.
It is listed as `PREP-2`."* § 8 risk 2: *"If C-9's seven is the operative population,
`OPS-DEC-02`'s object list is smaller than stated here."*

**The measurement, run here.**

`OBS` C-9's claim is at `PROPOSAL-C9-STATE-MODEL.md:485`, inside `## 8 · Applied to every live
case`, authored `2026-08-17`. Its § 8 table lists *"Seven `status: PROPOSED` on governed
artifacts"* as **one row** and `claude_md_migration_map.md` **front matter** as a **separate
row** of the same class.

`OBS` The frontmatter `PROPOSED` population at `main`'s last commit dated 2026-08-17
(`1aeca4f`), classified by the same mechanical rule as C-4, is **8 files**:
`BOOTSTRAP.md`, `deployment/deployment_profile.md`, `claude_md_migration_map.md`,
`plan_defined_parameters.md`, and the four `roles/`.

`OBS` First appearance on `main` of each of today's 12 (`git log main --reverse --diff-filter=A`):
8 on 2026-08-16; **4 after C-9 was authored** — `controlled_benchmark_ab.md` and
`scientist_reading_modes.md` on 2026-08-18, `cross_session_transport.md` and
`CAND-20260819-P5DOMAIN.md` on 2026-08-19.

`INF` **8 − `claude_md_migration_map.md` (which C-9 counts in its own row) = 7.** C-9's seven is
not a competing *definition* of the population. It is **the same population measured seven days
earlier**, before four of today's twelve existed. C-9 itself insists on exactly this reading in
its § 2.1, where it defends `materialization_log.md:238` — *"All are marked `status: PROPOSED`"*
— as *"**true on 2026-08-16 when written** … dated testimony"*.
**Falsifier:** if *"governed artifacts"* excludes a file I counted and includes one I did not,
the arithmetic could coincide by accident; the row-level separation of `claude_md_migration_map`
is the direct evidence against that, and any competing enumeration must name its seven objects.

**Correction.** § 8 risk 2 does not stand: C-9's seven cannot be *"the operative population"* for
a decision taken today, because it is a dated observation, not a definition. `PREP-2` is not an
unrun work package — it is the four commands above and it costs minutes, not a record.

---

## `M-4` The `MAPS TO` column claims identity where the source questions differ

The record states: *"This record adds no new decision surface … The mapping column is
load-bearing; nothing is renamed silently."* Measured against the readiness plan:

| Record | Claims | Readiness plan actually says | Divergence |
|---|---|---|---|
| `OPS-DEC-01` — *"By what route does the laboratory acquire a party entitled to write durable state on its behalf, **for the first operational run**"* | `MAPS TO D-6` | `D-6` — *"**Who performs `Φ−1c`'s `WORK_COMMIT`?**"*, options *(a) the operator commits · (b) an explicit activation act granting one session actorhood **for this act** · (c) leave the records uncommitted* | **Widened.** `D-6` scopes one act; `OPS-DEC-01` scopes a standing route for a whole run. `D-6`'s option (b) explicitly contains the words *for this act*; `OPS-DEC-01`'s option (c) reintroduces the scoping as a separate outcome |
| `OPS-DEC-02` — *"governed artifacts or declared rehearsal"* | `MAPS TO D-5` | `D-5` — *"**Unregistered rehearsal, or lift/scope the C-9 L2 hold first?**"*, options *(a) rehearsal claiming no actorhood · (b) scope the hold · (c) lift it* | **Re-cut.** `D-5` bundles the run class **with the C-9 hold**. The record relocates (b) and (c) to a *downstream automatic consequence* of `OPS-DEC-01 = (a)` — *"the C-9 `L2 suspended` hold must be scoped or lifted"*. **Scope-or-lift is itself a choice with different outcomes**, owned by the operator (`status_transition_owner: operator`), and it appears in the record only as a consequence, never as an option set |
| `OPS-DEC-03` — *"what constitutes independence: the registered Mirror seat, an unregistered session under an information barrier, or both"* | `MAPS TO D-14 (floor R2)` | `D-14` — *"**Review floor `R2`?**"* — and it sits in § 4.2, the **non-blocking** tier | **Mis-mapped.** `D-14` sets *how high* the ladder floor is; `OPS-DEC-03` asks *who may stand on it*. `C.1`'s `R2` is `INDEPENDENT (semi-blind)`; who counts as the independent party is not what `D-14` decides |

`INF` The mapping column is doing more work than a mapping: it is where three re-cuts are
recorded as identities. The claim *"nothing is renamed silently"* is true of the **names**; it is
not true of the **questions**.

---

## `M-5` The dependency map has no node for the decision that gates its root

`OBS` § 4's map shows `OPS-DEC-01` as a root with no inbound edge, `OPS-DEC-02` as a second
root, and no edge between them. `D-1` appears nowhere in the map. Its four appearances elsewhere
in the record (§ frontmatter, § 3 `LANE-P` preamble, `PREP-1`, § 6 namespace warning) all
describe the untracked-record hazard.

`OBS` The readiness plan states four edges on `D-1` explicitly, under the heading *"Dependency
edges v1 presented as absent (P-5)"*: `D-6 → D-1`, `D-8 → D-1`, `D-1 → D-8`, `D-4 → D-1`.

`INF` The record inherits its predecessor's own diagnosed defect at one level up: v1 of the
readiness plan *"presented dependency edges as absent"*, the FINAL restored them, and this record
drops the node they attach to. Corrected map: § MINIMUM DECISION SET.

---

## `M-6` Two quotations do not match their sources verbatim

`OBS` The record: *"`C.3` states **"Apertura review solo via Orchestrator"**"* (§ 2.5, and again
in `OPS-DEC-01`'s downstream consequences). `annex_c_review_protocol.md:50` reads
**`Apertura solo via Orchestrator`** — the word `review` is not in the string. The paraphrase is
faithful to the section's subject; the quotation marks are not.

`OBS` The record: *"`DEC-20260822` § **RATIONALE 6** records why an actor may not settle it: *"an
actor choosing the reading that makes its own contract binding would be exactly the convenient
interpretation the gate exists to prevent."*"* That string is verbatim at **§ E-6, line 151** —
where `DEC-20260822` is **quoting `REV-ROLES-MIRROR-001`**. `RATIONALE 6` paraphrases it —
*"an actor choosing the reading that makes its own contract binding **is exactly what the gate
prevents**"* — and cites `(E-6)`.

`INF` Both are locator errors, not substantive ones: the propositions survive. They are recorded
because this repository runs a locator-audit discipline in which a quotation is a verbatim claim
about bytes, and because the second one misattributes **Mirror's** reasoning to the **operator
determination** — which matters in a record whose whole subject is who may settle what.

---

## `M-7` `ACTIVE_ORCHESTRATOR` is reached at `I.2` step 10, not step 9

`OBS` `OPS-DEC-01` outcome (a): *"re-enter `I.2` steps 7–9 and promote a session to
`ACTIVE_ORCHESTRATOR` with a registered succession."* `I.2` reads: `9. condizioni PASS →
acquisizione ORCHESTRATOR_LEASE (I.3)`; `10. ORCHESTRATOR_REGISTRATION durevole →
ACTIVE_ORCHESTRATOR → governance ordinaria`. Steps 7–9 end at the lease; the promotion is step
10. The record states step 10 correctly two paragraphs earlier (*"`I.2` step 10 makes promotion a
durable operator-visible act"*), so this is an internal inconsistency, and it narrows the option
by one act.

---

## `M-8` § 10's XPORT row is a spot check in a table of sweeps

`OBS` The verification trail reports XPORT as `PRESENT main, HEAD, xport · ABSENT mirror,
evidence-index, orchestrator, lettore` — **7 refs**, in a table whose neighbouring rows are
57-ref sweeps with positive controls. Re-derived as a sweep:
`framework/protocols/cross_session_transport.md` resolves on **21 of 57 refs**; the candidate
`CAND-20260819-XPORT.md` on **17 of 44 branch refs**. Nothing the record asserts is false; the
row's method silently differs from the rows around it, and a reader comparing `0 of 57` against
`PRESENT main, HEAD, xport` is comparing a sweep to a sample.

---

## `M-9` 🔴 `REHEARSAL` does not stand `OPS-DEC-03` down — it selects outcome (d) without saying so

**What the record says.** `OPS-DEC-03` `CLASS: CONDITIONAL — fires only on `OPS-DEC-02` =
GOVERNED (or MIXED)`. Its outcome (d) — *"no review is declared for this run"* — is annotated
*"available only under `02 = REHEARSAL`"*. § 4's map: *"D5 stands down → no governed review is
opened, and the outcome record must say so."*

`INF` These two statements are not the same statement. If the decision **does not fire** under
`REHEARSAL`, then under `REHEARSAL` its outcome is (d) **by default**, and the three other
outcomes are unavailable — including **(b) an unregistered session under a declared information
barrier, output labelled non-governed**, which is the one outcome in the whole record that
requires no actorhood, no lease, no opener, no chooser and no activation. The rehearsal branch is
selected precisely *because* it needs none of those; and the record's conditionality removes,
along with the governance, the review posture that survives without it.

`OBS` This is not an abstract option. Two measured items sit under it:
- `C.3` defines the ladder's independent rung as `semi-blind = independence by task framing, **not
  by information barrier**`. So an information-barrier review is not merely *"a review class the
  ladder does not name"* (the record's phrasing, § `OPS-DEC-03` consequence (b)) — it is a
  **different independence mechanism from the one `R2` names**. The record's consequence is
  correct and understated.
- `reviews/plan/NON-AUTHOR-CONTRIBUTION-REV-ORCH-STATE-RECONSTRUCTION-001.md` exists on
  `refs/heads/plan-orchsurf-r4-transcription` — a third party to a review, *"holding neither the
  author's row nor the reviewer's"*, contributing mechanically re-derived facts with
  `mode: CONTRIBUTION_ONLY` and `verdict_transfer: NONE`. It is **inside** the ladder, needs no
  Orchestrator, and is not on `main` or on `mirror`, which is why a `main`-scoped census does not
  see it. It does **not** open a review and issues no verdict, so it does not defeat the record's
  `INF` that D5's default is unreachable — but it is evidence for `OPS-DEC-03`'s option set that
  § 2.5 does not carry.

**Correction.** `REHEARSAL` correctly stands down the *governed verdict*. It does not decide the
*review posture*, and the record's conditionality decides it silently. Under either branch of
`OPS-DEC-02` the question *"is anything reviewed, by whom, labelled how"* remains open, which is
the opposite of a decision the switch resolves.

---

## `M-10` `Φ−1a`'s scope is undetermined by the command that defines the corpus

`OBS` NEXT OPERATOR ACTION item 1: *"Copy the untracked planning records out of the repository,
byte for byte — now 12 files."* The 12 is the output of `git status --porcelain | grep '^??'`,
which by construction **excludes every ignored path**. Measured at the same tree (C-10): **9**
further paths exist on disk, are in no ref, and never appear in that output — 7
page-adjudication crops and `deployment/local_instance.md`, ignored by the repository's own
`.gitignore`, plus `.claude/settings.local.json`, ignored by the operator's global one
(`git check-ignore -q` fires on 9 of the 21). The repository's own `.gitignore`
says of the crops: *"A crop of a printed page reproduces the author's characters — **which is
exactly what makes it evidence**."*

`INF` Whether those belong in the preservation act is a real question with a real answer either
way, and the record's *"needs no decision at all"* is true of the **copy** and not of the
**corpus**. A byte copy scoped by `??` preserves **12 of the 21** untracked-on-disk paths and reports
itself complete. **Falsifier:** if the operator holds that ignored paths are by definition
outside any preservation obligation, the scope is settled by the `.gitignore` and no decision
remains; the record does not say this, and nothing else does either.

---

## `M-11` The destructibility hazard is larger than the record's own framing

`OBS` Re-derived per object: for each of the 11 untracked records under `learning/`,
`git hash-object <disk file>` then `git cat-file -e <result>` →
**8 have no git object for their current bytes**, 3 do. The 8 include
`LEGEND_OPERATIONAL_READINESS_PLAN_FINAL_v1.md`, both trial designs, the feasibility review, the
Mirror review, the TRIAL-002 register, and `LEGEND_MINIMUM_DECISION_PATH_v1.md` itself.

⚠️ **Method stated because it changes the number.** This predicate is *"the current bytes are
unrecoverable from the object database"*. It is stricter than *"this record has never had an
object"*, and it is the predicate the destructibility argument needs. Readiness `M-1` reported
*"4 have no git object at all"* over a 10-record corpus; that figure is not re-derived here and
the two are not compared — a record whose blob was written and then edited satisfies one
predicate and not the other. What is asserted is only the measured one, with its command.

---

# OPEN

**`O-1` · Does `OPS-DEC-01 = (a)` have an edge to `OPS-DEC-02`?**
`I.2` step 7: *"ogni attore legge `/roles/<suo>.md`, si reidrata, si **REGISTRA** (`ACTOR_ID` +
`SESSION_REF` + **capabilities dichiarate**)"*. The declared capabilities are drawn from a
contract that reads `status: PROPOSED`, and `DEC-20260822` consequence 2 forbids tracing an
exercised authority to one. If registration is a runtime act whose content is declarative — the
actor states what it can do, the source immaterial — there is no edge and the record's two roots
are independent. If the declared capabilities must be traceable to a binding contract, then
`OPS-DEC-01 = (a)` cannot complete before `OPS-DEC-02` resolves, and the two roots become an
**ordered pair**. The record's map asserts the first reading without stating that it is a
reading. Not adjudicated here.

**`O-2` · Is `OPS-DEC-05` parallel, or is it a precondition the record classes as parallel?**
Its own WHY OPERATOR asks *"whether the laboratory may run while a compensating protocol named in
`J.0` has zero instances — a governance question about the guarantee table itself."* That is the
grammar of a precondition. The `CLASS` line then reads `PARALLEL — a defined default exists;
gates nothing in the first run`. `J.0`'s row is measured and confirmed (C-8); whether it is
descriptive — a table of what the system does not guarantee — or constitutive is the question,
and the record answers it implicitly in the `CLASS` line while raising it explicitly two
paragraphs below.

**`O-3` · `PREP-5` is still unrun, and § 5's reduction still rests on it.**
Confirmed as the record states. Nothing in this review changes that: which clauses of the trial
design require a governed artifact has not been measured, and if the answer is *"several"* the
rehearsal branch closes. Note the interaction with `M-1`: `PREP-5` returning *"several"* raises
the set from three to four, not from two to four.

**`O-4` · `PREP-4` is not a formality — the population has moved.**
The record carries 39/39, 25/30, ~29/36 `AS REPORTED`, measured at `main@788c357` against 37
refs. Re-derived here: **57 refs**, and **47 `REV-*` records** under `reviews/mirror` across
their union (C-12). The structural claim survives; the denominators do not, and the census the
record wants is a census over a set that has grown by at least 8 verdict records and 20 refs.

**`O-5` · `XPORT`'s base has already moved 16 commits.**
`OBS` `BASE_HEAD 4454feab` (2026-08-19) is an ancestor of `main`'s tip `788c357` (2026-08-22),
with `git rev-list --count 4454feab..main` → **16**. `OPS-DEC-04`'s consequence (a) states *"`J.3`
requires a durable queue object citing the exact hash and base"*. Whether a base 16 commits
behind the tip is still the base a queue object may cite, or whether the candidate must be
re-derived first, is not raised in the record and is not answered anywhere I measured. It is a
question `OPS-DEC-04` inherits under every one of its four outcomes.

**`O-6` · `C.3`'s rotation clause under a single reviewer.**
`C.3` requires `rotazione` (body § 325: *"rotazione (mai coppie fisse)"*). With one reviewer the
clause is unsatisfiable, which would be a second measured ground under `OPS-DEC-03` beside
`CP-3`'s three. Counter-evidence, stated because it defeats the reading: `C.4` routes
`SYSTEM → Mirror` in the singular, which suggests rotation binds peer-Scientist review and not
system review. Not adjudicated here; it changes whether `OPS-DEC-03` is a preference or a
compliance question.

**`O-7` · The actual gate on `OPS-DEC-04` is not among the five surfaces.**
The record makes `OPS-DEC-04` blocking on `02 = GOVERNED` **and** *"the run routing authoritative
payload between sessions"*. The second conjunct is a property of the trial's design — decided by
whoever specifies the run, in design v2 or the execution protocol — not by any of `D1…D5`.
`PREP-5` is scoped to *"which parts require a governed artifact"*, which is a different question
from *"does the run route authoritative payload cross-session"*. Under the record's own
architecture, a fact nobody has been asked to determine decides whether a decision fires.

**`O-8` · The corpus this review belongs to has no preservation act.**
This file is untracked in the `evidence-index` worktree on branch
`plan-orchsurf-r4-transcription`. `Φ−1a` as written enumerates the ROOT CHECKOUT. Whether the
preservation obligation follows the *records* or the *checkout* is undetermined, and at least one
worktree now holds a planning record that no named act reaches.

---

# MINIMUM DECISION SET

## The criterion, applied consistently

The record's criterion, quoted: *"A decision is on the minimum path **iff no defined default
state lets operational execution proceed with durable output**."* Applied to six surfaces rather
than five — the record's own five, plus the one `M-1` restores:

| Surface | Default state | Execution proceeds with durable output? | On the path? |
|---|---|---|---|
| **`D-1` · corpus disposition** (readiness, blocking) | **none** — the corpus is untracked, 2 records carry 5 `BLOCK` `PRIVATE_NAME` findings, 8 have no object for their current bytes | ❌ committing without the redaction writes identifiers into the public edition; not committing writes nothing | ✅ **yes — omitted by the record** |
| D2 · actor (`OPS-DEC-01`) | none — no session in this cycle may `WORK_COMMIT` | ❌ nothing durable is written | ✅ yes |
| D1 · activation (`OPS-DEC-02`) | explicit — contracts stay `PROPOSED` | ✅ for a run that cites no contract | ⚠️ via the switch |
| D3 · XPORT (`OPS-DEC-04`) | undeclared — binds nobody | ✅ unless the run treats a dispatch as evidence | ⚠️ via the switch **and** `O-7` |
| D5 · independence (`OPS-DEC-03`) | *unreachable* for a new governed review | ❌ if any governed review is declared; **and see `M-9`** | ⚠️ via the switch |
| D4 · ledger (`OPS-DEC-05`) | explicit — absent, and known to be | ✅ the run produces no event either way | ❌ no — but see `O-2` |

`INF` **Under the record's own criterion the minimum viable set is three, not two:
`{ D-1, OPS-DEC-01, OPS-DEC-02 }`** — and the omitted member is the one that is *upstream* of the
member the record calls unavoidable (`D-6 → D-1`, in the source's own dependency column).
It becomes four if `PREP-5` returns *"several"* (`O-3`), and the record's § 8 risk 1 already
carries that.

## The corrected dependency map

```
   ┌──────────────────────────────────────────────────────────┐
   │  D-1 · corpus disposition            (readiness, BLOCKING)│  UPSTREAM ROOT
   │  copy · redact 2 · preserve pre-redaction bytes · commit  │  — absent from the record
   └───┬──────────────────────────────────────────────────────┘
       │  Φ−1a (copy)  ── needs no authority, no decision, no git act   ✅ record is right
       │  the other three acts ── each needs a decision the record does not carry
       ▼
   ┌──────────────────────────────────────────────────────────┐
   │  OPS-DEC-01 · authority route  (≈ readiness D-6, widened) │  UNAVOIDABLE
   └───┬───────────────────────────────────┬──────────────────┘
       │ registered actors                 │ operator executes
       ▼                                   ▼
  I.2 §7 registration ── (O-1) reads a    no lease ⇒ C.3 has no opener,
     PROPOSED contract; edge to             G.2 no chooser ⇒ OPS-DEC-03
     OPS-DEC-02 unresolved                  answered by the operator directly
  I.2 §8 L2 smoke  ⇒ the C-9 hold must be SCOPED or LIFTED
     └─ scope-vs-lift is readiness D-5 (b)/(c), carried here as a
        consequence and nowhere as an option set                      ← M-4

   ┌──────────────────────────────────────────────────────────┐
   │  OPS-DEC-02 · run class        (≈ readiness D-5, re-cut)  │  THE SWITCH
   └───┬───────────────────────────────────┬──────────────────┘
       │ GOVERNED                          │ REHEARSAL
       ▼                                   ▼
  D1 fires: activation act must     D1 stands down ✅
     discharge the roles/mirror.md  D3 stands down — but it was already
     branch (CP-3, three barriers)     non-binding by its own status line;
  D3 fires ONLY IF the run routes      the switch adds nothing here
     authoritative payload         D5 does NOT stand down — it is
     cross-session ── O-7: nobody      SILENTLY SET TO (d), foreclosing
     has been asked to determine       option (b), the one outcome needing
     this                              no governance at all              ← M-9
  D5 fires at the declared floor

  PARALLEL, no edge to the above:
     OPS-DEC-04 (XPORT)  ─ O-5: its BASE_HEAD is 16 commits behind main's tip
     OPS-DEC-05 (ledger) ─ O-2: classed PARALLEL, argued as a precondition
                            residue: cadence N stays UNASSIGNED (ESC-3) either way ✅
```

## What each decision unblocks, and what stays blocked

| Decision | Unblocks | Stays blocked regardless |
|---|---|---|
| `D-1` (omitted) | the redaction, the pre-redaction byte preservation, and therefore `Φ−1c`'s three EXIT criteria | nothing else — but nothing durable is safe to write until it resolves |
| `OPS-DEC-01` | `IMP-1` `WORK_COMMIT` · `IMP-4` lease + registration · `IMP-5` L2 smoke | `IMP-5` additionally by the C-9 hold; `Φ−1a` was never blocked |
| `OPS-DEC-02` | whether D1/D3/D5 are live questions; whether `CAND-20260818-SCIENTIST-AB-SPEC` becomes a precondition | the three `MAJOR`s `DEC-20260822` left open; the trial's scientific content |
| `OPS-DEC-03` | the run's review posture — **under either branch**, per `M-9` | `C.1`'s ladder, `C.2`'s format, cadence `N` |
| `OPS-DEC-04` | the dispatch discipline's status | `O-5`'s base question; the identical, unasked question for `scientist_reading_modes.md` and `controlled_benchmark_ab.md` |
| `OPS-DEC-05` | `IMP-6` | `G.3`'s retrospective — cadence `N` is `UNASSIGNED` **and** `CP-2(c)`'s challenge population is zero, so it stays unschedulable with the ledger built ✅ the record states this correctly |

## The switch, tested

`INF` The record's central claim — *"Three of the five resolve **by declaration** rather than by
construction, and the same declaration resolves all three"* — holds for **one** of the three
cleanly, and partially for the others:

- **D1 · activation — holds.** `REHEARSAL` leaves the contracts `PROPOSED` and the authority
  traced to the annexes, which is exactly `DEC-20260822` consequence 2. Confirmed.
- **D3 · XPORT — the switch adds little.** XPORT binds nobody today and binds nobody under
  `GOVERNED` either, until the operator approves; the run class does not move its status. The
  real gate is `O-7`, which is not a surface and not a decision anyone has been assigned.
- **D5 · independence — does not stand down; it is pre-decided.** `M-9`.

`INF` So the reduction's *mechanism* is sound — a single declaration does collapse several
questions — and its *reach* is overstated by one surface and understated in cost by one omitted
prerequisite. The framing the record itself nominates as the thing to attack (§ 8 item 4,
*"calling `OPS-DEC-02` a switch rather than a surface is the framing to attack"*) survives this
review. What does not survive is the claim that the resulting set is **two**.

## What this review does not do

It creates no `DEC`. It selects no outcome in any of the five enumerated option sets, nor in
readiness `D-1`'s four. It proposes no code, no schema, no normative file and no repository
change. It does not decide whether the redaction happens, how, or by whom — only that the
question exists, is blocking by the criterion the record supplies, and is absent from the
reduction. It activates nothing, opens no review, appends to no queue, and changes no `status:`
line. It resolves none of the eight `OPEN` items above.

---

## Verification trail

All commands run from
`<repo-root>/.claude/worktrees/evidence-index` unless a ROOT CHECKOUT
path is shown. `${r}` braces are mandatory — see C-2.

| # | Check | Command | Result |
|---|---|---|---|
| 1 | Measurement plane | `git rev-parse HEAD` · `git merge-base --is-ancestor 30cb4f3 HEAD` | `e4aa80c` · **false** — the record's `HEAD` is not reachable here |
| 2 | Refs | `git for-each-ref \| wc -l` | 57 |
| 3 | Lease | `python3 framework/scripts/lease_state.py` | `ACTIVE by derivation: 0`; 5 leases |
| 4 | Tracked denominator | `git ls-tree -r --name-only main \| wc -l` | 580 (581 at `30cb4f3`) |
| 5 | `PROPOSED` population | `git grep -n "^status: PROPOSED" main`, each hit compared to its own frontmatter end | 16 hits · **12 frontmatter** · 4 quotations in 3 files |
| 6 | Exact-clause population | `git grep -n "^status: PROPOSED — binding once Mirror hostile review passes and the operator approves" main` | **9 hits · 7 frontmatter** ← `M-2` |
| 7 | C-9 reconciliation | `git grep …` at `1aeca4f` (last `main` commit dated 2026-08-17) | **8 frontmatter**; − `claude_md_migration_map` (own C-9 row) = **7** ← `M-3` |
| 8 | Creation dates | `git log main --reverse --diff-filter=A --date=short -- <each of the 12>` | 8 on 08-16; 4 on 08-18/08-19 ← `M-3` |
| 9 | Event ledger | per-ref `git ls-tree -r --name-only "${r}" -- ledger/events` | **0 of 57** |
| 10 | — positive control | same sweep, `ledger/approvals` | **34 of 57** |
| 11 | Agent Card registry | same sweep, path match `agent.card` | 1 ref (`orchestrator`); 23 `UNVERIFIED`, 21 `last_verified: NONE` |
| 12 | XPORT protocol, swept | per-ref `git cat-file -e "${r}:framework/protocols/cross_session_transport.md"` | **21 of 57 refs** ← `M-8` |
| 13 | XPORT candidate | same, `governance/candidates/CAND-20260819-XPORT.md` | **17 of 44 branch refs**; present on `main` |
| 14 | XPORT base drift | `git merge-base --is-ancestor 4454feab main` · `git rev-list --count 4454feab..main` | ancestor · **16 commits** ← `O-5` |
| 15 | XPORT verdict | `git show mirror:reviews/mirror/REV-XPORT-MIRROR-002.md` | `verdict: ACCEPT`, 4 non-blocking |
| 16 | Approval queue | `git show main:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` | 6 lines · `XPORT` 0 · `SCIAB\|SCIENTIST-AB` 0 · control `GOV311` 5 · `APR-20260816-GOV311-001` `REQUESTED_BY: plan` |
| 17 | Review corpus | union of `reviews/**.md` over 57 refs | 82 files · mirror 60 (**47 `REV-*`**) · orchestrator 15 (OPEN/CLOSE) · plan 7 (AUTHOR-RESPONSE + 1 non-author contribution) ← `C-12`, `O-4` |
| 18 | Untracked, repo-wide | ROOT CHECKOUT disk vs `git ls-tree -r --name-only 30cb4f3`, `.gitignore` roots excluded; then `git check-ignore -v` on each residual | 21 on disk · **9 ignored** (`git check-ignore -q`) · **12 visible as `??`** = 11 `learning/` + 1 root audit ← `C-10`, `M-10` |
| 19 | Object recoverability | per record: `git hash-object <disk file>` → `git cat-file -e <sha>` | **8 of 11** `learning/` records: no object for current bytes ← `M-11` |
| 20 | Privacy scan | stage the 12 into a scratch dir, `python3 scripts/independent_privacy_scan.py --json <dir>` | exit **2** · **5 `BLOCK` / `PRIVATE_NAME` in 2 files** ← `M-1` |
| 21 | Redaction vocabulary | `grep -c` on the reviewed record for `redact`, `identifier`, `privacy`, `PRIVATE_NAME` | **0, 0, 0, 0** ← `M-1` |
| 22 | `D-6 → D-1` | `LEGEND_OPERATIONAL_READINESS_PLAN_FINAL_v1.md` § 4.1, `Depends on` column | `D-6` depends on `D-1` ← `M-1`, `M-5` |
| 23 | `Φ−1c` composition | same record, § 10 operating order | `redact 2 records · preserve design v1's pre-redaction bytes FIRST (M-7) · commit`, 3 EXIT criteria ← `M-1` |
| 24 | `C.3` verbatim | `git show main:governance/annex_c_review_protocol.md \| sed -n '50p'` | `Apertura solo via Orchestrator; rotazione; …; semi-blind = independence by task framing, not by information barrier` ← `M-6`, `M-9`, `O-6` |
| 25 | `RATIONALE 6` vs `E-6` | `git grep -n "convenient interpretation" main -- governance/decisions/` | line **151** = § E-6, quoting `REV-ROLES-MIRROR-001`; `RATIONALE` begins at line 222 ← `M-6` |
| 26 | `I.2` steps | `git show main:governance/annex_i_bootstrap_deployment.md` § I.2 | promotion to `ACTIVE_ORCHESTRATOR` is step **10** ← `M-7` |
| 27 | `P5.1` roots | `git show main:governance/plan_defined_parameters.md` § P5.1 | `governance/candidates/`, `ledger/`, `reviews/` — `learning/` is CONTENT ← `C-9` |
| 28 | Record is untracked | `git log --all --oneline -- learning/orchestrator/LEGEND_MINIMUM_DECISION_PATH_v1.md` | no output, on all 57 refs |

⚠️ **Row 21 falsifies itself once committed.** This review now contains the words it reports as
absent from the reviewed record. Reproduce it against
`learning/orchestrator/LEGEND_MINIMUM_DECISION_PATH_v1.md` only — never repository-wide.
