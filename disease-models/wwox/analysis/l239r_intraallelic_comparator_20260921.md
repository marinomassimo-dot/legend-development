# p.L239R — the intra-allelic comparator: what PMID 41153369 actually reports

**Analyst:** Scientist B · **Date:** 2026-09-21 · **Status:** non-canonical analysis file. Read-only toward every canonical file. No commit candidate. No treatment proposal.

**Target paper:** PMID **41153369** — Sunnetci-Akkoyunlu D, Kara B, Ozer T, Deniz A, Sakarya-Gunes A, Isik EB, Dogruoglu B, Ilkay Z, Yilmaz M, Sahin S, Eren-Keskin S, Cine N, Savli H. *Genetic Etiology of Developmental and Epileptic Encephalopathy in a Turkish Cohort: A Single-Center Study with Targeted Gene Panel and Whole Exome Sequencing.* **Genes (Basel)** 2025;16(10):1152 · PMCID **PMC12562696** · DOI [10.3390/genes16101152](https://doi.org/10.3390/genes16101152). Full text retrieved from **PubMed Central via the PubMed MCP** (`get_full_text_article`, `pmc_ids: ["PMC12562696"]`). Attribution: full text and metadata obtained **from PubMed / PubMed Central**.

**LEGEND record:** `[[paper_registry_current#PAPER 013]]` — `Status: processed`, `Genotype/model: two siblings with homozygous WWOX p.L239R`, `Claim links: none`, `Role: supportive cohort context paper`.

---

## 0 · Declared read depth and what was obtainable

| Section | State |
|---|---|
| Abstract | read — **and actively distrusted, see §0.1** |
| Introduction | read |
| Patients and Methods | read |
| Results | read (narrative only) |
| Discussion | read |
| Conclusions / limitations | read |
| **Tables (Table 1 demographic + clinical data, VUS table, WES table, literature-comparison table)** | 🔴 **NOT OBTAINABLE — every table callout returns as an empty reference and no table body is present in the extraction** |
| Figures | **not obtainable** — no figure image can be inspected in this environment and none is claimed |
| References | **not obtainable** — every citation returns as an empty bracket `[]` |

**Declared read depth: `partial_fulltext_read` — narrative body read in full; tabular data unobtainable.**

### 0.1 · Two extraction artefacts that shape everything below

1. **The empty-comma artefact is real and it is systemic, not confined to the abstract.** The MCP extractor strips **every gene symbol** from this article — in the abstract, in the Methods panel list, in the Results gene counts and in the Discussion. It is why the abstract reads `Variants were detected in,,,,,,,,,,, and.` and why the Results read `Pathogenic and likely pathogenic variants were identified in(= 8),(= 4),(= 3),(= 2),(= 2),(= 2),(= 2),(= 2),(= 1),(= 1),(= 1),(= 1) genes`. The orchestrator error recorded in the task brief — concluding from the abstract that WWOX does not appear — is fully explained: **the gene symbols are not in the delivered text at all.** They are not absent from the paper; they are absent from the extraction.
2. **Consequence for identification.** Because gene symbols are stripped, the gene carrying `p.L239R` is **never printed** in the retrievable text. It is nonetheless identifiable beyond reasonable doubt from two independent in-text anchors: the **cDNA/protein coordinates `c.716T>G, p.L239R`** (the WWOX allele named in PMID 42092735) and the **explicit disease label in the same sentence — `DEE28 or WOREE syndrome`**, which is WWOX-specific. That is stated here as an inference from surviving text, not as a quotation of the gene name.

---

## 1 · Question 1 — Find the WWOX case(s): how many, which variant, zygosity, siblings?

**Three passages in the body carry the allele. All three are reproduced verbatim, including the extractor's gaps.**

**(a) Results — segregation paragraph:**

> "According to the segregation analysis of available family members, we identified de novo variants in 18 patients (13.95%). A homozygousgene variant was detected in two siblings (case #49–50) from a consanguineous family. We identified two siblings (cases #23–24) with a homozygous variant ininherited from non-consanguineous, heterozygous parents."

**(b) Discussion — West syndrome paragraph:**

> "Additionally,missense variant (p.L239R) identified in patient (case #49) from a consanguineous family was linked to hypsarrhythmic EEG patterns and multifocal seizures consistent with previous reports emphasizing the gene's role in early-onset epilepsy and poor neurodevelopmental outcomes and linking to-related epileptic encephalopathy (DEE28 or WOREE syndrome) []."

**(c) Discussion — EIDEE paragraph:**

> "A homozygous missense variant in(c.716T>G, p.L239R) was identified in an infant presenting with hypsarrhythmia and multifocal epileptiform anomalies on a disorganized EEG background, consistent with EIDEE. While most previously reported cases involve truncating or splice-site variants leading to loss of function, emerging evidence indicates that certain missense variants may also lead to a somewhat milder course in terms of overall prognosis; nevertheless, in terms of epileptology, patients with missense variants still present with very early onset and multiple seizure types, frequently focal and spasms []."

**What can be stated as DATO:**

- The allele is **`c.716T>G, p.L239R`, homozygous**, in a patient from a **consanguineous family** — quote (c) gives zygosity and nucleotide change, quote (b) gives consanguinity.
- The gene is WWOX by coordinate + `DEE28 / WOREE syndrome` label — **INFERENCE from surviving text**, because the symbol itself is stripped.
- **Only ONE patient is individually described as carrying p.L239R: case #49.** Quote (b) names case #49 and no other.

**What is INFERENCE, and must be labelled as such — the "two siblings" attribution.**
Quote (a) states that *a* homozygous variant in *some* gene was found in **two siblings, cases #49–50, from a consanguineous family**. Quote (b) places **case #49** — the p.L239R patient — in **a consanguineous family**. The case numbers are adjacent and the consanguinity matches, so cases #49 and #50 are, on the retrievable text, **most plausibly the two p.L239R siblings**. But the gene name in quote (a) is stripped, and **the paper never states in retrievable narrative text that case #50 carries p.L239R**. The registry's `two siblings with homozygous WWOX p.L239R` is therefore **consistent with this paper but not verbatim-verifiable from it on this surface** — the confirming datum would be the per-case row for #50 in **Table 1, which the extractor did not return**.

**An internal inconsistency worth recording (not adjudicated here).** The same p.L239R material is syndromically classified **twice, differently**: quote (b) discusses it inside the **West syndrome** paragraph, quote (c) concludes it is **"consistent with EIDEE"**. Both mention hypsarrhythmia. This may reflect two different siblings (one WS, one EIDEE) described in two places, or one patient labelled inconsistently. **The text does not disambiguate, and the tables that would are unobtainable.**

---

## 2 · 🔴 Question 2 — Movement phenomenology in the p.L239R patient(s)

### The answer is: **NOT REPORTED. Not "reported absent" — simply never addressed.**

**The complete phenotype of the p.L239R patient(s), verbatim, is exhausted by the two Discussion sentences already quoted.** There is no dedicated case vignette for case #49 or #50 anywhere in the body. Every phenotypic word the paper spends on this allele is:

> "…linked to hypsarrhythmic EEG patterns and multifocal seizures consistent with previous reports emphasizing the gene's role in early-onset epilepsy and poor neurodevelopmental outcomes…"

> "…was identified in an infant presenting with hypsarrhythmia and multifocal epileptiform anomalies on a disorganized EEG background, consistent with EIDEE."

**That is the entire phenotype. Two clauses. EEG pattern, seizure type, and a generic prognostic phrase imported from prior literature.**

**Systematic scan of the movement lexicon across the whole retrievable body**, with every hit and its owner:

| Term searched | Present in body? | Attached to the p.L239R patient(s)? |
|---|---|---|
| hypokinesia / bradykinesia | **absent from the entire article** | no |
| rigidity | **absent from the entire article** | no |
| hypertonia | **absent from the entire article** | no |
| hypomimia | **absent** (the phrase *"immobility of the face"* occurs once, in the textbook description of **Marden–Walker syndrome**, unrelated patient) | no |
| oculogyric crisis | **absent from the entire article** | no |
| abnormal posturing | **absent from the entire article** | no |
| parkinsonism / parkinsonian | **absent from the entire article** | no |
| dystonia / dystonic | present **twice**, both for **case #51** (Marden–Walker, VUS, different gene): *"she exhibited microcephaly, abnormal motor development, and dystonic movements"* and *"The patient demonstrated bicycling movements of both feet, consistent with dystonia."* | **no** |
| movement disorder | present **once**, in **Methods**, as an HPO filtering term only: *"additional HPO terms reflecting each patient's individual clinical features (e.g., microcephaly, spasticity, hypotonia, movement disorder, structural brain anomaly, facial dysmorphism) were incorporated"* | **no** |
| hypotonia | present for **case #53** (*"moderate-severe hypotonia"*, NALCN/IHPRF1) and **case #59** (*"the patient exhibited severe hypotonia and feeding difficulties"*, HADDTS) | **no** |

**This is the crux, stated plainly.** The paper **does not report that the p.L239R patient(s) lacked parkinsonian features. It does not report their motor examination at all.** No tone, no posture, no spontaneous movement, no facial expression, no motor exam of any kind is recorded for case #49 or #50 in the retrievable text. The distinction this laboratory has spent two days documenting applies exactly here: **"not reported" ≠ "reported absent"**, and the honest classification of this comparator is the former.

Note further that the Methods show **"movement disorder" was an available HPO term in this study's own prioritisation vocabulary** — so the authors had the concept in hand and did not apply it to this case in any retrievable sentence. That is weak evidence at best (HPO terms were used to filter variants, not to report phenotypes), and is **not** converted here into an argument that the feature was looked for and not found.

---

## 3 · Question 3 — Age, seizure type, EEG, MRI, head circumference, development

| Datum | What the paper says, verbatim | State |
|---|---|---|
| **Age** | *"was identified in an infant"* — no age in months, no age at onset, no age at testing | **minimal** (cohort-level only: *"a median age at genetic testing of 4.69 years (range: 1 month to 17 years)"*) |
| **Seizure type** | *"hypsarrhythmic EEG patterns and multifocal seizures"*; the general claim that missense-variant patients *"still present with very early onset and multiple seizure types, frequently focal and spasms"* — the latter is **about the literature, not about these patients** | reported, thin |
| **EEG** | *"hypsarrhythmia and multifocal epileptiform anomalies on a disorganized EEG background"* | **the single best-reported item** |
| **MRI / neuroimaging** | 🔴 **NOT REPORTED.** No neuroimaging statement of any kind exists for case #49 or #50. (MRI is reported only for unrelated cases: #6 *"thin corpus callosum, and decreased white matter"*; #51 *"a thin corpus callosum, enlarged lateral ventricles, and polymicrogyria"*; #59 *"pachygyria, a thin corpus callosum, and a hypoplastic inferior vermis"*.) | **absent** |
| **Head circumference / microcephaly** | 🔴 **NOT REPORTED.** The words *microcephaly* / *microcephalic* appear **twice in the whole article** — once in the Methods HPO list, once for **case #51** (*"she exhibited microcephaly"*). **Neither instance refers to the p.L239R patient(s). No OFC value, centile, or trajectory appears anywhere in the article.** | **absent** |
| **Developmental status** | Only *"poor neurodevelopmental outcomes"*, and that phrase is explicitly attributed to **prior literature** (*"consistent with previous reports emphasizing the gene's role in… poor neurodevelopmental outcomes"*), **not** to an assessment of these patients. No developmental quotient, milestones, or regression data. | **absent as a measurement** |

### 3.1 · 🔴 The "acquired microcephaly" citation does not survive checking

PMID 42092735 states that p.L239R *"has previously been reported in association with acquired microcephaly and severe epileptic encephalopathy without prominent parkinsonian features"*, and names this paper as that prior report.

**This paper does not say that.** It reports, for the p.L239R patient(s): hypsarrhythmia, multifocal epileptiform anomalies, disorganized EEG background, multifocal seizures, and a literature-derived prognostic phrase. **It makes no statement about head circumference — congenital, acquired or otherwise.** The word *microcephaly* never touches this case.

Both halves of the citing sentence therefore mischaracterise the source in the same direction: **"acquired microcephaly" is not reported here, and "without prominent parkinsonian features" is not reported here either.** The citing authors appear to have converted *absence of report* into *reported phenotype* twice over — once into a positive finding (microcephaly) and once into a negative finding (no parkinsonism). Caveat that keeps this fair: the per-case **Table 1 is unobtainable**, and head circumference and motor findings are exactly the kind of datum a diagnostic-yield cohort puts in a table and not in prose. **What is established is that the narrative does not support the citation; what is not established is that the paper nowhere contains the data.**

---

## 4 · Question 4 — Protein or transcript work on p.L239R

**None. No functional work of any kind was performed in this study, on this allele or on any other.**

The Methods describe DNA extraction, amplicon panel sequencing, WES, alignment to hg19, HPO-driven filtering, ACMG classification, IGV visualisation and trio segregation — and nothing else. No Western blot, no immunoblot, no RT-PCR, no minigene, no expression construct, no cell line, no protein quantification appears anywhere in the article. Pathogenicity is asserted by **in-silico classification and segregation only**:

> "Detected variants were classified as 'pathogenic', 'likely pathogenic', or 'variants of uncertain significance (VUS)' according to the ACMG criteria."

The paper's own posture toward functional data is explicitly aspirational and always deferred to others:

> "Although p.I894S has not been functionally characterized, its location in the Domain II pore-forming region suggests a gain-of-function effect…"

> "Functional analyses are required to determine whether this variant results in a gain- or loss-of-function effect and thereby to clarify its precise pathogenic mechanism."

> "…longitudinal clinical monitoring, together with functional studies, is recommended to clarify pathogenicity…"

**Consequence for LEGEND's outstanding structural prediction.** The discovery-ledger prediction that **L239R yields absent or severely destabilised protein** (L239 buried, relSASA 0.000, ~3.5 Å from the anchors, same core as the reference genotype's Q230P) is **neither tested nor addressed here**. This paper contributes **no** protein-level or transcript-level datum. The prediction remains **untested**, and reading this paper — which the ledger framed as *"now a test of our hypothesis, not just backlog reading"* — **does not test it**. That is a clean negative result about the source, and it should be recorded as such rather than left as an open expectation.

