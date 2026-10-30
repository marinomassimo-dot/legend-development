# IT9 P4b-c: Q6 MYC / radial-glia group and controls (P3-10, 11, 12, 13, 16, 19, 20) plus the seed itself

Scientist-d3, 2026-10-30, task `ORCH-ROADMAP-IT9-20261030`, branch `task/it9-p4b-c`. Non-canonical research material; **not medical advice**; a database measure, a registry hit or a compatible network action is not a benefit. The reference genotype is a WWOX-DEE genotype class; no individual-level record is used. Criteria were committed first (`PRE_REGISTRATION.md`, commit edbeace9). No registry, ledger, current file, card or need was edited.

## 1. Decisions (first)

| Id | Compound | Role | Decision | Decisive datum or next step |
|---|---|---|---|---|
| P3-10 | harmine | Q6 mimics | **DROP** | MAO-A inhibited 16 fold more potently than DYRK1A in the same ChEMBL document (5 versus 80 nM): not a DYRK1A tool; mimics arm moves MYC with the disease direction; adult psychoactivity above 2.7 mg/kg |
| P3-11 | pomalidomide | Q6 mimics (as coded) | **DROP** | MYC sign **not derivable**: a molecular glue (IKZF1/3 neosubstrates), not a "CRL4 inhibitor"; the network holds IKZF1 -> MYC -1 and IKZF3 -> MYC +1; the CUL4A -> MYC record is a TRPC4AP ligase paper; boxed embryo-fetal toxicity; IKZF1/3 not in neural cells (adult atlas) |
| P3-12 | defosbarasertib | Q6 opposes | **DROP** | cytotoxic Aurora B inhibitor; AURKB not detected in adult brain nuclei, so it acts on cycling progenitors; edge is a T-ALL stability record; IV, no paediatric data |
| P3-13 | pinometostat | Q6 opposes | **DROP** | Dot1l deletion in mouse cortex reduces progenitors and upper-layer neurons (the readouts already low in WWOX-KO organoids); edge is a breast-cancer co-binding record; IV only, no CNS data |
| P3-16 | sirolimus | reference | **REFERENCE-ONLY** | seed/edge answer: no Q6 row; FKBP1A has no edges; no signed MTOR -> MYC edge; card EB-MTOR-AX-01 unchanged |
| P3-19 | lenalidomide | artefact control | **REFERENCE-ONLY, artefact CONFIRMED** | same mislabelled mechanism and wrong-receptor edge as pomalidomide |
| P3-20 | AT9283 | artefact control | **REFERENCE-ONLY, artefact CONFIRMED** | 93 human targets with a value of 1 micromolar or less (pre-registered threshold: more than 5) |

**Seed verdict: WEAK-DIRECTION-ONLY for candidate generation** (`seed_assessment_Q6_MYC.md`). Direction (MYC higher in WWOX-deficient radial glia) is supported in KO, SCAR12 and WOREE organoids at transcript and protein level; valence is not established, the one causal test (A51) is a multi-kinase inhibitor, the single-cell contrast is one library per genotype, and the paper is single-laboratory. Next experiment is at the seed, not at a compound: a MYC-specific graded lever with falsifier stated there.

Distinction asked for: "insufficient support" versus "no activity". Nothing here shows that any compound has no activity in a WWOX system; **no compound-response measurement exists in a WWOX system**, and none was sought in the sense of a bench result. The four DROP decisions rest on target action, direction compatibility with the seed paper, edge provenance, exposure and safety, not on a measured null.

Biological promise (given only the WWOX-seed link and target action), evidence depth, feasibility and next-experiment priority are separate columns in `qualification_Q6_group.tsv` and in each record.

## 2. Denominators and states

* ChEMBL: 7 molecules; **4,292 activity rows** retrieved (types IC50, Ki, Kd, EC50, DC50, Dmax, Potency, Inhibition; cap 3,000 per molecule, not reached; state ROWS_RETRIEVED for all), 1,717 target-by-type-by-assay groups; 9 curated mechanism rows (none for harmine, defosbarasertib and pinometostat: "none curated" is an absent datum, not a negative).
* Service log: 232 attempts in the final run, **0 non-200 except two 404 answers** (PubChem has no record for the ChEMBL pinometostat key, which is an answer, not an error). Not reached: SIGNOR web site (no HTTP answer on 2026-10-30), Ensembl REST (no answer; replaced by the Human Protein Atlas gene search). An earlier run was stopped after Ensembl retries stalled it; its data were not used.
* ClinicalTrials.gov API v2: 49 slices (7 compounds x 7), dated 2026-10-30; `trials_summary.tsv`; a zero is "no hits for the query string on that date". The sirolimus counts include everolimus records matched through the class.
* openFDA labels: pomalidomide (11 labels in the index, 10 fetched), lenalidomide (17, 10), sirolimus (21, 10); the label with the most sections was used; **sections fetched are not the whole label**. FAERS seizure-term report counts are reports, not incidence.
* Literature: Europe PMC searches (`literature_search_log.tsv`, 30 searches) and 36 abstracts fetched (`literature_abstracts.jsonl`). **All literature claims are abstract-level** unless stated. One paper was read at partial full-text depth: the seed paper (below).
* Human Protein Atlas: 22 genes, adult brain single-nuclei and region data only.

