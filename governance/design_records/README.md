---
artifact: LEGEND governance — design records
governance_version: 3.1.1
normative: NO — architectural provenance only
binding_on_actors: none
maintained_by: plan
created_on: 2026-08-16
---

# design_records/ — architectural provenance, not runtime law

Governance v3.1.1 requires Plan to archive here the material that explains **why the governance
is shaped the way it is**, and states its status without ambiguity:

> *"sono provenance architetturale, NON normativa runtime: non vincolano gli attori, spiegano
> perché la governance è fatta così."*

Nothing in this directory binds an actor. An actor that finds a rule here and not in
[`../GOVERNANCE_v3.1.1.md`](../GOVERNANCE_v3.1.1.md) or in a canonical annex is looking at
history, not at law. That distinction is the entire purpose of keeping these records in a
separate directory rather than folding them into the body.

## Required contents

| Record | Source | Status |
|---|---|---|
| **Prior-art matrix** — 17 primitives compared against Paperclip, Microsoft Agent Framework, Google ADK 2.0, A2A, OpenHands, Agno, Pydantic AI and Letta, each registered as `EXTERNAL_PRIOR_ART_CONSIDERED` and never as a dependency, with the explicit non-adoptions (external heartbeat / wake-sleep runtimes, durable server-backed runtimes, wholesale A2A transport) | *"LEGEND GOVERNANCE v3.1 — TARGETED HOSTILE PRIOR-ART REVIEW"* | **ARCHIVED** → [`prior_art_review_v3.1.md`](prior_art_review_v3.1.md) |
| **DEFER register** — five deferred items, each with its reopening trigger | same document | **ARCHIVED** — Parte 4 |
| **Amendment record E1–E10** — the ten amendments, plus the operator's three corrections on E1, E2 and E8 | same document | **ARCHIVED** — Parte 3, with the three corrections recorded as a proposed-vs-ratified divergence table rather than retconned |
| **Source verification status** — which external systems were verified primarily and which were not | same document | **ARCHIVED** — Agno marked ⚠ as the document itself marks it |

## What the archive is

`prior_art_review_v3.1.md` is a **byte-faithful copy** of the source file
`LEGEND_v3.1_prior_art_review_matrice (1).md`, taken from the filesystem, not from the chat:

```
SHA-256 (source, measured before copy)   2563f82e82d661f98ff5eb2b029a8568b519d0ac3ae91e4fd76ba21704d6988e
SHA-256 (archived, measured after copy)  2563f82e82d661f98ff5eb2b029a8568b519d0ac3ae91e4fd76ba21704d6988e
BYTE_IDENTITY                            PASS
```

**It carries no added header.** Classification metadata — `DESIGN RECORD — NON NORMATIVO`, the
fact that it binds no actor, and the divergences between what it proposed and what v3.1.1
ratified — lives here and in the materialization log, outside the historical bytes. A design
record annotated inside its own body is no longer the document that was written.

Provenance is testimony about a deliberation Plan did not witness, so none of it was
reconstructed while it was missing. It was requested three times and recorded as `MISSING` three
times (MAT-001, MAT-005, MAT-008) rather than approximated.

### The transcription that preceded it, and why it was wrong

Revision 3 archived a transcription taken from the chat rendering, which had mojibaked the
encoding. It was honestly labelled as a reconstruction and shipped with a published glyph map —
and it was still wrong in **49 of 151 lines**. The author writes `✔`; the map guessed `✅`. The
author writes `⚠` alone; the transcription added the words *VERIFIED* and *UNVERIFIED* that
appear nowhere in the source.

That is the evidence for `gold_is_in_the_details.md` § 5d's first clause rather than its second:
**re-derive the surface**. Declaring a reconstruction does not make it faithful; it only makes
the infidelity visible to whoever reads the declaration, which is not the same protection.
MAT-010 records it.

### What v3.1.1 ratified differently from what this document proposed

Recorded here rather than inside the historical bytes:

| Proposed | Ratified in v3.1.1 |
|---|---|
| E1 binds the checkpoint to `GOVERNANCE_VERSION` | binds it to `APPLICABLE_GOVERNANCE_FINGERPRINT`; the global version is audit only |
| E2 corollary: *ogni operazione mutante è un confine di transazione* | the idempotence boundary is the **significant durable milestone** |
| E8: `closed_by: EVENT_ID` on the opening event | the opening event is never mutated; the **closing** event carries `CLOSES_EVENT_ID`, and `closed_by` may exist only in a derived view |

These are the operator's three corrections. Where the two differ, the FROZEN body and annexes
A–J prevail exclusively.


