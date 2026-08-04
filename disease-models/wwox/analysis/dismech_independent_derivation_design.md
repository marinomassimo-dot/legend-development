# Independent derivation and canonicalisation — design

> **Non-canonical, and not yet executed.** This document designs and hardens a test. It does not
> perform the independent scientific derivation, modify production deduplication, emit DisMech
> nodes or change any canonical registry.
>
> Public, disease-level and de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Revision:** 11 · **Status:** GIT-ANCHORED INSTRUMENT, measurement not run
**Governs:** the independent second derivation owed by `dismech_export_spec.md` §14.1  
**Integrity baseline:** `data/dismech_phase2_baseline.json`  
**Blind contract:** `dismech_blind_derivation_contract.md`  
**Protocol tool:** `disease-models/wwox/analysis/scripts/dismech_independent_protocol.py`

## Revision 11 — aggregate verdicts disclose unavailable verification

Claude's Rev. 10 review confirmed that the Git anchor fails closed in a source archive, then
showed that the aggregate release runner still printed an unqualified `PASS` because Python's
test-level skip was visible only inside the individual target output. Rev. 11 makes the aggregate
verdict no stronger than the checks actually run:

1. the runner captures and republishes every target's output;
2. every `unittest` skip is counted with its stated reason;
3. zero skips retain `REGRESSION VERDICT: PASS`;
4. one or more skips produce `REGRESSION VERDICT: PASS WITH SKIPS`, the count and a target/reason
   line for each unavailable check;
5. an archive regression invokes the aggregate runner without `.git` and requires the verdict to
   name the unavailable Git-anchor verification.

This is a qualified successful run, not an authoritative integrity attestation. A fresh clone
with the object database remains the environment required for an unskipped Git-anchor check;
other environment-dependent checks may still qualify the aggregate verdict independently.

---

## Revision 10 — terminate trust in immutable Git objects

Claude's Rev. 9 review demonstrated that allowlist and baseline could be edited together and
re-sealed. Rev. 10 changes the trust model rather than adding another mutable hash file:

1. every declared input and output is committed in an immutable freeze commit;
2. `git_head_at_freeze` names that ancestor commit;
3. `verify-baseline` obtains each frozen blob with `git cat-file`, never from the working tree;
4. the declared hash must match the frozen blob and the current working bytes;
5. the baseline's own working bytes must equal its blob at `HEAD`;
6. the freeze commit must exist and be an ancestor of `HEAD`.

The exact two-file attack is a regression: editing the repository allowlist and updating its hash
inside an uncommitted baseline fails both because the baseline differs from `HEAD` and because the
new declared hash disagrees with the blob in the pinned tree.

This closes in-place and uncommitted re-sealing and makes every frozen byte recoverable with Git.
It does not claim protection from an actor authorised to create and approve a new sequence of
commits: at that boundary, commit review and the externally observed commit ID are the trust
anchor. The tool records and reports that identity rather than pretending a self-authored hash can
replace it.

A source archive without `.git` is publishable and can run the non-Git release checks, but it
cannot verify this baseline or build a blind bundle: `verify-baseline` returns non-zero by design.
The authoritative pre-measurement check therefore runs in a fresh clone that retains its Git
object database. The regression suite skips only the Git-specific positive test when that database
is absent; the CLI itself never converts absence into success.

---

## Revision 9 — root-of-trust and projection closure

Claude's hostile review reproduced one Rev. 8 bypass and one completeness gap. Both are closed:

| Rev. 8 defect | Consequence | Rev. 9 correction |
|---|---|---|
| Repository allowlist, receipt projection and blind contract were not sealed by the baseline | Editing the repository allowlist could legitimately copy the first sidecar into a bundle that still verified `CLEAN` | All three hashes are baseline inputs; `build-blind-bundle` runs baseline verification before copying anything; the exact leak experiment is a regression |
| Receipt projection was hand-authored | A missing qualifying paper could manufacture false eligibility divergence | Projection is deterministically generated from target-claim citations, paper identifiers and the last ledger-ordered complete receipt; committed bytes must reproduce exactly |

