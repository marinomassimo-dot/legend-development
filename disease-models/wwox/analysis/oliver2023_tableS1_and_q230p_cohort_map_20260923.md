# Oliver 2023 supplement (PMID 36779245) — Table S1, the `s001` bonus, and a reconciled `Q230P` patient map

> **Discovery-space artefact.** `HYPOTHESIS ≠ CLAIM`. Nothing canonical; nothing propagated.
> **Not medical advice.** Disease-level genotype classes only; no individual is described or linked.
> **Public edition.** Bibliographic metadata from **PubMed**.
> Artefacts: `files/fulltext/PMID36779245_Oliver2023_suppl_TableS1.xlsx` (`sha256 7825f659…2d74`) and
> `files/fulltext/PMID36779245_Oliver2023_suppl_S1_info.docx` (`sha256 4c674762…c41f`).

---

## 0 · Identity, and one correction to the acquisition record

Oliver KL, Trivisano M, … Scheffer IE. *"WWOX developmental and epileptic encephalopathy:
Understanding the epileptology and the mortality risk."* **Epilepsia 2023;64(5):1351–1367**,
`doi:10.1111/epi.17542`, `PMC10952634`. Verified against PubMed.

🟢 **Both supplementary files belong to this one study.** `EPI-64-1351-s002.xlsx` = **Supplementary
Table S1**; `EPI-64-1351-s001.docx` = **Supplementary Information** (methods, results, figure
legends). The filename stem `EPI-64-1351` matches the citation (volume 64, page 1351) exactly.
**No duplicate paper identity is created**; two artefacts, one study.

⚠️ **Note on the compilation's self-citation.** Inside Table S1 the paper cites itself as
*"Oliver, Trivisano et al. **2022**"* — the online-first year. The issue year is **2023**. Same
paper. The same trap applies to *"Piard J et al. Genet in Med. **2018**"*, which is
**PMID 30356099**, *Genet Med* **2019**;21(6):1308–1318, online 2018-10-25. 🔴 **One paper, two
years. Do not create a second `PAPER` record for either.**

---

## 1 · 🔴 TABLE S1 IS NOT WHAT THE ACQUISITION REQUEST ASSUMED

The pending matrix recorded `36779245` as *"`TABLE S1` only — body already read"*, closing
*"`CLAIM 033`'s survival contrast, after removing `Q230P`."*

**Table S1 contains no survival data.** It is a **variant/ACMG census**: 90 allele-observations ×
9 columns —

`Publication · Patient ID · WWOX variants · Consequence · Country of origin · Recurrent · # times reported · ACMG criteria met · ACMG classification`

🔴 **There is no age, no outcome, no date of death, no survival time and no genotype-class column.**
**The Kaplan–Meier contrast cannot be recomputed from it, with or without `Q230P`.**

And the `s001` supplement does not supply it either. Its only survival object is:

> *"**Supplementary Figure 6.** Survival analysis for **75 individuals** with WWOX-DEE stratified by
> **sex**. Time to seizure onset (A). Time to death (B). Survival curves calculated using the
> Kaplan-Meier method."*

🟢 Confirms `CLAIM 033`'s denominator (**n = 75** = the cohort's 13 + 62 from literature).
🔴 **Stratified by sex, not by genotype.** The genotype-stratified curve lives in the main paper as
a figure; **per-patient survival data are not deposited in either supplement.**

> ## 🎯 VERDICT: `SOURCE ACQUIRED` ✅ · `QUESTION AS POSED` ❌ **NOT RESOLVED — and now known to be unresolvable from any published Oliver surface.**
>
> This is not a failed acquisition. It **converts an acquisition debt into a correctly-classified
> data-availability limit**: the re-analysis requires patient-level survival data that Oliver does
> not publish. The blocker moves from `NEEDS_OPERATOR_PDF` to **`AUTHOR_DATA_REQUEST`** — a
> different class, with a different action (write to the corresponding author), and it should not
> sit in an acquisition queue any longer.

---

## 2 · 🎯 WHAT TABLE S1 *DOES* SETTLE — and it bears on `CLAIM 033` harder than the survival re-run would have

