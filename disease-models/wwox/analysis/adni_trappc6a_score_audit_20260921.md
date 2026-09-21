# FT-098 — Park 2020 (ADNI/AddNeuroMed transcriptional risk score): audit of the `TRAPPC6A` leg

**Target.** PMID 33134515 · PMCID PMC7577551 · DOI 10.1212/NXG.0000000000000517
Park YH, Hodges A, Simmons A, Lovestone S, Weiner MW, Kim S, Saykin AJ, Nho K.
*Association of blood-based transcriptional risk scores with biomarkers for Alzheimer disease.*
**Neurol Genet** 2020;6(6):e517. Identifiers, title and author list verified against
`mcp__PubMed__get_article_metadata` on 2026-09-21 — **all match the task brief.**

**Source artefact.** `files/fulltext/PMID33134515_PMC_MCPtext.txt` —
22,730 bytes · sha256 `16fff9c826cf2b630a3aa84e96d382353da352ef047546b93607a2f46d559b0c`.
Body only; the abstract is reproduced in this file (§8) and deliberately kept out of the artefact.

**Licence.** `get_copyright_status` returns
`"Copyright © 2020 The Author(s). Published by Wolters Kluwer Health, Inc. on behalf of the
American Academy of Neurology."`, `license.type: null`, `license.url: null`,
`is_open_access: false`, `source: "pubmed"`, `checked_sources: ["pubmed"]`,
`found_in_pmc: 0`. **PMC was never consulted by that call.** A direct
`get_full_text_article(["PMC7577551"])` returned a complete body — Introduction through
Conclusion, including Methods, Results, Discussion and limitations. **The paper is not
licence-walled on this surface.** The earlier `licence-walled, unread` classification rested on a
flag produced without querying the repository that in fact serves the text.

---

## 0 · VERDICT

**This paper can bear on the `TRAPPC6A` node-independence question, and it bears against it.**

The gene is readable here — not by symbol, which the extractor destroyed, but by its full HGNC
name in Roman type in the Discussion: *"encodes trafficking protein particle complex 6A."* That
sentence is unambiguous and requires no reconstruction.

What it says is decisive in the opposite direction from the Wave 2 claim. This is a
**blood transcriptomic case-control study**, not a human-genetic study. It performed **no genetic
association test of its own** on `TRAPPC6A`; its genetic input is other people's GWAS summary
statistics passed through COLOC and SMR. Its headline result is a **six-gene composite score**, and
its only statement about a neurocognitive role for `TRAPPC6A` is an **external citation** —
*"genetic variation of[TRAPPC6A] is reported to be associated with nonverbal reasoning"* —
immediately preceded by the authors' own disclaimer *"it is not clear how it affects the
pathogenesis of AD."* A cited nonverbal-reasoning association is not this paper's finding. It is a
pointer to someone else's, and the phenotype named is the phenotype of leg 3.

So `FT-098` is **not an independent leg**. It is a **re-citation of leg 1/leg 3 material inside a
composite-score paper about Alzheimer disease.** It was never independent support, and it does not
become support now that it has been read.

Two things the extraction genuinely prevented. The **six gene symbols cannot be individually
resolved in the Results**, so the per-gene up/down slot that `TRAPPC6A` occupies is not readable.
And **no figure is inspectable**; per **D-14** no negative asserted only by a figure is adjudicated
here. Neither limitation touches the verdict, which rests on quoted Roman-type prose.

---

## 1 · Study design and unit of analysis

**Design.** Case-control, cross-sectional, two cohorts, discovery plus replication. From
*Participants*: *"Data used in the study were obtained from Caucasian participants (AD, mild
cognitive impairment [MCI], and cognitively normal controls [CN]) in the Alzheimer's Disease
Neuroimaging Initiative (ADNI) and AddNeuroMed cohorts as discovery and replication samples,
respectively."* **ADNI is discovery; AddNeuroMed is replication.**

**N.** From *Results*: *"a total of 1,335 participants were included from 2 independent cohorts
(661 from the ADNI and 674 from AddNeuroMed)"*. The diagnosis-group comparison is smaller:
Table 3's caption reads *"Difference of the TRS between CN (N = 213) and AD (N = 103) ... in
ADNI"*. **The ADNI case-control contrast is 103 cases vs 213 controls**, not 661.