The projection rule includes PAPER 055 and PAPER 056, excludes cited PAPER 019 because it has no
complete receipt, and excludes complete reads 21212533 and 34214506 because their papers are not
cited by the three target claims. These are test outcomes, not authored membership.

---

## Revision 8 — hostile-review corrections

Rev. 7 had the right conceptual separation but its proposed measurement was not independent.
Four defects are corrected here rather than softened:

| Rev. 7 defect | Verified consequence | Rev. 8 correction |
|---|---|---|
| The second reader received the full export specification | §12 enumerates the first pass's decomposition, types, sources, states and expected merge | A self-contained blind contract contains generic rules but no live answers |
| The second reader received the full receipt ledger | events 35–36 disclose first-pass extraction counts, negative findings and sidecar outputs | An eligibility-only projection contains neither locator decisions nor first-pass outputs |
| The baseline hashed the complete append-only ledger | a legitimate later receipt would invalidate the baseline it was meant to preserve | The first 36 events are sealed as an immutable prefix; later suffix events are permitted |
| Axis 3 joined on locally assigned ordinal | different split order could compare unrelated propositions | Matching is within shared anchors: exact text first, canonical candidate second, ambiguity/unmatched otherwise; ordinal is never a join key |

Two implementation gaps are also closed: the canonicalisation table now exists as a versioned
asset with positive and negative fixtures, and a fail-closed tool verifies the baseline, builds
and audits the blind bundle, and compares completed outputs.

---

## 1. What is frozen, and what “frozen” means

`data/dismech_phase2_baseline.json` is an integrity seal for Rev. 7:

- exact hashes of the claim registry, paper registry, first generator and its test suite;
- exact hashes of the repository blind allowlist, generated receipt projection and blind contract;
- exact hash and record count of the first sidecar;
- the 19 occurrence identifiers, Ledger-A tally, evidence-assertion count and multi-lineage group;
- an append-only receipt-ledger prefix: event count 36, prefix SHA-256 and tail event ID.

The verifier requires every sealed byte to match. Receipt events appended after event 36 do not
invalidate the baseline; changing or truncating any of the first 36 does. This is the correct
identity for an append-only input.

Bundle construction invokes this verifier internally. Authenticating the bundle manifest against
an unsealed repository manifest is insufficient: the repository manifest itself is now part of
the sealed root of trust.

**Recovery boundary.** Every declared baseline input and output must exist as a blob in the pinned
Git tree. The verifier reads and hashes those blobs directly. A working file that exists but was
never committed cannot satisfy the contract.

Verification:

```bash
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py verify-baseline
```

Any error makes the comparison void. Re-freezing is a new baseline revision, never an in-place
repair made merely to obtain a green result.

---

## 2. The blind-input firewall

Independence is enforced by physical input isolation, not by asking a reader to ignore visible
answers.

### 2.1 Allowlisted packet

`data/dismech_blind_input_manifest.json` permits exactly:

1. the frozen claim registry;
2. the frozen paper registry;
3. `data/dismech_blind_receipt_projection.jsonl`;
4. `dismech_blind_derivation_contract.md`;
5. the PAPER 055 PDF matching its qualifying receipt fingerprint;
6. the PAPER 056 XML matching its qualifying receipt fingerprint;
7. the bundle's own `MANIFEST.json`.

The receipt projection contains only the active complete-read event, evidence depth, study
identifier, source fingerprint and bundle-local source path. It omits `evidence_basis`, outputs,
workflow, locator decisions and Phase-2 extraction receipts. Absence from the projection means
only “no qualifying complete receipt supplied”.

It is generated by one closed rule: for every paper cited in the complete registry blocks of the
target claims, resolve the PMID from the paper registry and select the last ledger-ordered
`complete_fulltext_read` event, if present. Papers outside target claims are excluded. The
committed JSONL must be byte-identical to this derivation:

```bash
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py \
  verify-receipt-projection
```

### 2.2 Explicitly excluded

- the first sidecar and Phase-2 report;
- the first generator, authored candidate table and tests;
- the Phase-2 baseline and all invariant counts;
- the full receipt ledger, especially locator events 35–36;
- the full export specification, revision history and live decompositions;
- this design and the canonicalisation fixture;
- prior chat, reviews and expectations.