### 2.1 · `Q230P` is the most recurrent WWOX allele in the entire compilation

| Allele | Consequence | Allele-observations |
|---|---|---|
| 🎯 **`c.689A>C` p.Gln230Pro** | **missense** | **9** |
| `c.790C>T` p.Arg264Ter | nonsense | 5 |
| `c.160C>T` p.Arg54Ter | nonsense | 4 |
| `c.716T>G` p.Leu239Arg | missense | 4 |
| exon 6–8 deletion | deletion | 4 |
| exon 6 deletion | deletion | 4 |
| `c.517-2A>G` | splice site | 3 |

**Class totals** (90 allele-observations, 19 publications):
missense **28** (31.1%) · deletion 23 · nonsense 14 · splice site 14 · nonsense/frameshift 9 · duplication 2.

> ### 🔴 **`Q230P` alone is 9 of the 28 missense allele-observations — 32.1% of the entire "missense" class.**

**Why this is load-bearing.** `CLAIM 033`'s **reservation (1)** already said the null/missense split
is *"sintattica, non funzionale"*, and named `Q230P` as its own counter-example — *"`Q230P` è
missense e **azzera la proteina**."* That reservation was stated qualitatively. **It is now
quantified**: the single allele demonstrated (Johannsen, PMID 29808465, read at full depth today) to
yield **no detectable protein** is not a rare contaminant of the "≥1 missense" arm — it is **the
largest single contributor to it**.

🎯 **Oliver's own wording concedes the premise.** The abstract describes the comparator arm as
*"those carrying at least one **presumed hypomorphic** missense pathogenic variant."* **`presumed`
is the authors' word.** For ~32% of that class the presumption is contradicted by a published
Western blot.

**`INFERENZA`, and it cuts in the direction `CLAIM 033`'s "Nota di direzione" already predicted.**
Misclassifying a functionally-null allele into the "missense" (assumed-hypomorphic) arm should
**dilute** the true separation. So the reported `p = .0085` plausibly **understates** the difference
between *residual function present* and *absent*. 🔴 **This is a direction, not a magnitude.** No
recomputation is possible (§1), no hazard ratio is offered, and **no change to `CLAIM 033`'s status
is proposed here.** What changes is that reservation (1) now has a number behind it.

### 2.2 · 🔴 `c.1057-2A>G` is ABSENT from the whole compilation — reservation (3) moves from possible to verified

`CLAIM 033` reservation (3) warned that a canonical acceptor allele of the reference genotype class
*"potrebbe non appartenere alla popolazione studiata"* because Oliver enrolled only
pathogenic/likely-pathogenic variants.

**Search of all 90 allele-observations: `1057` = 0 hits.**

🟢 **The reference genotype's splice allele appears nowhere in Oliver's P/LP variant universe.**
Reservation (3) is no longer a caution about what *might* be true — it is **measured**. The
survival statistic is derived from a variant population that **does not contain this allele**.

⚠️ **Bounded.** Absence from Oliver's compilation means the allele was not in the 19 publications
Oliver aggregated. It is **not** evidence about the allele's pathogenicity, frequency or
classification anywhere else.

### 2.3 · Both alleles of the worked-example genotype class, as Oliver classifies them

| Allele | Oliver's ACMG criteria | Oliver's classification |
|---|---|---|
| `c.689A>C` p.Gln230Pro | `PM2, PP3, PM3, PP4` (+`PP5` in 6 of 9 rows) | **Likely pathogenic** |
| `c.517-2A>G` | `PVS1, PM2` | **Likely pathogenic** |

🟡 Note the inconsistency inside Oliver's own table: the **same** `Q230P` allele carries `PP5` in six
rows and not in three (Johannsen, and two Piard rows). `PP5` is reputable-source evidence, a
property of the allele, not of the patient — so it should not vary row to row. Low consequence;
recorded because it shows the table was assembled per-report, not per-allele.

---

## 3 · 🔴 A DATA-INTEGRITY DEFECT IN TABLE S1 — it cannot be used as a patient-level source

Joining on `(Publication, Patient ID)` gives **60 distinct keys for 90 allele-observations**.

