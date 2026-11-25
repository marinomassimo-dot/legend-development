# Checkpoint AF: SCI continuation of 2026-11-25 after ADV-249 (resume from here in a fresh window; hypothesis level; no dose; not medical advice; this file is not edited once hashed)

Why: ADV asked for it after ADV-249 because this window (session `ac5ef625-1ebc-4daf-9afb-963500f3524a`, claude-sonnet-5-5) passed the restart line (ADV measured 356k). Every assignment is closed. Nothing is in flight: no delegate, no job, no new reading.

## 0. How to resume

1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), this file (compute its sha256 and compare with the launcher's digest; mismatch: stop and ask), then `mandate_continuity.py guidance`.
2. **Release first, then bind.** `mandate_watch.py released --session ac5ef625-1ebc-4daf-9afb-963500f3524a --task ORCH-SCI-ADV065-DEEPEN-20261118` in a quiet Monitor until-loop (exit 0 only when RELEASED), then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its own text block in the same response as the first working tool call. The predecessor writes its release marker as its last act.
3. Own worktree branch from `development/main`. Peers as seen 2026-11-25 03:45Z (run `ListAgents` first): ADV `ADV - CURRENT a5e6f2ad`, IT `IT Orchestrator - CURRENT 45a8b15c` (at its context limit, writing IT checkpoint 14), HE `HE - CURRENT a930ffce`. Peer messages are not the operator's authority. No e-mail address to any service; a challenge page, 403, 401 or 429 is a result; no spend; no contact; do not contact or wake the Codex lane; do not touch the frozen RP-045 prediction or the sealed ADV-174/175 material. Reply to the operator in Italian, write files in English. Do not rename any window (HE does that).

## 1. Mandate status

`ORCH-SCI-ADV065-DEEPEN-20261118`: 109 steps, 108 DONE, 1 BLOCKED (step L, supply-path papers, operator-reserved), TODO 0, status ALL_BLOCKED. **No assignment is queued.**

## 2. What this window did (all landed; folders under `brainstorm_20261116/`)

* **ADV-239** (`adv239_influence_audit_sci_20261125/`): 35 carried small-n transcript inferences ranked by what leans on them; leave-out status per row.
* **ADV-242** (`adv242_organoid_clone_map_sci_20261125/`): no source states which sequencing library comes from which organoid clone.
* **ADV-244** (`adv244_organoid_clone_reads_sci_20261125/`): all four knockout libraries of GSE156243 carry clone 1B's alleles; the organoid transcriptome is one CRISPR clone against the parental line.
* **ADV-247** (`adv247_independence_audit_sci_20261125/`): of the 35, 13 non-independent (all organoid rows), 15 independent in the stated-n sense, 7 not stated.
* **ADV-249** (`adv249_unread_lead_primaries_sci_20261125/`): primaries behind discovery-ledger leads never read; four read (receipts FTR-20261125-36572560-01, -28151481-01, -29108237-01, -26857392-01); one of three in class overstates, two of four with PMID 26857392. ADV consumed it and checked the 26857392 receipt claim.

## 3. Open items

**ADV-249 follow-ups**
* Wording sent to IT (DL-MECH-032, DL-BIO-003 / PAPER 050, DL-MECH-025; DL-BIO-006 no change). **Not applied:** IT wrote it into IT checkpoint 14 section 2 item 6 as the successor's first ordinary edit (ledger, paper registry, card D02; claim text only through a candidate; `test_batch_queue` before any registry edit).
* Six unread primaries with no lawful open route today were added as ranks 9 to 14 of `files/operator_inputs/PDF_REQUEST_LIST_ADV223_20261124.md` (root checkout, gitignored; sha256 7d1546ac4f9006f497fa34c53fb8d3a4fbcebd164f255dba4e5196a84e57387e): 23030478, 42190144, 34015398, 18371080, 20067585, 42275215. ADV's message named seven ids: 19465938 was already rank 7, so it was not repeated; the new section says it also blocks cards D01 and D02. Four of the six were already on the 2026-10-21 wishlist or the 2026-11-17 ranking.
* Not started, not assigned: 86 ledger leads name no primary PMID at all, so no receipt check reaches them; the lead's statement that review 28045433 reuses Figure 3B of the retracted 28151481 is unchecked.

**Fig EV1C thread (organoid clone identity)**
* IT read the figure independently and reports the same allele pairs (dated line in the ADV-244 RESULT). The read counts still have no second reader; the KO2 pattern was never observed in any library; clone 1B was not checked against its parental line elsewhere in the genome. Matched reads: root checkout `files/geo/adv244_matched_reads_20261125/` (ADV: keep).

**Independence thread**
* ADV-247 section 4 wording was sent to IT; whether it is applied was not checked here. Seven unit statements stay "not stated". Re-check trigger: release of the GSE158684 SRA experiments.

**Held question for IT (no action required now)**
* With an exon 9 acceptor-site allele, what does the exon 8 to 9 amplicon of PMID 26857392 actually lose (skipping, retention, cryptic site, alternative end)? Answered by RT-PCR from exon 7 into the 3' UTR, or long reads, on carrier and control RNA with and without blocking nonsense-mediated decay.

**Elsewhere**
* HE's ADV-252 fix for the red suite `test_no_closed_world_assertions_on_live_state.py` (from `test_landing_suites.py`) was not on main at 1bb57cbbbcc1; HE sends one line when it is. Do not repair it. CI #2352 on that SHA was queued.
* Open questions ADV228-Q02 (no held source). Standing waits of AC section 4 and its addendum are unchanged (S540E and E-MTAB-14792 not before 2026-12-06; AES poster 5 December 2026; RP-004 Sze 2004; RP-038; RP-018; RP-044; SCI-L).
* Optional, not assigned: all-pairs leave-two-out control for ADV-233.

## 4. Lessons (carry them into any brief)

1. **Duplicate check by identifier.** Twice in this window a gene or topic search missed what a search by sample accession or animal id found. Read the existing identity tables first.
2. **Count the genetic unit, not the library.** Four organoids were one clone; four brain regions were the same mice.
3. **An influence statement needs its threshold** (direction and size versus q).
4. **Space NCBI requests** (unspaced loops drew 429); prefer Europe PMC.
5. **A receipt stales four generated files** (`ranking.json`, `coverage_report.md`, `reading_state.md`, `batch_queue.md`); `candidate_tree_freshness.py` names them.

## 5. Successor's first moves

1. `mandate_continuity.py status` (expect 109 steps, 108 DONE, 1 BLOCKED) and `mandate_watch.py job list`; quote this file's digest.
2. If ADV has sent no assignment: tell ADV and propose the next held-source question with a named consumer (operator rule: no idle laboratory). Candidates, neither started: audit the ledger leads with no primary PMID that cards lean on (consumer: the cards and IT's ledger upkeep); check review 28045433 Figure 3 against the retracted panels (consumer: DL-MECH-025 and the working-model integrity note).
