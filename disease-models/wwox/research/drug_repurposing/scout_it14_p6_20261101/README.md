# IT14 P6: function -> target -> action -> compound lookup, external resources tried against a declared set

Scientist package P6, task ORCH-ROADMAP-IT14-20261101, host date 2026-10-31 (22:xx UTC). Non-canonical research material. Not medical advice; no dose, schedule or individual recommendation. A retrieved reference shows **coverage, not predictive ability, and is not validation**. Nothing here is WWOX evidence (no query contained the gene). Agreement between sources is not agreement between origins: several sources below copy the same ChEMBL or IUPHAR row.

## 1. Decision

**No external resource earns a place; the module already holds the data and what is missing is a join, not a source.** On a declared set of 8 compounds and 23 expected compound-gene relations (written before any lookup: `declared_set.tsv`), the module's existing sources (ChEMBL mechanism and activity through the adapter, GtoPdb files, DGIdb file, Open Targets mechanism) recovered **22 of 23**, with action type for 20 and a numeric potency for 20. Three candidates (DrugCentral, Pharos, BindingDB) recovered 8, 8 and 12 of the same 22 and **added zero pairs, zero action types and zero potencies** that the existing path lacked. The only relation recovered by nothing is ethosuximide -> KCNJ6 (GIRK2 block), which rests on my memory of the literature and was never checked: absence from every resource is not absence of the effect.

| Resource | Decision | Reason in one line |
|---|---|---|
| ChEMBL (mechanism + activity), GtoPdb files, DGIdb, Open Targets | KEEP (present) | recovered all 22 |
| DrugCentral file | WATCH | 0.96 MB, CC BY-SA 4.0 by link; adds no pair; reopen if a compound class absent from ChEMBL curation is needed (approved drugs only) |
| Pharos GraphQL | DISCARD | values identical to DrugCentral (one origin); target-first list did not contain the declared names |
| BindingDB REST | DISCARD | adds no pair or action; identity of 14 of 22 returned structures unverifiable without a cheminformatics toolkit; no licence sentence on the primary pages read |
| PDSP Ki | DISCARD | default query returned a 204 MB HTML table, no gene column, GPCR-centric; NMDA rows are native rat tissue without subunit |
| IUPHAR REST | DISCARD route | HTTP 401 without a key (registration forbidden); the download files in the module are the same content |
| PubChem bioassay | DISCARD | outcome per assay is not an action; no advantage |
| GitHub / Hugging Face scan | nothing adopted | `scan_github_hf.txt`; only API wrappers (pygtop needs the key-gated service) and dataset mirrors of BindingDB/ChEMBL (CC BY-SA 3.0 copies) |

**The single minimal integration (not applied; extends an existing script, adds no system):** in `framework/adapters/chembl.py`, function `_activities`, resolve each distinct `target_chembl_id` of the returned rows through `GET /target.json?target_chembl_id__in=...` (batches of 40, the same pattern the function already uses for assays) and add to every activity hit `gene_symbols` (GENE_SYMBOL synonyms of the target components), `target_type` and a `non_gene_target` flag set for the placeholder targets `Unchecked` and `NON-PROTEIN TARGET`. Reason, measured here: 152 of 517 ChEMBL rows for the declared compounds had no gene (96 are the `Unchecked` placeholder), and without gene symbols the module cannot ask "which compounds act on GRIN2B" across heteromeric complex targets without hand mapping (`trial_p6.py` does it in 15 lines, `selectivity_p6.py` then groups same-document rows). A test in `test_repurposing_adapter.py` would pin the fixture. This is a proposal in a README only.

## 2. What was run

Declared set (`declared_set.tsv`, fixed before looking, "basis" column says what I knew): ethosuximide (CACNA1G/H/I and KCNJ6), d-AP5 (GRIN1, GRIN2A-D), ezogabine/retigabine (KCNQ2, KCNQ3), bumetanide (SLC12A2, SLC12A1), radiprodil (GRIN2B), Ro 25-6981 (GRIN2B), apinocaltamide (CACNA1G/H/I), memantine (GRIN1, GRIN2A-D) = 23 pairs. Identity: d-AP5 CHEMBL84612 (GtoPdb ligand 4168, ChEMBL id in `ligands.csv`); Ro 25-6981 CHEMBL305195 by structure (the SMILES is the 4-hydroxyphenyl, methyl, benzylpiperidine propanol; no name or synonym in ChEMBL or GtoPdb confirms it); the other six from the module (IT8 P3).

Routes: (i) existing: ChEMBL mechanism endpoint and the module's own adapter `chembl.query({"molecule": id})`, GtoPdb `interactions.csv` (release 2026.3.1), DGIdb `interactions.tsv`, Open Targets GraphQL mechanism; (ii) candidates: DrugCentral file, Pharos ligand-first and target-first, BindingDB compound-first and target-first, PDSP default table, PubChem assaysummary head, IUPHAR REST probe. Target-first for 4 function genes (GRIN2B, KCNQ2, CACNA1G, SLC12A2) in `target_first.tsv`.