The one mechanistic gesture the paper makes toward missense WWOX alleles is a **clinical**, not biochemical, claim, and it is hedged and uncited to these patients:

> "While most previously reported cases involve truncating or splice-site variants leading to loss of function, emerging evidence indicates that certain missense variants may also lead to a somewhat milder course in terms of overall prognosis…"

---

## 5 · Question 5 — The denominator (secondary; recorded, nothing more)

Cohort and yield, verbatim:

> "A targeted gene panel was performed in a total of 129 patients with DEE. The cohort included 66 males and 63 females, with a median age at genetic testing of 4.69 years (range: 1 month to 17 years)."

> "Pathogenic and likely pathogenic variants were identified in 29 of the 129 patients, resulting in a diagnostic yield of 22.48%."

Per-gene counts, verbatim and unusable as printed:

> "Pathogenic and likely pathogenic variants were detected in(= 8),(= 4),(= 3),(= 2),(= 2),(= 2),(= 2),(= 2),(= 1),(= 1),(= 1),(= 1) genes ()."

**Recorded datum:** the counts sum to 29, consistent with the stated yield, but **every gene symbol is stripped, so WWOX cannot be mapped to a count from the retrievable text.** If cases #49–50 are the WWOX sibling pair (§1, INFERENCE), WWOX would be one of the five `(= 2)` entries, giving **2 WWOX patients / 129 DEE patients ≈ 1.6% of the cohort, ≈ 6.9% of the 29 solved cases** — but both figures rest on the sibling inference **and on a gene-to-count mapping that the extraction does not permit**. They are recorded as **provisional counselling context only**, not as a verified frequency, and no mechanistic weight is placed on them.

