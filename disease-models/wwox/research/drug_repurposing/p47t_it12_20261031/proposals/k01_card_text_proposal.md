# Proposal (not applied): text for card K01 (`cards/K01_hif_axis_glycolytic_shift.card.json`)

Proposed by `scientist-d`, IT12 P2-P47T, 2026-10-31. Nothing outside the package folder was edited. Not medical advice.

## 1. `p4_fields.functional_evidence_available`: replace the last sentence

Current last sentence: "Unresolved in vivo: hallmark hypoxia, apoptosis and glycolysis gene-set enrichment in the P47T knock-in brain (direction not stated in the text)."

Proposed: "In vivo, partial loss: in the P47T knock-in brain (adult homozygotes with chronic seizures, bulk RNA, 5 v 5 animals; cerebellum 4 v 3) the hallmark HYPOXIA, GLYCOLYSIS and APOPTOSIS gene sets are enriched in the mutant in PFC, cortex and hippocampus (Fig 8b: normalized enrichment about 1.5 to 2.0, 1.3 to 1.5 and 1.3 to 1.8; direction rests on convention, adjusted p is not reported) and weakly in cerebellum (Fig 9c: HYPOXIA 1.2, lowest of the ten bars shown). A reanalysis of the deposit (GSE215425, IT12 P2-P47T) shows that this enrichment is a broad modest shift of many hallmark members, led by glycolytic enzyme transcripts (Aldoa, Pgk1, Pfkp, Pkm, Tpi1, Hk2, Ldha; +0.1 to +0.6 log2) with extracellular-matrix and reactive genes among the larger changes, and is NOT by the selective hypoxia-response genes that rise in the human organoid: Bhlhe40, Ndrg1 fall, Ddit4, Ankrd37, Egln3 are flat, only Adm is higher (low expression, p 0.04 to 0.18). Hif1a, Epas1 and Egln1 transcripts are flat or lower. Two of five mutants carry a strong activity-dependent transcript signature (Nptx2, Bdnf) in all forebrain regions, and the one organoid-like signal in hippocampus is one of them. Transcripts only; no HIF protein, hydroxylation, oxygen condition or lactate was measured, and the deposit has no per-animal seizure or age record."

## 2. `p4_fields.temporal_or_model_limit`: append

"The three in-vivo mouse transcript contrasts now available (P17 conditional and germline deletion, four contrasts; P47T hypomorph, adult) do not reproduce the organoid's selective hypoxia-response pattern; the pattern is therefore, for now, a feature of one human organoid dataset (4 v 2 libraries, one WT line) and not a general WWOX-deficient neural finding. The P47T is a partial-loss allele with seizures and gliosis: it is neither a null nor free of the activity and composition rivals."

## 3. Statement (3) in the IT10 restatement list ("hNPC rows") and (4) ("mouse P17 brain shows no elevation")

Add after (4): "(5) adult P47T forebrain shows a modest glycolytic-enzyme transcript increase without the selective hypoxia-response genes (IT12)."

## 4. `endpoint_pursued`: three additions to step 0 (the structure of arms A to C is unchanged)

(a) In vivo anchor, P47T hippocampus and cortex: nuclear and cytoplasmic HIF-1alpha and HIF-2alpha protein and hydroxylated HIF by rapid perfusion fixation or in-situ freezing (HIF protein is lost within minutes after death; the deposited RNA tissue cannot be reused for this), pimonidazole adducts as a tissue-hypoxia marker independent of HIF, lactate by in-situ freezing or MRS, with the per-animal video-EEG seizure count of the 24 hours before collection recorded as a covariate and a pre-seizure-onset age group beside the adult group.
(b) Target panel read as a panel, not as the six IT7 genes: Bhlhe40, Ddit4, Ndrg1, Egln3, Ankrd37, Adm (the genes that separated the organoid pattern from a glycolytic-enzyme shift) beside Pgk1, Aldoa, Pkm, Pfkp; each reported individually; Ndrg1 and Bhlhe40 also need an oligodendrocyte-composition check (both are reported in oligodendroglia in my background knowledge; not verified in this package).
(c) The activity-silenced arm (already in step 0) becomes decisive for the in-vivo question: slices or cultures from the mutant with and without tetrodotoxin (or an equivalent silencing) before harvest.

## 5. Assertions

DA-K01-002 is unchanged. Add a new disease assertion for the P47T observation as `INFERENZA` / `COMPUTATIONAL_RESULT`, context mouse P47T/P47T adult bulk, direction "mixed: glycolytic-enzyme transcripts up modestly; selective hypoxia-response genes not up", locator `disease-models/wwox/research/drug_repurposing/p47t_it12_20261031/premises.tsv` rows P9 to P12. The six IT7 genes appear there as observations only (guard IT7_READOUT6).
