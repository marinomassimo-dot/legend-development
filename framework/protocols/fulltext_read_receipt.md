# Full-text read receipt — universal trace contract

> Applies to every disease model, workflow, skill, agent and ad-hoc analysis. It does not
> matter whether the work is called deep dive, discovery, dossier, red team, Q&A or batch.

## Invariant

No workflow may say that a study's full text was analysed unless it emits a
`FULLTEXT_READ_RECEIPT`. The receipt is the durable evidence that the paper was actually
worked, at what depth, through which sections, and with which outputs.

Retrieval, local storage, text extraction, indexing, RAG lookup, keyword search and reading
selected passages are different events. None of them means `complete_fulltext_read`.

## Before reading: duplicate-work gate

Resolve PMID and DOI, then query the authoritative receipt/tracking view before fetching or
analysing the paper.

- Existing `complete_fulltext_read` receipt with adequate coverage: reuse its dossier and
  outputs. Do not repeat the full reading.
- Existing partial receipt: resume from the uncovered sections.
- A new complete reading is allowed only with an explicit `reread_reason`: new article
  version or supplement, inadequate earlier coverage, contradiction/retraction, a genuinely
  new question outside the earlier coverage, adversarial re-analysis, or explicit operator
  request.
- A preprint and its published version are linked but are not silently treated as identical.

This gate saves tokens without turning an old shallow pass into a permanent false negative.

## Evidence-depth states

| State | Meaning | Counts as full text analysed? |
|---|---|---:|
| `retrieved_not_read` | File obtained or validated only | No |
| `queried_not_full_read` | Indexed/RAG-searched or selected passages inspected | No |
| `abstract_only` | Abstract/metadata analysed | No |
| `partial_fulltext_read` | Some full-text sections read; missing sections named | No |
| `complete_fulltext_read` | Entire available article read section by section; unavailable material named | Yes |

`complete_fulltext_read` requires a coverage map for Abstract, Introduction, Methods,
Results, Figures, Tables, Discussion, Limitations and Supplementary. Each value is
`read`, `captions_only`, `not_present`, `unavailable` or `not_read`; a complete receipt may
not contain `not_read`. Only a conservative `legacy_reconstruction` may use `unknown_legacy`,
and that state can never support `complete_fulltext_read`.

### 🔴 A receipt attests reading. It does not attest quotation.

**Capture the verbatim locator while the document is open.** For every statement the reading
will carry out, record the exact sentence that supports it: what it is evidence *for*, the
sentence quoted verbatim, and where in the source it sits — section, figure or table. They go
in the work manifest under `verbatim_locators`, and
[`deepdive_manifest.py`](../scripts/deepdive_manifest.py) refuses a `complete_fulltext_read`
without them.

**Reading and quoting are different facts, and the receipt only carries the first.** On
**2026-08-04** an export to an external knowledge base found that **no verbatim locator
existed anywhere in the canonical state**, across every complete read in this ledger.
Fourteen had to be recovered afterwards from two already-read papers, reopening the files and
issuing targeted receipts. The readings had recorded conclusions and not quotations.

Seconds while the document is open; a second reading to recover. And a knowledge base that
requires exact quotes — as DisMech does — cannot accept a conclusion without one, however
carefully it was reached.

If a reading supports no statement at all, waive the section with an argument. Waiving is
legitimate; silence is not, and a waiver surfaces as `[DECLARED GAP]` in
`session_self_eval.py`.

For every **new** complete read, the work manifest uses schema v2. Each evidentiary locator
must declare `surface` and `artifact`; `abstract` is not an evidentiary surface. The manifest
binds every artifact to SHA-256. At persistence time, body/table/supplement quotations are
matched against the declared local XML/HTML/TXT/DOCX with the article abstract separated
from its body; visual locators are bound to the inspected image hash. Missing fields,
unverified text, missing artifacts and declared gaps all block the append. Historical schema
v1 manifests remain visible as migration debt and are not rewritten. For a PDF, declare the
fingerprinted PDF as `article_binary` and a deterministic extracted TXT as `article_text`;
text locators point to the latter while the receipt remains bound to the former.

### 🔴 Evidence locality across branches

