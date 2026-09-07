# COMMIT CANDIDATE — the CLAIM 004 / CLAIM 011 dose contradiction, adjudicated at the vector map

**Candidate ID:** CC-20260826-DOSE-ADJUDICATION-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** figure-level adjudication of a named cross-claim contradiction
**Resolves:** §2 of [`CC-20260826-CROSS-CLAIM-CENSUS-01`](CC-20260826-CROSS-CLAIM-CENSUS-01.md),
which flagged this as `NEEDS_SCIENTIFIC_ADJUDICATION` pending one unread figure
**Change class:** 🔴 **MAJOR** — a `consolidated baseline` claim (`CLAIM 004`) and a
`flagged for review` claim (`CLAIM 011`) imply incompatible dose thresholds on the therapeutic
axis, and the discriminant that was expected to reconcile them **does not**
**Target WM:** current at BATCH_COMMIT time
**Batch gate:** intentionally untouched

---

## 0. The finding, and it is the opposite of what I predicted

[`CC-20260826-CROSS-CLAIM-CENSUS-01`](CC-20260826-CROSS-CLAIM-CENSUS-01.md) §2 proposed that the
contradiction would dissolve once Appendix Fig S1A of PMID 34747138 was read, because Obeid 2026
states that WPRE presence inverts the outcome at a fixed vg dose. The prediction was explicit:
if Repudi's vector carried WPRE, the two studies would be reconciled.

🔴 **Appendix Fig S1A, read at 300 dpi from the supplementary PDF, shows all three Repudi vectors
are WPRE-free.** The prediction is falsified, and the contradiction is not softened by the reading
— it is **sharpened**, because the discriminant is now excluded rather than merely unmeasured.

---

## 1. Adjudication recipe — reproducible, image not shipped (rule 5e)

| Item | Value |
|---|---|
| **Source** | `files/fulltext/figures/PMID34747138/EMMM-13-e14599-s001.pdf` (Appendix, 11 pp) |
| **source_pdf_sha256** | `1e5c30a903d96726cffae487e14f2e80593e4a6adf2e8b08efb70a5762f86cd2` |
| **Page** | 2 (Appendix Fig S1) |
| **Crop rect (PDF pt)** | full page `(0.00, 0.00, 510.00, 567.00)` |
| **dpi** | 300 → 2125 × 2363 px |
| **image_sha256** | `e362bdf80c8d850bb32859d20ff39d6264569f1332cb7455fdc649aac61f9c02` |

| Item | Value |
|---|---|
| **Source** | `files/fulltext/figures/PMID34747138/EMMM-13-e14599_article.pdf` |
| **source_pdf_sha256** | `32ee98733a6f45550f6b924b701734e111d171992ecba2535f0c32a5e105b438` |
| **Page / crop** | 4, rect `(400.00, 70.00, 545.00, 205.00)` pt — Figure 2C Kaplan-Meier |
| **dpi** | 600 → 1209 × 1126 px |
| **image_sha256** | `ac41ab21703026d593a30a18ced4dba09a038455df7528844e55956cdb3972fd` |

| Item | Value |
|---|---|
| **Source** | `files/fulltext/figures/PMID42422765/gr3.jpg` (Obeid Figure 3) |
| **source_sha256** | `c63f930cf5c558ae…` (as already declared in `deepdive_manifests/PMID42422765.json`) |
| **Crop box (source px)** | `(436, 0, 726, 297)` of 726 × 708, upscaled ×4.5 → 1305 × 1336 |
| **image_sha256** | `4c6f2fdd31867e96ce450eacdc4222e82ddb85a8e3624e85adbc66ddd586b996` |

⚠️ `gr3.jpg` is the **PMC CDN rendition at 726 px**, not a native-resolution original. It is
adequate for reading axis ticks, curve levels and legend `n`s, and is **not** adequate for
anything finer. Declared rather than glossed.

---

## 2. What the vector maps say

**Appendix Fig S1A** prints three constructs, left-to-right, each between flanking ITRs:

| Vector | Cassette as printed | WPRE |
|---|---|---|
| `AAV-mWwox` | `ITR │ hSynI │ mWwox │ IRES │ GFP │ polyA │ ITR` | **absent** |
| `AAV-hWWOX` | `ITR │ hSynI │ hWWOX │ polyA │ ITR` | **absent** |
| `AAV-GFP` | `ITR │ hSynI │ GFP │ polyA │ ITR` | **absent** |

**Obeid 2026 Figure 2A** prints two constructs: `AAV9 │ ITR │ Synapsin → WWOX │ ITR` and the same
with a yellow `WPRE` box appended after `WWOX`.

