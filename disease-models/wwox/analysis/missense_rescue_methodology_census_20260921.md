# W-6 · The transferable-methodology census — *can anyone measure whether a re-stabilised missense protein is functional?*

**Date:** 2026-09-21 · **Actor:** Orchestrator · **Mode:** READ-ONLY census.
**No canonical file written. No claim created. No receipt claimed. No therapy proposed.**

> 🔴 **§ 0 · This is a CENSUS, built from titles and abstracts. An abstract is not a read.**
> Every statement below about a paper's content rests on its PubMed abstract. Nothing here may be
> promoted to evidence without a full-text read and a receipt. Where a paper is described as
> "measuring X", read it as "reports measuring X".
> Source of all bibliographic records: **PubMed**. DOI links given per record.

---

## 1 · Why this census exists, and what it is NOT

LEGEND's own [`missense_proteostasis_matrix_20260921.md`](missense_proteostasis_matrix_20260921.md)
closed the WWOX proteostasis line with one sentence, which this file takes as its starting premise
rather than re-deriving:

> 🔴 **"No functional measurement has ever been made on a WWOX missense protein whose abundance was
> restored."** Not weak evidence — none. And the same paper supplies the counter-case: **P282A** is
> an SDR-span substitution indistinguishable from empty vector in every functional assay **with no
> stability defect at all**.

A fresh PubMed census confirms there is **no unread WWOX proteostasis literature** to add (§ 2 D of
[`next_node_scout_20260921_orchestrator.md`](next_node_scout_20260921_orchestrator.md)). So the
Candidate-D question could not be answered by reading more WWOX papers. It was re-posed as a
**methods** question, deliberately aimed **outside** the WWOX literature:

> **Does a laboratory or a transferable, published methodology exist that can measure whether a
> destabilised missense protein, once re-stabilised, is FUNCTIONAL — i.e. function per molecule, at
> matched abundance?**

---

## 2 · The answer

> ## 🟢 **YES. The methodology exists, is mature, is published, and is scaled.**
> ## It has been applied to an **oxidoreductase** and to a **neurodevelopmental epilepsy gene**.
> ## **WWOX has simply never been put through it.**

🔴 **And LEGEND did not know it existed.** Verified, not assumed: `registry_records.py get --pmid`
returns **zero records** for all six PMIDs below, and the strings `VAMP-seq`, `deep mutational
scan*` and `multiplexed assay*` occur **nowhere** in `disease-models/` or `framework/`. This is a
**capability gap in the disease model**, not merely an unread paper.

The class is **MAVE** — *multiplexed assays of variant effect*, also called deep mutational
scanning. The member that matters here is **VAMP-seq** (*variant abundance by massively parallel
sequencing*), which measures **steady-state intracellular abundance** of thousands of missense
variants at once. On its own VAMP-seq answers only the abundance half — which is precisely the half
LEGEND already has and already knows is insufficient. **What makes this census a finding is that
several groups now run an abundance assay and an orthogonal FUNCTION assay on the same variant
library, and report the two axes separately.** That is the "abundance-clamped, function-per-molecule"
comparison the matrix converges on, implemented and published.

---

## 3 · The census, ranked by transferability to WWOX

