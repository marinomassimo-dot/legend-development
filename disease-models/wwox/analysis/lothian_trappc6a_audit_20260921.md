# FT-099 — Lothian Birth Cohorts `TRAPPC6A` audit

**Paper.** Hamilton G, Harris SE, Davies G, Liewald DC, Tenesa A, Starr JM, Porteous D, Deary IJ.
*Alzheimer's Disease Genes Are Associated with Measures of Cognitive Ageing in the Lothian Birth
Cohorts of 1921 and 1936.* Int J Alzheimers Dis 2011;2011:505984.
PMID 21766012 · PMCID PMC3132531 · DOI 10.4061/2011/505984 · CC BY (open access).

**Source of text.** Retrieved from PubMed Central via the PubMed MCP
(`get_full_text_article`, `pmc_ids: ["PMC3132531"]`) and PubMed metadata
(`get_article_metadata`, `pmids: ["21766012"]`). Per PubMed attribution requirement: information
below is from PubMed / PMC; DOI link [10.4061/2011/505984](https://doi.org/10.4061/2011/505984).

**Read by.** Scientist B. **Date.** 2026-09-21. **Status.** READ-ONLY audit. No canonical file
touched, no commit candidate produced.

---

## 0 · Header — declared read depth and surface integrity

| Item | State |
|---|---|
| **Read depth** | **FULL BODY, TABLES ABSENT.** Introduction, Materials and Methods (2.1–2.4.4), Results (3.1–3.4), Discussion (4.1–4.3) and Conclusions (5) all returned as continuous prose and were read end to end. |
| **Gene symbols survived?** | **NO — partially stripped.** The extractor removed italicised gene symbols from running prose. Section *headings* survived (`4.2. APP`, `4.3. BIN1`); one non-italic instance of `APP` survived in Methods. **`TRAPPC6A` occurs ZERO times in the retrieved body.** It occurs once, intact, in the PubMed metadata abstract — which is a different retrieval path and preserved it. |
| **Statistical symbols survived?** | **NO.** Italic math symbols (`P`, `β`, `n`, `r²`, `D′` in some positions, frequency `f`) are also stripped, leaving fragments such as `(= −0.21)` and `only where≤ .00056`. Numeric values survive; their labels often do not. |
| **Tables obtainable?** | **NO. This is a finding, not an inconvenience.** Every in-text table/figure citation returned as an empty `()`. Tables 1–3 and Supplementary Tables S1–S11 (including `Table S1`, the SNP list, and `Tables S4–S6`, the haplotype windows) were **not** retrievable. **No numeric p-value for the `TRAPPC6A` haplotype exists anywhere in the obtainable text.** |
| **Figures/panels** | Not obtainable. None inspected. None claimed. |

### Evidence of the stripping, verbatim

> "A total of 158 SNPs were selected;from APP, 9 from, 6 from17 from, 6 from9 from29 from, and
> 16 from theregion, which included three SNPs from the 5′ end ofgene (Table S1)."

> "Two 3-SNP windows, comprising four adjacent SNPs from, reached our correctedvalue level
> (≤ .00056) with general cognitive ability at age 11 (MHT adjusted) in the overall LBC1936
> sample ()."

Both sentences are missing gene symbols at the elided positions, and the second is missing both
the `P` label and its table reference. **Per the standing rule: where a symbol is stripped, this
audit does not infer which gene a sentence names, except where the inference is stated explicitly
as an inference and its basis is given (see § 1.1).**

### 1.1 · How `TRAPPC6A` was identified in a body that never names it

The gene attribution rests on three mutually consistent anchors, not on guesswork:

1. **The abstract, retrieved intact, names exactly one haplotype gene.** Verbatim:
   > "One haplotype from TRAPPC6A was associated with nonverbal reasoning in both cohorts and
   > combined data sets. This haplotype explains a small proportion of the phenotypic
   > variability (1.8%)."
2. **Methods state that the chromosome-19 SNP set included exactly three SNPs at the 5′ end of
   one gene**, verbatim: "16 from theregion, which included **three SNPs from the 5′ end ofgene**".
3. **Discussion § 4.1 describes a three-SNP window at that same location with the same 1.8%**,
   verbatim: "This SNP window consisted of the SNPs (rs7247764, rs28555639, rs12460041) located at
   the 5′ end of thegene… explained 1.8% of the variation in the LBC1936."

The 1.8% figure, the "nonverbal reasoning" phenotype and the "both cohorts and combined" pattern
are unique in the paper and appear in both the intact abstract and § 4.1. **The identification is
therefore secure.** The operative identifiers going forward are the rsIDs
**rs7247764, rs28555639, rs12460041**, which the body does give verbatim.

---

## 2 · Question 1 — the actual `TRAPPC6A` result

**Results § 3.3, verbatim (gene symbol stripped, table reference empty):**

> "One 3-SNP window from thelocus reached significance with matrix reasoning in the4 negative
> subgroup (). Though not significant postpermutation analysis in the LBC1936, this finding was
> replicated in the LBC1921 and in post permutation analysis of the combined cohort."

**Discussion § 4.1, verbatim — the fullest statement of the result in the paper:**

> "One 3-SNP window located at the 5′ end of theregion was significantly associated with
> non-verbal reasoning in individuals lacking an4 gene in the LBC1936 data set. This SNP window
> consisted of the SNPs (rs7247764, rs28555639, rs12460041) located at the 5′ end of thegene.
> They span a genomic region of 1442 bp and are in complete LD (′ = 1). The genotype of this
> associated haplotype was TTT, and it was the most common haplotype (= 0.70). This haplotype was
> associated with a small decrease in Wechsler matrix reasoning scores (= −0.21) and explained
> 1.8% of the variation in the LBC1936. This was replicated in the LBC1921 cohort (= −0.18),
> where it explained 1.3% of the variation in Raven's Standard Progressive Matrices scores.
> Permutation analysis of the combined data set confirmed this result."

**Assembled:**

| Element | Value | Source |
|---|---|---|
| SNPs | rs7247764, rs28555639, rs12460041 (5′ end of the gene; 1442 bp; complete LD, D′ = 1) | § 4.1 verbatim |
| Haplotype | **TTT** — the *most common* haplotype, frequency 0.70 | § 4.1 verbatim |
| Cohort (discovery) | LBC1936, n = 998, **APOE ε4-NEGATIVE subgroup only** | § 3.3, § 4.1 |
| Phenotype (discovery) | WAIS-III **matrix reasoning** (nonverbal reasoning), age ~70 | § 2.2, § 4.1 |
| Effect (discovery) | β = **−0.21** (label stripped; a *decrease* in score); **1.8%** of variance | § 4.1 |
| Cohort (replication) | LBC1921, n = 505 | § 4.1 |
| Phenotype (replication) | **Raven's Standard Progressive Matrices** — a *different* instrument | § 2.2, § 4.1 |
| Effect (replication) | β = **−0.18**; **1.3%** of variance | § 4.1 |
| **p-value, any cohort** | **NOT PRESENT IN OBTAINABLE TEXT.** Lives only in the empty `()` table references. | — |
| Corrected or uncorrected? | **Mixed and adverse — see § 3.** | — |

**Second-hand record checked:** the claim of "both Lothian Birth Cohorts (1921 n≈505; 1936 n≈998)",
"single-SNP analyses did not survive multiple-testing correction" and "~1.8% of variance" are all
**accurate against the body**. The 1.8% is specifically the LBC1936 discovery figure; LBC1921 is
1.3%. No fabricated statistic found. The second-hand record's *omissions*, however, are the whole
story — see § 3.

**⚠️ Not stated in the obtainable text:** whether the LBC1921 replication was also restricted to
the APOE ε4-negative stratum. § 3.3 and § 4.1 state the ε4-negative restriction for LBC1936 only.
The natural reading is that the replication mirrored the stratum, but **the paper does not say so
in any sentence retrievable here**, and this audit will not assume it.

---

## 3 · 🔴 Question 2 — multiple testing, and whether the haplotype survives it

### 3.1 · The correction the authors pre-specified

**Methods § 2.4.1, verbatim:**

> "To determine the correct level of significance for regression and haplotype analyses of the
> LBC1936 cohort, a spectral decomposition program, SNPSpD, was used []. SNPSpD calculates an
> approximate estimate of the effective number of independent SNPs using a previously described
> method []. A Bonferroni calculation using this number of SNPs was used to determine the
> appropriate level of significance for regression and haplotype analysis."

**Methods § 2.4.3, verbatim — the haplotype analysis had a second, mandatory stage:**

> "The second approach was haplotype analysis. Each gene was examined for association with
> cognitive phenotypes using a sliding window of three SNPs, shifting one SNP at a time. Two
> stratified data sets, with or without theallele, were analysed similarly. … **SNP regions
> meeting the significance threshold were analysed using max(T), a label swapping-based
> permutation method.**"

**Results § 3.1, verbatim — the thresholds, as set by the authors:**

> "Spectral decomposition analysis calculated that the approximate estimate of the effective
> number of independent SNPs was 89.24. Therefore, in our regression and haplotype analyses, only
> where≤ .00056 (= 0.05/89.24), were results considered significant associations. … **max(T)
> permutation analysis was carried out on significant haplotype results, and a significance
> threshold of≤ .05 was applied to the results. Results with≤ .05 were considered significant in
> our replication cohort.**"

So the authors' own two-stage gate for a haplotype in the discovery cohort was:
**(i)** p ≤ 0.00056 (Bonferroni over 89.24 effective SNPs), **then (ii)** max(T) permutation at
p ≤ 0.05. Replication in LBC1921 was judged at an **uncorrected nominal p ≤ 0.05**.

### 3.2 · Does the `TRAPPC6A` haplotype survive it? — **In the discovery cohort, NO.**

**Results § 3.3, verbatim, the single most important sentence in this paper for LEGEND:**

> "One 3-SNP window from thelocus reached significance with matrix reasoning in the4 negative
> subgroup (). **Though not significant postpermutation analysis in the LBC1936**, this finding
> was replicated in the LBC1921 and in post permutation analysis of the combined cohort."

**The `TRAPPC6A` haplotype passed stage (i) and FAILED stage (ii) in the discovery cohort.** It
cleared the SNPSpD-Bonferroni threshold and then did **not** survive the authors' own max(T)
permutation in LBC1936. This is the correction the haplotype analysis received, and by the
paper's own pre-specified criterion the discovery result did not hold.

**The only permutation the haplotype passes is on the combined dataset** — § 4.1: "Permutation
analysis of the combined data set confirmed this result." **The combined dataset contains the
discovery cohort.** A permutation test on discovery + replication pooled is not an independent
correction of the discovery finding; it is the discovery finding re-tested with the replication
sample folded in. It cannot rescue a discovery result that failed permutation in its own cohort.

**Answering the brief's specific question — "haplotype tests are not automatically protected":**
correct, and here they were not. The single-SNP results and the haplotype results were held to
**the same Bonferroni threshold** (§ 3.1: "in our regression **and haplotype** analyses, only
where ≤ .00056"), so the haplotype did not receive a weaker family. But the haplotype family
carried an **additional** stage the single-SNP family did not — max(T) permutation — and the
`TRAPPC6A` haplotype failed it in discovery.

### 3.3 · What the correction did NOT cover — the uncounted multiplicity

The SNPSpD/Bonferroni denominator was **89.24 effective SNPs**. That single number was asked to
cover a search surface that includes, by the paper's own Methods:

- **Multiple cognitive phenotypes.** § 2.2 names, for LBC1936: MHT at age 11, MHT at age 70,
  verbal fluency, matrix reasoning, logical memory (immediate and delayed). That is 5–6 outcomes.
- **Three sample strata.** § 2.4.3, verbatim: "Two stratified data sets, with or without
  theallele, were analysed similarly" — i.e. the full sample **plus** ε4-positive **plus**
  ε4-negative, each analysed across every phenotype.
- **A sliding window across every gene.** § 2.4.3, verbatim: "a sliding window of three SNPs,
  **shifting one SNP at a time**" — ~150 overlapping windows across 158 SNPs.
- **Two covariate models** in the regression arm (§ 2.4.3: APOE ε4 status; age-11 MHT).

**None of phenotype count, stratum count or window count enters the 89.24 denominator.** The
`TRAPPC6A` hit is a *stratum-specific* result (ε4-negative) on *one* of several phenotypes.
Correcting for effective SNP number alone leaves the phenotype × stratum multiplicity entirely
unpriced. The max(T) permutation was the authors' safeguard against exactly this — and it is the
stage the haplotype failed.

### 3.4 · The haplotype was never a hypothesis about `TRAPPC6A`

**Methods § 2.3, verbatim:** "… and 16 from theregion, which included three SNPs from the 5′ end
ofgene (Table S1)."

The three SNPs were **incidental coverage** picked up while tiling the chromosome-19 / APOE
region, not a candidate-gene test of `TRAPPC6A`. The gene is absent from the paper's list of
target genes in the Introduction and has no section heading of its own — § 4.1 is titled
"**Chromosome 19 Locus**", not by the gene's name. **This is not a study that set out to test
`TRAPPC6A` and found it associated. It is a study of AD candidate genes in which three
along-for-the-ride SNPs produced a subgroup hit.**

The authors themselves cannot connect it to the AD locus that motivated the region, § 4.1
verbatim:

> "The SNP associated with LOAD in the recent GWAS study [], rs597668, is located in an
> intergenic region betweenandThis SNP was included in our study although we did not observe an
> association with any cognitive phenotype. Thehaplotype is located 31573 bp from the GWAS SNP,
> and analysis of the LD in this region shows that SNPs from the haplotype were not in the same
> LD block as the GWAS SNP (′ = 0.22), **so it is unclear whether our results are detecting the
> same effect. Replication of thehaplotype is required in a larger cohort.**"

---

## 4 · Question 3 — replication or discovery-plus-pooling?

**Both, and the design is genuinely two-stage — which is the one real strength here.**

**Methods § 2.1, verbatim:**
> "The LBC1936 was used as the discovery cohort. Significant results meeting the chosen
> statistical criteria were carried forward and investigated using the LBC1921."

**Results § 3.1, verbatim:**
> "The LBC1936 cohort was used as a discovery sample and the LBC1921 cohort as a replication
> cohort. Different significance thresholds were applied to each cohort."

So LBC1921 **was** run as a designated replication cohort with its own analysis, not merely
pooled. That is a real, pre-specified replication design and it is to the authors' credit.

**But four qualifications, each from the text:**

1. **The replication threshold was uncorrected.** § 3.1 verbatim: "Results with≤ .05 were
   considered significant in our replication cohort." Nominal p ≤ 0.05, no correction of any kind.
2. **The LBC1921 p-value is not obtainable.** It appears only in the stripped tables. This audit
   knows the *direction* (β = −0.18) and the *variance* (1.3%) and nothing else.
3. **The instrument differed.** § 2.2: LBC1936 was tested on "matrix reasoning (a subtest from the
   Wechsler Adult Intelligence Scale-III…)"; LBC1921 on "Raven's Standard Progressive Matrices".
   Both index nonverbal reasoning; they are not the same test. The authors flag this class of
   problem themselves in § 5: "not all cognitive tests used were all identical, although they were
   similar."
4. **The pooled analysis is the only one that passed permutation**, and it is not independent
   (§ 3.2 above). "Associated in both cohorts" and "confirmed by permutation" are, in this paper,
   two different results resting on two different samples — the second of which includes the first.

**The cohorts are independent samples but not independent pipelines.** Both are Edinburgh-area
Scottish birth cohorts from the Scottish Mental Surveys, run by the same investigators, genotyped
on the same chip at the same facility (§ 2.3: "All samples were genotyped at the WTCRF Genetics
Core with the Illumina Human 610-Quadv1 chip"). Different people — same lab, same region, same
platform. This is within-group replication, not cross-group replication.

---

## 5 · Question 4 — which cognitive domain, and the distance to WWOX-DEE

**The domain is nonverbal reasoning in cognitively healthy, non-demented older adults.**

**§ 2.2, verbatim:** "matrix reasoning (a subtest from the Wechsler Adult Intelligence Scale-III
used to assess nonverbal reasoning)"; "Raven's Standard Progressive Matrices (a test of non-verbal
reasoning)".

