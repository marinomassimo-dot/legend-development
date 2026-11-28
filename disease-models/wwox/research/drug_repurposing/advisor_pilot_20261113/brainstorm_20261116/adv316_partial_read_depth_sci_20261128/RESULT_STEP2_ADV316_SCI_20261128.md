# ADV-316 step 2 (SCI successors ba and bb, 2026-11-28): FINAL result, three records read, SCI checks on the Huang originals done (section "SCI checks, window bb")

Hypothesis level; not medical advice. PREREG_STEP2 (frozen 0f8d840dc; curated-set amendment before any unread part was opened). Delegates: legend-delegate, sonnet 5.5, effort high stated in every dispatch; six dispatches planned, five run (see 27339895). Reports verbatim: `FIRST_READ_*`, `BLIND_READ_*` in this folder. No safeguard stopped any delegate. One route was refused by the session's classifier (Wayback copy of the Huang supplement) and was not retried.

## Rates (denominator: 15 curated sentences = 5 + 3 + 7)
| record | sentences | blind SUPPORTED | ADD | MUST CHANGE | UNSETTLED |
|---|---|---|---|---|---|
| 41744777 (Nabakowski 2026) | 5 | 1 (C04) | 3 (C01-C03) | 1 (C05) | 0 |
| 42395553 (Petrozziello preprint) | 3 | 1 (C03) | 2 (C01, C02) | 0 | 0 |
| 27339895 (Huang 2016) | 7 | 0 | 3 (C01, C06, C07) | 3 (C02, C04, C05) | 1 (C03) |
| total | 15 | 2 | 8 | 4 (27 percent) | 1 |
Blind MUST CHANGE 4 of 15; any change (MUST CHANGE + ADD) 12 of 15. Against ADV-282's 43 of 124 (35 percent) MUST CHANGE the sample is small (15) and its sentences are claim clauses, not first compositions.

## Strict (first reader verified on the unread part AND blind MUST CHANGE)
* **Clean strict: 0.** Conditional: 1.
* 41744777 C05 (CLAIM 047 clause "a liver-de-targeted capsid costs ~8-fold packaging and brain exposure"): both readers flag it and SCI checked Fig 4D on the image (brain vg/ug DNA, AAV9 about 4.5e7, AAV9-DM about 7e5, about 60-fold lower; liver about 127-fold; heart DM lower too). The ~8-fold is packaging only; the clause can be read as 8-fold for brain too. The first reader's verdict is conditional on that reading ("FALSE if read as 8-fold"), so it is strict only on the ambiguous reading. The other C05 clause (primate brain, 1-4 vg/DG) is NOT THIS PAPER: an artefact of cutting a multi-paper claim sentence, not a defect of CLAIM 047.
* 27339895 (Huang): **no first reader was run**: the supplement (Fig. S1, where the antibody quality is "rechecked") could not be obtained (PMC bin: reCAPTCHA page; Europe PMC supplementaryFiles: error; PMC open-data bucket: no entry; Wayback: refused by the safeguard). Supplement ACCESS-LIMITED. The three blind MUST CHANGE (C02 "no mitochondrial or cytosolic purity marker row" and "every manipulation is overexpression"; C04 "with overexpression or dominant-negative constructs"; C05 the "under stress" leg) are on parts the receipt already counts as read, so they are listed apart, not strict. SCI text check: the main text builds dominant-negative dn-WWOXww into the binding and FRET experiments, and calls the antibodies "homemade" with quality "rechecked (supplemental Fig. S1)". **Owed: SCI check of Fig 4C/4D (alpha-tubulin row under cytosol lanes; cytochrome C row in 4D) and Fig 4E on the images** before any of these four statements is used.

## What one reader found and the other did not (listed apart)
* 41744777: PAPER 228 Role says "double-mutant AAV9-DM"; the XML has no "double mutant"/"two mutations" (SCI text search) and says "five point mutations". First reader only.
* 41744777: the "peak AR 7.3e7 and 5.8e5" (ratio 126) are printed in Results 3.3 and match no plotted point of Fig 3 (readers: Fig 3 liver means give about 155-170). SCI saw the text sentence; it cites "Figure 2" and "ventral side". Read the 126 as text-stated.
* 41744777: Fig 5A liver RNA falls about 28-fold, not 127 (first reader, by eye); heart is de-targeted as much as liver (Fig 4B); brain vg falls about 60-fold while "similar biodistribution" is in the abstract and Highlights (blind reader).
* 42395553: C01 "not disease-specific on these data" rests on a non-significant interaction (blind: "no significant interaction detected"); neuron n per cell and unit unstated (Fig 4B df 28 implies 8 per cell, Fig 4A n = 4); the 100 ng/mL, 24 h window is in Results text only. The unread Figures 1, 2 and Supplementary Figure 1 do not bear on any sentence (first reader).

