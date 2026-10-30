# IT9 P4b group A: Q2 metabolism/glycolysis proposals and the PDK reference (P3-01, P3-02, P3-03, P3-04, P3-14, P3-15)

Scientist-a3, 2026-10-30, task `ORCH-ROADMAP-IT9-20261030`, branch `task/it9-p4b-a`. Non-canonical research material. **Not medical advice; no dose, route, schedule or individual recommendation. A database or enzyme measure is not therapeutic benefit; a compatible action of a context-free signed network is not a predicted benefit.** Reference genotype: a WWOX-DEE genotype class; no individual-level record. No registration, contact, spend or access step was taken; no e-mail address or operator identity was sent to any service. Edits no registry, ledger, current file, card, need or earlier cycle folder.

## 1. Decisions (first)

| Cand | Compound | Decision | Decisive datum | Promise | Depth | Feasibility | Priority |
|---|---|---|---|---|---|---|---|
| P3-01 | balsalazide | **DROP** (insufficient support, not "inactive") | PPARG belongs to the metabolite mesalamine: 0 of 678 balsalazide rows and 0 of 428 mesalamine rows are on PPARG; the cited primary work activates PPARG at 30 mM, label 5-ASA Cmax is about 1.4 uM (ratio about 2e4) | LOW | MEDIUM | LOW | none |
| P3-02 | ramelteon | **DROP** (insufficient support; potent at MT1/MT2, Ki 0.014-0.112 nM) | the 3-edge chain comes from a coupling assay, a GNAO1-overexpression result in glioma stem-like cells and a Hes1-null skin transcriptome: no record measures receptor activation then a BNIP3 change; MTNR1A and MTNR1B are about 0 CPM in 6 organoid libraries | LOW | MEDIUM | HIGH to run, no target in the system | none |
| P3-03 | belzutifan | **INCONCLUSIVE** (go/no-go experiment defined) | missing: HIF-2alpha protein in WWOX-deficient neural cells and its causal share in LDHA/SLC2A1; adult brain EPAS1 is vascular (HPA); mouse cortical HIF-2alpha knockout has no developmental phenotype | LOW-MEDIUM | MEDIUM | MEDIUM-HIGH in vitro | MEDIUM-LOW |
| P3-04 | ceperognastat | **DROP** of the generated proposal (identity now verified by structure) | the only edge OGA->PFKP is a protein-activity record (O-GlcNAc on PFK1 inhibits the enzyme, A549 cancer cells) applied to a PFKP transcript seed (organoid ratio 1.00); OGA has 4 outgoing edges, all O-GlcNAc-on-enzyme; plus phase 2 and synaptic counter-evidence | LOW | MEDIUM | LOW | none |
| P3-14 | AR-12 | **REFERENCE-ONLY** (confirmed PDPK1; not a PDH-kinase hit) | target CHEMBL2534 = UniProt O15530 = HGNC:8816 PDPK1 (alias symbol PDK1); the PDH kinase is HGNC:8809 / Q15118; 0 of 110 complete rows are on any PDH kinase; PDPK1 IC50 5,000 nM (two documents) | n/a | MEDIUM | n/a | none |
| P3-15 | dichloroacetate | **REFERENCE-ONLY** (edge/valence question added) | PDK1 is both seed and target; the seed direction is uncertain and opposite across systems (lower in sign in organoid 0.78 and hNPC; higher in neurons d14 and in non-neural fibroblasts), so the compound's engine action flips; the engine output adds nothing beyond the seed | n/a | HIGH (existing) | n/a | unchanged |

Counts: 6 of 6 assigned; DROP 3, INCONCLUSIVE 1, REFERENCE-ONLY 2, KEEP-AS-PROPOSAL 0. Positive result: none of the four proposals survives as a WWOX-derived lever. Negative results are all "insufficient support" findings about the proposal chain or the compound-to-target step; **none is a finding that a compound is inactive**.

What carries over to the other Q2 proposals: (a) **the network record type matters**: two of four failures are mode mismatches (a protein-activity or coupling record, not a transcript effect, applied to a transcript seed); (b) **a symbol is not an identity** (PDK1); (c) **a target can belong to the metabolite** (balsalazide).

## 2. Files

`qualification_q2_metabolism.tsv` (rectangular; 6 rows x 23 columns; scores kept separate, no sum), `records/P3-xx_*.md` (items 1-8 per candidate), `edge_provenance_judged.tsv` (my judgement per edge/chain, with references and contexts) and `edge_provenance_live.tsv` (OmniPath records fetched live), `chembl_row_counts.tsv`, `chembl_rows_selected.tsv` (rows on the declared targets with assay type, organism, relation, units, document; `NO_ROWS_FOR_THIS_TARGET` where none), `hpa_adult_expression.tsv`, `organoid_target_gene_rows.tsv` and `hnpc_target_gene_rows.tsv` (local datasets, descriptive), `trials_registry_search.tsv` (every query: terms, date, hits), `faers_counts.tsv`, `DECISION_RULES.md` (committed before any outcome was read), scripts `qualify_p4b_a.py` (live `run` and `supp`), `build_tables_p4b_a.py` (offline, deterministic), `target_gene_rows_p4b_a.py`, `adhoc_lookup.py` (logged Europe PMC lookups), `test_qualify_p4b_a.py`, `collected*.json.gz`, `raw_store*.json.gz`, `raw_hashes.tsv`, `service_log.tsv`, `service_log_supp.tsv`, `adhoc_log.tsv`.

## 3. Denominators (units stated)