The canonicalisation fixture is deliberately absent: it belongs to the comparator after both
authoring passes, not to the independent reader.

### 2.3 Materialisation and audit

Build into a new or empty directory:

```bash
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py \
  build-blind-bundle /an/empty/path
```

The builder verifies every source hash before copying. The verifier rejects missing, modified and
undeclared files:

```bash
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py \
  verify-blind-bundle /the/bundle
```

Verification is stage-specific:

- `--stage pre`: no output;
- `--stage authored`: exactly `second_derivation_authored.jsonl` and
  `run_attestation.json`;
- `--stage reconciled`: those immutable authoring outputs plus
  `second_derivation_reconciled.jsonl` and `reconciliation_attestation.json`.

The verifier compares the bundle's `MANIFEST.json` with the sealed repository allowlist before it
reads the internal declarations. Replacing the manifest therefore cannot authorise an extra file.

The independent actor must run in a fresh context whose working directory exposes only this
bundle. A run performed by an actor with retained knowledge of the first pass is a rehearsal,
even if the filesystem is clean. Visibility of any excluded input sets
`contamination_status: CONTAMINATED` and makes the run void.

---

## 3. Three identities, kept apart

| Identity | Basis | Answers | Authority |
|---|---|---|---|
| `occurrence_id` | claim + registry anchor + local ordinal | Is this the same within-run occurrence slot? | structural, within one pass |
| `content_fingerprint` | exact proposition + context | Did authored content change byte-for-byte? | drift signal |
| `canonical_candidate_key` | conservatively canonicalised proposition + context | Might two authored statements merit equivalence review? | diagnostic only |

**Rule K1 — no promotion.** The canonical candidate key never enters the production `dedup_key`,
changes no terminal state and causes no merge.

**Rule K2 — candidate, not equivalence.** Equal canonical keys create a review question. They are
not evidence that two propositions mean the same thing.

**Rule K3 — local ordinal only.** An ordinal participates in a within-run structural ID because it
distinguishes multiple atoms from one span. It never establishes correspondence between two
independent passes.

---

## 4. Canonicalisation v1

The closed, versioned configuration is
`data/dismech_canonicalisation_v1.json`. It is applied by the comparator, never by the second
authoring pass.

### 4.1 Ordered transforms

1. Unicode **NFC**, not NFKC. Compatibility folding is deliberately excluded so notation such as
   superscripts is not silently rewritten.
2. Explicit dash-character mapping to ASCII `-`.
3. Whitespace collapse and trim.
4. Closed biomedical aliases using case-sensitive whole-token matching.

Only `proposition` and `context` are transformed. Every changed string retains a transformation
trace with before/after text and, for aliases, the entity identifier. Review therefore sees why a
collision occurred rather than receiving an opaque hash alone.

V1 contains only the alias family required by the present claims: `GSK3β`, `GSK3beta`,
`GSK-3β`, `GSK-3beta` → `GSK3β`, identified conservatively as `gene-symbol:GSK3B`. `Tau/tau` is
not normalised because a global case substitution cannot establish entity usage from prose.
Under-canonicalisation is the intended direction of failure.

### 4.2 Forbidden transforms

- word or clause reordering;
- free synonym resolution;
- case-folding of prose;
- qualifier, caveat or context removal;
- negation normalisation;
- causal-direction normalisation;
- numeric rounding, range merging or residue rewriting;
- species, system, allele or isoform collapse.

Positive fixtures verify typography-only convergence. Negative fixtures cover negation, reversed
causality, different residue ranges, changed readout direction and human-versus-mouse context.

```bash
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py \
  verify-canonicalisation
```

Adding an alias or transform requires a new reviewable configuration revision and both a positive
fixture and a nearest-risk negative fixture.

---

## 5. Independent run protocol

The blind reader follows only `dismech_blind_derivation_contract.md`. It chooses its own registry
anchors, atomisation, propositions, contexts and source attribution. It does not receive expected
counts or known collisions.

The output uses `assertion_candidate`, `assertion_occurrence`, `representation_item` and one
`independent_run_manifest`. The manifest attests:

- blind-contract version and bundle-manifest hash;
- actor/session identity and timestamps;
- `CLEAN` or `CONTAMINATED` status;
- record counts and output hash.

