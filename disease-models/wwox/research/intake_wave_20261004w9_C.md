context_policy: SOURCE_FIRST

# Intake wave 9 (2026-10-04), Scientist C: an allele class with a measured consequence, a *trans* regulator, and a blood-accessible readout

**Not medical advice.** Public edition: no individual-level record; patients are described at class
level only. Two of the six sources are **preprints, not peer reviewed**, and nothing in them raises
the status of any claim.

## Question

What does each source add to, or limit in, the claim that WWOX dose can be observed and altered
outside the gene-therapy route — in a measured splice consequence, in a *trans*-acting regulator of
WWOX transcription, and in an accessible human fluid?

## Sources and receipts

| Source | What it is | Receipt | Depth | Verdict |
|---|---|---|---|---|
| PMID 40183601 | 733-family paediatric epilepsy cohort; four WWOX diagnoses; cDNA result | `FTR-20261004-40183601-01` | partial | **INGEST** |
| PMID 42738875 | WWOX protein in L1CAM-captured plasma vesicles | `FTR-20261004-42738875-01` | partial | **INGEST** |
| PMID 42770556 | PRMT1–SFPQ intron retention; Wwox among long genes | `FTR-20261004-42770556-01` | partial | **INGEST** |
| PMID 42771216 | AAV delivery in two human ex vivo substrates | `FTR-20261004-42771216-01` | partial | **OFF-AXIS** (earned null: WWOX zero times) |
| medRxiv `PPR1269651`, doi `10.64898/2026.01.16.26344264` | optical genome mapping in 57 trios; one WWOX case | `FTR-20261004-PPR1269651-01` | partial | **INGEST** (preprint; never promoted) |
| Research Square `PPR1316475`, doi `10.21203/rs.3.rs-9950101/v1` | FASD GWAS; a parent-side WWOX haplotype | `FTR-20261004-PPR1316475-01` | partial | **INGEST** (preprint; never promoted) |

All six are PARTIAL: figures were read by legend except where a panel bore on a carried number,
supplements were read where they existed and were reachable, and introductions were skipped.

## The answer to the question, with its limits

1. **A measured splice consequence exists, and it is not where the selection put it.** The allele
   `NM_016373.4:c.107+119C>G` appears in both a preprint (in trans with a 51 kb exon-6 deletion,
   RT-PCR asserted but never shown) and a **peer-reviewed cohort** (homozygous, cDNA analysis
   showing inclusion of intron 1 and a premature stop). The measurement is in the cohort paper the
   selection listed as a **weak sixth item on two body hits**. What remains unmeasured in both is
   the decisive quantity: the aberrant **read fraction**, plus frame confirmation, NMD, protein,
   tissue. A deep intronic cryptic-donor allele is a new class for the model and transfers to no
   other allele.
2. **A *trans* regulator is plausible and weak.** PRMT1–SFPQ loss raises intron retention of Wwox
   in mouse neural crest, but the figure stars the **retention** change and not the **abundance**
   change for Wwox; the retained fraction moves from about 0.8 % to about 1.2–1.4 %; no
   Wwox-specific experiment exists; and the sentence linking this to human WWOX encephalopathy
   cites a pan-cancer paper with **zero** WWOX content. Read backwards it is a candidate lever;
   read honestly it is a long-gene effect that includes Wwox.
3. **A blood-accessible WWOX protein readout exists and is not an endpoint.** WWOX protein is
   measurable in L1CAM-captured plasma vesicles (Tier 1 by kind under §13), but as a **relative**
   NPX unit, in **singlet**, cross-sectionally, in a cohort with no WWOX genotype, with **one**
   marked comparison — and the paper's sex sentence is not the comparison its figure marks. The
   five-item specification for turning it into a pharmacodynamic endpoint is in
   `CC-20261004W9-C-EV-BIOMARKER-01`; the gating item is the detection **floor** in a genotype
   where WWOX protein is expected to be low or absent.
4. **The FASD preprint does not reach the dose question.** A parent-side intronic haplotype
   associated with a diagnosis outcome (risk ratio 4.07, adjusted p = 0.0002, frequency 0.117), only
   after imputation, with the defining markers absent from the second cohort, and an expression
   analysis keyed to **exposure** rather than genotype. It also contradicts itself: its table
   reports WWOX expression **decreased** and its discussion says **increased**.