**Tissue and measurement.** Whole blood; **transcriptomic**, by microarray. From *Blood-based RNA
expression microarray profiling*: *"The PAXgene Blood RNA Kit ... was used to purify total RNA from
whole blood collected in a PAXgene Blood RNA Tube."* and *"The Affymetrix Human Genome U219 Array
... in the ADNI and the Illumina Human HT-12 v3 Expression BeadChips ... in AddNeuroMed were used
for expression profiling."* After QC: *"the RNA expression profiles, which contained 21,150 probes
in the ADNI and 5,141 probes in AddNeuroMed"*.

**Unit of analysis.** The individual participant, carrying one scalar **transcriptional risk score
(TRS)**. From *Calculation of the TRS*: *"Finally, we calculated the TRS for each individual by
summing the polarized-scores over the corresponding genes."*

**Genotyping is present but instrumental, not the endpoint.** Genotypes were used for ancestry QC,
for imputation, and — through the *public* blood eQTL database and *published* AD GWAS summary
statistics — to choose and polarise genes. From *Selection of AD-associated SNPs and candidate
genes*: *"we started by considering 29 SNPs that had genome-wide significant associations
(< 5 × 10) in a recent AD GWAS meta-analysis"*. **No new genetic association was estimated in
these cohorts.** Imaging enters only as an outcome variable (FreeSurfer 5.1 hippocampal volume and
entorhinal cortical thickness, florbetapir PET SUV, ADAS-cog13).

**Method class, counted honestly.** Roman-type method words survive extraction and their counts are
informative: `COLOC` 18, `SMR` 15, `mendelian randomization` 3, `probe` 5, `transcript*` 11.
`blind` **0** and `permutation` **0** — both genuine zeros in the Roman class. This study is
**neither blinded nor permutation-tested**; it is a regression analysis with a replication cohort.

---

## 2 · Is `TRAPPC6A` identifiable?

**Yes — in the body, once, by full name; nowhere by symbol; and not at all in the abstract.**

Where it **cannot** be seen:

- **As a symbol in the body: 0 occurrences.** `grep -c TRAPPC6A` on the artefact returns **0**.
  This is the instrument, not the paper. Every italicised gene symbol in this source has been
  deleted by the extractor. Controls confirm the destruction is systematic and not specific to this
  gene: `CD33` 0, `APOE` 0 — and the sentence *"we evaluated discrepancies between the reported sex
  and sex determined from sex-specific gene expression data, includingand."* has lost **two**
  symbols mid-sentence, leaving the word-collision *"includingand"*.
- **In the Results sentence that assigns direction: not resolvable.** The sentence reads verbatim
  *"Among 6 target genes identified by COLOC and SMR from AD-associated SNPs with< 1 × 10, 2 genes
  (and) and 4 genes (,,, and) were labeled as high expression and low expression, respectively."*
  Six symbols, six empty slots. **No negative about `TRAPPC6A` may be drawn from this.**
- **In the PubMed metadata abstract: also destroyed.** The metadata abstract was checked as an
  independent surface and **it does not rescue the symbols**: *"Among functional genes identified to
  calculate the TRS,andwere significantly upregulated, andwas significantly downregulated"*. The
  usual cross-check fails here; both surfaces are damaged identically.

Where it **can** be seen — the finding:

- **Discussion, third gene paragraph, verbatim and complete:**
  > *"encodes trafficking protein particle complex 6A. Although it is not clear how it affects the
  > pathogenesis of AD, genetic variation ofis reported to be associated with nonverbal reasoning."*

  *"trafficking protein particle complex 6A"* is the HGNC approved **name** of `TRAPPC6A`. It is set
  in Roman type, so it survived. This is a direct reading, not a reconstruction: the paragraph's
  leading symbol and one mid-sentence symbol are gone, but the expanded name identifies the gene
  outright.

Two companion genes are recoverable the same way and are recorded here only to show the mechanism
is general, not to support any claim: the second Discussion paragraph reads *"encodes paired
immunoglobulin-like type 2 receptor alpha"* and then uses **`PILRA`** five times in Roman type as a
protein name; the first paragraph gives no name but cites `rs3865444`.

