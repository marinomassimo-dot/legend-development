# `TX007_GENOTYPE_CLASS_CEILING` — is the progenitor defect a property of all WWOX loss, or only of the engineered knockout?

**Date:** 2026-09-21 · **Actor:** Scientist B · **Node:** `TX007_GENOTYPE_CLASS_CEILING`

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and
> every ledger. Nothing here changes a claim, a paper record, the working model or the tracking log. Anything
> promotable goes through INGEST → DEEP_DIVE → BATCH_COMMIT.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> **Nothing here is medical advice.** No dose, schedule, indication or clinical recommendation is formulated
> anywhere in this file. Everything below is material for discussion with a treating clinical team and for nobody
> else.

---

## 0. Read depth declared up front

| PMID | Identity | Depth reached **in this session** | Returned body length | Figure access |
|---|---|---|---|---|
| **42397075** | Steinberg/Zonca … Aqeilan 2026, *Brain* — WWOX–MYC organoids | 🔴 **not fetchable.** `convert_article_ids` returns pmid + doi only — **no PMCID exists**, so the PMC route is unavailable, not untested. Worked from LEGEND's receipt `FTR-20260810-42397075-04` (`complete_fulltext_read`, coverage all-`read`) and its **30-locator** manifest | **0 bytes** | 🔴 **none, and this is load-bearing.** Every number in §1 is a **figure attestation captured by a prior session that had the rendered supplementary volume** (170 ppi, key pages re-read at 258 ppi). It is LEGEND's record. **I have not seen a pixel of it and do not present any of it as a fresh measurement.** |
| **42422765** | Obeid *et al.* 2026, *Mol Ther Oncol* — dose-ranged neuronal WWOX gene therapy | **full body read in-act** and re-analysed here for dose/WPRE/safety language | **48 780 characters (measured exactly)** | none this session. Panel values from LEGEND manifest `PMID42422765.json` (29 locators; receipt `FTR-20260814-42422765-06`, `complete_fulltext_read`, S1–S5 = 31 panels inspected) |
| **34747138** | Repudi *et al.* 2021, *EMBO Mol Med* | full body read in-act (Wave 2), re-queried here | ≈19 000 characters (approximate; not instrumented) | none |
| **22534828** | Chang J-Y *et al.* 2012, *Cell Death Dis* | **abstract only** | n/a | none |
| — | PubMed `WWOX AND (overexpression OR ectopic expression) AND (apoptosis OR neuron…)` | executed | **74 records** | n/a |
| — | PubMed `(WWOX OR WOX1) AND (ectopic OR overexpression OR transfection) AND apoptosis AND (neuron OR … OR neuroblastoma)` | executed | 🔴 **2 records, `total_count: 2`** | n/a |

🔴 **Parser warning, and this time it hits the doses.** In the Obeid body read in-act, **every vector-genome
exponent is deleted**: the text returns `"an LD (1.23 × 10vg) and a higher dose (HD, 2.63 × 10vg)"` and
`"a dose of 4 × 10vg"`. **The exponents are superscripts and the extractor removed them.** Therefore the values
`1.23 × 10¹¹ vg` and `2.63 × 10¹¹ vg` used below are **not quoted from my fetch** — they come from `CLAIM 011`,
which records them from a prior-session read of the rendered Figure 3B raster (`gr3.jpg`,
sha256 `c63f930c…4997d`). Anyone quoting a vg dose from extracted PMC text in this literature will print a dose
that is wrong by ten orders of magnitude. **Recorded as a method finding, not only as a caveat.**

---

## 1. The direct answer, before the evidence

