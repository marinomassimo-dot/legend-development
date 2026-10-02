context_policy: SOURCE_FIRST

# Intake wave 2 — 2026-10-03 — Scientist A: patient genotype→phenotype series and measured-vs-predicted allele consequences

- **Actor:** ACTOR_ID `scientist` (Scientist A), branch `task/sci-A-20261003`, dispatched by the Orchestrator under the standing authorisation of 2026-09-28.
- **Papers (6):** PMID 30356099 · PMID 39101447 · PMID 37974179 · PMID 35573960 · PMID 42193054 · PMID 24456803.
- **Method:** first pass written from each source (article XML, every figure image, every supplement) before any registry, claim or ledger record was opened; then compared. Patients are described at class level only (allele class × zygosity × phenotype band). **Not medical advice.**

## 1 · Question assigned

> What does each source add to, or limit in, the mapping from WWOX allele class (null/null, null/missense, CNV, canonical splice) to the phenotype axes — seizure onset and drug response, developmental ceiling, brain MRI signature, survival — and what does each source show about whether an allele's functional consequence was *measured* rather than *predicted*?

## 2 · Per paper

| PMID | Verdict | Allele class × zygosity (class level) | Consequence measured? | What is new versus held | Receipt (prepared) | Candidates |
|---|---|---|---|---|---|---|
| 30356099 (Piard 2019) | INGEST | 20 patients, null/null, null/missense, missense/missense, CNV | RNA for 2 of 20 (a canonical acceptor allele → exon 3 skipping; one missense, no anomaly); protein never | First read of the four supplementary tables and the figures: death count 9 not 8; the seven-patient null group includes a contiguous-gene deletion, an untested sib, a terminated pregnancy and two survivors; primary row for a homozygous Q230P death at 3 y 3 m; P47T/P47R mislabel in S2; possible double publication of one patient | `sciA_30356099_1.json` (partial — open multihop queue only) | PIARD-01, Q230P-01, CLAIM018-SOURCE-01 |
| 39101447 (You 2024) | INGEST | canonical donor × homozygous (isodisomy inferred) | Exon 2 skipping in a HEK293T minigene (65 nt, out-of-frame); no patient RNA, no protein | Registry over-read the minigene as protein truncation; vigabatrin "effect" is clinical, electrographic seizures persisted at 11 months | `sciA_39101447_1.json` | VIGABATRIN-01 |
| 37974179 (Dong 2023) | INGEST | two-deletion allele (intron-5 + exon-6, out-of-frame) / in-frame exons 6–8 deletion | Breakpoints measured (gap PCR, Sanger); consequences predicted | No PAPER record existed (stub only); DL-MECH-053 mislabels both deletions as splice-acceptor / missense | `sciA_37974179_1.json` | REGISTRY-01, DONG-01 |
| 35573960 (Riva 2022) | INGEST | nonsense / exon-6-only deletion (predicted null/null) | Exon 5–7 junction measured in patient fibroblast RNA; stop allele's mRNA detectable on the gel, unquantified; no protein | No identity record existed at all; drug-failure list includes vigabatrin; exome CNV false negative | `sciA_35573960_1.json` | REGISTRY-01, VIGABATRIN-01 |
| 42193054 (Sapuppo 2026) | INGEST (index case only) | exons 6–7 deletion + exon 8 frameshift, **phase unknown** | Nothing measured beyond DNA | Table 1 audited row by row: every non-index row is an already-counted Piard or Dong patient, with transcription errors; CLAIM 012 lacks the phase caveat | `sciA_42193054_1.json` | SAPUPPO-01 |
| 24456803 (Abdel-Salam 2014) | INGEST | nonsense × homozygous (one genotyped child; sib untested) | DNA only; rat "no protein" is borrowed | `c.160G>T` is impossible for p.Arg54*; the paper's own supplement says `c.160C>T`; registry note adds a muscle biopsy and a carrier-safety reading the paper does not support | `sciA_24456803_1.json` | ARG54-01 |

Receipt files are in the Orchestrator's scratch `receipts_pending_w2/`; none is appended.

## 3 · Dedup — each patient counted once

- The Abdel-Salam family (one genotyped homozygote + one untested sib) re-enters Piard 2019 S3 and Piard's null group, and is quoted by Dong and Sapuppo. **Count: 1 genotyped + 1 presumed.**
- Sapuppo 2026 Table 1 = Piard P2, P3, P4, P5, P9, P11, P15, P16 + Dong's patient + the index. **New individuals: 1.**
- Dong's patient appears again only in Sapuppo. **Count once.**
- Piard P8 and the Tarta-Arsene 2017 case match on six attributes and share an author; Riva 2022 tabulates them as separate columns. **Hypothesis of one individual; do not sum until Tarta-Arsene 2017 is read.**
- New individuals added to LEGEND by this wave: Riva's child, Dong's child, You's child, Sapuppo's index infant (four), plus Piard's series and the Abdel-Salam family already registered.

## 4 · Answer to the question, with its limits

