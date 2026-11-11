# SCI44 coda — K-channel RNA by cell class: predictions fixed before the run (2026-11-11)

Non-canonical research material. No claim on WWOX; no compound; RNA is not channel number, current or share. Written and committed **before** `kchan_expression.py` is run; the predictions are the Orchestrator's priors from background knowledge, unverified, and are scored against the output without change.

## Question
Which cell classes express the channel genes behind the K+ shares discussed in SCI43 and SCI44 (KATP, Kir2, Kir4.1, K2P, Kv7, HCN, GIRK), in the same processed public tables already used for the PDK isoform question (mouse cortex GSE52564, human GSE73721; local copies, input hashes recorded)? It decides which classes a Ba2+ or KATP drug effect in a slice could come from (the glia caveat of package C) and whether a neuronal KATP arm is expressed at all in the mouse neurons.

## Data (local, no download)
Mouse cortex per-sample FPKM, GSE52564 (sha256 of the tar 4cb522fb...), P7 neurons, astrocytes, microglia, endothelium, P17 OPC, newly formed and myelinating oligodendrocytes (two samples each); human table GSE73721 (sha256 140f376a...): neurons (n=1), mature astrocytes (12), fetal astrocytes (6), oligodendrocytes (5), myeloid (3), endothelium (2). Class means; floor 0.1 FPKM for ratios.

## Predictions (scored held / failed / not testable)
* **P1** Kcnj11 and Abcc8 are detected (>= 1 FPKM) in mouse neurons; Abcc8 neuron >= astrocyte.
* **P2** Kcnj10 (Kir4.1) astrocyte >= 10 x neuron in mouse and in human.
* **P3** Kcnj8 and Abcc9 (Kir6.1, SUR2) are highest in endothelium or astrocytes, below neurons in neither... (stated as: neuron < max(endothelium, astrocyte) for both genes, mouse).
* **P4** Kcnk1 (TWIK-1) astrocyte > neuron in mouse and human; Kcnk2 (TREK-1), Kcnk3 and Kcnk9 (TASK-1, TASK-3) each detected (>= 1 FPKM) in mouse neurons.
* **P5** Kcnj2 (Kir2.1) neuron >= astrocyte in mouse.
* **P6** Kcnq2 and Kcnq3 neuron >= 3 x astrocyte in mouse; Hcn1 neuron >= 3 x astrocyte in mouse.

## What each result would mean
* P1 held: the neuronal KATP arm has an expressed substrate in the mouse preparation (a precondition, not a share). P1 failed: the KATP arm needs a different cell class or age.
* P2 held and P4 (TWIK-1) held: a Ba2+ or K2P-blocker difference in a slice has an astrocytic route in both species; a neuronal attribution needs synaptic blockade and a cell-specific control.
* P3 held: Kir6.1/SUR2 are vascular or glial; the neuronal KATP is Kir6.2/SUR1.
* Nothing here changes a rank; RNA only, small n (two pools per mouse class; one human neuron sample).
