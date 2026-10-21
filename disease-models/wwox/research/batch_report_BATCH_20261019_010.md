# BATCH COMMIT REPORT — BATCH_20261019_010

> **A citation-repair batch: four live sentences cited detection rules that never existed.** Harness Engineering (ACTOR_ID `plan`, `PLAN-SURFACE-RANKING-20261021`) established by measurement that no row for any id from `D-27` to `D-36` has ever existed in this repository, appended the allocator addendum that maps each id to its state, and stopped — repairing the citations and deciding the rows are `BATCH_COMMIT` acts. This batch does the first and decides the second. Integrator: ACTOR_ID `orchestrator` (stated assumption), task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation. **Not medical advice.**

## Summary

- Type: MANUAL, **MINOR**. Pre-flight LINT `WARN` (0 BLOCK); post-propagation LINT `WARN`, **0 BLOCK**.
- **WM version: `WM_v7.27` PRESERVED — no bump, and the rule is the reason.** `state_manifest_current.md` § 2 bumps `working_model_version` for *"every `BATCH_COMMIT` that modifies the disease model"*, and `prompt_batch_commit.md` § 4.6 preserves the version, the WM timestamps and the WM changelog rows for a batch with no disease-model change. A detection-rule id cited in a research ledger's prose changes no claim, no block, no `Status`, no `Type`, no `Summary`, no support and no uncertainty; § 4.6's carve-out (*"status changes affecting evidence eligibility, claim meaning, support or uncertainty are not structural corrections"*) does not reach it. This is the same reasoning `BATCH_20261019_009` applied to a provenance sentence, applied to the same kind of object. So the version line, its date, the `Last update` note and the `Changelog` row of `working_model_history.md` are all **untouched**.
- Commit candidates: **none.** The scope is a cross-surface citation defect reported by another actor, not a candidate.
- Snapshot `backup/20261021_batch010` (not committed); pre-batch commit `167d6a4e352e078631300ee0690904facb878141`. No restore used.
- `FULL_FALLBACK`: **none.** All four op lists — discovery ledger 3 ops, full-text queue 1 op, dismissal ledger 1 op, batch-008 report 1 op — accepted by the record-scoped editor on the first dry run. No `reflow`, no `to_eof`.
- Receipts: 685 chained, untouched.
- **Ratchet, before and after:** `scripts/test_detection_rule_citations_resolve.py` **PASS before, PASS after**; unresolved citations **0 → 0**; declared `NEVER MINTED` debt **4 → 4** (`D-31`, `D-33`, `D-35`, `D-36`). It did **not** tighten, the reason is structural and stated below, and the baseline was **not** edited.

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_010.md` (this report); `backup/20261021_batch010/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation |
|---|---|
| `research/discovery_ledger_current.md` | **3 ops, 2 records.** `DL-MOL-005`: the `D-33` / `D-35` citation repaired in place. `DL-MECH-011`: the two `D-31` citations repaired in place. Each repair states that the id was **proposed and never minted**, names the candidate its formulation lives in, quotes that formulation, and quotes the wording it supersedes, per `prompt_batch_commit.md` § 7.2 |
| `research/full_text_queue_current.md` | **1 op.** `FT-142`: the `D-31` and `D-36` citations repaired in place, same three things, with `D-36`'s formulation (*the model-horizon / therapeutic-window distinction*) quoted from its candidate |
| `research/dismissal_ledger_current.md` | **1 op, append-only inside the allocator addendum.** The mint decision and its three reasons recorded where the next allocator reads them, plus the consequence for the ratchet. **No row added, removed or renumbered; the addendum's mapping table is untouched** |
| `research/batch_report_BATCH_20261019_008.md` | **1 op.** Its recommended-action 4 said the four ids were *"still unrepaired"*; corrected in place with the old wording quoted |
| `framework/state/state_manifest_current.md`, `state_history.md` | last-batch and last-LINT fields; `batch_20261019_010_scope` / `_candidates`. **`working_model_version` deliberately unchanged** |
| derived surfaces | `coverage_report`, `batch_queue`, `pathograph` (inventory and export), `reading_state`, `surface_census` regenerated from the committed inputs — **all five came back byte-identical**, which is the expected result of a batch that edits research prose and no registry record |

## FILES UNCHANGED