---

## 6 · Verdict on the proposition *"p.L239R predicts parkinsonism at the allele level"*

### `NOT SUPPORTED — movement phenomenology simply not reported`

**Reasoning.** This is a diagnostic-yield cohort paper. It reports genes, EEG patterns and syndrome labels; it does not phenotype. For the p.L239R patient(s) it spends **two clauses**, both EEG-centred. It contains **no motor examination, no tone description, no posture, no facial expression, no movement-disorder term, and no neuroimaging or head-circumference datum** for these patients. The words *hypokinesia*, *rigidity*, *hypertonia*, *bradykinesia*, *parkinsonism* and *hypomimia* **do not occur anywhere in the article**.

Therefore the comparator **cannot contradict** the new case report — a paper that never looked cannot report an absence — and it **cannot support** it either. The allele-level prediction is **untested on this surface**.

**Why not `CANNOT DETERMINE ON THIS SURFACE`:** that verdict would be right if the phenotype were merely hidden in an unobtainable table. Here the *narrative itself* is determinate about its own shallowness — the authors' prose on this allele is complete, self-contained and confined to electroclinical findings, and they had an HPO vocabulary containing "movement disorder" that they did not deploy in any retrievable sentence about this case. What remains genuinely undetermined is the **tabular** layer (Table 1 per-case rows for #49–50, which would carry head circumference and possibly examination findings, and which would confirm whether #50 shares the allele). **That residual uncertainty is declared, not resolved**, and it is the single thing that would most improve this comparator: a human-eye reading of Table 1 from the PMC HTML or the publisher PDF.

**The comparator is weak because the phenotyping is shallow — and that is itself the finding.**

---

## 7 · What this does to the new case report's phenotypic-expansion claim

The claimed contrast — *same allele, prior siblings, no parkinsonism* — **is not a contrast the cited source can bear**: PMID 41153369 reports no motor phenomenology and no microcephaly for its p.L239R patients at all, so the new case's "phenotypic expansion" rests not on a documented negative but on an **unexamined prior**, which neither strengthens the expansion claim nor rescues p.L239R as an allele-level predictor — it leaves n=1 standing entirely alone.
