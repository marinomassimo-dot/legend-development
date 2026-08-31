---
artifact: SCIENTIST A/B ACTIVATION READINESS — measured at the worktrees the design names
record_id: SCIENTIST-ACTIVATION-READINESS-001
task_id: SCIENTIST_ACTIVATION_READINESS_v1
author: plan
authored_on: 2026-08-22
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)

STATUS: READ_ONLY_ANALYSIS · READINESS ASSESSMENT
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - READINESS ASSESSMENT
  - NOT ACTIVATION
  - NOT A PAPER ASSIGNMENT
  - NOT AN ACTOR CREATION
  - NOT GOVERNANCE
  - NOT A PROTOCOL
  - NOT A DECISION
  - NOT EXECUTION AUTHORIZATION

naming_note: >
  Not a Session Learning Record (Annex E.6) and not a handoff. Named as the dispatch named it,
  and takes no `SLR` number it has not earned — the precedent of the six non-SLR records already
  in this seat.

domain: >
  CONTENT — verified this session. `governance/plan_defined_parameters.md` § P5.1 declares
  `CONTROL_PLANE_ROOTS` exhaustively as `governance/candidates/`, `ledger/`, `reviews/`.
  `learning/` is under none of them, so this file sits inside the `CANDIDATE_CONTENT_HASH` of any
  future candidate spanning this branch and moves it. Disclosed.

relation_to_prior_work: >
  Five records on this branch hold adjacent ground — `SCIENTIST-PIPELINE-READINESS-001`,
  `SCIENTIST-PIPELINE-EXECUTION-MODEL-001`, `SCIENTIST-BOOTSTRAP-CONTRACT-ANALYSIS-001`,
  `SCIENTIST_RUNTIME_PROFILE-001` and `SCIENTIST-FIRST-REAL-PAPER-PILOT-001`. This record does
  not restate their designs. It asks the one question none of them was asked: **if the operator
  opened two Scientist windows this afternoon, what would actually happen?** That question is
  answered by measuring the *runtime surfaces* — the two worktrees, their contracts, their
  fingerprints, their capability records — rather than the designs written about them. Three
  prior claims came back different, and one binding operator determination postdates four of the
  five records. Every fact reused was re-run here first.

verdict_transfer: >
  NONE. Every measurement below was executed in this session, at the HEAD named in § 1, by the
  command shown beside it. Where a prior record's number is contradicted, both numbers are given.
---

# SCIENTIST A/B ACTIVATION READINESS — 001

> **The four findings that decide this assessment.**
>
> **1 · 🔴 An operator determination dated today already answers half the question, and this
> branch cannot see it.** `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`
> — on `main` at `2bb2700`, **absent from this branch** — selects `OPTION B ·
> ACTIVATION_NOT_CONFIRMED`: the four role contracts, `roles/scientist.md` among them, **remain
> `PROPOSED` and are non-binding documents**, and *"a new, explicit activation act is required
> before any actor relies on these contracts as binding."* That is not a pending approval. It is
> a closed determination that activation has not occurred. **There is no binding Scientist role
> contract to activate a Scientist under.**
>
> **2 · 🔴 The two worktrees the design names for Scientist A and B are not behind — they predate
> the laboratory.** `lettore` is **201** commits behind `main`, `lettore-b` **203**, both **0
> ahead**. Neither contains `governance/`, `roles/`, `roles/scientist.md`,
> `scientist_reading_modes.md` or `BENCH-AB-001`. A session opened in either one **cannot compose
> its own governance fingerprint** — `governance/scripts/governance_fingerprint.py` is not on the
> ref — **cannot read its own contract**, and cannot reach the instrument it would be asked to
> run. This corrects `REV-ROLES-MIRROR-001` MINOR-3, which records all three Scientist worktrees
> as carrying the *superseded* contract blob: measured today, only `lettore-c` does. A and B
> carry **none**.
>
> **3 · 🔴 Both A and B worktrees hold the same uncommitted bytes, and the conflict that named it
> has been open for five days.** Blob `86bba8b` — a two-line receipt-id bump in
> `PMID42422765.json` — is present, byte-identical, in both working trees.
> `HANDOFF-C-2-PMID42422765` (2026-08-17) records it as `CONTENT RESOLVED · FORWARD OWNERSHIP
> UNRESOLVED`. `BOOTSTRAP.md` forbids proceeding past any point that could lose uncommitted work.
> **The sync is therefore not a fast-forward; it is gated on an ownership decision nobody holds** —
> and an identical two-line delta appearing independently in three working directories is itself
> the isolation signal, not a housekeeping item.
>
> **4 · The instrument layer is the healthiest thing here, and it is not what is blocking.** LINT
> `PASS`, receipts `128 chained, tail anchored`, growth anchors `PASS`, four fingerprints compose,
> the 79 KB builder and 90 KB manifest validator are present, the population is fixed at 65 units
> / 109 panels, and 17 commit candidates exist as precedent. **Not one item on the RED list in
> § 7 is technical.**

---

## TASK_STATUS

```
TASK_ID          SCIENTIST_ACTIVATION_READINESS_v1
MODE             READINESS ASSESSMENT · no actor created, contacted, opened or registered ·
                 no paper selected · no contract issued · no lease taken · no file outside
                 learning/plan/ written
STATE            COMPLETE — the six study areas and the final question are answered. Every
                 answer that could be measured was measured; every answer that is a judgement
                 is marked as one, with the party who owns the decision.

EXECUTED         31 measurements at this HEAD: git identity · worktree survey over 5 actor
                 worktrees (HEAD, ahead/behind, dirt, per-path presence) · lease derivation ·
                 fingerprint composition in 4 locations · fingerprint input set · approval-queue
                 parse · all-refs existence sweeps (3, each with a positive control) ·
                 blob-identity comparison of roles/scientist.md across 54 refs · agent-card
                 registry and L2 outcomes read from refs/heads/orchestrator · capability-row
                 count · task-ledger enumeration · LINT · receipts verify · growth anchors ·
                 surface census REGENERATED against the shared corpus and diffed against the
                 committed one · independent XML body/abstract measurement on 8 candidate
                 surfaces · pool derivation with reconciliation of 15 unmatched rows ·
                 MODE_A/MODE_B/C.1/C.4/H.1/§26/§27/§28/§32/G.1 read in place
NOT EXECUTED     no Scientist opened, spawned, contacted, assigned or registered · no paper
                 opened, read or selected · no surface built or frozen · no candidate opened ·
                 no lease taken · no Task Contract issued · no path under governance/ roles/
                 framework/ ledger/ runtime/ disease-models/ modified · no worktree synced,
                 cleaned or deleted · no dirty file touched in any worktree
FILES ADDED      exactly one — this file
```

---

## IDENTITY

### 1 · From repository evidence; not from `roles/scientist.md` or `roles/plan.md`, neither of which is binding — and § 2.1 is why that phrase is now a measurement rather than a caution

| Field | Measured value | Command |
|---|---|---|
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `b72af2f25d42c3cafb781d42b66ef3a1761cdb66` | `git rev-parse HEAD` |
| worktree | `.claude/worktrees/evidence-index` | `git rev-parse --show-toplevel` |
| vs `main` (`788c357d…`) | **2 behind · 41 ahead** | `git rev-list --left-right --count main...HEAD` |
| working tree | one untracked file (the previous record) | `git status --porcelain` |
| lease | **`ACTIVE by derivation: 0`** — 5 leases, 2 STALE, 3 RELEASED | `python3 framework/scripts/lease_state.py` |
| scientist fingerprint, here | `b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a` | `governance_fingerprint.py compose --role scientist` |
| scientist fingerprint, `main` | **identical** — `b66959cd…` | same, run in the root checkout |

