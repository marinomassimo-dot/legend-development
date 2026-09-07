---
record_type: TRIAL_EXECUTION_PROTOCOL
record_id: LEGEND-FIRST-OPERATIONAL-TRIAL-EXECUTION-PROTOCOL-V1
trial_id: TRIAL-001
task_id: FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1
title: First operational trial of LEGEND — executive protocol, evidence layers, and the primary unit of measure
author: unregistered session — no role contract, no ACTOR_ID
session_ref: legend-public-2a [cea07c]
actor_id: NOT ESTABLISHED — a session cannot resolve its own actorhood (OPCON-v1 § S.1.2)
dispatcher: operator
date: 2026-08-23
status: PROPOSED
binding: NO
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none
governance_version: 3.1.1 — read, cited, not exercised and not modified
measured_at: >
  branch `legend-operating-convention-v1` @ 30cb4f3fd700e2aaf6b608e363438f883ddc3760
  (3 commits ahead of `main` @ 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5, 0 behind),
  2026-08-23T20:14Z–20:31Z. Every figure below names the command that reproduces it.
supersedes_in_function: >
  learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md — as the *executable* record.
  The design is NOT withdrawn and NOT deleted: it remains the reasoning behind the choices this
  protocol executes, and its § 10 findings T-1…T-7 stay open and uncorrected here.
consumes_by_blob: >
  design      9d744eb7a284c80b7a6a2e1258fd04f1c9d44036  (TRIAL_DESIGN_v1, untracked working copy)
  sequence    959b57f4c93ccaed087338e5eaf60677fbbcf5c4  (FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001)
  Both hashed with `git hash-object` at the instant above. B.4 H-1b: an integration declares the
  blob of every source it consumed.
domain: >
  CONTENT. `learning/` is not among the exhaustive CONTROL_PLANE_ROOTS of P5.1, so this record sits
  inside the CANDIDATE_CONTENT_HASH of any future candidate rebased onto this branch. Disclosed.
class: WORKING RECORD (OPCON-v1 § B.1.2 row 7)
not_an_slr: >
  Not a Session Learning Record. Annex E.6 governs `SLR-*`; the name is deliberately not `SLR-`.
---

# LEGEND — FIRST OPERATIONAL TRIAL · EXECUTION PROTOCOL v1 · `TRIAL-001`

> **PROTOCOL ONLY · NOT AN AUTHORIZATION · ACTIVATES NOTHING · ACQUIRES NOTHING**
>
> This record specifies how the trial is run. It dispatches nobody, registers no actor, lifts no
> hold, issues no Task Contract, acquires no lease, acquires no paper, adopts no convention and
> writes to no canonical file. `main` is untouched and is not written by any phase of the protocol.

---

## 0 · What this record changes relative to the design

Three things, and nothing else.

| # | Change | Where | Why |
|---|---|---|---|
| **C-1** | 🔴 **The binary full-text model is retired.** `FULL_TEXT_AVAILABLE / NOT_AVAILABLE` is replaced by three layer statuses plus a criticality flag. | § 2 | Operator correction, 2026-08-23. And it is *measured* to be the right correction — § 2.4 |
| **C-2** | **The primary unit of measure is defined, and it is not time, tokens or files.** It is **auditor-minutes per VERIFIED CLAIM**, and `VERIFIED CLAIM` is defined *before* the metric that counts it. | § 5, § 6 | A metric whose numerator is defined before its denominator measures effort, not result |
| **C-3** | **The protocol is executable step-by-step**: entry criteria, blocking criteria, phase-by-phase artifacts, Mirror's and Plan's exact trigger points, and what remains useful when the trial fails. | § 3, § 4, § 8, § 9, § 10, § 12 | The design decided *what*; this decides *how*, in an order someone else can run |

Everything else the design established — the paper, the two arms, the write allowlist, the failure
modes, the nine operator decisions, the seven open findings — is **carried unchanged and not
re-argued**. Where this record re-measures a design figure, it says so and gives both numbers.

---

## 1 · The mandate constraints, and how each is discharged

Reproduced from the operator's instruction, each with the mechanism in this protocol that holds it.

| Constraint | Mechanism | Where |
|---|---|---|
| **PMID 28123895 stays the principal candidate** | fixed as the trial input; re-measured `NEVER_ANALYZED` today at 0 of 8 analysis surfaces, positive control 5 of 8, negative control 0 of 8 | § 3.1, § 15 |
| **No data acquisition without declaring the method** | Φ1 cannot begin until `TRIAL-001-ACQUISITION-DECLARATION.md` exists, naming route, tool, identifier, licence basis, executor and the digest of what arrived. **An acquisition performed before its declaration voids the input**, and Φ1 restarts | § 8 Φ1, § 4 B-3 |
| **No inference without available evidence** | § 5 condition V-4: a statement whose supporting layer is `UNAVAILABLE` and classified `CRITICAL` **cannot be carried as a claim**. It is emitted as an `EVIDENCE_NEEDED` entry instead | § 2.5, § 5 |
| **No adoption of the Operating Convention PROPOSALs** | OPCON-v1 is used as a *declared, non-binding working discipline* (design D-3a). P-1…P-8 are cited where relevant and **none is implemented**. The protocol adds no rule to the convention and amends no frozen rule | § 14 |
| **`main` unchanged** | no phase writes `main`; the write allowlist (design § 3.5, carried) is declared before Φ0; any write outside it is F-1 firing and halts the trial | § 4 B-8, § 14 |

---

## 2 · The evidence-layer model — the operator's correction, made executable

### 2.1 · Why the binary model had to go, stated as the failure it produces

A binary `FULL_TEXT_AVAILABLE / NOT_AVAILABLE` collapses two independent questions into one word:

- *Can the paper's argument be read?* — a property of the editorial prose.
- *Can a specific claim be checked against the thing it rests on?* — a property of one asset.

Collapsed, the model fails in **both directions**. It marks a paper unread because one
supplementary figure could not be retrieved — losing a complete, checkable reading. And it marks a
paper read when the editorial text arrived intact and the blot that carries the paper's central
result did not — **licensing an inference whose evidence nobody has seen.** The second failure is
the dangerous one, and § 2.4 measures that it is live in this repository today.

### 2.2 · The three layers, and the partition rule that makes them countable

The operator's specification names TEXT, FIGURE/ASSET and SUPPLEMENTARY. Taken literally these
**overlap**: a supplementary figure is both an asset and a supplement, and a unit counted in two
layers makes every layer percentage unreproducible. The overlap is resolved here by an explicit
partition rule, declared rather than assumed:

> **PARTITION RULE.** Every enumerated unit of the paper belongs to **exactly one** layer. The
> layers are disjoint and their union is the paper. Container wins over medium: anything published
> outside the main article file is `SUPPLEMENTARY_LAYER`, whatever its medium.

| Layer | Contains | Does **not** contain |
|---|---|---|
| **`TEXT_LAYER`** | abstract · introduction · methods · results · discussion · conclusions · limitations · reference list · textual tables of the main article · **figure captions** | the figures those captions describe |
| **`FIGURE_LAYER`** | main-article figures, individual panels, images, blots, schematics, plots, rendered graphics — *the data a caption talks about* | captions (they are `TEXT_LAYER`); anything supplementary |
| **`SUPPLEMENTARY_LAYER`** | everything published outside the main article file, of any medium: supplementary figures, supplementary tables, supplementary text and methods, source-data files, datasets, videos, code, associated assets | anything inside the main article file |

