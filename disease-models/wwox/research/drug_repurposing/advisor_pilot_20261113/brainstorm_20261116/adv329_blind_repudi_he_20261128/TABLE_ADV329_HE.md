# ADV-329: blind reading of Repudi 2021, Brain (PMID 33914858) for IT's ADV-328 (HE, 2026-11-28)

Reader: HE (ACTOR_ID plan), session 4441b7bf, claude-sonnet-5-5, effort high. One delegate (sonnet, effort medium) read the main text only
and was then stopped: the auto-mode classifier refused its Bash call, it wrote no file and read no supplement or image. The refusal is
recorded and was not retried or worked around. Everything below was read by HE.
Blind: IT's adv328 folder, its PREREG and ADV-314/315 tables were not opened. Extraction only; no claim; not medical advice.

## What was and was not read

| Source (files/fulltext/) | Read | sha256 (first 16) |
|---|---|---|
| PMID33914858_Repudi2021_Brain_operator_supplied.pdf, 17 pages, and its .txt | full text, all legends (text layer); Fig 1 legend is on PDF page 6 | 113522bb09b42a2d |
| supplement folder, File009 (supplementary figures and legends, text) | legends of Supp Fig 1, 4, 5, 6, 8; term search over the whole text | not hashed |
| File012.xlsx, File013.xlsx (RNA-seq tables), File014.xlsx (primers, antibodies) | read in full for the marker genes and the antibody list | not hashed |
| Figure images of the main article and the supplement | NOT VIEWED. Plot values (weights by age, bars) are therefore NOT READ | |

Page numbers: PDF page where checked; otherwise the journal pages printed (3061-3077), marked "journal".

## 1. Immunostaining and histology readouts

Terms searched (case-insensitive) over the main text and File009: parvalbumin, PV, NPY, neuropeptide, somatostatin, SST, GAD65,
GAD67, GAD, GABA, interneuron, Iba1, microglia.

| Readout | Result in the held text |
|---|---|
| PV, NPY, SST, GAD65/67 immunostaining or cell counts, any genotype | NOT PRINTED: no hit for any of these terms in the main text or File009 |
| Iba1 or microglia immunostaining | NOT PRINTED: no hit |
| Interneuron or GABAergic cell counts | NOT PRINTED: no hit |
| Antibody list (File014, sheet Antibodies, 10 primary) | CC1, WWOX, PDGFRa, NeuN, CNP, MBP, Tuj1, NG2, GFAP, Neurofilament H. No PV, NPY, SST, GAD or Iba1 antibody is listed |
| GFAP immunostaining | Supp Fig 1F only: loss of WWOX in astrocytes (GFAP-stained) of G-KO at P18, image; nothing counted or quantified in the legend |
| Other histology printed for conditional mice | below |

| Figure | Panel | Readout | Driver and genotypes | Age | Region | Unit | n | Statistic printed |
|---|---|---|---|---|---|---|---|---|
| Fig 4 | A | MBP, whole sagittal sections | S-KO vs S-Control | P18 | whole brain | image | not stated in the legend text read | none |
| Fig 4 | B,C | CNP and MBP fluorescence, sum intensity | S-KO vs S-Control | P18 | cortex | intensity | 3 vs 3 mice, three identical sections | text says "significant reduction"; P value NOT PRINTED in the text read |
| Fig 4 | D,E | CNP and MBP fluorescence, sum intensity | S-KO vs S-Control | P18 | cerebellum | intensity | 3 vs 3 mice | as above |
| Fig 4 | F,G | CC1+ and PDGFRa+ cells | S-KO vs S-Control | P17 | corpus callosum | cells per 0.5 mm2 | 3 vs 3, three sections each | mean ± SEM; * and ** marks; the threshold glyphs are garbled in the text layer |
| Fig 5 | EM | myelinated/unmyelinated axons per field, g-ratio | S-KO vs S-Control | P17 | corpus callosum, optic nerve | counts, ratio | 3 per genotype | ***P<0.001, t test |
| Fig 3 | F | snRNA-seq | S-KO vs S-Control | P17 | hippocampus | cell clusters | 1 vs 1 | none |
| Supp Fig 6 | A,B | CC1+ and NG2+ cells, corpus callosum | S-KO vs S-Control | P17 | corpus callosum | cells per 0.5 mm2 | 3 vs 3, three sections each | **P<0.01; legend prints S-KO 12±4 and S-Control 7±3 while it says "reduced" in S-KO: as printed, the direction does not match the numbers |
| Supp Fig 6 | C,D | CC1+ and NG2+ cells | S-KO vs S-Control | P17 | cerebellum | cells per 0.5 mm2 | 3 vs 3 | **P<0.01 |
| Supp Fig 6 | E | CC1 with cleaved caspase-3 | S-KO vs S-Control | P18 | brain sections | image | not stated | "no significant cell death", no count |
| Supp Fig 5 | A,B | MBP and Luxol fast blue | S-KO vs S-Control | P18 | sagittal sections | image | not stated | none |
| Supp Fig 5 | C | qRT-PCR of myelin genes | S-KO vs S-Control | P18 | cortex | fold change | 3 vs 3 | * P<0.05, ** P<0.01, *** P<0.001, t test |
| Supp Fig 5 | D-F | MBP, Luxol fast blue, EM | N-KO vs N-Control | P17 | sagittal, corpus callosum, cerebellum, optic nerve | image | not stated | none read |
| Supp Fig 8 | A,B | MBP | O-KO vs O-Control | P17 | brain, cortex | image | not stated | comparable signal, none |
| Supp Fig 1 | A-F | WWOX loss validation (NeuN, CC1, GFAP co-stains) | N-KO P16, S-KO P17, O-KO and G-KO P18 | as stated | cortex, cerebellum, corpus callosum | image | not stated | none |

