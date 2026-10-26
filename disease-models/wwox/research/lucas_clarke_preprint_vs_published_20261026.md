# Lucas-Clarke et al.: preprint (PPR1015434, PAPER 158) against the published article (PMID 42909904, PAPER 567)

> **Drosophila Alzheimer's-disease model; NOT WWOX-DEE evidence.** Observations are listed **per experimental contrast** and never as a generic "Wwox suppression raises Atf4, Ldh, lactate". Contrast codes used below:
> **KD0** = neuronal Wwox RNAi, no amyloid (LacZ control); **KD+A** = neuronal Wwox RNAi with neuronal Abeta42 (compared with control RNAi + Abeta42); **A** = Abeta42 alone (against LacZ, control RNAi); **OE0** = neuronal Wwox CRISPRa, no amyloid; **OE+A** = CRISPRa with Abeta42 (against control gRNA + Abeta42).
> Preprint surface: `files/fulltext/PPR1015434_LucasClarke2025_EPMC.xml` (text, section named) and its Supplemental Tables 1-7 workbook. Published surface: PDF `PMID42909904_LucasClarke2026_BrainComms_fcag385.pdf` and manifest `deepdive_manifests/PMID42909904.json` (entry numbers, "E#"). Status: **identical** (same value and wording), **changed** (value, statistic or interpretation differs), **absent** (not in the final version), **new** (only in the final version). Read 2026-10-26, `scientist-a`. Pyruvate, PDH and PDK are measured in neither version and are left out of this table.

## 0 · The Ldh log2 numbers: which contrast is which

| Number | Where | Contrast | Verdict |
|---|---|---|---|
| 1.19 | text of **both** versions ("1.19 log2 fold-change upregulation of Ldh after overexpression of Abeta42", Results lactate section; preprint adds "2.28-fold") | **A** (Abeta42 vs LacZ, control RNAi) | the table row for the SAME contrast is **1.1097** (RNAi Control LacZ vs Abeta42; adjusted P 5.3e-08), in the **preprint's own Table S3 as well as the published Supp Table 3**: a small text-versus-table discordance that predates publication and was not repaired |
| 1.1097 | Supp Table 3 (published) = Table S3 (preprint), identical row | **A** | matches the dossier link table, which ties it to Abeta42 alone |
| 1.29 | published text ("1.29 log2 fold-change increase in Ldh transcripts compared with Abeta42 overexpression alone", Fig 4E) | **KD+A vs A** (added effect of knockdown on the amyloid background) | **agrees** with the table row 1.2903 (adjusted P 1.2e-11), identical in both workbooks |
| 1.33 | **preprint** text ("1.33 log2 (2.51-fold) increase in Ldh transcripts compared to Abeta42 overexpression alone") | **KD+A vs A** | **changed** in the published text to 1.29; the preprint number 1.33 disagrees with its own Table S3 (1.2903), the published text fixed it |
| 2.85 | both texts, Supp Table 5 | **A** in the overexpression experiment (separate cohort, Abeta42 vs LacZ control gRNA) | identical |

So 1.19 (text) against 1.29 (table) is **not** a discordance: they are different contrasts. The only text-versus-table discordance is 1.19 vs 1.1097 (same contrast **A**), and, between versions, 1.33 vs 1.29 (same contrast KD+A vs A).
**Where a conflation exists (records to correct, not edited here):**
1. `PAPER 567` Note in `paper_registry_current.md` (about line 18066, written by `BATCH_20261019_018`): "about +1.2 to +1.3 log2 depending on the contrast: the text gives 1.19 for Abeta42 against control, the supplementary table as read 1.29 for the interaction". It sets a text figure of one contrast against a table figure of another, and omits that the table row for the 1.19 contrast reads 1.1097 and that the published text itself gives 1.29 for the interaction.
2. Any reading of "text 1.19, supplementary table 1.29" in `BATCH_20261019_018` or its candidate narrative (not located in the registries I searched beyond item 1; the batch record should be checked).
3. Not conflating, no correction needed: manifest entries E29, E30, E31 (one contrast each) and dossier `fulltext_dossiers/PMID42909904.md` section 2 row 4 and section 6 ("Ldh log2 1.19 vs table 1.1097" is the same contrast **A**). The dossier section 7 should additionally record that the preprint text gave 1.33 for KD+A vs A.