`CLAUDE.md` § 0: no ACTIVE lease and no runtime inventory ⇒ `BOOTSTRAP_MODE`. This session is not
Orchestrator, issues nothing and creates no actor. The single act it performs — one file under
`learning/plan/` on its own branch — traces to **H.1 `WORK_COMMIT`**, an annex, not a role
contract. After § 2.1 that distinction stops being a formality: the role contract this session
would otherwise cite has been determined non-binding.

### 1.1 · 🔴 The two commits this branch lacks are the two that govern the dispatch

```
2bb2700  The review that passed verified the object had not moved, and never read what it says
         → governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md
788c357  The pipeline is prepared where it can be read, and the authority to run it was not assumed
         → learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md
```

`git diff --name-only HEAD...main` returns exactly those two paths. **The branch that is asked
whether the Scientists can be activated is missing the binding determination on whether their
contract is in force, and the Orchestrator's own pipeline-preparation record.** Both were read
here via `git show main:…` — which is the remedy, and it is a remedy only because someone thought
to look. Recorded as a routing defect in § 6.3, not as a footnote.

---

## 2 · CURRENT SCIENTIST INFRASTRUCTURE

### 2.1 · Contracts — 🔴 `BLOCKED`, and the block is closed rather than pending

| Object | Measured state | Where |
|---|---|---|
| `roles/scientist.md` | `status: PROPOSED — binding once Mirror hostile review passes and the operator approves` | line 12, identical on `main` and here |
| activation determination | 🔴 **`OPTION B · ACTIVATION_NOT_CONFIRMED`** | `DEC-20260822-…`, `main` `2bb2700`, operator, H.1 |
| first hostile review of the contract | 🔴 **`CHANGES_REQUIRED` · C.2 verdict `WEAKENED`** (MAJOR-3) | `REV-ROLES-MIRROR-001`, `refs/heads/mirror` `1350477` |
| `AUTHOR_RESPONSE` to that review | **required and outstanding** (Annex C.2 — silence is not acceptance) | ibid. |
| `scientist_reading_modes.md` | `PROPOSED — … Until then it binds nobody.` | line 8, `main` and here |
| `controlled_benchmark_ab.md` | `PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC` | line 8 |
| `CAND-20260818-SCIENTIST-AB-SPEC` | **revision 6**, `state: READY FOR MIRROR REVIEW … no approval requested, granted or implied`; five prior revisions all `REQUEST CHANGES` | manifest frontmatter |
| approval queue | **6 lines · 2 approvals · both `CAND-20260816-GOV311`** — nothing names the Scientist spec | `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`, parsed |

🔴 **MAJOR-3, re-measured here rather than transferred.** `roles/scientist.md` asserts that
`scientist_reading_modes.md` *"binds every actor under this contract"*; that protocol's own
frontmatter says *"Until then it binds nobody."* Both sentences are on `main` today. Downstream:
the same contract fixes `scientist-a` and `scientist-b` *"FIXED on canonical execution of
CAND-20260818-SCIENTIST-AB-SPEC"* — **actor identity fixed by a document that declares itself
binding on nobody**, cited from a contract an operator determination holds non-binding.

**The consequence for activation is not a matter of degree.** Consequence 2 of the determination:
*"No actor authority may be assumed from these contracts. Any authority an actor exercises must be
traced to the governance body or to a named annex … never to a role contract clause standing
alone."* A Scientist opened today would have **no contract to read at registration**, and Annex
I.2 step 7 — *each actor reads its own contract* — has no object.

> **Prior-record divergence, stated because it changes the root cause.**
> `SCIENTIST-FIRST-REAL-PAPER-PILOT-001` § 8 records `B-1` (the missing approval line) as *"still
> the root."* Measured here, the approval line is now the **second** obstacle. The first is a
> closed operator determination that the contracts are non-binding and that a new activation act,
> **whose form is deliberately unspecified**, is required. Approving `CAND-20260818-SCIENTIST-AB-SPEC`
> would not by itself discharge it — the determination's own reasoning is that an approval bound
> to a content hash cannot nullify the meaning of a `status:` line inside that hash.

### 2.2 · 🔴 Worktrees — `BLOCKED`, and the measurement is qualitative, not a commit count

`git -C <wt> rev-list --left-right --count main...HEAD`, plus per-path presence on each ref.

| Worktree | ACTOR_ID | HEAD | behind · ahead | `governance/` | `roles/scientist.md` | reading modes | `BENCH-AB-001` | dirty |
|---|---|---|---:|---|---|---|---|---|
| `lettore` | *proposed* `scientist-a` | `9b0cf47` | **201 · 0** | 🔴 **ABSENT** | 🔴 **ABSENT** | ABSENT | ABSENT | **1 path** |
| `lettore-b` | *proposed* `scientist-b` | `cb50e17` | **203 · 0** | 🔴 **ABSENT** | 🔴 **ABSENT** | ABSENT | ABSENT | **1 path** |
| `lettore-c` | `scientist-c` | `908197b` | 65 · 0 | PRESENT | `e93281159c06…` (superseded) | ABSENT | ABSENT | clean |
| `mirror` | `mirror` | `da52ee5` | 65 · 77 | PRESENT | superseded | ABSENT | ABSENT | 1 path |
| `orchestrator` | `orchestrator` | `1e2fabd` | 37 · 42 | PRESENT | superseded | ABSENT | ABSENT | clean |

**Three consequences, each mechanical.**

**(a) A and B cannot bootstrap themselves.** The registration step every actor performs requires
reading `roles/<own>.md` and composing `APPLICABLE_GOVERNANCE_FINGERPRINT`. In `lettore` and
`lettore-b` the contract file does not exist on the ref and
`governance/scripts/governance_fingerprint.py` does not either — run there, `python3` returns
`No such file or directory`. Not "reads a stale contract." **Reads nothing.**

**(b) No worktree in the repository holds the instrument.** `BENCH-AB-001` and
`scientist_reading_modes.md` are `ABSENT` on all five actor refs, including Orchestrator's and
Mirror's. They exist on `main` and on this branch. Whatever the first run is, **every participant
syncs first, and the sync is a precondition of the design, not of the schedule.**

**(c) The dates say the drift is not converging.** `lettore`'s last commit is 2026-08-14, and its
distance from `main` is **201** where the same figure was recorded as 136 four days ago. Nothing
has been syncing these worktrees; they are drifting at roughly the rate `main` advances.

### 2.3 · 🔴 The dirty state — and why it is a stop condition rather than a chore

```
committed base   lettore     5888cf44be5dc7bf47b6ed3774c1450b1c65bf1f
committed base   lettore-b   5888cf44be5dc7bf47b6ed3774c1450b1c65bf1f    ← same base
working blob     lettore     86bba8bb441d7f626768607ed8144c4bcfaec884
working blob     lettore-b   86bba8bb441d7f626768607ed8144c4bcfaec884    ← byte-identical
delta            "receipt": "FTR-20260810-42422765-04"  →  "-05", twice, 397-line file
```

`runtime/handoff/C-2/HANDOFF-C-2-PMID42422765.md` (`refs/heads/orchestrator`, 2026-08-17) records
this as `status: CONTENT RESOLVED · FORWARD OWNERSHIP UNRESOLVED — escalated`, notes a third copy
of the same blob in `stash@{0}`, and marks the root cause `IPOTESI`: *"An identical two-line edit
appearing independently in three working directories is better explained by a tool than by three
people."* **Five days on, forward ownership is still unresolved and both trees are still dirty.**

