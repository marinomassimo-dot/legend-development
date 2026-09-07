---
artifact: MIRROR hostile review — the emerging LEGEND laboratory architecture
review_id: REV-LEGEND-LAB-ARCHITECTURE-001
task_id: REV-LEGEND-LAB-ARCHITECTURE-001
iteration: 1/3
mode: HOSTILE_REVIEW_ONLY
level: R4 METHOD
reviewer: mirror
author: two records by two distinct sessions — see OBJECT
adjudicator: NOT ASSIGNED — no ACTIVE lease exists, and C.3 puts review opening with Orchestrator
dispatcher: operator
date: 2026-08-22
governance_version: 3.1.1 (read, not exercised)
authority_claimed: none
classification:
  - HOSTILE REVIEW ONLY
  - NO DESIGN · NO REPAIR · NO REPLACEMENT ARCHITECTURE
  - NOT GOVERNANCE · NOT A DECISION · NOT AN AUTHOR_RESPONSE
domain: >
  CONTROL_PLANE. `reviews/` IS among the exhaustive CONTROL_PLANE_ROOTS declared at
  `main@788c357:governance/plan_defined_parameters.md:255-262` — measured, not assumed, because
  one of the objects under review asserts the opposite (F-2). This file therefore does NOT move
  any CANDIDATE_CONTENT_HASH.
format_note: >
  Annex C.2 is FROZEN and requires STEELMAN *before* the objections. The dispatch's OUTPUT list
  orders VERDICT and FINDINGS before STEELMAN. Every section the dispatch names is present; two
  are reordered so the FROZEN annex wins over the dispatch's ordering. The deviation is declared
  here rather than silently taken.
---

# REV-LEGEND-LAB-ARCHITECTURE-001

## OBJECT

Addressed as `(ref, path, blob)`, because in this repository a path is not an address.

| # | Object | Address |
|---|---|---|
| **OBJ-1** | Orchestrator-seat loop/coordination analysis | `orch-pipeline-loop-architecture@d6d46f8` : `learning/orchestrator/ORCHESTRATOR-SCIENTIFIC-PIPELINE-AND-LOOP-ARCHITECTURE-ANALYSIS-001.md` · blob `52868cf1735d` |
| **OBJ-2** | Plan-seat Scientist pipeline readiness | `plan-orchsurf-r4-transcription@2394b07` : `learning/plan/SCIENTIST-PIPELINE-READINESS-001.md` · blob `1ddf4b17e7f6` |
| **OBJ-0** | predecessor at the Orchestrator seat | `main@788c357` : `learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md` · blob `b8f83324a67b` |
| **CTX-1** | the lease record, both versions | `main@788c357` blob `c34f48668d` (5 rows) · `orchestrator@1e2fabd` blob `d8a2b47bf8` (9 rows) |

🔴 **The dispatch names two objects that do not exist under those names.** Searched
case-insensitively across all 37 heads this session: `"coordination protocol"` → **0 files**,
`"Orchestrator coordination"` → **0 files**, `"scientist pipeline model"` → **0 files**. Neither
phrase exists as file, candidate, protocol or identifier. One branch carries the nearer name —
`orch-agent-coordination-protocol`, created **2026-08-22T16:59:10Z, during this review** — and
`git diff main...orch-agent-coordination-protocol` is **empty**. It points at `788c357` with zero
commits of its own.

So the review is scoped to the two records that actually carry the concepts, named above. This is
not pedantry: it is F-9's mechanism, observed on the dispatch that commissioned this review.

---

## TASK_STATUS

```
TASK_ID       REV-LEGEND-LAB-ARCHITECTURE-001
ITERATION     1/3
MODE          HOSTILE_REVIEW_ONLY
STATE         COMPLETE for iteration 1 — 10 findings, all re-derived in this session
BLOCKING      none for the review. Every finding is owned by someone who is not Mirror.
NOT DONE      no design, no repair, no replacement architecture, no fix, no recommendation
DELIVERABLE   this file, one commit, branch `mirror`, under H.1 WORK_COMMIT — needs no lease
```

### Compliance of this review with the protocol it is written under

| Requirement | State |
|---|---|
| Annex C.2 single format, STEELMAN first | ✅ satisfied, with the reorder declared in frontmatter |
| C.2 declared falsifier | ✅ `WHAT_WOULD_CHANGE_MY_MIND` |
| C.2 `AUTHOR_RESPONSE` mandatory, silence ≠ acceptance | ⚠️ **owed by two authors on two branches; no channel exists to request it** (F-3) |
| C.3 *"apertura solo via Orchestrator"* | 🔴 **NOT SATISFIED.** This review was opened by an operator dispatch. `ACTIVE by derivation: 0`; there is no Orchestrator. I cannot cure this, and I record it rather than proceed silently. |
| C.2 `OBJECT` = claim id / `CANDIDATE_CONTENT_HASH` / directive id | 🔴 **NOT SATISFIED.** Both objects are `learning/` blobs on branches with no candidate and no hash. Nothing binds this review to a frozen object — see F-9 and the surface drift measured below. |
| G.2 Mirror may not self-approve its own method | ✅ nothing here changes Mirror's rubric, clustering, selection, yield or autonomy methodology |
| roles/mirror.md — no command, no primary evidence, ex post only | ✅ no actor is directed; no paper was read; no scientific claim is asserted |

---

## IDENTITY

**Established from repository evidence. Nothing is inherited from the dispatch, and nothing is
read from `roles/mirror.md` as a source of authority — that contract is `PROPOSED` and
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (main) determines `OPTION B —
ACTIVATION_NOT_CONFIRMED` for all four.**

| Fact | Measured value | How |
|---|---|---|
| Working directory | `<REPO_ROOT>/.claude/worktrees/mirror` | `pwd` |
| Branch | `mirror` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `a121cdd9a41b716575959593f584371b47d126f1` | `git rev-parse HEAD` |
| HEAD subject | *"The response conceded a false row against four artifacts, and the rule that counted them was never declared"*, 2026-08-22T18:40:19+0200 | `git log -1` |
| Working tree | **clean** before this record | `git status --porcelain` → empty |
| Worktree | `.claude/worktrees/mirror`, listed by `git worktree list` | — |
| Divergence from `main` | **74 ahead · 65 behind** | `git rev-list --count` both ways |
| **Lease** | **`ACTIVE by derivation: 0`** — and see F-1: this is true of *both* populations, and the population is not the one either reviewed record reports | run this session, both blobs |
| Runtime inventory | absent from this ref; present at `orchestrator:runtime/runtime_inventory.md` | `git ls-tree` per ref |
| Agent Card registry | absent from this ref; `orchestrator` only | `git ls-tree` per ref |
| `ACTOR_ID` | **`mirror`** — supported by `roles/mirror.md` (`actor_id: mirror`, `worktree: mirror`) and the registry card on `orchestrator`, both read at source. The worktree directory name matches both. **Registration status `REGISTERED_PENDING_L1_L2`; all four declared capabilities `UNVERIFIED`.** |
| `SESSION_REF` | **not observable, and not invented** | — |

