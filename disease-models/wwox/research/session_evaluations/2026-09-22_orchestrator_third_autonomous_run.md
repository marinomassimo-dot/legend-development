# Session self-evaluation — 2026-09-22, Orchestrator, third autonomous run

> Written **before** capability-scout and takeaways, per the rule that takeaways written first
> describe a session that went well. Non-canonical. Nothing here is medical advice.

## Scope and executable verdict

- **Batch/session:** third autonomous scientific run. Eight delegate waves plus direct Orchestrator
  work. Head `3c4759e`, landed on canonical `main` and on the task branch at every step.
- **Studies and complete-read receipt IDs:** one new receipt persisted —
  `FTR-20260922-30202070-01` (Schultz 2018, `partial_fulltext_read`, six verbatim locators).
  Bodies additionally retrieved and adjudicated without new receipts, against records already at
  full-text depth: `PMC6296882` (PMID 30362252), `PMC3354054` (PMID 22193544).
- **`session_self_eval.py`:** **PASS** — *"every complete read has landed and every declared output
  resolves."* 189 receipts, 84 complete-fulltext events, 72 active complete reads,
  `unread_premises: 0/0`.
- **Per-study manifest(s):** no new manifest. Two declared gaps opened by today's use of
  `PMID22193544.json` — it should gain the microtubule-assembly and Methods locators, and its
  existing entries declare no `surface`. Recorded, not silently absorbed.
- **Receipt verification:** `fulltext_receipts.py verify` → **OK: 189 chained, tail anchored.**
- **Structural LINT:** **PASS** (one `[INFO]`, background-only wikilink).
- **Local verdict:** **PASS.** Growth anchors PASS with `unread_premises=0`; publication gate PASS,
  0 blocks; prose `FT-` references unresolved **0**; `test_tool_routing.py` 7/7.
- **Workspace/global verdict and concurrent conditions:** `run_release_regressions.py` clean. Its
  only non-passes are declared environment skips — no PyMuPDF, no numpy, shallow clone, `files/`
  gitignored — the **KNOWN ENVIRONMENT** class, not new failures. Two Scientists running at the
  time of writing; the run was taken on a quiet tree.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | Three bodies read end to end. **Figures and supplements not read in any of them** — the route strips every `(Fig.)` number. Declared in the receipt rather than glossed. | `partial` | No figure-panel claim made anywhere today |
| Main message and original contribution | Each read was adjudicating a *named proposition*, not surveying. Schultz → reagent sensitivity; Davids → what the body says vs the abstract; Wang → which way the Tau arrow points. All three returned a different answer from the one expected. | `strong` | — |
| Hidden gold beyond keywords/abstract | 🔴 The three highest-value findings were **all** invisible to keyword search: an abstract/body divergence, a 27-day-old queued candidate, and an empty cell in a 2009 table. | `strong` | — |
| Source parity: context, type and recency | Two paywalls correctly distinguished from route failures (24369382, 21476439); the 2011 enzymology treated as a real historical result and **not** promoted to a disease-allele assay. | `strong` | — |
| Team type, field density, observation vs interpretation | Domain-G field densities carried positive controls throughout. The Łódź↔enzymology capability mapping is new and was not visible from either side alone. | `strong` | — |
| DATO / INFERENZA / IPOTESI separation | Held under pressure: the exon-9 in-frame call is labelled `PREDICTED` even though it is favourable, and the exon-7 one was killed **because** the separation was enforced. | `strong` | — |
| Existing claims touched; conflicts/revival triggers | `CLAIM 005`, `037`, `033`, `035`, `019`, `PAPER 044`, `DL-MECH-033/037/045`, `HYP-08`, `DIS-010`. One `REVIVAL_TRIGGER` proposed. **No canonical file modified.** | `strong` | Ten candidates queued, none propagated |
| Multi-hop and corpus cross-query | 🔴 **`failed` in one specific way, and it is the session's signature defect:** three findings already existed in the repository and were re-derived. The cross-query that would have found them is *"which claims share this entity"*, not *"which papers do I remember"*. | `failed` | See `D-25`, restated |

## Persistence diagnosis

- **Durable ledger/registry IDs and wikilinks:** `FTR-20260922-30202070-01`; queue entries
  `FT-128`…`FT-131`; candidates `CC-20260922-CLAIM005-CHAIN-NAMING-01`,
  `-HYP08-LYSOSOMAL-ARM-01`, `-SEIZURE-ASCERTAINMENT-01`, `-SPLICE-ARM-01`, `-TAU-DIRECTION-01`,
  `-EXON7-NATURAL-EXPERIMENT-01`, proposing `D-25`…`D-30`.
- **Reading queue/debt:** four new entries, all with depths declared per row. `FT-129` exists
  **because the ratchet caught me**, not because I volunteered it.
- **Dossier and commit candidate:** an append-only correction written into
  `fulltext_dossiers/PMID30370248.md`, whose prior diagnosis was wrong in the direction that
  suppressed a live contradiction.
- **Receipt source fingerprint, coverage and supplement state:** `source_fingerprint: null` for the
  MCP route — no durable local artefact exists in this deployment and the receipt says so. Coverage
  declares figures/supplement/references `not_read` with the extraction defect named as the cause.
