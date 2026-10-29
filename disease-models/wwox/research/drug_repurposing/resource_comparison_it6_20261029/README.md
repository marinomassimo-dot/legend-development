# P12 — Resource comparison on real questions (2026-10-29)

Question 1 (from P9): *which compounds are recorded on GluN2B (GRIN2B), and what does each resource say about them?*
Question 2 (P8 finding): *can a pore blocker such as memantine be found on the subunit?* (answered in `../pharmacology_it6_20261029/P8_capability_trial.md`).
Not a benchmark of efficacy; not a new harness. Equivalent results were compared (records on one target entity), never a count against a list.

## Independence first
| Resource | Where its content comes from | Independent of the others? |
|---|---|---|
| ChEMBL REST (live, ChEMBL_37, 2026-05-01) | primary curation | source |
| ChEMBL via ToolUniverse 1.5.7 (`ChEMBL_get_target_activities`) | the same REST endpoint (first row identical to the direct call, same `page_meta`) | **no: a wrapper** |
| GtoPdb 2026.3.1 CSV (local cache) | primary curation, pharmacologist-curated | source |
| GtoPdb via ToolUniverse (`GtoPdb_get_interactions`) | the same `interactions.csv` | **no: a wrapper** |
| DGIdb 2024 (local cache) | imports ChEMBL release 33, GtoPdb 2024.1, PharmGKB, TTD, TEND, TdgClinicalTrial | **no: aggregator**; its ChEMBL rows are an older ChEMBL than the live service |

## Measured, GRIN2B (`compare_grin2b.py`, `grin2b_comparison.json`)
| Dimension | ChEMBL live (adapter) | GtoPdb CSV | DGIdb | ToolUniverse |
|---|---|---|---|---|
| Records on GluN2B | 2,365 activity rows (human single-protein target; 2,000 retrieved, **truncated**, declared) | 38 records, 38 ligands | 97 records, 77 drugs | ChEMBL: 200 per call, `total_count` passed through (6,314 over all types and filters); GtoPdb: `total_matches 39, returned 25` (cap declared) |
| Identity | ChEMBL ids; **18 of 1,795 molecules in the retrieved rows carry a name** (the rest are unnamed research compounds) | ligand ids and names | drug names / RxCUI | same as the wrapped source |
| Action | none in activity rows (curated mechanism is a separate call) | **action and receptor site** (31 and 28 of 38 records) | interaction type on 66 of 97 | as source |
| Potency | yes: relation, value, units, pChEMBL, document | **numeric affinity on only 4 of 38 records** (channel blockers have none) | none | as source |
| Assay context / species | **assay organism, cell type, assay type, confidence per row** (adapter joins the assay endpoint) | target species; assay text on few | none | **not joined** (ChEMBL tool returns the raw activity rows; the frog-oocyte vs human-target distinction needs a second call) |
| Update | live (release 37) | 2026.3.1 (2026-10-12) | ChEMBL 33 and older sources | live |
| Cost observed | 13 requests, 52 s for 2,000 rows | local read | local read | 0.7 s per call; environment install 111 packages; separate venv required |

Name-normalised overlap of the named compounds (lower bound, salts not merged): ChEMBL-retrieved named 18, GtoPdb 38, DGIdb 77; ChEMBL&GtoPdb 1, ChEMBL&DGIdb 4, GtoPdb&DGIdb 21. The small ChEMBL–GtoPdb overlap is not a disagreement: ChEMBL's rows are mostly unnamed research compounds, GtoPdb's list is the named pharmacology of the receptor. DGIdb–GtoPdb overlap is import, not confirmation.

## What each is for, on this question
- **Potency with assay context for a compound or a target:** ChEMBL via the adapter. ToolUniverse adds nothing here (same rows, less context, plus an isolated environment).
- **Which compounds act on the receptor, with action and binding site:** GtoPdb. It has little numeric potency for channel blockers.
- **A quick list of drugs touching the gene:** DGIdb, with the caveat that it re-serves older ChEMBL and GtoPdb.
- **ToolUniverse (the question was whether it adds a capability the repository lacks):** on this question, no. Measured additions: pass-through of `total_matches`/`page_meta` (the adapter also reports them); a discovery catalogue of 2,719 tools (names only were scanned, 48 contain "chembl", 4 "gtopdb", none "nmda"); GtoPdb gene-symbol convenience. Measured costs: a 489 MB-class isolated environment, a 25-row cap on GtoPdb interactions, no assay join. Verdict: **WATCH, no adoption**; the earlier narrow L1000FWD use is unchanged and not repeated.

## Radar (most recent real run, 2026-10-29 05:20 UTC)
Selected `openFDA-NDC` with the outcome TO_TRIAGE: the probe watches `meta.last_updated` (2026-10-27 -> 2026-10-28), the refresh date of a **product catalogue** (138,151 NDC products on 2026-10-29). A refresh is not an approval, a label change for a card-linked compound, or evidence. Triage: **noise; probe removed** from `scout_daily.py` (commit "drop the openFDA-NDC refresh-date probe"); the openFDA adapter still reads NDC on demand. The same run: no new WWOX PubMed ids, no new discovery items, every other probe UNCHANGED (ToolUniverse, TxGNN code and explorer, MATRIX, DGIdb, ChEMBL, Open Targets). The SigCom-LINCS etag change logged on the previous run concerns the LINCS library already analysed; no new question. TxGNN and MATRIX: no condition changed, not reopened.

## Gaps surfaced by the work and small resource searches
- Research-compound identity in ChEMBL needs a structure key; name resolution fails (P8). Candidate: a PubChem/UniChem structure lookup (UniChem is already in the catalogue) - TRIAL only if a card needs a tool compound's potency.
- No resource gives receptor *state* (open-channel, agonist, voltage, Mg2+) as a field; it has to be read from documents.
