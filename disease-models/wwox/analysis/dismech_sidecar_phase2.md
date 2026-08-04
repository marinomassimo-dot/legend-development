# Phase-2 sidecar — CLAIM 016 / 024 / 035

> **Non-canonical.** A derivation exercise against the contract in
> [`dismech_export_spec.md`](dismech_export_spec.md). It changes none of the four current files,
> promotes nothing, and is not a commit candidate.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Revision:** 7, contract realigned
**Artefact:** [`data/dismech_sidecar_016_024_035.jsonl`](data/) — 49 records (a `derivation_manifest` plus 48), one JSON object per
line, `record_kind` ∈ `assertion_candidate` | `assertion_occurrence` | `representation_item`
**Scope:** CLAIM 016, 024, 035 only

---

## What changed

Revision 1 derived the sidecar and found every occurrence blocked at the last gate: no verbatim
locator existed anywhere in the canonical state. Revision 2 extracted those locators from the two
source artefacts. Revision 3 corrected the emission state, split the two quote-less conditions,
added both receipt lineages, and replaced authored span labels with exact registry anchors.
Revision 4 hardened the generator itself. Revision 5 made it **reproducible in public**: the
sidecar had been recording a hash measured on the local full-text corpus, so in a clean export —
which has no `files/` — the records diverged and both verify modes failed. That went unnoticed
because the new test was not among the release runner's targets, which is also why revision 4's
claim of a green clean export was wrong.

| | Rev. 1 | Rev. 3 |
|---|---:|---:|
| `ELIGIBLE_FOR_EXPORT` | 0 | **14** |
| quote absent | 17 | 3 |
| `ELIGIBILITY_DEBT` | 2 | 2 |
| Evidence assertions formed | 0 | **13** |

Fourteen occurrences now pass every gate and group into thirteen evidence assertions — the
deduplication rule is exercised end-to-end for the first time, not merely diagnosed.

**`ELIGIBLE_FOR_EXPORT`, not `EXPORTED`.** Nothing has been written to any output: no node is
emitted, no YAML exists, no attachment is counted. Revision 2 of this report used `EXPORTED` for
rows that had merely passed the gate, which the specification defines as "present in the output".
Corrected here and in the contract.

---

## Derivation, persisted

The derivation is no longer ad hoc. The script [`derive_dismech_sidecar.py`](./scripts/derive_dismech_sidecar.py),
held beside this report under `analysis/scripts/`, reads the claim registry, resolves each
candidate's anchor, and computes every identifier, key, grouping and total. Its hash contract is recorded in the output: `sha256` over the UTF-8 encoding of the parts
joined by `|`, no canonicalisation, truncated to 12 hex characters.

**No fail-open paths.** Two checks previously reported success while verifying nothing, and both
are now closed with negative tests. A locator without a receipt documenting its extraction can no
longer be eligible — it terminates in `LOCATOR_PROVENANCE_MISSING`; with the locator receipts
stripped from the ledger, all 14 eligible occurrences correctly fall out. And
`--audit-local-sources` distinguishes *verified* from *absent*: it exits 0 only when every expected
artefact was compared, 1 on mismatch, and **2 when artefacts are missing**, because absence is not
a pass. In a clean export it exits 2, as it should.

A bare wikilink is no longer evidence. `read_link` now separates a paper named in the claim's
`Source` field (`SUPPORTING`) from one merely cross-referenced elsewhere in the claim
(`UNQUALIFIED_REFERENCE`). CLAIM 016 references PAPER 019 by wikilink while its `Source` field
names "Cheng et al. 2020" in prose; the field text is recorded on the occurrence so the ambiguity
is visible to a reviewer rather than resolved by a guess.

**Environment independence.** The sidecar records the artefact fingerprint *declared by the
receipt*, never one measured on disk. Re-hashing the local corpus is a separate command,
`--audit-local-sources`, and its result never enters a record. Verified: in a clean export built
from tracked files only, `--verify-bytes` reports `BYTES IDENTICAL: 49 records`, the twenty
adversarial tests pass, and `run_release_regressions.py` returns `PASS (39 targets)` — the new
test now being one of them.