**A caption is `TEXT_LAYER`, and the figure it describes is not.** This is not a nicety invented
here: `framework/scripts/fulltext_receipts.py` already refuses `complete_fulltext_read` when any
section is `captions_only`, with the recorded reason *"a caption is authored prose, the figure is
the data (see D-14)"* — after a 2026-07-26 deep dive whose single most valuable finding was a
supplementary figure **whose panels contradict its own caption**.

### 2.3 · Per-layer status, and how it is derived without inventing a schema

Each layer takes one of three values. **They are derived, not declared** — computed from the
coverage fields the receipt schema already requires, so the protocol adds no field to any ledger
and the trial does not become framework construction (design F-1).

```
COMPLETE     every unit enumerated for the layer is at coverage state `read` or `not_present`
PARTIAL      at least one unit `read`, and at least one at `captions_only` / `unavailable` / `not_read`
UNAVAILABLE  no unit of the layer is `read`, and at least one is `unavailable` or `not_read`
             (a layer with every unit `not_present` is COMPLETE, not UNAVAILABLE — the paper has no
              such layer, which is a fact about the paper, not a gap in the reading)
```

The mapping from the existing receipt keys — `COVERAGE_KEYS` = abstract, introduction, methods,
results, figures, tables, discussion, limitations, supplementary; plus optional `references`
(`fulltext_receipts.py` lines 50–68) — is fixed as:

| Layer | Receipt coverage keys that compose it |
|---|---|
| `TEXT_LAYER` | `abstract` · `introduction` · `methods` · `results` · `discussion` · `limitations` · `tables` · `references` |
| `FIGURE_LAYER` | `figures` |
| `SUPPLEMENTARY_LAYER` | `supplementary` |

`figures: captions_only` therefore reads, in the layer model, as **`TEXT_LAYER` covered the caption
and `FIGURE_LAYER` did not** — which is precisely the distinction the binary model could not express
and the receipt vocabulary already could.

**And the rule the operator asked for, stated as the protocol's rule:**

> A paper is **`FULL TEXT COMPLETE`** when `TEXT_LAYER = COMPLETE` and that text is verifiable
> against a present, digest-matched artifact. **`FIGURE_LAYER` or `SUPPLEMENTARY_LAYER` short of
> `COMPLETE` does not, by itself, make the paper unread.** It becomes a declared epistemic limit
> **only** when a missing asset is needed to sustain a conclusion the reading actually carries —
> and then it is `CRITICAL_ASSET_GAP: YES`.

### 2.4 · 🔴 Finding T-8 — the gap this correction closes is already open in the repository

Measured today over `disease-models/wwox/registries/reading_state.md`, which is the derived union of
**128 receipts across 82 papers**:

```
per-cell coverage vocabulary observed, 10 section columns × 82 papers:
   read 505 · unknown_legacy 135 · not_present 106 · unavailable 31 · not_read 20 · captions_only 5
deepest-receipt rollup:
   complete_fulltext_read 49 · partial_fulltext_read 30 · abstract_only 2 · queried_not_full_read 1
```

> 🔴 **9 of those 49 `complete_fulltext_read` papers carry `supplementary: unavailable`.**
> PMID 17360458 · 18487609 · 18974271 · 19500159 · 24871327 · 32581702 · 34634460 · 36779245 ·
> 39416860.

The validator is not asleep — it explicitly refuses `complete_fulltext_read` when any section is
`not_read`, `unknown_legacy` or `captions_only`. **It permits `unavailable`.** That permission is
correct under the operator's rule *and only under it*: a missing supplement does not invalidate the
text. What is missing is the second half — **nothing anywhere classifies whether those nine missing
supplements were critical to a claim.** Nine papers carry a word that says "complete" over an
unexamined asset gap, and no instrument can currently tell a harmless one from a load-bearing one.

**This finding is registered, not repaired** (§ 13). It is not in the trial's write allowlist, it is
not this protocol's to fix, and repairing it mid-trial would be F-1 firing.

**A note on what the correction is *not*.** `FULL_TEXT_AVAILABLE` fires on **0 tracked paths**
(positive control `^status:` = 30 paths, negative control = 0). The binary model was never repo
vocabulary — it was the model in the operator's and this session's heads. Correcting it therefore
changes **no file** and costs nothing; the cost was in the nine papers above, which the vocabulary
already permitted and no one was counting.

### 2.5 · Classification of documentary gaps — required for every unit not `read`

Every unit that is not `read` is classified into exactly one class, at the moment it is found, by
the reader, **before** the claim set is assembled. **`G-0` is not a default**: a gap is `G-0` only
after the reader has stated which claim it was checked against.

| Class | Meaning | Consequence for the reading | Consequence for the claim |
|---|---|---|---|
| **`G-0` NOT_PRESENT** | the paper has no such unit | none — this is a fact about the paper | none |
| **`G-1` UNAVAILABLE_NOT_CRITICAL** | the unit could not be obtained, and **no carried claim rests on it**. The reader names the claims checked against it | logged; layer drops to `PARTIAL`; `FULL TEXT COMPLETE` **survives** | none |
| **`G-2` UNAVAILABLE_POSSIBLE_CLAIM_IMPACT** | the unit could not be obtained, and a carried claim **might** rest on it — the reader cannot tell without seeing it | logged; layer `PARTIAL`; an `EVIDENCE_NEEDED` entry is emitted naming the claim and the unit | the claim is carried **with its epistemic limit declared inline**, and it may not be typed `DATO` on that evidence alone |
| **`G-3` CRITICAL_FOR_CLAIM_VERIFICATION** | the unit could not be obtained, and a **named** carried claim cannot be checked without it | `CRITICAL_ASSET_GAP: YES`; the trial declares the limit in the outcome | 🔴 **the claim is NOT VERIFIED** (§ 5 V-4) and cannot enter a COMMIT CANDIDATE as `DATO`. It survives as `IPOTESI` with `EVIDENCE_NEEDED`, or it is withdrawn |

```
CRITICAL_ASSET_GAP  ≔  YES  iff  at least one unit is classified G-3
                       NO   otherwise
```

**`CRITICAL_ASSET_GAP` is a property of the pair (reading, claim set), not of the paper.** The same
missing figure is `G-1` for a reading that never cites it and `G-3` for one that does. It is
therefore re-evaluated whenever the claim set changes, and the outcome records the claim each `G-3`
is bound to. A `G-3` with no named claim is a classification error, not a gap.

### 2.6 · The status block every reading emits

Produced once per arm, per paper, in `TRIAL-001-LAYER-STATUS-<arm>.md`, and reproduced verbatim in
the outcome:

```
PAPER:                PMID 28123895
SURFACE:              <structured | pdf_only | absent>   (surface_census.py vocabulary)
ARTIFACT_DIGEST:      sha256 <…>                          (the bytes the layers were read from)

TEXT_LAYER:           COMPLETE | PARTIAL | UNAVAILABLE
FIGURE_LAYER:         COMPLETE | PARTIAL | UNAVAILABLE
SUPPLEMENTARY_LAYER:  COMPLETE | PARTIAL | UNAVAILABLE
CRITICAL_ASSET_GAP:   YES | NO

FULL_TEXT_COMPLETE:   YES | NO        (YES iff TEXT_LAYER = COMPLETE and digest-verified)

GAPS:
  <unit id> | <layer> | G-1|G-2|G-3 | <claims checked against it> | <what was tried to obtain it>
```

