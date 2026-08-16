---
artifact: LEGEND governance — annex register
governance_version: 3.1.1
status: COMPLETE — all ten annexes received and materialized
normative: no (this file is a register; the annexes it lists are the normative artifacts)
maintained_by: plan
created_on: 2026-08-16
last_updated: 2026-08-16 (MAT-002)
---

# ANNEX REGISTER — Governance v3.1.1

Governance v3.1.1 is a two-level structure: **CORPO** ([`GOVERNANCE_v3.1.1.md`](GOVERNANCE_v3.1.1.md))
**+ ANNESSI CANONICI A–J**, each materialized as a separate file. All ten were transmitted on
2026-08-16 and are materialized verbatim.

## Transmitted preamble (verbatim)

> Materializzati da Plan come file separati (es. `governance/annex_a_task_contract.md`). Le parti
> **[MAJOR]** richiedono il gate 3 completo. Campi minimi: estendibili, mai rimovibili. Modifiche
> rispetto alla v3.1 marcate **[v3.1.1]**.
>
> Regola trasversale: ogni meccanismo di coordinamento dichiara
> `GUARANTEE_PROVIDED / FAILURE_MODE_STILL_POSSIBLE / DETECTION / RECOVERY`. Sintesi consolidata:
> **Annex J.0**.
>
> Provenance: la prior-art matrix e il registro DEFER vivono in `design_records/` — spiegano il
> perché, non vincolano il runtime.

## The ten annexes

Hashes are a snapshot taken at MAT-002. They are recorded for audit; the authoritative value for
any fingerprint is the one computed at use time by the composition function
([`plan_defined_parameters.md`](plan_defined_parameters.md) § P2), never a number copied from
this table.

| Annex | File | Subject | SHA-256 (MAT-002) |
|---|---|---|---|
| **A** | [`annex_a_task_contract.md`](annex_a_task_contract.md) | Task contract, claim, generation, checkpoint, idempotent resume | `372d493b…50159` |
| **B** | [`annex_b_message_protocol.md`](annex_b_message_protocol.md) | Envelope, message types, ACK/heartbeat reliability, A2A name map | `f148b4e6…f0fb3` |
| **C** | [`annex_c_review_protocol.md`](annex_c_review_protocol.md) | Review ladder with floors, single review format, discipline | `a3fd5587…4a5b` |
| **D** | [`annex_d_commit_batch.md`](annex_d_commit_batch.md) | Three commit types, candidate manifest, GATE 0, batch transaction | `02febe99…83159` |
| **E** | [`annex_e_learning_lifecycle.md`](annex_e_learning_lifecycle.md) | Learning state machine, LEARNING_INDEX, provisional practice, compression budgets | `db2294ab…4be35` |
| **F** | [`annex_f_challenge_dissent.md`](annex_f_challenge_dissent.md) | Challenge severity, adjudication, lifecycle, DIAGNOSE before non-compliance | `23ee2c6e…f807` |
| **G** | [`annex_g_mirror.md`](annex_g_mirror.md) | Mirror perimeter, self-upgrade constraint, autonomy ledger and review yield | `80e37d38…f9954` |
| **H** | [`annex_h_authority_matrix.md`](annex_h_authority_matrix.md) | Authority matrix **[MAJOR]**, governance version and fingerprint roles | `e6182d55…76acd` |
| **I** | [`annex_i_bootstrap_deployment.md`](annex_i_bootstrap_deployment.md) | Bootstrap protocol, orchestrator lease, Agent Card, deployment profile | `a1e9e7fa…b937ef` |
| **J** | [`annex_j_runtime_control_plane.md`](annex_j_runtime_control_plane.md) | Guarantees not possessed, event ledger, state machines, approval queue, cost policy | `20e84e15…c2414` |

Plus [`plan_defined_parameters.md`](plan_defined_parameters.md) — the seven values the annexes
delegate to Plan by name, collected in one artifact so the fingerprint has one thing to hash
rather than seven scattered footnotes. `9860ac7a…0361e1`.

## What the annexes delegated to Plan, and where it now lives

| Delegating clause | Value | Status |
|---|---|---|
| A.1 — `RETRY_POLICY.on_exhaust` default | `PARK` | P1 |
| A.6 / H.1 — fingerprint composition | per-role pertinence sets + composition function, version 1 | P2 — executable: `governance/scripts/governance_fingerprint.py`, which parses § P2.2 rather than copying it |
| B.3 — ACK timeout | 30 minutes, PROVISIONAL with expiry | P3 |
| B.3 — HEARTBEAT cadence | 30 minutes, DOWN after 3 missed, PROVISIONAL | P4 |
| D.2 — `CANDIDATE_CONTENT_HASH` | SHA-256 over versioned prefix + tree oid + BASE_HEAD | P5 |
| E.5 — role subset budgets | 25 lessons or 4 000 words, PROVISIONAL | P6 |
| J.1 — event ledger one-writer design | option (a), per-actor JSONL consolidated by Plan | P7 — **design chosen; writer and validator not yet built** |
| G.3 — `MIRROR_RETROSPECTIVE ogni N batch` | — | **UNASSIGNED** by the annexes; left UNRESOLVED, not filled in by Plan |

## Downstream artifacts — now unblocked, still to build

| Artifact | Unblocked by | Status |
|---|---|---|
| `/roles/*.md` role contracts | H, A, B | pending |
| `/BOOTSTRAP.md` | I.1, I.2 | pending |
| `/deployment/deployment_profile.md` | I.5 | pending |
| Runtime inventory / Agent Card registry | I.4, body §43 | pending |
| `LEARNING_INDEX` | E.2 | pending |
| `ACTIVE_LESSONS` role subsets | E.5 + P6 | pending |
| Event ledger structure + consolidated view | J.1 + P7 | pending |
| Fingerprint composition script | A.6 + P2.4 | pending |
| Root `CLAUDE.md` router rewrite (bootstrap step 8) | H, I | **held** — see contradiction 1 in `design_records/materialization_log.md`; the current root CLAUDE.md is the load-bearing scientific core, and replacing it with a router is a lossy edit until that content has a durable home |
| First `INTEGRATION_CANDIDATE` | D.2 + P5 | pending; requires the branch to be brought up to `main` first (GATE 0 binds BASE_HEAD) |

## Still missing — design records

The prior-art matrix and the DEFER register (document *"LEGEND v3.1 prior art review"*) have not
been transmitted. They are provenance, not runtime law, so nothing is blocked on them, but
`design_records/` stays incomplete until they arrive. See
[`design_records/README.md`](design_records/README.md).
