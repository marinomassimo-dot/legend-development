# Independent verification of P3B-1 (TxGNN and Every Cure MATRIX), scientist-d

Verifier: scientist-c (did not produce the package). Object: merge e1ac941e, note
`disease-models/wwox/research/drug_repurposing/p3b1/txgnn_matrix_outcomes_20261026.md` (claims in its section 4).
Non-canonical quality check; nothing here is efficacy evidence or medical advice. Depth: database, API and repository
metadata only, never a paper full text (no receipt). Checked on 2026-10-26/27 against live primary sources, single polite
calls, no account, no e-mail. No per-drug MATRIX score is reproduced here: the scores were read into scratch only and deleted.

Verdict vocabulary: SUPPORTED / OVERSHOOT / WRONG_SOURCE / UNVERIFIABLE. Each non-SUPPORTED item says whether it is an
error (the note states something false) or an uncertainty (the check cannot decide).

## Summary

Seven of the eight claims are SUPPORTED as stated. Two small defects, neither touching a conclusion: claim 7 names issue 17
as reporting an explorer mismatch (it does not: OVERSHOOT, error) and claim 4 names the wrong file as the place where the
grouped-disease membership was read (WRONG_SOURCE for the file name, facts correct, error). One item cannot be reproduced
as worded: the explorer status (claim 6, UNVERIFIABLE, uncertainty). Both outcome labels follow from the evidence.

## Claim by claim

