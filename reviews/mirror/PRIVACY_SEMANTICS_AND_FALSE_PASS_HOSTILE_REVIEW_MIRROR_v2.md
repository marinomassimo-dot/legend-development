---
artifact: MIRROR hostile review (Annex C.2) — privacy semantics, record scope, false-pass surfaces
review_id: PRIVACY_SEMANTICS_AND_FALSE_PASS_HOSTILE_REVIEW_MIRROR_v2
object: the two privacy scanners as they stand at `57ea7a4`; `regenerate_adjudications.py verify`;
  `run_release_regressions.py` and the CI workflow that calls it; `CAND-20260826-ORCHMAJOR2`;
  the claim registry's cross-reference graph
continues: PRIVACY_GATE_REPAIR_HOSTILE_REVIEW_MIRROR_v1 — extends it, corrects two of its
  attributions, and reports one defect in v1 itself
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-26
verdict: ONE DEFECT CLASS UNDER ALL EIGHT PHASES — a predicate evaluated over a window wider
  than the unit it describes. 11 blocking findings, 4 of them new channels not in v1.
personal_data: none reproduced. The human role is **Operator** throughout. Every path form
  whose terminator is NOT in the shipped accepted set is written `/Users/⟨op⟩` — see § 0.2,
  which is the reason and is itself a finding.
scope_note: every figure below was produced by running a command in this session. Where a
  figure is another actor's, I re-derived it and say whether it held.
---

# The count did not move and the set underneath it did, on both gates and in the same direction

---

## 0 · OBSERVATION_SCOPE

### 0.1 · What was measured, and on which tree

| Fact | Value |
|---|---|
| Derivation window | `2026-08-26T08:01:50Z` → `08:38:40Z` |
| My worktree / HEAD | `.claude/worktrees/mirror`, branch `mirror` @ `57ea7a4` — 88 ahead of `main`, 0 behind |
| `main` | `788c357` |
| Trees measured | `git archive HEAD` export (685 files) · `git clone -b mirror` · `git clone -b main` · `git clone -b plan-major2-restricted-repair` |
| Untracked in my worktree | 11 files under `learning/mirror/`, `reviews/mirror/` — **excluded** from every count |
| Python · PyMuPDF | 3.9.6 · 1.26.5 |
| Tracked `.jsonl` | 10 files · 1 137 records · **0 malformed · 0 blank** |

Local NOT_FOUND is not repo-wide NOT_EXIST. Every negative below is scoped to this table.

### 0.2 · The redaction, which is a finding and not a courtesy

v1 spelled out seven path forms — `/Users/⟨op⟩.`, `**/Users/⟨op⟩**`, `/Users/⟨op⟩:` and four
more, each with the token written out — to demonstrate that they escape both scanners. It also
stated that the escapes are *"latent, not live"*. I re-measured that negative and it holds for
the tracked tree: **0 of
the 57 live path occurrences carry a terminator outside the accepted set** (§ 1.3).

Then I scanned v1's own file:

```
reviews/mirror/PRIVACY_GATE_REPAIR_HOSTILE_REVIEW_MIRROR_v1.md
    path-blocking = 3      terminator-escapes = 7
    line 113 after='⏎'  line 131 '.'  line 132 '*'  line 133 ':'
    line 134 '>'        line 137 '?'  line 144 '.'
```

**FINDING 0 — BLOCKING. Committing v1 places seven unblocked operator-identity paths into the
public tracked surface, and falsifies v1's own sentence in the act of publishing it.** The
review that documents the channel becomes the channel. v1 is untracked today, so the exposure
is not live; the moment it is committed it is. This review therefore writes every
non-accepted-terminator form as `/Users/⟨op⟩` and every Italian slash-pair as `⟨it⟩/⟨op⟩`. The
demonstrations lose nothing — they are executable in the session harness — and this file does
not become the first live instance of what it reports.

**My own draft, re-scanned rather than predicted — and the first scan falsified what this
section said.** I had written that the draft was clean before running the scan. It was not:

| finding in my draft | first scan | at commit |
|---|---|---|
| **3 terminator escapes** at one line — v1's forms, quoted verbatim in the paragraph above | 3 | **0** — redacted |
| **1 live third-party email address**, a published researcher's, reproduced in § 3.5 | 1 | **0** — redacted |
| 2 synthetic fixture addresses on a non-placeholder domain | 2 | **0** — mechanism stated, address not written |
| **1 `BROKEN_MARKDOWN_LINK`** — visible only when scanned *in the tree*, not in isolation | 1 | **0** — rephrased |
| 3 `PARENT_OF_ORIGIN_PAIRING` | 3 | **0** — `⟨MAT⟩` / `⟨PAT⟩`, see below |
| `ITALIAN_CITY` / `ITALIAN_HOSPITAL` on author given names | 11 | **11** — kept, see below |

I reproduced the exact defect I was reporting, one paragraph after describing it, and only the
scan caught it. Then I predicted the residual cost instead of measuring it, and was wrong twice
— the broken link appears only when the file is scanned inside the tree, and the homonym count
was 11, not the 6 the isolated scan showed. Both are the finding, not asides: a redaction policy
that is stated and not executed reads identically to one that is executed, and a file scanned
alone is not the same population as the same file scanned in its tree.

**`⟨MAT⟩` and `⟨PAT⟩`** stand for the two parent-side **vocabularies** the release gate defines
at module level — each a set of English and Italian forms, not a single word. Written as
placeholders throughout § 2, for the same reason as `⟨op⟩`, and *this paragraph names neither
vocabulary either*: writing both names in one paragraph re-fires the very rule § 2.3 is about,
which is how I found that out. Nothing in the finding depends on the literal strings — § 2.3 is
about *which records* carry a member of each set, and the placeholder states that more precisely
than one word would.

**The scanner was not touched to achieve this.** The redaction removes tokens from the published
surface; it does not add an attribution, invoke the negation escape hatch of § 2.3, or split a
paragraph to slip under a block boundary. Any of those would have been gaming the predicate this
review is auditing.

**What this document costs at commit, measured on the export with both files added.**

```
release gate    BLOCKS   301 → 301    (+0)
independent   BLOCKING   683 → 695    (+12, every one of them ITALIAN_CITY / ITALIAN_HOSPITAL
                                        on the six author name strings of § 3.1(c))
```

The remaining 12 are **kept deliberately and are not an exposure.** They are six published
authors' given names and initials — `Florence`, `Ao`, `AO`, `Napoli`, `Meyer` — and they are the
*subject* of § 3.1(c), which reports that a privacy gate blocks publication because an author is
named Florence. Redacting them would concede that a false positive is a true one. They are a gate
finding, not personal data: the distinction is the point of the section, and it is why the two
rows above are treated differently.

---

## 1 · PHASE 1 — the semantic model, derived rather than assembled

### 1.1 · The classes, and what actually delimits each

The shipped rule asks a one-character question: is the char before the match `/`, and is the
char after it a member of a 12-character set. Both halves are properties of neither the token
nor the path.

**A path segment is, by POSIX, any byte sequence excluding `/` and NUL.** Nothing else
terminates it. Every other member of `PATH_SEGMENT_AFTER` is a property of the *host syntax*
that quotes the path — markdown, JSON, shell, prose — not of the path. A terminator list is
therefore enumerating the complement of an open set, and cannot be completed. That is why the
set was assembled: there was nothing to derive it from.

