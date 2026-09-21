# WOREE therapeutic-class census — how many reported patients sit behind each therapeutic lever

**Scientist B · 2026-09-21 · READ-ONLY toward every canonical file and every ledger. No commit candidate. No receipt written. No canonical file modified. `TX-001`–`TX-007` are NOT re-ranked here.**

🔴 **This is classification for research planning. It is NOT treatment advice, NOT a recommendation, and NOT a statement about any individual.** It reasons about a WWOX-DEE genotype class assembled from published literature, never about a person.

Bibliographic records and full text below are from **PubMed / PubMed Central**. DOI links are given per source.

---

## VERDICT

**Gene addition addresses the largest share of reported patients, and it does so for a structural reason rather than a numerical one: it is the only lever whose applicability does not depend on what the endogenous alleles are.** In the largest genotype-classified cohort, **63 of 88 classified alleles (71.6 %) are predicted null and 25 of 44 classifiable individuals (56.8 %) are null/null** — a majority of reported patients therefore have **no recoverable endogenous substrate for any allele-specific lever at all**. The largest allele-specific class is PROTEIN-RESCUE at **25/88 alleles (28.4 %)**, but only **6/44 individuals (13.6 %)** could be served by it alone, and every one of those assignments is conditional on a measurement nobody has made for any WWOX missense allele; **RNA-RESCUE has zero demonstrated members**, because every measured WWOX splice outcome in the literature is exon skipping toward frameshift and no productive alternative outcome has ever been shown. Confidence: **MODERATE** on the null-versus-missense split (three independent cohorts agree in direction and magnitude), **LOW** on every partition *within* the null class (no published cohort separates splice from nonsense from frameshift from CNV), and **the entire census rests on severe-pole, consanguinity-enriched, ascertainment-biased cohorts**.

---

## 1 · METHOD and sources

### 1.1 · What was done

A synthesis over LEGEND's own records first, with PubMed used only to fill gaps. **One** new full text was read — the single most variant-dense WOREE source in the literature — and persisted before analysis. Everything else in this file is either (a) already held by LEGEND at full-text or dossier depth, or (b) explicitly labelled **ABSTRACT-LEVEL**.

**An abstract is not a read.** Every count drawn from an abstract carries that label on its own line.

### 1.2 · The one new full text, persisted before analysis

