# IT7 P8 licence inventory: independent verification

Verifier report, 2026-10-29. Subject: commit ba29fdd8 (`licence_inventory_it7_20261029.md` and `licence_inventory_it7.py`), inventory taken at `619418f1`.
Read-only toward the repository except this file. No history rewrite, visibility change, deletion, contact, registration or spend. No address,
mailbox, hostname or variant text is reproduced here; identity facts are counts and SHAs only. Not legal advice.

## 1. Recomputation

The script was re-run with `--rev 619418f1` (88 s). Its output matches the document's tables. Every count below was also recomputed with independent commands
(`git ls-tree`, `git rev-list --objects` + `cat-file --batch-check`, `git log --format`, Python parsing of the catalogue, `git grep`).

| item | document | verifier | result |
|---|---|---|---|
| tracked files / bytes at tip | 4 182 / 150 954 917 | 4 182 / 150 954 917 | confirmed |
| commits | 3 772 | 3 772 | confirmed |
| distinct blobs / bytes | 12 319 / 2 108 312 758 | 12 319 / 2 108 312 758 | confirmed |
| pack size | about 108 MiB | 108.02 MiB | confirmed |
| commits not in `origin/main` / `development/main` | 152 / 1 | 152 / 1 | confirmed |
| catalogue records / `targets[]` rows | 44 211 / 106 315 | 44 211 / 106 315 | confirmed |
| rows per claim source (22 sources) | table in section 2 | identical for all 22 | confirmed |
| class shares A/B/C | 1 623 / 47 061 / 57 631 = 1.5 / 44.3 / 54.2 % | same | confirmed |
| records by origin | 22 557 / 19 926 / 1 219 / 502 / 7 | same | confirmed |
| raw third-party response files | 132 files, 23 607 803 bytes decompressed | 132 files in the six folder groups, per-folder counts identical (3, 11+7+8, 49, 7, 46, 1); raw byte total not recomputed | confirmed (files), partly (bytes) |
| manifests / snippets / words / longest / >=25 / >=50 | 592 / 9 433 / 229 749 / 224 / 3 356 / 667 | identical | confirmed |
| page crops | 7 PNG added in ef20b9ef (3) and 902f943e (4), removed in de089055, 2026-08-09 | same; 7 deletions in de089055; reachable from `origin/main`, `development/main`, `backup/vps-main-2026-09-25` | confirmed; size stated "2.1 MB" is 2 031 445 bytes (2.03 MB, 1.94 MiB), a rounding looseness |
| Foundation letter PDF | 8ab8e4b8, 148 275 bytes, at tip | same | confirmed |
| corpus-seed blob / introducing commit | blob 43eb2dcedd, ca506034 (2026-08-06), cleaned dcbcc922 (2026-09-08) | same blob, commit and dates; ca506034 is 3 706 commits before the tip | confirmed |
| third-party addresses in that blob | "336 occurrences" | 430 occurrences, 262 distinct, in 245 of 706 records (generic address regex; none is the operator mailbox, none are placeholder/vendor domains) | NOT reproduced (defect D2) |
| other seed blobs (jsonl at tip, tsv, manifests) | not stated | 0 addresses in each | n/a |
| commits with the operator mailbox | 22 commits, 44 fields | 22 commits, 44 fields; all 22 reachable from `origin/main` | confirmed |
| operator hostname | 5 579 fields, 0 blobs | 5 579 fields, which sit in 2 790 commits (the document gives fields only); 0 files at the tip | confirmed; commit count added |
| placeholder fields | 18 | 18 (`example.org` 10, `example.invalid` 8) | confirmed |
| 40-hex strings at the tip | 819 distinct, 307 files, 202 commits | 819, 307, 202 commits (plus 489 blobs, 4 trees, 124 that resolve to nothing) | confirmed; composition added (D3) |
| path-ever count | 4 475 | 4 526 with `--all` in this worktree | difference is the extra task branches visible here, not a defect, but the figure depends on local refs |
| catalogue / associations / shareable-page versions | 5 / 11 / 54 | 5 / 11 / 54; first catalogue commit 2bd6cde1 is 410 commits before the tip | confirmed |
| preview directory | 23 image/PDF files at tip | 21 PNG + 2 PDF + 1 md = 24 | consistent |

