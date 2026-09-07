# WWOX Therapeutic Translation — Second Pass: Rescue, Directionality, Disease Modification

**A stress test of the conclusions in [`mechanism_intervention_map.md`](mechanism_intervention_map.md) that most affect prioritization.**
It does not extend the drug list — **no new candidate molecule is named anywhere in this file.** The only
entry it adds is a **negative**. What it does is separate four things the first pass allowed to blur:

| | |
|---|---|
| **SYMPTOM CONTROL** | the endpoint moves; the mechanism is untouched |
| **MECHANISTIC RESCUE** | a WWOX-dependent molecular state is measurably corrected |
| **DEVELOPMENTAL RESCUE** | a developmental/cognitive trajectory measurably changes |
| **DISEASE MODIFICATION** | the last two, in a system where the first is controlled for |

> **Status:** non-canonical analysis artefact, same class as the map it stress-tests.
> **READ-ONLY toward the four scientific current files.** Nothing here changes a claim, a paper record,
> the working model or the tracking log. Where it finds a defect in a canonical file, it **reports** it —
> §8 lists them — and the repair goes through INGEST → DEEP_DIVE → COMMIT, not through this file.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
> Alleles appear only as decoupled worked examples.
>
> **No clinical recommendation is formulated anywhere in this file. Nothing here is medical advice.**

---

## 0 · Surfaces searched, and their denominators

Every negative below is reproducible, and every negative carries the population it was measured over.
This section exists so no figure in this file can be read without knowing what it was drawn from
— and so the same figures can be re-measured later without guessing what "everything" meant.

| Surface | Population | Note |
|---|---|---|
| `disease-models/wwox/**/*.md` | the whole disease model | claims, ledgers, metas, dossiers, trackers |
| `registries/paper_registry_current.md` | **426 records** = 70 `PAPER` + 168 `CORPUS-STUB` + 188 `CORPUS P` (413 carry a `**Full title:**` line; 11 further `## ` headings are structural, not records) | the `CORPUS-STUB` and `CORPUS P` entries are catalogued, **not read** |
| `research/deepdive_manifests/*.json` | 64 manifests | verbatim locators, incl. image-read locators |
| `files/fulltext/` | **16 entries** = 7 machine-readable full texts (6 XML + 1 HTML, 7 distinct PMIDs) · 3 PDFs (not textually scanned) · 6 asset directories | the only primary artefacts held locally |
| Live connectors (PubMed, Scholar Gateway, bioRxiv, Clinical Trials, AdisInsight) | **unauthorized in this session** | ⚠️ **no external search was run.** Every "no evidence exists" below means *no evidence exists on the surfaces named above*, and nothing stronger |

⚠️ **The registry-title caveat, applied throughout.** A `CORPUS-STUB` title is a **bibliographic datum**,
not a measurement. A title can establish that a question was asked; it can never fix a direction. Where a
title is used below it is used only to show that a direction is **contested in the catalogued literature**,
which is a claim about this repository's state of knowledge and not about biology.

---

## 1 · mTOR directionality — re-derived, and the verdict changes

### 1.1 The single WWOX-specific datum, field by field

The map's §2.2 and N-01 rest on one measurement. Re-derived:

| Field | Value |
|---|---|
| **MODEL** | hESC-derived **WWOX-KO cerebral organoids** (CRISPR), Steinberg et al. 2021 · PMID 34268881 / PMC8350905 · GEO **GSE156243** |
| **TISSUE** | 3D human cerebral organoid, **bulk** — not sorted, not single-cell (the authors state single-cell RNA-seq was not performed) |
| **DEVELOPMENTAL_STAGE** | culture **week 15**. The KO organoids carry declared, severe **regionalization and maturation defects** — the comparison is not stage-matched, it is age-matched |
| **N** | **2 WT vs 4 KO.** Started 4 + 4; one WT failed QC, a second WT was excluded for not clustering |
| **READOUT** | bulk RNA-seq differential expression / EV gene lists. 🔴 **No protein. No phospho-S6. No phospho-4E-BP1. No LC3-II/p62. No autophagic flux. No rapamycin arm.** |
| **MTOR_DIRECTION** | **down** — transcript / gene-set level only |
| **EIF4EBP1_DIRECTION** | **down** — transcript |
| **AUTOPHAGY_DIRECTION** | **down** — transcript (`RB1CC1`/FIP200, `MDM2`, `RB1`) |
| **STATISTICAL_THRESHOLD** | fold-change filter + **raw `P < 0.01`** |
| **MULTIPLE_TESTING_STATUS** | 🔴 **not FDR-controlled.** The dossier records that numerous genes in the EV1/EV2 lists carry `padj > 0.05`. **Whether `EIF4EBP1`, `RB1CC1` or any mTOR-set member individually survives FDR is not recorded anywhere in LEGEND** |
| **LIMITATIONS** | see §1.2 — four, and they are not additive caveats, they are four independent reasons the direction does not carry |

### 1.2 Four reasons the direction does not carry

**(a) 🔴 The datum has no verbatim locator anywhere in this repository.**
`deepdive_manifests/PMID34268881.json` carries **12** locators; **none** touches mTOR, EIF4EBP1 or
autophagy. The 64-line dossier `fulltext_dossiers/PMID34268881.md` never names them. The commit candidate
`CC-20260814-34268881-01.md` never names them. The direction exists in LEGEND at exactly one place: a
summary line inside `DL-MECH-034`'s *"Altri assi alterati (DATO)"*. This repository's own export rule —
*"a conclusion reached carefully but without its quote cannot enter"* ([`README.md`](README.md), DisMech
§) — would refuse it. **A datum that could not be exported is currently carrying the file's second-ranked
negative finding.**

**(b) Transcript abundance is not mTORC1 activity — and this repository has already paid for that premise
on the adjacent kinase.** `CLAIM 016`'s load-bearing premise, *"GSK3β abundance reports GSK3β activity"*,
is tagged `PREMISE: DEFAULT_FROM_TEXTBOOK` precisely because in WWOX systems abundance and activity are
dissociable. *"`MTOR` transcript down ⇒ mTORC1 signalling down"* is the same premise applied to a kinase
whose output is set almost entirely post-translationally.

**(c) `EIF4EBP1` ↓, read as biology rather than as gene-set membership, points the other way.**
4E-BP1 is the **inhibitor** of eIF4E and the **substrate** of mTORC1. Less 4E-BP1 means less brake on
cap-dependent translation — which is the same functional output mTORC1 **activation** produces. Reading
`EIF4EBP1` ↓ as evidence of *"the mTOR pathway is down"* requires the premise that a gene's membership in
an mTOR annotation set fixes the sign of its contribution to that pathway's output. It does not.

**(d) The dataset's two directions are discordant under the coupling that would be needed to read them.**
mTORC1 is the canonical **suppressor** of autophagy. *"mTOR down **and** autophagy down"* is internally
coherent only if the autophagy call is driven by something other than mTORC1 — which is entirely possible
(`RB1CC1`/FIP200 is an initiation-complex component whose loss suppresses autophagy mTORC1-independently),
but that is an admission that the mTOR label is not what is producing the autophagy direction. Under the
textbook coupling the negative implicitly uses, **the two directions from the same list contradict each other.**

### 1.3 Counter-directional evidence on the authorized surfaces

**🔴 A correction to the map first.** §2.2 states that `CORPUS-STUB-043` is *"the only other WWOX record
naming mTOR"*. It is not. **Two of the 426 registry records** name mTOR anywhere in the record:

| Record | PMID | Title | Status |
|---|---|---|---|
| `CORPUS-STUB-043` | 36621327 | WWOX **activates autophagy** to alleviate LPS-induced acute lung injury **by regulating mTOR** | `not_processed` |
| `CORPUS-STUB-177` | 31966718 | EBV-LMP1 regulating **AKT/mTOR** signaling pathway **and WWOX** in nasopharyngeal carcinoma (PMC6965410, open access) | `not_processed` |

⚠️ **And the sharper number: across all 426 records, `rapamycin`, `everolimus`, `4E-BP`, `EIF4EBP1`, `LC3`
and `SQSTM1` return _zero_ hits.** Not one catalogued record in this corpus is an mTOR-pharmacology paper,
and not one names a protein-level mTORC1 or autophagy-flux readout.

**And the autophagy axis — the axis the mTOR direction would have to be read through — is catalogued in
two opposite directions:**

| Record | PMID | Direction stated in the title | Context |
|---|---|---|---|
| `CORPUS-STUB-043` | 36621327 | WWOX **activates** autophagy | LPS acute lung injury |
| `CORPUS-STUB-056` | 33300063 | WWOX **inhibits** autophagy | paclitaxel, ovarian carcinoma |
| `CORPUS-STUB-139` | 24008736 | WWOX **suppresses** autophagy | methotrexate, squamous cell carcinoma |

All three `not_processed`; none CNS; none developmental. **None of them fixes a direction, and none is
cited here as if it did.** What they establish is weaker and sufficient: **the sign of WWOX → autophagy is
not stable across the literature this repository has already catalogued.** That is the identical pattern
already canonical for WWOX ↔ ROS (`CLAIM 034`, instantiating `CLAIM 028`), and it removes the textbook
coupling that would let *autophagy ↓* report an mTOR direction at all.

**Local full-text corpus: zero mTOR measurements.** Across the 7 machine-readable full texts (~950 kB,
7 distinct PMIDs), the pattern `mTOR|4E-?BP|EIF4EBP1|rapamycin|everolimus|autophag|LC3|p62|SQSTM1|S6K|rpS6`
returns **three** hits — and **all three sit inside reference lists**, i.e. they are cited article titles,
not measurements:

| File | Match | Where |
|---|---|---|
| PMID 29724996 | `mTOR` | reference: *"Bufalin suppresses hepatocellular carcinoma … via the PI3K/AKT/mTOR pathway"* |
| PMID 32000863 | `autophag` | reference: *"WWOX **suppresses autophagy** for inducing apoptosis in methotrexate-treated human squamous cell carcinoma"* |
| PMID 38499540 | `autophag` | reference: *"Cisplatin-induced autophagy protects breast cancer cells…"* |

⇒ **zero measurements in the corpus.** Reproduce over `files/fulltext/`, which does not contain this file.
⚠️ Note the second row: the Cheng 2020 primary — read in full by this repository — **cites
`CORPUS-STUB-139`**, the counter-directional autophagy record. The contradiction was inside a paper LEGEND
has already read, in its bibliography, unread.

**No TSC logic is imported.** TSC is named once in this section, to say that the reflex it licenses is the
reflex this repository refuses to reason from. Nothing in the verdict below is derived from the fact that
mTOR inhibitors work in TSC.

### 1.4 Verdict

> ## `MTOR_DIRECTIONALITY_VERDICT: INSUFFICIENT`

**Yes — the evidence depends on one weak dataset, and it is weaker than the map states.** One bulk
transcriptome, `n = 2` versus `n = 4`, raw `P < 0.01`, no FDR, no protein, no locator, in a tissue with
declared maturation defects, carrying two directions that contradict each other under the coupling needed
to interpret either.