The `<what was tried to obtain it>` column is not decoration: an unobtained asset with no recorded
attempt is indistinguishable from an asset nobody looked for, and the difference is the whole
epistemic content of the gap.

---

## 3 · Entry criteria — what a paper must satisfy to enter the trial

All eight, conjunctive. **Each is re-derived at the moment of entry, never read from this table.**

| # | Criterion | Route | Status for PMID 28123895, measured 2026-08-23T20:2xZ |
|---|---|---|---|
| **E-1** | **Never analyzed.** The PMID appears, digit-bounded, on **none** of the 8 analysis surfaces | the § 15 sweep, with positive and negative controls | ✅ **0 of 8** (positive control PMID 42397075 → 5 of 8; negative control 99999999 → 0 of 8) |
| **E-2** | **In the queue, with a formed question.** A `## FT-` entry exists and its `**Why:**` states what the reading is for | `full_text_queue_current.md` | ✅ `FT-018`, `HIGH`, question formed — activation state vs level of WWOX under C1q |
| **E-3** | **No local surface yet** — so acquisition is a real, declared step and not a formality | `surface_census.py` vocabulary; `files/fulltext/` | ✅ `Surface: absent`; **0 of 174** corpus files match `28123895` or `PMC5214935` |
| **E-4** | **Acquirable by a declarable method**, at zero external spend (J.4 `DEFAULT_EXTERNAL_SPEND = 0`) | the queue entry's own record | ✅ PMCID `PMC5214935` recorded open. **Not verified by this session** — the connectors are unauthorized here (§ 4 B-2), so this is a recorded claim awaiting Φ1 |
| **E-5** | **The epistemic gates can fire on it.** At least two `framework/eval/failure_taxonomy.md` gates are live in the paper's own content | design § 2.2, carried | ✅ three: `MECHANISTIC_OVERTRANSFER`, `MECHANISM_DIRECTNESS_GATE`, `KG_EDGE_HAS_NO_SIGN` |
| **E-6** | **It has a figure and supplementary layer worth statusing.** A paper that is text-only cannot exercise § 2 | inspection at Φ1, after acquisition | ⏳ **UNKNOWN until Φ1.** If the paper turns out to have no assets, § 2 is exercised at `G-0` only, and the outcome says the layer model was **not tested** rather than that it passed |
| **E-7** | **Sized for one reading session.** Not a corrigendum, not a review of 400 references | queue metadata | ✅ a primary research article |
| **E-8** | **No individual-level linkage.** The reading reasons about the reference genotype class | public-edition rule, CLAUDE.md | ✅ an oncology model paper; no patient-level content expected |

> ⚠️ **E-6 is the one criterion this protocol cannot pre-satisfy, and it is disclosed rather than
> assumed.** If PMID 28123895 has no supplementary material, the trial still runs and still measures
> everything else — but `SUPPLEMENTARY_LAYER` reads `COMPLETE` trivially, and **the layer model's
> most important state, `G-3`, will not have been exercised.** The outcome must say so in those
> words, because a model that was never stressed is not a model that held.

**Alternates, in order, if an entry criterion fails at Φ1:** `FT-017` PMID 39933386 →
`FT-019` PMID 21444760. Both re-measured today at **0 of 8**. `FT-015` PMID 40263068 is a
corrigendum and fails E-7. **Substituting the paper is an operator decision (design D-1), not the
protocol's** — the protocol halts and escalates.

---

## 4 · Blocking criteria — what stops the trial, and at which phase

A block is not a failure. **A refusal is a result** and is recorded as one. What is forbidden is
proceeding past a block by weakening the check.

| # | Block | Fires at | Detected by | Release condition |
|---|---|---|---|---|
| **B-1** 🔴 | **Any entry criterion E-1…E-8 fails at the moment of entry** | Φ0 | the § 3 routes re-run | operator substitutes the paper (D-1) or the criterion is met |
| **B-2** 🔴 | **No declarable acquisition route.** Measured this session: the claude.ai PubMed / bioRxiv / Scholar Gateway connectors **require authorization and are unavailable**, so no acquisition can be performed or declared from here | Φ1 | connector state at the moment | operator authorizes a connector, supplies the PDF, or a session with web access runs `find-fulltext` (design D-2) |
| **B-3** 🔴 | **Acquisition performed before its method was declared** | Φ1 | the declaration's timestamp is later than the artifact's | 🔴 **the input is void.** Re-acquire under a declaration. This block cannot be waived — it is the operator's constraint, and an undeclared acquisition is unreproducible by construction |
| **B-4** 🔴 | **The surface refuses.** `benchmark_input_surface.py verify` fails on parity, a forbidden prior-output path, an unlisted file, or a content-scan hit | Φ1 | the tool | repair the spec and re-verify. **Never by relaxing the allowlist** |
| **B-5** 🔴 | **The freeze cannot be shown to precede content reading** | Φ5 | `FREEZE_TIMESTAMP_UTC` vs the first content-read instant | the arm's `D-REPRO` is void; the outcome says so. **The freeze is not back-dated** |
| **B-6** 🔴 | **A `NOT_IN_SOURCE` audit verdict** | Φ7 | the blind audit | per `legend-locator-audit`: blocks the reading from touching canonical state until resolved. The claim is withdrawn or re-anchored, and both are recorded |
| **B-7** | **An unanswered `OVERSHOOT` / `UNDERSHOOT`** | Φ8 | the audit + review | must be answered before any `BATCH_COMMIT`: the claim is narrowed to what the source says, or the locator is replaced |
| **B-8** 🔴 | **A write outside the declared allowlist** | any | `git status` against the allowlist | 🔴 **F-1 is firing — the trial has turned into framework construction.** Halt, record, escalate. Do not "just finish this one file" |
| **B-9** 🔴 | **`CRITICAL_ASSET_GAP: YES` on a claim proposed as `DATO`** | Φ6, Φ10 | § 2.5 `G-3` bound to a named claim | the claim is re-typed `IPOTESI` with `EVIDENCE_NEEDED`, or withdrawn. It does **not** enter the candidate as an observation |
| **B-10** 🔴 | **The candidate's gate field cannot be filled conformantly.** Measured: 8 of 8 `CAND-*` manifests carry `MIRROR_REVIEW`; **0 carry a value in the frozen vocabulary** `n/a \| PASS \| FAIL` (design T-5) | Φ10 | `annex_d_commit_batch.md` line 38 | 🔴 **the trial stops at the candidate by design** (design D-9a) unless the operator resolves the gate. Producing a ninth non-conforming value is not a release |
| **B-11** | **Money would be spent** | any | J.4 `DEFAULT_EXTERNAL_SPEND = 0` | operator authorization, per instance |
| **B-12** | **An escalation arrives as a diagnostic instead of a decision** | any | S.8.1 shape check | rewrite it decision-shaped: the decision in one sentence, the options, a recommendation, and what proceeds regardless |

---

## 5 · What "a verified claim" means — defined before anything counts them

**This definition is the denominator of the primary metric, and it is fixed here so that the metric
cannot be tuned by loosening it afterwards.**

> A carried statement is a **`VERIFIED CLAIM`** if and only if it satisfies **all five** conditions.
> Failing any one, it is not verified — and the protocol reports *which* condition failed, never a
> bare count of failures.

