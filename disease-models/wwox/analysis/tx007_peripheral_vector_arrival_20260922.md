# TX-007 — VECTOR ARRIVAL versus WWOX PROTEIN EXPRESSION in peripheral tissues

**Actor:** Scientist A · **Date:** 2026-09-22 · **Axis:** peripheral biodistribution (genome layer), not expression
**Scope:** `PMID 42422765` / `PMC13343157` (Obeid, Aqeilan et al. 2026) and `PMID 34747138` / `PMC8649866`
(Repudi & Aqeilan 2021) — the two AAV9-hSynI-WWOX arms in the **`Wwox`-null mouse (Aqeilan strain)**.

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, every registry,
> every queue, every ledger, every receipt and the state manifest. Nothing promoted, nothing committed,
> no `BATCH_COMMIT`, no receipt claimed, no git command executed, no external contact, no purchase.
>
> 🔴 **Nothing here is medical advice.** No molecule, no dose, no route, no schedule, no clinical framing.
> Every clinical question is `HUMAN_REQUIRED`.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> 🔴 **Alleles, drivers and species are never pooled.** `Wwox`-null (Aqeilan), `Wwox^ΔCre/ΔCre` (EIIA-Cre,
> Aldaz), the NCKU nulls, `gt/gt` hypomorph, `P47T` knock-in, Synapsin-Cre `S-KO`, Nestin-Cre `N-KO`,
> Alb-Cre `Wwox^hep−/−`, ACTA1 `Wwox^ΔSKM`, rat `lde/lde`, human WOREE and human SCAR12 are **different
> objects** and never share a row. Everything below concerns the **Aqeilan `Wwox`-null mouse** unless the
> row says otherwise.
>
> **Constructive continuation.** This file extends the original programme's own biodistribution question
> using the programme's own assay. Nothing here is offered as criticism of either paper: both report a
> peripheral result honestly, at the layer they measured it.

---

## 0 · Provenance — what I read, and the rule that governs every quotation below

🔴 **I did not read either primary body in this act.** `files/fulltext/` does not exist in this edition;
no external contact was made, and all contact is `HUMAN_REQUIRED`. **Every primary quotation in this file
is therefore tagged `SIBLING-ATTESTED` and carries the repository file and line it was taken from.** No
quotation is laundered into a first-hand read, and no number is relayed without its repo locator.

**Enumeration before filtering** (method bound of the brief, and the reason a previous wave was voided):
plain `ls disease-models/wwox/analysis/` — **166 entries** including 4 sub-directories (`data`,
`near_miss_cases`, `orchestration_reviews`, `scripts`) — and `ls -R disease-models/wwox/research/` —
24 top-level entries plus `commit_candidates` (113), `deepdive_manifests` (80), `fulltext_dossiers` (53),
`locator_audits` (1), `page_adjudications` (6 PMIDs), `pattern_audits` (2), `session_evaluations` (42).
**Both listings were read end to end before the first `grep`.** The files that turned out to carry the
decisive material — `cerebellum_layer_localisation_20260922.md` and
`purkinje_existing_material_experiment_20260922.md` — contain **neither** "peripheral" **nor** "biodistribution"
in their titles and would have been filtered out by a title-keyword sweep. That is the whole point of the bound.

### 0.1 The established finding, verified at source and NOT re-derived

| Element of the finding | Verified at | Verdict |
|---|---|---|
| vDNA quantified in **four brain regions only** | [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:56-62`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) — cortex/hippocampus/midbrain/cerebellum ✅ vDNA; spinal cord, sciatic nerve, liver ❌ | 🟢 **CONFIRMED** |
| The peripheral negative is a **PROTEIN** negative | [`:62`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) (liver, WB + IHC, both arms); [`:103`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) (2021 IHC: liver, pancreas, kidney, testis, ovary) | 🟢 **CONFIRMED** |
| The CNS-exclusivity premise is an **`INFERENZA`** from an expression assay | [`peripheral_phenotype_denominator_audit_20260922.md:348-352`](peripheral_phenotype_denominator_audit_20260922.md) §4.1 — `L3` quoted, then *"⇒ **The vector is not in the periphery.** Anything that changes there changes **through the brain**."* | 🟢 **CONFIRMED** — the arrow is the inference |
| It sits beside a measured fact: **WWOX protein IS in sciatic nerve and spinal cord** | [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:60-61`, `:172-173`](tx007_regional_wwox_forebrain_cerebellum_20260922.md); [`therapeutic_translation_second_pass.md:591`](therapeutic_translation_second_pass.md) (spinal cord 0.8–1.3× WT; sciatic nerve unquantified, seven animals, strong→barely detectable) | 🟢 **CONFIRMED** |
| Already named as a frontier item | [`tx007_purkinje_frontier_20260922.md:167`](tx007_purkinje_frontier_20260922.md) `B-f1`; [`:225-256`](tx007_purkinje_frontier_20260922.md) proposal `P1`; [`:383`](tx007_purkinje_frontier_20260922.md) `FR-1` | 🟢 **CONFIRMED — this file deepens `B-f1`/`P1`, it does not re-open them** |

🔴 **Lines already exhausted in the repository and deliberately NOT re-derived here:** the dose-unit audit
(`HD/LD = 2.1382`, closed); the cerebellar under-expression finding; the `3–16.7×` S3E attribution
contradiction; the dose non-monotonicity premise; the WPRE scope question (resolved as a scope difference,
[`tx007_regional_wwox_forebrain_cerebellum_20260922.md:380-403`](tx007_regional_wwox_forebrain_cerebellum_20260922.md)).

---

## 1 · TISSUE INVENTORY — what was demonstrably harvested, and what class of material that implies

### 1.1 The three-grade rule this section enforces on itself

🔴 **A tissue inventory is worthless if "harvested", "blotted" and "probably banked" are merged**, because
they license different next moves. Grades are assigned on evidence of *the measurement*, not on plausibility
of *the archive*.

| Grade | Means |
|---|---|
| 🟢 **DEFINITELY EXISTS** | A measurement on that tissue is reported in the paper. The tissue was **necessarily** dissected out of an animal in that arm. This is an inference about the past that cannot fail. |
| 🟡 **PROBABLY EXISTS** | The tissue is named in a Methods protocol, or is implied by a sentence that names it in a list with measured tissues, but no panel is assigned to it. |
| 🔴 **NOT ESTABLISHED** | Nothing in the repository places that tissue in a dissection. It may have been taken; the repository cannot say. |

⚠️ **All three grades concern whether the tissue was ever *in a tube*. None of them concerns whether anything
is still in a freezer in 2026.** That second question is `A-f4` and is stated as unknowable in §1.4.

### 1.2 `PMID 42422765` (Obeid 2026) — peripheral and extra-forebrain tissues

