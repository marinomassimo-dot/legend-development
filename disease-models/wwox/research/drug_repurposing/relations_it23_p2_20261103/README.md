# IT23 P2: can the Every Cure knowledge graph (EC-KG) add relation types the generator lacks? (2026-11-03)

Non-canonical research material. Public edition: the subject is the WWOX-DEE reference genotype class. **Not medical advice.**
Zero spend, no account, no key; no e-mail address or personal datum was sent anywhere. Nothing here edits a scientific current file,
a registry, a card, the ranking or the receipt ledger.

## 1. Decision

**WATCH.** Do not adopt EC-KG as a source of compound-target actions. Keep the recipe (this folder) and revisit on the triggers in section 8.

Reasons, each measured below:

1. **The assets exist and are downloadable**, key-less, with provenance fields (primary and aggregator source, publications, knowledge level, agent type, qualifiers). The earlier "data unavailable" note is wrong; so is the idea that the graph is small (81,149,812 edges, 7,354,612 nodes).
2. **On the generator's own question (compound, target, action) it adds almost nothing usable.** For the 613 of 868 proposal families that could be matched, 1,271 of the generator's 1,412 signed pairs (90.0 percent) are already in EC-KG, so the overlap is high and EC-KG's contribution is redundancy. Of the 17,068 pairs that are new and have an origin independent of ChEMBL, GtoPdb and DGIdb, 97.3 percent come from just two sources: LINCS (expression signatures) and CTD (custom licence). Only 536 carry an activity-level sign, 220 have two independent origins.
3. **It does add relation types the generator has no table for**, chiefly compound to disease (treats, contraindicated_in), adverse events (FAERS, SIDER, DrugCentral), compound to gene expression change (LINCS, CTD) and gene to disease or phenotype edges around WWOX (section 6). The most useful of these for LEGEND is the safety family, for example 26 matched compounds with a seizure-type adverse event in FAERS (CC0) and 21 with a DrugCentral seizure contraindication. That is a separate, smaller piece of work than adopting a graph.
4. **"Provenance-first" is only partly true in the data.** 178,055 of 699,408 fetched rows (25.5 percent) carry `primary_knowledge_source = infores:primekg`, an aggregator in the primary field, so their true origin cannot be told apart from DrugBank or other rows. Another 25.4 percent are DrugBank (CC BY-NC 4.0). Counting redundant copies as one origin is therefore not fully possible for a quarter of the subset.
5. **Redistribution is limited.** Of 41,397 W and 1-hop rows only 11,417 come from sources whose stated licence is permissive (CC0, CC BY, MIT, Apache, BSD, public domain). The rest are share-alike, non-commercial, UMLS-licensed, custom or aggregator rows and are kept as hashes only.

## 2. Assets (full table: `assets.tsv`)

| What | Where | Version | Size |
|---|---|---|---|
| Data (the release the preprint points to) | Zenodo record 10.5281/zenodo.20815442 (concept 10.5281/zenodo.20815441), reached from the ec-kg README | v0.15.19, 2026-06-23 | `kg-edges.parquet` 1,229,523,615 B; `kg-nodes.parquet` 317,316,819 B; drug-list, disease-list, indications-list under 3.3 MB |
| Data mirror | Hugging Face `everycure/kg-edges` (commit `fcd05859`), `everycure/kg-nodes` (commit `c9c60b2c`), modified 2026-05-28 | same row counts as Zenodo (81,149,812 / 7,354,612) | 49 + 8 parquet shards, 3.56 GB + 0.87 GB; **not downloaded**, so equality of content with Zenodo is not verified |
| Code, paper figures | github.com/everycure-org/ec-kg | HEAD `6422e2fd`, 2026-11-01, no tag, no release | about 1.9 MB |
| Code, pipeline | github.com/everycure-org/matrix | HEAD `2cfe733d` 2026-11-03; release v0.15.0-matrix 2026-02-05 | about 208 MB |
| Model or weights | none found: `huggingface.co/api/models?author=everycure` returns `[]`; Zenodo free-text search for "everycure" returns 0 hits. `everycure/matrix-scores` is a table of prediction scores, no licence declared, not fetched | | |
| Preprint | bioRxiv 10.64898/2026.08.26.747253, v1, 2026-08-31 (identity confirmed through the bioRxiv API; the full text was **not** read) | | |

Discrepancy found: the Hugging Face cards and the public-releases page say the published graph merges two sources (ROBOKOP and RTX-KG2); the Zenodo
data carry a third upstream, `primekg` (178,055 of the fetched rows have `upstream_data_source = [primekg]`), as the preprint says.

## 3. Licences, quoted from what was read

Code: Apache-2.0 for both repositories (`LICENSE` first lines "Apache License / Version 2.0, January 2004"; GitHub API `spdx_id: Apache-2.0`).

