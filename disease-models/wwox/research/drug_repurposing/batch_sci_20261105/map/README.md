# Map of the open questions of the Drug Repurposing module (sb-map, 2026-11-05)

Non-canonical research material, not medical advice; no dose, schedule or treatment preference appears. Public edition, WWOX-DEE reference genotype class; no individual-level record. Read-only analysis for the Orchestrator of task `ORCH-SCIBATCH-DR-20261105`. Nothing outside this directory was edited, no receipt was staged, nothing was committed. Papers were not read to build the map; where a status needed a fact, a status probe (open-access flag, HTTP code, identifier search) was run and is listed in `probes_run.tsv`.

## Answer first

1. DATO: the map has **115 rows**, one per distinct open question; 160 source items (15 work-order needs, 10 investigations, 18 uncarded items, 34 reopen rows, 3 challenges, the IT30 steps and conditional questions, residues, radar items, roadmap lines) map onto them with none dropped (`source_items_index.tsv`).
   - By kind: wet_lab_measurement 28, literature_executable 17, data_access_blocked 11, engine_or_infrastructure 28, decision 8, monitor 23.
   - By status: OPEN 92, IN_PROGRESS 5, CLAIMED_THIS_BATCH 3, CONCLUDED 14, SUPERSEDED 1.
   - Published on: main 86, not_applicable 2, task/it29 6, task/it30 21 (labels as in the brief, pinned to commits; see the note on `main` below).
   - Claimed by this batch: WO-01 (CH-SB-POSTONSET-RESTORATION), WO-19 (CH-SB-CONCORDANCE), WO-26 (CH-SB-VGB-WHITEMATTER).
2. INFERENZA: of the 92 OPEN rows, 28 are wet-lab measurements and 11 are blocked by access; 20 are executable at zero spend with a route that answered when probed and are not claimed (not counting the IT30 queue), and 23 more are partly executable.
3. DATO, five open questions that are executable at zero spend, unclaimed and not run (evidence in the section below): `WO-06` ISR and seizures plus two unread sources; `IT29-P12` methods of the oligodendrocyte-screen paper behind two signed rows; `RS-R6` genetic-interaction lookups for suppressors of WWOX loss; `TS-01` re-check of 21 reopen conditions nobody has probed; `TS-02` re-run of the clinical-trial census after 16 days.
4. DATO, questions that look open but are concluded: `RS-R3` (concluded by its own IT13 amendment), `WO-13` (NP5A3, served by IT16 P3 on 2026-11-01), `RM-NEXT` (the roadmap 'Next:' PX-478/HIF line, executed in IT9 and IT10), `RM-R1`, `RM-R3`, `RM-R4`, `RM-R5`, `RM-R6` (delivered in IT7), plus the literature halves of three challenges (`WO-05`, `WO-28`, `WO-31`).
5. DATO, contradictions between records: the only heading marked CURRENT in the module README is iteration 19 although iterations 20 to 28 exist; the roadmap stage pointer names S8 although S9 exists; `view/DEPLOY.md` says the view is served nowhere although the site answers HTTP 200; several reopen rows contradict the records that answered them (list below).
6. DATO, engine defects found while running `scout_daily.py --plan`: the plan reads 12 of 13 reopen tables and silently drops the Q1-complement table R1-R9 (`EN-01`); the diagnosis parser finds 0 items in the IT28 diagnosis (`EN-02`).
7. INFERENZA, not decided: see the last section (the status of each of the 15 hand-over proposals, roadmap R2 and R7 to R12 individually, probes made in unrecorded sessions, and the full-text routes of four PMC-listed papers).

## Refs read, and a note on `main`

| Label in the brief | Commit used for every hash and date in the map |
|---|---|
| `main` (baseline of this batch) | `14c5fc7b47043ebc9bef336d609f6386bd6bbaa2` |
| `task/it29` | `d099a5be465f91fe7dc8c7f108751fd34f3a242d` |
| `task/it30` (head read when the map was last built) | `286ac2a183c23053542fbb5a50f60436de981efb` |

