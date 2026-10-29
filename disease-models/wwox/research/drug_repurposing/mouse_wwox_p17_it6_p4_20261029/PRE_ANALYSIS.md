# GSE158681 / GSE158682 (mouse P17 brain, Wwox deletion): pre-analysis, iteration 6, package P4

Declared 2026-10-29 by scientist-b (ACTOR scientist-b), IT6 P4. COMMITTED BEFORE ANY EXPRESSION VALUE OF THE TWO DEPOSITS WAS OPENED FOR
THE CONTRAST. What was read before this file: the two GEO series records and the 21 sample records (text, design, labels), the two file
listings, the file names, the column headers and the first column (Ensembl transcript ids, no value) of the two TPM tables, the line
count of the tables, the Ensembl cDNA FASTA headers (to build the transcript-to-gene key), and the P3 census (which summed Wwox TPM
over its transcripts: that figure comes from the census, not from a look at this iteration). No TPM cell, no gene row of any set, no
Atf4/Ddit3/Pdk1 row was looked at. Exploratory, a COMPUTATIONAL RESULT on published data, not a new experiment, not medical advice.
TRANSCRIPT ONLY: no protein, phosphorylation, translation, activity or flux is measured in these deposits, and none can be inferred.
Credit: the deposits belong to the Aqeilan laboratory (Hebrew University; contributor names in the series records). The link of the
series to a paper is not stated in the deposit (no PubMed id in either record) and is UNVERIFIED.

## 1. Question

In a third neural system (mouse hippocampus and cortex at P17, true cell-targeted Wwox deletion plus the null), does the transcript level of
the pre-declared integrated-stress-response (ISR) target set move in the direction seen in the human knockout organoid (lower; GSE156243)
or in the human shWWOX progenitor line (higher; GSE126075), or in neither? Secondary, same sets, same method: does the mitochondrial-
translation / OXPHOS / import programme, the glycolysis/lactate set, the PDK genes (Pdk1 to Pdk4), and the progenitor and neuronal marker
statements that iteration 5 flagged set-dependent come out the same way under both of their alternative set definitions?
Nothing else is asked. The result is a sign-and-rank statement about mRNA in mouse tissue.

## 2. Verification of the deposit at the source (done before this file; on the record)

| Item | Finding |
|---|---|
| Hippocampus GSE158681 | 14 libraries, mouse, NextSeq 500, mm10, Salmon 1.2.1 (gcBias, validateMapping), tissue "Hippocampus", age P17 (every sample). Series design text: WT (n=3) vs KO (n=2), S-Ctrl (n=2) vs S-KO (n=3), N-WT (n=2) vs N-KO (n=2); "7 samples are control". Sample titles: S_Ctrl_1-2, S_KO_1-3, N_Ctrl_1-2, N_KO_1-2, KO_1-2, WT_1-3. Genotype strings: "S-Control", "Wwox deletion in neurons", "N-Control", "Wwox deletion in Neural Stem and Progenitors", "Wwox- null", "Wild type". |
| Cortex GSE158682 | 7 libraries, same pipeline and age: CRTX_S_Ctrl_1-4 ("S-Control") and CRTX_S_KO_1-3 ("Wwox deletion in neurons"). |
| Release status | both series record "Public on Oct 01 2026", submitted Sep 28 2020; sub-series of GSE158685 (BioProject PRJNA666183 and PRJNA666184; SRA SRP285667 and SRP285668). |
| File used | GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz (sha256 52ff4f07...e483; 111,083 transcripts) and GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz (sha256 77aecf5c...e060f; same 111,083 transcripts). Full hashes in inputs/SHA256SUMS. Columns: Name (Ensembl transcript id with version), Length, EffectiveLength, then one TPM column per animal. Per-transcript TPM from Salmon; NO integer counts. |
| Annotation | the deposit gives no gene symbol. The transcript ids match Ensembl release 92 (GRCm38) cDNA at 111,083 of 111,083; release 90, 93, 94, 95, 96, 98, 99 and 100 match fewer (106,428 / 110,474 / 110,040 / 109,672 / 108,782 / 108,370 incl. ncRNA / 108,192 / 108,033), so release 92 is the key. Source: https://ftp.ensembl.org/pub/release-92/fasta/mus_musculus/cdna/Mus_musculus.GRCm38.cdna.all.fa.gz (sha256 recorded in inputs/SHA256SUMS). |
| What the deposit does NOT state (UNVERIFIED) | the Cre driver of "S" (series text says neurons) and of "N" (series text says neural stem and progenitors): the driver names are not in the deposit; the control genotype of S-Control and N-Control (Cre-negative floxed littermate versus Cre-only versus other); the sex of the animals; litter or batch (the processing text mentions batch correction "in some designs" and gives no batch table); the Wwox allele type (conditional exon); the relation of the series to any publication. These are not assumed. The labels "S" and "N" are used as the deposit's labels only. |
| Deletion depth | judged on the summed Wwox TPM (gene ENSMUSG00000004637, all its annotated transcripts) per animal, reported FIRST in the results. The P3 census already reported (my reading of its own sum, not re-opened here) controls 3.3 to 4.3 and deletions 0.1 to 0.8 TPM in hippocampus, and cortex controls 8.0 to 26.5 against knockouts 3.8 to 9.0. |