Files: `trial_p6.py` (`--fetch` pulls and hashes; default rebuilds offline), `selectivity_p6.py`, `relations.tsv` (682 rows, source x compound x gene x action x value in nM x ref), `recovery.tsv`, `target_first.tsv`, `selectivity_same_document.tsv`, `comparison.tsv`, `licences.tsv`, `raw/fetch_log.tsv` and `raw/SHA256SUMS` (raw bodies are not committed: BindingDB licence unverified, ChEMBL/DrugCentral are share-alike copies; `--fetch` reproduces them), `pdsp_extract_summary.txt` (the 204 MB PDSP page stays in the scratchpad, SHA-256 91e390bb...d8e80d).

## 3. Measures (all counts from `recovery.tsv`, 23 pairs)

| Route | pairs recovered | with action type | with numeric potency |
|---|---|---|---|
| ChEMBL mechanism | 15 | 15 | 0 |
| ChEMBL activity (adapter) | 19 | 0 | 19 |
| GtoPdb file | 8 | 7 | 4 |
| DGIdb file | 17 | 13 | 0 |
| Open Targets mechanism | 15 | 15 | 0 |
| **existing path union** | **22** | **20** | **20** |
| DrugCentral | 8 | 8 | 7 |
| Pharos ligand-first | 8 | 7 | 7 |
| BindingDB compound-first (alias table by hand) | 12 | 0 | 12 |

Subset actually interrogated: 8 compounds, 23 pairs; ChEMBL activity rows fully retrieved (no truncation: 292, 21, 32, 28, 9, 27, 24, 84 rows). Not interrogated: any compound outside the set, any pair not declared (so false-positive rates for inclusion cannot be stated, only the off-declared-gene counts in `comparison.tsv`).

Target-first (function -> compounds), declared compounds found: GRIN2B 4 of 4 in ChEMBL (5,526 rows in 4 targets), 2 of 4 in BindingDB by exact SMILES string only (a lower bound), 1 in GtoPdb, 1 in DrugCentral, 0 in Pharos; KCNQ2 ezogabine found in ChEMBL, GtoPdb, DrugCentral; CACNA1G apinocaltamide in ChEMBL only, ethosuximide in ChEMBL (the rows count only if a numeric row exists: there is one, CACNA1I above 5,000,000 nM) and DrugCentral (action BLOCKER, no value); SLC12A2 bumetanide found in ChEMBL, GtoPdb, DrugCentral. So a function -> compound lookup with quantitative potency **already works from ChEMBL target-first for these channel and transporter targets**; what fails is gene-level reading of the answer (complex targets, placeholders).

Quantitative selectivity actually observable (`selectivity_same_document.tsv`, within one document; a ratio is not a selectivity claim across assays): Ro 25-6981 GluN2B 9 nM versus GluN2A 52,000 nM (document CHEMBL4308825, human, about 5,800 fold); apinocaltamide Cav3.1/3.2/3.3 6.4/18/7.5 nM versus Cav1.2 2,410 nM (document CHEMBL4177680, human); d-AP5 rat Ki GluN2A 390, 2B 2,800, 2C 5,900, 2D 21,000 nM (document CHEMBL4024770; the ordering is the one I expected); bumetanide SLC12A1 331 versus SLC12A2 2,512 nM (GtoPdb, one PMID, pIC50 6.48 versus 5.60; 7.6 fold). Ezogabine KCNQ2 EC50 ranges 150 to 11,200 nM across ChEMBL documents (75 fold), so one number would mislead. Ethosuximide has no usable T-type potency in any source (only a CACNA1I row "above 5,000,000 nM"), which agrees with IT8 Q07.

> **Grading added in IT15 (P2, 2026-11-01).** `selectivity_same_document.tsv` now carries a grade for each comparison and no longer shows a bare max/min. Re-read of the sentence above: the apinocaltamide human T-type against Cav1.2 comparison is LIMITED (same document, human recombinant, HEK293, FLIPR for all four, but the stimulus differs, calcium re-addition for Cav3.x and KCl for Cav1.2, and the origin is "unknown"; no ratio is offered), while the rat Cav3.x subtype spread in one format is INTERPRETABLE; the Ro 25-6981 GluN2B/GluN2A pair and the d-AP5 and bumetanide ratios are LIMITED (assay context for those documents was not retained, and ChEMBL answered HTTP 500 for Ro 25-6981 and ethosuximide on 2026-11-01); the ezogabine ranges mix homomers with the KCNQ2/KCNQ3 heteromer (LIMITED); Ro 25-6981 and radiprodil rows against the generic NMDA-receptor group are NOT_DETERMINABLE; the apinocaltamide document also holds CYP and hERG liability values, a panel and not a selectivity. See `../pharmacology_compare_it15_p2_20261101/README.md`.

## 4. Wrong or unverifiable links, and what a verifier should look at

