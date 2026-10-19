# COMMIT CANDIDATE — CC-20261019-SCIENTISTD-G4-VABAM-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d` (stated assumption of the Orchestrator), metabolic batch 2026-10-19 group G4, branch `task/metab-g4-d`.
**context_policy:** `QUESTION_DRIVEN` (named in the analysis note). **Not medical advice.** Class-level statements only.
**target_wm_version:** `WM_v7.20_2026-10-04` · **Change class:** MINOR (an annotation on one claim record; no status, no baseline claim, no working-model block touched).

## Target
`claim_registry_current.md`, record `CLAIM 001` ("Vigabatrin associated with VABAM in WWOX-DEE", `conflicting evidence`): one `replace-within` appending a wave note. Dry run 2026-10-19 with `record_scoped_edit.py apply` on this branch: exit 0, one op, key `CLAIM 001`.

## What the sources say (and do not)
- Sathe 2025 (PMID 39570186; manifest `PMID39570186.json`, receipt `FTR-20261019-39570186-01`): 11 of 11 symptomatic VABAM children had simultaneous hormonal therapy against 40 of 91 without VABAM (p = 0.001); peak dose not associated; causation explicitly not established; disease severity named as a rival explanation; radiologist not blinded to exposure.
- Stevering 2025 (PMID 39641935; receipt `FTR-20261019-39641935-01`): TSC cohort with blinded MRI and pre-treatment scans; 7 of 52 unexposed children had VABAM-like abnormalities; hormonal therapy not associated with the MRI finding (RR 0.94) but associated with symptoms (RR 9.00, eight exposed).
- Neither paper contains a WWOX patient. The WWOX VABAM anchor (`PAPER 003`, PMID 41442931) has no receipt, so whether the WWOX reports involved hormonal co-therapy is not known here. The batch selection file's "(Choi 2026, read)" is incorrect as written.

## Why this is a note and not a status change
The two cohorts disagree with each other on the MRI finding, neither is a WWOX system, and the source that would let the question be asked of WWOX is unread. The safety position in `BLOCK 1` rests on the human WWOX signal against the human WWOX efficacy reports and does not move.

## Op list (`claim_registry_current.md`)
```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 001",
  "old": "Both n = 1 per drug, different genotypes, short follow-up; neither changes the status. Not medical advice.",
  "new": "Both n = 1 per drug, different genotypes, short follow-up; neither changes the status. Not medical advice. **Wave note (2026-10-19, `CC-20261019-SCIENTISTD-G4-VABAM-01`):** two non-WWOX cohorts were read in full for the hormonal-therapy co-factor in VABAM (neither contains a WWOX patient). Sathe 2025 (PMID 39570186, single-centre retrospective, 108 vigabatrin-treated infantile-spasms children, 17 VABAM): all 11 symptomatic cases had simultaneous hormonal therapy against 40 of 91 children without VABAM (Fisher p = 0.001); peak dose was associated with no VABAM class; the authors name disease severity as a rival explanation and the radiologist was not blinded to exposure. Stevering 2025 (PMID 39641935, TSC registry plus prospective cohort, blinded MRI, pre-treatment scans): VABAM-like abnormalities in 7 of 52 children never given vigabatrin; vigabatrin independently associated with VABAM (RR 3.57); hormonal therapy not associated with the MRI finding (RR 0.94) but associated with predefined symptoms (RR 9.00, only eight exposed). The two cohorts disagree on whether hormonal therapy relates to the MRI finding, and neither isolates a mechanism. **The WWOX VABAM anchor (PAPER 003, PMID 41442931) still has no receipt in the ledger, so whether the WWOX reports involved concurrent hormonal therapy is unknown to this repository; no status change.**"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(all 11 symptomatic VABAM cases had simultaneous hormonal therapy | All 11 children with sVABAM were treated with VBG-HT, in comparison to 40 of 91 children without identified VABAM (p = 0.001). | PMID 39570186, Results 3.2 para 1; files/fulltext/PMID39570186_Sathe2025_PMC.xml)
(the authors name disease burden as a possible proxy | it is possible that our identified associations of VABAM with vigabatrin dosage (prior study) or concomitant hormonal therapy (prior and current study) are proxies for a link between VABAM and disease burden | PMID 39570186, Discussion para 2; same file)
(VABAM-like abnormalities occur in children never given vigabatrin | Prevalence of "VABAM-like MRI abnormalities not VGB-related" was, therefore, 13.5% (7/52 patients). | PMID 39641935, Results 3.2.2; files/fulltext/PMID39641935_Stevering2025_PMC.xml)
(hormonal therapy is not associated with the MRI finding in the TSC cohort | Concomitant hormonal/steroid therapy | .94 (.17-2.27) | .92 | PMID 39641935, Table 2 last row; same file)
(hormonal therapy is associated with symptoms in only eight exposed patients | although there were only eight patients treated with hormonal or steroid therapy | PMID 39641935, Results 3.3; same file)