### 🔴 The reviewing seat does not carry the objects it reviews

**MEASURED_AT `mirror@a121cdd`, this session.** 65 paths present on `main` are absent here.
Among them:

```
framework/protocols/scientist_reading_modes.md      ABSENT  — the protocol that defines MODE A/B,
                                                              the blind first pass, PARALLEL_READ_GROUP
framework/protocols/controlled_benchmark_ab.md      ABSENT  — the benchmark protocol
framework/protocols/cross_session_transport.md      ABSENT
framework/scripts/lease_state.py                    ABSENT  — the lease derivation
framework/scripts/benchmark_input_surface.py        ABSENT  — the blind-path builder
governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md   ABSENT
runtime/                                            ABSENT ENTIRELY — no lease record, no registry
governance/candidates/CAND-*                        7 of 7 ABSENT
ledger/tasks/plan/*, ledger/checkpoints/plan/*      ABSENT
```

**Every reading below of any of those objects is a cross-ref read.** None of it is reproducible by
standing in Mirror's seat, and I ran the lease derivation by extracting the script and both blobs
into a scratchpad outside the repository. Recorded as method, and again as F-7.

### Authority

**None claimed.** No gate is asserted, no verdict is binding, no actor is directed, no object is
activated, no finding is resolved. Under H.1 this review is `Epistemic / method review`, which is
Mirror's row; under Annex G it is ex post and pattern-based and is **never a veto before the
fact**. The four contracts remain `PROPOSED` and none of them is cited here as the source of a
rule.

---

## SURFACE_MAP

### Refs and worktrees

```
MEASURED_AT     2026-08-22T16:33Z … 17:02Z (session clock, UTC)
REFS            37 local heads at close of measurement  ·  4 remote  ·  5 tags
                🔴 36 at open. `orch-agent-coordination-protocol` was created at 16:59:10Z,
                   inside this review's own measurement window.
WORKTREES       19 at close. OBJ-1 measured 17 at 16:33Z.
NOT SURVEYED    refs/codex (4) · refs/stash (1) — content not enumerated
```

🔴 **The review's surface moved while the review was running, and nothing froze it.** Annex C.2
requires `OBJECT` to be a claim id, a `CANDIDATE_CONTENT_HASH` or a directive id — identifiers
that cannot move. This review's objects are two loose blobs. Every negative claim below is scoped
to the surface as measured at the stated instant and to nothing wider.

### The control plane, censused across all 37 heads — positive control passed

```
POSITIVE CONTROL   ledger/approvals/  → 21 hits across heads. Instrument working.

ledger/events/       (Annex J.1)      0 files · 0 refs of 37
active_lessons/      (CLAUDE.md §1)   0 files · 0 refs of 37
LEARNING_INDEX       (Annex E.2)      0 files · 0 refs of 37
```

Annex J.2 defines a transition as *"evento (J.1) + roster durevole."* Every actor transition ever
performed in this laboratory lacks the event half of its own definition. `roles/mirror.md` names
the consolidated event ledger as Mirror's **primary analysis surface**; it does not exist, and the
matching capability is recorded in that same file as *"blocked: the ledger has no writer yet."*

### Where the corpus actually lives

| Namespace | `main` | `mirror` | `orchestrator` | Plan's branch | total |
|---|---|---|---|---|---|
| `reviews/` — **CONTROL_PLANE** (hash-free to merge) | **3** | 50 | 14 | 7 | 74 |
| `learning/` — **CONTENT** (merging moves the hash) | 11 | 34 | 13 | 23 | 81 |

### Throughput, 2026-08-16 → 2026-08-22, all refs

```
commits, all refs                                                    324
  touching governance/ learning/ reviews/ ledger/ runtime/ roles/    311
  touching framework/state/ or disease-models/                         0
growth anchors, run this session   claims=39 · papers=70 · corpus=356 · literature=390   PASS
receipts, run this session          128 chained, tail anchored                            OK
unpushed to origin/main                                              455 commits
origin/main last advanced                                            2026-08-01
```

### Method failure in this session, recorded because it is the class under audit

My first per-ref sweep for the lease record returned **`ABSENT` on all 36 heads**, including
`main`, where a direct call had already succeeded. The cause was `"$r:runtime/…"` in zsh: `$r:r`
is a parameter modifier, so the shell resolved `main` and dropped `untime/…`. **A clean, wrong,
repository-wide negative.** It was caught only because one direct call disagreed with the loop.

This is the class OBJ-1 registers as R-6 with four prior instances; it is a fifth, produced while
auditing R-6, by the actor auditing it. The guard that would have caught it —
`PROV-POSITIVE-CONTROL-BEFORE-NEGATIVE-FINDING` — lives at
`governance/design_records/materialization_log.md:1026`, in a file no script reads and no
entrypoint cites. I did not reach it through the repository. Every negative claim in this review
was re-run with braces and with a stated positive control.

---

## STEELMAN

*Mandatory, and it comes first. It is not a courtesy paragraph.*

**These two records are the strongest artifacts this repository has produced, and the hostile
findings below exist because the records made themselves attackable.**

1. **Both refused the authority the dispatch offered.** Each was addressed as an actor and each
   measured `CLAUDE.md` § 0 instead, found both antecedents true, and declared `BOOTSTRAP_MODE`.
   OBJ-2 additionally refused to rule on whether its own governing protocol binds, on the ground
   that extending `DEC-20260822` by analogy would be a governance interpretation reserved to the
   operator. That refusal cost OBJ-2 the ability to say anything decisive, and it is correct.

2. **Both refused the interpretation that would have given them a role.** OBJ-1 § 5.2.5 and OBJ-2
   § 6.3 face the same fork on the third position and both decline it, citing the same principle —
   *an actor choosing the reading that gives it a function is the interpretation the gate exists to
   prevent.* Two independent sessions reached the same refusal from opposite seats.

3. **The epistemic discipline is real and it is measurable.** OBJ-2 declares `verdict_transfer:
   NONE` and re-measured the approval queue rather than accepting OBJ-1's report — and found a
   different number. OBJ-1 self-reports a regex false negative in the middle of the finding that
   the regex produced, and reports it as an instance rather than as a claim to have applied a
   practice. Both attach `MEASURED_AT` and `VALIDITY` to negative claims. This is better than
   most human review.

