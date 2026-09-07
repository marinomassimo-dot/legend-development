# COMMIT CANDIDATE — dose transferability: the decision table, and the ambiguity that turned out to be on the other side

**Candidate ID:** CC-20260826-DOSE-DECISION-TABLE-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** closes two open questions left by
[`CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01`](CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01.md) and
recasts its findings as a four-class decision table. **Does not supersede it.**
**Change class:** MODERATE — no claim reversal; qualifies a quantity used for reasoning
**Canonical targets:** `CLAIM 004` · `CLAIM 011` · `dismissal_ledger_current.md`
**Base head:** `ccddc28939234ad4fe29c417935a0dbe11de86d0` (branch `lettore`)
**Batch gate:** intentionally untouched

---

## 0. Two things the prior candidate left open, now closed against the primaries

### 🔴 Closure 1 — Repudi's per-hemisphere / total ambiguity is resolved by the paper's own Results sentence

The prior candidate wrote: *"If the legend means total, the table is dose-matched. If it means per
hemisphere, … the direction survives both readings; the magnitude does not."* It read the Methods
and the figure legend. **It did not read the Results narrative, which states the basis a third
time and settles it.**

| Locus | Verbatim |
|---|---|
| **Results** | *"Viral particles (**2 × 10¹⁰/hemisphere**) of AAV9-hSynI-mWwox, AAV9-hSynI-hWWOX, or AAV9-hSynI-EGFP were injected into the ICV region of `Wwox`-null mice at birth (P0)"* |
| **Methods** | *"Approximately 1 µl (**2 × 10¹⁰ GC/hemisphere**) virus was dispensed … **The other hemisphere was injected in the same way.**"* |
| Fig 2A/2D–F legends | bare *"(2 × 10¹⁰)"* — an abbreviation of the above |

⇒ **Repudi's total dose is 4 × 10¹⁰ GC**, stated on a per-hemisphere basis in two independent
places, with both hemispheres injected. The bare legend figure is an abbreviation, not a second
reading. **The branch is closed.**

**Consequence for the comparison.** The correct pairing is Repudi-4E10-total against Obeid's 4E10
column, not its 2E10 column:

| Region | Repudi Fig 2G (4E10 total, **P19, n = 3 mice**) | Obeid Fig S3C (4E10) | ratio |
|---|---|---|---|
| Cortex | ≈61.5 % | ≈53 % `*` | ≈1.16× |
| Hippocampus | ≈70.5 % | ≈52 % `ns (0.07)` | ≈1.36× |
| Cerebellum | ≈57 % | ≈61 % `ns` | 🔴 **≈0.93× — inverted** |

⚠️ **This changes the prior candidate's §2 conclusion.** It stated *"the direction survives both
readings"*. Under the **resolved** reading the direction survives in cortex and hippocampus and
**inverts in cerebellum**. A uniformly higher Repudi transduction is no longer the observation;
a **region-dependent** difference is. That is a weaker and more specific claim, and it is the one
the panels support.

Repudi Fig 2G's own counting basis, verbatim: *"NeuN and WWOX double-positive cells were
calculated from **3 identical sagittal sections** of the AAV-hWWOX-injected mice (**n = 3**)
brains"*, at **P19**.

### 🔴 Closure 2 — the unresolvable dose ambiguity is **Obeid's**, not Repudi's

The prior candidate treated Obeid's doses as totals without testing it. They are not stated on any
basis at all.

| Paper | Volume basis | Both hemispheres? | Dose basis stated? |
|---|---|---|---|
| Repudi 2021 | *"Approximately 1 µl"* per hemisphere | ✅ *"The other hemisphere was injected in the same way"* | ✅ **`GC/hemisphere`, twice** |
| Obeid 2026 | *"delivering **2.0 μL/hemisphere**"* | ✅ *"The procedure was repeated for the contralateral hemisphere"* | 🔴 **never** — every dose is a bare `vg` |

⇒ `4 × 10¹⁰ vg` in Obeid is **either** 4E10 total (2E10/hemisphere) **or** 4E10 per hemisphere
(8E10 total). The paper does not say, and the factor-of-two is exactly the size of the effect the
comparison is trying to detect. 🔴 **Injected vg is therefore `NON_TRANSFERABLE` between these two
studies for a reason that has nothing to do with biology: the two papers do not report the same
physical quantity.**

---

## 1. 🔴 The authors say it themselves

Obeid 2026, Discussion, verbatim:

> *"We also cannot exclude that the optimal dose was not achieved, as all vectors were tested at
> the same titer (4E10). Notably, a limitation of our study is that WWOX expression levels were not
> normalized across promoter conditions, and **vector genome copy number, transcript abundance, or
> protein levels were not systematically quantified across all constructs.**"*

