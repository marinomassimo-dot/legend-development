# INV-10 (sz-p, 2026-11-07): seizures, development and function in WOREE, a delta

Non-canonical, public edition, reference genotype class only. Not medical advice; no dose or therapy preference. Receipts staged (suffix 93), not recorded. The external report was not available; corrections answer the brief's description. Files: `evidence.tsv` (26 rows), `proposition_map.tsv`, `questions.tsv`, `queries.tsv`, `receipts/INDEX.tsv`.

## Answer first

1. DATO: no WWOX report records a developmental gain after a seizure response, and none records a sustained, dated, instrumented response. INFERENZA: the causal question is untested, not answered either way. The four propositions stay separate: (a) recovery from seizure control is not demonstrated; (b) some partial or transient responses had no documented progress; (c) the course without the response is unknown; (d) irrelevance of seizure reduction to development, function or quality of life is not demonstrated (`proposition_map.tsv`).
2. Perimeter. DATO: the 36 to 38 children are those exposed to four classes (vigabatrin, a hormonal regimen, the ketogenic diet, cannabidiol) in 14 reports, 6 with both endpoints (`../../batch_sci_20261105/a1_wwox_reports/README.md`). They are not the WOREE population nor all antiseizure drugs, and three further series sit outside it (12 children, 7 children at abstract level, a 50-person parent survey).
3. INFERENZA, one count to correct: of the four "discordant" children, the You 2024 case has an age-referenced statement ("did not reach the milestones expected for her age") and no before/after contrast; it coincides with spasm onset at 8 months, when vigabatrin followed. That is not a documented stall, and a lower age-standardised standing does not show loss of skills. Timed discordant children: three (E03 to E05). The tabulated counts and the INV-10 sentence should say "no progress recorded", not "development unchanged".
4. Vigabatrin case (E01 to E07): early seizures, other drugs, a quiet interval; spasm onset and the milestone statement at 8 months; vigabatrin added; at 11 months no seizures seen at home while video-EEG still recorded events; 13 months no visible seizures. DATO: absence at home is not electroclinical freedom; the authors credit three other drugs for early control. Succession is not causation. The early card and the need already separate the two endpoints.

## Errors of the report, one by one

* "Only lithium": wrong. DATO: ethosuximide was tested in the same Wwox-null paper (one acute provoked-seizure experiment, wild type floor-limited, nothing measured at the channel, E24; limits in `../../ttype_20261107/output/README.md`).
* "Cannabidiol and perampanel never studied or used": three levels. Published exposures exist (cannabidiol in 3 reports; perampanel in two children of one series and one adult; E20, E21, E22, E26). Outcomes attributable to a single compound: none (polytherapy, continuation is not efficacy). Studies designed to evaluate them in WWOX: none found (PubMed gives zero for each term with WWOX but misses table-level mentions; Q02 is a route limit, not an absence). One designed cannabidiol cohort contains three WWOX patients, two responders by its criterion; it was not designed around WWOX.
* d-APV block (`../../nmda_inv05_20261107/output/README.md`): shows dependence on NMDA receptor activity in slices; it does not validate felbamate or perampanel (targets and contexts differ). Not duplicated here.
* Fixed substrate or irreversible course: not supported by narratives and absence of complete responses. A delay before onset (delay from birth in all seven of one series, abstract level) shows a component not explained by later seizures; it does not exclude a further contribution.
* DEE comparisons (E13 to E19, `../../batch_sci_20261105/a2_baseline/README.md`): kept apart. Arm nulls are underpowered (about one chance in four); TSC trials test prevention before onset; UKISS shows a developmental arm difference only in unknown aetiology (abstract); KCNQ2 shows a poor-outcome majority and a possible treatment-choice association, not that seizure control is useless.
* Safety (`../../batch_sci_20261105/b1_whitematter/README.md`): two cases chosen for the abnormality estimate no WWOX-specific risk; the population rate is 18 of 64 imaged children of mixed aetiology. No indication to exclude or change a therapy.

## New information (Stage 1: 2 sources, Stage 2 unused)

* DATO (PMID 39039877, abstract only): 12 children, 2 seizure-free and 9 with continuing seizures at last follow-up, 1 death; drugs and developmental timing not stated (E08, E09). INFERENZA: the two seizure-free children are the first candidates in the record for a sustained response; their development is the datum that would test (a). Full text not reachable (Q08, Q09).
* DATO (PMID 40775196, abstract only, Lennox-Gastaut, not WWOX): caregiver-rated improvement was reached at a seizure reduction of about 31 percent, correlation 0.47 (E10, E11). Bounds (d) from a related disease; the rating is global.
* Consumed by the module (grep): INV-10 combined sentence and the 36 to 38 count, 18 of 64 in the vigabatrin card and work order, the instrumented-response line in the need. Not checked here: other rows of `../../batch_sci_20261105/integration/CONSUMERS.md`.

## Unresolved (NON RISOLTO)

Course of the two seizure-free children; per-compound outcomes; any measure of sleep, comfort, participation, caregiver burden or quality of life in WOREE; direct drug action versus mediation through seizures (E18 is an uncontrolled association).

## Changes proposed

INV-10 and CLAIM 031 sentence: replace "development unchanged" by "no progress recorded"; give timed discordant children as three (E03 to E05); name the perimeter (four classes) and the 12-child series as unread for treatment. Cards: keep benefit columns (seizures clinical and electrographic, acquisition, retention, vigilance and comfort, drug burden, quality of life) separate and empty where unmeasured. Perampanel and ethosuximide: general-activity wording as in `../../aed_compare_it31_20261107/output/README.md`.

## Next investigation of highest value

Q1 in `questions.tsv`: obtain the treatment and course of the two seizure-free children of the 12-child series (full text or published data), and set a within-child continuous score against stratum slopes. One responder with a measured gain would falsify the hypothesis of decoupling; a stable low level would fit the pre-onset component. In silico: the slope baseline; collaboration: the series data.

Depth: 39101447 and 42193054 reopened (text; tables not reopened); reused quotes copied from package tables. Unreachable: 39039877 full text (placeholder page, no challenge, no second tool). OR/parentheses test: `queries.tsv`.