**§ 2.1, verbatim — the sample is explicitly dementia-free:**
> "Individuals were excluded from this study if there was a personal history of dementia, if they
> had an MMSE score of less than 24, or if they did not have GWAS data."

Mean ages at testing: **69.58 ± 0.83 years** (LBC1936) and **79.11 ± 0.57 years** (LBC1921).

**The distance, stated plainly.** This paper measures a 0.21-SD shift in a matrix-reasoning score
among APOE ε4-negative Scots in their eighth and ninth decades, within the normal range of
cognitive ageing. WWOX-DEE is a neonatal-onset developmental and epileptic encephalopathy with
seizure onset in the first weeks of life, profound global developmental arrest and early
mortality. **There is no seizure, epilepsy or EEG phenotype anywhere in this paper** — the word
"epilepsy" does not appear in the retrieved body at all. There is no developmental phenotype, no
paediatric sample, no loss-of-function allele, and no rare variant: the associated haplotype is
the **most common** one (frequency 0.70). A common-variant, small-effect modifier of normal
late-life reasoning and a monogenic neonatal encephalopathy are different classes of genetic
claim, and a finding in the first does not transfer to the second. The most this paper could ever
have contributed is "this locus is not inert with respect to brain function in humans" — and § 3
establishes that it does not deliver even that at its own significance standard.

