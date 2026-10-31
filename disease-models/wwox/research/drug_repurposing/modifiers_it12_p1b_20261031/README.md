# IT12 P1-alt (scientist-b): genetic modifiers and suppressors of the WWOX defect

Package `modifiers_it12_p1b_20261031`, branch `task/it12-p1b`, 2026-10-31. Public edition, WWOX-DEE genotype class; hypotheses, not medical advice.

## 1. Decision

1. **GSE298081 cannot answer the question and the line is stopped as a source of pharmacological candidates.** It holds one WWOX-null HAP1 clone (c2.2; leukaemia-derived haploid line), one screen, no replicate screen, no parental control of its own and no re-expression arm. The contrast is an epistasis contrast (second knockout versus WT expectation), not a rescue contrast, and WWOX loss has no fitness phenotype in this readout (WWOX guides neutral in 39 WT screens, mean log2FC +0.158), so there is no WWOX-defect phenotype in it for anything to suppress. I did not substitute any other contrast.
2. **The authors' own scores exist and were read** (Zenodo MIT record, Data S1/S4/S8), which supersedes the IT11 crude count comparison: WWOX has 88 FDR calls (46 negative, 42 positive, 5 stringent), rank 18 from the sparsest of 298 screens; its profile resembles no other query (max r 0.085). The paper never mentions WWOX (0 matches), so the authors report no WWOX synthetic-lethal or suppressor gene.
3. **Calls are listed, not developed.** The positive calls include a mitochondrial-oxidation module (PDHA1 +0.567, CS +0.566, LIPT1 +0.345, NDUFAF1 +0.318) and the negative calls a glucose-uptake pair (SLC2A1 -0.593, HK2 -0.464). All sit near the FDR 0.1 limit in an unreplicated screen (same-sign call overlap between screens of one query gene: median 12 to 22 percent), most are generic hub genes (same-sign in 11 to 40 of 298 screens) and the system is non-neural.
4. **No new neural or neurodevelopmental suppressor exists in the public literature I could reach.** The only genetic rescue of a neural functional endpoint is Ldh lowering in the Wwox-RNAi + Abeta42 fly (PMID 42909904), already card E02. The other fly work puts Wwox as modifier of other genes (wrong direction; IT10 P2.3 row b confirmed at the source, not re-concluded). Mouse: GSK3/lithium (G01) and HIF (K01) are carded and are pharmacological or non-neural. No zebrafish, worm, yeast, rat cross or screen with a Wwox-null modifier endpoint was found (search floor, not a census).
5. **Three comparable candidacies were qualified (`candidates.tsv`); none is advanced.** C1 Ldh lowering: unchanged, E02. C2 PDH/TCA-entry loss: runs against E03, DROP as a lead, keep as counter-evidence, free extra probe arm. C3 glucose-uptake/hexokinase dependence: an aggravator, a caution note for E04 and 2-deoxyglucose-class ideas, not a candidate. **Probe verdicts: none needs a dedicated experiment. Development verdicts: none.**
6. **Conditional/limits.** Lever identity, active moiety, potency and exposure were NOT read at source: ChEMBL REST returned HTTP 500 on all attempts today (service error, not absence of data), and the DepMap portal is behind a human-verification page (no workaround attempted). Both are reopening items.

Reopening condition for the whole line: (a) a second WWOX-null clone or a WWOX re-expression screen in HAP1 (data holders), or (b) any WWOX-null versus corrected neural cell genetic-interaction or knockdown readout with a viability or activity endpoint, or (c) a new Wwox/WWOX suppressor with a neural endpoint in Drosophila, zebrafish or mouse. Measurement that would distinguish the alternative explanations of the HAP1 calls: a replicate screen of the same clone (chance), a second independent clone (clone-specific mutation or ploidy), guide-level alignment of EIF5AL1 (multi-mapping artefact), comparison with the hub tables (generic positive-interaction genes; done), a re-expression arm (WWOX-dependent).

## 2. What I read before forming questions (informed, not blind)

Brief and CLAUDE.md router; `roles/scientist.md` (header and first 50 lines), LEGEND_CORE section titles 21c to 21e (headings located, bodies not re-read in this run: declared); `matching_guidance_v3.md` first 60 lines (logic 7); `ops_it11_p5_20261031/scouting_it11.md` (GSE298081 paragraph), its README grep, `gse298081_wwox_ko_screen_check.py` and `evidence/gse298081_wwox_ko_top_both_ends.tsv`; `recovery_it10_p23_20261031/paths_verdicts.tsv` (path b row and others); `guards.tsv` (three guard tags); cards K01, L01, M01, G01, E02, E03 (`p4_fields`, comparisons). Not read: `roadmap_current.md`, `generation_it9_p2_20261030/v3/README.md`. So the questions were shaped by knowing IT11 found "no outlier" and IT10 found "wrong direction".

## 3. Usability table

See `usability_table.tsv` (accessibility, terms, identity, perturbation, contrast, replicates/timepoints, library and controls, data level, endpoint, confounders, computed call reproducibility, verdict; DepMap, fly genetics, Ldh rescue). Condensed:

