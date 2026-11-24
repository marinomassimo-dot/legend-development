# Inosine after activity in WWOX loss

context_policy: QUESTION_DRIVEN

**Disposition.** Defer oral inosine for a pediatric WWOX trial. Healthy mouse neurons make use of endogenous inosine during recovery. The entry of additional inosine is a separate, transporter-sensitive process. Adult human data show central exposure to urate and a renal adverse-event signal. A parent concentration in pediatric brain sufficient for neural rescue has yet to be established.

## Imported and internally generated inosine behave differently

In the published mouse dentate gyrus study, we recalculated within-mouse differences from the authors’ normalized mass-spectrometry data. For each mouse the transporter interaction is the change after stimulation or added substrate under 8MDP minus the corresponding change under vehicle. Each comparison uses its own baseline. The two panels represent different challenges. We did not pair animals across panels or estimate a between-panel interaction. [Primary study, Fig. 4a and Extended Data Fig. 4b](https://pmc.ncbi.nlm.nih.gov/articles/PMC10626993/) · [All recalculated contrasts](slice_comparison.tsv)

| Pentose phosphate signal | Mice | Median change with vehicle | Median transporter interaction (range) |
|---|---:|---:|---:|
| Addition of 100 µM inosine | 6 | +0.369 | −0.576 (−1.166 to −0.095) |
| KCl depolarization | 6 | +0.640 | +0.071 (−0.571 to +0.449) |

All six mice showed attenuation of the added-substrate response under transporter blockade. With depolarization the sign of the interaction split three to three. This agrees with a predominantly intracellular source under stimulation. Combined transporter inhibition does not identify which isoform carries the exogenous substrate. Tissue ion signals include multiple cell types and compartments.

A separate tracer experiment used **1 mM ribose-labelled inosine with 9 mM glucose**. Exogenous ribose entered glycolytic intermediates even with glucose available. Depolarization increased the normalized M+5 pentose phosphate signal in six of six mice (median paired change +0.282) while pentose phosphate carbon enrichment fell by a median 12.42 percentage points across the six mice. The unlabeled signal also rose in all six. This illustrates how dilution by endogenous carbon can lower fractional enrichment while labeled signal rises. Neither measurement alone estimates the rate of ATP synthesis. Five of six mice had paired phosphoenolpyruvate enrichment values; missing entries were excluded only for this contrast. Separately, after depolarization and recovery, PNP inhibition lowered the phosphocreatine signal in nine of nine mice (median paired difference −0.314 normalized units). This establishes a role for the endogenous reaction under the study conditions. It leaves the net effect of oral substrate on function unresolved. [Primary Fig. 4d–f, 5g–i and tracer methods](https://doi.org/10.1038/s42255-023-00890-z)

## What the human neural comparator resolves

Human iPSC-derived neurons incorporated nitrogen from 50 µM labeled **hypoxanthine** into ATP within 5 minutes. With 100 µM hypoxanthine, PRPP declined and the measured ATP pool showed no significant increase. Following mitochondrial uncoupling, 20 µM hypoxanthine alone failed to produce a significant ATP or total adenylate increase relative to recovery medium after 18 hours. Figure 7A also includes an inosine arm and separates several stereoisomeric pentoses. A labeled ATP molecule can therefore reflect replacement within a fixed pool. In the previous primary astrocyte study, added adenine and glucose materially changed the response to inosine. The cell systems, stresses, substrates and times differ. [Human neuronal experiments, Figs. 3, 6 and 7](https://pmc.ncbi.nlm.nih.gov/articles/PMC11342100/) · [Astrocyte comparison](README.md)

## Untreated WWOX datasets and a discriminating observation

| Gene | Human cerebral organoid, 2 control / 4 KO libraries | Mouse cortex, 4 / 3 | Mouse hippocampus, 2 / 3 |
|---|---:|---:|---:|
| SLC29A2 (ENT2) | −0.36 | −0.40 | −0.41 |
| PNP | +0.09 | −0.79 | −0.59 |
| HPRT1 / mouse Hprt | +0.29 | +0.00 | −0.60 |
| PGM2 | −0.23 | −0.19 | −0.69 |
| ADSL | −0.32 | −0.08 | −0.43 |

Values are KO minus control mean log2(1 + normalized expression). The two mouse regions come from the same study. The earlier ENT2 result motivated the panel. Among the additional genes, ADSL stays negative after omission of each library in each model. The two mouse PNP decreases reverse in the human organoid. PGM2 retains a negative sign across the full comparisons, although the cortical omission range crosses zero. In a separate juvenile hippocampal nuclei dataset, Pgm2 in astrocyte-marker nuclei changed from 62.3 to 32.0 CPM, whereas excitatory-marker nuclei changed from 14.0 to 16.0 CPM. Single pools per genotype preclude animal-level inference. The total Adsl rate changed from 15.0 to 13.7 CPM. Expression cannot establish enzyme activity, substrate limitation or an ADSL-deficiency diagnosis. [Bulk and omission results](salvage_bulk.tsv) · [Nuclear counts](cell_types.tsv) · [Composition sensitivity](mixture.tsv)

**Reopening test.** Compare separately base-labeled and ribose-labeled inosine with a hypoxanthine comparator at measured neural exposure in WWOX-deficient and corrected neuron–astrocyte cultures. Match developmental state, starting glucose, adenine and stimulus burden. Record absolute IMP, adenylosuccinate, AMP, ADP and ATP alongside isotopologues, phosphocreatine, viability and recovery of evoked transmission. If entry is limiting, added inosine should label intracellular products weakly despite preserved endogenous pentose production, and verified intracellular hypoxanthine delivery should partly bypass that defect. Accumulation of labeled adenylosuccinate with weak AMP formation would direct attention to the ADSL step, with selective enzyme activity and substrate-chase data needed to assign causality. If ribose reaches glycolysis with little net adenylate or functional recovery, its use as fuel explains tracer uptake. Glucose deprivation is unnecessary for this alternative. Prioritization would require a reproducible net functional and pool advantage in WWOX models at a credible exposure.

## Human exposure and pediatric feasibility

* In a five-person acute oral study, identified plasma hypoxanthine, xanthine and urate rose after ingestion. The accessible primary abstract gives no quantitative parent peak or assay limit for parent. A later trial’s statement about undetectable parent increase cites this earlier study; it is not an independent time course. Blood handling can itself generate inosine and hypoxanthine before separation. [Original acute study, abstract](https://pubmed.ncbi.nlm.nih.gov/11912550/) · [Human sample-processing comparison](https://pmc.ncbi.nlm.nih.gov/articles/PMC11670813/)
* A study in healthy adult men included three participants on inosine alone for 14 days. The authors report no rise in measured blood parent or ATP in this group. Fig. 3 shows day 1 and day 15 ATP/ADP for groups A–D. In a separate five-person combination cohort blood ATP rose 13.8%. Whole-blood extract, a cointervention, small groups and sparse sampling limit inference. Table 2 contains **urinary** purines. [Methods and Results, pp. 172–179](https://doi.org/10.6032/gnam.41.171)
* In SURE-PD, 44/75 adults gave a CSF sample, once at week 12, 2.5 hours after dosing. CSF **urate** was 40% and 50% higher in the two inosine arms versus placebo. This between-arm result supplies neither a paired CSF change nor an inosine exposure. In SURE-PD3, 17/147 inosine recipients and 4/149 placebo recipients experienced kidney stones, with 18 and 4 events, respectively. The reported event-rate ratio was 4.92 (95% CI 1.66–14.6). Participants had early Parkinson disease; absolute risks in children with WWOX disease remain unknown. [Phase 2, Fig. 2 and Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC3940333/) · [Phase 3, Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC8441591/)

The adult oral capsule studies do not establish an age-appropriate pediatric formulation, a free parent brain concentration, or compatibility with background antiseizure medicines and ketogenic regimens in WWOX. Parent, hypoxanthine and urate need separate timed assays. A change in serum urate or a decrease in seizure counts alone would not resolve the proposed mechanism.

## Reproduction

Run `python3 -B salvage_screen.py /path/to/legend/files OUTPUT_DIRECTORY` with the laboratory-held GEO/Ensembl inputs for [organoids](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243), [cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682), [hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) and [hippocampal nuclei](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158684). Run `python3 slice_comparison.py INPUT_DIRECTORY` with openpyxl and the publisher’s spreadsheets saved as MOESM5.xlsx, MOESM6.xlsx and MOESM10.xlsx. Outputs are summary contrasts. Each uses only mice with all required values for that contrast. [Fig. 4 workbook](https://static-content.springer.com/esm/art%3A10.1038%2Fs42255-023-00890-z/MediaObjects/42255_2023_890_MOESM5_ESM.xlsx) · [Fig. 5 workbook](https://static-content.springer.com/esm/art%3A10.1038%2Fs42255-023-00890-z/MediaObjects/42255_2023_890_MOESM6_ESM.xlsx) · [Extended Data Fig. 4 workbook](https://static-content.springer.com/esm/art%3A10.1038%2Fs42255-023-00890-z/MediaObjects/42255_2023_890_MOESM10_ESM.xlsx)