---

## 6 · Question 5 — gene or isoform?

**Isoform: absent. As expected, completely.**

- **`TRAPPC6AΔ` — zero occurrences** in the retrieved body. The body contains no Δ-isoform, no
  truncated transcript, no variant-transcript nomenclature of any kind for this gene.
- **"splice" / "splicing" — zero occurrences** in the retrieved body.
- **"transcript" — zero occurrences** in the retrieved body.
- **"isoform" — one occurrence, and it is about a different gene.** § 4.3, verbatim, under the
  heading `4.3. BIN1`: "It encodes several isoforms that are expressed in the central nervous
  system and may be involved in synaptic vesicle endocytosis." This refers to `BIN1`, not to the
  chromosome-19 gene.

The paper's unit of analysis is a **3-SNP genomic window spanning 1442 bp at the 5′ end of the
gene**. It is a positional, genotype-level test. It makes no statement whatever about which
transcript is produced, about alternative splicing, or about any Δ-isoform. **Corroborating a
locus is not corroborating an isoform, and this paper does not even corroborate the locus.**

---

## 7 · Question 6 — the authors' own framing

**Abstract (retrieved intact via metadata), final sentence, verbatim:**
> "These findings warrant further investigation as biological modifiers of cognitive ageing."

**§ 4.1, verbatim:**
> "…so it is unclear whether our results are detecting the same effect. Replication of
> thehaplotype is required in a larger cohort."

