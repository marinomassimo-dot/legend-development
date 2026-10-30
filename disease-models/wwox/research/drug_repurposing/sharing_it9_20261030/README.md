# IT9 P7: sharing, licences, privacy residuals, Internet view, continuity (scientist-d, 2026-10-30)

Branch `task/it9-p7`. Nothing reserved was executed: no history rewrite, no visibility change, no Pages enablement, no contact, no spend. No sensitive string is reproduced here.

## 1. Answers first

| question | answer |
|---|---|
| Can the gate's blind spot (html, js, css, patch, diff, cff, example; gz) be closed on the tip safely? | Yes for the seven plain-text suffixes (done, tested); NO for gzip. Tip before/after, privacy scan only: files read 4,256 -> 4,272 (+16: 4 html, 1 js, 1 css, 5 patch, 3 diff, 1 cff, 1 example); findings 30 -> 30 (all REVIEW), BLOCK 0 -> 0. The naive extension (suffixes only) would have added 3 BLOCK (one-line pages: a linkage word and both alleles tens of thousands of characters apart); the windowed rule removes them. Gate: PASS, 0 BLOCK |
| Is the repository public, is the view reachable? | Public (`private: false`, 0 forks, 0 stars), Pages not enabled, the site URL answers 404 |
| Do the DEPLOY.md section 11 facts and pins still hold? | Yes (section 4); the proposal workflow matches the package |
| Licences | Two attribution gaps fixed (adapter cache, Open Targets); STRING needs nothing (not redistributed); SIGNOR, LINCS, GEO and PubTator3 pages still unreadable (UNVERIFIED); R1, R2, R4, R5, R6, R7 stay reserved (`licence_table_it9.md`) |
| Continuity | Hourly control: 38 hours of existence, 38 runs, no gap, silent when unchanged, 0 failed deliveries after the probe. Radar: 2 scheduled runs possible, 2 evidenced, last at 05:20 UTC on 2026-10-30, after the last IT8 push (01:50). No small defect found (`continuity_verification_20261030.md`) |

## 2. Privacy: the four distinctions and the scan perimeter

The four distinctions, as the IT8 triage classifies them (`../privacy_triage_it8_20261029.md` sections 4 and 5) and as nothing in IT9 changes:

| class | meaning | IT8 count (BLOCK incidents, history) | at the tip |
|---|---|---|---|
| actual personal data | the operator's own name tokens in machine paths and one record | 14 incidents, 119 blobs | 0 |
| public identifier | published bibliographic data of third parties (262 author contact addresses, published-case statements, a vendor no-reply trailer) | 289 | 0 |
| fixture or detector text | reserved-domain addresses, `test_*` files, gate and rule vocabulary, false positives (hex fragments, UUID, SSH remotes) | 5 + 82 + 11 | gate and its tests only, exempt by name |
| potentially identifying clinical linkage | one statement naming the reference-class allele pair together; the pair is named on the same line in 24 tracked files at the tip by design | 1 | judgement reserved (section 5, item 4) |

Scan perimeter at the tip after this change, with the excluded surfaces:

