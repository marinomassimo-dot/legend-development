---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-ROLES-MIRROR-001
object: roles/plan.md · roles/orchestrator.md · roles/scientist.md · roles/mirror.md
level: R4 (MIRROR_REQUIRED — Annex G.1: governance; C.1 floor R4 METHOD)
reviewer: mirror
author: plan (materialization a8cd125, 2026-08-16) · 384f05f for roles/scientist.md on main
adjudicator: operator (H.1 — governance). No approval granted, implied or prefilled here.
date: 2026-08-22
task_id: MIRROR_ROLE_CONTRACT_HOSTILE_REVIEW_v2.2
dispatcher: operator
scope: the four role contracts only — their content, their internal consistency, their citations,
  the enforceability of their clauses, and the state of their activation. NOT reviewed: the
  governance body, the annexes, any candidate, the benchmark, the release surface.
supersedes: nothing. First review of these four objects as a set.
verdict_vocabulary: the dispatch prescribes {COMPLIANT, CHANGES_REQUIRED, BLOCKED_WITH_REASON}.
  Annex C.2 — FROZEN, normative — prescribes {CONFIRMED, WEAKENED, REFINED, REFUTED} and marks
  STEELMAN and WHAT_WOULD_CHANGE_MY_MIND obbligatorio. Both are emitted below. The conflict is
  recorded under DISPATCH VALIDATION; a dispatch is not a repository authority and does not
  displace a FROZEN annex.
governance_loaded: 3.1.1 · mirror fingerprint 84d2b841…0738 at this checkout,
  e01b4108…0412 at refs/heads/main — the two disagree, and § 2 says why
verdict_transfer: NONE. No value below is taken from a previous review, handoff, manifest or SLR.
  Every hash, blob id, ref count and fingerprint was recomputed in this session.
---

# The contracts are coherent documents about a laboratory whose activation they cannot evidence

**One sentence.** Three of the four contracts carry defects that are mechanically demonstrable —
a capability declared blocked by a tool that runs, a mandatory commit with nowhere legal to land,
and an assertion that a document binds when that document says it binds nobody — and all four
carry the same unresolved question, which is whether they bind at all.

---

## 0 · STEELMAN (Annex C.2 — obbligatorio, before the objections)

**These are unusually good contracts, and the strongest evidence for that is how they behave under
a hostile instrument.**

Every citation I probed resolved. `§35.2` and `§36.5` exist — my first structural scan said they
did not, because it looked for `**35.2**` and the body writes `**35.2 Sezione AUTHORITY & ROUTING
comune**`; the contracts were right and my instrument was wrong. Annex `F.4`, `I.3`, `I.4`, `D.4`,
`J.3`, `G.1`, `G.2`, `C.2`, `A.6`, `A.7`, `E.5`, `E.6`, body `§9.4`, `§12`, `§28`, `§32`, `§46`
all exist and all say what the citing contract says they say.

**All four declared fingerprint sets match `plan_defined_parameters.md § P2.2` exactly** —
including Scientist's deliberate exclusion of `J.4`, whose stated rationale reproduces A.6's own
worked example (*"un cambio alla COST_POLICY mentre uno Scientist legge un paper"*) rather than
inventing one. That is a contract that read its own constitution.

