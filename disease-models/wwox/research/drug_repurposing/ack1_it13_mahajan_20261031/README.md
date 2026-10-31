# IT13 P1: Mahajan 2005 closed in the module (receipt, interpretation, N12, trigger R3, design controls)

Orchestrator, task `ORCH-ROADMAP-IT13-20261031`, 2026-10-31 (Europe/Rome evening). Exploratory, non-canonical, **not medical advice; not a statement about any compound**. Reference genotype: a WWOX-DEE genotype class; no individual-level record.

## Decision first

| Question | Answer |
|---|---|
| Is the reading of PMID 16288044 now registered? | **Yes.** `FTR-20261031-16288044-01`, `complete_fulltext_read`, source = the operator-supplied AACR PDF (sha256 `6339ef85...d35`, kept in the local gitignored corpus `files/fulltext/PMID16288044_Mahajan2005_CancerRes.pdf`, **not** in the public repository). Work manifest `deepdive_manifests/PMID16288044.json` passes the strict validator. |
| What does the coverage map say, and what does it not? | Abstract, Introduction, Methods, Results, Discussion read; every numbered figure (1-8) inspected as an image (Figs 1-3 at 110 dpi, 4-8 at 130 dpi), with panel-level locators for Fig 4D-F, 5, 6B, 7B and 8. No tables and no limitations section exist in the paper. **Supplementary Figs S1-S2 are cited and unavailable.** Linearity of the Wwox bands (Fig 5E, 8A) was not assessed. |
| Which locators are used? | All rendered-page attestations, because the PDF text layer carries six control characters in Methods (the multiplication sign of cell counts) and the validator refuses such a surface (rule 5d). The text was not hand-corrected. |
| What changed in the module? | N12 (uncarded) loses 'abstract only; full text not obtained' and carries the reconciled reading; trigger R3 is satisfied **as to the source** and its remaining datum is stated as absent from the source; the design controls become explicit requirements (`controls_ack1_it13.tsv`). |
| Did any priority move? | **No.** N12 stays INSUFFICIENT, uncarded, no unit; no group moved; reading a paper is not a result. |

## What the original supports (see `experiments_mahajan2005.tsv`, one row per experiment)

- Supported, in overexpressed non-neural cells with an engineered activated kinase (caAck = L487F, C-terminally truncated): Tyr phosphorylation and a polyubiquitin smear on full-length Wwox (Fig 5D); Y33F is still phosphorylated and ubiquitinated (Fig 6B); Tyr287 is the **predominant, not the only**, phosphorylation site by pTyr signal of Tyr-to-Phe mutants (Fig 7B); lower Wwox with higher phospho-Ack1 across 16 tumours versus 16 benign prostates (Fig 8, correlation).
- **Not shown**: that Y287F resists ubiquitination or degradation (no such panel); that activated Ack1 shortens Wwox half-life (Fig 5E has no lane without activated Ack1, one time point, no quantification); that the route is proteasomal (Fig 5F shows MG-132-revealed ubiquitin only, no level rescue; the paper cites another group for proteasome-dependent accumulation of a truncated Wwox); that an ACK1 inhibitor raises WWOX (the only inhibitor is geldanamycin on Hsp90, and Wwox is not measured); anything in neurons, Q230P or G372R.
- Therefore the chain ACK1 -> Tyr287 -> polyubiquitination -> degradation is **partly demonstrated and partly inferred**; it is not compressed into a demonstrated causal chain.

## Consumers reconciled (and what was deliberately left alone)

| Consumer | Edit |
|---|---|
| `ranking_it8_p9_20261029/uncarded_items.tsv` N12 | the Mahajan clause and the 'waits for the full text (R3)' clause replaced by the reconciled reading; the rest (Xie 2015 limits, counter-evidence, substrate census) untouched |
| `recovery_it10_p23_20261031/reopen_searches.tsv` R3 (source of the R3 trigger row) | verdict and trigger state that the full texts were read and that the decisive datum (WWOX level after an ACK1 inhibitor) is absent from both sources; reopen only on a new datum |
| `ack1_it11_p24_20261031/design_it11_p24.md` | dated correction note on top (Y287F is to be interrogated, not assumed insensitive; no-activated-ACK1 chase arm; route arm with level read-out; presence gate); body untouched |
| `ack1_it12_mahajan_20261031/README.md` | dated note that the receipt proposal is executed |
| ranking, view, shareable edition | regenerated through the pipeline (see the closing record); no group move expected and checked |

The six controls are **specific to the ACK1/WWOX case**; they are not new general rules for drug repurposing.

## Limits

Not examined: supplement; Fig 5E and 8A linearity; the identity of the senior author beyond initials in the group count. The 2022 Nature Communications ACK1-CSK paper and the 2024 Aurora B report are handled in `ack1_probes_it13_p15_20261031` (reading depth stated there; the 2024 paper at abstract level only).
