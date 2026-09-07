---
artifact: MIRROR hostile review (Annex C.2) — executable repairs and false-green surfaces
review_id: PRIVACY_GATE_REPAIR_HOSTILE_REVIEW_MIRROR_v1
object: commits `f281292` (two-gate privacy repair) and `57ea7a4` (review correction); the
  tracked-tree blocking population they surface; `regenerate_adjudications.py` as a gate
continues: SCIENTIST_CROSS_REVIEW_PILOT_HOSTILE_REVIEW_MIRROR_v1 (does not reopen the pilot)
level: R4 (METHOD — Mirror)
reviewer: mirror
date: 2026-08-26
verdict: REPAIR_SOUND_IN_DIRECTION, UNSOUND_IN_PREMISE — 6 findings, 2 blocking
personal_data: none reproduced. The human role is **Operator** throughout. Adversarial
  fixtures carrying the identifier tokens were built in the session scratchpad only and are
  not part of this tree.
scope_note: every number below was produced by executing a command in this session against a
  clean `git archive HEAD` export, not against my working directory. Where I report another
  actor's figure I re-derived it and say whether it held.
---

# The rule says a path segment cannot be the common word, and two Italian words disprove it

---

## 0 · OBSERVATION_SCOPE

Every negative below is scoped to this table. **Local NOT_FOUND is not repo-wide NOT_EXIST.**

| Fact | Value |
|---|---|
| Derivation instant | `2026-08-26T06:32:33Z` |
| My worktree / HEAD | `.claude/worktrees/mirror`, branch `mirror` @ `57ea7a4` — 0 behind `main`, 88 ahead |
| Shared checkout | `legend-operating-convention-v1` @ `9a13c49` |
| Measured population | `git archive HEAD \| tar -x` → 685 files, 10 tracked `.jsonl` |
| Python | 3.9.6 · PyMuPDF 1.26.5 |
| Untracked in my worktree | 10 files under `learning/mirror/`, `reviews/mirror/` — **excluded** from every count by measuring the export, not the working directory |

**Why the export.** Both scanners walk the filesystem, not the index. My worktree carries 10
untracked files; scanning `.` here would have measured a tree nobody has. Every figure below
comes from the export.

**What this document deliberately does not reproduce, and the one thing that would have made
it lie.** I scanned my own draft before proposing it and it raised 18 findings, 4 of them the
case-identifier tokens, which occur **zero** times in the tracked tree today. Those are redacted:
this review is not the object that introduces them. The Italian slash-pair fixtures of § 2 are
written `minimo/⟨op⟩`, because spelling them out would have created the **first live instance of
the very false positive § 2 reports as latent** — the sentence "no such slash-pair occurs in the
tree today" would have been falsified by the file asserting it. The fixtures are executable in
the session harness; the demonstration loses nothing but the string.

> 🔴 **REDACTION APPLIED BEFORE THIS FILE WAS EVER COMMITTED — 2026-08-26, at the durability
> commit.** The draft this section originally described kept the operator token spelled out in
> path examples, on the argument that 57 such occurrences already exist in tracked files. That
> argument was wrong for seven of them. `PRIVACY_SEMANTICS_AND_FALSE_PASS_HOSTILE_REVIEW_MIRROR_v2`
> § 0.2 measured this file and found **7 terminator escapes** — path forms whose terminator is
> outside the accepted set, which no gate can see. Committing the draft would have placed seven
> unblocked operator-identity paths into the public tracked surface and falsified § 4's own
> *"latent, not live"* in the act of publishing it. So every occurrence of the operator token is
> now `⟨op⟩` / `⟨Op⟩` / `⟨OP⟩`, the paired parent-side vocabularies of § 5 are `⟨MAT⟩` / `⟨PAT⟩`,
> and the person noun that paired with a geography word is written *case-identifier*. No finding,
> count or verdict changed: every one of them is structural. This file was untracked when the
> redaction was made, so nothing durable was rewritten.
>
> Measured on a `git archive HEAD` export with this file added — before → after redaction:
> `public_release_gate.py` **307 → 301 BLOCKS**, `independent_privacy_scan.py` **686 → 683
> blocking**, and the seven invisible escapes → **0**. The six visible blocks were the cheap
> half; the seven the gate could not see were the reason.

