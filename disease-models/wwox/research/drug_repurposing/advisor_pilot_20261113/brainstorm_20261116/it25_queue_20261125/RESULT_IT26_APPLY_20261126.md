# IT26, 2026-11-26: apply report for the IT25 card queue

Hypothesis level; nothing here is medical advice; reference genotype class only. Orchestrator window `d26b0ae5`
(mandate ORCH-ROADMAP-IT59-20261119, step IT26).

## What was applied
`edits_it25.py` as it stands at this commit: 28 card edits (W01-W05, X01-X10, Y01-Y13) and 9 needs edits (N01-N09),
38 replacements (Y04 occurs twice), in 10 card packets and `needs/needs.json`; cards rebuilt by the bridge; then join, coverage, ranking,
views in every language (full and shareable), shareable package. Blind checks: readers A, B, C (IT25) and a fourth,
narrow one (packet D, sonnet, effort high; `BLIND_PACKET_D_IT26.txt`, `VERIFIER_REPORT_AS_DELIVERED_D_IT26.txt`) on the
places where IT26 departs from reader C.

## What changed against the prepared text
* **Reader C was wrong on one negative.** It wrote that Q230P has no held measurement. Johannsen 2018 (PMID 29808465)
  is held and reports transcript present and no detectable WWOX protein in one patient's fibroblasts. The reader had no
  PMID for it. The same false negative stood in card A01 `not_known/7` ("neither factor is measured for any WWOX
  allele") and in `needs.json` ("R is unmeasured for every WWOX allele"). All three are corrected.
* **Dated search behind the remaining negatives** (2026-11-26T00:12Z): `grep` for `Q230P|Gln230Pro|c.689A>C`,
  `P252A|Pro252Ala`, `P282A|Pro282Ala` over `research/deepdive_manifests/*.json` and `files/fulltext`,
  `files/supplement`. P252A: PMIDs 15266310, 24510053, 25612104, 41124647. P282A: 25612104, 30755385, 41124647. The one
  further measurement found: PMID 15266310 (SNU387, P252A of unknown zygosity, transcript and protein low). PMID
  25612104 and 30755385 carry genotypes only. PMID 21520031 (Pro282Ala, thyroid carcinoma) is recorded as unread in the
  PMID 25612104 manifest and was not opened. The card therefore says "No held measurement read for this card gives a
  calibrated value", not that none exists.
* **Packet D** (D1 and D4 MUST CHANGE, applied): P252A and P282A "at the empty-vector level in the function assays"
  overstated Zhang 2025 (non-significance, with intermediate means); "a boost multiplies the residual function and does
  not change it" read as a self-contradiction; "Bhlhe40 and Ndrg1 fall, Ddit4 and Ankrd37 flat" is false in cerebellum;
  the six-gene selective set was never named (now: Adm, Bhlhe40, P4ha1, Ankrd37, Ddit4, Egln3, from
  `p47t_it12_20261031/p47t_reanalysis_it12.py`). D2 and D3 additions applied.
* **Not settled:** the card's "+0.17 under a second normalisation" does not say which normalisation, and packet D could
  not check the set values; the US stiripentol label is not held.

## Per card: old sentence before and after, new sentence on the page
`BEFORE_AFTER_COUNTS_IT26.tsv`: for each edit, files/lines that held the old string at `7a0a8c450` and now (all 0 now),
over `cards`, `needs`, `join`, `coverage`, `ranking_it8_p9_20261029`, `view`. `new_full` / `new_shareable` = N means:
* not rendered by design: W02 (drug-assertion developmental stage), X05-X08 (disease-assertion notes), Y05, Y12, Y13
  (`functional_evidence_available`);
* W03: pharmacology is rendered on the full edition only;
* Y10: beyond the 360-character table clip of the novelty field. Y03 was first written with its verdict beyond that clip
  and was reordered so that the verdict shows.
`copied_card_sentences.py --base 7a0a8c450`: 20 card files, 106 replaced texts, 22 surfaces, 0 still held.

## Left as dated records, not edited
`therapeutic_hypotheses_ledger_current.md`, `missense_recovery_it5_p8_20261029/README.md` and
`commit_candidates/CC-20261029-INTEGRATOR-IT5-BATCH2-01.md` still carry "R is unmeasured for every WWOX allele";
`nmdar_pharmacology_it6_p9_20261029` is in the ADV-289 consumer queue.