| Tissue | Measurement reported | Arms | Age | Grade | Repo locator (file:line) |
|---|---|---|---|---|---|
| **Liver** | WWOX immunoblot **and** IHC, **negative** | 🟢 **BOTH LD and HD** | unstated | 🟢 **DEFINITELY EXISTS** | [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:62`](tx007_regional_wwox_forebrain_cerebellum_20260922.md), [`:174`](tx007_regional_wwox_forebrain_cerebellum_20260922.md); arm attribution [`tx007_per_arm_delivery_reconstruction_20260922.md:154`](tx007_per_arm_delivery_reconstruction_20260922.md) |
| **Sciatic nerve** | WWOX immunoblot + IHC, **positive**, unquantified | 🔴 **HD only** | 🔴 unstated | 🟢 **DEFINITELY EXISTS (HD)** · 🔴 **NOT ESTABLISHED (LD)** | [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:61`](tx007_regional_wwox_forebrain_cerebellum_20260922.md), [`:173`](tx007_regional_wwox_forebrain_cerebellum_20260922.md); band range [`therapeutic_translation_second_pass.md:591`](therapeutic_translation_second_pass.md) |
| **Spinal cord** | WWOX immunoblot + IHC, **positive** (0.8–1.3× WT) | 🔴 **HD only** | ~3 mo, P240, P300 | 🟢 **DEFINITELY EXISTS (HD)** · 🔴 **NOT ESTABLISHED (LD)** | [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:60`](tx007_regional_wwox_forebrain_cerebellum_20260922.md), [`:172`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) |
| **Blood (whole / serum)** | blood glucose, P10 / P20 / P30 | 🟢 **BOTH** | P10–P30 | 🟢 **blood was drawn** · 🔴 **whether any serum was banked: NOT ESTABLISHED** | [`tx007_per_arm_delivery_reconstruction_20260922.md:158`](tx007_per_arm_delivery_reconstruction_20260922.md) |
| **Gonad / reproductive tract** | fertility testing, **20 breeding cages per group** | 🔴 **HD only** | adult | 🔴 **NOT ESTABLISHED** — a breeding assay dissects nothing | [`tx007_per_arm_delivery_reconstruction_20260922.md:160`](tx007_per_arm_delivery_reconstruction_20260922.md) |
| **DRG** | AAV infection **in vitro**, E13.5 culture | n/a | E13.5 | 🔴 **NOT an in-vivo biodistribution tissue** | [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:86`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) |
| Heart, kidney, spleen, lung, muscle, pancreas, gut, bone | 🔴 **none** | — | — | 🔴 **NOT ESTABLISHED** | absence across [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:54-62`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) and the 80-cell grid of [`peripheral_phenotype_denominator_audit_20260922.md:83-92`](peripheral_phenotype_denominator_audit_20260922.md) |

**SIBLING-ATTESTED**, `PMID 42422765` Results, from
[`PMID42422765_partial_locators.md:253`](../research/fulltext_dossiers/PMID42422765_partial_locators.md):
> "WWOX protein was also detected in the sciatic nerve of HD-treated mice (Figures S6E–S6G), thus supporting functional relevance in the peripheral nervous system. In contrast, no WWOX expression was detected in the liver following either LD or HD treatment"

🎯 **The single most useful line in the inventory.** That one sentence dissects **two** peripheral organs out
of the same animals, and reports one positive and one negative — so the programme's own peripheral protein
result is **not** uniform, and the tissues to ask the genome question of are already named by the authors.

### 1.3 `PMID 34747138` (Repudi 2021) — a broader organ set, an older archive

| Tissue | Measurement | Arms | Age | Grade | Repo locator |
|---|---|---|---|---|---|
| **Liver, pancreas, kidney, testis, ovary** | transgene expression, **negative** (Appendix Fig S2B–C) | KO+AAV9-hSynI-mWwox / -hWWOX, and controls | **P17 AND 9 months** | 🟢 **DEFINITELY EXISTS — five organs, two ages** | [`PMID34747138_partial_locators.md:56-58`](../research/fulltext_dossiers/PMID34747138_partial_locators.md) `L3`; inventory row [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:103`](tx007_regional_wwox_forebrain_cerebellum_20260922.md); material status [`peripheral_phenotype_denominator_audit_20260922.md:222`](peripheral_phenotype_denominator_audit_20260922.md) T1-b |
| **Testis (Leydig)** | histology, Appendix Fig S4A | rescued | P17 | 🟢 **DEFINITELY EXISTS** | [`PMID34747138_partial_locators.md:62-70`](../research/fulltext_dossiers/PMID34747138_partial_locators.md) `L4` |
| **Optic nerve** | EM, g-ratio | KO/WT | P17 | 🟢 **DEFINITELY EXISTS** | [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:102`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) |
| **Blood** | glucose, from second week | all | ~P14 onward | 🟢 **drawn** · 🔴 banking NOT ESTABLISHED | [`PMID34747138_partial_locators.md:73-75`](../research/fulltext_dossiers/PMID34747138_partial_locators.md) |
| **Bone** | 🔴 **NONE — no quoted sentence exists anywhere in this repository** | — | — | 🔴 **NOT ESTABLISHED, and the assertion that it was measured is UNANCHORED** | [`peripheral_phenotype_denominator_audit_20260922.md:362-386`](peripheral_phenotype_denominator_audit_20260922.md) §4.3 |
| Spinal cord, sciatic nerve, heart, spleen, lung, muscle | 🔴 none | — | — | 🔴 **NOT ESTABLISHED** | [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:105-107`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) |

🔴 **The cortical-bone claim must not be carried into this axis.** Scientist G established that
*"cortical bone comparable to wild-type"* entered this repository through an interpretive paragraph and has
**no verbatim locator in any surface** ([`peripheral_phenotype_denominator_audit_20260922.md:362-386`](peripheral_phenotype_denominator_audit_20260922.md)).
It is `COULD NOT ESTABLISH`, and no bone tissue is inventoried here.

### 1.4 🔴 Material class — where DNA would plausibly remain, and where the repository cannot say

**This sub-section is where guessing is most tempting and most damaging, so every row states its evidence
class explicitly.**

| Paper / material | What the Methods establish (SIBLING-ATTESTED) | DNA-competent? | Verdict |
|---|---|---|---|
| **2026 — brain regions for vDNA** | *"tissue samples (up to 25 mg) were lysed in ATL buffer … DNA integrity and concentration were assessed … For qPCR, 50 ng of DNA template was used per reaction"* — [`cerebellum_layer_localisation_20260922.md:212-215`](cerebellum_layer_localisation_20260922.md), first-hand to Scientist C | 🟢 by construction | 🟢 **A DNA-extraction workflow demonstrably existed in this lab, for this paper.** Whether extracted DNA was retained: 🔴 **NOT ESTABLISHED** |
| **2026 — tissue for RNA** | *"Total RNA was isolated from **non-perfused tissue** using TRIzol"* — [`cerebellum_layer_localisation_20260922.md:244`](cerebellum_layer_localisation_20260922.md) | 🟡 TRIzol interphase retains DNA, **if the interphase was kept** | 🟡 **PROBABLY — and only if kept.** Never assume; TRIzol interphase is routinely discarded |
| **2026 — perfused, sectioned cohort** | *"(WT, KO, and KO injected mice) at different ages (P10-P180) … transcardially perfused using 4% PFA/PBS … Sagittal brain sections (14 μm) … stored at −80 °C … FFPE sagittal tissue sections (14 μm) … Fresh coronal sections … vibratome (50 μm)"* — [`purkinje_existing_material_experiment_20260922.md:207-211`](purkinje_existing_material_experiment_20260922.md) | 🟡 **fixed** material: FFPE and PFA/OCT DNA is fragmented and cross-linked | 🟡 **PROBABLY EXISTS as FIXED material only.** 🔴 The Methods name **brains**; they do **not** name peripheral organs in this perfusion protocol |
| **2026 — liver / sciatic nerve / spinal cord** | blotted **and** IHC-stained ([`:60-62`](tx007_regional_wwox_forebrain_cerebellum_20260922.md)) ⇒ **both a lysate route and a fixed route were used on these tissues** | 🟡 lysate: 🔴 unknown chemistry; fixed: 🟡 FFPE/OCT DNA-competent at short amplicon | 🟡 **PROBABLY EXISTS in at least one of the two classes** — and 🔴 **which one is NOT ESTABLISHED** |
| **2021 — liver, pancreas, kidney, testis, ovary** | negative expression panels at two ages; the 2021 Methods heading list **contains no immunoblot and no tissue-extraction section at all** — [`purkinje_cheapest_path_and_community_followup_20260922.md:384`](purkinje_cheapest_path_and_community_followup_20260922.md) | 🔴 no nucleic-acid workflow of any kind in that paper beyond prep titration | 🔴 **The 2021 archive is an IMAGE archive.** A frozen-lysate class is **NOT ESTABLISHED** and, on the Methods heading list, has no reason to exist |

> 🎯 **The inventory's operational verdict.** For the genome question, the material that matters is the
> **2026** liver / sciatic nerve / spinal cord set, because (a) those three tissues were demonstrably
> dissected out of treated animals, (b) the same paper ran a DNA-extraction-and-qPCR workflow on other
> tissues from the same programme, and (c) the ATL-lysis protocol is tissue-generic — the quoted Methods
> sentence sets a **mass** limit (25 mg), not a tissue restriction. **The 2021 five-organ set is broader and
> covers two ages, but its paper has no nucleic-acid workflow, so it is the weaker archive for this question.**
>
> 🔴 **And the bound that governs every row: whether ANY of this material still exists is `A-f4`, recorded as
> `HUMAN_REQUIRED` and "unknowable from a repository"** ([`tx007_purkinje_frontier_20260922.md:146`](tx007_purkinje_frontier_20260922.md)).
> **This file does not guess it, and every "no new animals" statement below is explicitly conditional on it.**

---

## 2 · METHOD REUSABILITY — is the vector-genome qPCR recoverable?

### 2.1 🎯 The headline: **substantially YES, and more than the record assumed** — the primer pair is in the repository

**SIBLING-ATTESTED**, `PMID 42422765` Materials and Methods, quoted first-hand by Scientist C at
[`cerebellum_layer_localisation_20260922.md:212-215`](cerebellum_layer_localisation_20260922.md):

> "tissue samples (up to 25 mg) were lysed in ATL buffer … DNA integrity and concentration were
> assessed prior to downstream applications by using DeNovix (DS-11FX+). **For qPCR, 50 ng of DNA
> template was used per reaction.** The primer sequences were as follows: forward
> 5′ GCTCTCTTAAGGTAGCCCCG 3′, reverse 5′ CGCCTCATCCTGGTCCTAAA 3′."

