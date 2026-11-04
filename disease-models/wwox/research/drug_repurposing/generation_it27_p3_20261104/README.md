# IT27 P3/P4: which verified WWOX knowledge the generator now reads, and what it changes (S8)

Non-canonical research material, not medical advice. Nothing here is a finding; every proposal stays conditional (`qualified = no`).

## Decision on the P1 results (what was chosen, what was not)
| Candidate input | Class after verification (`verification_it27_p1_20261104`) | Used by the generator? | Why |
|---|---|---|---|
| P47T v WT, PFC and parietal consensus (81 genes: DESeq2 padj<0.05 and |log2FC|>=1 in both regions, OLS FDR<0.10 in both, stable in ten leave-one-animal-out refits) | CONFIRMED, one origin (ten animals supply all libraries, residual correlation across regions 0.28) | **No, not as drug seeds** | 15 of the 81 look like tissue-restricted, non-neural-type transcripts by gene name (my reading, not an enrichment test; Atp2a1, Mybpc1, Mybpc3, Tnnc1, Myl4, Lhx3, Npw, Sct, Ighg1, Fgr, Cd28, Prtn3, F2, Ucma, Hmcn2): a dissection or composition rival that the deposit cannot exclude; only 22 of 81 have any DGIdb target; role is unknown. Seeding it would feed reversal scoring with a possible tissue artefact. Kept as a descriptive candidate list. |
| 56 genes called in all four deletion contrasts (GSE158681/2), myelin-enriched | DESCRIPTIVE_USABLE (n 2-4, TPM, red-cell transcripts look technical) | No | A maturation or composition question, not a drug lever; needs a role-resolving experiment first. |
| MTBLS12344 2-hydroxyglutarate | VERIFIED, narrower: nominal interaction only, already published, low pertinence | No | Cannot guide a pharmacological selection. |
| P47T contrast of the genes that ARE already seeds (Q2 module, Q3 ISR set, Q8 NFE2L2) | CONFIRMED | **Yes, as an annotation** | Same seeds, a third system with a different perturbation (partial-loss missense). |

## Consumption path (what the code does with it)
source `verification_it27_p1_20261104/results/p1a_all_regions_own_results.tsv.gz` -> representation: 7 rows appended to `generation_it22_p1_20261103/inputs_it22/seed_annotations.tsv` by `build_annotations_it27.py` (tag `P47T_PARTIAL_LOSS_MOUSE_{CONCORDANT|MIXED|DISCORDANT}`, rule fixed in the script: three regions, a |log2FC| under 0.15 carries no sign) -> read by `run_generation_it21.py` (`seed_guard_limits`, annotation set per seed id) -> column `seed_guards` of the proposal table -> no effect on order: the tags are not in `SUPPORT_LIMITING_GUARDS`.
Tags: Q2 SLC2A1, HK2, LDHA CONCORDANT (log2FC +0.2 to +0.9 in all three regions; none individually decisive); LDHB, BNIP3 and Q3 PSAT1 and Q8 NFE2L2 MIXED. No DISCORDANT seed exists. (A first draft called PSAT1 DISCORDANT on log2FC -0.03 by sign alone; the 0.15 floor was added for that defect, after seeing it, and is stated.)

## Measured (engine re-run on the refreshed action table, then `propose`; scratch runs, tables committed in `results_s8/`)
| Comparison | Rows | Changed |
|---|---|---|
| committed S7 v control run (old annotations) | 994 | **0 cells**: S7 reproduces exactly |
| control v S8 (new annotations) | 994 | `seed_guards` on 69 proposals; nothing else |
| eligible rows | 220 v 220 | 0 |
| hand-overs | 15 v 15, same ids | 0 |

Reading: the new knowledge is now visible on the 69 proposals whose contributing seeds include those genes (the Q2/Q3/Q8 families), and it changes no selection. That is the honest outcome: concordant, non-significant evidence from a different perturbation cannot move an order that is not allowed to rest on it. The second case (the module in the second system) is the glycolysis set only: the Q3 ISR set has six uncertain-direction seeds, which carry no tag.
Also in S8: `mechanism_clusters_it21.tsv` carries the new `tie_size` column (exact ties on the whole order key; rule unchanged, see `alternatives_it27_p5_20261104`).

## Limits
One origin; partial-loss missense with protein present; mixed tissue; 5 v 5; DESeq2 only (no second count method). Concordant is not confirmation, and partial loss is not complete loss. No seed was added, so no new question or hypothesis was generated.

## Addendum: the PX-478 modality barrier (included in `results_s8/`)
`modality_declarations_it27.tsv` (read by `load_modality_declarations` in `run_generation_it21.py`) declares PX-478 `protein_or_peptide` -> `small_molecule` at structure level (a single alpha-amino acid, no peptide bond; ChEMBL types it `Protein` with no sequence; evidence from a second actor in `verification_it27_p8_20261104`). The modality filter is not loosened: a declaration applies only while the computed modality still equals its `from_modality`, and it is one row (romidepsin, voclosporin and GDC-0152, which have peptide bonds or a peptidomimetic backbone, stay `protein_or_peptide`). Effect against the version without it: one proposal (IT21P2-0003) changes; its blocker moves from `modality_protein_or_peptide_not_small_molecule` to `decided_in_earlier_qualification_record` (it was qualified in IT9, card K01). Eligible rows 220 v 220, hand-overs 15 v 15 with the same ids: the false barrier hid a prior decision, it did not hide a new candidate.
