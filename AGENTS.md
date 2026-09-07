# AGENTS.md — the Codex adapter, and nothing else

This file exists so that a Codex-hosted session reaches **the same instruction chain a
Claude-hosted session reaches**, and so that the difference between the two runtimes is
*declared* rather than discovered. It carries no operating law of its own. Every rule it
could restate already has a home, and a rule with two homes drifts — which is not a
worry here but a measurement: on 2026-08-26 four live `codex/*` branches were found
carrying an `AGENTS.md` whose sync rule contradicted the one on `main`, unnoticed for
sixteen days, because nothing checks this file against anything.

> `ACTOR_ID != RUNTIME != SESSION != WORKTREE != AUTHORITY`
>
> You are running **Codex**. That is a runtime. It is not an actor, it is not an
> authority, and it does not decide which of those you have.

The contract is in the repository's canonical governance, scientific and release files.

---

## 1 · The chain, in this order

| # | Read | Why it is here and not summarised here |
|---|---|---|
| 1 | [`framework/state/state_manifest_current.md`](framework/state/state_manifest_current.md) | the live state; confirm `current_state: READY` |
| 2 | [`CLAUDE.md`](CLAUDE.md) | the router — **including its § 0**, which binds before anything else and which this file deliberately does not copy |
| 3 | [`BOOTSTRAP.md`](BOOTSTRAP.md) | on a first run with no laboratory at all. A lease is not a precondition for work — [§21e AGILE OPERATING MODE](framework/instruction/LEGEND_CORE.md#21e-agile-operating-mode) — and being in the root does not make you the Orchestrator |
| 4 | [`governance/ANNEX_INDEX.md`](governance/ANNEX_INDEX.md) → the body and annexes | the constitution |
| 5 | [`roles/`](roles/) — **your own contract, named by the operator** | who you are is assigned, never inferred |
| 6 | [`framework/protocols/index.md`](framework/protocols/index.md) and the skills `CLAUDE.md` § 2 names | the procedures for the work at hand |

`CLAUDE.md` is the router for both runtimes. It is not "the Claude file": it is the
shared entry, and this file's only job is to put a Codex session on it with the runtime
difference stated.

### 1.1 · Four obligations, **named here and stated elsewhere**

These bind before you reach the protocol that defines them, so an entry point that does
not at least *name* them makes them optional in practice. What follows is the name and
the address. **The rule itself is not reproduced here** — go and read it, because a rule
with two homes is a rule with two versions.

| Obligation | Where the rule actually lives |
|---|---|
| `FULLTEXT_READ_RECEIPT` — every full-text analysis emits and persists one, on every route | [`framework/protocols/fulltext_read_receipt.md`](framework/protocols/fulltext_read_receipt.md) |
| `verbatim_locators` — captured while the document is open, and `deepdive_manifest.py` refuses a complete read without them | [`framework/protocols/fulltext_read_receipt.md`](framework/protocols/fulltext_read_receipt.md), enforced by [`framework/scripts/deepdive_manifest.py`](framework/scripts/deepdive_manifest.py) |
| the local abstract corpus written by [`pubmed_corpus_harvest.py`](framework/scripts/pubmed_corpus_harvest.py) is a census, not evidence — **un abstract non è una lettura**, and it clears no reading debt | the harvester's own `evidential_status` declaration, and [`framework/master/gold_is_in_the_details.md`](framework/master/gold_is_in_the_details.md) |
| `STOP POLICY`, `DECISION AUTHORITY` and `AGILE OPERATING MODE` — when you may **not** stop, what you decide without the operator, and how your task branch reaches `main` in hours. Open all three at the start of the session, not when you first want to stop | [§21c STOP POLICY](framework/instruction/LEGEND_CORE.md#21c-stop-policy), [§21d DECISION AUTHORITY](framework/instruction/LEGEND_CORE.md#21d-decision-authority) and [§21e AGILE OPERATING MODE](framework/instruction/LEGEND_CORE.md#21e-agile-operating-mode) |

Naming is not stating: nothing above tells you what to *do*, and every one of them will
refuse you at a gate if you skipped its file.

## 2 · Fail closed

**If any surface in § 1 cannot be read, stop.** Do not proceed on the ones that loaded, and
do not reconstruct the missing one from memory or from this file. Record
`BLOCKED_BY_GOVERNANCE`, name the surface, and ask the operator.

The former runtime-parity bootstrap and its hook gate have been retired. Identity is still
assigned by the operator; repository work is validated by the scientific LINT, release gate,
regression suites, CI and ex-post review.

## 3 · Runtime boundary

No project-level Claude or Codex hook is registered. Runtime capabilities do not confer
repository authority; follow the assigned role and the canonical scientific, privacy and
release checks.

## 4 · Your ACTOR_ID

**It is assigned by the operator and confirmed at registration.** It is never derived
from the runtime you are hosted on, the session you are in, the directory you opened, or
the branch you are on. A working directory is not an identity, in either direction; the
lease is the Orchestrator's authority and nothing else is.

If you do not know your `ACTOR_ID`, you do not have one yet. Ask.

## 4 · Sync rule

Normative sources and the state manifest win. This file routes and declares; it
adjudicates nothing. Change it only when the chain in § 1 changes — never to restate a
rule that already has a home.