**What changes.** The map's N-01 is phrased as *"acts in the wrong direction"* and ranks **second** in
`TOP_NEGATIVE_FINDINGS`. That phrasing does not survive. There is no usable directional datum: the single
one is unlocatored, transcript-only, internally discordant, and its 4E-BP1 component inverts when read as
biology. N-01 was doing work it was not entitled to do — it was cited as a *demonstration* that an entire
approved drug class points the wrong way. It is not that. It is a statement that **the axis has never been
measured at the protein level in any WWOX system.**

**What does not change.** mTOR inhibitors do not enter. `INSUFFICIENT` is not a promotion. No positive
WWOX rationale exists at any tier, no WWOX system has ever received an mTOR inhibitor, and the operational
position — do not prioritize — is identical. **Only the reason changes, and the reason is what a reader
carries forward.** The correct sentence is now *"nobody has measured it"*, not *"it points the wrong way"*.

---

## 2 · Lithium — disaggregated

### 2.1 The seven components, separated

Re-derived from the primary artefact held locally: `files/fulltext/PMID32000863_Cheng2020_PMC.xml`
(sha256 `792b5b29…`), plus the image locators in `deepdive_manifests/PMID32000863.json`
(receipt `FTR-20260804-32000863-01`, audited 2026-08-10).

| Component | Status | What was actually measured |
|---|---|---|
| **ANTICONVULSANT_EFFECT** | ✅ **DEMONSTRATED** | LiCl **60 mg/kg i.p., three pre-treatments within 1 h** before PTZ. Caption: *"**d** Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg) suppressed PTZ-induced seizure activity in Wwox−/− mice."* Real, and not in dispute |
| **GENOTYPE_SPECIFIC_INTERACTION** | 🔴 **FAILED ITS OWN TEST** | Figure 7**d** stacks three genotype panels (`+/+`, `+/−`, `−/−`), **each carrying its own significance bracket; the wild-type panel is marked as significantly as the null.** Caption and Results name only `−/−` |
| **WWOX_MECHANISTIC_RESCUE** | ❌ **NOT MEASURED** | no GSK3β readout under lithium, no Tau phosphorylation, no target-engagement measure of any kind in treated animals |
| **WNT_DIRECTIONALITY** | ⚠️ **CONFLICTED — and unmeasured in the treated model** | see §2.3 |
| **DEVELOPMENTAL_RESCUE** | ❌ **NOT MEASURED — the authors say so themselves** | *"Whether lithium treatment can rescue the deficits in neuronal migration and differentiation during development in Wwox−/− mice **remains to be studied**."* (Discussion, closing) |
| **SURVIVAL** | ❌ **NOT MEASURED** | zero survival analysis in the paper (`Kaplan` 0 hits, `lifespan` 0 hits in the PMC XML). A ~1-hour acute pre-treatment cannot address survival |
| **OTHER_ENDPOINTS** | ❌ **NONE** | no behaviour, no myelin, no gliosis, no ECoG, no weight, no glycaemia, no histology under lithium |

⇒ **Lithium was tested on one endpoint, once, acutely, as a pre-treatment.** Six of seven rows are empty.

### 2.2 Does suppression in WT + HET + KO demonstrate anything WWOX-specific?

**No — and the reason is stronger than "untested".**

A drug effect is WWOX-specific only if the **genotype × treatment interaction** is non-null. Figure 7d
shows a main effect of treatment in all three genotypes and **no tested interaction**. But the same figure
contains the comparator that settles it: for **ethosuximide** (Figure 7**b**) the text explicitly declares
`n.s.` in `+/+` and `+/−` and significance in `−/−` — *"ethosuximide pretreatment had no effects on the
behavior changes in Wwox+/+ and Wwox+/− mice"*. For lithium the paper **declares no converse**.

⇒ The assay **can** detect genotype specificity. It detected it for the other drug, in the same figure, in
the same cohort, on the same day. **This is a negative result in an assay of demonstrated sensitivity, not
an absent measurement.** The map records the fact; it does not record this consequence, and the
consequence is what separates *"we don't know"* from *"we looked and it wasn't there"*.

**A general anticonvulsant effect is not counted as WWOX rescue anywhere in this file.**

### 2.3 The Wnt directional conflict, analysed

Three facts, each verified against the artefacts:

1. **In human WWOX-KO cerebral organoids, Wnt is hyperactivated.** Nuclear β-catenin ~1.7×; `WNT1/2B/3/3A/5A/8B`,
   `LEF1`, `AXIN2` up; partially recovered by W-AAV (`DL-MECH-034`). ⚠️ Same dataset, same `n=2/4`, same raw-`P`
   threshold as §1 — **but not the same evidential quality**: the Wnt direction is anchored by a **protein/localization**
   measure (nuclear β-catenin) and by W-AAV recovery, which the mTOR direction has nothing equivalent to.
2. **Lithium activates Wnt** by stabilizing β-catenin. Not in dispute.
3. 🔴 **In the mouse where lithium was tested, Wnt was never measured.** `Wnt` and `catenin` occur 5 and 4
   times in the PMC XML and **every occurrence is a Discussion citation of another system.**

**And the conflict has a second edge the map does not carry.** The primary's own Discussion invokes
lithium's Wnt action as a **potential benefit**, citing Lancaster 2011 — *"rescue **Wnt-dependent
cerebellar midline fusion** and neurogenesis deficits early in development"* — in a mouse whose phenotype
includes **cerebellar vermian lobule V/VI/VII fusion with Purkinje loss** and forebrain malformation
*"ranging from microcephaly to **holoprosencephaly**"*. The cited paradigm is **Wnt too low**, rescued by
**activating** Wnt.

⇒ On the axis measured in human **forebrain** organoids, lithium pushes the wrong way. On the axis the
primary itself names in mouse **cerebellar midline**, lithium would push the right way. **Neither is
measured in any WWOX system with a Wnt readout and a lithium arm in the same experiment.**

**The honest resolution is not *"lithium is contra-indicated by the Wnt mechanism"*. It is:** the Wnt sign
in WWOX loss is established in human **cerebral/forebrain** tissue, is **unmeasured in cerebellum**, and is
**unmeasured in every model in which lithium has been given**. The map's CHAIN D states the
contra-indication without the compartment. **A globally-acting agent on a pathway whose sign may split by
region cannot be scored on one region's sign.**

⚠️ *Calibration note, `INFERENZA`, not a refutation:* the same organoid transcript list also reports
**Shh ↑** (`SHH`, `GLI1`, `PTCH1`, `HHIP`), while the mouse null shows a **holoprosencephaly-range**
forebrain-division defect — classically a Shh-**deficiency** phenotype. Organoid ≠ mouse, transcript ≠
signalling, and HPE has non-Shh causes. Recorded only because it is the *same list* that supplies §1's mTOR
direction, and it is a second place where that list does not straightforwardly explain the in-vivo lesion
it is invoked beside.

### 2.4 Two defects in the chain, and one mutual exclusion

**🔴 Defect 1 — panel misattribution, propagated into a canonical claim.**
The map (CHAIN C and R-04) and `CLAIM 016`'s evidence boundary both cite **Fig. 7b** for the lithium panel.
The primary's caption reads *"**d** Pretreatment of a GSK3β inhibitor LiCl…"* and the Results text says
*"(Fig. 7 **d**)"*. **Lithium is 7d. 7b is ethosuximide.** The deepdive manifest has it right; the claim
and the map inherited the wrong panel from each other. Consequence for the conclusion: none. Consequence
for reproducibility: total — a reader sent to 7b to check the strongest negative in the lithium file lands
on a different drug.

**🔴 Defect 2 — *"GSK3β abundance elevated"* has no source in either cited source.**
R-04's `WWOX_DIRECT_EVIDENCE` field says *"GSK3β **abundance** elevated in Wwox-null cortex/hippocampus/cerebellum
(2 sources)"*, and `CLAIM 016`'s Summary says *"GSK3β is **elevated** in cortex, hippocampus and cerebellum"*.

- **Source 1 (Cheng 2020).** Figure 7c densitometry, read at 3× from the native 1946×1627 image and recorded
  in the manifest: **total GSK3β is flat across genotypes in every region** — cerebellum 2.2 / 2.4 / 2.4,
  hippocampus 2.3 / 2.4 / 2.6, cortex 2.2 / 2.4 / 2.6 — while **pSer9 falls** (2.7 / 3.1 / 1.3; 3.6 / 3.5 / 2.0;
  3.9 / 3.8 / 2.5). The paper's own Results say *"increased **activation** … as evidenced by
  **dephosphorylation** of GSK3β at Ser9"*. **Activation. Never abundance.**
- **Source 2 (Wang 2012, `CLAIM 035`).** Reports abundance and pS9 **unchanged** while kinase output falls.

⇒ **Neither source reports elevated GSK3β abundance.** `CLAIM 016`'s boundary explicitly preserves it
(*"Cosa NON cambia: il dato di abbondanza"*) — preserving something that is in neither source. And the map's
`PREMISE_TAG` on R-04 (*"abundance reports activity"*) is a premise about a datum that does not exist; the
real datum is a **phospho-site** measurement, which needs a different critique — supplied next.

**🔴 The mutual exclusion — `CLAIM 016` and `CLAIM 035` do not corroborate each other on this axis.**
`CLAIM 035` establishes that WWOX's inhibition of GSK3β is **S9-independent**, and derives from it a
measurement warning the map repeats: *de-repression caused by WWOX loss would be **invisible to a
phospho-S9 western***, and any WWOX study using pS9 as an activity readout *"produrrà un falso negativo"*.
**But the only in-vivo evidence that GSK3β is de-repressed in WWOX loss is a phospho-S9 western.**

The two cannot both describe the same brake:
- **(a)** the in-vivo pS9 fall is driven by something other than loss of the WWOX docking-site brake ⇒ Cheng's
  western is **not** evidence that the `CLAIM 035` mechanism operates in vivo, and CHAIN C has **no in-vivo anchor**; or
- **(b)** it *is* WWOX-dependent ⇒ `CLAIM 035`'s S9-independence needs a boundary it does not have.

The map fuses both claims into one chain (M4) and takes an anchor from each. **On this axis they exclude
each other.**

**And there is a concrete competing explanation for (a), already canonical here.** Ser9 is the AKT site;
AKT tone follows insulin and glucose. A systemic constitutive Wwox-null in the P14–P20 window is
hypoglycaemic, acidotic and uraemic (`CLAIM 036`: glucose **143.5 vs 250.6 mg/dL**, `p = 0.000131`). Cheng's
GSK3β westerns are taken at **P20**, in a systemic constitutive null. Hypoglycaemia → less insulin → less
AKT → **less pSer9** → reads as GSK3β "activation".
`PREMISE: INFERENZA`, and the transfer is stated: `CLAIM 036` is measured in a **different** null strain
(EIIA-Cre, Ludes-Meyers) than Cheng's; what transfers is the **confounder class**, not the numbers. It does
not refute the finding. It means the design cannot separate a WWOX-dependent brake from a systemic
metabolic one — **the identical criticism `CLAIM 036` already applies to the PV/glia markers, applied here
for the first time to the GSK3β datum that carries the entire M4 chain.**

### 2.5 Verdicts

> ### `LITHIUM_WWOX_SPECIFICITY: NOT DEMONSTRATED`
> — and specifically: **a negative result in an assay of demonstrated sensitivity**, not an absent test.
> The same figure detected genotype specificity for ethosuximide.

