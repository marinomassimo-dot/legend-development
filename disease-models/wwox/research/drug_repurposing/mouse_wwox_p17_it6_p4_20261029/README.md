# P4 (IT6): the iteration-5 gene sets in mouse P17 brain with Wwox deletion (GSE158681 hippocampus, GSE158682 cortex)

**This is a transcript-only result (Salmon TPM of mouse bulk tissue). No protein, phosphorylation, eIF2alpha, translation, activity, lactate or
flux is measured here, and none can be inferred from it.** Exploratory computational result on published data, not a new experiment, not
medical advice. Scientist-b, 2026-10-29. Pre-analysis: `PRE_ANALYSIS.md`, committed (8e424c9f) before any expression value was opened; the
results below came after it. Everything is reproducible from the raw files by `python3 -I p4_mouse_same_sets.py ... results` (about 95 s;
the output directory was regenerated into a second directory and is byte-identical) and `make_figure.py` (numpy + zlib; matplotlib is absent here).

## 1. One-paragraph answer

In four mouse contrasts (hippocampus: neuron-targeted deletion "S", neural-stem/progenitor-targeted deletion "N", germline null; cortex: "S")
the ISR target set sits **inside its matched null in every contrast** (centred mean +0.14, -0.13, -0.02 and +0.05; none animal-separated).
The mouse therefore does **not** side with the organoid (lower) and does **not** side with the shWWOX line (higher): the sign conflict
stays **UNRESOLVED**, and a third system with an unambiguous deletion adds a flat transcript signal, not a tiebreak. An organoid-sized
fall (-0.33) would have sat at or near the lower null edge in H_S and H_N (-0.30, -0.34) and beyond it in H_null and C_S (-0.20, -0.26), so a fall of
that size is not what these animals show; a small effect of either sign, and any effect at protein/phospho level, is not excluded.
The dataset behaves as described by its authors (myelin/oligodendrocyte transcripts -0.8 to -1.8 in all four deletion contrasts, all outside the
null and animal-separated), the deletion is deep (85, 94, 91 percent in the three hippocampal contrasts), and the control-versus-control
contrasts reveal a large background difference between the control groups that limits every other set (section 4).

## 2. Deposit verification (details in PRE_ANALYSIS section 2)

Series and sample records read at the source. Hippocampus: 14 libraries (S 2 ctrl / 3 KO; N 2 / 2; WT 3 / null 2), cortex: 7 (S 4 ctrl / 3 KO),
all P17, NextSeq 500, Salmon 1.2.1, mm10. Deposits carry transcript TPM only. The Ensembl-92 cDNA matches all 111,083 transcript ids (releases 90 to 100
match fewer), so release 92 was the gene key. **Deletion visible**, summed Wwox TPM (per animal in `results/wwox_depth.tsv`): hippocampus S 0.49 vs
3.37 (85 percent lower), N 0.21 vs 3.55 (94 percent), null 0.33 vs 3.89 (91 percent): every hippocampal contrast passes the 50 percent gate.
Cortex S 5.9 vs 18.8 (68 percent lower, passes) but with overlap between animals (KO 3.8, 5.0, 9.0; controls 8.0, 15.1, 25.7, 26.5): cortex is a weaker, noisier replication.
**UNVERIFIED** (the deposit does not state): the Cre drivers behind "S" and "N" (series text: neurons; neural stem and progenitors); the control genotype
(Cre-negative or other); sex; litter or batch; the allele; the link to any paper (no PubMed id in either record). The records say "Public on Oct 01 2026".
Sex was inferred only from Y-linked transcripts (Xist is not in the cDNA key): arms are **not sex-balanced** (hippocampus S KO 2 male 1 female-like vs control 1 and 1; N KO 2 male-like vs control 1 and 1;
null KO 1 and 1 vs WT all female-like; cortex mixed). Not adjusted.

## 3. Results (centred mean log2 KO/control of each pre-declared set; [2.5th, 97.5th percentile of its decile-matched null]; OUT = outside; sep = every KO animal on one side of every control animal)

