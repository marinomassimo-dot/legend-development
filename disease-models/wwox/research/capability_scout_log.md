# CAPABILITY SCOUT LOG — LEGEND

> Non-canonical operational log. Append-only. It tracks capability gaps and contains no
> scientific claims or canonical promotions.

---

## 2026-08-11 — Structured-landing identity parity

### Session Learning Delta

- A complete review read was already attached to `LIT-0333` and `CORPUS P333`.
- The self-evaluation gate scanned both registry files but did not recognise either identifier
  family, producing `ORPHAN_COMPLETE_READ`.
- The failure was in the gate's population definition, not in the scientific landing.
- A single shared identifier predicate now covers every native record family used by the landing
  files, including `LIT-*`, `CORPUS P*` and `CORPUS-STUB-*`.

### Capability Gaps

| Gap | Why it matters for LEGEND | Priority |
|---|---|---:|
| The landing gate's file population and record-ID population could diverge | A valid registry record could be called orphan, encouraging redundant ledger entries or weakening the gate | 5 |
| Source-transmission direction is not mechanically compared with its cited primary | Reviews can invert an intervention or experimental arm while remaining fluent | 3 |

### Candidate Capabilities

| Resource | Type | Gap covered | Case fit | LEGEND fit | Novel | Maturity | Cost/privacy | Action |
|---|---|---|---:|---:|---:|---:|---:|---|
| Shared structured-landing ID predicate plus regressions | gate | Registry/record population parity | 3 | 3 | 2 | 3 | 3 | IMPORT |
| Review-to-primary actor/perturbation/direction audit | mini-procedure | Transmission error detection | 2 | 3 | 2 | 2 | 3 | MONITOR |

### Mandatory Micro-Upgrade

- **Type:** MINI-PROCEDURE / gate improvement.
- **What improved today:** `session_self_eval.py` recognises registry-native structured records and
  has independent regressions for `LIT` and `CORPUS` landings.
- **Why proportionate:** it repairs the exact false failure exposed by this batch without adding a
  new registry, dependency or disease-specific rule.

### Import/Audit Notes

- No external repository, API or plugin was needed; cost and privacy risk are zero.
- The scientific and tooling changes remain separable for merge review.

### Next Micro-Step

- On the next review/primary pair, trial a three-field transmission audit — actor, perturbation,
  direction — before deciding whether it deserves a reusable manifest field.

---

## 2026-08-11 — Wwox mouse-series reading

### Session Learning Delta

- A record-level deduplicator classified PMID 17360458 as integrated because another paper's prose cited it.
- The same false positive survived an exact-PMID score of 100: syntactic exactness did not imply semantic identity.
- A study record needs one explicit identity surface, distinct from citations, claim links and reading debt inside its prose.
- The four-paper read also confirmed that genotype labels in structured HTML must remain the reference when PDF fonts lack ToUnicode.

### Capability Gaps

| Gap | Why it matters | Priority |
|---|---|---:|
| Separate record identity from incidental citation identifiers | Otherwise unread studies can be declared integrated and skipped | 5 |
| Keep a regression with a primary PMID A and cited PMID B | Prevents the same false-negative reading debt from returning | 5 |

### Candidate Capabilities

| Resource | Type | Gap covered | Case fit | LEGEND fit | Novel | Maturity | Cost/privacy | Action |
|---|---|---|---:|---:|---:|---:|---:|---|
| Existing `study_dedup_triage.py` plus identity-field regression | internal skill | Record identity vs prose citation | 3 | 3 | 2 | 3 | 3 | IMPORT |
| External bibliographic entity resolver | service/API | More permissive identity inference | 1 | 1 | 2 | 2 | 1 | SKIP |

### Mandatory Micro-Upgrade

- **Type:** MINI-PROCEDURE / regression.
- **What improved today:** exact identifiers are indexed only from declared bibliographic identity fields; a PMID mentioned only in record prose now remains new/in-pipeline instead of becoming `KNOWN_INTEGRATED`.
- **Why proportionate:** it repairs the exact failure that almost suppressed an assigned first read, without adding a new dependency or changing scientific state.

### Import/Audit Notes

- Targeted test passes, and the real four-PMID triage now returns two corpus placeholders and two queue entries; PMID 17360458 resolves to FT-032 rather than PAPER 057.
- No external repository, API key or sensitive-data flow was introduced.

### Next Micro-Step

- When this tooling commit is merged, rerun the repository's record-convention test with the intake test so field vocabulary and identity semantics cannot drift separately.

---

## 2026-09-09 — `scientist-c`, `AQEILAN-FT-C-001` wave 1 (PMID 20530675, PMID 21731849)

### Session Learning Delta

- A **supplement** retrieved from a paper previously read as partial produced **four** findings, none
  visible from the main text: a table that reverses the direction of the paper's headline
  association, a figure legend that contradicts the paper's own penetrance number, clone/control
  dependence of the functional rescue, and an antibody the Methods never describe.
- Two of four confidence intervals in a printed table were computed on the **negative count** instead
  of the total — reproducible exactly by the paper's own stated method, and one of them lies entirely
  above its own point estimate.
- A **same-lab review** was read as a runnable **citation-fidelity test** because five of its
  load-bearing sources already carry complete-read receipts here. Result: mostly faithful, with four
  specific drifts — including one where abstract and body are correct and only the **Conclusions**
  conflate two assays.
- A **two-column PDF** extracted with `pdftotext -layout` interleaved its columns and put a page
  number **inside** the sentence carrying the headline claim.
- `files/fulltext/` and `files/figures/` were **empty** in the shared checkout, so no prior manifest
  could be verified from bytes.

### Capability Gap

1. To quote safely from a PDF-only, multi-column paper we lacked **any mechanical detector for page
   furniture landing inside a sentence** — the one hazard that produces a locator which *passes*
   verification while matching a sentence nobody wrote.
2. To trust a printed confidence interval we lack **a recomputation check against its own stated
   numerator and denominator**. Two real defects here were found only because the reading did the
   arithmetic by hand.
3. To know whether a checkout can verify its own manifests we lacked a presence check — **closed in
   this same session by `scientist-a`'s `evidence_presence.py`**, found independently from the other
   direction. Recorded as convergence, not as a new gap.
4. To repair a persisted receipt whose **`study_id` is wrong** there is no lawful route at all; the
   ledger now refuses the *correct* DOI because an incorrect one was written first. This is a
   **schema** gap and is the operator's, not an actor's.

### Search Plan and Scoring

**No external search was run and no resource was imported.** The session's constraint was explicit —
no external spend, no API-keyed service — and gap 1 was answerable from inside the repository, which
is the cheaper and more auditable answer. Recorded so the absence is a decision, not an omission.

| Resource | Type | Gap covered | Case fit | LEGEND fit | Novel | Maturity | Cost/privacy | Action |
|---|---|---|---:|---:|---:|---:|---:|---|
| `framework/scripts/text_surface_intrusion_check.py` (built here) | internal script + 7 regressions | Gap 1 | 3 | 3 | 3 | 2 | 3 | **IMPORT** |
| `scientist-a`'s `evidence_presence.py` | internal, peer-shipped | Gap 3 | 3 | 3 | 2 | 2 | 3 | **AUDIT** — landed by a peer today; not re-verified by me |
| A CI recomputation check (Clopper–Pearson vs stated n/N) | proposed internal | Gap 2 | 2 | 3 | 3 | 1 | 3 | **MONITOR** — specified below, deliberately not built |
| `record_kind: identity_correction` for receipts | schema change | Gap 4 | 2 | 3 | 3 | 0 | 3 | **SKIP** — reserved; referred to the operator |
| PyMuPDF / `fitz`, external OCR or layout ML | external dependency | Gap 1, richer | 1 | 1 | 2 | 3 | 2 | **SKIP** — `fitz` is already absent in this environment and a red suite proves it; an ML layout model would also violate rule 5c if its output were ever declared as an artifact |

### Mandatory Micro-Upgrade

- **Type:** NEW INTERNAL CHECK + regressions.
- **What improved today:** `framework/scripts/text_surface_intrusion_check.py` with
  `test_text_surface_intrusion_check.py` (**7/7 PASS**). It reports every span in an extracted text
  surface where page furniture sits inside a continuing sentence — i.e. every span a verbatim quote
  must not cross. Fully **disease-agnostic**: it names no gene, disease or model.
- **Why proportionate:** it mechanises the exact judgement that saved this session's most load-bearing
  quote, and which was otherwise performed by eye against a rendered page.
- 🔴 **It was strengthened by its own first production run, which is the part worth keeping.** Run
  against the PMID 20530675 supplement it reported **chart axis ticks** as page numbers and
  **repeated table rows** as running headers. Both were turned into regressions and the heuristics
  narrowed — a bare integer counts only inside a consecutive numbering chain; a repeated line is
  excluded when it carries table-column gaps. **False positives on that document: 12 → 1.** The check
  was then turned on my own work: of 15 text locators in the `PMID21731849` manifest, **0** span an
  intrusion.

### Import/Audit Notes

- **No external repository, API key, paid service or sensitive-data flow was introduced.**
- Release regressions after the change: the one suite this change reddened —
  `test_scientific_consistency` — was **green again after fixing the science rather than the check**
  (a dossier had collapsed *normal mRNA + low protein* into a turnover mechanism; it now states that
  the pattern locates the loss post-transcriptionally and identifies no route, leaving turnover,
  impaired translation, insolubility and a technical epitope floor all open). The remaining six
  failures are environmental and pre-existing: `numpy` and `fitz` absent, a `master`/`main` fixture
  assumption, and `test_surface_census` failing because `files/` holds no bytes.

### Next Micro-Step

1. **Wire `text_surface_intrusion_check` into `deepdive_manifest.py`** for any locator whose declared
   `artifact` is a PDF-derived text surface, so a quote spanning an intrusion is refused rather than
   merely reportable. **Deliberately not done in the same change that introduced the checker** — a
   detector and the gate that enforces it should not land together, because the first production run
   is what tells you the thresholds are wrong, and it did.
2. **Build the CI recomputation check (gap 2).** Specified concretely so it is not a wish: given a
   table row carrying a count, a total and a printed exact-binomial interval, recompute
   Clopper–Pearson and flag disagreement, plus the cheap invariant that **an interval must contain its
   own point estimate** — which alone would have caught the Total OS row here.
3. **Re-derive the group publication counts** (137/64, carried forward from 2026-08-11) at the next
   wave rather than carrying them a third time.

---

## 2026-09-09 · `scientist-b`, wave 4 of `AQEILAN-FT-B-001`

**Session shape:** one item — pay the wave-3 reading debt on PMID 38499540 by minting a manifest
and a receipt, re-verifying rather than inheriting. `27551470` deliberately **not started**.

### Gap identified

**A declared-effort flag can improve between two edits of the same manifest, and nothing in this
repository would notice.** `deepdive_manifest.py` checks that `multihop.performed` is *present* and
well-shaped. It has no opinion about whether the value is *earned*, and it cannot have one: it sees
one manifest at one instant, with no access to what the previous version claimed. The strict
validator returned **PASS twice** on a manifest in which I had flipped `multihop.performed` from
`false` to `true` while performing no multi-hop work at all.

This is the same shape as `<fig\b` matching `<fig-count>`: **a plausible predicate answering a
different question from the one asked**, invisible to any check that only verifies the result is
well-formed — because the result *is* well-formed.

| Candidate | Kind | Gap | Value | Cost | Risk | Verdict |
|---|---|---|---|---|---|---|
| `manifest_flag_drift.py` — effort-flag drift over git history | proposed internal | this gap | 3 | 1 | 1 | **ADOPT** — built, below |
| A `.pptx` branch in `_artifact_text` + a binary supplement kind | internal, harness | the §7 gap, now wider | 3 | 2 | 2 | **REGISTERED, not built** — see below |
| Enforcing flag-drift as a validator BLOCK | internal gate | this gap | 2 | 2 | 3 | **SKIP** — a detector and its gate must not land together; the first production run is what tells you the rule is wrong, and here it did, twice |

### Mandatory Micro-Upgrade

- **Type:** NEW INTERNAL CHECK + regressions.
- **What improved today:** `framework/scripts/manifest_flag_drift.py` with
  `test_manifest_flag_drift.py` (**18/18 PASS**). It reads a manifest's own git history and reports
  every *monotonic self-improvement* of a declared-effort flag (`multihop.performed`,
  `group_assessment.performed`, `field_density.performed`, `corpus_crossquery.performed`,
  `retraction_check.performed`, and `verbatim_locators.waived` turning off), annotated with whether
  the author wrote anything in that block in the same edit. Read-only, advisory, blocks nothing.
  **Disease- and gene-agnostic:** it names no gene, disease or model.
- **Why proportionate:** it mechanises exactly the defect this session's own self-evaluation caught
  by hand, and which no machine check in the repository could see.
- 🔴 **It was corrected twice by its own production runs, and that is the part worth keeping.**
  - **v1** stayed silent whenever a note *existed* in the block. The `multihop` block of
    `PMID38499540.json` already carried a month-old note about reference numbering, so v1 returned
    **PASS on the exact edit it was written to catch** — while passing 11/11 of its own unit tests.
  - **v2** required the note to be *new or changed* in that revision. The motivating commit had
    changed one — about the **reference count**, not about the flag. **v2 also returned PASS.**
  - **v3 stopped suppressing and started annotating.** No string test can decide whether a note is
    *about* a flag, and tightening one until it caught this case would have manufactured false
    positives that teach people to ignore the output. The design changed instead of the threshold.
  - Both failures are preserved as regressions (`test_a_PREEXISTING_note_does_NOT_silence_it`,
    `test_a_stale_note_does_not_count_as_acknowledgement`) so neither can return silently.
- **First corpus run:** 71 manifests scanned, **3 drifts, 1 unaccompanied by any note** — a usable
  signal-to-noise ratio rather than a wall of findings. Two of the three are on other actors'
  manifests (`PMID24550385`, `PMID42128308`) and were **reported, not edited**.

### Registered and deliberately NOT built

**The `.pptx` gap, and it is wider than wave 3 recorded.** Wave 3 registered that
`_artifact_text` has no `.pptx` branch. Wave 4 found the more basic obstruction: `ARTIFACT_KINDS`
is `{article_binary, article_text, supplement_text, figure, table}` and has **no binary supplement
kind**, so a `.pptx` is declarable only as `supplement_text` — which its own text verification then
refuses. The containers are therefore not merely unreadable, they are **undeclarable**.
Consequence, measured on this paper: the single most consequential sentence of the whole reading —
the authors' note that the t-tests were computed on *fields* and not on *mice* — is carried in the
dossier only, and is **not** mislabelled as a `figure`. **Judged fresh and still not built**: not
for lack of budget, but because the fix needs a schema decision (what kind a binary supplement is)
and this session had already learned twice, in one afternoon, that a rule written to catch the case
in front of you gets its tests written to match it.

### Import/Audit Notes

- **No external repository, API key, paid service or sensitive-data flow was introduced.**
- No canonical current file was touched; no `BATCH_COMMIT`.
- Environment changed in this deployment's favour since wave 3: `tool_preflight.py` reports **6/6**
  tools present (`fitz`, `numpy`, `pdftotext`, `pdftoppm`, `pdfimages`, `git`, `flock`), and `fitz`
  plus `numpy` are what made this wave's independent re-measurement of Fig 3D possible at all.

### Next Micro-Step

1. **Do not gate on flag drift yet.** Let it run advisory across a few waves first; a detector that
   was wrong twice in its first hour has not earned a BLOCK.
2. **Adjudicate the two reported drifts** on `PMID24550385` and `PMID42128308` with their authors —
   both are probably legitimate multi-hop work, which is exactly why the tool asks rather than accuses.
3. **The `.pptx` item needs a schema decision first** (a binary supplement kind), not more code.

---

## 2026-09-09 · `scientist-c`, `AQEILAN-FT-C-001` wave 3 — the screen that returns CLEAN without screening anything

> Discharges the wave-2 capability-scout obligation as well, which was not run because the
> orchestrator scoped that session to landing only.

### Gap found, and it was found the hard way

`deepdive_manifest._refuse_suspect_surface(path, *parts)` is the single most safety-critical screen
in the reading pipeline: it is what stands between a corrupted text layer and twelve verbatim
locators anchored to characters no author wrote. **Its failure mode was a silent pass.** Called with
the arguments inverted — `(text, path_string)`, which is what I did on 2026-09-09 while screening
`PMID 16223882` — it never touches `path` before the loop, dutifully screens the *filename*, finds
no control characters there, and returns normally. The caller reads that as CLEAN.

The surface it was actually being asked about carries **191 C0 control characters** and **zero**
occurrences of `< > ≤ ≥ ± × − µ μ α β γ`, in a paper that prints `P < 0.05` and `β-actin`. The
correct call refuses it.

🔴 **Nothing in this repository would have caught it.** No test exercised the call shape; the
function's own docstring is about what it refuses, not about how it can be misused. It surfaced only
because I had separately counted the raw characters and disbelieved a verdict I had not earned. That
is not a control — that is luck with a good story, and it is exactly the class this log exists to
convert into machinery.

### Micro-upgrade shipped — an argument-shape guard, and its regressions

- `framework/scripts/deepdive_manifest.py`: `_refuse_suspect_surface` now refuses a non-`os.PathLike`
  first argument, and refuses a part that is merely the artifact's own path or filename — the mirror
  image, and precisely what the inverted call ended up screening. Neither check reads the text: they
  check the **shape of the call**, which is the thing that was wrong.
- `framework/scripts/test_suspect_surface_call_shape.py` — **9/9 PASS**, disease-agnostic, no WWOX,
  no gene, no disease anywhere in it.

**Mutation-tested rather than asserted.** Disabling the `PathLike` check turns exactly the two
inversion cases red and leaves the other seven green; restoring it returns 9/9. `test_deepdive_manifest.py`
stays green at **92 tests, OK (1 skipped)**.

**One test exists purely to keep the guard alive.** A guard that produces false positives gets
deleted, so `document_mentioning_its_own_filename_still_passes` pins the narrow form: the comparison
is against the whole stripped part, never a substring, so a real supplement that mentions its own
filename in a sentence still passes.

### Considered and deliberately not built

- **A resolution-route helper** that, given a PMCID, compares the archive's display JPEGs against
  the render PDF's embedded xref streams and reports which route is native. This wave measured a
  **~4× linear** difference on `PMID 41562193` (532×335 archive vs 2085×1313 embedded), and all three
  of that paper's load-bearing findings were unreadable at the archive resolution. It is recorded as
  `DL-METH-110` with the full recipe. **Not built as a tool** because one paper is a sample of one,
  and the honest revival trigger is already written into the ledger entry: an article whose render
  streams come out *lower* than its archive files would show the hierarchy is not general.
- **A needle-selector for page adjudications.** `regenerate_adjudications.py` requires a needle to
  resolve to exactly one span, and a needle that wraps a column break returns one rectangle per line
  and is refused as non-unique — a trap that cost me a full rebuild of twelve crops. A helper that
  picks a valid single-line needle from a sentence would save the next adjudicating reader that loop.
  **Not built this wave**: the correct shape is not obvious after one use, and I have already learned
  in this repository that a rule written to fit the case in front of you gets its tests written to
  match it. Registered here so the next reader who hits it has the diagnosis and not just the error.
- **Wiring `text_surface_intrusion_check.py` into the validator.** Still not done, for the third wave
  running. It is a command run by hand; it ran clean on both of this wave's text surfaces. It is not
  built here because it is a *different* change from this one, and shipping two unrelated upgrades in
  one commit is how a regression's cause becomes unattributable.

### Import/Audit Notes

- **No external repository, API key, paid service or sensitive-data flow was introduced.**
- No canonical current file was touched; no `BATCH_COMMIT`.
- Two growth ratchets improved by this wave's readings and re-anchored (`GA-20260909T144653Z-tighten`):
  registry-only full-text declarations **15 → 13**, unread premises **4 → 3**.

### Next Micro-Step

1. **Wire `text_surface_intrusion_check.py` into `deepdive_manifest.py` for PDF-derived surfaces.**
   Three waves of deferral is one too many, and it is now the oldest open item on this actor's list.
2. **The two receipt-contract findings of this wave are schema decisions and belong to the operator**
   — `first_read` being unrepresentable after a `legacy_reconstruction`, and the panel-relation
   vocabulary being unavailable to adjudicated locators. Neither is code.
3. **Re-measure the resolution hierarchy** on the next paper that has both an archive figure set and
   a render PDF. Two observations is still not a rule, but it is the point at which one is worth
   proposing.

---

## 2026-09-09 · `scientist-c` · `AQEILAN-FT-C-001` **wave 4 — the lot closes**

### Gap found, and it was found in my own tool

🔴 **`text_surface_intrusion_check.py`, shipped by this actor in wave 1, produced 25 false positives
on its second production paper.** `TABLE_ROW_RE` excludes repeated table rows by their wide
inter-column gaps; **PyMuPDF `get_text()` emits one cell per line**, so a table's values arrive as
short repeated lines with no gaps to detect. The wave-1 refinement was not wrong — it was **defeated
by a different extractor's line model**, which is a failure mode no amount of care on the original
document would have surfaced.

**The lesson is about the shape of the guard, not the bug.** A guard keyed to *how one extractor
lays text out* generalises no further than that extractor. The fix is keyed instead to a property of
the **document**: page furniture recurs once per page and is therefore *dispersed*, while table cells
recur densely inside one block. That property survives a change of extractor.

### Shipped

- **Dispersion test** (`HEADER_MIN_SPREAD = 0.25`), threshold chosen by **measuring both classes on
  two real papers**, not guessed: genuine furniture spans **53.7–111.5%** of a document, table cells
  **2.7–7.6%**. Result **28 → 14** intrusions on PMID 18460020, **false positives 25 → 0**, and the
  wave-1 paper (PMID 21731849) **unchanged at 13**.
- **Three regressions** (suite **10/10**), including the counterexample that chose the fix's shape:
  the `|` separator of a running header spans 70% of the document with a **median gap of 2**, so the
  obvious gap-based alternative would have discarded real furniture to remove false furniture.
- 🔴 **A rejected design recorded in the docstring rather than silently dropped.** An absolute line
  floor separated the classes just as cleanly *and silenced the suite's oldest regression*. Recorded
  so the next reader does not re-propose it, together with the ratio's own declared limit (a short
  document where a table honestly exceeds a quarter of the text).

### External scouting — nothing adopted, and the reason is specific

Two candidate routes were considered against this wave's actual friction and **declined**:

| Candidate | Verdict |
|---|---|
| A general table-region detector (heuristic or ML layout model) to replace `TABLE_ROW_RE` | **REJECT for now.** It is the same class of fix that just failed — keyed to layout rather than to a document property — and it would carry a model dependency into a guard whose whole value is that it is cheap and legible. The dispersion test costs four lines and no dependency. |
| Wiley TDM API for the supplement | **REFUSED, not rejected.** It is an API-keyed service; external spend is reserved to the operator. Recorded as a refusal so nobody reads the empty result as "the supplement does not exist". |

### Measured this wave, and worth keeping

- 🔴 **A task contract's acquisition hint can be false, and two repository records caught it before
  any network call**: `corpus_seed_pubmed_20260806.jsonl` carried the PMCID the hint denied, and
  `surface_census.md` recorded a structured surface the pre-flight said did not exist. **The census
  and the seed are usable as an acquisition dissent channel** — they were built for other purposes
  and answered this one. `oa_status_dissent.py` was run first and correctly returned a *negative*.
- 🔴 **`grep -c` as a counting method reported 21 `consolidated baseline` claims where a
  section-aware parse reports 18** — three occurrences are prose inside a CLAIM 004 audit note.
  Rule 4 forbids grep as a method of *analysis*; this is the same hazard pointed at a *threshold
  check*, where a wrong count silently changes whether a review floor triggers.
- **A per-PMID `retraction_check` cannot see the integrity status of the papers a paper depends on.**
  PMID 18460020 is clean and draws its virus and both antibodies from a paper under a standing
  expression of concern.

### Next Micro-Step

1. 🔴 **Wire `text_surface_intrusion_check.py` into `deepdive_manifest.py` for PDF-derived
   surfaces.** **Four waves of deferral.** It is now decisively the oldest open item on this actor's
   list, and this wave supplied the argument for it: the tool caught a real intrusion inside the
   sentence carrying a load-bearing claim, and it did so only because I remembered to run it.
2. **Propose a `Reagent provenance:` field for the paper registry** (`CC-20260909-18460020-01` §1).
   The registry can record that a paper *is* concerned; it cannot record that a paper *descends from*
   one, and a per-PMID check will never surface it.
3. **The two receipt-contract findings remain the operator's** — `identity_correction`, and coupled
   panel relations being unavailable to adjudicated locators. Unchanged, unimplemented, not worked
   around, and now carried across four waves without drift.

---

## 2026-09-09 · `scientist-a`, AQEILAN-FT-A-001 wave 4 (26499798, 31428585 — the lot's last readable papers)

### Micro-upgrade shipped

**`framework/scripts/locator_identifier_provenance.py`** + `test_locator_identifier_provenance.py`
— **12/12, mutation-tested in three directions.**

**The failure it was built from, in one line:** a locator's proposition asserted that reference 1 of
the paper being read was `PMID 29581896`. **The Europe PMC deposit carried the answer in its own
markup** — `<ext-link ext-link-type="pmid">29310447</ext-link>` — and 29581896 is a different paper by
the same author. I had resolved it by external author search and taken the first hit **while the
artefact containing the correct value was open**. Two blind auditors caught it, both by looking where
I had not.

**What the tool asks:** for every identifier (PMID, PMCID, DOI) asserted in a locator's *proposition* —
never the snippet, which the manifest validator already verifies verbatim — *does this value occur in
any artefact the manifest declares?* Buckets: `IN_ARTEFACT`, `DECLARED_EXTERNAL`,
`UNDECLARED_EXTERNAL`, `SOURCE_IDENTITY_UNVERIFIED`. It never claims an identifier is **wrong**;
nothing local can know that. It checks the cheaper property that failed here: whether the reading
**could have got the value from what it says it read**.

### 🔴 Two defects found in my own tool before it landed, and both are kept as tests

1. **The anti-bug tool was immune to the bug.** As first written it would have **missed the exact
   error it exists for**: the offending proposition contained the phrase *"no receipt here"* — a true
   statement about the ledger — and that silenced the check on a *different* assertion in the same
   sentence, that this identifier **is** reference 1 of the source. Provenance is two questions, and
   only one is waivable by a declaration: *"this identifier IS a citation of the source"* is
   adjudicated by the artefact and can never be declared away. `SOURCE_IDENTITY_UNVERIFIED` now
   outranks every marker, and that is **test 1**. `DEFAULTS THAT BIT US` already had the general
   form — *the anti-bug tool is immune to the bug* — and this is that entry paying out.
2. **The first headline number answered a different question.** `files/` is gitignored, so most
   manifests point at bytes that are not in a given checkout; with an empty haystack **every**
   identifier is "not in the artefact". The first run reported a corpus-wide provenance crisis that
   was really an evidence-locality fact. Unmeasurable manifests are now separated, excluded from the
   totals and from `--strict`, and that is **test 12**. Same shape as the `outputs` inverse-index
   trap in the receipt contract: *a plausible predicate that answers a different question, invisible
   to any check that only verifies the result is well-formed.*

### First measurement (2026-09-09, 80 manifests)

| | |
|---|---:|
| manifests | 80 |
| **measurable** (every declared artefact present) | **26** |
| unmeasurable (evidence absent from this checkout) | 54 |
| — over the measurable 26 — `IN_ARTEFACT` | 37 |
| `DECLARED_EXTERNAL` | 4 |
| `UNDECLARED_EXTERNAL` | 15 |
| **`SOURCE_IDENTITY_UNVERIFIED`** | **16** |

**16 identifiers are asserted as citations of a source that does not contain them, on manifests whose
evidence is present.** That is a review surface and **not 16 errors** — the tool's own output says so
in a printed note. It is offered to the orchestrator as a queue, not as a verdict.

### Learned this wave

- **A blind audit's most valuable output can be an omission, not an error.** Both auditors on the
  editorial independently reported a sentence **no locator of mine covered** — a *second* unsupported
  clinical claim, weaker than the one I had built the reading on because it carried no attribution at
  all. A reading is judged not only on whether its propositions are true, but on whether the document
  contains something worse that it walked past.
- **Land the reading before the audit when sessions are dying.** A session limit killed two auditors
  mid-run. The reading was persisted first and **no commit candidate was written until verdicts
  existed**: a landed reading with no candidate touches no claim. Nothing had to be reconstructed on
  resume. This is the repair for wave 2's `[UNAUDITED]` outcome.
- **A wrong value already in an append-only ledger has a lawful remedy and it is not an edit.**
  `receipt_correction` (`FTR-20260909-31428585-02`) carries coverage, depth, timestamps and fingerprint
  over unchanged and changes only the evidence basis.
- **Fetch the figures twice when the obvious route is low-resolution.** PMC's CDN blobs render
  Figure 2B of PMID 26499798 illegibly at 713×398; the same figure is embedded in the PMC PDF at
  2140×1194. The genotype finding of that reading exists only because the second surface was fetched,
  and both are fingerprinted so the choice is visible.

### Next Micro-Step

1. 🔴 **Wire `text_surface_intrusion_check.py` into `deepdive_manifest.py` for PDF-derived surfaces.**
   **Five waves of deferral now.** Unchanged and still the oldest open item on this actor's list.
2. **Triage the 16 `SOURCE_IDENTITY_UNVERIFIED` rows** above. They are one command away and no actor
   has been asked to own them.
3. **The receipt-contract items remain the operator's** — `identity_correction`, coupled panel
   relations for adjudicated locators, and the study-level rollup that leaves 25331887 and 34268881
   partial. Carried across five waves without drift and without being worked around.

## 2026-09-11 — end of the "improve the Scientists" session (orchestrator)

**Environment preflight (§ 3b, host `srv1879784`, Linux 6.8.0-139-generic):** `tool_preflight.py`
6/6 present; PyMuPDF **1.28.2**, now pinned (`requirements-analysis.txt`, `environment-md.yml`);
`unshare` and `bwrap` present, user namespaces usable; `strace` present; `firejail`, `inotifywait`
absent. A verdict below is keyed to this host.

**Session learning delta.** The session built the controls the 2026-09-09 retrospective asked for
and, in doing so, produced its own incident: a mutation harness wrote 54 real dossiers. Three
controls followed — a tracked-file guard in the release runner, a write-refusing tracer in the
meta-test, a `--guarded` runner — and Mirror showed the preventing one is blind to `os.open`, to
shells and to git (`REV-EXPOST-20260911-001` F1d). The gap, precisely: **to run any suite, mutant
or tool against the real checkout we lack a write refusal that does not depend on which Python
call the writer uses.** Second gap, measured twice and instrumented today: numbers quoted into
records (`record_number_provenance.py`, baseline 16 of 71). Third, the operator's: rate-limit
kills — five in two days — with native resume not reaching these sessions (`HARNESS-QUOTA-RESUME-001`).

**Capability gaps.**
1. To exercise a mutated tool against real artefacts we lack a kernel-level read-only view of the
   checkout (MF-1, MF-2).
2. To keep quoted numbers out of records we lacked an instrument — shipped this session.
3. To survive a session limit we lack an in-repo resumer; the operator's audit says the native path
   requires an interactive terminal — MONITOR, theirs.
4. The weekly `HARNESS-SCOUT-<YYYY>-W<WW>.md` channel has still never produced a file (census § 1.1)
   — the Junior's, not this session's; named so it is not forgotten again.

**Candidates, scored (case fit · LEGEND fit · novelty · maturity · cost-inverted).**

| Candidate | What it closes | Score | Verdict |
|---|---|---|---|
| **bubblewrap (`bwrap`)** — `--ro-bind <checkout> <checkout>` with a writable scratch copy for the run | Gap 1 at the kernel: **measured on this host today** — inside `bwrap --ro-bind / / --ro-bind $R $R`, a shell `echo >` dossier, `os.open(O_WRONLY|O_TRUNC)` and `git checkout --` all fail with `Read-only file system`; reads succeed (12,904 bytes); the real tree is clean after the probe. No install, no root, no tracer, no wrapping of Python calls — the write is impossible however it is attempted | 2 · 3 · 3 · 3 · 3 | **TRIAL** → wire as the default for `self_test_coverage.py --guarded` and for `mutate_matrix.py`: positive control is the probe above; acceptance is Mirror's F1(d) fixture refused |
| `unshare -Ur` + bind mounts | same, stdlib-ish; more assembly than `bwrap` | 2 · 3 · 2 · 3 · 3 | `AUDIT` as the fallback where `bwrap` is absent |
| `strace -f -e trace=openat,write` audit of a suite | detection of every write route after the fact, for hosts without namespaces | 1 · 2 · 2 · 3 · 3 | `MONITOR` — `bwrap` prevents, this only records |
| `inotifywait` on guarded trees during a battery | attribution of a concurrent editor's write in real time | 1 · 2 · 1 · 3 · 3 | `SKIP` on this host (absent); the runner's `mtime_verdict` covers the case by arithmetic |
| An in-repo "resume on limit" loop | Gap 3 | — | `MONITOR` — the operator's audit owns it; not this session's to add |

**Micro-upgrades obtained this session** (the mother rule, over-satisfied and listed once):
`screen_verdict.py` and seven screens that say what they screened; `self_test_coverage.py` with a
write-refusing tracer; `attribution_census.py`; `lot_internal_edges.py`;
`locator_contradiction_audit.py`; `dependency_integrity.py` and its manifest slot; `reacquire.py`
with recipes and a tracked retrieval manifest; the runner's tracked-file guard with `mtime_verdict`;
`record_number_provenance.py`; the versioned wrapper; the standing brief v2; four learned gates;
the handoff repair. **The minimal one that is this closing's own:** the `bwrap` measurement — a
capability the host already had, never named, that closes a gap two layers of Python could not.

**What remains to audit.** MF-1 to MF-8 in
`governance/candidates/2026-09-11_mirror_followup_tasks.md`, with `bwrap` now the recommended route
for MF-1/MF-2. **Cost / API / privacy risk:** none — nothing external, nothing installed, no spend.
**Next surgical micro-step:** `self_test_coverage.py --guarded` runs its command under
`bwrap --ro-bind` when `bwrap` is present and says `UNGUARDABLE` when it is not; acceptance is the
F1(d) fixture.

---

## 2026-09-11 (afternoon) — capability scout, `orchestrator`, re-issued Scientist mandate

**Environment preflight (this host):** `git` 2.x, Python 3.12.3, `bwrap` present (measured this
morning), no network call made by any tool landed today; nothing installed, no spend.

**Gaps this session measured, in the order they hurt:**

1. The undeclared in-place locator rewrite had no signal at all until read as a diff — closed today
   for committed history and for the working tree (`de3628b`); still open for a rewrite that
   precedes a manifest's first commit.
2. A relation entry carries no experimental context, so a cross-cell-line bridge (NE-3) is invisible
   to every check — OPEN; the field is specified in the roadmap § 4.
3. Three passing suites were outside the battery — closed in this closing commit.
4. `session_self_eval.py` executes none of the standalone screens (genre, erratum, OA dissent, flag
   drift) — the brief names them; nothing runs them — OPEN, one candidate below.

**Candidates, scored (case fit · LEGEND fit · novelty · maturity · cost-inverted).**

