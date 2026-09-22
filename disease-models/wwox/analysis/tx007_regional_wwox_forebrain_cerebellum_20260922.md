# TX-007 — Regional WWOX after AAV9-hSynI-WWOX: forebrain versus cerebellum

**Actor:** Scientist U · **Date:** 2026-09-22 · **Axis:** regional expression, not delivery chain
**Scope:** `PMID 42422765` / `PMC13343157` (Obeid, Aqeilan et al. 2026, *Mol Ther Adv* 34(3):201791,
[DOI](https://doi.org/10.1016/j.omta.2026.201791)) and `PMID 34747138` / `PMC8649866`
(Repudi & Aqeilan 2021, *EMBO Mol Med* 13:e14599, [DOI](https://doi.org/10.15252/emmm.202114599)).
Full texts of both retrieved this session **according to PubMed**, from PubMed Central.

**Not medical advice.** Nothing here is a treatment recommendation.

> **Out of scope by instruction.** The TX-007 dose-unit audit is closed; `HD/LD = 2.1382` is not
> re-derived or re-opened here. The delivery chain (titre, volume, route, timing, survival) belongs
> to a sibling actor and is touched only where a regional value cannot be read without it.

---

## 0 · Evidence provenance — what I read myself, and what I did not

This section governs how every number below may be used. It is first because the hard bound
*"never relay a number you have not read yourself, with its locator"* cannot be satisfied uniformly
for this paper from this worktree.

| Surface | Status this session |
|---|---|
| `PMID 42422765` **body text + Methods** | ✅ **SELF-READ.** PMC full text, 48 780 chars, via the PubMed MCP route. Every quotation marked `surface: body` below was read by me today. |
| `PMID 34747138` **body text + Methods + all six main figure legends** | ✅ **SELF-READ.** The 2021 PMC extraction carries the Figure 1–6 legends inline; the 2026 extraction does **not** carry any legend. |
| `PMID 42422765` **figure panels and captions (Fig 1–7)** | 🔴 **NOT SELF-READ.** The figure images live under `files/`, which is gitignored and **absent from this worktree**. |
| `PMID 42422765` **supplement (S1–S8)** | 🔴 **NOT SELF-READ.** Same reason. |
| Network retrieval of panels | 🔴 **BLOCKED.** `www.ncbi.nlm.nih.gov` and `www.ebi.ac.uk` both return `CONNECT tunnel failed, 403`; proxy status confirms `connect_rejected` policy denials for `ftp.ncbi.nlm.nih.gov`, `api.openalex.org`, `web.archive.org`, `media.springernature.com`. Recorded once, not retried. **A tool block is not a scientific stop** — the panel values are therefore carried as repo-recorded attestations, clearly marked. |

**Consequence, and it is the central epistemic fact of this file.** Every *per-region fold-of-WT
number* in this paper lives in a **figure panel**, not in the running text. The running text gives
direction words only — *"most prominently in the cortex and to a lesser extent in the hippocampus,
midbrain, and cerebellum"*. So:

- numbers tagged **`SELF-READ`** were read by me today;
- numbers tagged **`REPO-ATTESTED`** were read from the panels by a prior LEGEND actor at a stated
  resolution and are cited to that actor's file. **They are not laundered into first-hand data.**
  Where a REPO-ATTESTED number carries a canonical conclusion, that is flagged.

🔴 **E-notation is used for every dose and every exponent throughout** (`1.23E11`, not `1.23 × 10¹¹`),
because the extraction trap is live and visible in my own retrieval: the PMC text returns
*"a dose of 4 × 10vg"* — the exponent silently deleted.

---

## 1 · Region inventory — assayed versus NOT ASSAYED

`NOT ASSAYED` below means **nobody sampled that region for that measurement**. It is never `NORMAL`
and never `ABSENT EXPRESSION`.

### 1.1 `PMID 42422765` (2026) — regions carrying a WWOX *expression* measurement

| Region | vDNA (qPCR) | mRNA (RT-qPCR) | Protein (immunoblot) | Protein/IF (IHC) | Timepoints | Locator |
|---|---|---|---|---|---|---|
| **Cortex** | ✅ | ✅ | ✅ | ✅ | P30; ~3 mo; P180; P240; P300 | Fig 5A, 5E, 5I; S5A–S5D, S5H–S5I; S5E–S5G; S5J–S5K; S6B–S6D |
| **Hippocampus** | ✅ | ✅ | ✅ | ✅ | same | Fig 5B, 5F, 5J; S5; S6 |
| **Midbrain** | ✅ | ✅ | ✅ | ✅ | same | Fig 5C, 5G, 5K; S5; S6 |
| **Cerebellum** | ✅ | ✅ | ✅ | ✅ | same | Fig 5D, 5H, 5L; S5; S6 |
| **Spinal cord** | ❌ NOT ASSAYED | ❌ NOT ASSAYED | ✅ (~3 mo, P240, P300) | ✅ | ~3 mo onward only | S6A; S6B–S6D |
| **Sciatic nerve (PNS)** | ❌ NOT ASSAYED | ❌ NOT ASSAYED | ✅ (HD only) | ✅ | unstated | S6E–S6G |
| **Liver** | ❌ | ❌ | ✅ **negative** | ✅ **negative** | LD and HD | S6H, S6I |

**SELF-READ, `surface: body`, Results:**
> "Analysis of the cortex, hippocampus, midbrain, and cerebellum revealed a clear dose-dependent pattern, with higher vDNA levels in HD-treated mice than LD-treated mice across regions, with statistical significance in the hippocampus"

> "widespread, stable expression was maintained at P240 and P300 throughout the cortex, hippocampus, midbrain, cerebellum, and spinal cord following a single neonatal injection"

> "WWOX protein was also detected in the sciatic nerve of HD-treated mice ... In contrast, no WWOX expression was detected in the liver following either LD or HD treatment"

### 1.2 🔴 Regions NOT ASSAYED for WWOX expression in the 2026 paper — named

These are named because three of them are quantified for a *different* endpoint in the same paper,
which makes their absence from the expression series a choice rather than an oversight:

| Region | Assayed for | NOT assayed for | Locator of the endpoint it *does* carry |
|---|---|---|---|
| **Corpus callosum** | MBP myelin (WT vs KO only) | 🔴 **WWOX expression — NOT ASSAYED** | Fig 6D, 6E |
| **Striatum** | MBP myelin (WT vs KO only) | 🔴 **WWOX expression — NOT ASSAYED** | Fig 6E |
| **Anterior commissure** | MBP myelin (WT vs KO only) | 🔴 **WWOX expression — NOT ASSAYED** | Fig 6E |
| **Thalamus** | — | 🔴 **NOT ASSAYED at all** | — |
| **Brainstem / pons / medulla** | — | 🔴 **NOT ASSAYED at all** | — |
| **Hypothalamus** | — | 🔴 **NOT ASSAYED at all** | — (notable: the paper's central phenotype is hypoglycaemia) |
| **Olfactory bulb, amygdala, basal ganglia** | — | 🔴 **NOT ASSAYED at all** | — |
| **Cerebellar sub-structure** (Purkinje layer, granular layer, molecular layer, vermis vs hemisphere, lobules) | — | 🔴 **NOT ASSAYED.** Cerebellum is treated throughout as **one homogenised compartment** | — |
| **DRG** | AAV infection *in vitro* (E13.5 culture) | 🔴 not an *in vivo* biodistribution measurement | Methods, "DRG culture" |

🔴 **The cerebellar sub-structure gap is the largest single `NOT ASSAYED` on this axis.** The
cerebellum is dissected, homogenised and blotted. Purkinje cells — the cell type whose loss defines
cerebellar ataxia, and which are a tiny minority of cerebellar cells by number — are **never
resolved**. A whole-cerebellum blot is dominated by granule neurons. **Whatever the cerebellar
number turns out to be, it does not describe Purkinje cells, and must never be cited as if it did.**

### 1.3 `PMID 34747138` (2021) — a much smaller region inventory

| Region | Method | Measurement | Timepoint | n | Locator |
|---|---|---|---|---|---|
| **Cortex** | IF (NeuN + WWOX) | **% double-positive cells** — *not* fold-WT | P17 (mWwox), P19 (hWWOX) | n=3 mice, 3 sagittal sections each | Fig 1D–1E; Fig 2D, 2G |
| **Hippocampus** | IF | % double-positive | P19 | n=3 | Fig 2E, 2G |
| **Cerebellum** | IF | % double-positive | P19 | n=3 | Fig 2F, 2G |
| Corpus callosum | EM, CC1/PDGFRα IF | myelinated axons, g-ratio, OPC counts | P17, 6 mo | n=3 | Fig 4B–4C, Fig 5A–5F |
| Optic nerve | EM | myelinated axons, g-ratio | P17 | n=3 | Fig 5G–5I |
| Liver, pancreas, kidney, testis, ovary | IHC | **negative** | P17, 9 mo | — | Appendix |

🔴 **NOT ASSAYED in 2021:** midbrain, spinal cord, sciatic nerve, striatum, thalamus, brainstem,
hypothalamus — and, decisively for this axis, **WWOX protein as a fold of wild type in any region,
by any method.** 2021 has no regional Western blot at all.

**SELF-READ, `surface: body`, 2021 Results:**
> "Specific neuronal WWOX expression was detected in cortex (Figs 1D and 2D), hippocampus (Fig 2E), and cerebellum (Fig 2F) of P17-P19-treated mice. The percentage of NeuN and WWOX double-positive cells was calculated and found to range between 60 and 70% (Figs 1E and 2G)."

🔴 **The repo's "60–70% of neurons transduced" is a range spanning three regions, not a per-region
value.** Read in the source, "60 and 70%" is the **envelope over cortex + hippocampus + cerebellum
across two figures**. Any use of it as a single regional number is an over-read, and any use of it
as a cortical number is unsupported. Per-region values exist **only inside the Fig 1E / 2G bar
panels**, which I could not reach.

---

## 2 · Regional expression table

**Do not average these rows.** Each is one region, one arm, one timepoint. No whole-brain figure is
offered, because none of the panels is a whole-brain measurement.

### 2.1 `PMID 42422765` — dose arm (WPRE-FREE vector), P30

Vector: **AAV9-hSynI-hWWOX, no WPRE**. LD = `1.23E11 vg`, HD = `2.63E11 vg`, neonatal ICV.

| Region | Arm | T | mRNA (fold-WT) | Protein (fold-WT) | vDNA | Method | n | Locator | Status |
|---|---|---|---|---|---|---|---|---|---|
| Cortex | LD | P30 | ≈520 | 🔴 **no lane values recorded** | ≈2 800 | RT-qPCR / WB / qPCR | not stated in text | Fig 5E, 5I, 5A | **REPO-ATTESTED** (mRNA, vDNA) · **ABSENT** (protein lanes) |
| Cortex | HD | P30 | ≈700 · `ns` vs LD | 🔴 **no lane values recorded** | ≈8 800 · `ns` | same | — | Fig 5E, 5I, 5A | same |
| Hippocampus | LD | P30 | ≈540 | **14.2 / 19.5 / 9.2** | ≈2 000 | same | 3 lanes | Fig 5F, **5J**, 5B | **REPO-ATTESTED** |
| Hippocampus | HD | P30 | ≈650 · `ns` | **14.7 / 9.1 / 18.3** | ≈3 800 · **`*`** | same | 3 lanes | Fig 5F, **5J**, 5B | **REPO-ATTESTED** |
| Midbrain | LD | P30 | ≈65 | 🔴 **no lane values recorded** | ≈2 200 | same | — | Fig 5G, 5K, 5C | **ABSENT** (protein) |
| Midbrain | HD | P30 | ≈145 · `ns` (caption: *p = 0.08*) | 🔴 **no lane values recorded** | ≈7 300 · `ns` | same | — | Fig 5G, 5K, 5C | same |
| 🎯 **Cerebellum** | **LD** | **P30** | ≈37 | **0.7 / 0.5 / 0.7** | ≈320 | same | 3 lanes | Fig 5H, **5L**, 5D | **REPO-ATTESTED** |
| 🎯 **Cerebellum** | **HD** | **P30** | ≈95 · `ns` (caption: *p = 0.06*) | **0.7 / 0.5 / 0.2** | ≈730 · `ns` | same | 3 lanes | Fig 5H, **5L**, 5D | **REPO-ATTESTED** |
| *(KO control lanes)* | KO | P30 | — | cortex **0.02** · hippocampus **1.1** · midbrain **0.03** · cerebellum **0.08** | — | WB | — | Fig 5I–5L | **REPO-ATTESTED** |

⚠️ **The hippocampal KO lane reads `1.1` — wild-type intensity in a `Wwox`-null animal.** Flagged in
the repo dossier and **not flagged by the authors**. It is most consistent with a non-specific band
or a normalisation artefact on that blot. 🔴 **The hippocampal fold-WT values in Fig 5J therefore
carry an unresolved internal control failure and must not be quoted as a clean 9–19×.** This is the
one place where the forebrain side of the Operator's contrast is weaker than it looks.

⚠️ **Caption vocabulary boundary, REPO-ATTESTED from the Fig 5 caption:** *"in G and H it is near
significant, p value = 0.08 and 0.06, respectively"*. **"Near significant" is not a result class.**
Midbrain and cerebellar mRNA LD-vs-HD are `ns`, carried with their p-values beside them.

🔴 **Seven of eight LD-vs-HD comparisons in Figure 5 are `ns`** — the exception is hippocampal vDNA.
So the 2.14-fold dose separation is **statistically undetectable** in what arrives and what is
transcribed, in all four regions.

### 2.2 `PMID 42422765` — long-term, HD only, **SURVIVOR-SELECTED**

⚠️ **These rows describe the animals that lived.** The repo records that S5 explicitly marks one HD
and three LD animals as dead, and that every later expression comparison is made among survivors.
They do **not** describe the treated cohort.

| Region | Arm | T | Protein (fold-WT) | Method | Locator | Status |
|---|---|---|---|---|---|---|
| Cortex | HD | P300 | **8.2×** | WB | S5J | **REPO-ATTESTED** |
| Hippocampus | HD | P300 | **10.7×** | WB | S5J | **REPO-ATTESTED** |
| Midbrain | HD | P300 | **5.6×** | WB | S5J | **REPO-ATTESTED** |
| 🎯 **Cerebellum** | **HD** | **P300** | **1.4×** | WB | S5J | **REPO-ATTESTED** |
| Cortex | HD | P300 (2nd panel) | **4.6×** | WB | S5K / S6 | **REPO-ATTESTED** |
| Hippocampus | HD | P300 (2nd panel) | **4.7×** | WB | S5K / S6 | **REPO-ATTESTED** |
| Midbrain | HD | P300 (2nd panel) | **3.1×** | WB | S5K / S6 | **REPO-ATTESTED** |
| 🎯 **Cerebellum** | **HD** | **P300 (2nd panel)** | **0.6×** | WB | S5K / S6 | **REPO-ATTESTED** |
| 🎯 **Cerebellum** | HD | long-term | **0** *(printed)* | — | **S6D** | **REPO-ATTESTED** |
| Spinal cord | HD | ~3 mo, P240, P300 | present, not quantified vs WT in any record here | WB / IHC | S6A–S6D | **ABSENT** (no fold value) |
| Sciatic nerve | HD | unstated | detected, **not quantified** | WB / IHC | S6E–S6G | **ABSENT** |
| Liver | LD and HD | unstated | **not detected** | WB / IHC | S6H, S6I | **STATED (negative)**, SELF-READ in text |

### 2.3 `PMID 42422765` — WPRE comparison arm, low doses (a **different experiment**)

Vector: AAV9-hSynI-hWWOX **± WPRE**, at `2E10` and `4E10 vg`. Protein relative to WT = 1.
**REPO-ATTESTED** from the Fig 2E panel.

| Construct | Dose | Cortex | Hippocampus | Midbrain | 🎯 Cerebellum |
|---|---|---|---|---|---|
| WWOX, **no** WPRE | `2E10` | 0.8 | 0.9 | 0.3 | **0.1** |
| WWOX, **no** WPRE | `4E10` | 4.7 | 5.9 | 1.5 | **0.4** |
| WWOX **+ WPRE** | `2E10` | 11.6 | 11.9 | 4.0 | **2.4** |
| WWOX **+ WPRE** | `4E10` | 25.6 | 22.3 | 11.6 | **6.2** |

**DERIVED — WPRE multiplier per region, arithmetic shown** (+WPRE ÷ no-WPRE, same dose):

| Dose | Cortex | Hippocampus | Midbrain | 🎯 Cerebellum |
|---|---|---|---|---|
| `2E10` | 11.6 ÷ 0.8 = **14.5×** | 11.9 ÷ 0.9 = **13.2×** | 4.0 ÷ 0.3 = **13.3×** | 2.4 ÷ 0.1 = **24.0×** |
| `4E10` | 25.6 ÷ 4.7 = **5.4×** | 22.3 ÷ 5.9 = **3.8×** | 11.6 ÷ 1.5 = **7.7×** | 6.2 ÷ 0.4 = **15.5×** |

🔴 **Two things fall out and both are on this axis.** (1) In **every one of the eight cells** the
cerebellum is the lowest region. (2) The cerebellum has the **largest WPRE multiplier** of the four
regions at both doses — the element that was removed is the one that most helped the region that is
most under-expressed. The cerebellum is the only region that **never reaches WT without WPRE** at
either of these doses.

### 2.4 `PMID 34747138` (2021) — reported separately, and it cannot be merged

🔴 **No fold-of-WT value exists in the 2021 paper for any region.** The only regional quantity is
percent NeuN⁺WWOX⁺, and the per-region bars were unreachable. Dose `2E10` GC per hemisphere,
both hemispheres injected = `4E10` GC total, stated twice in the source (SELF-READ, Results and
Methods). Vector: `AAV9-hSynI-mWwox-IRES-EGFP` or `AAV9-hSynI-hWWOX`.

| Region | mRNA fold-WT | Protein fold-WT | % NeuN⁺WWOX⁺ | Locator | Status |
|---|---|---|---|---|---|
| Cortex | 🔴 **ABSENT — never measured** | 🔴 **ABSENT — never measured** | within 60–70% envelope; bar ≈61.5% | Fig 2G | **REPO-ATTESTED** (bar) |
| Hippocampus | 🔴 **ABSENT** | 🔴 **ABSENT** | bar ≈70.5% | Fig 2G | **REPO-ATTESTED** |
| 🎯 Cerebellum | 🔴 **ABSENT** | 🔴 **ABSENT** | bar ≈57% | Fig 2G | **REPO-ATTESTED** |
| Everything else | 🔴 **NOT ASSAYED** | 🔴 **NOT ASSAYED** | 🔴 **NOT ASSAYED** | — | — |

⚠️ **No value crosses between §2.4 and §2.1–2.3.** Different vectors (2021 has no WPRE arm and an
IRES-EGFP variant), different doses (`4E10` total vs `1.23E11`/`2.63E11`), different endpoints
(IF % vs Western fold-WT), different ages (P17–P19 vs P30–P300), different animals.

---

## 3 · 🎯 The cerebellum question, answered directly

### 3.1 The answer

**The cerebellum WAS assayed** — in both papers, in every 2026 expression modality (vDNA, mRNA,
protein, IHC) and at every 2026 timepoint. It is **not** a `NOT ASSAYED` region. So the loud
alternative does not apply, and the question has real numbers behind it.

**And on those numbers the Operator's hypothesis holds, in the direction stated.**

| | Cerebellum | Forebrain / other |
|---|---|---|
| **P30, LD** (`1.23E11`) | **0.7 / 0.5 / 0.7 × WT** | hippocampus 14.2 / 19.5 / 9.2 |
| **P30, HD** (`2.63E11`) | **0.7 / 0.5 / 0.2 × WT** | hippocampus 14.7 / 9.1 / 18.3 |
| **P300, HD** (survivor-selected) | **1.4 × WT** | cortex **8.2×**, hippocampus **10.7×**, midbrain **5.6×** |
| **P300, HD, 2nd panel** | **0.6 × WT** | cortex **4.6×**, hippocampus **4.7×**, midbrain **3.1×** |
| **S6D, long-term** | **0** printed | — |
| **No WPRE, `2E10` / `4E10`** | **0.1× / 0.4× WT** | cortex 0.8 / 4.7, hippocampus 0.9 / 5.9 |
| **+WPRE, `2E10` / `4E10`** | 2.4× / 6.2× | cortex 11.6 / 25.6, hippocampus 11.9 / 22.3 |

**Stated as a finding:** across **every WPRE-free arm at every dose and every timepoint that was
measured**, cerebellar WWOX protein sits between **0.1× and 1.4× of wild type**, while cortex,
hippocampus and midbrain in the same animals sit at **3.1× to 10.7×** at P300 and, on the
hippocampal blot, **9–19×** at P30. The Operator's *"5–11× WT elsewhere, cerebellum near or below
WT"* is a fair reading of the P300 panel (`5.6–10.7×` forebrain/midbrain against `1.4×` cerebellum)
and an understatement of the P30 hippocampal panel.

**Tag: `DATO` on the P30 Fig 5L cerebellar values and on the P300 S5J series, `REPO-ATTESTED`.**
**Tag: `INFERENZA` on the phrase "the cerebellum is not reconstituted"** — see the four
qualifications below, each of which weakens the inference without touching the numbers.

### 3.2 Four qualifications that must travel with the answer

1. 🔴 **Fold-of-WT is a ratio, and the denominator was never reported.** A low cerebellar fold-WT
   is equally consistent with *little transgene protein* and with *high endogenous wild-type WWOX in
   cerebellum*. The paper reports **no absolute regional WWOX level in wild-type brain**, in either
   paper, by any method. `PREMISE_TAG` — **"the cerebellum is under-expressed" is not separable from
   "the cerebellum has a larger WT denominator" with anything in these two papers.** This is the
   single most important unmeasured quantity on this axis and it is cheap to measure.

2. 🔴 **Whole-cerebellum homogenate cannot speak about Purkinje cells** (§1.2). Granule neurons
   dominate the blot by orders of magnitude in cell number.

3. ⚠️ **The forebrain comparator has a control failure.** The hippocampal KO lane reads `1.1` where
   the other three regions read `0.02–0.08`. The 9–19× hippocampal figure inherits that.

4. ⚠️ **Every P240/P300 row is survivor-selected**, and the dose arm's own explanation for its
   expression/survival mismatch — *"mice from either treatment group that failed to survive
   exhibited reduced WWOX expression"* (SELF-READ, `surface: body`, Results) — is itself a
   **post-hoc comparison of survivors against non-survivors**, i.e. selection-conditioned, and rests
   on S5A–S5D.

### 3.3 🔴 The dose does not raise the cerebellum

Worth isolating, because it is the datum most directly relevant to a coverage account. At P30 the
HD cerebellar lanes (`0.7 / 0.5 / 0.2`) are **not above** the LD lanes (`0.7 / 0.5 / 0.7`); the
lowest single value in the whole series belongs to the **high** dose. A 2.14-fold dose increase
produced **no upward movement in cerebellar protein at all**, while cerebellar vDNA means rose
≈320 → ≈730 (`ns`) and cerebellar mRNA means rose ≈37 → ≈95 (`ns`, caption *p = 0.06*).

⇒ **In the cerebellum, more vector genomes and more transcript did not become more protein.**
That dissociation is not commented on in the running text, which says only *"a trend toward higher
expression in HD-treated mice compared with LD-treated mice"* (SELF-READ).

---

## 4 · Transduction efficiency per region and per cell type — kept separate from expression level

**This is a different quantity from §2 and the two point in opposite directions.**

| Paper | Region | % transduced | Cell type | Method | Dose | Age | n | Locator | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | Cortex | ≈61.5% | NeuN⁺ neurons | IF co-stain | `4E10` total | P19 | 3 mice, 3 sagittal sections each | Fig 2G | **REPO-ATTESTED** (bar); envelope 60–70% **SELF-READ** |
| 2021 | Hippocampus | ≈70.5% | NeuN⁺ | IF | `4E10` | P19 | 3 | Fig 2G | same |
| 2021 | 🎯 **Cerebellum** | **≈57%** | NeuN⁺ | IF | `4E10` | P19 | 3 | Fig 2G | same |
| 2021 | all brain | — | **oligodendrocytes: WWOX NOT detected** | CC1 + WWOX co-stain | `4E10` | P17 | 3 | Appendix | **SELF-READ** (text) |
| 2026 | Cortex | ≈53% `*` | NeuN⁺ | IF | `4E10` | 🔴 **unstated** | 🔴 **unstated** | **S3C** | **REPO-ATTESTED** |
| 2026 | Hippocampus | ≈52% `ns (0.07)` | NeuN⁺ | IF | `4E10` | unstated | unstated | **S3C** | **REPO-ATTESTED** |
| 2026 | 🎯 **Cerebellum** | **≈61% `ns`** | NeuN⁺ | IF | `4E10` | unstated | unstated | **S3C** | **REPO-ATTESTED** |
| 2026 | any region | 🔴 **NOT ASSAYED at LD or HD** | — | — | `1.23E11` / `2.63E11` | — | — | — | 🔴 **the decisive gap — §7** |

**SELF-READ, `surface: body`, 2026 Results:**
> "quantification of WWOX immunohistochemical staining showed a significant increase in WWOX-positive NeuN neurons, rising from ∼40% to ∼55%–60% following treatment (p < 0.05)"

⚠️ **Note that the 2026 sentence gives no region.** The ∼40% → ∼55–60% figure is the S3C aggregate
in the **WPRE-comparison arm at `4E10`**, not the dose arm.

🔴 **The finding of this section, and it cuts against a simple coverage story.** In the 2026 paper
the **cerebellum has the HIGHEST percentage of transduced neurons of the three regions measured**
(≈61%, against ≈53% cortex and ≈52% hippocampus), and in the 2021 paper it has the lowest but is
still within a few points of the others (≈57% against ≈61.5% and ≈70.5%). **Cerebellar neurons are
being reached.** The cerebellar deficit is therefore **not, on this evidence, a failure to transduce
cerebellar neurons at all** — it sits either in per-cell output, or in the vDNA load per gram of
tissue (cerebellum ≈320–730 against cortex ≈2 800–8 800 — an ≈9–12× separation), or in the
unreported WT denominator of §3.2.1.

⚠️ Two caveats on the ≈61% figure that prevent it doing more work than it can. **S3C's measurement
age and n are stated nowhere** in the paper (repo-recorded as an author question, unanswerable by
further reading), and S3C is at `4E10`, a dose **13–21× below** the dose arm. It is not a
measurement of the LD/HD animals.

### 4.1 Oligodendrocytes

**SELF-READ, 2021 Results:**
> "WWOX expression was lacking in non-neuronal cells of the brain such as oligodendrocytes of KO mice injected with either AAV-mWwox or AAV-hWWOX"

2026 tested oligodendrocyte targeting directly with an **MBP-driven** vector at `4E10` and it failed
on every readout; the panel-level reason is recorded in the repo as **Fig 1M showing essentially
blank WWOX immunofluorescence in the MBP column (cortex only)**. The authors' own hedge, SELF-READ:
> "may reflect the limited oligodendrocyte tropism of AAV9 following neonatal ICV administration rather than a lack of relevance for oligodendrocyte WWOX expression"

⇒ **`NOT TRANSDUCED` for oligodendrocytes, in both papers.** This is a transduction fact, not a
biology fact, and the oligodendrocyte-autonomous question stays open.
🔴 **Astrocytes, microglia and cerebellar Purkinje cells were never co-stained for transduction in
either paper.** `NOT ASSAYED`.

---

## 5 · The WPRE confound — which experiments carry it

### 5.1 Construct-by-experiment map

**SELF-READ, `surface: body`, 2026 Methods, "Plasmid vectors" — this settles it:**
> "Constructs driven by EF1α, CMV, and MBP included WPRE, whereas the hSynI-driven vector was generated both with and without WPRE."

| Figure / experiment | Construct | WPRE | Doses | Status |
|---|---|---|---|---|
| **Fig 1** — four-promoter comparison | EF1α / CMV / MBP / hSynI | 🔴 **ALL carry WPRE** | `4E10` | **SELF-READ** (Methods) + REPO-ATTESTED (Fig 1 caption names all four as `-WPRE` constructs at `4E10`) |
| **Fig 2 + S3** — WPRE comparison | hSynI ± WPRE | **both arms present** | `2E10`, `4E10`, `8E10` | **SELF-READ** (text) |
| **Fig 3** — dose-response / survival | hSynI | 🔴 **WPRE-FREE** | `1.23E11` LD, `2.63E11` HD | **SELF-READ** |
| **Fig 4** — behaviour | hSynI | **WPRE-FREE** | HD only | **SELF-READ** (same arm) |
| **Fig 5** — regional DNA/mRNA/protein | hSynI | **WPRE-FREE** | LD, HD | **SELF-READ** |
| **Fig 6 + S7** — myelin, gliosis | hSynI | **WPRE-FREE** | LD, HD | **SELF-READ** |
| **Fig 7** — ECoG | hSynI | **WPRE-FREE** | HD | **SELF-READ** |
| **S8** — P1–P5 timing window | hSynI | **WPRE-FREE** | HD | REPO-ATTESTED |
| **2021 paper, all figures** | hSynI-mWwox-IRES-EGFP / hSynI-hWWOX | 🔴 **WPRE is never mentioned anywhere in the 2021 paper** — not in Methods, not in Results, not in any legend | `2E10`/hemisphere | **SELF-READ (absence)** |

**SELF-READ, 2026 Results, the design rationale:**
> "we generated AAV9-hSynI-WWOX vectors lacking the WPRE element to achieve tighter control of transgene expression and to proactively optimize the safety margin for clinical translation"

> "Taken together, these findings imply that removal of WPRE is associated with a more controlled neuronal WWOX expression profile ... However, this reduction in expression necessitates the use of higher vector doses to achieve comparable therapeutic outcomes."

### 5.2 Is any cross-arm comparison confounded by WPRE?

**No, within the dose arm — and yes, across figures.**

- ✅ **Fig 3–7 are internally clean.** LD versus HD is WPRE-free on both sides. **The regional
  cerebellum-versus-forebrain contrast of §3 is NOT confounded by WPRE**, because both sides of it
  come from the same WPRE-free blots.
- ✅ **Fig 1's promoter ranking is internally clean** — all four promoters carry WPRE at the same
  `4E10`. The authors' own declared limitation is a different one, SELF-READ:
  > "vector genome copy number, transcript abundance, or protein levels were not systematically quantified across all constructs"
  ⚠️ and that limitation **scopes to the promoter arm**, not to Fig 5. Reading it as global would
  falsely mark the regional data unmeasured.
- 🔴 **Any comparison that carries a bare `4E10` from Fig 1 or Fig 2 into Fig 3's dose axis IS
  confounded.** `4E10` with WPRE and `4E10` without it are separated by **3.8× to 24×** in protein
  (§2.3 arithmetic). The repo dossier records a prior actor making exactly this error and correcting
  it. **The label `4E10` is not one quantity in this paper.**

### 5.3 The review-versus-supplement contradiction — **RESOLVED, and it was never a contradiction**

The repo (`discovery_ledger_current.md` DL-MECH-009, `working_model_current.md`,
`paper_registry_current.md` PAPER 029, `disease_model.md`) records a flagged contradiction: the
Obeid 2026 *Neurobiol Dis* **review** summarises the design as *"WPRE removed to avoid
overexpression"*, while the primary's supplement shows WPRE **present** and raising expression.

**It resolves cleanly against the primary's own words, SELF-READ this session, `surface: body`,
Discussion:**
> "Although no overt toxicity was observed in prior studies, we removed WPRE as a proactive risk-mitigation step to improve the predictability and control of neuronal WWOX expression for potential clinical translation."

⇒ **The review's summary is a correct description of the FINAL therapeutic construct.** The
supplement's WPRE data describe an **earlier arm that was run in order to justify removing it**.
The two statements are about different constructs and both are true:

- **WPRE is present** in the four-promoter screen (Fig 1) and in one arm of Fig 2/S3 — experiments
  whose purpose was to characterise the element.
- **WPRE is absent** from every experiment that produces the paper's therapeutic result: the
  dose-response, survival, behaviour, regional expression, myelin, gliosis and ECoG (Fig 3–7, S5–S8).

🔴 **Recommended repo correction:** DL-MECH-009's `⚠️ contraddizione da segnalare` should be
downgraded from *contradiction* to **scope difference**, with the mapping above. Nothing in the
primary contradicts the review. **This is a scope error in LEGEND's own record, not an error in the
literature.** I have not edited any registry; this is recorded as a finding for the orchestrator.

### 5.4 🔴 BUT a real, unresolved contradiction is exposed — inside LEGEND, about the `3–16.7×`

The task brief, and `DL-MECH-009`, record `3–16.7×` as the **WPRE** effect per region. A second repo
file attributes **the identical four numbers to a different comparison entirely.**

| Repo file | The `3.0 / 3.0 / 5.5 / 16.7` numbers are attributed to | Locator cited |
|---|---|---|
| `research/discovery_ledger_current.md` L196 (DL-MECH-009) | **the WPRE effect** — *"WPRE aumenta WWOX 3–16.7×/regione"*, cortex 3.0, hippocampus 3.0, midbrain 5.5, **cerebellum 16.7** | **S3E** |
| `research/commit_candidates/CC-20260826-DOSE-DECISION-TABLE-01.md` §4 | **the dose effect in the WPRE-FREE arm** — densitometry relative to the `4E10` WPRE-free arm = 1, with `8E10` WPRE-free reading 3.0 / 3.0 / 5.5 / **16.7**; concluding *"Doubling vg multiplies WWOX protein by 3–17×"* | **S3E** |

**These cannot both be right.** One says the number measures `+WPRE ÷ −WPRE` at fixed dose; the
other says it measures `8E10 ÷ 4E10` at fixed (absent) WPRE. They propagate to opposite design
conclusions — *"WPRE is a dose-sparing booster"* versus *"vg is wildly non-linear"*.

**Why it is not resolvable from here.** The running text describes **both** comparisons in the same
sentence pair and cites the same panel range for both (SELF-READ):
> "immunohistochemical and immunoblot analyses of WWOX expression confirmed a dose-dependent increase, with low expression observed at 4 × 10vg in the absence of WPRE and markedly higher levels at 8 × 10vg. Notably, inclusion of WPRE at 4 × 10vg resulted in substantially higher expression (S3D–S3E)."

⚠️ **Quoted exactly as my retrieval returned it — the exponents are DAMAGED, not missing from the
paper.** `4 × 10vg` is the extractor eating `10^10`. In E-notation the sentence reads: `4E10`
WPRE-free < `8E10` WPRE-free, and `4E10` +WPRE higher than both. **The damage is shown rather than
silently repaired, because it is the live form of the exponent trap.**

So S3D–S3E genuinely contains both comparisons, and the text does not partition them by panel.
🔴 **Recorded UNRESOLVED.** What resolves it: **reading the S3E caption and axis label** in
`mmc1.pdf` / `mmc2.pdf` — a five-minute job for any actor whose worktree has `files/`, which mine
does not. Until then, **`3–16.7×` must not be cited as a WPRE effect without that check**, and the
independent WPRE multipliers derived in §2.3 from Fig 2E (`3.8×` to `24×`, cerebellum highest)
should be preferred because their construct labels are unambiguous.

⚠️ Note that the two readings agree on one thing that matters here: **the cerebellum carries the
largest multiplier of the four regions**, whichever variable is being multiplied.

---

## 6 · Anatomical expectation for neonatal ICV delivery to cerebellum

### 6.1 What this paper MEASURES about delivery geometry — `DATO`

**SELF-READ, `surface: body`, 2026 Methods, "ICV injection of AAV particles into P0-P5 null mice":**
> "The injection site was targeted at ±0.8 mm, 1.5 mm, and −1.6 mm, relative to lambda. These anatomical landmarks were visible through the skin at P0-P1. For older pups, the coordinates were adjusted to account for developmental changes; for P5 pups, the injection site was targeted at ±1.0 mm, 1.0 mm, and −2.0 mm."

> "delivering 2.0 μL/hemisphere through a Hamilton syringe with a 32G needle ... The procedure was repeated for the contralateral hemisphere."

> "ICV injections ... were conducted using stereotactic technique to ensure consistency"

**And the one delivery-geometry outcome the paper actually measures per region** (Fig 5A–5D,
REPO-ATTESTED): cerebellar vDNA ≈320 (LD) and ≈730 (HD), against cortical ≈2 800 and ≈8 800 —
an ≈**8.8–12×** lower vector-genome load in cerebellum than cortex in the same animals, `ns` on the
dose comparison.

⇒ **The paper measures a large regional gradient in delivered vector genomes, with the cerebellum at
the bottom.** That is this paper's evidence. It does not attribute the gradient to any cause.

### 6.2 Background expectation — 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK`, NOT this paper's evidence

Everything in this subsection is general knowledge about neonatal ICV AAV delivery. **None of it is
tested, stated or cited in either paper.** It is set out so that a later reader can see what is
expectation and what is measurement, and it must never be quoted as a result of `PMID 42422765`.

1. **Distance and CSF route.** The injection targets the **lateral ventricles**. Vector reaching the
   cerebellum must travel caudally through the third ventricle, cerebral aqueduct and fourth
   ventricle, or via subarachnoid CSF. Forebrain structures abutting the lateral ventricles
   (cortex, hippocampus, striatum) are exposed first and at higher local concentration.
2. **Cerebellar neurogenesis timing.** In mouse, cerebellar granule-cell precursors in the external
   granular layer proliferate intensely through roughly P0–P14. AAV genomes are **episomal** and are
   **diluted by cell division**. A vector delivered at P0–P5 is therefore lost from exactly the
   population that will become the numerical majority of the cerebellum — a dilution the forebrain,
   whose principal neurons are largely post-mitotic by birth, does not suffer to the same degree.
3. **Promoter timing.** hSynI is a **mature-neuron** promoter. Cerebellar granule neurons mature
   later than forebrain projection neurons, so promoter activity is expected to lag in cerebellum at
   any early assay point.
4. **Denominator.** If endogenous WWOX is regionally non-uniform, a fold-of-WT readout is
   regionally non-comparable. Neither paper reports it (§3.2.1).

**Each of 1–3 predicts lower cerebellar transgene DNA and protein, and 1 and 2 are consistent with
the ≈9–12× vDNA gradient the paper does measure.** ⚠️ **But none of them is a demonstration**, and
one measurement in the paper sits awkwardly with a pure coverage story: **§4's ≈61% cerebellar
NeuN⁺WWOX⁺, the highest of three regions.** A cerebellum that is poorly reached should not show the
highest transduced fraction. Either the fraction and the load are measuring different things (they
are: fraction of cells positive versus genomes per unit tissue, in a region with far higher cell
density), or S3C's unstated age and n make it not comparable, or per-cell output is the binding
constraint. **This cannot be settled from these two papers.**

---

## 7 · Does a regional-coverage account of the apparent non-monotonicity survive? — `IPOTESI`

### 7.1 The hypothesis, stated precisely

> **`IPOTESI` TX-007-RC.** The dose effect of AAV9-hSynI-WWOX is principally an effect on **how much
> CNS territory is reached**, not on **how much protein each transduced neuron makes**. A higher
> dose recruits additional neurons and additional regions across a delivery gradient whose caudal
> end is the cerebellum; per-cell expression in already-transduced neurons changes comparatively
> little. Under this account, the apparent non-monotonicity of the dose response is a
> **regional-coverage phenomenon**, and the residual deficits of surviving animals — ataxia in
> particular — are **anatomically explained** (an untransduced or under-expressing cerebellum)
> rather than biologically intrinsic to WWOX restoration.

### 7.2 Verdict: **the account SURVIVES, entirely untested, and the paper cannot refute it**

**What is consistent with it (not confirmation):**

| Observation | Locator | Fit |
|---|---|---|
| Regional vDNA gradient ≈9–12× cortex-over-cerebellum | Fig 5A–5D | ✅ a delivery gradient exists and is large |
| Seven of eight LD-vs-HD comparisons `ns` on vDNA and mRNA, while survival differs at `p < 0.0001` | Fig 5A–5H; Fig 3B caption | ✅ tissue-level mean expression does not explain the dose effect |
| HD cerebellar protein not above LD (`0.7/0.5/0.2` vs `0.7/0.5/0.7`) | Fig 5L | ✅ dose bought no cerebellar protein |
| Authors' own explanation is a **within-group survivor-versus-non-survivor** comparison | Results, S5A–S5D, SELF-READ | ✅ their explanation is also not a per-cell level account |
| Forebrain reaches 4.6–10.7× WT while cerebellum stays 0.6–1.4× at the same timepoint | S5J / S5K | ✅ the same dose is simultaneously too much and too little, **regionally** |

**What is inconsistent with a *pure* coverage account:**

| Observation | Locator | Tension |
|---|---|---|
| Cerebellar %NeuN⁺WWOX⁺ ≈61%, the **highest** of three regions | S3C | 🔴 coverage of cerebellar neurons is not obviously deficient |
| 2021: cerebellar transduction ≈57%, within a few points of cortex | Fig 2G | 🔴 same |

🔴 **The decisive measurement was never made, and naming it is the main deliverable of this
section: percent transduced neurons per region was NEVER measured at LD versus HD.** S3C exists only
in the `4E10` WPRE-comparison arm. Figure 5 measures DNA, transcript and protein **at tissue level**,
which by construction cannot separate *more cells at the same per-cell level* from *the same cells at
a higher level*. **So the coverage hypothesis is not merely unconfirmed in this paper — the
experiment that would discriminate it was not run in the dose arm at all.**

### 7.3 What would test it

1. **Per-region % NeuN⁺WWOX⁺ at LD and at HD**, same animals as Fig 5, with age and n stated. If the
   percentage rises with dose while per-cell intensity does not, the coverage account is supported.
2. **Per-cell WWOX intensity distribution** (single-neuron IF quantification, or single-nucleus
   readout) per region at LD and HD. A coverage effect predicts a **shifted fraction of positive
   cells at an unchanged modal intensity**; a per-cell effect predicts a shifted mode.
3. **Absolute wild-type WWOX per region**, to make fold-WT regionally comparable at all (§3.2.1).
4. **Cerebellar sub-structure resolution** — Purkinje versus granule layer, vermis versus hemisphere.
5. **A quantitative motor/ataxia battery in surviving HD animals**, which is the phenotype the
   cerebellar hypothesis predicts should persist. The 2026 rotarod result runs in the *opposite*
   direction (treated animals exceed WT, `*`) and the repo records the behavioural section as
   carrying a text-versus-panel contradiction; it cannot bear this weight.
6. The **intermediate-dose arm** between `1.23E11` and `2.63E11` already standing as a
   `REVIVAL_TRIGGER` in the repo — which would also test whether expression tracks dose at all.

⚠️ **Not asserted:** that the cerebellum explains any residual deficit; that the non-monotonicity is
a coverage effect; that cerebellar under-expression causes ataxia in this model. All three are
`IPOTESI`. The repo separately records that the cerebellar contribution to the WWOX ataxia phenotype
is itself an **open, contested question** (`CLAIM 039`), and this file does not settle it.

---

## 8 · What I could not establish

1. 🔴 **Cortex and midbrain individual lane values at P30 (Fig 5I, 5K).** Never recorded in the repo
   and unreachable by me. The P30 forebrain-versus-cerebellum contrast therefore rests on the
   **hippocampal** blot alone — the one with the `1.1` KO-lane control failure. **This is the
   weakest link in §3 and it is closable in minutes by an actor with `files/`.**
2. 🔴 **Whether `3.0 / 3.0 / 5.5 / 16.7` (S3E) is a WPRE effect or a `4E10`→`8E10` dose effect** —
   LEGEND's own records disagree (§5.4). Resolvable only by reading the S3E caption/axis.
3. 🔴 **Per-region % transduced at LD and HD** — not measured by the authors. Not a reading debt.
4. 🔴 **Absolute wild-type WWOX level per brain region** — not measured in either paper.
5. 🔴 **S3C's measurement age and n** — stated nowhere in the paper; already recorded in the repo as
   an author question, unanswerable by further reading.
6. 🔴 **Fig 5A–5D's GC normaliser.** The caption states *"normalized to WT levels"*, but wild-type
   mice receive no vector, so the normaliser is not a vector quantity and is undefined. Recorded in
   the repo as an author question. **This means even the vDNA gradient in §6.1 is on an
   uncharacterised scale**, and only its *ratios between regions within one panel* are usable.
7. 🔴 **The 2021 per-region transduction bars (Fig 1E, 2G)** — read only as repo attestations; the
   source text gives the 60–70% envelope, not per-region values.
8. 🔴 **Spinal cord and sciatic nerve fold-WT** — detected, never quantified against WT.
9. 🔴 **Any cerebellar sub-structure or cell-type-resolved value**, in either paper.
10. ⚠️ **S2's internal `n=5` (graph labels) versus `n=4` (caption) discrepancy** is recorded in the
    repo and **not resolved here**; it does not bear on any regional value above, and both are
    carried, neither chosen.
11. ⚠️ **Figure captions for the 2026 paper were not available on my surface at all.** Every 2026
    caption quoted in this file is a repo attestation. The repo's own most-repeated lesson on this
    paper — *"a figure is not read until its caption is read"* — applies to me by construction, and
    is the reason §0's provenance split is stated before any number.

---

## Summary for the orchestrator

- **The cerebellum was assayed**, in every modality and at every timepoint, in both papers. It is not
  a `NOT ASSAYED` region.
- **The Operator's hypothesis holds on the numbers as recorded:** cerebellum `0.1–1.4× WT` across
  every WPRE-free arm and timepoint; cortex/hippocampus/midbrain `3.1–10.7×` at P300 and `9–19×` on
  the P30 hippocampal blot. The high dose did **not** raise cerebellar protein above the low dose.
- **But transduction is not the deficit:** cerebellar `%NeuN⁺WWOX⁺` is ≈61%, the **highest** of three
  regions in the 2026 supplement. The deficit sits in vector-genome load per tissue (≈9–12× below
  cortex), in per-cell output, or in an **unmeasured wild-type denominator** — and these are not
  separated by anything in either paper.
- **The WPRE review-versus-supplement "contradiction" is a scope error in LEGEND's record, not a
  contradiction in the literature**, and resolves against the primary's own Discussion. Fig 3–7 —
  including all regional expression — are WPRE-free on both sides and **not** confounded by it.
- **A new, real contradiction is exposed inside LEGEND:** the `3–16.7×` figure is attributed to two
  mutually exclusive comparisons by two repo files, both citing S3E.
- **The regional-coverage account of the apparent non-monotonicity survives, untested**, because the
  discriminating measurement — per-region % transduced at LD versus HD — was never made.

*End of file. Complete run.*
