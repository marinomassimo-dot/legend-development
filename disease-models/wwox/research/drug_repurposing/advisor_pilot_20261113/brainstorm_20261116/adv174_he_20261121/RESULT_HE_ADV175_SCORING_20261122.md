# LLM generic-perturbation rubric against class prior: scored diagnostic on the Negraes 2021 CDKL5 screen (HE as scorer, 2026-11-22)

**Line 1. LEGEND engine evaluation on CDKL5 = CLOSED, NOT FEASIBLE (the repository has no target-agnostic reusable compound-ranking procedure; what ran is a labelled prompt-only proxy).**
**Line 2. Diagnostic: the proxy rubric minus the class prior B1 on the same rows is +0.169 AUC (paired 95 percent interval +0.061 to +0.286; 15 positive rows in 15 alias groups against 154 null rows in 150 groups, 169 rows). The interval excludes zero because B1 itself scores BELOW chance (AUC 0.287); the rubric alone is at chance (AUC 0.456, 95 percent interval 0.302 to 0.610). Scope: the defined extreme-tail subset only, one CDKL5 line, one dose, technical replicates.**

Written for: ADV. Hypothesis level; in-silico evaluation; no WWOX inference, no efficacy claim, no dose. **No per-compound outcome appears here.** Not an "engine AUC delta": the rubric orders the plausibility of perturbing network activity in the ACUTE setting without sign, while the label measures normalisation after CHRONIC exposure (IT's addendum).

## 1. Order of events (all hashes on main)
IT's frozen method `d4ff2ce91` (sha256 `deadfc68...7a99`); my scoring spec frozen at `40b13ffc7` (12:25:45Z) with its digest (`b29e5d7c...bb09c`); IT's freeze addendum `e61159995` (12:33:30Z, sha256 `91777a93...8d11`); IT's score file `634228f2d` (12:37:03Z, sha256 `9491b18d...9bcc`, recomputed by me before use, equal to the declared one); my addendum 1 (digest `370b080c...2b`) and scoring script v3 (digest `d42b8bb2...d72`) frozen at `6452a426b` (landed before any run against the key). I opened the key against a score only after all of that. **IT's disclosures I carry:** the engine scores were written in a scratch file before the addendum (no outcome visible to IT); the 0.10 margin and the addendum metric were written after the scores and before any outcome; one score was equalised by the frozen same-SMILES rule (the two entries of one compound, 4 to 5) before any outcome; nothing was re-scored. **Mine:** my spec was frozen without sight of any score, but after IT had already scored in scratch; the spec text and addendum 1 are now published in this folder and match their digests. The "declared baseline" of my frozen spec is read as IT's B1 (addendum 1); B2 (lipophilicity) is secondary and labelled so.

## 2. Counts and scope
Eligible rows 169: 15 positive rows (15 alias groups) and 154 null rows (150 alias groups) by my groups; IT's `alias_group` column gives 162 groups for the same rows (used for the addendum metric only). Excluded from the primary: the recognition stratum (5 rows, 4 groups, apart in section 5) and one row whose own label is null inside a positive-dominated alias group. All 175 ids were scored (no missing score).

**Sampling-rule disclosure (after IT's freeze):** the 175-row file was NOT a random draw of the library. It holds (a) every alias group in the high tail of the published recovery score (PR at or above 0.6, the paper's own rule) that also passed my viability screen (above the 10th percentile of the sheet's signed viability, sign and unit undefined: a separate choice of mine, not the authors'), (b) a random draw of 150 of the 178 available alias groups from the low tail (PR at or below 0.35, same viability screen), (c) the recognition stratum, scored apart. The middle band (about 70 percent of the library), the low-viability rows and the ambiguous high-recovery rows were excluded; aliases entered or left whole. **The estimand is therefore "ranking of high-tail against low-tail compounds in this one assay": no library-wide precision, calibration, prevalence or predictivity.** The library's positive class is also threshold-fragile (13 of the 25 compounds at the paper's line sit exactly on its first step), and PR reproduces only weakly across 13 exact-structure duplicate pairs (a reproducibility warning, see the ADV-174 result).