| Candidate | What it closes | Score | Verdict |
|---|---|---|---|
| `git log -p` as the detector's substrate (done) | gap 1: the file cannot show what changed; history can | 3 · 3 · 2 · 3 · 3 | `ADOPTED` (`locator_contradiction_audit.py --history`) |
| `git status --porcelain` as the derivation guard (done) | C22: inputs bound to a commit or refused | 3 · 3 · 2 · 3 · 3 | `ADOPTED` (`derived_inputs.py`) |
| `experimental_context` on coupled relations + WARN on discordant system | gap 2 | 3 · 3 · 2 · 2 · 3 | `TRIAL` next session (3 h; fixture 15070730 Fig 6/5) |
| a `screens` step in `session_self_eval.py` running the four standalone screens over the session's manifests and summing their INSUFFICIENT_DATA/REFUSED | gap 4 | 2 · 3 · 1 · 3 · 3 | `TRIAL` next harness session |
| biomedical relation-extraction models (`MANIFEST.md`, all `DESCRIBED`) to fill `experimental_context` | gap 2 by extraction | 2 · 1 · 2 · 1 · 1 | `REJECT` for this: an extracted value is an unverified value (NE-4's class); the reader authors the field with the document open |

**Micro-upgrade obtained this session (the mother rule):** the three enrolled suites; plus the
tool-level ones listed in the pilot results. **Cost / API / privacy risk:** none.
**Next surgical micro-step:** the `experimental_context` WARN, with 15070730 as the fixture.

---

## 2026-09-21 · Orchestrator · autonomous continuation, end-of-cycle scout

**Environment preflight — the verdict is keyed to the host that produced it.**
`python3 framework/scripts/tool_preflight.py` on host `vm`: **tools 6 · present 2 · missing 4** —
`fitz` (PyMuPDF), `pdftotext`, `pdftoppm`, `pdfimages` all **absent**; `import fitz` raises;
`import numpy` raises. Verdict: *"usable, with 4 optional tool(s) absent … Plans depending on them
will fail LATE unless chosen against now."* Every capability judgement below is keyed to that host.

### 1 · Session learning delta

Nine full-text readings receipted, two bounded censuses, the accessible queue emptied, and the
repository's **`UNREAD_PREMISE` ratchet taken 2 → 0** for the first time. Scientifically the session
was mostly subtractive: the TRAPPC6A independence claim retracted in full; the Chang cascade's first
node shown to disclaim its own load-bearing step; the autophagy sign fixed on abundance but not on
flux; the ketogenic rationale's specific step found to rest, in human cells, on a single transcript;
and a three-line convergence established that **every therapeutic candidate this literature has
produced acts by antagonising WWOX**, which is a category objection for a loss-of-function genotype.

### 2 · Capability gaps, as they actually bit

1. **To read any figure, table or reference list we lack a PDF/image surface entirely** — no
   PyMuPDF, no poppler, no egress. Structural, host-keyed, not closable here. `D-14` absorbed it:
   no figure-asserted negative was adjudicated all day.
2. 🔴 **To know which string counts an artifact can answer, we lacked a measurement and had only a
   prose warning.** The extractor deletes every italicised token. Readers were warned **in every
   brief, nine times**, and one still offered italic-class zeros as evidence. A warning that must be
   repeated nine times is a measurement nobody has written.
3. **To trace a citation we lack the reference list** — it was destroyed in every artefact, which
   structurally blocked the one question two papers were read to answer (*which primaries carry the
   HIF1α arc*).
4. **To stop a delegate's census being read as a statement about this repository we lacked a
   habit** — it cost three corrections in one day.

### 3 · Candidates, scored (case · LEGEND · novelty · maturity · cost-inverted)

| Candidate | What it closes | Score | Verdict |
|---|---|---|---|
| **`extraction_damage_report.py` + 11 regressions (built this session)** | gap 2 and gap 3: measures fused-token scars, empty cross-reference stubs, orphaned statistics and reference-list presence, then emits an **admissibility verdict** per token class | 3 · 3 · 3 · 3 · 3 | ✅ **ADOPTED** |
| **`scoped_record_edit.py` + 16 regressions (built this session)** | makes the narrowness of an operator-authorized edit to an append-only record **executable instead of careful** | 2 · 3 · 3 · 3 · 3 | ✅ **ADOPTED** |
| The census-vs-repository rule, written into the session state with its three worked failures | gap 4 | 3 · 3 · 1 · 3 · 3 | ✅ **ADOPTED** (procedure, not code) |
| Europe PMC `fullTextIdList` / Unpaywall / OpenAlex tiers via `find-fulltext` | gap 1 and gap 3 — the only route to figures and reference lists | 3 · 3 · 2 · 3 · **0** | `MONITOR` — needs egress this host does not have. **Not a tooling gap; a network gap.** |
| PyMuPDF / poppler import | gap 1 | 3 · 3 · 1 · 3 · 2 | `MONITOR`, host-keyed: absent **here**, present on other hosts in this same repository on 2026-09-09. Do not record as a property of LEGEND. |
| A biomedical NER model to recover deleted gene symbols | gap 2 by extraction | 2 · 1 · 2 · 2 · 1 | ❌ **REJECT.** An inferred symbol is a **fabricated** symbol, and the failure being guarded against is exactly a reconstructed identity. The right move is the one taken today: recover the gene from its **expanded HGNC name in roman type**, which the extractor does not touch. |

### 4 · The measurement the new tool immediately produced

Run over the **entire local corpus, 29 artefacts**:

```
artefacts measured: 29
italic-class counts INADMISSIBLE on: 29/29
reference list absent on:            29/29
```

🔴 **This is a corpus-wide property, not a per-paper accident.** Two consequences follow and should
be treated as standing facts rather than rediscovered: **no italic-class zero from any local
artefact has ever been admissible as evidence**, and **no citation attribution has ever been
traceable from any local artefact** — which is why `D-15` verifications in this repository have had
to be done against prose that names a source *in words*, and why `FT-111` exists.

### 5 · Mandatory closing

- **Added:** two tools with their regressions (11 + 16 tests), both routed in
  `framework/scripts/README.md` — `scripts/test_tool_routing.py` went red until they were, twice.
- **Micro-upgrade obtained (the mother rule):** gap 2 converted from a prose warning repeated nine
  times into a one-command measurement with an admissibility verdict, **and immediately used to
  characterise the whole corpus**.
- **Remains to audit:** whether `extraction_damage_report.py` should be wired into
  `session_self_eval.py` so that a receipt over a damaged artefact is *required* to declare the
  admissibility verdict rather than merely permitted to. That is a gate change and goes through
  Plan, not through this session.
- **Cost / API / privacy risk:** none. Both tools are local, stdlib-only, and read files this
  repository already holds.
- **Next surgical micro-step:** the `session_self_eval.py` wiring above, with the 29-artefact run as
  its fixture.

---

## 2026-09-21 — second autonomous run · Orchestrator

**Gap the session actually hit, stated as the session hit it, not as a survey.** This run did not
go looking for capabilities. It found two by being obstructed by their absence, which is the only
kind of capability finding this log should trust.

### Gap 1 — the tool that finds unread gold could not read the registry

`unread_gold.py` exists to prevent one failure (`FM-011`): a paper already on the registry,
correctly triaged, never read, while the model reconstructs its result from scratch. It printed
*"No unread Tier-A / Relevance-HIGH CORPUS"*, which reads as an all-clear. **It was a parse
failure.** Its `tier` selector looked for `**Tier (PHASE 1):**` where the registry writes
`**Tier (FASE 1):**` — **187 records, zero in English**. Its `relevance` selector looked for
`**Relevance:**` where the registry writes `**clinical relevance:**` — **254 records, zero of the
short form**. Both matched **nothing**.

🔵 **This is the repository's own §3 rule turned on its own instrument: a zero from a parser is not
evidence of absence until the parser is shown to be reading the document.** The same sentence was
already written down about PDF extractors and about MCP body text. It had never been pointed at a
LEGEND script.

Parsing correctly is still not enough. Of **164** unread corpus placeholders, **155 are `C`/`LOW`
and none is `A`/`HIGH`** — the FASE-1 triage gave one window one label, so a **tier-gated** filter
can only surface what triage already ranked, which is the one case needing no tool.

And the mechanism lens had a gap in the *question*: it hunted the proteostasis half of the missense
problem (*is the protein there?*) with no term for the other half (*does the protein work?*) — no
`enzym`, `substrate`, `catalytic`, `oxidoreduct`, `dehydrogenas`, `Km`, `cofactor`, `NAD`. Its one
"function" group was `binding|interact|partner|rescue`, **the interaction proxies the SDR-readout
assessment had already rejected as not measuring SDR function. The lens encoded the same blind spot
the science had.**

**What it was hiding:** `PMID 21476439`, the only published measurement of WWOX catalysis, filed as
`CORPUS P306`, Tier C, `background only`, unread since April.

**A second layer, found the same day by a delegate against itself:** a census run *with* catalysis
terms but *without* retinoid vocabulary still concluded the substrate question was "steroids or
nothing" — because its own query terms had no retinoid in them. ⇒ a substrate-class clause
(`steroid|retinoid|retinal|retinol|fatty acid|lipid|prostagland|xenobiotic`) was added for the same
reason one level up. **A lens that names only the class it already suspects will keep confirming
it.**

**Also fixed:** the tool chose what to read next from the registry's `Status` field alone, never
consulting the reading ledger. **19 of 164 placeholders advertised as "never deep-dived" carry
complete- or partial-read receipts.** They are now **annotated, not hidden** — a stale row is a
finding, and dropping it silently would hide one. An unreadable ledger annotates nothing, because
an absent ledger and an absent receipt are different facts.

**Persistence:** `framework/scripts/test_unread_gold.py`, **13 tests, mutation-tested — 5 fail when
the fixes are reverted.** One asserts against the **live registry** rather than a fixture, because
a fixture test would have passed throughout the period this was broken.

### Gap 2 — a number in one canonical file had stopped describing another file

A delegate checked four registry records against their manifests and found three wrong. The full
sweep found **16 of 34**, and the direction is the finding: **every one understates**, deltas
**+2 to +27**. Random transcription error gives both directions; one direction means a systematic
cause — and rules out the frightening reading. The registry is **not** claiming evidence it lacks;
it is **failing to claim evidence it has**.

🔴 **Two of the wrong records carry, in their own text, the sentence saying their declaration was
"reconciled from the ledger" by a named batch.** That batch left both counts wrong, because it
**restated** the declaration instead of **re-deriving** it. That is the whole argument for shipping
the derivation.

**Shipped:** `framework/scripts/locator_count_crosscheck.py` — read-only, routed in
`framework/scripts/README.md`, asking **one** question (*does `N` still equal
`len(manifest["verbatim_locators"]["entries"])`?*) and explicitly refusing the neighbouring ones,
which three other tools already own. **It reports and never edits**, because a tool that silently
corrected a canonical file would become a writer of canonical state — which is what the finding
argues against. `test_locator_count_crosscheck.py`, **10 tests, mutation-tested — 3 fail on
revert**, pinning the dict-versus-list trap, **anti-vacuity** (a scan finding nothing must FAIL,
since a guard with an empty population agrees with nothing), and the **direction** rule.

### The capability gap this run could NOT close, and did not pretend to

**Five structural findings, one shape:** `CLAIM 032`'s unsourced hypomorph · `CORPUS P306`'s tier ·
seven "anchor" papers on no recorded reading · the sixteen locator counts · **29** papers read,
receipted, and never given a `PAPER` record.

> 🔵 **Every LEGEND check verifies a record against itself. Nothing verifies that a thing which
> exists HAS a record.** The ratchets measure honesty *within* a record and are structurally blind
> to the space *outside* one. All five were found **by hand, while chasing something else.**

**No tool is proposed for it, deliberately.** Three instruments already have gaps between them
(harvest ↔ registry ↔ receipt ledger); a fourth would have gaps with all three. The operator's §26
says correct the science and reuse existing mechanism, and the honest answer here is that this is a
**one-time repair plus a reading habit**, not a guard. If it recurs after the ledger rows proposed
this run (`D-18`–`D-23`) exist, *that* is the evidence a guard would need.

**Cost / API / privacy risk:** none. Both tools are local, stdlib-only, read-only, and touch files
this repository already holds. 🔴 One privacy incident is recorded elsewhere and belongs here too:
the **publication gate refused a batch over a living researcher's e-mail address** written into a
public-edition file by a delegate. The gate was right; the address was removed and replaced with a
pointer to where it is published. **That was the only defect this run caught by machine rather than
by hand.**

**Next surgical micro-step:** wire nothing. Read `PMID 30853297` to receipt depth — it carries a
**measured** exon-6 skip, is a `Q230P` primary, and sits under a `consolidated baseline` claim at
abstract depth. The capability this run most lacks is not a script; it is a receipt.

## 2026-09-26 · Harness Engineering · publication monitor

**Reusable gap and evidence.** The daily development-push check treated dirty detached test
worktrees as unpublished actor work. `git worktree list --porcelain` already exposes whether a
worktree has a branch; the check had discarded that distinction. The role contract also
still said `no push`, despite §21d's development-repository exception.

**Change made.** Separate dirty branch worktrees from dirty detached worktrees in the
report, retain both paths, and keep both under `UNPUBLISHED` because detached changes
may be unique.
Correct the stale role pointer. A real-Git regression test covers the classification.
This changes operational monitoring only; no scientific inference or current file changes.

**Cost / API / privacy risk:** none; local Git and standard-library code only.
**Next micro-step:** observe the next scheduled report for its branch and detached lists.

## 2026-09-28 · Scientist · `BATCH_20260928_006` — a scope that MENTIONS closes, and a defect no check could see

**Reusable gap, with the evidence, and it is two gaps that share one lesson.**

🔴 **(1) `growth_anchors` cannot tell a propagation record from a prose mention.** Its backlog is
computed as *candidate files on disk that no disposition record or batch scope **names***. So the first
draft of this batch's `state_history.md` § 4 scope — which named `CC-20260928-A1-RESIDUE-02` inside a
clause reading *"QUEUED AND DELIBERATELY NOT PROPAGATED HERE"* and a peer's
`CC-20260928-WM-HISTORY-SPLIT-01` inside a clause reading *"ROUTED ELSEWHERE, NOT TOUCHED"* — **closed
both**. The backlog fell from 15 to 14 and a **peer's** candidate was closed without its author ever
writing a disposition. The scope said the opposite of what the counter read, in the same sentence.
**Caught by reading the backlog list against what the batch had actually done — by no check.**
*Interim repair, applied:* both ids removed from the scope, replaced by unambiguous descriptions, with
the reason stated **inside the scope itself** so the next author does not re-learn it; the ids live in
the batch report instead. Backlog restored to **16**. *Not wired:* a marker the scope could use to
mention a candidate without closing it (`not_propagated:` / `routed:` keys the matcher subtracts), or a
matcher that reads the clause around the id. That is **harness** and is handed to Harness Engineering;
`designed_for_growth` says correct the record and reuse existing mechanism before adding a guard, and
one occurrence is a repair.

🔴 **(2) A byte-conserving edit is invisible to every proof this repository runs.** `B11`, the finding
this batch repaired, existed for a whole batch cycle because op `B2` **moved** text rather than adding
or removing it: the record-scoped editor's proof that *"every byte outside the addressed records is
unchanged"* held, every presence check held, and `grep -c` on the moved string returned **1** at every
revision. What actually broke was **which paragraph a sentence belonged to** — structure, not content —
and nothing in the toolchain measures that. *Not wired, deliberately:* the candidate instrument would
be a per-record **paragraph-boundary digest** (count and byte-length of each line inside an addressed
record, compared before and after), which `record_scoped_edit.py` could compute for free since it
already partitions the file. It would have turned `B11` from a Mirror finding into a propagation
refusal. **This is the one item here worth building**, and it is a harness change, so it is named for
Harness Engineering rather than attempted from a reading branch.

**Cost / API / privacy risk:** none. Everything above is local, stdlib-only and read-only toward the
four scientific current files; no external retrieval, no spend, no new dependency.

**Next surgical micro-step:** not a script. `L4` is still **OWED** — `CC-20260928-A1-RESIDUE-02` is
written, measured and queued, and `main` carries `CLAIM 026`'s datum with none of its adjudication. The
capability most missing at this moment is a batch that lands it, not a tool.

## 2026-10-03 · Scientist C · intake wave 5 (group C) — a numeric table read from flattened text is silently wrong, and nothing in the toolchain reads one by cell

**Reusable gap, with the evidence, and it very nearly produced a false published finding.**

🔴 **The repository has no cell-aware reader for a JATS table, and the obvious extraction is wrong
in a way that looks right.** Reading PMID 42205472's Table 4 — the only cross-species brain and CSF
volume table in this wave, and the table that would convert any primate dose into a human one — from
the flattened `itertext()` of the `<table-wrap>` returns `Rat2.2200.1519.5`. Adjacent numeric cells
concatenate **with no delimiter**, and that string admits several readings. The one I first took made
the rat's CSF volume exceed the macaque's, and I had drafted a criticism of the source for an
internally implausible cell before re-extracting the table **by cell boundary** from the XML, which
gave `2.2 | 20 | 0.15 | 1 | 9.5` and showed the source is correct and self-consistent. **The defect
was mine.** Nothing would have caught it: the manifest validator checks that a *quoted sentence*
appears in the artefact, and a table is not a sentence; the locator-audit protocol adjudicates
`(proposition | quote | anchor)` triples, and a table cell has no quote to adjudicate.

*Interim repair, applied:* a six-line cell-wise reader was written into the session scratchpad and
used for every table in this wave (PMID 42205472 Tables 4 and 7, PMID 42134074 Table 1, which is the
index of every human intrathecal programme and whose dose and age columns are load-bearing). The
correction and the near-miss are recorded in the dossier, in the analysis note §9 and in
`CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01`.

*Not wired, and this is the item worth building:* the reader itself is trivial — iterate `tr`,
collect `td`/`th`, join with a delimiter — but the **place** for it is `deepdive_manifest.py`, which
already opens and normalises every declared artefact. If a locator could declare
`surface: "table"` with a `cell` address rather than a quoted sentence, a table-derived number would
become checkable by the same command that checks every other locator, and the blind audit would gain
a triple kind it currently cannot express. That is a harness change and is named for Harness
Engineering rather than attempted from a reading branch. One occurrence is a repair, not a gate —
but the occurrence here was a *false criticism of a correct source*, which is the failure mode this
repository is least able to detect, because nothing contradicts it.

🟡 **Secondary, smaller:** PMC serves figure and supplement binaries at
`https://pmc.ncbi.nlm.nih.gov/articles/instance/<pmcaid>/bin/<file>` while the documented-looking
`articles/<PMCID>/bin/<file>` returns **404** for the same asset. `pmc_pow_fetch.py` works perfectly
once given the right URL and solved the proof-of-work page for one supplement, but the path
convention is nowhere written down, and panel-level reading is now effectively mandatory (wave 4's
lesson, and reinforced here: both figures I rendered changed the reading). *Interim repair:* the
working path is recorded in the analysis note §9 and in this entry. *Candidate micro-step:* one line
in `framework/scripts/README.md` next to `pmc_pow_fetch.py`.

**Cost / API / privacy risk:** none. Everything above is local and stdlib-only; the only external
retrieval was free open-access fetching from PMC, with no spend and no new dependency.

**Next surgical micro-step:** not a script from this branch. The highest-value missing item this
wave identified is not a tool at all but a **document**: PMID 42134074's reference 81, the
multi-capsid primate study that triggered the regulatory hold which stopped a human paediatric
intrathecal programme. Every DRG-safety conclusion in this evidence base routes through a study
LEGEND has not read.

---

## 2026-10-04 — `BATCH_20261004_005` (ACTOR_ID `scientist`, Scientist O, batch integrator)

**CHANGE = NONE, and the reason is that the gate already existed and fired.**

🟡 **The gap this batch actually hit** is a cross-registry one: the paper registry and the literature
tracking log have nearly identical field names and **different Status vocabularies**, so a value copied
from one into the other (`not_processed`, which is a legitimate paper-registry stub value) is
`NOT_IN_VOCABULARY` in the log. I wrote exactly that into `LIT-0544`. It cost one cycle and nothing
reached `main`, because **`legend_lint.py` names the defect, the record and the vocabulary table in one
line** — `INVALID_LIT_STATUS: LIT-0544 … is NOT_IN_VOCABULARY against the log's Status vocabulary table
and is not grandfathered`. A gate that catches a mistake at the moment it is made, and says which table
to read, is not a capability gap; proposing a new tool here would add a second mouth for the same
sentence. The durable fix is procedural and is recorded in the batch report's self-evaluation:
**`registry_records.py fields` before writing a record kind this session has not written**, and never
carry a field value across registries because the field name matches.

🔵 **What did not need building, measured rather than assumed.** This batch's four heaviest needs were all
already served: `evidence_presence.py` settled thirteen PMIDs' artefact presence before any audit was
dispatched (0 absent in scope, so the SHA-256 search was not needed); `record_scoped_edit.py blocks`
measured every append anchor and produced **zero** refusals across 23 ops on six files; `registry_records.py
catalog`/`index` caught **nine** collided provisional identifiers and one stale «no landing exists» premise;
and the nine blind locator audits needed no new tooling, only sub-agents, the artefacts and `pdftoppm`.

🟢 **One external observation worth recording for whoever reads next.** The one red release suite the
previous batch named — `test_manifest_receipt_provenance.py`, 18 non-conforming against a ceiling of 15 —
is **green on this tree at 15 of 15**. The repair happened on `main` between batches, the ratchet was not
loosened, and the previous batch's instruction (*re-measure, never raise the ceiling*) is what made that
visible rather than argued.

**Cost / API / privacy risk:** none. Everything in this batch was local and stdlib-only; no external
retrieval, no spend, no new dependency. Two reserved acquisition routes were named and not attempted
(author outreach for the PMID 42397075 supplement; the paywalled PMID 38407561 and PMID 10786676).

**Next surgical micro-step:** again not a script. `DL-MECH-116` now carries, as a written protocol, the
assay specification that would turn *«nobody outside three laboratories has measured a WWOX activity»* from
a measured null into a testable experiment — purified WW2-SDR, a named substrate and cofactor, a YxxxK
catalytic-dead control, a titration. The missing item is the experiment, not the tool.

## 2026-10-19 — scientist-c, task METAB-G3-C-20261019 (group G3)

### Session Learning Delta
- Nineteen manifests built from open copies; panel-versus-text mismatches were common in small-lab primaries.
- A task worktree carries manifests and not the gitignored artefact bytes, so `paper_packet.py check` reported every artefact missing from the worktree.
- Movies and webp figures need decoders that the host lacks by default (ffmpeg via pip, ImageMagick).

### Capability Gaps
| Gap | Why it matters | Priority |
|---|---|---|
| To run `paper_packet.py check` from a task worktree we lacked shared-checkout artefact resolution. | Every Scientist in a worktree gets false "missing artefact" findings. | 4 |
| To read movie supplements we lack a video-decoder entry in `tool_preflight.py`. | A silent absence cost time before a static ffmpeg was installed. | 2 |
| To reach PMC-challenged open copies we lack a written Wayback-PMC route in the find-fulltext cascade. | Used for two papers; undocumented. | 2 |

### Capability outcome (`CHANGE = NONE` is valid)
- **Outcome:** CHANGE-MADE (first gap); the other two GAP-NEW, recorded.
- **Evidence:** the packet check failed from the worktree on this task's own manifests before the change and passes after it.
- **If a change was made — type:** CONNECTION
- **What improved and why it is proportionate:** `paper_packet.py` now defaults the validator job's artefact root to the shared checkout from a linked worktree when no `--artifact-workspace` is given (a peer added the explicit flag the same day; this is the default beneath it); two regression tests in `test_paper_packet.py` pin it. Host: Linux desktop, poppler 24.02.0, ImageMagick present, ffmpeg absent by default.

### Next Micro-Step
- Add a video-decoder line to `tool_preflight.py` with its test.
---

## 2026-10-19 — scientist-b, metabolic batch G2 (task `METAB-G2-B-20261019`)

**Capability gap that emerged (with evidence).** An identity defect the pipeline had no test for: PubMed's record for PMID 31145772 joins the title and abstract of one 2019 article with the authors, DOI and page range of a different 2021 article. Following the stored DOI at the publisher served the wrong PDF (1,979,803 bytes; sha256 `0d1d2ed323fe4cdbf74dd5a7ceac15664469c4b23bb5afc730792d80f96e9694`); the selection file carried the wrong first author; the receipt validator's DOI rule would have bound a reading of the right article to the wrong DOI. Found by reading the PDF's title page, not by a check.

**CHANGE (proportional micro-upgrade, shipped).** `framework/scripts/pubmed_identity_check.py` compares PubMed's title and first author with Crossref's record for the DOI PubMed stores and returns a record naming both identities (MATCH, TITLE_MISMATCH, AUTHOR_MISMATCH, NO_DOI, CROSSREF_UNAVAILABLE; exit 1 on anything but MATCH). Offline suite `framework/scripts/test_pubmed_identity_check.py` (4 tests), enrolled in `scripts/run_release_regressions.py`, routed once in `framework/scripts/README.md`. Calibration, live, 2026-10-19: 17 PMIDs of this lot, 16 MATCH, 1 TITLE_MISMATCH (the known hybrid), zero false positives. Use it at M1 before acquiring a body by DOI.

**Not built, and why.** A corpus-wide sweep of every registry PMID with this tool (about 900 Crossref calls) was not run in this batch; it is a one-line loop over the new tool and is left to the Orchestrator's discretion. A receipt-writer rule on DOI/PMID identity was not added: the brief requires the receipt DOI to equal the DOI PubMed carries, which is exactly the DOI the hybrid record gets wrong, so the rule needs an `identity_correction` decision that is not mine to make.

**Cost / API / privacy risk:** none; NCBI eutils and Crossref, no key, no spend. Four Scientists share one NCBI rate limit (HTTP 429 seen once); the tool retries with back-off.

**Next surgical micro-step:** run the tool over the registry PMIDs that carry a DOI and queue every non-MATCH for identity review.

## 2026-10-19 — scientist-d, metabolic batch group G4

**Capability gap recorded (with evidence).** Two, one closed and one named.

1. **Closed (shipped, `CHANGE` made):** `paper_packet.py check` could not validate a manifest from a task worktree, because the worktree holds the manifest but not the gitignored `files/` tree, and the packet's runner did not pass the validator's existing `--artifact-workspace`. Evidence: with `files/` absent the manifest check returned `No such file`; with `files/` a symlink to the shared tree it returned `artifact path escapes the workspace`. Fix: `check --artifact-workspace <root>` passes the root through. Regression: `ArtifactWorkspacePassthroughTests` in `framework/scripts/test_paper_packet.py` (69 tests, OK). Cost: one optional argument, no dependency.
2. **Named, not built:** the manifest validator proves that a quote exists in the body surface, not that it supports the proposition written beside it. In this wave the reader's re-reading caught seven propositions that outran their quotes before they were committed (incident D of `session_evaluations/2026-10-19_metabolic_G4_scientist-d.md`); no machine saw them. A mechanical aid is plausible and cheap to try: print each proposition beside its quote and the words of the proposition absent from the quote, as a prompt to the reader, never a gate. It is a heuristic and would produce false alarms on paraphrase, so it should be measured against the 4,319 locator entries counted on main on 2026-10-19 before anyone treats it as a control. Not built here because the sample of one wave cannot show its false-alarm rate.

**What did not need building.** The strict manifest validator, the dependency screen (`--manifest-block`), `registry_records.py` and `record_scoped_edit.py` (dry run on `CLAIM 001`) each worked first time.

**Cost / API / privacy risk:** none. The parked pair's open-access PDFs were refused by two publishers; no Unpaywall query was sent because it requires an e-mail address and the operator's may not be used for it without being asked. No shadow-library route was used.

**Next surgical micro-step:** run the proposition-versus-quote prompt over the existing manifests offline and count what it would have flagged.

## 2026-10-19 — scientist-b, interventions wave group H3

**Capability gap recorded (with evidence).** A Scientist staging receipts under the parallel-wave rule has no read-only way to validate them: `fulltext_receipts.py record` rewrites the hash chain and state manifest, and `validate` takes no receipt argument. Two waves wrote the same ad hoc script from the module's own validators.

**CHANGE (proportional micro-upgrade, shipped).** `framework/scripts/staged_receipt_check.py` runs the writer's own `validate_new_receipt` and `validate_receipt` over staged JSON files with an explicit artefact root and appends nothing; test `test_staged_receipt_check.py`; README routing row; release-regression enrolment. All 15 receipts of this wave return OK.

**Not built, and why.** An automatic proposition-versus-quote check (named by scientist-d) and a figure-file-to-label mapper (Dhillon: 11 PMC files in non-figure order) were not built; each is larger than a micro-step.

**Cost / API / privacy risk:** none; offline.

**Next surgical micro-step:** map PMC image files to figure labels from the JATS `fig` and `graphic` elements and warn when file order differs.
---

## 2026-10-19 — scientist-d, interventions batch group H5

**Capability gap recorded (with evidence).** Two, one closed and one measured.

1. **Closed (shipped, `CHANGE` made):** `deepdive_manifest.py` refused a well-formed `contradicts_locator` declaration whose prior manifest existed only on the task branch, with "is not a file under the workspace", because the prior manifest was looked up under the artifact root (the shared evidence checkout) alone. Evidence: 25 declared revisions of this branch's own manifests were refused; after the fix (look beside the manifest being validated first, then fall back to the artifact root) all eight affected manifests PASS from the task worktree with `--artifact-workspace` pointing at the shared checkout. Regression: `test_the_prior_manifest_may_live_in_the_branch_workspace_not_the_artifact_root` (205 tests OK).
2. **Measured, not built:** last wave named "the validator proves a quote exists, not that it supports the proposition". This wave measured it. Two blind auditors over 101 load-bearing triples returned 23 non-SUPPORTED (9 overshoot, 14 undershoot; 23%) while the validator, the receipt validator and the contradiction audit were all green. The pre-commit self re-read caught none of these 23. A plausible cheap aid: print each proposition beside its quote and list the proposition's number-bearing and quantifier words that occur nowhere in the quote or its two neighbouring sentences. A second small gap of my own: the text renderer I used skipped floats placed outside body sections (a 22-row table and figure legends); a `table-wrap` and `fig` count against the rendering would have flagged it at once.

**What did not need building.** `paper_packet.py check --artifact-workspace` (last wave's upgrade), the strict manifest validator, the dependency screen and `locator_contradiction_audit.py` each worked first time; the blind-audit method needed only a triples file and two agents.

**Cost / API / privacy risk:** none. All retrieval was Europe PMC REST and the PMC open-data bucket; no spend, no key, no new dependency; the auditors read local files only.

**Next surgical micro-step:** run the word-overlap aid over the existing manifests offline and compare what it flags against the 23 known cases.

---

## 2026-10-19 — scientist-a, metabolic batch G1 (task `METAB-G1-A-20261019`)

**Capability gap that emerged (with evidence).** The `--artifact-workspace` passthrough shipped by scientist-d the same day has a trap. `paper_packet.py check` builds the validator command with the value as typed, and the child process runs from the repository root, so a relative value typed inside a task worktree (`--artifact-workspace .`) names the worktree, not the shared checkout. Evidence: the run for one of this lot's manifests returned 10 BLOCK lines of the form `No such file or directory: <worktree>/files/fulltext/...` and four `artifact does not exist` lines, indistinguishable from missing evidence; the same command with an absolute path returned PASS for all fifteen manifests.

**CHANGE (proportional micro-upgrade, shipped).** `framework/scripts/paper_packet.py` now resolves the value to an absolute path against the invoker's working directory before it builds the command. Regression: `ArtifactWorkspacePassthroughTests.test_relative_workspace_is_resolved_against_the_invoker_not_the_child` in `framework/scripts/test_paper_packet.py` (the file is already in the release battery; the suite passes, 70 tests, 19 skipped for absent local corpora).

**Named, not built.** (1) Every spreadsheet, old `.doc` and aggregate-table derivation in this lot (xlsx cell dump, GNU strings of a legacy document, mean and fold-change recomputation) was a one-off script, and a hand reading of truncated digits once produced a false up-regulation before a script on full values reversed it. A small shared "derive and cite" helper (full values in, derivation file out, the manifest recipe pointing at it) would remove the temptation to read printed numbers; the shape is clear but the three derivation types differ enough that one tool would be speculative. (2) The `legend_commit.sh` pathograph-staleness refusal fired on every commit of a new manifest (15 times) and was bypassed each time with the dispatch brief's stated reason; a per-actor batch flag would shorten this, but the bypass reason is itself the audit trail and was kept.

**Cost / API / privacy risk:** none. The auto-mode classifier refused one dry-run of `record_scoped_edit.py apply` against the shared registry; the op list was shipped in the candidate with the refusal stated and the `old` string verified by a count in the branch's own file.

**Next surgical micro-step:** none required; the integrator dry-runs the DL-MECH-012 op list before applying.

## 2026-10-19 · scientist-d · DEBT-WWOX-DIRECT-D-20261019

**Gap (with evidence).** `pubmed_identity_check.py` reported TITLE_MISMATCH for PMID 17567906, a clean record, because for an article with no `ELocationID` it fell back to the last `ArticleId` of the whole efetch record, which sits in the reference list and is a cited paper's DOI. A false mismatch sends a reader hunting for a hybrid record that does not exist; the same defect in the other direction would pass a hybrid.

**CHANGE (proportional micro-upgrade, shipped).** `fetch_pubmed` now reads only `MedlineCitation/Article/ELocationID` and `PubmedData/ArticleIdList`, first match. Regression `test_doi_comes_from_the_article_not_its_reference_list` in `framework/scripts/test_pubmed_identity_check.py` (5 tests, OK). Disease-agnostic.

**Named, not built.** (1) PMC pages for author-manuscript deposits (Europe PMC XML returns HTTP 500) were reachable only through an Internet Archive capture of the PMC page plus the figure blobs it names; this route worked five times and is not written down in `find-fulltext`; a short tier entry would save the next actor an hour. (2) Three free-to-read papers are blocked by publisher bot challenges (no browser tool in this session); a browser-capable retrieval tier is an operator-side capability, not a script.

**Cost / API / privacy risk:** none; no keyed API, no paid or unauthorised source.

**Next surgical micro-step:** add the archived-PMC-page route to the `find-fulltext` skill's Tier 0 notes.

## 2026-10-20 · scientist-d · DEBT-WWOX-DIRECT-D-20261019 wave 2

**Gap (with evidence).** Three recurring acquisition failures, each costing a reading to rediscover: (1) Europe PMC `fullTextXML` returns HTTP 500 for author-manuscript PMC deposits; (2) ImageMagick `convert` crashes ("double free") on several PLOS and PMC supplementary TIFFs; (3) the PMC supplementary file for one article was another article's, and the article's own supplement sat on the publisher's page.

**CHANGE (proportional, shipped as a log entry; no code).** Routes that worked: (1) the Internet Archive capture of the PMC page, `https://web.archive.org/web/2025id_/https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/` (raw bytes, redirect gives the exact timestamp to record), with figure blobs fetched from the `cdn.ncbi.nlm.nih.gov/pmc/blobs/` URLs named in it; (2) `fitz.open(tif)[0].get_pixmap(matrix=...)` from PyMuPDF renders those TIFFs (the PDF-points page rect must be scaled up, since the TIFF dpi makes it small); (3) when a deposit's supplement does not match the article, follow the article page's own supplementary link on the publisher's site (here a `media.springernature.com` ESM URL) before declaring the supplement unretrievable.

**Named, not built.** A short "author-manuscript PMC" tier in `find-fulltext` and a `render_tiff.py` helper; both are two-hour jobs with a clear shape and a test (a TIFF fixture) and would pay back at the next supplement read.

**Cost / API / privacy risk:** none; no keyed API, no unlawful source.

**Next surgical micro-step:** add the archived-PMC-page route and the publisher-ESM check to the `find-fulltext` skill's Tier 0 and Tier 8 notes.
---

## 2026-10-20 — scientist-b, gold wave (task `GOLD-LEGACY-WWOX-B-20261019`)

**Capability gap that emerged (with evidence).** Re-acquiring absent artefacts was repeated by hand for ten papers: eutils esummary for the PMCID, efetch XML, then the PMC open-data bucket listing for figures, supplements and PDF, with the same traps each time (PMC web pages serve a reCAPTCHA; efetch returns a 7.6 kB stub with a publisher comment when XML is forbidden; author-manuscript figures are not in the bucket). One restricted stub was nearly taken for a text; one XML re-fetched four weeks later was byte-identical to the earlier copy (42422765), another differed by digest (39507621), so digests must be recorded per fetch.

**CHANGE (proportional micro-upgrade, shipped).** `framework/scripts/pmc_bucket_fetch.py` does the sequence once, never overwrites, writes only under files/, reports route, HTTP status, size and SHA-256 per file, and returns exit code 2 with `xml_state: restricted_stub` for a stub. Offline suite `framework/scripts/test_pmc_bucket_fetch.py` (stub versus full, bucket-key classification, no-overwrite), in the release battery; routed in `framework/scripts/README.md`. A first draft classified any `<restricted-by>` front-matter tag as a stub and mislabelled a full text; the live smoke test on a known-full paper caught it and the rule was removed.

**Named, not built.** (1) A manifest re-point tool: nine re-reads needed the same operation (map absent artefact names to new files, drop declared-absent artefacts, append locators, declare path-only changes); done by a scratch builder in this run. (2) Absent derived renders (PDF pages at fixed dpi) are regenerated with new digests; a convention for recording "same page, same dpi, new digest" in the artefact note would stop each reader inventing wording.

**Cost / API / privacy risk:** none; no key, no paid service, no personal address sent.

**Next surgical micro-step:** none required.

---

## 2026-10-20 · scientist-d · W4-W2B-D-20261019 (wave 4, group W2 second half)

**Gap (with evidence).** Three of eight papers read in wave 4 had publisher figure files whose numbering or whose attached image did not match the legend: one deposit's file `g002` was Figure 1; one deposit's `g003`, `g002`, `g004`, `g001` were Figures 1 to 4; one deposit showed the symptom timeline under the "Figure 1" caption (a bile-acid pathway legend) and the pathway under "Figure 2". A panel reading attached by file name or page order would have carried the wrong legend, and no tool can detect it because only the image content says which legend it belongs to. Separately, two 2026 deposits had no Internet Archive capture and one had no Europe PMC XML.

**CHANGE (proportional micro-upgrade, shipped as protocol text; no code).** `framework/protocols/scientist_operating_practice_v1.md`, Phase 5, gained two bullets: the figure-numbering trap with its three measured instances and the rule (open every image, match it to its legend by content, write the mapping in the artefact note), and the 2026-deposit routes (Europe PMC `fullTextXML` and `supplementaryFiles` ZIP; the PMC article page fetched with an empty User-Agent; `convert x.webp x.png` for WEBP). These are the routes this wave used, each recorded in the manifests' `acquisition_recipe`.

**Named, not built.** A `figure_legend_pairs.py` helper that lists, per figure file, the neighbouring caption and its dimensions would shorten the matching step but cannot decide it; the image still has to be opened. The route notes from wave 2 (archived-PMC-page tier in `find-fulltext`) are still not in that skill because `.claude/` writes need the operator's authorisation.

**Cost / API / privacy risk:** none; no keyed API, no unlawful source, no personal address sent.

**Next surgical micro-step:** none required beyond the protocol text.

---

## 2026-10-20 — scientist-b, wave 4 group W1 (task `W4-W1-B-20261019`)

**Capability gap that emerged (with evidence).** `staged_receipt_check.py` runs the writer's validators on a staged receipt but nothing compares `study_id.doi` with the DOI PubMed stores. In this wave one receipt and its manifest carried a DOI written from memory (the last character wrong) and passed the receipt validator, the manifest validator and the paper-packet checks; it was found only because the fetch record printed by the acquisition tool was compared by eye. The standing brief says an identifier comes from the artefact or a command; no tool enforced it for the DOI.

**CHANGE (proportional micro-upgrade, shipped).** `framework/scripts/staged_receipt_check.py --check-doi` fetches the DOI PubMed stores (esummary, no key, no User-Agent) and refuses a receipt whose DOI differs, and reports (does not hide) a PubMed read failure as unverified. Regression: `DoiCheck` in `framework/scripts/test_staged_receipt_check.py` (matching DOI passes, a last-character mismatch is refused, an unreadable PubMed answer is not silence). The eleven receipts of this wave all pass it. Rate-limit note: running the check over thirty receipts in parallel made some PubMed reads fail; sequential with a one-second pause is clean.

**Named, not built.** (1) A shared first-read manifest builder: two waves wrote the same private scratch builder (artefacts with SHA-256 and recipes, locator verification, retraction dependencies with citing relations, receipt JSON); (2) a reference-debt classifier (gene-direct references of a source against manifests and receipts).

**Cost / API / privacy risk:** none; no key, no paid service.

**Next surgical micro-step:** none required.

## 2026-10-20 (orchestrator, metabolic batch)

- **Gap:** the trial-then-record procedure for staged receipts was a hand sequence repeated seven times, and its first form (a symlinked evidence tree) failed for a reason unrelated to the receipts.
- **Change:** `framework/scripts/record_staged_receipts.py` (dry run by default, `--apply` records, never commits), with `test_record_staged_receipts.py`, a routing row and release-regression enrolment.
- **Not built, named:** a one-command regeneration of the four ledger-derived surfaces with the dirty-input reason filled from the staged actors; a Mirror-side check that a harness brief's "must not change" list is honoured by the diff.

## 2026-10-20/21 — scientist-a, drug-repurposing P3 known-roads reconnaissance (task `REPURP-P3-KNOWNROADS-A-20261020`)

**Capability gap that emerged (with evidence).** `dependency_integrity.py fetch` cannot ingest a current Retraction Watch snapshot. The download succeeds and the pin build then dies with `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x92 in position 6514` — a Windows-1252 right single quotation mark inside a title field. Three call sites open that CSV with a bare `encoding="utf-8"` (`count_rows`, `load_index`, and the staleness path). Consequence measured in this task: the held snapshot can never be refreshed, so both new manifests carry a dependency block whose snapshot is 41 days old and ageing, and the staleness is invisible except inside each block. The fix is `errors="replace"` (or a `cp1252` fallback) on those opens; DOIs are ASCII so the index is unaffected and only the odd title character is substituted.

**CHANGE (proportional, deliberately NOT a code edit).** The defect is **reported with its exact patch location** rather than patched, because editing a shared `framework/scripts/` file mid-task while a Harness agent is active in the tree is a coordination risk out of proportion to the defect. What shipped instead is the operational finding, recorded in the task record's `DEFAULTS_TAKEN` and in the self-evaluation: **`dependency_integrity.py screen` fails closed from a task worktree** (`snapshot absent`) because `files/` lives only in the shared checkout, and the correct invocation is from the shared checkout root with `--manifest-dir` pointing at the worktree's manifest directory. Both screens then returned `SCREENED_CLEAN`. Failing closed rather than reporting clean is the gate working as designed and is not the defect.

**Named, not built.** (1) A second-reader rule for locator fidelity: the manifest validator catches a stitched quote (two verbatim spans joined by an ellipsis, not verbatim as a whole) but nothing catches it at the moment of typing, and it is the one defect class in this task that would have put a locator in the record looking verified. (2) An origin-deduplication helper for therapy censuses: two drugs that are two arms of one figure are not two studies, and nothing in the toolchain surfaces that two PMIDs-worth of therapeutic evidence share one experiment — in this task lithium and ethosuximide were about to be counted twice.

**Cost / API / privacy risk:** none; no key, no paid service, no external spend.

**Next surgical micro-step:** the three-line encoding fix above, for Harness Engineering, with a regression that feeds `load_index` a row containing byte `0x92`.

## 2026-10-21 — scientist-b, early-benefit axis (task `REPURP-P3-EARLYBENEFIT-B-20261020`)

**Capability gap that emerged (with evidence).** This repository writes *instrument and modality
negatives* — "no WWOX paper uses this scale / this imaging modality / this electrophysiological
test" — and it has no discipline for the surface such a negative is a negative **of**. Measured
here: a PubMed probe for `WWOX AND ("visual evoked potential" OR electroretinogram OR DTI OR
"magnetic resonance spectroscopy" OR volumetry)` returns **0** (2026-10-21), and the full text of
a WOREE case series read the same session carries a **visual evoked potential** in a patient and a
**sleep study** that detected apnoea with hypopnoea, both in a Discussion paragraph and a
phenotype table. A title-and-abstract index cannot see an instrument used once in a five-patient
series, which is the normal case in a rare disease — so the probe's zero was about **indexing**
and the draft sentence about it would have been **false**. The cost class is the one
`epistemic_discipline` § 2 names as the expensive one: a false negative is silent, permanent and
self-reinforcing, and this one would have discouraged the very sweep that disproves it.

**CHANGE (proportional micro-upgrade, shipped).** The rule is written into the one place the
re-audit rule of `epistemic_discipline` § 2.3 points at — row **`D-37`** of the `DEFAULTS THAT BIT
US` table in [[dismissal_ledger_current]], with its detection rule ("say which surface the zero is
a zero of") and the measured counterexample. Shipped as a row, not as a promise, and the three
instrument negatives in
[`repurposing_early_benefit_20261020_scientist-b.md`](repurposing_early_benefit_20261020_scientist-b.md)
§ 2 are written in the bounded form the row requires, each with its dated query.

**Found while allocating the id, and reported rather than fixed:** `D-31`, `D-33`, `D-35` and
`D-36` are cited as detection rules in `discovery_ledger_current.md` and
`full_text_queue_current.md` and exist in **no row** of that table, while the table's own
allocator note reserves `D-27`–`D-30`. So `max(D-nn) + 1` as the note prescribes would have
collided with a live reference; `D-37` was allocated instead and the deviation is stated in the
row. The four dangling ids belong to other actors' records and were not touched.

**Named, not built.** (1) A full-text instrument sweep over the WOREE case literature's bodies and
tables — it would convert three indexing negatives into measured ones and is the cheapest decisive
move this axis produced; (2) a check that an id cited as `D-nn` anywhere in the research layer
resolves to a row of that table, which is the generic form of the dangling-reference finding above
and the same defect class as `D-22` (two surfaces, one fact, never compared).

**Cost / API / privacy risk:** none. Key-less PubMed reads only; no paid service, no new dependency.

**Next surgical micro-step:** none required to close this gap; the sweep in (1) is scientific work
for a future task, not a harness change.

---

## 2026-10-21 · `scientist-c` · `REPURP-P3-RESCUEREF-C-20261021` — the packet knows which surfaces exist and does not say which is best to read

**GAP (reusable, disease-agnostic, named with its evidence).** `paper_packet.py packet` lists
artefacts that are **present on disk and undeclared** — for PMID 42422765 it listed the publisher
PDF and all seven r2 figure files — and it is the one command a reader runs before opening
anything. It does not rank those surfaces for the act about to be performed. So a reader who
wants a figure learns that fourteen files exist and not that one of them is 2.4× better than the
one habit reaches for.

**Measured, this session.** Every one of the sixteen figure attestations persisted for this paper
rests on 726 × 708-class PMC CDN JPEGs described in the manifest as *"read at 104 effective ppi"*.
The publisher PDF, on disk and undeclared since 2026-10-19, carries the same figures as **300 dpi
embedded rasters** (Figure 3: 1744 × 1699). The adjudication this task was dispatched for — a
survival panel whose printed axes had to be read to the day — was impossible to do honestly at the
lower resolution and routine at the higher one. Nobody chose the worse surface; nobody compared
them, because nothing asks.

🔴 **And the second half of the gap is the one that bites silently.** Choosing *"extract the
embedded image"* as a rule would have been wrong for exactly one of this paper's eight figures:
**Figure 7's quantitative panels are vector**, its only embedded raster is 759 × 515 and carries
the ECoG traces alone. An extracted-image read of Figure 7 returns a surface with **no numbers on
it at all**, which a careful reader would plausibly write up as *"panel unreadable"* — a false
negative about an endpoint family, from a correct-looking method. What detected it here was an
aspect-ratio comparison: seven of eight figures matched a PDF image to within 0.002, Figure 7 was
off by 0.18.

**CHANGE = PRACTICE, shipped where the next reader of this paper will meet it, not as a tool.**
Before a figure is read, `pdfimages -list` on any publisher PDF held for the paper, with each
embedded image's aspect ratio compared against the CDN rasters. One command; two answers no
existing check asks — *is a better surface available*, and *is this figure vector*. It is written
into §0 of
[`drug_repurposing/woree_rescue_reference_scaffold.md`](drug_repurposing/woree_rescue_reference_scaffold.md)
and into the artefact notes of `deepdive_manifests/PMID42422765.json`, where the pairing rule and
the Figure 7 exception are stated with their measurements.

**Named, not built — deliberately, and the reason matters.** A `paper_packet.py` sub-command that
ranks figure surfaces (resolution, vector-versus-raster, aspect-ratio pairing against the declared
figure files) is the generic fix and it is **Harness Engineering's to build, at T0, not a
Scientist's to improvise mid-adjudication**. It is proposed here with its acceptance test already
available: run it over PMID 42422765 and it must prefer the publisher PDF for Figures 1–6 and a
**page render** for Figure 7, for the stated reason. A tool that returns the embedded raster for
Figure 7 has reproduced the defect this entry exists to prevent.

**Cost / API / privacy risk:** none. Local poppler-utils 24.02.0 only; no network, no paid
service, no new dependency, no patient-level material.

**Next surgical micro-step:** Harness Engineering triages the ranking sub-command above against
the acceptance test named; nothing in the scientific layer waits on it.

---

## 2026-10-21 · `plan` · `PLAN-LOCATOR-COUNT-CHECK-20261021` — for PMID 42422765 the best figure surface is the SUPPLEMENT, not the publisher PDF, and it is 500 ppi

**CHANGE = NONE (no tool, no gate, no registry). A MEASURED FACT, recorded where the next reader
of this paper will meet it**, because the entry above fixed an acceptance test on a premise that
measurement does not support, and a reader who follows it reaches the second-best surface.

**What the entry above specified:** *"run it over PMID 42422765 and it must prefer the publisher
PDF for Figures 1–6"*. `paper_packet.py rank` was built to that test and then measured the
surfaces instead of assuming them. It does not prefer the publisher PDF. It ranks
**`mmc2.pdf`** first, and the figures it is asked about are in there.

**Measured 2026-10-21 by `paper_packet.py rank --pmid 42422765` (PyMuPDF geometry, each ppi against
the printed width it was measured at — 103 figure-bearing candidates on disk, 0 not rankable):**

| candidate surface for Figures 1–6 | what it holds | measured |
|---|---|---|
| `files/supplement/PMID42422765/mmc2.pdf` pp. 3, 4, 6, 7, 9, 10 | embedded rasters 3321×3280, 2906×3769, 2906×2832, 2906×2875, 2906×3052, 2906×2695 | **500 ppi** (printed 418–478 pt wide) |
| `files/supplement/PMID42422765_r2/PMC13343157.1.pdf` pp. 4, 6, 7, 9, 10 | the SAME whole figures, embedded 1744 px wide | **300 ppi** (printed 418 pt) |
| `files/fulltext/figures/PMID42422765/gr1.jpg` … `gr6.jpg` | the PMC CDN web assets, 726–738 px wide | **111–125 ppi** |

`rank` pairs them by aspect ratio and says so in one line each — *"pairs with `gr1.jpg` to 0.0002
relative — the same whole figure at higher resolution"* — so this is the same figure at three
resolutions, not three different things. **1.67× over the publisher PDF, 4× over the CDN JPEGs.**

**`mmc2.pdf` is on disk in three places, byte-identical, sha256
`523b09e47b52620cacda9826bce88ac77dd8de65626f5148e2c8630383869cb4`** (25 838 791 bytes):

  - `files/supplement/PMID42422765/mmc2.pdf`
  - `files/supplement/PMID42422765_r2/mmc2.pdf`
  - `files/fulltext/PMID42422765_Obeid2026_assets/mmc2.pdf`

Three copies, since 2026-09-28 for the first two, and **nobody had compared them with anything.**
`rank` collapses 11 byte-identical duplicate surfaces for this paper to one row each, so the
duplication costs a reader nothing — but it also means the 500 ppi surface was present and unread
on three paths at once while every figure attestation for this paper rested on 104–125 ppi.

**No adjudication is withdrawn and none needs redoing.** A Scientist adjudicated a claim on these
figures at 300 dpi two hours before this measurement; a blind auditor cross-checked its waypoints
against the **printed axes**, which is resolution-independent, so the verdict stands on its own
evidence. What changes is only the choice the NEXT reader makes. That adjudication, its manifest
and its dossier belong to their authors and are untouched by this entry.

**THE RULE, one line:** `rank` now answers *which surface do I open for this figure*, so
**run `python3 framework/scripts/paper_packet.py rank --pmid <PMID>` before a figure read** and
open what it names — never the surface habit reaches for, and never the one a prior entry's
acceptance test named before anybody measured. It writes nothing, gates nothing and exits 0.
Routed in [`framework/scripts/README.md`](../../../framework/scripts/README.md) § 2.

**Why a supplement can beat the article PDF, stated once so it generalises:** the publisher
downsamples figures to the article's own print target; a supplementary "all figures" PDF is often
assembled from the author-submitted originals and never downsampled. So *"the publisher PDF is the
authoritative surface"* is a claim about provenance, not about resolution, and the two come apart.
Nothing here is specific to this paper — which is why it is `rank`'s question and not a note.

**Cost / API / privacy risk:** none. Local PyMuPDF geometry only; no network, no paid service, no
new dependency, no individual-level material.

**Next surgical micro-step:** none pending. The generic fix is shipped and routed; this entry is
the measured fact it produced.

## 2026-10-21 · scientist-a · REPURP-10H-P4-DEEP-A-20261022 · the candidate-card builder cannot represent a measured null

**Gap (new; the log was searched for "measured null", "NO_CHANGE" and "repurposing_bridge" and holds
no entry for it).** `framework/scripts/repurposing_bridge.py` accepts `direction` INCREASE, DECREASE
or UNKNOWN only. A measured "not significant, not rescued" has no value of its own, so building the
first twelve P4 packets forced five measured nulls to be entered as UNKNOWN (`DR-A01-003`,
`DR-A01-004`, `DR-A02-003`, `DR-B01-002`, `DR-D01-002` under
`disease-models/wwox/research/drug_repurposing/cards/`), and the built card then reads `direction
unknown` for a result that was measured, indistinguishable from one never measured; the bridge, its
documentation and the roadmap read UNKNOWN as *owed*. **Two related gaps from the same build:**
one `disease_assertion` per packet, so a multi-endpoint candidate has one endpoint compared and every
other measured endpoint is forced to "endpoint: mismatch"; and the card's `translation` block is a
constant UNKNOWN with no input path and one `access` key where the roadmap demands separate
`time_to_access` and `time_to_benefit`. The roadmap's other P4 fields have no typed slot.

**Change made:** none to the bridge (a Harness agent owns it). Compensation shipped inside the
scientist's own subdirectory: every null assertion carries a `measured_result_note` that states
"MEASURED NO ..., UNKNOWN does NOT mean owed", and `cards/check_cards.py` is a disease-agnostic-in-spirit
offline regression that fails a card with an absent P4 field, a score/rank key, a dose-looking
token, an abstention without its missing datum, or a receipt id absent from the ledger.

**Proposed fix, for Harness Engineering:** a declared fourth direction value (e.g. NO_CHANGE) that
requires a comparator and a test, compares to nothing and is never pooled, with its own `limits` line;
typed slots for the remaining P4 fields with the same UNKNOWN-not-absent rule; and a list of disease
assertions keyed by endpoint. Cost: hours. **Cost / API / privacy risk:** none.

**Update 2026-10-22 (same entry):** the measured-null and `translation` gaps were closed by Harness commit `b96e4cd9` before the cards landed (NO_CHANGE direction; translation fields reachable; two roadmap rows validated); the cards were rebuilt. Still open: one `disease_assertion` per packet (G-2), and typed slots for the other roadmap P4 fields.

---

## 2026-10-22 · scientist-d · R4c (repurposing group R4 follow-up lot)

**Gap (with evidence).** `docx_to_text.py` lists embedded images as "not read as text", but a supplementary Word file whose figures are EMF could not be opened at all: no ImageMagick delegate, no LibreOffice or Inkscape on the host, PyMuPDF does not read EMF. The three Figure S1 panels of PMID 42446932 were owed for a day for that reason alone; they carry one uncompressed EMF+ bitmap each.

**CHANGE (proportional micro-upgrade, shipped).** `framework/scripts/docx_media_extract.py` writes every `word/media/` file unchanged and decodes an EMF+ bitmap (24bppRGB, 32bppRGB, 32bppARGB, 32bppPARGB) to PNG with the standard library; vector EMF, compressed bitmaps and other pixel formats are reported "not decoded", and transparent areas of a decoded bitmap come out black (said in the output). Offline suite `test_docx_media_extract.py` (4 tests: unchanged media, decode, pixel order, refusals), enrolled in the release battery and routed in `framework/scripts/README.md`; run on the real file it reproduces the three 844 x 595 images read by hand.

**Named, not built.** A converter for WEBP and TIFF figures (ImageMagick `convert` handles WEBP here; TIFF went through PyMuPDF in wave 2) and a manifest-spec builder that writes the derived-artefact recipe from the extractor's own output; both are scratch code in every Scientist's session.

**Cost / API / privacy risk:** none; no keyed API, no unlawful source.

**Next surgical micro-step:** none required.

## 2026-10-22 · scientist-d · R4d (repurposing group R4, lot 3)

**Gap (with evidence).** Resuming seven manifests needed the same scratch code seven times (a builder that appends artifacts and locators, a figure fetch from the image addresses embedded in a saved article page, a stripper for reference-manager payloads in a Word supplement); the blind audit then narrowed 57 of 87 propositions that borrowed a subject or predicate from the sentence next to the quote.

**CHANGE = NONE.** The scratch helpers are session-local and not yet shared by three Scientists; the narrowing lesson is a drafting habit (write the proposition from the quote), recorded in the self-evaluation.

**Named, not built.** A shared resume-manifest builder that checks, before writing, that every scope word of a proposition occurs in its snippet.

**Cost / API / privacy risk:** none; no keyed API, no unlawful source (a publisher refusal was not circumvented).

**Next surgical micro-step:** none required.

## 2026-10-23 · plan · Drug Repurposing module (PLAN-DRUGREPURPOSING-MODULE-20261022)

**Gap (with evidence).** Twenty of the twenty-six candidates the mechanism-intervention map names cite their papers as author-year prose, so the join (`repurposing_join.py`) finds no `PAPER`, `CLAIM` or `DL-` id behind them and abstains (`module_proof_20261023.md` § 3.4). The hand-made cards for the same levers were written from the manifests by hand and therefore carry the evidence the derived cards cannot see. The gap is in the record's citation habit, not in a missing tool.

**CHANGE (proportional micro-upgrade, shipped).** The module itself: six one-file key-less adapters with their licences read at the source (`framework/adapters/`, `ACKNOWLEDGEMENTS.md` rendered from them), the join with per-paper depth and audit status and a one-hop inheritance through named records (146 → 59 abstentions), the `handoff` mode that turns each card's measured dependence into one SELECT / READ / REPLICATE / AUDIT row for the next batch, and two enrolled suites. No install, no framework, no registry, no score.

**Named, not built.** A second inheritance hop (two records away; would inflate the tables); a freshness gate on the committed `join/` snapshot (would turn red on unrelated batches — `run` prints the diff instead); an extractor that turns a locator into a typed drug assertion (that is a reading, and stays with the Scientists); ToolUniverse / OptimusKG installs (WATCH / TRY in `tool_survey_20261022.md`).

**Cost / API / privacy risk:** zero spend; six key-less public APIs with their rate limits honoured (PubTator 3 one request per query; openFDA under 1,000/day); no identifier of any person in any query; declined on terms: GtoPdb, CLUE, SemMedDB, Orphadata Products, AetherCell.

**Next surgical micro-step:** the selector resolves the map's prose citations to `PAPER` ids (the 21 SELECT rows); on the next `run` the join inherits them with nothing else to change.


## 2026-10-25 · orchestrator · Weekly WRITE intervention

**Gap (repeated).** Scientist-resolved source identifiers still absent from map records caused false single-paper and linkage-gap tasks (Scientist C, module_linkage_and_replicate_scientist-c_20261024.md §§1–2). The October 20 cleanup proposal also identified the preserved VPS history misreported as overdue task work.

**CHANGE (measured).** Three SOURCE_IDS rows and regeneration through the existing join: 339 queries, 26 cards; queue 8 AUDIT, 16 READ, 2 REPLICATE, zero SELECT. A PRESERVED_BACKUP class retains all divergence measurements without instructing a stale merge. Removed the capability-scout skill's contradictory compulsory-growth quota; its existing CHANGE = NONE procedure remains.

**Validation.** Six adapters passed real calls; adapter and join suites passed; hygiene regression constructs both divergent and merged backup refs alongside ordinary task controls. Full outcomes are in weekly_write_intervention_20261025.md and the task record.

**Cost / API / privacy risk:** zero spend, public key-less adapter calls only. No new source, dependency or scientific conclusion.

**Next surgical micro-step:** refresh the same join after the next scientific batch. No additional harness control is needed.

## 2026-10-27 · scout_daily · SigCom-LINCS

**WWOX question.** Transcriptional-reversal signatures for a WWOX-loss signature

**Contribution vs existing.** LINCS/CLUE declined on terms (module_proof_20261023); SigCom/iLINCS not yet reached

**Detected.** etag: '"70q5lh78i1i18z"' -> '"xw53wy0h2ri18z"'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; see source.

**Proof.** https://maayanlab.cloud/sigcom-lincs/

**Outcome.** TRIAGED 2026-10-27 (plan): no action. A landing-page ETag changes when the web app is redeployed; it says nothing about the signature libraries. The probe now reads the library count (metadata-api, 431 at baseline), so only a content change selects.

## 2026-10-27 · scout_daily · Discovery:sdr-enzyme-assay

**WWOX question.** WWOX SDR domain: no activity assay or substrate known

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper] Structural and mechanistic basis for the heterotetrameric benzaldehyde synthase from petunia. (2026-07-29) https://europepmc.org/article/MED/42525737; [paper] Engineering a Novel Cofactor-Versatile Short-Chain Dehydrogenase for Efficient Synthesis of Chiral Alcohols. (2026-05-13) https://europepmc.org/article/MED/42130227; [paper] Cloning, expression and molecular evolution of Komagataella phaffii ketoreductase with enhanced catalytic activity. (2025-07-04) https://europepmc.org/article/MED/40614109

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** TRIAGED 2026-10-27 (plan): no useful opportunity. Three enzyme-engineering papers on unrelated plant/yeast ketoreductases, none about WWOX or an orphan SDR substrate. GitHub half was rate-limited (HTTP 403) and re-rotates.

## 2026-10-27 · scout_daily · Discovery:isr-atf4-epilepsy

**WWOX question.** ISR/ATF4 modulators in epilepsy or DEE (candidate-class evidence is thin)

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper] The dual role of ATF4 in neurons: from stress adaptation to therapeutic intervention. (2026-06-11) https://europepmc.org/article/MED/42370203; [paper] Activation of the integrated stress response contributes to developmental delay and seizures caused by mitochondrial prolyl-tRNA synthetase  (2025-12-09) https://europepmc.org/article/MED/41380592; [paper] Inhibition of the Integrated Stress Response Prevents Natural Forgetting and Corrects Accelerated Forgetting Associated with Epilepsy. (2024-12-21) https://europepmc.org/article/MED/39708234

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** TRIAGED 2026-10-27 (plan), examined at discovery depth (Europe PMC record + open text skim, NOT a reading). (1) 41380592, Redox Biol 2026, PMC12754399, CC BY-NC: Drosophila PARS2 (mitochondrial tRNA synthetase) deficiency shows seizures; GENETIC suppression of GCN2 or ATF4 prevents them. Fills the 'ISR in epilepsy' gap only as an external invertebrate, genetic precedent: not WWOX, not pharmacological, not human neural. Not in the registries (git grep). Decision: READ candidate for a Scientist (full text is open; needs FULLTEXT_READ_RECEIPT). (2) 39708234, mouse, ISRIB corrects PTZ-accelerated forgetting: drug-in-seizure-model precedent about memory, not seizures or DEE; no full text (OA=N); WATCH. (3) 42370203 review of ATF4 in neurons: background only.

## 2026-10-27 · scout_daily · Discovery:residual-function-chaperone

**WWOX question.** residual-function / chaperone rescue of missense alleles

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper] Rett Syndrome: Specific MECP2 Variants are Associated With Elevated Serum Neurofilament Light Chain. (2025-08-05) https://europepmc.org/article/MED/40845725

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** TRIAGED 2026-10-27 (plan): no useful opportunity (Rett MECP2 serum NfL biomarker; no chaperone or residual-function content). GitHub half rate-limited (HTTP 403) and re-rotates.