Data: Zenodo metadata `license: cc-by-4.0`. The Hugging Face `LICENSE.md` (read in full) says:
- "The **Every Cure Knowledge Graph (EC KG)** is licensed under the **Creative Commons Attribution 4.0 International License** ... unless otherwise noted."
- "Users must comply with the licenses of the first-level knowledge sources and primary knowledge sources datasets. Where incorporated source data is subject to restrictions such as **Share-Alike (SA), Non-Commercial (NC), or No Derivatives (ND)**, those restrictions **remain in force for the original content**."
- "**CC BY 4.0 applies exclusively to the integration, curation, harmonization and added metadata** created by Every Cure ... while **original source licenses continue to govern their respective content**."

The per-source table (docs.dev.everycure.org/releases/primary_knowledge_sources, page dated 2026-07-23) lists, among the sources that appear in the subset: DrugBank "CC BY-NC 4.0 (Complete Database ...), CC0 1.0 (Open Data)"; ChEMBL "CC BY-SA 3.0"; BindingDB "CC BY 3.0 (BindingDB curated), CC BY-SA 3.0 (ChEMBL-derived)"; DrugCentral "CC BY-SA 4.0"; Guide to Pharmacology "CC BY-SA 4.0"; SIDER "CC BY-NC-SA 4.0"; CTD "Custom CTD License - free for research/education; commercial use requires written permission; attribution, linking, and usage notification required"; Semantic Medline and MeSH "UMLS Metathesaurus"; LINCS "CC BY 4.0"; FAERS "Public Domain and CC0 1.0"; DGIdb "MIT License"; IntAct "CC BY 4.0". PrimeKG is not in the table at all.
The preprint text itself is `cc_by_nd` (bioRxiv metadata); that covers the paper, not the data.

Consequence: the repository's redistribution rule is applied row by row on the **stated licence of the primary source**. Permissive rows are published in `extract_ecKG_wwox.tsv` (attribution: Every Cure Knowledge Graph v0.15.19, doi 10.5281/zenodo.20815442, CC BY 4.0, plus the source named in each row). All other rows are digest-only. This is not legal advice; the table is Every Cure's own statement and was not checked at each source.

## 4. What was fetched, and how (steps 1, 2, 5)

The 1.23 GB edge file is one parquet with 661 row groups and **no column statistics**, so no filter can skip row groups. Zenodo answers more than 133 requests per minute with HTTP 429. Route used (all in `reproduce_ecKG_wwox.py`): HTTP Range requests, throttled to about 110 per minute, row group by row group.

| Stage | Read | Kept |
|---|---|---|
| nodes | 5 of 10 columns of the node file (DuckDB range reads) | 204 MB slim table in scratch |
| so | columns `subject`, `object` of all 81,149,812 edges | 853 MB slim table in scratch |
| select | local | WWOX = node `NCBIGene:51741` (carries `HGNC:12799`; two other nodes named WWOX are non-human); 663 compound nodes matched to 613 of the 868 families in `proposals_it21.tsv` (by normalised base name or ChEMBL id; 411 by name only, 93 by ChEMBL only, 159 both); 1-hop set N1 = 1,337 nodes of type gene, protein, drug, disease, phenotype or cell; 2-hop set N2 = 274,399 nodes |
| fetch | every row group that holds a target row, all columns (all 661 are hit) | 699,408 edge rows: 3,293 incident to WWOX plus 696,115 incident to a matched compound; 66 distinct primary sources |

Network volume was not measured; by file size it is of the order of 0.5 GB (scan) + 1.2 GB (fetch) + 0.2 GB (nodes), streamed in pieces of about 2 MB and never stored whole. That exceeds the 300 MB per single download only as the sum of a query; no single file or request was above 2 MB (a whole-file download would have been 1.23 GB, the single "query-able route" being Range plus column pruning).
The N2 set is described but not written whole (274,399 nodes); the node table keeps W, N1 and the N2 nodes joined to a kept row.

Failures recorded (step 5):
- First scan with DuckDB `read_parquet` on the Zenodo URL: `HTTP GET error ... (HTTP 429 Too Many Requests)`, body `{"message":"133 per 1 minute","status":429}`, "retry quota for 'https://zenodo.org' exhausted". Branch replaced by the throttled reader.
- `python3 -m venv` failed (no `ensurepip`); packages were installed with `pip install --target` into scratch instead.
- A direct GET of `https://zenodo.org/api/records/20815441` (concept id) returns a 302 to `/api/records/20815442` (version id); the first parse failed on the redirect, the second succeeded.

## 5. How evidence was classified (step 3)