**§ 5 Conclusions, verbatim — the full limitations passage:**
> "This study indicates that gene specific variation and gene-gene interactions **may** influence
> cognition. Our strongest results implicate a role for a haplotype at thelocus in non-verbal
> reasoning in individuals lacking the4 allele. A less clear role forandin influencing verbal
> declarative memory in individuals carrying at least one4 allele is suggested.
>
> **The effect sizes we have observed in this study are small. Indeed, despite the comparability
> of genomic LD structure, the majority of these associations were not replicated in the LBC1921
> cohort.** However, it should be noted that the replication cohort (= 505) is smaller than the
> discovery cohort (= 998). **Particularly, our main results were observed in the
> smallerstratified groups.** In addition, the individuals in each cohort were retested at
> different ages; the LBC1921 were re-tested at age 79, while the LBC1936 were re-tested at age
> 70, and not all cognitive tests used were all identical, although they were similar.
>
> The results presented here were obtained with SNPs not previously associated with sporadic AD,
> suggesting that either allelic heterogeneity or a functional SNP is not yet identified ().
> Nonetheless, the results presented here identify interactions between recently identified and
> previously known AD genes and provide an interesting insight into potential molecular pathways
> underlying cognitive traits. **They require further investigation in larger identically
> phenotyped cohorts.**"