> ### `LITHIUM_DIRECTIONALITY: CONFLICTED ACROSS TWO AXES, AND UNMEASURED IN ITS OWN MODEL`
> **M4 (GSK3β):** plausible in direction, but its only in-vivo anchor is a pSer9 western that the
> S9-independence of the WWOX brake says should not have moved, with a canonical systemic-metabolic
> alternative explanation available and untested.
> **M5 (Wnt):** lithium activates a pathway measured hyperactive in human forebrain organoid tissue and
> **never measured in the treated mouse**, while the primary itself proposes the opposite sign for
> cerebellar midline.
> **Isoform (`DL-MECH-067`/`068`):** an ATP-competitive or global inhibitor cannot spare **GSK3β2** — enriched
> in growth cones, maximal in the developing brain, required for axon growth. A developmental-window risk
> that `TX-005`'s SAFETY score still does not carry.

> ### `LITHIUM_REPURPOSING_STATUS: DEPRIORITIZE`
> Verdict **unchanged**; reasons strengthened; scope narrowed. It remains a real anticonvulsant with real
> paediatric use. It is **not** a WWOX-mechanism drug, and it must not be scored on M4 while M4's in-vivo
> anchor is contested and M5's sign is unmeasured in lithium's own model.

> ### `REVIVAL_TRIGGER` (drug)
> *Reopen if a seizure-susceptibility experiment reports a **tested, pre-specified genotype × treatment
> interaction** for lithium in `Wwox−/−` versus `Wwox+/+` — the comparison ethosuximide already has in Fig. 7b
> — **or** if any WWOX system shows a lithium-attributable change in a **WWOX-dependent molecular readout**
> (Tau pS396/S404, nuclear β-catenin, or GSK3β kinase output by a non-pS9 assay) with a wild-type arm run in
> parallel.*

> ### `REVIVAL_TRIGGER` (the M4 mechanism, which is a separate object from the drug)
> *Reopen the in-vivo anchor if a **phospho-S9-independent** GSK3β activity assay in WWOX-deficient neural
> tissue reports de-repression — or if the pSer9 fall is reproduced in a **normoglycaemic or conditional**
> WWOX-null, separating it from the systemic metabolic collapse of `CLAIM 036`.*

---

## 3 · Decomposing PV / GABA / mTOR / circuit into eight axes

**These are not one therapeutic programme, and the map's own `PV_GABA_MTOR_PROGRAM_STATUS` block still
reports them under one heading with four rows.** Eight axes, each with its own evidence state. Three moved
in this pass.

### 3.1 `PV_INTERNEURON`

| Field | Value |
|---|---|
| `WWOX_DEPENDENCE_MEASURED` | **Partially.** Marker counts in **one** systemic constitutive KO at two weeks: PV⁺ ↓ (DG, CA1, whole hippocampus **−44%**), NPY⁺ ↓ **DG only**, GAD65/67 protein ↓ (`CLAIM 005`). Confounded by construction: that animal is hypoglycaemic/acidotic/uraemic in that window (`CLAIM 036`, confounder class transfers, numbers do not) |
| `DIRECTION_MEASURED` | Markers **down** in mouse; GABAergic markers **up** in human organoids (GAD67 ↑, `GAD1`/`GAD2` ↑). **Opposite, and unresolved** |
| `DIRECT_WWOX_EVIDENCE` | Yes — **marker level only.** `MARKER_TO_FUNCTION_GATE` unmet: no pan-GABA lineage count, no birthdating, no fate mapping, no apoptosis assay |
| `TRANSFERRED_EVIDENCE` | PV-deficit → hyperexcitability, from the broader DEE literature (T3/T4) |
| `ACTIONABLE_NODE` | 🔴 **None identified.** "PV interneurons" is a cell class, not a node a molecule engages |
| `INTERVENTION_EXISTS` | No |
| `WWOX_SPECIFIC_RESCUE` | None attempted |
| `MAIN_UNCERTAINTY` | Cell loss vs delayed maturation vs downregulated marker vs secondary metabolic injury — **four hypotheses, none discriminated** |
| `DECISIVE_EXPERIMENT` | Pan-GABAergic lineage count + birthdating/fate-mapping + apoptosis assay in a **neuron-conditional** (not systemic) null at matched stage. The floxed allele has existed since 2009 |

🆕 **New in this pass.** In the neuron-specific model, the interneuron exemplars *"look alike across
genotypes"* (Figure 6A) while inhibition **onto** L2/3 pyramidal neurons is halved. ⇒ the measured deficit
is in inhibitory **output**, not obviously in interneuron intrinsic excitability. That widens, rather than
narrows, the gap between *"fewer PV markers"* and *"less inhibition"*.

### 3.2 `GABA_RECEPTOR`

| Field | Value |
|---|---|
| `WWOX_DEPENDENCE_MEASURED` | Abundance only — `GABRB2`, `GABRB3` ↓ in organoids; GAD65/67 protein ↓ in mouse |
| `DIRECTION_MEASURED` | Receptor-subunit transcripts down; ligand-synthesis markers **up** in organoid, **down** in mouse. Species-discordant |
| `DIRECT_WWOX_EVIDENCE` | Yes, abundance only |
| `TRANSFERRED_EVIDENCE` | GABA-A pharmacology from general epileptology (T4) |
| `ACTIONABLE_NODE` | GABA-A receptor |
| `INTERVENTION_EXISTS` | Yes — many, all approved |
| `WWOX_SPECIFIC_RESCUE` | 🔴 **None — and the mechanism was falsified as a clinical predictor.** The depolarizing-GABA rationale predicts GABAergic drugs underperform; **vigabatrin resolved the spasms** in a published WWOX-null child (`CLAIM 001`, `CLAIM 031`; failure mode `FM-018`). Against that: VABAM documented in WWOX-DEE (n=2). **Neither closes the question** |
| `MAIN_UNCERTAINTY` | Whether a GABA-A agonist inhibits or excites this tissue — which is §3.3, and is unmeasured |
| `DECISIVE_EXPERIMENT` | §3.3's. A receptor measurement cannot answer it |

### 3.3 `CHLORIDE_HOMEOSTASIS`

| Field | Value |
|---|---|
| `WWOX_DEPENDENCE_MEASURED` | 🔴 **NO. Zero measurements.** Across every `*.md` under `disease-models/wwox/` **excluding this file and the map it stress-tests** (both of which discuss the absence and would otherwise match their own negative), and across the 7 machine-readable full texts, `NKCC1\|KCC2\|SLC12A2\|SLC12A5\|E_GABA\|gramicidin` returns **14 lines across 9 files, every one of them a request for the measurement or a statement of its absence** — **0 measured values**, against 426 registry records |
| `DIRECTION_MEASURED` | **None.** *"Depolarizing GABA"* is `IPOTESI` — the authors' reading of a marker pattern against the developmental literature, and the dossier says so explicitly |
| `DIRECT_WWOX_EVIDENCE` | None |
| `TRANSFERRED_EVIDENCE` | Neonatal-seizure and other-DEE bumetanide trials, **mixed to negative** (T3/T4) |
| `ACTIONABLE_NODE` | NKCC1 |
| `INTERVENTION_EXISTS` | Bumetanide — approved as a diuretic; **poor CNS penetration is a known, unsolved limitation of this route** |
| `WWOX_SPECIFIC_RESCUE` | None |
| `MAIN_UNCERTAINTY` | 🔴 **The sign of the effect.** Not the effect size — the direction |
| `DECISIVE_EXPERIMENT` | Gramicidin perforated-patch `E_GABA` in WWOX-KO vs **isogenic parental** neurons/organoids, with NKCC1/KCC2 quantification and the GABA response itself |

> 🔴 **Explicit compliance with the assignment's constraint.** GABA polarity has never been measured in any
> WWOX system. **Bumetanide and every chloride-directed intervention stay at `T6` / `INSUFFICIENT_EVIDENCE`
> and are not promoted.** Nothing in this second pass moved them, and nothing in this second pass may be
> read as moving them.

### 3.4 `NMDAR` — 🆕 **upgraded**

| Field | Value |
|---|---|
| `WWOX_DEPENDENCE_MEASURED` | ✅ **Yes — pharmacologically, inside the WWOX-deficient system.** **d-APV** applied to `Wwox` S-KO neocortical slices takes normalized burst frequency from 1.0 to **zero** (Figure 3D-d1, image-read at 6× from native pixels, `deepdive_manifests/PMID34634460.json`, receipt `FTR-20260810-34634460-02`) |
| `DIRECTION_MEASURED` | NMDAR blockade **abolishes** the pathological burst at the stage tested. ⚠️ On washout, frequency returns to **~1.85× baseline** — an overshoot, recorded, unexplained, and directly relevant to any chronic-blockade proposal |
| `DIRECT_WWOX_EVIDENCE` | **T1 conjunction for the tool compound** on the bursting endpoint, in an acute ex-vivo slice |
| `TRANSFERRED_EVIDENCE` | GRIN2A in the burst-suppression cohort (`DL-MECH-002`); memantine's approved use (T3/T5) |
| `ACTIONABLE_NODE` | NMDAR |
| `INTERVENTION_EXISTS` | Memantine — approved, CNS-penetrant, reversible. d-APV / MK-801 as tools |
| `WWOX_SPECIFIC_RESCUE` | ✅ **for the tool compound.** ❌ **for memantine**, which has never been given to a WWOX system. **The gap is now exactly one compound wide, not one experiment wide** |
| `MAIN_UNCERTAINTY` | (i) recordings are **P13–P17** in animals that die at 3–4 weeks; the authors themselves write that *"the chosen age group may mimic a **late-stage** disorder of WWOX"*; (ii) acute slice ≠ chronic in vivo; (iii) the washout overshoot; (iv) chronic NMDAR blockade in a developing brain removes a signal required for activity-dependent maturation — **the very process WWOX loss already impairs** |
| `DECISIVE_EXPERIMENT` | **Memantine** (not d-APV) dose–response on MEA burst frequency/amplitude and phase–amplitude coupling in WOREE patient-iPSC organoids **with parental and W-AAV-rescue lines as internal comparators**, plus a **chronic** arm reading a maturation endpoint, not only a burst endpoint |

> 🔴 **This discharges the map's `E-1`.** The map lists as its *"highest-value, lowest-cost open item"* a
> re-read of PMID 34634460 to determine whether the NMDAR/gap-junction dependence was established
> **pharmacologically**. **The re-read has already been performed** — receipt `FTR-20260810-34634460-02`,
> 21 verbatim locators, several image-anchored — **and it was.** The map was written without consulting it.
> **Chain B is T1 on the tool compound, not T2.** The cost of that experiment is now zero and its result is
> already in the repository.

### 3.5 `GAP_JUNCTION` — 🆕 **downgraded**