DATO: `main` moved while this map was built. At 2026-11-05T23:05Z `git rev-parse main` and `git rev-parse task/it29` both gave `0845ed06e8d0bc39d94b6d65351ec6f938b1c5e9`, which is `d099a5be465f91fe7dc8c7f108751fd34f3a242d` plus a closure-only commit (it changes `ledger/tasks/orchestrator/ORCH-ROADMAP-IT29-20261105.json` only). So every row marked `task/it29` in `published_on` is now also on `main` as of that commit, but the IT29 task record still shows P16 (push, CI, served-site check, cleanup) and P18 (dashboard) as IN_PROGRESS. At 23:14Z `task/it30` merged that `main` (head `1b0d865c6de2e4fe9583fa088108a97215c90f4e` at that moment). Earlier reads of `task/it30` were `852a26aca6727a0926d85f2e65bcf179ab67eacb` (22:35Z), `c26b3c6fcb3eabb56f729f6760681f2d6c3953ae` (23:05Z) and `0672016ebdb415f6ba036817c75be09fbbb98636` (23:23Z). Between the first two the IT30 session committed the CLM-pattern comparison and the bumetanide card update while its task record still showed S6 and S8 as TODO; the record was brought up to date in the commit `286ac2a183c23053542fbb5a50f60436de981efb` (23:23:19Z), so the rows `IT30-S6` and `IT30-S8` now follow the record (the lag is kept as contradiction 10). The IT29 worktree and branch were removed after landing: `git rev-parse task/it29` fails at 23:23Z, so the pinned commit is the only handle (it is an ancestor of `main`).

## How the map is built

* One row per distinct unknown. A work-order need and the investigation that proposes its test are one row (for example NEED-SEIZURE-CONTROL-SYMPTOMATIC splits into denominators, ethosuximide interaction and lithium specificity because the three have different statuses). Reopen rows that ask for the same datum as a need are merged into that need's row; the others keep their own row. `source_items_index.tsv` lists every source item with its row and the relation (primary, merged, not_a_question), plus the other files that name each reopen id.
* Columns are exactly those of the brief. `source_ref` and `status_evidence` use repository-relative paths with an anchor after `#`. `status_evidence` gives, for each cited record, the commit from `git log --diff-filter=A --format=%H -1` on the pinned ref; where that returns nothing (a file first created by a merge conflict resolution: `ranking.json`, `triggers.tsv`) the text says so and gives the first commit touching the path; where the concluding text is an amendment inside an older file, the commit is the first one in which the cited text appears (`git log -S`). `last_touched` is the latest commit date among the cited records on their refs.
* `kind` rules: wet_lab_measurement = the decisive datum is an experiment nobody has run and the module cannot run; data_access_blocked = the datum may exist but is not reachable by an open route; monitor = the row waits for a publication or deposit (a re-check is possible, the datum is not producible); literature_executable = answerable by reading or searching; engine_or_infrastructure = tools, stages, mandate steps and database lookups; decision = an Orchestrator choice or a stale-record correction.
* `status` rules: CONCLUDED = a record answers the question at the depth it needs (a part-answered question stays OPEN and its row says which part is open); SUPERSEDED = replaced by a later record; CLAIMED_THIS_BATCH = the three challenges of the brief; IN_PROGRESS = the IT30 session is working on it. Where the IT30 task record says TODO but committed files show the work, the files decide and the row names the record's reading.
* `executable_zero_spend`: yes = a route that answered when probed and no access barrier; partial = part of the question, or the route is uncertain; no; n/a for concluded rows. For IT30 queue steps, `blocking_reason` starts with `IT30-QUEUED` or `IT30 is working on it`: the map does not claim them.

### Counts, kind by status

| kind | OPEN | IN_PROGRESS | CLAIMED_THIS_BATCH | CONCLUDED | SUPERSEDED | total |
|---|---|---|---|---|---|---|
| wet_lab_measurement | 28 | 0 | 0 | 0 | 0 | 28 |
| literature_executable | 9 | 1 | 3 | 4 | 0 | 17 |
| data_access_blocked | 11 | 0 | 0 | 0 | 0 | 11 |
| engine_or_infrastructure | 14 | 4 | 0 | 10 | 0 | 28 |
| decision | 7 | 0 | 0 | 0 | 1 | 8 |
| monitor | 23 | 0 | 0 | 0 | 0 | 23 |
| total | 92 | 5 | 3 | 14 | 1 | 115 |