**The progenitor lesion is shared across genotype classes; its consequence is not — and the gradation of the
consequence cannot be attributed to genotype with the data as published.** In radial glia, MYC activation is
present in the engineered knockout **and** in both patient-derived lines at comparable magnitude (pseudobulk
log2FC on WT ≈ 1.8 / 1.65 / 1.6), so the molecular lesion `TX-007` cannot reach is **not** a property of the
CRISPR null alone. What *is* almost entirely the knockout's is the **downstream consequence** — cell composition
(neuronal fraction log2FC ≈ −2.6 in KO vs within ≈0.2 of WT in both patient lines) and the proliferation index.
But three things block reading that as a genotype gradient. **(i) There is no isogenic comparison across genotype
classes**: the knockouts are CRISPR clones on the JH-iPS11 background, while WOREE and SCAR12 are **different
individuals on different backgrounds**, so genotype and donor background are perfectly confounded. **(ii) The
system's own within-genotype, within-background variance is significant**: two isogenic knockout clones differ
from each other on the progenitor readout (SOX2⁺MYC⁺/SOX2⁺ ≈ 43 % vs ≈ 54 %, bracket `*`), and no analysis
partitions clone variance from line variance. **(iii) The patient lines' "near-normal" medians sit inside
enormous distributions** — on mitotic progenitors the SCAR12 and WOREE whiskers reach ≈41 % and ≈44 % against a
WT median of ≈3 % — so the missing SCAR12 bracket is a **non-significant result in a hugely dispersed,
unpowered comparison**, which is not evidence of normality. ⇒ **`TX-007`'s progenitor caveat should be left
general and re-worded, not graded by genotype (option (c), a specific re-wording, given in §3).** And the finding
that actually changes the portfolio is a different one: **`TX-007` has a measured efficacy floor and no measured
ceiling** — the low dose does not rescue survival, the high dose leaves surviving animals at **8.2× cortical and
10.7× hippocampal WWOX at P300**, the **cerebellum never reaches wild type at any dose or timepoint**, and the
survival threshold itself **has no measured expression difference behind it**. Nothing in the WWOX literature
bounds the upper end: the only published experiment joining WWOX overexpression, apoptosis and any neuronal term
is **two records**, neither in a neuron.

---

## 2. Task 1 — what IS and IS NOT established about the radial-glia compartment in residual-protein lines

**Provenance rule applied to this whole section.** `PMID 42397075` has no PMC deposit and no local artefact
reachable from this environment. Every panel value below is marked **`figure-attestation-from-prior-session`**
and is LEGEND's record (manifest `deepdive_manifests/PMID42397075.json`, receipt `FTR-20260810-42397075-04`), not
a measurement made here. Where a significance test is reported I say what it said; where a bracket is **absent**
I say it is absent and refuse to convert that into "not significant" — this repository has already paid for that
conversion twice (`CLAIM 005`, and again on `PMID 42422765` Figure S8).

| Readout | Engineered KO (isogenic to WT) | WOREE (patient) | SCAR12 (patient) | Test reported? | Established? |
|---|---|---|---|---|---|
| **RG cell fraction** (Fig. 2F, log2FC vs WT) | RGs ≈ **+0.55** | within ≈ **0.05** | ≈ **−0.15** | 🔴 **no bracket or P recorded in the manifest for panel F** | **NOT established** for patient lines. A log2FC plot without a test is a description |
| **Neuronal cell fraction** (Fig. 2F) | Neu ≈ **−2.6** | within ≈ 0.05 | ≈ −0.2 | same — none recorded | KO effect is large and visually unambiguous; **patient-line near-normality is untested** |
| Absolute cell counts (Fig. 2D) | 3020 | 5916 | 3422 | n/a | descriptive. WT 5649 |
| **Proliferation index** (Suppl. Fig. 5B, pH3⁺SOX2⁺ %) | ≈ **10 %**, bracket **`****`** | ≈ **6 %**, bracket **`*`** | ≈ **4.5 %**, 🔴 **no bracket drawn** | ✅ for KO and WOREE; **absent** for SCAR12 | **WOREE IS significantly elevated** — the patient class is **not** normal on this axis. SCAR12 **untested**, not normal. WT ≈ 3 % |
| ⚠️ **Dispersion of that index** | — | **whisker to ≈ 44** | **whisker to ≈ 41** | — | 🔴 **The patient distributions run to ~14× the WT median.** "Near-normal median" and "enormous spread" are both true, and only the first has been propagated |
| **RG transcriptome — MYC** (Suppl. Fig. 4, pseudobulk log2FC vs WT) | ≈ **1.8** | ≈ **1.65** | ≈ **1.6** | volcanoes: **MYC past threshold in both patient lines** | ✅ **ESTABLISHED and SHARED.** Co-directional partners also shared: SFRP1, H4C3 up; PTN, VIM, NR2F2, EDNRB down in both |
| RG transcriptome — regional identity (Suppl. Fig. 4F, NKX2.2:PAX6) | — | — | — | **all `ns`** | a declared negative: dorsoventral identity is not the lesion |
| **Cell-cycle phase distribution** (Fig. 4C, log2FC KO/WT) | S ≈ +0.78, G2M ≈ +0.5, G1/G0 ≈ −0.2, M ≈ −0.35 | 🔴 **not measured** | 🔴 **not measured** | 🔴 **"no error bars and no significance markers"**, and Fig. 4A KO/WT pseudotime densities are *near-superimposed* | **NOT established in ANY line, KO included.** The cell-cycle argument is the mechanistic core of the paper and it is plotted without error bars |
| **MYC promoter occupancy** (Fig. 4J, ChIP-seq vs 1000 random gene sets) | KO marker **inside** the null distribution | not done | not done | 🔴 **P reported for WT only** (`WT P-val < 0.0001`) | The panel supports "MYC binds immature-neuron promoters in WT and not detectably in KO". **The paper does not state a KO result**, and an unmarked comparison is not a declared negative |
| **Functional consequence** — neuronal output | SATB2⁺/nuclei WT ≈2.3 % → KO-A2 and KO-1B ≈0.5 % (`**`, `***`) | early/late neuron balance **inverted** (≈65 % early / 35 % late vs WT ≈35/65), n = 9094 cells | **same inversion, independently** | ✅ for the maturation phenotype in both patient lines | ✅ **ESTABLISHED: the patient lines have a real neuronal-maturation phenotype** — it is a *maturation* phenotype, not a *composition* one |