- **Can a future run distinguish full text from abstract only? How:** yes — every finding today is
  labelled `full-text` or `abstract-depth` at the point of use, and the three unacquirable papers
  (`24369382`, `21476439`, `18216017`) are recorded as **unacquirable**, not as unread, so no future
  run spends routes on them again.

## Process and capability diagnosis

- **Skills/gates/patterns used:** `legend_lint`, `growth_anchors`, `fulltext_receipts verify|record`,
  `public_release_gate`, `run_release_regressions`, `test_tool_routing`,
  `manifest_queue_id_crosscheck --prose`, `session_self_eval`.
- **Plausible skills deliberately declined, with reasons:** `legend-commit` — ten candidates is above
  its ≥5 trigger, but one is **MAJOR and states it requires operator authorization**, and several
  touch `consolidated baseline` claims at R3/R4. Propagating around a 27-day-old unapplied MAJOR
  would be the worst possible move. `find-fulltext` — declined for the three papers measured
  unacquirable; a cascade cannot defeat a licence.
- **Failures, retries, extraction mismatches or concurrency events:** two Scientist launches died on
  server **529**s having written nothing (**LOST**, not PARTIAL — verified by `git status`, so no
  partial conclusions were inherited). Extraction defects hit in three new token classes: figure
  numbers, kDa values, and the Greek subscript in `GSK3β`.
- **What caught each failure before an overclaim:** the ratchet (once, on me); reading the
  repository before writing (four times, twice on me); retrieving the primary body instead of
  accepting a hand-back (three times); computing rather than asserting (the exon table).
- **Disease-agnostic micro-upgrade shipped:** `manifest_queue_id_crosscheck.py --prose` — the
  RESOLVES check extended from manifest fields to commit candidates, ledgers and analysis files,
  after a candidate was found citing an `FT-` entry that was never written while every gate stayed
  green. **The upgrade, not the promise of one.**
- **Regression/evidence that makes the upgrade persistent:** five regressions plus a live-corpus
  assertion, **mutation-tested three ways and each mutation caught** (scan returning nothing → 2
  failures; dropping the queue-file exclusion → 2; dropping zero-padding canonicalisation → 1).
  21/21 pass restored; routed in `framework/scripts/README.md`.
- **Residual risk and next decisive action:** the residual risk is that **ten candidates sit
  unpropagated behind one unapplied MAJOR**, and the gap keeps widening. The next decisive action is
  not mine: `CC-20260826-SEIZURE-RECONCILIATION-01` needs an operator decision.

## Attribution census — required, fixed, parseable

```
ATTRIBUTION_CENSUS
incidents: 9
machine: 2   blind_auditor: 0   peer: 1   self: 6
severity_high: 3   of which self: 3
undetected_known: 3
```

**Counting, so the numbers can be argued with.**
`machine: 2` — the `UNREAD_PREMISE` ratchet returning 10 against my predicted 0; LINT refusing
`FT-128` for a missing identity line. `peer: 1` — Scientist D establishing that the seizure
contradiction was already held in a 27-day-old candidate, against my framing of it as new.
`self: 6` — the near-landed *"never propagated"* finding; the `D-25` §2 misframing; the
`26345274`/`30361190` count-quote conflation; the exon-7 hypomorph; the dangling `FT-112` pointer;
the `C-2` false alarm refused before landing.
`severity_high: 3` — the *"never propagated"* finding (headed for `D-26`), the count-quote
conflation (**landed**, corrected same day), and the exon-7 hypomorph (**landed**, withdrawn same
day). All three self.
🔴 `undetected_known: 3` — and this line is the point of the census. Three defects found **today**
were attributable to **earlier waves**: `PAPER 044` quoting an abstract's *"nonsense-mediated
decay"* inside a record declaring a complete full-text read; the `PMID30370248` dossier explaining
away a live contradiction; and `CC-20260921-WWOX-ENZYMOLOGY-P306-01` pointing at an `FT-` entry that
never existed. **A corpus reporting `0` on this line is reporting the limit of its census, not the
absence of defects.** This one does not.

## §21c output

```
DEFAULTS_TAKEN
- Two Scientists lost to server 529s: treated as infrastructure under §27, not a scientific stop.
  Relaunched rather than escalated; verified LOST not PARTIAL before relaunching.
- Ten candidates held unpropagated rather than running BATCH_COMMIT, because one queued MAJOR
  states it requires operator authorization and several targets are R3/R4.
- Three papers recorded as UNACQUIRABLE rather than unread, after a measured licence check.
- PMID 30362252 and 22193544 adjudicated against named propositions without new receipts, both
  records already carrying full-text-depth receipts; declared in each candidate.
- c.1061 left unresolved rather than inferred from what the prediction requires.
```

```
STOP_LOG
- No STOP-A…STOP-E condition was reached.
- No reserved act was performed: no researcher contacted, no cells requested, no funds committed,
  no access purchased, no external representation, no individual-level data touched.
- Acquisition of PMID 24369382, 21476439 and 18216017 is HUMAN_REQUIRED in the purchasing sense
  only; per §27 the science around them proceeded and is recorded.
```
