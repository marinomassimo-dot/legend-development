# CLAIM 039 — reconstruction and adjudication of the "structural explanation"

**Node:** `CLAIM039_STRUCTURAL_EXPLANATION_ADJUDICATION` · **Actor:** SCIENTIST A (`scientist-a`) · **Date:** 2026-09-23

**Status:** 🔴 **non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, every
registry, every queue, every ledger, the receipt chain and `framework/state/state_manifest_current.md`.
No claim edited, no paper record edited, no working-model edit, no commit candidate, no gate, no receipt,
no `BATCH_COMMIT`, **no git operation**, **no external contact of any kind**. This file is the only thing
written in this act.

> 🔴 **Nothing here is medical advice.** No molecule, no class, no dose, no route, no schedule, no compound
> and no druggability score is named anywhere in this file — deliberately, including the pro-myelinating
> directions that a hypomyelination finding makes reflexive to name.
> 🔵 **Public edition.** All reasoning is at the level of a **WWOX-DEE genotype class** and of named animal
> alleles. No individual-level record is described, reintroduced or inferred.
> ⚠️ **Alleles, species and models are never pooled.** `Wwox`-null mouse (Aqeilan), `Wwox^ΔCre/ΔCre` (Aldaz),
> NCKU `WD1`/`WD234` nulls, `Wwox^gt/gt`, `Wwox^P47T/P47T` knock-in, `Syn-Cre` S-KO, `Nestin-Cre` N-KO, rat
> `lde/lde`, human WOREE and human SCAR12 are **distinct objects**. Every statement below carries the model
> it was measured in.

---

## § 0 · READ DEPTH, DECLARED PER SOURCE, BEFORE ANY FINDING

### 0.1 Primary sources — this act

