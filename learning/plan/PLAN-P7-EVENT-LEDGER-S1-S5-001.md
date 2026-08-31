---
record_type: WORK_ANALYSIS
id: PLAN-P7-EVENT-LEDGER-S1-S5-001
title: The event ledger is built and has emitted nothing, which is the whole design
date: 2026-08-26
role: PRODUCER
mode: BUILD / DECISION-NEUTRAL SLICES ONLY
authority: Plan role contract — Annex J.1 derived view; § P7 is Plan-defined and already decided.
  No frontier crossed: D-3, D-4, P-1, P-2 untouched. No event emitted.
status: S1–S5 BUILT AND TESTED — CAND-20260826-P7LEDGER. S6 specified, not applied. S7 refused.
---

# § P7 EVENT LEDGER — SLICES S1–S5

> **Nothing here is medical advice.** Runtime control plane only.

**EG-07 read: *"specified, 23 named types, 0 code, 0 events."*** Three of those four are now
false. **The fourth is still true and is meant to be.**

---

## 1 · What was built

`CAND-20260826-P7LEDGER` — branch `plan-p7-event-ledger`, `BASE_HEAD 788c357d`, tip `cb9bec26`,
`CANDIDATE_CONTENT_HASH 17ead4262e034a49e30705463e6344f2cc1c4dd8b2a740e58006ecbbc8ba949c`.

| Slice | Contents | State |
|:--:|---|---|
| **S1** | schema, the **closed** 23-type enum, `validate_event`, chain validation | ✅ |
| **S2** | writer with the own-`ACTOR_ID` refusal, chain extension, duplicate-id refusal | ✅ |
| **S3** | tail anchor (`events` count + `head` digest), truncation detection | ✅ |
| **S4** | replayed consolidated view, cross-actor ordering, per-actor anchors | ✅ |
| **S5** | `CLOSES_EVENT_ID` resolution, `closed_by` **in the view only**, dangling and wrong-type closures reported | ✅ |
| **S6** | LINT wiring at INFO | ⏸ **specified, not applied** — § 4 |
| **S7** | first emission | 🛑 **refused** — § 3 |

**31 tests, all passing.** Every acceptance is paired with an arm that removes the property: the
nine closing types are each tested for refusing a missing `CLOSES_EVENT_ID` **and** for accepting
the same event once it carries one.

**Nothing was re-decided.** § P7 fixed option (a), the path, the format and the view; J.1 fixed the
event shape and the type list. This is implementation of a completed specification.

---

## 2 · Two properties that came out of building rather than reading

### 2.1 · The enum is closed, and J.1 calls it "tipi minimi"

*"Minimum types"* reads like a floor an implementation may extend. **It is treated as closed.** An
open list lets any actor mint a type, and Mirror — whose primary analysis surface this is (G.3) —
would be reasoning over a vocabulary nobody agreed on. Widening the tuple is a governed change to
§ P7, and the refusal message says so rather than saying "invalid".

### 2.2 · 🔴 A line is committed to only by its successor, so the tail is unprotected

Found by a test that failed, twice, and was wrong both times in an instructive way.

The first attempt tampered with the **first** line and expected the chain to break. It did not:
line 1 chains to `None` by definition, so an edited line 1 still validates — and `append` then
computes the new head from the *edited* line and seals the edit into a consistent history.

The second attempt tampered with the **last** line. Same result, and now the general rule was
visible: **a line's content is verified by exactly one thing — the next line's prev-hash.** The
line at the end of the file is verified by nothing inside the file.

| Tampered line | Chain sees it? | Anchor sees it? |
|---|:--:|:--:|
| a line **with** a successor | ✅ — and `append` then refuses to extend a broken chain | ✅ |
| the **last** line | ❌ — validates cleanly | ✅ |
| the **first** line, before any successor exists | ❌ | ✅ |

**This is the same shape as truncation and has the same single answer: the anchor.** It is exactly
why § P7 carries one, and the receipts ledger says the same thing in its own words: *"a hash chain
alone cannot detect truncation."*

⇒ **The writer does not consult the anchor**, and that is stated in the writer's own docstring, not
only here. Wiring it needs a decision about **where an event ledger's anchor is stored** — the
receipts ledger keeps its own in the state manifest — and inventing a second convention is
precisely what § P7 forbids. Until then the integrity claim is *"append-only, with edits to the
tail visible only to an externally held anchor"*, and **it must not be stated more strongly.**

---

## 3 · 🛑 S7 — refused, and the refusal is asserted by a test

**Build is not emit.** Nothing in the repository calls `append`. The module writes nothing on
import, on `validate` or on `consolidate`.

Two tests hold the frontier mechanically rather than by intention:

- `test_this_repository_has_emitted_no_event` — `ledger/events/` holds no `.jsonl`. If it ever
  does, the suite fails and says so;
- `test_importing_the_module_writes_nothing`.

And `validate` on a repository with no events **exits 3, not 0**, with the reason printed. A gate
returning success for having looked at nothing is the defect three other records this session are
about; this one refuses to be an instance of it.

**Why the frontier is real and not caution.** D-3 asks whether § P7 is normative. D-4 asks who may
emit and from when. Both are the Operator's. **A ledger written under a design whose normative
standing is undetermined, by the one actor who could also declare it normative, is the
self-written-record defect one layer up.** Writing the code is not writing the record.

---

## 4 · S6 — specified, deliberately not applied

S6 wires the ledger↔durable-state gap into LINT at **INFO**, which crosses no frontier.

**Not applied, for a reason that is about value rather than authority.** Until S7 there are zero
events, so the check has exactly one possible output on every ref — *"no ledger"*. Adding it now
puts a permanent unconditional line into `legend_lint.py`, whose population is the four scientific
current files and which this session has already found is a gate that **cannot fail on governance
paths** — see § 4.1 of `PLAN-MAJOR2-CANDIDATE-READINESS-001`.

⇒ **Applying S6 before S7 would add a line to the one gate that has just been shown to report
vacuous passes.** It is ready and it belongs with the first emission, not before it.

---

## 5 · Reproduction

**Run from a checkout of the candidate branch**, which is where the two new files live:

```
git worktree add --checkout <dir> plan-p7-event-ledger
```

then, inside it, run `event_ledger.py` and `test_event_ledger.py` — both in the
`framework/scripts` directory:

| Command | Expected |
|---|---|
| `event_ledger.py types` | 23 types, closed |
| `event_ledger.py validate` | **exit 3** — no ledger, nothing validated |
| `test_event_ledger.py` | 31 tests, OK |

and, from anywhere with the refs visible:

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5 --tip cb9bec26c9f71bf95e8a47d9a0b63ac6b2343381
```

✎ **Written this way because writing it the obvious way broke a guard, for the third time today.**
The first draft gave the two commands as plain root-relative paths. `test_documented_commands`
resolves those against **this** worktree, where the files do not exist — they are on the candidate
branch — and went red.

⇒ **A Plan record describing a candidate cannot name the candidate's new files by path**, because
the record lives on the branch that lacks them. Three variants of one constraint have now been hit
in one session: a path that is absent because it was never created; a dot-slash path that resolves
against the reader's directory; and this — **a path that is absent only from here.** The guard is
right every time and is right about a different thing each time, and there is no way to state
"this file exists on that branch" in a form it accepts.
