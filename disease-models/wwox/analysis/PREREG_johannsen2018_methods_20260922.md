# PRE-REGISTRATION — Johannsen 2018 (PMID 29808465) Methods retrieval

> **Discovery-space artefact.** `HYPOTHESIS ≠ CLAIM`. Nothing here is canonical.
> **Not medical advice.** Reasons about a reference WWOX-DEE genotype class, not any person.
> Primitive: `preregister_prediction`. Written and committed **before** the full text is retrieved.

---

## 1 · Why this paper, and why now

Two independent censuses this session concluded the same thing: the reagent and chemistry evidence
for the Q230P molecular-state question **is not in the repository** (0 of 81 manifests name a
detergent; 0 record a pellet step; 11 mention an antibody and none a catalogue number). The
instruction to *classify by actual chemical recipe, not the word RIPA* therefore has to go to the
papers' Methods.

**Baseline enumeration then found something larger.**

| Artefact | State |
|---|---|
| `deepdive_manifests/PMID29808465.json` | 🔴 **does not exist** — not among the 81 |
| `reading_state.md:98` | 🔴 **`abstract_only` · read** |
| receipts | one carries `reread_reason: inadequate_prior_coverage` |

**PMID 29808465 is the primary functional source for Q230P** — two homozygous sisters, patient
fibroblasts, *qRT-PCR transcript normal + Western blot protein not detected*, with the authors
leaving **impaired translation** and **premature degradation** both open. It is cited by
`PAPER 041` and load-bearing in the claim registry.

🔴 **The canonical status `MOLECULAR FATE UNRESOLVED` currently rests on an abstract.** Its Methods
have never been read. That is not a criticism of the grading — `abstract_only` is recorded
honestly, and the `PREMISE: DETECTION_FLOOR` note already refuses to read *not detected* as
*absent*. It means the highest-information available action is to read the Methods.

---

## 2 · The question

*Does Johannsen 2018's Methods section contain the chemistry needed to distinguish* **H3
post-translational degradation** *from* **H4 insolubility/misfolding** *— and if not, what is the
narrowest experiment that would?*

This matters because the two route to different interventions. If the Q230P species is degraded,
the target is turnover. If it partitions into a pellet the lysate discarded, the protein was
**present and never loaded onto the gel** — a different problem entirely, and one where "not
detected" is an artefact of fractionation rather than a measurement of abundance.

---

## 3 · EX-ANTE PREDICTIONS — with falsifiers

| # | Prediction | Falsifier |
|---|---|---|
| **P1** | **No pellet / insoluble-fraction analysis** is reported. The post-spin pellet is discarded unexamined. | Any resuspension, denaturing re-solubilisation or pellet blot is described. |
| **P2** | The lysis buffer is either **unnamed**, or named **without full detergent composition**; no SDS/urea/guanidine denaturing recovery step appears. | A complete recipe with a strong denaturant is stated. |
| **P3** | The **immunoblot detection floor is not quantified** — no dilution series, no recombinant standard, no stated LOD. | Any explicit sensitivity limit is reported. |
| **P4** | **No measurement of synthesis rate** — no pulse-label, no puromycin, no polysome fractionation. So "impaired translation" is offered as an alternative the paper **did not test**. | Any synthesis-rate measurement is present. |
| **P5** | The antibody is identified by **vendor at most**, with its **epitope region not stated**. | The epitope or immunogen region is given. |

## 4 · The consequence, pre-stated so it cannot be retrofitted

- **If P1 ∧ P2 hold:** *protein not detected* **cannot discriminate H3 from H4** in this source.
  The canonical `MOLECULAR FATE UNRESOLVED` is then not merely cautious but **exactly right**, and
  it cannot be narrowed from this paper at all. The therapeutic branch in §20 of the operator
  brief stays unselected — and that is a result, not a stall.
- **If P1 is falsified** (a pellet was examined): that is the highest-value datum in the corpus for
  this question and changes the next experiment immediately.
- **If P4 is falsified**: "impaired translation" becomes a tested alternative rather than an open
  one, which would narrow the state map by one hypothesis.

🔴 **Scoring rule, fixed now:** each prediction gets `SUPPORTED` / `REFUTED` / `AMBIGUOUS` /
`UNTESTED`. If the full text proves unobtainable, every prediction is scored **`UNTESTED`** and
none is quietly dropped. Retrieval failure is not evidence for a prediction.