| Set (measurable members in H_S) | H_S | H_N | H_null | C_S | control-vs-control (SW, NW, SN) |
|---|---|---|---|---|---|
| ISR_targets (11) | +0.14 [-0.30,+0.33] | -0.13 [-0.34,+0.31] | -0.02 [-0.20,+0.17] | +0.05 [-0.26,+0.27] | +0.18, +0.26, -0.06 |
| ISR_core5 (4) | +0.31 [-0.49,+0.55] | +0.09 [-0.56,+0.51] sep | +0.08 [-0.30,+0.30] sep | +0.08 [-0.42,+0.43] | +0.26, +0.27, +0.01 |
| UPR_branches (8) | +0.21 [-0.36,+0.39] | -0.12 [-0.41,+0.37] | -0.30 [-0.24,+0.18] OUT sep | -0.02 [-0.29,+0.33] | -0.65*, -0.55*, -0.09 |
| Mito_translation (76) | -0.09 [-0.11,+0.12] sep | -0.16 [-0.11,+0.14] OUT sep | -0.04 [-0.09,+0.05] | +0.11 [-0.08,+0.09] OUT sep | +0.23*, +0.38*, -0.13* |
| Mito_import (22) | -0.18 [-0.22,+0.24] sep | -0.32 [-0.24,+0.25] OUT sep | -0.09 [-0.15,+0.10] | +0.03 [-0.15,+0.17] | +0.15, +0.35*, -0.18* |
| OXPHOS_nuclear (71) | -0.24 [-0.09,+0.20] OUT sep | -0.36 [-0.10,+0.21] OUT sep | -0.08 [-0.06,+0.07] OUT | +0.15 [-0.01,+0.18] sep | +0.48*, +0.67*, -0.18* |
| Glycolysis_lactate (9) | -0.09 [-0.36,+0.43] | -0.19 [-0.41,+0.42] sep | -0.18 [-0.19,+0.18] | +0.11 [-0.18,+0.35] | +0.36, +0.35, +0.02 |
| Glycolysis_19 (16) | -0.07 [-0.27,+0.34] | -0.09 [-0.30,+0.34] | -0.21 [-0.14,+0.14] OUT sep | +0.11 [-0.12,+0.27] | +0.38, +0.41, -0.03 |
| PDK_family (4) | +0.39 [-0.49,+0.53] sep | +0.19 [-0.54,+0.52] | -0.30 [-0.35,+0.26] sep | +0.08 [-0.37,+0.44] | -0.31, -0.42, +0.12 |
| Prog_core4 (4) | -0.17 [-0.49,+0.54] sep | +0.00 [-0.58,+0.52] | +0.37 [-0.39,+0.29] OUT sep | +0.12 [-0.50,+0.44] | +0.26, +0.12, +0.16 |
| Prog_9 (9) | +0.24 [-0.32,+0.38] | -0.26 [-0.41,+0.39] sep | +0.29 [-0.22,+0.19] OUT sep | +0.11 [-0.30,+0.28] | -0.13, -0.02, -0.09 |
| Neuro_5 (5) | +0.30 [-0.53,+0.62] | +0.28 [-0.55,+0.62] sep | +0.14 [-0.28,+0.23] sep | +0.22 [-0.27,+0.45] sep | -0.41, -0.41, +0.01 |
| Neuro_10 (10) | +0.36 [-0.35,+0.41] sep | +0.34 [-0.39,+0.43] sep | +0.25 [-0.19,+0.16] OUT sep | +0.22 [-0.19,+0.32] sep | -0.38, -0.42*, +0.06 |
| Myelin_OL (10) | -1.78 [-0.33,+0.41] OUT sep | -1.02 [-0.36,+0.40] OUT sep | -1.66 [-0.17,+0.17] OUT sep | -0.80 [-0.18,+0.34] OUT sep | -0.31, -0.44*, +0.15* |
| Ctl_housekeeping (12) | +0.37 [-0.31,+0.37] sep | +0.24 [-0.35,+0.39] sep | +0.04 [-0.17,+0.15] sep | +0.17 [-0.17,+0.30] | +0.11, +0.18, -0.06 |
| Ctl_cytosolic_ribosome (78) | +0.02 [-0.09,+0.18] | -0.22 [-0.10,+0.19] OUT sep | +0.12 [-0.07,+0.06] OUT sep | +0.05 [-0.00,+0.18] | +0.66*, +0.88*, -0.21* |

