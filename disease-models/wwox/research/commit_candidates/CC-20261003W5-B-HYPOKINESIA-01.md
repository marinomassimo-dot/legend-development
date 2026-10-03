# COMMIT CANDIDATE — CC-20261003W5-B-HYPOKINESIA-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 5 2026-10-03, branch `task/sci-B-20261003w5`.
**context_policy:** `SOURCE_FIRST` — first pass written from the sources before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w5_B.md`).
**Not medical advice.** Class-level statements about published genotypes only.

## Target
`dismissal_ledger_current.md` · new `DIS-031` (provisional number; append at end of file).

## Finding
The only review in LEGEND's reach that makes a WWOX-specific movement-phenotype claim (PMID 33919646) builds it from five patients of one cohort (Piard 2019), and its "hypokinesia" is the primary's "poor spontaneous movements" row re-labelled. The primary's own "Movement disorder" row for those patients lists dystonia, myoclonus, startle, pedalling/boxing, limited voluntary movement or "no". It adds no patient and no independent observation. Independent hypokinesia observations in held sources are the 2026 L239R case report (`PAPER 145`) and one R54* child of `PAPER 119`.

## Change class
**MINOR** — a dismissal entry (negative claim) with its revival trigger; no claim status or block change. It narrows a review-level sentence that no registry record currently cites.

## Op list — `dismissal_ledger_current.md` (record-scoped; dry run 2026-10-03 with `record_scoped_edit.py apply` (no `--apply`) on main 48f1fe9 (branch base; no registry file changed on the branch): exit 0, 1 op(s), anchors ['EOF-append'])

```json
[
 {
  "op": "append",
  "text": "\n### DIS-031 — «A neonatal-onset hypokinetic movement disorder is a WWOX-specific feature (PMID 33919646)» → ⏸️ **NOT SUPPORTED AS AN INDEPENDENT OBSERVATION**\n- **PREMISE: DATO** (2026-10-03, `CC-20261003W5-B-HYPOKINESIA-01`, intake wave 5, Scientist B; read at source under `context_policy: SOURCE_FIRST`). The review [[paper_registry_current#PAPER 159]] states that the hypokinetic movement disorder 'was described from the neonatal period only, with WWOX pathogenic variants' and calls it 'highly suggestive for WWOX-related disorders'. Every WWOX datum in it comes from one source, [[paper_registry_current#PAPER 117]] (Piard 2019): its Table S1 lists six genotypes, each matching Piard patients 1, 2, 3, 4, 9 and 11, and counts 'Hypokinesia: 5'.\n- **What the primary records for those six** (Piard Supplemental Table 1, read at source): the 'Movement disorder' row reads pedalling and boxing possibly non-epileptic (1), **no** (2), dystonic upper-limb movements (3), myoclonus and dystonic upper-limb movements (4), limited voluntary movement (9), brief involuntary and startle movements (11). The separate 'Poor spontaneous movements' row is yes for 2, 3, 4, 9 and 11 — five. The review's five are that row, re-labelled as a hypokinetic movement disorder. The only Piard patient whose movement disorder is written 'hypokinetic movements' (patient 8) is not among the six. Piard reports poor spontaneous movements in 17 of 19 patients of the whole cohort.\n- **Boundary:** this does not show that hypokinesia is absent or uninformative in WWOX-DEE. Independent observations exist in held sources — the 2026 L239R case report ([[paper_registry_current#PAPER 145]]) and one R54* child of [[paper_registry_current#PAPER 119]] — and the review names its own recognition bias. What follows is narrower: **the review adds no patient and no independent observation, and its specificity claim compares descriptive vocabularies across source papers rather than measuring motor poverty against other profoundly impaired infants.**\n- **`REVIVAL_TRIGGER`:** a series that scores spontaneous movement or a defined hypokinetic sign with the same instrument in WWOX-DEE and in other early-onset DEEs of comparable severity, or WWOX patients with neonatal hypokinesia documented by a movement-disorder examination rather than inferred from motor poverty.\n"
 }
]
```

## Registry records needed
`PAPER 159` (created by `CC-20261003W5-B-REGISTRY-01`); `PAPER 117`, `PAPER 119`, `PAPER 145` exist.

### LOCATOR TRIPLES FOR BLIND AUDIT
(the review states the neonatal hypokinetic MD occurs only with WWOX | The rate of hypokinetic MD was low, and was described from the neonatal period only, with WW domain containing oxidoreductase (WWOX) pathogenic variants. | PMID 33919646, Abstract; files/fulltext/PMID33919646_Spagnoli2021_PMC.xml)
(the review's WWOX section is built from 5 of 20 cases of one cohort | 5/20 cases had neonatal-onset epilepsy with associated MD. | PMID 33919646, Results 3.4.1; files/fulltext/PMID33919646_Spagnoli2021_PMC.xml)
(the single cited source is Piard 2019 | The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature. | PMID 33919646, reference 46; files/fulltext/PMID33919646_Spagnoli2021_PMC.xml)
(the review's Table S1 counts hypokinesia in five WWOX patients | esia: 5 | PMID 33919646, Table S1 page 9, WWOX row MD-semiology cell (rendered page prints 'Hypokinesia: 5'); files/fulltext/PMID33919646_Spagnoli2021_supplement/Table_S1.txt)
(Piard's movement-disorder row records 'no' for one of the review's six | Movement disorder | PMID 30356099, Supplemental Table 1, row 'Movement disorder', column Patient 2 ('no'); files/fulltext/PMID30356099_Piard2019_supplement/41436_2018_339_MOESM1_ESM.xlsx)
(Piard writes 'hypokinetic movements' only for patient 8, who is not among the review's six | hypokinetic movements | PMID 30356099, Supplemental Table 1, row 'Movement disorder', column Patient 8; files/fulltext/PMID30356099_Piard2019_supplement/41436_2018_339_MOESM1_ESM.xlsx)
(Piard reports poor spontaneous movements across most of the cohort | Poor spontaneous movements were reported in 17 of 19 (89%). | PMID 30356099, Results, neurodevelopmental data; files/fulltext/PMID30356099_Piard2019_PMC_2026-09-27.xml)
(the review names a recognition bias | However, as hyperkinetic MD might be easier to recognize, a potential bias cannot be completely excluded. | PMID 33919646, Discussion; files/fulltext/PMID33919646_Spagnoli2021_PMC.xml)
