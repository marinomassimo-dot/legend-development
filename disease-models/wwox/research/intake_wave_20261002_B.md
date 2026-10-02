context_policy: SOURCE_FIRST

# Intake wave 2026-10-02 — Scientist B

**Actor:** scientist-b (ACTOR_ID `scientist`), dispatched by the Orchestrator under the scientist brief of
2026-10-02. **Branch:** `task/sci-B-20261002`. **Not medical advice.**

**Question assigned:** *What non-lineage evidence do these five give about WWOX in brain development, white matter and
epilepsy — and how much of it survives scrutiny?*

| PMID | Paper | Verdict | Depth | Dossier |
|---|---|---|---|---|
| 37501399 | Yang 2023, marmoset WGS and epilepsy loci | INGEST — earned near-null | complete | `fulltext_dossiers/PMID37501399.md` |
| 28763065 | Xia 2017, infant brain-volume GWAS | INGEST — bounded | partial (supplement appendices by label) | `fulltext_dossiers/PMID28763065.md` |
| 41378749 | Mondragon-Estrada 2025, spina bifida GWAS | INGEST — earned null | complete | `fulltext_dossiers/PMID41378749.md` |
| 25537520 | Chang 2014, review | INGEST as provenance map | partial (figure images unobtainable) | `fulltext_dossiers/PMID25537520.md` |
| 31315632 | Chou 2019, p53/TIAF1/WWOX triad | INGEST — earned null for the brain | complete | `fulltext_dossiers/PMID31315632.md` |

Prepared receipts (not appended at preparation time): `sciB_37501399_1.json`, `sciB_28763065_1.json`,
`sciB_41378749_1.json`, `sciB_25537520_1.json`, `sciB_31315632_1.json`. Each trial-recorded cleanly into a scratch
copy of the ledger.

## Exposure declared

`registry_records.py get --pmid` was run for identity and dedup only. For PMID 28763065 and PMID 41378749 that
surfaced `FT-142`, whose text says *"Neither paper is a WWOX paper"* — a prior conclusion, read before the papers.
Disclosed here; the first pass below contradicts it, which is some evidence it did not steer the reading.

## 1 · First pass (written before any claim, ledger lead or working-model text was opened)

**Marmoset (PMID 37501399).** Species *Callithrix jacchus*; unit: animals in two extended pedigrees, controls
include unaffected siblings. The WWOX signal is **SNP-only**: 17 intronic SNPs on one haplotype in the last intron
of the marmoset WWOX model transcript (about 31 kb), LAMP likelihood-ratio P 2.4e-6 to 9.2e-6 against a suggestive
threshold of 1e-5 ("LOD" in Table 1 is −log10 P). Carriers, control/case: colony 1 1/11 vs 9/9; colony 2 3/6 vs 5/5.
Called by GATK on 17x+ WGS from fingernail DNA, phased by WhatsHap, genotypes Sanger-confirmed. **No WWOX
copy-number event** in the CNV tables; the case-enriched deletion is **KCTD18-like** (Fisher P 0.012, not
significant after correction, per the authors). λ = 0.825 and the Q–Q tail does not exceed the null. Chimerism:
blood heterozygosity higher, so blood excluded and an allele-balance filter applied; the authors say it cannot be
quantified. With n = 31 related animals, "associated" means a suggestive pedigree co-segregation that identity by
descent from an affected founder pair can produce on its own.

**Infant GWAS (PMID 28763065).** Human, 561 infants, MRI at about 5 weeks; rs10514437 (WWOX intron, genotyped,
MAF 0.03) with ICV-adjusted white-matter volume, P 1.56e-8 against the study threshold 1.25e-8; −3.76% WM per copy
of the **common** allele, i.e. the minor allele goes with **more** white matter; variance explained 4.14%;
permutation P 8e-8; consistent across ancestry and sensitivity subsets. **No replication** (not available in PNC or
ENIGMA2). No eQTL or functional link reported.

**Spina bifida GWAS (PMID 41378749).** Human, Bangladesh, 89 cases / 97 controls in the models; three imputed
(R² 0.78) SNPs in WWOX **intron 8** — "coding region" in the abstract means gene body; OR about 6.2, p 2.2e-6,
suggestive threshold 1e-5 only; abstract pairs the wrong rsID with the lead statistics; **not reproduced** by the
technical replication. Authors: "hypothesis-generating".

