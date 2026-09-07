---
artifact: LEGEND learning — REHEARSAL vs GOVERNED EXECUTION across the scientific workflow
analysis_id: SWMA-v1
version: 1
authored_by: scientist-c
authored_in: worktree lettore-c, branch lettore-c, HEAD 908197b
authored_on: 2026-08-24
governance_version_in_this_checkout: 3.1.1
authority: none — this is an analysis. It assigns nothing, activates nothing, and amends nothing.
mode: REHEARSAL
standing: none — retained, not evidence
absent_objects: [TASK_ASSIGNMENT, TASK_ACK, TASK_CLAIM, CHECKPOINT, LEDGER_EVENT, REVIEW]
contamination_status: CLEAN with respect to the peer analyses — see § 0.2
independence_spent: none — no scientific source was opened for this work
---

# Scientific workflow modes — what can be done without governed state, and what cannot

## 0 · This document, first

### 0.1 · Its own standing

This file is a **rehearsal product** and says so in its frontmatter, because the argument below
would be self-refuting otherwise. No `TASK_ASSIGNMENT` names it, no `TASK_ACK` accepted it, no
`TASK_CLAIM` records an owner for it, no checkpoint binds it to a fingerprint, no event ledger
carries it, and no reviewer has been assigned to it. It is retained. It is not evidence.

That is not a disclaimer. It is the single finding this analysis rests on: **the mode of an act
is decided by which durable objects exist beside it, and by nothing else** — not by the
seriousness of the work, not by the vocabulary of the output, and not by the role the author
believes it holds.

### 0.2 · What was read to write it, and what was deliberately not

Read (all control-plane or normative, none scientific): the governance body and Annexes A, C, E,
H, I, J; `roles/scientist.md`; `framework/instruction/epistemic_discipline.md`;
`framework/master/gold_is_in_the_details.md`; the candidate, handoff and approval records in this
checkout. From branches this worktree is behind, read via `git show`:
`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md`,
`framework/protocols/scientist_reading_modes.md`, `runtime/agent_card_registry.md`,
`runtime/orchestrator_lease.md`, `framework/scripts/lease_state.py`.

**Not read, deliberately:** any output of `scientist-a` or `scientist-b` on this or any question;
`runtime/handoff/C-2/HANDOFF-C-2-PMID42422765.md` and its working JSON; any paper. The first
exclusion is what makes a convergence between the three analyses a signal rather than an echo
(body § 26). The second and third are refusals to spend independence — see § 5 — on objects this
task does not require.

Verified before claiming the first exclusion holds: `learning/scientist/` exists on **none** of
the seven branches checked out in the LEGEND worktrees, so there was no peer output to avoid
reading. Command in § 8.

---

## 1 · The state that decides the question

The question *"which activities need governed state?"* cannot be answered in the abstract while a
concrete answer is available, so the concrete state comes first. Every line here was executed in
this session; the commands are in § 8.

### 1.1 · "Governed" is not one switch — it is four layers, and they are in different states

| Layer | What it is | State, 2026-08-24 |
|---|---|---|
| **METHOD** | `framework/master/`, `framework/protocols/`, `epistemic_discipline.md` — parity of sources, locators, receipts, epistemic typing | **In force, and never depended on the laboratory.** `roles/scientist.md` states it: the scientific method "is not replaced by the governance and is not negotiable by it" |
| **INSTRUMENTS** | Annexes A–J — task contract, review ladder, commit gates, lease, approval queue, cost policy | **Installed and binding on their own terms** since commit `908197b`. `DEC-20260822` § SCOPE_LIMITATION is explicit: they "bind on their own terms, not through `roles/`" |
| **ROLE CONTRACTS** | `roles/scientist.md` and its three siblings | 🔴 **NOT ACTIVATED.** Operator determination `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`, OPTION B: the contracts remain `PROPOSED`; their status lines are "accurate, not stale"; "no actor authority may be assumed from these contracts" |
| **RUNTIME STATE** | lease, task record, claim, checkpoint, ledger event, review record | For `scientist-c`: **registered, unassigned.** The Agent Card exists; the task ledger is empty |

The fourth row, in numbers. Across the seven branches checked out in the LEGEND worktrees,
`ledger/tasks/` holds records for exactly **one** ACTOR_ID (`plan`, five task ids) and
`ledger/checkpoints/` for exactly **two** (`plan`, `mirror`). For `scientist-a`, `scientist-b` and
`scientist-c` the count is **zero task records and zero checkpoints, on every branch**. And
`DEC-20260822` E-10 records `lease_state.py` deriving **0 ACTIVE leases** — which, under
`CLAUDE.md` § 0, places any session reading it in `BOOTSTRAP_MODE`.

### 1.2 · What follows for this actor

