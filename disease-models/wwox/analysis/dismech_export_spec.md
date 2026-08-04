# LEGEND → DisMech export specification

> **Non-canonical.** This document specifies a proposed export contract. It writes nothing,
> promotes nothing, and modifies none of the four current files. It is a design artefact to be
> reviewed and revised before any code is written.
>
> Public, disease-level, de-identified throughout. Nothing here is medical advice.

**Status:** DRAFT rev. 7 — Phase 1 (specification), pending review
**Date:** 2026-08-04
**Supersedes:** rev. 1, rev. 2, rev. 2.1, rev. 3, rev. 4, rev. 5, rev. 6 (same date). **Feeds:** a future export script under the repository `scripts/` directory (Phase 3, not authorised by this document — the file does not exist and is deliberately not named as a path)
**Related:** [`DISMECH_INTEGRATION.md`](../../../DISMECH_INTEGRATION.md) · [`DATA_SOURCES.md`](../../../DATA_SOURCES.md) · [`_external_repos/MANIFEST.md`](../../../_external_repos/MANIFEST.md)

### Revision log

Rev. 2 responds to an adversarial review of rev. 1 that returned CHANGES REQUESTED on five
blocks. All five were checked against the pinned schema and the registries; **all five held**,
and block 2 was worse than reported. Corrections are listed here rather than silently applied,
because three of them were confident assertions in rev. 1.

| # | Rev. 1 said | Verified state | Section |
|---|---|---|---|
| 1 | Accounting identity over "candidate assertions" | Mixed four different units; no precedence, no dedup rule, no state for status-excluded claims; §11.1 and §5.4 assigned two terminal states to the same claims | §5 rewritten |
| 2 | "Exactly five claims — the complete eligible universe, derived not selected" | **Withdrawn.** The join counted any paper mention. Using the registry's own declared link roles the set is *different*: CLAIM 009 links PAPER 054 as `tensions`, not support; CLAIM 030 is linked by PAPER 056 as `supplies the functional assay` and was missed. The rev. 1 "independent convergence" was an artefact of a loose join | §5.4 rewritten |
| 2b | "30 of 35 claims terminate in `ELIGIBILITY_DEBT`", "the same debt already ratcheted in the state manifest" | **Both withdrawn.** The number is not measurable before atomization, and it is a different denominator from `unread_premise_baseline: 17` and from the registry-declaration ratchet | §5.4 |
| 3 | `DATO → mechanism_confidence: ESTABLISHED`; `IPOTESI → NO_EVIDENCE`; `WRONG_STATEMENT` is "the representational home" for the 2026-07-26 figure finding; `ModifierEnum` forces a sign | All four wrong against the pinned schema. `ESTABLISHED` requires *"strong evidence from multiple independent studies"*; `NO_EVIDENCE` means the cited reference lacks relevant evidence; `WRONG_STATEMENT` is for an annotated claim that is factually wrong where the citation documents the correction; `modifier` has no `required: true` | §3.3, §8 |
| 4 | `mitochondrial_dysfunction` → NOT ESTABLISHED, on initiating-lesion incompatibility | Wrong criterion. The module explicitly invites entries to substitute the disease-specific lesion and names a downstream conformance target. Correct verdict is `UNASSESSED` | §7 |
| 5 | Decompositions in §12 were atomic | Several are not: 024-a, 035-a and 016-c each fuse two statements; 035-e is an inference typed as data; `ESTABLISHED` on 024 is unsupported. Rule 2 of §4 also contradicted the multi-`EvidenceItem` pattern | §4, §12 |

Rev. 2.1 responds to a second adversarial review, which returned CHANGES REQUESTED on four
structural problems. All four held; two were verified against the pinned schema and the
registries and are worse than reported.

| # | Rev. 2 said | Verified state | Section |
|---|---|---|---|
| 6 | Deduplication merges same-proposition/same-source assertions and assigns one terminal state | Under-specified. PAPER 055 supports CLAIM 024 (`consolidated baseline`, `primary`) **and** CLAIM 028 (`flagged for review`, `secondary`): the same evidence carries one admissible and one inadmissible lineage, and rev. 2 did not say which wins. A fifth level, `AssertionOccurrence`, is required *before* deduplication | §3.1, §5.5 |
| 7 | Eight terminal states in one precedence chain | Mixed two universes. A `tensions` link is not a reading debt; `ONTOLOGY_OR_IDENTIFIER_GAP` was ordered after a receipt test that cannot run without a source ID; `SCHEMA_LOSS` governed `PREMISE_TAG`, which is not an evidence assertion. **Internal contradiction:** §12.3 assigned 016-e to `SCHEMA_LOSS` while the precedence chain would have stopped it at `ELIGIBILITY_DEBT` for having no source. Split into two ledgers | §5.2–5.4 |
| 8 | ≥ 2 independent converging studies → `ESTABLISHED`; `in observation` → `PROVISIONAL` | Multiplicity is necessary, not sufficient; and the status→confidence mapping reintroduced exactly the claim-status/mechanism-confidence conflation rev. 2 claimed to fix. **Worse:** the pinned schema states *"If not specified, the mechanism is assumed to be established"* — omitting the field is a silent upgrade to the strongest value, defeating Rule F1 by default | §3.3, §5.1 |
| 9 | Each normalised proposition yields zero or one emitted node | False under the entry-local architecture chosen in §10: a shared proposition yields one WOREE node and one SCAR12 node. The node-side identity of §5.4 breaks. Cardinality is `0..n`, and attachments need their own count | §3.1, §5.4 |
| 9b | "at least one case" of link-direction disagreement, rate "unmeasured" | Measured: **4 of 9** paper→claim links across the three complete-read papers have no return link (054→028, 055→028, 056→030, 056→028) | §5.6, §11.2 |

Rev. 3 responds to a third adversarial review, on the artefacts rather than the argument. All
five findings held, and three were self-contradictions between this document and the sidecar it
governs.

| # | Rev. 2.1 said | Verified state | Section |
|---|---|---|---|
| 10 | `EXPORTED` — "admissible; present in the output" | **False as used.** No node has been emitted and no YAML written, so nothing is in any output. Renamed `ELIGIBLE_FOR_EXPORT`; `EXPORTED` is reserved for a Phase-3 dry run that actually writes | §5.2–5.4 |
| 11 | `LOCATOR_MISSING` covers every quote-less occurrence | Conflates two different things. A quote not yet extracted is an open task; a quote **sought in the source and not found there** is a completed negative verification. Split into `LOCATOR_NOT_EXTRACTED` and `SOURCE_SUPPORT_NOT_FOUND` | §5.2–5.3 |
| 12 | One receipt reference per occurrence | Insufficient, and the emitted values were stale: rows pointed at `-02`/`-01` while the active complete reads are `-03` and the locator extraction is `-04`. Two fields are required — `eligibility_receipt_event` and `locator_extraction_receipt_event` | §5.2 |
| 13 | Measured sections current | Stale after locator extraction: 34 events and one `queried_not_full_read` in §5.6, and §14.1 still reporting "17 `LOCATOR_MISSING`, zero exportable, three PDFs". Real state: 36 events, three `queried_not_full_read`, two sources extracted, 14 eligible | §5.6, §14 |
| 14 | §14.1 "Answered" | Contradicted the sidecar report, which correctly recorded that structural anchors and an independent second derivation were still owed. Returned to **OPEN** | §14 |

Rev. 4 responds to a fourth adversarial review, this time of the generator rather than the
documents. All four blocks held, and each was reproduced before being fixed.

| # | Rev. 3 shipped | Verified defect | Fix |
|---|---|---|---|
| 15 | `dedup_key` over `source, proposition, context, locator_status, type, relation` | The contract requires a **locator fingerprint**; the code used only the *status*. Two different quotes from one source, with the same proposition and context, produced an identical key — distinct experiments could merge | `locator_fingerprint` is now hashed into the key, and a regression test asserts distinct locators diverge while identical ones still merge |
| 16 | `CLAIM_STATUS`, `SOURCE` and `LINK` as authored constants | Eligibility was computed from constants that a registry change would silently invalidate. Only the spans were read | Claim status, PMID, both link directions, receipt depth, receipt lineage and artefact fingerprint are now **read from the registries and the ledger**; artefact bytes are re-hashed on disk and a mismatch aborts |
| 17 | `--verify` printing "byte-for-byte" | It compared parsed objects. A differently serialised JSONL passed | Split into `--verify-bytes` (exact bytes, against one declared serialisation) and `--verify-semantic` (parsed records). Verified: a reformatted file now fails the first and passes the second |
| 18 | Hash contract "recorded in the output" | It appeared only on stdout; the JSONL contained no such record | A `derivation_manifest` record is now the first line of the sidecar, carrying the hash contract, the key components and the provenance sources |
| 19 | New script not executable | The clean export failed `test_release_surface` — not the pre-existing untracked-directory failure, as rev. 3 reported | Executable bit set, matching the repository's shebang policy |