- **28 keys carry exactly 2 alleles** — a readable biallelic genotype.
- **31 keys carry exactly 1 allele** — consistent with homozygosity, **but the table never says so**.
  There is no zygosity column. A homozygote and a compound heterozygote whose second allele went
  unlisted are **indistinguishable**.
- 🔴 **1 key carries THREE alleles:** `Piard J et al. Genet in Med. 2018 | pt #19` →
  `c.1073C>T p.Thr358Ile` + `c.598A>G p.Lys200Glu` + `c.689A>C p.Gln230Pro`.
  **No biallelic recessive genotype has three alleles.** Either the patient identifier is reused
  across distinct individuals, or one row is mis-assigned.

> 🎯 **This is exactly why the Operator brief's rule holds: *Oliver Table S1 is a useful compilation,
> not an independent patient observation; the primary paper wins for patient-level detail.*** The
> defect is not hypothetical — it is present, it touches a `Q230P` row, and anyone reconstructing
> genotypes from this table without the primaries would have inherited it silently.

---

## 4 · RECONCILED `Q230P` GLOBAL PATIENT MAP

Built from **primary sources first**, with Table S1 used **only** to enumerate reports and detect
omissions. Every allele-observation is attributed to the publication that made it.

| Primary source | Table S1 key | Ancestry (as printed) | Genotype class | Patients | Provenance strength |
|---|---|---|---|---|---|
| **Johannsen 2018** · PMID 29808465 | `Family1` | Afghan | 🟢 **`Q230P` / `Q230P`** homozygous | **2** (cousins, two related consanguineous families) | 🟢 **PRIMARY, full text read 2026-09-23** — *"homozygosity for the missense variant c.689A>C … in both girls"* |
| **Weisz-Hubshman 2019** · PMID 30853297 | `Family 2` | mixed Yemenite + Moroccan + Kurdish Jewish (family level) | 🟡 **`Q230P` / `c.517-2A>G`** compound heterozygous | **2 affected + 2 unaffected carriers** | 🟢 **PRIMARY, full text read 2026-09-23** — pedigree-level, not prose-level |
| **Piard 2019** · PMID 30356099 | `pt #6` | France | 🟡 `Q230P` / `c.1138dup p.Cys380LeufsTer149` | 1 | 🟡 **COMPILATION ROW** — primary not re-read today |
| **Piard 2019** | `pt #7` | Iran | 🟡 `Q230P` / **(second allele unlisted)** | 1 | 🟡 zygosity **not stated by the table** |
| **Piard 2019** | `pt #20` | Moroccan | 🟡 `Q230P` / **(unlisted)** | 1 | 🟡 zygosity not stated |
| **Piard 2019** | `pt #19` | France | 🔴 **UNUSABLE — three alleles listed** (§3) | ? | 🔴 **EXCLUDED from any count** |
| **Oliver 2023** · PMID 36779245 | `pt #1` | Italy | 🟡 `Q230P` / `exon 7–8 deletion` | 1 | 🟡 compilation + own cohort |
| **Oliver 2023** | `pt #2` | Italy | 🟡 `Q230P` / **(unlisted)** | 1 | 🟡 zygosity not stated |
| **Oliver 2023** | `pt #5` | North Africa | 🟡 `Q230P` / **(unlisted)** | 1 | 🟡 zygosity not stated |

### 4.1 · Counting, honestly

- **Allele-observations in Table S1: 9** — this is what *"# times reported = 9"* counts. 🔴 **It is
  not a patient count.** `Johannsen Family1` is **one row and two girls**; `Weisz-Hubshman Family 2`
  is **one row and two compound heterozygotes**.
- **Patients traceable to a named primary: 2 (Johannsen) + 2 (Weisz-Hubshman) = 4**, at full
  primary-source strength.
- **Plus 3 Piard + 3 Oliver rows** at compilation strength, one Piard row excluded as unusable.
- 🔴 **Best defensible range: 10–11 individuals**, with the residual uncertainty being `pt #19` and
  any undetected overlap between Piard's and Oliver's literature aggregation.