`BOOTSTRAP.md`, *What must never happen during bootstrap*: *"Never proceed past a point that could
lose uncommitted work … or that holds unintegrated content."* Both A and B worktrees are exactly
that. The sync in § 2.2 is therefore **not** `git merge --ff-only`; it is an ownership decision
first and a git operation second, and the actor who can take it holds a lease that does not exist.

🔴 **And the finding underneath the housekeeping.** Two worktrees whose entire purpose is
independent parallel reading contain the *same bytes*, written by something that reached both.
Whatever wrote them crossed the isolation boundary the pilot design treats as structural. The
hypothesis is testable and untested, and **it should be tested before independence is claimed of
these two directories**, not after.

### 2.4 · Fingerprints — 🔴 `NOT_READY`; three recorded values, none of them current

| Value | Where it is recorded | Composes to it today? |
|---|---|---|
| `ce3c0d94b407bbd1e3d1e33e628b7cffdc2a0fed9c3cb93bd26e7a900a665d04` | `runtime/agent_card_registry.md`, against **all three** Scientist cards | only inside `lettore-c` |
| `82423a48b700bc2b392b4c8e944eb6a0b07cefebddf63db00e96716cbed43e79` | `CHK-plan-0017`, *"recomputed at source in this worktree, 12 inputs listed"* | **nowhere measured today** |
| `b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a` | nowhere | `main` **and** this branch |

The 12-input pertinence set is parsed from § P2.2 and includes `roles/scientist.md`, so every
edit to the contract rotates the value. **It has rotated at least twice since the registry was
written, and the registry has not been updated once.** `lettore-c` composing `ce3c0d94…` is not
reassurance: it means C's environment is 65 commits stale, and it is the only place the registry
is still true.

Under A.6 a checkpoint written under a superseded fingerprint is `INCOMPATIBLE` and must not be
resumed. **There are no Scientist checkpoints, so nothing is currently broken by this** — and that
is precisely the window in which it is cheap to fix. It stops being cheap the moment a reading is
in flight.

🔴 **The sequencing hazard, re-measured and unchanged.** Canonical execution of
`CAND-20260818-SCIENTIST-AB-SPEC` edits `roles/scientist.md` and **rotates the scientist
fingerprint again**. A reading started before that execution would be resumable only under a
fingerprint it was not written under. The rotation is confined to the scientist set — `mirror` and
`plan` compose identically on `main` and here; `orchestrator` does not, and that is this branch's
own doing.

### 2.5 · Capabilities — `NOT_READY`, and a prior number is wrong in the system's favour

> **Correction, carried because it changes what is owed.** `SCIENTIST_RUNTIME_PROFILE-001` § 14
> and `SCIENTIST-FIRST-REAL-PAPER-PILOT-001` `B-3` both record *"L2 suspended by the C-9 hold;
> **0 of 27** capabilities `VERIFIED`."* Measured: **L2 ran, and its outcomes were ratified by
> operator decision of 2026-08-18.** `runtime/L2-OUTCOMES.md` records **3 VERIFIED of 12
> attempted**. The registry declares **21** capability rows (6 of them shared by three Scientists,
> so 33 per-actor instances) — neither figure is 27.

| Row | Capability | Outcome | Evidence class |
|---|---|---|---|
| `O4` | lease acquire · renew · observe expiry | **VERIFIED** | PRIMARY (orchestrator) |
| `S2` | **scientist worktree confinement** | **VERIFIED** | 🔴 **PRIMARY (scientist-c)** |
| `S4` | **scientist capability per plan** | **VERIFIED** | 🔴 **PRIMARY (scientist-c)** |
| `P1` | registry / structural validation | `CRITERION_MET / NAME_NOT_DELIVERED` | PRIMARY (plan) |
| `M1` · `M2` · `O3` · `M4` · `P2` · `M3` | — | criterion-met-unpromoted, blocked or not verified | mixed |

🔴 **The correction does not help Scientist A and B — it sharpens the deficit.** Under Annex I.4
a capability is verified *per actor*: *"CONFIGURED != PROVEN … Orchestrator assigns on `VERIFIED`
capabilities."* The only two Scientist capabilities ever verified were exercised by **`scientist-c`,
in `lettore-c`**. `scientist-a` and `scientist-b` hold **zero** verified capabilities of six
declared each — including `Worktree confinement` and `Full-text read producing a receipt`, the two
the pilot's independence argument rests on. **Confinement has been demonstrated in the one worktree
that is clean and never in the two that are dirty.**

`PROPOSAL-C9-STATE-MODEL.md` § 15 still reads *"L2 remains suspended"* while the ratified L2 round
is dated 2026-08-18. Two records disagree; both are measured above; **the reconciliation is the
operator's and is not performed here.**

### 2.6 · Required files — the existence sweep, each with a positive control

All-refs `git ls-tree -r --name-only "${r}"` over **54** refs. The `${r}` braces are deliberate:
`"$r:path"` in zsh applies the `:r` history modifier and returns ABSENT on every ref.

| Object | Refs carrying it | Refs *naming* it | Verdict |
|---|---:|---:|---|
| `roles/scientist.md` | **28** | — | ✅ positive control — the sweep works |
| `runtime/agent_card_registry.md` | 🔴 **1** (`orchestrator`) | 20 files | `BLOCKED` — invisible from `main` and from 4 of 5 actor worktrees |
| `runtime/L2-OUTCOMES.md` | 🔴 **1** (`orchestrator`) | — | same |
| `unresolved_disagreements.md` | 🔴 **0 of 54** | 16 refs, incl. `controlled_benchmark_ab.md` § 8.3 | `BLOCKED` — the destination §27 protects has no carrier |
| `ledger/events/` | 🔴 **absent** | G.1 / §29.3 route Mirror's primary analysis through it | `BLOCKED` for Mirror's own method |
| `ledger/tasks/scientist*/` | 🔴 **absent** — `ledger/tasks/` holds `plan/` only | — | **zero Scientist Task Contracts have ever existed** |
| `framework/eval/failure_taxonomy.md` | present, 30 lines | — | ✅ |
| `commit_candidates/` | 17 candidates | — | ✅ the terminus exists and has precedent |

🔴 **`P1` is blocked on a missing instrument, not a missing object.** The registry returned to the
`orchestrator` branch and `P1` still did not verify: measured in `L2-OUTCOMES.md`, **no validator
anywhere reads it** — 0 references across all five validators and 0 across every `*.py` in the
tree, with the search machinery positive-controlled first. *"Reading 314 lines and counting 30 rows
is measurement, not validation."* **Nothing in this repository can tell you the Agent Card registry
is wrong.** It has been wrong about the scientist fingerprint for two rotations, and that is the
demonstration.

### 2.7 · The technical layer — `READY`, and it is the only axis that is

| Check | Result | Command |
|---|---|---|
| structural LINT | **`VERDICT: PASS`** (1 INFO) | `legend_lint.py .` |
| receipt chain | **`OK: 128 chained, tail anchored`** | `fulltext_receipts.py verify` |
| growth anchors | **`PASS`** — claims 39 · papers 70 · corpus 356 · literature 390 | `growth_anchors.py check` |
| fingerprints | 4 roles compose | `governance_fingerprint.py compose --all` |
| surface builder | present, 79 395 bytes | `benchmark_input_surface.py` |
| manifest validator | present, 90 401 bytes | `deepdive_manifest.py` |
| benchmark corpus | 10 files · 592 instruction lines · **65 units / 109 panels** | `evidence_units.json`, parsed |

### 2.8 · The verdict table the dispatch asked for

