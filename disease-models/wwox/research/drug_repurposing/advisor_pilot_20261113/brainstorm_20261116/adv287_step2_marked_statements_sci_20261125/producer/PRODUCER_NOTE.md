# PRODUCER_NOTE, ADV-287 step 2 (16 NEW marked statements), 2026-11-25

Hypothesis level; reference genotype class only; nothing here is medical advice. Producer: legend-delegate, model Sonnet 5.5, effort high. Held bytes only (worktree and read-only `files/`); no web fetch, PubMed, download, contact or spend; no e-mail address written anywhere; no card, registry or ledger edited; no commit. The pre-source arithmetic column was written before any source was opened (frozen copy outside the repository at `/home/desktop/.claude/jobs/488a3ad0/tmp/adv287s2/pre.json`); it is copied unchanged into `STEP2_TABLE.tsv`.

## 1. Counts (16 statements)

| Class | n | k |
|---|---|---|
| CORRECT | 10 | 3, 6, 7, 9, 11, 13, 16, 17, 18, 22 |
| INCOMPLETE | 4 | 8, 10, 12, 20 |
| WRONG | 1 | 2 |
| NOT ASSESSABLE | 1 | 21 (proposed design, no source claim) |

By word role (from the list file): LOAD_BEARING 12 (k = 2, 7, 8, 9, 10, 11, 12, 13, 17, 18, 20, 22), all assessable; INCOMPLETE-or-WRONG 5 of 12 (k = 2, 8, 10, 12, 20). Carrier: WORD 3 (k = 8, 10, 12), OTHER 2 (k = 2, 20). INCIDENTAL 4 (k = 3, 6, 16, 21): 3 assessable, 0 INCOMPLETE-or-WRONG; k = 21 not assessable. The decision rule in the PREREG (rate at or below 25 percent) is the Orchestrator's to apply; with 12 assessable LOAD_BEARING statements one statement is about 8 points. Calls that would move the LOAD_BEARING rate if reversed: k = 7 (CORRECT to INCOMPLETE, +8 points) and k = 8 (INCOMPLETE to CORRECT, -8 points); k = 2 as WRONG or INCOMPLETE does not change the rate; k = 3 and k = 6 are INCIDENTAL and do not enter it.

## 2. Borderline calls (the ones a second reader could split)

- k = 2: the upper bound 9 fold is exceeded by the very panel the package cites (DeLeeuw Fig 4G: derived about 12.8 and 19.1 fold for A357V and G566H, from small vehicle bars measured by pixel; reading error about 8 percent, so the excess survives). I wrote WRONG (number); INCOMPLETE (rows left out or misread) is a fair alternative. The marked word every sits on "unmeasured for every WWOX allele", which I left standing (no calibrated amount-times-function value in any held allele; P252A and P282A losses are qualitative), so carrier OTHER.
- k = 3: CORRECT as a hedged derived inference. "A small part" depends on scale (linear 8 to 28 percent of the deficit, logarithmic up to 47 percent); the card upper deficit 25 is above my bar-scan 21 (the package reads one bar as 4 percent, my scan 7 percent).
- k = 6: CORRECT; sub-spans not including the 1 mg cohort are also supralinear (5 to 11 mg slope 1.21; 8 to 21 mg slope 1.44), so "supralinear only when the lowest cohort is included" holds for the contrast the sentence draws only.
- k = 7: CORRECT; the same Rico-Molina table lists enantiomers at 34 and 38 percent at 500 uM and cites about 40 percent from the 2015 report (second-hand); the sentence quotes the racemate. Reversal would make it INCOMPLETE with carrier OTHER.
- k = 8: INCOMPLETE rests on reading "the one cell-level signal found" over all held sources (other cell-level readings are in the repository record); read over the database rows alone it is correct. The restated source (IT9 P4a README) says "a cell-level signal".
- k = 20: INCOMPLETE, carrier OTHER if "every region" means the three forebrain regions; if it means all four regions the cerebellum is unchanged by leaving out M6 (0.363 to 0.372) and the carrier would be the word. The pre-source arithmetic line misread "the other three mutants" as four mutants in all; the sentence implies five.
- k = 18: CORRECT; scoped to the 56 unexposed infantile-spasms children of that report; another cohort in the same batch table (7 of 52 untreated, different design) does not contradict that count. Only the abstract of PMID 18783433 is held (as the card states).

## 3. What I could not reach or did not do

- No full text of PMID 18783433 (abstract record only); no E-MTAB-14792 record (BioStudies returned 403 as recorded on 2026-10-25 and 2026-10-29 in the repository; not re-queried, no web access); no Supplementary Fig S3 of Breton 2021 (not held); Sada 2015 abstract only; the Guyon, Yadav, Bouchez and Le Dudal papers cited in the stiripentol record were not re-opened (quoted from the repository record).
- Whether "unmeasured for every WWOX allele" (k = 2) holds over the full repository list of WWOX missense alleles was checked against the alleles held in the package (Q230P at abstract level; P252A and P282A in Zhang 2025); the repository files that hold the wider list are named in the package but were not reproduced; the stability census file was not located in the time spent.
- Figure readings are pixel or by-eye readings of held images (error stated in each src file); none is a quoted table value except where the figure prints numbers (Cheng 2020 Fig 7c).
- The Zhang 2025 amounts and the Johannsen Q230P datum were not re-measured.

## 4. Obeid stop and incidents

- The Obeid 2026 article was not opened and no manifest, dossier, receipt or article text of it was read for any statement. No statement of the 16 rests only on it; k = 10 (the one human knockout deposit) could in principle be affected if that article holds a human knockout deposit, which this check cannot exclude; the INCOMPLETE call rests on E-MTAB-14792 alone, which does not depend on it. A grep for its PMID over the src files and the table returns 0.
- Incidental exposure, disclosed: while locating sources for an earlier statement I printed `wwox_function_reference_it6_20261029.md` and read lines of `wwox_data_census_it6_20261029.md`, both of which carry rows derived from that article (the census row 10, line 18). I did not use any of it, copied none of it into any src file, and for k = 10 I copied only census rows 1 to 6 and the E-MTAB paragraph. The same step was followed by a classifier stop of my response; I recorded the stop, received no operator feedback, and did not work around it.
- I did not open the frozen RP-045 prediction or any ADV-174 / ADV-175 sealed or custodian material, and did not touch `files/adv174_negraes_custodian_he` or `files/adv175_predictor_for_it`.

## 5. Method notes

- src files are for the blind reader: verbatim sentence, pointers, whole tables or passages with locators (file, figure or table, panel, row; species and replicate unit beside values), no verdict. Some src files include the repository own "Reading" paragraphs verbatim as source records (src_07, src_08); they are labelled as such.
- Recomputations are in the table (`recomputation` column) and reproducible from the helper scripts in `/home/desktop/.claude/jobs/488a3ad0/tmp/adv287s2/` (not in the repository): `adm.py` (P47T per-animal Adm and leave-one-out with the IT12 TMM and logCPM formulas, reproduces IT12 0.957, 1.194, 0.809, 0.363), `k6.py`, `edges.py` and the by-hand pixel scans noted in src_02 and src_03.
- Held image files are numbered differently from the legends: for DeLeeuw 2026 the image `ACN3-9999-0-g003.jpg` carries the legend headed FIGURE 4 and `g004.jpg` the legend headed FIGURE 5; for Shah 2025 `FSB2-39-e70614-g004.jpg` carries the legend headed FIGURE 6.
- Corrected sentences keep "derived" beside every derived number and list the supporting rows for any extremum wording.
