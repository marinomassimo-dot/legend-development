# ADV-264 result: is "no held artefact" the same as "not read"? (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; no spend, no contact, no network request, no byte restored, `coverage_report.md` and `reading_state.md` not edited. Pre-registration: `PREREG_ADV264_SCI_20261125.md` (05:48:06Z, before any recount). Scripts: `recount_adv264.py` (population, classes, digests, second hit) and `extension_complete_bytes_adv264.py` (declared post hoc, section 3). Tables: `population_adv264.tsv`, `complete_best_state_bytes_adv264.tsv`, `restorable_vs_operator_adv264.tsv`, `evidence_presence_*.jsonl`. Rerun: `python3 -I recount_adv264.py <repo> <root checkout> <folder>`.

## 1. Answer

* **For ADV-219's 497, the answer is no: they are almost all partial reads, not lost complete reads.** Re-derived on the current ledger the population is **500** (1,091 primary studies, 591 held by ADV-219's name rule, 500 not held; ADV-219 had 1,077, 575 and 497 on an older ledger). **Only 1 of the 500 has an earlier complete receipt (0.2%)**; 295 (59%) are substantial partials (Methods and Results both read in the union of receipts) and 204 (41%) are thin partials.
* **The "unheld is not unread" finding lives somewhere else: the complete reads.** Of the **313** studies whose best receipt is complete, **271 have bytes by the name rule and 42 (13.4%) have none**; the digest route adds none. Those 42 are read papers whose bytes are not on this host (the ADV-262 cases Suzuki 2007 and Saadane 2021 are of this kind).
* **ADV-219's name rule missed bytes that are held: 79 of the 500 (15.8%)** have a file under `files/fulltext` (44 of them in `rescued_from_scratch_he46`, 35 in assignment folders) whose SHA-256 equals the receipt's `source_fingerprint`, under names the "PMID digits" rule does not match (for example `PMC524435_article_page.html`, `biorxiv_2023.09.25.559198v1.pdf`). Not held becomes **421**, held becomes **670**. ADV-219's class A and B flags were not computed for these 79.
* **The corrected best-state figures are the ones the ledger already gave; nothing needs raising for lost bytes.** Best receipt per study over all 1,952 ledger studies: **complete 313, partial 1,053, abstract only 568, queried not read 18** (two independent counts agree). Under the "latest receipt" rule the same studies read complete 255, partial 1,091, abstract 581, queried 25: the latest rule hides 58 complete studies and overstates partial by 38 and abstract by 13. ADV's cited 313 reproduces; 1,049 and 570 differ by +4 and -2 (the ledger moved).
* **Restorable with the documented tool: 1.** Over the 63 papers with a deepdive manifest among the 42 complete-no-bytes and the 21 partial-no-bytes (62 manifests, 329 declared artefacts, 148 present, 181 absent), `evidence_presence.py --search` over `files/`, the job folders and the worktrees finds **one** exact-digest copy: `files/fulltext/PMID30370248_Tanna2018_PMC.xml`, present at `/home/desktop/.claude/jobs/53cd1e96/tmp/adv122/producer_d/dl/PMC6194312.xml` (a job folder that is deleted with its job). **Not run (`--restore` was out of scope); proposed, one command, into the declared path only.** The other 61 need re-acquisition; whether an open route exists was not tested here (the two cases of ADV-262 show the PMC article page can answer where Europe PMC XML does not).

## 2. Two-hit read

| Count | First hit (ADV-219 code path, key PMID else DOI) | Second hit (raw lines, key = event-id token) | Resolved |
|---|---|---|---|
| Studies in ledger | 1,952 | 1,952 | equal |
| Best state complete / partial / abstract / queried | 313 / 1,053 / 568 / 18 | 313 / 1,053 / 568 / 18 | equal |
| Latest receipt partial | 1,091 | 1,090 | the token `IHRIN` is shared by two DOI-keyed studies (10.64898/2026.02.03.703439 and 10.1101/2023.09.25.559198); the token key merges them. The study key is the identity here |
| Digest matches | 79 (one computation) | the same 79 re-found by hashing again through `evidence_presence`-independent code was not run; a second hash pass over the same files is not independent | **one hit only**; reported as such |

## 3. Extension declared after the first run

The brief asked about the 497; the digest result and K1 = 1 showed that the "read but lost" class is not in them. I added, post hoc, the same byte check for the 313 complete studies (`extension_complete_bytes_adv264.py`): 271 by name, 42 none, 0 added by digest. Its second hit is the same ledger read with the ADV-219 name rule; there is no independent second computation for the 42.

## 4. Expectations scored

* **K1 share 0.08 (0.03 to 0.20): not met, lower: 0.002.**
* **B1 share at most 0.05: not met, higher: 0.158.**
* **Best-state complete rises under 5 percent when K1 is counted: met trivially**, because best state already counts every receipt; the change is 0.
* **At least one of 313, 1,049, 570 does not reproduce: met** (1,049 and 570 differ).

## 5. Proposed counts (for HE or the ordinary regenerate step; nothing edited)

1. `coverage_report.md` / `reading_state.md` best-state figures: no correction for lost bytes. If a "held" column is added, it should say 271 of 313 complete studies have bytes by name (42 do not).
2. ADV-219's "no held artefact" figure: 421, not 497, once digests are used; its held population is 670. Its class A and B flags should be recomputed over the added 79 (not done).
3. Name rule: add a digest match against the receipt's `source_fingerprint` to any future held-artefact audit.
4. The DREAM line of this morning ("ADV-219's 497 include this class") is **corrected here**: the 497 do not; the class is the 42 complete-no-bytes studies.

## 6. For the operator

None needed for the count. For the 42 complete reads without bytes, re-acquisition would let their locators be re-verified; the list is `complete_best_state_bytes_adv264.tsv` (rows with `-` in both byte columns). Two of them are already on the PDF request list (Suzuki 2007 at rank 16; Gao 2025 is a partial read, not in the 42).

## 7. Limits

* The byte check covers `files/fulltext`, `files/deepening_downloads`, `files/supplement`, `files/figures` and `files/operator_inputs` of the root checkout (8,298 files hashed); receipts without a `source_fingerprint` (936 of 2,734) can be matched by name only.
* A study held under a name the rule does not match, with no digest in its receipts, is still counted not held.
* The class K2 is a union-of-receipts statement; it says Methods and Results were read, not that the n or the data were checked.