## 3. Contrasts and experimental unit

The experimental unit is the ANIMAL (one library per animal; regions, transcripts, genes and reads are not replicates). Each contrast is
analysed alone; none is pooled with another, with the other region or with the organoid and hNPC data (different species, different
platforms, different n; only signs and ranks are laid side by side, never a combined statistic).

| Id | Knockout arm | Control arm | n (animal) | Role |
|---|---|---|---|---|
| H_S | S_KO_1-3 | S_Ctrl_1-2 | 3 v 2 | hippocampus, deposit's neuron-targeted deletion; counted |
| H_N | N_KO_1-2 | N_Ctrl_1-2 | 2 v 2 | hippocampus, deposit's neural stem/progenitor-targeted deletion; counted |
| H_null | KO_1-2 | WT_1-3 | 2 v 3 | hippocampus, germline null; counted (systemic illness at P17 is a confound) |
| C_S | CRTX_S_KO_1-3 | CRTX_S_Ctrl_1-4 | 3 v 4 | cortex, replication check of H_S only; NOT counted in the 2-of-3 rule |
| CC_SW, CC_NW, CC_SN | S_Ctrl vs WT; N_Ctrl vs WT; S_Ctrl vs N_Ctrl | | 2v3, 2v3, 2v2 | control-versus-control (no Wwox difference): background / batch specificity check |

No contrast has more than 3 or fewer than 2 animals per arm. No p value for a WWOX effect is computed or claimed anywhere; with 2 to 3
animals the smallest two-sided permutation p over animals is 0.20 (3 v 2, 2 v 3) or 0.33 (2 v 2), so a conventional significance
statement is impossible by design and n=1 inference is not attempted (no arm has n=1).

## 4. Method (the iteration-5 same-set method, reused, not rewritten)

Script: p4_mouse_same_sets.py, adapted from hnpc_gse126075_it5_20261029/p7_organoid_same_sets.py (same statistics, same seed 20261029,
same 10,000 draws, same expression-decile matching, same set-summary columns). Changes forced by the input, all declared here:
1. Input is Salmon transcript TPM, not integer counts. Transcript TPM is summed to Ensembl gene id (patch/haplotype transcripts, whose
   location field contains "_PATCH", are dropped from the gene key). TPM is used as deposited, with no further normalisation; the median
   centring removes the global offset.
2. Per-arm value = arithmetic mean over that arm's animals of gene TPM. R = log2((mean_KO + 0.5) / (mean_ctl + 0.5)); centred R = R minus
   the median R of the contrast's measurable universe.