| Field | Value |
|---|---|
| Source | Piard J, Philippe C, Marvier M, … Kini U, Callier P *et al.* **"The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature."** *Genet Med* 2019;21(6):1308–1318 |
| PMID / PMCID / DOI | 30356099 · PMC6752669 · [DOI](https://doi.org/10.1038/s41436-018-0339-3) |
| Retrieval | PubMed MCP `get_full_text_article`, `pmc_ids: ["PMC6752669"]`. Retrievability established **by attempting the fetch and measuring the body**, not by `is_open_access`. |
| Artefact | `files/fulltext/PMID30356099_PMC_MCPtext.txt` |
| **bytes** | **33,419** |
| **chars** | **33,357** |
| **sha256** | **`5dbb1c2fb85706d9e0b62ca71a0c10c1d0f2bea5b6ccaac3569a89592c7533e3`** |
| LEGEND status before today | `CORPUS-STUB-059`, **`not_processed`** — the largest WOREE series in the literature had never been read here. |

**Instrument check on the artefact, performed before any count was relied on.** The extractor's italic-deletion failure is active: `thegene` occurs **7** times and `inwere` **5** times, each a place where the italicised gene symbol *WWOX* was deleted. `WWOX` survives as a bare string only **19** times, all roman-type. **A count of `WWOX` in this artefact is an instrument reading, not a measure of how often the paper names the gene.**
**HGVS survived and its zeros are admissible.** `p.` tokens: 17 distinct, all intact. `c.[0-9]` matches **only twice** in the whole body (`c.1228G>T`, `c.600T>A`) — and that is itself a finding: **this paper names its variants at the protein level in prose and puts the cDNA-level per-patient table in Supplemental Tables 1–4, which are named in the body and are not present in the retrievable text.** Roman-class zeros, admissible: `minigene` 0 · `nonsense-mediated` 0 · `NMD` 0 · `antisense` 0 · `oligonucleotide` 0 · `ASO` 0 · `read-through` 0 · `ataluren` 0 · `AAV` 0 · `gene therapy` 0 · `chaperone` 0 · `proteostasis` 0 · `western` 0 · `blot` 0 · `half-life` 0. Present: `CNV` 24 · `exon` 19 · `splic*` 9 · `RT-PCR` 1 · `cryptic` 1.
Per **D-14**: Figure 2 (the 29-allele lollipop) is **not inspectable** here and nothing is claimed from it beyond the prose sentence that states its total.

### 1.3 · LEGEND records used (no re-fetch)

- [`wwox_splice_transcript_census_20260921.md`](wwox_splice_transcript_census_20260921.md) — the ANNOTATED/MEASURED line, and the measured-transcript inventory.
- [`variant_triage_rescuability.md`](variant_triage_rescuability.md) — the decision logic this file supplies the denominator for; its own text says the full-set version is *"planned, resources permitting"*.
- [`variant_structural_pipeline.md`](variant_structural_pipeline.md) · [`missense_proteostasis_matrix_20260921.md`](missense_proteostasis_matrix_20260921.md) · [`sdr_missense_readout_assessment_20260920.md`](sdr_missense_readout_assessment_20260920.md) · [`missense_rescue_methodology_census_20260921.md`](missense_rescue_methodology_census_20260921.md) · [`l239r_intraallelic_comparator_20260921.md`](l239r_intraallelic_comparator_20260921.md) · [`wwox_neonatal_parkinsonism_audit_20260921.md`](wwox_neonatal_parkinsonism_audit_20260921.md) · [`AUTONOMOUS_SESSION_STATE.md`](AUTONOMOUS_SESSION_STATE.md).
- **`research/fulltext_dossiers/PMID33916893.md`** — Banne *et al.* 2021, *Cells* 10(4):824, PMCID PMC8067556, [DOI](https://doi.org/10.3390/cells10040824). LEGEND holds this as a **`complete_fulltext_read`**, receipt `FTR-20260909-33916893-01`, manifest schema v2, **strict PASS, 0 gaps, 31 locators**, with its three supplementary XLSX tables recomputed rather than accepted. It is the single best-attested patient-level source LEGEND holds, and it is a **secondary source** — tabulating >21 other groups' patients.
- `claim_registry_current.md` CLAIM 013 · CLAIM 018 · CLAIM 019 · CLAIM 021 · `meta/meta_human_spectrum_current.md` · `paper_registry_current.md` · `literature_tracking_log_current.md`.

### 1.4 · The classes, exactly as briefed

| Class | Definition | Lever |
|---|---|---|
| **RNA-RESCUE** | splice-affecting alleles where a *productive* transcript outcome is conceivable | splice-switching ASO, exon skipping |
| **PROTEIN-RESCUE** | missense alleles producing an unstable but potentially recoverable protein | chaperone / proteostasis / stabiliser |
| **GENE-REPLACEMENT** | nonsense, frameshift, large deletion/CNV, and any allele with no recoverable endogenous substrate | AAV gene addition |
| **READ-THROUGH** | in-frame PTC alleles where read-through is conceivable | ataluren-class (context-dependent) |
| **UNASSIGNABLE** | evidence insufficient to place the allele | — |

🔴 **Three assignment rules, carried on every row.**

1. **A splice annotation is a PREDICTION, not an observation.** ANNOTATED (called splice-site by position or by SpliceAI/MaxEntScan/a diagnostic pipeline) and MEASURED (RNA or cDNA actually run) are held in **separate columns and are never merged**. Only a handful of WWOX alleles have ever been MEASURED.
2. **"Splice-site" does not imply "ASO-rescuable."** `variant_triage_rescuability.md` is explicit that an ASO *"does not repair the sequence and cannot recreate the abolished acceptor"* — it can only redirect splicing toward a productive outcome **if one exists**. Every RNA-RESCUE membership below is therefore marked **conditional**.
3. **PROTEIN-RESCUE membership is conditional on a measurement nobody has made.** In the one gene where the question has been answered at scale, **31/80 = 38.75 %** of known-pathogenic TSC2 missense alleles have **normal abundance** — an abundance-only criterion would misclassify about two in five. And WWOX's own **P282A is dead in every functional assay with no stability defect**. Every PROTEIN-RESCUE row carries that caveat.

---

## 2 · The variant-level table

Held alleles, with what is actually known about each. **ANNOTATED and MEASURED are separate columns and are never combined.** `Ev.` = evidence level of the patient count: **FT** = from a full text read (by LEGEND or here), **DOS** = from a LEGEND dossier over a complete full-text read of a secondary curation, **ABS** = 🔴 **ABSTRACT-LEVEL**.

### 2.1 · Splice-affecting alleles

| Variant (HGVS as published) | Consequence | ANNOTATED | MEASURED | Reported patients | Zygosity | Source PMID | Class | Confidence | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| `NM_016373.4:c.107+1G>A` | canonical **donor**, intron 1 | ✅ NGS + ACMG | ❌ **none — RNA never examined** | **5** (of a 7-patient series) | homozygous; *"possible regional founder effect"* (authors' mood, preserved) | 42721537 | **RNA-RESCUE (conditional) / GENE-REPLACEMENT if no productive outcome** | LOW — annotation only | 🔴 **ABS** (paywalled, Elsevier, `pmc_id: null`) |
| `c.172+1G>C` | canonical **donor**, intron 2 (WW1) | ✅ | ✅ **MEASURED — heterologous minigene, HEK293T, RT-PCR + Sanger → loss of exon 2** | 1 | homozygous via maternal UPD16 | 39101447 | **GENE-REPLACEMENT** (skipping → frameshift; no productive outcome reported) | MODERATE — only WWOX splice allele LEGEND has read the measurement of | **FT** |
| `NM_016373.3:c.606-1G>A` | canonical **acceptor**, intron 6 | ✅ WES | ❌ **none** | **5** | homozygous; described as "two seemingly unrelated families" but 🔴 **the paper itself states all patients and carriers share the same haplotype, "indicating the families are in fact related to one another"** → **5 patients, ONE kindred** | 26345274 | **RNA-RESCUE (conditional) / GENE-REPLACEMENT** | LOW — annotation only | 🔴 **ABS** (paywalled, Wiley, `pmc_id: null`) |
| `c.517-2A>G` | canonical **acceptor**, intron 5 → exon 6 | ✅ | ⚠️ **MEASURED (reported)** — *"Complementary DNA sequencing demonstrated…"* exon 6 skipping; LEGEND has **never seen the measurement** | ≥2 (Yemenite, in trans with Q230P) + 2 independent WOREE iPSC lines | compound het | 30853297 · 33916893 · 42397075 | **GENE-REPLACEMENT** (skipping → null-like; `CLAIM 018`) | MODERATE for pathogenicity, LOW for rescuability | 🔴 **ABS** for the measurement; **DOS** for the patient count |
| `NM_016373.4:c.516+1G>A` | canonical **donor** | ✅ | ⚠️ **MEASURED (reported)** — *"WWOX mRNA sequencing using peripheral blood RNA"*, exon 5 deleted; **patient tissue**; LEGEND has never seen it | 1 | — | 38407561 | **GENE-REPLACEMENT** | LOW | 🔴 **ABS** |
| `c.1057-2A>G` | canonical **acceptor**, intron 8 → exon 9 (ClinVar VCV001418567) | ✅ **SpliceAI acceptor-loss 0.96; MaxEntScan 7.28 → −0.67; cryptic acceptor gain +8 nt, 0.64** | ❌ **none — never measured in any system** | reference-genotype worked example; no patient count asserted here | — | LEGEND in-silico (`variant_triage_rescuability.md`) | **RNA-RESCUE (conditional)** — conditional on a productive outcome existing, which is unmeasured | LOW — pure prediction | in-silico |
| `c.409+1G>T` | canonical **donor** | ✅ | ❌ | comparator variant only | — | held in LEGEND records | **GENE-REPLACEMENT** (default) | LOW | repo |
| `c.229_230+2delGAGT` | donor-spanning indel | ✅ | ❌ | 1 (Chinese, compound het) | compound het | 33916893 Table S1 | **GENE-REPLACEMENT** | LOW | **DOS** |
| `c.605+5G>A` | **non-canonical splice-region** (+5, not ±1/±2) | ✅ | ❌ | ≤1 (one of 12 compound-het children) | compound het | 39039877 | **UNASSIGNABLE** — a +5 change may be silent, leaky or null; nothing distinguishes them here | VERY LOW | 🔴 **ABS** |

### 2.2 · Missense alleles

| Variant | Consequence | ANNOTATED | MEASURED | Reported patients | Zygosity | Source PMID | Class | Confidence | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| `c.689A>C` **p.(Gln230Pro)** | missense, buried SDR core, α-helix 227–232, relSASA 0.00 | ✅ ThermoMPNN +1.51 kcal/mol; ESM-2 −9.08 LLR (worst substitution at the site) | ⚠️ **protein-level endpoint only** — patient fibroblasts: *qRT-PCR normal WWOX transcript; Western blot: protein not detected*; authors leave **"impaired translation **or** premature degradation"** undiscriminated | **8 patients / 6 families** (4 homozygous: Afghan ×2, Moroccan, Iranian; 4 compound het: 2 French, 2 Yemenite in trans with `c.517-2A>G`). Independently: **4 families** in the 2019 series. **2 individuals** in the 2025 registry cohort. | both | 33916893 (census) · 30356099 (4 families) · 29808465 (function) · 40875931 | **PROTEIN-RESCUE (conditional)** — 🔴 and the conditionality is not rhetorical: no synthesis, solubility, half-life, route or function measurement exists for this allele | MODERATE for pathogenicity (`CLAIM 019`, consolidated baseline); **LOW** for recoverability | **DOS** + **FT**; 🔴 **ABS** for the Johannsen functional endpoint (LEGEND holds only the abstract) |
| **p.(Gly137Glu)** | missense, NAD(P)(H)-binding motif GANSGIG aa 131–137 | ✅ PolyPhen-2 probably damaging | ❌ | **3 families** | in trans with null in a gene where LoF is a known mechanism | 30356099 | **PROTEIN-RESCUE (conditional)** | LOW | **FT** |
| **p.(Ser318Leu)** | missense | ⚠️ the **only** missense in the 2019 series **not** called probably damaging by PolyPhen-2 | 🔴 **MEASURED — and it is the only measured missense RNA readout in the WWOX literature:** in P3, *"total RNA analysis by Sanger sequencing of reverse transcription PCR (RT-PCR) products **failed to detect any splicing anomaly** in leukocytes"* | **2 families** | in trans with null | 30356099 | **PROTEIN-RESCUE (conditional)** — the measured negative is what **keeps** it here rather than reclassifying it to RNA-RESCUE | LOW-MODERATE — the one allele with an experimental discriminator, and it is a negative in a non-neural tissue | **FT** |
| `c.140C>G` **p.(Pro47Arg)** | missense, WW1 hydrophobic core | ✅ | ❌ | **2 families** (2019 series). Separately, 2 Portuguese compound-het patients, alive at 4 y and 3 y, **in trans with `c.46_49del p.Asp16fs`** — ⚠️ likely the same patients | compound het | 30356099 · 33916893 | **PROTEIN-RESCUE (conditional)** | LOW — 🔴 and the genotypes are unmatched: the 2021 audit found P47R's phenotype **cannot be separated from the null-like allele in trans** | **FT** + **DOS** |
| **p.(Pro47Thr)** | missense, same residue, WW1 | ✅ *"key amino acid essential for maintaining the WWOX protein fully functional"*; **measured loss of peptide interaction for WW1** | ⚠️ binding assay, not abundance | **4 siblings, 1 consanguineous Saudi family** (SCAR12, not WOREE) | homozygous | 24369382 | **PROTEIN-RESCUE (conditional)** | LOW — and 🔴 **the 2021 figure mis-colours P47R/P47T**, applying the SCAR12 colour to the WOREE allele | **ABS** + **DOS** |
| **p.(Gly372Arg)** | missense | ✅ highly conserved | ❌ | 1 consanguineous family (SCAR12) | homozygous | 24369382 | **PROTEIN-RESCUE (conditional)** | LOW | **ABS** |
| `c.716T>G` **p.(Leu239Arg)** | missense, SDR span; LEGEND maps it to the **same helix as Q230P**, relSASA 0.000, 3.5 Å from the anchors (LEGEND's mapping, not the papers') | ✅ | ❌ — 🔴 **no Western, no fibroblast work, no transcript measurement of any kind**; LEGEND's own falsifiable prediction that L239R yields absent protein **remains untested** | **3 patients / 2 families** (2 siblings + 1 unrelated infant) | homozygous both | 41153369 · 42092735 | **PROTEIN-RESCUE (conditional)** | LOW | LEGEND partial full-text reads |
| **p.(Thr12Met)** | missense, N-terminal, **not** in a WW domain | ✅ | ❌ | 1 (first documented adult, 40 y) | homozygous | 39507621 | **PROTEIN-RESCUE (conditional)** | LOW | LEGEND full-text record |
| `c.406A>G` **p.(Ile136Val)** | missense, NAD(P)(H)-binding motif | ✅ | ❌ | 1 consanguineous case | homozygous | 35712340 | **PROTEIN-RESCUE (conditional)** | LOW | LEGEND full-text record |
| **p.(Glu17Lys)**, **p.(Thr358Ile)** | missense, **not in a known functional domain** | ✅ | ❌ | see below | — | 30356099 | **UNASSIGNABLE** (see §2.4) | VERY LOW | **FT** |
| **p.(His150Pro)**, **p.(Lys200Glu)** | missense | ✅ | ❌ | ≤1 family each | in trans with null | 30356099 | **PROTEIN-RESCUE (conditional)** | VERY LOW | **FT** |
| `c.911C>A` / `c.991C>A` **p.(Ser304Tyr)** | missense | ✅ | ❌ | ≥1; recurs independently in a second cohort's novel-variant list | — | held in LEGEND records · 39039877 | 🔴 **UNASSIGNABLE on nomenclature** — the source paper writes `c.991C>A` in its text and abstract and `c.911C>A` in Table 1 and Discussion. Only `c.911C>A` falls in codon 304. **Not normalised here.** | — | repo + 🔴 **ABS** |
| **p.Ala149Thr · p.Arg156Ser · p.Leu186Val · p.His263Arg · p.Met326Arg** | missense, novel | ✅ | ❌ | ≤1 each, within a 12-child compound-het cohort | compound het | 39039877 | **PROTEIN-RESCUE (conditional)** | VERY LOW | 🔴 **ABS** |
| `c.754C>G` **p.(Pro252Ala)** · `c.844C>G` **p.(Pro282Ala)** | missense, SDR span | ✅ | ✅ **MEASURED** — P252A: normal mRNA, accelerated turnover, lysosome-dependent (CQ and NH₄Cl restore; MG-132 does not; 3-MA does not). **P282A: no stability defect and dead in every functional assay.** | 🔴 **germline homozygous in a cancer proband who at 35 *"did not suffer from WWOX-related nervous system disease"*** | homozygous | 41124647 | 🔴 **NOT WOREE ALLELES** — included only because they carry the census's central brake. **Cancer-assay-dead is not neurologically null.** | — | LEGEND full-text read |

### 2.3 · Nonsense, frameshift, CNV and other null alleles

| Variant | Consequence | ANNOTATED | MEASURED | Reported patients | Zygosity | Source PMID | Class | Confidence | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| `c.160G>T` **p.(Arg54*)** | nonsense, exon 2 (aa 54 of 414) | ✅ | ❌ no NMD assay | ≥1 (index) + part of the 7-patient *"early premature stop codon / full knockdown"* group | homozygous | 24456803 · 30356099 | **GENE-REPLACEMENT**; **READ-THROUGH candidate** (in-frame PTC) | LOW | **ABS** + **FT** |
| `c.131G>A` **p.(Trp44*)** | nonsense, exon 2 | ✅ | ❌ | **2 homozygous patients** recorded (endpoints 7 y and 20 months) | homozygous | 33916893 · 30356099 | **GENE-REPLACEMENT**; **READ-THROUGH candidate** | LOW | **DOS** |
| `c.790C>T` **p.(Arg264*)** | nonsense | ✅ | ❌ | **2 homozygous patients** (endpoints 8 y 11 m, 5 y 2 m). Separately, 1 proband with R264* + an 84,828 bp exon-6 deletion | homozygous / compound het | 33916893 | **GENE-REPLACEMENT**; **READ-THROUGH candidate** | LOW | **DOS** |
| `NM_016373.4:c.571C>T` **p.(Gln191*)** | nonsense, novel | ✅ ACMG | ❌ | ≤2 (within the 7-patient Argentine series) | — | 42721537 | **GENE-REPLACEMENT**; **READ-THROUGH candidate** | LOW | 🔴 **ABS** |
| **p.Trp218\*** | nonsense, novel | ✅ | ❌ | ≤1 of 12 | compound het | 39039877 | **GENE-REPLACEMENT**; READ-THROUGH candidate | VERY LOW | 🔴 **ABS** |
| `c.45_48delGGAC` **p.Asp16Serfs\*63** / `c.46_49del p.Asp16fs` | frameshift, exon 1 | ✅ | ❌ | 2 siblings (Portuguese), in trans with P47R | compound het | 33916893 | **GENE-REPLACEMENT** | LOW | **DOS** |
| `c.1043del` **p.Phe348Serfs\*57** | frameshift, exon 8 (ClinVar 421407) | ✅ | ❌ | 1 | compound het with a 38 kb exons 6–7 deletion; 🔴 **parental testing not done → cis/trans not determined** | 42193054 | **GENE-REPLACEMENT** | LOW | LEGEND full-text record |
| `c.918del` **p.E306fs** | frameshift | ✅ | ❌ | 1 (Romanian, West syndrome) | compound het | 33916893 | **GENE-REPLACEMENT** | LOW | **DOS** |
| `c.231_409del` **p.D77Efs\*27** | frameshift | ✅ | ❌ | 1 (Italian) | compound het | 33916893 | **GENE-REPLACEMENT** | LOW | **DOS** |
| **p.R167Tfs\*8 · p.Leu275fs\*19 · p.N285Kfs\*10** | frameshift, novel | ✅ | ❌ | ≤1 each of 12 | compound het | 39039877 | **GENE-REPLACEMENT** | VERY LOW | 🔴 **ABS** |
| **Deletion encompassing exons 6–8** | multi-exon CNV | ✅ MLPA/array-CGH/qPCR | ⚠️ for the *analogous* exons 6–8 genomic deletion in a different context, cDNA showed exon 5 spliced directly onto exon 9 (22071891) | 🔴 **5 ALLELES — the most frequent pathogenic CNV in WWOX-related disorders.** The source reports **alleles, not patients**, and the count is not converted here. | — | 30356099 | **GENE-REPLACEMENT** | MODERATE (allele count is a direct quote) | **FT** |
| **Duplication encompassing exons 6–8** | multi-exon CNV | ✅ | ❌ | **1 allele** | — | 30356099 · 36779245 | 🔴 **UNASSIGNABLE** — a duplication's consequence (in-frame tandem, frameshifting, or null) is undetermined without RNA | VERY LOW | **FT** |
| **Homozygous deletion exons 1–4** · **homozygous deletion of the first six exons** | large CNV | ✅ | ❌ | part of the 7-patient *"full knockdown"* group; **premature death before 2 years in 5/7** | homozygous | 30356099 | **GENE-REPLACEMENT** | MODERATE | **FT** |
| **Exon-5 deletion, homozygous (Emirati)** · **two single-exon deletions in trans (P4)** · **two CNVs in trans (P2)** | intragenic CNV | ✅ | ❌ | 1 each | homozygous / compound het | 30356099 · 33916893 | **GENE-REPLACEMENT** | LOW | **FT** + **DOS** |
| **`loss1 exon2-8`** (large intragenic deletion) | CNV | ✅ | ❌ | ≤1 of 12 | compound het | 39039877 | **GENE-REPLACEMENT** | VERY LOW | 🔴 **ABS** |

### 2.4 · Explicitly UNASSIGNABLE

| Item | Why | Source |
|---|---|---|
| **P19's genotype `p.[Lys200Glu;Thr358Ile];[Gln230Pro]`** — three missense alleles in one patient | The authors themselves: *"It is not possible to determine whether one or both of these variants are the disease-causing missense variant in P19."* Thr358 *"is not located in a known functional domain."* | 30356099 (**FT**) |
| **`c.1228G>T` p.(Gly410Cys)**, 2 sisters, consanguineous Arab family | Excluded by the reviewing authors: mild phenotype, *"its causal role is questionable"*, and the change is **homozygous in two gnomAD individuals** | 30356099 (**FT**) |
| **`ENST00000402655:c.600T>A` p.(Ser200Arg)** | Affects only a **non-RefSeq 311-aa isoform**; the authors declined to consider the genotype causative | 30356099 (**FT**) |
| **`c.872T>C` p.(Leu291Pro)** | Annotated solely *"Esophageal squamous cell carcinoma, somatic"* — **not a WOREE/SCAR12 allele**; removing it is what reconciles 22 → 21 distinct variants | 33916893 (**DOS**) |
| **A 6.8 Mb 16q22.2-q23.1 deletion, heterozygous (Japanese infant, West syndrome)** | 🔴 *"no pathogenic variants were detected in the other allele of WWOX"* — **monoallelic. This is not a WOREE patient and must not be counted as one**, although it appears in the 2021 curation's DEE28 responder rows. | 31353122 (🔴 **ABS**) · 33916893 (**DOS**) |
| **The VUS pools** | 103 VUS in the 2021 curation (type column partitions **93 missense / 6 intronic / 2 nonsense / 2 indel**, recomputed from the deposit) and the **529-VUS** interpretability gap named in `variant_triage_rescuability.md`. 🔴 **These are different sets and neither is a pathogenic-allele set.** A VUS pool is not a therapeutic denominator. | 33916893 (**DOS**) · repo |

---

## 3 · The class counts, and exactly what the denominator is

### 3.1 · Primary denominator — the only cohort that classifies every individual

**Gao K, Riley LG, Raubenheimer J, Oliver KL, Wykes AD, Mentz J, Lee SJ, Pinner J, Cardamone M, Scheffer IE, Gold WA.** *"WWOX-Related Developmental and Epileptic Encephalopathy: Expanding the Clinical Spectrum and Deciphering the Genotype-Phenotype."* **Neurology 2025** · PMID 40875931 · [DOI](https://doi.org/10.1212/WNL.0000000000213883). LEGEND record: `PAPER 014` / `CLAIM 013`, *"full text reviewed (PDF)"*; the numbers below are **ABSTRACT-LEVEL as re-derived here** — the abstract gives percentages, `CLAIM 013` gives the same percentages, and **the artefact itself is gone** (`files/` is gitignored and was empty at session start).

> *"50 individuals with biallelic WWOX variants across 45 families, identifying 25 variants that have not been previously reported… Individuals classified with a null/null genotype (56.8%) were more likely to have hypertonia, seizures and respiratory complications compared with individuals with null/missense (29.5%) or missense/missense (13.6%) variant genotypes."*

**The denominator is 44 classifiable individuals, not 50.** 56.8 / 29.5 / 13.6 % has a **unique** exact integer solution over n ∈ [3, 50]: **n = 44, giving 25 / 13 / 6.** (Verified by exhaustive search; see DEFAULTS_TAKEN 1.) **Six of the 50 individuals are not genotype-classified by the source and are carried below as UNASSIGNABLE.**

| | Count | Share |
|---|---|---|
| Individuals in the cohort | 50 | — |
| Families | 45 | — |
| **Individuals with a classified genotype pair** | **44** | **88 % of 50** |
| null/null | 25 | 56.8 % of 44 |
| null/missense | 13 | 29.5 % of 44 |
| missense/missense | 6 | 13.6 % of 44 |
| **Classified alleles** | **88** | — |
| **null alleles** (2×25 + 13) | **63** | **71.6 %** |
| **missense alleles** (13 + 2×6) | **25** | **28.4 %** |

### 3.2 · The class census

| Therapeutic class | Alleles | % of 88 classified alleles | Patients **fully** served (both alleles in class) | % of 44 | Patients with **≥1** allele in class | % of 44 |
|---|---:|---:|---:|---:|---:|---:|
| **GENE-REPLACEMENT** (nonsense · frameshift · CNV · splice with no demonstrated productive outcome) | **63** | **71.6 %** | **25** | **56.8 %** | **38** | **86.4 %** |
| **PROTEIN-RESCUE** (conditional) | **25** | **28.4 %** | **6** | **13.6 %** | **19** | **43.2 %** |
| **RNA-RESCUE** (conditional) | ⊆ the 63 — 🔴 **not separable in any published cohort** | — | **0 demonstrated** | **0 %** | — | — |
| **READ-THROUGH** | ⊆ the 63 — 🔴 **not separable** | — | **0** | **0 %** | — | — |
| **UNASSIGNABLE** | 12 alleles (the 6 unclassified individuals) | 12 of 100 | 6 of 50 | 12 % | — | — |

🔴 **The RNA-RESCUE and READ-THROUGH rows are empty not because those alleles do not exist, but because every published WWOX cohort that classifies genotypes pools splice, nonsense, frameshift and CNV into a single "null" bin.** That is a property of the literature, not of this analysis, and it is the single biggest structural obstacle to the census.

🔴 **And the most decision-relevant line in the table is the one that is easiest to misread.** Gene addition does not "win" 71.6 % of alleles in the way a splice-switching ASO would win a splice allele: **AAV gene addition is allele-agnostic — it adds a transgene and does not care what the endogenous alleles are, so by mechanism its addressable share is 100 % of patients.** What the 56.8 % actually measures is the **complement**: the share of reported patients for whom **no allele-specific lever is conceivable at all**, because neither allele leaves anything to rescue. The two allele-specific levers are each bounded by a minority of alleles; the allele-agnostic one is bounded by none. **That asymmetry, not the percentage, is the finding.**

### 3.3 · Allele-level cross-check — a second, independent denominator

From the full text read today (PMID 30356099, aggregating its own 20 patients with all cases then published):

> *"By aggregating our patients with all cases reported so far in the literature, 37 patients from 27 families with a WOREE syndrome and biallelic WWOX pathogenic variants are known. A total of **29 different pathogenic/likely pathogenic alleles (10 CNVs and 19 SNVs)** have been identified."*

and

> *"All missense variants identified in individuals with WWOX-related encephalopathy (**11 aa changes in 12 families**)…"*

| Allele class in the 2019 aggregate | Count | % of 29 | Therapeutic class |
|---|---:|---:|---|
| CNVs (deletions + 1 duplication) | **10** | 34.5 % | GENE-REPLACEMENT (the duplication UNASSIGNABLE) |
| Missense SNVs | **11** | 37.9 % | PROTEIN-RESCUE (conditional) |
| **Non-missense SNVs** (nonsense + frameshift + splice, **not partitioned by the source**) | **8** *(derived: 19 − 11)* | 27.6 % | GENE-REPLACEMENT / RNA-RESCUE / READ-THROUGH — **not separable** |

**The two denominators agree in direction and differ in magnitude, and the difference is informative.** By allele, 2019 gives 37.9 % missense against 2025's 28.4 %; by family, 2019 gives *"one or two pathogenic CNVs in 14/27 families (52 %)"*. Both say the same thing: **the null-class alleles are the plurality, missense is roughly one allele in three, and the splice sub-class is too small to be reported separately by anybody.**

**Upper bound on RNA-RESCUE.** LEGEND's splice census plus today's reading names **nine** splice-affecting WWOX alleles in total (§2.1), against ≥29 distinct pathogenic alleles — a nominal ceiling of **roughly one allele in four at most, and plausibly far fewer**. Set against that ceiling: **zero** have a demonstrated productive outcome. **The demonstrated share of RNA-RESCUE is 0 %.**

### 3.4 · What the denominator is NOT

🔴 **State it plainly: this is not the true population, and it is not close.**

- **It is a denominator over *reported* patients in *published* cohorts.** The 2021 curation projects ≈121,000 WOREE cases worldwide (from 1,057 gnomAD alleles, ≈1:250, assuming trans phase and random mating → ≈1:62,000) against **217** it can enumerate. The authors themselves offer under-diagnosis first and *"many of these variants are benign"* second, **quantifying neither**, and declare the phase-unknown and random-mating limitations themselves. **Whatever the true number is, the published cohorts are a vanishing and non-random fraction of it.**
- **Severe-pole ascertainment.** Every cohort here was ascertained through a DEE or refractory-epilepsy clinic. Milder alleles — the ones most likely to retain the residual function a chaperone or an ASO would build on — are **systematically the ones that never reach these cohorts**. The 2021 curation says as much about its own missense-only SCAR12 group: it *"may be a sampling artefact rather than a rule."*
- **Consanguinity enrichment.** 10/27 families (37 %) in the 2019 aggregate are consanguineous and **all of them are homozygous for a single allele**. Both of the largest recurrent-allele clusters are founder or consanguineous. **Consanguinity inflates homozygosity and therefore inflates the apparent recurrence of individual alleles** — which is exactly the number an allele-specific therapy's feasibility depends on.
- **Survival bias, and it cuts toward MORE null, not less.** The 2025 cohort is a **parent-reported registry** recruited through a foundation; `CLAIM 013` records the survival bias as documented. Null/null patients die earliest and are least likely to be alive to be enrolled. **So 56.8 % null/null is plausibly a floor on the null share at birth, not a ceiling.**
- **Overlap is unquantified.** See §4.3 and §6.

---

## 4 · Recurrent alleles — ranked by reported patient count

🔴 **This is the most decision-relevant output in the file, because an allele-specific therapy's feasibility scales with how many patients share the allele.** Ranked by reported patients; independent families given where the source states them.

| Rank | Allele | Patients | Families / kindreds | Class | ANN / MEAS | Evidence level | The qualifier that must travel with the number |
|---:|---|---:|---|---|---|---|---|
| **1** | **p.(Gln230Pro)** `c.689A>C` | **8** | **6** | PROTEIN-RESCUE (conditional) | ANNOTATED + a protein-level endpoint | **DOS** (complete full-text read of a secondary curation) + **FT** | 🔴 **The most recurrent single WWOX allele of any class in the 2021 census** (its Figure 3B draws it at the axis maximum, the tallest lollipop of any mutation class). Within homozygous Q230P alone the recorded endpoint spans **death at 3 y 3 m** to **alive at 12 y and 10 y** — severe without being deterministic. The 8 and the 2019 series' 4 families **overlap and are not additive**. |
| **=2** | **`NM_016373.4:c.107+1G>A`** | **5** | 1 series, 7 patients total; *"possible regional founder effect"* | RNA-RESCUE candidate (conditional) / GENE-REPLACEMENT | **ANNOTATED ONLY — RNA never examined** | 🔴 **ABSTRACT-LEVEL** (Elsevier, `pmc_id: null`) | 🔴 On every line that uses it: **abstract-derived.** 5 of 7 patients at one centre in one country — **relatedness cannot be excluded**, and the authors' own word is *"possible"*. |
| **=2** | **`NM_016373.3:c.606-1G>A`** | **5** | 🔴 **ONE kindred**, not two families | RNA-RESCUE candidate (conditional) / GENE-REPLACEMENT | **ANNOTATED ONLY — RNA never examined** | 🔴 **ABSTRACT-LEVEL** (Wiley, `pmc_id: null`) | 🔴 Abstract-derived. **The paper states its own two "seemingly unrelated" families share a haplotype and are in fact related.** For therapy feasibility, 5-patients-one-kindred ≠ 5-patients-five-families. All five died before their third birthday. |
| **4** | **p.(Gly137Glu)** | ≥3 | **3 families** | PROTEIN-RESCUE (conditional) | ANNOTATED | **FT** | Binds the NAD(P)(H) motif region. No functional measurement exists. |
| **5** | **p.(Leu239Arg)** `c.716T>G` | **3** | **2 families** | PROTEIN-RESCUE (conditional) | ANNOTATED | LEGEND partial full-text reads | Same homozygous allele in ≥2 other children **did not produce** the parkinsonian presentation of the index case → **not an allele-level phenotype predictor**. LEGEND's own prediction that L239R yields absent protein is **untested**. |
| **6** | **p.(Pro47Thr)** | **4 siblings** | **1 family** | PROTEIN-RESCUE (conditional) | ANNOTATED + a measured WW1 binding loss | **ABS** + **DOS** | 4 patients but **one kindred**, SCAR12 not WOREE. |
| **7** | **p.(Ser318Leu)** | ≥2 | **2 families** | PROTEIN-RESCUE (conditional) | 🔴 **MEASURED — negative**: no splicing anomaly detectable in leukocyte RNA | **FT** | The **only** WWOX missense allele in the literature with an RNA discriminator, and it is a negative in a non-neural tissue. Also the only one PolyPhen-2 did **not** call probably damaging. |
| **8** | **p.(Pro47Arg)** `c.140C>G` | ≥2 | **2 families** | PROTEIN-RESCUE (conditional) | ANNOTATED | **FT** + **DOS** | 🔴 Its phenotype **cannot be separated** from the exon-1 frameshift in trans; the genotypes are unmatched. |
| **=9** | **p.(Arg264\*)** `c.790C>T` | **2** | 2 | GENE-REPLACEMENT; READ-THROUGH candidate | ANNOTATED | **DOS** | Endpoints 8 y 11 m and 5 y 2 m — 🔴 the source column is *"Death / last date of examination"* and **mixes the two**. |
| **=9** | **p.(Trp44\*)** `c.131G>A` | **2** | 2 | GENE-REPLACEMENT; READ-THROUGH candidate | ANNOTATED | **DOS** | Endpoints 7 y and 20 months, and **whether that divergence is survival or follow-up length is not resolved**. Sibship not stated. |
| **=9** | **`c.517-2A>G`** | ≥2 (+2 iPSC lines) | ≥1 | GENE-REPLACEMENT | ⚠️ MEASURED (reported): exon 6 skipping — **LEGEND has never seen the measurement** | 🔴 **ABS** for the measurement, **DOS** for the count | `CLAIM 018`, consolidated baseline. The only recurrent splice allele for which **characterised patient-derived material already exists**. |
| **—** | **Deletion encompassing exons 6–8** | 🔴 **not a patient count** | — | GENE-REPLACEMENT | ANNOTATED | **FT** | 🔴 **5 ALLELES**, the most frequent pathogenic CNV. The source reports alleles; converting them to patients would be an invention and is not done. **By allele it outranks everything except Q230P.** |

**Two lines that decide how this table should be used.**
1. **The top three are, in order: one missense allele (8 patients) and two canonical splice alleles (5 patients each).** 🔴 **Both splice counts are ABSTRACT-LEVEL and both are behind paywalls** — and one of them is a single kindred by its own paper's admission.
2. **The single most frequent *lesion* is not in the table's patient column at all**: the exons 6–8 deletion, at 5 alleles, is a CNV and therefore lands in GENE-REPLACEMENT regardless of how many patients carry it.

### 4.3 · Ten patients, two canonical alleles, zero RT-PCRs

LEGEND already held this and this census confirms it quantitatively: `c.107+1G>A` (5 patients) and `c.606-1G>A` (5 patients) are **ten reported patients across two canonical splice alleles whose RNA has never been examined by anyone** — and a group that owns WOREE fibroblasts and runs RT-PCR on WWOX transcripts is identified (PMID 35573960, Genoa). 🔴 Both counts are **abstract-derived**, and one of the two is a single kindred.

---

## 5 · What each class would need to become actionable

| Class | One concrete thing |
|---|---|
| **GENE-REPLACEMENT** | A **dose–response**: what fraction of wild-type WWOX must be restored, in how many cells, by what age, to move a defined endpoint. With 56.8 % of classified patients null/null, the binding question is no longer *which patients* but *how much and how early* — and `CLAIM 032` already records that an effective rescue may not need to be complete. |
| **PROTEIN-RESCUE** | The **abundance-clamped, domain-resolved, function-per-molecule comparison** on **one** disease-derived WWOX missense allele — matched wild-type and mutant levels, SDR-partner co-IP as the discriminating readout, a WW1-dependent partner as the control that must stay normal, everything normalised to WWOX input. Until that exists, all 25 alleles stay conditional, and the TSC2 number says ~2 in 5 abundance-based calls would be wrong. |
| **RNA-RESCUE** | **Junction-spanning RT-PCR ± NMD block, with band quantification**, on banked RNA from the two existing multi-patient splice cohorts (§4.3). One cheap assay either **populates this class or empties it**, and it is the only class in the table that a single experiment can settle. |
| **READ-THROUGH** | 🔴 **An enumeration, not an experiment.** LEGEND holds **no** systematic count of WWOX PTC alleles, **no** PTC-context annotation (stop-codon identity and the +4 nucleotide, which govern read-through efficiency), and **no** read-through datum of any kind — `ataluren` 0, `read-through` 0, `PTC124` 0, `ELX-02` 0 across the whole repository. Step one is a list. |
| **UNASSIGNABLE** | The **per-patient allele tables**. For the largest series these sit in supplementary files (Supplemental Tables 1–4) that are named in the body and are not retrievable here; for the 2025 registry the artefact is gone. Resolution is an acquisition problem, not an analysis problem. |

---

## 6 · Supplementary sources — variant-bearing cohorts with no LEGEND registry record

Added mid-task from a data-driven pass over `corpus_seed_pubmed_20260806.jsonl` (multi-gene epilepsy cohorts in which WWOX appears as one causative gene). 🔴 **All entries below are ABSTRACT-LEVEL. No additional full text was read — the one-full-text budget was spent on PMID 30356099 (§1.2).**

| PMID | Cohort | WWOX patients | Allele detail in the abstract | Overlap risk |
|---|---|---:|---|---|
| **39039877** | 12 children, WWOX-DEE, Peking University First Hospital, 2019–2023 | **12** | 🔴 **The most allele-informative abstract in this set.** *All 12 compound heterozygous.* 12 previously unreported alleles named: **6 missense** (p.Ala149Thr, p.Arg156Ser, p.Leu186Val, p.His263Arg, p.Ser304Tyr, p.Met326Arg) · **3 frameshift** (p.R167Tfs\*8, p.Leu275fs\*19, p.N285Kfs\*10) · **1 nonsense** (p.Trp218\*) · **1 splice-region** (`c.605+5G>A`, **+5, non-canonical**) · **1 CNV** (`loss1 exon2-8`). ⚠️ The sentence *"including 20 variants, 11 variants and 1 large intragenic deletion"* is **extractor-mangled**; 11 + 1 = the 12 names listed, against 20 variants in the cohort. Read no further into the mangled numerals. | China; plausible centre overlap with 32051108 and 35715422 |
| **37583270** | 124 children, genetic infantile epileptic spasms syndrome, multicentre India | **4** | none | India; plausible overlap with 40088508 |
| **34034642** | *"six patients and new mutations"*, WWOX-related EE | **6** | *"new mutations"* — not named in the abstract | unknown |
| **35792847** | 9 patients / 6 families, WOREE | **9** | not named | already `CORPUS-STUB-060`, `not_processed` |
| **32051108** | 1 Chinese patient, compound heterozygous | **1** | not named | China |
| **29390993** | targeted sequencing, intractable early-onset epilepsy | **1** | not named | — |
| **37095367** | WGS, Kazakhstani children with early-onset epilepsy | **≥1** | WWOX among 6 novel disease-gene variants | — |
| **32214227** · **31618474** · **35715422** · **40088508** | exome in Palestinian/Israeli Arabs (high consanguinity) · EIMFS genetic landscape · 36 children EIMFS · genetic epilepsies in infancy, India | **n not stated** | WWOX named as a causative/candidate gene only | high, within-country |
| **31353122** | 6.8 Mb 16q22.2-q23.1 deletion, Japanese infant, West syndrome | 🔴 **0 — EXCLUDED** | *"no pathogenic variants were detected in the other allele of WWOX"* → **monoallelic, not WOREE.** It nonetheless appears in the 2021 curation's DEE28 responder rows. | — |
| **30783266** | Correction to PMID 30356099 | 0 | Sequencing-method attribution only (one patient by genome rather than exome sequencing). **Changes no variant.** | — |

**Sub-count.** Additional *reported* WOREE/WWOX-DEE patients not in LEGEND's registry: **a defensible range of ≈24 to ≈35+**, not a point estimate. Firm floor from cohorts that state an n: 12 + 4 + 6 + 9 + 1 + 1 ≈ **33**, minus an unquantified overlap between the two Chinese and the two Indian sets, plus an unknown contribution from the four cohorts that name WWOX without an n. 🔴 **A defensible range beats a false total.**

**Do they change the ranking? NO.** Three reasons, each checkable:
1. **No new recurrent allele.** Every named allele in this set appears ≤1 time except `p.Ser304Tyr`, which recurs across cohorts **and is exactly the allele whose nomenclature is internally contradictory in its other source** — so it strengthens nothing and is held UNASSIGNABLE.
2. **No new measurement.** Not one of these adds a transcript measurement, an abundance measurement, a half-life, or a function-at-restored-abundance readout. **Every conditional stays conditional.** The class of things that would change the ranking is exactly the class of things none of these papers contains.
3. **The one allele-partitioned abstract points the other way and cannot be used.** PMID 39039877's *novel*-allele list is 6/12 missense — higher than the 28.4 % headline. But it is a **novel-allele subset**, not a cohort allele census (the cohort carries 20 variants; 12 are named), and all 12 patients are compound heterozygous, so it cannot be converted into a class share. Recorded as a **watch item**: if the full per-patient table shows a genuinely higher missense fraction in an East Asian cohort, the PROTEIN-RESCUE denominator is population-dependent. **That is a hypothesis this census raises and does not test.**

---

## 7 · NEGATIVE RESULTS — what this census cannot support

🔴 **Read this section before any of the numbers above are used.**

1. **No published WWOX cohort partitions its null alleles by mechanism.** RNA-RESCUE and READ-THROUGH therefore have **no denominator at all** — not a small one, none. Every cohort that classifies genotypes (2023, 2025) codes alleles as *null* or *missense* and stops.
2. **RNA-RESCUE is a class with zero demonstrated members.** Three WWOX splice alleles have ever had a transcript measured; LEGEND has read exactly one of those measurements. Every reported outcome is exon skipping toward frameshift. **No productive alternative outcome has been demonstrated for any WWOX allele in any system.** "Splice-site" therefore does **not** license "ASO-rescuable" on a single row of §2.1.
3. **PROTEIN-RESCUE is a class with zero demonstrated members in the sense that matters.** No functional measurement has ever been made on a WWOX missense protein whose abundance was restored. The one WWOX allele with a lysosomal-rescue result had **band intensity and nothing else** measured under the rescue; and the same paper supplies the counter-case, P282A, dead in every assay with no stability defect. The TSC2 number — **31/80 = 38.75 %** of known-pathogenic missense alleles with **normal abundance** — puts a figure on how often an abundance-only criterion would be wrong.
4. **Patient counts across cohorts are not additive and the overlap is not quantified.** The 2019 aggregate (37 patients), the 2021 curation (58 DEE28 rows, 56 excluding two medical terminations of pregnancy, plus 6 SCAR12), the 2023 series (13 patients / 12 families) and the 2025 registry (50 individuals / 45 families) **draw on overlapping literature** — the 2021 curation cites the 2019 series as the source of most of its Q230P patients. 🔴 **I could not exclude double counting for any recurrent allele, and no total across cohorts is stated anywhere in this file.**
5. **The 2025 cohort's own denominator is 44, not 50** — six individuals are unclassified and are carried as UNASSIGNABLE, not silently dropped.
6. **Two of the three top recurrent alleles are abstract-level and paywalled**, and one of those two is a single kindred by its own paper's statement. Neither has had RNA examined.
7. **The per-patient allele tables of the largest series are not retrievable here.** Supplemental Tables 1–4 of PMID 30356099 are named in the body and absent from the extraction; the PDF of PMID 40875931 is gone with the container. **The allele-by-allele version of this census is not producible from what is reachable from this deployment.**
8. **This census makes no prevalence claim.** The 2021 curation's own ≈121,000-versus-217 gap is reproduced here as *its* arithmetic under *its* declared assumptions (trans phase, random mating), not as a finding.
9. **Nothing here is a within-class ranking of patients by rescuability.** An allele is placed in a class; no allele is said to be more rescuable than another.
10. **Nothing here supports a genotype–phenotype prognosis for any individual**, and nothing here is medical advice.
11. **Instrument caveats, per class.** In `PMID30356099_PMC_MCPtext.txt` the italicised gene symbol *WWOX* was deleted throughout (`thegene` ×7, `inwere` ×5): **a zero or low count for `WWOX` there is an instrument reading, not a negative.** HGVS `c.`/`p.` strings are unitalicised and survived intact, so **the HGVS zeros and the roman-type method-word zeros listed in §1.2 ARE admissible.** In PMID 41153369 the extractor strips **every gene symbol**, which is why the WWOX allele there is identified from its cDNA coordinates and its disease label rather than from the gene name.
12. **Figure-only content is not adjudicated** (D-14). Figure 2 of PMID 30356099 — the 29-allele lollipop that would give the per-class allele partition directly — is not inspectable here.

---

## 8 · What this implies for the strategy ranking — stated, and stopped there

🔴 **`TX-001`–`TX-007` are NOT re-ranked here and no new strategy is proposed. The ranking decision belongs to the Orchestrator and the Operator.** What the census *implies*, said once:

- The lever that reaches the largest share of reported patients is **the allele-agnostic one**, and it reaches them **because** it is allele-agnostic. **56.8 % of classified individuals have no allele-specific lever available on either allele.**
- The largest **allele-specific** class is PROTEIN-RESCUE at **28.4 % of alleles**, but only **13.6 % of individuals** could be served by it alone — and **0 % of it is demonstrated**.
- RNA-RESCUE's *demonstrated* share is **0 %** and its *nominal ceiling* is roughly one allele in four. The gap between those two numbers is closable by **one RT-PCR on banked RNA from ten already-identified patients**. Nothing else in this census has that property.
- Therefore, if the census implies anything about sequencing of work, it is that **the cheapest experiment in the table is also the one that most changes the denominator** — and that is an observation, not a re-ranking.

---

## 9 · INFORMATION GAIN

| Axis | Verdict | One line |
|---|---|---|
| **Mechanistic graph** | **NO** | No new mechanism, partner, pathway or causal edge. This is a counting exercise over alleles already known to the model. |
| **Therapeutic hypothesis** | **NO** | Explicitly out of scope; no strategy proposed and none re-ranked. |
| **Experimental roadmap** | **YES** | It identifies, and for the first time **prices**, the single cheapest experiment that would either populate or empty an entire therapeutic class: junction-spanning RT-PCR ± NMD block on banked RNA from the ten patients already carrying the two recurrent canonical splice alleles. |
| **Genotype stratification** | **YES** | First allele-level therapeutic-class denominator in the repository — **63/88 null vs 25/88 missense alleles**, **25/13/6 individuals** across null/null, null/missense, missense/missense, with the 44-not-50 denominator established and the six unclassified individuals carried rather than dropped. |
| **Intervention ranking** | **YES — as an input, not as a decision** | It converts "which lever serves how many" from an adjective into a number, and it isolates the structural asymmetry (two levers bounded by minorities of alleles, one bounded by none) that the previous mechanism-plausibility ranking could not see. |
| **Uncertainty** | **YES** | It names **three classes with zero demonstrated members** (RNA-RESCUE, READ-THROUGH, and PROTEIN-RESCUE in the function-at-restored-abundance sense), separates ANNOTATED from MEASURED on every row, labels every abstract-derived count, and replaces a false total with a declared range where overlap could not be excluded. |

---

## 10 · DEFAULTS_TAKEN

1. **Gao 2025's percentages were converted to counts by exhaustive integer search**, not assumed: 56.8 / 29.5 / 13.6 % has a **unique** exact solution over n ∈ [3, 50], namely **n = 44 → 25 / 13 / 6**. The abstract gives percentages only. The denominator is therefore **44 classifiable individuals of 50**, and the remaining **6 are carried as UNASSIGNABLE**.
2. **"8 non-missense SNVs" in the 2019 aggregate is derived arithmetic** — 19 SNVs − 11 missense aa changes. The paper states both terms and not the difference.
3. **Allele-level totals for the 2025 cohort are derived** — 63 null = 2×25 + 13; 25 missense = 13 + 2×6. The paper reports genotype-pair classes, not allele counts.
4. **"Patients with ≥1 allele in class" is computed here**, not reported by any source.
5. 🔴 **Splice-affecting alleles default to GENE-REPLACEMENT wherever no productive outcome has been demonstrated — i.e. everywhere.** The alternative default (counting them as RNA-RESCUE on annotation alone) is precisely what `variant_triage_rescuability.md` forbids. Each such allele is *additionally* marked as an RNA-RESCUE **candidate** where the class is conceivable, and that dual marking is why the §3.2 rows do not sum to a partition.
6. **"Null" in the 2023 and 2025 cohorts is taken to include splice alleles.** The 2025 abstract does not say so explicitly, but it offers only *null* and *missense* as codes, and the 2023 paper — overlapping authorship (Oliver, Scheffer, Gold) and the same coding scheme — states that its variants *"comprised both missense and null changes including five copy number variants (four deletions, one duplication)."* Flagged as an **inference**, not a quotation.
7. **`c.606-1G>A` is counted as 5 patients in ONE kindred**, on the source's own haplotype statement, rather than as the "two seemingly unrelated families" of its framing.
8. **Where two sources report the same recurrent allele, both figures are given separately and never added** (Q230P: 8 patients / 6 families in the 2021 census; 4 families in the 2019 series; 2 individuals in the 2025 registry).
9. **CNV counts stated by a source as *alleles* are reported as alleles** and are not converted into patients (the exons 6–8 deletion: **5 alleles**).
10. **Duplications are UNASSIGNABLE by default**, because an in-frame tandem duplication, a frameshifting one and a functional null are not distinguishable without RNA.
11. **P252A and P282A are listed but excluded from every count** — they are germline homozygous in a cancer proband without WWOX-related nervous-system disease and are not WOREE alleles. They appear only because they carry the census's central brake.
12. **One full text was read (PMID 30356099) and persisted with bytes / chars / sha256 before analysis; the artefact was written from the MCP payload in the same session.** No second full text was read, including from the mid-task supplementary list.
13. **No receipt was written, no ledger touched, no canonical file modified, no commit candidate created.** This file is non-canonical analysis.

---

*Bibliographic data and full text from **PubMed / PubMed Central**. Principal DOIs: [10.1038/s41436-018-0339-3](https://doi.org/10.1038/s41436-018-0339-3) · [10.1212/WNL.0000000000213883](https://doi.org/10.1212/WNL.0000000000213883) · [10.1111/epi.17542](https://doi.org/10.1111/epi.17542) · [10.3390/cells10040824](https://doi.org/10.3390/cells10040824) · [10.1016/j.seizure.2026.08.027](https://doi.org/10.1016/j.seizure.2026.08.027) · [10.1002/ajmg.a.37363](https://doi.org/10.1002/ajmg.a.37363) · [10.1093/brain/awt338](https://doi.org/10.1093/brain/awt338) · [10.1186/1750-1172-9-12](https://doi.org/10.1186/1750-1172-9-12) · [10.1002/mgg3.2500](https://doi.org/10.1002/mgg3.2500) · [10.1002/ajmg.a.63074](https://doi.org/10.1002/ajmg.a.63074) · [10.3390/cimb48050449](https://doi.org/10.3390/cimb48050449).*

🔴 **Classification for research planning. Not treatment advice, not a recommendation, not a statement about any individual. Therapeutic output from this system supports discussion with a treating clinical team; it never substitutes for one.**
