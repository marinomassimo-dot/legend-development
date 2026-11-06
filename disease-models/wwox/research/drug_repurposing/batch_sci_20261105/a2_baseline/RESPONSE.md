# Author response, package A2 (`sb-a2`), correction round of 2026-11-06

Responds to the blind locator audit (`verify/audit_A2/audit_A2.tsv`, `audit_A2_README.md`; 43 triples) and the adversarial review (`verify/review_A/review_A.md`, `review_A.tsv`; statements A2-D01 to A2-D10, A2-MI-*, and the cross-package points XP-A to XP-F). Every finding below is answered ACCEPTED or DISPUTED, with the evidence and the place where it changed. No finding is disputed in substance. Four qualifications are set out in section 3. Not medical advice.

Files changed, all inside `a2_baseline/`:

* `README.md`: decision lines 1-5, 7, 8, 10; sections 1.1-1.5, 2, 3, 4, 5, 6, 7.
* `evidence_a2.tsv`: every row's depth label; content of A02, A06-A11, B02, B05, B06, B12, B13, C01-C05, D01, D05, D07, D09-D11; new row D14.
* `module_inputs.md`: INV-10, work order wording, CLAIM 031, registry items 1 and 6.
* `queries.tsv`: wording of Q04 and the route rows; new rows R23, R24, M03, M04.
* `receipts/`: propositions in `FTR-20261105-31929713-22` and `FTR-20261105-24225340-22`; `INDEX.tsv` dated.
* This file.

Event ids, reading times and DOIs of the receipts are unchanged.

## 1. Blind locator audit: 43 triples

| Triple | Audit verdict | Response | Change and place |
|---|---|---|---|
| A2-A01 | SUPPORTED | ACCEPTED | depth label normalised to `abstract_only`; access note moved to `design_limits`; a country abbreviation removed from `population` (no country names) |
| A2-A02 | SUPPORTED | ACCEPTED | `effect_on_development` now says no difference demonstrated, interval includes the about 3.0 points full mediation predicts (review A2-D01) |
| A2-A03 | SUPPORTED | ACCEPTED | depth label only |
| A2-A04 | SUPPORTED | ACCEPTED | depth label; access note moved |
| A2-A05 | SUPPORTED | ACCEPTED | depth label; access note moved |
| A2-A06 | SUPPORTED, paraphrase noted | ACCEPTED | "confined to" replaced by "the VABS benefit of steroid allocation was in children with no identified aetiology" |
| A2-A07 | SUPPORTED, stratification by hormone omitted | ACCEPTED | `design_limits` adds the hormone stratification |
| A2-A08 | SUPPORTED | ACCEPTED | `effect_on_development`: undemonstrated difference, printed sign, power 0.24 |
| A2-A09 | SUPPORTED, 229/129 printed for the seizure outcome | ACCEPTED | `n_per_arm` and `effect_on_symptomatic` rewritten; decision line 2 and README 1.2 carry it |
| A2-A10 | SUPPORTED, five categories inferred | ACCEPTED | `intervention_arms` and `n_per_arm` say the categories are inferred from 4 between-group degrees of freedom |
| A2-A11 | UNDERSHOOT | ACCEPTED | see the note after this table |
| A2-A12 | SUPPORTED | ACCEPTED | "full text not attempted" moved to `design_limits` |
| A2-B01 | SUPPORTED | ACCEPTED | depth label `partial_fulltext`; sections read moved to `design_limits` |
| A2-B02 | SUPPORTED, 72.0% computed | ACCEPTED | `design_limits` and README 1.3 say "computed from Table 1" |
| A2-B03 | SUPPORTED | ACCEPTED | depth label; decision line 4 and module_inputs say the 0 of 49 is over all genetic children, not a responder rate (review A2-D04) |
| A2-B04 | SUPPORTED | ACCEPTED | depth label |
| A2-B05 | SUPPORTED, 61 vs 62 recorded | ACCEPTED | `design_limits` states the Table 2 vs Tables 3-4 counts; decision line 3 carries them |
| A2-B06 | SUPPORTED, Table 4 the better anchor | ACCEPTED, anchor kept | see the note after this table |
| A2-B07 | SUPPORTED, RR 4.2 point verified | ACCEPTED | no change needed |
| A2-B08 | SUPPORTED | ACCEPTED | depth label |
| A2-B09 | SUPPORTED | ACCEPTED | depth label |
| A2-B10 | SUPPORTED | ACCEPTED | access note moved |
| A2-B11 | SUPPORTED | ACCEPTED | access note moved |
| A2-B12 | SUPPORTED, comparator dropped; guideline retired | ACCEPTED | `association_between_endpoints` carries both comparative sentences; `design_limits` says the guideline is flagged retired in its PubMed title |
| A2-B13 | OVERSHOOT | ACCEPTED | see the note after this table |
| A2-C01 | SUPPORTED, text-vs-table discrepancies | ACCEPTED | see the note after this table |
| A2-C02 | SUPPORTED | ACCEPTED | `design_limits` adds 19 of 27 placebo infants moved to open label and the hazard ratio interval, attributed to the audit; depth label `reused_prior_complete_read` |
| A2-C03 | SUPPORTED, untested counts and p 0.0495 not carried | ACCEPTED | `design_limits` adds the 36-month drug-resistance counts, the subdomain p 0.0495 (also in the module manifest, entry 7) and the adaptive composite against the drug |
| A2-C04 | SUPPORTED, group sizes printable | ACCEPTED | `n_per_arm` filled from the audit's reading of Table 2, attributed (not re-read here); TSC1 enrichment added |
| A2-C05 | SUPPORTED, PubMed types it Case Reports | ACCEPTED | `design_limits` |
| A2-D01 | SUPPORTED, 13/17 vs 14 | ACCEPTED | `design_limits` states both counts; checked in my own text of the abstract and Results |
| A2-D02 | SUPPORTED | ACCEPTED | depth label |
| A2-D03 | SUPPORTED | ACCEPTED | depth label |
| A2-D04 | SUPPORTED | ACCEPTED | depth label |
| A2-D05 | OVERSHOOT | ACCEPTED, with a refinement | see the note after this table |
| A2-D06 | SUPPORTED | ACCEPTED | depth label |
| A2-D07 | SUPPORTED, "discordance" is the package's label; D06 concordant; floor effect | ACCEPTED | `association_between_endpoints` rewritten as two separately reported trends; floor effect in `design_limits`; README 1.5 |
| A2-D08 | SUPPORTED | ACCEPTED | access note moved; the row says "a national cohort" |
| A2-D09 | SUPPORTED, Table 3 sums to 20 vs 21; "Normal 13 (45%)" | ACCEPTED | `design_limits`; both checked in my own text of Tables 2 and 3 |
| A2-D10 | SUPPORTED, 14 vs 13; p attached to the three-category row | ACCEPTED | `design_limits`; README 1.5 "(14 in Table 2)" |
| A2-D11 | SUPPORTED | ACCEPTED | `association_between_endpoints` now carries the adjustment as the abstract's assertion (review A2-D08) |
| A2-D12 | SUPPORTED | ACCEPTED | access note moved |
| A2-D13 | SUPPORTED | ACCEPTED | access note moved |

