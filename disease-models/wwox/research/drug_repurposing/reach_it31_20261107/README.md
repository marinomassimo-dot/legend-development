# IT31 P7a: where the knowledge on contrasting compounds sits, and who reads it

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class. Read-only counts over files already in the module; nothing was generated or ranked. Regenerate: `python3 reach_it31.py > reach_it31.tsv`.

## Answer first
1. DATO: the forward generator reaches the known pan-class-I deacetylase inhibitor reference **without being given its name**: stage row `IT21P2-0031` (conditional harm-arm, chain HDAC5 to SLC2A1 from two deposit origins counted once). It stops at hand-over on `main_target_weak_attribution` (Ki at HDAC5 3,600 nM against 1.3 nM at HDAC1, a mixed-measure comparison). So the reverse test "does the engine arrive at it from the seeds" is passed for this compound, and the same row shows why the generator is right to hold it.
2. DATO: that compound has **no card, no investigation row and no conditional question**. What LEGEND holds in documents about its other arms (class-level reasons, the HDAC3 counter-premise carried on the myelin endpoint) reaches the stage rows only as carried limits.
3. DATO: of the 14 compounds in the table, 2 are in the stage proposals (the reference above and one barbiturate, which also has a card) and none of the others is. The literature-derived layer (cards, conditional questions, investigations) holds 11. This repeats at compound level the finding of IT30 (1 of 22 compounds in both layers): the transcript-seeded generator and the literature pharmacology describe different compounds.
4. DATO: levetiracetam appears in no layer of the module (cards, stage, conditional questions, investigations); it occurs only in older analysis notes. The seizure comparators of P8 therefore start from a gap, not from a card.
5. INFERENZA: a join "stage proposal to card or conditional question by compound" would touch 2 of 14 rows. It is not built: the yield is too small to justify code, and the real limit is the data (compound-only effects carry no target to sign, IT29 case 2), not a missing script.
6. Not shown: any predictive skill. This table is presence and consumption, not a test of whether proposals work; recovery of a compound already known to LEGEND is a function check, not a discovery.

## Table (`reach_it31.tsv`)
Columns count rows or files that name the compound: stage proposals (IT21 stage, `generation_it30_p5_20261105/results_s11`), hand-over, the case-1 comparison, IT30 conditional questions, investigations, cards.

## Consequence for the queue
No change to ranking or cards. Two actions follow and are carried in the IT31 record: P8 package on seizure comparators (levetiracetam, ethosuximide, perampanel and the antiseizure agents named in WWOX-related reports, with sources for any usage figure), and the HDAC5 premise row proposed in `inv_drafts_it31/` (P4).
