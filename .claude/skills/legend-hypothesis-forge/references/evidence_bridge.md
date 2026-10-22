# Evidence Bridge: local packet contract

This dependency-free increment compares explicitly supplied directions. It queries no
service and verifies neither scientific claims nor receipt existence. It does not load or
write canonical state. Input assertions remain caller-qualified, and every output is IPOTESI.

Run the synthetic example from the repository root:

```bash
python3 framework/scripts/repurposing_bridge.py .claude/skills/legend-hypothesis-forge/references/evidence_bridge_example.json
python3 framework/scripts/test_repurposing_bridge.py
```

Input schema version 1 requires candidate id/name, one route, one disease_assertion and
an array of drug_assertions (empty means abstention). Each assertion declares id, target_id,
endpoint, direction (INCREASE/DECREASE/NO_CHANGE/UNKNOWN), source, locator, epistemic_status and context.
The context contains disease_id, genotype, species, cell_type and developmental_stage;
UNKNOWN is explicit and prevents a resolved comparison. Reading depth defaults to UNKNOWN.
A complete_fulltext_read declaration requires a receipt reference but the tool does not
verify the ledger: use the existing receipt tools before scientific reuse.

The disease direction describes a measured/qualified change at the target endpoint relative
to its declared comparator. The drug direction describes its perturbation at that same
endpoint. Matching target, endpoint and all context dimensions permits a sign comparison;
any mismatch or unknown produces UNRESOLVED. Opposite signs yield OPPOSES_DISEASE_CHANGE,
matching signs REINFORCES_DISEASE_CHANGE, and opposing qualified drug assertions CONFLICTING.
None is a biological acceptance/rejection, ranking or safety verdict. Cross-context bridges
remain visible for Scientist interpretation rather than being silently treated as equivalent.

Put counterevidence, comparator, dose/time, source versions, receipt references, source-specific
relation_assertions/relation_conflict, shared-origin identifiers, scores and experimental plans
in the input packet as needed. All supplied fields survive unchanged under input. Missing
conflict metadata never becomes false. The checksum covers canonical JSON content, not the
original file bytes. The tool adds no probabilities or pooled score. Translational dimensions
remain UNKNOWN until separately qualified; this tool never certifies safety or efficacy.

Two optional P4 blocks are **declared in the packet, never performed by this tool**, which
has no network (added 2026-10-20 from the external drug-repurposing roadmap, which names both
and which this tool lacked):

`label_lookup` records a pharmacological-label search on two separate axes. `status` is
MATCH_FOUND, NO_MATCH_FOUND, QUERY_ERROR or NOT_ATTEMPTED; `coverage` is independently
COMPLETE_FOR_QUERIES_RUN, COVERAGE_INCOMPLETE or UNKNOWN, so NO_MATCH_FOUND with incomplete
coverage is a legal and distinct statement. Omitting the block yields NOT_ATTEMPTED, which is
never NO_MATCH_FOUND. A concluded search must list the `queries` actually run; NOT_ATTEMPTED
must not. MATCH_FOUND requires `product_name` or `spl_id`; QUERY_ERROR requires `error`;
COVERAGE_INCOMPLETE requires `coverage_limit`. `source`, `retrieved_at`, `client_version`,
`active_ingredient`, `formulation` and `method` (primary / alternative /
primary_then_alternative / UNKNOWN) default to UNKNOWN. The outcome never touches the
directional comparison, never ranks and never drops a candidate: NO_MATCH_FOUND is
information not available, not DRUG_HAS_NO_LABEL, not proof of absence and not biological
counterevidence; a label that exists certifies neither approval, currency, paediatric
suitability nor WOREE relevance. Each state writes its own line under `limits`.

`p4_fields` carries the fields the plan added later — `endpoint_pursued`,
`functional_evidence_available`, `temporal_or_model_limit` and a `cellular_context` of
`target_expression`, `cells_tissue_stage`, `coverage` and `limits`. Every one is always
present in the card and defaults to UNKNOWN rather than being absent, because a missing field
reads as "not applicable" while UNKNOWN reads as "owed". A pathway or expression change does
not substitute for the functional measure, and target expression is not drug selectivity.
Unknown keys in either block are rejected rather than silently kept, so a typo cannot
become a field and no weight or score can be smuggled in. An empty `drug_assertions` list is
reported as `abstention: NO_DRUG_ASSERTIONS_SUPPLIED`, which is a different fact from a search
that returned nothing.

The Monarch/DGIdb adapter now offers --json with timestamp, request and raw responses,
interaction actions and scores as returned. Monarch coverage is conservative: without an
explicit total matching returned items it says INCOMPLETE. It does not implement pagination.
Only HGNC gene neighbors enter the human gene-symbol lookup. Other identifiers and pathways
remain raw discovery material. DGIdb source attribution is limited to fields actually returned
by the existing query; primary database provenance needs further qualification. API versions
and live schema compatibility have not been verified by the offline tests. A valid empty
response, a query failure and incomplete coverage remain distinct.

The example uses fictitious identifiers and assertions. It demonstrates plumbing, not WOREE
evidence. No ZIP recovery, external installation, live query or experimental validation is
claimed. To disable the increment, omit the optional command and continue the existing forge.

## Reported null, translation fields, roadmap rows (2026-10-22)

`NO_CHANGE` is a REPORTED null effect; `UNKNOWN` is a cell nobody measured. On a comparable cell
NO_CHANGE yields `NO_EFFECT_REPORTED` (never OPPOSES/REINFORCES, never pooled with them: beside a
positive it is CONFLICTING); in a non-comparable cell it stays UNRESOLVED but the reason says it was
a measured null. A disease assertion with NO_CHANGE is UNRESOLVED. An optional `translation` object
(keys `pediatric_suitability`, `cns_exposure`, `interactions`, `access`, `time_to_benefit`,
`functional_rescue`; `access` means time to access) fills the card's `translation`; each defaults to
UNKNOWN, unknown keys are refused. If a packet carries `p4_roadmap_fields`, the two rows
`indication_and_transfer` and `verification_scope` must be nonempty strings (UNKNOWN allowed); the
block is validated, never rewritten. Packets without these inputs build exactly as before.

Several endpoints: a packet may give `disease_assertions` (a list, possibly empty) instead of
`disease_assertion` (never both). Each drug assertion is compared with the disease assertion on its
own target and endpoint; with none, it is UNRESOLVED ("no disease assertion on this target and
endpoint"). The singular spelling builds exactly as before.
