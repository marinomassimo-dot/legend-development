# IT32 P5: forward runs after the two changes, no compound named

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class. Criteria were written in the IT32 record (P3 note) before the second run: *reach* (which catalogue families a run returns), *direction* (rows whose action is stated and consistent) and *consumption* (does a consumer read the relation). A rise in reach is not a rise in predictive skill.

## Run 1: need-driven search on the seizure need, before and after the target list was completed
Command: `repurposing_search.py need NEED-SEIZURE-CONTROL-SYMPTOMATIC --limit 100000` with the local catalogue cache. Change: `needs/needs.json`, intervention targets 2 (ABAT, CACNA1G) to 8 (adding SV2A, KCNQ2, KCNQ3, SCN1A, SCN2A, SCN8A; the roles say that a target is a search key and that the sign of the sodium-channel and Kv7 classes differs by lesion class in the case-2 table).

| Quantity | Before | After |
|---|---|---|
| catalogue records / families reached | 63 / 61 | 236 / 225 |
| rows with a stated, consistent direction | 0 | 0 |
| established antiseizure agents reached (by catalogue name, from the reference set named in IT31) | ethosuximide (CACNA1G), valproate (ABAT), vigabatrin (ABAT) | adds levetiracetam, brivaracetam and siblings (SV2A, and levetiracetam also via SCN1A listings), carbamazepine and lamotrigine (SCN1A/2A/8A), ezogabine (KCNQ2/3), phenobarbital (SCN2A) |

Reading: the representation gap was real (levetiracetam was unreachable because no target of the need pointed to SV2A) and is closed for these classes. The gain is reach only: every new row is `direction_unresolved`, most of the 162 added families come from broad gene listings (the sodium-channel targets alone return 145 to 136 rows each), and the sign of the sodium-channel and Kv7 classes flips with lesion class, so no class is read as favourable. Popularity control and matched decoy genes were not run: the claim made is reach, not specificity. Consumers of the added rows: none yet; they feed the P8-type comparator work (aed_compare_it31) and any future signed-row table.

## Run 2: transcript-seeded stage S12 versus S11
Recipe in `README.md`. Selection, eligibility (220) and hand-over (15) are identical to S11; the new column ties 20 proposals to INV-16 (12 eligible, 1 handed over). New, retired or reclassified proposals: none (by design: the change adds provenance, not a rule). Questions created or resolved: none; INV-16 gained neural precedents from NB-3 (below).

## What this does and does not show
* Shows: the engine reaches levetiracetam from the need's targets once the target list names SV2A; a premise shared by 20 proposals now points to the one measurement that decides it.
* Does not show: any improvement in predicting which agent helps in WWOX, any new hypothesis, or that the added families are worth studying. Recovery of agents already known to the module is a function check.