**What follows, stated precisely.**

1. ✅ **The molecular lesion in the progenitor compartment is shared.** MYC activation in radial glia is present in
   WOREE and SCAR12 at ~90 % of the knockout's magnitude, with a shared co-directional gene set. `TX-007`'s caveat
   therefore names something that exists in residual-protein genotypes too.
2. ✅ **A transcriptional change without a proportional compositional consequence is a real and common result, and
   that is exactly what this is.** Entry 2 and entry 25 of LEGEND's manifest are **not in conflict** — they
   measure different layers. The prior session's own correction (*"QUALIFIES MY OWN CLAIM, WHICH WAS TOO FLAT"*)
   is the right reading and is adopted here unchanged.
3. 🔴 **But "the patient lines are near-normal" is weaker than it has been propagated as.** On the one progenitor
   readout with a test, **WOREE is significantly elevated (`*`)**; SCAR12 carries **no bracket at all**; and both
   patient distributions have whiskers reaching ~41–44 % against a WT median of ~3 %. **Near-normal medians in
   wildly dispersed, untested distributions.**
4. 🔴 **The cell-cycle phase distribution — the mechanistic bridge from MYC to reduced neuron output — is not
   established in any line.** It is plotted without error bars or significance markers even for the knockout, and
   the pseudotime densities are near-superimposed. **Nobody has measured it in a patient line at all.**
5. 🔴 **No functional consequence of RG MYC activation has been measured in a patient line.** The maturation
   phenotype is real and shared; that it is *caused by* the RG MYC activation is an inference the paper's own
   reagent (A51, non-selective, one clone, no independent differentiations) cannot support.

---

## 3. Task 2 — the therapeutic question, in one sentence

> **`TX-007`'s progenitor caveat should be neither left as-is nor graded by genotype class, but re-worded to say
> what is actually measured — the progenitor *lesion* (MYC activation in radial glia) is present in
> residual-protein genotypes as well as in the engineered null, while the magnitude of its *downstream
> consequence* is unresolved because genotype is confounded with donor background and the patient-line
> comparisons are untested or dispersed.**

**Evidence for.** MYC pseudobulk log2FC ≈1.8 / 1.65 / 1.6 across KO / WOREE / SCAR12, with both patient volcanoes
carrying MYC past threshold and a shared co-directional partner set; the authors' own sentence that the therapy
*"rescued neuronal functional phenotypes without correcting RG abnormalities"* is written about the model as a
whole, not about one line; and the inverted early/late neuron balance is reproduced in **two independent patient
genotypes**.

**Strongest argument against.** That the *therapeutically relevant* quantity is not the lesion but its
consequence, and on consequence the patient lines really do sit far closer to wild type — neuronal fraction
within ≈0.2 log2FC, proliferation index 4.5–6 % against the knockout's 10 %, and only two genes differentially
expressed between SCAR12 and WOREE neurons. If the consequence is genuinely milder in residual-protein
genotypes, the ceiling really is higher for them, and leaving the caveat general **under-promises the therapy for
the majority of patients** — which is a real cost, not a conservative default.

**Why that argument nevertheless does not carry, and this is the decisive part.**

🔴 **There is no isogenic comparison across genotype classes anywhere in that paper.** The isogenic axis exists —
JH-iPS11 wild type against `JH WKO-1C`, `JH WKO-2C`, `KO-A2`, `KO-1B`, all CRISPR clones on that one background —
but every patient line is a **different individual on a different background**: WOREE `WSM S` (c.517-2A>G
homozygous), `LM-iPS` (c.864G>A over a ~93 kb 16q23.1 deletion), `WCH S` (c.410G>T p.Gly137Val / c.517-2A>G);
SCAR12 `WPM S` and `WPM D` (both c.1114G>C homozygous). **The comparison that generates the gradation —
KO > WOREE > SCAR12 — varies genotype and donor background together, and no isogenic patient-allele knock-in
exists.**