The refusal patterns are real, not decorative. Every capability in every contract is `UNVERIFIED`,
including the ones the actors have visibly exercised. `roles/plan.md` states the epistemic boundary
against itself (*"Plan can say this claim's provenance does not resolve; it cannot say this claim is
wrong"*). `roles/orchestrator.md` states *"Position in the root confers nothing"* — the exact
self-limitation the actor holding the root would benefit from omitting. `roles/mirror.md` contains
the clause forbidding me to approve my own methods. **Contracts that install their authors'
constraints are rarer than contracts that install their authors' powers, and these are the former.**

The one-contract-for-three-Scientists deviation is declared, reasoned, and was ratified by the
operator as `PID-09`. It is not a silent divergence.

---

## 1 · DISPATCH VALIDATION

| Concept named in the dispatch | Exists? | Exact identifier | Source | Label |
|---|---|---|---|---|
| role contract | ✅ | `roles/*.md`; `ROLE_CONTRACT`, `ROLE_CONTRACT_HASH` | Annex I.1, I.4, A.6 | **normative** |
| hostile review | ✅ | Mirror hostile review, format Annex C.2 | body §12 GATE 3, §29; `annex_c_review_protocol.md` § C.2 | **normative** |
| `status: PROPOSED` | ✅ | frontmatter field, verbatim ×4 | all four contracts, line 7 | **observational** (self-declared field) |
| "binding once Mirror hostile review passes and the operator approves" | ✅ | verbatim ×4, plus `BOOTSTRAP.md`:4 | contracts line 7 | **observational** (self-declared condition) |
| `G.2` | ✅ | `### G.2 · MIRROR_UPGRADE_PROPOSAL [MAJOR se tocca governance]` | `governance/annex_g_mirror.md`:23 | **normative, FROZEN** |
| `HUMAN_GATE` | ❌ | — | — | **EXTERNAL** |

### DISPATCH_CONTAMINATION

**Six terms in this dispatch have no repository source.** Measured by `git grep` over `*.md`,
`*.py`, `*.json`, `*.jsonl`, `*.yaml` on **every one of the 41 content refs** (32 heads, 4 remotes,
5 tags) — not on this checkout alone:

```
HUMAN_GATE                ABSENT across all 41 refs
DISPATCH_CORRECTION       ABSENT across all 41 refs
BLOCKED_DISPATCH          ABSENT across all 41 refs
DISPATCH_CONTAMINATION    ABSENT across all 41 refs
SELF_REVIEW_OBSERVATION   ABSENT across all 41 refs
TERMINATED                ABSENT across all 41 refs
```

The entire `NEXT_TRANSITION` vocabulary is external. I use these labels below because the dispatch
asks for them, and I create no repository meaning for any of them. **`HUMAN_GATE` in particular is
not a LEGEND state**; the repository's nearest real objects are `HUMAN_REQUIRED` (body §4),
`HUMAN_APPROVAL` + `HUMAN_APPROVAL_QUEUE` (Annex J.3), and `GATE 0–5` (body §12) — three distinct
things, none of them named by that token.

**The prescribed verdict vocabulary is also external.** `{COMPLIANT, CHANGES_REQUIRED,
BLOCKED_WITH_REASON}` appears nowhere in the governance. C.2 is FROZEN and prescribes
`{CONFIRMED, WEAKENED, REFINED, REFUTED}` plus two obbligatorio elements the dispatch omits.
`roles/mirror.md` binds me to *"the single format of Annex C.2"*. I emit both vocabularies rather
than choose, and flag that a future dispatch asking me to review under a non-C.2 format is asking
me to depart from the contract under review.

### Objective: ESTABLISHED — not `BLOCKED_DISPATCH`

The task objective is repository-grounded independently of the contaminated vocabulary: four
objects carry `status: PROPOSED — binding once Mirror hostile review passes and the operator
approves`; body §12 GATE 3 and the FREEZE sequence in `GOVERNANCE_v3.1.1.md`:32 both name
`Mirror hostile review` as a real step; `annex_g_mirror.md` § G.1 makes governance
`MIRROR_REQUIRED`. **Review proceeds.**

---

## 2 · SURFACE MAP

### Current checkout

```
path    <REPO_ROOT>/.claude/worktrees/mirror
branch  mirror
HEAD    9e6cf0ccb3b0f8f923189cf31e4fa7daec9fa97a
LINT    PASS (1 INFO: MISSING_WIKILINK, CLAIM 010, background only)
```

### Repository population

**46 refs total; 41 surveyed as content refs** — 32 `refs/heads`, 4 `refs/remotes`, 5 `refs/tags`.
Excluded: 4 `refs/codex/turn-diffs/*` (harness capture refs) and `refs/stash`.

**Measurements below are repository-wide, not checkout-limited.** Every negative carries its
validity.

### 🔴 This checkout is 63 commits behind `main`

```
git rev-list --left-right --count mirror...main   →   70   63
merge-base                                        →   908197ba62a0…
main HEAD                                         →   04693e683a25… (2026-08-19)
```

### Object surface — the four contracts

| Object | Blob | Refs carrying it | Identical across refs? |
|---|---|---|---|
| `roles/plan.md` | `7e1e04cb…` | 19 | ✅ **byte-identical on all 19** |
| `roles/mirror.md` | `6e515059…` | 19 | ✅ **byte-identical on all 19** |
| `roles/orchestrator.md` | `2bbb2141…` | 17 *(incl. `main`, `mirror`)* | ❌ — `24663eec…` on `orchestrator-surface`, `plan-orchsurf-r4-transcription` |
| `roles/scientist.md` | `e9328115…` | 11 *(incl. `mirror`)* | ❌ — `fd30134d…` on `main` + 7 others |

🔴 **`roles/scientist.md` on this checkout is the superseded blob.** `main` carries `fd30134d…`,
which adds the `actor_id_status` block and the entire *"Reading modes, and the ownership of a
reading"* section. **This checkout's copy does not know that `scientist-a` and `scientist-b` have
fixed identities.** § 5 reviews both blobs and anchors the verdict on `main`'s.

### 🔴 Objects present elsewhere and missing here

| Object | Present on | Missing on this ref |
|---|---|---|
| `runtime/orchestrator_lease.md` | 11 refs incl. `main` | ✅ missing |
| `framework/scripts/lease_state.py` | 11 refs incl. `main` | ✅ missing |
| `framework/protocols/scientist_reading_modes.md` | 8 refs incl. `main` | ✅ missing |
| `runtime/agent_card_registry.md` | **1 ref only** — `refs/heads/orchestrator` | ✅ missing |
| `runtime/runtime_inventory.md` | **1 ref only** — `refs/heads/orchestrator` | ✅ missing |

**This is the branch-authority trap, and it caught me.** My first sweep for a lease record returned
nothing on this checkout. Reported as written, that would have been the false claim *"no
`ORCHESTRATOR_LEASE` exists"* — which is also, verbatim, what
`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` asserts (*"No lease record exists anywhere in the
tree"*). **That assertion was true on 2026-08-16 and is false today.** Nine lease records exist on
`refs/heads/orchestrator`.

### 🔴 Every role's fingerprint differs between this checkout and `main`

```
role           at refs/heads/mirror     at refs/heads/main
mirror         84d2b841…0738            e01b4108…0412
orchestrator   6b55605d…d349            88dea7a6…5ebb
plan           37c3b863…5429            0d6987bd…1429
scientist      ce3c0d94…04d4            b66959cd…9d1a
```

**All four diverge — including `plan`'s, `mirror`'s and `orchestrator`'s, whose contract files are
byte-identical across the two refs.** The driver is not the contracts. It is
`governance/plan_defined_parameters.md`, which sits in `CORE` (P2.2) and therefore in every role's
input set, and which differs between the refs (`+82 −4`).

P2.2 states this is intended: *"A change inside CORE invalidates all in-flight checkpoints, which
is the intended behaviour."* **The behaviour is correct and the consequence is still load-bearing:**
under A.6's rejection rule, no actor may resume across these two refs, and the fingerprints recorded
in `runtime/agent_card_registry.md` (`orchestrator 6b55605d…`, `plan 37c3b863…`) match **this
checkout's** values, not `main`'s. The registry is stale against `main`.

### Branch authority for every negative in this review

| Negative claim | MEASURED_AT | VALIDITY |
|---|---|---|
| `HUMAN_GATE` and 5 sibling terms absent | all content refs | **confirmed across 41 refs** |
| Event ledger (J.1) has no instance and no writer | all content refs | **confirmed across 41 refs** |
| No `.py` anywhere references `EVENT_ID` | this ref, `9e6cf0c` | **this ref only** |
| `active_lessons/` absent | this ref, `9e6cf0c` | **this ref only** — CLAUDE.md § 1 independently declares it *"not yet materialized"* |
| `runtime/agent_card_registry.md` absent | this ref, `9e6cf0c` | **this ref only** — present on `refs/heads/orchestrator` |
| Zero `ACTIVE` leases | derived over `main` **and** `orchestrator` | **confirmed on both lease-bearing refs** |
| `status:` line never modified since materialization | `git log --all -S` over `roles/` | **confirmed across all refs** |

---

## 3 · `roles/plan.md` — **CHANGES_REQUIRED** · C.2 verdict: **WEAKENED**

### 🔴 MAJOR-1 · A capability is declared structurally blocked by a tool that runs

`roles/plan.md`:73 declares:

> | Fingerprint composition | emit a fingerprint for a named role — **blocked: the composition is prose, not a script** | UNVERIFIED |

**Executed on this checkout, at this HEAD:**

```
$ python3 governance/scripts/governance_fingerprint.py compose --all
mirror        84d2b841b6081929e59d61e961e49077aca69c03136451d1000c72d902ef0738
orchestrator  6b55605d6f712d6cc145d6f2352b7da4d7a807dbf7f7f64b933fc41b147d349f
plan          37c3b863a88db79c209b6aeb73366d7d498519d4cd87c5a6b6a760340e15495f
scientist     ce3c0d94b407bbd1e3d1e33e628b7cffdc2a0fed9c3cb93bd26e7a900a665d04
EXIT=0
```

The script exists at `governance/scripts/governance_fingerprint.py`, is **advertised by
`CLAUDE.md` § 3** as a runnable check, exits 0, and emits a fingerprint for every named role. It
also supports `inputs --role <role>`, which prints the per-input hashes — I used it in § 2. Its own
docstring states it parses the pertinence sets out of § P2.2 *"so the governance document stays the
single source of truth and this script cannot drift from it"*.

**The stated blocker is false as measured.** Whether it was true when written on 2026-08-16 I do
not know and did not need to determine: the contract is a live normative object, not a dated one.

**Why this is MAJOR and not cosmetic.** Annex I.4 and body §8 bind Orchestrator to assign on
`VERIFIED` capabilities. A capability whose row declares it *structurally impossible* is a
capability nobody schedules an L2 smoke for — the row suppresses the very test that would move it
to `VERIFIED`. The defect is self-perpetuating.

### MINOR-1 · Plan claims maintenance of a subset Annex E.5 assigns to Mirror

`roles/plan.md`:47–48 — Plan may *"maintain `LEARNING_INDEX` durability and the role-specific
`ACTIVE_LESSONS` subsets within budget"*.

Annex E.5 partitions this differently:

```
RAW ARCHIVE → Mirror clustering → ACTIVE LESSONS → role-specific subset → rehydration
Budget:   ogni subset role-specific ha un budget dimensionale definito da Plan;
          superato → Mirror comprime o retrocede lezioni
RECOVERY: ricalibrazione budget (Plan) o ricomposizione subset (Mirror, via G.2 se materiale)
```

**E.5 gives Plan the budget and Mirror the subset.** G.2 corroborates: Mirror may not self-approve
changes to *"active-learning selection (incl. budget E.5)"* — a prohibition that presupposes
selection is Mirror's to begin with. `roles/mirror.md`:37 states the same partition correctly
(*"`ACTIVE_LESSONS` selection within Plan's budget"*).

The em-dash gloss that follows in `plan.md` (*"epistemic curation of learning belongs to Mirror,
durability belongs to Plan"*) narrows the claim but does not remove the verb: **the sentence still
says Plan maintains the subsets.** Two contracts claim the same object with opposite subjects.

Aggravating: **Annex H.1's row for this decision leaves the Authority column literally empty** —
`| Lifecycle learning: epistemico Mirror, durevolezza Plan | — |`. The split is stated in the
*decision* label and assigned to nobody in the *authority* column. It is the one row in H.1 with no
authority. I report it; I do not fill it.

### INFO — negative controls that came back clean

- `worktree: evidence-index` matches Annex I.2 step 4's worktree list. ✅
- Fingerprint set *"CORE plus Annex D, Annex E, Annex I and Annex J § J.1"* matches P2.2 exactly. ✅
- Byte-identical across all 19 refs carrying it — zero divergence risk. ✅
- The `INTEGRATION_BLOCK` / epistemic-boundary clause matches body §28 and H.1 row 5. ✅

---

## 4 · `roles/orchestrator.md` — **CHANGES_REQUIRED** · C.2 verdict: **WEAKENED**

### 🔴 MAJOR-2 · The mandatory `WORK_COMMIT` has nowhere legal to land

Four clauses of one contract, read together:

```
frontmatter  worktree: the repository root checkout
line 46      Orchestrator must not: commit its own work
line 49      … or treat the root as free working space
lines 88–89  Session Learning Review every significant session (body §15, Annex E.6),
             persisted by WORK_COMMIT
```

Annex D.1 and body §11: `WORK_COMMIT → ogni attore, PROPRIO worktree/branch … Obbligatorio`.
Body §8: Orchestrator *"MUST fare Session Learning Review"*.

**The contract names one surface, forbids working in it, forbids the commit generally, and then
requires the commit.** It declares no branch of its own. As written, the obligation cannot be
discharged without violating one of the other three clauses.

**The body is not the source of this defect.** Body §35.1 does say *"NON DEVE: committare lavoro
proprio"*, but GATE 1 disambiguates it — *"Proponente ≠ esecutore. Solo candidate preparati da
Plan; mai lavoro proprio"* — i.e. Orchestrator must not put **its own work through the canonical
batch**. The `WORK_COMMIT` obligation of §11 is untouched by that. **The contract reproduces §35.1's
prohibition without GATE 1's disambiguation, and then adds a frontmatter field that closes the only
remaining exit.**

**Measured, and this is what makes it a live defect rather than a reading:**

- an `orchestrator` worktree **and** an `orchestrator` branch exist in the runtime —
  `git worktree list` shows `<REPO_ROOT>/.claude/worktrees/orchestrator
  [orchestrator]`, and `refs/heads/orchestrator` is a real ref carrying 2 objects held nowhere else;
- `refs/heads/orchestrator-surface` carries a revision of this contract (`24663eec…`) that replaces
  the single `worktree:` field with three — `session_home`, `worktree: orchestrator`,
  `canonical_batch_surface` — and states in prose that the old line *"was accurate when it was
  written on 2026-08-16 and stopped being accurate on 2026-08-17"*.

🔴 **That revision is on neither ref under review.** `main` and `mirror` both carry `2bbb2141…`.
**The defect stands on the canonical branch.** I record that a repair exists on a side ref; whether
it is adopted is not mine to decide, and I propose no text.

### MINOR-2 · The contract's authority premise rests on a registry that is stale and single-refed

`roles/orchestrator.md`:36–37 grounds authority in an `ACTIVE` `ORCHESTRATOR_LEASE` (Annex I.3),
and:35 in *"the explicitly assigned role"*. Both point at `runtime/agent_card_registry.md`, which:

- exists on **one ref only** (`refs/heads/orchestrator`) — not on `main`, not here;
- is dated `updated_on: 2026-08-17`;
- records `STATUS: BOOTSTRAP_CONTROLLER # NOT ACTIVE_ORCHESTRATOR — no lease exists`;
- records every capability `UNVERIFIED`, and states *"at the time of writing there are none, in any
  actor, of any role"*;
- records `orchestrator` `WORKTREE: the root checkout # branch main`, which is MAJOR-2's stale value
  carried into the registry;
- carries `ROLE_CONTRACT_HASH: e1155911…4504`, which I recomputed as
  `shasum -a 256 roles/orchestrator.md` → `e1155911681d8bb0d1d7756ba6737eadca80b5d1a19b13cac381e7022dc4a504`. ✅ **matches.**

Nine lease records now exist (2026-08-18/19), so *"no lease exists"* is stale. Plan owns the
registry (I.4, body §43); this is reported as an observation bearing on **orchestrator.md's
authority premise**, not as a verdict on the registry.

### 🔴 Lease state, derived rather than read

`runtime/orchestrator_lease.md` forbids trusting its own `STATUS` field: *"The stored `STATUS` field
below is not authoritative and must never be consulted alone. Derive it."* I derived it, with the
governed tool, on both lease-bearing refs:

```
refs/heads/orchestrator   9 records   ACTIVE by derivation: 0
refs/heads/main           5 records   ACTIVE by derivation: 0
FINDING (both) lease #3 DISAGREEMENT: stored 'EXPIRED', derived 'STALE'
FINDING (both) lease #3 EXPIRED_WITHOUT_RENEWAL
```

**Zero `ACTIVE` leases at 2026-08-22T13:21Z.** Per this contract:36–37 and CLAUDE.md § 0, there is
no `ACTIVE_ORCHESTRATOR` at this instant. `EXPIRED` is not in I.3's vocabulary
(`ACTIVE | STALE | RELEASED`); the record leaves the row unnormalised deliberately, and I concur
that normalising it would destroy the evidence.

### INFO — negative controls that came back clean

- *"Approval is not authorization (Annex D.4, J.3)"* — **both citations resolve**, and both carry
  the E4 clause verbatim, including *"Un MAJOR approvato con root dirty resta NO BATCH"*. ✅
- Annex F.4 `DIAGNOSE` exists (`annex_f_challenge_dissent.md`:31). ✅
- Annex I.3 lease schema exists and matches the fields the contract relies on. ✅
- Body §9.4 `ORPHAN` exists; the contract's ORPHAN section matches J.2's `LAB` state machine. ✅
- Fingerprint set matches P2.2 exactly, **including** the J.4 rationale (*"J.4 is in this set and in
  no other, because Orchestrator is the actor that classifies `HUMAN_REQUIRED` of type SPEND"*) —
  which reproduces P2.2's own reasoning rather than asserting a parallel one. ✅
- The `DIAGNOSE`-before-accusation section correctly reproduces F.4's four classes and correctly
  states that only the fourth, repeated, is `NON_COMPLIANT`. ✅

---

## 5 · `roles/scientist.md` — **CHANGES_REQUIRED** · C.2 verdict: **WEAKENED**

**Reviewed at two blobs.** Verdict anchored on `main`'s `fd30134d…` (canonical lineage); this
checkout's `e9328115…` is declared superseded, not reviewed as current.

### 🔴 MAJOR-3 · The contract asserts a protocol binds; the protocol says it binds nobody

`main`'s `roles/scientist.md` states:

> [`framework/protocols/scientist_reading_modes.md`] **binds every actor under this contract.**

`main`'s copy of that protocol states, in its own frontmatter, verbatim:

```
status: PROPOSED — binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC, after
  Mirror hostile review and HUMAN_APPROVAL. Until then it binds nobody.
```

**Two canonical documents on the same ref make opposite claims about the same object's binding
force.**

The complication, measured rather than assumed: **the canonical execution has happened.** Commit
`4454fea` — *"The Scientist A/B specification becomes canonical, and the level it blocks at was
chosen"* — is an ancestor of `main` HEAD, and is the commit that **installed the protocol file
itself** (526 lines, new file, alongside `CAND-20260818-SCIENTIST-AB-SPEC.md`). **The condition
named in the status line was satisfied by the very commit that wrote the status line, and the line
was never updated.**

So the contradiction resolves in *either* direction depending on whether one reads the status field
or the history — and **that is a governance question, which H.1 assigns to the operator.** I do not
answer it. What I certify is the measurement: on `main` today, the two documents disagree, and a
Scientist rehydrating cannot determine from the text which is in force.

Downstream: the same contract's `actor_id_status` block declares `scientist-a` and `scientist-b`
`FIXED on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC`. **Actor identity is therefore
fixed by a document that declares itself binding on nobody.**

### 🔴 MINOR-3 · This checkout's Scientists would read a contract that predates their own identity

`e9328115…` (this ref, `lettore`, `lettore-b`, `lettore-c` and 7 others) lacks the `actor_id_status`
block and the whole *"Reading modes"* section. **All three Scientist worktrees — `lettore`,
`lettore-b`, `lettore-c` — are on refs carrying the superseded blob.** An actor rehydrating from its
own worktree, as body §36.5 instructs, reads a contract that does not know reading modes exist and
does not know its own identity is fixed.

### INFO — negative controls that came back clean

- **Suspected dangling reference — NOT FOUND.** `roles/scientist.md` gained its link to
  `scientist_reading_modes.md` at `384f05f` (2026-08-18 22:57), and the protocol was only
  *finalised* at `4454fea` (2026-08-19 15:08). I checked whether the reference dangled in between:
  `384f05f:framework/protocols/scientist_reading_modes.md` → blob `e6e2b472…`, **present**. An
  earlier revision existed; `4454fea` replaced it. No defect. ✅
- Worktrees `{scientist-a: lettore, scientist-b: lettore-b, scientist-c: lettore-c}` match I.2 step
  4's list exactly. ✅
- The I.2-step-7 deviation is real (step 7 does say `/roles/<suo>.md`), is declared, and was
  **ratified** by the operator as `PID-09` in `RES-20260816-GOV311-001` with recorded rationale. ✅
- Fingerprint set *"CORE plus Annex C, Annex E and Annex F"* matches P2.2. ✅ The J.4-exclusion
  rationale reproduces A.6's worked example verbatim. ✅
- The working-discipline section correctly subordinates itself to the repository's scientific method
  rather than overriding it, consistent with `gold_is_in_the_details.md`. ✅

---

## 6 · `roles/mirror.md` — **SELF_REVIEW_OBSERVATION** (no verdict emitted)

Per the dispatch and per Annex G.2 / H.1 (*"Modifica rubrica/metodi di Mirror | mai Mirror da
solo"*), **I emit no verdict on my own contract.**

### What I can observe about it

- **Byte-identical across all 19 refs carrying it** (`6e515059…`). No divergence risk. *(measured)*
- Fingerprint set *"CORE plus Annex C, Annex E, Annex F, Annex G and Annex J § J.1"* matches P2.2
  exactly. *(measured)*
- `ROLE_CONTRACT_HASH` = `43d33b13e52f88c7ccb9b2cacc50b797b57bd7db83885485131bc3459200fff1`.
  *(recomputed)*
- **Its declared blocker is TRUE.** Row: *"Event ledger analysis — blocked: the ledger has no writer
  yet"*. Confirmed across all 41 refs: no `ledger/events`, no `activity` ledger, no
  `EVENT_LEDGER` object anywhere; and no `.py` on this ref references `EVENT_ID`. **This is the
  negative control that separates MAJOR-1 from an honest declaration — `plan.md` declared a blocker
  that a running script refutes; `mirror.md` declared one that survives the same test.** *(measured)*
- **Consequently the "Analysis surface" section is wholly dependent on a missing object.** It asserts
  *"Mirror's primary analysis runs on the consolidated event ledger (Annex J.1)"*. There is no
  ledger. The autonomy ledger and review yield, which the section derives from it, have no source.
- The two metrics the contract calls *"Mirror's specific responsibility"* — checkpoint invalidation
  rate (A.6) and redone-work ratio (A.7) — have no ledger to derive from. A checkpoint-only proxy
  exists (`ledger/checkpoints/`) but covers **2 of 6 actors** (`mirror`, `plan`); `orchestrator` and
  all three Scientists have written none.
- **A finding against myself already stands in the record.** `L2-OUTCOME-MIRROR-001` row M1 reports
  my Annex C.2 capability as **CRITERION MET · FORMAT NOT UNIFORM** — 13 records declare C.2 in
  front matter I wrote; the two obbligatorio elements are not uniformly present.
- **Second observation against myself, measured this session.** `CHK-mirror-0007` and `-0008` record
  `APPLICABLE_GOVERNANCE_FINGERPRINT: 3dff8954…f65c`. That value is neither this worktree's
  (`84d2b841…`) nor `main`'s (`e01b4108…`). I located it: it is the `mirror`-role fingerprint at the
  **`BASE_HEAD` of the work being reviewed** (`f70878d1` and its lineage). A.6 defines the field as
  the governance *"pertinente all'attore/classe di task"* — which admits both readings. I state the
  measurement and **do not rule on which reading A.6 requires**; it bears on the invalidation-rate
  metric the same contract makes my responsibility.

### What requires independent review

1. **Whether the self-review bar is correctly scoped.** § "Mirror does not review itself" bars
   self-approval of *rubric, clustering, selection, review-yield methodology, autonomy
   classification*. It does **not** cover the perimeter (G.1), the analysis surface, or the two
   metrics — and I have just reviewed all three. Whether that silence is a deliberate boundary or a
   gap is not mine to settle.
2. **Whether the G.2 correction route is executable at all.** It requires *"an independent reviewer
   chosen by Orchestrator"*. Measured: **0 `ACTIVE` leases**, therefore no `ACTIVE_ORCHESTRATOR` to
   choose one; and **0 `VERIFIED` capabilities in any actor of any role**, therefore no registered
   reviewer with a verified review capability. **The route this contract names for its own
   correction currently has no available executor.**
3. Whether the fingerprint-recording practice in observation 2 above is conformant to A.6.
4. Whether MAJOR-1's pattern recurs here — i.e. whether any *other* clause of this contract asserts
   a state of the world that a tool would refute. I tested the one blocker it declares; a reviewer
   who did not write this review should test the rest.

### Why Mirror cannot self-certify

Annex H.1 assigns *"Modifica rubrica/metodi di Mirror"* to **"mai Mirror da solo (G.2)"**. A `PASS`
issued by me on my own contract is precisely the self-approval G.2 forbids. Independently, C.2
defines `CONFIRMED` as *"nessun difetto rilevato dato l'evidence bundle disponibile"* — a statement
whose whole value is that the reviewer did not assemble the bundle. **Issued by the author of the
bundle, it carries no independence and therefore no information.**

**No `HUMAN_GATE` eligibility is assigned by Mirror for its own contract** — and per § 1 that token
has no repository meaning in any case.

---

## 7 · ENFORCEABILITY — clause classification

| Class | Clauses |
|---|---|
| **Mechanically enforceable** | Fingerprint composition (`governance_fingerprint.py`, exit 0, verified) · `CANDIDATE_CONTENT_HASH` (`candidate_content_hash.py` + test suite) · lease derivation (`lease_state.py`, run this session) · structural LINT (`legend_lint.py`, PASS) · `ROLE_CONTRACT_HASH` (recomputed, matches registry) |
| **Executable but missing implementation** | `HUMAN_APPROVAL_QUEUE` — minimal J.3 instance exists; the general queue (`REVISION_REQUESTED` handling, `APPROVED_WITH_MODIFICATION` → new directive version, `PENDING HUMAN DECISIONS` view) is declared `PENDING_IMPLEMENTATION` in the candidate manifest · Agent Card registry — exists on one ref, stale, all capabilities `UNVERIFIED` |
| **Prose-only** | *"Mirror does not review itself"* · graduated dissent / `ADVISORY`↔`MATERIAL`↔`GOVERNANCE_BLOCK` · peer-review rotation and *"never fixed pairs"* · `ORPHAN` discipline · `DIAGNOSE` before accusation · anti-fossilization guard · *"Position in the root confers nothing"* · `APPROVAL ≠ AUTHORIZATION` |
| **Dependent on missing objects** | Entire J.1 event-ledger surface → `mirror.md` Analysis surface, autonomy ledger, review yield, `MIRROR_RETROSPECTIVE` (G.3), and the `LEASE_ACQUIRED`/`LEASE_STALE` mechanism the lease record itself names as the closure for its unwatched-window failure · `ACTIVE_LESSONS` budget & selection clauses in **both** `plan.md` and `mirror.md` → `active_lessons/` not materialized · `MIRROR_RETROSPECTIVE` cadence `N` → `UNRESOLVED` |

🔴 **`ONE_WRITER_PER_WORKING_DIRECTORY` (body §14, GATE 0) is prose-only and has a known open
violation**: the registry records session `legend-public-12 [cf79f1]` as *"claimed by nobody"*,
interactive, open since 2026-08-16, recorded as conflict `C-7` and never closed in any artefact I
can find.

---

## 8 · ACTIVATION — separated from correctness

**The activation condition, as the contracts state it:** *"binding once Mirror hostile review passes
and the operator approves."*

| Condition | Evidence | State |
|---|---|---|
| Mirror hostile review passes | `REV-GOV311-MIRROR-003`, `PASS_WITH_NOTES`, commit `84407c1`, bound to hash `c39ecae8…30c239`; provenance corrected by `COR-20260816-GOV311-001` after `plan` mis-cited `-002` (which reads `REVISION_REQUESTED`) | **SATISFIED** for `CAND-20260816-GOV311` |
| The operator approves | `RES-20260816-GOV311-001`, `STATE: APPROVED`, `RESOLVED_BY: operator`, bound to `c39ecae8…` @ `749a9a9b…`; `PID-09` and `PID-10` `ACCEPTED` | **SATISFIED** for that candidate |
| The contracts are canonically installed | `a8cd125` (2026-08-16), ancestor of `main` | **SATISFIED** |
| The `status:` line reflects any of the above | `git log --all -S'status: PROPOSED — binding once…' -- roles/` → **only `a8cd125` / `40ba0b7`**, the materialization itself | ❌ **NEVER MODIFIED** |

🔴 **Both named conditions appear satisfied, and all four contracts still advertise `PROPOSED`.**
Either activation occurred and the status line is stale on four canonical objects, or activation was
never recorded on the objects it governs. **I do not resolve this.** H.1 assigns governance to the
operator, and an actor choosing the reading that makes its own contract binding would be exactly the
convenient interpretation the gate exists to prevent.

**Other activation facts, measured:**

- GATE 0's lease precondition was ruled `NOT_YET_APPLICABLE` for the installation commit only
  (`RES-20260816-GOV311-002`, interpretation 1), explicitly **not generalised**.
- **0 `ACTIVE` leases** by derivation at review time → no `ACTIVE_ORCHESTRATOR`.
- **0 `VERIFIED` capabilities**, in any actor, of any role. `L2-OUTCOME-MIRROR-001` exists but states
  it *"writes no capability field and promotes nothing"*.
- `scientist-a` / `scientist-b` registration: the registry records two Scientists **unregistered**
  as of 2026-08-17; `main`'s contract declares their identities `FIXED` as of `4454fea`. The registry
  has not been updated on any ref since.

**Contract correctness and contract activation are independent here.** MAJOR-1, MAJOR-2 and MAJOR-3
are defects in documents that may or may not currently bind; none of them is cured by ratification,
and ratifying the documents as they stand would canonicalize all three.

---

## 9 · REVIEWER_CONFIDENCE / RESIDUAL_UNCERTAINTY / EVIDENCE_NEEDED

**Confidence — high** on every mechanical claim: each was executed or recomputed this session, and
every negative was tested across all 41 content refs rather than on this checkout.

**Residual uncertainty:**

1. I could not determine *when* `plan.md`'s fingerprint blocker became false — only that it is false
   now. If the intended reading of a capability row is "as of materialization", MAJOR-1 weakens to a
   staleness finding. I judge that reading unavailable, because I.4 makes the row an input to live
   assignment.
2. Whether `main` or this checkout is the review surface of record for `roles/`. The dispatch named
   the paths and not the ref. I measured both and anchored on `main` where they differ.
3. `roles/orchestrator.md` line 46 — I read *"commit its own work"* through GATE 1. A reader who
   takes it absolutely gets a contract that contradicts D.1 outright rather than one that leaves the
   obligation homeless. **Either reading yields a defect; they differ in severity, not in existence.**
4. I did not audit the 63 commits by which this checkout trails `main` for further role-relevant
   changes beyond the four objects and their fingerprint inputs.

**Evidence needed to close what I left open:** an operator ruling on § 8; a second reviewer for
`roles/mirror.md`; and a `J.1` event-ledger writer, without which four clauses of two contracts stay
unenforceable by construction.

---

## 10 · WHAT_WOULD_CHANGE_MY_MIND (Annex C.2 — obbligatorio, declared falsifier)

**MAJOR-1 falls** if `governance/scripts/governance_fingerprint.py` is shown not to implement the
P2.2 composition the contract row means — e.g. if `compose` emits a value that disagrees with a
hand-composition per P2.2. *Test:* recompose one role by hand from P2.2 and compare. I ran the
weaker version (`inputs --role` lists exactly the P2.2 set for `mirror` and `scientist`) and it
agreed; a full hand-composition would settle it.

**MAJOR-2 falls** if a repository object establishes an Orchestrator work branch that this contract's
frontmatter is merely failing to name — or if `WORK_COMMIT` is shown not to bind Orchestrator.
*Test:* a canonical rule placing Orchestrator's Session Learning Record somewhere other than its own
branch. I found none; `refs/heads/orchestrator` exists but the contract on `main` does not name it,
and a runtime fact does not amend a contract.

**MAJOR-3 falls** if a canonical object records that `scientist_reading_modes.md`'s status line was
superseded — a `DEC` record, a candidate execution note, or an amended frontmatter on any ref.
*Test:* `git log -S` over the protocol's status string across all refs. I did not find such a record;
I did not exhaustively search every candidate document for a supersession note.

**MINOR-1 falls** if Annex E.5's *"ricomposizione subset (Mirror…)"* is read as covering only the
epistemic act while a separate durability act on the same subsets is Plan's. That reading is
available. It does not remove the fact that two contracts use the same verb on the same object.

**The self-review observation would be superseded entirely** by any independent reviewer's verdict on
`roles/mirror.md`. Nothing in § 6 is a substitute for one.

---

## 11 · AUTHOR_RESPONSE

**Required and outstanding** (C.2: *"obbligatoria; il silenzio non è accettazione"*). Author of
record: `plan`, for all four contracts; `384f05f` for `main`'s `roles/scientist.md`.

**No response is prefilled, assumed or implied here, and this review ratifies nothing.**