4. **The central diagnosis is right, and I re-derived it independently.** *Authority is not the
   blocker; addressing is.* H.1 allocates every edge of `Orchestrator → Plan → Mirror → Scientist`
   without gap or overlap. What is missing is a return edge: every actor's output lands on its own
   branch by H.1's own confinement of `WORK_COMMIT`, and nothing carries `(ref, path)` forward.
   Four independent documents met this failure **while analysing it**. That is a system diagnosing
   itself correctly.

5. **OBJ-1's § 3.4(b) is CONFIRMED verbatim by independent re-measurement.** I censused
   `HUMAN_APPROVAL_QUEUE.jsonl` by blob across 37 heads:

   ```
   20c24a2ba4   6 lines · 2 IDs   · 18 refs incl. main and mirror
   bb603d9a27  10 lines · 6 IDs   · orchestrator
   95fc816390  14 lines · 6 IDs   · evidence-index, p51c9-rebased
   DISTINCT APPROVAL_IDs repository-wide 10 · MAX on any ref 6 · main carries 2 · non-nested
   ```

   An append-only ledger has been appended to concurrently on two branches. J.1 forbids exactly
   this in terms. The finding is real, the measurement holds, and it was found by the record's
   author against the author's own seat.

6. **Every "not ready" item is owned by someone else, and both records say so without hedging.**
   OBJ-2 § 8.3: *"Nothing in the NOT_READY column is unblocked by more analysis."* A record that
   declares its own iterations 2 and 3 incapable of moving anything is a record not protecting its
   own mandate.

**The findings below do not dispute this. They attack what the records could not see from where
they stood, what they measured against a ref-local surface and reported as repository-wide, and
what the architecture does to an actor who behaves exactly as the records do.**

---

## VERDICT

Per Annex C.2's four values, per object.

| Object | Verdict | Scope |
|---|---|---|
| **OBJ-1** — Orchestrator-seat loop/coordination analysis | **WEAKENED** | The central diagnosis (addressing, not authority) survives. Two load-bearing measurements do not: the lease population (F-1) and `CONTROL_PLANE_ROOTS` (F-2). F-2 is a false negative promoted to a new open question **and** used as evidence for a structural conclusion in § 5.4.6. |
| **OBJ-2** — Plan-seat Scientist pipeline readiness | **REFINED** | No claim I tested is false. The independence model, the contamination taxonomy, the C analysis and the readiness matrix all hold at source. It inherits the lease-population error (F-1) and its blindness is a surface it declared and could not see past: the scientist worktrees' uncommitted state (F-5). |
| **The architecture as a whole, as these two records describe it** | **WEAKENED** | The 95/5 target is stated against a denominator that excludes the dominant human term (F-3); the only named check on Orchestrator adjudicating challenges to itself is disabled (F-4); the singleton invariant is computed over a ref-local population (F-1); and at 5 papers the coordination layer already consumes 100% of throughput (F-8). |

**`CONFIRMED` was available and I did not use it.** Under C.2 `CONFIRMED` means *"no defect found
given the available evidence bundle"* — never *"true"*. Defects were found.

```
REVIEWER_CONFIDENCE     HIGH on F-1, F-2, F-5, F-7, F-8 — each re-derived in this session with a
                        declared positive control, from git objects and working trees I read myself
                        MEDIUM on F-3, F-4, F-9 — the measurements are firm; the inference from
                        measurement to "this is the architecture's failure mode" is mine, not the
                        repository's, and is contestable
                        LOW on F-10 — the risk is real, the sizing is not measured

RESIDUAL_UNCERTAINTY    refs/codex (4) and refs/stash (1) were not enumerated. Chat transcripts
                        are not repository objects and were not read; every statement about what
                        an actor intended is BY-REPORT from a committed record. I cannot observe
                        any actor's liveness, and I have no instrument that could.

EVIDENCE_NEEDED         the consolidated event ledger (J.1). Five of the eight DETECTION routes in
                        governance/ terminate at Mirror instruments that do not exist, and the two
                        that would detect a RECURRING failure — annex_e:52 and annex_i:73 — are
                        both in the unavailable set. Recurrence is what G.1 makes MIRROR_REQUIRED.
```

---

## FINDINGS

Ten findings, one carrying a measured extension (F-6b). Each is anchored to a measurement taken in
this session, with the command class named. None is a prediction about anyone's conduct. **No fix
is proposed for any of them.**

---

### 🔴 F-1 · MAJOR · The lease record has forked, and the singleton invariant is derived over a ref-local population

**Review question 2 (Orchestrator control) · 4 (memory) · 5 (coordination collapse)**

Censused by blob across 37 heads, with positive control:

```
blob c34f48668d   5 rows   main + 10 other heads   last release 2026-08-18T14:05:20Z
blob d8a2b47bf8   9 rows   orchestrator ONLY       last release 2026-08-19T20:34:32Z
file absent        —       24 heads, INCLUDING mirror, lettore, lettore-b, lettore-c
```

I ran `lease_state.py` against **both** blobs in a scratchpad. Reproduced:

```
main's blob         5 records · ACTIVE by derivation: 0 · 2 findings on #3 · exit 1
orchestrator's blob 9 records · ACTIVE by derivation: 0 · 2 findings on #3 · exit 1
```

**The verdict is identical. The population differs by four records — 44%.** Leases #6, #7, #8 and
#9 exist on exactly one head. Three of them executed `CANONICAL_BATCH_COMMIT`s that are now
ancestors of `main`, and `main`'s own lease record does not contain them.

**All three analysis records report the short population as fact.** OBJ-0, OBJ-1 § 1.1 and OBJ-2
§ 1 each state *"five leases … most recent released 2026-08-18T14:05:20Z."* Repository-wide that
sentence is wrong, and it is the sentence each record uses to establish that it is in
`BOOTSTRAP_MODE`.

🔴 **The structural half is worse than the arithmetic half.** Lease #9's own `WRITE_SURFACE` field
states the reason, in the record itself:

> *"a lease row written on main or on the candidate branch would move `CANDIDATE_CONTENT_HASH`
> and void the approval this lease executes … the protection is `PROCEDURAL`."*

So by design, **during exactly the window in which a lease is `ACTIVE`, its row exists only on the
`orchestrator` branch** — the ref that 24 of 37 heads cannot see, and that the derivation, run
from any other checkout, does not read. Annex I.3 specifies its own `DETECTION` as *"doppio record
sulla stessa successione → alla scrittura o alla riconciliazione."* That detector is blind in
precisely the window it exists for.

This is `OBS-LEASE-DETECTION-GAP-001` **migrated, not closed.** The gitignored interim seat was
retired for being unreadable across checkouts. The tracked seat is absent from 24 of 37 heads and
four records stale on 11 of the remaining 13.