## Prediction
Predicted at least 1 strict. Observed: 0 clean strict, 1 conditional (41744777 C05), pending SCI checks on the Huang figures. The rejecting observation (0 strict) is therefore **not settled either way**; by the stated rule it is met on clean strict and not met on the conditional one. Not a verdict on the partial tier.

## SCI checks, window bb (Huang 2016, PMID 27339895; original image `files/figures/PMID27339895/fig4.jpg` plus the held page text `files/fulltext/PMID27339895_Huang2016_PMC5016130_wayback20250308.html`; read by eye, one image, hypothesis level)
* **Fig 4C (Cytosol and Mitochondria blots):** the alpha-tubulin row is present under the Cytosol lanes only; the Mitochondria panel has IκBα, pY33-WWOX, WWOX, p-ERK (blank) and ERK rows and no marker row. CONFIRMED (blind C02 (b), C07). Fig 4C carries no cytochrome C row.
* **Fig 4D (Mitochondria only, IoP 1, 2, 3 h):** a cytochrome C row IS present. Its band is faint in Control, 0 and 1 h and strong at 2 and 3 h, so as a marker it is not constant across lanes (by eye; no quantification printed). CONFIRMED. The printed "% reduction" rows are WWOX 0, 0, 91, 25, 12 and IκBα 0, 0, 93, 93, 8; the WWOX bands themselves do not look visibly different across lanes at this resolution (by eye only, no densitometry; single blot, no n stated). Consequence: the sentence "no mitochondrial or cytosolic purity marker row" is FALSE as written for the paper; it must say which blot (4C: cytosolic alpha-tubulin only; 4D: cytochrome C, uneven).
* **Fig 4E (MitoTracker overlap, n = 3 in the legend, mean ± S.D.):** WWOX in mitochondria about 84 (Cont), about 60 (IoP 3 h), about 86 (TNF-alpha); IκBα about 83, 50, 70. CONFIRMED against the blind table. The printed key reads "*p>0.05; **p<0.001; ****p<0.00001" (confirmed on the image: a typo for "<" or an unresolved meaning; UNSETTLED which). The replicate unit of n = 3 is not defined; 4C and 4D state no n.
* **Text checks (one-line searches on the held page):** "stress" occurs once, in a reference title about p53 and IκBα (apoptotic stress, hypoxia), none in a WWOX-mitochondria context: the blind C05 point (the paper's mitochondrial manipulation is IoP, not a stress, and WWOX leaves the mitochondria) stands on the text; the "low-dose maturation stimulus" description is the blind reader's reading, not verified by me. The only "mainly localized in the mitochondria" sentence is a citation-backed statement (refs 21, 22, 23, 38, 39). Dominant-negative and overexpression constructs occur in the binding, FRET and IP work (Methods "DNA Constructs"; Figs 6, 8), not in Fig 4: blind C04 and C02 (a) stand.

### The four Huang statements, settled
| Statement | Status after SCI check | Basis |
|---|---|---|
| C02 "no mitochondrial or cytosolic purity marker row" (and "every manipulation is overexpression") | MUST CHANGE confirmed, both clauses | Fig 4C alpha-tubulin and Fig 4D cytochrome C on the image; dn-WWOX and EGFP-WWOX constructs by the text |
| C04 "with overexpression or dominant-negative constructs" (mitochondrial data) | MUST CHANGE confirmed | Fig 4C-E endogenous proteins in MOLT-4; constructs only in binding/FRET/IP |
| C05 the "under stress" leg | MUST CHANGE confirmed on the text; not on a measurement | the one "stress" in a reference title; IoP used |
| C03 pS14 other lines | stays UNSETTLED | pS14 only in MOLT-4 (blind), supplement S1 not held |
Not strict: no first reader exists for Huang (supplement ACCESS-LIMITED), so these three MUST CHANGE confirmations do not alter the strict count (clean strict 0, conditional 1 on 41744777 C05). The prediction stays **UNSETTLED**, exactly as stated above.

## Owed
SCI checks of Huang Fig 4C/4D/4E: DONE (window bb); sentences to IT32 with the whole source named (files: fulltext XML/HTML, figures dirs, `files/figures/PMID41744777/` and `PMID42395553_r2/` new); receipts for the readings (figures of 41744777 as images; Figures 1, 2, S1 of 42395553; coverage_report, reading_state, ranking, both views, package); deliver to ADV; operator PDF list adds the Huang supplement PDF (https://pmc.ncbi.nlm.nih.gov/articles/instance/5016130/bin/10.1074_M116.716167_jbc.M116.716167-4.pdf, a person with a browser).
