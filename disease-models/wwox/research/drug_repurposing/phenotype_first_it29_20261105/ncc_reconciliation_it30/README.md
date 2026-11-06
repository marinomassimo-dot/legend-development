# IT30: the NCC screening table, endpoint qualified (rows S1-32 and S1-33 and the 20 compounds of the IT29 comparison)

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class. Zero spend; official supplements fetched from the publisher's static host and Europe PMC (public, no contact data sent). 2026-11-06.

## Decision (answer first)
* **KEEP** the table as data, with the endpoint it actually carries: the **primary Alamar Blue (AB) viability/metabolic screen of the cytokine-protection paper, values as percent of quetiapine** (paper 2, Table 1 column "AB screening (% quetiapine)"). **DISCARD** its use in IT29 as an oligodendrocyte-differentiation sign: neither as independent counter-evidence (rows S1-32, S1-33, five "contradictions" in the P12 scout) nor as independent confirmation (the five "agreements").
* The assignment is **strong but its cause is unknown**: the two papers' supplements carry the same values, and paper 1's text describes a different normalisation (T3). Do not attribute it to the publisher, the authors or LEGEND. Where paper 1's own Table S2 should be, nobody has been able to say from the files alone.
* **The NR3C1 and CYP51A1 signs are not restored.** Rows S1-32 and S1-33 stay in the signed table as an explicit **hold** (see the note in each row): the targets remain `unresolved`, now because the endpoint-qualified evidence is single-source and marker-level, not because of a contradiction. Restoring the favourable sign is a separate, reasoned decision (below).

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
Counts recomputed by running the same converter and search twice (rows S1-32 and S1-33 present, as committed; absent), same catalogue cache, `NEED-MYELINATION`.
| Output | With the two rows (as committed) | Without them | Real change |
|---|---|---|---|
| Rows in the signed table | 33 | 31 | 2 |
| Coupling rows from the converter | NR3C1 `unresolved`, CYP51A1 `unresolved` | NR3C1 `same`, CYP51A1 `opposite` (each one source, marker-level) | 2 |
| Search associations with a signed label (consistent + opposed) | 97 (29 + 68) | 216 (137 + 79) | 119 |
| Associations whose label differs | | | 114 rows over 111 families (104 `direction_unresolved` to `consistent`, 10 to `opposed`); 106 of the consistent rows are NR3C1 agonists, 2 CYP51A1 |
| IT29 P6 comparison, 20 compounds | Arm C: clobetasol abstained | clobetasol right | 1 compound; it is the circular case (the study that signs the target also tests clobetasol) |
| IT29 P12 scout table | 11 directions "recovered", 5 "contradictions", 6 "agreements" | 0 usable as differentiation direction | 11 (all reclassified, `ncc_20_compounds_it30.tsv`) |
| Dashboard, rankings, hypotheses, the four current files | not consumed | not consumed | none (checked: the view and the rankings do not read the signed table) |

## 4. What is held and why
Keeping the two rows as a hold leaves every committed output as it was (97 signed rows). Removing them without more would raise the signed count to 216, 106 of them one family of glucocorticoid agonists resting on one purified-OPC study with a neonatal glucocorticoid liability noted in the curation. That is the "volume is not quality" case the IT29 README already described, so the sign is not restored here. To restore, read paper 1's methods and the mouse studies' own readouts, then decide NR3C1 and CYP51A1 separately; until then the label is INCONCLUSIVE for the sign and DISCARD for the incongruous counter-evidence.
