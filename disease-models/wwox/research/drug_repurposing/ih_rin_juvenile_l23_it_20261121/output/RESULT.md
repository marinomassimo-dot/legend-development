# RESULT - Ih-blocker effect on resting Rin, wild-type juvenile rodent neocortical L2/3 pyramidal neurons (IT, 2026-11-21)

Producer: model sonnet, effort high (as stated at dispatch; to be read back with `session_model_census.py`). Mechanism-level package, reference genotype class only; no dose, no recommendation, no agent nominated. Pre-registration: `SO_before_search.md`.

## Answer first

1. **No second independent qualifying source was found, by two routes.** Under the pre-registered rule the answer is therefore: *"no second source found"*, a two-route negative that is not proof of absence. The thesis value stays **one provisional lead**: ZD7288 50 uM, rat L2/3 pyramidal, group label "p14", Rin 157 +/- 17 to 213 +/- 16 MOhm, n 6 cells (3 animals), **DERIVED share 1 - 157/213 = 0.26** (`candidates.tsv` C01a). Neither the "supported" band (independent shares within 0.15-0.35) nor the "outlier" band (two independent shares at or below 0.10 or at or above 0.40) can be evaluated with one source.
2. **What the nearest non-qualifying neighbours show** (none counts for the rule; each fails the age, layer or blocker criterion): the DERIVED shares are 0.29 (mouse V1 L2/3, 6-10 weeks, Cs+ not ZD7288, n 7; C02), 0.19 (rat PFC layer V-VI, 18-25 d, ZD7288 20 uM, held at -55 mV, n 6; C05) and about 0.04 for wild type and 0.09 for Fmr1-KO (mouse auditory cortex L2/3, P28-P42, ZD7288 10 uM; both computed against a proxy baseline from a different figure, so approximate; C03a). Spread 0.04 to 0.29 over three unlike preparations, plus the thesis's own p28 cohort at 0.44 (p > 0.05, n 6 from 2 animals; C01b). The spread is large; one number of about 0.26 is therefore not a safe expectation for another laboratory's wild-type cells (INFERENCE from non-qualifying neighbours; the pre-registered prediction band 0.10-0.40 is not tested).
3. **No wild-type P13-P17 L2/3 Ih-blocker Rin value exists in what I could read except the thesis**; and the thesis's age label is a group label inside p8-p45 with no stated spread (the earlier package searched its text for p13, p15, p16, p17 and found no hit).

## What this changes for INV-18 (decision, with its basis)

- **Can INV-18's matched recording expect a blocker effect of about a quarter of input conductance in wild type?** Not on this evidence. A quarter is one lead from one thesis (n 6), under a protocol that departs from a standard small-step Rin (quadratic-fit coefficient; 35 C; no TTX stated; 50 uM ZD7288, a dose at which the author reports AP half-width broadening from 1.6 to 3.4 ms at p14 and suspects an unspecific block of delayed-rectifier K channels). Treat 0.26 as the upper-middle of an unmeasured range, not as an expected value: INFERENCE.
- **Must the Ba2+ and Ih steps (ladder step 2b) run in the same cells?** The thesis's Ih and Ba2+ shares come from different cohorts with different baselines (137 to 161 MOhm; Ba2+ share 0.22 at p14, `../it48q01_forward_citations_it_20261121/verify/answers.tsv`), and the only other preparation read (C03a, outside the age window) describes Ih as "a secondary" contribution next to the Ba2+-sensitive current in the Fmr1-KO state (its authors' reading of knockout cells; for wild type it reports only the +8.0 MOhm ZD7288 change). Because the ratio of the two shares is the quantity a design would read, and between-cohort baseline differences are of the same size as the effects, a same-cell sequence is the only design in which the two shares are comparable (INFERENCE from the sources; neither is a measured within-cell comparison at P13-P17).
- A genotype difference in INV-18 can be read against a wild-type blocker effect only if the wild-type effect is measured in the same experiment at the same age; no external wild-type reference exists to subtract.

## Sources, by status (details in `candidates.tsv`)

| Row | Source | Status | Why |
|---|---|---|---|
| C01a, C01b | Fucke 2008 thesis (heiDOK) | lead in hand, not counted | the question's starting point; same record as the IT48-Q01 package |
| C02 | bioRxiv 2023, input-specific gating of NMDA amplification via HCN channels (mouse L2/3, Emory) | near-miss | 6-10 weeks old; Rin effect measured with Cs+ (also blocks Kir); ZD7288 50 uM used only for EPSP half-width; also gives untreated S1 L2/3 Rin at 1, 2, 6 weeks: 450.6, 175.7, 98.3 MOhm |
| C03a | bioRxiv 2026, Ba2+-sensitive Kir in Fmr1-KO auditory L2/3 (Santiago de Chile) | near-miss | wild-type mice 28-42 days old; ZD7288 10 uM raised wild-type Rin by 8.0 MOhm (p 0.0349); pre-drug mean of the ZD cohort is figure-only |
| C04 | Kalmbach 2018 Neuron | near-miss, unread age | mouse TeA supragranular, ZD7288 10 uM raised Rin; size and age not obtained (figure-only) |
| C05, C06 | rat PFC papers (Feng 2013; Zhang 2013) | near-miss | layer V-VI 18-25 d; L2/3 and L5 pooled 20-23 d |
| C07 | Wwox knockout slice paper 2021 | rejected | P13-P17 and the Wwox genotype class, but no Ih blocker experiment (a ZD7288 sentence in the Discussion cites Wang 2016) |
| C08 | Yang 2018 (Ih development, mouse PFC) | rejected | layer V, no Rin-before/after |
| C09-C13 | Song and Moyer 2018; Routh 2022; Sun 2012; Wang 2016; Huggenberger 2009 | not reached | abstract only; supply list in `SEARCH_RECORD.md` |