`scientist-c` **is** a registered actor: `runtime/agent_card_registry.md` records the registration
of 2026-08-17, with `ROLE_CONTRACT_HASH` matching canonical and the
`APPLICABLE_GOVERNANCE_FINGERPRINT` recomputed inside this worktree rather than copied. Its
capabilities are all `UNVERIFIED`, and I.4 says Orchestrator assigns on verified capabilities.

Registration is therefore real and is not sufficient. **Identity without an assignment is not
governed execution** — it is an actor who can be addressed, working on nothing that has standing.
That gap is the whole subject of this document, and it is not a defect to be hidden: it is the
current, accurate state.

One further fact, recorded because it bears on how much weight this analysis can carry: this
checkout is at `908197b` (2026-08-16) while the root branch is at 2026-08-23, a diff of 74 files.
Two of the changed files are `roles/scientist.md` and `governance/plan_defined_parameters.md`, and
`plan_defined_parameters.md` § P2 is in `CORE` for every role. **The fingerprint under which
`scientist-c` registered is therefore necessarily superseded.** Annex A.6's refusal rule does not
literally bite — it governs *resuming a checkpoint*, and there is no checkpoint to resume — but
the condition it protects against is present: this analysis is written under a role contract that
is both non-binding and no longer current.

---

## 2 · The two modes, defined from the repository's own usage

### 2.1 · REHEARSAL

The word is already in this repository with a fixed meaning.
`dismech_blind_derivation_contract.md` § 7: a contaminated run "is retained as a rehearsal but is
**void as independent evidence**". `dismech_independent_derivation_design.md` § 2: "A run
performed by an actor with retained knowledge of the first pass **is a rehearsal, even if the
filesystem is clean**."

Generalised, and used in that sense throughout this document:

> **REHEARSAL** — an execution whose products are *retained* and carry *no standing*: nobody is
> answerable for them, nothing may be resumed from them, no other actor may rely on them without
> re-deriving them, and no canonical object may be built on them.

Three things a rehearsal is **not**. It is not sloppy — it can be performed at full method
strength, and § 4 argues that for some activities it must be. It is not secret — its products are
kept, which is precisely why they are dangerous. And it is not rare: the governance sanctions one
explicitly, the Orchestrator's L2 batch **dry-run** (body § 38, "snapshot + lint, senza commit"),
defined entirely by what it omits.

### 2.2 · GOVERNED EXECUTION

> **GOVERNED EXECUTION** — an execution carrying the objects that give an act standing:

```
1. an OWNER with a durable TASK_CLAIM                     (A.3)
2. DIRECTIVE_VERSION + GENERATION                          (A.4)
3. a CHECKPOINT bound to an APPLICABLE_GOVERNANCE_FINGERPRINT   (A.6)
4. durable milestone evidence persisted by WORK_COMMIT     (§11, §18, A.7)
5. an event on the append-only ledger                      (J.1)
6. review at or above the floor for its object class       (C.1)
```

### 2.3 · The rider that makes the distinction hard to police

**Governed execution is documentary, not enforced.** Annex J.0 lists what LEGEND does not
possess: no atomic task checkout, no runtime RBAC for interactive actors, no guaranteed singleton.
The lease record says it in one line — `VISIBILITY ≠ LIFECYCLE ENFORCEMENT` — and names its own
weakest layer `PROCEDURAL`: "writing a row at all … Nothing compels the Orchestrator to record an
acquisition, and nothing runs between turns."

Two consequences, and both matter more than they look:

1. **The modes are distinguished *ex post*, by looking for the six objects — never *ex ante* by a
   mechanism that refuses.** A rehearsal cannot be blocked. It can only be marked.
2. **A rehearsal product is byte-indistinguishable from a governed one.** Same Markdown, same
   tables, same vocabulary, same confident prose. The defence is not the artefact; it is the
   *separate* objects beside it. Which is why the failure mode below is structural rather than a
   lapse of care.

### 2.4 · The failure mode: rehearsal laundering

A rehearsal artefact, written in the vocabulary of governed output, gets harvested later and
treated as though it had standing. Nobody decides to do this; it happens because the artefact
looks the part and the objects that would have contradicted it were never written.

The repository has already paid for adjacent versions of this. `COR-20260816-GOV311-001` records
`plan` attributing a `PASS_WITH_NOTES` to the review it had read (`-002`, which actually reads
`REVISION_REQUESTED`) rather than to the review that carried the disposition — a citation, not the
object, and checkable in one command at the time. `gold_is_in_the_details` rule 8 names the same
hazard in the reading domain: hundreds of abstracts sitting locally "make answering from them
*feel* like working". And `DEC-20260822` rationale 1 refuses the largest possible instance of it —
reading an approval bound to a content hash as though it activated the meaning of the bytes inside
that hash.

---

## 3 · The criterion — four tests

**If any one fires, governed execution is required.** If none fires, rehearsal is not merely
permitted but preferable: it costs less and carries no ceremony.

