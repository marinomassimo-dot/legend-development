---
record_type: TRIAL_DESIGN_PROPOSAL
record_id: LEGEND-FIRST-OPERATIONAL-TRIAL-DESIGN-V1
trial_id: TRIAL-001
task_id: FIRST_OPERATIONAL_TRIAL_DESIGN_v1
title: First operational trial of LEGEND on a real scientific case — design, metrics, failure modes
author: unregistered session — no role contract, no ACTOR_ID
session_ref: legend-public-f3 [f8f9ba]
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
  2026-08-23T18:13Z–18:22Z. Every figure below names the command that reproduces it.
predecessors:
  - learning/orchestrator/SCIENTIFIC-PIPELINE-PREPARATION-001.md  (the model)
  - learning/orchestrator/FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md  (the sequence)
  - learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md @ 30cb4f3  (Section S source)
consumes_by_blob: >
  OPCON-v1 read from `plan-orchsurf-r4-transcription:framework/protocols/legend_operating_convention_v1.md`
  @ e4aa80c2f0fc082cf89efa1a89f0642427b751ff — the ONLY ref of 48 carrying that path (§ 3.2, T-2).
  Cited under B.4 H-1b: an integration declares the blob of every source it consumed.
domain: >
  CONTENT. `learning/` is not among the exhaustive CONTROL_PLANE_ROOTS of P5.1
  (`governance/candidates/`, `ledger/`, `reviews/`), so this record sits inside the
  CANDIDATE_CONTENT_HASH of any future candidate rebased onto this branch. Disclosed.
class: WORKING RECORD (OPCON-v1 § B.1.2 row 7) — path chosen so the class holds; the filename is
  the operator's verbatim, the directory is its class home beside its two predecessors.
not_an_slr: >
  Not a Session Learning Record. Annex E.6 governs `SLR-*`; the name is deliberately not `SLR-`.
---

# LEGEND — FIRST OPERATIONAL TRIAL DESIGN v1 · `TRIAL-001`

> **PROPOSAL ONLY · NOT AN AUTHORIZATION · ACTIVATES NOTHING**
>
> This record designs a trial. It dispatches nobody, registers no actor, lifts no hold, issues no
> Task Contract, acquires no lease, adopts no convention, resolves no finding and writes to no
> canonical file. Every blocker named below is discharged by someone else, and § 8 names who.

---

## 0 · What this record is, and the one thing it adds

Two predecessors already exist. `SCIENTIFIC-PIPELINE-PREPARATION-001` established the **model** —
what a Scientist reading is and what it must produce. `FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001`
established the **sequence** — who moves when, and what is blocked.

This record adds the **object**: a trial whose deliverable is *a scientific result about WWOX*,
measured against pre-registered criteria, rather than a coordination sequence that terminates in a
process outcome. It is the first of the three whose success condition includes the four canonical
current files changing.

It also differs from its predecessors in one uncomfortable way, and the difference is the reason
§ 3.2 is where it is: **the paper the laboratory has prepared cannot be the paper this trial
reads**, and that was not measured before today.

---

## 1 · Executive summary

**The recommendation, in one sentence.** Run `TRIAL-001` as a **single-reader scientific loop on
one genuinely unread paper — PMID 28123895 — with a paired unstructured control arm, a blind
locator audit over both arms, one Annex C review, one Mirror R4 on the process, and a COMMIT
CANDIDATE that stops at the operator's gate**; and keep the prepared A/B benchmark
(`BENCH-AB-001`) for a *later* trial, because it measures a different thing and is blocked on
five human decisions this one does not need all of.

Five measured facts shape that recommendation. Each is re-derived in this record, none is
inherited from a prior message, and each names its route.

| # | Fact, measured 2026-08-23 | Route | Consequence |
|---|---|---|---|
| **1** | 🔴 **The prepared benchmark paper is not new evidence.** PMID 42397075 carries `complete_fulltext_read` in `reading_state.md` (line 117), receipt `FTR-20260810-42397075-03`, a schema-2 deep-dive manifest with 22 source artifacts, and a partial-locators dossier. | grep + manifest read | Using it would make the trial's own headline — *"evidence never previously analyzed"* — false. § 3.2 |
| **2** | **Its packet is nevertheless intact: 7 of 7 files present, 7 of 7 digests match**, and the evaluation population re-derives deterministically at **65 units / 109 panels** (two consecutive runs, identical sha256 `b41c7b9f432e48c7`). | `benchmark_manifest.json` + `shasum`; `benchmark_input_surface.py population` ×2 | The A/B benchmark is *prepared and sound*. It is the right instrument for the wrong question here. § 3.2 |
| **3** | 🔴 **Of 72 queue entries, exactly 4 carry a PMID with zero footprint on all 8 analysis surfaces — and none of the 4 has a local full text.** | population by `## FT-` headings, then measured; positive control `42397075` fires on 5 of 8 surfaces, negative control `99999999` on 0 of 8 | The trial's input **must be acquired**, and acquisition is a blocking step, not a formality. § 3.3 |
| **4** | 🔴 **Authority is not held: 0 ACTIVE leases; `scientist-a`/`scientist-b` `NOT_REGISTERED` with `ACTOR_ID UNRESOLVED` by governed decision; all 6 Scientist capabilities `UNVERIFIED`; L2 SUSPENDED by the C-9 hold; all four role contracts `PROPOSED`.** | `lease_state.py`; `orchestrator:runtime/agent_card_registry.md`; `roles/scientist.md`; `PROPOSAL-C9-STATE-MODEL.md` frontmatter | One decision — lifting or scoping the L2 hold — sits upstream of the lease, of assignment, and of everything else. § 8 D-4 |
| **5** | 🔴 **The Operating Convention this trial is asked to use as its working system is `status: DRAFTED`, `binding: NO`, `ACTIVATION: NOT_REQUESTED`, and exists on 1 of 48 refs** — not on `main`. | ref sweep, 48 refs, positive control 18/48, negative control 0/48 | *Using* it is an adoption act the operator has not performed. The trial can still run **under** it as a declared, non-binding working discipline — which is exactly what a trial of a convention should do. § 8 D-3 |

**What the trial is for.** Six dimensions were named in the mandate. Five of them are measurable on
a single LEGEND arm with instruments that exist today. The sixth — *efficiency against a
traditional workflow* — **has no baseline anywhere in this repository**, and cannot acquire one by
being asserted. It becomes measurable only if a control arm is run, and the honest form of the
efficiency question is not *"which reading was faster to produce"* but ***"which reading was
cheaper to check"***. § 6.

**The cost of the recommendation, stated up front.** One paper acquisition, one surface spec
authored by Plan (the real preparation cost — the population block is paper-specific and has
already been defect-repaired twice on the other paper), two reading sessions, one auditor pass per
arm, one review, one Mirror adjudication, one candidate. **Four human decisions are blocking**
(§ 8 D-1, D-2, D-4, D-6) and three are conditional.

---

## 2 · Objective

### 2.1 · What the trial is designed to find out about LEGEND

The mandate named six dimensions. A dimension that cannot be turned into a measurable predicate is
a slogan, so each is restated here as *the thing that will actually be counted*, with the
instrument that counts it. **The full metric definitions are § 6; this table is the mapping, and it
is what makes § 6 auditable rather than assembled after the fact.**