⚠️ **Do not over-read this.** Its scope is *"across all constructs"* / *"across promoter
conditions"* — the **promoter-comparison arm**. It does **not** apply to Figure 5, which quantifies
GC, mRNA and protein for the **LD/HD dose arm** at P30. Both statements are true and they scope to
different experiments. Reading the limitation as global would falsely mark Figure 5 unmeasured.

---

## 2. The decision table

**Classes.** `SUPPORTED` = both studies measure it on a comparable scale and it can carry a
comparison · `CONFOUNDED` = both measure it, but something uncontrolled sits between them ·
`UNMEASURED` = at least one study does not measure it · `NON_TRANSFERABLE` = measured on both
sides yet structurally incapable of transferring.

| # | Axis | Repudi 2021 (PMID 34747138) | Obeid 2026 (PMID 42422765) | **Verdict** |
|---|---|---|---|---|
| 1 | **Regional WWOX protein relative to WT** | ❌ WWOX IHC shown by region; **never quantified against WT** | ✅ **Fig 5I–L**, cortex/HPC/midbrain/cerebellum, *"WWOX intensity relative to WT"*, **P30**, LD & HD | 🔴 **UNMEASURED** (one side) |
| 2 | **Delivered genome copies per brain/region** | ❌ **absent** | ✅ **Fig 5A–D**, *"Vector genome copies (GC) … at postnatal day 30 (P30), measured by qPCR and normalized to WT levels"* | 🔴 **UNMEASURED** (one side); ⚠️ **and CONFOUNDED in unit** — see §3 |
| 3 | **Expression per genome** (protein or mRNA ÷ GC) | ❌ neither numerator nor denominator | ✅ **derivable within Obeid alone** — 5A–D ÷ 5E–H or 5I–L, same regions, same age | **UNMEASURED** cross-study; **SUPPORTED within Obeid only** |
| 4 | **% NeuN⁺WWOX⁺ (transduction)** | ✅ Fig 2G — **P19, n = 3 mice, 3 sagittal sections each** | ✅ Fig S3C — **age and n stated nowhere** | ⚠️ **CONFOUNDED** — one reason, not two (§0 removes the other) |
| 5 | **Measurement age** | ✅ P19 (Fig 2G), P17 (Appendix) | ✅ P30 (Fig 5); 🔴 **unstated (Fig S3C)** | ⚠️ **CONFOUNDED** — AAV expression rises for weeks post-injection; P19 vs unstated is not a comparison |
| 6 | **Vector architecture** | `ITR-hSynI-hWWOX-polyA-ITR` | same cassette, plus a WPRE-bearing arm | ✅ **SUPPORTED** (verified at Appendix Fig S1A pixels by the prior candidate) |
| 7 | **Promoter** | hSynI | hSynI | ✅ **SUPPORTED** |
| 8 | **WPRE status** | WPRE-free | both arms present and **directly compared** | ✅ **SUPPORTED as matched** — 🔴 and the comparison is what makes axis 11 `NON_TRANSFERABLE`: Fig S3F pairs `KO+W-WPRE (6E10vg)` against `KO+W (2.63E11vg)`, an implied **≈44× dose-equivalence for one cassette element** |
| 9 | **Titre method** | *"Viral titer was measured by qRT–PCR using bGH primers"* | *"Viral titers were determined by RT-qPCR using bGH primers"* | ⚠️ **CONFOUNDED** — nominally identical; **neither reports a reference material or standard curve**, and neither reports lot, empty-capsid ratio or infectivity |
| 10 | **Strain and age at injection** | FVB, P0 | FVB, P0 | ✅ **SUPPORTED** |
| 11 | 🔴 **Injected vg itself** | 2E10 GC/hemisphere ×2 = **4E10 total**, basis stated twice | bare `vg`, **hemisphere basis never stated**, 2.0 µL/hemisphere ×2 | 🔴 **NON_TRANSFERABLE** — different reported quantities (§0.2) **and** non-linear within one study (§4) |
| 12 | **Follow-up duration** | ~330 d | Fig 3B 300 d; **Fig 2B only 50 d** | ⚠️ **CONFOUNDED** — and this alone explains Obeid's apparent internal dose inversion |
| 13 | **Survival censoring** | legend: *"total n = 16, alive n = 6, spontaneously dead n = 6, 4 mice … taken out for analysis"* — while the curve reaches 0 % | censoring marked on the curve | ⚠️ **CONFOUNDED** — Repudi's terminal fraction cannot be taken at face value |

### Counts

| Verdict | Axes | n |
|---|---|---|
| ✅ `SUPPORTED` | 6, 7, 8, 10 | **4** |
| ⚠️ `CONFOUNDED` | 4, 5, 9, 12, 13 | **5** |
| 🔴 `UNMEASURED` | 1, 2, 3 | **3** |
| 🔴 `NON_TRANSFERABLE` | 11 | **1** |