🔴 **No primer sequence is invented anywhere in this file.** The pair above is **published by the authors and
transcribed into this repository**; it is reproduced here as a locator, not as a design. Anyone reusing it
must re-read it at the source before synthesis.

### 2.2 The method, component by component

| Component | Status | Value / what is known | Locator |
|---|---|---|---|
| **Primer pair (vDNA assay)** | 🟢 **RECOVERABLE** | forward `5′ GCTCTCTTAAGGTAGCCCCG 3′`, reverse `5′ CGCCTCATCCTGGTCCTAAA 3′` | [`cerebellum_layer_localisation_20260922.md:214-215`](cerebellum_layer_localisation_20260922.md) |
| **What that amplicon TARGETS** | 🔴 **METHODS_INVISIBLE** | The paper states the sequences and **not** the element they sit in. The separate *titration* assay is stated to use **bGH** primers — *"Viral titers were determined by RT-qPCR using bGH primers"* ([`tx007_per_arm_delivery_reconstruction_20260922.md:169`](tx007_per_arm_delivery_reconstruction_20260922.md)) — but **nothing states that the tissue assay uses the same target**, and the two are different experiments. 🔴 **Do not assume the tissue amplicon is bGH.** | as cited |
| **Template mass per reaction** | 🟢 **RECOVERABLE** | **50 ng DNA** | [`:213-214`](cerebellum_layer_localisation_20260922.md) |
| **Tissue input** | 🟢 **RECOVERABLE** | **up to 25 mg**, ATL-buffer lysis (a proteinase-K/column chemistry) | [`:212`](cerebellum_layer_localisation_20260922.md) |
| **DNA quantitation instrument** | 🟢 **RECOVERABLE** | DeNovix DS-11FX+ | [`:212-213`](cerebellum_layer_localisation_20260922.md) |
| **Host reference amplicon / normalising gene** | 🔴 **DOES NOT EXIST** — *validated negative* | `reference gene` 0, `single-copy` 0, `Actb`/`Gapdh`-as-DNA-reference 0 tokens in the served body | [`cerebellum_layer_localisation_20260922.md:217-218`](cerebellum_layer_localisation_20260922.md) |
| **Standard curve / absolute quantification** | 🔴 **DOES NOT EXIST** — *validated negative* | `standard curve` 0, `absolute quant` 0, `copies` 0, `diploid` 0 | [`:217-218`](cerebellum_layer_localisation_20260922.md), census [`:63-67`](cerebellum_layer_localisation_20260922.md) |
| **Plotted y-axis definition** | 🔴 **NOT READABLE** | Fig 5A–5D caption repo-attested as *"normalized to WT levels"* — 🔴 **undefined for vDNA, because WT animals receive no vector**, and the `RI` arms are **vehicle**, not vector | [`fold_of_wt_is_undefined_for_vdna_20260922.md:26-37`](fold_of_wt_is_undefined_for_vdna_20260922.md); [`tx007_regional_wwox_forebrain_cerebellum_20260922.md:565-568`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) |
| **Cycling conditions, polymerase, chemistry (probe vs dye), replicates** | 🔴 **METHODS_INVISIBLE** | nothing in the repository | — |
| **`n` per arm for Fig 5A–5D** | 🔴 **ABSENT** | `n =` / `n=` → **0 tokens in 48,780 chars of served body**, measured | [`cerebellum_layer_localisation_20260922.md:63`](cerebellum_layer_localisation_20260922.md); [`tx007_per_arm_delivery_reconstruction_20260922.md:164`](tx007_per_arm_delivery_reconstruction_20260922.md) |
| **Perfusion status of the DNA tissue** | 🔴 **NOT STATED.** (Stated only for RNA: *"non-perfused tissue"*.) | 🔴 This matters and is taken up in §3.1 | [`cerebellum_layer_localisation_20260922.md:244`, `:259`](cerebellum_layer_localisation_20260922.md) |
| **2021 tissue vDNA method** | 🔴 **DOES NOT EXIST** | the 2021 paper's only nucleic-acid step is prep titration; its Methods heading list has no tissue-extraction section | [`purkinje_cheapest_path_and_community_followup_20260922.md:384`](purkinje_cheapest_path_and_community_followup_20260922.md) |

### 2.3 Verdict

> 🟢 **The assay is reusable as a *relative* measurement without inventing anything**: the primer pair,
> template mass, tissue-mass limit, lysis chemistry and quantitation instrument are all recoverable from the
> repository. A peripheral tissue can be run **on the same plate, in the same design, against the same
> primers** as the four brain regions.
>
> 🔴 **It is NOT reusable as an *absolute* measurement, and it never was — not even in the brain.** No host
> reference amplicon, no standard curve, no stated copy units, and a y-axis whose printed denominator is
> undefined for a vector quantity. **The published brain vDNA panel itself supports only within-panel ratios**
> ([`cerebellum_layer_localisation_20260922.md:234-240`](cerebellum_layer_localisation_20260922.md)).
>
> 🎯 **Consequence, and it is a design instruction rather than a complaint: the peripheral extension must add
> the host reference amplicon and the standard curve that the original did not have** — otherwise a peripheral
> reading inherits an undefined axis and cannot be compared to the brain panel at all. **That addition is what
> converts a repeat into an answer**, and it is the difference between LEVEL 0 and LEVEL 1 in §6.

---

## 3 · INTERPRETATION LIMITS — stated before any outcome is contemplated

### 3.1 Normalisation: copy number **per diploid genome** requires a normaliser, and this assay has none

**Why it matters.** "Vector genomes per cell" is a **ratio of two measurements**: vector amplicon copies and
host genome copies in the same reaction. The 2026 assay measures only the first.

🟢 **What the fixed-mass design already buys, and it is more than it looks.** Scientist C's Methods finding is
that 50 ng of murine genomic DNA is a **fixed number of nuclei** (~6 pg per diploid genome ⇒ ~8.3 × 10³
nuclei), so a vector amplicon measured against fixed DNA **mass** is already approximately a per-nucleus
quantity — *"cell-density normalisation is built into the assay design"*
([`cerebellum_layer_localisation_20260922.md:222-229`](cerebellum_layer_localisation_20260922.md)).

🔴 **What it does not buy.** Fixed *input* mass is not the same as *verified* input mass. Without a host
amplicon there is no per-well check that 50 ng was actually loaded, no correction for inhibitors, and no
conversion to copies. **And fixed-mass normalisation is weakest exactly where this file wants to go:**

- **Liver** is polyploid in adult mouse. A large hepatocyte fraction is tetraploid or octoploid, so a fixed
  DNA mass corresponds to **fewer nuclei and far fewer cells** in liver than in brain. A per-nucleus reading
  from liver is not comparable to a per-nucleus reading from cortex without a ploidy statement.
- **Sciatic nerve** is dominated by Schwann-cell and fibroblast nuclei with a large acellular myelin and
  collagen mass; DNA yield per mg is low and variable.
- **Spinal cord** is the closest to the brain compartments and the most directly comparable.

> **Which normaliser, and why.** A **single-copy autosomal nuclear host gene** — the standard class for AAV
> biodistribution, and the class the census shows is absent here (`single-copy` 0 tokens). Two properties are
> load-bearing: it must be **single-copy** (so copies ÷ 2 gives diploid genomes directly) and **nuclear**
> (a mitochondrial normaliser varies by orders of magnitude between liver, nerve and brain and would
> manufacture a spurious tissue gradient). 🔴 **`Gapdh` and `Actb` are the wrong choice**: both have
> processed pseudogenes in mouse, so a "gene" amplicon is not a reliable single-copy target. 🔴 **An rRNA or
> total-RNA normaliser is categorically wrong here** — it is the denominator of the *transcript* panel, and
> the two are non-interconvertible ([`cerebellum_layer_localisation_20260922.md:252-257`](cerebellum_layer_localisation_20260922.md)).
> **This file does not name a specific gene**, because the correct choice depends on the assay platform and
> must be validated, and naming one from memory would be exactly the invention the brief forbids.

⚠️ **Perfusion is a normalisation problem too, not only a contamination problem** — see §3.3.

### 3.2 Matrix-matched blanks — and the repository already establishes that they exist

🟢 **The programme has vehicle-injected arms in both genotypes:** `KO+RI` and `WT+RI`, where
*"RI"* = **reference item** = *"PBS with 5% sorbitol and 0.001% pluronic F-68"*
([`fold_of_wt_is_undefined_for_vdna_20260922.md:26-33`](fold_of_wt_is_undefined_for_vdna_20260922.md);
arms listed at [`tx007_per_arm_delivery_reconstruction_20260922.md:194-195`](tx007_per_arm_delivery_reconstruction_20260922.md)).

