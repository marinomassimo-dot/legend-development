# ADV-144 result: the sizing gap C06 and group (b) of the RP-041 cold read (SCI window X, 2026-11-21; hypothesis level; class level; no dose; no recommendation to treat; not medical advice)

Pre-registration: `PREREGISTRATION_ADV144_GROUP_B_SCI_20261121.md` (commit `409755757`, before the briefs were opened). Held inputs: the consolidated pup brief (called **V2**: `experiment_brief_presidio013_sci_20261116/v2_consolidated_sci_20261119/PUP_BRIEF_V2_CONSOLIDATED.md`), the ADV-061 addendum record (`fig7_quant_ethosuximide_lithium_sci_20261115/README.md`) and the held Cheng 2020 full text (root `files/fulltext/PMID32000863_Cheng2020_PMC_r2.xml`). IT's table (`rp041_cold_read_it_20261121/output/`) is read, not redone. Scripts are in the job scratch (`sizing_adv144.py`, `numbers_adv144.py`, stdlib only); the numbers they print are reproduced in the tables below.

## Answer first
1. **C06 is not an arithmetic error; it is a wording defect.** "36 to 109" and "180 to 320" are both reproduced from the addendum's own inputs, but they answer **different contrasts**: 36 to 109 is the simple effect in knockouts (knockout sigma only); 180 to 320 is the interaction contrast, whose variance contains the **wild-type** sigma too, and the wild-type arms are the floor-bound ones (sigma about 1.07 to 1.30 against 0.54 to 0.94). The addendum's sentence "twice (not four times) the simple-effect number per cell" is true only when sigma is equal in all four cells. In general the interaction n per cell equals **the sum of the two simple-effect n values (knockout plus wild type)**: 36 + 140 = 176 and 109 + 207 = 316.
2. **The comparable statement:** at equal sigma the interaction needs 72 to 218 per cell (twice 36 to 109); with the addendum's floor-bound wild-type sigma it needs about 175 to 316 (the "180 to 320"). The truth for a real pilot lies between them and depends on the wild-type sigma **at a non-floor stimulus**, which the brief itself requires and the addendum has not measured. A dated clarification (not an error correction) is added to the addendum record.
3. **Group (b), 29 items (24 plus the five the blind reader added):** `GROUP_B_CLASSIFICATION_ADV144_SCI_20261121.tsv` holds one row per item with class, owner of the remaining decision, answer or rule with the INFERENCE label, locator, whether IT's text must change, what would change it, and the question for the laboratory or the operator. Counts and the main findings are below.
4. **Four findings that change the text beyond C06:** (a) the pilot row of V2 lists vehicle pups only while its stop rule refers to a panel agent (Q19); (b) one vehicle group cannot serve arms with different injection schedules unless every pup gets the same number of injections, drug or saline (Q15); (c) "wild-type animals are not limiting" holds only if wild types come from wild-type pairs: from heterozygote crosses 231 wild types need about 132 litters against 33 (Q45); (d) the "about 300 animals" total counts vehicle cells at 11, while V2 says the vehicle is about twice a test arm: with the square-root rule the total is about 354 (Q32).

## Part 1: the sizing (C06)
Inputs are only those the addendum states (its PTZ-alone table): coefficient of variation of S at within-animal correlation 0.6 and 1.0 for four groups, ratio 0.7, and the sigma on the log scale from sigma_log = sqrt(ln(1 + CV^2)). The addendum does not print alpha and power; I **reproduced its 36, 55, 77 and 109 exactly with two-sided alpha 0.05 and power 0.80** (z sum 2.8016; log of 0.7 = -0.3567), so those are the values it used (the 77 reproduces as 75.7 to 77 depending on the third decimal of sigma: 0.78 or 0.79).

| Group (record table) | sigma_log at rho 0.6 and 1.0 | simple effect, animals per arm (normal approximation) |
|---|---|---|
| 7b knockout | 0.54 and 0.67 | 35.8 and 55.1 |
| 7d knockout | 0.78 and 0.94 | 75.7 and 108.9 |
| 7d heterozygote | 1.06 and 1.23 | 139.7 and 185.5 |
| 7d wild type | 1.14 and 1.30 | 160.0 and 207.4 |

