# Independent verification, IT6 package P4 (mouse P17 Wwox deletion, GSE158681 / GSE158682), 2026-10-29

Verifier is not the producer. Transcript-level, exploratory, computational; not medical advice. Method: raw files re-downloaded into a new
empty directory, all code run with `python3 -I`, no registration, contact address, spend or access-control bypass. The independent
calculation was written before the producer's statistic code was read (it used only the pre-analysis text for sets, mapping and rules).

Overall: the numbers reproduce exactly and the central conclusion (ISR target set inside its matched null in every contrast, sign conflict
not broken) is SUPPORTED. Two supporting statements are overstated, one relevant observation is missing from the summary. No HIGH defect.

## 1. Inputs and deposit

| Check | Result |
|---|---|
| sha256 of the two TPM tables and the Ensembl release-92 cDNA FASTA, re-downloaded from the URLs in `inputs/PROVENANCE.md` | all three equal `inputs/SHA256SUMS` (52ff4f07..., 77aecf5c..., 7d2fcb0c...). Sizes 4,819,338 / 2,614,428 / 49,851,793 bytes |
| Iteration-5 set table sha256 | cdbac348...647b1, equal to the value declared |
| Series pages (text form) | GSE158681: 14 samples, overall design "WT (n=3) vs KO (n=2), S-Ctrl (n=2) vs S-KO (n=3), N-WT (n=2) vs N-KO (n=2)", "7 samples are control", P17, Salmon 1.2.1, mm10; GSE158682: 7 samples, "CRTX-S-KO (n=3) compared to CRTX-S-Ctrl (n=4)". Sample records: S_Ctrl_1-2 (S-Control), S_KO_1-3 (Wwox deletion in neurons), N_Ctrl_1-2 (N-Control), N_KO_1-2 (Wwox deletion in Neural Stem and Progenitors), KO_1-2 (Wwox- null), WT_1-3 (Wild type); cortex S-Control x4, deletion in neurons x3. All confirmed |
| Not stated by the deposit | confirmed: no Cre driver name, no control-genotype description beyond the label, no sex, no batch table (only "batch correction was included in some of DESeq2 designs"), no allele, no PubMed id or paper link in either record (zero matches for "pubmed"). The series summary reads like a paper abstract but cites nothing. One internal inconsistency not noted by the producer: the design text calls the N controls "N-WT", the sample records call them "N-Control" (minor) |
| Annotation | the FASTA has no Xist (confirmed), so the producer's reporting deviation (sex from Ddx3y, Kdm5d, Eif2s3y) is correct. Sex calls re-derived from the three Y genes agree with the README (hippocampus S KO: 2 male, 1 female-like; controls 1 and 1; N KO 2 male-like, controls 1 and 1; null KO 1 and 1; WT all female-like) |

## 2. Reproduction and independent calculation

- The producer's script, run exactly as described (about 93 s), regenerated `results/` byte-identical for all seven files (cmp, 0 differences).
- Independent code (own gene key from FASTA headers, patch genes dropped, transcript TPM summed to gene, universe mean TPM >= 1 in both arms,
  R = log2((mKO+0.5)/(mctl+0.5)) median-centred, own decile matching, 10,000 draws with a different seed, own animal-level score):

| Quantity | Independent | Producer |
|---|---|---|
| Wwox summed TPM, KO vs control; reduction | H_S 0.49 vs 3.37, 85.5 percent; H_N 0.21 vs 3.55, 94.0; H_null 0.33 vs 3.89, 91.5; C_S 5.94 vs 18.83, 68.5 | identical |
| ISR_targets (12 declared, 11 measurable; TRIB3 below 1 TPM) centred mean, null 2.5-97.5, rank | H_S +0.135 [-0.29, +0.33] p 0.40; H_N -0.134 [-0.35, +0.30] 0.47; H_null -0.019 [-0.21, +0.17] 0.93; C_S +0.051 [-0.25, +0.26] 0.65; none animal-separated | +0.135 [-0.302, +0.327]; -0.13; -0.02; +0.05; same |
| Myelin_OL (10) | H_S -1.78, H_N -1.02, H_null -1.66, C_S -0.80, all outside null (rank <= 0.0004) and animal-separated | identical |
| Control-vs-control (S-ctrl vs WT) | ISR +0.18 (inside null), myelin -0.31 (inside) | identical |

