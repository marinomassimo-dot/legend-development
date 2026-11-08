# Delta for the session that owns the needs and the generator (not applied by this pass)

Prepared 2026-11-08 by `plan`. Each item is exact text and a place; none is applied, and none changes a direction, a card or a ranking. Source of every sentence: [`README.md`](README.md) and the files it cites.

## A. Line identity (a lost qualifier) — `needs/needs.json`

1. `NEED-WNT-BETA-CATENIN`, observation `O3`, field `limits`, append:
   `The composition panel is of the JH-iPS11 iPSC knockout (clones WKO-1C and WKO-2C) in PMID 42397075 (scRNA-seq, week 16; immunostained SOX2-positive share graded WT about 13, patient lines about 43-48, knockout about 77 percent at week 7, hand readings of Figure 1F); the bulk deposit of O1 and O4 is the WiBR3 hESC knockout of PMID 34268881. Different parental backgrounds: the 2026 composition does not adjust the 2021 bulk, and the 2026 text reports a similar imbalance in the WiBR3 knockout at week 15 only by immunostaining (Supplementary Fig. 4I-J, not held).`
2. `NEED-WNT-BETA-CATENIN`, `counter_evidence`, third string ("Patient-derived lines … within about 0.3 of wild type on cell composition"): add at the end `That is the week-16 scRNA fraction; at week 7 the immunostained SOX2-positive share is intermediate in both patient lines, so they are a graded comparator, not a composition-matched control.`

## B. One sentence for the ten needs that lean on `GSE156243` — field `notes`

Needs: `ISR-ATTENUATION`, `PDH-PYRUVATE-AXIS`, `LACTATE-LDH`, `MITOCHONDRIAL-RESPIRATION`, `INHIBITORY-HYPOFUNCTION`, `GABA-CHLORIDE-GRADIENT`, `WNT-BETA-CATENIN`, `MTOR-AUTOPHAGY`, `NEUROINFLAMMATION-GLIA`, `REDOX-NRF2` (list and per-need counts: `needs_human_neural_systems.tsv`). Append to each, identical wording:
`Its human-neural transcript rests in part on the week-15 bulk organoid deposit GSE156243 (WiBR3 hESC knockout, 4 libraries against 2), whose composition differs from wild type and cannot be separated from genotype by adjustment (gse156243/independent_reanalysis_wnt_vs_maturation_20261025.md). Where this need names a gene set from that deposit, a within-cell-type contrast of the single-cell record E-MTAB-14792 (a different background, JH-iPS11; one library per condition in the preprint methods; not accessible) would replicate or fail to replicate it; see DL-MECH-181.`
`MTOR-AUTOPHAGY` and `REDOX-NRF2` have no composition or maturity caveat in the observation text read by the keyword pass; check by reading before adding.

## C. Open questions and searches

* `RS-NP3B2` (reopen search for the gene-level add-back data): extend the "decision at stake" with `and, once released, a within-radial-glia contrast of the knockout, SCAR12-class and WOREE-class libraries for the gene sets of the ISR, glycolysis, OXPHOS, Wnt, NRF2 and GABA-marker needs (DL-MECH-181)`.
* `WO-04`, `WO-07`, `WO-09`, `NR-03`, `NR-04`, `WO-36`: add the pointer `see DL-MECH-181 for the single-cell route that does not need new wet-lab material`.

## D. Generator and ranking

Nothing to change. If a ranking or generator reads "human neural transcript, two systems" as independent support for ISR, PDH or lactate rows, note that the two systems (bulk organoid; shRNA hNPC, one library per arm) are each composition- or stage-sensitive and neither is composition-independent; the only axis with a composition-independent human observation in the repository is MYC. Whether the generator reads that field is for the owner to check.

## E. Before and after

Not shown. No consumer has applied any of these. A run of the generator or a fresh searcher after the owner applies A to D is the way to show a change.
