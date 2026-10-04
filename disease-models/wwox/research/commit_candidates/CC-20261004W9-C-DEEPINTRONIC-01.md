# CC-20261004W9-C-DEEPINTRONIC-01 — a deep intronic WWOX allele with a measured RNA consequence, reported twice and read here for the first time

`context_policy: SOURCE_FIRST`. **Author:** ACTOR_ID `scientist`, Scientist C of intake wave 9,
2026-10-04. **Change class: MINOR** (new research-line record; narrows no `consolidated baseline`
claim). **Nothing here is medical advice.** Public edition: class level only.

Sources: PMID 40183601 (`FTR-20261004-40183601-01`, manifest PASS) and medRxiv preprint
doi `10.64898/2026.01.16.26344264` (`FTR-20261004-PPR1269651-01`) — **the preprint is not peer
reviewed and raises nothing**.

## 1 · Finding

`NM_016373.4:c.107+119C>G` — a deep intronic variant in WWOX intron 1 — now appears in two
independent sources, and **one of them measured its RNA consequence**:

| Source | Zygosity | Consequence | How established |
|---|---|---|---|
| PMID 40183601 (peer-reviewed cohort, 733 families) | **homozygous**, both parents carriers | **inclusion of intron 1 in NM_016373, premature stop codon** | cDNA analysis (tissue not stated) |
| medRxiv preprint (not peer reviewed) | in trans with a 51 kb deletion affecting exon 6 | "alternative splicing effect … confirmed using RT-PCR"; the donor gain is a prediction | RT-PCR asserted, **no data shown anywhere in the preprint or its two supplements** |

This is an allele class the model does not hold: **deep intronic, cryptic-donor gain, with a
measured transcript consequence**. The allele is **absent from the held ClinVar snapshot**
(`WWOX_clinvar_all_variants.csv`), so it is not reachable from that surface.

## 2 · What is measured and what is not

- **Measured:** that an aberrant transcript exists which retains intron 1 and terminates early
  (one source, cDNA).
- **Not measured in either source:** read fraction (aberrant vs normal), residual normal splicing,
  NMD, protein, the exact cryptic donor position, allele-specificity of the aberrant product, any
  minigene, any quantification. Tissue is stated in neither.
- The question that decides whether the allele is a null or a leaky hypomorph — **what fraction of
  WWOX transcript survives** — is therefore unanswered.

## 3 · Patient-count check (class level, as printed)

The two sources describe **different genotypes**: homozygous in the cohort record; in trans with a
large exon-6 deletion in the preprint. Sex, country of reporting centre and course as printed also
differ. **Two distinct cases; no overlap found.** Counted once each.

## 4 · Transfer limits

A cryptic-donor gain deep in intron 1 is not an acceptor allele, not a canonical ±1/±2 allele, not a
missense; no datum here transfers to any other WWOX allele class. n = 1 per source. The preprint
never raises a claim's status.

## 5 · Ops (provisional)

### 5.1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record after the current final research-line record) |
| record | `RL-C-20261004w9c1 — Deep intronic WWOX c.107+119C>G: an allele class with a measured RNA consequence (intron-1 inclusion, premature stop) in one peer-reviewed cohort and an unshown RT-PCR in one preprint; read fraction, NMD and protein unmeasured` |
| status | `open` |
| tag | `DATO` for the two source statements, `INFERENZA` for the class reading |
| body | §1–§4 of this candidate verbatim |
| class | MINOR |

### 5.2 · `disease-models/wwox/research/full_text_queue_current.md`

| field | value |
|---|---|
| op | `append` (new FT record, next free number measured at integration; FT-177 is the highest seen on 2026-10-04) |
| body | `Deep intronic WWOX alleles: the open question is the aberrant read fraction. Asking the reporting groups for the cDNA trace, or an RNA-seq/minigene replication, is the only route — neither source shows the experiment.` |
| class | MINOR |

## 6 · What would change this

- **Would strengthen:** a quantified RT-PCR or RNA-seq read fraction for the allele, in a stated
  tissue, with and without NMD inhibition.
- **Would falsify the class reading:** a demonstration that the aberrant species is a minor
  by-product and normal WWOX protein is preserved — which would make the allele hypomorphic rather
  than null and would break the biallelic-loss assumption used to call these cases solved.

## 7 · Brief premises tested

- The wave-9 selection called the preprint "a new allele class … with a measured RNA consequence".
  **Half right:** the class is new to the model, but the measurement the selection credits to the
  preprint is a single unillustrated sentence. The actual measurement is in a **peer-reviewed
  cohort the same selection listed as a weak sixth item on two body hits** (PMID 40183601).
- The selection's description of PMID 40183601 ("two hits may be a gene-list mention and nothing
  more") was **wrong**: the paper carries four WWOX diagnoses and the cDNA result.

### LOCATOR TRIPLES FOR BLIND AUDIT

Format: `(proposition | verbatim quote | anchor)`. Each artefact is on disk; quotes from the
cohort paper were verified by the manifest validator.

- [PMID 40183601, artefact `files/fulltext/PMID40183601_Henry2025_PMC.xml`] (A homozygous deep intronic WWOX variant was shown by cDNA analysis to cause inclusion of the first intron and a premature stop codon. | A homozygous WWOX c.107 + 119C>G variant was shown to lead to the inclusion of the first intron in transcript NM_016373 , leading to a premature stop codon after cDNA analysis. | Results, deep intronic variants paragraph)
- [PMID 40183601, artefact `files/fulltext/PMID40183601_Henry2025_supp_tableS9.txt`] (The same allele appears in the cohort's solved-cases table as a homozygous genotype with both parents as carriers. | Hom	WWOX	c.107+119C>G	NM_016373	Maternal, Paternal | Supplementary solved-cases table, WWOX row)
- [PMID 40183601, artefact `files/fulltext/PMID40183601_Henry2025_PMC.xml`] (WWOX accounts for four of the fifty-one solved infantile epileptic spasms cases in this cohort. | Infantile epileptic spasms syndrome 51/132 (38.6%) STXBP1 (6), CDKL5 (4), WWOX (4) | Table 1)
- [preprint doi 10.64898/2026.01.16.26344264, artefact `files/fulltext/PPR1269651_vanderSanden2026_medRxiv.xml`] (The preprint states the splicing effect was confirmed by RT-PCR, with no data, method or tissue given. | The alternative splicing effect of the variant was later confirmed using RT-PCR. | Results, WWOX section)
- [preprint doi 10.64898/2026.01.16.26344264, artefact `files/fulltext/PPR1269651_vanderSanden2026_medRxiv.xml`] (In the preprint the donor-strengthening effect is a prediction, not a measurement. | predicted to strengthen a cryptic splice donor site | Results, WWOX section)
