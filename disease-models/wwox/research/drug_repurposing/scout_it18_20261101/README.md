# IT18 scouting triage of seven candidates (2026-11-01)

Non-canonical research material. Metadata-level triage plus one probe; nothing installed, no third-party raw data tracked (digests only). `decisions.tsv` has the shape of `../scout_it15_p5_20261101/decisions.tsv`, so the radar reads the WATCH rows as reopen conditions. PROTON is handled separately in `../proton_it18_20261101/`. Fields marked "not recorded here" were not captured by the triage actor and are not asserted.

| Candidate | Verdict | Reason |
|---|---|---|
| Chem-PerturBridge | WATCH | no small plain-download perturbation asset found; the subsample option loads the whole file first |
| EuTxGNN | DISCARD | TxGNN again, nearly all predictions are deep-learning scores, no WWOX/WOREE path among 5,007 files |
| DrugClaw/DrugAudit | DISCARD | probe below; no licence; benchmark gold produced by the system it ranks |
| CLAMP | WATCH | GPL-3 code, separate weights clause, no assay-text task to score it on |
| OpenOncology | DISCARD | the module already has its evaluation lessons |
| DeepPurpose | DISCARD | binding prediction gives no action direction, which is the matching gap |
| awesome-computational-biology | OPTIONAL | discovery list only (CC0); each project has its own licence |

## The one probe (DrugAudit evidence file)
`drugaudit_probe.py` (stdlib only, safe `--help`, prints counts, copies no item text). `evidence.xlsx` at revision bc7b93ede215 (sha256 9df3f3d9...ca18ea4) was read in the scratch area only: 3,961 items, about 500 per source. It names 4 of the 186 universe compounds of the P4 matching task (gabapentin, pregabalin, lithium carbonate, ruxolitinib) and 2 of the 21 card compounds; each set has 2 items about mechanism or action; 8 of 508 ChEMBL items do, phrased "according to ChEMBL", the source the module already uses. Matching was on ChEMBL preferred names only, so counts may be slightly low. Output: `probe_drugaudit_output.txt`. Limit: one probe, name matching only; it does not test DrugAudit's own answer-qualification method.

## Scope notes added in IT19 (the decisions above were stated more widely than their checks)
- "No WWOX/WOREE in the file paths" (EuTxGNN) is a statement about names; the contents were not searched.
- A discard is for the question tried (here the IT18 matching question), not general uselessness; reopen conditions are in `decisions.tsv`.
- A triage on metadata is not a trial; only the DrugAudit evidence file was probed, and not DrugAudit's answer-qualification method.
- A licence file not found or not read is not a prohibition; nothing was copied, and terms must be read before any reuse.
- PROTON stays discarded for the current question and BioPathNet in WATCH within their documented limits; neither was reopened.