Every kept edge has: subject, object, predicate, `qualified_predicate`, aspect and direction qualifiers (subject and object), species and disease context, `primary_knowledge_source`, `aggregator_knowledge_source`, `publications`, `knowledge_level`, `agent_type`, upstream graph, `num_references`, extraction confidence, affinity.
`evidence_class`, in this order, first match wins (a heuristic on declared fields, not a re-reading of any source):
- **PREDICTION**: `knowledge_level = prediction`, or `agent_type = text_mining_agent`, or primary source SemMedDB or the targeted text-mining API, or an extraction confidence score is present.
- **OBSERVED**: a knowledge assertion with an anchor: a PMID or DOI in `publications`, or an `affinity`, or a `supporting_study_method_type`.
- **ANNOTATION**: everything else (database or ontology assertions without a stated anchor, FAERS and LINCS pipelines, entailments, PrimeKG-labelled rows).

Known weaknesses: LINCS rows come from experiments but are declared as a data-analysis pipeline without publications, so they land in ANNOTATION. CTD rows carry PMIDs and land in OBSERVED, but most are expression-level. An activity-level sign (+1 or -1) is derived from the object direction only when the aspect is `activity` or `activity_or_abundance`, and only with the compound as subject; expression aspects give no sign, the same discipline the generator applies.
**Origins**: one origin = one `primary_knowledge_source`; the copies carried by `rtx-kg2`, `robokop` and `primekg` as aggregator or upstream count as the same origin. An origin is called independent only if it is not ChEMBL, GtoPdb, DGIdb (the generator's compound side) and not one of the copy-prone ones (DrugBank, DrugCentral, BindingDB, Pharos, PrimeKG, Hetionet, ChEBI, NCIt), which may re-publish those.

## 6. What it adds against LEGEND (step 4); counts in `novelty.tsv`, `novelty_summary.json`

Compound to gene or protein pairs for the matched compounds: 85,662 distinct pairs.

| Status | Pairs | Meaning |
|---|---|---|
| IN_LEGEND_SAME_SIGN | 971 | pair and sign already in `family_actions` |
| IN_LEGEND_MIXED_SIGN | 106 | EC-KG carries both signs |
| IN_LEGEND_OPPOSITE_SIGN | 15 | EC-KG sign opposes the generator's (8 rest on prediction rows only; the others include PAC-1/CASP3, regorafenib/EPHA2, dactolisib/PIK3CB and PIK3R1, cyproterone/PGR, the BMP agonists on BMPR1A/BMPR2) |
| IN_LEGEND_ECKG_UNSIGNED | 172 | in `family_actions`, EC-KG has no activity sign |
| IN_LEGEND_UNSIGNED_ONLY | 1,227 | in `family_targets_any` only |
| NEW_PAIR_LEGEND_ORIGIN_PRESENT | 2,157 | not in LEGEND, but ChEMBL, GtoPdb or DGIdb is an origin: dropped by the generator's guards or a family mismatch, **not new knowledge** |
| NEW_PAIR_COPY_PRONE_ORIGIN_ONLY | 2,881 | only DrugBank, DrugCentral, BindingDB, PrimeKG and kin: probably the same claims |
| **NEW_PAIR_INDEPENDENT_ORIGIN** | **17,068** (190 compounds) | genuinely new origin; 10,319 LINCS only, 6,173 CTD only, 112 both |
| NEW_PAIR_PREDICTION_ONLY | 38,641 | text mining only; not counted |
| TARGET_NOT_MAPPED_TO_HGNC | 22,424 | target is a UMLS concept, UniProt or PR id without HGNC; not compared |

Of the 17,068: 6,468 best-evidence OBSERVED (CTD), 10,600 ANNOTATION (mostly LINCS); 536 have an activity-level sign; 220 have two independent origins.
Other relation types present in the subset and absent from the generator's tables (counts are fetched rows): compound to disease `treats_or_applied_or_studied_to_treat` 45,912 (mostly SemMedDB and text mining), `treats` 6,510, `applied_to_treat` 3,708, `contraindicated_in` 11,642, `has_adverse_event` 13,892 (FAERS), `has_side_effect` 5,866, compound to gene `affects`/`regulates` with expression aspects. Around WWOX itself (3,293 rows): 562 `associated_with`, 517 `interacts_with`, 372 `gene_associated_with_condition`, 303 `expressed_in`, 223 `directly_physically_interacts_with` (301 IntAct rows), 150 HPO phenotype rows; 1,104 of the 3,293 are PrimeKG-labelled, 839 SemMedDB, so only 109 are OBSERVED.
Compound to disease edges were not compared with LEGEND: the generator inputs (`family_actions`, `family_targets_any`) hold no indication or adverse-event table.

### The 10 most informative genuinely new relations (`top10_new_relations.tsv`)

Selection: status NEW_PAIR_INDEPENDENT_ORIGIN, the target is a direct WWOX neighbour (N1) with at least one non-prediction edge to WWOX, ranked by number of independent origins, activity-level sign, then PMIDs; at most two per compound and per target. **Each is a path in a graph, not a causal chain**: the compound leg and the WWOX leg come from different sources and different contexts, and nothing says the compound acts on WWOX.

| # | Compound | Bridge node | Compound-bridge origins (non-prediction) | Sign | PMIDs | Bridge-WWOX leg (source, class) |
|---|---|---|---|---|---|---|
| 1 | tretinoin | HOXA1 | CTD, LINCS | -/+ | 10 | IntAct physical interaction (ANNOTATION) |
| 2 | curcumin | HDAC1 | BindingDB, CTD | - | 6 | PrimeKG interacts_with (ANNOTATION) |
| 3 | curcumin | HIF1A | CTD | - | 2 | PrimeKG interacts_with (ANNOTATION) |
| 4 | nifedipine | TP53 | CTD | + | 1 | IntAct physical (ANNOTATION), Hetionet |
| 5 | disulfiram | MAPK8 | CTD | + | 1 | Hetionet, PrimeKG (ANNOTATION) |
| 6 | epigallocatechin gallate | MAPK8 | CTD | -/+ | 1 | Hetionet, PrimeKG (ANNOTATION) |
| 7 | tretinoin | PRKCA | CTD | - | 1 | IntAct physical (ANNOTATION) |
| 8 | progesterone | NOS3 | CTD | + | 1 | IntAct physical (ANNOTATION) |
| 9 | TCDD | IGF1 | CTD | - | 1 | LINCS regulates (ANNOTATION) |
| 10 | TCDD | PRKCA | CTD | + | 1 | IntAct physical (ANNOTATION) |

Honest reading: the list is dominated by CTD (one origin each, custom licence), the compounds are promiscuous natural or toxicological agents, and every WWOX leg is an annotation, not a measurement. These are leads for a lookup, not candidates; none of them is a proposal in `proposals_it21.tsv` by this route.

## 7. Files

| File | Content |
|---|---|
| `assets.tsv` | every asset: url, version, size, licence of code and of data, retrieval date |
| `extract_ecKG_wwox.tsv` | 11,417 edges (W and 1-hop, compound to N1) from sources with a permissive stated licence; 25 columns incl. provenance, qualifiers, `evidence_class`, `source_licence_stated` |
| `extract_digest_restricted.tsv`, `extract_digest_summary.tsv` | the 29,980 W and N1 rows from restricted sources as SHA-256 of key fields plus subject, object, predicate, source, evidence class; and counts per source for all hoods (including N2) |
| `nodes_ecKG_wwox.tsv` | W, N1 and the N2 nodes joined to a kept row (id, name, category, upstream) |
| `novelty.tsv` | per compound-target pair: status, origins, aggregators, evidence, sign, PMID count (rows with a LEGEND counterpart or an independent new origin) |
| `novelty_summary.json`, `top10_new_relations.tsv` | all counts used above; the ten paths |
| `reproduce_ecKG_wwox.py`, `build_ecKG_tables.py` | recipe; run `PYTHONPATH=<duckdb+pyarrow> python3 reproduce_ecKG_wwox.py all --work <scratch> --repo <drug_repurposing dir> --out <this dir>` (about 40 minutes, mostly throttled requests) |

Release note for the integrator: `extract_ecKG_wwox.tsv` (3.0 MB) and `extract_digest_restricted.tsv` (4.8 MB) are third-party derived rows; `scripts/public_release_gate.py` passes on this tree (0 blocks), but under the repository rule on third-party raw they may belong under the ignored `files/` area with only the SHA-256 kept here. The producer script has no shebang.

## 8. What could not be verified, and when to revisit

- The preprint text was not read; "about 95 primary sources" and "provenance-first" are the task's wording. The licence page lists 92 resources, the subset shows 66 distinct primary sources.
- The Hugging Face copy was not downloaded; it matches Zenodo only by row count.
- Compound matching is by normalised name or ChEMBL id with no structure check, no salt or prodrug handling; 255 of the 868 proposal families found no node.
- Evidence classes and signs are rules on declared fields; no edge was traced to its original paper. PrimeKG-labelled rows cannot be traced at all from this table.
- Licence classes are Every Cure's statements; "stated permissive" is not a legal clearance.
- N2 was counted, not delivered.

Revisit (WATCH to ADOPT-AS-EXTRACT) when: (a) a release resolves PrimeKG rows to their true primary sources; (b) LEGEND decides to add a safety lookup (seizure adverse events and contraindications from FAERS and DrugCentral), a narrow use that needs only permissive rows plus a licence check on DrugCentral; or (c) the generator gains a relation type for chemical-induced expression (LINCS, CC BY) with a stated rule for reading it.