| # | Source | Route | Depth **in this act** | Mark |
|---|---|---|---|---|
| **S1** | **Tochigi Y, Takamatsu Y, Nakane J, Nakai R, Katayama K, Suzuki H. 2019.** *Loss of Wwox Causes Defective Development of Cerebral Cortex with Hypomyelination in a Rat Model of Lethal Dwarfism with Epilepsy.* **Int J Mol Sci 20(14):3596.** PMID `31340538` · PMCID `PMC6678113` · [DOI](https://doi.org/10.3390/ijms20143596) · CC BY | PubMed MCP `get_full_text_article`, PMC body served in full | 🟢 **FULL BODY + METHODS**, read end to end. Abstract, Introduction, Results §§ 2.1–2.3, Discussion, Materials and Methods §§ 4.1–4.4 | 🟢 **FIRST-HAND** |
| **S2** | **Iacomino M, Baldassari S, Tochigi Y, … Suzuki H, Salpietro V. 2020.** *Loss of Wwox Perturbs Neuronal Migration and Impairs Early Cortical Development.* **Front Neurosci 14:644.** PMID `32581702` · PMCID `PMC7300205` · [DOI](https://doi.org/10.3389/fnins.2020.00644) | PubMed MCP `get_full_text_article` | 🟢 **FULL BODY + METHODS**, read end to end | 🟢 **FIRST-HAND** |
| **S3** | Suzuki H, Takenaka M, Suzuki K. 2007. *Phenotypic characterization of spontaneously mutated rats showing lethal dwarfism and epilepsy.* Comp Med 57:360–369. PMID `17803050` — **no DOI, no PMCID** | PubMed MCP `get_article_metadata` | 🟡 **ABSTRACT + MeSH only.** Body unobtainable in this environment (confirmed again this act) | 🟡 first-hand **at abstract depth**; body 🔴 **SIBLING-ATTESTED** via `research/fulltext_dossiers/PMID17803050.md` |
| **S4** | Suzuki H *et al.* 2009. Genes Brain Behav 8:650–660. PMID `19500159` · [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x) | PubMed MCP metadata | 🟡 **ABSTRACT + MeSH only** | 🟡 first-hand at abstract depth |
| **S5** | Takenaka M *et al.* 2008. J Androl 29:669–678. PMID `18676360` · [DOI](https://doi.org/10.2164/jandrol.108.005066) | PubMed MCP metadata | 🟡 **ABSTRACT only** | 🟡 first-hand at abstract depth |
| **S6** | Abdel-Salam G *et al.* 2014. Orphanet J Rare Dis 9:12. PMID `24456803` · [DOI](https://doi.org/10.1186/1750-1172-9-12) | PubMed MCP metadata | 🟡 **ABSTRACT only** | 🟡 first-hand at abstract depth |

🔵 **Attribution, as the retrieval tool requires:** every bibliographic record, abstract, MeSH list and
full text in this file was retrieved **from PubMed / PubMed Central**. DOIs are given as links above and
at every first use below.

### 0.2 🔴 A FIDELITY DEFECT IN THE SERVED TEXT, DECLARED BEFORE ANY QUOTATION

The PMC route strips `<italic>` markup. In this journal the **genotype symbols are italicised**, so
`lde/lde`, `+/+` and `+/lde` are **erased from the served string**, leaving grammatical holes:

> served: *"In rats, epileptic seizures and ataxic gait occur after PND 16 [,]."*
> published: *"In **`lde/lde`** rats, epileptic seizures and ataxic gait occur after PND 16 [refs]."*

I can prove the stripping convention rather than assume it: `deepdive_manifests/PMID31340538.json`
locator 2, recorded on 2026-08-06 from the **XML** artefact, reads *"there is no significant difference
between **+/+ and lde/lde** rats in the thickness of cerebral cortices at all ages"*, while the same
sentence served to me today reads *"there is no significant difference between and rats…"*. The stripped
tokens are exactly the italicised genotype symbols.

Citation brackets are likewise emptied: `[,]` and `[,,,]` are **reference-number lists whose numbers I
cannot recover**. Two independent egress routes to the marked-up XML (Europe PMC `fullTextXML`; NCBI
`efetch db=pmc`) were **refused by the proxy** (`connect_rejected`, HTTP 403) and the manifest's own
artefact `files/fulltext/PMID31340538_Tochigi2019.xml` **does not exist in this edition** (`files/` is
absent — it is the private-overlay path). See § 6.

⚠️ **Convention used below.** Every quotation is given **as served**, verbatim. Where I restore a stripped
genotype token I write it in ⟦brackets⟧ and it is a **reconstruction, not a quotation**.

### 0.3 Repository sources read directly this act

`ataxia_without_cerebellar_lesion_20260922.md` (§§ 6.0–6.3 in full) · `cerebellar_measurement_census_20260922.md`
(§ 4.3, §§ 6.1–6.4) · `claim_registry_current.md` CLAIM 016 `:290-302`, CLAIM 037 `:682`, CLAIM 038 `:699`,
CLAIM 039 `:716-729` · `paper_registry_current.md` PAPER 021 `:479-496` · `research/fulltext_dossiers/PMID31340538.md`
(entire) · `research/deepdive_manifests/PMID31340538.json` (all 11 locators) · `wwox_myelin_oligodendrocyte_census_20260921.md`
`:330-375` · `lde_myelin_vacuole_bridge_20260922.md` §§ 0–2.1.

🔴 **No figure panel was inspected.** I read no image in this act. Every statement about a figure is a
statement about its **caption or running text**, never about pixels.

---

## § 1 · BASELINE — what the repository already holds, cited and NOT re-derived

| # | Already held | Where | Re-derived here? |
|---|---|---|---|
| **B1** | The attribution sentences exist in Tochigi 2019's Discussion, and the repository's record of that paper *"stops one sentence short"* | `ataxia_without_cerebellar_lesion_20260922.md:358-372` § 6.1 | 🔴 **NO.** I **verify** it first-hand; I do not claim it |
| **B2** | The 2019 histology block *"spans the whole length of the hippocampus"*; males only; n ≥ 3 + 3; PND 5/10/15/21; no blinding; no motor test | same file `:374-398` § 6.2 | 🔴 **NO.** Verified first-hand, **and extended** — see § 2.2 |
| **B3** | The allele × cerebellar-evidence matrix — which allele had its cerebellum sectioned, assayed, Purkinje-marked | `cerebellar_measurement_census_20260922.md:360-388` § 4.3 | 🔴 **NOT REBUILT.** Cited as it stands |
| **B4** | The `A-f4` split: Q1 (is the cerebellum damaged) ≠ Q2 (does the vector reach Purkinje cells); `lde/lde` sits in **Q4**, blocked by an unnamed custody question at Nippon Veterinary and Life Science University, `HUMAN_REQUIRED` | same file `:539-561` § 6.2 | 🔴 **NOT REMADE.** Cited |
| **B5** | CLAIM 039 **already carries** the `LIGHT_MICROSCOPY_FLOOR` premise, the 32-locator parameter blank, the P1 foliation counter-evidence and *"il silenzio a 28 giorni non è mai stato evidenza di normalità cerebellare"* | `claim_registry_current.md:726`; audited `cerebellar_measurement_census_20260922.md:531` | 🔴 **NO.** I propose **no defect** on those limbs |
| **B6** | The 2019 read's own dossier and its 11-locator manifest | `research/fulltext_dossiers/PMID31340538.md`; `research/deepdive_manifests/PMID31340538.json` | 🔴 **NO** — but see § 2.1c, where their **contents decide the propagation question** |
| **B7** | The propagation-defect pattern: CLAIM 016 (lithium arm not genotype-specific, `:302`), CLAIM 039 limb (b) (the P1 foliation locator never captured, `:726`) | `claim_registry_current.md` | 🔴 **NO.** Counted, not re-derived |
| **B8** | Tochigi 2019's modal audit — *"axon-first explanation is explicitly modal"*, *"oligodendrocyte-first explanation is indicative"* | `wwox_myelin_oligodendrocyte_census_20260921.md:367-375` | 🔴 **NO.** Cited, and **§ 2.7 adds the point it misses** |

🎯 **What this act adds that no sibling holds:** the seven items enumerated in § 7.2. Everything else above
is carried, not claimed.

---

## § 2 · THE RECONSTRUCTED CHAIN — items 1–7 of the brief

### 2.1 Item 1 — EXACT SOURCE, retrieved first-hand

**Paper:** Tochigi *et al.* 2019, *Int J Mol Sci* **20**:3596 ([DOI](https://doi.org/10.3390/ijms20143596)),
PMID `31340538` / PMCID `PMC6678113`, CC BY, open access. **Section: Discussion — the fourth paragraph, the
one on myelination — final three sentences of that paragraph.**

#### 🟢 `L1` — the attribution, verbatim as served

> *"In ⟦lde/lde⟧ rats, epileptic seizures and ataxic gait occur after PND 16 [,]. **Such neurological
> defects have been reported in several mutant animals showing hypomyelination [,,,]. Therefore, part of
> the phenotype of ⟦lde/lde⟧ rats is associated with hypomyelination, accompanied by a reduced number of
> mature oligodendrocytes.**"*

#### ✅ Adjudication of the sibling's quotation

`ataxia_without_cerebellar_lesion_20260922.md:364-368` quotes these three sentences. **CONFIRMED —
word-for-word identical in substance.** The sibling's sentence order, wording, emphasis and the
"two sentences after" structure described in the brief are all exactly right: the repository's
pre-existing quote (`wwox_myelin_oligodendrocyte_census_20260921.md:353`, *"In `lde/lde` rats, epileptic
seizures and ataxic gait occur after PND 16"*) is **sentence 1**, and the attribution is **sentences 2–3**.

Two **corrections of hygiene, not of substance**, which I record because locator discipline is the point:

1. 🟡 The sibling prints `` `lde/lde` `` **inside the quotation marks** without flagging it as a restoration
   of stripped italic markup. The restoration is certainly correct, but a quotation mark should not contain
   an unmarked reconstruction. I use ⟦⟧ above for exactly this reason.
2. 🟡 The sibling renders both citation brackets as *"[refs]"*. That is honest but it conceals a real loss:
   **the reference numbers behind *"several mutant animals showing hypomyelination"* are unrecoverable in
   this environment.** The analogy's entire evidence base is therefore **unidentifiable** — see § 6.

#### 🟢 `L1b` — verified propagation defect (independent re-derivation)

`grep -riE "Such neurological defects|mutant animals showing hypomyelination|phenotype of .{0,20}rats is
associated with hypomyelination" --include=*.md .` → hits **only inside
`ataxia_without_cerebellar_lesion_20260922.md` itself** (the quote block and the grep string it records).
**Zero hits in any registry, dossier, ledger, queue or manifest.** Confirmed further at source:

- the **complete-read dossier** `research/fulltext_dossiers/PMID31340538.md` contains the tokens `ataxia`,
  `hypomyelination`, `PND 16` and `conduction` **only** in the paper's title line and in one negative
  inventory line (`:39`). The attribution is **absent from the dossier**;
- the **11 verbatim locators** of `deepdive_manifests/PMID31340538.json` are: 13-bp deletion; cortical
  thickness; MAP2 WB; APC counts; Iba1 WB; microglial Wwox absence; 46.2-kDa band; the glial contrast with
  the mouse; the `n ≥ 3` males sentence; the litter-reduction sentence; the Fig. 3 statistics caption.
  **None is the attribution; none is the Methods sectioning sentence; none is the axon sentence.**

⇒ 🔴 The defect is confirmed at **reading-artefact level**, not merely at claim level. This is the
**third instance** of the pattern already recorded on CLAIM 016 and on CLAIM 039 limb (b).

### 2.2 Item 2 — EXACT STRUCTURAL FINDING: measured versus inferred by analogy

**🟢 MEASURED, first-hand from Results § 2.2 and Methods §§ 4.1–4.4:**

| Axis | Value, verbatim or exact |
|---|---|
| **Myelin markers** | **MBP** and **CNP**, by IHC and western blot. *"⟦lde/lde⟧ rats showed significantly lower myelination on PNDs 5–21"* |
| **Mature oligodendrocyte marker** | **APC (clone CC-1)**. *"the number of APC-positive cells was significantly lower in a subarea of the cerebral cortex including the WM region of ⟦lde/lde⟧ than of ⟦+/+⟧ rats on PNDs 15–21"* |
| **Neurite marker** | **MAP2** — and, in the authors' own words, *"neurite marker MAP2 **mainly detected in immature dendrites** [,]"* |
| **Second neurite readout** | **FluoroPan Neuronal Marker** — *"indicating that **axon-like** vertical neurite growth is present but totally reduced in ⟦lde/lde⟧ at PND 21"* |
| **Other markers** | NeuN (A60 / EPR1263), GFAP, Iba1, Wwox (Sigma HPA050992, raised to human Wwox aa 32–110) |
| **Ages** | **PND 5, 10, 15, 21 only.** *"Normal (⟦+/+⟧,⟦+/lde⟧) and ⟦lde/lde⟧ rats at PNDs 5, 10, 15, and 21 were anesthetized with isoflurane"* |
| **n** | *"**At least three** affected and **three** normal males were included in each experiment (western blot and immunostaining) and examined each day"*; and *"All quantitative analysis … from at least three rats"* — 🔴 a **floor, not an n** |
| **Sex** | 🔴 **MALES ONLY.** *"**Male** rats were derived from the inbred LDE strain [,,]"* |
| **Blinding** | 🔴 **ABSENT.** The string `blind` occurs **nowhere** in the served body. No randomisation, no power calculation, no multiplicity correction; *"Student's t-test"* per age |
| **Section plane** | 🔴 **CORONAL** |
| **Tissue block** | 🔴 **HIPPOCAMPUS-SPANNING.** See `L2` |
| **Litter manipulation** | *"the numbers of littermates were reduced to <5 pups at around PND 5 to enhance the survive of ⟦lde/lde⟧ pups"* — a husbandry intervention that alters nutrition and maternal care, unmatched between arms as reported |

#### 🟢 `L2` — the tissue block, Methods § 4.3, verbatim

> *"Their brains were removed, fixed in 4% paraformaldehyde for 48 h, and embedded in paraffin, followed by
> sectioning into 5-µm-thick sequential **coronal sections spanning the whole length of the hippocampus** []."*

✅ **CONFIRMS** `ataxia_without_cerebellar_lesion_20260922.md:379` and the `A4` row of
`cerebellar_measurement_census_20260922.md:202`, **word for word**.
🎯 **And adds one thing neither holds:** the sentence ends in a **citation bracket**. The sectioning frame is
itself **inherited from a prior protocol**, not chosen for this question — which is the mildest possible
reading of why the cerebellum is absent, and the fairest one.

#### 🟢 `L3` — the mutant western never touched the cerebellum either

> *"Western blot analysis also showed that Wwox protein was expressed in different parts of the CNS,
> including the olfactory bulb, cerebral cortex, hippocampus, diencephalon, **cerebellum, brain stem, and
> spinal cord** (B)."*  — Results § 2.1, and the animals of that panel are **PND 21 normal males**.
> *"In contrast, no protein band with the same electrophoretic mobility was detected in **the whole brain and
> cerebral cortex** of ⟦lde/lde⟧ rats"* — the **mutant** blot.

⇒ ✅ **CONFIRMS first-hand** the census's `A4` finding that the cerebellar western is **wild-type only**.
The protein is documented in cerebellum, brainstem and cord; the **mutant** is documented in whole brain and
cortex. 🔴 **`NOT ASSAYED` in the mutant cerebellum, by either modality.**

**🔴 INFERRED BY ANALOGY, not measured — the load-bearing middle premise:**

> *"**Such neurological defects have been reported in several mutant animals showing hypomyelination** [,,,]."*

This is the only bridge between the measured cortical myelin deficit and the neurological phenotype. It is
**a literature analogy to unnamed other mutants, in unnamed species, with unnamed lesions**, and I cannot
recover which (§ 0.2). `PREMISE: ANALOGY_TO_OTHER_MUTANTS`.

**🔴 AND THE EXPLANANDUM ITSELF IS NOT MEASURED IN THIS PAPER.** The ataxic gait enters only through the
Introduction, as literature: *"Initially, ⟦lde/lde⟧ rats were identified as spontaneous mutants with severe
dwarfism, **gait ataxia**, pediatric epilepsy, male hypogonadism, and early postnatal death [,]."* There is
**no gait observation, no motor battery, no behavioural assay, no electrophysiology and no conduction
measurement anywhere in the 2019 Methods.** ⇒ **Not one animal in this study had both its myelin and its
gait measured.**

### 2.3 Item 3 — GENOTYPE / MODEL, and how far the authors extend it

**Allele:** rat `lde/lde` — *"a 13-bp deletion (c.1190_1202del) in exon 9 … causes frame-shift, resulting in
an aberrant C-terminal amino acid sequence (p.leu371Thrfs*53)"*. Inbred LDE strain, Nippon Veterinary and
Life Science University, protocol #29K-44. **One allele, one species, one colony, one sex.**

**Do the authors extend it beyond the allele? Twice, and both extensions must be read exactly:**

1. 🟡 **Model-validity extension:** *"Considering genetic and phenotypic similarities of ⟦lde/lde⟧ rats with
   WOREE syndrome, we conclude that ⟦lde/lde⟧ rat is a model for WOREE syndrome."* — a claim about the
   **model**, not about the mechanism of ataxia.
2. 🟡 **Mechanistic extension to humans, hedged twice over:** *"These findings suggest that retarded neurite
   growth and hypomyelination **may be involved in brain anomalies** occurring in patients with Wwox
   mutations."* — 🔴 note its object: **"brain anomalies"**, i.e. the **MRI** findings (*"hypoplasia,
   dysplasia, and atrophy"*, *"corpus callosum hypoplasia"*, *"delayed myelination and progressive
   demyelination"*). **The authors do NOT extend the ataxia attribution to humans.** No human motor
   phenotype is named in that sentence, and no ataxia is named in it at all.

⇒ **The attribution to ataxia is confined to the rat `lde/lde` allele.** Every use of it outside that allele
is the reader's extrapolation, not the authors'.

### 2.4 🎯 Item 4 — THE HEADLINE: **the structural explanation is NOT CEREBELLAR**

**Verified first-hand from the Methods, exactly as the brief asked.**

| Question | Answer, first-hand |
|---|---|
| Which cerebellar cell population does the explanation concern? | 🔴 **NONE.** No cerebellar cell type — not Purkinje, not granule, not Bergmann glia, not deep-nuclear, not cerebellar oligodendrocyte — is measured, named or counted anywhere in the paper |
| Which tissue does it concern? | 🟢 **Cerebral cortex (layers I–VI, quantified per layer) and corpus callosum / subcortical white matter.** That is the whole of it |
| Does the histology block contain cerebellum? | 🔴 **NO, by construction.** `L2`: *"coronal sections spanning the whole length of the hippocampus"*. A coronal block ending at the caudal hippocampus contains **no cerebellum, no brainstem, no cerebellar peduncle, no spinal cord, no peripheral nerve and no skeletal muscle** |
| Does any biochemical assay reach the mutant cerebellum? | 🔴 **NO.** `L3`: the cerebellum-containing CNS panel is **normal** rats; the mutant blot is *"the whole brain and cerebral cortex"* |
| Is the title consistent with this? | 🟢 **Yes, and it says so plainly:** *"Defective Development of **Cerebral Cortex** with Hypomyelination"* |

> ### 🎯 HEADLINE
> **The "structural explanation" that Tochigi *et al.* 2019 offer for the `lde/lde` neurological phenotype
> is an EXTRA-CEREBELLAR, FOREBRAIN one — cerebral cortex and corpus callosum — measured in a tissue block
> that ends at the hippocampus and therefore could not have seen the cerebellum, the brainstem, the
> peduncles or the cord even if a lesion had been there.**
>
> It therefore **cannot** fill the gap CLAIM 039 names. CLAIM 039's open question is *anatomical
> localisation*; this paper answers a **different** question — *what is wrong in the forebrain* — and then
> proposes, by analogy, that the answer covers *"part of the phenotype"*.
>
> ⇒ 🔴 **Converting "no cerebellar lesion was found" into "the lesion has been found, and it is myelin" is a
> substitution of one compartment for another, licensed by no measurement in either paper.**

### 2.5 🎯 Item 4b — the cerebellar record of the `lde` allele, verified first-hand

Because the brief's adversarial section demands it, I read the **only** `lde` paper that ever put cerebellum
on a slide — **S2, Iacomino 2020** — rather than rely on the census.

#### 🟢 `L4` — Iacomino 2020, Results, verbatim

> *"In addition, the development of cerebellum was delayed in ⟦lde/lde⟧ as shown by reduced number of
> foliation (, arrowheads)."*

#### 🟢 `L5` — its Methods, "Rat Experiments", verbatim, with a parameter the repository does not hold

> *"Resulted pups (**both sexes**) were dissected under the isoflurane anesthesia at **postnatal day 1 (P1)**."*
> *"**Twenty-μm-thick sequential sagittal cryosections were prepared from 1 to 2 mm lateral region to the
> midline.** Almost corresponding sections were used for comparison. **Nissl staining** were performed for
> histological examination."*
> *"Data from each **3** ⟦+/+⟧ and ⟦lde/lde⟧ rats genotyped by PCR were used for statistical analysis."*

🎯 **`1 to 2 mm lateral to the midline` appears nowhere in this repository** (verified by grep). Its
consequence is sharp and new:

> 🔴 **The single cerebellar observation in the entire `lde` literature is PARASAGITTAL — it is not the
> midline vermis.** The human WOREE abnormality this repository repeatedly names is **cerebellar *vermis*
> hypoplasia**, and in the very same paper it is named twice (proband II.1 MRI; fetus II.3 fetal and
> post-mortem MRI). **The one rat section plane that exists is 1–2 mm away from the structure the human
> finding names.** That is not evidence of sparing and it is not evidence of involvement; it is a sampling
> frame that cannot address the question, and it has been read as though it could.

Its remaining parameters, first-hand: **no foliation index, no count, no statistic** attached to the
cerebellar statement (the quantified endpoints are Satb2, Tbr1 and BrdU, all cerebral); **no blinding**;
**no Purkinje marker** — calbindin, Hcn1 and calretinin appear nowhere; **arrowheads on a Nissl panel** are
the entire record. ✅ This **confirms and does not weaken** the `A5` row at
`cerebellar_measurement_census_20260922.md:202`, which already called it *"no number, n=3, unblinded,
arrowheads only"*.

### 2.6 🎯 Item 4c — AND THE ATTRIBUTION WAS NEVER RESTATED, NOT EVEN IN-HOUSE

#### 🟢 `L6` — Iacomino 2020, Discussion, verbatim

> *"Previously, the clinical features of the ⟦lde/lde⟧ rats, characterized by dwarfism, postnatal lethality,
> epilepsy and **ataxic gait**, were related to a spontaneous homozygous 13-bp deletion within the exon 9 of
> ⟦Wwox⟧ (). Wide neuropathological alterations have been described in the postnatal **cerebral cortex** of
> ⟦lde/lde⟧ rats, including **severe hypomyelination (with a reduced number of mature oligodendrocytes)** and
> a significant reduction in cell populations of astrocytes and microglia ()."*

🎯 **Read what this does.** The 2020 paper — **with Tochigi Y as an author and Suzuki H as supervising
author of the animal work**, i.e. the same laboratory and two of the same people — **names the ataxic gait**,
**cites Tochigi 2019 for the hypomyelination**, and places them in **adjacent sentences** — and **does not
join them**. The ataxic gait is attributed to *the mutation*; the hypomyelination is reported as *a
neuropathological description of the cerebral cortex*. **The 2019 attribution is not restated, not defended,
not extended and not cited as an explanation.**

⇒ 🔴 **The attribution has ZERO forward citation weight, including from its own authors in their next paper
on the same allele.** That is a stronger adversarial datum than anything the retrieval census produced, and
it cuts directly against the framing that "the authors already explained it".

#### 🟢 `L9` — and the human proband of that same paper is SPASTIC, not ataxic (Results, verbatim)

> *"Neurological examination showed severe truncal hypotonia, arthrogryposis, **spastic tetraparesis**
> associated with some dystonic movements, **brisk deep tendon reflexes and clonus**."*
> — the same individual whose MRI shows *"hypoplasia of the corpus callosum … and inferior cerebellar
> vermis"* and *"T2 signal alterations of the parietal periventricular and frontal white matter"*.

🔴 Its force is developed in § 5.3(1); it is stated here so that every locator is defined where it is first
used. ⚠️ **n = 1, a different species, a different allele (`p.Arg264Ter`), a 4-year-old child and not a
21-day-old rat.** It refutes nothing. It removes an air of inevitability.

#### 🟢 `L10` — and the human neuropathology went elsewhere (Methods, "Neuropathological Studies", verbatim)

> *"During autopsy, a sample of brain tissue (**parietal coronal section**) was taken, after the brain
> hemispheres had been exposed by means of cutting the scissurae of the parietal and frontal bones."*

⇒ ✅ **CONFIRMS first-hand** the `H1` row of `cerebellar_measurement_census_20260922.md:220` and the `human WOREE neuropathology` row at `:373` and the point of
its § 6.3: the one WOREE fetus that had **cerebellar vermis hypoplasia on MRI** had its **parietal cortex**,
not its cerebellum, put on a slide. **The opportunity to test the cerebellar finding against histology
existed in this very study, and the histology went to a different lobe.**

### 2.7 🎯 Item 7 — THE H1a/H1b FORK, and the brief's framing of it is WRONG

#### 🟢 `L7` — the axon limb, verbatim

> *"The interaction between axons and oligodendrocytes is important for myelination [,], **suggesting** that
> the severe reduction in myelination of ⟦lde/lde⟧ cortices **may result, at least in part**, from the
> **retarded growth of axons predicted by the delayed differentiation of neurons**, as indicated by the
> reduced expression of **MAP2** and reduced immunostaining of **FluoroPan Neuronal marker**."*

#### 🟢 `L8` — the oligodendrocyte limb, the very next sentence, verbatim

> *"**In addition**, the reduced number of APC-positive oligodendrocytes in ⟦lde/lde⟧ cortices **indicates**
> that the marked reduction in myelination is **also** caused by the reduced number of mature
> oligodendrocytes."*

**🔴 CONTRADICTION WITH THE BRIEF, stated plainly.** The brief says *"the same Discussion offers
axon-primary as an **alternative** to myelin-primary"*, and the sibling table at
`ataxia_without_cerebellar_lesion_20260922.md:404` frames it as *"`H1a` myelin-primary **versus** `H1b`
axon-primary"*. **In the authors' own words the two limbs are ADDITIVE, not alternative.** The connectives
are *"In addition"* and *"**also** caused by"*. The authors hold **both**, as partial contributors to one
outcome. **The fork is the repository's construction, not the authors'** — and constructing it as a fork
silently converts a conjunction into a disjunction, which is exactly the kind of re-voicing
`gold_is_in_the_details.md` exists to catch.

**🎯 AND THE AXON LIMB RESTS ON NO AXONAL MEASUREMENT AT ALL.** This is the finding of § 2.7, and the
repository does not hold it:

| The claim | What was actually measured |
|---|---|
| *"retarded growth of **axons**"* | 🔴 **MAP2** — which the same paper defines as *"mainly detected in immature **dendrites**"*. A dendritic marker cannot report axonal growth |
| | 🔴 **FluoroPan Neuronal Marker** — a pan-neuronal stain, reported qualitatively as *"**axon-like** vertical neurite growth"*. *"Axon-like"* is a morphological impression, not an axonal identity |
| | 🔴 **Absent entirely:** neurofilament (SMI-31/SMI-312, NF-H/M/L), Tau-1, βIII-tubulin axonal tracing, axon calibre, axon count, axon density, electron microscopy, g-ratio |
| The verb chain | *"suggesting"* → *"may result, at least in part"* → *"**predicted by**"*. Three hedges in one sentence, and *"predicted by"* concedes that the axonal defect is **inferred, not observed** |

⇒ 🔴 **`H1b` is not a rival hypothesis supported by data. It is an unmeasured inference resting on a
dendritic marker.** Grading it as a coequal fork of `H1a` **over-credits it**.

#### The discriminating measurement, and whether anything cheaper separates them

| Route | What it separates | Cost class | Verdict |
|---|---|---|---|
| **EM: g-ratio + axon-calibre distribution on the same grids** | Fully separates *"thin myelin on normal axons"* (oligodendrocyte-primary) from *"normal-ratio myelin on thin/fewer axons"* (axon-primary) | 🔴 **NEW ANIMAL COHORT** — no `lde` EM exists and paraffin blocks cannot be retro-fitted for ultrastructure | ✅ **The sibling is right that nothing fully cheaper exists.** `ataxia_without_cerebellar_lesion_20260922.md:404` stands |
| 🎯 **Pan-axonal + myelin double-label on the EXISTING paraffin blocks** (e.g. a neurofilament axonal channel against MBP, same 5-µm sections) | **Partially.** Yields axon **density/number** per field against myelin area — enough to reject *"myelin normal per axon, axons merely fewer"*, **not** enough to give a true g-ratio | 🟡 **NEW ANALYSIS ON ARCHIVED MATERIAL — zero animals** | 🟡 **Cheaper, and genuinely informative, but it does not close the fork.** 🔴 **And it is `HUMAN_REQUIRED` and blocked:** it presupposes that 2019 blocks survive at Nippon Veterinary and Life Science University — the unnamed custody question of `cerebellar_measurement_census_20260922.md:549`. **I made no contact** |
| **OPC-stage panel (NG2 / PDGFRα / Olig2) versus APC on the same blocks** | Separates *fewer precursors* from *differentiation arrest* — a **different** fork, already flagged `UNRESOLVED` at `fulltext_dossiers/PMID31340538.md:80-82` | 🟡 archived material, same custody block | ⚪ **Does not address H1a/H1b.** Named so it is not mistaken for a route that does |

🔴 **And the answer that matters more than either limb:** the fork is **undecidable-and-irrelevant to CLAIM
039 as posed**, because **neither limb has ever been connected to a motor phenotype by any measurement, in
any `lde` animal, at any age.** Resolving H1a versus H1b would refine the *cortical myelin* mechanism and
would leave the *ataxia* question exactly where it is.

### 2.8 Item 6 — SCOPE: what transfers and what does not

| Target | Does the attribution transfer? | Why |
|---|---|---|
| **rat `lde/lde`, ♂, PND 5–21, cerebral cortex** | 🟢 **The measurement does.** The *attribution* remains `IPOTESI` even here | It is the measured object |
| **rat `lde/lde`, ♀** | 🔴 **NO.** Males only. And the 2007 ataxia denominator is **19 ♀ + 20 ♂** — the sex in which the myelin was never measured carries half the explanandum | `L5` |
| **rat `lde/lde` beyond PND 21** | 🔴 **NO.** The series **ends at PND 21**; the 2007 histology is at **~28 days**; the seizure window runs 16–63 d. The myelin series stops before the pathology observation begins | `L2`, S3/S5 abstracts |
| **rat `lde/lde`, any non-forebrain compartment** | 🔴 **NO.** Cerebellum, brainstem, peduncles, cord, nerve, muscle: `NOT SECTIONED`, `NOT BLOTTED` in the mutant | § 2.4 |
| **`Wwox`-null mouse (Aqeilan); NCKU `WD1`/`WD234`; `Wwox^gt/gt`; `Syn-Cre` S-KO; `Nestin-Cre` N-KO; `Wwox^P47T/P47T`; `Wwox^ΔCre/ΔCre`** | 🔴 **NO.** Different alleles, different species, different lesion classes. A C-terminal frameshift near-null in rat is not a protein-level null in mouse and is not a PPxY-binding hypomorph | Brief's non-pooling rule; `cerebellar_measurement_census_20260922.md:384-388` |
| **human WOREE (genotype class)** | 🔴 **NO, for ataxia.** The authors' own human extension is to **"brain anomalies"** on MRI, hedged *"may be involved"*, and names no motor sign. 🔴 **And the counter-datum is in the sister paper:** the WOREE proband with cerebellar vermis hypoplasia shows *"severe truncal hypotonia, arthrogryposis, **spastic tetraparesis** … **brisk deep tendon reflexes and clonus**"* (`L9`, S2) — a **pyramidal** picture, not an ataxic one | § 2.3; `L9` |
| **human SCAR12** | 🔴 **NO.** A different genotype class with a different, ataxia-defined presentation; nothing in this paper touches it | — |

**🔴 WHAT DOES NOT TRANSFER, stated as a list so it can be checked:** the sex · every age above PND 21 ·
every compartment outside the forebrain · every other allele and species · the human genotype class for any
**motor** statement · and, within the rat itself, **causality** — because a hedged association measured in
one compartment in one sex is not a cause of a sign measured in another study, in both sexes, at another age,
with no shared animal.

---

## § 3 · THE FOUR-WAY EXPLAINS / CORRELATES ADJUDICATION

**Rule applied:** a source *explains* X only if (i) X is measured in that source, (ii) the proposed
substrate is measured in the same animals, and (iii) the authors assert a causal relation in indicative
mood with a test behind it. Anything less is graded down.

| # | Does Tochigi 2019 explain…? | Explanandum measured **in this paper**? | Substrate measured **in the same animals**? | Authors' modal wording | 🎯 **VERDICT** |
|---|---|---|---|---|---|
| **(a)** | **Ataxia** | 🔴 **NO** — gait enters only as an Introduction citation; **no motor assay exists in the Methods** | 🔴 **NO** — no animal had both gait and myelin assessed | *"Therefore, **part of the phenotype** … **is associated with** hypomyelination"*; bridged by *"Such neurological defects **have been reported in several mutant animals**"* | 🔴 **DOES NOT EXPLAIN. `CORRELATES` AT BEST — and strictly, `CO-OCCURS BY ANALOGY`.** An associative verb, a partitive quantifier, a literature analogy as the only bridge, and **zero** shared animals. `IPOTESI` |
| **(b)** | **Cerebellar pathology** | 🔴 **NO** — cerebellum is **outside the tissue block** (`L2`) and **outside the mutant blot** (`L3`) | 🔴 **NO** | — no statement is made | 🔴 **DOES NOT ADDRESS. `OUT OF SAMPLING FRAME`.** Not a negative result; **`NOT MEASURED`**, which is not `NORMAL` |
| **(c)** | **Purkinje degeneration** | 🔴 **NO** | 🔴 **NO** | — no statement is made | 🔴 **`NEVER MEASURED`** — and not merely here: **no Purkinje marker of any kind (calbindin, Hcn1, calretinin, Pcp2) has ever been applied to any `lde` animal, at any age, in any of the six papers of the closed `lde` corpus.** Consistent with `cerebellar_measurement_census_20260922.md:369` |
| **(d)** | **Merely co-occur** | n/a | n/a | n/a | 🟢 **YES — and this is the HIGHEST DEFENSIBLE GRADE.** Cortical hypomyelination (measured: ♂, PND 5–21, n ≥ 3, coronal hippocampal block, unblinded) and ataxic gait (observed: both sexes, 21 d, 95%/0%, observational, unblinded, a different paper 12 years earlier) are **two properties of the same strain that were never measured in the same animal, the same sex, the same age window, the same region or the same section** |

> 🎯 **VERDICT IN ONE LINE.** Tochigi 2019 supplies a **hedged, extra-cerebellar, analogy-bridged
> association** between forebrain hypomyelination and *"part of the phenotype"* of the `lde/lde` rat. It is
> `IPOTESI`, not `DATO`; it is **forebrain**, not cerebellar; and it **explains neither the ataxia, nor
> cerebellar pathology, nor Purkinje degeneration.** Row **(d)** is the only row that survives.

---

## § 4 · PROPOSED CHANGES TO CLAIM 039 — **PROPOSED, NOT PROPAGATED**

🔴 **I am READ-ONLY toward `claim_registry_current.md`. Nothing below has been applied. CLAIM 039 is a gated
claim and this is an Operator decision.** If the Operator authorises it, the change belongs in a commit
candidate and a `BATCH_COMMIT`, not here.

⚠️ **My recommendation is DELIBERATELY MINIMAL, and it is NOT the edit the overnight finding invites.**
The finding *feels* like it should soften *"non ha spiegazione strutturale"*. It should not: that clause is
**true of PAPER 059** and the sentence already says *"in questo paper"*. The defect is **incompleteness as a
statement about the state of knowledge**, and the honest repair is an **addition** that is itself
**restrictive**, because what exists is not a cerebellar explanation.

### EDIT 1 — scope-guard on the opening clause (additive; nothing deleted)

**BEFORE** (exact string, `claim_registry_current.md` CLAIM 039, `Evidence boundary`, opening):

```
**Evidence boundary:** L'atassia **non ha spiegazione strutturale** in questo paper: il cervelletto è istologicamente indenne e nessun'altra regione, oltre a ippocampo e amigdala, mostra alterazioni al microscopio ottico.
```

**AFTER** (exact string proposed):

```
**Evidence boundary:** L'atassia **non ha spiegazione strutturale** in questo paper: il cervelletto è istologicamente indenne e nessun'altra regione, oltre a ippocampo e amigdala, mostra alterazioni al microscopio ottico. ⚠️ **La clausola vale di [[paper_registry_current#PAPER 059]] e non dello stato delle conoscenze**: un'attribuzione strutturale pubblicata esiste, è **extra-cerebellare** ed è `IPOTESI` — limb (d).
```

### EDIT 2 — insert a new limb (d) immediately before the `REVIVAL_TRIGGER` sentence

**INSERTION ANCHOR** (exact string; the new text goes **immediately before** it, nothing deleted):

```
🔴 **Nessuna delle due, né insieme, stabilisce una relazione causale fra cervelletto e fenotipo funzionale.** `REVIVAL_TRIGGER`:
```

**TEXT TO INSERT** (exact string proposed):

```
(d) 🔴 **Narrowing 2026-09-23 — esiste UNA attribuzione strutturale pubblicata, ed è EXTRA-CEREBELLARE e `IPOTESI`.** [[paper_registry_current#PAPER 021]] (Tochigi 2019, PMID 31340538 / PMC6678113, CC BY) scrive in Discussion, verbatim: *"In `lde/lde` rats, epileptic seizures and ataxic gait occur after PND 16 […]. Such neurological defects have been reported in several mutant animals showing hypomyelination […]. Therefore, part of the phenotype of `lde/lde` rats is associated with hypomyelination, accompanied by a reduced number of mature oligodendrocytes."* ⚠️ **Non è un DATO, non riguarda il cervelletto e non spiega l'atassia.** (i) Verbo *"is associated with"*, quantificatore *"part of the phenotype"*, e **premessa portante un'analogia con altri mutanti ipomielinizzanti** — non una misura: `PREMISE: ANALOGY_TO_OTHER_MUTANTS`. (ii) **In quel paper l'atassia non è misurata**: entra solo come citazione di letteratura in Introduzione; nei Methods non esiste alcun test motorio, comportamentale o elettrofisiologico. **Nessun animale ha avuto misurati insieme mielina e andatura.** (iii) 🔴 **Il blocco istologico non contiene cervelletto**: Methods § 4.3, *"sectioning into 5-µm-thick sequential coronal sections spanning the whole length of the hippocampus"*. Ogni misura MBP/CNP/APC è **corteccia cerebrale e corpo calloso**; il western che nomina il cervelletto è sui **normali**, mentre nel mutante il blot è *"the whole brain and cerebral cortex"*. (iv) Parametri: **solo maschi**, *"At least three affected and three normal males"*, PND 5/10/15/21, **nessuna dichiarazione di cecità**, nessuna randomizzazione, t-test non corretti, cucciolata ridotta a <5 per favorire la sopravvivenza dei mutanti. (v) 🔴 **`NEVER MEASURED`: nessuna misura di conduzione nervosa, EMG, g-ratio, microscopia elettronica, rotarod, footprint o balance-beam esiste in TUTTA la letteratura WWOX** — censimento PubMed 2026-09-23, query dedicata → **3 record, tutti e tre falsi positivi su "electron microscopy"** (PMID 40006511, 33300063, 15664696). (vi) **L'attribuzione non è mai stata ripetuta, nemmeno in casa:** [[paper_registry_current#PAPER 020]] (Iacomino 2020), che ha Tochigi e Suzuki fra gli autori, nomina l'andatura atassica e cita Tochigi 2019 **per la sola ipomielinizzazione**, in frasi adiacenti, **senza unirle**. ⇒ **La clausola «non ha spiegazione strutturale» resta vera di PAPER 059; come affermazione sullo stato delle conoscenze è incompleta, ma ciò che esiste è un'ipotesi ipomielinizzante di PROSENCEFALO, non una spiegazione cerebellare, e non sposta di un passo la domanda anatomica di questa claim.**
```

### EDIT 3 — wikilinks

**BEFORE** (exact):

```
**Wikilinks:** [[paper_registry_current#PAPER 059]] · [[claim_registry_current#CLAIM 037]]
```

**AFTER** (exact proposed):

```
**Wikilinks:** [[paper_registry_current#PAPER 059]] · [[paper_registry_current#PAPER 020]] · [[paper_registry_current#PAPER 021]] · [[claim_registry_current#CLAIM 037]]
```

### 🔴 WHAT I EXPLICITLY DO **NOT** PROPOSE

- ❌ **No change to `Status` (`in observation`), `Type` (`DATO`), `Transferability` (`T3`),
  `clinical relevance` (`INDIRECT`) or `Impact on Working Model` (`nessun cambio BLOCCO 1`).** Nothing here
  moves any of them.
- ❌ **No deletion of the clause *"non ha spiegazione strutturale"*.** It is true of its paper.
- ❌ **No change to the existing `REVIVAL_TRIGGER`.** Limb (d) does **not** satisfy it: a forebrain myelin
  association is neither a quantitative cerebellar endpoint nor a motor battery. The trigger stays armed.
- ❌ **No change to CLAIM 037, CLAIM 038, CLAIM 016, PAPER 020, PAPER 021, the working model, the discovery
  ledger, `DL-MECH-026/027`, any queue or any receipt.**
- ❌ **No new claim.** The attribution is `IPOTESI` in the source and would be a hypothesis-ledger object at
  most, not a claim — and I propose no ledger entry either.
- ❌ **No contact with any laboratory, author, foundation or institution.** The 2019 block-custody question
  remains `HUMAN_REQUIRED` and untouched.

### 🟡 One incidental registry defect found, reported, NOT repaired

`paper_registry_current.md` PAPER 021 carries, at `:480`, a *"Role correction (BATCH_20260806_002)"* that
reclassifies the paper **from** *"prenatal cortex / myelin assembly anchor"* **to** *"early postnatal
cortical neurite/glial/myelin maturation anchor (PND5–21)"* — and then, at `:494`, the **`Role:` field still
reads `prenatal cortex / myelin assembly anchor`**, i.e. the superseded value the correction supersedes.
🔴 **The correction was written and the field it corrects was never changed.** This is the **same propagation
failure mode** as CLAIM 016, CLAIM 039 limb (b) and § 2.1b — **fourth instance**, and the first one found in
the *paper* registry rather than the claim registry. 🔴 **I propose no edit; I am read-only and this is an
Operator decision.**

---

## § 5 · ADVERSARIAL VERIFICATION OF MY OWN CONCLUSION

**The attractive finding, named so it can be resisted:** *"the authors already explained the ataxia"* closes
a debate, converts an absence into a mechanism, and flatters the corpus. Per § 21 of the brief I apply more
pressure to it, not less.

### 5.1 `DATO` or `IPOTESI`, in the authors' own words?

🔴 **`IPOTESI`, on five independent grounds, each from the sentence itself:**

1. **The verb is associative:** *"is **associated with**"* — not *"causes"*, not *"results from"*, not
   *"is due to"*. The paper uses causal language freely elsewhere (*"is **also caused by** the reduced number
   of mature oligodendrocytes"*, `L8`) — so the associative verb here is a **choice**, not a house style.
2. **The quantifier is partitive:** *"**part of** the phenotype"*. **Which part is not specified.** The
   phenotype includes dwarfism, lethality, hypogonadism, uraemia, GH deficiency, seizures and ataxic gait.
   The sentence does **not** single out the ataxia, and reading it as an ataxia explanation **over-resolves
   it**. 🔴 **This is a correction to the framing in the brief and in the sibling file**, both of which treat
   the sentence as being about the ataxia specifically.
3. **The bridge is an analogy:** *"Such neurological defects have been **reported in several mutant
   animals**"* — other mutants, unnamed, unrecoverable (§ 0.2).
4. **"Therefore" carries no test.** No statistic, no correlation coefficient, no manipulation, no
   intermediate variable links the myelin measure to any neurological measure.
5. **The explanandum is not in the study.** The ataxia is a citation, not an observation (§ 2.2).

### 5.2 `NEVER MEASURED` — answered per axis, first-hand

🟢 **The `lde` corpus is CLOSED and I enumerated it this act.** PubMed, 2026-09-23:
`("lethal dwarfism with epilepsy") OR (lde AND rat AND Wwox)` → **6 records, total_count 6**:
`17803050` (2007 phenotype), `18676360` (2008 testis), `19500159` (2009 mapping + audiogenic),
`24456803` (2014 **human**, cites `lde` as comparator), `31340538` (2019 cortex), `32581702` (2020 migration).
**There is no seventh `lde` paper.** Every verdict below is therefore over a complete set.

| Axis | Verdict | Basis |
|---|---|---|
| **Nerve conduction / conduction velocity / EMG / compound action potential** | 🔴 **`NEVER MEASURED` — in the entire WWOX literature, not merely in `lde`** | `(WWOX OR Wwox) AND ("nerve conduction" OR "conduction velocity" OR electromyography OR "compound action potential" OR "g-ratio" OR "electron microscopy" OR rotarod OR footprint OR "balance beam")` → **3 records**, and 🔴 **all three are false positives matching only on *electron microscopy***: `40006511` (bladder-cancer hydrogel SEM/TEM), `33300063` (ovarian-carcinoma autophagosome TEM), `15664696` (retinal immuno-EM). **Positive control:** the same surface returns 6 for the `lde` query and 31 for `(WWOX OR Wwox) AND (ataxia OR ataxic)` (`ataxia_without_cerebellar_lesion_20260922.md:322`) |
| **g-ratio / myelin ultrastructure** | 🔴 **`NEVER MEASURED`**, any allele, any species | same query |
| **Quantitative motor battery (rotarod, footprint, kinematics, beam, pole, ledge)** | 🔴 **`NEVER MEASURED` in any `lde` animal** | same query → 0 non-spurious; 2019 Methods carry no behavioural assay; 2020 Methods carry none |
| **Any motor observation in `lde`** | 🟡 **ONE, observational and unblinded:** *"95% of the mutant rats had an ataxic gait"* (S3 abstract, first-hand). 🔴 PubMed indexes it under MeSH **`Lameness, Animal`** — **not** `Ataxia` — a retrieval hazard: the founding observation is invisible to an ataxia-keyed MeSH query | S3 |
| **Cerebellar histology in `lde`** | 🟡 **TWICE, both qualitative, neither quantified:** (1) the 2007 Discussion negative, whose n, age, stain and plane are unrecorded in all 32 locators (`claim_registry_current.md:726`); (2) the 2020 P1 Nissl foliation, arrowheads only, n=3, unblinded, **parasagittal 1–2 mm lateral to midline** (`L4`, `L5`) | § 2.5 |
| **Purkinje cells in `lde`** | 🔴 **`NEVER MEASURED`** — no calbindin, Hcn1, calretinin or Pcp2 in any of the six papers | § 3 row (c) |
| **Cerebellar molecular assay in mutant `lde`** | 🔴 **`NEVER MEASURED`** — the only cerebellar western is **wild-type** (`L3`) | § 2.2 |
| **Vision, vestibular function, proprioception, peripheral nerve, muscle in `lde`** | 🔴 **`NEVER MEASURED`**, all five | corpus enumeration + 2019/2020 Methods |

### 5.3 Does forebrain hypomyelination plausibly produce a 95%-penetrant ataxic gait?

🔴 **This is an unexamined inferential leap, and five independent facts weigh against it.**

1. 🎯 **The human counterpart of the attributed mechanism produces SPASTICITY, not ataxia.** `L9`,
   S2 Results, verbatim: *"Neurological examination showed severe truncal hypotonia, arthrogryposis,
   **spastic tetraparesis** associated with some dystonic movements, **brisk deep tendon reflexes and
   clonus**."* This proband has WOREE with **cerebellar vermis hypoplasia** on MRI **and** *"T2 signal
   alterations of the parietal periventricular and frontal white matter"* — i.e. the human with **both** the
   cerebellar finding and the forebrain white-matter finding presents with a **pyramidal** syndrome.
   ⚠️ **Stated fairly:** n = 1, a different species, a different allele (`p.Arg264Ter`), and a 4-year-old
   child is not a 21-day-old rat. It does not refute the attribution. **It removes its air of inevitability**,
   and it is a first-hand datum that the repository does not hold.
2. **The penetrance arithmetic does not exist.** 95%/0% is an **incidence across 39 mutants and 26 normals**
   (CLAIM 039). The myelin result is a **group-mean difference in n ≥ 3 males per age**. **No penetrance, no
   per-animal distribution and no severity grading is reported for the myelin phenotype in any paper.** An
   attribution from a group mean to a 95%-penetrant sign has **no arithmetic behind it at all**.
3. **The temporal lag is unaddressed.** The myelin deficit is already maximal-by-detection at **PND 5**, the
   earliest age sampled (so its true onset is **unbracketed**); the gait sign appears **after PND 16**. An
   ≥ 11-day gap with **no intermediate measurement of anything**, and the authors do not discuss it.
4. **The authors' own sentence couples the ataxia to the seizures, not to the myelin.** *"epileptic seizures
   **and** ataxic gait occur after PND 16"* — the two share a lower bound, and a post-ictal or
   seizure-burden-driven gait abnormality is at least as available. (This limb is already recorded, against
   its own author, at `ataxia_without_cerebellar_lesion_20260922.md:409`; I do not re-claim it.)
5. **The animal is systemically ill.** At 21 d it weighs **~56%** of normal, is **uraemic** (BUN 10.1 → 35.6
   ♂; 12.6 → 40.3 ♀), has **decreased plasma growth hormone** (S3 abstract, first-hand) and in 34% of cases
   convulses. 🔴 **"Ataxic gait" was scored observationally and unblinded in such an animal.** Cachexia,
   uraemic myopathy, skeletal dysplasia and weakness are not excluded by any measurement, and an
   **unblinded** observer scoring gait in a visibly dwarfed animal is the textbook setting for
   expectation-driven misclassification.

#### 🔴 Rival substrates the attribution does not exclude — enumerated

| # | Rival | Status in `lde` | Excluded by the attribution? |
|---|---|---|---|
| **R1** | **Cerebellar cortex / foliation** | P1 delay documented, **parasagittal, unquantified**; nothing at 21–28 d | 🔴 **NO** — outside the 2019 block entirely |
| **R2** | **Purkinje cell population** | `NEVER MEASURED` | 🔴 **NO** |
| **R3** | **Brainstem, cerebellar peduncles, deep cerebellar nuclei** | `NOT SECTIONED`; Wwox protein present there in **normals** (`L3`) | 🔴 **NO** |
| **R4** | **Spinal cord / dorsal columns** | `NOT SECTIONED`; protein present in normal cord (`L3`) | 🔴 **NO** |
| **R5** | **Peripheral nerve / Schwann cell** | `NEVER LOOKED FOR` in `lde`. 🔴 SIBLING-ATTESTED that the `Wwox`-deficient **mouse** carries *"peripheral nerve demyelination due to Schwann cell apoptosis"* and *"onion-bulb degeneration"* (`wwox_myelin_oligodendrocyte_census_20260921.md:116`) — **a different allele and species; a template, not evidence about `lde`** | 🔴 **NO** |
| **R6** | **Vestibular / labyrinthine** | `NEVER MEASURED` anywhere in WWOX | 🔴 **NO** |
| **R7** | **Corticospinal / upper motor neuron** | Never tested in `lde`; and **the human datum points here** (`L9`) | 🔴 **NO** — and cortical white-matter loss is *more* naturally a pyramidal substrate than a cerebellar one |
| **R8** | **Neuromuscular / muscle** | CPK ♀ ~8.5× higher, **unmarked for significance** (CLAIM 038, `:711`); no CK, no mass, no NMJ in `lde` | 🔴 **NO** |
| **R9** | **Seizure burden / post-ictal state** | 34% seizure incidence; shared PND 16 lower bound | 🔴 **NO** |
| **R10** | **Vision** | WOREE carries retinopathy and optic atrophy; **no `lde` visual assessment exists**, and **no vision-dependent motor comparison has ever been run in any WWOX model** (`ataxia_without_cerebellar_lesion_20260922.md:347`, `P6`) | 🔴 **NO** |
| **R11** | **Systemic / constitutional** (dwarfism, uraemia, GH deficiency, cachexia) | Measured and severe; never controlled for in any gait statement | 🔴 **NO** |
| **R12** | **Under-measurement of the explanandum itself** — *"ataxic gait"* as an unblinded observational label rather than a measurement | 🔴 **Live.** No kinematic definition, no scoring protocol, no inter-rater statistic exists | 🔴 **NO** |

⇒ **Twelve rivals, zero excluded.** The attribution is compatible with all of them because it excludes none
of them — which is precisely what an association bridged by analogy does.

### 5.4 Adversarial test of **my own** headline

| Challenge to me | My answer |
|---|---|
| *"You call it extra-cerebellar, but the 2019 western shows Wwox in cerebellum — so the biology is cerebellar too."* | 🟢 **Conceded on biology, rejected on evidence.** The protein's **presence** in normal cerebellum (`L3`) says nothing about **pathology** in the mutant, whose cerebellum was neither sectioned nor blotted. My headline is about the **sampling frame of the explanation offered**, not about where WWOX is |
| *"'Part of the phenotype' might mean the ataxia."* | 🟢 **It might.** I say so explicitly in § 5.1(2). **That is my point:** it is unspecified, and the repository should not resolve an author's ambiguity in the direction that makes the finding larger |
| *"You are over-reading the Methods; maybe cerebellum was in some sections."* | 🔴 **No.** A **coronal** block *"spanning the whole length of the hippocampus"* terminates rostral to the cerebellum by construction. And the **mutant western** independently confirms the gap (`L3`). Two independent modalities, same answer |
| *"Your `NEVER MEASURED` verdict is one query."* | 🟡 **Fair, and bounded.** It is one **multi-term** query over a **closed 6-record corpus** I enumerated separately, with a stated positive control and every hit inspected individually. A query census is a statement about what a query returns, not about biology; a non-indexed measurement in a figure panel I did not open would evade it |
| *"Iacomino 2020 not restating the attribution proves nothing — papers omit things."* | 🟢 **Conceded as proof; retained as weight.** Non-restatement is not refutation. But the 2020 paper places the ataxic gait and the Tochigi hypomyelination in **adjacent sentences** and **declines to join them**, with two of the 2019 authors present. That is an informative omission, and I grade it as weight, not proof |
| *"You read only two primaries."* | 🟢 **True.** S3 and S4 are abstract-depth and S3's body is unobtainable. Every statement resting on them is marked 🟡 or 🔴 SIBLING-ATTESTED above |

---

## § 6 · WHAT I COULD NOT VERIFY — exhaustive and unflattering

1. 🔴 **The reference numbers behind the analogy.** *"Such neurological defects have been reported in
   **several mutant animals showing hypomyelination** [,,,]"* — **I cannot name a single one of those
   mutants.** The served text strips citation numbers; the XML routes are proxy-blocked; the reference list
   is absent from the served body. **The entire evidential base of the attribution's middle premise is
   opaque to me.** Consequence: I cannot check whether those mutants are forebrain-hypomyelinating (which
   would support the analogy) or globally hypomyelinating including cerebellum, brainstem and cord (which
   would **undercut** it, because their ataxia could be cerebellar or spinal). 🎯 **This is the single most
   consequential gap in this file, and it is cheap to close for anyone with the marked-up PDF.**
2. 🔴 **The italicised genotype tokens.** Every ⟦⟧ in this file is a reconstruction. I justified the
   convention (§ 0.2) but I did not *observe* the tokens.
3. 🔴 **Two egress routes refused.** Europe PMC `fullTextXML` and NCBI `efetch db=pmc` both returned
   `CONNECT tunnel failed / 403 connect_rejected`. I did not work around the proxy and I did not disable TLS
   verification.
4. 🔴 **The manifest's own source artefact does not exist here.** `deepdive_manifests/PMID31340538.json`
   names `files/fulltext/PMID31340538_Tochigi2019.xml` with a sha256, plus six figure JPEGs — and
   **`files/` is absent from this edition**. So the 2026-08-06 locators are **unverifiable against their
   artefact** in the public edition. I verified them against the **live PMC body** instead, and all eleven
   reproduce. This is a structural gap in the public edition's auditability, not a defect of that read.
5. 🔴 **No figure panel inspected — in either paper.** I did not open Figure 4 (MBP/CNP/APC) or Figure 3 of
   Iacomino 2020 (the Nissl panel whose **arrowheads are the entire cerebellar record of the `lde` allele**).
   🔴 **I therefore cannot say what those arrowheads show**, and neither can any repository file.
6. 🔴 **PMID 17803050 remains unobtainable.** No DOI, no PMCID, confirmed again this act. The 95% figure, the
   19♀/20♂ denominator, the *"no marked pathologic changes in the cerebella"* sentence and the 32 locators
   are **SIBLING-ATTESTED** from `fulltext_dossiers/PMID17803050.md`; I verified only what the **abstract**
   carries (95% ataxic gait; hippocampal/amygdalar vacuoles; the serum panel; MeSH `Lameness, Animal`).
7. 🔴 **PMID 18676360 (Takenaka 2008) remains at ABSTRACT depth**, and remains the acquisition gap the
   sibling flagged. Its abstract independently pins the vacuole histology to **28 days** and the seizure
   window to **16–63 days**, and its own sampling frame is **testis, accessory sex organs and anterior
   pituitary**. **It is still absent from every registry, queue, ledger and dossier** (verified this act).
8. 🔴 **Whether the 2019 paraffin blocks or the 2020 cryoblocks still exist** at Nippon Veterinary and Life
   Science University. This gates the only cheap partial route in § 2.7. `HUMAN_REQUIRED`. **I made no
   contact of any kind and drafted none.**
9. 🔴 **Whether any unindexed measurement exists** in a figure, a supplement or a non-English source that my
   queries cannot see. A query census bounds retrieval, not reality.
10. 🟡 **The 95% collision, noted and NOT resolved.** *95%* is the **ataxic-gait** incidence in S3 (2007) and
    **also** the **audiogenic-seizure** incidence in S4 (2009) — *"Sound stimulation induced epileptic
    seizures in 95% of `lde/lde` rats"* (first-hand, abstract). The registry keeps them apart (CLAIM 039 vs
    CLAIM 037) and I found **no file that conflates them**. 🔴 **I flag it as a standing collision hazard for
    any future reader**, and verify nothing further.
11. 🔴 **I did not verify the sibling files' claims about alleles I did not read** — `P47T`, the NCKU nulls,
    the Aqeilan AAV programme, the Cre conditionals. § 2.8's non-transfer row cites
    `cerebellar_measurement_census_20260922.md` § 4.3 **as read**, and rebuilds nothing.
12. 🔴 **I did not open `deepdive_manifests` for any paper other than 31340538**, so I cannot say whether the
    same locator-coverage gap exists elsewhere.

---

## § 7 · NOVELTY GRADE — conservative

### 7.1 What is NOT novel, stated first

- 🔴 **The existence of the attribution is NOT my finding.** `ataxia_without_cerebellar_lesion_20260922.md`
  § 6.1 found it on 2026-09-22 and graded its own favoured hypothesis `A REDISCOVERY` for it. **I confirm it;
  I do not claim it.**
- 🔴 **The hippocampus-spanning block is NOT my finding** — same file § 6.2, and the `A4` row of the census.
- 🔴 **The `lde` non-cerebellar sampling frame, the allele matrix, the `A-f4` split, the
  `LIGHT_MICROSCOPY_FLOOR` premise and the P1 foliation counter-evidence are all pre-existing.**
- 🔴 **`NOT MEASURED ≠ NORMAL` is the repository's own principle**, already carried by CLAIM 039.

### 7.2 What IS new in this act — seven items, graded

| # | New item | Grade | Basis |
|---|---|---|---|
| **N1** | 🎯 **The authors hold axon-primary and oligodendrocyte-primary ADDITIVELY (*"In addition"*, *"**also** caused by"*), not as alternatives. The H1a/H1b *fork* is the repository's construction, not the authors'** | **C — NOVEL CONNECTION**, and it **corrects the brief** | `L7`, `L8` |
| **N2** | 🎯 **The *"retarded growth of axons"* limb rests on MAP2 — which the same paper calls a marker *"mainly detected in immature **dendrites**"* — plus a qualitative *"axon-like"* pan-neuronal stain. No axonal marker, calibre, count or ultrastructure exists. `H1b` is an unmeasured inference, not a coequal hypothesis** | **C — NOVEL CONNECTION** | § 2.7; verified absent from the repository by grep |
| **N3** | 🎯 **The attribution was never restated — not by the same laboratory, with two of the same authors, in the next `lde` paper, which cites Tochigi 2019 for the hypomyelination in a sentence adjacent to one naming the ataxic gait and declines to join them** | **C — NOVEL CONNECTION** | `L6` |
| **N4** | 🎯 **The only cerebellar section plane in the `lde` literature is PARASAGITTAL, *"1 to 2 mm lateral region to the midline"* — not the midline vermis that the human WOREE finding names, in the same paper** | **C — NOVEL PARAMETER**; the string appears nowhere in the repository | `L5` |
| **N5** | 🎯 **The WOREE proband in that same paper is SPASTIC, not ataxic — *"spastic tetraparesis … brisk deep tendon reflexes and clonus"* — while carrying both cerebellar vermis hypoplasia and frontal/parietal white-matter signal change** | **C — NOVEL ADVERSARIAL DATUM**, n = 1, cross-species, held at its weight | `L9` |
| **N6** | 🎯 **The zero for conduction / EMG / g-ratio / EM / rotarod / footprint / beam is FIELD-WIDE, not `lde`-restricted — 3 hits, all three false positives — and the `lde` corpus is CLOSED at exactly 6 records** | **B — EXTENSION** of the sibling's `lde`-scoped `P1` | PubMed censuses, 2026-09-23 |
| **N7** | 🟡 **PAPER 021's `Role:` field still carries the value its own `Role correction` line supersedes — fourth instance of the propagation defect, and the first in the *paper* registry** | **B — AUDIT FINDING** | `paper_registry_current.md:480` vs `:494` |

### 7.3 Overall grade

> **B, with three C-grade components (N1, N2, N3).**
> 🔴 **No new experiment, no new claim, no new mechanism, no promotion.** This act is a **verification and
> boundary-sharpening** act: it converts a sibling's first-hand finding into an independently verified one,
> **corrects two features of how that finding was framed** (the fork; "the ataxia" for "part of the
> phenotype"), **relocates the explanation from cerebellum to forebrain as a headline**, and **reduces the
> attribution's standing** rather than raising it. Grading it higher would be exactly the error § 5 exists
> to prevent.

---

## § 8 · SOURCE ATTRIBUTION

🔵 **According to PubMed / PubMed Central.** All bibliographic records, abstracts, MeSH terms, query counts
and full texts used in this file were retrieved from PubMed and PubMed Central via the PubMed MCP tools on
**2026-09-23**.

### Primary sources

| Source | Citation | Identifiers | Depth |
|---|---|---|---|
| **S1** | Tochigi Y, Takamatsu Y, Nakane J, Nakai R, Katayama K, Suzuki H. *Loss of Wwox Causes Defective Development of Cerebral Cortex with Hypomyelination in a Rat Model of Lethal Dwarfism with Epilepsy.* **Int J Mol Sci** 2019;20(14):3596. CC BY | PMID `31340538` · PMCID `PMC6678113` · [DOI](https://doi.org/10.3390/ijms20143596) | 🟢 FULL BODY + METHODS, first-hand |
| **S2** | Iacomino M, Baldassari S, Tochigi Y, Kośla K, Buffelli F, Torella A, Severino M, Paladini D, Mandarà L, Riva A, Scala M, Balagura G, Accogli A, Nigro V, Minetti C, Fulcheri E, Zara F, Bednarek AK, Striano P, Suzuki H, Salpietro V. *Loss of Wwox Perturbs Neuronal Migration and Impairs Early Cortical Development.* **Front Neurosci** 2020;14:644 | PMID `32581702` · PMCID `PMC7300205` · [DOI](https://doi.org/10.3389/fnins.2020.00644) | 🟢 FULL BODY + METHODS, first-hand |
| **S3** | Suzuki H, Takenaka M, Suzuki K. *Phenotypic characterization of spontaneously mutated rats showing lethal dwarfism and epilepsy.* **Comp Med** 2007;57(4):360–369 | PMID `17803050` · **no DOI, no PMCID** | 🟡 ABSTRACT + MeSH first-hand; body 🔴 SIBLING-ATTESTED |
| **S4** | Suzuki H, Katayama K, Takenaka M, Amakasu K, Saito K, Suzuki K. *A spontaneous mutation of the Wwox gene and audiogenic seizures in rats with lethal dwarfism and epilepsy.* **Genes Brain Behav** 2009;8(7):650–660 | PMID `19500159` · [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x) | 🟡 ABSTRACT + MeSH, first-hand |
| **S5** | Takenaka M, Yagi M, Amakasu K, Suzuki K, Suzuki H. *Retarded differentiation of Leydig cells and increased apoptosis of germ cells in the initial round of spermatogenesis of rats with lethal dwarf and epilepsy (lde/lde) phenotypes.* **J Androl** 2008;29(6):669–678 | PMID `18676360` · [DOI](https://doi.org/10.2164/jandrol.108.005066) | 🟡 ABSTRACT, first-hand |
| **S6** | Abdel-Salam G, Thoenes M, Afifi HH, Körber F, Swan D, Bolz HJ. *The supposed tumor suppressor gene WWOX is mutated in an early lethal microcephaly syndrome…* **Orphanet J Rare Dis** 2014;9:12 | PMID `24456803` · PMCID `PMC3918143` · [DOI](https://doi.org/10.1186/1750-1172-9-12) | 🟡 ABSTRACT, first-hand |
| **FP1–FP3** | False positives of the conduction/EM query, inspected and rejected: Liu CW *et al.* **Pharmaceutics** 2025 (PMID `40006511`, [DOI](https://doi.org/10.3390/pharmaceutics17020143)); Zhao Y *et al.* **Mol Med Rep** 2020 (PMID `33300063`, [DOI](https://doi.org/10.3892/mmr.2020.11754)); Chen ST *et al.* **Neuroscience** 2005 (PMID `15664696`, [DOI](https://doi.org/10.1016/j.neuroscience.2004.07.054)) | — | 🟡 ABSTRACT, first-hand; **used only as negatives** |

### Queries run this act (PubMed, 2026-09-23)

| Query | Count | Use |
|---|---|---|
| `("lethal dwarfism with epilepsy") OR (lde AND rat AND Wwox)` | **6** | Closed-corpus enumeration (§ 5.2) |
| `(WWOX OR Wwox) AND ("nerve conduction" OR "conduction velocity" OR electromyography OR "compound action potential" OR "g-ratio" OR "electron microscopy" OR rotarod OR footprint OR "balance beam")` | **3**, all false positives | Field-wide `NEVER MEASURED` (§ 5.2) |

⚠️ **A query census is a statement about what a query returns, not about biology.**

### Repository sources cited (read directly this act, not re-derived)

`disease-models/wwox/analysis/ataxia_without_cerebellar_lesion_20260922.md` §§ 6.0–6.3 ·
`disease-models/wwox/analysis/cerebellar_measurement_census_20260922.md` § 4.3, §§ 6.1–6.4 ·
`disease-models/wwox/analysis/wwox_myelin_oligodendrocyte_census_20260921.md` `:330-375` ·
`disease-models/wwox/analysis/lde_myelin_vacuole_bridge_20260922.md` §§ 0–2.1 ·
`disease-models/wwox/registries/claim_registry_current.md` CLAIM 016 / 037 / 038 / 039 ·
`disease-models/wwox/registries/paper_registry_current.md` PAPER 021 ·
`disease-models/wwox/research/fulltext_dossiers/PMID31340538.md` ·
`disease-models/wwox/research/deepdive_manifests/PMID31340538.json`.

---

🔴 **NOT CANONICALIZED. NOTHING PROPAGATED. CLAIM 039 IS A GATED CLAIM AND § 4 IS A PROPOSAL ONLY.**
🔴 **Nothing in this file is medical advice.**