Not found as histology in the text read: NeuN counts, CTIP2, TUNEL counts (NeuN appears only in the Supp Fig 1 validation images).

### Transcript readouts of the same markers (RNA-seq tables, not immunostaining)

File012 sheet "SKO_vs_S_Crtl_6_6_Crtx,hippo": S-KO vs S-Control at P17; the Fig 3A legend gives cortex 4 control and 3 S-KO, hippocampus 2 control and
3 S-KO, so the sheet's 6 vs 6 is this set (the sheet itself does not state it). File013 sheet "KO_WT_7_vs_7_unBatch": the design is NOT STATED in the
sheet; Supp Fig 4A counts hippocampi at P17 as 7 controls (wildtype 3, N-Control 2, S-Control 2) and 7 mutants (Wwox null 2, N-KO 2, S-KO 3), which matches the
7 vs 7 but is my reading, not a printed link. Values as in the tables (log2 fold change mutant over control; P, adjusted P):

| Gene | File012 S-KO vs S-Control | File013 KO vs WT (design not stated) |
|---|---|---|
| Pvalb | -0.75; P 2.6e-03; adj 3.4e-02 | -0.99; P 4.3e-08; adj 4.1e-06 |
| Sst | 1.06; P 5.2e-05; adj 2.6e-03 | 0.65; P 2.0e-02; adj 7.8e-02 |
| Npy | 1.89; P 3.4e-13; adj 4.3e-10 | 1.62; P 7.3e-10; adj 1.2e-07 |
| Gad1 | -0.18; P 0.26; adj 0.54 | 0.00; P 0.98; adj 0.99 |
| Gad2 | 0.52; P 1.8e-02; adj 0.12 | 0.23; P 8.1e-02; adj 0.21 |
| Vip | 0.08; P 0.75; adj 0.90 | 0.04; P 0.86; adj 0.92 |
| Gfap | 1.68; P 4.8e-04; adj 1.1e-02 | 1.65; P 2.1e-10; adj 3.7e-08 |
| Aif1 (Iba1) | 0.30; P 0.42; adj 0.69 | 0.35; P 0.29; adj 0.49 |

## 2. Blood chemistry, glucose, body weight, survival (Fig 1, PDF page 6)

| Datum | Line | Age | n | Statistic printed |
|---|---|---|---|---|
| Blood glucose, serum or blood chemistry | any | any | none | NOT PRINTED: "glucose" occurs only in slice-physiology solutions (10 mM), "serum" only in culture media and blocking solutions (text of the main article and File009 searched) |
| Body weight over time, Wwox-null (germline, not conditional) | Wwox-null vs WT | growth gap "from 4 days onwards"; image P18 | 3 vs 3 | mean ± SEM; ** P<0.01, *** P<0.001 t test (Fig 1B); weights by day NOT READ (plot) |
| Body weight, N-KO | Nestin-Cre | image P17 | 4 per genotype | mean ± SEM; ** and ***, t test (Fig 1E); values NOT READ |
| Body weight, S-KO | Synapsin I-Cre | image P17 | 4 per genotype | mean ± SEM; ** and ***, t test (Fig 1H); values NOT READ |
| Body weight, O-KO and G-KO | Olig2-Cre, GFAP-Cre | image P17 | the legend text after panel K was not read in full | "no weight loss" per legend (Fig 1K,N) |
| Survival, Wwox-null | germline | death by 3-4 weeks | WT 10, KO 11 | P=0.0023, log-rank |
| Survival, N-KO | Nestin-Cre | death by 3-4 weeks | N-Control 12, N-KO 14 | P=0.0002 |
| Survival, S-KO | Synapsin I-Cre | premature death (3-4 weeks) | S-Control 13, S-KO 15 | P=0.0001 |
| Survival, O-KO | Olig2-Cre | no lethality | O-Control 11, O-KO 10 | P=1.0 (second hand: the main-text read by the delegate; the legend end was not read by HE) |
| Survival, G-KO | GFAP-Cre | no lethality | G-Control 8, G-KO 9 | P=1.0 (same note) |
| Spontaneous seizure duration, S-KO | Synapsin I-Cre | P14-18 | 6 | 68.5 ± 13.4 s (delegate reading of the main text; not re-checked by HE) |

## 3. Drivers and ages

| Line (as printed) | Driver | Cells the paper says it deletes in | Ages studied |
|---|---|---|---|
| Wwox-null | germline | all | P18 images; weights from day 4; survival; RNA-seq hippocampus P17 |
| N-KO | Nestin-Cre | neural stem/progenitor cells | P16 (validation), P17 (MBP, LFB, EM, weight), survival |
| S-KO | Synapsin I-Cre | neurons | seizure onset P9; recordings P13-17 and P14-18; RNA-seq, snRNA-seq, EM, CC1/PDGFRa/NG2 at P17; MBP, CNP, qRT-PCR, caspase at P18 |
| O-KO | Olig2-Cre | oligodendrocyte lineage | P17-18 |
| G-KO | GFAP-Cre | astrocytes | P18 |
All conditional lines carry the Rosa26 loxP-STOP tdTomato reporter; background mixed C57BL6/J;129sv; controls named S-Control, S-HT (flox/+ with Cre), N-Control, O-Control, G-Control (delegate reading of the Methods, not re-checked).

## Limits

- No figure image was viewed: values drawn only in plots (weights by day, bar heights, Fig 4 P values) are NOT READ.
- The "NOT PRINTED" lines for markers rest on term search over the text layers of the main text and File009 and on the File014 antibody list; a marker shown only inside an unlabeled image would not be found this way.
- Rows marked delegate reading were not re-verified by HE.
