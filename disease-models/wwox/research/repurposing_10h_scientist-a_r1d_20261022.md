# R1D: first-reading scan flags resolved, and five reports that pair a protein readout with a function readout

> **Actor** `scientist-a` · **Task** `REPURP-10H-R1D-A-20261022` · 2026-10-22 · Non-canonical research record; it touches none of the four scientific current files, `disease_model.md`, the ledger or the registries (the integrator is mid-batch), `cards/`, `cards_early/` or `repurposing_bridge.py`. **Not medical advice.** Class level; **no dose, route, schedule or suitability is carried** (compound levels of the papers are deliberately not reproduced). **Every paper below is NOT WWOX EVIDENCE.** No receipt was recorded; five receipts are STAGED under `receipt_staging/scientist-a/`. Context policy `QUESTION_DRIVEN` throughout.

## 1 · The four first-reading scan flags (item 1)

The four propositions flagged by `locator_audit.py --strength-scan` (42587736 entry 15 'significantly'; 42650175 entries 3, 6 and 9 'rescue') were each repaired from the artefact, by widening the quote to the authors' own sentence (42587736 #15, which now carries 'these trends were not statistically significant, in part due to the high variance and limited scope of this experiment') or by narrowing the proposition to its quote (42650175 #3, #6; #9 loses the reader's word 'rescue', stated as 'an effect on the mutant protein'). Each revision carries `contradicts_locator` (audit: `CORRECTED`, auditors 0): the blind audit of these four repairs is **OWED**. The scan now reads 0 of 25 and 0 of 18 flagged; the working-tree contradiction audit reports every revision declared.

## 2 · Readings made (item 2): 5 of at most 6

Search: Europe PMC REST, 2024 to 2026, open-access body, chaperone or proteostasis term and missense/variant term and a function term (patch clamp, enzyme or transport activity, functional rescue), `NOT WWOX`; two queries, 37 and 8 hits, about 70 distinct titles screened, ten abstracts read; registry first (`registry_records.py get --pmid ... --hops 0` returned NO RECORD MATCHED for every candidate and no receipt existed; a statement about that query only). Selected on the three tests (substantive abstract, lawful body, a question it could change); one candidate (a preliminary computational-plus-in-vitro GALT paper, 39940658) was not read.

| PMID | Paper (class) | Protein readout and function readout it pairs | Depth | Staged receipt | Manifest |
|---|---|---|---|---|---|
| 40421674 | OTC pharmacological chaperones, hiPSC hepatocytes and patient hepatocytes | steady-state OTC protein, OTC activity, ureagenesis | complete | `FTR-20261022-40421674-01` | PASS, 23 entries |
| 39013852 | HTRA1 R274Q: protein corrector, ligands, peptide; knock-in mouse | oligomer state, protease activity, brain-vessel proteome (HtrA1 and substrates) | **partial**, supplement owed | `FTR-20261022-39013852-01` | PASS, 26 entries |
| 40449593 | GALC missense panel in a knockout cell line (no chaperone applied) | mature, secreted and precursor protein; activity; psychosine; age of onset | complete | `FTR-20261022-40449593-01` | PASS, 24 entries |
| 42161426 | GLA p.Met76Lys and an active-site chaperone, AC16 cardiomyocytes | protein by western blot, localisation, activity before and after the chaperone | complete | `FTR-20261022-42161426-01` | PASS, 12 entries |
| 41274966 | Pah missense mouse and an HDAC6 inhibitor | liver PAH protein and acetylated HSP90, plasma phenylalanine, coat colour | complete | `FTR-20261022-41274966-01` | PASS, 16 entries |

All five manifests: `deepdive_manifest.py --verify-artifacts --require-current-schema` PASS from the shared checkout; numeral-in-quote and quantifier/negation/strength-word checks run on every body locator; `--strength-scan` 0 flagged on each (the single word the home-made check lists is the label NOT in "NOT WWOX EVIDENCE"); receipts checked with `staged_receipt_check.py --check-doi` and `record --dry-run`, none recorded. **Contradiction of an earlier reading: none.** Text-versus-panel relations inside the new papers (`panel_qualifies_text`, `text_contradicted_by_panel`) are OWED a blind audit by someone else.

## 3 · What the five add to the open question: a function readout beside the protein fraction

The question left open by the 2026-10-22 single-measurement note is the *functional* readout. These are the findings that bear on how it must be paired, each tied to a locator (figure values are readings of printed panels):