**Interaction contrast** (2x2: genotype by treatment; interaction = difference of the two simple log-effects, size |ln 0.7|; equal n per cell; variance of the contrast = 2(sigma_KO^2 + sigma_WT^2)/n): n per cell = (z sum)^2 x 2(sigma_KO^2 + sigma_WT^2) / (ln 0.7)^2 = **n_simple(KO) + n_simple(WT)**.

| Knockout panel and rho | wild-type panel | interaction n per cell | twice the knockout simple n |
|---|---|---|---|
| 7b, 0.6 | 7d heterozygote | 175.5 | 71.6 |
| 7b, 1.0 | 7d heterozygote | 240.6 | 110.1 |
| 7d, 0.6 | 7d heterozygote | 215.4 | 151.3 |
| 7d, 1.0 | 7d wild type | 316.2 | 217.7 |
| equal sigma 0.78 in all cells | | 151.3 (exactly twice 75.7) | 151.3 |

The addendum's range (175.5 at the low pair, 316.2 at the high pair) rounds to its "180 to 320" and its derived totals (700 to 1,300 animals, 350 to 630 knockouts, 200 to 360 litters) also reproduce (4 cells x 175 to 316; 2 knockout cells x 175 to 316; divided by 1.75 knockouts per litter).

**Which statement is comparable with which:** the "per arm for a ratio of 0.7" is a simple effect in the **knockout** (sigma 0.54 to 0.94). The "per cell" interaction figure carries the **wild-type** sigma (1.07 to 1.30), taken from arms the addendum itself calls floor-bound (mean S 0.27 to 0.41, CV above 1.4). Two cautions, both inputs rather than arithmetic: (i) a lognormal sigma from a CV above 1.4 at a floor-bound arm (S = 0 occurs) is not trustworthy, and the brief requires a **non-floor** wild-type stimulus, at which sigma is unknown; (ii) the whole bracket comes from means and SEM bars of two figures.

**Blind recompute (a different delegate, different model):** see the section "Blind checks" below.

**Dated clarification written into the addendum record** (`fig7_quant_ethosuximide_lithium_sci_20261115/README.md`, line added after the ADV-061 addendum paragraph; no number changed): "The interaction n per cell is the sum of the knockout and wild-type simple-effect n; it equals twice the simple-effect n only at equal sigma. 180 to 320 uses wild-type sigma 1.07 to 1.30; equal sigma gives 72 to 218."

## Part 2: group (b) classification
Rule as pre-registered; one class per item (split where a part is class 1 and a part class 3), precedence 3 over 2 over 1; every derived number is labelled INFERENCE in the TSV. Items Q06, Q12 to Q15, Q18 to Q23, Q31 to Q34, Q37, Q39, Q42, Q43, Q45, Q61, Q62, Q67, Q68 and the five blind-reader additions (X1 to X5: lithium salt/vehicle/route/spacing; feeding and thermal state; own validated scale; pilot animals reused and sign-off; stop rule scope).