`executable_zero_spend`: n/a 15, no 38, partial 23, yes 39.

## The five open questions executable at zero spend, unclaimed and not run

Chosen for decision impact among the rows that are OPEN, `yes`, unclaimed and outside the IT30 queue; the other candidates are listed at the end of this section. No reading claim exists for the PMIDs involved (29618508, 27592856); the claims directory of the repository held, for the period after 22:00Z on 2026-11-05, claims by `sb-a1`, `sb-a2`, `sb-b1`, `sb-r1`, `sb-r2` only.

### 1. `WO-06` ISR and seizures, the Sephin1 rebuttal, five abstract-only glial papers (main)
* Question: is there a mammalian primary study of ISR modulation (ISRIB, PERK or GCN2 inhibitors, eIF2-alpha-P raising agents) on seizures or epilepsy models; what does the Sephin1 rebuttal paper (PMID 29618508) show; do the five abstract-only glial papers change at full text? The challenge `CH-IT28-ISR-ROLE` names 'a mammalian ISR-modulation seizure study' as its own reevaluation condition.
* Decision it can move: the design of the INV-02 test (rank 1, tie of 2) and the order of ISR lever classes; the IT28 verdict is that no class is preferable before the protein-level sign is measured, and a seizure precedent would be the first mammalian row for either direction.
* Evidence nobody ran it: (a) `batch_it28_p4_isr_role_20261105/B_neurons/README.md` says the seizure search was title and keyword searches of Europe PMC, 'not exhaustive', and lists PMID 29618508 as not read; (b) a git grep for ISRIB, PERK inhibitor, eIF2 and integrated stress over the IT29 phenotype-first and P10 packages and the IT30 context package returns 0 hits; (c) PMID 29618508 has no receipt on the three ledgers and no reading claim; (d) Europe PMC serves machine-readable full text for PMC5961032 (fullTextXML HTTP 200, 2026-11-05T23:16Z).
* Route and caveat: PubMed MeSH plus Europe PMC; NCBI and Europe PMC returned 5xx in several 2026-11-05 runs, so repeat failed queries.

### 2. `IT29-P12` methods behind two signed rows of the case-1 table (task/it29, now also main)
* Question: do the methods of the NCC oligodendrocyte-differentiation screen (PMID 27592856) explain its five contradictions with the frozen signs (clobetasol, ketoconazole, miconazole, tamoxifen, liothyronine; the paper uses thyroid hormone as its validation promoter)? Also unread: the 2015 OPC screen supplement and the public MEA screens of ToxCast chemicals.
* Decision it can move: whether signs in `signed_rows_case1_it29.tsv` are context-dependent by assay system; rows S1-32 and S1-33 already consume the screen as 'abstract-level, methods unread'.
* Evidence nobody ran it: the P12 README ends with 'Not reached: paper methods and figures, Nature 2015 supplement, MEA data deposit location, Baraban supplement'; no receipt and no claim for PMID 27592856; PMC5011342 serves fullTextXML (HTTP 200, 2026-11-05T23:16Z). Overlap risk: IT30 step S2 (IN_PROGRESS) re-checks IT29 residues ('independence by experimental origin').

### 3. `RS-R6` suppressors and modifiers of WWOX deficiency: the lookups never run (main)
* Question: is there a perturbation that suppresses a Wwox-null or hypomorph phenotype in fly, mouse, zebrafish or organoid? The three database lookups proposed in R6 (FlyBase, BioGRID ORCS, DepMap) 'were not run' (`recovery_it10_p23_20261031/README.md`, item 6); IT12 found DepMap behind a human-verification page and the fly literature in the wrong direction.
* Decision it can move: a lever that needs no residual WWOX would be the first for the missense and null classes; IT10 and IT12 found none in the literature reached.
* Evidence nobody ran it: a git grep over the whole tree at the baseline finds FlyBase and BioGRID ORCS only in the two IT10 files that say 'not run', and finds the Alliance of Genome Resources nowhere; the module, research notes and framework show the same on `task/it29` and `task/it30`. The Alliance API answered key-less (human gene record and genetic-interactions endpoint HTTP 200, 2026-11-05T22:51Z; content not analysed; the fly and mouse gene records were not requested). BioGRID ORCS bulk files and DepMap were not tested.