| # | Condition | Instrument | Verdict is |
|---|---|---|---|
| **V-1** | **TYPED.** The statement declares `DATO` \| `INFERENZA` \| `IPOTESI`; every negative and non-trivial conclusion carries its `PREMISE_TAG` | `epistemic_discipline.md`; presence is mechanical | mechanical |
| **V-2** | **ANCHORED.** ≥1 `(proposition, verbatim snippet, anchor)` triple whose artifact is present and digest-matched, and whose quote actually occurs in that artifact | `deepdive_manifest.py --verify-artifacts --require-current-schema` · `locator_audit.py --strict` | mechanical |
| **V-3** | **BLIND-AUDITED `SUPPORTED`.** An auditor who saw neither the dossier, nor the reader's identity, nor the conclusions returns `SUPPORTED` — not `OVERSHOOT`, not `UNDERSHOOT`, not `NOT_IN_SOURCE` | `legend-locator-audit`, fresh ephemeral session | adjudicated, blind |
| **V-4** | **LAYER-SUFFICIENT.** No `G-3` gap is bound to this claim; `CRITICAL_ASSET_GAP` is `NO` *for this claim*. **This is the operator's "no inference without available evidence", made countable** | § 2.5 classification + the layer status block | mechanical, given the classification |
| **V-5** | **REPRODUCED.** An independent session, given only the frozen artifacts and the recorded commands, re-derives the same verdict — without asking the reader anything | replay by a fresh session; `verify-freeze` | mechanical |

### 5.1 · The three states that are *not* failures, and are counted apart

Collapsing these into "unverified" would make the metric flatter and less true.

| State | Meaning | Counted as |
|---|---|---|
| **`UNVERIFIABLE_SURFACE`** | the quote is from a figure panel or image and cannot be matched as text. The `legend-locator-audit` vocabulary already carries this verdict, and the skill records that it **is fine, and must be declared as such** | **not `VERIFIED`, not a defect.** Its own bucket. A claim here is verifiable only by `FIGURE_LAYER` inspection, and whether that inspection was possible is exactly what § 2.3 records |
| **`WITHDRAWN_ON_AUDIT`** | the reader withdrew the claim when the audit found it unsupported | **a success of the instrument**, reported under D-REV, not as a loss |
| **`EVIDENCE_NEEDED`** | the claim was never carried, because its evidence layer was `G-2`/`G-3`. It exists as a stated question | **an output**, counted under D-UNC, and one of the trial's useful products (§ 12) |

> 🔴 **The gaming risk, named so it is visible.** Every one of V-1…V-5 is easier to satisfy by
> carrying **fewer, smaller, safer claims**. A reading that carries three trivial anchored
> statements scores a perfect verification rate and is worthless. **The primary metric is therefore
> never reported without the raw claim count and the claim-substance judgement beside it** (§ 6.4),
> and Mirror's R4 is explicitly asked whether the claim set was thinned to fit the metric (§ 9).

---

## 6 · What is measured

### 6.1 · The three rules that govern every number

1. **No composite, no weighting, no overall score.** Each dimension reports in its own table.
2. **Operational figures never proxy for quality.** A reading is not better for being faster,
   shorter or cheaper. They are reported apart and they break no tie.
3. **Every figure carries its command, the instant it was run, and its class** — `population-derived`
   figures decay on their own; `object-derived` figures do not (OPCON-v1 § S.7.6–7.7).

### 6.2 · 🔴 The primary unit of measure

```
PRIMARY UNIT ─────────────────────────────────────────────────────────────────
    auditor-minutes per VERIFIED CLAIM,  per arm

    numerator    minutes logged by the blind auditor on that arm, from the auditor's OWN
                 log, epoch-derived, counting only verification acts (locating the evidence,
                 reading it, returning a verdict). Not the reader's minutes.
    denominator  claims of that arm satisfying all five conditions of § 5.

    REPORTED AS A TRIPLE, ALWAYS:   (numerator, denominator, quotient)
    NEVER as the quotient alone — a quotient hides which half moved.

    IF denominator = 0  →  the value is UNDEFINED, not infinite, not "poor".
                           The numerator is still reported, and so is the reason the
                           denominator is zero, per § 5 condition.
───────────────────────────────────────────────────────────────────────────────
```

**Why the auditor's minutes and not the reader's.** The question LEGEND's discipline is supposed to
answer is not *"how fast can a reading be produced"* — it is *"how cheaply can a reading be
trusted by someone who was not there"*. Production cost is recorded (§ 6.5) and is not primary.

**Explicitly rejected as primary metrics**, each because it rewards the wrong behaviour:

| Rejected | Rewards |
|---|---|
| total wall time | rushing, and a shorter reading |
| token count | terseness, and it is `NOT OBSERVABLE` here unless the runtime exposes it — it is never estimated |
| number of files produced | ceremony |
| number of claims carried | volume over verifiability, the exact inflation V-1…V-5 exist to catch |

### 6.3 · Secondary measures — reported beside the primary, never folded into it

| # | Measure | Definition | Route |
|---|---|---|---|
| **S-1** 🔴 | **`NOT_LOCATABLE` fraction** | claims the auditor could not locate the evidence for **at all** ÷ claims audited, per arm | the auditor's log. This is the measure the anchoring discipline exists to move, and it is the one arm T is expected to lose on |
| **S-2** | **verification-failure profile** | claims failing V-1 / V-2 / V-3 / V-4 / V-5, counted separately, per arm | § 5 instruments |
| **S-3** | **audit verdict distribution** | `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE`, per arm | `legend-locator-audit` |
| **S-4** | **defects the audit caught that the reader's self-check did not** | set difference, enumerated not counted | audit vs the reader's own log |
| **S-5** | **layer coverage actually achieved** | the § 2.6 status block, per arm, plus the `G-1/G-2/G-3` census | § 2.5 |
| **S-6** | **`G-3` gaps bound to a named claim** | the count, **with the claims enumerated** | § 2.5 |
| **S-7** | **failure-taxonomy gate instances** | which gates fired, per arm, each with a locator | `framework/eval/failure_taxonomy.md` |

### 6.4 · The judgement that no instrument produces

**Claim substance.** Whether the verified claims are worth having is not mechanical and is not
faked with a number. It is one adjudicated question, answered by the Annex C reviewer and
cross-checked by Mirror:

> *Of the verified claims, how many would change what the working model says — and how many are
> true, anchored and inert?*

Reported as an enumeration with reasons, never as a score. **A trial where every claim is inert is
a trial where the primary metric is excellent and the reading was pointless**, and that outcome must
be sayable.

### 6.5 · Operational — recorded because someone will ask, breaking no tie

| Figure | Definition | Note |
|---|---|---|
| production cost | handover → completion declaration, per arm, wall clock from receipts | not primary |
| **blocked time** | cumulative time waiting on a human decision | 🔴 the figure that tests whether the operator is the bottleneck (design F-8) |
| token / cost | `NOT OBSERVABLE` unless the runtime exposes it — **never estimated** | |
| revisions | `WORK_COMMIT`s on the reading branch + review rounds (C.3 caps at 2 → adjudication) | |
| errors intercepted | audit verdicts ≠ `SUPPORTED`; Mirror findings; **mechanical refusals** | a refusal is an interception and counts as one |

### 6.6 · The friction log — the one required metric with no instrument

`TRIAL-001-FRICTION-LOG.md`, append-only, **written during the run and never reconstructed
afterwards**:

```
<epoch> | <UTC from `date -u -r <epoch>`> | <phase> | <what stopped, or had to be re-derived,
        or had no owner> | <who unblocked it> | <minutes lost>
```

