# TRAPPC6A as an independent epilepsy risk locus — targeted audit of PMID 41390778

**Analyst:** Scientist A · **Date:** 2026-09-21 · **Status:** non-canonical analysis. READ-ONLY toward every canonical file. No commit candidate. No therapeutic proposal.

---

## 0 · Provenance, read depth and what could NOT be obtained

**Source.** According to PubMed: Fu M, Tran T, Pasaniuc B, Vossel K, Chang TS. "Multi-task learning identifies shared genetic risk for late-onset epilepsy and alzheimer's disease." *Sci Rep* 2025 Dec 13;16(1):2517. PMID 41390778 · PMCID PMC12820071 · [DOI](https://doi.org/10.1038/s41598-025-32329-8).

**Author disambiguation — checked, not assumed.** The senior author's affiliation string, retrieved verbatim from the PubMed record, is:

> "Chang", "fore_name": "Timothy S" … "Mary S. Easton Center for Alzheimer's Research and Care, Department of Neurology, David Geffen School of Medicine, University of California, Los Angeles, CA, 90095, USA. [email redacted — public edition; the address is on the PubMed record]."

This is **Timothy S. Chang, UCLA** — not Nan-Shan Chang, NCKU. No author on this paper holds an NCKU affiliation; all five are UCLA / UPenn. **The paper is genuinely external to the lab whose cascade it would corroborate.** The surname trap was live and was avoided.

**Declared read depth: FULL TEXT READ — Introduction, Results, Discussion, Methods, and the body text of Tables 1–7.** 60,449 characters retrieved via PubMed MCP `get_full_text_article` on PMC12820071. Copyright status returns `"is_open_access": false` with `"statement": "© 2025. The Author(s)."`; the PMC record nonetheless served the full body.

**NOT obtainable — this is load-bearing for the whole audit:**

1. **Supplementary Table 4** — "A detailed list, including related genomic coordinates and functional annotations, were provided in Supplementary Table 4." This is the *only* place the eight SNPs are individually listed. **Not retrievable on this surface.** Therefore **no rsID, no effect size, no per-SNP p-value and no genomic coordinate for the TRAPPC6A-mapped SNP was ever read.**
2. **Supplementary Table 5** (the SNP→21-gene mapping), **Supplementary Tables 6–7** (All of Us descriptives). Not retrievable.
3. **Fig. 3** — a bar plot, the only display of per-SNP standardized coefficient magnitudes. This environment has **no figure/image tooling**; the panel was **not inspected and is not claimed to have been**.
4. 🔴 **EXTRACTION DEFECT — italicised gene symbols are systematically stripped from the PMC body text.** This is not an absence of data; it is a silent deletion. Demonstration, Methods, verbatim:

   > "Thegene has two key variants, rs7412 and rs429358, which determine the three common isoforms of the apolipoprotein E (apoE) protein"

   "The*APOE* gene" → "Thegene". Every italicised gene symbol in the body is gone. **The string `TRAPPC6A` therefore appears ZERO times in the 60kB body text**, and so do `APOE`, `BIN1`, `CLU`, `PVRL2`, `TOMM40` as running-text symbols. The gene names survive only in (a) the PubMed abstract record, (b) non-italic table headers such as `APOE-ε4 count`.

   **Consequence: every TRAPPC6A-specific statement in this audit rests on the abstract plus positional elimination, never on a readable sentence in the Results naming the gene.** This is stated once here and not softened later.

---

## 1 · What is the actual TRAPPC6A result?

**Finding: there is no TRAPPC6A "result" in the reportable sense. There is a gene name on a mapping list.**

The only text in the entire paper that names the gene is the abstract (PubMed record, verbatim):

> "The multi-task learning approach identified eight shared-risk single nucleotide polymorphisms mapping to key genes including the APOE-TOMM40-APOC1 cluster, BIN1, CLU, PVRL2, and TRAPPC6A."

Note the construction: eight **SNPs** *mapping to* genes. TRAPPC6A is an **annotation of a variant**, not a tested unit. The Results make the inflation ratio explicit — verbatim, with `[ ]` marking symbols the extractor deleted:

> "The eight shared risk SNPs were mapped to 21 genes using positional, expression quantitative trait loci (eQTL), and chromatin interaction mapping techniques."

**Eight SNPs → twenty-one genes.** TRAPPC6A is one of 21 gene labels derived from 8 variants. Methods, verbatim, give the mapping windows:

> "(1) positional mapping based on genomic coordinates from the GRCh38 reference genome, mapping SNPs to genes within ± 100 kb windows; (2) eQTL mapping using data from the GTEx v8 database … (3) chromatin interaction mapping using Hi-C data"

A ±100 kb window plus eQTL plus Hi-C will attach many genes to one signal. **Nothing in this establishes that TRAPPC6A is the causal gene at its SNP.**

**The SNP-level statistic.** The relevant Results paragraph, verbatim:

> "The model identified nine SNPs with non-zero weights for both phenotype prediction tasks. Among these, eight SNPs were identified as shared genetic risk factors for AD and LOE, defined by having coefficients in the same direction for both conditions. Seven of the eight were SNPs from the AD GWAS. The standardized coefficient magnitudes for these shared risk factors are presented in Fig.. A detailed list, including related genomic coordinates and functional annotations, were provided in Supplementary Table 4."

Three things follow, all of them limiting:

- The reported quantity is an **Elastic Net standardized coefficient**, not an odds ratio and **not a p-value**. This is a penalised-regression selection weight. It has no inferential calibration and no multiple-testing frame.
- "Shared" is defined by **sign agreement only** — "coefficients in the same direction for both conditions." That is the entire criterion. A variant with a large AD coefficient and a near-zero LOE coefficient of the same sign qualifies.
- **"Seven of the eight were SNPs from the AD GWAS."** Only ONE of the eight entered from the epilepsy GWAS. Which one is shown by colour in Fig. 3 ("SNPs identified from the epilepsy GWAS are marked in orange") — **a figure this environment cannot read.** Whether TRAPPC6A's SNP is the single epilepsy-GWAS variant or one of the seven AD-GWAS variants **CANNOT BE DETERMINED ON THIS SURFACE.** Prior probability alone puts it at 7:1 against.

**Cohort of discovery, and whether it replicated.** Discovery was UCLA ATLAS — and the modelling sample is far smaller than the headline N:

> "The modeling sample (= 9,986) was further restricted by applying stricter inclusion criteria to controls: age at last visit ≥ 70 and a minimum of five years of records … Given the limited number of cases for both phenotypes (658 cases for LOE and 376 cases for AD)"

**The eight SNPs were selected against 376 AD cases and 658 LOE cases.** N = 416,212 is the EHR denominator, not the genetic discovery set. **All of Us did not replicate the SNPs.** The validation repeated the longitudinal AD↔LOE models and the composite risk score only; there is no SNP-level replication anywhere in the paper. **No independent replication of the TRAPPC6A variant exists in this work.**

---

## 2 · 🔴 Is TRAPPC6A independent of APOE?

**Finding: NO conditional analysis, NO LD pruning, and by the paper's own arithmetic the TRAPPC6A signal sits in the chr19 / APOE-region group.**

### 2a · LD was deliberately retained, not removed

Methods, verbatim — the authors chose Elastic Net *because* it tolerates LD, which is the opposite of resolving it:

> "This approach enhances model stability and variance handling, aiding in variable selection by reducing the coefficients of less relevant variables to zero, thereby simplifying the model and improving its ability to manage multicollinearity—particularly useful given the many SNP features in linkage disequilibrium (LD)."

A search of the full text for `conditional`, `clump`, `prun` (in the sense of LD) returns **no conditional analysis and no LD clumping of the candidate set**. The single use of "pruned" is a QC step on imputation quality, unrelated:

> "SNPs with an imputation r² below 0.90 or a minor allele frequency of less than 1% were pruned."

**There is no analysis anywhere in this paper that conditions a shared-risk SNP on APOE genotype.**

### 2b · The paper partitions its own eight SNPs — and TRAPPC6A is not in the non-APOE partition

The authors themselves ran the APOE-dominance check, and in doing so enumerated exactly which variants lie outside the APOE region. Sensitivity analyses, verbatim:

> "To address potential concerns aboutregion dominance in our shared genetic risk score, we conducted additional analyses focusing exclusively on the four shared risk variants located outside theregion (chr2:127133851, chr8:27607412, chr10:11676714, and chr2:103489151). These variants map to,,, andgenes, respectively."

**The four outside-APOE variants are on chr2, chr8, chr10 and chr2. None is on chr19.** Eight shared SNPs minus four outside = **four remaining, all in the chr19 group the paper calls "near the APOE region"**:

> "A set of shared risk SNPs was identified near theregion. Among these, chr19:44885243 was the top SNP with the highest coefficient magnitude, particularly in predicting AD. Additionally, SNPs outside theregion, such as chr2:127133851, chr8:27607412, and chr10:11676714, also contributed significantly to the shared genetic risk"

TRAPPC6A is at **chr19q13.32** (external reference knowledge — **the paper never states TRAPPC6A's coordinate**, it is in the unreadable Supplementary Table 4). Since no outside-APOE variant is on chr19, **the TRAPPC6A annotation must derive from one of the four chr19 variants in the APOE-region group.** The abstract's own gene ordering is consistent: `PVRL2` — which is immediately adjacent to `TOMM40`/`APOE` and unambiguously inside that LD block — is listed alongside `TRAPPC6A`, after the three chr2/chr8 genes.

⚠️ **This is elimination logic, not a quotation.** The paper does not say "TRAPPC6A is in the APOE region." It says four variants are outside and names their chromosomes; chr19 is not among them. The inference is sound but it is an inference, and it is recorded as one.

### 2c · What the LD block actually spans, in the authors' words

> "This entire region was removed due to the dense LD block observed in European ancestries, which overlaps these three genes (,,)."

and

> "Theregion(including the overlapping linkage disequilibrium (LD) block withandgenes), emerged as an essential genomic risk locus among the mapped shared risk genes"

The authors treat chr19 around APOE as a **single dense LD block in Europeans** — and this study is **European-ancestry only**:

> "Another limitation is the study's applicability to individuals of European ancestry only."

European ancestry is precisely the population in which APOE-region LD is most extended. The excised window they used for the PRS is narrow — "chromosome 19 near(44,891,220 to 44,919,349, GRCh38)", about 28 kb — while their top SNP, chr19:44885243, lies just outside even that. **A 28 kb excision does not establish independence from a "dense LD block."**

### 2d · Verdict on question 2

**Not independent of APOE, and the paper never tests it.** No conditional analysis, no clumping, LD explicitly accommodated rather than resolved, and the gene sits in the chr19 partition the authors themselves segregate as APOE-region. **A locus in LD with APOE is not an independent epilepsy signal, and this paper supplies nothing that would separate the two.**

---

## 3 · Does the epilepsy association separate from the Alzheimer association?

**Finding: NO. The epilepsy arm is null in both cohorts, and the authors say so themselves.**

This is where the abstract and the Results diverge most sharply. The abstract offers "A shared genetic risk score effectively stratified patients into distinct AD-LOE risk groups." The tables say otherwise.

**UCLA discovery — Table 5, verbatim rows:**

| Predictor | Phenotype | Variation explained | OR (95% CI) | p |
|---|---|---|---|---|
| APOE-ε4 count | AD or LOE | 1.44% | 1.90 (1.41, 2.53) | < 0.001* |
| APOE-ε4 count | AD only | 7.57% | 4.31 (2.75, 6.78) | < 0.001* |
| APOE-ε4 count | **LOE only** | 0.01% | **1.05 (0.70, 1.54)** | **0.81** |
| AD-LOE shared GRS (full) | AD or LOE | 1.79% | 1.42 (1.22, 1.64) | < 0.001* |
| AD-LOE shared GRS (full) | AD only | 6.87% | 2.10 (1.64, 2.71) | < 0.001* |
| AD-LOE shared GRS (full) | **LOE only** | 0.29% | **1.16 (0.97, 1.38)** | **0.1** |
| AD-LOE shared GRS (without APOE) | AD or LOE | 0.63% | 1.24 (1.06, 1.45) | 0.01* |
| AD-LOE shared GRS (without APOE) | AD only | 0.72% | 1.28 (0.99, 1.66) | 0.056 |
| AD-LOE shared GRS (without APOE) | **LOE only** | 0.49% | **1.21 (1.01, 1.46)** | **0.04*** |

**The full shared GRS does not reach significance for epilepsy in the discovery cohort (p = 0.1).** The authors state it plainly:

> "a borderline 1.16-fold increase in the risk of LOE (95% CI: 0.97, 1.38) … However, no association was observed betweenallele count and LOE. While both-ε4 and the shared GRS were associated with the combined AD or LOE phenotype, the associations appeared to be primarily driven by AD cases rather than showing equivalent effects across both conditions individually."

**All of Us validation — Table 7, verbatim rows:**

| Predictor | Phenotype | Variation explained | OR (95% CI) | p |
|---|---|---|---|---|
| APOE-ε4 count | AD only | 0.46% | 1.98 (1.42, 2.84) | < 0.001* |
| APOE-ε4 count | **LOE only** | < 0.01% | **1.04 (0.90, 1.20)** | **0.59** |
| AD-LOE shared GRS (full) | AD only | 2.02% | 1.54 (1.40, 1.69) | < 0.001* |
| AD-LOE shared GRS (full) | **LOE only** | < 0.01% | **1.01 (0.96, 1.06)** | **0.80** |
| AD-LOE shared GRS (without APOE) | AD or LOE | 0.01% | 1.04 (0.95, 1.14) | 0.41 |
| AD-LOE shared GRS (without APOE) | AD only | 0.06% | 1.17 (0.96, 1.42) | 0.12 |
| AD-LOE shared GRS (without APOE) | **LOE only** | 0.02% | **1.09 (0.98, 1.20)** | **0.11** |

🔴 **This is the inversion.** In the validation cohort:

- The full shared GRS → LOE is **OR 1.01, p = 0.80, variance explained < 0.01%.** That is an exact null.
- **The entire non-APOE component of the score is null for every single phenotype** — AD or LOE p = 0.41, AD only p = 0.12, LOE only p = 0.11.
- The one UCLA result that looked like independent epilepsy signal — non-APOE GRS → LOE-only, OR 1.21, p = 0.04 — **failed to replicate** (All of Us OR 1.09, 95% CI 0.98–1.20, p = 0.11).

**And that UCLA result, even had it replicated, would not have implicated TRAPPC6A**: the "without APOE" score is built from exactly the four non-chr19 variants (chr2/chr8/chr10/chr2), i.e. **the partition that excludes TRAPPC6A** (§2b). The only LOE-positive finding in the paper comes from a score that leaves TRAPPC6A out.

**The authors' own concession**, verbatim:

> "First, pathway enrichment analyses primarily highlighted AD-related biological processes, with minimal evidence supporting epilepsy-specific pathways, suggesting a more limited genetic overlap than initially hypothesized. Second, we observed no significant association betweenand LOE in the All of Us cohort, a finding that diverges from some prior reports and calls into question the strength of's contribution to LOE susceptibility. Finally, associations with the shared genetic risk score appeared to be driven predominantly by AD cases, rather than showing comparable effects across both conditions. Collectively, these findings provide only limited evidence for shared genetic architecture"

and in the Results:

> "Notably, the most significantly enriched pathways were primarily associated with AD pathogenesis, with limited evidence for epilepsy-specific pathways."

**There is no analysis anywhere in this paper of TRAPPC6A against late-onset epilepsy on its own.** Sharing was defined by coefficient sign agreement in a joint model, and 7 of 8 variants entered from the AD GWAS. **Epilepsy does not separate from Alzheimer's here — it collapses into it.**

---

## 4 · Gene or isoform?

**Finding: gene-level only. The word "isoform" appears exactly once in the entire paper, and it refers to APOE protein isoforms.**

Exhaustive search of the 60kB body for `isoform`, `splic*`, `transcript`, `delta`, `Δ`, `TIAF1` returns **one** hit, verbatim:

> "Thegene has two key variants, rs7412 and rs429358, which determine the three common isoforms of the apolipoprotein E (apoE) protein: E2, E3, and E4, encoded by the ε2, ε3, and ε4 alleles, respectively."

That is APOE E2/E3/E4. **Nothing else.**

- **`TRAPPC6AΔ` does not appear. Neither does any Δ isoform, any splice variant, any alternative transcript, and `TIAF1` appears nowhere in the paper.**
- The analytic surface is **variant-level and gene-level throughout**. Methods: "Functional consequences of each variant were predicted using the Ensembl Variant Effect Predictor (VEP) database, which integrates multiple prediction algorithms including SIFT, PolyPhen-2, and CADD scores." VEP/SIFT/PolyPhen/CADD operate on variants and canonical protein consequence; **none of this is transcript-resolved isoform analysis.**
- eQTL mapping used **GTEx v8 gene-level expression** in brain tissues. Gene-level eQTL says nothing about which isoform is expressed.

**This paper contains zero evidence bearing on TRAPPC6AΔ.** It could not, by design.

---

## 5 · Study-design honesty — the authors' stated limitations

Quoted verbatim, in full, because the hedging is unusually frank and it matters:

**On phenotyping:**
> "The prevalences of AD and LOE were lower in both our discovery and validation datasets, likely reflecting the under-diagnosis of both conditions in EHRs. Participant samples in our study were selected based on ICD-10 diagnosis codes retrieved from EHRs, which could be subject to misclassifications. For example, individuals classified with LOE could also have undiagnosed mild cognitive impairment or AD. Similarly, some diagnosed with AD could exhibit subclinical seizures."

This is circular-contamination risk pointed directly at the shared-risk claim: if LOE cases are partly undiagnosed AD, an APOE-region variant will look "shared" without any epilepsy biology.

**On ancestry:**
> "Another limitation is the study's applicability to individuals of European ancestry only. Due to the small sample sizes of other ancestry groups in our dataset, we did not perform modeling for these populations. As a result, the generalizability of our findings to other ancestries is limited."

**On the absence of an LOE GWAS — the foundational substitution:**
> "One possible explanation is that we used a generalized epilepsyGWAS due to the lack of GWAS data specific to LOE, and the genetic risk factors may differ between these conditions."

The epilepsy candidate SNPs did not come from late-onset epilepsy at all. They came from a **generalized epilepsy** GWAS, a different phenotype.

**On the null starting point:**
> "Initially, we attempted to estimate the genetic correlation between these conditions using the established LDSC tool. However, results indicated no significant genetic correlation between AD and generalized epilepsy."

**The standard method returned no genetic correlation.** The multi-task Elastic Net was built *after* that null, explicitly to look again:

> "Despite the null results from LDSC, we hypothesized the existence of underlying genetic predispositions and overlapping biological pathways between AD and LOE. This led us to develop a multi-task Elastic Net model"

**On the overall strength of claim:**
> "Our findings provide initial evidence for potential shared genetic architecture between AD and LOE within a European population, though the extent and independence of this shared architecture require further investigation."

> "the extent of shared genetic architecture between AD and LOE appears limited and requires further validation in larger, more diverse cohorts."

The authors themselves flag **"independence"** as unresolved. They are not overclaiming; a downstream reader citing "TRAPPC6A is an epilepsy risk gene" would be.

---

## 6 · VERDICT

### Proposition under test: *"`TRAPPC6A` is an independently supported epilepsy risk locus."*

# `WEAK — large-screen hit, not validated`

The proposition fails on all three of its load-bearing words, and the per-SNP numbers that might have rescued it are unreadable on this surface.

| Word in the proposition | Status | Basis |
|---|---|---|
| **"independently"** (of APOE) | **Fails.** No conditional analysis, no LD clumping; LD explicitly accommodated by the model. Gene is in the chr19 partition the authors themselves segregate as APOE-region — the four non-APOE variants are chr2/chr8/chr10/chr2. | §2 |
| **"epilepsy"** | **Fails.** Full shared GRS → LOE: p = 0.1 (UCLA), **p = 0.80, OR 1.01 (All of Us)**. APOE-ε4 → LOE: p = 0.81 / p = 0.59. Enrichment "primarily associated with AD pathogenesis, with limited evidence for epilepsy-specific pathways." 7 of 8 SNPs came from the AD GWAS. No TRAPPC6A-vs-LOE test exists. | §3 |
| **"supported… locus"** | **Fails / undetermined.** One of 21 genes mapped from 8 penalised-regression coefficients selected against 376 AD and 658 LOE cases. No OR, no p-value, no rsID readable. No SNP-level replication in All of Us. | §1 |

**Sub-verdict, recorded separately and honestly:** on the narrow question *"what is the effect size and p-value of the TRAPPC6A SNP?"* the answer is **`CANNOT DETERMINE ON THIS SURFACE`** — that number lives in Supplementary Table 4 and Fig. 3, neither of which this environment can read. But the determination above does not depend on it: **even a large Elastic Net coefficient would not make an APOE-region chr19 variant an independent epilepsy signal when the epilepsy arm of the score is null in both cohorts.**

**What would change this verdict:** Supplementary Table 4 showing the TRAPPC6A SNP's rsID and coordinate at genuine distance from the APOE LD block *and* a conditional analysis on APOE genotype *and* a TRAPPC6A-specific LOE association surviving in All of Us. None of the three exists in this paper.

**Do not inflate.** Being named in a shared-risk abstract is not being a validated epilepsy gene.

---

## 7 · What this does and does not do for the Chang cascade's first node

**The disambiguation held, and that is a real result.** This is an authentically external paper: Timothy S. Chang (UCLA) has no connection to Nan-Shan Chang (NCKU), and Fu et al. plainly had no interest in, and no awareness of, the NCKU TIAF1/TRAPPC6AΔ cascade. Had `TRAPPC6A` carried a clean, APOE-independent epilepsy association here, it would have been exactly the external corroboration the node-independence audit was looking for. **It does not carry one.**

**What this paper does do:** it confirms that the *gene symbol* `TRAPPC6A` exists in the published genetic literature outside NCKU, attached to a neurodegeneration screen, as one of twenty-one gene labels mapped from eight variants. That is a faint mark of the locus being biologically looked at by someone else. It is the *weakest* usable form of external attestation — presence on an annotation list.

**What this paper does not do — four things, and they should be recorded as four:**

1. **It does not corroborate the Δ isoform.** `TRAPPC6AΔ` appears nowhere; no splicing, transcript or isoform analysis of any kind was performed (§4). The distinction the audit was built to hold is intact and the answer is unambiguous: **corroborating the locus is not corroborating the isoform, and here not even the locus is corroborated.** `TRAPPC6AΔ` remains a single-laboratory observation with **zero independent replication**. The node-independence finding stands unweakened.

2. **It does not supply an epilepsy association.** The epilepsy arm is null in the validation cohort (OR 1.01, p = 0.80). The proposed reading — "the gene at the head of the cascade is independently an epilepsy risk locus" — is not supported by the paper it was drawn from. The abstract's gene list invited that reading; the Results refuse it. **This is a seventh abstract-versus-results inversion in this literature in three days**, and the sharpest yet: an exact null (p = 0.80) sitting under a sentence about a score that "effectively stratified patients."

3. **It does not survive the APOE confound.** A chr19 variant in a dense European LD block, never conditioned on APOE, is not evidence about TRAPPC6A specifically. It is evidence about chr19q13. Attributing it to TRAPPC6A rather than to APOE/TOMM40/APOC1/PVRL2 is a mapping-window artefact, not a finding.

4. 🔴 **Even at its strongest, it would be the wrong kind of evidence for this disease model.** A common-variant risk locus for **late-onset epilepsy in elderly adults** — median case age at last visit 75.8 years, discovered in a cohort restricted to controls "age at last visit ≥ 70" — is a different object from a **neonatal-onset developmental and epileptic encephalopathy driven by biallelic loss of function**. Small-effect common-variant susceptibility in an ageing brain and Mendelian developmental encephalopathy are not the same causal regime, and a shared gene symbol does not bridge them. Even a `SUPPORTED` verdict here would not have licensed a mechanistic inference into a WWOX-DEE model; it would have licensed only the narrow statement that the locus is real outside NCKU.

**Net effect on the cascade's first node: unchanged, and the attempted repair failed cleanly.** The Chang mechanistic chain still rests on two NCKU-internal proteins — TIAF1 and TRAPPC6AΔ — with no external replication of either. The strongest candidate for external support of the `TRAPPC6A` gene turns out, on full-text reading, to be an APOE-region annotation in an AD-driven screen whose epilepsy signal is null on replication. **The loop opened by the node-independence audit closes negative.** That is a useful result: it converts an open question into a settled one, and it removes a corroboration the model might otherwise have been tempted to lean on.

---

*Non-canonical analysis. No canonical file was read for modification or written. No commit candidate produced. Nothing here is medical advice.*