🔴 **And the within-genotype, within-background variance is itself significant and of comparable size.** Two
isogenic knockout clones, same genotype, same donor, differ on the progenitor readout: SOX2⁺MYC⁺/SOX2⁺ ≈ **43 %
in KO-A2 versus ≈54 % in KO-1B**, with a bracket `*` drawn **between the two knockout clones**; on SOX2⁺ per
nuclei they read ≈21.5 % and ≈33 % against WT ≈15 %. **Clone-level variance in this system is measurable,
significant, and unpartitioned.** A between-line difference that is not shown to exceed it cannot be attributed
to genotype.

⇒ **`FLAG`, not `SCORE`. The gradation is confounded by donor background and cannot be attributed to genotype
with the data as published.** That is the honest verdict and, per the node brief, a full outcome rather than a
failed one.

**What would resolve it — one design.** An **isogenic allelic series on the JH-iPS11 background**: wild type,
CRISPR null, and knock-ins of `c.517-2A>G` (splice/null class) and `c.1114G>C` (missense/missense class), all on
the same parental line, with **≥3 independent clones per genotype and ≥3 independent differentiations**, scored
on the same four layers (RG fraction · proliferation index · RG transcriptome · cell-cycle distribution). That
single experiment separates genotype from background, partitions clone variance, and is the only way to know
whether `TX-007`'s ceiling moves with genotype class.

---

## 4. Task 3 — the dosing and overexpression finding the portfolio is not carrying

### 4.1 What was found, and where it sits

**In the human organoid arm** (`PMID 42397075`, figure attestation from prior session): WWOX protein after AAV9,
relative to WT = 1, **ranges 0.4× to 7×** across lines given the same vector — SCAR12 `WPM S1` goes from 0.1
untreated to **7** after AAV9; WOREE lines reach 0.4–0.9; the engineered knockouts reach 0.8 and 1.4. **A
seventeen-fold spread.** Downstream, SATB2 mRNA in treated WOREE runs from about wild-type level to about
**eleven-fold above it** (box ≈1 to ≈11, a visible point near 8.7, whisker to 13, against WT ≈1.3), BCL11B/CTIP2
about **three-fold**, and TCF-4 protein in the AAV9-rescued knockout falls to **0.3× WT**. The pattern is not
overshoot in one direction: **it is absence of level control.**

**In the mouse arm** (`PMID 42422765`, figure attestation from prior session): at **P300** the HD blot is labelled
**8.2-fold cortex, 10.7-fold hippocampus, 5.6-fold midbrain, 1.4-fold cerebellum** relative to WT; a second P300
panel reads cortex 4.6, hippocampus 4.7, midbrain 3.1, **cerebellum 0.6**. With the WPRE element — the
configuration of the 2021 proof-of-concept — Figure 2E lane values reach **25.6 / 22.3 / 11.6 / 6.2** across
cortex / hippocampus / midbrain / cerebellum at the higher of the two doses tested.

### 4.2 What the authors themselves say — verbatim, fetched in this act

> "Another central insight from the present study is the importance of precise control over transgene expression for both efficacy and safety."

`surface: body` · Discussion · PMID 42422765.

> "However, WPRE-containing vectors also produced a more intense and spatially diffuse neuronal signal, characterized by prominent punctate staining throughout neurons, likely reflecting elevated expression levels rather than altered subcellular targeting. Such amplification may increase peak transgene exposure and introduce variability across developmental stages and brain regions. Although no overt toxicity was observed in prior studies, we removed WPRE as a proactive risk-mitigation step to improve the predictability and control of neuronal WWOX expression for potential clinical translation."

`surface: body` · Discussion · PMID 42422765. 🔴 **Mood check, and it matters.** *"Although no overt toxicity was
observed"* is a **non-observation in studies not designed to detect it**, not a safety result; and
*"proactive risk-mitigation"* is the authors' own statement that the overexpression direction worried them.

> "we generated AAV9-hSynI-WWOX vectors lacking the WPRE element to achieve tighter control of transgene expression and to proactively optimize the safety margin for clinical translation"

> "However, this reduction in expression necessitates the use of higher vector doses to achieve comparable therapeutic outcomes."

`surface: body` · Results / Discussion · PMID 42422765. 🔴 **These two sentences are the trade-off in the authors'
own words: the design change that lowers per-genome expression buys its safety margin with more capsid.**

### 4.3 Is there published evidence about WWOX overexpression toxicity in neurons? — **No**

