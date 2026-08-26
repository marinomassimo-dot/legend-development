---
record_type: WORK_ANALYSIS
id: PLAN-CONTROL-PLANE-RELEVANCE-REDUCTION-001
title: The whole relevance fork is eight records on two refs no worktree has checked out
date: 2026-08-26
role: PRODUCER
mode: EXECUTABLE HARDENING / MECHANICAL REDUCTION
authority: Plan role contract. **The relevance set is NOT chosen here.** Every model below is
  measured; none is adopted. No governance text amended, no event emitted.
status: REDUCED to one semantic fork · four of five layers resolved by existing evidence
---

# CONTROL-PLANE RELEVANCE — MECHANICAL REDUCTION

> **Nothing here is medical advice.**

---

## 1 · The five layers, kept apart

The queue's instruction — *do not let one layer silently perform another* — is the whole method
here. Measured separately, four of the five are already settled and only one is open.

| Layer | Question | State |
|---|---|---|
| **PATH RESOLUTION** | starting anywhere, which repository root? | **settled** — `repo_root()` uses `--show-toplevel` and refuses outside a checkout (CPROOT, 12 tests) |
| **SOURCE DISCOVERY** | which objects exist that could be a control-plane record? | **mechanical** — enumerate refs; measured below, no judgement required |
| **RELEVANCE** | which discovered sources participate in current authority? | 🔴 **OPEN. The only open one.** |
| **SINGLETON CLASSIFICATION** | given a relevant set, how many ACTIVE? | **settled** — `lease_singleton.py` classifies an *explicit* set and discovers nothing |
| **AUTHORITY VERDICT** | which record is in force? | **blocked only by RELEVANCE**, and by nothing else |

🔴 The layer that most wants to swallow another is SOURCE DISCOVERY. A tool that enumerated its
own refs would be answering RELEVANCE silently, which is why `lease_singleton.py` has a test that
greps its own source for `for_each_ref`, `rev-parse`, `glob(` and `iterdir(`.

---

## 2 · Source discovery — the whole current repository

`runtime/orchestrator_lease.md` and `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl`, over 60 heads,
6 tags, 6 remote refs and 15 live worktrees.

| Object | Distinct blobs | Distribution |
|---|:--:|---|
| lease | **2** | `c34f4866` (5 records) on 47 heads · `d8a2b47b` (9 records) on `orchestrator` alone |
| approval queue | **3** | `20c24a2b` (6) on 44 heads · `bb603d9a` (10) on `orchestrator` · `95fc8163` (14) on `evidence-index` and `p51c9-rebased-onto-c89c2217` |
| tags | — | every tag carrying the queue carries `20c24a2b`. **Historic refs contribute nothing.** |
| remotes | — | no additional blob |

### Containment, which is what decides divergence

```
LEASE            main's 5 records are a strict PREFIX of orchestrator's 9   -> no contradiction
QUEUE            main ⊂ orchestrator   AND   main ⊂ evidence-index
                 orchestrator ⊄ evidence-index   AND   evidence-index ⊄ orchestrator
                 4 orchestrator-only records · 8 evidence-index-only records · additions DISJOINT
```

Both lateral sets carry `APPROVAL_ID` records — they are decision-bearing, not noise.

⇒ **The lease is `canonical_plus_strict_prefix`.** Every relevance model that includes the
superset returns the same records; a model that excludes it returns a strictly poorer set and
still contradicts nothing. **The lease does not require the decision.**

⇒ **The queue is `two_live_disjoint_suffixes`.** No containment resolves it.

---

## 3 · The models, run against the current repository

| Model | Lease sources | Queue sources | Queue verdict |
|---|---|---|---|
| **M1 CANONICAL_ONLY** (`main`) | `c34f4866` | `20c24a2b` | UNIQUE, trivially |
| **M2 CALLER_WORKTREE** | whichever the caller has | whichever the caller has | never divergent **because it can only ever see one** — the property that made two different objects both exit 0 |
| **M3 LIVE_WORKTREE_HEADS** | `c34f4866`, `d8a2b47b` | `20c24a2b`, `bb603d9a` | **UNIQUE by containment** |
| **M4 ALL_HEADS** | `c34f4866`, `d8a2b47b` | `20c24a2b`, `bb603d9a`, **`95fc8163`** | **DIVERGENT** |
| **M5 ALL_REFS** (+tags, +remotes) | same as M4 | same as M4 | **DIVERGENT**, identically |