* ChEMBL molecule-first activity pulls, each complete (total_count equals rows retrieved): balsalazide 678, mesalamine 428, ramelteon 334, belzutifan 238, ceperognastat 1, AR-12 110, sodium dichloroacetate 97, dichloroacetic acid 124 rows. Curated mechanism rows: 0, 3, 1, 1, 0, 1, 1, 0.
* Rows on the declared main targets: balsalazide PPARG 0 (and mesalamine PPARG 0); ramelteon MT1/MT2 6 rows over 2 documents; belzutifan EPAS1 10 rows over 3 documents (several measure types); ceperognastat OGA 1; AR-12 PDPK1 2, PDH kinases 0.
* ClinicalTrials.gov v2, 2026-10-30: 88 query rows in `trials_registry_search.tsv` (compound term x any condition, plus 7 condition terms); hits in the neurological and neurodevelopmental conditions: 0 for balsalazide, ramelteon, belzutifan, ceperognastat; 0 genuine for AR-12 (the one hit is a Holter monitor model); dichloroacetate 1 (MELAS) and 2 (PDH complex deficiency).
* openFDA spontaneous reports (counts, not rates; the count endpoint needs a key that is obtained with a contact address, so it was not used; terms were counted one by one): balsalazide 505 reports, ramelteon 7,349, belzutifan 618 (matched through a different field).
* Expression: HPA JSON for 21 gene symbols, 20 resolved (MGEA5 is not an HPA symbol; OGA resolved); organoid GSE156243 (4 KO, 2 WT libraries) and hNPC GSE126075 (one library per arm, CAGE): 21 genes each, 8 absent from the hNPC table.
* Edges: 14 OmniPath edge queries (two queries each), 25 matching record rows (the rest are NO_MATCHING_RECORD).
* Service layer: first run 310 attempts (302 HTTP 200, 5 HTTP 404 answers, 3 HTTP 403: the openFDA count endpoint without a key; not retried, not worked around); last `supp` run 32 attempts (20 HTTP 200, 12 HTTP 404 = zero matching reports). `supp` was run four times while its content was extended; only the last log is kept, as in P4a. No transport error occurred. An unrelated 404 (PubChem exact-key lookup for the stereo-qualified balsalazide key) is an answer, not an error. Moving services: counts may differ at re-query.

## 4. Pre-registration and honesty notes

* `DECISION_RULES.md` was committed (commit before this folder's outcomes were opened) after I had seen the P3 selection tables, which carry a general-knowledge feasibility judgment ("likely drop") for balsalazide; that is disclosed and was not used as evidence.
* Rule 2 (record mode versus seed level) decided P3-04 and, together with the absent target, P3-02. Rule 4 (target shown in a neural cell type) decided P3-03 into INCONCLUSIVE; belzutifan would have been KEEP-AS-PROPOSAL under a looser reading (organoid bulk shows low EPAS1), which I did not adopt.
* Reading depth: passage-level full text for Rao 2015 (PMC4598839, the OGA->PFKP reference) and Rousseaux 2005 (PMC2213148); the DailyMed belzutifan label (SPL XML) and the openFDA balsalazide and ramelteon labels were searched and read in the relevant sections; every other paper only at abstract level (Europe PMC). **No complete full-text read was done, so no read receipt was staged** (the protocol states that reading selected passages is not a complete read).

## 5. UNVERIFIED (consolidated)

PPARG potency of 5-ASA beyond one paper and the brain/CSF concentration of 5-ASA, ramelteon and belzutifan in children; which cell line the coupling record (Cell 2019) used; full texts of the GNAO1, HES1->BNIP3, and Science 2012 PFK1 papers; HIF-1alpha selectivity row for belzutifan; EPAS1, MTNR1A/B and OGA protein in any WWOX-deficient neural system; research-use availability of belzutifan, ceperognastat and AR-12; ceperognastat programme status after the 2026 reports; the WHO INN structure for ceperognastat; whether AR-12 touches PDH kinases (no measurement exists, absent data); PDK1 protein or activity in any WWOX-deficient neural system; human plasma Cmax of dichloroacetate (UNKNOWN since IT8 P3); the content of the 102 references behind HIF1A->PDK1. ChEMBL transcription of cited documents (none opened) is UNVERIFIED throughout.

## 6. Items for the batch path (no registry or file outside this folder was edited)

1. P3 candidate statuses for the Orchestrator's integration: P3-01 DROP, P3-02 DROP, P3-03 INCONCLUSIVE (go/no-go defined), P3-04 DROP (identity upgraded from name-matched to verified by structure), P3-14 REFERENCE-ONLY (PDPK1 confirmed), P3-15 REFERENCE-ONLY.
2. Hand-over to the seed-engine owners (not an edit): (a) filter or label network edges by record type (transcriptional versus post-translational/coupling) before applying them to a transcript seed; (b) resolve catalogue targets to seeds by HGNC id, not by text (PDPK1 versus PDK1); (c) credit a prodrug's target only through the active moiety record and say so.
3. Read receipts: none staged. Claim-registry notes: none proposed (nothing here changes a consolidated baseline claim).
4. Possible follow-up not started: the belzutifan go/no-go measurement, if the Orchestrator wants a HIF-2alpha-dependence readout on the existing WWOX-deficient datasets before any bench work (EPAS1 is 1.2-9.1 CPM in the organoid; a protein measure does not exist).

## 7. Checks run before the commit

See the final report of the delegate for the exact results (public release gate, release-surface, documented-commands, structured-data integrity, closed-world assertions, this folder's offline test).
