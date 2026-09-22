# SUBFIELD- AND CELL-TYPE-RESOLVED WILD-TYPE `Wwox`/`WWOX` EXPRESSION — scoring `P7`, adjudicating `H3`, and auditing one DATO line

**Node:** `E5_EXECUTION_P7_SCORING` · **Actor:** SCIENTIST 1 (`scientist-1`) · **Date:** 2026-09-22
**Status:** 🔴 **non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, every
registry, every ledger, the receipt chain and the state manifest. No claim, no paper record, no working-model
edit, no commit candidate, no gate, no promotion. Nothing here was promoted and nothing here may be cited as
canonical.

> 🔴 **Nothing in this file is medical advice.** No molecule, no dose, no route, no schedule, no compound, no
> screen. A mechanistic adjudication is not a treatment.
> 🔵 **Public edition.** All reasoning is at the level of a genotype class and of named animal alleles. No
> individual-level record appears anywhere.
> ⚠️ **Alleles and models are kept strictly separate and are never pooled.** `Wwox`-null mouse, `gt/gt`,
> `lde/lde` rat, `P47T`, `P47R`, `G372R`, human WOREE and human SCAR12 are **distinct**. Every statement
> below carries the model it was measured in. 🔴 **Nearly every source in this file is a WILD-TYPE expression
> map and carries no WWOX-deficient genotype at all** — which is exactly what `P7` asked for, and is also the
> boundary of what it can settle.

**This file executes `E5` of [`new_discovery_node_20260922.md`](new_discovery_node_20260922.md) § 7** — the
one component of that node's minimal discriminating experiment graded 🟢 **EXECUTABLE NOW**, zero cost, zero
animals — and scores the outstanding `P7`, left ⚪ **UNTESTED** at `new_discovery_node_20260922.md:256` and
restated as still unscored today at `lde_myelin_vacuole_bridge_20260922.md:271`.

---

## 0 · READ DEPTH, DECLARED PER SOURCE, BEFORE ANY FINDING

🔴 **Why this section is split, and why § 0.2 sits physically after § 2.** The method required § 2's Part B
expectation to be on disk **before** any external query ran. Read depths cannot be declared before the
sources are touched. So § 0.1 fixes the convention up front, § 2 was written and flushed to disk, and
§ 0.2 — **the completed per-source depth table, which governs everything in §§ 3–6** — was written
immediately after the search and before any finding was recorded. **Read § 0.2 before § 3.** The file order
preserves the audit trail; it is not a lapse.

### 0.1 The convention

| Mark | Meaning |
|---|---|
| 🟢 **READ DIRECTLY THIS ACT** | I fetched and read the artefact myself, in this act, at the stated depth |
| 🔴 **SIBLING-ATTESTED** | Quoted from a LEGEND dossier, ledger or analysis file, **with repo file and line**. A dossier is a contemporaneous record of someone else's read. **It is not a fresh fetch and is never presented as one** |
| 🟡 **ABSTRACT-DEPTH** | Title/abstract only. 🔴 **An abstract is not a read** |
| ⚫ **SOURCE_BLOCKED** | The surface was tested once in this act and failed. The failure is recorded as a fact with its exact mode. **No retries** |

---

## 1 · BASELINE — what the repository already held, and what I therefore did not redo

**`enumerate_baseline_before_scoring` was run before any external query.** I read
`new_discovery_node_20260922.md` in full, then `wwox_postnatal_svz_expression_20260922.md`,
`purkinje_cerebellar_celltype_wwox_census_20260922.md`, `cerebellum_layer_localisation_20260922.md`,
`wwox_myelin_oligodendrocyte_census_20260921.md` and `lde_myelin_vacuole_bridge_20260922.md`, and grepped the
whole `disease-models/wwox/` tree for `CA1|CA3|dentate|subfield`, for atlas tokens
(`Allen|HPA|proteinatlas|GTEx|DropViz|mousebrain|BrainRNAseq|snRNA|scRNA`) and for the Part C strings.

### 1.1 🔴 ALREADY HELD — I did not redo any of this, and I claim none of it as new

| Datum | Species · resolution | Where the repository holds it | Depth of the repository's hold |
|---|---|---|---|
| **Allen Mouse Brain Atlas ISH**: `Wwox` probe *"clearly visible in cerebellum cortex"*; strongest signal in **medial entorhinal cortex layer 2 (`ENTm2`)**, **basolateral amygdala (`BLAa`/`BLAp`)**, **isocortex layer 5** | mouse, adult · 🔴 **REGION only, no cell type, no hippocampal subfield** | `purkinje_cerebellar_celltype_wwox_census_20260922.md:289`; `wwox_postnatal_svz_expression_20260922.md:111` | 🔴 **A REVIEW'S RESTATEMENT of the atlas** (`PMC7727818`, Aldaz & Hussain 2020 § 2), not a query of the atlas itself |
| **DropViz** (Saunders 2018, mouse adult scRNA-seq): top cerebellar clusters = **`Pvalb`⁺ interneurons / GABAergic basket cells**, then **`Gabra6`⁺ granule cells**; also frontal L5, medial EC; ependymal/choroid *"data not shown"*. **No Purkinje cluster reported in either direction** | mouse, adult · 🟢 cell type | `purkinje_cerebellar_celltype_wwox_census_20260922.md:288`, `:297` | 🔴 Same review's restatement |
| **BrainRNAseq (mouse P7 cell-type RNA-seq)**: *"uniform expression … in neurons and all glial cell types"*; within the oligodendrocyte lineage **progenitors > mature myelinating** | mouse, **P7** · 🟡 broad classes | `wwox_postnatal_svz_expression_20260922.md:112`, `:137`; `purkinje_cerebellar_celltype_wwox_census_20260922.md` (same table) | 🔴 Same review's restatement |
| **GTEx** human bulk: cerebellum **median 12.1 TPM**, frontal cortex 6.9, amygdala 6.2, **hippocampus 5.6**; local CSV at `analysis/data/WWOX_tissue_expression_GTEx.csv` | human, adult · 🔴 **REGION only, bulk, NOT subfield-resolved** | `purkinje_cerebellar_celltype_wwox_census_20260922.md:292`, `:319-338` | 🟢 Local CSV held; the entry question was closed in favour of the hemisphere entry |
| **HBT** (Human Brain Transcriptome): WWOX mRNA conception→adult across NCX, HIP, AMY, STR, MD, CBC; cerebellar cortex shows a distinct larger early-postnatal rise | human · 🔴 **REGION only** | `wwox_postnatal_svz_expression_20260922.md:104`, `:137`-ff | 🔴 Restatement |
| **Tochigi 2019 rat IHC** (`PMID 31340538`, `lde` colony background): at PND21 Wwox immunoreactivity **co-localises with NeuN, APC(CC1) and GFAP** in representative images and is **not detected in Iba1⁺ microglia**; 🔴 *"There is no quantitative colocalisation analysis; the defensible wording is 'not detected by this assay', not universal absence of microglial expression"* | **rat**, PND21, cortex/callosum · 🟡 broad classes | `research/fulltext_dossiers/PMID31340538.md:56-58`; `research/discovery_ledger_current.md:608-620` (`DL-MECH-027`) | 🟢 **Full text read by LEGEND**, dossier + ledger |
| **Human WWOX IHC across normal tissues** (`PMID 16941225`): *"neurons, ependymal cells and astrocytes"*; *"robust WWOX protein expression in soma from cells of all three [cerebellar] layers"* | human, age not stated · 🟡 layer, qualitative | `wwox_postnatal_svz_expression_20260922.md:120`; `purkinje_cerebellar_celltype_wwox_census_20260922.md:287` | 🟡 **abstract depth + review restatement; the primary body is LICENCE-BLOCKED**, third confirmation |
| **HPA, DropViz, mousebrain.org, Allen API all unreachable** from this deployment — *"the control itself fails, so general egress is closed"* (`example.com` → HTTP 000) | — | `purkinje_cerebellar_celltype_wwox_census_20260922.md:118-127`; `wwox_postnatal_svz_expression_20260922.md:108` | 🟢 Read directly this act |
| **`P6` already SUPPORTED**: no WWOX paper reports subfield-resolved hippocampal `Wwox` expression; `Wwox expression hippocampus CA1 dentate gyrus in situ hybridization` → **0 PubMed records** | — | `new_discovery_node_20260922.md:255` | 🟢 Read directly this act |

### 1.2 🎯 What the baseline therefore leaves genuinely open — and it is exactly my task

1. 🔴 **No hippocampal-subfield-resolved `Wwox` datum exists anywhere in this repository, from any source,
   WWOX-specific or atlas.** The finest hippocampal resolution held is the word *"hippocampus"* (GTEx 5.6 TPM,
   HBT `HIP`). `P7` is genuinely unscored and I am not re-treading held ground.
2. 🔴 **Every atlas row the repository holds is a restatement of a 2020 review, not a query of the atlas.**
   `purkinje_cerebellar_celltype_wwox_census_20260922.md:722-723` sets an explicit `REVIVAL_TRIGGER` for
   *"any actor with egress"* to read these surfaces directly. That trigger is what this act tries to fire.
3. 🟡 **The cell-type list held is a list, not a ranking.** Tochigi gives co-localisation with three cell
   classes and non-detection in a fourth, **with no quantitation**; BrainRNAseq is restated as *"uniform"*
   with no numbers. **No ordered, numeric, cell-type-resolved table of `Wwox` expression exists in this
   repository.** Part B is therefore open, and is the rival-test the brief says it is.
4. ⚠️ **What I did NOT redo:** the cerebellar Purkinje census (done, 930 lines), the SVZ/germinal-zone
   question (done, and negative), the GTEx entry question (closed), the myelin/oligodendrocyte census (done),
   and `P1`–`P6` (all scored). I re-score none of them.

---

## 2 · PREREGISTERED EXPECTATION FOR PART B