**What remains unreadable, and is therefore not asserted.** Which of the six slots `TRAPPC6A`
occupies — high- or low-expression label, significant or not, ADNI or AddNeuroMed — **cannot be
read on this surface.** The Discussion devotes exactly three paragraphs to genes, directly after
the sentence *"we found that expression levels of 2 genes (and) were significantly increased, and 1
gene () was significantly decreased ... The expression of these genes in peripheral blood may be
associated with the corresponding AD-associated SNPs"*, which suggests the three elaborated genes
are the three replicated ones. That is an inference from document structure. Assigning *which* of
the three is the downregulated one would require matching by order, and **order-matching is
forbidden**: it would be a fabricated gene identity. It is left open.

---

## 3 · The claimed result and its strength

The claim is about **the score**, and the score's effects are small.

**Diagnosis, ADNI (discovery).** From *Results*: *"when AD-associated SNPs with< 1 × 10were
selected to identify candidate genes, the diagnosis group difference of the TRS for target genes
identified by COLOC or SMR was the largest (OR 1.18, 95% CI 1.07–1.31 for COLOC; OR 1.18, 95% CI
1.06–1.33 for SMR)"*. The uncolocalised comparator is weaker: *"the TRS of the candidate genes
without the colocalization step was significantly different between AD and CN in the ADNI (odds
ratio [OR] 1.06, 95% CI 1.01–1.13)"*, rising to *"(OR 1.08, 95% CI 1.02–1.15)"* with COLOC.

**Diagnosis, AddNeuroMed (replication).** *"the diagnosis group difference of the TRS for target
genes identified by COLOC or SMR was the largest (OR 1.20, 95% CI 1.12–1.30 for COLOC; OR 1.23, 95%
CI 1.13–1.35 for SMR)"*.

**Amyloid-stratified sensitivity, ADNI.** *"The result remained significant when the TRS was
compared between patients with AD with positive amyloid PET and CN with negative amyloid PET (OR
1.21, 95% CI 1.07–1.39 for COLOC; OR 1.24, 95% CI 1.08–1.43 for SMR)."*

**Imaging and cognition.** *"The TRS of target genes identified by COLOC or SMR was associated with
MRI-based imaging biomarkers (hippocampal volume and entorhinal cortical thickness), cortical
amyloid accumulation and ADAS-cog13 in the ADNI"*. And the replication is **partial**: *"In
AddNeuroMed, the TRS of target genes identified by COLOC or SMR was also associated with entorhinal
cortical thickness ... There was no significant association between the TRS and the hippocampal
volume in AddNeuroMed."*

**Strength, stated plainly.** Odds ratios of **1.18–1.24 per unit of score**, with lower confidence
bounds at 1.06–1.13. Entorhinal thickness replicates; **hippocampal volume does not**. Every
numeric association for imaging, amyloid and cognition sits in supplementary tables e-1 to e-7 and
figures e-1 to e-3, which are **not present on this surface** — so the imaging effect sizes and
their corrections are **unread**, and none is asserted here.

**Corrections.** Bonferroni is stated for **gene selection only**: *"Multiple testing correction was
performed using the Bonferroni method (< 8.4 × 10)"*, in the COLOC/SMR section. The exponent is
destroyed. **No multiple-testing correction is stated anywhere for the per-gene diagnosis
regressions** (§5) or for the TRS-biomarker regressions in the main text. Covariates are modest:
*"Covariates included age and sex."*, plus ICV and MRI field strength for the two structural
measures and education for ADAS-cog13. **`APOE` is genotyped but is not listed as a covariate in
any model described in the main text.**

*All p-value exponents in this source are destroyed by the extractor* — *"< 5 × 10"*,
*"< 1 × 10"*, *"< 8.4 × 10"*. No threshold is reconstructed anywhere in this audit.

---

## 4 · Class of evidence

The statement exists and is quoted here in full. It appears **twice**, and the sentences are
identical. Once at the end of *Statistical analysis*:

> *"The study is rated Class III because of the case control design and the risk of spectrum bias."*

and again as the abstract's *Classification of evidence* section (metadata surface):

> *"The study is rated Class III because of the case control design and the risk of spectrum bias."*