All four scientific current files — `working_model_current.md`, `working_model_history.md`, `claim_registry_current.md`, `paper_registry_current.md` and `literature_tracking_log_current.md` — are untouched, and so are `disease_model.md`, the `meta_*` files, the research lines, the biomarker, endpoint and therapeutic files, the receipt ledger (685), the DisMech sidecar, `growth_anchors.jsonl` (no structural count changed, so no `record`), every commit candidate, and `scripts/test_detection_rule_citations_resolve.py` — **the ratchet's code and its baseline were not touched, which is the point of a ratchet whose baseline lives in the content**. `capability_scout_log.md` and the `DEFAULTS THAT BIT US` rows themselves are also unchanged (see DEFAULTS_TAKEN 3).

## CHANGE LOG

1. **The defect, re-measured before it was repaired.** `git log -S'| **D-31** |'` and its siblings return zero commits; the addendum's mapping table is the state of record. On live surfaces (the suite's own definition: `git ls-files`, minus dated-record directories) the dangling ids are exactly `D-31`, `D-33`, `D-35`, `D-36`. The three renumbered ids are **not** dangling on any live surface: `D-32` and `D-34` are cited nowhere outside dated records, and `discovery_ledger_current.md`'s single `D-30` mention already reads *«vedi `D-26` (citato come il proposto `D-30` in quattro file di analisi)»* — it points at the id the rule actually carries and needed nothing. So **no citation in this batch's scope required a renumbering repair**; all four required the never-minted statement.
2. **Four citations repaired, each self-sufficient.** A reader meeting `D-31`, `D-33`, `D-35` or `D-36` in either file now learns, in the citing sentence, that the number is not a row, which candidate holds the formulation, and what the formulation says. `D-31` → `CC-20260922-POSTDIAGNOSIS-WINDOW-01` § 1, *«the set of ages an experiment tested is not the window it measured»*. `D-33` → `CC-20260922-TX007-DOSE-CHALLENGE-01`, *«a within-study control is not a replication, and a predecessor from the same laboratory is not independent corroboration»*. `D-35` → `CC-20260922-GTGT-CNS-QUALIFICATION-01` § 4, *«do NOT downgrade measured rescue because replication is absent»*. `D-36` → the same candidate § 4, never infer *«not performed because the animal could not survive long enough»* → *«biologically ineffective after that age»*.
3. **Nothing was improved while the hand was in there.** Each op is a `replace-within` on the defective fragment; three of the four are pure insertions that remove no byte of the original sentence, and the fourth (`FT-142`) adds a line and leaves both existing lines intact.
4. **The stale report sentence withdrawn where it was published**, in place, quoting the wording it replaces.

## DEFAULTS_TAKEN

1. **No WM bump**, for the reason stated in the Summary and derived from the two normative texts, with `BATCH_20261019_009`'s precedent cited as a precedent and not as the authority.
2. **No `growth_anchors.py record`:** no structural count changed (claims 47, papers 418, corpus 376, literature 681 — identical to the post-009 anchors). The registry scale acknowledgement was not renewed; nothing was asked for.
3. **`capability_scout_log.md` and `batch_report_BATCH_20261019_008.md` were measured, not assumed, to be out of scope as citing surfaces.** Both name the four ids, and the suite counts them as live surfaces. Read: both already describe the ids as *dangling* — they are correct statements **about the defect**, not citations **of a rule**, so neither needed the never-minted statement. Only the one sentence of report 008 that asserted the defect was still open was corrected, because that assertion stopped being true today.
4. **The snapshot was extended by hand.** `batch_commit.py snapshot` reads the declaration in `prompt_batch_commit.md` Phase 3, which does not name the three research ledgers this batch edits, so the snapshot held none of them. They were copied into `backup/20261021_batch010/` by hand and the base-qualified `git checkout 167d6a4e352e078631300ee0690904facb878141 -- <path>` route was the restore of record, exactly as Phase 3 prescribes for a path the snapshot does not hold. **Reported, not fixed:** adding those paths to the Phase 3 declaration is a protocol edit, it belongs to whoever owns that drift (the same drift Phase 3 records for 2026-09-28), and a repair batch is not the place to make one.
5. **Op form:** one op per defective fragment, so no byte outside those sentences moved and no `reflow` or `to_eof` had to be asserted.

## DECISIONS_TAKEN

🔴 **The four rows are DECLINED, not minted. Three reasons, weighed in the order of their weight.**