3. Measurable universe (replaces "count at least 10"): mean TPM at least 1 in BOTH arms. Sensitivities: threshold 0.5 and 2. Decile
   matching on log10((mean_KO + mean_ctl)/2 + 1) within that universe; set members outside the universe are reported as not measurable.
4. Set statistic: mean centred R over measurable members (needs at least 3 members); reference: 10,000 expression-decile-matched random
   sets of equal size from the universe excluding the members; reported: set mean, 2.5th and 97.5th percentile of the null, two-sided
   empirical rank. This ranks the set against random gene sets OF THIS COMPARISON; it treats genes as the sampling units and does not
   carry between-animal variance, so it is a NECESSARY condition for "moved" and never a p value for a WWOX effect (it is why the
   animal-level check below exists).
5. Animal-level check (added because the animal is the unit): per-animal set score = mean over measurable members of log2(TPM_gene + 0.5)
   minus the animal's own median of log2(TPM + 0.5) over the contrast's universe. "Separated" means every KO animal lies on one side of
   every control animal, on the side that matches the sign of the centred set mean. Leave-one-animal-out sign of the centred set mean is
   also reported. Descriptive only.
6. Ortholog mapping (fixed now, never tuned on values): mouse symbol of Ensembl 92 upper-cased equals the human symbol, with these
   exceptions: ATP5F1A=Atp5a1, ATP5F1B=Atp5b, ATP5F1C=Atp5c1, ATP5F1D=Atp5d, ATP5F1E=Atp5e, ATP5PB=Atp5f1, ATP5MC1=Atp5g1,
   ATP5MC2=Atp5g2, ATP5MC3=Atp5g3, ATP5PD=Atp5h, ATP5PF=Atp5j, ATP5PO=Atp5o, ATP5ME=Atp5i, ATP5MF=Atp5j2, ATP5MG=Atp5l, TIMM8A=Timm8a1,
   HPRT1=Hprt. A human member with no mouse match, or whose symbol maps to more than one primary-assembly gene id, is listed as unresolved
   and excluded (no member is replaced by a "close" gene). One-to-one orthology is assumed, not verified (UNVERIFIED for paralog-rich
   families such as PDK, SLC16, SLC2, HK, LDH).
7. Sex of each animal is described (Xist and Y-linked Ddx3y, Kdm5d, Eif2s3y TPM) and not adjusted; an arm imbalance in sex is a named limit.

## 5. Gene sets (frozen; the same as iteration 5, nothing added after seeing a value)

Source of the iteration-5 sets: hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv ('symbol' column, contrast C_hNPC rows) plus the same
"extra" members that p7_organoid_same_sets.py re-adds (SLC7A11 to ISR; PPP1R15A to UPR; PKM to Glycolysis; PDK4 to PDK; SLC16A3 to lactate
transporters; TOMM70 and TIMM23 to import; NDUFA11 to OXPHOS), read by the script from that file by sha256 (cdbac348...647b1, the p6 table
hash in p7_params.json). Sets: ATF4 (single gene), ISR_targets (ASNS, CHAC1, TRIB3, DDIT3, PHGDH, PSAT1, PSPH, SLC7A11, ATF5, PCK2, SESN2,
GADD45A), UPR_branches, OXPHOS_nuclear, Mito_translation, Mito_import, Glycolysis_lactate (10: SLC2A1, HK2, PFKP, ALDOA, PGK1, ENO1,
LDHA, PKM, BNIP3, LDHB), PDK_family (PDK1 to PDK4, also each gene alone), Lactate_transporters (SLC16A1, SLC16A3 alone), the marker sets
Mk_* of gse156243/marker_sets_declared.tsv as used in iteration 5, Ctl_housekeeping (ACTB, GAPDH, TBP, PPIA, HPRT1, B2M, TUBA1B, EEF1A1,
RPLP0, UBC, YWHAZ, GUSB), and the negative-control class Ctl_cytosolic_ribosome, which for the mouse is declared as the genes whose
Ensembl-92 symbol matches ^Rp[ls][0-9]+[a-z]?[0-9]?$ (this excludes pseudogenes, Rplp*, Mrpl*, Mrps*, Rpl3l-type paralogs), minus Rps4y1 and
Rps4y2 (Y-linked). The human ribosome list of iteration 5 contained pseudogenes of the CAGE matrix and is not transferable to the mouse key.