| Probe | Result |
|---|---|
| PubMed `(WWOX OR WOX1) AND (ectopic OR overexpression OR transfection) AND apoptosis AND (neuron OR neurons OR neuronal OR cortical OR hippocampal OR SH-SY5Y OR neuroblastoma)` | 🔴 **`total_count: 2`.** `PMID 27999774` (the HYAL-2–WWOX–SMAD4 **review**, already in LEGEND) and `PMID 22534828` |
| `PMID 22534828` (Chang J-Y *et al.* 2012, *Cell Death Dis*) — **abstract only, not read** | Abstract states *"TIAF1 was essential for p53-, WOX1- and dominant-negative JNK1-induced cell death"* and that *"TIAF1, p53 and WOX1 acted synergistically in … causing apoptosis"*. ⚠️ **COS cells, cancer lines and neuroblastoma grown on cancer ECM — not neurons.** ⚠️ Chang/NCKU line, on which LEGEND already holds a node-collapse and independence caution. **Abstract ≠ reading; this is a census entry, not evidence** |
| `PMID 42422765` body, read in full in-act | `overexpress` = **0**, `supraphysio` = **0**, `apopto` = **0**, `threshold` = **0**; `toxicity` = **1** (the non-observation quoted above); `tumor` = **3**, all in the Introduction describing WWOX as a tumour suppressor. 🔴 **No tumour surveillance result is reported in this paper at all.** All roman-type tokens — informative zeros |
| `PMID 34747138` body, read in full in-act (Wave 2) | the tumour non-finding is present and triply qualified: *"we did not detect gross tumor formation in the limited number of adult-null mice treated with AAV9-hSynI-WWOX that we examined (age 8–11 months)"* |
| LEGEND | holds the **principle** but not a datum: `FM-013` (*"«Più proteina» non è l'obiettivo; «più funzione» lo è. E il rescue supra-fisiologico è un rischio, non un successo"*), `N-05` (*"neither too little nor too much WWOX"*), `DL-MECH-009` (the WPRE trade-off, cerebellum 16.7×), and the repeated observation that WWOX is pro-apoptotic in several systems and that the Zfra/peptide programmes work by **consuming** WWOX |

⇒ **`DATO`: gene addition for WWOX produces uncontrolled, regionally uneven, durably supraphysiological protein
levels — 4.6–10.7× wild type in forebrain at P300, up to ~26× with WPRE, 0.4–7× across human organoid lines.**
⇒ **`IPOTESI`, untested: that this is harmful in neurons.** The overexpression direction is **not obviously
benign** — WWOX is a pro-apoptotic tumour suppressor and the organoid work shows loss of the apoptotic checkpoint
in its absence — but **no experiment anywhere has asked whether excess WWOX harms a neuron.** Both halves must
travel together. Reporting only the first would be alarmism; reporting only the second would be the
`DEFAULT_FROM_TEXTBOOK` failure this repository names.

---

## 5. Task 4 — the floor, the ceiling, and whether the window is narrow

### 5.1 The floor is measured and is a threshold, not a slope

`CLAIM 011` already records from Figure 3B (prior-session raster read of `gr3.jpg`, sha256 `c63f930c…4997d`):
**LD = 1.23 × 10¹¹ vg does not rescue survival** — it moves death from ~20 to ~90 days and the curve then reaches
zero — while **HD = 2.63 × 10¹¹ vg plateaus at ~80 % to day 300**, and at P20 the low dose had not corrected
hypoglycaemia. The paper's own words, read in-act, are consistent and softer: *"LD treatment modestly, though
significantly, extended lifespan relative to untreated-null controls … whereas HD treatment produced a marked"*
benefit. **Significant extension is not rescue**, and `CLAIM 011`'s existing flag — that *"dose-dependent"*
describes a continuum the panel refuses — stands.

### 5.2 🔴 The threshold has no measured expression difference behind it

LEGEND's manifest for `PMID 42422765`, entry 12 (figure attestation from prior session):

> "Two doses differing 2.1-fold are statistically indistinguishable in vector genomes and mRNA across four brain regions — seven of eight comparisons ns, the exception being hippocampal DNA — while producing opposite survival outcomes."

**This is the most consequential single fact in the whole node.** The two doses that separate death from ~80 %
survival **cannot be told apart by the measurements the paper makes**. Consequences, all of them:

- **The therapeutic window cannot currently be defined by a protein or transcript level**, because the assay that
  would define it does not resolve the two doses that matter.