Three classes are mandatory: **(a)** any point where the protocol forced a stop; **(b)** any figure
a receiver had to re-derive because a dispatch's stated value was wrong — *both halves get logged,
because a log that records only the error teaches the next dispatcher to supply fewer facts, when
the lesson is that the receiver re-runs them*; **(c)** any decision that had no owner.

**Everything else can be reconstructed from artifacts. Friction cannot.**

---

## 7 · The two arms, and the method of comparison

### 7.1 · Arm L — LEGEND

Same frozen bytes, same question, **under the full reading discipline**: receipt with per-section
coverage, work manifest with verbatim locators, the § 2.6 layer status block, `G-1/G-2/G-3`
classification, typed statements with premise tags, coverage map over the enumerated population,
and a COMMIT CANDIDATE that stops at the operator's gate.

### 7.2 · Arm T — control (unstructured)

Same frozen bytes, same question, **no LEGEND scaffolding**: no locator obligation, no typing
vocabulary, no receipt, no coverage map, no layer status. Free-form analysis notes, of the kind a
competent researcher writes for themselves. Output: `TRIAL-001-ARM-T-NOTES.md`.

Arm T is **not a LEGEND actor and must not be registered as one.** Its reader is instructed to work
as they naturally would and is explicitly told the notes will be audited.

### 7.3 · Method of comparison

```
                    ┌── arm L ── anchored, typed, layer-statused claims ───┐
frozen surface ─────┤                                                      ├── blind audit ── compare
                    └── arm T ── free-form notes, no anchors ──────────────┘
```

**Paired, same paper, same bytes, same question.** The comparison is **not** "which reading is
better" — without a gold-standard reading of this paper that question has no instrument, and
inventing one would be the failure the whole design exists to avoid.

The comparison that *does* have an instrument, and the only one this trial makes:

> **Given each arm's output and the frozen source, how expensive is it for an independent party to
> check a claim — and how many claims can be checked at all?**

The auditor receives both arms' claim sets **stripped of arm identity**, in interleaved order, and
logs per claim: minutes to reach a verdict, the verdict, and whether the evidence was locatable at
all. Arm L's claims arrive with anchors and the auditor verifies. Arm T's arrive without and the
auditor must first *find* the evidence, and may fail. **The asymmetry is declared here in advance as
the measurement** — not discovered afterwards and reported as arm T's defect.

**Statistics: none.** n = 1 paper, one reader per arm. Session variance is not separable from arm.
The trial reports raw distributions and **states that it cannot distinguish arm from session.** Any
sentence of the form "arm L is X% better" is out of bounds in the outcome.

### 7.4 · Two contaminations, declared before the run

| # | Contamination | Direction | Consequence |
|---|---|---|---|
| **K-1** | Arm T is run by the same class of reader that has LEGEND's discipline internalised. It will be *better* than a genuinely naive workflow | biases **against** LEGEND | the safe direction: a favourable result survives it. **A null result does not license "the discipline is worthless"** |
| **K-2** | The auditor is a LEGEND-shaped instrument and may find anchored claims easier to audit *because they are shaped like what it expects*, not because they are better anchored | biases **for** LEGEND | 🔴 disclosed, **unmitigated**, and named in the outcome. The trial cannot separate these, and saying so is the honest report |

### 7.5 · The barrier between arms, labelled in the Annex J.0 style

```
GUARANTEE_PROVIDED:          none by mechanism — the SURFACE blinding is mechanized
                             (allowlist · parity · content scan · forbidden-path check);
                             the barrier BETWEEN the two readers is discipline only
FAILURE_MODE_STILL_POSSIBLE: Plan reads or relays arm L's output to arm T before arm T freezes
DETECTION:                   receipts carry FREEZE_TIMESTAMP_UTC and SURFACE_COMMIT; inspection
                             makes a violation VISIBLE AFTER THE FACT, never prevented
RECOVERY:                    the trial is void for the second arm; the outcome says so
```

---

## 8 · The executive protocol, step by step, with the artifact each phase produces

**No phase writes `main`.** Every phase's artifact is named; a phase that produced no artifact did
not run.

| Φ | Owner | Act | **Artifact produced** | Gate to leave the phase |
|---|---|---|---|---|
| **Φ0** | operator + any session | **Pre-flight re-derived at the moment**, by the routes of the design § 3.1 and § 3 above — *never read from a table* | `TRIAL-001-PREFLIGHT.md` — 11 rows + the 8 entry criteria, each with its command and instant | every row satisfied at the moment of handover, or the trial does not start (B-1) |
| **Φ1a** | operator / a session with acquisition capability | **Declare the acquisition method — before acquiring** | `TRIAL-001-ACQUISITION-DECLARATION.md`: route · tool · identifier · licence basis · executor · expected artifact type | 🔴 **B-3.** Nothing is fetched until this file exists |
| **Φ1b** | same | Acquire; record the receipt; verify the digest | the artifact in `files/fulltext/` · `fulltext_receipts.py record` entry · the digest | `fulltext_receipts.py verify` passes; the artifact digest matches the declaration |
| **Φ1c** | Plan | Author the surface spec; `build --emit-digests`; `verify`; **enumerate the population**; **hand-check it independently**; **FREEZE before any content is read** | `TRIAL-001/surface_spec.json` · `benchmark_manifest.json` · population digest ×2 runs · `FROZEN_SHA256` | `verify` refuses on parity failure, forbidden path, unlisted file or content-scan hit (B-4). 🔴 **Two runs must give an identical population digest, and one hand enumeration must agree** — the enumerator was wrong twice on the other paper (design F-5) |
| **Φ1d** | Plan | **Enumerate the layer units** — which units compose `TEXT_LAYER`, `FIGURE_LAYER`, `SUPPLEMENTARY_LAYER` for *this* paper, before anyone reads them | `TRIAL-001-LAYER-POPULATION.md` — the unit list per layer, with the partition rule applied | 🔴 the population is enumerated **by an instrument that cannot see coverage.** A layer whose denominator is set by the reader is not a measurement |
| **Φ2** | operator (or Orchestrator **iff** a lease is ACTIVE) | Issue the two assignments under one group id: `TRIAL-001-L`, `TRIAL-001-T` | 2 contracts under `ledger/tasks/…` | Annex A.1 requires a resolvable `OWNER (ACTOR_ID)` — design D-4/D-5 |
| **Φ3** | Plan → each reader | HANDOVER: writer transfer + memory-scope check **recorded, not asserted** | `HANDOVER` block in each manifest | one writer per surface, transferred once |
| **Φ4** | readers, **concurrent and mutually blind** | Arm L reads under the reading obligations; arm T under none. **Both classify every non-`read` unit `G-0…G-3` at the moment they find it** | arm L: receipt, manifest, locators, layer status block · arm T: `TRIAL-001-ARM-T-NOTES.md` | no contact, no sight of the other arm, no sight of any prior LEGEND output |
| **Φ5** | Plan | **FREEZE each reading ON its completion declaration, BEFORE reading its content** | `RECEIPT-<arm>.json` with `FREEZE_TIMESTAMP_UTC`, `SURFACE_COMMIT`, `FIRST_PASS_STATE` | 🔴 B-5 — *a freeze taken after Plan has read the content is a freeze whose timing cannot be shown* |
| **Φ6** | Plan | Mechanical checks: `deepdive_manifest.py --verify-artifacts --require-current-schema` · `locator_audit.py --strict` · `dossier_quote_audit.py` · coverage over the frozen population · `fulltext_receipts.py verify` · `legend_lint.py` · `verify-freeze`. **Derive the § 2.6 layer status block from the receipt coverage — do not accept a declared one** | `TRIAL-001-CHECK-LOG.md` · `TRIAL-001-LAYER-STATUS-<arm>.md` · coverage map | any refusal halts and is recorded. **A refusal is a result** |
| **Φ7** | fresh blind sessions | **Locator audit of both arms, arm identity stripped, claims interleaved.** Per claim: verdict, minutes-to-verdict, and `NOT_LOCATABLE` yes/no | `reviews/…/REV-TRIAL001-AUDIT-001` + the auditor's own timing log | the auditor never sees the dossier, the reader's name, the arm label, or the conclusions |
| **Φ8** | reviewer | Annex C review at the floor for the claim class — **`R2` (INDEPENDENT, semi-blind) decided in advance**, because C1q is druggable and anti-C1q antibodies are in human trials, which makes any therapeutic-shaped inference `R2` by C.1. Full field set: `VERDICT` · `REVIEWER_CONFIDENCE` · `RESIDUAL_UNCERTAINTY` · `EVIDENCE_NEEDED` · `WHAT_WOULD_CHANGE_MY_MIND` · `AUTHOR_RESPONSE` | `REV-TRIAL001-R2-001` | AUTHOR ≠ REVIEWER; max 2 rounds → adjudication; `DISAGREEMENT_UNRESOLVED` is a legitimate close |
| **Φ9** | Mirror | **R4 on the process** (§ 9) | `REV-TRIAL001-MIRROR-002` | Mirror's stated primary surface does not exist (design T-4); its input is scoped **by declaration** to the frozen artifacts and receipts |
| **Φ10** | reader-L → operator | Assemble the COMMIT CANDIDATE; **stop at the gate** | `commit_candidates/CC-TRIAL001-…` | 🔴 B-9 and B-10. The trial's product is the candidate; the commit is the operator's (design D-9) |
| **Φ11** | Plan | Outcome — **each dimension its own table, no composite**; the primary metric as a triple; operational figures in a separate table that breaks no tie | `TRIAL-001-OUTCOME.md` · `TRIAL-001-FRICTION-LOG.md` (closed) · one SLR | every count is an enumerated set or carries the command that produced it |