| # | Dimension (mandate) | Measurable predicate | Instrument that exists today |
|---|---|---|---|
| **D-TRACE** | traceability of evidence | every carried statement resolves to a `(proposition, verbatim snippet, anchor)` triple whose artifact is present, digest-matched and locator-exact | `deepdive_manifest.py --verify-artifacts --require-current-schema` · `fulltext_receipts.py verify` |
| **D-SEP** | separation observation / inference / hypothesis | every carried statement typed `DATO` \| `INFERENZA` \| `IPOTESI`; every negative and non-trivial conclusion carries `PREMISE_TAG`; the `Observation` field free of conclusion verbs | mechanical for presence (`deepdive_manifest.py`); adjudicated for substance (Mirror) |
| **D-REPRO** | reproducibility of the reasoning | an independent session, given only the frozen artifacts + the recorded commands, re-derives every number and reaches the same audit verdicts without re-reading the paper | replay by a fresh session; `benchmark_input_surface.py verify-freeze` |
| **D-UNC** | identification of uncertainties | uncertainties and unresolved questions are **outputs with their own records**, not residue: `RESIDUAL_UNCERTAINTY`, `EVIDENCE_NEEDED`, `WHAT_WOULD_CHANGE_MY_MIND` populated and non-generic | Annex C.2 fields; count + Mirror on substance |
| **D-REV** | quality of the critical review | blind audit verdict distribution per arm: `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE`; defects caught by the audit that the reader's own self-check did not | `legend-locator-audit` skill · `locator_audit.py` · fresh blind sessions |
| **D-EFF** | efficiency vs a traditional workflow | **two figures, never one**: production cost (arm wall-clock, from receipts) and **verification cost** (auditor minutes per claim, and fraction of claims an auditor could not locate at all) | receipts for time; the auditor's own log for verification cost |

> 🔴 **D-EFF is the one dimension with no historical baseline.** Nothing in this repository records
> a traditional-workflow reading of any paper with a measured time or token cost. A comparison
> against a remembered or estimated baseline would be the exact failure OPCON-v1 § S.7.1 forbids —
> *mandate the command, never the integer*. **Either the control arm runs, or D-EFF is reported as
> `NOT MEASURED` with this sentence as the reason.** It is not reported as a favourable impression.

### 2.2 · The scientific question the trial answers about WWOX

Bound at paper selection (§ 8 D-1). For the recommended paper — **PMID 28123895, Bandini 2016,
*The non-inflammatory role of C1q during Her2/neu-driven mammary carcinogenesis*** — the question is:

> **Does this paper establish that C1q regulates the *activation state* of WWOX rather than its
> *level*; on what measured intermediate does that rest; and what, if anything, transfers from
> Her2/neu-driven mammary carcinogenesis to the WWOX-DEE reference genotype class?**

That question was chosen because it is genuinely open, genuinely relevant, and because **three
gates of `framework/eval/failure_taxonomy.md` are live inside it at once** —
`MECHANISTIC_OVERTRANSFER` (a route measured in a tumour model is a hypothesis for a
loss-of-function neurodevelopmental context, not a datum), `MECHANISM_DIRECTNESS_GATE` (activation
state is an intermediate that must be *measured*, not inferred from a phenotype), and
`KG_EDGE_HAS_NO_SIGN` (an edge is relevance, never direction). **A trial paper on which the
epistemic gates cannot fire measures nothing about epistemic discipline.**

The queue's own entry for it (`FT-018`, priority `HIGH`) already records a calibration defect worth
carrying into the trial: the priority matrix scored it `P3_LOW` on the BLOCK-1/safety axis while
its actual content is neuroinflammation + repurposing, and it was queued `HIGH` *against* the tier
under the rule *"ranking orders reading; it never authorizes not reading"*
(`READING_DEBT_FALSE_NEGATIVE`).

### 2.3 · What this trial is explicitly not

- **Not a mode benchmark.** It does not compare `MODE A` against `MODE B`. That is `BENCH-AB-001`,
  it is prepared, and it should run *after* one mode is known to work end to end.
- **Not framework construction.** No new protocol, no new rule, no new script beyond the one
  paper-specific surface spec § 5.2 Φ1 requires. Gaps found become findings (§ 10), not repairs.
- **Not a statistical study.** One paper, one reader per arm. Session variance is not separable
  from arm. Its value is the **material** it produces and the failure modes it surfaces.
- **Not medical advice**, and not an individual-level record. The trial reasons about the WWOX-DEE
  reference genotype class.

---

## 3 · Scope

### 3.1 · Pre-flight, re-derived today — not inherited

**MEASURED_AT: `legend-operating-convention-v1` @ `30cb4f3`, 2026-08-23T18:13Z–18:22Z.**
Every value here is a photograph and it decays (body § 43, OPCON-v1 § S.7.6); each row names how to
re-derive it.

| # | Class | Route | Measured today | Verdict |
|---|---|---|---|---|
| **PF-1** | system state | `framework/state/state_manifest_current.md` | `current_state: READY` (line 141) | ✅ |
| **PF-2** | structural LINT | `python3 framework/scripts/legend_lint.py .` | `VERDICT: PASS` · 1 `[INFO] MISSING_WIKILINK` | ✅ |
| **PF-3** | lease | `python3 framework/scripts/lease_state.py` | 5 leases; **`ACTIVE by derivation: 0`**; lease #3 `derived=STALE` vs `stored=EXPIRED` | 🔴 **BLOCKED** |
| **PF-4** | actor registration | `git show orchestrator:runtime/agent_card_registry.md` | `PARTIALLY REGISTERED — 3 of 6`; `scientist-a`/`-b` `NOT_REGISTERED`, `ACTOR_ID: UNRESOLVED`; `orchestrator` `STATUS: BOOTSTRAP_CONTROLLER` | 🔴 **BLOCKED** |
| **PF-5** | capabilities | `roles/scientist.md` | **6 of 6 `UNVERIFIED`**; contract `status: PROPOSED` | 🔴 **BLOCKED** |
| **PF-6** | the L2 hold | `governance/candidates/PROPOSAL-C9-STATE-MODEL.md` frontmatter | `status: ACCEPTED` · `acceptance_is_not_adoption: true` · `hold: … L2 suspended` | 🔴 **BLOCKED** — upstream of PF-3, PF-5 |
| **PF-7** | role activation | `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` | `BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE`; activation did **not** happen; a new explicit act is required | 🔴 **BLOCKED** |
| **PF-8** | tooling | presence + `--help` | **8 of 8 present**: `benchmark_input_surface.py` (7 subcommands), `deepdive_manifest.py`, `lease_state.py`, `fulltext_receipts.py`, `legend_lint.py`, `corpus_firewall.py`, `public_release_gate.py`, `failure_taxonomy.md` | ✅ **GREEN** |
| **PF-9** | seats | `git worktree list` | 25 worktrees; 11 non-scratch; all role seats present. 🔴 **`mirror` tip is `2767333` — it was `da52ee5` on 2026-08-22 and `1892071` the day before. It has now moved twice with no instrument reporting either move.** | 🟡 **PRESENT, RE-DERIVE** |
| **PF-10** | trial input | `files/fulltext/` + queue cross-check | **absent** for all four never-analyzed candidates | 🔴 **BLOCKED — § 3.3** |
| **PF-11** | external acquisition | MCP connector state, this session | claude.ai PubMed / bioRxiv / Scholar Gateway **require authorization and are unavailable here** | 🔴 **BLOCKED — § 8 D-2** |

**Three of the eleven are green, and the green ones are the machine.** Every blocking row is
authority, registration, or input — none is capability of the tooling.

### 3.2 · 🔴 Finding T-1 — the prepared paper cannot be the trial paper

`BENCH-AB-001` fixes PMID 42397075 (Aqeilan et al., *Brain* 2026, patient-derived neural
organoids). Its packet re-verifies clean today:

```
7 of 7 SOURCE_FILES present, 7 of 7 sha256 match declared     (benchmark_manifest.json + hashlib)
population: 65 units / 109 panels, deterministic over two runs (identical sha256 b41c7b9f432e48c7)
  main_figure 6 · main_results_section 7 · main_methods_section 2 · main_table 0
  supplementary_figure 10 · supplement_methods_section 24 · supplement_table_section 7
  source_data_blot 9
```

And the same paper measures as **already read**:

| Surface | Measured | Route |
|---|---|---|
| `reading_state.md` line 117 | `complete_fulltext_read` — 10 of 11 section columns `read`, 1 `not_present` | grep |
| `deepdive_manifests/PMID42397075.json` | schema 2, receipt `FTR-20260810-42397075-03`, 22 `source_artifacts`, `verbatim_locators` present | json read |
| `fulltext_dossiers/PMID42397075_partial_locators.md` | 12 locators captured 2026-08-09, with a recorded 🔴 preflight finding | file read |
| `full_text_queue_current.md` `FT-010` | *"letto parzialmente il 2026-08-09"*, receipts `-01` and `-02` | grep |

**The conflict is not about the surface — it is about the claim.** The benchmark surface blinds a
reader *mechanically* (allowlist, forbidden-prior-output paths, content scan), so a reader placed
in it sees no prior LEGEND output. What it cannot do is make the sentence *"a new WWOX evidence
never previously analyzed by the system"* true. **A trial whose headline is false at the start
measures nothing, however clean its instruments.**

`BENCH-AB-001` is not thereby wasted. It is the correct instrument for the question it was built
for — *does the mode directive change the reading* — and § 6.3 of the coordination plan already
argued, independently, that it is the more expensive experiment and proves the less fundamental
thing. **Keep it; run it second.**

### 3.3 · The candidate set, measured

**Population enumerated first, by an instrument that cannot see the property** (OPCON-v1 § S.7.2b):
the 72 `## FT-` headings of `full_text_queue_current.md`. Then the predicate `NEVER_ANALYZED` was
measured into that fixed denominator.

```
NEVER_ANALYZED(pmid)  ≔  the PMID appears, as a digit-bounded token, in NONE of:
   reading_state.md · fulltext_read_receipts.jsonl · deepdive_manifests/ (64 files)
   fulltext_dossiers/ (33) · commit_candidates/ (17) · claim_registry_current.md
   discovery_ledger_current.md · paper_registry_current.md
   ── deliberately EXCLUDING corpus seeds and batch_queue: appearing in a triage list is
      being SEEN, not being ANALYZED, and conflating them makes the predicate unsatisfiable
positive control  PMID 42397075 → fires on 5 of 8 surfaces
negative control  PMID 99999999 → fires on 0 of 8 (an unanchored substring test fired once —
                  the anchor is load-bearing, and the naive form was discarded, not reported)
```

**Result: 4 of 72 queue entries.** None has a local full text.

| Entry | PMID | Priority | Title | Local full text |
|---|---|---|---|---|
| `FT-018` | **28123895** | **HIGH** | The non-inflammatory role of C1q during Her2/neu-driven mammary carcinogenesis | ❌ (`PMCID PMC5214935`, recorded open) |
| `FT-017` | 39933386 | LOW-MED | Infantile Epileptic Spasms Syndrome: clinical and genetic variability, Argentina case series | ❌ |
| `FT-015` | 40263068 | MED-HIGH | Corrigendum — WWOX attenuates the progression of gallbladder cancer | ❌ |
| `FT-019` | 21444760 | MEDIUM | The mouse QTL map helps interpret human GWAS | ❌ |

**Recommended: `FT-018` / PMID 28123895** — for the reasons in § 2.2, plus: it is the only `HIGH`
in the set, its abstract has already been triaged (so the scientific question is formed rather than
fished for), and its recorded PMCID makes acquisition tractable. **Alternate: `FT-017`**, if the
operator prefers a clinical-phenotype object over a mechanistic one. `FT-015` is a corrigendum —
too small to exercise the dimensions. `FT-019` is methodological and only distantly WWOX-relevant.

> ⚠️ **One honesty note on the alternate.** `FT-017`'s own queue entry says it is useful *"only if
> WWOX appears in the cohort"*. That is unknown until the paper is read, so choosing it accepts a
> real chance that the trial's scientific yield is a filter decision. That is not a bad trial
> outcome — a well-documented `DISMISSAL` is a legitimate product — but the operator should choose
> it knowingly.

### 3.4 · In scope / out of scope

```
IN     one paper · two arms (LEGEND, control) · blind locator audit of both · one Annex C review
       · one Mirror R4 on the process · one COMMIT CANDIDATE · one operator gate · one outcome
       · one friction log · one SLR

OUT    a second paper · Scientist C and the § 32 synthesis conflict it instantiates
       · the MODE A / MODE B comparison · any governance amendment · any PROPOSAL implementation
       · any write to governance/, roles/, framework/protocols/ or plan_defined_parameters.md
       · any push to a public remote · any paid external service (J.4 DEFAULT_EXTERNAL_SPEND = 0)
```

### 3.5 · The write allowlist — declared before the run, so drift is visible

The trial may create or append to exactly these paths. **Anything outside this list is F-1
(§ 7) firing, and is the signal that the trial has turned back into framework construction.**

```
files/fulltext/<the trial paper>*                        (git-ignored; acquisition)
framework/eval/benchmarks/TRIAL-001/surface_spec.json    (the one new artifact Φ1 requires)
framework/eval/benchmarks/TRIAL-001/…                    (manifest, population, frozen receipts)
disease-models/wwox/research/fulltext_dossiers/…         (the reading's locators)
disease-models/wwox/research/deepdive_manifests/…        (the work manifest)
disease-models/wwox/research/commit_candidates/…         (the candidate)
disease-models/wwox/registries/…                         (ONLY via BATCH_COMMIT, after D-9)
learning/orchestrator/TRIAL-001-*                        (friction log, outcome, SLR)
reviews/<reviewer>/REV-TRIAL001-*                        (review + audit records)
```

---

## 4 · Roles

**The test applied to every row: does this role produce an artifact that some other role's absence
would leave missing?** A role that only reviews someone else's summary is not allocated.

| Role | Function in this trial | Verifiable output | Registration state today | Dimensions it is required for |
|---|---|---|---|---|
| **Operator** | the four blocking decisions; the commit gate; and — measured, not rhetorical — **the control plane itself**: routing, dispatch and anything that must happen between turns | `DEC-*` / approval entries | n/a | all — the trial cannot start without D-1, D-2, D-4, D-6 |
| **Reader · arm L** | the LEGEND reading: full text → receipt → work manifest with verbatim locators → coverage map → typed claim candidates → COMMIT CANDIDATE | receipt, manifest, dossier, candidate | 🔴 `scientist-a` `NOT_REGISTERED`, capabilities `UNVERIFIED`, L2 suspended | D-TRACE, D-SEP, D-UNC, D-EFF |
| **Reader · arm T** (control) | the same paper, same bytes, same question, **no LEGEND scaffolding**: no locator obligation, no typing vocabulary, no receipt, no coverage map. Free-form analysis notes | `TRIAL-001-ARM-T-NOTES.md` | n/a — **not a LEGEND actor**, and must not be registered as one | D-EFF, D-REV (as comparator) |
| **Plan** | build the surface · `verify` · enumerate the population · **FREEZE on each completion declaration, before reading content** · mechanical checks · the comparison · the outcome summary | surface, manifest, freeze receipts, outcome | ✅ registered 2026-08-17, `REGISTERED_PENDING_L1_L2`; contract `PROPOSED` | D-REPRO, and the timing guarantee of the whole run |
| **Blind auditors** (fresh, ephemeral) | audit every `(proposition, snippet, anchor)` triple of arm L; and, for arm T, **first locate** the evidence for each claim, logging the attempt | `reviews/…/REV-TRIAL001-AUDIT-*` | none needed — ephemeral, identity withheld | **D-REV, D-EFF** — the highest value per unit of governance cost in the whole design |
| **Reviewer** (Annex C floor) | the scientific review of the reading's inferences at the floor for the claim class: `R1` for an ordinary L2 inference, **`R2` if any claim is therapeutic-actionable** | `REV-TRIAL001-*` with the full C.2 field set | — | D-REV, D-UNC |
| **Mirror** | **R4 on the process, not on the paper.** Was the freeze timing shown? Did the audit run blind? Were uncertainties outputs or residue? Did the trial stay inside its write allowlist? | `REV-TRIAL001-MIRROR-001` | ✅ registered, `ACTIVE — IDLE (REGISTERED_PENDING_L1_L2)` | the judgement that the *method* held |