### 4. `TS-01` re-check of 21 reopen conditions that no record shows probed (main)
* Question: have R4 to R7; NP1B3; NP3A2 to NP3A5; NP3P1 to NP3P3; NP4G1 to NP4G4; NP5A1, NP5A2; NP5B1 to NP5B3 been met? Twelve others (R1, R2, R3, R8, R9, NP1B1, NP1B2, NP1B4, NP3A1, NP3B1, NP3B2, NP3B3) were last probed on 2026-10-31 (`bench_followup_it13b_20261031/README.md`, R2 under the label R3/R8) or 2026-11-01 (`radar_p4_it15_20261101/reopen_check_it15_p4.tsv`); NP5A3 is concluded.
* Decision it can move: each condition is the stated trigger for a card, flag or priority; unprobed, none can be reported as 'not met'.
* Evidence nobody ran it: the radar's own state file (`~/.local/state/legend/scout_daily_state.json`, outside git) lists 8 questions asked since 2026-11-02, 4 diagnosis and 4 work-order needs, no reopen condition; the R1-R9 table is not in the plan at all (`EN-01`). Routes: Europe PMC and PubMed title/abstract queries, GEO/SRA status calls.

### 5. `TS-02` clinical-trial census re-run (main)
* Question: has a study of WWOX-related epileptic encephalopathy been registered on ClinicalTrials.gov since the census of 2026-10-20 (no registered WOREE interventional study then)?
* Decision it can move: clinical-context flags of several cards and the sponsor-compound notes.
* Evidence nobody ran it: `clinical_census_20261020_raw/` holds one run; the two commits touching the census files are both dated 2026-10-20; `framework/scripts/clinical_census.py` is key-less and re-runnable.

### Other candidates (OPEN, executable, unclaimed), lower decision impact or partial route
* Lookups and readings with a working route: `WO-23` (Tau/catenin paired-readout precedent), `WO-32` (class IIa neuron-route search hole), `RS-NP1B4` (ChEMBL lever lookups, trigger met since 2026-11-01), `UN-N02` (one ChEMBL mechanism query).
* Radar items: `RD-TU` (ToolUniverse 1.5.9) and `RD-MA` (Monarch-app 1.32.0-rc1), minutes each, read at source.
* Engine: `EN-01` (table limit), `EN-02` (diagnosis parser), `EN-03` (generic terms, partly overlaps IT30 S10); `IT29-P11B` (decision: does TMP269 enter the catalogue). Queued by IT30 and not counted: `EN-09` (the UNMEASURED_AT_MAIN_TARGET ordering penalty, S9).
* Stale-record corrections: `DC-01` to `DC-05`.
* Partly executable: `WO-11`, `WO-12`, `WO-18`, `WO-25`, `NR-01`, `RS-R2`, `RS-R5`, `RS-NP1B1`, `RS-NP1B2`, `RS-NP3B1`, `RS-NP3B3`, `RS-NP4G1`, `RS-NP4G2`, `RS-NP4G4`, `UN-N03`, `UN-N08`, `RM-REST`, `EN-04`, `EN-05`, `EN-06`, `EN-07`, `EN-08`, `EN-10`. Of these `WO-25` (INV-03 isoform potencies and hERG numbers) matters most: the ChEMBL part is executable, but the three PMC-listed papers (PMC6758663, PMC1575949, PMC2880440) returned HTTP 500 from the Europe PMC full-text route on 2026-11-05T23:16Z.

## Questions that look open but are concluded, with the concluding record

