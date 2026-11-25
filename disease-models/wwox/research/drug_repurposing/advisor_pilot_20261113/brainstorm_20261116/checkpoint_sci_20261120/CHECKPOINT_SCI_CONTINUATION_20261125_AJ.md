# Checkpoint AJ: SCI continuation of 2026-11-25 after ADV-278 and the PREREG of the six newly held papers (resume from AI + AI addendum + this file; hypothesis level; not medical advice; this file is not edited once hashed)

Why: ADV asked for it after the six-paper PREREG (the tick reads context at 259k, above the 220k trigger). Written by session `0d0c6dc3-4d74-4dbb-8989-88e2e195f3c6` (claude-sonnet-5-5, effort high). Standing rules: AH sections 0 and 5, AI section 0 (release/bind procedure, peers, no e-mail to any service, challenge pages are results, no spend, Codex paused, frozen RP-045, sealed ADV-174/175, no renames, reply to the operator in Italian, files in English, state model and effort in every dispatch). Commit trailers: the attribution lines the session's own reminder gives (the successor uses its own session URL); never write an e-mail address into a public file (the publication gate blocks it: push 10 was refused on exactly this line).

## 1. State

* **ADV-278 closed** (on main, consumed by ADV): `adv278_wwox_protein_spec_sci_20261125/` (spec with a 200-word head, `adv278_n.py`, blind check). No successor needed for it.
* **35222658 correction closed** (RESULT_ADV276 section 1, AI addendum, checklist). Checklist now has six recurring checks (footer rows; variance from all eligible rows).
* **Six-paper reading (ADV-276 item after ADV-278), folder `adv276c_six_newly_held_sci_20261125/`:** PREREG committed 15:05Z (sha256 `8f77fb60bfa4005b41eb6fcc130f9c7b68a2a65d735228739e710469441049fa`; strict 2 of 6, range 0 to 4; loose 3, range 1 to 5). **Reading is done in draft**: `READER_DRAFT_SIX_SCI_20261125.md` (table per paper, draft score strict 1 of 6, loose 4 of 6, class of correction: an overexpression result carried as an endogenous one). Nine blind statements S1 to S9 are in `BLIND_STATEMENTS_SIX_SCI_20261125.md`; one verifier (`legend-delegate`, sonnet, effort high) was dispatched on them: its report was written to the old job's scratch (`.../jobs/0d0c6dc3/tmp/six/blind/out/REPORT.md`); if the file is gone, re-dispatch the same statements with the source texts (convert each `files/fulltext/PMID<p>_ADV272_PMC_r2.xml` with an XML to text script, supplement and figures under `files/`).

## 2. Open work, in order (the successor takes it)

1. Finish the six papers: read the verifier's verdicts against the draft (it overturned or corrected my drafts in every previous batch; a single-reader table is a draft), write `RESULT_ADV276_SIX_NEWLY_HELD_SCI_20261125.md` (per-paper table, scoring against the PREREG, class of correction, blind reading, wording for IT, section on receipts), make six receipts (adapt `adv276b_lead_receipts_sci_20261125/make_receipts_adv276s2b.py`: `prior_receipt` linked, event IDs `FTR-20261125-<pmid>-NN`; the XML paths `files/fulltext/PMID<p>_ADV272_PMC_r2.xml`), record them (`fulltext_receipts.py record` then `verify`), **commit the receipts first**, then regenerate `coverage_report.py`, `reading_state.py`, `ranking_it8.py run`; one wording message to IT (CLAIM 027 evidence boundary, RP-018 line, DL-MECH-120, -119, -157; RP-038 and 34210081 as precision notes).
2. Order of the wording for IT (ADV): RP consumers first (27845895, 39178853, 27641496), then the three reviews.
3. Close ADV-276 with ADV: PREREG scoring across increments, reconcile mandate step `OBJ_ACCEPTED[120]` when ADV closes it.
4. Session end: `legend-session-self-eval`, `legend-dream`, `legend-capability-scout`, `legend-session-takeaways`; final report to the operator in Italian.
5. Standing: 16061658 and 25738261 are not in PMC (operator list / access); ADV-223 operator PDF list unchanged.

## 3. Landing facts

`safe_push.py development main --expect-sha <sha> --serialize` in `nohup bash -c '...' < /dev/null &` plus a Monitor on the log; the landing lock queue can be 4 deep (up to ~25 min); do not commit or add untracked files in the worktree while it waits (write in the job scratch, copy after). After a merge of main, commit the merge before regenerating derived files.

## 4. Lessons added since AI addendum

1. Variance comes from all eligible rows, not the called ones (ADV-278: 0.22 against 0.26).
2. A review's shift between "endogenous" and "overexpressed" is easy to carry the wrong way: the title of Hsu 2017 says "when overexpressed", the claim sentence did not.
3. The ranking's "unread class" column names where to look first: for the six it pointed at figures (33363507: schematics, nothing found), supplement (33854788: the paper's own WWOX datum) and discussion (27845895).