> 🔴 **THIS CONTRADICTS THE REPOSITORY'S STANDING COUNT.**
> `missense_splice_reclassification_risk_20260921.md` §13 states `p.(Gln230Pro)` has **"8 patients,
> 6 families."** Today's reconstruction gives **10–11 individuals**. The discrepancy is **not**
> resolved here and **no canonical count is changed**. The most likely causes, in order: (a) the
> older figure predates Oliver's Table S1 and Weisz-Hubshman's full text; (b) family-level vs
> individual-level counting (Johannsen is 1 family, 2 girls); (c) genuine overlap between
> compilations that neither this file nor Table S1 can detect. **`STATE/RECEIPT` item, flagged for
> the next targeted pass.**

### 4.2 · 🔴 The rule that must travel with the compound heterozygotes

**`Q230P`/`c.517-2A>G` patients (Weisz-Hubshman Family 2) must NOT be used to isolate the molecular
effect of `Q230P`.** The other allele is a **demonstrated** severe splice defect: exon-6 skipping,
measured at band level (593 bp → 504 bp, **89 bp** = exon 6). 🔴 **That 89 nt is not a multiple of
three, so the skip is frame-shifting — but this is LEGEND's arithmetic; the paper never uses the
word "frameshift" for this allele.** Any phenotype in these two individuals is a two-allele
phenotype.
The same caution applies to `Piard pt #6` (`Q230P`/frameshift) and `Oliver pt #1`
(`Q230P`/exon 7–8 deletion).

🟢 **Only the Johannsen pair is `Q230P`/`Q230P`** — and they are therefore the **only** individuals
in the world literature from whom an unconfounded `Q230P` phenotype could be read, and the only
source of the `Q230P` functional data (§ `johannsen2018_fulltext_q230p_revival_20260923.md`).
🔴 **Weisz-Hubshman contains ZERO `Q230P` homozygotes** and **no protein work of any kind** (Western
= 0 hits, earned): it adds `Q230P` *carriers*, not `Q230P` *molecular* evidence. `CLAIM 030`'s
`PREMISE: DETECTION_FLOOR` is **not** touched by it.

### 4.3 · ⭐ The 1:177 founder rate belongs to `c.517-2A>G` alone

`c.517-2A>G` is the Yemenite Jewish founder allele: carrier rate **1:177**, measured as **2/353**
controls. 🔴 **No founder-population denominator of any kind was measured for `Q230P`**, and the
family carrying both alleles is of **mixed** Yemenite, Moroccan and Kurdish Jewish ancestry.

🔴 **Consequence for the patient map: the two Weisz-Hubshman `Q230P` individuals must not be counted
as founder-population cases, and the 1:177 carrier rate must never be attached to `Q230P`.** Table
S1's ancestry cell for this row — *"Yemenite + Moroccan Jewish + Kurdish"* — is a **family-level**
ancestry string, and reading it as **allele** ancestry is exactly the error to avoid.

🟡 **De-identification note.** Transmission attribution (which side of a family carried which allele)
is available in the primary and is **deliberately not recorded here**. It is individual-linking data
that this edition excludes, and the scientific point above is a property of the **allele**, which
needs none of it.

---

## 5 · 🎯 THE `s001` BONUS — the unrequested file carries more than the requested one

`EPI-64-1351-s001.docx` was not requested. It contains **primary RNA evidence** absent from both the
main-text abstract and Table S1.

### 5.1 · Patient 6 — two intronic deletions in *cis*, and a tissue-dependent RNA readout

> *"To further characterize this potential alternate splicing event we performed RT-PCR and Sanger
> sequencing of **fibroblast-derived RNA** from patient 6 and **leukocyte-derived RNA** from both
> [relatives] … Gel electrophoresis of these products confirmed an alternate splicing event in the
> **[carrier] leukocyte-derived RNA** sample harbouring the intronic deletions with the presence of
> the normal **489 bp** band and an additional lower band … Sequence analysis of these products
> confirmed the lower band as **exon 5 skipped** transcripts."*
>
> 🔴 *"**The alternate splicing event could not be resolved in fibroblast-derived RNA of patient 6**
> and leukocyte-derived RNA was unavailable."*

🟡 **Transmission attribution is elided in square brackets above** — it is in the primary and is
individual-linking data this edition excludes. Nothing in the finding below depends on it.