**Review (PMID 25537520).** 18 of 54 references from the authors' laboratory. Epilepsy and development sentences
rest on three independent primaries (Mallaret 2014, Abdel-Salam 2014, Suzuki 2009). Tau-inhibitor, TIAF1
("unpublished") and in-vivo transcription-factor statements rest on the laboratory itself, and the Conclusion
contradicts the body on in-vivo evidence. Nothing on myelin or white matter.

**Triad (PMID 31315632).** The brain statement rests on **one xenograft experiment** in Wwox-intact nude mice, one
lane per condition, non-reducing blots in which the housekeeping α-tubulin also "aggregates"; mechanism unknown by
the authors' statement; 26 of 56 references and all six behind the brain-aggregation background sentence are the
same laboratory; `WWOX AND TIAF1 NOT Chang NS[au]` = 0 on PubMed. SDR-vs-WW binding contradicts itself inside the
paper.

`FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON.` Admitted: `CLAIM 003`, `CLAIM 006`,
`CLAIM 016`, `CLAIM 030`, `CLAIM 035`, `CLAIM 037`, `DL-MECH-107`, `DL-BIO-004`, `FT-100`, `PAPER 056`,
`CORPUS P263`, `LIT-0263`, and the theme headings for myelin, white matter, epilepsy, GWAS, TIAF1, marmoset, spina
bifida, neural tube, Alzheimer, neurodegeneration and aggregation (all by `registry_records.py`).

## 2 · Comparison with the registries — add, bound, or leave untouched

| Source | `CLAIM 003` (neuronal WWOX loss → hypomyelination, consolidated) | `CLAIM 037` (seizure phenotypes in rodent models) | `CLAIM 006` (P47T astrogliosis) | `CLAIM 030` (severity tracks residual function) |
|---|---|---|---|---|
| Marmoset | untouched | **untouched** — a suggestive non-coding haplotype in a primate colony is not a seizure phenotype of WWOX loss; it does not extend the claim beyond rodents | untouched | untouched |
| Infant GWAS | **untouched** — volume of normal-range infants, minor allele with *more* WM; neither supports nor bounds a biallelic-null mechanism | untouched | untouched | untouched |
| Spina bifida GWAS | untouched | untouched | untouched | untouched |
| Review | untouched — its developmental and epilepsy sentences are already held from the same primaries | untouched — refs 26/27/48 already carried | untouched | untouched |
| Triad | untouched | untouched | untouched | untouched |

What each source **adds**, outside the claims:
- **To `DL-MECH-107` (intron 8):** three more intron-8 association signals, recorded as *not* convergence and as
  firing no trigger → `CC-20261002-B-INTRON8-01`.
- **To `FT-142`:** the "not a WWOX paper" negative is narrowed to "not a WWOX-function paper" →
  `CC-20261002-B-NONLINEAGE-01`.
- **To `CORPUS P263` / `LIT-0263`:** the review is read, its triage pathway ("P6 — DDR") and species ("rat") were
  wrong, and its sentences are mapped to their primaries → `CC-20261002-B-NONLINEAGE-01`.
- **To `DL-BIO-004`:** the triad is one more node of the same-laboratory aggregation chain that lead already
  down-weighted to *belief BASSO*; it supplies no independent replication, so the lead does not move.

Is any of the review's sentences sitting in the registries **as if independently established**? Measured: no claim
in `claim_registry_current` matches TIAF1, sciatic, Zfra, TRAPPC6A or Alzheimer; `neurodegenera` matches only
`CLAIM 037` (a quoted author interpretation) and `aggregat` only `CLAIM 033`. The Chang-lineage material lives in
research ledgers (`DL-BIO-004`, `FT-100`–`FT-102`) where it is already flagged single-laboratory. `CLAIM 016` and
`CLAIM 035` rest on `PAPER 056` (Wang 2012, co-authored by Chang N-S), which `PAPER 056` already flags. **Answer: no
inherited sentence found in a claim.**

## 3 · Answer to the question

