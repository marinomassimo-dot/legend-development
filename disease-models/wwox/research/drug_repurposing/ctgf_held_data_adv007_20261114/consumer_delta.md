# ADV-007 consumer delta (proposals for the integrator; nothing here was applied)

| # | Consumer | Proposal | Ground |
|---|---|---|---|
| 1 | `ranking_it8_p9_20261029/investigations_it20.tsv`, INV-06 `next_test`/`evidence_available` clause "IPOTESI; the Wwox-CTGF link is unsupported." | Optional replacement: "IPOTESI; no held Wwox expression datum supports a Wwox-CTGF link independent of cell composition (ADV-007): the one human KO organoid rise (CTGF +1.3 log2, 4 v 2 libraries) is of the size a progenitor-state shift alone would carry, and the mouse bulk contrasts disagree in sign; expression is not secretion." | `README.md` answer, `per_table.tsv` |
| 2 | INV-06 X1 (b)/(c) arm specification | No change from held Wwox data. If a candidate product is named in the positive-control or neutralisation arm, cite the neuron-specific Tsc literature of SCI50 as the ground, not a Wwox datum. | README "What it changes" |
| 3 | `signature_it23_20261103/composition_class.tsv` and its generator `reproduce_dseqr_cmap_comparison.py` | The 15 rows with blank log2fc/rho (symbol renames) carry default zero flags. Propose a dated Update line in that package's README naming the 15 genes and the cause; regenerating would change query QD/QF membership by up to 15 of 834 genes and is the package owner's call. Computed here for CCN2 only (rho -0.009). | `output/symbol_trace.tsv` |
| 4 | SCI50 README DREAM section | Disposition: executed, closed with this reason (appended by SCI as a dated Update line; no cell edited). | this package |
| 5 | IT open-questions map | No new row. OQ11 (null-neuron medium) stays the decisive measure. | README |

Corrections after delivery, if any, will be sent to everyone who received this version and will name what they replace.