| # | Claim | Verdict | What was checked |
|---|---|---|---|
| 1 | `matrix-scores` has no licence | SUPPORTED | HF API for the dataset (commit d6b121bf38112cf28e7c813d0a062651757c52a1, last modified 2026-07-01): `cardData` has only `dataset_info` and `configs`, no `license` key, no `license:` tag; the tree is `.gitattributes`, `README.md` and 11 parquet shards (no LICENSE); the raw card text has no occurrence of "licen", "CC BY", "Apache" or "terms". The docs source page `docs/src/releases/public_data_releases.md` (live page HTTP 200) lists four datasets (kg-nodes, kg-edges, drug-list, disease-list) and its Licensing section speaks of "the public datasets" as CC BY 4.0. `matrix-scores` is not in that table. Limit (uncertainty, not error): absence of a declared licence is what was shown; whether Every Cure intends the table to be public-licensed is not decidable from these sources, which is the note's own stance. A code search of the GitHub repository for the dataset name needs authentication and was not possible. |
| 2 | drug and disease lists CC BY 4.0; code Apache-2.0; kg-nodes/edges pass-through | SUPPORTED | HF API: drug-list (commit dc75f850...) and disease-list (commit c302a048...) `license: cc-by-4.0`; kg-nodes and kg-edges `license: other`, each with `LICENSE.md` (kg-edges also `LICENSE`); GitHub licence API for `everycure-org/matrix`: Apache-2.0. Row counts read from the parquet: 1 935 drugs, 23 224 diseases. |
| 3 | PrimeKG `kg.csv` md5 aac8191d...; CC0 on the record; README disclaims dataset licence | SUPPORTED | Dataverse record (DOI suffix IXA7BM, version 2.1) lists `kg.csv` md5 `aac8191d4fbc5bf09cdf8c3c78b4e75f`, size 981 751 236; the file downloaded here hashes to the same md5 and size; licence field CC0 1.0. The PrimeKG README "License" paragraph says the MIT licence "is distinct from any licenses governing the PrimeKG dataset itself". The file TxGNN's `TxData.py` downloads (datafile 7144484, a different Dataverse record) reports the same md5 and size. |
| 4 | MONDO 14533 / 13687 are members of grouped nodes 28005 / 27803; no WOREE node; WWOX 0 `drug_protein` rows | SUPPORTED (facts); WRONG_SOURCE (file name) | In `kg.csv`: node 28005 = "developmental and epileptic encephalopathy" (87 member ids, 14533 present, 13687 absent), node 27803 = "autosomal recessive spinocerebellar ataxia" (18 ids, 13687 present, 14533 absent); WWOX is node 602 (NCBI 51741) with 740 rows as either endpoint and 0 rows of relation `drug_protein`; the string "woree" is absent from `nodes.tab` and from the grouped-disease table. Error to correct: the note (claim 4 and section 1.3) cites `kg_grouped_diseases.csv` "of the TxGNN commit". At commit 0e0203c3939f that file does not exist (no such file in the root or in `data/`, which holds only `disease_files`); the real source is the Dataverse PrimeKG file `kg_grouped_diseases.tab`, which I read and which lists 14533 and 13687 with their group names. The conclusion is unaffected. |
| 5 | Five-node extract: flags, Spearman 0.79-0.84, top-50 overlap 29-32, baseline median 8 | SUPPORTED | Re-extracted from the 11 shards at the named commit: the SHA-256 of all 11 shards equals the 11 digests in the committed summary; the committed `matrix_scores_from_shards.py` and `matrix_trial_summary.py` rerun on them reproduce the committed aggregates exactly (flag counts, all pairwise values, baseline). Independent recomputation of Spearman with SciPy and of the top-50 sets (no tie at rank 50) agrees: DEE28 vs DEE1 0.8424 / 30, vs genetic-DEE parent 0.8306 / 32, vs SCAR12 0.8160 / 29, vs undetermined EOEE 0.7937 / 29. Each of the five nodes has 1 748 rows; the four named nodes have 0 in all of `is_known_positive`, `is_known_negative`, the four trial flags, `off_label` and the three `ec_indications_list*` columns; the parent has `off_label` = 6. Whole table: 24 371 target nodes, 25 046 known-positive and 38 408 known-negative pairs (duckdb over the shards). Baseline for DEE28: rho min/median/max 0.127 / 0.658 / 0.810, top-50 overlap 0 / 8 / 26, 86 nodes compared. Note on wording (not an error): the script draws 100 nodes by hash and keeps those sharing at least 1 000 drugs, so "86" is the retained count; the 100 draw is stated only in the script. MONDO ids of all five nodes exist in `disease-list` (names: DEE28, AR spinocerebellar ataxia 12, undetermined early-onset EE, DEE1, genetic DEE). |
| 6 | TxGNN: last commit 2024-05-06; sdist failure; no cp312 DGL wheel; 55 checkpoints, no `full_graph`; explorer 503 | SUPPORTED except the explorer | GitHub: head `0e0203c3939f`, 2024-05-06T20:52:40Z, "add reproduce info", repo `pushed_at` the same minute, MIT, 22 open issues. PyPI TxGNN 0.0.3 is sdist-only; its `setup.py` reads `requirements.txt` and the archive contains no `requirements.txt` (the build failure follows; I did not run the build). PyPI DGL 0.5.2 files exist only for cp36, cp37, cp38 (macOS, manylinux, Windows). Checkpoint zip from the reproduce README (208 526 110 bytes, about 199 MiB, reachable without login): central directory read by range request, 166 entries, 55 checkpoint directories = 11 splits (adrenal_gland, anemia, autoimmune, cardiovascular, cell_proliferation, complex_disease, diabetes, mental_health, metabolic_disorder, neurodigenerative, random) x 5 seeds, none named `full_graph`. The README separately links a different example-weights file (datafile id 1fxTFk...) that the note does not mention and I did not open: a gap in the note's "one zip" wording, not shown to change the finding. Explorer: UNVERIFIABLE as worded (uncertainty). One fresh attempt at txgnn.org returned no HTTP response at all (curl status 000, connection or timeout), not a 503; both are consistent with the site being offline, and the note itself flags that the state may change. I did not retry. The disease-area test lists contain neither group node (searched all nine files for 28005, 27803 and the group names; only "infantile onset" and "GRID2-related" ataxias appear), supporting section 1.3. |
| 7 | Issues 29, 25, 23, 18, 17, 31 as of now | SUPPORTED for 29, 25, 23, 18, 31; OVERSHOOT (error) for 17 | All six are still open. 29 (2026-04-02): released checkpoints give mean AUPRC 0.032 over five areas x five seeds versus 0.437 published; one reply (2026-07-15) speculates the paper's metric pairs each positive with one random negative and says the replier did not replicate TxGNN, matching the note's "speculation, unverified". 25 (2025-05-26): AUPRC 0.1-0.2 lower with the provided weights on `complex_disease`; one later "same problem" comment. 23 (2025-04-24): evaluation right after training differs from evaluation after save and reload. 18 (2024-11-08): ranked-list output differs from the explorer; the author adds "problem solved ... set split to full_graph", and a 2025-03-13 commenter says full_graph still does not match the explorer. 31 (2026-07-09): asks whether fine-tuned weights are available, 0 comments. Error: issue 17 is a question about obtaining zero-shot embeddings and says nothing about explorer output, so "issues 18 and 17 report output that does not match the explorer" should read "issue 18". Also, the note omits that the author of 18 reported the full_graph advice as solving his problem, which the same note relies on for the full_graph point; the later comment keeps the discrepancy open. Neither changes the outcome. |
| 8 | EC KG `NCBIGene:27102` labelled STK33 with EIF2AK1 identifiers | SUPPORTED | `kg-nodes` shards (commit c9c60b2c..., 7 354 612 rows): id `NCBIGene:27102`, name "STK33 protein, human", with HGNC:24921, UniProtKB:Q9BQI3, ENSEMBL:ENSG00000086232, OMIM:613635. UniProt Q9BQI3 is E2AK1_HUMAN (gene EIF2AK1, GeneID 27102); NCBI Gene 27102 is EIF2AK1; HGNC:24921 is EIF2AK1 (Ensembl ENSG00000086232). Real STK33 nodes exist separately (for example NCBIGene:65975). WWOX `NCBIGene:51741`, DEE28, SCAR12 and undetermined EOEE nodes are present. |