**Provenance is read, not authored.** Claim status comes from the claim registry; PMID and both
link directions from the paper registry; receipt depth, eligibility lineage and locator-extraction
lineage from the receipt ledger; and the artefact's bytes are **re-hashed on disk** and compared
with the receipt fingerprint, with a mismatch aborting the run. Revision 3 held these as authored
constants, so a registry change could have left `--verify` passing on stale eligibility. Only the
anchors, the propositions, their context and epistemic type, and the verbatim snippets remain
authored — those are judgement, and they are what the sidecar exists to expose for review.

**Two verification modes, because they answer different questions.**
`--verify-bytes` compares the serialised bytes against one declared serialisation;
`--verify-semantic` compares the parsed records. Revision 3 had a single `--verify` that compared
parsed objects while printing *"byte-for-byte"* — a differently serialised file passed it.
Confirmed on a reformatted JSONL: `--verify-bytes` exits 1, `--verify-semantic` exits 0.

The hash contract is now **inside the sidecar**, as a `derivation_manifest` first record carrying
the algorithm, the dedup-key components, the identity components and the provenance sources.
Revision 3's report claimed it was "recorded in the output" when it appeared only on stdout.

Anchors fail closed: a missing claim, a missing field or an out-of-range sentence ordinal aborts
rather than degrading. Twenty-eight adversarial tests in
[`test_derive_dismech_sidecar.py`](./scripts/test_derive_dismech_sidecar.py) cover the defects
that actually shipped: two distinct locators must not collapse into one dedup key, the 016/035
merge must still occur, provenance must come from the registries, a reformatted JSONL must fail
the byte check *when the CLI is actually invoked*, a claim-only link must keep a supporting role,
the locator receipt must descend from the complete read it claims, no environment-dependent value
may enter a record, and no record may be marked `EXPORTED`.

## Sources and their integrity

Extraction ran against the artefacts whose SHA-256 match the complete-read receipts, re-verified
at extraction time:

| Paper | Artefact | SHA-256 | Occurrences |
|---|---|---|---:|
| PAPER 055 · PMID 35716775 | `PMID35716775_Rotem-Bamberger2022.pdf` | `304a4d30…921673` ✅ | 5 |
| PAPER 056 · PMID 22193544 | `PMID22193544_Wang2012_PMC_JATS.xml` | `eb6f568d…388268` ✅ | 12 |
| PAPER 019 · PMID 32000863 | none — no receipt in the ledger | — | 2 |

For PAPER 056 the authoritative artefact is the **JATS XML**, which is the receipt's primary
locator; the PDF in the same directory has a different hash and was not used for quotation.

Two targeted receipts were recorded — `FTR-20260804-35716775-04` and
`FTR-20260804-22193544-04` — at `evidence_depth: queried_not_full_read`, linked to the prior
complete-read receipts with `reread_reason: explicit_operator_request`. **No new complete read is
claimed.** Coverage is `not_read` throughout by design: locating and quoting passages already
covered by a prior complete read is not itself a read, and the vocabulary has no value for
"queried" — inventing one would have weakened the very distinction the ledger exists to keep.
Ledger state: 36 chained events, tail anchored, `verify` OK.

---

## Result 1 — three inferences have no verbatim support in their own source

The three remaining occurrences are **all `INFERENZA`**, and all failed for the same reason: the
cited paper contains no statement supporting them. Their state is `SOURCE_SUPPORT_NOT_FOUND`, not
`LOCATOR_NOT_EXTRACTED` — the search was carried out and completed negatively. Revision 2 filed
them under a single "locator missing" state, which made a finished negative verification look like
an outstanding task someone could still discharge.

| Occurrence | Claim | Why no locator |
|---|---|---|
| WW-domain variants should not be interpreted domain-by-domain in isolation | 024 | The source discusses only engineered mutations. It contains no statement about disease-variant interpretation anywhere |
| A WWOX-DEE study using phospho-S9 as a GSK3β readout will produce a false negative | 035 | The source never examines pS9 as a readout in a WWOX-deficient setting |
| The mechanism transfers to human neurons and to WWOX-DEE | 035 | No WWOX-DEE allele and no human neuron appears anywhere in the source |