**Neither record notes it.** OBJ-1 § 2.3 enumerates cross-ref-only objects and the lease is not in
the table. OBJ-2 § 2.4 explicitly re-measures the approval queue's ref-dependence — the same test,
correctly applied to a different file — and does not apply it to the lease. The instrument that
would have caught it is the one both records already used.

**Consequence for review question 2, stated plainly:** the answer to *"who controls Orchestrator"*
is that the lease is written by Orchestrator, in Orchestrator's worktree, to a path the governance
declares readable by everyone and that 65% of heads do not carry — and the invariant that would
catch a second writer is computed by each reader over whatever subset its own checkout happens to
hold.

---

### 🔴 F-2 · MAJOR · OBJ-1's N-4 is false at OBJ-1's own declared measurement base, and it is load-bearing

**Review question 6 (governance drift) · 4 (memory)**

OBJ-1 asserts three times — frontmatter `domain:`, § 5.4.6, and as **N-4, a NEW open question**:

> *"`CONTROL_PLANE_ROOTS` still omits `reviews/`, five days after the operator-adjudicated MAJOR
> determination requiring it"* · *"`plan_defined_parameters.md:250` lists `CONTROL_PLANE_ROOTS` as
> `governance/candidates/` and `ledger/`"*

Measured at `main@788c357` — OBJ-1's own declared base, and the **identical blob `e1f9e1ec6fce`
is on OBJ-1's own branch**:

```
governance/plan_defined_parameters.md
255  Control-plane roots are declared here, exhaustively, as directory prefixes:
258  CONTROL_PLANE_ROOTS:
259  - governance/candidates/
260  - ledger/
261  - reviews/          ← present
```

`reviews/` entered at `178ea2a`, **2026-08-17T17:09:25+0200**, subject *"P5.1 gains reviews/,
states learning/ by intent, and the Orchestrator gets a branch"* — an ancestor of `main`. The
determination was propagated the same day it was adjudicated. Line 250 is prose mid-sentence and
contains no list.

**OBJ-0 and OBJ-2 both state the list correctly, including `reviews/`.** OBJ-1 therefore regressed
a measurement two sibling records had right, on the same day, from the same repository — and its
frontmatter declares `corrects:` **two** measurements of its predecessor, enumerating O-7 and O-4.
This third one is not among them and travels in the opposite direction.

**Why it is load-bearing and not cosmetic.** § 5.4.6 uses it to conclude:

> *"Layer C therefore exhibits the same property § 5.4.2 measures for layers A and B: a durable,
> correct, adjudicated record that has not altered the system it describes."*

The **symptom** is real — I measured `reviews/` at 3 on `main` against 74 repository-wide. The
**mechanism** OBJ-1 names for it does not exist. The record was propagated. See F-7 for what the
symptom's actual cause is, and note that the two causes have opposite implications for anyone
reasoning about it.

**Class.** A false negative promoted to a new open question and to evidence for a structural
conclusion — the exact class OBJ-1 registers as R-6 and enumerates four prior instances of. It is
the fifth. Mine, above, is the sixth.

---

### 🔴 F-3 · MAJOR · The 95/5 target is measured against a denominator that excludes the dominant human term

**Review question 1 (human bottleneck)**

Both records account for human involvement by counting **gates**:

```
OBJ-1 § 7.2    5 recurring per batch (HG-1…HG-5) + 7 one-time unblocking (HG-6…HG-12)
OBJ-2 § 8.3    11 one-time unblocking + 4 recurring
```

**Neither accounting contains a row for the thing the human actually does.** OBJ-1 says so itself,
in § 5.5.1, and then does not carry it into § 7.1's table or § 7.2's total:

> *"The three functions the dispatch wants to keep with the human are already the human's by H.1,
> and none of them is what the human is currently spending effort on. The measured human cost is
> transport."*

Measured, whole period rather than one day: **324 commits since 2026-08-16 across all refs.** H.1
confines `WORK_COMMIT` to *"ogni attore, solo proprio branch."* There is no merge, no message and
no shared file connecting any two sessions. Every session therefore began with an operator-composed
dispatch naming a role, a mode, a scope and — critically — **which ref to read.** The human is not
5% of the decisions. The human is 100% of the edges.

**Four hidden dependencies the gate accounting does not reach:**

| Where | The dependency | Measured |
|---|---|---|
| **routing** | no dispatch record in this repository carries a ref; a path is not an address | OBJ-1 B-5, re-derived here — this review had to be told OBJ-1's branch |
| **identity** | `SESSION_REF` is not observable by its holder; the registry derives all four **by set complement** on a stated assumption `pending L1`; C-7 — one session seen by all four actors and claimed by none — open since 2026-08-16 | registry at `orchestrator`; OBJ-1 § 5.1.2 |
| **ownership** | `ledger/registrations/` **0 files on every ref**. `scientist-a` and `scientist-b` are `NOT_REGISTERED` while their `ACTOR_ID`s are canonically fixed; I.2 step 7 has each actor read `roles/<its own>.md` at registration and **neither worktree carries `roles/` at all** | OBJ-2 N-2, N-7; re-measured in F-5 |
| **ambiguity** | OBJ-1 leaves 18 items open (Q-1…Q-10, O-1…O-6, N-1…N-4); OBJ-2 leaves 15 (Q-A…Q-H, U-1…U-7). **Not one is resolvable by any actor in the laboratory.** Six of OBJ-1's seven one-time gates are the operator's by H.1; the seventh (HG-11) is barred to Mirror by G.2 and assigned to nobody | both records' own tables |

The 5% is not a residue left after automation. It is the entire set of unresolved state, plus every
edge in the graph.

---

### 🔴 F-4 · MAJOR · Orchestrator adjudicates challenges against Orchestrator, and the one compensator the design names for that is disabled

**Review question 2 (who controls Orchestrator · circular authority · who reviews routing)**

Read at source, `main@788c357`:

```
H.1   Aggiudicazione challenge                      → Orchestrator (con rationale)
H.1   Livello Ladder (≥ floor) e reviewer           → Orchestrator
H.1   Epistemic / method review                     → Mirror
H.1   Modifica rubrica/metodi di Mirror             → mai Mirror da solo (G.2)
G.2   flusso: proposal → Plan candidate → reviewer INDIPENDENTE SCELTO DA ORCHESTRATOR → validazione
C.3   apertura review solo via Orchestrator
F.2   verdicts: ACCEPT | MODIFY | OVERRIDE_WITH_RATIONALE | ESCALATE
```

**There is no recusal clause anywhere.** A challenge against Orchestrator's routing is adjudicated
by Orchestrator, who may `OVERRIDE_WITH_RATIONALE`. Mirror reviews Orchestrator's method;
Orchestrator selects the reviewer of any change to Mirror's method and opens every review Mirror
might be given. **The loop is closed and its only exit is the operator — which is F-3.**

