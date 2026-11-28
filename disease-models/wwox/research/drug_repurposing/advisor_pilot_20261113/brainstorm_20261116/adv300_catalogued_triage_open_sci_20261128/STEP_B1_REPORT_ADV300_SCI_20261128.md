# ADV-300 step B batch 1 (records 1, 2) full-text reader

legend-delegate, claude-sonnet-5-5, effort high on 17 of 17 model turns read back. Model output, hypothesis level, not medical advice; saved verbatim.

---

FULL-TEXT CHECK, two records. Both texts were read in full. Counted data: record 1 has 0; record 2 has 1, which is borderline. No figure images or supplements were available for either record, and nothing was downloaded. All held-file paths below are under /home/desktop/legend-development/.claude/worktrees/sci_aw_20261128/disease-models/wwox/. Hypothesis-level only, not medical advice.

## Record 1: PMID 43036373 (/home/desktop/.claude/jobs/919d2041/tmp/adv300/ft/43036373_PMC13769701.txt)

**(1) What it is.** This is a commentary ("A Window Into WOREE: WWOX, Organoids, and Epilepsy"; the back matter gives the ORCID of Tracy A. Bedrosian). It comments on Steinberg et al., Brain 2026, PMID 42397075, and reprints that paper's abstract. The study it describes used human iPSC-derived cerebral/neural organoids: wild type, CRISPR WWOX knockout, and WOREE and SCAR12 patient-derived lines, with immunofluorescence, single-cell RNA-seq, MYC inhibition and neuron-directed AAV restoration. The commentary gives no n, replicate unit, dose or statistic; the one timing given is week 7 for the SOX2/neuron composition. It has no tables, figures or data of its own, and presents nothing as unpublished. The author declares no funding or conflicts.

**(2) Counted data: none.** Every result in it is attributed to Steinberg et al., so it fails condition 1. Its own contributions are appraisal and open questions (a possible developmental window for gene replacement; the relative contributions of neurogenesis, maturation and intrinsic neuronal dysfunction to seizures; the role of residual function). These are not results.

**(3) Uncounted.** No datum meets condition 1. The following are worth knowing but fall outside the rule.
- One held sentence about this record itself is now out of date. research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv:68 (TS-01) says: "one commentary on WOREE, WWOX and organoids (PMID 43036373) returned a restricted stub and was not read." It has now been read. I saw nothing in it that reports a new measurement or would meet a reopen condition by being new data. I did not check it against the 21 conditions one by one.
- The commentary's wording is stronger or flatter than held readings in places and should not be adopted as evidence:
  - "MYC inhibition reduced the SOX2-positive progenitor population and restored overall neuronal production." The held card research/drug_repurposing/cards/D01_a51.card.json:138 (field measured_result_note) says "MEASURED NO RECOVERY" for CTIP2/SATB2 (with an addendum that SATB2 recovery is neither shown nor excluded and that NEUN does rise).
  - "hyperexcitability phenotype was substantially normalized in both WOREE and SCAR12 models." The held claim registry (registries/claim_registry_current.md:69) restricts this to event rate, with amplitude and active-region share of the treated groups at or above wild type.

