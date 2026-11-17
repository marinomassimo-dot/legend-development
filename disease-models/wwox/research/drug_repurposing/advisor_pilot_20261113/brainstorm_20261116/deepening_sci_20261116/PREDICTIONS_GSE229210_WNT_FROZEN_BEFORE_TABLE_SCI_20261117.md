# Prediction frozen before the table is opened: GSE229210, Wnt readouts under WWOX overexpression (SCI, 2026-11-17)

Non-canonical. Exploratory. Not medical advice. Label: TRANSFER (a direction from a held organoid knockout result, tested in a different system). Not a rescue contrast, not a deficiency model, not a progenitor, not evidence about any individual.

State of the data at freezing: the GSE229210 CPM table has not been opened by this session; the repository records it as "public file not yet fetched" (it24 O10) and the rescue-dataset search of 2026-11-17 downloaded no matrix. If it turns out that someone opened it earlier, this file says so in the result and the score is labelled accordingly.

## Question
Held: in 4 knockout against 2 wild-type week-15 organoid libraries (GSE156243), the four transcriptional Wnt readouts are 4 of 4 up and the wider seven 7 of 7 up (`research/drug_repurposing/gse156243/prediction_wnt_sign_20261025.md`), with composition and maturation not separable. Does the mirror hold in a composition-free system: when WWOX is overexpressed in low-WWOX glioma lines (T98G, U87MG, U251MG, DBTRG-05MG; 3 cultures per arm per line), do the same readouts go down against the empty-vector arm?

Why this system at all: it has no cell-type composition to shift, so a cell-autonomous direction is not confounded by maturation. What it cannot give: a deficiency state, a neural-progenitor identity, or a statement about the organoid thread (the organoid thread is parked until a rescue contrast exists).

## Fixed before opening the table
- Sign hypothesis under test: overexpression lowers the readouts (mirror of the knockout-up result). A rival is no direction, or the opposite direction.
- Readout set R4: AXIN2, LEF1, NKD1, APCDD1. Wider set R7 adds TCF7L2, WNT5A, CTNNB1.
- Unit: a cell is one (line, gene) pair. Per cell: log2((mean CPM of the three OE cultures) + 1) minus log2((mean CPM of the three vector cultures) + 1). If the table is promoter-level, tags are summed per gene by the table's own gene assignment before this step; a gene without an assignment is "unmeasured".
- Expressed filter: a cell counts only if the mean CPM is at least 1 in at least one of its two arms. Cells failing it are "unmeasured" and are not counted for or against.
- Primary statistic: S = (cells in R4 that are expressed and have log2 difference below 0) divided by (cells in R4 that are expressed). Secondary: the same for R7, and the number of cells with absolute log2 difference at least 0.5.
- Null for significance: 1,000 random gene sets of the same size, matched on expression decile, as in the GSE156243 run. Reported as an orienting figure. With three cultures per arm no per-gene test is claimed.
- Outcome classes (exhaustive, by the primary statistic):
  - P (mirror holds): at least 8 expressed R4 cells and S at least 0.75.
  - M (mixed or flat): at least 8 expressed R4 cells and S between 0.25 and 0.75.
  - O (opposite): at least 8 expressed R4 cells and S at most 0.25.
  - U (unmeasurable): fewer than 8 expressed R4 cells (these genes are near-silent in glioma lines).

## Probabilities, written before the data
| Class | My probability | Naive baseline |
|---|---|---|
| P | 0.30 | 0.25 |
| M | 0.35 | 0.25 |
| O | 0.10 | 0.25 |
| U | 0.25 | 0.25 |

Scoring: the natural log of the probability assigned to the observed class, in nats; naive is ln(0.25) = -1.386. A positive difference means this prediction beat the naive one. Not tuned afterwards.

Basis of the numbers, labelled: INFERRED that AXIN2, LEF1, NKD1 and APCDD1 are often weakly expressed in glioma lines, which is why U carries 0.25; ASSUMED (recalled, not re-read in this session) that the literature has WWOX acting on Dishevelled and so against canonical Wnt signalling; the direction is therefore a transfer and its prior is held below 0.5 on P alone.

## What each class would and would not change
- P: a composition-free direction consistent with the organoid result; it raises, modestly, the chance that the organoid Wnt-up is partly cell-autonomous. It still does not make Wnt a lever, does not revive the organoid thread, and carries no drug claim.
- M: no information on direction; the organoid Wnt-up stays unresolved between cell-autonomous and composition.
- O: the sign does not transfer across these lines, or the organoid Wnt-up is mostly composition or maturation. It would strengthen, not prove, the composition reading.
- U: closes the item in one line; revival would need another dataset.
- No class changes a need, a card, a direction or a ranking by itself.

## Limits that travel with any result
Tumour-derived lines with low WWOX for reasons that may include other lesions; overexpression is not the mirror of loss; one series, one laboratory; CAGE counts, not RNA-seq; three cultures per arm; the empty-vector arm controls the virus, not the tumour background; no replicate independence beyond the cultures.

## Result
Not yet run.
