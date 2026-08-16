---
artifact: LEGEND governance — annex register
governance_version: 3.1.1
status: REGISTER — complete as a register; the annexes themselves are NOT materialized
normative: no (this file records requirements and status; the annexes, once materialized, are normative)
maintained_by: plan
created_on: 2026-08-16
---

# ANNEX REGISTER — Governance v3.1.1

The v3.1.1 body is a two-level structure: **CORPO** (materialized as
[`GOVERNANCE_v3.1.1.md`](GOVERNANCE_v3.1.1.md)) **+ ANNESSI CANONICI A–J**, which Plan MUST
materialize as separate files. The body transmitted to Plan referred to the annexes as
*"(allegato)"*; **the annex text was not transmitted with it.**

**None of the ten annexes exists yet.** This register is not a substitute for them and must
never be read as one. It records, for each annex: what the body binds it to contain, which body
sections depend on it, who is entitled to author it, and what is blocked while it is missing.

Per the LEGEND file protocol (`CLAUDE.md` → *File protocol*), stub or placeholder annex files
are invalid output. No empty `ANNEX_A.md` … `ANNEX_J.md` have therefore been created: an absent
file is an honest absence, a stub is a lie that passes a directory listing.

## Authorship classes

| Class | Meaning |
|---|---|
| `OPERATOR_SOURCED` | The body presents the annex as already drafted and attached. Plan materializes the supplied text; it does not compose the content. |
| `PLAN_DEFINED` | The body explicitly delegates the design to Plan. Plan composes it, and it goes through Mirror hostile review like everything else. |
| `MIXED` | Structure supplied, one or more parameters delegated to Plan. |

## Register