`files/` is gitignored for copyright reasons. A branch therefore transports a manifest but
does **not** transport the evidence bytes named by that manifest. Every probatory artifact
must be written to the persistent `files/` tree of the shared checkout, never only to an
ephemeral worktree or `/private/tmp`. A PASS obtained before that temporary workspace
disappears is historically true but operationally unverifiable and does not close the read.

When manifest work is isolated on a branch, keep the two roots explicit. `--workspace` is
where the versioned manifest and receipt ledger live; `--artifact-workspace` is the shared
checkout whose `files/` tree contains the fingerprinted evidence. Both validators retain
their containment checks within the selected evidence root:

```bash
python3 <branch>/framework/scripts/deepdive_manifest.py \
  --workspace <branch> --artifact-workspace <shared-checkout> \
  --disease wwox --pmid <PMID> --verify-artifacts --require-current-schema

python3 <branch>/framework/scripts/fulltext_receipts.py \
  --root <branch> --artifact-workspace <shared-checkout> \
  record --receipt <event.json>
```

The strict manifest command that counts is launched with the shared checkout as the current
directory and must resolve the evidence there. Omitting `--artifact-workspace` preserves the
single-workspace fail-closed default; a symlink that escapes the selected workspace remains
an error rather than a hidden bypass.

### 🔴 A text layer is not its page

**Seek XML/HTML PMC first, every time, and record its absence.** A PDF text layer is a
derivative of convenience; in this corpus it is often not the author's characters at all.
`PMID 33914858` extracts as `P 5 0.05` where the page prints `P < 0.05`, and three independent
extractors agree on the wrong character because they read the same defective layer —
**cross-checking extractors detects nothing**. 33 of 51 local PDFs carry the defect, and it
consumes precisely the load-bearing marks: `Wwox\x01/\x01` for `Wwox⁻/⁻` against
`Wwox\x02/\x01` for `Wwox⁺/⁻`, `q` for `±`, `D2` for `χ²`, `t` for `×`. Roughly four fifths of
the damage is printable, so a control-character screen alone is not enough and a "repair" of
the visible controls produces a surface that looks verified and is not.

Structured markup carries correct entities and has no rendered page to diverge from. That is
why every one of the fifteen existing complete reads is sound: all used XML or HTML.

`deepdive_manifest.py` screens a declared text surface for C0 controls, printable
substitutions and **suspicion by absence** — statistical language with none of
`< > ≤ ≥ ± × −`. A `SUSPECT` surface is refused, never normalised, and it cannot support
`complete_fulltext_read`. When no structured surface exists, the reading either anchors the
affected locators to the rendered page — which adjudicates, because the drawn glyph is the
author's — or declares the debt. It never hand-corrects the text: a manual fix across dozens
of points is indistinguishable from a rewrite and verifiable by nothing.

`abstract_snippet` resolves a different, interoperability-only obligation: when an external
index exposes the abstract but not the full text, it may accompany a non-abstract locator so
the headline proposition remains externally checkable. It is companion metadata, **never the
evidentiary quote**: it does not change `surface`, does not satisfy body/table/supplement
verification and cannot support `complete_fulltext_read`. The locator must still carry its
verbatim full-text `snippet`, non-abstract `surface` and fingerprinted `artifact`.

### 🔴 `captions_only` — because a caption is not its figure

`read` on `figures` or `supplementary` means **the images were inspected**. When only captions
and legends were read, the honest value is `captions_only`, and it **downgrades the receipt to
`partial_fulltext_read`** — `complete_fulltext_read` is refused.

This is not pedantry. On **2026-07-26** the single most valuable finding of a deep dive was that
Wang 2012 (PMID 22193544) describes its Supplementary Figure A, in **both** the main text **and**
the published legend, as the co-IP proving *"WWOX does not associate with Tau"* — while the image
contains **no Tau blot at all**, its two panels being labelled WWOX and GSK3β. Text and caption
agreed with each other and both were wrong. Reading the text more carefully could not have caught
it; only opening the image could. Had the caption been trusted, LEGEND would have registered a
false contradiction against a live mechanism — the silent, self-reinforcing kind of false negative
the whole discipline exists to prevent. See `D-14` in the dismissal ledger.

