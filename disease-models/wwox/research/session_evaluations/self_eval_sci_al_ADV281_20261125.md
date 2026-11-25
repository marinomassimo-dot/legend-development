# Self-evaluation - SCI window AL, ADV-281 (positive-control audit of null-wording card notes), 2026-11-25

## Scope and executable verdict

- Session: ADV-281, one increment-pair of the null-note audit (ten of the brief, nine surviving, plus six additions, fifteen notes in all). Actor `orchestrator` (SCI), session 9cc174db, `claude-sonnet-5-5`, effort high (census read back: 80 of 80 turns high at the time of writing). One delegate: blind sentence reader, `legend-delegate`, asked sonnet and high, read back model `claude-sonnet-5-5` on 165 turns (effort not listed for subagent transcripts by the census).
- Receipts: none written (a targeted null check, not a completed read). `session_self_eval.py`: PASS. Receipt verification OK (2,846 chained, tail anchored). Structural LINT: no block. Landing: `safe_push` gate PASS, six landing suites, one red on the first try (a shebang script without executable mode, fixed) and none on the second.

## Content diagnosis

| Dimension | Answer | Grade | Debt or correction |
|---|---|---|---|
| Rule fixed before the sources | PREREG with phrase list, routes, classes, predictions and a rejecting observation written before any source was opened; seen-beforehand items disclosed | strong | the screening of 130 candidates is one reader's judgement, not blind-checked |
| Two-route list | 63 null notes against SCI's ten; the difference explained (one field and keywords versus side-arm nulls and over-matching phrases); one of the ten dropped | strong | route T recall limit (DR-E03-001 matched by accident); 48 rows unaudited |
| Source reading | Held XML, supplements, rendered figure pages (hashes), workbook rows, ChEMBL rows; two missing bytes acquired on ADV's decision and read | strong | no figure images held for two papers; no video |
| Blind check | Sentence file built by script; reader saw no class; its verdicts reconciled with the first reader and shown side by side | strong | classes differ on four rows over the rule for a cited result; the in-study column agrees on all |
| Verification of the delegate | Two MUST CHANGE findings re-derived by SCI (chi-square 0.0393; the text of Collard) before use | strong | the other eleven delegate verdicts were not re-derived |
| Prediction calibration | P1 and P2 at the bottom of their ranges; rejecting observation not met; carried into the checkpoint | adequate | the first prediction was written for ten and scored on nine |
| Existing claims touched | Our own ADV-276 sentence for DR-P11-004 was wrong (an uncorrected test reproduces the printed value); stale "supplement not available" labels | strong | wording sent to IT; nothing applied here |

## Upgrade (the answer, not the promise)

Checklist line proposed for `PRE_READ_CHECKLIST_ADV276_SCI_20261125.md` (applied below in the same commit): a reproducibility claim about a printed p must name the test and say what the other standard tests give; a "not available" label is checked against the held folders before it is repeated; record "in-study check" beside every control class because a cited effect is not one.