| Field | Value |
|---|---|
| `WWOX_DEPENDENCE_MEASURED` | Apparently — carbenoxolone (CBX) 100 µM reduces burst frequency by **87%** in the S-KO slice |
| `DIRECTION_MEASURED` | Down — 🔴 **but not attributable**, on two grounds from the primary itself: **(i)** the effect **does not wash out** (*"This did not return to normal levels after washout"*; CBX frequency ~0.25 at washout against 1.0 baseline, duration still carrying a significance marker at washout) — an effect persisting through washout is not cleanly pharmacological at that concentration; **(ii)** the Discussion lists two off-target actions for CBX: **NMDA receptor block** and pannexin block |
| `DIRECT_WWOX_EVIDENCE` | Yes for the **compound**. 🔴 **No for the target.** Given that d-APV alone abolishes the burst, the CBX result is fully explicable as §3.4 again |
| `TRANSFERRED_EVIDENCE` | Gap-junction blockade in other epilepsy models (T4) |
| `ACTIONABLE_NODE` | Connexin gap junctions — **not established as separable from NMDAR in this dataset** |
| `INTERVENTION_EXISTS` | No CNS-appropriate selective connexin blocker. CBX is a tool, not a candidate |
| `WWOX_SPECIFIC_RESCUE` | Not attributable |
| `MAIN_UNCERTAINTY` | Whether **any** of the CBX effect is gap-junctional |
| `DECISIVE_EXPERIMENT` | **Occlusion.** A selective connexin blocker (or Cx36/Cx43 genetic manipulation) in the same preparation with a **sub-maximal d-APV** arm co-applied — if the effects occlude, the gap-junction node collapses into the NMDAR node. See `E-D2` |

🆕 **And a new negative belongs to this axis: the pannexin blocker went the wrong way.**
**BB-FCF** raised normalized burst frequency to **~2.55** during treatment and **~2.6** at washout, against
a baseline of 1.0, with **no significance test reported** — while both the Results and the Discussion
describe it as *"minimal effect on the network excitability in the Wwox S-KO model"*. **A 2.5-fold point
estimate with wide error and no test is not an absence of effect, and its direction is the opposite of the
one the sentence implies.** A reader of the prose alone would not know there was a direction to worry about.
⇒ recorded below as **N-16**.

### 3.6 `MTOR`

| Field | Value |
|---|---|
| `WWOX_DEPENDENCE_MEASURED` | Transcript-level only, one dataset, **no locator** — see §1 |
| `DIRECTION_MEASURED` | 🔴 **Not established** (`INSUFFICIENT`) |
| `DIRECT_WWOX_EVIDENCE` | One bulk transcriptome, `n=2/4`, raw `P<0.01`, internally discordant |
| `TRANSFERRED_EVIDENCE` | ⚠️ **Deliberately none.** TSC is not imported |
| `ACTIONABLE_NODE` | mTORC1 |
| `INTERVENTION_EXISTS` | Yes — rapamycin, everolimus, approved (in other indications) |
| `WWOX_SPECIFIC_RESCUE` | **None attempted anywhere.** No WWOX system has ever received an mTOR inhibitor |
| `MAIN_UNCERTAINTY` | Whether mTORC1 **activity** moves at all in a WWOX-deficient neuron |
| `DECISIVE_EXPERIMENT` | `E-D3` — one blot answers the whole row |

### 3.7 `SEIZURE_NETWORK_CONTROL`

| Field | Value |
|---|---|
| `WWOX_DEPENDENCE_MEASURED` | ✅ **Yes, and it is the best-measured axis.** Spontaneous neocortical bursting: **WT 0/11 slices · HET 4/23 (17%) · KO 36/42 (86%)**. Depolarized RMP (−79.25 / −75.51 / −73.62 mV), graded sag (1.18 / 2.04 / 2.57 mV); the authors attribute hyperexcitability to the **resting potential**, not to firing gain (*"not due to action-potential dependent frequency changes"*) |
| `DIRECTION_MEASURED` | Hyperexcitable. 🔴 **Corrected here: the E/I shift is carried by loss of inhibition, not by gained excitation.** sEPSC amplitude **23.3 ± 12.0 vs 24.7 ± 13.6 pA** (a 1.4 pA separation inside a 12-pA spread, ~6%; the excitatory *frequency* distributions are superimposed) against sIPSC amplitude **57.3 ± 31.0 vs 27.5 ± 19.4 pA** (−52%). The paper's Results say the shift operates *"primarily through an impairment in the amplitude of the inhibitory currents"*; its **abstract lists the excitatory finding first** |
| `DIRECT_WWOX_EVIDENCE` | Yes, neuron-specific deletion |
| `TRANSFERRED_EVIDENCE` | The entire symptomatic ASM literature (T3/T4) |
| `ACTIONABLE_NODE` | The excitability state itself |
| `INTERVENTION_EXISTS` | Yes — §3.4, plus every symptomatic ASM |
| `WWOX_SPECIFIC_RESCUE` | ✅ AAV9-hSynI-WWOX on SWD/ECoG (Fig 7E: `****` WT-vs-KO, `****` KO-vs-HD, `ns` WT-vs-HD, n=5/group); W-AAV normalizing organoid firing (`P=0.77` vs parental) |
| `MAIN_UNCERTAINTY` | **N-15.** This axis is the symptom, and correcting it has never been shown to move the developmental axis |
| `DECISIVE_EXPERIMENT` | `E-D1` |

🔴 **The map's CHAIN B inherits the abstract's ordering** — it opens *"↑excitatory drive, ↓spontaneous
inhibition"* — and so does `CLAIM 021`'s Summary. That ordering is not what the panels say. Two further
qualifications travel with this axis: the KS p-values (as extreme as `1.8e-100`) are run over **pooled
synaptic events**, not cells or animals, and must never be quoted as animal-level evidence; and
heterozygotes are **pooled into the control group** for the entire spontaneous-current analysis while
Table 1 marks them different from WT on four intrinsic properties — a bias whose direction is
**conservative** (it understates the effect), which is why it is a qualification and not a refutation.

🆕 **The heterozygote finding, and it re-scores a threshold argument elsewhere.**
The Discussion characterises heterozygote bursting as *"manifested **similarly**"* to the knockout's.
**4/23 against 36/42 is a sixth of the incidence.** And Table 1 marks the heterozygote significantly
different from wild type on **four** intrinsic properties (AP amplitude, input resistance, RMP, sag), with
input resistance **saturating at one allele** (102.88 / 143.26 / 143.03) while RMP and sag grade
monotonically. Independently — different model, different laboratory — Cheng's heterozygotes have a
**Tc-MEP latency statistically indistinguishable from the null** while amplitude is normal.

⇒ **`CLAIM 032`'s *"haploinsufficiency is not deleterious"* is a statement about lifespan, gross morphology
and the clinical status of carriers. At the level of network and conduction physiology, the heterozygote is
measurably abnormal in two independent models.** `CLAIM 032` already declares the limit — *"the threshold is
known for survival and morphology, not for cognition or epilepsy"* — but it declares it as an **absence of
evidence**. It is now filled in with **positive counter-observations on exactly the network endpoint**.
This is direct downgrade pressure on the map's `H-3` and on R-01's threshold argument; developed in §5.

### 3.8 `DEVELOPMENTAL_RESCUE`

| Field | Value |
|---|---|
| `WWOX_DEPENDENCE_MEASURED` | The **lesion** is measured: cortical thinning already at **E16.5** (~480 vs ~370 µm), impaired migration and layering, a delayed DCX→NeuN transition (DCX still high at P14/P20), progressive dyslamination in organoids |
| `DIRECTION_MEASURED` | n/a — this axis has no sign, it has a trajectory |
| `DIRECT_WWOX_EVIDENCE` | 🔴 **The decisive negative of the whole portfolio. No intervention in the WWOX literature carries a cognitive or developmental-trajectory endpoint.** AAV9's behavioural battery is locomotor/open-field/motor. Lithium's is one seizure score. The organoid rescues are cellular and electrophysiological |
| `TRANSFERRED_EVIDENCE` | Window logic from other genetic DEEs (T3) |
| `ACTIONABLE_NODE` | Neuronal WWOX protein, before or during the window |
| `INTERVENTION_EXISTS` | R-01 and the allele-level chains |
| `WWOX_SPECIFIC_RESCUE` | **Not on this endpoint. Anywhere.** |
| `MAIN_UNCERTAINTY` | Whether **any** post-onset intervention can move it |
| `DECISIVE_EXPERIMENT` | `E-D1` |

### 3.9 Revised programme status

> ### `PV_GABA_CIRCUIT_REVISED_STATUS`
> **The programme does not exist as a programme.** Eight axes, eight different evidence states:
>
> | Axis | Movement in this pass | State |
> |---|---|---|
> | `NMDAR` | 🆕 **UPGRADED** — pharmacological dependence established **inside** the WWOX system; map `E-1` discharged | **T1 for the tool compound**, T5 for memantine |
> | `GAP_JUNCTION` | 🆕 **DOWNGRADED** — not attributable; CBX blocks NMDAR, and its effect does not wash out | **not an independent node pending occlusion** |
> | *(pannexin)* | 🆕 **NEW NEGATIVE (N-16)** — the only WWOX measurement is **directionally adverse** | `DEPRIORITIZE` |
> | `MTOR` | 🆕 **RE-CHARACTERIZED** — from *"wrong direction"* to *"never measured at protein level"* | `INSUFFICIENT` (§1) |
> | `SEIZURE_NETWORK_CONTROL` | **CORRECTED** — the E/I shift is loss of inhibition, not gained excitation; the heterozygote is not "similar" | best-measured axis |
> | `CHLORIDE_HOMEOSTASIS` | unchanged | **T6, unrankable** — bumetanide not promoted |
> | `PV_INTERNEURON` | unchanged; the interneuron-intrinsic/output distinction sharpened | mechanism admitted, target not |
> | `GABA_RECEPTOR` | unchanged | mechanism survives; as a clinical predictor it was falsified |
> | `DEVELOPMENTAL_RESCUE` | — | **empty for every intervention in the portfolio** |
>
> **The circuit arm survives and is now stronger than the map scored it — but it has relocated entirely to
> NMDAR, and the gap-junction half of the node it used to share has come apart.**

---

## 4 · Symptom control versus disease modification — the endpoint matrix

**Legend.** ● supported cell · ○ measured, null / negative / mechanism-only · ✗ **measured and unfavourable**
· — **not measured**.

| Intervention | SEIZURE_CONTROL | DEVELOPMENTAL_TRAJECTORY | COGNITION | MOTOR_FUNCTION | NEURODEGENERATION | SURVIVAL | CELLULAR_MECHANISM | BIOMARKER_ONLY |
|---|---|---|---|---|---|---|---|---|
| **R-01** AAV9-hSynI-WWOX | ● **C1** | — | — | ● **C2** | ● **C3** | ● **C4** | ● **C5** | — |
| **R-02** NMDAR (tool) / memantine | ● **C6** *(tool only)* | — | — | — | — | — | ● C6 | — |
| **R-04** Lithium | ● **C7** *(non-specific)* | — *(authors: "remains to be studied")* | — | — | — | — | — | — |
| **R-05** Ketogenic diet | ● **C8** *(clinical, transferred)* | — | — | — | — | — | ○ **C9** | ✗ **C10** |
| **R-03** Wnt / tankyrase | — | — | — | — | — | — | ○ **C11** | — |
| **R-06** Anti-neuroinflammatory | — | — | — | — | ○ **C12** | — | ○ C12 | — |
| **R-07** Bumetanide | — | — | — | — | — | — | — | — |
| **R-08** Base / prime editing | — | — | — | — | — | — | — | — |
| **R-09** Proteostasis (SDR missense) | — | — | — | — | — | — | ○ **C13** | — |
| **Symptomatic ASM / window protection** | ● **C14** | ✗ **C15** | ✗ C15 | — | — | ✗ **C16** | — | — |

