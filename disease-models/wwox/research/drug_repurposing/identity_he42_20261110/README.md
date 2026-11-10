# HE42 — identity joins, reproducible inputs (Harness)

## 1. The substring fallback in consume_reader.py
`consume_reader.py` (generation_it41_20261109) joins a name to `identity_table.tsv` by exact lowercase name, then by `k in name or name in k`.

* On the committed IT41 inputs it never fired: every name that reached a row did so by exact match (checked over `compound_view.tsv`).
  So no wrong identity is in the delivered `compound_identity_join.tsv`.
* On realistic inputs it assigns the wrong row, silently (reproduced; fixtures in `test_compound_identity.py::JoinNames`):
  `GYKI 52466 / GYKI 53655` (two compounds in one cell) -> the first key's row for the whole cell; `Brilliant Blue` -> the FCF row;
  `Ro 25` -> Ro 25-6981; `GYKI 5` -> GYKI 52466; `Ro` -> ifenprodil or Ro 25-6981.
* Correction, in the reusable component: `compound_identity.join_names(name, table_keys)`.
  A name reaches a row only as EXACT, QUALIFIED (salt, stereo prefix, isotope label, deuterated form; the qualifier is kept in the output) or
  MULTI_PART (a cell naming several compounds, each resolved alone; a parenthetical comment is not split). A fragment or prefix is PROPOSED_ONLY
  (candidate keys listed, no row attached). An unrelated name (`brilliant blue g`, `d-APV`) is NO_CANDIDATE.
  A qualified form (labelled, stereoisomer) links to the parent's row with the qualifier visible; it is not asserted to be the same molecule.
* `identity_join.py` shows the call; its output `compound_identity_join_he42.tsv` has the same columns as the Orchestrator's file plus link, key, qualifier, proposed_keys.
  The Orchestrator's `consume_reader.py` is not edited here (their file); replacing its fallback line by `ci.join_names` is the whole change.

## 2. onfasprodil and NP10679
Not only a missing table row. Both are qualified catalogue records: `CAT:CHEMBL5095074` ONFASPRODIL (NAME_EXACT, synonyms include MIJ-821) and `CAT:CHEMBL5095254` NP-10679
(SYNONYM_EXACT from `NP10679`, a separator variant of the record name). `NO_IDENTITY_ROW` meant "no row in the local table".
`identity_table_additions.tsv` (also appended to `identity_it41_20261109/identity_table.tsv`) adds the rows requested by the Orchestrator for onfasprodil, NP10679, radiprodil, traxoprodil,
rislenemdaz, EVT-101, DQP-1105 (one row per subunit), ZD7288 and ivabradine (HCN1-4), carbenoxolone (GJD2, PANX1), d-APV and D-AP5.
Levels are those of `compound_identity` (selectivity NOT_ASSESSED). Gaps that stay as they are:

* DQP-1105: NOT_FOUND_BY_NAME in the catalogue -> NOT_READ on all four subunits. That says nothing about the compound.
* d-APV: NOT_FOUND_BY_NAME; the catalogue stores `D-Ap5`, found as D-AP5. The equivalence is not declared (no registry statement read in this task).
* ZD7288: catalogue record without a ChEMBL id, so only SOURCE_INTERACTION rows were read; MALAT1 also appears among its DGIdb rows.
* NP10679: ChEMBL activities exist (2 rows, COMPLETE) but none under GRIN2B -> EMPTY_RESULT, not evidence of absence.

## 3. Reproducible input of action_search.py
`action_search.py` fell back to an absolute path in the main checkout when `catalog/cache` was absent in the worktree. A clean clone therefore either read another checkout's file silently or failed with a traceback.
Now `compound_catalog.cache_file("gtopdb/interactions.csv")` (location: `$LEGEND_CATALOG_CACHE` else `catalog/cache`) checks the file against the SHA-256 pinned in `catalog/cache_manifest.json`.
Absent or changed -> `INPUT_NOT_AVAILABLE`, exit 3, with the URL and the pinned digest; nothing is written. The run prints the path and the digest it used.
Recipe: download `https://www.guidetopharmacology.org/DATA/interactions.csv` (public, terms in the manifest; not redistributed here) into `<cache>/gtopdb/`, `sha256sum` must equal the pin,
then `LEGEND_CATALOG_CACHE=<cache> python3 action_search.py`.
A second reproducibility defect: `search_rows.tsv` row order depended on the hash seed (iteration over a set of gene symbols); now sorted. Same rows (identical sorted digest); `PYTHONHASHSEED=1` and `=2` give identical files.
Truncations: `names` was cut at 160 and `sites` at 120 characters in `molecules.tsv`. Measured: 0 of 226 rows reached either limit, so no information was lost; the cut is removed anyway because `names` feeds identity joins. `molecules.tsv` is byte-identical before and after.

