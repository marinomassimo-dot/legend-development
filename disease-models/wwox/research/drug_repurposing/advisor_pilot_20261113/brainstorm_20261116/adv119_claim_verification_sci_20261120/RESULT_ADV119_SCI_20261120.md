# ADV-119 result: blind verification of twelve decision-driving claims (SCI successor window, 2026-11-20; hypothesis level; no dose; not medical advice; reference genotype class only)

**Answer first.** Of twelve claims (selection and test: `SELECTION_ADV119_SCI_20261120.md`, frozen at commit f58cb7d87731 before any verdict), **2 supported, 4 supported with limit, 0 overturned, 6 abstract only: not verifiable at this depth** (count by script from `VERDICTS_ADV119_SCI_20261120.tsv`; the verifier's and my adjudicated verdicts do not differ). One claim carried a wrong number in my own ledger: the vigabatrin infant MRI figure (C3). One carried a limit that matters to a decision text: the Brown 2016 repeated-dose apoptosis (C1). No priority experiment, arm or preference changes by itself (v3.1 6.22).

**Method.** One fresh delegate (`legend-delegate`, model claude-sonnet-5-5, effort high: stated in the brief, passed on dispatch, read back from its transcript with `session_model_census.py`: 28 turns, high on all 28), given only (claim, source) pairs; report as delivered in `VERIFIER_REPORT_AS_DELIVERED_ADV119_20261120.md`. Routes it reached: the PubMed full-text tool (PMC5214840, PMC11827727, PMC6215509, PMC13395050), ClinicalTrials.gov through a summarising reader (C5, and C10 Table 1: values as the reader returned them, not verbatim); it stopped at reCAPTCHA on three PMC article pages and found Europe PMC XML (500) and render routes closed. No workaround was tried. **Adjudication:** C3 and C1 were checked by me against the full-text XML re-acquired for this task (`pmc_bucket_fetch.py`, scratch, not committed); the verifier's negatives on both were true.

## Per claim
| # | Verdict | What the source says more or less |
|---|---|---|
| C1 Brown 2016 apoptosis, schedule | supported with limit | five of eight regions as printed (P 0.0087 to 0.0472, Mann-Whitney); tests declared one-tailed a priori; no correction across regions stated; repeated-dose exposure not measured; schedule 4 h spacing (Methods), 12 h (Results), "over 24" (abstract); single dose "no significant increase" not zero; striatum not assessable; males |
| C2 Brown 2016 brain values | supported with limit | 330, 1296, 2013 ng/ml of tissue, arithmetic 1.09, 4.27, 6.64 uM; "total", time point and ml-to-g are not in the text; half-life 2.2 to 2.5 h only at 15 and 30 mg/kg |
| C3 vigabatrin infants | supported with limit (numbers corrected) | 35.5 percent = 27 of 76 (raw 31 of 80); 13.5 percent = 7 of 52 pooled controls (23 TSC, 29 non-TSC epilepsy); RR 3.57 multivariable; 13 of 13 resolved; controls' abnormalities resolved too; not specific to vigabatrin or TSC |
| C4 lithium P5 and P15 | abstract only | wording matches; dose, route, LD50, n unread |
| C5 XEN496 | supported | enrolment, arms and stop reason in NCT04639310; adverse events in NCT04912856; non-serious events; 1 of 8 completed |
| C6 ketamine P7 | abstract only | "no effect" is frontal cortex layers II and III; Zou subcutaneous, Soriano intraperitoneal |
| C7 CGP 43487 P5 | abstract only | matches; route, n, tests unread; both olfactory and auditory cues |
| C8 ganaxolone guinea-pig | abstract only | males, 2.5 mg/kg s.c.; no mortality numbers in the abstract; the abstract also reports benefits |
| C9 gaboxadol Angelman | abstract only | zero is the least-squares difference (raw 3.3 and 3.2); 47 against 50 aged 4 to 12; 7 aged 2 to 3 added for safety |
| C10 West 2018 | supported | 11.8 uM frequency EC50; table values; frequency not reduced at 1 and 3 uM; no 10 uM group; kainate-treated adult male rat entorhinal slices |
| C11 Liddiard 2024 | abstract only | no blind route reached the text; my own PMC-page reading stays one reader |
| C12 Harman 2026 | supported with limit | all numbers match; paired t tests, n 9 and 11, crossover against own vehicle; genotype superscript unreadable in the tool |

## Where the changed claims are carried (told by name)
* **IT:** `batch_sci_20261105/map/open_questions_map.tsv` row **WO-26** carries C3 as "35.5 percent of 80 ... against 13.5 percent without the drug" (denominator and control composition now corrected); row **IT46-Q04** carries C1 as "repeated exposure ... raised apoptosis in 5 of 8 regions (a single dose did not)" (add: one-tailed a priori tests, repeated-dose exposure unmeasured); row IT45-Q01 cites the same apoptosis in passing.
* **HE:** `adv098_agent_sheets_he_20261119/BATCH2_Kv7_ezogabine_azetukalner_ICA069673_XE991_HE_20261119.md` (the rodent-exposure bullet and the two dated lines on Brown 2016 carry C1 and C2; the new limits are one-tailed testing, unmeasured repeated-dose exposure, and that "total" is an inference).
* **Mine, corrected by dated lines:** the ledger (V6 and section 0), the adv095 bridge comparative case, the ADV-117 comparison, v3.1 6.22.
* **Not edited here:** `checkpoint_sci_20261120/CHECKPOINT_SCI_CONTINUATION_20261120_P.md` carries the "35.5 percent" and is not edited once hashed (this result supersedes it).

## Weakest answers
The selection is my judgement under ADV's test (twelve of about fifty candidate lines); the six abstract-level claims are untested at full text, and four of them (C4, C6, C7, C8) could only be tested by a route the clients here cannot reach; the verifier's C5 and C10 table values passed through a summarising reader.