### `references` — optional, and a ratchet

`references` is an **optional tenth key**: the nine above are anchored in receipts already
persisted, and an append-only ledger cannot be retro-fitted. New reads should declare it.

It exists because **the reference list is where multi-hop expansion starts.** In the same
2026-07-26 run, a receipt declared `complete_fulltext_read` while the 28-item reference list had
never even been enumerated. The list turned out to contain a paper — the neuron-specific GSK3β
isoform, PMID 20067585 — that **qualified the reading's own inferences** and named a risk absent
from the therapeutic scoring. Debt had been *declared* and not *paid*; declaring it does not pay
it. `session_self_eval.py` reports the absence of this key rather than blocking on it.

## Required receipt

Every analysis-capable worker returns this block to its caller, even if the worker is
read-only:

```yaml
FULLTEXT_READ_RECEIPT:
  event_id: FTR-YYYYMMDD-<PMID-or-DOI-slug>-NN
  record_kind: contemporaneous_receipt
  study_id: {pmid: "...", doi: "..."}
  event_at: YYYY-MM-DDTHH:MM:SSZ
  analysis_at: YYYY-MM-DDTHH:MM:SSZ
  workflow: <skill/agent/ad-hoc route>
  evidence_depth: complete_fulltext_read
  source_locator: <PMCID, lawful URL, or local path>
  source_fingerprint: <sha256 when a lawful local artifact exists, otherwise null>
  source_kind: fulltext_local
  analysis_time_precision: second
  coverage:
    abstract: read
    introduction: read
    methods: read
    results: read
    figures: read
    tables: read
    discussion: read
    limitations: read
    supplementary: unavailable
  outputs: [<dossier, commit-candidate, ledger entry, report>]
  evidence_basis: [coverage_map, dossier]
  prior_receipt: null
  reread_reason: first_read
```

🔴 **`outputs` is what the run TOUCHED, not what the receipt ATTESTS, and reading it the
other way is a trap that survives inspection.** On 2026-08-11 an inverse index built from
`outputs` produced a plausible, well-formed and entirely false picture: five "stale or
unclaimed" manifest→receipt pointers and one "cross-claimed" manifest. The authoritative link
is the manifest's own `receipt` field, and measured directly it is correct on all 36 manifests
— zero absent, zero pointing at another paper's receipt.

The false positive is worth keeping because of its shape: `PMID38499540.json` appeared in the
`outputs` of `FTR-20260810-25331887-01` because **that reading really did write into that
file** — legitimate multihop work. A guard built on this field would have flagged exactly the
cross-paper reading we want, and its count would have risen with the quality of the reading.
No consumer in this repository derives attestation from `outputs`; the only thing that did was
a reviewer's inference. Same class as `<fig\b` matching `<fig-count>`: **a plausible predicate
that answers a different question from the one you asked**, invisible to any check that only
verifies the result is well-formed, because the result is well-formed.

🟡 **OPEN, deliberately not decided in a merge: what does a manifest's `receipt` point at —
the reading that PRODUCED the manifest, or the most recent reading of that paper?** The
validator requires the field and checks nothing about its target, so the tooling has no
opinion. `PMID42422765.json` declares `…-04` while `…-05` is a later receipt for the same
paper whose `outputs` name the manifest file. Under one reading `-04` is right, under the
other `-05` is; both are internally consistent, and neither is a referential defect. Changing
it swaps one truth for another, which is why `rechain --repoint-manifests` must never be
pointed at this case: it exists to follow a **renamed identifier**, not to re-decide which
reading a manifest documents.

`source_fingerprint` is mandatory whenever a **contemporaneous** receipt names a local
artifact. A receipt over a file that carries no digest claims "I read *this* document"
about something that can be replaced, truncated or regenerated afterwards while the receipt
keeps vouching for it. Remote locators (a PMCID, a lawful full-text URL, a bare DOI) have
nothing to hash and stay `null` for partial/legacy events. A **new complete** receipt is
stricter: it requires a lawful local PDF/XML/HTML snapshot, its exact repository-relative
path and a matching SHA-256, so a PubMed abstract page cannot masquerade as the document.
`event_at` is stamped by the authoritative writer; `analysis_at` remains the worker's
declaration and carries explicit `analysis_time_precision`. A `legacy_reconstruction` cannot
hash what it did not witness.

