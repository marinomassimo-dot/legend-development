# Independent comparison — rev. 13, after ordinal realignment

> **Non-canonical.** A re-measurement of the rev. 12 comparison after correcting three
> defects in the anchor contract. It re-authors nothing: the independent run's output is
> untouched and still hashes to its attestation.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Supersedes:** the conclusions of `dismech_independent_comparison_rev12.md`
**Inputs:** reference sidecar (49 records) · realigned independent derivation (73 records)
**Independent run:** `ec117b0a…`, `contamination_status: CLEAN`, **byte-identical, not modified**

---

## What rev. 12 measured, and what it actually found

Rev. 12 reported no proposition correspondence, 7 of 23 shared anchors, and concluded that
assertion identities are unstable across independent derivations and that atomization is
under-specified.

Three defects in the anchor contract were confounding that measurement. **All three are
mine**, in the design and the reader; none is a fault of the independent run.

| # | Defect | Effect |
|---|---|---|
| 1 | The anchor format never declared whether `sent[n]` is zero- or one-based | The reference indexed from 0, the independent run from 1. **31 of 31** anchors pointed one sentence late |
| 2 | A field heading carrying markup — `🔴 **\`PREMISE_TAG\` sul claim esistente**` — resolved only in verbatim form | Two anchors written in the plain form were rejected as a missing field |
| 3 | A field body ran to the next heading, but not to a horizontal rule | The last field of a claim swallowed the `---` separator, so its final sentence never compared equal |

The off-by-one was confirmed on **every** record before anything was transformed: 31 of 31.
The realignment tool refuses to write on a single counterexample, and it did refuse twice
— once for defect 2, once for defect 3 — until the reader was fixed.

---

## The four axes, re-measured

| Axis | Rev. 12 | Rev. 13 | Reading |
|---|---:|---:|---|
| 1 — anchor selection (shared) | 7 of 23 | **11 of 19** | Jaccard 0.304 → **0.579** |
| 2 — atomisation entries | 7 | 11 | more anchors comparable |
| 3 — unambiguous proposition matches | 0 | **0** | unchanged (see below) |
| 3 — structural ID collisions | 7 | **16** | now attributable, not confounded |
| 4 — deduplication | NOT_MEASURABLE | NOT_MEASURABLE | axis 3 correspondence still empty |

**New measurement the axes did not compute: split agreement.** At the 11 shared anchors,
the two runs produced the *same number of occurrences* at **7 of 11 (63 %)**.

```
=  2 vs 2   CLAIM 016|Summary|sent[0]           =  3 vs 3   CLAIM 035|Summary|sent[0]
=  1 vs 1   CLAIM 016|Meccanismo…|sent[1]       =  1 vs 1   CLAIM 035|Summary|sent[2]
=  2 vs 2   CLAIM 024|Summary|sent[0]           =  1 vs 1   CLAIM 035|Summary|sent[3]
                                                =  2 vs 2   CLAIM 035|Summary|sent[4]
≠  1 vs 2   CLAIM 016|Meccanismo…|sent[0]       ≠  1 vs 3   CLAIM 035|Summary|sent[1]
≠  1 vs 2   CLAIM 024|Precisazione…|sent[0]     ≠  1 vs 2   CLAIM 024|Precisazione…|sent[1]
```

---

## The finding that changes the conclusion

Axis 3 still reports zero matches. Read the records, and that number does not mean what it
appears to mean.

`CLAIM 016|Summary|sent[0]` — both runs split it into exactly two assertions:

| | |
|---|---|
| reference | *"In Wwox-null mice GSK3beta is elevated in cortex, hippocampus and cerebellum"* |
| independent | *"GSK3β abundance is elevated in cortex, hippocampus, and cerebellum of Wwox-null mice."* |
| reference | *"Lithium suppresses PTZ-induced seizure susceptibility in the Wwox-null mouse"* |
| independent | *"Lithium significantly suppresses PTZ-induced seizure susceptibility in Wwox-null mice."* |

Two readers, the same registry sentence, the same decomposition, the same two facts. They
differ in word order, in *abundance*, in *significantly*, in an Oxford comma, in
mouse/mice. Canonicalisation v1 folds `GSK3beta → GSK3β` and normalises dashes and
whitespace — and correctly refuses to fold word order or drop a qualifier, because doing
so is how *does not bind* and *binds* collapse into one.

**So axis 3 is measuring wording, not meaning, and it cannot separate "a different
assertion" from "the same assertion phrased differently".** The design anticipated this —
it requires every divergence to become a review item, precisely because the comparator is
not a semantic authority. What the rev. 12 report did was present the count as a result.

## What each side got right and wrong

| Claim | Verdict |
|---|---|
| Rev. 12: *"no semantically corresponding propositions"* | **Wrong on the reading.** At least one anchor shows two pairs any reader would call the same fact |
| Rev. 12: *"anchors 7/23, Jaccard 0.304"* | **Artefact.** 11/19 and 0.579 after realignment |
| Rev. 12: *"IDs do not stably identify the same assertion"* | **Now supported**, and better than before: 16 collisions at *aligned* anchors, no longer confounded by the offset |
| Rev. 12: *"the measured problem is under-specified atomization"* | **Partly.** Split agreement is 63 %, not zero. What is genuinely unspecified is the *form* of a proposition — nothing tells two faithful readers to phrase the same fact the same way |
| My hostile review: *"the divergence is an off-by-one, not a disagreement"* | **Over-claimed.** The off-by-one explained the anchor divergence; it did not explain the proposition divergence, which survives the fix |

## What is actually under-specified

1. **The anchor's ordinal base** — fixed, declared, and covered by seven regressions.
2. **The heading form** — fixed: decoration-free labels now resolve.
3. **The field boundary** — fixed: a field ends at a horizontal rule too.
4. **The proposition's form** — *open*. Two readers can be equally faithful and equally
   atomic and still write different sentences. Until there is a rule — or a review step
   that a human performs — axis 3 will keep reporting zero and meaning nothing by it.

## What must not be done

Widening canonicalisation until these pairs match. It would make this comparison green and
destroy the property that keeps it honest: the same widening that folds *significantly*
would eventually fold a negation or a direction. The design fails toward
under-canonicalisation deliberately, and that choice is what let the off-by-one be visible
at all rather than smoothed into false agreement.

## Next

1. Axis 3 reports a **review queue**, not a match count: `IDENTICAL`, `CANONICAL_CANDIDATE`,
   `DIVERGENT`, each with both texts side by side, and no aggregate.
2. Someone reads the 11 shared anchors and records, per pair, whether it is the same
   assertion. That is the measurement §14.1 actually wants, and no comparator can produce it.
3. Only then is there anything to say about atomization, and only then can axis 4 run.

## Related

[`dismech_independent_derivation_design.md`](dismech_independent_derivation_design.md) · [`dismech_blind_derivation_contract.md`](dismech_blind_derivation_contract.md) · [`dismech_independent_comparison_rev12.md`](dismech_independent_comparison_rev12.md) · [`data/dismech_second_derivation_realigned_016_024_035.jsonl`](data/)