## 4. Shareable view: why the IT41 compound names are withheld (H5)
Terms read on 2026-11-10 (official pages): ChEMBL "about": "The ChEMBL data is made available on a Creative Commons Attribution-Share Alike 3.0 Unported License"; the page says nothing on attribution wording, on what share-alike covers, or on names and identifiers.
GtoPdb about.jsp: "The Guide to PHARMACOLOGY database is licensed under the Open Data Commons Open Database License (ODbL)", contents "under a Creative Commons Attribution-ShareAlike 4.0"; silent on derived databases and on reusing ligand names. Code and data licences were read separately; neither page grants or forbids a single name.
Specific uncertainty kept: whether one drug name taken from ChEMBL or GtoPdb is protected content is not answered by these pages. This is not a legal audit; the repository's mechanism (shareable_sources.json: class A name sources) decides.
Check (`compound_names_shareable_basis.tsv`, 17 names of `compound_view.tsv`): for the best name match of each, the catalogue's `name_source` is `ChEMBL pref_name` or `DGIdb drug_name`; none is a class-A name source (MATRIX list, openFDA NDC), and no record of the 8 approved/clinical names searched carries a class-A source either.
So the omission follows the existing rule and is not an over-block. Nothing was whitelisted. What can be shown: the own-text fields (label, action, rationale, open premise, counter, next test), kind and order.
Conditions for showing names: (a) a separate share-alike file with its own licence text and credit line (ChEMBL CC BY-SA 3.0; GtoPdb ODbL / CC BY-SA 4.0), as `catalog/README.md` and `shareable_sources.json` class B already prescribe; or (b) a class-A name source for the compound (none for these 17).

## 5. Coordinator cost and targeted recall (H3)
Perimeter: the transcript of the Harness session (zero delegates), the slice from the IT41 mandate (`--since 2026-11-09T22:38`), read with `session_model_census.py` (extended: `--since`, share of cache read due to the start context, context drops).
Tokens are as logged; no conversion to plan share or money.

| Component of the slice (222 turns, one model) | Observed |
|---|---|
| Start context | 169,327 tokens; re-read on every turn = 65% of the 57.9 M cache read |
| Growth during the slice | peak 408,553; one drop (compaction) |
| Text of tool results, each carried to the end of the slice | about 14% of cache read (190 results, 260 thousand characters; largest 4-20 thousand characters; 5 results above 8 thousand characters carried about 3%) |
| Images / cold history | one earlier 566 thousand-character image block (JSON, not text) lies before the slice; not counted as text |
| Verification versus production | not separable in this transcript (no delegate); the verifier role of earlier mandates is in `delegation_budget.md` |

Cause chosen: the length of the context a mandate starts in, not tool-output size. Correction: the paragraph "The coordinator's own cost" in `framework/protocols/delegation_budget.md` plus the census fields that make the figure reproducible per mandate. No runtime change.

Targeted versus current recall, four real questions (scripted shell, no agent, no private memory in the loop; "current" = read in full every file that mentions the key; "targeted" = the one table row, status command or tool call that answers):

| Question | Current: files / bytes | Targeted: bytes | Answer found |
|---|---|---|---|
| source and basis of the GYKI 52466 label conflict | 12 / 61,471 | 1,788 | yes (basis, date) |
| state of the IT41 mandate and its next step | 1 / 7,483 | 183 | yes (COMPLETE) |
| are GYKI 53655 and GYKI 52466 the same | 2 / 14,926 | 4,762 | yes (distinct_from declared) |
| which code consumes identity_table.tsv | 6 / 22,499 | 1,141 | yes (consume_reader.py) |

No omission in the four. Limits: a simulation of reading habits, not a measured agent run; the targeted route requires knowing the key (all four did); time was under one second each. The originals stay in place and the targeted answers cite file and row, so the original is opened whenever the decision needs it.