| Class | What actually bounds it | Shipped rule's premise | Verdict |
|---|---|---|---|
| `TEXT_TOKEN` | word boundaries; the token may be a homonym | correct — lowercase must not block in prose | **sound** |
| `PATH_SEGMENT` | `/` on the left; `/` or end-of-path on the right | approximated by a 12-char list | **unsound, incomplete by construction** |
| `PATH_EMBEDDED_IN_PROSE` | the *host* punctuation, unbounded | not modelled | **11 forms escape** |
| `JSON_STRING_PATH` | JSON string escapes (`\\`, `\/`, `\uXXXX`) precede the path grammar | not modelled | **2 forms escape** |
| `JSONL_RECORD` | the newline **is** the record boundary | `.jsonl` inherits `.md` block rules | **§ 2, blocking** |
| `MULTILINE_PATH` | `\n` ends the path | `\n` ∉ `PATH_SEGMENT_AFTER` in the release gate; the independent scanner splits lines first | **scanner divergence** |
| `SYSTEM_OUTPUT_PATH` | `~`, `-`, whitespace-column separators | only `/` is a left delimiter | **3 forms escape** |
| `HASH_OR_SIGIL` | a ≥32-char hex run | correctly excluded | **sound, and it works** |

### 1.2 · The battery: 39 cases, both scanners, one command

| outcome | n | examples |
|---|---:|---|
| correct | 17 | `/Users/⟨op⟩/x`, a backtick-quoted path, a markdown link target, `,`, prose homonym in both cases, inside a SHA-256 |
| **FALSE NEGATIVE** | 18 | sentence period · markdown bold · `<…>` · `?` · `!` · em-dash · `:` · URL query · URL fragment · `}` · `</p>` · `~⟨op⟩/` · `MacBook-Air-di-⟨op⟩` · `AIR-DI-⟨OP⟩` · `C:\Users\⟨op⟩\` · JSON `\\` · JSON `\uXXXX` · a token glued to ≥18 letters |
| **FALSE POSITIVE** | 2 | `⟨it⟩/⟨op⟩` in `.md` and in `.jsonl` — v1's finding, reproduced |
| **SCANNER DIVERGENCE** | 2 | a path at end-of-line mid-file: independent BLOCKS, release gate is silent |

### 1.3 · The derivation, from the live population

86 case-insensitive occurrences of the token as a standalone alphabetic run:

```
in_path_context TRUE  : 57      preceding char: '/'  57   (root prefix: /Users/  57 of 57)
in_path_context FALSE : 29      preceding char: ' ' 19 · '-' 9 · '"' 1
following char        : '/' 58 · ' ' 16 · '`' 4 · <EOL> 3 · '.' 2 · '"' 1 · '-' 2
occurrences preceded by '/' whose follower is NOT accepted:  0
```

**The left side is closed (57 of 57 are `/Users/`); the right side is not.** So the
discriminator the rule needs is the **prefix**, which is enumerable, and not the terminator,
which is not.

Case forms: `⟨op⟩` 80 · `⟨OP⟩` 5 · `⟨Op⟩` 1. Digest membership, measured:

| form | exact ∈ PRIVATE | casefold ∈ GENERAL | casefold ∈ PATH |
|---|---|---|---|
| `⟨op⟩` | no | no | **yes** |
| `⟨Op⟩` | **yes** | no | yes |
| `⟨OP⟩` | no | no | **yes** |

**CORRECTION to v1 § 7.** v1 attributes the uppercase gap to *"uppercase has no reachable
digest"*. Measured: `/Users/⟨OP⟩/x` **BLOCKS in both scanners**, as do the title and mixed
forms. The uppercase gap is a **prose** gap only. The five live `-⟨OP⟩` hostname occurrences
escape because their left delimiter is `-`, not because of case. v1's § 9 gives that as the
second of two reasons; it is the only one.

### 1.4 · FINDING 1 — BLOCKING — a single adjacent character defeats the digest

The detector hashes the **whole maximal alphabetic run**. Anything glued to the token changes
the run, so the digest never matches:

| form | release gate | independent |
|---|---|---|
| `/Users/⟨op⟩/x` | BLOCK | BLOCK |
| `/Users/⟨op⟩2/y` | **silent** | **silent** |
| `/Users/⟨op⟩-1/y` | **silent** | **silent** |
| `/Users/⟨op⟩.old/y` | **silent** | **silent** |
| `/Users/⟨op⟩x/y` | **silent** | **silent** |

`⟨op⟩2` and `⟨op⟩-1` are what macOS produces when an account is duplicated. `⟨op⟩.old` is what
a backup produces. The independent scanner's `GLUED_NAME_CANDIDATE` detector exists precisely
for this class — and it is built from the **capitalised** full names, case-sensitively, so it
catches `⟨Op⟩x` and never `⟨op⟩2`.

### 1.5 · FINDING 2 — BLOCKING — the two scanners diverge in three classes, in both directions

They were kept independent on purpose. Nobody has ever measured their agreement.

| class | release gate | independent | live population |
|---|---|---|---|
| path at end of a line mid-file | **silent** | BLOCK | 0 today |
| email followed by a period | BLOCK | **silent** | **336 live** |
| capitalised name glued to a letter | **silent** | BLOCK | 0 today |

The middle row is the one that matters. The independent regex ends `(?![\w.-])`, which rejects
a match whose next character is `.`. PubMed writes corresponding addresses as
`Electronic address: ⟨local⟩@⟨host⟩.⟨tld⟩.` — **336 of the 430 emails in the corpus seed are
followed by a period.** The second-opinion scanner sees 94 of 430 in the file that carries 87 %
of the blocking population, and reports a smaller number without reporting that it is looking at
a different set.

Measured on a synthetic address (built in the session harness, not written here, because writing
a matchable address into this file would put a live `EMAIL_ADDRESS` block in it): trailing `.`
→ gate 1, independent 0. Trailing `,` `;` `)` `"` or end-of-line → 1 and 1 in every case. So the
divergence is exactly the sentence-final form, and that is the form PubMed emits.

Both scanners are silent when the address is followed by `-x`.

### 1.6 · The repair, prototyped and measured rather than proposed

Root-anchored, sub-run tokenised. No mega-regex; the tokenisation is the verifiable part.

```
1. find every PATH_ROOT prefix          — closed set: /Users/ /home/ /var/folders/ ~/ [A-Z]:\Users\
2. take the maximal following run of non-whitespace, non-quote characters
3. split that run on the separators  /  \
4. hash every alphabetic sub-run of length ≥3 against the PATH digest set
   (the ≥32-char hex-run skip is retained unchanged)
```

Measured side by side with the shipped predicate:

| | 26-fixture battery | live tracked tree |
|---|---|---|
| shipped rule | **17 FN · 1 FP** | 57 hits in 33 files |
| derived rule | **0 FN · 0 FP** | **59 hits in 33 files — a strict superset** |

The false positive closes **structurally**: `⟨it⟩/⟨op⟩` has no path root, so no special case is
needed and none is written. `/Users/⟨op⟩x/y` stays silent because `⟨op⟩x` is a different
segment; `/Users/⟨op⟩2/y` blocks because `⟨op⟩` is a sub-run of `⟨op⟩2`.

The two new live hits are both at `launch/KERNEL_SPEC.md:42`, offsets 58 and 66:

```
moves inside the existing base (`~/.legend/lineage/AIR-DI-⟨OP⟩-⟨op⟩/` →
```