Measured counts:

```
queue blobs over ALL heads     44 x 20c24a2b   2 x 95fc8163   1 x bb603d9a   -> 3 distinct
queue blobs over LIVE heads    10 x 20c24a2b                 1 x bb603d9a   -> 2 distinct
```

---

## 4 · 🔴 The minimum semantic fork

**M5 adds nothing to M4.** Tags and remotes carry only the canonical blob, so the "historical
ref" example does not discriminate. **M1 and M2 are not competitors** — M1 is M4 restricted to
one ref, M2 is the defect CPROOT was opened about.

Everything therefore turns on **exactly one difference: M3 against M4.** And that difference is
one object:

> `95fc8163` — 14 records, 8 of them lateral, carried by `evidence-index` and
> `p51c9-rebased-onto-c89c2217`, **neither of which any worktree has checked out.**

Remove that one blob from the relevant set and the queue is UNIQUE by containment, exactly like
the lease. Include it and the queue is DIVERGENT and no evidence in the repository resolves it.

**The decision reduces to:**

> **Does a control-plane record on a ref that no live worktree has checked out participate in
> current authority?**

Nothing smaller is available. Existing governance does not answer it: Annex J.3 says every
`HUMAN_REQUIRED` creates an object in the queue and that the daily brief exposes
`PENDING HUMAN DECISIONS`; it names no ref, and no rule turns a lateral approval on or off.

### Two mechanical facts the decider should have, neither of which decides it

🔴 **M3's relevant set is not a property of the repository.** It is a function of `git worktree
list` — this machine, this moment, not in any commit. **This session added three worktrees and
its own simulation branch while measuring**, and the LIVE set moved underneath the measurement.
A rule whose population is per-machine cannot be reproduced by a reviewer on another machine.

🔴 **M4's DIVERGENT verdict is stable and reproducible**, and it is a refusal, not an answer. It
would leave the authority verdict unavailable until someone decides — which is what a fail-closed
detector is supposed to do, and is also a halt.

**Not chosen. Both consequences stated so that neither reads as the obvious one.**

---

## 5 · The examples the queue named, and what each turned out to be worth

| Example | Reproducible? | Discriminates M3/M4? |
|---|---|---|
| current `main` | yes | no — in every model |
| Orchestrator worktree lineage | yes (`orchestrator`, live) | no — in M3 and M4 alike |
| other actor worktree (`lettore`, `lettore-b`, `lettore-c`, `mirror`) | yes | no — all carry the canonical blob |
| stale branch (`orchestrator-worktree`, `orchwt-rebased-onto-005888b6`, `p51c9-scope-c`) | yes | no — canonical blob or lease absent |
| deleted worktree | yes, **`evidence-index`** and `p51c9-rebased-onto-c89c2217` | 🔴 **YES — the only pair that does** |
| historical ref (6 tags) | yes | **no** — every tag carries `20c24a2b` |
| approval present laterally, absent on `main` | yes — 4 on `orchestrator`, 8 on `evidence-index` | the orchestrator four do not; the evidence-index eight do |
| conflicting ACTIVE lease across two sources | 🔴 **NO** | — |

**The conflicting-ACTIVE example is not reproducible from current repository state.**
`lease_singleton.py` over both real lineages returns **`NO_ACTIVE` — 0 ACTIVE across 2 sources**,
5 and 9 records. Annex J.0's compensating protocol is still unenforceable as deployed, and today
there is no instant at which it would fire. **Recorded as absent rather than synthesised**: a
fixture I built myself would be evidence about my fixture.

---

## 6 · What this does not do

It does not choose. It does not rank M3 above M4 or below it. It does not touch governance text,
and it does not deposit a detector whose verdict a gate could read — a detector that answered
`UNIQUE` for `two_live_disjoint_suffixes` would be asserting a settled authority nobody settled.

**TRUE OPERATOR DECISION, unchanged and now single:** does a control-plane record on a ref no
live worktree has checked out participate in current authority? Everything else in this layer
is already answered.