Rev. 5 responds to a fifth adversarial review, which ran the generator in a clean export rather
than the working tree. All four blocks held, and the first invalidated a claim rev. 4 had made
about its own verification.

| # | Rev. 4 shipped | Verified defect | Fix |
|---|---|---|---|
| 20 | Sidecar records carried `artefact_verification`, a hash measured on disk | **The sidecar was not reproducible in public.** A clean export has no `files/`, so the value became `artefact_absent`, the records diverged and both verify modes exited 1. An environment-dependent value had entered a deterministic artefact | The records now carry only the fingerprint **declared by the receipt**. Re-hashing local artefacts moved to a separate `--audit-local-sources` command whose result never enters a record |
| 21 | "Clean export fully green, first time in this chain" | **False, and the method was the reason.** `test_derive_dismech_sidecar.py` was not among the release runner's targets, so the suite could pass while the derivation itself failed there | The test is registered in the release runner (38 → 39 targets), and a regression invokes `--verify-bytes` on the committed sidecar |
| 22 | `read_link` returning `"declared"` for a claim-only link | Not in the role normalisation, so it became `UNMAPPED_ROLE`. Simulating a complete receipt for PAPER 019 sent both its occurrences to `LINK_ROLE_NON_SUPPORTING` — real evidence disqualified by a naming gap | Both raw roles are kept separately (`raw_link_role_paper_to_claim`, `raw_link_role_claim_to_paper`); a claim that cites a paper is a supporting citation by construction |
| 23 | Locator receipt merely located by workflow tag | Presence was checked, ancestry was not | The lineage is now **validated**: depth must be `queried_not_full_read`, `prior_receipt` must name the selected complete read, the fingerprint must match, and the outputs must name this sidecar. Any failure aborts |

Test hardening in the same revision: the serialisation tests now invoke the CLI and assert exit
codes rather than comparing strings in-process, and two tests assert that no environment-dependent
value can re-enter a record. Twenty tests, registered in the release runner.

Rev. 6 responds to a sixth adversarial review. Two findings were **fail-open** — the generator
reported success while checking nothing — which is the failure mode a verification layer must
never have.

| # | Rev. 5 shipped | Verified defect | Fix |
|---|---|---|---|
| 24 | Locator receipt validated *if present* | `read_receipts` returned `locator_event=None` without complaint. With the locator receipts removed from the ledger, all **14 occurrences stayed `ELIGIBLE_FOR_EXPORT`** carrying `locator_extraction_receipt_event: null` — a quote with no record of where it came from | New state `LOCATOR_PROVENANCE_MISSING`, ordered before `SOURCE_SUPPORT_NOT_FOUND`. An occurrence that has a locator decision but no receipt documenting the extraction can no longer be eligible. Negative test asserts it |
| 25 | `--audit-local-sources` exiting 0 on total absence | "No mismatch" was reported as success when nothing had been compared. In a clean export both artefacts were `artefact_absent` and the audit exited 0 | Three exit codes: `0` all expected artefacts verified, `1` mismatch, `2` audit incomplete because expected artefacts are absent. Clean export now exits 2 with *"absence is not a pass"* |
| 26 | Manifest claiming `"artefact_bytes": "re-hashed on disk at derivation time"` | False since rev. 5 moved the re-hash to a separate audit. `"paper_registry_current.md (both directions)"` was also wrong: the reverse direction is read from the claim registry | Manifest now names each provenance source separately and states that the fingerprint is the receipt's, not a measurement |
| 27 | `cited_by_claim` as the claim→paper role | A synthetic sentinel, and `read_link` matched `PAPER nnn` anywhere in the claim — for PAPER 019 it matched a **wikilink**, while the `Source` field names "Cheng et al. 2020" in prose | The two are now distinguished: `source_field` (the claim names the paper as a source) normalises to `SUPPORTING`; `wikilink_only` normalises to `UNQUALIFIED_REFERENCE` and is **not** supporting evidence. The `Source` field text is recorded on the occurrence so a reviewer can see what the claim actually says |

Six negative tests were added for these paths — a stripped ledger, a corrupted lineage, an absent
artefact, a bare wikilink, a Source-field reference, and the manifest's own accuracy. Twenty-six
tests, all in the release runner.

Rev. 7 is a contract realignment: rev. 6 added a ninth Ledger-A state in code without adding it
to the specification, and its audit regression tested a helper rather than the exit code that is
the actual contract.

| # | Rev. 6 shipped | Verified defect | Fix |
|---|---|---|---|
| 28 | `LOCATOR_PROVENANCE_MISSING` in the generator only | The specification still listed seven loss states, omitted the new one from the table and the precedence chain, and Rule A3 described three outcomes where there are four. Code and contract had diverged | State added to the table, the precedence chain, the accounting identity (now **eight** loss states), the eligibility gate and the exporter success criteria. Rule A3 rewritten with all four outcomes; new **Rule A4** states the provenance requirement |
| 29 | `test_audit_reports_incomplete_when_artefacts_are_absent` | It asserted `verify_artefact()` returned `artefact_absent` — never invoking `--audit-local-sources`, so a dispatcher regression would still pass | Audit extracted into `audit_local_sources()` returning `(exit_code, states, tally)`, shared by the CLI and the tests; two new regressions invoke the CLI and assert exit 2 on absence and exit 0 on a verified corpus |
| 30 | `raw_link_role_claim_to_paper: "source_field"` | `source_field` and `wikilink_only` are derived classifications, not verbatim roles recorded anywhere | Renamed to `claim_link_basis`; the raw role for that direction is `null`, because the registry declares none; `claim_source_field` keeps the verbatim text |

**Known limitation, recorded rather than fixed.** The locator lineage check validates *direct
parentage*: `prior_receipt` must name the currently selected complete read. A future receipt
correction that supersedes that event would cause a historically correct locator receipt to be
rejected. A full ancestry walk is the right answer and is not implemented; the limitation is
declared in the derivation manifest so it cannot be discovered by surprise.

Rev. 3 also replaced the sidecar's authored span labels with exact registry anchors
(`claim_registry_current.md#CLAIM {id}\|{field}\|sent[{n}]`), persists the derivation and its hash
contract, and records that the derivation re-derives byte-for-byte — reproducibility, not yet
independence.

---

## 0. Target pin

The export contract is defined against one exact upstream state. Any drift invalidates the
field mapping until re-verified.

| Item | Value |
|---|---|
| Repository | `monarch-initiative/dismech` |
| Commit | `c43343af4054eeeab847621eaab1e10da7efde84` |
| Commit date | 2026-08-04T03:58:08Z |
| Schema path | `src/dismech/schema/dismech.yaml` |
| Schema blob SHA | `e1a5bde3b0d35b23808018648a8fc267dc96b10c` |
| Schema size | 251 151 bytes / 6 690 lines |
| Licence | BSD-3-Clause (repository); ontology terms carry their own terms |
| Inspected | 2026-08-04, via the GitHub contents API; no clone retained |

**Pin discipline.** The exporter must fail closed if the schema blob SHA at run time differs
from the pinned value. A changed schema is a specification review event, not a runtime warning.

---

## 1. Scope

### 1.1 In scope for the proof of concept

| Surface | Path in DisMech | Why in scope |
|---|---|---|
| Disease entries | `kb/disorders/` | The two WWOX disease targets do not exist upstream |
| Mechanism modules | `kb/modules/` | Referenced via `Pathophysiology.conforms_to`; see §7 and §10 |

### 1.2 Explicitly deferred, not contracted

Four further `kb/` surfaces exist. Each maps onto a LEGEND layer by *apparent* subject matter.
None has a demonstrated contract, and none is exported by this specification. They are recorded
so that a later reader does not mistake omission for absence.

| Surface | Entries upstream | Apparent LEGEND counterpart | Why deferred |
|---|---:|---|---|
| `kb/groupings/` | 56 | — | Useful eventually (`GroupingBasisEnum.SHARED_MECHANISM` fits a WWOX group), unnecessary for two entries |
| `kb/hypotheses/` | 87 | [`therapeutic_hypotheses_ledger_current.md`](../research/therapeutic_hypotheses_ledger_current.md) | Directory-per-disorder workspace; structural equivalence to our ledger is asserted, not shown |
| `kb/surrogate_endpoints/` | 1 | [`biomarker_endpoint/`](../biomarker_endpoint/) | Single FDA surrogate-endpoint table; covers regulatory Tier 3 endpoints, not Tier 1/2 gene-linked biomarkers |
| `kb/comorbidities/` | 19 | — | Out of scope |