That is the single instance v1 § 9 called the sharpest, found there by eye. The derived rule
reaches it **by mechanism**, in both case forms, through the `~/` root, without adding a digest
and without touching the prose homonym. A rule that independently rediscovers the exposure a
human had to hunt for is the argument for the rule.

---

## 2 · PHASE 2 — JSONL RECORD SCOPE. The priority, and the sharpest finding of the session

### 2.1 · The measurement that settles the scope question

**Every one of the 10 tracked `.jsonl` files yields exactly ONE semantic block.** 1 137 records
→ 10 blocks. Zero blank lines, zero malformed records. So for `.jsonl`, `BLOCK_SCOPE ≡ FILE_SCOPE`
is not a risk, it is an identity.

The control that isolates the extension from the content: identical content, once as `.jsonl`
and once as `.md` with the records paragraph-separated, through the **real** gate.

| fixture | truth | as `.jsonl` | as `.md` | RECORD scope |
|---|---|---|---|---|
| **F1** variant A in paper 1, variant B in paper 2, linkage phrase in paper 3 | silent | **BLOCK** | silent | silent |
| **F2** all three in one record | BLOCK | BLOCK | BLOCK | **BLOCK** |
| **F3** ⟨MAT⟩ in paper 1, ⟨PAT⟩ in paper 3 | silent | **REVIEW** | silent | silent |
| **F6** two adjacent unrelated records | silent | **BLOCK** | silent | silent |
| **F7** explicit cross-record reassembly | BLOCK | BLOCK | — | **BLOCK** |
| **F8** implicit cross-record reassembly | BLOCK | BLOCK | — | **BLOCK** |

**JSONL_CORRECT_SCOPE_VERDICT = RECORD, with the reassembly rule kept at file scope.**

The prototype changes two functions and nothing else — `semantic_blocks` yields one record per
line for `.jsonl`, and `attribution_window` returns the record. Every character-window rule
(`cross_paragraph_pairing` ±2200/500, `parent_origin` ±350, `person_context` ±700) is untouched,
which is why F7 and F8 still block: the cross-block detector is file-scoped *by construction*
and does not depend on `semantic_blocks` at all.

Scored against the brief's four properties:

| | FILE (today) | LINE | **RECORD** |
|---|---|---|---|
| PRIVACY (F2, F7, F8 caught) | yes | F7/F8 lost | **yes** |
| PROVENANCE (the `pmid` that attributes the record is in the window) | no — 706 papers in one window | no — a record is a line, so identical | **yes** |
| LOW FALSE POSITIVE (F1, F3, F6 silent) | **no** | yes | **yes** |
| DETERMINISTIC LOCATOR | **no** — § 2.3 | partial | **yes** |

`LINE` and `RECORD` are the same partition of this corpus today (0 malformed, 0 blank). They
differ only in what they do with a record that does not parse, which is § 2.5.

### 2.2 · FINDING 3 — BLOCKING — the count did not move and the set underneath it did

Prototype over the whole tracked tree:

```
TODAY        total=494  BLOCK=489  REVIEW=5
RECORD_SCOPE total=494  BLOCK=489  REVIEW=5
```

Identical totals. Anyone comparing numbers concludes the repair is a no-op. The set:

| | today | record scope |
|---|---|---|
| `corpus_seed_pubmed_20260806.jsonl:273` | REVIEW | **gone** |
| `fulltext_read_receipts.jsonl:83` | **absent** | REVIEW |

One false REVIEW leaves; one **suppressed** REVIEW arrives. 5 = 5, and neither of them is the
same finding. Two counts that agree verify nothing when the set underneath was never compared.

The corpus-seed REVIEW is 100 % false, and now provably so rather than by inspection:
**5 records carry a ⟨MAT⟩ word, 1 carries a ⟨PAT⟩ word, and 0 records carry both.** There
is no pairing anywhere in that file. The reviewer sent to line 273 is sent to a record that
contains half of a finding that does not exist.

### 2.3 · FINDING 4 — BLOCKING — the privacy escape hatch is file-wide on `.jsonl`, and it fires today

`fulltext_read_receipts.jsonl`, 128 records, 564 KB:

| | records |
|---|---|
| ⟨MAT⟩ word | 82, 83, 104 |
| ⟨PAT⟩ word | 83, 104 |
| **both** | **83, 104** |
| `parent_origin_is_explicitly_negated` TRUE at record scope | **104 only** |
| `parent_origin_is_explicitly_negated` TRUE at FILE scope | **TRUE** |

Record 104 negates itself and is correctly suppressed. Record 83 does not — and at file scope
**record 104's negation suppresses record 83**, 21 records away, in a different paper. Record
83 in isolation → `REVIEW PARENT_OF_ORIGIN_ATTRIBUTED`. In the file → nothing.

The gate's own comment says *"a suppression is REPORTED, not silent. A privacy exemption nobody
can see in the output is the one that stops being reviewed."* This one is invisible.

**And the span that does the suppressing is not a sentence.** The single file-wide match is:

```
'without being treated as one.", "AND THE FATHER\'S'
```

`without` ends `evidence_basis[3]`; `THE FATHER'S` begins `evidence_basis[4]`. The 45 characters
the negation regex allows between subject and marker are spent on `being treated as one.", "` —
**the closing quote, the comma and the opening quote of the next JSON array element.** No human
wrote that phrase. JSON serialisation did.

Falsified rather than narrated — one mutation, one word, on a pristine copy:

| mutation | total | parent-of-origin findings |
|---|---:|---|
| control (unmutated HEAD) | 494 | corpus_seed:273 REVIEW, + 3 elsewhere |
| **M1 — `without` → `lacking` in record 104, nothing else** | **495** | **+ `fulltext_read_receipts.jsonl:82` BLOCK** |
| **M2 — record 104 deleted** | **495** | **+ `fulltext_read_receipts.jsonl:82` BLOCK** |
| M3 — record 83 alone | — | REVIEW at line 1 |
| M5 — record 104 alone | — | SILENT |

Note the severity and the locator. At file scope the finding is a **BLOCK at line 82** —
because `reference_present` is also computed over all 128 records, so the `else` branch is
taken — and line 82 is a record with a ⟨MAT⟩ word and no pairing. At record scope it is a
**REVIEW at line 83**, the record that actually pairs. Four defects composing: file-wide block,
file-wide negation, file-wide `reference_present`, wrong locator.

### 2.4 · FINDING 5 — BLOCKING — deduplication hides 39 % of the blocking population, all of it on `.jsonl`

`deduplicate()` keys on `(severity, code, path, line, message)`. A `.jsonl` record **is** a
line, so N findings in one record collapse to one.

```
raw findings        496   raw BLOCK 491
after deduplicate   306       BLOCK 301   <- the number a human is shown
collapsed away      190 blocking findings
```

| hidden | code | file |
|---:|---|---|
| **185** | `EMAIL_ADDRESS` | `corpus_seed_pubmed_20260806.jsonl` |
| 4 | `DIRECT_IDENTIFIER` | `framework/state/sync_epochs.jsonl` |
| 1 | `DIRECT_IDENTIFIER` | `fulltext_read_receipts.jsonl` |

The worst single record hides **13 email addresses behind one reported finding**. The
extension the repair admitted to the gate was admitted without the locator granularity that
extension requires: on `.md` the locator is a line of prose, on `.jsonl` it is an entire
bibliographic record. Any record-scope repair must add a record-internal component — the JSON
field path — or the reported count remains a count of *records touched*, not of findings.