> 🎯 **The very fact that closed the "fold-of-WT" escape route opens this one.** `RI` being vehicle is fatal
> to normalising vDNA *to WT* — and it is exactly what makes `KO+RI` and `WT+RI` the **correct matrix-matched
> vector-free blanks** for a peripheral arrival assay. **They are guaranteed zero-vector animals that went
> through the identical surgery, at the identical age, in the identical facility.** No better blank exists.

**Blank requirements, stated so that a null result is interpretable:**

| Blank | Why it is needed | What a positive signal in it would mean |
|---|---|---|
| **`KO+RI` peripheral tissue** | same genotype, same matrix, same surgery, zero vector | contamination in the workflow — **the whole run is void** |
| **`WT+RI` peripheral tissue** | controls for host-genome background and any primer cross-reactivity with the *endogenous* mouse/human locus | primer non-specificity; the amplicon is not vector-exclusive |
| **No-template control** | reagent contamination | standard |
| 🔴 **A spiked matrix control — vector-free peripheral tissue plus a known vector-genome input** | **This is the one the original brain assay did not need and the peripheral extension does.** It establishes recovery and inhibition **per tissue**, because liver and nerve lysates inhibit qPCR differently from brain | a low recovery here rescues a false negative from being read as "absent" |

🔴 **Without the spiked matrix control, "genomes ABSENT" in liver or nerve is not interpretable**, because an
absent signal and a failed extraction are the same number.

### 3.3 Residual blood and plasma — the confound that most threatens a POSITIVE

**The vector was injected into an animal; vector particles circulate.** A tissue reading includes whatever
vector is in the blood **inside** that tissue at the moment of harvest.

- 🔴 **The 2026 RNA tissue is stated to be non-perfused** ([`cerebellum_layer_localisation_20260922.md:244`, `:259`](cerebellum_layer_localisation_20260922.md));
  the perfusion status of the **DNA** tissue is 🔴 **NOT STATED anywhere in the repository**. The separate
  perfused cohort described at [`purkinje_existing_material_experiment_20260922.md:207-211`](purkinje_existing_material_experiment_20260922.md)
  is the **histology** cohort, and its protocol names **brains**.
- **Direction of bias:** blood contamination can only **add** vector signal, so it biases toward a false
  positive and **cannot** manufacture a false negative. 🎯 **This makes the two outcomes asymmetric in
  strength: an ABSENT result is robust to this confound; a PRESENT result is not.**
- **Tissues differ enormously in blood content.** Liver holds a large blood volume; peripheral nerve holds
  little. So an unperfused liver is the **most** contaminated reading available and an unperfused sciatic
  nerve among the least.
- **Mitigations, in order of strength:** (1) use perfused material if it exists — status unknown;
  (2) measure a **blood/plasma vector level from the same animal** on the same plate, so the tissue reading
  can be expressed against it; (3) report a **haemoglobin or erythroid-DNA marker per sample** as a blood-content
  covariate. ⚠️ Option (2) requires banked blood, which is 🔴 `NOT ESTABLISHED` (§1.2).
- ⚠️ At P30 the injection was ~30 days earlier and at P240/P300 ~8–10 months earlier, so circulating vector is
  expected to be far below its acute level. **That is an expectation from AAV pharmacokinetics, `PREMISE:
  DEFAULT_FROM_TEXTBOOK`, and neither paper measures it.** It reduces but does not remove the confound.

### 3.4 Episomal versus integrated — what a qPCR signal is and is not

- rAAV genomes persist overwhelmingly as **episomal circular concatemers** in post-mitotic cells; integration
  is a minority event. **A qPCR amplicon cannot tell the two apart** — it counts amplifiable templates.
- 🔴 **This matters most for the periphery and cuts in the direction of a false negative.** Peripheral tissues
  with proliferating compartments — liver in a growing animal, and any mitotic cell in nerve or cord — **dilute
  episomal genomes with every division**. So a tissue can have been transduced at P0 and read as vector-free at
  P30. ⚠️ Note the repository already uses exactly this argument for the **cerebellum**, where dividing granule
  precursors are named as an expected dilution sink
  ([`tx007_regional_wwox_forebrain_cerebellum_20260922.md:470-473`](tx007_regional_wwox_forebrain_cerebellum_20260922.md)).
  **The same logic transfers to liver, and the repository has not previously applied it there.**
- ⇒ **"Genomes absent at P30" is not "the vector never arrived."** It is *"amplifiable vector genomes are below
  the limit of detection in this tissue at this age."* A younger timepoint would be a different measurement.
- 🟢 **What could separate them if it ever mattered:** a linear-versus-circular discrimination (e.g. exonuclease
  pre-treatment) or an integration-site assay. **Both are out of scope here and neither is needed to answer the
  arrival question** — noted so that a later actor does not read a qPCR number as an integration statement.

### 3.5 Limit of detection — the number that decides whether "absent" means anything

🔴 **A negative without a stated LOD is not a result.** The original brain assay has **no standard curve**, so
it has **no stated LOD at all** ([`cerebellum_layer_localisation_20260922.md:217-218`](cerebellum_layer_localisation_20260922.md)).
Any peripheral extension must state, per tissue:

1. the **standard-curve range and efficiency**, from a plasmid or vector-genome dilution series;
2. the **LOD and LOQ in copies per reaction**, converted to **copies per diploid genome** using the host
   amplicon of §3.1;
3. the **recovery fraction** from the spiked matrix control of §3.2, per tissue;
4. the **number of wells and animals** at which the negative is declared — noting that the parent paper reports
   `n` for nothing (`n =` → 0 tokens).

⇒ **The strongest honest form of a negative is: "below X copies per diploid genome, at Y% recovery, in N
animals per arm."** Anything less is an absence of evidence.

### 3.6 🔴 Genome presence does NOT imply transduction of a given cell type

**This is the limit most likely to be over-read downstream, so it is stated as four separate failures:**

1. **Tissue ≠ cell type.** A liver reading is hepatocytes + Kupffer + endothelium + blood; a nerve reading is
   Schwann cells + fibroblasts + endothelium + axons whose nuclei are elsewhere. A bulk genome count assigns
   nothing to any of them.
2. **Genome ≠ transcript ≠ protein.** The hSynI promoter is a **neuron-specific** element; a genome in a
   hepatocyte is a genome in a cell that should not transcribe it. **Silence is the design, not a failure.**
3. **Cell-associated ≠ intracellular.** Extracellular or surface-bound capsid contributes amplifiable DNA.
4. **Nerve is a special case.** The sciatic nerve contains **axons of neurons whose cell bodies sit in spinal
   cord and DRG**. WWOX **protein** in sciatic nerve is therefore fully explicable by **axonal transport from a
   transduced central or ganglionic neuron**, with **no local transduction whatever**. 🎯 **So the existing
   sciatic-nerve protein positive is already compatible with a completely vector-free nerve** — which is
   precisely why the genome measurement is informative rather than confirmatory.

⚠️ **And the reciprocal bound, for symmetry:** the sciatic-nerve WWOX protein positive is
**unquantified against WT and reported in HD only**, with band intensity ranging from strong to barely
detectable across seven animals ([`therapeutic_translation_second_pass.md:591`](therapeutic_translation_second_pass.md);
[`tx007_regional_wwox_forebrain_cerebellum_20260922.md:571`](tx007_regional_wwox_forebrain_cerebellum_20260922.md)).
**It is a detection statement, not a magnitude**, and this file does not upgrade it.

---

## 4 · THE FOUR OUTCOMES — pre-stated, with what each licenses and what it does not

🔴 **Written before any measurement exists, per the preregistration primitive.** Each outcome is stated with
its licence **and its explicit non-licence**, because the failure mode on this axis is an over-read of a
delivery number into a mechanism.

### 4.1 Outcome A — genomes **ABSENT** (at or below the matrix-matched blank, with a stated LOD)

| | |
|---|---|
| 🟢 **What CHANGES in the disease model** | The load-bearing premise *"the vector is not in the periphery, therefore anything changing there changes through the brain"* ([`peripheral_phenotype_denominator_audit_20260922.md:352`](peripheral_phenotype_denominator_audit_20260922.md)) is **promoted from `INFERENZA` to `DATO`, at the genome layer**. The glucose rescue becomes a **demonstrated central-control effect** rather than a protein-blot inference. `CLAIM 036`'s systemic confounder → mediator re-reading ([`PMID34747138_partial_locators.md:85-92`](../research/fulltext_dossiers/PMID34747138_partial_locators.md)) gains its strongest single support. Frontier item `B-f1` retires permanently. |
| 🔴 **What does NOT change** | Nothing about **causality** — CNS-restricted delivery does not show that the brain *causes* the peripheral correction; it removes one alternative. Nothing about the **sciatic-nerve and spinal-cord protein positives**, which remain and now demand the axonal-transport reading of §3.6(4). Nothing about **Purkinje cells**, the cerebellar deficit, the dose non-monotonicity, or any of the 48 never-measured peripheral analyte cells ([`peripheral_phenotype_denominator_audit_20260922.md:101-107`](peripheral_phenotype_denominator_audit_20260922.md)). Nothing about the **2021** arm unless 2021 material is run. |
| ⚠️ **Residual risk** | Episomal dilution (§3.4) and extraction failure (§3.2) both produce this result spuriously. **A negative is only as strong as its spiked-recovery control.** |

