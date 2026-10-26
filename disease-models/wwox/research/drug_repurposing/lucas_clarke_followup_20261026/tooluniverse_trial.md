# ToolUniverse trial — one complete question, 2026-10-26

Scientist `scientist-c`. The verdict is about **this query only**.

## The question
"Which compounds modulate PDK2 (pyruvate dehydrogenase kinase isozyme 2; HGNC:8810, UniProt Q15119, Ensembl ENSG00000005882, ChEMBL target CHEMBL3861), with what action, from which sources?" PDK2 was resolved first and by accession; the symbol "PDK1" was avoided because of the PDPK1 collision (`compounds_and_sources.md`).

## Install, version, licence
Isolated environment outside the repository (`uv venv` in the session scratch directory; nothing installed into the repository, `pyproject` or system Python). `tooluniverse` **1.5.7**, **Apache-2.0** (licence file shipped in the wheel's metadata), upstream `github.com/mims-harvard/ToolUniverse`. It pulled 111 packages, about 489 MB on disk, and `load_tools()` registered **2719 tools**. No key, no account, no e-mail address supplied; the run called public databases through the package's own wrappers.

## Calls (raw result: `tu_results.json`, comparison: `tu_compare.json`)
1. `DGIdb_get_drug_gene_interactions` genes PDK2.
2. `OpenTargets_get_associated_drugs_by_target_ensemblID` ENSG00000005882.
3. `ChEMBL_search_activities` target CHEMBL3861, limit 1000 (the documented list-of-rows route: the package's `ChEMBL_search_mechanisms` documents that target filters are not supported).

## Comparison on equivalent results (list against list)
| Source | ToolUniverse returned | My direct/adapter route returned | Equal? |
|---|---|---|---|
| DGIdb, PDK2 | 4 compounds: VER-246608 (inhibitor; Guide to Pharmacology), AZD7545 (inhibitor; Drug Repurposing Hub, Guide to Pharmacology), SODIUM DICHLOROACETATE (inhibitor; ChEMBL), DEVIMISTAT (no action; a clinical-trial census) | the same 4 compounds with the same action types and sources (`dgidb_interactions.tsv`) | **yes, same compounds, actions and sources** |
| Open Targets, PDK2 | 1 candidate: sodium dichloroacetate, phase 3, congenital lactic acidosis | the same 1 (`opentargets_lists.tsv`) | yes |
| ChEMBL activities, CHEMBL3861 | 1000 rows, 864 molecules, 739 with a pchembl value | direct REST, same first 1000 rows: 864 molecules, 739 with pchembl | **yes, identical molecule sets** |

## What it did and did not add
- **Same documented lists, no extra compound.** For this query ToolUniverse is a wrapper over the same three services I had already called.
- **Fields dropped (in this call, default arguments):** its DGIdb tool returned the action type and source names but not the `approved` flag, the interaction score, the directionality field or the publication counts that `kg_thin_slice.drug_packet` carries (`dgidb_packet.json`).
- **Truncation not stated:** the ChEMBL call returned the first 1000 of **2527** activity rows (the service's `page_meta.total_count`, read on my direct call); the ToolUniverse result carried no total and no truncation flag (`metadata` empty), so a reader would take 1000 for the whole. The repository's adapters and `kg_thin_slice` state truncation.
- **No resolution step:** it accepted a gene symbol or Ensembl id as given; the PDK1/PDPK1 collision would pass through it unflagged (not tested for PDK1 in this trial, so that is a design observation, not a measured failure).
- **Cost:** large dependency footprint for what three small calls did. No call failed.
- **Not evaluated:** its other 2700 tools, its agentic routing, any query other than this one.

## Verdict (this query only)
**WATCH, not adopted.** Same compounds, actions and sources as DGIdb, Open Targets and ChEMBL called directly, with fewer fields and a silent 1000-row cap; no capability the repository's adapters lack for a "compounds-for-target" question. Reopen if a question needs a source the adapters do not wrap (a different database, or the many-source routing itself) and the same list-against-list comparison is made on it.
