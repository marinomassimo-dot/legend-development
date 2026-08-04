# DisMech Phase-2 independent derivation — blind contract

> **Non-canonical experimental contract.** This document contains the rules needed by an
> independent derivation, but none of the first pass's selected assertions, authored
> propositions, locators, state tallies, deduplication results or expected disagreements.
>
> Public, disease-level and de-identified. Nothing here is medical advice.

**Protocol version:** `blind-contract-v1`  
**Scope:** CLAIM 016, CLAIM 024 and CLAIM 035  
**Permitted inputs:** exactly the files declared by the bundle `MANIFEST.json`  
**Authoring outputs:** `output/second_derivation_authored.jsonl` plus
`output/run_attestation.json`. The later provenance reconciliation is outside the blind reader's
write authority.

## 1. Independence boundary

Work only inside the supplied bundle. Do not open the source repository, the first sidecar, its
generator or tests, the Phase-2 baseline, the independent-comparison design, revision histories,
reports, chat transcripts or prior reviews. Do not search for filenames named in the excluded
material. If any excluded input becomes visible, stop and mark the run `CONTAMINATED`; do not try
to compensate from memory.

The bundle contains two registries, an eligibility-only receipt projection and the source
artefacts whose fingerprints match qualifying complete reads. The projection intentionally omits
locator-extraction results from the first pass. Absence from the projection means that no
qualifying complete-read receipt was supplied; it does not mean the paper was not read in any
other historical sense.

The projection is generated, not curated. Its closed rule is: collect every `PAPER NNN` cited in
the complete registry blocks of `target_claim_ids`; resolve each paper's PMID from its
`Identifier` field; select the last ledger-ordered `complete_fulltext_read` event for that PMID, if
one exists; include exactly those active events and exclude complete reads of papers outside the
target claims. A cited paper with no qualifying complete event is absent by rule. A qualifying
paper without an allowlisted locator source makes bundle construction fail rather than being
silently omitted.

## 2. Units

Produce newline-delimited JSON using these record kinds:

- `assertion_candidate`: one registry span considered for atomisation;
- `assertion_occurrence`: one atomic, source-specific assertion derived from a candidate;
- `representation_item`: non-evidence content that cannot become an occurrence;
- `independent_run_manifest`: one record declaring protocol version, input-manifest digest,
  actor/session identifier, contamination status and output counts.

An assertion occurrence is the smallest statement with one epistemic type, one source, one
experimental context, one proposition and one causal direction. Multi-source convergence is not
one occurrence. Atomisation may split and re-attribute registry text; it may not generalise,
strengthen or supply a missing premise.

Context, qualifiers, negative results, species, system, allele state and transfer limits are part
of the assertion. Do not remove them to make two statements look alike.

## 3. Anchor and local identity

For every candidate record:

- `claim_id`: `016`, `024` or `035`;
- `registry_anchor`: `claim_registry_current.md#CLAIM NNN|<field heading>|sent[n]`;
- `raw_registry_span`: the exact registry sentence used;
- `atomization_outcome`: `ATOMIZED`, `ATOMIZATION_REQUIRED` or `NOT_EVIDENCE`.

For every occurrence add `registry_ordinal`, a zero-based local ordinal within its candidate.
`occurrence_id` is a deterministic hash of `claim_id + registry_anchor + registry_ordinal`.
The ordinal is a within-run identity component only. It is **not** a cross-run semantic match key.

Every occurrence must include:

```text
candidate_id, claim_id, registry_anchor, registry_ordinal, occurrence_id,
proposition, context, source_id, epistemic_type, evidence_relation,
terminal_state, locator, eligibility_receipt_event,
locator_extraction_receipt_event, content_fingerprint,
raw_link_role_paper_to_claim, raw_link_role_claim_to_paper,
claim_link_basis, normalised_role, unreached_tests,
locator_fingerprint, dedup_key
```

All hashes use UTF-8, SHA-256, lowercase hexadecimal and the first 12 hex characters after the
prefix. String components are used verbatim, the ordinal uses unsigned decimal notation, and
components are separated by the literal ASCII vertical bar (`|`), matching the Phase-2 production
hash contract. No listed hash component is optional:

```text
occurrence_id      = "OCC-" + H12(claim_id, registry_anchor, decimal registry_ordinal)
content_fingerprint = "CF-" + H12(proposition, context)
locator_fingerprint = "LF-" + H12(locator.snippet, locator.structural_anchor)
dedup_key           = "DK-" + H12(source_id, proposition, context,
                                   locator_fingerprint, epistemic_type, evidence_relation)
```

