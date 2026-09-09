# Batch self-evaluation — `scientist-c`, `AQEILAN-FT-C-001` wave 1, 2026-09-09

> Written **after** Part 1 returned its verdict and **before** capability scouting and takeaways.

## Scope and executable verdict

- **Batch/session:** `AQEILAN-FT-C-001` wave 1 of a 7-PMID lot. Reading mode `PRIMARY_EVIDENCE_READ`.
  Shared root checkout `/root/legend-development`, branch `main`, three scientist actors concurrent.
- **Studies and complete-read receipt IDs:**
  - `PMID 20530675` (Kurek 2010, *Cancer Res*) → `FTR-20260909-20530675-01`,
    `complete_fulltext_read`, `reread_reason: inadequate_prior_coverage`,
    `prior_receipt: FTR-20260814-20530675-01`.
  - `PMID 21731849` (Del Mare 2011, *Am J Cancer Res*, **review**) → `FTR-20260909-21731849-01`,
    `complete_fulltext_read`, `reread_reason: first_read`.
- **`session_self_eval.py`:** `PASS` — *every complete read has landed and every declared output
  resolves*. receipts 135 · complete_fulltext_events 67 · active_complete_reads 56 ·
  unread_premises **4/4** (ratchet held; not raised by this batch).
- **Per-study manifests:** both `PASS`, **0 gaps**, `schema_version 2`, strict
  (`--verify-artifacts --require-current-schema`) run from the shared checkout.
  31 locators (20530675) and 18 locators (21731849).
- **Receipt verification:** `OK: 135 chained receipt(s), tail anchored`.
- **Structural LINT:** `PASS` after every commit (one standing `[INFO]` on CLAIM 010, pre-existing).
- **Growth anchors:** `PASS` — claims 39 · papers 70 · corpus 356 · literature 390 · registry_only 15.
- **Local verdict:** both papers closed to `complete_fulltext_read` with no waivers.
- **Workspace/global verdict and concurrent conditions:** no blocking condition. Two concurrency
  events, both handled by the tooling and neither by me: the receipt writer rejected my first append
  (`analysis_at` later than the writer-stamped `event_at`), and a peer's path-scoped commit
  (`f2d0446`, `scientist-b`) swept my already-appended receipt into `HEAD` before my own commit —
  correct behaviour for a shared ledger path, recorded so it is not mistaken for a lost write.
  Ledger moved 130 → 135 during the session under peer appends; no `rechain` was needed because this
  deployment shares one ledger rather than forking it.

---

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | **11 of 11** figure surfaces on 20530675 read **as pixels** (5 main from the PMC blob CDN at native 1050px; 6 supplementary rendered at 150 dpi from the fingerprinted supplement PDF), Table 1A/1B and Supplemental Tables 1–10 read, supplement retrieved (24 pp, 6.0 MB) via `pmc_pow_fetch.py`. **2 of 2** on 21731849. Figure 3C additionally re-read at 300% to resolve printed P values. No `captions_only` anywhere. | `strong` | none |
| Main message and original contribution | 20530675: prevalence (58%, 48/83, Table 1A) + within-patient longitudinal direction (Fig 1B/1C, pixels) are the real contribution; the RUNX2 title is not. 21731849: a same-lab review, contribution is synthesis only. | `strong` | none |
| Hidden gold beyond keywords/abstract | Four findings live **only** in the supplement (S.Table 8 reversal; Fig S1 legend 86% vs body 100%; Fig S4 clone/control dependence; Fig S6 antibody gap). **A keyword search would return none of them** — three are in a supplement PDF and one is an arithmetic property of a printed interval. Also `DL-MECH-106` (SAOS-2 mRNA-preserved/protein-lost) sits in a bar label and a blot lane, in no sentence containing a mechanism word. | `strong` | none |
| Source parity: context, type and recency | Read on **both** axes. Type: 20530675 primary, 21731849 **review** — recorded as a secondary source that *cannot* be primary evidence, with `methods/results/tables/limitations/supplementary` = `not_present` because a review has none. Context: oncology/bone, i.e. the case `gold_is_in_the_details` rule 3 exists for; read in full precisely because Tier C and clinical relevance LOW are **not** licences not to read. | `strong` | none |
| Team type, field density, observation vs interpretation | `experimental_lab`, primary for the **gene**, **not** primary for the **disease** — stated separately, as required. Weighted split explicitly: first-hand weight to their own reagents/models/IHC; reduced weight to every step carrying a bone observation toward disease interpretation. Field density measured 2026-09-09: WWOX **707**, WWOX∧osteosarcoma **28**, WWOX∧RUNX2 **12**. | `partial` | 🔴 **The 137/64 publication counts were carried forward from the repository's 2026-08-11 measurement, not re-derived today.** Declared in both manifests, but it is a stale number in a field-density-sensitive slot. |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | Every carried statement typed. Transfer verdict **`ESPANSIONE` / T3** for both, stated in dossiers and receipts. Two `PREMISE: DEFAULT_FROM_TEXTBOOK` tags with `REVIVAL_TRIGGER`s: *low protein implies low transcription* (`DL-MECH-106`) and *a negative result is explained by method insensitivity* (21731849 §3.2). | `strong` | none |
| Existing claims touched; conflicts/revival triggers | **`CLAIM 036`** (`in observation`) touched twice and said so where the claim lives, via `CC-20260909-21731849-01` §3: its recorded osteosarcoma conflict now has a **named resolution in the literature that rests on nothing**, and its design constraint is **corroborated by the authors themselves**. **No consolidated baseline claim touched** — determined by enumerating all 18 and reading their titles, not assumed. | `strong` | none |
| Multi-hop and corpus cross-query | 36 and 63 references **enumerated as integers** with PMIDs. **Five of 21731849's load-bearing hops were already read in full**, which is what turned that reading into a runnable fidelity test rather than a summary. Corpus cross-query found the wrong-DOI propagation across two ledgers. | `partial` | 🔴 **Initially I recorded the two 20530675 multi-hop debts in the manifest and dossier only — prose, not the queue.** Closed during this evaluation as `FT-075`/`FT-076`. |