### 1.3 Out of scope entirely

- Any write to the four current files.
- Any pull request, issue, or upstream communication.
- Any use of a paid service (`/curate` defaults to a deep-research provider requiring a key).
- Any individual-level material. The private N-of-1 overlay is excluded by architecture and is
  not reachable from this pipeline.

---

## 2. The two disease targets

| Target | MONDO | Also known as | Upstream status |
|---|---|---|---|
| WOREE / DEE28 | `MONDO:0014533` | *developmental and epileptic encephalopathy, 28*; WOREE syndrome; EIEE28 | **absent** from `kb/disorders/` |
| SCAR12 | `MONDO:0013687` | *autosomal recessive spinocerebellar ataxia 12*; cerebellar ataxia-epilepsy-intellectual disability syndrome due to WWOX deficiency | **absent** from `kb/disorders/` |

Verified 2026-08-04: zero files matching `*WWOX*` in `kb/disorders/`; zero entries matching
`spinocerebellar` or `SCAR`. WWOX appears upstream only as a member gene inside umbrella
entries, and in `research/kg_gene_gap.tsv` it recurs in the `kg_only` column — present in the
Monarch KG, absent from curation.

The naming convention for gene-specific entries is empirically established by roughly thirteen
sibling files (`KCNQ2_Developmental_and_Epileptic_Encephalopathy.yaml`,
`GNAO1-Related_Developmental_and_Epileptic_Encephalopathy.yaml`, `DNM1_Encephalopathy.yaml`,
and others). `Early-Infantile_Developmental_and_Epileptic_Encephalopathy.yaml` states in its own
scope field that *"gene-specific variant spectra and natural history belong on the gene-specific
entries"* — the slot is named upstream and empty.

**No new MONDO term is required.** `kb/groupings/Childhood_Onset_Epilepsy_Syndromes.yaml` records
that a grouping *"is assembled below the level of the MONDO taxonomy to make that clinical
convention auditable"*. A MONDO umbrella class for WWOX-related disorders does not currently
exist (`total: 0` on the Monarch search API, 2026-08-04); requesting one is optional nosological
housekeeping and is a prerequisite for nothing in this specification.

---

## 3. Field mapping

### 3.1 Five units, kept separate

Rev. 1 used "assertion" for four different things; rev. 2 named four levels but merged lineage
into deduplication, losing the ability to account for an excluded lineage. Five levels are
required. Every rule below states which unit it governs.

| Unit | Definition |
|---|---|
| **Claim** | A numbered LEGEND registry entry. A dossier, not a statement. Never the unit of export |
| **Assertion occurrence** | One `(claim, source, proposition)` triple as the registries actually record it, carrying its own eligibility outcome. **The unit classified, and the unit the primary accounting identity governs** |
| **Evidence assertion** | The group of *admissible* occurrences sharing a proposition and a source. Carries `originating_claim_ids[]`. Never formed from an inadmissible occurrence |
| **Normalised proposition** | The deduplicated statement one or more evidence assertions are about |
| **Emitted node** | A `Pathophysiology` node (or `Discussion`, or `MechanisticHypothesis`) carrying one normalised proposition, on one disease entry, with *n* `EvidenceItem` attachments |

```
claim ─┬→ occurrence ─┐  (classified first)
       └→ occurrence ─┤
claim ──→ occurrence ─┴→ evidence assertion ──→ normalised proposition ─┬→ node (WOREE)
                         (admissible only)                              └→ node (SCAR12)
```

**Three record kinds.** An occurrence presupposes an atomic proposition and a single source, so a
statement that is *not yet* atomic cannot be one — `ATOMIZATION_REQUIRED` has to be reachable
before an occurrence exists. And content that is not evidence at all (a premise tag, a caveat, a
transferability tier) is never an occurrence in any state. Three record kinds are therefore
required, and together they are the sidecar schema (§12.4):

```
AssertionCandidate:            # pre-atomization; the unit ATOMIZATION_REQUIRED applies to
  candidate_id
  claim_id                     claim_status
  raw_registry_span            # verbatim registry text this candidate came from
  source_ids_observed[]        # zero, one, or many
  atomization_outcome          # ATOMIZED | ATOMIZATION_REQUIRED | NOT_EVIDENCE
  derived_occurrence_ids[]     # empty unless ATOMIZED

AssertionOccurrence:           # one (claim, source, atomic proposition) triple
  occurrence_id
  candidate_id                 claim_id            claim_status
  source_id                    link_direction      (claim→paper | paper→claim | both)
  raw_link_role                normalised_role     (raw is free text; see §5.6)
  proposition                  context
  locator                      locator_status
  epistemic_type               evidence_relation   (SUPPORT | PARTIAL | REFUTE)
  dedup_key                    evidence_assertion_id
  terminal_state               unreached_tests[]

RepresentationItem:            # Ledger B; not evidence, or evidence with an upstream loss
  item_id
  claim_id                     occurrence_id?      # present only when it accompanies one
  construct_type               # PREMISE_TAG | REVIVAL_TRIGGER | CAVEAT | TRANSFERABILITY
                               # | RECEIPT_LINEAGE | ONTOLOGY_TARGET
  content
  representation_state         # SCHEMA_LOSS | ONTOLOGY_BINDING_GAP
  mitigation                   # e.g. Discussion kind, or none
  flags[]                      # e.g. UPSTREAM_VERIFICATION_GAP
```

A candidate with `atomization_outcome: NOT_EVIDENCE` yields `RepresentationItem` records and no
occurrences. A candidate with `ATOMIZATION_REQUIRED` yields neither, and is counted as itself.

Four consequences:

- **Classify before deduplicating.** Rev. 2 merged first and assigned one state after, leaving
  undefined which lineage wins when they disagree. The live case: PAPER 055 supports CLAIM 024
  (`consolidated baseline`, role `primary`) *and* CLAIM 028 (`flagged for review`, role
  `secondary`). Under §5.5 the CLAIM 028 occurrence terminates in `STATUS_INELIGIBLE` and is
  counted there; the CLAIM 024 occurrence proceeds. The excluded lineage neither contaminates the
  export nor disappears from the ledger.
- **Many-to-one is normal.** CLAIM 016 and CLAIM 035 both assert direct WWOX inhibition of GSK3β
  from PAPER 056: two admissible occurrences, one evidence assertion, two `originating_claim_ids`.
- **One source per *occurrence*, many `EvidenceItem` per *node*.** The §4 atomicity rule binds the
  occurrence. Multi-source convergence is expressed at the node.
- **A proposition may yield more than one node.** Under the entry-local architecture (§10) a
  proposition holding for both disorders produces a WOREE node and a SCAR12 node, and one
  evidence assertion is attached to both. Node-evidence **attachments** are therefore counted
  separately from evidence assertions (§5.4).

### 3.2 Class-level correspondence

| LEGEND construct | DisMech class / slot | Notes |
|---|---|---|
| Disease model, per disorder | `Disease` | 49 slots; only a small subset is populated by this PoC |
| Normalised mechanistic proposition | `Pathophysiology` node (`name`, `description`, `role`, `biological_processes`, `mechanism_confidence`, `conforms_to`) | The workhorse |
| Evidence assertion | `EvidenceItem` (`reference`, `reference_title`, `supports`, `evidence_source`, `snippet`, `explanation`, `images`) | One per evidence assertion |
| Alternative / competing account | `MechanisticHypothesis` (`hypothesis_group_id`, `status`, `applies_to_subtypes`) | `MechanisticHypothesisStatusEnum`: CANONICAL, ALTERNATIVE, EMERGING, DEPRECATED |
| Open question, controversy, gap | `Discussion` (`kind`, `status`, `attaches_to`, `proposed_experiments`) | `DiscussionKindEnum`: OPEN_QUESTION, KNOWLEDGE_GAP, CONTROVERSY, CURATION_TODO, EMERGING_HYPOTHESIS, INTERPRETATION, HUMAN_MODEL_MISMATCH |
| Discriminating experiment | `Discussion.proposed_experiments` → `decision_criterion`, `would_support`, `would_refute` | See §9 |
| Shared WWOX mechanism | `kb/modules/` file + `Pathophysiology.conforms_to: "module#Node Name"` | See §7 |

