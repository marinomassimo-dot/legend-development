# PUBLIC DATA-DEPOSIT CENSUS FOR WWOX WORK — and the reanalysis opportunities that need no freezer

**Node:** `REANALYSIS_DEPOSIT_CENSUS` · **Actor:** SCIENTIST 3 (`scientist-3`) · **Date:** 2026-09-22
**Reports to:** Orchestrator · **Status of this file:** 🔴 **non-canonical analysis artefact.**

> READ-ONLY toward the four scientific current files, every registry, every ledger, the receipt chain and
> `framework/state/state_manifest_current.md`. No claim, no paper record, no working-model edit, no commit
> candidate, no receipt, no promotion. Nothing here may be cited as canonical.
>
> 🔴 **Nothing in this file is medical advice.** No molecule, no dose, no route, no schedule.
> 🔵 **Public edition.** Genotype-class and named-allele level only. No individual-level record.
> ⚠️ **Alleles and models are never pooled.** `Wwox`-null mouse, `Wwox^P47T/P47T` knock-in, `lde/lde` rat,
> hESC `WWOX`-KO (WiBR3), shRNA `WWOX` knockdown in hNPC, human WOREE and human SCAR12 are **distinct
> objects**, and every row below carries the object it was measured in.
> 🔴 **This is a community-stimulation census, not an evidence-weighting instrument.** No group's scientific
> claims are favoured here because that group is strategically interesting.

---

## § 0 · READ DEPTH, DECLARED PER SOURCE, BEFORE ANY FINDING

| Mark | Meaning |
|---|---|
| 🟢 **READ DIRECTLY THIS ACT** | I fetched the artefact myself, in this act, at the stated depth |
| 🔴 **SIBLING-ATTESTED** | Quoted from a LEGEND repo file, **with file AND line**. A contemporaneous record of someone else's read. **Never presented as a fresh fetch** |
| 🟡 **ABSTRACT-DEPTH** | Title/abstract only. 🔴 **An abstract is not a read** |
| ⚫ **SURFACE_BLOCKED** | The surface was tested once in this act and failed. Failure recorded with its exact mode. No retries |

### 0.1 Sources read directly this act

