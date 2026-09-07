# COMMIT CANDIDATE — what transfers instead of vg: ten candidate quantities, tested

**Candidate ID:** CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** systematic test of every alternative explanation derivable from the two studies
**Extends:** [`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md), which
excluded WPRE and left the residual unexplained
**Change class:** MODERATE — no claim reversal; replaces a **quantity** used for reasoning
**Canonical targets:** `CLAIM 004` · `CLAIM 011` · dismissal ledger
**Batch gate:** intentionally untouched

---

## 0. Method — no preferred explanation

Ten axes, each checked against what **both** papers actually report. An axis is `SUPPORTED` only
if both studies measure it on a comparable scale; `NOT_MEASURED` if either does not;
`CONFOUNDED` if both measure it but something uncontrolled sits between them.

🔴 **The result is not the one I expected.** The axis that looked most promising is `CONFOUNDED`,
and the reason is a missing figure caption rather than a biological difference.

---

## 1. The ten axes

| # | Axis | Repudi 2021 | Obeid 2026 | Verdict |
|---|---|---|---|---|
| 1 | **Age at injection** | P0–P1 | P0–P1 | ✅ **MATCHED** — excluded |
| 2 | **Strain / background** | FVB | FVB *(stated verbatim)* | ✅ **MATCHED** — excluded |
| 3 | **Titre assay calibration** | *"qRT–PCR using bGH primers"* | *"RT-qPCR using bGH primers"* | ✅ **MATCHED nominally.** ⚠️ Same method ≠ same standard curve, and neither reports a reference material |
| 4 | **Promoter / construct** | hSynI; `ITR-hSynI-hWWOX-polyA-ITR` | hSynI; same, WPRE-free arm | ✅ **MATCHED** (verified at Appendix Fig S1A pixels) |
| 5 | **Vector preparation** | Vector Biolabs **or** HUJI Vector Core | Fujifilm / Vector Biolabs / BIB; HUJI ELSC Core | ◐ **OVERLAPPING SOURCES, DIFFERENT LOTS.** Neither reports lot, empty-capsid ratio or infectivity |
| 6 | **Follow-up duration** | ~330 d | Fig 3B 300 d; **Fig 2B only 50 d** | 🔴 **NOT MATCHED across figures** — and this alone explains Obeid's apparent internal dose inversion |
| 7 | **Survival censoring** | 4 of 16 censored ("taken out for analysis"); 🔴 legend says 6 alive while the curve reaches 0 | censoring marked ("black dot… collected for analysis") | ⚠️ **CONFOUNDED** — Repudi's terminal fraction cannot be taken at face value |
| 8 | **Delivered genome copies per region** | ❌ **never measured** | ✅ Fig 5A–D, qPCR, normalised to WT | 🔴 **NOT_MEASURED on one side** — the obvious transferable quantity does not exist for Repudi |
| 9 | **Expression per genome** | ❌ not quantified regionally | ✅ Fig 2E, S3B, S3E, Fig 5I–L | 🔴 **NOT_MEASURED on one side** — and see §3, it is wildly non-linear |
| 10 | **Transduction efficiency (% NeuN⁺WWOX⁺)** | ✅ **Fig 2G** | ✅ **Fig S3C** | 🟡 **THE ONLY SHARED QUANTITY** — see §2 |

---

## 2. 🟡 The one shared quantity, and why it is `CONFOUNDED` rather than `SUPPORTED`

Both studies report the **identical assay under the identical label**: the percentage of NeuN⁺
neurons that are also WWOX⁺, in cortex, hippocampus and cerebellum, after WPRE-free
AAV9-hSynI-hWWOX at a nominal 2 × 10¹⁰ vg.

| Region | **Repudi Fig 2G** (2 × 10¹⁰, **P19, n = 3**) | **Obeid Fig S3C** (2E10) | Obeid Fig S3C (4E10) |
|---|---|---|---|
| Cortex | **≈61.5 %** (≈56–67) | ≈42 % | ≈53 % `*` |
| **Hippocampus** | **≈70.5 %** (≈62–79) | **≈39 %** | ≈52 % `ns (0.07)` |
| Cerebellum | **≈57 %** (≈49–65) | ≈53 % | ≈61 % `ns` |

Read at 600 dpi from the article PDF (Repudi) and at 300 dpi from `mmc1.pdf` page 4 (Obeid).

**At the same nominal dose, Repudi reports ≈1.5× the cortical and ≈1.8× the hippocampal
transduction that Obeid does.** Direction and magnitude are consistent with the survival gap, and
the largest divergence is in the **hippocampus** — the seizure-relevant region.

### 🔴 Why this cannot be closed

The Figure S3 caption, read in full from `mmc1.pdf` page 5, states neither a **measurement age**
nor an **n** for panel C:

> *"(C) A graph representing the percentage of NeuN and WWOX positive cells in the cortex,
> hippocampus and cerebellum in Wwox-null mice injected with AAV9-hSyn-hWWOX 2x10¹⁰vg and
> 4x10¹⁰vg. Quantification of the WPRE vector was not possible due to its expression pattern."*

Repudi's is **P19, n = 3**. Obeid's is **unstated**. Transduction percentage is age-dependent
(AAV expression rises over weeks post-injection), so a comparison across an unknown age gap is
not a comparison.

⚠️ **A further ambiguity that must not be resolved silently:** Repudi's Methods give
`2 × 10¹⁰ GC/hemisphere` (≈4 × 10¹⁰ total) while its Fig 2A legend prints a bare `2 × 10¹⁰`.
If the legend means *total*, the table above is dose-matched. If it means *per hemisphere*, then
Repudi's ≈61.5/70.5/57 should be compared with Obeid's 4E10 column (≈53/52/61) — **still higher
in cortex and hippocampus, slightly lower in cerebellum.** The direction survives both readings;
the magnitude does not.

⇒ **`CONFOUNDED`, not `SUPPORTED`.** The right quantity exists on both sides and the comparison is
blocked by a missing caption field.

---

## 3. 🔴 A finding that outranks the cross-study question: vg is non-linear *within* one study

Obeid Figure S3E, read at 300 dpi — densitometry relative to the `4 × 10¹⁰` WPRE-free arm (= 1):

| Arm | Cortex | Hippocampus | Midbrain | Cerebellum |
|---|---|---|---|---|
| AAV9-WWOX **4E10** (WPRE-free) | 1 | 1 | 1 | 1 |
| AAV9-WWOX **8E10** (WPRE-free) | **3.0** | **3.0** | **5.5** | **16.7** |
| AAV9-WWOX-WPRE **4E10** *(vs 8E10 = 1)* | **4.0** | **3.8** | **3.6** | **7.4** |

**Doubling the vg dose multiplies WWOX protein by 3 to 17×, and the multiplier is
region-dependent** — cerebellum 16.7× against cortex 3.0×.

And Figure S3F pairs **`KO+W-WPRE (6E10 vg)`** against **`KO+W (2.63E11 vg)`** — the paper itself
treats 6 × 10¹⁰ *with* WPRE as the comparator for 2.63 × 10¹¹ *without*, an implied **≈44-fold
dose-equivalence factor for a single regulatory element**.

⇒ **`vg` is not a linear proxy for anything.** It is non-linear in dose, non-uniform across
regions, and shifted ~44× by one cassette element. The cross-study discrepancy is a special case
of a within-study non-linearity, not a separate puzzle.

---

## 4. Answers in the operator's schema

**`TRANSFERABLE_QUANTITY_CANDIDATES`**
1. injected vg — **rejected**, §3
2. delivered vector genome copies per region — best in principle
3. WWOX **protein relative to wild type**, per region
4. WWOX mRNA relative to WT, per region
5. **% NeuN⁺WWOX⁺ transduced neurons**, per region

**`SUPPORTED`** — *(measured on a comparable scale by both studies)*
**None outright.** Candidate 5 is the only one both measure with the same assay and label.

**`NOT_MEASURED`**
- Candidate 2 — Repudi never assays vector genomes.
- Candidates 3 and 4 — Repudi shows WWOX IHC by region but **never quantifies it against WT**, and
  never measures mRNA.

**`CONFOUNDED`**
- Candidate 5 — by Obeid S3C's **unreported measurement age and n**, and by the per-hemisphere /
  total ambiguity in Repudi's own dose reporting.
- The survival endpoint itself — by follow-up duration (axis 6) and censoring (axis 7).

**`DECISIVE_MEASUREMENT`** — 🔴 **and it needs no new animals.**
> On banked tissue from both cohorts, run **one** protocol: regional **WWOX protein relative to
> wild type** by the same western, alongside **vector genome copies per diploid genome** by the
> same qPCR, on the **same regions at the same age**. Report transduction percentage **with its
> age and n**.
>
> **Protein-relative-to-WT is the quantity to standardise on**, not GC: it is on an absolute
> biological scale (WT = 1), it is the proximate cause of rescue, and Obeid already reports it in
> two figures. GC is one step further from the phenotype and is exactly where the 3–17×
> non-linearity of §3 enters.

---

## 5. Proposed canonical effect

1. **`CLAIM 011` (MODERATE).** Its LD/HD threshold must never be cited without its **vector
   configuration and follow-up window**. Add: *"expression per genome is non-linear in dose and
   region-dependent in this same study (3–17× for a 2× dose step), so the threshold is not a
   biological constant."*
2. **`CLAIM 004` (MODERATE).** Record the transduction percentages **with their age and n**
   (P19, n = 3) — they are the only quantity that could be compared with `PAPER 011`, and the
   comparison is currently blocked from the other side.
3. **Dismissal-ledger entry (strengthened).** *"A vg dose transfers between WWOX gene-therapy
   studies"* → ❌ **REJECTED**, now on a within-study ground as well as a between-study one.
   **`REVIVAL_TRIGGER`:** two studies reporting **regional WWOX protein relative to WT** at a
   matched age, agreeing on outcome at matched protein.
4. **`full_text_queue` note.** The missing S3C age/n is a **question for the authors**, not a
   reading debt — no further reading of this corpus can supply it.

---

## 6. What this does not claim

- **Not that Repudi's vector was better.** Different lots, unreported infectivity, and an
  unmatched measurement age are all live.
- **Not that transduction percentage explains the survival gap.** It is **directionally
  consistent and confounded**; consistency is not attribution.
- **Not that either study is wrong.** Both report what they measured. Neither set out to be
  comparable with the other, which is precisely the problem.

---

## Review required

None for queueing. §5.1–5.2 are MODERATE annotations that ride with
[`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md)'s operator review.