1. **Memantine GluN1/GluN2A IC50 0.95 nM** appears in ChEMBL (assay CHEMBL2399396, document CHEMBL2396530, a 2013 paper on polymethylene tetraamines, two-electrode voltage clamp at -70 mV), and is copied into DrugCentral (pX 9.02) and Pharos (one origin, counted once; BindingDB shows the same 0.95). IT8 P3 found 840 nM at -60 mV in another document; a 1000 fold gap suggests a unit slip (micromolar curated as nanomolar), **but I did not read the paper: UNVERIFIED**, the activity carries no validity comment. This is the decisive datum for anyone ranking by potency: open the paper's table for memantine.
2. **Bumetanide selectivity across origins**: DrugCentral pairs SLC12A1 Ki 25 nM (WOMBAT-PK, not publicly checkable) with SLC12A2 IC50 2,512 nM (IUPHAR) = 100 fold; the same IUPHAR paper gives 7.6 fold. A cross-origin pair is not a selectivity.
3. **Pseudo-ratios from family-complex targets**: ChEMBL targets named "Glutamate [NMDA] receptor" carry genes GRIN1 to GRIN3B; ratios against `GRIN1|GRIN2B` rows in the same document are not subunit selectivities (visible in the radiprodil and Ro rows of the selectivity table).
4. **Placeholder targets**: 96 rows on `Unchecked` (d-AP5 and Ro 25-6981 among them) would be read as target data by a naive join.
5. **Action-label vocabulary**: memantine, a pore blocker, is curated as negative allosteric modulator; d-AP5 is "inhibitor" in DGIdb and "antagonist" in GtoPdb. The explanation of inclusion is observable in ChEMBL (document, assay), GtoPdb (PMID, action comment, species) and DrugCentral (ACT_SOURCE), not in DGIdb or Pharos.
6. Identity of BindingDB structures (14 of 22 rows differ in SMILES string from the ChEMBL canonical form) cannot be settled without a cheminformatics library; none installed.

## 5. Costs and limits

Fetch of everything: about 60 s of requests plus the target-first loop; ChEMBL calls stayed at HTTP 200 (a transient 404-like empty response occurred once on an unrelated lookup and succeeded on retry). Disk: DrugCentral 0.96 MB, BindingDB target payloads 0.2 to 0.7 MB each, PDSP 204 MB (not kept). Nothing installed; no key, e-mail or registration used; the PDSP query was a plain public GET whose parameters were ignored by the service.

Limits: 8 compounds on channels and transporters with strong ChEMBL curation: coverage here says little about compounds ChEMBL does not hold. Primary papers were not read (no depth beyond database fields). Recovery counts for BindingDB depend on my hand alias table. DGIdb is a 2024-06 export. Release ChEMBL_37 is the module record; the live version string is in `raw/chembl_act_*.json` (`source_version`). GtoPdb licence verified on the primary page; BindingDB, Pharos, PubChem licences not verified. Radar check: `scout_daily.json` ran 2026-10-31 05:20 UTC with verdict NO_USEFUL_CHANGE (all watched items UNCHANGED; the only changes logged were the SigCom-LINCS etag and openFDA NDC version, not pertinent here).

## 6. Edits this implies (not made)

- `framework/adapters/chembl.py` `_activities`: gene symbols, target_type, `non_gene_target` flag (section 1); test fixture in `test_repurposing_adapter.py`.
- Capability log (`capability_scout_log.md`), IT14 close: record "function -> compound lookup is not a source gap; DrugCentral file WATCH; Pharos, BindingDB REST, PDSP, PubChem bioassay DISCARD; memantine 0.95 nM row UNVERIFIED".
- `licence`: DrugCentral CC BY-SA 4.0 by link verified 2026-10-31; GtoPdb ODbL / CC BY-SA 4.0 verified 2026-10-31.
- Any potency ranking that uses ChEMBL memantine GluN2A should exclude document CHEMBL2396530 until the table is read.


> **Grading note, IT16 P1.1 (2026-11-01).** The grader now also asks which decisive conditions each assay description leaves unstated (holding voltage and agonist concentration for voltage-clamp work, the stimulus for flux assays, ATP concentration for enzyme assays) and limits the comparison that depends on them: "no difference found in the fields available" no longer reads as "conditions shown equivalent". The observation, the values and the ratio stay; the missing field is named in the `limits` column. A document marked `document_kind` review/compilation in the context table is also limited, because it is not one origin. Effect on committed tables: same-document table (40 rows) INTERPRETABLE 3 to 2; Q-A (1,037 groups) INTERPRETABLE 492 to 0 and LIMITED 153 to 645 (394 of the 645 lack the agonist concentration, 379 the holding voltage; descriptions rarely state them), NOT_DETERMINABLE 392 unchanged; Q-B unchanged (60 groups; the enzyme rule fires only where the technique word is present in the description, so ATP concentration is not yet checked there). The 492 earlier INTERPRETABLE labels meant only "compatible in the fields examined" and are superseded by this note; primary papers could lift individual groups.