| surface | read now? |
|---|---|
| `.md .txt .json .jsonl .csv .tsv .yaml .yml .toml .py .sh .rst`, `LICENSE`, `.gitignore` | yes, as before |
| `.html .js .css .patch .diff .cff .example` | YES, new (16 tracked files), by the privacy scan only; evaluated in 1,400-character overlapping windows |
| `.gz` (8 tracked: catalogue, associations, raw ClinicalTrials.gov page, 4 derived tables, collected pharmacology) | NO, on purpose. Opened by content they raise 31 BLOCK, all false or public: 16 + 7 + 2 are the hex-letter token inside 10-character substance codes, 6 are a third-party investigator name in a public registry record. Closing it needs a substance-code carve-out and an allowlist for a public name, plus decompression limits: that narrows a privacy rule and is not small |
| PNG (46 at the tip), PDF (6), `.pdb`, `.gb` | no (images and binaries; not OCR'd) |
| `backup/`, `.git`, untracked and git-ignored files (`files/`), nested checkouts | no (gate walk rules) |
| commit messages, author metadata, tags, GitHub-side copies, forks, caches | not scanned by the gate; IT7 covers metadata separately |
| split or encoded strings | not matched by construction |
| history | not re-scanned in IT9: the new suffixes apply to the tip; `privacy_triage_it8.py gap-scan` (unchanged) reads history by content |

Change (all reversible by `git revert`): `scripts/public_release_gate.py` adds `PRIVACY_EXTRA_SUFFIXES`, `iter_privacy_files` (used only by `scan_privacy_and_secrets`; `TEXT_SUFFIXES`, so link, wikilink and corpus checks, is untouched) and a windowed `record_blocks` for those suffixes. No existing rule is weaker: files that were not read now are. Tests (`scripts/test_public_release_gate.py`, 59 -> 62 tests, all pass): each of the seven suffixes blocks a name token, an e-mail address and a linked two-variant statement; `.gz` stays outside; a one-line page with the linkage word and the alleles thousands of characters apart does not block; the same pair near each other blocks, at 15 offsets across a window boundary; the same far text in `.md` still blocks (old behaviour); the link check does not widen. Mutations: emptying the suffix set fails 2 tests, removing the windowing fails 1.

## 3. Licences

See `licence_table_it9.md`. Applied: `THIRD_PARTY_NOTICES.md` entry for the adapter cache (68 files: 12 ChEMBL under CC BY-SA 3.0, 12 openFDA, 1 Open Targets with its CC0 reading read 2026-10-30, 43 PubTator3 flagged UNVERIFIED at source). Evidence: `evidence/dgidb_source_licences_20261030.tsv` (48 sources), `evidence/action_pins_and_repo_20261030.txt`.

## 4. Internet view

`operator_request_publish_view.md` is the single request: facts re-verified today, the six steps (decision on wording and noindex, Pages source, environment branch rule, copy the workflow, dispatch) and the URL verification commands. The expected URL is `https://marinomassimo-dot.github.io/legend-development/`. Delivery stays open until it answers 200 with the table's digest.

## 5. Reserved decisions, ready to paste (recommendation, impact, restore)

1. History rewrite of the privacy findings (options J, K, E1 of IT8). Recommendation: J plus K now (done: record, and the tip gate closed); NO rewrite (E1) for the present findings alone. Reason: 14 incidents are the operator's own account name in paths and one record (already public through the repository address), 262 are published author addresses of third parties, 1 is a wording lapse; a rewrite changes about 96 per cent of commit hashes and breaks every SHA-anchored seal and receipt, for low-sensitivity content. If the operator nevertheless wants removal, do it once, together with R4 (the page-crop folder, all nine blobs) and before web publication: `git bundle create <outside>/pre-rewrite.bundle --all`, then `git filter-repo --replace-text <LOCAL_FILE>` and `--path <crop folder> --invert-paths` on a fresh clone, verify with `git rev-list --objects --all -- <folder>` and the privacy tool, re-anchor seals, force-push, then option I (host purge request). The replacement file is built locally from the git-ignored findings of the triage, never committed. Impact: all hashes change, forks and clones keep the old history. Restore: the bundle (before clones exist the whole state; afterwards none). Reserved.
2. Visibility. Recommendation: keep the repository public. Switching to private (F) stops new reads but not clones, contradicts the project's public aim and the Pages route, and the scan gives no reason to treat any finding as an exposure of the proband or family. Impact of keeping: none. Restore of a later switch: switch back; cache behaviour unread.
3. Web publication of the shareable view. Recommendation: publish, route A, after the two wording points (publish wording, noindex while history findings stay open) and with the step list of `operator_request_publish_view.md`. Impact: a static page with counts, identifiers, own text, a 12-record ChEMBL class-B file with licence and credit; indexable unless noindex is added; the history findings are unchanged by it. Restore: Unpublish site plus delete the workflow file; third-party copies cannot be recalled.
4. The allele-pair judgement (IT8 section 11.4): whether naming the two worked-example alleles together, with the public owner identity and the disease, identifies a family. No scan can answer. Recommendation: keep the worked-example naming (it is the public edition's design: the reference genotype class), keep the gate rule that forbids linking them as one individual's genotype, and do not reword the 24 tip lines unless the operator knows of a reason. Impact if reworded: the explanatory value of the public examples drops. Restore: `git revert`.
5. Foundation letter (R5). Recommendation: the operator records one line in `SPONSORSHIP.md` (date, who agreed to publication of the letter, name and letterhead); if no permission exists, ask the Foundation (one question, by the operator) and replace the PDF by a link and summary in the meantime. Impact on research: none. Restore: `git checkout <sha> -- docs/WWOX-Foundation-letter-of-support-public.pdf`.
6. Third-party content (R1, R2, R6). Recommendation: before publication changes nothing in the package (it carries counts and one licensed class-B file); for the tracked merged catalogue, record the pre-change digests and a bundle, then take the IT8 option B-narrow in a separate task branch (replace class C rows by claim-source counts and identifiers; split B rows per source). Impact: rankings that depend on class C rows drop to "unknown"; the builder must be offline-reproducible first. Restore: `git checkout <tag> -- <paths>`.
7. External communication (host purge request I, rights holders NCI, TTD, DTC, CKB, CGI, OncoKB, ClinPGx, publishers). Recommendation: none now. Send no message with the operator's address to any service (standing rule). Revisit I only if decision 1 is taken.

## 6. UNVERIFIED and not done

SIGNOR, LINCS data policy, GEO disclaimer, PubTator3, ClinPGx, DTC, CGI, OncoKB, TTD pages are unreadable from this host. The GitHub Settings click paths come from the documentation, not from a logged-in session. Syslog is unreadable, so a cron start without state is unprovable. The history was not re-scanned with the new suffixes. The gzip blind spot is open.

## 7. For the batch path

Nothing for the registries or the four current files. For the mandate record: P7 DONE; evidence this README. Close the three stale OPEN records (`ORCH-METABOLIC-BATCH-20261019`, `ORCH-REPURPOSING-10H-20261021`, `INTAKE-OVERNIGHT-20261002`) to silence 2 KB per hour of no-op watch events. After final package regeneration, the DEPLOY.md hash table is regenerated by `repurposing_view.py package`. No read receipts were staged.

Checksums of the evidence files: see `sha256sum evidence/*`.