### 3.3 Epistemic mapping — corrected

Rev. 1 mapped LEGEND's four levels onto `mechanism_confidence` as if they were the same axis.
They are not. **`supports` is a property of an evidence assertion; `mechanism_confidence` is a
property of the mechanism the node asserts.** A single direct observation can be unimpeachable
`DATO` and still support a disease mechanism only provisionally.

Verified enum semantics from the pinned schema:

```
ESTABLISHED  : "Well-established mechanism with strong evidence from multiple independent studies"
PROVISIONAL  : "Provisional mechanism under active investigation with emerging but incomplete evidence"
HYPOTHETICAL : "Hypothetical mechanism with limited or indirect evidence; plausible but not yet validated"

SUPPORT         : "The cited evidence directly supports the claim"
PARTIAL         : "The cited evidence partially or indirectly supports the claim"
REFUTE          : "The cited evidence directly contradicts the claim"
NO_EVIDENCE     : "The cited reference does not contain evidence relevant to the claim"
WRONG_STATEMENT : "The annotated claim contains a demonstrable factual error […]; the cited
                   evidence documents the correct information. Use this when the claim is
                   outright wrong, not merely contested."
```

**Axis 1 — evidence assertion → `supports`:**

| LEGEND type of the assertion | `supports` |
|---|---|
| `DATO`, source states the proposition directly | `SUPPORT` |
| `DATO`, source states it indirectly or in part | `PARTIAL` |
| `INFERENZA` | `PARTIAL`; the inferential step is stated in `explanation` |
| `IPOTESI` | Not an evidence assertion. Route to `MechanisticHypothesis` (`status: EMERGING`) or `Discussion` |
| `ESPANSIONE` | Not exportable as evidence. Route to `Discussion` (`kind: INTERPRETATION`) or withhold |

`NO_EVIDENCE` is **not** a marker for hypotheses. It describes a citation that does not bear on
the claim, and the exporter never has a reason to emit it.

**Axis 2 — normalised proposition → `mechanism_confidence`.** This is a **curatorial judgement,
not a computation.** Rev. 2 made it a lookup on study count; multiplicity is *necessary but not
sufficient* for the schema's "strong evidence from multiple independent studies".

`ESTABLISHED` may be proposed only when **all six** hold, and the proposal is recorded with its
justification for human review:

1. ≥ 2 studies, each with a complete-read receipt;
2. genuinely independent (not the same group, cohort, construct or reagent lineage);
3. each bears on **this exact proposition**, not on a neighbouring one;
4. directness and quality adequate for the proposition's scope (an in-vitro fragment result does
   not establish a disease mechanism);
5. contexts comparable under §8 Rule C1;
6. no substantial contrary evidence, including registry-declared tensioning links.

Fail any → `PROVISIONAL`. Indirect or model-only evidence for a proposition about human disease →
`HYPOTHETICAL`. **Default when uncertain: `PROVISIONAL`.**

**Rule E1.** No single-source proposition is `ESTABLISHED`, regardless of source strength or claim
status. This disqualifies rev. 1's treatment of CLAIM 024.

**Rule E2 — mandatory explicit emission.** The pinned schema declares:

> `mechanism_confidence` — *"Level of confidence in this pathophysiology mechanism.
> **If not specified, the mechanism is assumed to be established.**"*

Omission is therefore not a neutral absence: it is a silent upgrade to the strongest value, and
it defeats Rule F1 by default rather than by action — the most dangerous shape a flattening can
take, because nothing in the output shows it happened. **Every emitted `Pathophysiology` node
MUST carry an explicit `mechanism_confidence`. Omission fails closed**, and is covered by a
regression test under Rule F4.

**Rule E3 — claim status is not confidence.** LEGEND claim status governs *eligibility* (§5.1).
It never determines `mechanism_confidence`, which is assessed per proposition on the six criteria
above. Rev. 2's "`in observation` maps onto `PROVISIONAL`" reintroduced the very conflation it
claimed to remove, and is withdrawn.

### 3.4 The 2026-07-26 figure finding — downgraded to an open pattern

Rev. 1 asserted that `WRONG_STATEMENT` was "the representational home" for a paper whose text and
supplementary legend both assert an absence its figure does not show. **That was an over-read.**
The enum describes an *annotated claim* that is factually wrong where the *cited evidence
documents the correction* — a curation-annotation relation, not a paper-internal text/figure
mismatch. The schema explicitly reserves `REFUTE` for contradiction short of factual error, and
`NO_EVIDENCE` for irrelevance.

The finding may still be modellable — as an evidence assertion whose `explanation` records the
discrepancy, or as a `Discussion` of `kind: CONTROVERSY` — but no pattern is established, the
PoC does not attempt it, and §14 carries it as an open question for upstream discussion.

### 3.5 Constructs with no DisMech representation

| LEGEND construct | Disposition |
|---|---|
| `PREMISE_TAG` (incl. `PREMISE: DEFAULT_FROM_TEXTBOOK`) | `SCHEMA_LOSS`. Partial mitigation: restate the premise as a `Discussion` of `kind: KNOWLEDGE_GAP` with `status: OPEN` |
| `REVIVAL_TRIGGER` | `SCHEMA_LOSS`. Partial mitigation: `Discussion.proposed_experiments` where the trigger is an experiment; otherwise withheld |
| Dismissal ledger entries | Not exported. Rejections are internal epistemic hygiene, not curated disease knowledge |
| Transferability tier (T1–T4) | `SCHEMA_LOSS`. Approximate via `EvidenceSourceEnum` + explicit `genetic_context`; the approximation must be recorded, never silently substituted |
| Full-text read receipt ID | `SCHEMA_LOSS` upstream, but **retained in the exporter's own report** for every evidence assertion |

`SCHEMA_LOSS` does not mean the content is wrong or discarded. It means LEGEND holds something
the target vocabulary cannot say. Each entry is a candidate upstream contribution.

---

## 4. Atomization rules

These govern the **evidence assertion** (§3.1). An evidence assertion is the smallest statement
satisfying all of:

1. **One epistemic type.** If the sentence needs two of `DATO` / `INFERENZA` / `IPOTESI` /
   `ESPANSIONE` to be described honestly, it is not atomic.
2. **One source.** Multi-source convergence is expressed at the node, not inside the assertion
   (§3.1).
3. **One experimental context.** Species, system, allele state and stimulus are fixed. A murine
   full-KO observation and a human clinical inference are two assertions, always.
4. **One proposition.** A statement that fuses a structural fact with a functional consequence,
   or a region with a residue requirement, is two assertions. Conjunctions are the diagnostic:
   *and*, *while*, *thereby*.
5. **One causal direction.** If the direction is context-dependent, see §8.
6. **A verifiable locator.** A verbatim `snippet` attributable to the cited reference at a
   recorded position.

**Rule A1 — no creative interpretation.** Atomization may only *split* existing registry text and
re-attribute it. It may not merge, generalise, strengthen, or supply a missing premise. If an
atomic statement cannot be produced from the registry text as written, the outcome is
`ATOMIZATION_REQUIRED`, and resolution is a human curation task, not an exporter behaviour.

**Rule A2 — the caveat travels with the statement.** Where the registry attaches a warning to a
finding (a measurement caveat, a non-transferability note, a bounded scope), that warning is part
of the assertion and must appear in the node `description` or the evidence `explanation`. An
assertion exported without its caveat is a mis-export, not a partial export.

**Rule A3 — a locator is a separate test from a receipt, and has four outcomes.** A complete-read
receipt attests that a document was read in full. It does not attest that a verbatim quote
supporting a given proposition has been extracted and recorded. Rule 6 is evaluated
independently:

| Outcome | State |
|---|---|
| No extraction attempted yet | `LOCATOR_NOT_EXTRACTED` — an open task |
| Extraction happened, but no receipt in the ledger documents it | `LOCATOR_PROVENANCE_MISSING` |
| Extraction happened; the source contains no supporting statement | `SOURCE_SUPPORT_NOT_FOUND` — a completed negative verification, not a debt anyone can discharge by working harder |
| Verbatim quote extracted and its extraction receipted | passes |

**Rule A4 — a quote must carry its own provenance.** An occurrence that records a locator
decision without a locator-extraction receipt is never eligible, however strong its evidence. The
receipt must declare `evidence_depth: queried_not_full_read`, name the selected complete read in
`prior_receipt`, carry the same source fingerprint, and name this sidecar among its outputs.

---

## 5. Eligibility gate, terminal states, accounting

### 5.1 The gate, over assertion occurrences