| | Test | The question | Fires because |
|---|---|---|---|
| **T1** | **RELIANCE** | Will another actor, or a later session, build on this without re-deriving it? | Reliance on an unowned artefact is reliance on nothing (§ 18: "what is not in durable state did not happen") |
| **T2** | **ATTRIBUTION** | Must someone be answerable, so this can be challenged or reviewed? | Body § 2 attaches epistemic authority to *the responsible Scientist*. C.2 requires an `AUTHOR` and a mandatory `AUTHOR_RESPONSE`. A.3 is what makes an author exist |
| **T3** | **PROVENANCE** | Does later verifiability depend on something that must be captured **now**, while the surface is open? | Rules 5b–5e; the receipt contract; `deepdive_manifest.py` |
| **T4** | **CONSEQUENCE** | Does it spend, destroy, publish, bind canonical history, or reach a human as a decision input? | Body § 4 taxonomy; J.4 (`DEFAULT_EXTERNAL_SPEND = 0`); GATE 3; the four current files move only by `BATCH_COMMIT` |

### 3.1 · The asymmetry that gives the rule its shape

**T1, T2 and T4 are repairable late.** A rehearsal product can be adopted afterwards: assign it an
owner, open a review at its floor, put it through the gates. The cost is re-derivation, which is
work, not loss.

**T3 is not repairable at all.** A verbatim locator not captured while the document was open is
recoverable only by reopening the document. Rule 5b states the exchange rate and the date it was
paid: *"Capturing costs seconds, recovering costs the reading twice"* — on 2026-08-04 no verbatim
locator existed anywhere in the canonical state, and fourteen had to be recovered by reopening
papers already read.

> **The rule: rehearse where governance can be added later; never rehearse where it cannot.**

This inverts the intuitive ordering. The naive expectation is that reading a paper is harmless and
deciding is dangerous. The opposite holds: **a paper read in cheap rehearsal is the most expensive
rehearsal in the system**, because it burns the one thing that has to be contemporaneous — and, as
§ 5 shows, one thing that cannot be bought back at any price.

---

## 4 · The ten activities

Bands first, because the table is long.

```
BAND 1 · REHEARSAL_NATIVE          rehearsal is the right mode          → 4, 5
BAND 2 · REHEARSAL_UNDER_ANOTHER_NAME  possible; the product must not
                                    carry the governed word             → 6, 9
BAND 3 · REHEARSAL_AT_FULL_COST    possible only at full method
                                    strength; the cheap version
                                    destroys value                      → 1, 2, 3
BAND 4 · GOVERNED_ONLY             rehearsal yields nothing usable,
                                    or the act is barred                → 7, 8, 10
```

| # | Activity | Rehearsal possible? | Governed required? | Tests | What rehearsal spends irreversibly |
|---|---|---|---|---|---|
| 1 | Lettura paper | **Only at full method strength** | For the reading to *count* | T3, T1, T2 | Contemporaneous locator capture · **independence on that source** |
| 2 | Estrazione dati | **Only at full method strength** | For the extraction to *support* anything | T3, T1 | Locators · artefact placement in the shared `files/` |
| 3 | Costruzione evidenze | As a draft to be re-derived | Yes — provenance is Plan's to refuse | T1, T2, T3 | Nothing, if § 1–2 were done properly; everything, if they were not |
| 4 | Generazione ipotesi | **Yes, fully** | Only at *recording* — and at *discarding* | T1 (weak) | Nothing — **except the discards** (§ 4.4) |
| 5 | Confronto meccanismi biologici | **Yes** | At floor R1, R2 if therapeutic-actionable | T2, T4 | Nothing |
| 6 | Ranking evidenze | Yes, as *ordering* | Yes, when it **allocates work or excludes** | T4, T1 | Nothing, while it excludes nothing |
| 7 | Proposta drug repurposing | Only as internal hypothesis, no addressee | **Yes** | T4, T2, T1 | Nothing epistemically; the tools cost money, and money is T4 |
| 8 | Candidate generation | **Depends which of three objects** (§ 4.8) | Yes for two of the three | T1, T2, T4 | Nothing |
| 9 | Review scientifica | Yes, as **critique** — never as **verdict** | Yes for a verdict with standing | T2 | The reviewer's eligibility, if evidence was contributed |
| 10 | Produzione conclusioni | Only as a draft addressed to nobody | **Yes** | T1, T2, T4 | Nothing, provided the draft is not circulated as a conclusion |

### 4.1 · Lettura paper

Split the activity, because the two halves sit in different bands.

**Triage / abstract pass — rehearsal-native.** Rule 8 permits triage, ranking, census and export
pre-flight from an abstract corpus, and states its own limit in the same breath: *"un abstract non
è una lettura"*, and an `abstract_only` event clears no reading debt.