### 2.5 · Malformed records: the gate cannot fail closed because it never parses

`scan_privacy_and_secrets` treats `.jsonl` as plain text end to end. There is no parse, so
there is no parse failure, so "fail closed on a malformed record" is not a behaviour that can
be observed today — and **0 of 1 137 tracked records are malformed**, so no fixture in the tree
would exercise it. F5 (a truncated record between two clean ones) is SILENT at every scope.

This is a specification gap, not a defect: any record-scope implementation must *choose*, and
the choice must be written before it is relied on. The repair specification below makes it
explicit and makes fail-closed the default, because a record that cannot be parsed is a record
whose privacy content cannot be bounded.

### 2.6 · PRIVACY_SEMANTICS_REPAIR_SPEC

Not applied. Both scanners are unmodified in this tree.

| # | Change | Scope | Evidence | Verdict-neutral today? |
|---|---|---|---|---|
| R1 | Replace `in_path_context` with the root-anchored sub-run rule of § 1.6 | both scanners | § 1.6: 0 FN / 0 FP on 26 fixtures; live 57 → 59 | **no** — +2 real findings |
| R2 | `semantic_blocks` yields one record per line for `.jsonl`; `attribution_window` returns the record | release gate | § 2.1–2.3 | **totals yes, set no** — § 2.2 |
| R3 | Keep `cross_paragraph_pairing` file-scoped and say so in the code | release gate | F7/F8 still block under R2 | yes |
| R4 | A record that does not parse as JSON is a finding (`UNPARSEABLE_RECORD`, BLOCK), not a silence | release gate | § 2.5 — unexercised by the tree | yes, 0 live records |
| R5 | Extend the dedup key with the JSON field path for `.jsonl` | release gate | § 2.4 — 190 hidden | **no** — 301 → 491 shown |
| R6 | Add a differential regression: the two scanners must agree on a shared fixture corpus | both suites | § 1.5 — 3 divergence classes, 336 live | yes |
| R7 | Anchor `NG[-\d]{5,}` on a left word boundary | release gate | § 3.5 — 6 live false hits | **no** — removes 1 BLOCK |
| R8 | Fix the `else`-branch message so it names the condition that fired | release gate | v1 § 6, re-confirmed | yes |

R1, R2, R5 and R7 change verdicts and are the Operator's. R3, R4, R6, R8 change no verdict
today, which is the only safe moment to install them.

---

## 3 · PHASE 3 — PUBLIC_BIBLIOGRAPHY_DECISION_PACKET

### 3.1 · The population, attributed to a field path rather than a line

`corpus_seed_pubmed_20260806.jsonl`, 706 records, 20 top-level keys, every record parses.

| class | n | field path | share in that path |
|---|---:|---|---|
| `PUBLIC_CONTACT_EMAIL` | **430** | `.authors[].affiliations[]` | **430 of 430** |
| `INSTITUTION` (city) | 357 | `.authors[].affiliations[]` | 348 of 357 |
| `INSTITUTION` (hospital) | 142 | `.authors[].affiliations[]` | 137 of 142 |
| `ORCID_IF_PRESENT` | **480** | `.authors[].identifiers.ORCID` | 480 of 480 |
| `CALENDAR_DATE` | 17 | `.identifiers.pii` / `.doi` / `.elocation[]` | 16 of 17 |
| `AUTHOR_NAME` | — | `.authors[].fore_name` / `.last_name` / `.initials` | — |
| `CORRESPONDING_AUTHOR_FIELD` | **0** | — | **the field does not exist** |

Three facts the Operator's decision has to carry, none of which is in v1's packet:

**(a) `CORRESPONDING_AUTHOR_FIELD` is not a separable class in this data.** There is no such
key. Correspondence is a free-text substring inside the affiliation string. So "restrict the
contact field" cannot be implemented as a field rule; it is a substring rule inside a field
that must be kept for provenance.

**(b) 480 ORCIDs are present and BOTH scanners are silent on ORCID.** Measured directly:
`0000-0002-1825-0097` in a `.jsonl` → release gate SILENT, independent SILENT. An ORCID is a
permanent, globally unique, resolvable person identifier. An academic email decays; an ORCID
does not. The gate blocks 430 of the weaker identifier and misses 480 of the stronger one.

**(c) 12 blocking findings are on a person's actual name, mistaken for a place or a hospital:**

| n | field | value |
|---:|---|---|
| 6 | `.authors[].fore_name` | `Florence` — in `ITALIAN_CITIES` |
| 2 | `.authors[].fore_name` | `Ao` — matched by `\bAO\b`, IGNORECASE |
| 2 | `.authors[].initials` | `AO` |
| 1 | `.authors[].last_name` | `Napoli` |
| 1 | `.authors[].last_name` | `Meyer` — a children's hospital and a common surname |

A privacy gate blocking publication because an author is named Florence is the false-positive
class in its purest form, and it is inside the population the decision is about.

### 3.2 · The residual under each option, on the number a human is actually shown

`public_release_gate.py` today: **`VERDICT: BLOCK_PUBLICATION`, `BLOCKS: 301`**.

| | **A** block every person identifier | **B** exempt structured bibliographic metadata | **C** names/institutions permitted, contact restricted | **D** strip the email substring from `.affiliations[]` |
|---|---|---|---|---|
| **release-gate BLOCKS remaining** | **301** | **55** | **300** | **56** |
| independent scanner blocking | 683 | 71 | 165 | 589 |
| data removed | none | none | none | 430 email substrings |
| data exempted | none | the whole `.authors[]` subtree | `.authors[]` except emails | none |
| scientific provenance impact | none (nothing removed) | none | none | none — recoverable from PubMed by PMID |
| privacy impact | lowest | affiliations + 430 emails + 480 ORCIDs ship | 430 emails + 480 ORCIDs ship | emails gone; 480 ORCIDs still ship |
| implementation complexity | none (status quo) | **highest** — needs a trusted structural predicate, i.e. a schema contract | moderate — a field-path denylist | low — one field, one regex, one regeneration |
| risk of a permanently-red gate | **certain** | none | **certain — 300 of 301 remain** | none |

**The decisive number is the 300.** Option C — the middle path v1 laid out — moves the
authoritative gate by **one block**, because 245 of the corpus seed's 246 human-visible blocks
*are* the emails. C is a large win on the independent scanner (683 → 165) and a rounding error
on the tool that decides publication. The two tools barely share a population: the gate's 301 is
82 % email; the independent scanner's 683 is 74 % cities and hospitals, which the gate does not
detect at all.

So the decision is closer to binary than v1's three columns suggest: **do the 430 published
corresponding-author addresses ship, or not.** Everything else is noise on the gate.