- The paper's own explanation is *"mice from either treatment group that failed to survive exhibited reduced WWOX expression"* — which is a **post-hoc comparison of survivors against non-survivors**, i.e. selection-conditioned, and it rests on supplementary panels. Reinforcing that: **S5 explicitly marks one HD and three LD animals as dead**, so every later expression comparison is made among survivors.
- ⇒ **A minimum effective dose has been bracketed in vg but not in biology.** For a first-in-human programme that is the number a treating team would want and it does not exist.

### 5.3 The ceiling is not measured at all — and the same dose is simultaneously too much and too little

| Region | Achieved WWOX relative to WT | Direction |
|---|---|---|
| Cortex | **8.2×** (P300, HD); 4.6× (second P300 panel); up to **25.6×** with WPRE | 🔴 **over** |
| Hippocampus | **10.7×** (P300, HD); 4.7×; up to **22.3×** with WPRE | 🔴 **over** |
| Midbrain | 5.6× (P300); 3.1×; 11.6× with WPRE | over |
| **Cerebellum** | **1.4×** at P300 HD, **0.6×** on the second P300 panel; **0.2–0.7×** at P30 at both doses; 0.1–0.4× without WPRE | 🔴 **under — never reaches wild type at any dose or timepoint measured** |

🔴 **The window is not scalar, it is regional.** One ICV dose over-doses forebrain by roughly five- to eleven-fold
and **leaves the cerebellum below wild type**. That is directly consequential for the ataxia/SCAR12 axis, where
the cerebellum is the target organ — and it is the region where LEGEND's `DL-MECH-009` records WPRE giving the
largest boost (**16.7×** by Western, the highest of four regions), i.e. the element that was **removed** is the
one that most helped the region that is most under-dosed.

**Does anything in the literature bound the window from above? No.** `threshold`, `overexpress`, `supraphysio`
and `apopto` are all zero in the Obeid body. No toxicity endpoint was sought at 8–11× wild type. The tumour
non-finding belongs to the 2021 paper, is triply qualified (*gross*, *limited number*, *8–11 months*), and was
made in animals whose entire periphery remains WWOX-null. **The only upper-bound gesture in the whole programme
is precautionary, not empirical** — the WPRE removal.

### 5.4 Putting the two together

**Floor:** a hard, unexplained survival threshold between 1.23 and 2.63 × 10¹¹ vg, with no expression correlate.
**Ceiling:** unmeasured, with achieved levels durably 5–11× WT in forebrain and a 17-fold spread across human
lines. **⇒ The therapeutic window for `TX-007` is, as published, bounded below by an unexplained threshold and
unbounded above by anything anyone has measured.** That is not the same as saying the window is narrow — **it is
saying the window has never been drawn**, which is a different and more actionable statement. It is also, as the
node brief says, the single most decision-relevant question a treating team could ask about the therapy that
actually exists, and the honest answer is that the data to answer it were not collected.

**The window/age argument is not re-litigated here.** `DL-MECH-011` (efficacious window P1–P5 in mouse) and
`CLAIM 031` hold it; this section is orthogonal to it and does not restate it.

---

## 6. What LEGEND already knew · what is new

### 6.1 Already held — not re-derived

- `CLAIM 011` (line 202 ff.): the multi-domain rescue, **and** its flag that *"«dose-dependent» descrive un
  continuo dove il pannello mostra una soglia"*, with LD/HD vg values and the P20 hypoglycaemia observation.
- `DL-MECH-009`: WPRE as a **dose-sparing expression booster** (cortex 3.0×, hippocampus 3.0×, midbrain 5.5×,
  **cerebellum 16.7×**), and the explicit design tension *"dose-sparing vs rischio overexpression"* — including
  the noted contradiction between the review's *"WPRE removed to avoid overexpression"* and the primary's S3 data.
- `DL-MECH-010` (neuronal SynI sufficiency), `DL-MECH-011` (P1–P5 window), `DL-MOL-005` (durable P300 rescue).
- `FM-013` and `N-05`: *"neither too little nor too much WWOX"*; supraphysiological rescue is a risk, not a success.
- `mechanism_intervention_map.md` **line 412** already lists *"supraphysiological and regionally uneven long-term
  expression in survivors"* and the triply-qualified tumour non-finding under R-01's safety constraints.
- The 30 locators of `PMID 42397075` and the 29 of `PMID 42422765`, including entries 2, 12, 15, 22, 24, 25, 28
  and the prior session's **self-correction** at entry 25.

### 6.2 New in this node

1. 🔴 **The survival threshold has no measured expression difference behind it** — two doses differing 2.1-fold are
   statistically indistinguishable on vector genomes and mRNA in four brain regions (7 of 8 comparisons `ns`)
   while producing opposite survival outcomes. **`TX-007` has no biological definition of its minimum effective
   dose.** This is in the manifest but is carried nowhere in the therapeutic layer.