## 3. Primary and original metrics (title metric: B1 class prior is the headline comparator)
| Quantity | Value |
|---|---|
| AUC of the rubric (ORIGINAL primary, d4ff2ce91) | 0.456; stratified alias-group bootstrap 95 percent interval 0.302 to 0.610; label-permutation p (one-sided, AUC at least as high) 0.72 |
| AUC of B1 (vendor pathway class prior) | 0.287 (below chance) |
| AUC of B2 (lipophilicity, secondary comparator) | 0.715 |
| **Rubric minus B1, paired (my frozen spec: stratified cluster bootstrap, 10,000 draws, seed 175)** | **+0.169, 95 percent interval +0.061 to +0.286**; leave-one-positive-group-out range +0.136 to +0.186; share of draws above 0.15: 0.61 |
| ORIGINAL secondary (rubric minus B1) | the same number, +0.169 [+0.061, +0.286] |
| **ADDENDUM metric (IT's text as written: IT's alias groups, 2,000 unstratified resamples, useful gap 0.10)** | **+0.169; 95 percent [+0.060, +0.294]; 90 percent [+0.073, +0.273]**; share of draws above 0.10: 0.88 |
| Rubric minus B2 (secondary, descriptive) | -0.260, 95 percent interval -0.435 to -0.093 |
| Rank check, published PR (descriptive; truncated range by design) | Spearman: rubric -0.33, B1 -0.21, B2 -0.05 |

## 4. Sensitivities (each rubric-minus-B1, my frozen definitions; none changes the primary)
| Variant | Positive rows / null rows | Rubric AUC | B1 AUC | Gap, 95 percent paired interval |
|---|---|---|---|---|
| S-V viability screen at the 20th percentile | 9 / 139 | 0.510 | 0.373 | +0.137 [+0.011, +0.293] |
| S-N nulls restricted to PR at or below 0.30 | 15 / 68 | 0.339 | 0.244 | +0.095 [-0.019, +0.227] |
| S-L without the four named leads' classes (HCN, muscarinic, GSK3, Notch) | 15 / 140 | 0.450 | 0.297 | +0.153 [+0.047, +0.268] (addendum metric +0.153 [+0.041, +0.270]) |
The paper's 60 percent rule is fixed by the sampling and cannot be varied downward; the viability screen can only be tightened, which is S-V.

## 5. Recognition stratum (5 rows, 4 alias groups, apart; no AUC, no labels shown)
Percentile rank among all 175 rows: rubric median 0.43, range 0.18 to 1.00, one row in the top decile; B1 median 0.35, range 0.07 to 0.99, one in the top decile; B2 median 0.39, range 0.16 to 0.72, none in the top decile. IT flagged no recalled drug-response pair (`recognised` empty); absence of recall is not proof of absence.

## 6. Reading (ADV's rule applied exactly, then what it does and does not say)
- **Rule:** the paired interval's lower end is above zero, so the rule's wording is "incremental lift detected on this diagnostic" (+0.169, 15 positive rows, defined subset). Against the prespecified useful gap of 0.10 the interval (+0.061 to +0.286) spans it: whether the lift is at least 0.10 is **unresolved** (88 percent of the addendum draws exceed it; 61 percent exceed 0.15). S-N (tighter nulls) spans zero.
- **What it does not say:** the lift is over a baseline that points the WRONG way. B1 (neuronal-signalling and GPCR classes first) scores 0.29, so compounds the class prior favours are enriched among the low-tail non-normalisers; the rubric, which is a perturbation-plausibility score, is itself at chance (0.456; interval includes 0.5; permutation p 0.72) and correlates negatively with the published recovery score (Spearman -0.33). A lipophilicity rule (B2, 0.715) beats the rubric by 0.26. So the data do **not** show that the rubric ranks normalising compounds; they show that a class prior ranks them worse than chance in this tail contrast.
- **A post-hoc reading, untested:** strong network perturbers (the rubric's and the class prior's favourites) drive many of the 17 features out of control bounds and so sit in the low-PR tail; normalisation needs a perturbation in the right direction, which the rubric cannot specify (IT's addendum says this in advance). This is an interpretation, not a result.
- **Limits:** 15 positive rows; threshold-fragile positives; one line, one dose, technical replicates (one cluster); an extreme-tail design; one reader scoring the rubric once; four sensitivities and several metrics reported (no multiplicity adjustment); the 0.15 and 0.10 gaps are planning values.

## 7. Files
Spec and addendum text published here (digests above); the key, the sampling script, the predictor and score files stay where they are (key and script sealed outside git). Removal: delete this folder's ADV-175 files; the custodian folder is outside git.
