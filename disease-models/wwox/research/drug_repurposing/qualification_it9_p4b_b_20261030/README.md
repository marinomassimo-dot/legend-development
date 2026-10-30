# IT9 P4b group B: qualification of P3-05, P3-06, P3-07, P3-08, P3-09, P3-17, P3-18

Scientist-b3, task `ORCH-ROADMAP-IT9-20261030`, branch `task/it9-p4b-b`, 2026-10-30. Non-canonical research material. **Not medical advice; no dose or individual recommendation. A compatible action of a context-free signed network is not a benefit; a database or enzyme measure is not therapeutic effect.** The reference genotype is a WWOX-DEE genotype class; no individual-level record, no e-mail or operator identity was sent to any service. No registry, ledger, card, need or current file is edited.

## 1. Decisions (first)

| ID | Compound | Decision | Decisive datum |
|---|---|---|---|
| P3-05 | fosfestrol | **DROP** (compound); edge kept only as a question for selective ligands | active species DES is not ER-beta-selective (same-document ratios 0.7 to 1.5, five documents); the prodrug record has no ER measure; no label, CNS or paediatric data |
| P3-06 | implitapide | **DROP** | P4HB is the PDI subunit of the MTP complex (target CHEMBL2364681 = MTTP + P4HB): a complex-to-subunit mapping artefact; 0 activity rows; terminal edge XBP1->GAD1 cites a polymorphism association study |
| P3-07 | curcumin | **DROP** | PAINS/IMPS, unstable, non-bioavailable (J Med Chem review, abstract); 124 targets with type-B potency rows; EP300 micromolar and document-inconsistent |
| P3-08 | belnacasan | **KEEP-AS-PROPOSAL**, gated, low priority; reference for J01 | active acid VRT-043198 is a separate record: caspase-1 Ki 0.8 nM, PBMC IL-1beta release IC50 470 nM; mouse anticonvulsant reports; **but the edge is protein cleavage while the seed is a transcript** |
| P3-09 | JTE-151 | **INCONCLUSIVE** (insufficient support, not no activity) | 0 ChEMBL activity rows, no structure key, no registry record; missing: RORgamma values, CNS exposure, Rorc in Wwox-null microglia |
| P3-17 | felbamate | **REFERENCE-ONLY** | boxed warning: aplastic anaemia and hepatic failure; paediatric use established only for Lennox-Gastaut syndrome |
| P3-18 | memantine | **REFERENCE-ONLY** | no network edge (hop-0 symbol overlap on GRIN2C); IT8 P3 qualification reused |

Counts: 7 candidates; DROP 3, KEEP-AS-PROPOSAL 1, INCONCLUSIVE 1, REFERENCE-ONLY 2. The four fields promise / depth / feasibility / priority are separate columns in `qualification_b.tsv`.

**What the group shows about the engine (descriptive).** Of the five seed-specific proposals here, two fail on target mapping or compound class (P3-06, P3-07), one on selectivity of the active species (P3-05), one is level-mismatched (P3-08) and one is unsupported by data (P3-09). The edges were not equal: CASP1->IL1B (SIGNOR, 1991), ESR2->GAD2 (one neural reporter paper), RORC->IL6 (a microglia paper) have neural-relevant or curated sources; XBP1->GAD1 has none; P4HB->ERN1 concerns a different action than the drug's. n = 5 proposals: no rate is derived.

## 2. Files

`qualify_p4b_b.py` (live `run`, offline `rebuild`, `--help` safe), `tables_p4b_b.py` (deterministic derivation), `DECISION_CRITERIA.md` (written before any row was read), `qualification_b.tsv` (8 lines, 14 columns), `records/P3-0x_*.md` and `records/P3-1x_*.md` (items 1 to 8 per candidate), `measures_kept.tsv` (ChEMBL rows kept by assay type, species, relation, units), `edges_omnipath.tsv`, `expression_hpa.tsv`, `trials_ctgov.tsv`, `labels_openfda.tsv`, `identity_chembl.tsv`, `identity_pubchem.tsv`, `service_log.tsv`, `raw_hashes.tsv`, `raw_store.json.gz` (raw responses, 300 KB).

## 3. Denominators and service handling

* ChEMBL activity rows retrieved (molecule-first, all types, not truncated): fosfestrol 26 (+ DES CHEMBL411: 62 ER rows kept of 1,273 total), implitapide 0, curcumin 3,657 + 7, belnacasan 15 (+ acid CHEMBL4802237: 2), JTE-151 0, felbamate 300 + 10, memantine 546 + 56 + 5. 
* Service log: 191 attempts, 4 non-200, all HTTP 404 from openFDA meaning "no matching label" (a service answer, treated as absent data, not an error); no 5xx or transport failure. Retry layer from IT8 P3 (0, 2, 6, 15, 30 s). Hashes in `raw_hashes.tsv`. The script was run twice (the first run, 117 attempts, lacked the related-molecule and target steps and was overwritten).
* OmniPath edge records: 9 edge lookups, 9 with at least one record; HPA gene JSONs: 17 of 17 HTTP 200. HPA lists only the enriched cell types: an empty list means "not enriched", not "not expressed". HPA is adult tissue: **developmental-age expression was not checked for any gene (UNVERIFIED for all)**.
* ClinicalTrials.gov v2, 2026-10-30, queries `query.intr=<name>` alone and with `query.cond=(epilepsy OR seizure OR "developmental and epileptic encephalopathy" OR hypomyelination OR "neurodevelopmental disorder" OR leukodystrophy)`; returned counts and NCT ids in `trials_ctgov.tsv`. Name matching is loose (3 irrelevant hits for fosfestrol). No trial result was read.
* Literature: PubMed/E-utilities and the MCP PubMed tool; **all papers were read at abstract level only (PMIDs 21431948, 42216646, 28074653, 19587286, 37419402, 38170624 and 39675971 abstract/metadata; titles only for 32149426, 18335162, 20427770, 1919001, 19103749, 25525796, and for the implitapide and curcumin reference lists). No full text was opened, so no read receipt is staged.**

## 4. UNVERIFIED

Developmental expression of every gene; whether ChEMBL transcribed each cited document correctly (none opened); DES in-utero and thrombotic hazards and fosfestrol-to-DES conversion (general pharmacology, not retrieved); ER-beta binding to the endogenous gad2 locus; the termination reason of NCT01501383; brain concentration of VRT-043198; caspase selectivity of the acid; the ChEMBL JTE-151 record-to-structure link; research availability of every compound (no source states it); numerical RORgamma potencies of JTE-151; the felbamate GluN2C measure (UNKNOWN, no row); a specific seizure sentence in the memantine label; the 0.95 nM memantine GluN2A outlier row; Japanese trial registries for JTE-151.

## 5. Items for the batch path (nothing edited here)

1. Claim/registry candidates: (a) the implitapide->P4HB link is a complex-member artefact (ChEMBL complex CHEMBL2364681) - a catalogue note that complex targets split into members inherit the drug's sign for the non-catalytic partner; (b) belnacasan's ChEMBL record carries no caspase-1 potency, the active acid is CHEMBL4802237 (Ki 0.8 nM) - an identity note for card J01's catalogue compounds; (c) DES is not ER-beta-selective; (d) felbamate boxed-warning figures from the label of 2026-07-14.
2. No read receipt to record (no full text read).
3. Card J01 (abstention) could add, in its next-measurement text, the level-mismatch gate for the CASP1/IL1B edge; not edited here.
