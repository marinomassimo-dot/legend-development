# Batch self-evaluation — interventions batch 2026-10-19, group H5, scientist-d

> Written after the analytical work and before capability growth and takeaways. Part 1 was run first; the judgement below was written knowing its verdict. Not medical advice. Every paper in this group is a substitute for absent WWOX evidence.

## Scope and executable verdict

- **Batch/session:** `INTERV-H5-D-20261019`, branch `task/INTERV-H5-D-20261019`, 16 lot papers read (3 tier 1, 6 tier 2, 7 tier 3), one WWOX-direct held row re-read, one held row extracted without a receipt.
- **Receipt IDs (staged, not appended):** `FTR-20261019-<PMID>-01` for the 16 lot PMIDs and `FTR-20261019-41677633-03` (prior `-02`), listed in `interventions_wave_20261019_scientist-d.md` section 1. One is `complete_fulltext_read` (36044864); the Su 2026 re-read is `complete_fulltext_read`; the other fifteen are `partial_fulltext_read`.
- **`session_self_eval.py --workspace . --disease wwox`:** `VERDICT: PASS` (every complete read has landed and every declared output resolves). The `[DECLARED GAP]` lines belong to five other PMIDs; none concerns this wave.
- **Per-study manifests:** `deepdive_manifest.py --verify-artifacts --require-current-schema` returned `PASS`, zero gaps, for all 17. The eight manifests carrying `contradicts_locator` declarations passed once the prior-manifest lookup was fixed (micro-upgrade below); before the fix they were validated against a scratch workspace holding copies.
- **Receipt verification:** `fulltext_receipts.py verify` OK (475 chained receipts, tail anchored). All 34 staged receipts under `receipt_staging/scientist-d/` (17 this wave, 17 of the previous wave) validated in isolation with `validate_new_receipt` and `validate_receipt`: no errors. None appended.
- **Undeclared revisions:** `locator_contradiction_audit.py --working-tree --fail-on-undeclared`: 25 declared revisions, 0 undeclared.
- **Structural LINT:** `VERDICT: WARN`, no `BLOCK`; the warnings are pre-existing `UNLINKED_SUPPORT` lines on claims this wave did not touch.
- **Concurrent conditions:** `legend_commit.sh` refused each commit as `STALE` (pathograph drift); committed with `LEGEND_STALE_SURFACES_BECAUSE` naming the parallel wave; regeneration left to the Orchestrator. Recorded as a default taken.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | Body, tables and the figure images read for all 16 (the wave-1 lesson applied: no paper was read at caption level only). Complete read only for Yuskaitis; elsewhere `partial` because references were counted, supplements left unopened (Trico zip, Burst files, Hahn S2b-S6) or figures seen reduced (Salvati 3-5). | partial | Named per receipt and in note section 8. |
| Main message and original contribution | Stated per paper; for the group the message is a negative: no WWOX datum on fasting, dextrose, fluid, refeeding or thiamine exists. | strong | None. |
| Hidden gold beyond keywords/abstract | Nine source defects found by panel and table reading: Salvati p value (main text 0.0078, Table S1 0.0044 for the rat row); Hahn participant 3 seizure-free on IF alone while the Discussion says only on IF-MCT; Funayama Table 4 versus 7; Tesser 2.8% versus 3.8%; Trico plasma BHB level and correlation scopes; Burst 1101 versus 1053; Morris slope arithmetic; Garg infusion unit; Sun n versus t statistics. | strong | None. |
| Source parity: context, type and recency | Reviews, a hypothesis paper, case reports, pilots and cohorts labelled; the review-type papers say which parts are the authors' argument ("one might argue", "theoretically"). | strong | None. |
| Team type, field density, observation vs interpretation | `group_assessment` and PubMed counts (2026-10-19) in every manifest; the counts are search hits, not censuses, and say so. | partial | None. |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | Leads L1-L4 labelled `IPOTESI` with falsifiers; the negatives in the NEGATIVES candidate carry premises and revival triggers. | strong | None. |
| Existing claims touched; conflicts/revival triggers | No claim status or baseline claim is touched; `CLAIM 042` and `DL-MECH-020` were admitted for comparison and left unchanged. The locator audit was run anyway (101 triples). | strong | None. |
| Multi-hop and corpus cross-query | `registry_records.py` run per PMID and by theme; reference lists printed and read for two papers (Yuskaitis 80, Phillips-Farfan 39) and for the Su 2026 re-read (68); counted for the other fourteen. The Su 2026 list holds many WWOX-direct references that were not queued here. | partial | Fourteen reference lists unread. |

## Persistence diagnosis

