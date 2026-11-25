# ADV-231 pre-registration: is there a STAT3-axis transcript echo in held Wwox-deficient brain tables? (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Assignment ADV-231 (ADV message 2026-11-25), answering ADV228-Q01. About 60 minutes, no spend, no download, no contact. Checkpoint AC, RP-045 and the sealed ADV-174/175 material untouched. Frozen before any gene other than Socs3 was looked up in any table; time and digest are in the two companion files.

## 1. What had been seen before freezing (honest list, from the duplicate check ADV asked for first)
* The ADV-228 reading of PMID 30154439 (cancer lines: WWOX binds JAK2 and STAT3, restrains phospho-STAT3).
* `wwox_data_it24_p4_20261104/results/mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv`, one row: contrast C_S (cortex, S-deletion), Socs3, mean TPM 1.08 (KO, n 3) against 5.68 (control, n 4), centred log2 ratio -1.769, direction `down`, class `descriptive_only_n3v4`. That is the answer to "does Socs3 rise in the cortex knockout": no, it falls, at low expression and with a small n.
* `partial_benefit_it6_p10_20261029/README.md` line 104: this is the **human organoid** panel GSE156243 (week 15, 4 v 2 libraries), not brain: SOCS3 5.7 v 14.2 CPM lowered, STAT3 not separated. Line 54: P47T adult PFC, CTX, HPC, "IL6-JAK-STAT3 set positive", a pathway inference from an enrichment, no gene-level value carried. So the repository carries one measured Socs3 value in P17 cortex and a pathway-level inference for P47T; **no per-animal, fixed-list, control-versus-control analysis exists**. This run does only that remainder.
* NOT seen: any value of any other gene of the list below in any P17 or P47T table; the P47T per-animal table was opened for its header line only (column names), no gene row.

## 2. Frozen design
**Data (held, read only):** P17 TPM tables `GSE158681` (hippocampus: S_Ctrl 2, S_KO 3, N_Ctrl 2, N_KO 2, KO 2 [null], WT 3) and `GSE158682` (cortex: S_Ctrl 4, S_KO 3); P47T knock-in per-animal normalised counts `GSE215425_processed_data.csv.gz` (PFC, HPC, CTX 5 WT v 5 P47T; CB 4 v 3). Gene-to-symbol mapping with the same Ensembl 92 cDNA file and the same loader as ADV-224.

**Fixed gene list (nine), with the reason each is on it:** Stat3 (self-induced target and the axis member); Jak2 (axis member, the kinase WWOX binds in PMID 30154439); Il6st (gp130, the shared receptor chain, axis member); Socs3 (the canonical direct STAT3 target and negative-feedback gene); Socs1 (JAK/STAT feedback gene); Il6 (target and ligand of the loop); Osmr (STAT3-induced receptor, in the ADV-165 Cyfip2 panel); Bcl3 (STAT3 target); Pim1 (STAT3/STAT5 target). **Excluded on purpose** because ADV-095 already carries them as astrocyte-reactivity genes: Gfap, Lcn2, Serpina3n, C3, Timp1, Vim, Cd44, Cebpd. Wwox is read as a depth check only (not a list member).

**Contrasts (as ADV-224, same animals):** knockout-versus-own-control: H_S, H_N, H_null (hippocampus), C_S (cortex); control-versus-control noise floor: CC_SW (S_Ctrl v WT), CC_NW (N_Ctrl v WT), CC_SN (S_Ctrl v N_Ctrl). P47T: P47T v WT within each region, with the same rule.

**Per-animal rule:** a gene is *measurable* in a contrast if mean TPM >= 1 in both arms (P47T: mean normalised count >= 10 in both arms; the scale differs and is not TPM). Centred log2 ratio Rc = log2((mean KO + 0.5)/(mean control + 0.5)) minus the median of that ratio over all measurable genes in the contrast. *Separated* = every knockout animal above every control animal (or all below). Call HIGHER if Rc >= +0.3 and separated; LOWER if Rc <= -0.3 and separated; else NOT RESOLVED; not measurable stays NOT MEASURABLE. Every animal's value is printed.

**Gene verdict:** HIGHER (or LOWER) if the same call appears in at least two of H_S, H_N, H_null, or in C_S plus one hippocampal contrast; P47T: in at least two of four regions. A gene with any HIGHER/LOWER call in a control-versus-control contrast is *noise-prone* and its verdict is NOT RESOLVED. 

**Disposition (evaluated in this order):**
1. **Echo:** at least three of the six target genes (Socs3, Socs1, Il6, Osmr, Bcl3, Pim1) have verdict HIGHER and none of the nine has a noise-prone call.
2. **Inverse (no rising echo):** no more than one target HIGHER and at least one LOWER (for Socs3, the cortex row already says LOWER, so this is the expected branch).
3. **No echo:** at least four of the six targets measurable, none HIGHER or LOWER.
4. **Not resolvable:** otherwise (fewer than four of six targets measurable, or every called gene noise-prone).
A cell-composition caveat is added whenever a call is LOWER or HIGHER: Socs3, Il6 and Osmr are expressed in glia, neurons carry little of them, and the Gabrd result of this campaign showed a cell-class confound in these tables; no cell-resolved contrast (GSE158684 is one pool per arm) is used to separate them.

## 3. Predictions (frozen, knowing the cortex Socs3 row)
* P1: Socs3 is LOWER or NOT RESOLVED in C_S and never HIGHER in any contrast.
* P2: the disposition is 2 (inverse) or 3 (no echo); not 1.
* P3: Il6 is NOT MEASURABLE (below 1 TPM) in at least one of the P17 tables.
* P4: P47T: no target is HIGHER in two or more regions, and Stat3 is not separated.
* P5: at least one of the three control-versus-control contrasts shows a HIGHER or LOWER call for at least one of the nine genes (the noise floor is not empty).

## 4. What would change my mind
Two or more targets HIGHER in the knockouts (Socs3 rising in the hippocampus would contradict the cortex row and be reported as such), or a control-versus-control call in the very gene I would call (that makes the knockout call noise).

## 5. Outputs
A print-only script (no shebang, not executable, prints this paragraph without arguments), a per-animal table, a verdict table, the RESULT with the disposition, the DL-MECH-014 consequence, what phospho-STAT3 measurement would still be needed (Q02), one surprise line. No receipt is needed (no source is read; tables are held data), none will be written.
