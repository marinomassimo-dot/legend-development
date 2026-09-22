# Receipt ledger — the `189` vs `200` denominator, closed

**Date:** 2026-09-22 · **Actor:** Orchestrator · **Status:** 🟢 **CLOSED — measured, not inferred** · ⭐ **FORK RECONCILED 2026-09-22 under operator authorization — see § 7**
**Reason:** the Operator asked for the exact denominator once, before the next canonical propagation,
and explicitly did **not** ask for a new audit. This document exists so the question is never
re-derived. **No ledger record was created, altered, reordered or removed to produce it.**

---

## 1 · The answer

**Both numbers were correct. Neither was a reporting error.** They are two branches of the same
ledger, forked at record 189.

| | this branch | sibling `f7595f6` |
|---|---|---|
| total records | **189** | **200** |
| shared prefix, **in identical order** | **188** | **188** |
| appended beyond the prefix | **+1** | **+12** |
| duplicates | **0** | — |
| excluded / non-chained | **0** | — |
| invalid JSON lines | **0** | — |

`188 + 1 = 189`. `188 + 12 = 200`. **Union of distinct `event_id`s = 201.**

## 2 · It is a hash-chain FORK, and that is the operative fact

- Last shared record (#188): **`FTR-20260921-35984507-02`**
- Our #189: `FTR-20260922-30202070-01`, `ledger_prev_hash = 2fc6d9d6…`
- Sibling #189: `FTR-20260921-37974179-01`, `ledger_prev_hash = 2fc6d9d6…`

> 🔴 **Both sides chain from the IDENTICAL parent hash.** This is a clean fork, not a divergence of
> content or a disagreement about history.

**Consequence for the merge — this is the part that matters operationally:**

> **The merge is two-way and is NOT a concatenation.** Neither branch is a superset of the other, so
> taking either one loses records. And because every record's `ledger_prev_hash` points at its
> predecessor, appending one side's records to the other's tail **invalidates their hashes**: one
> side's appended records must be **re-chained** onto the merged tail, and the **state-manifest tail
> anchor re-computed**.

⚠️ Per `CLAUDE.md`, hand-editing the ledger breaks its hash chain and halts LEGEND **until the edit
is undone, or authorized and re-anchored**. A merge is therefore an **authorized, re-anchoring
operation**, not routine maintenance. It is not performed here.

## 3 · What the denominator is made of

```
189 rows  =  1 genesis record (no ledger_prev_hash)  +  188 hashed links
          =  189 unique event_id   ·   0 duplicates
          =  189 valid JSON lines  ·   0 invalid
```

By `record_kind`:

| kind | n |
|---|---|
| `contemporaneous_receipt` | **164** |
| `legacy_reconstruction` | **22** |
| `identity_correction` | **2** |
| `receipt_invalidation` | **1** |
| **total** | **189** |

`fulltext_receipts.py verify` → **`OK: 189 chained receipt(s), tail anchored in
framework/state/state_manifest_current.md`**.

⚠️ Note that `receipt_invalidation: 1` and `identity_correction: 2` are **records in the chain**, not
deductions from it. The ledger is **append-only**: a correction is appended, never applied in place.
So `189` is the count of *records*, and is **not** the same quantity as "papers read" — a question
this document does not answer and which must not be derived from this number.

## 4 · What each side contributed

**Ours (+1):** `FTR-20260922-30202070-01` — the Mallaret partial full-text read persisted in this
session.

**Sibling (+12), all dated `20260921`:** `37974179` · `35712340` · `42589397` · `42425971` ·
`40463067` · `42523332` · `41228229` · `30356099-02` · `37583270` · `31618474` · `32214227` ·
`30783266`.

## 5 · The four hypotheses the Operator named, answered

| hypothesis | verdict |
|---|---|
| duplicates | ❌ **0 duplicate `event_id`s** |
| excluded / non-chained records | ❌ **0 excluded; 189/189 chained** |
| prior reporting error | ❌ **no** — each number was correct for its own branch when reported |
| **branch divergence** | ✅ **yes, and specifically a hash-chain fork at record 189 from a shared parent** |

## 6 · Standing note for the next canonical propagation

This does **not** block the current science, and nothing in the WWOX model depends on it. But
**before any propagation that appends a receipt**, the fork must be resolved, because a new record
appended to this branch deepens the fork by one and makes the eventual re-chain larger. The decision
— merge now, or continue on this branch and re-chain later — is the Operator's, and the re-anchoring
is an authorized operation either way.

---

## 7 · ⭐ FORK RECONCILED — operator-authorized, 2026-09-22

Authorization: *"I authorize reconciliation of the confirmed receipt-ledger fork derived from the
common 188-record prefix."* Scope explicitly excluded unrelated registry cleanup and broader ledger
reconciliation; **none was performed.**

### 7.1 The five reported quantities

| | |
|---|---|
| **common prefix length** | **188** events, agreeing **in identical order** |
| **unique records from this branch** | **1** — `FTR-20260922-30202070-01` |
| **unique records from sibling `f7595f6`** | **12** — all dated `20260921` |
| **merged total** | **201** · 201 unique `event_id`s · **0 duplicates** |
| **semantic receipt content changed** | 🟢 **NO — proven, not asserted** (§ 7.3) |

### 7.2 The deterministic ordering rule used — the repository's own, not a new one

**`fulltext_receipts.py rechain --onto <base>`**, the canonical subcommand for exactly this operation
(*"rebase this ledger's divergent events onto another ledger's history"*). Its rule:

> **the base ledger's history is retained entire, and the divergent suffix of the incoming ledger is
> re-chained onto its tail, in the incoming ledger's own order.**

`--onto` was the **sibling** (200 events), incoming was **this branch** (189). Hence:
**188 shared prefix → sibling's 12 → this branch's 1.**

🟢 **The rule and chronology agree, which is why this assignment was chosen:** the sibling's twelve
are all `20260921` and ours is `20260922`, so the rebase order is also the event order. Final three,
in order: `FTR-20260921-32214227-01` · `FTR-20260921-30783266-01` · `FTR-20260922-30202070-01`.

**No `--rename` was needed or used** — the 13 divergent identifiers are pairwise distinct, so no
identifier collision arose and **no work manifest required re-pointing**.

### 7.3 Semantic preservation — proven by construction AND by measurement

**By construction.** The tool's `event_body()` strips exactly one field, and its docstring states the
invariant: *"`ledger_prev_hash` records WHERE an event sits, not WHAT it says … the body is the
identity a rechain must preserve, and the chain field is the only thing it is allowed to touch."*
`common_prefix_length` likewise compares **by body, deliberately not by digest**.

**By measurement.** Before the operation, the union of all distinct event bodies across both ledgers
was computed with the tool's own canonical serializer and fingerprinted:

```
expected  cc6cc9cff895ca9cfa5d8ca81716f81be8b729f11e0c6f23b3577ff7b73358b1
actual    cc6cc9cff895ca9cfa5d8ca81716f81be8b729f11e0c6f23b3577ff7b73358b1
```

And independently:

| check | result |
|---|---|
| all **189** pre-merge bodies present afterwards | ✅ |
| all **200** sibling bodies present afterwards | ✅ |
| pre-merge records whose **body** changed | **0** |
| pre-merge records whose **`ledger_prev_hash`** changed | **1** — `FTR-20260922-30202070-01`, the only record that had to move |
| records deleted, rewritten or deduplicated | **0** |

> **Only one chain field in the entire ledger changed, and no body changed at all.** *"Re-chain only
> the records that must move after the common fork point"* is satisfied at its minimum: one.

### 7.4 Tail, anchor, verification, gates

```
201 chained · head f64bed890f037ca8b67de5083e244151dd7f40fbccfade243856e1f1d20fc85e
state_manifest_current.md:  fulltext_ledger_events 189 → 201
                            fulltext_ledger_head   8c2ebb2e… → f64bed89…
```

`fulltext_receipts.py verify` → **`OK: 201 chained receipt(s), tail anchored`** · `legend_lint` →
**PASS** · `growth_anchors check` → **PASS**, `unread_premises 0` · `public_release_gate` → **PASS,
BLOCKS 0** · `current_state: READY`.

**Change footprint: exactly two files** — the ledger and the manifest anchor. Nothing else was
touched, and the pre-merge ledger was snapshotted before the operation.

### 7.5 What this closes, and the one thing it does not

🟢 **The fork is gone.** Appending a receipt no longer deepens a divergence, so the ordering
constraint between *"merge"* and *"next propagation"* — flagged in § 6 as a decision rather than a
detail — **is lifted**.

⚠️ **Unchanged, and still not derivable from `201`:** this is a count of **records**, including the
`identity_correction` and `receipt_invalidation` events, which the append-only ledger **appends
rather than applies**. **It is not a count of papers read** and must not be used as one.