---

## Persistence diagnosis

- **Durable ledger/registry IDs and wikilinks:** `DL-MECH-106` and `DL-METH-107` appended to
  `discovery_ledger_current.md`; `FT-075`, `FT-076`, `FT-077`, `FT-078` appended to
  `full_text_queue_current.md`; commit candidates `CC-20260909-20530675-01` and
  `CC-20260909-21731849-01`; both wikilinked to `[[claim_registry_current#CLAIM 036]]`.
  Receipts through the validated writer only. **Nothing sits in `staging/`.**
- **Reading queue/debt:** `FT-075` (PMID 18931939 — reagent source *and* premise source in one
  citation) and `FT-076` (PMID 16223882 — the Ad-WWOX construct, carrying a **standing expression of
  concern**, already assigned to this actor in a later wave). Both written into the queue, not
  carried in prose.
- **Dossier and commit candidate:** `fulltext_dossiers/PMID20530675.md` (317 lines) and
  `PMID21731849.md` (226 lines), each with artifact digest table, figure audit, negatives, and
  transfer verdict. One commit candidate each.
- **Receipt source fingerprint, coverage and supplement state:** 20530675 bound to the XML
  (`bb0a866f…`), full coverage map, `supplementary: read`. 21731849 bound to the **PDF**
  (`c0b1bddf…`) with the extracted TXT declared as `article_text`, exactly as the protocol requires
  for a PDF; `supplementary: not_present`, corroborated independently by Europe PMC `hasSuppl=N`.
- **Can a future run distinguish full text from abstract only? How:** yes, mechanically:
  `fulltext_receipts.py status --pmid <PMID>` returns depth, coverage map, source path and
  SHA-256, and both manifests declare `source_fulltext_indexed` with the Europe PMC query and date
  behind it. Neither depth rests on prose.

---

## Process and capability diagnosis

- **Skills/gates/patterns used:** `legend-deepdive` route; M0 duplicate-work gate re-run **per paper**
  rather than inherited from the dispatch; `pmc_pow_fetch.py`; strict manifest validator;
  `_refuse_suspect_surface` run explicitly on both PDF-derived surfaces;
  `legend-session-self-eval`. Imported-premise pattern (2026-08-06) applied to a review's disposal
  of two negatives. `panel_qualifies_text` / `text_contradicted_by_panel` used with pointer **and**
  needle on both papers.
- **Plausible skills deliberately declined, with reasons:** `find-fulltext` (cascade never reached —
  `efetch` and `pdf=render` sufficed); `legend-hypothesis-forge` (no molecule, dose or endpoint; T3);
  `legend-safety-triage` (no molecule promoted); `legend-proband-priority-matrix` (single assigned
  PMID, order fixed by dispatch); `legend-discovery` on paper 2 (a review contributes no new
  measurement to mine); **`legend-locator-audit` (R4)** — not triggered, and the determination was
  made **mechanically and re-made for the second paper**: all 18 `consolidated baseline` claims
  enumerated and read, every one WWOX-DEE neurobiology, none touching osteosarcoma/RUNX2/bone;
  `PMID 20530675` is `CORPUS P268` with `Claim links: none`.