## 2. Source terms (read at the sources in this session)

| claim | result |
|---|---|
| ChEMBL CC BY-SA 3.0 | CONFIRMED at the ChEMBL documentation ("made available on a Creative Commons Attribution-Share Alike 3.0 Unported License"). The page does not itself spell out attribution mechanics beyond "cite the publications / release DOI"; the policy file's wording "attribution with URL and release" is not on that page. |
| GtoPdb ODbL (database) and CC BY-SA 4.0 (contents) | CONFIRMED, verbatim, at the GtoPdb about page. |
| DGIdb has no licence of its own; per-source terms | PARTLY. The DGIdb web pages are script-rendered and returned no licence text. The public GraphQL endpoint returns, for every source, a licence string and a licence link, and no licence for DGIdb as a whole; this supports "per-source terms" but is an absence, not a statement. |
| DTC CC BY-NC-SA 3.0 | CONFIRMED as DGIdb's label and in the 2018 DTC paper ("available ... under CC BY-NC-SA 3.0"). The DTC site's current terms were not read. |
| CKB CC BY-NC-SA 4.0 | Confirmed only as DGIdb's label (source name there is now "CKB-CORE"). The CKB host did not resolve; unread at source. |
| CGI CC BY-NC 4.0 | Confirmed only as DGIdb's label. The CGI FAQ returned 403; unread at source. |
| TTD unclear | DGIdb's label confirmed ("All Rights Reserved" vs 2002 open-access description). The TTD site returned only its title; unread at source. |
| NCI "public domain declared by DGIdb; source page gone" | CONTRADICTED in part. DGIdb's own link, cancer.gov/policies/copyright-reuse, is live today. It says NCI text is "free of copyright" unless otherwise indicated, with third-party graphic exceptions. It does not use the phrase "public domain" and says nothing about Cancer Gene Index data specifically. Class C stays defensible; the wording "source page gone" is wrong (D4). |
| Other labels (OncoKB, MyCancerGenome, COSMIC, CancerCommons, CIViC CC0, FDA public domain, PharmGKB/ClinPGx CC BY-SA 4.0, DoCM CC BY 4.0, TEND/TALC/Tdg publisher tables, Clearity unknown) | Each matches DGIdb's licence string. Not read at their own sites here. |

Confirmed at source: ChEMBL and GtoPdb. Confirmed only as DGIdb's declaration: DTC (also in its paper), CKB, CGI, TTD, OncoKB and the rest. Unread at source: CKB, CGI, TTD, the DTC site, NCI Cancer Gene Index coverage, PharmGKB policy page, and every per-paper licence.

## 3. Alternatives, reversibility, missing items

Judgement of A to G: the effects and authority marks are sound. Notes:

- A: correct and the cheapest. It should say that a CC BY-SA 3.0 / ODbL-derived catalogue inside an MIT-labelled file is a share-alike question, which notices alone do not settle (the document says "may not be met"; keep that).
- B: "reversible from history" is true only while the history stays; if E is later chosen, B becomes irreversible. Say so.
- E: "NOT reversible for anyone who already cloned" is right, but the document omits the local safeguards and the wider footprint: a bundle of the pre-rewrite repository is a precondition; `backup/vps-main-2026-09-25`, the VPS recovery bundle and `refs/codex/turn-diffs` are further copies carrying the same material and are not touched by a rewrite of `main`; removing the operator hostname from the 2 790 commits that carry it rewrites about three quarters of all commits, so (d) is not a small add-on to (a)-(c) (the document ties the cost only to the earliest affected commit).
- F: the document says "reversible"; the effect of GitHub forks and caches on a private switch is unread here and should be marked so.

Risk statement for E (section 7) is mis-stated in two places (D3):

