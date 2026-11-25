# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-HDAC-SECOND-PLATFORM-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (own question, accepted into the mandate as an IT-initiated step) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the finding:** `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_hdac_second_platform_20261125/RESULT_HDAC_SECOND_PLATFORM_IT_20261125.md` (one reader, IT; PREREG committed after the Methods and Results text were read, before the blots). **Status:** PROPOSED, for the next `BATCH_COMMIT`; no registry file is edited by this act.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** One dated addition to one discovery-ledger entry; a source note on one registry line; no status, flag or claim link changes.

## 2 · Proposed lines
| Record | Change |
|---|---|
| `discovery_ledger_current.md` DL-REPO-003 | append, dated 2026-11-25: a second platform now read at figure level: a human ovarian carcinoma line (HO8910, the paper of PMID 23464470, the journal's open PDF) shows WWOX protein UP with sodium valproate 1 to 4 mmol/L over 48 h (pixel estimate 1.6 to 3.2 times control at 2 to 4 mmol/L, one blot, loading control beta-actin) and WWOX protein and mRNA UP in xenograft tumours (0.46 against 0.15; 0.305 against 0.193; ten mice per arm, tumours taken at death 47 versus 35 days, n per measurement not stated). The direction agrees with the hESC platform; it is a cancer line with wild-type WWOX, one blot per panel, no replicate unit; it does not address a neural cell, a WWOX allele or a patient. The fifth primary (PMID 28001369, same group as the hESC platform) stays unread. |
| `analysis/wwox_expression_boost_census_20260922.md` row B1 and unknown U4 (analysis file, ordinary route, dated note) | "read 2026-11-25 from the journal's open PDF; the 'no open access' statement was a route failure". |
| receipt | `FTR-20261125-23464470-01`, depth `partial_fulltext_read` (abstract, methods, results read; figures 4 and 5 opened; introduction, discussion, references not read). |

## 3 · Statements for the blind check at propagation time
1. Methods: HO8910; 1.0, 2.0, 3.0, 4.0 mmol/L sodium valproate, 48 h; anti-WWOX 1:250; beta-actin as loading control on the same stripped membrane; RT-PCR 30 cycles, normalised to GAPDH, WWOX 598 bp; 20 female nude mice equally divided; 0.4 percent valproate in drinking water.
2. Results text: tumour WWOX protein 0.46 +/- 0.065 against 0.15 +/- 0.025; mRNA 0.305 +/- 0.015 against 0.193 +/- 0.056; survival 47.12 +/- 0.73 against 34.58 +/- 0.46 days; no in vitro WWOX number printed.
3. Figure 4 (one blot, five lanes: control, 1.0, 2.0, 3.0, 4.0): WWOX band increases with dose by eye; the pixel estimate (script in the result folder) is 1.09, 1.63, 2.72, 3.17 times control.
4. Source file sha256 `c2a1066186030672a2a4c4ed0ad6efe82a594cb370073f41a2c4fc610485d778`.