**Complete full-text read — band 3.** T3 fires hardest here, and the machinery that satisfies it
is *already available in any checkout*: `deepdive_manifest.py`, the receipt writer,
`fulltext_receipts.py`. Nothing about the laboratory's unbootstrapped state prevents a reading
from being done at full method strength today. What is missing is the other half — an owner, a
review, a ledger event — and that half is repairable late.

So the honest statement is not "do not read". It is: **a reading performed today will need a
governed owner tomorrow, and the only version of it that survives that transition without being
redone is the one performed at full protocol strength now.** A reading compressed for time or
tokens is explicitly forbidden in both reading modes, for the reason that "a reading shortened for
budget produces a receipt that overstates itself".

One caution specific to this moment. `scientist_reading_modes.md` § 2.2 requires that every
reading Task Contract name exactly one `OWNER`, that ownership is "never inferred from a worktree,
a branch, or a file someone happens to have open", and that two contracts on one source are legal
only under a declared `PARALLEL_READ_GROUP`. There are no reading Task Contracts at all right now.
An unassigned reading is therefore not a small deviation from that protocol — it is the
`DUPLICATED_ASSIGNMENT` risk with nothing in place to detect it, since detection runs over
`ledger/tasks/*/`, which for scientists is empty.

### 4.2 · Estrazione dati

T3 again, plus a trap that is about *location* rather than attribution.
`roles/scientist.md` states it flatly: an evidentiary artefact belongs in the **shared checkout's**
`files/`, and the validation that counts is the one re-run there — **"a branch carries the
manifest; it does not carry the evidence."**

An extraction performed in an isolated worktree, against an artefact only that worktree holds,
produces a manifest that validates against something no other actor can see. The validator passes.
The evidence is unreachable. This is the one failure in this list that *wears the badge of having
been checked*, which rule 5c identifies as the worst class of false positive the system can
produce.

### 4.3 · Costruzione evidenze

Evidence is the object class whose review authority is shared: `EVIDENCE → Scientist +
Plan/provenance` (C.4), and Plan may refuse it on structural or provenance grounds alone
(`INTEGRATION_BLOCK`, § 28) without touching its scientific meaning. A rehearsal cannot produce
that refusal, and therefore cannot produce its absence either — an unrefused evidence bundle that
was never offered to Plan is not a validated bundle.

Practically: the quality of a rehearsal evidence bundle is entirely inherited from activities 1
and 2. If the locators and receipts were captured at full strength, the bundle is a draft that can
be adopted. If they were not, it is a bundle whose provenance cannot be reconstructed without
redoing the readings.

### 4.4 · Generazione ipotesi — and the asymmetry inside it

**The most rehearsal-tolerant activity in the system.** A hypothesis asserts nothing: it is typed
`IPOTESI` by construction, it lands in a non-canonical append-only ledger, and its failure mode is
the cheap one. `epistemic_discipline.md` § 2: *"a false positive gets tested and dies. A false
negative is silent, permanent, and self-reinforcing."*

🔴 **But the same section makes the discarding of hypotheses the opposite case.** A fan-out that
generates thirty candidates and keeps five has produced **twenty-five negatives**, and every one
of them owes a `REVIVAL_TRIGGER` in the dismissal ledger, because "nothing dies in silence" and "a
rejection recorded anywhere else is a rejection nobody will re-scan".

> **Generating hypotheses rehearses safely. Discarding them does not.**

A rehearsal that keeps only its survivors is not a cheap version of the governed activity. It is a
silent, compounding loss, and it is invisible precisely because the output looks tidier.

### 4.5 · Confronto meccanismi biologici

Rehearsal-native as reasoning; the floor decides when it must be reviewed — R1 for an important L2
inference, **R2 for a therapeutic-actionable one** (C.1).

Note what does *not* relax in rehearsal: `PREMISE_TAG` on every load-bearing premise, the ban on
presenting `INFERENZA` as `DATO`, and the `DEFAULTS THAT BIT US` consultation before any
discarding. **Rehearsal suspends standing; it never suspends method.** The documented hazard here
is mechanistic over-transfer, and the repository's own worked example is a correction of exactly
that: the transfer of a degradation route observed for P252A onto Q230P, "itself corrected on
audit".

### 4.6 · Ranking evidenze

Rehearsal-able as *ordering*. It crosses into governed territory at two distinct points, and they
are worth separating because only one of them is obvious.

**When it allocates work.** Task, priority and reassignment are Orchestrator's under H.1. A
ranking that decides what gets read next is an operational directive wearing an analytical
costume — the analysis is the scientist's, the allocation is not.

**When it excludes.** `gold_is_in_the_details` rule 2: *"Ranking orders reading. It does not
replace or negate it. If a ranking ends up discarding a study, the ranking is broken — fix the
ranking, don't lose the study."* An exclusion is a negative, so § 4.4 applies to it in full.

### 4.7 · Proposta drug repurposing