**The design knows this and names the compensator explicitly.** Annex F.3:

> *"Mirror: quali classi di dissent Orchestrator tende a `OVERRIDE` che poi risultano
> `VALIDATED_LATER`? Ex post, mai veto ex ante."*

That compensator requires two things, both measured absent in this session:

```
(a) the consolidated event ledger    ledger/events/  →  0 files, 0 refs of 37
(b) MIRROR_RETROSPECTIVE every N     N is UNASSIGNED. G.2 bars Mirror from setting it alone.
                                     Plan declined it (G.2 puts retrospective methodology inside
                                     Mirror's method); Mirror declined for the same reason.
                                     OBJ-2 B-9 · OBJ-1 HG-11 · ANNEX_INDEX row: UNASSIGNED
```

**So the sole named check on the adjudicator being the challenged party is an ex-post statistic
over a ledger with no writer, at a cadence nobody in the laboratory may set.**

**"What happens when Orchestrator is wrong" has a measured answer here, and it is not the ladder.**
The Orchestrator branch's own commit subjects record the detections:

```
ea4bd9d  "I routed curation to a surface that does not exist, and asserted a confirmation class against it"
677fbb2  "I deferred into a void inside the record written to note that I had deferred into a void"
88ccdc9  "I read a disjunction, evaluated one branch, and reported it to the operator as the only route"
0ccd7e2  "I wrote my own exposure as a delta one record after ruling that a delta is not a population"
```

Every one is **self-detection**. That is a property of the actor occupying the seat, not of the
architecture. An architecture whose error-detection record consists entirely of the subject
catching itself has not demonstrated that it can catch a subject that does not.

**And the contract governing the reviewer is the one contract no review can reach.**
`REV-ROLES-MIRROR-001` returned **no verdict** on `roles/mirror.md`, under the self-review
prohibition (OBJ-2 Q-H). Mirror may not review Mirror; Orchestrator picks who does; nobody has been
picked, because there is no Orchestrator.

---

### 🔴 F-5 · MAJOR · No Scientist checkout carries the protocol that defines its blindness, and A and B hold the same uncommitted edit to the benchmark paper's manifest

**Review question 3 (contamination · hidden leakage · shared assumptions)**

Measured directly against the branch tips and the working trees, this session:

| Worktree | `roles/` | `governance/` | `scientist_reading_modes.md` | behind `main` | dirty |
|---|---|---|---|---|---|
| `lettore` (`scientist-a`) | **0** | **0** | **0** | 201 | **1** |
| `lettore-b` (`scientist-b`) | **0** | **0** | **0** | 203 | **1** |
| `lettore-c` (`scientist-c`) | 4 | 22 | **0** | 65 | 0 |

🔴 **Zero of three Scientist checkouts carry the protocol that defines MODE A, MODE B, the blind
first pass, `PARALLEL_READ_GROUP`, the ban on relayed content, and the freeze ordering.** OBJ-2's
N-7 measures this for A and B. It does not measure it for C, and C is the one the records call
*"the healthiest of the three"* — it carries 22 governance files and still not this one, because
the protocol landed at `4454fea` on 2026-08-19 and `lettore-c` is 65 commits behind.

🔴 **The dirty file is the same file, and the content is byte-identical.**

```
lettore  /disease-models/wwox/research/deepdive_manifests/PMID42422765.json
lettore-b/disease-models/wwox/research/deepdive_manifests/PMID42422765.json
  working-copy sha256   6c3fe60fa09cdb8f4b957a20801751673e5bad66d84fb51b843ef60bcf888b83   ← identical
  committed blob        5888cf44be5dc7bf47b6ed3774c1450b1c65bf1f                           ← identical
```

PMID 42422765 is the paper `scientist_reading_modes.md` § 2.4 **special-cases by name**: the first
Task Contract naming it must cite `HANDOFF-C-2-PMID42422765` and declare single-owner versus group
member, and a contract omitting that is refusable by the actor.

**And the modification is uncommitted, so no ref carries it.** OBJ-1 § 2.1 and OBJ-2 § 2.2 both
declare the git object database as their surface. A reviewer restricted to that surface — which is
what both records are, and what this review was until I read the working trees directly — **cannot
see it.** I found it only by running `git status` inside each worktree.

**Why this is the sharpest contamination finding available.** Both records correctly state that
independence is *a property of the surface, not a promise*, and OBJ-2 § 5.4 enumerates precisely
what each instrument does and does not guarantee. The surface they mean is the enumerated,
digested input packet under `files/` — and `.gitignore:7` is `files/`. So **the one property both
records name as the guarantee is carried by no ref, verifiable by no cross-ref read, and
reproducible by no reviewer.** The three `verify` instruments bound the window from inside the
surface; nothing outside it can confirm that the window was the one described.

**Premature consensus, mechanically.** Two readers whose checkouts hold the same uncommitted bytes,
neither of whom can read the protocol forbidding shared prior output, produce agreement that is
indistinguishable from independence. OBJ-2 § 9.4 states the rule that would price this correctly —
*"two readers agreeing on an overshoot is two overshoots"* — and states it about the readings, not
about the surface that produced them.

---

### 🟠 F-6 · MEDIUM · Premature consensus is already measurable one layer above the Scientists, and its cause is a shared instrument at a ref-local default

**Review question 3 (premature consensus · synthesis bias)**

Three records, three sessions, three seats, three refs, **one wrong number**: OBJ-0, OBJ-1 and
OBJ-2 each independently report the lease population as *"five leases … most recent released
2026-08-18T14:05:20Z."*

The mechanism is not communication and is not carelessness. It is a **shared instrument invoked at
a ref-local default**:

```
framework/scripts/lease_state.py:   DEFAULT_HOME = "runtime/orchestrator_lease.md"
```

Relative to the working directory. Each session ran it in its own checkout, received an answer that
was **locally correct**, and reported it as a repository-wide fact. Three-way agreement here carries
no more information than one measurement, because all three measurements are the same measurement.

**This is the failure the A/B benchmark exists to expose, occurring in the layer that designs the
A/B benchmark.** OBJ-2's own § 9.4 supplies the correct pricing and does not apply it reflexively;
OBJ-1's own § 2.1 supplies the correct scoping rule — *"`NOT_FOUND` across 44 refs is not
`NOT_EXIST`"* — and applies it to nine object classes in § 2.3, of which the lease is not one.

**The discipline is real where it was applied.** OBJ-2 declares `verdict_transfer: NONE`,
re-measured the approval queue instead of accepting OBJ-1's report, and got a different and better
number. The gap is not that the practice is absent. It is that **nothing selects which measurements
get it**, so it is applied to whatever the author happened to distrust.