> 🔴 **§ 2 was written to disk in full BEFORE a single Part B query was run**, with §§ 3–9 absent from the
> file. Nothing in § 2 was edited afterwards. Being wrong is acceptable; retrofitting is not.
> ⚠️ **And I must declare a handicap against myself: this is NOT a blind prediction.** § 1.1 already holds
> BrainRNAseq *"uniform … in neurons and all glial cell types"* and Tochigi's neurons/astrocytes/
> oligodendrocytes-but-not-microglia. So the broad shape below is **substantially retrodiction from held
> baseline, and deserves almost no credit if it is confirmed.** The parts that are genuinely at risk are
> marked 🎯, and those are the only ones I will claim anything from.

**My ex-ante expectation, ranked, for wild-type rodent/human `Wwox` by cell type:**

| Rank | Cell type | Expected level | Genuinely at risk? |
|---|---|---|---|
| 1 | **Oligodendrocyte progenitor cells (OPC)** | highest or near-highest | 🟡 partly — baseline says progenitors > mature, but only within the lineage, not against all other types |
| 2 | **Excitatory / pyramidal neurons** | high | 🔴 no — retrodiction |
| 3 | **Inhibitory interneurons** | high, **comparable to or above pyramidal** | 🎯 **YES.** DropViz put `Pvalb`⁺ basket cells *above* granule cells in cerebellum. I predict interneurons are **not** below excitatory neurons |
| 4 | **Dentate granule cells** | high, **within ~2× of CA1 pyramidal neurons** | 🎯 **YES — this is the `P7`-bearing prediction** |
| 5 | **Cerebellar granule cells** | moderate-to-high | 🟡 partly |
| 6 | **Astrocytes** | moderate — **present, clearly non-zero, but below neurons** | 🎯 **YES.** This is the prediction that tests the Part C DATO line |
| 7 | **Cerebellar Purkinje cells** | 🔴 **I decline to predict.** The repository's own census says no dataset reports them in either direction | ⚪ declined |
| 8 | **Mature myelinating oligodendrocytes** | moderate, **below OPC** | 🔴 no — retrodiction |
| 9 | **Microglia** | **lowest of all types, but I predict NON-ZERO** | 🎯 **YES.** Tochigi's *"not detected"* is an IHC floor, not an absence; I predict a transcript atlas shows microglial `Wwox` measurably above zero and lowest of the set |

**And the three summary expectations I will be scored against:**

- 🎯 **B-E1.** **The dynamic range across all neural cell types will be narrow — I predict under ~5-fold
  between the highest and lowest neural cell type, excluding microglia.** If it is narrow, the
  "vulnerability simply tracks baseline WWOX expression" rival **cannot** explain a lesion that is present in
  one subfield and absent in its neighbour, because there is no gradient large enough to carry it.
- 🎯 **B-E2.** **Astrocytes and oligodendrocyte-lineage cells will not be trace-level.** I expect glial
  expression within the same order of magnitude as neuronal.
- 🎯 **B-E3.** **The expression-level rival will therefore be WEAKENED, not supported**, and a metabolic or
  lesion-mechanism explanation of differential vulnerability will remain necessary. 🔴 **This is the outcome
  that suits my own § 3/§ 4 conclusion, so it is the one I must be most suspicious of, and § 7 states what
  would have falsified it.**

**And for `P7` itself I restate the original author's prediction unchanged and do not soften it:** SUPPORTED
if wild-type hippocampal `Wwox` is broad/flat or DG-enriched; **REFUTED if CA1-enriched**.

---

## 0.2 · READ DEPTH — the completed table

