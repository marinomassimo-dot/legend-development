# Does a single-cell, fluorescence- or FACS-readable reporter of WWOX activity already exist?

**A methods-and-reagents census — assay technology, not biology.**

**Date:** 2026-09-21 · **Actor:** Scientist A · **Mode:** READ-AND-REPORT.
Read-only toward every canonical file and every ledger. No registry edited, no `*_current.md`
touched, no `BATCH_COMMIT`, no commit candidate, no receipt written, nothing committed or pushed.

**Assignment source:**
[`mave_portability_to_wwox_20260921.md`](mave_portability_to_wwox_20260921.md) § 6.B/6.C
(requirements `F1` and `F2`) and
[`missense_rescue_methodology_census_20260921.md`](missense_rescue_methodology_census_20260921.md).

**The question this file answers, and only this one:**
> Does any single-cell, fluorescence- or FACS-readable reporter of WWOX activity, WWOX protein
> level, or a WWOX-dependent molecular event already exist anywhere in the published literature —
> and if not, what is the nearest existing thing?

**Bibliographic source of every record below: PubMed.** DOI links are given per record, as the
retrieval tool's terms require. Web results are marked as such and carry their URL.

> ⚠️ **Nothing here is medical advice.** Non-canonical research-layer file.
> 🔴 **No sensor is proposed and no MAVE programme is proposed.** Both are materially new research
> programmes and the Operator's decision. This file establishes what exists and what the gap is,
> and stops there.
> 🔴 **Almost everything below is ABSTRACT-LEVEL.** Exactly two bodies were retrieved and read
> (§ 1). Every other row is a statement about a PubMed abstract, never about a paper's contents.

---

## 1 · ARTEFACT MANIFEST — the two full texts, persisted verbatim BEFORE analysis

