# ADV-209 result: MyeliMAP source check and the INV-06 estimand line (IT, 2026-11-24)

Pre-registration `PREREG_ADV209_IT_20261124.md` (written and committed on a task branch at 2026-11-24T10:36:57Z as 6286b3dd6, sha256 251412f1ec81dd3936f0fd7e8f608870a111d52452a5a107b9458a58bb9da3d3; the landing carries the same bytes, the branch was rebuilt on main after a ledger conflict), frozen before the paper body was opened. Hypothesis level; reference genotype class only; nothing is medical advice. No delegate, model call or spend; no ranking, drug or priority change.

Source: Ahuja et al., "MyeliMAP", Lab on a Chip 2026, 26, 1915-1929 (PMID 41664646, DOI 10.1039/d5lc01062d). Open-access PDF by a plain request to the institutional repository (HTTP 200, 3,082,910 bytes, 15 pages, sha256 e50d3739975ce742c0e8004beb0dfaf89541f220d038ed38f7fe27eb0bbc3114); text extracted with pdftotext; kept in scratch, not in git.

## Answer first
**HOLDS.** Every item of the pre-registered check is confirmed by the paper itself, so the INV-06 line is written with the numbers I read myself (labelled as graph readings) and at proposal level. One addition the pre-registration did not ask for and Codex's note does not carry: the authors themselves report that monocultures show MORE responses per microchannel than co-cultures and discuss it, with a reason other than selection under the speed estimator (see "What the authors say"). The paper neither shows nor excludes a responding-set effect on the speed summary.

## The seven items
| # | Check | Finding | Where |
|---|---|---|---|
| 1 | Week-8 speeds about 0.36 (co-culture) against 0.27 m/s (monoculture) | **Holds.** Fig 5e at week 8: co-culture about 0.36, monoculture about 0.27 m/s, three asterisks. Read from the plotted panel (page image), approximate. | Fig 5e |
| 2 | Responses per microchannel about 1.2 against 3.1 | **Holds** (within the pre-set tolerance). Fig 5c at week 8: co-culture about 1.2, monoculture about 3.15, four asterisks. Panel d (latency) about 6.05 against 7.45 ms. | Fig 5c, 5d |
| 3 | Replication | **Holds, with a nuance.** Legend: "N = 5 independent experiments (HD-MEA chips) with n = 15 PDMS microfluidic networks". Methods: the chip is the biological replicate and the three networks on it are technical replicates; "6-15 PDMS microfluidic networks per condition". The two excluded co-culture networks are named in Methods; the legend does not say whether n = 15 is before or after that exclusion. The test unit of the two-way ANOVA with Tukey is not stated. | Fig 5 legend; Methods |
| 4 | Methods: clustering, latency, path, exclusion | **Holds.** Each induced response is extracted "via a clustering algorithm" (the pipeline is cited to an earlier paper, not described here); latency is taken "at the beginning of the stimulation"; speed is distance over latency with the path "approximated to be 1960 um for all data points, based on the theoretical measurement of shortest possible path and longest possible path"; networks with defective stimulation (no artifact at any time point) were excluded: "two coculture PDMS microfluidic network". | Methods (electrophysiology analysis, statistics) |
| 5 | No WWOX perturbation, no tested drug | **Holds.** Human induced neurons with or without induced oligodendrocytes in a microfluidic platform; culture reagents only (doxycycline, a smoothened agonist in the oligodendrocyte medium); no WWOX and no tested compound. | Methods; whole paper |
| 6 | Same axon not identified across structural and electrical readouts | **Holds, and stronger.** Electron microscopy is shown only for co-culture, as representative images from N = 2 experiments with n = 6 networks (Fig 3), and the Discussion states that TEM showing unmyelinated axons is "data not shown"; the authors list TEM quantification across time points as future work. There is no monoculture electron microscopy and no pulse-to-axon linkage. | Fig 3 legend; Discussion |
| 7 | Availability | **Holds.** "The data supporting this article have been included as part of the supplementary information (SI)"; the analysis pipeline is by a DOI. The SI was not opened by me, so individual cluster and pulse records were not checked. | Data availability |

## What the authors say (not in Codex's note)
* "Neuron monocultures consistently showed a higher number of responses compared to cocultures, likely reflecting differences in axon excitability or axonal density"; the Discussion adds that the physical presence of the oligodendrocyte precursors "can partially obstruct axonal trajectories or alter their spatial distribution". So the authors read the larger response count as a difference in recruited or arranged axons, not as selection under the speed estimator, and they do not analyse the two together.
* The monoculture controls are in **separate devices**, because the axon-collecting channels differ in geometry and volume from the open chamber.
* Latency rises with repeated stimulation (their words: "progressive delay in spike propagation") and the direction of propagation was not analysed (backward propagation not excluded).
* Absolute velocities are lower than in comparable systems; the authors give three reasons (open chamber geometry, residual matrix layer, incomplete myelination) and say myelination was "partial rather than complete".

## Reading, bounded
* The faster plotted speed in the co-culture sits beside a smaller detected responding set at the same time point. The paper reports both and does not combine them. Whether the speed difference reflects faster conduction in the same axons or a different set of axons contributing responses is **not identifiable from the paper**: speed is latency at the start of the train over a fixed assumed path, the clusters are not tied to identified axons, and the structural and electrical readouts are not linked.
* Codex's stylised mixture arithmetic is carried only as an identification check, labelled as Codex's, and it does not reconstruct the paper's estimator (the pipeline is in a cited earlier paper that I did not read).
* A mean of per-response speeds need not equal the path divided by the mean latency (1,960 um over the plotted mean latencies would give about 0.32 and 0.26 m/s); I record this only as an arithmetic note, not as a discrepancy.
* Consequence for INV-06: a speed-only criterion is not recovery. Proposal level; no new apparatus; no compound promotion; the inosine dossier is untouched; the energy lead of the portfolio (abstract-only source) is untouched and not read here.

## Receipt
`RECEIPT_ADV209_MYELIMAP_IT_20261124.json` (coverage: abstract, results and discussion read; Methods read for the electrophysiology, analysis and statistics subsections and not for fabrication, culture, immunofluorescence and TEM preparation; figures captions_only with Fig 5 viewed as a page image; supplement not opened).

## Limits
Figure values are graph readings (approximate). The supplementary information was not opened. The cited analysis pipeline was not read. No author contact. Nothing here is about WWOX.
