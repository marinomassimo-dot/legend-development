# Privacy triage of the Git history (IT8 P1)

Status: working triage for the operator, 2026-10-29. Classification only. It rewrites no history, changes no visibility, deletes nothing and
contacts nobody. The decision on every option in section 10 is reserved to the operator.

Non-identifying by construction: this file names blobs and commits by SHA, files by path and line number, and everything else by class and count. No
matched string, address, name, variant or identifier is reproduced here. Anything a human needs in order to decide (the matched lines themselves) is kept
only in the local, git-ignored directory `files/privacy_local_it8/` of the operator's machine (`findings.jsonl`, `classified.jsonl`,
`isolated.jsonl`, `gap_findings.jsonl`, `tip_*.jsonl`).

Reproduce (repository root; the three first commands are the whole of it, the others are variants):

```
python3 disease-models/wwox/research/drug_repurposing/privacy_triage_it8.py scan          --out <LOCAL_DIR>   # gate over history, 4 jobs; about 5 min idle machine
python3 disease-models/wwox/research/drug_repurposing/privacy_triage_it8.py scan --tip    --out <LOCAL_DIR>   # the same over the tip, for "also present at the tip"
python3 disease-models/wwox/research/drug_repurposing/privacy_triage_it8.py classify      --out <LOCAL_DIR>   # every table of section 5, counts only
python3 disease-models/wwox/research/drug_repurposing/privacy_triage_it8.py scan-isolated [--tip] --out <LOCAL_DIR>   # scripts/independent_privacy_scan.py over the same files; 20 to 80 min depending on load
python3 disease-models/wwox/research/drug_repurposing/privacy_triage_it8.py compare [--tip]  --out <LOCAL_DIR>        # section 7 tables
python3 disease-models/wwox/research/drug_repurposing/privacy_triage_it8.py gap-scan [--tip]  --out <LOCAL_DIR>       # section 8: text the gate's suffix list never opens
python3 disease-models/wwox/research/drug_repurposing/privacy_triage_it8.py gate-delta --old-rev <REV>  --out <LOCAL_DIR>  # section 9 before/after
```

`<LOCAL_DIR>` must be outside the repository (the tool refuses otherwise). The tool imports `scripts/public_release_gate.py` and
`scripts/independent_privacy_scan.py` as modules and does not modify them. `classify` is deterministic (two runs compared byte for byte).

## 1. Answers first

| question | answer |
|---|---|
| Is the repository public? | Yes. Verified without credentials: the GitHub REST API reports `private: false`, `visibility: public`, 0 forks, 0 stars, 0 open issues or pull requests, 0 tags, one branch (`main`, at `10118886`), licence MIT. See section 2. |
| Does any actual private data of the proband or of the family appear exposed? | **No evidence of it in the 9 105 history-only text blobs read by the gate.** Of the three legacy full-name tokens only one matched in running text or paths, and it is the operator's own; the other two matched nowhere in the scanned text, and the short form of one of them matched only inside identifiers (UUIDs, UNII codes, short digests). What is exposed is (i) the operator's own given name (and once the family name) inside machine-account paths and in one decision record, history only, 119 blobs, all reachable from the public `main`, and (ii) 262 distinct third-party author contact addresses in four blobs (published bibliographic metadata; section 6.4). Both are low sensitivity; neither identifies the proband. The identity of the repository owner is itself public through the repository address and commit metadata, so (i) adds little new. One residual risk is not a scan result and is stated in section 11. |
| The IT7 headline (2 778 findings, 1 202 BLOCK in 198 blobs, about 124 commits) | Reproduced exactly on the same population (section 3). After deduplication: **402 distinct BLOCK incidents** (393 in the IT7 population), of which 14 are actual personal data of the operator, 1 is a statement naming the reference-class allele pair together, 11 are false positives, and the rest are third-party bibliographic data, synthetic fixtures and detector or rule text. |
| Does the tip still contain any of it? | The gate passes on the tip (`VERDICT: PASS`, `BLOCKS: 0`, run on this worktree). None of the 14 personal-data incidents is present at the tip. The tip does contain items the gate cannot see (section 8). |
| Gate rule | Implemented: a sensitive word fully inside a canonical UUID no longer blocks. 15 false positives removed in 6 blobs, 0 added, over the full classified set; mutation tests included (section 9). |