---

## 5 · RESULT

### 5.1 Retrieval outcome: **BLOCKED**, and the distinction matters

| Route | Outcome | What it establishes |
|---|---|---|
| PubMed MCP `convert_article_ids` | **no PMCID** | authoritative: the article is **not in PMC** |
| Unpaywall (`api.unpaywall.org`) | `curl (56) CONNECT tunnel failed, response 403` | 🔴 **transport blocked by this environment's network policy** |
| Europe PMC (`ebi.ac.uk`) | same 403 tunnel failure | 🔴 **transport blocked** |

🔴 **Only the first row is evidence about the paper.** The other two say nothing whatever about
whether an open copy exists — they say this container is not permitted to ask. Recording a blocked
request as "not available" would be the same error class as §6's self-matching `pgrep`: reporting a
property of the instrument as a property of the subject.

### 5.2 Predictions: all **`UNTESTED`** — none dropped, none inferred

| # | Prediction | Score |
|---|---|---|
| P1 | no pellet / insoluble fraction examined | **`UNTESTED`** |
| P2 | no full detergent composition | **`UNTESTED`** |
| P3 | detection floor not quantified | **`UNTESTED`** |
| P4 | no synthesis-rate measurement | **`UNTESTED`** |
| P5 | epitope region not stated | **`UNTESTED`** |

🔴 **The scoring rule fixed in §4 is honoured exactly: retrieval failure is not evidence for a
prediction.** I expected P1–P5 to hold, and I still do — and that expectation is worth nothing, so
it is not recorded as support. Had this been scored after the fact, the temptation to write "the
predictions are almost certainly right" would have been strong and would have been unfalsifiable.

### 5.3 🎯 What was obtained anyway — `NEW DETAIL`, from metadata alone

Retrieval failed; the cycle did not. The PubMed record carries indexer-assigned MeSH terms that the
abstract does not mention:

> **`HEK293 Cells`** · **`RNA Stability`** · `Cells, Cultured`

Both are **new to the repository's `abstract_only` record**, and both bear directly on the
molecular-state question:

- **`HEK293 Cells`** implies a **heterologous expression arm** — a second, independent measurement
  of Q230P protein in a non-patient context. The repository has been reasoning as though this
  source contains patient fibroblasts only. If an overexpression experiment exists, it is a
  different detection regime (higher expression, different chaperone load, different lysis) and it
  may be where a residual band would be visible if one exists anywhere.
- **`RNA Stability`** implies transcript stability was assessed as such, not merely level — a
  finer measurement than *"qRT-PCR normal"*.

🔴 **Bounded honestly:** MeSH terms are **indexer-assigned**, not author statements. They establish
that a professional indexer judged these topics present; they do **not** establish what was
measured, in which figure, or with what result. This is a **pointer**, not a datum, and it is
recorded at that strength. It does not narrow `MOLECULAR FATE UNRESOLVED` by even one hypothesis.

### 5.4 Grade and effect

**Grade: `NEW DETAIL`** — not `NEW CONNECTION`, because nothing here changes a mechanism; and not
`NONE`, because two previously unrecorded experimental contexts are now on file.

**Effect: `CREATED FOLLOW-UP` + `PREVENTED FALSE NOVELTY`.**
The false novelty prevented is subtle and worth naming: this session was one step from treating
*"the repository holds no lysis chemistry for Q230P"* as *"no lysis chemistry was ever published
for Q230P."* The baseline check showed the load-bearing paper was never read past its abstract —
so the corpus-level absence measured in `DISCOVERY_TRACE_lysis_chemistry` is, for this paper at
least, **an artefact of our own reading depth**, not a property of the literature.

### 5.5 The one precise action this leaves

**`HUMAN_REQUIRED`** — obtain Johannsen et al. 2018, *Neurogenetics* 19(3):151–156,
`doi:10.1007/s10048-018-0549-5`, and read **Methods** for: lysis buffer composition, any
pellet/insoluble handling, the HEK293 arm's design, antibody identity and epitope, and whether
transcript **stability** (not level) was measured.

Blocked here by network policy, not by the paper. A deployment permitted to reach Unpaywall,
Europe PMC or a library proxy may well obtain it without any human at all — **this is an
environment limit, and it should not be recorded as a literature limit.**