### 4.1 · Roles deliberately not allocated, with the reason

| Not allocated | Why |
|---|---|
| **Scientist C** | Its dispatched "synthesis / conflict resolution" function collides with body § 32 equivalence, H.1 adjudication authority and § 27 on forced consensus — an open, unresolved conflict. A single-reader trial **does not instantiate it**, and that is a saving, not an omission. |
| **A second Scientist (A/B)** | That is `BENCH-AB-001`. Adding it doubles the blocking decisions (both readers must be registered and L2-verified) to measure a *mode difference* the mandate did not ask about. |
| **Codex / R5 cross-model** | C.1 makes R5 the floor for *"casi cross-model specificati"*. This trial specifies none. Allocating it would be creating a role on principle. |
| **Metacognition agent** | Explicitly out of `controlled_benchmark_ab.md` § 10's scope, and nothing here needs it. |

### 4.2 · The degradation ladder — what the operator loses by cutting

Stated so a cheaper trial is a **choice with a known cost**, not an accident.

```
FULL          reader-L + reader-T + Plan + auditors + reviewer + Mirror   → all six dimensions
─ Mirror      … everything except R4                                      → lose: the judgement that the METHOD held.
                                                                             The trial still produces a reading; nothing
                                                                             judges whether the trial was run correctly.
─ arm T       … single arm                                                → lose: D-EFF entirely. Report it NOT MEASURED.
─ Plan        … reader + auditors + operator                              → lose: the FREEZE. Without a freeze taken
                                                                             before anyone reads the content, D-REPRO is
                                                                             unprovable — the trees could still move.
─ auditors    … reader alone                                              → lose: D-REV and the only instrument that
                                                                             catches a reading that says MORE than its
                                                                             source. This is the cut never to make:
                                                                             R-5 records a blind reviewer finding eight
                                                                             defects two informed reviewers had passed
                                                                             over twice.
MINIMUM VIABLE   reader-L + blind auditors + operator gate                → D-TRACE, D-SEP, D-UNC, partial D-REV
```

---

## 5 · Workflow

### 5.1 · Two arms, and why the control exists

```
                    ┌── arm L · LEGEND reading ──── receipt · manifest · locators · typed claims ──┐
frozen surface  ────┤                                                                              ├── blind audit ── review ── Mirror R4 ── outcome
                    └── arm T · unstructured read ── free-form notes, no anchors ──────────────────┘
```

**The comparison is not "which reading is better".** Without a gold-standard reading of this paper,
that question has no instrument, and inventing one would be the failure this whole design exists to
avoid. The comparison that *does* have an instrument is:

> **Given each arm's output and the frozen source, how expensive is it for an independent party to
> check a claim — and how many claims can be checked at all?**

Arm L's claims arrive with anchors; the auditor verifies. Arm T's claims arrive without; the
auditor must first *find* the evidence, and may fail. **The asymmetry is declared here, in advance,
as the measurement — not discovered afterwards and reported as arm T's defect.**

> 🔴 **A known contamination of the variable, recorded and not softened.** Arm T is run by the same
> class of reader that has LEGEND's discipline internalised. It will therefore be *better* than a
> genuinely naive traditional workflow, which biases D-EFF **against** LEGEND. That direction is
> the safe one — a favourable result survives the bias — but a null result does **not** license the
> conclusion that the discipline is worthless.

### 5.2 · Phase sequence

Owner · input · output · gate. **`main` is not written by any phase.**

| Φ | Owner | Act | Output | Gate |
|---|---|---|---|---|
| **Φ0** | operator + any session | **PRE-FLIGHT re-derived at the moment**, by the routes of § 3.1 — never read from this table | `TRIAL-001-PREFLIGHT.md` | every row satisfied *at the moment of handover*, or the trial does not start |
| **Φ1** | Plan | acquire the full text → `fulltext_receipts.py record`; author `surface_spec.json`; `build --emit-digests`; `verify`; `population`; **FREEZE the input manifest** | surface ×2, digests, population, `FROZEN_SHA256` set | `verify` refuses on parity failure, forbidden path, unlisted file or content-scan hit |
| **Φ2** | operator (or Orchestrator **iff** a lease is ACTIVE) | issue the two assignments under one group id: `TRIAL-001-L` and `TRIAL-001-T` | 2 contracts under `ledger/tasks/…` | Annex A.1 requires a resolvable `OWNER (ACTOR_ID)` — see § 8 D-4 |
| **Φ3** | Plan → each reader | HANDOVER: writer transfer + memory-scope check **recorded**, not asserted | `HANDOVER` block in the manifest | one writer per surface, transferred once |
| **Φ4** | readers, **concurrent and mutually blind** | arm L reads under the reading obligations; arm T reads under none | reading outputs in the surface output slots | no contact; no sight of the other; no prior LEGEND output |
| **Φ5** | Plan | **FREEZE each reading ON its completion declaration, BEFORE reading its content** | `RECEIPT-<arm>.json` with `FREEZE_TIMESTAMP_UTC`, `SURFACE_COMMIT`, `FIRST_PASS_STATE` | *a freeze taken after Plan has read the content is a freeze whose timing cannot be shown* |
| **Φ6** | Plan | mechanical checks: `deepdive_manifest.py --verify-artifacts --require-current-schema`; coverage over the fixed population; `fulltext_receipts.py verify`; `legend_lint.py`; `verify-freeze` | check log, coverage map | any refusal halts and is recorded — **a refusal is a result** |
| **Φ7** | fresh blind sessions | locator audit, **both arms**, reader identity withheld; per triple: `SUPPORTED · OVERSHOOT · UNDERSHOOT · NOT_IN_SOURCE · UNVERIFIABLE_SURFACE`; for arm T also `time-to-locate` and `NOT_LOCATABLE` | `REV-TRIAL001-AUDIT-L/T` | the auditor never sees the dossier, the reader's name, or the conclusions |
| **Φ8** | reviewer | Annex C review at the floor for the claim class, full C.2 field set including `WHAT_WOULD_CHANGE_MY_MIND` and `AUTHOR_RESPONSE` | `REV-TRIAL001-*` | AUTHOR ≠ REVIEWER; max 2 rounds → adjudication; `DISAGREEMENT_UNRESOLVED` is legitimate |
| **Φ9** | Mirror | **R4 on the process** | `REV-TRIAL001-MIRROR-001` | 🔴 Mirror's stated primary surface (the J.1 consolidated event ledger) **does not exist** — § 10 T-4. Its input is scoped, by declaration, to the frozen artifacts and receipts |
| **Φ10** | reader-L → operator | COMMIT CANDIDATE assembled; **stops at the gate** | `commit_candidates/CC-TRIAL001-…` | 🔴 **§ 8 D-9** — and see T-5 on `MIRROR_REVIEW` |
| **Φ11** | Plan | outcome summary — **each dimension its own table, no composite, no weighting**; operational figures in a separate table that breaks no tie | `TRIAL-001-OUTCOME.md`, `TRIAL-001-FRICTION-LOG.md`, one SLR | every count is an enumerated set or carries the command that produced it |