```
OCCURRENCE_ADMISSIBLE =
      originating claim status ∈ { consolidated baseline, in observation }
  AND atomic under §4
  AND source resolves to a paper-registry entry with a usable identifier
  AND that source carries evidence_depth = complete_fulltext_read in the receipt ledger
  AND the registry-declared link role is supporting for this claim (§5.6)
  AND a verbatim quote/locator exists and is recorded
  AND a locator-extraction receipt documents that extraction (Rule A4)
  AND disease/model context is preserved on the emitted node
```

Claim status governs eligibility only. It does not set `mechanism_confidence` (Rule E3).

### 5.2 Two ledgers

Rev. 2 ran one precedence chain over states belonging to two different universes, and
contradicted itself: §12.3 assigned 016-e (a premise with no source) to `SCHEMA_LOSS`, while the
chain would have stopped it at `ELIGIBILITY_DEBT`. The two are now separated.

**Ledger A — evidence accounting.** Governs assertion occurrences. Exactly one state each.
Every occurrence carries **two** receipt lineages: `eligibility_receipt_event`, the complete read
that made the source admissible, and `locator_extraction_receipt_event`, the targeted pass that
produced or failed to produce its quote. They are different events and must not be conflated.

| State | Meaning |
|---|---|
| `ELIGIBLE_FOR_EXPORT` | Passes every gate. **Not yet in any output**: no node has been emitted, so nothing is `EXPORTED` until a Phase-3 dry run writes one |
| `STATUS_INELIGIBLE` | Claim is `conflicting evidence`, `flagged for review`, `background only` or `archived` |
| `ATOMIZATION_REQUIRED` | Composite statement not separable without interpretation (Rule A1) |
| `IDENTIFIER_UNRESOLVED` | No usable source identifier; nothing downstream is evaluable |
| `ELIGIBILITY_DEBT` | Source identified, receipt absent or below `complete_fulltext_read` |
| `LINK_ROLE_NON_SUPPORTING` | Source is linked to this claim in a tensioning or counter-directional role |
| `LOCATOR_NOT_EXTRACTED` | Receipt adequate; no verbatim quote has been extracted yet for this proposition (Rule A3). An open task |
| `LOCATOR_PROVENANCE_MISSING` | A locator decision was made — a quote found, or support sought and not found — but no receipt in the ledger documents that extraction. A quote with no record of where it came from |
| `SOURCE_SUPPORT_NOT_FOUND` | Extraction was performed and the source contains **no statement supporting this proposition**. A completed negative verification, not a task |

`LINK_ROLE_NON_SUPPORTING` is a state of its own because a tensioning link is **not a reading
debt**. It is valid evidence in a different direction, and its onward routes are a separate node,
a `REFUTE` where §8 Rule C1 permits, or a `Discussion` — not a loss to be resolved by more
reading. CLAIM 009 / PAPER 054 is the live case.

**Ledger B — representation-loss accounting.** Governs LEGEND content that is not an evidence
occurrence, or that survived Ledger A but cannot be fully expressed upstream. Content may appear
in Ledger B *in addition to* being `ELIGIBLE_FOR_EXPORT` in Ledger A.

| State | Meaning |
|---|---|
| `SCHEMA_LOSS` | LEGEND construct with no DisMech representation — `PREMISE_TAG`, `REVIVAL_TRIGGER`, transferability tier, receipt ID (§3.5) |
| `ONTOLOGY_BINDING_GAP` | Missing or ambiguous MONDO / HP / GO / MAXO / NCIT target |
| `UPSTREAM_VERIFICATION_GAP` | **A flag, not a terminal state.** The locator exists and the content is representable, but upstream CI cannot verify it (figure, Methods, supplementary). It may accompany `ELIGIBLE_FOR_EXPORT` |

016-e — the `PREMISE: DEFAULT_FROM_TEXTBOOK` on CLAIM 016 — belongs to Ledger B only. It has no
source and no locator by construction and is never an occurrence, so Ledger A never sees it.

### 5.3 Precedence within Ledger A

An occurrence may fail several tests. It receives exactly one state, by this order:

```
1. STATUS_INELIGIBLE           — claim-level, cheapest
2. ATOMIZATION_REQUIRED        — until atomic, later tests are not well defined
3. IDENTIFIER_UNRESOLVED       — without a source ID no receipt test can run
4. ELIGIBILITY_DEBT            — receipt adequacy
5. LINK_ROLE_NON_SUPPORTING    — declared role of this source for this claim
6. LOCATOR_NOT_EXTRACTED       — quote extraction not yet performed
7. LOCATOR_PROVENANCE_MISSING  — extraction happened, no receipt documents it
8. SOURCE_SUPPORT_NOT_FOUND    — extraction performed, source does not support the proposition
9. ELIGIBLE_FOR_EXPORT
```

Rev. 2 ordered the binding test after the receipt test, which cannot run without an identifier;
corrected at step 3. The report records the terminal state **and** every test not reached, so
that resolving one blocker never implies the occurrence is now exportable.

### 5.4 The accounting identities

**Primary — Ledger A, over occurrences:**

```
occurrences enumerated  ==  ELIGIBLE_FOR_EXPORT  +  Σ(the eight Ledger-A loss states)
```

**Secondary — attachments, so deduplication and multi-entry emission stay auditable:**

```
node-evidence attachments emitted  ==  Σ over emitted nodes of (EvidenceItem count)
```

Attachments are counted separately from evidence assertions, and the two numbers are **not
expected to match**: one evidence assertion attaches to as many nodes as carry its proposition,
which under the entry-local architecture is up to one per disease entry. Rev. 2 equated them and
would have failed closed on correct output.

**Tertiary — Ledger B:** every representation loss is enumerated with the construct it belongs to
and, where applicable, the `ELIGIBLE_FOR_EXPORT` occurrence it accompanies.

The exporter asserts all three and fails closed on any violation. This is the *lossless* rule of
[`CLAUDE.md`](../../../CLAUDE.md) applied to export: a loss report that omits a loss is a
corrupted artefact, not a shorter one.

### 5.5 Deduplication — after classification, never before

Only **admissible** occurrences are grouped, and only on a full key. Grouping on
`proposition + source` alone — as rev. 2.1 first specified — merges distinct experimental supports:
one paper commonly reports the same proposition in more than one system, and merging a `SUPPORT`
with a `PARTIAL` silently strengthens the weaker one.

```
dedup_key = hash( source_id
                | normalised_proposition
                | context_fingerprint
                | locator_fingerprint
                | epistemic_type
                | evidence_relation )
```

`claim_id` is **lineage, not key**: it is collected into `originating_claim_ids` and never
participates in the grouping. Two occurrences with an identical `dedup_key` form one evidence
assertion. Inadmissible occurrences are never merged; they remain individually counted under their
own Ledger-A state.

Two live cases:

- **Merge.** CLAIM 016 and CLAIM 035 both assert direct WWOX→GSK3β inhibition from PAPER 056.
  Two admissible occurrences → one evidence assertion, two `originating_claim_ids`.
- **Split.** PAPER 055 → CLAIM 024 (`consolidated baseline`, role `primary`) and PAPER 055 →
  CLAIM 028 (`flagged for review`, role `secondary`) concern the same evidence. The CLAIM 028
  occurrence terminates in `STATUS_INELIGIBLE` and is counted there. Rev. 2 would have merged
  them and had no rule for which lineage governed the result.

---

## 5.6 What the gate admits — measured state, and what is not yet measurable

Receipt ledger (`fulltext_read_receipts.jsonl`, 36 chained events, tail anchored,
`fulltext_receipts.py verify` → OK):

| `evidence_depth` | Events | Distinct studies |
|---|---:|---:|
| `complete_fulltext_read` | 9 | **4** |
| `partial_fulltext_read` | 22 | 22 (all `legacy_reconstruction`) |
| `queried_not_full_read` | 3 | 3 |
| `abstract_only` | 1 | 1 |
| `retrieved_not_read` | 1 | 1 |

The four studies with a complete read, and their **declared link roles** as recorded in the paper
registry:

| PMID | Paper | Declared claim links |
|---|---|---|
| 22193544 | PAPER 056 | `035 (new)` · `016 (enriches)` · `030 (supplies the functional assay)` · `028 (supports)` |
| 34214506 | PAPER 054 | `034 (new)` · `028 (supports)` · **`009 (tensions)`** |
| 35716775 | PAPER 055 | `024 (primary)` · `028 (secondary)` |
| 21212533 | **not mapped** | — (orphan receipt, §11.2) |

