# FREEZE: informed-arm predictions of SCI (PRESIDIO-010), 2026-11-16

Status: DRAFT until `rule.json` sha256 is recorded in the ledger by HE (plan: by 09:45Z). Freeze = the commit that lands this file on main, after that hash exists and before any outcome table is opened. The blob must not change afterwards (HE's checker). Not medical advice; mechanism matching only; no agent is recommended; BLOCK-1 applies before any candidate row. Reference genotype class only.

rule_json_sha256: PENDING (HE)
cells: `output/cells.tsv` (sha256 recorded in `cells.sha256` at freeze); scorer draft `build_cells.py`; baselines `baselines.tsv`.
Role: predictor of the informed arm. I have not opened, extracted or been given any outcome table. Disclosed prior exposure and the rows scored separately are in `README.md` ("What I used and did not use").

## Predictions (class-level, mechanism only; ties stay ties)
**F1. Seizure endpoint, P13-P15 (and the declared TRANSFER to later/unspecified), BOTH rankings frozen (`output/rankings.tsv`, RULE_AMENDMENTS 2 and 4):** per-thread sum: top set of 5 of 15 (informativeness 0.67, at the claim limit, a weak prediction): score 9 (summed) NMDAR pore blockers, GABA-A positive modulators (non-benzodiazepine), benzodiazepines, sodium-channel blockers, valproate-type; of these, with origins collapsed and breadth adjusted, the first three lead (9) and sodium-channel (6) and valproate-type (3) are breadth members. Next, 6: T-type calcium, AMPA antagonists, GluN2B NAMs, GABA-AT/GAT, carbonic-anhydrase/multi-target (3 collapsed). Then 3: SV2A, Kv7 openers, cannabidiol/fenfluramine-type. Then 0: steroid/ACTH, ketogenic diet (no thread). Origin-collapsed ranking (single-origin collapse is itself a result): top set of 3 of 15 (informativeness 0.80): NMDAR pore blockers, GABA-A PAM, benzodiazepines; then 6: sodium-channel, T-type, AMPA, GluN2B NAMs, GABA-AT/GAT; then 3: SV2A, Kv7, carbonic-anhydrase/multi-target, valproate-type, cannabidiol/fenfluramine-type; then 0: steroid/ACTH, ketogenic diet. The matrix does NOT predict an order inside a tie set; a hit inside a tie set is scored as set membership and called a weak prediction. Null: undefined at P13-P15 (all contributing tiers equal); no p-value is claimed.
**F2. Among the four classes with coded outcomes in A1 (seizure endpoint):** GABA-AT/GAT (6) above cannabidiol/fenfluramine-type (3) above steroid/ACTH and ketogenic diet (0, tied). GABA-AT/GAT is a class I was exposed to (README); scored separately.
**F3. Development endpoint, any window (RULE_AMENDMENTS 5):** NULL ORDERING FROZEN: all 15 classes tied, informativeness 0; no ordering of any class (no thread links a class to a developmental outcome). Prediction: concordance with any observed ordering is at chance. This is a prediction, not an omission.
**F4. Seizure P6-P8:** not scorable; null ordering frozen (all 15 tied).
**F5. Aggravation (recorded apart, never netted):** AH2 NMDAR pore blockers, development, P6-P8: aggravation (abstract-level rodent premise). AH1 sodium-channel (seizure, P13-P15), AH3 GABA-A PAM and AH4 benzodiazepines (seizure, P6-P8): unknown; no prediction of direction is made.
**F6. Prospective, outside the class table:** LEAP-2: the NAM-sensitive fraction of the isolated NMDAR current in Wwox-null pyramidal cells at matched age and region (P13-P17) is at least 40%; a fraction inside 0-34% (the wild-type interval of Mierau 2004, a different region) rejects it. Outcome source: a future measurement; no date. LEAP-1: a held or future exposure-with-worsening statement for a sodium-channel agent exists only if interneuron firing depends on Nav; its absence is not evidence.

## Baselines (frozen with this file)
(i) PTZ-profile ranking: `baselines.tsv` (background pharmacology, labelled; IT to second-read). (ii) frequency-of-use ranking: HE from IT's counts, not mine. (iii) uniform class prior: all classes tied.

## Scoring rule proposed (HE and IT may amend BEFORE the outcome table is opened; not after)
Pairwise concordance over class pairs whose observed outcome ordering is classifiable; tied predictions score 0.5; unknown excluded. The matrix beats a baseline only if its concordance exceeds the best baseline by at least 0.10 on at least 10 classifiable child-agent pairs; otherwise the result is declared uninformative (rule v1). Classes with fewer than 3 children with a stated outcome are not scorable.

## What would change my mind
F1: a head-to-head in null slices that ranks a class outside the top tie above it (README, L7); a held drug-by-genotype measurement (none exists); an independent origin for any of T1, T2, T13. F2/F3: the coded outcomes, read after the freeze by someone else. F5: held exposure-with-worsening statements.

## Known weak points, stated before any outcome
Directness is my judgement (the permutation null is undefined at P13-P15, all contributing tiers equal); three threads share one origin; class targets and the PTZ profile are background knowledge; mouse age is not mapped to child age; the GABA axis is disputed in the held data.
