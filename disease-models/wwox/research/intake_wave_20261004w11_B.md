# Intake wave 11 (2026-10-04) — Scientist B: allele function and patient-count primaries

`context_policy: SOURCE_FIRST` (the Henry 2025 solved-cases table re-read was `QUESTION_DRIVEN`).
**Author:** ACTOR_ID `scientist`, Scientist B, branch `task/sci-B-20261004w11`. **Not medical
advice.** Public edition: class level only; no country, site or wording naming the parental side
of any inheritance or disomy.

**Assigned question:** what does each source add to, or limit in, the count of WWOX-diagnosed
individuals, the allele classes represented, and the route by which an allele becomes homozygous?

## 1 · Per paper

| PMID | Verdict | WWOX content (class level) | New vs held | Receipt file | Candidates |
|---|---|---|---|---|---|
| 40884527 (Beretti 2025, *Epilepsia Open*) | INGEST (denominator only) | 2/56 neonatal-onset pharmacoresistant MRI-negative epilepsies, 2/35 solved; WWOX on the panel; **no genotype, sex, onset or outcome** | a denominator; the two patients are **not countable** and plausibly overlap PMID 30356099 (shared co-authors, same centre; INFERENZA) | `sciB_40884527_1.json` (complete) | REGISTRY-01 |
| 40943441 (Panchenko 2025, *Int J Mol Sci*) | OFF-AXIS (mechanism-class citation) | WWOX named twice as a recessive gene unmasked by chromosome-16 isodisomy, citing PMID 38407561; the index patient (whole-chr-16 isodisomy) has **no** pathogenic chr-16 variant | the route is already held at research level (PMID 39101447, complete); the WM lacks it | `sciB_40943441_1.json` (partial: its one WWOX hop is paywalled) | ISODISOMY-01, REGISTRY-01 |
| 40083435 (Kava 2025, *Front Pediatr*) | INGEST | one female, homozygous `p.Leu239Arg` (M/M), first seizure 0.33 y, focal discharges, normal MRI, optic atrophy; LP by authors (June 2024), ClinVar conflicting; **predicted only** | 4th source for the allele; identity with the `PAPER 220` child (same university, shared author, overlapping window) plausible — **not summed** | `sciB_40083435_1.json` (complete) | L239R-01, REGISTRY-01 |
| 40183601 (Henry 2025, *Epilepsia*) — re-read | INGEST (owed sections) | homozygous `p.His322Arg` in two relatives, diagnostic per authors, VUS per ClinVar; **nothing measured**; earlier report = its own reference 11 (PMID 33726816, Table S7) — same family by inference | primary report of the VUS found; one gene-direct hop by content; no WWOX isodisomy case in this cohort | `sciB_40183601_1.json` (partial re-read, prior `-01`) | H322R-01 |

Receipts are in `scratchpad/receipts_pending_w11/` and copied to
`~/legend-receipts-backup-20261004/receipts_pending_w11/`. None was recorded in the real ledger.

## 2 · Answer to the assigned question, with limits

- **Count of WWOX-diagnosed individuals:** this wave adds **at most one** independent individual
  (the `p.Leu239Arg` child, only if distinct from `PAPER 220`) and **zero** with confidence. The
  two neonatal-cohort patients cannot be counted; the His322Arg family was already in the corpus
  and is the same family as an earlier DNA-only row; the isodisomy paper's patient is not a WWOX
  case. The commonest error in this corpus — one patient published twice — appeared **twice** in
  four papers (Kava/Yigit by institution and author; Henry/Stranneheim by the authors' own
  statement).
- **Allele classes:** no new class. Two homozygous SDR-region missense alleles (`p.Leu239Arg`,
  `p.His322Arg`), both **predicted, never measured**; one discordant classification (authors
  diagnostic vs ClinVar VUS).
- **Route to homozygosity:** consanguinity in every WWOX family of these papers where it is stated;
  isodisomy is held at research level (one complete reading) and proposed for the working model as
  a method rule, not as a frequency.

**What would change the model if true:** a published functional measurement of either missense
allele; a primary proving isodisomy for a WWOX allele with trio markers. **What would falsify the
counting inferences:** authors printing distinct family identifiers for the Kava/Yigit or
Henry/Stranneheim pairs.

## 3 · Brief and selection premises found wrong

1. B2 "a mechanism the model may not hold" — held at research level (PMID 39101447).
2. B3 "weakest item, a single WWOX token" — the token is a table row with a per-patient supplement.
3. B4 "the HGVS exists nowhere in the repo" — the wave-9 manifest and the ClinVar snapshot carry it.
4. B4 "may have no prior primary report" — it has one: the paper's own reference 11.
5. Wave-9 manifest "none [of 50 references] is WWOX-direct" — true of titles, false of content.

## 4 · Privacy observations (reported, not acted on)

The wave-9 Henry manifest (two snippets) and `CC-20261004W9-C-DEEPINTRONIC-01` (one triple) quote an
inheritance cell that names both parental sides; the corpus title of PMID 38407561 in the paper
registry names one. Details in `CC-20261004W11-B-H322R-01` §6 and `CC-20261004W11-B-REGISTRY-01` §4.