- **Durable IDs:** 17 manifests (16 new, one appended), 17 staged receipts, the analysis note, two commit candidates (`CC-20261019-SCIENTISTD-H5-REGISTRY-01`, `-NEGATIVES-01`), this file, the scout entry, the task JSON with `DEFAULTS_TAKEN` and `STOP_LOG`.
- **Reading queue/debt:** note section 8; Carvalho 2022 stays `partial` because an extract is not a read.
- **Can a future run distinguish full text from abstract only?** Yes: `source_kind: fulltext_local`, SHA-256, closed-vocabulary coverage, manifests whose body locators are verified against the XML and whose figure locators name the image files and their digests.

## Process and capability diagnosis

- **Skills/gates/patterns used:** `paper_packet.py packet/check`, `deepdive_manifest.py` strict, `dependency_integrity.py screen --manifest-block`, `registry_records.py`, `locator_contradiction_audit.py`, two blind auditors under the `legend-locator-audit` method (spawned without session history), `pmc-oa-opendata` bucket for figures and supplements.
- **Plausible skills deliberately declined:** `legend-deepdive` (run inline), `legend-discovery` and `legend-hypothesis-forge` (no comparator matures a lever; forging one would manufacture a lead), `legend-safety-triage` (no compound proposed for the reference genotype), `legend-paperqa` (external spend), `find-fulltext` (every lot paper had a lawful JATS body on the first request).
- **Failures, retries, concurrency events:** see the census.
- **Disease-agnostic micro-upgrade shipped:** `deepdive_manifest.py` now resolves the prior manifest named by a `contradicts_locator` beside the manifest being validated (`queue_root`) before falling back to the artifact root, so a task branch can declare a revision of its own manifests while `--artifact-workspace` points at the shared evidence checkout.
- **Regression/evidence:** `test_the_prior_manifest_may_live_in_the_branch_workspace_not_the_artifact_root` in `framework/scripts/test_deepdive_manifest.py` (205 tests OK, 6 skipped); manual: 25 declared revisions were refused with "not a file under the workspace" before the change and PASS after.
- **Residual risk and next decisive action:** the audit shows 23% of load-bearing propositions outran or undershot their quote while every structural gate was green; a reading-time check that prints each proposition beside its quote and the proposition words absent from it is the decisive next build. Also read the Carvalho figures 4-10 and supplement to turn the extract into a receipt.

## Attribution census

Incidents, one per defect or near-error, repeated instances of one class counted once:

| # | Incident | Caught by | Reached the record? |
|---|---|---|---|
| A | Manifest schema rejections: `research_type` outside the closed list, snippet under 30 characters, a quote with a hyphen glyph the surface does not carry (6 instances over 5 papers) | machine | no |
| B | My text renderer skipped floats placed outside the body sections: Tesser Table 1 (22 study rows) and Yuskaitis figure legends and key resources table were unread in the first pass while I was about to mark tables read | self (cross-count of `table-wrap` and `fig` elements in the XML against what the rendering printed) | would have |
| C | 23 of 101 load-bearing propositions overshot or undershot the quote beside them (9 OVERSHOOT, 14 UNDERSHOOT), all committed before the audit | blind auditor (two, spawned without history) | yes, until repaired |
| D | My derivation that Sun 2025's t statistics fit about 10 animals per group was wrong (they fit about 5-9) | blind auditor | yes, until repaired |
| E | A Burst manifest entry called the flow diagram "Figure 2"; the text calls it Figure 1 and the image file is g002 | blind auditor | yes, until repaired |
| F | `contradicts_locator` declarations were refused because the prior manifest existed only on the task branch, not under the artifact root | machine (then fixed in the validator, with a regression) | no |
| G | Inserting a locator mid-list shifted every later index and `locator_contradiction_audit.py` read it as 17 undeclared revisions | machine (the entry was re-added at the end) | no |
| H | The selection file links Dienel 2023 to the GSK3B arm and Funayama 2026 to thiamine risk; the texts mention neither (string counts 0) | self (reading and counting in the rendered text) | would have |
| I | Figure file numbering differs from figure labels in two papers (Hahn, Abbas): the first image opened as "Figure 1" was a different panel set | self (checked the XML figure-to-file map before attesting) | would have |

```
ATTRIBUTION_CENSUS
incidents: 9
machine: 3   blind_auditor: 3   peer: 0   self: 3
severity_high: 2   of which self: 1
undetected_known: 0
```

**Reading of the census.** Incident C is the one that matters: it reached committed manifests, every structural gate was green over it, and only blind auditors saw it; the self-check I ran before committing (re-reading each proposition against its snippet, the control wave 1 relied on) did not find these 23. That is a weaker result than wave 1's, and it argues for the blind step being routine and for a mechanical proposition-versus-quote aid. `undetected_known: 0` is an honest zero only in the sense that I know of none; two auditors read 101 of 252 locators, and the unaudited remainder carries the same expected defect rate until someone checks it.