🔴 **Not one axis in the `SUPPORTED` column is a dose quantity.** All four are design constants —
architecture, promoter, WPRE status, strain/age. They establish that the two experiments are
*comparable in kind*; **none of them carries a dose.**

⇒ **The queue's instruction is satisfied in the negative: there is no transferable vg dose, and
the evidence says so.** No estimate is offered in place of the unmeasured quantities.

---

## 3. ⚠️ A unit ambiguity in axis 2 that must not be resolved silently

Figure 5A–D reports *"Vector genome copies (GC) … **normalized to WT levels**"*. **Wild-type mice
receive no vector.** The normaliser is therefore not a vector quantity, and the caption does not
say what it is. The two readings that fit — GC per diploid genome expressed against the WT
two-copy endogenous `Wwox` signal, or qPCR signal against a WT-derived standard curve — differ by
a factor that is not derivable from the figure.

⇒ Even if Repudi had measured GC, **axis 2 would still not be `SUPPORTED` without this caption
field.** It is recorded as a question for the authors, not a reading debt: no further reading of
this corpus can supply it.

---

## 4. Why vg fails even within one study — retained from the prior candidate, unchanged

Obeid Fig S3E, densitometry relative to the `4 × 10¹⁰` WPRE-free arm:

| Arm | Cortex | Hippocampus | Midbrain | Cerebellum |
|---|---|---|---|---|
| WWOX **4E10** (WPRE-free) | 1 | 1 | 1 | 1 |
| WWOX **8E10** (WPRE-free) | **3.0** | **3.0** | **5.5** | **16.7** |

Doubling vg multiplies WWOX protein by **3–17×**, region-dependently. Combined with the ≈44×
WPRE equivalence of axis 8, `vg` is non-linear in dose, non-uniform across regions, and shifted by
an order of magnitude by a single cassette element.

⚠️ **A nomenclature boundary from the same figure set:** Fig 5's caption writes *"in G and H it is
**near significant**, p value = 0.08 and 0.06"*. `near significant` is not a result class. Those two
regional mRNA comparisons are `ns`, and must be carried as `ns` with the p-value beside them.

---

## 5. `DECISIVE_MEASUREMENT` — unchanged, and now with its unit fixed

> On banked tissue from both cohorts, one protocol: **regional WWOX protein relative to wild type**
> by the same western, alongside **vector genome copies per diploid genome** by the same qPCR —
> **with the normaliser named** — on the **same regions at the same age**. Report transduction
> percentage **with its age and n**.

**Standardise on protein-relative-to-WT, not GC.** It sits on an absolute biological scale
(WT = 1), it is the proximate cause of rescue, Obeid already reports it in two figures, and it is
one step closer to the phenotype than GC — which is exactly where the 3–17× non-linearity enters.

🔴 **No estimate is offered for any `UNMEASURED` axis.** Axes 1, 2 and 3 have no value on the
Repudi side and none is imputed.

---

## 6. Proposed canonical effect

1. **`CLAIM 011` (MODERATE).** The LD/HD threshold must never be cited without vector configuration
   and follow-up window. Add: *"expression per genome is non-linear in dose and region-dependent in
   this same study (3–17× for a 2× dose step), so the threshold is not a biological constant."*
2. **`CLAIM 004` (MODERATE).** Record the transduction percentages **with age and n** (P19, n = 3
   mice, 3 sections each) and the **total dose 4 × 10¹⁰ GC (2 × 10¹⁰/hemisphere, both hemispheres)**
   — the basis, not the bare figure.
3. **Dismissal-ledger entry (strengthened).** *"A vg dose transfers between WWOX gene-therapy
   studies"* → ❌ **REJECTED** on three independent grounds: within-study non-linearity; the ≈44×
   WPRE equivalence; and 🔴 **the two papers not reporting the same physical quantity**.
   **`REVIVAL_TRIGGER`:** two studies reporting **regional WWOX protein relative to WT** at a
   matched, stated age, agreeing on outcome at matched protein.
4. **`full_text_queue` note.** Two author questions, neither answerable by further reading:
   (a) Fig S3C's measurement age and n; (b) Fig 5A–D's GC normaliser.

---

## 7. What this candidate does not claim

- **Not that Repudi's vector was better.** Different lots, unreported infectivity, an unmatched
  measurement age and now a region-dependent rather than uniform difference.
- **Not that transduction percentage explains the survival gap.** Directionally consistent in two
  regions of three, and confounded.
- **Not that Obeid's Figure 5 is unmeasured.** The Discussion limitation scopes to the promoter arm
  (§1); Figure 5 is the dose arm and is quantified.
- **Not that either study is wrong.** Neither set out to be comparable with the other.

---

## Review required

None for queueing. §6.1–6.2 are MODERATE annotations that ride with
[`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md)'s operator review.