### 4.2 Outcome B — genomes **PRESENT**, protein **ABSENT**

| | |
|---|---|
| 🟢 **What CHANGES** | 🎯 **The peripheral negative is reclassified from a biodistribution result to an EXPRESSION/OUTPUT result.** The record currently collapses *arrival* and *expression* into one word — "no WWOX expression was detected in the liver" — and this outcome splits them. It is a **positive result for the promoter**: hSynI restricting output in a non-neuronal tissue is the construct working exactly as designed, and that is a **transferable safety and design datum** rather than a problem. The premise in §4.1 must then be **re-derived** rather than assumed, and a **direct peripheral contribution** to any peripheral endpoint becomes a live alternative that current reasoning excludes by fiat. |
| 🔴 **What does NOT change** | **Genomes are not transcripts.** This outcome does **not** show the periphery is transduced-and-functional, does **not** show any peripheral cell makes WWOX, and does **not** overturn the glucose result, which stands on its own arm-separating statistics at P20 ([`peripheral_phenotype_denominator_audit_20260922.md:358`](peripheral_phenotype_denominator_audit_20260922.md)). It does **not** identify which peripheral cell type holds the genomes (§3.6). It does **not** make the periphery a therapeutic target. |
| 🎯 **The one thing it would immediately license** | A **peripheral RT-qPCR** on the same material, using the published transcript primer pair ([`cerebellum_layer_localisation_20260922.md:246`](cerebellum_layer_localisation_20260922.md)) — because "genomes present, protein absent" makes *transcript* the next cheapest discriminating layer, and that assay also already exists. |

### 4.3 Outcome C — genomes **PRESENT**, protein **PRESENT**

| | |
|---|---|
| 🟢 **What CHANGES** | The **CNS-only rescue reading** must be re-evaluated for **that tissue**. Where this is most likely to occur is **spinal cord and sciatic nerve**, which already carry protein positives — and there the outcome would resolve §3.6(4): local transduction, not axonal transport. It would also make **safety** framing load-bearing: a neuron-restricted construct that transduces and expresses in peripheral tissue changes what a biodistribution package must contain. |
| 🔴 **What does NOT change** | **It does not make the peripheral phenotypes peripherally driven.** Correlated presence is not contribution. It does **not** touch the liver negative, which is a *both-arm* protein result ([`tx007_per_arm_delivery_reconstruction_20260922.md:154`](tx007_per_arm_delivery_reconstruction_20260922.md)) and would have to be overturned separately. It does **not** alter the glucose, fertility or survival results, which are organismal endpoints. 🔴 **Critically, it does not license reinterpreting the 2021 paper**, whose five-organ negative is a different vector, different dose, different ages and different animals ([`tx007_regional_wwox_forebrain_cerebellum_20260922.md:215-217`](tx007_regional_wwox_forebrain_cerebellum_20260922.md)) — **never pooled**. |
| ⚠️ **Most likely benign explanation, to be excluded first** | Residual blood (§3.3) plus, for spinal cord, the fact that spinal cord is **CNS tissue continuous with the injected compartment** — a positive there is barely surprising and should be scored as a *delivery-extent* result, not a *peripheral* one. 🔴 **Spinal cord must be scored separately from liver and sciatic nerve for exactly this reason.** |

### 4.4 Outcome D — **MATERIAL NOT AVAILABLE**

| | |
|---|---|
| 🟢 **What CHANGES** | **Nothing in the disease model.** The premise stays `INFERENZA`, the gap stays open, and the finding is about the archive rather than the biology. |
| 🟢 **What it nonetheless produces** | A **retention answer for `A-f4`**, which is currently `HUMAN_REQUIRED` and blocks the "no new animals" clause of **every** existing-material proposal in this file and its siblings ([`tx007_purkinje_frontier_20260922.md:146`](tx007_purkinje_frontier_20260922.md)). One answer unblocks or closes several proposals at once, so the enquiry has value whichever way it resolves. |
| 🔴 **PARK, with an explicit `REVIVAL_TRIGGER`** | Revive `B-f1`/this file on **any** of: (1) any statement of tissue, DNA or block retention from the 2026 or 2021 programme; (2) any WWOX gene-therapy cohort **already being generated and terminated**, to which peripheral tissue collection can be attached at zero additional animals — the same hook as `T2-d` ([`peripheral_phenotype_denominator_audit_20260922.md:233`](peripheral_phenotype_denominator_audit_20260922.md)); (3) publication of **any** AAV9-hSynI biodistribution dataset in any peripheral organ, in any disease programme, that reports genome copies per diploid genome; (4) recovery of the 2026 supplementary S6 at panel level, which could reveal a peripheral vDNA panel this repository has not seen. |
| 🔴 **What must NOT happen** | The absence of material must **not** be written down as *"the periphery is vector-free."* That is the exact substitution this file exists to prevent. |

### 4.5 The tissue-by-tissue prior, stated so the outcome is not read uniformly

| Tissue | Most informative outcome | Why |
|---|---|---|
| **Liver** | **A or B** | The protein negative is a **both-arm** result — the strongest peripheral negative on record. Genomes here would be the cleanest possible arrival/expression split. Confound: highest blood content, and polyploidy (§3.1). |
| **Sciatic nerve** | **B or C** | Protein is **present**; §3.6(4) means local transduction is one of two explanations and this measurement chooses. Confound: low DNA yield. |
| **Spinal cord** | least informative | CNS tissue continuous with the injected compartment; a positive is nearly expected and should not be scored as peripheral (§4.3). |
| **2021 five-organ set** | **A** | Five organs, two ages, one arm — breadth, but 🔴 an image-only archive (§1.4). |

---

## 5 · THE SYSTEMIC RESCUE PARADOX — `diverge_hypotheses`

### 5.1 The observation, stated without interpretation

> A **neuron-restricted, CNS-delivered** intervention in the Aqeilan `Wwox`-null mouse produces a
> **categorical organismal survival benefit** (HD ≈78–80% at 300 d against LD reaching 0% by ~80 d;
> [`tx007_per_arm_delivery_reconstruction_20260922.md:162`](tx007_per_arm_delivery_reconstruction_20260922.md))
> — while the historical untreated-null literature describes **major peripheral abnormalities**: uraemia,
> metabolic acidosis, hypocalcaemia, reduced bone volume, splenic and thymic hypocellularity, gonadal failure
> and growth arrest ([`peripheral_phenotype_denominator_audit_20260922.md:157-169`](peripheral_phenotype_denominator_audit_20260922.md) §1.5).

🔴 **And the bound that shapes every hypothesis below, taken from Scientist G and not re-derived:** *"No two
of these five are the same animal"* — the peripheral chemistry belongs to **EIIA-Cre** (`Wwox^ΔCre/ΔCre`,
Aldaz), the gene-therapy arms to the **Aqeilan null**, the acid-base datum to **one model, once, in three
animals, with an SEM ten times the wild type's**
([`peripheral_phenotype_denominator_audit_20260922.md:132-139`](peripheral_phenotype_denominator_audit_20260922.md) §3.5;
[`:112-114`](peripheral_phenotype_denominator_audit_20260922.md) §3.4).
**So part of the paradox may be an artefact of comparing two animals**, and that possibility is
hypothesis **S5** below rather than a caveat.

⚠️ **Already exhausted and not re-derived:** the *survival-versus-protein* mismatch, dissolved by
[`discovery_survival_expression_mismatch_20260922.md:128-147`](discovery_survival_expression_mismatch_20260922.md)
(the categorical early separator is **glucose at P20**, not regional protein). **That file answers "why does
the dose step work". This section asks a different question: "how can a brain-only intervention rescue an
animal with a systemic phenotype" — and the two must not be conflated.**

### 5.2 Six mechanistically distinct explanations

**Distinctness test applied:** each pair below predicts a **different measurement outcome**, named in the
discriminator row. Two hypotheses that differ only in wording were merged before this table was written.

---

#### **S1 · CENTRAL CONTROL — CNS rescue secondarily normalises systemic physiology**
Peripheral derangements are **outputs of central regulatory failure** (hypothalamic–pituitary axes, autonomic
outflow, feeding and glycaemic control). Restore neurons, restore the set-points, and the periphery follows
**without any peripheral cell ever expressing WWOX**.
- **Predicts:** peripheral analytes **normalise**, and they normalise **on the timescale of the central
  endpoint** (glucose corrects by P20), not later.