## 2026-10-27 · scout_daily · Discovery:dee-drug-response-data

**WWOX question.** paediatric DEE drug-response datasets (a gold set does not exist)

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper] Developmental and Epileptic Encephalopathy due to Cyclin-Dependent Kinase-Like 5 Deficiency: A Single-Center Experience Across Sex Differenc (2026-01-09) https://europepmc.org/article/MED/41619470; [paper] SLC6A1-Related Neurodevelopmental Disorder: A Scoping Review of Clinical Features and Emerging Therapeutic Strategies. (2026-05-05) https://europepmc.org/article/MED/42173049; [paper] Longitudinal analyses of electronic medical records reveal dynamic developmental trajectories for patients with SCN8A-related disorders. (2025-12-20) https://europepmc.org/article/MED/41420531

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** TRIAGED 2026-10-27 (plan): no useful opportunity at title depth: a CDKL5 single-centre series, an SLC6A1 scoping review, an SCN8A EMR trajectory analysis (41420531) that describes a cohort and releases no dataset. No paediatric DEE drug-response dataset surfaced. GitHub half rate-limited and re-rotates.

## 2026-10-27 · scout_daily · Discovery:pdh-assay

**WWOX question.** a PDH-specific measure (activity, phosphorylation or flux) is missing

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper] Thalamic PDK-PDHA1 Signaling is Associated with Opioid-Induced Loss-of-Righting-Reflex Sensitivity: Evidence from Phosphoproteomic Profiling (2026-10-20) https://europepmc.org/article/MED/42900260; [paper] Targeting the Lcn2/Lcn2R-Grb2 cascade ameliorates mitochondrial bioenergetic failure and neuronal death in hepatic encephalopathy. (2026-10-06) https://europepmc.org/article/MED/42838378; [paper] Hyperpolarized 13C-bicarbonate production correlates with excitatory neuron distribution in the human brain. (2026-09-01) https://europepmc.org/article/MED/42689174

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** TRIAGED 2026-10-27 (plan), discovery depth. 42689174, Imaging Neuroscience 2026, PMC13537045, CC BY: hyperpolarized 13C-pyruvate MRI in 40 healthy adults, bicarbonate/pyruvate ratio read as PDH flux, correlated with excitatory-neuron expression. A method precedent for PDH flux in vivo; a healthy-adult imaging study with no patient, WWOX or cell-assay content, so it does not fill the cell/tissue PDH-assay gap. WATCH, no read now. The other two (opioid thalamic phosphoproteomics, hepatic encephalopathy) are off-topic.

## 2026-10-27 · scout_daily · Discovery:assertion-extraction

**WWOX question.** module blind spot: typed drug assertions from papers and name-to-compound linking

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository] dphatIT1911/vn-biomedical-ner-llm-hybrid-icd10-rxnorm (2026-08-18, none stated) https://github.com/dphatIT1911/vn-biomedical-ner-llm-hybrid-icd10-rxnorm; [repository] Ineichen-Group/ClinicalTrials_DrugDisease_Pipeline (2026-04-08, none stated) https://github.com/Ineichen-Group/ClinicalTrials_DrugDisease_Pipeline; [repository] rtx4070-m4/Clinical-Scribe-AI-v4 (2026-03-20, MIT) https://github.com/rtx4070-m4/Clinical-Scribe-AI-v4

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** TRIAGED 2026-10-27 (plan), examined: Ineichen-Group/ClinicalTrials_DrugDisease_Pipeline (README read; pushed 2026-04-08; 0 stars). Code carries NO licence (default all rights reserved): not adopted, not run. Its output is trial-level drug-disease pairs linked to UMLS/MONDO, Zenodo 10.5281/zenodo.19351891 (CC BY-4.0, 122 MB, AACT snapshot 2025-12-01), not typed assertions from papers, and we already hold a ClinicalTrials.gov census. Decision: REJECT the code; WATCH the CC-BY data only if drug-name normalization (blind spot F6) becomes a work item. The other two hits (Vietnamese NER, a scribe app) are off-topic.

## 2026-10-27 · scout_daily · Discovery:neuron-perturbation-signatures

**WWOX question.** context-matched neuronal perturbation signatures for reversal queries

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper] Modeling myeloid cell development in health and disease using induced pluripotent stem cells. (2026-07-15) https://europepmc.org/article/MED/42528516; [preprint] Integrating genetically predicted transcriptomic signatures with longitudinal real-world data enables scalable drug repurposing for Alzheime (2026-05-15) https://europepmc.org/article/PPR/PPR1208319; [preprint] Ropinirole hydrochloride mitigates oxidative stress and neuroinflammation via the PI3K–mTOR pathway in TDP-43 hiPSC-derived microglial-like  (2026-03-10) https://europepmc.org/article/PPR/PPR1220571; [repository] EricSpencer00/als-signature-reversal (2026-08-19, MIT) https://github.com/EricSpencer00/als-signature-reversal; [repository] dralperenuysal/reinvent_geroprotector (2026-08-06, MIT) https://github.com/dralperenuysal/reinvent_geroprotector; [repository] sorrymaker330/drug_prediction (2026-04-10, none stated) https://github.com/sorrymaker330/drug_prediction

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** TRIAGED 2026-10-27 (plan): no useful opportunity at title/description depth (myeloid iPSC review, an Alzheimer EHR preprint, a TDP-43 microglia preprint; three small ALS/geroprotector repositories with 0 stars). Nothing offers a content-matched neuronal null.

## 2026-10-27 · plan · Radar iteration 3 (consumption check, catalogue probes, gap search)

**Consumption verified.** The only cron execution so far (2026-10-27 05:20 UTC; `~/.local/state/legend/scout_daily.log`, `scout_daily.json`) selected one item, SigCom-LINCS (landing-page ETag change). It was consumed in the loop that exists: the pending entry was triaged by `plan` the same day (entry above: no action, an ETag is a redeploy signal) and the probe was redefined to the signature-library count (431 at baseline). The cron run therefore predates the redefined probes; their first cron execution is the 2026-10-28 05:20 run.

**Probes added** (`scout_daily.py`, one call each, key-less, single attempt, failure = probe error with last good fingerprint kept): ChEMBL FTP `latest/` release file (cross-check of the API version; ChEMBL_37 at baseline), DGIdb source versions (count + hash of 48 source/version records; the repository probe sees only code), openFDA NDC `meta.last_updated` (2026-10-27 at baseline), Every Cure drug list / kg-nodes / kg-edges as three separate Hugging Face probes (licence, LICENSE file, card oid, commit sha) beside the existing scores and code probes, so terms of one never transfer to another (baseline: drug list CC BY 4.0 on card; scores no licence; kg nodes/edges licence "other" with a LICENSE file), GEO records matching LINCS and L1000 (count 15 at baseline; a count is not a signature). WWOX literature (two PubMed queries, new-PMID diff) was already probed. A real run on a scratch copy of the state: 20 probes, 0 errors, about 60 s wall time, then silent re-run behaviour covered by `test_scout_daily.py` (CatalogueProbes).

**Gap search** (7 calls: 4 searches, 3 page fetches, plus 3 reachability checks; about 6 minutes). Retained, each judged on one named gap.

- Claude Science connectors and skills (official page `claude.com/docs/claude-science/connectors-and-skills`). WATCH. Answers: compound catalogue breadth and reading assistance, interactively. Adds: named connectors to PubChem, ChEMBL, BindingDB, openFDA, Open Targets, GEO, STRING, ZINC, Rhea. Cost: product setting, not a repo dependency; maintenance none here. Terms: the page states read-only, no key, source licences apply (some non-commercial). The underlying databases are public APIs the module already calls (ChEMBL, openFDA, Open Targets) or can call directly; not a Claude-only capability. Remove: nothing installed.
- PubChem PUG-REST and BindingDB REST, called directly. TRIAL (one adapter each, only if a card needs it). Answers: compound identity and measured target affinity beyond ChEMBL. Both answered HTTP 200 today. Cost: one file plus self-test each (adapter convention). Terms: not read here, to read before adopting. Remove: delete the adapter.
- Dryad "drug repurposing candidates for rare neuro-muscular disorders" (May 2026, 618 KB; ensemble of rule, GNN and path models; seven disorders including pyridoxine-dependent epilepsy). WATCH. Answers: compound-to-need method precedent for a DEE-adjacent disease. Adds a ranked list for other diseases only; not WWOX or WOREE. Licence: not stated on the page ("licensed for reuse" only), so no reuse until read. Remove: nothing held.
- IxIDN / ORDON benchmarks (bioRxiv, June 2026; 574 and 793 rare diseases). WATCH. Answers: how to test a disease-association predictor; useful only if a predictor is ever adopted (none now). Licence and data location not verified.
- ToolUniverse: unchanged (v1.5.7 at last probe); WATCH, no concrete missing capability emerged. TxGNN: reopening condition unchanged (explorer unreachable today, no code commit since 2024-05-06, no full_graph checkpoint); REASONED WAIT; DEE-wide predictions are not WOREE-specific. MATRIX scores: licence still undeclared (REJECT use, probe continues). LINCS/SigCom: inconclusive route, probe on library count.

**Not done.** No connector was used or tested; the Claude Science page was read, not exercised. Licences of PubChem, BindingDB, the Dryad set and the benchmarks were not read.

## 2026-10-28 · junior-harness · Radar iteration 4 (2026-10-28)

**Consumption of the daily run.** The 2026-10-28 07:21 UTC run (`scout_daily.json`): verdict NO_USEFUL_CHANGE, ToolUniverse, TxGNN code and explorer, MATRIX code and scores, DGIdb, Monarch, SigCom-LINCS (library-count probe), iLINCS, Open Targets, ChEMBL all UNCHANGED. New probes baselined: ChEMBL FTP (chembl_37_sqlite), DGIdb-data (48 records), openFDA NDC (2026-10-27), Every Cure drug list (CC BY 4.0 on card). The ETag change on SigCom-LINCS (`70q5lh78i1i18z` -> `xw53wy0h2ri18z`) belongs to the 2026-10-27 log line, not to the 10-28 run. Checked on the primary service: the landing page is a JavaScript application (the fetch returned no text), the metadata API answers HTTP 200 and returns library records (first: EDS-1014, rank_matrix). I did not count libraries, so "library set unchanged" rests on the daily probe only. Nothing pertinent found; the local negative LINCS result of iteration 3 stays valid within its perimeter and was not rerun.

**Findings that change a prior assumption.**
- GtoPdb web services now require an API key obtained by request through the site's contact page (page text; live check: `/services/targets?geneSymbol=WWOX` returned HTTP 401 without a key). A key request means registration with an address, which this laboratory forbids. Adoption as an API is therefore blocked; the Download page was a login page in my fetch, so the file route is UNVERIFIED.
- ChEMBL target search resolves a group/subunit target by components: each component carries a UniProt accession and a `relationship` (for example `GROUP MEMBER`), target types distinguish single protein, protein family, complex. This is the cheapest answer to the family/complex question and needs no new dependency.
- ToolUniverse already wraps GtoPdb, NIH DSLD, Pharos and ChEMBL target search (module source pages). No changelog entry showing a new target-resolution capability was found.