1. The read-receipt ledger's hash chain (`ledger_prev_hash`) is a SHA-256 over each record's own content, and the state-manifest tail anchor is an event count plus a head digest of the same kind. Neither uses git commit hashes. Of the 913 ledger lines, exactly 1 contains a 40-hex string. A path or blob rewrite that does not edit `fulltext_read_receipts.jsonl` leaves the chain and anchor valid. The coupling that does exist is through records and seals that quote commit SHAs (39 `git_head_at_freeze` occurrences, `framework/state/state_history.md`, `sync_epochs.jsonl`, 12-character short SHAs in prose that the J2 deriver anchors on).
2. "202 resolve to commits that would change" is an upper bound. A commit changes only if it descends from the earliest rewritten commit. Of the 202: 199 descend from ca506034, 195 from ef20b9ef, 4 from 2bd6cde1 and 3 from 7aeef97c. 5 of the 202 are not reachable from the tip. The 489 blob and 4 tree SHAs change only if those very blobs are rewritten, and 124 strings already resolve to nothing in this clone (private-edition or truncated references).

Alternatives missing:

- H. Orphan or squashed public history, with the full history kept in a private archive: avoids `filter-repo` reconciliation, makes old SHA citations point into the archive, reversible while the archive exists. A cross between D and E.
- I. Provider-side removal request (cached views, dangling objects, fork network) to the hosting service. Needs contact, so OPERATOR; it is the only route that addresses what section 9 calls unverifiable.
- J. Do nothing but record: keep a dated register of the known exposures and a prepared response for a notice. It is the baseline against which A to G should be priced.
- K. Narrow rewrite limited to the personal-mailbox fields and the corpus-seed blob (cost set by ca506034, 3 706 commits), versus the class C catalogue versions (cost set by 2bd6cde1, 410 commits). The document mentions both costs but offers them as one operation.

"Reserved for the operator" list: complete for what it names. Additions: (i) the disposition of the history findings in section 4 below (a decision whether history-only privacy hits need action); (ii) the other copies (backup branch, recovery bundle, codex ref) and whether they are in or out of any rewrite or publication scope; (iii) who may re-anchor seals and the ledger tail after any rewrite; (iv) a legal-hold style decision not to destroy material while a notice is possible; (v) a request to the hosting provider (I).

## 4. History privacy scan (read-only, counts only)

Method. All 8 081 distinct (blob, path) pairs in history that are not blobs of the tip and whose suffix is a text suffix (json, jsonl, md, py, tsv, txt, yaml, sh, html and similar) were materialised outside the repository. The privacy section of `public_release_gate.py` (`scan_privacy_and_secrets`, run as a function on that directory) was applied to them.
`independent_privacy_scan.py` was started on the same set and stopped after about 19 minutes without output; it did not complete, so it is NOT reported. `commit_metadata_scan.py` with base `ca506034~1` blocks every non-project identity and is consistent with section 1 (its output was not otherwise used).

Result. 2 778 findings in 763 distinct blobs: 1 202 BLOCK (in 198 blobs) and 1 576 REVIEW. Baseline: the same function over an export of the tip gives 30 findings (1 BLOCK, 29 REVIEW), so the tip's PASS verdict does not carry over to history.