**(4) Searches.** Case-insensitive, over claim_registry_current.md, working_model_current.md, disease_model.md, discovery_ledger_current.md, therapeutic_hypotheses_ledger_current.md, research_portfolio.tsv, open_questions_map.tsv, the three card folders (JSON) and comparators_it39 output/*.tsv.
- Keywords: 42397075, 43036373, awag239, PMC13769701, Steinberg, organoid, "radial gli", MYC, hyperexcitab, SCAR12, Bedrosian, SATB2, Wnt, "developmental window", neuron-directed/specific restoration, Wnt near MYC, A51 near restore/SOX2/NeuN/SATB2, "MYC inhibit".
- I read context only around the hits that bear on the record. I did not read every organoid, MYC or Wnt hit, because no datum could pass condition 1.
- One regex (WOREE near SCAR12) exceeded ugrep's complexity limit. I reran it in Python over the registries and ledgers, printing only claim-registry and disease_model hits.

## Record 2: PMID 20535528 (/home/desktop/.claude/jobs/919d2041/tmp/adv300/ft/20535528_PMC2996532.txt)

**(1) What it measured.** A primary study of human glioblastoma tissue: 67 specimens, one per patient, bulk frozen tumour, with no non-tumour brain control.
- **Expression:** real-time RT-PCR for WWOX (semi-nested; the text states 77 cycles), Bax, Bcl2, EGFR, Ki67 and ErbB4 JM-a and JM-b, in duplicate, against three reference genes, with Universal Human Reference RNA as calibrator.
- **Allele status:** high-resolution-melting "hemizygosity" at D16S518 (intron 1), D16S3096 and D16S504 (intron 8), compared with database population homozygosity.
- **Methylation:** MethylScreen of two WWOX promoter fragments in 61 samples.
- **Results:** distal fragment methylated in 11/61 (18%) and TATA-proximal fragment in 9/61 (15%). Mean WWOX expression was 11.71 methylated vs 21.93 unmethylated (P = 0.15; medians 6.23 vs 12.04, P = 0.23). Hemizygosity was 18%, 38.5% and 54.5%, against population homozygosity of 17%, 26% and 36.7%. LOH showed no association with expression.
- **Spearman correlations with WWOX mRNA:** ERBB4 JM-a 0.7102, Bcl2 0.7092, Ki67 0.5440 (all P < 0.0001). EGFR 0.2413 (P 0.0611), Bax 0.2301 (0.0745), JM-b 0.2108 (0.1029) and Bcl2/Bax 0.1995 (0.1442) were not significant.
- No correlation with age, sex or survival time.

**(2) Counted data (1, borderline).**

**Datum.** In human glioblastoma tissue, WWOX mRNA co-varies positively with the ERBB4 JM-a transcript (Rs 0.7102, P < 0.0001) and not with JM-b (Rs 0.2108, P 0.1029). Locator: Results, the paragraph "In an experiment on 67 patients with GBM...", and Table 4.

**Held sentence,** research/drug_repurposing/research_portfolio.tsv:39 (RP-038): "The RNA side now stands at: no Erbb4 transcript deficit in a P47T knock-in bulk comparison (point mutant, not a null) and in a Wwox-KO snRNA pseudobulk; the human hNPC deposit could not carry a comparison (ADV-185); protein unmeasured". A later addendum in the same row (ADV-239) rewords the P47T reading to "no clear Erbb4 change".

**Changed sentence:** "The RNA side now stands at: no clear Erbb4 transcript change with Wwox perturbation in mouse (P47T knock-in bulk; Wwox-KO snRNA pseudobulk); in human glioblastoma specimens, WWOX mRNA co-varies positively with the ERBB4 JM-a transcript (Rs 0.71) but not JM-b (Rs 0.21, not significant), a between-tumour bulk correlation with no WWOX perturbation, no protein and no cell-type resolution; the human hNPC deposit could not carry a comparison (ADV-185); protein unmeasured."

**What it adds:** a human tissue, an isoform (JM-a, the one named in the row's minimal measurement), a positive sign and a correlational evidence level.

**What it does not change:**
- "nothing measures ErbB4 in WWOX-deficient neural cells" (same row) stays true, since GBM tumours are not a defined WWOX-deficient neural system.
- "a stabilisation arm (less ErbB4 without WWOX) is untested in neural cells" (open_questions_map.tsv:214, IT59-Q01) stays true.
- IT59-Q01 stays OPEN.

**Case against counting:** a reader who takes the RNA-side sentence to cover only WWOX-perturbation comparisons would score this 0.

**(3) Uncounted (own results failing condition 2 or 3).**
- **Ki67 and Bcl2 positive correlations.** None of these held sentences would read differently, because each concerns an intervention, a protein or a stress response, not an mRNA correlation in unperturbed tumours:
  - claim_registry_current.md:270 and working_model_current.md:152, "WWOX overexpression increased proliferation in 1 of 4 glioblastoma lines"
  - working_model_current.md:255, "a tumour suppressor whose overexpression is pro-apoptotic in cancer cell lines"
  - discovery_ledger_current.md:282 (DL-MECH-016), "WWOX(induction) —promotes→ lysosomal_degradation(Bcl-XL/Mcl-1)"
  - discovery_ledger_current.md:1428 (DL-MECH-054), "abbondanza/espressione WWOX —non determina necessariamente→ localizzazione + partner occupancy + output funzionale"; this would only gain a citation
  - discovery_ledger_current.md:3668 (DL-THER-115), loss lowers and restoration raises stress-induced apoptosis; no stress here
- **No correlation of WWOX mRNA with survival, age or sex.** The nearest held sentence (discovery_ledger_current.md:3873) concerns the WWOX/HIF1A ratio, and HIF1A was not measured here.
- **Promoter methylation frequencies, non-significant expression trend, intron-8 hemizygosity, subgroup medians (Table 3).** I found no held sentence on WWOX promoter methylation or LOH in glioma. The LOH hits in registries/working_model_current.md:41 concern germline uniparental isodisomy.
- **Reliability problems to carry if the datum is ever used:**
  - The printed P values fit n = 61, not the stated 67. My recomputation: EGFR, Bax and JM-b fit n = 61 exactly, while Bcl2/Bax fits n = 55. This is an inference; the paper does not state n for Table 4. No exact P is printed for JM-a.
  - Patient counts do not add up: 20 female + 35 male + 2 unspecified = 57, not 67.
  - The Conclusion says "LOH correlates with reduction of WWOX expression" and the Discussion implies an effect, but Results say there is no correlation (P 0.58 to 0.71), and Table 3 differences are not significant.
  - "Deletions" and "LOH" are inferred against database homozygosity with no matched normal DNA.
  - No non-tumour tissue was measured, so reduced expression in GBM is not shown.
  - No adjustment for tumour cell composition or multiple testing.
- The ErbB4 mechanism text (WW1 binding both JM-a PPxY motifs, membrane stabilisation, blocking ICD nuclear entry) and the breast-cancer parallels are citations of others.

**(4) Searches.** Same file set as record 1.
- Keywords: glioblastoma, glioma, GBM, Ki-67, Bcl-2, Bax, ErbB4, JM-a, methylat, heterozygosity/LOH/hemizyg, FRA16D, 20535528, PMC2996532, Kosla/Kosła, tumour/tumor suppressor, astrocytoma, tumour/cancer/carcinoma/neoplas/oncogen near WWOX or expression words, proliferat and apopto near WWOX, WWOX near promoter / hypermethyl, ERBB4 near mRNA/transcript/isoform.
- Context was read around the hits in registries, ledgers, cards, comparators, portfolio rows (including RP-038, line 39) and map rows (lines 68 and 214).
- No hit for 20535528 or PMC2996532, and no comparator row bears on this record.

## (5) Not read, and failures
- Not available: figure images and supplements for both records. Record 2's reference list was left out, so I cannot identify its cited sources. Its text refers to no figures that I saw; its four tables are present as text.
- Failure: only the ugrep regex noted under record 1.
- One oversized output of my own search was saved by the harness under /home/desktop/.claude/projects/ and I read it back there. I opened no memory file, note folder or other repository file, nor the other texts in the ft folder. Lines mentioning the excluded PMID were skipped.
- No files were written, no scratch directory was created, and no network was used.

