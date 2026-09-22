# LEGEND SCIENTIFIC DISCOVERY METHOD — V0, SHADOW MODE

**Status:** 🔴 **OBSERVATIONAL INSTRUMENTATION. NOT NORMATIVE. NOT A GATE. NOT AN AUTHORITY.**
Nothing in LEGEND reads this file at runtime. It creates no approval layer, no reviewer, no
registry and no workflow. It does not modify Orchestrator authority, and it cannot block a
`BATCH_COMMIT`, a deep dive, a hand-back or a landing.
**Date:** 2026-09-22 · **Author:** Orchestrator · **Companion to:**
[`LEGEND_SCIENTIFIC_DISCOVERY_METHOD_V0_PROPOSAL.md`](LEGEND_SCIENTIFIC_DISCOVERY_METHOD_V0_PROPOSAL.md)
(the argument) and `disease-models/wwox/research/native_primitive_scorecard_*.md` (the evidence).

> **What this file adds that neither companion has.** The proposal argues; the scorecard counts.
> Neither says **how to run the primitives without adopting them**. That is the whole content here.

---

## §0 · The rule that outranks everything below

The operator's standing directive **§26** forbids answering a scientific mistake with a new gate,
authority, auditor, registry or workflow.

🔴 **Citation correction, made here because this file would otherwise inherit the error.** The V0
proposal's §0 attributes that rule to *"`LEGEND_CORE` §26."* **`LEGEND_CORE.md` has no §26** — it
ends at **§22, FINAL MAXIMS**. The rule is the **operator's task directive** §26, which is how
every commit candidate in this repository cites it (*"per the operator's §26"*), and which
`governance/candidates/CAND-20260819-ORCHSURF.md:444` had already disambiguated in writing
(*"directive §26, not body §26"*). The proposal is the **only** file that misattributes it, and it
does so in the one sentence it calls *"the one design constraint that outranks everything below."*
**Corrected in the proposal in the same act as this file.** Nothing about the constraint changes;
only its address does.

**Therefore every primitive here is a habit, never a check.** A primitive that becomes a gate has
failed, because a gate converts a thinking move into a compliance move, and a compliance move is
satisfied by the cheapest output that passes it.

## §1 · What "shadow mode" means, exactly

| shadow mode **is** | shadow mode **is not** |
|---|---|
| running a primitive because it is useful, and **recording whether it changed an outcome** | running a primitive because a rule says to |
| a trace written **after** a cycle, in the artefact that cycle produced | a separate log, file or registry — 🔴 **there is no shadow-mode ledger, and creating one would be the §26 violation** |
| silent — nothing depends on it, nothing waits for it | a reporting obligation |
| abandonable mid-cycle with no consequence | a checklist to complete |

**An incomplete trace does not stop execution and is not a defect.** An absent trace is data about
the primitive's cost.

## §2 · The candidate set, reconciled honestly

🔴 **The directive's seven and the scorecard's eight are not the same list, and pretending they are
would be the first thing this file got wrong.** The mapping, stated rather than smoothed:

| directive §19 candidate | scorecard row | status |
|---|---|---|
| `enumerate_baseline_before_scoring` | same name | ✅ direct |
| `diverge_hypotheses` | same name | ✅ direct |
| `connect_domains` | same name | ✅ direct |
| `preregister_prediction` | same name | ✅ direct |
| `recursive_reread` | same name | ✅ direct |
| **`compress_experiment`** | 🔴 **no scorecard row exists** | **new — zero recorded instances, entering shadow mode with an empty evidence column** |
| **`adversarial_verify`** | 🔴 **no scorecard row exists** | **new — but see §2.1; it may already exist under another name** |
| — | **`gate_is_not_quantity`** (5 instances, 4 domains) | 🔴 **on the scorecard, absent from the directive's list** |
| — | **`verify_the_omitted_clause`** (6 instances) | 🔴 **the strongest row on the scorecard, absent from the directive's list** |
| — | **`outcome_distribution_width`** (1 + 1 failure) | 🔴 on the scorecard, absent from the directive's list |

**Consequence, recorded and not resolved:** the two primitives with the most recorded
outcome-changing instances in this repository are **not** in the directive's candidate set, and two
of the directive's candidates have **no recorded instances at all**. A V0 assembled from either list
alone would be assembled from the wrong evidence. **Shadow mode therefore runs all ten**, and the
merge itself is a finding about how candidate lists get written — from what an author remembers
proposing, not from what the record shows worked.

### §2.1 · `adversarial_verify` may be a rename, not a new primitive

Before this is scored as new, `enumerate_baseline_before_scoring` applies to the primitive set
itself. LEGEND already ships **`legend-locator-audit`** — a *blind* adversarial audit where the
auditor receives only `(proposition, quote, anchor)` triples, never the dossier, never the reader's
name, never the conclusions. That is a stronger instrument than any habit called
`adversarial_verify` would be, and it is **already implemented, already routed**.
⇒ 🟡 **`adversarial_verify` enters shadow mode `PROVISIONAL — SUSPECTED DUPLICATE`.** Its first job
is to establish that it does something the locator audit does not. **Proposing a primitive that
duplicates a better existing tool is exactly the §26 failure mode.**

## §3 · The trace format (directive §20)

Recorded **inside the artefact of the cycle**, as a short table at its end. Seven steps, one line
each. **Steps that produced nothing are named as such** — that line is the most informative one on
the page, because it is the only evidence that can ever lower a primitive's score.