- **Supports:** glucose is `DATO`-grade CNS-reversible in two papers at two doses
  ([`peripheral_phenotype_denominator_audit_20260922.md:358`](peripheral_phenotype_denominator_audit_20260922.md)); the
  `CLAIM 036` confounder→mediator argument ([`PMID34747138_partial_locators.md:85-92`](../research/fulltext_dossiers/PMID34747138_partial_locators.md)).
- **Against:** 🔴 established for **one analyte**. 0 of 48 non-glucose peripheral cells have ever been measured
  in a treated animal.
- **Discriminating readout:** **a clinical-chemistry panel on treated versus untreated animals.** S1 uniquely
  predicts *multiple* analytes correct *together*.

---

#### **S2 · EPIPHENOMENON — peripheral abnormalities are consequences, not death drivers**
The derangements are real but **not on the causal path to death**. The animal dies of a neurological or
central-metabolic event; the periphery is a passenger. Rescue survival and the derangements may **persist**.
- **Predicts:** 🎯 **treated survivors carry PERSISTENT peripheral abnormalities** — uraemia, low bone volume,
  splenic hypocellularity — while living to 300 days.
- **Supports:** Scientist G's explicit statement that *"either neuronal WWOX restoration corrects them … or it
  rescues survival despite them"* and that **nothing in the repository favours either**
  ([`peripheral_phenotype_denominator_audit_20260922.md:388-408`](peripheral_phenotype_denominator_audit_20260922.md) §4.4);
  the periphery stays genetically null in treated animals, so **no peripheral cell has a WWOX gene to re-express**.
- **Against:** a 300-day survivor with severe metabolic acidosis is physiologically hard to sustain — ⚠️ though
  the acidosis datum is from a **different mouse** (§5.1), so this objection is weaker than it sounds.
- **Discriminating readout:** **the same panel — but S2 is the outcome where analytes stay ABNORMAL.** S1 and
  S2 are separated by the *direction* of one measurement, which is why one panel discriminates both.

---

#### **S3 · BROADER BIODISTRIBUTION — the vector reaches more than the protein assays imply** 🎯 *this file's axis*
The periphery is **not** vector-free. Genomes arrive; some peripheral cells transcribe at a level a
whole-organ blot cannot resolve; the "CNS-only" framing is an artefact of the **detection layer**.
- **Predicts:** 🎯 **vector genomes detectable in peripheral tissue above a matrix-matched blank**, and
  plausibly a low-level peripheral transcript.
- **Supports:** the peripheral negative is a **protein** negative only (§0.1); **WWOX protein is present in
  sciatic nerve and spinal cord**, so the construct's product demonstrably leaves the brain
  ([`tx007_purkinje_frontier_20260922.md:167`](tx007_purkinje_frontier_20260922.md) `B-f1`); AAV9 after
  neonatal ICV is known to enter the circulation. ⚠️ that last is `PREMISE: DEFAULT_FROM_TEXTBOOK`.
- **Against:** the liver protein negative is a **both-arm** result, i.e. it held even at the high dose.
- **Discriminating readout:** **the peripheral vDNA qPCR — §§1–4 of this file.** 🎯 **S3 is the only hypothesis
  here that a DNA measurement can confirm, and the only one a DNA measurement can refute.**

---

#### **S4 · DETERIORATION PREVENTION — neuronal rescue forestalls a downstream systemic cascade**
Distinct from S1 in **mechanism and in timing**: not central set-point restoration, but prevention of a
**secondary insult** that the untreated null generates — seizures driving hypercatabolism and muscle
breakdown, or inability to feed driving catabolic uraemia and growth arrest. The periphery is normal because
the **assault on it** was prevented, not because a set-point was reset.
- **Predicts:** 🎯 peripheral analytes track **seizure burden and food intake**, not brain WWOX level; and the
  affected analytes are **specifically the catabolic ones** (BUN, creatine kinase, weight) rather than the
  regulated ones (glucose, calcium).
- **Supports:** `CLAIM 038` holds seizure-driven hypercatabolism and muscle disruption as a **live untested
  explanation of the uraemia**, with a named precedent in the SER rat
  ([`peripheral_phenotype_denominator_audit_20260922.md:122-126`](peripheral_phenotype_denominator_audit_20260922.md));
  **uraemia is the one chemistry analyte elevated in BOTH species** ([`:89`](peripheral_phenotype_denominator_audit_20260922.md));
  kidneys are **histologically normal with no proteinuria** in the rat — which fits catabolic uraemia far
  better than renal failure.
- **Against:** no dam-, intake- or seizure-stratified peripheral data exist anywhere.
- **Discriminating readout:** 🎯 **BUN + creatine kinase + muscle mass measured TOGETHER** — the trio the
  original authors themselves named ([`peripheral_phenotype_denominator_audit_20260922.md:416`](peripheral_phenotype_denominator_audit_20260922.md) §4.5).
  S4 predicts BUN and CK move **together**; S1 predicts BUN normalises **without** a CK signature.

---

#### **S5 · ATTRIBUTION ERROR — the peripheral phenotype was over-assigned to this genotype**
The "major peripheral abnormalities" are **not properties of the animal being treated**. They come from
`Wwox^ΔCre/ΔCre` (EIIA-Cre) and the rat `lde/lde`; the treated animal is the **Aqeilan null**. Some
derangements may be milder or absent in it, so there is **less paradox than the framing assumes**.
- **Predicts:** 🎯 **the UNTREATED Aqeilan null does not reproduce the EIIA-Cre chemistry** — in particular
  acidosis and hypocalcaemia.
- **Supports:** 🔴 **hypoglycaemia is demonstrably species-specific** (two mouse nulls yes, rat no) and
  **calcium is model-discordant** ([`peripheral_phenotype_denominator_audit_20260922.md:92-93`](peripheral_phenotype_denominator_audit_20260922.md) §3.3);
  the acidosis rests on **one model, one measurement, three animals, SEM ×10**
  ([`:112-114`](peripheral_phenotype_denominator_audit_20260922.md)); the NCKU nulls have **never had glucose
  measured at all** ([`:121`](peripheral_phenotype_denominator_audit_20260922.md)).
- **Against:** uraemia, gonadal failure and growth arrest **are** cross-model invariant, so S5 cannot dissolve
  the whole phenotype.
- **Discriminating readout:** 🎯 **the same panel run on the UNTREATED `KO+RI` arm.** S5 is the only hypothesis
  whose signature appears in the **control** animals, before any treatment comparison is drawn.

---

#### **S6 · SURVIVOR SELECTION — the rescued population is not the treated population**
The treated animals that live to be measured are a **selected subset**, and the peripheral picture in
survivors reflects **who survived**, not what the vector did. Either the periphery was mildest in those
animals to begin with, or the plotted arm is not the whole treated arm.
- **Predicts:** 🎯 **peripheral status at an EARLY timepoint, before mortality accrues, differs from the
  survivor picture** — and the spread among treated animals is **wide**, not tight.
- **Supports:** every P240/P300 expression row is **survivor-selected** and the paper's own explanation of its
  expression/survival mismatch is a **post-hoc survivor-versus-non-survivor comparison**
  ([`tx007_regional_wwox_forebrain_cerebellum_20260922.md:267-272`](tx007_regional_wwox_forebrain_cerebellum_20260922.md));
  🔴 **`censor*` → 0 occurrences and no censoring rule exists**
  ([`tx007_per_arm_delivery_reconstruction_20260922.md:176`](tx007_per_arm_delivery_reconstruction_20260922.md));
  🔴 **the vehicle-injected WT arm itself sits at ≈72% at 300 d, not 100%**
  ([`:195`](tx007_per_arm_delivery_reconstruction_20260922.md)) — so the procedure alone removes ~28% of
  *wild-type* animals, and the sciatic-nerve blot already shows **seven animals spanning strong to barely
  detectable** ([`therapeutic_translation_second_pass.md:591`](therapeutic_translation_second_pass.md)).
- **Against:** selection struggles to manufacture LD reaching **0%**
  ([`discovery_survival_expression_mismatch_20260922.md:55`](discovery_survival_expression_mismatch_20260922.md)).
- **Discriminating readout:** 🎯 **peripheral analytes at an early timepoint (P14–P20) in BOTH arms, with
  per-animal values plotted rather than group means.** S6 is the only hypothesis whose signature is in the
  **variance and the timing**, not in the group mean.

### 5.3 Mutual exclusivity — stated, because "six hypotheses" is worthless if they are one

| | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| **Peripheral analytes in treated survivors** | normal | 🔴 **abnormal** | normal | normal (catabolic ones) | normal-ish **in controls too** | depends on **timing** |
| **Peripheral vector genomes** | absent | absent | 🎯 **present** | absent | absent | absent |
| **Untreated `KO+RI` chemistry** | deranged | deranged | deranged | deranged | 🎯 **milder than EIIA-Cre** | deranged |
| **BUN/CK co-movement** | no | n/a | no | 🎯 **yes** | no | no |
| **Per-animal spread in treated arm** | tight | tight | tight | tight | tight | 🎯 **wide** |
| **Early (P14–P20) vs late divergence** | early | n/a | n/a | early | n/a | 🎯 **early ≠ late** |

🟢 **Every column differs from every other in at least one row**, so no two are restatements.
⚠️ **S1 and S4 are the closest pair** and are separated by exactly one row (BUN/CK co-movement) — which is why
that measurement is named rather than assumed.

### 5.4 🎯 The single measurement that discriminates the most

> ## 🥇 **ONE terminal blood draw per animal, run as a clinical-chemistry panel PLUS creatine kinase, on FOUR arms — treated, untreated `KO+RI`, `WT+RI`, and treated animals at an EARLY (P14–P20) timepoint — with per-animal values reported.**

**It discriminates five of six:**

| Hypothesis | How this one measurement decides it |
|---|---|
| **S1** | analytes **normalise across several families together** in treated animals |
| **S2** | analytes **stay abnormal** in 300-day survivors — the direct contradiction of S1, read off the same numbers |
| **S4** | **BUN and CK move together**, and the *regulated* analytes behave differently from the *catabolic* ones |
| **S5** | the **`KO+RI` control arm** is milder than the EIIA-Cre literature predicts |
| **S6** | the **early arm differs from the survivor arm**, and per-animal spread is wide |
| 🔴 **S3** | ❌ **NOT discriminated — a blood panel cannot see vector genomes.** |

> 🎯 **And that is the precise, non-redundant place of this file's own proposal.** The blood panel is the more
> powerful instrument and it is **already named twice in this repository** by two prior actors — as `T2-d`
> ([`peripheral_phenotype_denominator_audit_20260922.md:233`](peripheral_phenotype_denominator_audit_20260922.md))
> and as Scientist F §4 step 2 — and re-proposing it as new would be claiming someone else's experiment. **It
> is re-stated here only to be scored honestly, and the scoring is what is new: it settles five hypotheses and
> is blind to the sixth.** The peripheral vDNA qPCR is the **only** move that touches S3, it is **one to two
> ladder levels cheaper**, and it is **independent** — the two can run on different material, in either order.
> ⭐ **If both are ever run on the same cohort, one terminal bleed and one peripheral tissue punch per animal
> settle all six with zero additional animals.**

⚠️ **Standing bound.** All six are `IPOTESI`. None is a mechanism in a human, and nothing here is medical
advice or a proposal for any person.

---

## 6 · EXISTING-ASSET LADDER — every proposal in this file, classified

**Levels:** **L0** reanalysis of existing data · **L1** new analysis on stored material ·
**L2** new stain or assay on existing material · **L3** new animal.
**Rule applied:** prefer lower **only where information gain is comparable**, and say so explicitly where a
cheap option cannot discriminate.

| # | Proposal | Level | Discriminates | Conditional on | Honest bound |
|---|---|---|---|---|---|
| **A1** | **Recover the 2026 supplementary S6 at panel level** (S6A–S6I: spinal cord, sciatic nerve, liver) and read every caption and axis | **L0** | 🔴 **Nothing on the genome axis.** It could reveal an **unseen** peripheral vDNA panel, and it would put `n`, age and arm on the sciatic-nerve result | 🔴 five retrieval routes already failed; a sixth recovered S8 ([`peripheral_phenotype_denominator_audit_20260922.md:214`](peripheral_phenotype_denominator_audit_20260922.md) T0-c) | 🔴 **Say it plainly: the cheapest option CANNOT answer the question.** It is run first only because it is free and could make a later step unnecessary |
| **A2** | **Read the Fig 5 caption** to settle whether *"normalized to WT levels"* scopes to the vDNA panels | **L0** | Nothing peripheral — but it is the **precondition for citing any vDNA axis at all** | `files/` access | already an open `REVIVAL_TRIGGER` ([`fold_of_wt_is_undefined_for_vdna_20260922.md:51-53`](fold_of_wt_is_undefined_for_vdna_20260922.md)); **pointer only, not re-derived** |
| **A3** | **Open `PMID 34747138` Appendix S2B–C at panel level** — the five-organ peripheral westerns/IHC | **L0** | Converts the 2021 peripheral negative from running text to panel-level, and shows **which detection modality** produced it | OA bundle access ([`peripheral_phenotype_denominator_audit_20260922.md:213`](peripheral_phenotype_denominator_audit_20260922.md) T0-b) | 🔴 **Cannot see genomes.** A protein panel read more carefully is still a protein panel |
| 🥇 **B1** | **Peripheral vDNA qPCR on banked 2026 material** — liver, sciatic nerve, spinal cord; published primer pair; 50 ng per reaction; `KO+RI` and `WT+RI` as matrix-matched blanks | **L1** | 🎯 **S3, uniquely. The whole of §4.** | 🔴 **`A-f4` — tissue or extracted-DNA retention, `HUMAN_REQUIRED` and unknowable from here** ([`tx007_purkinje_frontier_20260922.md:146`](tx007_purkinje_frontier_20260922.md)) | **L1 and not L0**, because §2.3 requires **adding** a host single-copy reference amplicon, a standard curve and a spiked-matrix recovery control. 🔴 **Running the original assay unmodified would be L0 and would inherit an undefined axis — i.e. it would be cheaper and would not answer the question.** Stated explicitly, per the brief |
| **B2** | **Peripheral RT-qPCR** on the same material, published transcript primer pair ([`cerebellum_layer_localisation_20260922.md:246`](cerebellum_layer_localisation_20260922.md)) | **L1** | Splits **Outcome B** (genomes present, protein absent) into *not transcribed* versus *transcribed but not translated/below blot LOD* | RNA or TRIzol-interphase retention — 🟡 weaker than B1's condition | 🔴 **Only worth running conditionally on Outcome B.** Running it first would waste the material |
| **B3** | **DNA from archived 2021 peripheral material** (five organs, two ages) | **L1** | The same question in the **independent 2021 arm** | 🔴 **Weakest archive:** the 2021 Methods heading list contains **no tissue-extraction section at all** ([`purkinje_cheapest_path_and_community_followup_20260922.md:384`](purkinje_cheapest_path_and_community_followup_20260922.md)) | 🔴 **PARK.** Named for completeness; the material class is `NOT ESTABLISHED` and probably never existed |
| **C1** | **Vector-specific ISH/DNA-FISH on archived FFPE or OCT peripheral sections** — a human-`WWOX`- or vector-element-specific probe, with **zero endogenous background in a mouse host** | **L2** | 🎯 **Everything B1 answers, PLUS the cell type** — which B1 by construction cannot (§3.6(1)) | block retention; 🔴 the perfusion Methods name **brains**, so peripheral blocks are `NOT ESTABLISHED` (§1.4) | 🎯 **The one place where the cheap option is genuinely NOT comparable.** B1 gives a bulk number; C1 gives arrival **per cell**, on the same section as the protein channel. The species difference is the label — the design is already worked out for cerebellum at [`purkinje_existing_material_experiment_20260922.md:525`](purkinje_existing_material_experiment_20260922.md) `J3`, and **transfers to peripheral tissue unchanged** |
| **D1** | **Terminal clinical-chemistry panel + CK, four arms, per-animal values** (§5.4) | **L1** on banked serum / **L3** for acid-base and CBC | 🎯 **Five of six systemic hypotheses** | banked serum (🔴 `NOT ESTABLISHED`); 🔴 **bicarbonate and platelets are `NOT RECONSTRUCTIBLE` from any stored material at any price** ([`peripheral_phenotype_denominator_audit_20260922.md:230-232`](peripheral_phenotype_denominator_audit_20260922.md)) | 🔴 **NOT this file's proposal — it is `T2-d`/Scientist F's, re-stated only to be scored.** ⭐ **L3 cost falls to zero if attached to a cohort already being terminated** |
| **E1** | **A new peripheral-biodistribution animal arm** | **L3** | Everything, definitively | new animals | 🔴 **NOT PROPOSED.** Every question above has an L0–L2 route that should be exhausted first, and the L3 floor is already occupied by `T2-d`, which fills more cells per animal |

### 6.1 Recommended order, and why

