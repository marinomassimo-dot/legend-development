# Session self-evaluation — intake wave 8, 2026-10-04, Scientist B

```yaml
actor: scientist (Group B)
branch: task/sci-B-20261004w8
papers: 6
context_policy: SOURCE_FIRST
```

## Executable gate

| Check | Result |
|---|---|
| `deepdive_manifest.py --pmid N --verify-artifacts --require-current-schema` × 6 | **PASS, 0 gaps** on all six |
| `fulltext_receipts.py verify` | **OK** — 320 chained receipts, tail anchored |
| `growth_anchors.py check` | **PASS** — backlog flagged at 13 candidates, expected: this wave added three |
| `scripts/public_release_gate.py` | **PASS, 0 blocks**; none of the flagged REVIEW lines is in a file of mine |
| `legend_lint.py .` | **BLOCK_BATCH_COMMIT — 7 `ORPHAN_COMPLETE_READ`, none of them mine** (see below) |
| `test_pathograph.py` | FAILED on drift → regenerated with the generator → **32 tests OK** |
| `test_link_targets.py` | FAILED on 5 wikilinks of mine → fixed → **OK** |
| `test_section_references.py`, `test_fresh_clone_reader_journey.py`, `test_tool_routing.py` | **OK** |
| `session_self_eval.py` | FAIL, for the same 7 pre-existing orphans |

### The LINT block is not this session's

`legend_lint.py` reports 7 `ORPHAN_COMPLETE_READ` on this branch. **Run in the root checkout on
`main`, the same check reports the same 7.** They are complete reads landed by other actors whose
PMIDs have no registry record; this branch neither created nor worsened them. Measured:

```
cd <worktree> && legend_lint.py . | grep -c ORPHAN_COMPLETE_READ   -> 7
cd <root, main> && legend_lint.py . | grep -c ORPHAN_COMPLETE_READ -> 7
```

None of the six PMIDs of this session is in that list, and `CC-20261004W8-B-REGISTRY-01` exists
precisely so that they never join it.

## Written diagnosis

**What went well.** The reading that mattered most was the one the brief named, and reading its
**figure panels and its uncropped-blot supplement** — rather than its text — is what produced the
finding. Two of the paper's own summary sentences weakened against its panels (the transcript
panel's case/control overlap; the overexpression blot's near-equal lanes). Wave 4's lesson held
again.

**What nearly went wrong, three times.**

1. **I almost took a premise on trust.** The assignment described B2 as a measured WWOX–ion-channel
   association bridging to excitability. Checking the *data* rather than the Discussion — parsing the
   supplementary workbook cell-wise from its XML parts — showed WWOX is one row in a sheet with **no
   numeric cell anywhere**. Had I read only the prose, I would have carried a "measured association".
2. **I almost accepted a capsid that was not there.** B4 was assigned as an AAV9 headroom record; it
   is AAV-DJ throughout. One grep of the Methods caught it.
3. **I wrote five broken wikilinks.** `test_link_targets.py` caught them: I linked to `PAPER`
   records that this wave only *proposes*. A provisional target is not a link target. Fixed to plain
   text, which is the registry's own convention.

**The weakest part of the session.** Two supplements were not retrieved (B3's Figures S1–S4 and
Table S1; B4's Figures S1–S11). For B3 this is not cosmetic: **the hepatic-protein finding — the
most consequential transferable result in the group — rests on the authors' Results sentences
describing Figure S1, not on the panel.** I declared it in the dossier, in the receipt coverage
(`supplementary: not_read`) and in the candidate's falsification clause, and I did not promote the
finding beyond what that provenance supports. But declaring a gap is not closing one.

**Why every receipt says `partial_fulltext_read`.** Figure panels were adjudicated only for B1. For
the other five the legends were read in full and no carried number lives in a panel, so
`coverage.figures` is `captions_only` — which the ledger writer refuses to call a complete read, and
correctly. No receipt overclaims.

## The micro-upgrade this session owes

**The gap:** I spent three tool calls discovering the manifest's `acquisition_recipe` schema by
failing against the validator (`must be an object`), and two more discovering that
`group_assessment.total_publications` must be an integer and `research_type` a closed vocabulary.
Both are documented, but in `fulltext_read_receipt.md` rather than in the validator's own error
text or in `deepdive_manifest.py --help`.

**The proportional fix, recorded as a capability gap rather than implemented here** (the harness is
not this actor's to edit mid-wave, and §21d reserves it): `deepdive_manifest.py`'s two BLOCK messages
should name the expected shape inline — the `acquisition_recipe` key set and the `research_type`
enumeration — exactly as the `research_type` message already does. One message already does it
right; two do not. That asymmetry is the whole fix.

**Second gap, with evidence:** a name-disambiguation hole. `group_assessment` wants a publication
count, and for B5 the senior author's surname-initial query returned 634 records — an ambiguous name.
The validator requires an integer, which pressures a reader to supply a wrong one. I recorded the
ambiguity in prose and counted a different, specific author instead. A `group_assessment`
`counts_measured` convention for ambiguous names would stop the next reader guessing.

## Honest statement of what this session did not do

- Did not retrieve two supplements, as above.
- Did not follow a single reference hop. B1 has 31 gene-direct references, 14 already read and 17
  queued in its manifest; following them would have answered a different question.
- Did not run `legend-locator-audit`, which B1 now owes: two text-versus-panel weakenings are exactly
  what the blind audit exists for.
- Did not record any receipt. The ledger is hash-chained and three scientists ran in parallel; all
  six receipts are prepared and dry-checked, and the integrator appends them in event order.