None of these is wrong. Each is a defensible inference LEGEND drew — and two of them are among
the most useful things in the claim. But **none can be exported as evidence attributed to that
paper**, and this is exactly the failure mode the reviewer warned about before extraction began:
under schema pressure, an inference acquires a citation it does not have.

Their route upstream is a `Discussion` (`kind: INTERPRETATION`), or a node whose `EvidenceItem`
cites the underlying datum with `supports: PARTIAL` and an `explanation` that states the
inferential step. Not a `SUPPORT` on the inference itself.

## Result 2 — the source rewrote four propositions, and the identity scheme held

Extraction is not transcription: reading the actual sentence changed what four propositions could
honestly say.

| Occurrence | Authored from the registry | Rewritten against the source |
|---|---|---|
| `OCC-dd4b920216b5` (035) | WWOX binds GSK3β *through the ADH/SDR domain* | WWOX amino acids **388–407** are required for the interaction with GSK3β |
| `OCC-436d1e3fc758` (016) | *(same as above)* | *(same rewrite)* |
| `OCC-ce440979ee2c` (035) | The binding segment is **388–407**, homologous to Axin/FRAT/GSKIP | WWOX **388–412** contains the FXXXLI/VXRLE motif conserved in GSKIP, Axin and FRAT |
| `OCC-73cbabfc3be7` (024) | WW2 is not a canonical standalone PPxY-binding domain | WW2 lacks significant inherent affinity for the ErbB4 PY3 motif, yet the tandem binds PY3 more strongly than isolated WW1 (30 vs 78 μM) |

The third row is a real precision gain the registry had blurred: the paper reports **388–412** for
the sequence homology and **388–407** for the experimentally required segment. LEGEND had merged
the two into one number.

**The two-part identity worked exactly as designed.** All **19 of 19** `occurrence_id` values
survived the rewrite, because they carry no authored prose. Only the `content_fingerprint` values
changed — the drift signal doing its job, not an identity break. Under rev. 2.1's single
content-hash scheme, four identifiers would have silently changed and the dedup group would have
split.

(The identifiers shown are those of revision 3, in which the identity basis moved from
`claim + authored span label + ordinal` to `claim + exact registry anchor + ordinal`. That change
re-based every identifier once, deliberately and in a single step; it is the last such change the
scheme admits, because the anchor is now read from the registry rather than authored.)

## Result 3 — deduplication now runs, and holds through the rewrite

```
DK-a92ddbd26e6f  ←  OCC-dd4b920216b5 (CLAIM 035) + OCC-436d1e3fc758 (CLAIM 016)
     evidence_assertion_id: EA-138f70c17316
     proposition: "WWOX amino acids 388-407 are required for the interaction with GSK3beta"
     source: PAPER 056 · same context, epistemic type and evidence relation
```

14 eligible occurrences → 13 evidence assertions. Both members of the pair were rewritten
identically against the same sentence, so the group survived the rewrite intact —
`originating_claim_ids: [016, 035]`.

## Result 4 — a registry claim checked out, and one nuance was recovered

CLAIM 035 and PAPER 056 both assert an endogenous co-immunoprecipitation from mouse brain. It is
present: *"immunoprecipitation was performed in mouse brain extracts to verify the physiological
interaction between WWOX and GSK3β. Figure 2e shows that both GSK3β and WWOX were precipitated by
anti-GSK3β or anti-WWOX antibodies."* The registry is correct.

Two occurrences were downgraded from `SUPPORT` to `PARTIAL` on inspection:

- **S9 independence.** The source's pS9 observation — *"the phosphorylation levels of
  phospho-GSK3β S9 and phospho-β-catenin remained normal"* — is made under **RA-induced
  differentiation**, not inside the WWOX-mediated inhibition experiment. The claim is supported,
  but indirectly.
- **Linear-pathway reading.** *"our results connect WWOX, GSK3β and Tau in an exclusive, direct
  manner"* is the authors' own interpretation in the Discussion, not a result.