- **Failures, retries, extraction mismatches or concurrency events:**
  1. Europe PMC `fullTextXML` **404** on both papers (NIHPA / non-OA) — cascade continued.
  2. PMC `/bin/` figure route **404**; PMC article page returned a **reCAPTCHA** interstitial.
  3. Receipt append rejected: `analysis_at` later than writer-stamped `event_at`.
  4. Receipt append rejected: **`conflicting identifiers for the same study`**.
  5. Commit wrapper failure from **my own** unescaped inner double quotes in a message.
  6. `research_type` rejected against its enum; `source_fulltext_indexed_evidence` field name wrong.
  7. **Character-fidelity mismatch:** a candidate snippet used `µ` (U+00B5) where the artifact holds
     `μ` (U+03BC). Caught by pre-verifying every snippet against the validator's own extractor
     *before* writing the manifest.
  8. 🔴 **The one that mattered:** `pdftotext -layout` on a **two-column** article interleaved the
     columns and injected the page number `588` into the middle of the sentence carrying the
     headline claim.
- **What caught each failure before an overclaim:**
  - 1–2: the HTTP status itself; recorded as **surface facts** (`FT-077`), not silently routed around.
  - 3, 4, 6: **the tooling, not me.** The ledger writer and the manifest validator refused the
    appends. #4 is the important one: it refused my **correct** DOI because the prior receipt had
    persisted a **wrong** one, and I refused in turn to write the falsehood to satisfy the check.
  - 5: the shell, immediately; `git status` confirmed nothing staged before retrying.
  - 7: my own pre-verification pass against `_xml_surfaces` / `_normalise_text`.
  - 8: **comparison against the rendered page** — a human act that does not scale, which is exactly
    why it became this session's micro-upgrade.
  - **Attribution to others, per the protocol's instruction to name who caught what:**
    `scientist-a` shipped `framework/scripts/evidence_presence.py` in this same session to measure
    whether a checkout holds the bytes its manifests fingerprint — **the same defect I hit from the
    other direction** when `files/` turned out empty and the prior manifest failed
    `--verify-artifacts` on every path. Found independently, from two directions, in one session.
- **Disease-agnostic micro-upgrade shipped:** `framework/scripts/text_surface_intrusion_check.py`
  with `framework/scripts/test_text_surface_intrusion_check.py` (**7/7 PASS**). It detects page
  furniture — page numbers in a consecutive numbering chain, non-tabular running headers — sitting
  **inside a continuing sentence**, i.e. spans across which a verbatim quote must not be taken.
  Nothing in it mentions WWOX, a disease or a gene.
- **Regression/evidence that makes the upgrade persistent:** seven regressions, of which **two are
  field reports from the tool's own first production run**: chart axis ticks reported as page
  numbers, and repeated table rows reported as running headers. Rather than satisfy the check I
  **strengthened it** — a bare integer now counts as a page number only if it belongs to a
  consecutive numbering chain, and a repeated line is excluded if it carries table-column gaps.
  Result on the PMID 20530675 supplement: **12 false positives → 1**. And the tool was then turned on
  **my own work**: of 15 text locators in the 21731849 manifest, **0 span an intrusion**.
- **Residual risk and next decisive action:**
  1. 🔴 **A defect with no lawful repair.** `FTR-20260814-20530675-01` carries a wrong DOI;
     `receipt_correction` must preserve study identity, `receipt_invalidation` is for evidence
     belonging to a different study. So the ledger now **refuses the correct identifier**. My receipt
     omits the DOI and records the correct value in prose. **Next action: an
     `identity_correction` record kind that may change `study_id` only, leaving every reading field
     frozen — a receipt-schema change, and not this actor's to make.**
  2. The stale 137/64 group counts (above) should be re-derived at the next wave.
  3. `text_surface_intrusion_check.py` is **not wired into any gate**. It is a command, run by hand.
     Wiring it into `deepdive_manifest.py` for PDF-derived surfaces is the obvious next step and was
     deliberately **not** done in the same change as its introduction.

---

## The three failure modes the protocol warns about — checked against my own answers

- **Answering yes to everything:** two `partial` grades, both self-caught and one of them
  (queue-vs-prose) **fixed inside this evaluation** rather than promised.
- **Grading the outcome instead of the process:** the outcome was unusually good — a closed
  supplement debt, a reversed association, a contradicted penetrance figure. The **process** still
  carried a stale measurement and a debt written only in prose, and those are graded separately.
- **Writing the diagnosis myself and calling it evidence:** stated plainly. Four of the eight
  failures above were caught by **tooling, not by me**, and one defect was found independently by
  `scientist-a` from the opposite direction. That attribution is the part worth trusting.