Set-dependence variants, declared NOW because iteration 5 flagged those statements set-dependent but the lists behind its "19-gene panel",
"four canonical markers" and "10-gene neuronal panel" are not recoverable from the committed files (they were made in verification).
These P4 lists are therefore P4's own declarations, to be read as alternatives to the iteration-5 primary sets and NOT as a reproduction of
the iteration-5 verifier's lists:
- Glycolysis_19 = Glycolysis_lactate plus SLC2A3, SLC16A3, HK1, GPI, TPI1, GAPDH, PGAM1, PFKL, ENO2.
- Prog_core4 = SOX2, PAX6, HES1, HES5 (transcription-factor progenitor markers); Prog_9 = the iteration-5 Mk_radial_glia_progenitor set
  (includes NES and VIM); Prog_NESVIM = NES and VIM alone (reported per gene).
- Neuro_10 = TUBB3, MAP2, DCX, STMN2, SYT1, RBFOX3, NEUROD2, NEUROD6, SNAP25, NEFL; Neuro_5 = the iteration-5 Mk_neuronal_pan set.
- ISR_core5 = CHAC1, TRIB3, PSAT1, SESN2, ATF5 (the genes iteration 5 recorded as carrying the shWWOX rise) and ISR_org3 = CHAC1, TRIB3,
  SESN2 (carrying the organoid fall); plus a leave-one-gene-out table of ISR_targets (12 means). These are sensitivity sets; the decision
  below uses ISR_targets only.
- Myelin_OL = Mbp, Plp1, Mog, Mag, Mobp, Cldn11, Cnp, Mal, Opalin, Ugt8a: not a WWOX hypothesis; the deposit's own series text says myelination and
  oligodendrocyte-maturation transcripts are reduced, so this set is the positive control of the dataset and the composition indicator.
Mouse-specific caution: "progenitor" and "neuronal" markers in P17 bulk hippocampus measure what is left of progenitors (dentate
subgranular zone, glia) and the neuronal fraction; they are not comparable with the organoid or the 2D line in cell-state terms.

## 6. Controls

1. Perturbation depth: summed Wwox TPM per animal and per-arm reduction (1 - mean_KO / mean_ctl) for H_S, H_N, H_null, C_S. A contrast
   with less than a 50 percent reduction is declared UNINFORMATIVE about Wwox loss BEFORE any other gene is considered and is not counted.
2. Matched random sets (above) for every set; Ctl_cytosolic_ribosome and Ctl_housekeeping as unrelated classes; the transcriptome-wide
   spread of centred R (median, IQR) per contrast.
3. Control-versus-control contrasts CC_SW, CC_NW, CC_SN: a set that lies outside its own null in any of them is labelled
   BACKGROUND-SENSITIVE and cannot be called "moved".
