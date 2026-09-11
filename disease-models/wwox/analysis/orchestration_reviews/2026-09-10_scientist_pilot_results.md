# Scientist pilot results — three interventions, measured on the Aqeilan cases

**Written:** 2026-09-11 · **By:** `orchestrator` · index: [`2026-09-10_scientist_improvement_roadmap.md`](2026-09-10_scientist_improvement_roadmap.md).
Every number below was produced by a command run in this session; the command is named beside it.

## 1 · I-1 — two screens exit on nothing screened; a date must be on the calendar (`db35127`)

| | |
|---|---|
| Problem / desired | `genre_discriminator.py --artifact <empty>` and `erratum_scope_check.py --pmid <absent>` wrote honest `INSUFFICIENT_DATA` records and exited **0**; a caller reading the status read a pass. Desired: exit 2, record unchanged, the missing thing named. `external_provenance.date` `2026-13-45` passed the shape. |
| Historical case | NE-2 (C10, the green over an unscreened filename) moved one layer out; Mirror F6. |
| Before (recorded) | `genre … --artifact empty.txt --json` → exit 0 · `erratum … --pmid <absent>` → `examined: 0 … VERDICT: REPORTED`, exit 0 · `external_provenance_defect({date: 2026-13-45})` → `None` |
| After | exit 2 · exit 2 with `missing=PMID <the absent one>` · `its date 2026-13-45 is not on the calendar` |
| Wrong / right case | empty and absent artifact → 2; the module's own 26-page review fixture → `AGREES`, exit 0 (positive control, so refusing everything cannot pass). Absent PMID → 2; an examined manifest with `SCOPE_UNDECLARED` → still 0 (a reading debt, unchanged contract). |
| Entry point | the CLI the brief's M2/M3 names, through the real subprocess |
| Regressions | `test_screen_exit_codes.py` 7/7 (enrolled); `test_deepdive_manifest.py` 186 OK; self-tests 31/31 and 21/21 |
| Mutations | `status = 0` → 2 red · refusal disabled → 2 red · `fromisoformat` removed → 1 red |
| Cannot establish | that the bytes screened were the intended surface |

## 2 · I-2 — the fourth R4 trigger has a gate, and the silent reversal is a diff (`de3628b`)