5. **The delivery-substrate paper is an earned null for WWOX** and yields method discipline only:
   two human ex vivo substrates were never compared at a matched dose, some specimens showed no
   transduction at all, self-complementary cassettes flatter early endpoints, and a day-5 ranking
   inverted by day 14.

## What would change the model, and what would falsify these readings

| Statement | Would change the model if | Falsified by |
|---|---|---|
| Deep intronic cryptic-donor alleles are a real WWOX class with transcript-level loss | a quantified read fraction showed the aberrant species dominant, in a stated tissue | a quantification showing it is a minor by-product with preserved normal protein |
| SFPQ-dependent intron retention modulates WWOX dose | an SFPQ- or PRMT1-raising perturbation raised WWOX protein in neurons | the effect being fully explained by gene length, with no SFPQ binding in WWOX introns |
| Vesicle WWOX could become a pharmacodynamic endpoint | an absolute assay detected WWOX in people with biallelic WWOX alleles and tracked a dose change | vesicle WWOX shown unrelated to brain WWOX, or below the floor in that genotype |

## What the brief and the selection got wrong

1. **PMID 40183601 was mis-scoped.** Called a "weak sixth" whose "two hits may be a gene-list
   mention and nothing more"; it in fact carries four WWOX diagnoses and the wave's only measured
   RNA consequence. The body-hit count is a poor proxy when the data live in a supplement.
2. **The preprint's "measured RNA consequence" is one unillustrated sentence.** The selection
   credited the preprint with the measurement; the measurement with a method attached is in the
   peer-reviewed cohort.
3. **The preprint contradicts itself** on the second allele: Results call it a substitution with an
   HGVS string, the Discussion calls it "an InDel"; Results say "reanalysis of the genome data",
   the Discussion says "a newly generated short-read genome" while the supplement lists a short-read
   genome among the prior tests.
4. **The FASD preprint's WWOX haplotype is parent-side**, not the child's; the child-side hit was a
   different gene. The selection's phrasing ("a WWOX haplotype associated with FASD diagnosis risk")
   is true only with that qualifier.
5. **Wave 7's decline of the medRxiv preprint is not recorded anywhere in this repository** — zero
   hits for its DOI or PPR id. The only source for that decline is the wave-9 selection note.

## Patient-count check

The two `c.107+119C>G` cases are **distinct** (homozygous in the cohort; in trans with a large
deletion in the preprint). No held source carries that allele at all. The exon-6 deletion records
the model already holds differ in allele pair and, where printed, in size; exon-6 deletions recur
independently at the FRA16D fragile site, so a shared exon is not evidence of a shared family.
**No overlap found; each case counted once.**

## Candidates

| Id | Class | Subject |
|---|---|---|
| `CC-20261004W9-C-DEEPINTRONIC-01` | MINOR | the deep intronic allele class, measured vs asserted, and what is not measured |
| `CC-20261004W9-C-EV-BIOMARKER-01` | MINOR | vesicle WWOX under §13, with the five-item endpoint specification |
| `CC-20261004W9-C-TRANS-REGULATOR-01` | MINOR | PRMT1–SFPQ and Wwox, with the unsupported citation |
| `CC-20261004W9-C-REGISTRY-01` | MINOR | identity landings for all six sources (numbers provisional) |

## Acquisition notes for the next wave

- Europe PMC `bin/` returned **HTTP 403** for both figure and supplement files on two records;
  `pmc-oa-opendata.s3.amazonaws.com/<PMCID>.1/<file>` served them, and the medRxiv
  `supplementary-material` page served the preprint's two supplements.
- The Research Square PDF endpoint served a 35-page full text where the PMC record carries only an
  abstract — the route wave 7 recorded as blocked.
- Europe PMC `fullTextXML` on a PPR id returned a full JATS body for the medRxiv preprint (142 879 B).

## STOP_LOG

One model safety classifier halt: the write of the dossier for PMID 42770556 was stopped mid-file.
Per the brief the passage was not reworded and retried; the reading is carried by the deep-dive
manifest (PASS, strict, nine locators including a panel reading) and by
`CC-20261004W9-C-TRANS-REGULATOR-01`, and the receipt records that no dossier exists for that PMID.
No other halt occurred.