Governed. Three independent triggers, any one sufficient:

- **Review floor.** Therapeutic-actionable inference → **R2 independent, semi-blind** (C.1).
- **Safety.** The BLOCK-1 gate, and the standing frame that nothing here is medical advice.
- **Cost.** The triage and hypothesis tooling reaches paid services, and J.4 sets
  `DEFAULT_EXTERNAL_SPEND = 0`: any spend is `HUMAN_APPROVAL` *before* the spend, inside a
  `BUDGET_ENVELOPE`. In practice this, not the review ladder, is what stops most of this activity
  today.

The reasoning behind a repurposing idea is band-1 hypothesis work and rehearses freely. What is
governed is the **proposal** — the moment it acquires an addressee who could act on it, T4 has
fired and the mode question is closed.

### 4.8 · Candidate generation — the question has three referents

🔴 The word names three different objects in this repository, and the answer differs by object.
This is a naming collision in the prompt, not in my reading of it, and it needs disambiguating
before item 8 can be answered as asked.

| Reading | Object | Rehearsal? | Why |
|---|---|---|---|
| **(a) `INTEGRATION_CANDIDATE`** | Plan's D.2 object with a `CANDIDATE_CONTENT_HASH` | **No** | A candidate exists *in order to be reviewed*. GATE 1 requires proponent ≠ executor; GATE 5 binds every approval to the hash. An unreviewable candidate is a category error, not a draft |
| **(b) COMMIT CANDIDATE** | the scientific queue object feeding `BATCH_COMMIT` | **As a draft only** | It proposes a change to the four current files; those move only by `BATCH_COMMIT` |
| **(c) therapeutic candidate** | a molecule or hypothesis in the portfolio | **Yes** | Identical to § 4.4, with § 4.7's gates on the way out |

### 4.9 · Review scientifica — the least rehearsal-able of all

Not because the prose is harder. Because **every property that gives a review its value is a
property of the assignment, not of the reviewer's writing**: opened only through Orchestrator;
rotation, never fixed pairs; `AUTHOR ≠ REVIEWER ≠ ADJUDICATOR`; a reviewer who contributed no
evidence to the object; at most two rounds before adjudication; and a **mandatory
`AUTHOR_RESPONSE`, because silence is not acceptance** (C.2, C.3).

A rehearsal can produce every one of the textual fields — `STEELMAN`, `KEY_OBJECTIONS`,
`WHAT_WOULD_CHANGE_MY_MIND`. It cannot produce an author obliged to answer, an adjudicator, or a
satisfied floor. So:

> **Rehearsal yields a critique. Governed execution yields a verdict.**

And the critique is worth keeping — an unassigned reader can find what assigned ones missed. The
error is not writing it; the error is filing it under `VERDICT: CONFIRMED`, which in C.2's own
words means only "no defect detected given the available evidence bundle", never "true".

### 4.10 · Produzione conclusioni

Governed, by three separate routes:

- **Attribution.** Body § 2 makes a conclusion the responsible Scientist's, "subject to review,
  never to an order". Without a `TASK_CLAIM` there is no responsible Scientist, so the conclusion
  is not merely *unreviewed* — it is **unreviewable and unchallengeable**, because C.2 needs an
  author and F needs someone to challenge.
- **Canonicality.** The four scientific current files change only through `BATCH_COMMIT`, and are
  never reconstructed from chat memory.
- **Floor.** By class, per C.1.

A *draft* conclusion is legitimate and normal. What cannot be rehearsed is the word: a conclusion's
purpose is to be relied upon, so T1 fires almost by definition, and a "conclusion addressed to
nobody" is close to a contradiction in terms.

---

## 5 · What rehearsal spends and cannot repay: independence

T3 covers effort that must be spent twice. This is worse, and it is not in the four tests because
it is not a test — it is a cost that is incurred silently and recorded nowhere.

`dismech_independent_derivation_design.md` § 2: **"A run performed by an actor with retained
knowledge of the first pass is a rehearsal, even if the filesystem is clean."** Independence is a
property of the actor's *history*, not of the process, the prompt or the working directory. It
cannot be restored by clearing a filesystem, reframing a task, or waiting.

Three rules already depend on it, and each is silently defeated by a prior rehearsal:

- C.3 — a reviewer **who contributed no evidence** to the object under review;
- body § 26 — semi-blind is "independence by task framing, not by information barrier", explicitly
  best-effort, so it cannot re-blind someone who has already read;
- `scientist_reading_modes.md` § 3.8 step 5 — the blind locator audit, whose auditor "receives
  triples + packet, never the dossier or the reader's name". Step 5 is named as "the one that
  catches a careful reading that says more than its source".

**And there are three Scientists.** For any object, the independent-reviewer pool is 2 once the
author is excluded. Each additional rehearsal on that object removes one more. **A rehearsal
performed by all three leaves zero, and no R2 semi-blind review of that object is possible inside
this laboratory — not harder, impossible**, because what was destroyed is unrecoverable by any
process.