**Read in context, "warrant further investigation" is the weakest available positive verb**, and
the authors surround it with: small effect sizes, majority non-replication, results confined to
small stratified subgroups, non-identical instruments, non-identical testing ages, no LD with the
motivating GWAS signal, and an explicit call for replication in a larger cohort. **Nowhere do the
authors claim to have established a role for this gene.** § 5 says "may influence" and
"is suggested".

**No abstract-versus-results inversion was found in this paper.** The abstract is unusually honest:
it states plainly that "Single SNP analyses did not reveal any statistical association after
correction for multiple testing" and calls 1.8% "a small proportion of the phenotypic
variability". The abstract's one material omission is that it does not mention the failed
permutation in the discovery cohort — it reports "associated in both cohorts and combined data
sets" without noting that the discovery association did not survive max(T) in LBC1936. That is an
omission, not an inversion, and it is the omission that the second-hand record inherited.

---

## 8 · VERDICT

> **Proposition under test:** *"`TRAPPC6A` has independent human-genetic support for a
> neurocognitive role."*

# `WEAK — survives nominally but not after correction`

**Grounds, in order of weight:**

1. **The discovery result failed the authors' own pre-specified correction.** Verbatim § 3.3:
   "Though not significant postpermutation analysis in the LBC1936". The haplotype cleared
   Bonferroni-over-89.24-effective-SNPs and then failed max(T) permutation in the discovery
   cohort. By the paper's own two-stage criterion, LBC1936 is a negative result.