**I do not choose.** Two further facts belong with the choice: under every option the single
`PUBLIC_BIBLIOGRAPHIC_AUTHOR` hit (`.authors[].fore_name = ⟨Op⟩`, a published author sharing
the Operator's given name) is reported as *"Legacy personal identifier remains in public
material"* — the wording misattributes under A, B, C and D alike; and no option touches the 480
ORCIDs, which no rule currently sees.

### 3.3 · FINDING 6 — BLOCKING — the gate's headline privacy contradiction is a fragment of a Gmail address

```
[BLOCK] README_PRIVACY_CONTRADICTION README.md:1
        — Repository claims no patient is referenced, but case-linkage markers remain.
```

The rule concatenates **every text file in the repository into one string**, then asks whether a
"no patient referenced" claim exists anywhere and a patient marker exists anywhere. The claim is
in six unrelated policy files. The marker is:

| file | occurrences | matched text | actual context |
|---|---:|---|---|
| `corpus_seed_pubmed_20260806.jsonl` | 6 | `ng13827` | the tail of a published author's Gmail local part, `…ng13827@…` — the address itself is not reproduced here |

`NG[-\d]{5,}` has no left word boundary, so it matches inside an email local part. The most
alarming sentence the gate can print is fired by six occurrences of a published Taiwanese
researcher's Gmail address. **100 % false positive**, and — verified by the 2×2 in § 7.4 — this
BLOCK did not exist before `.jsonl` was admitted to `TEXT_SUFFIXES`: the repair created it.

Concatenation itself created no markers here (per-file 6, concatenated 6), so the cross-file
channel is latent rather than live. It is the same defect as § 2 one level up: a predicate
evaluated over a window wider than the unit it describes — here the window is the whole
repository.

---

## 4 · PHASE 4 — NON_PATH_IDENTITY_DECISION_PACKET

29 non-path occurrences. v1's figure of 16 uncovered is **confirmed**.

| # | Class | n | Surface | Reachable by a gate? | Removal consequence |
|---|---|---:|---|---|---|
| 1 | `EVIDENTIARY_QUOTE` / `MACHINE_HOSTNAME` | 11 | `launch/KERNEL_SPEC.md` ×6, `framework/eval/learned_gates_registry.md` ×3, others ×2 | **no** (left delimiter `-`) | **DESTROYS_EVIDENCE** — the four machine names *are* the measurement that justifies `DERIVED_IDENTITY_IS_NOT_IDENTITY` |
| 2 | `SYSTEM_USERNAME` | 5 | `framework/protocols/actor_identity_feasibility.md:146-150`, captured `lsof` output | **no** (whitespace column) | **CAN_BE_STRUCTURALLY_REDACTED** — the column position carries the argument, the string does not |
| 3 | `COMMON_WORD_HOMONYM` | 12 | Italian prose ×10, test fixtures ×2 | correctly silent, by design | **IS_NOT_NEEDED** — nothing to remove |
| 4 | `PUBLIC_BIBLIOGRAPHIC_AUTHOR` | 1 | `corpus_seed…jsonl:685` `.authors[].fore_name` | blocked, **mislabelled** | **MUST_REMAIN_TO_REPRODUCE** — it is a published author's name |

Under the derived rule of § 1.6, class 1 partially moves: the two `KERNEL_SPEC.md:42`
occurrences inside `~/.legend/lineage/…` become reachable (they sit under a `~/` root), while
the bare `MacBook-Air-di-⟨op⟩` prose forms stay outside any path and remain unreachable. So
**the derived rule reduces the uncovered set from 16 to 14 without any new policy.**

### 4.1 · The policy distinction, drawn and not selected

The brief asks for a distinction between *identity as the subject of the datum* and *identity
incidentally present in the evidence of a system measurement*. The two are separable
mechanically, by a property the repository already has:

| | `IDENTITY_AS_SUBJECT` | `IDENTITY_AS_MEASUREMENT_ARTEFACT` |
|---|---|---|
| test | remove the identifier — does a claim lose its referent? | remove the identifier — does a *measurement* lose its reproducibility? |
| example | a path naming whose machine produced a file | `AIR-DI-⟨OP⟩-⟨op⟩` as the observed output of the lineage-naming rule |
| correct treatment | redact or pseudonymise | **pseudonymise the token, preserve the shape** — `AIR-DI-⟨HOST⟩-⟨USER⟩` keeps the derivation visible |
| what the repository loses | nothing | nothing, **if the shape is preserved** |

Under this distinction, classes 1 and 2 are `IDENTITY_AS_MEASUREMENT_ARTEFACT` and are
`CAN_BE_PSEUDONYMIZED` rather than `DESTROYS_EVIDENCE` — provided the pseudonym preserves the
*structure* that made the observation meaningful (two derived tokens, one hostname-derived and
one username-derived, inside a single path segment). Class 4 is `IDENTITY_AS_SUBJECT` of a
*published* datum and is out of scope for redaction entirely.

**I do not select.** The unresolved question is the one v1 named and it is unchanged: the
repository's declared privacy boundary is the individual-level clinical record, not the
Operator, yet the system's own digest set lists the Operator's token beside the proband tokens.
Until that is settled, "uncovered" is not the same as "should be covered".

---

## 5 · PHASE 5 — ADJUDICATION HOSTILE MATRIX, derived independently

Green baseline re-derived in this session on a clean clone with the three source PDFs staged:
**exit 0, 27 artifacts, 47 locators** — reconciling with the recipes (9+7+11 = 27, 10+29+8 = 47)
and with the canonical transcriptions (`state_manifest_current.md` 18+37, `full_text_queue_current.md`
9+10). Each mutation applied to a pristine copy of that tree.

**ADJUDICATION_HOSTILE_STATE_COUNT = 21** · fail-open **15** · **ADJUDICATION_FALSE_PASS_COUNT = 8**

| mutation | exit | artifacts | locators | verdict |
|---|---:|---:|---:|---|
| A1 all recipes deleted | 0 | 0 | 0 | fail-open, counts differ |
| A2 directory renamed | 0 | 0 | 0 | fail-open, counts differ |
| **A3 one artifact's digest removed** | **0** | **27** | **47** | **INDISTINGUISHABLE** |
| **A4 all 7 digests of one recipe removed** | **0** | **27** | **47** | **INDISTINGUISHABLE** |
| **A5 manifest path misspelled** | **0** | **27** | **47** | **INDISTINGUISHABLE** |
| **A6 manifest key dropped** | **0** | **27** | **47** | **INDISTINGUISHABLE** |
| A7 `artifacts: []` | 0 | 20 | 18 | fail-open, counts differ |
| A8 `adjudicates: []` | 0 | 27 | 18 | fail-open, counts differ |
| **A9 png corrupted on disk after `write`** | **0** | **27** | **47** | **INDISTINGUISHABLE** |
| **N1 partial digest set — 6 of 11 removed** | **0** | **27** | **47** | **INDISTINGUISHABLE** |
| N2 manifest present but not valid JSON | 1 | — | — | failed — **uncaught traceback** |
| N3 manifest without `verbatim_locators` | 1 | — | — | failed — **uncaught `KeyError`** |
| N4 duplicate locators, ×3 | 0 | 27 | **51** | fail-open, count **inflated** |
| **N5 orphan `.png` on disk** | **0** | **27** | **47** | **INDISTINGUISHABLE** |
| **N6 orphan recipe directory, no json** | **0** | **27** | **47** | **INDISTINGUISHABLE** |
| N7 PyMuPDF absent | 2 | — | — | failed, clean message |
| N8 recipe shrunk to 3 of 9 artifacts | 0 | 21 | 43 | fail-open, counts differ |
| N9 `--pmid` names nothing | 0 | 0 | 0 | fail-open, counts differ |
| N10 dpi + 1 *(positive control)* | 1 | — | — | **correctly failed** |
| N11 source-PDF digest wrong *(positive control)* | 1 | — | — | **correctly failed** |
| N12 needle made ambiguous *(positive control)* | 1 | — | — | **correctly failed** |

**Can an incomplete run produce output indistinguishable from a fully verified one? Yes, in 8
of 21 probed states** — identical exit code, identical artifact count, identical locator count.

**Two refinements of v1 § 10.** v1 reports 9/9 fail-open; all nine reproduce. But four of them
(A1, A2, A7, A8) *change the counts*, so a downstream actor who compares against the recorded
27/47 would notice. Only A3–A6 and A9 are truly indistinguishable — which makes the transcribed
canonical counts the **only** defence, and § 5.1 shows nothing re-derives them.

Second: v1's framing implies uniform fail-open. It is not. N2 and N3 **fail closed** — but with
an uncaught Python traceback and **exit 1, the same code as a genuine digest mismatch**. Three
outcomes (evidence wrong · tool crashed · dependency missing) map onto two codes, grouped
wrongly.

### 5.1 · Nothing executes this command

- `test_regenerate_adjudications.py` imports the module and `check_needles`; **12 test methods,
  none calls `run()`**. Verified by reading the imports and grepping for `run(`.
- `run_release_regressions.py` lists the test file, never the command.
- `.github/workflows/public-release-gate.yml` does not mention it.
- `CLAUDE.md § 3` does not advertise it.

The only consumers are canonical Markdown files that **transcribe the counts**, in a command
that cannot be re-run from a clean clone because the PDFs are gitignored by design. The numbers
transcribed are exactly the ones a dropped key inflates.

**REGENERATE_ADJUDICATIONS_CROSSCHECK_STATUS = FAIL_OPEN_CONFIRMED, 15 of 21 states,
8 of them false-pass. Measured independently of Plan; Plan's analysis not read.**

---

## 6 · PHASE 6 — RELEASE_RUNNER_COMPLETENESS_FINDINGS

### 6.1 · The runner's verdict today is FAIL, and it is not my disk

| tree | verdict | failing test cases | failing suites |
|---|---|---:|---:|
| my worktree (11 untracked files) | **FAIL** | 10 | 8 |
| **clean `git clone -b mirror`** | **FAIL** | **9** | **8** |
| **clean `git clone -b main`** | **FAIL** | **7** | **6** |

**Disk-population contamination is real and it is exactly one test case.**
`test_documented_commands.py::test_documented_cli_flags_exist` fails in my worktree and passes
in the clean clone. One of the brief's four failure classes, isolated to a single assertion.

### 6.2 · The nine, attributed

| n | class | detail | inherited from `main`? |
|---:|---|---|---|
| **5** | **stale assertions *about* CLAUDE.md** | `test_locator_obligation…` wants `verbatim_locators`; `test_abstract_corpus…` wants `pubmed_corpus_harvest`; `test_fulltext_trace_contract` ×2 want `FULLTEXT_READ_RECEIPT` and `state-control`; `test_session_self_eval` wants `session_self_evaluation.md` | **yes** |
| 1 | executable bit | 4 shebang entrypoints without `+x`: `framework/scripts/lease_state.py`, `governance/scripts/candidate_content_hash.py`, `governance/scripts/governance_fingerprint.py`, `governance/scripts/test_candidate_content_hash.py` | **yes** |
| 1 | test suite not invoked | `governance/scripts/test_candidate_content_hash.py`, 7 test methods, absent from the inventory | **yes** |
| **2** | **dangling references in this seat's own documents** | 9 references across 7 `reviews/mirror/` and `learning/mirror/` files | **no — mirror introduced them** |

**The CLAUDE.md class is the sharpest, and the brief's phrasing needs inverting.** These are not
stale assertions *in* CLAUDE.md. CLAUDE.md became a router on 2026-08-16 and the operating law
moved to named normative files — deliberately, with a migration map. **Five tests still assert
that the law is in the router.** The migration was correct and the tests that pin the old shape
were never moved with it, so the release verdict has been FAIL since that day and the CI has
been red since that day.

### 6.3 · FINDING 7 — this seat's own review documents are two of the nine failures

Targets are named by **basename only**, with the directory in the third column. Writing them as
inline repository paths would make this table trip the two tests it reports — which it did on the
first draft, and is the same self-reference as FINDING 0.

| file | line | dangling target (basename) | declared directory | exists elsewhere? |
|---|---:|---|---|---|
| `REV-OPCON-PHASE2-MIRROR-001{,-ADD-001,-ADD-002}.md` | 5–6 | `artifact_index.py` | framework/scripts | **yes**, on `12928116` (another branch) |
| `SCIENTIST_CROSS_REVIEW_PILOT_HOSTILE_REVIEW_MIRROR_v1.md` | 742 | `pathograph.py` | framework/scripts | **yes**, on `9a13c49` |
| `REV-OPCONA-MIRROR-001.md` | 82 | `legend_operating_convention_v1.md` | framework/protocols | **yes**, on `12928116` |
| `REV-SCIAB-MIRROR-001.md` | 194 | `deepdive_manifest.py` | cited under scripts; the real one is under framework/scripts | **no** |
| `REV-SCIAB-MIRROR-001.md` | 197 | `PMID42397075.md` | disease-models/wwox/research/fulltext_dossiers | **no** |

Seven of nine are **cross-branch references**: a review of another actor's branch, committed to
`mirror`, cites objects that resolve only in the reviewed tree. That is a structural property of
this seat's work, not a typo, and the two remaining are typos. **I have not repaired them.** A
blanket path rewrite would be wrong for the cross-branch class — the reference is correct
relative to its subject — and rewriting a filed review is not the repository's correction
convention. The exact list is above; the repair is per-case and is the Operator's to assign.

### 6.4 · The false-green complement — what stays green because nothing runs it

A "runner completeness" check over **test files** already exists —
`test_release_runner_verdict.py::EveryTestSuiteIsActuallyRun::test_every_tracked_test_file_is_in_the_runner`
— and it is red on the file I derived independently. It works. It just does not cover
**commands**.

That extension is mechanically definable from two tracked files, with no new governance:
*every command in the fenced block of `CLAUDE.md § 3` must appear in a CI workflow or in the
runner's inventory.* Measured now:

| command advertised in `CLAUDE.md § 3` | in CI | suite only | verdict |
|---|---|---|---|
| `legend_lint.py .` | yes | yes | EXECUTED_IN_CI |
| `fulltext_receipts.py verify` | **no** | yes | SUITE_ONLY |
| `growth_anchors.py check` | **no** | yes | SUITE_ONLY |
| `unread_gold.py --help` | **no** | **no** | **UNCOVERED** |
| `public_release_gate.py` | yes | yes | EXECUTED_IN_CI |
| `run_release_regressions.py` | yes | no | EXECUTED_IN_CI |
| `governance_fingerprint.py compose --all` | **no** | **no** | **UNCOVERED** |

**7 advertised · 3 executed in CI · 2 suite-only · 2 uncovered.** And `SUITE_ONLY` is not
coverage: § 5 shows `test_regenerate_adjudications.py` runs 12 methods without ever calling the
command whose exit code is the gate.

Not advertised and not executed anywhere: `scripts/independent_privacy_scan.py` — the
second-opinion privacy scanner is in no workflow, no inventory and no runbook.

Two further false-green mechanics in the workflow itself:

1. **`Structural framework lint` has no `if: always()`**, while the gate step does. The
   regression step is failing today, so **`legend_lint.py` has not run in CI since the router
   migration.** A red step upstream silently removes a check downstream.
2. **`fetch-depth: 1`.** Any test reasoning about history sees a shallow clone.

And the synthesis: CI is red at `main` and at `mirror`, and has been for ten days. The
repository names this failure mode itself, in its own bibliography decision packet — *a gate
that is always red is a gate nobody reads*. It applies here, to the runner, first.

---

## 7 · PHASE 7 — MAJOR2_REVIEW_STATUS: a candidate exists and it was measured before it was read

`governance/candidates/CAND-20260826-ORCHMAJOR2.md` on `plan-major2-restricted-repair`
@ `a115cbd`, **3 commits ahead of `main`, 0 behind**. Delta-only: 2 files, +377/−5.

**Measured first, per the brief.** The candidate record was opened only after §§ 7.1–7.3.

### 7.1 · The object

```
worktree: the repository root checkout   →   worktree: orchestrator
commit its own work;                     →   commit its own work **to the canonical surface**;
```

### 7.2 · The falsification checklist, executed against the object

| # | Check | Method | Result |
|---|---|---|---|
| 1 | exactly two semantic changes | word-level diff, whitespace normalised | **PASS — 2 hunks**, the reflow adds no third |
| 2 | no wholesale ORCHSURF rev-4 inheritance | file list of the diff | **PASS** — `CAND-20260819-ORCHSURF.md` is absent; 2 files only |
| 3 | `BASE_HEAD` re-derived, not accepted | `git merge-base main <branch>` | **PASS** — `788c357d…`, equals `main` tip, equals the declared value |
| 4 | role-contract hash consistency | `governance_fingerprint.py compose --all` on both trees | **PASS, and contained** — only `orchestrator` moves, `88dea7a6…` → `247b6de9…`; mirror/plan/scientist byte-identical |
| 5 | worktree semantics | `worktree:` field across all role contracts | **PASS** — `mirror: mirror`, `plan: evidence-index`, now `orchestrator: orchestrator`. The old value was the only prose one; the change **normalises** the field |
| 6 | canonical-surface prohibition | diff scope | **PASS** — no canonical scientific file is touched |
| 7 | release gate on the candidate | run it | **PASS · BLOCKS 0**, same as `main` |
| 8 | **authority not widened** | capability set, not prose | **FINDING — see § 7.3** |

### 7.3 · FINDING 8 — the repair narrows a prohibition using a term the governance does not define

Change 2 turns an absolute prohibition into a scoped one. A scoped prohibition is a **widened
capability**: Orchestrator may now commit its own work anywhere that is not "the canonical
surface". Whether that widening is authorised is the Operator's call. Whether it is **bounded**
is mechanical, and it is not:

```
git grep -in "canonical surface"  <branch>  -- governance roles framework
→ the new clause in roles/orchestrator.md
→ the candidate record's own quotations of it
→ two incidental prose uses of "canonical surfaces" in a different sense
→ NO DEFINITION
```

There is no definition of *the canonical surface* anywhere in `governance/`, `roles/` or
`framework/`. The boundary of the newly-permitted capability is therefore prose, and check #7 of
v1's checklist — *"check the classification mechanism, not the label"* — has no mechanism to
check. This is not an objection to the change; it is the missing half of it.

Second, smaller: change 1 moves Orchestrator's worktree off the root, while the same clause
still says *"or treat the root as free working space"*. Both can be true, but the contract no
longer says who occupies the root, and that was previously answered by the field being changed.

### 7.4 · The candidate's own baseline claim, checked — and a 2×2 that corrects v1

The record states: *"`main` at `788c357d`, clean checkout — baseline · `PASS` · `BLOCKS: 0`"*.
**Verified: true.** But `mirror` @ `57ea7a4` is `BLOCK_PUBLICATION · 301`. Two variables differ
between those trees, so neither figure attributes anything on its own. The 2×2, run with the
gate source swapped between clean clones:

| | `main` gate | `mirror` gate |
|---|---|---|
| **`main` tree** | PASS · **0** | BLOCK · **273** |
| **`mirror` tree** | BLOCK · **2** | BLOCK · **301** |

- the **gate change alone** accounts for **273** blocks — the `.jsonl` admission opening the corpus seed;
- the **tree change alone** accounts for **2**;
- **26 more** exist only in the combination.

v1 reports *"2 blocks to 301"*. That "2" is the bottom-left cell and it is **correct**; the
sentence does not say which tree, and the naive reading (main is at 2) is wrong — main is at 0.

The 28 blocks the `mirror` tree contributes under the new gate are **entirely this seat's own
committed documents**: 26 `DIRECT_IDENTIFIER`, 1 `EMAIL_ADDRESS`, 1 `BROKEN_WIKILINK`, every one
in `reviews/mirror/` or `learning/mirror/`, led by `REV-P5DOMAIN-MIRROR-001.md` (4) and
`REV-XPORT-MIRROR-002.md` (3).

**MAJOR2_REVIEW_STATUS = MEASURED, 7 of 8 checks PASS, 1 finding (§ 7.3). Not an approval:
Mirror PASS is a role act and this session holds no dispatch for it.** The measurements above
are the evidence a PASS would rest on; the finding is the one thing that should be answered
first, and it is a governance question, not a code one.

---

## 8 · PHASE 8 — CROSS_CLAIM_CONTRADICTION_CHECK_READINESS

39 claims parsed from `claim_registry_current.md`. Three probes, each measured against the
declared positive fixture (CLAIM 005 ↔ CLAIM 037, mouse epilepsy).

| probe | scope | pairs emitted | **fixture recovered?** |
|---|---|---:|---|
| v1 — (organism, phenotype, polarity) | document | 11 | **NO** |
| v2 — same triple | sentence | 3 | **NO** |
| **v3 — shared axis, link coverage** | sentence, **no polarity** | **9** | **YES — classified RECONCILED** |

**v1 fails because of scope.** Any claim that *discusses* a species discordance carries both
polarities and both organisms at document level, so `polarity` returns "both" and the pair is
dropped. The claims most likely to encode a contradiction are exactly the ones the probe
discards. Same defect class as §§ 1, 2, 3.5 and 6: a predicate over a window wider than its unit.

**v2 fails for a reason narrowing cannot fix.** At sentence scope CLAIM 037 still scores
`(MOUSE, EPILEPSY, +1)` — from the sentence *"gli autori lasciano aperta la spiegazione (i topi
potrebbero morire prima di convulsionare)"*. A polarity detector cannot separate an assertion
from a hypothesis, a quotation or a stated alternative. In a registry whose whole epistemic
discipline is `DATO` / `IPOTESI` / `PREMISE_TAG` / `REVIVAL_TRIGGER`, a probe that ignores those
tags is measuring the wrong object.

