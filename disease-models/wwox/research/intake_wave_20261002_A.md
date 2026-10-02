# Intake wave 2026-10-02 — Scientist A: six sources on allele class × zygosity × phenotype, heterozygous carriers and gene dose

**Actor:** ACTOR_ID `scientist` (Scientist A), dispatched by the Orchestrator · **Branch:** `task/sci-A-20261002`
**context_policy:** `SOURCE_FIRST` for each of the six readings. The first pass of every paper (§ 2) was written before any LEGEND claim, ledger lead, triage note or registry prose about that paper or its alleles was opened. The comparison (§ 3–§ 4) came after. `CLAIM 030`, `CLAIM 032`, `CLAIM 033` and `analysis/ft116_cohort_triage_20260921.md` were read only once all six first passes existed.

🔴 **Not medical advice.** Class-level reasoning over published genotypes; no individual-level record, no sample identifier, no parent of origin and no geography is carried.

**Question assigned:** *What does each source add to — or limit in — the allele-class × zygosity × phenotype picture of the WWOX genotype class, and in particular what does it say about heterozygous carriers and about gene dose in either direction?*

---

## 1 · Verdicts

| PMID | Verdict | Depth (receipt prepared) | WWOX content in one line |
|---|---|---|---|
| 30746283 | **INGEST** | complete · `FTR-20261002-30746283-01` | homozygous canonical splice donor (one child) and homozygous nonsense (two sibs); three carriers described as *«healthy»*; a review table that mis-transcribes Q230P |
| 37095367 | **INGEST** (low weight) | complete · `FTR-20261002-37095367-01` | one missense + splice-donor case, labelled compound heterozygous with no phase; **not a corrigendum** |
| 29390993 | **INGEST** | complete · `FTR-20261002-29390993-01` | last-exon nonsense + **intragenic exon 6–8 duplication**, phase by parents; infantile-spasm group; parents asymptomatic by inclusion criterion |
| 24949445 | **OFF-AXIS for dose — recorded as a rejection** | complete · `FTR-20261002-24949445-01` | the *«WWOX and MAF»* duplication contains only WWOX exon 9: **not a dose-gain datum** |
| 40191585 | **INGEST** (population genetics) | partial · `FTR-20261002-40191585-01` | **`p.E17K` is WWOX `c.49G>A`** (read); founder haplotype; 172 UKBB missense carriers with **no phenotype** |
| 32081867 | **INGEST** (bounded) | partial · `FTR-20261002-32081867-01` | ASD-case deletion intronic for canonical WWOX; one **control** with an exon 6–8(-ish) deletion |

Receipt files (pending, not appended): `scratchpad/receipts_pending/sciA_<pmid>_1.json` for the six PMIDs above.

## 2 · First pass, per source (written before comparison)

