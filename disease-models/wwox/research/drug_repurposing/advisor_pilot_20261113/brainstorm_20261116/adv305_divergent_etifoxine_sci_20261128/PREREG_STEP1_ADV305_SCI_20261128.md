# ADV-305 step 1: pre-registration (SCI, window 64fc909a)

Frozen 2026-11-28T07:32:33Z, before any figure image, vehicle baseline, n or supplementary item of PMID 40561753 was opened by this unit. **Seen before freezing (disclosed):** the abstract and the printed means and SDs of sections 3.3 and 3.4 (zebrafish MEA: spikes, mean firing rate, electrographic events; culture MEA: spikes, mean firing rate, bursts). Step 0: `STEP0_ADV305_SCI_20261128.md`. This is a re-analysis, not a blind test. Hypothesis level; not medical advice. Held and public only; no contact; no spend.

## Question
In a developmental epilepsy model and in embryonic cortical cultures, does the anti-hyperexcitability effect of etifoxine track direct GABA-A potentiation (E1), TSPO-linked neurosteroid synthesis (E2) or a steroid-independent TSPO or metabolic action (E3)?

## Ligand properties used (from the paper's own discussion and the repository's etifoxine brief; each is a stated assumption, not a result)
Etifoxine: GABA-A positive modulator and TSPO ligand (the paper says it does not increase neurosteroid synthesis; the repository brief cites a frog-explant increase: disputed). XBD173: TSPO ligand that raises neurosteroid synthesis, negligible GABA-A affinity. PK11195: TSPO ligand that lowers basal steroid conversion, not a GABA-A modulator. Ro5-4864: TSPO agonist, proconvulsant in the same model (a negative control). Stiripentol (STP): GABA-A modulator, not a TSPO ligand.

## Quantity (fixed now)
Per assay and per compound, the vehicle-normalised effect on the two common parameters (number of spikes; mean firing rate): zebrafish MEA: value(treated) / value(DMSO vehicle) from the same figure; cultures: share of the 4-aminopyridine increase blocked = (value(4-AP alone) - value(treated)) / (value(4-AP alone) - 100) on the "% of baseline" scale. Ordering of the five compounds by effect in each assay; n per arm and the SD overlap are recorded; no significance claim is made from n of this size.

## Predicted observable per explanation
* **E1 (direct GABA-A):** STP and etifoxine are the two largest effects in both assays, and XBD173 and PK11195 are each smaller than etifoxine by a factor of at least 2 in both parameters in both assays; Ro5-4864 about 0.
* **E2 (steroidogenic TSPO):** etifoxine and XBD173 are the two largest TSPO-ligand effects in both assays and PK11195 is the smallest of the three by a factor of at least 2; Ro5-4864 (steroidogenic) is not required to be 0.
* **E3 (steroid-independent TSPO or metabolic):** etifoxine, XBD173 and PK11195 all reduce, and within an assay none differs from the others by more than a factor of 3 in either parameter; Ro5-4864 about 0.
A pattern is "favoured" if its prediction holds in both assays for both parameters; "ambiguous" if it holds in one assay only or the ordering of the two assays disagrees; otherwise "not supported". Unclassifiable in both assays: the result is "no discrimination".

## Strong counterexample to carry
STP, which has no TSPO action, is the largest effect in the zebrafish assay on the printed events (0.375 against 3 to 5 for the TSPO ligands) and in the cultures on the printed values: the GABA-A route reaches deeper suppression in this system than any TSPO ligand, whatever the TSPO ligands share. And the printed human result (Riebel: no change of allopregnanolone) weighs against E2 as the route of etifoxine.

## What each result changes
E1 favoured: etifoxine acts here as a second GABA-A modulator beside ganaxolone; TSPO-specific claims unsupported; the INV-10 probe role is "second GABA-A comparator". E2 or E3 favoured: etifoxine stays a TSPO-class probe; ganaxolone is the cleaner GABA-A comparator; the discriminating laboratory step becomes the TSPO block in the same cells. Ambiguous or no discrimination: etifoxine stays a conditional probe; the missing observation of step 0 is the next step; nothing in the repository's etifoxine decision changes.

## Readers
One figure reader (legend-delegate, sonnet, effort high stated in the dispatch) extracts values from Figs 1 to 5 of the held figures blind to this file; SCI computes the quantity; a second reader re-extracts one of three figures as an independent check of the extraction. A delegate stopped by a safeguard is recorded, counted not checked, not retried.