**Table.** Integration cost in hours for one adapter plus self-test, in the existing adapter convention.

| Candidate | Gap it fills | Licence (quoted) | Access mode | Hours | Verdict | Reason |
|---|---|---|---|---|---|---|
| ChEMBL target + activity REST (already used) | (1)(2) target identity with components (UniProt accession, group/complex relationship), activities with assay ids; 24,527,044 activities, 18,552 targets, ChEMBL_37 (status call today) | not re-read today; prior iterations recorded CC BY-SA 3.0 (UNVERIFIED this round) | key-less REST, HTTP 200 on search and activity today | 2-3 (target-resolution helper over the existing adapter) | ADOPT (extend existing) | No new source; fills target-family resolution for compound-target cards. Read the licence page before redistributing derived tables |
| GtoPdb / IUPHAR web services | (1) stable target and ligand ids, families, complexes, subunits, curated actions | "licensed under the Open Data Commons Open Database License (ODbL)"; contents "Creative Commons Attribution-ShareAlike 4.0" (page paraphrase of the web-services page) | JSON REST needs an API key by request (401 without; ~60 requests/min) | 3 if a key existed | REJECT for now (WATCH the download route) | Key = registration, forbidden. Revisit only if the operator authorises a key or the Download files turn out to be open |
| BindingDB REST and downloads | (2) measured affinity beyond ChEMBL | search snippet: BindingDB-curated data "under the Creative Commons Attribution 4.0 License", ChEMBL-imported records CC BY-SA 3.0 (secondary source: UCSD library dataset pages; the BindingDB download page itself states no licence) | REST page answers 200; download page shows no licence text | 3 | TRIAL (only on a card that needs it) | Licence is stated by a library mirror, not by the primary page: UNVERIFIED on the primary |
| Open Targets Platform | (1) target-disease-drug evidence with Ensembl/ChEMBL ids | "Open Targets Platform is marked with CC0 1.0." | GraphQL (HTTP 400 on empty probe, i.e. alive) and bulk | 0 (already used) | ADOPT (already) | Cleanest licence in the set |
| Pharos / TCRD | (1) target development level, ligands per target | about page: data from primary sources, "respect their individual licenses"; code MIT (secondary) | GraphQL `pharos-api.ncats.io/graphql` key-less (HTTP 400 empty probe); full TCRD download | 3 | WATCH | Adds a target-knowledge tier, not new compound-target facts; no own data licence, inherits sources |
| DrugCentral | (1) approved-drug to target with action | "DrugCentral is available under Creative Commons license" (version of the CC licence not stated: UNVERIFIED) | web, download, API (details not read) | 3 | WATCH | Overlaps ChEMBL/DGIdb; licence version unknown |
| Chemical Probes Portal | (2) expert-rated probes, selectivity, recommended use | only a secondary 2020 statement (Probes & Drugs dump CC BY-SA 4.0); portal licence UNVERIFIED (about page 404) | website; no API found | 4 (manual or scrape: not recommended) | WATCH | Useful as a manual cross-check of a candidate probe; no verified machine route |
| NIH DSLD API v9 | (4) US supplement labels, ingredients, doses | API spec page marked "CC0 1.0 Universal" (covers the spec page, data terms UNVERIFIED); NIH states inclusion is not endorsement | key-less REST, live: `browse-products?q=curcumin` HTTP 200, 817 hits; full dataset by request to ODS (not to be contacted: contains an address) | 4 | TRIAL (card-driven) | Only supplement source with a working key-less API; labels are manufacturer claims, not verified |
| Italian Ministry of Health notified-supplements register | (4) the local list for Italian products | none found | website search; a dataset or open-data entry not found | n/a | WATCH | Registry exists (reported >150,000 entries); no download or licence confirmed. Do not scrape without terms |
| EU register of health claims (Commission, from EFSA opinions) | (4) which claims are authorised per substance | no licence found | complete dataset as Excel from the register page | 2 | WATCH | Useful as a claims-status lookup; reuse terms UNVERIFIED |
| Open Food Facts | (4) packaged foods; marginal for supplements | "The Open Food Facts database is available under the Open Database License." Contents: "Database Contents License." Images: "Creative Commons Attribution ShareAlike" | key-less REST, live product call HTTP 200 | 3 | WATCH | Weak supplement coverage; ODbL share-alike on derived databases |
| Local pdftotext, pdfimages, pdftoppm, chromium (installed) | (5) PDF to text, embedded images, page raster, print to PDF | poppler tools (licence not read here: UNVERIFIED) | local, no install | 0 | ADOPT (use as is) | Already present; covers text, embedded rasters, page renders for vector figures |
| PyMuPDF | (5) text with coordinates, vector-aware page render | "GNU AGPL v3"; "separate commercial licences available from Artifex" | pip, not installed here | 2 | WATCH | AGPL; the poppler route covers the need today. Note: `get_images` lists raster objects only, vector charts need a page render |
| ToolUniverse | wrappers for GtoPdb, DSLD, Pharos, ChEMBL | not re-read (iteration 3 state) | pip/MCP | 4+ | WATCH | Daily probe UNCHANGED; the GtoPdb wrapper still needs the key; no tool-count promotion |
| TxGNN, Every Cure MATRIX | reopening conditions | unchanged: TxGNN explorer/code/ checkpoint no change; MATRIX scores no licence declared; drug list CC BY 4.0 on card | n/a | 0 | WATCH / REJECT use (scores) | Daily probes UNCHANGED; no pertinent condition changed |

**Perturbation data beyond iteration 3 (gap 3).** No new source reached verification in this scan; SigCom-LINCS and iLINCS probes unchanged. Not searched further to stay inside the small perimeter.

**Not verified.** Licence version of DrugCentral; primary licence page of ChEMBL and BindingDB; Chemical Probes Portal terms and API; DSLD data terms and bulk route; Italian register and EU claims register reuse terms; GtoPdb download files; poppler licence; the SigCom library count. No adapter written, nothing installed, no key requested, no address sent to any service.

**Observed cost of this scouting.** 7 web searches, 10 page fetches (3 returned nothing usable: 404, 403, JavaScript shell), about 16 key-less HTTP probes, 4 repository reads; about 2 minutes by the shell clock since worktree creation (model thinking time not included).

### Session close, iteration 4 (2026-10-28): capability gap record

- **Gap with evidence:** no supported way for a host process to deliver a prompt to a LIVE, idle interactive Claude Code session. `claude --bg --resume <id>` starts a copy when the session is already running, and revives a dead session only in a workspace whose trust dialog was accepted in the CLI (`hasTrustDialogAccepted` is false for the repository; probe on 2026-10-28 returned "Workspace not trusted"). Internal messaging sockets and the conversation store were not used (not a documented interface).
- **Change shipped:** `mandate_watch.py` (one control, two triggers): in-session cron for the live session (the runtime enqueues it only while idle), host cron for a dead session. Live proof 2026-10-28 20:31 UTC.
- **Residual:** the operator accepting the trust dialog once in the repository would make the dead-session path usable; the in-session cron dies with its session. WATCH: new `claude agents` / Remote Control capabilities that address an idle live session.

## 2026-10-29 · junior-harness · Radar iteration 5 (2026-10-29)

Perimeter: IT5 step P14, scouting part. Read-only (web fetch, key-less GET probes, repository). Nothing installed, no key requested, no address sent anywhere, no adapter written.

### (a) Real daily run consumed

- Source: `~/.local/state/legend/scout_daily.json`, `run_at` 2026-10-28T07:21:56+00:00 (`scout_daily.py --status`: "RADAR OK last run ... NO_USEFUL_CHANGE"). This is the same run iteration 4 consumed; no later execution exists (the clock read 2026-10-28 23:36 UTC when I started, the next cron fire is 05:20 UTC on 2026-10-29). Caveat: 07:21 is not the 05:20 cron slot, so this execution was most likely started by hand in a session; the cron slot of 2026-10-28 left no separate trace (the JSON is overwritten, the log is silent when nothing changes). The last cron line in `scout_daily.log` is 2026-10-27 05:20 (SigCom-LINCS ETag change, already judged in iteration 4 as an availability signal).
- Differences in the watched items (cache `scout_daily_state.json`): ChEMBL `ChEMBL_37` UNCHANGED; DGIdb release v.5.0.13 UNCHANGED, DGIdb-data 48 records BASELINE; openFDA NDC version 2026-10-27 BASELINE (no prior to compare); Every Cure MATRIX code v0.15.0-matrix UNCHANGED, scores card: licence null, not gated, no licence file, UNCHANGED; drug list `cc-by-4.0` BASELINE; kg-nodes and kg-edges licence `other` with a licence file present, BASELINE; TxGNN code last commit 2024-05-06 UNCHANGED, explorer `reachable: false` UNCHANGED (my own probe of txgnn.org today: timeout, so still unreachable); ToolUniverse v1.5.7 (published 2026-10-13, confirmed on the GitHub API today) UNCHANGED; SigCom-LINCS library count 431 UNCHANGED; GEO-LINCS-L1000 version 15 BASELINE; Open Targets 26.09 UNCHANGED. PubMed: no new WWOX PMIDs on either query. No probe errors.
- Verdict: nothing pertinent changed, so no primary page needed re-reading for the watched sources. Reopening conditions for TxGNN and MATRIX (public predictions, licence declared for scores, access) are all unmet: scores still declare no licence, explorer unreachable. The iteration-3 audit (`drug_repurposing/p3b1/txgnn_matrix_outcomes_20261026.md`) stays as is. Two things to know about the baselines: the kg-nodes/kg-edges licence file is a new fact the radar can now diff, but I did not read it (UNVERIFIED), and "BASELINE" rows cannot show change until the next run.

### (b) Candidates

Hours = one adapter plus self-test in the existing convention. Access verified by a key-less GET today unless stated.