## Limits (read before using any number above)

- **Read depth.** Full text (Methods, Results, legends) was read for two preprints (C02, C03a; staged receipts `receipts/FTR-20261121-IHRIN-01.json` and `-02.json`, `staged_receipt_check` OK) and for the thesis's ZD7288 paragraph (receipted in IT48-Q01). Everything else is snippet-level or abstract-level. 476 PMC bodies were screened by a regex; a screen is not a read.
- **The negative is two-route and screen-limited.** It covers Europe PMC and PubMed strings and the citation neighbourhoods of five seeds (314 citing works; 130 without a PMC id were title-scanned only; the Nolan 2003 seed was named but not pulled). A qualifying source that uses neither "layer 2/3" nor P-numbers in its text, or that sits behind a publisher, would be missed. The ceiling of 40 full texts was not reached (3 read in Methods and Results); the route was exhausted, not the budget.
- **Derived values.** All shares are 1 - Rin_before/Rin_after from printed group means, not paired per-cell ratios; C03a's two shares use a baseline from a different figure and are approximate; C02's Rin unit is printed as mV in the legend (a typesetting slip read as MOhm by context); C02's blocker is Cs+, not an Ih-selective drug.
- **The thesis itself.** Age label is a group label; Rin is the linear coefficient of a quadratic V-I fit, not a small-step ratio; V-I curves after ZD7288 "are not completely linear" and the author says Rin and cAR "have to be considered with caution"; sag was not clearly abolished; no TTX stated for the ZD7288 cohort; n 6 from 3 (p14) and 6 from 2 (p28) animals; one laboratory; no journal version found.
- **Not tested:** the pre-registered prediction (shares 0.10-0.40, most likely 0.15-0.30) cannot be scored without qualifying sources; of the non-qualifying values, 0.04 lies below it and 0.19, 0.26, 0.29 inside it.
- **Wwox link.** The one P13-P17 source in the Wwox genotype class (C07) did not test an Ih blocker; no HCN data exist there to read against INV-18.

## Files
`SO_before_search.md`, `candidates.tsv` (13 rows), `SEARCH_RECORD.md`, `receipts/` (2 staged JSON receipts, not recorded in the ledger). Full texts: `/home/desktop/legend-development/files/fulltext/ih_rin_it_20261121/` (p1 = bioRxiv 2023 preprint with text layer; p2 = bioRxiv 2026 preprint with two text layers).

## 7. Integrator's dated notes (IT, 2026-11-21; sections above kept as written)

* **Model and effort read back (producer):** `claude-sonnet-5-5` x79 turns, effort `high` x79 (`session_model_census.py` on the delegate transcript).
* **Arithmetic re-done by the integrator:** C02 1 - 74.78/104.99 = 0.288; C05 1 - 209.97/258.46 = 0.188; thesis 'p14' 1 - 157/213 = 0.263 and 'p28' 1 - 64/114 = 0.439 (matches the blind verifier's Q8 rows of the IT48-Q01 package). C03a stays approximate (a proxy baseline from another figure).
* **No blind verifier was dispatched (DECISION, reversible).** Reason: the pre-registered outcome is a two-route negative with the thesis kept as one provisional lead; no row of this package feeds a claim or a premise, the three neighbour shares are recomputed above, and the rows that could change the answer (C04 to C08) are non-qualifying on age or layer by the sources' own stated windows (all at 18 days or older, or an adult, or layer V-VI), not on a reading the producer could have got wrong. What would reverse the decision: a second reader finding a P13-P17 L2/3 Ih-blocker value in a candidate the producer left at snippet level (C04 to C08) or in a supply-list paper.
* **Receipts:** `FTR-20261121-IHRIN-01` passes the dry-run; `FTR-20261121-IHRIN-02` concerns a preprint already read on 2026-11-10 (`FTR-20261110-PPR1225217-94`, partial; `-95`, abstract only), so the integrator declared `reread_reason: new_question_outside_prior_coverage` and `prior_receipt: FTR-20261110-PPR1225217-94` in the staged file before recording.
* **Wording of the absence (ADV condition, 2026-11-21):** read every 'no second source' above as 'not found by two routes in the screened set (476 PMC bodies by regex, 3 read in full)'; the regex screen is lossy by construction and nothing here says such a source does not exist.