Section 2.4 spot check (drug-list presence, identifier level): present are sodium and glycerol phenylbutyrate, ursodeoxycholic
acid, TUDCA (listed as "Tudca"), bortezomib, stiripentol, vigabatrin, cannabidiol, valproic acid, fenfluramine, ganaxolone,
arimoclomol, metformin, nicotinamide, alpha-lipoic acid, beta-hydroxybutyrate (not "ketone esters": a naming gap, trivial),
trazodone, guanabenz, fasudil (`approved_usa` = NOT_APPROVED). Absent by name and synonym: dichloroacetate, amlexanox, ISRIB,
salubrinal. SUPPORTED.

## Do the outcome labels follow?

- TxGNN REASONED WAIT: follows. Verified: no `full_graph` checkpoint, no prediction table in the repository, explorer not
  reachable now, a legacy stack that PyPI cannot supply for this interpreter, the target diseases only inside 87- and 18-member
  groups, and a public reproduction failure that is unanswered. A wait with named reopening conditions is proportionate;
  "exclusion" would have been an overshoot and the note does not claim it. The only soft point is that the reproduction
  numbers are third-party and unreplicated (the note says so).
- MATRIX INCONCLUSIVE TRIAL, scores table only: follows. The licence is undeclared (claim 1), the WOREE node is scored but
  unlabelled (flags all zero), and the specificity result is consistent with a neighbourhood prior. One reading limit the
  note already states and I confirm: the sibling rho values (0.79-0.84) are not above the unrelated-node maximum (0.81), so
  only the top-50 overlap (29-32 against a maximum of 26) separates siblings from the baseline, and the baseline is a
  convenience sample, not a null.
- No MATRIX score as probability of efficacy or as independent confirmation: confirmed. The note's text and the committed
  summary hold only counts and agreement statistics (the JSON has no drug names or per-drug values). The dataset card does call
  the outputs "probabilities" (class-membership probabilities of the model); the note correctly refuses to carry that over.
  No section presents MATRIX or TxGNN agreement as confirming a WWOX hypothesis.

## Corrections suggested to the producer (none block the outcomes)

1. Claim 4 / section 1.3: replace "`kg_grouped_diseases.csv` of the TxGNN commit" by the Dataverse PrimeKG `kg_grouped_diseases.tab`.
2. Claim 7 / section 1.4 item 4: drop issue 17 from the explorer-mismatch sentence; note that issue 18's author reported full_graph as solving his case and a later commenter disagrees.
3. Section 1.1: say the README also links a separate example-weights file that was not examined.
4. Section 2.3: state that the baseline draws 100 nodes and retains the 86 sharing at least 1 000 drugs.
5. Explorer wording: "no HTTP response on a second day" is what I observed; keep "service state may change".

Cleanup: scratch files (shards, KG-node shards, PrimeKG files, lists) remain only in the session scratchpad outside the repository; nothing from the scores table was committed.


## Erratum (Orchestrator, 2026-10-27)

The finding that the TxGNN note's source `kg_grouped_diseases.csv` "does not exist" at the pinned
commit is itself wrong: `txgnn/data_splits/kg_grouped_diseases.csv` is present at commit
0e0203c3939f (HTTP 200 on the raw file; the GitHub contents listing for that directory names it
and `kg_grouped_diseases_bert_map.csv`). The producer's reading stands; the WRONG_SOURCE verdict
for claim 4 is withdrawn. The Dataverse `.tab` remains an equivalent second source.
