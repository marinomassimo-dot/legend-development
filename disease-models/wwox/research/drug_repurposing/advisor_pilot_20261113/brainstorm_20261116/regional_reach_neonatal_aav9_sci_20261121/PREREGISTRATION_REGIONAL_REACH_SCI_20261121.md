# Pre-registration: is the low cerebellar WWOX after neonatal ICV AAV9-hSynI a platform property or specific to Obeid 2026? (SCI window V, 2026-11-21; self-chosen after ADV-136, announced to ADV; hypothesis level; no dose, no recommendation for or against any use of any agent in any person; reference genotype class only; not medical advice)

Committed before any retrieval. Nothing about the answer has been looked up for this question; what is known is the paper's own panel (ADV-136 result): in high-dose mice the cerebellum is the lowest region at every age (P90 0.6 times WT in two lanes, P180 0.1 to 0.5, P300 1.4 in one mouse and 2.15 as a mean of three with SD above the mean), against cortex 2.0 to 10.6 and midbrain 1.3 to 5.2.

## Question
In published mouse work with neonatal (P0 to P2) intracerebroventricular AAV9 carrying a neuron-directed promoter (human synapsin I or an equivalent neuron-restricted promoter), how does transgene or transgene-protein level (or transduced-cell fraction) in the cerebellum compare with cortex in the same animals, with age, dose, denominator, n and statistic per row, and with marker (reporter or transgene readout) kept apart from function?

## Prediction (fixed now)
Cerebellar levels are lower than cortical levels in most qualifying rows (ratio at or below 0.5 in at least half of the rows that give a ratio), so the low cerebellar WWOX in the benchmark would be at least partly a platform property.

## Qualifying row (all must hold)
Mouse; ICV or intracisternal-at-neonatal-age injection at P0 to P2 of an AAV9 capsid (capsid variants are listed separately, not counted); promoter neuron-restricted (hSyn, Syn1 or equivalent; ubiquitous promoters are a separate stratum, not counted); a per-region read in the same animals including the cerebellum and a cortical region; harvest age and a per-region denominator stated (vector genomes per diploid genome, transcript or protein relative to a loading control or to a wild-type reference, or transduced-cell counts out of a stated total); n stated.

## Verdict rule (fixed now)
* **PLATFORM-LOW**: at least three papers from at least two distinct senior-author groups with a qualifying row, and at least two thirds of the ratio-giving rows show cerebellum at or below 0.5 of cortex.
* **PAPER-SPECIFIC**: at least three papers from at least two groups, and at least half of the ratio-giving rows show cerebellum at or above cortex (ratio 1 or higher).
* **CONFLICT**: both kinds present at those thresholds, or ratios between 0.5 and 1 dominate; the rows are named.
* **THIN**: fewer than three qualifying papers; the named missing measure is a per-region neuron-promoter readout with a denominator.
Rejecting observation for the prediction: PAPER-SPECIFIC. Ratios are taken within an animal or within a study; no cross-study pooling of absolute values; a different capsid, promoter class or injection age is a different stratum.

## Method
Plain clients only (Europe PMC REST with field-tagged queries; PubMed through the metadata tool; the PMC article page as a route for full text; a challenge page is a stop for that route and is recorded as the route result; an absence claim needs a second route). No contact e-mail is sent to any service. Sources read in full including figure legends and, where reachable, supplements; reached-or-not is stated per paper. One producer reads and tabulates; one blind verifier receives only the passages and the proposition for the rows that carry the verdict and adjudicates each negative against the source. Model and effort are stated in each dispatch and read back by `session_model_census.py`.

## What the result can change
Whether a partial-restoration design brief states a per-region expression range with the cerebellum as the expected floor of an AAV9-neuronal platform, and whether any ataxia or cerebellar endpoint needs a separate route (not a comparison of agents). It does not bear on WWOX biology; the cerebellar mechanism thread of 2026-09 (`analysis/cerebellar_discrimination_experiments_20260922.md` and siblings) is not reopened.

## Limits fixed in advance
Same model family for producer, verifier and this window; main texts only unless a supplement is reached; most studies use reporter genes, so a reporter ratio is a transduction ratio, not a WWOX ratio (a gene-specific protein can differ through stability and cell type); the benchmark's per-lane values are unreplicated blots (ADV-136 result).