**The paper names its own two weaknesses in the same breath as the rating**: `case control design`
and `spectrum bias`. Roman-type counts: `Class III` 1, `spectrum bias` 1 in the body.

On generalisability the paper is equally direct, in *limitations*: *"Second, the ADNI participants
may not be representative of the general population of older adults. To generalize our findings, we
need to validate our findings in larger community-based prospective cohort studies."* And on
causality: *"Finally, we analyzed cross-sectionally collected gene expression data. Our findings
thus represent association not causality."*

The participant base is further narrowed by ancestry filtering — *"only non-Hispanic participants of
European ancestry that clustered with HapMap CEU ... or Toscani in Italia populations"* — which is
correct practice for the analysis and a further limit on generalisability.

---

## 5 · Is any single gene load-bearing, or only the composite?

**Only the composite is load-bearing. This is the decisive section.**

Every headline association in this paper is an association of **the TRS**, a sum over six genes.
From *Calculation of the TRS*: *"we polarized gene expression levels by changing the sign of the
expression levels (-score) for genes labeled as low expression. Thus, elevated risk from gene
expression, irrespective of the direction of risk, could be additively incorporated in the TRS."*
A polarised additive sum **erases the identity of its components by construction**: sign is imposed
from the external eQTL database, and the score cannot attribute its association to any one term.

The paper did run a per-gene test — and it is a **secondary, descriptive check that the selection
step behaved**, not an independence test. Its stated purpose, from *Statistical analysis*:

> *"Although we designated target genes as high expression and low expression based on the
> integration of GWAS summary statistics and the public blood eQTL database, expression levels of
> the target genes in the ADNI and AddNeuroMed may not be different between AD and CN. Therefore,
> for target genes used to calculate the TRS, we performed logistic regression analysis of gene
> expression levels using the AD diagnosis group, with age and sex as independent variables and
> diagnosis as an outcome, to identify which genes are significantly upregulated or downregulated
> in AD compared with CN."*

Its outcome, from *Results*: *"In the ADNI, expression levels of 2 genes (and) were significantly
increased, whereas 1 gene () was significantly decreased ... Expression levels of the remaining 3
genes in ADNI were not significantly different between AD and CN."* In AddNeuroMed: *"2 genes (and)
were significantly increased, and 2 genes (and) were significantly decreased ... Expression levels
of the remaining 2 genes in AddNeuroMed were not significantly different"*, converging on *"the
diagnosis group difference and directionality of gene expression levels of,, andthat were
identified in ADNI were replicated in AddNeuroMed."* — **three genes of six.**

Three observations follow, none of which depends on knowing which gene is which:

1. **No effect size, no p-value and no confidence interval is reported in the main text for any
   individual gene.** The per-gene numbers live in table e-7 and figure e-3, both absent here. Even
   a reader with intact gene symbols would have **no quantitative per-gene result** on this surface.
2. **No multiple-testing correction is stated for the six per-gene tests.**
3. **Half the target genes failed the check in ADNI** (3 of 6 not significant), which is itself a
   caution against reading any single component as established.

**For the retracted claim this settles the matter.** Membership in a six-gene polarised sum is not
independent human-genetic support for a member gene. Even the paper's own per-gene follow-up is a
blood expression contrast between AD cases and controls — not a genetic test, and not a
neurocognitive one.

**And the paper says as much about `TRAPPC6A` itself.** Its entire substantive treatment of the gene
is three clauses, quoted in full in §2, and the neurocognitive claim inside them is **explicitly
attributed to someone else**: *"genetic variation ofis reported to be associated with nonverbal
reasoning."* *Is reported to be* — passive, cited, not measured here. The reference number is
destroyed with the superscripts, so **this surface cannot confirm which paper is cited**; the
phenotype descriptor *"nonverbal reasoning"* is readable and is the phenotype of leg 3
(PMID 21766012). The identification of the cited work is left as unverified, but the grammatical
point stands on its own: **whatever paper is cited, this one is citing, not demonstrating.**

---

## 6 · Gene versus isoform

**Gene-level throughout. There is no transcript-level resolution anywhere in this study, and the
answer comes from the Methods, not from string counts.**

Four methodological facts, each quoted:

1. **Microarray, not RNA-seq.** *"The Affymetrix Human Genome U219 Array ... and the Illumina Human
   HT-12 v3 Expression BeadChips ... were used for expression profiling."* Both are 3'-biased
   expression arrays designed to quantify a gene, not to discriminate its isoforms.
2. **One probe per gene, chosen by variance — an explicit collapse to gene level.** *"Finally, if a
   gene contained more than 1 microarray probe, we selected only the probe with the greatest
   variance."* Any isoform-discriminating information carried by the discarded probes is destroyed
   at this step, deliberately and by design.
3. **The eQTL input is gene-level.** *"we identified candidate genes that are located within ±1 Mbp
   of AD-associated and pruned SNPs that have a direct impact on gene expression (false discovery
   rate–corrected< 0.05 for eQTL)"* — gene expression, not transcript or exon usage.
4. **The score sums genes.** *"we transformed expression levels of each gene into a normal
   distribution"* … *"summing the polarized-scores over the corresponding genes."*

Roman-type token counts corroborate and do not carry the argument: `isoform` **0**, `splice` **0**,
`exon` **0**. These are Roman-class words, never italicised, so these zeros are informative — but
the finding rests on the platform and the one-probe-per-gene rule.

**Consequence.** This paper **cannot** distinguish a splice isoform from a full-length transcript
for `TRAPPC6A` or for any other gene. It therefore has **no purchase whatever on the `TRAPPC6AΔ`
isoform question**, consistent with the prior finding that none of the three legs ever bore on it.

---

## 7 · Abstract versus Results, and grammatical mood

**Softening, omission, inversion: essentially none. The paper's abstract is accurate. That is the
finding, and it is worth stating explicitly rather than passing over.**

Claim by claim:

| Abstract says | Body says | Verdict |
|---|---|---|
| *"The TRS was significantly associated with AD diagnosis, hippocampal volume, and entorhinal cortical thickness in the ADNI."* | ADNI: TRS associated with *"hippocampal volume and entorhinal cortical thickness), cortical amyloid accumulation and ADAS-cog13"* | Accurate, and **understates** — amyloid PET and ADAS-cog13 are omitted from the abstract, an omission in the conservative direction |
| *"The association of the TRS with AD diagnosis and entorhinal cortical thickness was also replicated in AddNeuroMed."* | *"There was no significant association between the TRS and the hippocampal volume in AddNeuroMed."* | **Accurate by careful construction.** Hippocampal volume is deliberately dropped from the replication sentence |
| *"The blood-based TRS is significantly associated with AD diagnosis and neuroimaging biomarkers."* | Same, with the hippocampal null | Supported |

**The one soft spot.** The failed hippocampal replication is handled by **omission rather than
statement**. A reader comparing the abstract's two sentences word by word will notice hippocampal
volume present in the first and absent from the second; a reader skimming will not. The body states
the null explicitly and without euphemism. This is **not** an inversion and **not** a misreport — it
is an abstract that is true but requires attentive reading. Recorded as a minor asymmetry, nothing
more.

**Mood of the central claims — checked specifically, because this session has three times found a
source's speculation re-voiced as its finding.** This paper does **not** commit that error. It is
consistently and correctly hedged:

- **Attributed prior knowledge, past passive:** *"In blood,andwere known to be associated with
  uptake of β-amyloid and herpes simplex virus 1 infection, respectively, both of which **may** play
  a role in the pathogenesis of AD."* — `were known to be` is not a claim to have shown it.
- **Speculative, marked:** *"This **suggests** that increased expression levels ofby rs3865444
  **may** interfere with peripheral uptake of Aβ, which **could** play a role in the pathogenesis of
  AD."*
- **Speculative, marked:** *"altered expression ofby rs1859788**may** be protective for AD due to
  decreased reactivation of HSV-1."*
- **Explicit ignorance, on `TRAPPC6A` specifically:** *"Although it is **not clear** how it affects
  the pathogenesis of AD, genetic variation ofis **reported to be** associated with nonverbal
  reasoning."*
- **Causal discipline:** *"Our findings thus represent association not causality."*

