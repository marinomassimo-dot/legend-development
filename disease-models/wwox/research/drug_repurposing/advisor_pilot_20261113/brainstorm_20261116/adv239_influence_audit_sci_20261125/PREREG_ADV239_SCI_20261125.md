# ADV-239 pre-registration: influence audit of carried small-n bulk-RNA inferences (SCI; hypothesis level; not medical advice)

Frozen at 2026-11-25T01:24:57Z, before any per-unit score or leave-out value was computed in this window. Effort high, no delegate, no spend, no external request except reading held files.

## What I had read before writing this (not blind)
* The brief, checkpoint AD sections 2, 3 and 7, and therefore the ADV-233 conclusions (P47T animals M6 and F8 carry the forebrain TNFA, IL6/JAK/STAT3 and HYPOXIA enrichments; GLYCOLYSIS survives; cerebellar cholesterol, fatty acid and mTORC1 are above every wild type).
* The opening of the IT12 README (its tables A and B, including group means and exact permutation p), the head of HELD_RESULTS_BY_GENE_derived.md, and statement snippets in investigations.tsv, the candidate cards and the claim registry.
* PMID 30290271 Results 3.5 and the Figure 6 legend (RNA-seq on neurospheres 2 KO v 3 WT; qRT-PCR on whole hippocampus 4 v 4). The "Aldaz/Kv7 sets" of the brief are this set: the matching trigger T19 carries it; Kcna2 is Kv1.2, not Kv7.

## Definitions
* **Inference**: a statement of direction, magnitude or enrichment about a gene, gene set or pathway, from a bulk transcript measurement (count or TPM table, or qRT-PCR reported with a bulk set) with **1 to 5 units in at least one arm** (unit = animal, organoid library or pool), that at least one consumer carries.
* **Consumer**: one research_portfolio row, one investigations.tsv row, one candidate card, one claim, one working-model or disease_model line, or one matching trigger. A consumer counts once per inference. Generated renderings, translations, shareable copies and result notes of the analysis itself are not consumers.
* **Counted** only after the hit is opened and read: a consumer that names the deposit without using the inference does not count.
* **Primary tier**: WWOX-deficient systems. **Secondary tier**: non-WWOX comparator deposits that a portfolio or investigation row uses with a direction; listed with animals and leave-out history, influence not computed in this task (cost cap, stated as a gap).

## Influence rule (applied to held per-unit tables only)
* Comparator and normalisation: those of the carried analysis where it states them (IT12 for GSE215425 sets; the folder's own script elsewhere); where only per-gene values are carried, log2 CPM or log2(TPM+1) as stated per row in the result table. Raw integer counts are normalised before scoring.
* Unit score: for a set, the mean over set genes of log2 expression centred per gene within the contrast; for a gene, its log2 value. Effect E = mean(mutant) minus mean(control).
* **Leave-one-out**: every unit of both arms is removed in turn (this includes the most extreme animal). Reported: smallest E_without / E, and whether any sign flips.
* **one-animal-driven**: some single removal flips the sign of E, or leaves less than 0.50 of E, or moves the statement across the threshold its source declared.
* **two-animal-driven**: P47T only, where ADV-233 already tested the flagged pair M6 and F8: the same rule with both removed. No other pair is searched (stated limit).
* **robust**: an arm of at least 3 on both sides and neither rule met. "Robust" means only that no single unit (and, for P47T, not the flagged pair) carries the effect; it does not mean the effect is significant, replicated, cell-resolved or causal.
* **not testable**: an arm with fewer than 3 units, a pooled library, or no per-unit value held. Where per-unit values exist with an arm of 2, report whether the two arms separate completely (descriptive, no disposition from it).
* A carried statement of "no change" or "flat" is not rescued by this rule: leave-one-out is reported, disposition "not testable for absence" if |E| < 0.20 log2.

## Ranking
Inferences ordered by the number of distinct consumers that lean on them (counted as above); ties by how many of those consumers are decisions about a compound or experiment.

## Predictions (recorded now)
* P1: among testable inferences from arms of 3 to 5, at least two thirds are robust to leave-one-out.
* P2: at least one carried inference outside the P47T hallmark sets is one-animal-driven.
* P3: no GSE156243 organoid inference is testable, because its control arm has 2 libraries.
* P4: the top-ranked inference (most consumers) comes from GSE156243, so the head of the ranking is "not testable" rather than "one-animal-driven".
* P5: the T19 set (PMID 30290271) is not testable (no per-animal value held).

## Rejecting observations
If every testable inference is robust and no consumer wording overstates its units, the audit's disposition is "no correction needed", stated as such. Stop at 120 minutes in two increments; anything not computed is listed as not computed.
