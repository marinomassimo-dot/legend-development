# IT30: the NCC screening table, endpoint qualified (rows S1-32 and S1-33 and the 20 compounds of the IT29 comparison)

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class. Zero spend; official supplements fetched from the publisher's static host and Europe PMC (public, no contact data sent). 2026-11-06.

## Decision (answer first)
* **KEEP** the table as data, with the endpoint it actually carries: the **primary Alamar Blue (AB) viability/metabolic screen of the cytokine-protection paper, values as percent of quetiapine** (paper 2, Table 1 column "AB screening (% quetiapine)"). **DISCARD** its use in IT29 as an oligodendrocyte-differentiation sign: neither as independent counter-evidence (rows S1-32, S1-33, five "contradictions" in the P12 scout) nor as independent confirmation (the five "agreements").
* The assignment is **strong but its cause is unknown**: the two papers' supplements carry the same values, and paper 1's text describes a different normalisation (T3). Do not attribute it to the publisher, the authors or LEGEND. Where paper 1's own Table S2 should be, nobody has been able to say from the files alone.
* **The two rows are withdrawn** (`../withdrawn_rows_it30.tsv`), the signed table now has 31 rows, and **NR3C1 and CYP51A1 were assessed separately on the evidence that remains** (section 4). No abstention is kept to preserve the earlier counts: the signed count moves from 97 to 216 and the outputs below were regenerated.

## 1. Material actually used
| Item | DOI | File | sha256 |
|---|---|---|---|
| Paper 1, differentiation screen (PMID 27592856, PMC5011342) | 10.1186/s13104-016-2220-2 | Additional file 2 (xlsx, 68,392 bytes; `% DMSO` columns) | `7c138174a261fa8680cb32b8b31c80cbccb093546947fd92a1eed9fde8cb9d21` |
| Paper 1 | same | Additional file 3 (xlsx, 51,934 bytes; `% Quet` columns). **This is the file IT29 called "differentiation as percent of quetiapine".** | `aea9d135c858ada20376ce5bd16cfed824b6352a1af47786ee50226125e9b046` |
| Paper 2, cytokine-protection screen (PMID 27629829, PMC5024459) | 10.1186/s13104-016-2219-8 | Additional file 3 (xlsx, 51,937 bytes; `% Quet` columns) | `55942e6fbe6279180dd4312de554872b4400ad48b244296881ae402f3ffed9f0` |
| Paper 2 | same | Additional file 2 (pdf, figure S1) | `40dd6972c76a9b7dfe3e4725cb6670b26e8654006f9c7547328099253f958a22` |

Fetched from `static-content.springer.com/esm/art:<doi>/MediaObjects/...` and the Europe PMC `supplementaryFiles` zip; the file IT29 used equals paper 1's Additional file 3 byte for byte (same hash). Both papers: BMC Research Notes, published 2016-09-05, same laboratory group.

