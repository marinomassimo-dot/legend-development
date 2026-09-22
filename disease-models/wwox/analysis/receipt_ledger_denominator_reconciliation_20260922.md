# Receipt ledger — the `189` vs `200` denominator, closed

**Date:** 2026-09-22 · **Actor:** Orchestrator · **Status:** 🟢 **CLOSED — measured, not inferred**
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