| Candidate | Gap it fills | Terms (sentence, URL, date) | Access mode | Hours | Verdict | Reason |
|---|---|---|---|---|---|---|
| HGNC REST (genenames) | (1) withdrawn / previous gene symbols and ids | "all data is released under the Creative Commons Public Domain (CC0) License." https://www.genenames.org/about/license/ 2026-10-29. Rate: "Please only send REST requests at a rate of 10 requests per second." https://www.genenames.org/help/rest/ | key-less; `fetch/symbol/WWOX` HTTP 200 JSON (hgnc_id HGNC:12799); `search/prev_symbol/X`, `prev_name`, `status:"Entry withdrawn"` documented, no dedicated history endpoint | 2 | ADOPT | Cleanest licence in the set; closes the withdrawn-symbol question for gene names in cards. Not yet tested on a real withdrawn symbol |
| UniChem (EBI) | (1) cross-resource compound ids (ChEMBL, DrugBank, PubChem, ChEBI) from an InChIKey | UniChem page: "a very simple, large-scale non-redundant database of pointers between chemical structures and EMBL-EBI chemistry resources". No licence text; only a link to the EMBL-EBI Terms of Use. https://chembl.gitbook.io/unichem/ 2026-10-29 | key-less; legacy `/unichem/rest/verbose_inchikey/<InChIKey>` HTTP 200 JSON (aspirin: DrugBank, others). v1 path `/unichem/api/v1/sources` answers 308 to a trailing slash | 3 | TRIAL | Fits an identity-resolver step (InChIKey to ids); the legacy endpoint may be retired, so the v1 API must be the target. Data licence not stated on the pages read: UNVERIFIED, so store only ids, not derived tables for redistribution |
| PubChem PUG REST | (1) name / InChIKey / CID resolution, properties | NCBI policy: "Make no more than 3 requests every 1 second." and "NCBI itself places no restrictions on the use or distribution of the data contained therein." but PubChem is listed among resources with material that "may be protected by copyright", users "expected to adhere to the terms" of holders. https://www.ncbi.nlm.nih.gov/home/about/policies/ 2026-10-29. The PubChem docs page itself returned a browser-check shell | key-less; `compound/name/aspirin/property/InChIKey/JSON` HTTP 200 (CID 2244) | 2 | ADOPT (identity lookup only) | Fine as a name/InChIKey resolver at 3 req/s; per-record source terms mean no bulk redistribution. PubChem's own data-usage page not read: UNVERIFIED |
| ChEBI 2.0 REST | (1) curated small-molecule identity, ontology classes | licence not read (aboutChebi 404) | key-less; `/chebi/backend/api/public/compound/15365/` HTTP 200 JSON | 3 | WATCH | Overlaps PubChem + UniChem for identity; add only if a card needs ontology class. Licence UNVERIFIED |
| ChEMBL REST (already used) | (1)(2) target components, activities with assay context | "The ChEMBL data is made available on a Creative Commons Attribution-Share Alike 3.0 Unported License." https://chembl.gitbook.io/chembl-interface-documentation/about 2026-10-29 (closes the iteration-4 "licence not re-read" item). Page also says web interface access "is made under the EBI's Terms of Use"; API key statement absent | key-less; target search HTTP 200 | 2-3 | ADOPT (extend existing) | Same as iteration 4. Caveat: `target/search?q=WWOX` returned total_count 0 (limit=1); I did not establish whether that means no ChEMBL target for WWOX, so a card must resolve by UniProt accession, not by free-text symbol |
| BindingDB downloads | (2) measured Ki/IC50 beyond ChEMBL | Download page (https://www.bindingdb.org/rwd/bind/chemsearch/marvin/Download.jsp, 2026-10-29): no licence or login sentence. Release `202610` files: All TSV 566.75 MB, ChEMBL subset TSV 328.82 MB, Assays TSV 9.65 MB, target sequences FASTA 7.31 MB. Licence only from a secondary source (UCSD library records, via search): own curated data CC BY 4.0, ChEMBL-imported subset CC BY-SA 3.0 | file download without login (as listed); REST `getLigandsByUniprots` HTTP 200 but empty body for Q9NZC7 and for P00533 (EGFR), so REST function UNVERIFIED | 3 | TRIAL (card-driven, local file lookup) | Useful when ChEMBL has no measurement; licence stated only by a mirror, so keep the ChEMBL-derived subset out and cite per record. If used, take the Assays + All TSV and filter locally |
| DrugCentral | (1)(2) approved-drug target actions | "available under Creative Commons license"; "download and use of this resource evidences your agreement to all the terms and conditions of license"; the licence link points to Attribution-ShareAlike 4.0 (CC BY-SA 4.0) legal code, version not named in text. https://drugcentral.org/privacy 2026-10-29 | web, download | 3 | WATCH | Closes iteration 4 version question (CC BY-SA 4.0 by link, not by sentence). Overlaps ChEMBL/DGIdb |
| PDSP Ki database | (2) receptor binding Ki for CNS targets | not read: fetch failed ("unable to verify the first certificate"); `curl` timed out | unknown | n/a | WATCH | Primary page unreachable from here; nothing to say about terms |
| DepMap / PRISM | (3) perturbation sensitivity by genotype | Secondary only (DepMap forum, search): own data typically CC BY 4.0, per-file licence shown in the download panel, other projects' data may differ; the portal terms page I fetched has no licence text and asks not to scrape. https://depmap.org/portal/terms/ 2026-10-29 | file download from the portal (login not stated) | 4 | WATCH | No concrete WWOX question requires it today (cell-line dependency of a tumour suppressor says little about WWOX-DEE neurons); per-file licence must be read at use. No CMap/L1000 successor reached verification; iteration-3 LINCS negative not repeated |
| Harmonizome-type aggregated sets | (3) | not searched | n/a | n/a | not assessed | No pertinent WWOX question identified; skipped by design |
| NIH DSLD API v9 | (4) US supplement labels | API guide page returned HTTP 403 in the fetcher, so no terms sentence this round (iteration 4 had the CC0 spec-page mark only). Live: `GET https://api.ods.od.nih.gov/dsld/v9/browse-products?method=by_keyword&q=curcumin&size=1` HTTP 200, 817 hits, JSON with ingredients and serving sizes; the same call without `method=by_keyword` returns HTTP 500 "Argument must be an instance of Query" | key-less REST | 4 | TRIAL (card-driven) | Correct call form now known; data terms still UNVERIFIED; labels are manufacturer statements |
| EU Novel Food status catalogue | (4) whether a substance is a novel food in the EU | page says the catalogue "is non-binding" (search summary of https://food.ec.europa.eu/safety/novel-food/novel-food-catalogue_en); no download, no licence found | web search interface only (found) | n/a | WATCH | Lookup by hand per card; no machine route confirmed |
| EU register of health claims | (4) authorised claims per substance | Register page: complete dataset can be downloaded "in Excel format" (search summary of the Commission register page); reuse terms not verified | Excel from the portal | 2 | WATCH | Authorised-claims list drawn from Regulation 432/2012; botanical claims excluded, so it answers little for botanicals |
| Italian Ministry register of notified supplements | (4) local products | "inclusion ... does not imply any tacit acceptance, authorisation or registration" (search summary of ministry statement); >150,000 entries; no download or licence found | website search, alphabetical list | n/a | WATCH | Do not scrape without terms |
| Local poppler tools (pdftotext, pdfimages, pdftoppm) | (5) text, embedded rasters, page raster | present at /usr/bin; poppler licence not read | local | 0 | ADOPT (as is) | Unchanged from iteration 4 |
| PyMuPDF | (5) text with coordinates, vector-aware page render, table finder | AGPL v3 per iteration 4 (not re-read). Correction of iteration 4: it IS installed in this deployment (`pip list`: pymupdf 1.28.2) | local, no install | 1 | TRIAL (local use only, never redistributed or served) | AGPL matters only on distribution/network service; a local read tool is not that. Table extraction not tested |
| Playwright (Python) | (5) viewport emulation for testing pages | repository licence Apache-2.0 (GitHub API, 2026-10-29). Install per docs = `pytest-playwright` via pip, then `playwright install` to fetch browsers; no account step mentioned (https://playwright.dev/python/docs/intro) | pip + browser download | 2 install, plus a browser binary of several hundred MB | REJECT for now | Not needed: Chromium is already installed and gives what is needed (next row) |
| Chromium headless, CDP without a library | (5) mobile-width screenshots and DOM dumps | Chromium installed as a snap | local | 1 for flags, 3-4 for a pipe-based CDP helper | TRIAL | Findings below |

Findings from the viewport test, all run from this shell:
- `chromium` (the snap wrapper) exits with rc 1 and "is not a snap cgroup for tag snap.chromium.chromium" when started from this session (the shell lives in the turbovnc user service), also under `systemd-run --user --scope`. Calling the real binary `/snap/chromium/current/usr/lib/chromium-browser/chrome --headless --no-sandbox --disable-gpu --user-data-dir=<dir> --dump-dom file://...` works (DOM returned; harmless dbus/UPower errors).
- `--window-size=390,844` is not honoured below a floor: `innerWidth` came out 500 (and innerHeight 701). A true phone-width test therefore needs CDP `Emulation.setDeviceMetricsOverride`, not the flag.
- A CDP client with no third-party library is possible through `--remote-debugging-pipe` (JSON messages separated by NUL on fds 3/4; no websocket needed; `websockets` is not installed). My 30-line probe hung twice (timeout 124), so I do NOT claim it works; I stopped there. The remaining cause is probably fd plumbing, not the approach.
- `--screenshot` produced no file in my test runs through the snap wrapper (that path failed for the cgroup reason above); not retried through the real binary.

ToolUniverse (decision): fills a concrete gap only partly. The repository has a `BindingDBTool` wrapper (`bindingdb_tools.json`: search by target needs a UniProt accession, "free-text gene or protein names are not supported", it points to ChEMBL_search_targets for names), plus the GtoPdb wrapper that needs a key (iteration 4). That is the same REST I could not make return data, and a thin adapter over BindingDB downloads or ChEMBL needs no framework. Verdict WATCH, not tried, not promoted. Daily probe UNCHANGED (v1.5.7).

### (c) Not verified

PubChem data-usage policy page (browser-check shell); UniChem and ChEBI data licences; BindingDB licence on the primary site and the REST function (empty 200 bodies); PDSP Ki terms and access; DepMap per-file licence and login; DSLD data terms (403 on the guide page); EU Novel Food catalogue and health-claims register reuse terms and download form (summaries via search only); the Italian register's download and terms; Playwright's browser-download source; poppler and PyMuPDF licences re-read; Harmonizome-type sets and CMap/L1000 successors (not searched); HGNC withdrawn-symbol lookup on a real withdrawn symbol; pipe-based CDP; kg-nodes/kg-edges licence file contents; whether ChEMBL really has no WWOX target. TxGNN explorer: only the timeout.

### (d) Observed cost of this scouting

6 web searches, 17 page fetches (6 unusable: 404 x3, 403, certificate error, bot-check shell), about 30 key-less GET probes (EBI, NCBI, HGNC, ChEMBL, BindingDB, NIH, GitHub API), 6 local browser runs, 2 pipe-CDP attempts, 1 written scratch probe (outside the repository). Roughly 25 minutes wall clock by estimate (no timer was started; the shell clock at start was 23:36 UTC on 2026-10-28).

### Session close, iteration 5 (2026-10-29): capability gap record

- **Gap with evidence:** agent-written regression tests repeatedly trip repository-wide guards that the writing agent never ran (closed-world absence pins; shebang mode) and a corpus-dependent test with a typed status value: three suites failed in the first final battery.
- **Change shipped:** the three tests/modes fixed; no new gate. Proportionate follow-up: add the two guard scripts to the briefs of test-writing agents (done in the next briefs).
- **Capabilities gained this iteration (real status):** reproducible catalogue rebuild with refusal on missing inputs; GtoPdb ligand identity reconciliation; DevTools-protocol viewport measurement from the stdlib; shareable package with a mutation-tested audit; `mandate_watch.py` jobs with process identity. Not operational: restart of a dead session (trust), publication outside the development repository (operator).

### Session close, iteration 6 (2026-10-29): capability gap record

- **Radar consumed.** Last real run 2026-10-29 05:20 UTC selected `openFDA-NDC` (catalogue refresh date 2026-10-27 -> 10-28); triage: a product-catalogue refresh date is not an approval or evidence and it self-selects daily, so the probe was removed from `scout_daily.py`; all other probes UNCHANGED (ToolUniverse, TxGNN, MATRIX, DGIdb, ChEMBL, Open Targets). TxGNN and MATRIX not reopened.
- **ToolUniverse (1.5.7, isolated venv 498 MB, 109 packages):** on the GluN2B question it re-serves the same ChEMBL activity rows and GtoPdb interactions as direct calls (no assay-organism join; GtoPdb interactions capped at 25 with the total declared). Verdict WATCH, no adoption; the earlier narrow L1000FWD use stands.
- **Capability executed:** ChEMBL adapter extended (accession resolution, activity rows with assay context, declared truncation, molecule-first reading). Measured finding: an empty single-subunit answer is not absence; pore blockers are curated against heteromeric complexes.
- **Gap with evidence:** research compounds in ChEMBL carry no name or synonym, so exact-name resolution fails (5 of 17 names); P9 resolved them through PubChem standard InChIKeys looked up in ChEMBL by hand. **Candidate (TRIAL, only if a card needs a tool compound's potency):** a keyless name -> InChIKey step (PubChem PUG REST) in front of the ChEMBL molecule lookup; stereochemistry must be checked (NVP-AAM077 matched only on the first block).
- **Gap with evidence:** Europe PMC XML fetched through Python's default urllib answered HTTP 503 where curl succeeded (two actors); use curl or set a User-Agent in `_http.py`-style helpers. No change shipped (the adapters already set a User-Agent).
- **Change shipped this close:** guards section in the standing brief; collision refusal in `record_staged_receipts.py`; marker-line note in `mandate_watch.py`. No new agent, framework or gate.

## 2026-10-29 · junior-harness · Radar iteration 7, package P8 (scouting)

Perimeter: zero spend, key-less reads, no account, no contact, nothing installed in the repository (one isolated venv, deleted). Full tables, licences and counts: `drug_repurposing/scout_it7_20261029.md`.

- **Mechanism literature (abstract depth, no reading receipt):** READ candidates by question: ISR kinase arm and ATF4 read-out (37804316 ISR potentiation by Sephin-1 protective in an HRI-driven model, GCN2/PERK untested; 41706892 ATF4 protein raised by mGluR activation without a transcription change), NMDAR Mg2+ gating by GluN2 (40010346 structure, paywalled; 42342644 DEE variant with raised Mg2+ sensitivity), glia vs seizure timing (41540500 spatial timeline), post-onset restoration design (34253921 within-animal Shank3, 42587157 adult Meis2 upregulation in one NDD risk model restored PV plasticity and suppressed seizures, 42190665 early postnatal Csnk2b). No primary study of PDH phosphorylation in epileptic neurons was found (not a biological negative).
- **Deltas:** TxGNN not reopened (explorer unreachable, last commit 2024-05-06). MATRIX not reopened: scores still declare no licence; kg-nodes/kg-edges `LICENSE.md` read, CC BY 4.0 for Every Cure's contribution only, upstream restrictions remain. NeMoCAD record unchanged (restricted, non-commercial). Unravel/rareSHIFT: DUA and non-commercial terms stated, no accession, matrix, sample or control metadata, and no WWOX public data.
- **Candidates:** TRIAL a direct Reactome adapter (CC0, key-less) and the leakage checks of the Bioinformatics 2026 leakage benchmark (MIT repo); WATCH KG-Bench, PrimeKG (CC0 file, upstream terms unverified), Hetionet, lincs-detectability-atlas (no licence file: no reuse), MIRA, drexml, CANDO; REJECT OptimusKG data (Dataverse licence CC BY-NC-SA 4.0).
- **ToolUniverse 1.5.7 trial (Reactome by UniProt accession, 24 calls):** same stId sets and 275 rows as the direct REST call, mean 1.05 s vs 1.02 s, no truncation; the wrapper turns a 404 into success with empty data and reports it as success (a gene symbol returning four species is Reactome's own behaviour, same rows direct). 484 MB, 2.5 s load. Decision: REMOVE (venv deleted).
- **Gap with evidence:** a wrapper that maps a not-found to an empty success repeats the "absence from silence" failure; any adapter must keep 404 distinct from an empty list. Change: recorded in the report; no code shipped here.
- **Not verified:** see section 5 of the report (full texts, drexml's unfilled MIT template, PrimeKG upstream terms, MATRIX scores licence outside the card, other ToolUniverse categories).

### Session close, iteration 7 (2026-10-29): capability gap record

- **Capabilities actually added:** typed signed subnetwork (P1) with an accession-based firewall check; usable-compound census with an UNKNOWN state and a bidirectional query (P2); a pre-registered three-method comparison with controls, run once (P3); context concordance with a printed derivation rule (P4); a full-loop regression that proves a null result propagates from needs to cards, coverage, join, handoff, work order and views (P6); selection funnel, hypotheses block, predictive-test and context sections in the physician view (P7); a licence and history inventory with a history-privacy subcommand (P8); the hourly control now logs RUNNING.
- **Gap with evidence:** merging a branch into main without running `scripts/public_release_gate.py` let two BLOCKs (hex fragments in free-text set-ids) sit on main for hours. **Change shipped:** the briefs and the integrator checklist already run the gate before the last commit; the orchestrator runs it after each merge (done from the third merge on). No new gate.
- **Gap with evidence:** verifier agents that start headless browsers leave them running. **Change shipped:** the briefs owe cleanup; the orchestrator ends orphans by explicit pid (no `pkill -f`).
- **Radar:** no new real run since the iteration-6 close entry; the hourly path was checked on the real scheduler (events show the :37 looks; RUNNING now logged). TxGNN, MATRIX and NeMoCAD: unchanged limits, not reopened.
- **Not adopted, with reason:** Reactome adapter and the leakage-benchmark checks stay TRIAL (no WWOX question is blocked by their absence); ToolUniverse removed after the Reactome trial (adds only a 404-as-success hazard); PrimeKG, Hetionet, KG-Bench, drexml, CANDO, mira stay WATCH.

## 2026-10-29 · junior-harness · Radar iteration 8, package P7 (scouting)

Perimeter: zero spend, key-less reads, no account, no contact, nothing installed in the repository (one isolated venv, deleted). Full tables, licences and counts: `drug_repurposing/scout_it8_20261029.md`.

- **Named gaps answered:** signature quality, neural compound response, brain exposure, human WWOX RNA, ranking with visible components, parent/salt identity.
- **Findings:** (1) GSE295444 and GSE295447 (1,680 iPSC-derived samples, cortical and dopaminergic neurons and progenitors, 12 compounds incl. rapamycin and lithium chloride, one dose, 7 h, DMSO controls): TRIAL for two pilot families only; GEO reuse terms UNVERIFIED; not a WWOX system. (2) Lim and Pavlidis 2021 (CC BY): CMap reproducibility is low (top-10 % recovery 17 %); ADOPT as the reading for a pre-fixed signature filter. (3) OREVID (code MIT, data CC BY-NC-SA, single-author preprint): its pre-registered LINCS reversal test is at chance, which corroborates the IT7 null; TRIAL its design (per-evidence-line hit rate, hub exclusion, leakage audit), not its data. (4) B3DB (CC0) gives BBB labels for 9 of the pilot names, logBB for 2, no Kp,uu; no open Kp,uu database found. (5) chembl_structure_pipeline in an isolated venv: 5 of 8 parents as ChEMBL, misses inorganic salts and sodium dichloroacetate; TRIAL as a mismatch check only.
- **Deltas:** TxGNN unchanged (MIT, last push 2024-05-06, explorer not reachable); MATRIX unchanged limits; Unravel/Foundation: no accession (only mouse WWOX deposits in GEO, plus one human cell line).
- **Radar and control facts:** daily radar last ran 2026-10-29 05:20 UTC without errors (selected openFDA-NDC, still awaiting triage in the pending log); hourly control logged 288 events, last check 21:37Z, IT8 RUNNING; 6 RESUME actions, 2 failed deliveries on 2026-10-28.
- **Gap with evidence:** the scout could not source the definitions of `distil_cc_q75` and `pct_self_rank_q25` that IT8 P4 counts. No code shipped; recorded for the next signature-filter registration.
- **Not verified:** see section 5 of the report.

- **Scope correction (2026-10-30, IT8 scout verification):** the iteration-7 ToolUniverse verdict (REMOVE) is limited to the Reactome-by-accession trial of 24 calls; "adds only a 404-as-success hazard" holds for that trial only, and the other ToolUniverse categories were not tested.

## 2026-10-30 — iteration 8 close (capability gap record)
- **Gap with evidence:** none new. The ranking tool's same-day snapshot ordering and the view tooling's fixed sleeps were repaired in-session (CHANGE = tools, with regressions).
- **Not adopted, with reason:** no new external tool; the IT8 scout candidates stay TRIAL/WATCH with licences flagged (OREVID data CC BY-NC-SA, CMap-Evaluation GPL-3.0).

## 2026-10-31 — iteration 9 close (capability gap record)
- **Gap with evidence:** the catalogue has no action type for molecular glues (cereblon modulators are coded as pathway inhibitors, so every IMiD-class proposal receives a wrong sign), and complex-target credit joins chains through shared members of different complexes. Both were handled by flags in the engine, not fixed in the catalogue. Recorded for the next catalogue rebuild.
- **Not adopted, with reason:** TxGNN (needs a Python 3.8 + DGL stack; installing a framework to emulate a brand), MATRIX scores (no licence stated); Open Targets was trialled and is already used in substance.

## 2026-10-31 — iteration 10 close (capability gap record)
- **Gap with evidence:** the generator had no input for the role of an observed change and counted convergence across one dataset; both are now sourced inputs (CHANGE = tools: dispose_it10.py, engine v4 member junction, with inverse tests). The complex-member join recorded at IT9 close is closed in the engine (39 of 161 best chains had an invalid junction).
- **Not adopted, with reason:** JUMP Cell Painting (data CC0; trial inconclusive: the declared PLK1 control failed, 2.9 percent of compounds map to the catalogue; WATCH with the reopening conditions in complementary_it10_p24), Enrichr GEO libraries (no advantage; library licence unverified; the one-file connector is optional, not adopted), RummaGEO (LICENSE file CC BY-NC-SA contradicts the API field), ToolUniverse (stays removed), HuggingFace (nothing usable found).
- **Open gap:** a sensitive Q230P protein-fate measurement (synthesis versus turnover) gates every stability lever; the neural HIF protein measurement gates K01; both are reopenable searches, not tools.

## 2026-10-31 — iteration 11 close (capability gap record)
- **Gap with evidence:** the score is a signed sum while the shown chain is one walk; the generator now reports how much of the calculation the chain stands for (CHANGE = tools: `Graph4.walks`, `explain_columns`, with tests; the signed walk sum equals the influence). Null covariates: a reach-matched null is available (`--match reach`); the single-seed Q6 protein set is covariate-sensitive. The generator selftest failure was a fixture incompatibility, repaired.
- **Not adopted, with reason:** JUMP morphology (calibrated once on designed pairs, not above chance within source; closed with a reopening condition), Enrichr GEO libraries (no advantage; academic non-profit service), RummaGEO (LICENSE file CC BY-NC-SA), RxRx3-core (licence forbids neuroscience use), REx (RL path search, Docker/GPU). No external resource decomposes a signed multi-path sum; the exact decomposition was implemented locally.
- **Open gaps:** a sensitive Q230P protein-fate measurement (R1) gates the stability levers; a Cell Painting WWOX perturbation in a neural line with designed controls would reopen morphology; a GitHub token is absent on this host, so Pages cannot be enabled from here.

## 2026-10-31 — iteration 12 close (capability gap record)
- **Gap with evidence:** the decisive missing datum for the product-dependent levers is whether a patient-derived neural model makes WWOX protein above the assay floor (no model shown; G372R SCAR12 the one to retest). It is a measurement, not a tool. A second gap was access: the Brain 2026 supplement is not reachable (no PMC copy; bioRxiv rate-limited); reopening is library or operator access.
- **Method capability exercised, not added:** the limited transcript reanalysis from a deposited count table with units, exact permutation and leave-one-animal-out (P47T, GSE215425) and its independent recompute; no new tool. The animal-level activity signature (two animals) is a reminder to report per-animal pivots.
- **Not adopted, with reason:** GSE298081 (HAP1 WWOX-null screen) as a source of candidates: one clone, no replicate or rescue arm, no fitness phenotype for WWOX loss, the paper never mentions WWOX; DepMap (portal behind a human-verification page, nothing circumvented); ChEMBL REST returned HTTP 500 for one agent on the day (service error, not absence of data). ToolUniverse and new connectors: no gap named, none installed.
- **Open:** ChEMBL release of the 2026-10-30 responses is expected ChEMBL_37 but not recorded (notices keep it unattributed); `cards_early/check_cards.py` fails on 8 of 9 early cards (the bridge now emits `endpoint_outcomes`), a mechanical regeneration not done in IT12.

## 2026-10-31 — iteration 13 close (capability gap record)
- **Gap with evidence:** the signed-network generator does not fit synaptic and channel biology (a hand-built 7-seed E/I run returned proteasome and HDAC inhibitors through GAD1 and NPY chains and no row for ethosuximide or ezogabine); the phenotype-first entry plus a transcript panel computed from a deposit was the useful tool. CHANGE = NONE in the generator; recorded as a modality limit.
- **Access gaps:** GEO returned HTTP 200 with 0 bytes for six GSE158684 files on three routes; E-MTAB-14792 returned 403; nothing was circumvented. Reopening is data-holder release or a later fetch.
- **Capability exercised, not added:** independent recomputation of a transcript panel from raw tables (animals as units, background from control-line contrasts); verification of a recovery contrast from a figure image.
- **Not adopted, with reason:** no external tool installed; no resource found that decomposes a recovery contrast into WWOX-specific and transgene effects.

## 2026-11-01 — iteration 14 close (capability gap record)
- **Gap with evidence:** a function-to-compound question across complex targets needed hand mapping because ChEMBL activity rows named no genes; CHANGE = tools (`framework/adapters/chembl.py`: `target_type`, `target_gene_symbols`, `non_gene_target`; regressions). Eight external resources were tried on a declared set of 8 compounds and 23 relations with known answers (coverage only, not validation): the existing union recovered 22 of 23; DrugCentral, Pharos and BindingDB added no pair, action or potency.
- **Decisions:** KEEP ChEMBL mechanism and activity, GtoPdb release files, DGIdb file, Open Targets mechanism; WATCH DrugCentral file (CC BY-SA 4.0 by link; approved drugs only; some rows from a source with unstated terms); DISCARD Pharos (one origin with DrugCentral), BindingDB REST (no licence text on the pages read; structure identity unverified), PDSP Ki (204 MB table without a gene column), IUPHAR REST (key required), PubChem bioassay (an outcome is not an action). GitHub and Hugging Face scans: nothing adoptable.
- **Access:** the GSE158684 matrices became readable on 2026-10-31 evening; the SRA reads behind them are not public (status `hup`); E-MTAB-14792 stays 'Study not accessible'; the 2024 Aurora B paper is closed access (publisher bot check not circumvented). The daily radar last ran 2026-10-31 05:20 UTC with NO_USEFUL_CHANGE.

## 2026-10-29 · scout_daily · openFDA-NDC

**WWOX question.** Date of the last openFDA NDC refresh (drug product / marketed-status catalogue)

**Contribution vs existing.** access-category and product lookups; one call, key-less, far below the 1,000/day limit

**Detected.** version: '2026-10-27' -> '2026-10-28'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; see source.

**Proof.** https://api.fda.gov/drug/ndc.json?limit=1

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-10-30 · scout_daily · Discovery:residual-function-chaperone

**WWOX question.** residual-function / chaperone rescue of missense alleles

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper] A Mild Neurodevelopmental Phenotype Associated with a Novel BRAT1 Variant: Expanding Genotype-Phenotype Correlations. (2026-10-06) https://europepmc.org/article/MED/42930560; [repository] ykshim2013/rosetta-ddg-protocol (2025-12-19, MIT) https://github.com/ykshim2013/rosetta-ddg-protocol

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-01 · scout_daily · ToolUniverse

**WWOX question.** Can one live-lookup layer (MCP) answer gene-level WWOX queries?

**Contribution vs existing.** optional isolated tool; see tooluniverse_capability_test_20261026.md (work saved) and tool_survey row 12

**Detected.** release: 'v1.5.7' -> 'v1.5.8'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; Apache-2.0.

**Proof.** https://github.com/mims-harvard/ToolUniverse/releases

**Outcome.** TRIAGED, KEEP as optional isolated tool, no re-run (IT15 P5, 2026-11-01): v1.5.7->v1.5.8 touches protein design, model providers and label fixes, no ChEMBL/GtoPdb/IUPHAR/BindingDB/PubChem change; no new question. See disease-models/wwox/research/drug_repurposing/scout_it15_p5_20261101/.

## 2026-11-01 · scout_daily · Discovery:pdh-assay

**WWOX question.** a PDH-specific measure (activity, phosphorylation or flux) is missing

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper] Distinct Post-Exposure Metabolic States Following Pharmacological Perturbation of Mitochondrial Respiratory Complexes I-V in SH-SY5Y Cells:  (2026-10-15) https://europepmc.org/article/MED/42941930

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item (shown where a repository states one).

**Proof.** Europe PMC / GitHub search, public endpoints, no key

**Outcome.** CLOSED, context only (IT15 P4, 2026-11-01): PMID 42941930 = Int J Mol Sci 27(20):9160, CC BY, SH-SY5Y 13C-glucose NMR after respiratory-chain inhibitors, no WWOX perturbation; no method adopted, no receipt. See disease-models/wwox/research/drug_repurposing/radar_p4_it15_20261101/.

## 2026-11-01 · IT15 close · capability gap record

**Gap observed.** Comparing potencies across ChEMBL documents needed assay context (cell system, stimulus, agonist concentration, validity comment), which the REST service returns but was not retained by earlier tables, and the service returned HTTP 500 repeatedly for some molecules. A ChEMBL review document is graded as a single experiment by any document-level rule.

**Change made.** The existing comparison script now grades and refuses a ratio when conditions differ; the regrade tool and 16 regressions were added; the queue reconciles against existing assessments.

**CHANGE = NONE for resources.** ToolUniverse v1.5.8 (KEEP optional, no re-run), ChEMBL offline dump (WATCH, reopen on a gene-per-subunit need or two 5xx on a task-critical query in a day), UniChem bulk files (WATCH, terms unread), Papyrus (DISCARD for now), DTA-GNN (WATCH), SIMPATHIC and rd-explainer (DISCARD). See `drug_repurposing/scout_it15_p5_20261101/`.

## 2026-11-01 · scientist · Radar IT16-P6 (gap table, extension of scout_daily.py, one bounded real run)

Target behaviour: roadmap_current.md section "Daily discovery and bounded follow-up" as read at remote main (the
local task branch lags it). No new scheduler, log or register: `scout_daily.py`, its test, this log and the
existing WATCH list were extended.

| # | Required | Before this package | Now | Executed |
|---|---|---|---|---|
| 1 | Resolve remote main SHA, read context at that revision, cache by SHA/blob, freshness limit, old CURRENT heading not authoritative | not implemented (no revision read) | `resolve_context` (ls-remote, show, blob cache, `freshness_limit`, `outranked_by`) | yes: SHA 1cda3d2a, second run a cache hit |
| 2 | Three explicit channels with error / no_news / delta; probes of known resources are not discoveries | GitHub + Europe PMC only; probes mixed into one verdict | GitHub, Hugging Face (models, datasets, Spaces), Nature portfolio via Crossref; Europe PMC complement; known resources counted apart | yes; Crossref first returned HTTP 400 (invalid `select`), reported as error, fixed, second run delta |
| 3 | Two or three priority questions with a decision each; room for the unexpected; no WWOX keyword needed | one theme a day, gap only | 11 questions with category + decision + roadmap row; 2 per run plus one open slot | yes |
| 4 | Followed teams/repos 6/18/3, configurable, no filling, replace-or-suspend with reason, weekly deep check, discovery unaffected | absent | `follow_add`, `follow_due`, seed of 3 repos from existing WATCH decisions, `scout_daily_config.json` | partly: 3 repos active, deep check ran once, no replacement ever needed |
| 5 | Versions per source type, dedup, claim labels, counter-evidence, no popularity as quality | latest commit only, ranking by stars | default-branch head and release kept apart, HF revision/card/files, paper status; dedup by DOI/title/name; 6 claim labels (all `unknown` but `declared`); recency ranking | yes for repositories; HF/papers only metadata |
| 6 | Signal to decision to integration states; log line is not evaluation | absent | `trace_event` / `--trace`: evidence kinds exclude log lines; adopted_in_plan distinct from verified | tested; no real adoption traced yet |
| 7 | Briefing with deltas only, one next step, errors visible, save claimed after read-back, concurrent edits kept | silent cron lines | `briefing`, `save_text` / `save_state` with read-back, locked merge, append-only pending log | yes |
| 8 | Licences per part, no spend / e-mail / registration | licence of repos only | per-part `licences` (code, data, weights, service, article) | yes |

Bounded real run (public unauthenticated endpoints, no token, no contact address, scratch state directory so the cron
cache was not touched): run 1 = 53 HTTP calls, 80 s (50 s of it one timeout on txgnn.org, an existing probe); run 2 =
about 55 calls, 80 s. Limits met: unauthenticated GitHub search needs a pause (7 s between questions kept); Hugging
Face search matches names and tags only, so multi-word capability phrases return nothing and a single short term is
used; Crossref cannot filter by journal, so Nature-portfolio titles are filtered client-side from the 10.1038 prefix.
Outcome: run 1 = GitHub no_news, Hugging Face no_news, Nature error (HTTP 400, an invalid field of mine), Europe PMC
delta; run 2 = delta on all four. Run-2 hits were not read: they are discovery, not evidence, and the Hugging Face
hits were mostly marketing "content repurposing" spaces, i.e. noise. Nothing was adopted, installed or traced.
Remaining only planned: weekly follow cycle over several weeks, trace entries from real examinations, an
independent-reproduction label for any candidate, supplements and corrections lookup for papers.

## 2026-11-01 · scout_daily · Discovery:diagnosis:evaluation

**WWOX question.** Evaluation the principal bottleneck: without outcomes independent of the module no step above can be called predictive

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Structure-based drug repurposing and in vitro evaluation of VAV2-associated candidates for suppression of macrophage foam-cell formation in  (2026-09-19, published record) https://europepmc.org/article/MED/42762289; [paper/europepmc] Contextual Representation Learning With ResNet Refinement and Deep Classification for Enhanced Drug Target Interaction Prediction. (2026-07-01, published record) https://europepmc.org/article/MED/42464502; [paper/europepmc] Structure-based multi-pocket virtual screening identifies FDA-approved candidate compounds targeting MPXV thymidylate kinase. (2026-09-14, published record) https://europepmc.org/article/MED/42807188; [repository/github] TakumiKen32/neuroblastoma-drug-repurposing-reconstruction-2 (2026-10-30, none stated, default-branch head be01a8a77218 2026-10-30, release none published) https://github.com/TakumiKen32/neuroblastoma-drug-repurposing-reconstruction-2; [repository/github] ahad21005-cloud/Brain_aneurysm (2026-10-20, none stated, default-branch head cad5f2c12277 2026-10-20, release none published) https://github.com/ahad21005-cloud/Brain_aneurysm; [repository/github] dr-ronak/Ontology-Bridged-Drug-Repurposing-Multi-Agent-GraphRAG (2026-10-04, none stated, default-branch head 3ad867e8c182 2026-10-04, release none published) https://github.com/dr-ronak/Ontology-Bridged-Drug-Repurposing-Multi-Agent-GraphRAG; [model/huggingface] Myric/apex-quant-benchmarks (2026-11-01, apache-2.0) https://huggingface.co/Myric/apex-quant-benchmarks; [dataset/huggingface] vedangfake/chess-slm-benchmark (2026-11-01, none stated) https://huggingface.co/datasets/vedangfake/chess-slm-benchmark; [dataset/huggingface] Agnuxo/P2PCLAW-Innovative-Benchmark (2026-11-01, mit) https://huggingface.co/datasets/Agnuxo/P2PCLAW-Innovative-Benchmark; [paper/nature] Drug repurposing in hereditary ataxia (2026-10-12, journal-article) https://doi.org/10.1038/s44386-026-00079-w; [paper/nature] An integrative single-cell genetic analysis prioritizes immune cell-specific genes and drug repurposing hypotheses in Alzheimer’s disease (2026-10-02, journal-article) https://doi.org/10.1038/s41514-026-00532-0

**Why asked.** diagnosis row 'Evaluation' (R3/R7) [disease-models/wwox/research/drug_repurposing/diagnosis_it16_20261101/README.md @ blob e21ec10f05, main 3e167e250fd6]: "Evaluation the principal bottleneck: without outcomes independent of the module no step above can be called pr"

**If confirmed (decision).** Evaluation: closing 'the principal bottleneck: without outcomes independent of the module no step above can be called predictive' Roadmap: R3.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-01 · scout_daily · Discovery:diagnosis:catalogue-and-identity

**WWOX question.** Catalogue and identity no rate of wrong identity per source; 35+22 failed REST attempts in IT15 not yet turned into a cache

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] Beimnet-Abdi/TenaEquip (2026-09-25, none stated) https://github.com/Beimnet-Abdi/TenaEquip; [repository/github] Beimnet-Abdi/MedEquip (2026-09-25, none stated) https://github.com/Beimnet-Abdi/MedEquip; [repository/github] aayambansal/CER-Bench (2026-09-10, Apache-2.0) https://github.com/aayambansal/CER-Bench; [dataset/huggingface] saadtaleb/tess-courbes-hors-catalogue (2026-10-28, cc-by-4.0) https://huggingface.co/datasets/saadtaleb/tess-courbes-hors-catalogue; [dataset/huggingface] edithatogo/global-medicines-atlas-catalogue (2026-10-28, apache-2.0) https://huggingface.co/datasets/edithatogo/global-medicines-atlas-catalogue; [space/huggingface] invariant-computing-lab/rari-estimator-catalogue (2026-10-27, none stated) https://huggingface.co/spaces/invariant-computing-lab/rari-estimator-catalogue

**Why asked.** diagnosis row 'Catalogue and identity' (R2) [disease-models/wwox/research/drug_repurposing/diagnosis_it16_20261101/README.md @ blob e21ec10f05, main 3e167e250fd6]: "Catalogue and identity no rate of wrong identity per source; 35+22 failed REST attempts in IT15 not yet turned"

**If confirmed (decision).** Catalogue and identity: closing 'no rate of wrong identity per source; 35+22 failed REST attempts in IT15 not yet turned into a cache' Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-01 · scout_daily · Team:aayambansal

**WWOX question.** Evaluation the principal bottleneck: without outcomes independent of the module no step above can be called predictive

**Contribution vs existing.** one-level exploration of aayambansal's public listing (19 scanned, 17 without a shared term); not recursive

**Detected.** owner of discovered aayambansal/CER-Bench; other public work matching ['evaluation']: [github] aayambansal/delphi-benchmark (2026-09-09, none stated, matched ['evaluation']) https://github.com/aayambansal/delphi-benchmark

**Why asked.** diagnosis row 'Evaluation' (R3/R7) [disease-models/wwox/research/drug_repurposing/diagnosis_it16_20261101/README.md @ blob e21ec10f05, main 3e167e250fd6]: "Evaluation the principal bottleneck: without outcomes independent of the module no step above can be called pr"

**If confirmed (decision).** Evaluation: closing 'the principal bottleneck: without outcomes independent of the module no step above can be called predictive' Roadmap: R3.

**Minimal test.** read the repository's README and latest default-branch commit; record the SHA and release apart

**Cost / licence.** reading the listing entries: minutes; per item, shown where stated.

**Proof.** public github listing of aayambansal, no key

**Outcome.** TO_TRIAGE (a listing match is a lead, not a reading)

## 2026-11-01 · scout_daily · Decision:dr-ronak/Ontology-Bridged-Drug-Repurposing-Multi-Agent-GraphRAG

**WWOX question.** Evaluation: without outcomes independent of the module no step can be called predictive (diagnosis row Evaluation, diagnosis_it16_20261101/README.md blob e21ec10f05, main 3e167e250fd6)

**Contribution vs existing.** signal -> examination -> trial -> decision traced in the run state (via question:diagnosis:evaluation); full record: disease-models/wwox/research/drug_repurposing/radar_it17_p2_20261101/README.md

**Detected.** repository created and last pushed 2026-10-04, default-branch head 3ad867e8c182, no release, 0 stars; README (797 lines) holds unresolved merge markers at lines 1, 691, 797; links come from text matching of ChEBI definitions to Disease Ontology terms and are labelled hypotheses; a precision fixture is future work (line 666); one smoke test; README says MIT but the API reports no licence and the tree has no LICENSE file. Measures no outcome, so it cannot supply the independent outcome set the Evaluation row lacks. Declared yes, implemented not run, reproduced no; unknown is not negative.

**If confirmed (decision).** Decision for that question: DISCARD (state reject). Reopen if a labelled drug-disease fixture with a reported precision and a LICENSE file appear. Roadmap: R3.

**Cost / licence.** examination: 6 public API requests, no clone, nothing executed; stated MIT in text, none reported by the API (unresolved).

**Proof.** https://api.github.com/repos/dr-ronak/Ontology-Bridged-Drug-Repurposing-Multi-Agent-GraphRAG/readme (README lines 1, 666, 674, 691, 797)

**Outcome.** DISCARD for this question (examined, no trial needed); not integrated

- **Pointer added 2026-11-08 (DREAM-2):** the E-MTAB-14792 access gap above has an unsent request drafted for the operator: [`drug_repurposing/ebi_access_request_E-MTAB-14792_draft.md`](drug_repurposing/ebi_access_request_E-MTAB-14792_draft.md). The route is a re-check of the public status, then the operator's decision; it is not sent from the module, and no e-mail address is given to any service. Nothing else in this log changes.


## 2026-11-09 · Orchestrator · universal completion and operational attribution

**REPEATED gap:** assigned work deferred despite executable steps, and intermediate delivery
reported as completion. Prior correction: [autonomy/originals session evaluation](session_evaluations/2026-11-08_autonomy_originals.md);
this pass: [universal completion](session_evaluations/2026-11-09_universal_completion.md).
**CHANGE:** the existing continuity rule explicitly covers every actor and runtime within
its scope, with shared entry/delegate/closing routes; operational causal attribution lives
in epistemic discipline. No new tool, gate, registry or external service. Existing checks
verify routing and schema behaviour; universal future model obedience is not demonstrated.
**Next:** observe adoption through existing task evidence; no external scouting needed for this gap.


## 2026-11-12 · Orchestrator · SCI48 (KEAP1/NRF2 comparator) · session capability outcome

**GAP-NEW:** to freeze a candidate on a base that is behind `development/main` without paying a battery for faults main already fixed, a session lacks a check that says so. Evidence: the first SCI48 battery (run 20261112-175935-cbb802c5, SHA e2b0ce41) failed two suites that were already failing at its base 0bed3857 and had been fixed on main hours earlier (`ranking.json` receipt count 1816 against 1818 by `3b877bfc`; Chromium launcher by `4ff3ced5`), costing about 70 minutes. The pre-freeze recipe (`framework/scripts/README.md` section 13) covers the four quick suites, not the distance to main. **Candidate (not implemented here):** `verify_run.py run` prints one line, before the clone, "base is N commits behind development/main; generated surfaces touched on main since: …", never blocking. **Change made in this session:** none to the harness; the lesson is in the Orchestrator's memory and in the session evaluation. Owner of a fix: Harness engineering. No external scouting, no cost, no privacy risk.


## 2026-11-12/13 · Orchestrator · SCI49 (cell-context verification, Kir2 drug-name route) · session capability outcome

**GAP-NEW:** a delegate that must stage receipts for sources it read can be refused the claim step (`paper_packet.py claim`) by the session permission classifier (V12, SCI49 B): its 26 receipts were staged without a claim, and the Orchestrator cannot run the claim on its behalf without permission laundering. Evidence: V12 final report and `kir2_drugname_sci49_20261112/receipts` note. **Candidate (not implemented here):** staged receipts carry an explicit `claim: none` field that the integrator's `record_staged_receipts.py` accepts, or claims are made by the Orchestrator at dispatch for the PMIDs a brief names. Owner: Harness engineering. **Also observed (repeated, no change):** bursts of PMC page requests meet a bot check; the brief rule "space requests by seconds" is the control. No external scouting, no cost, no privacy risk.


## 2026-11-13 · Orchestrator · SCI50 (phenotype-first myelination hypotheses) · session capability outcome

**GAP-REPEATED (no change here):** a delegate's `paper_packet.py claim` was refused by the session permission classifier (V13, as in SCI49 B); its 19 receipts are staged without a claim. The candidate recorded on 2026-11-12 (an explicit `claim: none` accepted by the integrator's recorder, or claims made at dispatch) stands; owner Harness engineering. **Also:** the generative-value comparison "against the current path" (a git-grep table that separates represented, new combination, explanation only) was the discipline that exposed the over-claim; it is a procedure of this package, not a tool, and needs none. No external scouting, no cost, no privacy risk.


## 2026-11-13 · Orchestrator · SCI51 (M1 versus EBP reagents) · session capability outcome

**GAP-NEW:** a source-notice check is missing from the reading procedure: a paper's PNAS Correction and Editorial Expression of Concern (PIPE-307, PMID 39083422) were missed by the producer and verifier of SCI50 and found only by a later blind verifier. Evidence: `m1_ebp_reagents_sci51_20261113/verify/audit.md` item 3. **Candidate (not implemented here):** when a paper becomes a reagent source, the receipt tool (or the brief) runs one PubMed query for the article's linked Correction/Retraction/Expression-of-Concern records (`related` or a title search with the article types) and records the result in the receipt as `post_publication_notices`; owner Harness engineering. **Also repeated:** a delegate's `paper_packet.py claim` refused by the permission classifier (staged without a claim). No external scouting, no cost, no privacy risk.


## 2026-11-15 · plan · strategic continuity, useful-signal relay and consumed observations

**GAP-REPEATED:** the standing continuity rule existed but a legacy incomplete wait, wrong prior ordering, stale standing BLOCKED fields, cadence phase drift and lost deferred observations could still strand useful research. A report addressed to Plan was filed without strategic disposition. **CHANGE:** repaired existing state/code and common routes; original radar reports are discoverable, producers name strategic judgment, and all actors relay relevant signals through the existing channel. Continuous next-work selection also works without fresh input; own portfolio notes do not become new evidence. **Verification:** 125 Advisor and 84 scout tests PASS; actual P12 coverage and P13 mechanism-lens work were delivered/consumed; P14 switched to an open question and IT closed WO-11 without a new operator prompt. Source and limits: `drug_repurposing/advisor_continuity_20261115/README.md` and task `PLAN-ADV-CONTINUOUS-RESEARCH-20261115`. No generative or multi-day reliability improvement is inferred from plumbing tests.

**Reusable distinction:** an event observed is not a result consumed; a previous choice is not perpetual activity; an Advisor annotation is not fresh evidence. These are now executable cases, not another approval step.

**GAP-REPEATED, separate publication diagnosis:** receipt-only increments left ranking summary counts behind the ledger (1957/1958, then1958/1959/1960 today) while all69unit records and37ranked interventions stayed unchanged. The existing regeneration recipe repairs it; protocol clarification alone has not made that boundary automatic. Candidate for later Harness diagnosis: reuse the existing publication/derived-surface tools to expose or repair this coupling proportionately, without a new service, approval or disease-specific dependency. No such additional architecture adopted or handoff claimed here; the final publication snapshot is repaired. No external scouting or spend.

## 2026-11-02 · scout_daily · Discovery:diagnosis:catalogue-use

**WWOX question.** Catalogue use no funnel from source records to identity-resolved to method-usable to evaluated compounds; vigabatrin assertions not recoded 

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [dataset/huggingface] GreenNode/VieDocOCR-Benchmark (2026-11-02, none stated, revision f9d373e2190f, 22670 files) https://huggingface.co/datasets/GreenNode/VieDocOCR-Benchmark; [dataset/huggingface] Digital-Divide-Data/DDD-Kenya-Kamba-Extending-Benchmarks (2026-11-02, cc-by-4.0, revision f348e066251c, 63 files) https://huggingface.co/datasets/Digital-Divide-Data/DDD-Kenya-Kamba-Extending-Benchmarks; [dataset/huggingface] xinyi234/vulnmirage-benchmark (2026-11-02, other, revision a41e9374dfa5, 14 files) https://huggingface.co/datasets/xinyi234/vulnmirage-benchmark; [paper/nature] Microstructural injury to the optic nerve with vigabatrin treatment in West syndrome: A DTI study (2025-07-16, journal-article) https://doi.org/10.1038/s41598-025-06336-8

**Why asked.** diagnosis row 'Catalogue use' (R2) [disease-models/wwox/research/drug_repurposing/diagnosis_it18_20261101/README.md @ blob e278961562, main b193f1a4f54b]: "Catalogue use no funnel from source records to identity-resolved to method-usable to evaluated compounds; viga"

**If confirmed (decision).** Catalogue use: closing 'no funnel from source records to identity-resolved to method-usable to evaluated compounds; vigabatrin assertions not recoded in I' Roadmap: R3.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-02 · scout_daily · Discovery:diagnosis:compound-target-action

**WWOX question.** Compound-target-action six discordances unresolved at source; 83 percent of module mechanism pairs have no independent counterpart

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [dataset/huggingface] pdabrowskitumanski/lab4-compound-sources (2026-10-28, none stated) https://huggingface.co/datasets/pdabrowskitumanski/lab4-compound-sources; [dataset/huggingface] CompoundAI/pe-bench (2026-10-19, cc-by-4.0) https://huggingface.co/datasets/CompoundAI/pe-bench; [dataset/huggingface] cora-health/compounded-injection-price-index (2026-10-11, cc-by-4.0) https://huggingface.co/datasets/cora-health/compounded-injection-price-index; [paper/nature] Global warming intensifies compound renewable energy droughts (2026-10-29, journal-article) https://doi.org/10.1038/s43247-026-04183-7

**Why asked.** diagnosis row 'Compound-target-action' (R2/R5) [disease-models/wwox/research/drug_repurposing/diagnosis_it18_20261101/README.md @ blob e278961562, main b193f1a4f54b]: "Compound-target-action six discordances unresolved at source; 83 percent of module mechanism pairs have no ind"

**If confirmed (decision).** Compound-target-action: closing 'six discordances unresolved at source; 83 percent of module mechanism pairs have no independent counterpart' Roadmap: R2.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-02 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] picspin/study-design-agent (2026-10-23, MIT) https://github.com/picspin/study-design-agent; [repository/github] mbote-droid/bioeng-termbench (2026-10-16, MIT) https://github.com/mbote-droid/bioeng-termbench; [repository/github] Ayesha037/biogenesis (2026-10-11, none stated) https://github.com/Ayesha037/biogenesis; [model/huggingface] Shicheng/biomedical-ai-resource-track-baseline (2026-11-02, apache-2.0) https://huggingface.co/Shicheng/biomedical-ai-resource-track-baseline; [dataset/huggingface] nhminh107/vibiomir-biomedical-corpus (2026-11-02, cc-by-nc-4.0) https://huggingface.co/datasets/nhminh107/vibiomir-biomedical-corpus; [model/huggingface] AI999X/biomedical-science-ai999x (2026-11-01, apache-2.0) https://huggingface.co/AI999X/biomedical-science-ai999x

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-03 · scout_daily · MTBLS12344

**WWOX question.** Is the metabolomics dataset openly accessible (metabolic-signature question)?

**Contribution vs existing.** dated accessibility record: tool_survey_20261022.md; a status change is a reachability signal only

**Detected.** status: 401 -> 200

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; see source.

**Proof.** https://www.ebi.ac.uk/metabolights/ws/studies/public/study/MTBLS12344

**Outcome.** AVAILABILITY SIGNAL (reachability changed; not a capability: check the reopening condition named above, then decide)

## 2026-11-03 · scout_daily · Discovery:diagnosis:matching-evaluation

**WWOX question.** Matching evaluation duplication of evidence, improper transfer between molecules and unknown turned into negative are tested by fixtures but

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [preprint/europepmc] A Large-Scale Pharmacogenomic Knowledge Graph for Drug-Gene-Variant-Disease Discovery (2025-09-25, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1090369; [dataset/huggingface] gaia-benchmark/results_public (2026-11-03, none stated, revision 92364b4800f2, 4 files) https://huggingface.co/datasets/gaia-benchmark/results_public; [dataset/huggingface] Tushar29k/agent-guardrails-adversarial-benchmark (2026-11-03, none stated, revision d7786f09eb4c, 5 files) https://huggingface.co/datasets/Tushar29k/agent-guardrails-adversarial-benchmark; [dataset/huggingface] syedhuq/multihop-rag-benchmark (2026-11-03, cc-by-4.0, revision f41fcf28de60, 3 files) https://huggingface.co/datasets/syedhuq/multihop-rag-benchmark; [paper/nature] Drug repurposing and African natural product screening, targeting the Parkinson‘s-associated LRRK2 G2019S mutant kinase using molecular dock (2026-10-15, journal-article) https://doi.org/10.1038/s41598-026-71061-9; [paper/nature] Drug repurposing in hereditary ataxia (2026-10-12, journal-article) https://doi.org/10.1038/s44386-026-00079-w

**Why asked.** diagnosis row 'Matching evaluation' (R3/R7) [disease-models/wwox/research/drug_repurposing/diagnosis_it20_20261102/README.md @ blob 23f287e46c, main e7f00f13cc11]: "Matching evaluation duplication of evidence, improper transfer between molecules and unknown turned into negat"

**If confirmed (decision).** Matching evaluation: closing 'duplication of evidence, improper transfer between molecules and unknown turned into negative are tested by fixtures but not by a ' Roadmap: R3.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-03 · scout_daily · Discovery:diagnosis:provenance-through-intermediaries

**WWOX question.** Provenance through intermediaries four T-type entries (terodiline, suloctidil, phloroglucinol, bepridil) get a direction through DGIdb copie

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Artemis: Harnessing Knowledge Graphs for Next-Generation Drug Target Prioritization. (2026-06-26, published record) [+1 mirror(s) merged] https://europepmc.org/article/MED/42614934; [paper/europepmc] Statistics and Ontology of Published Small Molecule Ring Systems. (2026-02-01, published record) https://europepmc.org/article/MED/41757738; [repository/github] harshk242/burp (2026-11-02, none stated) https://github.com/harshk242/burp; [repository/github] MuhammadMuneeb007/drug-disease-mapping (2026-10-24, NOASSERTION) https://github.com/MuhammadMuneeb007/drug-disease-mapping; [repository/github] smolyanko/biomedical-ner-pipeline (2026-09-28, MIT) https://github.com/smolyanko/biomedical-ner-pipeline

**Why asked.** diagnosis row 'Provenance through intermediaries' (R2/R5) [disease-models/wwox/research/drug_repurposing/diagnosis_it20_20261102/README.md @ blob 23f287e46c, main e7f00f13cc11]: "Provenance through intermediaries four T-type entries (terodiline, suloctidil, phloroglucinol, bepridil) get a"

**If confirmed (decision).** Provenance through intermediaries: closing 'four T-type entries (terodiline, suloctidil, phloroglucinol, bepridil) get a direction through DGIdb copies of the ChEMBL group ac' Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-03 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] ma3u/MinimumViableHealthDataspacev2 (2026-11-02, Apache-2.0) https://github.com/ma3u/MinimumViableHealthDataspacev2; [repository/github] aiswaryanandan24-cell/PharmGraph-Agentic-AI-Pipeline-for-Drug-Interaction-Discovery (2026-11-02, MIT) https://github.com/aiswaryanandan24-cell/PharmGraph-Agentic-AI-Pipeline-for-Drug-Interaction-Discovery; [repository/github] orevid-org/orevid (2026-11-02, MIT) https://github.com/orevid-org/orevid; [model/huggingface] rav39439/next_token_prediction (2026-11-03, none stated) https://huggingface.co/rav39439/next_token_prediction; [dataset/huggingface] THEORACLEEEE/polymarket-predictions (2026-11-03, mit) https://huggingface.co/datasets/THEORACLEEEE/polymarket-predictions; [dataset/huggingface] Ciroc0/dmi-aarhus-predictions (2026-11-03, cc-by-4.0) https://huggingface.co/datasets/Ciroc0/dmi-aarhus-predictions

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-04 · scout_daily · Discovery:work_order:NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR

**WWOX question.** Which of three readings (NMDAR gain, permissive necessity, AMPAR-led drive) explains the d-APV-sensitive bursting, and does the bursting dep

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Heterosynaptic NMDA receptor plasticity in hippocampal dentate granule cells. (2026-07-22, published record) https://europepmc.org/article/MED/42558507; [paper/europepmc] Modeling the coexistence of NMDAR-dependent LTP and LTD mediated by changes in AMPAR conductance. (2026-06-22, published record) https://europepmc.org/article/MED/42331308; [paper/europepmc] Chronic joint pain drives sex-specific changes in hippocampal glutamatergic signaling and sleep. (2026-09-21, published record) https://europepmc.org/article/MED/42768134; [repository/github] JudyXChen/SpontaneousNMDAR (2026-11-02, none stated, default-branch head 5b0480267999 2026-10-07, release none published) https://github.com/JudyXChen/SpontaneousNMDAR; [repository/github] kalpanapandyanmims1999/-kalpanapandya16-NMDARInhibitors (2026-10-28, none stated, default-branch head 1739aae10ae3 2026-10-28, release none published) https://github.com/kalpanapandyanmims1999/-kalpanapandya16-NMDARInhibitors; [repository/github] KhondamirRustamov/iGluR-peptides (2026-10-15, none stated, default-branch head 4ee79b2d76e5 2026-10-15, release none published) https://github.com/KhondamirRustamov/iGluR-peptides; [paper/nature] BME (CDRI-08) mitigates hypoxia-induced hippocampal neurodegeneration and memory impairment via modulating NMDAR-CREB-BDNF signaling and apo (2026-08-23, journal-article) https://doi.org/10.1038/s41598-026-65605-2; [paper/nature] Sex and genotype influence the disruption of circulating NMDAR-related amino acids in patients with Parkinson’s disease (2026-08-11, journal-article) https://doi.org/10.1038/s41531-026-01507-4

**Why asked.** work_order entry NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 4e96385baf, main cceaf8540686]: "Which of three readings (NMDAR gain, permissive necessity, AMPAR-led drive) explains the d-APV-sensitive burst"

**If confirmed (decision).** E1 decides whether an NMDAR gain is present or the dependence is permissive; a partial blocker is read only after E1, and without E1 a memantine result cannot b Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-04 · scout_daily · Discovery:work_order:NEED-GSK3B-DEREPRESSION

**WWOX question.** Is GSK3 output actually raised in WWOX loss, and in which direction does each class of GSK3 inhibitor move the Wnt readout? The only datum i

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Circulating Extracellular Vesicles in Alcoholic Liver Disease Affect Skeletal Muscle Homeostasis and Differentiation. (2025-02-01, published record) https://europepmc.org/article/MED/39921321; [paper/europepmc] DCI improves diabetic encephalopathy by modulating the BDNF/NF-κB/GSK-3β pathway. (2025-04-03, published record) https://europepmc.org/article/MED/40187477; [repository/github] r-universe/gsk3 (2026-11-01, none stated) https://github.com/r-universe/gsk3; [repository/github] gauravkadupatil-png/GSK32 (2026-10-04, none stated) https://github.com/gauravkadupatil-png/GSK32; [repository/github] spiliotislab/sept9-gsk3-phosphoswitch-code (2026-09-29, MIT) https://github.com/spiliotislab/sept9-gsk3-phosphoswitch-code; [dataset/huggingface] DenyTranDFW/Benchmark_2026_B44_Mortgage_Trust_2160315 (2026-11-04, gpl) https://huggingface.co/datasets/DenyTranDFW/Benchmark_2026_B44_Mortgage_Trust_2160315; [dataset/huggingface] AirCaps/a5s-small-v2-asr-benchmark-dataset (2026-11-04, other) https://huggingface.co/datasets/AirCaps/a5s-small-v2-asr-benchmark-dataset; [dataset/huggingface] crawlcheck/agent-safety-benchmark (2026-11-04, cc-by-4.0) https://huggingface.co/datasets/crawlcheck/agent-safety-benchmark

**Why asked.** work_order entry NEED-GSK3B-DEREPRESSION [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 4e96385baf, main cceaf8540686]: "Is GSK3 output actually raised in WWOX loss, and in which direction does each class of GSK3 inhibitor move the"

**If confirmed (decision).** Raised output with a Tau-versus-catenin separation by one class would make that class a compensation hypothesis independent of residual WWOX protein; unchanged  Roadmap: R3.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-04 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] marinomassimo-dot/legend-development (2026-11-04, MIT) https://github.com/marinomassimo-dot/legend-development; [repository/github] Dengyuemed/dengyuemed.github.io (2026-11-03, none stated) https://github.com/Dengyuemed/dengyuemed.github.io; [repository/github] api-evangelist/omass-therapeutics (2026-10-31, none stated) https://github.com/api-evangelist/omass-therapeutics; [space/huggingface] danielenglish1996/ai-content-repurposing (2026-09-22, none stated) https://huggingface.co/spaces/danielenglish1996/ai-content-repurposing; [space/huggingface] RottenShadow/ailixir-drug-repurposing (2026-07-08, none stated) https://huggingface.co/spaces/RottenShadow/ailixir-drug-repurposing; [space/huggingface] nexustech1/repurposingagent (2026-07-06, none stated) https://huggingface.co/spaces/nexustech1/repurposingagent

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-05 · scout_daily · ToolUniverse

**WWOX question.** Can one live-lookup layer (MCP) answer gene-level WWOX queries?

**Contribution vs existing.** optional isolated tool; see tooluniverse_capability_test_20261026.md (work saved) and tool_survey row 12

**Detected.** release: 'v1.5.8' -> 'v1.5.9'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; Apache-2.0.

**Proof.** https://github.com/mims-harvard/ToolUniverse/releases

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-05 · scout_daily · Monarch-app

**WWOX question.** Phenotype/disease KG API changes

**Contribution vs existing.** kg_thin_slice.py uses it

**Detected.** release: 'v1.31.1' -> 'v1.32.0-rc1'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; BSD-3-Clause.

**Proof.** https://github.com/monarch-initiative/monarch-app/releases

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-05 · scout_daily · Discovery:work_order:NEED-INHIBITORY-HYPOFUNCTION

**WWOX question.** In the Wwox neuron-deleted neocortical slice, is the lost fast GABA-A inhibition the step that makes bursting (rather than a graded change o

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] BrenoKaffer/gabarita (2026-11-05, none stated, default-branch head 6e6d67fe5f40 2026-11-05, release none published) https://github.com/BrenoKaffer/gabarita; [repository/github] Bronze012/gabarito-med (2026-11-05, none stated, default-branch head c30080b18885 2026-11-05, release none published) https://github.com/Bronze012/gabarito-med; [repository/github] lucasgenial/gabarito360 (2026-11-05, none stated, default-branch head 9ea0a2977b57 2026-11-05, release none published) https://github.com/lucasgenial/gabarito360; [model/huggingface] georgeliu59/caption_qwen35_9b_trainset_retrieval_benchmark_110426 (2026-11-05, none stated) https://huggingface.co/georgeliu59/caption_qwen35_9b_trainset_retrieval_benchmark_110426; [dataset/huggingface] crawlcheck/vendor-benchmark (2026-11-05, cc-by-4.0) https://huggingface.co/datasets/crawlcheck/vendor-benchmark; [dataset/huggingface] Tushar29k/voice-agent-adversarial-benchmark (2026-11-05, none stated) https://huggingface.co/datasets/Tushar29k/voice-agent-adversarial-benchmark; [paper/nature] Altered axonal initial segment development links circuit and Kv7 dysfunction in an Fmr1 knockout rat (2026-09-12, journal-article) https://doi.org/10.1038/s42003-026-10958-7; [paper/nature] GABA and glutamate interplay during tactile processing: an fMRS study (2026-09-01, journal-article) https://doi.org/10.1038/s42003-026-09547-5

**Why asked.** work_order entry NEED-INHIBITORY-HYPOFUNCTION [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 4e96385baf, main 8c7c46cf47b4]: "In the Wwox neuron-deleted neocortical slice, is the lost fast GABA-A inhibition the step that makes bursting "