2. 🔴 **The window is regional, not scalar**: the same dose leaves forebrain at 4.6–10.7× WT and **cerebellum
   below WT at every dose and timepoint measured** — and the removed WPRE element is precisely the one that most
   boosted cerebellum (16.7×). Nobody has stated the cerebellar under-dosing as a translational problem for the
   ataxia axis.
3. 🔴 **The gradation across genotype classes is confounded by donor background, and the system's own
   within-genotype clone variance is significant** (two isogenic KO clones, `*` between them, ≈43 % vs ≈54 % on
   SOX2⁺MYC⁺/SOX2⁺). This is the argument that decides Task 2 and it is not written anywhere in LEGEND.
4. 🔴 **"The patient lines are near-normal" is a median statement over distributions whose whiskers reach ~41–44 %
   against a WT median of ~3 %** — and **WOREE carries a `*` on that very readout.** The near-normality has been
   propagated; the dispersion and the WOREE significance have not.
5. 🔴 **The cell-cycle phase distribution — the mechanistic bridge of the whole paper — is plotted without error
   bars or significance markers even in the knockout, and has never been measured in a patient line.**
6. ✅ **Field-density measurement on the safety question**: `(WWOX OR WOX1) AND (ectopic OR overexpression OR
   transfection) AND apoptosis AND (any neuronal term)` returns **2 records**, neither in a neuron, one of them a
   review. **There is no published experiment on WWOX overexpression toxicity in neurons.**
7. ✅ **Method finding**: the PMC extractor **deletes vector-genome exponents**. `"1.23 × 10vg"` is what the body
   returns. Any dose quoted from extracted text in this literature is wrong by orders of magnitude.

---

## 7. Corrections, with exact file and line coordinates

**W3-C1 — `TX-007`'s scoring line carries no dose-control or overexpression term.**
- **File:** `disease-models/wwox/therapeutics/therapeutic_strategies_current.md` · **line 98**
- **Exact current text:** `- **Scoring:** MATCH 3 · EVID 2 (strong preclinical + n=1 news; *not* 3 = no proven human efficacy) · TIME→patient 1–2 (company + FDA route exist; trial not yet open; n-of-1 compassionate route possible) · SAFETY 1–2 (AAV9 CNS: n=1, immunogenicity/dose/long-term unknown) · TIME-BUY 3 (causal lever) · **REVERS 0** (⚠️ irreversible — AAV persists) · ACTION 2 · PROTO-FIT 2`
- **Exact proposed replacement:** `- **Scoring:** MATCH 3 · EVID 2 (strong preclinical + n=1 news; *not* 3 = no proven human efficacy) · TIME→patient 1–2 (company + FDA route exist; trial not yet open; n-of-1 compassionate route possible) · SAFETY 1 (AAV9 CNS: n=1, immunogenicity/dose/long-term unknown; **and the therapy does not set an expression level — 4.6–10.7× WT in forebrain at P300, up to ~26× with WPRE, 0.4–7× across human organoid lines, cerebellum below WT at every dose, in a pro-apoptotic tumour suppressor whose overexpression toxicity in neurons has never been tested**) · TIME-BUY 3 (causal lever) · **REVERS 0** (⚠️ irreversible — AAV persists, **and an irreversible modality with no measured upper bound is a different object from one with a titratable dose**) · ACTION 2 · PROTO-FIT 2`
- **Why:** `REVERS 0` and uncontrolled overexpression compound each other and neither is stated next to the other.

**W3-C2 — `TX-007`'s progenitor caveat should be re-worded, per §3.**
- **File:** `disease-models/wwox/therapeutics/therapeutic_strategies_current.md` · TX-007 window/age caveat bullet
  (immediately following line 98)
- **Issue:** it says the therapy *"does NOT repair the progenitor defect"* without saying that the **lesion** is
  shared across genotype classes while the **magnitude of its consequence** is unresolved and confounded.
- **Proposed:** append — `⚠️ **Genotype-class status of this caveat, measured 2026-09-21:** the progenitor *lesion* (MYC activation in radial glia) is present in WOREE and SCAR12 patient-derived organoids at ~90% of the engineered knockout's magnitude, so the caveat is **not** an artefact of the CRISPR null. The *magnitude of its consequence* (cell composition, proliferation index) is much smaller in the patient lines — but **that gradation cannot be attributed to genotype**: the knockouts are isogenic clones on one background while the patient lines are different donors, no isogenic allelic series exists, and two isogenic knockout clones differ significantly from each other on the same readout. Leave the caveat general. See [`tx007_genotype_class_ceiling_20260921.md`](../analysis/tx007_genotype_class_ceiling_20260921.md).`

