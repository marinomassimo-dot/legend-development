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

*[EMPTY AT COMMIT — written only after retrieval.]*