### Supported-cell records

| # | Cell | MODEL | EVIDENCE_LEVEL | WWOX_SPECIFIC | DIRECT / TRANSFERRED | LIMITATION |
|---|---|---|---|---|---|---|
| **C1** | R-01 · seizure | `Wwox`-null mouse, ICV P0–P5, HD 2.63 × 10¹¹ vg | **T1** | **YES** | DIRECT | SWD (Fig 7E) is solid. 🔴 The **second** epilepsy endpoint in the same figure — average spikes/day (7C) — prints **`p = 0.2000`** on the panel face for WT-vs-KO while the text calls it *"a significant elevation"*. n=5/group |
| **C2** | R-01 · motor | same | **T1** | **YES** | DIRECT | Dose-graded (S4A: WT ~0, KO ~3.6, LD ~1.8, HD ~0.3; WT-vs-HD `ns`, LD-vs-HD `***`). 🔴 But Fig 4D/4E carry asterisks (`*p<0.05`) for **velocity and total distance against WT** while the text states *"no significant differences between groups"*. And **LD animals do not survive to P90**, so all P90 behaviour is HD-only and survivor-selected |
| **C3** | R-01 · neurodegeneration/gliosis | same | **T1** | **YES** | DIRECT | Gliosis quantified with an untreated-KO baseline only in S8I (GFAP⁺ WT ~5 / KO ~44 / treated-at-P5 ~5). 🔴 S7H shows **LD significantly worse than WT** (`**`) while HD is `ns`. 🔴 **Myelination is not quantified in any treated arm of this study** — Fig 6F, S7I and S8G are representative images with no axis, no bar, no significance marker, and the only MBP quantification (6E) has **no treated arm** — yet the text claims *"near-complete rescue across affected regions"* |
| **C4** | R-01 · survival | same | **T1** | **YES** | DIRECT | HD plateaus ~75–80% to day 300; LD moves death from ~20 to ~90 d then reaches zero; 4 × 10¹⁰ and 8 × 10¹⁰ rescue nothing. 🔴 **A threshold with no measured expression correlate** — vector genomes and mRNA are `ns` between the two doses in **7 of 8** region comparisons (exception: hippocampal DNA). The paper's explanation is a **post-hoc survivor-vs-non-survivor** comparison; S5A–D label one HD and three LD animals *"Dead"* |
| **C5** | R-01 · cellular mechanism | same + PMID 34747138 | **T1** | **YES** | DIRECT | Transduction rises **~40% → 55–60%** of neurons; oligodendrocytes **never transduced** yet myelin improves; hypoglycaemia corrected by CNS-only restoration. 🔴 Expression is **supraphysiological and regionally uneven** — §5 |
| **C6** | R-02 · network / seizure | `Wwox` S-KO neocortical slice, P13–P17 | **T1 (tool) / T5 (memantine)** | **YES** (tool) | DIRECT | **d-APV abolishes bursting.** Acute ex-vivo; the authors call the stage *"a late-stage disorder"*; washout overshoots to ~1.85× baseline; **memantine itself has never been given to a WWOX system** |
| **C7** | R-04 · seizure | `Wwox`-null mouse, PTZ, acute pre-treatment | **T5** | 🔴 **NO** | DIRECT (drug) | Suppression in **all three genotypes including wild type**; ethosuximide in the same figure **is** genotype-specific. An anticonvulsant in an animal that has seizures |
| **C8** | R-05 · seizure | human WOREE, observational | **T3/T4** | Partially (clinical population) | DIRECT (clinical) / TRANSFERRED (rationale) | Seizure improvement in **3/5** WOREE patients in one report; against that, **1/3** continued the diet in another, and KD is listed among the *ineffective* interventions in a severe WOREE case |
| **C9** | R-05 · cellular mechanism | `Wwox`-KO mouse + human organoid | **T2** | **YES** | DIRECT | PDK1/GLUT1/HK2/PKM2 measured up; OXPHOS↓/glycolysis↑ **transcriptome, not flux**. No Seahorse, no fluxomics, in any WWOX system |
| **C10** | R-05 · biomarker | human | **T1 (negative)** | **YES** | DIRECT | ✗ **The biomarker does not report.** Four independent human sources show normal metabolism; the single MRS outlier reports cerebral lactate *"extremely low"* — the **opposite** of the Warburg prediction — in a patient with a confounding `HSPG2` variant |
| **C11** | R-03 · cellular mechanism | human WWOX-KO cerebral organoid | **T2** | **YES** | DIRECT | Nuclear β-catenin ~1.7×, WNT/LEF1/AXIN2 up, **partially recovered by W-AAV**. 🔴 Forebrain only; **cerebellar sign unmeasured** (§2.3). No intervention arm in any WWOX system |
| **C12** | R-06 · gliosis / mechanism | `Wwox`-null and `Wwox^P47T` mouse | **T2** | **YES** | DIRECT | ↑IBA1/GFAP **area fraction** (not glial cell number); only `Il6`, **not** `Tnf-a`, significant at n=4/group. 🔴 **The target is downstream of the target** — neuron-restricted WWOX rescue reduces gliosis by itself |
| **C13** | R-09 · cellular mechanism | patient fibroblasts (SDR missense) | **T1 endpoint / T6 mechanism** | **YES** | DIRECT | The **endpoint** is measured (normal transcript, protein not detected); the **mechanism** is not — translation vs solubility vs turnover undiscriminated |
| **C14** | ASM · seizure | human WWOX-DEE cohorts and cases | **T1** | Population-specific | DIRECT | Real and fully indicated for quality of life, status epilepticus, SUDEP, sleep, manageability |
| **C15** | ASM · development & cognition | human WWOX-null children | **T1 (negative)** | **YES** | DIRECT | ✗ *"The developmental outcome was unfavourable with profound impairment **despite improvement of epileptic activity**"*; cognitive impairment **precedes** the epileptic encephalopathy and *"did not improve with achievement of better control"*. Vigabatrin **resolved** the spasms; at two years the child was profoundly delayed. Limits: **N=2, observational, uncontrolled** |
| **C16** | ASM · survival | human cohort | **T1 (counter-signal)** | **YES** | DIRECT | ✗ In one cohort the only **non**-drug-resistant patient died at 8 years — drug responsiveness did not protect survival |

### N-15 applied as a falsification rule

**Rule:** `SEIZURE_CONTROL` must not be counted as `DEVELOPMENTAL_TRAJECTORY` without direct evidence.
Applied mechanically to the matrix above, it yields two observations:

1. **Every intervention with a filled `SEIZURE_CONTROL` cell has an empty `DEVELOPMENTAL_TRAJECTORY` cell
   and an empty `COGNITION` cell. Without exception — including R-01.**
2. **The only cells anywhere in those two columns that carry data are the human observational ones, and
   their value is negative** (C15).

> ### `SYMPTOM_VS_DISEASE_MODIFICATION_MATRIX_COMPLETE: NO`
> The matrix is complete as a **map of what has been measured**. It is not complete as a **comparison of
> interventions**, because the column that would rank them is empty for every candidate in the portfolio.
> **That emptiness is the finding, not a gap in this pass's work** — and it applies with full force to the
> one intervention the map placed above all others.

---

## 5 · AAV9-hSynI-WWOX under a stronger standard

Because R-01 was the **only** entry in `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION`, it is held here to a
standard the weaker candidates are not. Sources: PMID 42422765 (dose study, 29 verbatim locators, receipt
`FTR-20260814-42422765-06`, complete read) and PMID 34747138 (`FTR-20260810-34747138-01`, 20 locators).

| Field | Assessment |
|---|---|
| **TARGET_CELL_TYPE** | hSynI promoter, neurons. Transduction **~40% → 55–60%** of neurons. 🔴 Oligodendrocytes **never transduced** — which is what makes the myelin recovery non-cell-autonomous and is the strongest part of the mechanism. ⚠️ The MBP-driven comparator vector produced **essentially no detectable WWOX**, so the oligodendrocyte-autonomous question is **unanswered by that experiment, not answered negatively** |
| **TIMING** | P0–P5. All of P1–P5 give survival, **but** the 300-day panel shows only **P1 and P5**; P2/P3/P4 exist solely in the 40-day panel, and **P3 is an n=3 arm that lost animals** (~67% at ~24 d). Post-natal dosing beyond P5 is **explicitly declared future work** |
| **DOSAGE** | Four survival doses across two figures: **4 × 10¹⁰ → none survive · 8 × 10¹⁰ → none survive · 1.23 × 10¹¹ (LD) → death by ~90 d · 2.63 × 10¹¹ (HD) → ~75–80% plateau to day 300.** The threshold is therefore **not** an artefact of comparing two doses. 🔴 **But it has no measured expression correlate** (C4) |
| **DISTRIBUTION** | 🔴 **The cerebellum is under-transduced at every dose and every timepoint.** At P30, Figure 5L cerebellum sits **below** wild type; at P300, S6D prints cerebellum **0** against cortex 4.6, hippocampus 4.7, midbrain 3.1, and S5J prints cortex **8.2×**, hippocampus **10.7×**, midbrain **5.6×**, cerebellum **1.4×** wild type. Meanwhile the `Wwox`-null shows vermian lobule V/VI/VII foliation defects with Purkinje loss, and **ataxic gait is the single most penetrant phenotype of the rat model — 95% versus 0%** (`CLAIM 039`), more penetrant than seizures. ⇒ **The vector systematically under-treats the region carrying the most penetrant motor phenotype, and no cerebellum-specific endpoint is reported** |
| **RESCUE_ENDPOINTS** | See C1–C5. Survival, SWD, motor and gliosis are supported; **myelination is claimed but unquantified in this study's treated arms**; development and cognition are **absent** |
| **SURVIVAL** | ✅ Strongest cell in the portfolio — with the threshold/expression mismatch stated |
| **SEIZURES** | ✅ On SWD. ⚠️ One of the two epileptiform endpoints in the same figure is text-vs-panel contradicted (`p = 0.2000`) |
| **DEVELOPMENT** | 🔴 **NOT MEASURED.** No cognitive assay, no learning task, no developmental-trajectory endpoint exists in either paper. The behavioural battery is locomotor, open-field and motor |
| **POTENTIAL_OVEREXPRESSION_RISK** | 🔴 **Real, quantified and durable.** The WPRE construct produces **11.6 / 11.9 / 4 / 2.4×** WT at 2 × 10¹⁰ and **25.6 / 22.3 / 11.6 / 6.2×** at 4 × 10¹⁰ (cortex/hippocampus/midbrain/cerebellum); at P300 the HD survivors sit at **8.2 / 10.7 / 5.6 / 1.4×** WT. ⇒ **the same animal is 5–11× supraphysiological in three regions and at-or-below normal in the fourth.** Against: `CLAIM 028` (WWOX output is partner- and context-dependent; *"more WWOX = better"* is not linear), the organoid **loss of the apoptotic checkpoint**, WWOX's pro-apoptotic role in some contexts, and tumour-suppressor status with a still-null periphery and a non-finding qualified three times (*gross*, *limited number*, *8–11 months*). **"Neither too little nor too much WWOX" is not a rhetorical caution here — one animal has both** |
| **IMMUNE / DELIVERY_LIMITATIONS** | ICV, neonatal, **stereotaxic** (a declared upgrade from free-hand in 2021). **Not CNS-confined:** WWOX protein detected in the **sciatic nerve** of HD animals (blot, **no quantification**, band intensity ranging from strong to barely detectable across seven animals) and in **spinal cord** at 0.8–1.3× WT; **liver negative** (0.03–0.1, at background). 🔴 **No immunological measurement appears in the locators** — no anti-capsid or anti-transgene response, no complement, no DRG histopathology. 🔴 **Correction to the map:** R-01's `KNOWN_MAJOR_SAFETY_CONSTRAINTS` field asserts *"dose-limiting DRG/peripheral-ganglion toxicity at high systemic dose"* in a field that otherwise reports this vector's own measurements. **No DRG assessment appears in either WWOX paper.** The only place in this repository where DRG pathology is stated is a **review, at class level** — PMID 42128308 §11, *"high-dose AAV administration"* driving DRG pathology as *"a key regulatory concern in pediatric CNS gene therapy programs"*. Whatever its route into the map, the statement is **TRANSFERRED (T4/T5)**, not measured in WWOX, and belongs labelled as such. The genuinely WWOX-measured PNS fact is different and more specific: **the neuron-specific construct reaches the sciatic nerve** — a biodistribution finding, not a toxicity finding. ⚠️ And the same review closes a loop the map does not carry: WPRE removal was framed as a safety choice, but **efficacy was repurchased with vector** (a six-fold dose increase), while §11 of that review names high-dose AAV as the driver of DRG pathology |
| **TRANSLATIONAL_DISTANCE** | The mouse is dosed at P0–P5 (≈ human perinatal) in a systemic constitutive null that dies at 3–4 weeks untreated. A human recipient is a compound-genotype child **past** the window, with part of the damage laid down before birth — cortical thinning is measurable at **E16.5**. The single human datum is a compassionate n-of-1 reported at **news level only**, one-month outcome, not peer-reviewed |