| Source | Identity | Depth | What I took from it |
|---|---|---|---|
| **PMID 31543760** / **PMC6730490** | Kośla K … Bednarek AK, *Front Cell Neurosci* 2019, [DOI](https://doi.org/10.3389/fncel.2019.00391) — `WWOX` silencing in human neural progenitors | 🟢 **full served body, read end to end** (≈ 24 kB) | Design of the deposit behind `GSE126075`; **two deposit sentences whose accession string is deleted by the extractor** |
| **PMID 34747138** / **PMC8649866** | Repudi S … Aqeilan RI, *EMBO Mol Med* 2021, [DOI](https://doi.org/10.15252/emmm.202114599) — neonatal neuronal WWOX gene therapy | 🟢 **full served body, read end to end** | 🔴 **No data-availability section, no accession, no omics assay anywhere in the paper** |
| **PMID 36828035** / **PMC10835625** | Hussain T … Aldaz CM, *Prog Neurobiol* 2023, [DOI](https://doi.org/10.1016/j.pneurobio.2023.102425) — `Wwox^P47T` knock-in mouse | 🟢 **full served body (60,088 chars) retrieved; read targeted** — every occurrence of `RNA-seq`, `transcriptom`, `deposit`, `accession`, `availab`, `GEO`, `GSE`, `SRA`, `BioProject` inspected in ±350–800-char windows, plus the RNA-seq Methods §4.14 and Results §2.8 read in full | **Bulk RNA-seq exists, n=5 vs 5, four regions including cerebellum**; 🔴 **no data-availability statement and no accession on this surface** |
| **PMID 41984841** / **PMC13099603** | Bidany-Mizrahi T … Aqeilan RI, *PNAS* 2026, [DOI](https://doi.org/10.1073/pnas.2534844123) | 🟢 **full served body (43,544 chars) retrieved; token-swept** for the same nine deposit tokens, plus tail read | RNA-seq **and p63 ChIP-seq** (NovaSeq 6000); 🔴 **zero occurrences of any deposit token; no data-availability section on this surface** |
| **PMID 41090157** / **PMC12517091** | Hussain T … Aldaz CM, *Blood Neoplasia* 2025, [DOI](https://doi.org/10.1016/j.bneo.2025.100153) | 🟢 **full served body (27,637 chars) retrieved; token-swept** identically | Transcriptome + exome of `Wwox`-KO × VkMYC plasma cells; 🔴 **zero deposit tokens; no data-availability section on this surface** |
| **PMC11998783** (PMID 40235507) and **PMC12734678** | Cheng F *et al.* — human cerebellar single-nucleus multiome, 103,861 nuclei | 🟡 **ABSTRACT-DEPTH, and involuntarily so.** Both PMC records return `full_text: ""` — an **empty body**, not a short one | 103,861 nuclei, snRNA-seq + snATAC-seq, cerebellum + frontal cortex, **Purkinje and granule cells separately analysed**; 🔴 **no accession obtainable** |
| PubMed metadata + ID-conversion | 20 + 18 PMIDs resolved to PMCIDs/DOIs | 🟢 this act | PMC presence/absence per paper; 🔴 **the PubMed record carries no databank/accession field in this server's schema** |
| WebSearch | 6 queries (§ 2.2) | 🟢 this act | Title of `PMID 42397075` established: *"Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids"*; no accession from any snippet |

### 0.2 🔴 Sources carried on the repository's authority, not on mine (SIBLING-ATTESTED)

| Fact carried | Repo file **and line** |
|---|---|
| `GSE156243` = the 2021 `WWOX`-KO cerebral-organoid RNA-seq | `research/discovery_ledger_current.md:765` (`DL-MECH-034`), repeated `:797` (`DL-MOL-010`) |
| `GSE156243` is **WT n=2 vs engineered KO n=4**, week-15 organoids, and contains **zero molecules of any splice-allele transcript** | `analysis/tx001_public_rna_data_feasibility_20260921.md:348` (N-18), design at `analysis/mechanism_intervention_map.md:922` |
| The 2021 paper's data-availability block reads **`Gene Expression Omnibus:()`** — the accession string deleted by the extractor | `analysis/tx001_public_rna_data_feasibility_20260921.md:24–26`, `:209–214`, `:352` (N-22) |
| `GSE126075` = Kośla 2019, the transcriptome re-used by the Genoa 2020 paper; **not an independent replication** | `research/deepdive_manifests/PMID32581702.json:38` and `:208` |
| `GSE117387` = the Abdeen 2018 mouse mammary-tumour RNA-seq, and LEGEND **could not reproduce its processing** | `research/fulltext_dossiers/PMID30082886.md:89` |
| `GSE193659` = the Łódź bladder CAGE deposit; `GSE31684` is a **re-used public cohort, not a WWOX deposit** | `research/deepdive_manifests/PMID37519886.json:81`, `:334`, `:359` |
| Nascimento's own 18 per-sample deposits are `GSM8002943`–`GSM8002960`; `GSE186538` and `GSE199762` are **the re-used adult-EC series, NOT Nascimento's deposit**; depth `author-code`, **none resolved against GEO** | `research/commit_candidates/CC-20260922-NASCIMENTO-DATA-ROUTE-01.md:136–138`, `:146`; `analysis/AUTONOMOUS_SESSION_STATE.md:47–48` |
| No GEO/dbGaP accession for the Nascimento snRNA-seq is obtainable; the statement is deferred to the publisher, which is 403 | `analysis/wwox_postnatal_svz_expression_20260922.md:241–244`; `analysis/nascimento_accession_and_g372r_20260922.md:20`, `:460` |
| 🔴 **The 2026 gene-therapy paper states `Data and code availability: Not relevant.`** — there is no deposited source data to request | `analysis/tx007_animal_flow_survival_validity_20260922.md:82`, `:694`, `:733` (`A-8`) |
| The Cheng cerebellar multiome is known to LEGEND only as a **conference abstract**, with accession, access terms, cluster definitions and Purkinje nucleus count all `NOT STATED` | `analysis/tx007_purkinje_frontier_20260922.md:149` (`A-f7`), citing `analysis/purkinje_cerebellar_celltype_wwox_census_20260922.md:511`, `:734` |

---

## § 1 · BASELINE — what the repository already held, and what I therefore did **not** redo

`enumerate_baseline` was run **before any external query.** I read
`tx001_public_rna_data_feasibility_20260921.md`, `nascimento_accession_and_g372r_20260922.md` (both by
targeted token sweep over the full file), `splice_allele_rna_evidence_20260922.md`,
`wwox_postnatal_svz_expression_20260922.md`, `next_scientist_scout_20260921.md`,
`chang_ncku_wave1_20260920.md`, `chang_ncku_wave2_node_independence_20260920.md`,
`adelaide_node_discriminator_20260921.md`, `lodz_node_discriminator_20260921.md`,
`downstream_wwox_independent_rescue_census_20260921.md`,
`purkinje_cerebellar_celltype_wwox_census_20260922.md`, `wwox_subfield_celltype_expression_20260922.md`,
`CC-20260922-NASCIMENTO-DATA-ROUTE-01.md`, and grepped **the whole repository** for
`GSE\d+|PRJ[NE][AB]\d+|SRP\d+|E-MTAB|PXD\d+|MassIVE|ArrayExpress|dbGaP|EGA[SD]\d+|phs\d+` and for
`accession|Data availability|deposited`.

### 1.1 🔴 ALREADY HELD — not redone, and none of it claimed as new here

**Seven accession strings exist anywhere in this repository.** Four are WWOX-associated deposits; three are
re-used third-party series.

| Accession | What it is | Status in the repository |
|---|---|---|
| `GSE156243` | 2021 hESC `WWOX`-KO cerebral-organoid RNA-seq, WT n=2 vs KO n=4 | **Held and already worked.** `TX001` established definitively that it cannot answer the splice-allele question |
| `GSE126075` | Kośla 2019 hNPC `shWWOX` CAGE | **Held only as an attribution label.** Its design, arms and chemistry were **not** in the repository |
| `GSE117387` | Abdeen 2018 `Wwox`-KO mouse mammary tumour RNA-seq | Held; explicitly **not reproduced** |
| `GSE193659` | Kołat/Bednarek 2023 bladder-cancer CAGE | Held |
| `GSE31684` | public bladder cohort **re-used** as a validation set | Held; 🔴 **not a WWOX deposit** |
| `GSE186538`, `GSE199762`, `GSM8002943`–`GSM8002960` | Nascimento 2023 postnatal SVZ snRNA-seq — the first two are **re-used adult-EC series**, the GSM range is the study's own 18 samples | Held at depth `author-code`; 🔴 **never resolved against GEO** |

### 1.2 🟢 Is there already a systematic deposit census? **NO.**

I checked explicitly. There is a **route-specific** accession hunt for one paper
(`nascimento_accession_and_g372r_20260922.md`), a **feasibility study of one question against one deposit**
(`tx001_public_rna_data_feasibility_20260921.md`), and scattered attributions. `tx001` § 6 itself says so:
it had *"no GEO, SRA, ArrayExpress or EGA query tool"* and describes its own result as *"a census of the
**literature**, which is a weaker instrument"* (`:305`). **There is no census of deposits.** This file is
therefore **not a `REDISCOVERY`** in the census sense, while overlapping the baseline heavily — which is why
§ 1.1 exists and why nothing in it is re-asserted below as a finding.

### 1.3 🔴 What the baseline already closes, so I did not reopen it

- Whether `GSE156243` can measure a splice-allele transcript. **Closed: it cannot** (`tx001` N-18). Not reopened.
- Whether the 2026 *Brain* organoid paper has an establishable accession. **Closed as NOT ESTABLISHABLE**. I confirmed only that it has no PMC deposit and recovered its **title**, which the repository did not hold.
- Whether the 2026 gene-therapy paper deposited data. **Closed: `Data and code availability: Not relevant.`** Not reopened, and it is the reason 🎯 Q2 fails below.

---

## § 2 · METHOD, QUERIES RUN, AND POSITIVE CONTROLS

### 2.1 🔴 The instrument, established first — and it is badly limited

**Every dedicated data-repository surface is blocked from this deployment.** Measured, once each, this act:

| Surface | Route | Result |
|---|---|---|
| `www.ncbi.nlm.nih.gov` (GEO accession viewer, `GSE156243`) | `curl` | ⚫ `CONNECT tunnel failed, response 403`, `HTTP:000`. The proxy's own status endpoint records it: `{"kind":"connect_rejected","host":"www.ncbi.nlm.nih.gov:443"}` |
| `www.ncbi.nlm.nih.gov` | `WebFetch` | ⚫ `EGRESS_BLOCKED` |
| `www.ebi.ac.uk` — BioStudies/ArrayExpress search, PRIDE v3 API, ENA portal API | `curl` ×3 | ⚫ `HTTP:000` ×3 |
| `www.ebi.ac.uk/biostudies/arrayexpress/studies?query=WWOX` | `WebFetch` | ⚫ `EGRESS_BLOCKED` |
| `api.datacite.org` (DOI search for WWOX datasets) | `WebFetch` | ⚫ `EGRESS_BLOCKED` |
| `www.omicsdi.org` (cross-repository dataset index) | `WebFetch` | ⚫ `EGRESS_BLOCKED` |
| `www.europepmc.org`, `api.crossref.org`, `api.openalex.org` | `curl` ×3 | ⚫ `HTTP:000` ×3 |
| `www.biorxiv.org`, `becker.wustl.edu` | `WebFetch` ×2 | ⚫ `EGRESS_BLOCKED` ×2 — **`WebFetch` failed on 6 of 6 distinct hosts tested, so it is blocked wholesale, not host-selectively** |

**🟢 Positive control that egress is not wholly dead, so the zeros above are about these hosts and not about a
dead network:** in the same act, **WebSearch returned results for all six queries**, and the **PubMed MCP
served five complete article bodies**, one of them 60,088 characters. The instrument works; the data
repositories are unreachable.

> 🔴 **Therefore the single most important statement in this file: I could not verify that ANY accession
> resolves. Every `ACCESS STATUS` below is `NOT VERIFIED`, and none is guessed.**

### 2.2 Queries actually run, with their counts

**PubMed (`[All Fields]`-expanded; `query_translation` checked term-by-term on each):**

| Query | Hits | Positive control inside it |
|---|---|---|
| `WWOX AND (RNA-seq OR transcriptome OR "RNA sequencing" OR microarray OR "single-cell" OR snRNA-seq OR scRNA-seq)` | **119** | ✅ returns `34268881` (the known `GSE156243` paper) and `32581702` |
| `WWOX AND (proteomic OR interactome OR "mass spectrometry" OR ChIP-seq OR ATAC-seq OR methylome OR "CUT&RUN" OR phosphoproteom*)` | **28** | ✅ returns `37519886` (the known `GSE193659` paper) |
| `WWOX AND (RNA-seq OR transcriptome OR "single-cell" OR proteomic OR sequencing) AND (brain OR neuron OR epilepsy OR neurodevelopmental)` | **74** | ✅ returns `42397075`, `32581702`, `36828035` |
| `(Aqeilan RI OR Suzuki H OR Bednarek AK OR Aldaz CM)[Author] AND WWOX AND (transcriptome OR RNA-seq OR proteomic OR microarray OR "single-cell")` | **36** | ✅ all four named groups return records |
| `Kosla K[Author] AND WWOX AND neural progenitor` | **2** | ✅ returns `31543760` (the `GSE126075` source) and `32581702` |
| `Repudi S[Author] AND Wwox` | **6** | ✅ returns `34747138`, `34268881`, `42422765` |
| `(Tochigi Y OR Suzuki H)[Author] AND (lde rat OR Wwox) AND (transcriptome OR RNA-seq OR microarray OR expression profiling)` | **1** | ⚠️ the single hit is `32581702` — the **Genoa** paper, whose transcriptome is **Łódź's** `GSE126075`. **The `lde` rat group has no transcriptomic deposit reachable by this query.** |

**One query is reported with a boundary rather than a count:** `WWOX AND (brain OR neuron* OR neural OR
cerebral OR cerebellum OR epilep* OR WOREE OR SCAR12 OR organoid OR hippocamp* OR glia OR oligodendrocyte)
AND (…)` was **rejected by the server** — `INVALID_QUERY: too many boolean operators (21, max 20)`. It
produced no zero and none is carried.

**WebSearch (6 queries):** WWOX + GEO data availability; Repudi *Brain* 2021 accession; Cheng cerebellar
multiome accession; `awab174` data availability; Steinberg *Brain* 2026 `awag239` accession; WWOX
ProteomeXchange/PRIDE. 🟢 **Positive control:** the Steinberg query returned the paper's **exact title and
author list**, so the surface reaches the target literature. 🔴 **Not one of the six returned an accession
string**, and the engine could not index GEO itself.

### 2.3 🔴 The hazard that governs every negative in § 3, measured TWICE this act

**Positive control for the hazard, read directly in `PMC6730490`:** the Methods say

> *"The raw data from CAGE experiment are deposited in NCBI Gene Expression Omnibus (GEO) Database with
> accession number."*

— and the Data Availability section says

> *"The datasets generated for this study can be found in NCBI GEO Database,."*

**The sentence survives; the hyperlinked accession string is deleted.** The repository independently holds a
second instance — `PMC8350905`'s *"Gene Expression Omnibus:()"*
(`tx001_public_rna_data_feasibility_20260921.md:24–26`). **Two independent instances, one measured today.**

⇒ **A zero for `GSE` in a served body is evidence about the surface, not about the paper.** Where the *whole*
data-availability section is also absent (PNAS 2026, *Blood Neoplasia* 2025), that is a **stronger** failure
than string deletion and is labelled as such below — but it is still not evidence that the authors deposited
nothing.

---

## § 3 · THE CENSUS

**Every row: `NEW ANIMALS? = NO`.** No row required a new animal, and none is flagged.
**Every row: `ACCESS STATUS = NOT VERIFIED`** — see § 4 for why, per row.

### 3.1 WWOX-associated deposits that are NAMED (accession string in hand)

| # | ACCESSION | REPOSITORY | GROUP | PAPER | ASSAY | ORGANISM / ALLELE-MODEL (never pooled) | SAMPLE STRUCTURE | ACCESS | WHAT REANALYSIS ALONE COULD ANSWER | GAIN | COST | NEW ANIMALS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **D1** | `GSE126075` | GEO | **Łódź / Bednarek** (Kośla) | PMID 31543760, [DOI](https://doi.org/10.3389/fncel.2019.00391) | **CAGE** (5′-end TSS), Illumina HiSeq | **Human**, H9-hESC-derived neural progenitors, **shRNA `WWOX` knockdown vs scrambled** — 🔴 a knockdown, **not** a patient allele | **4 arms**: hNPC/shScr, hNPC/shWWOX, 14-d differentiated neurons/shScr, neurons/shWWOX. 9,427 genes analysed; 2,282 DEG in hNPC, 7,392 in neurons. 🔴 **replicate n per arm is NOT STATED anywhere in the paper** | **NOT VERIFIED** | Promoter/TSS-level consequences of WWOX loss in **human neural** cells, and whether the program is **differentiation-stage-dependent** (the paper's own numbers say it is: 44 vs 109 enriched sets undifferentiated, 0 vs 4 differentiated) | **MEDIUM–HIGH** | desk-hours | **NO** |
| **D2** | `GSE156243` | GEO | **Jerusalem / Aqeilan** (Steinberg) | PMID 34268881, [DOI](https://doi.org/10.15252/emmm.202013610) | bulk RNA-seq, KAPA stranded poly-A, 75 bp SE | **Human**, WiBR3 hESC **CRISPR `WWOX`-KO** cerebral organoids — 🔴 **engineered KO, not the `c.517-2A>G` patient line** | WT **n=2** vs KO **n=4**, week-15 organoids. EV selection at raw *P*<0.01; five symbols corrupted by spreadsheet auto-dating | **NOT VERIFIED** | Cell-type deconvolution of the KO organoid; expression of the WWOX-independent downstream nodes the rescue census enumerated; ⚠️ **already closed for the splice question** | **MEDIUM** | desk-hours | **NO** |
| **D3** | `GSM8002943`–`GSM8002960` | GEO (per-sample; **series accession unknown**) | **Nascimento *et al.*** | PMID 38122823 | snRNA-seq, human postnatal SVZ/EC stream | **Human**, wild type, 23 GW–27 y | 18 samples incl. `EC_Stream`. 🔴 the *"all samples"* DE table also contains **50–79-y adult cortex from `GSE186538`** | **NOT VERIFIED** | 🎯 **Q1 partial** — cell-type-resolved `WWOX` in human **postnatal forebrain**. 🔴 **No cerebellum, no Purkinje** | **MEDIUM** | desk-hours | **NO** |
| **D4** | `GSE117387` | GEO | **Jerusalem / Aqeilan** (Abdeen) | PMID 30082886, [DOI](https://doi.org/10.1038/s41419-018-0896-z) | bulk tumour RNA-seq | **Mouse**, conditional `Wwox` ablation, mammary tumours — 🔴 **non-CNS; somatic, background-confounded (C3H/B6-129)** | not re-established here | **NOT VERIFIED** | WWOX-loss transcriptional program in a **non-neural** tissue, as a contrast set only | **LOW** | desk-hours | **NO** |
| **D5** | `GSE193659` | GEO | **Łódź / Bednarek** (Kołat) | PMID 37519886, [DOI](https://doi.org/10.3389/fgene.2023.1214968) | **CAGE**, lentiviral stable transduction | **Human**, 3 bladder-cancer lines (RT-112, HT-1376, CAL-29), WWOX/AP-2 variants — 🔴 **non-CNS, cancer** | 18 profiles; 🔴 the three lines were treated as **biological replicates** | **NOT VERIFIED** | A second, independent **CAGE** WWOX-perturbation object — usable only as a **methodological** cross-check on D1, never as disease evidence | **LOW** | desk-hours | **NO** |

### 3.2 Deposits that are DECLARED but whose accession is NOT OBTAINABLE from this deployment

| # | PAPER | GROUP | ASSAY | ORGANISM / ALLELE-MODEL | SAMPLE STRUCTURE | WHY NO ACCESSION | WHAT IT WOULD ANSWER | GAIN | NEW ANIMALS |
|---|---|---|---|---|---|---|---|---|---|
| **U1** | PMID 42397075, *Brain* 2026, [DOI](https://doi.org/10.1093/brain/awag239) — **"Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids"** (title established this act) | **Jerusalem / Aqeilan** (Steinberg, Zonca; **Davila-Velderrain** on the author line) | **single-cell RNA-seq** of patient-derived organoids | **Human**, WOREE (`c.517-2A>G`, WSM) and SCAR12 (`G372R`, WPM) iPSC lines — 🔴 **the only deposit-class object in the field carrying real patient alleles** | not establishable | 🔴 **No PMC deposit** (repo-attested test: esummary returns only pubmed/doi/pii; elink to pmc returns nothing). Publisher 403/blocked. WebSearch returned the title but no accession | Allele-resolved, cell-type-resolved human neural transcriptome — the **highest-value** object in this census **if** it is deposited openly | **HIGH (conditional)** | **NO** |
| **U2** | PMID 33914858, *Brain* 2021, [DOI](https://doi.org/10.1093/brain/awab174) — neuronal `Wwox` deletion | **Jerusalem / Aqeilan** (Repudi) | bulk RNA-seq of **whole cortex and hippocampus** (🟡 description recovered at WebSearch-snippet depth only) | **Mouse**, neuronal-conditional `Wwox` ablation | not establishable | 🔴 No PMC deposit; repo already records this paper as unobtainable (`next_scientist_scout_20260921.md:215`) | Myelination/oligodendrocyte program under **neuronal** WWOX loss, in the tissue the disease is in | **MEDIUM–HIGH (conditional)** | **NO** |
| **U3** | PMID 41984841, *PNAS* 2026, [DOI](https://doi.org/10.1073/pnas.2534844123) | **Jerusalem / Aqeilan** | RNA-seq **+ p63 ChIP-seq** (NovaSeq 6000) | **Mouse** conditional `Wwox`-KO epidermis / cSCC + human keratinocytes — 🔴 **non-CNS** | not establishable | 🔴 **No data-availability section at all** in the served PMC body; 0 occurrences of 9 deposit tokens. Ships 4 XLSX supplementary datasets | The **only WWOX ChIP-seq-adjacent object** found — a direct-binding map, if deposited | **LOW for CNS; MEDIUM as a mechanism contrast** | **NO** |
| **U4** | PMID 41090157, *Blood Neoplasia* 2025, [DOI](https://doi.org/10.1016/j.bneo.2025.100153) | **MD Anderson / Aldaz** (Hussain) | transcriptome + exome | **Mouse**, B-cell-specific `Wwox` deletion × VkMYC — 🔴 **non-CNS** | not establishable | 🔴 **No data-availability section** in the served body; 0 deposit tokens | WWOX-loss program in a third non-neural lineage | **LOW** | **NO** |
| **U5** | Cheng F *et al.* — human cerebellar **snRNA-seq + snATAC-seq multiome**, PMID 40235507 / `rs.3.rs-6264481`, and conference abstract [DOI](https://doi.org/10.1002/alz70855_105855) | Cleveland Clinic (Cheng) — 🔴 **not a WWOX group** | **single-nucleus multiome**, 103,861 nuclei, 431,834 peak-to-gene linkages | **Human**, AD/ADRD and **cognitively normal controls**, cerebellum + frontal cortex. 🔴 **Wild type for WWOX; adult; not developmental** | 103,861 nuclei; **Purkinje and granule clusters analysed separately** | 🔴 **Both PMC records return an EMPTY body.** Preprint host blocked | 🎯 **Q1's best structural fit** — the only object found that separates **Purkinje** from granule cells at scale and could carry a `WWOX` row | **HIGH (conditional on accession)** | **NO** |

### 3.3 Papers checked that deposited NOTHING — measured, not assumed

| # | PAPER | Finding |
|---|---|---|
| **N1** | PMID 34747138, *EMBO Mol Med* 2021, [DOI](https://doi.org/10.15252/emmm.202114599) — **the founding WWOX gene-therapy paper** | 🟢 **Read in full this act. There is no data-availability section, no accession, and no omics assay of any kind.** Every readout is imaging, EM, cell-attached electrophysiology or behaviour |
| **N2** | PMID 42422765 (2026) — **the second WWOX gene-therapy paper** | 🔴 SIBLING-ATTESTED, first-hand `S-body` in the repository: ***"Data and code availability: Not relevant."*** (`tx007_animal_flow_survival_validity_20260922.md:694`, `:733`) |
| **N3** | PMID 36828035, *Prog Neurobiol* 2023 — `Wwox^P47T` knock-in | 🟢 **Read this act. Bulk RNA-seq EXISTS** — Methods §4.14: *"RNA was isolated from HPC, PFC, (parietal) CTX, **and CB**"*, `n = 5` mice/group (2 M, 3 F), 150–280 d, ScriptSeq v2, 76 nt PE HiSeq3000, ~40 M tags/sample. 🔴 **No data-availability statement and no accession anywhere on the served surface** |
| **N4** | Suzuki / Tochigi — the `lde` rat | 🔴 **No transcriptomic deposit reachable.** The one PubMed hit for the group + transcriptome query is the **Genoa** paper, whose molecular figure is **Łódź's `GSE126075`** |
| **N5** | Chang / NCKU | No omics deposit surfaced in any of the four PubMed sweeps. Repo-attested: their reachable corpus is biochemical, and one flagship is *"5,029 bytes of deposit"* with no full body (`chang_ncku_wave1_20260920.md:27`) |

### 3.4 🔴 The most striking single finding in the census, and it is NOT a deposit

**A `Wwox^P47T/P47T` CEREBELLAR bulk RNA-seq was generated and appears never to have been reported.**

- Methods §4.14 names four regions: `HPC, PFC, (parietal) CTX, and CB`.
- Results §2.8 is titled *"…in **forebrains** of Wwox P47T mice"* and reports DEG counts for **exactly three**: PFC 425, CTX 363, HPC 1508.
- Every downstream analysis named in the Results — BRETIGEA cell-type estimation, GSEA, IPA upstream regulators — is reported *"in all three tissues (HPC, PFC, CTX)"*.
- 🔴 **The cerebellar arm is collected in the Methods and absent from the reported Results.** ⚠️ **Bound:** the extractor strips figure and table content, so I **cannot exclude** that the CB data appear in a figure panel or a supplementary table. What I can say is that **no CB transcriptome result appears in the running text**, and that the section heading itself says *forebrains*.

**Why this matters:** the laboratory's cerebellar frontier is blocked on the absence of any cell-type- or
region-resolved cerebellar WWOX measurement in a disease genotype. Here is a **named-allele cerebellar
transcriptome, with n=5 per arm, that already exists.** 🔴 **And it is NOT a reanalysis opportunity**, because
no accession exists to reanalyse: it is a `HUMAN_REQUIRED` contact, and it stays frozen (§ 10).

---

## § 4 · ACCESS-VERIFICATION RESULTS — and exactly what I could not check

| Accession / object | What I attempted | Result |
|---|---|---|
| `GSE156243` | `curl` to the GEO accession viewer | ⚫ `CONNECT tunnel failed, response 403` — logged by the proxy itself |
| `GSE156243` | `WebFetch` to the same URL | ⚫ `EGRESS_BLOCKED` |
| Any ArrayExpress/BioStudies record for `WWOX` | `WebFetch` + `curl` | ⚫ `EGRESS_BLOCKED` / `HTTP:000` |
| Any PRIDE / ProteomeXchange record for `WWOX` | `curl` to PRIDE v3 API; WebSearch | ⚫ API blocked; WebSearch returned **only documentation about PRIDE**, no WWOX dataset |
| Any ENA study for `WWOX` | `curl` to the ENA portal API | ⚫ `HTTP:000` |
| Cross-repository index (OmicsDI) and DOI registry (DataCite) | `WebFetch` ×2 | ⚫ `EGRESS_BLOCKED` ×2 |
| `GSE126075`, `GSE117387`, `GSE193659`, `GSM8002943`–`60` | — | ⚫ **Not attempted individually**: the surface was already proven blocked on `GSE156243`. Repeating a proven-blocked call is not a measurement |

🔴 **Therefore: 0 of 5 named accessions (§ 3.1) verified as resolving. 0 of 5 unobtainable accessions
(§ 3.2) obtained. `ACCESS STATUS` for every row in this census is `NOT VERIFIED`, and I do not infer open,
controlled, registration-gated or withdrawn status for any of them.**

⚠️ **What `NOT VERIFIED` does and does not mean.** It does **not** mean "probably absent". `GSE156243`,
`GSE126075`, `GSE193659` and `GSE117387` are each attested inside this repository by a reader who had the
paper in front of them, and `GSE193659` is additionally named **in the published abstract** of PMID 37519886
(*"deposited in the Gene Expression Omnibus database under the GSE193659 record"* — 🟡 abstract-depth, but an
abstract is a published assertion by the authors even though it is not a read). The unverified quantity is
**resolution**: whether the record exists today, what licence it carries, and what is inside it.

---

## § 5 · RANKED REANALYSIS OPPORTUNITIES

Ranked on `SCIENTIFIC VALUE × INFORMATION GAIN × EXECUTABILITY × COMMUNITY VALUE ÷ MARGINAL COST`.
🔴 **Executability is the term that dominates and it is near zero for every row, because no accession was
verified to resolve from here.** The ranking is therefore a ranking of *what to try first when a session with
repository egress exists*, not a claim that any of it is executable tonight.

### R1 — `GSE126075`: the human neural WWOX-perturbation CAGE object nobody here has opened

| Field | Value |
|---|---|
| **GROUP** | Łódź / Bednarek (Kośla) |
| **EXISTING ASSET** | `GSE126075` — CAGE over 4 arms: human hNPC ± `shWWOX`, undifferentiated and 14-day differentiated |
| **OPEN QUESTION** | Does WWOX loss in **human neural** cells change **which promoter/TSS is used**, not merely how much transcript there is — and is the effect **stage-gated**, collapsing as cells differentiate? |
| **MINIMAL FOLLOW-UP** | Download the deposited CAGE tag clusters; recompute TSS-cluster usage per arm; test the stage interaction. Desk-only |
| **NEW ANIMALS?** | **NO** |
| **INFORMATION GAIN** | **MEDIUM–HIGH.** The repository holds this accession **only as an attribution label**; it has never established what is in it, and a 5′-end assay answers a question no other WWOX object in this census can pose |
| **COST / COMPLEXITY** | Desk-hours, zero spend — **once** the accession resolves |
| **WHAT IT COULD CHANGE** | It would give the first *human neural* WWOX-perturbation promoterome, and would test the paper's own striking asymmetry (109 vs 4 enriched sets) as a **stage-gating** claim rather than a described curiosity |
| **THE ONE QUESTION NOTHING CHEAPER ANSWERS** | Whether WWOX loss shifts **TSS choice** in human neural cells. No bulk 3′ RNA-seq object in this census can see that |
| **🔴 WHAT IT WOULD NOT ANSWER** | Nothing about any **patient allele** — this is shRNA knockdown. Nothing about **splicing** — CAGE reads 5′ ends. Nothing about **protein**. And 🔴 **the paper states no replicate n per arm**, so the reanalysis may find it has no error model at all, which is itself the first thing to check |

### R2 — `GSE156243`: re-opened for the questions `TX001` did not ask

| Field | Value |
|---|---|
| **GROUP** | Jerusalem / Aqeilan (Steinberg) |
| **EXISTING ASSET** | `GSE156243` — WT n=2 vs engineered `WWOX`-KO n=4 cerebral organoids, week 15 |
| **OPEN QUESTION** | What is the expression status, in a **human WWOX-null neural** object, of the **WWOX-independent downstream nodes** the rescue census enumerated — and does cell-type deconvolution of the KO organoid reproduce the neural-population shift the paper claims from imaging? |
| **MINIMAL FOLLOW-UP** | Pull the deposited counts; run deconvolution; read out the named downstream nodes. Desk-only |
| **NEW ANIMALS?** | **NO** |
| **INFORMATION GAIN** | **MEDIUM.** The object is already held and already partly characterised; this is incremental, not new territory |
| **COST / COMPLEXITY** | Desk-hours |
| **WHAT IT COULD CHANGE** | It could convert several `NOT ASSAYED` cells in the downstream-rescue census into measurements, at zero marginal cost |
| **THE ONE QUESTION NOTHING CHEAPER ANSWERS** | Whether the downstream rescue nodes are even **expressed** in a human WWOX-null neural tissue — a precondition every rescue hypothesis silently assumes |
| **🔴 WHAT IT WOULD NOT ANSWER** | Nothing allele-specific (`tx001` N-18 is definitive: **zero molecules** of any splice-allele transcript). Nothing cerebellar — organoids are forebrain. Nothing about vector arrival. And `n=2 vs 4` with raw `P<0.01` selection is a weak error model for any new claim |

### R3 — the Nascimento postnatal human SVZ snRNA-seq (`GSM8002943`–`GSM8002960`)

| Field | Value |
|---|---|
| **GROUP** | Nascimento *et al.* — 🔴 **not a WWOX group**; WWOX would be an incidental gene in their object |
| **EXISTING ASSET** | 18 human postnatal snRNA-seq samples, 23 GW–27 y, including the EC stream |
| **OPEN QUESTION** | 🎯 **Q1, partially**: what is `WWOX` abundance across human postnatal neural cell types? |
| **MINIMAL FOLLOW-UP** | 🔴 **Not the raw data.** The repository already identified the cheaper route: **Supplementary Tables 4/5/6 are free DE-gene tables** — read the `WWOX` row. That needs no accession at all |
| **NEW ANIMALS?** | **NO** |
| **INFORMATION GAIN** | **MEDIUM**, and **bounded**: absence of `WWOX` from a DE table is `NOT_TESTED_OR_NOT_SIGNIFICANT`, **never** non-expression |
| **COST / COMPLEXITY** | Near-zero for the supplement route |
| **WHAT IT COULD CHANGE** | It would be the first **human postnatal** cell-type-resolved WWOX datum in the model |
| **THE ONE QUESTION NOTHING CHEAPER ANSWERS** | Whether `WWOX` is even in the object's ~21,563-gene feature universe — which the repository correctly flags as the first thing to test |
| **🔴 WHAT IT WOULD NOT ANSWER** | 🔴 **No cerebellum, no Purkinje cell, no oligodendrocyte-vs-neuron contrast of the kind Q1 asks for**, and Table 5 silently contains 50–79-y adult cortex, so a `WWOX` row read from it is **not** a postnatal statement |

### R4 — the Cheng human cerebellar single-nucleus multiome

| Field | Value |
|---|---|
| **GROUP** | Cleveland Clinic / Cheng — 🔴 **outside the WWOX field entirely** |
| **EXISTING ASSET** | 103,861 nuclei, snRNA-seq **+** snATAC-seq, human cerebellum and frontal cortex, **Purkinje and granule clusters analysed separately**, 431,834 peak-to-gene links |
| **OPEN QUESTION** | 🎯 **Q1 at the cerebellum**: is `WWOX` expressed in **human Purkinje cells**, and does it differ from granule cells? |
| **MINIMAL FOLLOW-UP** | One query of the deposited object for the `WWOX` row per cluster |
| **NEW ANIMALS?** | **NO** |
| **INFORMATION GAIN** | **HIGH if it resolves** — it would be the first Purkinje-resolved WWOX measurement using an actual Purkinje **marker-defined cluster**, where the repository's only existing human cerebellar observation identifies a **layer**, not a cell |
| **COST / COMPLEXITY** | Minutes of analysis; 🔴 **blocked on an accession that does not exist in any surface I can reach** |
| **WHAT IT COULD CHANGE** | It would settle whether the Purkinje-layer IHC sentence the repository recovered has a transcriptomic correlate at cell-type resolution |
| **THE ONE QUESTION NOTHING CHEAPER ANSWERS** | Purkinje-vs-granule `WWOX` in **human** tissue, with marker-defined clusters |
| **🔴 WHAT IT WOULD NOT ANSWER** | 🔴 Everything about disease. The donors are **AD/ADRD and cognitively normal controls** — **adult, wild type for WWOX, not developmental.** A `WWOX` value here is a wild-type expression datum and says nothing about WOREE, SCAR12, any named allele, or any therapy. It also cannot separate transcript from protein |

### 🔴 Not ranked, because it is not a reanalysis opportunity: the `Wwox^P47T` cerebellar RNA-seq

The single highest-value object this census found (§ 3.4) — a named-allele cerebellar transcriptome, `n=5`
per arm, that appears unreported — **has no accession.** Reaching it requires contacting the authors. That
is `HUMAN_REQUIRED`, it stays `HUMAN_REQUIRED`, and I took no step toward it (§ 10). It is recorded here so
that it is **visible** to the operator, not so that it is actioned.

---

## § 6 · THE HONEST NEGATIVE, QUANTIFIED

**The field deposited very little, and this deployment can verify none of it.** The numbers:

| Quantity | Count |
|---|---|
| PubMed records returned by the four WWOX-omics sweeps (union, before triage) | ~**150** |
| Papers whose deposit status I examined **first-hand** this act | **5** (`PMC6730490`, `PMC8649866`, `PMC10835625`, `PMC13099603`, `PMC12517091`) — plus **2** retrieved and found to be **empty bodies** (`PMC11998783`, `PMC12734678`) |
| Papers whose deposit status is carried **SIBLING-ATTESTED** with file and line | **6** |
| WWOX-associated **named** accessions now in hand | **5** (`GSE126075`, `GSE156243`, `GSE117387`, `GSE193659`, `GSM8002943`–`8002960`) — 🔴 **4 of the 5 were already in the repository before tonight** |
| Genuinely **new** named accessions found by this census | 🔴 **ZERO** |
| Accessions **verified as resolving** | 🔴 **ZERO of 5** |
| Deposits found in **any repository other than GEO** — ArrayExpress, ENA, PRIDE, MassIVE, dbGaP, EGA, Zenodo, Dryad, figshare | 🔴 **ZERO**, and ⚠️ **this zero is worthless**: every one of those surfaces was `EGRESS_BLOCKED` or `HTTP:000`. **It is a statement about my network, not about the world.** It must not be recorded as evidence of absence |
| Papers examined first-hand that declare a deposit sentence | **1 of 5** (`PMC6730490`) — and 🔴 **its accession string is deleted by the extractor** |
| Papers examined first-hand with **no data-availability section at all** in the served body | **4 of 5** |
| WWOX-relevant deposits carrying a **real patient allele** | 🔴 **ZERO named.** The only candidate (U1, *Brain* 2026) has no obtainable accession |
| WWOX **proteomic / interactomic / ChIP / ATAC / methylome** deposits named anywhere | 🔴 **ZERO.** One ChIP-seq experiment exists (U3, PNAS 2026) with no obtainable accession |
| Deposits that address 🎯 **Q2** (separating vector **ARRIVAL** from **EXPRESSION** from **FUNCTION**) | 🔴 **ZERO — and this one is a strong, measured negative**, because both WWOX gene-therapy papers were checked directly: the 2021 paper has **no omics and no data-availability section at all** (read in full this act), and the 2026 paper states ***"Data and code availability: Not relevant."*** |

**The one-line version: eleven papers were checked at deposit level, one declares an accession in its served
body, that accession string is deleted by the extractor, and zero of the five accessions the laboratory now
holds could be verified to resolve.**

### 6.1 What this closes, cheaply

🟢 **The gene-therapy reanalysis direction is closed.** The laboratory's sharpest distinction — arrival vs
expression vs function — **cannot be attacked from any public deposit**, because the only two gene-therapy
papers in the field deposited nothing, and one says so explicitly. That direction should not be re-scouted.
The `A-f4` freezer question is not merely the blocker for the two frozen packets; **for this question class
it is the only route that exists.**

### 6.2 What I refuse to pad

I found no reason to add rows for TCGA/CCLE-based WWOX reanalyses (e.g. PMID 42589397, PMID 37519886's
survival arms). Those are **re-uses of third-party cancer cohorts**, they generate no WWOX-specific deposit,
the repository has already audited one of them and found its headline survival result fragile
(`CUTPOINT_ENDPOINT_DRIFT_GATE`, `framework/eval/learned_gates_registry.md:65`), and including them would
make a thin census look productive. **They are deliberately excluded.**

---

## § 7 · WHAT I COULD NOT VERIFY — exhaustive

1. 🔴 **That any accession resolves.** Zero of five. Every repository surface blocked (§ 4).
2. 🔴 **The access licence, embargo state or controlled/open status of every row.** Not one.
3. 🔴 **The accession for the 2026 *Brain* patient-organoid scRNA-seq (U1)** — the highest-value object in the census. No PMC deposit; publisher unreachable; WebSearch gave the title and not the accession.
4. 🔴 **The accession for the *Brain* 2021 neuronal-`Wwox` RNA-seq (U2)**, and **its sample structure** — the description *"whole cortex and hippocampus"* is 🟡 **WebSearch-snippet depth**, which is below abstract depth. It must be re-established from the paper before it is used.
5. 🔴 **The accession for the Cheng cerebellar multiome (U5)**, and therefore whether R4 is executable at all.
6. 🔴 **Whether PNAS 2026 (U3) and *Blood Neoplasia* 2025 (U4) deposited anything.** Their served PMC bodies contain no data-availability section; I cannot distinguish "not deposited" from "section not served".
7. 🔴 **Whether the `Wwox^P47T` cerebellar RNA-seq results appear in a figure panel or supplementary table.** The extractor strips figure and table content. I established only that **no CB transcriptome result appears in the running text** and that the Results heading says *forebrains*.
8. 🔴 **The replicate `n` per arm of `GSE126075`.** The paper states none in the served body.
9. 🔴 **Whether the Nascimento series accession exists.** Only per-sample `GSM` identifiers are in hand, at `author-code` depth, and none was resolved.
10. 🔴 **Everything about non-GEO repositories.** ArrayExpress, ENA, PRIDE, MassIVE, jPOST, dbGaP, EGA, Zenodo, Dryad and figshare were **never successfully queried**. The census is, by construction, **a GEO-shaped census recovered from paper bodies**.
11. ⚠️ **Whether the four PubMed sweeps have adequate recall.** `[All Fields]` does not index Methods, supplements or data-availability statements — the repository established this in a different context (`nascimento_accession_and_g372r_20260922.md:211`). A deposit belonging to a paper that never says "WWOX" in an indexed field is **invisible to this census**.
12. ⚠️ **The Aqeilan bench inventory** (hESC `WWOX`-KO, W-AAV rescue line, WOREE and SCAR12 patient iPSCs) is repo-attested from a **`partial_fulltext_read`** receipt. I did not re-verify it, and nothing here rests on it except context.

---

## § 8 · NOVELTY GRADE — conservative

### 🟡 **C — NOVEL CONNECTION**

**Why not B (`TRIVIAL INFERENCE`):** three results are not inferable from what the repository held.
(i) A **cerebellar** `Wwox^P47T` bulk RNA-seq, `n=5` per arm, exists in the Methods of a paper the repository
has read, and **no cerebellar result appears in its Results** — directly adjacent to the laboratory's
blocked cerebellar frontier. (ii) The **accession-deletion hazard was measured a second time, live**, in a
different paper from the one the repository documented, establishing it as a **property of the extraction
surface** rather than an incident. (iii) The **gene-therapy deposit direction is closed by direct
measurement** — the 2021 paper was read end to end and has no omics and no data-availability section at all,
which the repository did not know; it only knew the 2026 paper's *"Not relevant."*

**Why not D (`NOVEL TESTABLE HYPOTHESIS`):** nothing here proposes a new mechanism or a falsifiable claim
about WWOX biology. R1's stage-gating question is **re-description of the source paper's own reported
numbers**, not a new hypothesis. The census is an instrument-and-availability result.

**Why not E or F:** no experiment is generated (the one experiment-shaped object, § 3.4, is unreachable and
`HUMAN_REQUIRED`), and no therapeutic space is expanded.

**The connection that earns the C:** the laboratory's own preference order ranks `REANALYSIS` first, and the
two most mature packets are frozen on a freezer question. This file establishes that **the top-ranked class
is very nearly empty for this field** — and, more sharply, that the class is empty **precisely where the
laboratory most needs it**: for allele-carrying human neural data and for the arrival/expression/function
distinction. That is a structural fact about the field, not about the search.

---

## § 9 · SOURCE ATTRIBUTION

*According to PubMed*, and with every DOI given as a link, as that service requires.

### 9.1 Read directly this act
- **PMID 31543760** · PMC6730490 · Kośla K, Płuciennik E, Styczeń-Binkowska E, Nowakowska M, Orzechowska M, Bednarek AK. *The WWOX Gene Influences Cellular Pathways in the Neuronal Differentiation of Human Neural Progenitor Cells.* Front Cell Neurosci 2019. [DOI](https://doi.org/10.3389/fncel.2019.00391) → the deposit behind `GSE126075`
- **PMID 34747138** · PMC8649866 · Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI. *Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes.* EMBO Mol Med 2021. [DOI](https://doi.org/10.15252/emmm.202114599) → **no deposit**
- **PMID 36828035** · PMC10835625 · Hussain T *et al.*, Aldaz CM. *WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice phenocopying human SCAR12.* Prog Neurobiol 2023. [DOI](https://doi.org/10.1016/j.pneurobio.2023.102425) → **RNA-seq incl. CB; no accession**
- **PMID 41984841** · PMC13099603 · Bidany-Mizrahi T *et al.*, Aqeilan RI. PNAS 2026. [DOI](https://doi.org/10.1073/pnas.2534844123) → RNA-seq + ChIP-seq; **no data-availability section served**
- **PMID 41090157** · PMC12517091 · Hussain T *et al.*, Aldaz CM. Blood Neoplasia 2025. [DOI](https://doi.org/10.1016/j.bneo.2025.100153) → transcriptome + exome; **no data-availability section served**
- **PMID 40235507** · PMC11998783 · Cheng F *et al.* [DOI](https://doi.org/10.21203/rs.3.rs-6264481/v1) and PMC12734678 [DOI](https://doi.org/10.1002/alz70855_105855) → **abstract-depth only; empty bodies**

### 9.2 Referenced, not read directly this act
- **PMID 34268881** · PMC8350905 · Steinberg DJ *et al.*, Aqeilan RI. EMBO Mol Med 2021. [DOI](https://doi.org/10.15252/emmm.202013610) → `GSE156243`
- **PMID 42397075** · Steinberg DJ, Zonca A, … Davila-Velderrain J, Aqeilan RI. *Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids.* Brain 2026. [DOI](https://doi.org/10.1093/brain/awag239) → 🟡 title at WebSearch depth
- **PMID 33914858** · Repudi S *et al.* Brain 2021. [DOI](https://doi.org/10.1093/brain/awab174) → 🟡 WebSearch-snippet depth
- **PMID 42422765** · 2026 gene-therapy paper → 🔴 SIBLING-ATTESTED only
- **PMID 32581702** · PMC7300205 · Iacomino M *et al.*, Striano P, Suzuki H, Salpietro V. Front Neurosci 2020. [DOI](https://doi.org/10.3389/fnins.2020.00644) → re-uses `GSE126075`
- **PMID 30082886** · PMC6079009 · Abdeen SK *et al.*, Aqeilan RI. Cell Death Dis 2018. [DOI](https://doi.org/10.1038/s41419-018-0896-z) → `GSE117387`
- **PMID 37519886** · PMC10373930 · Kołat D *et al.*, Bednarek AK. Front Genet 2023. [DOI](https://doi.org/10.3389/fgene.2023.1214968) → `GSE193659`, named in the abstract
- **PMID 38122823** · Nascimento *et al.* → `GSM8002943`–`GSM8002960`, `GSE186538`, `GSE199762` (the last two **not theirs**)
- **PMID 42589397** · PMC13467099 · Hammouz RY, Maciejek K, Bednarek AK. Int J Mol Sci 2026. [DOI](https://doi.org/10.3390/ijms27156740) → TCGA re-use; **deliberately excluded** from the census (§ 6.2)

### 9.3 Accessions named in this file
`GSE126075` · `GSE156243` · `GSE117387` · `GSE193659` · `GSM8002943`–`GSM8002960` · `GSE186538` · `GSE199762` · `GSE31684`
🔴 **Every one is carried from a paper body or from a repository attestation. None was resolved. None was guessed, constructed or pattern-matched.**

---

## § 10 · STANDING LINE — every contact here is `HUMAN_REQUIRED`, and I took no external action

🔴 **I contacted nobody.** I sent no email, opened no message, filled in no data-access request, submitted no
repository application, represented no foundation, and requested no material or data from any author, group
or institution. I read public web search results and public bibliographic records; that is the entirety of
my external activity.

**Every contact implied anywhere in this file is `HUMAN_REQUIRED` and remains so**, specifically and without
exception:

- Any request to **Aldaz / MD Anderson** for the `Wwox^P47T` **cerebellar** RNA-seq of § 3.4 — the highest-value object found, and the one most likely to tempt action. `HUMAN_REQUIRED`. **Frozen.**
- Any request to **Aqeilan / Jerusalem** for the 2026 *Brain* patient-organoid scRNA-seq accession (U1), the 2021 *Brain* accession (U2), or the PNAS 2026 deposit (U3). `HUMAN_REQUIRED`.
- Any request to **Bednarek / Łódź** regarding `GSE126075`'s replicate structure. `HUMAN_REQUIRED`.
- Any request to **Cheng / Cleveland Clinic** for the cerebellar multiome accession or access terms (U5). `HUMAN_REQUIRED`.
- Any **controlled-access application** to dbGaP, EGA or any equivalent, for any row. `HUMAN_REQUIRED`.
- Any contact with **Genoa / Striano / Zara**, **Chang / NCKU**, **Suzuki / Tochigi**, or **Nascimento *et al.***. `HUMAN_REQUIRED`.

🔴 **Nothing in this file is medical advice, and nothing in it authorises an external action.**

---

## Appendix · How to check this file cheaply

| Claim | Cheapest independent check |
|---|---|
| The accession string is deleted from `PMC6730490` | Fetch `PMC6730490` through the same PubMed surface and search for `accession number.` — the sentence ends at a full stop with no identifier |
| The `Wwox^P47T` paper collected cerebellum | Fetch `PMC10835625`, read Methods §4.14: *"RNA was isolated from HPC, PFC, (parietal) CTX, and CB"* |
| No cerebellar result is reported | Same body, Results §2.8 heading — *"in forebrains of Wwox P47T mice"* — and the three DEG counts 425 / 363 / 1508 |
| The 2021 gene-therapy paper has no deposit | Fetch `PMC8649866` and search for `availab` — it occurs nowhere in the body |
| The repositories are unreachable | `curl -sS -o /dev/null -w "%{http_code}" "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243"` → `000`, with `CONNECT tunnel failed, response 403` |

---

# 🔴 CORRECTION — appended by the Orchestrator, 2026-09-22, same session

> **This file's most striking finding is WRONG, and the correction is recorded here rather than by
> editing the claim in place, so that the reasoning and its refutation both stay legible.**

## What this file claimed

> *"A `Wwox^P47T/P47T` **CEREBELLAR** bulk RNA-seq exists and appears never to have been reported.
> PMID 36828035 … Methods §4.14: `"RNA was isolated from HPC, PFC, (parietal) CTX, **and CB**"` …
> Results §2.8 is titled `"…in **forebrains**…"` and reports only PFC/CTX/HPC."*

## What is actually the case

🟢 **Verified by the Orchestrator at 🟢 direct-read depth this act** — `PMC10835625` fetched through
PubMed, **60,088 characters**, after Scientist 5 reached the same text independently by a different
route. According to PubMed, PMID 36828035, [DOI](https://doi.org/10.1016/j.pneurobio.2023.102425):

1. 🎯 **The paper's TITLE is** *"WWOX P47T partial loss-of-function mutation induces epilepsy,
   progressive neuroinflammation, and **cerebellar degeneration** in mice phenocopying human
   SCAR12."*
2. **Results §2.9 is a dedicated cerebellar section**, *"Transcriptome profiling of Wwox P47T
   cerebella provides further evidence of dysfunction"*: *"EdgeR analysis identified a total of
   **1059 DEGs (376 genes upregulated, 683 genes downregulated)** comparing both groups at an
   FDR < 0.01."* With IPA, GSEA (lipid metabolism and ROS topmost) and a separate cytokine qRT-PCR arm.
3. **And Purkinje cells are not merely sampled, they are the phenotype:** *"Since [these] mice
   displayed motor abnormalities along with evidence of significant **cerebellar atrophy and PC
   degeneration**, we sought to evaluate the transcriptional changes associated with WW domain LoF
   in CB."*

## Why the error happened, and what survives

**The observation was true; the inference was not.** §2.8 *is* titled "forebrains" and *does* report
only three regions. What the reasoning missed is that §2.8 opens *"we **first** performed…"* — it is
the first of two sections by design, and §2.9 is the second. 🔴 **An absent section heading in a
served text was read as an absent experiment.** That is the same false-negative mode this session
recorded twice elsewhere tonight: *treating a surface one did not reach as evidence that nothing was
there.*

**What survives unchanged:** everything else in this file. The census counts, the `NOT VERIFIED`
access statuses, the egress-blockage evidence, the measured negative that **neither WWOX
gene-therapy paper deposited anything**, and the conclusion that the reanalysis class is nearly
empty — none of these rest on the `36828035` lead, and the lead was correctly **frozen and
deliberately NOT ranked** as an opportunity, which limited the damage to this one section.

🎯 **And the correction is worth more than the claim it replaces.** Put beside Scientist 5's
independent read of `PMID 18676360` — whose entire sampling frame is blood → reproductive organ
weights → testes → pituitary, with **cerebellum, brainstem, cord, nerve and muscle all absent** —
the real result is a **sampling asymmetry between alleles**, not a field-wide blind spot:

| Allele | Cerebellar sampling |
|---|---|
| **`lde/lde` rat** | 🔴 never sectioned — confirmed independently twice |
| **`P47T` mouse** | 🟢 cerebellum is the title subject; atrophy, PC degeneration, 1059-DEG transcriptome |

⚠️ **Consequence for `A-f4`, stated carefully.** The custody unknown is **not** the blocker for
*"does WWOX loss damage the cerebellum"* — that has a published answer in `P47T`. It may still gate
the **TX-007** question, which is **vector arrival at Purkinje cells at therapeutic dose** — a
different question that a degeneration phenotype does not answer. The two must not be merged.

**The one real methodological caveat in `36828035`**, which replaces the withdrawn claim: §2.8 reads
*cerebellar biofunctions* out of **parietal cortex** GSEA — a cross-region inference that should be
labelled as such wherever it is used.

## 🔴 Addendum to the correction — the repository already held the answer, and that is the lesson

No fetch was needed to catch this. **The `P47T` cerebellar phenotype was already in the repository,
in four places**, and each contradicts the withdrawn lead on its own:

| Where | What it already said |
|---|---|
| `research/discovery_ledger_current.md:2375` | `Wwox^P47T/P47T` → *"epilessia ad esordio adulto, **neurodegenerazione cerebellare**, atassia, neuroinfiammazione progressiva"* |
| `research/discovery_ledger_current.md:217` | *"cervelletto: astro-microgliosi progressiva + **perdita Purkinje** (`Wwox^P47T`)"* |
| `research/discovery_ledger_current.md:134` | proposes an experiment in `P47T` mice measuring *"rallenta la **perdita di Purkinje**"* — i.e. the laboratory was already designing around this phenotype |
| `research/commit_candidates/CC-20260826-CLAIM006-HARDENING-01.md:64,144` | audits **Fig. 9** by name — *"…further evidence of severe dysfunction in Wwox P47T **cerebella**"* — and already lodges the sharper caveat that the cerebellar inflammation measurement *"has **no declared age**"* and *"cannot support any progression claim in the cerebellum"* |

⇒ 🎯 **The cheapest prevention was the mandatory step, not a better tool.** `enumerate_baseline_before_scoring`
run over `research/` would have surfaced all four rows before any conclusion was formed, and the
lead would never have been written. The failure was not one of retrieval, of egress, or of the
served surface — **it was skipping the baseline on one specific claim** while performing it
faithfully everywhere else in this file.

⚠️ **And the same discipline bounds this correction too.** Because the phenotype was already held,
**nothing in the working model changes**, and none of tonight's other findings rest on the withdrawn
lead. What is genuinely new from the full read is narrower and is recorded as such: the **1059-DEG
cerebellar transcriptome of §2.9**, the **cross-region inference in §2.8**, and — already lodged
independently by `CC-20260826-CLAIM006-HARDENING-01` — that the cerebellar inflammation arm carries
**no declared age**.