`*` in the last column = outside its own null in that control-versus-control contrast (no Wwox difference between the arms). Universe threshold
1 TPM (sensitivities 0.5 and 2 in `results/set_summary.tsv`: signs identical in all 126 contrast-by-set cells except two values within 0.01 of zero: H_N Prog_core4 and CC_NW Prog_9). Figure: `fig1_sets_vs_matched_null.png`.
Pre-declared decision verdicts are in `results/verdicts.tsv`. Members not resolvable at the mouse key (declared rule, excluded): ATP5ME, NDUFB1, MRPL50P2, TOMM70
(mouse Tomm70a), GPI (mouse Gpi1) and ALDOA (two non-patch genes carry the symbol), see `results/set_member_resolution.tsv`; TRIB3 is below 1 TPM in every
contrast (a missing value, not absence), so ISR_targets has 11 measurable members, ISR_org3 (CHAC1, TRIB3, SESN2) has 2 and is not evaluable, and the single gene ATF4 is not a set.

| Verdict by the pre-declared rule | Sets |
|---|---|
| ISR_targets | NOT MOVED: outside the null in 0 of 3 counted contrasts (ISR_core5 also 0 of 3) |
| OXPHOS_nuclear | criterion (a) met (lower in S -0.24 and N -0.36, null band +/-0.1, animal-separated) but NOT MOVED: it also differs between control groups (+0.48, +0.67, -0.18), the cytosolic-ribosome control moves in H_N, null contrast not separated, cortex opposite (+0.15) |
| Mito_translation, Mito_import | NOT MOVED: outside only in H_N; cortex has the opposite sign for translation (+0.11, outside); control groups differ |
| Glycolysis_lactate (10-gene, 9 measurable), Glycolysis_19, PDK_family | NOT MOVED (Glycolysis_19 outside only in the null contrast, -0.21; PDK_family signs +0.39, +0.19, -0.30) |
| Prog_core4, Prog_9, Neuro_5, Neuro_10 | NOT MOVED (each outside only in the null contrast, Prog with signs that differ between contrasts; Neuro_10 positive in all four contrasts +0.22 to +0.36 but outside only once) |
| Myelin_OL | positive control behaves: lower in all four deletion contrasts (-1.78, -1.02, -1.66, -0.80); not "MOVED" under the rule only because control groups also differ in it |

## 4. What limits every statement (read before using any row above)

1. **The control groups differ from each other as much as knockouts differ from their controls.** Transcriptome-wide, the IQR of centred log2 ratios is
   about +/-0.28 (H_S), +/-0.30 (H_N), +/-0.16 (null), +/-0.23 (cortex), versus +/-0.35 and +/-0.41 for S-control vs WT and N-control vs WT, and the unrelated cytosolic-ribosome control moves
   +0.66 and +0.88 between those control groups. The same gene classes (OXPHOS, mito translation, ribosome, UPR) that look "lower" in a cell-targeted deletion differ as much between control groups. The germline-null contrast uses WT controls and is the most exposed; S and N are compared with their own controls.
2. 2 to 3 animals per arm; the gene-level matched null ignores animal-to-animal variance (hence the animal-separation column); smallest possible animal-level permutation p is 0.20 or 0.33.
3. Composition: myelin/oligodendrocyte transcripts fall 1.7 to 3.4-fold, so neuron and glia fractions shift in bulk tissue; a relative rise of neuronal markers (Neuro_10) is the expected composition effect and is not a cell-state claim.
4. Sex imbalance (above), unstated batch, unstated driver and control genotype (UNVERIFIED); symbol-based mouse-human orthology; TPM without counts.
5. Mouse P17 in vivo versus a week-15 organoid and a 2D line: only the sign of a set is laid side by side with the human systems, never combined with them.
6. Per-gene rows (`results/key_genes.tsv`) are listed with per-animal TPM and are not differential-expression calls; e.g. Hif1a is slightly higher in sign in the three hippocampal contrasts (+0.22 to +0.28) and Pdk1 has no consistent sign (-0.20, +0.32, +0.13, cortex -0.10).

## 5. Consequences (statements of wwox_systems_comparison_it5_20261029.md)