| # | Paper | Path | Bytes | Chars | sha256 |
|---|---|---|---|---|---|
| **R1** | PMID `42523332` / PMC13405132 — Aragon-Ramirez WS *et al.*, *bioRxiv* 2026, *"Golgi CATCHR complexes function as organizing hubs for vesicle tethering and fusion"* — [DOI](https://doi.org/10.64898/2026.06.16.732723) | `files/fulltext/PMID42523332_PMC_MCPtext.txt` | **50 075** | **50 049** | `7f2da97ba52357412af1e8f5e6b8c746e305b91197f4cad98ebe3af89f14bcbd` |
| **R2** | PMID `41228229` / PMC12610808 — *Cancers* 2025, *"The Role of WWOX in Cancer Progression: Mechanisms and Therapeutic Potential"* — [DOI](https://doi.org/10.3390/cancers17213435) | `files/fulltext/PMID41228229_PMC_MCPtext.txt` | **40 019** | **39 965** | `6995106bd59bda3e81d9481542880986a91df85b24ab6a93521fc305a720b840` |

R1's abstract was persisted separately as `files/fulltext/PMID42523332_PMC_MCPabstract.txt`
(1 703 chars).

### 1.1 🔴 Retrievability was established by FETCHING, and the measured lengths are above

Neither body's retrievability was inferred from a flag. `get_copyright_status` was not consulted
for either; the fetch was attempted directly and the character counts are the measured result.
**R1 is a bioRxiv preprint that delivered 50 049 characters. R2 delivered 39 965.**

### 1.2 🔴 Fidelity note on R2 — declared, not hidden

R1's payload was written to disk by the tool and copied byte-for-byte. **R2's payload was returned
inline rather than to a file, so its persisted body was transcribed from the returned payload in
this session.** The transcription is faithful to the returned text with three declared
normalisations forced by the shell heredoc: typographic apostrophes rendered as `'` (affects
`5-aza-2'-deoxycytidine`, `3'-UTR`, `WWOX's`, `MYC's`), and the CJK-compatibility numeral in
`LC3-Ⅱ` rendered as `LC3-II`. **No word, sentence, number or ordering was altered.** Where R2 is
quoted below, the quote is reproduced from the returned payload. A reader who needs byte-identity
should re-fetch `PMC12610808`.

### 1.3 Extraction damage, stated before any count is offered

Both artefacts come from the same PMC-to-text route that this repository has repeatedly certified
as **stripping italics, superscripts, subscripts and reference lists**. In both bodies the
italicised gene symbol is visibly deleted mid-sentence — R2 reads *"Thegene is located in the
region of human chromosome 16q23.3-24.1"*, R1 reads *"the levels ofand"*. **Reference lists are
ABSENT from both.** Therefore:

> **ITALIC-CLASS COUNTS ARE INADMISSIBLE IN BOTH ARTEFACTS. ROMAN-CLASS COUNTS ARE ADMISSIBLE.**

`WWOX` survives in roman in both bodies (it is set roman as a protein name), so counts of `WWOX`
are roman-class and admissible. Counts of the italicised gene symbol are not offered anywhere in
this file. No figure panel was inspected; figure legends reproduced in body text are quoted where
used, and nothing is asserted from an image.

---

## 2 · VERDICT

> ## 🟠 **NEAREST-THING. No single-cell, FACS-readable WWOX activity reporter exists in the published literature, and no query run today found one.**
>
> **The nearest existing thing is a cell-surface lectin stain.** A 2026 bioRxiv preprint reports
> that WWOX knockdown causes N- and O-glycosylation defects detected as *increased plasma-membrane
> binding of the lectins HPA and GNL* — a WWOX-dependent molecular event displayed on the **outside
> of an intact, unfixed cell**, quantified **per cell**, using reagents that are routine
> flow-cytometry conjugates. **It was measured by microscopy in 30 cells, in one preprint, after
> siRNA knockdown, as a side observation in a Golgi-tethering paper — it is not a validated assay
> and nobody has put it on a cytometer.**
>
> Everything else that is genuinely fluorescent and genuinely per-cell (the NCKU FRET series) is
> ectopic, microscopy-bound and not poolable; everything else that is genuinely
> WWOX-perturbation-validated (the Wnt/β-catenin reporters) is bulk luciferase and destroys the cell.

**And one correction to the inherited roadmap, which is the most consequential thing in this file:**

> 🔴 **`F4` was recorded as ADVERSE and that assessment is now wrong in both of the two nearest
> candidates.** `mave_portability_to_wwox_20260921.md` § 6.B states *"WWOX appears to act positively
> in its characterised interactions, so loss would most likely **remove** a signal."* **Both
> nearest-things are gain-on-loss.** WWOX knockdown **increases** lectin binding (R1); WWOX
> knockdown **stimulates** Wnt/β-catenin transcriptional activity (PMID `19465938`). Both are the
> same easy sorting direction as TSC2's pS6, for the same reason — on those two axes WWOX is a
> **negative** regulator. See § 8.

---

## 3 · THE QUERIES, verbatim, with result counts

**A negative is only as good as the search that produced it.** Every query below was issued today.
Counts are `total_count` as returned by the tool, not the number of records inspected.

### 3.1 PubMed (`mcp__PubMed__search_articles`)

| # | Query string, verbatim | Filter | `total_count` |
|---|---|---|---|
| Q1 | `WWOX AND (GFP OR fluorescent OR mCherry OR HaloTag OR fusion protein)` | — | **49** |
| Q2 | `WWOX AND (substrate OR oxidoreductase OR enzymatic activity OR catalytic)` | — | **486** |
| Q3 | `WWOX short-chain dehydrogenase reductase substrate identification` | — | **1** |
| Q4 | `WWOX AND (BiFC OR bimolecular fluorescence complementation OR FRET OR BRET OR NanoBiT OR split luciferase OR proximity ligation)` | — | **6** |
| Q5 | `WWOX substrate product enzyme reaction identified` | `date_from=2021` | **0** |
| Q6 | `WWOX AND (luciferase reporter OR reporter assay OR TCF/LEF OR TEAD OR HIF-1 OR AP-1)` | — | **31** |
| Q7 | `WWOX AND (flow cytometry OR FACS OR intracellular staining OR cell sorting)` | — | **36** |
| Q8 | `WWOX AND (degron OR protein stability reporter OR GFP-P2A-mCherry OR ratiometric OR half-life)` | — | **4** |
| Q9 | `WWOX Wnt beta-catenin TCF reporter Dishevelled` | — | **0** ⚠️ |
| Q10 | `WWOX biosensor OR (WWOX AND live-cell imaging quantitative single cell)` | — | **0** |
| Q11 | `WWOX Wnt signaling pathway inhibition` | — | **6** |
| Q12 | `WWOX antibody validation specificity knockout-validated` | — | **0** ⚠️ |
| Q13 | `WWOX glycosylation Golgi lectin` | — | **0** |
| Q14 | `WWOX AND (split-GFP OR protein-fragment complementation OR NanoLuc OR HiBiT OR tandem fluorescent timer)` | — | **0** |
| Q15 | `WWOX review 2025 function substrate remains unknown enzymatic` | `date_from=2024` | **0** ⚠️ |
| Q16 | `WWOX SDR domain catalytic activity NAD steroid metabolism` | `date_from=2012` | **0** ⚠️ |
| Q17 | `The Role of WWOX in Cancer Progression: Mechanisms and Therapeutic Potential[Title]` | — | **1** |
| Q18 | `WWOX[Title/Abstract] AND (deep mutational scanning[Title/Abstract] OR variant effect[Title/Abstract] OR multiplexed[Title/Abstract] OR VAMP-seq[Title/Abstract])` | — | **0** |
| Q19 | `WWOX AND HaloTag` | — | **0** |
| Q20 | `WWOX high-content imaging high-throughput screen quantitative immunofluorescence` | — | **0** ⚠️ |

⚠️ **Q9, Q12, Q15, Q16 and Q20 are over-conjuncted queries and their zeros are worthless as
evidence.** PubMed's translator ANDed every content word, so Q12 required the literal token
`knockout-validated` and Q15 required the literal token `2025` in the record. **These five zeros
are instrument readings about query construction, not statements about the literature**, and none
of the negatives in § 7 rests on any of them. The load-bearing zeros are **Q10, Q13, Q14, Q18 and
Q19**, all of which are short, correctly-translated conjunctions.

### 3.2 WebSearch

| # | Query string, verbatim |
|---|---|
| W1 | `WWOX physiological substrate identified oxidoreductase enzyme activity 2025 2026` |
| W2 | `anti-WWOX antibody ABN413 flow cytometry intracellular staining validated` |
| W3 | `"WWOX" substrate still unknown 2024 2025 review "yet to be" enzyme oxidoreductase function` |
| W4 | `OpenCell WWOX split-mNeonGreen2 endogenous tagging library HEK293T` |

🔴 **W3 produced a misattributed quotation and it was caught by reading the paper.** W3's synthesis
asserted that a 2025 review states *"the true substrate(s) of this oxidoreductase remain to be
identified"*, and offered PMC12610808 among its links. **PMC12610808 was then fetched and read in
full: the string `substrate` occurs ZERO times in its body.** The sentence is not in that review.
It is carried here as an **unsourced web synthesis, attributable to no paper this session read**,
and it is used nowhere as evidence. See § 5.4. **This is the second search-layer false attribution
this repository has recorded today's class of; a web snippet is not a source.**

---

## 4 · CENSUS TABLE, per search line

Column meanings, kept strict because this is where a false positive is most likely:

- **single-cell?** — does the assay produce one number per cell, or one number per well/lysate?
- **quantitative?** — is that number a graded measurement, or a categorical/localisation call?
  🔴 **A localisation study is NOT a single-cell quantitative assay**, and is scored `NO` here.
- **pooled-compatible?** — can a library of genotypes be mixed in one vessel, sorted on the signal,
  and the genotype recovered from the sorted cells? This is the hard one and almost everything fails it.
- **Held by LEGEND** — reported by BOTH methods: `registry_records.py get --pmid` (surfaces:
  the two registries, the queue, the ledgers) **and** `grep -rn "<PMID>" --include=*.md
  disease-models/` (everything else, including `analysis/` and `batch_queue.md`, and uncommitted state).

### 4.1 Search line 1 — WWOX fluorescent fusions / tagged constructs

| PMID | What it actually offers | single-cell? | quantitative? | pooled-compatible? | Retrievability tested how | Held by LEGEND (both methods) |
|---|---|---|---|---|---|---|
| `42523332` | **myc-WWOX**, not a fluorescent fusion. Used *because* commercial anti-WWOX antibodies failed in IF. Colocalisation with COG8, LQ=0.27, n=20, 3 cells. **A localisation study.** [DOI](https://doi.org/10.64898/2026.06.16.732723) | NO (3 cells, colocalisation) | NO | NO | **FETCHED — 50 049 chars** (§ 1) | `registry_records.py`: **NO RECORD MATCHED**. `grep`: **FOUND** — `registries/batch_queue.md:459`, status `unmatched`. 🔴 The two methods disagree and the grep is right. |
| `24968878` | WWOX cDNA transfection in U266 myeloma; MeSH carries `Green Fluorescent Proteins`, i.e. GFP as a **vector/transfection marker**. Readout is growth arrest and apoptosis. [DOI](https://doi.org/10.3892/ijmm.2014.1824) | NO | NO | NO | UNTESTED — not fetched | Not checked individually (screened out as a collision, see below) |
| `26458445` · `26070663` · `22869583` | **Keyword collisions.** All three are *fluorescence in situ hybridization* / cytogenetics of `WWOX` translocations. No protein fusion of any kind. [DOI](https://doi.org/10.11406/rinketsu.56.2056) · [DOI](https://doi.org/10.1101/gr.191247.115) · [DOI](https://doi.org/10.1158/0008-5472.CAN-12-0213) | n/a | n/a | n/a | UNTESTED | — |

**Line-1 result: no published GFP-WWOX, WWOX-GFP, mCherry-WWOX or HaloTag-WWOX construct used as a
per-cell quantitative abundance readout was found by Q1 or Q19.** `WWOX AND HaloTag` = 0 (Q19,
short conjunction, load-bearing). Of Q1's 49 records the fluorescence signal is dominated by FISH.

🔴 **A reagent's absence from PubMed is not its absence from the world.** Fluorescent WWOX
constructs almost certainly exist in Addgene deposits and in methods sections that PubMed does not
index at the abstract level, and this extractor strips reference lists where such deposits are
cited. **The honest statement is "no published quantitative single-cell use found by these
queries", not "none exists".**

### 4.2 Search line 2 — WWOX protein–protein interaction sensors

| PMID | What it actually offers | single-cell? | quantitative? | pooled-compatible? | Retrievability tested how | Held by LEGEND (both methods) |
|---|---|---|---|---|---|---|
| `27339895` | **Time-lapse FRET**, IκBα·ERK·WWOX, MOLT-4 T cells. Abstract reports the complex *"exhibits an increased binding strength by 1-2-fold after exposure to ionophore A23187/PMA for 15-24 h"*. [DOI](https://doi.org/10.1074/jbc.M116.716167) | **YES** | **YES** (weakly — fold-change in FRET) | **NO** — ectopic pairs, time-lapse microscopy, ratiometric with donor/acceptor controls | UNTESTED | `registry_records.py`: **MATCH** — `paper_registry_current.md:2693`, `literature_tracking_log_current.md:6061`. `grep`: **FOUND** — `batch_queue.md:198`, `catalogued only` |
| `27845895` | **Tri-molecular real-time FRET**, Smad4→WWOX→p53 and Smad4→Hyal-2→WWOX, hyaluronan-induced. [DOI](https://doi.org/10.18632/oncotarget.13268) | **YES** | YES (weakly) | **NO** | UNTESTED | `registry_records.py`: **MATCH** — `full_text_queue_current.md:3721` `[mention]`, *"not yet retrieved"*. `grep`: **FOUND** — `full_text_queue_current.md` `FT-073` body |
| `29581896` | *"Chasing the signaling run by tri-molecular time-lapse FRET microscopy."* Self-described **perspective review article** describing the FRET design. [DOI](https://doi.org/10.1038/s41420-018-0047-4) | YES | YES (weakly) | **NO** | UNTESTED | `registry_records.py`: **NO RECORD MATCHED**. `grep`: **FOUND** — `research/fulltext_dossiers/PMID31428585.md` ×3, incl. an explicit note that it *"has no receipt in this corpus"* and a recorded PMID-confusion correction. 🔴 Methods disagree; grep right. |
| `19918364` | WWOX–CREB interaction *"most strongly in the nuclei as determined by FRET analysis"*, rat DRG neurons after sciatic transection. **In a neuronal context** — the only one in this line. [DOI](https://doi.org/10.1371/journal.pone.0007820) | YES | YES (weakly) | **NO** — in vivo tissue | UNTESTED | `registry_records.py`: **NO RECORD MATCHED**. `grep`: **FOUND** — `batch_queue.md:139`, `unmatched` |
| `41984841` | **Proximity ligation assay (PLA)**, WWOX–p63, cSCC. *"proximity ligation assays together with biochemical and cellular analyses **support a close association**"* — the authors' own hedge, preserved. [DOI](https://doi.org/10.1073/pnas.2534844123) | **YES** (PLA puncta are per cell) | **YES** (puncta counts) | **NO** — fixed, permeabilised, ligation + rolling-circle amplification, imaging | UNTESTED | `registry_records.py`: **MATCH** — `paper_registry_current.md:6855`. `grep`: **FOUND** — dedicated dossier `research/fulltext_dossiers/PMID41984841.md` |
| `31315632` | p53/TIAF1/WWOX triad; PPIs by *"co-immunoprecipitation, FRET microscopy, and yeast two-hybrid"*. [DOI](https://doi.org/10.1186/s12964-019-0382-y) | YES (FRET part) | YES (weakly) | **NO** | UNTESTED | `registry_records.py`: **NO RECORD MATCHED**. `grep`: **FOUND** — `batch_queue.md:118`, `unmatched` |
| `32185845` | **Fluorescence anisotropy + ITC**, WWOX WW1 ± pTyr33 against a p73-derived peptide. *"the quantitative effect of phosphorylation on this specific interaction is determined here for the first time"*; binding affinity to p73 **decreases** when WWOX is phosphorylated. **Purified/synthetic material.** [DOI](https://doi.org/10.1002/cbic.202000032) | **NO** — cuvette, no cells | **YES** (Kd) | **NO** | UNTESTED | Not individually checked — flagged for the Operator as an unchecked candidate |

**Line-2 result: BiFC = 0, split-GFP = 0, NanoBiT = 0, HiBiT = 0, NanoLuc = 0, tandem fluorescent
timer = 0** (Q14, short conjunction, load-bearing). **FRET and PLA exist and are per-cell; neither
is pooled-compatible, and every FRET record is from one laboratory (NCKU/Chang).**

🔴 **LEGEND already carries an open `conflicting evidence` flag against that laboratory's
localisation claims** (`discovery_ledger_current.md:808`, `paper_registry_current.md:6557`: Aldaz
places WWOX perinuclear/Golgi and attributes the Chang lab's pro-apoptotic phenotype to *"artefatto
dei vettori adenovirali"*). **Any weight placed on the FRET series inherits that dispute.**

### 4.3 Search line 3 — a WWOX-dependent transcriptional or signalling reporter

🔴 **The binding sub-question was: was the reporter validated as WWOX-dependent by a WWOX
perturbation, or is it merely downstream in a pathway WWOX is said to touch?** Answered per row.

| PMID | Reporter | WWOX-perturbation-validated? | single-cell? | quantitative? | pooled-compatible? | Retrievability | Held by LEGEND |
|---|---|---|---|---|---|---|---|
| `19465938` | **Wnt/β-catenin transcriptional activity** (Bouteille 2009). [DOI](https://doi.org/10.1038/onc.2009.120) | 🟢 **YES, BIDIRECTIONALLY** — *"enforced WWOX expression inhibited, and inhibition of endogenous WWOX expression stimulated the transcriptional activity of the Wnt/beta-catenin pathway"*. **Overexpression AND knockdown, opposite directions.** The strongest validation in this census. | **NO** — bulk luciferase, lysate | YES, per well | **NO** — the cell is destroyed to read it | UNTESTED | `registry_records.py`: **MATCH** — `paper_registry_current.md:3073`. `grep`: **FOUND** — `discovery_ledger_current.md:88` and `:188`, `analysis/therapy_levers.md:23`, `batch_queue.md:300`. **LEGEND reasons from this paper already.** |
| `25678599` | **β-catenin–TCF/LEF luciferase in MCF-7 + Xenopus secondary-axis induction** (El-Hage 2015). [DOI](https://doi.org/10.1158/1541-7786.MCR-14-0180) | 🟢 **YES** — *"By using both a luciferase assay in MCF-7 cells and a Xenopus secondary axis induction assay, it was demonstrated that WWOX inhibits the BCL9-2 function"*. Ectopic WWOX. | **NO** | YES, per well | **NO** | UNTESTED | `registry_records.py`: **MATCH** — `paper_registry_current.md:4658`. `grep`: **FOUND** — `batch_queue.md:211`, `catalogued only` |
| `39894307` | **Dual-luciferase**, p53 and NRF2 transcriptional activity, toosendanin-induced. [DOI](https://doi.org/10.1016/j.bcp.2025.116790) | 🟡 **PARTLY** — *"TSN-induced WWOX activation controlled the transcriptional activity of p53 and NRF2"*; WWOX-dependence of the ferroptosis phenotype is stated (*"its effect was dependent on WWOX"*), but the perturbation driving the reporter is **pharmacological**, not a clean WWOX knockdown/knockout. | **NO** | YES, per well | **NO** | UNTESTED | `registry_records.py`: **MATCH** — `paper_registry_current.md:1009`. `grep`: no additional surface |
| `38902482` | **Hippo / YAP-TEAD** in ESCC. [DOI](https://doi.org/10.1007/s10528-024-10856-9) | 🟡 **WWOX-perturbed, but NOT a reporter.** WWOX overexpression reduces YAP and TEAD; readouts named are **RT-qPCR and Western blot**, plus a YAP rescue. **No TEAD-luciferase or fluorescent reporter is claimed in the abstract.** Scored as *not a reporter*. | NO | n/a | NO | UNTESTED | `registry_records.py`: **MATCH** — `full_text_queue_current.md:4998` `[mention]`. `grep`: **FOUND** — same, *"secondo record emerso dal censimento di splicing"* |
| `35328751` | **HIF1α axis**, WWOX-silenced normal human fibroblasts across O₂ × glucose. [DOI](https://doi.org/10.3390/ijms23063326) | 🟢 **YES** — WWOX silenced, glycolysis genes/proteins/activity and lactate measured. **But the readout is gene expression, enzyme activity and lactate — bulk biochemistry, no reporter construct.** | NO | YES, per dish | NO | UNTESTED | `registry_records.py`: **MATCH** — `paper_registry_current.md:519`. `grep`: no additional surface |
| `40198927` | WWOX/P73/HIF-1α in gallbladder cancer. [DOI](https://doi.org/10.1016/j.tice.2025.102885) | 🟡 WWOX overexpression, but readouts are **WB, IHC, co-IP, CCK-8, Transwell**. No reporter. | NO | n/a | NO | UNTESTED | `registry_records.py`: **MATCH** — `paper_registry_current.md:1350` |
| `42589397` | `WWOX`/`HIF1A` **expression-ratio** analysis of TCGA BRCA/OV. [DOI](https://doi.org/10.3390/ijms27156740) | ❌ **NO** — bioinformatic, no perturbation, no assay. Authors self-label *"hypothesis-generating"*, *"statistically fragile"*. | NO | n/a | NO | Body already in corpus (`files/fulltext/PMID42589397_*`) | `registry_records.py`: **MATCH** — `full_text_queue_current.md:5127`, `claim_registry_current.md:451` via `FT-113` |
| `37615513` | `WWOX`-**promoter** luciferase for an intronic eQTL (rs9922483). [DOI](https://doi.org/10.1002/ijc.34703) | ❌ **Inverted object.** This reporter measures transcription **OF** `WWOX`, not a consequence **OF** WWOX protein activity. Irrelevant to F1. | NO | YES, per well | NO | UNTESTED | Not individually checked |

**Line-3 result: WWOX-dependent reporters DO exist and at least one (`19465938`) is validated by
WWOX perturbation in both directions — but every single one is a bulk luciferase or bulk
biochemistry readout. Not one is fluorescent, not one is per-cell, not one survives the
measurement.** `WWOX biosensor` = 0 (Q10).

### 4.4 Search line 4 — antibodies validated for intracellular flow cytometry

| Item | Finding | Held by LEGEND |
|---|---|---|
| **Any anti-WWOX antibody with published intracellular-flow validation** | 🔴 **NONE FOUND.** Q7 (`WWOX AND (flow cytometry OR FACS OR intracellular staining OR cell sorting)`) returned 36 records; inspection of the returned set found **no record whose flow readout is WWOX itself**. The flow in these papers is apoptosis/cell-cycle (annexin-V, PI) on WWOX-perturbed cells — WWOX is the **independent variable**, never the stained analyte. | — |
| **Any anti-pY33-WWOX antibody with published intracellular-flow validation** | 🔴 **NONE FOUND** by Q7, Q12 or W2. | — |
| **`ABN413`** | 🔴 **No published intracellular-flow validation found.** W2 returned no record naming `ABN413` at all; the engine surfaced Abcam catalogue pages instead. **`ABN413` is a Merck/Millipore catalogue number and this checkout cannot reach a vendor datasheet (all direct HTTP egress is blocked), so its validated-applications list is UNVERIFIED here, not negative.** | Named in LEGEND methods elsewhere (per the assignment) |
| **Commercially listed anti-WWOX / anti-pY33-WWOX antibodies** | W2 surfaced Abcam listings: `ab216660`, `ab238144` (total WWOX) and **`ab193624`, `ab129881` (phospho-Y33)**. 🔴 **These are catalogue listings, not validations, and no datasheet was fetched.** They establish that a **phospho-specific WWOX antibody exists as a product** — the reagent shape F2 asks for — and nothing more. [abcam ab193624](https://www.abcam.com/en-us/products/primary-antibodies/wwox-phospho-y33-antibody-ab193624) · [abcam ab129881](https://www.abcam.com/en-us/products/primary-antibodies/wwox-phospho-y33-antibody-ab129881) | — |
| 🔴 **A published failure, from a body actually read** | **R1, verbatim:** *"Commercial anti-WWOX antibodies did not show any specific signal for IF prompting us to use a myc-WWOX for localization studies."* A 2026 group **abandoned commercial anti-WWOX antibodies for immunofluorescence in RPE1** — the application class nearest to intracellular flow. `[PREPRINT]` | `batch_queue.md:459` |
| **Near-miss: mass cytometry** | R2 reports CyTOF on eight HCC tissues stratified by WWOX status. **The CyTOF panel measured CD68, CD204, CD45, PD-L1, Granzyme B, PD-1 — not WWOX.** WWOX status came from IHC and serum. **So WWOX has never been in a cytometry panel, even at CyTOF resolution.** | R2 read this session |

**Line-4 result: the single most important reagent in the TSC2 template — an antibody that works on
fixed, permeabilised cells in a cytometer — has NO WWOX counterpart in the published literature by
these queries, and the one group that tried commercial anti-WWOX antibodies in a fluorescence
application in 2026 reported that they did not work.**

### 4.5 Search line 5 — WWOX enzymatic activity assays *(see § 5, which this line feeds)*

| PMID | What it offers | single-cell? | quantitative? | pooled-compatible? | Retrievability | Held by LEGEND |
|---|---|---|---|---|---|---|
| `21476439` | **The only published WWOX enzyme assay found.** Sałuda-Gorgul *et al.*, *Z Naturforsch C* 2011. Bacterially expressed WWOX fusion proteins; *"oxidoreductase activity in a crude extract"*; *"defined a course of enzymatic reactions for selected steroid substrates, and determined related Km values"*; SDR domain reactive with **NAD⁺ and NADP⁺** for all examined steroid substrates; **reduction activity NOT observed** with NADH/NADPH. [DOI](https://doi.org/10.1515/znc-2011-1-210) | **NO** — cuvette, bacterial crude extract | **YES** (Km) | **NO** | UNTESTED. **No PMCID is returned for this record**, so PMC retrievability is not merely unchecked — there is no PMC identifier to check. | `registry_records.py`: **MATCH** — `paper_registry_current.md:4217` → **`CORPUS P306`**, Tier **C**, *"screened — corpus placeholder"*, **`Claim links: none`**. `grep`: **FOUND** — `batch_queue.md:292`, `catalogued only`. 🔴 **LEGEND holds this paper and has never connected it to anything.** |
| `34210081` | Lee CS, …, O'Keefe LV, *Cells* 2021 (the Adelaide review). Poses the substrate question as one of two named open questions. [DOI](https://doi.org/10.3390/cells10071637) | n/a | n/a | n/a | **Already read by LEGEND — 26 370 chars**, `full_text_queue_current.md:5178` | `registry_records.py`: **MATCH**. `grep`: **FOUND** — `full_text_queue_current.md:5171/5178`, `batch_queue.md:348`, `analysis/next_node_scout_20260921_orchestrator.md:116`, and the locator table of [`adelaide_node_discriminator_20260921`](adelaide_node_discriminator_20260921.md) |
| `41228229` | *Cancers* 2025 review. **Read in full today (R2).** | n/a | n/a | n/a | **FETCHED — 39 965 chars** | `registry_records.py`: **MATCH** — `paper_registry_current.md:1069`. `grep`: **FOUND** — `batch_queue.md:322`, `screened` |
| `40327201` | Hammouz *et al.*, *Funct Integr Genomics* 2025 — *"Twenty-five years of WWOX insight in cancer"*. Abstract-level: names Wnt/β-catenin, TGF-β, Dishevelled, SMAD3; **says nothing about substrate or catalysis**. [DOI](https://doi.org/10.1007/s10142-025-01601-5) | n/a | n/a | n/a | UNTESTED (`PMC12055895` exists) | `registry_records.py`: **MATCH** — `paper_registry_current.md:1229` |

### 4.6 Search line 6 — degradation / stability reporters

| Finding | Detail |
|---|---|
| **Q8 returned 4 records** | `39933386` (an IESS case series from Argentina — `half-life` keyword collision, no WWOX construct), `35738035`, `25447306`, `19500159`. **None is a WWOX stability reporter.** |
| **GFP-degron applied to WWOX** | 🔴 **NONE FOUND.** |
| **Ratiometric GFP-P2A-mCherry (or equivalent) applied to WWOX** | 🔴 **NONE FOUND.** |
| **What the field does have** | Only **bulk** degradation biochemistry, which LEGEND already holds: ACK1 phosphorylates WWOX at Tyr287 → polyubiquitination → degradation; ITCH mediates K63 ubiquitination (stabilising) and K274 ubiquitination. **R2, verbatim:** *"While it is established that ACK1 is crucial for the degradation of WWOX, the specific ubiquitination site responsible for WWOX degradation and the ubiquitin E3 ligase involved in this process remain unclear"*. |
| **The one directly relevant prior asset** | `mave_portability_to_wwox_20260921.md` § 6.A already concluded that **the abundance half (VAMP-seq: C-terminal GFP fusion + IRES-mCherry normaliser + 4-bin FACS) is portable to WWOX today**, with `RISK 1` (mislocalisation of a Golgi/membrane-associated protein by a C-terminal GFP) unresolved. 🔴 **R1 sharpens `RISK 1` rather than resolving it**: R1 places WWOX on **mid-Golgi membranes** and reports that a **myc** tag was needed because antibodies failed — it says nothing about whether a bulky C-terminal fluorophore is tolerated. |

**Line-6 result: no WWOX abundance reporter of any kind exists. The abundance axis remains a thing
that COULD be built from an off-the-shelf method, not a thing that has been built.**

---

## 5 · 🔴 THE SUBSTRATE QUESTION — is WWOX's physiological substrate still unidentified as of 2026?

### 5.1 The answer

> ## 🔴 **YES — still unidentified as of 2026, and this census found nothing that changes it.**
> **But the position is more textured than LEGEND's inherited one-liner, and the texture matters:
> a published in-vitro substrate characterization DOES exist, from 2011, and the field's own review
> literature declined to accept it as the answer ten years later.**

### 5.2 The evidence, with dates

| Date | Source | What it says, verbatim where quoted | Weight |
|---|---|---|---|
| **2011** | PMID `21476439`, *Z Naturforsch C* — Sałuda-Gorgul, Seta, Nowakowska, **Bednarek** (Łódź). [DOI](https://doi.org/10.1515/znc-2011-1-210) | *"using two bacterial expression systems, we have cloned WWOX fusion proteins showing oxidoreductase activity in a crude extract, defined a course of enzymatic reactions for **selected steroid substrates**, and determined related Km values. Our results show that the SDR domain of the WWOX protein has dehydrogenase activity and is reactive both in the presence of NAD+ and NADP+ for all examined steroid substrates. On the other hand, with the same substrates and reduced cofactors (NADH and NADPH) **reduction activity was not observed**."* | 🟡 **ABSTRACT-LEVEL.** In vitro. Bacterial expression. **Crude extract.** *Selected* substrates chosen on a prior hypothesis (*"Due to its potential role in sex-steroid metabolism"*), not discovered. **This is an activity demonstration on candidate substrates, not an identification of the physiological one.** The authors' own mood is preserved: they *defined a course of reactions for selected substrates*; they do not claim to have found the substrate. |
| **2021** | PMID `34210081`, *Cells* — Lee, Choo, Dayan, Richards, O'Keefe (Adelaide). [DOI](https://doi.org/10.3390/cells10071637) | *"Despite more than twenty years of research on the[] protein, **the substrate and product of the enzyme reaction that it catalyses are yet to be discovered**."* — and the review's own framing sets this as one of two named outstanding questions: *"what is the actual substrate and product of theenzyme activity?"* | 🟢 **HIGH.** **LEGEND has read this in full (26 370 chars) and holds the locator**: [`adelaide_node_discriminator_20260921.md`](adelaide_node_discriminator_20260921.md) line 204, `L4`, *"34210081 · §3, ¶1 (opening sentence)"*. 🔴 **Written TEN YEARS AFTER the 2011 paper, by a review whose explicit purpose was to survey exactly this.** |
| **2025** | PMID `41228229`, *Cancers* — read in full today (**R2**). [DOI](https://doi.org/10.3390/cancers17213435) | **The string `substrate` occurs ZERO times in the body.** What it does assert, verbatim: *"The SDR domain, characterized by its NSYK motif for binding both estrogen and androgen, demonstrates oxidoreductase activity and plays a crucial role in sex-steroid metabolism"*. | 🟡 **A measured negative, not a positive.** This is a **roman-class count on a body certified italic-class-inadmissible**, so the zero is admissible. The review neither identifies a substrate nor restates that one is missing. **It asserts a physiological role — sex-steroid metabolism — without naming a substrate or a product.** That is an inherited assertion, not a new identification. |
| **2025** | PMID `40327201`, *Funct Integr Genomics* — Hammouz, Baryła, Styczeń-Binkowska, **Bednarek** (Łódź), *"Twenty-five years of WWOX insight in cancer"*. [DOI](https://doi.org/10.1007/s10142-025-01601-5) | Abstract-level. Surveys WW-domain PPIs (Dishevelled, SMAD3, Wnt/β-catenin, TGF-β). **Names no substrate, no product, no catalytic cycle.** | 🟡 **ABSTRACT-LEVEL.** 🔴 **Notable**: Bednarek is senior author of both the 2011 substrate paper and this 2025 twenty-five-year retrospective. **The 2025 retrospective from the group that did the 2011 enzymology does not present a substrate as settled.** |
| **2021–2026** | Q5 `WWOX substrate product enzyme reaction identified` (`date_from=2021`) → **0**. Q3 `WWOX short-chain dehydrogenase reductase substrate identification` → **1**, and that one is the Adelaide review asking the question. | | 🟢 Two independent query shapes; neither surfaced a substrate-identification paper. |

### 5.3 The synthesis, stated with its hedges intact

1. **An in-vitro oxidoreductase activity of the WWOX SDR domain on steroid substrates was reported
   in 2011**, with Km values, cofactor dependence (NAD⁺/NADP⁺, oxidative direction only), from
   bacterially expressed protein in crude extract. **LEGEND holds this paper as a Tier-C corpus
   placeholder with zero claim links and has never read it.**
2. **The field did not treat that as the identification of the physiological substrate.** The 2021
   Adelaide review — the most substrate-focused review in the corpus, written a decade later, by an
   independent group — states the substrate and product *"are yet to be discovered"* and frames it
   as an outstanding question.
3. **Nothing between 2021 and 2026 found by these queries identifies one.** The 2025 reviews carry
   the sex-steroid *role* forward as an inherited assertion while naming no substrate.
4. **Therefore `TX-003`'s standing position — *"WWOX is an oxidoreductase with undefined
   physiological substrate/activity"* — survives 2026 intact.** 🔴 **But it should be carried with
   the 2011 datum attached**, because the two are not the same statement: *"no substrate has ever
   been demonstrated"* would be **false**; *"no physiological substrate has been identified"* is
   **true**. LEGEND's phrasing is already the correct one; what was missing is the knowledge that a
   candidate-substrate enzymology paper exists at all.
5. 🔴 **Consequence for F1, and it is negative.** Even taking the 2011 result at face value, a
   steroid dehydrogenase activity measured spectrophotometrically in bacterial crude extract with
   exogenous NAD⁺ **supplies nothing to F1**. F1 asks for a consequence that changes **inside a
   single intact cell** when WWOX is lost. A cuvette assay on purified protein is the opposite of
   that. **The 2011 paper does not reduce the F1 gap by any amount.**

### 5.4 🔴 The misattributed quotation, recorded so it is not repeated

WebSearch query W3's synthesis asserted: *"the true substrate(s) of this oxidoreductase remain to
be identified."* It offered PMC12610808 (= PMID `41228229`) among its links. **That body was then
fetched, persisted and counted: `substrate` = 0 occurrences.** The sentence is not in that paper.
It most plausibly originates from the ScienceDirect topic page also returned by W3, which is an
aggregator page, not a paper.

**The sentence is therefore carried nowhere in this file as evidence**, and § 5.2 rests only on
`34210081` (LEGEND-read, locator held) and on the measured zero in `41228229`. **A search-engine
synthesis is not a source, and the only reason this was caught is that the paper was read.**

---

## 6 · WHAT THE NEAREST THING WOULD NEED to become F1 + F2 — concrete and itemised

🔴 **This section describes gaps. It is not a proposal, not a design, and not a recommendation to
build anything.** Whether any of it is worth doing is the Operator's decision.

### 6.1 The three nearest things, ranked

| Rank | Candidate | F1 (cell-autonomous single-cell consequence) | F2 (flow-compatible reagent) | Fatal gap today |
|---|---|---|---|---|
| **🥇 1** | **Cell-surface lectin binding after WWOX depletion** — R1, PMID `42523332` | 🟡 **PARTIALLY SUPPLIED.** *"WWOX KD caused N- and O-glycosylation defects as revealed by the **increased plasma membrane binding** of the lectins HPA and GNL, which bind to the exposed Tn antigen and higher terminal mannose of underglycosylated proteins, respectively."* Cell-autonomous, displayed on the cell surface. | 🟡 **PARTIALLY SUPPLIED.** Fluorophore-conjugated HPA and GNL are ordinary reagents. 🔴 **And critically: the epitope is on the OUTSIDE.** No fixation, no permeabilisation — cells stay **alive, intact and sortable**, and genomic DNA is recoverable from live sorted cells. That is a **better** starting point than TSC2's fixed-cell pS6 stain, which required lysing fixed cells to recover DNA. | Measured by **microscopy, n = 30 cells**, after **siRNA**, in **one non-peer-reviewed preprint**, as an aside in a paper about something else. **`flow` appears once in R1's body and it is inside the word "workflow" in a mass-spec method; `cytometr` = 0; `FACS` = 0.** Nobody has put this on a cytometer. |
| **🥈 2** | **Time-lapse FRET of WWOX–partner complexes** — `27339895`, `27845895`, `29581896`, `19918364` | 🟢 Supplied in form: complex formation is a WWOX-dependent molecular event, read per cell. 🔴 But it reports **binding**, which `mave_portability_to_wwox_20260921.md` § 6.C already identified as the class that cannot be pooled. | 🟡 Fluorescent, yes. Flow-compatible, **no** as implemented. | Requires **two ectopic fusion partners**, time-lapse imaging, ratiometric donor/acceptor controls. Single laboratory. Inherits LEGEND's open Aldaz/Chang localisation conflict. |
| **🥉 3** | **Wnt/β-catenin transcriptional reporter** — `19465938`, corroborated by `25678599` | 🟢 **F1 supplied in substance and best-validated in the census** — WWOX-dependence shown by overexpression **and** knockdown, in opposite directions, and the effect is transcriptional, hence cell-autonomous. | 🔴 **NOT SUPPLIED.** Luciferase. Bulk lysate. The cell is destroyed by the measurement. | The readout format, and only the readout format. |

### 6.2 What candidate 1 (lectin) would need — itemised

1. **Peer review.** R1 is a bioRxiv preprint. Nothing built on it should outrank that fact.
2. **A cleaner perturbation.** siRNA knockdown, efficiency by **RT-PCR only** (*"Two biological
   repeats of the knockdown (KD) efficiency of WWOX siRNA measured with RT-PCR"*) — no protein-level
   confirmation reported. A knockout plus **re-expression rescue** is what would make the lectin
   shift attributable to WWOX rather than to an off-target or to the co-observed Golgi-area change.
3. **A demonstration on a cytometer**, which does not exist: dynamic range, coefficient of
   variation, and the separation between WWOX-null and WT populations. **Without a measured
   separation there is no way to know whether the effect is sortable at all.**
4. **A mixing experiment.** Can a WWOX-null cell be recovered from a WT background by sorting on
   lectin signal? This is the pooled-compatibility question and it is untested.
5. **Graded, not binary, response.** The preprint tests presence vs absence. **A missense-variant
   readout requires the signal to track partial activity.** If the lectin shift saturates at any
   loss of WWOX, it scores nulls and tells you nothing about a hypomorph.
6. 🔴 **Domain attribution, which is the item that decides whether this is relevant to WWOX-DEE at
   all.** R1 is explicit that it does not know: *"Although the molecular mechanism of WWOX remains
   unknown, its tandem WW domains could function as a scaffold to recruit PPxY-containing
   trafficking proteins to Golgi membranes, whereas its C-terminal short-chain
   dehydrogenase/reductase (SDR) domain **may** regulate Golgi physiol[ogy]"* — two speculations,
   both hedged, in one sentence. **If the glycosylation phenotype is WW-domain-dependent, the
   readout cannot report on SDR-domain missense alleles, and the entire SDR-span missense question
   that motivates LEGEND's interest is outside its reach.**
7. **Cell-type transfer.** RPE1, a retinal pigment epithelium line. The disease phenotype is
   neuronal and developmental. `F3` (cell-autonomy in an editable, expandable cell type) is
   *provisionally* satisfied by RPE1 for the assay, but **whether a neuronal WWOX function is being
   measured at all is untouched.**
8. **Independent replication.** There is none. **Q13 `WWOX glycosylation Golgi lectin` = 0** — this
   observation is, as of today, a single unreplicated preprint paragraph.

### 6.3 What candidate 3 (Wnt reporter) would need — itemised

1. **Replacement of luciferase with a fluorescent protein.** Fluorescent TCF/LEF reporters are a
   standard, published reporter class. 🔴 **That is a statement about what the reporter class
   permits in general. It is NOT a claim that anyone has built one for WWOX** — Q10 (`WWOX
   biosensor`) = 0, Q14 (split-GFP / NanoLuc / HiBiT / fluorescent timer) = 0, and **Q9's zero is
   one of the over-conjuncted ones and proves nothing**.
2. **A measured dynamic range for the WWOX perturbation specifically.** Bouteille reports direction
   (*inhibited* / *stimulated*), not magnitude at single-cell resolution. A reporter that moves
   30 % in bulk may be unsortable per cell.
3. **Confounder control.** Wnt reporter output is driven by many things other than WWOX. **The TSC2
   assay worked because pS6 is close to TSC2. Wnt/TCF is several nodes downstream of WWOX and every
   one of those nodes is a confounder** in a pooled library where cells differ only in `WWOX`.
4. **Resolution of an abundance/function confound**: a reporter shift caused by less WWOX protein is
   indistinguishable from one caused by less-active WWOX protein unless abundance is measured in the
   same cell. That is precisely the dissociation the TSC2 paper showed matters in 38.75 % of
   pathogenic alleles.

### 6.4 What is NOT needed, and this is worth stating

`F5` (endogenous-locus editing so genotype is recoverable from sorted cells) was already scored
**available** in `mave_portability_to_wwox_20260921.md`, and nothing found today changes it.
**F5 remains the one requirement the field supplies off the shelf.**

---

## 7 · NEGATIVE RESULTS — explicit and prominent

🔴 **Every statement in this section is of the form *"no published report was found by these
queries"*. None is of the form *"there is none".* Reagents live in methods sections, supplementary
tables, Addgene deposits and vendor catalogues; PubMed indexes abstracts; and the extractor used
here strips italics, superscripts and reference lists. Absence here is a property of the search.**

1. **No published single-cell, fluorescence- or FACS-readable reporter of WWOX activity was found**
   by Q1–Q20 or W1–W4. Specifically: **`WWOX biosensor` = 0** (Q10).
2. **No WWOX protein-complementation sensor of any kind was found.** `WWOX AND (split-GFP OR
   protein-fragment complementation OR NanoLuc OR HiBiT OR tandem fluorescent timer)` = **0**
   (Q14). **BiFC returns no WWOX record** within Q4's set of 6.
3. **No WWOX-HaloTag construct was found.** `WWOX AND HaloTag` = **0** (Q19).
4. **No WWOX MAVE, deep mutational scan or VAMP-seq dataset exists in PubMed.**
   `WWOX[Title/Abstract] AND (deep mutational scanning[TIAB] OR variant effect[TIAB] OR
   multiplexed[TIAB] OR VAMP-seq[TIAB])` = **0** (Q18). This **confirms** the premise of
   `missense_rescue_methodology_census_20260921.md` § 2 by an independent query shape.
5. **No anti-WWOX or anti-pY33-WWOX antibody with a published intracellular-flow-cytometry
   validation was found** (Q7, Q12, W2). **`ABN413` returned no publication and no datasheet;
   direct HTTP egress is blocked in this checkout, so its validated-application list is
   UNVERIFIED, which is not the same as negative.**
6. **No GFP-degron and no ratiometric dual-fluorescence stability construct applied to WWOX was
   found** (Q8, 4 records, none relevant).
7. **No fluorescent (as opposed to luciferase) WWOX-dependent transcriptional reporter was found**
   (Q6, Q10, Q11).
8. 🔴 **`WWOX glycosylation Golgi lectin` = 0 in PubMed** (Q13) — **the nearest thing this census
   found is not indexed by the terms that describe it, and has no independent replication.**
9. 🔴 **Five of the twenty PubMed queries (Q9, Q12, Q15, Q16, Q20) are over-conjuncted and their
   zeros are instrument readings about query construction, not bibliographic negatives.** They are
   listed in § 3.1 for completeness and are load-bearing for nothing.
10. 🔴 **Whether `WWOX` is present in the OpenCell endogenous split-mNeonGreen2 library is
    UNRESOLVED.** W4 confirmed the resource exists (1 310 HEK293T lines from 1 757 targeted genes;
    *"fluorescent signal was successfully detected for 1310"*) but returned no per-gene answer, and
    `opencell.czbiohub.org` cannot be queried from this checkout. **If `WWOX` is in that library, an
    endogenously tagged, live-cell, per-cell-quantifiable WWOX abundance line already exists and
    this census's line-1 negative would need immediate revision.** This is the single highest-value
    unresolved check handed forward, and it needs only a web lookup from a machine with egress.
11. **The two bodies read contain no WWOX-DEE / WOREE content.** R1 mentions neuronal development
    once in passing and studies RPE1 cells; R2 names WOREE and SCAR12 in its introduction and then
    discusses only cancer. **Neither paper is about this disease, and every transfer in this file is
    this reader's, not any author's.**
12. **No figure panel was inspected in either body.** Every quantitative statement attributed to R1
    comes from body text or from a figure legend reproduced in body text, quoted verbatim.

---

## 8 · 🔴 The F4 correction — the one inherited assessment this census overturns

`mave_portability_to_wwox_20260921.md` § 6.B records:

> | **F4** | **The direction of the signal should ideally be a GAIN on loss of function** (easier
> sorting). TSC2 is a negative regulator → pS6 **rises**. | ⚠️ **Adverse.** WWOX appears to act
> positively in its characterised interactions, so loss would most likely **remove** a signal.
> Sorting on signal loss is harder and more confounded by abundance. |

**Both nearest-things found today are gain-on-loss, for the same structural reason: on these two
axes WWOX is a NEGATIVE regulator, exactly like TSC2.**

| Axis | Direction on WWOX loss | Source, verbatim |
|---|---|---|
| **Surface lectin binding** | **UP** | *"WWOX KD caused N- and O-glycosylation defects as revealed by the **increased** plasma membrane binding of the lectins HPA and GNL"* — R1 `[PREPRINT]` |
| **Wnt/β-catenin transcription** | **UP** | *"enforced WWOX expression **inhibited**, and inhibition of endogenous WWOX expression **stimulated** the transcriptional activity of the Wnt/beta-catenin pathway"* — PMID `19465938` |
| **HIF1α glycolytic output** | **UP** | WWOX-silenced fibroblasts show *"higher glycolysis genes expression, their activity, and the lactate concentration"* — PMID `35328751`, abstract-level |

**The premise behind the `F4` adverse call — "WWOX appears to act positively in its characterised
interactions" — is true of its *binding* partnerships (it scaffolds, it stabilises) and false of its
*regulatory* outputs (it suppresses Wnt, it suppresses HIF1α, its loss degrades glycosylation).
`F4` should be re-scored from ⚠️ ADVERSE to 🟢 FAVOURABLE on every downstream-output axis named
here.** 🔴 This does not move `F1` or `F2` by a single step, and it must not be read as if it did.
It removes one of the four failing requirements from the failing column.

**Revised standing of the five requirements, for the Operator's convenience — LEGEND's canonical
record is unchanged by this file:**

| # | Prior (`mave_portability`) | After this census |
|---|---|---|
| `F1` | 🔴 ABSENT | 🟠 **NEAREST-THING IDENTIFIED** — surface glycosylation, one unreplicated preprint, domain attribution unknown |
| `F2` | 🔴 ABSENT | 🟠 **REAGENT CLASS IDENTIFIED** — fluorescent HPA/GNL lectins; never used on a cytometer for WWOX |
| `F3` | ❓ UNKNOWN, plausibly adverse | ❓ **UNCHANGED** — RPE1 is editable and expandable, but neuronal relevance untouched |
| `F4` | ⚠️ ADVERSE | 🟢 **FAVOURABLE** — gain-on-loss on all three characterised output axes |
| `F5` | ✅ Available | ✅ **UNCHANGED** |

> **The § 6.C conclusion of `mave_portability_to_wwox_20260921.md` therefore stands, with one word
> changed: the gate on a WWOX function MAVE is still the prior invention of a single-cell,
> fluorescence-readable WWOX activity sensor — but it is no longer true that nothing in the
> literature points at what such a sensor might read. One thing does, and it is a cell-surface
> sugar.**

---

## 9 · INFORMATION GAIN, per item

| Item | Mechanistic graph | Therapeutic hypothesis | Experimental roadmap | Genotype stratification | Intervention ranking | Uncertainty |
|---|---|---|---|---|---|---|
| **A · WWOX KD → increased surface HPA/GNL lectin binding** (R1, `42523332`) | **YES** — a WWOX→Golgi→N-/O-glycosylation edge with a named, measurable output; it instantiates the "trafficking–metabolism interface" that `working_model_current.md:63` and `CLAIM 026` already assert from interactome data alone | **NO** — `MECHANISTIC PROBE ONLY`; no molecule, no lever, no window | **YES** — the first named candidate for `F1`+`F2` in the history of this question | **NO** — presence/absence only; graded response untested; domain attribution unknown | **NO** | **YES** — preprint; siRNA; n=30; RPE1; zero replication (Q13=0); WW-vs-SDR attribution explicitly unresolved by the authors |
| **B · The substrate question, resolved with its texture** (`21476439` 2011 vs `34210081` 2021 vs `41228229` 2025) | **YES** — an in-vitro steroid-dehydrogenase activity with Km values exists and LEGEND did not know it, held as a Tier-C placeholder with zero claim links | **NO** — but it constrains `TX-003`: the standing phrase *"undefined physiological substrate/activity"* is correct and should stay, now with the 2011 datum attached rather than absent | **YES (negative)** — a cuvette assay on bacterial crude extract contributes **nothing** to `F1`; the enzymology route to a single-cell readout is closed, not merely unopened | **NO** | **NO** | **YES (reduced)** — the negative is now dated, sourced to a read review with a held locator, and bounded by two independent 2025 reviews |
| **C · `F4` re-scored ADVERSE → FAVOURABLE** (§ 8) | **YES** — separates WWOX's *binding* role (positive/scaffolding) from its *regulatory* role (negative/suppressive); that distinction was conflated in the inherited assessment | **NO** | **YES** — removes one of four failing MAVE requirements; the sorting direction is the easy one on every characterised output axis | **NO** | **NO** | **YES (reduced)** — three independent axes agree on direction |
| **D · No anti-WWOX antibody has any published intracellular-flow validation; a 2026 group reports commercial anti-WWOX antibodies fail in IF** (§ 4.4, R1 verbatim) | **NO** | **NO** | **YES** — forecloses the most direct port of the TSC2 template (antibody stain of fixed cells) and redirects toward surface or genetic readouts | **NO** | **NO** | **YES (increased, correctly)** — the reagent floor under every WWOX protein-level measurement in this corpus is weaker than assumed, which also bears on the western-blot floor flagged in `candidate_adjudication_20260921.md:52` |
| **E · `19465938` is a bidirectionally WWOX-validated transcriptional reporter** (§ 4.3) | **NO** — LEGEND already reasons from this paper (`discovery_ledger_current.md:88`, `:188`) | **NO** | **YES** — reclassifies a paper LEGEND holds as *mechanism* into a paper LEGEND holds as *assay precedent*; it is the best-validated WWOX-dependent reporter in existence and it is already in the corpus | **NO** | **NO** | **NO** — adds no uncertainty; the paper is unchanged |
| **F · No WWOX MAVE exists (Q18 = 0)** | **NO** | **NO** | **YES** — independently confirms the premise of `missense_rescue_methodology_census_20260921.md` by a second query shape | **NO** | **NO** | **YES (reduced)** — the census's central premise is now double-sourced |
| **G · OpenCell membership of `WWOX` is UNRESOLVED** (§ 7 item 10) | **NO** | **NO** | **YES** — names a single cheap check that could overturn this file's line-1 negative | **NO** | **NO** | **YES (increased, correctly)** — an open, answerable question is now on the record instead of an unexamined assumption |
| **H · `registry_records.py` returned NO RECORD MATCHED for four papers the grep then FOUND** (`42523332`, `29581896`, `19918364`, `31315632`) | **NO** | **NO** | **NO** | **NO** | **NO** | **YES** — a fourth same-day confirmation that the tool's surface list excludes `registries/batch_queue.md`, `analysis/` and `research/fulltext_dossiers/`. **The dual-method rule earned its keep four times in one session.** |

---

## 10 · DEFAULTS_TAKEN

1. **Scope held to methods and reagents, as instructed.** No mechanism hunt. WWOX biology appears
   only where it determines whether an assay could work.
2. **Two full texts read, and only two**, against a budget of two: R1 (`42523332`) because its
   abstract named WWOX as a Golgi/glycosylation regulator and glycosylation is lectin-FACS-readable
   — i.e. it plausibly answered F1/F2 — and R2 (`41228229`) because the substrate question was
   named the highest-value item and a web snippet had put a substrate claim in its mouth that
   needed checking. **No paper was read to look productive; § 5.4 is why R2 was worth the budget.**
3. **`get_copyright_status` was not called at all.** The standing rule says the flag records what
   was not checked; the fetch was attempted directly in both cases and both delivered. Reported
   lengths are measured.
4. **Every census row is labelled abstract-level unless it is R1 or R2.** No paper's contents are
   asserted from a title.
5. **Localisation was scored as failing `single-cell?` and `quantitative?`**, deliberately and
   hard, because that is the distinction most likely to manufacture a false positive here. R1's
   WWOX/COG8 colocalisation (`LQ=0.27, n=20, 3 cells`) is scored NO/NO despite being fluorescent and
   per-cell, because a colocalisation coefficient is not a measurement of activity. **The one R1
   result that is scored YES — the lectin shift, `n = 30 cells` — is scored YES only because it is
   a per-cell intensity measurement of a WWOX-dependent output, not a localisation call.**
6. **Vendor catalogue pages were not fetched** (HTTP egress blocked; the proxy was not worked
   around). `ABN413` and the Abcam listings are reported as catalogue-level and UNVERIFIED.
7. **`pooled-compatible?` was scored on what was published, not on what is conceivable.** Every
   candidate whose reagent class *could* be adapted is scored NO with the adaptation described in
   § 6 — because scoring potential as fact is exactly how a census becomes a proposal.
8. **R2's persisted body was transcribed from an inline tool payload, with three declared character
   normalisations** (§ 1.2). Byte-identity with PMC is not claimed for R2; it is claimed for R1.
9. **Five over-conjuncted queries were kept in the record rather than deleted and re-run**, and
   their zeros were explicitly disqualified (§ 3.1). A query log that hides its own failures cannot
   support a negative.
10. **No sensor was proposed and no MAVE programme was proposed.** § 6 states gaps in the existing
    object; it names no new construct, no cell line to build, no experiment to fund, and no
    sequence of work. Both would be materially new research programmes and are the Operator's
    decision.
11. **Nothing canonical was touched.** No `*_current.md`, no registry, no ledger, no receipt, no
    commit candidate, no `BATCH_COMMIT`, no commit, no push. Two new files were written to
    `files/fulltext/` (the persisted bodies, required by STEP 1) and this one analysis file.