### 5.3 · How a session is opened

Under OPCON-v1 § S.1–S.4, applied as a **declared, non-binding working discipline** (§ 8 D-3):

1. The session records `(pwd, session id)` — occupancy is established by nothing weaker (S.2.2).
2. It **does not claim actorhood**. A session cannot resolve its own actorhood (S.1.2); *"none"* is
   a correct answer, and every trial artifact says which it is.
3. Occupancy of the working directory is measured by **polling peers**, not inferred (S.2.3). A
   co-occupant is a hazard even with zero conflicting writes — one `git clean` from any of them
   destroys every untracked artifact (S.2.4).
4. One writer per file for its lifetime in the working tree (S.2.5).
5. Every timestamp is derived from the **raw epoch** — `date -u -r <epoch>` — never from a renderer
   that hardcodes a literal `Z` (S.4.1). `cp -p` and `git archive` forge mtime and birthtime, so no
   trial measurement attributes work by mtime (S.4.2).
6. **Preservation does not wait for attribution** (S.3.3). `WORK_COMMIT` of the session's own named
   paths on its own branch is the author's own authority (S.6.1) and should happen early.

### 5.4 · Artifacts and attribution

Every trial artifact carries, in frontmatter:

```yaml
author:        <seat, or "unregistered session — no role contract">
session_ref:   <name> [<ref>]      # attribution AID, not proof (S.3.4)
actor_id:      <resolved id, or NOT ESTABLISHED>
measured_at:   <branch> @ <sha>, <UTC instant>
consumes_by_blob: <blob ids of every source consumed>   # B.4 H-1b
```

Attribution ranks (S.3): rank 1 is a claim **plus an artifact independent of the claim** — for an
uncommitted file, the harness-written transcript `tool_use` entries. Rank 4, *elimination by
`started`*, is **invalid**: `started` is a property of the runtime incarnation, not of the
conversation (S.1.4). Absent `session_ref` ⇒ `UNATTRIBUTED`, and an unattributed artifact **is
claimed before anyone commits it**.

### 5.5 · When Mirror intervenes — and when it must not

```
Φ9      R4 on the process, after both arms are frozen and audited.        ← the allocated intervention
Φ0 (optional, recommended)  a blind R4-shaped read of THIS design, bound by blob, before Φ1.
NEVER   as a third reader of the paper. R4 is not a reading; Mirror's object is the process (Annex G).
NEVER   as the authority that lifts a blocker. Mirror produces findings, never authorizations.
```

### 5.6 · Escalation

The floor is OPCON-v1 § S.8 — **a floor, never a ceiling**. These always reach the operator: a
frozen rule would have to change · an irreversible governance choice is required · two valid
interpretations produce materially different architectures · a body § 48 stop condition is live ·
money would be spent (J.4 `DEFAULT_EXTERNAL_SPEND = 0`) · an authority nobody holds would have to be
allocated · the act requires an ACTIVE lease and none is held.

**An escalation is decision-shaped** (S.8.1): the decision in one sentence, the options, a
recommendation with its rationale, and what proceeds regardless. **A diagnostic report is not an
escalation**, and a session with nothing to do while it waits has scoped its own work wrongly.

### 5.7 · The arm-L ↔ arm-T barrier, labelled in the Annex J.0 style

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

## 6 · Metrics

### 6.1 · The three rules that govern every number below

1. **No composite, no weighting, no overall score.** Each dimension reports in its own table.
2. **Operational figures never proxy for quality.** Time, tokens, output volume and arm agreement
   are recorded because they are cheap to record and someone will ask. They are reported apart,
   they break no tie, and **a reading is not better for being faster, shorter or cheaper.**
3. **Every figure carries its command, the instant it was run, and its class** (OPCON-v1 § S.7.6,
   § S.7.7) — `population-derived` figures decay on their own; `object-derived` figures do not.
   A reader who catches `27` reading `28` must be able to tell whether the instrument moved or the
   repository did.

### 6.2 · Primary dimensions

| Dimension | Unit / measure | Route | Evaluator | Class |
|---|---|---|---|---|
| **D-TRACE** | claims with ≥1 anchored locator ÷ claims carried; manifest `PASS` under `--verify-artifacts --require-current-schema`; `source_artifacts` complete; coverage map consistent with where locators come from | mechanical | Plan | object |
| **D-SEP** | statements typed `DATO`/`INFERENZA`/`IPOTESI` ÷ statements carried; negatives with `PREMISE_TAG` + revival trigger; `DEFAULT_FROM_TEXTBOOK` declared where used; count of hypothesis→observation promotions **found by the audit** | mechanical for presence; adjudicated for substance | Plan; Mirror | object |
| **D-REPRO** | a fresh session, given only frozen artifacts + recorded commands, reproduces: every reported count, the population digest, and the audit verdict per triple. Report **matches ÷ attempted**, and every mismatch verbatim | replay | independent session | object |
| **D-UNC** | uncertainties recorded as their own entries; `RESIDUAL_UNCERTAINTY` / `EVIDENCE_NEEDED` / `WHAT_WOULD_CHANGE_MY_MIND` populated and **specific** (a falsifier that no observation could satisfy counts as absent) | presence mechanical; substance adjudicated | Plan; Mirror | object |
| **D-REV** | audit verdict distribution per arm; **defects the audit caught that the reader's own self-check did not**; failure-taxonomy gate instances per arm, with locator | blind audit; Mirror | blind agents; Mirror | object |
| **D-EFF** | **(a) production cost**: handover → completion declaration, per arm, wall clock from the receipts. **(b) verification cost**: auditor minutes per claim, per arm; and `NOT_LOCATABLE` claims ÷ claims audited, per arm | receipts; auditor log | Plan lists; nobody scores | object |

### 6.3 · Operational — recorded apart, never a quality proxy

| Figure | Definition | Route | Note |
|---|---|---|---|
| total wall time | first Φ0 command → `TRIAL-001-OUTCOME.md` written | receipts + commit timestamps, epoch-derived | includes blocked time — see below |
| **blocked time** | cumulative time in states waiting on a human decision | the friction log | 🔴 **the figure that tests § 5.2's claim that the operator is the control plane** |
| token / cost | **`NOT OBSERVABLE` unless the runtime exposes it — never estimated** | — | If the operator can read a per-session figure, record it; otherwise the cell says `NOT OBSERVABLE`, and that is the honest entry |
| revisions | `WORK_COMMIT`s on the reading branch + review rounds (C.3 caps at 2 → adjudication) | `git log`, review records | |
| findings produced | claim candidates typed, by type; contradictions/negatives carried; unresolved questions | manifest + dossier | |
| errors intercepted | audit verdicts ≠ `SUPPORTED`; Mirror findings; **mechanical refusals** (`verify`, `verify-freeze`, LINT, manifest) | logs | a refusal is an interception, and is counted as one |
| analysis vs correction | wall time before first completion declaration vs after | receipts + commits | coarse by construction; labelled as coarse |

### 6.4 · The friction log — the one required metric with no instrument

`TRIAL-001-FRICTION-LOG.md`, append-only, **written during the run and never reconstructed
afterwards**. One line per event, at the moment:

```
<epoch> | <UTC from `date -u -r <epoch>`> | <phase> | <what stopped, or had to be re-derived,
        or had no owner> | <who unblocked it> | <minutes lost>
```