Nulls differ by at most 0.02 at the band edges (different seed and my own decile rule), as expected. The README's "126 cells with identical
sign at thresholds 0.5, 1, 2 except two" is loose: 126 contrast-by-set keys exist, only 115 have a value at all three thresholds; the two
exceptions (H_N Prog_core4, CC_NW Prog_9) are real and within 0.01 of zero (LOW).

## 3. Pre-analysis timing and adherence

- `PRE_ANALYSIS.md` was committed at 07:48:43 UTC (8e424c9f); the script file dates from 07:49, the result files 07:50-07:51, the analysis commit
  09370e17 at 07:56. The ordering is consistent with "declared before results". That no expression value was opened earlier is the producer's
  statement and cannot be verified from history (UNVERIFIABLE beyond the order of commits); what the pre-analysis says was read (headers,
  first column, FASTA, P3 census Wwox figures) is plausible and the P3 Wwox figures it quotes are census numbers, disclosed as such.
- Rules followed: animal as unit (one library per animal, arm = mean of animals), set table by sha256, seed 20261029, 10,000 draws, thresholds
  0.5/1/2, depth gate, control-vs-control, positive control, ribosome and housekeeping classes. Nothing added after values. Reporting items
  (Xist absent, ISR_org3 / Prog_NESVIM / ATF4 not evaluable, six unresolved human members) are disclosed and consistent with rule 6 (declared
  mapping, no replacement by a "close" gene).
- Substituted lists: Glycolysis_19, Prog_core4, Neuro_10, ISR_core5/ISR_org3, Myelin_OL are P4's own declarations, written in the
  pre-analysis, before values, and labelled as not a reproduction of the iteration-5 verifier lists. This is honest. The consequence is that
  the mouse run cannot confirm or refute the iteration-5 "set-dependent" statements as such, only whether a plausible alternative definition
  changes a mouse sign; the README says this.
- One verdict-engine detail: for OXPHOS_nuclear criterion (b) was applied as "separated in every contrast that is outside the null"
  (H_null fails), stricter than the text ("in each of those [two] contrasts"). H_S and H_N are both separated, so under the literal text (b) is
  met; the set is still NOT MOVED through (d) background-sensitive and (f) ribosome control, so no verdict changes (LOW).

## 4. Judgement of the stated conclusions

| Statement | Verdict | Numbers |
|---|---|---|
| Deletion is deep: 85, 94, 91 percent hippocampus; cortex 68 percent, noisier | SUPPORTED | reproduced; cortex KO 3.8/5.0/9.0 vs controls 8.0/15.1/25.7/26.5 overlap (control spread 3-fold) |
| Positive control passes (myelin/oligodendrocyte lower) | SUPPORTED | -1.78, -1.02, -1.66, -0.80, all outside null and animal-separated, in line with the deposit's own summary text. Caveat: it is also lower between N-control and WT (-0.44) and slightly higher S-ctrl vs N-ctrl (+0.15), so the producer's rule labels it NOT MOVED; the effect is 3 to 10 times the control difference, so the control is valid |
| ISR target set inside matched null in all four contrasts, no sign, none animal-separated | SUPPORTED | above; leave-one-gene-out means 0.07 to 0.25 (H_S), signs not all concordant |
| "ISR sign UNRESOLVED; the third system does not break the tie" | SUPPORTED | follows from the declared rule (0 of 3 counted contrasts outside null) |
| "Third system flat" and "a fall of organoid size (-0.33) is not what these animals show" | PARTLY OVERSTATED | gene-level null carries no animal variance. Animal-level ISR score differences (KO minus control) with SE: H_S +0.09 (SE 0.17), H_N -0.13 (SE 0.14), H_null +0.01 (SE 0.07), C_S +0.09 (SE 0.09). -0.33 is excluded at roughly 2.5, 1.5, 5 and 4.7 SE respectively: fine for H_S, H_null (WT controls, see D1) and cortex, but NOT excluded in H_N (n 2 v 2). The organoid fall is carried by CHAC1, TRIB3, SESN2; in mouse bulk P17 tissue Chac1 is 1.5 to 7 TPM, Trib3 is below 1 TPM (not measurable) and Sesn2 5 to 8 TPM, so low basal levels limit what a fall could show (ISR_org3 is not evaluable). "Cannot resolve effects smaller than about 0.3 and does not arbitrate" is the defensible wording, not "flat" |
| "Control groups differ as much as KO vs control" | PARTLY OVERSTATED | transcriptome-wide centred-R IQR: KO contrasts +/-0.27-0.29 (H_S), +/-0.30 (H_N), +/-0.17 (null), +/-0.24 (C_S); S-ctrl vs WT +/-0.35, N-ctrl vs WT +/-0.41 (confirmed) but S-ctrl vs N-ctrl only +/-0.13, the smallest of all. The large control difference is WT versus the two Cre-line control groups (WT all female-like and a different genetic background or batch are candidate causes, UNVERIFIED); the cell-targeted contrasts H_S and H_N are made against their own matched controls and are not undermined at the claimed scale. The limit bites mainly on H_null and on the ribosome / OXPHOS reading. Ribosome class S-ctrl vs WT +0.66, N-ctrl vs WT +0.88, S vs N -0.21 reproduced |
| OXPHOS / mito sets not corroborating, not refuting | SUPPORTED | OXPHOS H_S -0.24, H_N -0.36 (null band +/-0.1, separated), H_null -0.08, cortex +0.15; control-vs-control +0.48, +0.67, -0.18 and ribosome control outside null in H_N: non-specific |
| Consequences for `wwox_systems_comparison_it5_20261029.md` (ISR unchanged, glycolysis not extended, PDK1 unchanged, progenitor / neuronal unchanged for human, mitochondrial no corroboration) | SUPPORTED, with one wording fix | Pdk1 -0.20, +0.32, +0.13, cortex -0.10 and Hif1a +0.22/+0.28/+0.27 reproduced. The statement that Prog_core4 and Prog_9 "disagree in sign in H_S and H_N" holds only for H_S (-0.17 vs +0.24); in H_N Prog_core4 is +0.003 (sign changes with threshold: -0.007 at 2 TPM) |
| "Lowers the expected value of further transcript re-analyses of public deposits; raises relative priority of protein / phospho experiment" | OVERSTATED (judgement) | one underpowered bulk-tissue system (2 to 3 animals, low basal ISR expression, 3 of 4 contrasts compared with different control types) is weak ground for deprioritising other transcript data; the protein / phospho priority argument stands on its own |