⇒ **Repudi's `AAV-hWWOX` and Obeid's WPRE-free `AAV9-hSynI-hWWOX` are the same architecture.**

---

## 3. The comparability audit — every discriminant I could name, checked

| Axis | Repudi 2021 (PMID 34747138) | Obeid 2026 (PMID 42422765) | Match |
|---|---|---|---|
| Laboratory | Aqeilan | Aqeilan | ✅ same |
| Serotype | AAV9 | AAV9 | ✅ |
| Promoter | hSynI | hSynI | ✅ |
| Transgene | hWWOX | hWWOX | ✅ |
| **WPRE** | **absent** (Appendix Fig S1A, pixels) | **absent** in the failing arm | ✅ |
| Route / age | ICV, P0–P1 | ICV, P0–P1 | ✅ |
| **Titration** | *"Viral titer was measured by qRT–PCR using bGH primers"* | *"Viral titers were determined by RT-qPCR using bGH primers"* | ✅ **same method, same primers** |
| **Background** | FVB | *"Mice were kept on an FVB (Friend leukemia Virus B) background"* | ✅ |
| Vector source | Vector Biolabs / HUJI Vector Core | Fujifilm / Vector Biolabs / BIB; HUJI ELSC Core | ◐ overlapping |
| Injection | **free-hand**, ~1 µL/hemisphere | **stereotactic** (Kopf frame, Micro-4 pump, 1–1.5 µL/min), 2.0 µL/hemisphere | ❌ **differs** |
| Dose | `2 × 10¹⁰` GC/hemisphere → **4 × 10¹⁰ total** (Methods); Fig 2A legend prints `AAV-hWWOX (2 × 10¹⁰)` | LD **1.23 × 10¹¹**, HD **2.63 × 10¹¹**; separate arm at **4 × 10¹⁰** and **8 × 10¹⁰** | ❌ |

⚠️ **Repudi's own dose is internally ambiguous.** Methods say per-hemisphere and *"the other
hemisphere was injected in the same way"*; the Figure 2A legend prints a bare `(2 × 10¹⁰)`. The
consistent reading is **4 × 10¹⁰ total**, but the paper does not say so in the legend, and the
alternative reading (2 × 10¹⁰ total) makes the contradiction **worse**, not better. Both readings
are recorded; neither is chosen silently.

---

## 4. The survival curves, read at pixel level

**Repudi Fig 2C** (600 dpi crop, recipe §1) — `KO+AAV-hWWOX (n = 16)`, green:
holds ≈93 % from ~90 d through ~270 d, then steps ≈78 % (~295 d) → ≈62 % (~318 d) → ≈15 %
(~322 d) → **0 % by ~330 d**. WT (n = 6) flat at 100 %. KO (n = 8) to 0 % by ~28 d.
`p < 0.0001`, log-rank.

**Obeid Fig 3B** (×4.5 crop, recipe §1):
- `WT+RI n=20` — 100 % → ≈90 % (~50 d) → ≈72 %, flat to 300 d. **Wild type itself is not 100 %.**
- `KO+RI n=10` — 0 % by ~18 d.
- **`KO+WWOX (LD) n=20` (1.23 × 10¹¹) — declines from ~20 d, reaches 0 % by ~80 d.**
- `KO+WWOX (HD) n=30` (2.63 × 10¹¹) — ≈78 % at ~85 d, flat to 300 d.

### The comparison, on a common endpoint

| Study | Dose (WPRE-free hSynI-hWWOX) | Survival ≈270–300 d |
|---|---|---|
| **Repudi 2021** | **2–4 × 10¹⁰** | **≈93 % at 270 d** |
| Obeid 2026 LD | 1.23 × 10¹¹ (**3–6× higher**) | **0 % — all dead by ~80 d** |
| Obeid 2026 HD | 2.63 × 10¹¹ | ≈78 % at 300 d |

🔴 **Repudi's three-to-sixfold LOWER dose of the same vector architecture, in the same strain,
titrated by the same method in the same laboratory, outperforms Obeid's LD by the entire width of
the experiment and is comparable to Obeid's HD.**

---

## 5. `VG_DOSE_ALONE_IS_NOT_TRANSFERABLE` — **SUPPORTED**, with the discriminant in hand

The operator's condition was: do not promote without the vector discriminant. It is now read, and
it **excludes** vector configuration as the explanation. The hypothesis survives on stronger
ground than the route originally proposed:

1. **Within Obeid 2026**, WPRE presence inverts survival at a fixed 4 × 10¹⁰ vg — vector
   configuration beats dose.
2. **Between Repudi and Obeid**, vector configuration is *matched* and dose is *inverted relative
   to outcome* — so dose does not determine outcome even at fixed configuration.