**Non-lineage evidence, after scrutiny: almost none survives as evidence; what survives is bounded context.**

- **Epilepsy.** The only non-rodent item (marmoset) is a suggestive, intronic, single-haplotype pedigree association
  with no genome-wide signal, a deflated λ, carriers among unaffected and unrelated controls in one colony, and no
  function. It is **not** a WWOX deletion — the brief's premise is wrong. It does not survive as evidence that WWOX
  variation causes epilepsy in a primate.
- **White matter.** One human signal (infant GWAS) is sub-threshold by the study's own correction, unreplicated,
  non-functional, and its minor allele is associated with *larger* white-matter volume. It survives only as "WWOX-locus
  common variation may be associated with infant WM volume — unreplicated".
- **Brain development.** The spina-bifida signal is nominal, imputed and not replicated; it does not survive. The
  review's developmental statements are second-hand copies of primaries LEGEND already holds.
- **Brain aggregation / neurodegeneration (non-lineage? no).** Both Chang-laboratory papers are lineage, not
  non-lineage; the triad's brain data are one tumour-bearing mouse per arm with intact Wwox.

**Limits of this answer.** Two of five readings are partial (figure images for the review; appendix plot books for
the infant GWAS). The marmoset CNV absence rests on a reader's audit of the S7 sheets (an `.xlsx` that the manifest
validator cannot verify as text), and its intron annotation on S6, same limitation — both are stated in the dossier,
neither is a locator.

## 4 · What would change the model, and what would falsify this reading

- **Would change it:** an independent infant or child MRI GWAS replicating rs10514437 (or a proxy) for white matter
  at P < 5e-8 with an eQTL showing the allele changes WWOX expression in developing brain — that would make the
  white-matter limb touch human common variation (still T3 for the genotype class). A marmoset follow-up showing a
  coding or splice WWOX variant segregating with EEG-confirmed seizures would make the primate item real.
- **Would falsify this reading:** a marmoset CNV call over WWOX that S7 does not show (my negative is a reading of
  S7, not of the BAMs); a published replication of the spina-bifida WWOX locus; or a non-Chang laboratory replicating
  WWOX–TIAF1 binding or tumour-induced brain aggregation.

## 5 · Candidates

| ID | Class | What |
|---|---|---|
| `CC-20261002-B-NONLINEAGE-01` | MINOR | `CORPUS P263` / `LIT-0263` metadata and reading status; `FT-142` negative narrowed; 13 triples |
| `CC-20261002-B-INTRON8-01` | MINOR | annotate `DL-MECH-107` with three non-convergent intron-8 signals; 6 triples |

## 6 · Reading debt named (not queued — the queue belongs to the integrator)

- PMID 24503545 (Chiang 2013, WOX1 in human nervous-system tumours) — the only WWOX-direct reference of the infant
  GWAS, cited for axonal WOX1 expression; no registry record.
- PMID 21368882 (Lee 2010, TGF-β and TIAF1 self-aggregation) — cited by both Chang papers; no registry record.
- Figure images of PMID 25537520 (four schematics) — owed for a complete read.

## 7 · Anything in the brief that was wrong

1. **"WWOX gene deletion was more common in epileptic marmosets than control marmosets"** — not in the paper. The
   abstract's deletion sentence is about **KCTD18-like**; WWOX is a SNP haplotype; the CNV tables contain no WWOX
   event.
2. **"a locus within the coding region of WWOX"** (spina bifida) — the variants are intronic (intron 8); the abstract
   also names rs7184417 with rs28688166's statistics.
3. **"91 cases / 97 controls"** — the association models use 89/97; 91/98 is the folate-available set.
4. Minor: "neared genome-wide significance" (infant GWAS) is the paper's wording, but against the conventional 5e-8
   the SNP passes; it is "short" only of the paper's four-phenotype Bonferroni threshold.

## 8 · Hindsight observation on the trial-record route

`fulltext_receipts.py --ledger <scratch copy> record` appended to the scratch copy **and re-anchored the checkout's
`framework/state/state_manifest_current.md`** to the scratch tail. I reverted that file with `git checkout --`. An
integrator trial-recording in a scratch *clone* is safe; trial-recording with `--ledger` inside a working checkout
is not.