**If confirmed (decision).** A heterozygote with inhibition like the knockout would put the NMDAR/excitatory-gain readings first; a knockout-specific receptor-limited loss would make positi Roadmap: R3.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-05 · scout_daily · Discovery:work_order:NEED-ISR-ATTENUATION

**WWOX question.** Is the ISR kinase arm active at all in WWOX-deficient neural cells, and is it compensatory or harmful? After the mouse P17 transcripts the s

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] 6nguyen/cut-israel-ties (2026-11-05, none stated) https://github.com/6nguyen/cut-israel-ties; [repository/github] arielf-idra/notam-isr (2026-11-05, MIT) https://github.com/arielf-idra/notam-isr; [repository/github] RokuIL/Live-From-Israel (2026-11-05, none stated) https://github.com/RokuIL/Live-From-Israel; [model/huggingface] israel-adewuyi/AlphabetSort (2026-11-04, none stated) https://huggingface.co/israel-adewuyi/AlphabetSort; [dataset/huggingface] israel-adewuyi/tinystories_african (2026-11-04, none stated) https://huggingface.co/datasets/israel-adewuyi/tinystories_african; [dataset/huggingface] Hebrish/Israeli-Name-Sentences (2026-11-03, cc-by-4.0) https://huggingface.co/datasets/Hebrish/Israeli-Name-Sentences

**Why asked.** work_order entry NEED-ISR-ATTENUATION [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 4e96385baf, main 8c7c46cf47b4]: "Is the ISR kinase arm active at all in WWOX-deficient neural cells, and is it compensatory or harmful? After t"

**If confirmed (decision).** A measured elevation would give the need its first controlled WWOX-system row on the pathway; a flat result removes the premise of F3 for card E01. Transcripts  Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-06 · scout_daily · Discovery:work_order:NEED-LACTATE-LDH

**WWOX question.** Is LDH activity or lactate raised in WWOX-deficient neural cells? (IT8 P3 2026-10-29: the former second half of this question, whether stiri

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Exploring Cross-Sectional and Longitudinal Associations Among DNA Methylation, Prognostic Proteins, and Symptoms in Patients Prescribed Oral (2026-10-08, published record) https://europepmc.org/article/MED/42848710; [paper/europepmc] LDH-related Metabolic Alterations in Alzheimer's Disease: Evidence from Clinical and Transcriptomic Analyses. (2026-09-01, published record) https://europepmc.org/article/MED/42870594; [preprint/europepmc] Drosophila melanogaster  lactate dehydrogenase deficiency recapitulates the exercise intolerance of human glycogen storage disease type XI (2026-07-10, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1277259; [repository/github] luccabruno3z/luccabruno3z.github.io (2026-11-06, none stated, default-branch head e68b8fb21c94 2026-11-06, release none published) https://github.com/luccabruno3z/luccabruno3z.github.io; [repository/github] luccabruno3z/ldh-lol (2026-11-06, none stated, default-branch head 359854340e6d 2026-11-05, release timelines 2026-10-30) https://github.com/luccabruno3z/ldh-lol; [repository/github] ldhawka/ldhawka.github.io (2026-11-05, none stated, default-branch head 7644641f84d8 2026-11-05, release none published) https://github.com/ldhawka/ldhawka.github.io; [model/huggingface] gschottlender/graphmatch-bioactivity-models (2026-09-21, none stated) https://huggingface.co/gschottlender/graphmatch-bioactivity-models; [model/huggingface] prime7781/drug-bioactivity-predictor (2026-08-24, mit) https://huggingface.co/prime7781/drug-bioactivity-predictor; [dataset/huggingface] Sepideh2027/Bioactivity-Bench (2026-07-23, none stated) https://huggingface.co/datasets/Sepideh2027/Bioactivity-Bench; [paper/nature] Structural characterization and CO2 adsorption enhancement of synthesized calcined flower-like Mg–Al LDH@γ-Al2O3 (2026-09-20, journal-article) https://doi.org/10.1038/s41598-026-72292-6; [paper/nature] Interface-driven electrocatalytic activity of NiFe-LDH on MnO2-modified SWCNT hierarchical nanostructures for overall water splitting (2026-09-15, journal-article) https://doi.org/10.1038/s41598-026-66726-4

**Why asked.** work_order entry NEED-LACTATE-LDH [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 4e96385baf, main 0845ed06e8d0]: "Is LDH activity or lactate raised in WWOX-deficient neural cells? (IT8 P3 2026-10-29: the former second half o"

**If confirmed (decision).** If lactate is not raised, the need loses its WWOX observation and E02 moves to P3 by rule; if raised, the node is tested with a nanomolar human-LDHA inhibitor,  Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-06 · scout_daily · Discovery:work_order:NEED-MYC-PROGENITOR-PROLIFERATION

**WWOX question.** Is the MYC rise in WWOX-deficient radial glia a driver, a marker of retained progenitor state or a consequence of the cell-cycle shift, and 

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] MYC-driven gliosis impairs neuron-glia communication in amyotrophic lateral sclerosis. (2026-05-01, published record) https://europepmc.org/article/MED/41004427; [paper/europepmc] Walnut-Derived Extracellular Vesicles Orchestrate a Pre-Regenerative Niche via c-Myc Mediated Metabolic Reprogramming. (2026-07-01, published record) https://europepmc.org/article/MED/42206567; [paper/europepmc] Microglial ADGRG1: AD glial resilience generator. (2025-10-01, published record) https://europepmc.org/article/MED/41038155; [repository/github] anttiluode/TheMycelialCortex (2026-06-16, MIT) https://github.com/anttiluode/TheMycelialCortex; [repository/github] GautamGripen/NeuronWiseLabs-MyCodeBackups (2026-04-13, none stated) https://github.com/GautamGripen/NeuronWiseLabs-MyCodeBackups; [space/huggingface] Sepideh2027/ligand-bioactivity-predictor (2026-07-23, none stated) https://huggingface.co/spaces/Sepideh2027/ligand-bioactivity-predictor; [dataset/huggingface] Ni3SinghR/provbench-egfr-bioactivity (2026-06-29, cc-by-sa-3.0) https://huggingface.co/datasets/Ni3SinghR/provbench-egfr-bioactivity; [model/huggingface] JuliTech-001/Druglikeness-bioactivity-model (2026-03-19, none stated) https://huggingface.co/JuliTech-001/Druglikeness-bioactivity-model

**Why asked.** work_order entry NEED-MYC-PROGENITOR-PROLIFERATION [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 4e96385baf, main 0845ed06e8d0]: "Is the MYC rise in WWOX-deficient radial glia a driver, a marker of retained progenitor state or a consequence"

**If confirmed (decision).** If MYC difference vanishes within cell-cycle and potency strata, MYC is a marker and the need moves to inert for lever purposes. If genetic MYC lowering moves n Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-06 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] Exynos-8890/gptr-bench (2026-11-05, Apache-2.0) https://github.com/Exynos-8890/gptr-bench; [repository/github] cw-jlu/Drug-Repurposing-Agent (2026-10-03, none stated) https://github.com/cw-jlu/Drug-Repurposing-Agent; [repository/github] RyanWangZf/BioDSA (2026-09-30, MIT) https://github.com/RyanWangZf/BioDSA; [model/huggingface] SINAI/ALIA-es-biomedical-7B-Instruct (2026-11-03, apache-2.0) https://huggingface.co/SINAI/ALIA-es-biomedical-7B-Instruct; [model/huggingface] Alberto/ALIA-es-biomedical-7B-Instruct-gguf (2026-11-01, apache-2.0) https://huggingface.co/Alberto/ALIA-es-biomedical-7B-Instruct-gguf; [model/huggingface] mradermacher/Gemma4-Biomedical-E4B-GGUF (2026-10-28, apache-2.0) https://huggingface.co/mradermacher/Gemma4-Biomedical-E4B-GGUF

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-07 · scout_daily · PubMed:wwox_any

**WWOX question.** New WWOX paper or external precedent that could reopen a research question

**Contribution vs existing.** not checked against the registry (never grepped); intake triage decides new vs already read

**Detected.** 42991897 Population-specific differences in ClinVar pathogenic and likely pathogenic variants of ep

**Cost / licence.** abstract screen: minutes; a full read needs its receipt; PubMed metadata; full text per paper.

**Proof.** https://pubmed.ncbi.nlm.nih.gov/?term=42991897

**Outcome.** TO_TRIAGE (abstract = discovery, not a reading)

## 2026-11-07 · scout_daily · Discovery:task_step:OBJ_P8/P8

**WWOX question.** P8 Pharmacological comparisons incl. AEDs

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Risks of neurodevelopmental disorders after prenatal exposure to antiepileptic drugs. (2026-09-14, published record) https://europepmc.org/article/MED/42736039; [paper/europepmc] Prophylactic Antiepileptic Drugs in Nontraumatic Intracerebral Hemorrhage: A Network Meta-Analysis. (2026-05-05, published record) https://europepmc.org/article/MED/42087030; [paper/europepmc] Assessment of Preparedness for Medical Emergencies in Saudi Dental Colleges: A National Cross-Sectional Study. (2026-10-25, published record) https://europepmc.org/article/MED/42928625; [repository/github] the-sunnyy/fx (2026-11-07, none stated, default-branch head 5c1b1e17b252 2026-11-07, release none published) https://github.com/the-sunnyy/fx; [repository/github] cecattot/tipos_abstratos_dados (2026-11-07, none stated, default-branch head cc814a5d016a 2026-11-07, release none published) https://github.com/cecattot/tipos_abstratos_dados; [repository/github] GersonPardim/Simulador_Interativo_de_-Arvores (2026-11-07, none stated, default-branch head 1e25b3034fb2 2026-11-07, release none published) https://github.com/GersonPardim/Simulador_Interativo_de_-Arvores; [model/huggingface] Shoriful025/molecular_bioactivity_predictor_gnn (2026-01-08, mit) https://huggingface.co/Shoriful025/molecular_bioactivity_predictor_gnn; [model/huggingface] aksw/Bike-bioactivity (2025-11-24, apache-2.0) https://huggingface.co/aksw/Bike-bioactivity; [space/huggingface] fatmamattar/bioactivity-predictor (2025-06-21, none stated) https://huggingface.co/spaces/fatmamattar/bioactivity-predictor; [paper/nature] An artifact audit of budget-dependent LoRA rank comparisons (2026-11-05, journal-article) https://doi.org/10.1038/s41598-026-78535-w; [paper/nature] Stage harmonized temporal survival comparisons in de novo metastatic breast cancer using SEER (2026-11-04, journal-article) https://doi.org/10.1038/s41598-026-77501-w

**Why asked.** task_step ORCH-ROADMAP-IT31-20261106 OBJ_P8 step P8 [TODO] [ledger/tasks/orchestrator/ORCH-ROADMAP-IT31-20261106.json @ blob 87f4985c9d, main 25a01f7a524d]: "P8 Pharmacological comparisons incl. AEDs"

**If confirmed (decision).** step P8 (orchestrator): whether a found method/resource changes how it is done Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-07 · scout_daily · Discovery:work_order:NEED-MYELINATION

**WWOX question.** Does vigabatrin or CPP-115 exposure add myelin injury in a Wwox-deficient juvenile model, given the baseline white-matter loss in the human 

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Pharmacokinetics of Loading Dose Vigabatrin Administered via Enteral Tube in Participants With Post-Anoxic Status Epilepticus. (2026-10-01, published record) https://europepmc.org/article/MED/42723519; [paper/europepmc] Vigabatrin-related MRI changes and tapering strategy in hemispherotomy for infantile spasms: illustrative case. (2026-07-13, published record) https://europepmc.org/article/MED/42441989; [paper/europepmc] Microstructural injury to the optic nerve with vigabatrin treatment in West syndrome: A DTI study. (2025-07-16, published record) https://europepmc.org/article/MED/40670421

**Why asked.** work_order entry NEED-MYELINATION [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 25a01f7a524d]: "Does vigabatrin or CPP-115 exposure add myelin injury in a Wwox-deficient juvenile model, given the baseline w"

**If confirmed (decision).** A clean absence of added injury would move H02 to a position without harm rows; its presence would make the sibling tag a card-level C3 for vigabatrin as well. Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-07 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] AikyaKumar/hetionet-drug-repurposing (2026-11-06, none stated) https://github.com/AikyaKumar/hetionet-drug-repurposing; [repository/github] medical-device-design/FDA-kg (2026-11-05, none stated) https://github.com/medical-device-design/FDA-kg; [repository/github] Harsheys27/BioLens (2026-11-05, none stated) https://github.com/Harsheys27/BioLens; [dataset/huggingface] Venkat071989/superkart-sales-prediction (2026-11-07, none stated) https://huggingface.co/datasets/Venkat071989/superkart-sales-prediction; [space/huggingface] sadansabo/Nigerian_National_Flood_Prediction_System (2026-11-07, none stated) https://huggingface.co/spaces/sadansabo/Nigerian_National_Flood_Prediction_System; [space/huggingface] soradash/stock-ai-prediction (2026-11-07, none stated) https://huggingface.co/spaces/soradash/stock-ai-prediction

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-08 · scout_daily · Discovery:work_order:NEED-NEUROINFLAMMATION-GLIA

**WWOX question.** Is glial density in a Wwox-deficient brain below, equal to or above wild type before the first spike? The sign conflicts between species, so

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Harnessing Neurogenic Potential of Glial Cell Types as an Emerging Strategy for Treating Epilepsy. (2026-10-15, published record) [+1 mirror(s) merged] https://europepmc.org/article/MED/42941915; [paper/europepmc] Biofluid Biomarkers of Neuronal and Glial Injury in Epilepsy and Seizures: A Comprehensive Review. (2026-10-03, published record) https://europepmc.org/article/MED/42884085; [model/huggingface] diamandislabii/ViT-Glial-Tumor-Classification (2025-06-16, none stated, revision f70e4cd93758, 4 files) https://huggingface.co/diamandislabii/ViT-Glial-Tumor-Classification; [paper/nature] Disrupted glial-mediated synaptic refinement in Fragile X syndrome (2026-10-25, journal-article) https://doi.org/10.1038/s41598-026-75819-z; [paper/nature] Conversational brain AI for adaptive epilepsy care (2026-10-16, journal-article) https://doi.org/10.1038/s41591-026-04719-6

**Why asked.** work_order entry NEED-NEUROINFLAMMATION-GLIA [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 0a3a34f95c41]: "Is glial density in a Wwox-deficient brain below, equal to or above wild type before the first spike? The sign"

**If confirmed (decision).** It decides whether this need is a readout, a seizure consequence or a seizure-independent lever. Until then no glial modulator is proposed, and no position move Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-08 · scout_daily · Discovery:work_order:NEED-PDH-PYRUVATE-AXIS

**WWOX question.** Is PDH phosphorylation higher in WWOX-deficient neural cells, and does a PDK inhibitor change it in a genotype-dependent way without lowerin

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Shaoyao Gancao Decoction alleviates ulcerative colitis-associated secondary liver injury by inhibiting the phosphorylation of pyruvate dehyd (2026-04-04, published record) https://europepmc.org/article/MED/41941988; [paper/europepmc] The pyruvate dehydrogenase complex at the crossroads of cancer metabolism and cell death. (2026-07-01, published record) https://europepmc.org/article/MED/42462696; [paper/europepmc] BICC1 attenuates oxidative stress-induced osteogenic injury via regulation of the PDK/PDH axis in MC3T3-E1 cells. (2026-09-08, published record) https://europepmc.org/article/MED/42709265; [repository/github] pdh9311/pdh9311 (2026-11-08, none stated, default-branch head c0098a626655 2026-11-08, release none published) https://github.com/pdh9311/pdh9311; [repository/github] AmanSingh1812/btcusdt-scalper-paper-trading (2026-11-08, none stated, default-branch head 766f83a7c30a 2026-11-08, release none published) https://github.com/AmanSingh1812/btcusdt-scalper-paper-trading; [repository/github] AmanSingh1812/btcusdt-scalper-highfreq-paper-trading (2026-11-08, none stated) https://github.com/AmanSingh1812/btcusdt-scalper-highfreq-paper-trading; [dataset/huggingface] MLL-Lab/MultiBBQ-perturbations (2026-11-07, cc-by-4.0) https://huggingface.co/datasets/MLL-Lab/MultiBBQ-perturbations; [dataset/huggingface] ChicagoHAI/openaireview-perturbation (2026-11-02, other) https://huggingface.co/datasets/ChicagoHAI/openaireview-perturbation; [dataset/huggingface] anuosi666/Perturbation-response-identification (2026-10-20, none stated) https://huggingface.co/datasets/anuosi666/Perturbation-response-identification

**Why asked.** work_order entry NEED-PDH-PYRUVATE-AXIS [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 0a3a34f95c41]: "Is PDH phosphorylation higher in WWOX-deficient neural cells, and does a PDK inhibitor change it in a genotype"

**If confirmed (decision).** A genotype-by-inhibitor interaction would give the first WWOX-system row for DCA on this need; the known glucose-lowering and neuropathy signals would remain as Roadmap: R2.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-08 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] carson-olaf/mva-hackathon-2026 (2026-10-30, NOASSERTION) https://github.com/carson-olaf/mva-hackathon-2026; [repository/github] api-evangelist/healx (2026-10-30, none stated) https://github.com/api-evangelist/healx; [repository/github] neonbhai/mva-research (2026-10-29, none stated) https://github.com/neonbhai/mva-research; [space/huggingface] Darkweb007/content-repurposing-pipeline (2026-06-23, none stated) https://huggingface.co/spaces/Darkweb007/content-repurposing-pipeline; [space/huggingface] DiyaR2002/drug-repurposing (2026-06-13, none stated) https://huggingface.co/spaces/DiyaR2002/drug-repurposing; [space/huggingface] vrindagotephd/Clinical_Trials_Drug_Repurposing_AI_Tool (2026-06-11, none stated) https://huggingface.co/spaces/vrindagotephd/Clinical_Trials_Drug_Repurposing_AI_Tool

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-09 · scout_daily · Discovery:work_order:NEED-REDOX-NRF2

**WWOX question.** In WWOX-deficient versus isogenic corrected human neural cells that include microglia or CNS-macrophage-like cells, are NRF2 target activity

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Selective NRF2 target induction despite falling NFE2L2 transcription across the MASLD spectrum: implications for marginal donor grafts and K (2026-10-20, published record) https://europepmc.org/article/MED/42901279; [paper/europepmc] Variant-informed multimodal tissue-state modeling reveals an NRF2 stress niche and dependency axis in KEAP1/NFE2L2-altered cancer. (2026-10-06, published record) https://europepmc.org/article/MED/42903351; [paper/europepmc] The KEAP1-NFE2L2/NRF2 Axis in Non-Small Cell Lung Cancer Radioresistance: Redox Homeostasis and Emerging DNA Damage Response Mechanisms. (2026-09-03, published record) https://europepmc.org/article/MED/42708106; [repository/github] kireol/nrf24l01SenderNodeMcu (2026-11-08, MIT, default-branch head 705604a444fb 2016-09-09, release none published) https://github.com/kireol/nrf24l01SenderNodeMcu; [repository/github] AtherNet29/BW-16-RTL8720DN-DEAUTHER-EVILTWIN-NRF24 (2026-11-08, none stated, default-branch head ac8815017131 2026-11-08, release none published) https://github.com/AtherNet29/BW-16-RTL8720DN-DEAUTHER-EVILTWIN-NRF24; [repository/github] mrdulasolutions/MCAS.Opensource (2026-11-08, NOASSERTION, default-branch head 5b01f0f1563e 2026-11-08, release v0.2.0 2026-07-27) https://github.com/mrdulasolutions/MCAS.Opensource; [dataset/huggingface] aikseng/Kras-Nrf2-Dataset (2025-08-12, mit) https://huggingface.co/datasets/aikseng/Kras-Nrf2-Dataset; [paper/nature] Beauvericin exhibits antitumor activity in pancreatic cancer cells: Integrative analysis suggests potential modulation of the KEAP1-NRF2-HMO (2026-09-20, journal-article) https://doi.org/10.1038/s41598-026-72126-5; [paper/nature] PCHP‑1 A from Polygonatum cyrtonema Hua alleviates APAP‑induced acute liver injury via Nrf2/Keap1 and NF‑κB pathways (2026-09-03, journal-article) https://doi.org/10.1038/s41598-026-70075-7

**Why asked.** work_order entry NEED-REDOX-NRF2 [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 4d10771c21ae]: "In WWOX-deficient versus isogenic corrected human neural cells that include microglia or CNS-macrophage-like c"

**If confirmed (decision).** If neither ROS nor NRF2 tone nor cytokine protein differs and activation changes nothing: the axis moves to inert and the card is closed. If ROS is raised and a Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-09 · scout_daily · Discovery:work_order:NEED-SEIZURE-CONTROL-SYMPTOMATIC

**WWOX question.** Is the ethosuximide late-phase effect reproducible with a drug-by-genotype test and a same-day control, is the lithium effect genotype-speci

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Cannabidiol reduces atypical absence seizures and epileptic spasms in a Gabrb3+/D120N mouse model of Lennox-Gastaut syndrome. (2026-06-11, published record) https://europepmc.org/article/MED/42274296; [paper/europepmc] Case Report: Adenylosuccinate lyase deficiency type I caused by splicing disruption due to a novel missense variant in the ADSL gene. (2025-10-24, published record) https://europepmc.org/article/MED/41211455; [paper/europepmc] From barbiturates to ganaxolone: The importance of chirality in drug development and in understanding the actions of old and new antiseizure (2025-02-05, published record) https://europepmc.org/article/MED/39920975; [dataset/huggingface] elsiddik/egypt-real-estate-prices-compounds-2026 (2026-11-05, cc-by-4.0) https://huggingface.co/datasets/elsiddik/egypt-real-estate-prices-compounds-2026; [dataset/huggingface] cora-health/peptide-compounding-status-index (2026-11-03, cc-by-4.0) https://huggingface.co/datasets/cora-health/peptide-compounding-status-index; [dataset/huggingface] molport/In-stock-Screening-Compound-Database (2026-10-08, cc-by-nc-4.0) https://huggingface.co/datasets/molport/In-stock-Screening-Compound-Database

**Why asked.** work_order entry NEED-SEIZURE-CONTROL-SYMPTOMATIC [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 4d10771c21ae]: "Is the ethosuximide late-phase effect reproducible with a drug-by-genotype test and a same-day control, is the"

**If confirmed (decision).** A reproduced interaction would give an F1 on the T-type and seizure needs; a not-reproduced one gives C1. For the diet and vigabatrin the denominators decide wh Roadmap: R2.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-09 · scout_daily · Follow:mims-harvard/ToolUniverse

**WWOX question.** live-lookup layer tried on a capability the adapters lack

**Contribution vs existing.** followed since 2026-11-01 (WATCH ToolUniverse; tooluniverse_capability_test_20261026.md)

**Detected.** default-branch head 99b81ebec84f -> e3a819ff1f8d; latest release {"date": "2026-11-01", "tag": "v1.5.8"} -> {"date": "2026-11-05", "tag": "v1.5.9"}

**If confirmed (decision).** reopen condition: a capability the adapters lack becomes available, or terms change Roadmap: R9.

**Cost / licence.** reading the change: minutes; see source.

**Proof.** https://github.com/mims-harvard/ToolUniverse

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-09 · scout_daily · Follow:everycure-org/matrix

**WWOX question.** open drug-disease score matrix, inconclusive trial

**Contribution vs existing.** followed since 2026-11-01 (WATCH EveryCure-MATRIX-code; p3b1/txgnn_matrix_outcomes_20261026.md)

**Detected.** default-branch head 96fd24ce4aee -> 233511014e57; latest release {"date": "2026-02-05", "tag": "v0.15.0-matrix"} -> {"date": "2026-02-05", "tag": "v0.15.0-matrix"}

**If confirmed (decision).** reopen condition: a stated licence for the scores table, or a code/data release Roadmap: R9.

**Cost / licence.** reading the change: minutes; see source.

**Proof.** https://github.com/everycure-org/matrix

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-10 · scout_daily · EveryCure-MATRIX-scores

**WWOX question.** Has a licence for the scores table been stated (the stated reopening condition)?

**Contribution vs existing.** p3b1/txgnn_matrix_outcomes_20261026.md: scores table declared no licence on 2026-10-26

**Detected.** card_oid: '0c542d0a858e574deb6ae9293ce05646ce94e242' -> '011677840b8ea1a4c797ea3f0953c261c75548af'; sha: 'd6b121bf38112cf28e7c813d0a062651757c52a1' -> '4a53314d0d354844464abd98409a406c42930691'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; see source.

**Proof.** https://github.com/everycure/matrix-scores/releases

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-10 · scout_daily · EveryCure-kg-nodes

**WWOX question.** Did the MATRIX knowledge-graph nodes change content or terms (graph terms are separate; upstream licences stay in force)?

**Contribution vs existing.** p3b1/txgnn_matrix_outcomes_20261026.md section 2.1

**Detected.** card_oid: '807c5cc867fd73f88fc6f19af8cce483502169a0' -> '876c65ddabb4c5fbc63e7369863823f702dbbaf0'; sha: 'c9c60b2c55e72cedb757b0422f4ea160a9bffc5c' -> 'cfb7d6579105ee73ba72b34717f9f2c8b0d0f90d'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; other.

**Proof.** https://github.com/everycure/kg-nodes/releases

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-10 · scout_daily · EveryCure-kg-edges

**WWOX question.** Did the MATRIX knowledge-graph edges change content or terms (separate from nodes, scores, code)?

**Contribution vs existing.** p3b1/txgnn_matrix_outcomes_20261026.md section 2.1

**Detected.** card_oid: '368ec637d86abcf0f33088e2dd2c1421c077c967' -> '99db56bc72c682da8eb3dd685e4efbb67a1b3823'; sha: 'fcd0585957ab5137771b256dad3714dcaf44b7db' -> '4b6fd25467fcb4499058024cc9da80514db8dd31'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; other.

**Proof.** https://github.com/everycure/kg-edges/releases

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-10 · scout_daily · Discovery:work_order:NEED-SYSTEMIC-GLYCAEMIA-GROWTH

**WWOX question.** Is the P10 glucose difference real (knockout about 95, wild type about 130), and does any dose of the vector correct it? It would resolve th

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Anatomy-aware, label-informed approach improves image registration for challenging datasets. (2026-09-08, published record) https://europepmc.org/article/MED/42709748; [preprint/europepmc] A guide to selecting high-performing renewable antibodies for KIF5A (Q12840) across western blot, immunoprecipitation, and immunofluorescenc (2026-06-30, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1283125; [paper/europepmc] Inadequate antibody validation places substantial numbers of animal and human tissue samples at risk of waste. (2026-10-06, published record) https://europepmc.org/article/MED/42837326; [dataset/huggingface] wraith1337/knockout-cup-windows64 (2026-11-09, none stated, revision 4eb40ed51242, 1 files) https://huggingface.co/datasets/wraith1337/knockout-cup-windows64; [model/huggingface] reax-knockout/sn92-gen-a1 (2026-10-21, apache-2.0, revision d57f18b92547, 26 files) https://huggingface.co/reax-knockout/sn92-gen-a1; [model/huggingface] suchirsalhan/polypythia-160m-knockout-continue (2026-09-21, apache-2.0, revision f253c185e1c2, 344 files) https://huggingface.co/suchirsalhan/polypythia-160m-knockout-continue; [paper/nature] Estimated glucose disposal rate is associated with continuous glucose monitoring metrics in type 1 diabetes (2026-10-15, journal-article) https://doi.org/10.1038/s41598-026-75846-w; [paper/nature] In-race continuous glucose monitoring in highly trained male distance runners: a context-dependent reversal of the glucose–performance assoc (2026-10-08, journal-article) https://doi.org/10.1038/s41598-026-74914-5

**Why asked.** work_order entry NEED-SYSTEMIC-GLYCAEMIA-GROWTH [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 975535a93695]: "Is the P10 glucose difference real (knockout about 95, wild type about 130), and does any dose of the vector c"

**If confirmed (decision).** It would resolve the two glucose rows and either remove the C2 or make it a C1. Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-10 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] rasel-isu/biomedical-AI-benchmark (2026-08-09, none stated) https://github.com/rasel-isu/biomedical-AI-benchmark; [repository/github] nithin-jella/RareDx-Agentic-Diagnostic-Assistant (2026-08-06, none stated) https://github.com/nithin-jella/RareDx-Agentic-Diagnostic-Assistant; [repository/github] AI-in-Health/BioMedArena (2026-06-25, MIT) https://github.com/AI-in-Health/BioMedArena; [dataset/huggingface] MohsinElis/biomedical-disease-mapping (2026-11-07, mit) https://huggingface.co/datasets/MohsinElis/biomedical-disease-mapping; [model/huggingface] edh1/gemma4-biomedical-e4b-litertlm (2026-10-25, gemma) https://huggingface.co/edh1/gemma4-biomedical-e4b-litertlm; [space/huggingface] fatenahaq/biomedical-research-ai (2026-10-20, none stated) https://huggingface.co/spaces/fatenahaq/biomedical-research-ai

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-11 · scout_daily · PubMed:wwox_any

**WWOX question.** New WWOX paper or external precedent that could reopen a research question

**Contribution vs existing.** not checked against the registry (never grepped); intake triage decides new vs already read

**Detected.** 43004178 Genetic and regulatory architecture of meat yield traits in commercial pig populations.

**Cost / licence.** abstract screen: minutes; a full read needs its receipt; PubMed metadata; full text per paper.

**Proof.** https://pubmed.ncbi.nlm.nih.gov/?term=43004178

**Outcome.** TO_TRIAGE (abstract = discovery, not a reading)

## 2026-11-11 · scout_daily · Discovery:work_order:NEED-WWOX-GENE-ADDITION

**WWOX question.** Does an intermediate vector level separate a threshold from a gradient, and is the benefit only prevented inside the first days of life or a

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Quantized large language models in biomedical natural language processing: evaluation and recommendation. (2026-11-04, published record) https://europepmc.org/article/MED/42982917; [preprint/europepmc] The Temporal Validity of Taxonomic Entailments in Evolving Biomedical Ontologies (2026-11-04, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1358204; [preprint/europepmc] Quantifying performance inflation from hidden sample dependence in biomedical image classification benchmarks (2026-10-08, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1337091; [repository/github] ipb-halle/MetFamily (2026-10-21, GPL-2.0, default-branch head a54924fec7b6 2026-10-21, release 1.0 2019-03-27) https://github.com/ipb-halle/MetFamily; [repository/github] Ivan-Cheuk0/DSM5TR-NLP-Transdiagnostic (2026-10-19, none stated, default-branch head 1357c9852115 2026-10-19, release none published) https://github.com/Ivan-Cheuk0/DSM5TR-NLP-Transdiagnostic; [repository/github] nepalanurag/Biomedical-Imaging-Analysis (2026-10-16, none stated, default-branch head fc46054946d8 2026-10-16, release none published) https://github.com/nepalanurag/Biomedical-Imaging-Analysis; [space/huggingface] Jeev321/Quantified_Self (2026-01-12, none stated) https://huggingface.co/spaces/Jeev321/Quantified_Self; [space/huggingface] GatewayInc/gateway-wealth-bridge-quantified-gold-rush (2025-10-21, none stated) https://huggingface.co/spaces/GatewayInc/gateway-wealth-bridge-quantified-gold-rush; [space/huggingface] Quantified/Clip-Generator-V3-Server (2024-11-19, none stated) https://huggingface.co/spaces/Quantified/Clip-Generator-V3-Server; [paper/nature] Structure-property correlations of alkaline-free extracted cellulose nanocrystals for prospective biomedical applications (2026-09-16, journal-article) https://doi.org/10.1038/s41598-026-71481-7; [paper/nature] Impact of adpkd-associated PKD1 gene variants on the human facial phenotype quantified by 3d geometric morphometry (2026-08-13, journal-article) https://doi.org/10.1038/s41598-026-65632-z

**Why asked.** work_order entry NEED-WWOX-GENE-ADDITION [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 3f8f17fb9598]: "Does an intermediate vector level separate a threshold from a gradient, and is the benefit only prevented insi"

**If confirmed (decision).** Quantified myelination would add a controlled row on the same need; a failure would move the card to C2 by rule; a treated-after-onset arm would show whether th Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-11 · scout_daily · Discovery:work_order:NEED-WWOX-MISSENSE-PROTEIN-RESCUE

**WWOX question.** Is the Q230P-class protein made and then cleared, by which route (proteasome, lysosome), and does any protein that returns carry function pe

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Molecular pathogenesis and gene therapy-based intervention of GTPBP3-related mitochondrial disease. (2026-04-09, published record) https://europepmc.org/article/MED/41957021

**Why asked.** work_order entry NEED-WWOX-MISSENSE-PROTEIN-RESCUE [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 3f8f17fb9598]: "Is the Q230P-class protein made and then cleared, by which route (proteasome, lysosome), and does any protein "

**If confirmed (decision).** No protein with synthesis present closes A02 and A05 for this allele; soluble native protein on the ruler would give the first WWOX-system row on the need; prot Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-11 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] glusman-team/graph-monorepo (2026-11-10, Apache-2.0) https://github.com/glusman-team/graph-monorepo; [repository/github] GKHarjithadithyha/medsafe (2026-11-10, none stated) https://github.com/GKHarjithadithyha/medsafe; [repository/github] oncodash/oncodashkb (2026-11-10, none stated) https://github.com/oncodash/oncodashkb; [dataset/huggingface] JiaxinShi/lychsim-genia-pasr-predictions-20261106 (2026-11-11, none stated) https://huggingface.co/datasets/JiaxinShi/lychsim-genia-pasr-predictions-20261106; [model/huggingface] Noor-Khan/dog-breed-prediction (2026-11-10, mit) https://huggingface.co/Noor-Khan/dog-breed-prediction; [dataset/huggingface] LundAISociety/hot-building-predictions (2026-11-10, odbl) https://huggingface.co/datasets/LundAISociety/hot-building-predictions

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-12 · scout_daily · Monarch-app

**WWOX question.** Phenotype/disease KG API changes

**Contribution vs existing.** kg_thin_slice.py uses it

**Detected.** release: 'v1.32.0-rc1' -> 'v1.32.0'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; BSD-3-Clause.

**Proof.** https://github.com/monarch-initiative/monarch-app/releases

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-12 · scout_daily · Discovery:reopen:biopathnet_it18_20261101/0

