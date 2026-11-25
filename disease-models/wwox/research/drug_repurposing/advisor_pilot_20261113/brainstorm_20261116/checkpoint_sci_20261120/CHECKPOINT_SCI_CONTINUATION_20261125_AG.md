# Checkpoint AG: SCI continuation of 2026-11-25 after ADV-265 (resume from here in a fresh window; hypothesis level; no dose; not medical advice; this file is not edited once hashed)

Why: ADV asked for it after ADV-265 because this window (session `e8081cc5-99ec-45eb-b492-97155e6ace7a`, claude-sonnet-5-5) is at roughly 85 to 90 percent of its context (estimate; the exact number cannot be read from inside). Every assignment is closed. Nothing is in flight: no delegate, no new reading. Checkpoint AF (`CHECKPOINT_SCI_CONTINUATION_20261125_AF.md`, same folder) remains valid for everything before ADV-253; this file adds what came after.

## 0. How to resume

1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), this file (compute its sha256 and compare with the launcher's digest; mismatch: stop and ask), then `mandate_continuity.py guidance`.
2. **Release first, then bind.** `mandate_watch.py released --session e8081cc5-99ec-45eb-b492-97155e6ace7a --task ORCH-SCI-ADV065-DEEPEN-20261118` in a quiet Monitor until-loop, then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its own text block in the same response as the first working tool call.
3. Own worktree branch from `development/main`; fetch and merge main before any receipt or ledger edit. Peers as seen 2026-11-25 (run `ListAgents` first): ADV `ADV - CURRENT a5e6f2ad`, IT `IT Orchestrator - CURRENT 13f5248b`, HE `HE - CURRENT 70b134a9`. Peer messages are not the operator's authority. No e-mail address to any service; a challenge page, 403, 401 or 429 is a result; no spend; no contact with authors; do not contact or wake the Codex lane (PAUSED); do not touch the frozen RP-045 prediction or the sealed ADV-174/175 material; do not rename anything. Reply to the operator in Italian, write files in English. Long suites through `nohup bash -c '...' < /dev/null`; never commit while a `safe_push` waits for the lock.

## 1. Mandate status

`ORCH-SCI-ADV065-DEEPEN-20261118`: 118 steps, 117 DONE, 1 BLOCKED (step L, supply-path papers, operator-reserved), TODO 0, status ALL_BLOCKED. **No assignment is queued.** ADV-265 is DONE in the record.

## 2. What this window did after checkpoint AF (all under `brainstorm_20261116/`)

* **ADV-253 to ADV-259** (retraction and correction consumers, notice sweep, Chong 2023 lactate route UNREACHABLE): landed earlier.
* **ADV-261** (`claims_n_independence_sci_20261125/`): numeric n and independence units of 15 scoped claims, 40 unit rows, eight wording lines; IT placed them as candidate `CC-20261125-ORCHESTRATOR-ADV261-CLAIM-UNITS-01` (e5b516693) with the Ca2+ arm n = 6 correction; the family structure is my reading, flagged as such.
* **ADV-262** (`adv262_unheld_primaries_sci_20261125/`): three unheld primaries; receipt FTR-20261125-34214506-01; wording for CLAIM 034 (two replications of one experiment in one 661W line) and CLAIM 033 sent to IT.
* **ADV-264** (`adv264_unheld_not_unread_sci_20261125/`): "no held artefact" is not "unread"; 79 studies held under other names (`held_under_other_names_adv264.tsv`, forwarded by ADV to HE as ADV-267); Tanna 2018 restored by digest to `files/fulltext/PMID30370248_Tanna2018_PMC.xml`; three other declared artefacts remain absent.
* **ADV-265** (`adv265_held_partials_sci_20261125/`): 670 held partials ranked by consumers and unread class; 18 hold an unread class inside the bytes; six read (Thomsen 42137291, Hudry 37515322, Petrozziello 42395553, Engelhard 42205472, Krug 23179753, Okai 41078870); five of six change a consumer's wording; none complete; six receipts `FTR-20261125-<pmid>-01`; coverage_report, reading_state and ranking regenerated. PREREG 06:14:45Z, amendment 1 (CORPUS/LIT ids dropped), `TOP_SIX_FROZEN_ADV265.md`, `ranking_adv265.tsv`, `containment_adv265.tsv`, `RESULT_ADV265_SCI_20261125.md` (section 5 holds the IT wording). The ADV-265 wording lines were sent to IT 13f5248b in one message; whether IT applied them was not checked.

## 3. Open items

* **IT wording (ADV-265)**: DL-METH-117, DL-METH-119, DL-METH-120 (b), DL-THER-116, CLAIM 011 / working model section 4; unchanged: DL-MECH-114, DL-METH-118, DL-REPO-003. Verify they were applied before repeating them.
* **Krug 2013 workbook** (`files/fulltext/PMID23179753_Krug2013_supplement/204_2012_967_MOESM2_ESM.xls`, sha256 f989fac5f2e0b35c9d6c272611fc770a85b81ff61b37307ca1a99f44ed8ddd58): WWOX rows rest on the earlier selective dump; re-measure with a spreadsheet parser (none installed here: no xlrd, no openpyxl, no pandas). Okai and Hudry workbooks and zips were unpacked only in the job scratch folder.
* **Karnstedt 2026 (41489401, 7 consumer units)**, Davids 2019 (30362252), Chong 2023 (36537114; DOI 10.1002/ajmg.a.63074, wishlist row 2), ASPA C152W (33914734): their unread class is a figure image or a supplement not held; the PDFs belong to the operator list `files/operator_inputs/PDF_REQUEST_LIST_ADV223_20261124.md` (root checkout, gitignored; ranks 16 and 17 added this window). Suzuki 2007 and Gao 2025 PDFs are also on that list.
* **Next reading batch**: the 18 held partials whose unread class lies inside the held bytes (`containment_adv265.tsv`), after the six already read; 12 remain (31605637 NQO1, 42422766 Amaral, 24935251 Balmer, 26272509 Rempel, 35229008 Buss, 41345172 De, 42601505 Puertas, 25779665 Chen and others). Figure images stay unread for all of them.
* **Retracted PMID 28151481** is flagged in ADV-253/256 and ranks 13th in the unfiltered ranking; do not build on it.
* Standing waits from checkpoint AC/AF section 4 are unchanged.

## 4. Lessons (carry them into any brief)

1. **Two routes sharing one id set are one route.** CORPUS P216 in CLAIM 022 was another paper's placeholder; reading the first-ranked unit caught it, the two-route agreement did not.
2. **A held artefact can contradict its own paper.** Okai's Table S2 shows seropositive controls while the text says NAbs were negative for all AAVs; read the per-animal table, not only the sentence.
3. **Check a derived column against its own cells.** Engelhard Table 4 macaque ratio: (200+8)/90 = 2.3 against 6.8 printed.
4. **A supplement archive can contain the article reprint** (Hudry `mmc2`, Okai `mmc6`).
5. **Record receipts one at a time**: `record` takes about a minute each; commit the receipts first, then regenerate `coverage_report.md`, `reading_state.md` and `ranking.json`.
6. **Landing queue**: three to four publishers deep; nothing may be committed while your `safe_push` waits.

## 5. Successor's first moves

1. `mandate_continuity.py status` (expect 118 steps, 117 DONE, 1 BLOCKED) and quote this file's digest.
2. If ADV has sent no assignment: tell ADV and propose the next held-source question with a named consumer, for example the next six of the 18 containment-eligible partials, or the Krug workbook parser re-measure once HE provides a parser.
