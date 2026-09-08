# Residual closure after the 2026-09-07 consolidation — design record

> Non-normative. Records what the operator mandated on 2026-09-07/08 to close the residuals
> the consolidation register left open, what was done, and how each transformation can be
> re-verified. It legislates nothing; the operating law it touches is `LEGEND_CORE.md` §21d,
> whose provenance callout points here. The consolidation itself is not reopened by this
> record and the private preservation directory is untouched except for one new
> subdirectory of originals, listed below.

Actor: Orchestrator (session `legend-public-20`), under the operator's in-session mandate.
Peers consulted in the same cycle over the cross-session channel: `legend-public-6a` (the
consolidation session; confirmed the branch was this session's to land and restated its two
open defects), `legend-public-ad` (no ACTOR_ID, nothing uncommitted here), `legend-public-71`
(reported uncommitted work in this checkout as lost; verified together: its files were removed
by the guard-retirement pass before this session began and are preserved byte-for-byte in the
operator's 2026-09-07 19:53 backup — the claim was withdrawn). No Mirror or Plan session was live
on this machine; Mirror's record was consulted as written — the two hostile reviews below.

## 1 · `privacy-gate-strengthening` — landed, after establishing the real state

**The discordance, settled by execution.** The branch tip `8005048` said F-1 and F-2 of
`reviews/mirror/PRIVACY_GATE_REPAIR_HOSTILE_REVIEW_MIRROR_v1.md` were repaired; the review
said both were present. Fixtures run against the branch's own scanner files on 2026-09-07:

| fixture | branch gate | branch independent scan |
|---|---|---|
| F-1 `minimo/⟨op⟩` (Italian superlative pair) | **BLOCK** — not repaired | **BLOCK** — not repaired |
| F-2 `/Users/⟨op⟩⏎` (path ending a line mid-file) | BLOCK — repaired | BLOCK — line-scoped by design |
| live `/Users/⟨op⟩/…` | BLOCK | BLOCK |
| prose `il ⟨op⟩ contesto` | silent | silent |

The branch's F-1 "repair" walked left from the slash over path characters and accepted a
space as a path opener, which is exactly the shape of the superlative pair; the independent
scanner had no F-1 change at all. So F-2 was repaired and F-1 was not, in either scanner.

**What was landed instead of the branch's files.** The branch's `public_release_gate.py` was
cut from an older base and would have deleted `tracked_paths`, `tracked_documents` and the
index-based `is_nested_checkout` that `main` carries; it was not merged. The strengthening
was re-applied onto `main`'s gate, and both scanners now carry:

- `.jsonl` in the scanned suffixes (14 tracked `.jsonl` files were never opened before);
- the **root-anchored path rule** Mirror prototyped in
  `PRIVACY_SEMANTICS_AND_FALSE_PASS_HOSTILE_REVIEW_MIRROR_v2.md` § 1.6: a closed set of path
  roots (`/Users/`, `/home/`, `/var/folders/`, `~/`, `X:\Users\`), the run of non-whitespace
  non-quote characters after it, every alphabetic sub-run casefolded and hashed against the
  path digest set. F-1 closes structurally (a slash-pair has no root); F-2 closes because
  a run ends at whitespace; the F-3 forms (period, bold, colon, angle bracket) are caught
  because only alphabetic sub-runs are hashed and the token precedes the punctuation, so
  it does not matter that the punctuation sits inside the run; list punctuation (`, ; |`
  and brackets) ends a run, so a table cell or CSV field after a path is a separate run;
  and `~/.legend/lineage/AIR-DI-…` is reached through the `~/` root;
- the content-address **fragment skip**: a private three-letter token inside a hex run of
  ≥ 12 characters carrying a digit is a candidate identifier (`RPC-` + 12 hex), not a name —
  three false BLOCKs in `pathograph_export.jsonl` measured, all removed;
- **record scope on `.jsonl`** (Mirror v1 F-4, v2 Phase 2): block-scoped rules, the
  attribution window and the parental-word window are evaluated over one line, never
  across records. Two windows are deliberately left file-wide, because clipping them
  removed BLOCKs the file-wide form raised: the cross-paragraph reassembly window
  (explicit pairing language ± 2200 characters; two variants in two records and "these two
  variants together in the same person" in a third) and the person-context window (± 700;
  a person noun in one record and the two variants in the next two). The one asymmetry is
  stated: a parental word and a variant in different records are not a transmission claim,
  a person noun near two variants in neighbouring records may be, and the gate errs
  towards scanning more. Both directions are pinned by tests. Measured effect on
  `pathograph_export.jsonl`: one false `PARENT_OF_ORIGIN_PAIRING` BLOCK on a line with no
  variant became four `REVIEW`s, each attributed to its own record;
- **`PUBLIC_BIBLIOGRAPHIC_AUTHOR`** (REVIEW, never silent): a match on the `fore_name` /
  `last_name` field of a record in `registries/corpus_seed_pubmed_*.jsonl`. This is option C
  of Mirror's decision packet — names and institutions permitted, contact fields restricted —
  which is the choice the operator's e-mail instruction below implies. One live hit, a
  published author sharing the operator's given name; the same token anywhere else in the
  file still blocks.

Tests: 55 in `test_public_release_gate.py` (42 on `main`, +13), 16 in
`test_independent_privacy_scan.py` (6 on `main`, +10), every fixture above included. The independent scanner is not part of the release gate
or of `run_release_regressions.py`; its own verdict over the corpus seed stays red on Italian
cities and institutions by its own policy, and that was not changed.

## 2 · Machine paths — normalised in 22 tracked files, 37 occurrences

Convention, the consolidation's own: `/Users/⟨op⟩/Desktop/legend-public` → `<REPO_ROOT>`,
any other `/Users/⟨op⟩` → `<HOME>`. After this record no tracked file carries a
`/Users/⟨op⟩` path (the literal `/Users/` survives in 12 files, 54 times, in fixtures and
examples that name nobody — counted excluding this record, which quotes the forms). Two further forms of the same identity, found by the blind
review, were normalised as well: the OS account name in five captured `lsof` rows of
`framework/protocols/actor_identity_feasibility.md` (→ `<user>`), and the Claude-projects
slug `-Users-⟨op⟩-Desktop-legend-public` in one design note and one code comment — neither
form is a rooted path and neither scanner reaches it. Three files needed more than a
substitution:

| file | why | what was done |
|---|---|---|
| `disease-models/wwox/registries/fulltext_read_receipts.jsonl` | hash-chained, tail-anchored | events `FTR-20260811-21075834-01` (line 95) and `FTR-20260811-23435430-02` (line 125): the path inside `evidence_basis` strings only, no other field; `ledger_prev_hash` recomputed for the 35 events after line 95 with the writer's own `receipt_digest`; manifest re-anchored with `fulltext_receipts.py anchor`; `verify` OK 130. sha256 before `7831168e954b6390cb30efbb7c8ffcc714d7ec2316f87cbbd895309caca26de2`, after `187b2afb88a2698dd20d758f0d3d45622758b8c2c7b77385f7ad30de8c9e69ff`; head before `c4635ce6…b080aa`, after `bcc3622d34481954fbb1671630c4d58c7504cfff8743bd84ace959eb3bd3cb07` |
| `framework/state/sync_epochs.jsonl` | hash-chained, tail-anchored, one event | `workspace` and four path strings in `observations`; head before `53ec0cdb…f779f5`, after `1f10fc71a601d092fee56b9ced6ced72772e3c928de51e33f9463b2b18df1fdf`; manifest anchor updated; `sync_epochs.py verify` OK |
| `learning/scientist/evalset/frozen_set_v1.json` | digest pinned in `EVALUATOR_FROZEN_SET_AND_BLIND_ROUND_DESIGN_SCIC_v1.md` | one string, `corpus_root`; sha256 `15e2bf63…a68e87` → `54905e7661986707e35d078efbbc4235f45f310ae80d1474989ecb9384d39f45`; both pins updated and a dated note placed beside the recipe |

`launch/KERNEL_SPEC.md:42` carried the operator's machine-derived identity twice inside one
path-like string; it now reads `AIR-DI-⟨OP⟩-⟨op⟩`, the form Mirror's own reviews use. The
remaining hostname mentions — 8 occurrences on 6 lines, five lines in that file and one in
`learned_gates_registry.md` — are not paths and were not touched: they are Mirror v2's
Phase-4 decision packet, still the operator's.

**Verifiable transformation.** The pre-transformation bytes of the two ledgers, the state
manifest, the frozen set, the corpus seed and its manifest are preserved privately at
`legend-public-preservation-20260907-consolidation/residual-closure-20260907/originals/` with a
`SHA256SUMS.txt`; re-running the substitutions above over those bytes and re-chaining with
`fulltext_receipts.receipt_digest` reproduces the tracked files byte for byte. The
consolidation register's own note that `.json`/`.jsonl` and the pinned frozen set were left
alone is now superseded by this section, under the operator's explicit authorisation. No
scientific content changed; no signature was fabricated; the chain fields were recomputed by
the ledger's own function, not authored.

## 3 · PubMed corpus seed — affiliation e-mails redacted from the published copy

Structure checked first: every address sits inside `authors[].affiliations[]` strings, none
elsewhere. The address alone was replaced by the literal `[email redacted]`; no affiliation
field was removed and no other byte changed. 430 occurrences, 262 distinct addresses, 245
records, plus one malformed double-`@` fragment. `corpus_seed_pubmed_20260806.manifest.json`
carries the new sha256 (`2d0165ef97dafdbd29b8990c4a319548ca2360252d1ef41cf16456a17fb14e43`),
the previous one, and a `redacted_in_published_copy` block stating what, why and how many;
`pubmed_corpus_harvest.py --verify` OK. The derived `.tsv` never carried addresses. The
unredacted original is private, in the directory above.

## 4 · `CHK-plan-0010` collision — the archived checkpoint recovered as `CHK-plan-0020`

The consolidation excluded branch `evidence-index`'s `CHK-plan-0010.json` (task
`P51C9-REMEDIATION-001`) because `main` holds a `CHK-plan-0010` for `SCIENTIST-AB-SPEC-001`.
The archived record (from tip `7a90a91`, sha256
`553dbb5817a53234567f395e3c134dab68d3f2ed016a2f7e86ad75caa441ad76`, also in the private
bundle) now lives at `ledger/checkpoints/plan/CHK-plan-0020.json`: its `CHECKPOINT_ID` is the
only value changed and a `_RECOVERED_UNDER_NEW_ID` block at the top states original id, task,
provenance and reason. `main`'s `CHK-plan-0010` is untouched. The one reference that meant the
recovered record — `CAND-20260817-P51C9.md` § 4 — carries a renumbering note; the references to
`CHK-plan-0010` in `SCIENTIST-AB-SPEC-001.json`, `CHK-plan-0011.json` and
`CAND-20260818-SCIENTIST-AB-SPEC.md` mean the canonical one and were left alone.

## 5 · `CAND-20260826-RTBRIDGE.md` — annotated as retired

Front-matter `status: RETIRED` and a banner under the title: the runtime bridge it describes
was removed from `main` on 2026-09-07 (`4341ef9`); the body is kept unaltered as history and
instructs no current actor. `CAND-20260829-RTBRIDGE8` and `CAND-20260831-RTBRIDGE13` are named
in the banner as being in the same position; they were not rewritten.

## 6 · §21d aligned to the current mandate

The push rule now says what is true: agents push to `development` only, fast-forward, one
ref, gate PASS on the exact SHA, recorded in the session report; `development/main` is
included when the change alters no guarantee or the operator has mandated it in session;
`origin` is the operator's alone; **nothing mechanical enforces any of it** — the runtime
guard and its hooks were retired on 2026-09-07, and the controls are the ones the pushing
actor performs and records plus the tracking-ref reflog. The per-push blind Mirror review and
the `ledger/push_authorizations.jsonl` precondition — a ledger that never existed — were
replaced by §21e's ex-post review. No guard, blocking hook, PR obligation or authorisation
procedure was introduced. `scripts/test_stop_policy.py` asserts the new body verbatim; the
DEC's hash table carries the 2026-09-03 value as history (it did not reproduce the body it
was said to cover) and the 2026-09-08 value derived by the DEC's own recipe — no trailing
newline, over the asserted constant. The same pass found and repaired what `4341ef9` had
left behind in §21c: its hash row was stale (the body it covered had been rewritten) and its
provenance callout had lost its value and half a sentence; both now carry the re-derived
digest (34 lines) with the old value kept as history.

**The earlier push to `origin`, investigated with the evidence available and closed.**
`refs/remotes/origin/main` moved to `4341ef9` by `update by push` at 2026-09-07 20:15:51
+0200, ten minutes after that commit was made on `main` here. The tracking-ref reflog shows
the push was made from this clone; it does not name the actor. No session transcript in this
project's Claude directory and no shell history line records a push to `origin` at that time
(shell history holds three pushes, all to `development`). The peer sessions asked all
disclaim it. **Attribution: not determined.** No compromise is inferred from the reflog alone.
What the push published is measured, not assumed: `origin/main` moved from `8ab8e4b`
(2026-08-01, 3 commits) to `4341ef9` — **679 commits**, among them the corpus seed with its
affiliation e-mails, the 22 files with machine paths this record normalises, and the five
commits authored with a personal address that the consolidation register's residual 2 lists.
None of that was on `origin` before 2026-09-07 20:15:51. So the exposure § 7 describes as
"earlier commits" is on the public release repository's history, not only on `development`'s.
The local investigation ends here; what to do about `origin`'s history is the operator's.

## 7 · Blind review before landing — findings, repairs, acceptances

A fresh reviewer instance (Mirror role, no conversation history; given the diff, the gate
output and read-only access) returned BLOCK with 8 blocking findings and 6 notes, every one
with an executed fixture. Each was repaired in the same commit or accepted with a reason:

| finding | disposition |
|---|---|
| §21c hash row stale and callout mangled since `4341ef9`; §21d hash serialised differently from the DEC's own recipe | **repaired** — both blocks re-derived by the recipe (§21c 34 lines, §21d 57), callout restored, old values kept as history |
| path run kept list punctuation inside it, so `/home/legend,⟨op⟩`, `\|/home/legend\|⟨op⟩\|` and `(vedi /home/legend)(⟨op⟩)` blocked; the shipped comment described a mechanism the code did not have | **repaired** in both scanners — `, ; \| ( ) [ ] < >` end a run; comment rewritten to the real mechanism; three fixtures added |
| independent scanner applied the digest skip before the path check, losing `/var/folders/⟨op⟩9f2c…` | **repaired** — path context decided first; fixture added |
| parental-word and person-context windows still crossed `.jsonl` records | **repaired for the parental-word window** (clipped to the line; fixture added). The person-context clip was applied and then **reverted at round 2** (R-1): it removed cross-record BLOCKs — proband in one record, the two variants in the next two — so that window stays file-wide, with a fixture pinning the BLOCK |
| narrowing the reassembly window removed a pre-existing BLOCK | **repaired** by reverting the narrowing (conservative direction), stated in § 1 |
| "no tracked file carries a `/Users/…` path" was false as written; OS account name in `lsof` rows and the projects slug survived unseen | **repaired** — wording fixed, both forms normalised (§ 2) |
| counts: 14 tracked `.jsonl` (not ten); +12 / +10 tests; 8 hostname occurrences on 6 lines | **repaired** in this record and in the scanner comment |
| the push rule is widened in the same commit that removes its enforcement, and the only ratification cited is inside the change | **accepted** — the ratification is the operator's in-session mandate of 2026-09-07/08, which is exactly what the DEC row and this record cite; a wider rule with no mechanical control is what is true, and saying so is the point |
| Windows separators inside JSON strings (`C:\\\\Users\\\\…`), JSON `\/`-escaped POSIX paths, and unrooted forms (`/Volumes/…/Users/⟨op⟩`, `/root/⟨op⟩`, `/mnt/c/Users/⟨op⟩`, lowercase `/users/`, `~⟨op⟩/`, `../Users/⟨op⟩`) are silent in both scanners | **accepted as a stated limit** — none occurs in the tree today (measured by the reviewer); the root set is closed on purpose so the homonym stays silent, and widening it is a Mirror task, not a closure |

## 8 · What this closure does and does not do

It cleans the **tip**: after this landing the publication gate is green on the exact tree
pushed. It does not rewrite published history: the machine paths, the affiliation e-mails and
the five commits authored with a personal address remain in earlier commits of
`development/main` and of `origin/main`, exactly as the consolidation register's residual 2
records. Removing them is a history rewrite, reserved to the operator, and is not part of
this session.
