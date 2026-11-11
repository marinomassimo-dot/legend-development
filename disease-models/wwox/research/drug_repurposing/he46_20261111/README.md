# HE46 — conditions, propagation, generative capacity (Harness Engineering, 2026-11-11)

Non-canonical. Harness work: generic components and checks. Scientific meaning stays with SCI46 and IT46.

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

**What was added, with existing parts only.** `role_reference_check.py` keeps five things apart: *input* (the entity rows), *rules* (`role_rules_it44.tsv`: gtopdb_type and catalogue_status only), *result* (`role`), *reference* (the catalogue's `modality`, `molecule_type`, `chemistry.inorganic`, which no rule reads) and *judgement* (a reviewer reading the disagreements, recorded apart; none here). A molecule missing from the catalogue is `NO_REFERENCE`, never an agreement. Same-inputs, two-refs reproduction is the existing pattern of `conditions_before_after.py --old-ref`; no eval platform, no new store (output: `role_reference_check.tsv`, 484 rows, 0.5 s).

**Result on the 484 role rows** (`role_reference_check.tsv`): candidate/probe roles agree with the reference for 163 rows, **disagree for 5, are unverifiable for 6** (modality unknown), have no reference for 1; 8 rows the rules left `unqualified_entity` are small molecules in the catalogue (a coverage gap, not an error). 197 rows (activity-only molecules, not in the catalogue) have no reference at all: the check is silent about HE45's `unqualified_entity` default for them, so "197 default rows no longer candidate" is a claim the reference cannot confirm or refute.

| Disagreement | Reading of the reference | Judgement (mine, to be confirmed by IT46's reviewer) |
|---|---|---|
| rapastinel, apimostinel (S1, S13) role `candidate` | catalogue `protein_or_peptide` | the reference is right: no GtoPdb row, so the peptide rule R5 (peptide, probe unless approved) never fired and the clinical-stage rule R8 made them candidates. A rule on the catalogue modality would close it; the rules file is not mine |
| ML252 (S3) role `probe` | `chemistry.inorganic` flag set | the reference is wrong here (an organic small-molecule Kv7 inhibitor): a flagged field is not a truth either |
| AZD8108, indantadol, CX1739, MK-8777 `candidate` | modality unknown | unverified: cannot be settled from the catalogue |

**What this does and does not establish.** It shows that an independent field can separate right labels from doubtful ones on data already held (5 doubtful of 169, one of which is the reference's own error), and that the reference is itself fallible and shares a source (ChEMBL) with `catalogue_status`. It is not an improvement test: the engine was not changed here. For IT46's new case the same frame applies as it stands: name the reference before running, keep the engine's labels out of the scorer, and report `NO_REFERENCE` counts beside agreements. A gain measured on the case used to design the change is not a result on a new case.

Remove: delete `role_reference_check.py` and `role_reference_check.tsv`.