Three classes are mandatory to log: **(a)** any point where the protocol forced a stop; **(b)** any
figure a receiver had to re-derive because a dispatch's stated value was wrong — *both halves get
logged, because a log that records only the error teaches the next dispatcher to supply fewer
facts, when the lesson is that the receiver re-runs them*; **(c)** any decision that had no owner.

**This log is the trial's most valuable output and the one most likely to be skipped.** Everything
else can be reconstructed from artifacts; friction cannot.

### 6.5 · Pre-registered success criteria — and their falsifiers

Registered **before** the run, so a disappointing result cannot be re-described afterwards.

**The trial succeeds *as an experiment* if** — and this is independent of whether LEGEND comes out
well — every phase produced its artifact, both arms froze with shown timing, the audit ran blind,
the mechanical gates ran (pass or refuse, both recorded), Mirror adjudicated the process, and the
outcome reports each dimension separately with the route that produced each number.

**LEGEND is judged to improve a dimension only against these, each with its falsifier:**

| Dimension | Improvement criterion | Falsifier — what would show the opposite |
|---|---|---|
| D-TRACE | every claim in arm L resolves to a digest-matched, locator-exact triple; manifest `PASS` | any claim carried without a resolvable anchor, or a manifest that cannot pass its own validator |
| D-SEP | 100 % of carried statements typed; every negative carries a premise tag | the audit finds a hypothesis carried as an observation |
| D-REPRO | an independent session reproduces every reported count and verdict from the record alone | any figure that cannot be re-derived without asking its author |
| D-UNC | uncertainties are entries with falsifiers, not adjectives | `WHAT_WOULD_CHANGE_MY_MIND` present but unsatisfiable by any observation |
| D-REV | the blind audit finds ≥1 defect the reader's self-check did not | the audit finds nothing and the reader found nothing — **which is evidence about the audit, not a clean bill** |
| D-EFF | **verification cost per claim is lower for arm L, and arm L's `NOT_LOCATABLE` fraction is lower** | arm T's claims are located and checked as fast and as reliably as arm L's → **the traceability advantage is not supported by this trial**, and the outcome says exactly that |

> **`NO IMPROVEMENT MEASURED` is a legitimate, publishable outcome.** So is
> `DISAGREEMENT_UNRESOLVED`. Neither is re-run to a better number. A trial that can only succeed is
> not an experiment.

---

## 7 · Failure modes — how LEGEND could fail this trial

| # | Failure | Why it is likely here | Early signal | Guard |
|---|---|---|---|---|
| **F-1** | 🔴 **The trial becomes framework construction** — the mandate's own stated risk, and the repository's demonstrated gravitational pull | every predecessor record grew a governance analysis inside a scientific task | any write outside the § 3.5 allowlist; any new rule proposed mid-run | the allowlist is declared **before** Φ0; gaps become § 10 findings, not repairs |
| **F-2** | The reader reads its own prior output | guaranteed if the paper is 42397075 (§ 3.2); possible for any paper via the repo's own dossiers | a locator pointing at a LEGEND file instead of the source | `forbidden_prior_output_paths` + content scan; `verify` refuses |
| **F-3** | The freeze is taken after Plan read the content | it is the cheapest corner to cut under time pressure | `FREEZE_TIMESTAMP_UTC` later than the first content read | Φ5 ordering; the receipt records both instants |
| **F-4** | Arm T is contaminated by internalised LEGEND discipline | same model class in both arms | arm T spontaneously produces anchors | declared in § 5.1 as a known contamination; biases **against** LEGEND, so a favourable result survives it |
| **F-5** | 🔴 **The population enumerator is wrong** | it was wrong **twice** on the other paper — a fixed caption window ran 925 characters into the next caption and reported 12 panels for a caption printing 6; hand-listed methods headings were short by 4 | counts that change between two runs, or that a hand check contradicts | determinism check (two runs, identical digest) **plus** one independent hand enumeration before freeze |
| **F-6** | A reported figure decays between measurement and report | measured: every population-derived figure in the convention's own audit decayed within an hour; every object-derived one held | a number with no command and no instant beside it | § 6.1 rule 3 — command + instant + class on every figure |
| **F-7** | 🔴 **A sweep lies silently** | five distinct mechanisms are already documented in this laboratory: scope, anchor, syntax, shell word-splitting, wrong object | a sweep with no positive control; a control that shares the search's flaw | every sweep carries a control **that can fail**; the population is enumerated by an instrument that cannot express the property. *This record's own first ref sweep returned `0/48` for the target **and `0/48` for its positive control** — a zsh word-splitting fault. It was caught by the control and re-run; the corrected sweep is § 3.2's* |
| **F-8** | **The operator becomes the bottleneck** | measured: for this run, The Operator *is* the control plane — routing, dispatch and everything between turns | blocked time exceeds reading time | § 6.3 measures it explicitly; § 8 front-loads every blocking decision |
| **F-9** | 🔴 **The candidate cannot pass its gate** | measured, § 10 T-5: **8 of 8 CAND manifests carry `MIRROR_REVIEW`; 0 carry a value in the frozen vocabulary** `n/a \| PASS \| FAIL` | Φ10 produces a candidate no one can mark conformant | Φ10 **stops at the operator gate by design**; the trial's product is the candidate, not the commit |
| **F-10** | Escalations arrive as diagnostics | the failure S.8.1 was written against | a message that reports a problem and asks nothing | escalations are decision-shaped or they are not sent |
| **F-11** | Attribution or work is lost to co-located sessions | measured precedent: 12 untracked files across two seats, 3 claimed, **0 overwritten** — the exposure is that one `git clean` destroys them all | an untracked trial artifact older than an hour | `WORK_COMMIT` own named paths early; poll occupancy before writing |
| **F-12** | **The reading is excellent and proves nothing** | a single good reading is not evidence about a system | the outcome reads as a paper summary rather than a dimension-by-dimension table | Φ11's reporting rules; Mirror's R4 object is the process |

> 🔴 **The failure mode that would be worst, stated plainly.** Not that the trial fails — that
> the trial *succeeds decoratively*: every artifact produced, every gate green, and no claim in the
> outcome that an independent party could falsify. **F-12 and the D-REV falsifier are the two
> guards against it, and both work only if they are read before the run rather than after.**

---

## 8 · Decisions required of the operator

Each is decision-shaped (S.8.1): one sentence, the options, a recommendation, and what proceeds
regardless. **Nothing in this record performs any of them.**