### 🔴 F-6b · The same shape, measured a third time, in the one block that carries a positive control

OBJ-1 § 3.5 states the executable-coupling census and controls it:

```
OBJ-1:   framework/scripts 51 · scripts 35 · governance/scripts 3   = 89
         POSITIVE CONTROL  grep -c 'def ' framework/scripts/legend_lint.py → 26  (instrument working)

re-derived this session, same ref 788c357, tracked files only, no untracked .py present:
         framework/scripts 51 · scripts 37 · governance/scripts 3   = 91
         POSITIVE CONTROL  grep -c 'def ' framework/scripts/legend_lint.py → 26   ← reproduces exactly
```

**The control reproduces and the count does not.** `scripts/` holds 37 `.py` files at `788c357`,
not 35, measured against the git tree and against the working tree, which agree.

🔴 **A positive control validates the instrument it controls for, and OBJ-1's controlled the
content-matching step while the error was in the population step.** The grep worked; the
enumeration of what the grep was run over did not. The conclusion — *0 executables read
`learning/` or `reviews/`* — survives intact, because 0 of 91 is still 0.

That is the third instance in these two records of the same shape, and it is the shape that
matters most for an architecture whose reviews are counts: **F-1** (verdict right, population
short by 4 of 9), **F-2** (mechanism named, mechanism absent), **F-6b** (control passed, denominator
off by 2). In each case the number was checked and the set underneath it was not. **Two counts that
agree are not a second measurement if both were taken over an unexamined population** — which is
the same failure the A/B benchmark is built to expose in readings, appearing here in the layer that
builds it.

---

### 🔴 F-7 · MAJOR · Memory does not disappear; it stops at the ref boundary, and the boundary that was adjudicated to matter currently buys nothing

**Review question 4 (memory loop)**

| Namespace | domain | merging moves a candidate hash? | on `main` | total across refs |
|---|---|---|---|---|
| `reviews/` | CONTROL_PLANE | **no** | **3** | **74** |
| `learning/` | CONTENT | **yes** | 11 | 81 |

`CLASS-P51-REVIEWS-LEARNING-001` was operator-adjudicated MAJOR on 2026-08-17 on a fixed-point
argument: a review bound to the hash of the candidate it judges cannot sit inside that hash, or
Gate 5 could never be satisfied. **The argument is correct.** But the hash-free class and the
hash-bearing class are **equally unconsolidated** — 4% and 14% on `main`. The binding constraint is
not that merging is expensive. It is that **nothing merges**, and against that constraint the
CONTROL_PLANE/CONTENT partition changes no observable outcome today.

**Where memory disappears: nowhere. Where it is not retrieved: at the ref.**

```
TEST 1 (re-derived)       0 of 91 executables read learning/ or reviews/
                          — 91, not OBJ-1's 89. See F-6. The conclusion is unaffected.
TEST 2 (re-measured)      active_lessons/  → 0 files, 0 refs of 37 — and CLAUDE.md § 1's single
                          pointer in the router loaded every session points AT THAT PATH
TEST 3 (re-measured)      LEARNING_INDEX   → 0 files, 0 refs of 37
TEST 4 (this review)      a reader standing on `main` finds 3 reviews and 11 learning records
                          out of 155 written
```

**The reviewing seat is the sharpest instance.** Branch `mirror` is 65 commits behind `main` and
does not carry `scientist_reading_modes.md`, `controlled_benchmark_ab.md`, `lease_state.py`,
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`, any `CAND-*`, or `runtime/` at all. **The actor
whose declared mandate is memory holds a corpus of 50 reviews and 34 learning records on a ref that
carries neither the protocols nor the decisions those records are about.** Mirror's memory and the
objects Mirror's memory is about are on disjoint refs.

**Where lessons are not retrieved, and the one channel that works.** OBJ-1 § 5.4.4 names FC-4 as
the single measured instance of propagation — the `NOT_FOUND ≠ NOT_EXIST` rule, which travelled
*through the operator writing it into the next prompt.* I can confirm the same channel and no
other: that rule appears in OBJ-1 § 2.1, OBJ-2 §§ 2.4–2.5, and **in the dispatch that commissioned
this review**. Zero repository mechanisms carried it. The working channel is a human retyping a
lesson, which is F-3's transport cost wearing a different hat.

**Where old mistakes repeat.** F-2 is one; my own zsh sweep is another; OBJ-1's own R-6 enumerates
four more. Six instances of one class. The guard —
`PROV-POSITIVE-CONTROL-BEFORE-NEGATIVE-FINDING` — is registered at
`governance/design_records/materialization_log.md:1026`, in a namespace neither E.6 nor E.2 names,
read by no script, cited by no entrypoint, and held `PROVISIONAL` by an expiry event
(*"Mirror's first coordination review"*) that has never occurred and that no single actor may
schedule. Annex E.3 states *"Mai provisional per sempre."* It has been provisional since it was
written.

---

### 🔴 F-8 · MAJOR · At 5 papers the coordination layer already consumes 100% of throughput; the scaling term is actors × sessions, not papers

**Review question 5 (5 → 5000)**

```
2026-08-16 → 2026-08-22, all refs
  commits                                                             324
  touching governance/ learning/ reviews/ ledger/ runtime/ roles/     311   (96%)
  touching framework/state/ or disease-models/                          0   (0%)
  growth anchors, run this session   claims=39 · papers=70 · corpus=356 · literature=390   PASS, unchanged
  receipts, run this session          128 chained, tail anchored                            unchanged
  papers read                                                           0
