# SCI47 package B — pre-registration: is the KCNQ2 neuron attribution of the mouse table also seen in an independent human cell-class table? (2026-11-12; committed before any value of the new resource is read)

Non-canonical research material. Not medical advice; no compound; no claim on WWOX. Reference genotype class only. RNA only: not protein, not current, not function.

## Why this case (chosen over the other two of the mandate)
* **The decision it can change.** Kv7 (KCNQ2/3) lever designs (IT46 S3/R5, lever L5 of package A) assume the channel sits in the recorded neurons. The two held tables disagree: mouse P7 neurons Kcnq2 30.68 FPKM (two pools; astrocytes 0.22) against the human table's single neuron sample KCNQ2 0.10 FPKM (n = 1; fetal astrocytes 4.30, mature cortical astrocytes 0.73; KCNQ3 16.80 in the same neuron sample). An attribution of the lever to neurons, or its restriction to one species or stage, depends on which table is typical. A third, independent human table can say whether the single sample is an outlier.
* **Not chosen:** the NRF2 panel (the SCI46 table is already decision-complete for its purpose; only its wording is corrected, below); the neuron-versus-glia attribution of GABA levers (needs age-resolved P13-17 data that no small processed table offers; stated as a perimeter, not analysed).

## Question (narrow)
In an independent processed human brain cell-class table, is KCNQ2 higher in neuronal classes than in glial classes?

## Sample, context and resource (metadata checked before download)
Human Protein Atlas, `rna_single_nuclei_cluster_type.tsv.zip` (5,254,086 bytes; SHA-256 b24e46d48e12a8c2944cfe3c48191d62b1c93f207cd8f78d6a942d5ed7870edf; downloaded 2026-11-12 by plain curl; columns Gene, Gene name, Cluster type, nCPM; 49 cluster types, multi-region adult human brain nuclei; **one pooled value per gene and cluster type; no donor or replicate level**). Not P7, not P13-17, not cortical layer II/III, not a WWOX-deficient cell. nCPM is a normalised count scale and is **not** comparable with the FPKM of the Zhang tables: only the order and ratios inside each table are compared.

## Genes (fixed now)
KCNQ2, KCNQ3, KCNQ5 (the channel; KCNQ5 as context). Class controls: SNAP25, RBFOX3, SLC17A7, GAD1 (neuronal), GFAP, AQP4 (astrocyte), P2RY12 (microglia), MBP (oligodendrocyte), PDGFRA (OPC). Identifiers: HGNC symbols as served in the table; a symbol absent from the table is reported "not in table" (not zero); a zero is reported as zero.

## Classes
Neuronal: cluster types named excitatory, projection neurons, interneurons or neurons (all listed, region-specific ones marked as such). Glial: astrocytes, bergmann glia, microglia, oligodendrocyte progenitor cells, oligodendrocytes. The forebrain classes (forebrain excitatory, forebrain projection neurons, cge/mge derived interneurons, other excitatory neurons, pvalb+ excitatory neurons) are the closest to the cortex in this table; they are named, not assumed to be layer II/III.

## Comparison and rule (written before the run)
Per gene: the highest value among the forebrain neuronal classes against the highest value among the glial classes.
* **Supports a neuron attribution in both species at RNA level:** KCNQ2 forebrain neuronal maximum at least 3 times the glial maximum, and at least 1 nCPM (both thresholds exploratory conventions of this note, not detection limits and not universal).
* **Contrary result:** KCNQ2 forebrain neuronal maximum below 3 times the glial maximum, or below 1 nCPM. Then the species discrepancy stands as unresolved and a human check of the recorded cell class is required before the Kv7 lever is transferred to human tissue.
* **Controls:** the neuronal control genes must be highest in neuronal classes and GFAP/AQP4 in astrocytes; if not, the table is not read for KCNQ2.
* **Zhang local input check:** the raw value of KCNQ2 in the human neuron sample of the held input is looked up; if it is exactly the loader's floor (0.10 shown for 0 or below-limit values), it is reported as a floor value of that table, not as an expression level.
No statistics: one value per class, nuclei are not replicates. Results are descriptive.

## What this cannot settle (stated now)
Age (adult nuclei against P7 and P13-17), layer, protein, current, and the Wwox genotype. The missing measure is an age-matched, layer-resolved Kcnq2/Kv7 readout in the recorded cell class (immunolabelling or in situ at P13-17, or the Kv7-blocker-sensitive current in the same cells as the sIPSC programme).
