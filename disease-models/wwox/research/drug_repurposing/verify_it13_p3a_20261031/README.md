# IT13 verification ver3a: P3a mouse E/I transcript claims (independent recompute)

## 0. Decision
| Item | Verdict |
|---|---|
| 1. Pvalb lower 4/4 (-1.70, -0.85/-0.86, -1.16, -0.59), background <= 0.18; pan-interneuron panel flat | CONFIRMED for Pvalb and background; panel "flat" CONFIRMED WITH CORRECTION: Slc32a1 is lower in 4/4 (-0.35 to -0.41), Gad1 3/4, Lhx6 3/4 |
| 2. Npy higher 4/4 | CONFIRMED for sign (every KO animal above every control animal in all four); CORRECTION: only H_S (+2.51) clearly exceeds the within-deposit background (control line N vs WT +0.73); H_N (+0.69) and H_null (+0.72) are inside it; cortex has no background estimate |
| 3. Cacna1g/Cacna1h lower or flat; Kcnj6 flat | CONFIRMED (Cacna1g +0.08 / -1.01 / -0.44 / -0.28; Cacna1h -0.53 / -0.44 / -0.68 / -0.15; Kcnj6 -0.14 / +0.05 / -0.25 / -0.23). Caveat: Cacna1h control-line background reaches +0.90, Kcnj6 +0.57, so these are not interpretable at n = 2-4 |
| 4. Slc12a2 and Slc12a5 both lower, NKCC1:KCC2 not raised | CONFIRMED WITH CORRECTIONS: Slc12a2 lower 4/4 (-1.09, -0.82, -0.64, -0.45); Slc12a5 lower in 3/4 but HIGHER in H_N (+0.28). log2 NKCC1/KCC2 ratio change: -0.54, -1.10, -0.23, +0.20 (cortex slightly raised, noise-level). "Not raised" holds in 3/4 hippocampal contrasts; not "both lower 4/4" |
| GEO accession-to-tissue mapping | CONFIRMED (GSE158681 = P17 hippocampus, GSE158682 = P17 cortex) |

Numbers agree with the producer's `results/genes_individual.tsv` gene by gene to within 0.01 log2 (Pvalb -1.70/-0.85/-1.16/-0.59 vs producer -1.701/-0.855/-1.156/-0.586; Npy, Slc12a2/5, Cacna1g/h, Kcnj6, Gad2 all matched).

## 1. What I knew before, and plan
I had seen the producer's claims and the README sections defining contrasts and panels (not its tables). I defined contrasts from the GEO sample sheet before computing: hippocampus (GSE158681, 14 animals): S = neuron deletion, 3 KO (S_KO) vs 2 S_Ctrl; N = neural stem/progenitor deletion, 2 N_KO vs 2 N_Ctrl; null = 2 KO vs 3 WT; cortex (GSE158682): 3 CRTX_S_KO vs 4 CRTX_S_Ctrl. Background = control vs control: S_Ctrl v WT, N_Ctrl v WT, S_Ctrl v N_Ctrl (hippocampus only; the cortex deposit has no second control). Unit = animal (one sample = one animal; the deposit does not state litters, sex or cage, unverifiable). Statistic: transcript TPM summed to gene (Ensembl r92 cDNA, sha256 matches `inputs/SHA256SUMS`, symbols from the fasta header), log2((mean KO+0.5)/(mean ctrl+0.5)). Own code: `ver3a_check.py`, output `ver3a_output.txt`. Producer script not run.

## 2. Animals that drive results
* Pvalb H_null: WT_1 is low (13.4 vs 23.6/21.4), KO 6.6/10.3; still separated but control spread is wide. C_S: KO_3 79.9 overlaps control min 73.5 (not animal-separated).
* Npy H_null: KO (138.6/136.4) equals the N_Ctrl line (134/143); the "rise" is relative to WT and is the control-line difference. Cortex Npy KO_3 (1108) largest.
* Slc12a5 H_N: N_KO_2 145.5 drives the +0.28.
* Wwox deletion check: Wwox gene TPM falls 1.6-2.5 log2 in every KO contrast (residual 0.1-0.8 TPM hippocampus; cortex 3.8-9.0 vs 8-26.5 controls, a partial reduction, as expected from a neuron-restricted deletion in bulk tissue).

## 3. Unverifiable
Sex, litter, and which Cre line each control belongs to are not stated in the series metadata (labels only: S-Control, N-Control, Wild type). The series text calls N controls "N-WT" in the design sentence and "N-Control" in sample characteristics. Whether TPM were quantified on GRCm38 r92 is assumed from the producer's input; transcript IDs in the table matched the fasta (no unmapped transcripts reported in my run beyond those without a symbol, which were skipped).

## 4. GEO access
Public GEO text view (acc.cgi, form=text) returned data for both series (about 11 MB each); sample titles and counts match the held matrix columns exactly (14 and 7 samples). Nothing circumvented.

## 5. Edits this implies (proposals)
Reword P3a item 4 to "Slc12a2 lower 4/4; Slc12a5 lower in 3/4 (higher in N); ratio not raised in hippocampus, +0.2 in cortex"; reword Npy as "higher 4/4 in sign, beyond the control-line band only in S"; name Slc32a1 as a consistent mild decrease within the pan-interneuron panel.
