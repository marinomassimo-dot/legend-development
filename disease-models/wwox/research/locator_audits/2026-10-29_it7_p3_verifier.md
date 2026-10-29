# IT7 P3 independent verification (network-prediction comparison)

Verifier, 2026-10-29. Object: `disease-models/wwox/research/drug_repurposing/network_comparison_it7_p3_20261029/` at 0d9d9879 (pre-registration eadbe26a, amendment ae430b6d). Exploratory, computational, not medical advice. The reference genotype class is a WWOX-DEE genotype class; no individual-level record is involved.

## Verdict

The producer's headline numbers reproduce exactly and the verdict labels follow the rules as written. No defect changes a verdict. Defects are about reproducibility of the network inputs, licence attribution, wording and small bookkeeping.

## 1. Timing and rule application

Commit order (git author dates, UTC): PRE_REGISTRATION and inputs eadbe26a 15:13:18; AMENDMENT 1 plus run script ae430b6d 15:18:51; results, README, deviations 0d9d9879 15:52:49. The repaired P1 (31446616, 15:15:10) lies between the two first commits, consistent with the amendment text. The pre-registration holds question, universe, methods, parameters, comparators, measures, decision rules (section 8; E1 rules in section 5) and controls (section 6); the amendment changes none of them. The run script first appears in ae430b6d (5 min after the registration), so code was not registered with the protocol; this is acceptable because every parameter is in the text. Timestamps are self-asserted by one actor; nothing external witnesses them.

Rule-by-rule application (all match unless stated):
- E1: D 0.329 < matched-null 95th percentile, exact p 0.060 > 0.05, 5 of 6 concordant: neither TRANSFERS nor DOES NOT TRANSFER, so INCONCLUSIVE. Correct.
- Signal rule S1-S5: NET-EXT fails S1 (0.047), S2, S3, S4, S5. SIG fails S1 by 0.007 (0.1429 < 0.15) and S2. NO ADDED VALUE by clause (i) (|U| = 256 >= 150, no signal). Correct as written.
- S3 (WWOX edges): difference below 0.03, so no added value. Correct.
- Rule application differs from the pre-registration in no verdict-bearing way. Items that differ without effect: (a) the four HIF1A edges are selected by content (declared in the amendment); (b) REF-0 hits 0 families in U versus 1 in the registration (declared, DEVIATIONS 4); (c) the swapped-context SIG value is identical to the primary by construction (Spearman is symmetric), so that control carries no information for SIG; (d) NET-WWOX was not given a C2 null (not required).
- Post-hoc elements: control C2b (in-degree matched random inputs) was not pre-registered, is labelled as such, and no verdict depends on it (NET fails S1 on the point estimate alone). Script edits after the amendment: delimiter/gene-column fix for E1 and the micro-sign fix of the 10 uM sensitivity; neither touches a verdict (the second touches only a non-verdict sensitivity). The tie handling of the top-decile measure is a design choice, not in a verdict.
- Thin spot: SIG at rho 0.143 versus threshold 0.15 is a point-estimate call; its 90 percent interval [0.039, 0.243] contains both. The producer says so in section 5 of the README.

## 2. Inputs

- sha256 of every file under `inputs/` equals INPUTS.tsv (the INPUTS.tsv row for itself cannot hold and is stale: 1465a672... listed, actual ed95a21e...).
- P1 (31446616) nodes, edges, systems and derived gene values (stored there as `derived_gene_values.tsv`) match byte for byte. P2 pilot tables match at 9de71f34, and are also identical at 7ad3e697 (the cited commit).
- LINCS local files match the listed hashes (sig_info 19da29c0, gene_info 741216cc, extract_rows 33149888, extract.npy 2939e0bf). GSE215425 `processed_data.csv.gz` re-downloaded from GEO: d654f6bd... matches. The series matrix was not re-fetched.
- OmniPath: `resources?format=json` re-fetched, hash 84f756a9... matches. The raw interaction exports cannot be matched by hash (the exact query is not recorded; my differently-parameterised export has another hash). Re-deriving with the stated licence rule gave 49 919 of the 50 015 committed CollecTRI pairs and 55 539 of the 56 374 of my SIGNOR-source pairs in the committed file (committed file is a subset; 835 pairs differ, 96 committed pairs I did not reproduce). The committed edge files are internally licence-clean (every source in them is commercial or composite in the OmniPath list), and my independent propagation on them reproduced the producer's NET and REF-1 rhos to all printed digits.
- Universe: 578 families with usable = yes; the 17 non-usable families are exactly the 17 card-linked-only families. Own code from `sig_info` plus the extract: 1 239 signatures, |U| = 256, matches. Card-linked families inside U: one (sirolimus). Ethosuximide, lithium and vigabatrin families are not in U. The network files contain no compound nodes. Generic TF-to-WWOX CollecTRI edges exist (17 rows, WWOX as a target gene); they are public regulatory edges, not cards or compound edges, and no compound targets enter through them.
- BioNAV/NeMoCAD: not referenced in the script; the documents say not used. Consistent.