| # | Axis | Verdict |
|---|---|---|
| I-1 | Scientist role contract | 🔴 **BLOCKED** — determined non-binding today; a new activation act is required and its form is unspecified |
| I-2 | Reading-modes + benchmark protocols | 🔴 **BLOCKED** — `PROPOSED`; *"binds nobody"*; the candidate is at revision 6, unapproved |
| I-3 | Worktrees `lettore` / `lettore-b` | 🔴 **BLOCKED** — 201/203 behind, no governance, no contract, no instrument, both dirty under an unresolved conflict |
| I-4 | Fingerprints | **NOT_READY** — three recorded values, none current; one further rotation is already scheduled by the pending candidate |
| I-5 | Capabilities for A and B | **NOT_READY** — 0 of 6 each; the two Scientist rows that verified belong to `scientist-c` |
| I-6 | Required files (`unresolved_disagreements`, event ledger, task ledger, registry reach) | 🔴 **BLOCKED** on the first; **NOT_READY** on the rest |
| I-7 | Reading modes as *specifications* | ✅ **READY** — MODE_A 74 lines, MODE_B 83, both complete and mutually exclusive by design (§ 4) |
| I-8 | Technical stack | ✅ **READY** — every validator green, both tools present, population fixed |
| I-9 | Corpus / candidate paper | 🔴 **BLOCKED** — § 3.2 |
| I-10 | Lease and Task Contracts | 🔴 **BLOCKED** — 0 ACTIVE leases; 0 Scientist Task Contracts ever issued |

**Two `READY`. Four `NOT_READY`. Six `BLOCKED`.** The two `READY` axes are the two nobody was
worried about.

---

## 3 · THE FIRST REAL PAPER PILOT — MINIMUM VIABLE

`SCIENTIST-FIRST-REAL-PAPER-PILOT-001` designs this experiment in full. **This section does not
redesign it.** It states the *minimum* — the smallest configuration that is still scientifically
valid — and reports what the minimum costs when measured against today's corpus.

### 3.1 · The minimum, with the reason each number cannot go lower

| Parameter | Minimum | Why not less, why not more |
|---|---|---|
| **papers** | 🔴 **one** | Two papers multiply every unresolved variable by two and measure budget instead of method. One paper is also the shape `BENCH-AB-001` fixed its population against, and `commit_candidates/` shows 17 single-paper precedents. `SCIENTIST-PIPELINE-EXECUTION-MODEL-001` § 6.1 already measured that "5 papers" and the governance do not fit |
| **readers** | **two**, MODE A and MODE B, one paper, declared `PARALLEL_READ_GROUP` | Without the group declaration the protocol classifies two contracts on one source as `DUPLICATED_ASSIGNMENT` — *accidental*, a defect, not a design |
| **selection** | **metadata-only screen, screener disqualified from reading** | Anyone who reads the paper to judge whether it qualifies has spent the blindness they were checking for. § 28 permits Plan to run a structural screen that decides nothing about meaning |
| **blindness** | **null-prior over a pinned corpus**, proved by enumeration | The alternative — remove the corpus — is the benchmark's proof, and it is sufficient rather than necessary. A paper with zero LEGEND statements about it cannot be contaminated by them |
| **allowed context** | packet · discipline set · output schema · two-stage protocol · validator; **corpus in stage 2 only** | Everything a reading needs and nothing that anticipates its conclusion |
| **forbidden context** | the other reader's output, identity or progress · the corpus during stage 1 · **any network retrieval, both stages** · a research question · an evidence target · an anticipated conclusion · the evaluation population · the pilot's own scoring design | H.1: *"Conclusione scientifica — Scientist responsabile (soggetta a review, mai a ordine)"* binds the dispatcher too |
| **output** | manifest schema v2 · dossier · claim candidates · receipt · (B) critical reading · stage-2 addendum · **one real `FULLTEXT_READ_RECEIPT`** per reader · terminating at a commit candidate | The run ends at *candidate proposed*. `BATCH_COMMIT` is a separate authorized act under a lease |
| **network** | 🔴 **zero, for both readers** | Plan performs the retraction check before handover, so no mandated step needs it. One pre-step removes a whole contamination class |

### 3.2 · 🔴 What the minimum costs today — the corpus has not moved in seven days

I regenerated the census against the **shared checkout's** corpus rather than reading the committed
photograph:

```bash
python3 framework/scripts/surface_census.py --disease wwox \
  --corpus <repo-root>/files/fulltext --out <scratch> --date 2026-08-22
```

| | committed (2026-08-15) | regenerated (2026-08-22) |
|---|---|---|
| corpus entries · papers | 174 · 87 | **174 · 87 — unchanged** |
| listing digest | `825fc4a9d8415b0e` | **`825fc4a9d8415b0e` — identical** |
| totals block (surface + sentinel) | — | **byte-identical**; `diff` returns only the date line |

**The photograph is still true, and that is the bad news.** Seven days of the laboratory being
blocked produced **zero corpus growth**. The acquisition precondition has not advanced at all.

Derived here, not transferred: 116 census rows · **48** with no receipt · **12** unread with
`structured` + `clean`. (The strict parse matched 101 of 116 rows; all 15 unmatched are
`pdf_only` + `SUSPECT` and fail both gates, so the pool is unaffected — reconciled rather than
rounded.) The same 12 PMIDs come back. Their surfaces, measured by me in the shared checkout:

| PMID | body chars | abstract chars | verdict |
|---|---:|---:|---|
| 42395553 | **0** | 2 065 | 🔴 no `<body>` element at all |
| 38355659 | **258** | 0 | 🔴 empty body — **and it is the correction to `38182577`, which is read** |
| 30470736 | **308** | 0 | 🔴 empty body |
| 27551470 | 9 489 | — | thin; 0 `<fig>` in body |
| 31428585 | 10 645 | — | 0 `<fig>` in body; `Front Oncol` |
| 25238781 | 14 151 (HTML text) | — | short for a primary report |
| 21115974 · 16223882 · 18460020 · 21731849 · 25245215 · 26499798 | 40 k–65 k | — | substantive; oncology by title and journal |

**Three of twelve carry no readable body**, and the census verdict `structured` + `clean` cannot
see it — the exact failure the full-text queue's Appendix 3 predicted. The residue is
predominantly oncology and review: against a criterion requiring primary WWOX-DEE data that is
close to a clean sweep of disqualifications.

🔴 **So the minimum viable pilot has an acquisition step in front of it, and the acquisition has
not started.** `full_text_queue_current.md` holds **72** entries with **11** at `HIGH`; `find-fulltext`
is the existing route. **The first real scientific experiment begins by acquiring the paper it is
about** — and that step is available *today*, requires no lease, no contract and no activation, and
is the single highest-value thing that can be done while everything else is blocked.

---

## 4 · MODE A AND MODE B — NOT IDENTITIES

The dispatch is right to refuse permanent identities, and the repository refuses them
independently. Body § 32: the three Scientists are *"equivalenti … no specializzazioni statiche."*
`scientist_reading_modes.md` § 0 puts the difference in the only place both constraints allow:
**"The difference is a property of the task, not of the actor."** A mode that stops rotating has
become a static specialization, and that is what Mirror's anti-fossilization guard exists to catch.

### 4.1 · The two modes, from the directives as written

```
MODE A · PRIMARY_EVIDENCE_READ       the reader of what the paper shows        (MODE_A.md, 74 lines)
MODE B · INDEPENDENT_CRITICAL_READ   the reader of what the paper does not     (MODE_B.md, 83 lines)
```

🔴 **MODE B is not "MODE A plus criticism", and reading it that way breaks the pilot.** MODE_B
requires *"the whole primary reading — the same completeness, the same outputs, the same
discipline, nothing reduced — **and in addition**"* eleven mandatory critical axes. *"This half is
not abbreviated because you also have a second half. A critical record over a thin reading is
criticism without evidence."* **B is A plus a second full deliverable**, and its budget is the
larger one. Any plan that treats B as the cheaper seat has mis-scoped the run.