**A2-A11 (UNDERSHOOT).** The row now follows the audit's wording: the commentary restates A07 and A08 with numbers and A09 without numbers. The anchor quote is now the restating sentence. `design_limits` records that the commentary additionally asserts, as the commentators' opinion, a treatment preference (not reproduced here, under the no-clinical-preference rule) and that combination therapy may enhance 18-month outcomes, which the trial's null does not support. It also records that the statement "were quickly given vigabatrin" sits in that editorial passage and is not verified as trial protocol. README 1.1 is rewritten to match, and the receipt `FTR-20261105-31929713-22` now labels that locator as an editorial passage.

**A2-B06 (anchor kept).** The audit's point stands, and `design_limits` now says that the anchor carries the overall 76% and that the responder split comes from the Table 4 cells (22, 40, 5, 47). I kept the abstract anchor. In the XML, Table 4's cells are separate elements inside a paragraph, so no contiguous source string exists to quote. The cells are stated in `association_between_endpoints`, and the audit verified them.

**A2-B13 (OVERSHOOT).** `association_between_endpoints` is replaced by the audit's wording, keeping the hedge "might", the comparator and "the same study". `transfer_conditions` no longer says UKISS was the only randomised source of developmental data; it says "pointer to UKISS as the randomised source of the developmental statement".

**A2-C01 (text-vs-table discrepancies).** `design_limits` carries the open-label drug-resistance and neurodevelopmental discrepancies, attributed to the audit because this package did not re-read the trial. The depth label is now `reused_prior_complete_read FTR-20261021-33180985-01 (not re-read by this package)`, and the row says the trial tests prevention, not response.

**A2-D05 (OVERSHOOT).** The development and association fields are rewritten as tendencies:

* severe psychomotor delay 26% vs 0%, with no test reported;
* last DQ/IQ not significantly different (53.4 vs 42.9, lower in SCN1A-negative);
* the authors' own wording, "tend to".

Refinement: Table 1 prints ataxia or gait disorder in 4 (44%) of the SCN1A-negative group (p .017), while the text says gait was considered normal in 44% of that group. The row states both readings. README 1.5 and the receipt `FTR-20261105-24225340-22` (proposition relabelled as a tendency) are aligned.