4. Positive control of the dataset: the Myelin_OL set should be lower in the knockouts (the deposit's own statement); if it is not lower in
   any hippocampal knockout contrast, the contrasts are reported as not behaving as described.
5. The cortex contrast C_S is the independent-tissue replication of H_S (same genotype, other region, other animals).

## 7. Decision criterion (the one that could change a decision)

Counted contrasts: H_S, H_N, H_null, each only if its depth control passes. A set is "MOVED" (direction = sign of its centred mean) only if
ALL hold: (a) in at least two of the counted contrasts its centred mean lies outside the 2.5th to 97.5th percentile of its own matched
null, with the same sign; (b) in each of those contrasts it is "separated" at animal level (section 4.5); (c) it is not outside its null
with the opposite sign in the third counted contrast; (d) it is not BACKGROUND-SENSITIVE; (e) the sign is the same at universe thresholds
0.5, 1 and 2; (f) the cytosolic-ribosome control is not outside its null with the same sign in those contrasts (otherwise the set is
"NON-SPECIFIC": a shift shared with an unrelated class). A set meeting (a) to (f) and ALSO outside its null in C_S with the same sign is
"MOVED and replicated in cortex"; with C_S inside the null it is "MOVED, not replicated in cortex".
Applied to ISR_targets:
- MOVED lower: the mouse sides with the organoid sign; MOVED higher: sides with the shWWOX line; either is "concordant in sign at
  transcript level in a third system", nothing more. NOT MOVED, NON-SPECIFIC, BACKGROUND-SENSITIVE or inconsistent: the ISR sign stays
  UNRESOLVED and the third system does not break the tie.
Applied to Glycolysis_lactate, Glycolysis_19, PDK_family and Pdk1: same rule; a statement is "set-independent" only if the 10-gene and
19-gene definitions both give MOVED in the same direction; "set-dependent" if only one does or they differ in sign. For Prog_core4,
Prog_9, Prog_NESVIM, Neuro_5, Neuro_10: same. A single gene is never called differentially expressed; per-gene numbers are listed with
per-animal TPM and the animal-level range only.

## 8. What each outcome would mean

| Outcome | Consequence (transcript level only) |
|---|---|
| ISR_targets MOVED lower | the third system sides with the organoid; supports "ISR targets are lower with Wwox loss in neural tissue" as a transcript sign in two of three systems, still no protein/phospho measure; weakens the progenitor-line rise as the general case |
| ISR_targets MOVED higher | sides with the shWWOX line; the organoid sign becomes the exception; a drug-signature reversal built on the organoid's ISR-lower list would have no support in a more physiological in-vivo deletion |
| ISR_targets not moved / non-specific / background-sensitive | the sign conflict stays UNRESOLVED; the third system cannot discriminate; the matched protein/phospho plus target-mRNA experiment (systems comparison section 3.1(c)) remains the next step; no need rank changes |
| Depth control fails in a contrast | that contrast is uninformative and is excluded; if all fail, the question is restricted to descriptive and stated so |
| Glycolysis/PDK/progenitor/neuronal sets | each statement is re-labelled set-independent or set-dependent by the rule in section 7, in the mouse only; no human statement is changed by a mouse result alone |
Stable regardless of outcome: nothing here measures ATF4 protein, eIF2alpha phosphorylation, PERK/GCN2 activity, translation, OCR/ECAR,
PDH activity, lactate or flux; Atf4 mRNA is not Atf4 activity (translationally controlled); a missing or low value is not biological
absence; no result validates or refutes a drug-signature reversal; nothing concerns a person or an allele.

## 9. Known limits

Transcript only; 2 to 3 animals per arm, gene-level null ignores animal variance; Salmon TPM, no counts, so no count-based universe or
dispersion model; arm-level composition (oligodendrocyte maturation, myelination, neuronal/glial fraction) changes with the phenotype and
can mimic set changes; the germline null at P17 is systemically ill; cortex S controls are said by the census to vary 8 to 26 TPM in Wwox
(control-to-control spread, so cortex is a weaker replication); S/N driver identity, control genotype, sex and batch UNVERIFIED; mouse
versus human orthology is symbol-based; the human sets were declared for a human lineage; the sets carry the author's prior knowledge,
not an external validated signature; no multiplicity correction is made and none is claimed because nothing is called significant.

## 10. Reproducibility

Run with python3 -I p4_mouse_same_sets.py <hippocampus.txt.gz> <cortex.txt.gz> <ensembl92_cdna.fa.gz> <p6 per_gene_in_sets.tsv> <out_dir>;
numpy only; seed 20261029; outputs are deterministic. Raw files are not committed (hippocampus table 4.8 MB, cortex 2.6 MB, Ensembl FASTA
about 50 MB); their URLs and sha256 are in inputs/SHA256SUMS and inputs/PROVENANCE.md. Deviations from this declaration are listed in the
README as deviations and are not edited in here.
