---
record_type: SCIENTIST_WORK_PACKET
id: SCIENTIST-PACKET-RELATION-TYPING-001
title: Relation typing and scale annotation over the declared WWOX claim graph
date: 2026-08-25
status: PREPARED — NOT DISPATCHED. Requires review before execution.
authority_precondition: BLOCKED — see § 0.2
---

# SCIENTIST WORK PACKET — RELATION TYPING (WWOX claim graph)

> **Frame-neutral by construction.** This packet states what is to be adjudicated and what
> evidence exists. It carries **no preferred answer**, and it inherits **no conclusion** from the
> Orchestrator, from Plan, or from any prior analysis. Where a prior reading exists it is named
> as a thing to be checked, never as a thing to be confirmed.

> Nothing here is medical advice. Disease-level only; no individual-level record.
> The human role is referred to as **Operator**.

---

## 0 · Preconditions

### 0.1 What this packet is

39 claim nodes in `disease-models/wwox/registries/claim_registry_current.md` are connected by 20
undirected edges that the registry **already declares**. **0 of 20 carry a relation type.
0 of 39 carry a biological scale.** This packet asks for those annotations to be adjudicated
against primary evidence.

The edges are not proposed here and are not new. Each already exists because a claim record links
to another claim record. Nothing in this packet asks for an edge to be created or removed.

### 0.2 🛑 Authority — this packet is prepared, not dispatched

`governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` selects
**`OPTION B — ACTIVATION_NOT_CONFIRMED`**, `BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE`:

> *"The four contracts remain `PROPOSED` … non-binding documents. Their `status:` lines are
> accurate, not stale."* … *"A new, explicit activation act is required before any actor relies
> on these contracts as binding."*

**No Scientist may execute this packet until that activation act exists.** No part of this
document performs, schedules or specifies it.

### 0.3 A gap the executing Scientist should know about

`roles/scientist.md` has **no OUTPUT / RETURN / deliverable schema section** (measured: its
sections are *Why one file*, *Common section*, *Epistemic independence*, *Working discipline*,
*Reading modes*, *Declared capabilities*, *Fingerprint set*, *Session obligations*). The contract
governs how a Scientist reads and what independence means; it does not define the shape of what
comes back. **§ 4 of this packet therefore states its own return format explicitly**, rather than
citing a clause that does not exist. If the contract later gains a schema, that schema wins.

---

## 1 · Permitted vocabulary — closed sets, not suggestions

These are the values the assembler already declares. **Do not extend them. Do not coin new
relation words.** If no admitted value is true, say so (§ 3).

**Edge relation type — choose exactly one, or decline:**

| Value | |
|---|---|
| `DIRECT` | |
| `INDIRECT_UNKNOWN_INTERMEDIATES` | |
| `ASSOCIATED` | |
| `CONTROVERSIAL_OPEN` | |

**Node biological scale — choose exactly one, or decline:**

| Value | |
|---|---|
| `MOLECULAR` | |
| `CELLULAR` | |
| `TISSUE` | |
| `ORGANISM` | |

---

## 2 · The 20 typing tasks

For each row: the endpoints are the two claim records; the "declaring field" is **where in the
registry the link is already written**, which tells you what kind of statement created it;
"reciprocal" says whether both records point at each other; "shared evidential papers" are the
paper records both endpoints already cite.

**Task ID → edge → declaring field(s) → reciprocal → shared evidential paper(s)**

| Task | Edge (source ↔ target) | Declaring field(s) | Recip. | Shared evidential paper(s) |
|---|---|---|---|---|
| T-01 | CLAIM 001 ↔ CLAIM 002 | `Clinical meaning` | no | **none** |
| T-02 | CLAIM 001 ↔ CLAIM 031 | `Wikilinks` | yes | PAPER 045 |
| T-03 | CLAIM 003 ↔ CLAIM 004 | `Wikilinks` | yes | **none** |
| T-04 | CLAIM 005 ↔ CLAIM 036 | `Evidence boundary` | no | PAPER 057 |
| T-05 | CLAIM 005 ↔ CLAIM 037 | `Evidence boundary`, `Wikilinks` | yes | PAPER 058 |
| T-06 | CLAIM 009 ↔ CLAIM 028 | `⚠️ Counter-directional evidence (BATCH_20260726_001)` | no | PAPER 054 |
| T-07 | CLAIM 009 ↔ CLAIM 034 | `Summary`, `⚠️ Counter-directional evidence` | yes | PAPER 054, PAPER 071 |
| T-08 | CLAIM 016 ↔ CLAIM 035 | `Meccanismo aggiunto (BATCH_20260726_001)`, `Wikilinks` | yes | PAPER 056 |
| T-09 | CLAIM 019 ↔ CLAIM 030 | `Source`, `Wikilinks` | yes | PAPER 041, PAPER 042 |
| T-10 | CLAIM 019 ↔ CLAIM 032 | `Source`, `Wikilinks` | yes | PAPER 041 |
| T-11 | CLAIM 019 ↔ CLAIM 033 | `Wikilinks` | no | PAPER 040 |
| T-12 | CLAIM 028 ↔ CLAIM 034 | `Clinical meaning` | no | PAPER 054 |
| T-13 | CLAIM 028 ↔ CLAIM 035 | `Wikilinks` | no | PAPER 056 |
| T-14 | CLAIM 030 ↔ CLAIM 032 | `Wikilinks` | no | PAPER 039, PAPER 041, PAPER 043 |
| T-15 | CLAIM 030 ↔ CLAIM 033 | `Clinical meaning` | no | **none** |
| T-16 | CLAIM 030 ↔ CLAIM 035 | `Clinical meaning` | no | PAPER 056 |
| T-17 | CLAIM 031 ↔ CLAIM 032 | `Clinical meaning` | no | PAPER 049 |
| T-18 | CLAIM 036 ↔ CLAIM 038 | `Summary`, `Wikilinks` | yes | PAPER 057 |
| T-19 | CLAIM 037 ↔ CLAIM 038 | `Wikilinks` | yes | PAPER 058, PAPER 059 |
| T-20 | CLAIM 037 ↔ CLAIM 039 | `Wikilinks` | yes | PAPER 059 |