1. **Protein present is not function present (GLA).** The mutant enzyme is made at about 1.8 times the empty-vector level and sits in the cytoplasm like wild type (Figure 4C, 4D-E), yet its activity (about 0.65) is not different from the empty-vector background (about 0.35; ns) while wild type is about 1.15 (Figure 4F). The same paper's chaperone arm has no empty-vector arm, so a gain of about 0.10 cannot be separated from an effect on the host cells' own enzyme. **Lesson: an activity readout needs a null-construct arm and a wild-type arm in the same experiment.**
2. **The same compounds raise the wild type (R44Q in the earlier lot; OTC here).** In the OTC paper the compounds raise wild-type protein and activity in control cells and do nothing in a missense patient line with no detectable protein (Supplementary Figure S1B); a gain in patient hepatocytes is about 11 percent in activity while ureagenesis rises about 2.3-fold, which the activity does not explain. **Lesson: treat wild type alongside, and measure the function that the protein serves, not only a downstream pathway output.**
3. **Quantity predicts function over a range and not within the low range (GALC).** Mature protein and activity correlate at r = 0.93 over 37 variants, but the enlarged panel below 8 percent activity shows no ordering, one active-site variant sits off the line, and the intracellular precursor does not locate a variant on the activity axis (r = -0.02). The activity-versus-onset correlations (r = 0.94, n = 12; r = 0.98, n = 7) are carried by one or two points; ten of twelve variants sit between 0 and 1.6 percent activity with onset from 4.5 to 22 months. **Lesson: a coefficient over a wide range is not a resolution within the range where a recovered protein would sit.**
4. **Oligomer state and activity separate (HTRA1).** A trimeric non-interface mutant is reduced in activity; interface mutants are monomers with residual activity; correctors give partial restoration (about 40 to 60 percent of untreated wild type for the best-treated mutants), and the in-vivo 'rescue' of the substrate signature leaves the corrected genotype about five- to six-fold above wild type for two substrates; the headline Pan-HtrA1 rise includes the corrector protein itself. **Lesson: report the residual gap to wild type next to the gain.**
5. **A function readout in an animal still needs n and units (PKU mouse).** Plasma phenylalanine falls (to about 44 percent below sham at the last time point, still about three times wild type), liver PAH protein rises, and the study's Table 1 lists two sham animals against 'three per group'; several printed means do not equal the mean of the printed individual values (reader's recomputation, INFERENZA); the supplement's three blot sets are repeat runs of the same eight samples. **Lesson: the unit of replication must be named per panel.**

**Reading for WWOX (INFERENZA, reader's).** WWOX is a cytosolic SDR-family protein with no per-molecule function assay in the repository, so none of these designs transfers as a measurement; what transfers is the structure of a valid pairing: fractions of the same cell lysate (soluble, pellet, total), an empty-construct arm, a wild-type arm treated identically, a function readout on the recovered protein measured in the same samples, the residual gap to wild type reported beside the gain, and the replication unit stated. **None of the five papers supplies a WWOX function assay, and none should be read as doing so.** This note does not say which function assay to build.

## DEFAULTS_TAKEN

| Condition | Default | Why safe |
|---|---|---|
| The strength-scan flags concerned first-reading entries | repaired in place with `contradicts_locator` (CORRECTED, auditors 0) | the revision is visible and the audit is declared owed, not claimed |
| 39013852 supplement is large (17 MB figures PDF, ten PDFs, four workbooks) | not opened; receipt `partial_fulltext_read`, owed section named | an unopened supplement is never recorded as read |
| Compound levels and schedules are in several papers | not carried in any proposition | no dose or schedule |
| Table 1 of 41274966 is a text table whose printed values disagree with its means | reader's recomputation declared INFERENZA, page render attached | no data file exists to confirm |
| The tasks were told to read at most 6; five met the three tests | the sixth (a preliminary GALT paper) not read | proportion |
| 40421674 Table S1 workbook | the first rows and header were read as a table; the compound-by-concentration replicates were not re-tabulated | declared here rather than overstated |

## STOP_LOG

Empty. No reserved act was needed; no ledger or registry was touched; nothing pushed; no receipt recorded.

## OWED

* Blind audit by someone else of: the four repairs of section 1; every relation declared in the five new manifests (notably 40449593 Figure 6 leverage statements, 41274966 Table 1 recomputation and two-sham finding, 42161426 Figure 4F background statement, 39013852 Figure 4D readings).
* The supplement of 39013852.
* The WWOX function assay itself (not designed here).