```
| step | what happened |
|---|---|
| BASELINE          | what was enumerated, at what scope, and what it found or failed to find |
| DIVERGE           | how many hypotheses, and which survived — name the one you would have chosen first |
| CONNECT           | what was imported from outside the corpus, with WHAT TRANSFERS / WHAT DOES NOT |
| PREDICT           | the predictions, and their adjudication: CONFIRMED / REFUTED / UNTESTED |
| SEARCH/EXPERIMENT | routes run, positive controls carried, and every zero's interpretation |
| ADJUDICATE        | the verdict, in the vocabulary the claim will actually carry |
| REVISIT           | what this cycle makes askable of literature already read |
| produced nothing  | 🔴 REQUIRED LINE. Which steps returned nothing, and whether that was cost or information |
```

**Grading vocabulary for a `recursive_reread` return**, fixed so it cannot drift:
`NO NEW INFORMATION` · `REDISCOVERY` · `NEW DETAIL` · `NEW CONNECTION` · `NEW TESTABLE HYPOTHESIS` ·
`EXPERIMENT-CHANGING INSIGHT`.
🔴 **A fact already represented elsewhere in this repository grades `REDISCOVERY`, however much work
it took to find.** Do not reward finding what is already held.

## §4 · The scoring rule, and the one revision this run makes

**A primitive earns an evidence count only from an instance where it CHANGED AN OUTCOME** — a
conclusion, a grade, a next experiment, or a caught error. **A primitive that merely ran does not
count.** Failures count with the same weight as benefits. A primitive with zero recorded failures is
marked ***untested against failure***, not clean.

### §4.1 · `outcome_distribution_width`, revised (directive §24)

The original rule — *an experiment's value is the width of its outcome distribution* — **failed
once**, by being applied to a readout that could not carry the discrimination. The revision:

> **score = `OUTCOME WIDTH` × `HYPOTHESIS DISCRIMINATION`**
>
> A **wide but non-discriminating** outcome distribution is **low value**.
> A **narrow but hypothesis-separating** measurement can still be **high value**.
> 🔴 **And the clause whose absence caused the failure: check that any arm you add perturbs ONLY
> the variable in question.** The withdrawn 26–30 °C arm moved synthesis, degradation and the
> chaperone complement at once.

**To be tested prospectively.** This formulation is not yet evidenced; it is a repair of a rule that
broke, and repairs of broken rules are exactly the kind that look right and are not.

### §4.2 · `verify_the_omitted_clause` — count the two mechanisms SEPARATELY (directive §23)

Two distinct things wear the same name and **must not be merged**:

| | mechanism | what it would justify |
|---|---|---|
| **A** | **SOURCE OMISSION** — a limiting clause exists in the source and was not propagated | 🟢 a **native scientific-reading primitive** |
| **B** | **HAND-BACK COMPRESSION** — the delegate found it and omitted it from the summary | 🟠 **agent communication / harness design**, not a reading primitive |

**Only source-side value supports the primitive.** Current tally: of six recorded instances,
**two are cleanly source-side** (Hamdan's second discriminator; Breton's *"caudal-side down"*) and
**three are corrections to delegate reports**. ⚠️ **The headline count of 6 is therefore not the
number that supports adoption; the number is 2.** Counting them together would measure how much a
hand-back compresses and call it a property of the literature.

🟢 **A third class appeared this run and is recorded as source-side-equivalent:** the omitted clause
was in **our own evidence chain** — a page adjudication that restored `±`, `<`, `⁺` and `⁻` on a
table row and never named the row's **unit**, while the needle used to find the row was made of the
very character in doubt. No delegate was involved. *(`research/recursive_reread_3_4_units_20260922.md`
§4.1.)* It counts as **A**, because the artefact was read and the adjacent fact was in it.

## §5 · KEEP / REFINE / DROP / MORE DATA — criteria written so they can actually fire

| verdict | fires when |
|---|---|
| **KEEP** | ≥ 3 outcome-changing instances, **from ≥ 2 different actors on ≥ 2 different days**, **and** ≥ 1 recorded instance where the primitive was run and correctly returned nothing |
| **REFINE** | the rule was sound and the **application** was not — i.e. a failure that the rule as written contains nothing to prevent |
| **DROP** | ≥ 2 instances where running it **cost** a cycle and changed no outcome, with no compensating success; **or** it is shown to duplicate a shipped tool |
| **MORE DATA** | everything else — including every primitive with **zero recorded failures**, which is the default state of six of ten |

🔴 **The missing instrument, unchanged and still not built.** Every row's failure column would fill
fastest by running a primitive **deliberately on a case where it should not help** and recording
that it did not. **No such run has been made.** Until one is, a `KEEP` on this page is a statement
about a sample with no negative controls in it, and should be read that way.

## §6 · What would falsify shadow mode itself

Stated so this file is not unfalsifiable:

1. **If trace-writing starts changing the science** — if a cycle is shaped to fill seven rows —
   shadow mode has become a gate and must be withdrawn. **Symptom: a `CONNECT` row that imports an
   analogy nobody needed.**
2. **If the traces are never read**, they are cost with no return and must be withdrawn.
3. **If a primitive's count rises without any `produced nothing` line ever appearing**, the counting
   is measuring enthusiasm, not outcomes.
4. **If anything begins to depend on a trace** — a review, a landing, a hand-back acceptance —
   §26 has been violated and the dependency, not the trace, is the thing to remove.

## §7 · What this file explicitly does NOT do

- ❌ No primitive is mandatory. ❌ No primitive may block anything.
- ❌ No new registry, ledger, reviewer, approval layer or workflow. **There is no shadow-mode ledger.**
- ❌ Orchestrator authority is unchanged. Delegate contracts are unchanged.
- ❌ Nothing here is implemented, and nothing here is recommended for implementation.
- ❌ Nothing here is medical advice, and no primitive on this page has any clinical meaning.