Targeted locator extraction is not a new complete read. A locator decision is not eligible until
its new extraction receipt is persisted through the validated ledger writer and linked to the
qualifying complete receipt. Persistence happens after the isolated run, so
`second_derivation_authored.jsonl` carries `LOCATOR_PROVENANCE_MISSING` and null extraction-receipt
IDs for new locator decisions. It is immutable after attestation.

A deterministic reconciliation writes a separate `second_derivation_reconciled.jsonl`. It may
change only `locator_extraction_receipt_event`, `terminal_state` and `unreached_tests` and must
attest both hashes. The verifier compares every record and rejects any rewrite of proposition,
context, anchor, source, locator or epistemic judgement:

```bash
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py \
  verify-reconciliation /the/bundle
```

No second pass has been run in Rev. 8.

---

## 6. Four axes, never collapsed into one verdict

### Axis 1 — anchor selection

Compare sets of `(claim_id, registry_anchor)`. Report intersection, union, baseline-only and
second-only anchors. Jaccard is retained as a diagnostic description, never an acceptance score.

A difference means scope judgement differs. It is not an occurrence-ID failure.

### Axis 2 — atomisation and source attribution

For every shared anchor report, side by side:

- occurrence counts;
- source-ID sets;
- epistemic-type sets;
- evidence-relation sets.

This axis identifies under-specified splitting or attribution rules before semantic matching is
attempted.

### Axis 3 — proposition correspondence

Within each shared anchor:

1. pair unique exact `(proposition, context)` matches as `IDENTICAL`;
2. among residuals, pair unique equal canonical candidate keys as `CANONICAL_CANDIDATE`;
3. retain non-unique collisions as `AMBIGUOUS_MATCH_GROUP`;
4. retain every residual occurrence as baseline-only or second-only.

The comparator never pairs by ordinal. It also refuses to force a pair merely to reduce the
unmatched count. Every canonical candidate, ambiguity and unmatched occurrence is a review item.

### Axis 4 — deduplication

Dedup partitions are compared only over unambiguous cross-run correspondences. For every pair of
matched occurrences, the comparator asks whether each pass places that pair in the same production
dedup group. It separately reports the diagnostic canonical-candidate partition.

The production key remains unchanged whatever the diagnostic partition shows.

Run only after a valid second sidecar exists:

```bash
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py compare \
  disease-models/wwox/analysis/data/dismech_sidecar_016_024_035.jsonl \
  /the/reconciled/bundle > comparison_review_packet.json
```

The CLI refuses comparison unless the baseline, sealed bundle, clean run attestation, immutable
authored output and provenance-only reconciliation all verify. The report explicitly contains
`aggregate_verdict: null`. It is a review packet, not a score.

---

## 7. Acceptance and closure

The measurement counts only when all of these hold:

1. the Phase-2 baseline verifier passes;
2. all baseline-referenced bytes are durably recoverable;
3. the bundle was built from the declared allowlist and verified before the run;
4. the actor ran in a fresh, isolated context;
5. the attestation says `CLEAN` and its bundle/output hashes verify;
6. authored and reconciled stage verification finds exactly the permitted outputs;
7. all four axes were computed on their declared universes;
8. every divergence is a labelled review item.

§14.1 closes only after each review item is resolved as:

- an under-specified generic rule, now amended and regression-tested; or
- an accepted judgement difference with a written reason.

It does not close on Jaccard, match percentage, absence of crashes or agreement produced by a
canonicalisation key.

---

## 8. Research-loop record

```text
experiment_id: DISMECH-INDEPENDENCE-PROTOCOL-REV8
question: Does an allowlisted blind bundle plus non-ordinal matching remove the verified
          contamination and correspondence defects without changing Rev. 7 output?
baseline: Rev. 7 design exposed full spec + receipt events 35–36 and joined Axis 3 by ordinal.
single_change: replace the measurement boundary with a sealed blind-input firewall and compare
               propositions within anchors by exact/canonical candidate matching.
success_criterion: extra/mutated inputs fail; first-pass answers are absent; ledger suffixes pass
                   while prefix mutations fail; swapped ordinals match correctly; negative
                   semantic fixtures do not collapse; Rev. 7 remains byte-identical.
result: instrument implemented; measurement not run.
guardrails: no canonical scientific file modified; no production dedup change; no scientific
            conclusion; canonical keys remain diagnostic.
decision: KEEP for the instrument, pending independent hostile review.
next_step: Claude hostile-review Rev. 8; repair any contract defect before selecting the blind actor.
```

