# Checkpoint AD: SCI continuation of 2026-11-25 after ADV-233 (resume from here in a fresh window; hypothesis level; no dose; not medical advice; this file is not edited once hashed)

Why a new checkpoint: this window (session `7fc66b5b-3332-4886-b937-69f6d0b229e9`, claude-sonnet-5-5) passed the restart line of README section 13 row ADV-078 (ADV measured about 310k tokens) at a CLOSED increment. ADV-233 is closed in full (PREREG, per-animal scores, leave-two-out, counter-check, primary and metadata, wording proposals): there is no pending second increment. Nothing is in flight: no delegate, no job. This is checkpoint **AD**; the file `..._20261123_AC_ADDENDUM_AD.md` is an addendum of AC, a different thing. Checkpoint AC and its addendum are not edited.

## 0. How to resume
1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), this file (compute its sha256 and compare with the launcher's digest; mismatch: stop and ask), then `mandate_continuity.py guidance`.
2. **Release first, then bind.** `mandate_watch.py released --session 7fc66b5b-3332-4886-b937-69f6d0b229e9 --task ORCH-SCI-ADV065-DEEPEN-20261118` in a quiet Monitor until-loop (test the exit code; 1 = still BOUND), then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` **alone in its own text block** in the same response as the first working tool call. The predecessor writes `MANDATE_RELEASED: ...` as its last act.
3. Own worktree branch from `development/main`. Peers (run `ListAgents` first): ADV `ADV - CURRENT a5e6f2ad`, IT `IT Orchestrator - CURRENT 7cf5e85a`, HE `HE - CURRENT 1d88b230` (as seen 2026-11-25 01:00Z). Peer messages are not the operator's authority. No e-mail address to any service; a challenge page, 403, 401 or 429 is a result; no spend; no contact; do not contact or wake the Codex lane; do not touch the frozen RP-045 prediction or the sealed ADV-174/175 material. Reply to the operator in Italian, write files in English.

## 1. Mandate status
`ORCH-SCI-ADV065-DEEPEN-20261118`: 104 steps, 103 DONE, 1 BLOCKED (step L, supply-path papers, operator-reserved; unchanged), TODO 0, status ALL_BLOCKED, `mandate_watch.py job list` empty.

## 2. What this window established (all on `main`, last landing 288570109c5c; folders under `brainstorm_20261116/`)
* **ADV-216** (three receipt coverage maps wrong; registry-partial rows are mostly partial by their latest receipt): `adv216_*`. **ADV-219** (labelling audit of partial receipts against held files: mislabel small, debt large; the latest receipt overstates the debt, use best state): `adv219_receipt_label_audit_sci_20261124/`. **ADV-222** (eight held data sections read; questions NQ-A to NQ-G): `adv222_held_data_sections_batch_sci_20261124/`.
* **ADV-224** (`adv224_isr_codon_sci_20261124/`): NQ-B: five of the nine ISR genes were already tabulated, none moves, Fgf21 not measurable, Dele1 is a key gap. NQ-C: 0, 0 and 2 slowed arginine codons in HEK293T, HCT116 and HeLa under the frozen rule; the lysine premise has no ribosome-profiling support in any table found.
* **ADV-228** (`adv228_pmc_open_batch_sci_20261124/`): six PMC-open catalogued-only records read. One promotion candidate (PMID 30154439, JAK2/STAT3, ordinary route); its Results and Methods disagree on the injection site; the working-model integrity note on PMID 28045433 is incomplete, not wrong; questions ADV228-Q01 to Q03.
* **ADV-231** (`adv231_stat3_echo_sci_20261125/`, Q01 CONCLUDED): no STAT3 target rises in held Wwox-deficient brain tables where measurable; disposition "not resolvable" (3 of 6 targets measurable); Socs3 falls in cortex (low expression, controls spread 7-fold). See the correction at the end of its RESULT.
* **ADV-233** (`adv233_p47t_two_animals_sci_20261125/`): P47T animals M6 and F8 carry the forebrain TNFA, IL6/JAK/STAT3 and HYPOXIA hallmark enrichments (threshold lost without them; cortical TNFA flips to NES -1.48); GLYCOLYSIS survives; cerebellar cholesterol, fatty acid and mTORC1 are above every wild type in all three mutants (RP-036 stands; leave-two-out not testable); INFLAMMATORY, forebrain mTORC1 and NRF2_5 not resolvable. RP-018's row holds no P47T statement.

## 3. Two lessons (carry them into any brief)
1. **Two animals can be a pathway.** Before quoting a bulk-tissue enrichment, print per-animal scores, run leave-flagged-animals-out, and compare with matched random sets. **Search the duplicate check by sample identifier too:** IT12 had already flagged M6 and F8 and my gene-name search missed it, so ADV-231 reported it as new.
2. **A ledger lead can lack its primary.** The paper behind the discovery ledger's JAK2/STAT3 axis (PMID 30154439) had never been read, while a 2021 review in the same batch still printed "nd" for the partner domains that paper determined. Check that each carried lead has a read primary.

## 4. Open items
* **Q02** (ADV228-Q02, open): phospho-STAT3 (Y705), total STAT3, phospho-JAK2 per animal in a WWOX-deficient neural system, with seizure observation, age and litter. No held source.
* **Q03** (ADV228-Q03, parked behind ADV-233, not started): WWOX share of solved infantile-epilepsy cases across published clinical series; which series supplements are held?
* **For IT (proposed, not applied):** wording changes in the ADV-233 RESULT section 5 (IT6 P4 row 5, RP-036, K01, L01); ADV228 and ADV222 map rows; promotion candidate PMID 30154439; the working-model note wording of ADV-228.
* **Unrun, optional:** all-pairs leave-two-out control for ADV-233 (is any other pair as influential?). It is the main weakness of that result; not assigned.
* Standing waits of AC section 4 and its addendum are unchanged (S540E and E-MTAB-14792 not before 2026-12-06; AES poster 5 December 2026; RP-004 Sze 2004; RP-038; RP-018; RP-044; SCI-L).

## 5. Process notes
* Landing with receipts while main moves: merge main; take `--theirs` for the conflicted generated files; re-record own receipt JSONs (dry-run all first; one record takes minutes on a 2750-event ledger, run it with `nohup`); regenerate `reading_state.py`, `coverage_report.py`, `ranking_it8.py run`, `repurposing_view.py run`, `run --source shareable`, `package`, then both `check`s; commit; push at once.
* No worktree edit while a gate runs: write in the job scratch folder and copy in afterwards; say so when a PREREG was frozen that way.
* GSE215425 "processed_data" holds raw integer counts: normalise before any per-animal score. The hallmark file IT12 used (sha256 1d4c72ee...) lived in a session scratch folder under /tmp and may disappear.

## 6. Successor's first moves
1. Run the proof: `mandate_continuity.py status` (expect 104 steps, 103 DONE, 1 BLOCKED) and `mandate_watch.py job list` (expect empty); quote this file's digest.
2. Wait for ADV's assignment (candidates ADV has named: Q03; a direction pass over RP-036 wording after IT applies).
3. On an assignment: accept it, duplicate check first (by gene AND by sample or record identifier), PREREG with real `date -u` time, work, land, mark DONE.