**Rev. 1's central result is withdrawn.** It reported "exactly five claims — 009, 016, 024, 034,
035 — the complete eligible universe, derived rather than selected", and treated its agreement
with an independently reached shortlist as mutual validation. The join behind it counted *any*
mention of a paper inside a claim, ignoring the role the registry declares. Reading the roles:

- **CLAIM 009 is out.** PAPER 054 is linked as `tensions` — it is the counter-directional
  evidence *against* the mitochondrial inference, not support for it. Exporting it as support
  would invert the registry's meaning.
- **CLAIM 030 is in, and was missed.** PAPER 056 declares it `supplies the functional assay`.
- **CLAIM 028 is linked by all three papers** but is `flagged for review` → `STATUS_INELIGIBLE`.

Stated precisely, because rev. 2 was still loose: **six** claims are linked to a complete-read
paper in a role *interpreted* as supporting — 016, 024, 028, 030, 034, 035 — of which **five are
status-admissible**, CLAIM 028 being `flagged for review`. The agreement rev. 1 celebrated was an
artefact: the two methods produced different sets and only appeared to agree because neither had
been checked against the declared roles.

**Link roles are free text, not a controlled vocabulary.** The observed values across three papers
are `new`, `primary`, `secondary`, `enriches`, `supports`, `supplies the functional assay`,
`tensions`. Nothing constrains them. The sidecar therefore stores `raw_link_role` verbatim and a
separately derived `normalised_role`, and the normalisation mapping is itself reviewable content —
never inferred silently at export time. Rev. 2 spoke of "the registry's declared roles" as though
they were an enum.

**Link-direction disagreement, now measured.** Rev. 2 reported "at least one case" and called the
rate unmeasured. Across the three complete-read papers there are 9 paper→claim links, and
**4 have no return link** from the claim:

| Link | Claim status | Return link |
|---|---|---|
| PAPER 054 → CLAIM 028 | flagged for review | **absent** |
| PAPER 055 → CLAIM 028 | flagged for review | **absent** |
| PAPER 056 → CLAIM 028 | flagged for review | **absent** |
| PAPER 056 → CLAIM 030 | in observation | **absent** |

Three of the four converge on CLAIM 028, which suggests a single unresolved reconciliation rather
than diffuse drift — but that is a hypothesis, and the rate across the full 46-paper registry
remains unmeasured. The exporter must traverse both directions and record every disagreement as a
reconciliation item, never silently pick one.

**Two numbers from rev. 1 are withdrawn and not replaced:**

- *"30 of 35 claims terminate in `ELIGIBILITY_DEBT`."* Not measurable. Terminal states apply to
  evidence assertions, and atomization has not been performed on 32 of 35 claims. A claim-level
  count is a category error, and it also contradicted §11.1's statement that every composite
  claim terminates in `ATOMIZATION_REQUIRED` — the same claims cannot hold two terminal states.
- *"the same debt already ratcheted in the state manifest."* False equivalence. The manifest
  tracks `unread_premise_baseline: 17` and a separate registry-declaration ratchet. Those have
  different denominators and different meanings from any export-eligibility count. The export
  report will produce its own number, named as its own thing.

**What is safe to say today:** five status-admissible claims are linked to a complete-read paper in a
role interpreted as supporting (six before the status filter). Whether any of them contains an exportable evidence assertion is determined by §4 and §5,
and is answered by the Phase 2 sidecar (§12.4), not before.

---

## 6. The anti-flattening rule

A well-typed target schema exerts constant pressure toward tidiness. Rev. 1 drifted the same way
five times: a claim-level gate that would have exported `INFERENZA` as `DATO`; a `SUPPORT`/
`REFUTE` framing that LEGEND's own protocol had refused; a module conformity assumed from a file
name; three enum values read as stronger than their definitions; and a join that dropped the
distinction between supporting and tensioning evidence. Every drift moved toward the schema and
away from the registry. None was carelessness — each epistemic caveat is a field that does not
fill in neatly.

**Rule F1.** No exported assertion may carry a stronger epistemic type, a more definite causal
direction, or a higher `mechanism_confidence` than its registry source supports. The exporter
computes both values and fails closed on any upgrade.

**Rule F2.** Absence of a warning in the output where the registry carries one is a violation of
F1, not a formatting difference.

**Rule F3.** A registry-declared link role (`tensions`, `enriches`, `supports`, `primary`,
`secondary`) is part of the evidence, not metadata. Re-labelling a tensioning link as support is
an F1 violation.

**Rule F4.** F1–F3 are machine-checkable, not matters of judgement, and must be covered by
regression tests before the exporter is trusted.

Upstream holds the same line independently: `kb/modules/mitochondrial_dysfunction.yaml` records
that it *"deliberately does NOT adjudicate the contested mitochondrial free-radical theory of
aging (…) such claims belong on the relevant disorder entry."*

---

## 7. Module conformity matrix

`Pathophysiology.conforms_to` takes a `module#Node Name` reference. Conformance is therefore a
semantic claim about **one node**, not about a module as a whole, and not a topical resemblance
between file names.

**Rule M1.** No `conforms_to` may be emitted until the target node has been read and the
conformance assessed. An unassessed module is `UNASSESSED`, never a default match.

**Rule M2 — assess the node, not the module's framing.** A module may declare a canonical chain
drawn from one disease context while explicitly inviting others to substitute their own
initiating lesion. Rejecting a node because the module's *framing* differs is the wrong test.
The tests are: does the node's proposition hold in WWOX biology, and does an evidence assertion
passing §5 support it?

| Candidate module | Assessed | Verdict | Basis |
|---|---|---|---|
| `mitochondrial_dysfunction` | partially, 2026-08-04 | **`UNASSESSED`** | Rev. 1 marked this NOT ESTABLISHED because the module's initiating lesion is somatic mtDNA accumulation with age, absent in a germline neurodevelopmental disorder. **That was the wrong test (Rule M2):** the module's own notes state that entries conform *"substituting the disease-specific lesion (e.g. … secondary mitochondrial injury in neurodegeneration and metabolic disease) while preserving the conserved chain"*, and name `#Bioenergetic Decline and Oxidative Stress` as the key conformance target. The correct blocker is different and narrower: no WWOX evidence assertion currently passes §5 for that node — CLAIM 009 is an `INFERENZA` whose only complete-read link is a `tensions` link (§5.6) |
| `disabled_macroautophagy` | no | `UNASSESSED` | Candidate for the turnover / CMA line |
| `epilepsy_excitation_inhibition_imbalance` | no | `UNASSESSED` | Candidate for pathway P2 |
| `excitatory_synapse_scaffold_disruption` | no | `UNASSESSED` | Candidate for pathway P1 |
| `cerebellar_purkinje_degeneration` | no | `UNASSESSED` | Candidate for the SCAR12 entry |
| `antisense_oligonucleotide_therapy` | no | `UNASSESSED` | Candidate for the splice-correction line; `AsoMechanismEnum` includes `SPLICE_MODULATION_EXON_INCLUSION` and `SPLICE_MODULATION_EXON_SKIPPING` |

**No conformity has been established** — which is not the same as no module being conformant. The
distinction that matters: *not yet supported by eligible evidence* is a different verdict from
*incompatible*, and only the first is true here.

---

## 8. Comparability gate for SUPPORT / REFUTE

Two LEGEND findings may point in opposite directions without being a contradiction. CLAIM 009
(deficiency → oxidative/bioenergetic stress, `INFERENZA`) and CLAIM 034 (acute knockdown in a
stressed WWOX-wild-type photoreceptor system reduces superoxide, `DATO + ESPANSIONE`) are the
worked case. The registry states that CLAIM 009 does **not** rise to `conflicting evidence`
because *"il protocollo riserva quello stato a studi comparabili, e questi non lo sono"*, and the
paper registry encodes the same judgement as the link role `009 (tensions)`.

**Rule C1.** Two assertions may be placed as `SUPPORT` and `REFUTE` on the same node only if all
four hold:

1. same biological entity state (germline loss vs. acute knockdown are different states);
2. same or defensibly homologous system and cell type;
3. same measured endpoint;
4. same direction of perturbation.

Fail any → the assertions are exported as **separate contextualised nodes**, and their tension is
recorded as a `Discussion` of `kind: CONTROVERSY` or `KNOWLEDGE_GAP`, never as `REFUTE`.

Applying C1 to 009 / 034: fails (1), (2) and (4). Disposition: separate nodes plus one
`Discussion`. The `ESPANSIONE` component of CLAIM 034 — any transfer to WWOX-DEE — is not
exportable as evidence under §3.3 and is withheld or routed to the same `Discussion`.