| Row | Looks open because | Concluding record (path, commit) |
|---|---|---|
| `RS-R3` | N12 `what_would_reopen` and `triggers.tsv` R3_q1_complement still say 'above all R3' | `disease-models/wwox/research/drug_repurposing/recovery_it10_p23_20261031/reopen_searches.tsv` row R3 (IT13 amendment: both full texts read, datum absent), text first in commit `3560deaf85549ee189c3c5a044bd1f58694b1ec6` |
| `WO-13` | NP5A3 still NEEDS-DATUM in the reopen row, in `triggers.tsv` and in N17 | `disease-models/wwox/research/drug_repurposing/catalogue_resilience_it16_p3_20261101/README.md` section 4, added in commit `3d5cf1dfe37d156de32b19b1ee65369de008422b` |
| `RM-NEXT` | roadmap 'Next:' tells the reader to resolve the HIF neural premise with the PX-478 case | `disease-models/wwox/research/drug_repurposing/hif_it10_p21_20261031/README.md` section 0 (premise cannot be resolved with public data), added in commit `9a319876f28d9cb7507df711b7720bfb3d5db92f` |
| `RM-R3` | roadmap table lists R3 as 'first' with no status | `disease-models/wwox/research/drug_repurposing/network_comparison_it7_p3_20261029/README.md` section 1, added in commit `0d9d98794d650dcd8d6b3ae2615f2816ba540b63` |
| `RM-R6` | roadmap table lists R6 as 'next' with no status | `disease-models/wwox/research/drug_repurposing/loop_demonstration_it7_p6_20261029/README.md`, added in commit `f76f6edcfa0101ed63c0da4991136ff0e068d0f3` |
| `WO-05` | ISR lever meaning (CH-IT28-ISR-ROLE) | `disease-models/wwox/research/drug_repurposing/batch_it28_p4_isr_role_20261105/README.md`, added in commit `36add76506b741aec60b9c91aa6b5ef6e5af3b18`; residues are `WO-06` |
| `WO-28` | HDAC5 lever validity (CH-IT28-HDAC5-LEVER) | `disease-models/wwox/research/drug_repurposing/batch_it28_p3_hdac5_20261105/README.md`, added in commit `36add76506b741aec60b9c91aa6b5ef6e5af3b18`; residues `WO-29`, `WO-30` |
| `WO-31` | class IIa HDACs in CNS myelination (CH-IT29-CLASSIIA-CNS-MYELIN) | `disease-models/wwox/research/drug_repurposing/cycle_it29_p10_20261105/RETURN.md` on `task/it29`, added in commit `1bfc19d3fabdab52ced50f8d7ed1621adbd537aa`; residue `WO-32` |

Also concluded or partly concluded, not separate rows: the documentary search for HIF protein or activity in WWOX-deficient neural cells (closed in IT10 P2.1 and IT12 P2-P47T; the measurement stays open as `WO-08`); the census item 'MTBLS12344 released?' (public since 2026-11-02, integrated twice in `wwox_data_it24_p4_20261104` and `verification_it27_p2_20261104`; the 2026-11-01 radar entry '401' is outdated; lactate and pyruvate remain unanswered: `WO-09`); the question whether the public site exists (HTTP 200, `DC-03`); two of the three autophagy stubs behind `NR-01`; NP3A1 is concluded as 'undecidable at one pooled library per genotype' but its datum is absent (`RS-NP3A1`, OPEN).

## Published on `main`, only on `task/it29`, only on `task/it30`

