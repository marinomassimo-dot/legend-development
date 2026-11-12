# SCI46 queue item (data analysis): is the NRF2 axis present, and where, by cell class? Predictions fixed before the run (2026-11-12)

Non-canonical research material. Not medical advice; no compound; no claim on WWOX. RNA only: class means of FPKM, two animal pools per mouse class, one human neuron sample; RNA is not protein, nuclear localisation, activity or current. Inputs already on this disk from earlier work (no download in this item): GSE52564 (mouse cortex purified classes, Zhang 2014) and GSE73721 (human classes, Zhang 2016); input hashes are recorded by the script and compared with those in `kchan_expression_sci44_20261111/*.tsv`. This file is committed before the script is run; it is not edited afterwards.

## The new question, and the decision it can change
SCI46 (README of `keap1_nrf2_sci46_20261111`, T01 and M-K1) names **target presence per cell class** as the bridge no source supplies: are KEAP1, NFE2L2, a target-gene panel and the fumarate receptor HCAR2 present in the neuron and in the astrocyte, and is a **neuron-specific target-gene readout above the floor of a bulk measurement**? Decision: whether the INV-08 X0/X1 target-gene readout can be read in a neuron-enriched or mixed culture (then a per-cell-class readout is a refinement) or only in a sorted or imaged cell class (then it is a requirement), and whether the HCAR2 arm of the fumarate comparison belongs to microglia only.

## Genes (fixed)
Mouse symbols (human in capitals): Keap1, Nfe2l2, Nqo1, Hmox1, Gclm, Gclc, Txnrd1, Srxn1, G6pdx (human G6PD), Gsr, Gpx4, Slc7a11, Fth1, Hcar2, Bach1, Gsk3b, Btrc, Wwox; markers Rbfox3, Gfap, Cx3cr1 (mouse and human), Mog for myelinating oligodendrocytes. A gene absent from a table is reported absent, not zero.

## Rules
Detected = class mean at or above 1 FPKM. "Higher" = class mean at least twice the other, both values reported. One human neuron sample cannot support a class difference by itself: human statements are marked single-sample. Classes: mouse neurons (P7), astrocytes (P7), microglia, OPC (P17), newly formed and myelinating oligodendrocytes (P17), endothelium; human neuron, fetal and mature astrocytes, microglia, oligodendrocytes and other classes as present.

## Predictions (recollection and inference; unverified; scored unchanged)
* **NP1.** Nfe2l2 and Keap1 are detected in mouse neurons, astrocytes, microglia and OPC.
* **NP2.** Nqo1 is higher in mouse astrocytes than in neurons (the astrocyte-selective ARE activity of the tBHQ study, abstract, is the only basis).
* **NP3.** Hmox1 is highest in mouse microglia among the seven classes.
* **NP4.** Hcar2 is detected in mouse microglia and not in neurons or astrocytes (below 1 FPKM in both).
* **NP5.** Nqo1 in mouse neurons is below 5 FPKM and in astrocytes above 20 (a neuron-specific target readout would be near the floor of a bulk measurement).
* **NP6.** Keap1 and Nfe2l2 do not differ by a factor of two between mouse neurons and astrocytes.
* **NP7.** In the human table the single neuron sample has NQO1 below the astrocyte classes (same direction as mouse; single sample).
* **NP8.** Wwox is detected in mouse neurons and astrocytes and is higher in neurons than in astrocytes.
* **NP9 (descriptive).** G6pdx and Gclm are detected in all four main mouse classes; no direction is predicted.