Machine-readable shape: [`fulltext_read_receipt.schema.json`](../schemas/fulltext_read_receipt.schema.json).

Executable append/query/validation utility:

```bash
python3 framework/scripts/fulltext_receipts.py status --pmid <PMID>
python3 framework/scripts/fulltext_receipts.py record --receipt <event.json>
python3 framework/scripts/fulltext_receipts.py validate   # parse + chain
python3 framework/scripts/fulltext_receipts.py verify     # + state-manifest tail anchor
python3 framework/scripts/fulltext_receipts.py anchor      # re-anchor after a repair
```

`status` exits `0` only when the ledger contains a complete receipt for that study; partial
or absent history exits `1`. This makes the preflight usable as an execution gate.
Unless explicitly overridden for testing or a different disease instance, all commands use
the authoritative sink
`disease-models/<disease>/registries/fulltext_read_receipts.jsonl`. A missing or invalid
ledger fails closed. Appends take an exclusive filesystem lock, revalidate the complete
history, append one event, flush and `fsync` before reporting success.

## Append-only is enforced, not asserted

Calling a file append-only does nothing. Three mechanisms make the word true, each covering
a failure the previous one cannot see:

| Mechanism | Detects | Where it is checked |
|---|---|---|
| `ledger_prev_hash` chain over every persisted event | a historical event rewritten or deleted | `validate`, and `LINT` as `BLOCK_SYSTEM` |
| tail anchor (`fulltext_ledger_events` + `fulltext_ledger_head`) in the state manifest | the ledger **truncated from the end** — the surviving prefix stays perfectly self-consistent, so no chain can see this | `verify`, and `LINT` as `BLOCK_SYSTEM` |
| exclusive `flock` + full revalidation, strict schema-v2 work-manifest verification and atomic anchor update inside the lock | concurrent appends interleaving, direct calls bypassing the CLI gate, appends extending an already-corrupted history, and partially written manifest updates | `append_receipt` |

The chain field is stamped by the ledger writer and never authored by hand: a skill or agent
emits exactly the receipt shown above, with no integrity bookkeeping to get wrong.

**The honest limit.** Someone who rewrites the ledger *and* re-anchors the manifest in the
same operation is not caught by arithmetic — nothing self-contained can catch that. What the
design guarantees is that such an edit is a visible diff in a second file, under version
control, rather than an invisible one. The integrity claim degrades to "reviewable", never
to "undetectable"; overstating it would be exactly the kind of unearned assurance this
protocol exists to prevent.

## Merging two branches that both appended — `rechain`

🔴 **A hash chain refuses two parents, and that refusal is the design working, not a bug in
anyone's branch.** When two actors append different events onto the same predecessor, neither
line is wrong and the *concatenation of both* is: the second event's `ledger_prev_hash` names
a predecessor that is no longer its predecessor. Git will merge the two JSONL files without
complaint — they touch different lines — and `validate` will then say `line 61: broken hash
chain`. Resolving it by editing the file is forbidden and would not help: the digests are over
the whole records.

Measured on **2026-08-10**, when the fork stopped being hypothetical: three of five branches
had diverged — `lettore` at event 60, `lettore-b` and `codex/pmid-42422765-s8` at event 61 —
and three of five merges were blocked at once.

The only lawful resolution is to **move one line's events to the end of the other's history**,
recomputing nothing but their position:

```bash
git show main:disease-models/wwox/registries/fulltext_read_receipts.jsonl > /tmp/base.jsonl
python3 framework/scripts/fulltext_receipts.py rechain --onto /tmp/base.jsonl --dry-run
python3 framework/scripts/fulltext_receipts.py rechain --onto /tmp/base.jsonl
```

`--dry-run` names every event that would move and writes nothing. Without it the ledger is
rewritten under the same exclusive lock `append_receipt` uses, re-read from disk, and the
manifest tail anchor updated in the same operation; if any of that fails the original bytes go
back.

**What `rechain` refuses, and why each refusal is not decoration:**

