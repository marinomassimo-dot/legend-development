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
| **Source verification status** — which external systems were verified primarily and which were not | same document | **ARCHIVED** — Agno preserved as ⚠ **UNVERIFIED**, as the document itself classified it |

## What the archive is, and what it is not

Provenance is testimony about a deliberation Plan did not witness, so none of it was
reconstructed while it was missing. It was requested three times and recorded as `MISSING` three
times (MAT-001, MAT-005, MAT-008) rather than approximated; it arrived on the third and is
archived unmodified in substance.

One caveat travels with it. The document reached Plan through a channel that had already
corrupted its character encoding, so the archived file is a **declared transcription with a
published reconstruction map**, not a byte-identical copy — see its own fidelity declaration. It
must not be cited as byte-faithful.

## Present contents

- [`prior_art_review_v3.1.md`](prior_art_review_v3.1.md) — the archived design record.
- [`materialization_log.md`](materialization_log.md) — append-only: what Plan materialized, from
  what source, what it refused to compose, and the session learning of each step.
- [`claude_md_migration_map.md`](claude_md_migration_map.md) — the rule-by-rule evidence that the
  root `CLAUDE.md` became a router without losing law.