```

**The 5 → 5000 question is not answerable as posed, because the system has not yet processed 1.**
Six days of an eight-actor laboratory produced 324 commits, 7 canonical batches, 74 reviews, 81
learning records, 9 lease rows and zero scientific state transitions.

**Bottleneck.** It is not per-paper cost. The coordination layer's work is `O(actors × sessions)`,
serialized behind **one** lease and **one** human transport edge, while the scientific layer's work
is `O(papers)` and has not started. Multiplying papers by 1000 does not touch the term that is
currently binding.

**Cost explosion, from the record rather than from a model.** Lease #9's `RELEASE_REASON`
enumerates the post-batch validation actually performed for **one** candidate: two tree
comparisons, a 533-path content diff, hash reproduction against the new canonical main, 65 suites /
950 tests compared **set-wise, by test name and normalised failure reason, not by count**, LINT,
publication gate, growth anchors, 128 receipts, four fingerprints — plus D.4's mandatory
`SNAPSHOT → APPLY → POST-COMMIT VALIDATE` and D.3's `GATE 0`. D.5 fixes batch size at *"smallest
coherent auditable unit."* That fixed cost is per batch, and it does not amortize.

**Review explosion, concretely.** The reading acceptance test is five steps; steps 1–4 are
mechanical and their tools exist. **Step 5 — the blind locator audit over every
(proposition, snippet, anchor) triple — has no executable form**, and OBJ-2 § 7.3 names it as *"the
step that is skipped first under time pressure."* Its cost grows with total triples, not with
papers. The instrument OBJ-2 § 9.4 assigns to it is *blind agents* — whose blindness is the one
property no ref can carry (F-5).

**Coordination collapse, with a name.** `MIRROR_SAMPLED` is the perimeter for ordinary batches
(G.1). Searched across all 37 heads: it appears in exactly **three files** — `GOVERNANCE_v3.1.1.md`
§ 29.1, `annex_g_mirror.md` § G.1, `roles/mirror.md` — and all three merely restate the
`MIRROR_REQUIRED | MIRROR_SAMPLED | NO_MIRROR` enumeration. **No sampling rate, fraction, cadence
or trigger is defined anywhere.** The nearest thing is body § 41, which lists *"sampling Mirror"*
among the purposes of the first cycle — a purpose, not a parameter. At 5 papers the omission is
invisible. At 5000 it is the difference between reviewing everything and reviewing nothing, and
G.2 bars Mirror from setting it alone.

🔴 **And both records under review state that further analysis cannot move any of this** — OBJ-2
§ 8.3: *"Nothing in the NOT_READY column is unblocked by more analysis. Iterations 2 and 3 of this
task cannot move any of it."* Both were nonetheless produced as **iteration 1 of 3**, and this
review is **iteration 1 of 3**. The coordination layer is scheduling its own continuation against
its own finding. That is the collapse mode, and it is already running.

---

### 🔴 F-9 · MAJOR · Both records are `learning/`, declare themselves non-governance, and are shaped as sequencing instructions with colliding identifier namespaces

**Review question 6 (governance drift · accidental authority · temporary rules)**

Both records disclaim governance repeatedly and in good faith — OBJ-1 § 11 and OBJ-2 § 11.2 are
eleven- and ten-line enumerations of what they do not do. **And both close with an ordering
statement in the imperative voice of a plan:**

> OBJ-1 § 10.1 — *"Nothing else in this list is downstream-blocked by as much."* · *"Two of these
> five are one-way doors."*
> OBJ-2 `NEXT_TRANSITION` — *"B-1 and B-2 gate everything downstream."*

**Both mint identifier namespaces with no registry, and the namespaces collide:**

| Identifier | In OBJ-1 | In OBJ-2 |
|---|---|---|
| `B-1` | *No `ACTIVE` lease* | *Role contract activation* |
| `N-1` | *the approval queue exists in three non-nested versions* | *No Task Contract owned by any scientist exists* |
| `R-1` | a **risk** | a **readiness** item |

Same day, sibling branches, same architecture. **Neither record can cite the other's identifiers
without ambiguity**, and a third reader citing `B-1` says nothing until they also say which record.
OBJ-1 creates `HG-1…HG-12`, `N-1…N-4`, `B-1…B-6`, `R-1…R-11`; OBJ-2 creates `U-1…U-7`, `B-1…B-16`,
`Q-A…Q-H`, `N-1…N-7`, `A-1…A-9`, `R-1…R-7`. Sixty-plus identifiers, zero registries, zero owners.

**The drift path is named by the record it threatens.** OBJ-1's R-1, quoting the operator decision:
*"a check never formally adopted, but consulted at every dispatch until 'reconstruction says
BLOCKED' becomes the operative reason a task does not proceed — a gate with no adoption record."*
The measured transmission channel for exactly that is FC-4: **the operator writes it into the next
prompt.**

🔴 **This dispatch is an instance.** It names `"Orchestrator coordination protocol"` and
`"Plan scientist pipeline model"` as though they were repository objects. Neither phrase exists on
any of 37 heads, as file, candidate, protocol or identifier. They are the operator's names for two
`learning/` records that both state they define nothing. **A record that defines nothing has been
addressed as a protocol and a model within hours of being written**, which is drift measured on the
instrument that named drift.

**Temporary becoming permanent, two measured instances:**

```
Q-1   originates inside PROPOSAL-ORCH-STATE-RECONSTRUCTION, which
      DEC-20260822-ORCH-STATE-RECONSTRUCTION-CANDIDATE placed in
      OPTION B — HELD_AS_CANDIDATE · "No further work is authorized."
      Q-1 is now cited across four records and sits at the head of OBJ-1's dependency order.
      A question inside a held candidate has become the repository's most-cited blocker with
      no act that ratified it.

#3    lease #3 carries STATUS: EXPIRED — a value Annex I.3 does not define (ACTIVE|STALE|RELEASED).
      Deliberately not normalised, correctly, because a record edited to agree with its own
      derivation has stopped being evidence. The consequence is permanent: an undefined vocabulary
      term is now in the record forever, and `lease_state.py --check` returns exit 1 on every
      clean run. A gate whose PASS is "exit 1 with two known findings" trains its readers to read
      a non-zero exit as normal — which is the condition under which the next, real finding is
      not seen.
