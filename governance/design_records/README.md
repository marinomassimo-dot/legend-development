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
| **Prior-art matrix** — the mechanisms considered from Paperclip, Microsoft Agent Framework, Google ADK 2.0, A2A, OpenHands, Pydantic AI, Letta, each registered as `EXTERNAL_PRIOR_ART_CONSIDERED` and never as a dependency, with the explicit non-adoptions (external heartbeat / wake-sleep runtimes, durable server-backed runtimes — rejected as opposed to the visible-actors requirement, §34) | document *"LEGEND v3.1 prior art review"* | **MISSING — not transmitted to Plan** |
| **DEFER register** — what the targeted hostile prior-art review deliberately deferred rather than adopted | same document | **MISSING — not transmitted to Plan** |
| **Amendment record E1–E10** — the ten amendments and the operator's three corrections on E1, E2 and E8 | same document | **MISSING — not transmitted to Plan**; the body marks their *effects* inline with `[v3.1.1]` but does not carry the review that produced them |

## Why these cannot be reconstructed

The body records the *outcome* of the prior-art review, not the review. A prior-art matrix is a
record of judgements actually made about specific external systems, and a DEFER register is a
record of options actually declined and why. Both are testimony about a deliberation Plan did
not witness. Composing them from the body would produce a plausible document describing a
review that never happened in that form — provenance fabricated to fill a provenance slot,
which is the precise failure this directory exists to prevent.

They are therefore recorded as a tracked debt, not silently omitted, and not approximated.

## Present contents

- [`materialization_log.md`](materialization_log.md) — what Plan materialized, from what source,
  what it refused to compose, and the session learning.