🎯 **`DATO`, and it is methodologically load-bearing.** The same laboratory, the same gene, the same
assay: **resolvable in leukocyte RNA, NOT resolvable in fibroblast RNA.** This is a direct,
published, WWOX-specific **tissue-choice warning** for any junction-spanning RT-PCR allele
characterisation — and it happens to favour exactly the surface the allele-characterisation workflow
proposes (**blood**).

🔴 **Internal contradiction in the same supplement, flagged so it is not propagated.** The body text
says *"exon 5 skipped."* The legend of its own Figure 1B says *"demonstrated **exon 6** skipping as
seen at the junction of exon 4 and 5 with underlying exon 6 sequence."* The body text is internally
coherent (exon 5 absent ⇒ exon 4 joins exon 6); **the legend's "exon 6" is a typographical error.**
Recorded because this repository already carries a live exon-5/exon-6 naming hazard.

### 5.2 · Patients 9 and 10 — allele imbalance measured by Sanger

> *"Using primers placed in **exons 4 and 6**, we identified two transcripts in the patient compared
> to the control … two copies of exon 5 were spliced into the transcript in tandem. Duplication of
> the **106-bp** exon is predicted to cause insertion of 14 amino acids and a premature termination
> codon (`WWOX:p.His173Glyfs*14`). The transcript with the duplicated exon 5 produced a **faint
> band, suggestive of low abundance.** … the transcript allele balance was **heavily skewed toward
> the `c.728dupT` allele**."*

🎯 **A cheap precedent for quantitative allele-balance readout from Sanger traces**, without qPCR
or RNA-seq. 🟢 Also yields **exon 5 = 106 bp** — a second independent exon length for the
repository's exon map.

### 5.3 · Imaging supplements bearing on the cerebellar frontier

- **Supp. Fig. 2B:** Patient 10 at 14 months — *"abnormal increased signal in **dentate nuclei** and
  dorsal medulla."* 🎯 A **cerebellar** (dentate) abnormality, in a supplement, in a genotype cohort.
- **Supp. Fig. 2A:** restricted diffusion / low ADC in **dorsal midbrain** and **dorsal pons central
  tegmental tract** in three patients.
- **Supp. Fig. 3:** Patient 7 at 19 days — *"Normal ventricles, brainstem, **cerebellum**, basal
  ganglia and occipital cortex."* 🔴 **An explicit cerebellar NEGATIVE at 19 days of age.**

🟡 **`INFERENZA`, weak and bounded:** these two rows are compatible with a cerebellar finding that is
**absent neonatally and present later**, i.e. acquired rather than malformative. **Two patients, two
time points, different individuals — this is a hypothesis-shaped observation, not a time course.**
It is offered to the `ataxia_without_cerebellar_lesion` node as a **lead**, not as evidence.

---

## 6 · DELTA SUMMARY

| Question | Before today | After today |
|---|---|---|
| `CLAIM 033` survival re-run without `Q230P` | `NEEDS_OPERATOR_PDF` (Table S1) | 🔴 **Unresolvable from any Oliver surface** → reclassify as **`AUTHOR_DATA_REQUEST`** |
| `CLAIM 033` reservation (1), *"missense is a syntactic class"* | qualitative, one counter-example | 🟢 **Quantified: `Q230P` = 32.1% of the missense class**; authors' own word is *"presumed"* hypomorphic |
| `CLAIM 033` reservation (3), *"the allele may not be in the cohort"* | a caution | 🟢 **Verified: `c.1057-2A>G` absent from all 90 allele-observations** |
| `Q230P` patient map | *"8 patients, 6 families"* | 🟡 **10–11 individuals, 4 at primary strength**; discrepancy flagged, **not** silently overwritten |
| Table S1 as a patient-level source | assumed usable | 🔴 **Defective** — no zygosity column; one key with three alleles |
| WWOX splice RT-PCR tissue choice | untested assumption | 🟢 **Published WWOX-specific evidence: leukocyte worked, fibroblast failed** |

🔴 **No canonical file, registry, queue, ledger or state manifest was modified by this reading.**
`CLAIM 033` is **untouched**; the six Operator-gated candidates were **not** touched.