| # | PMID | Paper | Why it matters here | Retrievability — **tested how** |
|---|---|---|---|---|
| **M-1** | **42425971** | Biar CG, …, Calhoun JD, *Nat Commun* 2026 — *"An integrated, scaled approach to resolve TSC2 variants of uncertain significance"*. Abstract: *"we use massively parallel sequencing to measure the steady-state abundance of almost 9000"* variants. [DOI](https://doi.org/10.1038/s41467-026-75442-6) | 🔴 **The closest template in existence.** **TSC2 is a neurodevelopmental / epilepsy gene** with exactly WWOX's problem — thousands of missense VUS, one-at-a-time assays that do not scale. A rare neurodevelopmental disease solving the missense-VUS problem with an abundance MAVE *integrated* with functional data is the paper a WWOX programme would copy. | ⚠️ **UNTESTED.** `PMC13478581` exists; `get_copyright_status` returned `checked_sources: ["pubmed"]` **only**, so PMC was never consulted and `is_open_access:false` records *what was not checked*. **Must be fetched to know.** |
| **M-2** | **34314704** | Amorosi CJ, …, Dunham MJ, *Am J Hum Genet* 2021 — *"Massively parallel characterization of CYP2C9 variant enzyme **activity and abundance**"*. [DOI](https://doi.org/10.1016/j.ajhg.2021.07.001) | 🔴 **The paired design, on an oxidoreductase.** The title states the two axes explicitly. CYP2C9 is a cytochrome P450 — an **oxidoreductase with a defined catalytic cycle**, which is functionally nearer to WWOX (an SDR oxidoreductase) than any other entry. **But note the asymmetry that limits the transfer, and it is the same one `TX-003` already records: CYP2C9 has a known substrate and WWOX does not.** | ⚠️ **UNTESTED** — `PMC8456167` exists, `checked_sources: ["pubmed"]` only. The `All rights reserved` statement is the **journal's**, not a PMC licence reading. |
| **M-3** | **39319420** | Boyle GE, …, Fowler DM, *Genetics* 2024 — *"Deep mutational scanning of CYP2C19 in human cells reveals a **substrate specificity–abundance tradeoff**"*. [DOI](https://doi.org/10.1093/genetics/iyae156) | 🔴 **A published, named dissociation of abundance from function** in a second oxidoreductase — and in **human cells**, not yeast. This is the empirical counterpart of the P282A counter-case: within one protein family, abundance and function come apart. It would tell a WWOX programme what the dissociation looks like when you go looking for it at scale. | ⚠️ **UNTESTED** — `PMC11538415` exists, `checked_sources: ["pubmed"]` only. |
| **M-4** | **40463067** | Voutsinos V, …, Hartmann-Petersen R, *bioRxiv* 2025 — *"A complete map of human cytosolic degrons and their relevance for disease"*; >200,000 30-residue tiles from >5,000 cytosolic proteins, 99.7 % coverage. [DOI](https://doi.org/10.1101/2025.05.10.653233) | 🔴 **Directly interrogable against LEGEND's open CMA question.** The matrix records that `41124647` *speculated* chaperone-mediated autophagy from a predicted KFERQ-like motif (`LRSVQ`, aa 187–191) that **was never mutated**, with `LAMP2A` and `LAMP2` at zero occurrences. A systematic degron map is an **independent, orthogonal** way to ask whether WWOX carries a cytosolic degron and where — **without** re-running the authors' own assumption. ⚠️ **Preprint, not peer-reviewed — weight accordingly.** | 🟢 **OPEN — CC BY-NC-ND 4.0, `is_open_access: true`, `checked_sources` includes `pmc`.** The one entry verified retrievable today. |
| **M-5** | **29785012** | Matreyek KA, …, Fowler DM, *Nat Genet* 2018 — *"Multiplex assessment of protein variant abundance by massively parallel sequencing"* — the founding VAMP-seq paper. [DOI](https://doi.org/10.1038/s41588-018-0122-z) | The method's primary description: what it measures, its dynamic range, its controls, and its **limits**. Needed to judge whether WWOX is even a suitable substrate for it (WWOX is a mitochondrial/membrane-associated protein in part, and VAMP-seq reads a fluorescent-fusion abundance in a reporter line — **that is a real compatibility question, not a formality**). | ⚠️ `PMC5980760` exists; `checked_sources` includes `pmc` and licence is null → **likely not OA-licensed**, but not proven. Fetch once. |
| **M-6** | **40957416** | Axakova A, …, Roth FP, *Am J Hum Genet* 2025 — *"Landscapes of missense variant impact for human superoxide dismutase 1"*; motivated by 26 % of ClinVar SOD1 missense variants being VUS. [DOI](https://doi.org/10.1016/j.ajhg.2025.08.016) | A **neurological** disease (ALS) missense landscape from an independent major group (Roth). Useful as a second exemplar and for how they argue clinical actionability from a MAVE — but SOD1 is a small soluble homodimer, **structurally unlike WWOX**, so the transfer is procedural, not biological. | ⚠️ UNTESTED. `PMC12696502` exists. |

**Excluded for cause:** `38362799` / `42437345` / `40501845` (MYH7 and MYBPC3 cardiomyopathy MAVEs —
sarcomeric proteins, mechanically assayed; procedurally interesting, biologically remote);
`37843401` (PTEN, molecular-dynamics *prediction*, not measurement, and no PMCID); `32796835`
(tRNA sequencing — a keyword collision, not a variant-effect assay); `37106706` (GJB2 review).

---

## 4 · What this does and does not change

### It changes the experimental roadmap, and that is a real change
The matrix's *"best next experiment"* was written as a **bespoke design** — a titratable promoter, a
dilution series, western-matched levels, a domain-resolved co-IP panel. That design is still
correct and still the cheapest **one-allele** answer. What this census adds is that the **many-allele**
version is not hypothetical: it is a published platform with reported dynamic range, controls and
known failure modes. **A WWOX programme no longer has to invent the assay; it has to port it.**

### It does NOT change the therapeutic queue, and nothing here may be read as if it did
Nothing in this census is an intervention. **Therapeutic classification of the entire census:
`MECHANISTIC PROBE ONLY`.** A MAVE tells you which variants are destabilised and whether the
destabilised ones retain function when present — it does **not** supply a molecule that re-stabilises
them, and it says nothing about neurons, developmental window, seizures or clinical course.

### The obstacle that survives intact, and it is the binding one
🔴 **Every functional MAVE above needs a functional readout that can be scored in pooled format —
and WWOX has none.** `TX-003` already records the reason: *"WWOX is an oxidoreductase with undefined
physiological substrate/activity"*, and the Adelaide review read today put it in the authors' own
words — *"Despite more than twenty years of research on the[] protein, the substrate and product of
the enzyme reaction that it catalyses are yet to be discovered."* CYP2C9 and CYP2C19 are tractable
**because their substrates are known and their turnover is scoreable in a pooled yeast or human-cell
assay.** WWOX is not in that position.

So the honest statement of the finding is a conditional, and it must be carried as one:

> **The abundance half is portable to WWOX today** (VAMP-seq measures steady-state abundance of a
> tagged protein and needs no substrate). **The function half is not portable until a scoreable
> WWOX function exists.** The candidates for that function are **binding**, not catalysis — the
> SDR-domain partner panel the matrix already specifies (tau, GSK3β, POLE4) with a WW1-dependent
> partner as the control that must stay normal. **Whether any of those can be run in pooled,
> multiplexed format is the open question this census hands forward, and it is unanswered.**

---

## 5 · Next actions, ranked — and none of them is a claim

1. **Test retrievability by fetching**, not by reading a flag. Four of six rows are `UNTESTED`
   under this repository's own standing rule: `is_open_access:false` with
   `checked_sources: ["pubmed"]` records *what was not checked*. `PMID 41124647` returned that exact
   flag and then delivered 68,491 characters. **Attempt the fetch; measure the body length.**
2. **Read M-1 (TSC2) first**, not M-2. It is the only entry that is simultaneously a
   **neurodevelopmental disease**, a **missense-VUS problem of LEGEND's shape**, and an
   **integrated** abundance-plus-function design. The question to put to it: *what functional assay
   did they pair with abundance, and would an analogue exist for a protein with no known substrate?*
3. **Read M-4 (degron map) second** — it is the one verified-open entry, and it can be interrogated
   against an **already-open LEGEND question** (the unvalidated KFERQ-like `LRSVQ` motif) rather
   than opening a new one.
4. **Do not open a WWOX MAVE as a research line.** That would be a materially new programme and is
   the Operator's decision, not an autonomous one. This census records that the option exists and
   what it would cost to evaluate; it does not propose it.

---

## 5b · One observation about the guard, recorded and NOT acted on

This file cites **six PMIDs that LEGEND holds in no form**, and
`legend_lint.py` / `session_self_eval.py` both return **`unread_premises: 0/0`** with it in the
tree. Two hours earlier the same ratchet fired on a *single* citation — `PMID 42464650` — and again
on `PMID 33520443`. The difference is that those two are **WWOX-corpus** papers and these six are
not.

🔴 **So the `UNREAD_PREMISE` ratchet protects against leaning on an unread *WWOX* paper, not
against leaning on an unread *anything*.** That is a scope property of the guard, plausibly by
design — its docstring is about conclusions resting on unopened corpus papers — but it means a
methodological or cross-domain citation enters the reasoning layer **unanchored and silently**, and
this file is the first in the repository to do so at volume.

**No gate is proposed and none should be.** This session is scientific; adding a guard is not its
work. The existing control is sufficient and was used: the six papers are queued as `FT-115`, so
they carry an anchor whether or not a checker demands one. The observation is written down so the
next harness session can decide whether the scope is intended, with a worked example in hand.

---

## 6 · Declared limits

- **Nothing here was read.** Six abstracts, one census. No receipt, no locator, no claim.
- **Retrievability is asserted for exactly one row** (M-4) and declared UNTESTED for four.
- **The transfer argument is mine, not any author's.** No paper above mentions WWOX. Every
  statement that a method "would" apply to WWOX is an inference by this file, and the binding
  obstacle in § 4 is stated precisely because that inference does not survive without it.
- **`P282A` remains the brake.** An SDR-span substitution can be functionally dead with normal
  abundance. Any MAVE result on WWOX would have to be read against that, and an abundance-only
  MAVE would be **actively misleading** for exactly the alleles that matter most.

*Not medical advice. Non-canonical research-layer file.*
