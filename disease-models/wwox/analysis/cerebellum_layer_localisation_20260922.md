# At which layer does the forebrain–cerebellum divergence in AAV9-hSynI-WWOX rescue emerge?

**Actor:** Scientist C · **Date:** 2026-09-22 · **Axis:** layer localisation, not magnitude
**Question class:** decomposition along `VECTOR DELIVERY → VECTOR GENOME → TRANSCRIPTION →
TRANSLATION → PROTEIN STABILITY → CELL-TYPE COMPOSITION → FUNCTION`

**Sources.** According to PubMed: `PMID 42422765` / `PMC13343157` — Obeid, Aqeilan *et al.* 2026,
*Molecular Therapy: Advances* 201791, [DOI](https://doi.org/10.1016/j.omta.2026.201791); and
`PMID 34747138` / `PMC8649866` — Repudi & Aqeilan 2021, *EMBO Molecular Medicine* 13:e14599,
[DOI](https://doi.org/10.15252/emmm.202114599). Supporting: `PMID 33255508` — Aldaz & Hussain 2020,
*Int J Mol Sci* 21:8922, [DOI](https://doi.org/10.3390/ijms21238922); `PMID 17291468` — Kumar &
Buckmaster 2007, *Brain Res* 1142:54–60, [DOI](https://doi.org/10.1016/j.brainres.2007.01.027);
`PMID 36828035` — Hussain *et al.* 2023, *Prog Neurobiol* 223:102425,
[DOI](https://doi.org/10.1016/j.pneurobio.2023.102425).

**Not medical advice.** Nothing here is a treatment, dose or route recommendation. Every dose is in
E-notation because the served extraction eats exponents (demonstrated in § 0.3).

> **Scope discipline.** The dose non-monotonicity premise is **CLOSED** (survival-horizon artefact,
> `CC-20260826-DOSE-ADJUDICATION-01` § 6) and is **not reopened anywhere in this file**. The
> `HD/LD = 2.1382` unit question is closed and not re-derived. Animal flow, censoring and
> Kaplan–Meier validity belong to sibling nodes and are touched only where a layer assignment
> depends on them.

---

## 1 · Provenance ledger — what is first-hand here, and what is inherited

### 1.1 Surfaces

| Surface | Status this session |
|---|---|
| `PMID 42422765` **body + complete Materials and methods** | ✅ **FIRST-HAND.** Retrieved via the PubMed MCP route, **48,780 chars** — matches the stated body length exactly. Read section by section today. |
| `PMID 34747138` **body + Methods + all six main figure legends** | ✅ **FIRST-HAND.** The 2021 extraction carries Figure 1–6 legends inline. |
| `PMID 42422765` **figure panels, captions, supplement S1–S8** | 🔴 **NOT FIRST-HAND.** `files/` is gitignored and absent from this worktree; the served 2026 extraction carries **no figure captions**. |
| `PMID 33255508` GTEx regional values | ✅ **FIRST-HAND cross-check** against the repository's own local extract `disease-models/wwox/analysis/data/WWOX_tissue_expression_GTEx.csv`, read by me today (§ 5.2). |
| `PMID 17291468` reagent fact | ✅ **FIRST-HAND at abstract depth**, quoted verbatim below. Body not retrieved. |
| `PMID 36828035`, `PMID 32000863` Purkinje findings | 🟡 **REPO-ATTESTED** from this repository's deep-dive manifests, plus first-hand PubMed abstracts. |

### 1.2 The provenance ceiling, carried and never laundered

🔴 **Every 2026 panel number in this file is a REPO ATTESTATION from a prior actor, not a first-hand
read.** They are inherited from `analysis/tx007_regional_wwox_forebrain_cerebellum_20260922.md`
(Scientist U) and `analysis/tx007_saturation_hypothesis_20260922.md`, whose strongest backing is
`FTR-20260814-42422765-06`, a `complete_fulltext_read` with `supplementary: read`. Rows are tagged
**`REPO-ATTESTED`** throughout. Any arithmetic I perform on them inherits that tag and is tagged
**`DERIVED-FROM-REPO-ATTESTED`** — a derived number cannot be better-provenanced than its inputs.

**The Methods ARE first-hand, and that is what makes this file additive.** The prior nodes
established *what the panels say*. This file establishes *what the measurement instruments can and
cannot mean*, which is a Methods question and is therefore answerable at first hand from here.

### 1.3 Extraction validation — named positive controls before any negative claim

Token census over the 48,780-char 2026 body, run by me today:

| Positive controls (must be non-zero) | count | Validated negatives (zero, and the controls prove the surface works) | count |
|---|---|---|---|
| `cerebell` | 7 | `Purkinje` | **0** |
| `hSynI` | 17 | `granule` | **0** |
| `WPRE` | 29 | `half-life` / `turnover` / `cyclohexim` / `proteasom` / `degrad` | **0 / 0 / 0 / 0 / 0** |
| `Materials and methods` | 1 | `n =` / `n=` | **0 / 0** |
| `GAPDH` | 1 | `p <` / `P <` / `p value` / `p =` | **0 / 0 / 0 / 0** |
| `bGH` | 1 | `reference gene` / `housekeep` / `standard curve` / `absolute quant` / `single-copy` | **0 × 5** |
| `immunoblot` | 6 | `Actb` / `beta-actin` / `18S` / `Hprt` / `Tbp` | **0 × 5** |
| `NeuN` | 2 | `vermis` / `lobul` / `molecular layer` / `calbindin` | **0 × 4** |
| `qPCR` 5 · `RT-qPCR` 2 · `ICV` 12 · `ataxia` 7 | — | `gait` / `beam` / `catwalk` / `copies` / `per cell` / `diploid` | **0 × 6** |

⇒ The served surface indexes gene symbols, reagent names, method vocabulary and region names. The
zeros above are therefore **scientific absences in the served body**, not parser zeros. The brief's
statement that the 2026 extraction carries **zero `n =` tokens and zero P-values** is confirmed
first-hand.

**The exponent trap, shown rather than repaired** — first-hand quotations:
> "an LD (1.23 × 10vg) and a higher dose (HD, 2.63 × 10vg)"
> "low expression observed at 4 × 10vg in the absence of WPRE and markedly higher levels at 8 × 10vg"
> "all vectors were tested at the same titer (4E10)"

The exponents are **eaten** in prose and **survive** where the paper itself wrote E-notation. Hence
`1.23E11`, `2.63E11`, `2E10`, `4E10`, `6E10`, `8E10` throughout.

**One PubMed zero discarded, per failure mode (d).** The query
`Wwox expression pattern developing mouse brain immunohistochemistry hippocampus cortex` returned 0,
and its `query_translation` expanded **`pattern` into the MeSH `"behavior"` block**. A wrong MeSH
expansion must be discarded, so that zero carries no information. The zeros that *are* carried
(`WWOX AND Purkinje` → 2; `Wwox brain regional expression distribution mouse Purkinje` → 0 with a
complete and correct translation) were checked term-by-term against their returned translations, and
`WWOX AND (cerebellum OR cerebellar) AND …` → 4 hits including the known-positive `PMID 32581702`
serves as the positive control for the surface.

### 1.4 Prior-art sequence, executed before anything is declared new

`FIND ISSUE` → `SEARCH EXISTING CLAIMS` → `SEARCH EXISTING CANDIDATES` → `SEARCH DISCOVERY LEDGER`.

| Already held — **not** rediscovered here | Where |
|---|---|
| Cerebellum assayed in every 2026 modality; `0.1×–1.4× WT` in every WPRE-free arm | `tx007_regional_wwox_forebrain_cerebellum_20260922.md` §§ 2–3 |
| Cerebellar `%NeuN⁺WWOX⁺ ≈ 61%`, the highest of three regions, `4E10` WPRE arm only | same, § 4 |
| Per-region % transduced at LD/HD **never measured** | same, § 7.3; saturation file § 3.3 |
| Fold-WT denominator never reported — *"the single most important unmeasured quantity on this axis"* | same, § 3.2.1 |
| Whole-cerebellum homogenate cannot speak about Purkinje cells | same, § 1.2 |
| Hippocampal KO lane reads `1.1` — control failure on the P30 forebrain comparator | same, § 2.1; saturation file § 4 |
| `3–16.7×` (S3E) attribution **UNRESOLVED**: WPRE effect vs `4E10→8E10` dose effect | same, § 5.4; saturation file § 1 |
| WPRE "contradiction" is a **scope difference**, Figs 3–7 WPRE-free on both sides | same, § 5.3; saturation file § 5 |
| Dose non-monotonicity **CLOSED** as follow-up-horizon artefact | `CC-20260826-DOSE-ADJUDICATION-01` § 6 |
| Volume is a stated constant `2.0 µL/hemisphere`; "HD spread further" REFUSED | `tx007_per_arm_delivery_reconstruction_20260922.md` § 7.1 |
| `CLAIM 039` already narrowed and propagated; cerebellar contribution neither established nor excluded | `claim_registry_current.md` CLAIM 039; `CC-20260920-CLAIM039-CEREBELLAR-01` |
| `PMID 32581702`: delayed cerebellar foliation at P1 in `lde/lde` | CLAIM 039 evidence boundary |
| `PREMISE: DETECTION_FLOOR` vocabulary — *not detected* ≠ *absent* | `CC-20260920-DETECTION-FLOOR-01` |
| GTEx regional WWOX TPM, cerebellum highest; local CSV verified | `wwox_postnatal_svz_expression_20260922.md` §§ 4–5 |
| `Wwox^P47T/P47T`: WT-level protein, yet Purkinje loss and reduced molecular/granular layer | `discovery_ledger_current.md` L2375; `PMID 36828035` |

**What is new in this file, and only this:** §§ 3.2, 3.3 (no reference amplicon, no housekeeping
gene, fixed-mass input ⇒ the vDNA readout is inherently per-genome-equivalent); § 5.3 (the
baseline-correction arithmetic against the GTEx ratio, which nobody has applied); § 6.2 (the reagent
chain `MAB377 = clone A60` ⇒ Purkinje cells are excluded from the transduced-fraction denominator by
construction); § 6.4 (the anti-WWOX antibody has no identifier, and why that is a magnitude problem
and not a layer problem); § 4.2 (the denominator-free within-region dose arithmetic); § 7 (the
seven-layer verdict); § 8 H5 and H7.

---

## 2 · 🔴 The central prohibition, restated as arithmetic — and the paradox dissolves

The task forbids collapsing **`NeuN⁺WWOX⁺ fraction`** into **`WWOX amount per transduced cell`**.
These are quantities at two different layers, and the apparent contradiction —
*highest transduced fraction, lowest protein* — is not a contradiction at all. It is what the
conjunction **forces**.

Write `F` = fraction of countable neurons scoring positive, `C` = vector genomes per transduced
nucleus, `V` = vector genomes per host-genome-equivalent of tissue. Then, to first order,
`V ≈ F × C`, so `C ≈ V / F`.

**ARITHMETIC DEMONSTRATION — NOT A MEASUREMENT.** The two terms come from **different arms, different
doses and different animals** (`F` from S3C, `4E10` **+WPRE** comparison arm; `V` from Fig 5A/5D,
`1.23E11`/`2.63E11` **WPRE-free** dose arm). Transferring between them is forbidden. The
demonstration is shown **only** to prove that the two numbers are jointly satisfiable, and its
output is never used as a result:

| | `V` cerebellum ÷ cortex | `F` cortex ÷ cerebellum | ⇒ `C` cerebellum ÷ cortex |
|---|---|---|---|
| LD-equivalent | 320 ÷ 2800 = **0.1143** | 53 ÷ 61 = **0.8689** | **0.0993 ≈ 1/10** |
| HD-equivalent | 730 ÷ 8800 = **0.0830** | 53 ÷ 61 = **0.8689** | **0.0721 ≈ 1/14** |

⇒ **A cerebellum with the highest positive fraction and ~1/10 the genome load per nucleus is
internally consistent, and implies roughly 7–14× fewer vector genomes per transduced cell.** The
"paradox" exists only under the prohibited collapse. It also explains why a positive-fraction
readout and a load readout can point in opposite directions without either being wrong:
**positivity is a threshold measure — one expressing genome can score a cell positive — while load
is a quantity.** A region can be near-universally positive at the detection threshold and still be
an order of magnitude below on amount.

🔴 **This is a reconciliation, not a finding.** The conclusion licensed is negative and important:
**S3C's 61% cannot be used, in either direction, as evidence about cerebellar per-cell output.**

---

## 3 · The instruments, read first-hand from Methods — because the layer assignment depends on them

### 3.1 Delivery — measured, or assumed?

**FIRST-HAND, 2026 Methods, verbatim:**
> "ICV injections … were conducted using stereotactic technique to ensure consistency"
> "The injection site was targeted at ±0.8 mm, 1.5 mm, and −1.6 mm, relative to lambda. These
> anatomical landmarks were visible through the skin at P0‑P1. For older pups … for P5 pups, the
> injection site was targeted at ±1.0 mm, 1.0 mm, and −2.0 mm."
> "A Micro-4 nano-pump controller was used to ensure a steady injection rate of 1–1.5 μL/min,
> delivering **2.0 μL/hemisphere** through a Hamilton syringe with a 32G needle … The needle was kept
> at the injection site for 30‑60 s to allow proper diffusion … The procedure was repeated for the
> contralateral hemisphere."

**FIRST-HAND, 2021 Methods, verbatim — and it is a different procedure:**
> "**Free‐hand** intracranial injections … **Trypan blue 0.1% was added to the virus** to enable
> visualization of the dispensed liquid. An injection site was located at 2/5 of the distance from
> the lambda suture to each eye … the needle was inserted to a depth of approximately 3 mm.
> Approximately **1 µl** (2 × 10[E10] GC/hemisphere) virus was dispensed using a NanoFil syringe with
> a **33G** beveled needle."

| | 2021 | 2026 |
|---|---|---|
| Technique | **free-hand** | **stereotactic** |
| Volume per hemisphere | **1 µL** | **2.0 µL** |
| Needle | 33G bevelled, depth ~3 mm | 32G, coordinate-targeted |
| Rate / dwell | not stated | 1–1.5 µL/min, 30–60 s dwell |
| Tracer | **Trypan blue 0.1%** — visualisation of the dispensed liquid; **no distribution result reported** | none |

🔴 **A THIRD, MECHANICAL REASON THE TWO PAPERS CANNOT BE MERGED, and it is first-hand.** Beyond
different vectors, doses, endpoints and animals, the **delivery procedure itself differs in
technique and in injectate volume by 2×**. Injectate volume is a first-order determinant of
neonatal ICV distribution. So the fact that cerebellum is the *lowest* transduced fraction in 2021
(≈57%) and the *highest* in 2026 (≈61%) must **not** be read as a change in cerebellar biology,
in vector quality, or in anything else. The two numbers are not on a common axis. Reported
separately, never merged, never differenced.

**Is cerebellar access measured?** 🔴 **No — in either paper.** Neither reports a CSF tracer
distribution, a vector-spread time course, a post-injection verification histology of the injection
site, or any measurement of what reaches the fourth ventricle or the cerebellar surface. The 2021
Trypan blue is used to see the **dispensed liquid at the needle**, and no distribution result is
reported anywhere in that paper. **The only delivery-related measurement in either paper is the
downstream endpoint — vDNA per region at P30 in 2026.** Cerebellar access is therefore **assumed**;
the gradient is measured, its cause is not.

**Background expectation — `PREMISE: DEFAULT_FROM_TEXTBOOK`, NOT evidence from these papers.** Both
papers target the lateral ventricles; vector reaching cerebellum must travel caudally (third
ventricle → aqueduct → fourth ventricle) or via subarachnoid CSF, so periventricular forebrain is
exposed first and at higher local concentration. **This is background, it is not tested, stated or
cited in either paper, and it must never be quoted as a result of `PMID 42422765`.**

### 3.2 🔴 NEW — the vDNA qPCR has **no host reference amplicon**, and the input is fixed **mass**

**FIRST-HAND, 2026 Methods, verbatim:**
> "tissue samples (up to 25 mg) were lysed in ATL buffer … DNA integrity and concentration were
> assessed prior to downstream applications by using DeNovix (DS-11FX+). **For qPCR, 50 ng of DNA
> template was used per reaction.** The primer sequences were as follows: forward
> 5′ GCTCTCTTAAGGTAGCCCCG 3′, reverse 5′ CGCCTCATCCTGGTCCTAAA 3′."

**One primer pair. No second amplicon. Validated negative: `reference gene` 0, `single-copy` 0,
`Actb`/`Gapdh`-as-DNA-reference 0, `standard curve` 0, `absolute quant` 0, `copies` 0, `diploid` 0.**

**Two consequences, and they pull in opposite directions.**

✅ **(a) The readout is inherently per-genome-equivalent, so the "cerebellum is cell-dense" escape
hatch is CLOSED.** Fifty nanograms of murine genomic DNA is a fixed number of nuclei (~6 pg per
diploid genome ⇒ ~8.3 × 10³ nuclei). A vector amplicon measured against a **fixed DNA mass** is
therefore a measure of **vector genomes per host nucleus**, not per gram of tissue and not per
unit volume. Cell-density normalisation is built into the assay design. **The prior nodes describe
the 8.8–12.05× gap as a "vDNA load per tissue" or "per gram" quantity and offer cerebellar cell
density as a possible explanation; on the stated Methods, that explanation is unavailable, because
density is already divided out.** This is the single most consequential Methods finding in this file.

🔴 **(b) But the absolute scale is unrecoverable, and the panel's own denominator is undefined.**
Without a standard curve there is no conversion to copies; without a host amplicon there is no
internal check that 50 ng was actually loaded per well. And the prior nodes record the Fig 5A–5D
caption as *"normalized to WT levels"* — 🔴 **REPO-ATTESTED, and undefined for vDNA, because WT mice
receive no vector.** So:
- ✅ **ratios between regions inside one panel** are usable, and are per-nucleus;
- ✅ **ratios between doses inside one region** are usable (§ 4.2);
- 🔴 **the absolute copies-per-nucleus number is NOT RECONSTRUCTABLE**, and whether the plotted
  quantity is raw copies per reaction at all is **NOT READABLE** from the served surface.

### 3.3 🔴 NEW — the RT-qPCR likewise has **no housekeeping gene**, and normalises to total RNA mass

**FIRST-HAND, 2026 Methods, verbatim:**
> "Total RNA was isolated from **non-perfused tissue** using TRIzol … cDNA was synthesized from 1 μg
> total RNA … **For qPCR, 50 ng of cDNA template was used per reaction.** The primer sequences were
> as follows: forward, 5′ ACCTACTTGGACCCAAGACTGGCG 3′, reverse, 5′ GGTGCTGCCGTCGTATCTTTGCC 3′."

**One primer pair. No housekeeping gene. No ΔΔCt statement (`delta Ct` 0, `ΔΔCt` 0, `2-ΔΔ` 0).**

⇒ The transcript readout is **WWOX amplicon per fixed mass of total RNA**. Total RNA is dominated
by rRNA, so this normaliser is approximately *per ribosome*, not *per cell* and not *per nucleus*.
🔴 **The vDNA and mRNA panels are therefore normalised to two different and non-interconvertible
denominators** (host genomes vs total RNA mass). Cerebellar granule neurons are small, with cell
bodies of a fraction of a cortical pyramidal neuron's volume, so the nuclei-per-µg-RNA relationship
is not the same in the two compartments. **Consequence: any transcript-per-genome ratio built from
these two panels has units that do not cancel** — see § 4.3, where the arithmetic is shown and then
declared unusable, as the brief requires.

Also first-hand: **RNA came from non-perfused tissue**, so blood-borne vector genomes and
transcripts are not excluded. Direction of bias not determinable from here.

### 3.4 The immunoblot — two candidate loading controls, and the antibody has no identifier

**FIRST-HAND, 2026 Methods, verbatim:**
> "The following antibodies were used: **rabbit polyclonal anti-WWOX 1:10,000**; mouse monoclonal
> anti-GAPDH (CB-1001), Calbiochem 1:10,000; rabbit polyclonal anti-HSP90 (4874 S), cell signaling
> 1:1000."

- 🔴 **The anti-WWOX antibody carries no vendor, no catalogue number and no clone** — the one
  reagent that generates every WWOX number in the paper. `NOT STATED`. See § 6.4 for why this is a
  **magnitude** problem and not a **layer** problem.
- ⚠️ **Two loading controls are listed and the served surface does not say which normalises Fig 5 or
  S5J.** `NOT READABLE` (captions absent).
- 🔴 **No densitometry method** (`densitom` 0), no replicate statement, no statistic in the body.

### 3.5 Immunohistochemistry — and the reagent that decides § 6

**FIRST-HAND, 2026 Methods, verbatim:**
> "Sagittal brain sections (14 μm) … rabbit polyclonal anti-WWOX 1:5,000 … and **mouse anti-NeuN,
> (MAB377), Milipore, 1:500** … Sections were then imaged using a 3DHISTECH panoramic scanner."

**FIRST-HAND, 2021 Fig 1E legend, verbatim:**
> "Graph showing the percentage of NeuN and WWOX double‐positive cells in different parts of the
> brain (cortex, hippocampus, and cerebellum) from KO mice injected with AAV‐mWwox at P17. NeuN and
> WWOX double‐positive cells were calculated from 3 identical sagittal sections of the
> AAV‐mWwox‐injected mice (n = 3) brains."

⚠️ **Neither paper states, for any region, which anatomical field was counted, how many cells formed
the denominator, or — in cerebellum — which layer.** `NOT STATED`. For the 2026 S3C values the
prior nodes record that **age and n are stated nowhere in the paper**.

### 3.6 Function — the instruments, and what they can localise

**FIRST-HAND, 2026 Results, verbatim:**
> "Motor coordination was assessed at P18 using **hindlimb clasping test**. As shown in 4A and S4B,
> untreated Wwox-null mice displayed severe motor impairment, whereas LD treatment resulted in
> partial improvement and HD treatment achieved near-complete rescue, with **ataxia scores**
> approaching those of WT controls."

🔴 **FLAG — nomenclature versus construct validity, and it is new.** The brief states that no
published cerebellar functional endpoint has been identified. The 2026 paper **does** carry a
dose-resolved endpoint the authors call an *"ataxia score"* — but the **instrument is the hindlimb
clasping test**, a general marker of neurological dysfunction that does not localise to cerebellum
and is routinely positive in corticospinal, basal-ganglia and diffuse neurodegenerative models. The
same instrument carries the 2021 ataxia claim (*"improved motor coordination in rescued mice as
presented by hindlimb clasping test"*, first-hand). ⇒ **The label is cerebellar; the assay is not.**
The brief's statement stands on substance: **no cerebellum-localising functional endpoint exists in
either paper.** What exists is an ataxia-labelled clasping score.

**The rest of the 2026 functional battery, first-hand from Methods:** open field, elevated plus
maze, rotarod, at **3 months**, in **WT + RI versus KO rescued (HD)** only — no LD arm and no KO+RI
comparator, because untreated KO animals are dead. Validated negatives: `gait` 0, `beam` 0,
`catwalk` 0, so **no footprint, beam-walk or kinematic gait analysis**; and no eyeblink
conditioning, no vestibulo-ocular reflex, no ledge or hindlimb-suspension battery.

⚠️ And the rotarod runs the wrong way for a cerebellar-deficit account, first-hand:
> "Treated KO mice exhibited **significantly higher motor coordination and learning compared with WT
> mice**."

A supra-WT rotarod result in an animal hypothesised to have an unreconstituted cerebellum is an
uninterpretable comparator, and the repository separately records the behavioural section as
carrying a text-versus-panel contradiction. **It cannot bear weight in either direction.**

**ECoG, first-hand:** *"the recording electrode was positioned above the **right dorsal cortex**, and
the reference electrode was placed contralaterally"* — single-channel, cortical. 🔴 **No cerebellar
electrode anywhere.** So the paper's one physiological readout is, by electrode placement, blind to
cerebellum.

---

## 4 · The arithmetic — what cancels, what does not, and what that localises

### 4.1 The panel values used (all `REPO-ATTESTED`; no averaging across regions)

Vector: AAV9-hSynI-hWWOX, **WPRE-FREE**. LD `1.23E11 vg`, HD `2.63E11 vg`, neonatal ICV,
`2.0 µL/hemisphere` both arms.

| Layer | Cortex LD / HD | Hippocampus LD / HD | Midbrain LD / HD | 🎯 Cerebellum LD / HD | Locator |
|---|---|---|---|---|---|
| vDNA, P30 | ≈2800 / ≈8800 `ns` | ≈2000 / ≈3800 `*` | ≈2200 / ≈7300 `ns` | **≈320 / ≈730 `ns`** | Fig 5A–5D |
| mRNA, P30 | ≈520 / ≈700 `ns` | ≈540 / ≈650 `ns` | ≈65 / ≈145 `ns` (*p* = 0.08) | **≈37 / ≈95 `ns` (*p* = 0.06)** | Fig 5E–5H |
| protein lanes, P30 | 🔴 never recorded | 14.2/19.5/9.2 · 14.7/9.1/18.3 | 🔴 never recorded | **0.7/0.5/0.7 · 0.7/0.5/0.2** | Fig 5I–5L |
| protein, P300 HD | 8.2× | 10.7× | 5.6× | **1.4×** | S5J |
| protein, P300 HD 2nd panel | 4.6× | 4.7× | 3.1× | **0.6×** | S5K/S6 |
| KO control lanes | 0.02 | **1.1** ⚠️ | 0.03 | 0.08 | Fig 5I–5L |

⚠️ **The hippocampal KO lane reads `1.1` — wild-type intensity in a null animal**, where the other
three regions read 0.02–0.08. Already held; carried here as a **QC flag on every P30 hippocampal
value**, which matters in § 5.3 because the panels the baseline correction fails to rescue are
precisely the panels that are independently suspect.

⚠️ **Every P240/P300 row is survivor-selected**: it describes the animals that lived, not the
treated cohort.

### 4.2 🎯 NEW — the denominator-free arithmetic: within-region, across dose, the baseline cancels **exactly**

This is the only arithmetic in the whole problem where the unmeasured wild-type regional denominator
**cancels identically**, because it is the same region, the same blot normalisation and the same
unknown constant on both sides. `DERIVED-FROM-REPO-ATTESTED`.

| Region | vDNA HD/LD | mRNA HD/LD | protein HD/LD (lane means) |
|---|---|---|---|
| Cortex | **3.14×** | **1.35×** | 🔴 not computable — lanes never recorded |
| Hippocampus | **1.90×** | **1.20×** | 14.033 ÷ 14.300 = **0.98×** |
| Midbrain | **3.32×** | **2.23×** | 🔴 not computable |
| 🎯 **Cerebellum** | **2.28×** | **2.57×** | 1.400 ÷ 1.900 = **0.74×** |
| *(nominal dose ratio)* | *2.1382×* | *2.1382×* | *2.1382×* |

**Three results fall out, and none of them requires the missing baseline.**

1. ✅ **The cerebellum's genome delivery tracks dose essentially proportionally** — `2.28×` against a
   nominal `2.1382×`. Vector *arrival* in cerebellum is dose-responsive.
2. ✅ **The cerebellum's transcription tracks dose supra-proportionally** — `2.57×`, the **highest
   mRNA dose-response of the four regions**, and higher than cortex's `1.35×` despite cortex
   receiving `3.14×` more genomes. Whatever is wrong in cerebellum, **it is not that the region
   fails to transcribe additional genomes.**
3. 🔴 **Protein does not follow, and it does not follow in the forebrain either** — hippocampus
   `0.98×`, cerebellum `0.74×`. Two regions, one shared behaviour.

⇒ **The layer at which dose-responsiveness is lost is the same in both compartments, and it lies
between TRANSCRIPT and PROTEIN.** This is a baseline-independent, extraction-independent,
caption-independent result, and it is the strongest statement this evidence supports.

> 🔴 **Not a reopening of the dose non-monotonicity premise.** The `0.74×` and `0.98×` are
> *within-region protein-versus-dose* observations already held as a **plateau** in
> `tx007_saturation_hypothesis_20260922.md` § 2–3. The CLOSED premise concerns *survival* across
> Fig 2 and Fig 3 horizons and is untouched. Nothing here is offered as a survival claim.

**And it constrains the question as asked.** A transcript→protein ceiling shared by cerebellum and
hippocampus **cannot itself be the source of a cerebellum-specific divergence**. It localises the
*dose* anomaly; it does not localise the *regional* one.

### 4.3 The cross-region ratios — shown, then declared unusable, with the reason

| Quantity | Cortex ÷ cerebellum, LD | Cortex ÷ cerebellum, HD |
|---|---|---|
| vDNA | 2800 ÷ 320 = **8.75×** | 8800 ÷ 730 = **12.05×** |
| mRNA | 520 ÷ 37 = **14.05×** | 700 ÷ 95 = **7.37×** |

**Transcript-per-genome, the ratio the brief asks for. THE ARITHMETIC IS SHOWN AND THE RESULT IS
DECLARED UNAVAILABLE:**

| | Cortex | 🎯 Cerebellum | Cortex ÷ cerebellum |
|---|---|---|---|
| LD | 520 ÷ 2800 = 0.1857 | 37 ÷ 320 = 0.1156 | **1.61×** |
| HD | 700 ÷ 8800 = 0.0795 | 95 ÷ 730 = 0.1301 | **0.61×** — cerebellum *higher* |

🔴 **UNAVAILABLE, for three independent reasons, each sufficient on its own.**
1. **The units do not cancel** (§ 3.3): numerator is per µg total RNA, denominator is per fixed mass
   of genomic DNA. There is no conversion factor, and the relationship between the two differs
   between a granule-cell-dominated and a pyramidal-cell-dominated compartment.
2. **Both panels are on undefined scales** — the vDNA panel's *"normalized to WT levels"* is
   undefined for a quantity wild-type animals do not have (§ 3.2b).
3. **The direction reverses between doses** (1.61× → 0.61×) on `ns` comparisons with no reported `n`
   and no variance. A quantity whose sign flips across a non-significant dose step is not a
   quantity.

⚠️ It is worth recording what the numbers *would* say if they were usable, precisely so that nobody
later mistakes it for a result: **they do not show a cerebellar transcription deficit.** At HD the
cerebellum's transcript-per-genome is the higher of the two. **Any account that localises the
divergence to TRANSCRIPTION has to argue against the paper's own arithmetic, in the only direction
the arithmetic runs.**

**Protein-per-transcript.** Hippocampus ÷ cerebellum: LD `(14.300/540) ÷ (0.633/37)` = **1.55×**;
HD `(14.033/650) ÷ (0.467/95)` = **4.39×**. 🔴 **Also UNAVAILABLE**, and for a fourth reason on top
of the three above: numerator and denominator are each a fold-of-**a different unmeasured regional
wild-type quantity** — regional WT protein for one, regional WT transcript for the other. Two
unmeasured, unrelated denominators do not cancel. `NOT RECONSTRUCTABLE`.

---

## 5 · 🎯 The wild-type regional baseline question — answered

The brief asks whether the wild-type regional WWOX level is even known, and notes this may dissolve
the whole anomaly. It does not dissolve it. It **halves** it, and nobody has applied the correction.

### 5.1 In the two AAV papers: NOT MEASURED, and asserted by citation

🔴 **Neither paper reports an absolute or relative wild-type WWOX level for any brain region, by any
method.** Validated negatives in the 2026 body: `absolute quant` 0, `standard curve` 0, `reference
gene` 0. The 2026 paper's only statements about wild type are **pattern**, not amount, first-hand:
> "In the absence of WPRE, WWOX expression was reduced but exhibited a more uniform, predominantly
> cytoplasmic distribution that **closely resembled endogenous WWOX patterns in WT neurons**."
> "the presence of WPRE downstream of the transgene markedly augmented WWOX expression **when
> compared with wild-type (WT) expression**."

WT is used as a **reference line**, never as a measured regional quantity.

And the 2021 paper **asserts uniformity by citation**, first-hand, Discussion:
> "**WWOX is ubiquitously expressed in all brain regions** (Chen; Chiang; Aldaz & Hussain)."

🔴 **That sentence is the load-bearing premise under every fold-WT number in this literature, and it
is a citation, not a measurement — made by the same laboratory whose panels the premise validates.**
`PREMISE_TAG: UNIFORM_REGIONAL_BASELINE_ASSERTED_BY_CITATION`.

### 5.2 In the wider corpus: the premise is measured, and it is **false in the direction that matters**

One of the three cited sources addresses the regional question directly.
🎯 **`PMID 33255508` (Aldaz & Hussain 2020), abstract, FIRST-HAND, verbatim:**
> "Exploration of gene expression databases indicates that [WWOX] expression is **comparatively
> higher in the human cerebellar cortex than in other CNS structures**. … single-cell RNA-seq data
> … indicate that neurons from the medial entorhinal cortex, Layer 5 from the frontal cortex as well
> as GABAergic basket cells and **granule cells from cerebellar cortex** are the specific neuronal
> subtypes that display the highest [WWOX] expression levels. … Higher [WWOX] expression in
> interneurons and **granule cells from cerebellum** points to a direct link to the described
> cerebellar ataxia in cases of WWOX loss of function."

And the quantities, **verified first-hand today** against the repository's own local extract
`disease-models/wwox/analysis/data/WWOX_tissue_expression_GTEx.csv` (human adult, bulk, TPM):

| Region | TPM | ÷ `Brain_Cortex` |
|---|---|---|
| `Brain_Cerebellar_Hemisphere` | **12.1278** | **1.771×** |
| `Brain_Cerebellum` | **11.2144** | **1.637×** |
| `Brain_Spinal_cord_cervical_c-1` | 10.4735 | 1.529× |
| `Brain_Substantia_nigra` | 7.4768 | 1.092× |
| `Brain_Cortex` | 6.84932 | 1.000× |
| `Brain_Frontal_Cortex_BA9` | 6.8204 | 0.996× |
| `Brain_Hippocampus` | **5.58518** | **0.815×** |

⇒ **Cerebellum ÷ cortex ≈ 1.77×; cerebellum ÷ hippocampus ≈ 2.17×; cerebellum ÷ substantia nigra
≈ 1.62×.** The cerebellum is the **highest-expressing** brain region in the table, and the
hippocampus — the comparator carrying the largest apparent cerebellar deficit — is the **lowest**.

🔴 **Provenance boundary on these numbers, and it is severe.** They are **human**, **adult**,
**bulk parenchyma**, **mRNA**, from a **public database described in a review**. The denominator the
fold-WT numbers actually need is **mouse**, **P30 and P300**, **regional**, **protein**. GTEx is a
`PREMISE`-grade proxy for it, not a substitute. ⚠️ And the repository separately holds, from the same
review's description of the HBT resource, that **cerebellar cortex shows a distinct, larger
early-postnatal rise** in WWOX — which, if it transfers, makes the *neonatal and juvenile* cerebellar
denominator relatively **larger** than the adult ratio above, i.e. the correction at P30 would be
**bigger** than the correction at P300. **NOT MEASURED.**

### 5.3 🎯 NEW — the correction, applied

In these experiments the animals are **`Wwox`-null**, so there is no endogenous contribution and the
readout is exactly `fold-WT = transgene_absolute ÷ WT_regional_absolute`. Let `K` be the
(unmeasured) ratio of wild-type regional WWOX, cerebellum over the comparator. Then the value of `K`
at which the observed fold-WT divergence corresponds to **no difference at all in absolute transgene
protein** is simply the observed ratio of fold-WT values. `DERIVED-FROM-REPO-ATTESTED`.

| Panel | comparator ÷ cerebellum | `K` required to null the divergence | residual after the GTEx `K` |
|---|---|---|---|
| **4E10 +WPRE**, cortex | 25.6 ÷ 6.2 | **4.13** | **2.33×** |
| **2E10 +WPRE**, cortex | 11.6 ÷ 2.4 | **4.83** | **2.73×** |
| **P300 HD S5J**, midbrain | 5.6 ÷ 1.4 | **4.00** | **2.47×** |
| **P300 HD S5J**, cortex | 8.2 ÷ 1.4 | **5.86** | **3.31×** |
| **P300 HD S5J**, hippocampus | 10.7 ÷ 1.4 | **7.64** | **3.52×** |
| **P300 2nd panel**, cortex | 4.6 ÷ 0.6 | **7.67** | **4.33×** |
| **P300 2nd panel**, hippocampus | 4.7 ÷ 0.6 | **7.83** | **3.61×** |
| **4E10 no-WPRE**, cortex | 4.7 ÷ 0.4 | **11.75** | **6.64×** |
| **P30 LD**, hippocampus ⚠️ QC | 14.300 ÷ 0.633 | **22.58** | **10.40×** |
| **P30 HD**, hippocampus ⚠️ QC | 14.033 ÷ 0.467 | **30.07** | **13.85×** |
| **2E10 no-WPRE**, cortex 🔴 floor | 0.8 ÷ 0.1 | 8.00 | 4.52× |

**Four findings, and the third is the one nobody has stated.**

1. 🔴 **The baseline does NOT dissolve the anomaly.** Nulling it needs `K` between **4 and 30**. The
   best available measured `K` is **≈1.6–2.2×**. A residual cerebellar shortfall of roughly
   **2.3× to 4.3×** survives the correction across the P300 panels and the WPRE arms.
2. 🎯 **But it accounts for roughly a factor of two of it, and that correction has never been
   applied in this repository or, so far as the served text shows, in either paper.** ⇒ **Every
   cerebellar fold-WT number in this literature should be de-rated by ~1.8× against a cortical
   comparator and ~2.2× against a hippocampal one before the two are compared at all.** The
   headline contrast *"forebrain 5–11× WT, cerebellum 1.4×"* becomes, corrected, closer to
   *"forebrain 5–11×, cerebellum ~2.5×-equivalent"* — still a real deficit, materially smaller than
   advertised, and **no longer an order of magnitude**.
3. 🎯 **No single `K` reconciles all panels — and the panels it fails hardest are the panels that
   are independently suspect.** The required `K` spans 4.0 → 30.1. If the true `K` were ≈5, the
   **+WPRE arms and the P300 midbrain comparison would be fully explained by the denominator alone**,
   while the **P30 hippocampal panel would need `K` ≈ 23–30** — and the P30 hippocampal panel is the
   one whose **KO control lane reads `1.1`**, and the one whose cortical and midbrain lane values
   were **never recorded by anyone**. That the denominator hypothesis fails precisely where the
   measurement is independently broken is a coherence result, not a selection: **the residual
   divergence is smallest where the evidence is cleanest.**
4. 🔴 **The `2E10` no-WPRE row is at the detection floor and must not be used.** Cerebellar `0.1×`
   against a cerebellar KO lane of `0.08×` is **not a measurement of a small amount** — it is a
   value at the assay floor. `PREMISE: DETECTION_FLOOR` (`CC-20260920-DETECTION-FLOOR-01`).
   **`NOT DETECTED` is never `ABSENT`.** The same applies to the `0` printed at S6D.

**Direction of the residual is therefore established, its magnitude is not.** A real cerebellar
shortfall survives; it is roughly 2–4× rather than 6–20×; and it cannot be sharpened further without
the measured mouse-protein denominator.

---

## 6 · Cell-type composition and the Purkinje gap

### 6.1 The homogenate is a granule-cell measurement

**FIRST-HAND, 2026 Methods:** cerebellum is dissected, snap-frozen, homogenised and blotted as **one
compartment**. Validated negatives in the body: `Purkinje` 0, `granule` 0, `molecular layer` 0,
`lobul` 0, `vermis` 0, `calbindin` 0. 🔴 **Cerebellar sub-structure is NOT ASSAYED in either paper,
by any method, at any timepoint.**

⚠️ **`PREMISE: DEFAULT_FROM_TEXTBOOK`, background and not evidence from these papers:** cerebellar
granule cells outnumber Purkinje cells by orders of magnitude and constitute the large majority of
all neurons in the rodent brain. A whole-cerebellum homogenate — of protein, of RNA, or of DNA — is
therefore a granule-cell-dominated measurement. **Whatever any cerebellar number in either paper
turns out to be, it does not describe Purkinje cells, and must never be cited as if it did.**

**And § 3.2a sharpens this into something usable.** Because the vDNA assay loads a **fixed DNA
mass**, its denominator is *nuclei*, and in cerebellum the nuclei are overwhelmingly granule-cell
nuclei. So the 8.75–12.05× cerebellar vDNA deficit is, to first order, a statement that **the
average cerebellar nucleus — i.e. the average granule-cell nucleus — carries roughly one tenth the
vector genome load of the average cortical nucleus.** That is a much more specific claim than "the
cerebellum receives less vector", and it is the most localised statement the existing data support.

### 6.2 🔴 NEW — the reagent excludes Purkinje cells from the transduced-fraction **denominator**

The reagent chain closes, and it closes against the number the brief centres on.

**Link 1 — FIRST-HAND, 2026 Methods, verbatim:** *"mouse anti-NeuN, (**MAB377**), Milipore, 1:500"*.
Millipore `MAB377` is the original anti-NeuN monoclonal, **clone A60**.

**Link 2 — FIRST-HAND at abstract depth, `PMID 17291468` (Kumar & Buckmaster 2007), verbatim:**
> "Some notable exceptions (i.e., NeuN-negative neurons) include **Purkinje cells in cerebellum**,
> mitral cells in olfactory bulb, and photoreceptors in retina … as assayed with the widely used
> monoclonal antibody **A60**."

⇒ 🔴 **A `%NeuN⁺WWOX⁺` figure in cerebellum excludes Purkinje cells from both numerator and
denominator, by reagent construction.** The cerebellar `≈61%` (2026, S3C) and `≈57%` (2021, Fig 2G)
are statements about the **NeuN-positive cerebellar population** — granule cells, molecular-layer
and Golgi interneurons, and deep-nuclei neurons — and are **silent** about the cell type whose loss
defines cerebellar ataxia.

⚠️ **Stated at its real strength.** The A60 Purkinje-negativity is well documented but is background
here, at abstract depth, and laboratories do occasionally report weak or variable Purkinje signal.
The claim that is unassailable, and the one I make, is the **negative** one:
**Purkinje-cell transduction is NOT ESTABLISHED by a NeuN co-stain and could not be, whatever the
number.** `NOT ASSAYED` — and, per the hard bound, that is neither `NORMAL` nor `ABSENT`.

🔴 **It follows that the highest-transduced-fraction datum, the single observation that argues
hardest against a delivery-limited account, is measured on a population that by construction cannot
include Purkinje cells.** No prior file in this repository records this. It does not make the 61%
wrong; it makes it inapplicable to the ataxia question.

### 6.3 Does `hSynI` drive equally in granule and Purkinje cells? NOT ASSAYED — and the reagent exists

🔴 Neither paper measures promoter activity in any cerebellar cell type. Validated negative:
neither body contains `granule` or `Purkinje`.

⚠️ **`PREMISE: DEFAULT_FROM_TEXTBOOK`:** human synapsin I is a mature-neuron promoter; cerebellar
granule neurons mature postnatally over roughly P0–P21, later than forebrain projection neurons,
so promoter onset is expected to lag in cerebellum at any early assay point. **Not tested, stated or
cited in either paper.**

🎯 **And the discriminating reagent already exists in both laboratories.** FIRST-HAND, 2026 Methods:
*"Custom-made AAV9-CBA-hWWOX and **AAV9-hSynI-EGFP** viral particles were obtained from the Vector
ELSC Core Facility at the Hebrew University of Jerusalem"*; and 2021 used **AAV9-hSynI-EGFP as its
control virus**. A reporter readout is **baseline-free by construction** — GFP has no endogenous
counterpart, so it needs no wild-type denominator, no anti-WWOX antibody and no assumption about
regional WWOX levels. **Nobody has quantified it per cerebellar layer.** This is the cheapest
available separation of the promoter layer from every layer beneath it.

### 6.4 🔴 NEW — which candidate confounds can produce a *layer-localised* divergence, and which cannot

This is a layer problem, so a confound that scales every region by the same factor is not a
candidate answer. Separating the two classes is itself a result.

| Confound | Class | Why |
|---|---|---|
| **anti-WWOX antibody has no vendor, catalogue number or clone** (§ 3.4); and every fold-WT compares **human** WWOX transgene protein against **mouse** Wwox protein — 93% identical, 95% similar (FIRST-HAND, 2021 Introduction) with **unstated** cross-species affinity | 🟡 **MAGNITUDE ONLY** | A fixed affinity ratio between the orthologues rescales **every region identically**. It means **no fold-WT number in this literature is on an absolute scale** — but it cannot create a regional divergence. |
| **No qPCR standard curve, no host reference amplicon** (§ 3.2) | 🟡 **MAGNITUDE ONLY** | Removes the absolute axis; within-panel regional ratios survive. |
| **GAPDH / HSP90 loading control, and which one is used is unreadable** | 🔴 **LAYER-CAPABLE** | `fold-WT = (WWOX/loading)_treatedKO ÷ (WWOX/loading)_WT`. A region-specific loading-protein level **cancels to first order**. It fails **only** if the loading protein per unit tissue differs between treated-KO and WT **within** a region — and in this model it demonstrably can: the same paper reports genotype-dependent **astrogliosis, microgliosis and hypomyelination**, and `Wwox^P47T/P47T` shows **reduced cerebellar molecular and granular layer thickness with Purkinje loss** (`PMID 36828035`). If KO-versus-WT composition diverges **more** in cerebellum than forebrain, the cerebellar fold-WT is biased. This is hypothesis **H5**. |
| **mRNA normalised to total RNA mass, protein to a loading protein, vDNA to DNA mass** (§ 3.3) | 🔴 **LAYER-CAPABLE** | Three incommensurable denominators, and their relationship to cell number differs between a granule-cell and a pyramidal-cell compartment. Blocks every cross-layer ratio (§ 4.3). |
| **Non-perfused tissue for RNA** | 🟡 magnitude, direction undetermined | Blood-borne vector and transcript not excluded; no reason to expect a large regional asymmetry, but **NOT ASSAYED**. |

---

## 7 · 🎯 The verdict — the per-layer table, and where the divergence emerges

For each layer: what was measured, where, how, at what dose and age, with what `n`, its locator, and
whether that layer **can** account for the divergence.

| # | Layer | Measured? | Method · dose · age · `n` · locator | 🎯 Can this layer account for the divergence? |
|---|---|---|---|---|
| 1 | **VECTOR DELIVERY** | 🔴 **NOT ASSAYED as delivery.** Route and geometry are **assumed**, not measured, in both papers. Only the stated procedure is first-hand: stereotactic ICV, `±0.8/1.5/−1.6 mm` re lambda at P0–P1, `2.0 µL/hemisphere`, 1–1.5 µL/min, 32G, both hemispheres (2026); free-hand, ~1 µL, 33G, Trypan-blue-visualised, **no distribution result** (2021) | 2026 Methods (FIRST-HAND); 2021 Methods (FIRST-HAND). Age P0–P5 (2026) / P0 (2021). `n` for delivery: not applicable | 🟡 **CANNOT BE EVALUATED — no delivery measurement exists.** Volume is a **stated constant** across arms, so "HD spread further" is REFUSED (already held). The caudal-CSF-route expectation is **background, not evidence.** `NOT ASSAYED` ≠ `NORMAL` |
| 2 | **VECTOR GENOME** | ✅ **MEASURED, and it is the one layer where a cross-region comparison sits on a common scale.** Cerebellum **8.75× (LD)** and **12.05× (HD)** below cortex | qPCR, **50 ng DNA per reaction** (FIRST-HAND), one primer pair, **no host reference amplicon**, **no standard curve**; LD `1.23E11` / HD `2.63E11`; **P30**; `n` 🔴 **not stated anywhere** (`n =` 0 tokens); Fig 5A–5D, **REPO-ATTESTED**; caption *"normalized to WT levels"* 🔴 undefined for vDNA | 🎯 **YES — this is where the divergence is demonstrably present, and § 3.2a makes it sharper than the prior record: because input is fixed DNA *mass*, the readout is per *nucleus*, so the cerebellar cell-density explanation is already divided out and is unavailable.** The deficit is ~10× **per nucleus**. ⚠️ Whether the panel plots that quantity is `NOT READABLE`; absolute copies are `NOT RECONSTRUCTABLE` |
| 3 | **TRANSCRIPTION** | ✅ **MEASURED.** Cerebellum 14.05× (LD) / 7.37× (HD) below cortex — **but its dose-response is the strongest of the four regions, `2.57×`** | RT-qPCR, **50 ng cDNA per reaction** from 1 µg total RNA, **non-perfused tissue**, one primer pair, **no housekeeping gene** (FIRST-HAND); LD/HD; **P30**; `n` 🔴 not stated; Fig 5E–5H, **REPO-ATTESTED** | 🔴 **NO — and the paper's own arithmetic runs the other way.** The cerebellum transcribes **supra-proportionally** with dose (`2.57×` vs cortex `1.35×`), and its transcript-per-genome is the **higher** of the two at HD (§ 4.3). Any transcription-deficit account must argue against this. ⚠️ Transcript-per-genome is `NOT RECONSTRUCTABLE` — units do not cancel |
| 4 | **TRANSLATION** | 🔴 **NOT ASSAYED — by anyone, anywhere, in any WWOX paper.** No polysome profiling, no ribosome profiling, no nascent-chain labelling, no puromycin assay | Validated negative on the served 2026 body; nothing in the repository's corpus | 🔴 **INDISCRIMINABLE.** Cannot be separated from PROTEIN STABILITY (#5) by any existing measurement: a single steady-state protein number is the **product** of synthesis and degradation, and no experiment splits them |
| 5 | **PROTEIN STABILITY** | 🔴 **NOT ASSAYED — by anyone.** `half-life` 0 · `turnover` 0 · `cyclohexim` 0 · `proteasom` 0 · `degrad` 0, with positive controls passing. No regional WWOX turnover measurement exists in this corpus | — | 🔴 **INDISCRIMINABLE from #4.** ⚠️ **But the one layer-free observation available points at this joint:** within-region protein does **not** rise with dose in either cerebellum (`0.74×`) or hippocampus (`0.98×`) while genomes and transcripts do (§ 4.2). ⇒ **the transcript→protein step is where dose-responsiveness is lost, in BOTH compartments** — so it localises the *dose* ceiling and, being shared, **cannot by itself produce a cerebellum-specific divergence** |
| 6 | **CELL-TYPE COMPOSITION** | 🟡 **PARTIALLY, and on a population that excludes the cell type of interest.** `%NeuN⁺WWOX⁺`: 2026 cortex ≈53% `*`, hippocampus ≈52% `ns(0.07)`, **cerebellum ≈61% `ns`** — the **highest**; 2021 cortex ≈61.5%, hippocampus ≈70.5%, cerebellum ≈57% | 2026: IF, **`4E10` +WPRE arm only**, age 🔴 not stated, `n` 🔴 not stated, S3C, **REPO-ATTESTED**. 2021: IF, `4E10` total, P17/P19, **n = 3 mice × 3 sagittal sections** (legend FIRST-HAND), Fig 1E/2G, bars **REPO-ATTESTED**. 🔴 Counted field and cell denominator **not stated** in either | 🎯 **YES — and it is the layer with the largest unmeasured lever.** The cerebellum is treated as **one homogenate**; sub-structure is `NOT ASSAYED`; and § 6.2 shows **MAB377 = clone A60 excludes Purkinje cells from the fraction's denominator by construction**. 🔴 **Per-region % transduced at LD and HD was NEVER measured**, so nothing here can separate *more cells* from *more protein per cell* at the therapeutic dose |
| 7 | **FUNCTION** | 🔴 **NO cerebellum-localising endpoint.** The only dose-resolved motor endpoint is a **hindlimb clasping score** the authors label *"ataxia scores"* — an instrument that does not localise to cerebellum. Rotarod/open-field/EPM: HD only, 3 months, WT+RI comparator, and rotarod reads **supra-WT**. ECoG: single channel over **right dorsal cortex** | Clasping: **P18**, LD **and** HD, Fig 4A/S4B, text FIRST-HAND, values REPO-ATTESTED. Battery: 3 months, HD only, `n` in legends only (🔴 absent from served surface). ECoG: from ~P14, 7 days, *"limited cohort"* | 🔴 **CANNOT BE EVALUATED.** `gait` 0 · `beam` 0 · `catwalk` 0 — no footprint, beam-walk or kinematic analysis; no eyeblink conditioning; no VOR; no cerebellar electrode. **A cerebellar functional deficit is neither established nor excluded**, consistent with `CLAIM 039`'s standing narrowing |

### 7.1 🎯 The answer, stated plainly

**The divergence is demonstrably present at layer 2, VECTOR GENOME, and it cannot be localised any
further downstream on existing evidence.**

**What is established.**
- ✅ A cerebellar deficit in **vector genomes per host nucleus** of **~9–12×** relative to cortex,
  at P30, in the same animals, at both doses (§ 4.3, § 3.2a). This is the **only** cross-region
  comparison in the whole problem that sits on a denominator-free scale, and the fixed-mass DNA
  input means **cerebellar cell density does not explain it**.
- ✅ A shared **transcript→protein ceiling** in cerebellum *and* hippocampus across the dose step
  (§ 4.2). Denominator-free. It localises the **dose** anomaly and, being shared, **cannot** be the
  source of the **regional** one.
- ✅ **Transcription is not the cerebellar bottleneck** — the cerebellum's dose-response in transcript
  is the strongest of four regions.
- ✅ Roughly **a factor of 1.8–2.2 of the apparent divergence is a denominator artefact** and should
  be removed before any comparison (§ 5.3). A residual of ~2.3–4.3× survives on the clean panels.

**What is INDISCRIMINABLE, and why — each reason independent and sufficient.**

1. 🔴 **Everything from layer 3 downstream is expressed as a fold of an unmeasured regional
   wild-type quantity.** Cross-region comparison of two ratios with two unmeasured, unequal, and
   provably non-uniform denominators is not a comparison. **This alone blocks localisation to
   TRANSCRIPTION, TRANSLATION, PROTEIN STABILITY or COMPOSITION.**
2. 🔴 **TRANSLATION and PROTEIN STABILITY are NOT ASSAYED by anyone**, so they cannot be separated
   from each other, let alone assigned a regional coefficient. A steady-state protein number is
   their product.
3. 🔴 **Per-region % transduced at LD and HD was never measured.** S3C exists only in the `4E10`
   WPRE arm; Fig 5 is tissue-level. ⇒ *more cells* and *more protein per cell* are not separable at
   the therapeutic dose. This is the acknowledged hole and it is not a reading debt — the experiment
   was not run.
4. 🔴 **The three layers are measured against three incommensurable denominators** (DNA mass, total
   RNA mass, loading protein), so no ratio between adjacent layers is computable (§ 4.3).
5. 🔴 **Cerebellar sub-structure is NOT ASSAYED**, and the one cell-type-resolved measurement that
   exists **excludes Purkinje cells by reagent construction** (§ 6.2).
6. ⚠️ **The forebrain comparator at P30 carries a control failure** (KO lane `1.1`), and cortical and
   midbrain P30 lane values were never recorded, so the P30 contrast rests on the single suspect
   blot.

⇒ **Formally: the divergence emerges no later than VECTOR GENOME, is not attributable to
TRANSCRIPTION, and the question of whether an additional divergence emerges at TRANSLATION,
PROTEIN STABILITY or CELL-TYPE COMPOSITION is `NOT RECONSTRUCTABLE` from anything published.**
Per the brief, the deliverable in that situation is the smallest experiment that could discriminate
them — § 9.

---

## 8 · Seven mechanistically distinct explanations

Competing hypotheses are **preserved**. No winner is selected, because no discriminating evidence
exists. **No numerical probabilities.** Each is `IPOTESI` unless marked.

### H1 · Denominator — cerebellum simply has more endogenous WWOX to be measured against
**Mechanism.** Wild-type cerebellar WWOX is the highest in the CNS, concentrated in granule cells.
Fold-WT therefore has its largest denominator in cerebellum, and a given absolute transgene output
appears as the smallest fold there. The divergence is partly an artefact of the **ratio**, not of any
biological layer.
**Also predicts.** Absolute WWOX per µg protein in **untreated WT** mouse cerebellum exceeds cortex
by ≥2×; the apparent cerebellar deficit shrinks in proportion when re-expressed absolutely; the
effect is present at every dose, every timepoint and in every arm — which is exactly the observed
pattern (`0.1×–1.4×` universally).
**Supports.** `PMID 33255508` (highest in cerebellar cortex; granule cells the top neuronal subtype);
GTEx cerebellum/cortex **1.771×**, cerebellum/hippocampus **2.172×**, verified locally; and the 2021
paper's own baseline premise is **a citation, not a measurement** (§ 5.1).
**Against.** Nulling the divergence needs `K` = **4.0–30.1**; the measured proxy is **1.6–2.2**. So
H1 is **partially confirmed and insufficient** — it removes ~2× of a 6–20× headline and leaves
~2.3–4.3× on the clean panels (§ 5.3). It also cannot explain the vDNA gap, which has no WT
denominator at all.
**Cheapest discriminator.** Absolute regional WWOX immunoblot in **untreated WT mice** against a
recombinant-WWOX standard curve, total-protein normalised, P30 and P300. No vector, no new cohort
beyond WT controls the colony already breeds.

### H2 · Per-nucleus genome deficit from mitotic dilution in the granule lineage
**Mechanism.** AAV genomes are episomal and are diluted by cell division. Neonatal ICV at P0–P5
targets a forebrain that is largely post-mitotic, but cerebellar granule-cell precursors in the
external granular layer proliferate intensely for the following ~2 weeks. Vector delivered at P0
is therefore lost from precisely the population that becomes the numerical majority of cerebellar
nuclei. The deficit is in **copies per nucleus**, established after injection, in the cerebellum's
dominant cell type.
**Also predicts.** The per-nucleus cerebellar vDNA deficit **widens** between an early (≈P7) and a
late (P30) timepoint, while the forebrain ratio is stable; **deep cerebellar nuclei and
molecular-layer interneurons** — post-mitotic earlier — carry near-forebrain copy numbers while the
**granular layer** does not; a **later** injection (P10–P14, after most granule-cell divisions)
narrows the cerebellar deficit; genome load per transduced cerebellar nucleus is far below cortical
(the § 2 demonstration shows ~1/10 is the value such a conjunction forces).
**Supports.** The measured 8.75–12.05× vDNA gap on a **fixed-mass DNA input**, i.e. already
per-nucleus (§ 3.2a) — the strongest single piece of evidence in the file. Consistent with the
cerebellum reaching ~61% positivity while carrying ~1/10 the load, since positivity is a threshold
measure and one genome suffices to score a cell (§ 2).
**Against.** The 2026 S8 arm reports that HD delivery at **any** point P0–P5 fully rescued the
phenotype with *"robust WWOX expression … including the cortex, hippocampus, and cerebellum"*
(FIRST-HAND) — a five-day window is short relative to EGL proliferation, so this is weak evidence
against and the S8 statement is text-level, HD-only and unquantified. ⚠️ `PREMISE:
DEFAULT_FROM_TEXTBOOK` on the EGL proliferation timing — **not tested, stated or cited in either
paper.**
**Cheapest discriminator.** vDNA per nucleus measured **per cerebellar layer** (granular vs Purkinje
vs deep nuclei) by laser-capture or single-nucleus qPCR, at two ages, in the **same** animals whose
cortex is measured. An injection-age series (P1 vs P10) with per-region per-nucleus vDNA is the
stronger but costlier version.

### H3 · Promoter-cell-type mismatch — `hSynI` is weak or late in cerebellar granule cells
**Mechanism.** The transgene is driven by human synapsin I, a mature-neuron promoter. Cerebellar
granule neurons mature over P0–P21, later than forebrain projection neurons, so per-genome
transcription is lower or delayed in the compartment that supplies most cerebellar nuclei.
**Also predicts.** Transcript per vector genome is **lower** in cerebellum than cortex, and the gap
narrows with age; an `hSynI`-EGFP reporter shows weak granular-layer and strong deep-nuclei signal;
a promoter with granule-cell activity (or a ubiquitous one) closes the cerebellar gap at equal dose.
**Supports.** Cerebellum is the lowest region in **every one of the eight cells** of the ±WPRE
Fig 2E matrix (already held); the +WPRE cerebellar multiplier is the **largest of four regions**
(13–24× at both doses, already held), which is what a **transcript-limited** compartment looks like
when a post-transcriptional enhancer is added.
**Against.** 🔴 **The paper's own arithmetic runs the other way.** Cerebellar transcript
dose-response is `2.57×`, the strongest of four regions, and at HD cerebellar transcript-per-genome
is **higher** than cortical (0.1301 vs 0.0795). ⚠️ That ratio is formally unusable (§ 4.3), so it
weakens rather than refutes H3 — but the direction is not H3's.
**Cheapest discriminator.** 🎯 **Quantify the `AAV9-hSynI-EGFP` control vector per cerebellar layer.**
Both laboratories already hold this reagent, and a reporter needs **no wild-type denominator, no
anti-WWOX antibody and no baseline assumption** — it isolates layer 3 from layers 1, 2, 4, 5 and 6 in
one stain.

### H4 · Regional protein stability — cerebellar neurons degrade WWOX faster
**Mechanism.** WWOX is a short-lived protein with ubiquitin-pathway partners (ITCH is a canonical
WW1 interactor, FIRST-HAND from the 2021 Introduction). If cerebellar neurons have a higher WWOX
turnover rate, equal transcript yields less steady-state protein — and a saturable degradation
capacity would additionally cap output as dose rises.
**Also predicts.** WWOX half-life in cerebellar tissue is shorter than in cortex; proteasome or
E3-ligase inhibition raises cerebellar WWOX disproportionately; **protein fails to track transcript
in the region with the shortest half-life** — and the largest gains come from a construct that
raises output post-transcriptionally, not from more capsids.
**Supports.** 🎯 **The strongest denominator-free signal in the file:** within-region protein does
**not** rise with dose in cerebellum (`0.74×`) **or** hippocampus (`0.98×`) while vDNA rises
`2.28×`/`1.90×` and mRNA `2.57×`/`1.20×` (§ 4.2). A synthesis-independent ceiling is exactly what a
saturable degradation or chaperone-capacity limit produces. Consistent with the repository's held
position that in WWOX **severity tracks residual protein function, not abundance**
(`CLAIM 030`), and with `Wwox^P47T/P47T` showing **WT-level protein** yet cerebellar degeneration
(`PMID 36828035`) — protein amount is not the whole story in this gene.
**Against.** 🔴 The ceiling is **shared** with hippocampus, so as stated it localises the **dose**
anomaly and **not** the **regional** one. H4 becomes a regional explanation only in a stronger form
— that cerebellar turnover is *faster still* — for which **there is no evidence in any direction**:
regional WWOX turnover has **never been measured by anyone** (validated negative, § 1.3).
**Cheapest discriminator.** Cycloheximide chase (or pulse-SILAC) on acute cortical and cerebellar
slices or synaptosomes from **wild-type** mice — two tissues, one gel series, no vector, no cohort.

### H5 · 🔴 NEW — Denominator-composition drift at the loading-control step
**Mechanism.** `fold-WT = (WWOX/loading)_treatedKO ÷ (WWOX/loading)_WT`. The loading protein cancels
**only** if its level per unit tissue is the same in treated-KO and WT **within** each region. In
this model it is not guaranteed: the KO brain carries astrogliosis, microgliosis and hypomyelination,
and cerebellar cytoarchitecture is genotype-sensitive. If KO-versus-WT composition diverges **more**
in cerebellum than in forebrain, the cerebellar fold-WT is biased downward with no biological
difference in per-cell output at all. Note this is **layer-capable**, unlike the antibody-identity
and standard-curve problems, which are magnitude-only (§ 6.4).
**Also predicts.** Re-normalising the same lysates to **total protein** (Ponceau / REVERT) rather
than GAPDH moves the cerebellar fold-WT and leaves the forebrain roughly unchanged; GAPDH per µg
total protein differs between KO and WT cerebellum; the bias tracks the degree of structural
divergence per region.
**Supports.** Two loading controls are listed and **which one normalises Fig 5 is unreadable**
(§ 3.4); the same paper reports strong genotype-dependent glial and myelin changes; `Wwox^P47T/P47T`
shows **reduced cerebellar molecular and granular layer thickness with Purkinje loss and degenerated
dendrites** (`PMID 36828035`), i.e. cerebellar composition **is** genotype-sensitive in this gene;
and `PMID 32000863` reports Purkinje loss and granular-cell apoptosis in `Wwox`-null mice.
**Against.** 🔴 The cerebellar deficit **also appears in vDNA**, a DNA-mass-normalised measurement
with no protein loading control anywhere in it. So H5 cannot be the whole account — at most it
inflates the protein-layer component of a deficit that is independently present at layer 2.
**Cheapest discriminator.** Re-blot the archived lysates with **total-protein normalisation** and
report WWOX per µg total protein alongside the GAPDH-normalised value. Same samples, one gel, and it
also fixes every fold-WT number retrospectively.

### H6 · Purkinje invisibility — a measurement-layer mechanism, not a biological one
**Mechanism.** Every cerebellar number in both papers is either (a) a whole-cerebellum homogenate,
dominated by granule cells, or (b) a NeuN co-stain which, with clone A60, **excludes Purkinje cells
from both numerator and denominator**. The Purkinje population could be **entirely untransduced** or
**fully reconstituted**, and no existing measurement could tell the difference. Under this
hypothesis the forebrain–cerebellum "divergence" as posed is partly a comparison between a
forebrain measured in its principal neurons and a cerebellum measured in a cell type that is not the
one the ataxia phenotype is about.
**Also predicts.** A calbindin (or PCP2/Car8) + WWOX co-stain returns a Purkinje transduced fraction
**unlike** 61%; Purkinje WWOX intensity distribution is bimodal or near-zero; and a cerebellar
functional deficit, if present, correlates with the Purkinje number and not with the homogenate
number.
**Supports.** Reagent chain closed at first hand: 2026 Methods `MAB377` = clone A60; `PMID 17291468`
verbatim — *"NeuN-negative neurons include Purkinje cells in cerebellum … antibody A60"*. Validated
negatives: `Purkinje` 0, `calbindin` 0, `molecular layer` 0 in the served body. And the sibling
finding that the cerebellum is treated throughout as one homogenate (already held).
**Against.** Nothing — **it is a gap, not a claim.** ⚠️ Which also means it explains nothing on its
own. Its value is that it **invalidates the single observation that argues hardest against a
delivery-limited account**, and it is the cheapest gap in the whole problem to close.
**Cheapest discriminator.** Calbindin + WWOX (and calbindin + vector-genome or reporter) co-stain on
**sections that already exist**. One antibody, one stain, existing material.

### H7 · 🔴 NEW — A pre-existing cerebellar lesion: the rescue window closes earliest in cerebellum
**Mechanism.** If the cerebellar lesion is substantially established **before** the injection, then
no P0–P5 restoration acts on it. The cerebellum would then be a compartment whose substrate — the
cells available to transduce and the architecture they sit in — is already altered at the moment of
delivery, producing a low and **dose-invariant, time-invariant** output no matter what arrives.
**Also predicts.** A cerebellar structural deficit is measurable in the KO **at or before P0**;
cerebellar volume, foliation or layer thickness in the **treated** KO at P30 remains below WT even
where forebrain endpoints normalise; the cerebellar fold-WT is **flat** across dose, across
timepoint and across ±WPRE — which is what is observed (`0.1×–1.4×` in every WPRE-free arm at every
dose and time); and no injection age within the tractable window narrows it.
**Supports.** Human WOREE: *"cerebellar vermis hypoplasia … have been described in most cases"*, and
a **fetal MRI at 21 weeks** showing mild cerebellar vermis hypoplasia **with normal cortical gyration
and lamination for age** — the repository's own reading records the cerebellum as **the earliest
detectable sign** (`discovery_ledger_current.md` L911, L554). Rat `lde/lde`: *"the development of
cerebellum was delayed … as shown by reduced number of foliation"* at **P1** (`PMID 32581702`, via
`CLAIM 039`'s evidence boundary). `Wwox`-null mouse: *"defective cerebellar midline fusion"*,
Purkinje loss, granular-cell apoptosis (`PMID 32000863`).
**Against.** 🔴 **It does not explain the vDNA gap**, which is a delivery/genome quantity and would
not follow from an altered substrate once the readout is per-nucleus. ⚠️ **Species firewall:** the
fetal-MRI and vermis evidence is **human**, the foliation delay is **rat `lde/lde`**, and the AAV
experiments are **mouse FVB `Wwox`-null**. These do not transfer, and `CLAIM 039` explicitly remains
a rat-model claim with the human imaging material **not integrated**. H7 is therefore a
**cross-species hypothesis on a mouse dataset** and is tagged as such.
**Cheapest discriminator.** Cerebellar volume, foliation index, molecular/granular layer thickness
and total-cell stereology in **untreated KO at P0–P2** versus WT, plus the same measures in treated
KO at P30. It is also the measurement `CLAIM 039`'s standing `REVIVAL_TRIGGER` already asks for.

### 8.1 Distinctness check

| | H1 | H2 | H3 | H4 | H5 | H6 | H7 |
|---|---|---|---|---|---|---|---|
| **Layer it acts at** | the **ratio** (all layers ≥3) | 2 → 6 | 3 | 4–5 | measurement of 5 | measurement of 6 | 1 and 6, pre-injection |
| **Predicts low per-cell output?** | no | **yes** | **yes** | **yes** | no (apparent only) | unknown | no |
| **Predicts low per-nucleus genomes?** | no | **yes** | no | no | no | unknown | no |
| **Survives if WT baseline turns out uniform?** | 🔴 **dies** | yes | yes | yes | yes | yes | yes |
| **Survives if per-nucleus vDNA gap is an artefact?** | yes | 🔴 **dies** | yes | yes | yes | yes | yes |
| **Explains dose-invariance of the cerebellar value?** | **yes** | partly | partly | **yes** | yes | — | **yes** |
| **Falsified by a reporter (GFP) showing normal cerebellar signal?** | no | partly | 🔴 **dies** | no | no | no | no |

Seven distinct mechanisms, seven distinct falsifiers, no two collapsing onto the same measurement.

---

## 9 · 🎯 The single highest-information experiment

**Experiment compression.** Four disconnected measurements would answer four questions. One
co-registered measurement answers five, and it is specified as **one cohort, one tissue-processing
pipeline, three channels read on the same material**, with an internal absolute standard rather
than a second study.

> ### 🎯 **A cerebellar-layer-resolved, absolutely-calibrated per-cell readout at LD and HD**
>
> **Cohort.** `Wwox`-null mice treated neonatally at LD and at HD with the WPRE-free
> AAV9-hSynI-WWOX vector, plus **untreated wild-type** and **untreated KO** controls, harvested at
> **P30** and at **P300**, with `n` and animal flow stated per arm per age. One hemisphere per
> animal to imaging, the contralateral to biochemistry, **from the same animal**.
>
> **Channel A — per-cell WWOX with cell-type identity.** WWOX immunofluorescence intensity
> quantified **per cell**, co-stained with **calbindin** (Purkinje), **NeuN** (granule and
> interneuron, with its A60 limitation stated), and a glial marker, resolved by **cerebellar layer**
> (granular / Purkinje / molecular / deep nuclei) and against cortical layer 5 and CA1 on the same
> sections. Report the **full intensity distribution**, not a mean, and the **positive fraction**
> separately.
>
> **Channel B — per-nucleus vector genomes in the same layers.** Vector-genome copies per nucleus by
> DNA-FISH, or by laser-capture / single-nucleus qPCR, **with a single-copy host reference amplicon
> and a plasmid standard curve** — the two controls the published assay lacks (§ 3.2).
>
> **Channel C — the absolute calibration, which is the part that rescales the literature.** WWOX
> protein per µg **total protein** (Ponceau/REVERT, not GAPDH alone) in each region of the
> **untreated wild-type** animals, against a **recombinant WWOX standard curve**, with the
> anti-WWOX antibody identified by vendor, catalogue and lot, and its **human-versus-mouse WWOX
> affinity ratio measured on recombinant standards of both orthologues.**

**What it separates, mechanism by mechanism.**

| Reads out | Settles |
|---|---|
| Channel C alone | **H1** outright, and **rescales every fold-WT number in this literature onto an absolute axis** — removing the objection that blocks localisation at layers 3–6 (§ 7.1 reason 1). Also removes the magnitude-only confounds of § 6.4 |
| Channel A, **distribution shape** at LD vs HD | 🔴 **The central prohibition, resolved by measurement.** A *coverage* effect shifts the **fraction** positive at an unchanged **modal intensity**; a *per-cell-output* effect shifts the **mode**. This is the never-measured per-region % transduced at LD and HD, delivered **with** the per-cell amount the fraction cannot contain |
| Channel A, **calbindin channel** | **H6** outright — the first Purkinje-resolved WWOX measurement in this model, and the first cerebellar number that describes the cell type the ataxia phenotype is about |
| Channel B ÷ Channel A positive fraction | **genomes per transduced cell**, per layer — **H2** directly, and it supplies the quantity § 2 could only demonstrate conditionally |
| Channel A ÷ Channel B per layer | per-genome output per cell type — **H3**, on a scale where the units cancel because both channels are per-cell |
| Layer thickness, Purkinje counts and cell-type proportions, read off the same sections | **H5** (composition drift) and **H7** (pre-existing substrate), at zero marginal cost |
| — | 🔴 **H4 (protein stability) is the acknowledged residual.** It is the one hypothesis this experiment does not settle, because a steady-state per-cell amount is still a synthesis × degradation product. **H4 becomes the named next experiment**, and its cheapest form is a cycloheximide chase on wild-type cortical and cerebellar slices — no vector, no cohort |

**Why this and not the alternatives.**
- **If only one channel can be run, run Channel C.** It is the cheapest (wild-type controls the
  colony already breeds, no vector, no imaging), it is the denominator of every disputed number, and
  it is the measurement whose absence makes all the others uninterpretable. But it discriminates only
  **H1** — it is foundational, not discriminating, and it must not be mistaken for the answer.
- **If a second, cheaper discriminator is wanted before committing**, quantify the
  **`AAV9-hSynI-EGFP` reporter both laboratories already own**, per cerebellar layer. It isolates
  **H3** with no baseline, no anti-WWOX antibody and no new construct.
- **The one-line caption read that is cheaper than all of them**, for an actor whose worktree has
  `files/`: the **S3E caption and axis label** in `mmc1.pdf`, which closes the `3–16.7×` attribution
  dispute in minutes (§ 10).

**Not asserted, explicitly.** That the cerebellum explains any residual deficit · that cerebellar
under-expression causes ataxia in this model · that any hypothesis above is correct · any dose or
route for any species. No medical advice.

---

## 10 · `REVIVAL_TRIGGER`s

| Closed / blocked item | Status | `REVIVAL_TRIGGER` |
|---|---|---|
| **Dose non-monotonicity** | 🔒 **CLOSED** as a follow-up-horizon artefact (`CC-20260826-DOSE-ADJUDICATION-01` § 6). **Not reopened here** | An **intermediate dose arm** specified as a fraction of HD, **with per-region % transduced measured in the same animals**. 🔴 Expression data alone must **not** reopen it — the § 4.2 within-region protein ratios (`0.74×`, `0.98×`) are a **plateau**, already held, and are not a survival claim |
| **`3–16.7×` = WPRE effect or `4E10`→`8E10` dose effect** | 🔴 **UNRESOLVED**; two repository files disagree, both citing S3E. **Must not be cited as a WPRE effect** | **One read of the S3E caption and axis label** in `mmc1.pdf` / `mmc2.pdf`, by any actor whose worktree has `files/`. Until then prefer the Fig 2E-derived multipliers, whose construct labels are unambiguous |
| **2026 figure captions / supplement** | 🔴 **SOURCE_BLOCKED.** `files/` absent; network is an allowlist and general egress is 403 at CONNECT. **Not retried here**, per `SOURCE_BLOCKED → set trigger → CONTINUE` | Any legitimate route to the supplementary captions. On opening, record **caption text, arm labels, dose, WPRE status, region, timepoint, normalisation denominator, values and statistics** for **S3C, S3E, S3F, S5J, S5K, S6D** — and above all **whether Fig 5A–5D plots raw copies per reaction or a derived quantity** (§ 3.2b) |
| **Cortex and midbrain P30 lane values (Fig 5I, 5K)** | 🔴 Never recorded by anyone; the P30 forebrain contrast rests on the **one blot with the `1.1` KO lane** | `files/`-enabled read of Fig 5I and 5K. ~5 minutes, and it is the weakest link in the whole regional argument |
| **`CLAIM 039` cerebellar contribution** | 🟡 Narrowed and propagated (`BATCH_20260921_001`); neither established nor excluded | **Standing, unchanged:** a quantitative cerebellar endpoint in the `lde/lde` strain — Purkinje counts, foliation index, molecular-layer thickness — or a motor battery. 🎯 **This file adds a second trigger:** a **cerebellum-localising** motor endpoint in the **mouse** AAV model, because § 3.6 establishes that the existing *"ataxia score"* is a **hindlimb clasping** measurement and does not localise |
| **Wild-type regional WWOX baseline** | 🔴 **NOT MEASURED** in either paper; asserted by citation. Proxy is human/adult/bulk/mRNA | 🎯 **NEW:** any absolute regional WWOX quantification in **mouse** brain protein — from any source, at any age. On arrival, **re-run § 5.3's correction table**, which is pre-specified and mechanical |
| **Purkinje-cell transduction** | 🔴 **NOT ASSAYED**, and not assayable by a NeuN co-stain (§ 6.2) | 🎯 **NEW:** any calbindin / PCP2 / Car8 co-stain with WWOX or with a vector reporter in this model. Any `%NeuN⁺WWOX⁺` cerebellar figure encountered in future reading must be recorded as **granule-lineage, Purkinje-excluded** |
| **anti-WWOX antibody identity** | 🔴 `NOT STATED` — no vendor, no catalogue, no clone, for the reagent behind every WWOX number (§ 3.4) | 🎯 **NEW:** an author correspondence answer, a lot number in any related paper, or a **Reporting Summary / Key Resources Table** in the supplement. Flagged as **magnitude-only** (§ 6.4) — it does not explain the regional divergence, but no fold-WT number is on an absolute scale without it |
| **Regional WWOX turnover** | 🔴 **NOT ASSAYED by anyone** — validated negative across the corpus | 🎯 **NEW:** any WWOX half-life, cycloheximide-chase, proteasome-inhibition or pulse-labelling measurement, in any tissue, in any species. **H4 cannot be evaluated at all until one exists** |

---

## 11 · What I could not establish

1. 🔴 **Whether the divergence has any component downstream of VECTOR GENOME.** Blocked by six
   independent reasons (§ 7.1), any one of which is sufficient. `NOT RECONSTRUCTABLE`.
2. 🔴 **TRANSLATION and PROTEIN STABILITY are NOT ASSAYED by anyone**, in these papers or anywhere
   in this corpus, and **cannot be separated from each other** by any existing measurement.
3. 🔴 **Absolute regional wild-type WWOX in mouse brain protein.** The best available proxy is human,
   adult, bulk, mRNA. The correction is derived (§ 5.3) but its magnitude rests on that proxy.
4. 🔴 **Whether Fig 5A–5D plots raw copies per reaction.** Without it, even the per-nucleus reading
   of the vDNA gap — the strongest result in this file — carries a `NOT READABLE` on its y-axis
   definition. This is the single most consequential thing a `files/`-enabled actor could close.
5. 🔴 **Absolute vector-genome copies per nucleus.** No standard curve and no host reference
   amplicon in the published assay (§ 3.2). `NOT RECONSTRUCTABLE`.
6. 🔴 **Any cerebellar sub-structure or Purkinje-resolved value**, in either paper.
7. 🔴 **Per-region % transduced at LD and at HD** — never measured; not a reading debt.
8. 🔴 **S3C's measurement age and `n`**, and the counted field and cell denominator for every
   transduced-fraction figure in both papers. `NOT STATED`; already recorded as an author question.
9. 🔴 **Which loading control normalises Fig 5 and S5J** — GAPDH or HSP90. `NOT READABLE`.
10. 🔴 **Cortex and midbrain P30 protein lane values**; and no `n` or P-value anywhere on the served
    2026 surface (validated: `n =` 0, `p <` 0).
11. 🔴 **The `3–16.7×` attribution** — inherited UNRESOLVED and left UNRESOLVED. Not cited as a WPRE
    effect anywhere above.
12. 🔴 **Whether the anti-WWOX polyclonal detects human WWOX and mouse Wwox with equal affinity.**
    93% identity / 95% similarity is first-hand from the 2021 Introduction; equal antibody affinity
    does not follow. Classified **magnitude-only** (§ 6.4) and therefore not a candidate answer to
    the layer question — but it means no fold-WT number is absolute.
13. ⚠️ **Whether GAPDH per µg total protein differs between treated-KO and WT cerebellum**, which is
    the condition under which **H5** becomes live. Not determinable from published text.
14. ⚠️ **Whether the human/rat cerebellar developmental findings transfer to the mouse FVB
    `Wwox`-null model.** **H7 is a cross-species hypothesis on a mouse dataset** and is tagged as
    such; `CLAIM 039` remains a rat-model claim and the human imaging material remains
    unintegrated by operator condition.
15. ⚠️ **Any cerebellar functional endpoint.** The only dose-resolved motor measurement is a
    **hindlimb clasping** score, which does not localise; the rotarod reads **supra-WT** and the
    repository records that section as carrying a text-versus-panel contradiction; the ECoG
    electrode is **cortical**. A cerebellar functional deficit is **neither established nor
    excluded**.

---

## Summary for the orchestrator

- 🎯 **The divergence is demonstrably present at layer 2, VECTOR GENOME, and cannot be localised
  further downstream.** ~9–12× below cortex, and — because the published qPCR loads a **fixed DNA
  mass with no host reference amplicon** (first-hand Methods) — that is a **per-nucleus** deficit,
  so **cerebellar cell density does not explain it.** The prior record's "per gram of tissue" reading
  and its cell-density escape hatch are closed.
- 🔴 **The central prohibition dissolves the apparent paradox.** `V ≈ F × C`: a highest-fraction,
  lowest-load cerebellum is internally consistent and **forces** ~7–14× fewer genomes per transduced
  cell. Shown as a cross-arm **demonstration, never used as a result**. The 61% is a **threshold**
  measure; the load is a **quantity**. They cannot be collapsed and they do not conflict.
- 🎯 **The wild-type baseline question, answered: partially yes, and nobody has applied the
  correction.** Neither paper measures it; the 2021 paper **asserts** uniformity by citation. GTEx
  (verified first-hand locally) gives cerebellum/cortex **1.771×**, cerebellum/hippocampus
  **2.172×** — cerebellum the highest CNS region. Nulling the divergence needs `K` = **4.0–30.1**.
  ⇒ **The anomaly does not dissolve, but ~2× of it is a denominator artefact, and every cerebellar
  fold-WT number should be de-rated by ~1.8–2.2× before comparison.** Corrected, the deficit is
  **~2.3–4.3×** on the clean panels, not an order of magnitude. And **no single `K` fits all panels
  — the ones it fails hardest are the P30 hippocampal panel with the `1.1` KO lane.**
- 🎯 **Denominator-free result: the transcript→protein step is where dose-responsiveness is lost — in
  cerebellum `0.74×` AND hippocampus `0.98×`**, while genomes rise `2.28×`/`1.90×` and transcripts
  `2.57×`/`1.20×`. Baseline cancels exactly. It localises the **dose** ceiling and, being **shared**,
  cannot be the source of the **regional** divergence. **Not** a reopening of the closed premise.
- 🔴 **Transcription is NOT the cerebellar bottleneck.** The cerebellum has the **strongest** mRNA
  dose-response of four regions.
- 🔴 **NEW reagent finding: `MAB377` is clone A60, which does not label Purkinje cells** (`PMID
  17291468`, verbatim). ⇒ **the ≈61% cerebellar transduced fraction excludes Purkinje cells from its
  own denominator by construction** — so the one datum that argues hardest against a delivery-limited
  account is inapplicable to the ataxia question.
- 🔴 **NEW: the paper's only dose-resolved "ataxia score" is a hindlimb clasping test** — an
  instrument that does not localise to cerebellum. The ECoG electrode is cortical. `gait`, `beam`,
  `catwalk` = 0. **No cerebellum-localising functional endpoint exists in either paper.**
- 🔴 **NEW: a third, mechanical reason the two papers cannot be merged** — 2021 is **free-hand,
  ~1 µL/hemisphere, 33G**; 2026 is **stereotactic, 2.0 µL/hemisphere, 32G**. The 57%-versus-61%
  cerebellar difference is not on a common axis and must not be differenced.
- 🔴 **TRANSLATION and PROTEIN STABILITY are NOT ASSAYED by anyone.** No WWOX turnover measurement
  exists in this corpus, in any tissue or species.
- 🎯 **Seven distinct hypotheses preserved, no winner selected, no probabilities.** H1 denominator ·
  H2 mitotic dilution of episomal genomes in the granule lineage · H3 `hSynI` promoter mismatch ·
  H4 regional turnover · **H5 (new)** loading-control composition drift · **H6** Purkinje
  invisibility · **H7 (new)** pre-existing cerebellar lesion. Each has its own falsifier; none
  collapses onto another's measurement.
- 🎯 **One experiment, three co-registered channels, five hypotheses separated:** a
  cerebellar-layer-resolved per-cell WWOX intensity distribution with **calbindin** identity, plus
  per-nucleus vector genomes in the same layers with a host reference amplicon and standard curve,
  plus an **absolute wild-type regional calibration** as its internal standard. **The distribution
  shape is the measurement that resolves the central prohibition** — shifted fraction at unchanged
  mode means coverage, shifted mode means per-cell output. **H4 is the named residual.** If only one
  channel can be run: the absolute WT baseline, which is the cheapest and rescales the whole
  literature but discriminates only H1.
- ⚡ **Cheapest actionable items for a `files/`-enabled actor, in order:** the **S3E** caption
  (closes the `3–16.7×` dispute) · **Fig 5A–5D's** y-axis definition (decides whether the strongest
  result in this file stands) · **Fig 5I and 5K** lane values (closes the weakest link).
- ✅ **No registry, queue, ledger, receipt or canonical file was edited. No `BATCH_COMMIT`. No git
  command was run.** This file is the only output.

*End of file. Complete run.*

---

## 11 · ORCHESTRATOR VERIFICATION — added 2026-09-22, after hand-back

### 11.1 🟢 The GTEx baseline ratios reproduce — with one precision point

Re-computed independently from the repository's own
`analysis/data/WWOX_tissue_expression_GTEx.csv`:

| ratio | using `Brain_Cerebellum` (11.2144) | using `Brain_Cerebellar_Hemisphere` (12.1278) | reported |
|---|---|---|---|
| cerebellum / cortex BA9 (6.8204) | **1.6442** | **1.7782** | 1.771 |
| cerebellum / hippocampus (5.58518) | **2.0079** | **2.1714** | **2.172 — exact** |

⇒ **The figures require the `Brain_Cerebellar_Hemisphere` entry**, not `Brain_Cerebellum`. Two
cerebellar entries exist and they differ by 8%, so **the entry used should be named.** With the lower
entry the ratios are **1.64× / 2.01×** instead.

🟢 **The substantive conclusion is unaffected in direction and approximately unaffected in
magnitude:** GTEx puts cerebellar WWOX **1.6–2.2× HIGHER** than cortex or hippocampus — the *opposite*
of the uniform baseline both papers assume — so **a fold-of-WT computed against a uniform baseline
OVERSTATES the cerebellar deficit**, by roughly 2×.

🔴 **And the bound this correction must carry, which is larger than the 8% one:** **GTEx is HUMAN
RNA; the experiment is MOUSE PROTEIN.** This is a cross-species **and** cross-modality transfer, so it
is **indicative of a direction, not an applicable correction**. The pre-specified correction table in
§ 2 is the right shape and must wait for a **mouse-protein regional baseline** before being applied to
any number. Nothing here licenses restating a published fold-of-WT as corrected.

### 11.2 🟢 The within-region dose arithmetic is the strongest result here, and it is baseline-immune

Within a region, `HD/LD` **cancels the regional baseline exactly** — whatever it is, measured or not.
So these four numbers survive every objection in § 11.1:

| | vDNA | mRNA | protein |
|---|---|---|---|
| cerebellum | **2.28×** | **2.57×** | **0.74×** |
| hippocampus | — | — | **0.98×** |

*(nominal dose ratio **2.1382×**)*

⇒ **Genome and transcript track dose. Protein does not — in BOTH compartments.** So the dose ceiling
sits at the **transcript → protein** step, and because it is **shared** between cerebellum and
forebrain it **cannot** be what produces the regional divergence. **Transcription is not the cerebellar
bottleneck**, and that is established without any baseline at all.

⚠️ This is **not** a reopening of the closed non-monotonicity premise. It is the **plateau** already on
record, now localised to a step.

### 11.3 The prohibition, honoured as arithmetic

`V ≈ F × C` — highest transduced **fraction** combined with ~1/10 genome **load** *forces* ~7–14× fewer
genomes per transduced cell. 🟢 **Positivity is a threshold measure; load is a quantity. There was
never a paradox** — and the two must not be collapsed, which was the central prohibition.
