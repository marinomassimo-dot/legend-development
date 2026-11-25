# ADV-233 pre-registration: do two P47T animals carry the other carried P47T signatures? (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Assignment ADV-233 (ADV message 2026-11-25). Held data and held primary only; no download, no spend, no contact. Checkpoint AC, RP-045, ADV-174/175 untouched. Frozen before any per-animal hallmark score, any leave-two-out run or any random-set run (time and digest in the companion files).

## 1. What had been seen before freezing (honest list)
* **IT12 (`p47t_it12_20261031`, 2026-10-31) already identified M6 and F8** as animals with Nptx2 and Bdnf 20 to 30 fold above wild type in the three forebrain regions ("high-activity", post hoc); the hippocampal HIF selective shift disappears without M6; M6 has the highest astrocyte score. My ADV-231 post hoc observation was therefore **not new** (my duplicate check searched gene names, not animal identifiers). IT12 ran leave-ONE-animal-out for its own sets only (HIF, NRF2 and others), never leave-two-out and never per animal on the inflammatory or lipid hallmarks.
* IT12 hallmark NES and BH q per region (all animals), including HPC/CTX/PFC TNFA, IL6, INFLAMMATORY, HYPOXIA, GLYCOLYSIS, and CB cholesterol, fatty acid metabolism, mTORC1 and others (RP-036 numbers).
* ADV-231: STAT3-axis per-animal scores computed on raw counts **without library-size normalisation** (a flaw I now state: the table is integer counts, not "normalised counts" as my ADV-231 result says; the frozen ADV-231 calls median-centre every contrast and are not affected, the post hoc score is). Library sizes differ by up to about 25 percent between animals; M6 and F8 are not consistently large.
* Primary (held; complete read receipt FTR-20260913-36828035-03): a text search before freezing found no animal identifier (no M6 or F8), no batch note, no per-animal age; spontaneous generalised seizures in adult homozygotes (3 monitored animals, 11 to 22 seizures in 43 to 53 h); RNA-seq animals 150 to 280 days old.
* NOT seen: any per-animal score on a hallmark set; any result without M6 and F8; any random-set null.

## 2. Frozen design
**Normalisation and engine:** IT12's own script `p47t_reanalysis_it12.py` (TMM, log2 CPM prior 2, per region), unchanged, run twice: all animals, and with the M6 and F8 columns removed from every region (leave-two-out). Hallmark release: MSigDB mouse 2023.2.Mm `mh.gmt`, same file as IT12 (sha256 1d4c72ee...). For per-animal scores: set score = mean over the set's genes (genes with mean CPM at least 1 across the region's animals) of centred log2 CPM, centred on the mean of all animals of the region; the same normalisation functions copied from IT12.

**Carried inferences and their sets:** (a) the authors' upstream-regulator inference TNF, NF-kB, IL1B, RELA (IT6 row 5): proxy HALLMARK_TNFA_SIGNALING_VIA_NFKB (an enrichment tool cannot be re-run; the proxy is stated); (b) "IL6-JAK-STAT3 set positive": HALLMARK_IL6_JAK_STAT3_SIGNALING; (c) HALLMARK_INFLAMMATORY_RESPONSE; (d) HIF/K01 anchor: HALLMARK_HYPOXIA, HALLMARK_GLYCOLYSIS; (e) RP-036 (cerebellum): HALLMARK_CHOLESTEROL_HOMEOSTASIS, HALLMARK_FATTY_ACID_METABOLISM, HALLMARK_MTORC1_SIGNALING; (f) L01: NRF2_5 (IT12 set); (g) the reactive-pan list (C3, Cd44, Vim, Timp1, Cebpd, Stat3, Socs3, Lcn2, Chil1, Serpina3n): it belongs to the human organoid panel, **no P47T inference is carried on it**; scored here as a descriptive extra, excluded from dispositions.

**Stated threshold of each carried inference (no new threshold):** the repository's own reading of these hallmark results is "enriched" = positive NES with BH q < 0.05 over the 50 hallmarks (RP-036 wording). For NRF2_5: IT12's rule, mean difference >= +0.30 and exact p <= 0.05 (met in HPC only, with all animals).

**"Carried by the same two animals" (forebrain: HPC, CTX, PFC):** BOTH (i) M6 and F8 are ranks 1 and 2 on the set score among all 10 animals in at least two of the three forebrain regions, AND (ii) the leave-two-out run loses the threshold in at least two of the regions where the full run met it. **"Robust to leave-two-out":** the threshold is still met in every region where the full run met it. **Otherwise "not resolvable"** (partial loss, or the two conditions disagree).
**Cerebellum:** the mutants are M6, F8 and F10 only; removing two leaves one mutant, so leave-two-out is **not testable**. Instead: report each animal; "all three mutants above every wild type" = robust per animal; "M6 and F8 above the wild-type maximum, F10 not" = carried by M6/F8; else not resolvable.

**Counter-check (library-wide variability):** for each carried set and forebrain region, 1000 random sets matched on size and on mean-expression quintile (seed 20261125); the fraction in which M6 and F8 are ranks 1 and 2 among all 10 animals (chance for two named animals: 1 in 45). If random sets show it often (more than 10 percent), a "two-animal" pattern is not specific to the biology of the set.

## 3. Predictions (frozen)
* P1: M6 and F8 are ranks 1 and 2 for TNFA, IL6 and INFLAMMATORY in at least two forebrain regions.
* P2: at least two of those three sets are "carried by two animals" under the rule.
* P3: HYPOXIA or GLYCOLYSIS keeps its threshold in at least one forebrain region after removal.
* P4: in the cerebellum, cholesterol or fatty acid metabolism is not "carried by M6/F8".
* P5: random matched sets put M6 and F8 in ranks 1 and 2 in more than 10 percent of draws in at least one forebrain region (a general shift of those two libraries).

## 4. Outputs
Folder: the two IT12 run outputs (GSEA tables), the per-animal scores, the random-set table, scripts (print-only or writing only to a named output folder), a receipt for the targeted re-read of the primary (animal-note question), a disposition table per carried inference with the RP and card each touches, and proposed wording (not applied).