## 2. Adversarial review: statements for package A2

| Statement | Verdict | Response | Change and place |
|---|---|---|---|
| A2-D01 | NARROW | ACCEPTED | see the note after this table |
| A2-D02 | HOLDS | ACCEPTED | the audit's A09 caveat (group sizes printed with the seizure outcome) is now inside line 2 |
| A2-D03 | NARROW | ACCEPTED, with a precision | see the note after this table |
| A2-D04 | HOLDS, with a condition | ACCEPTED | the condition is now in line 4, README 1.3 and `module_inputs.md`: 0 of 49 is over all genetic-aetiology children and is not a responder rate. Line 4 also cites the new row D14 |
| A2-D05 | HOLDS, instrument condition must travel | ACCEPTED | line 5, README 1.3 and section 3 condition 4, and `module_inputs.md` now say that the comparison with WWOX reports holds only as a binary |
| A2-D06 | HOLDS | ACCEPTED | no change; the reviewer's recomputation (2.385, 1.911, 0.239) matches mine |
| A2-D07 | NARROW | ACCEPTED | line 7 rewritten from the review's wording, separating depths: four abstract-level associations, one partial-full-text test that found lead time not independent of aetiology. README 1.4, 2 and 3 condition 3 aligned |
| A2-D08 | NARROW | ACCEPTED | see the note after this table |
| A2-D09 | HOLDS | ACCEPTED | no change |
| A2-D10 | NARROW | ACCEPTED | see the note after this table |
| A2-MI-INV10 | NARROW | ACCEPTED | `evidence_available` bullet 2 replaced by the review's corrected wording (no demonstrated difference, power about one in four; TSC trials of pre-onset prevention); depth labels added to every bullet and to the transfer conditions; the underpowered-null condition added |
| A2-MI-WORKORDER | HOLDS | ACCEPTED | no substantive change; wording aligned with A2-D10 ("genetic and structural DEEs", binary comparison) |
| A2-MI-CLAIM031 | NARROW | ACCEPTED | see the note after this table |
| A2-MI-REG | HOLDS | ACCEPTED | item 1 now says the eight sources were read at partial full-text depth (receipts `partial_fulltext_read`); item 4 (the correction to the brief) is kept; item 6 is added for PMID 42190144; nothing removed |
| XP-A | NARROW | ACCEPTED for the A2 side | the binary-only comparison and the instrument difference are carried into line 5, README 1.3 and 3, and `module_inputs.md`. The combined INV-10/CLAIM 031 sentence spans A1 and is the Orchestrator's to place |
| XP-B | NARROW | not addressed to A2 | concerns A1 (CLAIM 042, ketogenic diet) |
| XP-C | NARROW | not addressed to A2 | concerns A1 (the CLAIM 031 qualifier); A2 still leaves the qualifier unresolved and says so |
| XP-D | NARROW | not addressed to A2 | concerns A1 (imaging) |
| XP-E | NARROW | not addressed to A2 | concerns A1 (cohort overlap) |
| XP-F | NARROW | ACCEPTED | see the note after this table |
| Review section 6, A2: arm-level nulls underpowered, missing from the conditions | (finding) | ACCEPTED | README 3 now opens its breakers with it; `module_inputs.md` INV-10 transfer conditions carry it |
| Review section 8, A2: missed source PMID 42190144 | (finding) | ACCEPTED | see the note after this table |
| Review section 9, A2 section 4: items 1 and 2 must say partial | (finding) | ACCEPTED | item 1 rewritten; item 2 concerns abstract-level receipts and needed no change |
| Review section 10: table labels `full_text` against eight partial receipts | (finding) | ACCEPTED | as XP-F |

**A2-D01 (NARROW).** Line 1 is rewritten from the review's corrected wording. It now says:

* no developmental arm difference was demonstrated despite a 15-19-point early cessation difference;
* the comparisons had about one chance in four of detecting the mediated difference, so this is an undemonstrated difference, not a shown absence;
* EPISTOP and PREVeNT test prevention before onset, not response after onset;
* PREVeNT's spasm comparison was neither prespecified nor tested.

Rows A02 and A08 (effect fields), C01-C02 (`design_limits`), README 1.1, the README 3 breakers and `module_inputs.md` INV-10 bullet 2 are aligned.

**A2-D03 (precision).** Line 3 now carries the discrepancy. The review's "66% on the smaller denominator" assumes the numerator 40 stays the same with 61 responders, but the 40 is printed only in Table 4, which counts 62. The line therefore says "about 66% on the smaller if the numerator is unchanged". Row B06 says the same.