## 2. Endpoint, control and meaning of the columns
| | Paper 1 text | Paper 2 text | The file (both papers' Additional file 3) |
|---|---|---|---|
| What it measures | MBP-positive oligodendrocyte differentiation; hits are compounds reaching at least 50 percent of the T3-promoted level; the word quetiapine does not occur in the text | primary AB (Alamar Blue) screen of cell viability/metabolism under inflammatory cytokines; normalised to quetiapine; differentiation (MBP) examined later in selected compounds | columns `10/2/0.4/0.08 uM (% Quet)` |
| Control | T3 | quetiapine | quetiapine = 100 (the assay normaliser) |
| Table S2 described as | "all of the acute OL differentiation assay NCC library screening data" | "the data for all compounds tested in the cytokine protection screen" | 727 compounds, 728 rows with header |

Reconciliation evidence: (a) the two files' **cell values are identical** in all 728 rows and 8 columns; only the zip packaging differs (sizes 51,934 and 51,937 bytes, different hashes); (b) of 15 compounds read from paper 2's Table 1 "AB screening (% quetiapine)", **12 appear in the file with the same rounded value** and the other 3 differ by a rounding step or a spelling variant (toremifene 73 v 74.87, fluphenazine 91 v 92.63, benztropine as "Benzatropine" 123 v 122.96); (c) **T3 (triiodothyronine) is negative in the file** (-37.8 and -36.3 at the first two doses) and thyroxine -185.6: in a differentiation screen normalised to T3 the control would sit at 100, here it is negative, which fits a viability/metabolic readout and not the stated T3-normalised MBP table. Not read: paper 1's methods beyond the passages about the files, and the figures. Cause of the duplication: unknown.

## 3. Consequences, only on outputs that consume these rows
Counts from running the same converter and search twice (rows S1-32 and S1-33 present, as committed in IT29; absent, as now), same catalogue cache, `NEED-MYELINATION`. The 'without' column is the current state of the repository.
| Output | With the two rows (as committed) | Without them | Real change |
|---|---|---|---|
| Rows in the signed table | 33 | 31 | 2 |
| Coupling rows from the converter | NR3C1 `unresolved`, CYP51A1 `unresolved` | NR3C1 `same`, CYP51A1 `opposite` (each one source, marker-level) | 2 |
| Search associations with a signed label (consistent + opposed) | 97 (29 + 68) | 216 (137 + 79) | 119 |
| Associations whose label differs | | | 114 rows over 111 families (104 `direction_unresolved` to `consistent`, 10 to `opposed`); 106 of the consistent rows are NR3C1 agonists, 2 CYP51A1 |
| IT29 P6 comparison, 20 compounds | Arm C: clobetasol abstained | clobetasol right | 1 compound; it is the circular case (the study that signs the target also tests clobetasol) |
| IT29 P12 scout table | 11 directions "recovered", 5 "contradictions", 6 "agreements" | 0 usable as differentiation direction | 11 (all reclassified, `ncc_20_compounds_it30.tsv`) |
| Dashboard, rankings, hypotheses, the four current files | not consumed | not consumed | none (checked: the view and the rankings do not read the signed table) |

## 4. NR3C1 and CYP51A1, assessed separately on the residual evidence
| | CYP51A1 (inhibition of the enzyme, lanosterol demethylase) | NR3C1 (activation of the glucocorticoid receptor) |
|---|---|---|
| Residual rows | R22, R24 (miconazole in vivo, lesion and neonatal), R27 (voriconazole null: the effect is not generic P450 inhibition), R28 (human cells), R30 (ketoconazole and azoles; **CYP51 siRNA** with about 80 percent knockdown giving more MBP-positive cells; a pathway inhibitor abrogates the effect), R31, R37 | R23, R25 (clobetasol in vivo), R26 (**RU486 blocks the clobetasol effect** and GR phosphorylation), R28 (human cells) |
| Independent origins | two studies (25896324, 30046109) | one study (25896324) |
| Target control | genetic (siRNA) and pharmacological, plus a specificity control | one pharmacological antagonist (non-selective: it also acts on the progesterone receptor) |
| Endpoint | MBP-positive oligodendrocytes, CC1 cells, remyelinated axons; marker level, non-WWOX | same |
| Decision | **sign restored: inhibition of the enzyme is concordant with differentiation** (the converter's `opposite`), qualified: marker-level, mouse and human cells, the sterol-pathway reading means EBP and TM7SF2 are alternative routes | **sign restored as single-source: activation is concordant** (the converter's `same`), qualified: one study, antagonist-only target control, and the 106 associations that follow are one study counted many times, not 106 confirmations; the neonatal liability of glucocorticoids is not scored here |
| Why not an abstention | the evidence is replicated and has a genetic control | an abstention here would rest on the 'volume' of the result, which is not a property of the evidence; the qualification above is carried in the note instead |

Neither sign is a WWOX measurement, an efficacy claim or a ranking: each remains `EXTERNAL_TRANSFER`, and the compounds that reach these targets stay conditional hypotheses. The independent verification of this part is a fresh reader of rows R22 to R31; until then the note `single study` stays on NR3C1.