**T-01, T-03 and T-15 share no evidential paper between their endpoints.** They cannot be settled
by reading one source. Either two or more primaries must be read, or the correct outcome is a
decline (§ 3). Do not resolve them by inference from the endpoints' status, type or pathway.

### The question to adjudicate — identical for all 20

> Reading the shared primary evidence, which of the four admitted relation types — if any —
> describes the relation between these two claims as the evidence supports it?
>
> Not: which relation would make the graph tidier. Not: which relation the claim titles imply.
> Not: which relation the endpoints' epistemic status suggests.

### Evidence locators already available

- Claim records: `disease-models/wwox/registries/claim_registry_current.md`
- Paper records: `disease-models/wwox/registries/paper_registry_current.md`
- Per-paper verbatim locators: `disease-models/wwox/research/deepdive_manifests/PMID*.json`
  (**64 manifests, 30 bound to at least one claim**)
- Full texts: `files/fulltext/`
- Receipt chain: `python3 framework/scripts/fulltext_receipts.py verify`

---

## 3 · `NOT_SUPPORTED` and disagreement are acceptable outcomes

Explicitly and without penalty:

- **`NOT_SUPPORTED`** — the shared evidence does not support any of the four types. Correct and
  expected for at least some edges.
- **`INSUFFICIENT_EVIDENCE`** — the reading cannot settle it; say what would.
- **`NO_ADMITTED_VALUE_IS_TRUE`** — the relation is real but **none of the four terms fits**. Do
  not force one. Forcing an admitted value writes a known falsehood into the graph. Describe the
  relation in prose and stop; extending the vocabulary is a governance act, not a reading.
- **Unresolved disagreement between Scientists** — a recorded standing disagreement is a valid
  terminal state. Do not converge for the sake of converging.

An edge that ends `UNTYPED` after adjudication is a **result**, not a failure. The count of typed
edges is not a target and no target has been set.

---

## 4 · What to return, per task

Because no contract schema exists (§ 0.3), return exactly:

```
TASK_ID:
EDGE:
VERDICT:            one of DIRECT | INDIRECT_UNKNOWN_INTERMEDIATES | ASSOCIATED |
                    CONTROVERSIAL_OPEN | NOT_SUPPORTED | INSUFFICIENT_EVIDENCE |
                    NO_ADMITTED_VALUE_IS_TRUE
PRIMARY_READ:       PMID(s) actually opened
VERBATIM_LOCATOR:   proposition · quote verbatim · anchor (section / figure / table)
DIRECTIONALITY:     is the relation directional in the evidence? if so, which way?
WHAT_WOULD_CHANGE_IT:
OBSERVATION_SCOPE:  what was read, what was not, and the denominator of any negative
```

A `complete_fulltext_read` requires verbatim locators (`LEGEND_CORE.md` § 5.1). Every reading
emits a `FULLTEXT_READ_RECEIPT`; the caller persists it before closing the turn.

---

## 5 · Two separate replication tasks (not edge typing)

Both come from an **uncommitted, non-canonical** reading of PMID 32000863 and are listed here
**to be checked independently, not confirmed**. The originating artifact is deliberately not
attached, so the replication is blind to its conclusions.

| Task | Question | Where |
|---|---|---|
| **R-01** | Does the Figure 7 legend define the four-asterisk (`****`) significance marker? Enumerate every significance marker the legend defines and every marker the panels use. | PMID 32000863, Fig. 7 legend + panels |
| **R-02** | At what postnatal age were the animals in the Figure 7c western blot? Report what the Methods say and what the Fig. 7c legend says, separately, without reconciling them. | PMID 32000863, Methods + Fig. 7c legend |

For both: report what the source says. If the two surfaces disagree, **record the disagreement as
the finding** — do not choose between them.

---

## 6 · Out of scope for this packet

- Creating, removing or redirecting any edge.
- Decomposing any claim node, or changing any claim's identity or title.
- Extending either vocabulary.
- Editing any canonical file, or performing a BATCH_COMMIT.
- Any DisMech representation question. DisMech is a separate downstream surface; nothing in this
  packet asks about it, and its semantics are not to be imported.
