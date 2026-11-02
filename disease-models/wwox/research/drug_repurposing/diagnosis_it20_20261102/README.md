# IT20 P0 - diagnosis of the open gaps (2026-11-02)

Non-canonical research material; not medical advice. Baseline: `main` = `development/main` = `dba013f3` (code `2ebb5710`, CI success; the record-only commit's CI was running), dashboard served and verified, folder trust accepted, one worktree. This table supersedes `../diagnosis_it18_20261101/README.md` as the latest diagnosis; rows IT19 resolved are dropped, not reopened. The radar derives its questions from the rows below (it reads the latest `diagnosis_it*` directory).

| Stage | Declared | Implemented | Executed | Advantage measured | Validation missing |
|---|---|---|---|---|---|
| Provenance through intermediaries | R2/R5 | DGIdb rows carry a claim source; IT19 group guard on the direct ChEMBL path | yes | none | four T-type entries (terodiline, suloctidil, phloroglucinol, bepridil) get a direction through DGIdb copies of the ChEMBL group action; original source, republishing source, ChEMBL release and target level are not carried together |
| Specific pharmacological evidence | R5 | group guard abstains when fewer than half of a group record's components are module targets | yes | 3 of 4 changed pairs right | the guard holds back bepridil although Cav3.2 pharmacology exists (IC50 0.4 uM at -70 mV, PMID 15855830); no usable link from a specific measurement to the engine without a name exception |
| Matching evaluation | R3/R7 | rule-selected reference of 32 pairs (17 determinate), IT18 locked comparison | yes | no disagreement found, no superiority shown or excluded | duplication of evidence, improper transfer between molecules and unknown turned into negative are tested by fixtures but not by a contrasting-case comparison before and after the IT20 change |
| WWOX-guided hypothesis generation | R6 | needs, qualifications, target-first searches | yes | WWOX contribution zero on directed needs (IT18) | no comparison of an external-only search against the WWOX-qualified one at equal usable universe on an open question |
| Public presentation of evidence | R10 | online shareable view with direction and abstention block | yes | none | the first screen is technical; the path from a biological thread to a compound and its missing measurement takes many steps; funnel units are not shown as one reproducible chain |
| Radar | R9 | plan derived from diagnosis, tables, never-asked rule (IT19) | simulated | wait time simulated 24 to 21 days | no production observation after the change; questions about provenance, republishing sources and evidence presentation are not yet in the plan |
| Continuity | R12 | self-check cron; monitor; per-job memory cap | yes | one resume after a controlled stop observed (manual path, IT20 P1) | no delivery by the scheduled hourly cron to a dead session observed |

## Questions chosen for IT20
1. Can a republished ChEMBL group action keep its original source, release and target level through DGIdb without excluding specific documented records?
2. Can a specific measurement (Cav3.2 pharmacology) reach the engine through the existing qualification structures, without a name list?
3. Does the WWOX-qualified search change a decision relative to an external-only search at equal usable universe?
4. Can a reader of the public page go from a biological thread to a compound, its support, its counter-evidence and its missing measurement in few steps?