**A2-D08 (NARROW).** Line 8 is rewritten: the KCNQ2 adjustment is carried as the abstract's own assertion, and the model is said to be unreadable from an abstract. The line now names the depth of each of its three sources: two abstract-level, one partial full text. Row D11 and README 1.5 and 2 are aligned.

**A2-D10 (NARROW).** Line 10 is rewritten:

* Row 1 fires for the genetic and structural strata only, because rows A03 and A05 record a randomised developmental difference in the unknown stratum (abstract level). The departure from the pre-registered condition is declared.
* Row 2 fires.
* Row 3 does not fire.

`module_inputs.md` follows: `decisive_uncertainty` and the work-order wording now say "genetic and structural DEEs", and the label "generic-DEE baseline" is renamed "non-WWOX DEE baseline" so that it cannot be read as a claim about DEE generally.

**A2-MI-CLAIM031 (NARROW).** The proposal is kept unchanged in substance. The narrowing now reads "coupled in randomised data read at abstract level (the 14-month and 4-year reports of one trial, in infants with no identified aetiology)". The quote is labelled abstract level, and each source of the evidence-boundary line carries its depth: all three are partial full text. A binary-only caveat is added.

**XP-F (NARROW).** Every `source_depth` cell now uses the closed vocabulary:

* `abstract_only` (21 rows);
* `partial_fulltext` (19 rows, including the short commentary, whose receipt says `partial_fulltext_read`);
* `reused_prior_complete_read FTR-... (not re-read by this package)` (4 rows for the three TSC trials).

Sections read and access notes moved to `design_limits`. README states that no source was read by this package to complete depth, and `queries.tsv` wording is normalised ("read at partial full-text depth").

**Review section 8 (PMID 42190144).** Row D14 is added at abstract level, with no receipt, as instructed (only the PubMed record was read; no PMC record exists). I made it `context` rather than `support`; see section 3 (c). It also matters for A1: its abstract names WWOX among the cohort's novel gene associations. The module already holds that abstract in discovery ledger entries DL-MECH-001, DL-MOL-001 and DL-REPO-001. Two older claims on the PMID (scientist-b 2026-10-20, scientist-a 2026-10-23) are not live work here. New `queries.tsv` rows R23, M03 and M04 record this, and `module_inputs.md` item 6 proposes the queue and identity entries.

## 3. Qualifications (nothing disputed in substance)

**(a) A2-D03 arithmetic.** See the A2-D03 note in section 2. The numerator of the smaller denominator is not printed, so "66%" is conditional.

**(b) A2-B06 anchor.** See the A2-B06 note in section 1. The suggested Table 4 anchor is not a contiguous source string in the XML.

**(c) Role of D14.** The review says this cohort "points the same way as A2's line 4 and would strengthen it". It strengthens the part "a favourable outcome is absent" (profound intellectual disability in most, irrespective of genotype). It does not strengthen "whatever the response", because the abstract does not cross seizure outcome with development. Counting it as `support` would overstate it, so it is `context`.

**(d) Country names.** The correction round lists "no country names". Every prose occurrence has been removed: a country abbreviation in row A01, and another in `module_inputs.md` and in the Q04 note of `queries.tsv`. One literal remains: the Q01 search string in `queries.tsv`. It is the official full name of the UKISS trial and contains a country name. A query log must reproduce the exact string that was run, so I kept it there only. `README.md` refers to Q01 by description, and elsewhere the trial is "UKISS". The public release gate passed with this literal in place (run of 2026-11-05) and again in this round (section 4). If the rule admits no exception, the Orchestrator can replace that single cell with "the full name of UKISS as a phrase search", at the cost of reproducibility. "Europe PMC" appears only as the name of a literature service, not as a country.

## 4. Re-validation (2026-11-06)

* **`evidence_a2.tsv`:** 45 lines, 20 fields on every line. Every quote is verified verbatim against its source text (full-text conversion, PubMed record or module manifest snippet) and is at most 25 words. No tab or newline inside a field. None of the forbidden phrases, no country names, no per-weight dose notation, no administered-dose number, no e-mail-like string.
* **`queries.tsv`:** 48 lines, 6 fields each.
* **`receipts/INDEX.tsv`:** 25 lines, 5 fields each.
* **Receipts:** all 24 pass `staged_receipt_check.py --check-doi` at 2026-11-06T07:10:20Z, dated in `INDEX.tsv`. No new receipt was created: event ids keep suffix 22 and their 2026-11-05 date part.
* **Release gate:** `scripts/public_release_gate.py` (staging mode, read-only, report outside the repository) was re-run after these edits. The result is in the final message to the Orchestrator.