**v3 passes, and it is the check the fixture actually supports.** No polarity, no semantics:
two claims that describe the same `(organism, phenotype)` axis and carry no wikilink to each
other are a **question**.

```
claim pairs sharing ≥1 axis : 9
  already cross-referenced  : 1     <- CLAIM 005 / CLAIM 037, both directions
  NOT cross-referenced      : 8     <- CANDIDATE_FOR_REVIEW, all DATO-vs-DATO
link density of the reconciliation graph: 11 %
```

Five of the eight are on the single axis `MOUSE / EPILEPSY` — the axis on which CLAIM 005 writes
the normative sentence **"No canonical statement may describe a Wwox-null mouse as showing
epileptogenesis."**

| A | B | shared axis |
|---|---|---|
| CLAIM 004 | CLAIM 005 | MOUSE/EPILEPSY |
| CLAIM 004 | CLAIM 016 | MOUSE/EPILEPSY |
| CLAIM 005 | CLAIM 016 | MOUSE/EPILEPSY |
| CLAIM 016 | CLAIM 037 | MOUSE/EPILEPSY |
| CLAIM 004 | CLAIM 037 | HUMAN/EPILEPSY, MOUSE/EPILEPSY, MOUSE/SURVIVAL |
| CLAIM 004 | CLAIM 011 | MOUSE/MYELIN |
| CLAIM 004 | CLAIM 031 | HUMAN/SURVIVAL |
| CLAIM 004 | CLAIM 038 | MOUSE/GLYCEMIA |

