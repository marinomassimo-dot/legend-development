# Batch self-evaluation: parallel scientific batch, drug repurposing (ORCH-SCIBATCH-DR-20261105)

Non-canonical research record, not medical advice. Written by the Orchestrator that ran the batch, after the executable gate. Self-assessment is the weakest evidence; where another actor caught something it is attributed.

## Scope and executable verdict

- Batch/session: ACTOR_ID `orchestrator` (stated assumption), 2026-11-05/06, five literature packages plus an open-question map, verified by blind audits, delta audits and adversarial reviews.
- Studies and receipts: 109 staged receipts (none recorded, none a complete read); 1,178 receipts in the ledger on this branch, unchanged by the batch.
- `session_self_eval.py`: **PASS** (no complete read pending, every declared output resolves). `fulltext_receipts.py verify`: OK, 1,178 chained. Structural LINT: WARN (no BLOCK). `public_release_gate.py`: PASS, 0 blocks. Trial record of all staged receipts in a throwaway clone: TRIAL OK. Release battery on a no-hardlinks clone of the final head: see the task record.
- Concurrent conditions: IT29 landed on `main` during the batch (merged in); IT30 worked beside it; the account usage limit stopped all in-flight agents twice.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full text, figures, tables, supplements | No source was read to complete depth; figures captions only; supplements not opened except where a row says so; many rows abstract level | partial | declared in every row's `source_depth` and in `VERIFICATION.md` |
| Main message and contribution | The discordance in WWOX cases is the expected pattern in genetic strata; the white-matter safety record is endpoint-specific; "myelin after onset untested" was a search artefact | strong, after correction | first drafts overreached; corrections traced in RESPONSE.md files |
| Hidden gold beyond keywords | Reviewers' own searches found the post-onset leukodystrophy arms and the 64-child cohort the producers' gene-anchored queries could not reach | partial | the gene-anchored search design is the root cause; named in R1/R2 READMEs |
| Source parity | Case reports, trials, animal studies and abstracts were tabulated with depth labels; abstract rows support leads only | partial | depth vocabulary normalised late (A1, A2) |
| Team type, density, observation versus interpretation | DATO/INFERENZA/IPOTESI labelled per decision line; reviewers moved several INFERENZA that were stated as DATO | partial | |
| Existing claims touched | CLAIM 001, 031, 042 proposals; none applied | strong | locator audit done though not mandatory |
| Multi-hop and corpus cross-query | patient-overlap and cohort-overlap checks done by A1 and the reviewers | partial | the 64-child cohort overlap is probable, unproven |

## Persistence diagnosis

- Durable IDs: task record, challenge ids, row ids; staged receipts with index files; two staged discovery leads; proposals in `integration/`.
- Can a future run tell full text from abstract only? Yes, per row and per receipt.
- Derived surfaces: unaffected (no ledger change); the integrator regenerates after recording.

## Process and capability diagnosis

- Used: map reader, five Scientist packages, blind locator audit, delta audit, adversarial review, author response, staged-receipt validator, trial record, release gate, `discovery_lead.py`.
- Failures and what caught them: see the census.
- Micro-upgrade shipped: none to the engine; two findings handed to the integrator (`scout_daily.py` table limit; diagnosis parser). Process lesson recorded for briefs: add the patient-overlap rule, the public-gate wording rule and "keep scripts in your own scratch folder" to every Scientist brief; ask auditors for a pointer to the governing passage rather than drafted wording; ask every producer for a search not anchored on the question's own gene names.
- Residual risk: Orchestrator narrowing edits (43 fields in three tables) not re-audited; map not independently re-derived; two questions not executed.

## Attribution census

```
ATTRIBUTION_CENSUS
incidents: 18
machine: 3   blind_auditor: 4   peer: 6   self: 5
severity_high: 4   of which self: 2
undetected_known: 0
```

Classes counted once each: machine: a staged receipt over-claiming a complete read (refused by the checker), a browser-style fetch attempted twice by readers and blocked by the permission layer, a file name hidden by an ignore rule; blind auditor: dropped hedges and overshoot, mis-located quotes, omitted material elements, cohort age at imaging written as age at first exposure; peer (reviewers): the myelin-emptiness headline, "four independent cohorts" that were three centres, "start age decides does not survive" inverting the record, unnecessary or colliding vocabulary proposals, schema errors in proposed rows, depth claims contradicting receipts; self: an invented 40-character hash typed into the task record (caught by me with `git rev-parse` before commit), briefs that omitted the overlap and gate-wording rules (found before the readers returned), a reader's plausible replacement quotation written from memory (caught by that reader against the source), forbidden phrases listed verbatim in a compliance report (fixed), repeated `cd` into a peer's worktree (no write). `severity_high` = would have reached the record: the hash, the myelin headline, the start-age sentence, the replacement quotation.

## §21c output

DEFAULTS_TAKEN and STOP_LOG are in the task record `ledger/tasks/orchestrator/ORCH-SCIBATCH-DR-20261105.json` (the missing scientific prompt; the two usage-limit stops; the declined auditor; the IT29 landing). No stop for a reserved act.
