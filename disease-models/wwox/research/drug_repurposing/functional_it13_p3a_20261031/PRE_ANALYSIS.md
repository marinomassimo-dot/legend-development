# P3a pre-analysis (written and committed before any expression value of the panels below was opened)

Scientist, task ORCH-ROADMAP-IT13-20261031, package P3a, branch `task/it13-p3a`. Not medical advice. Transcript-level only: RNA is not protein is not current.

## What I had seen before writing this
* The IT6 P4 package (`mouse_wwox_p17_it6_p4_20261029`) summary: ISR/OXPHOS/glycolysis/progenitor/neuron/myelin sets, deletion depth (Wwox TPM down 85, 94, 91 percent in the three hippocampal contrasts; cortex 68 percent), a control-versus-control background (the Cre-line control groups differ from wild type), and `set_summary.tsv` rows for `Neuro_5`, `Neuro_10` (pan-neuronal; centred means +0.14 to +0.36, not separating from the matched null). `Mk_GABAergic` there is ONE gene (DLX2): the interneuron axis was **not** measured.
* I had NOT opened any value for the genes listed in section 2.

## 1. Data and contrasts (all P17 mouse, Salmon TPM, deletion verified by IT6 P4; deposit sha256 in `inputs/SHA256SUMS`)
Within-line contrasts are primary (S: neuron-targeted deletion, hippocampus 3 KO v 2 ctrl and cortex 3 KO v 4 ctrl; N: neural stem/progenitor-targeted deletion 2 v 2; null 2 v 3). The control-versus-control contrasts (CC_SW, CC_NW, CC_SN) are the empirical background for the same sets: an effect is read only against that band.
No variant WWOX protein exists in these animals (deletions/null): the dataset can speak to consequences of loss, not to any variant.

## 2. Panels (declared now, not edited after)
* PAN (pan-neuronal): Snap25 Syt1 Rbfox3 Stmn2 Map2 Syp Nefl Eno2
* EXC (excitatory): Slc17a7 Camk2a Neurod2 Neurod6 Satb2 Tbr1
* INH_ALL: Gad1 Gad2 Slc32a1 Dlx1 Dlx2 Dlx5 Lhx6
* PV: Pvalb Kcnc1 Kcnc2 Lhx6
* SST_NPY: Sst Npy Cort Nos1
* VIP_CCK: Vip Cck Calb2 Htr3a
* IEG (activity-regulated): Fos Fosb Npas4 Arc Egr1 Egr2 Egr4 Junb Nr4a1 Bdnf Btg2 Dusp1
* ASTRO: Gfap Aqp4 Aldh1l1 Slc1a3 ; MYELIN: Mbp Plp1 Mog Mag Mobp (composition covariates)
* Individual genes (descriptive, no set test): Slc12a2 Slc12a5 Kcnq2 Kcnq3 Kcnj3 Kcnj6 Kcnj9 Kcnj10 Hcn1 Hcn2 Cacna1g Cacna1h Scn1a Scn2a Scn8a Gabra1 Gabra2 Gabrb2 Gabrb3 Gabrg2 Grin1 Grin2a Grin2b Grin2c Grin2d Gria1 Gria2 Panx1 Atp1a3 Kcna2 Grm3

## 3. Statistic
Per gene log2((mean KO + 0.5)/(mean ctrl + 0.5)); set score = mean over measurable members (mean TPM >= 1 in at least one arm, reported with 0.5 and 2.0 as sensitivity), median-centred on all genes with mean TPM >= 1; null = 10,000 expression-decile-matched random sets (seed 20261031) as in IT6 P4; animal level: per-animal mean log2(TPM+0.5) over the set, exact permutation p of the group labels; leave-one-gene-out sign. Selectivity contrasts: INH_ALL minus PAN, PV minus PAN, SST_NPY minus PAN, INH_ALL minus EXC (difference of centred set means; its band = the same difference in the three CC contrasts and in the 10,000 matched draws).

## 4. Predictions (fixed now; direction of change is not taken as benefit, only as evidence for a reading)
* R-dis (interneuron-selective deficit): INH_ALL, PV or SST_NPY lower than PAN and EXC by more than the CC band, in S and null hippocampus.
* R-comp (composition or generalised neuronal change): INH sets move with PAN/EXC (selectivity contrasts inside the band); the IT6 positive PAN offset (+0.14 to +0.36) is the reference.
* R-act (network hyperactivity at the time of sampling): IEG set higher than matched null in S and null, with animal separation; in N (stem-cell deletion, no spontaneous seizure expected) not. A raised IEG set cannot separate seizure-at-sacrifice from interictal hyperactivity and is not a measure of E/I.
* R-null: nothing separates from the matched null and the CC band at n = 2 to 4; then the deposit cannot answer, the abstention stands and the answer to the question is the stated resolving measurement.
No test is declared as confirmatory. Expected from power: at 2 to 3 animals per arm the minimum exact permutation p is 0.1 (3 v 2) or 0.167 (2 v 2): no panel can reach p < 0.05 by animals alone; separation is read as non-overlap of the animal scores plus matched-null position, as in IT6 P4.
