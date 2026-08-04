# Axis 3 — review result

> **Non-canonical.** The human judgement axis 3 requires, performed blind by a reviewer
> with no project context, then un-blinded. It changes no canonical file.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Reviewer:** fresh session, no repository access, sides shuffled per anchor
**Prompt:** [`dismech_axis3_blind_reviewer_prompt.md`](dismech_axis3_blind_reviewer_prompt.md) · **Key:** `data/dismech_axis3_blinding_key.json`
**Scope:** 11 anchors · 37 propositions · `A` = reference derivation, `B` = independent derivation

---

## The headline

The comparator reported **0 proposition matches**. The human reviewer found **10 `SAME`**,
and 20 of 37 propositions in some form of correspondence.

| Verdict | Count | |
|---|---:|---|
| `SAME` | 10 | same fact, different words |
| `SUBSUMED` | 6 | contained in a larger statement on the other side |
| `SPLIT` | 4 | corresponds to two or more taken together |
| `DIFFERENT` | 12 | not the same assertion |
| `ABSENT` | 5 | no counterpart |
| **total** | **37** | |

**Correspondence of some kind: 20 of 37 (54 %).** Axis 3's zero was an artefact of
conservative canonicalisation, exactly as rev. 13 argued — and the conservatism was the
right choice, because it is what let the off-by-one be visible instead of smoothed away.

## Independent confirmation of the split metric

The reviewer, blind, recorded split agreement at **7 of 11 anchors**. The mechanical count
in rev. 13 was **7 of 11**, on the same anchors. Two methods with nothing in common agreeing
exactly is the strongest signal in this exercise that the anchor realignment was correct.

---

## Finding 1 — the reference derivation under-split a sentence. Mine.

Every one of the five `ABSENT` verdicts falls on the independent side: it asserted five
things with no counterpart in the reference. Three of them come from a single anchor.

`CLAIM 035 | Summary | sent[1]` reads:

> *"Il legame blocca la fosforilazione di Tau su S396/S404 (ma non sul sito MKK4 S422),
> **ripristina** l'assemblaggio dei microtubuli Tau-dipendente **e promuove** la crescita
> neuritica indotta da RA."*

Three coordinated assertions: blocks phosphorylation · restores microtubule assembly ·
promotes neurite outgrowth. The reference derivation produced **one** proposition, covering
only the first. The independent reader produced **three**.

Rule 4 of the atomization contract says a proposition is one proposition, and that
*"conjunctions are the diagnostic: and, while, thereby"*. The reference derivation broke its
own rule; the independent run applied it correctly. Two of that claim's findings — the
microtubule rescue and the neurite-outgrowth effect — were silently absent from the
reference sidecar.

## Finding 2 — an inference presented as data. Also mine.

At `CLAIM 035 | Summary | sent[3]` the reviewer marked both sides `DIFFERENT`, and its
reason for the reference proposition is precise:

> *"'GSK3β output falls' is an interpretation, while [the other] reports specific Tau
> phosphorylation changes."*

The reference proposition reads *"Phospho-GSK3β-S9 is unchanged while GSK3β output falls."*
What the source measures is a fall in Tau S396/S404 phosphorylation; *output falls* is a
step of abstraction the sentence does not take. A blind reviewer with no knowledge of this
project's epistemic discipline applied it more strictly than the derivation did.

## Finding 3 — a deliberate correction is indistinguishable from an omission

`β9`, *"WWOX binds GSK3β through its ADH/SDR domain"*, was marked `ABSENT`: no reference
proposition says it. That is true, and it is deliberate — rev. 2 re-scoped that statement to
*"residues 388–407 are required"* after reading the source, because the domain-level claim
is our framing and not the paper's.

The comparison cannot tell a correction from an oversight. Nothing in the instrument can:
both look like a missing proposition. Only the derivation's own record of *why* it re-scoped
distinguishes them, which is an argument for keeping that record.

## Finding 4 — the verdict vocabulary is missing a value. My defect.

`SUBSUMED` has no reciprocal. When the reviewer judged that one proposition contains
another, it could label the contained one `SUBSUMED` but had no term for the containing one,
and fell back on `DIFFERENT`. Three verdicts are this artefact:

| anchor | contained | containing, forced to `DIFFERENT` |
|---|---|---|
| 1 | β1 `SUBSUMED` | α1 |
| 2 | α3 `SUBSUMED` | β2 |
| 7 | α14 `SUBSUMED` | β11 |

Corrected, `DIFFERENT` falls from 12 to **9**, and correspondence rises to **23 of 37
(62 %)**. A vocabulary needs `SUBSUMES` before the next run.

---

## What this decides about the contract

Rev. 13 posed the question: mostly `SAME` means only the *form* of a proposition is
unspecified; mostly `DIFFERENT` or `SPLIT` means the contract under-determines what an
assertion is.

The answer is **neither cleanly, and the split tells you why**:

- **Where both readers split the same way, they largely agree.** At the 7 anchors with
  matching splits, `SAME` dominates. Wording differs and meaning does not.
- **Where the splits differ, the divergence is not a disagreement about meaning but about
  granularity** — and at anchor 8, the granularity rule already exists and was simply not
  followed.

So the contract is not under-determined in the way rev. 12 suggested. What failed is
*compliance* with a rule it already contains, and the failure is in the reference
derivation. The repair is not a new rule: it is applying rule 4 and re-deriving.

## What must not be concluded

That the independent run is "better". It produced 21 propositions to 16, and more is not
automatically right — some of its extras may over-split, and the comparison cannot tell.
What is established is narrower and firmer: **at one anchor the reference derivation
collapsed three coordinated assertions into one, and two findings were lost by it.**

## Next

1. Re-derive `CLAIM 035 | Summary | sent[1]` at the correct granularity — three assertions,
   with locators for each. The two missing ones need quotes from PAPER 056, which is already
   read and receipted.
2. Re-examine every reference anchor whose sentence contains a coordinating conjunction;
   anchor 8 is unlikely to be the only one.
3. Add `SUBSUMES` to the verdict vocabulary.
4. Reconsider the `GSK3β output falls` proposition: either restate it as the measured fall
   in Tau S396/S404 phosphorylation, or mark the abstraction as the inference it is.
5. Axis 4 becomes measurable for the first time — there is now a non-empty correspondence
   set — but only over the 10 `SAME` pairs, which is a small universe. Do it after step 1.

## Raw reply

Preserved verbatim in [`data/dismech_axis3_review_raw_reply.md`](data/), because a tally can
be recomputed and a justification cannot be reconstructed.

## Related

[`dismech_axis3_review_sheet_blinded.md`](dismech_axis3_review_sheet_blinded.md) · [`dismech_independent_comparison_rev13.md`](dismech_independent_comparison_rev13.md) · [`dismech_export_spec.md`](dismech_export_spec.md)