---

## 1 · The delta, re-derived and correctly attributed

The commit reports *"36 findings to 701, 2 blocks to 301"*. Both halves are true and they are
**two different tools**, which the sentence does not say. I isolated the scanner change by
running the *pre-repair* scanners over *byte-identical HEAD content* — the two trees differ by
the two scanner files and nothing else (`diff -rq`, empty).

| Tool | pre-repair | post-repair |
|---|---|---|
| `independent_privacy_scan.py` findings | 36 | **701** |
| `independent_privacy_scan.py` blocking | 18 | **683** |
| `public_release_gate.py` BLOCKS | 2 | **301** |

**CURRENT_FINDING_COUNT = 701 · CURRENT_BLOCK_COUNT = 683 (independent) / 301 (release gate).**

One arithmetic slip in `f281292`: *"612 of 683 **new** blocking findings"*. 683 is the total;
the delta is **665**. The 612 figure is right and the denominator it is quoted against is not.

Behaviours **A** (`.jsonl` reached), **D** (homonym silent), **E** (hex runs), **F** (clean
files) all verified independently and hold. The four pre-repair `PRIVATE_NAME` findings were
all one three-letter case-identifier token matched inside SHA-256 seals — a 100 % false-positive rate,
now zero. That part is a clean win.

---

## 2 · FINDING 1 — BLOCKING — the path rule's premise is false

The repair's justification, quoted from the source:

> a path segment sits between two separators, [so] the token cannot be the common word

That premise is falsified by two ordinary Italian words. `in_path_context` asks only whether the
match is preceded by `/` and followed by a member of a 12-character set. In
`minimo/⟨op⟩` — *minimum/maximum*, standard Italian — the token is preceded by `/` and
followed by a space. Both scanners raise a blocking `PRIVATE_NAME`/`DIRECT_IDENTIFIER`:

| fixture | expected | independent | release gate |
|---|---|---|---|
| `Il valore minimo/⟨op⟩ del parametro.` (`.md`) | silent | **BLOCK** | **BLOCK** |
| `{"nota": "range minimo/⟨op⟩ ammesso"}` (`.jsonl`) | silent | **BLOCK** | **BLOCK** |

This is the exact class the repair was built to avoid, re-admitted through the repair's own
definition. **Latent, not live**: no such slash-pair occurs in the tree today, and all 57 live
lowercase hits are genuine `/Users/⟨op⟩` paths. It is a defect of the rule, not of the tree —
in an Italian-language repository that grows.

`TESTED_POLICY` vs `BUG`: the *decision* (lowercase must not block in prose) is tested policy and
I do not contest it. The *implementation* admits a case the decision excludes. **BUG.**

---

## 3 · FINDING 2 — BLOCKING — the two scanners disagree, and the publication gate is the one that misses

`public_release_gate.py` scans whole-file text; `independent_privacy_scan.py` scans line by line.
`path_segment_after` does not contain `\n`. Therefore a path ending a line blocks in the
independent scanner and **passes the release gate**:

```
The home directory is /Users/⟨op⟩⏎next line
   independent_privacy_scan.py → BLOCK
   public_release_gate.py      → silent
```

Only a path at the very end of the *file* is caught by the gate (`end >= len(text)`), which is
why the author's fixture passed. A path at the end of any line mid-file is the ordinary case, and
it escapes the authoritative gate. Two implementations kept independent on purpose have diverged
on the single most common emission form of the class the Operator authorised. **BUG.**

---

## 4 · FINDING 3 — the terminator set is a list where a grammar is needed

Six further path forms carry the identifier past **both** scanners:

| form | example | both scanners |
|---|---|---|
| sentence period | `It lives under /Users/⟨op⟩.` | silent |
| markdown bold | `Root is **/Users/⟨op⟩**` | silent |
| colon (shell / `lsof`) | `/Users/⟨op⟩: permission denied` | silent |
| angle bracket | `<file:///Users/⟨op⟩>` | silent |
| backslash separator | `C:\Users\⟨op⟩\Desktop` | silent |
| JSON-escaped backslash | `{"cwd": "C:\\Users\\⟨op⟩\\..."}` | silent |
| URL query | `/Users/⟨op⟩?x=1` | silent |

The first three are realistic in this repository *today* — it is full of markdown prose and
captured shell output. Classified **BUG** for period/bold/colon/angle; the two backslash forms are
`NEW_OPERATOR_DECISION` (darwin-only tree; whether Windows separators are in scope was never asked).

Note the asymmetry that shows the set was assembled, not derived: `\` **is** an accepted
terminator while `.` is not, so `/Users/⟨op⟩\` blocks and `/Users/⟨op⟩.` does not.

---

## 5 · FINDING 4 — BLOCKING — `.jsonl` was admitted to the gate without the block-scope rule `.json` needed

`attribution_window()` special-cases `.json` and returns the whole file, with a written rationale:
*"for a per-paper record the file IS the record"*. `.jsonl` was added to `TEXT_SUFFIXES` and **not**
to that special case — and for `.jsonl` the rationale inverts: the file is **706 records**, not one.

Measured on `corpus_seed_pubmed_20260806.jsonl`: **706 lines, 0 blank lines, 3 925 102 characters
→ one single block.** Every block-scoped rule in the gate therefore degenerates to file scope over
706 unrelated published papers.

It already fires. The live tree emits:

```
[REVIEW] PARENT_OF_ORIGIN_ATTRIBUTED corpus_seed_pubmed_20260806.jsonl:273
```

⟨MAT⟩ words sit on lines 273/491/513/580/624; the lone ⟨PAT⟩ word is on line **634**.
Different papers. The reviewer is sent to line 273, which contains no pairing.

**And it is one harvest away from a false BLOCK.** The file already carries 7 `compound_linkage`
phrases across 6 records and 1 752 study identifiers. Only the absence of a variant string holds
the gate green. I proved this rather than asserting it — mutation: two records, two *different*
plausible published papers, one naming `Q230P`, one naming `c.1057-2A>G`, inserted 630 records
apart, nothing linking them:

```
[BLOCK] REIDENTIFYING_VARIANT_COMBINATION corpus_seed_pubmed_20260806.jsonl:487
        — An exact two-variant combination is linked as one genotype/case.
[BLOCK] PARENT_OF_ORIGIN_PAIRING          corpus_seed_pubmed_20260806.jsonl:274
        — ...with no published study to attribute them to.
