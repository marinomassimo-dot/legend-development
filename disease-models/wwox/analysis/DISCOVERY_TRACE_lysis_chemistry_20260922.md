# DISCOVERY_TRACE — can the corpus's own lysis chemistry distinguish "WWOX degraded" from "WWOX in the pellet"?

> **Discovery-space artefact.** Nothing here is a canonical claim. `HYPOTHESIS ≠ CLAIM`.
> Produced with [`legend-discovery-method`](../../../.claude/skills/legend-discovery-method/SKILL.md) V0,
> first repository-native use.
> **Not medical advice.** This reasons about a reference WWOX-DEE genotype class, not any person.

**Date:** 2026-09-22 · **Cycle type:** `recursive_reread` composed with `preregister_prediction`,
entered at REVISIT · **Primitives invoked:** `enumerate_baseline_before_scoring`,
`preregister_prediction`, `recursive_reread`. DIVERGE and CONNECT deliberately **skipped** — this
is a bounded census question over artefacts the repository already holds, not a mechanism problem.

---

## 1 · WHY THE QUESTION CHANGED

**OLD QUESTION** under which the corpus's abundance studies were read:
*"what did this study measure about WWOX protein abundance?"*

**NEW QUESTION:**
*"Could the lysis chemistry each study actually used have recovered an insoluble or aggregated
WWOX species at all — and therefore which 'reduced/absent protein' results in our corpus are
chemically incapable of separating* degraded *from* in the pellet*?"*

**WHY IT CHANGED — two inputs, neither available at first read.**

1. A re-read of Wang 2011 (`PMID 22193544`) found a buffer **named RIPA that contains neither SDS
   nor deoxycholate**. A buffer's *name* therefore does not establish its *stringency*, and a
   census built on buffer names is measuring vocabulary.
2. The cross-domain SDR pair (engineered stabilisation anti-correlated with activity; a pathogenic
   human SDR missense recoverable by restabilisation) makes **fold-incompetence** a live reading of
   a buried proline. A fold-incompetent species is the one most likely to partition into a pellet
   — precisely the fraction a non-denaturing lysate discards before the gel is loaded.

Together these say: an "absent protein" result obtained in a mild buffer is **consistent with
degradation and with aggregation equally**, and the corpus may not record enough chemistry to tell
which. That is a property of the *corpus*, not of any one paper, so it is a re-read question.

---

## 2 · EX-ANTE PREDICTIONS — written and committed before any searching

Each carries its falsifier. Being wrong here is an acceptable outcome; rewriting these after
looking is not.

| # | Prediction | Falsifier |
|---|---|---|
| **P1** | The repository records an **explicit lysis recipe** (named detergents, at stated concentrations) for **fewer than half** of the WWOX studies that report a protein-abundance result. | ≥50 % carry an explicit recipe. |
| **P2** | **At least one further artefact beyond Wang 2011** either names a buffer without recording its detergent composition, or records **no lysis step at all**. | Wang 2011 is the unique instance. |
| **P3** | **No** study in the corpus records a **pellet / insoluble-fraction recovery** step (resuspension and denaturing re-solubilisation of the post-spin pellet). | Any study records one. |
| **P4** | Lysis chemistry and antibody-epitope geometry are recorded in **different artefacts**, so **no single artefact** can answer *"could this study have seen an aggregated WWOX?"* | Some artefact holds both. |
| **P5** | The dominant failure is **source-side** (cause **A**: the paper never wrote the recipe) rather than **extraction-side** (cause **B**: the paper wrote it and our dossier dropped it). | B ≥ A among instances found. |

**P5 is the one that decides what to build.** If **A** dominates, no repository primitive can fix
it and the finding is a bound on the literature. If **B** dominates, it is an extraction defect
and belongs to the reading layer — the distinction the Operator required be kept separate.

---

## 3 · BASELINE — `enumerate_baseline_before_scoring`, both steps

🔴 **Step 2 is the one that historically gets skipped.** Enumeration without reading is not a
baseline. Both steps are recorded below.

**Step 1 — ENUMERATE (by listing, never by guessed filename):** *[to be filled before step 2]*

**Step 2 — READ (grep target concepts across every artefact enumerated):** *[to be filled]*

**Absence-claim scope, declared in advance.** Any absence asserted from this cycle is bounded to:
`FILE TYPE` = repository Markdown + JSONL artefacts · `LANGUAGE` = English ·
`DOCUMENT CLASS` = deep-dive manifests, dossiers, read receipts, registries, queue entries ·
`SOURCE SCOPE` = this repository only, **not** the published literature. A recipe absent *here* is
not a recipe absent *in the paper* — separating those two is what P5 measures.

---

## 4 · RESULT — recorded only after the searches

*[EMPTY AT COMMIT — this section is written after §3 is executed.]*

### 4.1 Prediction-by-prediction

*[empty]*

### 4.2 What the zeros were — the returns that scored nothing

*[empty — a re-read that does not list its zeros is not scoreable]*

### 4.3 Grade

*[empty]* — one of `NONE` · `REDISCOVERY` · `NEW DETAIL` · `NEW CONNECTION` · `NEW HYPOTHESIS` ·
`EXPERIMENT-CHANGING`

### 4.4 Effect on the method itself

*[empty]* — one of `PREVENTED FALSE NOVELTY` · `CHANGED HYPOTHESIS` · `CHANGED EXPERIMENT` ·
`FOUND NEW CONNECTION` · `KILLED BAD EXPERIMENT` · `CREATED FOLLOW-UP` · `NO EFFECT`