## 3. UNVERIFIED and not done

* Identity: all seven are now VERIFIED by structure; pinometostat with a stereo-specification difference at the cyclobutane ring between ChEMBL and PubChem.
* Seed paper: Supplementary material not read and not held (hESC organoid replicate, 2D NSC blots, A51 experiment, MYC ChIP-seq); published Methods are in the supplement; the one-library-per-condition fact is from the preprint methods as recorded in `census_reconciliation_it7_20261029.md`; Fig 3K y axis exceeds 100 percent (unreconciled); the Fig 3K and 3L percentages are read off the plots (approximate).
* The CUL4A -> MYC SIGNOR record: abstract says TRPC4AP, not CRBN; the SIGNOR entry itself could not be opened; whether the full text supports a CRBN attribution is UNVERIFIED.
* Human CSF or brain concentrations: not retrieved for any compound; harmine pharmacokinetics beyond the phase 1 abstract; paediatric pinometostat results; fetal-stage expression of DYRK1A, AURKB, DOT1L, IKZF1/3 in radial glia (the atlas is adult).
* MAO-A interaction risk, Aurora B and mitotic microcephaly, the mTORC1-to-MYC translational rationale, and the prodrug relation of AZD1152: general knowledge, not fetched.
* Not done: kinome-wide selectivity from a primary screen paper (ChEMBL panels only); GtoPdb or DGIdb fresh calls; trials results (only registry metadata); any bench work.
* Disclosure: while testing access to the seed paper's open-access status, one Unpaywall query carried a placeholder address at example.org (not an operator address, not an e-mail of anyone); the answer was not used. No other e-mail or identity was sent.

## 4. Seed paper read receipt

`disease-models/wwox/research/receipt_staging/scientist-d3/FTR-20261030-42397075-08.json`, evidence depth `partial_fulltext_read` (supplementary not read), source `files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf`, fingerprint 9775f766..., validated with `staged_receipt_check.py --artifact-root /home/desktop/legend-development --check-doi` (OK). Next free sequence number was 08 (existing 01 to 07 across dates).

## 5. For the batch path (nothing edited here)

1. Record the receipt above, in event order, after the usual trial.
2. Catalogue coding limit (add to the P3 item 4): ChEMBL codes cereblon modulators as "CRL4(CRBN) inhibitor"; a "molecular glue / degrader" action type is missing, so every IMiD-class proposal gets a wrong sign; and complex-level SIGNOR edges (CRBN_CUL4A_DDB1_RBX1) are split to members and attributed to CUL4A alone.
3. Edge-provenance note for the network: the four Q6 MYC edges (DYRK1A, AURKB, DOT1L, CUL4A) are single-record, cancer-line, protein-stability or co-binding records; DOT1L -> MYC is coded +1 from a "binding" record.
4. Discovery-ledger note: Q6 seed verdict WEAK-DIRECTION-ONLY; the MYC valence is the open question; one library per genotype in the single-cell data.
5. Card EB-MTOR-AX-01: `label_lookup` is `NOT_ATTEMPTED`; this folder holds the sirolimus label sections and trial counts (no card edit made).
6. Research-material pointer to this folder; no registry, need or current-file change proposed.

## 6. Files

`candidates/` (7 records, items 1 to 8 each), `qualification_Q6_group.tsv` (7 rows x 21 columns), `seed_assessment_Q6_MYC.md`, `PRE_REGISTRATION.md`, tables `identity.tsv`, `chembl_mechanism.tsv`, `measures_by_target_type.tsv`, `measures_detail.tsv`, `trials_summary.tsv`, `trials_nervous_system_detail.tsv`, `labels_sections.tsv`, `edge_records_omnipath.tsv`, `expression_hpa_summary.tsv`, `expression_hpa_raw.tsv`, `faers_seizure_counts.tsv`, `literature_*`, `service_log.tsv`, `faers_service_log.tsv`, `raw_hashes.tsv`, `run_summary.json`, `collected.json.gz` (label sections cut at 12,000 characters; the raw store, 5.7 MB, is not kept: hashes are in `raw_hashes.tsv`). Scripts: `qualify_p4b_c.py` (`run`, offline `rebuild`), `lit_p4b_c.py`, `faers_p4b_c.py`; all take `--help` and the network ones need no key.