| # | Decision | Options | Recommendation | Proceeds regardless |
|---|---|---|---|---|
| **D-1** 🔴 | **Which paper does `TRIAL-001` read?** *Scope is `Strategia complessiva → Operatore` (H.1); this record orders within a scope, it does not set one.* | (a) **PMID 28123895** `FT-018` HIGH · (b) PMID 39933386 `FT-017` · (c) PMID 42397075 — prepared but already read · (d) a paper the operator supplies | **(a)** — the only `HIGH` of the four measured never-analyzed candidates, abstract already triaged, three failure-taxonomy gates live in it | nothing; Φ1 cannot start |
| **D-2** 🔴 | **How is the full text acquired?** The claude.ai PubMed / bioRxiv / Scholar connectors **require authorization and are unavailable in this session.** | (a) authorize the connectors · (b) the operator supplies the PDF · (c) run `find-fulltext` in a session with web access | **(b) or (c)** — fastest, and `PMC5214935` is recorded as open | nothing; Φ1 cannot start |
| **D-3** 🔴 | **Does `TRIAL-001` run *under* OPCON-v1?** It is `DRAFTED`, `binding: NO`, `ACTIVATION: NOT_REQUESTED`, on **1 of 48 refs** and not on `main`. | (a) **run under it as a declared non-binding working discipline**, and let the trial be its first field test · (b) adopt it first (a governance act) · (c) run without it | **(a)** — it costs nothing, it changes no frozen rule, and it produces exactly the evidence an adoption decision would need. **(b) is a separate decision this trial should not force.** | the trial can run either way; only the outcome's scope changes |
| **D-4** 🔴 | **Is the C-9 hold on L2 lifted or scoped for this trial?** Without it no capability reaches `VERIFIED`, and assignment on verified capabilities is body § 8 / I.4. | (a) lift · (b) **scope it to the four capabilities this trial exercises** · (c) leave it, and run the trial explicitly as a **capability rehearsal that claims no actorhood** | **(b) or (c).** Note that (c) is not a workaround: a full-text read producing a receipt, a work manifest with verbatim locators, worktree confinement and Auto Mode active **are the L2 smoke evidence**. The trial and the smoke test are the same act. | under (c) the trial runs and produces no governed Scientist artifact |
| **D-5** | **Are the Scientist `ACTOR_ID`s resolved?** Currently `UNRESOLVED` **by governed decision** — a governed decision is undone by a governed decision. | (a) resolve now · (b) leave unresolved and run under (D-4c) | (b) for this trial — a single-reader rehearsal needs no persistent Scientist identity | the trial runs under (D-4c); a *governed* reading does not |
| **D-6** 🔴 | **Does the control arm run?** | (a) **yes** · (b) no | **(a)** — it is the only route to D-EFF, and D-EFF is the dimension the mandate asked about that the repository cannot otherwise answer | under (b), D-EFF is reported `NOT MEASURED`, with § 2.1's reason quoted |
| **D-7** | **Is a blind R4-shaped pre-review of *this design* commissioned before Φ1?** | (a) yes, bound by this file's blob · (b) no | **(a)**, if it costs less than one reading session. R-5's record: a blind reviewer found eight defects two informed reviewers had passed over twice | the trial can start without it |
| **D-8** | **Is the review floor `R1` or `R2`?** C.1: `R1` for an ordinary L2 inference, **`R2` for a therapeutic-actionable inference**. C1q is druggable and anti-C1q antibodies are in human trials. | (a) **`R2`**, decided now · (b) decide when the claims exist | **(a)** — derogation is permitted only upward, so choosing `R2` in advance costs nothing and removes a mid-run judgement | Φ8 runs at whichever floor is set |
| **D-9** 🔴 | **Does `TRIAL-001` end at the COMMIT CANDIDATE, or at `BATCH_COMMIT`?** Only the second changes the four canonical current files — the thing LEGEND exists to do. | (a) stop at the candidate · (b) **proceed to `BATCH_COMMIT` if LINT is green and the review closed** | **(b)**, gated. A trial that stops at the candidate proves the coordination loop; only (b) proves the scientific loop. See T-5 on the gate field | Φ10 produces the candidate either way |

---

## 9 · Next steps, in order

| # | Step | Owner | Blocked by |
|---|---|---|---|
| 1 | Decide **D-1** (paper) and **D-2** (acquisition) | operator | — |
| 2 | Decide **D-3** (convention), **D-4** (L2 hold), **D-6** (control arm) | operator | — |
| 3 | *(optional, recommended)* commission the blind pre-review of this design, **bound by this file's blob id** | operator | D-7 |
| 4 | Acquire the full text; record the receipt; verify the digest | Plan / any session with acquisition capability | D-1, D-2 |
| 5 | Author `TRIAL-001/surface_spec.json` — **the real preparation cost**; the population block is paper-specific and has a documented defect history (F-5) | Plan | step 4 |
| 6 | Φ0 pre-flight **re-derived at the moment**, never read from § 3.1 | any session | steps 1–5 |
| 7 | Φ1 → Φ11 as § 5.2 | as assigned | Φ0 clean |
| 8 | Register the trial's own findings; **do not fix the framework mid-run** | the trial | — |

**A note on this record's own preservation.** It is untracked as written, as its predecessor
`FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md` still is. Under § S.6.1 a `WORK_COMMIT` of an
author's own named paths on its own branch is that author's own authority, and § S.2.4's measured
hazard is that one `git clean` from any co-occupant destroys every untracked artifact at once.
**Committing both records on this branch is available and is not performed here** — it was not
asked for.

---

## 10 · Findings registered, not corrected

Per the mandate: gaps found during trial design are recorded as findings. **None is repaired here.**

| # | Finding | Evidence | Disposition owner |
|---|---|---|---|
| **T-1** | 🔴 **The prepared benchmark paper is not new evidence.** PMID 42397075 carries `complete_fulltext_read`, a receipt, a schema-2 manifest and a dossier. The mandate's candidate case and the laboratory's prepared instrument are **mutually exclusive**, and nothing recorded that before today. | § 3.2 | operator (D-1) |
| **T-2** | **OPCON-v1 exists on 1 ref of 48** (`plan-orchsurf-r4-transcription` @ `e4aa80c`), `status: DRAFTED`, `binding: NO`. A convention that is the working system of a trial, and that is absent from the branch anyone would check out, is a routing hazard. *Positive control 18/48, negative 0/48.* | ref sweep | Plan / operator (D-3) |
| **T-3** | 🟡 **OPCON-v1 § B.7 M-h reads *"artifacts carrying `session_ref:` — 0"*. Measured at `30cb4f3` and at `main` over 581 tracked paths: **1** — `governance/design_records/materialization_log.md`, twice, carrying a raw session UUID rather than the `name [ref]` form § S.3.4 declares.** *Controls: `^status:` 30, `^zzq_control:` 0.* The conclusion M-h draws survives; **the count does not**, and the difference is the form, not the ref. | `git grep -l -E "^session_ref:"` | the convention's author (correction travels to the source — S.5.6) |
| **T-4** | 🔴 **Mirror's stated primary analysis surface does not exist.** Annex G.3 makes the consolidated event ledger Mirror's object; `ledger/events/` and `ledger/consolidated/` are on **0 refs**. Φ9's input must be scoped to frozen artifacts and receipts **by declaration** — which this design does, and which is a decision rather than an oversight. | prior sweep, consistent with `ledger/` contents here | Plan / operator |
| **T-5** | 🔴 **No one can currently emit a conforming `MIRROR_REVIEW`.** `annex_d_commit_batch.md` line 38 fixes the vocabulary `n/a \| PASS \| FAIL + REVIEW_ID`. Measured at `30cb4f3`: **8 of 8** `CAND-*` manifests carry the field, **0 conform** — observed values `PASS_WITH_NOTES`, `PENDING` ×2, `ACCEPT`, `REQUEST CHANGES` ×2, `REQUIRED · NOT PERFORMED · NOT ASSUMED`; two use the column-aligned form. **Two of these are scheduling states, not review outcomes.** This gates the trial's own candidate (F-9). *Scope stated: 8 is the count of `CAND-` paths at this HEAD across the whole tree, not on other refs; OPCON-v1 records 9 at its own scope, and the difference is scope, not disagreement.* | `git ls-tree` then measured; positive control fires on the annex, negative control 0 | Plan (P-8 in the convention's register) |
| **T-6** | **A role seat moved twice with no instrument reporting either move.** `mirror` tip: `1892071` → `da52ee5` (2026-08-22) → **`2767333`** (measured 2026-08-23T18:19Z). Not wrong; **unreported**, and a pre-flight that reads a predecessor's table instead of re-deriving would have been wrong on this row for the third consecutive day. | `git worktree list` | Plan |
| **T-7** | **No baseline exists for "efficiency vs a traditional workflow."** Measured over **297 tracked files** under `disease-models/wwox/` + `framework/eval/`: records carrying a measured reading **duration** — **1**, and it is `analysis/scripts/md_helix_screen.py`, a molecular-dynamics script whose "duration" is a simulation length, **not a reading**. *Positive control `receipt` 160 of 297; negative control 0.* Separately, `traditional workflow \| unstructured read \| control arm \| baseline read` fires on 5 files across the whole tree — **all five in the biological sense**, experimental control arms inside the papers being read. **The dimension is answerable only by running the control arm; asserting it is not available.** | the two sweeps above, with their controls | operator (D-6) |

