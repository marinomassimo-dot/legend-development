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

## Result (appended 2026-11-17 after the run; everything above this line is unchanged and was frozen in commit 47eba936e)

**Class M (mixed or flat).** 10 expressed R4 cells, 5 down, S = 0.50. Scored class probability 0.35: ln(0.35) = -1.050 nats against the naive ln(0.25) = -1.386, a difference of +0.336 nats in favour of this prediction. Scored by class alone, separate from every other line of this session. Label: TRANSFER. Not a rescue result.

Source: `GSE229210_CPM_all_samples.txt.gz` from the GEO FTP supplementary folder (plain client, empty User-Agent, no contact parameter), sha256 `05fe94a4525b8252dcc3eb173bbf552c5dee5030b95bf6c1972a9918bf4301a3`; 43,037 gene rows keyed by versioned Ensembl gene ID, 24 sample columns (4 lines x vector or WWOX x 3). The table was not opened by this session before freezing; no earlier opening is recorded. Not a FULLTEXT_READ_RECEIPT case (a deposited matrix, not a paper). Script `run_gse229210_sci_20261117.py`, output `result_gse229210_sci_20261117.json` (same folder).

Gene mapping (not in the frozen text, a mapping step): symbols to Ensembl IDs through the public Ensembl REST xrefs endpoint on 2026-11-17: AXIN2 ENSG00000168646, LEF1 ENSG00000138795, NKD1 ENSG00000140807, APCDD1 ENSG00000154856, TCF7L2 ENSG00000148737, WNT5A ENSG00000114251, CTNNB1 ENSG00000168036, WWOX ENSG00000186153. The table has no symbol column.

| Gene | DBTRG-05MG | T98G | U87MG | U251MG |
|---|---|---|---|---|
| AXIN2 | unmeasured | -0.01 | -1.02 | +0.39 |
| LEF1 | +0.06 | -0.17 | +0.29 | +1.10 |
| NKD1 | unmeasured | -0.45 | unmeasured | unmeasured |
| APCDD1 | unmeasured | -0.73 | unmeasured | +0.35 |

Cell value: log2(mean OE CPM + 1) minus log2(mean vector CPM + 1). Down cells: AXIN2 x2, LEF1 x1, NKD1 x1, APCDD1 x1 = 5 of 10. Cells with absolute difference at least 0.5: 3 (U87MG AXIN2 -1.02, T98G APCDD1 -0.73, U251MG LEF1 +1.10).
Wider set R7: 22 expressed cells, 12 down, S = 0.55; 7 cells with absolute difference at least 0.5. TCF7L2 -0.39, +0.34, -0.31, +0.40; WNT5A +0.85, +0.38, -0.81, +0.60; CTNNB1 -0.04, -0.57, -0.17, -0.44 across the four lines in the column order above.

Orienting null (1,000 random sets of four genes, each drawn from the same decile of mean CPM across the 24 samples as the corresponding readout; seed 229210): mean S 0.44; the share of random sets with S at least as high as observed 0.40, at most as high 0.69. The observed S is inside the null.

## What this does and does not say
- No direction. The lines disagree gene by gene and line by line (U87MG and T98G lean down, U251MG leans up, LEF1 up in three of four lines). By the frozen table this changes nothing: the organoid Wnt-up stays unresolved between cell-autonomous and composition.
- **The dose is small, and this is the main limit.** Post-hoc manipulation check, not frozen: WWOX itself is up by log2 0.45, 0.35, 0.71 and 0.16 in DBTRG-05MG, T98G, U87MG and U251MG (about 1.1 to 1.7-fold in CPM; baseline CPM 21 to 43). A mild increase in a line that is not WWOX-null is a weak probe of a readout, so class M may reflect too small a perturbation as much as an absent effect. It is not a test that could have refuted the mirror strongly, and I do not claim it refutes it.
- Three of four readout genes are near-silent in two or three of the four lines (NKD1 expressed in one line, APCDD1 in two, AXIN2 in three); the readout set is thin in this system, as the U class anticipated, although 10 cells passed the filter.
- Revival condition for this item: a dataset in which WWOX is restored in a WWOX-null neural line or organoid (E-MTAB-14792, if released, or a new deposit). The organoid Wnt thread stays parked on that condition, as before.
- Limits carried from the frozen text: tumour-derived lines, overexpression is not the mirror of loss, CAGE counts, three cultures per arm, no per-gene test claimed.
- Not medical advice; no need, card, direction or ranking changes.