### Quality signals, weighted proportionately

Three text-versus-panel discrepancies in the dose paper — locomotor (4D/4E), spike count (7C), and a
myelin dose-dependence claimed against unquantified panels — **each in the direction favourable to the
therapy**; blinding declared as *"in a blinded manner **when feasible**"* against the 2021 paper's
unconditional statement; and a declared commercial interest (one consultant, three employees, funding)
absent from the 2021 paper.

**What this is, and what it is not.** It is **not** an argument against the data, most of which are strong
and quantified. It is a reason the paper's **unquantified and text-only** assertions carry less weight than
its quantified panels. **The verdict below follows the quantified panels.**

### Verdict

> ### `AAV9_WWOX_STATUS: SPLIT — partial downgrade`
>
> | Scope | Class |
> |---|---|
> | **Survival · SWD/electrographic · motor · gliosis**, at **HD**, in the **P0–P5 window** | `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` — **retained** |
> | **Developmental trajectory · cognition** | 🔻 `PROMISING_BUT_GAP` — **never measured, for any intervention** |
> | **Myelination**, in the dose study | 🔻 `PROMISING_BUT_GAP` — **claimed in text, unquantified in every treated panel** |
> | **Cerebellum** | 🔻 `PROMISING_BUT_GAP` — **systematically under-transduced**, while carrying the most penetrant phenotype |
> | **Post-neonatal administration** | 🔻 `PROMISING_BUT_GAP` — **never tested; explicitly future work** |

**This is a downgrade, not a re-labelling.** The class previously attached to an **intervention**; it now
attaches to an **(intervention × endpoint × window)** triple. That is the map's own rule — *"tier is
assigned to the conjunction, not to the drug"* — **applied for the first time to its own top entry**.

**And R-01 still ranks first.** Nothing else is close, and no other candidate gained ground here. What it
no longer does is rank first *on disease modification* — because **nothing in the portfolio has been
measured there**, and the previous class name asserted a readiness that the developmental column does not
support.

**Decisive tests for R-01** — the map's two, retained, plus three the second pass adds:

1. **Intermediate-dose arm between 1.23 and 2.63 × 10¹¹ vg — carrying an expression readout.** The existing
   threshold has no expression correlate; a third dose without one would reproduce the same gap.
2. **Delayed, post-onset dosing in a hypomorphic (non-null) model, with a cognitive/learning endpoint** —
   not ECoG and myelin alone. See `E-D1`.
3. 🆕 **A cerebellum-directed arm** (route or capsid) with a motor/ataxia endpoint.
4. 🆕 **Quantified MBP in the treated arms of the dose study.** The claim exists; the measurement does not.
5. 🆕 **A long-term safety arm in animals carrying 5–11× physiological WWOX**, with tumour surveillance
   **beyond 8–11 months** and DRG histopathology — the two qualifications the existing non-finding names
   about itself.

---

## 6 · Revival triggers