### 2.1 PMID 30746283 — two families, WES + Sanger
Family 1: one child, **homozygous** `c.409+1G>T` (canonical donor, intron 4; genomic position matches Ensembl's exon-4 end at 78,149,051). DEE band: focal seizures at two months, then spasms, refractory. **Both parents and an unaffected sib are heterozygous**, described as *«healthy»*, with no examination reported. No RNA test: the consequence is *«might cause»*. Family 2: two sibs **homozygous** `p.Arg54*` (allele first reported elsewhere); severe DEE with burst suppression and hypsarrhythmia; no parental testing. Discussion: *«one functional copy … is sufficient»* — an inference from zygosity. Table 1 prints the 2018 Q230P report as `p.Gly230Pro` with reversed arrows, and lists a compound heterozygote beside the Discussion's *«All … homozygous»*.

### 2.2 PMID 37095367 — WGS, 20 children
One WWOX case: `p.Ser304Tyr` + `c.230+1G>T`, *«AR, compound heterozygous»*, phase not shown, no parental genotypes, ACMG on a commercial platform (per-variant class not printed). Early focal epilepsy, psychomotor delay, spastic ataxia; an affected sib died in infancy, not genotyped. The pedigree arrow marks a sib drawn unaffected. PubMed type: Journal Article; the linked erratum is an author-surname correction.

### 2.3 PMID 29390993 — 172-gene panel, 74 children
One WWOX patient: `p.Gln354Ter` (PVS1 Pathogenic) in trans with an **exon 6–8 duplication** (Likely pathogenic, **no PVS1**), each allele inherited from a different parent; Figure 2 a-2 depth plot inspected. Phenotype: infantile-spasm group (Table S4), inside a cohort defined by drug-resistant early-onset epilepsy. Both parents asymptomatic **by inclusion criterion**.

### 2.4 PMID 24949445 — seven heterogeneous cases
One child with a 16q23.1 duplication (NCBI36 77,445,915–78,190,209; 0.744–0.827 Mb), inheritance unknown (no paternal DNA), a language-dominant neurodevelopmental disorder with declining nonverbal IQ and epilepsy whose EEG normalised on valproate. Authors: the duplication *«affects two dose-sensitive genes: WWOX … and MAF»*.

### 2.5 PMID 40191585 — FoundHaplo
`p.E17K` = **WWOX `c.49G>A`**, `p.Cys121Trp` = SCN1B `c.363C>G` (Methods; italics lost in PubMed). 172 UKBB carriers (WES), 0 of 1,573 in an epilepsy cohort, 157 kb core haplotype shared by all 175 carriers examined. Disease haplotypes from three affected-child/parent duos; the children's second allele is not stated. Pathogenicity inherited by citation. **No carrier phenotype.**

### 2.6 PMID 32081867 — PsychArray, 128 ASD families, 365 controls
ASD case: heterozygous loss chr16:78,302,399–78,361,149 (hg19), described as involving *«the last exon of the two shorter gene transcript variants»*; high-functioning PDD-NOS, normal IQ, EEG and MRI; not qPCR-validated. A control without psychiatric history: heterozygous loss chr16:78,386,295–78,466,632. The authors' *«weak risk factors»* sentence rests on the case plus a citation.

## 3 · Computations made after the first pass (reader's, `PREMISE: INFERENZA`, all from free public references)

| Computation | Route and digest | Result |
|---|---|---|
| WWOX canonical exons, GRCh37 | Ensembl REST `lookup/symbol/homo_sapiens/WWOX?expand=1`, sha256 `62e1eb90624465ad6697f7f82e2414d010e8621b3d0f0cc5ad9e18c31a9e6f97` | ENST00000566780: exon 5 ends 78,198,186; exon 6 78,420,757–845; exon 7 78,458,767–952; exon 8 78,466,385–649; exon 9 79,245,505–79,246,564 |
| Paper-4 duplication, NCBI36 → GRCh37 | Ensembl REST `map/human/NCBI36/16:77445915..78190209:1/GRCh37`, sha256 `d18cc68b7f461b8966569153ad1ceee8a750552684e609c328bd6d2854246bcb` | 78,888,414–79,632,708 → **WWOX exon 9 only** (+ most of MAF, 79,619,740–79,634,611) |
| Paper-6 case deletion | hg19 coordinates against the exon map | **inside canonical intron 5** |
| Paper-6 control deletion | same | **exons 6, 7 and most of 8** (call ends 17 bp short of exon-8 end) |
| Paper-3 duplication frame | exon lengths 89 + 186 + 265 = 540 nt | a direct tandem copy of exons 6–8 would be **in frame** |
| Paper-3 nonsense position | LEGEND boundary map: exon 9 begins at c.1057 | codon 354 lies in the last exon: NMD escape expected |
| Paper-5 epilepsy-cohort expectation | 172 / 468,481 × 1,573 | ≈ 0.6 expected carriers: the observed 0 is uninformative |
| Paper-5 founder citation | held PDF text layer of PMID 30853297; positive control `517-2` ×11 | `c.49`, `49G`, `Glu17`, `E17K` each ×0: the citation does not support the founder attribution |

## 4 · Comparison with what LEGEND already holds (counted once)

- **`p.Glu17Lys` — three sources, likely one cluster of patients, one ancestral allele.** The held WWOX-DEE cohort (PAPER 018, PMID 36779245) lists two `p.Glu17Lys` carriers, each with the missense in trans with a deletion. It recruits at the same centre, under the same ethics committee, as FoundHaplo's three duos, so two of those duos are likely those two children (INFERENZA). The same held cohort states that two of its patients were *«briefly reported»* in its references 29–30; its reference 29 is PMID 31618474 (Burgess 2019). That cohort's `p.Glu17Lys` + intron-4-deletion patient is tabulated with EIMFS, which matches the Burgess patient whom `ft116_cohort_triage_20260921.md` § 5.2 assigned to WWOX by elimination only. **The Burgess patient's WWOX attribution is therefore supported by a read source in LEGEND's own corpus, and that patient is not a new patient** (INFERENZA from the held cohort's own statement plus genotype match; not adjudicated here because it touches a peer's triage note). The `p.Glu17Lys` carrier of PMID 30356099 (PAPER 117) remains a separate report. FoundHaplo's founder haplotype explains why the allele *«recurs»* across these reports: it is one ancestral allele, not repeated mutation. The allele stays **UNASSIGNABLE** for pathogenicity (ClinVar: conflicting): nothing in this wave measures its function.
- **Exon 6–8 rearrangements.** LEGEND holds the exon 6–8 **deletion** as the most frequent pathogenic CNV (`ft116` § 6.2). This wave adds an exon 6–8 **duplication** in an affected child (PMID 29390993, possibly in frame) and an exon 6–8(-ish) **deletion** in a psychiatrically unaffected control (PMID 32081867). Neither is a dose datum in the gain direction.
- **Q230P mis-transcription.** PMID 30746283's review table names the 2018 Q230P allele `p.Gly230Pro`; the held primary (PAPER 041) is the authority. Genotype caution: secondary tables are not sources for alleles.
- **No overlap found** for the Ehaideb families, the Bayanova case or the Rim patient; none is excluded either. All three are counted as reports, not as confirmed-new individuals.

## 5 · Answer to the assigned question, with its limits

| Source | Allele class | Zygosity | Phenotype band | Call | Segregation / function | Named per patient? | Pathogenicity call |
|---|---|---|---|---|---|---|---|
| 30746283 fam 1 | canonical splice donor | homozygous | DEE (spasms, refractory) | WES + Sanger | carriers: both parents + sib; **no RNA** | yes | own |
| 30746283 fam 2 | nonsense | homozygous | severe DEE | WES | none reported | yes | inherited (first report) |
| 37095367 | missense + splice donor | compound het (asserted, phase unshown) | early focal epilepsy, delay, spastic ataxia | WGS | none | yes | own (commercial ACMG) |
| 29390993 | last-exon nonsense + intragenic exon 6–8 **duplication** | compound het (parental testing) | infantile-spasm group | panel + MLPA | parents tested; **no function** | yes | own |
| 24949445 | 3′-partial duplication (exon 9 + MAF) | heterozygous | NDD with epilepsy (not DEE) | array CGH | none | yes | own, **refuted as a dose datum by its own coordinates** |
| 40191585 | missense `p.Glu17Lys` | carriers (copy number unknown) | **none reported** | WES + IBD | founder haplotype | listed, not per carrier | inherited by citation |
| 32081867 case | intronic deletion (canonical) | heterozygous | high-functioning ASD | array | not qPCR-validated | yes | own (*«weak risk»*) |
| 32081867 control | exon 6–8(-ish) deletion | heterozygous | *«without psychiatric history»* | array | not validated, not examined | coordinates only | n/a |

**Heterozygous carriers.** Four new carrier observations: two null-class carrier sets in families (asserted *«healthy»*; asymptomatic by enrolment criterion), one exon-level deletion in an unexamined control, and 172 missense carriers with no phenotype. **None is a demonstrated negative for haploinsufficiency** (`CLAIM 032`, `PREMISE: NOBODY_LOOKED`). The largest set is missense and therefore outside the haploinsufficiency question altogether (`CLAIM 032`/`033` `DO_NOT_INFER`).

**Gene dose, gain direction.** The model still holds **no WWOX dose-gain datum**: the one candidate (PMID 24949445) does not contain the gene, and the intragenic duplication (PMID 29390993) is an allele of uncertain class, not added dose.

**Gene dose, loss direction.** One exon-level heterozygous deletion in a control without psychiatric history (PMID 32081867), unvalidated and neurologically unassessed: a single, weak observation consistent with `CLAIM 032`, never a negative.

**What the sources license against the three claims:**
- **`CLAIM 032`** — nothing new is licensed beyond *«carriers exist and were not examined»*. Candidate `CC-20261002-HETEROZYGOTE-CARRIERS-01` appends that, with each source's limit. The authors' *«one functional copy is sufficient»* (PMID 30746283) is not evidence.
- **`CLAIM 032` `DO_NOT_INFER` / `CLAIM 033` reservation (1)** — honoured: the `p.Glu17Lys` carriers are missense heterozygotes and are not chained to the null/wild-type question; a CNV deletion (PMID 32081867) is not a missense and is not used for `CLAIM 033`.
- **`CLAIM 033`** — no change. Two new compound-heterozygous genotypes are each null-class plus an allele of uncertain class (a missense with no function data; a possibly in-frame duplication). They are reports, without outcome data, and cannot enter a survival comparison.
- **`CLAIM 030`** — no change: no abundance or function measurement in any of the six.
- **`ft116`** — its *«not one new missense allele»* stands for its eight papers. This wave adds one new missense allele (`p.Ser304Tyr`, function unknown, genotype unphased), so the 19-allele missense enumeration would become 20 **only** after this case's phase is established. That is recorded here, not applied.

**What would change the model if true, and what would falsify it.** If carrier phenotyping (UKBB `p.Glu17Lys`, or exon-level deletion carriers) showed a neurological or EEG signal, `CLAIM 032`'s *«a copy preserves some endpoints»* would narrow. A null-class carrier series examined and found normal on EEG and cognition would be the first real negative. A whole-gene WWOX duplication with a phenotype would be the first dose-gain datum. RNA from either splice-donor allele, or from the exon 6–8 duplication, would move those alleles out of *uncertain class*.

## 6 · What the brief got wrong, or framed too strongly
1. **PMID 24949445 is not a dose datum.** The abstract's *«microduplication affecting WWOX and MAF»* is true only of WWOX exon 9.
2. **PMID 40191585 is not the most consequential paper for haploinsufficiency.** It settles the gene (`p.E17K` is WWOX) and the founder origin, but its carriers are missense heterozygotes with no phenotype.
3. **PMID 32081867's case deletion is not a heterozygous WWOX loss of the canonical gene.** The paper's own wording names only the shorter transcripts.
4. The queue's corrigendum typing of PMID 37095367 is confirmed wrong (as `ft116` § 2.2 said).

## 7 · Reading debt named, not paid
- PMID 25411445 (Mignot 2015) is still held at stub depth: cited by PMID 30746283's review table and already named in `CLAIM 030`'s revival trigger.
- PMID 28721938, 26345274, 25716914 and 17470496 (case series cited by PMID 30746283's table) are mention-only in the registries.
- PMID 27569545 (Leppa 2016), the sole support for PMID 32081867's *«weak risk»* sentence, is mention-only.
- PMID 31618474 Supplementary Table 2 is still unacquired; § 4's identification makes it a confirmation, not a dependency.
- PMID 40191585's supplement Notes 1–2 and Figures S1–S11, and PMID 32081867's Table S3 rows and Figure S1, are unread (both receipts are `partial`).

## 8 · Artefacts (shared checkout `files/fulltext/`, gitignored)
| Artefact | sha256 |
|---|---|
| `PMID30746283_Ehaideb2018_PMC.xml` | `bfa69a29938b61847beb6e08e56534ec9b4bd5cc9c3b94222f95e85c3e4375f0` |
| `PMID37095367_Bayanova2023_PMC.xml` | `c92f0ee3b3f54a5b4e525e8a67766fd076f74646c84eca8870d9baec5f3396d7` |
| `PMID29390993_Rim2018_PMC.xml` | `63ddf492152993063dbf79dbefcd7275380d5516b0c39debf35496cd37c65687` |
| `PMID24949445_Szymanska2014_PMC.xml` | `728096ca8f49a18bddcad30fe8f0c004bfd2cbf1a9497c8481240b913ffe476d` |
| `PMID40191585_Robertson2025_PMC.xml` | `f1b4cb31a4898024a1fe9bc0420f53150952074c20d2a8e41a8b44ba617e4691` |
| `PMID32081867_Bacchelli2020_PMC.xml` | `dad25ab0ab9a16481cc4a41852978ba30cf2c582c6314f526975e21d9ee619bc` |
| `PMID30746283_assets/PMID30746283_PMC6368664_supplementaryFiles.zip` | `e2e49262bf72c768c1bfaeb067e597e48fc20c204133a3d0ddd6529a06733be0` |
| `PMID37095367_assets/PMID37095367_PMC10293429_supplementaryFiles.zip` | `f59fc9bc8ab9e3cfd241308a3e98bc837f476144a26b06ac2804b7bac9c90bf7` |
| `PMID29390993_assets/PMID29390993_PMC5796507_supplementaryFiles.zip` | `47058d51c806fb03152f544f593c7254c18bbfad5cdca6a6063d6af33c229e75` |
| `PMID40191585_assets/PMID40191585_PMC11970371_supplementaryFiles.zip` | `8e05ef69e16e351e963108edf4ba4f5bb8bb9f18e86dca6387cf7d0eece8204f` |
| `PMID32081867_assets/PMID32081867_PMC7035424_supplementaryFiles.zip` | `afc0d9565eb324177adc23214ad1c2c6a86524728634105d15ada9eff179cbc9` |

Routes: XML by NCBI E-utilities `efetch db=pmc id=<PMCID number>&retmode=xml`; archives by Europe PMC REST `<PMCID>/supplementaryFiles` (no User-Agent, 2026-10-02). PMID 24949445 has no supplementary archive (Europe PMC returns an empty bean). Derived surfaces and their extractors are declared in each manifest.

## 9 · Candidates
- `CC-20261002-HETEROZYGOTE-CARRIERS-01` — `CLAIM 032` qualification (MINOR).
- `CC-20261002-DOSE-GAIN-DISMISSAL-01` — `DIS-022`…`DIS-025` (MINOR; numbers provisional).
- `CC-20261002-INTAKE-A-REGISTRY-01` — `PAPER 119`–`124`, `LIT-0421`–`0425`, `CORPUS P253` / `LIT-0253` promotion (MINOR; numbers provisional).
