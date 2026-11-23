# Ethosuximide, WNT signaling and cortical fate in WWOX loss

**Research decision, 23 November 2026.** Three WNT markers respond to direct ethosuximide exposure. A broader, independently defined WNT3A signature fails to transfer to the same treated library (rank 126/218). The evidence supports a marker-specific lead. In ordinary mouse cortical cultures exposed to 700 µM ethosuximide for eight hours, the three reliably measured WNT readouts rose together. Across 218 treatments, the panel ranked third using our count-based calculation and **tied for second** after processing by the study authors. Both calculations used the same single treated library. The corresponding WNT readouts were already elevated in untreated human WWOX-null organoids. Simple transcriptional reversal is therefore a poor rationale at this stage. Whether the drug increases or reduces the yield of surviving cortical neurons in the WWOX condition remains unresolved. [Hadwen et al.](https://doi.org/10.1093/hmg/ddy221) · [Earlier disease-side analysis](../gse156243/independent_reanalysis_wnt_vs_maturation_20261025.md)

## The direct drug observation

A previous ethosuximide study in rat hippocampal neural stem cells reported enhanced proliferation and differentiation, with functional perturbations implicating PI3K/Akt/Wnt at 100 µM. The mechanistic connection we tested was that this action might reinforce an already elevated WNT program in developing WWOX-deficient tissue. The independent drug screen used mouse mixed cerebrocortical cultures at DIV21. These preparations differ in exposure, stage and lineage. [Tiwari et al., primary study](https://pubmed.ncbi.nlm.nih.gov/26420483/) · [Direct ethosuximide sample](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2983478)

| WNT readout | Median control CPM | Drug minus median vehicle, log2 | Authors' robust z after technical correction |
|---|---:|---:|---:|
| AXIN2 | 16.77 | +0.062 | +2.10 |
| NKD1 | 7.14 | +0.511 | +1.21 |
| APCDD1 | 8.94 | +0.402 | +1.90 |
| LEF1 | 0.19 | −0.097 | Below our coverage floor; excluded |

The mean over eligible genes was +0.325, against leave-one-vehicle-out values from −0.219 to +0.212. Median-ratio normalization gave +0.337. Only 51 of 10,000 random triplets matched for baseline expression and control variation achieved a value at least as large. The drug exceeded 215 of the other 217 agents and 14 of the 15 other agents in its library identifier block. On the authors' screen, which removes four principal components, one drug had a higher mean z and a second tied with ethosuximide at the displayed precision. None of the three individual gene results had an adjusted P value below 0.83. Shared technical effects, the selected panel and the lack of a treated biological replicate limit both ranks. A three-gene RNA change cannot establish nuclear β-catenin activity or dependence on WNT signaling. [Count results](results/drug_summary.tsv) · [Specificity calibration](results/drug_specificity.tsv) · [Author processing](results/author_processing.tsv) · [Author-based rank](results/author_rank.tsv)

## The regional-fate prediction fails

We applied marker panels from an independent day-21 human neural organoid perturbation study to the week-15 WWOX knockout. A classical posterior shift would lower telencephalic progenitor markers and raise at least one posterior or diencephalic progenitor panel. Instead **all four progenitor panels increased**. The CNS-neuron panel decreased. Quantities are WWOX knockout minus control mean differences on log2(CPM + 1), four vs two libraries. They measure marker expression in whole tissue.

| Marker panel | Eligible genes | WWOX difference | Range after omitting a library |
|---|---:|---:|---:|
| Telencephalic progenitors | 11 | +0.286 | +0.245 to +0.341 |
| Diencephalic progenitors | 10 | +0.272 | +0.148 to +0.395 |
| Hindbrain progenitors | 6 | +2.085 | +1.131 to +3.039 |
| Spinal cord progenitors | 6 | +1.196 | +0.636 to +1.756 |
| CNS neurons | 11 | −0.146 | −0.214 to −0.077 |

Each mean also retained its sign on dropping a gene. A higher relative progenitor contribution or altered expression within cells could generate this pattern. The source diencephalic markers include cortical hem. Bulk RNA cannot resolve regional cell counts or total neuronal yield. [GSE156243](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Transferred markers](results/disease_markers.tsv) · [Checks](results/disease_scores.tsv)

The GSK3 inhibitor CHIR99021 also produced different lineage outcomes across human organoid conditions. In the HES3 SMG2 series (days 0–9; eight organoids per concentration; endpoint day 21), the odds of a telencephalic progenitor among sampled cells relative to control decreased at 0.6 and 1 µM (each OR about 0.13), were unresolved at 1.4 µM and increased at 1.8 µM (OR 6.16). In another experiment, H9 CHIR_E gave strong telencephalic depletion and hindbrain enrichment (OR 14.25). Retinoic acid also produced this joint direction in some conditions. The source's cell-level enrichment tests and their adjusted P values do not quantify uncertainty across independent organoids. CHIR acts on GSK3, has a different mechanism from ethosuximide, and its concentrations cannot be converted into ethosuximide concentrations. These outcomes explain why elevation of a transcriptional pathway cannot by itself predict regional benefit or harm. [Sanchís-Calleja et al., Fig. 2, Supplementary Fig. 1 and Table 3](https://doi.org/10.1038/s41592-025-02927-5) · [All source contrasts, including XAV939](results/reference.tsv)

In a post-primary check, the WWOX peripheral-progenitor panel rose (+0.199, five eligible genes). Neither neural crest nor peripheral neuronal panels met the four-gene coverage floor. Among the high CHIR conditions the reference supplies no PNS-progenitor row linking that specific finding to the drug proxy. The lack of a row is an unavailable comparison. This sensitivity supplies no alternative regional match. [Post-primary rules](sensitivity.md) · [Peripheral-lineage transfer](results/peripheral_scores.tsv) · [Source comparisons](results/peripheral_reference.tsv)

## Broader WNT response from human neural progenitors

We selected 20 upregulated and 20 downregulated genes after WNT3A stimulation in human primary neural progenitors (75 donor pairs, 48 h), excluding all four markers that motivated follow-up. CHIR reproduced the sign for all 37 genes with usable estimates (74 pairs). Co-treatment with XAV reversed 20/20 available increased genes and 12/18 decreased genes relative to WNT3A alone (six pairs). The latter arm showed little median reversal. The experiments share donors. Two column labels in the published workbook are misleading. Reading G/H as mean abundance/log2 fold change, consistent with the description sheet, exactly reproduces the reported 762 WNT3A and 3,031 CHIR genes at the authors’ thresholds. [Matoba et al., Fig. 1 and Supplementary Table 3](https://www.nature.com/articles/s41593-024-01773-6) · [Frozen prediction](npc_prediction.md) · [Reference checks](results/npc_reference.tsv)

In the mouse drug screen, both independently defined arms increased (+0.168 and +0.139 log2 units). The signed score was +0.015, inside the nine-vehicle range of −0.061 to +0.069. Ethosuximide ranked 126/218 overall and 4/16 in its sample-ID block. Matching identical symbols or requiring a unique HGNC→MGI association gave the same 9 up-arm and 12 down-arm genes. The marker result lacks support for a broad 48-hour progenitor-like program in this 8-hour cortical exposure. An early neuronal WNT response remains a separate possibility. [Drug results](results/npc_drug.tsv) · [Gene coverage](results/npc_coverage.tsv)

In untreated human WWOX-null organoids only 5/20 increased and 12/20 decreased genes passed the detection filter. The first arm missed the frozen minimum of eight. The exploratory score was −0.035 and changed sign on library omission. Fifteen assignments, with gene eligibility fixed to the observed control pair, describe sensitivity only. These data cannot resolve direction in the WWOX preparation. [Disease-side estimates](results/npc_disease.tsv)

## Shorter exposure in a neuronal reference

A temporally closer comparison used primary rat hippocampal neurons at DIV14, stimulated with Wnt3a for four hours in three matched experiments. A different panel selected the 20 strongest nominal P values in each direction and omitted the original four markers. The reference itself is strongest for induced genes. Only one selected induced gene and zero repressed genes passed 5% FDR. In the mouse drug data the acute score ranked 17/218 by matching symbols and 12/218 by rat→human→mouse gene identifiers, both second of 16 in the block. The scores (+0.037 and +0.057) remained inside the respective vehicle ranges. Both arms rose, so the prespecified joint response failed. [Primary study and Table 3](https://doi.org/10.1155/2016/4672841) · [Frozen rules](rat_acute_prediction.md) · [Reference strength](results/rat_acute_reference.tsv) · [Drug result](results/rat_acute_drug.tsv)

The induced arm alone ranked 4/218 and 2/218. Eight of 11 orthology-mapped genes rose. Removing one gene at a time moved the unilateral rank from first to fifteenth. Even this arm's +0.129 was inside its leave-one-vehicle-out range (−0.232 to +0.204). A partial early neuronal response is worth checking in independent cultures. Its strength relative to other drugs and its magnitude relative to controls answer different questions. [Unilateral sensitivity](results/rat_acute_up_only.tsv)

## Independent review of the original three genes

On 23 November at 09:56 UTC the laboratory reviewer acknowledged completion against revision 2a5845cbc. The independent recalculation confirmed third of 218 from the counts, tied second after the authors' correction and second of 16 within block HI.3140. All nine vehicle libraries came from other blocks. Within-block centering against other treated conditions yielded global ranks 3–5. Matching decoys additionally on pairwise gene correlations gave 16/1,017 at or above the observed score. Without NKD1 the primary rank dropped to 22/218. These sensitivity calculations support replication of a small early response. GEO documents one treated library and one replicate per compound; how many physical wells fed that library is undocumented. Earlier references to a single well in the predictions should be read as a single observed library. The reviewer retained the existing priority of ethosuximide as a WWOX candidate. [Reviewed revision](https://github.com/marinomassimo-dot/legend-development/tree/2a5845cbc/disease-models/wwox/research/drug_repurposing/ethosuximide_wnt_fate_20261123) · [GEO design](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE110256)

## A direct nuclear β-catenin test limits the lower-concentration claim

An orthogonal assay tested ethosuximide itself (PubChem CID 3291, substance 170464802) in WNT3A-conditioned mouse C2C12 cells. The measured nuclear β-catenin stimulation was **−0.3% at 2 µM and +0.2% at 10 µM**, below the authors’ 40% activity threshold at either concentration. The screen median was +0.7% at each concentration across 2,509 tested substances (2,500 distinct identified compounds). The same assay detected methotrexate (+41%, +74%) and rotenone (+43.8%, +92.8%). These are values reported as percent activity by the depositor; they do not represent percentages of responding cells. [PubChem AID 1117326](https://pubchem.ncbi.nlm.nih.gov/bioassay/1117326) · [Lee et al., assay definition](https://doi.org/10.1371/journal.pone.0130796) · [Derived screen distribution](results/nuclear_screen.tsv) · [Compound rows](results/nuclear_controls.tsv)

**What it rules down.** A readily detectable, broadly acting potentiation of nuclear β-catenin at 2–10 µM is unsupported in this cell type. A context-dependent, higher-exposure neural effect remains possible: the rat progenitor work used 100 µM and the cortical three-marker result used 700 µM. The distinction has an empirical comparator. Riluzole was also inactive in the C2C12 nuclear assay (−0.8%, +0.7%), although an independent human iPSC-progenitor study measured WNT3A-dependent potentiation of a TCF/LEF reporter, with a reported EC50 around 5 µM. Nuclear accumulation and transcriptional reporter activity probe different steps in different cells. That comparison demonstrates a possible source of discordance; it gives no direct human reporter result for ethosuximide. [Zhao et al., Fig. 5](https://pubmed.ncbi.nlm.nih.gov/22923789/) · [Direct compound records](results/nuclear_controls.tsv)

A relevant follow-up would measure nuclear β-catenin and TCF/LEF transcription in the same neural preparation and exposure series, with genotype, vehicle and pathway controls. Pairing these with cortical neuron yield would establish whether any engagement is linked to a WWOX-relevant developmental outcome. The current direct evidence does not justify increasing the candidate’s overall priority.

## What would change the decision

**Working prediction.** If the developmental action depends on where a progenitor starts on the WNT response curve, identical ethosuximide exposure could increase neuronal yield in a WNT-low compartment while having little benefit or a detrimental effect on cortical fate in a WNT-high compartment. Classify cultures by pretreatment canonical WNT activity independently of genotype, then compare the within-lineage change in absolute surviving cortical neurons per starting progenitor between WWOX-null and isogenic cultures. Measure nuclear β-catenin and cycling alongside neuronal yield, and compare with both a WNT-normalizing condition and another agent matched for reduction of network activity. Recovery of absolute cortical-neuron yield at verified exposure without further WNT elevation in the deficient compartment would favor developmental benefit through another route. A rise restricted to progenitor number or marker-positive percentages would leave that question open. No WWOX-deficient preparation in these datasets received ethosuximide. [Prior four-gene drug test](../ethosuximide_cortex_20261123/README.md)

## Reproduction and permissions

The [initial rules](prediction.md) were committed before extracting new expression values, enrichment odds or marker rankings. Supplementary Tables 1 and 3 of Sanchís-Calleja et al. (2025) were used under CC BY 4.0; this is a new selection, calculation and interpretation by the LEGEND laboratory. Only derived summaries and original code are distributed. Source checks used selected primary methods, reported endpoints, the figure design and data tables.

Download the [GSE110256 counts](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE110nnn/GSE110256/suppl/GSE110256_combined.count.txt.gz), [sample annotations](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE110nnn/GSE110256/matrix/GSE110256_series_matrix.txt.gz), [Table 3](https://pmc-oa-opendata.s3.amazonaws.com/PMC12904787.1/41592_2025_2927_MOESM5_ESM.xlsx), [Table 1](https://pmc-oa-opendata.s3.amazonaws.com/PMC12904787.1/41592_2025_2927_MOESM3_ESM.xlsx), and [WWOX series](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243). Pass the paths to each script in that order. Python 3 and NumPy suffice.

```bash
python3 analyze.py "$DRUG_COUNTS" "$DRUG_META" "$TABLE3" "$TABLE1" "$WWOX_COUNTS" results
python3 sensitivity.py "$DRUG_COUNTS" "$DRUG_META" "$TABLE3" "$TABLE1" "$WWOX_COUNTS" results
python3 author_rank.py "$AUTHOR_TABLES" results
```

For the independent processing check, use Gene Symbol in the [authors' public application](http://bigbear.med.uottawa.ca:1000/apps/mouseCorticalRNA-app/). Select Axin2, Nkd1 and Apcdd1 in turn. Keep the full positive and negative z ranges including outliers. Copy both tables for each gene into a tab-separated file with that symbol as its name. The script handles duplicate displayed zeros, enforces 218 unique drug conditions and uses decimal values for ties. [Input hashes](results/sources.tsv)

The broader analysis uses factual numerical inputs locally from the [authors' Table 3](https://static-content.springer.com/esm/art%3A10.1038%2Fs41593-024-01773-6/MediaObjects/41593_2024_1773_MOESM5_ESM.xlsx). The workbook and its contents remain with the authors and publisher. The repository provides the original analysis, gene eligibility and derived summaries. For the cross-species check, supply the HGNC complete set snapshot and NCBI mouse gene_info listed in the [input manifest](results/npc_inputs.tsv).

```bash
python3 npc_transfer.py "$NPC_TABLE3" "$DRUG_COUNTS" "$DRUG_META" "$HGNC" "$MOUSE_GENE_INFO" "$WWOX_COUNTS" results
```

For the acute neuronal comparison download the [public author supplement](https://pmc-oa-opendata.s3.amazonaws.com/PMC5223035.1/4672841.f1.zip) and [rat NCBI gene_info](https://ftp.ncbi.nlm.nih.gov/gene/DATA/GENE_INFO/Mammalia/Rattus_norvegicus.gene_info.gz). The PMC record marks the article open access but supplies no license code. The source files are not included. The [manifest](results/rat_acute_inputs.tsv) identifies the locally analyzed version.

```bash
python3 rat_acute.py "$RAT_SUPP_ZIP" "$DRUG_COUNTS" "$DRUG_META" "$HGNC" "$MOUSE_GENE_INFO" "$RAT_GENE_INFO" results
```

For the nuclear assay, download the [complete PubChem assay CSV](https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1117326/CSV) and run `python3 nuclear_reporter.py assay.csv results`. The deposited study is open access. We report selected factual measurements and our own summaries. [Input checksum](results/nuclear_input.tsv)