BLOCK-severity blobs by code (history-only blobs): direct identifier 125 (205 findings in all severities), e-mail address 24, parent-of-origin pairing 35, parent-of-origin reference-genotype 31, parent-of-origin variant linkage 32, re-identifying variant combination 9, clinical-case linkage 17, geographic-case linkage 13, parent-of-origin linkage 8.
Excluding the gate source, its tests, the independent scanner and `launch/KERNEL_SPEC.md` (detector vocabulary, expected to self-match): direct identifier 91 blobs, e-mail 16, pairing 15, reference-genotype 11, variant linkage 12, clinical-case linkage 5, geographic-case linkage 1, re-identifying combination 1.
The 91 non-self-referential direct-identifier blobs were introduced by 74 commits dated 2026-08-10 to 2026-10-28 (77 in August, 8 in September, 6 in October); 72 of them sit at paths that still exist at the tip, so they are earlier versions that were later cleaned or reworded. The largest single introducing commits are d84ed69a, cb50e177 and 43668dd0. A list of all introducing commits for the 176 BLOCK blobs that map to a commit (147 commits, 4 in July, 100 in August, 31 in September, 41 in October) is reproducible with the gate function above.
Crude pattern count (the gate's two variant patterns, paragraph level, in history-only blobs): 1 252 paragraphs carry both variant patterns, in 517 blobs; 255 of those also carry a person or linkage term, in 213 blobs; the tip, by the same crude test, has 54 and 13 paragraphs. This test is not a finding; the gate's own semantic logic (reference-genotype and negation windows) is the judge, and it was applied above.

Limits. The findings are not adjudicated: the digest-matched "direct identifier" hits could be matches on common words in older, looser text, and the pairing/linkage codes include text that the public edition's reference-genotype wording would now accept. Blobs reached only through merges were not all mapped to a commit (22 of 198). Binary files, PDFs and files over 30 MB were not scanned. No finding was checked against the hosting provider.

## 5. Severity-ranked defects

| id | severity | defect | where |
|---|---|---|---|
| D1 | HIGH | Section 5 and ranking row 4 understate history privacy exposure because the gate was never run on history. Run read-only, it reports 198 history-only blobs with BLOCK findings (91 direct-identifier blobs outside gate and test files, 74 introducing commits, Aug to Oct 2026), against 1 BLOCK at the tip. Not adjudicated, but it changes problem 4 from "mailbox, hostname, seed e-mails" to an open scan result the operator must see. Open item 8 should be marked as done in this verifier file and kept open for adjudication. | document sections 5, 6 (row 4), 8 (item 8) |
| D2 | MEDIUM | "336 occurrences" of third-party addresses in the corpus-seed blob does not reproduce: 430 occurrences, 262 distinct, in 245 of 706 records. The figure is not printed by the script; it is a hand number without a command. Direction of error: understated. | document section 5 |
| D3 | MEDIUM | Risk statement for E mis-describes the ledger and over-counts the SHA exposure: the ledger chain and tail anchor are content hashes, only 1 of 913 lines holds a 40-hex string, and only commits descending from the earliest rewritten commit change (199, 195, 4 or 3 of 202 depending on the starting point; 5 are unreachable from the tip; 124 strings already resolve to nothing). The risk that is real, seals and short SHAs, is not counted. Omitted: the pre-rewrite bundle, the other copies, and the fact that removing the hostname rewrites about 2 790 of 3 772 commits. | document section 7 |
| D4 | MEDIUM | NCI "source page gone" is wrong; the NCI reuse page is live and says "free of copyright" with third-party exceptions, without the words "public domain" and without naming the Cancer Gene Index. Whether it covers CGI rows is unread. | document section 2 table, section 6 row 1, policy file text |
| D5 | LOW | Alternatives table lacks H (orphan or squashed public history with a private archive), I (hosting-provider removal request), J (do nothing and record). B's reversibility is conditional on E not being chosen. F's reversibility is stated without reading how forks and caches behave. | document section 7 |
| D6 | LOW | Reserved list lacks: disposition of history privacy findings; other copies (backup branch, recovery bundle, codex ref); who re-anchors seals; no-destruction while a notice is possible; provider request. | document section 8 |
| D7 | LOW | Rounding and labelling: crops "2.1 MB" is 2.03 MB; hostname commits (2 790) not given beside the 5 579 fields; "4 475 paths ever" depends on which refs exist locally. | document sections 0, 4, 5, 10 |
| D8 | LOW | ChEMBL attribution wording ("URL and release version") and DGIdb "no licence of its own" are policy-file statements not found on the pages read; DTC, CKB, CGI, TTD remain declarations by DGIdb. The document already says "not verified"; this report only confirms that status. | document section 2 |

Not defects: script output equals document tables; hash-chain remark in CLAUDE.md is correctly cited but over-applied (D3); page-crop and Foundation-letter facts are exact.

Reproduce the checks: the script command in the document; `git rev-list --objects`/`cat-file --batch-check` for blobs; the catalogue parse from section 2 of the document; `git grep -I -h -o -E '\b[0-9a-f]{40}\b' 619418f1` for the SHA census; `scan_privacy_and_secrets` from `scripts/public_release_gate.py` called on a directory of materialised history-only blobs for section 4.