### 8.1 · Artifact index — what exists at the end, and who owns each

| Artifact | Phase | Owner | Survives a failed trial? |
|---|---|---|---|
| `TRIAL-001-PREFLIGHT.md` | Φ0 | any session | ✅ |
| `TRIAL-001-ACQUISITION-DECLARATION.md` | Φ1a | acquirer | ✅ **and is reusable by any future reading of this paper** |
| the full text + receipt + digest | Φ1b | acquirer | ✅ **the corpus grows regardless of outcome** |
| `TRIAL-001/surface_spec.json` + manifest + frozen population | Φ1c | Plan | ✅ |
| `TRIAL-001-LAYER-POPULATION.md` | Φ1d | Plan | ✅ |
| arm L: receipt · manifest · dossier · locators | Φ4 | reader-L | ✅ |
| `TRIAL-001-ARM-T-NOTES.md` | Φ4 | reader-T | ✅ |
| `RECEIPT-L.json` · `RECEIPT-T.json` | Φ5 | Plan | ✅ |
| `TRIAL-001-CHECK-LOG.md` · `TRIAL-001-LAYER-STATUS-<arm>.md` | Φ6 | Plan | ✅ |
| `REV-TRIAL001-AUDIT-001` + timing log | Φ7 | blind auditor | ✅ **the highest-value artifact per unit of cost** |
| `REV-TRIAL001-R2-001` | Φ8 | reviewer | ✅ |
| `REV-TRIAL001-MIRROR-002` | Φ9 | Mirror | ✅ |
| `CC-TRIAL001-…` | Φ10 | reader-L | conditional — B-9/B-10 may empty it |
| `TRIAL-001-OUTCOME.md` · `TRIAL-001-FRICTION-LOG.md` · SLR | Φ11 | Plan | ✅ |

---

## 9 · When Mirror intervenes

**Mirror's object is the process, never the paper.** R4 is `METHOD (Mirror)` in the Annex C ladder,
and Annex G scopes it to perimeter, self-upgrade and metrics. Under G.1 this trial is
**`MIRROR_REQUIRED`** — it is a first-of-kind methodology run, which is the `processo inferenziale
methodology-changing` row of C.1.

| When | What Mirror is asked | What it produces |
|---|---|---|
| **M-0 · before Φ1** *(now — § 13)* | **Hostile review of this protocol**, bound by this file's blob | findings, registered and **not auto-corrected** |
| **M-1 · Φ9, after both arms are frozen and audited** | R4 on the process: was the freeze timing *shown*? Did the audit run blind, with arm identity actually stripped? Were uncertainties outputs with falsifiers, or residue? Did the trial stay inside its write allowlist? Was the layer population enumerated before it was measured? 🔴 **Was the claim set thinned to make § 5's conditions easier to satisfy?** (§ 5.1) | `REV-TRIAL001-MIRROR-002` |
| **M-2 · on demand, any phase** | if a block B-1…B-12 fires and its release is contested | a finding, never a release |

| Mirror must **never** | Why |
|---|---|
| act as a third reader of the paper | R4 is not a reading; Annex G makes the process its object |
| lift a blocker or authorize anything | Mirror produces findings, never authorizations |
| resolve its own findings inside the trial | findings are registered; repairs happen after, outside the trial (design F-1) |
| be treated as having read the consolidated event ledger | it does not exist (design T-4). Mirror's input is scoped by declaration, and its review must say so |

---

## 10 · When Plan intervenes

Plan is the **timing and mechanical guarantor** of the trial. It is the only role whose absence makes
`D-REPRO` unprovable, because the freeze is its act.

| When | What Plan does | Why it must be Plan and not the reader |
|---|---|---|
| **P-0 · before Φ1** *(now — § 13)* | **Feasibility review of this protocol**, bound by this file's blob: can Φ1c/Φ1d be built at the stated cost, with the instruments that exist? | the surface spec is Plan's real cost, and only Plan can price it |
| **P-1 · Φ1c** | build the surface, `verify`, enumerate the population twice, and freeze **before content** | a reader who enumerates its own population sets its own denominator |
| **P-2 · Φ1d** | enumerate the layer units, before anyone reads them | same reason, applied to § 2 |
| **P-3 · Φ3** | record the handover and the writer transfer | one writer per file for its lifetime |
| **P-4 · Φ5** | freeze each arm **on** its completion declaration, before reading content | the freeze is the timing guarantee, and it cannot be self-attested by the arm it freezes |
| **P-5 · Φ6** | run every mechanical check; **derive** the layer status rather than accept a declared one | a self-declared layer status is a claim, not a measurement |
| **P-6 · Φ11** | assemble the outcome: each dimension its own table, the primary metric as a triple, no composite | |

| Plan must **never** | Why |
|---|---|
| read arm L's content before arm T freezes | B-5 / § 7.5 — it is the single mechanism by which the barrier fails |
| author or edit a claim | Plan measures; it does not read the paper |
| relax a spec to make `verify` pass | B-4 |

---

## 11 · Success and failure criteria, pre-registered

### 11.1 · The trial succeeds *as an experiment* if — independent of whether LEGEND looks good

Every phase produced its named artifact · both arms froze with **shown** timing · the audit ran
blind with arm identity stripped · every mechanical gate ran and its result was recorded, pass or
refuse · the layer status was **derived** and every non-`read` unit classified `G-0…G-3` · Mirror
adjudicated the process · and the outcome reports each dimension separately, with the route that
produced each number.