## 2. Visibility (what is verifiable and what is not)

Verified now, read-only and unauthenticated (`gh` is not installed on this machine; HTTPS to `github.com` and `api.github.com` was used):

| fact | value | how |
|---|---|---|
| repository page and API | HTTP 200 without credentials | `curl` on the repository page and on `/repos/<owner>/<name>` |
| `private` / `visibility` | `false` / `public` | API body |
| refs served | exactly one: `refs/heads/main` = `101188866f39...` (= local `development/main`); no tags; 0 pull requests | `git ls-remote` over HTTPS, `/branches`, `/tags`, `/pulls` |
| forks, stars, watchers, network | 0, 0, 0, 0 | API body |
| created / last push | 2026-08-23 / 2026-10-29 | API body |
| licence, wiki, issues | MIT; issues and wiki enabled | API body |

Consequences: the object database that anyone can clone is exactly the history reachable from `101188866f39`. The local refs `backup/vps-main-2026-09-25`, the `refs/codex/...` turn-diff ref and every `task/*` branch are **not** on the remote (verified by `ls-remote`); material found only through them (section 3, "other refs") is local exposure only.

Not verifiable from here: whether GitHub retains unreachable objects, cached views or search-engine copies of earlier states; whether anyone cloned the repository between 2026-08-23 and now (0 forks and 0 stars are the only signals); the repository's behaviour on a visibility switch. Anyone who cloned has the whole history; only a hosting-side action can address the remainder (option I of IT7 section 7).

## 3. What IT7 covered, and the delta

IT7 scanned the history-only text (blob, path) pairs of `619418f1` (3 772 commits) with `scan_privacy_and_secrets` of the release gate. This triage re-ran the same function with finding-level output.

| measure | IT7 | this run | note |
|---|---|---|---|
| revision | `619418f1` | `fccf0a3f` (3 894 commits; 3 893 on the served `main`) | 122 commits after `619418f1` |
| history-only text (blob, path) pairs in the IT7 population | 8 081 | **8 081** | same rule: text suffix, at most 30 MB, blob not at the tip of the revision |
| findings, IT7 population | 2 778 in 763 blobs; BLOCK 1 202 in 198 blobs | **2 778 in 763; BLOCK 1 202 in 198** | identical |
| non-self-referential BLOCK blobs | 166 | 166 | IT7 listed the isolated scanner under `framework/scripts/`, where it has never lived (it is `scripts/`); no result changed, because that file produces no gate finding |
| blobs mapped to an introducing commit | 156 of 166 (10 unmapped) | 204 of 204 | single `git log --all -m --raw` pass instead of one `--find-object` per blob |

Delta and other refs, analysed separately from the IT7 population:

| segment | pairs | findings | BLOCK findings | BLOCK blobs | what the BLOCK findings are |
|---|---|---|---|---|---|
| IT7 population (history-only at `619418f1`) | 8 081 | 2 778 | 1 202 | 198 | section 5 |
| delta: pairs that became history-only in the 122 later commits (reachable from the served `main`) | 176 | 14 | 3 | 2 | 2 findings are a DailyMed set-id (false positive, one blob of IT7 P2's pilot table); 1 is a review record discussing the rule |
| other refs only (local branches, backup ref, codex ref; not on the remote) | 848 at run time (the number moves with live branches) | 115 | 8 | 4 | rule discussion in records (6), one short digest (1), one published case (1) |

Everything in the delta is reachable from the served `main`; 121 of the 122 later commits are pushed (one local mandate-record commit is not).

## 4. Method: deduplication and classification

Units, stated so that a verifier can recompute them:

| unit | definition |
|---|---|
| occurrence | one gate finding (the function's own unit; one per matched word, address or rule hit) |
| blob | one distinct Git blob (here also one (blob, path) pair: no blob occurs under two paths in the population) |
| introducing commit | the earliest commit (by committer time, then SHA) whose diff adds or modifies the blob, over all refs, merges included |
| distinct incident | one underlying string or record: for UUID-contained hits the UUID; for machine paths the path run; for e-mail the case-folded address; for name tokens and rule hits the lower-case alphanumeric normalisation of the line. Edited or reflowed copies of one statement count as separate incidents, so incident counts are upper bounds |

Classification is by structure, not by reading the matched word:

| class | rule |
|---|---|
| detector text or rule discussion | path is the gate, its tests, the isolated scanner, its tests or `launch/KERNEL_SPEC.md` (except that its machine-path hits are personal data, below), or the line talks about the rule (gate, detector, BLOCK/REVIEW, pairing, "not carried") |
| false positive (hex fragment, common word) | the hex-letter private token inside a canonical UUID or beside digits in a short digest; an SSH remote `git@host`; the generic phrase "patient-derived" |
| synthetic fixture or example | reserved or fake address domains, or a `test_*` file |
| public or bibliographic identifier | an address in published bibliographic metadata or beside a PMID; a parental or case statement on a line with a PMID/PMC/DOI or in a per-paper file (`PMIDnnn`, `PPRnnn`, dossier, deep-dive manifest, commit candidate of a named paper); the gate's own REVIEW attribution |
| actual personal data | an exact-case name token in text; the casefolded name token inside a machine home path |
| potentially identifying clinical linkage | a line carrying both variant patterns of the reference class together as one genotype |
| unresolved | none remains: 12 lines that no rule classified were read in context and adjudicated by hand (table `MANUAL` in the script, keyed by blob prefix, line and code: 6 published-case statements, 4 rule discussions, 1 detector-vocabulary regex in a battery script, 1 generic phrase) |

Sampling check done here: every line behind a non-detector, non-personal class was read in masked form (variants replaced by placeholders) once; the published-case class is 21 blobs, the lines are third-party case or cohort descriptions with a PMID or per-paper file.

## 5. Results

BLOCK findings, all segments (the whole population of 9 105 pairs at run time):

| class | occurrences | blobs | introducing commits | distinct incidents | blobs reachable from the served `main` | blobs whose path is still at the tip | incidents also at the tip |
|---|---|---|---|---|---|---|---|
| public or bibliographic identifier | 465 | 26 | 22 | 289 | 25 | 26 | 0 |
| synthetic fixture or example | 33 | 16 | 16 | 5 | 16 | 16 | 2 |
| detector text or rule discussion | 501 | 42 | 33 | 82 | 40 | 39 | 56 (gate and its tests, exempt in the gate by name) |
| false positive (hex, common word) | 22 | 12 | 9 | 11 | 11 | 11 | 0 |
| actual personal data (operator's own name tokens) | 191 | 119 | 94 | 14 | 119 | 100 | 0 |
| potentially identifying clinical linkage | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| **total** | **1 213** | **204** | **163** | **402** | | | |

IT7 population only: 1 202 occurrences, 198 blobs, 158 introducing commits, 393 distinct incidents (the 11 occurrences, 9 incidents and 5 commits that differ are the delta and the other-refs segments; commits are counted once per class in the table above and once overall in the total, because one commit can introduce blobs of several classes).

Sub-types (whole population; occurrences / blobs / incidents):

| class | sub-type | occ. | blobs | incidents |
|---|---|---|---|---|
| personal | casefolded name token inside a `/Users/<name>/...` or `~/...` path (macOS home of the operator, 2026-08 to 2026-09) | 190 | 118 | 13 |
| personal | exact-case name token in running text (one decision record, line 14) | 1 | 1 | 1 |
| public | third-party author contact address (corpus seed, three audit notes) | 433 | 4 | 262 |
| public | parental / case statement on a published case, cohort or preprint | 31 | 21 | 26 |
| public | vendor no-reply co-author trailer | 1 | 1 | 1 |
| fixture | reserved or fake address domain | 25 | 15 | 4 |
| fixture | address in a `test_*` file | 8 | 8 | 1 |
| detector / rule | gate, scanner, their tests, kernel spec (vocabulary) | 461 | 21 | 65 |
| detector / rule | rule discussed in review, session and handoff records | 40 | 21 | 18 |
| false positive | token inside a canonical UUID (DailyMed set-id 2, Signature Commons entity ids 12, a session directory name 1) | 15 | 6 | 7 |
| false positive | token inside a short digest or commit SHA | 2 | 2 | 2 |
| false positive | SSH remote form, not a mailbox | 4 | 3 | 1 |
| false positive | generic phrase "patient-derived" | 1 | 1 | 1 |
| clinical linkage | reference-class allele pair named together | 1 | 1 | 1 |

REVIEW findings (the gate's own "not blocked, read it" severity): 1 694 occurrences in 683 blobs, 34 distinct incidents. 1 682 occurrences (31 incidents) are parental statements attributed to a published study (PMID/DOI in the same record) or a published author's name field; the other 12 are the gate's own vocabulary. They are listed for completeness; the gate has already adjudicated them by its attribution rule.

By month of the introducing commit (blobs): personal data 2026-08: 111, 2026-09: 8; clinical-linkage statement 2026-10: 1; false positives 2026-09: 4, 2026-10: 8; third-party bibliographic 2026-08: 1, 2026-09: 7, 2026-10: 18.

## 6. The substantial cases (source, context, reachability, tip)

### 6.1 Operator's name tokens in machine paths (class personal; 118 blobs, 13 incidents)

Source: ledger, session, handoff and queue records of 2026-08 that quote the operator's macOS working directory (a home directory named after the operator, then `Desktop/legend-public/...` or `legend-codex-...`), plus `launch/KERNEL_SPEC.md` (12 blobs; a lineage directory name under `~/.legend/`). The largest single incident is one working-directory path repeated in 89 blobs (107 occurrences). Context: a path or a lineage id, not a statement about a person. First added 2026-08-10 (`5d3571ad` is the earliest by committer time), last 2026-09-07 (`9cd92a15`); 93 introducing commits. Reachable: all 118 blobs from the served `main`. At the tip: 100 of the 118 blobs are earlier versions of paths that still exist, but **0 of the 13 incidents is present at the tip** (the gate passes). Sensitivity: low; the operator's account name is the operator's own first name, which is also in the repository address.

### 6.2 Operator's name in one decision record (class personal; 1 blob, 1 incident)

`governance/decisions/DEC-20260820-ORCH-SESSION-HOME.md` line 14, blob `de4fcc32`, added 2026-08-20 (`ec4bf603`): a `ratified_by` field with the operator's given and family name. History only; reachable from the served `main`; the tip version no longer carries it.

### 6.3 One statement naming the reference-class allele pair together (class clinical linkage; 1 blob)

`disease-models/wwox/research/locator_audits/2026-10-28_it4_ptc_enumeration_independent_verification.md`, blob `4acc3a62e2`, lines 73 and 90, added 2026-10-28 (`f878cc54`); reachable from the served `main`; a later version of the file exists at the tip and passes. The line describes the reference class as one missense allele plus one null-predicted splice allele and names both. **Context the gate cannot weigh:** at the tip the two alleles are named on the same line in 24 tracked files and anywhere in the same file in 48 (the first allele alone in 459, the second alone in 60; measured at `fccf0a3f` over tracked text files). The public edition's design names the worked-example alleles; what the gate forbids is *linking* them as one individual's genotype by wording. So this blob is a one-off wording lapse against a rule the repository enforces at the tip, and also a sample of a pairing the repository publishes elsewhere by design. Whether the pair itself is acceptable in a public repository is the operator's decision (section 11).

### 6.4 Third-party author contact addresses (class public; 4 blobs, 262 distinct addresses, 433 occurrences)

`registries/corpus_seed_pubmed_20260806.jsonl` blob `43eb2dcedd` (430 occurrences, 261 distinct, 245 of 706 records; introduced `ca506034` 2026-08-06; cleaned at the tip by `dcbcc922`) and three audit notes quoting a corresponding author's address (2026-09-20/21). These are published bibliographic contact data of third parties, which the 2026-09-07 decision (option C: names and institutions allowed, contact fields restricted) says should not be carried. They are not the project's subject and not private to the family; they are a third-party privacy-policy exception in history. Reachable from the served `main`; 0 present at the tip.

### 6.5 Everything else

False positives (section 5) are hex-letter matches inside identifiers (UUIDs, a 10-character UNII code, short digests, an SSH remote), plus one generic phrase. Synthetic fixtures are `example.org`, `x.invalid` and `e.st` addresses in tests and in records quoting them. Detector text is 461 gate-vocabulary occurrences in 21 blobs of the gate, its tests, the scanner and the kernel spec, plus 40 occurrences in records that discuss the rules. Published-case statements are third-party case, cohort or preprint descriptions with a PMID or per-paper file name (for example a family description in a published pedigree).

## 7. Isolated scanner versus gate: why they disagree

| aspect | `scan_privacy_and_secrets` (gate) | `independent_privacy_scan.py` |
|---|---|---|
| walk | git-aware: skips files that are untracked and ignored, prunes nested checkouts, skips `backup/`; exempts `scripts/public_release_gate.py` and its test by name | plain `rglob`; no git; skips only its own source; scans the gate and its test |
| file types | `.md .txt .json .jsonl .csv .tsv .yaml .yml .toml .py .sh .rst`, `LICENSE`, `.gitignore` | `.cfg .csv .ini .json .jsonl .md .py .rst .toml .tsv .txt .yaml .yml`, `LICENSE`, `NOTICE`; no `.sh`, no `.gitignore` |
| decoding | UTF-8 with replacement | strict UTF-8; an undecodable file is an error and is not scanned (0 such files here) |
| unit | whole file, paragraph or JSON/JSONL record; windows of +-350 and +-700 characters | one line |
| name tokens | five exact and three casefolded digests, plus a path rule; ignores letters inside 32+ hex runs and 12+ hex fragments with a digit | same digests and the same hex carve-outs (ported), checked per line; path words decided first; adds codepoint-assembled name matching *inside larger tokens* ("glued" names) |
| semantic rules | parent-of-origin pairing, variant linkage, reference-genotype linkage, person/proband windows, clinical regimen, geography word `Italy`, two-variant combinations; negation and PMID/DOI attribution lower a finding to REVIEW or suppress it | none |
| other detectors | e-mail (placeholders and `example.invalid/.test` exempt), report ids, private keys, token shapes, PRIVATE/MIXED provenance | e-mail (only `example.com` and `example.invalid` informational), Italian city and hospital lists, one geography digest, `dd-mm-yyyy` dates, `AA123-45` ids |
| e-mail edge | accepts an address followed by a full stop | does not match an address followed by `.` or `-` (a corresponding-author address ending a sentence is missed: 1 blob here) |
| speed | about 5 min for the history on 4 jobs | 20 to 80 min; the IT7 verifier stopped it after 19 min; a memoised SHA-256 (same digests) makes it finish |

Measured over the same history-only files reachable from the served `main` (self-referential paths excluded):

| comparison | blobs |
|---|---|
| gate non-self BLOCK | 168 |
| scanner non-self BLOCK | 781 |
| both | 131 |
| gate only | 37: the semantic parent-of-origin and linkage rules, which the scanner does not have (38 blobs carry such rules; only 2 of them are also blocked by the scanner for another reason) |
| scanner only | 650: Italian city and hospital names, calendar dates, `AA123-45` ids and the project's own no-reply identity, which the gate whitelists |
| name-token agreement | gate direct-identifier blobs 114, scanner private-name blobs 115, both 114; the one scanner-only blob is the corpus-seed author-name field that the gate downgrades to REVIEW by design |
| e-mail agreement | gate 16, scanner 25, both 15; the 10 scanner-only blobs all quote the project's own no-reply commit identity, which the gate whitelists as publishable by construction; 1 gate-only blob is the sentence-final-address blind spot |

At the tip the contrast is starker: the gate has 0 non-self BLOCK blobs, the scanner has 65 (city and hospital names in affiliations and literature notes, DOI `pii` fields shaped like dates, institution sponsors, a drug code that matches the `AO` hospital abbreviation). Every scanner-only tip hit sampled here (all four categories with a non-bibliographic context were read) is published or generic text; none is personal. The disagreement is therefore not a disagreement about the same items: the two tools check different things, and neither subsumes the other. Only the name-token and e-mail checks overlap, and there they agree.

## 8. What is NOT covered

| area | size | status |
|---|---|---|
| PNG images | 48 history-only pairs (10.4 MB); 46 tracked at the tip | not read by any scan; not OCR'd |
| PDF | 7 history-only pairs (1.5 MB); 6 at the tip | not read |
| other binaries (`.pdb`, `.gb` at the tip) | few | not read |
| files over 30 MB | 0 in history or at the tip | n/a |
| HTML, JavaScript, CSS, patch, diff, `.cff`, `.example`, `.gitignore`, extensionless | 184 history-only pairs and 24 at the tip (HTML and gzip included) | **the gate's suffix list never opens them**, and the IT7 subcommand writes `.html` files to disk but the gate ignores them, so "html scanned" in IT7 section 5 is not so. Scanned here by content (renamed to `.txt`, same gate function): see below |
| gzip-compressed tables | 15 history-only pairs; 6 at the tip | decompressed and scanned here as text (same call) |
| commit messages, author and committer metadata, tags, refs, tree names | all | not part of this scan (IT7 sections 5 and 6 cover metadata separately) |
| strings split across lines or encoded (base64, escapes) | unknown | by construction not matched |
| deleted-and-never-committed material, GitHub-side copies, forks, caches | unknown | not observable |

Gate-blind text scanned here by content (counts):

| segment | pairs | findings | what they are |
|---|---|---|---|
| history-only, text-like files outside the suffix list | 184 | 185 BLOCK | 66 name-token hits in 5 gzip blobs: all are the hex-letter token inside UNII substance codes of the catalogue (false positive); 119 two-variant "combination" hits, one per blob, in 119 versions of the view's HTML pages: a block-scope artefact (the whole page is one 1.6 to 2 MB line, so a linkage word anywhere pairs with both variant patterns anywhere; the page names the reference-class alleles in separate cards), not a statement linking them |
| tip, the same kinds of files | 24 pairs (23 blobs) | 27 BLOCK | 18 UNII false positives and 6 hits on a third-party investigator name in a ClinicalTrials.gov raw page (public registry), in 3 gzip blobs; 3 two-variant block-scope hits in 2 HTML pages |

So the part of the tip that the gate does not read contains no personal data of the family either, but it **does** contain text that the gate would block if it read it (all classified false or public above). That is a standing blind spot, listed as an option in section 10.

## 9. Targeted contextual rule for the gate (implemented)

Hypothesis tested: a UUID is a record identifier; the only private token made of hex letters only can sit inside one by chance, and a DailyMed set-id or a Signature Commons entity id is such a UUID.

Rule (in `scan_privacy_and_secrets`, `scripts/public_release_gate.py`): a sensitive word is skipped when its whole span lies inside a canonical UUID, `(?<![0-9A-Za-z])[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}(?![0-9A-Za-z])`, that contains at least one decimal digit; computed lazily once per file and only for a sensitive word, so the gate's run time is unchanged. A word beside a UUID (space, comma, hyphen) or glued to it is outside the span and still blocks; a UUID with a short or long group is not a UUID and still blocks.

Before and after, over every blob that carried any finding (843 blobs, both gates run on the same files):

| | findings | BLOCK | DIRECT_IDENTIFIER |
|---|---|---|---|
| before | 2 907 | 1 213 | 208 |
| after | 2 892 | 1 198 | 193 |
| removed | 15 in 6 blobs | 15 | 15 |
| added | 0 | 0 | 0 |

The 15 removed are exactly the UUID sub-types of section 5 (DailyMed set-id 2, Signature Commons entity ids 12, a session directory name 1). Nothing classified as personal data, linkage, public data or detector text changed. The 7 remaining false positives (2 short digests, 4 SSH remotes, 1 phrase) are not UUID-shaped and are left alone: widening the rule to them would narrow the digest carve-out, which `public_release_gate.py` records as deliberately not lowered.

Tests (`scripts/test_public_release_gate.py::test_identifier_inside_a_canonical_uuid_does_not_block_but_beside_one_it_does`): positive (token inside the first group, a middle group, upper case); mutations that must still block (token after a space; token glued after a UUID with a hyphen; token glued before it; between two UUIDs; a first group of 5 hex; a last group of 11 hex; a UUID containing the token plus the token again outside; a real identifier beside a clean UUID; a real identifier beside a UUID that contains the token). The test fails on the unchanged gate and passes on the new one; all 59 gate tests pass.

The isolated scanner was not changed (the two stay independent on purpose); at the tip it flags no UUID-contained token, so the two do not diverge on any tracked file today.

## 10. Options for the operator (decision reserved)

Facts that bound the options: the exposure is public and small in kind (operator name tokens, third-party author addresses, one pairing sentence); the earliest affected commit is `ca506034` for the addresses (3 827 commits before the served tip), `5d3571ad` for the paths (about 3 754), `ec4bf603` for the record (about 3 421) and `f878cc54` for the pairing sentence (about 407); the served history is about 3 893 commits. A rewrite that removes the paths or the addresses therefore changes about 96 % of all commit hashes. The remote has no forks, stars or pull requests, so a forced replacement would collide with few visible third parties, but clones and caches are unobservable.

| option | what it does | impact | restore path |
|---|---|---|---|
| J. Record and keep | this file plus the local directory as the dated register; no change to history | none; exposure stays | trivial |
| K. Close the tip's blind spot | extend the gate to HTML and gzip text (renamed-by-content as in `gap-scan`), accepting the UUID rule and a UNII and block-scope carve-out; no history action | forward protection only; a new gate run on the tip would first need the false positives of section 8 handled | revert the gate commit |
| E1. Narrow rewrite, text only | `git filter-repo --replace-text` on the operator's name tokens, the 262 addresses and the pairing sentence; history shape kept | removes the findings above from every revision; about 96 % of hashes change; seals that cite short SHAs and the read-receipt records must be re-anchored (IT7 section 7, E) | pre-rewrite bundle of all refs, including the VPS backup, taken first; old objects survive in other clones |
| F. Private switch | hides the repository from new readers | stops new reads; does not retract clones; may cost the project's public aim | switch back; behaviour of caches and forks on a switch is unread here |
| H. Orphan or squashed public history with a private archive | publishes a clean tip as the only public history | no old SHAs in public; every SHA citation in tracked text must be mapped | the archive; old public history survives in clones |
| I. Hosting-provider request | asks the host to purge cached views and unreachable objects | the only route to what section 2 lists as unverifiable | none |
| M. Metadata only | a mailmap-style rewrite of commit identities | does not touch blobs; IT7 counts 5 579 hostname fields in 2 790 commits, so it is the larger operation | bundle first |

Impact summary for the decision: options J and K need no authority beyond landing a normal commit; E1, F, H and I are the operator's alone. Whether any of them is warranted depends on a judgement this triage cannot make: whether the operator's own name tokens in paths, public third-party author addresses and one pairing sentence justify rewriting about 96 % of the public history. The scan gives no reason to treat any finding as an urgent exposure of the proband's or family's identity.

## 11. Residual uncertainties

1. The scan covers text blobs the gate or the HTML/gzip pass can read; images (48 PNG in history), PDFs, commit metadata, GitHub-side state and encoded or line-split strings are not covered.
2. The "no proband-name hit" statement rests on the gate's digest tokens (five exact, three casefolded). A name written in a form those digests do not cover (a nickname, a different transliteration, initials) would not be found by either tool. The isolated scanner's glued-name and city checks found nothing of that kind on a sample read at the tip; the history output was classified only by category counts, not read item by item.
3. The class "public or bibliographic" for published-case statements rests on a PMID/PMC/DOI or a per-paper file name on the same line or path (21 blobs); the lines were read once, in masked form, not independently re-derived. A different verifier will re-derive a sample.
4. The reference-class allele pair is named together on 24 tracked lines at the tip by design. No scan can say whether that pair, together with the public identity of the repository owner and the disease, identifies a family to someone who knows them. That judgement, and not any finding above, is the largest open item of this triage. It is reserved to the operator.
5. Distinct-incident counts are upper bounds for rule lines (edited copies count separately) and exact for UUIDs, paths and addresses.
6. "Other refs only" numbers depend on the branches that exist while the tool runs; the segment is local-only and not on the remote.
7. The isolated scanner was run with memoised SHA-256 (same digests). Its history output was compared with the gate at blob level, not read finding by finding.