This is the strongest argument in this document for marking rehearsals, and the strongest argument
against uncoordinated parallel rehearsal on any object that may later need independent review.

A live instance, stated because it is this session: three Scientists appear to have received the
same analytical question, on three branches, with the same output path. On a **methodological**
object that is benign, and § 26 makes convergence a signal — provided none of us read the others,
which is why § 0.2 declares that I did not. Had the object been a **paper**, the same arrangement
would have consumed the entire independent-reviewer pool for it in one afternoon, with no record
that it had happened. And it would have been an undeclared `PARALLEL_READ_GROUP`: legal only when
declared, and detectable only through `ledger/tasks/*/`, which for scientists is empty.

---

## 6 · The chain, kept separate — and where the mode boundary actually falls

The requested separation, mapped onto the repository's own instruments:

| Layer | LEGEND type | Review object (C.4) | Who owns it | Moves by |
|---|---|---|---|---|
| **Dato scientifico** | `DATO` | `EVIDENCE` → Scientist **+ Plan/provenance** | the reader, jointly with provenance | receipt · locator · manifest |
| **Interpretazione** | `INFERENZA` | `INFERENCE` → peer Scientist | the responsible Scientist | peer review at floor |
| **Ipotesi** | `IPOTESI` | *(no C.4 object)* | the responsible Scientist | append to a non-canonical ledger |
| **Decisione operativa** | — | 🔴 **none** | **Orchestrator** (task, priority) or **Operatore** (spend, MAJOR, strategy) | adjudication or approval |

Two observations fall out of the table, and both are structural rather than rhetorical.

**The fourth layer has no reviewer.** Annex C.4 names three review objects — `EVIDENCE`,
`INFERENCE`, `SYSTEM` — and *decision* is not among them. Decisions are **adjudicated** under H.1,
not reviewed under C. So the separation the operator asks to maintain is also a separation of
**who**: a Scientist never owns the fourth layer, and an analysis that slides from hypothesis into
recommendation has crossed an authority boundary, not merely an epistemic one. `ESPANSIONE`, worth
noting, is not a rung between hypothesis and decision — it is off to the side, "for strategy space
only", and cannot enter the current files without explicit promotion.

**The mode boundary does not run parallel to the layer boundary.** The naive model is monotonic:
data cheap, decisions governed. What the four tests actually produce is a **U**.

```
    governance
      required
         ▲
    high │ ███                                     ███
         │ ███  T3 · non-retroactive          T4  ███
         │ ███  capture, independence         T2  ███
     low │ ███         ░░░░░       ░░░░░          ███
         └──────────────────────────────────────────────▶
            DATO      INFERENZA   IPOTESI      DECISIONE
         (capture)                             (authority)
```

The left arm is mandated by **irreversibility**: what is not captured while the surface is open is
gone, and the actor's independence with it. The right arm is mandated by **authority and
consequence**. The trough in the middle is where governance can be added late, and that is exactly
where rehearsal earns its keep.

---

## 7 · One proposed micro-upgrade — `REHEARSAL_MARK`