| | |
|---|---|
| Problem / desired | Mirror F2: `entries[0].proposition` reversed in place + `contradicts_locator: "yes"` → strict validator PASS, 0 gaps. Desired: a declaration is an object naming the prior locator and what changed; unaudited → not a complete read; an undeclared rewrite is visible. |
| Historical case | NE-1 (29724996 Fig 6A). |
| Before (recorded) | the F2 path: PASS 0 gaps; `locator_contradiction_audit.py` 0/0 declared; live corpus carries **0** `contradicts_locator` objects |
| After — validator | string → BLOCK · object without `entry`/`receipt` → BLOCK · well-formed, no audit → `[DECLARED GAP]` (blocks a complete receipt) · audited → complete · with a workspace, a missing prior manifest or entry index → BLOCK · undeclared entries untouched |
| After — history | `--history` over the live corpus: **81 manifests, 125 revision pairs, 240 field changes, 0 declared, 187 same-day (counted), 53 cross-date undeclared (listed)**. `--working-tree` at HEAD: 81 manifests, 0 changes, exit 0; with `--fail-on-undeclared` and a reversed snippet in the fixture: exit 1 naming the entry. |
| Wrong / right case | reversed `entries[0]` no declaration → listed / exit 1; declared object → not a candidate; same-day refinement → counted not listed; no git repository → `INSUFFICIENT_DATA` exit 3 (the first cut reported `manifests=0` as SCREENED — refused by the tool now) |
| Entry point | `deepdive_manifest.py --verify-artifacts --require-current-schema` (M3) and `locator_contradiction_audit.py --working-tree --fail-on-undeclared` (added to the brief's M3) |
| Regressions | `test_deepdive_manifest.py` +7 cases (`ContradictingAPersistedLocatorIsDeclaredAndAudited`), `test_locator_contradiction_audit.py` +6 (`TheSilentReversalIsVisibleAsADiff`, throwaway git repo with dated commits); both suites green; `locator_contradiction_audit.py --self-test` 9 passed |
| Mutations | validator call removed → 5 red · audit always credited → 2 red · `declared=True` → 3 red · `cross_date=True` → 1 red |
| Cannot establish | whether the correction is right; a rewrite before the manifest's first commit; which of the 53 historical revisions were contradictions |

## 3 · I-3 — a derived surface binds to committed inputs or refuses (`4810628`)

| | |
|---|---|
| Problem / desired | NE-6: generators read whatever is on disk. Desired: refuse to write over an uncommitted input, name it; allow with a stated reason; never a silent pass outside git. |
| Before (recorded) | no generator asked; `a8a6a1d` asserted cleanliness in prose |
| After — live | four surfaces regenerated on this checkout: `inputs BOUND … committed at de3628bd3bf1`, all byte-identical (`git status disease-models/` empty). An untracked `PMID00000000.json` under `deepdive_manifests/` → `pathograph.py --out --export` **REFUSED, exit 2**, the file named. |
| Wrong / right case | modified input → DIRTY exit 2 · untracked input (C22's exact shape) → DIRTY · committed → BOUND exit 0 · reason given → proceeds, reason and files printed · blank reason → refused · the surface being written and its generated siblings excluded · no git → UNBOUND, proceeds, named |
| Entry point | `batch_queue.py`, `coverage_report.py`, `reading_state.py` (`--out`), `pathograph.py` (`--out`/`--export`); `prompt_batch_commit.md` phase 4.7 carries `--inputs-dirty-because` |
| Regressions | `test_derived_inputs.py` 11/11 (enrolled); generator suites green; `test_batch_queue` red only on the inherited ratchet; `test_generated_surfaces_are_regenerated.py` green |
| Mutations | DIRTY never reported → 6 red · guard call removed from `reading_state` → 1 red · untracked ignored → 3 red |
| Cannot establish | whose the uncommitted file is; a wrong committed input |

## 4 · The benefit, with numerators and denominators

| Measure | Value | Command |
|---|---|---|
| Historical near-errors now refusable by a machine on their own fixture | **5 of 6** — counted from `data/2026-09-10_scientist_incident_controls.jsonl` (rows written by `deepdive_manifest.py`-, `test_screen_exit_codes.py`- and `test_derived_inputs.py`-backed fixtures) of rows whose `improvements[].status` contains `collaudato` (NE-1 declared half, NE-2, NE-4 as WARN, NE-5, NE-6); NE-3 needs the audit | `data/2026-09-10_scientist_incident_controls.jsonl`; this file § 1–3 |
| Correct cases wrongly refused | **0** observed: four live surfaces regenerated BOUND and byte-identical; 186 + 20 + 11 + 7 validator/audit/guard/screen tests green; the review fixture `AGREES` | suites named above |
| Cases left unexaminable, named as such | history without git → exit 3; guard without git → UNBOUND; screens over nothing → exit 2 | — |
| Additional verification cost | `--working-tree` over 81 manifests: under 2 s; `--history`: ~40 s (125 `git show` pairs); the guard: one `git status` per write | timed in session |
| Controls actually used in readings | **none yet by a Scientist** — no wave ran after they landed; the brief's M3 now names them | — |
| Undeclared historical revisions surfaced | 53 cross-date (review queue) / 240 total | `locator_contradiction_audit.py --history --json` |

## 5 · Battery, gate, publication

Release battery at `7e6e58c` (`scripts/run_release_regressions.py`): `FAIL` on exactly the two inherited reds — `test_batch_queue` (ratchet; operator's `BATCH_COMMIT`) and `test_surface_census` (gitignored evidence) — over 105 suites (103 at baseline + `test_screen_exit_codes.py`, `test_derived_inputs.py`); nothing green before is red after. `legend_lint.py .` PASS; `growth_anchors.py check` PASS; `fulltext_receipts.py verify` OK 156. Gate and push on the final SHA: task record `battery_and_publication`.