### 11.2 · The trial fails *as an experiment* if

Any of: an arm's freeze cannot be shown to precede content reading · the audit was not blind ·
a figure appears in the outcome without the command that produced it · the layer population was set
by the reader · a write happened outside the allowlist · **or the outcome reads as a paper summary
rather than a dimension-by-dimension table** (design F-12).

### 11.3 · LEGEND is judged to improve a dimension only against these, each with its falsifier

| Dimension | Improvement criterion | Falsifier |
|---|---|---|
| **PRIMARY** | **arm L's auditor-minutes per verified claim is lower than arm T's, and arm L's `NOT_LOCATABLE` fraction is lower** | arm T's claims are located and checked as fast and as reliably → **the traceability advantage is not supported by this trial**, and the outcome says exactly that |
| D-TRACE | every arm-L claim resolves to a digest-matched, locator-exact triple; the manifest passes its own validator | any claim carried without a resolvable anchor |
| D-SEP | 100 % of carried statements typed; every negative carries a premise tag | the audit finds a hypothesis carried as an observation |
| D-REPRO | an independent session reproduces every reported count and verdict from the record alone | any figure that cannot be re-derived without asking its author |
| D-UNC | uncertainties are entries with **satisfiable** falsifiers | `WHAT_WOULD_CHANGE_MY_MIND` present but unsatisfiable by any observation |
| D-REV | the blind audit finds ≥1 defect the reader's self-check did not | the audit finds nothing and the reader found nothing — **which is evidence about the audit, not a clean bill** |
| **D-LAYER** *(new)* | every non-`read` unit is classified; every `G-3` names its claim; the § 2.6 block is derivable from the receipt with no hand-declared value | a `G-3` with no claim bound to it, or a layer status that cannot be re-derived from coverage |

> **`NO IMPROVEMENT MEASURED` is a legitimate, publishable outcome.** So is
> `DISAGREEMENT_UNRESOLVED`. Neither is re-run to a better number. **A trial that can only succeed
> is not an experiment.**

---

## 12 · What remains useful if the trial fails

Enumerated per failure mode, because "we learned something" is not a result.

| If this fails | What survives, and why it has value on its own |
|---|---|
| **acquisition (B-2/B-3)** | the acquisition declaration becomes the **first written acquisition method in this repository**, reusable by every future reading. And the trial has measured, rather than assumed, that LEGEND cannot currently acquire a paper unaided |
| **the reading is thin or the paper is irrelevant** | a **documented `DISMISSAL` is a legitimate scientific product** — it discharges `FT-018` from the queue with a reason, which is what the queue is for. And the full text enters the corpus permanently |
| **arm L scores no better than arm T** | 🔴 **this is the single most valuable possible outcome.** It is the first measured evidence in this repository about whether the discipline earns its cost, and it can only be produced by running it. It goes in the outcome unsoftened |
| **the audit finds nothing** | evidence about the **auditor**, per the D-REV falsifier — and a calibration fact about a blind-audit instrument the laboratory is otherwise trusting on precedent |
| **the candidate cannot pass its gate (B-10)** | design T-5 is confirmed with a ninth data point and a live blocked candidate — a **concrete, reproducible instance** of a gate nobody can currently satisfy, which is stronger than the eight-manifest survey |
| **a mechanical instrument refuses** | a refusal is a result. Every refusal is a defect found before it reached a canonical file |
| **the layer model is never stressed (E-6)** | the model is still specified, derivable from existing receipts, and § 2.4's nine papers remain measured and open. The correction stands on its own measurement, not on this trial |
| **the trial is abandoned midway** | the **friction log** — the only artifact that cannot be reconstructed afterwards, and the one that says where a laboratory of this shape actually stalls |
| **everything fails** | § 13's findings register, and the design's T-1…T-7 plus this record's T-8, all bound to blobs, none auto-corrected |

---

## 13 · Reviews commissioned before this protocol closes

Per the operator's instruction. **Both are bound to a specific blob, and neither's findings are
corrected automatically.**

```
REVIEWED OBJECT
  path   learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1.md
  blob   NOT PRINTABLE HERE — see below
  branch legend-operating-convention-v1 @ 30cb4f3 — the protocol itself is untracked
```

> 🔴 **A record cannot contain its own blob id.** Writing the id into the file changes the bytes and
> therefore changes the id. The blob is produced by `git hash-object -w` on the **final** bytes of
> this file (§ 15), written into the object database so both reviewers can read exactly these bytes
> from any worktree, and it is **carried in the dispatch to each reviewer, not in the record**. Each
> review must quote the blob it was given back, and a review that does not name a blob is a review
> of a moving object — B.4 H-1b.

| Review | Reviewer | Question put | Binding |
|---|---|---|---|
| **hostile review** | Mirror (M-0) | *Attack this protocol. Where does it let a bad reading through? Where can a number be gamed, a gate satisfied trivially, or a gap classified `G-1` that is really `G-3`?* | none — findings only |
| **feasibility review** | Plan (P-0) | *Can Φ1a–Φ1d actually be built with the instruments that exist, at a stated cost? Which phase has no owner, no instrument, or an instrument that will refuse?* | none — findings only |

**Handling of findings — fixed in advance so it cannot be decided after they arrive:**

1. Every finding is **registered verbatim** in `§ 13.1` with its reviewer and the blob it was made
   against. **None is corrected in this version.**
2. A finding that would change the protocol produces a **`v2`, authored by the operator's decision**
   — not an edit to the blob that was reviewed, which would orphan the review.
3. A finding the protocol declines to act on says **why**, in the register. Silence is not a
   disposition.
4. 🔴 **A finding is not a blocker unless the operator makes it one.** Neither reviewer holds
   authority over this record, and neither is asked to grant one.

### 13.1 · Findings register — populated on receipt

| # | Reviewer | Blob reviewed | Finding | Disposition |
|---|---|---|---|---|
| — | — | — | *awaiting M-0 and P-0* | — |

### 13.2 · Findings this protocol registers of its own, uncorrected

| # | Finding | Evidence | Owner |
|---|---|---|---|
| **T-8** 🔴 | **9 of 49 `complete_fulltext_read` papers carry `supplementary: unavailable`, and nothing classifies whether the missing supplement was critical to a claim.** The validator refuses `not_read` and `captions_only` under `complete_fulltext_read` and permits `unavailable` — correct under § 2's rule, incomplete without § 2.5's classification | § 2.4 | Plan / operator — **outside this trial's write allowlist** |
| **T-9** | **The 8-surface `NEVER_ANALYZED` sweep is fragile in two documented ways, and both fired in producing this record.** (a) In `zsh` an unquoted `$VAR` holding a path list **does not word-split**, so the whole sweep silently returned 0 of 8 for its own positive control. (b) Two of the eight surface paths were named in the wrong directory and simply did not exist, under-counting the positive control to 3 of 8 before correction | § 15 | this record — the corrected form is § 15, and it is the form to reuse |
| **T-10** | **`^## FT-<digits>$` matches 46 of 72 queue headings; `^## FT-` matches 72.** 26 headings carry trailing text. **The instrument was defining the population again** — an anchored-to-end-of-line split silently drops a third of the queue | § 15 | Plan |

Design findings **T-1…T-7 remain open and are not resolved here.**

---

## 14 · What this protocol does not do

- It does **not** start the trial, acquire the paper, build a surface, or author a `surface_spec`.
- It does **not** dispatch, register, activate, assign, or grant authority to anyone. The two
  reviews of § 13 are requests for findings and carry no authority in either direction.