* `main` baseline: 86 rows. Everything the module recorded up to IT28 (work order, ranking, reopen tables, IT28 challenges, scout decisions, IT24 P4 data census, IT16 resilience).
* Only `task/it29` at the baseline (6 rows: `WO-29`, `WO-31`, `WO-32`, `IT29-P12`, `IT29-P11B`, `IT29-P14`): the class IIa myelin challenge and its return, the TMP269 identity and pracinostat residues, the NCC-screen scout, the verifier corrections. Also only there at the baseline: the README 'start here' banner, the stage pointer S10, INV-03/04/06 notes in the ranking, the dashboard integration. All of it is on `main` from `0845ed06e8d0bc39d94b6d65351ec6f938b1c5e9`.
* Only `task/it30` (21 rows: the 15 steps S0 to S14, the five conditional questions `CQ-IT30-01` to `CQ-IT30-05` on benztropine, bumetanide, clemastine, rapamycin and vigabatrin, and the stated limit `EN-10`). Also only there: stage S11 with carried limits kept whole, the compound-context adapter, the CLM-pattern evaluation (30 cases; verdict WATCH/TRIAL), the chosen S8 question (consume the neonatal bumetanide record into card F03). The IT30 record at the build head: DONE S5, S6, S8; IN_PROGRESS S0, S2, S3, S11; TODO S1, S4, S7, S9, S10, S12, S13, S14.
* Not under git (2 rows): the two radar items, whose source is the scout briefing in `~/.local/state/legend/`.
* Collision notes for the Orchestrator: the IT30 S8 choice is the bumetanide consumption, so none of the five above overlaps it; `IT30-CQ5` (vigabatrin sign across seizure models) shares the compound, not the question, with the claimed vigabatrin white-matter challenge; `IT30-S2` may overlap `IT29-P12`; `IT30-S10` may overlap `EN-01` and `EN-03`.

## Contradictions between records

| # | Record A | Record B | Rows |
|---|---|---|---|
| 1 | Module `README.md` on `main`: 'exactly one heading carries CURRENT', iteration 19 (2026-11-02); `roadmap_current.md` sends the reader there | Iterations 20 to 28 have task records and packages but no README section; the radar briefing treats the README as the newest dated evidence. The banner on `task/it29` and `task/it30` (and `main` from `0845ed06e8d0bc39d94b6d65351ec6f938b1c5e9`) calls everything below it a historical index | `DC-01` |
| 2 | `roadmap_current.md` on `main`: 'Current stage (IT27)' names `generation_it27_p3_20261104/results_s8` | `generation_it28_p6_20261105/results_s9` exists on `main`; `task/it29` text admits the pointer named S8 through IT28; `task/it30` still names S10 while S11 is committed | `DC-02` |
| 3 | `roadmap_current.md` header: 'Updated 2026-11-01' | Standing-method bullets for IT22 to IT28 (up to 2026-11-05) sit below it; the file itself says an old 'current' heading is not authoritative | `DC-05` |
| 4 | `view/DEPLOY.md` 'State (2026-11-01)': only a local preview exists, served nowhere (same text on all three refs) | The public dashboard answers HTTP 200 (last-modified 2026-11-05T04:16:05Z, HEAD at 22:58:09Z) and the repository `README.md` links it; the IT19 'residual operation' is evidently done | `DC-03` |
| 5 | `uncarded_items.tsv` N12 and `triggers.tsv` R3_q1_complement: reopen 'above all R3' | The R3 row (IT13 amendment): both full texts read, Wwox level after an ACK1 inhibitor not measured | `RS-R3, DC-04` |
| 6 | `reopen_searches_it15_qa.tsv` NP5A3 and `reopen_searches_it12_p1b.tsv` NP1B4: NEEDS-DATUM | IT16 P3 pulled and regraded the Ro 25-6981 and ethosuximide context (NP5A3); the ChEMBL service answered again on 2026-11-01 (NP1B4); IT18 P1 names this stale-row limit and says the remedy is to update the verdict | `WO-13, RS-NP1B4, DC-04` |
| 7 | `needs/needs.json` NEED-MTOR-AUTOPHAGY: three WWOX/autophagy registry stubs 'none has been read' | The registry holds PAPER 148 as a complete full-text read (receipt FTR-20261019-24008736-03) and PAPER 152 promoted from stub 056; only stub 043 (PMID 36621327) is unprocessed | `NR-01, DC-05` |
| 8 | `view/work_order.json` `research_update` 2026-10-29 | Entries 7 and 11 are dated 2026-11-01 | `DC-05` |
| 9 | `scout_it21_p6_20261103/decisions.tsv`: leakage benchmark 'TRIAL (reading only), cost 1 h' | The package README: a test would measure nothing a decision rests on, no link predictor is in use | `EN-07` |
| 10 | IT30 task record at heads `c26b3c6fcb3eabb56f729f6760681f2d6c3953ae`, `1b0d865c6de2e4fe9583fa088108a97215c90f4e`, `0672016ebdb415f6ba036817c75be09fbbb98636`: S6 and S8 TODO | Committed files (CLM-pattern README with verdict, `S8_CHOICE.md`, F03 card update) show both done; the record was corrected in `286ac2a183c23053542fbb5a50f60436de981efb` (a lag of minutes, resolved) | `IT30-S6, IT30-S8` |
| 11 | `radar_p4_it15_20261101/reopen_check_it15_p4.tsv`: MTBLS12344 '401 no permission' | `wwox_data_it24_p4_20261104/README.md`: public since 2026-11-02 and integrated (an outdated probe, not a conflict at its date) | `WO-09` |