## The Scientist-development ledger — `sviluppo_lettori.md`

**Archived 2026-09-11**, on the operator's instruction, as the second design record in this
directory. Same classification as the first: **non-normative, binding on no actor.** An actor
that finds a rule here and not in the FROZEN body, an annex, `LEGEND_CORE.md` or
`scientist_standing_brief.md` is reading a hypothesis, not law.

```
SHA-256 (source, measured before copy)   14d0b82bbf4f879eff847e4b4c2a92aa969b57159f14f2fa915dfd7741751410
SHA-256 (archived, measured after copy)  14d0b82bbf4f879eff847e4b4c2a92aa969b57159f14f2fa915dfd7741751410
BYTE_IDENTITY                            PASS
bytes / lines                            282,297 / 10,612
```

**It carries no added header**, for the reason stated above: a design record annotated inside its
own body is no longer the document that was written. The file's name is the one the document gives
itself in its first line; the working copy carried the last-reviewed repository in its filename
(`…_TOOLUNIVERSE`), and that suffix is deliberately not archived — the ledger is cumulative and its
name must not move with every review.

### What it is

A cumulative ledger of **eighteen Tier-1 repository reviews** — Robin, AutoScientists, DisMech,
Gemma Curation Agents, CORAL, Paperclip, ATHENA, ARIS, Medea, ARA, Scholar Loop, ResearchOS,
llm4xray, AI-Scientist-v2, OpenScientist, BioDSA/DeepEvidence, Autoresearch, ToolUniverse — each
mined for what it says about how LEGEND's **Scientists** should read, extract, verify and remember.
Per review: new patterns, patterns strengthened, patterns weakened, new specialist roles, new
deterministic-software candidates, scaling / review / provenance / context implications, changes to
the provisional design, and new unresolved questions. Every claim carries a state from its own
vocabulary — `EMERGING`, `STRONGER`, `WEAKER`, `UNRESOLVED`, `BENCHMARK`, `REJECT`,
`ADOPT CANDIDATE` — and a cumulative pattern ledger is re-tabled after each review without deleting
the previous state.

**It is not a plan and it is not a decision.** Its own § 18 fixes the update protocol and its own
closing sections repeat that final adoption stays *"surgical: maximum gain, minimum harness"*.

### Why it is worth a Harness Engineer's time

It is the clearest existing statement of the boundary this repository keeps rediscovering the hard
way: **what must be deterministic software and what must stay scientific judgment.** Several of its
strongest convergences name defects LEGEND has already paid for — corpus completeness that no
reviewed repository solves, `citation exists ≠ citation supports`, `runtime success ≠ scientific
completeness`, validator failure that must never become approval, retrieval failure that must never
become negative evidence, and the rule that a producer may not self-certify its own result. Others
are proposals LEGEND has not tested: a fungible `ScientistPool(N)` with atomic paper claiming, a
capability plane with progressive disclosure, breadth/depth as task modes, fail-closed
`INCONCLUSIVE`, and a reviewer that may downgrade but never upgrade on the same evidence.

Read it beside — never instead of — the measured record of how the Scientists actually performed:
[`../../disease-models/wwox/analysis/orchestration_reviews/2026-09-09_actor_retrospective.md`](../../disease-models/wwox/analysis/orchestration_reviews/2026-09-09_actor_retrospective.md)
and
[`../../disease-models/wwox/analysis/orchestration_reviews/2026-09-11_scientist_due_diligence_as_is.md`](../../disease-models/wwox/analysis/orchestration_reviews/2026-09-11_scientist_due_diligence_as_is.md).
Where a pattern here and a measurement there disagree, the measurement is the evidence and the
pattern is the hypothesis.

### How to extend it

Append, never overwrite: the document's § 18 gives the per-review template and the state
vocabulary, and requires a contradicted conclusion to be recorded as
`Previous state / New evidence / Updated state / Reason` rather than silently replaced. A future
review lands as a new section plus a re-tabled cumulative ledger, in this same file, keeping the
byte-faithful history of what was already concluded.

## Present contents

- [`prior_art_review_v3.1.md`](prior_art_review_v3.1.md) — the archived design record.
- [`materialization_log.md`](materialization_log.md) — append-only: what Plan materialized, from
  what source, what it refused to compose, and the session learning of each step.
- [`claude_md_migration_map.md`](claude_md_migration_map.md) — the rule-by-rule evidence that the
  root `CLAUDE.md` became a router without losing law.
- [`sviluppo_lettori.md`](sviluppo_lettori.md) — the cumulative Scientist-development ledger:
  eighteen Tier-1 repository reviews, their pattern states and the open questions they leave.