Two disciplines specific to each, quoted because they are the operative constraints:

- **A:** *"Report at the level at which the paper states it."* The `Observation` / `Author
  interpretation` seam is *"the single most consequential thing MODE A does, because it is what
  makes the reading attackable."*
- **B:** *"A criticism is a claim and carries the same burden."* And *"Under-reading is a finding
  too … undershoot is the rarer and more dangerous one, because a narrowing nobody challenges
  becomes a permanent false negative."* Every axis with no finding carries `searched; none found`
  **and what was searched** — *"Silence on an axis is an incomplete reading, not a clean paper."*

### 4.2 · What each receives — identical, and how identity is *proved*

| Input | Proof of identity, not assertion of it |
|---|---|
| the paper packet | SHA-256 per file, equal across both surfaces; `verify` enforces parity |
| the pinned corpus | one commit SHA **plus** the `files/` tree digest — `files/` is gitignored and the SHA does not cover the bytes; re-derived at completion |
| the discipline set | `epistemic_discipline` · `gold_is_in_the_details` · `fulltext_read_receipt` · `scientist_reading_modes` · `failure_taxonomy`, byte-identical |
| the output schema | one shape, or there is no comparison |
| the two-stage protocol | both must know stage 1 freezes before stage 2 opens |
| validator + completion gate | `deepdive_manifest.py --verify-artifacts --require-current-schema` → `VERDICT: PASS` as a **precondition**, not a self-report |
| `PARALLEL_READ_GROUP` | the declaration that makes two readings *intended* rather than a defect |

**Differing: exactly two files.** `ASSIGNMENT.md` and `benchmark/MODE_DIRECTIVE.md`. 18 of 20
surface files byte-identical.

### 4.3 · What each does NOT receive, with the mechanism for each

| Excluded | Mechanism | How far it actually reaches |
|---|---|---|
| LEGEND's prior output on this paper | null-prior selection gate | **absolute** — it does not exist to be read |
| the other reader's output, identity, progress or existence beyond the group name | separate worktrees, no channel; Orchestrator relays no content | **structural** — a `BLOCKER` is answered on the protocol, never on the paper |
| the corpus, during stage 1 | staging + freeze | 🔴 **a prohibition, not a wall** — see § 4.5 |
| network retrieval, both stages | Plan runs the retraction check before handover | structural, at the cost of one pre-step |
| a research question, evidence target or hypothesis to test | absent from every input file **by design**, not by omission | design |
| any anticipated conclusion, from anyone | H.1 — *"mai a ordine"* | governance; binds the dispatcher |
| the evaluation population | Plan holds the denominator; it is not in the surface | a reader who knew it could optimize coverage against it |

### 4.4 · When information may merge — three moments, and the order is load-bearing

```
MERGE-0  never during stage 1        the two readings do not touch, at all
MERGE-1  each reader × the corpus    stage 2, AFTER that reader's own stage-1 freeze.
                                     Still not A × B. Each meets the model alone.
MERGE-2  A × B                       only after BOTH stage-1 freezes and BOTH addenda.
                                     Structural comparison by shared unit — never by
                                     Plan's reading of whether two claims "mean the same"
```

**The freeze is what makes anchoring detectable rather than merely forbidden.** The pre-corpus
record exists, is digested and cannot be revised, so a stage-2 addendum may **never edit stage 1**
— it may only append `corpus_reference` entries typed `corroborates · narrows · contradicts ·
orthogonal · supersedes_premise`. A corpus citation written into `verbatim_locators` either
invalidates the entry or, worse, silently gives the paper sentences it does not contain.

🔴 **And the governance's own independence model is weaker than this, which cuts both ways.**
Body § 26: *"Independence by task framing, not by information barrier."* The surface-based
blindness is therefore **above the floor**, not required by it. That means (a) a lighter first run
is governable, and (b) a design that promises a barrier owes a mechanism the governance never
asked for — so the promise, not the floor, is what must be honoured if it is made.

### 4.5 · The honest limit, stated before the benefits

`BENCH-AB-001` makes every *before* and *after* check mechanical and only the *during* checks
prohibitions. **A pilot with the corpus present moves one item from the mechanical column into the
prohibition column**: the corpus is reachable during stage 1, and "do not open it yet" is an
instruction. Three things bound the damage and none is a promise — the freeze precedes stage 2;
`benchmark_input_surface.py locators` marks a stage-1 locator pointing at a corpus path
`BENCH_INVALID` for that entry, **recorded, never silently dropped**; and *"a declared
contamination is a usable result, and an undeclared one silently invalidates the experiment for
everyone."*

---

## 5 · HANDOFF — WHO RECEIVES THE OUTPUTS

The dispatch offers four paths and is right not to assume a Scientist C. **All four are real, they
are not alternatives, and they fire at different times.** Measured from C.1, C.4, H.1, G.1 and
body §§ 27–29.

| Path | Trigger | Receives | Authority | Timing |
|---|---|---|---|---|
| **Orchestrator** | **always** — every completion | the completion payload; assigns the review level and opens every review | C.3 — *"apertura solo via Orchestrator"*; H.1 — *Livello Ladder e reviewer* | **first, and it is not optional** |
| **Plan** | always | structural / provenance / schema integration; the comparison matrix, aligned **by shared unit** | H.1 — *Integrazione strutturale*; **§ 28 — Plan `NON risolve significato scientifico conteso`** → `INTEGRATION_BLOCK → Orchestrator → Scientist` | after Orchestrator |
| **blind locator audit** | 🔴 **always, and it is not a Scientist** | only `(proposition, quote, anchor)` triples + the source artifact. **No dossier, no conclusions, no reader identity** | none — forms no scientific conclusion. `legend-locator-audit` is the existing instrument | per triple, **100 %**, not sampled |
| **peer Scientist** | **conditional** — C.1 floors: `inferenza L2 importante → R1`; `therapeutic-actionable → R2` | the claim + its locators + the packet — **not** the other reading | C.4 `INFERENCE → peer Scientist`; *"reviewer senza evidenza contribuita"* | routed by content, unknowable at design time |
| **adjudication** | **conditional** — `disaccordo persistente → R3 TRIADIC`, after **max 2 rounds** | both statements, quoted and typed, plus both locator sets | a **turn**, never a post. `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`, rotation, *"mai coppie fisse"* | only if disagreement persists |
| **Mirror** | **floor R4** — *processo inferenziale methodology-changing*, and a first end-to-end run is that on its face | both frozen readings, both addenda, timelines, surface verifications, the null-prior proof, the pin and its re-digest, the audit verdicts, every disagreement quoted and typed, contamination declarations | `SYSTEM → Mirror`; **not** the power to decide whether anything commits | **after both freezes**, never streaming |

### 5.1 · Three things this routing forbids

**No synthesis actor.** § 27: `INFERENCE_A + INFERENCE_B + DISAGREEMENT_UNRESOLVED` with an
explanation *"è esito legittimo; la sintesi forzata è un errore."* Nobody is appointed to make A
and B agree.

**Adjudication is a turn, not a post.** `APPROVAL-GOV311-DEVIATIONS.md` sketches the shape
`A → B hostile review → C adjudication`; making C the standing adjudicator is the static
specialization § 32 forbids, arrived at by scheduling instead of by decree.

**Mirror gets nothing early, and nothing ranked.** Handoff is gated on the *second* freeze — a
Mirror observation on A relayed while B is still reading is a contamination path with a governance
actor in the middle. And § 8.5 forbids an overall score, so the comparison matrix handed over is
**structural and unweighted**: a ranking given to the adjudicator of *method* invites the method
verdict to follow the science verdict.

