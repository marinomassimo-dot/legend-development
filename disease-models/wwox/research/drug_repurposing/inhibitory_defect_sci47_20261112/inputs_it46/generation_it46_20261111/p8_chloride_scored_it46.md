# IT46 P8: scoring of the GABA/chloride gene extraction (predictions in `p8_chloride_prereg_it46.md`, committed before the run)

Non-canonical working note. RNA class means (FPKM); not channel number, current or share; no claim on WWOX; no compound. Inputs: the same local GEO tables as SCI44 (the first mouse input digest d32fe75d... equals the SCI44 table's); extraction by `chloride_gaba_expression.py` (a copy of `kchan_expression.py`, gene list and output names only); outputs in `expr/`.

| Gene | Prediction | Mouse P7 neurons against the best other class | Human (one neuron sample) | Score |
|---|---|---|---|---|
| Slc12a5 (KCC2) | NEURON_ENRICHED | 22.79 against OPC 4.81: NEURON_ENRICHED | 11.70 against 0.60: NEURON_ENRICHED | held |
| Slc12a2 (NKCC1) | not neuron-enriched | 5.26 against newly formed oligodendrocytes 100.12: enriched elsewhere | 3.60 against hippocampal astrocytes of an epilepsy region 28.55: enriched elsewhere | held |
| Slc6a1 (GAT-1) | SHARED neurons and astrocytes | neurons 128.67, astrocytes 419.72 (3.3-fold): enriched elsewhere under the 3-fold convention | 79.60 against 58.83: SHARED | **partly** (human held; mouse fails by the convention) |
| Abat (GABA-T) | not neuron-enriched | 53.59 against 53.02: SHARED | 36.80 against 22.10: SHARED | held |
| Gabra1 | NEURON_ENRICHED | 5.49 against OPC 3.60: SHARED | 110.60 against 1.85: NEURON_ENRICHED | **failed in mouse** (OPC class high), held in human |
| Gabrb3 | NEURON_ENRICHED | 24.53 against OPC 21.79: SHARED | 35.30 against 3.48: NEURON_ENRICHED | **failed in mouse** (OPC class high), held in human |
| Gabrg2 | NEURON_ENRICHED | 24.13 against OPC 3.69: NEURON_ENRICHED | 69.50 against 1.65: NEURON_ENRICHED | held |
| Gad1 | NEURON_ENRICHED | 66.94 against OPC 11.11: NEURON_ENRICHED | 113.00 against 2.88: NEURON_ENRICHED | held |
Five of eight held in both species; one partly; two failed in the mouse table because the P17 OPC class reads the GABA-A subunits at a level close to the P7 neurons (a class difference in age as well as type: P7 neurons against P17 OPC).

## What it changes (INFERENZA; RNA, small n, one age per class)
* S6 (chloride gradient): KCC2 is neuron-enriched in both tables, so a KCC2-directed lever is attributable to neurons; NKCC1 is enriched in oligodendrocyte-lineage cells and astrocytes, so an NKCC1 blocker applied to a slice is **not** neuron-only.
* S7 (GABA supply): GAT-1 mRNA is higher in astrocytes than in neurons in the mouse table (so a reuptake blocker acts on glial uptake too) and the transaminase gene is read equally in neurons and astrocytes: a supply lever is not a neuron-only manipulation.
* S5: GABA-A subunit RNA is shared with the OPC class at P17 for two of three subunits.
* The S7 result (`s7_case/result_it46.md`) is **not rewritten**: on the day of the case the context join added nothing (NOT_IN_TABLE); this extension gives it data afterwards and is reported as a follow-up. Limits: P7 neurons are not P13-17 layer II/III pyramidal cells; one human neuron sample; two pools per mouse class; KCC2/NKCC1 mRNA is not the chloride gradient (that is the E_GABA measurement of IT46-Q01).
