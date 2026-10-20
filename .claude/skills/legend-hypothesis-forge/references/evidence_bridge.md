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
endpoint, direction (INCREASE/DECREASE/UNKNOWN), source, locator, epistemic_status and context.
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