### 5.2 · 🔴 The routing has two measured holes

**(a) The disagreement has nowhere to land.** `unresolved_disagreements.md` — the destination
`controlled_benchmark_ab.md` § 8.3 names for every disagreement flag, referenced on **16** refs —
exists on **0 of 54**, positive-controlled. **The outcome § 27 most explicitly protects is the one
the state cannot hold.**

**(b) Mirror's own primary input does not exist.** § 29.3: *"L'analisi primaria di Mirror avviene
sull'EVENT LEDGER consolidato (J.1), non leggendo le chat."* `ledger/events/` is absent from this
tree and has no writer. Mirror at floor R4 would be reading the artifacts directly — which is
workable, and is **a declared deviation from its own method**, not a silent one.

### 5.3 · Scientist C — given no function here

`scientist-c` is `REGISTERED_PENDING_L1_L2` with a verified fingerprint and the only two verified
Scientist capabilities in the repository, while A and B are `NOT_REGISTERED` with `ACTOR_ID
UNRESOLVED`. **The one Scientist that is qualified is the one no design uses.** That is an
operational accident and not an argument for giving C a standing role.

🔴 **But the inversion has a governance edge the prior records do not draw.** Body § 32:
*"**Scientist C da creare subito** (`lettore-c`), **qualificato insieme ad A/B**."* The
qualification was meant to be joint. Today it is split, and A and B are the half that did not
happen. Activating A and B alone is not merely completing the set — it is finishing a split § 32
told the system not to make, six days late, with the two halves qualified under different
governance fingerprints. That is worth one deliberate decision rather than a default.

---

## 6 · WHAT MUST EXIST BEFORE THE FIRST PAPER

### 6.1 · Technical

| # | Requirement | State |
|---|---|---|
| T-1 | `lettore` and `lettore-b` synced to a ref carrying `governance/`, `roles/`, the protocols and the benchmark | 🔴 **absent — 201/203 behind** |
| T-2 | both worktrees **clean**, with C-2 forward ownership resolved first | 🔴 **both dirty, 5 days open** |
| T-3 | each actor composes its own fingerprint **in situ** and the value is recorded | 🔴 **impossible today — the script is not on either ref** |
| T-4 | the paper packet present in the **shared checkout's** `files/`, verified and digested | 🔴 no paper; corpus static for 7 days |
| T-5 | surface built → `verify` → **freeze**, one per reader | 🔴 no surface exists |
| T-6 | `CORPUS_PIN` — commit SHA **plus** `files/` tree digest | 🔴 object does not exist (`0` refs) |
| T-7 | `NULL_PRIOR_PROOF` — an enumerated command-produced sweep, archived | 🔴 object does not exist (`0` refs) |
| T-8 | `--artifact-workspace` pointed at the shared checkout; the strict manifest command run **with the shared checkout as cwd** | ⚠️ available, untested — a PASS inside an ephemeral worktree *"does not close the read"* |
| T-9 | validators green | ✅ **all four PASS today** |

### 6.2 · Governance

| # | Requirement | State |
|---|---|---|
| G-1 | 🔴 **a binding Scientist role contract** — i.e. the explicit activation act `DEC-20260822` requires | 🔴 **BLOCKED** — form unspecified; owner **operator** |
| G-2 | `AUTHOR_RESPONSE` to `REV-ROLES-MIRROR-001` | 🔴 required and outstanding; owner **plan** |
| G-3 | MAJOR-1/2/3 dispositioned — MAJOR-3 is the Scientist one | 🔴 no verdict rendered by anyone |
| G-4 | `CAND-20260818-SCIENTIST-AB-SPEC` reviewed and approved → the protocols bind | 🔴 revision 6, `READY FOR MIRROR REVIEW`, 5 prior `REQUEST CHANGES`; queue holds no line for it |
| G-5 | an **ACTIVE** `ORCHESTRATOR_LEASE` | 🔴 `ACTIVE by derivation: 0` |
| G-6 | registration (I.2 step 7) → `ACTOR_ID` fixed for A and B | 🔴 `NOT_REGISTERED`, `ACTOR_ID UNRESOLVED` |
| G-7 | L2 for A and B → capabilities `VERIFIED` **per actor** | 🔴 0 of 6 each; the verified rows belong to `scientist-c` |
| G-8 | two Task Contracts naming resolved `ACTOR_ID`s and a shared `PARALLEL_READ_GROUP` | 🔴 `ledger/tasks/` holds `plan/` only — none has ever existed |
| G-9 | § 32 joint-qualification question settled | 🔴 open (§ 5.3) |

### 6.3 · Routing

| # | Requirement | State |
|---|---|---|
| R-1 | `unresolved_disagreements.md` with a named writer and append discipline | 🔴 **0 of 54 refs** |
| R-2 | the Agent Card registry reachable from the refs the actors are on | 🔴 **1 of 54** — `orchestrator` only |
| R-3 | a registry **validator** — `P1`'s missing instrument | 🔴 absent; *"not authorized to anyone"* under the current decision |
| R-4 | 🔴 **the branch answering a question carries the decision governing it** | 🔴 `DEC-20260822` is on `main`, absent here — § 1.1 |
| R-5 | Mirror's consolidated event ledger | 🔴 `ledger/events/` absent, no writer |
| R-6 | review levels assigned by Orchestrator, floors from C.1 with R4 for the process | ⚠️ specified; unexercisable without G-5 |

**R-4 is small and it is the one I would fix first**, because it is the cheapest and because it
already bit: a readiness assessment written without `git show main:…` would have reported the
Scientist contract as *pending approval* when an operator had determined it *non-binding* the same
day. The general form: **a branch cut before a determination cannot see it, and nothing in the
tooling says so.**

### 6.4 · Validation

| # | Requirement | State |
|---|---|---|
| V-1 | `deepdive_manifest.py --verify-artifacts --require-current-schema` → `VERDICT: PASS`, both readers, as a precondition | ⚠️ tool ready; nothing to validate |
| V-2 | `fulltext_receipts.py verify` → chain intact **after** both receipts append | ✅ 128 chained today |
| V-3 | `benchmark_input_surface.py verify` · `verify-freeze` · `verify --post-read` | ⚠️ tool ready; no surface |
| V-4 | stage-1 locator containment — **zero corpus paths** | ⚠️ mechanism exists (`locators`) |
| V-5 | `NULL_PRIOR_PROOF` re-runs at the pin with the same enumerated result | 🔴 no such proof object |
| V-6 | blind locator audit on **100 %** of triples, per-triple verdict | ⚠️ instrument exists; not scheduled |
| V-7 | coverage map with **no `not_read`**, or an honestly declared partial | ⚠️ rule exists; 🔴 **`Q-10` is open** — whether a *declared partial* may produce a commit candidate is answered nowhere. `BENCH-AB-001` allows it, but its output was quarantined; with a real destination those are different questions |
| V-8 | every `Uncertainty` carrying its *"and by what"* clause | 🔴 proposal only. Measured over the **39** claims of `claim_registry_current.md`: `Uncertainty`, `Limitations` and `Contradictory evidence` appear **0, 0 and 0** times |

---

## 7 · THE ACTIVATION GATE

**No composite score, and no threshold.** § 8.5 refuses a weighted verdict, so this is an
enumeration of states with the command that decides each. **A single RED is dispositive**: the
list is not a tally.

### 🔴 RED — must wait