---

## 11 · What this record does not do

- It does **not** start the trial, acquire a paper, build a surface, or author a `surface_spec`.
- It does **not** dispatch, register, activate, assign, or contact any actor. **No session was
  messaged and no subagent was spawned in producing it** — see the note below.
- It does **not** create a Task Contract, a candidate, a `DEC`, an approval, or a ledger event.
- It does **not** lift the C-9 hold, verify a capability, acquire a lease, or resolve an `ACTOR_ID`.
- It does **not** adopt, amend, activate or reinterpret OPCON-v1, and it implements none of its
  proposals P-1…P-8.
- It does **not** modify `governance/`, `roles/`, `framework/`, `ledger/`, `runtime/` or any of the
  four scientific current files, and it advances neither `main` nor any other branch.
- It does **not** resolve T-1…T-7, or any observation carried by its predecessors.
- It does **not** claim actorhood for its author. A session cannot resolve its own actorhood, and
  *"none"* is the correct answer here.

### 11.1 · On consulting Mirror and Plan — the decision, and its reason

The mandate left this to the Orchestrator's judgement. **Nine live peer sessions were enumerated**
(`mirror-87 [103de0]`, `mirror-75 [f3044e]`, `mirror-1b [a85964]`, `mirror-42 [6cb8b5]`,
`evidence-index-58 [432290]`, `evidence-index-61 [765ff9]`, `evidence-index-86 [7483d0]`,
`lettore-c-1e [ac92c7]`, `legend-public-af [ceddab]`), so consultation was available. **It was not
performed**, for three measured reasons:

1. **This session holds no authority to declare in a dispatch.** § S.5.1 requires a dispatch to
   name its authority basis. Measured: 0 ACTIVE leases, `ACTOR_ID` not established. There is
   nothing to declare beyond a relayed mandate, and a session cannot resolve its own actorhood
   (S.1.2).
2. **There was no blob to review.** § B.4 H-1b: *a review declares the blob it reviewed*. Findings
   produced against a design still being written are findings against a moving object.
3. **The consultation is better spent later, and is scheduled rather than skipped** — § 8 D-7
   commissions exactly the Mirror pre-review the mandate contemplated, bound by **this file's blob
   id**, and § 5.2 Φ9 allocates Mirror's R4. Plan's feasibility-and-load judgement is § 9 step 5,
   where the surface spec is authored and its cost is real rather than estimated.

**Both are therefore owed and named, not omitted.** Neither produces an authorization; both
produce findings.

### 11.2 · Constraint compliance

| Constraint (mandate) | Result |
|---|---|
| no modification to `main` without HUMAN APPROVAL | ✅ `main` untouched; nothing committed; one new untracked file on a non-`main` branch |
| existing PROPOSALs remain PROPOSALs | ✅ P-1…P-8 and `PROPOSAL-C9` cited, none implemented |
| no new rules added to the convention | ✅ every rule cited is quoted from an existing normative or convention file; gaps are § 10 findings |
| real state verified, nothing inherited | ✅ § 3.1, § 3.2, § 3.3 and § 10 re-derived at `30cb4f3` today; § 12 carries the commands. **Two inherited figures were re-measured and both came back different — `session_ref` 0 → 1 (T-3, a real difference) and `CAND` manifests 9 → 8 (T-5, a scope difference) — and one sweep of this record failed its own positive control and was re-run (F-7).** |
| the trial validates LEGEND in the real world, and does not become framework construction | ✅ § 3.5 declares the write allowlist before the run; F-1 makes the drift detectable; the deliverable is a scientific result plus a dimension-by-dimension outcome |

---

## 12 · Verification trail — commands, and the instants they were run

All at `legend-operating-convention-v1` @ `30cb4f3fd700e2aaf6b608e363438f883ddc3760`,
2026-08-23T18:13Z–18:22Z. **Every figure in this record is reproducible from this list.**

```bash
# identity, divergence, working tree
git rev-parse HEAD && git rev-parse --abbrev-ref HEAD && git rev-parse main
git log --oneline main..HEAD | wc -l          # 3      git log --oneline HEAD..main | wc -l   # 0
git status --porcelain

# system state and gates
grep -n "current_state" framework/state/state_manifest_current.md      # line 141: READY
python3 framework/scripts/legend_lint.py .                             # VERDICT: PASS
python3 framework/scripts/lease_state.py                               # ACTIVE by derivation: 0

# authority and registration
git show orchestrator:runtime/agent_card_registry.md                   # 3 of 6; a/b NOT_REGISTERED
grep -c "UNVERIFIED" roles/scientist.md                                # 6
sed -n '1,25p' governance/candidates/PROPOSAL-C9-STATE-MODEL.md        # ACCEPTED; L2 suspended
sed -n '1,25p' governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md

# the prepared packet: 7 of 7 present and digest-matching, via SOURCE_FILES[].surface_path
python3 -c "import json,hashlib,os;m=json.load(open('framework/eval/benchmarks/BENCH-AB-001/benchmark_manifest.json'));\
[print(('OK ' if os.path.exists(e['surface_path']) and hashlib.sha256(open(e['surface_path'],'rb').read()).hexdigest()==e['sha256'] else 'BAD'),e['surface_path']) for e in m['SOURCE_FILES']]"
python3 framework/scripts/benchmark_input_surface.py population \
        --spec framework/eval/benchmarks/BENCH-AB-001/surface_spec.json --source-root .
#   run twice → identical sha256 b41c7b9f432e48c7 ; 65 units / 109 panels

# the prior reading of that paper  (T-1)
grep -n "42397075" disease-models/wwox/registries/reading_state.md     # line 117: complete_fulltext_read

# the ref population  (T-2) — NOTE the shell: `for r in $refs` does NOT split in zsh
git for-each-ref --format='%(refname)' refs/heads refs/remotes | wc -l              # 48
while IFS= read -r r; do git cat-file -e "${r}:<path>" 2>/dev/null && echo "$r"; done \
  < <(git for-each-ref --format='%(refname)' refs/heads refs/remotes)
#   legend_operating_convention_v1.md → 1 ; control controlled_benchmark_ab.md → 18 ; nonsense → 0

# session_ref adoption  (T-3)
git ls-tree -r --name-only HEAD | wc -l                                # 581 tracked paths
git grep -l -E "^session_ref:" HEAD                                    # 1 (materialization_log.md)
git grep -l -E "^status:" HEAD | wc -l                                 # 30  (positive control)
git grep -l -E "^zzq_control:" HEAD | wc -l                            # 0   (negative control)

# the gate field  (T-5)
git ls-tree -r --name-only HEAD | grep "CAND-"                         # 8, all in governance/candidates/
grep -n "MIRROR_REVIEW" governance/annex_d_commit_batch.md             # line 38: n/a | PASS | FAIL

# the trial input  (§ 3.3)
grep -c "^## FT-" disease-models/wwox/research/full_text_queue_current.md   # 72
#   NEVER_ANALYZED measured into that denominator over 8 analysis surfaces → 4 entries

# seats  (T-6)
git worktree list                                                      # 25 total, 11 non-scratch
```

> **Every value above is a photograph, and it decays.** A later reader who gets a different number
> should re-run the command beside it and check the **class** first (§ 6.1 rule 3): a
> population-derived figure that moved may mean only that a branch was opened, while an
> object-derived one that moved means the repository did.
