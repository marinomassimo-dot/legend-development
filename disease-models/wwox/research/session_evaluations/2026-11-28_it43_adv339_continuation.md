# Self-evaluation — IT43, ADV-339 continuation (BATCH_20261128_013), 2026-11-28

Hypothesis level; nothing here is medical advice. Written by the actor that did the work; attributions say who caught what.

## Scope and executable verdict
- Batch/session: `BATCH_20261128_013` (MINOR), claim records CLAIM 030 and CLAIM 031; mandate ORCH-ROADMAP-IT59-20261119, IT successor 43. Published `83b1e5500` (gate PASS, ls-remote).
- Studies and receipts: `FTR-20261128-42422765-03`, `-32000863-02`, `-19936220-46`, `-30290271-01`, `-36779245-01`, `-26499798-03`, `-33916893-03`, all `queried_not_full_read` (sentence-level readings by delegates, no complete read claimed).
- `session_self_eval.py`: VERDICT PASS (4009 receipts, 0 unread premises; declared gaps listed are older manifests: 30361190, 32000863, 34214506, 35716775).
- Receipt verification: OK, tail anchored. LINT: WARN (existing UNLINKED_SUPPORT warnings, no BLOCK). `growth_anchors check` PASS. `test_batch_queue` OK.
- Workspace verdict: CI for `83b1e550` and the earlier tips not yet complete when written (runs about 50 minutes); read from a completed run only.

## Content diagnosis
| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | Three readers per sentence opened the whole source papers, figures and held supplements (Wang 2012 supplement fetched from the PMC bucket first; Hussain 2019 supplement tables not obtainable, Europe PMC error XML, not retried) | partial | Hussain supplementary tables, Mignot 2015 (held at no depth), two mp4 files |
| Main message and original contribution | 2 of 12 sentences fail on all readers; both are attribution errors, not wrong arms: a contrast placed in a paper with no such arm (CLAIM 031), an independence label on two reviews of one primary report (CLAIM 030) | strong | pooled 8 of 23 reported with the draw difference |
| Hidden gold | The 8-bar structure of Fig 3b, the second harvest in the Johannsen text, p-β-catenin in Wang Fig 1b/1c, Fig 4D/E asterisks versus «indistinguishable» all came from reading figures, not keywords | partial | reading-dependent cells listed, not edited |
| Source parity | Table rows (Oliver Table 1/2, Banne Table 1 rowspans) read from markup; figure values labelled estimates | strong | |
| Team type / observation vs interpretation | the CLAIM 030 «R4 satisfied» label was checked as the batch review floor before editing | strong | |
| DATO / INFERENZA separation | HE's UNSETTLED on interpretive atoms (H3.1, H5.1, H6.2) left unedited | strong | |
| Existing claims touched | CLAIM 030, 031; copies found by `git grep` in DL-MECH-039 and HYP-20260709-07 | partial | two copies uncorrected (see failures) |
| Multi-hop | S6 traced to Mignot 2015 through reference lists of both reviews | partial | Mignot not opened; the named pattern (independent-corroboration check) goes to SCI's successor |

## Persistence diagnosis
- Durable IDs: `BATCH_20261128_013`, `CC-20261128-ORCHESTRATOR-IT43-ADV339-01`, folder `adv339_exclusivity_it_20261128/` (`RESULT_ADV339_part3_*`, `SELECTION_IT43.md`, `second_reader_tables/`, `DREAM_*`).
- Reading debt: CLAIM 042 (source PMID 36537114) and the CLAIM 030 K274R paragraph (PMID 25331887) need a complete read; the other counted sentences are picked up only when a premise that cites them is used (ADV decision).
- My first reader's table is held as digests of two delegate hand-backs (delegates cannot write report files), not a delegate-written file.
- A future run distinguishes these readings from complete reads by `evidence_depth: queried_not_full_read` and the coverage block.

## Process and capability diagnosis
- Used: blind packets (no labels, no expected answer), three independent readers with tables withheld, blind verifier on the final atoms, `test_batch_queue`, receipts through the validated writer, regeneration order join, coverage, ranking, view trio, `safe_push` with the lock.
- Declined: a scripted edit of the two ledger copies after the classifier refusal (not worked around); a stand-alone tool for receipt drafting (the script is job-local; proportional).
- Failures and events: (1) first `safe_push` refused: SCI's four receipts landed while I waited at queue position 3, so the ledger, ranking and view files conflicted; restarted from `development/main` and re-recorded (about 10 minutes). (2) a `git rm --cached` on the receipts folder also staged deletion of IT42's four receipts; seen at once in `git status`, restored from `development/main`. (3) the auto-mode classifier refused my scripted edit of `discovery_ledger_current.md` and `therapeutic_hypotheses_ledger_current.md`; recorded, not retried; ADV put it on the operator list. (4) HE's table file changed after my first read (HE-CHECK notes appended); I re-copied and recounted.
- What caught each: the delegate's negative search caught the Obeid AED misattribution (confirmed by HE and by me on the XML); SCI caught «una barra per linea» (8 bars) and the second harvest; HE's check caught the «crisi» reading in +/+ and +/-; the blind verifier gave 10 of 10 on the final text.
- Micro-upgrade shipped: none to the framework; the relanding recipe is recorded in memory (receipt regeneration against the new ledger tail; check `git status` for `D` lines after `git rm --cached`). CHANGE = NONE.
- Residual risk: two uncorrected copies of the CLAIM 031 sentence; CI of the landing tip not yet read from a completed run.

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 6
machine: 3   blind_auditor: 3   peer: 0   self: 1
severity_high: 0   of which self: 0
undetected_known: 0
```
Incidents: Obeid misattribution (blind_auditor: delegate and HE), «una barra per linea» (blind_auditor: SCI), «independently» (blind_auditor: all three), `safe_push` refusal on conflicting paths (machine), classifier refusal (machine), `git rm --cached` side effect (self, caught by `git status`; never reached a commit). `undetected_known` is 0 only as far as this census can see.

## §21c output
`DEFAULTS_TAKEN`: reading-dependent cells not edited; two ledger copies not edited after refusal. `STOP_LOG`: one classifier refusal, recorded.