| Refusal | The failure it prevents |
|---|---|
| the base's own chain must verify | extending a corrupted history with fresh, honest-looking links |
| the incoming chain must verify | moving events that were already untrustworthy |
| a moved event may differ in `ledger_prev_hash` **and nothing else**, re-compared after the fact | a rewrite wearing a merge's clothes — a coverage map or a fingerprint quietly changed in transit |
| the base prefix must come out byte-identical | a mutation applied *before* a digest is taken yields a chain that verifies against the mutated event, so neither the chain nor the sequence check would say a word |
| `validate_ledger_sequence` runs over the merged whole | ordering is not the only thing a merge breaks — see below |

🔴 **The last one is the one that actually fired.** `lettore` and `codex/pmid-42422765-s8`
both recorded a second receipt for PMID 42422765 and both called it
`FTR-20260810-42422765-02` — one for the figures, one for Supplementary S8, different
coverage, different fingerprint, different source. Each branch is internally valid. The
collision exists **only once the lines are in one file**, which is precisely what no
per-branch check can see, and rechaining the second onto the first is refused with
`duplicate event_id`.

**That refusal is not something the tool may resolve.** Re-minting an event's identifier
changes its body, and a rechain that edited a body would be the thing this whole section
exists to forbid. Which of the two colliding events is renamed — and the downstream files
that name it — is an operator decision, taken before the second merge, not during it.

**Until a fork is rechained, keep appending.** A branch that goes on recording on its own line
is behaving correctly; the divergence is a chain refusing two parents, not an actor's mistake.
What must not happen is a hand edit of the ledger to make a merge look clean.

## The registry-declaration ratchet

The receipt ledger is the authority on *reading*; the paper registry is the authority on
*claims*. When the two disagree — a registry record declaring `full text reviewed` with no
persisted complete receipt behind it — the disagreement is data, not an error to smooth over.

Records predating the ledger are grandfathered by **count and exact record identity**, recorded
in the state manifest as `registry_only_fulltext_declarations_baseline` and
`registry_only_fulltext_declaration_ids`. Count alone is not a ratchet: deleting one old
declaration and adding an unsupported one elsewhere leaves the same number. Deleting the
historical records would falsify history;
retroactively upgrading them to `complete_fulltext_read` would manufacture evidence. So they
are kept visible and frozen: `LINT` returns `BLOCK_BATCH_COMMIT` when a non-grandfathered
identity appears, even if the total count is unchanged. This forces every new full-text
declaration through a real receipt. When the count falls —
because a record was genuinely back-filled against surviving evidence — `LINT` says so as
`INFO`, and the baseline plus resolved identities are lowered by hand. The ratchet only
turns one way.

## Persistence and canonical promotion

1. A read-only subagent returns the receipt; it must not pretend that chat output alone is
   durable state.
2. The calling/main session persists it in the authoritative append-only operational receipt
   sink **before closing the turn or reporting the paper as read**.
3. The next lawful `BATCH_COMMIT` mirrors the highest supported depth and receipt reference
   into the literature tracking / paper registry. Canonical files are never edited around
   the batch gate.
4. If persistence fails, the outcome is `ANALYSIS_DONE_RECEIPT_NOT_PERSISTED`: report the
   failure and keep the paper in reading debt. Never silently mark it complete.

The coverage report and batch queue consume this ledger directly and fail closed if it is
missing or invalid. The receipt sink is the event history; those generated views are not
the event history and must remain reconstructable from it.

## Historical reconstruction is not a contemporaneous receipt

Never fabricate a past analysis timestamp or coverage map. A backfill inferred from old
dossiers, commit candidates, notes or logs uses `record_kind: legacy_reconstruction`, may
set `analysis_at: null`, and lists every supporting artifact in `evidence_basis`. File
presence or a retrieval manifest alone supports only `retrieved_not_read`. A legacy record
may claim `complete_fulltext_read` only when surviving evidence demonstrates complete
section-by-section coverage; otherwise it remains partial or unresolved reading debt.

## Prohibited shortcuts

