# RS-R6: is there a perturbation that suppresses or modifies a WWOX-loss phenotype?

Package `disease-models/wwox/research/drug_repurposing/rs_r6_it30_20261106`, 2026-11-06 (UTC). Public edition, WWOX-DEE reference genotype class. Hypotheses, not medical advice; no dose or schedule anywhere.

## Answer (labelled)

1. DATO. As measured changes in stated endpoints, none a rescue of a developmental, myelin or survival endpoint, and not as a screen result: nine measured modifier rows exist in systems with Wwox loss (lithium, ethosuximide, digoxin twice, D-APV, A51, N-acetyl-cysteine, p53 deletion, Ldh knockdown), all small, single-laboratory and most non-neural or provoked or ex vivo. Five were not re-read today (census rows).
2. DATO. The earlier "NO-MATERIAL" in `recovery_it10_p23_20261031/reopen_searches.tsv` row R6 concerns genetic suppressors in fly, zebrafish, mouse and organoid. It is not contradicted: none of the key-less lookups run today found a genetic suppressor screen or cross for a Wwox-loss phenotype.
3. DATO. The only genotype-by-drug pattern in a Wwox-null animal is ethosuximide (no effect in wild type and heterozygote at a low PTZ dose); lithium suppressed in all genotypes (repository census). Neither rescues a developmental, myelin or survival endpoint.
4. DATO. Alliance genetic-interaction records for the fly gene (15 records, 4 papers) all have Wwox as the modifier of another gene, never as the defect. Human has one record (WWOX with FASN, HAP1, BioGRID); mouse, zebrafish, rat, worm and frog have none.
5. DATO. MGI: 7 Wwox genotypes, all single-marker, no double mutant annotated. IMPC: no Wwox line. BioGRID ORCS: bulk blocked; the page lists WWOX in 16 hits of 1408 screens (rows not extracted).
6. DATO. DepMap 24Q4 (public mirror, computed locally): WWOX is non-essential; no robust expression-conditional dependency (differences 0.1 to 0.25 Chronos units, gene list not stable when two blood lineages are removed). Oncology class only.
7. INFERENZA. Four controllable, testable lines follow (`hypotheses.md`): T-type channel block, HIF1-alpha restraint, antioxidant relief, Ldh lowering (carded). All sit downstream of WWOX loss and need no residual protein; none has a target-specific control or a developmental endpoint.
8. INFERENZA. A dependency (Chk2 with DNA damage; DepMap) is not a modifier of the neurological phenotype, a knockout is not an inhibitor, and Wwox acting on another gene is not another gene acting on Wwox loss; none of these is counted as a modifier.
9. IPOTESI. The cheapest discriminating step is a genotype-by-drug test with matched seizure scores plus a genetic target arm (H1); a conditional Hif1a arm (H2) tests whether the digoxin signal is target-borne.
10. DATO. Nothing here supports a rescue claim for the WWOX-DEE reference class; absence of a hit in a bounded search is not absence.

## Step 1: what was done before and what was not

* R6 (IT10 P2.3): the searches were PubMed `Wwox AND (suppress* OR rescue*)` in title and abstract with organism terms, plus intended FlyBase, BDSC, MGI and BioGRID ORCS lookups; the three database lookups are recorded in that file as "not run". Triggers row `R6_q1_complement` points to it. Uncarded item N12 (ACK1/ITCH stability levers) depends on this datum and is unrelated to a suppressor.
* IT12 P1-alt (`modifiers_it12_p1b_20261031`): read the HAP1 GIN352 WWOX-null screen (88 calls, unreplicated, leukaemia-derived line, epistasis not rescue), the fly Wwox papers (Wwox as modifier, wrong direction) and the Ldh rescue (card E02). DepMap portal blocked by a verification page.
* Repository census `analysis/downstream_wwox_independent_rescue_census_20260921.md`: four positive pharmacological arms in WWOX-null systems (digoxin, D-APV, ethosuximide, A51) and lithium non-specific. The map row text ("only Ldh") undercounts this and could be reworded.
* Not run before today and run now: Alliance interactions and phenotypes for human and four model organisms, MGI report file, IMPC, BioGRID ORCS routes, DepMap via figshare, five PubMed strings. Not run at all: the FlyBase web interface itself (Alliance carries its genetic interactions), BDSC stock crosses (wet work), a systematic PubMed screen of the 9 remaining titles of one search.

## Evidence by class (`evidence_rs_r6.tsv`)

* MEASURED MODIFIER, 9 rows (+2 counter rows): M01 to M09, C01, C04.
* INTERACTION, 6 rows (+2 bounded nulls): I01 to I06, N01, N02. Wwox as modifier of other genes (fly), FASN-HAP1 record, GIN352 table, physical records.
* ONCOLOGY DEPENDENCY, 2 rows: O01 (Chk2 plus DNA damage, abstract only), O02 (DepMap, computed).
* GRAPH PROXIMITY, 0 rows. Zero unmerged classes.
* Gene replacement (AAV-WWOX; PMID 34747138, 42422765) and the fly Wwox1 transgene rescue of radiation sensitivity (PMID 16007179) restore WWOX itself and are excluded as modifiers.

## Counter-evidence sought

Lithium is not genotype-specific (C01). Ethosuximide controls had a low PTZ dose (floor effect). Digoxin dose and n are weak and the glycaemia arm is a metabolic proxy. p53 deletion accelerates osteosarcoma (C04). Wwox RNAi even suppresses a fly tumour (I03), showing direction cuts both ways. No suppressor screen was found in zebrafish, rat or mouse.

## Not reachable or partial

BioGRID ORCS bulk files (redirect to an error page) and web service (access key needed; not registered). The ORCS table rows were not extracted: one request to the page endpoint was made and a scripted full pull was refused by the permission classifier, so only the count (16 hits in 1408 screens) is reported. DepMap portal (verification page) bypassed through the public figshare mirror, which needs no account. Europe PMC full text for PMC5146760 and PMC7566881 (HTTP 500; the latter read as HTML). Supplementary tables of PMID 32694731 not reached. Figures not viewed anywhere today.

## Receipts and queries

Nine staged receipts in `receipts/` (suffix 26; validated, see `receipts/INDEX.tsv`); depth is passage-level (`queried_not_full_read`) for five full-text routes and `abstract_only` for four. Every query with time and hit count is in `queries.tsv` (Q01 to Q27). Bytes of the MGI report and DepMap files stayed in the scratch directory outside the repository.

## Independent verification (IT30, 2026-11-06)
A separate context reconstructed the Alliance records, the DepMap distribution (WWOX non-essential: n = 1,178 models, mean +0.055, one model below -0.5, none below -1) and the source of each measured-modifier row before reading these conclusions, and confirmed the classification and the directions, with seven wording corrections applied above (M02 and M04 transfer text, the floor-effect sentence, the I04 and I01 perturbation fields, M09 breakers, the lead sentence). The verification also found, for hypothesis H2 (HIF1-alpha restraint), that a wild-type arm exists in the digoxin experiment with glucose falling, so the signal may be non-target-borne: H2 keeps that as its breaker. Could not be checked: the A51 numbers (paywalled source), the query-versus-library direction of the FASN record, the supplement of the FASN paper, the MGI counts, the BioGRID ORCS hits. Verifier report: `../context_it30_20261105/VERIFY_RS_R6.md`.

> **Update 2026-11-10 (IT41):** the fly Wwox1 transgene rescue of radiation sensitivity named above is superseded: PMID 21075834 attributes that phenotype to background mutations, and no published rescue of a Wwox-loss phenotype was found (fly_wwox_feasibility_it41_20261110).