| # | Item | Decided by | Owner |
|---|---|---|---|
| **R-1** | `roles/scientist.md` is a **non-binding document** by operator determination; a new explicit activation act is required and its form is unspecified | `DEC-20260822-…`, `main` `2bb2700`, § 3 of `IMMEDIATE_CONSEQUENCES` | **operator** |
| **R-2** | the only hostile review of that contract returned **CHANGES_REQUIRED / WEAKENED**, and its `AUTHOR_RESPONSE` is outstanding | `REV-ROLES-MIRROR-001`, `mirror` `1350477` | plan → Mirror |
| **R-3** | `lettore` and `lettore-b` carry **no `governance/`, no `roles/`, no contract, no protocol, no benchmark**; neither can compose its own fingerprint | per-path `git ls-tree` on both refs; `governance_fingerprint.py` → `No such file` | Orchestrator + the actors |
| **R-4** | both worktrees hold **uncommitted, unintegrated content** under a conflict whose forward ownership is unresolved since 2026-08-17; `BOOTSTRAP.md` forbids proceeding | `git -C <wt> status --porcelain`; `HANDOFF-C-2-PMID42422765` | Orchestrator, lease ACTIVE |
| **R-5** | **0 ACTIVE leases**, so nobody may issue a Task Contract, assign a review level or open a review | `lease_state.py` | Orchestrator |
| **R-6** | **0 Scientist Task Contracts have ever existed**; `A`/`B` are `NOT_REGISTERED`, `ACTOR_ID UNRESOLVED` | `ledger/tasks/` = `plan/`; agent card registry | Orchestrator, under lease |
| **R-7** | both reading protocols are `PROPOSED` — *"Until then it binds nobody"* — on an unapproved revision-6 candidate | frontmatter line 8 ×2; approval queue parse | operator |
| **R-8** | **no paper qualifies**, and the corpus has not moved in seven days | census regenerated 2026-08-22; digest identical; 3 of 12 have no body | Plan screens → operator/Orchestrator selects |
| **R-9** | `unresolved_disagreements.md` exists on **0 of 54 refs** while being named on 16 — the legitimate outcome § 27 protects has no carrier | all-refs sweep, positive-controlled | Plan, under a task |

### 🟡 YELLOW — possible but risky

| # | Item | The risk, concretely |
|---|---|---|
| **Y-1** | A and B hold **0 of 6** verified capabilities each; the two verified Scientist rows are **`scientist-c`'s** | Assigning on unverified capabilities is exactly what `CONFIGURED != PROVEN` forbids. Confinement is demonstrated in the clean worktree and never in the dirty two |
| **Y-2** | the recorded scientist fingerprint is stale in **two** places, and canonical execution of the pending candidate will rotate it **again** | A reading started before that execution is resumable only under a fingerprint it was not written under — abandon or re-anchor |
| **Y-3** | the Agent Card registry lives on **one** ref and **no validator reads it** | It has been wrong about the fingerprint across two rotations and nothing detected it. Registering A and B into it records their identity in the least verifiable object in the system |
| **Y-4** | the corpus is present during stage 1 and "do not open it" is a **prohibition, not a wall** | Detectable via the freeze and the locator containment check; not preventable |
| **Y-5** | `Q-10` — may a **declared partial** reading produce a commit candidate? | With a real destination, *legitimate result* and *sufficient to move the model* are different questions, and nothing on any ref answers the second |
| **Y-6** | § 32 asks for A/B/C **qualified together**; today the split runs the other way | Finishing the split by default rather than by decision is how a static specialization arrives without anyone choosing it |
| **Y-7** | Mirror at floor R4 without its consolidated event ledger | Workable, but it is a declared deviation from Mirror's own § 29.3 method — declare it, do not discover it |
| **Y-8** | this branch could not see the determination governing its own question | Fixed by reading across refs; **unfixed as a class** |

### 🟢 GREEN — can start now, and none of it needs activation, a lease or a contract

| # | Item | Why it is green |
|---|---|---|
| **G-1** | **acquire a qualifying paper** — `find-fulltext` over the 11 `HIGH` entries of the 72-entry queue, targeting fresh WWOX-DEE primary literature | No actor authority is required to acquire. It is the longest-lead item and it has not started |
| **G-2** | **run the metadata-only selection screen** at the pin, in the shared checkout | § 28 permits it — structural, decides nothing about meaning. The screener is thereby disqualified from reading, which is a feature |
| **G-3** | **create `unresolved_disagreements.md`** with its writer and append discipline | Independent of every approval. It clears R-9 |
| **G-4** | **recompose the scientist fingerprint into the registry** and record both superseded values | Owed for three records running. Clears half of Y-2 |
| **G-5** | **resolve C-2 forward ownership and clean both worktrees** | Content is already in canonical `main`; what is missing is a decision, not an analysis |
| **G-6** | **sync `lettore` and `lettore-b`** — both are ancestors of `main`, `0 ahead`, so it is a fast-forward **once G-5 lands** | Verified: `git merge-base --is-ancestor` returns true for both |
| **G-7** | **materialize `CORPUS_PIN` and `NULL_PRIOR_PROOF`** as objects | Both are `0 refs` today; both are pure Plan work |
| **G-8** | **the `AUTHOR_RESPONSE` to `REV-ROLES-MIRROR-001`** | Owed under C.2; silence is not acceptance |
| **G-9** | **run the validators, keep them green** | They are green today and are the one axis that is |

**G-1 through G-9 are all independent of R-1.** They can proceed in full while the activation
question sits with the operator, and every one of them shortens the critical path.

---

## 8 · THE FINAL QUESTION

> *"What is the earliest scientifically valid moment where opening Scientist A and B windows
> improves LEGEND rather than increasing noise?"*

**The moment is defined by a state, not a date, and the state is reachable without waiting for the
hardest blocker.** Stated as a condition that can be checked by command:

> **The earliest scientifically valid moment is when a qualifying paper exists in the shared
> corpus with a proved null prior, both reader worktrees are clean and carry the governance they
> will be judged under, each composes its own fingerprint in situ, an ACTIVE lease has issued two
> Task Contracts under one `PARALLEL_READ_GROUP` against a contract that has been activated by an
> explicit act, and the disagreement the run is allowed to produce has a file to land in.**
>
> **Everything before that state is noise — not because the readers would read badly, but because
> nothing they produced could be attributed, resumed, reviewed or landed.**

**Why each clause is load-bearing, and none is ceremony.** A reading produced today would carry a
fingerprint composed from a contract determined non-binding, in a worktree that cannot compute it,
under no Task Contract, by an actor with no fixed `ACTOR_ID`, on a paper with no verified null
prior, and its disagreement — the one outcome § 27 explicitly protects — would have nowhere to go.
That is not a cautious reading of the rules. **It is six independent reasons why the output could
not be used**, and producing unusable output on a real disease model is the definition of noise.

**Three things follow, and the third is the one I would act on.**

**One — the gate is not the paper and it is not the tooling.** The instrument layer is green
today. Question 6 asked for a checklist and the checklist came back with its two `READY` rows on
the axes nobody doubted.

**Two — the earliest moment is *not* gated on the hardest blocker being resolved first.** R-1 is
an operator act with no date. But **nine GREEN items are independent of it**, and they include the
longest-lead item in the whole programme: acquiring a paper. Sequencing the acquisition *behind*
the activation would add the acquisition's duration to the activation's, for no reason.

**Three — 🔴 and the finding I would put above the assessment.** The corpus has not moved in seven
days: same 174 entries, same 87 papers, same digest `825fc4a9d8415b0e`. The two worktrees have not
moved either, and their distance from `main` grew from 136 to 201 in four days. **The system has
spent a week producing analyses of its own readiness while the one precondition that nobody's
approval blocks — having a paper worth reading — went untouched.** Five design records now exist
about a first experiment that has no subject. **The sixth should not be a seventh; it should be a
paper.**

---

## 9 · OPEN QUESTIONS