## 5. Defects

| Id | Severity | Defect | Requested repair |
|---|---|---|---|
| D1 | MEDIUM | "Control groups differ as much as KO vs control" is stated for all controls; S-ctrl vs N-ctrl IQR is +/-0.13, below every KO contrast; the large difference is WT vs Cre-line controls | restate: WT differs from both Cre-line control groups by +/-0.35-0.41; S and N controls are close; the germline-null contrast is the exposed one |
| D2 | MEDIUM | "A fall of organoid size is not what these animals show" is not excluded in H_N at animal level (-0.13 +/- 0.14 SE) and the organoid-driving genes are near or below the measurable floor in mouse | state detectable effect size (about 0.3), replace "flat" by "no resolvable sign", add the Chac1/Trib3/Sesn2 expression floor |
| D3 | MEDIUM-LOW | Atf4 mRNA is lower in all four deletion contrasts (uncentred log2 -0.55, -0.97, -0.60, -0.71; centred -0.16, -0.71, -0.39, -0.51; animal-separated in H_S and H_N; control-vs-control centred +0.04, +0.16) and is not mentioned in the README, which reports Hif1a and Pdk1 instead. ATF4 mRNA is not activity and a single gene is never called, but the one gene of the axis with a consistent sign belongs in the table with that qualification | add per-gene Atf4 sentence to section 4.6 / consequences |
| D4 | LOW | "126 cells" sign statement counts 11 cells without all three thresholds | write 115 of 126 |
| D5 | LOW | OXPHOS verdict text applies (b) more strictly than declared (outcome unchanged) | note in README |
| D6 | LOW | README H_S ISR "+0.14" vs `verdicts.tsv` "+0.13" (value 0.135) | harmonise rounding |
| D7 | LOW | "disagree in sign in H_S and H_N" for the progenitor sets, H_N is +0.00 (threshold-dependent sign) | restrict to H_S |
| D8 | LOW | priority sentence on deprioritising transcript re-analyses overreaches | soften or drop |
| D9 | INFO | design text "N-WT" vs sample label "N-Control" in GSE158681; not noted | mention |

No HIGH defect: no number was wrong, no post-hoc set or threshold was found, all derived tables reproduce byte for byte, and the headline
(ISR UNRESOLVED, positive control passes) stands. Conclusion strength is limited by n = 2 to 3, gene-level nulls, and low basal expression
of the ISR readout genes.
