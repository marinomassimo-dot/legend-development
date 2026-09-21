# NODE_WWOX_HUMAN_PRENATAL_AND_INFANT_PHENOTYPE — Wave 1 read (W-1, W-2)

**Date:** 2026-09-21 · **Actor:** SCIENTIST A · **Mode:** READ-AND-REPORT, read-only toward every
canonical file. No BATCH_COMMIT, no commit candidate, no receipt recorded, no registry edited.
**Node:** selected by [[next_node_scout_20260921_orchestrator]] § 3.
**Research question:** *what is measurably different about the human brain, before birth and in
infancy, when WWOX is lost or varied — and does any of it discriminate genotype classes?*

**Sources.** Both papers retrieved from PubMed / PubMed Central via
`mcp__PubMed__get_full_text_article` and `mcp__PubMed__get_article_metadata`.
W-1 — PMID 28763065 · PMC5611727 · [DOI](https://doi.org/10.1038/tp.2017.159).
W-2 — PMID 41378749 · PMC12697008 · [DOI](https://doi.org/10.1002/bdr2.70007).

> **Not medical advice.** Nothing below supports or modifies any therapeutic decision.

---

## 1 · VERDICT

> ### **PARTIAL — and the partial is almost entirely negative.**
>
> **Neither paper is a mechanism result and neither touches a WOREE genotype class:** W-1's WWOX
> signal **did not cross the paper's own genome-wide threshold** and its allele, effect size and
> direction are not recoverable from the retrievable text, while W-2's WWOX signal is **nominal
> against a *suggestive* threshold the authors set at 1E‐05 — no genome-wide threshold was ever
> applied — in 89 cases versus 97 controls with no external replication.**
>
> **The single fact that decides it:** W-2's abstract says the WWOX variant lies *"within the
> coding region of WWOX"*; **its own Results place the three chromosome-16 variants "within the
> 8th intron"**, and the abstract's rsID (`rs7184417`) **does not occur anywhere in the paper's
> body**, which names `rs28688166` carrying the identical OR and p. The claim that motivated this
> paper's selection is refuted by the paper itself.

**Secondary verdict, and it may be worth more than the papers:** the brief's premise that neither
paper is held by LEGEND is **wrong**. See § 7. Both are present in the repository, and the
substantive conclusion for each had already been reached.

---

## 2 · W-1 · PMID 28763065 — infant brain-volume GWAS

Xia K, Zhang J, Ahn M, Jha S, Crowley JJ, Szatkiewicz J, Li T, Zou F, Zhu H, Hibar D, Thompson P,
[consortium author], Sullivan PF, Styner M, Gilmore JH, Knickmeyer RC.
*Transl Psychiatry* 2017;7(8):e1188. [DOI](https://doi.org/10.1038/tp.2017.159)

*(Byline copied in the same act from the `get_article_metadata` return, per the
AUTONOMOUS_SESSION_STATE rule that an identifier or byline enters a record only by copy from a
verified source. One author entry in the returned record is an empty object — rendered above as
`[consortium author]` rather than guessed.)*

### 2.1 Retrieval

| | |
|---|---|
| Body returned | **non-empty**; transcribed verbatim to a working file measuring **23,652 characters** |
| Coverage | Introduction → Materials and methods → Results → Discussion, complete to the final sentence |
| **Not present in the returned body** | **every table and every figure**, including Table 1, which is where the per-SNP allele and effect size live; figure *legends* are also absent (unlike W-2, which returned one) |
| Instrument damage | **all italicised gene symbols elided** (`WWOX` occurs **0** times, `IGFBP7` **0** times in the body); **all superscript exponents elided**; **all citation numbers elided** |

🔴 **`WWOX` = 0 and `IGFBP7` = 0 in the body of a paper whose two headline hits are in those two
genes. This is an instrument reading, not a biological negative** (`D-15`). The symbols **survive
intact in the PubMed metadata abstract**, which is how the SNP→gene mapping below is established.

### 2.2 Design

| Item | Value |
|---|---|
| Design | Genome-wide association study, **cross-sectional** (one MRI per infant; no longitudinal analysis is reported, and the Discussion names longitudinal change as something *future* work should address) |
| n | **561 infants** (300 male, 261 female), 0–24 weeks of age; scans "around 5 weeks of age" |
| Family structure | 295 singletons/unpaired twins, 17 sibling pairs, 232 twins (61 same-sex DZ, 37 MZ, 18 opposite-sex DZ pairs); handled by ACE-based linear mixed effects models |
| **Age at scan** | **neonatal / early infancy — NOT 1 year, NOT 2 years.** This is the node's whole reason for existing and it holds up |
| Ancestry | **63% European ancestry; remainder primarily African ancestry.** Sensitivity subsets: European n=356, non-European n=205 |
| Endpoint | **Four GLOBAL brain tissue volumes only: ICV, GM, WM, CSF.** No regional volume, no cortical thickness, no surface area, no DTI, no myelin-specific measure. WM = global white-matter volume from atlas-based T1/T2 tissue segmentation |
| SNPs tested | **8,762,422**, imputed (MACH-Admix, 1000 Genomes phase1_release_v3), retained at average r²>0.8 and MAF ≥0.01 |
| Covariates (ICV, WM) | 3 genotypic PCs, scanner platform, birth weight, gestational age at birth, sex, age at MRI; **ICV was itself a covariate for GM, WM and CSF** |
| Power | "sufficient to discover a genetic effect on the order of ~8% with 80% power" |

### 2.3 The threshold, and whether WWOX crossed it — **NO**

The Methods construct the threshold explicitly: *p*-values below **1.25 × 10^x** were genome-wide
significant, being "the conventional GWAS threshold of 5 × 10^y ... divided by four" (Bonferroni
across the four MRI phenotypes); the suggestive level was likewise **1.25 × 10^z** = conventional
suggestive 5 × 10^w / 4.

🔴 **Every exponent in that passage is elided by the extractor, on both the full-text and the
metadata surface.** The mantissas survive. The exponents are recovered here **by arithmetic, not by
reading**: the conventional GWAS and suggestive thresholds are 5 × 10⁻⁸ and 5 × 10⁻⁷, and
5×10⁻⁸/4 = 1.25×10⁻⁸ and 5×10⁻⁷/4 = 1.25×10⁻⁷ reproduce the printed mantissa `1.25` exactly.
**Labelled INFERENCE. The arithmetic is the paper's own; the exponent is not quoted.**

| Quantity | Value as retrievable |
|---|---|
| SNP | **rs10514437**, intronic in **WWOX** (gene identity from the metadata abstract) |
| Phenotype | **global white matter volume (WM)** |
| *p* | **mantissa `1.56`; exponent ELIDED by the extractor on both surfaces** |
| Genome-wide threshold | mantissa `1.25`; exponent elided → **1.25 × 10⁻⁸ by arithmetic (INFERENCE)** |
| **Did it cross the threshold?** | **NO.** Results: *"fell just short of genome-wide significance for WM"* |
| Abstract's word | *"neared genome-wide significance"* |
| **Abstract vs Results** | **CONSISTENT.** Both hedge. `neared` ≈ `fell just short`. **No inversion here — the hedge survives the read intact and must survive every downstream use.** |
| Effect size, direction, allele | 🔴 **NOT RECOVERABLE.** They live in Table 1, which the extractor did not return. The body gives only a *range across all top SNPs*: "absolute percent differences of 0.85–9.54% in volume per risk allele, explaining 0.27–6.52% of the phenotypic variance". **This is a range, not the WWOX value. Do not attribute either endpoint of it to rs10514437.** |
| Permutation | empirical *p* mantissa `8`, **exponent elided and not recoverable by arithmetic** (no stated construction constrains it). Authors: "Low empirical-values suggest these findings are reliable and robust" |

🔴 **The most likely reconstruction of the WWOX *p* is 1.56 × 10⁻⁸** — it is the only exponent that
makes "fell just short" true against a 1.25 × 10⁻⁸ threshold (1.56e-8 is 1.25× above it, whereas
1.56e-7 would be 12× above it and would also fail the *suggestive* level). **This is INFERENCE from
the authors' own verb, not a quoted number, and it is a standing `D-15` exposure: the exact
exponent requires the publisher PDF or the JATS, neither of which is reachable in this checkout.**
The verdict does not depend on it — *below threshold* is stated in words either way.

### 2.4 Was WWOX pre-specified? — **NO**

**Hypothesis-free.** 8,762,422 SNPs × 4 phenotypes, no candidate-gene list, no prior WWOX
hypothesis anywhere in the Introduction or Methods. WWOX surfaced **post hoc** as one of the
top-ranked loci and is discussed afterwards. Multiple-testing correction was **Bonferroni across
the four phenotypes only** (÷4 on the conventional 5×10⁻⁸); the 8.76M SNPs are handled by the
conventional threshold itself. No FDR, no permutation-based family-wise control (permutation was
run only on the two top SNPs, after the fact, as a validity check).

### 2.5 Replication — **NONE**

There is **no replication cohort**. The ENIGMA2 (adult) and PNC (adolescent) comparisons are
explicitly disclaimed: *"These comparisons do not represent a conventional replication sample."*
They test shared genetic determinants across ages, not replication.

The authors close: *"To our knowledge, this is the first study of its kind, consequently
independent replication is critical."*

🔴 **One cross-cohort sentence is unattributable.** Results state *"The SNP tagging[gene] is
nominally significant in ENIGMA2 (=0.048) with the same direction of effect."* **The gene symbol is
elided and the ENIGMA2 phenotype is ICV, not WM** (the Methods state GM and WM data were not
available for ENIGMA2). **Whether this sentence concerns WWOX cannot be determined from this
surface, and it is not claimed either way.** Attribution method: exhausted — the symbol is absent
from the body, and the metadata abstract does not contain this sentence.

### 2.6 An ancestry caveat that cannot be attributed — stated, not resolved

Results: *"Although Fvalues were below 0.05 for our top hits inand, we note that the minor (A)
allele for theSNP is very rare in populations of European ancestry ... We were unable to run
sensitivity analysis in individuals of European ancestry as the minor allele did not occur in this
group."* The Conclusion repeats it: *"This is particularly true for the intronic SNP inwhich has a
low minor allele frequency, was imputed, and was not present in the largest racial/ethnic group in
the study."*

🔴 **Which of the two hits this caveat attaches to cannot be read off this surface** — the gene
symbol is elided in both sentences. Both branches are recorded, and **neither is asserted**:

- **If it is IGFBP7/rs114518130** (the GM hit), the WWOX signal is unaffected by this caveat.
- **If it is WWOX/rs10514437**, then the already-sub-threshold WM signal additionally rests on a
  rare, imputed allele absent from 63% of the cohort — **materially weaker still**.

*Weak external indication only, flagged as such and resting on nothing in the paper:* dbSNP
accession ranges place `rs114518130` in a 1000-Genomes-era build and `rs10514437` in a much older
one, which is **consistent with** the rare allele being the IGFBP7 hit. **This is a numbering
convention, not evidence, and it is not used to support any conclusion below.** The verdict is
written to hold under the *worse* branch.

### 2.7 Does the paper discuss WWOX biology? — **YES, briefly, as plausibility narrative**

*"Mutations inare associated with brain phenotypes including autosomal recessive spinocerebellar
ataxia-12 (SCAR12; MIM #614322), epilepsy, mental retardation and microcephaly. MRI studies are
limited, but hypomyelination, hypoplasia of the corpus callosum and posterior white matter
hyperintensities have been reported. In adult human brains, levels of the protein encoded by(WOX1)
are high in neuronal axons and nerve bundles such as corpus callosum and striatal fascicles,
consistent with our observed association with WM."*

🔴 **Every clause of that passage is cited to prior literature. Not one of them is measured in this
paper.** It is the authors offering post-hoc plausibility for a locus that did not reach their own
threshold. **It is not a WWOX result and must never be cited as one.** Note in particular that the
WOX1 axon/corpus-callosum statement is about **adult human brain** — imported into an infant paper
as analogy.

### 2.8 The headline overlap claim — **SUPPORTED in Results**

The paper's own headline is that infant and adolescent/adult brain-volume genetics **overlap
minimally**. Checked against Results:

- Sign tests, neonate vs adolescent WM: significant at three thresholds, but **"Percent overlap is
  small with 53.8, 51.2 and 50.6% of SNPs showing the same direction of effect versus 50% expected
  by chance."** ICV neonate-vs-adult: 50.40%. Adolescent-vs-adult ICV: 50.80%.
- **"Adult polygenic scores for ICV did not predict neonatal ICV"**, though they did predict
  adolescent ICV.
- **"Previously published genome-wide significant hits for ICVin adults did not predict ICV in
  infants"**.
- Cross-age polygenic scores explained **0.4–1.6%** of variance, against 74–93% within-age.
- Discussion: *"However, percent overlap in sign tests was minimal and the percent of variance
  explained by polygenic scores was small. The overall pattern of results suggests genetic
  determinants of global brain volumes are highly distinct at different ages."*

**YES — the framing is supported by the Results, quantitatively and in several independent
analyses.**

> 🔴 **What this implies, and it is the most transferable thing in W-1.** This paper is direct
> empirical evidence that **a WWOX neuroimaging association measured in adults or adolescents does
> not license a developmental claim, and vice versa.** Effects at one life stage barely transfer to
> another *in this very phenotype class*. Any future LEGEND use of an adult WWOX neuroimaging or
> neurodegeneration association as evidence about the WOREE window must carry this as a named
> counter-premise. **This is a methodological constraint LEGEND can use; it is not a WWOX finding.**

### 2.9 What was NOT tested in W-1

- **No regional white matter, no myelin-specific measure, no DTI, no g-ratio, no cortical thickness
  or surface area.** The endpoint is one global volume. *(Consistent with the standing finding in
  [[wwox_myelin_oligodendrocyte_census_20260921]] that **no g-ratio and no electron microscopy exist
  anywhere in this literature**.)*
- **No WWOX expression, no eQTL, no functional follow-up.** The Discussion notes of its top
  associations generally that **"none are known eQTLs"**. There is **no evidence in this paper that
  rs10514437 alters WWOX at all.**
- **No rare or biallelic WWOX variant.** MAF ≥0.01 was an inclusion filter: rare variants were
  excluded by design.
- **No WWOX-deficient individual.** No participant is reported to carry a WWOX-related disorder.
- **No longitudinal trajectory, no outcome, no seizure or developmental phenotype.**
- CNV burden did not predict any volume; schizophrenia and ASD polygenic scores did not predict any
  volume. **These are the paper's own null results and are unrelated to WWOX.**

---

## 3 · W-2 · PMID 41378749 — folate × genetic risk for neural tube defects, Bangladesh

Mondragon-Estrada E, Wang X, Uhler MD, Farooque A, Liu K, Mukherjee SK, Ekramullah SM, Arman DM,
Islam J, Suchanda HS, Christiani DC, Warf BC, Mazumdar M, Morton SU.
*Birth Defects Res* 2025;117(12):e70007. [DOI](https://doi.org/10.1002/bdr2.70007)

### 3.1 Retrieval

| | |
|---|---|
| Body returned | **non-empty**; transcribed verbatim to a working file measuring **16,868 characters** (narrative body 13,730 + Table 1, Figure 1 legend and back matter 3,138) |
| Coverage | Introduction → Methods 2.1–2.6 → Results 3.1–3.4 → Discussion → Funding/Ethics. **Table 1 returned in full. Figure 1 legend returned.** Figure images not inspectable (`D-14`) |
| Instrument damage | **gene symbols elided** (`WWOX` survives **once**, as a *protein* name in the final Discussion sentence, un-italicised); citation numbers replaced by author-year strings, which here survive |

### 3.2 Design

| Item | Value |
|---|---|
| Design | Case-control GWAS, Bangladesh, enrolment December 2016 – December 2022 |
| Cases | infants <1 year with **myelomeningocele or meningocele** (spina bifida); 73/89 myelomeningocele, 16/89 meningocele; lumbar 64.0%, sacral/lumbosacral 30.3%, thoracic 4.5% |
| Genotyped | 228 infants, Illumina Global Screening Array, **saliva** (112 SB / 116 non-SB) |
| **n after QC, as analysed** | 🔴 **89 cases / 97 controls = 186** — Results §3.1 and Table 1 (`Cases (= 89)`) |
| **n in the abstract** | 🔴 **"91 infants with SB and 97 without"** — **DOES NOT MATCH THE RESULTS** (see §3.5) |
| Array QC | ≤10% missingness → 391,638 variants; MAF ≥1% → 358,034; HWE → **353,151 genotyped variants** |
| Imputation | **TOPMed Imputation Server**, GRCh38/hg38 panel; R²≥0.7 → 11,568,400; MAF≥1% → **7,152,841 analysed** |
| Model | **logistic-Firth hybrid regression** |
| Covariates in all models | maternal age, infant sex, **10 principal components** |
| Interaction terms | **SNP × Folate** and **SNP × Arsenic**, added stepwise across four models |
| Stratification control | λ = 1.08 → 1.22 across models; LDSC intercept 1.03 → 1.05 |
| Exposures | maternal food-frequency-derived annual folate intake (standardised); maternal **toenail** arsenic (µg/g) |

### 3.3 The threshold — **NOTHING REACHED GENOME-WIDE SIGNIFICANCE, AND NONE WAS EVER APPLIED**

Methods 2.5, verbatim: **"We addressed multiple comparisons by only considering loci above the
suggestive threshold= 1E‐05."**

🔴 **That is the paper's entire multiple-testing policy.** The conventional genome-wide threshold
(5 × 10⁻⁸) is **never invoked**: the string `genome-wide significan` occurs **0 times** in the
returned body — and unlike a gene symbol, this phrase is not italicised, so **here the zero count is
informative rather than an instrument artefact**. The paper's own word throughout is **"nominal"**
(9 occurrences).

**Where 2.22E‐06 sits:** it is **below** the authors' suggestive threshold of 1E‐05 (so it qualifies
for reporting), and it is **≈44× above** the conventional genome-wide threshold of 5 × 10⁻⁸ (so it
does not approach significance in the usual sense). **"Nominal" is the authors' word. It must be
carried forward unchanged.**

### 3.4 The WWOX hit — and the abstract's "coding region" is **REFUTED BY RESULTS**

| | **Abstract** | **Results §3.1** |
|---|---|---|
| rsID | **`rs7184417`** | **`rs28688166`** |
| Location | **"within the coding region of WWOX"** | **"within the 8th intron of"** WWOX |
| Effect allele | not given | **EA = C** |
| OR | **6.20** | **6.20** |
| *p* | **2.22E‐06** | **2.22E‐06** |
| Locus | 1 of 2 loci | **three variants on chromosome 16** |

Results, verbatim: *"Three variants on chromosome 16 were within the 8th intron of, including
rs28688166 (Effect allele [EA] = C, odds ratio [OR] = 6.20,= 2.22E‐06; Figure)."*

🔴 **Programmatic check: `rs7184417` occurs ZERO times in the returned body, and `rs28688166` occurs
once.** The two are not italicised tokens, so the zero count here is **not** an extractor artefact —
it is a real absence. Identical OR and identical *p* on two different rsIDs means either the two are
perfect LD proxies with different lead SNPs chosen in abstract and body, or the abstract carries a
transcription error. **Either way the abstract's identifier is uncorroborated by the paper's own
Results.**

🔴 **And the location claim is directly contradicted.** The abstract says *coding region*; the
Results say *8th intron*. **The Results win** (`gold_is_in_the_details`, Results-first), and they
are also the biologically credible reading: WWOX spans ~1.1 Mb of which the coding sequence is a
vanishing fraction. The word `exon` occurs **0** times in the body; `intron` occurs 3 times.

> 🔴 **CONSEQUENCE FOR THIS REPOSITORY.** [[next_node_scout_20260921_orchestrator]] § 4 (row W-2)
> currently states: *"A **coding-region** WWOX variant (`rs7184417`, OR 6.20, p = 2.22E-06)
> **nominally** associated with spina bifida."* **The "coding-region" half of that sentence, and the
> rsID, reproduce the abstract and are contradicted by the paper's Results.** The scout correctly
> flagged it for scrutiny in the same row — the scrutiny has now been done and it failed.
> **Flagged for the Orchestrator; I am read-only and have not edited that file.** The scout's
> *"nominal"* is correct and survives.

Note the abstract makes the same overstatement twice: it also calls the ISOC2 hit *"in the coding
region of ISOC2"*, where Results say only *"one variant overlapped(rs4801638; EA = G, OR = 0.24,=
5.75E‐06; Figure)"*. **This is a systematic abstract-level upgrade of "overlapping/intronic" to
"coding", not a one-off slip.**

### 3.5 A third abstract-vs-Results discrepancy: the sample size

- **Abstract:** *"After quality filtering, genome-wide association was performed on 91 infants with
  SB and 97 without."* (= 188)
- **Results §3.1 and Table 1:** *"A total of 7,152,841 variants from 89 participants with SB and 97
  participants without (Table) were included"*; Table 1 header `Cases (= 89)`.
- **Methods 2.4 reconciles it:** *"Among 226 infants with genotype data, 189 (cases = 91, controls =
  98) had maternal food frequency data available"* ... *"of those 189 infants, **186** also had
  maternal toenail arsenic concentration data ... and were used as the final set for genomic
  analysis."* **186 = 89 + 97.**

🔴 **The abstract's "91" is the folate-only case count carried forward into a sentence describing
the final analysed set, whose true case count is 89.** Arithmetic, not interpretation. **The correct
analysed n is 89/97 = 186.**

**This makes three independent abstract-vs-Results discrepancies in one paper** (rsID, coding-vs-
intronic, n) — a seventh, eighth and ninth instance of the pattern already recorded nine-fold in
[[AUTONOMOUS_SESSION_STATE]]. **In this literature the abstract does not index the results, and W-2
is now the most concentrated single example LEGEND holds.**

### 3.6 Was the WWOX signal robust to the folate and arsenic terms? — **YES as a main effect**

This is the one question W-2 answers cleanly and in WWOX's favour.

- **Model 1 (no folate, no arsenic):** the chr16/WWOX variants are among *"five variants nominally
  associated with SB on chromosomes 16 and 19"*. **The WWOX signal is a MAIN EFFECT — it does not
  require any interaction term to appear.**
- **Model 2 (folate as covariate):** *"the five previously identified variants remained nominally
  associated with SB and no additional loci were identified"* (λ=1.09, LDSC=1.03). **Survives.**
- **Model 3 (folate as interaction term):** two *additional* variants appear — `rs7925532` and
  `rs7936053`, in **CNTN5**. WWOX is not re-reported here but is not reported as lost either.
- **Models 4–5 (arsenic covariate, then arsenic interaction):** arsenic as covariate added nothing;
  the arsenic interaction surfaced a chr2 lncRNA locus (`rs438326`) and, via the folate-interaction
  term, **CTNNA2** (`rs925404`, OR 22.39, p=4.60E‐06).

🔴 **So the WWOX locus is NOT a folate-interaction finding.** It is the base-model main effect, and
it persists when folate is controlled for. **CNTN5 is the folate-interaction locus; CTNNA2 is the
arsenic-conditioned one.** Do not let W-2 be cited as "a folate × WWOX interaction" — the paper does
not report one.

Neither exposure differed between groups: folate *"was not different between case and control
groups"* (case median 133,897 vs control 143,418 µg/year, Wilcoxon p=0.30); arsenic likewise
(0.99 vs 1.07 µg/g, p=0.41). Periconceptional folic-acid use: 13.5% of cases vs 21.6% of controls,
p=0.21 (Table 1).

### 3.7 Replication — **none external; internal technical replication is UNATTRIBUTABLE**

**External: NONE.** Abstract: *"These nominal associations should be assessed in additional cohorts
with larger sample sizes."* Discussion: *"Future studies can replicate this hypothesis‐generating
analysis in a larger cohort with more comprehensive covariates."* and *"Additional work is also
needed to clarify any role for these genes in NTD formation."*

**Internal technical replication (§3.4) — WWOX's status in it cannot be determined.** Verbatim:
*"Two previously identified nominal loci were replicated using the imputed dosages computed on the
Michigan Imputation Server–theafter considering 10 PCs, age, and sex as covariates, and folate as a
covariate and interaction terms (Figure), and thelocus after considering 10 PCs, age, and sex as
covariates, and folate and arsenic as covariates and interaction terms (Figure)."*

🔴 **Both gene names are elided.** Attribution method attempted and its result stated: the two
replicated loci are described by the *model* they came from — the folate-interaction model and the
folate+arsenic-interaction model — which in §3.2 and §3.3 produced **CNTN5** and **CTNNA2 / the
chr2 lncRNA** respectively. **That is suggestive that WWOX was not among the two replicated loci,
and it is NOT asserted**, because the WWOX variants also persisted into the folate-interaction
model and could be the first referent. **Recorded as unresolved on this surface.** It is a
*technical* replication (re-imputation on a second server from the same 186 samples) in any case —
**it is not independent evidence and could not have been, since no second cohort exists.**

### 3.8 Does the paper say anything about WWOX biology? — one attributed sentence

*"encodes a WW domain‐containing oxidoreductase which is expressed in the developing spinal cord
(Chen et al.)."*

🔴 **Cited to Chen et al. — it is a literature statement, not a measurement made here.** It is
nonetheless the only sentence in either paper that ties WWOX to a *prenatal human/mammalian
neurodevelopmental structure*, and it is the closest either paper comes to the node's question.
**It is a citation LEGEND could chase; it is not evidence LEGEND has acquired.**

The remaining WWOX discussion is generic domain description (WW domains bind PPxY motifs; the SDR
domain's *"physiological substrate(s) for this domain have not been identified yet"*) and a broken-
by-elision sentence naming spinocerebellar ataxia and epileptic encephalopathy. **The authors state
plainly: "While none of these genes have been associated with SB previously".**

### 3.9 What was NOT tested in W-2

- **No functional work of any kind.** No expression, no eQTL, no perturbation, no model system.
- **No brain or spinal-cord imaging, no neurodevelopmental outcome, no seizure phenotype.** The
  endpoint is the presence of a myelomeningocele/meningocele at ascertainment.
- **No rare or biallelic WWOX variant.** MAF ≥1% was an inclusion filter on both the array and the
  imputed set — **rare variants were excluded by design, twice.**
- **No WWOX-deficient individual.** No participant is reported to carry a WWOX-related disorder.
- **No periconceptional exposure measurement.** The authors name this themselves: *"As folate intake
  and arsenic levels used in this study are based on proxies obtained at enrollment, these may
  differ from periconceptional exposures most relevant to NTD development."* **The exposure window
  that matters for neural tube closure was not measured.**
- **No maternal genotype.** Only infant genotype was tested, though maternal folate is the exposure.
- **No anencephaly** — cases are spina bifida only.
- Authors' own limitations, verbatim: *"Limitations to the study include the small cohort size for
  high‐dimensional GWAS analysis, the use of single timepoint data for folate and arsenic levels,
  and the potential for unmeasured confounding factors to modify the observed associations."*

---

## 4 · VERBATIM LOCATORS

**Re-match method.** Each quote was copied from the tool return, the two bodies and the two metadata
abstracts were transcribed verbatim to four working files, and every quote was then matched as an
exact substring by script (`rematch.py`, exact `str.count`, no normalisation, no fuzzy matching).
**Unicode was preserved as returned** — W-2 uses U+2010 non-breaking hyphens throughout (`2.22E‐06`,
`logistic‐Firth`), which are distinct from ASCII `-` and are reproduced as such.

> ### **RE-MATCH COUNT: 51/51 matched · ZERO MISMATCHES.**
> 22 W-1 body · 3 W-1 abstract · 22 W-2 body · 4 W-2 abstract.

🔴 **Declared limitation of this check.** The match is against a **transcription** of the tool
return, so it verifies that every quote below is an exact substring of the retrieved text as
transcribed; it cannot detect an error introduced in the transcription itself. Two curly
apostrophes in W-1 (`'BrainCloud'`, `'winner's curse'`) were normalised to ASCII in transcription —
**no quote below draws on those passages.**

### 4.1 W-1 · PMID 28763065

| # | Proposition | Exact quote | Anchor |
|---|---|---|---|
| L-01 | The WWOX SNP did **not** reach the threshold | `An intronic SNP in(rs10514437) fell just short of genome-wide significance for WM` | Results ¶1 (and repeated Discussion ¶1) |
| L-02 | Abstract's hedge, preserved | `An intronic SNP in WWOX (rs10514437) neared genome-wide significance for white matter volume (P=1.56 × 10).` | Abstract (metadata surface) |
| L-03 | Threshold construction (exponents elided) | `-values <1.25 × 10were considered genome-wide significant (Bonferroni correction for four MRI phenotypes, which is from the conventional GWAS threshold of 5 × 10[ref.] divided by four)` | Methods · Statistical methods |
| L-04 | Suggestive level construction | `The suggestive significance level for this correction was=1.25 × 10, which is derived from the conventional suggestive GWAS threshold of 5 × 10[ref.] divided by four.` | Methods · Statistical methods |
| L-05 | Hypothesis-free scan, not candidate-gene | `We investigated associations between 8 762 422 SNPs and four infant brain volume measures (ICV, GM, WM and CSF).` | Methods · Statistical methods |
| L-06 | Cohort size and age range | `A total of 561 infants (300 male, 261 female) between 0 and 24 weeks of age` | Methods · Subjects |
| L-07 | Ancestry composition | `Overall, 63% of subjects are European ancestry; remaining subjects are primarily African ancestry.` | Methods · Subjects |
| L-08 | Life stage — the node's premise | `infants who received high-resolution MRI scans of the brain around 5 weeks of age` | Introduction ¶2 |
| L-09 | Variants were imputed | `Imputation was performed with MACH-Admixusing the 1000 Genomes Project (1000G) reference panel` | Methods · Genome-wide genotyping |
| L-10 | Endpoint is global tissue volume | `Automatic segmentation of brain tissue into gray matter (GM), white matter (WM) and cerebrospinal fluid (CSF) was performed using an atlas-based expectation-maximization segmentation algorithm` | Methods · Image acquisition and analysis |
| L-11 | Power limit | `Sample size is sufficient to discover a genetic effect on the order of ~8% with 80% power` | Methods · Statistical methods |
| L-12 | Permutation, exponent elided | `Permutation testing yielded an empirical-value of 8 × 10for rs10514437's association with WM` | Results ¶2 |
| L-13 | The other, significant hit (for contrast) | `An intronic SNP in(rs114518130) achieved genome-wide significance for GM` | Results ¶1 |
| L-14 | Gene identity of both hits | `An intronic single-nucleotide polymorphism (SNP) in IGFBP7 (rs114518130) achieved genome-wide significance for gray matter volume (P=4.15 × 10).` | Abstract (metadata surface) |
| L-15 | Other loci also only "nearing" | `Additional loci nearing genome-wide significance were located near (within 500 kb) transcriptional regulators expressed in developing brain` | Results ¶1 |
| L-16 | Ancestry caveat — gene unattributable | `Although Fvalues were below 0.05 for our top hits inand, we note that the minor (A) allele for theSNP is very rare in populations of European ancestry` | Results ¶3 |
| L-17 | …and the sensitivity analysis it blocked | `We were unable to run sensitivity analysis in individuals of European ancestry as the minor allele did not occur in this group.` | Results ¶3 |
| L-18 | **No replication cohort exists** | `These comparisons do not represent a conventional replication sample.` | Discussion ¶3 |
| L-19 | Replication is still owed | `To our knowledge, this is the first study of its kind, consequently independent replication is critical.` | Discussion · Conclusion |
| L-20 | The caveat repeated at the close | `This is particularly true for the intronic SNP inwhich has a low minor allele frequency, was imputed, and was not present in the largest racial/ethnic group in the study.` | Discussion · Conclusion |
| L-21 | Cross-age overlap is minimal — Results | `However, percent overlap in sign tests was minimal and the percent of variance explained by polygenic scores was small.` | Discussion ¶3 |
| L-22 | …and the conclusion drawn from it | `The overall pattern of results suggests genetic determinants of global brain volumes are highly distinct at different ages.` | Discussion ¶3 |
| L-23 | Abstract states the same | `suggests minimal overlap between common variants impacting brain volumes at different ages` | Abstract (metadata surface) |
| L-24 | Cross-age polygenic signal exists but is weak | `Neonatal polygenic scores for WM showed positive associations with adolescent WM at thresholds between<0.01 and<0.5` | Results ¶6 |
| L-25 | WWOX biology is cited, not measured | `Mutations inare associated with brain phenotypes including autosomal recessive spinocerebellar ataxia-12 (SCAR12; MIM #614322), epilepsy, mental retardation and microcephaly.` | Discussion ¶1 |
| L-26 | The WM plausibility argument is an **adult** analogy | `In adult human brains, levels of the protein encoded by(WOX1) are high in neuronal axons and nerve bundles such as corpus callosum and striatal fascicles,consistent with our observed association with WM.` | Discussion ¶1 |

### 4.2 W-2 · PMID 41378749

| # | Proposition | Exact quote | Anchor |
|---|---|---|---|
| L-27 | **The WWOX variants are INTRONIC, and the rsID is rs28688166** | `Three variants on chromosome 16 were within the 8th intron of, including rs28688166 (Effect allele [EA] = C, odds ratio [OR] = 6.20,= 2.22E‐06; Figure).` | Results § 3.1 |
| L-28 | **The abstract says "coding region" and names a different rsID** | `one within the coding region of WWOX, including rs7184417 (odds ratio [OR] = 6.20, p = 2.22E-06)` | Abstract · Results (metadata surface) |
| L-29 | The same upgrade applied to ISOC2 | `a second in the coding region of ISOC2 (rs4801638; OR = 0.24, p = 5.75E-06)` | Abstract · Results (metadata surface) |
| L-30 | …against the body's weaker wording | `On chromosome 19, one variant overlapped(rs4801638; EA = G, OR = 0.24,= 5.75E‐06; Figure)` | Results § 3.1 |
| L-31 | **Only a suggestive threshold was ever applied** | `We addressed multiple comparisons by only considering loci above the suggestive threshold= 1E‐05.` | Methods § 2.5 |
| L-32 | **Analysed n is 89/97** | `A total of 7,152,841 variants from 89 participants with SB and 97 participants without (Table) were included` | Results § 3.1 |
| L-33 | Table confirms the case count | `Cases (= 89)` | Table 1 |
| L-34 | **The abstract says 91** | `After quality filtering, genome-wide association was performed on 91 infants with SB and 97 without.` | Abstract · Methods (metadata surface) |
| L-35 | Where "91" comes from | `Among 226 infants with genotype data, 189 (cases = 91, controls = 98) had maternal food frequency data available.` | Methods § 2.4 |
| L-36 | …and why the final set is 186 | `of those 189 infants, 186 also had maternal toenail arsenic concentration data` | Methods § 2.4 |
| L-37 | Five nominal variants in the base model | `Logistic‐Firth hybrid regression identified five variants nominally associated with SB on chromosomes 16 and 19` | Results § 3.1 |
| L-38 | **WWOX survives folate adjustment** | `When folate was included as a covariate (λ= 1.09, LDSC= 1.03), the five previously identified variants remained nominally associated with SB and no additional loci were identified` | Results § 3.2 |
| L-39 | Folate did not differ between groups | `Folate intake was not different between case and control groups` | Results § 3.2 |
| L-40 | Statistical method | `Genome‐wide association studies (GWAS) were completed using logistic‐Firth hybrid regressions with covariates as indicated.` | Methods § 2.5 |
| L-41 | The interaction terms | `Maternal folate intake and maternal nail arsenic concentration were included as covariates along with their interaction terms (SNP × Folate, SNP × Arsenic) as indicated.` | Methods § 2.5 |
| L-42 | Imputation and MAF filter | `Variants with an estimated imputation quality (R2) ≥ 0.7 (11,568,400 variants) and MAF ≥ 1% (7,152,841 variants) were retained` | Methods § 2.3 |
| L-43 | Replication was technical, and its loci unattributable | `Two previously identified nominal loci were replicated using the imputed dosages computed on the Michigan Imputation Server` | Results § 3.4 |
| L-44 | **"nominal" is the authors' own word** | `Our results, while only nominal associations, highlight the importance of considering multidimensional contributors` | Discussion |
| L-45 | **The requested verbatim: replication is owed** | `These nominal associations should be assessed in additional cohorts with larger sample sizes.` | Abstract · Conclusions (metadata surface) |
| L-46 | …restated in the Discussion | `Future studies can replicate this hypothesis‐generating analysis in a larger cohort with more comprehensive covariates.` | Discussion |
| L-47 | …and again | `Additional work is also needed to clarify any role for these genes in NTD formation.` | Discussion |
| L-48 | Authors' own limitations | `Limitations to the study include the small cohort size for high‐dimensional GWAS analysis, the use of single timepoint data for folate and arsenic levels, and the potential for unmeasured confounding factors to modify the observed associations.` | Discussion |
| L-49 | These genes are novel to SB — no prior | `While none of these genes have been associated with SB previously` | Discussion ¶1 |
| L-50 | The one prenatal WWOX statement — **attributed, not measured** | `encodes a WW domain‐containing oxidoreductase which is expressed in the developing spinal cord (Chen et al.).` | Discussion ¶1 |
| L-51 | SDR substrate still unknown (corroborates standing model) | `the physiological substrate(s) for this domain have not been identified yet.` | Discussion ¶1 |
| L-52 | WWOX described only as an oxidoreductase without substrate | `while both WWOX and ISOC2 are oxido‐reductases without defined substrates.` | Discussion ¶5 |

*(52 rows drawing on 51 distinct verified quotes; L-01 matches at two positions in W-1, Results and
Discussion, and is cited once.)*

---

## 5 · NEGATIVE RESULTS — what these papers CANNOT support

This section is the main output of the wave. **A clean negative is the finding here.**

### 5.1 Neither paper is a mechanism result

🔴 **BOTH ARE ASSOCIATION STUDIES. NEITHER CONTAINS A PERTURBATION OF ANY KIND** — no knockdown, no
knockout, no overexpression, no rescue, no drug, no cell line, no animal, no tissue. **No causal
verb may be used of either.** WWOX is not shown to *do* anything in either paper; a statistical
signal was observed at a locus that contains WWOX.

### 5.2 A GWAS locus is not a gene function — and neither paper establishes the gene

- **W-1** offers **no evidence that rs10514437 affects WWOX**, and states of its top associations
  generally that **"none are known eQTLs"**. The SNP is intronic in a 1.1 Mb gene spanning a common
  fragile site. **Attributing the WM signal to WWOX function is an assumption the paper does not
  test.**
- **W-2** likewise provides **no functional, expression or eQTL evidence**; the chr16 variants are
  intronic and the gene is named by position.

### 5.3 What each paper specifically cannot support

**W-1 cannot support:**
- ❌ *"A WWOX variant is significantly associated with infant white matter."* **It is not — it fell
  short of the paper's own threshold.** The only defensible phrasings are the sources' own:
  **"neared"** / **"fell just short of"** genome-wide significance.
- ❌ Any effect size, direction or risk allele for rs10514437 — **not recoverable from this surface.**
- ❌ Any statement about *regional* white matter, myelin, corpus callosum, g-ratio or oligodendrocytes.
  **The measurement is one global volume.**
- ❌ Any replicated finding. **There is no replication cohort, and the authors say replication is
  "critical" and not done.**
- ❌ Any claim about WWOX-deficient brains. Rare variants were excluded by MAF filter.

**W-2 cannot support:**
- ❌ *"A coding-region WWOX variant is associated with spina bifida."* **The Results place the
  variants in the 8th intron; the abstract's rsID appears nowhere in the paper.**
- ❌ *"A WWOX variant reached genome-wide significance."* **Nothing did, and no genome-wide threshold
  was applied.** The word is **nominal**.
- ❌ *"Folate interacts with WWOX."* **The paper reports no such interaction.** WWOX is a base-model
  main effect; the folate-interaction locus is CNTN5.
- ❌ Any replicated finding. **No external cohort exists**; the internal technical replication
  re-imputes the same 186 samples and **its loci cannot be attributed to WWOX on this surface.**
- ❌ Any claim that WWOX causes, or contributes causally to, neural tube defects. OR 6.20 with 89
  cases at p = 2.22E‐06 against a suggestive threshold is a **hypothesis-generating signal** — the
  authors call their own analysis *"hypothesis‐generating"*.

### 5.4 Negatives that are NOT negatives — instrument readings

🔴 Per `D-15`, the following are **instrument artefacts and must not be recorded as absences**:
`WWOX` = 0 and `IGFBP7` = 0 in the W-1 body; all superscript exponents in both papers; all citation
numbers in W-1; the gene names in W-2 § 3.4's replication sentence; the gene names in W-1's F-st and
ENIGMA2 sentences. **No conclusion in this file rests on any of these counts.**
Conversely, `genome-wide significan` = 0 and `exon` = 0 in the W-2 body **are** informative, because
those strings are not italicised tokens and the same passages render other unitalicised text
correctly.

### 5.5 No figure image was inspected

`D-14` holds. W-2's Figure 1 legend was returned as body text and is quotable; **no figure panel in
either paper was inspected, and no finding here rests on one.**

---

## 6 · GENOTYPE TRANSFERABILITY

> ### 🔴 **HEADLINE: A NOMINAL COMMON-VARIANT ASSOCIATION TELLS US NOTHING ABOUT A BIALLELIC NULL.**
> **Neither paper touches ANY WOREE genotype class. Not one.**

### 6.1 The argument, stated in full so it is not skipped

WOREE is caused by **biallelic rare loss-of-function** of WWOX: two damaged alleles, little or no
functional protein. Both papers measure **common variation (MAF ≥1%) in individuals carrying two
ordinarily functional WWOX alleles** — rare variants were *excluded by design* in both, by an
explicit MAF filter (W-1: MAF <0.01 dropped; W-2: MAF ≥1% applied twice).

A common-variant association at a locus **could** in principle inform a biallelic-null mechanism,
but **only** under three assumptions, all of which must be argued and **none of which is satisfied
here**:

| Assumption | Status in W-1 | Status in W-2 |
|---|---|---|
| **A1 — the variant acts *through WWOX*** (eQTL, splicing, regulatory evidence) | ❌ **Not shown.** No functional data; the paper says of its top loci that "none are known eQTLs" | ❌ **Not shown.** No functional data of any kind |
| **A2 — the phenotype is monotone in WWOX dosage** across the whole range from 2 functional alleles to 0 | ❌ **Not shown, and not testable in this design.** Small quantitative shifts among two-allele carriers do not extrapolate to a null | ❌ **Not shown.** Same |
| **A3 — the association is robust** | ❌ **Fails: sub-threshold, unreplicated, single cohort**, possibly rare-allele-and-imputed | ❌ **Fails: nominal against a suggestive threshold, n=186, unreplicated externally** |

**With A1 and A2 unestablished and A3 failed in both papers, no inference to any WOREE genotype
class is available.** The inference would be weak even if A3 held, because A1 and A2 are the load-
bearing ones.

### 6.2 Per genotype class

| Genotype class | Touched by W-1 / W-2? | Why |
|---|---|---|
| **null / null** | ❌ **NO** | Requires two rare LoF alleles. **Excluded by the MAF filter in both papers.** No participant is reported with a WWOX-related disorder |
| **splice / null** | ❌ **NO** | Neither paper examines splicing, splice-site variants, or transcript structure. `exon` = 0 in W-2's body; no transcript analysis in W-1 |
| **splice / missense** | ❌ **NO** | Same. Neither paper contains a missense variant or a splice variant |
| **missense / missense** | ❌ **NO** | **Neither paper reports a single WWOX coding variant.** W-2's abstract appears to — and its Results refute it (8th intron). This class is *specifically* the one W-2 looked like it might touch, and it does not |
| **residual-protein** | ❌ **NO** | Requires a protein-abundance or activity measurement. **Neither paper measures WWOX protein or mRNA at all** |
| **large deletion / CNV** | ❌ **NO** | W-1 *did* analyse CNVs — and reported **CNV burden was not significantly associated with any neuroimaging trait**, with no WWOX-specific CNV reported. That is a null on CNV *burden* in a general population, **not** evidence about a WWOX 16q23.1 deletion. W-2 performed no CNV analysis |

### 6.3 The one honest residue

The **endpoint classes** are directionally consistent with WOREE phenotypes — W-1's phenotype is
white matter, and WOREE imaging shows hypomyelination and callosal hypoplasia; W-2's endpoint is
neural tube closure, the earliest neurodevelopmental endpoint there is. **Directional consistency
of an endpoint is not evidence of a shared mechanism**, and in W-1's case the association did not
reach the paper's own threshold. **This residue raises no belief and is recorded so it is not
mistaken for one later.**

---

## 7 · 🔴 CORRECTION TO THE BRIEF AND TO THE SCOUT — both papers ARE held

The brief invited a correction if the scout was wrong. **It is wrong, and the way it is wrong is the
failure mode [[AUTONOMOUS_SESSION_STATE]] already names: "a delegate's census describes THE FIELD,
never THIS REPOSITORY." It has recurred.**

**What is true:** neither PMID carries a **paper-registry record** and neither carries a **receipt**.
Verified: `registry_records.py get --pmid <both> --hops 1` → `NO RECORD MATCHED` on both;
`reading_state.py` → 123 papers, 186 receipts, **0 occurrences of either PMID**.

**What is false:** the scout's *"NOT HELD — no record in any surface"*. **Both papers are present in
the repository, and the substantive conclusion for each had already been reached:**

| Surface | Git state | What it holds |
|---|---|---|
| [[wwox_myelin_oligodendrocyte_census_20260921]] (line 131) | **clean/committed** | **PMID 28763065 is already tabulated**, with the hedge intact and the caveat already drawn: *"GWAS: intronic WWOX SNP rs10514437 **neared** genome-wide significance for infant white-matter volume. Common variant, not WWOX deficiency"* — and the group verdict: *"**None of these six distinguishes hypomyelination from demyelination, or oligodendrocyte failure from axonal loss.** They are the class of evidence the model already had."* |
| `discovery_ledger_current.md` (line 1487, record **`DL-MECH-060`**) | **clean/committed** | **PMID 41378749 is already a `READ_NEXT` directive**, with the correct caveat pre-written: *"spremere il valore metodologico/traslazionale senza confondere contesto prenatale generico con WWOX"* |
| `therapeutic_hypotheses_ledger_current.md` (line 131, **`HYP-20260705-07`**) | **clean/committed** | **The folate lead is already forged, scored and PARKED** — *"Folate/neural-tube bridge resta background, non repurposing"*, ranked **3/15**, translatability *bassa*, `status: parked`, with *"Evidenza PRO: PMID 41378749 nel batch"* |
| `batch_queue.md` (lines 461, 523) | clean/committed | both PMIDs present as corpus-seed rows, `unmatched` |
| `full_text_queue_current.md` (FT-113) | uncommitted when I checked; **committed mid-session** by a parallel actor (`e096984`) | both PMIDs, in the queue entry the scout itself wrote today |

### 7.1 Why the check missed it — a reproducible tool-coverage finding

1. **`registry_records.py get --pmid` answers "is there a RECORD KEYED TO this PMID", not "does the
   laboratory know this paper".** `discovery_ledger_current` **is** in the tool's searched surface
   list and **is** clean in the working tree, yet `get --pmid 41378749` returns `NO RECORD MATCHED`
   while that file contains the PMID as a `READ_NEXT` line **inside** `DL-MECH-060`. **A PMID
   mentioned in a record's body is not found by `--pmid`.**
2. **Two surfaces that hold these papers are not searched by the tool at all:**
   `therapeutic_hypotheses_ledger_current.md` (where the folate hypothesis is parked) and
   `disease-models/wwox/analysis/` (where the myelin census sits). The tool's `--source` list names
   seven surfaces and neither is among them.
3. **`full_text_queue_current.md` was uncommitted at the time of the check**, so the tool — which
   reported reading *"at commit 9a2092040523"* — could not have seen FT-113. It was committed later
   in the session by a parallel actor (`e096984`), which is itself the point: **the tool reads
   committed state, and a parallel laboratory moves under it.** Not a defect; a staleness artefact.
4. **The tool itself printed the correct warning and it was overridden:** *"🔴 This is not evidence
   that the laboratory does not know this paper: it is a statement about this query over these
   files."* **The scout converted that warning into a negative.** The tool behaved correctly.

### 7.2 Two live incorrect statements flagged for the Orchestrator (I am read-only; nothing edited)

1. **[[next_node_scout_20260921_orchestrator]] § 4, row W-2** states *"A **coding-region** WWOX
   variant (`rs7184417`, OR 6.20, p = 2.22E-06)"*. **Both the location and the rsID reproduce the
   abstract and are contradicted by that paper's Results** (§ 3.4 above). The row's *"nominally"* is
   correct and survives.
2. **[[next_node_scout_20260921_orchestrator]] § 4, rows W-1 and W-2** mark both papers
   **"🔴 NOT HELD — no record in any surface"** / **"🔴 NOT HELD"**. **Accurate as a statement about
   registry records and receipts; false as a statement about the repository** (§ 7 above).

### 7.3 Method rule earned here

> 🔴 **`NO RECORD MATCHED` IS NOT `NOT HELD`.** Before a brief or a scout calls a paper new, the
> PMID must be checked against the **analysis directory and the therapeutic-hypotheses ledger** as
> well — neither is covered by `registry_records.py` — **and against the uncommitted working tree**,
> which the tool does not read. A plain PMID sweep across `disease-models/` costs one command and
> would have caught all five hits here. *(This is a structural extension of the standing rule
> "a delegate's census describes the field, never this repository", which was already written down
> and still did not prevent the error, because the delegate ran the right tool and misread its
> output rather than skipping the check.)*

---

## 8 · THERAPEUTIC CLASSIFICATION

Only W-2 contains anything intervention-adjacent. W-1 contains nothing.

| Item | What it actually is in the paper | **Classification** |
|---|---|---|
| **Folate / maternal folate intake** | An **observational maternal dietary exposure**, derived from a food-frequency questionnaire at enrolment (after birth), used as a **covariate and interaction term**. **Not administered, not randomised, not titrated, not measured periconceptionally.** It did not differ between cases and controls (p=0.30), and periconceptional folic-acid use did not either (13.5% vs 21.6%, p=0.21). **No folate effect on any WWOX-related quantity is reported, and no folate × WWOX interaction is reported anywhere in the paper.** | **NOT TRANSFERABLE TO WOREE** |
| **Folic acid supplementation** (Introduction background only) | A population-level public-health measure cited from prior literature (23% NTD reduction, 70% severity reduction in the US). **Not studied here, and not studied in any WWOX context.** Its window is **periconceptional** — closed years before WOREE presents. | **NOT TRANSFERABLE TO WOREE** |
| **Arsenic / maternal toenail arsenic** | An **environmental toxin exposure**, a covariate and interaction term. **Not an intervention at all.** Did not differ between groups (p=0.41). | **NOT TRANSFERABLE TO WOREE** |
| **W-1: anything** | Nothing intervention-like. The Discussion's closing aspiration *"it may be possible to develop treatments that normalize adverse trajectories"* is an ambition for the field, not a candidate, a target or a result. | **n/a — no intervention present** |

> **This corroborates rather than creates.** `HYP-20260705-07` already parked exactly this lead at
> **3/15** with translatability *bassa* and the note *"non usare per cambiare terapia"*. **The full
> read supports that parking and supplies the reason it was right: the paper reports no WWOX ×
> folate interaction at all, so even the weak bridge the hypothesis entertained is not present in
> the source.** `HYP-20260705-07` should stay `parked`; this file adds a reason, not a re-score.
> **No therapeutic hypothesis is created, modified or promoted by this wave.**

---

## 9 · INFORMATION GAIN

| Item | Changed? | One line |
|---|---|---|
| **Mechanistic graph** | ❌ **NO** | Neither paper contains a perturbation, an expression measurement or an eQTL; two association signals at a locus add no edge and modify none. |
| **Therapeutic hypothesis** | ❌ **NO** | The only intervention-adjacent item (folate) was already forged, scored 3/15 and parked as `HYP-20260705-07`; the read supports that parking and creates nothing. |
| **Experimental roadmap** | ❌ **NO** | Neither paper suggests an experiment LEGEND could run or commission; W-2's one interesting pointer (*"expressed in the developing spinal cord (Chen et al.)"*) is a **citation to chase**, not a roadmap item, and is logged in § 10 as such. |
| **Genotype stratification** | ❌ **NO** | **Zero of six genotype classes are touched.** Both papers excluded rare variants by MAF filter, by design, and neither reports a single WWOX coding or splice variant. |
| **Intervention ranking** | ❌ **NO** | Nothing ranked, nothing re-ranked, nothing added or removed. |
| **Uncertainty** | ❌ **NO** | No belief in the working model moves up or down. What changes is *documentation*: two leads that **looked** open are now closed **with numbers and the authors' own hedges** rather than with an abstract sentence — which prevents a future overclaim without altering a present belief. |

> ### **NO ACROSS THE BOARD, on all six, for the disease model.**

**The wave's actual yield is methodological, and it sits outside the six items — recorded here so it
is not smuggled into one of them:**

1. **A live incorrect statement in a landed repository file is identified and flagged** — the
   "coding-region WWOX variant" in the scout, refuted by the source's own Results (§ 3.4, § 7.2).
   **This prevents a false premise entering the model**; it does not add a true one.
2. **A reproducible tool-coverage gap is characterised** — `NO RECORD MATCHED` ≠ `NOT HELD`, with
   the three specific mechanisms named and a one-command remedy (§ 7.1, § 7.3).
3. **Three further abstract-vs-Results discrepancies are documented in a single paper** (rsID,
   coding-vs-intronic, n), extending the standing count and making W-2 the densest worked example
   LEGEND holds of that pattern.
4. **W-1 supplies an empirical, citable constraint against life-stage extrapolation** (§ 2.8):
   infant and adult brain-volume genetics overlap minimally, measured four ways in one cohort.
   **This is a constraint on how LEGEND may reason, not a WWOX finding** — and it is precisely the
   lesson the Chang batch reached structurally, now with numbers behind it from a human cohort.

---

## 10 · DEFAULTS TAKEN — decided without instruction

1. **Recovered the threshold exponents by arithmetic** (1.25 × 10⁻⁸ / 10⁻⁷) from the mantissas that
   survived plus the paper's own stated construction, and **labelled the result INFERENCE** rather
   than quoting a number the extractor did not return. **The verdict does not depend on it.**
2. **Did NOT assert the exponent of the WWOX p-value.** Reported the mantissa `1.56` as quoted,
   named `1.56 × 10⁻⁸` as the most likely reconstruction with the reasoning shown, and flagged the
   exact value as a standing `D-15` acquisition need. **A PDF or the JATS would settle it.**
3. **Used the PubMed *metadata* abstract as a second surface** to recover the gene symbols the
   full-text extractor elided (IGFBP7 ↔ rs114518130, WWOX ↔ rs10514437). Kept the two surfaces as
   **separate re-match corpora**, since their Unicode and punctuation differ.
4. **Left two gene attributions unresolved rather than guessing** — W-1's ancestry caveat (§ 2.6)
   and ENIGMA2 sentence (§ 2.5), and W-2's technical-replication loci (§ 3.7). Both branches are
   stated for the W-1 caveat and **the verdict is written to hold under the worse branch.**
5. **Mentioned the dbSNP accession-range indication in § 2.6 but excluded it from every conclusion**,
   as it is a numbering convention and not evidence from either paper.
6. **Ran an unrequested repository-wide PMID sweep** beyond `registry_records.py` and
   `reading_state.py`, because the brief invited verification of the scout's "not held" claim and
   the registry tool prints an explicit warning that its negative is not a repository-level one.
   **This produced § 7, and I judge it the most valuable part of the wave.**
7. **Flagged, did not fix,** the two incorrect statements in
   `next_node_scout_20260921_orchestrator.md`. I am read-only toward every file but this one.
8. **Counted L-01 once in the locator table** although it matches at two positions in W-1 (Results
   and Discussion); the re-match script reports the multiplicity.
9. **Transcribed both bodies to working files to make the re-match executable**, and **declared the
   limitation of doing so** (§ 4) rather than claiming a check stronger than the one performed.
10. **Did not record a receipt, did not create a commit candidate, did not touch any canonical
    file.** No `FULLTEXT_READ_RECEIPT` is claimed for either paper, per the brief.

---

*END — `human_prenatal_infant_wave1_20260921.md`. Read-only wave. Nothing canonical was modified.*