**WWOX question.** BioPathNet (emyyue/BioPathNet b051a900, gene-function checkpoint model_epoch_12) Reopen if any of: (1) explanation for one query runs in <= 

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [preprint/europepmc] MC-Bayes: A Python-based wrapper for MotionCor3 processing of EER files compatible with Bayesian polishing (2026-08-07, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1294466; [paper/europepmc] Memory-Saving Version of k-Wave Toolbox for Single-Frequency Simulations. (2026-09-22, published record) https://europepmc.org/article/MED/42784474; [preprint/europepmc] QRAFT: Scaling coalescent-based species tree inference to one million taxa (2026-11-06, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1361066; [repository/github] Rameshsain070/Rameshsain070 (2026-11-12, none stated, default-branch head 40a7ff800964 2026-11-12, release none published) https://github.com/Rameshsain070/Rameshsain070; [repository/github] Gnanasudharsan/ramp-accessibility-agent (2026-11-12, MIT, default-branch head 19e4bf5a1263 2026-11-12, release none published) https://github.com/Gnanasudharsan/ramp-accessibility-agent; [repository/github] ramazantufekci/ramazantufekci (2026-11-12, AGPL-3.0, default-branch head 5197f370f323 2026-11-12, release 8 2025-10-07) https://github.com/ramazantufekci/ramazantufekci; [model/huggingface] realnewbiexvwu/pvz-agent-artifacts (2026-11-12, lgpl-3.0) https://huggingface.co/realnewbiexvwu/pvz-agent-artifacts; [model/huggingface] hmkz-1981/gemma-4-e4b-agentic-rl-think-effort-GGUF (2026-11-12, apache-2.0) https://huggingface.co/hmkz-1981/gemma-4-e4b-agentic-rl-think-effort-GGUF; [model/huggingface] LoosiFR/qwen35-9b-agentic-v2.5-GGUF (2026-11-12, none stated) https://huggingface.co/LoosiFR/qwen35-9b-agentic-v2.5-GGUF; [paper/nature] Data-driven and physics-guided neural approaches for LCR circuit modeling: a comparative analysis (2026-10-22, journal-article) https://doi.org/10.1038/s41598-026-74713-y; [paper/nature] A lightweight privacy-aware federated vision transformer for tomato leaf disease classification (2026-10-14, journal-article) https://doi.org/10.1038/s41598-026-65968-6

**Why asked.** reopen biopathnet_it18_20261101 table row 0 [WATCH - explanations not] [disease-models/wwox/research/drug_repurposing/biopathnet_it18_20261101/decisions.tsv @ blob 6b733ad502, main 940182af525c]: "BioPathNet (emyyue/BioPathNet b051a900, gene-function checkpoint model_epoch_12) Reopen if any of: (1) explana"

**If confirmed (decision).** reopen condition met? Reopen if any of: (1) explanation for one query runs in <= 8 GB RAM on CPU (e.g. an upstream subgraph-restricted explain mode, or a host wit Roadmap: R9/R12.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-12 · scout_daily · Discovery:reopen:function_pharm_it14_p3_20261101/NP3P1

**WWOX question.** Heterozygote versus wild-type sIPSC (amplitude and charge) in the neuron-deleted neocortical slice source data or a new report with the thre

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [preprint/europepmc] Chronic Stress Alters Dorsal Bed Nucleus of Stria Terminalis Synaptic Neurotransmission in a Dravet Syndrome Mouse Model (2026-05-21, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1235764; [paper/europepmc] Chemogenetic astrocyte modulation reduces spontaneous hippocampal discharges and metabolite changes in an epilepsy mouse model. (2025-10-25, published record) https://europepmc.org/article/MED/41137858; [paper/europepmc] A Novel Compound QO-83 Alleviates Acute and Chronic Epileptic Seizures in Rodents by Modulating KV7 Channel Activity. (2025-03-01, published record) https://europepmc.org/article/MED/40125810

**Why asked.** reopen function_pharm_it14_p3_20261101 table row NP3P1 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/reopen_searches_it14_p3.tsv @ blob abb8c8031e, main 940182af525c]: "Heterozygote versus wild-type sIPSC (amplitude and charge) in the neuron-deleted neocortical slice source data"

**If confirmed (decision).** reopen condition met? source data or a new report with the three genotypes separated Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-12 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] BoukeliaAbdelbasset/MINT-KG (2026-11-08, none stated) https://github.com/BoukeliaAbdelbasset/MINT-KG; [repository/github] stringtang/mva-hackathon-2026 (2026-10-29, none stated) https://github.com/stringtang/mva-hackathon-2026; [repository/github] api-evangelist/axcelius-i-ii (2026-10-29, none stated) https://github.com/api-evangelist/axcelius-i-ii; [dataset/huggingface] TheFamousHesham/drug-repurposing-pan (2026-06-05, none stated) https://huggingface.co/datasets/TheFamousHesham/drug-repurposing-pan; [space/huggingface] Priyabhanderi2/drug-repurposing (2026-04-07, none stated) https://huggingface.co/spaces/Priyabhanderi2/drug-repurposing; [space/huggingface] KiranKKT/Drug_Repurposing (2025-12-29, none stated) https://huggingface.co/spaces/KiranKKT/Drug_Repurposing

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-13 · scout_daily · Discovery:reopen:function_pharm_it14_p3_20261101/NP3P2

**WWOX question.** Locus of the lost sIPSC current (receptor-limited or release-limited), with a physiological-chloride internal solution an electrophysiology 

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] MAPT-A152T mutation drives neuronal hyperactivity through Fyn-NMDAR signaling in human iPSC-Derived neurons: Insights into Alzheimer's patho (2024-12-24, published record) https://europepmc.org/article/MED/39811068; [paper/europepmc] Effects of esketamine on electrophysiology and metabolic reprogramming in brain organoids: insights into antidepressant mechanisms. (2025-08-30, published record) https://europepmc.org/article/MED/40885845; [paper/europepmc] Response of iPSC-derived neurons from individuals with treatment-resistant depression to (2 R,6 R)-hydroxynorketamine and reelin: an explora (2025-11-18, published record) https://europepmc.org/article/MED/41257792; [repository/github] nmdarksky/nmdarksky.github.io (2026-10-05, none stated, default-branch head 5b2c4a468ce6 2026-10-05, release none published) https://github.com/nmdarksky/nmdarksky.github.io; [repository/github] BrainCircuitsBehaviorLab/NMDAR_paper (2026-09-30, GPL-3.0, default-branch head e77d0254382d 2026-09-30, release none published) https://github.com/BrainCircuitsBehaviorLab/NMDAR_paper; [repository/github] nmdarosa/nmdarosa.github.io (2026-09-28, none stated, default-branch head 8d8b04033248 2026-09-28, release none published) https://github.com/nmdarosa/nmdarosa.github.io; [paper/nature] Priming of human iPSCs with doxorubicin causes genome-wide transcriptional reprogramming and functional impairments in iPSC-derived cardiomy (2026-10-10, journal-article) https://doi.org/10.1038/s41536-026-00513-7; [paper/nature] Author Correction: Cryopreservable dopaminergic progenitors derived from human iPSCs with accelerated loss of pluripotency and early functio (2026-09-07, journal-article) https://doi.org/10.1038/s41531-026-01569-4

**Why asked.** reopen function_pharm_it14_p3_20261101 table row NP3P2 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/reopen_searches_it14_p3.tsv @ blob abb8c8031e, main 387f6ae49edb]: "Locus of the lost sIPSC current (receptor-limited or release-limited), with a physiological-chloride internal "

**If confirmed (decision).** reopen condition met? an electrophysiology report with the same-cell triad (isolated NMDAR current, sIPSC charge, resting potential and input resistance) and mini Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-13 · scout_daily · Discovery:reopen:function_pharm_it14_p3_20261101/NP3P3

**WWOX question.** Same-system comparison of the subtype selectivity of the GABA-A positive modulators under discussion a head-to-head in one system with diaze

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [preprint/europepmc] Systemic diazepam alters local hippocampal CA1 circuits and differentially affects entorhinal and CA3 inputs (2026-08-23, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1304123; [paper/europepmc] Chronic Chrysin, but Not Diazepam, Induces Anxiolytic-like Effects Without Behavioral Tolerance. (2026-09-10, published record) https://europepmc.org/article/MED/42796464; [paper/europepmc] Female ddY mice show a weaker diazepam-induced reduction in aggressive biting behavior toward inanimate objects and lower hypothalamic KCC2  (2026-11-05, published record) https://europepmc.org/article/MED/42988109; [repository/github] gabacorporation/gaba-corporation (2026-11-13, none stated) https://github.com/gabacorporation/gaba-corporation; [repository/github] RBPerez1701/saliksik-gabay-portal (2026-11-13, none stated) https://github.com/RBPerez1701/saliksik-gabay-portal; [repository/github] rzamora-openit/GABAI (2026-11-13, MIT) https://github.com/rzamora-openit/GABAI; [dataset/huggingface] marissadolorfino/BIOINF595_BioactivityReport (2025-04-29, mit) https://huggingface.co/datasets/marissadolorfino/BIOINF595_BioactivityReport; [dataset/huggingface] Desp-ML/Bioactivity_report_QM9 (2025-04-24, cc0-1.0) https://huggingface.co/datasets/Desp-ML/Bioactivity_report_QM9; [dataset/huggingface] Desp-ML/Bioactivity_Final_Project_QM9 (2025-04-24, none stated) https://huggingface.co/datasets/Desp-ML/Bioactivity_Final_Project_QM9

**Why asked.** reopen function_pharm_it14_p3_20261101 table row NP3P3 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/reopen_searches_it14_p3.tsv @ blob abb8c8031e, main 387f6ae49edb]: "Same-system comparison of the subtype selectivity of the GABA-A positive modulators under discussion a head-to"

**If confirmed (decision).** reopen condition met? a head-to-head in one system with diazepam as comparator Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-14 · scout_daily · Discovery:reopen:function_pharm_it14_p3_20261101/NP3P3

**WWOX question.** Same-system comparison of the subtype selectivity of the GABA-A positive modulators under discussion a head-to-head in one system with diaze

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [dataset/huggingface] luxuan-lulu/Bioactivity_Final_project (2025-04-16, mit, revision a61f6bb5f68b, 10 files) https://huggingface.co/datasets/luxuan-lulu/Bioactivity_Final_project; [model/huggingface] Brent1997/bioactivity_predictor_for_CHEMBL274_with_text_based_model (2025-04-02, none stated, revision 3fb982d5dfca, 1 files) https://huggingface.co/Brent1997/bioactivity_predictor_for_CHEMBL274_with_text_based_model; [dataset/huggingface] DanielShunom/ubiquitin-l1-hydrolase-bioactivity (2024-11-18, afl-3.0, revision eb1982013b17, 4 files) https://huggingface.co/datasets/DanielShunom/ubiquitin-l1-hydrolase-bioactivity; [paper/nature] Comparative evaluation of dexmedetomidine, diazepam, and acepromazine as adjuvants to lidocaine in intravenous regional anaesthesia in goats (2026-11-11, journal-article) https://doi.org/10.1038/s41598-026-75456-6; [paper/nature] A novel approach to cut flower preservation: pre- and postharvest application of GABA in Matthiola incana (2026-08-18, journal-article) https://doi.org/10.1038/s41598-026-67476-z

**Why asked.** reopen function_pharm_it14_p3_20261101 table row NP3P3 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/reopen_searches_it14_p3.tsv @ blob ce41d1a3c7, main 1c8ed97f15fe]: "Same-system comparison of the subtype selectivity of the GABA-A positive modulators under discussion a head-to"

**If confirmed (decision).** reopen condition met? a head-to-head in one system with diazepam as comparator (met by Ralvenius 2016 alone, with qualifications; it does not resolve the dispute) Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-14 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] mbzuai-ai4bio/BioXArena-Pro (2026-11-11, MIT) https://github.com/mbzuai-ai4bio/BioXArena-Pro; [repository/github] xX-its-amit-Xx/biocalib (2026-05-31, GPL-3.0) https://github.com/xX-its-amit-Xx/biocalib; [repository/github] boheling/skillbench (2026-05-24, MIT) https://github.com/boheling/skillbench; [dataset/huggingface] healthcare-biomedical-ai/Trauma-Resuscitation-Constraint-Verification-Benchmark (2026-11-13, none stated) https://huggingface.co/datasets/healthcare-biomedical-ai/Trauma-Resuscitation-Constraint-Verification-Benchmark; [dataset/huggingface] healthcare-biomedical-ai/Specialty-Referral-Intake-Constraint-Validation-Benchmark (2026-11-13, none stated) https://huggingface.co/datasets/healthcare-biomedical-ai/Specialty-Referral-Intake-Constraint-Validation-Benchmark; [model/huggingface] mradermacher/Bio-Medical-MultiModal-Llama-3-8B-V1-GGUF (2026-11-12, other) https://huggingface.co/mradermacher/Bio-Medical-MultiModal-Llama-3-8B-V1-GGUF

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-15 · scout_daily · ToolUniverse

**WWOX question.** Can one live-lookup layer (MCP) answer gene-level WWOX queries?

**Contribution vs existing.** optional isolated tool; see tooluniverse_capability_test_20261026.md (work saved) and tool_survey row 12

**Detected.** release: 'v1.5.9' -> 'v1.5.10'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; Apache-2.0.

**Proof.** https://github.com/mims-harvard/ToolUniverse/releases

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-15 · scout_daily · Discovery:diagnosis:compound-with-several-or-opposed-actions

**WWOX question.** Compound with several or opposed actions: pracinostat (class I potent, class IIa uncertain) Multi-target contributions are ALREADY computed 

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Binding affinities for histamine receptors 1 to 4: Systematic comparison of ligands from the Psychoactive Drug Screening Program Ki database (2026-06-12, published record) https://europepmc.org/article/MED/42391979; [paper/europepmc] Guiding student use of generative AI in undergraduate pharmacology: a narrative review and proposed source-checking process framework. (2026-07-28, published record) https://europepmc.org/article/MED/42583001; [preprint/europepmc] How Intercurrent Event Strategies Shape Estimands: Practical Applications in Clinical Pharmacology (2026-06-15, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1252190; [repository/github] oashu741-source/clinical-trial-data-cleaner (2026-07-25, none stated, default-branch head c5f9ea645063 2026-07-25, release none published) https://github.com/oashu741-source/clinical-trial-data-cleaner; [paper/nature] Missing data imputation for wearable time series (2026-09-20, journal-article) https://doi.org/10.1038/s41598-026-71659-z; [paper/nature] A solution to the mystery of the missing neutrinos (2026-08-27, journal-article) https://doi.org/10.1038/d41586-026-02628-9

**Why asked.** diagnosis row 'Compound with several or opposed actions: pracinostat (class' (case / limit layout) [disease-models/wwox/research/drug_repurposing/diagnosis_it28_20261105/README.md @ blob dabb9bb5a8, main 9aa28b3700a2]: "Compound with several or opposed actions: pracinostat (class I potent, class IIa uncertain) Multi-target contr"

**If confirmed (decision).** Compound with several or opposed actions: pracinostat (class: closing 'Multi-target contributions are ALREADY computed and decomposed; the missing piece is assay-matched potency (47 v 5,113 nM) whose m' Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-15 · scout_daily · Discovery:diagnosis:knowledge-present-but-not-influencing-th

**WWOX question.** Knowledge present but not influencing the result (a) NOT_CONSUMED defect: 762 GtoPdb ligands without a ChEMBL id (747 after the labelled and

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [preprint/europepmc] Model-dependent GD2 upregulation in Ewing sarcoma with the EZH2 inhibitor tazemetostat: Prerequisites for combination with GD2-specific CAR  (2026-07-24, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1284994; [paper/europepmc] EZH2 inhibitor tazemetostat voluntarily withdrawn from market. (2026-07-01, published record) https://europepmc.org/article/MED/42386529; [preprint/europepmc] EZH2 Inhibition in Advanced Epithelioid Sarcoma: Real-World Evidence of Target Validation and Implications for Next-Generation Inhibitor Dev (2026-09-11, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1317321; [repository/github] Ankita2612-hub/EZH2-Breast-Cancer-Integrative-Analysis (2026-11-14, none stated, default-branch head 29aa181bb533 2026-11-14, release none published) https://github.com/Ankita2612-hub/EZH2-Breast-Cancer-Integrative-Analysis; [repository/github] MD-Mushfiqur123/EZH2-in-Breast-Cancer- (2026-11-13, none stated, default-branch head ceec53d21d14 2026-11-13, release none published) https://github.com/MD-Mushfiqur123/EZH2-in-Breast-Cancer-; [repository/github] MD-MUSHFIQUR-RAHIM/ezh2-brca (2026-11-13, none stated) https://github.com/MD-MUSHFIQUR-RAHIM/ezh2-brca

**Why asked.** diagnosis row 'Knowledge present but not influencing the result' (case / limit layout) [disease-models/wwox/research/drug_repurposing/diagnosis_it28_20261105/README.md @ blob dabb9bb5a8, main 9aa28b3700a2]: "Knowledge present but not influencing the result (a) NOT_CONSUMED defect: 762 GtoPdb ligands without a ChEMBL "

**If confirmed (decision).** Knowledge present but not influencing the result: closing '(a) NOT_CONSUMED defect: 762 GtoPdb ligands without a ChEMBL id (747 after the labelled and radioactive exclusion) never joined to' Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-15 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] MALL-Lab/PRECISION_paper (2026-11-13, GPL-3.0) https://github.com/MALL-Lab/PRECISION_paper; [repository/github] tonnidas/biograph-agent (2026-11-13, none stated) https://github.com/tonnidas/biograph-agent; [repository/github] mahmoodphd/DrugRAG (2026-11-12, MIT) https://github.com/mahmoodphd/DrugRAG; [model/huggingface] Krishmahaseth/house-price-prediction-model (2026-11-14, mit) https://huggingface.co/Krishmahaseth/house-price-prediction-model; [model/huggingface] karthick1586/churn_prediction (2026-11-14, none stated) https://huggingface.co/karthick1586/churn_prediction; [model/huggingface] Noor-Khan/employee-attrition-prediction (2026-11-14, mit) https://huggingface.co/Noor-Khan/employee-attrition-prediction

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-16 · scout_daily · Discovery:diagnosis:lever-with-a-pertinent-measure:-rock2,-b

**WWOX question.** Lever with a pertinent measure: ROCK2, belumosudil v SAR-407899 Executed and compared; the residual is pharmacology qualification, not gener

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Discovery of Deuterated 3,4-Dihydro-benzo[e][1,4]diazepine-2,5-dione Derivatives as Potent, Selective and Orally Bioavailable ROCK2 Inhibito (2026-08-01, published record) https://europepmc.org/article/MED/42593922; [paper/europepmc] Discovery of N‑Acylhydrazone Derivatives as ROCK Inhibitors: A Journey from Virtual Screening and Structure-Based De Novo Design to the Iden (2026-01-27, published record) https://europepmc.org/article/MED/42006256; [repository/github] ahn2747/ROCK2_analysis (2026-10-27, none stated, default-branch head e5e3d97935de 2026-10-27, release none published) https://github.com/ahn2747/ROCK2_analysis; [repository/github] zpdlf003-wq/rock2 (2026-10-27, none stated) https://github.com/zpdlf003-wq/rock2; [repository/github] rockesprortsofficial-dot/ROCK2 (2026-10-19, none stated, default-branch head 88f399c9e2af 2026-10-19, release none published) https://github.com/rockesprortsofficial-dot/ROCK2; [dataset/huggingface] jyLee0111/omx_f_object-rock2 (2026-08-20, apache-2.0) https://huggingface.co/datasets/jyLee0111/omx_f_object-rock2; [model/huggingface] wmeddie/smolvla_place_rock2 (2025-12-06, none stated) https://huggingface.co/wmeddie/smolvla_place_rock2; [model/huggingface] clembench-playpen/meta-llama_3.1_KTO_KTO_all_games_ROCK2 (2025-02-28, none stated) https://huggingface.co/clembench-playpen/meta-llama_3.1_KTO_KTO_all_games_ROCK2; [paper/nature] S2O-SARUNet: SAR-to-optical self-attention Res-UNet for grayscale images colorization (2026-11-15, journal-article) https://doi.org/10.1038/s41598-026-73580-x; [paper/nature] NSFA AQE CenterOBB detects oriented SAR ships using frequency domain noise suppression and angle quality estimation (2026-11-09, journal-article) https://doi.org/10.1038/s41598-026-79138-1

**Why asked.** diagnosis row 'Lever with a pertinent measure: ROCK2, belumosudil v SAR-407' (case / limit layout) [disease-models/wwox/research/drug_repurposing/diagnosis_it28_20261105/README.md @ blob dabb9bb5a8, main ee5f6cdaaa14]: "Lever with a pertinent measure: ROCK2, belumosudil v SAR-407899 Executed and compared; the residual is pharmac"

**If confirmed (decision).** Lever with a pertinent measure: ROCK2, belumosudil v SAR-407: closing 'Executed and compared; the residual is pharmacology qualification, not generation: ROCK1 "conflict" has under 1% of the mass and i' Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-16 · scout_daily · Discovery:diagnosis:lever-with-unresolved-role:-isr-modulato

**WWOX question.** Lever with unresolved role: ISR modulators (INV-02) and HDAC5 to SLC2A1 Missing measurement (protein-level ISR sign) and a thin premise (one

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] IsrarSoomro60/IsrarSoomro60 (2026-11-16, none stated) https://github.com/IsrarSoomro60/IsrarSoomro60; [repository/github] pcarlsgaard/isr_hsc_kinetics (2026-11-16, none stated) https://github.com/pcarlsgaard/isr_hsc_kinetics; [repository/github] CatKod/embedded-iot-toolkit (2026-11-16, MIT) https://github.com/CatKod/embedded-iot-toolkit; [model/huggingface] twanghcmut/so101-left-arm-task3-isr (2026-11-09, none stated) https://huggingface.co/twanghcmut/so101-left-arm-task3-isr; [space/huggingface] Malak-Israr/reviewmind (2026-10-03, none stated) https://huggingface.co/spaces/Malak-Israr/reviewmind

**Why asked.** diagnosis row 'Lever with unresolved role: ISR modulators (INV-02) and HDAC' (case / limit layout) [disease-models/wwox/research/drug_repurposing/diagnosis_it28_20261105/README.md @ blob dabb9bb5a8, main ee5f6cdaaa14]: "Lever with unresolved role: ISR modulators (INV-02) and HDAC5 to SLC2A1 Missing measurement (protein-level ISR"

**If confirmed (decision).** Lever with unresolved role: ISR modulators (INV-02) and HDAC: closing 'Missing measurement (protein-level ISR sign) and a thin premise (one muscle knockdown origin); the engine cannot supply either' Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-16 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [space/huggingface] amancharde/sanjeevani-drug-repurposing (2025-12-26, none stated) https://huggingface.co/spaces/amancharde/sanjeevani-drug-repurposing; [model/huggingface] muraria/tnbc-drug-repurposing (2025-12-23, none stated) https://huggingface.co/muraria/tnbc-drug-repurposing; [model/huggingface] DPruddh7556/drug-repurposing-models (2025-11-08, none stated) https://huggingface.co/DPruddh7556/drug-repurposing-models

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-16 · scout_daily · Follow:mims-harvard/ToolUniverse

**WWOX question.** live-lookup layer tried on a capability the adapters lack

**Contribution vs existing.** followed since 2026-11-01 (WATCH ToolUniverse; tooluniverse_capability_test_20261026.md)

**Detected.** default-branch head e3a819ff1f8d -> 0da8fb3fcae2; latest release {"date": "2026-11-05", "tag": "v1.5.9"} -> {"date": "2026-11-14", "tag": "v1.5.10"}

**If confirmed (decision).** reopen condition: a capability the adapters lack becomes available, or terms change Roadmap: R9.

**Cost / licence.** reading the change: minutes; see source.

**Proof.** https://github.com/mims-harvard/ToolUniverse

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-17 · scout_daily · PubMed:wwox_any

**WWOX question.** New WWOX paper or external precedent that could reopen a research question

**Contribution vs existing.** not checked against the registry (never grepped); intake triage decides new vs already read

**Detected.** 43036373 A Window Into WOREE: WWOX, Organoids, and Epilepsy.

**Cost / licence.** abstract screen: minutes; a full read needs its receipt; PubMed metadata; full text per paper.

**Proof.** https://pubmed.ncbi.nlm.nih.gov/?term=43036373

**Outcome.** TO_TRIAGE (abstract = discovery, not a reading)

## 2026-11-17 · scout_daily · PubMed:wwox_dee

**WWOX question.** New WWOX paper or external precedent that could reopen a research question

**Contribution vs existing.** not checked against the registry (never grepped); intake triage decides new vs already read

**Detected.** 43036373 A Window Into WOREE: WWOX, Organoids, and Epilepsy.

**Cost / licence.** abstract screen: minutes; a full read needs its receipt; PubMed metadata; full text per paper.

**Proof.** https://pubmed.ncbi.nlm.nih.gov/?term=43036373

**Outcome.** TO_TRIAGE (abstract = discovery, not a reading)

## 2026-11-17 · scout_daily · Discovery:reopen:functional_it13_p3a_20261031/NP3A2

**WWOX question.** Ethosuximide on the provoked seizure score with a same-day three-genotype design, a drug-by-genotype interaction test and measured exposure;

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Electroclinical and behavioral outcomes of add-on ethosuximide in children with developmental and epileptic encephalopathy with spike-wave a (2026-07-10, published record) https://europepmc.org/article/MED/42485909; [paper/europepmc] Aza-Michael approach for the rapid synthesis of 3,5-dimethylpyrazole derivatives with potential biological significance. (2026-07-15, published record) https://europepmc.org/article/MED/42839581; [paper/europepmc] Treatment responses to antiseizure medication in children with Angelman syndrome. (2026-09-07, published record) https://europepmc.org/article/MED/42771958

**Why asked.** reopen functional_it13_p3a_20261031 table row NP3A2 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/functional_it13_p3a_20261031/reopen_searches_it13_p3a.tsv @ blob 1906f5bd43, main bf7cba6706f8]: "Ethosuximide on the provoked seizure score with a same-day three-genotype design, a drug-by-genotype interacti"

**If confirmed (decision).** reopen condition met? source data released or the experiment reproduced Roadmap: R2.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-17 · scout_daily · Discovery:reopen:functional_it13_p3a_20261031/NP3A3

**WWOX question.** Resting potential and the M-current (Kv7) component in neuron-deleted versus control slices at P13 to P17, with the isolated NMDAR current a

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] MartyBordeaux/NMDAR_Braess (2026-09-17, MIT, default-branch head 33665958e50e 2026-09-17, release none published) https://github.com/MartyBordeaux/NMDAR_Braess; [repository/github] xxh87/uADEV_anti_NMDAR_Encephalitis_Case (2026-08-29, none stated, default-branch head 3516f24a2a93 2026-08-29, release none published) https://github.com/xxh87/uADEV_anti_NMDAR_Encephalitis_Case; [repository/github] penghuike3-hash/r14-r8-nmdar-readout-audit (2026-08-28, none stated) https://github.com/penghuike3-hash/r14-r8-nmdar-readout-audit; [paper/nature] Phase separation in multi-component membrane during cell adhesion (2026-11-03, journal-article) https://doi.org/10.1038/s44431-026-00049-2; [paper/nature] Liquid metal interfaces for component mounting on kirigami stretchable substrates (2026-10-30, journal-article) https://doi.org/10.1038/s41528-026-00662-1

**Why asked.** reopen functional_it13_p3a_20261031 table row NP3A3 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/functional_it13_p3a_20261031/reopen_searches_it13_p3a.tsv @ blob 1906f5bd43, main bf7cba6706f8]: "Resting potential and the M-current (Kv7) component in neuron-deleted versus control slices at P13 to P17, wit"

**If confirmed (decision).** reopen condition met? an electrophysiology report from the neuron-deleted line Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-18 · scout_daily · Discovery:reopen:functional_it13_p3a_20261031/NP3A4

**WWOX question.** E_GABA (gramicidin perforated patch) in Wwox-deficient neurons a chloride-gradient measurement in a WWOX-deficient neuron

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Severe neonatal epilepsy linked to a novel homozygous SLC12A5 Arg508Cys variant with impaired chloride transport. (2026-06-17, published record) https://europepmc.org/article/MED/42309338; [dataset/huggingface] referencesource/motor-fuel-dispenser-measurement-tolerances-nist (2026-11-17, other, revision 25bd6dc1cadc, 3 files) https://huggingface.co/datasets/referencesource/motor-fuel-dispenser-measurement-tolerances-nist; [dataset/huggingface] danylochernov/cloud-vps-measurements (2026-11-17, cc-by-4.0, revision f6e0c4263bb8, 7 files) https://huggingface.co/datasets/danylochernov/cloud-vps-measurements; [model/huggingface] SZLHOLDINGS/measurement-master-v1-candidate (2026-11-16, apache-2.0, revision 0eabed41bae5, 9 files) https://huggingface.co/SZLHOLDINGS/measurement-master-v1-candidate; [paper/nature] Edge-centric functional network organization reveals seizure pathways in human epilepsy (2026-09-15, journal-article) https://doi.org/10.1038/s42005-026-02860-9; [paper/nature] Measurement of parent–child quality time: psychometric properties, measurement invariance, and demographic differences (2026-08-09, journal-article) https://doi.org/10.1038/s41598-026-64429-4

**Why asked.** reopen functional_it13_p3a_20261031 table row NP3A4 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/functional_it13_p3a_20261031/reopen_searches_it13_p3a.tsv @ blob 1906f5bd43, main 8a7f3e460b66]: "E_GABA (gramicidin perforated patch) in Wwox-deficient neurons a chloride-gradient measurement in a WWOX-defic"

**If confirmed (decision).** reopen condition met? a chloride-gradient measurement in a WWOX-deficient neuron Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-18 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] JINGEWU/BioMedArena (2026-04-30, MIT) https://github.com/JINGEWU/BioMedArena; [repository/github] sahithirmaryada/RareDx-Agentic-Diagnostic-Assistant (2026-04-30, none stated) https://github.com/sahithirmaryada/RareDx-Agentic-Diagnostic-Assistant; [repository/github] d-feng/Bio-llm-agent-evals (2026-02-21, none stated) https://github.com/d-feng/Bio-llm-agent-evals; [dataset/huggingface] scalingX/lifesci-biomedical-nlp-swe-envs-nocap (2026-11-16, none stated) https://huggingface.co/datasets/scalingX/lifesci-biomedical-nlp-swe-envs-nocap; [dataset/huggingface] Redpine-AI/redpine-biomedical-qa (2026-11-16, cc-by-4.0) https://huggingface.co/datasets/Redpine-AI/redpine-biomedical-qa; [dataset/huggingface] healthcare-biomedical-ai/Surgical-Critical-Care-Medication-Constraint-Verification-Benchmark (2026-11-16, none stated) https://huggingface.co/datasets/healthcare-biomedical-ai/Surgical-Critical-Care-Medication-Constraint-Verification-Benchmark

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-19 · scout_daily · PubMed:wwox_any

**WWOX question.** New WWOX paper or external precedent that could reopen a research question

**Contribution vs existing.** not checked against the registry (never grepped); intake triage decides new vs already read

**Detected.** 43048821 Multi-omic Insight into the Causal Relationship Between Programmed Cell Death and Cognitiv

**Cost / licence.** abstract screen: minutes; a full read needs its receipt; PubMed metadata; full text per paper.

**Proof.** https://pubmed.ncbi.nlm.nih.gov/?term=43048821

**Outcome.** TO_TRIAGE (abstract = discovery, not a reading)

## 2026-11-19 · scout_daily · Discovery:reopen:functional_it13_p3a_20261031/NP3A1

**WWOX question.** Nucleus-resolved parvalbumin composition in the Wwox-deletion mouse (snRNA matrices of GSE158684 or PV immunostaining in the neuron-targeted

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/nature] snRNA-seq of acral melanoma reveals heterogeneity and identifies novel progression marker and cancer-associated fibroblasts subpopulation (2026-07-17, journal-article) https://doi.org/10.1038/s41698-026-01618-4; [paper/nature] The U1 snRNP protein U1C and Helix H of U1 snRNA are critical for small molecule splicing modulator function (2026-07-16, journal-article) https://doi.org/10.1038/s41467-026-74765-8

**Why asked.** reopen functional_it13_p3a_20261031 table row NP3A1 [PARTIAL (nucleus-level d] [disease-models/wwox/research/drug_repurposing/functional_it13_p3a_20261031/reopen_searches_it13_p3a.tsv @ blob 1906f5bd43, main 7c63688e748e]: "Nucleus-resolved parvalbumin composition in the Wwox-deletion mouse (snRNA matrices of GSE158684 or PV immunos"

**If confirmed (decision).** reopen condition met? any of: (a) the eight snRNA SRA experiments leave hup and at least 3 independent libraries per arm are shown by barcode overlap with at leas Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-19 · scout_daily · Discovery:reopen:glia_maturation_it14_p4_20261101/NP4G1

**WWOX question.** Peer review (with source data) of the same-laboratory preprint on a primary oligodendroglial role of WWOX under challenge (PPR1124524) the p

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [preprint/europepmc] RETRACTED: Pre-ictal signature-guided individualized closed-loop tTIS suppresses seizures onset in pediatric epilepsy (2026-04-03, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1173610; [preprint/europepmc] WITHDRAWN: Development of the correlation between mitophagy-related genes and epilepsy (2024-12-09, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR952107; [paper/europepmc] Accuracy of epilepsy screening tools in community and primary care settings across countries in Sub-Saharan Africa: systematic review and me (2026-05-07, published record) https://europepmc.org/article/MED/42097643; [dataset/huggingface] elifepathways/sciencebeam-dataset-scielo-preprints (2026-11-16, cc-by-4.0, revision 0d627c13d522, 55 files) https://huggingface.co/datasets/elifepathways/sciencebeam-dataset-scielo-preprints; [dataset/huggingface] SZLHOLDINGS/ouroboros-arxiv-preprint (2026-11-02, apache-2.0, revision 34a2d9381066, 9 files) https://huggingface.co/datasets/SZLHOLDINGS/ouroboros-arxiv-preprint; [dataset/huggingface] jasonfan/preprint-improve-202610 (2026-10-29, none stated, revision 3cce7f2c46bb, 1784 files) https://huggingface.co/datasets/jasonfan/preprint-improve-202610

**Why asked.** reopen glia_maturation_it14_p4_20261101 table row NP4G1 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/glia_maturation_it14_p4_20261101/reopen_searches_it14_p4.tsv @ blob 53be97d5b9, main 7c63688e748e]: "Peer review (with source data) of the same-laboratory preprint on a primary oligodendroglial role of WWOX unde"

**If confirmed (decision).** reopen condition met? the preprint is published with source data and the disagreement is resolved Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-19 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] inoue0426/OncoGraph (2026-11-18, MIT) https://github.com/inoue0426/OncoGraph; [repository/github] ahsitab/DrugInsight-RAG (2026-11-17, none stated) https://github.com/ahsitab/DrugInsight-RAG; [repository/github] K-Dense-AI/drug-discovery-agent-skills (2026-11-16, MIT) https://github.com/K-Dense-AI/drug-discovery-agent-skills; [dataset/huggingface] SalahALHaismawi/Arabic-OCR-benchmark-predictions (2026-11-19, other) https://huggingface.co/datasets/SalahALHaismawi/Arabic-OCR-benchmark-predictions; [space/huggingface] Sangvinor/Rotor-sail-prediction (2026-11-19, none stated) https://huggingface.co/spaces/Sangvinor/Rotor-sail-prediction; [space/huggingface] Aidanam/credit-risk-prediction (2026-11-19, none stated) https://huggingface.co/spaces/Aidanam/credit-risk-prediction

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-20 · scout_daily · Discovery:reopen:glia_maturation_it14_p4_20261101/NP4G2

**WWOX question.** Independent reproduction of the OPC differentiation delay (DRG-OPC co-culture or null-OPC monoculture) a report from an independent laborato

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/nature] Declining environmental predictability erodes reproduction in a tropical seabird (2026-11-13, journal-article) [bridge to the question: reproduction] https://doi.org/10.1038/s41558-026-02795-7; [paper/nature] A two-stage cascade framework for traffic sign detection: reproduction and boundary analysis (2026-11-10, journal-article) [bridge to the question: reproduction] https://doi.org/10.1038/s41598-026-80390-8

**Why asked.** reopen glia_maturation_it14_p4_20261101 table row NP4G2 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/glia_maturation_it14_p4_20261101/reopen_searches_it14_p4.tsv @ blob 53be97d5b9, main 98235a07dfd6]: "Independent reproduction of the OPC differentiation delay (DRG-OPC co-culture or null-OPC monoculture) a repor"

**If confirmed (decision).** reopen condition met? a report from an independent laboratory Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-20 · scout_daily · Discovery:reopen:glia_maturation_it14_p4_20261101/NP4G3

**WWOX question.** Oligodendrocyte-lineage census in the Synapsin-Cre deletion before the first spontaneous seizure (about P7 to P8) the census is reported

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Ethnic Representation, Deprivation and Seizure Outcomes in a UK Tertiary Epilepsy Clinic. (2026-01-23, published record) [bridge to the question: seizure] https://europepmc.org/article/MED/41619632; [paper/europepmc] Modelling seizure-related predictors of epilepsy diagnostic gap in two urban informal settlements of Nairobi using machine learning. (2025-12-29, published record) [bridge to the question: seizure] https://europepmc.org/article/MED/41584324; [dataset/huggingface] Nexdata-kr/396-Hours-Korean-Spontaneous-Speech-Data (2026-11-19, none stated, revision 25a8a65bc0a8, 20 files) [bridge to the question: spontaneous] https://huggingface.co/datasets/Nexdata-kr/396-Hours-Korean-Spontaneous-Speech-Data; [dataset/huggingface] Nexdata-kr/215-Hours-Korean-Financial-Domain-Entity-Annotated-Spontaneous-Speech-Data (2026-11-19, none stated, revision 6e191b109052, 10 files) [bridge to the question: spontaneous] https://huggingface.co/datasets/Nexdata-kr/215-Hours-Korean-Financial-Domain-Entity-Annotated-Spontaneous-Speech-Data; [dataset/huggingface] MediaCatch/mc_da_spontaneous (2026-11-06, none stated, revision cb47fb23c048, 58 files) [bridge to the question: spontaneous] https://huggingface.co/datasets/MediaCatch/mc_da_spontaneous

**Why asked.** reopen glia_maturation_it14_p4_20261101 table row NP4G3 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/glia_maturation_it14_p4_20261101/reopen_searches_it14_p4.tsv @ blob 53be97d5b9, main 98235a07dfd6]: "Oligodendrocyte-lineage census in the Synapsin-Cre deletion before the first spontaneous seizure (about P7 to "

**If confirmed (decision).** reopen condition met? the census is reported Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-20 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] Hkweb3/drug-graveyard (2026-11-20, none stated) https://github.com/Hkweb3/drug-graveyard; [repository/github] CarterPry/RareDiseaseArb (2026-11-19, none stated) https://github.com/CarterPry/RareDiseaseArb; [repository/github] tttongwang/tttongwang.github.io (2026-11-18, none stated) https://github.com/tttongwang/tttongwang.github.io; [space/huggingface] DPruddh7556/drug-repurposing-ai (2025-11-07, none stated) https://huggingface.co/spaces/DPruddh7556/drug-repurposing-ai

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-20 · HE judgement of the 05:20Z briefing (the first after the lexical bridge, e0d935bb5)

**What the bridge did on this run.** It dropped 32 hits that shared no whole word with the OPC question (opcua, Opciones, DRG payment design: the 14 Nov homonyms) and counted 48 more as adjacent. Seven items were still shown under NP4G2 and NP4G3. None is a lead.