## 3. Recomputation (own code, scipy-free)

- E1 (HPC): D = 0.329, exact one-sided p = 0.0595 (15 of 252), 5 of 6 genes in build direction (LDHB -0.10 against), matched-null 95th percentile 0.396 (producer 0.389; different draw, same conclusion). PFC 0.186 / 0.163, CTX 0.219 / 0.194, CB 0.035 / 0.343 (35 assignments). Counts are integer-valued; column totals 32.6-49.1 M.
- SIG rho 0.1429; bootstrap 90 percent interval [0.039, 0.243] (producer same). REF-1 rho -0.0854 (25 non-zero families). NET-EXT rho 0.0474 (3 hops, damping 0.5, 1/out-degree, k = 0 excluded). BASE-promisc 0.0306. All equal the README.
- Frequent hitters: own random matched readouts flag 37 NET families (producer 38) and rho without them 0.018 (producer 0.011); both far below 0.10.
- Producer script re-run as documented: `family_scores.tsv` and `signature_scores.tsv` byte-identical; `results_summary.json` identical except `wall_seconds` (982 vs 962); E1 summary byte-identical. Wall time 982 s.

## 4. Judgement of the claims

- "No added value, minimum detectable effect about 0.15": correct as an operational statement. The standard error 0.063 gives 1.645 x 0.063 + 0.84 x 0.063 = 0.157, so "about 0.15" is slightly generous. The wording "no added value" is clear in the README as "no detectable gain"; for SIG the interval reaches 0.24, so it is not evidence of absence and should not be read as "SIG does not work". The README's section 5 already says this. NET-EXT (upper bound 0.15) is the better-supported negative.
- "Inconclusive" for E1: correct; the data lean in the build direction (three regions, 5/6 genes) but nothing passes. No over- or under-statement. The claim that the compound results carry no demonstrated WWOX-loss relevance is correctly conditional.
- Reopening conditions (a)-(d) are reasonable; (d) a larger module is the most informative given that five of six genes are L1000-inferred. Missing: a stated look at signature quality (the README lists it under UNVERIFIED).
- Nothing is presented as WWOX-specific therapeutic evidence. The sirolimus percentiles are labelled an anecdote.

## 5. Licences

- OmniPath metadata (re-fetched): SIGNOR CC BY 4.0 (commercial); CollecTRI and DoRothEA composite; TRRUST CC BY-SA 4.0; HTRIdb and RegNetwork LGPLv3 (as OmniPath labels them); DoRothEA-A_CollecTRI "Informal". GEREDB (AFL, academic) rows excluded. The SIGNOR licence could not be checked at the SIGNOR site (connection refused from this host); the TRRUST page states CC BY-SA 4.0.
- The README attribution names only SIGNOR (CC BY 4.0) and "constituent resources". The committed CollecTRI file contains TRRUST-derived content (share-alike), so share-alike and per-resource attribution should be stated for that file.

## Defect list (severity ranked)

1. MEDIUM - Network inputs are not exactly reproducible: the raw OmniPath exports are not committed, the query URL/parameters are not recorded, and no fetch-and-filter script exists. The licence filter, sign consensus and symbol rule cannot be re-run from the record; my re-derivation differs by 96 and 835 pairs (rho unaffected here). Add the query and filter script, or commit the raw exports' hashes with the parameters.
2. MEDIUM - Licence attribution incomplete: TRRUST content (CC BY-SA 4.0) and LGPL-labelled resources sit in the committed CollecTRI file without share-alike or per-resource notice; SIGNOR terms not checked at source.
3. LOW - SIG "no added value" rests on a 0.007 gap to the threshold with an interval spanning it; wording should keep "not detected, not excluded" in the verdict table (the body already does).
4. LOW - The stated MDE 0.15 is slightly low (0.157 by the same arithmetic).
5. LOW - Bookkeeping: INPUTS.tsv self-hash stale; README wall time 932 s vs results_summary 962 s; the P2 provenance string says 7ad3e697 while the repaired P2 head is 9de71f34 (content identical); the swapped-context SIG control is vacuous and should be marked so; C2 (SD-matched) is a weak null, as the producer says.
6. INFO - The registration is not externally time-witnessed; run script was registered 5 minutes after the protocol.
