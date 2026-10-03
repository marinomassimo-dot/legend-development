# COMMIT CANDIDATE — CC-20261003W6-B-CBDRESPONSE-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 6 2026-10-03, branch `task/sci-B-20261003w6`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w6_B.md`).
**Not medical advice.** Class-level statements about published patients only.

## Target
- `research/discovery_ledger_current.md`, record `DL-MECH-030` (the WWOX-DEE cohort record that holds "cannabidiolo: 4/4 lo hanno continuato"): one `replace-within` appending a class-level note on the first genotype-stratified cannabidiol **response** row naming WWOX (PMID 40126049, Table 2).
- Not edited, deliberately: `HYP-20260709-01` in `therapeutic_hypotheses_ledger_current.md` repeats the 4/4 continuation; a `replace-within` there was refused by `record_scoped_edit.py` (records are `###`, the tool resolves level 2 only: `ANCHOR_MISSING`). `DL-MECH-030` already links that hypothesis; the integrator may mirror the note there by hand if wanted.

## What the source says (and does not)
Table 2 row `WWOX (3 pts)`: mean seizure reduction 41.7 % (SD 38.2); ≥ 50 % responder rate 2/3; CGI improvement 2/3 — all **at last follow-up** (minimum 3 months), >99 % purified CBD **added to a median of three ASMs**, retrospective, open-label, seizure diaries/records, CGI-I scored retrospectively. Denominator for each fraction is 3. No allele, zygosity, sex, onset, age at CBD, syndrome, dose, follow-up length or centre is printed for the three. Appendix S1 worsening lists (seizures 15, CGI 19) do not name WWOX. The authors warn rows of two or three may reflect chance.

## Overlap test (counted once)
No held WWOX source is cited. Oliver 2023 (PMID 36779245; four CBD continuers; under PUBLICATION_INTEGRITY_HOLD) shares no named centre with the CBD study. Riva 2022 (PMID 35573960; one case, "CBD oil" ineffective) shares three authors and a contributing centre with the CBD study, but names a different product. Overlap is **undetermined** in both cases (INFERENZA). Rule: the three are one unlinked aggregate; never summed with the 4/4 continuers or the single "CBD oil" case.

## Change class
**MINOR** — an annotation on a discovery-ledger record; no claim status, no working-model block, no consolidated baseline touched.

## Registry need
PMID 40126049 needs `PAPER`/`LIT` identity records — carried by `CC-20261003W6-B-REGISTRY-01` (provisional `PAPER 151`, `LIT-0444`).

## Ordering
Receipt `FTR-20261003-40126049-01` appended before propagation.

## Op list — `discovery_ledger_current.md` (dry run 2026-10-03 with `record_scoped_edit.py apply` on this branch: exit 0, 1 op, key `DL-MECH-030`)
```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-030",
  "old": "Sono pattern di continuazione, non evidenza.",
  "new": "Sono pattern di continuazione, non evidenza. **Wave-6 note (2026-10-03, `CC-20261003W6-B-CBDRESPONSE-01`):** the only genotype-stratified cannabidiol *response* row held for WWOX is PMID 40126049 Table 2 — three WWOX patients on >99 % purified CBD, added to a median of three ASMs, open-label, retrospective: mean seizure reduction 41.7 % (SD 38.2), ≥50 % responders 2/3, CGI-I improved 2/3, all at last follow-up (≥ 3 months); no allele, age, syndrome or follow-up length is printed, and the authors warn that rows of two or three may reflect chance. Not linkable to this cohort's four continuers (no shared centre named; overlap undetermined, INFERENZA). Count once as an unlinked aggregate; do not pool with the 4/4 continuation; not a genotype-specific efficacy result."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(the WWOX row has three patients with mean reduction 41.7 % SD 38.2, responders 2/3, CGI improved 2/3 | WWOX (3 pts) 41.7 (38.2) 2/3 2/3 | PMID 40126049, Table 2 row WWOX; files/fulltext/PMID40126049_CerulliIrelli2025_PMC.xml)
(effectiveness is measured at the last follow-up visit against baseline | Effectiveness outcomes included mean seizure reduction, ≥50% seizure reduction, and seizure freedom at the last follow‐up visit relative to the baseline observation period. | PMID 40126049, Methods, Outcome measures; files/fulltext/PMID40126049_CerulliIrelli2025_PMC.xml)
(CBD was added to existing antiseizure medication | patients were taking a median of 3 ASMs (IQR = 2–4) | PMID 40126049, Results, ASM data and response to treatment; files/fulltext/PMID40126049_CerulliIrelli2025_PMC.xml)
(two- or three-patient rows may reflect chance rather than genotype | in smaller subgroups with only two or three patients, the observed response rates may be influenced by chance or individual patient characteristics rather than the underlying genetic cause | PMID 40126049, Discussion, limitations paragraph; files/fulltext/PMID40126049_CerulliIrelli2025_PMC.xml)
(Table 2 reports fractions, not percentages, for groups of five or fewer | Percentages have been reported only for groups with more than five patients. | PMID 40126049, Table 2 footnote; files/fulltext/PMID40126049_CerulliIrelli2025_PMC.xml)
(the seizure-worsening patients are listed by gene | showing seizure worsening, this occurred in three patients harboring TSC2 pathogenic variants, | PMID 40126049, Appendix S1, Supplementary results para 1; files/fulltext/PMID40126049_CerulliIrelli2025_supplement/EPI-66-2253-s001.pdftotext-layout.txt)