> **A1 → A2 → A3 → B1 → (B2 conditional on Outcome B) → C1 if and only if cell-type assignment is needed.**
>
> 🎯 **B1 is the decision point of this ladder and the single highest-information move available at L1.** It is
> the only proposal here that touches **S3**, it is the only one that splits **arrival** from **expression**,
> and its outcome is **genuinely unpredicted** — a rare property, and the reason to run it rather than
> a measurement whose answer is already inferable.
>
> ⚠️ **Three honest statements the ladder must carry:**
> 1. **The free L0 options cannot answer the question.** They are run first because they are free and could
>    make B1 unnecessary — not because they are comparable.
> 2. **B1 must be L1 and not L0.** The original assay lacked the normaliser, the standard curve and the
>    matrix-matched recovery control that a peripheral reading needs (§2.3, §3). Re-running it unmodified is the
>    cheaper option that does not discriminate.
> 3. **All of B1, B2, C1 and the L1 half of D1 are conditional on `A-f4`, which is `HUMAN_REQUIRED`.** If the
>    material is gone, **Outcome D** applies and the revival triggers of §4.4 stand.

---

## 7 · What I could not establish

1. 🔴 **Whether any 2026 or 2021 peripheral material still exists.** `A-f4`, `HUMAN_REQUIRED`, unknowable from a repository.
2. 🔴 **What the vDNA amplicon targets.** Sequences are published; the element they sit in is `METHODS_INVISIBLE`. **The titration assay's bGH primers must not be assumed to be the tissue assay's target.**
3. 🔴 **Perfusion status of the 2026 DNA tissue.** Stated for RNA (non-perfused); not stated for DNA.
4. 🔴 **Whether the Fig 5A–5D y-axis is raw copies per reaction.** `NOT READABLE`; open `REVIVAL_TRIGGER`.
5. 🔴 **`n` for any Fig 5 panel.** `n =` → 0 tokens in the served body.
6. 🔴 **Age and `n` for the sciatic-nerve panel.** Unstated; LD was never assayed there at all.
7. 🔴 **Whether the 2026 supplementary S6 contains a peripheral vDNA panel this repository has never seen.** Five retrieval routes failed. **This is the one residual way the whole question could already be answered in print**, and A1 exists to check it.
8. 🔴 **Whether liver/nerve lysates from 2026 were frozen or discarded**, and whether the TRIzol interphase was kept.
9. ⚠️ **Whether the untreated Aqeilan null reproduces the EIIA-Cre peripheral chemistry** — hypothesis **S5**, and unmeasured in either direction.

---

## Summary for the orchestrator

- **TISSUE INVENTORY.** 🟢 **DEFINITELY EXISTS:** 2026 liver (**both arms**), sciatic nerve (**HD only**), spinal cord (**HD only**); 2021 liver, pancreas, kidney, testis, ovary at **P17 and 9 months**. 🟡 **PROBABLY EXISTS:** fixed/FFPE material for the 2026 tissues; TRIzol interphase DNA. 🔴 **NOT ESTABLISHED:** heart, kidney, spleen, lung, muscle, bone in 2026; the 2021 archive is **image-only** (no tissue-extraction Methods section at all); and **whether anything survives in a freezer is `A-f4`, `HUMAN_REQUIRED`, and is not guessed anywhere in this file.**
- **METHOD REUSABILITY.** 🟢 **Recoverable and better than the record assumed** — the vDNA **primer pair, 50 ng template, 25 mg ATL lysis and DeNovix quantitation are all in the repository, published by the authors**, and no sequence is invented here. 🔴 **`METHODS_INVISIBLE`:** amplicon target, cycling conditions, chemistry, replicates, `n`, perfusion status of the DNA tissue. 🔴 **Structurally absent and confirmed by validated token negatives:** host reference amplicon, standard curve, absolute-copy units. ⇒ **reusable as a relative assay; must be upgraded with a single-copy nuclear normaliser, a standard curve and a spiked-matrix recovery control to answer a peripheral question.**
- **DISCRIMINATING MEASUREMENT (diverge).** **One terminal blood draw run as a clinical-chemistry panel plus creatine kinase, on four arms — treated, `KO+RI`, `WT+RI`, and an early P14–P20 treated arm — with per-animal values.** It settles **five of six** systemic hypotheses (S1, S2, S4, S5, S6) and is 🔴 **blind to S3**. That blindness is exactly the gap the peripheral vDNA qPCR fills, and it is why the two are complementary rather than competing. **The blood panel is not claimed as new — it is `T2-d`/Scientist F's, re-stated only to be scored.**
- **LADDER.** **L0:** A1 recover S6 panels, A2 read the Fig 5 caption, A3 open 2021 Appendix S2B–C — all free, **and none of them can answer the genome question**. 🥇 **L1: B1, peripheral vDNA qPCR on banked 2026 liver / sciatic nerve / spinal cord, published primers, `KO+RI` and `WT+RI` as matrix-matched blanks** — the only move that touches S3 and the only one that splits arrival from expression. **L1 conditional:** B2 peripheral RT-qPCR if Outcome B. **L1 parked:** B3 (2021 material, class probably never existed). **L2:** C1 vector-specific ISH on archived peripheral sections — the one case where the cheaper option is **not** comparable, because only C1 assigns arrival to a cell type. **L3:** not proposed; the floor is already occupied by `T2-d`, which fills more cells per animal.
- **The peripheral negative remains an `INFERENZA` at the genome layer, and this file does not change that.** It establishes that the measurement which would change it is **runnable with the programme's own published assay**, names the four outcomes in advance, and states the normalisation, blank, blood-contamination, episomal-dilution, LOD and cell-type bounds that make each outcome interpretable.

*End of file. Complete run. Scientist A, 2026-09-22. READ-ONLY toward every canonical file; one file written; no commit; no external contact; nothing here is medical advice.*

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V1 · 🟢 The primer pair is CONFIRMED verbatim, and it is what makes `B1` executable

`cerebellum_layer_localisation_20260922.md:212–215` carries, marked **FIRST-HAND** from the 2026
Methods:

> *"tissue samples (up to 25 mg) were lysed in ATL buffer … **For qPCR, 50 ng of DNA template was
> used per reaction.** The primer sequences were as follows: forward 5′ GCTCTCTTAAGGTAGCCCCG 3′,
> reverse 5′ CGCCTCATCCTGGTCCTAAA 3′."*

🎯 **The programme's own published vector-genome assay is recoverable without inventing a single
sequence.** That is the difference between "somebody should measure the periphery" and a runnable
protocol, and it is why `B1` sits at `L1` rather than in the wish column.

## V2 · 🔴 A scope trap I walked into myself — recorded because it is the session's recurring defect

Checking the hand-back's *validated negatives* (`reference gene`, `standard curve`, `single-copy`,
`diploid` = 0), a **repository-wide** grep returns **5–9 files each**. That looks like a refutation.
It is not.

**The claim is scoped to the 2026 paper's Methods block. My grep was scoped to the whole
repository — the wrong instrument for the claim.** Worse, the two scopes are *anti-correlated by
construction*: those tokens appear in LEGEND's analysis files **precisely because LEGEND is
documenting their absence from the paper.**

> 🔴 **A validated negative about a source can be masked by the analysis that records it.**
> Searching "does the corpus mention X" cannot answer "does the source contain X", and here it
> returns the opposite answer with full confidence.

This is the fourth member of the search-defect family, and the first where the failing searcher was
the verifier rather than the Scientist. The hand-back's scoping was correct; my check was not.
`SOURCE DEPTH` vs `ANALYSIS DEPTH` is exactly the distinction that resolves it — the tokens live at
analysis depth, and the claim was about source depth.

## V3 · What is and is not established

**Established:** the assay is recoverable; the tissues in the 🟢 class were necessarily dissected
(a reported measurement entails a dissection); the 2021 archive is image-only, so `B3` is correctly
parked.

**NOT established, and correctly flagged `HUMAN_REQUIRED` (`A-f4`):** whether any DNA-bearing
material survives in a freezer. No guess is made anywhere in the file, and Outcome D carries four
revival triggers.

**The asymmetry that matters, and the file states it before the outcomes rather than after:**
blood contamination biases only toward a false positive, so **an ABSENT result is robust and a
PRESENT result is not**; and without a standard curve there is no LOD, so a negative is
uninterpretable without spiked-matrix recovery per tissue. That upgrade is what makes `B1` an `L1`
rather than an `L0`.

🔴 **The peripheral negative remains an `INFERENZA` at the genome layer.** Nothing in this file
changes that, and the file does not claim to. Also preserved: WWOX protein in sciatic nerve is
**fully explicable by axonal transport from a transduced central or DRG neuron with no local
transduction** — which is why the genome measurement is informative rather than confirmatory.

The terminal blood panel is credited to its originating Scientist (`T2-d`) and re-stated only to be
scored, not claimed as new. It settles five of six systemic hypotheses and is **blind to S3** —
the one the vDNA measurement covers.