**Measured versus predicted.** Across six papers and 26 individuals described first-hand (Piard 20, Abdel-Salam 2, four single cases), a consequence was measured on **patient** RNA for exactly three alleles: a canonical acceptor allele → exon 3 skipping (Piard P1, tissue unstated), a missense allele → no splice change (Piard P3), and an exon-6-only deletion → exon 5–7 junction in fibroblasts (Riva). One canonical donor allele was measured only in a heterologous minigene (You). **No protein from any allele, no NMD test, no quantified ratio of aberrant to correct product** appears anywhere in the set. Every "null", "truncated", "in-frame residual function" label is a prediction from position and frame. Q230P, the commonest missense in the largest series, had no RNA studied in any of its four carriers there.

**Allele class → phenotype.**
- *Seizure onset* does not separate classes in this set: day-1 to day-20 onsets occur in null/null (Riva), predicted-null CNV compounds (Sapuppo, Dong) and null/missense genotypes (Piard S1).
- *Drug response* is resistance almost everywhere; the exceptions are clinical, single and genotype-heterogeneous (Piard P2, null / in-frame exon-7 deletion, seizure-free from 2 y 3 m; You, predicted null, visible seizures stopped under vigabatrin while the EEG did not normalise). Vigabatrin failed in another predicted null/null child (Riva).
- *Developmental ceiling* is uniform (no sitting, walking or speech) across every WOREE genotype class in Piard S1 — zero variance, so it cannot discriminate classes.
- *MRI*: thin corpus callosum and atrophy dominate; inferior vermis hypoplasia appears in one null/null child (Riva) while Piard S4 records none in 33 WOREE patients.
- *Survival*: the paper that most supports "null genotypes are most severe" (Piard) defines its null group from seven hand-picked patients that include a contiguous-gene deletion (also removing NUDT7, VAT1L, CLEC3A), an untested sib, a termination and two long survivors, and leaves out its own homozygous p.Arg264* pair who lived to 8 y 11 m and 5 y 2 m. Its "no premature death with missense-only genotypes" survives only under a < 3 y cut-off, because a homozygous Q230P patient died at 3 y 3 m.

**Limits.** Case reports and one 20-patient series; ascertainment toward severe and toward the dead; the xlsx supplement cannot carry a machine-verified locator (its facts are recorded with the recount script); nothing here measures residual function.

## 5 · What would change the model, and what would falsify it

- **Would change it:** an RT-PCR with an NMD inhibitor, or a protein assay, on cells carrying any of these alleles — in particular a quantified residual correct-splice fraction for a canonical acceptor or donor allele — would replace a predicted class with a measured one. A confirmed identity between Piard P8 and Tarta-Arsene 2017 would remove one patient from every census that sums the two.
- **Would falsify the "null is most severe" reading as used in LEGEND:** a genotype-traced re-tabulation of Piard S1 + S3 that (a) drops the contiguous-gene deletion and the untested sib, (b) excludes the termination, (c) includes all biallelic truncating genotypes, and still shows no survival difference from null/missense genotypes. The data to do it are in the persisted supplement.

## 6 · Corrections to LEGEND found after the first pass (all as candidates)

- `PAPER 043`: `c.160G>T` → `c.160C>T`; a non-existent muscle biopsy; an untested sib presented as a case; carrier cancer risk stated as absent against the authors (`CC-20261003-A-ARG54-01`).
- `CLAIM 018`: Source line still names "Piard 2019"; the allele does not occur in that paper or its supplement (`CC-20261003-A-CLAIM018-SOURCE-01`, MAJOR taken conservatively).
- `CLAIM 019`: primary row for the homozygous Q230P death (`CC-20261003-A-Q230P-01`).
- `CLAIM 001` / `PAPER 016` / `DL-MOL-007`: electrographic persistence; Riva's vigabatrin failure; phenobarbital/nitrazepam were adverse-event stops (`CC-20261003-A-VIGABATRIN-01`).
- `CLAIM 012` / `PAPER 012`: phase unknown; Table 1 is not a count source; wrong title (`CC-20261003-A-SAPUPPO-01`, MAJOR).
- `DL-MECH-053`: both Dong alleles are deletions, not "splice-acceptor" and "missense" (`CC-20261003-A-DONG-01`). Noted, not proposed: `DL-MECH-022`'s *«nessuna proteina residua»* for Riva's patient is predicted, not measured.
- Identity records for PMID 35573960 (none existed) and PMID 37974179 (stub only) (`CC-20261003-A-REGISTRY-01`).

## 7 · Where the selection's hypotheses held and where they did not

- A1 "how many alleles were assayed": answered — two of twenty, from the supplement the selector could not see.
- A2 "minigene ≠ patient RNA": held; the residual fraction is not measurable from the published gel.
- A3 "exome called one thing, genome another": partly — the exome was right on exon-6 dosage; what it missed was the heterozygous loss of exons 7–8 and the phase.
- A4 "found only after array-CGH and Q-PCR": the first detection was fibroblast RT-PCR; the order was RT-PCR → qPCR → array-CGH.
- A5 "comparison table provenance": confirmed as the main problem — the table re-counts known patients with errors.
- A6 "convergence argued, not measured": held; and the paper's own nomenclature is internally inconsistent.