And one occurrence gained support that had not been anticipated: the de-repression reading in
CLAIM 016 is partially supported by *"SH-SY5Y cells in which WWOX expression was reduced by RNAi
showed increased pTau S396 levels"* — a loss-of-function observation the registry had not
connected to that statement.

---

## Accounting

| Ledger A state | Occurrences |
|---|---:|
| `ELIGIBLE_FOR_EXPORT` | 14 |
| `SOURCE_SUPPORT_NOT_FOUND` | 3 |
| `ELIGIBILITY_DEBT` | 2 |
| `STATUS_INELIGIBLE` · `ATOMIZATION_REQUIRED` · `IDENTIFIER_UNRESOLVED` · `LINK_ROLE_NON_SUPPORTING` · `LOCATOR_NOT_EXTRACTED` · `LOCATOR_PROVENANCE_MISSING` | 0 |
| **total** | **19** |

| Check | Result |
|---|---|
| Ledger A: `occurrences == ELIGIBLE_FOR_EXPORT + Σ(eight loss states)` | ✅ 19 = 14 + 5 |
| Ledger B: every representation item carries a state | ✅ 8 items, all `SCHEMA_LOSS` |
| Candidate closure: `ATOMIZED` ⟺ occurrences; `NOT_EVIDENCE` ⟺ items | ✅ |
| Attachments counted separately from assertions | ✅ 0 nodes emitted, 0 attachments |

| Record kind | Count |
|---|---:|
| `derivation_manifest` | 1 |
| `assertion_candidate` | 21 — 14 `ATOMIZED`, 6 `NOT_EVIDENCE`, 1 `ATOMIZATION_REQUIRED` |
| `assertion_occurrence` | 19 |
| `representation_item` | 8 |

The single `ATOMIZATION_REQUIRED` candidate is CLAIM 016's *"GSK3β acts as an amplifier rather
than a standalone upstream driver"*: two sources, not separable without interpretation, so it
never becomes an occurrence. Ledger B holds three transferability tiers, two clinical caveats, one
`PREMISE_TAG` and two receipt-lineage records.

## What this still does not establish

- **§14.1 remains OPEN.** Revision 3 replaced the authored span labels with exact registry
  anchors, so `raw_registry_span` is now *read out of the registry* and an anchor that does not
  resolve is a hard failure (verified: a bad sentence ordinal, an absent field and an absent claim
  all abort). `occurrence_id` derives from `claim + anchor + ordinal` and contains no authored
  prose, so any second pass choosing the same anchors gets the same identifiers however it words
  the propositions. The derivation re-derives exactly, verified separately for bytes and for parsed records (49 records). But that is
  *reproducibility*, not *independence*: a genuinely independent second authoring pass — different
  reader, same registry — has not been run, and until it has, the anchor choice itself remains
  unvalidated judgement.
- Nothing about the other 32 claims.
- The propositions remain a proposal for review. A second reviewer may atomize differently; the
  `content_fingerprint` exists so that such a difference is visible rather than silent.
- No node has been emitted and no YAML written. Fourteen exportable occurrences is a precondition
  for a dry run, not a dry run.

## Next

1. **Independent second derivation.** A second pass over the same registry, without reference to
   this one, choosing its own anchors and propositions; compare identifiers, dedup groups and
   terminal states. This is the one thing standing between §14.1 and closure.
2. Decide the upstream route for the three `SOURCE_SUPPORT_NOT_FOUND` inferences — a `Discussion`
   of `kind: INTERPRETATION`, or a node whose `EvidenceItem` cites the underlying datum with
   `supports: PARTIAL` and an `explanation` stating the inferential step.
3. Only then a Phase-3 exporter dry run.

## Related

[`dismech_export_spec.md`](dismech_export_spec.md) · [`DISMECH_INTEGRATION.md`](../../../DISMECH_INTEGRATION.md) · [`DATA_SOURCES.md`](../../../DATA_SOURCES.md) · [`claim_registry_current.md`](../registries/claim_registry_current.md) · [`paper_registry_current.md`](../registries/paper_registry_current.md)