## Engine findings from `scout_daily.py --plan` (run once, 2026-11-05T22:39:39Z)

* DATO: 69 questions: 15 work-order needs (weight 3), 43 reopen conditions (weight 2: 25 NP rows and 18 scout-decision rows), 3 roadmap rows (weight 2) and 8 further roadmap rows (weight 1). The briefing of 2026-11-05T05:20 names two radar items to examine: ToolUniverse 1.5.8 to 1.5.9 (`RD-TU`) and Monarch-app 1.31.1 to 1.32.0-rc1 (`RD-MA`); neither version string occurs in any record on the three refs.
* DATO, `EN-01`: `TABLE_LIMIT = 12` with tables ordered by iteration number; `main` holds 13 reopen/decision tables, so `recovery_it10_p23_20261031/reopen_searches.tsv` (R1 to R9) is dropped. Reproduced by applying the script's regex and sort to `git ls-tree` of the baseline.
* DATO, `EN-02`: the diagnosis parser needs six cells per row; `diagnosis_it28_20261105/README.md` has four, so the plan carries a provisional note and no diagnosis-derived question since IT28.
* DATO, `EN-03`: derived terms are generic for several needs and the ISR discovery items of the briefing are unrelated; IT18 P1 measured about 40 percent noise and did not fix it.

## What I could not decide, and why

* The 15 hand-over proposals of the S9/S10/S11 stages (Pracinostat, ASTX-660, Desidustat, AT-13148, Razuprotafib, SAR-407899, LGH-447, Ravoxertinib, Rineterkib, Tretinoin, EPZ004777, TAK-901, AZ960, GSK2816126, Tapinarof): every name occurs in qualification or comparison records (IT9, IT21, IT22, IT27), but the status of each as a question would need reading each proposal's decision-scope row; no row was written.
* `RM-REST`: roadmap R2 and R7 to R12 are plan rows without a status; R8 (human WWOX RNA opportunity) has no dedicated monitoring record that I found; R10 is the IT29 dashboard step, IN_PROGRESS in the IT29 record.
* Whether the PubMed MCP full-text tool serves the PMC-listed papers that Europe PMC's XML route refused (PMC524435 for NP5A1; PMC6758663, PMC1575949, PMC2880440 for INV-03): not tested, because it opens papers; rows `WO-11` and `WO-25` say `partial`.
* The open-access status of the two primary papers behind NP5A2 (Hess 1996, Fischer 1997): their PMIDs are not given in the reopen row and were not resolved.
* 'Not probed' statements rest on the probe records I found (IT13b follow-up, IT15 P4 check, the radar state file); a probe made in an unrecorded session would not show.
* Counts depend on the merge rule above; a one-row-per-source-item reading would give 160 items (see the index) instead of 115 rows.

## Files in this directory

* `open_questions_map.tsv`: the map, 12 columns, tab-separated, UTF-8, no tab or newline inside a field.
* `source_items_index.tsv`: every source item, its row, the relation, and other files that name it.
* `probes_run.tsv`: every status probe (route, string, time, result).

Not medical advice. Nothing here qualifies, ranks or recommends a compound.