| Class | Items |
|---|---|
| 1 only (closed by held text) | Q18 (the Cheng scale is printed), Q23 (the 27 cells re-enumerated from V2 line 47), Q33 (all four litter figures reproduce; 75 is the superseded four-times arithmetic, 25 the optimistic-sigma interaction figure) |
| 1 plus a remaining laboratory or operator part | Q06, Q13 (dose and route printed; volume not), Q37 (two death statements do not conflict; colony survival is the laboratory's), Q62, X1 (spacing), and 1 plus a rule: Q14, Q32, X5 |
| 2 (a rule I define; INFERENCE) | Q12, Q15, Q20, Q21, Q31, Q34, Q39, Q67, Q68, X3; with a laboratory input: Q19, Q22, Q45 |
| 3 (only the laboratory or operator can decide) | Q42, Q43, Q61, X2, X4 |

**Predictions scored (pre-registered):**
* P1 (60 percent: different effect sizes explain the gap): **missed on the mechanism, held on the substance**: the gap is a different variance (the wild-type sigma), not a different effect size; no arithmetic error.
* P2 (60 percent: at least 8 of 24 have a class 3 part): **held** (15 of the 24 have a remaining laboratory or operator part; only 3 are pure class 3).
* P3 (50 percent: at least 5 of 24 are class 1): **missed**: only 3 of 24 are closed by held text alone (Q18, Q23, Q33); the rest need a rule, a laboratory fact or both.
* P4 (55 percent: the blind recompute reproduces 36 to 109 within 10 percent and does not reproduce 180 to 320 without an input the addendum does not state): first clause **held** (36 to 109 reproduced by my script and by the blind delegate); second clause **missed** (180 to 320 reproduces from stated inputs in both recomputes: the wild-type sigma is in the record's own table).
* P5 (65 percent: Q67 and Q68 are class 2 or 3): **held** (both class 2).

## Blind checks
**(a) Sizing recompute.** A delegate of a different model (requested `opus`, briefed at effort medium, stdlib only, no repository file opened; the model and effort are as requested in the dispatch and were not read back from a census) received only the CVs, ratio, alpha, power and the 2x2 description, not my numbers or the addendum's. Its results agree with mine to the third decimal: simple effect per arm 35.8, 55.1, 75.7, 108.9, 139.7, 185.5, 160.0, 207.4 (rounded up 36, 56, 76, 109, 140, 186, 160, 208; exact noncentral-t values one animal higher); interaction per cell 175.5 to 316.2 over the eight knockout-by-wild-type pairings (t-based with pooled or Welch degrees of freedom: within one animal). It stated unprompted that (a) the interaction n equals twice one genotype's simple n exactly when the two sigmas are equal and (b) in general it is the sum of the two simple-effect n (verified in every row). It listed its assumptions (CV of the already-aggregated S; same rho in both genotypes; two-sided; no attrition or multiplicity adjustment). **Outcome: the addendum's 36 to 109 and 180 to 320 both reproduce from its stated inputs; my pre-registered P4 (second clause) is missed.**

**(b) Classification.** A second delegate (requested `opus`, briefed at effort medium, not read back) received only V2 and the held Cheng 2020 full text and ten of the questions in plain words, with the three-class rule, not my answers. Its report is a hand-back message only. Comparison by class: **8 of 10 agree** (Q13, Q18, Q32, Q33, Q39, Q67, Q68, Q23-and-Q34 taken together as its question I). Two differ:
* Q45 (wild-type source): the reader proposed class 3 (only the laboratory knows colony yield) and no litter figure; I gave a litter count from the brief's own 1.75 knockouts per litter and 7 pups per litter and labelled it INFERENCE. The two do not conflict (the count is conditional on the source); the row keeps both parts (class 2 and 3).
* Q61 (rescue trigger): the reader read the status definition as the trigger (class 1 plus 3); I had called it pure class 3. The definition of status is held (Cheng 2020; V2 line 30), the rescue procedure and who decides are not; **row changed to class 1 and 3**.
Added from the reader: the null band 0.85 to 1.15 in the panel-validity rule (Q67), the share-of-zeros criterion and the unit caveat (S is an area over 60 minutes, the floor bracket is in mean stage) in Q68. Its sizing of the vehicle (five vehicle cells doubled, about 350) agrees with my 354. It reported one extraction step interrupted by a safety classifier (dose strings in Methods) and reported no dose text. The reader's only added caution is that Q23 and the pilot (Q34) are two different questions; they are kept as two rows.

## Limits
Every number is a normal approximation unless a t-based value is shown; all inputs come from means and upward error bars of two published figures (the addendum's own limits stand). Q13 to Q15 use the printed regimens of Cheng 2020 by locator; none of their values is copied here (no-dose perimeter) and none is proposed for any laboratory. The classification is mine; the laboratory's and the operator's questions are phrased, not answered. Nothing here is a design value for a laboratory until its own sign-off.

## CHOICE
* **Next most informative verifiable step:** measure the **wild-type sigma at a non-floor stimulus**, because it is the single input that moves the interaction sizing from 72 to 316 per cell. That is the pilot (stage 1), not a document; it needs the laboratory.
* **Rejecting observation:** a pilot in which wild-type vehicle sigma at a non-floor stimulus is within 20 percent of the knockout's (then the interaction n is about twice the knockout simple n, 72 to 218) would reject the 180 to 320 figure as a planning number; a pilot in which it stays above 1.0 would confirm it and the interaction is out of reach, as the brief already says.
* **For IT:** the text changes marked `text_change_for_IT = yes` in the TSV (Q12, Q15, Q19, Q22, Q31, Q32, Q33, Q39, Q45) and the C06 wording; ADV-143 keeps its OPEN-GAP markers and this file closes them with the locators above.
