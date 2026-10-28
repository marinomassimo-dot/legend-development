# Fly PARS2 reading for the ISR need (PMID 41380592), iteration 3
Actor scientist-c. context_policy SOURCE_FIRST for the first pass, QUESTION_DRIVEN for the comparison. Research layer, non-canonical.
**NOT WWOX EVIDENCE.** Drosophila model of mitochondrial prolyl-tRNA synthetase (PARS2) deficiency; GENETIC suppression only; no compound tested.

## What was actually read (true depth)
Redox Biol 2026;89:103966, PMC12754399, CC BY-NC (article XML: "open access article under the CC BY-NC license"). Artefacts in the shared checkout `files/`: PMC efetch XML (sha256 `5c7fffb1...b11a`), nine figure JPEGs and `mmc1.docx` from the PMC open-data bucket, nine supplementary images extracted from the DOCX. Read: abstract, introduction, all Results, Discussion, all Methods, the key-resources table, all nine main figure images, Table S1 and all nine supplementary images (S1 to S9; the file has no legends, only image titles). NOT read: any cited paper; the reference list was counted (60), searched for WWOX (none), and four titles looked at, so `references` is `not_read`. The article has no limitations section (two limitation sentences in the Discussion) and no results table. The dependency screen failed closed (Retraction Watch snapshot absent) and was not run. Manifest `deepdive_manifests/PMID41380592.json`: 49 locators (30 body, 19 figure or supplementary-image attestations), strict verification PASS. Receipt staged at `receipt_staging/scientist-c/FTR-20261027-41380592-01.json`; a trial append in a throwaway clone succeeded; the ledger of the real checkout was not touched.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted HYP-20261026-10 and -11, cards E01 and E02, DL-MECH-173.

## Decisive experiments (all GENETIC; elav-GAL4 pan-neuronal RNAi; dPARS2 RNAi background)
| Arm | Readout | Result (figure estimates, plot reading) | Controls, n |
|---|---|---|---|
| dPARS2 RNAi + GCN2 RNAi (BDSC 35355) | bang-sensitive fraction (adult, 4-6 or 5-7 days, sex not stated), recovery time, pupariation, eclosion | bang sensitivity about 87 -> 30 percent; recovery about 100 -> 10 s; pupariation lag mostly closed (about 95 percent at day 6) | control 0 percent, GCN2 RNAi alone about 4; 3 vials x 10 flies; recovery n=30; development N=3, n 28-30; Fisher exact |
| dPARS2 RNAi + ATF4 RNAi (THFC THU5856) | same | bang sensitivity about 93 -> 46 percent (vials about 30 to 62); recovery about 100 -> 15 s; development lag under a day | ATF4 RNAi alone about 10 percent; same n |
| mechanism | P-GCN2 up, P-PERK unchanged; P-eIF2 alpha up; puromycin incorporation down; GCN2 RNAi lowers P-eIF2 alpha (about 140 -> 109) and restores puromycin to about 60 percent | phosphorylation and synthesis (flux-like) readouts in head | N=3 to 4 |

Direction: suppression of the ISR kinase or effector REDUCES the phenotype (rescue direction), partially. Not done: any pharmacological ISR modulator; mitochondrial readouts after GCN2/ATF4 suppression; Ldh after suppression; lifespan, EEG, climbing; PERK perturbation; GCN2/ATF4 double-RNAi dilution control (a GFP titration control exists only for the dPARS2 transgene rescue, Supp S4). Knockdown efficiency measured in single-RNAi lines only (GCN2 mRNA about 37 to 57 percent lost, ATF4 about 27 to 42 percent). Seizure-like behaviour and developmental delay move together: no independent fitness measure. Text/panel defects: Results say 5-7 days, Methods 4-6 days; Fig 6B key assigns the solid bar to dPARS2 RNAi, which read literally contradicts the text (P-GCN2 rises).
Other observations (abundance, not flux): OXPHOS subunit protein falls (complex I MT-ND1, NDUFS1, NDUFS3; II, III, IV; not V), in-gel activity stains lower (qualitative for heads); Ldh transcript and Ldh protein (about 10-fold, one blot, N=3) up; no Ldh activity, lactate or PDH/PDK data; the ATF4-to-Ldh step is borrowed from an S2-cell paper. Human PARS2 V95I HEK293T single clone: ISR up via P-GCN2 (non-neural, one clone).

## What it provides
A precedent that an ISR can be harmful when a mitochondrial translation lesion drives it in neurons, and a design (kinase-resolved readouts, OXPHOS covariate, basal tone, genetic vs eIF2B-activator distinction). It is NOT a WWOX experiment: no link of WWOX to mitochondrial translation is shown, and the WWOX-side readouts (fly Atf4 needs amyloid; human knockout organoid ISR targets lower than chance) are unchanged.

## Consequences (propagated only where source-supported)
- HYP-20261026-10: precedent-and-design bullet, Stage 1 readouts, Stage 2 caution; no status, ranking or reopening change (`hypcurrent_it3_isr_20261027/ledger_edits.json`).
- HYP-20261026-11: readout addition to the complex I arm (below).
- Card E01: text for/transfer-limits/not_known/next_measurement; card E02: one observation row and counter-evidence sentence; both added by `build_cards.py` only once the ledger holds the receipt.
- HYP-20260709-01, -05 and E03/E04: none (no ketone, diet, PDH, PDK or pyruvate measurement; Supp S6 lists no pyruvate-metabolism term).