Proposed, not adopted. `scientist-c` has no authority to introduce a protocol, and § 1 says why.
Routed for Mirror's epistemic judgement and Plan's durability judgement (H.1: "Lifecycle learning:
epistemico Mirror, durevolezza Plan").

**Problem it addresses.** § 2.3: a rehearsal cannot be blocked, only marked; and § 2.4: an unmarked
rehearsal is byte-indistinguishable from governed output and gets harvested as though it had
standing.

**Precedent.** The DisMech contracts already carry a `contamination_status` field which "attests
the hash of `second_derivation_authored.jsonl`, never a later reconciliation", and declares a
contaminated run "void as independent evidence". This generalises that field beyond one exercise.

Frontmatter block on every artefact produced outside governed execution:

```yaml
mode: REHEARSAL
standing: none — retained, not evidence
absent_objects: [TASK_CLAIM, CHECKPOINT, LEDGER_EVENT, REVIEW]   # which of the six are missing
contamination_status: CLEAN | CONTAMINATED   # and, if contaminated, what was seen
promotion_path: what would have to happen for this content to acquire standing
independence_spent: []   # objects on which this actor can no longer serve as independent reader
```

**`independence_spent` is the field that carries the load.** The other five are bookkeeping that
could be reconstructed later from the absence of the objects they name. Independence cannot: it is
consumed at the moment of reading, it leaves no trace in any ledger, and § 5 shows a pool of two
that three actors can empty in an afternoon without anyone noticing. **It is recordable only at
the moment it is spent** — which is the same argument rule 5b makes about locators, applied to the
reader instead of the source.

Failure modes, declared rather than assumed, per the transversal `GUARANTEE / FAILURE / DETECTION /
RECOVERY` rule:

```
GUARANTEE:  a rehearsal artefact cannot be read as governed output without contradicting
            its own frontmatter; independence expenditure becomes visible when incurred
FAILURE:    the mark is omitted — nothing enforces it (J.0: no runtime RBAC), which is the
            same PROCEDURAL layer the lease record already names as its weakest
DETECTION:  an artefact under learning/ or a working tree with no corresponding TASK_CLAIM
            and no mark; Plan sees this at reconciliation over ledger/tasks/*/
RECOVERY:   mark it late, or re-derive under a contract; late marking is honest and
            late independence accounting is not — by then the reader cannot remember
            what it had not yet read
```

---

## 8 · OBSERVED

Every line executed in this session, in `lettore-c` at `908197b`. Commands given so a reviewer
re-runs rather than reads.

| # | Observation | How |
|---|---|---|
| O-1 | The four role contracts are **not activated**; they remain `PROPOSED`; "no actor authority may be assumed from these contracts" | `git show legend-operating-convention-v1:governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` — OPTION B, operator determination, 2026-08-22 |
| O-2 | `scientist-c` **is** a registered actor since 2026-08-17: fingerprint recomputed inside this worktree, `ROLE_CONTRACT_HASH` canonical, session `86d4c569…` | `git show orchestrator:runtime/agent_card_registry.md` |
| O-3 | All declared capabilities of every actor were `UNVERIFIED` at the time that registry was written — "there are none, in any actor, of any role" | same file. `runtime/L2-OUTCOMES.md` exists on `orchestrator` and was **not** read; O-3 may have decayed |
| O-4 | **Zero task records and zero checkpoints for any Scientist, on every one of the seven branches.** Task records exist for one ACTOR_ID only (`plan`, 5 distinct ids on the root branch); checkpoints for two, counted as per-branch maxima (`plan` 19 on the root branch, `mirror` 8 on `mirror`) | `for b in legend-operating-convention-v1 evidence-index orchestrator mirror lettore lettore-b lettore-c; do git ls-tree -r --name-only $b \| grep -cE '^ledger/(tasks\|checkpoints)/scientist'; done` → `0` ×7 |
| O-5 | `0 ACTIVE` leases by derivation as of 2026-08-22; five records, all `STALE` or `RELEASED` | `DEC-20260822` E-10, quoting `python3 framework/scripts/lease_state.py`. **Not re-derived here** — this checkout has no `runtime/` and no `lease_state.py` |
| O-6 | The diff from this checkout to the root branch tip is **74 files changed, 20 679 insertions, 19 deletions**; it includes `roles/scientist.md` (M) and `governance/plan_defined_parameters.md` (M), the latter in `CORE` for every role → the registration fingerprint is superseded | `git diff --shortstat 908197b legend-operating-convention-v1` · `git diff --name-status 908197b legend-operating-convention-v1 -- governance/ roles/` |
| O-7 | A protocol directly on this subject exists and is **not in this checkout**: `framework/protocols/scientist_reading_modes.md`, whose own frontmatter reads "Until then it binds nobody" | `git show legend-operating-convention-v1:framework/protocols/scientist_reading_modes.md` |
| O-8 | `learning/scientist/` exists on **none** of the seven branches; no peer analysis was available to read, so § 0.2's `CLEAN` is verified and not merely asserted | `for b in …; do git ls-tree -r --name-only $b \| grep -c '^learning/scientist/'; done` → `0` ×7 |
| O-9 | The `learning/<role>/` layout is the established convention — counts are per branch, and the largest for each role is `plan` 10 (on the root branch), `mirror` 35 (on `mirror`), `orchestrator` 11 (on `orchestrator`). This file follows the layout rather than inventing a path | `for b in …; do git ls-tree -r --name-only $b \| grep '^learning/' \| cut -d/ -f2 \| sort \| uniq -c; done` |
| O-10 | `lettore` and `lettore-b` contain **zero** files under `governance/` or `roles/`: Scientists A and B are on branches that predate the governance installation | `git ls-tree -r --name-only lettore \| grep -cE '^(governance\|roles)/'` → `0`; same for `lettore-b` |
| O-11 | `runtime/handoff/C-2/` exists on `orchestrator`, containing a handoff for PMID 42422765 and a working JSON named for `lettore` and `lettore-b`. **Not opened** — see § 0.2 | `git ls-tree -r --name-only orchestrator \| grep '^runtime/'` |

## 9 · INFERRED

Reasoned, not observed. Each carries its load-bearing premise, per `PREMISE_TAG`.

- **I-1 · Every scientific act available to `scientist-c` today is a rehearsal, by determination
  rather than by choice.** O-1 removes the contract, O-4 removes the claim, O-5 removes the lease.
  `PREMISE: DATO` (O-1, O-4, O-5). *Boundary:* O-5 is quoted from a 2026-08-22 record, not
  re-derived here; a lease acquired since would change the lab's state and **not** this
  conclusion, which rests on O-4 independently.
- **I-2 · Governance is partially, not wholly, in force — and the parts are separable.** The
  instruments bind on their own terms while the role contracts do not.
  `PREMISE: DATO` — `DEC-20260822` § SCOPE_LIMITATION states it in those words.
- **I-3 · The role contracts' `status: PROPOSED` could not have been flipped inside the approved
  candidate.** `roles/` sits inside the content domain, so editing it changes the
  `CANDIDATE_CONTENT_HASH` the approval binds to. `PREMISE: DATO` — `DEC-20260822` E-4 verifies
  `roles/` inside the domain; P5.1 lists the control-plane roots. *This explains the mechanism and
  is expressly not an argument for activation:* `DEC-20260822` weighed and rejected that reading.
- **I-4 · The required-governance profile across the epistemic chain is U-shaped, not
  monotonic.** `PREMISE: INFERENZA` — derived from T3's non-retroactivity at the capture end and
  T2/T4 at the decision end. Falsifiable: name a middle-layer activity whose governance cannot be
  added after the fact, and the shape is wrong.
- **I-5 · Independence is the only quantity a rehearsal spends that no later act can repay.**
  `PREMISE: DATO` for the mechanism (`dismech_independent_derivation_design.md` § 2, C.3, § 26);
  `PREMISE: INFERENZA` for the pool arithmetic, which assumes the three-Scientist roster of body
  § 32 and no external reviewer.
- **I-6 · The dangerous half of hypothesis work is the discarding, not the generating.**
  `PREMISE: DATO` — `epistemic_discipline.md` § 2 on the false-negative asymmetry and the single
  named destination for `REVIVAL_TRIGGER`.

## 10 · OPEN QUESTIONS

- **Q-1 · Is the parallel assignment of this question to three Scientists a declared group?** If
  it is, the group should be named the way `scientist_reading_modes.md` § 2.2 requires. If it is
  not, three branches carry three different files at one path and the collision surfaces at
  integration. Either way it is currently undetectable: detection runs over `ledger/tasks/*/`
  (O-4). **Authority: Orchestrator.**
- **Q-2 · Does `runtime/handoff/C-2/` concern Scientist C?** The label `C-2` and the working file
  named for `lettore` and `lettore-b` point in different directions, and a filename is not
  evidence. Not opened. **Authority: Orchestrator.**
- **Q-3 · What is the correct mode vocabulary?** `scientist_reading_modes.md` already defines
  MODE A / MODE B *within* governed reading. This document adds an orthogonal axis (standing).
  Whether both belong in one vocabulary is a protocol question. **Authority: Plan (durability),
  Mirror (epistemic).**
- **Q-4 · Have capabilities been verified since O-3?** `runtime/L2-OUTCOMES.md` exists and was not
  read. It bears directly on whether anything can be assigned to `scientist-c` at all (I.4).
- **Q-5 · Should this checkout be brought up to the root branch before further work?** O-6 says
  the governance surface under which `scientist-c` registered has moved, including its own role
  contract. **Authority: Orchestrator.**
- **Q-6 · Does `REHEARSAL_MARK` (§ 7) survive contact with a hostile reviewer?** Its own failure
  mode is that nothing enforces it — the same `PROCEDURAL` weakness the lease record names.

## 11 · NON DECIDED

Explicitly not done, not authorised, and not implied by this document — the scope discipline is
borrowed from `DEC-20260822` and is not decoration.

- **No activation of anything.** § 1's reading of `DEC-20260822` is a citation, not a
  re-determination; this document does not resolve, weaken or reopen it.
- **No claim of authority.** `scientist-c` claims no task, no capability and no reviewer role.
  Nothing here is a `TASK_ACK`, a `TASK_CLAIM` or a checkpoint.
- **No protocol.** § 7 is a proposal at `OBSERVED`/`LOCAL` in Annex E's lifecycle. Not
  `PROVISIONAL`, which would need `SUCCESS_CRITERION`, `FAILURE_CRITERION`, `EXPIRY` and
  `ROLLBACK`, and an owner who can set them.
- **No amendment.** No frozen text, no annex, no role contract, no `*_current.md` is touched. No
  extension field is introduced into Annex A.
- **No scientific conclusion.** No paper was opened; no claim, evidence, hypothesis or ranking is
  produced, revised or withdrawn. Nothing here touches the WWOX model.
- **No verdict on any actor.** O-10 and O-11 are facts about branches, not judgements about
  `scientist-a`, `scientist-b` or `orchestrator`, whose contexts I have not seen.
- **No answer to Q-1…Q-6.** Each is routed to the authority that owns it under H.1.
- **No self-promotion of this file.** It is a rehearsal product. It acquires standing only by an
  act this document cannot perform.
