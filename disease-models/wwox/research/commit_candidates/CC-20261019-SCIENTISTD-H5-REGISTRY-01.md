# COMMIT CANDIDATE — CC-20261019-SCIENTISTD-H5-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d` (stated assumption of the Orchestrator), interventions wave 2026-10-19 group H5, branch `task/INTERV-H5-D-20261019`.
**target_wm_version:** `WM_v7.20_2026-10-04` · **Change class:** MINOR (registry identity records and one queue note; no claim status and no working-model block changes).
**Not medical advice.** Class-level statements only. **Every row is a substitute, labelled NOT WWOX EVIDENCE: none carries a WWOX patient or a WWOX measurement except the Su 2026 row (cell culture).**

## Target and need
Sixteen lot papers had no registry record at the start (`registry_records.py get --pmid` returned `NO RECORD MATCHED`). The integrator needs `PAPER` and `LIT` identity records so the staged receipts have something to attach to. Provisional numbers are left to the integrator. Su 2026 (PMID 41677633) already has a record; its row adds the re-read receipt only.

| PMID | Short title | Source type | Model | Transferability | Role (one line) | Receipt |
|---|---|---|---|---|---|---|
| 36044864 | Yuskaitis 2022 DEPDC5 and fasting | primary, mouse and rat neurons | neuron-specific Depdc5 knockout | T3 | Fasting protection lost in the knockout despite lower glucose and higher ketones | FTR-20261019-36044864-01 |
| 25814935 | Phillips-Farfan 2015 caloric restriction and kindling | primary, rat | young Wistar, 15% restriction | T3 | Threshold up, kindling rate unchanged, pS6 and pAKT lower, glucose and ketones unchanged | FTR-20261019-25814935-01 |
| 35134125 | Salvati 2022 hypoglycaemia and AMPK | primary, rat and mouse | absence-epilepsy models | T3 | Fasting and insulin worsen spike-wave seizures; main text and Table S1 disagree on a p value | FTR-20261019-35134125-01 |
| 42360174 | Hahn 2026 fasting with MCT | crossover pilot | human adults | T3 | No significant difference; Kaplan-Meier by start sequence; one seizure-free IF-alone participant | FTR-20261019-42360174-01 |
| 40589985 | Sun 2025 neonatal hypoglycaemic rats | primary, rat | pups, insulin model | T3 | Higher later PTZ score; reporting inconsistent (n, t statistics, glucose threshold) | FTR-20261019-40589985-01 |
| 40119223 | Garg 2025 neonatal hypoglycaemia thresholds | narrative review | human newborns | T3 | No consensus threshold; correction issued; unit mismatch in Figure 3 | FTR-20261019-40119223-01 |
| 42638834 | Sobrinho 2026 Glut1-DS cohort | retrospective cohort | human SLC2A1 | T3 | Ketogenic therapy in 85%; unvalidated score; internal numeric inconsistencies | FTR-20261019-42638834-01 |
| 36117414 | Dienel 2023 glycogen in epilepsy | hypothesis review | rodent and human | T4 | Starved-rat glycogen non-recovery; no GSK3 or WWOX mention | FTR-20261019-36117414-01 |
| 38681648 | Tao 2024 Wernicke after glucose | case report, n = 1 adult | human | T4 | Temporal association only; no thiamine level | FTR-20261019-38681648-01 |
| 42087252 | Funayama 2026 parenteral dextrose refeeding | retrospective cohort | human adults, anorexia nervosa | T4 | Dextrose tied to magnesium and calcium falls; not phosphorus; no thiamine mention | FTR-20261019-42087252-01 |
| 39871710 | Abbas 2025 pediatric enteral refeeding | retrospective cohort | human children | T3 | Refeeding syndrome 10.4% under a 10 kcal/kg/day start with thiamine and phosphorus | FTR-20261019-39871710-01 |
| 42384016 | Trico 2026 MCT ketones in type 1 diabetes | tracer study and pilot RCT | human adults | T4 | Memory accuracy ceiling; BHB below 0.5 mmol/L; relative-versus-absolute ketone oxidation | FTR-20261019-42384016-01 |
| 41069084 | Burst 2026 hyponatraemia, oedema, ODS | retrospective cohort | human adults | T4 | Oedema 0.5%, ODS 1.3%; water excess and low-solute diets in case lists | FTR-20261019-41069084-01 |
| 40944047 | Ziaka 2025 fluids in TBI | narrative review | human adults | T4 | Hypotonicity and fluid balance statements; no dextrose mention | FTR-20261019-40944047-01 |
| 39861362 | Tesser 2025 parenteral nutrition preterm | qualitative review | human preterm | T4 | Early aggressive parenteral energy: uncertain benefit; glucose rates printed | FTR-20261019-39861362-01 |
| 36235546 | Morris 2022 enhanced PN RCT | pilot RCT | human preterm | T4 | No benefit; slower P100 that vanishes after enteral adjustment | FTR-20261019-36235546-01 |
| 41677633 | Su 2026 (re-read) | primary, cell culture | Wwox-null MEFs, SCC-15, HeLa | T2 | Serum-free stress; null cells resist death; ROS rise in both; no glucose manipulation | FTR-20261019-41677633-03 |

## Queue and register notes
- Correct the interventions selection file's description of PMID 36117414: the text never mentions GSK3 (string count 0), so the "links H5 to the GSK3B arm" remark does not come from this paper.
- Correct its description of PMID 42087252: the paper never mentions thiamine (string count 0); the thiamine question is answered only by 38681648 (one case) and 39871710 (a protocol).
- Carvalho 2022 (PMID 35984507) remains `partial_fulltext_read`; the 2026-10-19 extract of its glucose conditions is described in the analysis note section 6 and is not a read.

## Discovery-ledger proposals (not appended)
Leads L1-L3 of the analysis note (`IPOTESI`), each with a falsifier in the note.
