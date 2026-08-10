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

### Invalidating a receipt whose study identity is unsupported

A metadata correction cannot repair a receipt whose reading evidence belongs to a different
study: preserving the wrong identity would keep false reading depth, while changing it would
rewrite what the event attested. Append a linked `record_kind: receipt_invalidation` event
with `reread_reason: receipt_invalidation`, `invalidates_receipt` equal to its direct
`prior_receipt`, and a substantive `invalidation_reason`. The reading fields remain unchanged
so the administrative event cannot manufacture a new read. Consumers remove that study from
the active depth index; the invalid original remains visible and hash-chained. A later genuine
read may establish new depth through a new linked event.