- No complete receipt inferred only from `integrated`, `promoted`, a claim, or a citation.
- No receipt inherited by papers cited inside another paper.
- No complete receipt from file presence, PMC availability or a retrieval manifest.
- No second full read merely because a different skill was invoked.
- No overwrite: corrections and rereads append a new event linked through `prior_receipt`.

### Correcting receipt metadata without fabricating a reread

If a persisted receipt names the wrong output path or record because of a collision, append
a linked event with `reread_reason: receipt_correction`. This is **not** a second reading.
The writer requires the correction to preserve `record_kind`, study identity, `analysis_at`,
evidence depth, source locator/fingerprint and the complete coverage map; only event metadata,
evidence basis and outputs may change. Consumers use the latest equal-depth event, while the
incorrect historical event remains visible in the hash chain.

## Named open schema items — registered, not designed

Four defects in this contract are **known, measured and deliberately unfixed**. The first three
are schema, so they belong to the operator; the fourth is an enforcement absent from the
validator, blocked only until one manifest is corrected by its author. None of them breaks
anything while nothing changes, which is why registering them is the whole of the right action
today.

🔴 **Registering is not deferring.** A proposal that lives in a cross-session message dies with
the session, and the loss is invisible because nobody misses what they never saw written. Each
item below therefore carries **its own measurement, reproduced here rather than reported** —
so that whoever eventually designs the fix inherits the evidence and not a recollection of it.
The commands are in this repository; the numbers are dated because they will move.

One rule binds any of these if it is ever built, and it is deliberately narrower than the form
it was first written in:

> **New records must declare the field. The treatment of legacy records — absence,
> `unknown_legacy` in a derived view, or an explicit migration — remains part of the schema
> decision and is not anticipated here. No substantive value will be reconstructed from
> branches, chat or memory.**

🔴 **The wider form was self-contradicting and is recorded rather than quietly replaced.** It
read "prospective only · marked `unknown_legacy` on every existing record · never backfilled",
and **marking every existing record is exactly a backfill.** Worse, receipts are append-only:
a mark on a persisted record is not a write this system permits at all. The demand for
`unknown_legacy` is preserved above; what is not preserved is the pretence that where it
materialises has already been decided.

### 1. The figure denominator has no basis, and today it has no schema either

`panel_coverage` reports a fraction. Nothing anywhere says **what the denominator counted**,
and the surfaces disagree: a published figure, a PMC rendering and a supplementary sheet split
panels differently, so a count without its surface is a number without an object.

Measured 2026-08-11 across the 50 manifests in `deepdive_manifests/`:

| key | manifests | container | type |
|---|---|---|---|
| `panel_coverage` | 12 | `/reading_budget/` | free-text string — `5/17`, `0/26`, `39/39 panels inspected as images` |
| `figure_coverage` | 3 | `/verbatim_locators/` | dict |
| neither | 35 | — | — |

No manifest carries both, and `grep -rn "panel_coverage\|figure_coverage" framework/scripts
scripts .claude` returns **nothing**: neither key is read by any code. Two names, two
containers, two types, one validator that has never seen either.

🔴 **Their existence does not make the proposal redundant — it is the argument for it.** Two
ungoverned representations of one quantity are not a partial implementation of an authoritative
form; they are the two things an authoritative form has to consolidate, and neither can be
promoted as-is, because neither records what it counted.

The proposal, recorded as received: one authoritative place in the **manifest**, beside the
figure inventory — `panels_present`, `panels_inspected`, `denominator_basis`,
`denominator_status` — which the receipt **summarises or references and never duplicates**.
`denominator_status` is what lets `unknown` be said honestly instead of a figure being forced.
This is the slot `SURFACE_CONTAINMENT_PRECHECK_GATE` names as contract territory.

🔴 **Counted per artifact and per surface, never as one global scalar.** This follows directly
from the reason the field is needed at all: if the published figure, the PMC rendering and the
supplementary sheet do not agree on what a panel is, a single number averages surfaces that
are not the same object — and it would report a clean fraction while doing it. The twelve
free-text values above are already global scalars, which is why none of them can say what it
counted.

### 2. A receipt changes author when it is merged

The ledger has **no `actor` field** — 19 distinct keys, none of them naming who read the paper.
Attribution is therefore reconstructed from *which branch holds the record*, and that method
decays with exactly the operation this repository runs to make progress.