2. **The replication was judged at an uncorrected p ≤ 0.05**, in a smaller cohort (n = 505),
   using a different nonverbal-reasoning instrument, and its p-value is not obtainable on this
   surface.
3. **The only permutation the haplotype passes is on the pooled sample containing the discovery
   cohort**, which cannot independently correct the discovery finding.
4. **The result is confined to a stratified subgroup** (APOE ε4-negative) on one of several
   phenotypes, and stratum × phenotype multiplicity was never priced into the correction.
5. **`TRAPPC6A` was incidental coverage of the APOE region, not a tested candidate**, and its
   haplotype is not in LD with the GWAS SNP that motivated the region (D′ = 0.22), so the authors
   cannot say it reflects the same signal.
6. **The effect is a 0.21-SD shift on the most common haplotype (f = 0.70) in healthy
   septuagenarians and octogenarians** — a domain remote from neonatal epileptic encephalopathy.

The verdict is **not** `NOT SUPPORTED`, because the paper's two-stage discovery/replication design
was genuine, the direction of effect was consistent across cohorts (β = −0.21 → −0.18) and the
variance explained was of comparable magnitude (1.8% → 1.3%). Something non-random may be present.
But at the paper's own evidentiary bar it did not clear, and the authors do not claim it did.

The verdict is **not** `CANNOT DETERMINE ON THIS SURFACE`, because the decisive sentence — the
permutation failure in the discovery cohort — is present verbatim in the retrievable Results. The
missing p-values would sharpen the picture; they would not change it, since the pass/fail outcome
of each correction stage is stated in prose.

**Unobtainable, and what it would have added:** the exact p-values for the haplotype in LBC1936,
LBC1921 and the combined sample (Tables 1–3, Supplementary S4–S6). Whether LBC1921's replication
was also ε4-stratified. The full 158-SNP list (Table S1). None of these could overturn the
permutation failure; the first would only tell us how close the call was.

---

## 9 · Closing — the state of the node-independence assessment

**The `TRAPPC6A` node-independence assessment does not survive this reading, and should be
recorded as collapsed.**

The audit recorded that `TRAPPC6AΔ` — the splice isoform on which the Chang/NCKU mechanistic
cascade begins, and which no group outside that lab has ever reported — was single-lab, but that
the *gene* `TRAPPC6A` carried independent human-genetic support from three cohorts. Taking those
three legs in turn: **PMID 41390778** (UCLA, 416,212 records + All of Us) was read and its epilepsy
arm is null on replication (OR 1.01, 95% CI 0.96–1.06, p = 0.80, variance < 0.01%, with the
authors conceding "minimal evidence supporting epilepsy-specific pathways"). **PMID 33134515**
(ADNI + AddNeuroMed) is licence-walled and unobtainable here; it remains an unread citation and
cannot be counted as support in either direction. **PMID 21766012 — this paper — is, on reading, a
result that failed the authors' own permutation correction in its discovery cohort and replicated
only at an uncorrected nominal threshold, in an APOE-stratified subgroup, on an incidentally
genotyped three-SNP window that the authors could not tie to the locus signal that motivated its
inclusion.** It cannot carry an independence claim.

**The gene therefore retains no demonstrated independent human-genetic support for a
neurocognitive role on any surface this laboratory can reach.** One leg is null, one is unread,
and the third — the one the assessment leaned on hardest — says, in its own Results, that it did
not survive correction. What remains is a hedge the authors wrote themselves: "These findings
warrant further investigation."

**And the load-bearing point, which was true before this reading and is unchanged by it: none of
these three papers ever bore on the isoform.** All three are locus-level or genotype-level human
genetics. `TRAPPC6AΔ` appears in none of them — in this paper the strings `TRAPPC6AΔ`, "splice",
"splicing" and "transcript" occur zero times. Even had all three legs held, they would have
corroborated a *locus*, not the splice isoform on which the Chang/NCKU cascade actually depends.
The node-independence assessment was, from the outset, answering a question adjacent to the one
that matters. It now fails on its own terms as well.

---

*Scientist B, 2026-09-21. READ-ONLY. No canonical file modified; no commit candidate created; no
therapeutic inference drawn. Full text and abstract retrieved from PubMed/PMC;
DOI [10.4061/2011/505984](https://doi.org/10.4061/2011/505984).*