- It does **not** create a Task Contract, a candidate, a `DEC`, an approval, or a ledger event.
- It does **not** lift the C-9 hold, verify a capability, acquire a lease, or resolve an `ACTOR_ID`.
- It does **not** adopt, amend, activate or reinterpret OPCON-v1, and it implements **none** of its
  proposals. OPCON-v1 remains `DRAFTED`, `binding: NO`, `ACTIVATION: NOT_REQUESTED`.
- It does **not** add a field to any receipt, manifest or ledger schema. § 2's layer statuses are
  **derived from fields that already exist**, which is why the correction costs no framework change.
- It does **not** modify `governance/`, `roles/`, `framework/`, `ledger/`, `runtime/` or any of the
  four scientific current files.
- It does **not** advance `main` or any other branch, and it stages nothing.
- It does **not** repair T-8, T-9, T-10 or the design's T-1…T-7.
- It does **not** claim actorhood for its author. A session cannot resolve its own actorhood, and
  *"none"* is the correct answer here.
- It does **not** delete or withdraw the design record it transforms. That record holds the
  reasoning these decisions rest on, and the reviews of § 13 cite its blob.

---

## 15 · Verification trail — commands, and the instants they were run

All at `legend-operating-convention-v1` @ `30cb4f3fd700e2aaf6b608e363438f883ddc3760`,
2026-08-23T20:14Z–20:31Z.

```bash
# identity and divergence
git rev-parse HEAD && git rev-parse --abbrev-ref HEAD && git rev-parse main
git log --oneline main..HEAD | wc -l        # 3        git log --oneline HEAD..main | wc -l   # 0
git status --porcelain                      # 2 untracked records under learning/orchestrator/

# the binary model is not repo vocabulary  (§ 2.4)
git grep -l -E "FULL_TEXT_AVAILABLE" HEAD | wc -l   # 0
git grep -l -E "^status:" HEAD | wc -l              # 30   (positive control — CAN fail)
git grep -l -E "zzq_no_such_token" HEAD | wc -l     # 0    (negative control)

# the layer vocabulary that already exists  (§ 2.3)
sed -n '44,75p'  framework/scripts/fulltext_receipts.py    # DEPTHS, COVERAGE_KEYS, COVERAGE_STATES
sed -n '420,432p' framework/scripts/fulltext_receipts.py   # complete_fulltext_read refuses
                                                           #   not_read / unknown_legacy / captions_only
                                                           #   and PERMITS unavailable  ← T-8

# T-8, measured over the union of 128 receipts / 82 papers
#   parse the '| paper | deepest receipt | …' table, NOT the 'papers read in parallel' table above it
python3 - <<'PY'
lines=open('disease-models/wwox/registries/reading_state.md').read().split('\n')
hdr=[l for l in lines if l.startswith('| paper | deepest receipt')][0]
cols=[c.strip() for c in hdr.strip().strip('|').split('|')]
rows=[l for l in lines[lines.index(hdr)+2:] if l.startswith('| PMID')]
bad=[dict(zip(cols,[x.strip() for x in l.strip().strip('|').split('|')])) for l in rows]
hit=[d['paper'] for d in bad if d['deepest receipt'].strip('`')=='complete_fulltext_read'
     and d['supplementary'] not in ('read','not_present')]
print(len(rows), len(hit), hit)          # 82 rows · 9 papers · the nine PMIDs of § 2.4
PY

# 🔴 the NEVER_ANALYZED sweep — the CORRECTED form  (T-9)
#   (a) zsh does NOT word-split an unquoted $VAR: use an array, or the sweep returns 0 for everything
#   (b) two surfaces were named under the wrong directory and silently did not exist
R=disease-models/wwox
surfaces=( $R/registries/reading_state.md  $R/registries/fulltext_read_receipts.jsonl
           $R/research/deepdive_manifests  $R/research/fulltext_dossiers
           $R/research/commit_candidates   $R/registries/claim_registry_current.md
           $R/research/discovery_ledger_current.md  $R/registries/paper_registry_current.md )
for s in "${surfaces[@]}"; do [ -e "$s" ] || echo "MISSING: $s"; done      # none
for pmid in 28123895 42397075 99999999; do
  hits=0
  for s in "${surfaces[@]}"; do
    grep -rqE "(^|[^0-9])${pmid}([^0-9]|\$)" "$s" 2>/dev/null && hits=$((hits+1))
  done
  echo "PMID $pmid -> $hits of 8"
done
#   28123895 → 0 of 8        the trial input, never analyzed
#   42397075 → 5 of 8        POSITIVE CONTROL — fires, and DID fail twice before the two fixes above
#   99999999 → 0 of 8        negative control
#   also 0 of 8: 39933386 · 40263068 · 21444760   (the three alternates)

# the trial input has no local surface  (E-3)
ls files/fulltext/ | wc -l                                   # 174
ls files/fulltext/ | grep -icE "28123895|PMC5214935"         # 0
awk '/^## FT-018/,/^## FT-019/' $R/research/full_text_queue_current.md   # Surface: absent; PMC5214935

# 🔴 queue population — the instrument defined the population, again  (T-10)
grep -c '^## FT-' $R/research/full_text_queue_current.md                          # 72
python3 -c "import re;t=open('$R/research/full_text_queue_current.md').read();\
print(len(re.findall(r'^## (FT-\d+)\s*\$',t,flags=re.M)))"                        # 46  ← WRONG
#   26 headings carry trailing text. Split on '^## FT-\d+.*\$', denominator 72:
#     structured 23 · absent 17 · NO_SURFACE_LINE 17 · pdf_only 10 · UNCLASSIFIED 5

# the instruments the protocol relies on, all present
for s in fulltext_receipts deepdive_manifest locator_audit dossier_quote_audit \
         surface_census caption_census coverage_report trace_claim_foundation \
         figure_ppi_preflight benchmark_input_surface legend_lint; do
  python3 framework/scripts/$s.py --help >/dev/null 2>&1 && echo "OK $s" || echo "?? $s"
done

# the review floor and the audit vocabulary
sed -n '21,43p' governance/annex_c_review_protocol.md    # R0…R5; the mandatory C.2 field set
sed -n '21p'    governance/annex_g_mirror.md             # MIRROR_REQUIRED | MIRROR_SAMPLED | NO_MIRROR
grep -n "MIRROR_REVIEW" governance/annex_d_commit_batch.md   # line 38: n/a | PASS | FAIL   (B-10)

# blobs consumed, and this record's own
git hash-object learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md
#   9d744eb7a284c80b7a6a2e1258fd04f1c9d44036
git hash-object learning/orchestrator/FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md
#   959b57f4c93ccaed087338e5eaf60677fbbcf5c4
git hash-object -w learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1.md
#   → the blob of § 13, written into the object database so both reviewers can read the exact
#     bytes from any worktree via `git cat-file -p <blob>`. It is NOT a commit and NOT a ref:
#     the object is unreferenced and gc-prunable. It survives `git clean`; it is not preservation.
```

> **Every value above is a photograph, and it decays.** A later reader who gets a different number
> should re-run the command beside it and check the **class** first: a population-derived figure
> that moved may mean only that a file was appended, while an object-derived one that moved means
> the repository did. **And three sweeps in this record returned a confident wrong answer before a
> control caught them** — T-9 twice, T-10 once. A sweep without a control that *can fail* is not a
> measurement.