| # | Source | Depth **in this act** | Basis / exact failure mode |
|---|---|---|---|
| S1 | **`PMID 31340538` / `PMC6678113`** — Tochigi 2019, *Int J Mol Sci*, the `lde` colony cortical paper | 🟢 **READ DIRECTLY, full body, end to end** | Retrieved via the PubMed MCP route. [DOI](https://doi.org/10.3390/ijms20143596). 🔴 **A sibling also read this body first-hand earlier today** (`lde_myelin_vacuole_bridge_20260922.md:392-395`); my read is an **independent re-derivation**, not a first retrieval, and I claim no priority for the retrieval |
| S2 | **`PMID 33255508` / `PMC7727818`** — Aldaz & Hussain 2020, *Int J Mol Sci* review | 🟢 **READ DIRECTLY, full body** | PubMed MCP. [DOI](https://doi.org/10.3390/ijms21238922). This is the source of the repository's Allen/DropViz/BrainRNAseq/HBT/GTEx rows; reading it directly **upgrades those rows from restatement-of-a-restatement to restatement-read-first-hand** — 🔴 it does **not** make them atlas queries |
| S3 | **`PMID 34831305` / `PMC8623516`** — Steinberg & Aqeilan 2021, *Cells* review | 🟢 **READ DIRECTLY** (targeted extraction of every expression-bearing passage) | PubMed MCP. [DOI](https://doi.org/10.3390/cells10113082) |
| S4 | **`PMID 36247526` / `PMC9561749`** — *The transcriptome of rat hippocampal subfields*, LCM + RNA-seq of rat CA1/CA2/CA3/DG | 🟢 **READ DIRECTLY, full body** | PubMed MCP. [DOI](https://doi.org/10.1016/j.ibneur.2022.09.009). 🔴 **The served text has every gene symbol silently deleted** (the italics-stripping extraction defect this repository already documents), e.g. *"we have identified the gene(peroxisomal biogenesis factor 5-like)"*, **and the GEO accession is stripped too**. So the one perfectly-species-matched subfield dataset in existence was located but **its values could not be reached** |
| S5 | **Allen Mouse Brain Atlas API** (`api.brain-map.org`) | ⚫ **SOURCE_BLOCKED** | `EGRESS_BLOCKED` by the network egress proxy, tested once. **No retry** |
| S6 | **Human Protein Atlas** (`www.proteinatlas.org/ENSG00000186153-WWOX/brain`) | ⚫ **SOURCE_BLOCKED** | `EGRESS_BLOCKED`, tested **once**, as instructed. 🟢 **This independently reproduces the block recorded in `purkinje_cerebellar_celltype_wwox_census_20260922.md:529-532` and `wwox_postnatal_svz_expression_20260922.md:108`** — a fourth confirmation. Recorded as a fact, not retried |
| S7 | **Hipposeq** (`hipposeq.janelia.org`) — 🎯 *the* resource that would settle `P7` numerically | ⚫ **SOURCE_BLOCKED** | `EGRESS_BLOCKED`, tested once. **This is the single most consequential block in this act** and § 7 states exactly what it costs |
| S8 | **GTEx portal API**, **BrainRNAseq**, **Allen celltypes**, **EBI Expression Atlas**, **Ensembl REST** | ⚫ **SOURCE_BLOCKED** | All HTTP `000` / gateway `403` on CONNECT, one probe each. Proxy status confirms `connect_rejected … policy denial` for `ncbi`, `ebi`, `europepmc`, `crossref`, `openalex` |
| S9 | **Abudiab et al. 2025**, bioRxiv `10.1101/2025.11.22.689900`, *"WWOX deficiency uncovers a cell-autonomous mechanism impairing myelin repair"* | 🟡 **SEARCH-SYNTHESIS DEPTH ONLY — WEAKER THAN AN ABSTRACT** | 🔴 `biorxiv.org` `EGRESS_BLOCKED`; `api.biorxiv.org` gateway `403`; **no PMID exists** (PubMed returns 0 records for the cell-autonomous/oligodendrocyte query). What I have is a **search engine's prose synthesis of the preprint**, not a quoted abstract and not a body. 🔴 **It is used in this file as a FLAG ONLY and overturns nothing.** It is already this repository's `FT-007`, logged as never retrieved (`full_text_queue_current.md:106-107`, `:2966`) |
| S10 | The repository baseline of § 1 | 🟢 read directly this act | Files and lines given inline throughout |
| S11 | `PMID 19500159`, `PMID 17803050` (the two vacuolation primaries) | 🔴 **NOT FETCHED — SIBLING-ATTESTED only where used** | Both are recorded by this repository as unretrievable through open channels. I did not re-attempt them; `P7` does not require them |
| S12 | 🎯 **`learning/scientist/PILOT_PMID33914858_FULLTEXT_DEEPDIVE_SCIC_v1.md`** — actor `lettore-c`, an **810-line** experiment-by-experiment reconstruction of `PMID 33914858` with **30 verbatim locators** | 🔴 **SIBLING-ATTESTED — read directly by me this act, at the ARTEFACT level** | 🔴 **ADDED IN REVISION.** I read this file directly, with repo file and line for every use. 🔴 **I have NOT read the `PMID 33914858` PDF** — `files/` is gitignored and absent from this worktree. Every `Lnn` locator below is the pilot's transcription of a body I have never seen, and is labelled at every single use |

> 🔴 **Declared plainly: I queried ZERO expression atlases directly. Every atlas statement in this file
> reaches me through a published review that describes the atlas, or through a primary IHC paper.** That is a
> real and severe limit on § 3 and § 5, and § 7 does not soften it.

---

## 3 · `P7` SCORED

**`P7` as preregistered, restated without improvement:**
> *"`Wwox` expression in the wild-type hippocampus will NOT show a clean CA1 ≫ DG/CA3 gradient. I expect a
> broadly distributed neuronal expression, which would weaken `H3`, and leave the explanation with the lesion
> mechanism rather than with the baseline. SUPPORTED if expression is broad/flat or DG-enriched; REFUTED if
> CA1-enriched."*

### 3.1 The evidence, by resource, with its resolution limit stated in the same row

| # | Resource · species · age | What it actually says about hippocampal `Wwox` | 🔴 Resolution limit |
|---|---|---|---|
| **E-a** | 🎯 **Rat IHC, PND21, `+/+` and `+/lde`** — Tochigi 2019, S1, 🟢 read directly. **The `lde` colony itself: same species, same strain, same laboratory as the vacuoles** | **Verbatim, Results § 2.1:** *"Immunohistochemical analysis showed that Wwox protein was widely expressed in the forebrain (C–I), especially in layers II-III and V of the cerebral cortex, as well as the white matter (D), corpus callosum (CC) (E), **hilus in the hippocampus** (F), habenular nuclei (HN), thalamus (G), hypothalamus (H), and internal capsule (IC) (I)."* 🎯 **The ONLY hippocampal sub-structure singled out in the entire corpus is the HILUS — a dentate-gyrus substructure. `CA1` is not named.** And the Discussion adds: *"Immunostaining detected Wwox protein in the soma of neurons located in the cerebral cortex, hippocampus, thalamus, and hypothalamus, **as well as in brain regions containing abundant myelin sheath, such as the CC, white matter, and internal capsule**"* | 🔴 **Qualitative IHC.** *"Especially"* is an author's visual emphasis, not a measurement. **No subfield densitometry, no CA1/CA3/DG comparison, no denominator.** 🔴 And `NOT NAMED ≠ ABSENT` — `PREMISE: DETECTION_FLOOR`, already held by this repository as `CC-20260920-DETECTION-FLOOR-01`. 🔴 I did **not** inspect the figure panel |
| **E-b** | **Allen Mouse Brain Atlas ISH**, mouse adult — via S2, 🟢 read first-hand *as a review's description* | *"ISH probes significantly light up a region of hippocampal formation, specifically **layer 2 of the medial entorhinal cortex (ENTm2** …) and also the anterior (BLAa) and posterior (BLAp) regions of the basolateral amigdalar nucleus"*; to *"a much lesser extent"* isocortex L5, and *"clearly visible in cerebellum cortex"* | 🔴 **CA1, CA3 and DG are named NOWHERE**, in either direction, by authors whose explicit purpose was to identify the highest-expressing regions. 🔴 **This is an argument from a review's silence about a resource I could not query** (S5 blocked). It is suggestive, not decisive |
| **E-c** | 🎯 **DropViz scRNA-seq**, mouse adult — via S2, 🟢 read first-hand as a review's description. **The only cell-type-resolved hippocampal datum that exists** | *"markers **Lhx1, Nxph3, and Gad2** identify the neuronal clusters expressing the most [`Wwox`] in hippocampus … Further dissection by subclustering highlights **very specifically neurons from the medial entorhinal cortex (identified by Slc17a7 and Reln markers) as those cells expressing, by far, the highest number of transcripts in hippocampal formation.**"* 🎯 **The top `Wwox`-expressing population in the hippocampal formation is an entorhinal population, NOT CA1 pyramidal cells.** ⚠️ **NEW TO THIS REPOSITORY** — a grep confirms `Lhx1`, `Nxph3` and `Slc17a7` appear in no `disease-models/wwox/` file | 🔴 **A ranking, not a table.** *"By far the highest"* fixes the top; it gives **no value for CA1, CA3 or DG** and therefore cannot order them against each other. 🔴 Mouse, adult, transcript — three steps from rat, PND21–28, protein |
| **E-d** | **BrainRNAseq cell-type RNA-seq**, mouse **P7** — via S2, 🟢 read first-hand as a review's description | *"At P7, **uniform expression** of [`Wwox`] is detected in neurons and all glial cell types"* | 🔴 **Cell CLASS, not subfield.** Says nothing about CA1 vs DG. Single time point. *"Uniform"* is the review's word for a figure I have not seen |
| **E-e** | **GTEx**, human adult bulk — S2 + the **local** CSV `analysis/data/WWOX_tissue_expression_GTEx.csv`, 🟢 read directly | `Brain_Hippocampus` = **5.585 TPM**; cerebellum 12.1; frontal cortex 6.9; amygdala 6.2 | 🔴 **NOT SUBFIELD-RESOLVED, AND SAYS SO.** GTEx dissects *"hippocampus"* as one block. It cannot address `P7` at all and is recorded only to close the route |
| **E-f** | 🎯 **`PMID 36247526`** — rat LCM RNA-seq of CA1/CA2/CA3/DG, S4, 🟢 read directly. **Wistar rat, 3 months, n=4, the correct species and the correct resolution** | 🔴 **NOTHING.** The one dataset in existence that could answer `P7` numerically **in the right species** exists, is published, and **its per-gene values did not reach me**: the served full text has every gene symbol stripped and the GEO accession stripped with them | ⚫ **The decisive near-miss of this act.** The data exist and are public; this deployment cannot read them |

### 3.2 🔴 The adversarial pass on my own score, run before the score is written

I owe `H3` its best case, so I state the three ways this could be wrong:

1. 🔴 **Not one source measured CA1 against CA3 against DG.** Every row above is either a *ranking of tops* (E-b, E-c), a *cell-class uniformity claim* (E-d), a *qualitative "especially" list* (E-a), or *not subfield-resolved at all* (E-e). **A gene can fail to be the regional top and still be CA1-enriched relative to DG and CA3.** That possibility is untouched by anything I found.
2. 🔴 **E-a's hilus is not the dentate granule layer.** The hilus is the polymorphic layer — mossy cells and interneurons, not granule cells. *"DG-enriched"* is therefore **not** the right description of E-a and I will not use it. The defensible wording is **"the only hippocampal sub-structure named is on the dentate side, and CA1 is not named."**
3. 🔴 **Protein, transcript, species and age are all mismatched across the rows.** E-a is rat protein at PND21; E-c is mouse transcript in adult; E-d is mouse transcript at P7. This corpus's own record is that WWOX mRNA and protein dissociate. **Pooling them would be exactly the error this laboratory forbids, so I do not pool them — I report their agreement in DIRECTION only.**

### 3.3 🎯 THE SCORE

> ## `P7` = 🟢 **SUPPORTED** — on the "broad/flat" branch, not the "DG-enriched" branch.

**Four independent resources, in two species, at two molecular levels, and NOT ONE of them shows CA1
enrichment.** The single in-species protein map names the **hilus** and does not name CA1. The single
cell-type-resolved hippocampal dataset puts the top population *"by far"* in the **medial entorhinal cortex**.
The single cell-class dataset says **uniform**. The preregistered `REFUTED` condition — *"REFUTED if
CA1-enriched"* — **is met by no source whatsoever.**

**🔴 And the part that stays open, named exactly as the brief requires.** `P7` had two halves, and only one is
closed:

| Half of `P7` | Status |
|---|---|
| *"will NOT show a **clean CA1 ≫ DG/CA3 gradient**"* — i.e. is CA1 the standout? | 🟢 **CLOSED, SUPPORTED.** No resource makes CA1 a standout; two actively rank a non-CA1 population above everything in the hippocampal formation |
| *"broadly distributed"* — i.e. **what IS the numeric CA1 : CA3 : DG ratio?** | 🔴 **STILL OPEN, AND I CANNOT CLOSE IT.** **No number for any hippocampal subfield exists in anything I reached.** The two resources that hold it — **Hipposeq** (S7, `EGRESS_BLOCKED`) and the **GEO deposit of `PMID 36247526`** (S4, accession stripped from the served text) — are both public and both unreachable from this deployment |

⇒ **`P7` is SUPPORTED as a refutation of CA1-enrichment. It is NOT established as a positive measurement of
flatness.** Those are different claims and I am scoring only the first.

---

## 4 · VERDICT ON `H3`

> **`H3` as preregistered by the sibling:** *"Cell-autonomous subfield expression gradient — CA1 pyramidal and
> amygdalar neurons simply express `Wwox` more than DG granule/CA3 cells, so the null bites hardest there."*
> Its own stated falsifier: *"`H3` requires CA1 ≫ DG/CA3. A flat or inverted gradient kills it and touches
> nothing else."*

> ## 🔴 `H3` = **SEVERELY WEAKENED — and it SPLITS. Not killed.**

`H3` made **two** claims welded into one row, and the atlas evidence separates them and sends them opposite
ways. Nobody has noticed this because nobody had the expression map next to the lesion map.

### 4.1 The CA1 half — 🔴 fails, and fails in the strongest available species

`H3` needs CA1 ≫ DG/CA3. **The rat's own map names the hilus and not CA1** (E-a), and it does so **in the
paper written by the same group that reported the CA1 vacuoles** — that paper's own Introduction states
*"Pathological analysis of `lde` rat brains at **PND 28** revealed many extracellular vacuoles in the **CA1
region of the lateral hippocampus** and amygdala"* (🟢 read directly this act, S1, Introduction; note this
**upgrades to a direct read** an observation previously held only as 🔴 SIBLING-ATTESTED `O3`). 🎯 **So in a
single paper, one figure names the hilus as an expression site and the Introduction names CA1 as the lesion
site, and the two do not coincide.** `H3`'s CA1 half predicted exactly the opposite.

### 4.2 🔴 The amygdala half — **it SURVIVES, and this cuts against my own conclusion**

**I am obliged to report this because it damages my verdict.** The basolateral amygdala — `BLAa` and `BLAp` —
is, per Allen ISH (E-b), one of only **two** regions in the entire mouse brain singled out as significantly
lighting up for `Wwox`. **And the amygdala is the second of the two territories that vacuolate in `lde/lde`**
(6 of 9 affected animals, `new_discovery_node_20260922.md:107`). **For the amygdala, high expression and
lesion DO coincide, exactly as `H3` predicts.** `H3` is therefore not a uniformly failed hypothesis; it is a
hypothesis that is **right about one of its two territories and wrong about the other** — and no file in this
repository had noticed either half.

### 4.3 🎯 The stroke that does the real damage, and it is not about the hippocampus at all

**The highest-expressing region of the hippocampal formation is `ENTm2`, medial entorhinal cortex layer 2
(E-b and E-c agreeing across two independent atlases and two molecular levels). No WWOX model has ever
been reported to vacuolate in the entorhinal cortex.** If baseline expression set vulnerability, `ENTm2`
should be the first structure to fail, and it is not reported as failing at all.

🔴 **Stated against myself:** this is an argument from absence, and the absence is weak — the 2007 and 2009
reports took the hippocampus and amygdala as their object, and **nobody looked at the entorhinal cortex**.
`NOT REPORTED ≠ SPARED`. I do not treat this as a refutation; I record it as the **most valuable open
measurement this whole line generates** (§ 5.3).

### 4.4 What this changes in the sibling's ranking

| Before (`new_discovery_node_20260922.md:220`) | After this act |
|---|---|
| `H0` ≳ `H5` > `H2` > **`H3`** > `H4` > `H1` > `H6` | `H0` ≳ `H5` > `H2` > `H4` > **`H3`ᴬᴹʸ** > `H1` > `H6` > **`H3`ᶜᴬ¹** |

🔴 **And `E5` did NOT do what § 7 of the sibling node promised it could.** That section claimed `E5` *"is the
only component that can kill `H3` without tissue"*. **It cannot, and I will not claim it did.** `E5` as
executed rules out the *gradient direction* `H3` requires; it cannot rule out a modest CA1 > DG difference,
because **no resource reachable here reports subfield values at all**. The tissue experiment `E1` remains
necessary. 🎯 **The honest upgrade is that `E1` should now carry an entorhinal-cortex sampling box** — a
change that costs nothing and tests § 4.3.

---

## 5 · PART B — CELL-TYPE-RESOLVED WILD-TYPE `Wwox`, AND THE RIVAL IT WAS MEANT TO TEST

### 5.1 The table — every cell type the brief named, with the model each statement was measured in

🔴 **Read the "Level" column as ORDINAL AND PARTIAL. There is not one number in it, anywhere, for any cell
type, in any source I reached.** That is the finding, not a formatting failure — see § 5.2.

| Cell type | Level, as reported | Model · age · molecule | Source · depth |
|---|---|---|---|
| **Excitatory / pyramidal neurons** | 🟢 **HIGH.** *"a high degree of colocalization of NeuN and Wwox in the cytoplasm of **pyramidal neurons located at layers II-III and V** of the cerebral cortex"*; and *"the **high level of Wwox protein in pyramidal neurons** in [`+/+`] cerebral cortices"* | **rat**, PND21, **protein** | S1 🟢 direct |
| ″ | 🟢 **HIGHEST IN ISOCORTEX.** *"deep-layer pyramidal neurons, specifically **from Layer 5**, show the highest levels of [`Wwox`] expression"*; Allen ISH agrees on isocortex L5 | **mouse**, adult, **transcript** | S2 🟢 direct (review of DropViz + Allen) |
| **Inhibitory interneurons** | 🟢 **HIGH — at or above excitatory, where both were ranked.** In cerebellum the top clusters are *"interneurons (`Pvalb`+ cells)"*, and on subclustering *"specifically **GABAergic basket cells** … are the top cell types"*. In hippocampus **`Gad2`** is one of the three markers identifying the top-expressing clusters | **mouse**, adult, **transcript** | S2 🟢 direct |
| **Dentate granule cells** | 🔴 **NOT REPORTED, IN EITHER DIRECTION, ANYWHERE.** The rat map names the **hilus**, which is the polymorphic layer and **not** the granule layer | — | 🔴 absent from the entire corpus |
| **CA1 / CA3 pyramidal cells** | 🔴 **NOT REPORTED, IN EITHER DIRECTION, ANYWHERE** | — | 🔴 absent from the entire corpus |
| **Medial entorhinal cortex L2 neurons** *(not on the brief's list; added because it is the answer)* | 🎯 **HIGHEST in the whole hippocampal formation, "by far"** (`Slc17a7`+/`Reln`+), concordant with Allen ISH `ENTm2` | **mouse**, adult, **transcript** + ISH | S2 🟢 direct |
| **Cerebellar granule cells** | 🟢 **HIGH — second to basket cells.** `Gabra6`+ granule cells among top cerebellar clusters; *"to lesser extent, granular neurons"* | **mouse**, adult, **transcript** | S2 🟢 direct |
| **Cerebellar Purkinje cells** | 🔴 **NOT REPORTED, IN EITHER DIRECTION.** 🔴 **ALREADY-HELD AND NOT REDONE** — `purkinje_cerebellar_celltype_wwox_census_20260922.md` is 930 lines on exactly this and I add nothing | — | already held |
| **Oligodendrocyte progenitors (OPC)** | 🟢 **HIGHEST WITHIN THE LINEAGE.** *"Within the oligodendrocyte population, the highest [`Wwox`] expression levels are observed in **progenitor** oligodendrocytes, with **significantly lower** levels in mature myelinated oligodendrocytes"* | **mouse**, P7, **transcript** | S2 🟢 direct |
| ″ | 🟡 corroborated at the weakest tier: *"WWOX is expressed the highest in OPCs followed by newly formed and mature oligodendrocytes"* | mouse/human | **S9 🟡 SEARCH-SYNTHESIS ONLY — a flag, not evidence** |
| **Mature myelinating oligodendrocytes** | 🟢 **PRESENT AND WIDESPREAD, but below OPC.** *"Wwox protein was also detected in the cytoplasm of **most APC-positive oligodendrocytes** in the CC … and in other regions throughout the forebrain"* — and the authors flag it as a **correction to the prior literature**: *"Although previous immunohistochemistry found that Wwox protein was present in neurons and astrocytes **but not in oligodendrocytes**, our double immunofluorescence … clearly showed that Wwox protein **was** present in oligodendrocytes. **To our knowledge, this study is the first to show that Wwox is expressed in oligodendrocytes.**"* | **rat**, PND21, **protein** | S1 🟢 direct |
| **Astrocytes** | 🟢 **PRESENT, with a DISTINCT subcellular pattern.** *"Wwox protein showed a **dot-like condensed localization** in the cytoplasm of GFAP-positive astrocytes located in layer V … observed in **both gray and white matter**"*, and *"differed from the cytoplasmic diffuse distribution of Wwox in neurons and oligodendrocytes"* | **rat**, PND21, **protein** | S1 🟢 direct |
| **Microglia** | 🔴 **CONTRADICTED BETWEEN SOURCES — see § 5.4** | — | S1 vs S2, both 🟢 direct |
| **All neurons + all glia together** | 🟢 **UNIFORM.** *"At P7, **uniform expression** of [`Wwox`] is detected in neurons and **all glial cell types**"* | **mouse**, P7, **transcript** | S2 🟢 direct |
| **Ependymal + choroid plexus cells** | 🟢 present, *"significant number of [`Wwox`] transcripts"* — 🔴 but *"(data not shown)"* | mouse, adult | S2 🟢 direct |

### 5.2 🔴 Scoring my own § 2 preregistration — including the ones I cannot score

| Preregistered | Outcome |
|---|---|
| OPC highest | 🟡 **PARTIAL.** Highest *within the oligodendrocyte lineage*. **Never ranked against neurons anywhere** |
| Excitatory neurons high | 🟢 SUPPORTED — 🔴 and this was **retrodiction**, worth nothing, as § 2 warned |
| 🎯 **Interneurons not below excitatory** | 🟢 **SUPPORTED**, and this one was at risk: basket cells are the *top* cerebellar type, above granule cells, and `Gad2` marks a top hippocampal cluster |
| 🎯 **DG granule within ~2× of CA1** | ⚪ **UNSCORABLE. Neither value exists.** I was wrong to think this was scoreable without Hipposeq |
| Cerebellar granule moderate-high | 🟢 SUPPORTED |
| 🎯 **Astrocytes present but below neurons** | 🟡 **HALF-SCORED, and the half I can score went against me.** *Present*: 🟢 confirmed. *Below neurons*: ⚪ unscorable — and the one cell-class dataset says **uniform**, i.e. **not** below. My directional guess is unsupported |
| Purkinje — declined | ⚪ correctly declined; still unreported |
| Mature OL below OPC | 🟢 SUPPORTED (retrodiction) |
| 🎯 **Microglia lowest but NON-ZERO** | 🔴 **SPLIT AND UNRESOLVED — § 5.4.** Transcript: supported. Protein: refuted. I will not pick the one that suits me |
| 🎯 **B-E1 — dynamic range under ~5×** | ⚪ **UNSCORABLE, AND THIS IS THE REAL RESULT OF PART B.** See § 5.3 |
| 🎯 **B-E2 — glia not trace-level** | 🟢 **SUPPORTED**, on the strongest wording available: *"uniform … in neurons and all glial cell types"* |
| 🎯 **B-E3 — the expression rival is weakened** | 🟢 **SUPPORTED, but NOT by the route I expected** — § 5.3 |

### 5.3 🎯 WHAT THIS DOES TO THE EXPRESSION-LEVEL RIVAL FOR DIFFERENTIAL VULNERABILITY

**The rival, stated at full strength so it can be beaten honestly:** *if the cell types that degenerate in
WWOX loss are simply the ones that expressed the most WWOX to begin with, then differential vulnerability is
explained by the baseline and no metabolic — or any other — mechanism is needed.* **A metabolic hypothesis
must beat this rival before it is worth anything.** So: does the vulnerability ranking track the expression
ranking?

| Cell type / region | Wild-type `Wwox` | Outcome in a WWOX model | Track? |
|---|---|---|---|
| Cerebellar basket cells + granule cells | 🟢 **top** | ataxia is syndromic across models | ✅ |
| Basolateral amygdala | 🟢 **top (Allen)** | 🟢 **vacuolates, `lde/lde`** | ✅ |
| Hippocampal interneurons | 🟢 high (`Gad2` cluster) | 🟢 PV/NPY interneurons **reduced**, `Wwox`-null mouse | ✅ |
| 🔴 **OPC → mature oligodendrocyte** *(row REVISED — see below)* | 🟢 **OPC highest in lineage** | 🟢 maturation fails in the **whole-body** `lde/lde` and in **neuron-specific** S-KO; 🔴 **but deleting `Wwox` in oligodendrocytes ALONE does nothing** — `L02`, `L18` | 🔴 **CONFOUNDED → ❌** |
| 🔴 **Medial entorhinal cortex L2** | 🎯 **HIGHEST in the hippocampal formation** | 🔴 **no lesion reported in any model** | ❌ *(weak — never examined)* |
| 🔴 **CA1 pyramidal** | 🔴 **not named as high; the rat map names the hilus instead** | 🟢 **vacuolates, 9/9, `lde/lde`** | ❌ |
| 🎯🔴 **Cerebral cortex layer V pyramidal neurons** | 🎯 **HIGHEST cell type in the isocortex** — Allen ISH, DropViz, **and** *"high level of Wwox protein in pyramidal neurons"* by IHC in the rat itself | 🎯 **SPARED, AND MEASURED AS SPARED**: *"no significant difference of neuron number"*, *"no significant difference … in the thickness of cerebral cortices at all ages"*, *"[no difference] in neuron number in each cortical layer at PND21"* | ❌❌ |

> ### 🎯 THE DECISIVE ROW IS THE LAST ONE, AND IT IS NOT AN ARGUMENT FROM ABSENCE.
> In the **`lde/lde` cerebral cortex**, the cell type carrying the **highest** `Wwox` expression in the
> isocortex — the layer V pyramidal neuron — is **quantified, at four postnatal ages, and found normal in
> number, in cortical thickness and in layer distribution.** In the **same animals, in the same paper**, the
> **oligodendrocyte lineage** — which is *not* the top expresser, and whose *mature* members express
> **significantly less** than their own progenitors — is the compartment that **fails**.
>
> 🔴 **The highest-expressing cell type is the spared one, and a lower-expressing lineage is the lost one, in
> one animal, one paper, one set of measurements.** Nothing here rests on "nobody looked".

> 🔴 **REVISED: the oligodendrocyte row was the rival's best row and it does not survive `L02`.** I had
> scored it ✅ because the lineage that expresses most (OPC) is the lineage that fails. **But the failure is
> not caused by that lineage's own `Wwox`**: an Olig2-Cre oligodendrocyte-specific deletion produces *"no
> phenotype abnormalities"* and no MBP change (🔴 SIBLING-ATTESTED, `L02`/`L18`, S12:472, :488). In the
> whole-body null the lineage's high expression and its failure **co-occur without one causing the other** —
> a textbook confound. ⇒ **the row is de-confounded AGAINST the rival, and the rival loses its strongest
> case.** 🔴 **Note the discipline: this row moves on a REQUIREMENT result, and it moves the row's CAUSAL
> reading only. It does not change any expression value, and § 6.2 Finding 4 keeps the two axes apart.**

⇒ **VERDICT ON THE RIVAL: 🔴 the expression-level rival is REFUTED as a *general* explanation of differential
vulnerability, and survives only as a *partial* correlate.** It gets the amygdala, the interneurons and the
cerebellum right — **3 of 7 rows, revised down from 4** — it gets the two rows that were actually *measured
against it* wrong, and its fourth row turns out to be a confound rather than a hit. **A hypothesis that explains why cortical layer V neurons survive while
oligodendrocytes fail is therefore still required, and Part B does not supply one.** It only clears the
ground — which is exactly what the brief asked it to do, and 🔴 **I record that clearing the ground is not
the same as having a metabolic hypothesis, and this file proposes none.**

🔴 **The unfalsifiable version must be named before it regrows.** "Expression tracks vulnerability" can be
rescued by asserting an unmeasured *dependence* rather than a *level* — that layer V neurons express much
`Wwox` but do not *need* it. **That version is not the rival I tested, it predicts nothing I could measure,
and it must not be allowed to inherit the tested version's credibility.**

### 5.4 🔴 AN UNREGISTERED CONTRADICTION THIS ACT EXPOSES — microglia

Two sources this repository relies on, **both read directly by me today, disagree flatly**:

| Source | Says |
|---|---|
| **S1**, rat PND21, **protein/IHC** 🟢 | *"**Iba1-positive microglia** in the cerebral cortex and CC **were not immunostained** with antibody to Wwox"*; and the Discussion builds on it: *"The **lack of Wwox expression in microglia** suggests that the decrease of microglia in `lde` rats is a **secondary** phenomenon"* |
| **S2**, mouse, **transcript/RNA-seq** 🟢 | *"[`Wwox`] expression remains **stable throughout life in microglial cells**"*, and *"**substantial upregulation** of [`Wwox`] expression can be observed in microglial cells upon treatment of mice with **lipopolysaccharide (LPS)**"* — i.e. microglial `Wwox` is not merely present but **regulated** |

🔴 **This is not a nuance. `DL-MECH-027`'s inference that the microglial decline in `lde/lde` is *secondary*
rests on the premise of microglial non-expression** — and that premise is contradicted by a transcript
dataset in another species. The repository's own dossier already hedged the IHC correctly
(*"the defensible wording is 'not detected by this assay', not universal absence"*,
`PMID31340538.md:56-58`), **but the hedge did not propagate to the inference that depends on it.**
`PREMISE: DEFAULT_FROM_TEXTBOOK` → 🔴 **`IHC non-detection = non-expression` is a DEFAULT, not a foundation,
and it is load-bearing here.** `REVIVAL_TRIGGER`: any microglial `Wwox` transcript value, or any WWOX
antibody validated on microglia, reopens the secondary/primary status of the microglial phenotype.
⚠️ Species and modality both differ, so this is a **registered tension, not a refutation**, and I resolve it
in neither direction.

---

## 6 · PART C — THE ADVERSARIAL CHECK ON *"WWOX IS PREFERENTIALLY EXPRESSED IN NEURONS"*

**The line under audit**, `disease-models/wwox/meta/meta_network_myelin_glia_current.md:38`, under
**Core Findings (DATO)**, 🟢 read directly this act:

> *"WWOX is preferentially expressed in neurons; neuron-specific deletion is sufficient to replicate the null
> phenotype (Brain 2021)"*

**The line it was set against**, `research/discovery_ledger_current.md:608-620`, `DL-MECH-027`, 🟢 read
directly this act:

> *"**Wwox è espresso in neuroni, astrociti e oligodendrociti, ma NON in microglia** (primo report su
> oligodendrociti)"*

### 6.1 First, the question as the brief posed it — and the brief's framing is not where the defect is

**Are they compatible?** 🟢 **YES. `preferential ≠ exclusive`, and on that axis the two lines do not
conflict at all.** A gene can be expressed in four cell classes and still be expressed *most* in one of them.
🔴 **`DL-MECH-027` does not contradict the DATO line, and I will not manufacture a conflict that is not
there.** **The defect is somewhere else, and it is worse.**

### 6.2 🔴 THE LINE IS OVER-STATED. Four findings, stated without softening — one of them against myself.

**FINDING 1 — 🔴 "preferentially" has NO measurement behind it anywhere in this repository or in any source I
reached, and the one dataset that could rank cell classes says the opposite word.**

The only cell-class-resolved quantitative dataset in the whole corpus is BrainRNAseq at mouse P7, and the
review that carries it into this repository says, verbatim (S2, 🟢 read directly today):

> *"At P7, **uniform** expression of [`Wwox`] is detected in neurons and **all glial cell types**."*

**`uniform` is not `preferential`. It is the denial of `preferential`.** And the same review's *own summary*
of where `Wwox` is most abundant is a list of **regions and neuronal subtypes**, never a statement that
neurons as a class exceed glia as a class. 🔴 **No source I reached ranks neurons above astrocytes or above
oligodendrocytes. Not one.** Meanwhile the primary rat IHC (S1, 🟢) reports `Wwox` in *"**most** APC-positive
oligodendrocytes"*, in astrocytes in **both grey and white matter**, and — in the same sentence that names the
cortical layers — *"**as well as the white matter** (D), corpus callosum (CC) (E)"*, i.e. the authors
themselves put **myelinated white matter alongside the neuronal layers**, not below them. S3 restates exactly
this: *"the expression was **mainly apparent in the layers II-III and V of the wild-type rodent cortex and
the white matter**"* (🟢 read directly today).

**FINDING 2 — 🔴 the line is a COMPOUND, and the weld is what makes it look measured.**

> *"WWOX is preferentially expressed in neurons"* **;** *"neuron-specific deletion is sufficient to replicate
> the null phenotype"*

The second clause is about **the sufficiency of a lesion**. The first is about **the distribution of a
molecule**. 🔴 **They are different experiments, and only the second one was done.** *Sufficiency of neuronal
deletion does not imply preferential neuronal expression* — a uniformly expressed gene can still produce the
whole phenotype when deleted in neurons alone, because sufficiency measures which cell's loss **matters**,
not which cell holds **most protein**. **Welding an unmeasured expression claim to a measured deletion
result, inside one `DATO` bullet, with one citation, transfers the deletion's evidentiary weight to the
expression claim.** That is the actual defect, and it is a species of exactly the failure
`epistemic_discipline.md` § 2 was written for: *the most dangerous premises are the ones too obvious to write
down.*

**FINDING 3 — 🔴 CORRECTED IN REVISION. My first formulation of this finding was WRONG, and I state the error
before I state the replacement.**

> ### 🔴 WHAT I WROTE, AND WHY IT WAS FALSE
> I originally wrote that *"the citation points at a paper this repository has NEVER SUCCESSFULLY READ"* and
> nominated it to the Orchestrator as the single most load-bearing claim in this file. **On verification it
> did not survive, and it is right that it did not.** `PMID 33914858` **was read, in full**, by actor
> `lettore-c`. There is an **810-line** artefact —
> **`learning/scientist/PILOT_PMID33914858_FULLTEXT_DEEPDIVE_SCIC_v1.md`** (S12, 🟢 read directly by me in
> this revision) — carrying an experiment-by-experiment reconstruction, **30 verbatim locators**,
> figure-panel adjudication, a supplementary assessment and a DisMech crosswalk, and recording the PDF's
> sha256, byte count and page count.
> 🔴 **I inferred "never read" from the absence of a dossier and a receipt. That inference was invalid: I
> searched the canonical chain and concluded from its silence, exactly the false-negative failure
> `epistemic_discipline.md` § 2 exists to prevent.** `PREMISE: DEFAULT_FROM_TEXTBOOK` → 🔴 *"no receipt and
> no dossier ⇒ not read"* is a **default, not a foundation**, and it was load-bearing and wrong.

**The replacement finding — narrower, true, and stronger than what it replaces:**

> 🔴 **The evidence behind that `DATO` line is not reachable through the canonical chain.**

What survives verification, each item checked directly by me in this revision:

- 🟢 **No receipt.** No entry in `fulltext_read_receipts.jsonl` carries `study_id.pmid == "33914858"`; the
  matching lines are other papers' receipts that merely cite it.
- 🟢 **No dossier.** There is no `research/fulltext_dossiers/PMID33914858.md`.
- 🟢 **Retrieval logged failed.** `research/retrieval_manifest.jsonl` → `FAILED_HTTP_403_CLOUDFLARE`.
- 🟢 **Suspended in the queue.** `research/fulltext_dossiers/PMID34747138_locators.md:19`, `:224`.
- 🎯 🔴 **And the pilot itself names the reachability defect, verbatim** (S12, lines 44–45): *"every text
  surface for this paper is **gitignored and local to one machine**. CI sees none of them. **A reader on a
  fresh clone has nothing.**"* The PDF and both extracted text surfaces live in `files/` and `staging/`,
  **both gitignored** (S12:34–36).
- 🎯 🟢 **The read is un-receipted by DELIBERATE, PRINCIPLED ABSTENTION — not by failure**, and this is the
  part I most misrepresented. S12 § 15, verbatim: *"This read has **not** been recorded as a receipt event.
  Whether an adjudicated surface may back a `contemporaneous_receipt` is exactly the gate FT-044 says does
  not yet exist, and issuing one here would decide that question by doing it."* 🔴 **That is a correct and
  disciplined refusal, and my original wording traduced it.**

⇒ **The defect is REACHABILITY, not absence of reading.** A `DATO`-tagged line in a meta-network file is
backed by a real, thorough, 810-line read whose **underlying text surfaces cannot be reached by anyone on a
fresh clone**, and which is **deliberately un-receipted** pending a gate that does not yet exist. 🔴 **That
is a more precise finding than the one it replaces, and it is the one the Orchestrator should carry.**

**FINDING 4 — 🎯 ADDED IN REVISION. The conflation I diagnosed is confirmed by the primary itself, in a
verbatim locator I had never seen.**

🔴 **SIBLING-ATTESTED throughout — `learning/scientist/PILOT_PMID33914858_FULLTEXT_DEEPDIVE_SCIC_v1.md:472`
(`L02`), `:471` (`L01`), `:488` (`L18`), `:486` (`L16`), `:493` (`L23`). I have NOT read the PDF; `files/` is
gitignored and absent from this worktree. These are the pilot's transcriptions, not my fetches.**

| Locator | Class | Verbatim, as the pilot transcribes it | Anchor |
|---|---|---|---|
| **`L01`** | CLEAN | *"…either neural stem and progenitors (using Nestin-Cre; N-KO), mature neurons (Synaspin I-Cre; S-KO), **oligodendrocytes (Olig2-Cre; O-KO)** or astrocytes (GFAP-Cre; G-KO)"* | Introduction, p.3062 |
| 🎯 **`L02`** | CLEAN | *"…**ablating WWOX expression in oligodendrocytes…and astrocytes…and observed no phenotype abnormalities**"* | Results, p.3065 |
| **`L18`** | CLEAN | *"we examined MBP staining in **O-KO** and control littermates at P17 and **found no major changes** (Supplementary Fig. 8)"* | Results, p.3070 |

> ### 🎯 `L02` IS THE PRIMARY EVIDENCE FOR THE CONFLATION, AND IT SHARPENS THE DIAGNOSIS RATHER THAN ONLY
> CONFIRMING IT.
>
> What the paper actually establishes about oligodendrocytes is a **requirement** result: delete `Wwox` in
> oligodendrocytes and **nothing happens**. That is a statement about **necessity**. It is **not** a statement
> about **abundance**, and it cannot become one.
>
> 🔴 **And now put `L02` next to S1, which I read directly in Part B:** Tochigi 2019 reports `Wwox` protein in
> *"**most** APC-positive oligodendrocytes"*, and calls itself *"the first to show that Wwox is expressed in
> oligodendrocytes."*
>
> 🎯 **So in the oligodendrocyte lineage, expression and requirement DISSOCIATE, and both halves are
> measured: the gene is present in most of these cells (S1, protein, rat) and deleting it from them alone
> does nothing (`L02`/`L18`, mouse).** **The word *"preferentially"* in the audited `DATO` line collapses
> precisely that dissociation into a single adjective.** A cell can hold a lot of a protein and not need it;
> a cell can need a protein it holds little of. **That is the whole content of this Part C**, and the
> repository's own corpus contains both measurements, on opposite sides of the same lineage, filed apart.

🔴 **Kept strictly separate, because the separation IS the finding:** `L02` is a **requirement/necessity**
result and it does **NOT** rescue the **expression-level** rival that § 5.3 refutes. Those are two different
axes and nothing in this file lets one settle the other. § 5.3 asks *does expression LEVEL predict
vulnerability*; `L02` asks *is this cell's own copy of the gene NEEDED*. 🎯 **Running them together would
reproduce, inside my own file, exactly the error I am auditing in someone else's line.**

### 6.3 🔴 CORRECTED IN REVISION — what my Part A/B data do to the line's LOAD-BEARING consequence

The line is load-bearing for the model three rows below it in the same file
(`meta_network_myelin_glia_current.md:40`):

> *"WWOX neuronal loss → reduced oligodendrocyte maturation → **non-cell-autonomous** hypomyelination"*

> ### 🔴 SECOND ERROR, CORRECTED. I originally wrote that this arrow *"loses its warrant."* **That was wrong,
> and it was wrong for the same reason Finding 3 was wrong: I reasoned from what I could not reach.**
>
> **The arrow has a direct, purpose-built warrant, and it is in the very paper I had written off.** It does
> **not** depend on the "preferentially expressed" premise at all. Two independent legs, 🔴 SIBLING-ATTESTED
> from S12:
>
> - **Leg (i) — the deletion that was actually done.** `L01` + **`L02`** + `L18`: an **Olig2-Cre
>   oligodendrocyte-specific `Wwox` deletion exists**, and it produces *"no phenotype abnormalities"*, no
>   survival difference (`L03`: *"P-value 1.0, no significance, log-rank Mantel-Cox test"*, S12:473) and
>   *"no major changes"* in MBP at P17.
> - **Leg (ii) — the positive transfer experiment.** **`L16`** (S12:486, CLEAN): *"OPCs that were cultured
>   with **Wwox-null DRGs** displayed significantly reduced differentiation into myelinating
>   oligodendrocytes…"* — i.e. **wild-type OPCs are impaired by null NEURONS.**
>
> 🎯 **Leg (i) is a necessity test and leg (ii) is a sufficiency test, and together they are exactly what a
> non-cell-autonomous claim requires.** My § 6.3 as first written asserted the arrow was unsupported **while
> the supporting experiments sat in an artefact I had not looked for.** I withdraw that assertion without
> qualification.

**What survives, and it is a real qualification rather than a refutation.** The arrow is warranted but is
**over-tagged as flat `DATO`**, and the pilot — which did read the body — says so more sharply than I could
have. 🔴 SIBLING-ATTESTED, S12 § 11 `M3`, verbatim:

> *"**This is the weakest link in the paper carrying the most downstream weight.** Both legs are compromised:
> leg (i) is a qualitative, single-marker, single-age negative reported only in **an inaccessible
> supplement** with no n and no statistic; leg (ii) is a **compositional** measure in a **PNS-axon/CNS-glia
> hybrid** whose categories are constrained to sum to 100%. Neither leg supplies a mediator — no molecule, no
> signal, no contact. … **"Non-cell-autonomous" is best read as a description of where the *trigger* is, not
> as a mechanism.** It is `DATO` that neuronal deletion suffices and oligodendrocyte deletion (as tested)
> does not; it is `IPOTESI` that the route is a neuron→OPC instructive signal."*

And `M1` records that the negative arm is **conditional on a control nobody has seen**: *"the Cre-efficiency
validation for O-KO and G-KO is Supplementary Fig. 1E/F, **unavailable**. **A poorly recombining Olig2-Cre
yields exactly this result.**"* (S12 § 11 `M1`; `0 of 9 supplementary figures obtained`, S12 § 15.)

🔴 **And the authors themselves leave the door open — `L23`, CLEAN (S12:493):** *"we **cannot exclude the
cell autonomous functions of WWOX in oligodendrocytes** or astrocytes in other neurological disorders."*

⇒ **Revised position on the arrow:** the **trigger location** is `DATO`; the **route** is `IPOTESI`; the
**negative arm** is conditional on an unseen Cre control. **The meta file's flat `non-cell-autonomous` is
defensible in direction and over-tagged in confidence** — a much smaller correction than I first claimed, and
one that touches the *second* clause's neighbourhood rather than the expression clause I audited.

**Three things still press on it, in descending order of solidity — restated after the correction:**

1. 🔴 **DEMOTED IN REVISION, against myself.** I had argued from *"`Wwox` is expressed in **most**
   APC-positive oligodendrocytes"* (S1) and from *"`Wwox` is **highest in progenitors**, significantly lower
   in mature cells"* (S2) that the lesion has *"a cell-autonomous shape."* 🎯 **`L02` answers both directly:
   the cells that express it were deleted, and nothing happened.** 🔴 **My two arguments were EXPRESSION
   arguments deployed against a REQUIREMENT conclusion — the exact conflation this Part C audits, committed
   by me, one section after I diagnosed it.** They are retained here only as the record of the error. **They
   carry no weight against the arrow.**
2. 🟡 **What genuinely remains from that line of argument is narrow:** the O-KO negative is a **single
   marker at a single age in a single supplement nobody has seen**, with the Cre-efficiency control also
   unseen. So *"oligodendrocyte `Wwox` is not required"* is established **for MBP at P17 in developmental
   myelination**, and for nothing else. **`NOT TESTED ≠ NOT REQUIRED`** — and the authors say as much
   themselves (`L23`).
3. 🟡 **The Abudiab preprint now has a precise place to sit, and it is NOT a contradiction** — S9,
   *"WWOX deficiency uncovers a cell-autonomous mechanism impairing myelin repair"*, reporting conditional
   deletion in oligodendroglia impairing OPC differentiation and WWOX stabilising **SOX10**. 🎯 **Note what
   the two studies actually ask: `L18` tests DEVELOPMENTAL myelination (MBP, P17, naïve animal); S9 tests
   ADULT MYELIN REPAIR after cuprizone demyelination. Those are different questions, and a gene can be
   dispensable for building myelin and required for rebuilding it.** `L23`'s *"cannot exclude the cell
   autonomous functions … in other neurological disorders"* is the same door, opened by the same laboratory
   four years earlier. 🔴 **I COULD NOT READ THIS PREPRINT — `EGRESS_BLOCKED`, bioRxiv API 403, no PMID,
   and what I hold is a search engine's prose, not an abstract. It carries NO weight and settles nothing.**
   It is a flag and the top retrieval priority in this file; the repository already logs it as `FT-007`,
   never retrieved (`full_text_queue_current.md:106-107`). 🎯 **If it says what the search engine says, the
   correct repair is NOT to overturn `non-cell-autonomous` but to bound it to development — which is a
   smaller and better-shaped correction than the one I proposed in my first draft.**

🔴 **Note the primary's own position, which is neither of the two stories and which I must not flatten:**
S1's Discussion proposes *both* routes at once — *"the severe reduction in myelination of [`lde`] cortices
may result, **at least in part**, from the retarded growth of axons"* **and** *"the reduced number of
APC-positive oligodendrocytes … indicates that the marked reduction in myelination is **also** caused by the
reduced number of mature oligodendrocytes."* **The primary says "both, in part". The repository's meta file
says "non-cell-autonomous", flat.**

### 6.4 🎯 THE VERDICT, stated as the brief demanded — not softened

> ## 🔴 **THE DATO LINE IS OVER-STATED. It should not stand as written.**

- 🔴 *"preferentially expressed in neurons"* is **not a `DATO`**. It is, at best, an `INFERENZA` from a
  deletion experiment; the only cell-class-resolved dataset in the corpus describes the distribution as
  **uniform**, and the primary rat IHC places `Wwox` in most oligodendrocytes, in astrocytes in grey and
  white matter, and *"as well as the white matter"* alongside the neuronal layers.
- 🔴 It is **compound**, welding an unmeasured expression claim to a measured deletion result under one
  citation and one `DATO` tag.
- 🔴 **CORRECTED:** its citation is to a paper that **was** read, in full, in an 810-line pilot artefact —
  but whose **text surfaces are gitignored, machine-local and invisible to CI**, and whose read is
  **deliberately un-receipted** pending a gate that does not exist. **The defect is reachability, not
  absence.** My first formulation of this bullet was wrong and is corrected in Finding 3.
- 🟢 **The second clause is fine, and is now positively corroborated.** *"Neuron-specific deletion is
  sufficient to replicate the null phenotype"* is a real result about a real experiment — and `L02`/`L03`
  supply its **matched negative control** (glia-specific deletion → no phenotype, log-rank *P* = 1.0), which
  is what makes the four-arm comparison strong. 🔴 **Nothing in this file touches it. The problem is its
  passenger.**
- 🟢 **`DL-MECH-027` is correctly held and is NOT the over-stated one.** It says *"neurons, astrocytes and
  oligodendrocytes"* without ranking them, and its dossier hedges the microglial negative properly. **A
  correctly-held line confirmed is a real result, and this is one.**

🔵 **I am READ-ONLY toward `meta/`, `research/` and every registry. I propose; I do not promote. No file but
my own was touched, and the wording above is a finding for the Orchestrator, not an edit.**
🎯 **Minimal proposed repair, for whoever holds the pen:** split the line in two, retag the first half
`INFERENZA` or delete it, keep the second half as `DATO` — 🔴 **and attach the REACHABILITY state of
`PMID 33914858`, not a claim that it is unread**: read in full, 30 locators, `learning/scientist/PILOT_…`,
**un-receipted by principled abstention**, text surfaces gitignored and machine-local.

### 6.5 🔴 EXISTING, UNAPPLIED CORRECTIONS THAT TOUCH THIS WORK — **not mine to apply**

S12 § 15 carries **eight** proposed canonical corrections `C1`–`C8`, all recorded there as explicitly
**NOT APPLIED**. Two are adjacent to this file and I name only those two, as instructed:

| # | Target | What it says | Status |
|---|---|---|---|
| **`C1`** | `claim_registry_current.md#CLAIM 003` | The boundary note reads *"Non promuovibile senza una delezione o un rescue **Olig2/CNP-specifici**"* — 🎯 **but an Olig2-Cre deletion exists in the source paper itself** (`L02`, `L18`). *"The note misstates the evidence base of its own source paper"* | 🔴 **UNAPPLIED** |
| **`C2`** | `paper_registry_current.md#PAPER 004` | Add an `Evidence depth:` field stating `metadata_and_abstract_only — no receipt`, since *"its absence makes an abstract-level record indistinguishable from an unexamined one"* | 🔴 **UNAPPLIED** |

🔵 **Neither is mine to apply, and I have applied neither.** I am READ-ONLY toward `claim_registry_current.md`
and `paper_registry_current.md`, and I did not edit the pilot. `C1` is recorded here only because it is the
same dissociation this section is about: **a canonical note asks for an experiment that had already been
done, because the evidence for it was not reachable.** 🔴 **That is the same reachability defect as Finding 3,
showing up a second time, in a second file.** `C3`–`C8` exist and are not restated here.

---

## 7 · WHAT I COULD NOT VERIFY — exhaustive and unflattering

1. 🔴 **I queried ZERO expression atlases. Not one.** Allen (`api.brain-map.org`), HPA (`proteinatlas.org`),
   Hipposeq (`hipposeq.janelia.org`), BrainRNAseq, DropViz, Allen celltypes, GTEx portal, EBI Expression
   Atlas and Ensembl REST are **all `EGRESS_BLOCKED`**, each tested once. **Every atlas statement in §§ 3 and
   5 reaches me through a 2020 review describing those atlases.** A review's description of a figure is not
   an atlas query, and I have not treated it as one — but the whole of § 3's mouse evidence rests on it.
2. 🔴 **There is no number in this file for any hippocampal subfield, for any cell type, in any species.**
   `P7` is scored on **ranked and qualitative statements only**. I have not measured flatness; I have shown
   that nobody reports CA1 as the standout.
3. 🔴 **The single best-matched dataset in existence was located and could not be read.** `PMID 36247526`
   (S4) is LCM RNA-seq of **rat** CA1/CA2/CA3/DG — right species, right resolution, published, with a GEO
   deposit. The served full text has **every gene symbol and the accession itself silently stripped**. 🔴 **I
   did not obtain a single value from it.** An actor with egress should go straight there; it is the
   cheapest remaining move in this entire line.
4. 🔴 **Hipposeq is the resource that would settle `P7` numerically and it is blocked.** That block, not my
   analysis, is why half of `P7` stays open (§ 3.3).
5. 🔴 **I inspected no figure panel, anywhere.** The rat *"hilus in the hippocampus"* datum — the single most
   load-bearing item in § 4 — is a **sentence pointing at a panel (F) that I have not seen**. If panel F
   shows CA1 staining that the sentence did not enumerate, § 4.1 weakens sharply.
6. 🔴 **`NOT NAMED ≠ ABSENT`, and § 4 leans on a not-named.** CA1's absence from Tochigi's *"especially"*
   list is an **author's emphasis**, not a measurement of CA1. `PREMISE: DETECTION_FLOOR`
   (`CC-20260920-DETECTION-FLOOR-01`).
7. 🔴 **The `ENTm2`-is-unlesioned argument (§ 4.3) is an argument from absence and a weak one.** Nobody ever
   examined the entorhinal cortex in `lde/lde`. I flagged this in place and did not score on it.
8. 🔴 **The Abudiab preprint (S9) was NOT read — not even at abstract depth.** `biorxiv.org` blocked, bioRxiv
   API 403, no PMID. I have a **search engine's synthesis**, which is weaker than an abstract and is not a
   quotation of anything. 🔴 **Its SOX10 mechanism, its `Cnp-Cre` conditional, its cuprizone result and its
   snRNA-seq claim are all UNVERIFIED by me** and are used nowhere as evidence.
9. 🔴 **Species, age and molecule are mismatched across every comparison in this file.** Rat protein at PND21
   vs mouse transcript at P7 vs mouse transcript in adult vs human bulk RNA. The corpus's own record is that
   WWOX mRNA and protein dissociate. **I report directional agreement only and have pooled nothing.**
10. 🔴 **I did not re-fetch either vacuolation primary** (`PMID 19500159`, `PMID 17803050`); both are logged
    unretrievable and `P7` did not require them. The `9/9` and `DG/CA3 appear spared` facts remain 🔴
    SIBLING-ATTESTED and the figure-caption defect at `PMID19500159.md:117-123` is **untouched by this act**.
11. 🔴 **Purkinje cells are still unreported in either direction** and I added nothing to that question.
12. 🔴 **Dentate granule cells and CA1/CA3 pyramidal cells have no `Wwox` datum at all, in any source, in
    either direction.** The cell type at the centre of `H3` has never been measured.
13. 🔴 **My § 2 preregistration was substantially retrodiction and I said so before searching.** Of eleven
    preregistered items, **four proved unscorable**, one went against me (astrocytes-below-neurons), and one
    split irreconcilably (microglia). **That is a weak preregistration and I do not claim credit for the
    parts that were already in the baseline.**
14. 🔴 **§ 6.3's conclusion is conditional on an unread preprint** and must not be reported as though it
    were not.
15. 🔴 **Whether the meta line's second clause is itself sound is UNTESTED here.** **I audited the line's
    support, not the underlying biology.**

### 7.1 🔴 ADDED IN REVISION — two errors of my own, and what they cost

16. 🔴 **I claimed `PMID 33914858` had "never been successfully read by this repository". It was read, in
    full, in an 810-line artefact with 30 verbatim locators.** I inferred absence from the silence of the
    canonical chain (no receipt, no dossier, failed retrieval manifest) and **never searched outside it** —
    I did not grep `learning/`, which is where the read lives. 🔴 **I nominated that claim to the
    Orchestrator as the single most load-bearing statement in the file, and it was the one that broke.** The
    corrected finding (reachability, not absence) is in § 6.2 Finding 3.
17. 🔴 **I claimed the `non-cell-autonomous` arrow "loses its warrant". It has a direct, two-legged warrant
    — an Olig2-Cre deletion (`L02`, `L18`) and a DRG–OPC co-culture (`L16`) — built for exactly that
    purpose, in the paper I had written off.** Corrected in § 6.3. **Both errors have the same root: I
    treated a surface I could not reach as evidence that nothing was there.** That is the false-negative
    failure mode `epistemic_discipline.md` § 2 names as *"silent, permanent, and self-reinforcing"*, and I
    committed it twice in one file.
18. 🔴 **I have NOT read the `PMID 33914858` PDF, and cannot.** `files/` and `staging/` are gitignored and
    **absent from this worktree**. Every `L01`/`L02`/`L03`/`L16`/`L18`/`L23` quotation is the pilot's
    transcription, at 🔴 SIBLING-ATTESTED depth, labelled at every use. **I verified none of them against
    the body.**
19. 🔴 **The O-KO negative arm rests on material nobody has seen.** `L18`'s MBP result is in **Supplementary
    Fig. 8** and the Cre-efficiency validation is **Supplementary Fig. 1E/F** — S12 records **0 of 9
    supplementary figures obtained**. 🔴 **A poorly recombining Olig2-Cre would produce the same negative**,
    and that possibility is untested. My § 5.3 revision and § 6.3 both lean on this negative and inherit its
    weakness.
20. 🔴 **The development-vs-repair reconciliation of `L18` against the Abudiab preprint (§ 6.3 item 3) is my
    own construction and is UNVERIFIED on both sides** — I read neither the supplement nor the preprint. It
    is offered as the shape a correction should take, **not as a finding**.

---

## 8 · NOVELTY GRADE — conservative

> ## **C — NOVEL CONNECTION**

**Why not `A` (rediscovery).** Three things in this file are in no `disease-models/wwox/` file: the DropViz
hippocampal subcluster resolution (`Lhx1`/`Nxph3`/`Gad2` → medial EC, `Slc17a7`+/`Reln`+ — a grep confirms
these tokens appear nowhere in the tree); the scoring of `P7` and the split adjudication of `H3`; and the
§ 5.3 anti-correlation between the wild-type expression map and the `lde/lde` lesion map.

**Why not `B` (trivial inference).** The `hilus` sentence, the GTEx values, the Allen region list and the
BrainRNAseq uniformity were **all already held** — 🔴 **and the hilus datum was even noted by a sibling
earlier today** (`lde_myelin_vacuole_bridge_20260922.md:403`). **Every ingredient of § 4.1 was on the shelf.**
What was absent was putting the expression map next to the lesion map and asking whether they agree. That is
more than an inference from one held fact, but it is **not much more**, and `B` is a defensible reading that
I will not argue against.

**Why not `D`/`E`/`F`.** 🔴 **This file generates no new testable hypothesis, designs no experiment and names
no therapeutic direction.** It **kills and splits a rival**, which is negative work. The one experimental
consequence it produces — *add an entorhinal-cortex sampling box to `E1`* — is a **modification of a sibling's
existing design**, not a new experiment. 🔴 **Grading this `E` would be inflation and I decline it.**

**What it is worth, at its true size:**
1. 🎯 `P7`, preregistered by another actor and left explicitly untested, is **scored** — and scored
   `SUPPORTED` with the open half named.
2. 🎯 `H3` is **split**, which nobody expected: it fails on CA1 and **survives on the amygdala**.
3. 🎯 The expression-level rival for differential vulnerability is **refuted as a general explanation**, on a
   measured sparing in the highest-expressing cortical cell type — 🔴 **not** on an absence of reports.
4. 🔴 A `DATO` line is shown to be over-stated and compound — **and the conflation is confirmed from the
   primary itself by `L02`, a locator I had never seen when I diagnosed it.**
5. 🔴 An unregistered contradiction (microglia, § 5.4) is put on the record.
6. 🔴 **A reachability defect is named:** the evidence behind that line was read in full and is invisible to
   a fresh clone — and `C1` shows the same defect biting a second file, where `CLAIM 003`'s boundary note
   asks for an Olig2-specific deletion **that already exists in its own source paper**.

### 8.1 🔴 ADDED IN REVISION — why the grade does not move

**It stays `C`, and it is a cleaner `C` than the one I first claimed.** The revision *removed* two assertions
of mine and *added* primary evidence I did not find myself:

- 🔴 **Two of my conclusions were wrong** (§ 7.1 items 16–17) and are corrected in place, not deleted.
- 🎯 **The Part C diagnosis — that the line welds an unmeasured *expression* claim to a measured
  *requirement* result — survived contact with the primary and was sharpened by it.** `L02` is the evidence
  for my own argument, and **it existed before I made the argument**; I reasoned my way to a conflation whose
  proof was already sitting in the repository, unconnected.
- 🔴 **That is not a promotion.** Diagnosing a conflation whose primary evidence already exists is a
  **connection**, which is what `C` means. 🔴 **It is emphatically not `D` or `E`: I generated no hypothesis
  and designed no experiment, and the strongest single item in my original handback was retracted.**

**And what it is NOT worth:** 🔴 **a null result cleanly established is the whole of this file.** No mechanism
was found, no number was obtained, no atlas was queried, and the metabolic question the brief pointed at is
**left exactly as open as it was** — with one rival removed from in front of it.

---

## 9 · SOURCE ATTRIBUTION

**According to PubMed.** Bibliographic records, abstracts and full texts in this file were retrieved from
**PubMed / PubMed Central** via the PubMed MCP route. Web search results were retrieved from the open web.

| Source | Identifier | Depth here |
|---|---|---|
| Tochigi Y *et al.* 2019, *Int J Mol Sci* — `lde/lde` rat cortex, hypomyelination, `Wwox` localisation | PMID **31340538** · PMC6678113 · [DOI](https://doi.org/10.3390/ijms20143596) | 🟢 full body read directly |
| Aldaz CM & Hussain T 2020, *Int J Mol Sci* — WWOX LoF in neurodevelopmental/neurodegenerative disorders | PMID **33255508** · PMC7727818 · [DOI](https://doi.org/10.3390/ijms21238922) | 🟢 full body read directly |
| Steinberg DJ & Aqeilan RI 2021, *Cells* — WWOX-related neurodevelopmental disorders: models | PMID **34831305** · PMC8623516 · [DOI](https://doi.org/10.3390/cells10113082) | 🟢 read directly (targeted extraction) |
| *The transcriptome of rat hippocampal subfields* 2022, *IBRO Neurosci Rep* — LCM RNA-seq, rat CA1/CA2/CA3/DG | PMID **36247526** · PMC9561749 · [DOI](https://doi.org/10.1016/j.ibneur.2022.09.009) | 🟢 body read; 🔴 **gene symbols and GEO accession stripped from the served text — no value obtained** |
| Abudiab B *et al.* 2025, bioRxiv (**unrefereed preprint, no PMID**) — *WWOX deficiency uncovers a cell-autonomous mechanism impairing myelin repair* | [DOI](https://doi.org/10.1101/2025.11.22.689900) · repository `FT-007` | 🟡 **search-synthesis depth only — NOT READ. Flag, not evidence** |
| Suzuki H *et al.* 2009, *Genes Brain Behav* — `lde/lde` vacuolation | PMID **19500159** · [DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x) | 🔴 not fetched; 🔴 SIBLING-ATTESTED where used |
| Suzuki H *et al.* 2007, *Comp Med* — `lde` rat phenotype | PMID **17803050** (no DOI registered) | 🔴 not fetched; 🔴 SIBLING-ATTESTED where used |
| Repudi S *et al.* 2021, *Brain* — the citation behind the audited DATO line | PMID **33914858** · [DOI](https://doi.org/10.1093/brain/awab174) | 🔴 **NOT READ BY ME.** 🟢 **Read in full by actor `lettore-c`** — 810-line pilot, 30 locators. 🔴 **Un-receipted by principled abstention; no dossier; text surfaces gitignored and machine-local; retrieval logged `FAILED_HTTP_403_CLOUDFLARE`.** Every `Lnn` quotation in this file is 🔴 SIBLING-ATTESTED from that artefact |
| 🎯 `learning/scientist/PILOT_PMID33914858_FULLTEXT_DEEPDIVE_SCIC_v1.md` — actor `lettore-c` | repo artefact, 810 lines | 🟢 **read directly by me in revision**; the source of `L01`, `L02`, `L03`, `L16`, `L18`, `L23`, `M1`, `M3`, `C1`, `C2` and the reachability statement |

**Databases named and their status in this deployment:** Allen Mouse Brain Atlas (`api.brain-map.org`,
`brain-map.org`) ⚫ blocked · Human Protein Atlas (`proteinatlas.org`) ⚫ blocked · Hipposeq
(`hipposeq.janelia.org`) ⚫ blocked · DropViz (`dropviz.org`) ⚫ blocked · BrainRNAseq (`brainrnaseq.org`)
⚫ blocked · GTEx portal ⚫ blocked (🟢 but a local extract is held at
`disease-models/wwox/analysis/data/WWOX_tissue_expression_GTEx.csv`) · EBI Expression Atlas ⚫ blocked ·
Ensembl REST ⚫ blocked · bioRxiv and its API ⚫ blocked · Human Brain Transcriptome — via S2 only.

🔵 **No contact details of any living person are reproduced. No individual-level record appears anywhere in
this file. 🔴 Nothing in this file is medical advice, and no molecule, dose, route, schedule or compound is
named anywhere in it.**
