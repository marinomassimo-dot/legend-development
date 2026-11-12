# HE46 — conditions, propagation, generative capacity (Harness Engineering, 2026-11-11)

Non-canonical. Harness work: generic components and checks. Scientific meaning stays with SCI46 and IT46.

## 0. What HE45 left, read on the real tree (H0)

Closure: HE45 COMPLETE and landed (f76439c2, CI #652 success); IT45 COMPLETE (142f6c5f, CI #655 and publication #34 success); SCI45 N1 consumed by IT45 (INV-18 burst/NMDAR arm). Nothing of HE45's units, cache, loader or roles was redone. Each component, as *available*, *called* and *able to change a result*:

| Component | Called by | Changed a result? |
|---|---|---|
| `assay_conditions.py` (reader and comparer) | exactly one consumer path: `comparison_engine.compare_props` (an earlier search listing three research scripts matched only column names such as `assay_conditions_that_decide`) | yes: IT45 `p1_comparisons_it45.md` (COMPARABLE 4 to 0, CONDITIONS_INSUFFICIENT 0 to 1, NO_POTENCY_PAIR 0 to 4). No investigation, card or need text was found that reads the states |
| `CONDITIONS_INSUFFICIENT` | `comparison_engine.derive`, merged weakest-wins; read by IT45 p1 and p4 tables | yes, in those tables only |
| `measurement.summarise` | `activity_search.py` (one call) | yes: IT45 S10 read recovered 7 catalogue-status molecules that the capped read lost (Potency flood) |
| shared ChEMBL cache and adapter | `activity_search.py` | yes: IT45 dose-response read 1 min 32 s for three targets |
| `unqualified_entity` | `entity_roles.role_of`, `eval_it44.py`, `effect_roles.py` | yes: IT45 counts 197 default rows no longer shown as candidates (the reference cannot confirm it: section 6) |
| `hypothesis_package.load_comparison` (engine/ loader) | `comparison_engine`, `consume_reader.py` | yes for the four registered comparison packages; `glun2b_comparators_sci42_20261110` (the only package with pH propositions) is not registered and has no comparison table |
| the corrections of SCI45 (Imin, TASK-3) | INV-18, IT45-Q05, the view | yes; two older SCI44 documents were not reached until section 2 |

## 1. pH and temperature in the conditions reader (H1, H4)

**What was missing.** HE45 left pH and temperature out of `framework/scripts/assay_conditions.py` and said so. The comparison packages do carry them: 14 of 122 proposition cells state a pH or say it is not stated, 28 state a temperature (`decisive.tsv` of nine packages). SCI45 asked for a pH axis (consumer delta row 10; SCI45 delta rows 10 and 6 for the pH and Mg2+ axes).

**What the reader now does** (read from the wording of those cells, not a universal parser):

| Case in the packages | Reading |
|---|---|
| `pH 7.6 or 6.9 set with HCl` (a series) | `pH` values 7.6 and 6.9; agrees only with an equal series; `pH 6.9` against the series is INSUFFICIENT (one value of a series is not the series) |
| `pH 7.4` / `pH 7.3` | absolute, equal → agreement, different → documented incompatibility; never goes through the nM table |
| bath / aCSF / buffer / recording solution against pipette / internal | `pH_extracellular` and `pH_intracellular` are separate fields; a pH with no side meets the extracellular one only when the values are equal (note: "side stated on one side only"); when they differ the side may be the reason, so INSUFFICIENT, not an incompatibility |
| `pHo step (7.4 to 7.1, with 7.7)` | `pH_step` (baseline, target); never an absolute value |
| `a 0.2 pH unit fall` | `pH_delta`; never an absolute value, and a step never agrees with a difference |
| `pH 7.4 to 7.2` with no word saying range or step | left in `unplaced`: not guessed |
| `(pH not stated)`, `no Zn2+ or pH stated`, `temperature ... not in the abstract` | `NOT_STATED`; `pH not applicable` is `NOT_APPLICABLE` (kept apart; the reasons say "declared not stated" or "declared not applicable" on the other side) |
| `30-32 C`, `35 C`, `room temperature` | `temperature_C`; room temperature is read as 18-26 C and the reason says so (35 C against room temperature is documented incompatibility; 23 C against it is not decidable) |
| `Fura-2 loading 37 C`, incubation, slicing, storage | not the assay temperature: kept in `unplaced` |
| `transfer to a slice (bicarbonate buffer, 35 C, Mg2+) is untested` (glun2b D17) | a contrast clause: not applied, listed under `contrast`. The proposition inherits D09's 23 C through `As D09` |
| `As D09; 35 C`, `As D09; pH 7.4` | a local override replaces only the field the cell states |
| reference to a missing or circular proposition | named in the reasons and in `unplaced`; the pair cannot read as agreement |

**Before and after on the real tables** (`conditions_before_after.py --old-ref 142f6c5f`, same inputs for both runs):

* Compound-level `comparison_state` of the four registered comparison packages: 67 rows, **0 changed** (3 NOT_COMPARABLE, 1 CONDITIONS_INSUFFICIENT, 8 NO_POTENCY_PAIR, 55 SINGLE_OR_NONE unchanged). **No compound decision changes.** The pH axis is not exercised by any registered package: the pH-bearing propositions are in `glun2b_comparators_sci42_20261110` (no comparison table, not registered) and in `ro25_6981`, where pH 7.4 appears on both sides of every pair that carries it.
* Every pair of propositions inside each of nine decisive tables (898 pairs): 8 change state, 890 do not (`conditions_pairs_before_after.tsv`). One agreement falls to INSUFFICIENT (glun2b D08 against D11: pH 6.9 stated on one side only, previously a documented agreement the text did not support). Seven INSUFFICIENT become documented incompatibilities, all through temperature (ampa D15 at 4 C against slices at 30-34 C; chloride P01/P03 at 35 C against P08 at 32-34 C).
* So: the reader is now able to refuse a false agreement and name a temperature or pH difference, and on the tables that exist today it changes no compound decision. It is a capability for the next comparison (SCI46 is expected to bring pH and Mg2+ conditions), not a correction of an existing result.

Tests: `framework/scripts/test_assay_conditions.py` (37, 15 new, each from a wording found in the packages).

Remove: revert the commit of `assay_conditions.py` and its test; no data file depends on it, `comparison_engine.py` calls `parse`/`compare` unchanged.

## 2. A correction followed to its consumers: TREK-1 residual current (H2)

Case: SCI45 `ph_k2p_sci45_20261111`, dated update after the Q1 verification. Bagriantsev 2011 (21765396) Table S1 gives mouse TREK-1 pK1/2 7.51 and **Imin 0.25** (residual current at acid); with it a pool of 0.53 loses 0.03-0.18 for a 0.1-0.3 unit fall of pHo, never the 0.28 of the Wwox pair (first run, Imin 0, had let slope 2 reach it).

| Link | Where | Carries the corrected value or conclusion? |
|---|---|---|
| source | Bagriantsev 2011 Table S1 (read by the Q1 verifier V6; receipt `k2p_pointers_sci45_20261111/verify/receipts/FTR-20261111-21765396-85.json`) | origin |
| parameter | `ph_k2p_sci45_20261111/size_check_imin.py`, `size_check_imin.tsv` | yes (24 rows with Imin 0.25 reproduce from the formula: `test_trek1_correction_reach.py`) |
| analysis | `ph_k2p_sci45_20261111/README.md` answer 2, dated update; `output/premises.tsv` row 6 | yes; answer 4 carried a slope-1 bound as "at most 0.04": clarified by a dated line (0.03-0.08) |
| hypothesis | `output/hypotheses.tsv` KP1 context | yes ("partial contributor only, size check with Imin 0.25") |
| delta | `consumer_delta.md` rows 1 and 2 | yes |
| investigation | INV-18 `next_test` "[IT45 from SCI45] ... partial contributor only (TREK-1 Imin 0.25)" | yes |
| open questions | IT45-Q05 | yes (excluded below 0.1 unit, partial contributor above) |
| dashboard | `view/index.html` and `content_source.json` (two hits of "Imin 0.25") | yes |
| card / brief | no compound card and no next brief carries a TREK-1 pool statement (the K2P tools are not in the catalogue; `next_brief_sci45` is about NMDA and ASIC) | not applicable |
| **older consumers** | `pdh_pdk_sci44_20261110/S7_coda.md` section 5 (the TASK-3 "new chain through pH"); `kchan_expression_sci44_20261111/README.md` ("points ladder step 2b toward TASK-3 and TREK-1 tools") | **no, until now.** SCI45's delta row 5 asked for a dated update of the coda; IT45 consumed rows 1, 5, 6 and 11 in INV-18 but the coda itself was not touched. Both now have a dated Update line (original text kept) pointing at the SCI45 package and at INV-18 |

Outcome: the correction had reached INV-18, the open question and the dashboard; it had not reached two earlier SCI44 documents that still described the refuted TASK-3 route as current. Remedy proportional to the defect: two dated lines, one clarification, one test of three assertions. No versioning system, no new register. The experiments and preregistrations of SCI45 are not rewritten.

Remove: delete `test_trek1_correction_reach.py`; the dated Update lines are history and stay.

## 3. A hypothesis nobody could reach (H3, with IT46)

**Path chosen:** physiological hypotheses written by Scientists in their own table layout, to the generation that reads `hypothesis_package.py`. The loader required `hyp_id` plus `alternatives.tsv` and `experiments.tsv` (an absent file stopped the read), so a package with another layout could not be registered at all; five packages with 24 hypotheses sat outside the manifest (`check` listed their names only).

| | before | after |
|---|---|---|
| hypotheses returned for INV-18 | 3 (MH1-MH3) | 3 + 13 in their own layout: SCI43 KH1-KH5 (key `hyp_id`), SCI45 KP1-KP5 (key `id`), HCN HY1-HY3 (key `hypothesis_id`) |
| hypotheses returned for INV-08 (NRF2/KEAP1) | 0 | 6 (`nrf2_inv08_20261107`, key `hyp_id`) |
| `check` on unread folders | names | names and counts: `gsk3_eif2b_20261107 (5 hypotheses unreachable)` |

* Link: manifest role `hypotheses_only` (four rows added to `hypothesis_packages.tsv`; this is the delta row 9 consumer edit of SCI45 for KP1-KP5, made here because it is a loader registration, not a scientific edit). Rows are verbatim, with their file:line; the key is `package::key` because local ids repeat (H1 appears in three packages); duplicates in one table, a missing key column and an empty table are stated, never hidden.
* **Second input.** The same path reads packages with three different key columns and no compound in common (K2P/pH tools, Ih blockers, NRF2/KEAP1 hypotheses), and a synthetic package with unrelated ids and names (`ZQ1`, `tool-alpha`) in `test_hypothesis_package.py::HypothesesOwnLayout`: nothing in the path depends on a compound name or on `KP1`.
* Not registered: `gsk3_eif2b_20261107` (its README names INV-02 once and the subject is GSK3 (INV-09): two investigations, the manifest takes one; left to the Orchestrator); `aed_compare_it31_20261107` has no hypotheses table; `nmda_asic_ph_sci45_20261111` has none either (`net_sign.tsv` is a computed table, not hypotheses), so it is not a `hypotheses_only` package.
* What the loader does **not** do: it maps no column. Which cell of a KP row answers which question of a conditional proposal (observation, relation, premise, action, expected result) is the consumer's choice. IT46's generator (`conditional_proposals`) still reads only `record_for`; until it also calls `hypotheses_for(pk, inv)`, the 13 + 6 rows are reachable but not yet used. Trace for IT46:

```
python3 framework/scripts/hypothesis_package.py check            # 39 rows over 10 packages; unread folders with counts
python3 framework/scripts/hypothesis_package.py show --inv INV-18   # block "hypotheses in their own layout"
python3 -c "import sys; sys.path.insert(0,'framework/scripts'); import hypothesis_package as hp; r=hp.hypotheses_for(hp.load_all(),'INV-18'); print(len(r['rows']), r['rows'][0]['columns'])"
```

Remove: delete the four `hypotheses_only` rows of `hypothesis_packages.tsv` (the loader then returns what it returned before) and revert `hypothesis_package.py` and its test.

## 4. Reading debts and provenance (H5)

**The three S10 readings IT45 reports as not recorded** (PMIDs 38116420 [Markovtsov 2023], 31411465 [Tran 2019], 21964340 [Dawson 2011]; reader: IT45 delegate, `generation_it45_20261111/verify_s10/VERDICTS.md`):

| Check | Result |
|---|---|
| Ledger receipts naming the paper | 0, 0, 0 |
| Staged receipts naming the paper | 0, 0, 0 |
| Deep-dive manifests naming the paper | none (the PMIDs occur only in `generation_it45_20261111`, and for 31411465 in the IT43 pointer tables and the view) |
| Source bytes the reader worked from | exist: `pmc_html.txt`/`pmc.html` (38116420), `tran.pdf`/`tran.txt` (31411465, HAL accepted manuscript), `nat.xml` (21964340), plus eight figure/table images of 38116420, in the scratchpad of session 4325d70d; digests in `reading_debt_s10.tsv` |
| Reader's quotations found verbatim in those bytes (`reading_debt_check.py`, after whitespace/case/markup folding; a quotation is a quoted span of 40 characters or more inside one line) | 7 of 13, 1 of 16, 0 of 3. The misses are abridged quotations ("..." elisions, bracketed edits, compound numbers) whose first 60-90 percent matches; they are not exact spans |
| Supplementary files | not reached in any of the three (the reader says so) |

**Disposition: the debt is kept.** What exists is the reader's report and the bytes; there is no contemporaneous receipt with a source fingerprint written when the reading happened, and the report's locators are not all exact spans. A receipt dated now would present a reconstruction as a reading. If the Orchestrator wants the paper counted at all, the supported route is `record_kind: legacy_reconstruction` (it never upgrades the depth), not a `complete_fulltext_read`. Nothing was written to the ledger.

**Preservation, which was the real risk.** The bytes lived only in a session scratchpad of the kind the disk plan (`DISK.md`) lists as removable. 160 ledger and staged receipts (45 distinct source fingerprints, 80 events each recorded in both ledger and staged files) name a scratchpad as the source, all 45 are currently held in session 9400b253's scratchpad. All 45, and the S10 bytes above, are now copied (digest-verified) to `files/fulltext/rescued_from_scratch_he46/` (14 MB, untracked store; `evidence_presence.py --search files/fulltext/rescued_from_scratch_he46` finds them by SHA-256). Inventory: `scratch_sources_preserved.tsv` (58 rows). The scratchpads themselves were not touched.

**Same origin, not independence.** In `verify_s10/VERDICTS.md` the ChEMBL curated record ([CH]) is a human transcription of the paper's tables; where a row says "[CH] agrees" (for example MMF 127,200 nM) the two routes share one origin and add no independence. The reader labels the tiers ([FT], [AB], [CH]) and no result in `s10_dose/result_it45.md` counts a [CH] agreement as a second confirmation; nothing needed correcting.

Remove: delete `reading_debt_check.py` and the two TSVs; the preserved files are copies and may be removed once the operator no longer wants the 45 sources kept outside the scratchpads.

## 5. COMPLETE records with a pending verification (H8)

**Is it history or open work?** History. Four closed Orchestrator records carry a "pending" clause: IT40 ("Publish, CI and site pending"), IT41 ("publication and site check pending in P12"; "CI pending"), IT45 ("CI pending at the time of writing") and IT18 ("Pages site not creatable by the workflow token: pending one account operation"). Read against the public API on 2026-11-11 (`ci_runs.py status`): the runs on the commits those records name concluded `success` (IT40: gate #625 and publication #24 on 31919734; IT41: gate #632 and publication #26 on e2dbe391, #631/#25 on 975535a9; IT45: gate #654 and publication #34 on bfd5304e, #655 on 142f6c5f); the publication workflow has run successfully since #24, so the IT18 site exists. No run is still open.

**What was wrong at the canonical point.** `mandate_continuity.py` already reads a record by step status: a step `BLOCKED` with a named blocker keeps the mandate incomplete, and `COMPLETE` beside such a step is `INCONSISTENT_COMPLETE`. What §12 of `cross_session_transport.md` did not say is how a technical wait is written, so the wait went into prose and the record closed over it. Added there (one paragraph): a pending CI run, publication or battery is its own `BLOCKED` step (blocker = run number or process identity, unblock = observed conclusion), closed `DONE` with run number, workflow, full SHA and conclusion, and only then `COMPLETE`; a "pending" clause in a record that later closes is replaced by the observed result. The wait itself uses `ci_runs.py wait <sha> --timeout N` or `process_wait.py`, no second monitor.

**New tool.** `framework/scripts/ci_runs.py` (`status`, `wait`; stdlib, no token, the repository read from the `development` remote; exit codes 0/1/3/124/2; `no run seen` is never success; 7 tests without network). Before it, each closure checked the run with an ad hoc call.

**Not done, on purpose.** The four records were not edited (they are the Orchestrator's, and the clause is dated history); no heuristic over prose ("a COMPLETE record that says pending") was added, because `locator_propagation.py` records that this kind of heuristic was measured and rejected. The mandate hook is not touched, and nothing was stopped to test it.

Remove: delete `ci_runs.py`, its test and its README row, and the paragraph in §12; nothing depends on them.

## 6. Evaluation without circular truth (H6, support for IT46's trial on a new case)

**The trap, found in the existing scorer.** `generation_it44_20261110/eval_it44.py` counts "drug-role" and "non-drug-role" molecules from `entity_roles_it44.tsv`, which is the engine's own output; those counts restate the engine's labels, so they cannot show that a label is right (IT45's `eval_it45.md` says the scorer is "not an independent truth"; this makes the consequence measurable).

**What was added, with existing parts only.** `role_reference_check.py` keeps five things apart: *input* (the entity rows), *rules* (`role_rules_it44.tsv`: gtopdb_type and catalogue_status only), *result* (`role`), *reference* (the catalogue's `modality`, `molecule_type`, `chemistry.inorganic`, which no rule reads) and *judgement* (a reviewer reading the disagreements, recorded apart; none here). A molecule missing from the catalogue is `NO_REFERENCE`, never an agreement. Same-inputs, two-refs reproduction is the existing pattern of `conditions_before_after.py --old-ref`; no eval platform, no new store (output: `role_reference_check.tsv`, 484 rows; observed 4.4 s and about 570 MB resident, almost all of it loading the 44,211-entry catalogue).

**Result on the 484 role rows** (`role_reference_check.tsv`): of 175 candidate or probe rows, 163 agree with the reference, **5 disagree, 6 are unverifiable** (modality unknown) and 1 has no reference; 8 rows the rules left `unqualified_entity` are small molecules in the catalogue (a coverage gap, not an error). 197 rows (activity-only molecules, not in the catalogue) have no reference at all: the check is silent about HE45's `unqualified_entity` default for them, so "197 default rows no longer candidate" is a claim the reference cannot confirm or refute.

| Disagreement | Reading of the reference | Judgement (mine, to be confirmed by IT46's reviewer) |
|---|---|---|
| rapastinel, apimostinel (S1, S13) role `candidate` | catalogue `protein_or_peptide` | the reference is right: no GtoPdb row, so the peptide rule R5 (peptide, probe unless approved) never fired and the clinical-stage rule R8 made them candidates. A rule on the catalogue modality would close it; the rules file is not mine |
| ML252 (S3) role `probe` | `chemistry.inorganic` flag set | the reference is wrong here (an organic small-molecule Kv7 inhibitor): a flagged field is not a truth either |
| AZD8108, indantadol, CX1739, MK-8777 `candidate` | modality unknown | unverified: cannot be settled from the catalogue |

**What this does and does not establish.** It shows that an independent field can separate right labels from doubtful ones on data already held (5 disagreements among 175 candidate or probe rows, one of which is the reference's own error, and 6 unverifiable), and that the reference is itself fallible and shares a source (ChEMBL) with `catalogue_status`. It is not an improvement test: the engine was not changed here. For IT46's new case the same frame applies as it stands: name the reference before running, keep the engine's labels out of the scorer, and report `NO_REFERENCE` counts beside agreements. A gain measured on the case used to design the change is not a result on a new case.

Remove: delete `role_reference_check.py` and `role_reference_check.tsv`.

## 7. DREAM, simplification, scouting (H9)

`dream_pass.py quiet --since 2026-11-11` reported 94 commits since the date, so the pass ran; the helper only selected inputs.

* **Corrected in one table, old in another.** Found and repaired: the SCI45 TASK-3 and Imin corrections had not reached `pdh_pdk_sci44_20261110/S7_coda.md` section 5 and `kchan_expression_sci44_20261111/README.md` (section 2); `ph_k2p_sci45` answer 4 carried a slope-1 bound as the bound (clarified). The INV-18 text, IT45-Q05 and the view were already current.
* **Qualified capacity not called.** (a) 19 hypotheses of five packages could not be reached by the loader (section 3); reachable now, not yet used by `conditional_proposals` (IT46 P5 maps the cells). (b) `glun2b_comparators_sci42_20261110` holds the only pH-bearing propositions (D08, D09, D12, D17: NP10679 at pH 6.9 and 7.6) but has no comparison table and is not a registered comparison package, so the reader's pH axis cannot reach `compound_view` row V07 (NP10679, "a pH-linked comparison, subordinate to a measured tissue pH"); what the reader says today on those propositions: D08 (pH 6.9) against D09 (series 7.6 or 6.9) is INSUFFICIENT, D17 inherits D09's 23 C and not the 35 C of an untested transfer. A comparison table for that package is a producer artefact; not made here. (c) the reader has one caller.
* **Revival triggers.** The dismissal ledger names no trigger about pH, temperature, K2P channels or comparison conditions; none fired. Stated, not assumed.
* **Duplication that drifts.** None found beyond the two dated documents of section 2; the copies of receipts in ledger and staged files are by design (the ledger is the record, the staged file its proposal). No duplication was removed: CHANGE = NONE for this item.
* **Retrieval test on a new question** ("what does the repository hold on the pH dependence of the GluN2B tool NP10679, and who reads it?"): `dream_pass.py pairs GluN2B "pH 6.9"` returned, in one call, `comparison_S1.md` line 20 (GtoPdb pH 6.9, pIC50 7.64; the trial abstract), `compound_view.tsv` row V07 (the consumer, with its open premise), `provenance_it42.md`, and the `glun2b_comparators_sci42_20261110` README; from there `decisive.tsv` D08/D09/D17 are the originals and `assay_conditions.py compare` gives the state. The path reaches the originals and one consumer; it does not reach an investigation card because V07 is a probe row.
* **External scouting:** none. No need emerged that the held tools do not cover (the unmet needs of this window were inside the repository: two documents, one loader role, one reference field). System One was not reopened and no runtime was installed.

## 8. Cost: the dominant factor of the release battery (H7)

**Measured, not assumed.** The last complete battery before this window (HE45, `/tmp/he45_keep/he45_battery_cbc62fcb.log`): 239 suites, 3,699 s of suite time; `test_repurposing_view.py` 1,395 s (38 percent), `test_repository_surface_determinism.py` 556 s, `test_self_test_coverage.py` 341 s; the three are 62 percent. A per-class timing of the view suite (nice 19, shared load, 1,689 s in total): `ShareableAudit` 637 s (26 tests, about one 28 s `audit_html` call each), `RealViewports` 324 s, `BriefBrowser` 115 s, `It7P7Browser` 103 s. A profile of one `audit_html` call: `scan_strings` 13 s and `pair_scan` 7 s; the shareable build passes 163,129 strings of which 14,811 are distinct (page: 16,162 and 2,628).

**Improvement tried: memoise the per-string scan** (the same string is scanned about eleven times). The report was identical on five pages (the real shareable build, the full build, the committed English page, a page with an injected name, one with injected identifiers: violations, co-attested, suppressed and wording equal). CPU time over three repeats, old against new: 6.8-7.9 s against 6.4-7.4 s, about 6 percent, inside the noise of a shared machine (the wall-clock figures of the first comparison, 15.9 against 9.9 s, were load, not the change). **Reverted**: the code is the publication privacy gate, a 6 percent gain does not justify touching it, and the dominant cost is elsewhere (string building in `grams`, regex over 5 MB pages). CHANGE = NONE for the audit; the measure, the identity check and the reason are kept here for the next person who wants to try an algorithmic change (an indexed lookup rather than a memo).

**What did reduce cost in the window.** A new test without `verbosity=2` failed the first battery four minutes in; running `test_release_runner_verdict.py`, `test_release_surface.py` and `test_documented_commands.py` before freezing a SHA (written in memory and in section 13) avoids a 60-minute run dying late. The disk cost of the battery is now removed by its owner (section 9): about 0.9 GB of unique blocks per clone, 26 GB across 28 forgotten ones. No tokens were converted into money or plan shares.

## 9. Verification clones removed where they are created (the operator's addition to HE46)

Who creates the clones: nobody in code. `run_release_regressions.py` only runs tests in the current directory; the CI workflows use the hosted runner; battery, publication and receipt-trial clones were made by hand by whichever session needed one (`framework/scripts/README.md` section 13 carried the recipe). `owned_scratch.py` already gave a box that carries `PID:START` and refuses a stranger; what was missing was the lifecycle around it. Added: **`framework/scripts/verify_run.py`** (one component for the three sessions; the one canonical instruction is the section-13 row of `framework/scripts/README.md`, the router row is in section 7).

* `run --sha S --label L --mandate T [--task-record R] -- COMMAND`: owned box (`legend-verify-*`, run id, supervisor `PID:START`), `git clone --no-hardlinks`, checkout S, `files/` hard-linked only, the command's log written outside the clone, and at the end (pass, fail or interrupt) the evidence is kept and the exact directory removed if every check holds. `reap` concludes this session's earlier finished or interrupted runs (`--actor` for a role); `status`; `unrecognised` lists clone-like directories with no manifest of ours and removes nothing.
* Evidence kept (default `/tmp/legend-verify-keep/<run_id>/`): `manifest.json`, `run.log`, `clone_state.txt`, `--keep` artefacts, `unsaved_changes.tar.gz` when the clone held changes that exist nowhere else; the mandate record gets a `VERIFICATION_EVIDENCE` entry (run id, SHA, state, exit code, evidence directory, log SHA-256, clone state).
* Removal checks: ownership by manifest, `.run_id` and inode; run finished; no process (any, but the remover) with its cwd, executable, open file or memory map under the box, children included; the SHA and every ref commit of the clone exist in the source repository; changes not in the source are archived and re-read, above 50 MB, unique data under `files/` (link count 1) or an ignored non-cache file with no other link keep the directory; log and exit code present. Symlinks are unlinked, never followed; hard-linked corpus files only lose their name in the clone. Nothing is ever killed. A problem is a precise `KEPT` reason in the manifest and on screen; it does not change the verdict and blocks nothing.
* Protected, never touched: `files/`, datasets and caches, sessions and scratchpads (`claude-*`), Python environments, worktrees, other sessions' or unrecognised runs (an old directory with no manifest is listed, never removed by age or name).
* Tests (`test_verify_run.py`, 17, fixtures only): pass and fail keep the evidence and remove the clone; a process inside the directory keeps it and a later `reap` removes it; a stranger, a look-alike name, a symlinked box, a manifest naming something else, a missing box and an incomplete manifest delete nothing; unsaved files are archived (and kept above the limit); unique corpus data and a commit only the clone holds keep the directory; a symlink target and a hard-linked original survive; a second call changes nothing; another session's run is not reaped; SIGTERM concludes and cleans; a killed supervisor leaves a run that the next call concludes only after its command has ended.
* **First real run (SHA c0789939, run `20261111-230442-37a1b947`): FAIL, and the tool did its job.** Exit 1 from one suite, `test_ci_runs.py` (its slug test assumed a `development` GitHub remote, which a clone of a local path does not have). The clone was removed by the tool (0.91 GB freed), `run.log` (8,019 lines), `manifest.json` and `clone_state.txt` stayed readable, and the mandate record gained its `VERIFICATION_EVIDENCE` entry (log SHA-256 `4598a97f...`). The run also exposed a second defect of the tool itself: a worktree has no `files/`, so the clone had no corpus and every corpus suite skipped (the verdict would have read as a pass with many skips); `corpus_of` now links the corpus of the checkout the source is a worktree of, and the manifest records `files_linked_from`. Both fixed with tests (`test_ci_runs`, `test_verify_run`, 18 now); the battery is run again on the fixed SHA.
* Not done: the clones already in `/tmp` stay as the operator left them; the 28 removals of 2026-11-11 were manual. Old temporaries without provenance appear in `unrecognised`.

## 10. Mandate association that the monitor can see (the operator's urgent addition)

**Read on 2026-11-11 ~22:55Z.** `mandate_watch check --deliver none` for `ORCH-ROADMAP-IT46-20261111` and `ORCH-SCI46-20261111`: from the root checkout `NO_RECORD` (the records live in unmerged worktrees: `--root` must name the worktree); from the worktrees the record was read (`CONTINUE`) and `state UNKNOWN`, `session null`. The runtime inventory (`claude agents --json`) was readable (7 sessions). Transcripts: no transcript held a valid marker for either task. **Break points:** IT46's session (4325d70d, `legend-development-4e`) wrote `MANDATE_BOUND: ORCH-ROADMAP-IT46-20261111. Identità: orchestrator. ...` at 21:48:36Z, a sentence, which the canonical reader refuses on purpose (a quoted or negated mention must not bind) and where the `.` would have joined the id; SCI46's session (9400b253, `legend-development-40`) received its assignment at 21:48:57Z and never wrote a marker. A statement in the task record is not an association; only a marker line in the owner's own transcript is. Identity came from the transcript's session id and the live inventory, not from any process's directory (the SCI46 session's cwd is the root checkout, the worktree is the record's).

**Repair.** The two owners were asked, through the internal transport, to write the plain line themselves; this session wrote no marker for another's mandate. Both did. Re-read from their worktrees: IT46 `RUNNING / NONE`, session 4325d70d, record `CONTINUE`; SCI46 `RUNNING / NONE`, session 9400b253, record `CONTINUE` (both "activity 2 min ago"; nothing was delivered, nothing resumed, no duplicate started).

**General defect, reproduced and fixed.** An embedded marker left the mandate `UNKNOWN` with no hint why. `mandate_watch.find_near_marker` now reports the session and the line that came closest (never binding it), and the `why` says what to write. Test: a marker inside a sentence is refused and named, the plain line then binds, a fenced or unrelated mention is not reported (`test_mandate_watch.py`, 2 new). Canonical point: `cross_session_transport.md` section 12, "Accepting a mandate: write the marker, then prove it was recognised" (the three things to read in the check: own session id, the intended record via `--root`, `RUNNING` while working or waiting on a battery).

| Guarantee | State |
|---|---|
| association verified | yes for both, by the owner's own marker and the live inventory |
| classification verified | `RUNNING` by recent activity for both today; a long idle battery wait stays `RUNNING` only through a registered `mandate_watch job` or recent background-task output (existing tests cover both, one fixture was added for the near-miss) |
| resume request supported | `RESUME` is requested only for an absent or idle silent session with work left, under its own id, once per record change, and never for a live session (existing tests) |
| resume proven | not proven here and not claimed: it needs a live runtime, a trusted workspace and the bound id; no live session was stopped to test it |
