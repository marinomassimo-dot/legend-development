# WO-32 remainder: class IIa HDAC RNA along the oligodendrocyte lineage; predictions frozen before the extraction was run

2026-11-15, IT. Inputs: the two hash-recorded GEO tables already held (mouse GSE52564 cell classes: astrocytes P7, neurons P7, OPC P17, newly formed and myelinating oligodendrocytes P17, microglia, endothelial; human GSE73721 groups), extraction by the existing `targets_expression.py --genes HDAC4,HDAC5,HDAC7,HDAC9 --prefix wo32_classiia` and the existing join rule (floor 1.0 FPKM, 3-fold). Nothing has been run yet on these four genes by me; I do not remember values for them.
* F1: Hdac7 is below the 1.0 FPKM floor in OPC, newly formed and myelinating oligodendrocytes, and its highest class is endothelial. Missed otherwise.
* F2: Hdac9 is below the floor in at least two of the three oligodendrocyte-lineage classes. Missed otherwise.
* F3: Hdac4 or Hdac5 reaches the floor in at least one oligodendrocyte-lineage class. Missed otherwise.
* F4: no class IIa gene is "enriched" (3-fold over the best other class) in the oligodendrocyte lineage; at most one is neuron-enriched. Missed otherwise.
* F5 (case-level): the RNA result does not support "class IIa HDACs are expressed in the oligodendrocyte lineage at a level that would make their inhibition a myelin lever"; it is a bounded RNA answer, not an expression-of-protein or function answer.
RNA is not protein or function; a gene below the floor is unknown at the protein level, not shown absent.