## 1 · Table by experimental contrast

| # | Contrast | Claim | Preprint (locator) | Published (locator) | Status |
|---|---|---|---|---|---|
| 1 | KD0 | neuronal knockdown shortens lifespan, TRiP line: 57 vs 42 d | Results, first section | E8 (N 91-105, chi2 30.76) | identical |
| 2 | KD0 | second independent RNAi line (KK) also shortens it (40 d); "two independent UAS-RNAi constructs" | Results, first section | not in any assay row; line listed only in Supp Table 1A | **absent** |
| 3 | KD0 | glial knockdown 70 vs 74 d; climbing unaffected (neuronal and glial) | Results, first section | E9, E10 | identical (published adds F and t values) |
| 4 | KD0 | sleep up, circadian rhythm unchanged, neuronal and glial (males) | Results, sleep section | E11 and Fig 2 | identical; **new**: statistics, `tim-GAL4` period lengthened (Supp Fig 2T), wing ROS up (E15, Supp Fig 2U, wing not brain) |
| 5 | KD+A | lifespan 41 vs 26 d, Cox interaction | Results, Wwox knockdown modifies Abeta42 phenotypes | E17 (Z 4.815); preprint also gave KK 24 d | TRiP identical; KK **absent** |
| 6 | KD+A | climbing lowered | both RNAi lines, TRiP padj 0.0011, KK 0.0004, interaction ns | E19 (TRiP only, F 12.51, P 0.0019) | **changed** (one line) |
| 7 | KD+A | total and soluble Abeta42 up; insoluble | insoluble "only trending towards an increase" (P 0.0602); total P 0.033, soluble P 0.0024 | E24 (insoluble ns, padj 0.2412; total padj 0.0127, soluble padj 0.011) | **changed** (statistics re-run, wording from trend to ns) |
| 8 | KD+A | visible deposits unchanged | number P 0.1135, size P 0.6771 | E22 (number P 0.2020, size P 0.8218) | **changed** values, same conclusion |
| 9 | KD0, A, KD+A | transcript counts (54/44; 23/51; 58/54) | Results, pyruvate metabolism section | E26-E27 | identical |
| 10 | A | Ldh up, log2 1.19 (text); table 1.1097 | text 1.19; Table S3 1.1097 | E31, E30 | identical in both versions, **discordance text vs table in both** (section 0) |
| 11 | KD+A vs A | Ldh up, text 1.33 (preprint) vs 1.29 (published); table 1.2903 | text 1.33 | E29 (table 1.2903), text 1.29 | **changed** text, table identical |
| 12 | KD0 | Ldh not changed by knockdown without amyloid | not in text (Table S3 has no Ldh row for KD0) | no Ldh row for KD0 in Supp Table 3 | identical (table only) |
| 13 | KD0 / A / KD+A | lactate: KD main F 7.524 (padj 0.0636), A main F 27.846 (padj 0.0050), interaction F 23.606 (padj 0.0174, +1.30 log2); 2-hydroxyglutarate | Results, lactate section | E37-E41 (2-hydroxyglutarate in the same entries) | identical values |
| 14 | KD0 | lactate with knockdown WITHOUT amyloid is -0.43 log2 (Supp Table 4 last column); Supp Fig 5A shows it | Table S4 carries the column; text silent | Supp Table 4, Supp Fig 5A | **new** as a stated contrast (column present in both tables, never in text) |
| 15 | KD+A | ATP unchanged | one P (0.5720) | E46 (F values for all three effects, n 4) | identical data, **new** detail |
| 16 | KD+A | Ldh RNAi added to Wwox RNAi rescues climbing 14/21/28 d (padj 0.0081, <0.0001, <0.0001); 3 genotypes, no Ldh-alone arm; lactate not measured in the double line | Results, lactate section | E51 | identical; limitations same in both |
| 17 | KD+A | Atf4 immunofluorescence up (P 0.0022, n 6) | Results | E57 | identical |
| 18 | KD0 | Atf4 unchanged without amyloid | not in text | E58, Supp Fig 5E | **new** |
| 19 | KD+A | sima:GFP unchanged (P 0.5185); one genotype pair, day 14 | Results | E66 (adds t 0.6623, day 14, n 7-9) | identical |
| 20 | KD+A | Xbp1 splicing unchanged | P 0.7574 | E61 (t 1.365, P 0.1954) | **changed** value, same conclusion |
| 21 | KD+A | **Atf4 -> Ldh is the authors' inference**: Atf4 is never knocked down or activated; PERK and eIF2alpha phosphorylation are not measured; "this could be the mechanism" | Results end of lactate section | E63 and E62 | identical wording in both; Discussion "place Wwox upstream of Atf4, Ldh and Lactate" (E64) is in the published Discussion |
| 22 | KD+A | "Atf4, rather than the HIF1alpha orthologue sima, is primarily responsible" | Discussion | E70 | identical |
| 23 | OE0 | no effect on lifespan (60 vs 58 d) or climbing | Results, upregulation section | E71 | identical |
| 24 | OE+A | lifespan 47.5 vs 29 d; climbing days 14, 21; plaque size and number; MSD total, soluble, insoluble | Results | E72, E75, Fig 6 | identical; a glial-OE null reads padj 0.0800 (preprint) and 0.7997 (published), a **changed** value |
| 25 | OE+A | human WWOX cDNA rescues lifespan (41 vs 51 d); climbing | climbing P 0.0371 | E73 and Supp Fig 6C-D; Ser14/Tyr33 variants rescue similarly, Drosophila cDNA better | lifespan identical; variants and dWwox comparison **new** |
| 26 | OE+A | transcripts 305 down 59 up; r -0.8341; Ldh not reversed | Results | E78-E82 (E82 = Ldh not restored) | identical |
| 27 | A (OE cohort) | Abeta42 alone: 2-hydroxyglutarate and citrate up | Results | E45 | identical |
| 28 | OE0 / OE+A | L-methionine: interaction padj 0.0073 and 0.0133; **interpretation**: preprint "upregulation of Wwox in the presence of Abeta42 reduces L-methionine levels"; published "decreased after Wwox overexpression in the control background but unaltered by overexpression in the presence of Abeta42" (about 2.85e6 -> 0.9e6 in LacZ; about 1.5e6 vs 1.46e6 with Abeta42, Supp Fig 8) | Results, last section | E84, Supp Fig 8 | numbers identical, **interpretation changed** |
| 29 | OE+A | lactate: preprint "occurred without restoring lactate levels"; published Introduction "did not alter lactate levels", Discussion "without a reduction in Ldh or 2-hydroxyglutarate"; lactate is in no displayed OE panel and not in the significant lists, and Abeta42 alone did not raise it in that cohort | Results last section | E89, E82 | **changed** wording |
| 30 | OE+A | glycolytic-enzyme transcripts (Gapdh1, Eno, Pgk, Pgi, Tpi) lower, undiscussed | Table S5 rows present | E99-E103 | identical in the table, discussed in neither |
| 31 | Fig 1A | Wwox expression: preprint "high levels ... in both neuronal and glial cell-types"; published "detectable"; panel shows glia highest | Results, first section | E1-E2 | **changed** wording |
| 32 | title, abstract | "protects against" -> "controls"; "downstream of an increase in Atf4" -> "driven by activation of Atf4"; "key mediator" of pyruvate metabolism added | title, abstract | title, abstract | **changed** |

## 2 · What this changes for the records (not edited here)

- `PAPER 158` / `LIT-0447` (preprint): the "two independent RNAi" statement and "OE lowers L-methionine" stay as true descriptions of the **preprint**; they must not be carried to `PAPER 567` (rows 2, 6, 28).
- `PAPER 567` Note: the Ldh sentence of section 0, item 1.
- Any statement of the chain as "Wwox suppression -> Atf4/Ldh/lactate" without the contrast code: lactate and Atf4 rise only in **KD+A**, not in **KD0** (rows 14, 18); Atf4 -> Ldh is an inference (row 21).