**W3-C3 — `CLAIM 011` records the floor and not the ceiling.**
- **File:** `disease-models/wwox/registries/claim_registry_current.md` · **line 205** (the `🔴 Flagged 2026-08-10` block of `CLAIM 011`)
- **Issue:** the block resolves the **threshold** at the low end and explicitly defers the other domains, but says
  nothing about the **upper** end — neither the P300 regional overexpression (8.2× cortex, 10.7× hippocampus) nor
  the finding that the two doses are statistically indistinguishable on vector genomes and mRNA in 7 of 8
  comparisons while producing opposite survival.
- **Proposed:** extend the existing append-only flag with a second paragraph carrying both, sourced to manifest
  `PMID42422765.json` entries **12** and **28**, and stating that **the minimum effective dose is bracketed in vg
  and not in biology**.

**W3-C4 — `therapy_levers.md` C2 (re-stating Wave 1 C-6 with the extra numbers this node adds).**
- **File:** `disease-models/wwox/analysis/therapy_levers.md` · **line 29**
- **Exact current text:** `- **C2. Proof that restoring WWOX reverses the phenotype.** In WOREE-derived brain organoids, WWOX re-expression corrected cortical/molecular CNS anomalies (PMID **34268881**, EMBO Mol Med 2021).`
- **Exact proposed replacement:** `- **C2. Restoring WWOX changes the phenotype — "corrected" is the authors' framing, not the panels'.** In WOREE-derived brain organoids WWOX re-expression improves cortical/molecular CNS readouts (PMID **34268881**), but the rescue is supraphysiological, ubiquitously promoted and **partial**, and in the 2026 organoid work (PMID **42397075**) it **does not set a level**: restored WWOX protein spans **0.4× to 7× wild type across lines given the same vector**, SATB2 mRNA in treated WOREE runs from wild-type level to **~11× above it**, and TCF-4 falls to **0.3×**. Displacement, in both directions — not normalisation.`

**W3-C5 (new) — the tumour non-finding is attributed to the wrong paper's era.**
- **Files:** `disease-models/wwox/analysis/mechanism_intervention_map.md` · **line 412** (R-01 safety row)
- **Issue:** the row is correct, and this is an addition rather than a fix: the triply-qualified tumour
  non-finding (*gross*, *limited number*, *8–11 months*) belongs to `PMID 34747138` (2021). **`PMID 42422765`
  (2026), the dose-ranging study that defines the clinical doses, reports no tumour surveillance at all** —
  `tumor` occurs three times in its body, all in the Introduction describing WWOX as a tumour suppressor.
- **Proposed:** add `; the 2026 dose-ranging study reports **no tumour surveillance of any kind**`.

---

## 8. Source attribution

Retrieved from **PubMed / PubMed Central**. Bodies for `PMID 42422765` and `PMID 34747138` were fetched and read
in this session; all figure- and panel-level values are **prior-session figure attestations from LEGEND's
receipt-backed locator manifests** and are labelled as such wherever they appear.

| PMID | Citation | DOI |
|---|---|---|
| 42397075 | Steinberg DJ, Zonca A, Abdellatif D *et al.* Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026 | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) |
| 42422765 | Obeid M *et al.* Neuron-specific WWOX gene therapy produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy. *Mol Ther Oncol* 2026 | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) |
| 34747138 | Repudi S *et al.* Neonatal neuronal WWOX gene therapy rescues Wwox-null phenotypes. *EMBO Mol Med* 2021 | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |
| 34268881 | Steinberg DJ *et al.* Modeling genetic epileptic encephalopathies using brain organoids. *EMBO Mol Med* 2021 | [10.15252/emmm.202013610](https://doi.org/10.15252/emmm.202013610) |
| 22534828 | Chang J-Y *et al.* TIAF1 self-aggregation in peritumor capsule formation… and cell death. *Cell Death Dis* 2012 — **abstract only; COS/cancer/neuroblastoma, not neurons; Chang/NCKU line, independence caution applies** | [10.1038/cddis.2012.36](https://doi.org/10.1038/cddis.2012.36) |
| 27999774 | HYAL-2–WWOX–SMAD4 Signaling in Cell Death and Anticancer Response — **review**, already in LEGEND | via PubMed (DOI not re-resolved in this session) |

---

**End.** Not medical advice. Read-only toward every canonical file; nothing promoted, nothing committed.
