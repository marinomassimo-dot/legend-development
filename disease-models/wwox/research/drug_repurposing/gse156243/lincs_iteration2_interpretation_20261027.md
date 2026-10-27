# LINCS reversal output of the GSE156243 WWOX-knockout signature, iteration 2: controls, wrapper versus service, compound identity, context, return to WWOX

Scientist-d, task SD-IT2-LINCS-20261027 (package W3). Exploratory. Not medical advice; class level; no dose or suitability. Everything LINCS-derived is NOT WWOX EVIDENCE.
A knockout signature is NOT a rescue signature and NOT a Q230P or variant-specific signature. A q-value or z-score is not efficacy. Same-lineage services are one vote.

## 0. Declaration, fixed BEFORE any request of this iteration (offline findings that preceded it are listed so the declaration is not blind to them)

Seen offline before declaring (stored files and the public metadata tables only, no new request):
(a) the stored S1P/S1P2 request files are 29,450 bytes, the byte count of the hyphen-stripped S1 request (the verbatim S1 request is 32,714): the shuffled-direction requests were built from the tracked, hyphen-stripped entity map (`uuid_transform_manifest.tsv`, publication-gate transform) and `sigcom_permuted_direction_query.py` never restores the hyphens, whereas S1 was sent from the verbatim map. This yields the hypothesis H-ENC below.
(b) S0 has 8 genes in both arms and a median log2 mean CPM of 3.65 against 5.09 for S1; 70 percent of S1 symbols (587 of 834) lie in the 12,328-gene L1000 space against 61 percent for S0. S0 is therefore not matched to S1 on expression or on L1000-space membership.

Requests (SigCom LINCS `enrich/ranktwosided`, `l1000_cp`, limit 100, sequential, 15 s apart, one request each, no retry, no key):
DIAG (S1 re-sent with hyphen-stripped ids), S1P and S1P2 (the existing shuffled sets, ids with hyphens), N1-N3 (random sets matched to S1 per gene on expression decile and L1000-space membership, arms disjoint, seeds 20261101-03), K1-K2 (pseudo-contrasts: the four KO libraries split 2 v 2, top 517 / 317 genes by Welch t on log2 CPM; no condition difference by construction). Eight requests. If a request errors it is recorded, not repeated.
Direct L1000FWD public API: S1 and one null (N1), one request each, to learn which limits belong to the wrapper.

Predictions (each falsifiable by `lincs_it2_summarise.py`):
- **H-ENC.** DIAG returns an empty ranking (`reversers 0`) while S1P and S1P2 with hyphens return non-empty rankings. If DIAG is non-empty the encoding hypothesis is false and the emptiness stays unexplained.
- **P-N (content null).** In each of N1-N3 the share of `MCLF*` 4 uM / 6 h signatures among top-100 reversers plus top-100 mimickers is below 20 percent (S1: 60 percent; S0: 0.5 percent). At or above 40 percent in any N set: the family is selected by L1000-space/expression content alone (coverage effect) and S1 loses its specificity.
- **P-K (differential-like noise null).** Same quantity in K1-K2 below 20 percent. At or above 40 percent: any high-variance DE-like list pulls the family.
- **P-S1P (direction control, as P7-P9 of the earlier declaration).** In S1P and S1P2 the 4 uM / 6 h MCLF share of top-100 reversers is at least 40 percent AND the strongest |z-sum| is at least 50 percent of S1's (16.65): the family and the score are properties of gene content, not of the up/down pattern. Either one below: direction contributes.
- **P-WRAP.** The direct L1000FWD result for S1 also returns 50 (not 100) similar/opposite hits: the cap belongs to the service, not to ToolUniverse. If it returns more, the cap was the wrapper's.
Outcome vocabulary: USEFUL / INCONCLUSIVE / DISCARD as in the earlier declaration. Absence from a result is "not returned", never "ineffective".