**Where the failure mode occurred is on LEGEND's side, not the source's.** Park et al. wrote
*"is reported to be associated with nonverbal reasoning"* — a citation, flagged as a citation, sitting
next to an admission that no mechanism is known. Wave 2 read that as an independent human-genetic
finding for `TRAPPC6A`. **The paper did not overstate; the reading did.** This is the same failure
mode found three times elsewhere in this session, and here it is caught at its cleanest: the source
is innocent and the re-voicing is ours.

---

## 8 · Abstract as retrieved (metadata surface, reproduced here and not in the artefact)

Reproduced for the §7 comparison, labelled **metadata, not body text**. Gene symbols are destroyed
here as they are in the body.

> **Objective** — *"To determine whether transcriptional risk scores (TRSs), a summation of
> polarized expression levels of functional genes, reflect the risk of Alzheimer disease (AD)."*
>
> **Methods** — *"Blood transcriptome data were from Caucasian participants, which included AD, mild
> cognitive impairment, and cognitively normal controls (CN) in the Alzheimer's Disease
> Neuroimaging Initiative (ADNI, n = 661) and AddNeuroMed (n = 674) cohorts. To calculate TRSs, we
> selected functional genes that were expressed under the control of the AD risk loci and were
> identified as being responsible for AD by using Bayesian colocalization and mendelian
> randomization methods. Regression was used to investigate the association of the TRS with
> diagnosis (AD vs CN) and MRI biomarkers (entorhinal thickness and hippocampal volume). Regression
> was also used to evaluate whether expression of each functional gene was associated with AD
> diagnosis."*
>
> **Results** — *"The TRS was significantly associated with AD diagnosis, hippocampal volume, and
> entorhinal cortical thickness in the ADNI. The association of the TRS with AD diagnosis and
> entorhinal cortical thickness was also replicated in AddNeuroMed. Among functional genes
> identified to calculate the TRS,andwere significantly upregulated, andwas significantly
> downregulated in patients with AD compared with CN, all of which were identified in the ADNI and
> replicated in AddNeuroMed."*
>
> **Conclusions** — *"The blood-based TRS is significantly associated with AD diagnosis and
> neuroimaging biomarkers. In blood,andwere known to be associated with uptake of β-amyloid and
> herpes simplex virus 1 infection, respectively, both of which may play a role in the pathogenesis
> of AD."*
>
> **Classification of evidence** — *"The study is rated Class III because of the case control design
> and the risk of spectrum bias."*

---

## 9 · What LEGEND may now record for `FT-098`

Proposals only. This audit is READ-ONLY and writes no registry, queue, ledger or current file.

**Correct the access status.**
`FT-098` must stop being carried as **licence-walled**. It is **open on the PMC route and now
read**. The classification error is reproducible and worth recording as a lesson in its own right:
`get_copyright_status` returned `is_open_access: false` with `checked_sources: ["pubmed"]` and
`found_in_pmc: 0`, and that flag was treated as a wall. **A copyright call that has not consulted
PMC cannot establish that PMC will not serve the text.** Recommended standing rule: never record a
`licence-walled` status from a `get_copyright_status` result whose `checked_sources` omits `pmc`
without first attempting `get_full_text_article`. Two lines of tool call would have prevented an
unread leg from being counted as unreadable.

**Record the reading.**
`FT-098` moves from *unread* to **read, on the MCP/PMC text surface, with a declared extraction
defect**. Artefact and hash as given at the head of this file.

**Record what the paper bears on.**
- It is **blood transcriptomic case-control**, self-rated **Class III** for *"the case control
  design and the risk of spectrum bias"*.
- Its result is a **six-gene composite score**, OR ≈ 1.18–1.24, with entorhinal thickness
  replicating and **hippocampal volume failing to replicate** in AddNeuroMed.
- It performs **no genetic association test of its own**; genetic input is external GWAS summary
  statistics plus a public CN blood eQTL database.
- It is **gene-level throughout** and has **no isoform resolution**, so it cannot speak to
  `TRAPPC6AΔ`.

**Record the node-independence finding.**
`FT-098` is **not independent support** for a `TRAPPC6A` neurocognitive role. Two reasons, both
quotable: membership in a polarised additive six-gene score is not per-gene evidence, and the
paper's only neurocognitive statement about the gene is a **citation** — *"genetic variation ofis
reported to be associated with nonverbal reasoning"* — introduced by *"it is not clear how it
affects the pathogenesis of AD."* The named phenotype, **nonverbal reasoning**, is leg 3's
phenotype. On this surface the destroyed reference number prevents confirming the citation target,
so the following is recorded as **probable and unverified, pending a figure- and
reference-preserving surface**: legs 2 and 3 are **not independent of each other**; leg 2 cites
leg 3's phenotype for the only claim that made it look like support.