**Sign discipline (corrected).** Rev. 1 stated that `ModifierEnum` forces a sign on every
`biological_processes` entry. It does not: the pinned schema declares `modifier` with
`range: ModifierEnum` and **no** `required: true`. The constraint is therefore ours, not the
schema's, and it must be stated as such:

**Rule C2.** Where LEGEND's evidence does not establish a context-independent direction, the
exporter omits `modifier` rather than choosing one. Omission is the honest encoding of an
undetermined sign; picking a direction to fill the field is an F1 violation.

---

## 9. What DisMech has that LEGEND does not

The mapping runs in both directions. Two upstream constructs have no systematically populated
LEGEND counterpart, and both are worth adopting inward regardless of whether an export ever ships.

| Upstream construct | LEGEND state | Finding |
|---|---|---|
| `Discussion.proposed_experiments` → `decision_criterion`, `would_support`, `would_refute` | `next_decisive_experiment_or_decision` is declared at [`LEGEND_CORE.md:47`](../../../framework/instruction/LEGEND_CORE.md) and appears **0 times in 35 claims** | A core field never instantiated. "The discriminating experiments that separate them" is a declared mission objective with no structured form |
| `DiscussionKindEnum.HUMAN_MODEL_MISMATCH` | Present only implicitly, inside transferability prose and genotype caveats | No controlled category. For WWOX the human-vs-murine divergence is a live question, not an edge case |

Neither depends on DisMech accepting anything. Both are zero-cost relative to the export.

---

## 10. Architecture — recommendation

```
kb/disorders/WWOX-Related_Developmental_and_Epileptic_Encephalopathy.yaml   MONDO:0014533
kb/disorders/<SCAR12 entry>.yaml                                            MONDO:0013687
```

**Recommendation: (b) entry-local nodes, no shared module, for the PoC.**

Rationale: a module asserting a mechanism shared between WOREE and SCAR12 requires at least one
normalised proposition that (i) is supported by an evidence assertion passing §5, (ii) holds for
both disorders without weakening, and (iii) is not already covered by an existing module. **No
proposition currently meets all three** — five claims are linked to a complete-read paper in a
supporting role (§5.6), none has been atomized, and no module is conformant (§7). Authoring
`wwox_loss_of_function` now would assert a shared mechanism the evidence does not yet support:
precisely the flattening Rule F1 forbids.

Promotion path to **(c) hybrid** — a thin shared module plus entry-local specifics — opens when
condition (i)–(iii) is met by at least one proposition, with context and lineage preserved. Full
standalone **(a)** is not proposed. The schema route stays available
(`GroupingBasisEnum.SHARED_MECHANISM`; precedent modules referenced by existing entries include
`ciliopathy_dysfunction`, `fibrotic_response`, `telomere_attrition`).

---

## 11. Claim inventory

35 claims. Status distribution: 19 `consolidated baseline`, 13 `in observation`,
1 `conflicting evidence`, 1 `background only`, 1 `flagged for review`.

### 11.1 Claims with a composite `Type` field

Composite = the `Type` field names more than one epistemic level. **These are claims, not
assertions, and therefore carry no terminal state.** Each is a claim whose atomization is known
in advance to be non-trivial.

| Claim | Status | `Type` as written |
|---|---|---|
| 002 | consolidated baseline | `DATO + INFERENZA prudente` |
| 006 | consolidated baseline | `DATO + INFERENZA prudente` |
| 016 | in observation | `DATO (abbondanza, murino) + DATO meccanicistico (biochimica) + INFERENZA prudente` |
| 019 | consolidated baseline | `DATO (endpoint funzionale) + IPOTESI` |
| 025 | in observation | `DATO + INFERENZA` |
| 026 | in observation | `DATO + INFERENZA` |
| 029 | in observation | `DATO + INFERENZA prudente` |
| 030 | in observation | `DATO (serie allelica) + INFERENZA (la regola)` |
| 031 | in observation | `DATO (osservazione clinica) + INFERENZA (degli autori)` |
| 033 | in observation | `DATO (statistica di coorte) + IPOTESI` |
| 034 | in observation | `DATO (sistema fotorecettoriale) + ESPANSIONE` |
| 035 | in observation | `DATO (biochimica) + INFERENZA (trasferimento)` |

CLAIM 002 and CLAIM 006 are the load-bearing evidence for §3.1: both are `consolidated baseline`,
and a status-only gate exports their inferential component as data.

**12 is a floor, not a count.** §12.1 shows CLAIM 024 — whose `Type` reads `DATO` alone —
decomposing into five occurrences, one of them an inference. So the `Type` field undercounts in
**at least one** case. Rev. 2 called this systematic on a single example; whether it generalises
is unknown until the sidecar atomizes more than three claims.

### 11.2 Other observations

- Six claims (010, 022, 023, 025, 027, 028) cite no paper-registry entry at all.
- PMID 21212533 carries a complete read receipt and resolves to no paper-registry entry. This
  **orphan receipt** is out of scope for the export and in scope for registry reconciliation.
- Among the three complete-read papers, 4 of 9 paper→claim links have no return link (§5.6);
  three involve CLAIM 028. The rate across the full 46-paper registry is unmeasured.
- 46 papers are in the paper registry; 26 distinct studies appear in the receipt ledger.

---

## 12. Worked decompositions

Illustrative, and **not yet validated**. Rev. 1 presented these as atomic; several were not.
They are corrected below and remain proposals for the Phase 2 sidecar (§12.4).

### 12.1 CLAIM 024

`consolidated baseline` · `Type: DATO` · PAPER 055 (PMID 35716775, complete receipt, role
`024 (primary)`). System: purified human WWOX WW fragments plus synthetic ErbB4 peptides. **No
full-length WWOX, no pathogenic variant, no cell, no animal.**

| # | Evidence assertion | Type |
|---|---|---|
| 024-a1 | WW2 is not a canonical standalone PPxY-binding domain | `DATO` |
| 024-a2 | WW2 pre-orders and stabilises an otherwise unstable WW1 | `DATO` |
| 024-b | WW2 can directly engage a second PPxY motif when sequence, spacing, linker and orientation create a compatible topology | `DATO` |
| 024-c | The largest direct WW2 effect is obtained with engineered short-linker tandem peptides; native ErbB4 PY1PY2 gains affinity but remains predominantly WW1-bound | `DATO` (bounding condition) — **travels with 024-b** under Rule A2 |
| 024-d | WW-domain variants should not be interpreted domain-by-domain in isolation | `INFERENZA` |

Rev. 1 fused a1 and a2 into one assertion (violating §4 rule 4) and proposed
`mechanism_confidence: ESTABLISHED`. Both corrected: the propositions split, and confidence is
**`PROVISIONAL` at most** — a single in-vitro fragment study cannot meet the schema's
"multiple independent studies" bar (Rule E1).

### 12.2 CLAIM 035

`in observation` · PAPER 056 (PMID 22193544, complete receipt, role `035 (new)`).

| # | Evidence assertion | Type |
|---|---|---|
| 035-a1 | WWOX binds GSK3β through the ADH/SDR domain | `DATO` |
| 035-a2 | The binding segment is residues 388–407, homologous to the Axin/FRAT/GSKIP docking motif | `DATO` |
| 035-a3 | L404 is strictly required for the interaction | `DATO` |
| 035-b | Binding blocks Tau phosphorylation at S396/S404 but not at the MKK4 site S422 | `DATO` |
| 035-c | The interaction is detectable between endogenous proteins in mouse brain | `DATO` (`evidence_source: MODEL_ORGANISM`) |
| 035-d | Inhibition occurs with phospho-GSK3β-S9 unchanged | `DATO` |
| 035-e1 | Tau knockdown abolishes the effect; WWOX and siRNA-GSK3β are non-additive | `DATO` |
| 035-e2 | Therefore WWOX, GSK3β and Tau lie on one linear pathway with Tau as effector | `INFERENZA` |
| 035-f | Any WWOX-DEE study using pS9 as a readout of GSK3β activity will produce a false negative | `INFERENZA` |
| 035-g | Transfer to human neurons and to WWOX-DEE | `INFERENZA` — no WWOX-DEE allele was tested; that statement travels with it (Rule A2) |

Rev. 1 fused a1–a3 and typed e as `DATO`. The epistasis *observations* are data; the linear-pathway
*reading* is an inference, and separating them is the difference between exporting a result and
exporting an interpretation.

### 12.3 CLAIM 016

`in observation` · two sources, only PAPER 056 with a complete receipt (role `016 (enriches)`).