Hash exact authored text; do not canonicalise any production identity. The comparator computes
its separate diagnostic key later.

## 4. Epistemic and source rules

- `DATO`: the source directly states or shows the proposition.
- `INFERENZA`: the proposition is an explicit interpretation rather than a direct observation.
- `IPOTESI` and `ESPANSIONE`: not evidence assertions; route to a representation item.
- `evidence_relation`: `SUPPORT` for direct support, `PARTIAL` for indirect support or inference.
- A tensioning or counter-directional source is not supporting evidence for the proposition.
- Preserve paper→claim and claim→paper link evidence separately. Do not invent a raw role where
  the registry supplies only a link or prose reference.

## 5. Eligibility states and precedence

Assign exactly one terminal state to every occurrence, in this order:

1. `STATUS_INELIGIBLE`
2. `ATOMIZATION_REQUIRED`
3. `IDENTIFIER_UNRESOLVED`
4. `ELIGIBILITY_DEBT`
5. `LINK_ROLE_NON_SUPPORTING`
6. `LOCATOR_NOT_EXTRACTED`
7. `LOCATOR_PROVENANCE_MISSING`
8. `SOURCE_SUPPORT_NOT_FOUND`
9. `ELIGIBLE_FOR_EXPORT`

An occurrence is eligible only when the claim status is admissible; it is atomic; its paper and
identifier resolve; the receipt projection contains a qualifying complete read for the source;
the source link is supporting; and a verbatim locator exists with a new extraction receipt that
names the qualifying complete receipt as `prior_receipt` and this run's output as an output.

A qualifying complete read does not prove that a locator exists. Search for each occurrence's
support independently:

- no extraction attempted → `LOCATOR_NOT_EXTRACTED`;
- extraction decision without its own receipt → `LOCATOR_PROVENANCE_MISSING`;
- extraction completed and no supporting statement exists → `SOURCE_SUPPORT_NOT_FOUND`;
- supporting locator plus extraction receipt → passes the locator gates.

Targeted extraction is not a complete read. During blind authoring, every new locator decision
has `locator_extraction_receipt_event: null` and terminates at
`LOCATOR_PROVENANCE_MISSING`. Persist new extraction receipts through the normal validated writer
in the source repository only after the isolated run has ended. A separate deterministic
reconciliation may then create `output/second_derivation_reconciled.jsonl`; it must preserve the
authored file byte-for-byte and may change only `locator_extraction_receipt_event`,
`terminal_state` and `unreached_tests`. It also creates
`output/reconciliation_attestation.json` with both file hashes and the receipt events used.

## 6. Locator discipline

For a located statement record:

```json
{
  "snippet": "short verbatim extract",
  "structural_anchor": "section, figure, table or page",
  "source_fingerprint": "sha256 from the receipt projection"
}
```

Do not use keyword search as a substitute for reading a study. This run is a targeted extraction
from artefacts already covered by complete-read receipts; it does not claim a new complete read.
Inspect enough surrounding structure to determine whether the extract actually supports the
proposition and context.

## 7. Accounting and output

Every selected candidate must close:

- `ATOMIZED` → one or more occurrence records;
- `NOT_EVIDENCE` → one or more representation items;
- `ATOMIZATION_REQUIRED` → no occurrence, with the unresolved reason recorded.

Do not deduplicate by judgement. Compute `dedup_key` by §3 and group only occurrences that pass
every eligibility gate. Assign one deterministic evidence-assertion identifier per resulting
group and keep all originating lineages; excluded occurrences retain their own terminal states and
do not participate. Do not use any canonicalisation table: canonical candidate generation belongs
to the later comparator, not to the independent authoring pass.

The run manifest must declare:

```text
protocol_version, bundle_manifest_sha256, actor_session_id,
started_at, completed_at, contamination_status,
record_counts, output_sha256
```

`contamination_status` is `CLEAN` or `CONTAMINATED`. It attests the hash of
`second_derivation_authored.jsonl`, never a later reconciliation. A contaminated run is retained
as a rehearsal but is void as independent evidence.

## 8. Forbidden conclusions

This exercise does not modify any registry, establish a biomedical claim, validate DisMech
content, author a production exporter or approve canonicalisation for production deduplication.
Its result is a review packet for methodological comparison only.