CLAIM 004 and CLAIM 016 carry a mouse-epilepsy axis and link to neither 005 nor 037. That is
precisely the population the constraint in CLAIM 005 is about, and it was generated by a
predicate that adjudicates nothing.

**CROSS_CLAIM_CONTRADICTION_CHECK_READINESS = READY as shared-axis link coverage (v3, fixture
passes, 8 candidates); NOT READY as a polarity detector (v1 and v2 both fail the declared
fixture, for two different reasons).** I have adjudicated no science. Every pair above is a
question for a Scientist seat or the Operator, not a finding.

---

## 9 · The one defect under all eight phases

| § | Surface | Unit the rule describes | Window the rule uses |
|---|---|---|---|
| 1 | path identity | a path segment | one character to the right |
| 2 | `.jsonl` block rules | one bibliographic record | 706 records |
| 2.3 | the negation escape hatch | one record's own disclaimer | the whole 564 KB file |
| 2.4 | `deduplicate()` | one finding | one line = one record |
| 3.5 | `README_PRIVACY_CONTRADICTION` | one document's claim | every text file, concatenated |
| 5 | `checked += 1` | an artifact **verified** | an artifact **rendered** |
| 6.4 | the runner inventory | every check the repository advertises | every tracked `test_*.py` |
| 8 | claim polarity | one asserted sentence | one whole claim |

