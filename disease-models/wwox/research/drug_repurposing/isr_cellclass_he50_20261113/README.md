# ISR genes in the held cell-class RNA tables (HE50, answers IT49-Q02's extraction)

Non-canonical working note. Not medical advice. Values for the scientific owners to interpret; this note interprets nothing. Task record `ledger/tasks/plan/PLAN-HE50-DESIGN-ONLY-PHARMACOLOGY-20261113.json`.

## What was done
* The gene list comes from the text of IT49-Q02 (`isr_states.py` parses it): `EIF2AK1-4, EIF2B1-5, PPP1R15A/B, EIF2S1` = **12 symbols**. The case's result note says "all 11 ISR genes": the counts differ. A consumer's own list should be compared with the twelve (the symbol list staged for the INV-02 hypotheses in `isr_inv02_it50_20261113` had eleven on 2026-11-13, with PPP1R15B absent; passed to its owner, not edited here).
* The extraction is the existing one (`generation_it47_20261112/b1_cellclass/targets_expression.py`), made parametric by `--genes` and `--prefix` instead of a fifth copy; without those options its output is byte-identical to the committed tables (checked). The 18 registered input files (`input_digests.tsv`, copied from IT47) were hashed again before use: no mismatch.
* The per-gene check printed nothing: every symbol is present in both tables, every mouse class has the replicate rows its files give (two), no human symbol sits on more than one row. A symbol absent from a table would have been printed as absent (unknown, not low), and an ambiguous one as ambiguous.
* The classification is `cell_context.py`'s join unchanged (floor 1.0 FPKM, 3-fold rule), with the two new tables added in-process only; the committed join and `cell_context_it46.tsv` are not changed.

## Files
`isr_expression_mouse.tsv`, `isr_expression_human.tsv` (class means, replicate counts, input hashes); `isr_cell_class_states.tsv` (24 rows: state per gene and species); `isr_states.py`; `input_digests.tsv`.

## Values (state by the existing rule; FPKM of the neuron class against the best other class)
| Gene | Mouse | Human |
|---|---|---|
| EIF2AK1 | shared (10.7 neurons P7; 15.4 OPC P17) | shared (10.9; 14.1 tumour astrocytes) |
| EIF2AK2 | enriched elsewhere (0.4; 4.6 astrocytes P7) | shared (7.6; 9.0 tumour astrocytes) |
| EIF2AK3 | shared (4.5; 11.7 OPC) | shared (3.7; 9.8 myeloid) |
| EIF2AK4 | shared (3.9; 7.6 astrocytes) | shared (3.7; 3.0) |
| EIF2B1 to EIF2B5 | shared in all five (neuron 5.1 to 19.0; best other 9.1 to 38.1) | shared in all five |
| PPP1R15A | enriched elsewhere (48.0; 377.6 microglia) | enriched elsewhere (3.7; 24.9 myeloid) |
| PPP1R15B | shared (20.1; 27.2 newly formed oligodendrocytes) | enriched elsewhere (4.8; 24.3 myeloid) |
| EIF2S1 | shared (5.1; 13.2 endothelium) | shared (10.9; 10.4 tumour astrocytes) |
No gene is neuron-enriched in either table. Read as: an ISR measurement in a mixed preparation cannot be attributed to neurons from RNA alone; whether that matters for the planned cell-class naming is for the scientific owners.

## Limits that travel with the values
RNA class means, not protein, activity or the direction of the ISR in a WWOX-deficient cell (that stays unmeasured). The mouse neuron class is a P7 sample (two replicates), oligodendrocyte-lineage classes are P17; the human neuron class is a single column and the human non-neuronal groups include tumour and epilepsy-region astrocytes: ages, regions and states differ between classes. The 1.0 FPKM floor and the 3-fold rule are conventions of the join, not biology. These are the same two public tables used by earlier extractions; no new download.

## Consumer (proposed, not applied)
Registering the two tables in `cell_context.TABLES` would let the existing join answer for the ISR genes in every consumer that calls it (the INV-02 hypotheses rows currently say "unknown"); that edit is in a shared file and is left to the integrator. Then regenerate `cell_context_it46.tsv` and the rows that quote it.