| Statement | After P4 |
|---|---|
| ISR direction UNRESOLVED (organoid lower vs shWWOX higher) | **Unchanged: still UNRESOLVED.** The third system does not break the tie; its ISR set is flat (and not distinguishable from matched random sets or from control-versus-control differences). Consequence (a)-(c) of that file stand; the matched protein/phospho plus target-mRNA experiment stays the next step. Add to the comparison as one row: mouse, in vivo, three deletion types, "inside null, no sign" |
| Drug-signature reversal built on the organoid list inherits the ISR-lower sign | **Unchanged**, and now also not supported by a mouse transcript sign; neither refuted |
| Glycolysis "higher in both human systems" (10-gene HIF-type set) | **Not extended to the mouse**: 10-gene -0.09, -0.19 (cell-targeted), 19-gene -0.07, -0.09; nothing outside the null in the cell-targeted contrasts. The human statement stays set-dependent (organoid and hNPC only); not a refutation (different species, tissue and composition) |
| PDK1 not raised; middle link of the HIF1A-PDK-PDH chain has no transcript support | **Unchanged**, one more system without support: Pdk1 no consistent sign, PDK family inside null; the finding remains "absence of support" |
| Progenitor identity: hNPC drop robust, organoid "higher" set-dependent | **Unchanged for the human systems.** In the mouse neither the 4-gene nor the 9-gene definition gives a moved set, and the two disagree in sign in H_S and H_N (so the statement is also set-dependent here); a mouse P17 bulk progenitor set is not a cell-state readout |
| Neuronal markers lower (CAGE neurons) / not clearly lower (organoid) | Mouse: neuronal 5- and 10-gene sets positive in all four contrasts (+0.14 to +0.36), outside the null once; the sign opposes the human "lower" but is composition-confounded (myelin set -0.8 to -1.8) and is below criterion. No change to the human statement |
| Mitochondrial programmes: OXPHOS / mito translation lower in the organoid | Mouse OXPHOS lower in S and N but not specific (ribosome control and control-versus-control differences move too; cortex opposite): **no corroboration, no refutation** |

For needs and priorities: NEED-ISR-ATTENUATION may receive one observation (evidence_scope COMPUTATIONAL_RESULT, readout_level transcript, model type mouse in vivo
cell-targeted and null deletion, result "ISR target set not distinguishable from matched random sets and from control-vs-control differences in 4 contrasts; no sign"), with the n of 2 to 3 stated. No
rank, track, goal or "unmeasured" status (eIF2alpha-P, GCN2/PERK, ATF4 protein, translation) changes, because a flat mRNA result cannot move a protein/phospho/flux question. **I edited no needs file and no current file; that landing is for the integrator.**
Priority: this lowers the expected value of further transcript re-analyses of public WWOX deposits for the ISR question (a third system with a visible deletion is flat); it raises the relative priority of the matched protein/phospho experiment.

## 6. Deviations from the pre-analysis, and what stayed open

- Deviations: none in method or sets. Reporting deviations: Xist is not in the cDNA key (non-coding), so sex was read from Ddx3y, Kdm5d and Eif2s3y only; ISR_org3 and Prog_NESVIM have fewer than 3 measurable members and are not evaluable by the declared rule; six human members have no mouse match under the declared rule (excluded, not replaced).
- Not done: counts-based or dispersion-model analysis (no counts in the deposit; SRA raw reads were not fetched); no sex-stratified re-analysis; no adjustment for composition.
- UNVERIFIED: Cre drivers of S and N; control genotypes; sex; batch; allele; paper link; one-to-one orthology of PDK/SLC16/SLC2/HK/LDH.

## 7. Files

`PRE_ANALYSIS.md` (committed first) · `p4_mouse_same_sets.py` · `make_figure.py` · `fig1_sets_vs_matched_null.png` · `inputs/SHA256SUMS`, `inputs/PROVENANCE.md` (raw tables and the Ensembl FASTA are not committed; hippocampus 4.8 MB, cortex 2.6 MB, FASTA 50 MB) ·
`results/`: set_summary.tsv (all contrasts and thresholds), verdicts.tsv, key_genes.tsv, wwox_depth.tsv, isr_leave_one_gene_out.tsv, set_member_resolution.tsv, results.json (parameters, hashes).
