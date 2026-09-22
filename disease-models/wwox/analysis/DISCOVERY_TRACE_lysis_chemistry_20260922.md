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

**Step 1 — ENUMERATE (by listing, never by guessed filename):**
`ls disease-models/wwox/research/deepdive_manifests/*.json` → **81 manifests**.

**Step 2 — READ (grep target concepts across every artefact enumerated):**

| Concept | Manifests | Note |
|---|---|---|
| `western` / `immunoblot` — the **abundance denominator** | **28** | the studies whose results this question is about |
| any detergent — `RIPA`, `deoxycholate`, `Triton`, `NP-40`, `CHAPS` | **0** | 🔴 not one, in 81 manifests |
| `\blysis\b` (word-boundary) | **1** | `PMID25012504` |
| `\blysates?\b` | **8** | the noun only; no chemistry attached |
| `pellet` / `insoluble` / `sonicat` | **0** | 🔴 |
| `epitope` / `immunogen` | **2** | `PMID19500159`, `PMID39416860` — **neither names a detergent** |

> 🔴 **STEP 2 CAUGHT A FALSE POSITIVE THAT WOULD HAVE INVERTED THE ANSWER.** An unbounded
> `grep -i lysis` returns **48 of 81** manifests, which reads as *"the corpus discusses lysis
> extensively."* **47 of those 48 are the substring inside `ana-lysis`.** With a word boundary the
> true count is **1**. Enumeration gave 48; reading gave 1. This is the exact failure mode step 2
> exists for, and it is a **tenth** way a search returns a false result: not a false negative from
> a missed synonym, but a **false positive from a substring of an unrelated high-frequency word.**

**Schema check — why the zeros are structural.** A manifest's top-level keys are:
`pmid · doi · receipt · group_assessment · field_density · multihop · corpus_crossquery ·
retraction_check · landing · skills_considered · concurrency_note · verbatim_locators`.
**There is no Methods field and no reagent field.** A buffer recipe can only ever land in
`verbatim_locators`, and only if a reader happened to quote it for some other purpose.

**Absence-claim scope, declared in advance.** Any absence asserted from this cycle is bounded to:
`FILE TYPE` = repository Markdown + JSONL artefacts · `LANGUAGE` = English ·
`DOCUMENT CLASS` = deep-dive manifests, dossiers, read receipts, registries, queue entries ·
`SOURCE SCOPE` = this repository only, **not** the published literature. A recipe absent *here* is
not a recipe absent *in the paper* — separating those two is what P5 measures.

---

## 4 · RESULT — recorded only after the searches

Searches executed after the pre-registration was committed at `44d1a74`.

### 4.1 Prediction-by-prediction

| # | Prediction | Outcome | What actually happened |
|---|---|---|---|
| **P1** | explicit lysis recipe for **< 50 %** of abundance studies | 🟢 **SUPPORTED — and I under-predicted the magnitude** | Not "fewer than half". **Zero of 28.** No manifest in the corpus names a single detergent. I predicted a shortfall; the actual state is an absence. |
| **P2** | ≥1 artefact beyond Wang 2011 with a named buffer lacking composition, or no lysis step | 🟠 **SUPPORTED, but the framing was wrong** | Wang 2011 is not one bad record among several. It is the **only** paper whose buffer chemistry the repository has *ever* recovered — and that recovery came from a **re-read**, not from its manifest. Its manifest names no detergent either. |
| **P3** | **no** study records pellet / insoluble-fraction recovery | 🟢 **SUPPORTED** | Zero of 81 mention `pellet`, `insoluble` or `sonicat`. |
| **P4** | chemistry and epitope geometry never in the same artefact | 🟢 **SUPPORTED** | Two manifests mention an epitope; neither names a detergent. Intersection empty. |
| **P5** | source-side (**A**) dominates extraction-side (**B**) | 🔴 **REFUTED — by being unanswerable, which is the finding** | The question cannot be asked of this corpus. **Neither A nor B is measurable**, because the extraction layer has **no field for the datum**. See §4.3. |

**P5's refutation is the most valuable line in this cycle**, and it is exactly the case
`preregister_prediction` exists to protect: had P5 been written after the search, it would have
been written as *"a third cause exists"* and would have looked like foresight rather than a miss.

### 4.2 The zeros — returns that scored nothing

A re-read that does not list its zeros is not scoreable. These were looked for and **not** found:

- **No detergent name anywhere** — searched `RIPA`, `deoxycholate`, `Triton`, `NP-40`, `CHAPS`.
- **No buffer-composition disagreement to adjudicate.** The hypothesis that other papers would
  replicate the Wang 2011 name-vs-composition mismatch returned nothing, because **no second
  composition exists in the repository to compare against**. Zero, not a contradiction.
- **No pellet-recovery precedent**, so the §17 census cannot be built from held material.
- **`PMID25012504`**, the single genuine `lysis` hit, carries the word without a recipe — it did
  not rescue P1.

### 4.3 🎯 Grade: `NEW CONNECTION` — and it names a **third** cause, not a third instance

The finding is not *"the corpus records lysis chemistry badly."* It is:

> **The deep-dive manifest schema has no slot for reagent or Methods chemistry at all.** The
> absence is not a reading failure and not a source failure. It is **structural**.

This splits a distinction the programme has been holding as a binary:

```
A · SOURCE-SIDE OMISSION      the paper never wrote the clause
B · HAND-BACK COMPRESSION     the report dropped it in summarising
C · SCHEMA-SIDE OMISSION      ← new: the field does not exist, so the datum
                                was never capturable, never dropped, never carried
```

🔴 **C is currently invisible because it looks like A.** A missing recipe reads as *"the paper
didn't say"* when the truth may be *"we never had anywhere to put it."* And the two route to
opposite layers: **A** is a bound on the literature and cannot be fixed; **B** belongs to the agent
communication layer; **C** belongs to the manifest schema. Merging C into B — the natural move,
since both are "our side" — sends the fix to the wrong layer entirely.

**This does not license a schema change.** One cycle is not evidence. It licenses **stating the
bound**, which is §4.4.

### 4.4 Effect: `CHANGED EXPERIMENT` + `PREVENTED FALSE NOVELTY` + `CREATED FOLLOW-UP`

- **CHANGED EXPERIMENT.** The standing instruction to *"classify by actual chemical recipe, not the
  word RIPA"* **cannot be executed from repository artefacts.** Any solubility or pellet census
  must return to the papers' Methods sections as primary retrieval. A census built from manifests
  would have returned a confident, uniform, and entirely vacuous answer.
- **PREVENTED FALSE NOVELTY, twice.** (i) The `ana-lysis` substring would have supported
  *"48 manifests discuss lysis"* — off by 47. (ii) "No WWOX study examined the pellet" was about to
  be restated; the bounded form is **"no repository artefact records one,"** which is a statement
  about our extraction, not about the literature. The scope declaration in §3 forced that split.
- **CREATED FOLLOW-UP.** Cause **C** needs a second independent instance before anyone touches a
  schema. The test is cheap and pre-stated here: pick another Methods-level datum that changed a
  conclusion — antibody catalogue number, fixation protocol, animal age at sacrifice — and ask
  whether the manifest schema has a slot for it. **If C is real, the answer is no for all three.**
  If any has a slot, C is narrower than claimed.

---

## 5 · FOLLOW-UP EXECUTED — and it **weakens** cause C, as pre-stated it should be allowed to

§4.4 pre-stated the test: *"pick another Methods-level datum that changed a conclusion — antibody
catalogue number, fixation protocol, animal age at sacrifice — and ask whether the manifest schema
has a slot for it. **If C is real, the answer is no for all three.**"*

Run over the same 81 manifests:

| Methods datum | Manifests | Verdict against the pre-stated criterion |
|---|---|---|
| detergent / lysis chemistry | **0** | the original instance |
| antibody catalogue / RRID | **2** | 🔴 not zero |
| fixation protocol (PFA / formalin) | **3** | 🔴 not zero |
| animal age at sacrifice | **13** | 🔴 not zero, and not rare |

🔴 **C IN ITS STRONG FORM IS REFUTED, by the test I wrote to refute it.** I claimed the datum was
*never capturable*. It is captured — sporadically. The criterion was "no for all three"; the answer
is yes for all three.

**The surviving, weaker form.** There is no **dedicated field**, so capture is **incidental**: a
Methods datum reaches the repository only when a reader quotes it into `verbatim_locators` for some
*other* purpose. That predicts presence that is uneven rather than absent — which is what the
gradient shows.

🎯 **And the gradient is the actual finding, better than the one I predicted.** Capture probability
tracks **how close the datum sits to the question the first reader was asking**:

```
age at sacrifice   13   ← a DESIGN variable; readers quote it to describe the experiment
fixation            3
antibody catalogue  2
detergent           0   ← a BENCH variable; no reader's question ever made it relevant
```

This is the `recursive_reread` thesis, measured: **value sits in the part of the paper the first
reader's question made irrelevant** — and the census shows *which* parts those are, corpus-wide.
Bench chemistry is the systematically invisible class.

**One concrete bound, immediately usable.** 🔴 **Eleven manifests mention an antibody; zero record a
catalogue number.** The repository therefore **cannot identify which antibody any study used.**
Given that a published "no protein" finding has already reversed on a change of antibody, any
epitope-geometry reasoning over held artefacts is unsupported — that too must return to the papers.

**Status of C:** strong form refuted; weak form ("incidental capture, gradient by reader-question
proximity") has **two** instances and remains a candidate. Still no schema change. The honest note
is that the gradient hypothesis was **generated after seeing the data** and is therefore not
pre-registered — it must be tested on a fourth datum before it counts as anything.

---

### 4.5 Honest limits of this cycle

- This measured **81 deep-dive manifests**, not the full repository. Dossiers, receipts and queue
  entries were **not** exhaustively read. A recipe may sit in one; it would not change C, which is
  a claim about the manifest schema, but it would soften P1's "zero".
- **One cycle.** C has a single instance. By this method's own standard that is a candidate, not a
  finding, and §4.4 treats it as one.
- DIVERGE and CONNECT were skipped by design. If the zeros have a mechanistic explanation other
  than "no field exists", divergence would have been the step to find it, and it was not run.