Eight independent surfaces, one shape. Every one of them was a rule written correctly for the
unit its author had in mind, and then evaluated over a larger unit that arrived later — a new
extension, a bigger file, a router migration, a growing registry. The repository's own phrase
for this is in `designed_for_growth.md`: it is not that these rules are wrong, it is that none
of them says out loud what it is scoped to, so growth silently rescopes them.

**The generalisable repair is not eight patches. It is that every scoped predicate declares its
unit, and a test asserts the declaration** — which is what makes R3 and R4 of § 2.6 more
valuable than R1 and R2, even though they change no verdict today.

---

## 10 · TRUE_HUMAN_DECISIONS_REQUIRED

Everything above is a measurement. These seven are not, and none of them is mine.

| # | Decision | Why it is not mechanical | Blocks |
|---|---|---|---|
| **D1** | Do the **430 published corresponding-author email addresses** ship? | § 3.2: this single answer moves the gate from 301 to 56. Option C moves it by 1. | the entire publication gate |
| **D2** | Are the **480 ORCIDs** in scope for the privacy gate at all? | § 3.1(b): permanent person identifiers, currently invisible to both scanners. Adding them is a policy extension, not a bug fix | the definition of "person identifier" |
| **D3** | Is the **Operator's identity** inside the gate's scope, or only the individual-level clinical record? | § 4: `CLAUDE.md` says one thing, the digest sets say another. v1 raised it; it is unchanged | 57 live path findings + 16 uncovered |
| **D4** | Which of R1/R2/R5/R7 to authorise, in what order | § 2.6: each changes a verdict; R5 raises the visible count 301 → 491 | the record-scope repair |
| **D5** | Are **Windows path separators** in scope? | § 1.2: a darwin-only tree; the question was never asked | 2 of the 18 false negatives |
| **D6** | Define **"the canonical surface"**, or decline the MAJOR-2 narrowing | § 7.3: the widened capability has no checkable boundary | `CAND-20260826-ORCHMAJOR2` |
| **D7** | The **five stale CLAUDE.md assertions**: move the tests to the normative files, or restore the strings to the router | § 6.2: the migration was deliberate; which side is authoritative is a governance call | CI green, and every gate downstream of the failing step |

---

## 11 · FINAL OUTPUT

| key | value |
|---|---|
| `PRIVACY_SEMANTICS_REPAIR_SPEC` | § 2.6 — 8 repairs, R1–R8; R1's derived rule measured at **0 FN / 0 FP** on 26 fixtures vs **17 FN / 1 FP** shipped; live 57 → 59, a strict superset |
| `JSONL_CORRECT_SCOPE_VERDICT` | **RECORD**, with `cross_paragraph_pairing` kept at file scope. Preserves privacy (F2/F7/F8), provenance, low FP (F1/F3/F6) and a deterministic locator. Totals unchanged today; **the set is not** |
| `PUBLIC_BIBLIOGRAPHY_DECISION_PACKET` | § 3 — A/B/C/D at **301 / 55 / 300 / 56** visible BLOCKS. C moves the authoritative gate by 1. `CORRESPONDING_AUTHOR_FIELD` does not exist; 480 ORCIDs are invisible; 12 blocks are on real author names |
| `NON_PATH_IDENTITY_DECISION_PACKET` | § 4 — 29 occurrences, **16 uncovered**, reduced to **14** by R1 with no new policy. Distinction drawn (`IDENTITY_AS_SUBJECT` vs `IDENTITY_AS_MEASUREMENT_ARTEFACT`), not selected |
| `ADJUDICATION_HOSTILE_STATE_COUNT` | **21** probed (v1's 9 + 12 new) · 15 fail-open · 6 correctly failed, all 3 positive controls fired |
| `ADJUDICATION_FALSE_PASS_COUNT` | **8** — exit code, artifact count and locator count all identical to a fully verified run |
| `RELEASE_RUNNER_COMPLETENESS_FINDINGS` | § 6 — clean-clone verdict **FAIL** (9 cases / 8 suites; `main` 7/6). 5 are stale assertions about the CLAUDE.md router; 2 are this seat's own dangling references; 1 disk-dependent case isolated. Command-level completeness: **7 advertised, 3 in CI, 2 uncovered**. `legend_lint.py` has not run in CI since the migration |
| `MAJOR2_REVIEW_STATUS` | **MEASURED before reading the justification.** `CAND-20260826-ORCHMAJOR2` @ `a115cbd`, 3 ahead / 0 behind. 7 of 8 checks PASS — BASE re-derived, exactly 2 semantic changes, fingerprint contained to one role, gate PASS/0. **1 finding: `canonical surface` is undefined.** Not an approval |
| `CROSS_CLAIM_CONTRADICTION_CHECK_READINESS` | **READY** as shared-axis link coverage (v3; fixture recovered; 9 pairs, 1 reconciled, **8 candidates**, 5 on MOUSE/EPILEPSY). **NOT READY** as a polarity detector — v1 and v2 both fail the declared fixture |
| `TRUE_HUMAN_DECISIONS_REQUIRED` | **7** — § 10, D1–D7 |

**No scanner, gate, runner, governance file or canonical scientific file was modified.** Every
repair above is a specification with a measurement beside it, and every one of them is the
Operator's to authorise.