Reproduced 2026-08-11 over 20 local and remote refs: **114 distinct `event_id`, 106 present on
more than one ref, 8 on exactly one.** `FTR-20260810-34831305-01…04` live on 10, 10, 10 and 9
refs respectively. For 93% of the ledger, "the branch that holds it" reports **propagation** —
which histories have been carried where — and propagation is not authorship. The
identification fails not because the branch set is noisy but because it answers a different
question.

🔴 **And the single-branch class is a queue, not a population.** All 8 singletons are today's
unmerged tail, timestamped 17:57–20:50 UTC on `lettore`, `lettore-b` and one `codex/` branch.
The same count was **6** four hours earlier: new reading pushes records in, propagation pushes
them out.

🔴 **But the mechanism is propagation, not merging, and the difference is not pedantic.** The
statement to keep is: *propagating a history that contains receipts to a **new** ref may
increase the apparent holders; a merge that carries no new receipts, or one into a branch that
already holds them, changes nothing.* Measured over the three merges of 2026-08-11 —
`git rev-list --parents -n1 <merge>`, then the `event_id` sets of each parent:

| merge | target | incoming | new to target | result |
|---|---|---|---|---|
| `4c458d1` | 94 | 63 | **0** | 94 |
| `2629cff` | 94 | 94 | 1 | 95 |
| `8030d20` | 95 | 101 | 11 | 106 |

One merge in three moved nothing, and it was the largest-looking one by branch age. "Every
merge dilutes attribution" reads like a tax on integration and would make an integrator
hesitate over an operation that **can** be free — one of these three added nothing, and `n = 3`
supports exactly that and no rate. "A third of merges is free" is the sentence to avoid, and it
is the one I wrote first: three observations do not carry a frequency, and a frequency is what
an integrator would plan around. The honest consequence
is not to merge less — it is to **never promise anyone that attribution is recoverable after
the fact.** Provenance identifies an author at the moment of writing and stops meaning that
afterwards.

Hence the second half of the proposal: an eventual `actor_id` is **separate from the runtime
endpoint** — an endpoint is where a session could be reached today, an actor is who did the
work — and, like every item here, is **never reconstructed retrospectively**, least of all from
branch membership, which the table above shows is not the quantity anyone thinks it is.

### 3. Back matter is inside the evidential surface, and the obvious fix breaks two real locators

`_xml_surfaces` separates the abstract and nothing else, so where a deposit folds the
bibliography into `<body>` — Europe PMC does; `efetch` files it under `<back>` — reference
titles sit in the surface a locator is verified against. On `PMID 30158849`, 122 of 127
`<article-title>` elements are verbatim in the surface, and a review's reference titles read
exactly like its own findings.

The obvious repair is to drop `ref-list`, `ack`, `fn-group` and `back` from the body surface.
Measured 2026-08-11 across **355 text locators on XML artifacts**, that repair would lose
**2** — both in `PMID30370248`, and both legitimate:

> `entries[6]` — *"Reference 53 is a human recessive cerebellar-ataxia paper, not a mouse
> seizure experiment"*, quoting that reference's title, anchored `Reference 53, Mallaret et al.
> 2014`. `entries[7]` is the same shape on `Reference 104`.

Their proposition **is about the bibliography**; the reference title is the object of the
claim, not a sentence smuggled in as the authors' prose. So the fix is not exclusion but a
**third declarable surface** — a locator says it is quoting back matter, and one that does not
may not land there. That is a schema change to `surface`, hence this list.

🔴 **What the 355 do and do not show.** The admissible form is: **in the current set, 353 of
355 XML text locators do not depend on back matter, and the two remaining are intentional
bibliographic uses.** They do **not** show that
contamination has never affected a reading — a reader misled by a reference title into a
conclusion that produced no locator leaves nothing for this measurement to find. The audit
covers the verified surface, not the reading. Said explicitly because "the hazard has not
bitten" is the kind of sentence that gets quoted without its denominator.

The two deliberate hits are still why the repair must not be built as if they were defects —
`ADJUDICATE_THE_DEFECT_LIST_BEFORE_BUILDING_THE_GUARD`.

### 4. A rule stated in a comment, enforced by nothing

`text_contradicted_by_panel` and `panel_qualifies_text` are assertions made **by the panel
about the text**, and the module says so: *"the marker belongs to the PANEL locator — the
evidence that makes the assertion."* Nothing checks it. A text locator may carry either marker
and point at another text locator, and the validator will accept text contradicting text
wearing the word "panel".

**The rule stands as written:** an entry asserting either relation is a reading of the panel
and declares `surface: figure`. Measured across the corpus, 59 coupled locators: 58 on
`figure`, **1 on `body`** — `PMID23435430.json` `entries[9]`.

🔴 **That one is an incompletely modelled case, not a counterexample, and I filed it as a
counterexample first.** The entry quotes the caption of Figure 6A, carries the coupled
relation, states that the pixels were inspected — and declares **no figure artifact at all**,
only the XML. The caption proves that Figure 6A shows HEK293T cells and not the hepatic result
the running text attributes to it: excellent *textual* evidence of a miscitation, and not the
panel reading the relation asserts. The pixels have neither artifact nor attestation.

The correct representation needs three locators, and the manifest has two of them:

| | locator | surface |
|---|---|---|
| 1 | the running text attributing the result to Figure 6A | `body` — exists, `entries[8]` |
| 2 | the caption, verified character-for-character | `body` — exists, `entries[9]`, without the coupled relation |
| 3 | the reading of Figure 6A's pixels, with a figure artifact and a visual attestation, carrying `text_contradicted_by_panel` → (1) | `figure` — **missing** |

The one thing that entry gets right and must not be "fixed": **the caption is not renamed
`figure`.** Its own anchor argues it — labelling a caption quote `figure` would exempt it from
character-for-character verification. It simply cannot stand in for the pixel locator.

So the open item is the **absent enforcement**, not a vocabulary change. Routed to the
manifest's author, who alone can attest to having looked at those pixels; the 59 will be
re-measured once the correction lands. If cases then remain that genuinely need two axes — as
`O7b` in the 2026-08-10 orchestration review argues on other grounds, together with
`panel_qualifies_text` and `schematic` — the vocabulary item gets registered **with those**,
and not with this one.

🔴 **Recorded because I had the discipline backwards.** I ran
`ADJUDICATE_THE_DEFECT_LIST_BEFORE_BUILDING_THE_GUARD` on a list of one, concluded the single
instance was legitimate, and stopped — which is the gate performed rather than applied.
Adjudication asks what an instance *is*; I asked only whether its author had a reason, found a
good one, and promoted "well argued" to "correctly modelled". A defect list of one is where
that substitution is easiest to make, because there is no second instance to disagree.

### Four fixtures to write before any of this is built

Kept here because they are the cheap part and they age well: each names a confusion that has
already occurred at least once, and a fixture written now costs nothing while a fixture
written after the implementation tends to describe whatever the implementation does.

1. **A receipt propagated to several branches does not change author.** The property under
   test is invariance, not the value — see the table in item 2.
2. **A historical receipt does not receive a future manifest.** No key introduced later may
   appear on a record written before it existed, by any route including regeneration of a
   derived view.
3. **A partial and a complete read of the same episode are one paper, not two.** The coverage
   and queue joins consume depth per study; two depths of one reading must not double a
   denominator.
4. **`abstract_anchoring_waived` is not a figure waiver.** Two independent waivers over two
   different surfaces; a locator waiving one must never be read as having waived the other.

None of the four is implemented. They are conserved with the proposal because they are what
would make it checkable rather than merely written down.

### Invalidating a receipt whose study identity is unsupported

A metadata correction cannot repair a receipt whose reading evidence belongs to a different
study: preserving the wrong identity would keep false reading depth, while changing it would
rewrite what the event attested. Append a linked `record_kind: receipt_invalidation` event
with `reread_reason: receipt_invalidation`, `invalidates_receipt` equal to its direct
`prior_receipt`, and a substantive `invalidation_reason`. The reading fields remain unchanged
so the administrative event cannot manufacture a new read. Consumers remove that study from
the active depth index; the invalid original remains visible and hash-chained. A later genuine
read may establish new depth through a new linked event.
