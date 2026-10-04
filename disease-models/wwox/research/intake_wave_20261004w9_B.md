# Intake wave 9 (2026-10-04) — Scientist B

`context_policy: SOURCE_FIRST` for every paper (first passes committed before any registry, ledger or candidate text was opened; the comparison with the wave-8 lead and the DRG records followed). Not medical advice. This note lists PMIDs, so it lives under `research/`.

## Per paper

| PMID | What it is | Verdict | WWOX | Receipt (prepared, not recorded) |
|---|---|---|---|---|
| 23179753 | Krug 2013, hESC developmental-neurotoxicity platform (valproate, methylmercury) | INGEST (partial read) | zero in text; five probe-set rows in the supplement, all UP with valproate | `FTR-20261004-23179753-01` |
| 24935251 | Balmer 2014, HDAC-inhibitor time-course in neural differentiation | INGEST (partial read) | zero in text; one treated row UP (1.574, adjusted p 0.042); one untreated developmental row DOWN (0.59) | `FTR-20261004-24935251-01` |
| 26272509 | Rempel 2015, classifier for HDAC inhibitors (genome-wide table) | INGEST (partial read) | zero in text; three of five probe sets UP with valproate | `FTR-20261004-26272509-01` |
| 27188386 | Shinde 2017, STOP-Toxukn/Toxukk indices (signed-fold tables) | INGEST (partial read) | zero in text; UP in both systems (+2.127, +1.683); Table 7 membership at 1000 uM without direction | `FTR-20261004-27188386-01` |
| 32355866 | **Bey 2020** (not Hordeaux), intra-CSF AAV9/AAVrh10 in macaques | INGEST (partial read) | none | `FTR-20261004-32355866-01` |
| 35333110 | Hordeaux 2022, Krabbe gene therapy, GLP ICM macaque tox | INGEST (partial read) | none | `FTR-20261004-35333110-01` |

Dedup: all six had no registry record and no receipt; none is a duplicate of a held record. Files: `scratchpad/receipts_pending_w9/sciB_<pmid>_1.json`.

## Answer to the assigned question, with limits

**Does the valproate direction in the curated database row settle?** The four primaries read do not contain the curated direction. Where a sign is recoverable the valproate effect on WWOX probe sets is **up** (ratios 1.33 to 2.13, adjusted p 0.007 to 0.042), in immature neural-lineage cells from one hESC line, at 0.6 to 2 mM; no row shows WWOX down with valproate; the one "down" row is an untreated developmental change. The four papers share data and are not four replications. The text of none of them names WWOX. So (a) the paper-level statement that valproate "decreases" WWOX is unsupported by the four primaries read, (b) the opposite statement that valproate "increases" WWOX is supported only as a supplementary probe-set observation in immature cells at millimolar concentrations, and (c) the fifth primary (PMID 28001369, paywalled) is unread and remains the only candidate source for a decrease. Neither direction says anything about a patient with two loss-of-function alleles, a mature neuron, or a clinical exposure. Proposed correction of the lead: `CC-20261004W9-B-VPA-DIRECTION-01`.

**Where each paper stops talking about WWOX.** Text: never. Supplement: Table S1 (PMID 23179753), Tables S1-S2 (PMID 24935251), the genome-wide Table S1 (PMID 26272509), Tables 1, 3, 5, 6, 7 (PMID 27188386). The gene-therapy papers do not carry the gene.

**DRG (two papers).** PMID 32355866: eight macaques, GFP reporter, lumbar intrathecal 2.5E+13 vg or ICV 4.5E+12 vg, triple immunosuppression, three weeks; DRG GFP in large-diameter neurons; mild-to-moderate mononuclear infiltration without a grade table. PMID 35333110: GLP ICM in juvenile rhesus, three doses (4.5E12 to 4.5E13 GC), no immunosuppression, 3 and 6 months; DRG neuronal degeneration at most minimal; dorsal axonopathy dose dependent up to grade 3 at the top dose (Figure 5C; the text sentence says minimal to mild); no progression 90 to 180 days; secreted-enzyme cargo. Increments only: `CC-20261004W9-B-HORDEAUX-ATTRIBUTION-01`.

## Briefs and selection tested

1. The selection called PMID 32355866 "Hordeaux 2020"; it is Bey 2020 (first author Bey, Nantes).
2. The selection said all four valproate primaries show "zero WWOX hits" and that the datum might be unrecoverable: the main text indeed has none, but all four supplements carry WWOX rows (recoverable by script, no image reading needed).
3. The selection said none carries a receipt and none is held: confirmed.
4. The wave-8 lead asks for the five primaries; four were readable and one remains blocked.
5. A dependency screen flagged one cited reference of PMID 32355866 (retracted 2022); citation only.

## What would change the model, and what would falsify it

- Would raise the valproate lead: WWOX transcript and protein up in human neural cells (not probe-level, not immature hESC) with and without valproate, with an HDAC-inhibition control. Would drop it: no change, or the fifth primary showing a decrease in a relevant cell.
- Would change the DRG record: a graded primate study of a non-secreted cargo at similar GC per gram brain showing grade 2 or more degeneration.

## What I did not read

Figures as images except the exposure figures, the benchmark-concentration panel, Figure S5 and Figure 5; supplementary PDFs of PMID 23179753, 24935251, 26272509 and the pptx of PMID 27188386; the gene lists beyond header, sentinel and WWOX rows; PMID 35333110 supplements.

## Receipts and landing

Receipts are prepared, not recorded. Manifests sit in `deepdive_manifests/`; they point at root `files/fulltext/` artefacts (gitignored, hardlinked into the worktree).
