# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-238) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the findings:** `advisor_pilot_20261113/brainstorm_20261116/adv233_p47t_two_animals_sci_20261125/RESULT_ADV233_P47T_TWO_ANIMALS_SCI_20261125.md` (SCI, leave-two-out on the P47T forebrain deposit; section 5 proposes the wording) and `p47t_it12_20261031/premises.tsv` row P8 (IT12, 2026-10-31).
**Status:** PROPOSED, for the next `BATCH_COMMIT` that the queue triggers. No registry, card or dossier file is edited by this act; the ordinary-route wording (IT6 P4 README row 5, IT12 README, a map line) is applied separately and is not part of this candidate.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS (stated before any apply)
**MINOR.** Wording only: three sentences that state a P47T forebrain transcript enrichment as holding "in all three regions" gain the qualifier that it is carried by two of five mutant animals. No claim, grade, ranking row, number or experiment structure changes.

## 2 · What and why
SCI's ADV-233 removed the two animals (M6 and F8) that IT12 had already flagged on 2026-10-31 for activity-gene outliers and re-ran the carried hallmark enrichments: **on q < 0.05 TNFA_VIA_NFKB is met in no forebrain region without them (cortex reverses; M6 alone is enough), IL6_JAK_STAT3 and HYPOXIA lose q < 0.05 in some or all regions but keep a positive score in all three regions (about three quarters of the full score); GLYCOLYSIS stays in all three.** [Qualified by ADV-239 (SCI, 2026-11-25): the first draft of this sentence said 'met in no region' without the threshold.] The repository states the first two as "positive in all three regions" and the third as an in-vivo anchor. A consumer that quotes the three-region statement without the qualifier overstates it. The wording below is the same for every consumer: the enrichment is a **state of two of five mutants**, not shown to be genotype-wide, and not shown to be a pathway.

## 3 · Proposed wording, consumer by consumer (read before listing: each hit below was opened in place)
| # | Consumer (file, location) | Current text | Proposed wording |
|---|---|---|---|
| 1 | `drug_repurposing/cards/J01_glial_reactivity_modulation.card.json`, `/input/p4_card/evidence_for_and_against/for[1]` (and its packet and the view's copy) | "A regulator-level inflammatory signature is positive in three forebrain regions of the P47T homozygote." | append (SCI's wording, ADV-239 section 4): " TNFA/NF-kB rests more than half on animal M6 (cortex reverses without it). IL6/JAK/STAT3 loses the q threshold without M6 and F8 but keeps its sign and about three quarters of its enrichment score." |
| 2 | same card, `/input/p4_card/novelty_for_woree` item (4) | "...the regulator-level inflammatory inference there does not rest on those canonical transcripts (absence from a thresholded list is not a measurement)." | append: " The TNFA part also rests on one or two animals (ADV-233, ADV-239)." |
| 3 | `drug_repurposing/cards/K01_hif_axis_glycolytic_shift.card.json`, `/p4_fields/functional_evidence_available` (sentence beginning "In vivo, partial loss (IT12 P2-P47T)") | "...the hallmark HYPOXIA, GLYCOLYSIS and APOPTOSIS gene sets are enriched in the mutant in PFC, cortex and hippocampus..." | append at the end of that sentence group: " Leave-two-out (ADV-233): GLYCOLYSIS stays enriched in all three forebrain regions without M6 and F8; HYPOXIA keeps q < 0.05 only in hippocampus but keeps a positive score in all three regions (ADV-239)." |
| 4 | `fulltext_dossiers/PMID36828035.md` lines 117 to 118 (item 7, `DATO`) | "...TNFA/NFκB, IL6-JAK-STAT3 and INFLAMMATORY_RESPONSE enriched in all three." | append: " [This is the paper's own statement. A leave-two-out re-run on the deposit (ADV-233, 2026-11-25) finds the TNFA enrichment lost without two of the five mutants (cortex reverses) and IL6-JAK-STAT3 below q 0.05 but sign-stable.]" |
| 5 | `locator_audits/2026-10-29_it6_p10_verifier.md` row 10 | "P47T regulator inference positive in all three forebrain regions ... SUPPORTED" | none: a dated audit of what the paper says, not of the repository's use of it; add only a pointer line "see ADV-233" if the batch wants one |
| 6 | `p47t_it12_20261031/proposals/k01_card_text_proposal.md` | the unapplied K01 text proposal | pointer line to the ADV-233 survival result (the card text proposal was applied to the card as item 3) |
| 7 | `research_portfolio.tsv` row RP-036 | see section 4 | patched by ADV (the portfolio is ADV's) |
Read and found **not to carry the three-region inflammatory inference**: `simulation_it23_p3_20261103/README.md` (network simulation with RELA and STAT3 nodes; no P47T statement), `needs/needs.json` (RELA gene record), `analysis/mechanism_intervention_map.md` line 574 (area fractions; "only Il6, not Tnf-a" is a qPCR statement), `session_evaluations/2026-11-24_sci-ac_adv216.md` (SCI's own note of the finding).

## 4 · RP-036 exact sentence (for ADV to patch)
Append to the RP-036 row's state text: "Per animal, all three cerebellar mutants exceed every wild type on the cholesterol, fatty acid and mTORC1 set scores (leave-two-out not testable with three mutants); forebrain mTORC1 enrichment is lost in cortex and prefrontal cortex without M6 and F8 (ADV-233)."

## 5 · What this does NOT do
No claim, grade or ranking change; no change to what IT12 concluded about K01 and L01 (its own text already named M6 and F8 in the hypoxia paragraph); no protein-level or phospho-STAT3 datum is created; the authors' upstream-regulator tool was not re-run.

## 6 · Statements for the blind check at propagation time
1. In ADV-233's `disposition_adv233.tsv`, on q < 0.05 TNFA_VIA_NFKB and IL6_JAK_STAT3 are met in no forebrain region without M6 and F8, HYPOXIA in hippocampus only, GLYCOLYSIS in all three; and in ADV-239's `gsea_loo_adv239.tsv` the scores of IL6_JAK_STAT3 and HYPOXIA stay positive in all three regions without the pair, TNFA reverses in cortex.
4. **Further consumers and wording:** ADV-239 RESULT section 4 (SCI) gives wording for K01, J01, L01, F02, F03, INV-06, INV-15, INV-16, T19 and CLAIM 005; it is to be taken into this candidate at propagation, after the blind check, and none of it is applied here.
2. The J01 card sentence quoted in row 1 and the K01 card sentence quoted in row 3 exist verbatim at the stated locations.
3. M6 and F8 are named in `p47t_it12_20261031/premises.tsv` (P8) and in its README section 5 (dated 2026-10-31).