```

Line 487 is a *third* unrelated record. Blocks: 301 → 303. Three unrelated published papers
reported as one linked genotype. A false BLOCK on the publication gate is not the benign
direction of a validation failure — it is the gate stopping publication for a reason that is not
in the data, on the largest and fastest-growing file in the repository.

---

## 6 · FINDING 5 — a BLOCK whose message names a condition that did not fire

The `else` branch of the parent-of-origin rule emits *"with no published study to attribute them
to"*. It is reached whenever `reference_present` is true — **regardless of attribution**. On the
corpus seed the window contains 1 752 study identifiers, so the message is false about the state
that produced it. A human sent to find an unattributed record will find 706 attributed ones.
Pre-exists `.jsonl`; `.jsonl` is what makes it reachable at scale. **BUG (auditability).**

---

## 7 · FINDING 6 — behaviour B is not met, and a passing test says it is

Required behaviour **B** — uppercase identifiers block in `.md`/`.json`/`.jsonl` — **fails for the
token this repair is about**:

| token | `.md` | `.json` | `.jsonl` |
|---|---|---|---|
| the three case-identifier tokens, uppercased | BLOCK | BLOCK | BLOCK |
| `⟨OP⟩` | **silent** | **silent** | **silent** |

Cause: `sha256("⟨op⟩")` was placed in `PATH_CASEFOLD_IDENTIFIER_DIGESTS` (consulted only in
path context) and never in `CASEFOLD_IDENTIFIER_DIGESTS`. Casefolding `⟨OP⟩` yields `⟨op⟩`,
which the general set does not contain.

**This is not tested policy.** Both suites carry a test named for this behaviour —
`test_uppercase_private_name_in_compound_token_blocks` /
`test_uppercase_identifier_inside_compound_token_blocks` — and both build their token from
codepoint assembly — a three-letter case-identifier token — whose casefold digest **is** in the general
set. The suites
exercise the one token family that already worked and never the one whose digest was
deliberately withheld. The test passes; a reader concludes uppercase identifiers block; the
identifier at issue in this very repair does not. **That is the false-green surface, inside the
repair's own evidence.**

No test asserts `⟨OP⟩` must stay silent, so this is a gap, not a decision — but whether the
homonym argument extends to the uppercase form (`IL ⟨OP⟩ CONTESTO`) is genuinely the
Operator's call. **NEW_OPERATOR_DECISION**, with the gap named.

---

## 8 · BLOCKING_POPULATION_BY_CLASS

Independent scanner, clean tracked tree, 701 findings / 683 blocking.

| Class | Count | Blocking | Where |
|---|---:|---:|---|
| `PUBLIC_INSTITUTION` (Italian hospitals/universities in PubMed affiliations) | 143 | 143 | 142 corpus seed |
| `PUBLIC_INSTITUTION` / geography (`ITALIAN_CITY` in affiliations) | 368 | 363 | 358 corpus seed |
| `PUBLIC_EMAIL` (published corresponding-author addresses) | 111 | 98 | 94 corpus seed |
| `PATH_IDENTITY` (`/Users/⟨op⟩`, the class the Operator approved) | 57 | 57 | 33 files |
| `PUBLIC_BIBLIOGRAPHIC_AUTHOR` | 1 | 1 | corpus seed `fore_name` |
| `HASH_OR_SIGIL_FALSE_POSITIVE` | 0 | 0 | was 4 pre-repair, now eliminated |
| `COMMON_WORD_HOMONYM` (`potenza`, correctly INFO) | 5 | 0 | 3 files |
| `CALENDAR_DATE` (incl. one false positive reading a numeric range as a 5th-millennium date) | 21 | 21 | 17 corpus seed |
| `OTHER` (a non-allowlisted `example.org` test fixture, project git identity) | — | 4 | test suites, 1 review |
| `OPERATOR_PERSONAL_IDENTITY` non-path / `SYSTEM_USERNAME` / `MACHINE_HOSTNAME` | 16 | **0** | § 9 — *no gate reaches these* |

**BY_EXTENSION** — `.jsonl` 620 · `.md` 54 · `.py` 16 · `.json` 7 · `.tsv` 4.
**Dominant file**: `corpus_seed_pubmed_20260806.jsonl` = **612 of 701 (87 %)**.

The corpus-seed population is **100 % public PubMed bibliographic metadata** — author
affiliations, hospitals, cities and corresponding-author addresses at US and UK research
institutes. Zero operator content, zero individual-level record. I did not touch the
data to make the gate green.

---

## 9 · NON_PATH_PERSONAL_IDENTITY_EXPOSURE — the commit's 16 is correct, and 11 are unreachable

I re-derived this with the scanner's own `in_path_context` predicate rather than by eye. My first
count was 23 and the commit's was 29; the commit is right and I was counting lowercase only.

**86 case-insensitive occurrences: 57 in path context, 29 not.** Of the 29:

| Class | n | Surface | Covered? |
|---|---:|---|---|
| `COMMON_WORD_HOMONYM` | 12 | Italian prose (10) + test fixtures (2) | correctly silent — **by design** |
| `PUBLIC_BIBLIOGRAPHIC_AUTHOR` | 1 | corpus seed `fore_name` + ORCID | blocked, but **mislabelled** as a private identifier |
| `MACHINE_HOSTNAME` | 11 | `KERNEL_SPEC.md` ×6, `learned_gates_registry.md` ×3 … | **NOT COVERED** |
| `SYSTEM_USERNAME` | 5 | `actor_identity_feasibility.md:146-150`, captured `lsof` | **NOT COVERED** |

The uncovered 16 are `AIR-DI-⟨OP⟩`, `MacBook-Air-di-⟨op⟩`, `MacBook Air di ⟨op⟩`,
`AIR-DI-⟨OP⟩-⟨op⟩`, and the OS username column of captured `lsof` output. Two independent
reasons they escape: uppercase has no reachable digest (§ 7), and the lowercase forms are preceded
by `-` or whitespace, not `/`.

`launch/KERNEL_SPEC.md:42` is the sharpest single instance — `~/.legend/lineage/AIR-DI-⟨OP⟩-⟨op⟩/`
carries the operator's machine-derived identity **twice inside one path-like string**, and neither
occurrence is reachable by either gate in either case form.

**Honest framing of the exposure.** These are quoted *measurement outputs* inside the specification
of the `DERIVED_IDENTITY_IS_NOT_IDENTITY` gate: the four names **are** the evidence for the rule.
Redacting them removes the measurement that justifies the gate. And the repository's declared
privacy boundary is the *individual-level clinical record*, not the Operator — `CLAUDE.md` says the
public edition excludes the N-of-1 overlay. But the system's **own digest set** lists the Operator's
name beside the case-identifier tokens, so by its own policy this is prohibited surface that no gate reads.
That contradiction is the question, and it is the Operator's to settle — I have not extended policy.

---

## 10 · REGENERATE_ADJUDICATIONS — nine degraded states, nine PASSes

Measured, not read. Baseline on a tree with the three source PDFs staged:
**exit 0, 27 artifacts, 47 locators** — a genuine green. Each mutation was applied to a *pristine*
copy of that green tree.

| Mutation | exit | verdict |
|---|---:|---|
| `ZERO_COVERAGE` — all recipes deleted | 0 | **FAIL-OPEN** |
| `ZERO_COVERAGE` — adjudications directory renamed | 0 | **FAIL-OPEN** |
| `MISSING_DIGEST` — one artifact | 0 | **FAIL-OPEN** |
| `MISSING_DIGEST` — all 7 artifacts of one recipe | 0 | **FAIL-OPEN** |
| `MISSPELLED_MANIFEST` — declared, not found | 0 | **FAIL-OPEN** |
| `MANIFEST_REMOVED` — key dropped | 0 | **FAIL-OPEN** |
| `EMPTY_ARTIFACTS` — recipe checks nothing | 0 | **FAIL-OPEN** |
| `EMPTY_ADJUDICATES` — no locator claims (mine, unspecified) | 0 | **FAIL-OPEN** |
| `STALE_ON_DISK` — png corrupted after `write` (mine, unspecified) | 0 | **FAIL-OPEN** |

Three results deserve quoting exactly.

**`GREEN_OUTPUT_WITHOUT_CURRENT_VERIFICATION`.** With all 7 digests of one recipe removed, the run
still prints:

> `OK: 27 adjudication artifact(s) regenerate to their declared digest, and 47 locator(s) resolve…`

The sentence is **false**. `checked += 1` runs before the digest branch, so `checked` counts
artifacts *rendered*, not *verified*: 7 of those 27 declared no digest at all and the per-artifact
line saying so goes to **stdout, never to `failures`**.

**`MISSING_OR_MISSPELLED_MANIFEST`.** `snippets()` returns `None` both when no manifest is declared
*and* when the declared path does not exist. A typo therefore prints *"no manifest declared"* —
which is untrue — and the locator↔snippet binding is skipped while the summary still claims 47
locators resolved.

**`ZERO_COVERAGE`.** An empty or renamed directory prints `OK: 0 adjudication artifact(s)…` and
exits 0. A gate whose population is empty reports success.

**Can a downstream actor mistake this for PASS? Yes, and one already has.** The command is not run
by `run_release_regressions.py` — only `test_regenerate_adjudications.py` is, and that suite's 12
tests exercise `check_needles` geometry and the span predicate; **none calls `run()`**, so nothing
in CI tests the exit code at all. The actual consumer is the canonical state, by transcription:
`state_manifest_current.md:112` records *"verify PASS over 18 artifacts and 37 locator
resolutions"*; `full_text_queue_current.md:3116` records *"→ PASS (9 artefatti, 10 locator)"*.
Those counts reconcile with my run today (18+9 = 27, 37+10 = 47), so the record is accurate now —
and the numbers transcribed are exactly the ones I proved can be inflated by a dropped key, in a
command that cannot be re-run from a clean clone because the PDFs are gitignored by design.

**REGENERATE_ADJUDICATIONS_CROSSCHECK_STATUS = FAIL_OPEN_CONFIRMED, 9/9 states, measured
independently of Plan (Plan's analysis not yet materialised in this tree).**

---

## 11 · PUBLIC_BIBLIOGRAPHY_DECISION_READY — the surface, not the choice

612 of 701 findings are one file of public PubMed metadata. **I do not choose.**

| | **A** — block all person identifiers | **B** — permit structurally-identified bibliographic metadata | **C** — names/institutions permitted, contact fields restricted |
|---|---|---|---|
| `PRIVACY_RISK` | lowest | low for affiliations; **real for emails** — 111 addresses, many decades old, still deliverable, republished as a bulk set | low: the residual personal-contact channel is closed |
| `REPRODUCIBILITY_COST` | **highest** — the seed cannot ship; corpus provenance becomes unverifiable | none | low — a reader can re-fetch emails from PubMed by PMID |
| `SCIENTIFIC_PROVENANCE_COST` | **severe** — affiliation is how group credibility and author disambiguation are done (`research-group-analyst` depends on it) | none | negligible — no analysis in this repo keys on author email |
| `IMPLEMENTATION_COMPLEXITY` | none — status quo | **highest** — needs a trusted structural predicate (field path + provenance), i.e. a new schema contract | moderate — one field-name denylist over `.jsonl` records |
| `FALSE_POSITIVE_RISK` | **committed and permanent**: today 612, of which 0 are private | shifts risk to a *false negative* if the structural marker can be forged or misapplied | small: an email in a free-text affiliation string, not a field |
| `FAILURE_MODE` | gate is permanently red → **the gate stops being read**, which is the worst outcome for every other rule it carries | a private record mislabelled as bibliographic passes silently | an email inside prose escapes the field rule |
| `AUDITABILITY` | trivial | needs the marker to be independently checkable, else it is an assertion | good — the denylist is enumerable and testable |

**Two facts the decision should carry.** (i) Under *every* option the single
`PUBLIC_BIBLIOGRAPHIC_AUTHOR` hit is reported as *"Legacy personal identifier remains in public
material"* — a published author sharing the Operator's given name is structurally indistinguishable
to a digest scanner, so the finding's **wording** misattributes under A, B and C alike. (ii) Option
A's failure mode is the one this repository has already named elsewhere: a gate that is always red
is a gate nobody reads.

---

## 12 · MAJOR2_REVIEW_READY

**Precondition unmet — no review performed.** No MAJOR-2 candidate exists in this tree or on any
branch reachable from it: no new object, no routing from Orchestrator. Reviewing an unmaterialised
candidate would produce an approval of nothing. The falsification checklist the brief specifies is
recorded verbatim in § 13 and will be executed on the object when it exists — against the object,
not against the Operator's wording of it.

---

## 13 · Checklists, prepared and not executed

### 13a · MAJOR-2, when it materialises

1. **Exactly two semantic changes** — `git diff` reduced to semantic hunks; count them; a third is a finding.
2. **No wholesale ORCHSURF rev-4 inheritance** — diff the candidate against rev 4 and name every clause that arrived without being authorised.
3. **Correct BASE_HEAD** — re-derive it; do not accept the declared value.
4. **Role-contract hash consistency** — recompute via `governance_fingerprint.py compose --all`; compare to the declared hash, not to the previous report.
5. **Contradiction actually resolved** — construct the case that made it a contradiction and re-run it; a reworded clause is not a resolution.
6. **Root reserved for canonical batch** — verify by attempting the excluded act, not by reading the rule.
7. **Orchestrator own-work commit remains noncanonical** — check the classification mechanism, not the label.
8. **No hidden authority expansion** — diff the *capability set*, not the prose; a widened verb is an expansion.
9. **Coherence proof** — the resulting contract must be shown consistent, not merely unobjectionable.

### 13b · Scientific candidates — hostile review checklist

Prepared for the restored Orchestrator to assign. Not executed indiscriminately.

| # | Challenge | Refutation test |
|---|---|---|
| 1 | Evidence **inherited vs re-derived** | Ask which command produced each figure *in this session*. An inherited number is a citation, not a measurement. |
| 2 | **Locator/provenance mismatch** | Resolve every locator to its span independently; confirm the needle is unique on the page. |
| 3 | Evidence in the **manifest but absent from the claim** | Diff manifest locators against claim citations both ways; the unused half is the interesting half. |
| 4 | **Over-generalised genotype conclusions** | Name the alleles actually assayed; any statement wider than that set is unsupported. |
| 5 | **Endpoint-specific effects collapsed into global statements** | List every endpoint measured; check the direction of each; one significant endpoint is not "rescue". |
| 6 | **Absence of reporting as evidence of absence** | For each negative, ask whether the assay could have detected it. Unmeasured ≠ absent. |
| 7 | **Symptomatic rescue as disease modification** | Require a disease-course endpoint; seizure suppression is not modification. Check whether the effect appears in wild-type too — if it does, it is not genotype-specific. |
| 8 | **Transferred evidence labelled direct** | Trace each claim to the organism/cell/allele it was measured in; a mouse result about a different allele is transferred. |
| 9 | **Directionality conflicts** | Where two sources disagree in sign, both must be carried; a silent pick is a defect. |
| 10 | **Paper/preprint/publication identity mismatch** | Reconcile DOI/PMID/preprint; confirm the version read is the version cited. |
| 11 | **Unresolved visual/PDF surface treated as adjudicated** | Require `regenerate_adjudications.py verify` — **and, given § 10, require the artifact and locator counts to be re-derived, not read from the summary line.** |

---

## 14 · Verdict

| Behaviour required | Result |
|---|---|
| A — `.jsonl` scanned where `.json` is | **PASS** in both scanners; one unrepaired sibling (§ 5) and one honest-but-omitted population (`benchmark_input_surface.py` `DEFAULT_TEXT_SUFFIXES`, which *names* the omission as `suffix_not_scanned`) |
| B — uppercase blocks in `.md`/`.json`/`.jsonl` | **FAIL** for `⟨OP⟩`; PASS for the other three tokens; the test that appears to cover it does not (§ 7) |
| C — lowercase blocks as tracked path identity | **PASS** on all 57 live cases; **7 terminator forms escape** and one prose form falsely blocks (§ 2–4) |
| D — Italian homonym non-blocking in prose | **PASS** — and re-admitted by the path rule in an Italian slash-pair (§ 2) |
| E — SHA/hex runs raise no identifier findings | **PASS**, verified at the 32-char boundary; 4 live false positives eliminated |
| F — clean files stay clean | **PASS** |

**PRIVACY_GATE_REPAIR_VERDICT = SOUND IN DIRECTION, UNSOUND IN PREMISE.** The repair closes a real
channel and eliminates a real false-positive class. Its stated justification is false, its
terminator set is a list where a grammar is required, the two scanners now disagree on the most
common form of the authorised class, and admitting `.jsonl` to the release gate opened a
false-BLOCK channel on the largest file in the tree.

**I did not modify any scanner.** Every finding here is a measurement; the repairs are the
Operator's to authorise, and three of them are policy questions rather than code.