| # | Evidence assertion | Type | Source | Terminal state |
|---|---|---|---|---|
| 016-a | In Wwox-null mice, GSK3β is elevated in cortex, hippocampus and cerebellum | `DATO` | PAPER 019 | `ELIGIBILITY_DEBT` |
| 016-b | Lithium significantly suppresses PTZ-induced seizure susceptibility in that model | `DATO` | PAPER 019 | `ELIGIBILITY_DEBT` |
| 016-c1 | WWOX is a direct physical inhibitor of GSK3β | `DATO` | PAPER 056 | **duplicate of 035-a1** → merged under §5.5, one node, two `originating_claim_ids` |
| 016-c2 | Therefore loss of WWOX de-represses GSK3β rather than merely raising its level | `INFERENZA` | PAPER 056 | candidate, `PARTIAL` |
| 016-d | GSK3β acts as an amplifier of an already vulnerable system rather than a standalone upstream driver | `INFERENZA` | both | **`ATOMIZATION_REQUIRED`** — rests on two sources and cannot be split without interpretation, so it never becomes an occurrence. Rev. 2.1 gave it `ELIGIBILITY_DEBT` with `source: both`, violating the one-source definition of an occurrence; that contradiction is what forced the `AssertionCandidate` record |
| 016-e | Load-bearing premise: *protein abundance reports kinase activity*. `PREMISE: DEFAULT_FROM_TEXTBOOK`; abundance and activity are dissociable in this system | premise | — | **Ledger B only** — `SCHEMA_LOSS`, mitigated as `Discussion`, `kind: KNOWLEDGE_GAP`, `status: OPEN`. Not an occurrence: no source, no locator by construction, so Ledger A never sees it |
| 016-f | Not clinically transferable to the reference genotype at present | caveat | — | travels with 016-d (Rule A2) |

Rev. 1 fused c1 and c2 — exporting the datum and the de-repression inference as one statement —
and handled the 035 overlap as a note rather than a rule. Rev. 2 assigned 016-e a Ledger-A state
its own precedence chain would never have reached; that contradiction is what forced the two-ledger
split of §5.2.

CLAIM 016 remains the specification's proof of value: a claim-level gate would export seven
heterogeneous statements — two in eligibility debt, one duplicate, three inferences, one textbook
premise and one clinical caveat — as a single mechanistic assertion.

### 12.4 Phase 2 deliverable: a sidecar, not a registry change

The sub-assertion structure above is a genuine improvement to LEGEND and is independent of
DisMech. It must **not** be applied to the canonical claim registry yet.

Phase 2 produces a **non-canonical sidecar manifest** under this `analysis/` directory covering
CLAIM 016, 024 and 035 only. A single file holds all three record kinds of §3.1, discriminated by
`record_kind: assertion_candidate | assertion_occurrence | representation_item`, so that both
ledgers are auditable from one artefact — an occurrence-only sidecar could not represent Ledger B
at all.

Derivation discipline:

- `raw_link_role` preserved verbatim; `normalised_role` derived and separately reviewable.
- Identifiers are **two-part**. `occurrence_id` is derived from `claim + registry span + ordinal`
  and carries no authored prose, so it survives re-authoring; a separate `content_fingerprint`
  hashes the proposition and context, and its *change* is a drift signal to review, never an
  identity change. Rev. 2.1 specified a single content-derived ID over authored prose; the
  Phase-2 exercise measured it at **1 of 3 stable** under independent re-derivation and the scheme
  was corrected — see [`dismech_sidecar_phase2.md`](dismech_sidecar_phase2.md).
- `dedup_key`, `evidence_assertion_id` and `originating_claim_ids` are **computed** from the rows,
  never authored, so deduplication is reproducible rather than curated.
- Every candidate accounts for its outcome: `ATOMIZED` links to its occurrences, `NOT_EVIDENCE`
  links to its representation items, `ATOMIZATION_REQUIRED` links to neither and is counted as
  itself.

**Acceptance test for Phase 2: independent double re-derivation.** The sidecar is derived twice
from the registry text without reference to the first pass, and the two are compared on
identifiers, dedup groups and terminal states. Divergence means the derivation rests on judgement
that the specification has not captured, and the contract is amended before anything is built on
it.

Only after identity stability, reproducible deduplication and a migration path are demonstrated on
those three claims does a registry change become a `BATCH_COMMIT` proposal.

---

## 13. Success criteria for Phase 3 (exporter)

The exporter is not authorised by this document. When it is written, it must satisfy:

1. Read-only toward every LEGEND file. Output to `staging/` only.
2. Schema blob SHA verified against §0; fail closed on mismatch.
3. Every **assertion occurrence** terminates in exactly one of the nine Ledger-A states (§5.2),
   by the precedence of §5.3, with `unreached_tests[]` recorded.
4. All three identities of §5.4 asserted — occurrences, attachments, representation losses — and
   fail closed on any violation. Attachment count is **not** compared against assertion count.
5. Deduplication runs only over admissible occurrences (§5.5); every `originating_claim_ids`
   lineage reported, every excluded lineage counted under its own state.
6. Every exported occurrence reports **both** receipt event IDs — eligibility and locator
   extraction — its source locator, and the basis of each link direction.
6b. No occurrence with a locator decision is eligible without a locator-extraction receipt whose
   lineage validates (Rule A4).
7. Both link directions traversed (claim→paper and paper→claim); disagreements reported, never
   silently resolved.
8. Fail closed on any epistemic, direction, or confidence upgrade (Rules F1–F3), with regression
   tests (Rule F4).
9. `mechanism_confidence` explicitly emitted on **every** node; omission fails closed (Rule E2).
10. `ESTABLISHED` never emitted for a single-source proposition (Rule E1), never derived from
    claim status (Rule E3), and never emitted without its recorded six-criterion justification.
11. `modifier` omitted where the direction is undetermined (Rule C2).
12. No `conforms_to` for an `UNASSESSED` module (Rule M1).
13. No `SUPPORT`/`REFUTE` pairing failing the comparability gate (Rule C1).
14. Deterministic output: identical inputs produce byte-identical YAML and report.
15. No network calls at export time beyond the pinned-schema check.

---

## 14. Open questions for Phase 2 review

1. **OPEN.** Are assertion identities stable across an *independent* re-derivation, and are dedup
   groups computable without judgement? Partially answered by
   [`dismech_sidecar_phase2.md`](dismech_sidecar_phase2.md). What is established: identities are
   structural (`occurrence_id` = `claim + registry anchor + ordinal`, all read from the registry);
   the derivation reproduces exactly, verified separately for bytes and for parsed records; the
   predicted dedup collision reproduces by computation; and provenance — claim status, both link
   directions, receipt depth and lineage, artefact bytes — is read from the registries and the
   ledger rather than authored, with fingerprint mismatch a hard failure. What is **not**
   established: a genuinely independent second authoring pass, choosing its own anchors and
   propositions, has not been run. Reproducibility of a deterministic generator is not
   independence, and the anchor choice remains unvalidated judgement.

   Locator extraction from the two relevant already-read sources was performed in the same phase:
   14 of 19 occurrences reach `ELIGIBLE_FOR_EXPORT`, 3 terminate in `SOURCE_SUPPORT_NOT_FOUND` and
   2 remain in `ELIGIBILITY_DEBT`.
2. Do the five `UNASSESSED` modules conform on any node once §5-passing evidence exists, or does
   the WWOX evidence base simply not reach module level yet?
3. Given that the `Type` field undercounts composites (§11.1), should the claim registry carry an
   explicit sub-assertion structure — and if so, migrated how?
4. Is `PREMISE_TAG` genuinely unrepresentable, or does a `Discussion` of `kind: KNOWLEDGE_GAP`
   preserve enough of it to be worth emitting?
5. Should the orphan receipt (PMID 21212533) and the PAPER 056 ↔ CLAIM 030 link asymmetry be
   reconciled before, or independently of, the exporter?
6. Is there an upstream pattern for a paper-internal text/figure discrepancy (§3.4)? This is a
   question for the DisMech maintainers, not one this repository can answer alone.

---

## 15. What this specification does not decide

- Whether a pull request is ever opened.
- Whether the `/curate` red-team runs. It requires a paid provider by default; the skill also
  supports a non-paid backend, but either way it is out of the first cycle and needs an operator
  decision, not an inference from this document.
- Anything about PhEval. Formal evaluation of `phenotypic_neighbors.py` is a separate project
  with an unsolved benchmark-circularity problem: HPO annotations are the input and therefore
  cannot be the ground truth.
- Any change to the four current files. Nothing in this document is a commit candidate.
