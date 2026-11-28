# Checkpoint IT37 (session c1c43605), written 2026-11-28 at about 252k context (measured: session_model_census peak 251581, 118 turns)

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119, bound by IT37 (verified BOUND), effort read back high (sonnet 5.5). Read this file only (`_10` is IT36's, done). Codex is never contacted. Measure context with `session_model_census.py --json --dir <project folder>` before stating a figure to a peer.

## Done (all landed on main; last push `4a16ca67a`, gate PASS)
* **IT36 owed text:** `research/session_evaluations/self_eval_orchestrator_it36_20261128.md` (self-evaluation, scout, takeaways).
* **Fresh reader on the checkpoint-36 "not re-read" clauses** (delegate afab97cd, sonnet 5.5, effort high stated; resumed for four reads): 26 clause parts, **2 MUST CHANGE (8 percent)**, 6 ADD, 18 OK. Both MUST CHANGE confirmed at source and repaired: "P14 to P18" for a systemic-null blood chemistry held at P18 only (CLAIM 036), and "denominator undefined" false for Fig 2G of PMID 34747138 (also in line 23 of `meta_gaba_paradox_current.md`). Re-read of repairs 11 items: 8 OK, 3 ADD, 0 MUST CHANGE. Two more live copies of the stage got dated pointers (`metabolic_differential_vulnerability_reposed_20260922.md`, `earliest_lesion_developmental_timeline_20260921.md`); third read: 4 OK, 3 ADD per paragraph, 0 MUST CHANGE, applied, not re-read. ADV corrected RP-019 on the same two points (`28ab242ea`). Line 422 of `peripheral_phenotype_denominator_audit_20260922.md` is a design, left.
* **CI:** runs 2897, 2900, 2907, 2909, 2912, 2914 success; 2918 (`44654d981`), 2925, 2928, 2929 and the later pushes were still in progress at the last read (queue about 20, each about 55 min). A monitor was armed in the old window and ends with it: re-read with `ci_runs.py status <full sha>`; a red from the check-run annotations.
* **ADV-333** (accepted from my proposal; folder `advisor_pilot_20261113/brainstorm_20261116/adv333_cross_it_20261128/`): PREREG frozen (`bb56d1e64`) before the whole read; cross of the 183 no-receipt records with the decision cells of RP-016, RP-018, RP-042, RP-043 found **no open-access record bearing on those four rows** (54 candidates with a PMID and no receipt: 6 open access, 7 requests timed out and unchecked, 41 not open inferred; six clinical case-series records are access-limited, operator PDF items). The nearest consumer of an open record is **RP-017** (named, and stated not to be one of the four). Record: PMID 31829254 (Mol Brain 2019, mouse VTA; Wwox picked by ISH similarity to Slc17a6; anti-WWOX sc-366,157 IHC, male C57BL/6J, age not stated, N = 6 mice, 22 slices, 22 medial and 14 lateral images; Fig 6c: 73.88 and 70.24 percent of WWOX-positive cells triple-labelled, about 10 percent carrying neither TH nor VGLUT2). **No antibody-specificity control is stated or visible** (frozen rejecting observation met: citable specificity premise rejected). RESULT states a premise line for RP-017 (immunoreactivity reported, not a demonstrated neuronal WWOX premise) and the registered missing observation (deficient-tissue or peptide-block control, per-animal proportions). Second reader on my first composition: **1 of 26 MUST CHANGE (4 percent)** ("adult" for animals of unstated age), 5 ADD; repairs applied, not re-read. Receipt `FTR-20261128-31829254-01` = `partial_fulltext_read` (text whole, Figs 5 and 6 viewed, Figs 1-4 captions only, references not read beyond WWOX statements). Derived surfaces regenerated and landed (ranking, reading_state, coverage, view trio, package, i18n collect). **Not done:** a countable PAPER NNN record (needs Figs 1-4, a deepdive manifest and a BATCH_COMMIT). Held bytes: `files/fulltext/PMID31829254_PMC6907252_epmc_20261128.xml` (sha256 `785a10ea6b5998f1777e8fdf14c3b68301e8ae541f3e4b11cd8e49c176a29543`); figures were fetched from `static-content.springer.com` into the job folder only.

## Open, in order
| # | Item | State |
|---|---|---|
| 1 | Hand ADV-333 to ADV (RP-017 owner) | message sent with this checkpoint |
| 2 | CI of 2918 and later | read; red from annotations |
| 3 | ADV-333 completion: PAPER NNN record (Figs 1-4 images, manifest, BATCH_COMMIT) only if ADV wants a countable record for a paper that moves one row's premise line; otherwise leave as partial | ADV decides |
| 4 | ADV-286 dates | C1 re-check 2026-12-05, C2 not before 2026-12-06, UNRESOLVED 2026-12-12 |
| 5 | IT36's worktree `it_36_20261128` removal | only via `branch_hygiene.py --removal` showing no reason (keep-age 6 h, eligible after 2026-11-28T20:55Z if it writes no more); never remove ignored files |
| 6 | My own worktree `it_37_20261128` | the next IT window makes its own; mine stays until the keep-age |

## Rules and traps (new this window)
* A catalogued stub can duplicate a processed record under another id (P295 = PMID 19936220, P363 = PMID 19500159): check the registry PMID against the ledger before calling a stub unread.
* An open-access scan whose display filter drops the "no" rows loses the count: print and keep the whole table before filtering.
* "Adult" and similar age words belong to the source's own description; copy the age the paper states for the animals used (the VTA paper states none).
* A repair is a first composition: three rounds again (2 of 26, 3 of 11 ADD, 3 of 7 ADD per paragraph); the last repairs go unread unless a further read is paid for.
* One receipt stales ranking.json, reading_state.md, coverage_report.md, the view, the package and the i18n collect: commit the receipt, regenerate, then land once (done in one push).
* The classifier stopped one response of mine after reading a record about tCAG discrepancies; recorded, not retried (nothing was lost: no file was half-written).
* The Agent tool takes `model` but no effort parameter: state the effort in the prompt.

## Peers at writing
ADV a5e6f2ad (accepted ADV-333; fixes the RP-008 stale line), HE c72e94ee, SCI f59eabd0. Disk 11 GB free at the last look.
