# WWOX records naming a cell line that the register marks as problematic (IT, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Question accepted by ADV with five conditions; pre-registration: `PREREG_CELL_LINE_IDENTITY_IT_20261125.md`. Register: Cellosaurus flat file, version 57.0, retrieved 2026-11-25 by plain request, sha256 `3b5a9fc56b49854230ae90fb7cee57a3bf9f961df98be215a634203526f476ef`. ICLAC was not queried separately: its entries are cited inside the register comments and are not an independent source here.

## 1 · The denominator
**78 lines** named in the perimeter (`census_lines.tsv`, sha256 `b0e26c77a23f106b8e7995aeecfe24938f736bc3879c0d11117aee9d5605f3f5`, frozen before the look-up): **42** by structured fields, **78** by text (36 text-only, none field-only, because the text route scans the whole perimeter, fields included).

**What the 36 text-only entries are.** Real cultures, not false hits: 34 established lines and two donor fibroblast cultures known by repository number (GM08399, GM18453). They are missing from route S because only cards, the paper registry and the literature log have model fields at all (19 of the 36 appear in a ledger, 7 in the expression-boost census, 1 in a claim or the working model), and because many registry model fields say «cell line» without naming it. False hits (author initials KB and MKN, a hypothesis label H1, gene and residue tokens) were removed by hand before the freeze.

**Both ratios.** Flagged lines: **8 of 78** by the full census; **1 of 42** by structured fields (SH-SY5Y, the mildest note). Seven of the eight are visible only in text, so a field-based audit would have missed every contaminated line.

**Recall check (after the freeze, register-driven).** Every name and synonym of the register's flagged entries was searched in the perimeter; no further flagged line was found (remaining hits were surnames, years and residue numbers). Names under three characters were excluded; the only one that matters, KB, occurs only as author initials.

## 2 · The eight flagged lines
| Line | Record | Register wording (short) | Class | What changes in our records |
|---|---|---|---|---|
| HO-8910 | CVCL_6868 | Contaminated; HeLa derivative (originally ovarian) | A | expression-boost census rows A2 and B1 are not ovarian evidence and share one line; `DL-REPO-003` already carries the flag |
| SGC-7901 | CVCL_0520 | Contaminated; HeLa derivative (originally gastric) | A | census row A7: the gastric attribution cannot rest on this line |
| BGC-823 | CVCL_3360 | Contaminated; HeLa derivative (originally gastric) | A | same row A7 |
| SMMC-7721 | CVCL_0534 | Contaminated; HeLa derivative (originally hepatocellular) | A | corpus stub and literature record only (PMID 22736928, title says «hepatoma»); no claim link: label to carry if ever promoted |
| CNE2 | CVCL_6889 | Contaminated; STR identical to CNE-1, seems a HeLa hybrid | A | corpus stub and literature record only (PMID 31966369); no claim link: same |
| U87MG | CVCL_0022 (ATCC stock) | Misidentified: not the original line; probably still glioblastoma | A (label) | `DL-MECH-054`: label only |
| HepG2 | CVCL_0027 | Misclassified: hepatoblastoma, not hepatocellular carcinoma | B | two ledger entries use it as a liver-derived reporter system: no inference changes |
| SH-SY5Y | CVCL_0019 | Partially contaminated (some redistributors, mouse line) | B | 13 records including claims and one card: no change unless a paper's own stock is shown affected |

Class A here means the record says contaminated or misidentified (HO-8910 carries both «contaminated» and «HeLa derivative»); class B is a note that is not a plain misidentification. The sign of no finding is inferred from the class.

## 3 · Predictions
P1 (1 to 8 flagged): held, at the upper edge. **P2 failed as written:** SH-SY5Y, a flagged line (partial note), carries neural statements including a WWOX knock-down (`CLAIM 035`, working model, `DL-MECH-064` and `-066`); no neural statement rests on a HeLa-derived line, and nothing shows the stocks used were affected. P3 held: census rows A2 and B1 (one line, HO-8910) read as two ovarian observations, and row A7 as three gastric lines.

## 4 · Blind second reader
One delegate (sonnet, effort high), own parser over the same file, given the 78 names and not these results (`VERIFIER_REPORT_AS_DELIVERED_CELL_LINES_IT_20261125.txt`). It found the same eight flagged entries. SUPPORTED: the four HeLa derivatives, CNE-2, U87MG (qualified: «most probably» glioblastoma) and the shared line of rows A2 and B1. PARTLY: «label only» for HepG2 is too weak where a record says hepatocellular carcinoma; the SH-SY5Y note states no consequence. **Overturned, and checked by IT against the PubMed abstract:** PMID 25720522 does report WWOX: transcripts of all five genes rose in SNU-719 after 5-aza and/or trichostatin A; no per-line result is given for the three EBV-negative lines. IT's own line in `DL-REPO-003` said the opposite and is corrected. **Two further findings, checked and written by wording:** (a) the therapeutic ledger calls PMID 35984507 an observation «in neurons»; its abstract says the experiments were mainly in differentiated SH-SY5Y neuroblastoma cells (plus diabetic rat brain homogenates); (b) the hepatocellular negative (PMID 15266310) does not name the treated lines, and its low expressors include Chang (registered HeLa derivative, `CVCL_0238`) and SK-Hep-1 (registered misclassified, probably endothelial, `CVCL_0525`): both lie outside the census because no record names them, which is the main limit of a records-only perimeter. Not checked: the lines behind the evodiamine HCC statement of the discovery ledger.

## 5 · Limits
Perimeter only: dossiers, other analysis files, session reports and held full texts were not scanned. The register speaks about a line name, not about the stock a given laboratory used. Papers behind rows A2, A7 and the corpus stubs were not re-read.