**Signals, one reason each.**
- NP4G2 (independent reproduction of the OPC delay), two Nature-portfolio items: DISCARD. A tropical-seabird paper and a traffic-sign paper, bridged only by the word "reproduction", which names the kind of evidence the row waits for, not its biology. Fix landed with this entry: question-form words (reproduction, report, census, independent) leave the bridge terms; two tests.
- NP4G3 (OPC census before the first seizure), two Europe PMC items and a Korean speech dataset: DISCARD. Shared word "seizure" only; both are epidemiology of clinic populations. The weak spot that remains is a single generic biology word; a rule of two shared words would drop the designed counterexample (Oligodendrocyte maturation defects in Wwox-null mice), so it is not applied.
- Open slot, Hkweb3/drug-graveyard (created 2026-11-20, no licence, 0 stars): DEFER, no adoption. Shelved Phase 2/3 drugs matched to rare-disease genetics; its own README says the automated direction labels failed validation and direction must be settled by reading. That is the same lesson as our class-level direction problem (the sign of a drug's action against the target), found independently; it is a precedent for the method, not a source for WWOX. Its top lead (rapastinel, a NMDAR positive modulator, for GRIN loss-of-function) points the opposite way to our NMDAR-hyperfunction question and is not a candidate for it.
- Open slot, CarterPry/RareDiseaseArb (already a followed team): DEFER to the ADV sponsor question, which is reserved to the operator. It maps the pediatric priority review voucher statute and one 2025 court ruling on pre-1962 "deemed approved" applications; it says nothing about the science. Nothing was checked against the statute here.
- Open slot, tttongwang.github.io and DPruddh7556/drug-repurposing-ai: DISCARD (a personal site; a generic repurposing space with no stated method).
- europepmc "HTTP 0" on NP4G2: one transient probe error; the next run is the test, nothing changed.

**Beyond the lexical bridge.** Nothing more is justified now: one briefing is one measurement, the false hits fell from the 14 Nov kind (homonyms) to the kind a one-word bridge still allows, and the only remedy that would remove them (two shared words) costs a real hit. Re-measure on the next briefing before touching the bridge again.

**Outcome.** TRIAGED (0 leads, 0 adoptions; one dated line forwarded to ADV in the meeting reply).

## 2026-11-20 — IT successor M, session close (ADV-106 to ADV-118 stretch)

**Session learning delta.** Two prospective generator tests (RP-005) ended inconclusive (arms differed on 4 of 28 pooled slots; no advantage of the repository materials over the abstract shown); a reserve was rebuilt from today's results and consumed as dated open-question lines; the eIF2B epsilon reagent search turned "no phosphomimetic found" into "one exists (S540E, preprint, abstract level)".

**Capability gap (new).** To state that a reagent, mutant or compound is absent from the literature we lack a spelling-expansion step: a mutation or residue written in one notation (S540D) missed the paper that used another (S540E; also Ser540Glu, p.Ser540Glu, mouse 536, rat 535). The 2026-11-12 "none found" and my own first string sets both missed it; the correction came from a broader concept query (serine numbers with mutant, mutation or phosphomimetic). Evidence: advisor_pilot_20261113/brainstorm_20261116/adv114_eif2b_reagent_it_20261120/EIF2B_REAGENT_SEARCH_ADV114_IT_20261120.md section 1.

**Candidate (not built).** A small helper that expands a residue or substitution into its notations and numbering variants and prints the query strings to put in the record; or a line in the search-record rule: an absence names its strings and at least one concept-level query. Cost: hours. Not implemented here because the current task was the search, not the tool; the lesson is in memory (it-successor-m-20261120-pitfalls) and in the ADV DREAM line for RP-018. Marked for the next harness task if a second case appears.

**Environment.** Host-specific tool verdicts not used this session (no SKIP or REJECT on tool absence).

**Outcome.** Gap recorded (new); change made: none; no cost, API or privacy risk (plain clients, generic client name, no contact parameter). Strategic Advisor: assess this lead against the standing roadmap and current work; apply cross-session transport section 12 (Route useful signals) and contact the relevant Harness or Science owner when worthwhile.

## 2026-11-20 — IT successor N, session close (WM103 part 1 stretch)

**Session learning delta.** The second blind check of a repaired sentence found one overshoot («partly corrects P20 glucose» where the P20 panel has no untreated knockout group); the sentence was rewritten in the verifier's own wording and part 1 of the WM103 candidate landed as three dated notes; the knockout glucose baseline in the source figure exists at P10 only.

**Capability gap.** None new. One near-miss, already covered: three sessions are listed under the name SCI, and the delivery note for the message sent to the one the checkpoint named did not say which inbox received it. The remedy that exists (address by `name [ref]` from the checkpoint, and read «who a message really reached», cross-session transport section 5) was applied; the residual question (did that session read it) stays open and is not counted as a defect.

**Environment.** Host-specific tool verdicts not used this session (no SKIP or REJECT on tool absence).

**Outcome.** `CHANGE = NONE`; no cost, API or privacy risk. Strategic Advisor: assess this note against the standing roadmap and current work; apply cross-session transport section 12 (Route useful signals) and contact the relevant Harness or Science owner when worthwhile.

## 2026-11-21 — SCI window U, session close (ADV-133 strand 1, RP-037, RP-038)

**Session learning delta.** Three strands closed with sentences (a named missing measure; a conditional class that survives a pre-registered comparison as not ranked; a conditional handle class with a developmental-timing conflict). A blind verifier overturned one producer absence claim, and two source papers print an F value that does not match the printed p value.

**Capability gap.** One reusable gap: persisting a delegate report verbatim from the session transcript (search the project transcript for the report's first line, strip the harness indent, add the model and effort header read back by `session_model_census.py`) was rewritten four times in one window; a small shipped helper would remove the repeat. Proposed to Harness Engineering; not built here (a new script carries routing, shebang and `--help` obligations that belong to its owner). A second near-miss is already covered: the publication gate refused a verbatim report that pairs a person word with an animal dose unit within 700 characters; the remedy (run `public_release_gate.py` before the first push) is recorded in memory and in the checkpoint.

**Environment.** Host-specific tool verdicts not used this session (no SKIP or REJECT on tool absence).

**Outcome.** `CHANGE = NONE` shipped; one proposal to Harness Engineering. No cost, API or privacy risk.

## 2026-11-21 · scout_daily · Discovery:work_order:NEED-NEUROINFLAMMATION-GLIA

**WWOX question.** Is glial density in a Wwox-deficient brain below, equal to or above wild type before the first spike? The sign conflicts between species, so

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Multi-glial inhibitory plasticity in epilepsy and sleep: implications for post-traumatic epileptogenesis. (2026-08-19, published record) [bridge to the question: glial] https://europepmc.org/article/MED/42617910; [paper/europepmc] Dual Notch-1 pathway regulation mitigates glial activation and preserves myelin integrity: neuroprotective and anticonvulsant actions of pen (2026-10-01, published record) [bridge to the question: glial] https://europepmc.org/article/MED/42820746; [paper/europepmc] The Neuroprotective Role of a Caspase-1 Inhibitor Against Apoptosis via Inhibition of Glial Hyperactivation in a Mouse Model of Epilepsy. (2026-05-01, published record) [bridge to the question: glial] https://europepmc.org/article/MED/42216646; [paper/nature] An AAV vector for glial cells (2026-07-08, journal-article) [bridge to the question: glial] https://doi.org/10.1038/s41587-026-03193-2; [paper/nature] Evaluation of autophagy in neonatal rat glial cells in an in vitro model of hypoxic–ischemic injury (2026-07-04, journal-article) [bridge to the question: glial] https://doi.org/10.1038/s41598-026-60076-x

**Why asked.** work_order entry NEED-NEUROINFLAMMATION-GLIA [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 07b3e76fb4a6]: "Is glial density in a Wwox-deficient brain below, equal to or above wild type before the first spike? The sign"

**If confirmed (decision).** It decides whether this need is a readout, a seizure consequence or a seizure-independent lever. Until then no glial modulator is proposed, and no position move Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-21 · scout_daily · Discovery:work_order:NEED-WWOX-GENE-ADDITION

**WWOX question.** Does an intermediate vector level separate a threshold from a gradient, and is the benefit only prevented inside the first days of life or a

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] The delayed-onset of inertial cavitation in tissue-mimicking agar phantom. (2026-04-10, published record) [bridge to the question: onset] https://europepmc.org/article/MED/41916333; [paper/europepmc] A Multimodal Biomedical Sensing Approach for Muscle Activation Onset Detection. (2026-03-18, published record) [bridge to the question: onset] https://europepmc.org/article/MED/41902075; [paper/europepmc] Predicting health and disease: a conceptual framework for AI in preventive and precision medicine. (2026-07-02, published record) [bridge to the question: prevented] https://europepmc.org/article/MED/42392670

**Why asked.** work_order entry NEED-WWOX-GENE-ADDITION [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 07b3e76fb4a6]: "Does an intermediate vector level separate a threshold from a gradient, and is the benefit only prevented insi"

**If confirmed (decision).** Quantified myelination would add a controlled row on the same need; a failure would move the card to C2 by rule; a treated-after-onset arm would show whether th Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-21 · scout_daily · Team:mims-harvard

**WWOX question.** Does an intermediate vector level separate a threshold from a gradient, and is the benefit only prevented inside the first days of life or a

**Contribution vs existing.** one-level exploration of mims-harvard's public listing (30 scanned, 28 without a shared term); not recursive

**Detected.** followed team (repo mims-harvard/ToolUniverse); other public work matching ['structure']: [github] mims-harvard/SPECTRA (2026-05-28, MIT, matched ['structure']) https://github.com/mims-harvard/SPECTRA

**Why asked.** work_order entry NEED-WWOX-GENE-ADDITION [disease-models/wwox/research/drug_repurposing/view/work_order.json @ blob 153e14f097, main 07b3e76fb4a6]: "Does an intermediate vector level separate a threshold from a gradient, and is the benefit only prevented insi"

**If confirmed (decision).** Quantified myelination would add a controlled row on the same need; a failure would move the card to C2 by rule; a treated-after-onset arm would show whether th Roadmap: R9.

**Minimal test.** read the repository's README and latest default-branch commit; record the SHA and release apart

**Cost / licence.** reading the listing entries: minutes; per item, shown where stated.

**Proof.** public github listing of mims-harvard, no key

**Outcome.** TO_TRIAGE (a listing match is a lead, not a reading)

## 2026-11-21 — HE successor F, triage of the three pending radar entries above

- NEED-NEUROINFLAMMATION-GLIA (3 hits, glial bridge): TRIAGED, no lead. The three titles (glial inhibitory plasticity in epilepsy and sleep, Notch-1 regulation of glial activation in a seizure model, a caspase-1 inhibitor) are matched by the word "glial" only; none measures glial density in a Wwox-deficient brain, which is the question of the need. Not read at full text; a title is not a reading.
- NEED-WWOX-GENE-ADDITION (3 hits, "onset" and "prevent" bridges): TRIAGED, no lead. The hits are an ultrasound cavitation phantom, a muscle-activation sensor and a general AI-in-medicine framework: one-word lexical bridges that the briefing already names as its remaining false-hit kind (see the entry above on the lexical bridge). Nothing about vector level or treatment timing.
- Team mims-harvard (SPECTRA, MIT, matched on "structure"): TRIAGED, no lead. A protein-structure repository; no stated link to a WWOX question, no adoption.

**Outcome.** TRIAGED (0 leads, 0 adoptions). The remedy for one-word bridges stays as recorded above; this is one more measurement of the same false-hit kind, not a new problem.

## 2026-11-21 — IT successor Q, session close

- **Gap (new, small).** To fold a design team's answers into a governing text by script we lack a scripted check for tension between an inserted answer and the sentence it sits next to. The numeric checker (`current_text_adv143_it_20261121/check_current_text.py`: new tokens, History verbatim, dropped tokens) caught none of the conflicts the round-3 reader found (pilot ages, series age, E2 against the floor rule, "stage" against "grade"); a same-family reader found them, a new layer each round.
- **Evidence.** `verify_adv146/COMPARISON_ADV146_IT_20261121.md` (criteria 1 and 2 not met; six CONFLICT-OPEN and one OPEN-GAP added by repair).
- **Outcome.** GAP-NEW, no change made: a proportionate candidate is a term-collision scan (the same defined term or number used in an answer and in a neighbouring rule sentence with different values), proposed for the next text-work task, not built now. No external search was run (the gap is internal); no cost or privacy risk.
- **Next micro-step.** If ADV-148 returns answers to integrate, run the integration script, then a collision scan on the touched sentences before any reader is dispatched.
- Strategic Advisor: assess against the standing roadmap and the ADV-148 queue; route to Harness if worthwhile.

## 2026-11-22 · scout_daily · Discovery:task_step:OBJ_ACCEPTED/Integrate

**WWOX question.** Integrate SCI X results when each lands: ADV-139 (INV-15 question wording and resume condition in investigations_it20.tsv via the establishe

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Ultrasound-responsive nanotherapy promotes axonal regeneration after SCI via reactivating CREB/miR-129-5p signaling. (2026-09-22, published record) [bridge to the question: regeneration] https://europepmc.org/article/MED/42828130; [paper/europepmc] Corrigendum to "Investigation of the effects of umbilical cord and adipose-derived mesenchymal stem cells on endoplasmic reticulum stress in (2025-12-16, published record) [bridge to the question: investigations] https://europepmc.org/article/MED/41412325; [paper/nature] Predicting energy consumption in directed energy deposition using incremental learning-integrated transfer learning (2026-02-25, journal-article) [bridge to the question: integrate] https://doi.org/10.1038/s44334-025-00065-6

**Why asked.** task_step ORCH-ROADMAP-IT59-20261119 OBJ_ACCEPTED step Integrate [TODO] [ledger/tasks/orchestrator/ORCH-ROADMAP-IT59-20261119.json @ blob cc2c1e9ca7, main 42e209737714]: "Integrate SCI X results when each lands: ADV-139 (INV-15 question wording and resume condition in investigatio"

**If confirmed (decision).** step Integrate (orchestrator): whether a found method/resource changes how it is done Roadmap: R3.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-22 · scout_daily · Discovery:reopen:glia_maturation_it14_p4_20261101/NP4G1

**WWOX question.** Peer review (with source data) of the same-laboratory preprint on a primary oligodendroglial role of WWOX under challenge (PPR1124524) the p

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Mild malformation of cortical development with oligodendroglial hyperplasia in epilepsy (MOGHE)-like spectrum with a unique NRAS c.182A>G (p (2026-09-30, published record) [bridge to the question: oligodendroglial] https://europepmc.org/article/MED/42996408; [paper/europepmc] Altered oligodendroglial cell development and increased myelination in SCN2A gain-of-function-linked epilepsy. (2026-10-07, published record) [bridge to the question: oligodendroglial] https://europepmc.org/article/MED/42855710; [paper/europepmc] Molecular Heterogeneity of WNT and mTOR Signaling Pathways in Mild Malformation of Cortical Development with Oligodendroglial Hyperplasia an (2026-11-17, published record) [bridge to the question: oligodendroglial] https://europepmc.org/article/MED/43043571; [paper/nature] Embryonic exposure to 3,3’,5-triiodo-L-thyronine affects oligodendroglial lineage during neurodevelopment in zebrafish (2026-07-22, journal-article) [bridge to the question: oligodendroglial] https://doi.org/10.1038/s41598-026-63428-9

**Why asked.** reopen glia_maturation_it14_p4_20261101 table row NP4G1 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/glia_maturation_it14_p4_20261101/reopen_searches_it14_p4.tsv @ blob 53be97d5b9, main 42e209737714]: "Peer review (with source data) of the same-laboratory preprint on a primary oligodendroglial role of WWOX unde"

**If confirmed (decision).** reopen condition met? the preprint is published with source data and the disagreement is resolved Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-22 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [dataset/huggingface] healthcare-biomedical-ai/Ambulatory-Surgery-Medication-and-Allergy-Constraint-Verification-Benchmark (2026-11-20, none stated, revision 969ff8cc3477, 3 files) https://huggingface.co/datasets/healthcare-biomedical-ai/Ambulatory-Surgery-Medication-and-Allergy-Constraint-Verification-Benchmark; [dataset/huggingface] healthcare-biomedical-ai/Behavioral-Medicine-Counseling-Dialogue-Intent-Classification-Dataset (2026-11-20, none stated, revision 24a949225660, 3 files) https://huggingface.co/datasets/healthcare-biomedical-ai/Behavioral-Medicine-Counseling-Dialogue-Intent-Classification-Dataset; [space/huggingface] Biomedical/Degradation_Predict_Copy (2026-11-20, none stated, revision dc94ffa9855f, 4 files) https://huggingface.co/spaces/Biomedical/Degradation_Predict_Copy

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-23 · scout_daily · Discovery:reopen:glia_maturation_it14_p4_20261101/NP4G3

**WWOX question.** Oligodendrocyte-lineage census in the Synapsin-Cre deletion before the first spontaneous seizure (about P7 to P8) the census is reported

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Case Report: Myelin oligodendrocyte glycoprotein antibody-associated cortical encephalitis masked by peri-ictal magnetic resonance imaging a (2026-08-21, published record) [bridge to the question: oligodendrocyte] https://europepmc.org/article/MED/42698690; [paper/europepmc] Integrative genomic and spatial transcriptomic analysis elucidates the oligodendrocyte-mediated etiology of epileptic cortical thinning. (2026-03-26, published record) [bridge to the question: oligodendrocyte] https://europepmc.org/article/MED/41885647; [paper/europepmc] Autoimmune-associated epilepsy or acute symptomatic seizures? A case series of recurrent seizures in patients with myelin oligodendrocyte gl (2026-01-28, published record) [bridge to the question: oligodendrocyte, seizure] https://europepmc.org/article/MED/41616748; [repository/github] Difei1993/TLE-Mature-Oligodendrocyte-P5 (2026-10-13, MIT, default-branch head 946fcfbf8fbc 2026-10-13, release v1.0.0 2026-10-09) [bridge to the question: oligodendrocyte] https://github.com/Difei1993/TLE-Mature-Oligodendrocyte-P5; [paper/nature] Single-cell transcriptomic insights into conserved and divergent oligodendrocyte lineage programs across species (2026-10-25, journal-article) [bridge to the question: oligodendrocyte, lineage] https://doi.org/10.1038/s42003-026-11256-y; [paper/nature] Effects of thioredoxin-1 on oligodendrocyte lineage cells altered by the 1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine (2026-09-24, journal-article) [bridge to the question: oligodendrocyte, lineage] https://doi.org/10.1038/s41531-026-01581-8

**Why asked.** reopen glia_maturation_it14_p4_20261101 table row NP4G3 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/glia_maturation_it14_p4_20261101/reopen_searches_it14_p4.tsv @ blob 53be97d5b9, main 859262b99837]: "Oligodendrocyte-lineage census in the Synapsin-Cre deletion before the first spontaneous seizure (about P7 to "

**If confirmed (decision).** reopen condition met? the census is reported Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-23 · scout_daily · Discovery:reopen:glia_maturation_it14_p4_20261101/NP4G4

**WWOX question.** Human isogenic patient-allele neuron-OPC system with an oligodendrocyte compartment such a system is reported

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/europepmc] Chromatin remodeling factor BAF155 coordinates oligodendroglial-neuronal communications linked to regional myelination and autism-like behav (2025-12-21, published record) [bridge to the question: oligodendrocyte] https://europepmc.org/article/MED/41423560; [preprint/europepmc] A developmental switch to facilitation shapes synaptic plasticity at neuron-OPC synapses in white matter (2026-04-03, preprint (not peer reviewed)) [bridge to the question: neuron] https://europepmc.org/article/PPR/PPR1214614; [paper/europepmc] Spared Nerve Injury Induces Long-Term and Brain Region-Specific Changes in Oligodendrocyte Density in Mice. (2026-04-01, published record) [bridge to the question: oligodendrocyte] https://europepmc.org/article/MED/41964505

**Why asked.** reopen glia_maturation_it14_p4_20261101 table row NP4G4 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/glia_maturation_it14_p4_20261101/reopen_searches_it14_p4.tsv @ blob 53be97d5b9, main 859262b99837]: "Human isogenic patient-allele neuron-OPC system with an oligodendrocyte compartment such a system is reported"

**If confirmed (decision).** reopen condition met? such a system is reported Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-23 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] kongkong-bit/ER-DReKG (2026-11-20, none stated, default-branch head 1ca01d28b522 2026-11-20, release none published) https://github.com/kongkong-bit/ER-DReKG; [repository/github] jdjzq/CPM-DDI-KG (2026-11-16, NOASSERTION, default-branch head 979891d15e27 2026-11-16, release none published) https://github.com/jdjzq/CPM-DDI-KG; [repository/github] zhuhengwei00/target-aware-drug-repurposing (2026-11-15, none stated) https://github.com/zhuhengwei00/target-aware-drug-repurposing; [model/huggingface] telepaties/laptop-price-prediction-model (2026-11-23, none stated) https://huggingface.co/telepaties/laptop-price-prediction-model; [model/huggingface] At1uri/conformal-prediction-vault (2026-11-23, mit) https://huggingface.co/At1uri/conformal-prediction-vault; [dataset/huggingface] At1uri/conformal-prediction-coverage-benchmarks (2026-11-23, mit) https://huggingface.co/datasets/At1uri/conformal-prediction-coverage-benchmarks

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-23 · scout_daily · Follow:mims-harvard/ToolUniverse

**WWOX question.** live-lookup layer tried on a capability the adapters lack

**Contribution vs existing.** followed since 2026-11-01 (WATCH ToolUniverse; tooluniverse_capability_test_20261026.md)

**Detected.** default-branch head 0da8fb3fcae2 -> df5ee941a89c; latest release {"date": "2026-11-14", "tag": "v1.5.10"} -> {"date": "2026-11-14", "tag": "v1.5.10"}

**If confirmed (decision).** reopen condition: a capability the adapters lack becomes available, or terms change Roadmap: R9.

**Cost / licence.** reading the change: minutes; see source.

**Proof.** https://github.com/mims-harvard/ToolUniverse

**Outcome.** TO_TRIAGE (a detected change is not a reading)

## 2026-11-24 · scout_daily · Discovery:reopen:modifiers_it12_p1b_20261031/NP1B1

**WWOX question.** Second WWOX-null clone or WWOX re-expression arm of the HAP1 genetic-interaction screen (N-P1B-1) the data holders report a second clone or 

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [paper/nature] Neuron-specific expression of transmembrane protein 130 (TMEM130) (2026-06-20, journal-article) [bridge to the question: expression] https://doi.org/10.1038/s41598-026-59183-6; [paper/nature] Nonlinear dynamics of seizure suppression via optogenetic modulation of neuron-astrocyte interaction (2026-03-18, journal-article) [bridge to the question: interaction] https://doi.org/10.1038/s41598-026-42663-0

**Why asked.** reopen modifiers_it12_p1b_20261031 table row NP1B1 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/modifiers_it12_p1b_20261031/reopen_searches_it12_p1b.tsv @ blob 98d03e4c5d, main e9a3b7e643f9]: "Second WWOX-null clone or WWOX re-expression arm of the HAP1 genetic-interaction screen (N-P1B-1) the data hol"

**If confirmed (decision).** reopen condition met? the data holders report a second clone or a re-expression screen, or a new deposit appears Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TRIAGED 2026-11-24 (plan): no reopen. Reopen condition (a second WWOX-null clone, a re-expression screen, or a new deposit) not met; the two hits are a TMEM130 expression paper and an optogenetic seizure-dynamics model, matched on the words 'expression' and 'interaction' only.

## 2026-11-24 · scout_daily · Discovery:reopen:modifiers_it12_p1b_20261031/NP1B2

**WWOX question.** Genetic-interaction readout in WWOX-null versus corrected human neural cells (N-P1B-2) a neural isogenic line becomes available or a deposit

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [preprint/europepmc] Excitatory Dysfunction and Phenotypic Rescue in a Human Neuronal Model of  SCN2A  -Related Disorders (2026-05-19, preprint (not peer reviewed)) [bridge to the question: human] https://europepmc.org/article/PPR/PPR1233826; [paper/europepmc] Isogenic modeling of 1q21.1 reciprocal CNVs in human ES cells reveals divergent neurodevelopmental trajectories. (2026-02-01, published record) [bridge to the question: human, cells] https://europepmc.org/article/MED/41370233; [paper/europepmc] Human induced pluripotent stem cell-derived cortical neurons from monozygotic twins with the Gαo1 K278del mutation reveal disease mechanisms (2026-11-05, published record) [bridge to the question: human] https://europepmc.org/article/MED/42984270; [dataset/huggingface] noryxxxx/44-set-available (2026-11-18, none stated, revision 48948ae94d6e, 2435 files) [bridge to the question: available] https://huggingface.co/datasets/noryxxxx/44-set-available; [dataset/huggingface] dfgjhdfhjgjdf/35-set-available (2026-11-18, none stated, revision da417be8894e, 2434 files) [bridge to the question: available] https://huggingface.co/datasets/dfgjhdfhjgjdf/35-set-available; [model/huggingface] availablename2/stockrulekeeper-qwen3-8b-fixed6 (2026-11-10, none stated, revision 619fd0c42b49, 3 files) [bridge to the question: available] https://huggingface.co/availablename2/stockrulekeeper-qwen3-8b-fixed6

**Why asked.** reopen modifiers_it12_p1b_20261031 table row NP1B2 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/modifiers_it12_p1b_20261031/reopen_searches_it12_p1b.tsv @ blob 98d03e4c5d, main e9a3b7e643f9]: "Genetic-interaction readout in WWOX-null versus corrected human neural cells (N-P1B-2) a neural isogenic line "

**If confirmed (decision).** reopen condition met? a neural isogenic line becomes available or a deposit of such a screen appears Roadmap: R1/R8.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TRIAGED 2026-11-24 (plan): no reopen. Reopen condition (a WWOX neural isogenic line or a deposit) not met; the hits are isogenic or patient-cell models of other genes (SCN2A, 1q21.1, GNAO1) and an unrelated dataset, matched on 'human' and 'cells'.

## 2026-11-24 · scout_daily · Discovery:open-slot

**WWOX question.** unplanned find: no gap assumed

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [repository/github] URK23CS7048Rohan/Old-Drug-New-Diseases (2026-10-27, NOASSERTION) https://github.com/URK23CS7048Rohan/Old-Drug-New-Diseases; [repository/github] kushagra0526/atlas-discovery-kg-repurposing-prototype (2026-10-26, none stated) https://github.com/kushagra0526/atlas-discovery-kg-repurposing-prototype; [repository/github] nalgirkarh-prog/RareDiseasePipeline (2026-10-25, MIT) https://github.com/nalgirkarh-prog/RareDiseasePipeline

**Why asked.** open slot: no priority assumed

**If confirmed (decision).** whether it reveals a question we did not know to ask Roadmap: R9.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)

## 2026-11-25 · scout_daily · ToolUniverse

**WWOX question.** Can one live-lookup layer (MCP) answer gene-level WWOX queries?

**Contribution vs existing.** optional isolated tool; see tooluniverse_capability_test_20261026.md (work saved) and tool_survey row 12

**Detected.** release: 'v1.5.10' -> 'v1.5.11'

**Cost / licence.** reading the change: minutes; any adoption: unestimated until triaged; Apache-2.0.

**Proof.** https://github.com/mims-harvard/ToolUniverse/releases

**Outcome.** TRIAGED 2026-11-25 (plan, release notes read): no reopen. v1.5.11 repairs return schemas and loaders and adds Health Canada drug-product, PubMLST and pharmacogenomic tools; no capability the adapters lack was named by an open question, licence unchanged.

## 2026-11-25 · scout_daily · Discovery:diagnosis:compound-with-several-or-opposed-actions

**WWOX question.** Compound with several or opposed actions: pracinostat (class I potent, class IIa uncertain) Multi-target contributions are ALREADY computed 

**Contribution vs existing.** unchecked: a search hit is the first look (no relevance scoring)

**Detected.** [preprint/europepmc] Identification of shared blood transcriptomic features and candidate sedative targets in chronic insomnia with comorbid anxiety: an in-silic (2026-10-30, preprint (not peer reviewed)) [bridge to the question: target] https://europepmc.org/article/PPR/PPR1353779; [paper/nature] Context-aware tooth instance segmentation and missing-tooth localization in panoramic radiographs (2026-11-16, journal-article) [bridge to the question: missing] https://doi.org/10.1038/s41598-026-78690-0; [paper/nature] Missing marks made visible (2026-08-06, journal-article) [bridge to the question: missing] https://doi.org/10.1038/s41570-026-00861-4

**Why asked.** diagnosis row 'Compound with several or opposed actions: pracinostat (class' (case / limit layout) [disease-models/wwox/research/drug_repurposing/diagnosis_it28_20261105/README.md @ blob dabb9bb5a8, main 9147e69e7e65]: "Compound with several or opposed actions: pracinostat (class I potent, class IIa uncertain) Multi-target contr"

**If confirmed (decision).** Compound with several or opposed actions: pracinostat (class: closing 'Multi-target contributions are ALREADY computed and decomposed; the missing piece is assay-matched potency (47 v 5,113 nM) whose m' Roadmap: R5.

**Minimal test.** read the source; reproduce one stated result on public inputs before any adoption

**Cost / licence.** screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated.

**Proof.** GitHub, Hugging Face, Crossref (Nature portfolio), Europe PMC: public endpoints, no key

**Outcome.** TRIAGED 2026-11-25 (plan, title depth): no reopen; the three hits are an insomnia transcriptomics preprint, a dental image model and a commentary on missing marks, matched on one word.

## 2026-11-25 — HE successor, title-depth triage of the radar backlog

**Population.** The 83 blocks still reading `TO_TRIAGE` above, dated 2026-10-29 to 2026-11-25 (the two of 25 November carry their own outcome). Definition of yield, frozen first: `drug_repurposing/checkpoint_he_20261120/HE_RADAR_YIELD_PREREG_20261125.md`. Figures and candidates: `HE_RADAR_YIELD_20261125.md` in the same folder.

**Outcome.** TRIAGED 2026-11-25 (plan), title depth, covering those blocks: 0 yield at triage time by definition; 0 adoptions; the candidates listed in the result file are discovery hits, not readings. The earlier `TO_TRIAGE` lines stay as written (the log is append-only).

## 2026-11-25 — SCI (ADV-279): held files whose bytes are not what their name says

**Gap (with evidence).** To count a study as readable from held bytes we lack a content check at that step: study 30362252 was selected for its two "figures", which are HTML "HTTP 404" pages saved under image names; a magic-bytes pass over 6,100 held files (host of this session; ImageMagick, pdftoppm and PyMuPDF present, ffmpeg absent) found 39 mismatches, 27 of them HTML or empty (`brainstorm_20261116/adv279_next_ten_held_partials_sci_20261125/PREREG_ADV279_AMENDMENT1_SCI_20261125.md`). Search of this log on 2026-11-25 for "magic", "error page" and "content check": no earlier record.

**Outcome.** Gap recorded (new). No change made by Science and no external search; routed to Harness Engineering through ADV (acquisition step and held-file count). Interim: ADV-280 excludes error-page and empty files first. No cost, API or privacy risk. Strategic Advisor: assess these leads against the standing roadmap and current work; apply cross-session transport section 12 (Route useful signals) and contact the relevant Harness or Science owner when worthwhile.

## 2026-11-25 — SCI (ADV-280): the consumer sentence is not carried to the second reader by any tool

**Gap (with evidence).** A facts-only second reading of ten held records agreed with the first reader on every fact and the batch scored strict 0 of 10; a second reader given the verbatim consumer sentences and the sources found the two strict items (a card parenthesis describing a paper's own assays as dye-reduction measures when only one is; a ledger lineage line calling every figure republished when two legends declare it) and a third that the first reader kept loose (`adv280_next_ten_held_partials_sci_20261125/BLIND_SENTENCES_REPORT_ADV280_SCI_20261125.md`). Building the sentence file took one inline script that pulled text out of cards, the ledger and the claim registry by assertion id; no tool does it, and the video files of two records could not be watched (no ffmpeg on this host, as in ADV-279).

**Outcome.** CHANGE = proportional, shipped: four checks added to `PRE_READ_CHECKLIST_ADV276_SCI_20261125.md` (the blind reader gets the repository sentence; a description of the source's own assays repeated from memory; a null needs its activity check; a faint band on a small strip is measured). No external search, no spend. Candidate for Harness Engineering, not done by Science: a small `consumer_sentences.py ID...` that prints the verbatim consumer text of a card assertion, ledger entry or claim by identifier, to build the sentence file in one call (ADV-281 will need it for ten card notes). Strategic Advisor: assess against the standing roadmap and current work.

## 2026-11-25 — HE (ADV-279 follow-up): consumer count misses author-year mentions; held-file gap closed

**Gap (with evidence).** `framework/scripts/consumer_count.py` joins a study to a record by PMID, DOI or `PAPER NNN` only. The working model cites PMID 42137291 as "Thomsen 2026" and the count does not see it, so the count misses uses as well as it invented them before this change. Size over the whole model: not measured. Note: `checkpoint_he_20261120/HE_CONSUMER_JOINS_20261125.md`.

**Outcome.** CHANGE = NONE for the author-year gap (which author-year forms are unambiguous is undecided; no external search). The SCI ADV-279 held-content gap recorded above is closed by `framework/scripts/held_content_check.py`. No cost, API or privacy risk. Strategic Advisor: assess against current work per cross-session transport section 12.

## 2026-11-25 — SCI (ADV-281): null notes need a two-route list and a sentence file built by tool

**Gap (with evidence).** SCI's earlier scan found ten null-wording card notes by one field and keywords; two routes (the structured `direction` field and null phrases over `measured_result_note` and `note`) plus screening by reading give 63 (`adv281_null_note_control_audit_sci_20261125/screen_adv281.tsv`). The blind sentence file needed one inline script over the card JSON, and the first phrase list both over-matched ("no effect size", "null" for a knockout genotype) and under-matched (DR-E03-001 matched by accident). No tool prints the null notes of the cards with their routes, nor the verbatim consumer sentence of an assertion.

**Outcome.** CHANGE = proportional, shipped: three lines in `PRE_READ_CHECKLIST_ADV276_SCI_20261125.md` (name the test that reproduces a printed p; check a "not available" label against the held folders; an in-study check column). No external search, no spend. Candidate for Harness Engineering, not done by Science: `consumer_sentences.py ID...` (as recorded on 2026-11-25 after ADV-280) and a `null_notes.py` that runs both routes over the cards and prints the screening table. Strategic Advisor: assess against the standing roadmap and current work.

## 2026-11-25 - SCI (ADV-282): consumer sentences for list-membership claims

**Gap (with evidence).** In ADV-282 the verified errors were statements about what a deposited list contains ("only NFE2L2", G6PD missed) and about thresholds without units; each could be caught by a script that takes a card sentence, extracts the gene symbols and checks them against the deposited lists named in the same card. The `consumer_sentences.py` and `null_notes.py` candidates for HE recorded under ADV-281 already cover the extraction; the list check is the missing half (`adv282_null_note_control_audit_sci_20261125/`).

**Outcome.** CHANGE = proportional, shipped: two lines in `PRE_READ_CHECKLIST_ADV276_SCI_20261125.md`. No external search, no spend. Candidate for Harness Engineering, not started here.

## 2026-11-25 - SCI (ADV-283): CHANGE = NONE

Gap: none beyond the one recorded under ADV-282; the merged-table column-total check is one line of the analysis script's pattern and is carried by the self-evaluation addendum. No external search, no spend.

### 2026-11-25, SCI, ADV-282 increment 3
Gap: a first reading that grades facts misses wording errors that follow from the sentence's own numbers. CHANGE = NONE in the harness: a column in the first-reading TSV ("sentence arithmetic against its own numbers", filled before any source is opened) is the fix, used from increment 4. A table printer for Table S1-style transposed clinical sheets (one column per individual) would have saved two extraction rounds; candidate for HE, not requested.

### 2026-11-25, SCI, ADV-285
Gap: an assignment premise ("no functional readout is held") was wrong because the repository already held it; CHANGE = NONE in the harness: a grep of the repository for the readout terms, named in the PREREG, before any external search. A route-count script (PubMed esearch plus Europe PMC, both with overlap) was reusable and is in `adv285_*/search_adv285.py`; candidate for HE as a shared tool, not requested.

### 2026-11-26, SCI, ADV-291 and ADV-292
Gap: no single command lists the readable reading queue with the standing exclusions; the exclusions live in PREREG prose and three scripts of different dates, and SCI's first ADV-292 list was wrong by four records because of it. CHANGE = NONE in the harness for now: a bullet in the ADV-276 pre-read checklist. Candidate for HE if another reading batch follows ADV-292: one script that reads an exclusion table (record, reason, date) on top of `consumer_count.py`.

## 2026-11-28 - IT Orchestrator windows IT30 and IT31 (written by IT32 from the record)
Gap, repeated: a blind-verification packet can carry less than the source its sentence rests on (page 3 of a 24-page
supplement; a text conversion without front matter or image-only tables), and the reader then cannot judge a
whole-document negative. No tool checks it. CHANGE = NONE in the harness: the dispatch names the complete source files
and states what the conversion drops. Candidate for the harness scout, not implemented here. Evidence:
`session_evaluations/self_eval_orchestrator_it30_it31_20261128.md`. No external search, no spend.
