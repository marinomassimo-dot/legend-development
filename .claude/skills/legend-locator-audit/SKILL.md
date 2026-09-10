---
name: legend-locator-audit
description: Blind adversarial audit of the verbatim locators behind a completed reading, before that reading may touch a consolidated baseline claim or justify a MAJOR working-model bump. The auditor receives only (proposition, quote, anchor) triples plus the source artefact — never the dossier, never the reader's name, never the conclusions. It answers two mechanical questions per triple — does the quote support the proposition, and does the source say MORE or LESS than the proposition claims. Use it when a reading narrows, reverses, corroborates or removes a `consolidated baseline` claim, when a commit candidate declares a MAJOR change class, or when the operator asks for "hostile review della lettura", "audit dei locator", "verifica critica della lettura". READ-ONLY toward every canonical file — it produces a verdict per triple, never an edit.
---

# LEGEND — blind locator audit

## What this is for

A reading can be careful, honest and still say more than its source. That failure is not
caught by any structural check: the receipt is valid, the manifest is complete, every locator
resolves — and the proposition still overshoots the sentence beneath it.

Measured on 2026-08-06. A complete, well-executed reading of PMID 30290271 produced a
dossier whose evidence boundary recorded *"NPY: whole hippocampus not significant"*. The paper
reports **no statistic at all** for that comparison — its running text says only *"Number of
NPY+ interneurons in the entire hippocampus is shown in Fig. 2D"*. The claim was a reading of
an unmarked panel, which is a legitimate observation and a different fact from a reported
test. Nothing in the pipeline objected. A second reader, checking the quote against the
source, found it in minutes.

That is what this audit exists to catch, and the reason it is cheap: **it never re-reads the
paper.**

## The two questions, and nothing else

For each `(proposition, quote, anchor)` triple, with the source artefact open:

1. **Does the quote support the proposition?** Not "is the proposition plausible" — whether
   *this sentence* carries *this claim*.
2. **Does the source say MORE or LESS than the proposition claims?** Overshoot is the common
   failure. Undershoot is the rarer and more dangerous one, because a narrowing nobody
   challenges becomes a silent false negative, and this repository treats those as the
   compounding loss.

Verdict per triple: `SUPPORTED` · `OVERSHOOT` · `UNDERSHOOT` · `NOT_IN_SOURCE` ·
`UNVERIFIABLE_SURFACE` (the quote is from a figure panel or an image and cannot be matched as
text — legitimate, but it must be *declared* as an attestation rather than a verified quote).

## 🔴 Blind by construction

The auditor receives:

- the triples,
- the source artefact,
- the target claim's current canonical text, if the reading touches one.

The auditor does **not** receive: the dossier, the reader's identity, the discovery-ledger
entry, the proposed commit candidate, or any narrative of what the reading concluded.

This is not ceremony. On 2026-08-06 two reviewers with full context passed the same pipeline
back and forth twice, each finding real defects in the other's work; a reviewer who did not
know who wrote what then found eight more in an hour. Knowing the author makes a reviewer
reconstruct intent instead of testing behaviour. Blindness is the active ingredient, not the
tooling.

Spawn the auditor as a separate agent with no session history. Give it the triples as data.

## When it is mandatory

- the reading **narrows, reverses, corroborates or removes** a `consolidated baseline` claim;
- the commit candidate declares **`Change class: MAJOR`**;
- the reading produces a **rejection** that closes a research direction — negatives get the
  same scrutiny as positives, per the premise/negative discipline in `CLAUDE.md`;
- 🔴 the reading **contradicts, corrects or replaces an existing persisted verbatim locator**,
  whatever claim status is involved. Added 2026-09-10; the evidence is below.

### Why the fourth trigger exists

The 2026-09-09 sweep produced six near-errors that were one step from landing. **Machines caught
none of them** (`2026-09-09_actor_retrospective.md` § 5.2). Blind auditors caught two — and were
run at all only because a `consolidated baseline` claim happened to be in scope on one actor's
readings.

The one this trigger is named after was caught by nobody but the reader. `scientist-b`, reading
Figure 6A of PMID 29724996 at the 667 px PMC rendering, made the counts ~14 vs ~1 of ~15 and
**began drafting a correction to an existing locator that was exactly right** — at 400 dpi the
bars resolve as stacked by genotype within each outcome category, and the persisted values 11/12
vs 4/18 are what the figure shows. In the actor's own words:

> *"The wrong edit would have been confident, well-argued, and would have passed every gate this
> repository owns."*

It touched no `consolidated baseline` claim, so no auditor was ever in the loop. What stood
between it and the ledger was one reader applying one procedural rule in the right order. **A
repository whose deepest control is "the reader remembered the rule" has a control gap at exactly
the point where an actor is most confident** — and an edit to an existing correct locator is the
highest-confidence act a reader performs, because the reader believes they are fixing an error.

### The cost, measured rather than feared

The objection below — a gate that fires on everything gets switched off — is real and this trigger
is scoped to survive it. **The audit need cover only the contradicted triples**, not the reading,
so its cost is bounded by how often a reading contradicts a persisted locator. Measured over the
eleven waves of the 2026-09-09 sweep, that is **three times**:

| Reading | Disposition | Audited? |
|---|---|---|
| `scientist-b`, PMID 18674750 `entries[21]` | landed, and correct | no |
| `scientist-b`, PMID 29724996 Fig 6A | withdrawn by the reader | no |
| `scientist-a`, PMID 34268881 `entries[14]` | corrected by the audit | **yes** |

**1 of 3 today; the target is 3 of 3.** Three audits across a day of eleven waves is not a gate
that fires on everything.

## When it is NOT required

Every other reading. A descriptive case report landing as a corpus record with no claim
change does not need an adversary, and demanding one would halve the throughput of the thing
that is already the bottleneck: at the time of writing, complete reads number in the dozens
against a corpus in the hundreds and a horizon in the hundreds of thousands.

A gate that fires on everything is a gate that gets switched off.

## What it produces

A table, one row per triple, and one line of disposition:

| # | Verdict | Proposition | What the source actually supports |
|---|---|---|---|

- **Any `NOT_IN_SOURCE`** blocks the reading from touching canonical state until resolved.
- **`OVERSHOOT` / `UNDERSHOOT`** must be answered before the `BATCH_COMMIT`: either the
  proposition is rewritten to what the source carries, or the divergence is argued explicitly
  in the commit candidate.
- **`UNVERIFIABLE_SURFACE`** is fine and must be *declared as such* — a figure reading is an
  attestation, and "no significance marker is drawn" is not "the difference was tested and
  found absent".

## What this is not

Not a re-reading, not a second derivation, not a scientific opinion on the paper. The
repository has already measured what independent re-derivation costs and yields: in the
DisMech Phase-2 experiment the atomisation axis was confirmed exactly by two blind reviewers,
while the deduplication axis stayed structurally uninformative *at any scale*. Reconstruction
belongs at export time, where being wrong means shipping. This audit belongs at reading time,
where being wrong means a claim.

## Related

`legend-session-self-eval` · `legend-deepdive` · `framework/protocols/fulltext_read_receipt.md`
· `LOCATOR_OVERSHOOT_GATE` in `framework/eval/learned_gates_registry.md`