```

---

### 🟠 F-10 · MEDIUM · The one gate whose failure is externally irreversible is prose, and its backlog is 455 commits

**Review question 1 (human gates) · 6 (drift)**

`HG-4` (public push) is `public_release_gate.py` **plus** a human reading
`git diff origin/main..main --stat` — described in the repository as *"the one judgement no gate
makes."*

```
origin/main   8ab8e4b   2026-08-01T10:30:33+0200
main          788c357   2026-08-22
origin/main..main       455 commits unpushed, 21 days
```

Every other gate in the system fails **inward** — a batch aborts, a candidate is rejected, a lease
expires, and D.4's `SNAPSHOT → restore` recovers it. `HG-4` is the only one whose failure leaves
the repository and cannot be recalled, in an edition whose entire privacy design is the layering
that keeps the individual-level record out. It has no carrier, no record class, no ledger entry and
no `APPROVAL_ID` type of its own beyond J.3's generic set, and the backlog it is asked to judge has
grown to 455 commits across a period in which 96% of commits were coordination artifacts written by
eight actors on 37 branches.

**Sizing is not measured and I do not claim it.** What is measured is that the reviewable surface
grows monotonically while the reviewing act stays a single human reading a `--stat`, and that both
records' human-gate accountings list `HG-4` as *"per push"* without noting that the per-push cost
is a function of how long since the last one.

---

## WHAT_WOULD_CHANGE_MY_MIND

*Declared falsifiers, per finding. Each is a specific measurement, not a standard of proof.*

| Finding | Falsified by |
|---|---|
| **F-1** | A ref other than `orchestrator` carrying lease rows #6–#9; **or** a normative clause I did not find that scopes the I.3 singleton to a single declared seat and names which one; **or** a demonstration that `lease_state.py` reads across refs rather than `DEFAULT_HOME` relative to CWD. Any one kills the finding. |
| **F-2** | `governance/plan_defined_parameters.md` at `788c357` **not** containing `- reviews/` under `CONTROL_PLANE_ROOTS`; **or** a second `CONTROL_PLANE_ROOTS` declaration elsewhere that omits it and is the operative one. I searched the file: one occurrence, line 258. Show me a second and F-2 falls. |
| **F-3** | A durable record — any ref, any path — in which one actor addressed another actor directly and the recipient acted on it without an operator dispatch between them. **One instance falsifies the "100% of edges" claim.** I found none across 324 commits; I did not read chat transcripts, and a transcript is not a repository object. |
| **F-4** | A recusal clause for challenge adjudication anywhere in the body or annexes; **or** any artifact under any name that performs the F.3 `OVERRIDE → VALIDATED_LATER` analysis; **or** an assignment of `MIRROR_RETROSPECTIVE` cadence `N` to any owner. |
| **F-5** | `scientist_reading_modes.md` present at the tip of `lettore`, `lettore-b` or `lettore-c`; **or** a rule stating that a Scientist reads its protocol from the benchmark input surface rather than from its worktree, which would make the absence correct by design rather than a gap. **The uncommitted-identical-bytes half is not falsifiable by argument** — the two sha256 values are equal or they are not. |
| **F-6** | Any of OBJ-0, OBJ-1 or OBJ-2 qualifying its lease statement with a `MEASURED_AT` scoping it to its own ref. All three state it unqualified; show me one that does not. |
| **F-6b** | `scripts/` containing 35 rather than 37 `.py` files at `788c357`. I measured the git tree and the working tree separately and they agree at 37; a third route disagreeing would put the error on my side. |
| **F-7** | A merge commit, on any ref, moving `reviews/` or `learning/` records from an actor branch onto `main`; **or** any executable in the repository that reads either namespace. I measured 0 of 89 executables and re-ran the positive control. |
| **F-8** | One commit between 2026-08-16 and 2026-08-22 touching `framework/state/` or `disease-models/`. **A single one falsifies the 0%.** I measured across all refs, not only `main`. Also falsified by a defined `MIRROR_SAMPLED` rate anywhere in the normative surface. |
| **F-9** | An identifier registry for `HG-*` / `N-*` / `B-*` / `U-*` / `Q-*`; **or** a repository object named `"Orchestrator coordination protocol"` or `"Plan scientist pipeline model"`; **or** an adoption record for `Q-1` outside the held candidate. |
| **F-10** | An `APPROVAL_ID` of type `DESTRUCTIVE` or a dedicated record class covering a public push; **or** a scheduled cadence for it. |

**What would change my mind about the review as a whole.** The two records are honest, and the
findings above are about what could not be seen from a single ref plus what the architecture does
to an actor who behaves exactly as these two did. If a mechanism exists that carries state across
refs without an operator — one I failed to find across 37 heads — then F-1, F-3, F-6 and F-7 are
one finding about my own sweep and not four about the architecture.

**And this review inherits its own F-1.** Every negative claim here is scoped to 37 local heads in
this clone at the stated instant. `refs/codex` (4) and `refs/stash` (1) were not enumerated. A
clone, a remote or a codex ref I cannot see is outside every claim above.

---

## NEXT_TRANSITION

```
FROM   iteration 1/3 — hostile review delivered. 10 findings, all re-derived this session.
       No design produced. No repair proposed. No replacement architecture offered.
       No governance object touched. No actor directed. No paper read.

TO     nothing this actor can enter.
```

**What is owed, and by whom — stated as obligations that already exist, not as requests.**

```
Annex C.2   AUTHOR_RESPONSE is MANDATORY and "il silenzio non è accettazione".
            Two authors, on two branches, neither reachable from here.
            🔴 There is no channel. This review's own delivery is F-3's transport problem,
               and I cannot solve it from inside the finding.

C.3         This review was opened by an operator dispatch, not by Orchestrator, because
            there is no Orchestrator. That defect is in the review, is declared, and is
            not curable by the reviewer.
```

**What iterations 2 and 3 of this task could measure that iteration 1 did not:**

```
NOT MEASURED   refs/codex (4) and refs/stash (1) — content not enumerated
NOT MEASURED   whether the three HUMAN_APPROVAL_QUEUE versions can be reconciled without loss,
               or whether the divergence has already produced a decision recorded in one place
               and contradicted in another
NOT MEASURED   the uncommitted working-tree state of the remaining 13 worktrees. I read 6.
               F-5 was invisible from git objects; the same class may be present elsewhere.
NOT MEASURED   whether any Codex worktree holds scientific work that would collide with a
               first batch — body § 41 forbids double work with the Codex worktrees, and four
               Codex worktrees carry PMID-named branches
NOT MEASURED   PROPOSAL-C9-STATE-MODEL, read here only through OBJ-1's Q-10
```

**The state this record leaves behind.**

```
Nothing is activated, assigned, adopted, resolved, repaired or authorized.
One file is added, on branch `mirror`, under H.1 WORK_COMMIT — which requires no lease.
main is unchanged. No governance, roles, framework, ledger or runtime path is written.
No candidate is created. No gate is asserted. No scientific artifact exists that did not before.

`reviews/` is CONTROL_PLANE, so this file moves no CANDIDATE_CONTENT_HASH — verified at
main@788c357:governance/plan_defined_parameters.md:261, which is F-2.

Iteration 1 of 3.
```

---

## WHAT THIS REVIEW DOES NOT DO

- It does **not** design, repair, or propose a replacement architecture — the dispatch forbade all
  three and no finding above carries a remedy.
- It does **not** resolve `Q-1…Q-10`, `O-1…O-6`, `N-1…N-4`, `Q-A…Q-H` or `U-1…U-7`.
- It does **not** rule on whether any role contract or protocol binds.
- It does **not** activate, register, or verify any actor or capability.
- It does **not** assert `CONFIRMED` on any object, and `WEAKENED`/`REFINED` are C.2 verdicts on
  the records reviewed, not determinations of anyone's authority.
- It does **not** constitute an `AUTHOR_RESPONSE`, a Session Learning Record under Annex E.6, a
  `MIRROR_UPGRADE_PROPOSAL` under G.2, or a `MIRROR_RETROSPECTIVE` under G.3.
- It does **not** attest any lease lifecycle. `OBS-LEASE-DETECTION-GAP-001` still stands and F-1
  extends it rather than closing it.
- It is **not** a `WORK_COMMIT` toward a candidate and **not** a `CANONICAL_BATCH_COMMIT`.