**Do not reopen the retraction.**
The retraction of the `TRAPPC6A` claim stands on legs 1 and 3, which fell on their own evidence.
This reading was undertaken to discharge an unread-debt, and it discharges it. Nothing here rescues
the claim and nothing here is needed to break it further. **The correct outcome is a closed debt,
not a revived node.**

**Residual debt, small and explicit.**
Supplementary tables e-1 to e-7 and figures e-1 to e-3 carry every per-gene statistic and every
imaging effect size. They are **not on this surface**. If the per-gene numbers for `TRAPPC6A` are
ever wanted — and §5 argues they would not change the verdict, since the score is what is
load-bearing — they require the publisher HTML or PDF, not this route.

---

## Declaration

**Author:** Scientist A · **Date:** 2026-09-21 · **Mode:** READ-ONLY.

**No canonical file modified.** No registry, queue, ledger, current file or working model was read
for write or altered. No git operation was performed. No commit candidate is produced. Two files
were written and nothing else: the verbatim source artefact
`files/fulltext/PMID33134515_PMC_MCPtext.txt` and this analysis.

**Declared limits.**

1. **No figure inspected.** Figures 1 and 2 and supplementary figures e-1 to e-3 are image content
   and are not inspectable on this surface. Per **D-14**, no negative asserted only by a figure is
   adjudicated in this audit. Figure *captions* were read as text and are quoted only as captions.
2. **No supplementary table read.** Tables e-1 to e-7 are absent. Every per-gene statistic and every
   imaging effect size in this paper lives there. Main-text tables 1–3 are present as captions only,
   without their bodies.
3. **Extraction defect, and exactly which token classes it destroyed.** The MCP/PMC renderer drops
   all *italicised* runs. Destroyed: (a) **every gene symbol**, in body and in the metadata abstract
   alike — `TRAPPC6A` 0, `CD33` 0, `APOE` 0 occurrences, and the collision *"includingand"* proves
   the deletion is silent and unmarked; (b) **the italic *P*** and **every numeric exponent** —
   *"< 5 × 10"*, *"< 1 × 10"*, *"< 8.4 × 10"*; (c) **italic statistical symbols** — the LD *r²*
   reduced to *"(> 0.8)"* and *"(> 0.1)"*, the imputation *R²* to *"anvalue of 0.30"*, and the
   *z*-score to *"(-score)"*; (d) **superscript reference numbers**, which run citations into the
   following sentence (*"molecular mechanisms.Transcriptional risk scores"*) and make the target of
   the `nonverbal reasoning` citation unrecoverable; (e) **trial registry identifiers**, leaving
   *"identifiers are,, and."*
   **Not destroyed:** Roman-type method words, protein names, rsIDs, cohort names, ORs and their
   confidence intervals. Zeros counted in the Roman class are therefore informative and are reported
   as such (`blind` 0, `permutation` 0, `isoform` 0, `splice` 0, `exon` 0); zeros counted in the
   italic gene-symbol class are **not** informative and **no negative is drawn from any of them.**
   **No gene identity was reconstructed from position, ordering or plausibility anywhere in this
   audit.** Where the paper's structure suggests an assignment (§2, §5), the inference is labelled
   as structural and left unresolved.
4. **Licence.** `Copyright © 2020 The Author(s). Published by Wolters Kluwer Health, Inc. on behalf
   of the American Academy of Neurology.` `license.type: null`, `license.url: null`,
   `is_open_access: false` — that flag from `checked_sources: ["pubmed"]` only, with PMC not
   consulted. The full body was served by PMC on request. **No open-access licence is asserted**;
   the finding is narrower and sufficient: **the text is retrievable on the PMC route, so the leg
   was never unreadable.**
5. **Attribution.** Article metadata and full text retrieved from **PubMed / PubMed Central**.
   DOI: https://doi.org/10.1212/NXG.0000000000000517