```text
experiment_id: DISMECH-INDEPENDENCE-PROTOCOL-REV9
question: Does sealing the repository packet definition and deriving the receipt projection close
          the reproduced allowlist bypass and false-eligibility risk?
baseline: Rev. 8 verified a bundle against an unsealed repository allowlist and carried an
          author-written two-row projection.
single_change_1: add manifest, projection and blind contract hashes to the baseline and require
                 baseline verification inside bundle construction.
success_criterion_1: adding the first sidecar to the repository allowlist makes verify-baseline
                     and build-blind-bundle fail before any leak bundle is produced.
single_change_2: derive the projection from target citations + paper PMID + last complete receipt.
success_criterion_2: committed bytes reproduce; target papers 055/056 are present; cited 019 with
                     no complete receipt and non-target complete reads are absent by rule.
result: both changes implemented and regression-tested; independent measurement not run.
guardrails: Rev. 7 sidecar unchanged; no canonical scientific file or production dedup modified.
decision: KEEP, pending Claude re-review.
next_step: hostile-review Rev. 9, then durable commit/snapshot before selecting a fresh blind actor.
```

```text
experiment_id: DISMECH-INDEPENDENCE-PROTOCOL-REV10
question: Does pinning every declared byte to an ancestor Git tree reject a coordinated working-
          tree edit of allowlist + baseline while making all sealed bytes recoverable?
baseline: Rev. 9 terminated trust at a mutable, uncommitted baseline.
single_change: commit the complete Phase-2 packet, then verify baseline-at-HEAD and every declared
               input/output against git_head_at_freeze:path via git cat-file.
success_criterion: clean committed baseline passes; one-file edits fail; two-file allowlist +
                   baseline reseal fails for both HEAD mismatch and frozen-blob mismatch; every
                   declared path is retrievable from the pinned ancestor.
result: implemented with a temporary-Git exploit regression and clean-export verification.
guardrails: no push; no four-current scientific change; append-only receipt prefix remains valid;
            trust boundary is stated as reviewed Git history, not absolute protection from an
            authorised committer.
decision: KEEP, pending Claude re-review of the Git trust boundary.
next_step: only after a green review, select an actor with no exposure to prior derivations.
```

```text
experiment_id: DISMECH-INDEPENDENCE-PROTOCOL-REV11
question: Does the aggregate release verdict disclose when the authoritative Git-anchor check
          cannot run in a source archive?
baseline: Rev. 10's protocol test correctly skipped its positive Git-object check without .git,
          while the aggregate runner still printed an unqualified PASS over all 40 targets.
single_change: aggregate unittest skip counts and reasons in the release runner and qualify the
               successful verdict whenever at least one check is skipped.
success_criterion: a source-archive execution names the Git-object skip in PASS WITH SKIPS; a run
                   with zero skips alone may emit the plain PASS form; the runner remains exit 0
                   because the limitation is disclosed rather than misrepresented as verified.
result: implemented with a nested source-archive runner regression; measurement not run.
guardrails: no baseline, scientific registry, sidecar or production matcher modified; no skip is
            converted into a failure or silently discarded.
decision: KEEP, pending Claude hostile review of Rev. 11.
next_step: after a green review, select an actor with no exposure to prior derivations.
```

## Related artefacts

- `dismech_export_spec.md`
- `dismech_sidecar_phase2.md`
- `dismech_blind_derivation_contract.md`
- `data/dismech_phase2_baseline.json`
- `data/dismech_blind_input_manifest.json`
- `data/dismech_blind_receipt_projection.jsonl`
- `data/dismech_canonicalisation_v1.json`
- `disease-models/wwox/analysis/scripts/dismech_independent_protocol.py`
- `disease-models/wwox/analysis/scripts/test_dismech_independent_protocol.py`