⇒ **A vg number is not a transferable quantity across studies.** Any inference of the form
*"a clinical WWOX dose must exceed ~10¹¹ vg"* reads a study-specific constant as a biological one.

**What is NOT concluded.** Not that either paper is wrong; not that Repudi's rescue is
unreliable; and **not** that the residual is explained. The unmatched axes are **injection
technique** (free-hand vs stereotactic), **volume** (1 vs 2 µL/hemisphere), and **vector lot/prep
year**. `PREMISE_TAG: INFERENZA` on any claim that delivery efficiency is the residual cause —
it is the leading candidate and **has not been measured**.

🔴 **The measurement that would settle it exists in Obeid 2026 and was never used for this.**
Obeid quantifies **vector genome copies in brain tissue at P30 by qPCR** (Figures 5A–5D). If
Repudi's brains were assayed the same way, the two studies could be compared on **delivered
genomes per brain** instead of on injected vg — the quantity that actually transfers. That is a
tissue-qPCR run on banked material, not a new animal study.

---

## 6. A second finding: Obeid 2026 contains an apparent internal dose inversion, and it is a follow-up artifact

Obeid reports that the WPRE-free vector at **8 × 10¹⁰ vg** produced *"improved outcomes, including
rescue of lethality"* (Fig 2B), while the same WPRE-free vector at **1.23 × 10¹¹ vg** — 1.5×
higher — produced only a *"modest"* extension ending in total mortality by ~80 d (Fig 3B).

🔴 **Read at pixels, Figure 2B's x-axis ends at 50 days.** The `8 × 10¹⁰` arm (n = 5, magenta)
is flat at 100 % to ~31 d; the `4 × 10¹⁰` arm (n = 3, yellow) falls to ≈33 % by ~20 d with one
animal censored at ~25 d; untreated KO reaches 0 % at ~19 d.

⇒ *"Rescue of lethality"* in Figure 2 means **"alive at about 31 days"**. In Figure 3, followed to
300 days, the same word means **"alive at 300 days"**. **`NOMENCLATURE_CONFLICT`, not a true
contradiction** — one word, two follow-up windows, inside one paper. Recorded because a reader
comparing the two figures without the axes will infer a dose inversion that the data do not show.

---

## 7. A third finding: Repudi Fig 2C's legend and its panel disagree

The legend states *"total n = 16, alive n = 6, spontaneously dead n = 6, 4 mice (shown in yellow)
were taken out for analysis"*. **The plotted green curve reaches 0 %.** A Kaplan-Meier with 6
animals alive cannot terminate at zero; censored animals hold the curve above it.

`EPISTEMIC_STATUS`: **`UNRESOLVED`.** Most likely the "alive" count was current at manuscript
writing while the curve was drawn later, or the censored animals were plotted as events. **Either
way the survival fraction at ~330 days cannot be taken from this panel at face value**, and the
`≈93 % at 270 d` figure used in §4 — which is read before any of the ambiguous terminal steps —
is the part that is safe to use.

---

## 8. Proposed canonical effect

- **`CLAIM 004` (MAJOR annotation).** Record the dose **with its vector configuration and its
  comparator**: `AAV9-hSynI-hWWOX`, **WPRE-free** (Appendix Fig S1A), `2 × 10¹⁰` GC/hemisphere
  (≈`4 × 10¹⁰` total), survival ≈93 % at 270 d then declining, `p < 0.0001` vs untreated. **Never
  the dose alone.**
- **`CLAIM 011` (MODERATE annotation, flag not lifted).** Its threshold *"between 1.23 and
  2.63 × 10¹¹ vg"* is a threshold **for this study's vector, prep and delivery**, and is
  contradicted at 3–6× lower dose by `PAPER 005`/`PAPER 063`'s own predecessor. The `REVIVAL_TRIGGER`
  already on the claim — an intermediate-dose arm — is **necessary but not sufficient**; it must
  also report delivered genome copies per brain.
- **New dismissal-ledger entry.** *"A vg dose measured in one WWOX gene-therapy study transfers to
  another"* → ❌ **REJECTED**. `REVIVAL_TRIGGER`: two studies reporting **delivered vector genome
  copies per brain region** by the same assay, agreeing on outcome at matched delivered dose.
- **No change to the direction of `CLAIM 004`'s rescue finding**, which is not in question.

---

## 9. Review required

🔴 **Operator authorization.** MAJOR: it qualifies a `consolidated baseline` claim's headline
quantity and contradicts a threshold currently used to reason about trial dosing. It also
**retracts a prediction this session published** in the census candidate, which is recorded here
rather than quietly amended.