Recorded, not resolved. Numbering continues the prior records where the question is the same one.

| # | Question | Owner |
|---|---|---|
| **Q-2** | do the benchmark's seven output fields become canonical claim-registry fields, or stay run-local? | operator, on a Plan candidate |
| **Q-4** | what is `scientist-c`'s function, and when is its `ACTOR_ID` fixed? Given none here | operator + Orchestrator at registration |
| **Q-5** | the `OMISSION` asymmetry — MODE B only | Mirror (method), on a Plan note |
| **Q-7** | which paper? The pool is empty of qualifiers; acquisition is required | operator/Orchestrator, on a metadata-only screen |
| **Q-10** | may a **declared partial** reading produce a commit candidate? Unanswered on any ref | operator, on the pilot candidate |
| **Q-11** | 🔴 **what form does the activation act of `DEC-20260822` take?** The determination requires one and *"does not specify its form"*. Everything downstream waits on an object nobody has described | **operator** |
| **Q-12** | 🔴 does approving `CAND-20260818-SCIENTIST-AB-SPEC` discharge the activation act, or are they two acts? The determination's reasoning implies two; nothing states it | **operator** |
| **Q-13** | § 32 requires A/B/C *"qualificato insieme"*. Is the split qualification a deviation to register, or is the clause spent? | operator, on Mirror's note |
| **Q-14** | what wrote blob `86bba8b` into three working directories? `IPOTESI` since 2026-08-17, untested. It is a cross-worktree write in the two trees whose isolation the pilot depends on | Orchestrator, at registration |
| **Q-15** | who may build the **registry validator**? `P1` cannot reach `VERIFIED` without it and building it is *"not authorized to anyone"* | **operator** |

---

## 10 · VALIDATION

### 10.1 · Constraint compliance — checked, not asserted

| Constraint from the dispatch | Compliance |
|---|---|
| this is **not** activation | ✅ no actor opened, contacted, registered or assigned |
| this is **not** assignment of papers | ✅ no paper selected; § 3.2 names a pool and disqualifies it |
| this is **not** creating new actors | ✅ none created; `scientist-c` given no function; no D or E proposed |
| measure the existing infrastructure (6 axes) | ✅ § 2.1–2.7, each with the command |
| classify READY / NOT_READY / BLOCKED | ✅ § 2.8 — 2 / 4 / 6 |
| define the minimum viable first experiment | ✅ § 3.1, with what the minimum costs today in § 3.2 |
| MODE A / MODE B, not permanent identities | ✅ § 4 — modes are task properties (§ 32, protocol § 0); no identity defined |
| what each receives / does not / when it merges | ✅ § 4.2, § 4.3, § 4.4 |
| analyse the handoff; do not assume Scientist C | ✅ § 5 — six paths separated by trigger and timing; C given no function; no synthesis actor |
| what must exist before the first paper | ✅ § 6 — technical · governance · routing · validation |
| produce the GREEN / YELLOW / RED gate | ✅ § 7 — 9 RED, 8 YELLOW, 9 GREEN, no composite score |
| answer the final question | ✅ § 8 |
| output to the named path | ✅ `learning/plan/SCIENTIST-ACTIVATION-READINESS-001.md` |

### 10.2 · What this record does NOT do

It does not activate, register, qualify or open any actor · issue a Task Contract · take a lease ·
select, acquire or open a paper · build, verify or freeze a surface · create
`unresolved_disagreements.md` · sync, clean or touch any worktree or any dirty file · update the
Agent Card registry or recompose a fingerprint into it (**owed for a third record running, and
reported rather than performed**) · render a verdict on MAJOR-1, MAJOR-2 or MAJOR-3 · write the
`AUTHOR_RESPONSE` owed to `REV-ROLES-MIRROR-001` · perform or specify the activation act of
`DEC-20260822` · reconcile the `L2 suspended` / `L2 ratified` disagreement between
`PROPOSAL-C9-STATE-MODEL` § 15 and `runtime/L2-OUTCOMES.md` · open a governance candidate · write
into `framework/`, `governance/`, `roles/`, `ledger/`, `runtime/` or `disease-models/` · read any
paper or form any scientific conclusion.

Every item in §§ 3, 4.4 and 6 marked as a minimum or a requirement is an assessment of what the
existing design implies. **None of it binds anyone**, and § 7 names who would have to act.

### 10.3 · The three prior claims this record contradicts

| Prior claim | Where | Measured here |
|---|---|---|
| *"0 of 27 capabilities `VERIFIED`; L2 suspended"* | `RUNTIME_PROFILE` § 14, `PILOT` `B-3` | **L2 ran and was ratified 2026-08-18** — 3 VERIFIED of 12 attempted, of 21 declared rows. The Scientist rows that passed are **`scientist-c`'s**, which makes the deficit for A and B sharper, not milder |
| *"All three Scientist worktrees are on refs carrying the superseded blob"* | `REV-ROLES-MIRROR-001` MINOR-3 | Only `lettore-c` does. `lettore` and `lettore-b` carry **no `roles/scientist.md` and no `governance/` at all** — a stronger defect than the one reported |
| *"`B-1` (the missing approval line) is still the root"* | `PILOT` § 8 | The root is now `DEC-20260822`'s **`ACTIVATION_NOT_CONFIRMED`**, a closed determination that postdates the framing. B-1 is the second obstacle |

### 10.4 · Negative claims — each with the instrument and how long it holds

| Claim | Instrument | Validity |
|---|---|---|
| `unresolved_disagreements.md` on 0 of 54 refs | `git ls-tree -r --name-only "${r}"`, positive control `roles/scientist.md` → **28** refs | until a ref is pushed |
| `runtime/agent_card_registry.md` on 1 of 54 | same sweep | same |
| no Scientist Task Contract has ever existed | `find ledger/tasks -type d` → `plan/` only | until one is written |
| `lettore` / `lettore-b` carry no `governance/` | `git ls-tree "${r}" governance` → empty, both | until synced |
| the corpus is unchanged since 2026-08-15 | census regenerated against the shared checkout; digest and totals block identical | **until the next acquisition** — this is the claim most likely to expire, and expiring it is `G-1` |

---

## 11 · NEXT_TRANSITION

The dispatch asked whether LEGEND is ready to activate Scientist A and B. **It is not, and the
reason is not the one four of the five prior records name.** The pending approval is real but it
is second: an operator determined **today** that the Scientist role contract is a non-binding
document and that a new activation act — *whose form nobody has described* — is required. Beneath
that, the two worktrees the design names do not contain the governance they would be judged under,
cannot compute their own fingerprints, hold five-day-old uncommitted work under an unresolved
conflict, and have drifted 201 and 203 commits from `main` while five records were written about
them.

**And the nine GREEN items are independent of all of it:**

```
G-1   acquire a qualifying paper — no lease, no contract, no activation required.
      The longest lead, and it has not started
G-5   resolve C-2 forward ownership; clean both trees
G-6   fast-forward lettore and lettore-b — both verified ancestors of main, 0 ahead
G-3   create unresolved_disagreements.md — named on 16 refs, existing on 0
G-4   recompose the scientist fingerprint into the registry — owed for a third record
G-7   materialize CORPUS_PIN and NULL_PRIOR_PROOF — 0 refs each
G-8   answer REV-ROLES-MIRROR-001 — required, outstanding, and it is plan's
```

`R-1` remains the operator's and has no date. Everything above can happen while it waits.

🔴 **The finding worth carrying out of this record above the gate:** for a week the corpus has not
gained a single entry, the two reader worktrees have not gained a single commit, and the
repository has gained six analyses of a first experiment that still has no paper. **The readiness
deficit that is easiest to close is the one nobody is blocked on.**