| Annex | Subject | Bound by | Must contain (per the body) | Authorship | Status |
|---|---|---|---|---|---|
| **A** | TASK CONTRACT | §22, §4, §9.3, §36.2, §36.3 | Full contract schema: Task ID, directive version, generation, owner, priority, objective, scope, acceptance criteria, dependencies, review floor, **A.1 INTERACTION_MODE** (`QUESTIONS_ALLOWED` / `AUTONOMOUS_COMPLETE`, E6), **A.3 TASK_CLAIM** with G/F/D/R, **RETRY_POLICY** (E7), deliverable with durable-milestone plan (E2), current state + TASK_ACK, **A.6 checkpoint schema + fingerprint composition** (E1) | MIXED — schema `OPERATOR_SOURCED`; A.6 fingerprint composition explicitly `PLAN_DEFINED` (§6, §30) | ABSENT |
| **B** | COMMUNICATION | §20.2, §20.4, §21 | Message types; envelope `MESSAGE_ID, TASK_ID, ACTOR_ID, FROM, TO, TYPE, STATE_CHANGE?, DURABLE_POINTER`; ACK obligation and timeout→resend→BLOCKER; HEARTBEAT feeding the DOWN timeout; broadcast receipts; **B.5 nominal map to A2A states** (E5); normative routing table | OPERATOR_SOURCED | ABSENT |
| **C** | PEER REVIEW FORMAT | §25 | Single review format: mandatory STEELMAN, VERDICT `CONFIRMED / WEAKENED / REFINED (+formulation) / REFUTED`, REVIEWER_CONFIDENCE, RESIDUAL_UNCERTAINTY, EVIDENCE_NEEDED, WHAT_WOULD_CHANGE_MY_MIND, mandatory AUTHOR_RESPONSE | OPERATOR_SOURCED | ABSENT |
| **D** | INTEGRATION_CANDIDATE MANIFEST | §11, §12 GATE 2/5 | Manifest schema carrying, at minimum, LINT PASS + publication gate PASS/0 in the same window, CANDIDATE_CONTENT_HASH and BASE_HEAD | OPERATOR_SOURCED | ABSENT |
| **E** | LEARNING LIFECYCLE | §17 | States `OBSERVED → LOCAL → PROVISIONAL → VALIDATING → PROMOTED / REJECTED / SUPERSEDED / EXPIRED`; confirmation classes; ≥2 threshold or 1 + Mirror validation; mandatory PROVISIONAL expiry with `PROMOTE / REJECT / EXTEND_WITH_REASON`; change isolation only in VALIDATING | OPERATOR_SOURCED | ABSENT |
| **F** | ORCHESTRATOR_CHALLENGE | §9.2 | Structured challenge object and mandatory adjudication `ACCEPT / MODIFY / OVERRIDE_WITH_RATIONALE / ESCALATE`, recorded | OPERATOR_SOURCED | ABSENT |
| **G** | MIRROR PERIMETER + AUTONOMY LEDGER | §3, §29.1, §29.3 | **G.1** `MIRROR_REQUIRED / MIRROR_SAMPLED / NO_MIRROR` perimeter; AUTONOMY LEDGER schema — HUMAN_REQUIRED PREVENTABLE vs UNAVOIDABLE, blocked hours, false escalations, exclusion of voluntary supervision | OPERATOR_SOURCED | ABSENT |
| **H** | AUTHORITY MATRIX | §7, §35.2 | The normative authority matrix, to be replicated into each worktree's CLAUDE.md | OPERATOR_SOURCED | ABSENT |
| **I** | BOOTSTRAP, LEASE, DEPLOYMENT PROFILE | §0.2, §0.4, §8, §9.4, §38, §47 step 9 | Bootstrap protocol detail; ORCHESTRATOR_LEASE (acquisition, ACTIVE singleton, governed reacquisition); DEPLOYMENT_PROFILE with the concrete `<REPO_ROOT>`; **I.4 registry = LEGEND AGENT CARD** with declared vs L2-verified capabilities | OPERATOR_SOURCED | ABSENT |
| **J** | SYSTEM OBJECTS | §12 GATE 3, §4, §29.3, §36.6, and the GUARANTEE rule | **J.0** consolidated, normative synthesis of the guarantees NOT possessed (E10); **J.1** consolidated EVENT LEDGER, Mirror's primary analysis surface; **J.2** actor state machine (ACTIVE / DOWN / PARKED / …); **J.3** HUMAN_APPROVAL_QUEUE durable object; **J.4** COST_POLICY with `DEFAULT_EXTERNAL_SPEND = 0` | MIXED — J.1 ledger design explicitly `PLAN_DEFINED` (§49.P: *"design del ledger scelto da Plan, con G/F/D/R"*); the rest OPERATOR_SOURCED | ABSENT |

## What the absence blocks

Downstream artifacts Plan owns cannot be composed without the annexes they depend on, and
composing them from the body alone would mean inventing normative content:

| Blocked artifact | Blocked by |
|---|---|
| `/BOOTSTRAP.md` | Annex I (bootstrap protocol, lease, deployment profile) |
| `/roles/*.md` | Annex H (authority matrix), Annex A (contract schema), Annex B (routing) |
| `APPLICABLE_GOVERNANCE_FINGERPRINT` composition | Annex A.6 + the role contracts that supply `ROLE_CONTRACT_HASH` |
| Runtime / authority inventory, Agent Card | Annex I.4 (card schema), §43 columns |
| `LEARNING_INDEX` + role-specific `ACTIVE_LESSONS` with budget | Annex E (lifecycle), §19 (budget, Plan-defined) |
| EVENT LEDGER structure + consolidated view | Annex J.1 — Plan-designed, but J.0's G/F/D/R declaration frames it |
| CLAUDE.md router update (§0.3, §35.1, §35.2) | Annex H, Annex I |
| First INTEGRATION_CANDIDATE | Annex D (manifest schema) |

## Ledger append-only constraint (recorded here so it is not lost)

Independently of Annex J.1's final design, the EVENT LEDGER obeys a constraint given directly
to Plan: **a source event already written is never modified.** The closing event points back to
the opening one via `CLOSES_EVENT_ID`, and `closed_by` may exist **only in a derived view**.
This is carried forward into whatever ledger design Plan proposes.