| item | GSE298081 |
|---|---|
| access / terms | public GEO; paper CC BY-NC; authors' Zenodo record MIT; Mendeley copy licence not read |
| samples | GIN352 = GSM9006656 (T0), GSM9006851, GSM9007046, GSM9007241 (T13 A/B/C); 298 screens, 39 WT screens |
| perturbation | CRISPR indels (1 bp, 55 bp) in one clone, then TKOv3 library; no rescue, no drug |
| contrast | query vs WT-expectation (qGI); no own parental control; MCMC replicate analysis 0 |
| endpoint | proliferation fitness, 13 doublings, rich medium (25 mM glucose, 1 mM pyruvate) |
| missing | rescue/re-expression arm; second clone; replicate; neural cell; WWOX phenotype |

## 4. Evidence by source (depth)

| source | depth | what it gives |
|---|---|---|
| GSE298081/82 SOFT | metadata, whole file parsed | design, four GIN352 samples |
| PMC13281610 (Cell 2026, PMID 42049019) | full text XML; design, qGI, replicate, suppression, data-availability passages read; whole text searched for WWOX | no WWOX statement; thresholds |
| Zenodo 20734737 Files S1, S4, S8 | tables parsed in full by `gin352_extract_it12.py`, `replicate_overlap_it12.py` | the 88 calls, WT neutrality of WWOX, hub counts, profile correlation |
| PMC13684411 (PMID 42909904) | Ldh-rescue sentences re-read; whole paper covered by repository receipts | the one neural genetic rescue (fly), carded |
| PMC3016910 (21075834), PMC4547717 (26302329) | genetic-interaction passages read | Wwox as modifier of others; wrong direction |
| PMC11828923 (39952983), PMC8187448 (34103633) | text searched | no modifier, no WWOX dependency data |
| 16007179, 26390919 | not re-read | (IT10 abstract level) |
| Europe PMC searches | titles only | floor, not a census |

Locators: `premises.tsv`.

## 5. Candidates (`candidates.tsv`)

| id | modifier | evidence level | context | verdicts |
|---|---|---|---|---|
| P1B-C1 | Ldh lowering | rescue (fly epistasis) | fly neurons, Abeta42 | probe: as E02; development: not advanced; HAP1 LDHA +0.016 (FDR 0.88) does not corroborate |
| P1B-C2 | PDHA1/CS/LIPT1/NDUFAF1 loss | association | HAP1 | probe: free arm in E03 experiment only; development: DROP; counter-evidence to E03 |
| P1B-C3 | SLC2A1/HK2 dependence | association (aggravator) | HAP1 | not a candidate; caution note for E04 |

Convergence with K01/L01/M01/G01: none claimed. K01 is sign-compatible (the clone looks glycolysis-weighted) but one clone cannot separate WWOX from clonal adaptation, and SLC2A1/HK2 are IT7 seed rows. L01, M01, G01, E01 genes show no interaction (non-informative for neural premises). Guard tags IT7_READOUT6 (reported, not scored), ISR_SIGN_UNRESOLVED (ATF4 +0.033, EIF2AK1/3/4 reported, no ISR reversal scoring), HELD_OUT_ENDPOINT (not touched) were respected.

## 6. For the batch path

Files, not applied: `proposals/card_and_need_proposals_it12_p1b.md` (card notes for E03/E04/K01/E02, needs N-P1B-1..4, proposed receipts, registry note closing the IT11 WATCH). Package files: `README.md`, `usability_table.tsv`, `candidates.tsv`, `premises.tsv`, `gin352_extract_it12.py`, `replicate_overlap_it12.py`, `evidence/` (summary.json, profile_correlation.json, s1_gin352_row.json, selected_genes_qgi_fdr.tsv, wwox_gin352_significant_gis_with_hubs.tsv, replicate_call_overlap.json, geo_gin352_samples.txt, source_sha256.txt). Run: `python3 -I gin352_extract_it12.py <unzipped GIN-v1.0.4> <out>`. Derived tables hold only the 88 WWOX-query calls and selected genes (attribution: Billmann, Costanzo et al., Cell 2026; Zenodo 10.5281/zenodo.15320010 MIT). Nothing under `files/`, cards, needs, registries or the ledger was touched.

## 7. Disclosures and UNVERIFIED

* Non-blind: IT10 and IT11 results were read before the questions; the counts and correlations are my own scripts, not the authors' code; the replicate-overlap figure mixes media and clones.
* Early exploration ran inline Python (xlsx parsed as XML, no openpyxl) before the two scripts were written; the scripts were then run and reproduced the numbers (rep. overlap 0.122 / 0.223; summary). The first version of the script truncated numbers in `selected_genes_qgi_fdr.tsv` (string slicing); fixed and rerun; three rows (ATF4, TP53, EIF2AK4) were appended from the inline run.
* Large downloads were kept outside the repo (scratchpad `it12b/`; Zenodo zip 687 MB, md5 verified equal to the record).
* I did not re-read LEGEND_CORE 21c to 21e bodies, `roadmap_current.md`, or the IT9 v3 README (time); no stop condition or decision-authority question arose.
* UNVERIFIED: absence of WWOX protein in clone c2.2; exon/position of the two indels; HAP1 ploidy of the clone (two alleles suggest at least diploid, an inference); whether EIF5AL1 guides multi-map to EIF5A (the paralog EIF5AL1 is depleted -0.96 in WT screens, EIF5A -1.81, which suggests it); Mendeley Data licence; the PMC13281610 supplementary figures; all lever identities, potencies and exposure (ChEMBL HTTP 500); DepMap WWOX data (access control); PDH deficiency neurological statement (textbook, not sourced); the 55-bp frameshift reading (arithmetic only).