Every trigger states **what new observation would materially change the verdict**. *"More evidence"* appears
nowhere. Marked `NEW` (written here), `REWRITTEN` (the map's trigger presupposed something this pass
removed), or `CARRIED` (the map's trigger survives and is reproduced for completeness).

### `DEPRIORITIZE` (12)

| # | Candidate | `REVIVAL_TRIGGER` | |
|---|---|---|---|
| 1 | **R-04 Lithium** | A seizure-susceptibility experiment reporting a **tested, pre-specified genotype × treatment interaction** for lithium in `−/−` vs `+/+` — the comparison ethosuximide already has; **or** a lithium-attributable change in a WWOX-dependent molecular readout (Tau pS396/S404, nuclear β-catenin, or non-pS9 GSK3β output) with a parallel wild-type arm | `REWRITTEN` |
| 2 | **N-01 mTOR inhibitors** | A **protein-level** mTORC1 readout in a WWOX-deficient neuronal system — p-S6 (S235/236, S240/244) and the **p-4E-BP1/total-4E-BP1 ratio**, with an assay-positive control — showing **mTORC1 hyperactivation**; **or** an autophagic **flux** measurement (LC3-II/p62 ± bafilomycin) in a WWOX-deficient neuron that fixes the sign of the WWOX→autophagy relationship | `REWRITTEN` — the map's trigger accepted "any protein-level readout"; this pass shows the axis is not merely unmeasured but **directionally undetermined**, so the trigger must fix a **sign**, not merely produce a number |
| 3 | **N-03 Na-channel blockers** | Documented Na-blocker response in WWOX burst-suppression cases, or a Nav dependence measured in a WWOX model | `CARRIED` |
| 4 | **N-07 Digoxin** | A cardiac-glycoside-class agent with a CNS-bioenergetic endpoint (not glycaemia) in a WWOX system, at a dose with a defensible paediatric index — **and** verification of the reported 100 mg/kg i.p. against the original PDF, which remains unchecked | `NEW` |
| 5 | **N-08 Dichloroacetate** | Falsification of R-05 by Seahorse (removing the dominating alternative) **together with** a PDK-inhibition arm showing a CNS endpoint at a dose below the documented neuropathy threshold | `NEW` |
| 6 | **N-09 pTyr33-WWOX peptide** | The full text (currently paywalled) contradicting the abstract on the direction of pTyr33-WOX1's action; the refutation rests on the abstract alone | `CARRIED` |
| 7 | **N-10 Splice-switching ASO (acceptor allele)** | A **systematic counterexample search** returning any published case where an SSO restored a transcript across an **abolished invariant acceptor** — the search this repository has never run, which is why the status is `stress-tested` and not `refuted`; **or** junction-spanning RT-PCR (map `E-4`) revealing a productive cryptic isoform that masking could redirect | `NEW` |
| 8 | **N-11 4-PBA / TUDCA** | Confirmation of the **lysosomal/CMA** arm for the SDR-missense allele **plus** evidence that 4-PBA's **HDAC-inhibitor / HSP-co-inducer** action — a different mechanism from the retracted ER-chaperone one — changes WWOX solubility or function; the ER rationale itself cannot be revived | `CARRIED, sharpened` |
| 9 | **N-12 HSP70 co-inducers** | **LAMP2A-dependence** demonstrated for the variant's degradation (associative HSC70/LAMP1 evidence is insufficient) **together with** a co-inducer arm that raises **soluble, correctly localized, partner-binding** WWOX rather than total abundance | `NEW` |
| 10 | **N-13 Pro-myelinating agents** | An **oligodendrocyte-specific** WWOX deletion or rescue (Olig2/CNP-Cre) showing a cell-autonomous myelin phenotype — the residual gap the authors attribute to one is their `IPOTESI`, and the AAV oligodendrocyte arm is technically confounded by poor neonatal-ICV tropism | `NEW` |
| 11 | **N-14 Antioxidants** | A **redox-flux** measurement in a WWOX-deficient **neural** system, germline rather than acute-knockdown, fixing the sign of WWOX ↔ ROS in that context; the two counter-directional primaries are a photoreceptor knockdown and a fly, neither comparable | `NEW` |
| 12 | 🆕 **N-16 Pannexin blockade** | A **powered, significance-tested** pannexin-blocker arm in a WWOX system reporting a **reduction** in burst frequency at a stage where the current measurement showed a ~2.5-fold **increase** — and, per the authors' own suggestion, at an **earlier developmental stage** than P13–P17 | `NEW` |

### `PROMISING_BUT_MECHANISTIC_GAP` (3)

| # | Candidate | `REVIVAL_TRIGGER` (here: what would **promote** it) | |
|---|---|---|---|
| 13 | **R-02 Memantine / NMDAR** | **Memantine itself** (not d-APV) reducing burst frequency and phase–amplitude coupling dose-dependently in a WWOX-deficient system **with the isogenic parental and rescue lines as internal comparators**; and a **chronic** arm showing that the maturation cost of sustained NMDAR blockade does not exceed the network benefit. *(The tool-compound conjunction is already satisfied — see §3.4.)* | `NEW` |
| 14 | **R-05 Ketogenic diet** | **Seahorse OCR/ECAR or isotope tracing** on donor-derived cells (and on the existing WWOX-KO organoids) confirming a real bioenergetic shift. **Falsifier, symmetrically stated:** if flux is normal, the rationale falls and the entry moves to `DEPRIORITIZE` regardless of the empirical DEE evidence | `NEW` |
| 15 | **R-09 Proteostasis (SDR missense)** | **Nascent synthesis + pulse-chase with soluble/insoluble fractionation** discriminating translation from solubility from turnover; promotion of any hit **only** on ≥2 orthogonal readouts beyond abundance, including **subcellular localization and partner binding**, and only if the stabilizer demonstrably spares **388–407/L404** | `NEW` |

### `TRANSFER_HYPOTHESIS` (3)

| # | Candidate | `REVIVAL_TRIGGER` | |
|---|---|---|---|
| 16 | **R-03 Wnt / tankyrase** | Nuclear β-catenin state measured **first** in the target compartment, then XAV939 **vs** CHIR99021 on cortical-layering rescue in WOREE organoids. 🆕 **And a compartment the map does not require: a cerebellar Wnt measurement**, because §2.3 shows the sign may split by region and the whole lever is scored on forebrain. Plus a paediatric-compatible modality, which does not currently exist | `NEW` |
| 17 | **R-06 Anti-neuroinflammatory** | In the existing `Wwox^P47T` mouse (>1 year survival): does the agent reduce astro-microgliosis, slow Purkinje loss and improve motor coordination **beyond** what neuron-restricted WWOX rescue achieves on its own? The comparator arm is the trigger — without it the axis remains a consequence being treated as a cause | `NEW` |
| 18 | **R-08 Base / prime editing** | Junction-spanning RT-PCR ± NMD block and amplicon (long-read if needed) sequencing establishing the real transcript — **the mandatory gate before any modality choice** — followed by a PAM-availability and bystander-cytosine survey at the locus. ⚠️ `DL-MECH-069` (NMD efficiency may itself be WWOX-dependent) means the NMD-block control may be a **variable**, and the design must treat it as one | `NEW` |

### Outside the three requested classes, written because they carry weight (3)

| # | Object | `REVIVAL_TRIGGER` | |
|---|---|---|---|
| 19 | **R-01-B** — the newly downgraded AAV arm | Any endpoint in the `DEVELOPMENTAL_TRAJECTORY` or `COGNITION` column, in any WWOX model, under any intervention, **with a seizure-matched comparator arm** — the design of `E-D1`. Separately, quantified MBP in a treated arm, and a cerebellum-transducing route with a motor endpoint | `NEW` |
| 20 | **R-07 Bumetanide** (`INSUFFICIENT_EVIDENCE`, listed for completeness — it is not in the three requested classes and is **not** promoted) | Gramicidin perforated-patch `E_GABA` in WWOX-KO vs isogenic parental neurons, with NKCC1/KCC2 and the GABA response. **This single measurement converts the whole M3 axis from T6 to T2 — or closes it.** Until it exists, bumetanide is unrankable, not low-ranked | `CARRIED` |
| 21 | **The `GAP_JUNCTION` node** (a node, not a candidate) | Occlusion: a selective connexin blocker, or Cx36/Cx43 genetic manipulation, showing an effect **that survives sub-maximal NMDAR blockade**. If it does not, the node collapses into NMDAR and stops being an independent target | `NEW` |

> ### `REVIVAL_TRIGGER_COUNT: 18` in the three requested classes · **21 written in total**
> (12 `DEPRIORITIZE` including the new N-16 · 3 `PROMISING_BUT_MECHANISTIC_GAP` · 3 `TRANSFER_HYPOTHESIS`
> · 3 outside those classes, itemized above.)

---

## 7 · The preclinical discrimination package

**Four experiments.** Each is chosen because it kills more than one hypothesis. Ordered by how much of the
symptomatic / mechanistic / developmental confusion it removes per unit cost.

**Scope note, stated so the omission is visible:** the map's `E-4` (junction-spanning RT-PCR ± NMD block)
and `E-5` (nascent synthesis + pulse-chase) are **retained unchanged** and are deliberately **not** in this
package. They discriminate **which mechanistic branch** an allele takes; they do not bear on the
symptomatic/mechanistic/developmental distinction this package exists to resolve. They remain mandatory
gates in their own chains.

### `E-D1` — Delayed dosing with a seizure-matched comparator

| Field | |
|---|---|
| **QUESTION** | Does restoring neuronal WWOX **after** the developmental window move a developmental/cognitive endpoint — or only the symptomatic ones? |
| **MODEL** | A **hypomorphic (non-null)** model that survives past weaning — the `Wwox^gt/gt` hypomorph or the `Wwox^P47T` knock-in (>1 year). **Not** the systemic null, which dies before any learning assay can run and is metabolically decompensated in the only window it offers |
| **INTERVENTION** | AAV9-hSynI-WWOX at three timepoints: P0–P5 (established window) · post-onset early · post-onset late |
| **CONTROL** | AAV9-hSynI-GFP at each timepoint · untreated hypomorph · wild type · 🔴 **and a symptomatic comparator arm: an ASM titrated to equivalent SWD suppression** |
| **PRIMARY_ENDPOINT** | A **cognitive/learning** measure — the empty column — pre-specified, blinded, powered |
| **MECHANISTIC_ENDPOINT** | Regional WWOX protein (cortex · hippocampus · midbrain · **cerebellum**) · SWD burden · myelin **quantified against wild type** · sIPSC amplitude in L2/3 pyramidal neurons |
| **EXPECTED_IF_TRUE** | The cognitive endpoint improves in the gene-therapy arms and **not** in the seizure-matched ASM arm |
| **EXPECTED_IF_FALSE** | Both arms suppress SWD equally and **neither** moves the cognitive endpoint ⇒ gene addition past the window is symptomatic, and **N-15 extends to the causal lever itself** |
| **INTERPRETATION_RISK** | 🔴 **The ASM-matched arm is the whole design.** Without it, any cognitive improvement is attributable to seizure reduction and the experiment answers nothing — which is precisely the error N-15 was written to prevent. Second risk: a hypomorph is not a null; the timepoints must be anchored to a **measured developmental landmark**, not to a calendar, or the "window" is a species artefact |
| **KILLS AT ONCE** | R-01's post-neonatal gap · N-15's scope (symptomatic levers only, or all late levers?) · `H-3`'s threshold argument on a cognitive endpoint · the `TIME-BUY` scoring of `TX-006` |

### `E-D2` — The occlusion experiment

| Field | |
|---|---|
| **QUESTION** | (a) Does the carbenoxolone effect survive when NMDAR is already blocked? (b) Does **memantine** — the actual candidate — reproduce d-APV's effect? |
| **MODEL** | `Wwox` S-KO neocortical slices at P13–P17 (the exact preparation where bursting is characterized) **and** WOREE patient-iPSC organoids on MEA, with parental and W-AAV-rescue lines |
| **INTERVENTION** | d-APV · **memantine (dose–response)** · carbenoxolone · **sub-maximal d-APV + CBX co-application** · a selective connexin blocker · BB-FCF |
| **CONTROL** | Isogenic parental/rescue line as internal comparator · vehicle · **washout reported for every arm** |
| **PRIMARY_ENDPOINT** | Normalized burst frequency, duration, amplitude; phase–amplitude coupling |
| **MECHANISTIC_ENDPOINT** | **Occlusion** — the co-application arm |
| **EXPECTED_IF_TRUE** | Gap junctions are an independent node ⇒ CBX reduces bursting **further** in the presence of sub-maximal d-APV |
| **EXPECTED_IF_FALSE** | No further reduction ⇒ the gap-junction node **collapses into the NMDAR node**, and R-02 becomes the only circuit candidate in the portfolio |
| **INTERPRETATION_RISK** | 🔴 d-APV already drives frequency to **zero**, so there is **no headroom for occlusion at full block** — the co-application must run at a sub-maximal concentration taken from the memantine dose–response, or the experiment cannot fail informatively. And the **washout overshoot** (~1.85× baseline after d-APV) must be reported for every arm, not only the treatment phase; a blocker that rebounds above baseline is a different clinical object from one that does not |
| **KILLS AT ONCE** | The `GAP_JUNCTION` row · R-02's compound gap · N-16 · and it merges the map's `E-1` and `E-9` into one experiment |

### `E-D3` — The one-blot mTOR / autophagy row

| Field | |
|---|---|
| **QUESTION** | Does mTORC1 **activity** move in a WWOX-deficient human neuron, and in which direction? |
| **MODEL** | WWOX-KO vs **isogenic parental** hESC-derived neurons/organoids (the bench already exists), plus WOREE patient-derived |
| **INTERVENTION** | **None — this is a measurement**, which is why it is the cheapest experiment in the package |
| **CONTROL** | Isogenic parental · **an assay-positive control in the same lysates** (insulin / amino-acid stimulation and rapamycin) |
| **PRIMARY_ENDPOINT** | p-S6 (S235/236 and S240/244) · **p-4E-BP1 (T37/46) and total 4E-BP1, as a ratio** — never the transcript |
| **MECHANISTIC_ENDPOINT** | LC3-II / p62 **with and without bafilomycin A1** — **flux**, not steady state; a steady-state LC3 blot cannot separate blocked degradation from reduced initiation, which is the exact ambiguity §1 identified |
| **EXPECTED_IF_TRUE** | The transcript reading is right ⇒ reduced p-S6 and a reduced p-4E-BP1/total ratio, with reduced autophagic flux |
| **EXPECTED_IF_FALSE** | Unchanged or **increased** mTORC1 phosphosignal ⇒ the sole directional datum behind N-01 was a transcript artefact, and the row closes as *unmeasurable-by-transcript* rather than as *unfavourable* |
| **INTERPRETATION_RISK** | An organoid with declared regionalization and maturation defects has a different **cell composition** from its control; a bulk-lysate difference may be composition rather than signalling — the identical criticism the dossier already makes of the glycolysis/OXPHOS signal. Mitigate with a 2D neuronal line or a cell-type-resolved readout |
| **KILLS AT ONCE** | N-01's directional claim · the `MTOR` row of §3 · and it decides whether an entire approved drug class is a live question or a closed one |

### `E-D4` — Genotype × treatment, once, for the whole repurposing shelf

| Field | |
|---|---|
| **QUESTION** | Which compounds on the shelf show a **tested interaction** with WWOX genotype, rather than a main effect? |
| **MODEL** | One seizure-susceptibility assay (PTZ threshold or spontaneous-seizure burden) in `Wwox+/+`, `+/−` and `−/−` **littermates** — the design that already exists |
| **INTERVENTION** | Lithium · a **non-lithium** GSK3β inhibitor (and, if available, an Axin-site ligand, which also tests `H-1`) · memantine · **ethosuximide as the positive control for detectable specificity** |
| **CONTROL** | Vehicle in all three genotypes; 🔴 **the interaction term pre-specified and reported**, never inferred from per-genotype significance stars — the exact failure that produced this file's §2 |
| **PRIMARY_ENDPOINT** | **Genotype × treatment interaction**, powered for it |
| **MECHANISTIC_ENDPOINT** | For the GSK3β arms, a **non-pS9** kinase-output readout (Tau pS396/S404, or the GS-1 peptide assay) in the treated brains — the measurement that separates target engagement from anticonvulsion |
| **EXPECTED_IF_TRUE** | Interaction significant for the mechanism-directed compound and not for the generic anticonvulsant |
| **EXPECTED_IF_FALSE** | No compound shows an interaction ⇒ the whole GSK3β repurposing arm is a general-anticonvulsant story and R-04 moves from `DEPRIORITIZE` to closed |
| **INTERPRETATION_RISK** | 🔴 The systemic null is **hypoglycaemic, acidotic and uraemic** in the assay window (`CLAIM 036`), and Ser9 is the AKT site. **Running this in the systemic null reproduces the confounder it is meant to remove.** A normoglycaemic model, a conditional deletion, or a glucose-clamped arm is required before any pS9-adjacent readout is interpretable at all |
| **KILLS AT ONCE** | R-04 · the M4 in-vivo anchor · `H-1`'s premise if the Axin-site arm is included · and it retires or promotes the entire GSK3β shelf in one design |

> ### `TOP_DISCRIMINATING_PRECLINICAL_EXPERIMENTS`
> **`E-D3`** (cheapest — one blot, no intervention, closes a drug class) → **`E-D2`** (one preparation,
> resolves two nodes and one new negative, and discharges two of the map's ten experiments) →
> **`E-D4`** (one design, retires or promotes a whole shelf) → **`E-D1`** (most expensive, and the only one
> that can answer the question the entire portfolio is ranked on).

---

## 8 · Canonical claims affected — reported, not repaired

**Nothing below is edited by this file.** Each is a defect or a boundary for the pipeline to carry through
INGEST → DEEP_DIVE → COMMIT.

| Claim / record | What this pass found | Class |
|---|---|---|
| **`CLAIM 016`** | (a) The evidence boundary cites **Fig. 7b** for the lithium panel; the primary's caption and Results say **Fig. 7d**, and 7b is ethosuximide. (b) The Summary's *"GSK3β is elevated"* and the boundary's preserved *"dato di abbondanza"* are **in neither cited source** — Cheng's Fig 7c shows total GSK3β **flat** and pSer9 **falling**; Wang reports both **unchanged** | 🔴 defect ×2 |
| **`CLAIM 016` × `CLAIM 035`** | They are measured on **incompatible axes**. `CLAIM 035` says the WWOX brake is **S9-independent** and warns that a pS9 western would return a false negative; the **only in-vivo de-repression evidence is a pS9 western**. Either the in-vivo signal is not the `CLAIM 035` mechanism (⇒ CHAIN C has no in-vivo anchor) or S9-independence needs a boundary | 🔴 mutual exclusion |
| **`CLAIM 016`, alternative explanation** | Ser9 is the AKT site; the systemic null is hypoglycaemic at P18 (`CLAIM 036`) and the westerns are at P20. `PREMISE: INFERENZA`, confounder class transferred from a different null strain — it does not refute, it means the design cannot separate | ⚠️ boundary |
| **`CLAIM 021`** | The Summary's *"increased excitatory drive, reduced spontaneous inhibition"* carries the **abstract's ordering**. The panels: excitatory amplitude +6% (1.4 pA inside a 12-pA SD) with superimposed frequency distributions; inhibitory amplitude **−52%**. The paper's own Results say the shift is *"primarily through an impairment in the amplitude of the inhibitory currents"* | 🔴 emphasis defect |
| **`CLAIM 021`, unpropagated content** | The source establishes **pharmacological** NMDAR dependence (d-APV → burst frequency **zero**), a **non-attributable** gap-junction effect (CBX blocks NMDAR; no washout), and a **directionally adverse** pannexin result. None of this reached the claim, which states only that *"bursting depends on NMDAR and gap junction activity"* | 🔴 under-propagation |
| **`CLAIM 032`** | *"Haploinsufficiency is not deleterious"* is true of lifespan, gross morphology and carrier clinical status. **Two independent models now show the heterozygote measurably abnormal on network and conduction physiology** (bursting in 4/23 slices vs 0/11 WT; four intrinsic properties; Tc-MEP latency indistinguishable from the null). The claim's declared limit is now filled with **positive counter-observations**, not absence of evidence | ⚠️ boundary — and it re-scores `H-3` |
| **`CLAIM 011`** | (a) The survival threshold has **no measured expression correlate** (7 of 8 dose comparisons `ns`), and the paper's explanation is survivor-conditioned. (b) **Myelination is not quantified in any treated arm** of the dose study, while the text claims *"near-complete rescue"*. (c) **Cerebellum is at or below wild type at every dose and timepoint** | 🔴 ×3 |
| **`CLAIM 004`** | The map's R-01 field asserts **DRG toxicity** as a property of this vector; it is a **review-sourced, class-level** statement (PMID 42128308 §11) with **no DRG assessment in either WWOX paper**. The WWOX-measured PNS fact is **sciatic-nerve biodistribution**, which is a different object | ⚠️ transferred-as-direct |
| **`CLAIM 002` / `DL-MECH-034`** | The *"mTOR/EIF4EBP1 ↓, autofagia ↓"* line has **no verbatim locator** in the manifest (12 entries, none touching it), no mention in the dossier and none in the commit candidate. Under this repository's own export rule it could not be exported — yet it carries `TOP_NEGATIVE_FINDINGS` #2 | 🔴 unlocatored load-bearing datum |
| **Paper registry** | `CORPUS-STUB-177` (PMID 31966718) is a **second** unread WWOX+mTOR record, contradicting the map's *"only other WWOX record naming mTOR"*. `CORPUS-STUB-043`, `-056` and `-139` name WWOX↔autophagy in **two opposite directions** | 🔴 map correction · ⚠️ read-priority |
| **`therapy_levers.md` · `TX-005`** | Both still carry *"lithium … **abolishes** seizures"* and *"the strongest repurposing signal"*, **without** the all-three-genotypes boundary that `CLAIM 016` has carried since 2026-08-10 | 🔴 unpropagated boundary |

---

## 9 · Closing blocks

> ### `MTOR_DIRECTIONALITY_VERDICT`
> **`INSUFFICIENT`.** One bulk transcriptome (`n=2` vs `n=4`, raw `P<0.01`, no FDR, no protein, **no
> locator**), whose two directions contradict each other under the coupling needed to read either, and whose
> `EIF4EBP1` component inverts when read as biology rather than as gene-set membership. The autophagy axis it
> would have to be read through is catalogued in **two opposite directions** in this repository's own
> registry. **No positive WWOX rationale exists at any tier and mTOR inhibitors remain out** — but the reason
> is *"never measured"*, not *"wrong direction"*, and N-01 must stop being cited as a demonstration.

> ### `LITHIUM_REPURPOSING_VERDICT`
> **`DEPRIORITIZE` — verdict unchanged, reasons strengthened, scope narrowed.**
> `LITHIUM_WWOX_SPECIFICITY: NOT DEMONSTRATED` — a **negative in an assay of demonstrated sensitivity**, not
> an absent test. `LITHIUM_DIRECTIONALITY: CONFLICTED ACROSS TWO AXES AND UNMEASURED IN ITS OWN MODEL`.
> Six of the seven disaggregated components are **empty**; the seventh is a general anticonvulsant effect,
> and a general anticonvulsant effect is not counted as WWOX rescue.

> ### `PV_GABA_CIRCUIT_REVISED_STATUS`
> **Decomposed into eight axes; three moved.** `NMDAR` **upgraded** to T1 for the tool compound (the map's
> `E-1` was already discharged in the repository). `GAP_JUNCTION` **downgraded** — carbenoxolone blocks
> NMDAR, its effect does not wash out, and the node is not separable. **Pannexin blockade enters as a new
> negative (N-16)**, directionally adverse on the only WWOX measurement. `MTOR` re-characterized as
> unmeasured rather than contra-directional. `SEIZURE_NETWORK_CONTROL` corrected on which current carries
> the E/I shift. `CHLORIDE_HOMEOSTASIS`, `PV_INTERNEURON` and `GABA_RECEPTOR` unchanged — **bumetanide is
> not promoted.** `DEVELOPMENTAL_RESCUE` is empty for every intervention in the portfolio.

> ### `AAV9_WWOX_STATUS`
> **`SPLIT` — partial downgrade.** `READY_FOR_WWOX_PRECLINICAL_CONSIDERATION` **retained** for survival,
> SWD, motor and gliosis at HD in the P0–P5 window. **Downgraded to `PROMISING_BUT_GAP`** for developmental
> trajectory and cognition (never measured), myelination in the dose study (claimed, unquantified),
> the cerebellum (systematically under-transduced while carrying the most penetrant phenotype), and any
> post-neonatal application (never tested). **It still ranks first; it no longer ranks first on disease
> modification, because nothing has been measured there.**

> ### `SYMPTOM_VS_DISEASE_MODIFICATION_MATRIX_COMPLETE: NO`
> Complete as a map of what has been measured; incomplete as a comparison of interventions. **Every
> intervention with a filled `SEIZURE_CONTROL` cell has empty `DEVELOPMENTAL_TRAJECTORY` and `COGNITION`
> cells, without exception.** The only data in those columns are human, observational, and **negative**.

> ### `REVIVAL_TRIGGER_COUNT: 18`
> in the three requested classes (12 `DEPRIORITIZE` · 3 `PROMISING_BUT_MECHANISTIC_GAP` ·
> 3 `TRANSFER_HYPOTHESIS`); **21 written in total**, the extra three covering the newly downgraded AAV arm,
> bumetanide, and the gap-junction node.

> ### `TOP_DISCRIMINATING_PRECLINICAL_EXPERIMENTS`
> **`E-D3`** protein-level mTORC1 + autophagic flux (one blot, no intervention — closes a drug class) →
> **`E-D2`** occlusion: memantine, CBX and sub-maximal d-APV in one preparation (resolves two nodes and a
> new negative; subsumes the map's `E-1` and `E-9`) → **`E-D4`** genotype × treatment with a pre-specified
> interaction term and a non-pS9 engagement readout (retires or promotes the GSK3β shelf) → **`E-D1`**
> delayed dosing in a hypomorph **with a seizure-matched ASM comparator** and a cognitive primary endpoint
> (the only experiment that can answer the question the portfolio is ranked on).

> ### `CANONICAL_CLAIMS_AFFECTED`
> `CLAIM 016` (panel misattribution; abundance datum absent from both sources) · `CLAIM 016 × CLAIM 035`
> (mutual exclusion on the S9 axis) · `CLAIM 016` (systemic-hypoglycaemia alternative explanation, via
> `CLAIM 036`) · `CLAIM 021` (E/I emphasis; and three unpropagated pharmacological results) ·
> `CLAIM 032` (haploinsufficiency boundary now filled by positive counter-observations) ·
> `CLAIM 011` (threshold without expression correlate; myelin unquantified; cerebellar gap) ·
> `CLAIM 004` (DRG constraint is transferred, not measured) · `CLAIM 002` / `DL-MECH-034`
> (unlocatored mTOR/autophagy line) · paper registry (`CORPUS-STUB-177` unrecognized; three
> counter-directional autophagy stubs) · `TX-005` and `therapy_levers.md` (the lithium boundary never
> propagated). **Ten records. None edited here.**

> ### `THERAPEUTIC_CANDIDATES_UPGRADED`
> **One, and only in part: R-02.** Chain B moves **T2 → T1 for the tool compound** — the pharmacological
> dependence was established inside the WWOX-deficient system, and the evidence was already in the
> repository when the map scored it conservatively. **Memantine itself does not move**: it has still never
> been given to a WWOX system, and the gap is now precisely one compound wide instead of one experiment wide.
> **No new candidate was added to any shortlist. No empty slot was filled.**

> ### `THERAPEUTIC_CANDIDATES_DOWNGRADED`
> **R-01** — split; downgraded for development, cognition, myelin-in-the-dose-study, cerebellum, and
> post-neonatal use. **The gap-junction node** — removed as an independent target pending occlusion.
> **Pannexin blockade** — enters as **N-16**, `DEPRIORITIZE`, on the only WWOX measurement that exists.
> **N-01's rationale** — from *"acts in the wrong direction"* to *"never measured at protein level"*; this
> is a **weakening of a negative, not a promotion of the drug class**, and the operational position is
> unchanged.

---

**Layer discipline.** This file modified no canonical file, promoted no hypothesis, named no new molecule,
formulated no clinical indication, dose, schedule or sequence of care, and designed no sequence or construct.
Where it disagrees with [`mechanism_intervention_map.md`](mechanism_intervention_map.md), it is the newer
reading and the weaker artefact; reconciliation goes through the pipeline. Every molecule named anywhere in
this chain is **material for discussion with a treating clinical team**, and nothing here substitutes for one.
**Not medical advice.**