1. **Two dated batches already decided this the other way, deliberately, and nothing has been measured since that they did not have.** `CC-20260922-MODEL-HORIZON-01`'s disposition records that the batch which minted `D-21` rewrote the candidate's `D-31` reference *«as prose, because no such row exists in this ledger»* — it saw the dangling number and chose prose over a row. `CC-20260922-GTGT-CNS-QUALIFICATION-01`'s records that *«the `D-35` and `D-36` dismissal rows are operator directives and this batch skips the optional D-rows»*. Minting now would reverse two adjudications of 2026-09-27 on no new evidence, which is the shape of a decision made for tidiness.
2. **The substance is already where it is read, and now in four more places.** `D-21`'s cost cell carries the window lesson in prose; `DL-MOL-005`'s own append-only rectification **is** the `D-33` lesson applied to the datum it governs; and after this batch each of the four citing sentences carries its formulation verbatim. A row would create a second home for wording whose only source is a **closed** candidate nobody propagated — and the one thing the brief forbade is improving that wording, so the row would be a verbatim copy of prose that lost its own propagation.
3. **`harness_development_principles.md` answers a mistake with a habit or a tool rather than with more rows, and both already exist** — the allocator addendum, and a ratchet that goes red on a fifth dangling citation. The `D-26` row refuses the same purchase in its own words: *«no gap `D-27`–`D-30` is created for tidiness»*.

🔵 **The honest cost of declining, stated rather than buried.** Four rules that four live sentences wanted are not in the table, so they cannot be consulted by a reader who opens `DEFAULTS THAT BIT US` and reads down it — which is how that table is used. The decline is only defensible because the repair makes each rule usable **at the point of use**, and that is why the formulation is quoted in every one of the four sentences rather than merely referenced. If a fifth surface needs one of these rules, that is new evidence of demand and the next integrator should mint it; this report is the record that the question was decided once, on these grounds, and not avoided.

🔴 **Why the ratchet does not tighten, and why that is not a defect of the repair.** The suite's unresolved set was **0 before and 0 after**: it was already 0, because the addendum's declaration is what resolves the four citations. Its declared-debt counter was **4 before and 4 after**, and a complete citation repair **cannot** lower it — `test_every_id_the_addendum_declares_never_minted_is_actually_cited` requires every declared id to remain cited from a live surface, so the only way to lower the count is to **mint** a row (then the addendum row stops saying NEVER MINTED and the suite tightens by itself) or to delete the citations, which would destroy the sentences that need the rules. The brief's expectation that a complete repair tightens the suite holds for the *minting* branch; on the *declining* branch the counter is structurally pinned at four. **The baseline was not edited**, in the test or in the ledger's mapping table. What the repair changes is something the counter cannot see: four numbers that resolved only by a reader finding the addendum are now four sentences that carry their own rule.

🔵 **One measurement that corrects the brief, reported rather than quietly worked around.** The brief said to point a citation at the renumbered id *«where one of the three renumbered rules is meant»*. Measured on the two files: no live citation of `D-30`, `D-32` or `D-34` needs that repair — `D-32` and `D-34` are cited on no live surface at all, and the single `D-30` mention already names `D-26` as the canonical id. All four repairs are therefore of the never-minted kind.

## Verification

`legend_lint.py`: `WARN`, **0 BLOCK** (exit 0). `fulltext_receipts.py verify`: OK, **685 chained**, tail anchored. `growth_anchors.py check`: **PASS** (claims 47, papers 418, corpus 376, literature 681, registry-only 4, unread premises 0). `public_release_gate.py`: **PASS, 0 BLOCKS**. `scripts/test_detection_rule_citations_resolve.py`: **6 tests, OK**, before and after. The five derived surfaces regenerate byte-identical. No e-mail string, no truncated digest and no study-identifier literal outside the lines already present. **The full release battery was not run — the Orchestrator runs it.**

## Recommended next actions

- **The capability gap named by `BATCH_20261019_009` stands**: nothing re-derives a count a registry record asserts about a manifest, a ledger or a figure.
- **If a fifth surface ever needs `D-31`, `D-33`, `D-35` or `D-36`,** mint that one row from its candidate rather than re-deciding the whole set: demand from two independent surfaces is the evidence this batch did not have.
- **The Phase 3 snapshot declaration does not name the three research ledgers** that batches now routinely edit (DEFAULTS_TAKEN 4). Worth one line of protocol edit by whoever owns it.
